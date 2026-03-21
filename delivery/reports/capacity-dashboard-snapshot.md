---
title: "Capacity Dashboard Snapshot"
created: 2026-03-10
updated: 2026-03-21
tags:
  - delivery/capacity
  - type/report
status: active
---

# Commercial Capacity Dashboard
## Admiral Systems — Week of March 8, 2026

**Last Updated:** March 8, 2026
**Data Source:** Linear Export + Historical Throughput Analysis
**Update Frequency:** Weekly (every Monday)

---

## CAPACITY SNAPSHOT

### At a Glance

| Status | People | Action |
|---|---|---|
| OVER CAPACITY | elfajri, haykal, daz | Do NOT assign new work |
| AT CAPACITY | sean, shafiq | No new projects |
| AVAILABLE | davis, luthfi, tiara.almira | Can take new work |

---

## DESIGN CAPACITY

| Person | Active / Capacity | Projects | Status | Available For |
|---|---|---|---|---|
| tiara.almira | 3 / 5 | PLU, RCG, HPL | Available | 2 more design tasks |

**Design availability:** tiara.almira has ~2 slots available. Can take small-medium design engagements.

---

## DEVELOPMENT CAPACITY

| Person | Active / Capacity | Projects | Status | Available For |
|---|---|---|---|---|
| davis | 1 / 17 | ORG (wrapping up) | Available | Large new project |
| luthfi | 4 / 7 | RCG, SB | Available | Small-medium project |
| sean | 8 / 8 | XCL, ANI6 | FULL | Nothing new |
| elfajri | 21 / 13 | PLU, UTV, SPI, RCG, L&D | OVER CAPACITY | Must offload first |
| haykal | 21 / 4 | AST-Ops, AI-Gen | OVER CAPACITY | Must offload first |
| shafiq | 2 / 2 | HPL, RCG | FULL | Low throughput baseline |

**Dev availability:** davis has significant capacity (16 slots). luthfi has room for a small-medium engagement (3 slots).

---

## DATA / ENGINEERING CAPACITY

| Person | Active / Capacity | Projects | Status | Available For |
|---|---|---|---|---|
| davis | 1 / 17 | ORG (wrapping up) | Available | Large data/engineering project |

**Data availability:** davis is the primary data/engineering resource and is largely available.

---

## STRATEGY / OPS CAPACITY

| Person | Active / Capacity | Projects | Status | Available For |
|---|---|---|---|---|
| daz | 36 / 7 | 15 projects (!) | CRITICAL | Must triage immediately |

**Ops availability:** NONE. daz is at 5x capacity. Emergency triage required before any new ops work.

---

## DECISION MATRIX: Can We Take This Project?

### Before saying YES to any new engagement, answer these questions:

```
1. What capabilities does this project need?
   [ ] Design    -> Check tiara.almira's availability
   [ ] Dev       -> Check davis/luthfi availability
   [ ] Data      -> Check davis availability
   [ ] Strategy  -> BLOCKED (daz overloaded)

2. How many issues/month will it generate?
   Small project:   10-15 issues/month
   Medium project:  20-30 issues/month
   Large project:   40+ issues/month

3. Does the available person have room?
   Person's capacity - current active = available slots
   Available slots >= project's monthly issues?

4. Timeline check:
   Use estimation guide:
   1-2 pt issue = 1-2 weeks
   3 pt issue   = 2 weeks
   5 pt issue   = 3 weeks
   8 pt issue   = 5-6 weeks
```

### Current Answers:

| Project Type | Can We Take It? | Who? | Notes |
|---|---|---|---|
| Large dev/data project | YES | davis | 16 slots available |
| Small-medium dev project | YES | luthfi | 3 slots, must finish RCG/SB first |
| Design-only project | YES (small) | tiara.almira | 2 slots available |
| Design + dev project | MAYBE | tiara + davis/luthfi | If dev scope fits capacity |
| Any project needing sean | NO | - | At capacity with XCL + ANI6 |
| Any project needing elfajri | NO | - | Over capacity, must offload first |
| Strategy/ops-heavy project | NO | - | daz at 5x capacity |

---

## TEAM THROUGHPUT BASELINE

| Person | Avg Issues/Month | Capability | Best Used For |
|---|---|---|---|
| davis | 17 | Dev/Data | Data engineering, backend development |
| elfajri | 13 | Dev | Frontend/fullstack (when not overloaded) |
| sean | 8 | Dev/Design | Design + Webflow development |
| luthfi | 7 | Dev | Frontend development |
| daz | 7 | Strategy/Ops | Project management, ops (when focused) |
| tiara.almira | 5 | Design/Dev | UI/UX design, some development |
| haykal | 4 | Dev/AI | AI workflows, SEO content |
| shafiq | 2 | Dev | Development (low throughput) |
| **TOTAL** | **~63** | | |

**Total agency capacity ceiling: ~60-70 issues/month.** New projects must fit within this.

---

## ESTIMATION REFERENCE

When scoping new projects for clients, use these calibrated timelines:

| Story Points | Expected Duration | Confidence |
|---|---|---|
| 1 point | 1 week | Medium |
| 2 points | 1.5 weeks | Medium |
| 3 points | 2 weeks | Medium |
| 5 points | 3 weeks | Medium |
| 8 points | 5-6 weeks | Low |

**Most reliable estimators:** davis and tiara.almira (4.0 days/point). Use their estimates as the benchmark.

**Estimation adjustment factors:**
- If assignee is elfajri or daz: multiply expected duration by 1.5x (overloaded)
- If the project has 3+ concurrent resources: add 20% for coordination overhead
- If the issue requires client review: add 1-2 weeks for review cycle

---

## ACTIVE PROJECT COMMITMENTS

| Project | Status | Key People | End Date | Risk |
|---|---|---|---|---|
| ANI6-Beta-AST | 56% done | sean, davis, elfajri, tiara | TBD (wrong date in system) | Medium |
| XCL-Beta-WebflowMigration | 65% done | sean | TBD (wrong date in system) | Medium |
| CT-Beta-P_RMD-Q3 | 82% done | rohan | Wrapping up | Low |
| RCG-Epsilon-P_SPL | 67% done | elfajri, luthfi, haykal, tiara | TBD | HIGH (off track) |
| HPL-BETA-RMD-2026 | 19% done | tiara (design), TBD (dev) | TBD | Medium (needs dev assignment) |
| UTV-Beta-P_RMD-2026 | Active | elfajri | TBD | Medium |
| SB-StudioScents | 50% done | luthfi | Wrapping up | Low |

**Projects wrapping up soon (freeing capacity):**
- ORG-Gamma (89% done) -> davis freed up
- CT-Beta (82% done) -> rohan freed up
- SB-StudioScents (50% but small) -> luthfi partially freed

---

## HOW TO UPDATE THIS DASHBOARD

Every Monday:
1. Export current Linear data or check each person's active issue count
2. Update the "Active / Capacity" column for each person
3. Update the project status table
4. Review: has anyone crossed from "Available" to "Full" or vice versa?
5. Share with commercial team before any new project discussions

---

*This dashboard should be reviewed before every new project commitment.*
