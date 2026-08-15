#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

HUGO_BIN="${HUGO_BIN:-hugo}"

# Keep this intentionally small and Hugo-standard: verify the theme metadata and
# strict-build the bundled example site. Deeper content/style checks should live
# in review, not in the default theme CI path.
test -f theme.toml
test -f README.md
test -d exampleSite

"$HUGO_BIN" version
"$HUGO_BIN" \
  --source exampleSite \
  --gc \
  --minify \
  --panicOnWarning \
  --noBuildLock
