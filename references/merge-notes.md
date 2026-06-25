# Literature Skill — Merge Notes

This skill was created by merging two separate repos:
- [Literature_downloader_skill](https://github.com/IvanZhuyf3/Literature_downloader_skill) (paper-at-home) — PDF download via CDP+Playwright
- [Zot_add](https://github.com/IvanZhuyf3/Zot_add) (zot) — Zotero workflow (dedup + metadata + download + attach)

## Key Changes from Original Repos

### zot.py — download_pdf() modified
**Original:** Read `paper_at_home.skill_base` from config.yaml to find external `main.py` path.
**Merged:** Uses `SKILL_BASE / "main.py"` (same directory). No longer needs `paper_at_home` section in config.

```python
# Before (Zot_add original)
pah = cfg.get("paper_at_home", {})
skill_base = pah.get("skill_base", "")
main_py = Path(skill_base) / "main.py"

# After (merged)
main_py = SKILL_BASE / "main.py"
download_dir = cfg.get("download", {}).get("temp_dir", "")
```

### config.yaml — merged sections
Combined paper-at-home's `chrome`/`download`/`rate`/`debug`/`publishers` with Zot's `zotero` section.
Removed `paper_at_home` section entirely (no longer needed — zot.py now uses SKILL_BASE).

### config.yaml.example — merged template
Covers all sections. Users who only want /download can skip the `zotero` section.

### requirements.txt — merged
Added `pyzotero>=1.5.0` to the original paper-at-home deps.

### .gitignore — merged
Added `config.yaml` (contains Zotero API key), `temp/` (for clone staging), `debug_screenshots/`.

## Dual Copies

The skill exists in two locations:
1. **Workspace repo**: `C:\Users\Ivanz\OneDrive\Hermes_workspace\Literature_skill` (git repo, development)
2. **Hermes skills dir**: `C:\Users\Ivanz\AppData\Local\hermes\skills\research\literature-skill` (registered copy)

These are **independent copies**, not symlinks. Changes to the workspace repo must be re-copied to the skills dir, or the skill re-registered.

## Testing Notes

- All Python files pass `py_compile` syntax checks
- `main.py --help` and `zot.py` (no args) both produce correct usage output
- The Hermes venv Python (3.11) doesn't have skill dependencies; system Python (3.14) does. Use full system Python path for testing: `"/c/Users/Ivanz/AppData/Local/Programs/Python/Python314/python.exe"`
- Local skill registration: `hermes skills install` only accepts HTTP(S) URLs. For local skills, copy the directory to `~/.hermes/skills/<category>/<name>/`
