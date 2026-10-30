"""Rebuild the index table in SKILL.md from the YAML front matter of every card in papers/.

Usage (from the skill folder):  python scripts/build_index.py
Only standard-library Python is needed.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
START, END = "<!-- index:start -->", "<!-- index:end -->"
REQUIRED = ["id", "authors", "year", "journal", "doi", "gist", "keywords", "data"]


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
    if missing:
        raise SystemExit(f"{path.name}: missing {', '.join(missing)}")
    if meta["id"] != path.stem:
        raise SystemExit(f"{path.name}: id '{meta['id']}' must match the file name")
    return meta


def short_ref(meta):
    # "van Etten J" -> "van Etten": drop the trailing initials, keep particles
    parts = meta["authors"].split(",")[0].strip().split(" ")
    surname = " ".join(parts[:-1]) if len(parts) > 1 else parts[0]
    journal = meta.get("journal_short") or meta["journal"]
    return f"{surname} et al. {meta['year']}, *{journal}*"


def short_data(value):
    v = value.lower()
    for name in ["dataverse", "zenodo", "github", "figshare", "dryad"]:
        if name in v:
            return name.capitalize() if name != "github" else "GitHub"
    return "none" if v.startswith("none") else "see card"


cards = sorted((ROOT / "papers").glob("*.md"))
rows = ["| ID | Paper | Gist | Keywords | Data |", "|---|---|---|---|---|"]
for p in sorted(cards, key=lambda c: front_matter(c)["year"]):
    m = front_matter(p)
    kw = ", ".join(k.strip() for k in m["keywords"].split(",")[:6])
    rows.append(f"| [{m['id']}](papers/{p.name}) | {short_ref(m)} | {m['gist']} | {kw} | {short_data(m['data'])} |")

skill = ROOT / "SKILL.md"
text = skill.read_text(encoding="utf-8")
if START not in text or END not in text:
    raise SystemExit("SKILL.md needs the index:start and index:end markers")
new = re.sub(re.escape(START) + r".*?" + re.escape(END), START + "\n" + "\n".join(rows) + "\n" + END, text, flags=re.S)
skill.write_text(new, encoding="utf-8")
print(f"Index rebuilt with {len(cards)} papers. SKILL.md is {len(new.encode())} bytes.")
