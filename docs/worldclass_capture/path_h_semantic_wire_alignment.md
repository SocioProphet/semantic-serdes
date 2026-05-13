# Path-H Semantic Wire Alignment

Status: draft integration slice  
Owner: Semantic SerDes / TritRPC alignment  
Scope: semantic-control projection only; no quantum-state serialization

## Purpose

This document aligns the Path-H qutrit / hybrid control profile with Semantic
SerDes and the semantic wire format.

The governing split is:

```text
SemanticCell / SHIR assertion
  -> SemanticControlCodebook
  -> WireSemanticProjection
  -> RouteProjectionBundle
  -> TritRPC Path-H frame
  -> receipt / replay / projection-loss report
```

Path-H is the hot control lane. Semantic SerDes is the meaning-preservation
layer. The bridge between them is a handle-bound projection, not an inline
semantic payload.

## Core rule

Path-H MUST NOT carry full semantic state, policy payloads, n-ary assertion
graphs, sensitive context, or trainable semantic tensors on the hot path.

Path-H MAY carry compact, replayable handles and ternary coordinates that
resolve to those objects through Semantic SerDes registries and receipts.

In short:

```text
full meaning off-hot-path
lawful ternary projection on-hot-path
receipt binds both
```

## Layer contract

### 1. Semantic source layer

Semantic source objects are `SemanticCell` and SHIR-family objects.

They preserve:

- plane
- truth class
- time model
- merge model
- scope
- provenance
- governance
- replayability
- n-ary relation structure where applicable
- projection-loss reports for lossy lowering

Examples:

```text
PermissionClaim(actor, action, resource, condition)
Delegation(actor, delegate, capability, bound)
NegatedPermissionClaim(actor, action, resource, condition)
```

### 2. Semantic control codebook

`SemanticControlCodebook` defines the compact alphabet used to project typed
semantic objects into the hot ternary coordinate space.

It binds:

- semantic symbol identity
- compact symbol code
- trit vector
- semantic role
- allowed truth-class policy
- required state243 reference
- allowed CTRL243 constraints
- loss policy

The codebook is not the source of truth for the claim. It is the source of
truth for the claim's hot-path dispatch coordinate.

### 3. Wire semantic projection

`WireSemanticProjection` binds concrete source cells to the hot coordinate.

For Path-H semantic control, it SHOULD include:

- `source_cells` pointing to SemanticCell or SHIR objects
- `hot_coordinate.sem243_ref`
- `hot_coordinate.state243_ref`
- `handle_bindings.route_h`
- `handle_bindings.context_h`
- `handle_bindings.schema_h`
- `handle_bindings.bundle_h`
- `placement_policy.sensitive_off_hot_path: true`
- `resolver.replay_required: true`

### 4. Route projection bundle

`RouteProjectionBundle` binds the Path-H route to the semantic projection
family.

It prevents route drift by requiring every route pattern to cite:

- projection references
- semantic references
- family reference
- provenance
- governance

### 5. Path-H frame

The Path-H frame carries only the hot projection:

```yaml
CTRL243:
  profile: 2
  lane: 2
  evidence: 2
  fallback: 1
  routefmt: 1

payload:
  seq: 1842
  ttl_ms: 5000
  route_h: handle:route-path-h-permission-claim-v1
  basis_id: 7
  sem243_ref: sem243:policy.permission.claim
  state243_ref: state243:allow-mid-deny:v0.1
  context_h: handle:context-actor-action-resource-condition
  schema_h: handle:schema-shir-assertion-v0.1
  bundle_h: handle:bundle-permission-claim-001
  projection_id: wire-projection-path-h-permission-claim-001
```

The full semantic bundle is resolved off-hot-path.

## Field separation

Do not collapse these axes:

| Field | Meaning |
| --- | --- |
| `truth_class` | epistemic status of the semantic object |
| `CTRL243.evidence` | evidence mode of the hot control frame |
| `basis_id` | physical / measurement / representation basis handle |
| `sem243_ref` | semantic control alphabet coordinate |
| `state243_ref` | ternary state-family coordinate |
| `route_h` | route/service/schema/context-policy handle |
| `bundle_h` | off-hot-path semantic bundle handle |

A verified Path-H frame may carry an `INFERRED` semantic object. An observed
semantic object may be carried through a sampled transport frame. These are
orthogonal axes.

## Required invariants

1. Every Path-H semantic frame MUST reference a `WireSemanticProjection`.
2. Every `WireSemanticProjection` MUST reference one or more source cells.
3. Every `route_h` used by Path-H semantic control MUST resolve to a
   `RouteProjectionBundle`.
4. Every `sem243_ref` MUST resolve under `codebook_version` and `epoch_id`.
5. Every lossy lowering MUST emit or cite a projection-loss report.
6. Sensitive semantic objects MUST remain off-hot-path when
   `sensitive_off_hot_path` is true.
7. Every replayable frame MUST bind `route_h`, `schema_h`, `bundle_h`,
   `projection_id`, and the codebook epoch.
8. Path-H quantum or hybrid frames MUST use `CTRL243.profile = 2`.
9. Qutrit-specific BSM3 events MUST use the quantum or hybrid lane.
10. Semantic receipts MUST preserve `truth_class` separately from
    `CTRL243.evidence`.

## Negative fixture targets

Future CI fixtures should reject:

- Path-H semantic frame with no `projection_id`
- projection with no `sem243_ref`
- Path-H frame with `CTRL243.profile != 2`
- qutrit / BSM3 event using classical lane
- inline sensitive semantic payload when `sensitive_off_hot_path = true`
- stale codebook epoch without accepted rollover policy
- lossy semantic lowering with no projection-loss report
- route handle with no `RouteProjectionBundle`
- control frame that collapses `truth_class` into `CTRL243.evidence`

## Current files in this slice

- `schemas/worldclass_capture/semantic_control_codebook.schema.json`
- `examples/worldclass_capture/semantic_control_codebook.example.yaml`
- `examples/worldclass_capture/path_h_semantic_wire_projection.example.yaml`
- `examples/worldclass_capture/path_h_route_projection_bundle.example.yaml`

## Doctrine sentence

Semantic SerDes preserves meaning. `WireSemanticProjection` lowers meaning.
`RouteProjectionBundle` binds meaning to route. Path-H transports only the
compact ternary control projection. Receipts prove what was preserved, lost,
replayed, and governed.
