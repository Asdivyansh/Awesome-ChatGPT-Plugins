#!/usr/bin/env python3
"""Generate the full plugin catalog from data/plugins.json.

Outputs:
  catalog/README.md        index of every category, with counts
  catalog/<category>.md    one table per official directory category
  data/plugins.csv         flat export for spreadsheets

Usage:
  python3 scripts/build_catalog.py
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "plugins.json"
CATALOG = ROOT / "catalog"
CSV_OUT = ROOT / "data" / "plugins.csv"

# Order and emoji for the official directory categories.
CATEGORIES = [
    ("featured", "⭐"),
    ("new-and-noteworthy", "🆕"),
    ("small-business", "🏪"),
    ("productivity", "⚡"),
    ("creativity", "🎨"),
    ("developer-tools", "💻"),
    ("business-and-operations", "💼"),
    ("data-and-analytics", "📊"),
    ("communication", "💬"),
    ("education-and-research", "🎓"),
    ("scientific-research", "🔬"),
    ("security", "🔐"),
    ("finance", "💰"),
    ("healthcare", "🩺"),
    ("travel", "✈️"),
    ("other", "🧩"),
]
# Curated shelves that overlap the topical categories. They're listed in the
# index but don't get their own catalog page.
SHELVES = {"featured", "new-and-noteworthy", "small-business"}

KIND_LABELS = {
    "app": "Apps SDK app",
    "connector": "Partner connector",
    "openai": "Built by OpenAI",
    "bundle": "Skill bundle",
    "template": "Template",
}


def md_escape(text: str) -> str:
    """Escape text for use inside a markdown table cell."""
    text = re.sub(r"\s+", " ", text or "").strip()
    return text.replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")


def badges(p: dict) -> str:
    out = []
    if p.get("developer") == "OpenAI" or p["kind"] == "openai":
        out.append("💠")
    if p.get("skills"):
        out.append("🧩")
    if p.get("apps"):
        out.append("🔌")
    if p.get("desktop_only"):
        out.append("🖥️")
    return " ".join(out)


def sort_key(p: dict) -> str:
    return re.sub(r"[^a-z0-9]", "", p["name"].lower()) or p["name"].lower()


def anchor_letter(p: dict) -> str:
    first = sort_key(p)[:1].upper()
    return first if first.isalpha() else "#"


def render_table(plugins: list[dict]) -> list[str]:
    lines = [
        "| Plugin | What it does | Developer | Includes |",
        "| --- | --- | --- | :---: |",
    ]
    for p in plugins:
        name = md_escape(p["name"])
        lines.append(
            f"| [{name}]({p['url']}) | {md_escape(p['tagline'])} "
            f"| {md_escape(p.get('developer') or '—')} | {badges(p)} |"
        )
    return lines


LEGEND = (
    "**Legend:** 💠 built by OpenAI · 🧩 ships skills · 🔌 ships an MCP app/connector · "
    "🖥️ desktop app only"
)


def build_category_page(slug: str, emoji: str, meta: dict, plugins: list[dict], snapshot: str) -> str:
    plugins = sorted(plugins, key=sort_key)
    letters: dict[str, list[dict]] = {}
    for p in plugins:
        letters.setdefault(anchor_letter(p), []).append(p)

    out = [
        f"# {emoji} {meta['title']}",
        "",
        f"> {meta['description']}",
        "",
        f"**{len(plugins):,} plugins** in this category of the "
        f"[ChatGPT Plugin Directory](https://chatgpt.com/plugins?category={slug}) "
        f"(snapshot: {snapshot}).",
        "",
    ]
    out += [
        LEGEND,
        "",
        "**Jump to:** " + " · ".join(f"[{l}](#{l.lower() if l != '#' else 'other'})" for l in letters),
        "",
        "[← Back to catalog index](README.md) · [← Back to curated list](../README.md)",
        "",
    ]
    for letter, group in letters.items():
        heading = letter if letter != "#" else "Other"
        out += [f"## {heading}", ""]
        out += render_table(group)
        out.append("")
    return "\n".join(out)


def build_mcp_page(data: dict) -> str:
    """List plugins whose directory page exposes their MCP server endpoint."""
    remote, local = [], []
    for p in sorted(data["plugins"], key=sort_key):
        for srv in p.get("mcp_servers", []):
            (remote if srv["transport"] == "http" else local).append((p, srv))
    out = [
        "# 🔌 Plugins with Public MCP Endpoints",
        "",
        "Some directory listings show the MCP server behind the plugin. Remote (HTTP) servers can usually be "
        "added to any MCP client, such as Codex, Claude, Cursor, VS Code, or the "
        "[MCP Inspector](https://github.com/modelcontextprotocol/inspector), "
        "although most require signing in with the vendor first.",
        "",
        f"**{len(remote)} remote endpoints** and **{len(local)} local (stdio) servers** as of {data['snapshot_date']}.",
        "",
        "[← Back to catalog index](README.md)",
        "",
        "## 🌐 Remote (Streamable HTTP)",
        "",
        "| Plugin | What it does | Endpoint |",
        "| --- | --- | --- |",
    ]
    for p, srv in remote:
        out.append(f"| [{md_escape(p['name'])}]({p['url']}) | {md_escape(p['tagline'])} | `{srv['target']}` |")
    out += [
        "",
        "## 💻 Local (stdio)",
        "",
        "These run on your machine and are mostly used by Codex in the ChatGPT desktop app.",
        "",
        "| Plugin | What it does | Command |",
        "| --- | --- | --- |",
    ]
    for p, srv in local:
        out.append(f"| [{md_escape(p['name'])}]({p['url']}) | {md_escape(p['tagline'])} | `{md_escape(srv['target'])}` |")
    return "\n".join(out)


def build_index(data: dict, by_cat: dict[str, list[dict]]) -> str:
    snapshot = data["snapshot_date"]
    plugins = data["plugins"]
    kinds = Counter(p["kind"] for p in plugins)
    with_skills = sum(1 for p in plugins if p.get("skills"))
    by_openai = sum(1 for p in plugins if p.get("developer") == "OpenAI" or p["kind"] == "openai")
    devs = Counter(p.get("developer") for p in plugins if p.get("developer"))

    out = [
        "# 📚 Full ChatGPT Plugin Catalog",
        "",
        f"Every plugin listed in the public [ChatGPT Plugin Directory](https://chatgpt.com/plugins), "
        f"grouped by OpenAI's official categories. **{len(plugins):,} unique plugins** as of **{snapshot}**.",
        "",
        "> [!NOTE]",
        "> This catalog is **generated** from a directory snapshot by "
        "[`scripts/build_catalog.py`](../scripts/build_catalog.py). Inclusion here is not an endorsement. "
        "For hand-picked recommendations, see the [curated list](../README.md).",
        "",
        "## Categories",
        "",
        "| Category | Plugins | About |",
        "| --- | ---: | --- |",
    ]
    for slug, emoji in CATEGORIES:
        meta = data["categories"].get(slug)
        if not meta:
            continue
        count = len(by_cat.get(slug, []))
        link = f"[{emoji} {meta['title']}]({slug}.md)" if slug not in SHELVES else f"{emoji} {meta['title']} ([below](#{slug}))"
        out.append(f"| {link} | {count:,} | {md_escape(meta['description'])} |")

    out += [
        "",
        "## Directory at a glance",
        "",
        "| Stat | Value |",
        "| --- | ---: |",
        f"| Unique plugins | {len(plugins):,} |",
        f"| Built by OpenAI | {by_openai:,} |",
        f"| Ship at least one skill | {with_skills:,} |",
        f"| Distinct developers | {len(devs):,} |",
    ]
    for kind, n in kinds.most_common():
        out.append(f"| Listing type: {KIND_LABELS.get(kind, kind)} | {n:,} |")

    n_mcp = sum(1 for p in plugins if p.get("mcp_servers"))
    out += [
        f"| Expose their MCP server | {n_mcp:,} ([see list](mcp-endpoints.md)) |",
        "",
        "Want the raw data instead? Use [`data/plugins.json`](../data/plugins.json) "
        "or [`data/plugins.csv`](../data/plugins.csv).",
    ]

    for slug in ("featured", "new-and-noteworthy", "small-business"):
        meta = data["categories"].get(slug)
        if not meta:
            continue
        emoji = dict(CATEGORIES)[slug]
        out += ["", f'<a id="{slug}"></a>', "", f"## {emoji} {meta['title']}", "", f"> {meta['description']}", ""]
        out += render_table(by_cat.get(slug, []))  # keep the directory's own order

    out += ["", LEGEND, ""]
    return "\n".join(out)


def main() -> None:
    data = json.loads(DATA.read_text())
    by_cat: dict[str, list[dict]] = {}
    for p in data["plugins"]:
        for c in p["categories"]:
            by_cat.setdefault(c, []).append(p)
    # Shelves keep the directory's ranking order.
    for slug in SHELVES:
        order = data.get("shelf_order", {}).get(slug)
        if order:
            idx = {pid: i for i, pid in enumerate(order)}
            by_cat[slug] = sorted(by_cat.get(slug, []), key=lambda p: idx.get(p["id"], 1e9))

    CATALOG.mkdir(exist_ok=True)
    for old in CATALOG.glob("*.md"):
        old.unlink()
    for slug, emoji in CATEGORIES:
        if slug in SHELVES or slug not in data["categories"]:
            continue
        page = build_category_page(slug, emoji, data["categories"][slug], by_cat.get(slug, []), data["snapshot_date"])
        (CATALOG / f"{slug}.md").write_text(page + "\n")
    (CATALOG / "README.md").write_text(build_index(data, by_cat) + "\n")
    (CATALOG / "mcp-endpoints.md").write_text(build_mcp_page(data) + "\n")

    fields = ["id", "name", "tagline", "developer", "categories", "kind", "website", "version", "skills", "apps", "capabilities", "url"]
    with CSV_OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for p in sorted(data["plugins"], key=sort_key):
            row = {k: p.get(k, "") for k in fields}
            for k in ("categories", "skills", "apps", "capabilities"):
                row[k] = "; ".join(row[k] or [])
            w.writerow(row)

    print(f"Wrote {len(data['plugins']):,} plugins into {len(list(CATALOG.glob('*.md')))} catalog pages and {CSV_OUT.name}")


if __name__ == "__main__":
    main()
