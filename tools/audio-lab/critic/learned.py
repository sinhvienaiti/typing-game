"""Learned layers: L3 audiobox-aesthetics, L4 CLAP + AST, L5 reference distance (§4.1, §4.4).

They only rank or flag; they never block. Models load lazily, once per process, from the offline
Hugging Face cache (HF_HUB_OFFLINE=1, no token; see common/env.py). MPS when available, CPU
fallback (AUDIOLAB_DEVICE=cpu forces CPU). Sounds shorter than 300 ms, and longer ones whose
card sets critic.loop_eval.enabled, are scored on a 3-4 s repetition at the game rhythm (§4.4).
Files the AI policy forbids never reach a model (§10.2, critic/policy.py).
"""
from __future__ import annotations

import os
import time
from dataclasses import dataclass, field

import numpy as np

from . import audio as A
from . import vocab as V
from .audio import fnum
from .spec import Spec
from .thresholds import L2, LEARNED

AES_REPO = "facebook/audiobox-aesthetics"
CLAP_MODELS = ("laion/clap-htsat-unfused", "laion/larger_clap_general")
L5_MODEL = "laion/larger_clap_general"
AST_MODEL = "MIT/ast-finetuned-audioset-10-10-0.4593"
LONG_S = 120.0                 # ours: longer files are scored on fixed windows (time and RAM, §4.1)
LONG_WINDOWS = (6, 10.0)       # ... six evenly spaced 10 s windows


def revision(repo: str) -> str | None:
    """The pinned Hugging Face revision (common/fetch_models.MODELS, §10.8); models load exactly it."""
    from common.fetch_models import MODELS
    entry = MODELS.get(repo)
    return entry[0] if entry else None


def pinned_id(repo: str) -> str:
    rev = revision(repo)
    return f"{repo}@{rev}" if rev else repo


def windows(x: np.ndarray, n_win: int, k: int) -> list[np.ndarray]:
    """k evenly spaced windows of exactly n_win samples (deterministic; the whole signal if shorter)."""
    if len(x) <= n_win:
        return [x]
    k = max(1, min(k, int(np.ceil(len(x) / n_win))))
    starts = np.linspace(0, len(x) - n_win, k).round().astype(int)
    return [x[s: s + n_win] for s in starts]


def ai_steps(r: dict) -> list[dict]:
    """Models that heard this file, as SOURCES.json `aiSteps` names (build.ledger.mark_ai_step)."""
    out: list[dict] = []

    def add(step, model):
        if {"step": step, "model": model} not in out:
            out.append({"step": step, "model": model})

    # model ids carry the pinned revision the critic loaded (build.critic_link records exactly it)
    if (r.get("L3") or {}).get("available"):
        add("critic:audiobox", pinned_id(AES_REPO))
    l4 = r.get("L4") or {}
    if l4.get("available"):
        for mid in (l4.get("clap") or {}).get("models") or []:
            add("critic:clap", pinned_id(mid))
        if (l4.get("ast") or {}).get("available"):
            add("critic:ast", pinned_id(AST_MODEL))
    if (r.get("L5") or {}).get("available"):
        add("critic:clap", pinned_id(L5_MODEL))
    return out

_CACHE: dict = {}
LOG: dict = {}


def _quiet() -> None:
    """Silence torch/transformers chatter that is not ours to fix (deprecations, macOS notes)."""
    import logging
    import warnings
    warnings.filterwarnings("ignore", category=FutureWarning)
    warnings.filterwarnings("ignore", category=UserWarning, module=r"torch\..*")
    for name in ("torch.distributed.elastic", "transformers", "audiobox_aesthetics"):
        logging.getLogger(name).setLevel(logging.ERROR)
    os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")


def no_ai(path) -> bool:
    from .policy import path_forbidden
    return path_forbidden(path)


def device() -> str:
    _quiet()
    import torch
    want = os.environ.get("AUDIOLAB_DEVICE", "auto").lower()
    mps = torch.backends.mps.is_available()
    if want == "cpu" or (want == "mps" and not mps):
        return "cpu"
    return "mps" if mps else "cpu"


# ---------------------------------------------------------------- inputs
def repetition(sigs: list[np.ndarray], sr: int, rate_hz: float) -> np.ndarray:
    """~10 plays at the game rhythm, rotating variants, 3-4 s long (§4.4)."""
    interval = 1.0 / rate_hz if rate_hz and rate_hz > 0 else 0.35
    total = float(np.clip(L2["rep_plays"] * interval, L2["rep_min_s"], L2["rep_max_s"]))
    n = int(total * sr)
    out = np.zeros(n, dtype=np.float32)
    pos, k = 0, 0
    while pos < n:
        s = sigs[k % len(sigs)]
        m = min(len(s), n - pos)
        out[pos: pos + m] += s[:m]
        pos += max(1, int(interval * sr))
        k += 1
    return out


@dataclass
class Item:
    key: str
    audio: A.Audio
    spec: Spec
    variants: list = field(default_factory=list)    # other Audio of the same variant set
    _cache: dict = field(default_factory=dict)

    @property
    def short(self) -> bool:
        """Scored on the repetition: shorter than 300 ms (§4.4), or the card asks (critic.loop_eval.enabled)."""
        return self.audio.duration < L2["short_s"] or self.spec.loop_eval

    @property
    def long(self) -> bool:
        return self.audio.duration > LONG_S

    @property
    def input_kind(self) -> str:
        return "repetition" if self.short else (f"{LONG_WINDOWS[0]} đoạn {LONG_WINDOWS[1]:g} s" if self.long else "file")

    def mono(self, sr: int) -> np.ndarray:
        if sr not in self._cache:
            if self.long:            # fixed windows, joined: bounded time and memory for L3/AST
                x = A.resample(self.audio.mono, self.audio.sr, sr).astype(np.float32)
                x = np.concatenate(windows(x, int(LONG_WINDOWS[1] * sr), LONG_WINDOWS[0]))
            else:
                sigs = [A.resample(v.mono, v.sr, sr).astype(np.float32) for v in [self.audio, *self.variants]]
                x = repetition(sigs, sr, self.spec.rate_hz) if self.short else sigs[0]
            self._cache[sr] = x.astype(np.float32)
        return self._cache[sr]


def _err(e: Exception) -> str:
    return f"{type(e).__name__}: {str(e)[:300]}"


# ---------------------------------------------------------------- L3 audiobox-aesthetics
def _aes():
    if "aes" not in _CACHE:
        t0 = time.time()
        from audiobox_aesthetics.infer import AesPredictor
        from audiobox_aesthetics.model.aes import AXES_NAME, AesMultiOutput, Normalize
        import torch
        from common.fetch_models import snapshot
        snap = snapshot(AES_REPO, revision(AES_REPO))
        if not (snap / "model.safetensors").is_file():
            raise FileNotFoundError(f"thiếu bản đã ghim {pinned_id(AES_REPO)} trong cache (run.sh models)")

        class _Pinned(AesPredictor):
            """AesPredictor loads `main`; this one loads the pinned snapshot folder (§10.8)."""

            def setup_model(self):
                self.device = torch.device(device())
                model = AesMultiOutput.from_pretrained(str(snap))
                model.to(self.device)
                model.eval()
                self.model = model
                self.target_transform = {ax: Normalize(mean=model.target_transform[ax]["mean"],
                                                       std=model.target_transform[ax]["std"]) for ax in AXES_NAME}

        pred = _Pinned(checkpoint_pth=None, data_col="path")
        _CACHE["aes"] = pred
        LOG["aes"] = {"load_s": fnum(time.time() - t0), "device": str(pred.device), "repo": pinned_id(AES_REPO)}
    return _CACHE["aes"]


def run_l3(items: list[Item]) -> dict[str, dict]:
    _quiet()
    import torch
    try:
        pred = _aes()
    except Exception as e:
        return {it.key: {"available": False, "reason": _err(e)} for it in items}
    out = {}
    t0 = time.time()
    for it in items:
        x = it.mono(16000)
        batch = [{"path": torch.from_numpy(x[None, :].copy()), "sample_rate": 16000}]
        try:
            r = pred.forward(batch)[0]
        except RuntimeError:          # MPS op missing -> CPU once, then retry
            pred.model.to("cpu")
            pred.device = torch.device("cpu")
            LOG["aes"]["device"] = "cpu (fallback)"
            r = pred.forward(batch)[0]
        out[it.key] = {"available": True, "scores": {k: fnum(v, 3) for k, v in r.items()},
                       "input": it.input_kind}
    LOG.setdefault("aes", {})["s_per_file"] = fnum((time.time() - t0) / max(1, len(items)), 3)
    return out


# ---------------------------------------------------------------- CLAP
class Clap:
    def __init__(self, model_id: str):
        import torch
        from transformers import ClapModel, ClapProcessor
        t0 = time.time()
        self.id = model_id
        rev = revision(model_id)
        self.model = ClapModel.from_pretrained(model_id, revision=rev).eval()
        self.proc = ClapProcessor.from_pretrained(model_id, revision=rev)
        self.dev = device()
        try:
            self.model.to(self.dev)
        except Exception:
            self.dev = "cpu"
        self.sr = self.proc.feature_extractor.sampling_rate
        self.scale = float(self.model.logit_scale_a.exp().item()) if hasattr(self.model, "logit_scale_a") else 100.0
        self._text: dict[str, "torch.Tensor"] = {}
        self.max_len = int(getattr(self.proc.feature_extractor, "nb_max_samples", 10 * self.sr))
        LOG[f"clap:{model_id}"] = {"load_s": fnum(time.time() - t0), "device": self.dev, "revision": rev}

    @staticmethod
    def _pool(e):
        import torch
        if not torch.is_tensor(e):
            e = e.pooler_output if hasattr(e, "pooler_output") else e[0]
        return torch.nn.functional.normalize(e, dim=-1)

    def text(self, texts: list[str]):
        import torch
        miss = [t for t in texts if t not in self._text]
        if miss:
            tok = self.proc.tokenizer(miss, padding=True, return_tensors="pt").to(self.dev)
            with torch.no_grad():
                e = self._pool(self.model.get_text_features(**tok)).cpu()
            for t, v in zip(miss, e):
                self._text[t] = v
        return torch.stack([self._text[t] for t in texts])

    def audio(self, x: np.ndarray):
        """Unit audio embedding. Inputs longer than the extractor's 10 s are cut into fixed, evenly spaced
        10 s windows whose embeddings are averaged: the extractor's own `rand_trunc` picks a random
        crop (np.random), which made scores of a 15 s file differ run to run."""
        import torch
        segs = windows(np.asarray(x, dtype=np.float32), self.max_len, LONG_WINDOWS[0])
        embs = [self._embed(s) for s in segs]
        if len(embs) == 1:
            return embs[0]
        return torch.nn.functional.normalize(torch.stack(embs).mean(dim=0), dim=-1)

    def _embed(self, x: np.ndarray):
        import torch
        state = np.random.get_state()          # belt and braces: no global RNG use leaks into scores
        np.random.seed(0)
        try:
            feats = self.proc.feature_extractor([x], sampling_rate=self.sr, return_tensors="pt")
        finally:
            np.random.set_state(state)
        try:
            with torch.no_grad():
                f = {k: v.to(self.dev) for k, v in feats.items()}
                return self._pool(self.model.get_audio_features(**f)).cpu()[0]
        except RuntimeError:
            if self.dev == "cpu":
                raise
            self._to_cpu()
            return self._embed(x)

    def _to_cpu(self) -> None:
        """MPS op missing: move to CPU once (text embeddings are cached on CPU already)."""
        self.model.to("cpu")
        self.dev = "cpu"
        LOG[f"clap:{self.id}"]["device"] = "cpu (fallback)"


def _clap(model_id: str) -> Clap:
    if model_id not in _CACHE:
        _CACHE[model_id] = Clap(model_id)
    return _CACHE[model_id]


def _ast():
    if "ast" not in _CACHE:
        t0 = time.time()
        from transformers import ASTFeatureExtractor, ASTForAudioClassification
        rev = revision(AST_MODEL)
        fe = ASTFeatureExtractor.from_pretrained(AST_MODEL, revision=rev)
        model = ASTForAudioClassification.from_pretrained(AST_MODEL, revision=rev).eval()
        dev = device()
        try:
            model.to(dev)
        except Exception:
            dev = "cpu"
        _CACHE["ast"] = (fe, model, dev)
        LOG["ast"] = {"load_s": fnum(time.time() - t0), "device": dev, "repo": pinned_id(AST_MODEL)}
    return _CACHE["ast"]


def run_l4(items: list[Item], clap_models=CLAP_MODELS) -> tuple[dict[str, dict], dict[str, np.ndarray]]:
    """CLAP zero-shot (ensemble of the given models) and AST tags. Returns (results, L5 embeddings)."""
    _quiet()
    import torch
    out: dict[str, dict] = {it.key: {"available": True, "clap": {}, "ast": {}, "flags": []} for it in items}
    embeds: dict[str, np.ndarray] = {}
    claps = []
    for mid in clap_models:
        try:
            claps.append(_clap(mid))
        except Exception as e:
            for it in items:
                out[it.key]["clap"].setdefault("errors", []).append(f"{mid}: {_err(e)}")
    t0 = time.time()
    for it in items:
        r = out[it.key]
        sp = it.spec
        labels = V.labels_for(sp.game, sp.clap_labels)
        expected = list(sp.clap_expected or V.GROUP_EXPECTED.get(sp.group, []))
        labels += [e for e in expected if e not in labels]
        pairs = V.contrast_for(sp.game, sp.group, sp.clap_contrast)
        if claps:
            sims = np.zeros(len(labels))
            pair_p = np.zeros(len(pairs))
            pam = []
            aud = {}
            for c in claps:
                a = aud[c.id] = c.audio(it.mono(c.sr))
                if c.id == L5_MODEL:
                    embeds[it.key] = a.numpy()
                s = (c.text(labels) @ a).numpy()
                sims += s / len(claps)
                for j, (good, bad) in enumerate(pairs):
                    ps = torch.softmax(c.text([good, bad]) @ a * c.scale, dim=-1).numpy()
                    pair_p[j] += ps[1] / len(claps)
                if not sp.dirty:
                    pam.append(float(torch.softmax(c.text(list(V.PAM_PAIR)) @ a * c.scale, dim=-1)[0]))
            order = np.argsort(-sims)
            top = [(labels[i], fnum(sims[i], 3)) for i in order[: LEARNED["clap_topk"]]]
            r["clap"].update({"models": [c.id for c in claps], "revisions": {c.id: revision(c.id) for c in claps},
                              "top3": top,
                              "expected": expected, "intent": sp.intent,
                              "contrast": [{"good": g, "bad": b, "p_bad": fnum(p, 3)} for (g, b), p in zip(pairs, pair_p)],
                              "pam_clean": fnum(np.mean(pam), 3) if pam else None,
                              "input": it.input_kind})
            if sp.intent:
                r["clap"]["intent_cos_info_only"] = fnum(float(np.mean([(c.text([sp.intent]) @ aud[c.id]).item() for c in claps])), 3)
            topl = [t for t, _ in top]
            if expected and not any(e in topl for e in expected):
                r["flags"].append({"layer": "L4", "id": "clap_expected_missing", "value": topl, "threshold": expected,
                                   "msg_vi": f"CLAP không xếp nhãn mong đợi vào top-3 (top-1: “{topl[0]}”)"})
            for (g, b), p in zip(pairs, pair_p):
                if p > 0.5:
                    r["flags"].append({"layer": "L4", "id": "clap_material", "value": fnum(p, 3), "threshold": 0.5,
                                       "msg_vi": f"CLAP nghe giống “{b}” hơn “{g}” (sai chất liệu?)"})
    LOG["clap_s_per_file"] = fnum((time.time() - t0) / max(1, len(items)), 3)
    try:
        fe, model, dev = _ast()
    except Exception as e:
        for it in items:
            out[it.key]["ast"] = {"available": False, "reason": _err(e)}
        fe = None
    t0 = time.time()
    if fe is not None:
        labels = model.config.id2label
        for it in items:
            r, sp = out[it.key], it.spec
            feats = fe(it.mono(16000), sampling_rate=16000, return_tensors="pt")
            try:
                with torch.no_grad():
                    p = torch.sigmoid(model(**{k: v.to(dev) for k, v in feats.items()}).logits[0]).cpu()
            except RuntimeError:
                if dev == "cpu":
                    raise
                dev = "cpu"                       # MPS op missing: CPU from here on
                model.to(dev)
                _CACHE["ast"] = (fe, model, dev)
                LOG["ast"]["device"] = "cpu (fallback)"
                with torch.no_grad():
                    p = torch.sigmoid(model(**feats).logits[0]).cpu()
            top = torch.topk(p, 5)
            tags = [(labels[int(j)], fnum(v, 3)) for v, j in zip(top.values, top.indices)]
            exp = list(sp.ast_expected or V.AST_EXPECTED.get(sp.group, []))
            r["ast"] = {"available": True, "top5": tags, "expected": exp, "input": it.input_kind}
            hit = None
            for t, v in tags:
                if t in sp.ast_forbid and (t == tags[0][0] or v >= LEARNED["ast_forbid_min"]):
                    hit = t
                    r["flags"].append({"layer": "L4", "id": "ast_forbidden", "value": [t, v], "threshold": sp.ast_forbid,
                                       "msg_vi": f"AST gắn nhãn không mong muốn “{t}” ({v:.2f})".replace(".", ",")})
                    break
            if tags[0][0] in V.SPEECH and sp.group not in V.VOICE_GROUPS and hit != tags[0][0]:
                r["flags"].append({"layer": "L4", "id": "ast_speech", "value": tags[0], "threshold": "không phải Speech",
                                   "msg_vi": f"AST gắn nhãn tiếng nói “{tags[0][0]}” cho một SFX"})
            if tags[0][1] < LEARNED["ast_low_conf"]:
                r["flags"].append({"layer": "L4", "id": "ast_low_conf", "value": tags[0][1],
                                   "threshold": LEARNED["ast_low_conf"],
                                   "msg_vi": f"AST khó nhận ra âm này (tự tin cao nhất {tags[0][1]:.2f})".replace(".", ",")})
            if exp and not any(t in exp and v >= LEARNED["ast_expected_min"] for t, v in tags):
                r["flags"].append({"layer": "L4", "id": "ast_expected_missing", "value": [t for t, _ in tags],
                                   "threshold": exp, "msg_vi": "AST không thấy nhãn mong đợi trong top-5"})
    LOG["ast_s_per_file"] = fnum((time.time() - t0) / max(1, len(items)), 3)
    for r in out.values():
        r["score"] = 1.0 - min(1.0, len(r["flags"]) / 2.0)
    return out, embeds


# ---------------------------------------------------------------- L5 reference distance
def embed(items: list[Item]) -> dict[str, np.ndarray]:
    _quiet()
    c = _clap(L5_MODEL)
    return {it.key: c.audio(it.mono(c.sr)).numpy() for it in items}


def kad(x: np.ndarray, y: np.ndarray) -> float:
    """Kernel audio distance: unbiased MMD^2, Gaussian kernel, median-distance bandwidth, x1000."""
    z = np.vstack([x, y])
    d2 = ((z[:, None, :] - z[None, :, :]) ** 2).sum(-1)
    bw = np.median(d2[np.triu_indices(len(z), 1)]) + 1e-12
    k = np.exp(-d2 / bw)
    n, m = len(x), len(y)
    kxx, kyy, kxy = k[:n, :n], k[n:, n:], k[:n, n:]
    mmd = ((kxx.sum() - np.trace(kxx)) / (n * (n - 1)) + (kyy.sum() - np.trace(kyy)) / (m * (m - 1))
           - 2 * kxy.mean())
    return float(mmd * 1000)


def run_l5(cand: dict[str, np.ndarray], refs: dict[str, np.ndarray]) -> tuple[dict[str, dict], dict]:
    R = np.stack(list(refs.values()))
    S = R @ R.T
    np.fill_diagonal(S, -np.inf)
    nn = S.max(axis=1)
    p10 = float(np.percentile(nn, 10))
    out = {}
    for k, e in cand.items():
        sims = R @ e
        v = float(sims.max())
        r = {"available": True, "nearest_sim": fnum(v, 4), "ref_p10": fnum(p10, 4), "n_refs": len(refs),
             "nearest_ref": list(refs)[int(np.argmax(sims))], "flags": []}
        if v < p10:
            r["flags"].append({"layer": "L5", "id": "ref_far", "value": fnum(v, 4), "threshold": fnum(p10, 4),
                               "msg_vi": "xa bộ âm đã duyệt hơn mức P10 trong họ"})
        out[k] = r
    batch = {"n_refs": len(refs)}
    if len(refs) >= LEARNED["kad_min"] and len(cand) >= 2:
        batch["kad_x1000"] = fnum(kad(np.stack(list(cand.values())), R), 4)
    return out, batch
