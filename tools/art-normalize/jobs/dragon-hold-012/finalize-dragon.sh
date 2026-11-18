#!/usr/bin/env bash
set -euo pipefail
printf '%s\n' 'Hồ sơ 012 đã khóa; dùng rebuild-012d.sh.' >&2
exit 1
source "$(dirname -- "${BASH_SOURCE[0]}")/../../common.sh"
exec python3 "$ART_NORMALIZE_DIR/finalize_dragon.py" "$@"
