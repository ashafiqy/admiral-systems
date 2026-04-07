---
title: "Migration Plan: GitHub to Google Drive"
created: 2026-04-06
updated: 2026-04-06
tags:
  - type/decision
  - operations/architecture
status: active
---

# Migration Plan: GitHub to Google Drive

## Decision

Migrate the admiral-systems vault from GitHub (Git repo) to Google Drive (shared folder with local sync). The team uses Google Workspace — Drive removes the Git friction and gives everyone instant access via browser or Obsidian.

## How It Works

```
Google Drive Cloud (Admiral Systems Vault/)
        |
        | Google Drive for Desktop (auto-sync)
        |
   Local folder (e.g. G:\My Drive\Admiral Systems Vault\)
        |
        |--- Obsidian reads/writes .md files
        |--- Claude Code reads/writes .md files
        |--- Team browses via Drive web UI
```

## Migration Steps

### Phase 1: Set Up Google Drive
- [ ] Create `Admiral Systems Vault/` in Google Drive
- [ ] Share with team (Edit: seniors/partners, View: juniors)
- [ ] Ensure Google Drive for Desktop is installed and syncing
- [ ] Copy all vault files from Git repo to Drive (exclude `.git/`, `.obsidian/`)

### Phase 2: Point Obsidian
- [ ] Open the Drive local folder as an Obsidian vault
- [ ] Transfer Obsidian settings (plugins, hotkeys, appearance)
- [ ] Verify `[[wikilinks]]` and frontmatter parsing work

### Phase 3: Update Claude Code
- [ ] Open Claude Code sessions from the Drive local folder
- [ ] Delete `/commit` and `/vault-sync` skills (replaced by Drive auto-sync)
- [ ] Create `/changelog` skill (appends entries to HISTORY.md)
- [ ] Update `.claude/settings.local.json` (remove git permissions)
- [ ] Review bot skills for git references

### Phase 4: Update Vault Docs
- [ ] Update `CLAUDE.md` — remove Git refs, add Drive workflow, conflict handling
- [ ] Update `HISTORY.md` — add migration entry
- [ ] Update `remote-claude-architecture.md` — Drive replaces GitHub
- [ ] Update `admiral-systems-ecosystem-prd.md` — architecture, data flows
- [ ] Update `admiral-systems-ecosystem-diagram.html` — Vault node
- [ ] Review agent playbooks for git references

### Phase 5: Handle Sharkie Submodule
- [ ] Remove submodule from sharkie repo
- [ ] Create symlink or update sharkie CLAUDE.md to reference Drive path

### Phase 6: Team Onboarding
- [ ] Share Drive folder with all team members
- [ ] Create brief Obsidian setup guide
- [ ] Post Slack announcement

### Phase 7: Archive Git Repo
- [ ] Final commit with "Migrated to Google Drive" README
- [ ] Archive repo on GitHub

## What Changes

| Area | Git (old) | Google Drive (new) |
|------|-----------|-------------------|
| Sync | Manual (/commit, /vault-sync) | Automatic (Drive for Desktop) |
| Version history | Git log + diffs | Drive file versioning + HISTORY.md |
| Team access | Need Git + GitHub | Drive web UI or local sync |
| Obsidian vault | Points to git repo folder | Points to Drive local folder |
| Claude Code | Same — local files | Same — local files |
| Change log | Git commits | HISTORY.md via /changelog |

## Risks

| Risk | Mitigation |
|------|------------|
| Conflict copies from simultaneous edits | Announce large edits in Slack. Resolve conflicts immediately. |
| Accidental file deletion | Drive has trash + 30-day recovery |
| .obsidian/ sync conflicts | Each user's .obsidian/ is local; ignore in Drive if needed |
| WSL2 bot can't access Drive | Mount via symlink or manual sync script |
