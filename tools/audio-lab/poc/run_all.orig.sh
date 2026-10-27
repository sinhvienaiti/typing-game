#!/usr/bin/env bash
# Reproduce the "AI ears" PoC end to end. Everything stays under $P (no system install,
# no API key, no account). Needs: macOS arm64, curl, unzip, ~10 GB free disk, internet once.
set -euo pipefail
P="${P:-$(cd "$(dirname "$0")" && pwd)}"
export UV_CACHE_DIR="$P/cache/uv" UV_PYTHON_INSTALL_DIR="$P/cache/python" UV_NO_CONFIG=1
export HF_HOME="$P/cache/hf" HF_HUB_DISABLE_TELEMETRY=1 TOKENIZERS_PARALLELISM=false
cd "$P"

# 0. a private uv binary (system python3 is 3.9.6; uv fetches a standalone CPython 3.12)
if [ ! -x dl/uv/uv-aarch64-apple-darwin/uv ]; then
  mkdir -p dl/uv && (cd dl/uv &&
    curl -sSLO https://github.com/astral-sh/uv/releases/latest/download/uv-aarch64-apple-darwin.tar.gz &&
    curl -sSLO https://github.com/astral-sh/uv/releases/latest/download/uv-aarch64-apple-darwin.tar.gz.sha256 &&
    shasum -a 256 -c uv-aarch64-apple-darwin.tar.gz.sha256 && tar xzf uv-aarch64-apple-darwin.tar.gz)
fi
UV="$P/dl/uv/uv-aarch64-apple-darwin/uv"

# 1. venv A: analysis + learned critics (transformers 5.x)
[ -x .venv/bin/python ] || "$UV" venv --python 3.12 .venv
"$UV" pip install --python .venv/bin/python numpy scipy librosa soundfile pyloudnorm matplotlib pedalboard \
  torch torchaudio transformers audiobox_aesthetics
# 1b. venv B: the MiDashengLM remote code only works with transformers 4.57.x
[ -x .venv-tf4/bin/python ] || "$UV" venv --python 3.12 .venv-tf4
"$UV" pip install --python .venv-tf4/bin/python "transformers==4.57.6" torch torchaudio librosa soundfile numpy

# 2. test material: synthetic archetypes + 8 Kenney CC0 sounds (each zip in its own folder)
mkdir -p samples/synthetic samples/cc0_kenney
.venv/bin/python -I gen_samples.py samples/synthetic
get() { mkdir -p "dl/$1" && [ -f "dl/$1/$1.zip" ] || curl -sSL -o "dl/$1/$1.zip" "$2"; (cd "dl/$1" && unzip -q -o "$1.zip" -d x); }
get kenney-impact "https://kenney.nl/media/pages/assets/impact-sounds/87b4ddecda-1677589768/kenney_impact-sounds.zip"
get kenney-scifi  "https://kenney.nl/media/pages/assets/sci-fi-sounds/6b296f9ecf-1677589334/kenney_sci-fi-sounds.zip"
for f in impactPunch_heavy_000 impactMetal_heavy_000 impactBell_heavy_000 impactWood_heavy_000 impactGeneric_light_000; do
  cp "dl/kenney-impact/x/Audio/$f.ogg" "samples/cc0_kenney/kenney_$f.ogg"; done
for f in laserLarge_000 explosionCrunch_000 spaceEngineLow_000; do
  cp "dl/kenney-scifi/x/Audio/$f.ogg" "samples/cc0_kenney/kenney_$f.ogg"; done
.venv/bin/python -I degrade.py samples/degraded samples/synthetic/syn_punchy_impact.wav samples/synthetic/syn_scifi_zap.wav \
  samples/cc0_kenney/kenney_impact{Punch,Metal,Wood,Bell}_heavy_000.ogg samples/cc0_kenney/kenney_explosionCrunch_000.ogg \
  samples/cc0_kenney/kenney_laserLarge_000.ogg

# 3. technical critic (JSON + PNG per file)
.venv/bin/python -I analyze.py samples/synthetic/*.wav samples/cc0_kenney/*.ogg --out out/analyze --profile-map profile_map.json
.venv/bin/python -I analyze.py samples/degraded/*.wav --out out/analyze_degraded --profile impact

# 4. learned critics (first run downloads ~2.7 GB of weights into $HF_HOME; later runs: HF_HUB_OFFLINE=1)
.venv/bin/python -I critics.py --manifest manifest.json --out out/critics.json --only aes,clap,ast
.venv/bin/python -I critics.py --manifest manifest_degraded.json --out out/critics_degraded.json --only aes,clap,ast
.venv-tf4/bin/python -I listener.py --manifest manifest.json --out out/listener.json
.venv-tf4/bin/python -I listener.py --manifest manifest_degraded.json --out out/listener_degraded.json

# 5. tables
.venv/bin/python -I score_pairs.py > out/pairs.md
.venv/bin/python -I make_tables.py > out/tables.md
echo "done: see $P/report.md, $P/out/"
