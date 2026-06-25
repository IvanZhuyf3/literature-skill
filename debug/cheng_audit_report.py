#!/usr/bin/env python
"""Generate Cheng audit report markdown."""
import json, re, time, requests
from collections import Counter
from lit.core.config import load
from lit.core.zotero import _local_db

cfg = load()
key = cfg.get('semantic_scholar', {}).get('api_key', '')
headers = {'x-api-key': key, 'Content-Type': 'application/json'}
s2_get = {'x-api-key': key} if key else {}

with open('people/Ji-Xin_Cheng/profile.json', 'r') as f:
    p = json.load(f)

# 1. Fetch all DOIs from each profile, tracking source
doi_to_profiles = {}
s2_id_names = {}
s2_id_counts = {}

for sid in p['s2_ids']:
    offset = 0
    while True:
        resp = requests.get(
            f'https://api.semanticscholar.org/graph/v1/author/{sid}/papers',
            params={'fields': 'externalIds', 'limit': 100, 'offset': offset},
            headers=s2_get, timeout=15,
        )
        if resp.status_code == 429:
            time.sleep(5); continue
        if resp.status_code != 200:
            break
        data = resp.json()
        for paper in data.get('data', []):
            doi = paper.get('externalIds', {}).get('DOI')
            if doi:
                doi_to_profiles.setdefault(doi.lower(), set()).add(sid)
        if 'next' not in data:
            break
        offset = data['next']
        time.sleep(0.5)
    resp2 = requests.get(
        f'https://api.semanticscholar.org/graph/v1/author/{sid}',
        params={'fields': 'name,paperCount'},
        headers=s2_get, timeout=15,
    )
    if resp2.status_code == 200:
        s2_id_names[sid] = resp2.json().get('name', sid)
        s2_id_counts[sid] = resp2.json().get('paperCount', 0)
    else:
        s2_id_names[sid] = sid
        s2_id_counts[sid] = 0
    time.sleep(0.8)

# 2. Low-confidence profiles (J. Cheng without second initial)
LOW_CONF = {'2116039843', '2219903942', '2107265746'}

# 3. Zotero DOIs
conn = _local_db()
rows = conn.execute("""
    SELECT LOWER(idv.value) AS doi FROM itemData id
    JOIN fields f ON id.fieldID = f.fieldID
    JOIN itemDataValues idv ON id.valueID = idv.valueID
    WHERE f.fieldName = 'DOI'
""").fetchall()
conn.close()
zotero_dois = {r['doi'] for r in rows if r['doi']}

# 4. New DOIs
new_dois = set(doi_to_profiles.keys()) - zotero_dois

# 5. Batch metadata
new_list = sorted(new_dois)
papers_info = []
for i in range(0, len(new_list), 500):
    batch = [f'DOI:{d}' for d in new_list[i:i+500]]
    resp = requests.post(
        'https://api.semanticscholar.org/graph/v1/paper/batch',
        params={'fields': 'title,year,venue,publicationTypes'},
        headers=headers, json={'ids': batch}, timeout=60,
    )
    if resp.status_code == 429:
        time.sleep(5); continue
    if resp.status_code == 200:
        results = resp.json()
        for j, paper in enumerate(results):
            doi = new_list[i+j]
            info = {'doi': doi, 'profiles': sorted(doi_to_profiles.get(doi, set()))}
            if paper:
                info['title'] = paper.get('title', '')
                info['year'] = paper.get('year')
                info['venue'] = paper.get('venue', '')
                info['pub_types'] = paper.get('publicationTypes', [])
            else:
                info['title'] = '???'
                info['year'] = None
                info['venue'] = ''
                info['pub_types'] = []
            papers_info.append(info)
    time.sleep(0.5)

# 6. Filter
NON_JOURNAL = [
    r'^10\.1117/12\.', r'^10\.1117/2\.',
    r'^10\.1364/(cleo|fio|ntm|microscopy|cosi|up\.|translational|ls\.|sensors)',
    r'^10\.1109/(cleo|leos|ipcon|lissa|sensors)', r'^10\.23919/cleo',
    r'^10\.1096/fasebj', r'^10\.1158/1538-7445',
    r'^10\.1158/(1538-8514|1557-3265|1940-6207)',
    r'^10\.(1007/978|1016/b978|1201/b|1142/978)',
    r'\.s\d{3}$', r'^10\.15278/isms', r'^10\.1002/sdtp',
    r'^10\.21203/rs', r'^10\.(26434/chemrxiv|33774/chemrxiv)', r'^10\.1101/',
]
GARBAGE_TITLES = [
    'advertising', 'front matter', 'frontmatter', 'subject index',
    'table of contents', 'editorial board', 'back matter',
    'inside cover', 'innentitelbild',
]

def classify(info):
    doi = info['doi']
    d = doi.lower()
    for pat in NON_JOURNAL:
        if re.search(pat, d):
            return False, 'denylist'
    pt = info.get('pub_types', [])
    if pt and 'Conference' in pt and 'JournalArticle' not in pt:
        return False, 'conference'
    profiles = set(info.get('profiles', []))
    if profiles and profiles <= LOW_CONF:
        return False, 'low_conf_only'
    title_lower = (info.get('title') or '').lower()
    for kw in GARBAGE_TITLES:
        if kw in title_lower:
            return False, f'junk'
    if re.search(r'(abstract\s+\d+|supplement|poster)', title_lower):
        return False, 'abstract'
    if re.search(r'\.suppl|_supplement|suppl_', d):
        return False, 'supplement'
    return True, 'ok'

journal = []
rejected = []
for info in papers_info:
    ok, reason = classify(info)
    if ok:
        journal.append(info)
    else:
        rejected.append((info, reason))

journal.sort(key=lambda p: p.get('year') or 0, reverse=True)

# 7. Generate markdown
lines = []
lines.append('# Ji-Xin Cheng — S2 Audit Report')
lines.append('')
lines.append(f'> Generated: 2026-06-25')
lines.append(f'> S2 profiles scanned: {len(s2_id_names)}')
lines.append(f'> S2 total unique DOIs: {len(doi_to_profiles)}')
lines.append(f'> Already in Zotero: {len(doi_to_profiles) - len(new_dois)}')
lines.append(f'> New (not in Zotero): {len(new_dois)}')
lines.append('')
lines.append('## Filter Summary')
lines.append('')
rc = Counter(r for _, r in rejected)
lines.append(f'| Filter | Count |')
lines.append(f'|--------|-------|')
lines.append(f'| S2 new DOIs (raw) | {len(new_dois)} |')
for reason, count in rc.most_common():
    lines.append(f'| Rejected: {reason} | {count} |')
lines.append(f'| **Confirmed missing journal papers** | **{len(journal)}** |')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## Missing Journal Papers')
lines.append('')
lines.append(f'| # | Year | Title | Venue | DOI |')
lines.append(f'|---|------|-------|-------|-----|')

for i, paper in enumerate(journal, 1):
    yr = paper.get('year') or '?'
    title = (paper.get('title') or '???').replace('|', '/')
    venue = (paper.get('venue') or '').replace('|', '/')
    doi = paper['doi']
    lines.append(f'| {i} | {yr} | {title} | {venue} | `{doi}` |')

lines.append('')
lines.append('---')
lines.append('')
lines.append('## S2 Profiles Discovered (20)')
lines.append('')
lines.append('| S2 ID | Name in S2 | Papers | Confirmed |')
lines.append('|-------|-----------|--------|-----------|')

for sid in p['s2_ids']:
    name = s2_id_names.get(sid, sid)
    count = s2_id_counts.get(sid, '?')
    conf = '⚠️' if sid in LOW_CONF else '✓'
    lines.append(f'| `{sid}` | {name} | {count} | {conf} |')

lines.append('')
lines.append('---')
lines.append('')
lines.append('## Rejected (false positives + non-journal)')
lines.append('')
lines.append('| DOI | Year | Title | Reason |')
lines.append('|-----|------|-------|--------|')

for info, reason in rejected:
    yr = info.get('year') or '?'
    title = (info.get('title') or '???')[:50].replace('|', '/')
    doi = info['doi']
    lines.append(f'| `{doi}` | {yr} | {title} | {reason} |')

lines.append('')

md = '\n'.join(lines)
with open('cheng_audit.md', 'w', encoding='utf-8') as f:
    f.write(md)

print(f'Done: {len(journal)} journal papers, {len(rejected)} rejected')
print(f'Written to cheng_audit.md')
