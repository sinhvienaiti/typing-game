"""Build ~/AudioLab/libraries/index.json: one entry per library audio file.

  run.sh gen.index_library                    # incremental (reuses entries whose sha256 is unchanged)
  run.sh gen.index_library --verify-pitch     # also measure f0 of pitched samples (pYIN octave + FFT peak), slower
  run.sh gen.index_library --summary          # print the instrument table of the current index

Each entry: file, library, pack, licence, sha256, duration, sample rate, channels, inferred family
and tags; for instrument samples also instrument id, articulation, note/MIDI (confirmed with the
library's SFZ map when there is one), dynamics, velocity range, round robin and mic.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import soundfile as sf

from common import env
from gen import libraries as L
from sampler.naming import midi_to_note, parse_sample_name, slug
from sampler.sfz import parse_sfz

INDEX_VERSION = 1
SUSTAIN_RE = re.compile(r"(sus|trem|vib|roll|bowed|nv|long|mute)", re.I)

# Instrument family by instrument slug (VCSL / VSCO-2-CE).
FAMILY = {
    "dan-tranh": ("instrument/plucked-string", ["zither", "vietnamese"]),
    "folk-harp": ("instrument/plucked-string", ["harp"]),
    "concert-harp": ("instrument/plucked-string", ["harp"]),
    "harp": ("instrument/plucked-string", ["harp"]),
    "gong-1": ("instrument/gong", ["metal"]),
    "gong-2": ("instrument/gong", ["metal"]),
    "slit-drum": ("instrument/wood-perc", ["wood", "log-drum"]),
    "woodblock": ("instrument/wood-perc", ["wood"]),
    "anvil": ("instrument/metal-perc", ["metal"]),
    "brake-drum": ("instrument/metal-perc", ["metal"]),
    "hand-chimes": ("instrument/bell", ["metal", "chime"]),
    "tubular-bells-1": ("instrument/bell", ["metal", "chime"]),
    "tubular-bells-2": ("instrument/bell", ["metal", "chime"]),
    "frame-drum": ("instrument/drum", ["skin"]),
    "cello-section": ("instrument/bowed-string", ["strings"]),
    "flute": ("instrument/woodwind", ["wind"]),
    "f-horn": ("instrument/brass", ["horn"]),
    "tenor-trombone": ("instrument/brass", ["trombone"]),
    "timpani": ("instrument/drum", ["skin", "orchestral"]),
    "glock": ("instrument/mallet", ["metal"]),
    "marimba": ("instrument/mallet", ["wood"]),
    "xylo": ("instrument/mallet", ["wood"]),
    "percussion": ("instrument/percussion", []),
    "temp": ("instrument/percussion", []),
}
HS_FAMILY = {"chordophones": "instrument/string", "idiophones": "instrument/idiophone",
             "membranophones": "instrument/drum", "aerophones": "instrument/wind",
             "strings": "instrument/string", "woodwinds": "instrument/woodwind", "brass": "instrument/brass",
             "percussion": "instrument/percussion", "keys": "instrument/keys"}
# Kenney: keyword (lower-case stem) -> family. First match wins.
KENNEY_RULES = [
    (r"^footstep", "footstep"), (r"^impact", "impact"), (r"punch", "impact"),
    (r"explosion", "explosion"), (r"laser|phaser|^zap", "weapon/laser"),
    (r"engine|thruster", "engine"), (r"forcefield", "forcefield"), (r"^door", "door"),
    (r"computernoise|glitch|slime|spacetrash", "electronic"),
    (r"powerup|pepsound|phasejump|tone|^high|^low", "ui/synth"),
    (r"^(click|mouseclick|mouserelease|switch|toggle|tick|select|rollover|scroll)", "ui/click"),
    (r"^(back|close|open|maximize|minimize|drop|bong|pluck|glass|scratch)", "ui/move"),
    (r"^(confirmation|question)", "ui/confirm"), (r"^error", "ui/error"),
    (r"^(card|cards)", "foley/cards"), (r"^(chip|chips)", "foley/chips"), (r"^(dice|die)", "foley/dice"),
    (r"^book", "foley/book"), (r"^cloth|belt", "foley/cloth"), (r"knife|chop", "foley/blade"),
    (r"coins", "foley/coins"), (r"^metal|latch", "foley/metal"), (r"leather", "foley/leather"),
    (r"creak", "foley/wood"), (r"jingles", "music/jingle"),
]
KENNEY_PACK_FAMILY = {"voiceover-pack": "voice", "voiceover-pack-fighter": "voice",
                      "music-jingles": "music/jingle", "interface-sounds": "ui", "ui-audio": "ui"}
WEIGHTS = ("light", "medium", "heavy")


def camel_words(s: str) -> list[str]:
    return [w.lower() for w in re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])|\d+", s)]


# ---------- per-library parsing ----------

def kenney_entry(relp: Path) -> dict:
    """kenney/<pack>/Audio/impactMetal_heavy_000.ogg -> family impact, material metal, weight heavy."""
    pack = relp.parts[1]
    sub = [p for p in relp.parts[2:-1] if p.lower() != "audio"]
    stem = relp.stem
    if stem.lower() == "preview":
        return {"instrument": pack, "articulation": "", "kind": "preview", "family": "preview",
                "key": "preview", "tags": ["preview"], "rr": None}
    m = re.match(r"^(.*?)[_\-]?(\d+)$", stem)
    base, variant = (m.group(1), int(m.group(2))) if m and m.group(1) else (stem, None)
    words = [w for part in re.split(r"[_\-\s]+", base) for w in camel_words(part)]
    low = base.lower().replace("_", "").replace("-", "")
    family = KENNEY_PACK_FAMILY.get(pack)
    if not family or not family.startswith(("voice", "music")):
        family = next((fam for pat, fam in KENNEY_RULES if re.search(pat, low)), family) or "sfx"
    kind = "voice" if family == "voice" else "music" if family.startswith("music") else "sfx"
    tags = [w for w in words if w not in WEIGHTS]
    weight = next((w for w in words if w in WEIGHTS), None)
    material = None
    if family in ("impact", "footstep") and len(words) > 1:
        material = next((w for w in words[1:] if w not in WEIGHTS), None)
    return {
        "instrument": pack, "articulation": slug("-".join(sub)), "kind": kind,
        "family": family + (f"/{material}" if material and family in ("impact", "footstep") else ""),
        "material": material, "weight": weight, "key": slug(base) or slug(stem),
        "variant": variant, "rr": (variant + 1) if variant is not None else None,
        "tags": sorted(set(tags + [pack] + [slug(s) for s in sub])),
    }


def instrument_entry(lib: str, relp: Path) -> dict:
    """vcsl/<cat>/<sub>/<Instrument>/[<artic>/]file  or  vsco2ce/<section>/<Instrument>/[<artic>/]file."""
    parts = relp.parts[1:-1]
    if lib == "vcsl":
        inst_i = 2
    else:
        inst_i = 1 if len(parts) > 1 else 0
    inst_name = parts[inst_i] if len(parts) > inst_i else parts[-1]
    artic = parts[inst_i + 1:]
    name = parse_sample_name(relp.name)
    instrument = slug(inst_name)
    articulation = slug("-".join(artic))
    fam, ftags = FAMILY.get(instrument, (HS_FAMILY.get(parts[0].lower(), "instrument"), []))
    if articulation.startswith("pizz"):
        fam = "instrument/plucked-string"
    tags = sorted(set(ftags + [slug(p) for p in parts] + ([name.descriptor] if name.descriptor else [])))
    return {
        "instrument": instrument, "articulation": articulation, "family": fam, "tags": tags,
        "key": name.descriptor or articulation or instrument,
        "note": name.note, "midi_named": name.midi_named, "dyn": name.dyn, "vel_layer": name.vel_layer,
        "rr": name.rr, "mic": name.mic,
    }


# ---------- SFZ maps ----------

def load_sfz_map(root: Path, lib: str) -> dict[str, dict]:
    """lower-case library-relative sample path -> SFZ region info (single-articulation files win)."""
    sfz_root = root / f"{lib}-sfz"
    out: dict[str, dict] = {}
    if not sfz_root.exists():
        return out
    for sfz in sorted(sfz_root.rglob("*.sfz")):
        keyswitch = bool(re.search(r"keyswitch|-ks\b", sfz.stem, re.I))
        for r in parse_sfz(sfz):
            try:
                relp = r.sample.resolve().relative_to(sfz_root.resolve()).as_posix().lower()
            except ValueError:
                continue
            info = {
                "sfz": L.rel(sfz, root), "keycenter": r.keycenter,
                "lokey": r.get("lokey"), "hikey": r.get("hikey"),
                "lovel": r.get("lovel"), "hivel": r.get("hivel"),
                "offset": r.get("offset"), "volume_db": r.get("volume"), "tune": r.get("tune"),
                "ampeg_release": r.get("ampeg_release"), "trigger": r.get("trigger"),
                "seq_position": r.get("seq_position"), "keyswitch": keyswitch,
            }
            old = out.get(relp)
            if old is None or (old["keyswitch"] and not keyswitch):
                if old is not None and old["keycenter"] != info["keycenter"]:
                    info["conflict"] = old["keycenter"]
                out[relp] = info
    return out


# ---------- pitch check (optional) ----------

F0_METHOD = "pyin-octave+fft-peak-v2"
STABLE_CENTS = 10.0     # max drift between the two halves of the window for a usable reading


def spectral_peak(seg: np.ndarray, sr: int, guess: float, width: float = 1.06) -> float | None:
    """Frequency of the strongest spectral peak within guess/width..guess*width (Hann, zero-padded
    FFT, log-parabolic interpolation). Accurate to ~1 cent; works for inharmonic bars and bells."""
    if len(seg) < 256 or guess <= 0:
        return None
    n = 1 << max(18, int(np.ceil(np.log2(len(seg)))) + 4)
    spec = np.abs(np.fft.rfft(seg * np.hanning(len(seg)), n=n))
    lo, hi = max(1, int(guess / width * n / sr)), min(len(spec) - 2, int(guess * width * n / sr) + 1)
    if hi <= lo:
        return None
    k = lo + int(np.argmax(spec[lo:hi]))
    if k in (lo, hi - 1):            # rising toward the edge: the real peak is outside the window
        return None
    a, b, c = np.log(spec[k - 1:k + 2] + 1e-12)
    den = a - 2 * b + c
    return float((k + (0.5 * (a - c) / den if den else 0.0)) * sr / n)


def estimate_f0(path: Path, expected_midi: int) -> dict:
    """pYIN (22.05 kHz) finds the octave; the FFT peak within ±150 cents of the mapped key in that
    octave, at the file's rate, gives the cents (pYIN alone misreads bars and bells).

    Window: 60-660 ms after the onset (shorter files: what is there). `stable` is False when the
    two halves of the window differ by more than STABLE_CENTS (pitch glides, chorus, beating);
    the sampler only auto-tunes stable readings.
    """
    import librosa
    import soxr
    y, sr = sf.read(path, dtype="float32", always_2d=True)
    y = y.mean(axis=1)
    env_ = np.abs(y)
    if env_.max() <= 0:
        return {"hz": None, "conf": 0.0, "method": F0_METHOD}
    onset = int(np.argmax(env_ > env_.max() * 0.1))
    avail = (len(y) - onset) / sr
    t0, t1 = (0.06, 0.66) if avail >= 0.5 else (0.03, max(0.06, avail))
    seg = y[onset + int(t0 * sr): onset + int(t1 * sr)]
    lo = librosa.midi_to_hz(max(expected_midi - 19, 20))
    hi = librosa.midi_to_hz(min(expected_midi + 19, 120))
    y22 = soxr.resample(seg, sr, 22050) if sr != 22050 else seg
    frame = 4096 if len(y22) >= 4096 else 2048
    if len(y22) < frame:
        return {"hz": None, "conf": 0.0, "method": F0_METHOD}
    f0, voiced, prob = librosa.pyin(y22, fmin=lo, fmax=min(hi, 22050 / 2.5), sr=22050,
                                    frame_length=frame, hop_length=512)
    ok = voiced & np.isfinite(f0)
    if ok.sum() < 3:
        return {"hz": None, "conf": float(np.nanmean(prob)) if prob is not None else 0.0, "method": F0_METHOD}
    coarse = float(np.median(f0[ok]))
    octave = int(round((float(librosa.hz_to_midi(coarse)) - expected_midi) / 12))
    # Peak within ±150 cents of the mapped key in pYIN's octave: other partials are further away.
    peak = spectral_peak(seg, sr, float(librosa.midi_to_hz(expected_midi + 12 * octave)), 2 ** (1.5 / 12))
    hz = peak or coarse
    half = len(seg) // 2
    ha, hb = spectral_peak(seg[:half], sr, hz, 1.03), spectral_peak(seg[half:], sr, hz, 1.03)
    drift = abs(1200 * np.log2(ha / hb)) if (peak and ha and hb) else None
    m = float(librosa.hz_to_midi(hz))
    return {"hz": round(hz, 2), "midi": round(m, 3), "cents": round((m - expected_midi) * 100, 1),
            "octave_off": int(round((m - expected_midi) / 12)), "conf": round(float(np.mean(prob[ok])), 3),
            "coarse_cents": round(float(librosa.hz_to_midi(coarse) - expected_midi) * 100, 1),
            "drift_cents": round(drift, 1) if drift is not None else None,
            "stable": bool(drift is not None and drift <= STABLE_CENTS), "method": F0_METHOD}


# ---------- build ----------

def scan_files(root: Path, ledger: list[dict]) -> list[tuple[Path, dict]]:
    out = []
    for r in ledger:
        if r.get("path", "").endswith("-sfz"):
            continue
        base = root / r["path"]
        for f in L.audio_files(base):
            out.append((f, r))
    seen, uniq = set(), []
    for f, r in out:
        if f not in seen:
            seen.add(f)
            uniq.append((f, r))
    return uniq


def reusable_f0(old: dict | None, e: dict) -> bool:
    """A previous f0 reading is kept while the file, its key and the method are unchanged."""
    f0 = (old or {}).get("f0") or {}
    return bool(old and old.get("sha256") == e["sha256"] and f0 and f0.get("for_midi") == e.get("midi")
                and f0.get("method") == F0_METHOD)


def mode(counter: Counter):
    return counter.most_common(1)[0][0] if counter else None


def build_index(root: Path = L.ROOT, verify_pitch: bool = False, previous: dict | None = None,
                log=print) -> dict:
    root = Path(root)
    ledger = L.read_ledger(root)
    if not ledger:
        raise SystemExit(f"chưa có sổ {L.ledger_path(root)}; chạy gen.fetch_libraries trước")
    cache = L.ShaCache(root)
    prev = {e["file"]: e for e in (previous or {}).get("files", [])}
    sfz_maps = {lib: load_sfz_map(root, lib) for lib in L.GIT_LIBRARIES}
    entries = []
    for f, rec in scan_files(root, ledger):
        relp = Path(L.rel(f, root))
        lib = rec["library"]
        try:
            info = sf.info(str(f))
        except RuntimeError as e:
            log(f"  bỏ qua (không đọc được): {relp}: {e}")
            continue
        e = {
            "file": relp.as_posix(), "library": lib, "pack": rec.get("pack"), "pack_path": rec["path"],
            "licence": rec.get("licence"), "sha256": cache.get(f), "bytes": f.stat().st_size,
            "format": info.format, "subtype": info.subtype, "sample_rate": info.samplerate,
            "channels": info.channels, "frames": info.frames, "duration": round(info.duration, 4),
        }
        if lib == "kenney":
            e.update(kenney_entry(relp))
        else:
            e.update(instrument_entry(lib, relp))
            lib_rel = relp.relative_to(lib).as_posix()
            s = sfz_maps.get(lib, {}).get(lib_rel.lower())   # SFZ names may differ in case
            if s:
                e["sfz"] = {k: v for k, v in s.items() if v is not None and k != "keyswitch"}
        e["instrument_id"] = f"{lib}/{e['instrument']}" + (f".{e['articulation']}" if e["articulation"] else "")
        entries.append(e)
    cache.save()
    resolve_pitch(entries)
    if verify_pitch:
        n = 0
        for e in entries:
            if e.get("kind") != "pitched" or e.get("midi") is None:
                continue
            old = prev.get(e["file"])
            if reusable_f0(old, e):
                e["f0"] = old["f0"]
                continue
            e["f0"] = {**estimate_f0(root / e["file"], e["midi"]), "for_midi": e["midi"]}
            n += 1
        log(f"  đo cao độ: {n} file mới")
    else:
        for e in entries:
            old = prev.get(e["file"])
            if reusable_f0(old, e):
                e["f0"] = old["f0"]
    libs = {}
    for r in ledger:
        lib = libs.setdefault(r["library"], {"licence": r.get("licence"), "packs": 0, "commit": r.get("commit")})
        lib["packs"] += 1
    return {
        "version": INDEX_VERSION,
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "root": str(root),
        "libraries": libs,
        "instruments": summarize(entries),
        "files": sorted(entries, key=lambda x: x["file"]),
    }


def resolve_pitch(entries: list[dict]) -> None:
    """Set kind (pitched / unpitched), midi and midi_source for instrument samples."""
    groups: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        if e["library"] != "kenney":
            groups[e["instrument_id"]].append(e)
    # octave offsets learned from SFZ: per folder, then per instrument
    by_folder: dict[str, Counter] = defaultdict(Counter)
    by_inst: dict[str, Counter] = defaultdict(Counter)
    for e in entries:
        s = e.get("sfz")
        if s and s.get("keycenter") is not None and e.get("midi_named") is not None:
            d = s["keycenter"] - e["midi_named"]
            by_folder[str(Path(e["file"]).parent)][d] += 1
            by_inst[e["library"] + "/" + e["instrument"]][d] += 1
    for iid, items in groups.items():
        named = sum(1 for e in items if e.get("midi_named") is not None)
        pitched = named >= max(2, 0.6 * len(items))
        for e in items:
            e["kind"] = "pitched" if pitched and e.get("midi_named") is not None else "unpitched"
            if e["kind"] != "pitched":
                e["midi"] = None
                e["midi_source"] = None
                continue
            s = e.get("sfz") or {}
            if s.get("keycenter") is not None:
                e["midi"], e["midi_source"] = s["keycenter"], "sfz"
            else:
                off = mode(by_folder.get(str(Path(e["file"]).parent), Counter()))
                src = "name+folder-sfz-offset"
                if off is None:
                    off = mode(by_inst.get(e["library"] + "/" + e["instrument"], Counter()))
                    src = "name+instrument-sfz-offset"
                if off is None:
                    off, src = 0, "name"
                e["midi"], e["midi_source"] = e["midi_named"] + off, src
            e["note_spn"] = midi_to_note(e["midi"])
    for e in entries:
        if e["library"] == "kenney":
            e.setdefault("midi", None)


def summarize(entries: list[dict]) -> dict:
    out: dict[str, dict] = {}
    groups: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        groups[e["instrument_id"]].append(e)
    for iid, items in sorted(groups.items()):
        kinds = Counter(e.get("kind") for e in items)
        kind = kinds.most_common(1)[0][0]
        art = items[0]["articulation"] or ""
        family = Counter(e.get("family") for e in items).most_common(1)[0][0]
        # plucked strings ring out (vibrato included); only tremolo is held
        sustain = kind == "pitched" and bool(SUSTAIN_RE.search(art)) and \
            (family != "instrument/plucked-string" or "trem" in art)
        rel = [e["sfz"]["ampeg_release"] for e in items if e.get("sfz", {}).get("ampeg_release") is not None]
        d = {
            "library": items[0]["library"], "pack": items[0].get("pack"), "kind": kind, "family": family,
            "files": len(items), "licence": sorted({e.get("licence") for e in items}),
            "mode": "sustain" if sustain else "oneshot",
            "release": round(min(max(rel), 3.0), 3) if (sustain and rel) else (0.3 if sustain else None),
            "sample_rates": sorted({e["sample_rate"] for e in items}),
            "rr_max": max((e.get("rr") or 1) for e in items),
        }
        if kind == "pitched":
            roots = sorted({e["midi"] for e in items if e.get("midi") is not None})
            d.update(roots=roots, range=[midi_to_note(roots[0]), midi_to_note(roots[-1])] if roots else None,
                     playable=[midi_to_note(max(0, roots[0] - 3)), midi_to_note(min(127, roots[-1] + 3))]
                     if roots else None,
                     layers=max(len({(e.get("vel_layer"), e.get("dyn")) for e in items if e.get("midi") == r})
                                for r in roots) if roots else 0,
                     midi_source=dict(Counter(e.get("midi_source") for e in items)))
            f0 = [e["f0"] for e in items if e.get("f0", {}).get("cents") is not None]
            if f0:
                cents = [x["cents"] - 1200 * x["octave_off"] for x in f0]
                octs = Counter(x["octave_off"] for x in f0)
                d["f0_check"] = {"checked": len(f0), "octave_off": dict(octs),
                                 "median_abs_cents": round(float(np.median(np.abs(cents))), 1),
                                 "within_10_cents": int(sum(abs(c) <= 10 for c in cents)),
                                 "unstable": int(sum(not x.get("stable", False) for x in f0))}
                # every checked sample sounds a whole octave away from its mapped key (e.g. glockenspiel)
                if len(f0) >= 4 and len(octs) == 1 and next(iter(octs)) != 0:
                    d["octave_fix"] = 12 * next(iter(octs))
        else:
            d["keys"] = sorted({e.get("key") for e in items if e.get("key")})
        out[iid] = d
    return out


def write_index(index: dict, path: Path) -> None:
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(index, ensure_ascii=False, indent=1))
    os.replace(tmp, path)


def print_summary(index: dict) -> None:
    print(f"{'nhạc cụ':44} {'loại':9} {'file':>4}  {'quãng / phím':28} lớp rr  nguồn nốt")
    for iid, d in index["instruments"].items():
        if d["kind"] == "pitched":
            span = f"{d['range'][0]}–{d['range'][1]} (chơi {d['playable'][0]}–{d['playable'][1]})"
            src = ",".join(f"{k}:{v}" for k, v in d.get("midi_source", {}).items())
            print(f"{iid:44} {d['kind']:9} {d['files']:>4}  {span:28} {d['layers']:>3} {d['rr_max']:>2}  {src}")
        else:
            keys = ", ".join(d.get("keys", [])[:4]) + (" …" if len(d.get("keys", [])) > 4 else "")
            print(f"{iid:44} {d['kind']:9} {d['files']:>4}  {keys[:40]}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="gen.index_library", description=__doc__.split("\n")[0])
    ap.add_argument("--verify-pitch", action="store_true", help="đo f0 của mẫu có cao độ (pYIN tìm quãng tám, đỉnh FFT cho cent), ghi vào index")
    ap.add_argument("--summary", action="store_true", help="chỉ in bảng nhạc cụ của index hiện có")
    ap.add_argument("--root", default=str(L.ROOT), help=argparse.SUPPRESS)
    ap.add_argument("--out", default=None, help="mặc định <root>/index.json")
    a = ap.parse_args(argv)
    env.apply()
    root = Path(a.root)
    out = Path(a.out) if a.out else root / L.INDEX_NAME
    previous = json.loads(out.read_text()) if out.exists() else None
    if a.summary:
        if not previous:
            raise SystemExit("chưa có index")
        print_summary(previous)
        return 0
    index = build_index(root, verify_pitch=a.verify_pitch, previous=previous)
    write_index(index, out)
    print_summary(index)
    kinds = Counter(e.get("kind") for e in index["files"])
    print(f"\n{len(index['files'])} file, {len(index['instruments'])} nhóm; "
          + ", ".join(f"{k}: {v}" for k, v in sorted(kinds.items())) + f"\nĐã ghi {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
