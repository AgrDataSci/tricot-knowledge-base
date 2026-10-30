"""Rebuild the index table in SKILL.md and index.json from the YAML front matter of every card in papers/.

index.json carries a content-based version and a hash per card, so an assistant can
compare its installed copy with the live repository and fetch only what changed.

Usage (from the repository root):  python scripts/build_index.py
Only standard-library Python is needed.

Rules checked for every card
- required fields are present and filled
- the doi field is present; it may be empty for CGSpace items still waiting for their handle
- the id matches the file name
"""
import datetime
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
START, END = "<!-- index:start -->", "<!-- index:end -->"
VSTART, VEND = "<!-- version:start -->", "<!-- version:end -->"
RAW = "https://raw.githubusercontent.com/AgrDataSci/tricot-knowledge-base/main/"
REQUIRED = ["id", "title", "authors", "year", "journal", "type", "gist", "keywords", "data"]
PRESENT = ["doi", "open_copy", "license"]  # must exist, may be empty


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise SystemExit(f"{path.name}: no front matter")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    missing = [k for k in REQUIRED if not meta.get(k)]
    missing += [k for k in PRESENT if k not in meta]
    if missing:
        raise SystemExit(f"{path.name}: missing {', '.join(missing)}")
    if meta["id"] != path.stem:
        raise SystemExit(f"{path.name}: id '{meta['id']}' must match the file name")
    return meta


def surname(author):
    # "van Etten J" -> "van Etten"; an organization name is kept whole
    parts = author.strip().split(" ")
    if len(parts) > 1 and re.fullmatch(r"[A-ZÀ-Ý]{1,3}", parts[-1]):
        return " ".join(parts[:-1])
    return author.strip()


def short_ref(meta):
    authors = [a for a in meta["authors"].split(",") if a.strip() and "co-author" not in a]
    first = surname(authors[0])
    if len(authors) == 2 and "and" not in meta["authors"]:
        who = f"{first} and {surname(authors[1])}"
    elif len(authors) == 1 and "co-author" not in meta["authors"]:
        who = first
    else:
        who = f"{first} et al."
    journal = meta.get("journal_short") or meta["journal"]
    return f"{who} {meta['year']}, *{journal}*"


def short_data(value):
    v = value.lower()
    for name in ["dataverse", "zenodo", "github", "figshare", "dryad"]:
        if name in v:
            return name.capitalize() if name != "github" else "GitHub"
    return "none" if v.startswith("none") else "see card"


cards = sorted((ROOT / "papers").glob("*.md"))
metas = [(front_matter(p), p) for p in cards]
metas.sort(key=lambda x: (x[0]["year"], x[0]["id"]))
rows = ["| ID | Paper | Type | Gist | Keywords | Data |", "|---|---|---|---|---|---|"]
for m, p in metas:
    kw = ", ".join(k.strip() for k in m["keywords"].split(",")[:5])
    rows.append(f"| [{m['id']}](papers/{p.name}) | {short_ref(m)} | {m['type']} | {m['gist']} | {kw} | {short_data(m['data'])} |")

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


people = ROOT / "people.md"
entries = [{"id": m["id"], "year": m["year"], "type": m["type"], "gist": m["gist"],
            "keywords": m["keywords"], "path": f"papers/{p.name}", "hash": digest(p)} for m, p in metas]
people_hash = digest(people) if people.exists() else ""
version = hashlib.sha256(("".join(e["hash"] for e in entries) + people_hash).encode()).hexdigest()[:12]

index_path = ROOT / "index.json"
updated = datetime.date.today().isoformat()
if index_path.exists():
    old = json.loads(index_path.read_text(encoding="utf-8"))
    if old.get("version") == version:
        updated = old.get("updated", updated)  # unchanged content keeps its date
index = {"version": version, "updated": updated, "cards": len(entries), "raw_base": RAW,
         "people": {"path": "people.md", "hash": people_hash}, "papers": entries}
index_path.write_text(json.dumps(index, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

skill = ROOT / "SKILL.md"
text = skill.read_text(encoding="utf-8")
for a, b in [(START, END), (VSTART, VEND)]:
    if a not in text or b not in text:
        raise SystemExit(f"SKILL.md needs the {a} and {b} markers")
new = re.sub(re.escape(START) + r".*?" + re.escape(END), START + "\n" + "\n".join(rows) + "\n" + END, text, flags=re.S)
stamp = f"Installed version `{version}`, updated {updated}, {len(entries)} cards."
new = re.sub(re.escape(VSTART) + r".*?" + re.escape(VEND), VSTART + stamp + VEND, new, flags=re.S)
skill.write_text(new, encoding="utf-8")
no_doi = [m["id"] for m, _ in metas if not m["doi"]]
print(f"Index rebuilt with {len(cards)} papers. Version {version} ({updated}). SKILL.md is {len(new.encode())} bytes.")
if no_doi:
    print(f"{len(no_doi)} cards still need a handle or DOI: {', '.join(no_doi)}")
