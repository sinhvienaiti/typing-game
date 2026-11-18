"""Parse multisample file names (VCSL, VSCO-2-CE and similar) into note, dynamics, round robin.

Examples (stem -> descriptor, note, dyn/vel, rr, mic):
  EWHarp_Normal_A#1_v2_RR1      -> ewharp-normal, A#1, v2, rr1
  B1_f_1                        -> "", B1, f, rr1          (VCSL Dan Tranh)
  sus_A#3_r01_main              -> sus, A#3, -, rr1, main  (VCSL Hand Chimes)
  Anvil_Hit1_v1_rr1_Mid         -> anvil-hit1, -, v1, rr1, mid
  gong_2_f                      -> gong-2, -, f
  hit_full2_loudest_ST          -> hit, -, fff (alias), rr2, st
  FX_01                         -> fx-01 (no note/dynamics, so the number is part of the name)

Note names follow scientific pitch (C4 = MIDI 60) here. Libraries disagree on octave numbering
(VCSL Dan Tranh "B1" is MIDI 47), so the index confirms keys with the libraries' own SFZ maps.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

PITCH_CLASS = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}
NOTE_RE = re.compile(r"^([A-Ga-g])(#|s|b)?(-?\d)$")
VEL_RE = re.compile(r"^(?:v|vl|vel)(\d+)$", re.I)
RR_RE = re.compile(r"^(?:rr|r)(\d+)$", re.I)
INT_RE = re.compile(r"^\d+$")

DYN_RANK = {"ppp": 1, "pp": 2, "p": 3, "mp": 4, "mf": 5, "f": 6, "ff": 7, "fff": 8}
# Words that stand for a dynamic only when no real marking (pp..ff) or v<n> is present.
DYN_ALIAS = {"soft": "p", "quiet": "p", "light": "p", "loud": "f", "full": "f", "loudest": "fff"}
ALIAS_RR_RE = re.compile(r"^(soft|quiet|light|loud|full|loudest)(\d+)$", re.I)
MICS = {"mid", "sum", "main", "close", "room", "far", "near", "st", "stereo", "amb", "ambient",
        "mono", "ovh", "oh", "tree", "spot"}

NAMES_SHARP = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")


def note_to_midi(note: str) -> int:
    """'A#1' / 'Bb2' / 'b2' / 'Cs4' / '60' -> MIDI number (C4 = 60)."""
    note = note.strip()
    if INT_RE.match(note):
        return int(note)
    m = NOTE_RE.match(note)
    if not m:
        raise ValueError(f"not a note name: {note!r}")
    pc = PITCH_CLASS[m.group(1).lower()]
    acc = m.group(2) or ""
    pc += 1 if acc in ("#", "s") else -1 if acc == "b" else 0
    return 12 * (int(m.group(3)) + 1) + pc


def midi_to_note(midi: int) -> str:
    return f"{NAMES_SHARP[midi % 12]}{midi // 12 - 1}"


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


@dataclass(frozen=True)
class SampleName:
    stem: str
    descriptor: str            # leftover words, lower-case, '-' joined ("" when none)
    note: str | None           # as written, e.g. "A#1"
    midi_named: int | None     # scientific-pitch reading of `note`
    dyn: str | None            # ppp..fff (aliases mapped)
    vel_layer: int | None      # explicit v<n> / vl<n>
    rr: int | None
    mic: str | None

    @property
    def layer_rank(self) -> tuple[int, int]:
        """Sort key for velocity layers (explicit v<n> first, then dynamics)."""
        return (self.vel_layer or 0, DYN_RANK.get(self.dyn or "", 0))


def tokens(stem: str) -> list[str]:
    return [t for t in re.split(r"[_\-\s]+", stem) if t]


def parse_sample_name(name: str | Path) -> SampleName:
    stem = Path(name).stem
    toks = tokens(stem)
    note = dyn = mic = None
    vel = rr = None
    alias = None
    words: list[tuple[int, str]] = []
    ints: list[tuple[int, str]] = []
    for i, t in enumerate(toks):
        low = t.lower()
        if note is None and NOTE_RE.match(t):
            note = t
        elif low in DYN_RANK:
            dyn = low
        elif VEL_RE.match(t):
            vel = int(VEL_RE.match(t).group(1))
        elif RR_RE.match(t):
            rr = int(RR_RE.match(t).group(1))
        elif low in MICS:
            mic = low
        elif low in DYN_ALIAS:
            alias = max(alias or "ppp", DYN_ALIAS[low], key=lambda d: DYN_RANK[d])
        elif ALIAS_RR_RE.match(t):
            m = ALIAS_RR_RE.match(t)
            a = DYN_ALIAS[m.group(1).lower()]
            alias = max(alias or "ppp", a, key=lambda d: DYN_RANK[d])
            rr = rr if rr is not None else int(m.group(2))
        elif INT_RE.match(t):
            ints.append((i, t))
        else:
            words.append((i, low))
    if dyn is None and vel is None and alias is not None:
        dyn = alias
    # A trailing bare number is a round robin when the name also has a note or a dynamic.
    if ints and rr is None and (note or dyn or vel is not None):
        last_tag = max(i for i, t in enumerate(toks) if t.lower() not in MICS)
        if ints[-1][0] == last_tag:
            rr = int(ints[-1][1])
            ints = ints[:-1]
    desc = "-".join(t for _, t in sorted(words + ints))
    return SampleName(
        stem=stem, descriptor=slug(desc), note=note,
        midi_named=note_to_midi(note) if note else None,
        dyn=dyn, vel_layer=vel, rr=rr, mic=mic,
    )
