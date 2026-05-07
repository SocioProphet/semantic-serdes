# Authority Map v0.1 — ViewContract ownership

Status: draft  
Scope: portable view contracts across agent authority, policy authority, ontology authority, workspace fingerprints, graph runtime, traversal evidence, and transport.

## Purpose

This note records the authority/data ownership split behind `ViewContract`.

The core correction is that graph-view sharing has two intertwined spines:

1. Data / analysis spine: identity proofs, entity graph state, graph views, traversal and materialization evidence.
2. Authority / evidence spine: agent authority, policy decisions, ontology terms, workspace/environment fingerprints, execution verdicts, and transport binding.

A view is not valid merely because the graph traversal was valid. A view is valid only when its data projection is bound to principal authority, policy purpose, ontology meaning, workspace/environment state, runtime evidence, traversal evidence, and transport authentication.

## Repository ownership

| Plane | Owner | Responsibility |
| --- | --- | --- |
| Portable schema shape | `SocioProphet/semantic-serdes` | `ViewContract` schema, typed portable refs, semantic surface projection shape. |
| Agent authority | `SocioProphet/agent-registry` | Agent identity, session, tool grants, memory grants, denied scopes, revocation, runtime authority. |
| Policy authority | `SocioProphet/policy-fabric` | Policy bundles, compiled plans, decisions, verdicts, obligations, validation reports, release packs, replay reports. |
| Ontology authority | `SocioProphet/ontogenesis` | `ViewContract`, `DisclosureMode`, `TypedAbsence`, `PolicyBarrier`, `RedactionBoundary`, `RevocationEpoch`, JSON-LD contexts, SHACL gates. |
| Execution evidence | `SocioProphet/agentplane` | Work orders, bundles, placement decisions, verdicts, run artifacts, replay artifacts, session artifacts. |
| Workspace/environment fingerprints | `SocioProphet/sociosphere` | Workspace, environment, release-set, artifact, policy, tenant/workspace, rollback, topology, and source-exposure fingerprints. |
| Platform identity ingress | `SocioProphet/prophet-platform` | Platform-facing identity/session/proof ingress contracts and runtime services. |
| Deep identity proof | `SocioProphet/identity-is-prime-reference` | Identity-prime proof artifacts, prime-topic constraints, merge veto math, congruence evidence. |
| Entity graph materialization | `SocioProphet/regis-entity-graph` | Canonical identity graph, proof-derived graph deltas, evidence attachments, revocation graph consequences. |
| Graph operation runtime | `SocioProphet/meshrush` | Governed graph-view operation, diffusion, stopping, crystallization, runtime graph traces. |
| Traversal/materialization evidence | CairnPath owner repo TBD | CairnLine, CairnStep, step traces, materialization traces, cut certificates, frontier commitments. |
| Transport binding | `SocioProphet/TriTRPC` | Envelope, schema/context id, AAD binding, authenticated metadata transport. |
| Knowledge standards | `SocioProphet/socioprophet-standards-knowledge` | Claim, annotation, provenance, knowledge lifecycle, TriTRPC knowledge binding. |
| Storage standards | `SocioProphet/socioprophet-standards-storage` | Storage contexts, graph abstraction, receipt/projection/storage semantics, benchmark workload expectations. |
| Agent standards | `SocioProphet/socioprophet-agent-standards` | Agent profiles, conformance levels, evidence obligations, identity/auth standards. |

## Normative split

Semantic SerDes owns the portable contract shape. It must not become the policy authority, ontology authority, agent grant authority, or execution authority.

Runtime repositories consume references. They must not duplicate upstream authority schemas unless explicitly acting as a profile or adapter layer.

## ViewContract authority roots

A valid `ViewContract` composes at least these roots:

- principal authority: human, agent, service, or workload identity and session context;
- agent authority: agent registry grants, denied scopes, revocation state, and runtime authority, when the principal is an agent;
- policy authority: policy bundle, compiled plan, decision, purpose, obligations, and revocation epoch;
- semantic authority: Semantic SerDes profile plus Ontogenesis terms and SHACL gates;
- workspace authority: Sociosphere/Lattice fingerprints for workspace, environment, release, artifacts, policy, tenant, and rollback;
- data authority: Regis source graph and MeshRush graph view references;
- runtime evidence: AgentPlane work order, verdict, run, and replay references;
- traversal evidence: CairnPath refs when traversal/materialization occurred;
- transport binding: TriTRPC schema/context id and AAD/auth references.

## Required follow-up profiles

The schema added in this tranche is portable and reference-heavy by design. The next authority-specific profiles should land in their owner repos:

1. `agent-registry`: AgentAuthorityRef profile and validator.
2. `policy-fabric`: PolicyAuthorityRef profile and validator.
3. `ontogenesis`: ViewContract ontology terms and SHACL gate.
4. `sociosphere`: WorkspaceFingerprintRef / ViewSignature input profile.
5. `agentplane`: RuntimeEvidenceRefs / verdict/work-order profile.
6. CairnPath owner repo: TraversalEvidenceRefs / CairnLine materialization profile.

## Implementation note

The schema intentionally validates reference shape and cross-field requirements, not dereference resolution. Dereference validation belongs in a multi-repo conformance harness once the referenced owner repos expose stable fixture refs.
