"""AL-13: GLB → PNG ở đúng đường dẫn cache do Node truyền vào.

Camera 3/4 cố định, Cycles CPU, ánh sáng trung tính, nền trong suốt.
Node mã hóa tiếp thành WebP; không lưu .blend, cache hay file phụ.
"""
import math
import os
import sys

import bpy
import numpy as np  # có sẵn trong Python của Blender
from mathutils import Vector


def main():
    args = sys.argv[sys.argv.index('--') + 1:]
    if len(args) != 2:
        raise ValueError('Cần đường dẫn GLB và ảnh cache')
    source, output = map(os.path.abspath, args)
    # Danh sách cấm; không import tài sản của game đang dừng.
    denied = ('immortality-cultivation', 'tu-tien', 'tu_tien', 'monkeytype')
    if any(word in source.lower() for word in denied):
        raise ValueError('Đường dẫn nguồn bị chặn')
    if os.path.basename(os.path.dirname(output)) != '.thumbs' or not output.endswith('.webp'):
        raise ValueError('Chỉ ghi ảnh vào library/.thumbs/<md5>.webp')
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.context.preferences.filepaths.save_version = 0
    bpy.context.preferences.filepaths.use_auto_save_temporary_files = False
    bpy.ops.import_scene.gltf(filepath=source, import_pack_images=True)
    scene = bpy.context.scene
    scene.frame_set(1)
    meshes = [o for o in scene.objects if o.type == 'MESH']
    if not meshes:
        raise ValueError('GLB không có mesh')
    # Đỉnh thật sau modifier (armature ở khung 1), không dùng hộp bao: hộp bao
    # chiếu góc 3/4 rộng hơn hình chiếu thật, rồng chỉ chiếm 1/3–1/2 khung.
    depsgraph = bpy.context.evaluated_depsgraph_get()
    chunks = []
    for obj in meshes:
        evaluated = obj.evaluated_get(depsgraph)
        mesh = evaluated.to_mesh()
        count = len(mesh.vertices)
        if count:
            co = np.empty(count * 3, dtype=np.float32)
            mesh.vertices.foreach_get('co', co)
            matrix = np.array(obj.matrix_world, dtype=np.float64)
            chunks.append(co.reshape(-1, 3).astype(np.float64) @ matrix[:3, :3].T + matrix[:3, 3])
        evaluated.to_mesh_clear()
    if not chunks:
        raise ValueError('GLB không có đỉnh')
    points = np.concatenate(chunks)
    low, high = points.min(axis=0), points.max(axis=0)
    center = Vector(((low + high) / 2).tolist())
    radius = float(np.linalg.norm(points - np.array(center), axis=1).max())
    if not math.isfinite(radius) or radius <= 0:
        raise ValueError('Kích thước GLB không hợp lệ')
    # Đổi trục +Y glTF được importer xử lý thành +Z Blender.
    direction = Vector((1.0, -1.0, 0.78)).normalized()
    rotation = direction.to_track_quat('Z', 'Y')
    right, up = rotation @ Vector((1, 0, 0)), rotation @ Vector((0, 1, 0))
    offset = points - np.array(center)
    xs, ys = offset @ np.array(right), offset @ np.array(up)
    width, height = float(xs.max() - xs.min()), float(ys.max() - ys.min())
    if not math.isfinite(max(width, height)) or max(width, height) <= 0:
        raise ValueError('Hình chiếu GLB rỗng')
    # Khung vừa hình chiếu thật, chừa 5% mỗi bên; camera giữ góc 3/4 cố định.
    middle = center + right * float((xs.max() + xs.min()) / 2) + up * float((ys.max() + ys.min()) / 2)
    bpy.ops.object.camera_add(location=middle + direction * radius * 4)
    camera = bpy.context.object
    camera.rotation_euler = rotation.to_euler()
    camera.data.type = 'ORTHO'
    camera.data.ortho_scale = max(width, height) * 1.1
    camera.data.clip_start = max(radius / 1000, 0.0001)
    camera.data.clip_end = radius * 20
    scene.camera = camera
    # Bỏ camera/đèn được nhúng trong GLB khỏi khung và ánh sáng xem trước.
    for obj in list(scene.objects):
        if obj.type == 'LIGHT':
            bpy.data.objects.remove(obj, do_unlink=True)
    # Phát sáng hằng (emissiveFactor không texture, như quả cầu lửa trắng 1,1,1 × 3)
    # phủ trắng màu vẽ; game tự thay shader. Ảnh xem trước bỏ nó, giữ phát sáng có texture.
    for material in bpy.data.materials:
        for node in (material.node_tree.nodes if material.node_tree else []):
            color, strength = node.inputs.get('Emission Color'), node.inputs.get('Emission Strength')
            if color is not None and strength is not None and not color.is_linked:
                strength.default_value = 0.0
    for offset, energy, size in [((2, -3, 4), 550, 4), ((-3, -1, 2), 300, 3), ((0, 3, 3), 450, 3)]:
        bpy.ops.object.light_add(type='AREA', location=center + Vector(offset) * radius)
        light = bpy.context.object
        light.data.energy = energy * radius ** 2
        light.data.shape = 'DISK'
        light.data.size = size * radius
        light.rotation_euler = (center - light.location).to_track_quat('-Z', 'Y').to_euler()
    scene.world = bpy.data.worlds.new('AL13 Neutral')
    scene.world.use_nodes = True
    scene.world.node_tree.nodes['Background'].inputs[0].default_value = (0.18, 0.18, 0.18, 1)
    scene.world.node_tree.nodes['Background'].inputs[1].default_value = 0.5
    scene.render.engine = 'CYCLES'
    scene.cycles.device = 'CPU'
    scene.cycles.samples = 16
    scene.render.threads_mode = 'FIXED'
    scene.render.threads = 4
    scene.render.resolution_x = scene.render.resolution_y = 256
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = True
    scene.render.use_file_extension = False
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'
    scene.render.image_settings.color_depth = '8'
    scene.render.image_settings.compression = 100
    scene.view_settings.view_transform = 'Standard'
    scene.render.filepath = output
    bpy.ops.render.render(write_still=True)


if __name__ == '__main__':
    main()
