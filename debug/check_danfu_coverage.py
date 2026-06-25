"""Check Dan Fu's Zotero collection year coverage."""
import json, sqlite3

with open("people/Dan_Fu/profile.json") as f:
    p = json.load(f)

print("S2 IDs:", p.get("s2_ids"))
print("S2 counts:", p.get("s2_paper_counts"))
print("Zotero collection:", p.get("zotero_collection"))
print()

db_name = p.get("zotero_collection", "Dan Fu")
zotero_db = "C:/Users/Ivanz/Zotero/zotero.sqlite"
conn = sqlite3.connect(zotero_db)

rows = conn.execute("""
    SELECT DISTINCT idv.value
    FROM collectionItems ci
    JOIN collections c ON ci.collectionID = c.collectionID
    JOIN itemData id ON ci.itemID = id.itemID
    JOIN fields f ON id.fieldID = f.fieldID
    JOIN itemDataValues idv ON id.valueID = idv.valueID
    WHERE c.collectionName = ? AND f.fieldName = 'date'
    ORDER BY idv.value
""", (db_name,)).fetchall()

years = sorted(set(r[0][:4] for r in rows if r[0] and r[0][:4].isdigit()))
print(f"Years in Zotero ({len(years)}): {years}")

# Also check total papers
count = conn.execute("""
    SELECT COUNT(DISTINCT ci.itemID)
    FROM collectionItems ci
    JOIN collections c ON ci.collectionID = c.collectionID
    WHERE c.collectionName = ?
""", (db_name,)).fetchone()[0]
print(f"Total papers in collection: {count}")

conn.close()
