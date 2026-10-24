"""Bộ phát mẫu Python (sample player) cho Audio Lab.

  run.sh sampler list [--kind pitched]                 # nhạc cụ trong ~/AudioLab/libraries/index.json
  run.sh sampler info dan-tranh.normal                 # quãng, lớp cường độ, round robin, bảng phím
  run.sh sampler render -i dan-tranh.normal --notes "0:C5:0.5:100 0.25:D5:0.5:90" -o out.wav
  run.sh sampler render --midi song.mid --map "0=vcsl/dan-tranh.normal,9=vcsl/frame-drum" -o out.wav
  run.sh sampler render --midi loop.mid -i flute.susnv --bars 8 --tail wrap -o loop.wav
  run.sh sampler render --instrument-dir ~/rec/bell --notes "0:C5:1" -o out.wav
  run.sh sampler render --notes-json notes.json -o out.wav  # nốt ghi "instrument": "dan-tranh.normal"
  run.sh sampler phrase dan-tranh.normal               # câu thử của một nhạc cụ
  run.sh sampler phrases [--library vcsl] [--kind pitched]   # câu thử cho mọi nhạc cụ

Ra WAV 48 kHz 24-bit stereo, kèm <tên>.json (nốt nào lấy mẫu nào, dời bao nhiêu, nguồn và giấy phép).
Dời cao độ tối đa 3 bán cung (kế hoạch §3.2); nốt ngoài tầm thì báo lỗi, hoặc bỏ qua với --skip-out-of-range.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from common import env
from sampler.engine import MAX_SHIFT_CAP, OutOfRange, Sampler, notes_from_json, parse_note_spec
from sampler.instrument import from_folder, from_index, load_index
from sampler.midi import read_midi
from sampler.naming import midi_to_note
from sampler.phrases import test_phrase

OUT_DIR = env.WORK / "_sampler"


def _sampler(a) -> Sampler:
    return Sampler(max_shift=a.max_shift, rr_mode=a.rr, seed=a.seed, veltrack=a.veltrack)


def _write(render, out: Path, extra: dict | None = None) -> None:
    render.write(out)
    rep = dict(render.report)
    if extra:
        rep.update(extra)
    out.with_suffix(".json").write_text(json.dumps(rep, ensure_ascii=False, indent=1))
    peak = rep.get("peak_dbfs")
    print(f"{out}  {rep['duration']:.2f} s, {len(rep['notes'])} nốt, bỏ {len(rep['skipped'])}, "
          f"đỉnh {peak} dBFS" + (f", hạ {rep['gain_applied_db']} dB" if rep["gain_applied_db"] else ""))


def cmd_list(a) -> int:
    ix = load_index(a.index)
    for iid, d in ix["instruments"].items():
        if a.kind and d["kind"] != a.kind:
            continue
        if a.library and d["library"] != a.library:
            continue
        if d["kind"] == "pitched":
            print(f"{iid:44} {d['kind']:9} {d['range'][0]}–{d['range'][1]}  chơi {d['playable'][0]}–"
                  f"{d['playable'][1]}  lớp {d['layers']} rr {d['rr_max']} {d['mode']}"
                  + (f" octave_fix {d['octave_fix']:+d}" if d.get("octave_fix") else ""))
        else:
            print(f"{iid:44} {d['kind']:9} {len(d.get('keys', []))} phím, rr {d['rr_max']}")
    return 0


def cmd_info(a) -> int:
    inst = from_index(a.instrument, load_index(a.index), tuning=a.tuning)
    print(f"{inst.id}: {'có cao độ' if inst.pitched else 'không cao độ'}, {len(inst.zones)} mẫu, "
          f"mode {inst.mode}, release {inst.release} s, họ {inst.family}")
    for n in inst.notes:
        print(f"  ghi chú: {n}")
    if inst.pitched:
        play = inst.playable(a.max_shift)
        print(f"  gốc: {' '.join(midi_to_note(r) for r in inst.roots())}")
        print(f"  chơi được (±{a.max_shift} bán cung): {midi_to_note(play[0])}–{midi_to_note(play[-1])}"
              f", thiếu: {' '.join(midi_to_note(m) for m in range(play[0], play[-1]) if m not in play) or 'không'}")
        for r in inst.roots():
            layers = sorted({(z.lovel, z.hivel) for z in inst.zones if z.root == r})
            rr = max(z.rr for z in inst.zones if z.root == r)
            tune = [round(z.tune_cents) for z in inst.zones if z.root == r and z.tune_cents]
            print(f"    {midi_to_note(r):4} lớp {layers} rr {rr}" + (f" chỉnh {tune} cent" if tune else ""))
    else:
        for k, m in inst.keymap.items():
            zs = [z for z in inst.zones if z.key == k]
            print(f"    {k:28} MIDI {m:3} ({midi_to_note(m)})  lớp {sorted({(z.lovel, z.hivel) for z in zs})}"
                  f" rr {max(z.rr for z in zs)}")
    return 0


def _load_instruments(a, s: Sampler) -> None:
    ix = None
    names = []
    if a.instrument_dir:
        inst = from_folder(a.instrument_dir, pitched=a.pitched, octave_offset=a.octave_offset)
        names.append(s.add(inst))
    for name in a.instrument or []:
        ix = ix or load_index(a.index)
        names.append(s.add(from_index(name, ix, tuning=a.tuning), name))
    for item in (a.map or "").split(","):
        if item.strip():
            ch, _, name = item.partition("=")
            ix = ix or load_index(a.index)
            if name not in s.instruments:
                s.add(from_index(name, ix, tuning=a.tuning), name)


NEED_INSTRUMENT = "cần --instrument, --instrument-dir, --map, hoặc trường \"instrument\" trong --notes-json"


def cmd_render(a) -> int:
    s = _sampler(a)
    _load_instruments(a, s)
    meta = {}
    if a.midi and not s.instruments:
        raise SystemExit(NEED_INSTRUMENT)
    if a.midi:
        cmap = {int(ch): name for ch, _, name in (i.partition("=") for i in (a.map or "").split(",") if i.strip())}
        default = (a.instrument or [None])[0] if a.instrument else (next(iter(s.instruments)) if not cmap else None)
        notes, meta = read_midi(a.midi, channel_map=cmap or None, default_instrument=default, transpose=a.transpose)
        bpm = a.bpm or meta["bpm"]
    elif a.notes or a.notes_json:
        bpm = a.bpm
        notes = parse_note_spec(a.notes, bpm) if a.notes else notes_from_json(json.loads(Path(a.notes_json).read_text()), bpm)
        for n in notes:
            n.midi = n.midi + a.transpose if n.midi is not None else None
    else:
        raise SystemExit("cần --midi, --notes hoặc --notes-json")
    ix = None
    for name in sorted({n.instrument for n in notes if n.instrument and n.instrument not in s.instruments}):
        ix = ix or load_index(a.index)         # notes may name index instruments directly
        s.add(from_index(name, ix, tuning=a.tuning), name)
    if not s.instruments:
        raise SystemExit(NEED_INSTRUMENT)
    length = a.length
    if a.bars:
        beats = a.bars * (a.beats_per_bar or meta.get("beats_per_bar", 4))
        length = beats * 60.0 / (bpm or 120.0)
    try:
        r = s.render(notes, length=length, tail=a.tail, normalize=a.normalize,
                     on_out_of_range="skip" if a.skip_out_of_range else "error")
    except OutOfRange as e:
        raise SystemExit(f"nốt ngoài tầm: {e}\n(dùng --skip-out-of-range để bỏ qua và ghi vào báo cáo)")
    out = Path(a.out) if a.out else OUT_DIR / "renders" / "render.wav"
    _write(r, out, {"midi": str(a.midi) if a.midi else None, "midi_meta": meta})
    return 0


def _phrase(a, s: Sampler, inst, out_dir: Path) -> None:
    name = s.add(inst)
    notes, length = test_phrase(inst, a.max_shift, name)
    r = s.render(notes, normalize="guard")
    _write(r, out_dir / f"{inst.id.replace('/', '__')}.wav", {"phrase": True, "phrase_length": length})


def cmd_phrase(a) -> int:
    out_dir = Path(a.out_dir) if a.out_dir else OUT_DIR / "phrases"
    if a.instrument_dir:
        inst = from_folder(a.instrument_dir, pitched=a.pitched, octave_offset=a.octave_offset)
        _phrase(a, _sampler(a), inst, out_dir)
    names = list(a.names) + list(a.instrument or [])
    ix = load_index(a.index) if names else None
    for name in names:
        _phrase(a, _sampler(a), from_index(name, ix, tuning=a.tuning), out_dir)
    if not names and not a.instrument_dir:
        raise SystemExit("cần tên nhạc cụ hoặc --instrument-dir")
    return 0


def cmd_phrases(a) -> int:
    ix = load_index(a.index)
    out_dir = Path(a.out_dir) if a.out_dir else OUT_DIR / "phrases"
    done = 0
    for iid, d in ix["instruments"].items():
        if d["kind"] not in ("pitched", "unpitched"):
            continue
        if (a.kind and d["kind"] != a.kind) or (a.library and d["library"] != a.library):
            continue
        _phrase(a, _sampler(a), from_index(iid, ix, tuning=a.tuning), out_dir)
        done += 1
    print(f"{done} câu thử trong {out_dir}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="sampler", description=__doc__.split("\n")[0],
                                 epilog="\n".join(__doc__.split("\n")[1:]),
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--index", default=None, help="index.json (mặc định ~/AudioLab/libraries/index.json)")
    ap.add_argument("--max-shift", type=float, default=MAX_SHIFT_CAP, help="trần dời cao độ, ≤ 3 bán cung")
    ap.add_argument("--rr", choices=("cycle", "random"), default="cycle", help="cách xoay round robin")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--veltrack", type=float, default=0.5, help="0 = không đổi độ to theo velocity, 1 = (v/127)^2")
    ap.add_argument("--tuning", choices=("auto", "sfz", "none"), default="auto",
                    help="auto: sửa quãng tám, bù lệch 5–70 cent theo f0 đo trong index (thay tune của SFZ)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("list", help="liệt kê nhạc cụ")
    p.add_argument("--kind", choices=("pitched", "unpitched", "sfx", "music", "voice"))
    p.add_argument("--library")
    p.set_defaults(fn=cmd_list)

    p = sub.add_parser("info", help="chi tiết một nhạc cụ")
    p.add_argument("instrument")
    p.set_defaults(fn=cmd_info)

    def src(p):
        p.add_argument("-i", "--instrument", action="append", help="id nhạc cụ trong index (lặp được)")
        p.add_argument("--instrument-dir", help="thư mục mẫu tự đặt tên kiểu VCSL (nốt, v<n>, rr<n>)")
        p.add_argument("--pitched", action="store_true", default=None, help="ép coi thư mục là có cao độ")
        p.add_argument("--octave-offset", type=int, default=0, help="cộng vào nốt đọc từ tên (12 nếu C3 = đô giữa)")

    p = sub.add_parser("render", help="dựng MIDI hoặc danh sách nốt ra WAV")
    src(p)
    p.add_argument("--midi", help="file .mid")
    p.add_argument("--map", help="kênh MIDI (0–15) = nhạc cụ, ví dụ '0=dan-tranh.normal,9=frame-drum'")
    p.add_argument("--notes", help="'start:nốt:dài[:vel[:phím]]' cách nhau bằng dấu cách")
    p.add_argument("--notes-json", help="file JSON: [{start, note|midi|key, dur, vel, instrument, cents, pan}]")
    p.add_argument("--bpm", type=float, help="khi có: start/dài tính bằng phách")
    p.add_argument("--transpose", type=int, default=0)
    p.add_argument("--length", type=float, help="độ dài (giây)")
    p.add_argument("--bars", type=float, help="độ dài theo ô nhịp (cần bpm, hoặc lấy từ MIDI)")
    p.add_argument("--beats-per-bar", type=int)
    p.add_argument("--tail", choices=("keep", "cut", "wrap"), default="keep",
                   help="wrap: gập đuôi vang về đầu để vòng lặp liền")
    p.add_argument("--normalize", choices=("guard", "peak", "none"), default="guard")
    p.add_argument("--skip-out-of-range", action="store_true")
    p.add_argument("-o", "--out", help="file WAV ra (mặc định ~/AudioLab/work/_sampler/renders/render.wav)")
    p.set_defaults(fn=cmd_render)

    p = sub.add_parser("phrase", help="câu thử cho một hoặc vài nhạc cụ")
    src(p)
    p.add_argument("names", nargs="*")
    p.add_argument("--out-dir")
    p.set_defaults(fn=cmd_phrase)

    p = sub.add_parser("phrases", help="câu thử cho mọi nhạc cụ trong index")
    p.add_argument("--kind", choices=("pitched", "unpitched"))
    p.add_argument("--library")
    p.add_argument("--out-dir")
    p.set_defaults(fn=cmd_phrases)

    a = ap.parse_args(argv)
    if not 0 < a.max_shift <= MAX_SHIFT_CAP:
        ap.error(f"--max-shift phải trong (0, {MAX_SHIFT_CAP}] (kế hoạch §3.2)")
    env.apply()
    try:
        return a.fn(a)
    except (KeyError, FileNotFoundError, ValueError) as e:
        msg = e.args[0] if isinstance(e, KeyError) and e.args else str(e)
        print(f"sampler: {msg}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
