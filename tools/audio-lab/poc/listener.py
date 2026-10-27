"""listener.py - small local audio-language model that "describes" a sound in words.

Model: mispeech/midashenglm-0.6b-fp32 (Xiaomi, Apache-2.0, trust_remote_code; the
remote .py files were read before running: they import only torch/torchaudio/transformers/numpy).

Usage: HF_HOME=<cache> python -I listener.py --manifest manifest.json --out out/listener.json
"""
import argparse
import json
import os
import time

import librosa
import numpy as np
import soundfile as sf
import torch
from transformers import AutoModelForCausalLM, AutoProcessor, AutoTokenizer

MID = "mispeech/midashenglm-0.6b-fp32"
PROMPTS = {
    "caption": "Write the detailed caption about this audio within 1-2 sentences.",
    "quality": "Is this sound clean, or is it distorted, clipped or muffled? Answer in one short sentence.",
    "punch": "On a scale from 1 to 10, how punchy and powerful is this sound? Reply with the number first, then a short reason.",
    "clean_yn": "Is this sound clean and free of distortion? Answer yes or no.",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    items = json.load(open(a.manifest))
    if a.limit:
        items = items[: a.limit]
    dev = os.environ.get("LISTENER_DEVICE") or ("mps" if torch.backends.mps.is_available() else "cpu")
    t0 = time.time()
    model = AutoModelForCausalLM.from_pretrained(MID, trust_remote_code=True).to(dev).eval()
    tok = AutoTokenizer.from_pretrained(MID, trust_remote_code=True)
    proc = AutoProcessor.from_pretrained(MID, trust_remote_code=True)
    log = {"load_s": round(time.time() - t0, 1), "device": dev}
    res = {}
    per = []
    for it in items:
        x, sr = sf.read(it["path"], always_2d=True, dtype="float32")
        x = librosa.resample(x.mean(axis=1), orig_sr=sr, target_sr=16000)
        if len(x) < 16000:  # clips < ~0.2 s crash the remote code (audio-token span mismatch): pad to 1 s
            x = np.pad(x, (0, 16000 - len(x)))
        out = {}
        for key, prompt in PROMPTS.items():
            # Same string the repo's chat_template.jinja renders; built by hand because the
            # remote processor's apply_chat_template path breaks under transformers 5.x
            # ("got multiple values for keyword argument 'sampling_rate'").
            text = ("<|im_start|>user\n" + prompt + "<|audio_bos|><|AUDIO|><|audio_eos|><|im_end|>\n"
                    "<|im_start|>assistant\n")
            t1 = time.time()
            with torch.no_grad():
                inp = proc(text=[text], audio=[x.astype(np.float32)])
                inp = inp.to(device=model.device)
                if "input_values" in inp:
                    inp["input_values"] = inp["input_values"].to(model.dtype)
                gen = model.generate(**inp, do_sample=False, max_new_tokens=60, repetition_penalty=1.05)
            n_in = inp["input_ids"].shape[1]
            # the remote generate() runs on inputs_embeds and returns ONLY new tokens;
            # strip the prompt only if it is actually echoed back
            echoed = gen.shape[1] > n_in and torch.equal(gen[:, :n_in].cpu(), inp["input_ids"].cpu())
            g = gen[:, n_in:] if echoed else gen
            txt = tok.batch_decode(g, skip_special_tokens=True)[0].strip()
            per.append(time.time() - t1)
            out[key] = txt
        res[os.path.basename(it["path"])] = out
        print(os.path.basename(it["path"]), json.dumps(out, ensure_ascii=False))
    log["s_per_prompt"] = round(float(np.mean(per)), 2)
    res["_log"] = log
    json.dump(res, open(a.out, "w"), indent=1, ensure_ascii=False)
    print(log)


if __name__ == "__main__":
    main()
