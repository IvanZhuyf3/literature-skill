"""Check Delong Zhang's actual affiliation strings from CrossRef per year."""
import json, requests, time

dois = [
    ("2011", "10.1021/jz200516n"),
    ("2013", "10.1021/ac3019119"),
    ("2014", "10.1021/ar400331q"),
    ("2015", "10.1021/acs.analchem.5b02434"),
    ("2016", "10.1126/sciadv.1600521"),
    ("2017", "10.1021/acs.jpclett.7b00575"),
    ("2019", "10.1126/sciadv.aav7127"),
    ("2022", "10.1002/lpor.202100719"),
    ("2024", "10.1039/d4sc03985h"),
    ("2025", "10.1002/anie.202505038"),
    ("2026", "10.1002/viw.20250199"),
]

for year, doi in dois:
    try:
        resp = requests.get(
            f"https://api.crossref.org/works/{doi}",
            headers={"User-Agent": "lit-skill/1.0 (mailto:research@example.com)"},
            timeout=10,
        )
        if resp.status_code != 200:
            print(f"{year} {doi}: HTTP {resp.status_code}")
            continue
        authors = resp.json()["message"].get("author", [])
        for a in authors:
            fn = a.get("family", "").lower()
            gn = a.get("given", "").lower()
            if fn == "zhang" and gn.startswith("d"):
                affs = [aff.get("name", "") for aff in a.get("affiliation", [])]
                print(f"{year} {doi}:")
                for aff in affs:
                    print(f"  -> {aff}")
                break
    except Exception as e:
        print(f"{year} {doi}: ERROR {e}")
    time.sleep(0.5)
