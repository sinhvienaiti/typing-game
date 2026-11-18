"""Opt-in real-browser check (Chrome over CDP): AUDIOLAB_BROWSER=1 pnpm audio:test."""
import os
import shutil
from pathlib import Path

import pytest

CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")


@pytest.mark.skipif(os.environ.get("AUDIOLAB_BROWSER") != "1", reason="đặt AUDIOLAB_BROWSER=1 để thử bằng Chrome thật")
@pytest.mark.skipif(not (CHROME.exists() or os.environ.get("CHROME_PATH")) or not shutil.which("node"),
                    reason="cần Chrome và Node")
def test_board_in_real_chrome():
    from board.browser_check import run

    assert run() == 0
