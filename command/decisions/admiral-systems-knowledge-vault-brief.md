---
title: "Project Brief: Admiral Systems — Company Knowledge Vault (ETL System)"
created: 2026-03-22
updated: 2026-03-22
tags:
  - type/decision
  - ops/architecture
status: reference
---

# Project Brief: Admiral Systems — Company Knowledge Vault (ETL System)
**Version:** 1.2
**Date:** 2026-03-22
**Status:** Reference — original vision document

> This is the original ETL vision for the vault. The current vault structure has evolved differently — see [[CLAUDE]] for the live conventions. For the implementation architecture (bots, Agent Teams, ETL triggers), see [[remote-claude-architecture]]. For team roles and governance, see [[roles-responsibilities-2026-q1]].

---

## 1. Problem Statement

Admiral Systems operates in a high-context, client-facing environment where critical decisions, commitments, and deliverables are discussed across multiple tools — meetings, Slack threads, emails, and shared files. Currently, each team member maintains their own knowledge silo, leading to situations where:

- A team member who leaves a meeting early misses decisions made after their departure
- Client commitments (e.g. a deliverable timeline change) are communicated verbally but never land in a shared record
- New team members or returning colleagues have no reliable way to catch up on project context
- There is no single source of truth Claude or anyone else can consult before taking action

**The goal** is to build a shared Company Knowledge Vault where structured, Claude-curated context lives — always up to date, always traceable to source, and always queryable to drive downstream actions like task creation in Linear.

---

## 2. Proposed Architecture

The system is structured as a three-layer ETL pipeline.

```
┌─────────────────────────────────────────────────────────────┐
│                        EXTRACT                               │
│  (Read-only messy human data sources)                        │
│                                                              │
│  Google Drive  ·  Granola  ·  Gmail  ·  Slack               │
│  (incl. Google Meet + Gemini AI notes as Drive docs)         │
└─────────────────────────┬───────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                       TRANSFORM                              │
│  Claude digests, structures, and writes to the vault         │
│                                                              │
│  · Summarise decisions and commitments                       │
│  · Extract action items with owners                          │
│  · Add last_edited timestamp + source references             │
│  · Link related notes via [[wikilinks]]                      │
│  · Commit to GitHub with diff for human review               │
└─────────────────────────┬───────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                         LOAD                                 │
│  (Structured vault + downstream actions)                     │
│                                                              │
│  GitHub Repo (vault)  →  Linear (tasks)                      │
│  Obsidian (team reads vault via linked notes)                │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Data Sources (Extract Layer)

| Source | Access Method | Status | Notes |
|--------|--------------|--------|-------|
| Google Drive | Google Drive MCP (read-only) | 🔲 To configure | Shared Drive for all client + internal files, client dropoff folders, and Google Meet/Gemini AI notes. |
| Google Meet + Gemini AI Notes | Google Drive MCP (read-only) | 🔲 To configure | After each Meet call, Gemini automatically creates a Google Doc in Drive containing the AI summary, action items, and full transcript in separate sections. No additional integration required — covered by Google Drive MCP once configured. |
| Granola | Granola MCP (local cache) | 🔲 To configure | Reads `cache-v3.json` locally. Accesses transcripts, AI summaries, and human notes with speaker attribution. |
| Gmail | Gmail MCP | 🔲 To configure | MCP server available for connecting to Claude. |
| Slack | Slack MCP | ✅ Configured | Reads channel messages and threads. |

All sources are **read-only** at the Extract layer. Claude never writes back to any source system.

> **Note on Google Meet + Gemini AI Notes:** To ensure these documents land in a predictable, shared location rather than each meeting organiser's personal My Drive, the team should configure Google Meet to save notes to a specific folder in the Shared Drive. This can be set per-user in Google Meet settings.

---

## 4. The Knowledge Vault (Load Layer)

### Storage
The vault is a **private GitHub repository** containing markdown files. GitHub is chosen because:
- Files are plain `.md`, so wikilinks (`[[RCG]]`) are preserved and rendered correctly by Obsidian
- Every Claude commit creates a native audit trail (diff + commit message)
- The PR/review workflow gives humans an approval step before changes go live
- Free at this team's scale
- Cloudflare R2 is an optional sync backend if the team wants Obsidian to work offline without Git knowledge

### Team Access
Each team member clones the vault repo and opens it as their Obsidian vault. The **Obsidian Git plugin** handles auto-pull/push on a timer so it stays invisible to non-technical members.

### Vault Folder Structure

> **Note:** The original proposed structure below differs from the current live vault. See [[CLAUDE]] for the actual vault structure in use.

```
/vault
  /clients
    /RCG
      context.md              ← Master reference: who they are, key contacts, commitments
      decisions-log.md        ← Running log of decisions made, with source links
      deliverables.md         ← What was promised, when, and current status
    /[CLIENT-CODE]/
  /projects
    /RCG-001-webflow-build
      brief.md
      status.md
  /meetings
    /client
      2026-03-17--RCG--weekly-sync.md
    /internal
      2026-03-17--internal--team-standup.md
  /people
    daz.md
    val.md
    haykal.md
    tiara.md
    shafiq.md
  /inbox                      ← Claude's staging area before human review
    2026-03-19--granola--RCG-weekly-sync--draft.md
```

### Note Frontmatter Standard

Every Claude-written or Claude-updated note must include a YAML frontmatter block:

```yaml
---
last_edited: 2026-03-19T14:30:00+08:00
edited_by: claude
sources:
  - type: google_meet
    title: "RCG Weekly Sync — 2026-03-17"
    url: https://docs.google.com/document/d/[ID]
  - type: granola
    title: "RCG Weekly — March 17"
    url: null
  - type: google_drive
    title: "RCG Brand Feedback March 2026"
    url: https://docs.google.com/document/d/[ID]
  - type: gmail
    title: "Re: Design deliverable timeline"
    url: https://mail.google.com/mail/u/0/#inbox/[thread_id]
  - type: slack
    title: "#rcg-project thread, 2026-03-17"
    url: https://admiralsystems.slack.com/archives/[channel]/p[timestamp]
confidence: high  # high | medium | low — Claude's self-assessment of the synthesis
review_required: false
---
```

This directly solves the requirement for `last_edited` timestamps and source references on every vault note.

---

## 5. Naming Conventions

Consistent naming across the vault, Google Drive, Linear, and Slack is critical for an agency. When client volume grows, ambiguous names like "Meeting Notes" or "Brief v2" become impossible to navigate. The following conventions apply across all systems.

### 5.1 General Principles

- **Always include the client code** — every file, folder, and task that touches a client must include their code so it is immediately identifiable out of context (e.g. in search results, Slack previews, Linear).
- **Dates are ISO 8601** — always `YYYY-MM-DD`. This ensures chronological sort order works correctly in every tool.
- **Lowercase with hyphens for vault files** — matches how Obsidian and GitHub handle filenames cleanly.
- **Title Case for Google Drive** — more readable for non-technical team members browsing Drive.
- **No spaces in vault filenames** — spaces cause issues in some Git and CLI workflows.
- **Double hyphens as field separators** — single hyphens are used within fields (e.g. `webflow-build`), so double hyphens (`--`) separate the distinct parts of a filename.

---

### 5.2 Client Codes

Each client gets a short, memorable uppercase code assigned at onboarding. This code appears in every file, folder, task, and note related to that client.

| Client | Code |
|---|---|
| Red Centre Global | `RCG` |
| [Next client] | `[3-letter code]` |

**Rules for assigning codes:**
- 3 letters preferred, 4 maximum
- Based on client name initials or a recognisable abbreviation
- Must not conflict with existing codes
- Assigned in the client's `context.md` on day one and never changed

---

### 5.3 Project Codes

Projects get a sequential code combining the client code and a number:

```
[CLIENT-CODE]-[NNN]
```

Examples:
- `RCG-001` — first project for Red Centre Global
- `RCG-002` — second project for Red Centre Global

The full project name follows the code in folder names and Linear:

```
RCG-001-webflow-build
RCG-002-brand-refresh
```

---

### 5.4 Vault File Naming

```
YYYY-MM-DD--[client-or-scope]--[description].md
```

The `[client-or-scope]` field is either a client code or an internal scope keyword:

| Scope | Keyword |
|---|---|
| Client-specific | `RCG`, `[CLIENT-CODE]` |
| Internal team | `internal` |
| Studio-wide | `studio` |
| New business | `bizdev` |

Examples:

```
2026-03-17--RCG--weekly-sync.md
2026-03-17--internal--team-standup.md
2026-03-10--RCG--scope-change-design-deliverable.md
2026-03-01--bizdev--new-client-intro-acme.md
```

Inbox drafts (Claude-generated, pending review):

```
2026-03-19--granola--RCG-weekly-sync--draft.md
2026-03-19--gmail--RCG-design-timeline--draft.md
```

---

### 5.5 Google Drive Naming

Google Drive uses Title Case and spaces for readability by non-technical team members browsing the Shared Drive.

**Folders:**

```
[CLIENT CODE] — [Full Client Name]           ← client root folder
[CLIENT CODE] — Meetings                     ← meeting notes subfolder
[CLIENT CODE] — Deliverables                 ← work product subfolder
[CLIENT CODE] — Client Dropoff               ← client-accessible folder
[CLIENT CODE] — [PROJECT-CODE] [Name]        ← project subfolder
```

Examples:

```
RCG — Red Centre Global
RCG — Meetings
RCG — Client Dropoff
RCG — RCG-001 Webflow Build
```

**Files:**

```
YYYY-MM-DD [CLIENT CODE] [Description]
```

Examples:

```
2026-03-17 RCG Weekly Sync (Gemini Notes)
2026-03-10 RCG Brand Feedback Round 2
2026-02-28 RCG-001 Webflow Brief
```

> **Google Meet + Gemini AI notes** are auto-named by Google (e.g. "Notes for RCG Weekly Sync"). The team should rename these immediately after the meeting to match the convention above, before they get picked up by the ETL pipeline.

---

### 5.6 Linear Task Naming

Linear tasks follow a verb-first convention so every task reads as an actionable instruction:

```
[ACTION VERB] [deliverable] — [CLIENT CODE]
```

Examples:

```
Design homepage hero section — RCG
Review copy feedback from client — RCG
Fix mobile nav overflow — RCG-001
Deliver brand book PDF — RCG
```

Claude-generated tasks automatically get the `claude-generated` label and include a source link in the description.

---

### 5.7 Slack Channel Naming

Slack channels follow a predictable structure so any team member can find a channel without asking:

```
client-[client-code-lowercase]          ← main client channel
client-[client-code-lowercase]-feed     ← automated updates (Claude, Linear, Drive)
internal-[topic]                        ← internal team topics
bizdev-[topic]                          ← new business
```

Examples:

```
#client-rcg
#client-rcg-feed
#internal-ops
#internal-hiring
#bizdev-pipeline
```

---

## 6. Transform Rules (Claude's Processing Logic)

When Claude processes raw data from any source, it follows these rules:

**What Claude synthesises:**
- Decisions made (with who made them and when)
- Commitments to clients (deliverables, timelines, scope changes)
- Action items (owner, due date if mentioned)
- Context that would prevent a future team member from being blindsided

**What Claude does not do:**
- Invent or infer facts not present in the source
- Overwrite existing vault entries without preserving prior content
- Mark `confidence: high` if the source is ambiguous or incomplete

**Write behaviour:**
- New context → creates a new file in `/inbox/` with `review_required: true`
- Update to existing context → opens a PR against the existing vault file; human reviews the diff before merge
- Action items → pushed directly to Linear via Linear MCP (no human review required for task creation, only for vault writes)

---

## 7. Downstream Actions (Load Layer — Linear)

Once context is in the vault, the second output of the pipeline is task creation in Linear. The flow:

```
Meeting note / email / Slack thread
  → Claude extracts action items
  → Claude creates Linear issues with:
      - Title (verb-first, client code suffix)
      - Assignee (mapped from people/ vault notes)
      - Project (mapped from projects/ vault notes)
      - Source link in description
      - Label: "claude-generated" (for traceability)
```

The `claude-generated` label in Linear allows the team to audit and clean up AI-created tasks separately from human-created ones.

---

## 8. Open Flags / Decisions Required

**Flag 1 — Human review workflow to define.**
The team needs to decide the minimum review requirement before Claude-written content moves from `/inbox/` to live vault folders. Options:
- Any one team member can approve (fast)
- Shafiq approves all vault writes (controlled, creates a bottleneck)
- Auto-approve after 24 hours if no objection (async-friendly)

**Flag 2 — Granola is machine-local.**
GranolaMCP reads meeting data directly from Granola's local cache file without making any API calls to Granola's servers. This means the ETL pipeline can only extract Granola data from the machine where Granola is installed. If multiple team members use Granola, each person's meetings need to be extracted from their own machine, or a shared Granola workspace needs to be set up. Granola's Enterprise API provides programmatic access to workspace-wide notes for Enterprise customers — this may be worth evaluating as the team scales.

**Flag 3 — Write-capable Google Drive MCP needed (Phase 2 only).**
The current Google Drive MCP connected to this Claude environment is read-only. A write-capable MCP server will need to be configured if Claude is ever required to update Google Drive directly (e.g. to post a summary back into a client folder). For Phase 1, this is not required — Claude writes only to GitHub.

---

## 9. MCP Stack Required

| MCP Server | Purpose | Status |
|---|---|---|
| Google Drive MCP | Read client files, meeting notes, dropoffs, and Google Meet/Gemini AI notes | 🔲 To configure |
| Gmail MCP | Read relevant email threads | 🔲 To configure |
| Granola MCP | Read meeting transcripts and summaries | 🔲 To configure |
| Slack MCP | Read channel messages and threads | ✅ Configured |
| Linear MCP | Create and update tasks | ✅ Configured |
| Google Drive MCP (write) | Optional: post summaries back to Drive | 🔲 Phase 2 |

---

## 10. Phased Delivery

### Current State (Before Phase 1)

The GitHub vault repository has been created and populated with a custom structure. **This structure differs from the folder layout and naming conventions described in this brief.** See [[CLAUDE]] for the live vault structure and [[remote-claude-architecture]] for the implementation plan.

---

### Phase 1 — Foundation
- ⬜ Vault reassessment: compare brief to actual vault structure and reconcile
- ⬜ Agree final folder structure and naming conventions
- ⬜ Define and apply note templates and frontmatter standard across vault
- ⬜ Configure Obsidian Git plugin for all team members
- ⬜ Configure Google Meet to save Gemini AI notes to the Shared Drive
- ⬜ Connect Google Drive MCP (read-only)
- ⬜ Connect Gmail MCP
- ⬜ Connect Granola MCP on Shafiq's machine
- ⬜ Run first manual ETL cycle: Google Meet notes + Gmail → vault

### Phase 2 — Full Pipeline
- ⬜ Connect GitHub MCP for Claude commits
- ⬜ Build the Linear task creation flow from vault action items
- ⬜ Establish human review workflow for inbox notes
- ⬜ Add Granola to the pipeline

### Phase 3 — Automation
- ⬜ Schedule notification cron (see [[remote-claude-architecture]])
- ⬜ Refine confidence scoring and source linking
- ⬜ Evaluate Granola Enterprise for team-wide transcript access
- ⬜ Evaluate write-capable Google Drive MCP for Phase 2 feedback loop

---

## 11. Success Criteria

The system is working when:

1. A team member who missed part of a meeting can query the vault and find an accurate summary with the source transcript linked
2. No client commitment goes unrecorded in the vault for more than 24 hours after a meeting
3. Action items from meetings appear in Linear automatically, with source attribution
4. New team members can onboard to a client project by reading the vault without asking anyone
5. Every vault entry has a `last_edited` timestamp and at least one `sources` reference
6. Any team member can find any file in Google Drive, any task in Linear, or any vault note within 30 seconds using the naming convention alone

---

*Brief prepared by Claude for review by Shafiq / Admiral Systems.*
*Open flags in Section 8 are pending team confirmation. Phase 1 is blocked on vault reassessment — see Section 10.*
