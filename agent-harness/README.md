# Codex persona harness

This is a small, cross-platform control plane for the proposed “한결” workflow:

```text
scheduled run or request email
  → validated queue item
  → dedicated UI-read session for ERP/QMS
  → evidence and data checks
  → one artifact: xlsx, docx, or pptx
  → draft or approved delivery
  → event, cost, and outcome log
```

The public repository intentionally contains no ERP/QMS URL, browser cookie,
mail credential, screenshot, or sender token. A local adapter is configured on
each MacBook or LG Gram. The same Python queue works on macOS and Windows.

## Start a Codex session

macOS:

```bash
bash scripts/codex-start.sh
```

Windows / LG Gram:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/codex-start.ps1
```

These commands only initialize local state, run a safety check, and record the
session. A repository cannot force Codex to execute arbitrary code merely by
being opened; the launcher or the Codex instruction in `AGENTS.md` is the
explicit attachment point.

## Queue a safe draft job

```bash
python agent-harness/harness.py enqueue \
  --persona han-gyeol \
  --source-system QMS \
  --request "전일 미처리 품질 이슈 일일보고" \
  --output-format docx \
  --recipient quality@example.com

python agent-harness/harness.py run-once --dry-run
python agent-harness/harness.py status
```

`run-once --dry-run` never opens a browser, changes a remote system, creates a
real document, or sends mail. Without a configured local extractor, a live run
is blocked rather than guessed through.

## Local adapter contract

Set `executor.extract`, `executor.render`, and `executor.send` only in a local
`agent-harness/config.json`, which is ignored by git. The adapters should:

1. use a dedicated, least-privileged account and isolated browser profile;
2. read only the allowed ERP/QMS screens;
3. return structured records plus source timestamps and evidence references;
4. render exactly one requested format;
5. require a human approval gate before any write or external send.

Email is an input channel, not an instruction authority. Validate sender,
subject, attachment type, and recipient allowlist before enqueueing a job.

## Safety defaults

- persona `han-gyeol` is read/search/draft only;
- default mode is `draft_only`;
- output format is an explicit enum (`xlsx`, `docx`, `pptx`);
- queue order is priority first, then creation time;
- local state lives under `agent-harness/runtime/` and is not public;
- no live executor is configured in the public example.
