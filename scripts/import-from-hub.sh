#!/bin/bash
# Import a content-hub export into dropkit.contents posts.
# Usage: bash scripts/import-from-hub.sh <slug> [source_md]
#   slug: hw_fit | refinery-YYYY-MM-DD | custom
#   source_md: optional path; default by slug
set -euo pipefail

SITE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HUB="${CT_CONTENT_HUB:-/Users/claire/content-hub}"
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

if [[ ! -f "$SRC" ]]; then
  echo "missing source: $SRC" >&2
  exit 1
fi

OUT="$SITE_ROOT/src/content/posts/${SLUG}.md"
TITLE=$(grep -m1 '^# ' "$SRC" | sed 's/^# //' || echo "$SLUG")
DATE=$(date +%Y-%m-%d)
DESC=$(grep -m1 '공통 HW축\|정제된 신호\|결정표' "$SRC" | head -c 160 | tr '\n' ' ' || true)

{
  echo '---'
  echo "title: $(printf '%s' "$TITLE" | sed 's/"/\\"/g')"
  echo "description: \"${DESC:-Imported from content-hub}\""
  echo "pubDate: ${DATE}"
  echo "draft: false"
  echo "tags: [local-llm, hardware]"
  echo '---'
  echo
  # drop duplicate H1 if present (layout already shows title)
  awk 'BEGIN{skip=0} /^# / && skip==0 {skip=1; next} {print}' "$SRC"
} > "$OUT"

BYTES=$(wc -c < "$OUT" | tr -d ' ')
echo "imported $SRC → $OUT ($BYTES bytes)"
echo "imported $SRC → $OUT ($BYTES bytes). Prefer factory ship-to-dropkit.sh on health-ok runs."
