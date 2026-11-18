"""critics.py - learned "AI ears" for game SFX (no account, no token).

Critics:
  aes   Meta audiobox-aesthetics (CE, CU, PC, PQ; 1-10 scale)       facebook/audiobox-aesthetics
  clap  LAION CLAP prompt match + zero-shot quality/category probes  laion/clap-htsat-unfused,
                                                                     laion/larger_clap_general
  ast   AudioSet tagger (527 classes) for category recognition       MIT/ast-finetuned-audioset-10-10-0.4593

Usage:
  HF_HOME=<cache> python -I critics.py --manifest manifest.json --out out/critics.json [--only aes,clap,ast]
manifest.json: [{"path": ..., "intent": "text prompt the sound was made for"}, ...]
"""
import argparse
import json
import os
import time

import numpy as np
import soundfile as sf
import torch
import librosa

DEVICE = "mps" if torch.backends.mps.is_available() else "cpu"

QUALITY_PROBES = [
    "a punchy, powerful, high quality impact sound effect",
    "a weak, thin, quiet little click",
    "a harsh, distorted, clipped, overdriven noise",
    "a muddy, boomy, muffled low thud",
]
# PAM-style good/bad pair (Deshmukh et al. 2024, arXiv:2402.00282)
PAM_PAIR = ["the sound is clear and clean.", "the sound is noisy and with artifacts."]
CATEGORY_PROBES = [
    "a sci-fi laser gun shot", "a big explosion", "a metal impact clang", "a wooden hit knock",
    "a bronze bell strike", "a body punch hit", "a fire breath whoosh", "a low engine hum loop",
    "an industrial machine drone", "a user interface click",
]


def load_mono(path, sr):
    x, s = sf.read(path, always_2d=True, dtype="float32")
    x = x.mean(axis=1)
    if s != sr:
        x = librosa.resample(x, orig_sr=s, target_sr=sr)
    return x.astype(np.float32)


def dir_size_mb(path):
    tot = 0
    for root, _, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            if not os.path.islink(fp):
                tot += os.path.getsize(fp)
    return round(tot / 1e6, 1)


# ---------------------------------------------------------------- audiobox-aesthetics
def run_aes(items, log):
    from audiobox_aesthetics.infer import AesPredictor
    t0 = time.time()
    try:
        pred = AesPredictor(checkpoint_pth=None, data_col="path")
    except Exception as e:  # record the exact reason (gating, network, API change...)
        log["aes_error"] = repr(e)
        return {}
    log["aes_load_s"] = round(time.time() - t0, 2)
    log["aes_device"] = str(pred.device)
    out = {}
    per = []
    for it in items:
        x, s = sf.read(it["path"], always_2d=True, dtype="float32")
        wav = torch.from_numpy(x.T.copy())
        t1 = time.time()
        r = pred.forward([{"path": wav, "sample_rate": s}])[0]
        per.append(time.time() - t1)
        out[it["path"]] = {k: round(v, 3) for k, v in r.items()}
        # variant: tile short clips to >= 2 s so the 10 s window is less empty (diagnostic only)
        if x.shape[0] / s < 2.0:
            reps = int(np.ceil(2.0 * s / x.shape[0]))
            tiled = torch.from_numpy(np.tile(x.T, (1, reps)).copy())
            r2 = pred.forward([{"path": tiled, "sample_rate": s}])[0]
            out[it["path"]]["tiled2s"] = {k: round(v, 3) for k, v in r2.items()}
    log["aes_s_per_file"] = round(float(np.mean(per)), 3)
    return out


# ---------------------------------------------------------------- CLAP
def run_clap(items, model_id, log):
    from transformers import ClapModel, ClapProcessor
    t0 = time.time()
    try:
        model = ClapModel.from_pretrained(model_id).eval()
        proc = ClapProcessor.from_pretrained(model_id)
    except Exception as e:
        log[f"clap_error_{model_id}"] = repr(e)
        return {}
    dev = DEVICE
    try:
        model.to(dev)
    except Exception:
        dev = "cpu"
    log[f"clap_load_s_{model_id}"] = round(time.time() - t0, 2)
    log[f"clap_device_{model_id}"] = dev
    sr = proc.feature_extractor.sampling_rate

    def text_emb(texts):
        tok = proc.tokenizer(texts, padding=True, return_tensors="pt").to(dev)
        with torch.no_grad():
            e = model.get_text_features(**tok)
        if not torch.is_tensor(e):
            e = e.pooler_output if hasattr(e, "pooler_output") else e[0]
        return torch.nn.functional.normalize(e, dim=-1)

    q = text_emb(QUALITY_PROBES)
    pam = text_emb(PAM_PAIR)
    cat = text_emb(CATEGORY_PROBES)
    intents = text_emb([it["intent"] for it in items])
    scale = model.logit_scale_a.exp().item() if hasattr(model, "logit_scale_a") else 100.0
    out = {}
    per = []
    for i, it in enumerate(items):
        x = load_mono(it["path"], sr)
        t1 = time.time()
        feats = proc.feature_extractor([x], sampling_rate=sr, return_tensors="pt")
        feats = {k: v.to(dev) for k, v in feats.items()}
        with torch.no_grad():
            a = model.get_audio_features(**feats)
        if not torch.is_tensor(a):
            a = a.pooler_output if hasattr(a, "pooler_output") else a[0]
        a = torch.nn.functional.normalize(a, dim=-1)
        per.append(time.time() - t1)
        cos_int = float((a @ intents[i:i + 1].T).item())
        qs = (a @ q.T)[0]
        qp = torch.softmax(qs * scale, dim=-1)
        ps = torch.softmax((a @ pam.T)[0] * scale, dim=-1)
        cs = (a @ cat.T)[0]
        top = torch.topk(cs, 3)
        out[it["path"]] = {
            "intent_cos": round(cos_int, 4),
            "quality_cos": [round(float(v), 4) for v in qs],
            "quality_probs": [round(float(v), 3) for v in qp],
            "quality_top": QUALITY_PROBES[int(torch.argmax(qs))],
            "pam_clean_prob": round(float(ps[0]), 3),
            "category_top3": [(CATEGORY_PROBES[int(j)], round(float(cs[int(j)]), 3)) for j in top.indices],
        }
    log[f"clap_s_per_file_{model_id}"] = round(float(np.mean(per)), 3)
    return out


# ---------------------------------------------------------------- AST AudioSet tagger
def run_ast(items, log, model_id="MIT/ast-finetuned-audioset-10-10-0.4593"):
    from transformers import ASTFeatureExtractor, ASTForAudioClassification
    t0 = time.time()
    try:
        fe = ASTFeatureExtractor.from_pretrained(model_id)
        model = ASTForAudioClassification.from_pretrained(model_id).eval()
    except Exception as e:
        log["ast_error"] = repr(e)
        return {}
    dev = DEVICE
    model.to(dev)
    log["ast_load_s"] = round(time.time() - t0, 2)
    log["ast_device"] = dev
    labels = model.config.id2label
    out = {}
    per = []
    for it in items:
        x = load_mono(it["path"], 16000)
        t1 = time.time()
        inp = fe(x, sampling_rate=16000, return_tensors="pt")
        inp = {k: v.to(dev) for k, v in inp.items()}
        with torch.no_grad():
            logits = model(**inp).logits[0]
        p = torch.sigmoid(logits).cpu()
        per.append(time.time() - t1)
        top = torch.topk(p, 5)
        out[it["path"]] = [(labels[int(j)], round(float(v), 3)) for v, j in zip(top.values, top.indices)]
    log["ast_s_per_file"] = round(float(np.mean(per)), 3)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--only", default="aes,clap,ast")
    a = ap.parse_args()
    items = json.load(open(a.manifest))
    which = a.only.split(",")
    hf = os.environ.get("HF_HOME", os.path.expanduser("~/.cache/huggingface"))
    log = {"device": DEVICE, "torch": torch.__version__}
    res = {}
    if os.path.exists(a.out):
        res = json.load(open(a.out))
        log = res.get("_log", log)
    for name in which:
        before = dir_size_mb(hf) if os.path.exists(hf) else 0
        t0 = time.time()
        if name == "aes":
            res["aes"] = run_aes(items, log)
        elif name == "clap":
            res["clap_unfused"] = run_clap(items, "laion/clap-htsat-unfused", log)
            res["clap_larger_general"] = run_clap(items, "laion/larger_clap_general", log)
        elif name == "ast":
            res["ast"] = run_ast(items, log)
        log[f"{name}_total_s"] = round(time.time() - t0, 1)
        log[f"{name}_cache_growth_mb"] = round(dir_size_mb(hf) - before, 1)
        print(name, "done", log)
        res["_log"] = log
        json.dump(res, open(a.out, "w"), indent=1)


if __name__ == "__main__":
    main()
