"""Critic weights in the shared Hugging Face cache (L3 audiobox, L4 CLAP x2 + AST).

  run.sh models                      check the offline cache (no network; default)
  AUDIOLAB_ONLINE=1 run.sh models --download   fetch the pinned files once, without a token

Only the files the critic reads are fetched (allow_patterns), at the pinned revision itself (never
`main`), so a moved `main` can neither add files nor move refs/main under the critic (§10.8). The
critic loads the same pinned revision (critic.learned.revision). No token is ever
used (HF_HUB_DISABLE_IMPLICIT_TOKEN=1, token=False). Generative models (Stable Audio 3, ACE-Step)
are not here: they wait for the owner's step 0 (AUDIO_PIPELINE.md §10.1, §15.1).
"""
from __future__ import annotations

import argparse
import os
import sys

from common import env

TOKENIZER = ["config.json", "merges.txt", "preprocessor_config.json", "special_tokens_map.json",
             "tokenizer.json", "tokenizer_config.json", "vocab.json"]
# repo -> (pinned revision, files, licence)
MODELS = {
    "facebook/audiobox-aesthetics": ("9b1dd8e5df9af7216e836a98974fe3b82c56ded6",
                                     ["config.json", "model.safetensors"], "CC-BY-4.0"),
    "laion/clap-htsat-unfused": ("8fa0f1c6d0433df6e97c127f64b2a1d6c0dcda8a",
                                 TOKENIZER + ["pytorch_model.bin"], "Apache-2.0"),
    "laion/larger_clap_general": ("ada0c23a36c4e8582805bb38fec3905903f18b41",
                                  TOKENIZER + ["pytorch_model.bin"], "Apache-2.0"),
    "MIT/ast-finetuned-audioset-10-10-0.4593": ("f826b80d28226b62986cc218e5cec390b1096902",
                                                ["config.json", "model.safetensors", "preprocessor_config.json"],
                                                "BSD-3-Clause"),
}


def snapshot(repo: str, revision: str):
    return env.HF_HOME / "hub" / f"models--{repo.replace('/', '--')}" / "snapshots" / revision


def check() -> list[str]:
    """The pinned snapshot of every critic model has its files (refs/main is only reported: the
    critic loads the pinned revision, so a moved main does not change what it hears)."""
    problems = []
    for repo, (rev, files, lic) in MODELS.items():
        snap = snapshot(repo, rev)
        ref = snap.parent.parent / "refs" / "main"
        missing = [f for f in files if not (snap / f).exists()]
        size = sum((snap / f).stat().st_size for f in files if (snap / f).exists())
        main_rev = ref.read_text().strip() if ref.is_file() else None
        state = "đủ" if not missing else f"thiếu {', '.join(missing)}"
        if main_rev and main_rev != rev:
            state += f"; chú ý: refs/main = {main_rev[:10]} (bộ chấm vẫn nạp bản đã ghim)"
        print(f"{repo}@{rev[:10]}  {lic:<12} {size / 1e6:8.1f} MB  {state}")
        if missing:
            problems.append(repo)
    return problems


def download() -> list[str]:
    if os.environ.get("AUDIOLAB_ONLINE") != "1":
        sys.exit("tải mô hình cần AUDIOLAB_ONLINE=1 (một lần, rồi quay về offline)")
    for k in env.TOKEN_VARS:
        os.environ.pop(k, None)
    from huggingface_hub import snapshot_download

    bad = []
    for repo, (rev, files, _lic) in MODELS.items():
        path = snapshot_download(repo, revision=rev, allow_patterns=files, token=False)
        got = os.path.basename(path)
        print(f"{repo}@{rev[:10]}: {path}")
        if got != rev:
            print(f"  CẢNH BÁO: tải về {got}, khác bản đã ghim {rev}", file=sys.stderr)
            bad.append(repo)
    return bad


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="models", description="Trọng số của bộ phê bình trong cache Hugging Face chung.")
    ap.add_argument("--download", action="store_true", help="tải (cần AUDIOLAB_ONLINE=1)")
    a = ap.parse_args(argv)
    env.apply()
    if a.download:
        if download():
            return 1
    problems = check()
    print("Cache mô hình: " + ("ĐỦ" if not problems else f"THIẾU ({len(problems)} kho)"))
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
