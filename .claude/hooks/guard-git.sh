#!/usr/bin/env bash
# PreToolUse guard (owner 12/11/2026: rules enforced by the machine). Blocks, for every Claude session in this repo:
#  - git add of media (images, audio, video, 3D) or of whole trees (-A, --all, ".") — media travels by `pnpm media:push`.
# Pushing is not blocked: the owner made no such rule (12/11/2026, "tôi đâu có ra luật này").
# Exit 2 = block; stderr goes back to Claude. No model call, no tokens.
cmd=$(python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null)
[ -z "$cmd" ] && exit 0
if echo "$cmd" | grep -Eq '(^|[;&|[:space:]])git([[:space:]]+-C[[:space:]]+[^[:space:]]+)?[[:space:]]+add([[:space:]]|$)'; then
  if echo "$cmd" | grep -Eq 'git[^;&|]*[[:space:]]add[^;&|]*[[:space:]](-A|--all|\.|-u)([[:space:]]|$)'; then
    echo "BLOCKED by .claude/hooks/guard-git.sh: stage explicit paths only (no -A, --all, -u or '.')." >&2; exit 2
  fi
  if echo "$cmd" | grep -Eiq '\.(png|jpe?g|webp|gif|avif|exr|psd|wav|ogg|mp3|m4a|flac|aac|mp4|mov|webm|glb|gltf|bin|fbx|blend)([[:space:];&|]|$)'; then
    echo "BLOCKED by .claude/hooks/guard-git.sh: no media in Git; use pnpm media:push." >&2; exit 2
  fi
fi
exit 0
