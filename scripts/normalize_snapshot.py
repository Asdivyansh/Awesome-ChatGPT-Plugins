#!/usr/bin/env python3
"""Convert a raw directory snapshot (from scrape_directory.js) into data/plugins.json.

Usage:
  python3 scripts/normalize_snapshot.py path/to/directory-snapshot.json
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "plugins.json"
SHELVES = ("featured", "new-and-noteworthy", "small-business")


def kind_of(plugin_id: str, developer: str | None) -> str:
    """Classify a listing by its directory ID prefix."""
    if plugin_id.startswith("plugin_connector_1p_"):
        return "openai"
    if plugin_id.startswith("plugin_connector_"):
        return "connector"
    if plugin_id.startswith("plugin_asdk_app_"):
        return "app"
    if plugin_id.startswith("plugin_templated_"):
        return "template"
    if plugin_id.startswith("Plugin_") and developer == "OpenAI":
        return "openai"
    return "bundle"  # packaged plugins: skills and/or MCP servers


MORE = re.compile(r"^\+(\d+) more")
# The directory renders "<name><url-or-command>" as adjacent spans with no separator.
SERVER = re.compile(r"^(.*?)(https?://\S+|\./\S.*|(?:python3?|node|npx|uvx|uv|bunx?|deno|docker|pnpm|java|go|cargo)(?:\s|$).*)$")


def clean_skills(items: list[str]) -> tuple[list[str], int]:
    """Drop the collapsed "+N more..." item and return (visible skills, total count)."""
    visible, hidden = [], 0
    for item in items:
        m = MORE.match(item)
        if m:
            hidden += int(m.group(1))
        else:
            visible.append(item)
    return visible, len(visible) + hidden


def parse_servers(items: list[str], transport: str) -> list[dict]:
    out = []
    for item in items:
        m = SERVER.match(item)
        name, target = (m.group(1), m.group(2)) if m else (item, "")
        out.append({"name": name, "transport": transport, "target": target})
    return out


def split_list(value: str | None) -> list[str]:
    return [s.strip() for s in (value or "").split(",") if s.strip()]


def main(src: str) -> None:
    raw = json.loads(Path(src).read_text())
    details = raw.get("details", {})
    plugins = []
    for pid, p in raw["plugins"].items():
        d = details.get(pid, {})
        sec = d.get("sec", {})
        developer = d.get("Developer")
        skills, skill_count = clean_skills(sec.get("Skill", []) + sec.get("Skills", []))
        plugins.append({
            "id": pid,
            "name": p["n"].strip(),
            "tagline": (p.get("d") or "").strip(),
            "description": d.get("long", ""),
            "developer": developer,
            "website": d.get("Website"),
            "version": d.get("Version"),
            "category_label": d.get("Category"),
            "categories": p["c"],
            "kind": kind_of(pid, developer),
            "capabilities": split_list(d.get("Capabilities")),
            "apps": sec.get("App", []) + sec.get("Apps", []),
            "skills": skills,
            "skill_count": skill_count,
            "mcp_servers": parse_servers(sec.get("MCP Servers", []), "http")
            + parse_servers(sec.get("Local MCP Server (STDIO)", []), "stdio"),
            "starter_prompts": d.get("prompts", []),
            "desktop_only": bool(p.get("desk")),
            "url": f"https://chatgpt.com/plugins/{pid}",
        })
    plugins.sort(key=lambda x: x["name"].lower())
    out = {
        "snapshot_date": raw["snapshot_date"],
        "source": "https://chatgpt.com/plugins",
        "categories": {
            slug: {"title": s["title"], "description": s["desc"], "count": s["n"]}
            for slug, s in raw["stats"].items()
        },
        "shelf_order": {k: v for k, v in raw.get("order", {}).items() if k in SHELVES},
        "plugins": plugins,
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print(f"Wrote {len(plugins):,} plugins ({sum(1 for p in plugins if p['developer'])} with details) to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
