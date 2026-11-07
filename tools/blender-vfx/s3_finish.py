"""Đóng gói riêng S3: giữ alpha thật; không sửa bộ đóng gói D1."""
import argparse, hashlib, json, subprocess
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[2]
FONT='/System/Library/Fonts/Supplemental/Arial.ttf'
def save(im,path,prompt):
    im.save(path,**({'quality':94} if path.suffix=='.jpg' else {})); path.with_suffix('.prompt.txt').write_text(prompt+'\n',encoding='utf-8')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args();out=a.out.resolve();out.relative_to(ROOT/'.local/blender-samples/s3')
    meta=json.loads((out/'render.json').read_text()); prompt=(out/'sample.prompt.txt').read_text(); files=sorted((out/'rgba').glob('*.png')); assert len(files)==meta['frames']
    ims=[Image.open(p).convert('RGBA') for p in files]; assert all(im.size==tuple(meta['resolution']) for im in ims)
    measures=[]; hashes=[]
    for p,im in zip(files,ims):
        arr=np.array(im); alpha=arr[...,3]; yy,xx=np.where(alpha>2); w,h=im.size; border=np.concatenate([alpha[0],alpha[-1],alpha[:,0],alpha[:,-1]])
        measures.append(dict(frame=int(p.stem),alpha_max=int(alpha.max()),alpha_sum=int(alpha.sum()),margin_px=int(min(xx.min(),yy.min(),w-1-xx.max(),h-1-yy.max())) if len(xx) else w//2,bbox=[int(xx.min()),int(yy.min()),int(xx.max()+1),int(yy.max()+1)] if len(xx) else None,border_alpha_max=int(border.max())))
        hashes.append(hashlib.sha256(arr.tobytes()).hexdigest());p.with_suffix('.prompt.txt').write_text(prompt,encoding='utf-8')
    for bg,suffix in [((8,11,17),'dark'),((205,204,195),'light')]:
        idx=[1,4,8,13,20,len(ims)-1] if len(ims)==32 else [3,9,16,24,34,len(ims)-1]
        idx=[min(i,len(ims)-1) for i in idx]
        sheet=Image.new('RGB',(1020,746),(30,34,42));d=ImageDraw.Draw(sheet);font=ImageFont.truetype(FONT,17)
        d.text((12,9),f'{meta["job"]} · {meta["method_short"]}',font=font,fill='white')
        for j,i in enumerate(idx):
            tile=Image.alpha_composite(Image.new('RGBA',ims[i].size,(*bg,255)),ims[i]).convert('RGB').resize((332,332),Image.Resampling.LANCZOS)
            x=4+j%3*340;y=38+j//3*354;sheet.paste(tile,(x,y));d.text((x+5,y+334),f'f{i+1:02} · {i/meta["fps"]:.3f} s',font=font,fill='white')
        save(sheet,out/f'sheet-{suffix}.jpg',prompt+f'\nTấm ghép, khung {[i+1 for i in idx]}, nền {bg}.')
    rgb=[]
    for im in ims:
        # S3-1 v2: nhân ở float để RGBA uint8 không tràn số, MP4 giữ đúng độ sáng.
        arr=np.array(im,dtype=np.float32);rgb.append(np.round(arr[...,:3]*arr[...,3:4]/255.).astype('uint8'))
    v=out/'preview-black.mp4';subprocess.run(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{ims[0].width}x{ims[0].height}','-r',str(meta['fps']),'-i','-','-an','-c:v','libx264','-crf','16','-pix_fmt','yuv420p','-movflags','+faststart',str(v)],input=b''.join(x.tobytes() for x in rgb),check=True);v.with_suffix('.prompt.txt').write_text(prompt,encoding='utf-8')
    boxes=[m['bbox'] for m in measures if m['bbox']];extent=max(max(b[2]-b[0],b[3]-b[1])/ims[0].width for b in boxes)
    val=dict(frames=measures,unique_pixel_frames=len(set(hashes)),total_frames=len(hashes),pixel_sha256=hashes,minimum_margin_px=min(m['margin_px'] for m in measures),border_alpha_max=max(m['border_alpha_max'] for m in measures),final_alpha_max=measures[-1]['alpha_max'],maximum_extent_fraction=round(extent,5),sheet_frames=[i+1 for i in idx])
    (out/'validation.json').write_text(json.dumps(val,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in val.items() if k not in ['frames','pixel_sha256']},indent=2))
if __name__=='__main__':main()
