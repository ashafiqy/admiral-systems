---
title: "Playbook: Bulk Priority Sync"
created: 2026-03-10
updated: 2026-03-21
tags:
  - operations/playbook
  - delivery/linear
status: active
---

# Bulk Priority Sync Playbook

Sync the p0–p3 Linear labels to the native Linear Priority field so issues are sortable in all Linear views. Labels are NOT removed — both coexist.

Read [[priority-mapping]] first for context on the label system and rules.

---

## When to Run This

- After a batch of issues is created or imported without the Priority field set
- After any audit shows Priority field drift from labels
- Periodically (e.g., monthly) as a workspace health check

---

## Step-by-Step

### 1. Fetch issues by label

Run one query per label. Each returns a list of issue IDs.

```
list_issues(labelName: "p0-critical")   → collect all issue IDs
list_issues(labelName: "p1-high")       → collect all issue IDs
list_issues(labelName: "p2-medium")     → collect all issue IDs
list_issues(labelName: "p3-low")        → collect all issue IDs
```

> Results may be paginated. Continue fetching until all pages are exhausted.

---

### 2. Update Priority field for each bucket

Use `save_issue` for each issue ID. Run calls in parallel for speed.

**p0-critical → Urgent (priority: 1)**
```
save_issue(id: "<issue-id>", priority: 1)
```

**p1-high → High (priority: 2)**
```
save_issue(id: "<issue-id>", priority: 2)
```

**p2-medium → Normal (priority: 3)**
```
save_issue(id: "<issue-id>", priority: 3)
```

**p3-low → Low (priority: 4)**
```
save_issue(id: "<issue-id>", priority: 4)
```

Priority integer reference:
| Integer | Linear Label |
|---|---|
| `1` | Urgent |
| `2` | High |
| `3` | Normal |
| `4` | Low |

---

### 3. Handle errors

- **`Entity not found: Issue`** — issue belongs to an archived team. Skip it and continue. Do not retry.
- **Cancelled tool calls** — if one parallel call fails, subsequent calls in the same batch may be cancelled. Re-run the full batch excluding the failed ID.
- **Timeout or rate limit** — wait briefly, then retry the remaining IDs.

---

### 4. Verify

After the sync, spot-check a sample:

```
get_issue(id: "<issue-id>")   → confirm `priority` field matches expected value
```

Also run:
```
list_issues(labelName: "p0-critical")
```
and confirm all returned issues have `priority: 1` in the response.

---

## What NOT to Do

- Do **not** remove labels after syncing. Labels stay on the issue permanently.
- Do **not** set priority on issues that have no p0–p3 label. Leave those untouched.
- Do **not** use the legacy `critical` label (without `p0-` prefix) as a mapping source.
- Do **not** treat `p0-critical` as equivalent to Linear's default "No priority" — they are opposites.

---

## Example Full Run (pseudocode)

```
# Fetch
p0_ids = list_issues(labelName: "p0-critical").issues.map(i => i.id)
p1_ids = list_issues(labelName: "p1-high").issues.map(i => i.id)
p2_ids = list_issues(labelName: "p2-medium").issues.map(i => i.id)
p3_ids = list_issues(labelName: "p3-low").issues.map(i => i.id)

# Sync (parallel per bucket)
for id in p0_ids: save_issue(id, priority: 1)
for id in p1_ids: save_issue(id, priority: 2)
for id in p2_ids: save_issue(id, priority: 3)
for id in p3_ids: save_issue(id, priority: 4)
```
