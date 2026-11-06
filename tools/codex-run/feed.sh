#!/usr/bin/env bash
# Keep one Codex lane busy from a list file that may grow while it runs (queue.sh reads its list only once).
#
#   nohup tools/codex-run/feed.sh .local/codex-lane-mac-<name>.txt >> .local/codex-lane-mac-<name>.out 2>&1 &
#
# Same line format as queue.sh (name | brief | cwd | effort | sandbox | model). Each new line runs through
# queue.sh in order (so limits are waited out the same way); with no new line the feed checks again every 30 s.
# Append lines at any time (owner 07/11: add work every 30 minutes so Codex never idles).
# Stop: touch <list>.stop (the running ticket finishes first), or kill the feed, its queue.sh and codex exec.
set -u
list="$1"
here="$(cd "$(dirname "$0")" && pwd)"
n=0
stamp() { date '+%d/%m %H:%M'; }
items() { grep -v '^[[:space:]]*#' "$list" | grep -v '^[[:space:]]*$'; }
echo "$(stamp) feed start $list"
while [ ! -e "$list.stop" ]; do
  if [ "$(items | wc -l | tr -d ' ')" -gt "$n" ]; then
    n=$((n + 1))
    one="$list.item$n"
    items | sed -n "${n}p" > "$one"
    "$here/queue.sh" "$one"
    rm -f "$one"
  else
    sleep 30
  fi
done
echo "$(stamp) feed stopped ($list.stop)"
