# SHIR SerDes v0.1

Status: draft
Owner: Semantic SerDes
Tracking issue: <https://github.com/SocioProphet/semantic-serdes/issues/6>
Ontology contract: <https://github.com/SocioProphet/ontogenesis/issues/26>

## Purpose

This draft defines the first machine-readable serialization slice for the Semantic Hyperknowledge Intermediate Representation (SHIR).

SHIR complements the existing semantic-serdes primitives:

- Semantic cells preserve plane, truth class, time model, merge model, provenance, governance, and replayability.
- Context cells preserve entity, derived, and global context.
- Surface projections govern query/export/application surfaces.
- Agent messages and decision artifacts capture agent communication and decisions.
- Replay artifacts support deterministic rerun and audit.

SHIR adds a hyperknowledge-oriented contract for induced assertions, n-ary relation preservation, linkage candidates, governed assertions, projection-loss reporting, and receipts for semantic graph/retrieval/ML lowering.

## First executable slice

The v0.1 slice covers this path:

```text
text/table/RDF source
  -> CandidateAssertion
  -> LinkageCandidate
  -> Assertion
  -> ProjectionLossReport
  -> Receipt
```

The slice intentionally does not implement a GNN trainer or RDF parser in this repository. Semantic-serdes owns schemas, examples, validation contracts, and manifests. Executable compilers and training packs belong in downstream MLOps/runtime repositories.

## Schemas added in this slice

- `schemas/shir_candidate_assertion.schema.json`
- `schemas/shir_linkage_candidate.schema.json`
- `schemas/shir_assertion.schema.json`
- `schemas/shir_projection_loss_report.schema.json`
- `schemas/shir_receipt.schema.json`

## Example fixtures added in this slice

- `examples/shir_candidate_assertion.example.yaml`
- `examples/shir_linkage_candidate.example.yaml`
- `examples/shir_assertion.example.yaml`
- `examples/shir_projection_loss_report.example.yaml`
- `examples/shir_receipt.example.yaml`

The fixture theme is SourceOS/AgentOS storage:

```text
TopoLVM provisions local persistent volumes for Kubernetes nodes.
```

The examples demonstrate candidate extraction, linkage ambiguity between Kubernetes node concepts and AgentMachine node concepts, n-ary relation preservation through connector role bindings, temporal/policy/evidence context, projection-loss reporting for PyG-style lowering, semantic leakage metadata, and reproducibility receipts.

## Validation command

After installing repository validation dependencies, validate the new fixtures with:

```bash
python tools/validate_semantic_serdes.py \
  shir_candidate_assertion.schema.json:examples/shir_candidate_assertion.example.yaml \
  shir_linkage_candidate.schema.json:examples/shir_linkage_candidate.example.yaml \
  shir_assertion.schema.json:examples/shir_assertion.example.yaml \
  shir_projection_loss_report.schema.json:examples/shir_projection_loss_report.example.yaml \
  shir_receipt.schema.json:examples/shir_receipt.example.yaml
```

## Design boundaries

- Do not promote candidate assertions directly to truth.
- Do not collapse n-ary relations into binary graph edges without a projection-loss report.
- Do not export graph-ML manifests without semantic leakage metadata.
- Do not encode policy and receipt details into trainable tensors unless the task explicitly requires governance prediction.
- Do not introduce a proprietary runtime dependency.

## Follow-up work

Future slices should add schema coverage for anchors, connectors, links, role bindings, contexts, induction traces, ontology influence records, schema-alignment candidates, noise assessments, curation decisions, conceptual diagnostics, and graph-ML projection manifests.
