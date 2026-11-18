#!/usr/bin/env bash
set -euo pipefail
source "$(dirname -- "${BASH_SOURCE[0]}")/../../common.sh"
export ART_NORMALIZE_DIR
python3 - <<'PY'
import ast
import os
from pathlib import Path
import subprocess
root = Path(os.environ['ART_NORMALIZE_DIR'])
files = []
for folder, directories, names in os.walk(root):
    directories[:] = [name for name in directories if name not in ('.tmp', '__pycache__')]
    files.extend(Path(folder)/name for name in names)
for p in files:
    if p.suffix == '.py':
        ast.parse(p.read_text(encoding='utf-8'), filename=str(p))
    elif p.suffix == '.sh':
        subprocess.run(['bash', '-n', str(p)], check=True)
print('ĐẠT: cú pháp Python và bash của công cụ cùng hồ sơ lô.')
PY
