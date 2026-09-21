#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

python3 agent-harness/harness.py init
python3 agent-harness/harness.py doctor
python3 agent-harness/harness.py session-start --agent codex
