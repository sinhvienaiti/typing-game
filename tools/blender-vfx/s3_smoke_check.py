"""S3-2: kiểm cỡ nguồn, alpha, video; không mở hoặc sửa host trò chơi."""
import argparse,json,subprocess
from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[2]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);args=ap.parse_args();out=args.out.resolve();out.relative_to(ROOT/'.local/blender-samples/s3')
    meta=json.loads((out/'render.json').read_text());val=json.loads((out/'validation.json').read_text());prompt=(out/'sample.prompt.txt').read_text()
    ims=[Image.open(p).convert('RGBA') for p in sorted((out/'rgba').glob('*.png'))];boxes=[m['bbox'] for m in val['frames'] if m['bbox']]
    width=max(b[2]-b[0] for b in boxes); center=(min(b[0] for b in boxes)+max(b[2] for b in boxes))/2;cy=(min(b[1] for b in boxes)+max(b[3] for b in boxes))/2
    ids=[3,9,16,24,34,len(ims)-1];body=64;sheet=Image.new('RGB',(960,738),(29,33,40));draw=ImageDraw.Draw(sheet);font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',13)
    draw.text((8,6),'S3-2 · Kiểm cỡ nguồn: thân quy ước 64 px; chưa phải ảnh trong game',font=font,fill='white')
    for row,(bg,ratio) in enumerate([((205,204,195),1.3),((205,204,195),1.6),((8,11,17),1.3),((8,11,17),1.6)]):
        scale=body*ratio/width;sz=round(ims[0].width*scale)
        for col,idx in enumerate(ids):
            im=ims[idx].resize((sz,sz),Image.Resampling.LANCZOS);tile=Image.new('RGBA',(160,144),(*bg,255));tile.alpha_composite(im,(round(80-center*scale),round(68-cy*scale)));x=col*160;y=30+row*176;sheet.paste(tile.convert('RGB'),(x,y))
            draw.line((x+48,y+136,x+112,y+136),fill=(125,125,125),width=1)
            draw.text((x+3,y+146),f'{ratio:.1f}× thân · f{idx+1:02}',font=font,fill='white')
    sheet.save(out/'sheet-body-scale.jpg',quality=94);(out/'sheet-body-scale.prompt.txt').write_text(prompt+'\nTấm kiểm nguồn: thân quy ước 64 px, chiều ngang khói cực đại 83,2/102,4 px (1,3/1,6 lần), 6 mốc trên nền sáng/tối. Đường thước 64 px chỉ để đo. Chưa xác nhận cỡ pixel trong host.\n')
    proc=subprocess.run(['ffmpeg','-v','error','-i',str(out/'preview-black.mp4'),'-f','rawvideo','-pix_fmt','rgb24','-'],check=True,stdout=subprocess.PIPE)
    decoded=np.frombuffer(proc.stdout,dtype=np.uint8).reshape((-1,ims[0].height,ims[0].width,3));assert len(decoded)==len(ims)
    errors=[]
    for im,frame in zip(ims,decoded):
        a=np.asarray(im,dtype=np.float32);expected=np.round(a[...,:3]*a[...,3:4]/255);errors.append(float(np.abs(frame.astype(np.float32)-expected).mean()))
    nonempty=[val['pixel_sha256'][i] for i,m in enumerate(val['frames']) if m['alpha_max']>0]
    check={'body_width_px_assumed':body,'effect_width_body_ratios':[1.3,1.6],'maximum_alpha_bbox_width_px':width,'nonempty_frames':len(nonempty),'unique_nonempty_frames':len(set(nonempty)),'decoded_video_frames':len(decoded),'video_mean_abs_error_255':round(float(np.mean(errors)),4),'video_duration_seconds':len(decoded)/meta['fps'],'first_alpha_max':val['frames'][0]['alpha_max'],'final_alpha_max':val['final_alpha_max'],'edge_alpha_max':val['border_alpha_max'],'minimum_margin_px':val['minimum_margin_px'],'scale_evidence':'Kiểm tương đối với thân quy ước 64 px; chưa đo bề ngang thân trong host.','internal_motion_evidence':'48 thời điểm render riêng; cần xem MP4 ở 32 fps; không nội suy hoặc lặp khung.'}
    (out/'source-check.json').write_text(json.dumps(check,indent=2,ensure_ascii=False)+'\n');print(json.dumps(check,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
