"""Read a MIDI file (mido) into sampler notes: tempo map, note on/off pairs, sustain pedal."""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import mido

from sampler.engine import Note


def read_midi(path: str | Path, channel_map: dict[int, str] | None = None, default_instrument: str | None = None,
              transpose: int = 0, sustain_pedal: bool = True) -> tuple[list[Note], dict]:
    """Notes in seconds. channel_map: {0..15: instrument name}; unmapped channels use
    default_instrument, or are skipped (listed in meta['skipped_channels'])."""
    mid = mido.MidiFile(str(path))
    t = 0.0
    held: dict[tuple, list] = defaultdict(list)      # (ch, note) -> [(start, vel)]
    pedal = defaultdict(bool)
    pedal_hold: dict[int, list] = defaultdict(list)  # ch -> [(note, start, vel)]
    notes: list[Note] = []
    tempos, sigs, skipped = [], [], set()

    def inst_for(ch: int) -> str | None:
        if channel_map and ch in channel_map:
            return channel_map[ch]
        return default_instrument

    def finish(ch, note, start, vel, end):
        inst = inst_for(ch)
        if inst is None and channel_map:
            skipped.add(ch)
            return
        notes.append(Note(start=start, midi=note + transpose, velocity=vel, duration=max(0.0, end - start),
                          instrument=inst))

    for msg in mid:                      # merged tracks, msg.time = delta seconds (tempo applied)
        t += msg.time
        if msg.is_meta:
            if msg.type == "set_tempo":
                tempos.append((round(t, 6), round(mido.tempo2bpm(msg.tempo), 4)))
            elif msg.type == "time_signature":
                sigs.append((round(t, 6), f"{msg.numerator}/{msg.denominator}"))
            continue
        if msg.type == "note_on" and msg.velocity > 0:
            held[(msg.channel, msg.note)].append((t, msg.velocity))
        elif msg.type in ("note_off", "note_on"):
            q = held.get((msg.channel, msg.note))
            if q:
                start, vel = q.pop(0)
                if sustain_pedal and pedal[msg.channel]:
                    pedal_hold[msg.channel].append((msg.note, start, vel))
                else:
                    finish(msg.channel, msg.note, start, vel, t)
        elif msg.type == "control_change" and msg.control == 64 and sustain_pedal:
            down = msg.value >= 64
            if pedal[msg.channel] and not down:
                for note, start, vel in pedal_hold.pop(msg.channel, []):
                    finish(msg.channel, note, start, vel, t)
            pedal[msg.channel] = down
    for (ch, note), q in held.items():       # notes never released end with the file
        for start, vel in q:
            finish(ch, note, start, vel, t)
    for ch, items in pedal_hold.items():
        for note, start, vel in items:
            finish(ch, note, start, vel, t)
    notes.sort(key=lambda n: (n.start, n.midi or 0))
    bpm = tempos[0][1] if tempos and tempos[0][0] == 0 else 120.0
    num = int(sigs[0][1].split("/")[0]) if sigs else 4
    meta = {"length": round(t, 6), "ticks_per_beat": mid.ticks_per_beat, "tempos": tempos or [(0.0, 120.0)],
            "time_signatures": sigs or [(0.0, "4/4")], "bpm": bpm, "beats_per_bar": num,
            "skipped_channels": sorted(skipped), "notes": len(notes)}
    return notes, meta


def write_midi(path: str | Path, notes: list[tuple[float, int, float, int]], bpm: float = 120.0,
               channel: int = 0, ticks_per_beat: int = 480) -> Path:
    """Write (start_beats, midi, dur_beats, velocity) notes to a type-0 file (tests, sketches)."""
    mid = mido.MidiFile(type=0, ticks_per_beat=ticks_per_beat)
    tr = mido.MidiTrack()
    mid.tracks.append(tr)
    tr.append(mido.MetaMessage("set_tempo", tempo=mido.bpm2tempo(bpm), time=0))
    tr.append(mido.MetaMessage("time_signature", numerator=4, denominator=4, time=0))
    ev = []
    for start, note, dur, vel in notes:
        ev.append((round(start * ticks_per_beat), 1, mido.Message("note_on", note=note, velocity=vel, channel=channel)))
        ev.append((round((start + dur) * ticks_per_beat), 0,
                   mido.Message("note_off", note=note, velocity=0, channel=channel)))
    now = 0
    for tick, _, msg in sorted(ev, key=lambda e: (e[0], e[1])):
        tr.append(msg.copy(time=tick - now))
        now = tick
    tr.append(mido.MetaMessage("end_of_track", time=0))
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    mid.save(str(path))
    return path
