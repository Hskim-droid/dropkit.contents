#!/bin/bash
# Import a content-hub export into private staging, outside this public checkout.
# Usage: bash scripts/import-from-hub.sh <slug> [source_md]
#   slug: hw_fit | refinery-YYYY-MM-DD | custom
#   source_md: optional path; default by slug
set -euo pipefail

SITE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HUB="${CT_CONTENT_HUB:?set CT_CONTENT_HUB to the factory tree}"
STAGING="${CT_PRIVATE_STAGING:?set CT_PRIVATE_STAGING to an absolute private directory outside this checkout}"
SLUG="${1:?slug required (e.g. hw_fit)}"
SRC="${2:-}"

case "$SLUG" in
  hw_fit) SRC="${SRC:-$HUB/out/hw_fit/latest.md}" ;;
  refinery|refinery-latest) SRC="${SRC:-$HUB/out/refinery/latest.md}"; SLUG="refinery-$(date +%Y-%m-%d)" ;;
  *)
    if [[ -z "$SRC" ]]; then
      echo "custom slug needs source path: $0 $SLUG /path/to/file.md" >&2
      exit 2
    fi
    ;;
esac

if [[ ! "$SLUG" =~ ^[a-z0-9][a-z0-9_-]*$ ]]; then
  echo "invalid slug: use lowercase letters, digits, underscores or hyphens" >&2
  exit 2
fi

if [[ ! -f "$SRC" ]]; then
  echo "missing source: $SRC" >&2
  exit 1
fi

python3 - "$SRC" "$STAGING" "$SLUG" "$SITE_ROOT" <<'PY'
import datetime
import json
import os
import sys
from pathlib import Path

source, staging, slug, site = sys.argv[1:]
folder = Path(staging)
if not folder.is_absolute():
    raise SystemExit('Private staging must be an absolute path')
folder = folder.resolve()
site = Path(site).resolve()
if folder == site or site in folder.parents:
    raise SystemExit('Private staging cannot be inside the public checkout')
folder.mkdir(parents=True, exist_ok=True, mode=0o700)
if folder.stat().st_mode & 0o077:
    raise SystemExit('Private staging must restrict access to its owner (mode 700)')
target = folder / (slug + '.md')
lines = Path(source).read_text(encoding="utf-8").splitlines()
title = slug
for i, line in enumerate(lines):
    if line.startswith("# "):
        title = line[2:]
        del lines[i]
        break
description = next((line[:160] for line in lines if any(
    word in line for word in ("공통 HW축", "정제된 신호", "결정표")
)), "Imported from content-hub")
# JSON strings are valid YAML quoted scalars, including colons and quotes.
header = ["---", "title: " + json.dumps(title, ensure_ascii=False),
          "description: " + json.dumps(description, ensure_ascii=False),
          "pubDate: " + datetime.date.today().isoformat(),
          "draft: true", "approved: false", "tags: [local-llm, hardware]", "---", ""]
# Exclusive creation preserves existing posts, including during concurrent imports.
fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
with os.fdopen(fd, "w", encoding="utf-8") as output:
    output.write("\n".join(header + lines) + "\n")
print('Private draft created: ' + str(target))
PY

echo "Review in private staging. Only approved, non-draft notes may be copied into the public checkout."
