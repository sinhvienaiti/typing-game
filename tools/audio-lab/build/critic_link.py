"""Critic results -> licence log (§10.6, §10.7).

The critic never writes a ledger: each of its JSON files lists `ai_steps` (step + model repo).
This module matches those files to SOURCES.json records by SHA-256 (runtime OGG or master WAV),
records the steps with ledger.mark_ai_step, and adds one `model` row per critic model so
licence_check can see which weights heard which file.
"""
from __future__ import annotations

import json
from pathlib import Path

from build import ledger

# Critic weights (AudioLab README, HF cache revision at download). Local scoring only.
CRITIC_MODELS = {
    "facebook/audiobox-aesthetics": ("CC-BY-4.0", "https://huggingface.co/facebook/audiobox-aesthetics"),
    "laion/clap-htsat-unfused": ("Apache-2.0", "https://huggingface.co/laion/clap-htsat-unfused"),
    "laion/larger_clap_general": ("Apache-2.0", "https://huggingface.co/laion/larger_clap_general"),
    "MIT/ast-finetuned-audioset-10-10-0.4593": ("BSD-3-Clause",
                                                "https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593"),
}


def hf_weights_sha(repo: str, revision: str) -> str | None:
    """sha256 of the weights blob in the offline HF cache (the blob file name)."""
    from common import env

    snap = env.HF_HOME / "hub" / f"models--{repo.replace('/', '--')}" / "snapshots" / revision
    for name in ("model.safetensors", "pytorch_model.bin"):
        p = snap / name
        if p.is_symlink():
            blob = Path(p.readlink()).name
            if len(blob) == 64:
                return blob
    return None


def critic_steps(critic_dirs: list[Path]) -> dict[str, list[dict]]:
    """sha256 of each scored file -> its ai_steps, from audiolab.critic.file/1 JSON files."""
    out: dict[str, list[dict]] = {}
    for d in critic_dirs:
        for p in sorted(Path(d).expanduser().glob("*.json")):
            if p.name.startswith("_"):
                continue
            try:
                doc = json.loads(p.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                continue
            if not isinstance(doc, dict) or not str(doc.get("schema", "")).startswith("audiolab.critic.file/"):
                continue
            sha = (doc.get("file") or {}).get("sha256")
            steps = [s for s in doc.get("ai_steps") or [] if isinstance(s, dict) and s.get("step")]
            if sha and steps:
                have = out.setdefault(sha, [])
                have += [s for s in steps if s not in have]
    return out


def model_rows(models: set[str], date: str | None = None) -> list[dict]:
    """One ledger row per 'repo@revision' the critic logged (the revision it loaded, not refs/main)."""
    rows = []
    for mid in sorted(models):
        resolved = ledger.resolve_model(mid)
        repo = resolved.split("@", 1)[0]
        lic, url = CRITIC_MODELS.get(repo, (None, None))
        if lic is None or "@" not in resolved:
            raise LookupError(f"mô hình {mid}: không rõ giấy phép hoặc revision đã ghim")
        rev = resolved.split("@", 1)[1]
        sha = hf_weights_sha(repo, rev)
        if not sha:
            raise LookupError(f"mô hình {repo}@{rev}: không thấy trọng số trong HF cache")
        rows.append(ledger.model_row(repo, rev, lic, url, sha, "critic", date))
    return rows


def apply(sources_path: Path, critic_dirs: list[Path], rows_path: Path | None = None) -> dict:
    """Mark critic AI steps on matching records; add model rows to `rows_path` (licences jsonl).

    Returns {"files": n records touched, "steps": n steps added, "models": [...], "unmatched": n}."""
    sources_path = Path(sources_path)
    recs = ledger.records(ledger.read_sources(sources_path))
    by_sha: dict[str, list[str]] = {}
    for key, rec in recs.items():
        for h in {rec.get("sha256"), rec.get("masterSha256")} - {None}:
            by_sha.setdefault(h, []).append(key)
    steps = critic_steps(critic_dirs)
    touched, added, used, unmatched = set(), 0, set(), 0
    for sha, items in steps.items():
        keys = by_sha.get(sha)
        if not keys:
            unmatched += 1
            continue
        for s in items:
            n = ledger.mark_ai_step(sources_path, s["step"], keys, s.get("model"))
            added += n
            touched.update(keys)
            if s.get("model"):
                used.add(ledger.resolve_model(s["model"]))
    rows = model_rows(used) if used else []
    if rows and rows_path is not None:
        ledger.append_rows(Path(rows_path), rows)
    return {"files": len(touched), "steps": added, "models": sorted({m.split("@", 1)[0] for m in used}),
            "revisions": sorted(used), "unmatched": unmatched,
            "modelRows": [r["key"] for r in rows]}
