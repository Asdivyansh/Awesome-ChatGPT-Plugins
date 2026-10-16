# 🏛️ A Short History of ChatGPT Plugins

"Plugin" has meant four different things in ChatGPT since 2023. This page traces the lineage, from the 2023 OpenAPI plugins through GPTs and Apps to today's skill-and-MCP plugins, so you can make sense of old tutorials and new docs.

[← Back to the list](../README.md)

## Contents

- [Timeline](#timeline)
- [Four generations compared](#four-generations-compared)
- [The 2023 plugin era](#the-2023-plugin-era)
- [Iconic 2023 plugins and where they are now](#iconic-2023-plugins-and-where-they-are-now)
- [Legacy resources](#legacy-resources)

## Timeline

Dates marked † come from search snippets of pages that block automated access, or were reported inconsistently. Treat them as approximate.

| Date | Event | Source |
| --- | --- | --- |
| 2023-03-23 | **ChatGPT plugins** announced as a limited alpha: an `ai-plugin.json` manifest plus an OpenAPI spec. OpenAI ships browsing and code-interpreter plugins and open-sources a retrieval plugin. | [OpenAI](https://openai.com/index/chatgpt-plugins/) |
| 2023-05-12 | Web browsing and the plugins beta roll out to all Plus users (70+ plugins at first). | [Release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) † |
| 2023-11-06 | **GPTs** announced at the first DevDay: custom ChatGPTs with instructions, knowledge, and Actions. | [OpenAI](https://openai.com/index/introducing-gpts/) |
| 2024-01-10 | **GPT Store** launches. | [OpenAI](https://openai.com/index/introducing-the-gpt-store/) |
| 2024-03-19 | Plugins beta winds down: no new plugin installs or conversations. | [Help Center](https://help.openai.com/en/articles/8988022-winding-down-the-chatgpt-plugins-beta) † |
| 2024-04-09 | Existing plugin conversations end, and the 2023 plugin era is over. | [Help Center](https://help.openai.com/en/articles/8988022-winding-down-the-chatgpt-plugins-beta) † |
| 2025-06-04 | Connectors expand to deep research and chat. Custom **MCP** connectors arrive in beta. | [Help Center](https://help.openai.com/en/articles/11487775) † |
| 2025-09 | **Developer mode** beta: full MCP client support, including write tools. | [Help Center](https://help.openai.com/en/articles/12584461) † |
| 2025-10-06 | DevDay 2025: **apps in ChatGPT** and the **Apps SDK** preview, built on MCP. Pilot partners: Booking.com, Canva, Coursera, Figma, Expedia, Spotify, Zillow. | [OpenAI](https://openai.com/index/introducing-apps-in-chatgpt/) |
| 2025-11-21 | **MCP Apps** (SEP-1865) proposed by MCP maintainers at OpenAI and Anthropic together with the MCP-UI creators. | [MCP blog](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/) |
| 2025-12-17 | **App submissions open** and the in-product app directory launches. The Apps SDK goes beta, and connectors are renamed apps. | [OpenAI](https://openai.com/index/developers-can-now-submit-apps-to-chatgpt/) |
| 2025-12-19 | **Agent skills** (`SKILL.md`) arrive in Codex. | [Changelog](https://learn.chatgpt.com/docs/changelog#codex-2025-12-19) |
| 2026-01-26 | MCP Apps becomes the first official MCP extension. | [MCP blog](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/) |
| 2026-02-02 | Codex desktop app introduced. | [Changelog](https://learn.chatgpt.com/docs/changelog#codex-2026-02-02) |
| 2026-03-25 | **Plugins launch in Codex**: bundles of skills, app integrations, and MCP config, plus `@plugin-creator`. | [Changelog](https://learn.chatgpt.com/docs/changelog#codex-2026-03-25) |
| 2026-06-12 | Per-app permission levels for users and admins. | [Plugin changelog](https://developers.openai.com/plugins/changelog) |
| 2026-06-22 | `openai/skills` deprecated in favor of `openai/plugins`. | [GitHub](https://github.com/openai/skills) |
| **2026-07-09** | **Apps become plugins.** The App Directory becomes the universal **Plugin Directory** for ChatGPT and Codex, the Codex app merges into the ChatGPT desktop app, and ChatGPT Work launches. | [What's new](https://learn.chatgpt.com/docs/whats-new) · [OpenAI](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) |
| 2026-07 | Codex CLI adds portable **Agent Plugins** packages (`plugin.json`). | [What's new](https://learn.chatgpt.com/docs/whats-new) |
| 2026-07-29 | **Sign in with ChatGPT** beta for select plugins (Airtable, GitLab, HubSpot, Notion, Supabase, Vercel). | [Changelog](https://learn.chatgpt.com/docs/changelog#codex-2026-07-29) |
| 2026-08-25 | Admin plugin for ChatGPT Work and Codex. | [OpenAI](https://openai.com/index/introducing-admin-plugin/) † |
| 2026-09-11 | **Custom GPT retirement** announced: GPTs migrate to plugins, with retirement scheduled for 2026-12-11. | [Migration guide](https://learn.chatgpt.com/docs/migrate-custom-gpts) · [FAQ](https://help.openai.com/en/articles/20001519) † |
| 2026-09-29 | DevDay 2026: **Plugin Extensions**, **MCP Events**, and Sign in with ChatGPT for developers. | [What's new: DevDay 2026](https://learn.chatgpt.com/docs/whats-new/devday-2026) |
| 2026-12-11 | *(scheduled)* Custom GPTs stop running. | [FAQ](https://help.openai.com/en/articles/20001519) † |

## Four generations compared

| | **Plugins (2023–24)** | **GPTs (2023–26)** | **Apps in ChatGPT (2025–26)** | **Plugins (2026–)** |
| --- | --- | --- | --- | --- |
| **Underlying tech** | `/.well-known/ai-plugin.json` + OpenAPI spec for a REST API | Instructions, knowledge files, built-in tools, and **Actions** (OpenAPI) | Apps SDK on **MCP**, which became the MCP Apps standard | **Skills** (`SKILL.md`) + **MCP server** + optional MCP Apps UI, extensions, and hooks |
| **UI** | Text in chat | Text in chat | Widgets: inline, carousel, fullscreen, picture-in-picture | Widgets + sidebar apps, panels, file viewers, rich forms |
| **Where it runs** | ChatGPT (plugin model picker) | ChatGPT | ChatGPT on web, desktop, and mobile | ChatGPT Chat and Work, Codex desktop and CLI |
| **Distribution** | Plugin store (beta) | GPT Store, share links | App directory | Universal Plugin Directory, workspace publishing, Git and npm marketplaces |
| **Who can build** | Waitlisted developers | Any paid user (no code) | Verified developers | Anyone for personal plugins, admins for workspace plugins, verified developers for the public directory |
| **Status** | Retired April 2024 | Retiring December 2026 | Folded into plugins in July 2026 | **Current** |

## The 2023 plugin era

On **March 23, 2023**, OpenAI [announced ChatGPT plugins](https://openai.com/index/chatgpt-plugins/) as a waitlisted alpha. Each plugin was a REST API described by an OpenAPI spec and a manifest hosted at `/.well-known/ai-plugin.json`. ChatGPT read the manifest's `description_for_model` to decide when to call it. OpenAI shipped first-party **Browsing**, **Code Interpreter**, and an open-source **Retrieval** plugin, alongside about a dozen launch partners: Expedia, FiscalNote, Instacart, KAYAK, Klarna, Milo, OpenTable, Shopify, Slack, Speak, Wolfram, and Zapier.

The beta reached all Plus users in May 2023 and grew to roughly 1,000 plugins. When [GPTs](https://openai.com/index/introducing-gpts/) arrived in November 2023, their **Actions** reused the same OpenAPI-plus-auth model. Plugin installs stopped on **March 19, 2024**, and the remaining conversations ended on **April 9, 2024**. None of the 2023 plugins were migrated to the 2026 format.

<details>
<summary><b>What a 2023 manifest looked like</b></summary>

From [openai/plugins-quickstart](https://github.com/openai/plugins-quickstart):

```json
{
  "schema_version": "v1",
  "name_for_human": "TODO List (no auth)",
  "name_for_model": "todo",
  "description_for_human": "Manage your TODO list. You can add, remove and view your TODOs.",
  "description_for_model": "Plugin for managing a TODO list, you can add, remove and view your TODOs.",
  "auth": { "type": "none" },
  "api": { "type": "openapi", "url": "http://localhost:5003/openapi.yaml" },
  "logo_url": "http://localhost:5003/logo.png",
  "contact_email": "legal@example.com",
  "legal_info_url": "http://example.com/legal"
}
```

Today's equivalent is a folder with `plugin.json` ([Agent Plugins](https://agent-plugins.org) schema), `skills/<name>/SKILL.md`, and `mcp.json`. There's no OpenAPI spec. See [Package your plugin](https://developers.openai.com/plugins/build/plugins).

</details>

## Iconic 2023 plugins and where they are now

The **Successor** column is checked against this repo's directory snapshot (October 10, 2026). Some listings are region-limited, so "none found" isn't proof that a plugin doesn't exist.

| 2023 plugin | Type | What it did | Successor (2026) |
| --- | --- | --- | --- |
| Browsing | First-party | Search and read the live web | Built-in ChatGPT search |
| Code Interpreter | First-party | Sandboxed Python, files, and charts | Built-in data analysis |
| Retrieval | First-party (open source) | Semantic search over your documents | File uploads, connected apps, and [Company Knowledge](https://chatgpt.com/plugins/Plugin_b0672f102c2081919b893649fdcfeeaa) |
| Wolfram | Launch partner | Math, data, and computation | [Wolfram](https://chatgpt.com/plugins/plugin_asdk_app_69fe0bf66c8481919c513d799406436e) plugin |
| Expedia | Launch partner | Trip planning with handoff to booking | [Expedia](https://chatgpt.com/plugins/plugin_connector_68e004f14af881919eb50893d3d9f523) plugin |
| Shopify (Shop) | Launch partner | Product search across Shop merchants | [Shopify](https://chatgpt.com/plugins/plugin_asdk_app_69e65c430b3081919aa4d962ab5d1698) plugin (store management) |
| Slack | Launch partner | Query and act on Slack | [Slack](https://chatgpt.com/plugins/plugin_asdk_app_69a1d78e929881919bba0dbda1f6436d) plugin |
| FiscalNote | Launch partner | Legal, political, and regulatory data | [PolicyNote](https://chatgpt.com/plugins/plugin_asdk_app_69a87595e18c81919121d76e18c959bd) plugin |
| OpenTable | Launch partner | Restaurant recommendations with booking links | [OpenTable](https://chatgpt.com/plugins/plugin_asdk_app_6935ba0e15b48191ae8ad5795b213c19) plugin |
| Instacart | Launch partner | Recipes to shopping carts | Instacart app launched December 2025, but it isn't in this repo's public directory snapshot (it may be region-limited) |
| Zapier | Launch partner | Actions across 5,000+ apps | [Zapier MCP](https://docs.zapier.com/mcp/get-started/connect/chatgpt) as a custom MCP server; no public directory listing |
| KAYAK | Launch partner | Flight, hotel, and car search | None found |
| Klarna | Launch partner | Product search and price comparison | None found |
| Speak | Launch partner | AI language tutoring | None found. See [italki](https://chatgpt.com/plugins/plugin_asdk_app_6948af96247c81919904f9478c34334f) and [Preply](https://chatgpt.com/plugins/plugin_asdk_app_69443c60fa6481919e4ecf30e6b382f0) for tutoring |
| Milo | Launch partner | Parenting and family logistics | None (company inactive) |
| Zillow | Early partner (May 2023) | Real-estate listing search | Zillow app launched October 2025, but it isn't in this repo's public directory snapshot. [Redfin](https://chatgpt.com/plugins/plugin_asdk_app_69446e62b0448191925a9c3398500f72) is listed |
| ScholarAI | Community favorite | Paper search with citations | [Consensus](https://chatgpt.com/plugins/plugin_asdk_app_6943e6f4a928819195962de16fb9ffe4), [Elicit](https://chatgpt.com/plugins/plugin_asdk_app_69fcf53d4d8481919b65501a96bbed02), and [Scite](https://chatgpt.com/plugins/plugin_asdk_app_6952b3a3f1e881918951582d59483c78) |
| Show Me Diagrams | Community favorite | Mermaid and PlantUML diagrams in chat | [Mermaid Chart](https://chatgpt.com/plugins/plugin_asdk_app_696609ce0304819185fafa6a660e0f1e), [Figma](https://chatgpt.com/plugins/plugin_connector_68df038e0ba48191908c8434991bbac2) (FigJam), and [Whimsical](https://chatgpt.com/plugins/plugin_asdk_app_69c6561277188191a1beac515a4b2ea4) |
| WebPilot / Link Reader | Community favorite | Read web pages and documents | Built-in browsing and file uploads |
| AskYourPDF | Community favorite | Chat with PDFs | Native file uploads; [Adobe Acrobat](https://chatgpt.com/plugins/plugin_asdk_app_6938a7d323f48191aeabaf579802bf45) for PDF editing |

## Legacy resources

These are historical and don't work with today's plugins.

- [ChatGPT plugins announcement](https://openai.com/index/chatgpt-plugins/) - The original March 2023 launch post.
- [ChatGPT plugins are here!](https://community.openai.com/t/chatgpt-plugins-are-here/115731) - Launch thread with developer reactions (OpenAI Developer Community).
- [OpenAI connects ChatGPT to the internet](https://techcrunch.com/2023/03/23/openai-connects-chatgpt-to-the-internet/) - Launch-day coverage (TechCrunch).
- [Peeking under the hood with ChatGPT plugins](https://www.scalevp.com/blog/peeking-under-the-hood-with-chatgpt-plugins) - How the manifest and `description_for_model` drove tool selection.
- [openai/plugins-quickstart](https://github.com/openai/plugins-quickstart) - "ChatGPT plugin in under 5 minutes" (`ai-plugin.json` + OpenAPI). **Archived.**
- [openai/chatgpt-retrieval-plugin](https://github.com/openai/chatgpt-retrieval-plugin) - The retrieval plugin and vector-DB reference.
- [Winding down the plugins beta](https://help.openai.com/en/articles/8988022-winding-down-the-chatgpt-plugins-beta) - The 2024 shutdown notice.
- [Jeadie/awesome-chatgpt-plugins](https://github.com/Jeadie/awesome-chatgpt-plugins) · [HighwayofLife/awesome-chatgpt-plugins](https://github.com/HighwayofLife/awesome-chatgpt-plugins) · [imaurer/awesome-chatgpt-plugins](https://github.com/imaurer/awesome-chatgpt-plugins) - The 2023 awesome lists (inactive).
- [transitive-bullshit/chatgpt-plugin-ts](https://github.com/transitive-bullshit/chatgpt-plugin-ts) - TypeScript toolkit for 2023 plugins.
- [transitive-bullshit/chatgpt-well-known-plugin-finder](https://github.com/transitive-bullshit/chatgpt-well-known-plugin-finder) - Scanned the top 1M sites for `/.well-known/ai-plugin.json`.
- [cloudflare/chatgpt-plugin](https://github.com/cloudflare/chatgpt-plugin) - Cloudflare Workers examples for 2023 plugins.
