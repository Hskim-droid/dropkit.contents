#!/bin/bash
# Import a content-hub export into dropkit.contents posts.
# Usage: bash scripts/import-from-hub.sh <slug> [source_md]
#   slug: hw_fit | refinery-YYYY-MM-DD | custom
#   source_md: optional path; default by slug
set -euo pipefail

SITE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HUB="${CT_CONTENT_HUB:?set CT_CONTENT_HUB to the factory tree}"
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

OUT="$SITE_ROOT/src/content/posts/${SLUG}.md"
python3 - "$SRC" "$OUT" "$SLUG" <<'PY'
import datetime
import json
import sys
from pathlib import Path

source, target, slug = sys.argv[1:]
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
          "draft: true", "tags: [local-llm, hardware]", "---", ""]
# Exclusive creation preserves existing posts, including during concurrent imports.
with Path(target).open("x", encoding="utf-8") as output:
    output.write("\n".join(header + lines) + "\n")
PY

BYTES=$(wc -c < "$OUT" | tr -d ' ')
echo "imported $SRC → $OUT ($BYTES bytes)"
echo "Draft only. Review the source and frontmatter before setting draft: false."
