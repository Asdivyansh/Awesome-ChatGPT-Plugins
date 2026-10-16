# 🛠️ Building and Publishing a ChatGPT Plugin

A condensed, link-heavy field guide to building a plugin and getting it into the [Plugin Directory](https://chatgpt.com/plugins) (as of October 2026). Always check the [official docs](https://developers.openai.com/plugins) before you submit. Requirements change often.

[← Back to the list](../README.md)

## Contents

- [Pick a plugin shape](#pick-a-plugin-shape)
- [The build path](#the-build-path)
- [Package format](#package-format)
- [Submission checklist](#submission-checklist)
- [Listing limits](#listing-limits)
- [Monetization rules](#monetization-rules)
- [After you publish](#after-you-publish)
- [Already have a Claude plugin?](#already-have-a-claude-plugin)

## Pick a plugin shape

| Shape | Contains | Good for | Review effort |
| --- | --- | --- | --- |
| **Skills-only** | `skills/*/SKILL.md` | Workflows, playbooks, house style, coding conventions | Light: automated skill scan, no test cases |
| **MCP-only** | One remote MCP server | Connecting a product's data and actions | Full MCP review |
| **Skills + MCP** | Both | Most vendor plugins: tools plus "how to use them well" | Full MCP review |
| **+ UI** | MCP tools that return [MCP Apps](https://modelcontextprotocol.io/docs/extensions/apps) resources | Maps, carousels, editors, checkout, games | Full MCP review + UI guidelines |

Read [Plugin architecture](https://developers.openai.com/plugins/concepts/plugins) and [Skills](https://developers.openai.com/plugins/concepts/skills) to choose.

## The build path

1. **Plan:** [Brainstorm use cases](https://developers.openai.com/plugins/plan/use-case) → [Define tools](https://developers.openai.com/plugins/plan/tools)
2. **Build the server:** [Build an MCP server](https://developers.openai.com/plugins/build/mcp-server) (TypeScript or Python) or start from the [MCP server + UI quickstart](https://developers.openai.com/plugins/build/app-quickstart)
3. **Add skills:** [Build skills](https://developers.openai.com/plugins/build/skills), or scaffold them with `@skill-creator`
4. **Add UI (optional):** [Add UI to your MCP server](https://developers.openai.com/plugins/build/chatgpt-ui) · [UI guidelines](https://developers.openai.com/plugins/concepts/ui-guidelines) · [`@openai/apps-sdk-ui`](https://openai.github.io/apps-sdk-ui/)
5. **Add auth:** [Authentication](https://developers.openai.com/plugins/build/auth) (OAuth 2.1, DCR, CIMD)
6. **Test:** [Connect and test](https://developers.openai.com/plugins/deploy/connect-chatgpt) with the MCP Inspector and a personal plugin ([Add custom MCP server](https://developers.openai.com/api/docs/guides/custom-mcp-server))
7. **Tune discovery:** [Optimize metadata](https://developers.openai.com/plugins/guides/optimize-metadata) with a golden prompt set
8. **Package and submit:** [Package your plugin](https://developers.openai.com/plugins/build/plugins) → [Upload and submit](https://developers.openai.com/plugins/deploy/submission)

> [!TIP]
> The fastest start is **[Plugin Creator](https://learn.chatgpt.com/docs/build-plugins)** (`@plugin-creator`). It scaffolds the manifest and folders and a local marketplace entry so you can install and test before submitting.

## Package format

Upload a **ZIP** at [platform.openai.com/plugins](https://platform.openai.com/plugins) containing either:

```text
my-plugin/
├── plugin.json        # Agent Plugins manifest (agent-plugins.org)
├── mcp.json           # one remote MCP server
└── skills/
    └── triage/
        └── SKILL.md
```

or a Codex-style `.codex-plugin/plugin.json` with `.mcp.json`.

**Constraints:**

- **One MCP server** per plugin, and you can't add one to an existing skills-only plugin.
- Packages with `.app.json` app references or **lifecycle hooks** can't be submitted.
- **No secrets in the ZIP.** The manifest rejects `clientSecret`, `test_credentials`, and `reviewer_instructions`.

## Submission checklist

- [ ] **Verified identity.** Individual or business verification in your OpenAI Platform org settings. You need org owner rights or the `api.apps.write` permission.
- [ ] **Public HTTPS MCP server** using **streamable HTTP** (usually `/mcp`). Local, tunnel-only, and stdio-only servers aren't accepted, and neither are `.mcpb` files.
- [ ] **Domain verification.** Serve the portal's token at `https://<host>/.well-known/openai-apps-challenge`.
- [ ] **Auth is none, OAuth, or mixed.** There's no API-key or bearer-token flow.
- [ ] **Tool annotations.** Explicit `readOnlyHint`, `destructiveHint`, and `openWorldHint` booleans on every tool.
- [ ] **Exactly 5 positive and 3 negative test cases**, a **demo recording URL**, and release notes.
- [ ] **Reviewer test account** with sample data. It can't use MFA, SMS or email codes, magic links, or a private network.
- [ ] **Website, support, privacy policy, and terms URLs**, all HTTPS.
- [ ] **Works on desktop and mobile.** No ads, no "trial" or demo-only plugins, content suitable for ages 13+.
- [ ] **Naming.** Don't append "MCP", "MCP Server", or "Plugin" to the name, and avoid generic dictionary-word names.
- [ ] **Data minimization.** Don't collect PCI, PHI, government IDs, or credentials, and don't send full chat history or precise location in tool inputs.

Sources: [Submission](https://developers.openai.com/plugins/deploy/submission) · [Remote MCP review requirements](https://developers.openai.com/plugins/deploy/app-review) · [Plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines) · [Submission errors](https://developers.openai.com/plugins/deploy/submission-errors)

## Listing limits

| Field | Limit |
| --- | --- |
| Display name | ≤ 30 characters |
| Short description | ≤ 30 characters |
| Long description | ≤ 4,000 characters |
| Developer name | ≤ 80 characters |
| Starter prompts | Up to 3, each ≤ 128 characters, unique, no `@mentions` |
| Capabilities | Up to 20, each ≤ 120 characters |
| Icon | Square, ≥ 48×48 px; PNG, JPEG, WebP, or SVG; ≤ 5 MiB |
| URLs | HTTPS, ≤ 1,024 characters |

## Monetization rules

- **Physical goods only.** Selling digital products, subscriptions, credits, or tokens is banned, including indirect freemium upsells.
- Users may **sign in to an existing paid account**. You can say a feature needs another plan and link to an informational page, but you can't show plans or link to an upgrade or checkout page.
- **External checkout** on your own domain is generally available. In-widget checkout with saved payment methods is allowed. The **ChatGPT payment sheet ("Instant Checkout")** is a private beta for select marketplaces.
- Conversion specs for [product checkout](https://developers.openai.com/plugins/guides/product-checkout-conversion-spec), [restaurant reservations](https://developers.openai.com/plugins/guides/restaurant-reservation-conversion-spec), and [local-services quotes](https://developers.openai.com/plugins/guides/local-services-request-quote-conversion-spec) are in beta for approved partners. To apply, use the [merchants form](https://chatgpt.com/merchants/).

Source: [Checkout API reference](https://developers.openai.com/plugins/build/monetization) · [Plugin guidelines: Commerce](https://developers.openai.com/plugins/plugin-guidelines#commerce-and-monetization)

## After you publish

| Change | What happens |
| --- | --- |
| New or changed **MCP tools** | Continuous review: OpenAI scans daily or when you press *Rescan*. New tools go live after automated checks. Changed tools keep the old definition until the new one passes. |
| Server-only fixes and result data | Live as soon as you deploy |
| UI resource at the same URI | Live on deploy, but ChatGPT may cache it for up to 1 hour |
| Metadata, assets, or skills | Upload a new ZIP, which creates a new version that goes through review |
| MCP origin (scheme, host, or port) | Can't change. Contact support. |

Featured placement is chosen by OpenAI and **can't be requested**.

## Already have a Claude plugin?

OpenAI publishes a guide for exactly this: **[Submit your Claude Code plugin to OpenAI](https://developers.openai.com/plugins/guides/submit-claude-plugin)**. Skills-only Claude archives can be uploaded directly, and plugin formats are converging on [Agent Skills](https://agentskills.io) and [Agent Plugins](https://agent-plugins.org).
