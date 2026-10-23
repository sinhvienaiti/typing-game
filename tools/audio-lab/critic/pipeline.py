"""Run the layered critic over files: measure, gate, flag, rank, draw, write."""
from __future__ import annotations

import datetime as dt
import platform
import time
from dataclasses import dataclass, field
from pathlib import Path

from . import artifacts, audio as A, features, hygiene, learned, policy, psycho, report, score
from . import spec as S
from .thresholds import LEARNED, SCHEMA_FILE, VERSION

ALL_LAYERS = ("L1", "L1b", "L2", "L3", "L4", "L5", "L6")
FAST_LAYERS = ("L1", "L1b", "L2", "L6")


@dataclass
class Options:
    layers: tuple[str, ...] = ALL_LAYERS
    stage: str = "final"
    group: str | None = None
    game: str | None = None
    variant_set: bool = False
    clap_models: tuple[str, ...] = ()
    seed: int = 0
    quiet: bool = False
    blind_cards: bool = False     # also write <stem>.blind.png for the Listening Board


def parse_layers(s: str | None) -> tuple[str, ...]:
    if not s or s.lower() == "all":
        return ALL_LAYERS
    if s.lower() == "fast":
        return FAST_LAYERS
    want = [x.strip().upper().replace("L1B", "L1b") for x in s.split(",") if x.strip()]
    bad = [x for x in want if x not in ALL_LAYERS]
    if bad:
        raise ValueError(f"lớp không có: {', '.join(bad)}; chọn trong {', '.join(ALL_LAYERS)}")
    return tuple(x for x in ALL_LAYERS if x in want)


def now_iso() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def tool_info(layers) -> dict:
    import numpy, scipy, soundfile, librosa
    libs = {"numpy": numpy.__version__, "scipy": scipy.__version__, "soundfile": soundfile.__version__,
            "libsndfile": soundfile.__libsndfile_version__, "librosa": librosa.__version__}
    try:
        import pyloudnorm
        libs["pyloudnorm"] = getattr(pyloudnorm, "__version__", "?")
    except Exception:
        pass
    if psycho.AVAILABLE:
        libs["mosqito"] = getattr(psycho._mq, "__version__", "?")
    return {"name": "audio-lab critic", "version": VERSION, "layers": list(layers),
            "python": platform.python_version(), "libs": libs}


def _card_for(path: Path, cards: list[S.Spec]) -> S.Spec | None:
    return S.match(path.stem, cards) if cards else None


def _spec_for(path: Path, cards: list[S.Spec], opts: Options) -> S.Spec:
    card = _card_for(path, cards)
    if card is not None:
        sp = S.from_mapping(card.raw, card.path, group_override=opts.group, game=opts.game)
        if not sp.id:
            sp.id = S.stem_id(path.stem)
        return sp
    return S.from_mapping(None, None, group_override=opts.group, sound_id=S.stem_id(path.stem), game=opts.game)


@dataclass
class RefSet:
    """Approved references of one card (its `refs`), or the CLI --refs for files without card refs."""
    key: str
    spec: S.Spec
    paths: list[Path]
    audio: list = field(default_factory=list)        # [(path, Audio, ai_ok)]
    l2: dict = field(default_factory=dict)
    l1b: dict = field(default_factory=dict)
    skipped: list = field(default_factory=list)
    broken: list = field(default_factory=list)

    def analyse(self) -> None:
        rows, l1b_rows = [], []
        for rp in self.paths:
            try:
                ra = A.load_checked(rp)
                rm, rctx = features.analyze(ra, self.spec)
            except Exception as e:  # noqa: BLE001 - a broken reference must not stop the run
                self.broken.append(f"{rp}: {getattr(e, 'msg_vi', None) or type(e).__name__}")
                continue
            if rm.get("silent"):
                self.skipped.append(str(rp))
                continue
            rows.append(rm)
            l1b_rows.append(artifacts.detect(ra, rm, rctx, self.spec)["metrics"])
            self.audio.append((rp, ra))
        self.l2 = features.ref_stats(rows)
        self.l1b = artifacts.ref_stats(l1b_rows)

    def to_json(self) -> dict:
        return {"key": self.key, "n": len(self.audio), "files": [str(p) for p, *_ in self.audio],
                "skipped_silent": self.skipped, "skipped_broken": self.broken}


def _ref_sets(files: list[Path], cards: list[S.Spec], cli_refs: list[str], opts: Options) -> tuple[dict, dict]:
    """(sets by key, set key by file). Card refs win over --refs for that card's files."""
    sets: dict[str, RefSet] = {}
    by_file: dict[Path, str | None] = {}
    for f in files:
        card = _card_for(f, cards)
        if card is not None and card.refs:
            key = f"card:{card.id or card.path}"
            if key not in sets:
                sets[key] = RefSet(key, _spec_for(f, cards, opts), A.collect(card.refs))
        elif cli_refs:
            key = "cli"
            if key not in sets:
                sets[key] = RefSet(key, _spec_for(f, cards, opts), A.collect(cli_refs))
        else:
            key = None
        by_file[f] = key
    for rs in sets.values():
        rs.analyse()
    return sets, by_file


def _score_one(p: Path, name: str, sp: S.Spec, rs: RefSet | None, pol, opts: Options, L: set, tool: dict,
               created: str) -> tuple[dict, tuple]:
    """Measure, gate (L1), flag (L1b) and score (L2) one file. Raises A.LoadError for unusable files."""
    t0 = time.time()
    a = A.load_checked(p)
    m, ctx = features.analyze(a, sp)
    tm = {"measure": round(time.time() - t0, 3)}
    ai_ok, ai_why = pol.check(p, a.sha256)
    r = {
        "schema": SCHEMA_FILE, "tool": tool, "created": created,
        "file": {"path": str(p.resolve()), "name": p.name, "stem": name, "sha256": a.sha256, "bytes": a.nbytes,
                 "format": a.fmt, "subtype": a.subtype, "sample_rate": a.sr, "channels": a.channels,
                 "frames": a.frames, "duration_s": round(a.duration, 4)},
        "spec": sp.to_json(), "stage": opts.stage, "layers": list(opts.layers),
        "cloud_ok": ai_ok, "ai_policy": {"allowed": ai_ok, "reason": ai_why}, "ai_steps": [],
        "refs": {"set": rs.key if rs else None, "n": len(rs.audio) if rs else 0},
        "verdict": "UNGATED", "metrics": m,
        "L1": None, "L1b": None, "L2": None, "L3": None, "L4": None, "L5": None,
        "flags": [], "notes_vi": [], "card": None, "timing_s": tm,
    }
    prov = pol.provenance(p, a.sha256)
    if prov.get("kind"):
        r["provenance"] = prov
    if a.duration > learned.LONG_S:          # L3/L4/L5 hear fixed windows only (time and RAM)
        r["long_file"] = {"duration_s": round(a.duration, 1), "learned_input": f"{learned.LONG_WINDOWS[0]} đoạn "
                          f"{learned.LONG_WINDOWS[1]:g} s"}
    if "L1" in L:
        t1 = time.time()
        g, gctx = hygiene.gate(a.data, a.sr, m, sp, opts.stage, subtype=a.subtype,
                               source_qa=pol.source_qa(a.sha256))
        ctx.update(gctx)
        r["L1"] = g
        r["verdict"] = g["verdict"]
        tm["L1"] = round(time.time() - t1, 3)
    if "L1b" in L:
        t1 = time.time()
        r["L1b"] = artifacts.detect(a, m, ctx, sp, rs.l1b if rs else None, ai_generated=prov.get("ai_generated"))
        r["flags"] += r["L1b"]["flags"]
        tm["L1b"] = round(time.time() - t1, 3)
    if "L2" in L and not m.get("silent"):
        t1 = time.time()
        l2 = features.l2_score(m, sp, rs.l2 if rs else None)
        l2["psycho"] = psycho.measure(a.mono, a.sr, (m.get("onset_ms") or 0) / 1000, m.get("lufs_m_max"))
        l2["refs_used"] = sum(1 for t in l2["targets"] if t["source"] == "refs")
        r["L2"] = l2
        tm["L2"] = round(time.time() - t1, 3)
    return r, (a, sp, ctx)


def _broken(p: Path, name: str, sp: S.Spec, code: str, label_vi: str, msg_vi: str, a, opts: Options,
            tool: dict, created: str) -> dict:
    """Result for a file the critic cannot score (unreadable, empty, NaN/Inf, analysis error): BLOCK."""
    try:
        sha = a.sha256 if a is not None else A.sha256(p)
        nbytes = p.stat().st_size
    except OSError:
        sha, nbytes = "", 0
    chk = {"id": code, "label_vi": label_vi, "measured_on": "raw", "value": None, "unit": "", "limit": None,
           "ok": False, "fix": "reject", "msg_vi": msg_vi, "blocking": True}
    ok_sr = a is not None and a.sr > 0
    return {
        "schema": SCHEMA_FILE, "tool": tool, "created": created,
        "file": {"path": str(p.resolve()), "name": p.name, "stem": name, "sha256": sha, "bytes": nbytes,
                 "format": a.fmt if a is not None else None, "subtype": a.subtype if a is not None else None,
                 "sample_rate": a.sr if a is not None else 0, "channels": a.channels if a is not None else 0,
                 "frames": a.frames if a is not None else 0, "duration_s": round(a.duration, 4) if ok_sr else 0.0},
        "spec": sp.to_json(), "stage": opts.stage, "layers": list(opts.layers),
        "cloud_ok": False, "ai_policy": {"allowed": False, "reason": "file không chấm được"}, "ai_steps": [],
        "refs": {"set": None, "n": 0}, "verdict": "BLOCK",
        "metrics": {"duration_ms": round(a.duration * 1000, 1) if ok_sr else None, "peak_dbfs": None,
                    "true_peak_dbtp": None, "dc_offset": None, "head_silence_ms": None, "silent": False,
                    "broken": code},
        "L1": {"stage": opts.stage, "pass": False, "verdict": "BLOCK", "blocking": [code], "fixes": [],
               "failed": [code], "checks": [chk]},
        "L1b": None, "L2": None, "L3": None, "L4": None, "L5": None,
        "flags": [], "notes_vi": [msg_vi], "card": None, "timing_s": {},
        "error": {"code": code, "msg_vi": msg_vi},
    }


def run(paths: list[str], spec_path: str | None = None, refs: list[str] | None = None,
        out_dir: str | Path | None = None, opts: Options | None = None,
        sources: list[str] | None = None) -> dict:
    opts = opts or Options()
    t_all = time.time()
    L = set(opts.layers)
    files = A.collect(paths)
    if not files:
        raise SystemExit("không có file âm nào để chấm")
    cards = S.load_cards(spec_path) if spec_path else []
    out = Path(out_dir) if out_dir else report.default_out()
    report.check_out(out)
    out.mkdir(parents=True, exist_ok=True)
    created = now_iso()
    tool = tool_info(opts.layers)
    pol = policy.load(sources)
    ref_sets, ref_of = _ref_sets(files, cards, list(refs or []), opts)

    results, ctxs = [], {}
    used_names: set[str] = set()
    for p in files:
        name = report.unique_stem(p.stem, used_names)
        sp = _spec_for(p, cards, opts)
        rs = ref_sets.get(ref_of[p]) if ref_of[p] else None
        try:
            r, ctx_entry = _score_one(p, name, sp, rs, pol, opts, L, tool, created)
            ctxs[name] = ctx_entry
        except A.LoadError as e:          # one broken file never stops the batch: it is blocked
            r = _broken(p, name, sp, e.code, e.label_vi, e.msg_vi, e.audio, opts, tool, created)
        except Exception as e:  # noqa: BLE001
            r = _broken(p, name, sp, "analysis_error", "Lỗi khi đo",
                        f"bộ chấm lỗi khi đo file ({type(e).__name__}: {str(e)[:200]})", None, opts, tool, created)
        if not opts.quiet and r.get("error"):
            print(f"audio-lab critic: {p.name}: {r['error']['msg_vi']} (CHẶN)")
        if not opts.quiet and r.get("long_file"):
            print(f"audio-lab critic: {p.name} dài {r['long_file']['duration_s']} s: lớp học máy chỉ nghe "
                  f"{r['long_file']['learned_input']}")
        results.append(r)

    # learned layers on files that passed (or can be fixed) and that the AI policy allows
    model_status: dict = {}
    if L & {"L3", "L4", "L5"}:
        by_key = {r["file"]["stem"]: r for r in results}
        elig = [r for r in results if r["verdict"] != "BLOCK" and r["cloud_ok"] and not r["metrics"].get("silent")]
        items = [learned.Item(r["file"]["stem"], ctxs[r["file"]["stem"]][0], ctxs[r["file"]["stem"]][1])
                 for r in elig]
        if opts.variant_set:
            for it in items:
                it.variants = [o.audio for o in items if o is not it]
        for r in results:
            for lay in ("L3", "L4", "L5"):
                if lay in L:
                    r[lay] = {"available": False, "reason": "bị chặn ở L1" if r["verdict"] == "BLOCK" else
                              (f"không đưa vào mô hình: {r['ai_policy']['reason']}" if not r["cloud_ok"] else
                               "file im lặng" if r["metrics"].get("silent") else "không chạy")}
        embeds = {}
        if items and "L3" in L:
            t1 = time.time()
            for k, v in learned.run_l3(items).items():
                by_key[k]["L3"] = v
            model_status["L3"] = round(time.time() - t1, 2)
        if items and ("L4" in L or "L5" in L):
            t1 = time.time()
            res4, embeds = learned.run_l4(items, opts.clap_models or learned.CLAP_MODELS)
            if "L4" in L:
                for k, v in res4.items():
                    by_key[k]["L4"] = v
                    by_key[k]["flags"] += v["flags"]
            model_status["L4"] = round(time.time() - t1, 2)
        l5_batch = {}
        if items and "L5" in L:
            t1 = time.time()
            for key, rs in ref_sets.items():
                keys = [r["file"]["stem"] for r in elig if r["refs"]["set"] == key]
                ok_refs = [(p, a) for p, a in rs.audio if pol.check(p, a.sha256)[0]]
                if not keys:
                    continue
                if len(ok_refs) < LEARNED["ref5"]:
                    for k in keys:
                        by_key[k]["L5"]["reason"] = f"cần ít nhất 5 âm tham chiếu đã duyệt được phép đưa vào AI (có {len(ok_refs)})"
                    continue
                missing = [it for it in items if it.key in keys and it.key not in embeds]
                if missing:          # --clap-models without the L5 model
                    embeds.update(learned.embed(missing))
                cand = {k: embeds[k] for k in keys}
                ref_items = [learned.Item(str(p), a, rs.spec) for p, a in ok_refs]
                res5, l5_batch[key] = learned.run_l5(cand, learned.embed(ref_items))
                for k, v in res5.items():
                    by_key[k]["L5"] = v
                    by_key[k]["flags"] += v["flags"]
            for r in results:
                if r["L5"] and not r["L5"].get("available") and r["L5"]["reason"] == "không chạy" and r["refs"]["set"] is None:
                    r["L5"]["reason"] = "chưa có âm tham chiếu đã duyệt (cần ít nhất 5)"
            model_status["L5"] = round(time.time() - t1, 2)
        for r in results:
            r["ai_steps"] = learned.ai_steps(r)
        model_status["log"] = learned.LOG
        model_status["l5_batch"] = l5_batch

    batch_extra = score.combine(results, seed=opts.seed)
    for r in results:
        if r.get("error"):
            r["notes_vi"] = [r["error"]["msg_vi"]]
            continue
        notes = list(((r.get("L2") or {}).get("notes_vi")) or [])
        notes += [f["msg_vi"] for f in r["flags"]][:2]
        r["notes_vi"] = notes[:3]

    if "L6" in L:
        from . import card
        for r in results:
            if r["file"]["stem"] not in ctxs:       # unreadable file: nothing to draw
                continue
            t1 = time.time()
            a, sp, ctx = ctxs[r["file"]["stem"]]
            png = out / f"{r['file']['stem']}.png"
            try:
                card.render(r, ctx, str(png))
                r["card"] = png.name
                if opts.blind_cards:
                    blind = out / f"{r['file']['stem']}.blind.png"
                    card.render(r, ctx, str(blind), blind=True)
                    r["card_blind"] = blind.name
            except Exception as e:  # noqa: BLE001 - a card failure must not lose the scores
                r["card_error"] = f"{type(e).__name__}: {str(e)[:200]}"
            r["timing_s"]["L6"] = round(time.time() - t1, 3)

    batch = report.write(out, results, {
        "created": created, "tool": tool, "stage": opts.stage, "layers": list(opts.layers),
        "refs": {k: v.to_json() for k, v in ref_sets.items()}, "ai_policy": {"ledgers": pol.loaded},
        "models": model_status, "listen": batch_extra["listen"],
        "spec_path": str(spec_path) if spec_path else None, "elapsed_s": round(time.time() - t_all, 2),
    })
    if not opts.quiet:
        report.print_console(results, out)
    return batch
