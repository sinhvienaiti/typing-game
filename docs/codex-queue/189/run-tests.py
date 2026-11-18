"""Chạy test keys trong sandbox Mac: chuyển cache numba/matplotlib/pytest vào tmp của phiếu.

Lệnh: bash tools/audio-lab/run.sh docs/codex-queue/189/run-tests.py
Không thay cấu hình Audio Lab chung hoặc các test của phiếu 182.
"""
import os
from pathlib import Path

repo = Path(__file__).resolve().parents[3]
cache = repo / 'tmp/keys-firefly/test-cache'
cache.mkdir(parents=True, exist_ok=True)
from common import env
env.CACHE = cache  # các test gọi env.apply() cũng giữ cache trong sandbox
env.apply()
import pytest

raise SystemExit(pytest.main(['-c', str(repo / 'tools/audio-lab/pytest.ini'),
                             '--rootdir', str(repo / 'tools/audio-lab'),
                             str(repo / 'tools/audio-lab/keys/tests'), '-q',
                             '-o', f'cache_dir={cache / "pytest"}']))
