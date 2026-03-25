# ADR Note Update: Event / Context / Surface Braid

## Corrections
1. Keep `Observed`, `Asserted`, `Inferred`, and `Reputed` as epistemic truth classes.
2. Move "operational truth" into a surface/usability axis.
3. Treat join and multistage limits as query-shape dependent rather than fixed per platform name.
4. Express entity-context refresh as a validity/replay model that can capture the documented floor and our stricter internal SLA separately.

## Canonical triad
- Event primitive: raw + normalized event
- Context primitive: entity / derived / global context
- Surface primitive: query and export projections

## Governing law
Any cross-boundary object must preserve:
- plane
- truth class
- time model
- merge model
- provenance
- governance/review status
- replayability

## Missing but planned
- parity matrix artifacts
- alias map artifacts
- executable validator bindings
