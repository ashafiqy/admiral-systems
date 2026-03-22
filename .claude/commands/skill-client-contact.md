<!-- bot-skill
name: client-contact
description: Contact info and team lookup for a client
type: query
tools: Read,Glob,Grep
-->

Find the client matching "$ARGS" in `clients/`. Read project briefs, meeting notes, and contact information to find client contacts (names, emails, phones) and internal team members assigned with their roles. If no client matches "$ARGS", list available client folders. Keep concise for chat.