---
title: "Action Plan Checklists"
created: 2026-03-10
updated: 2026-03-21
tags:
  - delivery/linear
  - type/checklist
status: active
---

# Phased Action Plan & Checklists
## Admiral Systems — Linear Workspace Improvement

**Start Date:** March 8, 2026
**Timeline:** 4 weeks to implement core changes, ongoing hygiene thereafter

---

## Phase 1: Emergency Triage (Week 1: Mar 8-14)

### R1. Triage daz's Active Issues

**Goal:** Reduce daz from 36 active issues to max 7, focused on 2-3 projects.

**Process:** For each of daz's active issues, make ONE decision:

- [ ] **DELEGATE** — Reassign to a specific person with capacity (davis, luthfi, tiara)
- [ ] **DEFER** — Move to Backlog, remove from current sprint, update due date
- [ ] **CANCEL** — Cancel with a reason if no longer relevant

**Triage meeting:** Schedule 1-hour session with daz + delivery lead.

**Decision framework:**
1. Is this client-facing with a real deadline this month? -> Keep (max 7)
2. Is someone else able to do this? -> Delegate
3. Is this a recurring ops task that's never been completed? -> Cancel and set up as Linear recurring issue
4. Everything else -> Defer to backlog

**See companion file:** `Daz-Active-Issues-Triage.csv` for the full list with triage columns.

### R2. Triage All 233 Overdue Issues

**Goal:** Reduce from 233 to <30 overdue issues.

**Process:** Each assignee triages their own overdue items in a 30-min session:

- [ ] **daz** — 143 overdue issues (bulk of these are recurring tasks: cancel those first)
- [ ] **haykal** — 21 overdue (mostly weekly SEO content: cancel/consolidate)
- [ ] **elfajri** — 15 overdue
- [ ] **sean** — 12 overdue
- [ ] **tiara.almira** — 9 overdue
- [ ] **luthfi** — 6 overdue
- [ ] **prj-website-rev** — 5 overdue (external — notify client contact)
- [ ] **davis** — 4 overdue
- [ ] **rohan** — 3 overdue
- [ ] **shafiq** — 2 overdue
- [ ] **Unassigned** — 13 overdue (assign an owner or cancel)

**For each overdue issue, choose ONE action:**
1. Still needed with a real deadline? -> **Update the due date** to a realistic one
2. Still needed but no hard deadline? -> **Remove the due date**, keep in backlog
3. No longer relevant? -> **Cancel** with a brief reason

**See companion file:** `Overdue-Issues-Triage.csv` for the full list.

### R3. Close [ARCHIVED] HPL Project

**Goal:** Zero open issues on the archived project.

- [ ] Review the 3 "In Progress" issues — migrate to HPL-BETA-RMD-2026 if still relevant
- [ ] Bulk-cancel remaining 37 open issues with note: "Migrated to HPL-BETA-RMD-2026 or no longer relevant"
- [ ] Verify [ARCHIVED] HPL-BetaEngagement-RMD shows 0 open issues
- [ ] Document any context that needs to carry over to the new HPL project

### Phase 1 Completion Criteria

- [ ] daz has <=7 active issues
- [ ] daz is focused on <=3 projects
- [ ] Overdue count is <50 (after recurring task cleanup)
- [ ] [ARCHIVED] HPL project has 0 open issues
- [ ] All recurring ops tasks have been canceled and replaced with Linear recurring issues (or a single weekly checklist)

---

## Phase 2: Build the Capacity Model (Weeks 2-3: Mar 15-28)

### R4. Establish Per-Person Throughput Baselines

- [ ] Share the throughput data with each team member for validation
- [ ] Agree on capacity numbers (issues/month) per person:

| Person | Proposed Capacity | Capability | Validated? |
|---|---|---|---|
| davis | ~17 issues/mo | Dev/Data | [ ] |
| elfajri | ~13 issues/mo | Dev | [ ] |
| sean | ~8 issues/mo | Dev/Design | [ ] |
| luthfi | ~7 issues/mo | Dev | [ ] |
| daz | ~7 issues/mo | Strategy/Ops | [ ] |
| tiara.almira | ~5 issues/mo | Design/Dev | [ ] |
| haykal | ~4 issues/mo | Dev/AI | [ ] |
| shafiq | ~2 issues/mo | Dev | [ ] |

- [ ] Document agreed baselines in a shared location (Notion/Linear docs)
- [ ] Calculate points-per-sprint capacity for each person

### R5. Make Estimation Mandatory for Client Work

- [ ] Announce policy: all client project issues must have an estimate before entering a sprint
- [ ] Backfill estimates on current In Progress and In Review items
- [ ] Use fibonacci scale: 1, 2, 3, 5, 8 (already in use, just enforce consistency)
- [ ] Set up a Linear workflow rule or team agreement: issues without estimates cannot be moved to "In Progress"
- [ ] Track estimation coverage weekly (target: >90% for client work within 2 weeks)

### R6. Add Work Type Field

- [ ] Create a custom field in Linear called "Work Type" with values:
  - `Design`
  - `Development`
  - `Data`
  - `Strategy/Ops`
- [ ] Apply to all active client project issues (start with In Progress, then Backlog)
- [ ] Train team: every new issue gets a work type when created
- [ ] Goal: 100% coverage on new issues, >80% on existing active issues by end of Phase 2

### R7. "No Ticket, No Work" Policy

- [ ] Announce policy to all team members and leadership/commercial team
- [ ] Set up Slack -> Linear shortcut (Linear's Slack integration) for quick ticket creation
- [ ] Create a Linear template for "ad hoc requests" with minimal required fields:
  - Title
  - Assignee
  - Work Type
  - Estimate
  - Project (or "Unplanned")
- [ ] Establish weekly audit: each team member reports any untracked work in standup
- [ ] Leadership buy-in: seniors and commercial team commit to creating tickets for all requests

### Phase 2 Completion Criteria

- [ ] Throughput baselines published and agreed upon by team
- [ ] >80% estimation coverage on active client issues
- [ ] Work Type field exists and is populated on >50% of active issues
- [ ] Slack -> Linear shortcut is live and team has been trained
- [ ] "No Ticket, No Work" policy is documented and communicated

---

## Phase 3: Process Discipline (Weeks 3-4: Mar 22 - Apr 4)

### R8. Sprint Discipline with Hard Limits

- [ ] Define sprint capacity per person:
  - Formula: `monthly throughput baseline * (sprint length / 30 days) * 0.8 (20% buffer)`
  - Example for 2-week sprint: davis = 17 * (14/30) * 0.8 = ~6-7 issues per sprint
- [ ] Establish sprint planning ceremony (if not already in place):
  - Review capacity per person
  - Load sprint only up to capacity limits
  - If sprint is full, new work goes to NEXT sprint
- [ ] Set up Linear sprint views that show capacity vs. loaded
- [ ] Rule: anything NOT in a sprint is explicitly "not committed to the client"
- [ ] Track sprint completion rate weekly (target: >80%)

**Per-person sprint capacity (for 2-week sprints):**

| Person | Issues/Sprint | Points/Sprint |
|---|---|---|
| davis | 6-7 | 24-28 |
| elfajri | 5-6 | 20-24 |
| sean | 3-4 | 12-16 |
| luthfi | 3 | 12 |
| daz | 3 | 12 |
| tiara.almira | 2-3 | 8-12 |
| haykal | 2 | 8 |
| shafiq | 1 | 4 |

### R9. Create the Commercial Capacity Dashboard

- [ ] Set up the dashboard (see `Capacity-Dashboard-Snapshot.md`)
- [ ] Assign owner for weekly updates (delivery lead)
- [ ] Schedule: update every Monday, share with commercial team
- [ ] Make it the required input for all "should we take this project?" conversations
- [ ] Review format after 2 weeks and iterate

### R10. Fix Priority System

- [ ] Define priority thresholds and communicate to team:
  - **Urgent** (<5%): Client SLA breach, production down, revenue at risk
  - **High** (20-25%): Current sprint commitments, client deadlines this week
  - **Medium** (40-50%): Planned upcoming work, next sprint candidates
  - **Low** (20-30%): Nice-to-haves, internal improvements
- [ ] Bulk re-triage current issues (focus on the 386 "High" items first):
  - How many are actually current sprint commitments? -> Keep as High
  - How many are just "important but not this sprint"? -> Downgrade to Medium
  - How many are internal/backlog items? -> Downgrade to Low
- [ ] Track priority distribution weekly until it reaches healthy ranges

### Phase 3 Completion Criteria

- [ ] Sprint capacity limits defined and enforced for all team members
- [ ] Capacity Dashboard is live and updated weekly
- [ ] Priority distribution: <10% Urgent, <30% High
- [ ] Sprint planning ceremony in place with capacity checks
- [ ] Sprint completion rate >60% for first sprint under new system

---

## Phase 4: Workspace Hygiene (Ongoing: Apr 5+)

### R11. Workspace Cleanup

**Labels:**
- [ ] Audit all 90 existing labels — list which are in use vs. dead
- [ ] Consolidate to ~15-20 meaningful labels organized by category:
  - Type: `bug`, `feature`, `improvement`, `maintenance`, `documentation`
  - Phase: `discovery`, `design`, `development`, `qa`, `uat`
  - Status modifier: `blocked`, `needs-info`, `client-review`
- [ ] Remove duplicate/conflicting labels (e.g., "p1-high" since priority field exists)
- [ ] Batch-update existing issues to new label taxonomy

**Archived/Completed Projects:**
- [ ] ORG-Gamma-CDPEngineering (89% done, 0 active) -> Close remaining issues, mark Completed, archive
- [ ] PLU-Beta-P_SPL (marked Completed, 7 active) -> Close or reassign the 7 review items, then properly mark complete
- [ ] SB-StudioScents (marked Completed, 5 active) -> Close or reassign active items

**Triage Queue:**
- [ ] Clear the 34 items stuck in Triage (avg 116 days)
  - Assign each to a person or cancel
  - Set up a rule: nothing stays in Triage >48 hours
- [ ] Designate a triage owner per team

**Stale Backlog:**
- [ ] Review 75+ issues >90 days old in backlog
  - Still relevant? -> Add to upcoming sprint or update description
  - Not relevant? -> Cancel with reason
- [ ] Set up monthly backlog grooming ceremony (30 min, first Monday of month)

**Calendar Invite Noise:**
- [ ] Cancel/delete the ~20 auto-imported calendar invitations (DLVRY-196 to DLVRY-216)
- [ ] Disable or fix the email-to-Linear integration that created them

**Project Data Cleanup:**
- [ ] Fix incorrect target dates:
  - XCL target date: Feb 2025 -> correct to actual date
  - UTV target date: 2024 -> correct to actual date
  - ANI6 target date: May 2025 -> correct to actual date
- [ ] Add summaries to the 5 projects missing them
- [ ] Add milestones to the 7 active projects missing them
- [ ] Update project health status for all active projects (7 show "No updates")

**Naming Convention:**
- [ ] Document the naming convention and what Greek letters mean
- [ ] Standardize: `{CLIENT}-{Phase}-{Team/Capability}`
- [ ] Apply to future projects consistently

### Phase 4 Completion Criteria

- [ ] Labels reduced to <=20, all actively used
- [ ] All completed projects properly archived
- [ ] Triage queue at 0, with <48hr SLA enforced
- [ ] No backlog items older than 90 days without a recent review
- [ ] All project metadata (dates, summaries, milestones) is current
- [ ] Calendar noise deleted and integration fixed

---

## Ongoing Weekly Cadence

After all phases are complete, maintain these weekly rituals:

| Day | Activity | Owner | Duration |
|---|---|---|---|
| Monday | Update Capacity Dashboard | Delivery Lead | 15 min |
| Monday | Sprint planning / capacity check | All | 30 min |
| Wednesday | Mid-week progress check (async in Linear) | All | 5 min |
| Friday | Weekly closing: complete/cancel/carry over | All | 15 min |
| 1st Monday/mo | Backlog grooming | All | 30 min |
| 1st Monday/mo | Capacity review with commercial team | Delivery + Commercial | 30 min |

---

## Success Metrics (Track Weekly)

| Metric | Week 1 | Week 2 | Week 3 | Week 4 | Target |
|---|---|---|---|---|---|
| Overdue issues | | | | | <30 |
| Avg active per person | | | | | <7 |
| Max active (any person) | | | | | <10 |
| Estimation coverage | | | | | >90% |
| Work type coverage | | | | | >90% |
| Sprint completion rate | | | | | >80% |
| Priority: % Urgent+High | | | | | <30% |
| Items in Triage | | | | | 0 |

*Fill in each week to track progress against targets.*
