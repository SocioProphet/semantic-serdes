#!/usr/bin/env python3
"""Validate Smart ETL v0.1 contract examples.

This validator intentionally checks both JSON Schema conformance and cross-graph
planning invariants that JSON Schema alone cannot express: target consistency,
DAG acyclicity, policy readiness, placement coverage, evidence completeness,
and failed-branch capture for blocked plans.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover
    print(f"missing dependency: {exc}", file=sys.stderr)
    sys.exit(2)

REQUIRED_RECEIPT_TOKENS = [
    "search",
    "sql_parse",
    "policy",
    "workflow_plan",
    "placement",
    "dry_run",
    "evidence_bundle",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text())


def load_schemas(schema_dir: Path) -> dict[str, Any]:
    return {path.name: load_json(path) for path in schema_dir.glob("*.schema.json")}


def make_validator(schema: dict[str, Any], schemas: dict[str, Any]) -> jsonschema.Draft202012Validator:
    store = {name: value for name, value in schemas.items()}
    store.update({value.get("$id", name): value for name, value in schemas.items()})
    resolver = jsonschema.RefResolver.from_schema(schema, store=store)
    return jsonschema.Draft202012Validator(schema, resolver=resolver)


def add_error(errors: list[str], code: str, message: str) -> None:
    errors.append(f"{code} {message}")


def validate_derivation(plan: dict[str, Any], errors: list[str]) -> None:
    intent_target = plan["intent"]["target_dataset_ref"]
    derivation = plan["logical_derivation"]
    asset_datasets = set(plan["asset_graph"]["dataset_refs"])

    if derivation["target_dataset_ref"] != intent_target:
        add_error(errors, "E_DERIVATION_003", "derivation target does not match intent target")
    if intent_target not in asset_datasets:
        add_error(errors, "E_DERIVATION_002", "target dataset missing from asset graph")
    for src in derivation["source_dataset_refs"]:
        if src not in asset_datasets:
            add_error(errors, "E_DERIVATION_001", f"source dataset missing from asset graph: {src}")
    if "select_star" in derivation.get("unsafe_constructs", []):
        add_error(errors, "E_DERIVATION_006", "select_star is blocked for governed derivations")

    target_columns = [c for c in derivation.get("target_columns", []) if c != "*"]
    lineage_targets = {edge.get("target_column") for edge in derivation.get("column_lineage", [])}
    if plan.get("status") in {"validated", "ready_for_submission", "submitted"}:
        missing = sorted(set(target_columns) - lineage_targets)
        if missing:
            add_error(errors, "E_DERIVATION_009", f"target columns missing lineage: {missing}")


def validate_policy(plan: dict[str, Any], errors: list[str]) -> None:
    decisions = plan.get("policy_graph", {}).get("policy_decisions", [])
    if not decisions:
        add_error(errors, "E_POLICY_001", "plan has no policy decisions")
        return
    for decision in decisions:
        checked = set(decision.get("permissions_checked", []))
        for required in ("read", "derive"):
            if required not in checked:
                add_error(errors, "E_POLICY_008", f"permission not checked: {required}")
        if decision.get("decision") == "deny" and plan.get("status") in {"validated", "ready_for_submission", "submitted"}:
            add_error(errors, "E_POLICY_003", "denied policy decision cannot be ready, validated, or submitted")
        if decision.get("decision") == "requires_rewrite" and not decision.get("required_rewrites"):
            add_error(errors, "E_POLICY_006", "requires_rewrite decision lacks required_rewrites")
        if decision.get("denied_columns") and plan.get("status") in {"validated", "ready_for_submission", "submitted"}:
            add_error(errors, "E_POLICY_004", "denied columns present while plan is marked ready, validated, or submitted")


def validate_dag(plan: dict[str, Any], errors: list[str]) -> None:
    graph = plan.get("execution_graph", {})
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])
    node_ids = {node.get("step_id") for node in nodes}
    for edge in edges:
        if edge.get("from_step_id") not in node_ids or edge.get("to_step_id") not in node_ids:
            add_error(errors, "E_DAG_001", "edge references unknown workflow step")

    adjacency = {node_id: [] for node_id in node_ids}
    for edge in edges:
        if edge.get("from_step_id") in adjacency:
            adjacency[edge["from_step_id"]].append(edge.get("to_step_id"))

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            add_error(errors, "E_DAG_002", "cycle detected")
            return
        if node in visited:
            return
        visiting.add(node)
        for nxt in adjacency.get(node, []):
            if nxt:
                visit(nxt)
        visiting.remove(node)
        visited.add(node)

    for node in list(node_ids):
        if node:
            visit(node)
    if graph.get("dag_status") != "acyclic":
        add_error(errors, "E_DAG_003", "workflow dag_status must be acyclic for v0.1 examples")


def validate_placement(plan: dict[str, Any], errors: list[str]) -> None:
    executable_steps = {
        f"workflow_step:{node['step_id']}"
        for node in plan.get("execution_graph", {}).get("nodes", [])
        if node.get("executable")
    }
    placements = plan.get("placement_graph", {}).get("placement_decisions", [])
    placed_steps = {p.get("step_ref") for p in placements}
    missing = sorted(executable_steps - placed_steps)
    if missing:
        add_error(errors, "E_PLACEMENT_001", f"executable steps missing placement decisions: {missing}")
    for placement in placements:
        if placement.get("selected_engine") not in placement.get("engine_candidates", []):
            add_error(errors, "E_PLACEMENT_002", "selected engine is not in engine_candidates")
        if placement.get("decision_status") == "blocked" and plan.get("status") in {"validated", "ready_for_submission", "submitted"}:
            add_error(errors, "E_PLACEMENT_003", "blocked placement cannot be ready or submitted")


def validate_evidence(plan: dict[str, Any], errors: list[str]) -> None:
    joined = " ".join(plan.get("evidence_graph", {}).get("receipt_refs", []))
    for token in REQUIRED_RECEIPT_TOKENS:
        if token not in joined:
            add_error(errors, "E_EVIDENCE_001", f"missing required receipt token: {token}")


def validate_failed_branches(plan: dict[str, Any], errors: list[str]) -> None:
    denied = any(d.get("decision") == "deny" for d in plan.get("policy_graph", {}).get("policy_decisions", []))
    blocked = plan.get("status") in {"policy_blocked", "placement_blocked", "failed"} or denied
    if blocked and not plan.get("failed_branches"):
        add_error(errors, "E_FAILED_BRANCH_001", "blocked or denied plan missing FailedPlanBranch")
    for branch in plan.get("failed_branches", []):
        if branch.get("should_index_for_future") and not branch.get("reusable_lesson"):
            add_error(errors, "E_FAILED_BRANCH_004", "indexed failed branch missing reusable_lesson")


def validate_example(path: Path, schemas: dict[str, Any]) -> tuple[bool, list[str]]:
    bundle = load_json(path)
    errors: list[str] = []
    plan = bundle.get("smart_etl_plan")
    if not plan:
        return False, ["E_LOAD_001 example missing smart_etl_plan"]

    validator = make_validator(schemas["smart-etl-plan-v0.1.schema.json"], schemas)
    for exc in sorted(validator.iter_errors(plan), key=lambda e: list(e.path)):
        location = "/".join(map(str, exc.path)) or "<root>"
        add_error(errors, "E_SCHEMA_001", f"{location}: {exc.message}")

    if not any(e.startswith("E_SCHEMA") for e in errors):
        validate_derivation(plan, errors)
        validate_policy(plan, errors)
        validate_dag(plan, errors)
        validate_placement(plan, errors)
        validate_evidence(plan, errors)
        validate_failed_branches(plan, errors)

    expect = bundle.get("expect", "pass")
    if expect == "pass":
        return not errors, errors
    if expect == "fail":
        expected_families = bundle.get("expected_error_families", [])
        matched = all(any(e.startswith(fam) for e in errors) for fam in expected_families)
        return bool(errors) and matched, errors
    return False, [f"E_LOAD_002 unknown expect value {expect!r}"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--schemas", default="schemas/smart-etl")
    parser.add_argument("--examples", default="examples/smart-etl")
    args = parser.parse_args()

    schemas = load_schemas(Path(args.schemas))
    failures = 0
    for path in sorted(Path(args.examples).glob("*.example.json")):
        ok, errors = validate_example(path, schemas)
        print(f"{'PASS' if ok else 'FAIL'} {path}")
        for error in errors:
            print(f"  {error}")
        if not ok:
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
