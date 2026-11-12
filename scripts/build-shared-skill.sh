#!/usr/bin/env bash
# Build the shareable "seo-wiki" skill zip from the current wiki.
#
#   ./scripts/build-shared-skill.sh
#
# Output: dist/seo-wiki.zip — upload it on claude.ai to update the shared
# skill (see README, "Sharing the wiki as a skill"). Only wiki pages go in:
# raw/, drafts/, research-digests/, wiki/log.md and CLAUDE.md stay out.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WIKI="$ROOT/wiki"
TEMPLATE="$ROOT/share/seo-wiki/SKILL.md"
DIST="$ROOT/dist"
OUT="$DIST/seo-wiki"
REF="$OUT/references"

[ -f "$TEMPLATE" ] || { echo "Missing $TEMPLATE" >&2; exit 1; }

rm -rf "$OUT" "$DIST/seo-wiki.zip"
mkdir -p "$REF/index"

# Page folders and the timeline, without Obsidian/macOS clutter. The
# `origin: raw/...` frontmatter line is dropped because raw/ isn't shipped;
# source URLs stay in each page's Citation line.
#
# claude.ai caps a skill zip at 200 files, so concept and playbook pages
# ship one file each, but the 200+ source pages are bundled into one file
# per first letter (sources/a.md, sources/b.md, ...). Each bundled page
# starts with a `<!-- page: slug -->` marker line.
for d in concepts playbooks; do
  mkdir -p "$REF/$d"
  for f in "$WIKI/$d"/*.md; do
    grep -v '^origin: raw/' "$f" > "$REF/$d/$(basename "$f")"
  done
done
mkdir -p "$REF/sources"
for f in "$WIKI/sources"/*.md; do
  slug=$(basename "$f" .md)
  letter=$(printf '%s' "$slug" | cut -c1 | tr 'A-Z' 'a-z')
  bundle="$REF/sources/$letter.md"
  [ -f "$bundle" ] || printf '# Source pages: %s\n\nEach page starts with a `<!-- page: slug -->` line.\n' "$letter" > "$bundle"
  { printf '\n<!-- page: %s -->\n\n' "$slug"; grep -v '^origin: raw/' "$f"; } >> "$bundle"
done
cp "$WIKI/timeline.md" "$REF/timeline.md"

page_title() {  # first H1 of a page, else the slug in title case
  t=$(awk '/^# / { sub(/^# +/, ""); print; exit }' "$1")
  [ -n "$t" ] || t=$(basename "$1" .md | tr '-' ' ' | awk '{ for (i = 1; i <= NF; i++) $i = toupper(substr($i, 1, 1)) substr($i, 2); print }')
  printf '%s' "$t"
}

# One line per page: slug, file and title, so a [[slug]] resolves with one
# grep. Bundled source pages show their bundle file.
{
  echo "# Page map"
  echo
  echo "One line per page: \`slug | file | title\`. Print any page with"
  echo "\`bash scripts/page.sh slug\`."
  echo
  for d in concepts playbooks; do
    for f in "$WIKI/$d"/*.md; do
      slug=$(basename "$f" .md)
      echo "$slug | $d/$slug.md | $(page_title "$f")"
    done
  done
  for f in "$WIKI/sources"/*.md; do
    slug=$(basename "$f" .md)
    letter=$(printf '%s' "$slug" | cut -c1 | tr 'A-Z' 'a-z')
    echo "$slug | sources/$letter.md | $(page_title "$f")"
  done
} > "$REF/page-map.md"

# Split index.md into one catalog per section so the skill can read the
# short concept/playbook catalogs whole and grep the long sources one.
awk -v dir="$REF/index" '
  /^## Concepts/  { out = dir "/concepts.md" }
  /^## Playbooks/ { out = dir "/playbooks.md" }
  /^## Sources/   { out = dir "/sources.md" }
  out { print > out }
' "$WIKI/index.md"
for s in concepts playbooks sources; do
  [ -s "$REF/index/$s.md" ] || { echo "index.md has no '$s' section (expected ## Concepts / ## Playbooks / ## Sources)" >&2; exit 1; }
done

# Stamp the build date, commit and page counts into SKILL.md.
n_c=$(ls "$REF/concepts" | wc -l | tr -d ' ')
n_p=$(ls "$REF/playbooks" | wc -l | tr -d ' ')
n_s=$(ls "$WIKI/sources"/*.md | wc -l | tr -d ' ')
commit=$(git -C "$ROOT" rev-parse --short HEAD 2>/dev/null || echo unknown)
dirty=""
if [ -n "$(git -C "$ROOT" status --porcelain -- wiki 2>/dev/null)" ]; then
  dirty=" (includes uncommitted wiki edits)"
fi
info="**Snapshot built $(date +%Y-%m-%d)** (wiki version $commit): $n_c concept pages, $n_p playbooks, $n_s source pages."
awk -v info="$info" '{ if ($0 == "{{BUILD_INFO}}") print info; else print }' "$TEMPLATE" > "$OUT/SKILL.md"
mkdir -p "$OUT/scripts"
cp "$ROOT/share/seo-wiki/scripts/page.sh" "$OUT/scripts/page.sh"

# claude.ai rejects descriptions over 1024 characters or containing < or >.
desc=$(awk '/^description:/ { sub(/^description: */, ""); print; exit }' "$OUT/SKILL.md")
if [ "${#desc}" -gt 1024 ]; then
  echo "SKILL.md description is ${#desc} characters; the limit is 1024." >&2; exit 1
fi
case "$desc" in *'<'*|*'>'*) echo "SKILL.md description must not contain < or >." >&2; exit 1;; esac

# -D leaves out directory entries; claude.ai counts every entry toward its
# 200-file limit.
(cd "$DIST" && zip -rqXD seo-wiki.zip seo-wiki -x '*.DS_Store')
n_files=$(zipinfo -1 "$DIST/seo-wiki.zip" | wc -l | tr -d ' ')
if [ "$n_files" -gt 200 ]; then
  echo "Zip has $n_files files; claude.ai allows at most 200. Bundle more pages." >&2
  exit 1
fi

size=$(du -h "$DIST/seo-wiki.zip" | cut -f1 | tr -d ' ')
echo "Built dist/seo-wiki.zip ($size, $n_files of 200 files): $n_c concepts, $n_p playbooks, $n_s sources, commit $commit$dirty."
echo "Next: upload it on claude.ai to update the shared seo-wiki skill."
