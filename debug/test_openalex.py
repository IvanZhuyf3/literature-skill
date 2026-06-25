"""Quick OpenAlex API exploration for Ping Wang."""
import requests, json

resp = requests.get(
    "https://api.openalex.org/authors",
    params={"search": "Ping Wang", "filter": "works_count:>5", "per-page": 10},
    headers={"User-Agent": "lit-skill/1.0 (mailto:research@example.com)"},
    timeout=15,
)
data = resp.json()
print(f"Total Ping Wang author profiles: {data['meta']['count']}")
print()

for a in data["results"][:10]:
    name = a.get("display_name", "")
    wid = a.get("id", "").split("/")[-1]
    wc = a.get("works_count", 0)
    aff = a.get("last_known_institution")
    aff_name = ""
    aff_country = ""
    if aff:
        aff_name = aff.get("display_name", "")
        aff_country = aff.get("country_code", "")
    topics = [t.get("display_name", "") for t in a.get("topics", [])[:3]]
    topic_str = " | ".join(topics) if topics else "(none)"
    print(f"{wid} | {name} | {wc} works | {aff_name} ({aff_country})")
    print(f"  topics: {topic_str}")
    print()

# Now try looking up by the DOIs we already have for Ping Wang
# OpenAlex has /works?filter=doi:xxx which returns authorships
print("=" * 60)
print("Testing DOI reverse lookup (like our S2 method)...")
print()

test_dois = [
    "10.1021/acs.analchem.5b02434",   # Purdue era
    "10.1117/12.2246098",             # HUST era
    "10.1021/acs.analchem.2c03981",   # recent
    "10.1038/s41467-025-59030-8",     # most recent
]

for doi in test_dois:
    resp = requests.get(
        f"https://api.openalex.org/works/doi:{doi}",
        headers={"User-Agent": "lit-skill/1.0 (mailto:research@example.com)"},
        timeout=10,
    )
    if resp.status_code != 200:
        print(f"  {doi}: HTTP {resp.status_code}")
        continue
    work = resp.json()
    print(f"  {doi}")
    for au in work.get("authorships", []):
        author = au.get("author", {})
        name = author.get("display_name", "")
        aid = author.get("id", "").split("/")[-1] if author.get("id") else ""
        # Check if this looks like our Ping Wang
        if "wang" in name.lower() and name.lower().startswith("p"):
            insts = au.get("institutions", [])
            inst_names = [i.get("display_name", "") for i in insts]
            print(f"    -> {name} (ID: {aid}) | institutions: {inst_names}")
    print()
