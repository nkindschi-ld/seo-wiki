#!/usr/bin/env bash
# Print one wiki page by its [[slug]]: bash scripts/page.sh <slug>
# Concept and playbook pages are single files; source pages live inside
# per-letter bundles (references/sources/a.md, ...) after a
# `<!-- page: slug -->` marker line.
set -eu
slug="${1:?usage: page.sh <slug>}"
REF="$(cd "$(dirname "$0")/../references" && pwd)"

for d in concepts playbooks; do
  if [ -f "$REF/$d/$slug.md" ]; then cat "$REF/$d/$slug.md"; exit 0; fi
done

letter=$(printf '%s' "$slug" | cut -c1 | tr 'A-Z' 'a-z')
bundle="$REF/sources/$letter.md"
if [ -f "$bundle" ] && grep -qx "<!-- page: $slug -->" "$bundle"; then
  awk -v m="<!-- page: $slug -->" '
    $0 == m { on = 1; next }
    on && /^<!-- page: / { exit }
    on { print }
  ' "$bundle"
  exit 0
fi

echo "No page named '$slug'. Search references/page-map.md for a close match." >&2
exit 1
