# Artifact inventory: semantic-serdes

This inventory records the semantic-serdes-relevant artifacts produced in the local worldclass bundles during the 2026-04-09 chat work.

## Canonical contract families identified for this repo

### Existing semantic-serdes spine
- `semantic_cell`
- `surface_projection`
- `tag_transition`
- `alias_map`
- `agent_message`
- `agent_decision_artifact`
- `replay_artifact`
- `context_merge_policy`

### New contract families proposed for landing here
- `wire_semantic_projection`
- `beacon_context_bundle`
- `temporal_constraint_cell`
- `sandbox_path_cell`
- `environment_epoch_bundle`
- `toolchain_capability_cell`
- `export_boundary_policy_cell`
- `artifact_commit_bundle`
- `coordination_semaphore`
- `surface_family_bundle`
- `route_projection_bundle`
- `code_bundle_cell`
- `symbol_cell`
- `recovery_claim`

## Local artifact families produced in chat

### Schemas
The local worldclass bundles included schema files for all of the above families under `schemas/`.

### Examples
The local worldclass bundles included example YAMLs for:
- environment epoch bundle
- export boundary policy cell
- artifact commit bundle
- wire semantic projection
- beacon context bundle
- temporal constraint cell
- surface family bundle
- route projection bundle
- code bundle cell
- symbol cell
- recovery claim

### Supporting docs
- glossary
- claim matrix
- observed-vs-asserted sandbox table
- schema-to-repo mapping
- migration guide
- merge readiness report
- apply playbook

### Patch material
Local bundles organized semantic-serdes patch material as:
- `repo_patchsets/semantic-serdes/patches/0001-worldclass-schema-pack.patch`
- `repo_patchsets/semantic-serdes/patches/0002-ci-and-acceptance.patch`

## Recommended landing strategy

1. Land the schema families under repo-native schema paths.
2. Land example YAMLs under repo-native example paths.
3. Land validator and workflow coverage.
4. Only after that, lift supporting docs that are still useful after the schemas are canonicalized.

## Preservation note

This inventory exists so the work is explicitly referenced in GitHub even before every schema/example file is individually copied into the repository.