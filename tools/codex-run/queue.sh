#!/usr/bin/env bash
# Run Codex tickets one after another from a list file on the Mac, riding out ChatGPT usage limits
# (bash twin of queue.ps1).
#
#   tools/codex-run/queue.sh .local/codex-lane-mac-a.txt
#
# List lines: name | brief | cwd | effort | sandbox | model   (blank lines and lines starting with # are skipped;
# effort defaults to high, sandbox to workspace-write, model to gpt-6.1-sol (pick by the work: README); backslashes in paths are read as /).
# A run that hits the usage limit waits until the time Codex names ("try again at 8:54 AM", else 30 minutes)
# and runs again, up to 12 times; a dropped connection runs again after 2 minutes, up to 4 times.
# Failed log dirs are kept as <name>-prev-<MMddHHmm>.
set -u
[ $# -ge 1 ] || { echo "usage: queue.sh <list>" >&2; exit 2; }
root=$(cd "$(dirname "$0")/../.." && pwd)
run="$root/tools/codex-run/run.sh"
list=$1
cd "$root" || exit 2

stamp() { date '+%d/%m %H:%M'; }

# "try again at 8:54 AM" -> that moment today (tomorrow if passed) + 2 minutes, as epoch seconds.
resume_at() {
  local t at
  t=$(grep -o 'try again at [0-9]\{1,2\}:[0-9]\{2\} *[AaPp][Mm]' "$1" 2>/dev/null | tail -1 | sed 's/try again at //')
  if [ -n "$t" ]; then
    at=$(date -j -f '%Y-%m-%d %I:%M %p' "$(date +%Y-%m-%d) $(echo "$t" | tr 'apm' 'APM')" +%s 2>/dev/null)
  fi
  if [ -z "${at:-}" ]; then echo $(( $(date +%s) + 1800 )); return; fi
  [ "$at" -le "$(date +%s)" ] && at=$(( at + 86400 ))
  echo $(( at + 120 ))
}

grep -v '^[[:space:]]*#' "$list" | grep -v '^[[:space:]]*$' | tr '\\' '/' | while IFS='|' read -r name brief cwd effort sandbox model; do
  name=$(echo "$name" | xargs); brief=$(echo "$brief" | xargs)
  cwd=$(echo "${cwd:-.}" | xargs); effort=$(echo "${effort:-high}" | xargs); sandbox=$(echo "${sandbox:-workspace-write}" | xargs); model=$(echo "${model:-gpt-6.1-sol}" | xargs)
  log="$root/.local/codex-runs/$name"
  limits=0; drops=0
  while :; do
    [ -d "$log" ] && mv "$log" "$log-prev-$(date +%m%d%H%M)"
    echo "$(stamp) start $name ($model, $effort, $sandbox)"
    "$run" "$name" "$brief" "$cwd" "$effort" "$sandbox" "$model" > /dev/null < /dev/null
    code=$?
    events="$log/events.jsonl"
    # Only a run that failed or left no report counts: a finished run's events may quote these words from files it read.
    failed=0; { [ "$code" -ne 0 ] || [ ! -s "$log/last.md" ]; } && failed=1
    if [ "$failed" -eq 1 ] && grep -q 'usage limit' "$events" 2>/dev/null; then
      limits=$((limits + 1))
      echo "$(stamp) end $name exit $code (usage limit $limits)"
      [ "$limits" -ge 12 ] && { echo "$(stamp) giving up on $name"; break; }
      until_ts=$(resume_at "$events")
      echo "$(stamp) waiting for the limit to reset at $(date -r "$until_ts" '+%d/%m %H:%M')"
      while [ "$(date +%s)" -lt "$until_ts" ]; do sleep 60; done
      continue
    fi
    if [ "$code" -ne 0 ] && grep -q 'stream disconnected' "$events" 2>/dev/null; then
      drops=$((drops + 1))
      echo "$(stamp) end $name exit $code (connection dropped $drops)"
      [ "$drops" -ge 4 ] && { echo "$(stamp) giving up on $name"; break; }
      sleep 120
      continue
    fi
    echo "$(stamp) end $name exit $code"
    break
  done
done
echo "$(stamp) queue done"
