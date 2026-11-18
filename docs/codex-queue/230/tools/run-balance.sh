#!/bin/bash
# Ticket 230: rerun the 220 balance reports in the codex copy (never in the worktree).
# Usage from the parent repo root: bash docs/codex-queue/230/tools/run-balance.sh <id> <first-seed> [stages]
# <id> is a key of docs/codex-queue/220/variants.json (v0, v6, f1..f4).
set -u
ROOT="$(pwd)"
C="$ROOT/games/typing-survival/tmp/codex-230"
id="$1"; first="$2"; stages="${3:-c1-s1}"
tag="$id-s$first"; [ "$stages" != "c1-s1" ] && tag="x-$tag"
set_arg="$(python3 -I -c 'import json,sys; print(json.load(open(sys.argv[1]))[sys.argv[2]])' docs/codex-queue/220/variants.json "$id")"
mkdir -p "$C/runs"
args=(--import tsx scripts/balance.ts "--stages=$stages" --seeds=100 "--first=$first" --g3c "--json=$C/runs/$tag.json" "--out=$C/runs/$tag.md")
[ -n "$set_arg" ] && args+=("--set=$set_arg")
start=$(date +%s)
( cd "$C/codex" && TMPDIR="$C/tmpdir" nice -n 15 node "${args[@]}" > /dev/null 2> "$C/runs/$tag.err" )
code=$?
end=$(date +%s)
printf '{"tag":"%s","set":"%s","stages":"%s","first":%s,"exit":%s,"start":%s,"end":%s,"seconds":%s,"uptime":"%s"}\n' \
  "$tag" "$set_arg" "$stages" "$first" "$code" "$start" "$end" "$((end-start))" "$(uptime | sed 's/"//g')" >> "$C/runs/timeline.jsonl"
