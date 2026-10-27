#!/usr/bin/env bash
# Run one Codex task (a markdown brief) non-interactively on the Mac and keep its logs (bash twin of run.ps1).
#
#   tools/codex-run/run.sh <name> <brief.md> [cwd] [effort] [sandbox]
#   tools/codex-run/run.sh 005a-td-vs-images-characters docs/codex-queue/005a-td-vs-images-characters.md games/typing-defense
#
# Codex CLI: $CODEX_BIN, else the newest copy inside Cursor's ChatGPT extension (0.162.0-alpha reaches gpt-6.1-sol).
# Logs: .local/codex-runs/<name>/{brief.md, events.jsonl, last.md, err.txt}
set -u
[ $# -ge 2 ] || { echo "usage: run.sh <name> <brief.md> [cwd] [effort] [sandbox]" >&2; exit 2; }
name=$1; brief=$2; cwd=${3:-.}; effort=${4:-ultra}; sandbox=${5:-workspace-write}
model=${CODEX_MODEL:-gpt-6.1-sol}
root=$(cd "$(dirname "$0")/../.." && pwd)
codex=${CODEX_BIN:-$(ls -d "$HOME"/.cursor/extensions/openai.chatgpt-*/bin/macos-aarch64/codex 2>/dev/null | sort -V | tail -1)}
[ -n "$codex" ] && [ -x "$codex" ] || { echo "Codex CLI not found (set CODEX_BIN)" >&2; exit 127; }
case "$effort" in high|xhigh|max|ultra) ;; *) echo "effort must be high, xhigh, max or ultra" >&2; exit 2 ;; esac
# Owner 27/10: every run at ultra; a lower effort in a lane file is raised (CODEX_EFFORT_EXACT=1 keeps it).
[ "${CODEX_EFFORT_EXACT:-0}" = 1 ] || effort=ultra
case "$sandbox" in read-only|workspace-write|danger-full-access) ;; *) echo "bad sandbox: $sandbox" >&2; exit 2 ;; esac

log="$root/.local/codex-runs/$name"
mkdir -p "$log"
workdir=$(cd "$root/$cwd" && pwd) || exit 2
[ -f "$root/$brief" ] || { echo "brief not found: $brief" >&2; exit 2; }

{
  cat <<'EOF'
You are Codex working for the owner of the typing-game repo (/Users/toandx/htdocs/typing-game) on a Mac mini M4 (macOS).
House rules for this task:
- Do exactly the task below. Touch only the paths it allows. Never run git commit, git push, git reset, git clean or git stash.
- The task may name paths from the Dell laptop: read D:\typing-game as /Users/toandx/htdocs/typing-game. There is no WSL here: git, node, pnpm, python3 and ImageMagick 7 (/opt/homebrew/bin/magick) run directly. For tools/art-normalize export ART_MAGICK=/opt/homebrew/bin/magick. Font for contact sheets: /System/Library/Fonts/Supplemental/Arial.ttf.
- Other agents work in this repo at the same time (game code, game docs, tools/audio-lab). Never edit outside the paths the task allows, and do not run the games' builds or test suites.
- Tu Tien (games/immortality-cultivation, docs/games/tu-tien) is paused by the owner: do not touch it.
- Images: use your built-in image generation tool (image_gen). Save every image where the task says, with its exact prompt next to it as <name>.prompt.txt.
- Sounds must follow tools/audio-lab/DECISIONS.md Q6 (shaped by the action, no cheap puff/pop/thump sounds); write prompts affirmatively.
- Docs in Vietnamese with full diacritics, in the existing style of the folder.
- End with a short report: what you made (paths), what you skipped and why, anything the owner must look at.

TASK
EOF
  echo
  cat "$root/$brief"
} > "$log/brief.md"

# --disable memories: the owner's Codex memory writer failed inside a run on the Dell (apply_patch on memory_summary.md).
env -u OPENAI_API_KEY -u CODEX_API_KEY "$codex" exec -m "$model" -c "model_reasoning_effort=\"$effort\"" \
  --disable memories --skip-git-repo-check -s "$sandbox" -C "$workdir" --json -o "$log/last.md" - \
  < "$log/brief.md" > "$log/events.jsonl" 2> "$log/err.txt"
code=$?
echo "exit $code"
[ -f "$log/last.md" ] && cat "$log/last.md"
exit $code
