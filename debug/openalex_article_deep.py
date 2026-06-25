"""Deep dive into the 'other:article' category — what are they really?"""
import requests, json, time
from collections import Counter, defaultdict

MAILTO = "lit-skill/1.0 (mailto:research@example.com)"
HEADERS = {"User-Agent": MAILTO}

def openalex_get_author_works(openalex_id, max_papers=800):
    all_works = []
    cursor = "*"
    while cursor and len(all_works) < max_papers:
        resp = requests.get("https://api.openalex.org/works", params={
            "filter": f"author.id:{openalex_id}",
            "per-page": 200,
            "cursor": cursor,
            "select": "doi,publication_year,type,title,primary_location,authorships",
        }, headers=HEADERS, timeout=30)
        if resp.status_code != 200:
            break
        data = resp.json()
        works = data.get("results", [])
        if not works:
            break
        all_works.extend(works)
        cursor = data.get("meta", {}).get("next_cursor")
        time.sleep(0.15)
    return all_works


for author, oa_id in [("Ji-Xin Cheng", "A5086153927"), ("Ping Wang", "A5011310852")]:
    print(f"\n{'='*70}")
    print(f"  {author}: 'article' type deep dive")
    print(f"{'='*70}")

    works = openalex_get_author_works(oa_id)

    # Filter to type=article
    articles = [w for w in works if w.get("type") == "article"]

    # Sub-classify by venue and DOI prefix
    venue_counter = Counter()
    doi_prefix_counter = Counter()
    sample_by_venue = defaultdict(list)

    for w in articles:
        doi = (w.get("doi") or "").replace("https://doi.org/", "").lower().strip()
        title = (w.get("title") or "")[:60]
        year = w.get("publication_year", "?")

        loc = w.get("primary_location", {})
        source = loc.get("source", {}) if loc else {}
        venue = source.get("display_name", "(no venue)") if source else "(no venue)"
        venue_type = ""
        if source:
            venue_type = source.get("type", "")

        # Get institutions for this author
        institutions = []
        for au in w.get("authorships", []):
            a = au.get("author", {})
            aid = (a.get("id") or "").split("/")[-1]
            if aid == oa_id:
                institutions = [i.get("display_name", "") for i in au.get("institutions", [])]
                break

        venue_counter[venue] += 1
        prefix = doi.split("/")[0] if "/" in doi else doi[:15]
        doi_prefix_counter[prefix] += 1
        sample_by_venue[venue].append({
            "doi": doi, "title": title, "year": year,
            "institutions": institutions[:2],
            "venue_type": venue_type,
        })

    print(f"\n  Top venues for type='article' ({len(articles)} total):")
    for venue, count in venue_counter.most_common(20):
        samples = sample_by_venue[venue]
        inst_sample = samples[0]["institutions"] if samples else []
        vtype = samples[0].get("venue_type", "") if samples else ""
        print(f"    {count:>4} | {venue[:50]:50s} | type={vtype}")
        # Show one sample
        s = samples[0]
        print(f"         e.g: {s['year']} {s['doi'][:40]} | inst: {inst_sample}")

    print(f"\n  Top DOI prefixes:")
    for prefix, count in doi_prefix_counter.most_common(15):
        print(f"    {prefix:30s} {count:>4}")

    time.sleep(1)
