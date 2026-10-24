"""Math checks for blender/static_model_tools.py, run inside Blender (bpy and numpy):
  blender --background --factory-startup --python-exit-code 1 --python scripts/models/test/static_model_tools_check.py
"""
import os
import sys

import numpy as np

sys.dont_write_bytecode = True  # no __pycache__ next to the helper
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "blender"))
import static_model_tools as smt  # noqa: E402


def ring_points(centre, radius, count=720, height=1.0):
    angles = np.linspace(0, 2 * np.pi, count, endpoint=False)
    base = np.stack([centre[0] + radius * np.cos(angles), np.zeros(count), centre[1] + radius * np.sin(angles)], axis=1)
    top = base.copy()
    top[:, 1] = height
    return np.concatenate([base, top])


# A round base of radius 1.5 centred at (0.4, 0.1) and a small platform standing
# off it at -X (the keep, barracks, seal dais): found without help.
base = ring_points((0.4, 0.1), 1.5, height=6.0)
xs, zs = np.meshgrid(np.linspace(-2.3, -1.5, 17), np.linspace(-0.8, 0.0, 17))
small = np.stack([xs.ravel(), np.full(xs.size, 0.5), zs.ravel()], axis=1)
x, z, radius = smt.ring_fit(np.concatenate([base, small]))
assert abs(x - 0.4) < 0.05 and abs(z - 0.1) < 0.05, (x, z)
assert abs(radius - 1.5) < 0.05, radius
assert abs(smt.footprint(np.concatenate([base, small])) - 3.0) < 0.1

# A wide platform against the base (the archer): an exclusion box gives the base ring.
xs, zs = np.meshgrid(np.linspace(-2.3, -1.15, 25), np.linspace(-1.4, 0.6, 25))
wide = np.stack([xs.ravel(), np.full(xs.size, 0.5), zs.ravel()], axis=1)
points = np.concatenate([base, wide])
lo, hi = points.min(axis=0), points.max(axis=0)
cut = (-1.12 - (lo[0] + hi[0]) / 2) / ((hi[0] - lo[0]) / 2)  # the platform, not the base (x >= -1.1)
x2, z2, radius2 = smt.ring_fit(points, exclude=[[-1, -1, cut, 1]])
assert abs(x2 - 0.4) < 0.05 and abs(z2 - 0.1) < 0.05 and abs(radius2 - 1.5) < 0.05, (x2, z2, radius2)

# An oval with a drum and a platform at its front corners (the barracks): boxes
# take them out, the ring is centred on the oval.
angles = np.linspace(0, 2 * np.pi, 720, endpoint=False)
fence = np.stack([0.1 + 2.2 * np.cos(angles), np.zeros(720), 0.2 + 1.5 * np.sin(angles)], axis=1)
drum = np.array([[1.2, 0.3, -1.6], [1.5, 0.3, -1.7], [1.0, 0.3, -1.65]])
points = np.concatenate([fence, drum])
lo, hi = points.min(axis=0), points.max(axis=0)
frac_z = lambda z: (z - (lo[2] + hi[2]) / 2) / ((hi[2] - lo[2]) / 2)
x4, z4, radius4 = smt.ring_fit(points, exclude=[[-1, -1, 1, frac_z(-1.4)]])
assert abs(x4 - 0.1) < 0.05 and abs(z4 - 0.2) < 0.05 and 2.0 < radius4 <= 2.2, (x4, z4, radius4)

# An oval (4.6 x 3.6, the barracks fence) gets an approximate ring: near its
# middle, reaching about its long half-axis.
angles = np.linspace(0, 2 * np.pi, 720, endpoint=False)
oval = np.stack([2.3 * np.cos(angles), np.zeros(720), 1.8 * np.sin(angles)], axis=1)
x3, z3, radius3 = smt.ring_fit(oval)
assert abs(x3) < 0.25 and abs(z3) < 0.25 and 2.0 < radius3 < 2.45, (x3, z3, radius3)

# Colour: luminance moves part of the way, each channel stays between 1 and its target ratio.
spec = {"strength": 0.6, "minGain": 1.0, "maxGain": 1.5, "maxTint": 0.12}
for rendered, target in [((0.40, 0.20, 0.02), (0.45, 0.30, 0.04)), ((0.3, 0.3, 0.3), (0.2, 0.25, 0.3)), ((0.05, 0.05, 0.05), (0.6, 0.6, 0.6))]:
    rendered, target = np.array(rendered), np.array(target)
    gains = smt.colour_gains(spec, rendered, target)
    ratio = target / rendered
    assert np.all(gains >= np.minimum(ratio, 1.0) - 1e-9) and np.all(gains <= np.maximum(ratio, 1.0) + 1e-9), (gains, ratio)
    assert np.all(gains <= 1.5 * (1 + 0.12) + 1e-9), gains

# Roll-off: monotonic, never above 1, identity below the knee and for gains <= 1.
values = np.linspace(0, 1, 101)[:, None].repeat(3, axis=1)
out = smt.roll_off(values.copy(), np.array([1.4, 1.0, 0.8]))
assert np.all(np.diff(out[:, 0]) >= 0) and out[:, 0].max() <= 1.0 + 1e-9
assert np.allclose(out[:, 1], values[:, 1]) and np.allclose(out[:, 2], values[:, 2] * 0.8)
assert np.allclose(out[values[:, 0] * 1.4 <= 0.8, 0], values[values[:, 0] * 1.4 <= 0.8, 0] * 1.4)
print("static checks passed")
