# Worldclass capture: semantic-serdes

This branch captures the semantic-serdes portion of the worldclass wire/semantic control-fabric work developed in chat on 2026-04-09.

## Purpose

This is a preservation and landing branch. It is not the final integrated shape. It exists so the work is captured in GitHub in the correct repository with a clear landing plan.

## Core recommendation

The semantic-serdes repo is the right home for the canonical semantic contracts and examples that were drafted in the worldclass packs. The highest-priority additions are:

- `wire_semantic_projection.schema.json`
- `beacon_context_bundle.schema.json`
- `temporal_constraint_cell.schema.json`
- `sandbox_path_cell.schema.json`
- `environment_epoch_bundle.schema.json`
- `toolchain_capability_cell.schema.json`
- `export_boundary_policy_cell.schema.json`
- `artifact_commit_bundle.schema.json`
- `coordination_semaphore.schema.json`
- `surface_family_bundle.schema.json`
- `route_projection_bundle.schema.json`
- `code_bundle_cell.schema.json`
- `symbol_cell.schema.json`
- `recovery_claim.schema.json`

These should land with example YAML instances and validator integration.

## Why this belongs here

The existing semantic-serdes objects already provide the correct governance spine:

- `semantic_cell`
- `surface_projection`
- `tag_transition`
- `alias_map`
- `agent_message`
- `agent_decision_artifact`
- `replay_artifact`

The new objects extend that spine into wire projection, beacon bundles, temporal constraints, boundary governance, environment topology, and code-intelligence recovery.

## Source bundles produced in chat

The strongest local bundles generated during the work were:

- `worldclass_outputs_v4.zip`
- `worldclass_outputs_v5.zip`
- `worldclass_outputs_v6.zip`
- `worldclass_outputs_v7.zip`
- `worldclass_outputs_v8.zip`

The semantic-serdes-specific patch material was organized under the local paths:

- `repo_patchsets/semantic-serdes/patches/0001-worldclass-schema-pack.patch`
- `repo_patchsets/semantic-serdes/patches/0002-ci-and-acceptance.patch`

## Immediate landing order

1. Add schemas and examples under repo-native paths.
2. Add validation workflow coverage for the new schemas/examples.
3. Add one migration/ADR note documenting the new contract families.
4. Only then freeze names and cross-repo references.

## Important note

This capture branch preserves the work and the landing plan. It does not claim that the new schemas are already accepted or canonical.