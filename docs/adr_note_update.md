# ADR Note Update: Event / Context / Surface Braid

This note updates the earlier security-context field model.

## Corrections
1. "Operational truth" is not an epistemic truth class. It is modeled through `surface` and `surface_visibility`.
2. Join-budget language must be query-shape dependent, not a flat platform-name rule.
3. Daily entity refresh may remain an internal SLA, but the semantic contract should preserve the documented five-day-style validity and replay window separately from operational policy.

## Canonical braid
The canonical braid uses three primitives:
- Event primitive: raw + normalized event
- Context primitive: entity / derived / global context
- Surface primitive: Search / Rules / Dashboards / Export projections

Cross-plane movement is represented using `semantic_cell`, `surface_projection`, and `replay_artifact`.
Evolving topic and policy labels use `tag_transition`.
Multi-agent exchange uses `agent_message` and `agent_decision_artifact`.
