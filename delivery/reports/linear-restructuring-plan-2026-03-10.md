---
title: "Linear Restructuring Plan"
created: 2026-03-10
updated: 2026-03-21
tags:
  - delivery/linear
  - type/report
status: active
---

**Linear Restructuring Plan**

Operational Audit & Strategic Transformation Roadmap

Admiral Systems (Devhaus Pte. Ltd.) | March 2026

Document Owner: Daz (COO) | Linear Owner: Shafiq Yussaini

CONFIDENTIAL — Internal Use Only

# **Table of Contents**

# **Executive Summary**

**The Problem**

Linear is not functioning as a single source of truth. Six people tackle one project with nobody knowing who does what. Every client project is exceeding 3 months. Seniors say yes to deadlines they cannot hit. Timeline visibility is misleading — the Scott Walker project dropped from 77% to 61% completion with no early warning. Updates live in Slack and WhatsApp, not Linear. Juniors get lost because issues lack specs, schemas, and creative direction.

**The Audit Verdict**

After a full review of the admiralhq workspace (14 teams, 24 projects, 65+ labels, 15 users), the existing SOP documentation is comprehensive but almost none of it is reflected in the live workspace. The gap between documented standards and actual usage is the root cause of operational chaos.

**The Plan**

This document provides a 4-week phased restructuring plan that consolidates teams under a 3-company umbrella model, reduces 67 labels to ~30, enforces mandatory fields on every issue, and establishes Shafiq as the single Linear owner with clear escalation paths. The Jireh Law project serves as the validation testbed before rolling out to paying clients.

> **Updated March 16, 2026** — Post-implementation review. Team restructure and priority sync completed. Cleanup begins week of 17 March using Linear views as the primary cleanup mechanism.

| ICE Score           | Impact                                  | Confidence                                  | Ease                                |
| :------------------ | :-------------------------------------- | :------------------------------------------ | :---------------------------------- |
| **6.4 (P1 — High)** | 9/10 — Every project is bleeding margin | 80% — Proven frameworks, team buy-in needed | 8/10 — Config changes, no new tools |

# **Part 1: Current State Audit**

## **1.1 Workspace Architecture — Team Sprawl**

The workspace contains 14 teams. This is approximately 2.5x more than a team of 15 active users should have. Per-client teams (P-RCG, P-Cartracker, P-XCL, P-ANI6, P-ORG, P-LevelUp) fragment workload visibility and make it impossible to see who is doing what across the organisation.

| Team                  | Key   | Purpose                  | Verdict                                       |
| :-------------------- | :---- | :----------------------- | :-------------------------------------------- |
| **DeliveryHQ**        | DLVRY | Client delivery hub      | KEEP ✅ — Umbrella for all delivery sub-teams |
| **Admiral-Projects**  | —     | Admiral client projects  | CREATED ✅ — Sub-team under DeliveryHQ        |
| **RMD-Projects**      | —     | RMD client projects      | CREATED ✅ — Sub-team under DeliveryHQ        |
| **Sprklabs-Projects** | —     | Sprklabs client projects | CREATED ✅ — Sub-team under DeliveryHQ        |
| **Internal**          | —     | Internal ops + strategy  | CREATED ✅ — Replaces AdmiralGroup            |
| **Leadership**        | —     | Cross-company leadership | CREATED ✅                                    |
| **Advisors**          | —     | Advisory board           | EXISTS — Not actively in use                  |
| **Devstudio**         | —     | Indonesia ops            | EXISTS — Not actively in use                  |
| **AdmiralGroup**      | AST   | Legacy internal ops      | ARCHIVED ✅                                   |
| **DAZ**               | DAZ   | Personal team            | ARCHIVED ✅                                   |
| **P-RCG**             | RCG   | Client team              | ARCHIVED ✅                                   |
| **P-Cartracker**      | PCT   | Client team              | ARCHIVED ✅                                   |
| **P-XCL**             | PXC   | Client team              | ARCHIVED ✅                                   |
| **P-ANI6**            | ANI6  | Client team              | ARCHIVED ✅                                   |
| **P-ORG**             | PORG  | Client team              | ARCHIVED ✅                                   |
| **P-LevelUp**         | —     | Client team              | ARCHIVED ✅                                   |

**Implemented State (as of March 15, 2026):** 6 active teams under a 3-company umbrella model. DeliveryHQ acts as the delivery hub with Admiral-Projects, RMD-Projects, and Sprklabs-Projects as entity sub-teams. Internal handles all internal ops. Leadership handles cross-company strategy. All 8 per-client and legacy teams have been archived.

## **1.2 Label Taxonomy — Redundancy & Overlap**

65 labels exist across the workspace. Many are redundant with native Linear features (priority labels duplicate Linear’s built-in priority system) or overlap with each other (engagement model labels vs. project labels vs. tier labels). The tiered structure from the SOP has been partially implemented but not enforced.

| Category             | Current Count | Target Count | Action                                                                                                                                  |
| :------------------- | :------------ | :----------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **Priority (p0-p3)** | 4             | 4            | KEEP + SYNC ✅ — Labels retained for SLA context; Linear Priority field synced to match so issues can be sorted natively. Both coexist. |
| **Engagement model** | 6             | 5            | KEEP — alpha through epsilon                                                                                                            |
| **Client tags**      | 10            | 10           | KEEP — Active clients only                                                                                                              |
| **Work discipline**  | 6             | 5            | SLIM — design, frontend, backend, data, content                                                                                         |
| **Project phase**    | 4             | 4            | KEEP — discovery, design-phase, development, launch                                                                                     |
| **Urgency/due**      | 4             | 0            | DELETE — Use Linear due dates                                                                                                           |
| **Status flags**     | 4             | 3            | SLIM — blocked, needs-review, needs-qa                                                                                                  |
| **Financial**        | 4             | 0            | DELETE — Use custom fields                                                                                                              |
| **Location**         | 3             | 2            | KEEP — sg, id                                                                                                                           |
| **Entity**           | 5             | 3            | SLIM — admiral, sprklabs, rmd                                                                                                           |
| **Other/legacy**     | 15            | 0            | DELETE — Clean up                                                                                                                       |

**Current state (March 16, 2026):** 67 labels. Cleanup begins week of 17 March using dedicated Linear views to surface issues needing label attention.

**Target State:** \~30 labels maximum, organised in 5 tiers: Engagement Model, Client, Discipline, Phase, Status. All other metadata via custom fields or native Linear features.

## **1.3 Issue Quality — The Real Problem**

The BetaWorkflow project (created 9 March 2026 by Shafiq) demonstrates the issue template structure is being followed: issues have acceptance criteria, task overviews, and blockers sections. However, across all 19 issues, zero have due dates and zero have estimates. This is the single biggest operational gap. Without dates and estimates, Linear cannot provide timeline visibility, capacity planning, or early warning signals.

| Compliance Check                    | Status       | Target     | Gap                                      |
| :---------------------------------- | :----------- | :--------- | :--------------------------------------- |
| **Issues with due dates**           | **CRITICAL** | 100%       | 0% of BetaWorkflow issues have dates     |
| **Issues with estimates**           | **CRITICAL** | 100%       | 0% of BetaWorkflow issues have estimates |
| **Issues with acceptance criteria** | **OK**       | 100%       | 100% compliance — well done Shafiq       |
| **Issues with assignees**           | **OK**       | 100%       | 100% compliance                          |
| **Issues with milestones**          | **OK**       | 100%       | 3 milestones across 19 issues            |
| **Issues with labels**              | **CRITICAL** | 100%       | 0% have any labels applied               |
| **Project-level updates**           | **CRITICAL** | Weekly     | No project updates logged                |
| **ICE scores on issues**            | **CRITICAL** | All P0/P1  | Zero ICE scoring in practice             |
| **RACI custom fields**              | **CRITICAL** | All issues | Fields not configured in workspace       |

## **1.4 Project Naming — Inconsistent Convention**

The SOP defines CLIENT-MODEL-TYPE-PERIOD but actual projects use mixed formats:

| Current Name              | Should Be                  | Compliant? |
| :------------------------ | :------------------------- | :--------- |
| SB-AST-JirehLaw           | JRL-Beta-Website-2026      | No         |
| HPL-BETA-RMD-2026         | HPL-Beta-RMD-2026          | Close      |
| ANI6-Beta-AST             | ANI-Beta-Website-2026      | No         |
| CT-Beta-P_RMD-Q3          | CT-Beta-Website-Q3         | No         |
| ORG-Gamma-CDPEngineering  | ORG-Gamma-CDP-2025         | Close      |
| AST-Internal-BetaWorkflow | AST-Internal-Workflow-2026 | Close      |

# **Part 2: Root Cause Analysis**

Mapping the problem statements from the meeting to root causes in Linear:

| Problem                                       | Root Cause in Linear                                                           | Fix                                                                          |
| :-------------------------------------------- | :----------------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| **6 people, nobody knows who does what**      | No RACI fields configured. Assignee is the only accountability marker.         | Configure RACI custom fields. Enforce R+A on every issue.                    |
| **Seniors doing PM \+ ops \+ delivery**       | No workstream separation. All work flows through same status pipeline.         | Dedicated senior initiative project. Separate internal vs. client boards.    |
| **Juniors taking contradictory instructions** | Multiple seniors can comment/assign without clear authority chain.             | Single Accountable person per issue. Juniors only take direction from A.     |
| **Every project exceeding 3 months**          | Zero due dates. Zero estimates. No velocity tracking possible.                 | Mandatory dates \+ estimates. Block status transition without them.          |
| **Over-delivery destroying margins**          | No scope boundary markers. No commercial approval gate.                        | Add scope-change label. Require Rohan/Daz approval for new scope.            |
| **No one chasing client feedback**            | No client-delay tracking. No SLA on blocked status.                            | Add client-blocked status. Auto-escalate after 48hrs.                        |
| **SOWs drafted without tech sign-off**        | No issue linking between commercial and technical workstreams.                 | Mandatory blockedBy link to tech review issue before SOW moves to Done.      |
| **Scott project dropped 77% to 61%**          | Linear % is based on issue count, not weighted effort. Reopened issues drop %. | Use milestone-based tracking. Weekly project updates are mandatory.          |
| **Updates in Slack not Linear**               | No enforcement mechanism. No consequence for missing updates.                  | Shafiq’s standup bot posts to Linear. Weekly project update is a scored KPI. |

# **Part 3: The Restructuring Plan**

## **3.1 New Team Architecture ✅ Completed March 15, 2026**

Consolidated from 14 teams into a 3-company umbrella model with 6 active teams:

```
DeliveryHQ               ← delivery hub (all client work flows through here)
├── Admiral-Projects     ← Admiral Systems client projects
├── RMD-Projects         ← RMD client projects
└── Sprklabs-Projects    ← Sprklabs client projects
Internal                 ← internal ops, HR, commercial, learning & development
Leadership               ← cross-company strategy and oversight
```

> Advisors and Devstudio teams exist in the workspace but are not currently in active operational use.

| Team                  | Purpose                  | Lead        | Status    |
| :-------------------- | :----------------------- | :---------- | :-------- |
| **DeliveryHQ**        | Delivery hub             | Shafiq (PM) | Active ✅ |
| **Admiral-Projects**  | Admiral client work      | Shafiq (PM) | Active ✅ |
| **RMD-Projects**      | RMD client work          | Shafiq (PM) | Active ✅ |
| **Sprklabs-Projects** | Sprklabs client work     | Shafiq (PM) | Active ✅ |
| **Internal**          | Internal ops + strategy  | Daz (COO)   | Active ✅ |
| **Leadership**        | Cross-company leadership | Daz (COO)   | Active ✅ |

**What was done (March 15, 2026):**

1. All 8 per-client and legacy teams archived (P-RCG, P-XCL, P-ANI6, P-ORG, P-Cartracker, P-LevelUp, DAZ, AdmiralGroup).
2. All 22 projects reassigned to their correct entity sub-team. DeliveryHQ remains as the parent hub across all projects.
3. RMD entity handled via the RMD-Projects sub-team, not a label merge.

## **3.2 Mandatory Issue Fields (Week 1\)**

Every issue in Linear must have these fields completed before it can move to In Progress:

| Field                 | Type         | Required? | Who Sets It      | Enforcement                  |
| :-------------------- | :----------- | :-------- | :--------------- | :--------------------------- |
| **Title**             | Text         | Yes       | Creator (senior) | Linear native                |
| **Description \+ AC** | Markdown     | Yes       | Creator (senior) | Template enforced            |
| **Assignee**          | User         | Yes       | Creator or PM    | Linear native                |
| **Due Date**          | Date         | Yes       | PM or senior     | Automation blocks transition |
| **Estimate (points)** | Number       | Yes       | PM or senior     | Automation blocks transition |
| **Priority**          | Select       | Yes       | PM (from ICE)    | Auto-set from ICE score      |
| **Project**           | Project      | Yes       | Creator          | Linear native                |
| **Milestone**         | Milestone    | Yes       | PM               | Manual enforcement           |
| **Labels (min 2\)**   | Multi-select | Yes       | Creator          | Client \+ discipline minimum |
| **Accountable (A)**   | User         | Yes       | PM               | Custom field — single user   |

## **3.3 Issue Creation Rules (Week 1\)**

**Senior-Only Issue Creation**

**Issue Template (Mandatory for all issues):**

Every issue must follow this structure. No exceptions.

\# Task Overview

\[2-3 sentences: what needs to happen, why it matters, what the output looks like\]

\#\# Acceptance Criteria

\- \[ \] Criteria 1 (specific, testable, binary pass/fail)

\- \[ \] Criteria 2 (maximum 5 criteria)

\#\# Task Blockers

\[What could stop this from being completed\]

\#\# Task Dropoff

\[What happens after this is done — who reviews, what’s next\]

## **3.4 Project-Level Updates (Week 2\)**

**Weekly Project Update Template:**

Every active project gets a project-level update every Friday by 4 PM SGT. This is Shafiq’s responsibility to enforce. Rohan and Daz read project updates — they should never need to dig into issues.

Format:

HEALTH: \[Green/Amber/Red\]

PROGRESS: \[X% complete, was Y% last week\]

THIS WEEK: \[3 bullet max — what was delivered\]

NEXT WEEK: \[3 bullet max — what’s planned\]

RISKS: \[Anything that could derail timeline or margin\]

CLIENT STATUS: \[Last contact date, any pending decisions\]

MARGIN CHECK: \[On track / At risk / Breached \+ % if available\]

## **3.5 Client Delay Tracking (Week 2\)**

A new workflow status is needed in DeliveryHQ:

| Status          | When to Use                  | Auto-Action                  | Escalation                                              |
| :-------------- | :--------------------------- | :--------------------------- | :------------------------------------------------------ |
| **Triage**      | New issue, needs review      | None                         | PM reviews within 24hrs                                 |
| **Todo**        | Reviewed, ready for sprint   | None                         | None                                                    |
| **In Progress** | Actively being worked on     | Start timer in Tracking Time | None                                                    |
| **Blocked**     | Waiting on client input      | Stop timer. Start SLA clock. | Auto-notify after 48hrs. Escalate to Rohan after 72hrs. |
| **In Review**   | Ready for QA or approval     | None                         | PM reviews within 24hrs                                 |
| **Done**        | Completed, acceptance met    | Stop timer                   | None                                                    |
| **Cancelled**   | Descoped or no longer needed | Archive                      | None                                                    |

## **3.6 Scope Change Protocol (Week 2\)**

Any work not in the original SOW is a scope change. It must be evaluated before it enters Linear:

Step 1: Senior identifies scope change.

Step 2: Senior creates issue with label scope-change and assigns to Rohan.

Step 3: Rohan evaluates commercial impact (does this affect margin? Does the client pay extra?).

Step 4: If approved, Rohan changes label to scope-approved and assigns back to delivery.

Step 5: If rejected, issue is Cancelled with reason documented.

**No scope change enters the sprint without Rohan’s approval. This is non-negotiable.**

## **3.7 Standup → Linear Integration (Week 3\)**

Shafiq’s current Slack standup format (yesterday/today/blockers) is good but siloed. The integration path:

Phase 1 (Immediate): Shafiq manually updates Linear issue comments with standup-relevant items at the end of each standup. 5 minutes, not negotiable.

Phase 2 (Week 3-4): Build a Slack-to-Linear bot that parses standup messages and creates comments on referenced issues. Use Linear issue identifiers (AST-320, DLVRY-45) in standup messages for auto-linking.

Phase 3 (Month 2+): Full automation where standup summaries generate project-level updates.

# **Part 4: AI Agent — SOW to Linear Pipeline**

## **4.1 Pipeline Architecture**

The sub-agent takes two inputs and produces a fully populated Linear project:

| Step  | Input                                  | Process                                                                                       | Output                       |
| :---- | :------------------------------------- | :-------------------------------------------------------------------------------------------- | :--------------------------- |
| **1** | Tally CSV (Business Readiness Compass) | Parse client context, industry, pain points, pricing model, market size                       | Client profile object        |
| **2** | SOW document (from Rohan/Daz)          | Extract scope, deliverables, timeline, budget, success criteria                               | Scope definition object      |
| **3** | Engagement model template (CSV)        | Match engagement type, pull issue templates with ICE scores and RACI defaults                 | Issue template array         |
| **4** | Claude merges 1+2+3                    | Personalise templates with client context, calculate dates from timeline, assign team members | Project brief \+ issue list  |
| **5** | Linear MCP integration                 | Create project, milestones, all issues via Linear API                                         | Live Linear project with URL |

## **4.2 Tally CSV Field Mapping**

The Business Readiness Compass submission maps to Linear project fields as follows:

| Tally Field                    | Maps To                            | Used In                          |
| :----------------------------- | :--------------------------------- | :------------------------------- |
| Company Name                   | Project name prefix                | Project creation                 |
| Company Website                | Project description \+ audit input | Step 2 audit process             |
| Industry                       | Engagement template selection      | Template matching                |
| Business Stage                 | Complexity/scope calibration       | ICE confidence scoring           |
| Team Size                      | Resource allocation hints          | RACI defaults                    |
| What keeps them awake at 3am?  | Project objectives                 | Issue descriptions               |
| How do customers find you?     | Channel strategy                   | Alpha/Gamma issue prioritisation |
| What makes you different?      | Positioning in project brief       | Project description              |
| How do you charge?             | Revenue model for ROI calc         | Margin projections               |
| Typical deal size              | Engagement model matching          | Budget allocation                |
| Sales cycle length             | Timeline calibration               | Milestone date setting           |
| Biggest marketing challenge    | Primary issue focus                | P0 issue identification          |
| Digital presence rating (1-10) | Scope complexity indicator         | Estimate multiplier              |

## **4.3 Jireh Law Validation Test**

The Jireh Law project (SB-AST-JirehLaw) is the designated test bed. Current state: project shell exists with brief but zero issues. Here is the validation plan:

| \#    | Validation Step                                                           | Success Criteria                                        | Owner  |
| :---- | :------------------------------------------------------------------------ | :------------------------------------------------------ | :----- |
| **1** | Run AI agent on Joshua’s Tally submission \+ Jireh SOW                    | Project brief auto-generated matches manual brief       | Shafiq |
| **2** | Verify all issues have: dates, estimates, AC, labels, assignee, milestone | 100% field compliance across all generated issues       | Shafiq |
| **3** | Verify RACI: every issue has R and A assigned                             | Zero issues without Accountable person                  | Shafiq |
| **4** | Run mock standup and verify Linear update flow                            | Issue comments reflect standup items within 10 mins     | Shafiq |
| **5** | Log a mock client delay and verify escalation                             | Client Blocked status triggers notification after 48hrs | Shafiq |
| **6** | Generate weekly project update                                            | Rohan/Daz can understand status in \<60 seconds         | Shafiq |
| **7** | Simulate scope change request                                             | Rohan receives notification, approval gate works        | Rohan  |
| **8** | Full team walkthrough                                                     | Team can find their issues, understand next actions     | Daz    |

# **Part 5: 4-Week Implementation Roadmap**

## **Week 1: Foundation (10-16 March)**

**Theme: Clean the house. Zero new features — just fix what’s broken.**

| \#    | Task                                                          | Owner  | Effort  | ICE     | Status                                           |
| :---- | :------------------------------------------------------------ | :----- | :------ | :------ | :----------------------------------------------- |
| **1** | Archive 8 teams (DAZ, AdmiralGroup, all P-\* teams)           | Shafiq | 2 hours | **8.1** | ✅ Done — Mar 15                                 |
| **2** | Reassign all 22 projects to correct entity sub-teams          | Shafiq | 3 hours | **7.2** | ✅ Done — Mar 15                                 |
| **3** | Sync p0–p3 priority labels to Linear native Priority field    | Shafiq | 2 hours | **7.5** | ✅ Done — Mar 15 (153 issues updated)            |
| **4** | Set up Linear workspace views for operational visibility      | Shafiq | 2 hours | **8.0** | ✅ Done — Mar 16 (10 views configured)           |
| **5** | Add issues to Linear                                          | Shafiq | —       | —       | ✅ Done — Mar 16                                 |
| **6** | Label cleanup (67 labels → ~30)                               | Shafiq | 1 hour  | **6.4** | Rolling into Week 2                              |
| **7** | Rename all active projects to CLIENT-MODEL-TYPE-PERIOD format | Shafiq | 1 hour  | **5.4** | Rolling into Week 2                              |
| **8** | Add due dates \+ estimates to all active issues               | Shafiq | Ongoing | **9.0** | Rolling into Week 2 — use Missing Estimates view |
| **9** | Communicate changes to team via Slack (Daz sends the message) | Daz    | 30 mins | **8.0** | Pending                                          |

> **Note on items 6–10:** These roll into Week 2. The workspace views created in item 4 (Missing Estimates, No Priority Set, Floating Issues, etc.) are now the primary cleanup mechanism — rather than batch-fixing manually, the team will work through these views weekly.

## **Week 2: Enforcement (17-21 March)**

**Theme: Make it impossible to do it wrong.**

| \#    | Task                                                                  | Owner         | Effort  | ICE     |
| :---- | :-------------------------------------------------------------------- | :------------ | :------ | :------ |
| **1** | Set up Linear automations: block In Progress without date \+ estimate | Shafiq        | 2 hours | **9.0** |
| **2** | Create scope-change and scope-approved labels \+ workflow             | Shafiq        | 1 hour  | **7.5** |
| **3** | Write weekly project update template and distribute                   | Shafiq        | 1 hour  | **7.0** |
| **4** | First Friday project update for all active projects                   | Shafiq        | 3 hours | **8.0** |
| **5** | Train juniors on new workflow (30 min session, recorded)              | Shafiq        | 1 hour  | **6.5** |
| **6** | Train seniors on issue creation standards (30 min session)            | Shafiq \+ Daz | 1 hour  | **7.0** |
| **7** | Begin Jireh Law AI agent test (Steps 1-3 of validation)               | Shafiq        | 4 hours | **7.2** |
| **8** | Set up Slack notification for Client Blocked \>48hr                   | Shafiq        | 1 hour  | **6.0** |

## **Week 3: Integration (24-28 March)**

**Theme: Connect the dots. Linear becomes the nerve centre.**

| \#    | Task                                                       | Owner           | Effort  | ICE     |
| :---- | :--------------------------------------------------------- | :-------------- | :------ | :------ |
| **1** | Complete Jireh Law validation (Steps 4-8)                  | Shafiq          | 4 hours | **7.5** |
| **2** | Standup-to-Linear manual posting begins (Phase 1\)         | Shafiq          | Ongoing | **6.5** |
| **3** | Run AI agent on Hop Lun project as second test             | Shafiq          | 3 hours | **6.0** |
| **4** | First full weekly audit: dates, estimates, labels, updates | Shafiq          | 2 hours | **8.0** |
| **5** | Share audit results with team \+ Daz                       | Shafiq          | 30 mins | **7.0** |
| **6** | Iterate on AI agent based on Jireh \+ Hop Lun learnings    | Shafiq \+ Davis | 4 hours | **6.5** |
| **7** | Configure Tracking Time sync for Jireh Law project         | Shafiq          | 2 hours | **5.5** |
| **8** | Begin standup bot development (Phase 2\) if Phase 1 works  | Davis           | 8 hours | **5.0** |

## **Week 4: Scale (31 March \- 4 April)**

**Theme: Roll out to all active projects. Measure everything.**

| \#    | Task                                                                 | Owner          | Effort  | ICE     |
| :---- | :------------------------------------------------------------------- | :------------- | :------ | :------ |
| **1** | Apply new standards to all active projects (HPL, ANI6, CT, ORG, WLX) | Shafiq         | 6 hours | **8.5** |
| **2** | Full compliance audit: publish scorecard to team                     | Shafiq         | 2 hours | **7.0** |
| **3** | AI agent available for all new projects going forward                | Shafiq         | 2 hours | **7.5** |
| **4** | Retrospective: what worked, what didn’t, what to iterate             | Shafiq \+ Daz  | 1 hour  | **6.0** |
| **5** | Update Linear SOP document with actual learnings                     | Shafiq         | 2 hours | **5.5** |
| **6** | Present results to advisory board (Andrew, Simon, Alex)              | Daz            | 1 hour  | **6.0** |
| **7** | Set monthly cadence: first Monday audit, second Monday retro         | Shafiq         | 30 mins | **5.0** |
| **8** | Jireh Law project goes live — validate hypercare workflow            | Shafiq \+ Sean | 2 hours | **7.0** |

# **Part 6: RACI for the Restructuring Itself**

This restructuring plan needs its own RACI to avoid the exact problem it’s trying to fix:

| Activity                         | R          | A          | C             | I            |
| :------------------------------- | :--------- | :--------- | :------------ | :----------- |
| **Linear workspace restructure** | **Shafiq** | **Daz**    | Davis, Sean   | All team     |
| **Team communication**           | **Daz**    | **Daz**    | Shafiq        | All team     |
| **AI agent development**         | **Shafiq** | **Shafiq** | Davis, Daz    | Rohan        |
| **Label \+ field configuration** | **Shafiq** | **Shafiq** | Daz           | Davis, Sean  |
| **Training delivery**            | **Shafiq** | **Shafiq** | Daz           | All team     |
| **Weekly audits**                | **Shafiq** | **Daz**    | None          | All team     |
| **Scope change process**         | **Rohan**  | **Daz**    | Davis         | Shafiq, team |
| **Client communication changes** | **Rohan**  | **Daz**    | Davis         | Shafiq, Sean |
| **Jireh Law validation**         | **Shafiq** | **Shafiq** | Sean, Elfajri | Daz, Joshua  |
| **Advisory board presentation**  | **Daz**    | **Daz**    | Rohan         | Advisors     |

# **Part 7: Risk Register**

| Risk                                                   | Likelihood | Impact       | Mitigation                                                                | Owner  |
| :----------------------------------------------------- | :--------- | :----------- | :------------------------------------------------------------------------ | :----- |
| **Seniors resist mandatory fields (dates, estimates)** | High       | **Critical** | Daz sends clear message: this is not optional. Shafiq enforces weekly.    | Daz    |
| **Team reverts to Slack/WhatsApp for updates**         | High       | **High**     | Shafiq’s standup bridges the gap. Public scorecard creates peer pressure. | Shafiq |
| **AI agent produces inaccurate issues**                | Medium     | **Medium**   | Jireh Law is non-revenue test. Iterate before paying clients.             | Shafiq |
| **Juniors confused by new workflow**                   | Medium     | **Low**      | Recorded training session. Buddy system for first 2 weeks.                | Shafiq |
| **Migration breaks existing project tracking**         | Low        | **High**     | Archive, don’t delete. All data preserved and recoverable.                | Shafiq |
| **Rohan doesn’t engage with scope change gate**        | Medium     | **Critical** | Daz escalation. Auto-notify if scope-change sits \>48hrs.                 | Daz    |
| **Client-Blocked SLA causes false positives**          | Medium     | **Low**      | Set 48hr threshold initially, tune based on Week 2 data.                  | Shafiq |

# **Part 8: Success Metrics**

Measured weekly by Shafiq, reported to Daz every Friday:

| Metric                                   | Current | Week 2 Target | Week 4 Target | Measurement              |
| :--------------------------------------- | :------ | :------------ | :------------ | :----------------------- |
| **Issues with due dates**                | \~10%   | 70%           | 100%          | Linear filter            |
| **Issues with estimates**                | \~10%   | 70%           | 100%          | Linear filter            |
| **Issues with 2+ labels**                | \~5%    | 60%           | 90%           | Linear filter            |
| **Weekly project updates**               | 0%      | 50%           | 100%          | Manual check             |
| **Client delays logged in Linear**       | 0%      | 50%           | 90%           | Client Blocked count     |
| **Scope changes through approval gate**  | 0%      | 70%           | 100%          | scope-change label count |
| **Issue creation by seniors only**       | Unknown | 80%           | 95%           | Creator audit            |
| **Standup items reflected in Linear**    | 0%      | 30%           | 70%           | Comment audit            |
| **Average project overrun vs. timeline** | 30%+    | 20%           | \<10%         | Target date vs. actual   |
| **Daz can see workload in \<60 seconds** | No      | Partial       | Yes           | Daz’s judgement          |

# **Part 9: Next Actions**

Immediate (Today):

1\. Daz approves this plan and sends team-wide Slack message announcing Linear restructure.

2\. Shafiq begins Week 1 tasks (team archival, label cleanup).

3\. Davis reviews AI agent architecture (Part 4\) and flags any technical blockers.

Week of 17 March:

4\. Shafiq runs Jireh Law through the AI agent pipeline as first test.

5\. First Friday project update published for all active projects.

6\. Senior issue creation training delivered (30 min, recorded).

End of March:

7\. Full compliance audit published. Non-compliance is visible to entire team.

8\. AI agent validated on 2 projects (Jireh Law \+ Hop Lun).

9\. Retrospective completed. SOP updated with actual learnings.

# **Part 10: What's Been Built (March 15–16, 2026)**

The following operational artefacts were created during the initial implementation phase:

| Artefact                       | Purpose                                                                                                                                                                                                         |
| :----------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Linear Workspace Views**     | 10 custom views created at workspace level for leadership and team visibility. Covers WIP per person, triage queue, overdue issues, in-review bottleneck, priority health, capacity, and per-company overviews. |
| **Priority Mapping Reference** | Standalone context document explaining the p0–p3 label system, how SLA maps to each label, and why both labels and the Linear Priority field are maintained simultaneously.                                     |
| **Priority Sync Playbook**     | Step-by-step agent playbook for bulk-syncing p0–p3 labels to the Linear native Priority field. Used for periodic maintenance to keep priority data accurate for sorting and reporting.                          |

---

# **Part 11: Future Changes**

## **11.1 Priority Setting — Shift from SLA-Driven to ICE-Driven**

**Current model:** Priority labels (p0–p3) are assigned based on SLA thresholds.

| Label       | Current Criteria              |
| :---------- | :---------------------------- |
| p0-critical | Drop everything — 24-hour SLA |
| p1-high     | This week — 48-hour SLA       |
| p2-medium   | This sprint — 1-week SLA      |
| p3-low      | Backlog — no fixed SLA        |

**Future model:** Priority is determined by ICE score (Impact × Confidence × Ease). SLA becomes one input that influences the ICE score — for example, a tight client deadline raises the Impact dimension — but it does not unilaterally determine the priority label.

**Why this matters:**

- Prevents gaming: a low-value task cannot claim p0 solely because of a self-imposed deadline
- Aligns priority with actual business value, not just urgency
- Gives leadership a defensible, consistent scoring method across all three companies

**What stays the same:** The p0–p3 label system is retained. Only the _criteria_ for assigning each label changes. Once ICE thresholds are agreed, the priority mapping reference document will be updated accordingly.

**Owner:** Daz (COO) to define ICE scoring thresholds per label tier. Shafiq to update the priority mapping reference and retrain the team.

---

_This document was originally generated from a live audit of the admiralhq Linear workspace on 10 March 2026. Updated 16 March 2026 — post-implementation review reflecting team restructure, project mapping, priority sync, and workspace view setup completed March 15–16, 2026._
