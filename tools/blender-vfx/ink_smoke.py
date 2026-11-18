"""Khối nhiễu động giới hạn: nhanh hơn bake Mantaflow cho mẫu 1,5 giây."""
SEED = 71102
FRAMES = 36
LOBE_COUNT = 11
DENSITY = 48.0
REFERENCE = '.local/video-review/sheets/beast-death-ink-smoke__take1.jpg'

import math
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import *

scene, out = setup('ink', FRAMES, SEED, samples=16)
area('Pale jade back rim', (1.4, 2.0, 3), 2200, (.7, .9, .84), 1.3)
area('Ivory side rim', (-3, 1, 1.5), 1700, (1, .94, .8), 1.2)
rng = random.Random(SEED)
clouds = []
for i in range(LOBE_COUNT):
    bpy.ops.mesh.primitive_cube_add(size=2)
    obj = bpy.context.object
    obj.name = f'Turbulent ink volume {i}'
    mat = bpy.data.materials.new(f'Porous ink {i}')
    mat.use_nodes = True
    nt = mat.node_tree
    nt.nodes.clear()
    def node(kind): return nt.nodes.new(kind)
    def link(a, b): nt.links.new(a, b)
    def mathnode(op, a, b):
        n = node('ShaderNodeMath'); n.operation = op
        for ix, v in enumerate((a, b)):
            if isinstance(v, (int, float)): n.inputs[ix].default_value = v
            else: link(v, n.inputs[ix])
        return n.outputs[0]
    coord = node('ShaderNodeTexCoord')
    sub = node('ShaderNodeVectorMath'); sub.operation = 'SUBTRACT'
    link(coord.outputs['Generated'], sub.inputs[0]); sub.inputs[1].default_value = (.5, .5, .5)
    dist = node('ShaderNodeVectorMath'); dist.operation = 'LENGTH'; link(sub.outputs[0], dist.inputs[0])
    noise = node('ShaderNodeTexNoise'); noise.noise_dimensions = '4D'
    noise.inputs['Scale'].default_value = 4.3
    noise.inputs['Detail'].default_value = 5
    noise.inputs['Roughness'].default_value = .7
    link(coord.outputs['Generated'], noise.inputs['Vector'])
    # Biên mềm giữ khối trong khung; nhiễu khoét dần khối thay vì chỉ hạ alpha.
    radius_noise = mathnode('MULTIPLY', noise.outputs['Fac'], .55)
    radius_noise = mathnode('ADD', radius_noise, .14)
    envelope = mathnode('SUBTRACT', radius_noise, dist.outputs['Value'])
    envelope = mathnode('MULTIPLY', envelope, 16)
    envelope = mathnode('MAXIMUM', envelope, 0)
    envelope = mathnode('MINIMUM', envelope, 1)
    threshold = node('ShaderNodeValue')
    porous = mathnode('SUBTRACT', noise.outputs['Fac'], threshold.outputs[0])
    porous = mathnode('MAXIMUM', porous, 0)
    den = mathnode('MULTIPLY', porous, envelope)
    gain = node('ShaderNodeValue')
    den = mathnode('MULTIPLY', den, gain.outputs[0])
    volume = node('ShaderNodeVolumePrincipled')
    volume.inputs['Color'].default_value = (.018, .022, .025, 1)
    volume.inputs['Anisotropy'].default_value = .35
    link(den, volume.inputs['Density'])
    output = node('ShaderNodeOutputMaterial'); link(volume.outputs[0], output.inputs['Volume'])
    obj.data.materials.append(mat)
    angle = i * math.tau / LOBE_COUNT + rng.uniform(-.3, .3)
    direction = Vector((math.cos(angle), math.sin(angle) * .64, rng.uniform(-.25, .55)))
    clouds.append((obj, noise, threshold, gain, direction, rng.uniform(.52, .85), rng.uniform(0, 20)))

def update(t):
    end = (FRAMES - 1) / 24
    for obj, noise, threshold, gain, direction, radius, phase in clouds:
        expansion = 1 - math.exp(-t * 16)
        obj.location = direction * expansion * .78 + Vector((0, 0, .13 * t))
        size = radius * (.23 + .77 * expansion)
        obj.scale = (size * (1 + .10*t), size * .84, size * (1.05 + .22*t))
        obj.rotation_euler = (.08*t*math.sin(phase), .12*t*math.cos(phase), .18*t*math.sin(phase*.4))
        noise.inputs['W'].default_value = phase + t * .65
        # Tăng ngưỡng đục lỗ từ sau cú phụt; tan hết trước khung cuối.
        q = min(1, max(0, (t - .12) / (end - .2)))
        threshold.outputs[0].default_value = .38 + .20 * q ** 1.1
        gain.outputs[0].default_value = DENSITY * (1 - q) ** 2.3
        obj.hide_render = t < .001 or t >= end - .04

render(scene, out, update, {'seed': SEED, 'reference': REFERENCE, 'lobes': LOBE_COUNT,
       'method': 'bounded turbulent procedural volume; no Mantaflow bake', 'density': DENSITY},
       f'Reference: {REFERENCE}\nBlender material study: a short decisive outward puff of black ink smoke, pale jade and ivory grazing rim light, layered porous rolling turbulent volume, density erosion into fine wisps, complete disappearance within 1.5 seconds. Envelope expansion stops after the initial impulse. Orthographic camera at 55 degrees, wide clear margins, transparent RGBA. Seed {SEED}. Script: tools/blender-vfx/ink_smoke.py; bounded noisy volume chosen to keep rendering under ten minutes.')
