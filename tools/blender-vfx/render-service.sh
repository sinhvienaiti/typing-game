#!/usr/bin/env bash
# Run Blender renders for sandboxed Codex lanes. Blender 5.2 segfaults inside the Codex sandbox (07/11/2026:
# three crashes, each one a macOS "Blender quit unexpectedly" dialog for the owner); outside it, Cycles and
# EEVEE render fine. So Codex writes the scripts and a request file, and this service runs Blender.
#
#   nohup tools/blender-vfx/render-service.sh >> .local/blender-queue/service.log 2>&1 &
#
# Request: .local/blender-queue/<name>.req
#   line 1: script path, must be under tools/blender-vfx/ and end in .py
#   line 2: output folder, must be under .local/
#   lines 3+: optional VFX_*=value environment lines (anything else is ignored)
# Result: <name>.log (Blender output) and <name>.done (exit code; 2 = request refused, 124 = 15 min timeout).
# One render at a time. Stop: touch .local/blender-queue/.stop
set -u
cd "$(dirname "$0")/../.." || exit 1
Q=.local/blender-queue
B=/Applications/Blender.app/Contents/MacOS/Blender
mkdir -p "$Q"
echo "$(date '+%d/%m %H:%M') render service start"
while [ ! -e "$Q/.stop" ]; do
  for r in "$Q"/*.req; do
    [ -e "$r" ] || continue
    n="${r%.req}"
    mv "$r" "$n.taken"
    script=$(sed -n 1p "$n.taken")
    out=$(sed -n 2p "$n.taken")
    case "$script" in tools/blender-vfx/*.py) ;; *) echo "refused: script must be tools/blender-vfx/*.py, got '$script'" > "$n.log"; echo 2 > "$n.done"; continue ;; esac
    case "$out" in .local/*) ;; *) echo "refused: output must be under .local/, got '$out'" > "$n.log"; echo 2 > "$n.done"; continue ;; esac
    case "$script$out" in *..*) echo "refused: '..' in a path" > "$n.log"; echo 2 > "$n.done"; continue ;; esac
    envs=()
    while IFS= read -r l; do
      case "$l" in VFX_[A-Z0-9_]*=*) envs+=("$l") ;; esac
    done < <(sed -n '3,$p' "$n.taken")
    mkdir -p "$out"
    echo "$(date '+%d/%m %H:%M') render $(basename "$n"): $script -> $out"
    env ${envs[@]+"${envs[@]}"} timeout 900 "$B" -b --factory-startup -P "$script" -- "$out" > "$n.log" 2>&1
    echo $? > "$n.done"
    echo "$(date '+%d/%m %H:%M') done $(basename "$n"): exit $(cat "$n.done")"
  done
  sleep 3
done
echo "$(date '+%d/%m %H:%M') render service stopped"
