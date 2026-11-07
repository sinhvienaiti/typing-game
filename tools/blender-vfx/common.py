"""Tiện ích render mẫu vật liệu; chỉ ghi vào thư mục đầu ra được chỉ định."""
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
for key in ('TMPDIR', 'BLENDER_USER_CONFIG', 'BLENDER_USER_SCRIPTS',
            'BLENDER_USER_DATAFILES', 'BLENDER_USER_RESOURCES'):
    folder = ROOT / '.local/blender-home' / key.lower()
    folder.mkdir(parents=True, exist_ok=True)
    os.environ[key] = str(folder)
import bpy
from mathutils import Vector


def setup(name, frames, seed, samples=24):
    out = Path(sys.argv[sys.argv.index('--') + 1]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    (out / 'rgba').mkdir(exist_ok=True)
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    scene = bpy.context.scene
    scene.render.engine = os.environ.get('VFX_ENGINE', 'BLENDER_EEVEE')
    if scene.render.engine == 'BLENDER_EEVEE':
        scene.eevee.taa_render_samples = 32
        scene.eevee.volumetric_tile_size = '2'
        scene.eevee.volumetric_samples = 64
        scene.eevee.use_volume_custom_range = True
        scene.eevee.volumetric_start = 3
        scene.eevee.volumetric_end = 11
        scene.eevee.use_volumetric_shadows = True
    if scene.render.engine == 'CYCLES':
        scene.cycles.device = 'CPU'
        scene.cycles.samples = int(os.environ.get('VFX_SAMPLES', str(samples)))
        scene.cycles.seed = seed
        scene.cycles.use_denoising = True
    scene.render.resolution_x = int(os.environ.get('VFX_SIZE', '512'))
    scene.render.resolution_y = scene.render.resolution_x
    scene.render.resolution_percentage = 100
    scene.render.fps = 24
    scene.frame_start, scene.frame_end = 1, frames
    scene.render.film_transparent = True
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'
    scene.render.image_settings.color_depth = '8'
    scene.render.threads_mode = 'FIXED'
    scene.render.threads = 6
    scene.view_settings.view_transform = 'Standard'
    scene.view_settings.look = 'None'
    scene.world.color = (0, 0, 0)
    bpy.ops.object.camera_add(location=(0, -7 * math.cos(math.radians(55)), 7 * math.sin(math.radians(55))))
    cam = bpy.context.object
    cam.rotation_euler = (-cam.location).to_track_quat('-Z', 'Y').to_euler()
    cam.data.type = 'ORTHO'
    cam.data.ortho_scale = 5.6
    scene.camera = cam
    return scene, out


def emission(name, color, strength):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nt = mat.node_tree
    nt.nodes.clear()
    e = nt.nodes.new('ShaderNodeEmission')
    e.inputs['Color'].default_value = (*color, 1)
    e.inputs['Strength'].default_value = strength
    o = nt.nodes.new('ShaderNodeOutputMaterial')
    nt.links.new(e.outputs[0], o.inputs['Surface'])
    return mat, e


def glow(scene):
    # Alpha du quầng được suy ra từ chính quầng, giữ nguyên alpha vật liệu gốc.
    nt = bpy.data.node_groups.new('VFX compositor', 'CompositorNodeTree')
    scene.compositing_node_group = nt
    nt.interface.new_socket(name='Image', in_out='OUTPUT', socket_type='NodeSocketColor')
    r = nt.nodes.new('CompositorNodeRLayers')
    g = nt.nodes.new('CompositorNodeGlare')
    g.inputs['Type'].default_value = 'Fog Glow'
    g.inputs['Quality'].default_value = 'High'
    g.inputs['Threshold'].default_value = 1.2
    g.inputs['Size'].default_value = .18
    nt.links.new(r.outputs['Image'], g.inputs['Image'])
    bw = nt.nodes.new('CompositorNodeRGBToBW')
    nt.links.new(g.outputs['Image'], bw.inputs[0])
    mx = nt.nodes.new('ShaderNodeMath')
    mx.operation = 'MAXIMUM'
    nt.links.new(r.outputs['Alpha'], mx.inputs[0])
    nt.links.new(bw.outputs[0], mx.inputs[1])
    a = nt.nodes.new('CompositorNodeSetAlpha')
    a.inputs['Type'].default_value = 'Replace Alpha'
    nt.links.new(g.outputs['Image'], a.inputs['Image'])
    nt.links.new(mx.outputs[0], a.inputs['Alpha'])
    c = nt.nodes.new('NodeGroupOutput')
    nt.links.new(a.outputs[0], c.inputs[0])


def render(scene, out, update, params, prompt):
    (out / 'sample.prompt.txt').write_text(prompt + '\n', encoding='utf-8')
    sources = (Path(__file__), Path(sys.argv[sys.argv.index('-P')+1]))
    source_sha = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    for p in sources:
        (out / p.name).write_bytes(p.read_bytes())
    started = time.monotonic()
    test = os.environ.get('VFX_TEST_FRAMES')
    frames = [int(f) for f in test.split(',')] if test else range(1, scene.frame_end + 1)
    times = []
    for frame in frames:
        scene.frame_set(frame)
        update((frame - 1) / scene.render.fps)
        scene.render.filepath = str(out / 'rgba' / f'{frame:04d}.png')
        tick = time.monotonic()
        bpy.ops.render.render(write_still=True)
        times.append({'frame': frame, 'seconds': round(time.monotonic() - tick, 3)})
        print(f'VFX_FRAME {frame} {times[-1]["seconds"]}s', flush=True)
    data = dict(params, engine=scene.render.engine, blender=bpy.app.version_string,
                camera_elevation=55, resolution=[scene.render.resolution_x, scene.render.resolution_y], fps=24,
                frames=scene.frame_end, duration=scene.frame_end / 24,
                render_seconds=round(time.monotonic() - started, 3), frame_times=times)
    data['source_sha256'] = source_sha
    (out / ('probe.json' if test else 'render.json')).write_text(json.dumps(data, indent=2), encoding='utf-8')


def area(name, loc, power, color, size):
    bpy.ops.object.light_add(type='AREA', location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler = (-obj.location).to_track_quat('-Z', 'Y').to_euler()
    obj.data.energy = power
    obj.data.color = color
    obj.data.shape = 'DISK'
    obj.data.size = size
