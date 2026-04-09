# Semantic SerDes Pack v2

This pack extends the v1 semantic-cell/tag/surface work with the missing contract layer:
- context merge policy
- agent message envelope
- agent decision artifact
- replay artifact

## Design intent

The system is modeled as a braided flow across three primitives:
1. Event primitive: raw + normalized event
2. Context primitive: entity / derived / global context
3. Surface primitive: Search / Rules / Dashboards / Export / Conversation projections

The important correction is that operational usability belongs on the **surface axis** rather than inside the epistemic truth classes.

## Files

### Enums
- `canonical_enums.yaml`

### Schemas
- `schemas/semantic_cell.schema.json`
- `schemas/tag_transition.schema.json`
- `schemas/surface_projection.schema.json`
- `schemas/context_merge_policy.schema.json`
- `schemas/agent_message.schema.json`
- `schemas/agent_decision_artifact.schema.json`
- `schemas/replay_artifact.schema.json`

### Examples
- `examples/*.example.yaml`

### Documentation
- `docs/adr_note_update.md`

## Recommended next steps
1. Add parity-matrix templates for event/context/surface bands.
2. Add machine-readable alias maps for vendor naming drift.
3. Connect these schemas to workflow validation in the coordination repo.
4. Add worked examples for asset, user, process, artifact, and WHOIS/GTI context.
