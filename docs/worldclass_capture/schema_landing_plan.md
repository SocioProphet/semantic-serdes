# Semantic-serdes schema landing inventory

This file records the schema and example families that should be lifted from the local worldclass packs into repo-native structure.

## Schema families to add

### Wire and beacon semantics
- `wire_semantic_projection`
- `beacon_context_bundle`
- `coordination_semaphore`

### Time and event constraints
- `temporal_constraint_cell`

### Environment and boundary governance
- `sandbox_path_cell`
- `environment_epoch_bundle`
- `toolchain_capability_cell`
- `export_boundary_policy_cell`
- `artifact_commit_bundle`

### Surface and route decomposition
- `surface_family_bundle`
- `route_projection_bundle`

### Code-intelligence / reverse-engineering lane
- `code_bundle_cell`
- `symbol_cell`
- `recovery_claim`

## Example families to add

- environment epoch example
- export boundary policy example
- artifact commit bundle example
- wire semantic projection example
- beacon context bundle example
- temporal constraint example
- surface family bundle example
- route projection bundle example
- code bundle cell example
- symbol cell example
- recovery claim example

## Acceptance gates

A schema family should not be considered landed until:

1. schema file exists in repo-native path
2. at least one example validates
3. validator or workflow covers it
4. naming and scope are reconciled with current repo conventions
5. cross-repo references to TriTRPC are documented

## Relationship to TriTRPC

Semantic-serdes owns the canonical semantic contract layer.
TriTRPC owns the wire carriage and cadence/control layer.
The new schema families above are the seam between those two worlds.