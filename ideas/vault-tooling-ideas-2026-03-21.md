---
title: Vault Tooling Ideas — Tools, Agents & Commands
created: 2026-03-21
updated: 2026-03-21
author: Claude
tags:
  - type/idea
  - admiral/operations
  - admiral/delivery
  - admiral/tooling
status: draft
---

# Vault Tooling Ideas

Generated from a full scan of the Admiral Systems vault on 2026-03-21. Each idea references actual vault signals — files, gaps, and patterns found during the audit.

---

## Tools to Build

### Client Index Auto-Populator

_Script that scans `clients/` folders and populates [[_client-index]] automatically._

- **Rationale:** [[_client-index]] has an empty table despite 4 active clients with rich briefs. Each client folder has a consistent structure (brief, meetings, deliverables) that can be parsed.
- **Effort:** quick

### Linear CSV Analyzer

_Tool that ingests Linear CSV exports and generates delivery health summaries._

- **Rationale:** `delivery/linear/` has ~5MB of CSV exports (`all-issues-export.csv`, `overdue-issues-triage.csv`, `daz-active-issues-triage.csv`). Currently these are raw dumps — no automated analysis exists despite the vault having detailed reports in `delivery/reports/` that were clearly written manually from this data.
- **Effort:** medium

### Sprint Sync Bridge

_Pull current sprint data from Linear exports into [[sprint-current]]._

- **Rationale:** [[sprint-current]] is an empty template with placeholder dates. Real sprint work happens in Linear, but the vault has no bridge to keep the two in sync. The [[linear-restructuring-plan-2026-03-10|Linear restructuring plan]] consolidated teams from 14→6, meaning sprint data is now more manageable to surface.
- **Effort:** medium

### Meeting Notes Normalizer

_Standardize meeting note formats across clients._

- **Rationale:** Meeting formats vary wildly — Jireh Law's intro meeting is a ~43K token raw transcript dump, 4Walls meetings have structured "AI summary + account manager notes," and RCG's meetings are minimal. [[tpl-meeting-notes]] exists but isn't consistently applied.
- **Effort:** quick

---

## Agents to Create or Improve

### Client Health Check Agent

_Agent that audits a client folder against the template and flags gaps._

- **Rationale:** [[_template-client]] defines the expected structure (brief, deliverables/, meetings/) but actual clients diverge. RCG has minimal docs (`project-info.md` is just slug + dates), while 4Walls has a comprehensive 13.7KB SOW-style brief with KPI tiers. No agent exists to flag which clients need attention.
- **Effort:** quick
- **Location:** [[agent-playbooks]] directory

### SOP Generator Agent

_Agent that generates draft SOPs from existing playbooks and team docs._

- **Rationale:** `operations/sops/` is completely empty, yet [[agent-playbooks]] has 8 detailed playbooks and [[roles-responsibilities-2026-q1]] documents operational rules (e.g., "issue creation → seniors only," "Linear updates by 10AM daily"). The raw material exists to draft SOPs — it just hasn't been formalized.
- **Effort:** medium
- **Location:** [[agent-playbooks]] directory

### Beta Workflow Orchestrator Agent

_End-to-end agent that runs the beta engagement workflow steps in sequence._

- **Rationale:** The [[project-brief|beta workflow project brief]] documents a 7-step workflow (alignment → audit → devil's advocate → design → Google Sheet → Linear project) but each step is manually triggered. The individual playbooks exist ([[create-linear-project]], [[linear-quality-checker]], [[create-issue-step3b-google-sheet]]) but there's no orchestration agent chaining them. Jireh Law is flagged as the first live test case.
- **Effort:** large

### Risk Register Agent

_Agent that scans client milestones, overdue issues, and capacity to populate [[risks]]._

- **Rationale:** [[risks]] is an empty template. Meanwhile, `delivery/linear/overdue-issues-triage.csv` tracks overdue items, client milestone files have explicit dates and dependencies (e.g., 4Walls has 4 phased milestones with clear completion criteria), and [[capacity]] is also empty. The data to surface risks exists across multiple files — no agent connects them.
- **Effort:** medium

### Standup Prep Agent

_Agent that generates a standup summary from Linear data + recent meeting notes per client._

- **Rationale:** [[roles-responsibilities-2026-q1]] requires "Juniors update Linear by 10AM daily" and "Seniors before Monday standup." No agent exists to compile cross-client status. The restructuring plan shows 4 active project teams (Admiral-Beta, RMD-Beta, Sprklabs-Epsilon, Internal) — a standup agent could pull from each.
- **Effort:** medium

---

## Commands & Skills

### `/client-status`

_Generate a quick status snapshot for one or all clients._

- **Rationale:** No command exists for quick client health views. Currently requires manually reading each client's brief, latest meeting notes, and cross-referencing Linear exports. With 4 active clients across 3 entities (Admiral, RMD, Sprklabs), a single-command overview would save significant context-switching.
- **Effort:** quick

### `/new-client`

_Scaffold a new client folder from [[_template-client]] with prompted metadata._

- **Rationale:** [[_template-client]] exists with `brief.md`, `deliverables/`, and `meetings/` but requires manual copy and frontmatter population. All 4 existing clients follow the `{entity}-{phase}-{codename}` naming pattern — this command could enforce that convention automatically.
- **Effort:** quick

### `/new-sop`

_Create a new SOP from [[tpl-sop]] with guided prompts._

- **Rationale:** [[tpl-sop]] exists but `operations/sops/` is empty. Making SOP creation frictionless would help fill this critical gap.
- **Effort:** quick

### `/weekly-review`

_Generate a weekly delivery review across all clients and internal work._

- **Rationale:** `delivery/reports/` has 10 analytical documents assembled manually. No command automates the weekly review cycle. [[tpl-sprint-review]] exists as a template but isn't being used — a command could generate reviews from vault state + Linear data.
- **Effort:** medium

### `/strategy-check`

_Compare current delivery activity against strategy and OKRs._

- **Rationale:** [[strategy]] is a skeleton and `command/okrs/` is empty. Once populated, this command would help the leadership layer (Daz, Rohan, Valentin) verify that client work aligns with strategic pillars.
- **Effort:** medium (depends on strategy being populated first)

### `/onboard-team-member`

_Generate an onboarding checklist from team docs and SOPs._

- **Rationale:** The roster references onboarding but has no checklist. [[roles-responsibilities-2026-q1]] has 11 team members but the roster only lists 1. With 5 juniors needing clear guidance on Linear usage, update cadences, and approval flows, a structured onboarding command would reduce ramp-up friction.
- **Effort:** medium

---

## Top 3 Highest-Impact Ideas

1. **Client Health Check Agent** — The gap between well-documented clients (4Walls: detailed SOW with KPIs) and under-documented ones (RCG: minimal `project-info.md`) is a delivery risk. An agent that flags missing deliverables per client against the [[_template-client]] standard would immediately surface blind spots across the 4 active engagements.

2. **SOP Generator Agent** — The vault has 8 detailed agent playbooks and a comprehensive [[roles-responsibilities-2026-q1|roles & responsibilities doc]] with operational rules, but `operations/sops/` is completely empty. Converting existing operational knowledge into formal SOPs would bridge the gap between "what we know" and "what the team can reference" — critical with 5 junior team members.

3. **`/client-status` Command** — With 4 clients across 3 partner entities, each at different phases and with different documentation depths, a single-command status view would eliminate the most frequent context-switching cost. The data already exists in the vault — it just needs surfacing.
