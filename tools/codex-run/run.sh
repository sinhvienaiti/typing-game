#!/usr/bin/env bash
# Run one Codex task (a markdown brief) non-interactively on the Mac and keep its logs (bash twin of run.ps1).
#
#   tools/codex-run/run.sh <name> <brief.md> [cwd] [effort] [sandbox] [model]
#   tools/codex-run/run.sh 005a-td-vs-images-characters docs/codex-queue/005a-td-vs-images-characters.md games/typing-defense
#
# Codex CLI: $CODEX_BIN, else the newest copy inside Cursor's ChatGPT extension (0.162.0-alpha reaches gpt-6.1-sol).
# Logs: .local/codex-runs/<name>/{brief.md, events.jsonl, last.md, err.txt}
set -u
[ $# -ge 2 ] || { echo "usage: run.sh <name> <brief.md> [cwd] [effort] [sandbox] [model]" >&2; exit 2; }
# Owner 27/10: pick the model and effort by the kind of work (README, "Chọn model"), not ultra for everything.
name=$1; brief=$2; cwd=${3:-.}; effort=${4:-high}; sandbox=${5:-workspace-write}
model=${6:-${CODEX_MODEL:-gpt-6.1-sol}}
root=$(cd "$(dirname "$0")/../.." && pwd)
codex=${CODEX_BIN:-$(ls -d "$HOME"/.cursor/extensions/openai.chatgpt-*/bin/macos-aarch64/codex 2>/dev/null | sort -V | tail -1)}
[ -n "$codex" ] && [ -x "$codex" ] || { echo "Codex CLI not found (set CODEX_BIN)" >&2; exit 127; }
case "$effort" in low|medium|high|xhigh|max|ultra) ;; *) echo "effort must be low, medium, high, xhigh, max or ultra" >&2; exit 2 ;; esac
case "$model" in gpt-6.1-sol|gpt-6-astra|gpt-6-luna|gpt-6-sol) ;; *) echo "model not in the list of README (Chọn model): $model" >&2; exit 2 ;; esac
case "$sandbox" in read-only|workspace-write|danger-full-access) ;; *) echo "bad sandbox: $sandbox" >&2; exit 2 ;; esac


# ---- Gates (owner 12/11/2026: rules enforced by the machine, not by memory). No model call, no tokens. ----
# Exit 78 = refused by a gate. Nothing bypasses a gate; fix the ticket instead.
gate() { echo "GATE REFUSED ($name): $1" >&2; mkdir -p "$root/.local/codex-runs"; echo "$(date '+%F %T') $name $1" >> "$root/.local/codex-runs/gate-refusals.log"; exit 78; }
# G1 critic: every ticket carries a line starting "Phản biện: PASS" (one fresh critic passed it; AGENTS.md lighter review).
grep -q "^Phản biện: PASS" "$root/$brief" || gate "no line 'Phản biện: PASS' in $brief (run a fresh critic first)"
# G2 one lane: no other Codex run in progress.
# More lanes only when the owner asks (AGENTS.md "one lane unless the owner asks for more"; owner 15/11/2026:
# "giao cho nó 2 làn làm việc đi"): CODEX_LANES=2 lets a second run start.
running=$(pgrep -f "[c]odex exe[c] -m" | wc -l | tr -d ' ')
[ "$running" -ge "${CODEX_LANES:-1}" ] && gate "$running Codex run(s) in progress (lanes ${CODEX_LANES:-1})"
# G3 quota: below 15 % left in the 5-hour or weekly window, only image tickets (the brief uses image_gen).
used=$(python3 - <<'PY'
import glob, json, os
fs = sorted(glob.glob(os.path.expanduser('~/.codex/sessions/**/rollout-*.jsonl'), recursive=True), key=os.path.getmtime)
u = 0
for f in fs[-3:]:
    for l in open(f, errors='ignore'):
        if 'rate_limits' not in l: continue
        try:
            d = json.loads(l); p = d.get('payload', d); r = p.get('rate_limits') or p.get('info', {}).get('rate_limits')
            if r: u = max((r.get('primary') or {}).get('used_percent', 0), (r.get('secondary') or {}).get('used_percent', 0))
        except Exception: pass
print(int(u))
PY
)
# Owner 13/11 18:2x: "từ h áp dụng lại luật dưới 15% thì codex chỉ dùng để tạo ảnh" — below 15 % left, image tickets only, no exceptions.
# An image ticket asks for generation ("Tối đa N lần `image_gen`" or "Dùng công cụ `image_gen`"); "không gọi image_gen" does not count.
# Owner 16/11/2026 22:4x waiver: "tôi đã nói cứ cho codex làm đi, tôi sẽ reset codex sau" — CODEX_QUOTA_WAIVER=1 lifts G3 until the owner resets Codex.
if [ "${CODEX_QUOTA_WAIVER:-0}" != 1 ] && [ "${used:-0}" -gt 85 ] && ! grep -Eq '(Tối đa [0-9]+ lần `?image_gen|Dùng công cụ `?image_gen)' "$root/$brief"; then gate "Codex quota ${used}% used (<15% left): image tickets only"; fi
# G4 sample before batch: a ticket with a line "Lô: ..." must carry "Mẫu đã gửi: <path>" and that file must exist.
if grep -q "^Lô:" "$root/$brief"; then
  s=$(sed -n 's/^Mẫu đã gửi: *//p' "$root/$brief" | head -1)
  [ -n "$s" ] && [ -e "$s" ] || gate "batch ticket without 'Mẫu đã gửi: <existing path>' (send the owner two samples first)"
fi

# G5 art source for VFX (owner 17/11/2026: "rõ ràng đã có rule, cấm tự làm các hiệu ứng vfx bằng code, tại sao bạn vẫn tự ý làm?").
# A code ticket that touches effects (paths with ult/vfx/skill/burst/fx or the words "hiệu ứng"/"VFX") must carry a line
# "Nguồn hình: <path>[, <path>...]" naming the approved image/video/model files each visible layer uses; every path must exist.
# Image-generation tickets are exempt (they make the sources). Code may only place, time, tint and animate those sources.
if ! grep -Eq '(Tối đa [0-9]+ lần `?image_gen|Dùng công cụ `?image_gen)' "$root/$brief" \
   && grep -Eiq '(src/lab/[a-z-]*(ult|vfx|fx|burst|skill)|hiệu ứng|VFX)' "$root/$brief"; then
  src=$(sed -n 's/^Nguồn hình: *//p' "$root/$brief" | head -1)
  [ -n "$src" ] || gate "VFX ticket without 'Nguồn hình: <approved art files>' (no code-drawn effects; AGENTS.md)"
  for p in $(echo "$src" | tr ',' ' '); do
    case "$p" in /*) f="$p";; *) f="$root/$p";; esac
    ls $f >/dev/null 2>&1 || gate "Nguồn hình path not found: $p"
  done
fi

log="$root/.local/codex-runs/$name"
mkdir -p "$log"
workdir=$(cd "$root/$cwd" && pwd) || exit 2
[ -f "$root/$brief" ] || { echo "brief not found: $brief" >&2; exit 2; }

{
  cat <<'EOF'
You are Codex working for the owner of the typing-game repo on a Mac mini M4 (macOS). Since 03/11/2026 the repo lives on an external SSD at /Volumes/SS990TPRO/htdocs/typing-game; /Users/toandx/htdocs/typing-game is a symlink to it. Always write through the /Volumes path.
House rules for this task:
- Do exactly the task below. Touch only the paths it allows. Never run git commit, git push, git reset, git clean or git stash.
- The task may name paths from the Dell laptop: read D:\typing-game as /Volumes/SS990TPRO/htdocs/typing-game. There is no WSL here: git, node, pnpm, python3 and ImageMagick 7 (/opt/homebrew/bin/magick) run directly. For tools/art-normalize export ART_MAGICK=/opt/homebrew/bin/magick. Font for contact sheets: /System/Library/Fonts/Supplemental/Arial.ttf.
- Other agents work in this repo at the same time (game code, game docs, tools/audio-lab). Never edit outside the paths the task allows, and do not run the games' builds or test suites.
- Tu Tien (games/immortality-cultivation, docs/games/tu-tien) is the owner's current focus and other agents edit it: write there only the paths the task allows, never its src, scripts, tests or docs.
- Never send third-party reference images (screenshots or art from commercial games, reference boards) to any image tool; use only the repo's own images the task names.
- Images: use your built-in image generation tool (image_gen). Save every image where the task says, with its exact prompt next to it as <name>.prompt.txt.
- Sounds must follow tools/audio-lab/DECISIONS.md Q6 (shaped by the action, no cheap puff/pop/thump sounds); write prompts affirmatively.
- Docs in Vietnamese with full diacritics, in the existing style of the folder.
- End with a short report: what you made (paths), what you skipped and why, anything the owner must look at.
- If a limit stops the task before it is done (a tool such as image_gen answers HTTP 429 or says to try later, or the task says not to start before a time), do not give up: keep every file as it is, write your report, and make the very last line of your final message exactly `CODEX-WAIT-UNTIL: HH:MM` (24-hour local time the tool or the task gives) or `CODEX-WAIT-UNTIL: unknown`. The runner waits until then and runs the task again; on that run, continue from what is already done.

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
# Keep the worker's own report: if the brief names docs/codex-queue/<n>-report.md and that file exists, never overwrite it;
# only when it is missing, save last.md there (13/11: callers' `cp last.md report` erased Codex's detailed reports).
rep=$(grep -o 'docs/codex-queue/[0-9a-z]*-report\.md' "$root/$brief" | head -1)
if [ -n "$rep" ] && [ ! -s "$root/$rep" ] && [ -s "$log/last.md" ]; then cp "$log/last.md" "$root/$rep"; fi
echo "exit $code"
[ -f "$log/last.md" ] && cat "$log/last.md"
exit $code
