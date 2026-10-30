#!/usr/bin/env bash
# Run Codex tickets one after another from a list file on the Mac, riding out ChatGPT usage limits
# (bash twin of queue.ps1).
#
#   tools/codex-run/queue.sh .local/codex-lane-mac-a.txt
#
# List lines: name | brief | cwd | effort | sandbox | model   (blank lines and lines starting with # are skipped;
# effort defaults to high, sandbox to workspace-write, model to gpt-6.1-sol (pick by the work: README); backslashes in paths are read as /).
# Limits never end a ticket (owner, 31/10: wait for the quota, then carry on; never stop while waiting):
# - a ChatGPT usage limit waits until the time Codex gives ("try again at 8:54 AM"), else 30 minutes, and runs again;
# - a tool limit inside a finished run (image_gen 429, a "not before 19:48" precondition) is reported by Codex as a last
#   line "CODEX-WAIT-UNTIL: HH:MM" or "CODEX-WAIT-UNTIL: unknown" (rule in run.sh); the queue waits the same way and runs again;
# - a dropped stream or "at capacity" runs again in 2 min, then every 15 min after the fourth drop.
# Failed log dirs are kept as <name>-prev-<MMddHHmm>.
set -u
[ $# -ge 1 ] || { echo "usage: queue.sh <list>" >&2; exit 2; }
root=$(cd "$(dirname "$0")/../.." && pwd)
run="$root/tools/codex-run/run.sh"
list=$1
cd "$root" || exit 2

stamp() { date '+%d/%m %H:%M'; }

# "CODEX-WAIT-UNTIL: 19:48" (24-hour) on the report's last line -> that moment today (tomorrow if passed) + 2 minutes;
# "unknown" or anything else -> 30 minutes from now. Prints nothing when the report has no such line.
tool_wait_at() {
  local line t at
  line=$(grep -v '^[[:space:]]*$' "$1" 2>/dev/null | tail -1 | tr -d '`*' | sed 's/^[[:space:]]*//')
  case "$line" in CODEX-WAIT-UNTIL:*) ;; *) return ;; esac
  t=$(echo "$line" | grep -o '[0-9]\{1,2\}:[0-9]\{2\}' | head -1)
  [ -n "$t" ] && at=$(date -j -f '%Y-%m-%d %H:%M' "$(date +%Y-%m-%d) $t" +%s 2>/dev/null)
  if [ -z "${at:-}" ]; then echo $(( $(date +%s) + 1800 )); return; fi
  [ "$at" -le "$(date +%s)" ] && at=$(( at + 86400 ))
  echo $(( at + 120 ))
}

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
  limits=0; drops=0; tools=0
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
      until_ts=$(resume_at "$events")
      echo "$(stamp) waiting for the limit to reset at $(date -r "$until_ts" '+%d/%m %H:%M')"
      while [ "$(date +%s)" -lt "$until_ts" ]; do sleep 60; done
      continue
    fi
    if [ "$code" -ne 0 ] && grep -qE 'stream disc|at capac' "$events" 2>/dev/null; then
      drops=$((drops + 1))
      echo "$(stamp) end $name exit $code (connection dropped $drops)"
      if [ "$drops" -ge 4 ]; then sleep 900; else sleep 120; fi
      continue
    fi
    if [ "$code" -eq 0 ]; then
      until_ts=$(tool_wait_at "$log/last.md")
      if [ -n "$until_ts" ]; then
        tools=$((tools + 1))
        echo "$(stamp) end $name exit 0 (tool limit $tools)"
        echo "$(stamp) waiting for the tool to reopen at $(date -r "$until_ts" '+%d/%m %H:%M')"
        while [ "$(date +%s)" -lt "$until_ts" ]; do sleep 60; done
        continue
      fi
    fi
    echo "$(stamp) end $name exit $code"
    break
  done
done
echo "$(stamp) queue done"
