# Codex work rules for dropkit.contents

This repository is a public contents hub. The `agent-harness/` directory is a
local, opt-in control plane for persona jobs; it does not contain credentials
or live ERP/QMS connectors.

When Codex starts work in this repository:

1. Run `python agent-harness/harness.py doctor` before using the queue.
2. Use `python agent-harness/harness.py session-start --agent codex` to record
   the session attachment.
3. Keep jobs in `draft_only` mode until the user explicitly authorizes a live
   connector or email sender.
4. Treat UI extraction as read-only. Do not approve, delete, post, or send from
   a screen session without an explicit task and a human approval gate.
5. Never add secrets, cookies, screenshots containing business data, or local
   runtime state to git.

The harness is deliberately cross-platform: use `scripts/codex-start.sh` on
macOS and `scripts/codex-start.ps1` on Windows/LG Gram.
