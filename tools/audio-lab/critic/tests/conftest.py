import json
import os

import pytest

from critic import pipeline
from critic.tests import synth


def pytest_configure(config):
    config.addinivalue_line("markers", "models: loads audiobox/CLAP/AST from the offline cache (AUDIOLAB_TEST_MODELS=1)")


def pytest_collection_modifyitems(config, items):
    if os.environ.get("AUDIOLAB_TEST_MODELS") == "1":
        return
    skip = pytest.mark.skip(reason="mô hình học máy: đặt AUDIOLAB_TEST_MODELS=1 để chạy")
    for it in items:
        if "models" in it.keywords:
            it.add_marker(skip)


@pytest.fixture(scope="session")
def synth_run(tmp_path_factory):
    """The synthetic set scored once with the fast layers (no models, no PNG)."""
    root = tmp_path_factory.mktemp("critic")
    files = synth.make_set(root)
    out = root / "out"
    batch = pipeline.run([str(root / "in")], spec_path=str(root / "cards.yaml"), out_dir=out,
                         opts=pipeline.Options(layers=("L1", "L1b", "L2"), quiet=True))
    res = {}
    for name in files:
        res[name] = json.loads((out / f"{name}.json").read_text(encoding="utf-8"))
    return {"root": root, "files": files, "batch": batch, "res": res, "out": out}
