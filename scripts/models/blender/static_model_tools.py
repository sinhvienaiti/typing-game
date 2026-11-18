"""
Static model helper: one unrigged Tripo/Meshy GLB -> one game-ready GLB.

Generic (any game). The Space Typing helper (space_typing_model_tools.py) stays
byte-identical to Space's copy; this file is for props, buildings, projectiles,
loot and attachments that carry no rig and no clip.

Headless only:
  blender --background --factory-startup --python static_model_tools.py -- \
    --input art-src/3d/<kind>/<id>.glb --output art-src/models/<kind>/<id>.glb \
    --id <kind>/<id> --spec '<json>' [--reference <2D png>] [--report <json>] [--preview <dir>]

Every length is metres and every coordinate is in the glTF/game frame:
+Y up, the model's front faces -Z, +X is the model's own right (a character
facing -Z holds its right hand at +X). Steps, in order:

  1. Import into an empty scene with merge_vertices: a plain glTF import
     splits the mesh at every UV/normal seam, and decimating split pieces
     opens cracks; merged, the seams are only UV seams and stay locked.
  2. Join meshes; refuse a file with an armature (rigged models go elsewhere).
  3. Orient: "rotate" (row-major 3x3) then "yaw" (degrees about +Y; +90 turns
     +X to -Z). Tripo puts the picture's view direction at +X, so a front
     picture usually needs yaw 90.
  4. Scale uniformly so "size.measure" equals "size.metres" (with
     "size.maxHeight", no taller than that: a building fills its ring unless
     that would make it taller than its design window):
     height (Y extent), width (X), depth/length (Z), or footprint = diameter
     of the occupation ring fitted to the outline of the lowest quarter (the
     assist platform and stairs that stick out do not count; see ring_fit).
  5. Pivot: "base" (bounding-box centre, lowest point), "centre", "feet"
     (centre of the lowest 2 % of vertices), "footprint" (centre of the
     occupation ring, on the ground; "ringExclude" boxes help the fit, see
     ring_fit) or {"frac": [fx, fy, fz]} (bounding box, -1..1), then
     "pivotOffset" (metres) moves the pivot.
  6. Decimate (collapse) to "triangles". UV seams and open borders are locked
     with a vertex group, so islands cannot crack apart; normals are then
     transferred from the undecimated copy so shading does not change.
  7. Colour: "colour.gain" (linear RGB gains) or "colour.match" with
     --reference: the base colour is rendered unlit from the picture's view,
     its mean is compared with the picture's foreground mean (chroma key);
     the brightness moves "strength" of the way (log space) toward it within
     [minGain, maxGain], the hue the same share within 1 +- maxTint (see
     colour_gains). Values a gain would push past white roll off (gain <= 1
     leaves the curve linear). Never past the picture's mean. A new PNG
     texture is written; the source image is not modified.
     Then "material": {"metallic": scale, "roughnessMin": floor} rewrites the
     metallic-roughness texture (new image): Tripo marks painted gold as
     metal, which PBR lighting turns brown.
  8. Sockets: Empties named FX_*, parented to the mesh. Each value is
     [x, y, z] | {"at": [x, y, z]} | {"frac": [fx, fy, fz]} |
     {"ray": "-y|+y|-x|+x|-z|+z", "x"|"fx": .., "y"|"fy": .., "z"|"fz": .., "start"?: ..}
     (first hit along the axis through the given line, from outside the model,
     or from "start" on that axis, e.g. a floor under a roof) |
     {"from": "FX_other"}; each may add "offset": [dx, dy, dz].
  9. "expect": {"height"|"width"|"depth"|"footprint": [min, max]} reports a
     size more than 20 % outside its window as a warning.
 10. Export GLB (+Y up). --report writes the numbers; --preview renders
     before/after 3/4 views (EEVEE, lit) and unlit, plus front and top
     (after export, so preview objects never ship).
"""

import argparse
import json
import math
import os
import shutil
import sys
import tempfile

import bmesh
import bpy
import numpy as np
from mathutils import Matrix, Vector
from mathutils.bvhtree import BVHTree

# glTF (x, y, z) <-> Blender (x, -z, y)
def to_blender(p):
    return Vector((p[0], -p[2], p[1]))


def to_gltf(v):
    return [v.x, v.z, -v.y]


C = Matrix(((1, 0, 0), (0, 0, -1), (0, 1, 0)))  # glTF -> Blender basis change

MEASURES = ("height", "width", "depth", "length", "footprint")
AXES = {"x": 0, "y": 1, "z": 2}


def log(*parts):
    print("[static]", *parts, flush=True)


# ----------------------------------------------------------------------------
def parse():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    parser = argparse.ArgumentParser(prog="static_model_tools.py")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--id", default="model")
    parser.add_argument("--spec", required=True, help="JSON object (see the module docstring)")
    parser.add_argument("--reference", default="", help="2D picture the colours are matched to")
    parser.add_argument("--report", default="")
    parser.add_argument("--preview", default="")
    args = parser.parse_args(argv)
    spec = json.loads(args.spec)
    if not isinstance(spec, dict):
        raise SystemExit("--spec must be a JSON object")
    return args, spec


def import_input(path):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=path, merge_vertices=True)
    for obj in list(bpy.context.scene.objects):
        if obj.type in ("LIGHT", "CAMERA"):
            bpy.data.objects.remove(obj, do_unlink=True)
    if any(o.type == "ARMATURE" for o in bpy.context.scene.objects):
        raise SystemExit("input has an armature; the static helper only takes unrigged models")
    meshes = [o for o in bpy.context.scene.objects if o.type == "MESH"]
    if not meshes:
        raise SystemExit("input has no mesh")
    select_only(meshes)
    if len(meshes) > 1:
        bpy.ops.object.join()
    obj = bpy.context.view_layer.objects.active
    # Clear parents/empties from the importer; keep only the mesh.
    for other in list(bpy.context.scene.objects):
        if other is not obj and other.type == "EMPTY":
            bpy.data.objects.remove(other, do_unlink=True)
    if obj.parent is not None:
        matrix = obj.matrix_world.copy()
        obj.parent = None
        obj.matrix_world = matrix
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    return obj


def select_only(objects):
    bpy.ops.object.select_all(action="DESELECT")
    for o in objects:
        o.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]


def triangles(obj):
    obj.data.calc_loop_triangles()
    return len(obj.data.loop_triangles)


def gltf_points(obj):
    """Vertex positions in the glTF frame as an (n, 3) array."""
    co = np.empty(len(obj.data.vertices) * 3, dtype=np.float64)
    obj.data.vertices.foreach_get("co", co)
    co = co.reshape(-1, 3)
    m = np.array(obj.matrix_world)
    world = co @ m[:3, :3].T + m[:3, 3]
    return np.stack([world[:, 0], world[:, 2], -world[:, 1]], axis=1)


def bounds(points):
    return points.min(axis=0), points.max(axis=0)


# ----------------------------------------------------------------------------
def orientation(spec):
    rotation = Matrix.Identity(3)
    if spec.get("rotate") is not None:
        values = [float(v) for v in spec["rotate"]]
        rows = Matrix((values[0:3], values[3:6], values[6:9]))
        if abs(rows.determinant() - 1.0) > 1e-3:
            raise SystemExit("rotate must be a proper rotation (determinant 1)")
        rotation = rows
    yaw = math.radians(float(spec.get("yaw", 0.0)))
    if yaw:
        c, s = math.cos(yaw), math.sin(yaw)
        rotation = Matrix(((c, 0, s), (0, 1, 0), (-s, 0, c))) @ rotation
    return rotation  # glTF frame


def ring_fit(points, exclude=None, step=5, tolerance=0.12, tries=600):
    """Occupation ring of a building, seen from above. The lowest quarter of
    the model is cut into 5-degree sectors around its box centre; each
    sector's outermost point is a point of the outline. A circle is fitted to
    that outline by RANSAC (seeded, so repeatable): the circle through three
    outline points that the most other points lie within 12 % of wins, then a
    least-squares fit on the points in that band refines it. An assist platform, side
    stairs or a drum sticking out are not on the circle and do not count.
    "exclude" lists boxes [fx0, fz0, fx1, fz1] in fractions of the model's
    bounding box (-1..1, X and Z) whose points are not part of the outline:
    for a platform the fit cannot tell from the base, or an oval base. With
    boxes, the rest of the outline is the base: the ring is centred on its box.
    Returns (centre x, centre z, radius)."""
    lo, hi = bounds(points)
    xz = points[points[:, 1] <= lo[1] + 0.25 * (hi[1] - lo[1])][:, [0, 2]]
    if exclude:
        centre2, half2 = (lo[[0, 2]] + hi[[0, 2]]) / 2, np.maximum((hi[[0, 2]] - lo[[0, 2]]) / 2, 1e-9)
        frac = (xz - centre2) / half2
        drop = np.zeros(len(xz), dtype=bool)
        for fx0, fz0, fx1, fz1 in exclude:
            drop |= (frac[:, 0] >= min(fx0, fx1)) & (frac[:, 0] <= max(fx0, fx1)) & (frac[:, 1] >= min(fz0, fz1)) & (frac[:, 1] <= max(fz0, fz1))
        xz = xz[~drop]
    origin = (xz.min(axis=0) + xz.max(axis=0)) / 2
    d = xz - origin
    radius = np.hypot(d[:, 0], d[:, 1])
    sector = ((np.degrees(np.arctan2(d[:, 1], d[:, 0])) % 360) // step).astype(int)
    outline = []
    for index in range(360 // step):
        inside = np.nonzero(sector == index)[0]
        if inside.size:
            outline.append(xz[inside[np.argmax(radius[inside])]])
    outline = np.array(outline)

    def fit(subset):  # algebraic (Kasa) circle
        a = np.column_stack([subset[:, 0], subset[:, 1], np.ones(len(subset))])
        b = (subset ** 2).sum(axis=1)
        sx, sz, c = np.linalg.lstsq(a, b, rcond=None)[0]
        centre = np.array([sx / 2, sz / 2])
        return centre, float(np.sqrt(max(c + centre @ centre, 1e-12)))

    def near(centre, r, share=tolerance):
        reach = np.hypot(*(outline - centre).T)
        return np.abs(reach - r) <= share * r

    low, high = outline.min(axis=0), outline.max(axis=0)
    span = float(np.linalg.norm(high - low))

    def plausible(centre, r):  # nearly straight edges fit huge circles: refuse them
        return r <= 0.6 * span and np.all(centre >= low) and np.all(centre <= high)

    rng = np.random.default_rng(0)
    best, best_count = None, -1
    for _ in range(tries):
        centre, r = fit(outline[rng.choice(len(outline), 3, replace=False)])
        if not plausible(centre, r):
            continue
        count = int(near(centre, r).sum())
        if count > best_count:
            best, best_count = (centre, r), count
    centre, r = best
    # Least squares on the points in the band: an oval or a rounded square gets
    # its average circle. A platform that touches the base inside the band
    # would pull it: give that one a "ringExclude" box.
    for _ in range(3):
        refined = fit(outline[near(centre, r)])
        if not plausible(*refined):
            break
        centre, r = refined
    kept = outline[near(centre, r)]
    if exclude:
        # The boxes already took the platform out: what is left is the base,
        # whatever its shape (round, oval, rounded square). Centre on its box.
        kept = outline
        centre = (kept.min(axis=0) + kept.max(axis=0)) / 2
    reach = np.hypot(*(kept - centre).T)
    return float(centre[0]), float(centre[1]), float(np.percentile(reach, 90) if reach.size else r)


def footprint(points, exclude=None):
    """Diameter of the occupation ring (see ring_fit)."""
    return 2.0 * ring_fit(points, exclude)[2]


def footprint_centre(points, exclude=None):
    """Ring centre on the ground."""
    x, z, _radius = ring_fit(points, exclude)
    return np.array([x, points[:, 1].min(), z])


def measure(points, kind, exclude=None):
    lo, hi = bounds(points)
    size = hi - lo
    if kind == "height":
        return float(size[1])
    if kind == "width":
        return float(size[0])
    if kind in ("depth", "length"):
        return float(size[2])
    if kind == "footprint":
        return footprint(points, exclude)
    raise SystemExit("size.measure must be one of " + ", ".join(MEASURES))


def place(obj, spec):
    """Rotate, scale and move the pivot to the origin (applied to the mesh)."""
    rotation = orientation(spec)
    obj.matrix_world = (C @ rotation @ C.inverted()).to_4x4() @ obj.matrix_world
    bpy.context.view_layer.update()
    select_only([obj])
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    size = spec.get("size") or {}
    points = gltf_points(obj)
    scale = 1.0
    if size:
        current = measure(points, size["measure"], spec.get("ringExclude"))
        if current <= 1e-9:
            raise SystemExit("cannot measure " + size["measure"])
        scale = float(size["metres"]) / current
        # Fill the ring, but never past the top of the design height window.
        if size.get("maxHeight"):
            height = float(points[:, 1].max() - points[:, 1].min())
            scale = min(scale, float(size["maxHeight"]) / height)
    obj.scale = (scale, scale, scale)
    bpy.context.view_layer.update()
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    points = gltf_points(obj)
    lo, hi = bounds(points)
    centre = (lo + hi) / 2
    pivot_mode = spec.get("pivot", "base")
    if pivot_mode == "base":
        pivot = np.array([centre[0], lo[1], centre[2]])
    elif pivot_mode == "centre":
        pivot = centre
    elif pivot_mode == "feet":
        low = points[points[:, 1] <= lo[1] + 0.02 * (hi[1] - lo[1])]
        pivot = np.array([low[:, 0].mean(), lo[1], low[:, 2].mean()])
    elif pivot_mode == "footprint":
        pivot = footprint_centre(points, spec.get("ringExclude"))
    elif isinstance(pivot_mode, dict) and "frac" in pivot_mode:
        pivot = centre + np.array(pivot_mode["frac"], dtype=float) * (hi - lo) / 2
    else:
        raise SystemExit("pivot must be base, centre, feet, footprint or {frac: [x, y, z]}")
    pivot = pivot + np.array(spec.get("pivotOffset", [0, 0, 0]), dtype=float)
    obj.location = -to_blender(pivot)
    bpy.context.view_layer.update()
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
    return rotation, scale


# ----------------------------------------------------------------------------
def lock_seams(obj):
    """Vertex group "free": 1 inside UV islands, 0 on seams and open borders."""
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    uv = bm.loops.layers.uv.active
    locked = set()
    for v in bm.verts:
        if v.is_boundary:
            locked.add(v.index)
            continue
        if uv is not None:
            seen = {(round(l[uv].uv.x, 5), round(l[uv].uv.y, 5)) for l in v.link_loops}
            if len(seen) > 1:
                locked.add(v.index)
    bm.free()
    group = obj.vertex_groups.new(name="StaticFree")
    free = [i for i in range(len(obj.data.vertices)) if i not in locked]
    if free:
        group.add(free, 1.0, "REPLACE")
    if locked:
        group.add(sorted(locked), 0.0, "REPLACE")
    return group, len(locked)


def decimate(obj, target):
    count = triangles(obj)
    if not target or count <= target:
        log(f"{count} triangles, budget {target or 'none'}: kept")
        return count, count, 0
    source = obj.copy()
    source.data = obj.data.copy()
    bpy.context.scene.collection.objects.link(source)
    group, locked = lock_seams(obj)
    modifier = obj.modifiers.new("StaticDecimate", "DECIMATE")
    modifier.decimate_type = "COLLAPSE"
    modifier.ratio = target / count
    modifier.use_collapse_triangulate = True
    group_name = group.name
    modifier.vertex_group = group_name
    modifier.vertex_group_factor = 10.0
    select_only([obj])
    bpy.ops.object.modifier_apply(modifier=modifier.name)
    # Same shading as before: normals from the undecimated copy.
    transfer = obj.modifiers.new("StaticNormals", "DATA_TRANSFER")
    transfer.object = source
    transfer.use_loop_data = True
    transfer.data_types_loops = {"CUSTOM_NORMAL"}
    transfer.loop_mapping = "POLYINTERP_NEAREST"
    bpy.ops.object.modifier_apply(modifier=transfer.name)
    # Applying modifiers invalidates Python references to the group: look it up again.
    obj.vertex_groups.remove(obj.vertex_groups[group_name])
    bpy.data.meshes.remove(source.data, do_unlink=True)
    after = triangles(obj)
    log(f"decimated {count} -> {after} triangles ({locked} seam/border vertices locked)")
    return count, after, locked


# ----------------------------------------------------------------------------
def base_colour_nodes():
    found = []
    for material in bpy.data.materials:
        if material.node_tree is None:
            continue
        for node in material.node_tree.nodes:
            if node.type != "BSDF_PRINCIPLED":
                continue
            socket = node.inputs.get("Base Color")
            if socket is None or not socket.is_linked:
                continue
            source = socket.links[0].from_node
            for _ in range(3):
                if source.type == "TEX_IMAGE":
                    break
                linked = [i for i in source.inputs if i.is_linked]
                if not linked:
                    source = None
                    break
                source = linked[0].links[0].from_node
            if source is not None and source.type == "TEX_IMAGE" and source.image is not None:
                # Workbench "Texture" colour shows the active image node.
                material.node_tree.nodes.active = source
                found.append(source)
    return found


def srgb_to_linear(c):
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(c):
    c = np.clip(c, 0.0, 1.0)
    return np.where(c <= 0.0031308, c * 12.92, 1.055 * np.power(c, 1 / 2.4) - 0.055)


def image_array(image):
    width, height = image.size
    data = np.empty(width * height * image.channels, dtype=np.float32)
    image.pixels.foreach_get(data)
    return data.reshape(height, width, image.channels)


def load_raw(path):
    image = bpy.data.images.load(path, check_existing=False)
    image.colorspace_settings.name = "Non-Color"
    array = image_array(image)
    bpy.data.images.remove(image)
    return array


def picture_mean(path):
    """Linear mean colour of the picture's subject (flat chroma background removed)."""
    rgba = load_raw(path)
    rgb = rgba[:, :, :3]
    corners = np.array([rgb[2, 2], rgb[2, -3], rgb[-3, 2], rgb[-3, -3]])
    key = np.median(corners, axis=0)
    mask = np.abs(rgb - key).max(axis=2) > 0.22
    if rgba.shape[2] == 4:
        mask &= rgba[:, :, 3] > 0.5
    # Key spill: pixels of the key's own hue (strong chroma) left on the rim.
    key_hue = key - key.min()
    if np.linalg.norm(key_hue) > 0.5:
        hue = rgb - rgb.min(axis=2, keepdims=True)
        chroma = np.linalg.norm(hue, axis=2)
        similar = (hue @ key_hue) / np.maximum(chroma * np.linalg.norm(key_hue), 1e-6)
        mask &= ~((similar > 0.95) & (chroma > 0.35))
    for _ in range(3):  # erode: drop the anti-aliased rim
        mask = mask & np.roll(mask, 1, 0) & np.roll(mask, -1, 0) & np.roll(mask, 1, 1) & np.roll(mask, -1, 1)
    pixels = srgb_to_linear(rgb[mask])
    return pixels.mean(axis=0), int(mask.sum())


def camera_for(direction_gltf, points, resolution, ortho=True):
    scene = bpy.context.scene
    lo, hi = bounds(points)
    centre = to_blender((lo + hi) / 2)
    radius = float(np.linalg.norm(hi - lo)) / 2
    data = bpy.data.cameras.new("StaticCamera")
    camera = bpy.data.objects.new("StaticCamera", data)
    scene.collection.objects.link(camera)
    scene.camera = camera
    direction = to_blender(direction_gltf).normalized()
    if ortho:
        data.type = "ORTHO"
        data.ortho_scale = radius * 2.1
    else:
        data.lens = 85
    camera.location = centre + direction * radius * 8
    camera.rotation_euler = (centre - camera.location).to_track_quat("-Z", "Y").to_euler()
    data.clip_end = radius * 40
    scene.render.resolution_x = resolution
    scene.render.resolution_y = resolution
    return camera


def unlit_mean(obj, direction_gltf):
    """Linear mean base colour of the visible surface, unlit, from one direction."""
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_WORKBENCH"
    scene.display.shading.light = "FLAT"
    scene.display.shading.color_type = "TEXTURE"
    scene.display.shading.show_shadows = False
    scene.display.shading.show_cavity = False
    scene.view_settings.view_transform = "Standard"
    scene.render.film_transparent = True
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    camera = camera_for(direction_gltf, gltf_points(obj), 512)
    folder = tempfile.mkdtemp(prefix="static-unlit-")
    path = os.path.join(folder, "unlit.png")
    scene.render.filepath = path
    bpy.ops.render.render(write_still=True)
    rgba = load_raw(path)
    shutil.rmtree(folder, ignore_errors=True)
    bpy.data.objects.remove(camera, do_unlink=True)
    covered = rgba[:, :, 3] > 0.99
    return srgb_to_linear(rgba[:, :, :3][covered]).mean(axis=0)


LUMA = np.array([0.2126, 0.7152, 0.0722])


def colour_gains(spec, rendered, target):
    """Brightness first, hue second: the luminance moves "strength" of the
    way (log space) toward the picture, clamped to [minGain, maxGain]; each
    channel's tint relative to that moves the same share, clamped to
    1 +- maxTint. A channel never passes its target nor moves away from it."""
    strength = float(spec.get("strength", 0.6))
    low = float(spec.get("minGain", 1.0))
    high = float(spec.get("maxGain", 1.5))
    tint_max = float(spec.get("maxTint", 0.12))
    rendered = np.maximum(rendered, 1e-6)
    lum_ratio = float((target * LUMA).sum() / (rendered * LUMA).sum())
    gain = float(np.clip(lum_ratio ** strength, low, high))
    relative = (target / rendered) / lum_ratio
    tint = np.clip(np.exp(strength * np.log(np.maximum(relative, 1e-6))), 1 - tint_max, 1 + tint_max)
    tint = tint / float((rendered * tint * LUMA).sum() / (rendered * LUMA).sum())  # tint keeps luminance
    gains = gain * tint
    ratio = target / rendered
    return np.clip(gains, np.minimum(ratio, 1.0), np.maximum(ratio, 1.0))


def roll_off(linear, gains, knee=0.8):
    """Scale each channel by its gain; a channel whose gain is above 1 maps
    [knee, gain] onto [knee, 1] with slope 1 at the knee, so nothing clips
    and a gain of 1 or less leaves the curve linear."""
    out = linear * gains
    for channel, gain in enumerate(gains):
        if gain <= 1.0:
            continue
        values = out[..., channel]
        over = values > knee
        span = (gain - knee) / (1.0 - knee)
        u = (values[over] - knee) / (1.0 - knee)
        values[over] = knee + (1.0 - knee) * u / (1.0 + u * (span - 1.0) / span)
    return out


def apply_gains(nodes, gains):
    folder = tempfile.mkdtemp(prefix="static-colour-")
    done = {}
    for node in nodes:
        source = node.image
        if source.name in done:
            node.image = done[source.name]
            continue
        width, height = source.size
        pixels = image_array(source)  # image colour space as stored (sRGB bytes -> 0..1)
        linear = roll_off(srgb_to_linear(pixels[:, :, :3].astype(np.float64)), np.asarray(gains, dtype=np.float64))
        pixels[:, :, :3] = linear_to_srgb(linear)
        image = bpy.data.images.new(source.name + "_colour", width, height, alpha=source.channels == 4)
        image.colorspace_settings.name = source.colorspace_settings.name
        image.pixels.foreach_set(pixels.astype(np.float32).ravel())
        # Lossless here: the packager encodes WebP once per tier.
        path = os.path.join(folder, image.name + ".png")
        image.filepath_raw = path
        image.file_format = "PNG"
        image.save()
        image.reload()
        image.pack()
        node.image = image
        done[source.name] = image
    return folder


def recolour(obj, spec, reference, view_gltf, report):
    colour = spec.get("colour")
    if not colour:
        return None
    nodes = base_colour_nodes()
    if not nodes:
        report["warnings"].append("no base colour texture; colour step skipped")
        return None
    entry = {}
    if "gain" in colour:
        gains = np.array(colour["gain"], dtype=float)
    else:
        if not reference or not os.path.exists(reference):
            report["warnings"].append("colour.match without a reference picture; colour step skipped")
            return None
        target, count = picture_mean(reference)
        before = unlit_mean(obj, view_gltf)
        gains = colour_gains(colour, before, target)
        entry.update(target=target.round(4).tolist(), before=before.round(4).tolist(), picturePixels=count)
    folder = apply_gains(nodes, gains)
    if "before" in entry:
        after = unlit_mean(obj, view_gltf)
        entry["after"] = after.round(4).tolist()
        lum = lambda c: float((np.array(c) * LUMA).sum())
        entry["luminance"] = {"target": round(lum(entry["target"]), 4), "before": round(lum(entry["before"]), 4), "after": round(lum(after), 4)}
    entry["gains"] = gains.round(4).tolist()
    log("colour gains", entry["gains"], "luminance", entry.get("luminance"))
    report["colour"] = entry
    return folder


def mr_image_node(socket):
    """(image node, channel) feeding a Principled input through Separate Color, or (None, None)."""
    if not socket.is_linked:
        return None, None
    link = socket.links[0]
    node, channel = link.from_node, {"Red": 0, "Green": 1, "Blue": 2}.get(link.from_socket.name)
    for _ in range(3):
        if node.type == "TEX_IMAGE":
            return node, channel
        linked = [i for i in node.inputs if i.is_linked]
        if not linked:
            return None, None
        node = linked[0].links[0].from_node
    return (node, channel) if node.type == "TEX_IMAGE" else (None, None)


def matte(spec, report, folder):
    """"material": {"metallic": scale, "roughnessMin": floor} on the metallic-
    roughness texture (written new; the source image is not modified). Tripo
    marks painted gold and bronze as metal, which PBR lighting turns brown;
    the art direction is matte painted vinyl (TK 23.1)."""
    settings = spec.get("material")
    if not settings:
        return
    scale = float(settings.get("metallic", 1.0))
    floor = float(settings.get("roughnessMin", 0.0))
    done = {}
    entry = {}
    for material in bpy.data.materials:
        if material.node_tree is None:
            continue
        bsdf = next((n for n in material.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None)
        if bsdf is None:
            continue
        metal, rough = bsdf.inputs["Metallic"], bsdf.inputs["Roughness"]
        metal_node, metal_channel = mr_image_node(metal)
        rough_node, rough_channel = mr_image_node(rough)
        if metal_node is None:
            metal.default_value *= scale
        if rough_node is None:
            rough.default_value = max(rough.default_value, floor)
        node = metal_node or rough_node
        if node is None:
            continue
        source = node.image
        if source.name not in done:
            pixels = image_array(source)
            if metal_node == node:
                entry["metallicBefore"] = round(float(pixels[:, :, metal_channel].mean()), 3)
                pixels[:, :, metal_channel] *= scale
                entry["metallicAfter"] = round(float(pixels[:, :, metal_channel].mean()), 3)
            if rough_node == node:
                entry["roughnessBefore"] = round(float(pixels[:, :, rough_channel].mean()), 3)
                pixels[:, :, rough_channel] = np.maximum(pixels[:, :, rough_channel], floor)
                entry["roughnessAfter"] = round(float(pixels[:, :, rough_channel].mean()), 3)
            width, height = source.size
            image = bpy.data.images.new(source.name + "_matte", width, height, alpha=source.channels == 4)
            image.colorspace_settings.name = source.colorspace_settings.name
            image.pixels.foreach_set(pixels.astype(np.float32).ravel())
            image.filepath_raw = os.path.join(folder, image.name + ".png")
            image.file_format = "PNG"
            image.save()
            image.reload()
            image.pack()
            done[source.name] = image
        for other in (metal_node, rough_node):
            if other is not None and other.image == source:
                other.image = done[source.name]
    report["material"] = entry
    log("material", entry)


# ----------------------------------------------------------------------------
def socket_point(name, value, tree, points, made):
    lo, hi = bounds(points)
    centre = (lo + hi) / 2
    half = (hi - lo) / 2
    if isinstance(value, list):
        value = {"at": value}
    offset = np.array(value.get("offset", [0, 0, 0]), dtype=float)
    if "at" in value:
        return np.array(value["at"], dtype=float) + offset
    if "frac" in value:
        return centre + np.array(value["frac"], dtype=float) * half + offset
    if "from" in value:
        if value["from"] not in made:
            raise SystemExit(f"{name}: socket {value['from']} must come first")
        return made[value["from"]] + offset
    if "ray" in value:
        axis_name = value["ray"]
        sign = -1.0 if axis_name[0] == "-" else 1.0
        axis = AXES[axis_name[1]]
        start = np.zeros(3)
        for other in range(3):
            if other == axis:
                continue
            letter = "xyz"[other]
            if letter in value:
                start[other] = float(value[letter])
            elif "f" + letter in value:
                start[other] = centre[other] + float(value["f" + letter]) * half[other]
            else:
                start[other] = centre[other]
        start[axis] = (lo[axis] - 1.0) if sign > 0 else (hi[axis] + 1.0)
        if "start" in value:  # begin inside the model (a floor under a roof)
            start[axis] = float(value["start"])
        direction = np.zeros(3)
        direction[axis] = sign
        hit, _normal, _index, _distance = tree.ray_cast(to_blender(start), to_blender(direction))
        if hit is None:
            raise SystemExit(f"{name}: ray {axis_name} from {start.round(3).tolist()} hits nothing")
        return np.array(to_gltf(hit)) + offset
    raise SystemExit(f"{name}: socket needs at, frac, from or ray")


def make_sockets(obj, spec, report):
    sockets = spec.get("sockets") or {}
    if not sockets:
        return {}
    depsgraph = bpy.context.evaluated_depsgraph_get()
    tree = BVHTree.FromObject(obj, depsgraph)
    points = gltf_points(obj)
    made = {}
    for name, value in sockets.items():
        if not name.startswith("FX_"):
            raise SystemExit(f"socket {name}: names start with FX_")
        point = socket_point(name, value, tree, points, made)
        made[name] = point
        empty = bpy.data.objects.new(name, None)
        bpy.context.scene.collection.objects.link(empty)
        empty.empty_display_type = "SPHERE"
        empty.empty_display_size = 0.05
        empty.location = to_blender(point)
        bpy.context.view_layer.update()
        matrix = empty.matrix_world.copy()
        empty.parent = obj
        empty.matrix_world = matrix
    report["sockets"] = {name: [round(float(v), 3) for v in point] for name, point in made.items()}
    log("sockets", ", ".join(made))
    return made


# ----------------------------------------------------------------------------
def export(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    bpy.ops.export_scene.gltf(
        filepath=path, export_format="GLB", export_yup=True, export_apply=True,
        export_texcoords=True, export_normals=True, export_materials="EXPORT",
        export_animations=False, export_skins=False, export_morph=False,
        export_image_format="AUTO", use_selection=False)
    log("exported", path)


def preview_setup(background):
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_WORKBENCH"
    scene.display.shading.light = "STUDIO"
    scene.display.shading.color_type = "TEXTURE"
    scene.display.shading.show_shadows = True
    scene.display.shading.shadow_intensity = 0.45
    scene.display.light_direction = (0.45, -0.35, 0.82)
    scene.display.shading.show_cavity = False
    scene.view_settings.view_transform = "Standard"
    scene.render.film_transparent = False
    scene.display.shading.background_type = "VIEWPORT"
    scene.display.shading.background_color = background
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGB"


def flat_material(name, rgba):
    """Plain colour for preview helpers, in Workbench and EEVEE alike."""
    material = bpy.data.materials.new(name)
    material.diffuse_color = rgba
    bsdf = next((n for n in material.node_tree.nodes if n.type == "BSDF_PRINCIPLED"), None) if material.node_tree else None
    if bsdf is not None:
        bsdf.inputs["Base Color"].default_value = rgba
        bsdf.inputs["Roughness"].default_value = 0.9
    return material


def lit_setup():
    """EEVEE with a sun and a grey sky: PBR as a glTF viewer shows it, so a
    metallic map that darkens painted gold is visible before the matte step."""
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE"
    scene.eevee.taa_render_samples = 16
    scene.view_settings.view_transform = "Standard"
    scene.render.film_transparent = False
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGB"
    world = bpy.data.worlds.get("PreviewWorld") or bpy.data.worlds.new("PreviewWorld")
    if world.node_tree is None:
        world.use_nodes = True
    background = next((n for n in world.node_tree.nodes if n.type == "BACKGROUND"), None)
    background.inputs["Color"].default_value = (0.55, 0.57, 0.6, 1)
    background.inputs["Strength"].default_value = 1.0
    scene.world = world
    data = bpy.data.lights.new("PreviewSun", "SUN")
    data.energy = 2.5
    data.angle = math.radians(8)
    sun = bpy.data.objects.new("PreviewSun", data)
    scene.collection.objects.link(sun)
    # From the front right, above (glTF (0.5, 1, -0.7) -> Blender).
    sun.rotation_euler = to_blender((0.5, 1.0, -0.7)).normalized().to_track_quat("Z", "Y").to_euler()
    return sun


def ground(points):
    lo, hi = bounds(points)
    extent = float(max(hi[0] - lo[0], hi[2] - lo[2])) * 1.6 + 0.2
    # Under the model, not at the pivot: a projectile or a held item is pivoted at its centre or grip.
    bpy.ops.mesh.primitive_plane_add(size=extent, location=(float((lo[0] + hi[0]) / 2), float(-(lo[2] + hi[2]) / 2), float(min(lo[1], 0.0)) - 0.001))
    plane = bpy.context.active_object
    plane.name = "PreviewGround"
    plane.data.materials.append(flat_material("PreviewGround", (0.42, 0.44, 0.40, 1)))
    plane.color = (0.42, 0.44, 0.40, 1)
    return plane


def markers(made, size):
    objects = []
    for name, point in made.items():
        bpy.ops.mesh.primitive_uv_sphere_add(radius=size, location=to_blender(point), segments=12, ring_count=6)
        sphere = bpy.context.active_object
        sphere.name = "PreviewMarker_" + name
        sphere.data.materials.append(flat_material("PreviewMarker", (1.0, 0.1, 0.8, 1)))
        objects.append(sphere)
    return objects


def ring(radius):
    bpy.ops.mesh.primitive_torus_add(major_radius=radius, minor_radius=max(radius * 0.012, 0.02), location=(0, 0, 0.02))
    torus = bpy.context.active_object
    torus.name = "PreviewRing"
    torus.data.materials.append(flat_material("PreviewRing", (0.1, 0.9, 1.0, 1)))
    return torus


def render(path, direction_gltf, points, resolution=640):
    camera = camera_for(direction_gltf, points, resolution)
    bpy.context.scene.render.filepath = path
    bpy.ops.render.render(write_still=True)
    bpy.data.objects.remove(camera, do_unlink=True)


THREE_QUARTER = (0.5, 0.55, -0.85)  # front (-Z), the model's right (+X), from above


def preview(folder, name, obj, made, spec, stage):
    os.makedirs(folder, exist_ok=True)
    safe = name.replace("/", "__")
    base_colour_nodes()  # make the base colour the node Workbench shows
    points = gltf_points(obj)
    extras = [ground(points)]
    lo, hi = bounds(points)
    if stage == "after":
        extras += markers(made, float(max(hi - lo)) * 0.012 + 0.005)
        if spec.get("ring"):
            extras.append(ring(float(spec["ring"])))
    sun = lit_setup()
    render(os.path.join(folder, f"{safe}__{stage}.png"), THREE_QUARTER, points)
    bpy.data.objects.remove(sun, do_unlink=True)
    preview_setup((0.30, 0.31, 0.34))
    if stage == "after":
        render(os.path.join(folder, f"{safe}__top.png"), (0.0, 1.0, -0.0001), points)
        render(os.path.join(folder, f"{safe}__front.png"), (0.0, 0.0, -1.0), points)
    # Unlit base colour from the same 3/4 view: what the colour step compares with the picture.
    shading = bpy.context.scene.display.shading
    shading.light, shading.show_shadows = "FLAT", False
    render(os.path.join(folder, f"{safe}__{stage}_unlit.png"), THREE_QUARTER, points)
    for extra in extras:
        bpy.data.objects.remove(extra, do_unlink=True)


def check(report, spec, points):
    lo, hi = bounds(points)
    size = hi - lo
    values = {"height": float(size[1]), "width": float(size[0]), "depth": float(size[2]), "length": float(size[2])}
    report["size"] = [round(float(v), 3) for v in size]
    # The ring only means something for a building (a footprint size or check).
    if (spec.get("size") or {}).get("measure") == "footprint" or "footprint" in (spec.get("expect") or {}):
        values["footprint"] = footprint(points, spec.get("ringExclude"))
        report["footprint"] = round(values["footprint"], 3)
    results = {}
    for key, window in (spec.get("expect") or {}).items():
        value = values[key]
        low, high = float(window[0]), float(window[1])
        if value < low:
            off = (value - low) / low
        elif value > high:
            off = (value - high) / high
        else:
            off = 0.0
        status = "ok" if off == 0 else ("near" if abs(off) <= 0.2 else "off")
        results[key] = {"value": round(value, 3), "expected": [low, high], "deviation": round(off, 3), "status": status}
        if status == "off":
            report["warnings"].append(f"{key} {value:.2f} m is {off * 100:+.0f}% outside {low}-{high} m")
    report["expect"] = results


def main():
    args, spec = parse()
    report = {"id": args.id, "input": args.input, "output": args.output, "warnings": []}
    obj = import_input(args.input)
    report["trianglesSource"] = triangles(obj)
    rotation, scale = place(obj, spec)
    report["scale"] = round(scale, 5)
    report["yaw"] = spec.get("yaw", 0)
    obj.name = args.id.split("/")[-1] + "_mesh"
    if args.preview:
        preview(args.preview, args.id, obj, {}, spec, "before")
    _before, after, locked = decimate(obj, int(spec.get("triangles") or 0))
    report["triangles"] = after
    report["seamVerticesLocked"] = locked
    # The picture's view: Tripo's +X, raised 25 degrees, through the same turn.
    view = rotation @ Vector((1.0, math.tan(math.radians(25)), 0.0))
    folder = recolour(obj, spec, args.reference, (view.x, view.y, view.z), report) or tempfile.mkdtemp(prefix="static-colour-")
    matte(spec, report, folder)
    made = make_sockets(obj, spec, report)
    check(report, spec, gltf_points(obj))
    export(args.output)
    if folder:
        shutil.rmtree(folder, ignore_errors=True)
    if args.preview:
        preview(args.preview, args.id, obj, made, spec, "after")
    if args.report:
        os.makedirs(os.path.dirname(args.report), exist_ok=True)
        with open(args.report, "w", encoding="utf-8") as handle:
            json.dump(report, handle, indent=1)
    log("done", args.id, json.dumps({k: report[k] for k in ("triangles", "size", "warnings")}))


if __name__ == "__main__":
    main()
