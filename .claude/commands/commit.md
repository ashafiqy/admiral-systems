Commit and push all pending changes in the admiral-systems vault.

**Important: Run all git commands directly (e.g. `git status`, `git add ...`). Never prefix with `cd <path> &&` — this triggers an unbypassable security prompt in Claude Code. The working directory is already the vault root.**

1. Run `git status` to see what's changed (staged, unstaged, untracked)
2. If there are no changes, tell the user and stop
3. Stage all changed and new files: `git add` each file individually (not `git add .` or `git add -A`, to avoid accidentally staging sensitive files like .env)
4. Run `git diff --cached` to read the staged changes
5. Generate a concise commit message (1-2 sentences focused on the "why", not just listing files). Match the style of recent commits in `git log --oneline -5`.
6. Commit with the message, appending this trailer on a separate line after a blank line:
   `Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>`
7. Run `git push`. If the push hangs or fails, tell the user to run `! git push` manually.
8. Report: what was committed, the commit message, and whether the push succeeded.
