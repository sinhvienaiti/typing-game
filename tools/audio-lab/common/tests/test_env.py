import os
import subprocess
import sys

from common import env
from common import launch


def test_apply_drops_tokens_and_sets_safe_vars(monkeypatch):
    monkeypatch.setenv("HF_TOKEN", "x")
    monkeypatch.setenv("HUGGING_FACE_HUB_TOKEN", "y")
    monkeypatch.delenv("AUDIOLAB_ONLINE", raising=False)
    env.apply()
    assert "HF_TOKEN" not in os.environ
    assert "HUGGING_FACE_HUB_TOKEN" not in os.environ
    assert os.environ["HF_HUB_DISABLE_IMPLICIT_TOKEN"] == "1"
    assert os.environ["HF_HUB_DISABLE_TELEMETRY"] == "1"
    assert os.environ["HF_HUB_OFFLINE"] == "1"
    assert os.environ["TOKENIZERS_PARALLELISM"] == "false"
    assert os.environ["HF_HOME"] == str(env.HF_HOME)


def test_online_switch(monkeypatch):
    monkeypatch.setenv("AUDIOLAB_ONLINE", "1")
    assert env.safe_env()["HF_HUB_OFFLINE"] == "0"


def test_paths_outside_repo():
    for p in (env.HOME, env.MODELS, env.WORK, env.HF_HOME, env.VENV):
        assert env.REPO not in p.parents
    assert env.LAB.name == "audio-lab"
    assert (env.LAB / "run.sh").is_file()


def test_board_port_contract():
    assert (env.BOARD_HOST, env.BOARD_PORT, env.BOARD_PORT_FALLBACK) == ("127.0.0.1", 3191, 3192)


def test_aliases_cover_pnpm_scripts():
    for alias in ("critic", "board", "specs", "licence-check", "test"):
        assert alias in launch.ENTRYPOINTS


def test_shell_env_matches_python_env():
    out = subprocess.run(
        ["bash", "-c", f'source "{env.LAB}/common/env.sh" && env'],
        capture_output=True, text=True, check=True,
        env={"HOME": os.environ.get("HOME", ""), "PATH": "/usr/bin:/bin", "HF_TOKEN": "leak"},
    ).stdout
    shell = dict(line.split("=", 1) for line in out.splitlines() if "=" in line)
    assert "HF_TOKEN" not in shell
    for k, v in env.safe_env(online=False).items():
        assert shell.get(k) == v, k


def test_running_python_is_audiolab_venv():
    assert sys.version_info[:2] == (3, 12)
    assert sys.prefix == str(env.VENV)
