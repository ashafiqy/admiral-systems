Pull the latest vault changes from the remote admiral-systems repo.

**Important: Run all git commands directly (e.g. `git pull`). Never prefix with `cd <path> &&` — this triggers an unbypassable security prompt in Claude Code. The working directory is already the vault root.**

1. Run `git status` to check for any uncommitted local changes
2. If there are uncommitted changes, warn the user and ask whether to stash them first or abort
3. Run `git pull --ff-only` to pull the latest changes
4. If the pull fails due to diverged branches, tell the user and suggest `! git pull --rebase`
5. Run `git log --oneline -5` to show what was pulled
6. Report: whether the pull succeeded, how many new commits were pulled, and a brief summary of what changed
