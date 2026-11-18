"""Records shared by the readers, the builder and the report."""
from __future__ import annotations

import re
from dataclasses import dataclass, field

# Issue severities, worst first in the report.
DISAGREE = "disagree"   # code catalog and sound list say different things
PLAN = "plan"           # AUDIO_PIPELINE proposes something the game docs do not (game docs win)
RANGE = "range"         # value outside the plan's §4.3.3 starting range (rank only, never a gate)
STALE = "stale"         # a reader could not find a rule text it relies on: check the reader
INFO = "info"


@dataclass
class Issue:
    game: str
    id: str | None
    kind: str
    detail: str
    severity: str = DISAGREE
    code: object = None
    listing: object = None

    def as_dict(self) -> dict:
        return {"game": self.game, "id": self.id, "kind": self.kind, "severity": self.severity,
                "detail": self.detail, "code": self.code, "list": self.listing}


@dataclass
class Entry:
    id: str
    game: str
    in_code: bool = False
    in_list: bool = False
    proposed: str | None = None     # basis when the id comes from the plan or prose only
    code: dict = field(default_factory=dict)
    listing: dict = field(default_factory=dict)


@dataclass
class GameData:
    game: str
    label: str
    files: dict[str, str]             # role -> path relative to the game folder
    entries: list[Entry]
    issues: list[Issue]
    bus_levels: dict[str, dict]       # bus -> {"code": {...}, "doc": {...}}
    context: dict                     # game-wide rules (see readers/*)
    rules: list[tuple[str, dict]]     # (id regex, classification), first match wins

    def entry(self, sound_id: str) -> Entry | None:
        for e in self.entries:
            if e.id == sound_id:
                return e
        return None

    def rule_for(self, sound_id: str) -> dict | None:
        for pattern, rule in self.rules:
            if re.fullmatch(pattern, sound_id):
                return rule
        return None
