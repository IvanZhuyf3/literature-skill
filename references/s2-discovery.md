# S2 Profile Discovery + Audit + Confidence Scoring

> Techniques developed 2026-06-25. Covers `lit discover-s2`, `audit_new_papers()`,
> and the high/low confidence pipeline in `find_new_papers()` / `track_all.py`.

## Problem

Semantic Scholar has severe profile duplication. One person (Ji-Xin Cheng) had
**20 separate S2 author profiles** for the same identity — different dash encodings
(Unicode U+2010 vs ASCII `-`), abbreviated forms (`J. Cheng`), space variants.
Only 3 were known before discovery.

S2 author search (`/author/search?query=...`) is useless for common names — returns
homonyms with no way to distinguish them.

## Solution: DOI Cross-Reference

**Key insight**: We already have the person's papers in Zotero. Batch-query those DOIs
on S2's paper API → get all authors → filter by surname + given-first-initial.

### API Flow

1. Get all DOIs from person's Zotero collection (local SQLite)
2. `POST /graph/v1/paper/batch` with `{ids: ["DOI:10.xxx", ...], fields: "authors"}`
   - Max 500 per request (1 request for Cheng's 424 DOIs)
   - Near-instant (<1s)
3. Collect all `(authorId, name)` pairs, count appearances across papers
4. Filter: `surname == target_surname AND given_first_initial == target_initial`
   - Use `_norm_preserve()` to handle Unicode dashes, accents
   - Match on first initial only (J), not full initials (JXC) — `J. Cheng` is valid
5. `confirmed` flag: if target has ≥2 given names (Ji-Xin), check if second
   initial (X) appears anywhere in candidate's name. `J. Cheng` → unconfirmed.

### Cost

| Author | DOIs | S2 Profiles Found | API Calls | Time |
|--------|------|-------------------|-----------|------|
| Cheng | 424 | 20 | 1 batch + 20 author lookups | ~30s |
| Wei Min | 133 | 7 | 1 batch + 7 author lookups | ~15s |
| Dan Fu | 75 | 4 | 1 batch + 4 author lookups | ~10s |

## S2 Data Quality Issues

S2 is **dirty**. Confirmed problems:

1. **Profile mixing**: S2 assigned papers from a different "J. Cheng" (Harvard, 1973
   liquid crystals) to Cheng's main profile (`144507368`). One-off false positives.
2. **Empty affiliations**: `affiliations: []` for ALL authors on ALL papers. S2 provides
   `paperCount` and `hIndex` but no affiliation data. **Use CrossRef for affiliations.**
3. **Misclassified publication types**: ~20% of conference papers tagged as
   `JournalArticle` by S2. DOI prefix denylist is more reliable.
4. **Garbage DOIs**: journal front matter ("Advertising and Front Matter"), subject
   indices, abstract supplements all have DOIs and appear in author profiles.

## Audit: Finding Missing Papers

After discovering all S2 IDs, full-scan all profiles → diff with Zotero → filter to
journal articles.

### Filtering Pipeline (denylist-first)

```
raw S2 DOIs (e.g. 607)
  → minus Zotero DOIs (e.g. 394 already in library)
  → denylist filter: SPIE, OSA/Optica conferences, IEEE conf, FASEB/AACR abstracts,
     bioRxiv/medRxiv preprints, ChemRxiv, book chapters, supplementary files,
     ACM/AAAI/IJCAI conferences
  → garbage title filter: "advertising", "front matter", "subject index",
     "editorial board", "inside cover", "innentitelbild"
  → low-confidence-profile-only filter: DOIs appearing ONLY in unconfirmed S2 profiles
  → result: confirmed missing journal papers
```

**Critical**: DOI denylist takes **priority** over S2 `publicationTypes`. S2 misclassifies
~20% of conferences as JournalArticle.

## Confidence Scoring in find_new_papers()

Each new paper gets `confidence: "high" | "low"`:

| Condition | Result |
|-----------|--------|
| CrossRef affiliation matches `known_affiliations` in profile.json | **high** |
| CrossRef returns data but no affiliation match | **low** |
| CrossRef lookup fails (404, timeout) | **high** (no signal → trust) |
| `known_affiliations` is empty/missing | **low** (can't verify → human review) |

### track_all.py Split

- **high** → auto import + quick + attach download, **[SILENT]** (empty stdout)
- **low** → output to stdout for cron agent → generate .md → send to user for review

### known_affiliations in profile.json

```json
{
  "known_affiliations": ["Boston University", "Purdue", "Lawrence Berkeley"]
}
```

These are matched against CrossRef `author[].affiliation[].name` with substring matching
(bidirectional). Essential for distinguishing homonyms (e.g. Delong Zhang in spectroscopy
vs Delong Zhang in AI/semiconductors at Sun Yat-sen University).

**Pitfall**: If `known_affiliations` is empty, ALL new papers default to low. This is
intentional — prevents silent false-positive imports for new tracked people whose
affiliations haven't been configured yet.

## item_key Passing (import → download sync lag)

`import_run()` creates Zotero items via cloud API. `quick_single()` / `attach_single()`
look up items via local SQLite (`find_by_doi`). The SQLite copy hasn't synced yet after
a cloud API write → every download fails with "DOI 不在 Zotero 库中".

**Fix**: Both `quick_single(doi, item_key=...)` and `attach_single(doi, item_key=...)`
accept an optional `item_key` that skips the SQLite lookup entirely.

```python
result = import_run(doi)
ik = result["item_key"]       # from cloud API response
quick_single(doi, item_key=ik)  # pass directly, skip SQLite
```

## CLI Commands

```bash
# Discover all S2 IDs + audit missing papers (preview only)
python -m lit discover-s2 Ji-Xin_Cheng

# Save discovered IDs to profile.json + run audit
python -m lit discover-s2 Ji-Xin_Cheng --save

# Save + auto-download all missing journal papers
python -m lit discover-s2 Ji-Xin_Cheng --download
```
