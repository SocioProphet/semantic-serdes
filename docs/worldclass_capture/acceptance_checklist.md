# Semantic-serdes phase 2 acceptance checklist

This checklist defines what should be true before PR #4 is promoted from staging material to an accepted phase-2 landing slice.

## Contract integrity

- [ ] Every new schema in `schemas/worldclass_capture/` has at least one matching example.
- [ ] The worldclass capture validation workflow passes for all listed pairs.
- [ ] No schema name duplicates an existing canonical contract with different semantics.

## Naming and scope

- [ ] `worldclass_capture` names are reviewed for eventual canonical placement.
- [ ] Cross-repo dependencies on TriTRPC are documented where relevant.
- [ ] Temporary capture labels are not mistaken for final canonical names.

## Review intent

- [ ] Temporal, beacon, semaphore, surface/route, and code-intelligence families are all represented.
- [ ] Reviewers agree which families are mature enough for promotion first.
- [ ] Families that remain exploratory are explicitly left in the capture namespace.

## Suggested first-promotion set

The strongest candidates for first promotion remain:
- `temporal_constraint_cell`
- `beacon_context_bundle`
- `coordination_semaphore`
- `surface_family_bundle`
- `route_projection_bundle`

The code-intelligence families should likely follow after additional review:
- `code_bundle_cell`
- `symbol_cell`
- `recovery_claim`
