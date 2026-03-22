---
title: Remote Claude Architecture — Bots, ETL, Agent Teams
created: 2026-03-22
updated: 2026-03-22
tags:
  - type/decision
  - ops/architecture
  - ops/tooling
status: active
---

# Remote Claude Architecture — Bots, ETL, Agent Teams

## 1. Overview

Admiral Systems runs a persistent WSL2 instance with Claude Code available 24/7, serving as the central AI layer for vault management, ETL processing, and team automation. Three interfaces connect to this single Claude installation: a Telegram bot for personal mobile access, a Slack bot for team-facing queries and commands, and a direct SSH terminal for interactive sessions and Agent Teams. All three interfaces share the same vault repositories, MCP server stack, and skill definitions, ensuring consistent behavior regardless of how Claude is invoked.

## 2. System Architecture

```
INTERFACES                       PROCESSING                 OUTPUTS
─────────                        ──────────                 ───────
Telegram Bot ─────┐
(mobile, /commands)│              ┌────────────────────┐
                   ├────────────→ │  WSL2 Claude Code  │ ──→ GitHub Vault
Slack Bot ─────────┤              │                    │     (admiral-systems)
(team, @mentions)  │              │  MCP Stack:        │
                   ├────────────→ │   ✅ Slack          │ ──→ Linear
Direct Terminal ───┘              │   ✅ Linear         │     (issues + tasks)
(SSH, interactive,                │   🔲 Gmail          │
 Agent Teams)                     │   🔲 Google Drive   │ ──→ Slack
                                  │   🔲 Granola        │     (notifications)
                                  └────────────────────┘
```

All three interfaces invoke the same Claude Code binary on the WSL2 instance. The bots use `claude -p` (non-interactive, single prompt), while the direct terminal supports full interactive sessions including Agent Teams. The MCP stack provides Claude with read/write access to external services — Slack and Linear are configured today, with Gmail, Google Drive, and Granola planned for Phase 2.

## 3. Interfaces

| Aspect | Telegram Bot | Slack Bot | Direct Terminal |
|---|---|---|---|
| **Audience** | Personal / single user | Team-facing / multiple users | Operator (SSH access required) |
| **Access** | Mobile app, any network | Slack workspace channels | SSH into WSL2 instance |
| **Invocation** | `/commands` (e.g., `/skill vault-status`) | `@claude` mentions in channels/DMs | `claude` interactive or `claude -p` |
| **Conversation scope** | Global conversation history per user | Thread-based history per channel | Session-based (lost on exit) |
| **Write confirmation** | `/confirm` to approve writes | `@claude confirm` in thread | Interactive Y/N prompts |
| **Agent Teams** | Not supported (non-interactive) | Not supported (non-interactive) | Fully supported (interactive mode) |
| **Best for** | Quick queries on the go, mobile ETL triggers | Team queries, shared ETL triggers, notifications | Complex synthesis, vault maintenance, Agent Teams |

See [[wsl-claude-telegram-setup]] for the Telegram bot setup guide and [[wsl-claude-slack-setup]] for the Slack bot setup guide.

## 4. Processing Modes

| Mode | Trigger | Method | Best For |
|---|---|---|---|
| Bot Query | Slack/Telegram message | `claude -p` read-only + skills | Quick queries, status checks, confirmed write ops |
| ETL Sync (manual) | Telegram `/skill etl-sync` or Slack `@claude etl-sync` | `claude -p` with ETL prompt + subagents | Processing finalized documents on demand |
| ETL Notification Cron | Cron on WSL (daily, morning) | `claude -p` scan + Slack digest | Surfaces new files for team confirmation before processing |
| Interactive Session | SSH to WSL terminal | `claude` interactive, Agent Teams capable | Complex synthesis, vault maintenance, devil's advocate |

Both Telegram and Slack trigger the same underlying Claude processing pipeline. Telegram uses `/commands` (e.g., `/skill etl-sync`, `/skill vault-status`) while Slack uses `@claude` mentions (e.g., `@claude etl-sync`, `@claude vault-status`). The bot wrapper script translates these into the appropriate `claude -p` invocation with the correct prompt, working directory, and skill context.

## 5. ETL Trigger Strategy

### 5.1 Manual Trigger (Primary)

Manual triggers are the primary ETL mechanism because they carry the highest confidence — a human has explicitly confirmed that the source documents are finalized and ready for processing.

- **Telegram**: `/skill etl-sync` followed by `/confirm` to approve
- **Slack**: `@claude etl-sync` or `@claude etl-sync [client-code]` (e.g., `@claude etl-sync rcg`)
- Human confirms docs are finalized before processing begins
- Result: vault entries created with `confidence: high` and `review_required: false`
- All vault writes are committed to GitHub, making diffs visible for post-hoc review

### 5.2 Notification Cron (Safety Net)

The notification cron acts as a safety net to catch documents that were finalized but never manually triggered for ETL processing. It does not auto-process anything — it only notifies the team and waits for explicit confirmation.

- Cron runs daily at start of working hours (e.g., 9 AM) on the WSL2 instance
- Claude scans Google Drive for new or modified files since the last check
- Posts a Slack digest to `#internal-vault-sync`:

```
Vault Sync Check — 2026-03-22

New or modified files found in Google Drive:
• RCG — Weekly Sync Notes (modified 14h ago)
• 4Walls — Client Feedback Round 3 (new, added 20h ago)
• Jireh Law — Sitemap Draft (modified 2h ago) ⚠️ recently modified

Reply in this thread:
• @claude sync all — process everything
• @claude sync "filename" — process specific file
• ignore — don't process any
```

- Files modified recently (< 4h) get a warning flag to indicate they may still be in progress
- Nothing is processed until a team member replies in the thread to confirm
- This eliminates the risk of syncing incomplete or in-progress documents into the vault

### 5.3 Why Notification Cron Instead of Auto-Processing

Auto-processing on a timer is unreliable for document-based ETL because there is no way to programmatically distinguish a "finished" document from one that is merely paused:

- A team member may stop editing a Google Doc and go to sleep — the document is incomplete, just paused until morning
- No cool-down window (2 hours, 6 hours, overnight) can reliably distinguish "done" from "paused for the night"
- Auto-processing risks creating vault entries and Linear issues from half-written notes, incomplete meeting summaries, or draft client feedback
- The notification cron catches everything that manual triggers might miss, while keeping a human in the loop for the final decision
- The result is zero risk of bad syncs — every ETL run is human-authorized

### 5.4 ETL Processing Flow

Once a trigger is confirmed (whether manual or via cron notification reply), Claude executes the following pipeline:

```
Trigger (manual via Telegram /command or Slack @mention)
  → Claude reads sources via MCP (Drive, Gmail, Slack, Granola)
  → Extracts: decisions, commitments, action items, context
  → Writes to vault: structured markdown with frontmatter + [[wikilinks]]
  → Creates Linear issues: action items with source attribution + claude-generated label
  → Notifies via Slack: posts summary to relevant -feed channel
  → Commits to GitHub: diff visible for human review
```

Each vault entry created by ETL includes source attribution (which document, which meeting, which email thread) so the team can trace any extracted item back to its origin. Linear issues include the same attribution in their description.

See [[admiral-systems-knowledge-vault-brief]] for the original ETL vision and detailed transform rules.

## 6. Agent Teams

Claude Code Agent Teams (experimental, enabled via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) allow multiple Claude instances to coordinate on complex tasks. A lead agent creates teammate agents, assigns them subtasks, and synthesizes their outputs. Teammates can work in parallel, share findings via inter-agent messaging, and collaborate through a shared task list.

Agent Teams require an interactive terminal session — they cannot be invoked through the bot interfaces (Telegram or Slack) because those use non-interactive `claude -p` mode.

### 6.1 Where Agent Teams Add Value

Agent Teams are best suited for interactive sessions via SSH/terminal where complex, multi-faceted work benefits from parallelism and cross-referencing:

1. **Weekly vault maintenance sprint** — A lead agent creates a team to audit vault health:
   - Teammate 1: Scan client folders for stale notes, missing briefs, and outdated status fields
   - Teammate 2: Cross-reference Linear issues with vault content to find orphaned tasks or undocumented decisions
   - Teammate 3: Validate frontmatter fields, [[wikilinks]] integrity, and kebab-case naming conventions across all files
   - Lead synthesizes findings into a vault health report with prioritized action items

2. **Complex multi-source ETL synthesis** — Processing a full week of meetings, Slack threads, and email chains:
   - One teammate per data source (Drive docs, Slack threads, email, Granola transcripts)
   - Teammates cross-reference findings across sources to deduplicate decisions and reconcile conflicting information
   - Lead synthesizes everything into structured vault entries and Linear issues with full source attribution

3. **Devil's Advocate reviews (Beta Workflow Step 2b)** — Structured adversarial review as described in [[project-brief]]:
   - Teammate 1: Presents audit findings, proposed changes, or draft deliverables
   - Teammate 2: Challenges assumptions, identifies gaps, stress-tests conclusions
   - Lead arbitrates disagreements and writes the final output incorporating both perspectives

4. **New client onboarding** — Parallel setup of all client infrastructure:
   - Teammate 1: Create vault folder structure from [[_template-client]] with initial frontmatter and placeholder files
   - Teammate 2: Set up Linear project following the [[create-linear-project]] playbook
   - Teammate 3: Draft initial client brief from discovery notes, call transcripts, or proposal documents
   - Lead reviews all outputs for consistency and completeness

### 6.2 Where Agent Teams Are NOT Suitable

- **Bot-triggered operations** — Telegram and Slack bots use `claude -p` (non-interactive mode), which does not support Agent Teams
- **Scheduled cron ETL runs** — Cron jobs run non-interactively and cannot recover if a teammate fails or the session drops
- **Simple read-only queries** — Asking for a client summary or vault status does not benefit from multiple agents; a single `claude -p` call is faster and cheaper

### 6.3 Current Limitations

- **Experimental** — Agent Teams are behind a feature flag and disabled by default; behavior may change between Claude Code releases
- **No session resumption** — If the WSL2 instance restarts or the terminal session drops, all in-progress teammate work is lost with no way to resume
- **One team per session** — A single terminal session supports one active team at a time; nested teams (a teammate spawning its own sub-team) are not supported
- **Token costs scale linearly** — Each teammate consumes its own token budget; a 4-agent team uses roughly 4x the tokens of a single agent for the same wall-clock duration
- **Split panes require tmux** — To visually monitor multiple teammates, the operator needs tmux or a similar terminal multiplexer running in the SSH session

## 7. Skills Registry

Skills are shared command definitions available across both bot interfaces. Each skill maps to a specific operation that Claude executes against the vault, Git, or external services.

| Skill | Description | Write Operation |
|---|---|---|
| `sync` | Pull latest changes and update submodules | git pull |
| `git-pull` | Pull latest changes from a specific repo | git pull |
| `git-pull-sub` | Pull latest changes for a submodule | git pull |
| `vault-status` | Show vault health — last updated files, stale notes | Read-only |
| `client-brief` | Pull a client summary from the vault | Read-only |
| `etl-sync` | Trigger ETL processing for recent sources | Vault write + Linear |

Both bots enforce a confirmation step before executing any write skill. This prevents accidental vault modifications from a mistyped command or an ambiguous query:

- **Telegram**: Claude responds with a summary of what it intends to do, and the user must send `/confirm` to proceed
- **Slack**: Claude responds in-thread with the proposed action, and a team member must reply `@claude confirm` to approve

Read-only skills (`vault-status`, `client-brief`) execute immediately without confirmation since they do not modify any state.

## 8. MCP Stack

The MCP (Model Context Protocol) stack provides Claude with structured access to external services. Each MCP server exposes read and/or write operations that Claude can invoke during processing.

| MCP Server | Purpose | Status | Priority |
|---|---|---|---|
| Slack MCP | Read/write Slack messages, search channels, post notifications | ✅ Configured | — |
| Linear MCP | Create/update issues, manage projects, query task status | ✅ Configured | — |
| Gmail MCP | Read email threads, search messages, extract action items | 🔲 To configure | Phase 2 |
| Google Drive MCP | Read client files, meeting notes, Gemini AI-generated summaries | 🔲 To configure | Phase 2 |
| Granola MCP | Read meeting transcripts from local Granola cache | 🔲 To configure | Phase 2 |

The Phase 2 MCP servers (Gmail, Google Drive, Granola) are required for the full ETL pipeline. Until they are configured, ETL processing is limited to sources accessible through the already-configured Slack and Linear MCPs plus direct vault content.

## 9. Phased Roadmap

| Phase | Focus | Key Deliverables |
|---|---|---|
| Phase 1 (current) | Manual vault curation + bot interfaces | Telegram bot running on WSL2, Slack bot integrated with workspace, vault structure and [[CLAUDE]] conventions established, skills registry operational |
| Phase 2 | ETL pipeline + remaining MCPs | Gmail MCP configured for email thread extraction, Google Drive MCP configured for document access, Granola MCP configured for meeting transcripts, manual ETL trigger via both bots, notification cron posting daily digests to `#internal-vault-sync` |
| Phase 3 | Agent Teams + automation | Interactive Agent Teams for complex multi-source synthesis, automated Slack notifications to client `-feed` channels after ETL runs, vault health monitoring with weekly maintenance sprints, new client onboarding automation via Agent Teams |

## 10. Related Documents

- [[wsl-claude-telegram-setup]] — Telegram bot setup guide (installation, systemd service, command routing)
- [[wsl-claude-slack-setup]] — Slack bot setup guide (app manifest, event subscriptions, channel configuration)
- [[admiral-systems-knowledge-vault-brief]] — Original ETL vision document (transform rules, source-to-vault mapping, confidence model)
- [[roles-responsibilities-2026-q1]] — Team roles and governance (who can trigger ETL, who reviews outputs)
- [[create-linear-project]] — Linear project creation playbook (labels, workflows, automation rules)
- [[linear-quality-checker]] — Linear quality validation playbook (issue completeness, label hygiene, stale task detection)
