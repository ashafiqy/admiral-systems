---
title: "Beta Workflow - Project Brief"
created: 2026-02-18
updated: 2026-03-21
tags:
  - operations/beta-workflow
  - type/project-brief
status: active
---

# Plan: Admiral Systems — Beta Engagement Workflow Improvement (Linear Project Brief & Issues)

## Context

On March 9, 2026, the Admiral Systems senior team (Daz, Shafiq/Davis, Sean, Val, Rohan) aligned on formalizing their client delivery operations. The key outcome: create a Linear project that serves as the **internal source of truth** for the senior team to track the work of improving and completing the Beta Engagement Workflow. Once the workflow is solid, it will be applied to client projects — with Joshua's Law Firm as the first live test case (in a **separate** Linear project).

The `beta-engagement-workflow-v1.png` defines the canonical flow being improved:
- **Step 1** – Project alignment, Discovery Questionnaire, SOW (seniors only), Lead Magnets → dump context into Claude
- **Step 2** – Audit (Screaming Frog, sitemap check, content plan)
- **Step 2b** – Claude plays Devil's Advocate on Step 2 outputs
- **Step 3** – Finalize sitemap, user flows, commercial sitemap approval
- **Step 3b** – Single Google Sheet output: page slugs, types, CMS fields, content/creative direction, meta, JSON schema, **plus a Claude prompt template** for generating Linear brief + issues
- **Step 3c** – Claude creates the Linear project + issues from the Google Sheet via MCP
- **Right rail** – Weavy (weavy.ai) → Creatives → Figma → Relume (base components) → Webflow

---

## RACI Key

| Letter | Meaning |
|---|---|
| **R** | Responsible — does the work |
| **A** | Accountable — owns the outcome, signs off |
| **C** | Consulted — input needed before/during |
| **I** | Informed — kept in the loop on completion |

**Team shorthand:** Daz · Shafiq · Davis · Sean · Val · Rohan

---

## Project Brief

**Linear Project Name:** Beta Engagement Workflow — Improvement
**Linear Project Slug:** `AST-Internal-BetaWorkflow`
**Description:** Internal senior team project to document, build, and refine the Admiral Systems end-to-end client engagement workflow. This is the source of truth for all tasks to get the workflow production-ready — covering documentation, Claude AI prompts/automations, tooling setup, and team alignment. Output: a proven, repeatable process ready to deploy on client engagements.
**Not in scope:** Delivery of any specific client project (Joshua's Law Firm is a separate Linear project)

**Timeline:** 4 weeks total (9 Mar – 6 Apr 2026)
- Weeks 1–2: Steps 1 & 2 documentation (Phase 2 priority)
- Weeks 3–4: Claude AI build, standards, validation

**Success Criteria:**
- All workflow steps (1 → 3c) documented with clear owners, inputs, and outputs
- Claude prompts for Steps 2b, 3b, 3c written, tested, and version-controlled
- Step 3b Google Sheet master template exists and is usable
- Linear project + issue creation via Claude (Step 3c) is functional via MCP
- Team tooling (Figma, Claude Pro, Granola, Weavy) set up for all seniors
- Updates cadence and template agreed upon and enforced
- Steps 2 onwards validated on Joshua's Law Firm once improved (tracked in Joshua's project, not here)

---

## Execution Standards (from `agent/` folder)

- **Project naming:** `{CLIENT}-{Phase}-{Type}` → `AST-Internal-BetaWorkflow`
- **Project description:** 3 blocks only — Header, Overview, Milestones table. No RACI, no SOW, no risk register in Linear.
- **Issue descriptions:** Follow `Task_Template.md` — Title (verb phrase), Task Overview (1 sentence), Additional Notes (task-specific links only), Acceptance Criteria (max 5 checkboxes), Task Blockers (leave empty), Task Dropoff (leave empty).
- **Milestones:** Create as Linear milestone objects via `save_milestone`, not just table rows.

**Execution sequence:**
1. Run `list_teams` + `list_users` to get correct IDs
2. Confirm Linear MCP is live (`list_projects`)
3. Pull reference projects for quality bar: `sb-ast-jirehlaw-142bad2832c5` (brevity) + `hpl-beta-rmd-2026-9be83c8cefeb` (milestone structure)
4. Create project via `save_project`
5. Create 4 milestone objects via `save_milestone`
6. Create issues per epic via `save_issue`
7. Create Team Operations & Policies as a Linear Document (Epic 4)

**Milestone structure for this project:**

| Phase | Focus | Target Date | Epics Covered |
|---|---|---|---|
| Phase 1 | Foundation & Team Setup | 16 Mar 2026 | Epic 3 (Urgent items) |
| Phase 2 | Workflow Documentation — Steps 1 & 2 first | 23 Mar 2026 | Epic 1 |
| Phase 3 | Claude AI Prompts & Automation | 30 Mar 2026 | Epic 2 |
| Phase 4 | Standards, Validation & Handoff | 6 Apr 2026 | Epic 5 |

---

## Linear Issue Backlog

### Epic 1: Workflow Documentation (Steps 1–3c)
> Phase 2 milestone · Steps 1 & 2 are priority in weeks 1–2

**Goal:** Written SOPs for each step of the workflow diagram.

| Issue | R | A | C | I | Priority |
|---|---|---|---|---|---|
| Document Step 1 — Discovery, SOW & Lead Magnets | Val, Rohan | Daz | Shafiq, Sean | Davis | High |
| Document Step 2 — Audit process (Screaming Frog, sitemap, content plan) | Davis, Shafiq | Daz | Val, Rohan | Sean | High |
| Document Step 2b — Claude as agent/sub-agent: checker (Devil's Advocate) on audit outputs; Shafiq + Davis define the agent spec together | Shafiq, Davis | Daz | Val | Rohan, Sean | High |
| Document Step 3 — Sitemap finalization & user flows | Davis | Daz | Shafiq, Val, Rohan | Sean | High |
| Document Step 3b — Davis + Shafiq decide CMS vs static vs folder structure per sitemap page (factoring in lead gen initiatives identified during Step 2 audit, which may require additional folders/pages); Claude as agent/sub-agent then populates the Google Sheet (artifact creator) and/or validates the output (checker) | Davis, Shafiq | Daz | Val, Sean, Rohan | — | High |
| Document Step 3c — Linear brief + issue generation via Claude | Shafiq | Daz | Davis, Rohan | Val, Sean | High |
| Document Weavy → Creatives → Figma → Relume → Webflow design pipeline | Sean | Daz | Davis, Shafiq, Val | Rohan | Medium |

---

### Epic 2: Claude AI Prompts & Automation
> Phase 3 milestone

**Goal:** Build the Claude-powered steps of the workflow.

| Issue | R | A | C | I | Priority |
|---|---|---|---|---|---|
| Build Step 2b Claude agent/sub-agent (checker role — Devil's Advocate on audit outputs) | Shafiq, Davis | Daz | Val | Sean, Rohan | High |
| Build Step 3b Claude agent/sub-agent (artifact creator — populates Google Sheet from sitemap incl. CMS/static/folder decisions and lead gen initiatives surfaced in Step 2 audit) + create master Sheet template | Davis, Shafiq | Daz | Val, Sean, Rohan | — | High |
| Build Step 3b → Linear project brief generation prompt | Shafiq | Daz | Rohan, Val | Davis, Sean | High |
| Build Step 3c Linear issue generation prompt (title, desc, AC, weight, due date, tags, assignee) | Shafiq | Daz | Davis, Rohan | Val, Sean | High |
| Integrate Step 3c with Linear via MCP | Shafiq | Daz | Davis | All | High |
| Test full Step 2b → 3b → 3c pipeline on a dry-run project | Shafiq | Daz | Davis, Val, Sean, Rohan | — | High |
| Build Claude prompt library with version control | Shafiq | Daz | Davis | All | Medium |

---

### Epic 3: Tool & Team Setup
> Phase 1 milestone · Urgent items first

**Goal:** Get all seniors properly equipped to run the workflow.

| Issue | R | A | C | I | Priority |
|---|---|---|---|---|---|
| Create Linear project: Beta Engagement Workflow — Improvement | Shafiq | Daz | — | All | Urgent |
| Purchase Claude Pro (Cloud team plan) for all seniors | Daz | Daz | Shafiq | All | Urgent |
| Resolve Rohan's Hong Kong VPN → GCP access issue | Rohan, Shafiq | Daz | — | All | Triage |
| Set up Linear workspace structure (teams, labels, templates) | Shafiq | Daz | Davis, Rohan | All | High |
| Configure Open Router API + cost tracking | Shafiq | Daz | Davis | All | Deprioritized |

---

### Epic 4: Team Alignment & Operations
> Linear Document — NOT issues

**Goal:** Align the senior team on working practices and enforce them.

> These are NOT Linear issues. They should be created as a **Linear Document** attached to the project — a living reference for all seniors.

**Linear Document title: "Admiral Systems — Team Operations & Policies"**

Sections to include:

| Section | R | A | C | I |
|---|---|---|---|---|
| Updates cadence decision (daily vs. sequential) + rationale | All seniors | Daz | — | Juniors |
| Linear update template (TLDR / did / doing / blockers) | Shafiq, Daz | Daz | All seniors | Juniors |
| Meeting SOP — Gemini transcript must be manually enabled each meeting | Shafiq | Daz | — | All |
| 60-day client response policy | Daz | Daz | Rohan, Val | All |
| 3-month project timeline + 4-week penalty policy | Daz, Rohan | Daz | Val, Davis, Shafiq | All |
| R&D note: Slack → Claude → Linear updates integration (est. 2–3 days when prioritised) | Shafiq | Daz | Davis | All |
| Junior office hours schedule (1 senior/week, rotating) | Rohan | Daz | All seniors | Juniors |
| Junior onboarding guide (workflow, tools, escalation path) | Davis, Shafiq | Daz | Val, Sean, Rohan | Juniors |

---

### Epic 5: Design & Webflow Standards
> Phase 4 milestone

**Goal:** Standardize technical delivery so juniors and seniors work consistently.

| Issue | R | A | C | I | Priority |
|---|---|---|---|---|---|
| Define Google Analytics + AEO standard setup for Webflow | Shafiq, Davis | Daz | Rohan | Sean, Val | Medium |
| Define Webflow page/component naming conventions | Davis | Daz | Shafiq, Sean | All, Juniors | Medium |
| Document Weavy (video content generation) workflow | Val, Sean | Daz | Rohan, Shafiq | Davis | Medium |
| Define content production pipeline (10–20 pieces/month) | Rohan | Daz | Val, Sean | All | Medium |

---

## Files Referenced
- [Meetings/Weekly seniors alignment - 09 Mar 2026.md](../Meetings/Weekly%20seniors%20alignment%20-%2009%20Mar%202026.md) — source of all decisions and action items
- [workflows/beta-engagement-workflow-v1.png](../workflows/beta-engagement-workflow-v1.png) — canonical workflow diagram (Steps 1–3c + design pipeline)
- [agent/instructions/create-linear-project.md](../agent/instructions/create-linear-project.md) — agent playbook for Linear project + milestone + issue creation
- [agent/Project_Template.md](../agent/Project_Template.md) — template for Linear project descriptions
- [agent/Task_Template.md](../agent/Task_Template.md) — template for Linear issue descriptions
- [agent/instructions/next-session.md](../agent/instructions/next-session.md) — MCP reconnect checklist + reference project IDs

---

## Verification / How to Validate This Project Is Done

1. **Linear MCP live:** `list_projects` returns results before touching anything.
2. **Project created correctly:** `AST-Internal-BetaWorkflow` exists in Linear with 3-block description (Header, Overview, Milestones) — no RACI, no SOW embedded.
3. **4 milestones exist:** Phase 1–4 created as Linear milestone objects, matching the Milestones table in the project description.
4. **Issues follow template:** Each issue has a verb-phrase title, 1-sentence Task Overview, and max 5 AC checkboxes. Task Blockers and Task Dropoff are empty on creation.
5. **Epic 4 is a document:** "Admiral Systems — Team Operations & Policies" exists as a Linear Document, not issues.
6. **Dry run of Steps 2b → 3b → 3c:** Claude produces a valid Linear project brief + issues for a sample project with zero manual filling-in.
7. **Live test on Joshua's Law Firm (Steps 2 onwards):** Once workflow is improved, it is applied to Joshua's project (tracked separately).
8. **Team adoption:** All seniors posting Linear updates using the agreed template within the first week.
