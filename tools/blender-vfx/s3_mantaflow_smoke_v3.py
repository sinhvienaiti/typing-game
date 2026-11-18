"""S3-2 v3: Mantaflow nhỏ, luồng mảnh theo trục lên của camera; giữ nguyên recipe cũ."""
import json, math, os, sys, time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from s3_common import *
SEED=711036; FRAMES=48; FPS=32
REFERENCE='.local/video-review/sheets/beast-death-ink-smoke__take1.jpg'
s,out=setup(FRAMES,FPS);started=time.monotonic();s.gravity=tuple(-UP*.3)
# Le volume du domaine n'est jamais une surface visible.
bpy.ops.mesh.primitive_cube_add(size=2,location=(0,0,0));domain=bpy.context.object;domain.name='S3 gas domain';domain.scale=(2.0,2.0,2.1);bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
mod=domain.modifiers.new('S3 Mantaflow gas','FLUID');mod.fluid_type='DOMAIN';d=mod.domain_settings;d.domain_type='GAS';d.resolution_max=int(os.environ.get('VFX_FLUID_RES','96'));d.cache_frame_start=1;d.cache_frame_end=FRAMES;d.cache_type='ALL';d.cache_directory=str(out/'fluid-cache');d.cache_data_format='UNI';d.use_noise=True;d.noise_scale=2;d.vorticity=1.25;d.time_scale=1.0;d.use_dissolve_smoke=True;d.dissolve_speed=40;d.use_dissolve_smoke_log=True;d.timesteps_max=3
mat=bpy.data.materials.new('Mantaflow ink with transparent erosion');mat.use_nodes=True;n=mat.node_tree.nodes;n.clear();l=mat.node_tree.links;attr=n.new('ShaderNodeAttribute');attr.attribute_name='density';mul=n.new('ShaderNodeMath');mul.operation='MULTIPLY';l.new(attr.outputs['Fac'],mul.inputs[0]);mul.inputs[1].default_value=7
vol=n.new('ShaderNodeVolumePrincipled');vol.inputs['Color'].default_value=(.009,.014,.017,1);vol.inputs['Anisotropy'].default_value=.2;l.new(mul.outputs[0],vol.inputs['Density']);o=n.new('ShaderNodeOutputMaterial');l.new(vol.outputs[0],o.inputs['Volume']);domain.data.materials.append(mat)
for i,(x,y,vel) in enumerate([(-.48,0,tuple(screen(-.65,2.15))),(-.15,.08,tuple(screen(-.18,2.75))),(.23,-.09,tuple(screen(.45,2.4))),(.50,.02,tuple(screen(.85,1.85)))]):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=16,ring_count=8,radius=.095,location=screen(x,-1.03,y));ob=bpy.context.object;ob.scale=(.85,.85,1.5);bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    m=ob.modifiers.new('short ink inflow','FLUID');m.fluid_type='FLOW';f=m.flow_settings;f.flow_type='SMOKE';f.flow_behavior='INFLOW';f.surface_distance=1.5;f.density=1.3;f.temperature=.45;f.use_initial_velocity=True;f.velocity_coord=vel
    f.use_inflow=True;f.keyframe_insert(data_path='use_inflow',frame=1);f.keyframe_insert(data_path='use_inflow',frame=4);f.use_inflow=False;f.keyframe_insert(data_path='use_inflow',frame=5);ob.hide_render=True
for loc,power,color in [((-2,1.8,2.5),600,(1,.94,.83)),((2,1,2),850,(.7,.9,.85))]:
    bpy.ops.object.light_add(type='AREA',location=loc);ob=bpy.context.object;ob.rotation_euler=(-ob.location).to_track_quat('-Z','Y').to_euler();ob.data.energy=power;ob.data.color=color;ob.data.size=2
bpy.ops.object.effector_add(type='TURBULENCE',location=(0,0,.4));field=bpy.context.object;field.field.strength=.75;field.field.size=.35;field.field.seed=SEED
bpy.context.view_layer.objects.active=domain;domain.select_set(True)
s.frame_set(1);print('S3_BAKE_START',flush=True);bpy.ops.fluid.bake_all();bake=time.monotonic()-started;print('S3_BAKE_SECONDS',bake,flush=True)
if bake>480:
    (out/'timeout.json').write_text(json.dumps({'bake_seconds':bake,'reason':'ngừng trước ngân sách 10 phút'}));raise RuntimeError('S3 budget: bake too slow')
def update(t):
    q=min(1,max(0,(t-.6)/(.86875)));mul.inputs[1].default_value=8*(1-q)**1.6;domain.hide_render=t>=(FRAMES-1)/FPS
# Probe và bản đủ dùng thư mục cache riêng: Blender chưa lưu blend có thể xoá cache khi dựng lại domain.
render(s,out,update,{'job':'beast-death-ink-smoke','method_short':'Mantaflow 96, bốn luồng mảnh đi lên','seed':SEED,'reference':REFERENCE,'method':'Mantaflow gas fluid simulation; turbulence seed fixed','fluid_resolution':d.resolution_max,'bake_seconds':round(bake,3)},f'Reference: {REFERENCE}\nBlender S3-2 Mantaflow study. Four thin asymmetric ink-smoke jets aligned to screen-up rise and spread with turbulent rolling wisps and open directional channels. Restrained ivory and pale-jade rim illumination. A four-frame emission impulse, physical fluid advection, and a density envelope lead to a completely transparent end. Play-camera elevation 55 degrees, evaluate at 1.5 times body width. 48 renders at 32 fps, fixed turbulence seed {SEED}. Recipe: tools/blender-vfx/s3_mantaflow_smoke_v3.py.')
