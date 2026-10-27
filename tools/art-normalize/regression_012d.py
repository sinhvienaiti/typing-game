"""Ca hồi quy 012d bằng ảnh tổng hợp; không truy cập dữ liệu game."""
import importlib.util
import json
import math
import os
from pathlib import Path
import signal
from unittest.mock import patch
import normalize as n


def check(ok, message):
    if not ok:raise RuntimeError(message)


def load_job(filename='rebuild_012c.py'):
    path=n.ROOT/'jobs/dragon-hold-012'/filename
    spec=importlib.util.spec_from_file_location('job_test_012d',path)
    job=importlib.util.module_from_spec(spec);spec.loader.exec_module(job)
    return job


def run(d):
    job=load_job()
    # A colour near, but off the key-to-paint line must not be recoloured.
    sample=bytearray([0,255,0,255]*45);point=22
    sample[point*4:point*4+4]=bytes((55,155,32,255));sample[(point+1)*4:(point+1)*4+4]=bytes((96,64,32,255))
    distances=[math.dist(sample[p*4:p*4+3],(0,255,0)) for p in range(45)]
    check(n.edge_matte(point,15,3,sample,distances,(0,255,0),True) is None,'Matte chấp nhận màu không giải thích được bằng pha khóa.')

    paint=d/'paints-012d.png'
    n.im('-size','120x100','xc:#00FF00','-fill','#13180F','-draw','rectangle 10,10 109,89',
         '-fill','#A46A30','-draw','rectangle 13,13 106,86','-fill','#5A8C3C','-draw','rectangle 14,18 18,80',
         '-fill','#C03030','-draw','rectangle 45,20 55,80','-fill','rgb(160,82,40)','-draw','rectangle 56,20 56,80',
         '-fill','#807420','-draw','rectangle 57,20 57,80',
         '-fill','rgb(10,140,8)','-draw','rectangle 9,20 9,79',paint)
    source=n.rgba(paint)[2]
    for mode in ('connected','global'):
        out=d/f'paints-{mode}-012d.png';n.key(paint,out,mode=mode)
        pixels=n.rgba(out)[2]
        # Whole interior, INCLUDING the 4–10 px inner ring and paint boundaries.
        changed=[(x,y) for y in range(14,86) for x in range(14,106)
                 if pixels[(y*120+x)*4:(y*120+x)*4+4]!=source[(y*120+x)*4:(y*120+x)*4+4]]
        check(not changed,f'Đổi sơn trong lòng/vành 4–10 px: {changed[:5]}')
        for y in range(20,80):
            for x in (10,11,12,107,108,109):
                i=(y*120+x)*4
                check(pixels[i:i+4]==source[i:i+4],'Làm sáng/hạ alpha viền sơn tối.')
        aa=pixels[(40*120+9)*4:(40*120+9)*4+4]
        check(aa[:3]==bytes((19,24,15)) and 125<=aa[3]<=130,'Sai viền tối khử răng cưa pha khóa.')
        pr=job.preserve_interior(paint,out,(0,255,0))
        check(pr['pixels']>4000 and pr['rgb_changed']==pr['alpha_changed']==0,'Sai preserve_interior.')
    damaged=bytearray(source);i=(40*120+60)*4;damaged[i]=0;damaged[i+3]=100
    n.save_rgba(120,100,damaged,d/'damaged-interior.png')
    pr=job.preserve_interior(paint,d/'damaged-interior.png',(0,255,0))
    check(pr['rgb_changed']>0 and pr['alpha_changed']>0,'preserve_interior bỏ sót thay đổi.')
    res=job.key_residue(d/'damaged-interior.png',(0,255,0))
    check(res['interior_semitransparent']>0,'key_residue bỏ alpha 9–127.')
    no_hue=d/'no-key-hue-012d.png'
    n.im(paint,'-fill','rgb(104,174,97)','-draw','rectangle 35,35 65,65',no_hue)
    n.key(no_hue,d/'no-key-hue-cut-012d.png',no_key_hue=True)
    latest=load_job('rebuild_012d.py')
    pr=latest.preserve_interior(no_hue,d/'no-key-hue-cut-012d.png',(0,255,0),True)
    residue=latest.key_residue(d/'no-key-hue-cut-012d.png',(0,255,0))
    check(residue['moderate_key_interior']==315 and residue['key_fringe']==0,
          'Bộ đếm job hiện hành bỏ sắc khóa vừa trong lòng/viền.')
    no_hue_pixels=n.rgba(d/'no-key-hue-cut-012d.png')[2]
    check(pr['allowed_hue_changes']>=961 and pr['rgb_changed']==pr['alpha_changed']==0
          and all(n.key_excess(no_hue_pixels[(y*120+x)*4:(y*120+x)*4+3],(0,255,0))[0]==0
                  for y in range(35,66) for x in range(35,66)),
          'Không kẹp/đếm đổi sắc theo job no-key-hue.')
    strong=d/'strong-paint-012d.png'
    n.im(paint,'-fill','rgb(30,110,20)','-draw','rectangle 35,35 65,65',strong)
    n.key(strong,d/'strong-cut-012d.png')
    pr=job.preserve_interior(strong,d/'strong-cut-012d.png',(0,255,0))
    check(pr['strong_key_away_from_bright']>=961 and pr['strong_key_removed']>=961,'Không đếm sơn khóa bị xóa.')
    # Thin antialiased neutral rim passes; a 10x10 pocket has exactly 64 core pixels.
    rim=d/'neutral-rim-012d.png'
    n.im('-size','64x64','xc:#604020','-fill','#E3E3E3','-draw','rectangle 10,10 49,49',
         '-fill','#E6E6E6','-draw','rectangle 11,11 48,48',rim)
    check(job.neutral_residue(rim,(224,224,224))['enclosed_neutral_ge_64_pixels']==0,'Vành mềm bị báo túi.')
    pocket=d/'neutral-core-012d.png'
    n.im('-size','64x64','xc:#604020','-fill','#E0E0E0','-draw','rectangle 2,20 11,29',pocket)
    check(job.neutral_residue(pocket,(224,224,224))['enclosed_neutral_ge_64_pixels']==64,'Túi lõi 64 px không bị bắt.')
    check(latest.neutral_residue(rim,(224,224,224))['enclosed_neutral_ge_64_pixels']==0
          and latest.neutral_residue(pocket,(224,224,224))['enclosed_neutral_ge_64_pixels']==64,
          'Chốt túi/vành mềm runner 012d lệch unit test lịch sử.')
    # Grey paint just beyond high must not connect a protected 63-pixel pocket
    # to the exterior. A +15% candidate threshold opens that corridor.
    bridge=d/'neutral-paint-bridge-012d.png'
    n.im('-size','80x80','xc:#E0E0E0','-fill','#604020','-draw','rectangle 10,10 70,70',
         '-fill','#AFAFAF','-draw','rectangle 10,20 29,20',
         '-fill','#E0E0E0','-draw','rectangle 30,20 38,26',bridge)
    n.key(bridge,d/'neutral-paint-bridge-cut-012d.png')
    check(n.rgba(d/'neutral-paint-bridge-cut-012d.png')[2][(22*80+33)*4+3]==255,
          'Nới ngưỡng ứng viên làm xuyên cầu sơn, mất túi khóa <64 px.')
    # Execute the job guards with synthetic ART/STAGE and mocked processing.
    # Reaching validation is a failure, never a nested real build. Both the
    # historical 012c runner and the current 012d runner must hold every guard.
    from contextlib import ExitStack
    import tempfile
    guards=(("interior","decal","Nội thất decal",True),("icon","icon","Nội thất icon",True),
            ("rejected","backdrop","Bản sọc",True),("backdrop","backdrop","Phông chưa đạt",False),
            ("residue","decal","Còn màu khóa",True))
    for runner in ('rebuild_012c.py','rebuild_012d.py'):
        guarded=load_job(runner)
        for guard,kind,word,seam_pass in guards:
            art=d/f'guard-art-{runner[:-3]}-{guard}';stage=d/f'guard-stage-{runner[:-3]}-{guard}';art.mkdir()
            # With records/ present and digest mocked, a removed guard runs on to
            # make_reviews and fails there by name, not on a missing output file.
            (stage/'records').mkdir(parents=True)
            fake={"size":[1024,1024],"corner_alpha":[0]*4,"margins_ltrb_alpha_gt_0":[[50]*4]*4}
            spec={"kind":kind,"input":"source.png","output":"output.png"}
            preservation={"rgb_changed":1 if guard in ("interior","icon") else 0,"alpha_changed":0}
            with ExitStack() as stack:
                for name,value in (("ART",art),("STAGE",stage)):
                    stack.enter_context(patch.object(guarded,name,value))
                for name,value in (("snapshot",{"old_records":[spec],"tool_sha256":{}}),("tool_hashes",{}),
                                   ("simple_metrics",fake),("key_residue",{"strong_key_far_from_edge":1 if guard=="residue" else 0}),
                                   ("fringe_metrics",{}),("preserve_interior",preservation),("run",{}),("digest","0"*64)):
                    stack.enter_context(patch.object(guarded,name,return_value=value))
                stack.enter_context(patch.object(guarded,'verify_originals',return_value=None))
                stack.enter_context(patch.object(n,'rgba',return_value=(64,64,bytearray([0,255,0,255]*4096))))
                # A passing report trips the rejected-012 guard; a failing one must
                # get past it and trip the backdrop pass guard on the new tile.
                stack.enter_context(patch.object(n,'reference_metrics',return_value={"x":{"pass":seam_pass}}))
                stack.enter_context(patch.object(guarded,'sidecar',return_value=None))
                stack.enter_context(patch.object(guarded,'make_reviews',side_effect=RuntimeError('Không được tới validation')))
                try:guarded.build()
                except ValueError as error:check(word in str(error),f'Sai chốt job {runner} {guard}: {error}')
                else:raise RuntimeError(f'Job {runner} bỏ chốt {guard}.')
    # A wrong-hash archive found late in phase 1 must stop both runners before a.png moves.
    for runner in ('rebuild_012c.py','rebuild_012d.py'):
        archived=load_job(runner)
        art=d/f'archive-hash-art-{runner[:-3]}';stage=d/f'archive-hash-stage-{runner[:-3]}';art.mkdir();(stage/'images').mkdir(parents=True)
        before={}
        for name in ('a.png','z.png'):
            (art/name).write_bytes(paint.read_bytes());before[name]=archived.digest(art/name)
        archived.archive_name(art/'z.png').write_bytes(b'invalid late archive')
        (stage/'images/a.png').write_bytes(rim.read_bytes())
        (stage/'manifest.json').write_text(json.dumps({'tool_sha256':{},'original_sha256':{},'historical_sha256':{},'before_sha256':before,
                                                     'artifacts_sha256':{'a.png':archived.digest(stage/'images/a.png')}}))
        with patch.object(archived,'ART',art),patch.object(archived,'STAGE',stage),patch.object(archived,'tool_hashes',return_value={}):
            try:archived.publish()
            except ValueError as error:check('hash' in str(error),f'{runner}: sai nhánh từ chối bản lưu: {error}')
            else:raise RuntimeError(f'{runner}: không chặn bản lưu sai hash.')
        check((art/'a.png').is_file() and archived.digest(art/'a.png')==before['a.png']
              and not archived.archive_name(art/'a.png').exists(),
              f'{runner}: công bố đã sửa file trước khi kiểm hết.')
    # The current runner must refuse a late dangling archive before moving a.png.
    current=load_job('rebuild_012d.py')
    art=d/'publish-012d-art';stage=d/'publish-012d-stage';art.mkdir();(stage/'images').mkdir(parents=True)
    for name in ('a.png','z.png'):(art/name).write_bytes(paint.read_bytes())
    before={name:current.digest(art/name) for name in ('a.png','z.png')}
    (art/'z.rejected-012c.png').symlink_to(d/'missing-012d.png')
    (stage/'manifest.json').write_text(json.dumps({'tool_sha256':{},'original_sha256':{},'historical_sha256':{},
                                                 'before_sha256':before,'artifacts_sha256':{}}))
    with patch.object(current,'ART',art),patch.object(current,'STAGE',stage),patch.object(current,'tool_hashes',return_value={}):
        try:current.publish()
        except ValueError as error:check('Symlink' in str(error),'Sai nhánh từ chối symlink treo.')
        else:raise RuntimeError('Pha một nhận symlink treo.')
    check(all(current.digest(art/name)==sha for name,sha in before.items()) and not (art/'a.rejected-012c.png').exists(),
          'Pha một sửa file trước khi kiểm toàn bộ tên.')
    with patch.object(n,'im',wraps=n.im) as decoder:
        n.validate_input(paint)
        check(str(decoder.call_args.args[-1]).startswith('PNG:'),'identify không khóa coder đã kiểm.')
    # Signature rejection occurs before any decoder; single frame GIF/BMP/TIFF too.
    for ext in ('gif','bmp','tiff'):
        f=d/f'signature-012d.{ext}';n.im(paint,f)
        with patch.object(n,'im',wraps=n.im) as decoder:
            try:n.validate_input(f)
            except ValueError as e:check('cấm SVG' in str(e),'Sai nhánh chữ ký.')
            else:raise RuntimeError('Nhận định dạng ngoài PNG/JPEG/WebP.')
            check(decoder.call_count==0,'Gọi decoder trước kiểm chữ ký.')
    animated=d/'animated-012d.webp';n.im(paint,rim,'-set','delay','10','-loop','0',animated)
    try:n.validate_input(animated)
    except ValueError as e:check('ảnh động' in str(e),'Không tới chốt frame.')
    else:raise RuntimeError('Nhận WebP động.')
    # Library leading-dash filename must stay an ordinary absolute PNG operand.
    dash=d/'-script';dash.write_bytes(paint.read_bytes())
    cwd=Path.cwd()
    try:
        os.chdir(d)
        for index,writer in enumerate((lambda out:n.fit('-script',out,(64,64),.08),
                                      lambda out:n.pad('-script',out,(64,64),.08,'1x1',d),
                                      lambda out:n.sheet(['-script'],out,'white',32,d))):
            writer(d/f'dash-{index}.png')
    finally:os.chdir(cwd)
    check((d/'dash-0.png').stat().st_mode & 0o777 == 0o644,'File công bố không có quyền thường 0644.')
    # A swapped PNG must still be read with its checked PNG decoder.
    swap=d/'swap-012d.png';swap.write_bytes(paint.read_bytes());n.validate_input(swap)
    swap.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="120" height="100"><rect width="120" height="100" fill="magenta"/></svg>')
    try:n.im(n.input_image(swap),'info:')
    except Exception:pass
    else:raise RuntimeError('Ảnh bị tráo thành SVG vẫn được giải mã.')
    canary=d/'decoder-canary-012d.png'
    hostile=d/'hostile-canary-012d.png'
    hostile.write_text(f'<image><read filename="xc:red"/><write filename="{canary}"/></image>')
    with patch.object(n,'im',wraps=n.im) as decoder:
        try:n.validate_input(hostile)
        except ValueError:pass
        else:raise RuntimeError('Nhận MSL giả PNG.')
        check(decoder.call_count==0 and not canary.exists(),'Canary được giải mã trước kiểm chữ ký.')
    # keep-size pins the actual Lanczos+tile pixels, not merely dimensions.
    w,h,pixels=n.rgba(d/'seam-x.png')
    expected=n.im('-size',f'{w}x{h}','-depth','8','rgba:-','-virtual-pixel','tile','-filter','Lanczos','-resize','320x288!','-depth','8','rgba:-',data=pixels)
    check(n.rgba(d/'keep-size.png')[2]==expected,'keep-size không dùng Lanczos+tile.')
    check(n.seam_metrics(*n.rgba(d/'keep-size.png'))['x']['criteria']['edge'],'keep-size làm gãy mép lặp.')
    # Width 30 is near the boundary; width 60 pins a clearly invalid compensation.
    tw,th,texture=n.rgba(d/'texture.png');compensated=bytearray(texture)
    for y in range(th):
        for c in range(3):
            delta=texture[(y*tw+tw-1)*4+c]-texture[y*tw*4+c]
            for k in range(60):
                weight=(1+math.cos(math.pi*k/60))*.25
                a,b=(y*tw+k)*4+c,(y*tw+tw-1-k)*4+c
                compensated[a]=max(0,min(255,round(texture[a]+weight*delta)))
                compensated[b]=max(0,min(255,round(texture[b]-weight*delta)))
    compensation=n.reference_metrics(tw,th,compensated,tw,th,texture)['x']
    check(not compensation['criteria']['row_streak'] and compensation['row_source_residual']>=8,
          'Bù lệch 60 px thiếu biên trượt rõ ràng.')
    # Mid-band dip leaves columns 1..13 untouched; near 0.93 must pass.
    base=n.rgba(d/'seam-x.png')[2]
    measurements=[]
    for amount,should_pass in ((.30,False),(.10,True)):
        modified=bytearray(base)
        for y in range(h):
            for x in range(15,27):
                for c in range(3):
                    i=(y*w+x)*4+c
                    modified[i]=round(128+(base[i]-128)*(1-amount))
        intrinsic=n.seam_metrics(w,h,modified)['x']
        ref=n.reference_metrics(w,h,modified,w,h,base)['x']
        measurements.append([amount,intrinsic['band_detail_ratio'],ref['band_detail_source_ratio']])
        check(intrinsic['criteria']['detail']==should_pass and ref['criteria']['detail']==should_pass,
              f'Sai ngưỡng chi tiết giữa dải: {measurements}')
    # Both edges and the inner cut, with modest 9-level one-sided streaks.
    for starts in ((0,),(w-30,),(12,)):
        modified=bytearray(base)
        for y in range(60,h,60):
            for start in starts:
                for x in range(start,start+30):
                    for c in range(3):modified[(y*w+x)*4+c]+=9
        check(not n.seam_metrics(w,h,modified)['x']['criteria']['row_streak'],'Sọc 9 một bên vẫn qua.')
        check(not n.reference_metrics(w,h,modified,w,h,base)['x']['criteria']['row_streak'],'Reference bỏ sót sọc 9.')
    for width in (5,8,12):
        fold=bytearray(base)
        for y in range(h):
            for x in range(width):
                a,b=(y*w+x)*4,(y*w+w-1-x)*4;fold[b:b+4]=fold[a:a+4]
        check(not n.seam_metrics(w,h,fold)['x']['criteria']['mirror'],'Gập gương hẹp vẫn qua.')
    partial=bytearray(base)
    for y in range(h):
        for x in range(13,45):
            a,b=(y*w+x)*4,(y*w+w-1-x)*4;partial[b:b+4]=partial[a:a+4]
    check(not n.seam_metrics(w,h,partial)['x']['criteria']['mirror'],'Gập chỉ ở dải 13–45 không bị bắt.')
    # A narrow fold with a DC colour offset passes intrinsic controls;
    # only reference_mirror may reject the additional fold.
    mirror_source=bytearray(base);mirror_after=bytearray(base)
    for y in range(h):
        for x in range(40):
            for c in range(3):
                a,b=(y*w+x)*4+c,(y*w+w-1-x)*4+c
                mirror_source[b]=base[a]+9;mirror_after[b]=base[a]+4
    reference_only=n.reference_metrics(w,h,mirror_after,w,h,mirror_source)['x']
    check(not reference_only['criteria']['reference_mirror'] and
          all(value for name,value in reference_only['criteria'].items() if name!='reference_mirror'),
          f'Fixture phải chỉ trượt reference_mirror: {reference_only["criteria"]}')
    # Analytic gradient pins controls at exactly 2k+1 columns, not 2k/2k+3.
    gradient=bytearray(v for y in range(16) for x in range(80) for v in (2*x,123,100,255))
    control=n.seam_metrics(80,16,gradient)['x']['mirror_control_mae']
    check(abs(control-14)<1e-5,'Khoảng cách cặp đối chứng không bằng 2k+1.')
    # A known zero-cost corridor pins minimum path search (including worst-cut mutants).
    corridor=bytearray([90,40,20,255]*100*24)
    for y in range(24):
        for x in range(70,100):
            corridor[(y*100+x)*4:(y*100+x)*4+4]=bytes((20,160,220,255))
        for k in range(5,26):
            corridor[(y*100+70+k)*4:(y*100+70+k)*4+4]=bytes((90,40,20,255))
    selected=n.sa.minimum_path(n.sa.rows(100,24,corridor,'x'),30)
    check(all(9<=k<=21 for k in selected),'Đường nối bỏ tìm sai số nhỏ nhất.')
    # Native low-detail columns must be compared to themselves, not scaled positions.
    rw,rh,ref=n.rgba(d/'texture.png');low_tail=bytearray(ref)
    for y in range(rh):
        for x in range(rw-60,rw):
            for c in range(3):
                i=(y*rw+x)*4+c;low_tail[i]=round(128+(ref[i]-128)*.3)
    n.save_rgba(rw,rh,low_tail,d/'low-tail-source-012d.png')
    n.seamless(d/'low-tail-source-012d.png',d/'low-tail-tile-012d.png','x',.12)
    mapped=n.reference_metrics(*n.rgba(d/'low-tail-tile-012d.png'),rw,rh,low_tail)['x']
    check(mapped['criteria']['detail'] and mapped['band_detail_ratio']<.9,'Reference không so đúng cột nguồn chi tiết thấp.')
    # Hard and maximum-error joins of a nonperiodic source must fail at the cut.
    tw,th,tex=n.rgba(d/'texture.png');band=math.ceil(tw*.12);ow=tw-band
    ramp=bytearray(tex)
    for y in range(th):
        for x in range(tw):
            for c in range(3):
                i=(y*tw+x)*4+c;ramp[i]=max(0,min(255,round(tex[i]+80*x/(tw-1)-40)))
    scores={k:sum(abs(ramp[(y*tw+ow+k)*4+c]-ramp[(y*tw+k)*4+c]) for y in range(th) for c in range(3)) for k in range(5,band-5)}
    for cut in (min(scores,key=scores.get),max(scores,key=scores.get)):
        hard=bytearray(v for y in range(th) for x in range(ow) for v in ramp[(y*tw+(ow+x if x<cut else x))*4:(y*tw+(ow+x if x<cut else x))*4+4])
        gate=n.reference_metrics(ow,th,hard,tw,th,ramp)['x']
        check(not gate['criteria']['cut_continuity'],'Cắt cứng/cột sai nhất vẫn qua.')
    # Feathered tiles built here, independently of minimum_path and overlap_pixels.
    lo,hi=5,band-5;mid=(lo+hi)//2
    def feathered(src,cuts,radius=3):
        out=bytearray(ow*th*4)
        for y in range(th):
            for x in range(ow):
                i=(y*ow+x)*4
                if x>=band:out[i:i+4]=src[(y*tw+x)*4:(y*tw+x)*4+4];continue
                t=min(1,max(0,(x-cuts[y]+radius)/(2*radius)));t=t*t*(3-2*t)
                for c in range(3):out[i+c]=round(src[(y*tw+ow+x)*4+c]*(1-t)+src[(y*tw+x)*4+c]*t)
                out[i+3]=255
        return out
    def cost(src,y,k):
        error=sum((src[(y*tw+ow+k)*4+c]-src[(y*tw+k)*4+c])**2 for c in range(3))
        a,b=max(0,k-4),min(band-1,k+4)
        return error+60*(sum(abs(src[(y*tw+ow+a)*4+c]-src[(y*tw+b)*4+c]) for c in range(3))/3)**2
    # The DP's own cost minimised per row, with no continuity, tears the tile
    # into slivers; only path_continuity sees it (B1 torn this way jumps 174 px).
    torn=[min(range(lo,hi),key=lambda k:cost(tex,y,k)) for y in range(th)]
    gate=n.reference_metrics(ow,th,feathered(tex,torn),tw,th,tex)['x']
    check(not gate['pass'] and not gate['criteria']['path_continuity'] and gate['inferred_path_max_jump']>8,
          f'Đường nối rách theo từng hàng vẫn qua: {gate["criteria"]}')
    # A smooth bright bump centred in the overlap: the DP must cut around it,
    # while a straight cut through the middle halves it and must fail.
    bump=bytearray(tex)
    for y in range(th):
        for x in range(band):
            for c in range(3):
                i=(y*tw+x)*4+c;bump[i]=min(255,round(tex[i]+80*math.exp(-((x-mid)/4.5)**2)))
    n.save_rgba(tw,th,bump,d/'bump-source-012d.png')
    n.seamless(d/'bump-source-012d.png',d/'bump-tile-012d.png','x',.12)
    gate=n.reference_metrics(*n.rgba(d/'bump-tile-012d.png'),tw,th,bump)['x']
    check(gate['pass'],f'Đường nối DP quanh vật sáng không qua chốt: {gate["criteria"]}')
    straight=n.reference_metrics(ow,th,feathered(bump,[mid]*th),tw,th,bump)['x']
    check(not straight['pass'] and not straight['criteria']['cut_continuity'],'Cắt thẳng giữa dải qua vật sáng vẫn qua.')
    # Pin the feather against the public source, independently of overlap_pixels.
    import struct
    raw=(d/'seam-x.png').read_bytes();offset=8;metadata=None
    while offset<len(raw):
        count=struct.unpack('>I',raw[offset:offset+4])[0];kind=raw[offset+4:offset+8];payload=raw[offset+8:offset+8+count]
        if kind==b'tEXt' and payload.startswith(b'art-normalize-seam\0'):
            metadata=json.loads(payload.split(b'\0',1)[1])
        offset+=12+count
    check(metadata is not None,'Không ghi đường nối trong PNG.')
    info=metadata['axes']['x'];path=info['path'];radius=info['radius']
    check(2<=radius<=4 and len(path)==th,'Sai bán kính/đường nối.')
    check(all(abs(a-b)<=4 for a,b in zip(path,path[1:])),'Đường nối DP nhảy >4 px giữa hai hàng.')
    for y in range(th):
        x=path[y]-1;t=(x-path[y]+radius)/(2*radius);t=t*t*(3-2*t)
        for c in range(3):
            expected=round(tex[(y*tw+ow+x)*4+c]*(1-t)+tex[(y*tw+x)*4+c]*t)
            check(base[(y*ow+x)*4+c]==expected,'Đường nối mất feather 2–4 px.')
    # No handlers at import, and a signal in unlink is delivered AFTER cleanup.
    import subprocess,sys
    script="""import sys,signal,os
from pathlib import Path
before=signal.getsignal(signal.SIGHUP)
sys.path.insert(0,sys.argv[1]);import normalize as n
if signal.getsignal(signal.SIGHUP)!=before:raise RuntimeError('import thay handler')
n.install_signal_handlers()
real=Path.unlink
def interrupted(path,*args,**kwargs):
    if path.name.endswith('.partial'):os.kill(os.getpid(),signal.SIGTERM)
    return real(path,*args,**kwargs)
Path.unlink=interrupted
n.publish_file(Path(sys.argv[2]),Path(sys.argv[3]))
"""
    for sig in ('SIGTERM','SIGHUP','SIGINT'):
        published=d/f'signal-unlink-{sig}-012d.png'
        child=subprocess.run([sys.executable,'-c',script.replace('signal.SIGTERM',f'signal.{sig}'),
                              str(n.ROOT),str(paint),str(published)],cwd=d,capture_output=True)
        check(child.returncode!=0 and published.read_bytes()==paint.read_bytes() and not list(d.glob('.normalize-*.partial')),
              f'{sig} lúc dọn để lại partial hoặc đích hỏng.')
    highlight=d/'highlight-012d.png';n.im('-size','64x64','xc:#E0E0E0','-fill','#604020','-draw','rectangle 10,10 53,53',
              '-fill','rgb(221,206,216)','-draw','rectangle 10,12 15,35',highlight)
    n.key(highlight,d/'highlight-cut-012d.png',fuzz=.06)
    rgb=n.rgba(d/'highlight-cut-012d.png')[2][(20*64+12)*4:(20*64+12)*4+4]
    check(rgb==bytes((221,206,216,255)),'Mất highlight có sắc độ của Tripo.')
    events=[];fsync=n.os.fsync;link=n.os.link
    def synced(fd):events.append('fsync');return fsync(fd)
    def linked(a,b):events.append('link');return link(a,b)
    with patch.object(n.os,'fsync',side_effect=synced),patch.object(n.os,'link',side_effect=linked):
        n.publish_file(paint,d/'fsync-before-link-012d.png')
    check(events==['fsync','link'],'Công bố thiếu fsync trước link.')
    print('012d: chi tiết giữa dải (mức, nội ảnh, nguồn): '+json.dumps(measurements))
    (d/'measurements-012d.json').write_text(json.dumps(measurements))
