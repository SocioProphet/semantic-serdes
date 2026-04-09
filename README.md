# Semantic SerDes

[![License](https://img.shields.io/github/license/SocioProphet/semantic-serdes)](https://github.com/SocioProphet/semantic-serdes/blob/main/LICENSE)
![GitHub stars](https://img.shields.io/github/stars/SocioProphet/semantic-serdes)

> A high-performance schema library for semantic serialization and deserialization with compatibility across modern platforms.

---

## Overview

**Semantic SerDes** (Serialization / Deserialization) provides a canonical schema pack for structured, semantics-aware data interchange. It defines the contract layer that governs how events, context, and surface projections are encoded, merged, replayed, and surfaced across service boundaries.

The system is modeled as a **braided flow** across three primitives:

| Primitive | Description |
|-----------|-------------|
| **Event** | Raw and normalized event objects |
| **Context** | Entity, derived, and global context cells |
| **Surface** | Query and export projections (Search, Rules, Dashboards, Export, Conversation) |

Every cross-boundary object must preserve its **plane**, **truth class**, **time model**, **merge model**, **provenance**, **governance status**, and **replayability**. This pack extends the v1 semantic-cell/tag/surface work with the missing contract layer:

- Context merge policy
- Agent message envelope
- Agent decision artifact
- Replay artifact

### Key Features

- **Canonical enum definitions** — single source of truth for planes, truth classes, time models, merge models, scopes, and surfaces.
- **JSON Schema contracts** — machine-readable schemas for every first-class object, enabling automated validation.
- **Worked examples** — YAML examples covering semantic cells, tag transitions, surface projections, agent messages, context cells (asset, user, process, artifact, WHOIS/GTI), and more.
- **Parity-matrix templates** — ready-to-use templates for event/context/surface band comparison.
- **Alias maps** — machine-readable maps to handle vendor naming drift across integrations.
- **Validation tooling** — a bundled Python validator (`tools/validate_semantic_serdes.py`) for CI integration.
- **Architecture Decision Records** — documented design rationale in `docs/`.

---

## Repository Structure

```
semantic-serdes/
├── canonical_enums.yaml          # Canonical enum values (plane, truth_class, time_model, …)
├── schemas/                      # JSON Schema definitions
│   ├── semantic_cell.schema.json
│   ├── tag_transition.schema.json
│   ├── surface_projection.schema.json
│   ├── context_merge_policy.schema.json
│   ├── agent_message.schema.json
│   ├── agent_decision_artifact.schema.json
│   ├── replay_artifact.schema.json
│   └── alias_map.schema.json
├── examples/                     # YAML usage examples
│   ├── semantic_cell.example.yaml
│   ├── tag_transition.example.yaml
│   ├── surface_projection.example.yaml
│   ├── context_merge_policy.example.yaml
│   ├── agent_message.example.yaml
│   ├── agent_decision_artifact.example.yaml
│   ├── replay_artifact.example.yaml
│   ├── alias_map.example.yaml
│   ├── asset_context_cell.example.yaml
│   ├── user_context_cell.example.yaml
│   ├── process_context_cell.example.yaml
│   ├── artifact_context_cell.example.yaml
│   ├── global_context_cell.example.yaml
│   └── parity_matrix.template.yaml
├── tools/
│   └── validate_semantic_serdes.py   # Python validation utility
└── docs/
    └── adr_note_update.md            # Architecture Decision Record notes
```

---

## Installation

### Using the schemas directly

Clone the repository and reference schemas from the `schemas/` directory:

```bash
git clone https://github.com/SocioProphet/semantic-serdes.git
```

### Validation tool

The bundled validator requires Python 3.8+ and the `jsonschema` package:

```bash
pip install jsonschema
python tools/validate_semantic_serdes.py
```

---

## Usage

### Canonical enums

The `canonical_enums.yaml` file is the single source of truth for all allowed enum values:

```yaml
plane:
  - RAW
  - EVENT
  - ENTITY
  - DERIVED
  - GLOBAL
  - SURFACE

truth_class:
  - OBSERVED
  - ASSERTED
  - INFERRED
  - REPUTED

time_model:
  - INSTANT
  - INTERVAL
  - SNAPSHOT
  - TIMELESS
  - QUERY_WINDOW

merge_model:
  - APPEND
  - MERGED
  - CONDITIONAL_FALLBACK
  - FIRST_MATCH
  - OVERWRITE
  - PARALLEL
  - MATERIALIZE
```

### Validating a semantic cell

```python
import json
import jsonschema
import yaml

with open("schemas/semantic_cell.schema.json") as f:
    schema = json.load(f)

with open("examples/semantic_cell.example.yaml") as f:
    instance = yaml.safe_load(f)

jsonschema.validate(instance, schema)
print("Validation passed.")
```

### Working with agent messages

See [`examples/agent_message.example.yaml`](examples/agent_message.example.yaml) for a complete envelope example and [`schemas/agent_message.schema.json`](schemas/agent_message.schema.json) for the full contract.

---

## Design Principles

1. **Epistemic truth classes** (`OBSERVED`, `ASSERTED`, `INFERRED`, `REPUTED`) are preserved through every transformation — they are never collapsed or overwritten.
2. **Operational usability** belongs on the **surface axis**, not inside epistemic truth classes.
3. **Join and multistage limits** are query-shape dependent, not fixed per platform name.
4. **Entity-context refresh** is expressed as a validity/replay model that separates documented platform floors from stricter internal SLAs.

---

## Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for full details. In short:

1. Fork this repository.
2. Create a feature branch: `git checkout -b my-new-feature`.
3. Commit your changes: `git commit -am 'Add some feature'`.
4. Push to the branch: `git push origin my-new-feature`.
5. Open a pull request against `main`.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

Special thanks to the [SocioProphet](https://github.com/SocioProphet) team for their vision and dedication to building rigorous, semantics-first data interchange standards.
