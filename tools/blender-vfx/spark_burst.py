"""Blender -b --factory-startup -P tools/blender-vfx/spark_burst.py -- <out>"""
# Tham số chỉnh cho lô sau; cùng seed cho cùng hình học và chuyển động.
SEED = 71101
FRAMES = 16
PARTICLES = 42
DUST = 22
REFERENCE = '.local/video-review/sheets/beast-hit-spark-burst__take1.jpg'

import math
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import *

scene, out = setup('spark', FRAMES, SEED)
glow(scene)
rng = random.Random(SEED)
mats = []
for i in range(5):
    c = (0.35, 0.85, 0.66) if i % 2 else (1.0, 0.94, 0.78)
    mats.append(emission(f'IvoryJade-{i}', c, 1.15 if i % 2 else 1.75)[0])

particles = []
for i in range(PARTICLES + DUST):
    # Phân bố không đều theo hướng đòn, tránh vòng pháo hoa đồng tâm.
    angle = rng.uniform(0, math.tau)
    direction = Vector((math.cos(angle), math.sin(angle) * .72, rng.uniform(-.35, .8))).normalized()
    speed = rng.uniform(3.0, 7.4) * (1 if i < PARTICLES else .65)
    life = rng.uniform(.17, .42) if i < PARTICLES else rng.uniform(.24, .49)
    delay = rng.uniform(0, .025) if i < PARTICLES else rng.uniform(.045, .11)
    width = rng.uniform(.009, .017) if i < PARTICLES else rng.uniform(.003, .007)
    mesh = bpy.data.meshes.new(f'streak-{i}')
    obj = bpy.data.objects.new(f'streak-{i}', mesh)
    scene.collection.objects.link(obj)
    for mat in mats: mesh.materials.append(mat)
    particles.append((obj, direction, speed, life, delay, width, i < PARTICLES))

flashmat, flashnode = emission('Short ivory hit core', (1, .96, .82), 9)
bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=12, radius=1)
flash = bpy.context.object
flash.data.materials.append(flashmat)

def path(d, speed, t):
    return d * speed * .15 * (1 - math.exp(-t / .115)) + Vector((0, 0, -.9 * t * t))

def update(t):
    size = .12 * math.exp(-t * 37) if t < .13 else 0
    flash.scale = (size * 1.8, size, size * .65)
    flashnode.inputs['Strength'].default_value = 9 * math.exp(-t * 24)
    for obj, d, speed, life, delay, width, streak in particles:
        age = t - delay
        obj.hide_render = age < 0 or age >= life
        if obj.hide_render: continue
        fade = (1 - age / life) ** .8
        n = 7
        verts, faces = [], []
        a = d.cross(Vector((0, 0, 1))).normalized()
        b = d.cross(a).normalized()
        shutter = min(age + .008, .042 if streak else .009)
        for k in range(n):
            u = k / (n - 1)
            p = path(d, speed, max(0, age - shutter * (1 - u)))
            rad = width * fade * (.06 + .94 * math.sin(u * math.pi * .8))
            for j in range(6):
                v = p + rad * (a * math.cos(j * math.tau / 6) + b * math.sin(j * math.tau / 6))
                verts.append(v)
        for k in range(n - 1):
            for j in range(6): faces.append((k * 6 + j, k * 6 + (j + 1) % 6, (k + 1) * 6 + (j + 1) % 6, (k + 1) * 6 + j))
        obj.data.clear_geometry()
        obj.data.from_pydata(verts, [], faces)
        for poly in obj.data.polygons: poly.material_index = min(4, poly.index // 6)
        obj.data.update()

render(scene, out, update, {'seed': SEED, 'reference': REFERENCE, 'particles': PARTICLES, 'dust': DUST},
       f'Reference: {REFERENCE}\nBlender material study, high-end donghua impact: one compact ivory and pale jade flash, short tapered emissive particle motion trails, varied speeds and immediate cooling, finer secondary luminous dust. One sharp attack followed by complete decay within 0.667 seconds. Orthographic camera at 55 degrees, wide clear margins, transparent RGBA. Seed {SEED}. Script: tools/blender-vfx/spark_burst.py; all parameters and trajectories recorded in source.')
