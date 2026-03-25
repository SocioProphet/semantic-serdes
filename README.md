# Semantic Serdes Pack v3

This pack extends the earlier semantic-serdes contracts with:
- parity matrix template
- alias map schema
- worked UDM/ECG-style examples
- GitHub Actions validation workflow
- local validation script

## Contents
- `schemas/` JSON Schemas
- `examples/` YAML examples and templates
- `.github/workflows/validate-semantic-serdes.yml`
- `tools/validate_semantic_serdes.py`
- `canonical_enums.yaml`
- `docs/adr_note_update.md`

## Recommended placement in coordination repo
- `schemas/semantic-serdes/`
- `examples/semantic-serdes/`
- `.github/workflows/`
- `tools/`

## Local validation
```bash
python -m pip install pyyaml jsonschema
python tools/validate_semantic_serdes.py --schema-dir schemas   semantic_cell.schema.json:examples/asset_context_cell.example.yaml   tag_transition.schema.json:examples/tag_transition.example.yaml   surface_projection.schema.json:examples/surface_projection.example.yaml
```
