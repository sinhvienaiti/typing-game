"""S3-1 v2: nới máy 1,07% để extent nằm dưới 65%; giữ recipe v1/D1."""
import math, random, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from s3_common import *
SEED=711031; FRAMES=32; FPS=48
REFERENCE='.local/video-review/sheets/beast-hit-spark-burst__take1.jpg'
s,out=setup(FRAMES,FPS); s.camera.data.ortho_scale=5.66; glow(s); rng=random.Random(SEED)
particles=[]
for i in range(211):
    main=i<7; medium=7<=i<31
    angle=math.radians(([-9,1,12,23,32,41,50][i] if main else rng.uniform(-10,50)))
    direction=Vector((math.cos(angle),math.sin(angle)))
    distance=rng.uniform(2.65,3.17) if main else rng.uniform(.75,3.0)
    life=rng.uniform(.24,.42) if main else rng.uniform(.30,.59)
    delay=0 if main else rng.uniform(.0,.045)
    if i==210: life=.64; delay=0
    width=rng.uniform(.012,.021) if main else rng.uniform(.005,.009) if medium else rng.uniform(.003,.007)
    tail=rng.uniform(.65,1.30) if main else rng.uniform(.12,.32) if medium else rng.uniform(.012,.05)
    color=(1,.92,.75) if i%4 else (.57,.89,.79)
    m,alpha=emissive(f'S3 spark {i}',color,3.2 if main else 1.7 if medium else 1.3)
    mesh=bpy.data.meshes.new(f'taper {i}'); ob=bpy.data.objects.new(f'{"primary" if main else "dust"}-{i}',mesh); s.collection.objects.link(ob); mesh.materials.append(m)
    particles.append((ob,alpha,direction,distance,life,delay,width,tail,rng.uniform(-.075,.075),rng.uniform(-.06,.06)))
# Deux filaments très fins: ancrage du contact, pas une boule lumineuse.
cores=[]
for angle,length,width in [(20,.62,.014),(100,.28,.007)]:
    mesh=bpy.data.meshes.new('core'); ob=bpy.data.objects.new('thin contact filament',mesh); s.collection.objects.link(ob); m,a=emissive('ivory core',(1,.95,.83),7); mesh.materials.append(m); cores.append((ob,a,math.radians(angle),length,width))
def ribbon(ob,points,widths):
    verts=[]
    for k,(x,y,z) in enumerate(points):
        prev=points[max(0,k-1)]; nxt=points[min(len(points)-1,k+1)]; dx=nxt[0]-prev[0]; dy=nxt[1]-prev[1]; ln=max(.00001,math.hypot(dx,dy)); w=widths[k]
        verts.extend([screen(x-dy/ln*w,y+dx/ln*w,z),screen(x+dy/ln*w,y-dx/ln*w,z)])
    faces=[(2*k,2*k+1,2*k+3,2*k+2) for k in range(len(points)-1)]; ob.data.clear_geometry(); ob.data.from_pydata(verts,[],faces); ob.data.update()
def update(t):
    for ob,a,angle,length,w in cores:
        a.default_value=max(0,1-t/.075)**2; ob.hide_render=t>=.075
        d=(math.cos(angle),math.sin(angle)); ribbon(ob,[(-1.35+d[0]*v*length,-.42+d[1]*v*length,0) for v in [-1,0,1]],[0,w,0])
    for ob,a,d,dist,life,delay,w,tail,bend,offset in particles:
        age=t-delay; ob.hide_render=age<0 or age>=life or t>=(FRAMES-1)/FPS
        if ob.hide_render:continue
        q=age/life; travel=dist*(1-math.exp(-age/ .075)); tl=min(travel,tail*(.8+.2*(1-q)))
        a.default_value=(1-q)**.7
        pts=[]; widths=[]
        for k in range(11):
            u=k/10; r=travel-tl*(1-u); pts.append((-1.35+d.x*r,-.42+offset+d.y*r+bend*r*r-.28*age*age,0)); widths.append(w*math.sin(math.pi*u)**.8*(.65+.35*(1-q)))
        ribbon(ob,pts,widths)
render(s,out,update,{'seed':SEED,'camera_ortho_scale':5.66,'job':'beast-hit-spark-burst','method_short':'7 tia chính + 24 tia phụ + 180 hạt mịn','reference':REFERENCE,'primary_streaks':7,'secondary_streaks':24,'fine_particles':180,'fan_degrees':60,'main_direction_degrees':20,'impact_pivot':[.259,.575],'method':'camera-facing tapered emission trails; seeded drag trajectories; separate fine dust'},f'Reference: {REFERENCE}\nBlender S3-1. Seven elongated tapered primary ivory and pale-jade trails follow a 60-degree impact fan to screen-right and upward. Twenty-four short secondary trails and 180 fine motes form separate scale layers. Two thin ivory contact filaments flash briefly at the anchored strike. Restrained coloured halos, fast release and long cooling decay, complete transparent ending. Target occupied extent 55–65 percent of the square. 32 unique renders at 48 fps over 0.667 seconds. Seed {SEED}. Exact recipe: tools/blender-vfx/s3_directional_spark_v2.py. Orthographic camera span 5.66, refined from v1 span 5.6 to keep the measured extent below 65 percent.')
