#!/usr/bin/env bash
# Re-score the 40-sound PoC set offline with the shared venv (no download, no token).
# Fixtures: ~/AudioLab/work/_fixtures/poc40. Output: ~/AudioLab/work/_poc/<stamp>/out.
# Usage: bash tools/audio-lab/poc/rerun.sh [--rules-only]
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$HERE/../common/env.sh"
FIX="$AUDIOLAB_WORK/_fixtures/poc40"
RUN="$AUDIOLAB_WORK/_poc/$(date +%Y%m%d-%H%M%S)"
mkdir -p "$RUN/out"
PY=("$AUDIOLAB_PY" -I)

# Manifests in Git hold paths relative to the fixture root.
"${PY[@]}" - "$HERE" "$FIX" "$RUN" <<'EOF'
import json, sys
here, fix, run = sys.argv[1:4]
for m in ("manifest.json", "manifest_degraded.json"):
    items = json.load(open(f"{here}/{m}"))
    for it in items:
        it["path"] = f"{fix}/{it['path']}"
    json.dump(items, open(f"{run}/{m}", "w"), indent=1)
EOF

"${PY[@]}" "$HERE/analyze.py" "$FIX"/synthetic/*.wav "$FIX"/cc0_kenney/*.ogg \
  --out "$RUN/out/analyze" --profile-map "$HERE/profile_map.json"
"${PY[@]}" "$HERE/analyze.py" "$FIX"/degraded/*.wav --out "$RUN/out/analyze_degraded" --profile impact
if [ "${1:-}" != "--rules-only" ]; then
  "${PY[@]}" "$HERE/critics.py" --manifest "$RUN/manifest.json" --out "$RUN/out/critics.json" --only aes,clap,ast
  "${PY[@]}" "$HERE/critics.py" --manifest "$RUN/manifest_degraded.json" --out "$RUN/out/critics_degraded.json" --only aes,clap,ast
  (cd "$RUN" && "${PY[@]}" "$HERE/score_pairs.py" > out/pairs.md)
fi
echo "$RUN/out"
