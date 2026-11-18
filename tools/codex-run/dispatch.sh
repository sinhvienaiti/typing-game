#!/usr/bin/env bash
# Zero-token lane dispatcher (owner 16/11/2026). Reads docs/work/LANES.md, starts the next queued ticket on each free lane.
root=$(cd "$(dirname "$0")/../.." && pwd); cd "$root" || exit 1
lanes=docs/work/LANES.md; log=.local/codex-runs/dispatch.log; mkdir -p .local/codex-runs
while :; do
  # mark finished
  grep -oE '^- \[~\] [0-9a-z]+' "$lanes" | awk '{print $3}' | while read -r id; do
    if [ -f "docs/codex-queue/$id-report.md" ] && ! pgrep -f "[c]odex-run/run.sh $id " >/dev/null; then
      sed -i '' "s/^- \[~\] $id |/- [x] $id |/" "$lanes"; echo "$(date '+%F %T') done $id" >> "$log"; fi
  done
  # start next per lane section if none running there
  awk '/^## /{sec=$0} /^- \[[ ~]\]/{print sec "\t" $0}' "$lanes" | grep -v "Cần Claude" > /tmp/lanes.$$
  for sec in $(cut -f1 /tmp/lanes.$$ | sort -u | tr ' ' '\001'); do
    s=${sec//$'\001'/ }
    grep -F "$s" /tmp/lanes.$$ | grep -q '\[~\]' && continue
    line=$(grep -F "$s" /tmp/lanes.$$ | grep '\[ \]' | head -1 | cut -f2); [ -z "$line" ] && continue
    id=$(echo "$line" | awk -F'|' '{print $1}' | awk '{print $NF}'); brief=$(echo "$line" | awk -F'|' '{gsub(/ /,"",$2);print $2}'); eff=$(echo "$line" | awk -F'|' '{gsub(/ /,"",$3);print $3}')
    CODEX_LANES=3 nohup tools/codex-run/run.sh "$id" "$brief" . "$eff" > ".local/codex-runs/$id.out" 2>&1 &
    sleep 5
    if grep -q "GATE REFUSED" ".local/codex-runs/$id.out"; then echo "$(date '+%F %T') refused $id: $(head -1 .local/codex-runs/$id.out)" >> "$log"
    else sed -i '' "s/^- \[ \] $id |/- [~] $id |/" "$lanes"; echo "$(date '+%F %T') start $id" >> "$log"; fi
  done
  rm -f /tmp/lanes.$$
  sleep 180
done
