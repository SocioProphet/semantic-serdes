#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path

try:
    import yaml
    import jsonschema
except ImportError as e:
    print(f"missing dependency: {e}", file=sys.stderr)
    sys.exit(2)

def load_doc(path: Path):
    text = path.read_text()
    if path.suffix.lower() in {".yaml", ".yml"}:
        return yaml.safe_load(text)
    return json.loads(text)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schema-dir", default="schemas")
    ap.add_argument("pairs", nargs="+", help="schema_name:file_path")
    args = ap.parse_args()

    schema_dir = Path(args.schema_dir)
    failures = 0
    for pair in args.pairs:
        if ":" not in pair:
            print(f"invalid pair {pair}; expected schema:file", file=sys.stderr)
            failures += 1
            continue
        schema_name, file_path = pair.split(":", 1)
        schema = load_doc(schema_dir / schema_name)
        doc = load_doc(Path(file_path))
        try:
            jsonschema.validate(instance=doc, schema=schema)
            print(f"OK  {file_path}  against  {schema_name}")
        except jsonschema.ValidationError as e:
            failures += 1
            print(f"FAIL {file_path} against {schema_name}: {e.message}", file=sys.stderr)
    sys.exit(1 if failures else 0)

if __name__ == "__main__":
    main()
