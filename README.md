# Prompt Library

This repository stores a structured, version‑controlled library of reusable prompts.

## Structure

```
prompt-library/
├── prompts/                  # individual prompt entries (.md + .json)
│   ├── <domain>/
│   │   ├── PR-001_slug.md
│   │   └── PR-001_slug.json
├── schemas/                 # JSON Schema for validation
├── scripts/                 # helper utilities (e.g., build-index.py)
├── prompt-library.json      # auto‑generated master index (do not edit manually)
└── .github/workflows/       # CI for linting & validation
```

## Contribution Guide

1. Copy `templates/metadata.md` and `templates/metadata.json` (coming soon) into the appropriate `prompts/<domain>/` folder.
2. Update metadata fields and add your full prompt text in the fenced block.
3. Run `python scripts/build-index.py` to regenerate `prompt-library.json`.
4. Commit both files and open a pull request. CI must pass schema validation.

## License

MIT
