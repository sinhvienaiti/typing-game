#!/bin/bash
# gen.sh <name> <canvas: portrait|square|landscape> <prompt-file>  -> prints the copied PNG path
set -e
D=/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/ea3cd405-f9d2-442c-a760-74fe0277c6ca/scratchpad/codex-art
CX=~/.cursor/extensions/openai.chatgpt-26.1007.21434/bin/macos-aarch64/codex
name=$1; canvas=$2; pf=$3; ref=$4
case $canvas in portrait) c="a portrait canvas, about 2:3 (taller than wide)";; landscape) c="a landscape canvas, about 3:2 (wider than tall)";; *) c="a square canvas";; esac
prompt="Use your built-in image generation tool (image_gen) to generate exactly ONE image on $c. Use the text between <<< and >>> verbatim as the image prompt: do not shorten, reorder, soften or add to it.
<<<
$(cat "$pf")
>>>
$( if [ -n "$ref" ]; then echo "The attached image is the approved main image of this same subject: pass its path to the image tool as a reference image (referenced_image_paths) and keep the design identical, following the view instructions inside the prompt."; fi )
Do not run shell commands and do not write files yourself. When the image is done, reply only with the absolute path of the generated PNG."
cd $D/logs
imgargs=(); if [ -n "$ref" ]; then imgargs=(-i "$ref"); fi
env -u OPENAI_API_KEY -u CODEX_API_KEY "$CX" exec --skip-git-repo-check --json "${imgargs[@]}" -o "$name.last.txt" "$prompt" > "$name.events.jsonl" 2> "$name.err.txt" < /dev/null
src=$(grep -o '/Users/[^ "]*\.png' "$name.last.txt" | tail -1)
[ -f "$src" ] || { echo "NO_IMAGE"; cat "$name.last.txt"; exit 2; }
n=1; while [ -f "$D/out/$name-a$n.png" ]; do n=$((n+1)); done
cp "$src" "$D/out/$name-a$n.png"; echo "$D/out/$name-a$n.png"
