"""S3: tiện ích riêng, giữ nguyên recipe D1 và chỉ ghi trong vùng được giao."""
import hashlib, json, math, os, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
for key in ('TMPDIR','BLENDER_USER_CONFIG','BLENDER_USER_SCRIPTS','BLENDER_USER_DATAFILES','BLENDER_USER_RESOURCES'):
    folder=ROOT/'.local/s3/blender-home'/key.lower(); folder.mkdir(parents=True,exist_ok=True); os.environ[key]=str(folder)
import bpy
from mathutils import Vector
RIGHT=Vector((1,0,0)); UP=Vector((0,math.sin(math.radians(55)),math.cos(math.radians(55))))
DEPTH=RIGHT.cross(UP)
def screen(x,y,z=0): return RIGHT*x+UP*y+DEPTH*z

def setup(frames,fps=48):
    out=Path(sys.argv[sys.argv.index('--')+1]).resolve(); out.relative_to(ROOT/'.local'); out.mkdir(parents=True,exist_ok=True); (out/'rgba').mkdir(exist_ok=True)
    bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
    s=bpy.context.scene; s.render.engine=os.environ.get('VFX_ENGINE','BLENDER_EEVEE')
    s.render.resolution_x=s.render.resolution_y=int(os.environ.get('VFX_SIZE','512')); s.render.resolution_percentage=100
    s.render.fps=fps; s.frame_start=1; s.frame_end=frames
    s.render.film_transparent=True; s.render.image_settings.file_format='PNG'; s.render.image_settings.color_mode='RGBA'; s.render.image_settings.color_depth='8'
    s.render.threads_mode='FIXED'; s.render.threads=6; s.view_settings.view_transform='Standard'; s.view_settings.look='None'; s.world.color=(0,0,0)
    if s.render.engine=='BLENDER_EEVEE':
        s.eevee.taa_render_samples=48; s.eevee.volumetric_tile_size='2'; s.eevee.volumetric_samples=96
        s.eevee.use_volume_custom_range=True; s.eevee.volumetric_start=3; s.eevee.volumetric_end=11
    bpy.ops.object.camera_add(location=DEPTH*7)
    cam=bpy.context.object; cam.rotation_euler=(-cam.location).to_track_quat('-Z','Y').to_euler(); cam.data.type='ORTHO'; cam.data.ortho_scale=5.6; s.camera=cam
    return s,out

def emissive(name,color,strength):
    m=bpy.data.materials.new(name); m.use_nodes=True; n=m.node_tree.nodes; n.clear(); l=m.node_tree.links
    e=n.new('ShaderNodeEmission'); e.inputs[0].default_value=(*color,1); e.inputs[1].default_value=strength
    tr=n.new('ShaderNodeBsdfTransparent'); mix=n.new('ShaderNodeMixShader'); mix.inputs[0].default_value=1
    l.new(tr.outputs[0],mix.inputs[1]); l.new(e.outputs[0],mix.inputs[2]); o=n.new('ShaderNodeOutputMaterial'); l.new(mix.outputs[0],o.inputs['Surface'])
    return m,mix.inputs[0]

def glow(s):
    nt=bpy.data.node_groups.new('S3 thin-core halo','CompositorNodeTree'); s.compositing_node_group=nt; nt.interface.new_socket(name='Image',in_out='OUTPUT',socket_type='NodeSocketColor')
    r=nt.nodes.new('CompositorNodeRLayers'); g=nt.nodes.new('CompositorNodeGlare'); g.inputs['Type'].default_value='Fog Glow'; g.inputs['Quality'].default_value='High'; g.inputs['Threshold'].default_value=1.4; g.inputs['Size'].default_value=.17
    nt.links.new(r.outputs['Image'],g.inputs['Image']); bw=nt.nodes.new('CompositorNodeRGBToBW'); nt.links.new(g.outputs['Image'],bw.inputs[0])
    mx=nt.nodes.new('ShaderNodeMath'); mx.operation='MAXIMUM'; nt.links.new(r.outputs['Alpha'],mx.inputs[0]); nt.links.new(bw.outputs[0],mx.inputs[1])
    a=nt.nodes.new('CompositorNodeSetAlpha'); a.inputs['Type'].default_value='Replace Alpha'; nt.links.new(g.outputs['Image'],a.inputs['Image']); nt.links.new(mx.outputs[0],a.inputs['Alpha']); o=nt.nodes.new('NodeGroupOutput'); nt.links.new(a.outputs[0],o.inputs[0])

def render(s,out,update,meta,prompt):
    for p in [Path(__file__),Path(sys.argv[sys.argv.index('-P')+1])]: (out/p.name).write_bytes(p.read_bytes())
    (out/'sample.prompt.txt').write_text(prompt+'\n',encoding='utf-8')
    frames=[int(x) for x in os.environ['VFX_TEST_FRAMES'].split(',')] if os.environ.get('VFX_TEST_FRAMES') else range(1,s.frame_end+1)
    started=time.monotonic(); times=[]
    for f in frames:
        s.frame_set(f); update((f-1)/s.render.fps); s.render.filepath=str(out/'rgba'/f'{f:04d}.png'); tick=time.monotonic(); bpy.ops.render.render(write_still=True)
        times.append({'frame':f,'seconds':round(time.monotonic()-tick,3)}); print('S3_FRAME',f,times[-1]['seconds'],flush=True)
    data=dict(meta,blender=bpy.app.version_string,engine=s.render.engine,fps=s.render.fps,frames=s.frame_end,duration=s.frame_end/s.render.fps,resolution=[s.render.resolution_x,s.render.resolution_y],camera_elevation=55,render_seconds=round(time.monotonic()-started,3),frame_times=times,source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(sys.argv[sys.argv.index('-P')+1])]})
    (out/('probe.json' if os.environ.get('VFX_TEST_FRAMES') else 'render.json')).write_text(json.dumps(data,indent=2),encoding='utf-8')
