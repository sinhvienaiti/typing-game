#!/bin/bash
# Nightly junk cleanup (owner 17/11: "nên có 1 lịch xoá file rác mỗi 23h tối").
# Only removes leftovers that are safe by construction:
#  1. headless Chrome started for captures (--headless + --remote-debugging-port) running > 2 h;
#  2. temp Chrome profiles (prof*, st-cdp-*, puppeteer/playwright profiles) not opened by any process, older than 2 h;
#  3. Codex hand-off folders /private/tmp/typing-game-* older than 3 days (their sheets are already copied to typing-game-review);
#  4. Claude scratchpads older than 3 days under /private/tmp/claude-501/*/*/scratchpad.
# Never touches the repo, art-src, typing-game-review, the user's own Chrome or running work.
# Usage: nightly.sh [--apply]   (without --apply it only lists)
APPLY=0; [ "$1" = "--apply" ] && APPLY=1
LOG=/Volumes/SS990TPRO/htdocs/typing-game/.local/cleanup/nightly.log
say(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
free_before=$(df -g / | awk 'NR==2{print $4}')
say "start apply=$APPLY free=${free_before}G"

# 1. orphan headless Chrome > 2 h
ps -axo pid=,etime=,command= | grep -E 'Google Chrome.*--headless.*--remote-debugging-port|chrome-headless-shell' | grep -v grep | while read -r pid et rest; do
  # etime: [[dd-]hh:]mm:ss
  secs=$(echo "$et" | awk -F'[-:]' '{n=NF; s=$n+$(n-1)*60; if(n>=3)s+=$(n-2)*3600; if(n>=4)s+=$(n-3)*86400; print s}')
  if [ "$secs" -gt 7200 ]; then say "chrome pid=$pid age=${et}"; [ $APPLY = 1 ] && kill "$pid" 2>/dev/null; fi
done

inuse=$(lsof -Fn 2>/dev/null | grep -oE '/(private/)?(tmp|var/folders)/[^ ]*(prof[0-9]+|st-cdp-[A-Za-z0-9]+|puppeteer_dev_profile-[A-Za-z0-9]+|playwright_chromiumdev_profile-[A-Za-z0-9]+)' | sort -u)
del(){ for p in "$@"; do
  [ -e "$p" ] || continue
  echo "$inuse" | grep -qF "$p" && continue
  sz=$(du -sh "$p" 2>/dev/null | cut -f1); say "rm $sz $p"; [ $APPLY = 1 ] && rm -rf "$p"
done; }

# 2. temp Chrome profiles
del $(find /private/tmp/claude-501 -maxdepth 3 -type d -name 'prof[0-9]*' -mmin +120 2>/dev/null)
del $(find "${TMPDIR:-/var/folders}" /private/tmp -maxdepth 2 -type d \( -name 'st-cdp-*' -o -name 'puppeteer_dev_profile-*' -o -name 'playwright_chromiumdev_profile-*' \) -mmin +120 2>/dev/null)
# 3. Codex hand-off folders
del $(find /private/tmp -maxdepth 1 -type d -name 'typing-game-*' -mtime +3 2>/dev/null)
# 4. old Claude scratchpads
# a scratchpad goes only when nothing inside changed for 3 days and no running command names it
running=$(ps -axo command=)
for sp in $(find /private/tmp/claude-501 -mindepth 3 -maxdepth 3 -type d -name scratchpad 2>/dev/null); do
  [ -n "$(find "$sp" -mtime -3 -print -quit 2>/dev/null)" ] && continue
  echo "$running" | grep -qF "$sp" && continue
  del "$sp"
done

free_after=$(df -g / | awk 'NR==2{print $4}')
say "done free=${free_after}G (was ${free_before}G)"
