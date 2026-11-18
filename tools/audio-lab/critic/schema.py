"""JSON Schema of the per-file result (audiolab.critic.file/1). Bump the version on breaking changes."""
from __future__ import annotations

from .thresholds import SCHEMA_FILE

_NUM = {"type": ["number", "null"]}
_FLAG = {
    "type": "object",
    "required": ["layer", "id", "msg_vi"],
    "properties": {"layer": {"enum": ["L1b", "L4", "L5"]}, "id": {"type": "string"}, "msg_vi": {"type": "string"}},
}
_LAYER = {"type": ["object", "null"]}
_CHECK = {
    "type": "object",
    "required": ["id", "label_vi", "measured_on", "ok", "fix", "blocking"],
    "properties": {
        "id": {"type": "string"}, "label_vi": {"type": "string"},
        "measured_on": {"enum": ["raw", "fixed", "both"]}, "ok": {"type": "boolean"},
        "fix": {"type": "string"}, "blocking": {"type": "boolean"}, "msg_vi": {"type": "string"},
    },
}

FILE_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": SCHEMA_FILE,
    "title": "Audio Lab critic: one file",
    "type": "object",
    "required": ["schema", "tool", "created", "file", "spec", "stage", "layers", "verdict", "metrics",
                 "L1", "L1b", "L2", "L3", "L4", "L5", "flags", "score", "ask_owner", "read_card", "notes_vi",
                 "card", "cloud_ok", "ai_policy", "ai_steps", "refs", "timing_s"],
    "properties": {
        "schema": {"const": SCHEMA_FILE},
        "tool": {"type": "object", "required": ["name", "version", "layers"]},
        "created": {"type": "string"},
        "file": {"type": "object", "required": ["path", "name", "stem", "sha256", "sample_rate", "channels", "duration_s"],
                 "properties": {"sha256": {"type": "string"}, "sample_rate": {"type": "integer"},
                                "channels": {"type": "integer"}, "duration_s": {"type": "number"}}},
        "spec": {"type": "object", "required": ["group", "group_source", "family", "loop", "dirty"]},
        "stage": {"enum": ["final", "raw"]},
        "layers": {"type": "array", "items": {"enum": ["L1", "L1b", "L2", "L3", "L4", "L5", "L6"]}},
        "verdict": {"enum": ["PASS", "NEEDS_FIX", "BLOCK", "UNGATED"]},
        "metrics": {"type": "object", "required": ["duration_ms", "peak_dbfs", "true_peak_dbtp", "dc_offset",
                                                    "head_silence_ms", "silent"]},
        "L1": {"type": ["object", "null"], "required": ["stage", "pass", "verdict", "blocking", "fixes", "checks"],
               "properties": {"checks": {"type": "array", "items": _CHECK},
                              "verdict": {"enum": ["PASS", "NEEDS_FIX", "BLOCK"]}}},
        "L1b": {"type": ["object", "null"], "required": ["metrics", "flags", "thresholds_source"]},
        "L2": {"type": ["object", "null"], "required": ["score", "targets", "notes_vi", "psycho"],
               "properties": {"score": _NUM, "psycho": {"type": "object", "required": ["available"]}}},
        "L3": _LAYER, "L4": _LAYER, "L5": _LAYER,
        "flags": {"type": "array", "items": _FLAG},
        "score": {"type": "object", "required": ["combined", "stage", "rank_group", "rank", "rank_l2", "rank_l3"],
                  "properties": {"combined": _NUM, "stage": {"enum": ["batch1", "batch1-dirty", "ref5", "ref5-dirty"]}}},
        "ask_owner": {"type": "object", "required": ["value", "reasons"],
                      "properties": {"value": {"type": "boolean"}, "reasons": {"type": "array", "items": {"type": "string"}}}},
        "read_card": {"type": "boolean"},
        "notes_vi": {"type": "array", "items": {"type": "string"}},
        "card": {"type": ["string", "null"]},
        "card_blind": {"type": ["string", "null"], "description": "Listening Board card: no name, verdict or score"},
        "cloud_ok": {"type": "boolean"},
        "ai_policy": {"type": "object", "required": ["allowed", "reason"],
                      "properties": {"allowed": {"type": "boolean"}, "reason": {"type": ["string", "null"]}}},
        "ai_steps": {"type": "array", "items": {"type": "object", "required": ["step", "model"]}},
        "refs": {"type": "object", "required": ["set", "n"],
                 "properties": {"set": {"type": ["string", "null"]}, "n": {"type": "integer"}}},
        "timing_s": {"type": "object"},
    },
}
