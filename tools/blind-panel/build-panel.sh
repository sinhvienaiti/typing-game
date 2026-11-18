#!/bin/bash
# Build a blind judging packet from lab capture videos (30 fps, 1920x1080):
# one 12-frame play-camera sheet and one 8-frame 1:1 crop strip per candidate, all under neutral labels.
# The key (label -> source) is written only to KEY_FILE, which must lie outside OUT_DIR.
#
# Usage:
#   OUT_DIR=<packet dir> KEY_FILE=<key.json outside OUT_DIR> CROP=640x360+1040+50 \
#   SHEET_FRAMES="6 9 15 21 24 25 26 29 32 39 54 89" CROP_FRAMES="29 31 33 35 38 41 45 50" \
#   tools/blind-panel/build-panel.sh K=/path/a.mp4 M=/path/b.mp4 ...
#
# Pick labels yourself in a non-obvious order; never reuse the previous packet's mapping.
set -euo pipefail
: "${OUT_DIR:?}" "${KEY_FILE:?}"
CROP=${CROP:-640x360+1040+50}
SHEET_FRAMES=${SHEET_FRAMES:-"6 9 15 21 24 25 26 29 32 39 54 89"}
CROP_FRAMES=${CROP_FRAMES:-"29 31 33 35 38 41 45 50"}
FONT=${FONT:-/System/Library/Fonts/Supplemental/Arial.ttf}
mkdir -p "$(dirname "$KEY_FILE")" "$OUT_DIR"
case "$(cd "$(dirname "$KEY_FILE")" && pwd -P)/" in "$(cd "$OUT_DIR" && pwd -P)/"*) echo "KEY_FILE must be outside OUT_DIR" >&2; exit 2;; esac
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
cw=${CROP%%x*}; rest=${CROP#*x}; ch=${rest%%+*}
key="{"
for pair in "$@"; do
  L=${pair%%=*}; V=${pair#*=}
  [ -f "$V" ] || { echo "missing $V" >&2; exit 2; }
  T=$TMP/$L; mkdir -p "$T"
  ffmpeg -v error -y -i "$V" -fps_mode passthrough "$T/%03d.png"
  tiles=()
  for n in $SHEET_FRAMES; do
    i=$(printf %03d $((n+1))); t=$(printf "%.2f" "$(echo "$n/30" | bc -l)")
    magick "$T/$i.png" -resize 480x270 \( -size 480x30 xc:'#10141c' -font "$FONT" -fill white -pointsize 18 -gravity center -annotate +0+0 "$L · t=$t s" \) -append "$T/s$n.png"
    tiles+=("$T/s$n.png")
  done
  magick \( "${tiles[@]:0:4}" +append \) \( "${tiles[@]:4:4}" +append \) \( "${tiles[@]:8:4}" +append \) -append -quality 90 "$OUT_DIR/$L-sheet.jpg"
  c=()
  for n in $CROP_FRAMES; do
    i=$(printf %03d $((n+1))); t=$(printf "%.2f" "$(echo "$n/30" | bc -l)")
    magick "$T/$i.png" -crop "$CROP" +repage \( -size "${cw}x32" xc:'#10141c' -font "$FONT" -fill white -pointsize 20 -gravity center -annotate +0+0 "$L · t=$t s · 1:1 crop" \) -append "$T/c$n.png"
    c+=("$T/c$n.png")
  done
  magick \( "${c[@]:0:4}" +append \) \( "${c[@]:4:4}" +append \) -append -quality 92 "$OUT_DIR/$L-hit-crops.jpg"
  key="$key\"$L\": \"$V\","
done
mkdir -p "$(dirname "$KEY_FILE")"
printf '%s}\n' "${key%,}" > "$KEY_FILE"; chmod 600 "$KEY_FILE"
ls "$OUT_DIR"
