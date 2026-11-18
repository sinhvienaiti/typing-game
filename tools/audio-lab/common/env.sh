# Audio Lab environment. Source it: `source tools/audio-lab/common/env.sh`.
# No tokens, no telemetry, Hugging Face offline unless AUDIOLAB_ONLINE=1.

_al_here="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
export AUDIOLAB_LAB="$(cd "$_al_here/.." && pwd)"            # tools/audio-lab (code, Git)
export AUDIOLAB_REPO="$(cd "$AUDIOLAB_LAB/../.." && pwd)"     # typing-game root
unset _al_here

# Heavy data lives outside every repo.
export AUDIOLAB_HOME="${AUDIOLAB_HOME:-$HOME/AudioLab}"
export AUDIOLAB_MODELS="$AUDIOLAB_HOME/models"
export AUDIOLAB_LIBRARIES="$AUDIOLAB_HOME/libraries"
export AUDIOLAB_WORK="$AUDIOLAB_HOME/work"
export AUDIOLAB_REVIEW="$AUDIOLAB_HOME/review"
export AUDIOLAB_BIN="$AUDIOLAB_HOME/bin"
export AUDIOLAB_CACHE="$AUDIOLAB_HOME/cache"
export AUDIOLAB_VENV="$AUDIOLAB_HOME/.venv"
export AUDIOLAB_PY="$AUDIOLAB_VENV/bin/python"
export AUDIOLAB_UV="$AUDIOLAB_BIN/uv"

# uv: private binary, private CPython, no user config, never fetch Python on its own.
export UV_CACHE_DIR="$AUDIOLAB_CACHE/uv"
export UV_PYTHON_INSTALL_DIR="$AUDIOLAB_HOME/python"
export UV_NO_CONFIG=1
export UV_PYTHON_DOWNLOADS=never
export UV_PYTHON_PREFERENCE=only-managed

# Hugging Face: shared cache, never a token, no telemetry.
export HF_HOME="$AUDIOLAB_MODELS/hf-cache"
export HF_HUB_DISABLE_IMPLICIT_TOKEN=1
export HF_HUB_DISABLE_TELEMETRY=1
export HF_HUB_DISABLE_PROGRESS_BARS=1
export DO_NOT_TRACK=1
export TOKENIZERS_PARALLELISM=false
unset HF_TOKEN HUGGING_FACE_HUB_TOKEN HF_TOKEN_PATH
if [ "${AUDIOLAB_ONLINE:-0}" = "1" ]; then
  export HF_HUB_OFFLINE=0
else
  export HF_HUB_OFFLINE=1
fi

# Library caches out of $HOME defaults and out of the repo.
export TORCH_HOME="$AUDIOLAB_MODELS/torch"
export MPLCONFIGDIR="$AUDIOLAB_CACHE/matplotlib"
export MPLBACKEND=Agg
export NUMBA_CACHE_DIR="$AUDIOLAB_CACHE/numba"
# Python runs with -I (ignores PYTHON* vars); launch.py moves bytecode to $AUDIOLAB_CACHE/pycache.

# Act like an activated venv for child processes.
export VIRTUAL_ENV="$AUDIOLAB_VENV"
case ":$PATH:" in
  *":$AUDIOLAB_VENV/bin:"*) ;;
  *) export PATH="$AUDIOLAB_VENV/bin:$PATH" ;;
esac

# Listening Board port (strict; 3192 only if 3191 is busy).
export AUDIOLAB_BOARD_HOST=127.0.0.1
export AUDIOLAB_BOARD_PORT="${AUDIOLAB_BOARD_PORT:-3191}"
