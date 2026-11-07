"""S3-2 v3: nối tiếp v2; giảm mật độ, advect theo trục lên, làm mềm sợi và phá chân đối xứng."""
import math,random,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from s3_common import *
SEED=711035;FRAMES=48;FPS=32;REFERENCE='.local/video-review/sheets/beast-death-ink-smoke__take1.jpg'
s,out=setup(FRAMES,FPS);rng=random.Random(SEED)
bpy.ops.mesh.primitive_cube_add(size=2);ob=bpy.context.object;ob.name='soft curling ink density field';ob.scale=(2.1,2.1,2.1)
mat=bpy.data.materials.new('soft anisotropic ink field');mat.use_nodes=True;nt=mat.node_tree;n=nt.nodes;n.clear();l=nt.links

def M(op,a,b=0):
    no=n.new('ShaderNodeMath');no.operation=op
    for k,v in enumerate([a,b]):
        if isinstance(v,(int,float)):no.inputs[k].default_value=v
        else:l.new(v,no.inputs[k])
    return no.outputs[0]
def V(op,a,b):
    no=n.new('ShaderNodeVectorMath');no.operation=op
    for k,v in enumerate([a,b]):
        if isinstance(v,tuple):no.inputs[k].default_value=v
        else:l.new(v,no.inputs[k])
    return no.outputs['Value'] if op=='DOT_PRODUCT' else no.outputs['Vector']
def noise(vec,scale,detail):
    no=n.new('ShaderNodeTexNoise');no.noise_dimensions='4D';no.inputs['Scale'].default_value=scale;no.inputs['Detail'].default_value=detail;no.inputs['Roughness'].default_value=.7;l.new(vec,no.inputs['Vector']);return no
geo=n.new('ShaderNodeNewGeometry');timev=n.new('ShaderNodeValue');gain=n.new('ShaderNodeValue');erosion=n.new('ShaderNodeValue');attack=n.new('ShaderNodeValue')
# Warping the field itself breaks tube symmetry; two noise octaves erode internally.
warp=noise(geo.outputs['Position'],3.6,3);l.new(timev.outputs[0],warp.inputs['W']);offset=V('MULTIPLY',V('SUBTRACT',warp.outputs['Color'],(.5,.5,.5)),(.36,.36,.36));pos=V('ADD',geo.outputs['Position'],offset)
x=V('DOT_PRODUCT',pos,tuple(RIGHT));y=M('SUBTRACT',V('DOT_PRODUCT',pos,tuple(UP)),M('MULTIPLY',timev.outputs[0],.58));z=V('DOT_PRODUCT',pos,tuple(DEPTH))
coarse=noise(pos,5.3,4);fine=noise(pos,16,3);l.new(timev.outputs[0],coarse.inputs['W']);l.new(timev.outputs[0],fine.inputs['W'])
field=0
for i in range(7):
    anchor=rng.uniform(-.65,.65);side=(-1 if anchor<0 else 1);spread=rng.uniform(.30,.75);phase=rng.uniform(0,math.tau);height=rng.uniform(1.45,2.35);radius=rng.uniform(.19,.30)
    u=M('DIVIDE',M('ADD',y,1.25+rng.uniform(-.18,.18)),height);clampu=M('MINIMUM',M('MAXIMUM',u,0),1)
    theta=M('ADD',M('ADD',M('MULTIPLY',clampu,8.1),phase),M('MULTIPLY',timev.outputs[0],1.1))
    curl=M('MULTIPLY',M('SINE',theta),M('MULTIPLY',clampu,.35));xc=M('ADD',M('ADD',M('MULTIPLY',clampu,spread*side),anchor),curl);zc=M('MULTIPLY',M('COSINE',theta),.21)
    radial=M('SQRT',M('ADD',M('POWER',M('SUBTRACT',x,xc),2),M('POWER',M('SUBTRACT',z,zc),2)))
    r=M('MULTIPLY',M('ADD',M('MULTIPLY',M('SINE',M('MULTIPLY',clampu,math.pi)),.85),.15),radius)
    env=M('POWER',M('MAXIMUM',M('SUBTRACT',1,M('DIVIDE',radial,r)),0),2.2)
    valid=M('MULTIPLY',M('GREATER_THAN',u,0),M('LESS_THAN',u,1));env=M('MULTIPLY',env,valid);field=M('ADD',field,env)
porous=M('MAXIMUM',M('SUBTRACT',coarse.outputs['Fac'],erosion.outputs[0]),0);den=M('MULTIPLY',M('MULTIPLY',M('MULTIPLY',field,porous),fine.outputs['Fac']),gain.outputs[0])
vol=n.new('ShaderNodeVolumePrincipled');vol.inputs['Color'].default_value=(.025,.037,.044,1);vol.inputs['Anisotropy'].default_value=.25;l.new(den,vol.inputs['Density']);output=n.new('ShaderNodeOutputMaterial');l.new(vol.outputs[0],output.inputs['Volume']);ob.data.materials.append(mat)
for loc,power,color in [((-2,1,-1.2),700,(1,.94,.84)),((2,1,-1.1),850,(.7,.9,.84))]:
    bpy.ops.object.light_add(type='AREA',location=screen(*loc));a=bpy.context.object;a.rotation_euler=(-a.location).to_track_quat('-Z','Y').to_euler();a.data.energy=power;a.data.color=color;a.data.size=1.8

def update(t):
    end=(FRAMES-1)/FPS;q=min(1,max(0,(t-.13)/(end-.13)));atk=1-math.exp(-t*20)
    ob.hide_render=t<.001 or t>=end;ob.scale=(2.1*(.45+.55*atk),2.1*(.65+.35*atk),2.1*(.65+.35*atk));ob.location=UP*(-.25)
    timev.outputs[0].default_value=t*.85;erosion.outputs[0].default_value=.26+.32*q**.9;gain.outputs[0].default_value=110*atk*(1-q)**1.3
render(s,out,update,{'job':'beast-death-ink-smoke','method_short':'sợi khói mềm, cuộn và trôi lên' ,'seed':SEED,'reference':REFERENCE,'method':'anisotropically warped procedural density field around seven asymmetrical advecting curled filaments; no Mantaflow','death_width_body_ratio':1.5},f'Reference: {REFERENCE}\nBlender S3-2 v3. Seven asymmetric ink-black density filaments curl upward and outward, with broad empty channels, soft porous boundaries, internal small rolling wisps and restrained pale ivory/jade grazing rims. A warped volumetric density field gives soft wispy edges throughout the volume. Fast release, slow internal advection and erosion, final alpha zero. Evaluate at 1.5 times beast body width at 55-degree camera elevation. 48 unique rendering times at 32 fps over 1.5 seconds. Seed {SEED}. Exact recipe: tools/blender-vfx/s3_field_smoke_v3.py.')
