"""Merge all prompt JSON files into prompt-library.json and validate."""
import json, pathlib, sys
try:
    import jsonschema
except ImportError:
    print("Please `pip install jsonschema` to use this script.")
    sys.exit(1)

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = json.load(open(ROOT / "schemas" / "prompt.schema.json"))

entries = []
for p in ROOT.glob("prompts/**/*.json"):
    data = json.load(open(p))
    jsonschema.validate(data, SCHEMA)
    entries.append(data)

with open(ROOT / "prompt-library.json", "w") as f:
    json.dump(entries, f, indent=2)
print(f"Wrote {len(entries)} entries to prompt-library.json")
