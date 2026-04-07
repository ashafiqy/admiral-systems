Append a changelog entry to the vault HISTORY.md.

1. Read `HISTORY.md` to find the current date section
2. If today's date section already exists, append the new entry below existing entries for that date
3. If today's date doesn't exist, create a new `## YYYY-MM-DD` section at the top (below the frontmatter and heading)
4. Write a concise entry describing what was changed and why (1-2 lines per item)
5. If the user provides `$ARGUMENTS`, use them as the changelog entry text
6. If no arguments provided, ask the user what changed
7. Include the source if applicable (e.g. "Source: Granola meeting notes")
8. Report: what was added to the changelog
