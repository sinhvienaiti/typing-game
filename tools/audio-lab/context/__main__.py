"""Context renders (BATCH1_BRIEF §3.5).

  run.sh context scenarios
  run.sh context voices                       # record the macOS voices once (~/AudioLab/work/_context/voices)
  run.sh context render --scenario dh-cast-chain --slot fire.cast=A.wav --slot fire.impact.a=B.wav ...
                        [--focus fire.cast] [--delay 0.15] [--duck-from request|voice] --out OUT.wav
  run.sh context render --scenario ts-xung-3s --slot gun.xung.A=a1.wav,a2.wav --slot gun.xung.B=b1.wav,b2.wav \
                        --slot gun.xung.loop=L.wav --slot gun.xung.tail=T.wav --slot hit.t1=H.wav \
                        [--config proposed|current] [--bed-db 16] [--focus gun.xung] --out OUT.wav
  run.sh context render --scenario td-wordhit-chain --slot word-hit=A3:a3.wav,C4:c4.wav,... --slot coin=C.wav ...
                        [--config proposed|current] [--focus word-hit] --out OUT.wav
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from common import env


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="context", description="Dựng âm trong bối cảnh trận (bộ trộn giống game).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("scenarios")
    sub.add_parser("voices")
    r = sub.add_parser("render")
    r.add_argument("--scenario", required=True)
    r.add_argument("--slot", action="append", default=[], help="id=file")
    r.add_argument("--focus")
    r.add_argument("--delay", type=float, default=0.15)
    r.add_argument("--duck-from", default="request", choices=["request", "voice"])
    r.add_argument("--no-sweep", action="store_true")
    r.add_argument("--config", default="proposed", choices=["proposed", "current"],
                   help="Tuyến Cuối, Lời Gọi: cách phát (ts-*, td-*)")
    r.add_argument("--bed-db", type=float, default=16.0, help="Tuyến Cuối: nền liên thanh thấp hơn phát đơn bao nhiêu dB")
    r.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    env.apply()
    from . import scenes, td_scenes, ts_scenes, voices
    if a.cmd == "scenarios":
        print("\n".join(scenes.SCENARIOS + ts_scenes.SCENARIOS + td_scenes.SCENARIOS))
        return 0
    if a.cmd == "voices":
        for v in voices.VOICES:
            for w in voices.WORDS:
                print(voices.record(v, w))
        return 0
    if a.scenario in ts_scenes.SCENARIOS:
        ts: dict = {}
        for kv in a.slot:
            k, _, p = kv.partition("=")
            files = [Path(x).expanduser() for x in p.split(",") if x]
            if k in ("gun.xung.A", "gun.xung.B"):
                ts.setdefault("gun.xung", {})[k[-1]] = files
            else:
                ts[k] = files
        doc = ts_scenes.render(a.scenario, ts, Path(a.out).expanduser(), focus=a.focus, config=a.config,
                               delay_s=a.delay, bed_db=a.bed_db, sweep=not a.no_sweep)
        print(json.dumps(doc["metrics"], ensure_ascii=False, default=float))
        return 0
    if a.scenario in td_scenes.SCENARIOS:
        td: dict = {}
        for kv in a.slot:
            k, _, p = kv.partition("=")
            if ":" in p.split(",")[0] and not p.startswith("/"):       # word-hit=A3:a.wav,C4:b.wav
                td[k] = {n: Path(f).expanduser() for n, _, f in (x.partition(":") for x in p.split(",") if x)}
            else:
                td[k] = Path(p).expanduser()
        doc = td_scenes.render(a.scenario, td, Path(a.out).expanduser(), focus=a.focus, config=a.config,
                               delay_s=a.delay, sweep=not a.no_sweep)
        print(json.dumps(doc["metrics"], ensure_ascii=False, default=float))
        return 0
    slots = {}
    for kv in a.slot:
        k, _, p = kv.partition("=")
        slots[k] = Path(p).expanduser()
    doc = scenes.render(a.scenario, slots, Path(a.out).expanduser(), focus=a.focus, delay_s=a.delay,
                        duck_from=a.duck_from, sweep=not a.no_sweep)
    print(json.dumps(doc["metrics"], ensure_ascii=False, default=float))
    return 0


if __name__ == "__main__":
    sys.exit(main())
