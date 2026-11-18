"""Chỉ chạy test keys; giữ mọi cache kiểm thử trong tmp/keys-firefly."""
from pathlib import Path
from common import env
repo=Path(__file__).resolve().parents[3]
cache=repo/'tmp/keys-firefly/test-v2-cache'
cache.mkdir(parents=True,exist_ok=True)
env.CACHE=cache
env.apply()
import pytest
raise SystemExit(pytest.main(['-c',str(repo/'tools/audio-lab/pytest.ini'),
    '--rootdir',str(repo/'tools/audio-lab'),str(repo/'tools/audio-lab/keys/tests'),
    '-q','-o',f'cache_dir={cache/"pytest"}']))
