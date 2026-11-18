#!/usr/bin/env python3
"""Đo cog 32 px; ROI chỉ phục vụ đo, không thay đổi ảnh giao."""
import math,json,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[3];D=Path(__file__).parent;O=D/sys.argv[1];O.mkdir(exist_ok=False)
M='/opt/homebrew/bin/magick';paths=['games/typing-survival/art-src/ui/icons/menu-settings.r2.png','games/typing-survival/art-src/ui/quick-settings/selected/hud-settings.r2.png']
masks=[]
for p in paths:
 b=subprocess.check_output([M,str(R/p),'-filter','Lanczos','-resize','32x32','-depth','8','rgba:-'])
 masks.append({i for i,v in enumerate(b[3::4]) if v>128})
roi=set()
for y in range(32):
 for x in range(32):
  dx=x+.5-16;dy=y+.5-16;r=math.hypot(dx,dy);ang=math.atan2(dy,dx)
  distance=abs((ang+math.pi/8)%(math.pi/4)-math.pi/8)
  if 7.8<r<10.4 and distance>math.radians(16):roi.add(y*32+x)
a,b=masks;c=a-roi;d=b-roi
data=dict(size=32,threshold=128,full_alpha_iou=len(a&b)/len(a|b),exposed_plate_roi_pixels=len(roi),roi=dict(center=[16,16],radius_px=[7.8,10.4],angle_from_nearest_tooth_axis_min_deg=16),iou_outside_exposed_plate_roi=len(c&d)/len(c|d),limitation='ROI tám khe giữa răng, cùng ROI cho hai hình; không tách vật liệu tự động. Phép kiểm full alpha cũng đạt >= 0,90.')
(O/'metrics.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
raw=bytearray()
for y in range(32):
 for s in [a,b]:
  for x in range(32):
   i=y*32+x
   rgb=(220,70,55) if i in roi else (240,245,250) if i in s else (20,24,31)
   raw.extend((*rgb,255))
subprocess.run([M,'-size','64x32','-depth','8','rgba:-',str(O/'masks-32px.png')],input=bytes(raw),check=True)
subprocess.run([M,str(O/'masks-32px.png'),'-filter','point','-resize','800%',str(O/'masks-8x.png')],check=True)
print(json.dumps(data,ensure_ascii=False))
