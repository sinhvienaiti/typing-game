#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
URL="https://typing-game.local"

for path in \
  "$ROOT_DIR/portal/dist/index.html" \
  "$ROOT_DIR/games/vocab-shooter/dist/index.html" \
  "$ROOT_DIR/games/recall-typing/dist/index.html" \
  "$ROOT_DIR/games/karaoke-typing/dist/index.html" \
  "$ROOT_DIR/games/space-typing/dist/index.html" \
  "$ROOT_DIR/games/monkeytype/frontend/dist/index.html"
do
  if [[ ! -f "$path" ]]; then
    echo "Static build is missing: $path"
    echo "Run: pnpm build:local"
    exit 1
  fi
done

# New games are checked only once they are checked out.
for path in \
  "$ROOT_DIR/games/dragon-hold/dist/index.html" \
  "$ROOT_DIR/games/typing-defense/dist/index.html" \
  "$ROOT_DIR/games/typing-survival/dist/index.html" \
  "$ROOT_DIR/games/immortality-cultivation/dist/index.html"
do
  [[ -f "${path%/dist/index.html}/package.json" ]] || continue
  if [[ ! -f "$path" ]]; then
    echo "Static build is missing: $path"
    echo "Run: pnpm build:local"
    exit 1
  fi
done

# Typing Feel keyboard sounds (feel.typing-game.local): the catalogue is in Git,
# its sound files come from Drive.
FEEL_CATALOGUE="$ROOT_DIR/typing-feel/public/v1/keys/keys-manifest.json"
if [[ ! -f "$FEEL_CATALOGUE" ]]; then
  echo "Typing Feel catalogue is missing: $FEEL_CATALOGUE"
  echo "Run: pnpm feel:import ~/AudioLab/review/staging/keys-firefly"
  echo "     (on a fresh clone the catalogue comes with Git; get its sound files with: pnpm media:pull)"
  exit 1
fi

# The Typing Feel origin the parent's build:<game> sets (VITE_TYPING_FEEL_ORIGIN), or nothing.
feel_origin() {
  node -e '
    const script = require(process.argv[1]).scripts?.[process.argv[2]] ?? "";
    const match = /(?:^|\s)VITE_TYPING_FEEL_ORIGIN=(["\x27]?)([^\s"\x27]+)\1(?=\s|$)/.exec(script);
    process.stdout.write(match ? match[2].replace(/\/+$/, "") : "");
  ' "$ROOT_DIR/package.json" "$1"
}

# The page links rel="preconnect" to that origin (vite.config.ts adds it only when the build has one).
has_preconnect() {
  # The last grep reads all its input (no -q), so pipefail never sees a SIGPIPE.
  tr '\n' ' ' <"$1" | grep -o '<link[^>]*>' | grep -F 'rel="preconnect"' | grep -F -e "href=\"$2\"" -e "href=\"$2/\"" >/dev/null
}

# A game's own `pnpm build` or `pnpm check` leaves a dist without Typing Feel
# (docs/games/TYPING_FEEL_SERVICE.md §5.1): never serve that one on the play host.
# Checked only for a game whose vite.config.ts reads the origin (a branch before
# its Typing Feel step builds the same either way). Such a game's build:<game>
# must set the origin: without it the game would play with keyboard sounds off
# (its copied sets are gone) and nothing would say so.
for entry in dragon-hold:build:dragon typing-defense:build:td typing-survival:build:survival; do
  dir="${entry%%:*}"
  script="${entry#*:}"
  html="$ROOT_DIR/games/$dir/dist/index.html"
  [[ -f "$ROOT_DIR/games/$dir/package.json" && -f "$html" ]] || continue
  grep -qs VITE_TYPING_FEEL_ORIGIN "$ROOT_DIR/games/$dir/vite.config.ts" || continue
  origin="$(feel_origin "$script")"
  if [[ -z "$origin" ]]; then
    echo "games/$dir reads VITE_TYPING_FEEL_ORIGIN, but the parent's $script sets none: its keyboard sounds would be off on the play host."
    echo "Add VITE_TYPING_FEEL_ORIGIN=https://feel.typing-game.local to $script and ${script/build:/dev:}:app in package.json, then run: pnpm $script"
    exit 1
  fi
  has_preconnect "$html" "$origin" && continue
  echo "  → games/$dir/dist was built without Typing Feel ($origin); rebuilding with: pnpm $script"
  if ! command -v pnpm >/dev/null 2>&1 || ! (cd "$ROOT_DIR" && pnpm "$script") || ! has_preconnect "$html" "$origin"; then
    echo "games/$dir/dist/index.html has no preconnect to $origin: it cannot be served on the play host."
    echo "Run: pnpm $script"
    exit 1
  fi
done

open_url() {
  if command -v open >/dev/null 2>&1; then
    open "$URL"
    return
  fi

  if command -v wslview >/dev/null 2>&1; then
    wslview "$URL"
    return
  fi

  if command -v cmd.exe >/dev/null 2>&1; then
    cmd.exe /C start "" "$URL" >/dev/null 2>&1 || true
    return
  fi

  if command -v powershell.exe >/dev/null 2>&1; then
    powershell.exe -NoProfile -Command "Start-Process '$URL'" >/dev/null 2>&1 || true
    return
  fi

  if command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$URL" >/dev/null 2>&1 || true
    return
  fi

  echo "Open this URL in your browser: $URL"
}

open_url
