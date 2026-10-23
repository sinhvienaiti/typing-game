"""Instruments for the sample player: zones built from libraries/index.json or from a folder.

A zone is one sample file with its root key (pitched) or key name (unpitched), velocity range
and round-robin slot. Velocity ranges come from the library SFZ map when it has them, else the
layers found at each root are split evenly over 1..127 (soft to loud).
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from sampler.naming import DYN_RANK, parse_sample_name, slug

AUDIO_EXTS = (".wav", ".wave", ".flac", ".ogg", ".oga", ".mp3", ".aif", ".aiff")
SUSTAIN_WORDS = ("sus", "trem", "vib", "roll", "bowed", "nv", "long")
UNPITCHED_BASE_NOTE = 36   # first MIDI note of an unpitched key map (C2, GM drum area)


@dataclass
class Zone:
    path: Path
    key: str                      # articulation / variant name
    root: int | None              # MIDI root key (None when unpitched)
    rank: tuple = (0, 0)          # velocity order (explicit v<n>, dynamics)
    lovel: int = 0
    hivel: int = 0                # 0 = not assigned yet
    rr: int = 1
    tune_cents: float = 0.0
    sha256: str | None = None
    file: str | None = None       # library-relative path, for provenance
    licence: str | None = None
    pack_path: str | None = None
    f0_cents: float | None = None     # measured deviation from `root` (index --verify-pitch)
    f0_conf: float | None = None
    f0_drift: float | None = None     # cents between the halves of the window (None: no clear peak)


@dataclass
class Instrument:
    id: str
    pitched: bool
    zones: list[Zone]
    mode: str = "oneshot"         # "oneshot" rings to the end; "sustain" fades at note-off
    release: float = 0.3          # seconds, release fade after note-off (sustain or choke)
    default_key: str | None = None
    keymap: dict[str, int] = field(default_factory=dict)
    source: str = ""
    family: str = ""
    notes: list[str] = field(default_factory=list)   # what loading changed (octave fix, tuning)

    def keys(self) -> list[str]:
        return sorted({z.key for z in self.zones})

    def roots(self, key: str | None = None) -> list[int]:
        key = key or self.default_key
        return sorted({z.root for z in self.zones if z.root is not None and (z.key == key or key is None)})

    def playable(self, max_shift: float, key: str | None = None) -> list[int]:
        """MIDI notes reachable within the pitch-shift cap."""
        key = key or self.default_key
        out = set()
        for r in self.roots(key):
            tunes = [z.tune_cents for z in self.zones if z.root == r and z.key == key]
            t = sum(tunes) / len(tunes) / 100.0 if tunes else 0.0
            cap = int(max_shift + 1e-9) + 1
            out |= {r + d for d in range(-cap, cap + 1) if 0 <= r + d <= 127 and abs(d + t) <= max_shift + 1e-6}
        return sorted(out)

    def key_for_midi(self, midi: int) -> str | None:
        for k, n in self.keymap.items():
            if n == midi:
                return k
        return None


def assign_velocity_ranges(zones: list[Zone]) -> None:
    """Split 1..127 between the layers of each (key, root) group, unless all zones have ranges."""
    groups: dict[tuple, list[Zone]] = defaultdict(list)
    for z in zones:
        groups[(z.key, z.root)].append(z)
    for items in groups.values():
        if all(z.hivel > 0 for z in items):
            continue
        ranks = sorted({z.rank for z in items})
        n = len(ranks)
        bounds = [round(127 * (i + 1) / n) for i in range(n)]
        for z in items:
            i = ranks.index(z.rank)
            z.lovel = 1 if i == 0 else bounds[i - 1] + 1
            z.hivel = bounds[i]


def finalize(inst: Instrument) -> Instrument:
    assign_velocity_ranges(inst.zones)
    keys = Counter(z.key for z in inst.zones)
    if inst.default_key is None and keys:
        inst.default_key = keys.most_common(1)[0][0]
    if not inst.pitched and not inst.keymap:
        names = sorted(keys)
        base = UNPITCHED_BASE_NOTE if len(names) <= 128 - UNPITCHED_BASE_NOTE else 0
        inst.keymap = {k: base + i for i, k in enumerate(names) if base + i <= 127}
    return inst


def _mode_for(articulation: str, pitched: bool) -> str:
    a = articulation.lower()
    return "sustain" if pitched and any(w in a for w in SUSTAIN_WORDS) else "oneshot"


# ---------- from the library index ----------

def load_index(path: str | Path | None = None) -> dict:
    if path is None:
        from gen.libraries import INDEX_NAME, ROOT
        path = ROOT / INDEX_NAME
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"chưa có {path}; chạy: run.sh gen.index_library")
    return json.loads(path.read_text())


def resolve_id(index: dict, name: str) -> str:
    """Full id ('vcsl/dan-tranh.normal') or a unique short form ('dan-tranh.normal', 'frame-drum')."""
    ids = list(index["instruments"])
    if name in ids:
        return name
    short = {i: i.split("/", 1)[1] for i in ids}
    exact = [i for i, s in short.items() if s == name]
    if len(exact) == 1:
        return exact[0]
    pref = [i for i, s in short.items() if s.startswith(name + ".")]
    for suffix in (".normal", ".sus", ".susvib"):
        hit = [i for i in pref if i.endswith(suffix)]
        if len(hit) == 1:
            return hit[0]
    if len(pref) == 1:
        return pref[0]
    cands = exact or pref
    if cands:
        raise KeyError(f"'{name}' chưa rõ, chọn một: {', '.join(sorted(cands))}")
    raise KeyError(f"không có nhạc cụ '{name}' trong index (xem: run.sh sampler list)")


def from_index(name: str, index: dict | None = None, root: str | Path | None = None,
               tuning: str = "auto") -> Instrument:
    index = index or load_index()
    iid = resolve_id(index, name)
    meta = index["instruments"][iid]
    root = Path(root or index["root"])
    pitched = meta["kind"] == "pitched"
    entries = [e for e in index["files"] if e["instrument_id"] == iid and not (pitched and e.get("midi") is None)]
    mics = Counter(e.get("mic") for e in entries)
    if len(mics) > 1:   # several mic positions would act as fake round robins: keep the main one
        keep = mics.most_common(1)[0][0]
        entries = [e for e in entries if e.get("mic") == keep]
    zones = []
    for e in entries:
        s = e.get("sfz") or {}
        z = Zone(
            path=root / e["file"], key=e.get("key") or "", root=e.get("midi") if pitched else None,
            rank=(e.get("vel_layer") or 0, DYN_RANK.get(e.get("dyn") or "", 0)), rr=e.get("rr") or 1,
            lovel=s.get("lovel", 0) if s.get("hivel") else 0, hivel=s.get("hivel", 0) or 0,
            tune_cents=float(s.get("tune") or 0.0), sha256=e.get("sha256"), file=e["file"],
            licence=e.get("licence"), pack_path=e.get("pack_path"),
        )
        f0 = e.get("f0") or {}
        if pitched and f0.get("cents") is not None:
            z.f0_cents, z.f0_conf = float(f0["cents"]), float(f0.get("conf") or 0.0)
            z.f0_drift = f0.get("drift_cents")
        zones.append(z)
    if not zones:
        raise KeyError(f"'{iid}' không có mẫu dùng được")
    if pitched:   # one articulation per pitched instrument: keep the main key
        main = Counter(z.key for z in zones).most_common(1)[0][0]
    else:
        main = None
    inst = Instrument(
        id=iid, pitched=pitched, zones=zones,
        mode=meta.get("mode") or _mode_for(iid.split(".", 1)[-1] if "." in iid else "", pitched),
        release=meta.get("release") or 0.3, default_key=main, source="index",
        family=meta.get("family") or "",
    )
    if pitched and any(z.key != main for z in zones):
        for z in zones:            # pitched instruments may mix descriptors; treat them as one key
            z.key = main
    if pitched:
        apply_tuning(inst, meta, tuning)
    return finalize(inst)


NO_AUTOTUNE_FAMILIES = ("instrument/gong", "instrument/idiophone", "instrument/percussion")
STRICT_CONF_FAMILIES = ("instrument/bell",)     # inharmonic: correct only very confident readings
NO_AUTOTUNE_ARTIC = ("vib", "trem", "gliss", "fx", "roll")
# Correct measured deviations in this band (cents). 5 leaves margin under the plan's 10-cent target.
TUNE_MIN_CENTS, TUNE_MAX_CENTS = 5.0, 70.0
# Plucked strings go flat as a loud pluck decays; the reading is their average pitch over 60-660 ms.
# Above this drift there is no single pitch to correct to: leave the sample and say so.
TUNE_MAX_DRIFT = 30.0


def apply_tuning(inst: Instrument, meta: dict, tuning: str) -> None:
    """tuning: 'auto' (octave fix + f0 cents correction where reliable), 'sfz' (library map only), 'none'."""
    if tuning not in ("auto", "sfz", "none"):
        raise ValueError("tuning must be auto, sfz or none")
    if tuning == "none":
        for z in inst.zones:
            z.tune_cents = 0.0
        return
    if tuning == "sfz":
        return
    fix = int(meta.get("octave_fix") or 0)
    if fix:
        for z in inst.zones:
            z.root += fix
            if z.f0_cents is not None:
                z.f0_cents -= 100 * fix
        inst.notes.append(f"octave_fix {fix:+d}: every sample sounds {fix:+d} semitones from its SFZ key")
    artic = inst.id.split(".", 1)[1] if "." in inst.id else ""
    if inst.family.startswith(NO_AUTOTUNE_FAMILIES) or any(w in artic for w in NO_AUTOTUNE_ARTIC):
        return
    fixed, overrode, gliding = 0, 0, []
    min_conf = 0.9 if inst.family.startswith(STRICT_CONF_FAMILIES) else 0.6
    for z in inst.zones:
        c = z.f0_cents
        if c is None or z.f0_drift is None or (z.f0_conf or 0) < min_conf or abs(c) > TUNE_MAX_CENTS:
            continue            # no reliable reading: keep the SFZ tune
        if z.f0_drift > TUNE_MAX_DRIFT:
            if abs(c) > 10:
                gliding.append(f"{Path(z.path).name} {c:+.0f}c drift {z.f0_drift:.0f}c")
            continue
        # A reliable reading replaces the SFZ `tune` (VCSL Folk Harp's map tunes some in-tune samples).
        new = -c if abs(c) > TUNE_MIN_CENTS else 0.0
        overrode += bool(z.tune_cents) and abs(new - z.tune_cents) > 1.0
        fixed += bool(new)
        z.tune_cents = new
    if fixed:
        inst.notes.append(f"tuned {fixed} samples that measured {TUNE_MIN_CENTS:g}-{TUNE_MAX_CENTS:g} cents off "
                          f"(f0 drift <= {TUNE_MAX_DRIFT:g}c, conf >= {min_conf})")
    if overrode:
        inst.notes.append(f"measured f0 replaced the SFZ tune of {overrode} samples")
    if gliding:
        inst.notes.append(f"left {len(gliding)} gliding samples untuned (listen before use): " + ", ".join(gliding))


# ---------- from a folder (owner recordings, tests, other libraries) ----------

def from_folder(folder: str | Path, inst_id: str | None = None, pitched: bool | None = None,
                octave_offset: int = 0, mode: str | None = None, release: float = 0.3) -> Instrument:
    """Scan a folder of samples named like VCSL/VSCO (note, v<n>/dynamics, rr<n>).

    octave_offset: semitones added to every parsed note (12 when names use C3 = middle C).
    """
    folder = Path(folder)
    files = sorted(p for p in folder.rglob("*") if p.is_file() and p.suffix.lower() in AUDIO_EXTS)
    if not files:
        raise FileNotFoundError(f"không có file âm trong {folder}")
    parsed = [(f, parse_sample_name(f.name)) for f in files]
    named = sum(1 for _, n in parsed if n.midi_named is not None)
    if pitched is None:
        pitched = named >= max(2, 0.6 * len(parsed))
    zones = []
    for f, n in parsed:
        if pitched and n.midi_named is None:
            continue
        sub = f.parent.relative_to(folder).as_posix()
        key = n.descriptor or slug(sub) or slug(folder.name)
        zones.append(Zone(path=f, key=key, root=(n.midi_named + octave_offset) if pitched else None,
                          rank=n.layer_rank, rr=n.rr or 1, file=str(f)))
    if pitched:
        main = Counter(z.key for z in zones).most_common(1)[0][0]
        for z in zones:
            z.key = main
    inst = Instrument(id=inst_id or f"folder/{slug(folder.name)}", pitched=pitched, zones=zones,
                      mode=mode or _mode_for(folder.name, pitched), release=release, source=str(folder))
    return finalize(inst)
