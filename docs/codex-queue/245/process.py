#!/usr/bin/env python3
"""Phiếu 245: hậu kỳ và kiểm ảnh độc lập, không chạy game.
Chạy: python3 docs/codex-queue/245/process.py <thư-mục-mới> [selection.json]
Yêu cầu Python 3 chuẩn, ImageMagick 7; không cần Pillow hoặc mạng.
"""
import json, subprocess, sys, math, colorsys, os, statistics, shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).parent
OUT=Path(sys.argv[1]); OUT.mkdir(parents=True,exist_ok=False)
MAG='/opt/homebrew/bin/magick'; FONT='/System/Library/Fonts/Supplemental/Arial.ttf'
SEL=json.loads(Path(sys.argv[2]).read_text()) if len(sys.argv)>2 else {}
def run(args): return subprocess.check_output([MAG,*map(str,args)])
def make(args,p):
    p=Path(p); assert not p.exists(),p
    run([*args,'-colorspace','sRGB','-depth','8','-define','png:color-type=6',p]);return p
def dim(p): return tuple(map(int,run(['identify','-format','%w %h',p]).split()))
def rgba(p,n=None):
    args=[p]
    if n: args+=['-filter','Lanczos','-resize',f'{n}x{n}!']
    return run([*args,'-alpha','on','-depth','8','rgba:-'])
def bbox(p,t=16):
    b=rgba(p);w,h=dim(p);I=[i for i,a in enumerate(b[3::4]) if a>t]
    return min(i%w for i in I),min(i//w for i in I),max(i%w for i in I)+1,max(i//w for i in I)+1
def mask(p,n=24,t=128):
    b=rgba(p,n);return {(i%n,i//n) for i,a in enumerate(b[3::4]) if a>t}
def bounds(s):return min(x for x,y in s),min(y for x,y in s),max(x for x,y in s)+1,max(y for x,y in s)+1
def opening(s):
    e={(x,y) for x,y in s if all((x+dx,y+dy) in s for dx,dy in [(0,0),(1,0),(0,1),(1,1)])}
    return {(x+dx,y+dy) for x,y in e for dx,dy in [(0,0),(1,0),(0,1),(1,1)]}
def iou(a,b):return len(a&b)/max(1,len(a|b))
def luma(rgb):return sum(v*c/255 for v,c in zip(rgb,[.2126,.7152,.0722]))
def wcag(rgb):
    v=[x/255 for x in rgb];v=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in v]
    return sum(x*c for x,c in zip(v,[.2126,.7152,.0722]))
def prompt(p,text):p.with_suffix('.prompt.txt').write_text(text+'\n')
def clean_edge(src,dst,keyed):
    b=bytearray(rgba(src));w,h=dim(src)
    edge=run([src,'-alpha','extract','-bordercolor','black','-border','3','-threshold','50%','-morphology','Edge','Disk:3','-shave','3x3','-depth','8','gray:-'])
    edgesix=run([src,'-alpha','extract','-bordercolor','black','-border','6','-threshold','50%','-morphology','Edge','Disk:6','-shave','6x6','-depth','8','gray:-'])
    ac=cc=0
    for i in range(w*h):
        j=4*i;a=b[j+3]
        if a not in (0,255) and edge[i]==0:
            target=0 if a<128 else 255
            if abs(target-a)<=32:b[j+3]=target;ac+=1
        if not keyed or not b[j+3] or not edgesix[i]:continue
        hh,ss,vv=colorsys.rgb_to_hsv(*(v/255 for v in b[j:j+3]))
        if 285<=hh*360<=330 and ss>.5:
            # Chỉ khử màu khóa còn loang ở mép ngoài 6 px.
            # Giữ luma gần nguyên, không sửa vân hay phần tranh bên trong.
            grey=round(luma(b[j:j+3])*255);b[j:j+3]=bytes([grey]*3);cc+=1
    # Bỏ đốm alpha rời 1 px do rung Lanczos ở mép khung; không xóa tranh.
    s={i for i,a in enumerate(b[3::4]) if a>16};islands=[]
    while s:
        start=s.pop();stack=[start];comp=[start]
        while stack:
            i=stack.pop();x=i%w
            for j,valid in [(i-1,x>0),(i+1,x<w-1),(i-w,i>=w),(i+w,i<w*(h-1))]:
                if valid and j in s:s.remove(j);stack.append(j);comp.append(j)
        if len(comp)<20:islands.extend(comp)
    for i in islands:b[4*i+3]=0
    assert not Path(dst).exists()
    subprocess.run([MAG,'-size',f'{w}x{h}','-depth','8','rgba:-','-colorspace','sRGB','-define','png:color-type=6',str(dst)],input=b,check=True)
    return dict(alpha_rounded_pixels=ac,edge_despill_pixels=cc,isolated_edge_pixels_removed=len(islands),rgb_interior_changed=0)
def nine(src,sl,wh,p,scale=1):
    w,h=dim(src);W,H=wh;l,r,t,b=sl
    dl,dr,dt,db=[max(1,round(x*scale)) for x in sl]
    if dl+dr>=W or dt+db>=H:raise ValueError((src,wh,sl,scale))
    xs=[0,l,w-r,w];ys=[0,t,h-b,h];dx=[0,dl,W-dr,W];dy=[0,dt,H-db,H]
    args=['-size',f'{W}x{H}','xc:none']
    for iy in range(3):
        for ix in range(3):
            sw,sh=xs[ix+1]-xs[ix],ys[iy+1]-ys[iy]
            dw,dh=dx[ix+1]-dx[ix],dy[iy+1]-dy[iy]
            args+=['(',src,'-crop',f'{sw}x{sh}+{xs[ix]}+{ys[iy]}','+repage','-filter','Lanczos','-resize',f'{dw}x{dh}!',')','-geometry',f'+{dx[ix]}+{dy[iy]}','-composite']
    return make(args,p)
def sheet(images,p,tile):
    subprocess.check_call([MAG,'montage',*map(str,images),'-background','#20242b','-geometry','+8+8','-tile',tile,str(p)])
def caption(src,text,p):
    return make([src,'-background','#20242b','-gravity','south','-splice','0x26','-font',FONT,'-pointsize','13','-fill','#f3ead2','-annotate','+0+5',text],p)

games={
 'dh':dict(game='Dragonhold',folder='games/dragon-hold/art-src/ui/frames',panel='panel-large.alpha.png',json='panel-large.json',scale=.12),
 'ww':dict(game='Wordwoven',folder='games/typing-defense/art-src/ui/frames-epic',panel='panel-large.v2.alpha.png',json='panel-large.v2.json',scale=.18),
 'll':dict(game='Last Line',folder='games/typing-survival/art-src/ui/frames-epic',panel='panel-large.alpha.png',json='panel-large.json',scale=.16)}
assets=[]
for tag,g in games.items():
    if tag!='ll':
        for name,num in [('list-row',2),('list-row-active',1)]:
            assets.append(dict(tag=tag,name=name,src=ROOT/g['folder']/f'{name}.try{num}.png',folder=g['folder'],kind='row'))
    assets.append(dict(tag=tag,name='close',src=ROOT/g['folder']/'close.try1.png',folder=g['folder'],kind='icon'))
for a in json.loads((BASE/'assets.json').read_text())[3:]:
    assets.append(dict(tag='ll',name=a['name'],src=ROOT/a['folder']/(a['name']+'.try1.png'),folder=a['folder'],kind='foe'))
metrics={};processed={};records=[]
for a in assets:
    tag,name,kind=a['tag'],a['name'],a['kind'];key=tag+'-'+name
    src=ROOT/SEL.get(key,str(a['src'].relative_to(ROOT))); assert src.exists(),src
    rawprompt=src.with_suffix('.prompt.txt').read_text()
    if tag in ['dh','ww']:
        k=OUT/(key+'-key.png')
        cache=BASE/'stage-v1'/(key+'.key.png')
        if cache.exists() and key not in SEL:shutil.copyfile(cache,k)
        else:subprocess.check_call(['bash',str(ROOT/'tools/art-normalize/key-alpha.sh'),str(src),str(k),'--mode','global','--despill','protect-interior'],env=dict(os.environ,ART_MAGICK=MAG),stdout=subprocess.DEVNULL)
    else:k=src
    # Tách nền/chuẩn hoá alpha: bỏ sương bán trong suốt; RGB nguyên vẹn.
    # Nhị phân ở nguồn rồi Lanczos tạo mép AA hẹp khi thu; không làm nét.
    matte=make([k,'(',k,'-alpha','extract','-threshold','50%',')','-alpha','off','-compose','CopyOpacity','-composite'],OUT/(key+'-matte.png'))
    x0,y0,x1,y1=bbox(matte);crop=f'{x1-x0}x{y1-y0}+{x0}+{y0}'
    if kind=='row':
        # Chỉ đổi kích thước theo cách cắt chín mảnh: co đều về cao 256,
        # giữ nguyên hai đầu, co lòng/cạnh giữa theo chiều ngang.
        tall=make([matte,'-crop',crop,'+repage','-filter','Lanczos','-resize','x256'],OUT/(key+'-height256.png'))
        sl=[200,200,48,48]
        pre=nine(tall,sl,(1536,256),OUT/(key+'-pre-edge.png'))
        final=OUT/(key+'.png');cleanup=clean_edge(pre,final,True)
        b=rgba(final);w,h=dim(final);center=[]
        for y in range(80,176):
            for x in range(256,1280):center.append(tuple(b[4*(y*w+x):4*(y*w+x)+3]))
        med=tuple(round(statistics.median(c[i] for c in center)) for i in range(3))
        conf=dict(size=[1536,256],slice=dict(zip(['left','right','top','bottom'],sl)),fill='#%02x%02x%02x'%med,repeat='stretch',display_scale=34/256,center='stretch',source=src.name,notes='Lòng dùng nguyên tranh; fill chỉ là siêu dữ liệu. Viền trên/dưới 48 px = 18,75% chiều cao. Hiển thị cả bốn đường cắt ở cùng tỷ lệ 34/256 hoặc 51/256.')
        (OUT/(key+'.json')).write_text(json.dumps(conf,ensure_ascii=False,indent=2)+'\n')
        # Độ lệch luma theo chiều kéo của hai rail thẳng.
        rail=[]
        for y in [16,24,32,224,232,240]:
            vals=[luma(b[4*(y*w+x):4*(y*w+x)+3]) for x in range(220,1316)]
            rail.append(statistics.pstdev(vals))
        rail_profiles=[]
        for y0,y1 in [(0,48),(208,256)]:
            vals=[statistics.mean(luma(b[4*(y*w+x):4*(y*w+x)+3]) for y in range(y0,y1)) for x in range(220,1316)]
            rail_profiles.append(statistics.pstdev(vals))
        metrics[key]=dict(size=[1536,256],slice_pct=48/256*100,rail_single_scanline_stdev_max=max(rail),rail_luma_stdev_max=max(rail_profiles),rail_measurement='Độ lệch chuẩn của luma trung bình mỗi cột trong dải viền 48 px; chỉ đoạn x=220..1315, bỏ hai đầu.',fill=conf['fill'],text_wcag=(wcag([243,234,210])+.05)/(wcag(med)+.05))
    else:
        brighten=['-channel','RGB','-evaluate','Multiply','1.10','+channel'] if key in ['dh-close','ll-brute.small','ll-splitter.small'] else []
        pre=make([matte,'-crop',crop,'+repage',*brighten,'-filter','Lanczos','-resize','716x716','-background','none','-gravity','center','-extent','1024x1024'],OUT/(key+'-pre-edge.png'))
        final=OUT/(key+'.png');cleanup=clean_edge(pre,final,tag in ['dh','ww'])
        for n in [256,128,64]:
            pre_small=make([final,'-filter','Lanczos','-resize',f'{n}x{n}'],OUT/(key+f'.{n}-pre-edge.png'))
            q=OUT/(key+f'.{n}.png');clean_edge(pre_small,q,tag in ['dh','ww']);prompt(q,rawprompt)
    prompt(final,rawprompt)
    # Tờ bản sinh | bản hậu kỳ, không sửa phần vẽ.
    before=make([src,'-filter','Lanczos','-resize','256x256','-background','#20242b','-alpha','remove','-alpha','off','-gravity','center','-extent','272x272'],OUT/(key+'-raw-tile.png'))
    after=make([final,'-filter','Lanczos','-resize','256x256','-background','#20242b','-alpha','remove','-alpha','off','-gravity','center','-extent','272x272'],OUT/(key+'-final-tile.png'))
    proof=make([before,after,'+append'],OUT/(key+'-raw-vs-final.png'))
    prompt(proof,rawprompt)
    b=rgba(final);w,h=dim(final);bb=bbox(final);alph=b[3::4]
    partial=[i for i,v in enumerate(alph) if 0<v<255]
    edge=run([final,'-alpha','extract','-bordercolor','black','-border','3','-threshold','50%','-morphology','Edge','Disk:3','-shave','3x3','-depth','8','gray:-'])
    stray=sum(edge[i]==0 for i in partial)
    colour=0;nonzero=0
    for i in range(0,len(b),4):
        if not b[i+3]:continue
        nonzero+=1;hh,ss,vv=colorsys.rgb_to_hsv(*(v/255 for v in b[i:i+3]));colour+=int(285<=hh*360<=330 and ss>.5)
    m=metrics.setdefault(key,{})
    m.update(cleanup=cleanup,size=[w,h],alpha_min=min(alph),alpha_max=max(alph),bbox=list(bb),longside_pct=max(bb[2]-bb[0],bb[3]-bb[1])/w*100,centre_offset_pct=[((bb[0]+bb[2])/2-w/2)/w*100,((bb[1]+bb[3])/2-h/2)/h*100],partial_outside_3px=stray,key_magenta_pct=100*colour/max(1,nonzero))
    if kind!='row':
        n=24 if kind=='foe' else 32;s=mask(final,n);x0,y0,x1,y1=bounds(s)
        m.update(display_720=n,opening_pct=100*len(opening(s))/len(s),coverage_pct=100*len(s)/((x1-x0)*(y1-y0)),pixels_720=len(s))
    processed[key]=final;records.append(a|dict(src=str(src.relative_to(ROOT)),staged=str(final),prompt=rawprompt))
    print('processed',key,flush=True)

# Nền panel thật: giữ hình góc/cạnh, không thay bằng fill.
panels={}
for tag,g in games.items():
    src=ROOT/g['folder']/g['panel'];conf=json.loads((ROOT/g['folder']/g['json']).read_text());w,h=dim(src)
    sl=list(conf['slice'].values())
    # Một số khung alpha và JSON của đợt cũ khác khổ. Quy đổi đồng đều
    # đường cắt theo khổ ảnh thực; không suy diễn fill.
    cw,ch=conf['size'];sl=[round(sl[0]*w/cw),round(sl[1]*w/cw),round(sl[2]*h/ch),round(sl[3]*h/ch)]
    for label,W,H,f in [('720',360,300,1),('1080',540,450,1.5)]:
        panels[tag,label]=nine(src,sl,(W,H),OUT/(tag+'-panel-'+label+'.png'),g['scale']*f)

names=['Raindrop Tile','Hail Stone','Velvet Switch','Marble Key','Cedar Tap']
for tag,g in games.items():
    for label,n,f in [('720',32,1),('1080',44,1.5)]:
        panel=panels[tag,label];W,H=dim(panel)
        ico=make([processed[tag+'-close'],'-filter','Lanczos','-resize',f'{n}x{n}'],OUT/(tag+'-close-'+label+'-icon.png'))
        x,y=W-round(45*f)-n,round(42*f)
        # Ô cỡ thật của Close là góc trên phải panel, nhãn trống.
        cell=make([panel,ico,'-geometry',f'+{x}+{y}','-composite','-crop',f'{round(120*f)}x{round(76*f)}+{W-round(120*f)}+0','+repage'],OUT/(tag+'-close-'+label+'.png'))
        make([cell,'-filter','point','-resize','400%'],OUT/(tag+'-close-'+label+'-4x.png'))
        bg=rgba(panel);ib=rgba(ico);values=[];sx=[];bx=[]
        for iy in range(n):
            for ix in range(n):
                ii=4*(iy*n+ix);bi=4*((y+iy)*W+x+ix)
                if ib[ii+3]>128:
                    lv=luma(ib[ii:ii+3]);bv=luma(bg[bi:bi+3]);values.append(abs(lv-bv));sx.append(lv);bx.append(bv)
        metrics[tag+'-close']['contrast_'+label]=dict(mean_abs_luma=statistics.mean(values),mean_subject_minus_bg=statistics.mean(sx)-statistics.mean(bx))
    if tag=='ll':continue
    for label,W,H,f in [('720',300,34,1),('1080',450,51,1.5)]:
        args=[panels[tag,label]]
        for i,text in enumerate(names):
            state='list-row-active' if i==1 else 'list-row';key=tag+'-'+state
            row=nine(processed[key],[200,200,48,48],(W,H),OUT/(tag+'-'+label+f'-row{i}.png'),H/256)
            rowtext=make([row,'-font',FONT,'-pointsize',str(round(15*f)),'-fill','#f3ead2','-gravity','west','-annotate',f'+{round(39*f)}+0',text],OUT/(tag+'-'+label+f'-row{i}-text.png'))
            args+=[rowtext,'-geometry',f'+{round(30*f)}+{round((66+i*40)*f)}','-composite']
        mock=make(args,OUT/(tag+'-list-'+label+'.png'))
        make([mock,'-filter','point','-resize','400%'],OUT/(tag+'-list-'+label+'-4x.png'))
    metrics[tag+'-list-pair']=dict(iou_source=iou(mask(processed[tag+'-list-row'],256),mask(processed[tag+'-list-row-active'],256)),iou_720=iou(mask(OUT/(tag+'-720-row0.png'),34),mask(OUT/(tag+'-720-row1.png'),34)))

foes=[a for a in assets if a['kind']=='foe'];pairs=[]
for i,a in enumerate(foes):
    for b in foes[i+1:]:
        pairs.append(dict(a=a['name'],b=b['name'],iou=iou(mask(processed['ll-'+a['name']]),mask(processed['ll-'+b['name']]))))
metrics['foe_pairs_24']=pairs
# Các nút Close cùng nghĩa ở ba game được miễn khác dáng.
metrics['close_pair_exemption']='Ba nút cùng hành động Close; yêu cầu đĩa tròn giống nhau, không áp IoU khác dáng giữa ba game.'
frame=ROOT/'games/typing-survival/art-src/ui/frames-epic'
for label,n,f in [('720',24,1),('1080',36,1.5)]:
    word=nine(frame/'word-plate.alpha.png',[230,230,220,220],(round(112*f),round(64*f)),OUT/('word-'+label+'.png'),.04*f)
    cells=[]
    for i,a in enumerate(foes):
        key='ll-'+a['name'];p=processed[key];title=a['name'].split('.small')[0].replace('-',' ').title()
        ico=make([p,'-filter','Lanczos','-resize',f'{n}x{n}'],OUT/(key+'-'+label+'-icon.png'))
        W,H=dim(word);x,y=(W-n)//2,round(10*f)
        cell=make([word,ico,'-geometry',f'+{x}+{y}','-composite','-font',FONT,'-pointsize',str(round(10*f)),'-fill','#f3ead2','-gravity','south','-annotate',f'+0+{round(9*f)}',title],OUT/(key+'-'+label+'.png'));cells.append(cell)
        bg=rgba(word);ib=rgba(ico);sv=[];bv=[]
        for iy in range(n):
            for ix in range(n):
                ii=4*(iy*n+ix);bi=4*((iy+y)*W+ix+x)
                if ib[ii+3]>128:sv.append(luma(ib[ii:ii+3]));bv.append(luma(bg[bi:bi+3]))
        metrics[key]['contrast_'+label]=dict(mean_subject_minus_bg=statistics.mean(sv)-statistics.mean(bv))
    row=make([*cells,'+append'],OUT/('foes-'+label+'-1x.png'));make([row,'-filter','point','-resize','400%'],OUT/('foes-'+label+'-4x.png'))

(OUT/'metrics.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n')
for r in records:r.pop('prompt')
(OUT/'records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2,default=str)+'\n')
print('done',OUT,flush=True)
