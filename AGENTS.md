# Codex work rules for dropkit.contents

This repository is the public publication and document-content hub. It contains
Astro publication infrastructure, research notes, project introductions, and
social/media copies. The executable local-model engine and UI-to-document
harness live in the separate [`local-llm`](https://github.com/Hskim-droid/local-llm)
repository.

When Codex starts work here:

1. Keep edits within the site, public writing, content ledger, or publication
   configuration unless the user explicitly asks for a repository-level change.
2. Run `npm ci`, `npm run build`, and `git diff --check` for site or content
   changes.
3. Keep examples synthetic. Never add credentials, cookies, screenshots with
   business data, ERP/QMS records, mail addresses, or local runtime state.
4. Do not add executable ERP/QMS connectors, mail senders, unattended writes, or
   cloud model fallbacks to this content repository.
5. For harness or local-model changes, work in
   [`local-llm`](https://github.com/Hskim-droid/local-llm) and run its own Go and
   Python checks there.
