#!/usr/bin/env bash
set -euo pipefail
source "$(dirname -- "${BASH_SOURCE[0]}")/common.sh"
exec python3 "$ART_NORMALIZE_DIR/normalize.py" icon "$@"
