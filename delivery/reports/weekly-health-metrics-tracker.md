---
title: "Weekly Health Metrics Tracker"
created: 2026-03-10
updated: 2026-03-21
tags:
  - delivery/metrics
  - type/report
status: active
---

# Weekly Health Metrics Tracker
## Admiral Systems — Linear Workspace

**Instructions:** Update this tracker every Monday. Compare against targets. Flag any metric that moves in the wrong direction for 2+ consecutive weeks.

---

## Baseline (March 8, 2026)

| # | Metric | Baseline | 30-Day Target | 90-Day Target |
|---|---|---|---|---|
| 1 | Total overdue issues | 233 (24.8%) | <100 (<11%) | <30 (<5%) |
| 2 | Avg active issues per person | 12.2 | <9 | <7 |
| 3 | Max active issues (any person) | 36 (daz) | <15 | <10 |
| 4 | daz active issues | 36 | <10 | <7 |
| 5 | Estimation coverage (client work) | 48% | >70% | >90% |
| 6 | Work type field coverage | 6.5% | >50% | >90% |
| 7 | Issues in cycles/sprints | 46.6% | >70% | >90% |
| 8 | Avg time in "In Review" | 59 days | <20 days | <5 days |
| 9 | Avg time in "In Progress" | 50 days | <25 days | <14 days |
| 10 | Sprint completion rate | 20% | >60% | >80% |
| 11 | Priority: % Urgent+High | 56.1% | <40% | <30% |
| 12 | Items stuck in Triage | 34 | <10 | 0 |
| 13 | Unassigned active issues | 6 | 0 | 0 |

---

## Weekly Tracking

### Week 1 (Mar 9-15) — Phase 1: Emergency Triage

| # | Metric | Value | Trend | Notes |
|---|---|---|---|---|
| 1 | Overdue issues | | | |
| 2 | Avg active/person | | | |
| 3 | Max active (person) | | | |
| 4 | daz active issues | | | |
| 5 | Estimation % | | | |
| 6 | Work type % | | | |
| 7 | Issues in sprints % | | | |
| 10 | Sprint completion % | | | |
| 11 | % Urgent+High | | | |
| 12 | Triage queue | | | |
| 13 | Unassigned active | | | |

**Phase 1 checklist:**
- [ ] daz triage complete?
- [ ] Overdue bulk triage complete?
- [ ] Archived HPL closed?

---

### Week 2 (Mar 16-22) — Phase 2 Start

| # | Metric | Value | Trend | Notes |
|---|---|---|---|---|
| 1 | Overdue issues | | | |
| 2 | Avg active/person | | | |
| 3 | Max active (person) | | | |
| 4 | daz active issues | | | |
| 5 | Estimation % | | | |
| 6 | Work type % | | | |
| 7 | Issues in sprints % | | | |
| 10 | Sprint completion % | | | |
| 11 | % Urgent+High | | | |
| 12 | Triage queue | | | |
| 13 | Unassigned active | | | |

**Phase 2 checklist:**
- [ ] Throughput baselines shared with team?
- [ ] Estimation policy communicated?
- [ ] Work Type field created in Linear?

---

### Week 3 (Mar 23-29) — Phase 2/3

| # | Metric | Value | Trend | Notes |
|---|---|---|---|---|
| 1 | Overdue issues | | | |
| 2 | Avg active/person | | | |
| 3 | Max active (person) | | | |
| 4 | daz active issues | | | |
| 5 | Estimation % | | | |
| 6 | Work type % | | | |
| 7 | Issues in sprints % | | | |
| 10 | Sprint completion % | | | |
| 11 | % Urgent+High | | | |
| 12 | Triage queue | | | |
| 13 | Unassigned active | | | |

**Phase 2/3 checklist:**
- [ ] "No Ticket, No Work" policy live?
- [ ] Slack -> Linear shortcut set up?
- [ ] Sprint capacity limits defined?

---

### Week 4 (Mar 30 - Apr 5) — Phase 3/4

| # | Metric | Value | Trend | Notes |
|---|---|---|---|---|
| 1 | Overdue issues | | | |
| 2 | Avg active/person | | | |
| 3 | Max active (person) | | | |
| 4 | daz active issues | | | |
| 5 | Estimation % | | | |
| 6 | Work type % | | | |
| 7 | Issues in sprints % | | | |
| 10 | Sprint completion % | | | |
| 11 | % Urgent+High | | | |
| 12 | Triage queue | | | |
| 13 | Unassigned active | | | |

**Phase 3/4 checklist:**
- [ ] Capacity Dashboard live and shared with commercial?
- [ ] Priority re-triage complete?
- [ ] Label consolidation started?

---

## Per-Person Active Issue Tracking

Track each person's active issue count (In Progress + In Review) weekly:

| Person | Capacity | Baseline | Wk 1 | Wk 2 | Wk 3 | Wk 4 | Status |
|---|---|---|---|---|---|---|---|
| daz | 7 | 36 | | | | | CRITICAL |
| elfajri | 13 | 21 | | | | | OVER |
| haykal | 4 | 21 | | | | | OVER |
| sean | 8 | 8 | | | | | FULL |
| prj-website-rev | - | 8 | | | | | (external) |
| luthfi | 7 | 4 | | | | | OK |
| rohan | - | 3 | | | | | OK |
| tiara.almira | 5 | 3 | | | | | OK |
| shafiq | 2 | 2 | | | | | FULL |
| davis | 17 | 1 | | | | | AVAILABLE |

**Status key:**
- AVAILABLE = Active < 50% of capacity
- OK = Active < 80% of capacity
- FULL = Active >= 80% of capacity
- OVER = Active > capacity
- CRITICAL = Active > 2x capacity

---

## Monthly Capacity Review (for Commercial Team)

**Schedule:** First Monday of each month
**Attendees:** Delivery Lead + Commercial Team
**Duration:** 30 minutes

### Agenda Template

1. **Review metrics trend** (5 min)
   - Are we improving week over week?
   - Any metrics moving in the wrong direction?

2. **Current capacity snapshot** (10 min)
   - Who is available? Who is overloaded?
   - What projects are wrapping up (freeing capacity)?
   - What projects are ramping up (consuming capacity)?

3. **Pipeline discussion** (10 min)
   - What new projects are in the pipeline?
   - What capability do they need (Design/Dev/Data)?
   - Do we have the right people available?

4. **Decisions** (5 min)
   - Can we take on [project X]? YES/NO/CONDITIONAL
   - Do we need to hire/contract for any capability gap?
   - Are there projects we should pause to free capacity?

### Decision Record

| Date | Project | Decision | Rationale | Assigned To |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

---

## How to Collect Metrics

### Quick method (5 minutes):
1. Open Linear -> Issues view
2. Filter: Status = "In Progress" OR "In Review" -> count per assignee (metrics 2, 3, 4, 13)
3. Filter: Due Date < today AND Status != Done/Canceled -> count (metric 1)
4. Filter: Status = "Triage" -> count (metric 12)
5. Check current sprint completion in Cycles view (metric 10)

### For estimation/label coverage:
1. Export current issues to CSV
2. Count issues with Estimate field populated / total active issues (metric 5)
3. Count issues with Work Type / total active issues (metric 6)
4. Count issues in a Cycle / total active issues (metric 7)

### For priority distribution:
1. Filter all open issues
2. Group by Priority
3. Calculate Urgent + High as % of total (metric 11)

---

*Keep this tracker updated weekly. It takes <15 minutes to collect all metrics from Linear. The investment pays for itself in avoided overcommitment and missed deadlines.*
