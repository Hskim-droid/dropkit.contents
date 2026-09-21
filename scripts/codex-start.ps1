$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Root

python agent-harness/harness.py init
python agent-harness/harness.py doctor
python agent-harness/harness.py session-start --agent codex
