"""Recipe loading, validation, hashing and seeded variant planning (§5.1 step 9, §5.3)."""
from __future__ import annotations

import copy
import hashlib
import json
import zlib
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import yaml

from build import ledger, policy

SCHEMA_ID = "audiolab.recipe/1"

CHAIN_DEFAULTS = {
    "dcHpfHz": 35.0,
    "hpfHz": None,
    "filters": [],
    "saturation": None,
    "headTrim": {"thresholdDb": -50.0, "preRollMs": 0.5},
    "maxLengthMs": None,
    "tail": {"floorDb": -60.0, "fadeMs": 10.0},
    "loopCrossfadeMs": 0.0,
    "normalise": {"mode": "lufs-m-max", "target": -20.0},
    "limiter": {"ceilingDbtp": -1.0, "releaseMs": 60.0, "maxGrDb": 6.0},
}
LOOP_CHAIN = {"headTrim": None, "tail": None, "normalise": {"mode": "lufs-i", "target": -26.0}}


class RecipeError(ValueError):
    pass


def load(path: Path | str) -> dict:
    path = Path(path)
    data = json.loads(path.read_text(encoding="utf-8"))
    validate(data, str(path))
    return data


def validate(data: dict, where: str = "recipe") -> None:
    errs = ledger.schema_errors("recipe", data)
    if errs:
        raise RecipeError(f"{where}: công thức không hợp lệ:\n  " + "\n  ".join(errs[:12]))
    ids = [layer["id"] for layer in data["layers"]]
    if len(ids) != len(set(ids)):
        raise RecipeError(f"{where}: id lớp bị trùng: {ids}")


def recipe_hash(data: dict) -> str:
    """sha256 of the canonical recipe, ignoring prose fields."""
    core = {k: v for k, v in data.items() if k not in ("$schema", "description", "notes")}
    blob = json.dumps(core, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def chain_params(data: dict) -> dict:
    """Recipe chain merged over defaults (loops: no head trim, no tail fade, LUFS-I)."""
    base = copy.deepcopy(CHAIN_DEFAULTS)
    if data.get("loop"):
        base.update(copy.deepcopy(LOOP_CHAIN))
    for k, v in (data.get("chain") or {}).items():
        if isinstance(v, dict) and isinstance(base.get(k), dict):
            base[k] = {**base[k], **v}
        else:
            base[k] = v
    return base


def export_stem(data: dict) -> str:
    exp = data.get("export") or {}
    return exp.get("path") or "sfx/" + data["id"].replace(".", "-")


# ---------------------------------------------------------------- variants

def read_spec(spec_path: Path | str | None) -> dict | None:
    """Variation hints from a spec card (specs lane, card.schema.json).

    `randomisation: {group, pitch_cents, gain_db}` -> limits (null gain with a pitch limit = 0 dB,
    both null = no limit); `variants.target` -> default count. Also accepts `variation: {pitchCents, gainDb}`.
    """
    if spec_path is None:
        return None
    card = yaml.safe_load(Path(spec_path).read_text(encoding="utf-8")) or {}
    out: dict = {"path": str(spec_path), "id": card.get("id"), "group": None, "limits": None, "count": None}
    rnd = card.get("randomisation")
    if isinstance(rnd, dict) and ("pitch_cents" in rnd or "gain_db" in rnd):
        pc, gd = rnd.get("pitch_cents"), rnd.get("gain_db")
        out["group"] = rnd.get("group")
        if pc is not None or gd is not None:
            out["limits"] = (None if pc is None else float(pc), 0.0 if gd is None else float(gd))
        out["hasLimits"] = True
    else:
        for key in ("variation", "variants", "random"):
            v = card.get(key)
            if isinstance(v, dict) and ("pitchCents" in v or "gainDb" in v):
                out["limits"] = (float(v.get("pitchCents", 0)), float(v.get("gainDb", 0)))
                out["hasLimits"] = True
                break
    var = card.get("variants")
    if isinstance(var, dict) and isinstance(var.get("target"), int):
        out["count"] = var["target"]
    return out


def read_spec_limits(spec_path: Path | str | None) -> tuple[float | None, float | None] | None:
    spec = read_spec(spec_path)
    return spec["limits"] if spec else None


def limits_for(data: dict, spec: dict | tuple | None) -> tuple[tuple[float | None, float | None] | None, str]:
    """Spec card limits win over the recipe group; None = unlimited."""
    if isinstance(spec, tuple):
        return spec, "spec"
    if spec and spec.get("hasLimits"):
        return spec["limits"], f"spec:{spec.get('group') or 'card'}"
    group = policy.group_name(data.get("group"))
    if group is None:
        return None, "none"
    if group not in policy.VARIATION_LIMITS:
        return None, f"unknown-group:{group}"
    return policy.VARIATION_LIMITS[group], f"group:{group}"


def _clamp(rng_pair, limit: float | None, what: str, warnings: list[str]) -> tuple[float, float]:
    lo, hi = (float(rng_pair[0]), float(rng_pair[1])) if rng_pair else (0.0, 0.0)
    if lo > hi:
        lo, hi = hi, lo
    if limit is None:
        return lo, hi
    c_lo, c_hi = max(lo, -limit), min(hi, limit)
    if (c_lo, c_hi) != (lo, hi):
        warnings.append(f"{what}: khoảng [{lo}, {hi}] vượt giới hạn ±{limit}, đã thu về [{c_lo}, {c_hi}]")
    return c_lo, max(c_lo, c_hi)


@dataclass
class LayerPlan:
    layer_id: str
    source: dict
    swap_index: int = 0          # 0 = the layer's own source
    pitch_cents: float = 0.0
    gain_db: float = 0.0
    offset_ms: float = 0.0
    synth_seed: int = 0


@dataclass
class VariantPlan:
    n: int
    seed: int
    base: bool
    pitch_cents: float = 0.0
    gain_db: float = 0.0
    layers: dict[str, LayerPlan] = field(default_factory=dict)

    def to_json(self) -> dict:
        return {
            "variant": self.n, "seed": self.seed, "base": self.base,
            "pitchCents": round(self.pitch_cents, 3), "gainDb": round(self.gain_db, 3),
            "layers": {k: {"swap": v.swap_index, "pitchCents": round(v.pitch_cents, 3),
                           "gainDb": round(v.gain_db, 3), "offsetMs": round(v.offset_ms, 3),
                           "synthSeed": v.synth_seed} for k, v in self.layers.items()},
        }


def _u(rng: np.random.Generator, lo: float, hi: float) -> float:
    return float(rng.uniform(lo, hi)) if hi > lo else float(lo)


def plan_variants(data: dict, spec: dict | tuple | None = None,
                  seed_override: int | None = None, count_override: int | None = None) -> tuple[list[VariantPlan], list[str], str]:
    """Seeded plan: same recipe + seed -> same plan. Returns (plans, warnings, limit source)."""
    v = data.get("variants") or {}
    spec_count = spec.get("count") if isinstance(spec, dict) else None
    count = int(count_override or v.get("count") or spec_count or 1)
    seed = int(seed_override if seed_override is not None else v.get("seed", 0))
    include_base = bool(v.get("includeBase", True))
    warnings: list[str] = []
    limits, limit_src = limits_for(data, spec)
    if limit_src.startswith("unknown-group"):
        warnings.append(f"nhóm '{data.get('group')}' không có trong bảng 5.3; không giới hạn biến thể")
    p_lim, g_lim = limits if limits else (None, None)
    g_pitch = _clamp(v.get("pitchCents"), p_lim, "variants.pitchCents", warnings)
    g_gain = _clamp(v.get("gainDb"), g_lim, "variants.gainDb", warnings)
    layer_ranges = {}
    for layer in data["layers"]:
        vary = layer.get("vary") or {}
        layer_ranges[layer["id"]] = (
            _clamp(vary.get("pitchCents"), p_lim, f"{layer['id']}.vary.pitchCents", warnings),
            _clamp(vary.get("gainDb"), g_lim, f"{layer['id']}.vary.gainDb", warnings),
            _clamp(vary.get("offsetMs"), None, f"{layer['id']}.vary.offsetMs", warnings),
            [layer["source"], *vary.get("swap", [])],
            vary.get("reseed", True),
            vary.get("swapMode", "random"),
        )
    plans = []
    for n in range(1, count + 1):
        base = include_base and n == 1
        rng = np.random.default_rng(np.random.SeedSequence([seed, n]))
        plan = VariantPlan(n=n, seed=seed, base=base)
        if not base:
            plan.pitch_cents = _u(rng, *g_pitch)
            plan.gain_db = _u(rng, *g_gain)
        for layer in data["layers"]:
            lid = layer["id"]
            (pc, gd, om, sources, reseed, swap_mode) = layer_ranges[lid]
            lp = LayerPlan(layer_id=lid, source=sources[0])
            # Draw in a fixed order for every layer so plans stay stable when ranges change to zero.
            draws = (_u(rng, *pc), _u(rng, *gd), _u(rng, *om), int(rng.integers(len(sources))))
            if not base:
                lp.pitch_cents, lp.gain_db, lp.offset_ms, lp.swap_index = draws
            if swap_mode == "cycle":            # deliberate combos: variant n -> source n-1
                lp.swap_index = (n - 1) % len(sources)
            lp.source = sources[lp.swap_index]
            salt = zlib.crc32(lid.encode("utf-8"))
            lp.synth_seed = int(np.random.SeedSequence([seed, n if reseed else 1, salt]).generate_state(1)[0])
            plan.layers[lid] = lp
        plans.append(plan)
    if isinstance(spec, dict) and spec.get("id") and spec["id"] != data["id"]:
        warnings.append(f"thẻ spec là của id '{spec['id']}', công thức là '{data['id']}'")
    if limits == (0, 0) and count > 1:
        warnings.append("nhóm này không đổi ngẫu nhiên cao độ/độ to (5.3); biến thể chỉ khác ở lớp hoán đổi")
    return plans, warnings, limit_src
