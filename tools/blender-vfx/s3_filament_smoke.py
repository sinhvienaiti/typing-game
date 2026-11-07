"""S3-2: thể tích kéo sợi theo spline cuộn; không sửa volume cụm tròn D1."""
import math, random, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from s3_common import *
SEED=711032; FRAMES=48; FPS=32
REFERENCE='.local/video-review/sheets/beast-death-ink-smoke__take1.jpg'
s,out=setup(FRAMES,FPS);rng=random.Random(SEED)
def area(name,loc,power,color,size):
    bpy.ops.object.light_add(type='AREA',location=screen(*loc));ob=bpy.context.object;ob.name=name;ob.rotation_euler=(-ob.location).to_track_quat('-Z','Y').to_euler();ob.data.energy=power;ob.data.color=color;ob.data.shape='DISK';ob.data.size=size
area('ivory grazing rim',(-2,1,-1.2),350,(1,.94,.82),2)
area('pale jade rim',(2,1,-1.4),500,(.7,.89,.82),1.5)
area('soft face',(0,1,3),15,(.6,.68,.72),3)
# Local, anisotropic noise breaks up the tube surface; the tube path creates directional curls.
clouds=[]
for i in range(9):
    mesh=bpy.data.meshes.new(f'filament volume {i}');ob=bpy.data.objects.new(f'curling ink strand {i}',mesh);s.collection.objects.link(ob)
    mat=bpy.data.materials.new(f'porous ink filament {i}');mat.use_nodes=True;nt=mat.node_tree;nt.nodes.clear();n=nt.nodes;l=nt.links
    def mathnode(op,a,b):
        no=n.new('ShaderNodeMath');no.operation=op
        for k,v in enumerate([a,b]):
            if isinstance(v,(int,float)):no.inputs[k].default_value=v
            else:l.new(v,no.inputs[k])
        return no.outputs[0]
    coord=n.new('ShaderNodeTexCoord');mapping=n.new('ShaderNodeVectorMath');mapping.operation='MULTIPLY';l.new(coord.outputs['Generated'],mapping.inputs[0]);mapping.inputs[1].default_value=(1.4,1.4,.50)
    noise=n.new('ShaderNodeTexNoise');noise.noise_dimensions='4D';noise.inputs['Scale'].default_value=8;noise.inputs['Detail'].default_value=4;noise.inputs['Roughness'].default_value=.7;l.new(mapping.outputs[0],noise.inputs['Vector'])
    fine=n.new('ShaderNodeTexNoise');fine.noise_dimensions='4D';fine.inputs['Scale'].default_value=21;fine.inputs['Detail'].default_value=2.5;l.new(mapping.outputs[0],fine.inputs['Vector'])
    threshold=n.new('ShaderNodeValue');gain=n.new('ShaderNodeValue')
    density=mathnode('MAXIMUM',mathnode('SUBTRACT',noise.outputs['Fac'],threshold.outputs[0]),0);density=mathnode('MULTIPLY',density,fine.outputs['Fac']);density=mathnode('MULTIPLY',density,gain.outputs[0])
    vol=n.new('ShaderNodeVolumePrincipled');vol.inputs['Color'].default_value=(.006,.010,.012,1);vol.inputs['Anisotropy'].default_value=.25;l.new(density,vol.inputs['Density'])
    o=n.new('ShaderNodeOutputMaterial');l.new(vol.outputs[0],o.inputs['Volume']);mesh.materials.append(mat)
    side=rng.choice([-1,1]);spread=.17+(i/8)*.62;phase=rng.uniform(0,math.tau);radius=rng.uniform(.17,.28) if i<6 else rng.uniform(.08,.14)
    clouds.append((ob,noise,fine,threshold,gain,side,spread,phase,radius,rng.uniform(-.38,.38),rng.uniform(.75,1.18)))
def update(t):
    end=(FRAMES-1)/FPS;q=min(1,max(0,(t-.18)/(end-.18)));attack=1-math.exp(-t*17)
    for i,(ob,noise,fine,threshold,gain,side,spread,phase,radius,anchor,height) in enumerate(clouds):
        ob.hide_render=t<.001 or t>=end
        if ob.hide_render:continue
        verts=[];faces=[];N=45;K=10
        # Long holes remain between separate streams; tips curl, not circular lobes.
        for k in range(N):
            u=k/(N-1);curl=(max(0,(u-.4)/.6))**1.5
            theta=phase+u*5.6+t*1.2
            x=anchor+side*(spread*u*1.65)+math.sin(theta)*(.10+.28*curl)*attack
            y=-1.12+u*(1.45+.75*attack)*height+t*.23+.14*math.cos(theta)*curl
            z=.12*math.sin(theta*.8+i)
            x*=.28+.72*attack
            r=radius*(.18+.82*math.sin(math.pi*u)**.6)*(.48+.52*attack)*(1-.25*q)
            # Rippling boundary gives taper and holes at scale; density noise supplies inner rolling wisps.
            r*=.72+.28*math.sin(u*22+phase-t*3)**2
            for j in range(K):
                angle=math.tau*j/K;verts.append(screen(x+r*math.cos(angle),y,z+r*.82*math.sin(angle)))
        for k in range(N-1):
            for j in range(K):faces.append((k*K+j,k*K+(j+1)%K,(k+1)*K+(j+1)%K,(k+1)*K+j))
        faces.append(tuple(reversed(range(K))));faces.append(tuple((N-1)*K+j for j in range(K)))
        ob.data.clear_geometry();ob.data.from_pydata(verts,[],faces);ob.data.update()
        noise.inputs['W'].default_value=phase+t*.7;fine.inputs['W'].default_value=phase+t*1.1
        threshold.outputs[0].default_value=.25+.30*q**1.1;gain.outputs[0].default_value=220*attack*(1-q)**1.45
render(s,out,update,{'job':'beast-death-ink-smoke','method_short':'thể tích kéo sợi có cuộn xoáy','seed':SEED,'reference':REFERENCE,'strands':9,'method':'bounded noise volumes swept along evolving curling filaments; not a fluid simulation','death_width_body_ratio':1.5},f'Reference: {REFERENCE}\nBlender S3-2. Ink-black smoke rises and opens into nine separated tapered filaments, with curved directional eddies, long empty channels between the streams, porous fine inner wisps, and pale ivory/jade grazing rims. A fast upward-outward release gives way to slower curling and density erosion, reaching alpha zero at the end. Evaluate composited at 1.5 times beast body width with 55-degree play-camera elevation. 48 unique samples at 32 fps over 1.5 seconds. Seed {SEED}. Recipe: tools/blender-vfx/s3_filament_smoke.py; directional bounded noisy volumes, not Mantaflow.')
