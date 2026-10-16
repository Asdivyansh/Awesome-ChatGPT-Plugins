# 🚀 Using ChatGPT Plugins

A practical guide to finding, installing, and using plugins in ChatGPT and Codex (as of October 2026).

[← Back to the list](../README.md)

## Contents

- [What a plugin is](#what-a-plugin-is)
- [Where plugins run](#where-plugins-run)
- [Install a plugin](#install-a-plugin)
- [Use a plugin in a chat](#use-a-plugin-in-a-chat)
- [Permissions and safety](#permissions-and-safety)
- [Connect your own MCP server](#connect-your-own-mcp-server)
- [For workspace admins](#for-workspace-admins)
- [Troubleshooting](#troubleshooting)

## What a plugin is

A **plugin** is an installable bundle that teaches ChatGPT and Codex how to work with a product or workflow. It can contain:

| Part | What it does |
| --- | --- |
| 🧩 **Skills** | Folders with a `SKILL.md` file (plus optional scripts and references) that describe a repeatable workflow, such as "triage a Sentry issue" or "draft a PRD". |
| 🔌 **App (MCP server)** | Tools that connect to an outside system: read your Notion pages, search flights, create a Stripe payment link. Apps were called "connectors" until December 2025. |
| 🖼️ **UI (optional)** | Interactive widgets that render inside the chat (maps, carousels, editors, games), built on the open [MCP Apps](https://modelcontextprotocol.io/docs/extensions/apps) standard. |
| 🧱 **Extensions (optional)** | Sidebar apps, side panels, file viewers, rich forms, and composer mentions ([Plugin Extensions](https://developers.openai.com/plugins/build/extensions), announced at DevDay 2026). |

Source: [Plugin architecture](https://developers.openai.com/plugins/concepts/plugins) · [Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins)

## Where plugins run

- **ChatGPT Chat and Work** on web, desktop, and mobile.
- **Codex** inside the ChatGPT desktop app, which absorbed the standalone Codex app on July 9, 2026, and the **Codex CLI** (`/plugins`).
- **Not** the Codex IDE extension.
- Listings marked **Desktop only** need the ChatGPT desktop app. In this repo they're tagged 🖥️.

ChatGPT and Codex share one **[Plugin Directory](https://chatgpt.com/plugins)**. Directory tabs separate OpenAI, workspace, and personal plugins.

## Install a plugin

1. Open the **[Plugin Directory](https://chatgpt.com/plugins)** (or **Plugins** in the ChatGPT sidebar).
2. Pick a plugin and press **+** (Install).
3. If prompted, **connect** the underlying account. OAuth runs either at install or the first time you use it. Some partners support **Sign in with ChatGPT** (beta).

> [!TIP]
> Uninstalling a plugin doesn't disconnect apps you connected separately. Manage connected apps from your ChatGPT settings.

## Use a plugin in a chat

- **Just ask.** ChatGPT can pick an installed plugin when it's relevant ("find me a hotel in Lisbon under €150").
- **Mention it.** Type **`@`** and choose the plugin or one of its skills (`@Figma turn this into a wireframe`).
- **In Codex,** skills are invoked with **`$`** (`$skill-name`).
- **Use the starter prompts** on each plugin's directory page. They show what the plugin is good at.

## Permissions and safety

- **Approval levels.** For each app you choose whether ChatGPT asks *always*, *before changes*, or *only before important changes* (since June 2026). Admins can set workspace defaults.
- **Read vs. write.** Check the plugin page's **Capabilities** (for example `Read`, `Write`, `Interactive`) before connecting accounts that can move money or send messages.
- **Elevated risk labels.** Custom MCP servers and some listings carry an [elevated risk](https://help.openai.com/en/articles/20001062) label.
- **Data sharing.** When connected, ChatGPT may share relevant chat context and memories with the plugin. The developer's privacy policy, linked on every directory page, applies.
- **Prompt injection.** Plugins that read the open web or your inbox can encounter malicious instructions. Keep confirmations on for actions that matter.

## Connect your own MCP server

The 2025 "developer mode" became **Add custom MCP server**:

1. Go to [chatgpt.com/plugins](https://chatgpt.com/plugins), press **+**, and choose **Add custom MCP server**.
2. Enter the server URL. SSE and streamable HTTP are supported, with OAuth, no auth, or mixed auth.
3. Choose **Create as a plugin**. It appears under **Personal** and you invoke it with `@` in a Work chat.

This flow is web-only, labeled *elevated risk*, and subject to workspace permissions. For private servers, see [Secure MCP Tunnel](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels). The full guide is [Add custom MCP server](https://developers.openai.com/api/docs/guides/custom-mcp-server).

You can also build a plugin **without code** using the [Plugin Creator](https://learn.chatgpt.com/docs/build-plugins) (`@plugin-creator`).

## For workspace admins

Business, Enterprise, and Edu admins control plugins in two places:

- **Admin → Plugins** (`chatgpt.com/admin/plugins`): set each plugin to *Available* or *Installed* per role, publish workspace plugins, and import or daily-sync plugin marketplaces from GitHub (Codex, Claude-compatible, and Agent Plugins 1.0 formats).
- **Workspace apps** (`chatgpt.com/admin/ca`): MCP server access, action controls, and app permissions.

Enterprise admins can also export the public catalog as CSV. See [Plugin controls](https://learn.chatgpt.com/docs/enterprise/apps-and-connectors), [Plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management), and [Admin controls, security, and compliance](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-for-plugins-and-apps).

> [!NOTE]
> **Custom GPTs are being retired.** OpenAI announced in September 2026 that custom GPTs will migrate to plugins, with retirement scheduled for **December 11, 2026** (subject to change). See [Moving custom GPT workflows to plugins](https://learn.chatgpt.com/docs/migrate-custom-gpts).

## Troubleshooting

| Problem | Try this |
| --- | --- |
| A plugin from this list doesn't appear for you | Some listings depend on your region, plan, or workspace settings. Plugins and apps are off by default in some Enterprise and Edu workspaces. |
| "Desktop only" | Install the ChatGPT desktop app. These plugins need local access, such as a browser or local files. |
| ChatGPT isn't using the plugin | Mention it explicitly with `@`, or start a new chat after installing. |
| Auth keeps failing | Disconnect and reconnect the app from your ChatGPT settings, and check that your account has the required permissions in the third-party product. |

---

Sources: [Plugins (learn.chatgpt.com)](https://learn.chatgpt.com/docs/plugins) · [Plugins in ChatGPT and Codex (Help Center)](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex) · [What's new](https://learn.chatgpt.com/docs/whats-new)
