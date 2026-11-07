"""Rebuild the topic map in SKILL.md, the index table in index.md, and index.json from the YAML front matter
of every card in papers/.

index.json carries a content-based version and a hash per card, so an assistant can
compare its installed copy with the live repository and fetch only what changed.

Usage (from the repository root):  python scripts/build_index.py
Only standard-library Python is needed.

Rules checked for every card
- required fields are present and filled
- the doi field is present; it may be empty for items still waiting for their handle
- the id matches the file name
- card and PDF file names are all lowercase (papers/*.md and papers-pdf/*.pdf)
- every relation uses a known CiTO term and points to an existing card
- peer_reviewed and curated_card are yes or no
- source is team or external; a team card should have at least one author listed in people.md
  (a warning only, since author lists may be shortened or name an institution)

Relations are declared in the card front matter as a YAML list, one per line:

relations:
  - extends: mancini-2017-scirep
  - citesAsDataSource: desousa-2024-asd  # optional note after a hash

The version combines the hashes of every card, people.md and the instructions in SKILL.md
(without its generated blocks), so editing any of them produces a new version.

The script adds the inverse links and writes the graph to index.json and relations.jsonld
(JSON-LD with the CiTO vocabulary).

SKILL.md carries a short topic map (card ids grouped by question area and by crop) so the
skill stays under about 20 KB as cards are added. Topics and crops are assigned by matching
the patterns in TOPICS and CROPS against each card's keywords, gist and type. Every card must
fall in at least one topic; the script stops with an error otherwise. The full table with
the gist of every paper is written to index.md, which assistants open only as a fallback.

It also rewrites the status table in README.md, between the status markers, so the counts
of PDFs, cards, people and links always match the repository. Run it after any change to a
card, a PDF or people.md.
"""
import datetime
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
START, END = "<!-- index:start -->", "<!-- index:end -->"  # in index.md
TSTART, TEND = "<!-- topics:start -->", "<!-- topics:end -->"  # in SKILL.md
VSTART, VEND = "<!-- version:start -->", "<!-- version:end -->"
RAW = "https://raw.githubusercontent.com/AgrDataSci/tricot-knowledge-base/main/"
RSTART, REND = "<!-- relations:start -->", "<!-- relations:end -->"
SSTART, SEND = "<!-- status:start -->", "<!-- status:end -->"
# CiTO terms (http://purl.org/spar/cito/) and their inverses
RELATIONS = {
    "extends": "isExtendedBy",
    "reviews": "isReviewedBy",
    "updates": "isUpdatedBy",
    "usesDataFrom": "providesDataFor",
    "usesMethodIn": "providesMethodFor",
    "citesAsDataSource": "isCitedAsDataSourceBy",
    "agreesWith": "isAgreedWithBy",
    "disagreesWith": "isDisagreedWithBy",
    "discusses": "isDiscussedBy",
}
REQUIRED = ["id", "title", "authors", "year", "journal", "type", "source", "peer_reviewed", "curated_card",
            "gist", "keywords", "data"]
YESNO = ["peer_reviewed", "curated_card"]  # must be yes or no
SOURCES = {"team": "team", "external": "external, curated"}  # value -> label in the index
PRESENT = ["doi", "open_copy", "license"]  # must exist, may be empty

# Topic map in SKILL.md. Each pattern is a regular expression matched, case-insensitive and on
# word boundaries, against a card's keywords, gist and type. A card can sit in several topics.
TOPICS = [
    ("Origins of tricot, guides and the handbook", r"tricot origin|tricot guide|tricot handbook|ten steps|guide|book|retrospective"),
    ("Trial design, sample size and data quality", r"sample size|sample-size|data quality|validity|trial design|trial size|plot size|incomplete block|trial dimensions|sampling"),
    ("Who hosts trials and representativeness", r"host farmer|farm typology|representativeness|external validity|selection bias|research population|site selection|target population of environments|tpe"),
    ("Ranking data analysis and statistics", r"plackett-luce|plackett-luce trees|ranking data|partial rankings|bradley-terry|thurstonian|rank aggregation|variance components|gge biplot"),
    ("Climate and environmental covariates", r"climate|rainfall|chirps|temperature|agera5|environmental|dry spell|heat|frost|precipitation"),
    ("Gender, social inclusion and farmer segments", r"gender|women|intersectionality|social inclusion|youth|farmer segments|user segments|farmer segmentation|household heterogeneity|household type|intrahousehold"),
    ("Trait preferences, product profiles and demand-led breeding", r"trait preferences?|trait prioritization|product profiles?|demand-led|demand-driven|market segments?|market segmentation|market preference"),
    ("Consumer testing and food quality", r"consumer|sensory|food quality|gari|eba|taste|texture|tasting"),
    ("Product concept testing and seed choice", r"vpct|product concept|seed choice|seed products?|agro-dealer|seed price"),
    ("Genebanks, genomics and pre-breeding", r"genebanks?|genebank accessions|genomic|gwas|qtl|landraces|3d.breeding|etnam|pre-breeding|nested association|heritability"),
    ("Yield measured by farmers and genetic gain", r"farmer-generated yield|yield estimation|volumetric|harvest measurement|genetic gain|absolute yield"),
    ("Costs and budgeting", r"cost|costing|budget|budgeting|cost per farmer"),
    ("Farmer motivation, participation and feedback", r"motivation|incentives|farmer feedback|feedback sessions|reciprocity|participatory research|farmers' experiments|farmer participation"),
    ("Impact, adoption, variety release and institutionalization", r"impact|adoption|institutionalization|outcome study|agricultural policy|variety release|scaling|mainstreaming|varietal turnover"),
    ("Data standards, ontologies and software", r"ontolog\w*|fair data|fair principles|care principles|brapi|data standards|software design|r package|api|sikia|data governance|data integration|metadata"),
]
CROPS = [
    ("amaranth and other opportunity crops", r"amaranth|opportunity crops|nus|neglected and underutilized"),
    ("banana", r"musa|black sigatoka|black leaf streak"),
    ("cassava", r"cassava|gari|eba|fufu"),
    ("common bean", r"common bean|bean"),
    ("forages", r"forages?|grassland|grass-legume"),
    ("groundnut", r"groundnut"),
    ("maize", r"maize"),
    ("potato", r"potato"),
    ("rice", r"rice"),
    ("sorghum", r"sorghum"),
    ("sweetpotato", r"sweetpotato"),
    ("teff", r"teff"),
    ("wheat", r"wheat"),
]


def matches(meta, pattern):
    text = " ".join([meta["keywords"], meta["gist"], meta["type"]]).lower()
    return re.search(r"\b(?:" + pattern + r")\b", text) is not None


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise SystemExit(f"{path.name}: no front matter")
    meta = {"relations": []}
    in_rel = False
    for line in m.group(1).splitlines():
        if in_rel and line.lstrip().startswith("- "):
            item, _, note = line.lstrip()[2:].partition("#")
            rel, _, target = item.partition(":")
            meta["relations"].append({"type": rel.strip(), "target": target.strip(), "note": note.strip()})
            continue
        in_rel = False
        if line.startswith("relations:"):
            in_rel = True
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    missing = [k for k in REQUIRED if not meta.get(k)]
    missing += [k for k in PRESENT if k not in meta]
    if missing:
        raise SystemExit(f"{path.name}: missing {', '.join(missing)}")
    if meta["id"] != path.stem:
        raise SystemExit(f"{path.name}: id '{meta['id']}' must match the file name")
    if meta["source"] not in SOURCES:
        raise SystemExit(f"{path.name}: source '{meta['source']}' must be one of {', '.join(SOURCES)}")
    for k in YESNO:
        if meta[k] not in ("yes", "no"):
            raise SystemExit(f"{path.name}: {k} '{meta[k]}' must be yes or no")
    return meta


def people_surnames():
    # surnames of everyone in the people.md tables, e.g. "Kauê de Sousa" -> "de sousa"
    path = ROOT / "people.md"
    if not path.exists():
        return []
    names = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| ") and not line.startswith("| Person"):
            words = line.split("|")[1].strip().split(" ")
            i = next((k for k, w in enumerate(words[1:], 1) if w[:1].islower()), len(words) - 1)
            names.append(" ".join(words[i:]).lower())
    return names


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
upper = [f"papers/{p.name}" for p in cards if p.name != p.name.lower()]
upper += [f"papers-pdf/{p.name}" for p in sorted((ROOT / "papers-pdf").glob("*")) if p.suffix.lower() == ".pdf" and p.name != p.name.lower()]
if upper:
    raise SystemExit("File names must be all lowercase. Rename: " + ", ".join(upper))
metas = [(front_matter(p), p) for p in cards]
metas.sort(key=lambda x: (x[0]["year"], x[0]["id"]))
rows = ["| ID | Paper | Type | Peer-reviewed | Source | Gist | Keywords | Data |", "|---|---|---|---|---|---|---|---|"]
for m, p in metas:
    kw = ", ".join(k.strip() for k in m["keywords"].split(",")[:5])
    rows.append(f"| [{m['id']}](papers/{p.name}) | {short_ref(m)} | {m['type']} | {m['peer_reviewed']} | {SOURCES[m['source']]} | {m['gist']} | {kw} | {short_data(m['data'])} |")

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


ids = {m["id"] for m, _ in metas}
links = []  # (source, relation, target, note)
for m, p in metas:
    for r in m["relations"]:
        if r["type"] not in RELATIONS:
            raise SystemExit(f"{p.name}: unknown relation '{r['type']}'. Use one of {', '.join(RELATIONS)}")
        if r["target"] not in ids:
            raise SystemExit(f"{p.name}: relation target '{r['target']}' is not a card")
        links.append((m["id"], r["type"], r["target"], r["note"]))
graph = {i: [] for i in ids}
for a, rel, b, note in links:
    graph[a].append({"relation": rel, "card": b, "note": note})
    graph[b].append({"relation": RELATIONS[rel], "card": a, "note": note})

people = ROOT / "people.md"
entries = [{"id": m["id"], "year": m["year"], "type": m["type"], "source": m["source"],
            "peer_reviewed": m["peer_reviewed"], "curated_card": m["curated_card"], "gist": m["gist"],
            "keywords": m["keywords"], "path": f"papers/{p.name}", "hash": digest(p),
            "relations": graph[m["id"]],
            **({"not_established": m["not_established"]} if m.get("not_established") else {})} for m, p in metas]
people_hash = digest(people) if people.exists() else ""


def instructions_hash(text):
    # hash SKILL.md without its generated blocks, so only instruction edits change it
    for a, b in [(TSTART, TEND), (VSTART, VEND), (START, END), (RSTART, REND)]:
        text = re.sub(re.escape(a) + r".*?" + re.escape(b), a + b, text, flags=re.S)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


skill_hash = instructions_hash((ROOT / "SKILL.md").read_text(encoding="utf-8"))
install = ROOT / "INSTALL.md"
install_hash = digest(install) if install.exists() else ""
version = hashlib.sha256(("".join(e["hash"] for e in entries) + people_hash + skill_hash + install_hash).encode()).hexdigest()[:12]

index_path = ROOT / "index.json"
updated = datetime.date.today().isoformat()
if index_path.exists():
    old = json.loads(index_path.read_text(encoding="utf-8"))
    if old.get("version") == version:
        updated = old.get("updated", updated)  # unchanged content keeps its date
index = {"version": version, "updated": updated, "cards": len(entries), "raw_base": RAW,
         "skill": {"path": "SKILL.md", "hash": skill_hash},
         "people": {"path": "people.md", "hash": people_hash},
         "install": {"path": "INSTALL.md", "hash": install_hash},
         "index_table": {"path": "index.md"}, "papers": entries}
index_path.write_text(json.dumps(index, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

# JSON-LD export of the citation graph with the CiTO vocabulary
def node_id(meta):
    return meta["doi"] or f"{RAW}papers/{meta['id']}.md"
by_id = {m["id"]: m for m, _ in metas}
nodes = []
for m, _ in metas:
    node = {"@id": node_id(m), "dcterms:identifier": m["id"], "dcterms:title": m["title"],
            "dcterms:date": m["year"], "fabio:hasURL": f"{RAW}papers/{m['id']}.md"}
    for a, rel, b, note in links:
        if a == m["id"]:
            node.setdefault(f"cito:{rel}", []).append({"@id": node_id(by_id[b])})
    nodes.append(node)
jsonld = {"@context": {"cito": "http://purl.org/spar/cito/", "dcterms": "http://purl.org/dc/terms/",
                       "fabio": "http://purl.org/spar/fabio/"}, "@graph": nodes}
(ROOT / "relations.jsonld").write_text(json.dumps(jsonld, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

# Topic map in SKILL.md and full table in index.md
untopiced = [m["id"] for m, _ in metas if not any(matches(m, pat) for _, pat in TOPICS)]
if untopiced:
    raise SystemExit("Cards in no topic. Add a keyword to the card or a pattern to TOPICS: " + ", ".join(untopiced))
newest_first = sorted(metas, key=lambda x: (x[0]["year"], x[0]["id"]), reverse=True)
topic_lines = ["### By question", ""]
for name, pat in TOPICS:
    hits = [m["id"] for m, _ in newest_first if matches(m, pat)]
    topic_lines.append(f"- **{name}.** " + ", ".join(hits))
topic_lines += ["", "### By crop", ""]
for name, pat in CROPS:
    hits = [m["id"] for m, _ in newest_first if matches(m, pat)]
    if hits:
        topic_lines.append(f"- **{name}.** " + ", ".join(hits))

index_md = ROOT / "index.md"
index_md.write_text(
    "# Index of cards\n\n"
    "Generated by `scripts/build_index.py`. Do not edit by hand. One row per card, oldest first, with the gist of each paper. "
    "Assistants route questions with the topic map in `SKILL.md` and open this table only when the map does not settle which cards to read.\n\n"
    + START + "\n" + "\n".join(rows) + "\n" + END + "\n", encoding="utf-8")

skill = ROOT / "SKILL.md"
text = skill.read_text(encoding="utf-8")
for a, b in [(TSTART, TEND), (VSTART, VEND)]:
    if a not in text or b not in text:
        raise SystemExit(f"SKILL.md needs the {a} and {b} markers")
new = re.sub(re.escape(TSTART) + r".*?" + re.escape(TEND), TSTART + "\n" + "\n".join(topic_lines) + "\n" + TEND, text, flags=re.S)
stamp = f"Installed version `{version}`, updated {updated}, {len(entries)} cards."
new = re.sub(re.escape(VSTART) + r".*?" + re.escape(VEND), VSTART + stamp + VEND, new, flags=re.S)
skill.write_text(new, encoding="utf-8")
no_doi = [m["id"] for m, _ in metas if not m["doi"] and m["type"] != "flyer"]  # flyers have no handle
team_names = people_surnames()
unmatched = [m["id"] for m, _ in metas if m["source"] == "team"
             and not any(n in m["authors"].lower() for n in team_names)]
external = [m["id"] for m, _ in metas if m["source"] == "external"]
not_pr = [m["id"] for m, _ in metas if m["peer_reviewed"] == "no"]
to_curate = [m["id"] for m, _ in metas if m["curated_card"] == "no"]
print(f"{len(links)} relations between cards.")
print(f"Index rebuilt with {len(cards)} papers. Version {version} ({updated}). SKILL.md is {len(new.encode())} bytes.")
if len(new.encode()) > 20480:
    print("Warning: SKILL.md is over the 20 KB budget. Move detail to a file opened on demand.")
if no_doi:
    print(f"{len(no_doi)} cards still need a handle or DOI: {', '.join(no_doi)}")
print(f"{len(metas) - len(external)} team cards, {len(external)} external cards curated by the core team.")
not_pr = [m["id"] for m, _ in metas if m["peer_reviewed"] == "no"]
print(f"{len(metas) - len(not_pr)} peer-reviewed cards, {len(not_pr)} not peer-reviewed.")
to_curate = [m["id"] for m, _ in metas if m["curated_card"] == "no"]
print(f"{len(metas) - len(to_curate)} cards checked by a person, {len(to_curate)} still to check.")
if unmatched:
    print(f"Check source: team cards with no author found in people.md: {', '.join(unmatched)}")

# Status table in README.md
readme = ROOT / "README.md"
rtext = readme.read_text(encoding="utf-8")
if SSTART not in rtext or SEND not in rtext:
    raise SystemExit(f"README.md needs the {SSTART} and {SEND} markers")
pdfs = len(list((ROOT / "papers-pdf").glob("*.pdf")))
contacts = [line.split("|")[8].strip().lower() for line in people.read_text(encoding="utf-8").splitlines()
            if line.startswith("| ") and not line.startswith("| Person") and line.count("|") >= 10]
n_yes = sum(c.startswith("yes") for c in contacts)
n_no = sum(c.startswith("no") for c in contacts)
status = [
    "| | Count |", "|---|---|",
    f"| Source documents in `papers-pdf/` | {pdfs} |",
    f"| Cards in `papers/` | {len(metas)} ({len(metas) - len(external)} team, {len(external)} external) |",
    f"| Cards still waiting for a handle or DOI | {len(no_doi)} |",
    f"| Peer-reviewed cards | {len(metas) - len(not_pr)} ({len(not_pr)} not peer-reviewed) |",
    f"| Cards checked by a person (`curated_card: yes`) | {len(metas) - len(to_curate)} of {len(metas)} |",
    f"| People in `people.md` | {len(contacts)} ({n_yes} agreed to be contacted, {len(contacts) - n_yes - n_no} pending, {n_no} declined) |",
    f"| Links between cards | {len(links)} |",
]
rnew = re.sub(re.escape(SSTART) + r".*?" + re.escape(SEND), SSTART + "\n" + "\n".join(status) + "\n" + SEND, rtext, flags=re.S)
readme.write_text(rnew, encoding="utf-8")
print(f"README status updated: {pdfs} PDFs, {len(metas)} cards, {len(contacts)} people.")
