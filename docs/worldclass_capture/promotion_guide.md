# Worldclass capture promotion guide

This note describes how to move files from `worldclass_capture` into canonical repo-native placement without losing review discipline.

## Promotion rule

A `worldclass_capture` file should only be promoted when all of the following are true:

1. the name is stable and no longer obviously provisional
2. at least one example validates against the schema
3. the semantics fit the repo's existing naming and governance model
4. any cross-repo dependency on TriTRPC is documented
5. the file is useful beyond the specific 2026-04-09 chat session

## Suggested order

### Promote first
These are the strongest candidates for eventual canonicalization:
- `temporal_constraint_cell`
- `beacon_context_bundle`
- `coordination_semaphore`
- `surface_family_bundle`
- `route_projection_bundle`

### Promote second
These are strong but should follow after naming and cross-repo review:
- `code_bundle_cell`
- `symbol_cell`
- `recovery_claim`

## Why keep the capture layer for now

The capture prefix preserves two useful truths:
- the work is real and reviewable in-repo
- it is not yet being asserted as settled canonical contract vocabulary

That is the right state for phase 2.