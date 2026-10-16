# Contributing

Thanks for helping make **Awesome ChatGPT Plugins** better! This list has two layers:

| Layer | File(s) | How it's maintained |
| --- | --- | --- |
| **Curated list** | [`README.md`](README.md) | Hand-picked by humans. PRs welcome. |
| **Full catalog** | [`catalog/`](catalog/) + [`data/`](data/) | Generated from the public [ChatGPT Plugin Directory](https://chatgpt.com/plugins) by [`scripts/build_catalog.py`](scripts/build_catalog.py). Don't edit by hand. |

## Adding a plugin to the curated list

A plugin belongs in the README if it is:

1. **Live** in the official [ChatGPT Plugin Directory](https://chatgpt.com/plugins), or is an open-source plugin/MCP server that people can actually install in ChatGPT or Codex.
2. **Genuinely useful.** It does something ChatGPT can't do alone, and the description holds up when you try it.
3. **Not a duplicate.** If a vendor has several listings, pick the official one.

### Entry format

```markdown
- [Plugin Name](https://chatgpt.com/plugins/<plugin_id>) - What it lets you do, in one factual line. 🧩
```

- Link to the plugin's `chatgpt.com/plugins/...` page. Open the plugin in the [directory](https://chatgpt.com/plugins) and copy the URL.
- Keep the description to one line (aim for under 100 characters) and end it with a period. Don't start with the plugin's name, and skip hype words like "best", "powerful", "seamless", or "revolutionary".
- Add `🧩` if the plugin ships skills and `🖥️` if it's desktop-only. If its source is public, append ` · [source](<repo-url>)`.
- Within a section, ⭐ editor's picks come first, then everything else A–Z. Maintainers assign ⭐.
- Edit `README.md` directly. Don't touch the generated `catalog/` and `data/` files.

### Adding a resource (tutorial, tool, framework)

Use the same format and link to the canonical source. Paywalled content and SEO listicles will be declined.

## Updating the full catalog

The catalog is generated from a snapshot of the public directory. The directory sits behind bot protection, so the snapshot runs in your own browser:

1. Open [chatgpt.com/plugins](https://chatgpt.com/plugins), paste [`scripts/scrape_directory.js`](scripts/scrape_directory.js) into the DevTools console, and wait for `directory-snapshot.json` to download (a few minutes).
2. Normalize it into `data/plugins.json`:

   ```bash
   python3 scripts/normalize_snapshot.py ~/Downloads/directory-snapshot.json
   ```

3. Regenerate `catalog/*.md` and `data/plugins.csv`:

   ```bash
   python3 scripts/build_catalog.py
   ```

Put the snapshot date in your PR title. Neither script needs any dependencies beyond Python 3.9+.

## Reporting a problem

- **A listing is dead or misbehaving?** Open an issue using the *Report a plugin* template.
- **A plugin is unsafe or misleading?** Report it to OpenAI from inside ChatGPT, and also open an issue here so we can remove it from the curated list.

## Pull request checklist

- [ ] Searched the README to make sure the entry isn't already there
- [ ] Link points to the official directory page or source repo
- [ ] Description is one line, factual, and ends with a period
- [ ] Entry is in the right section
