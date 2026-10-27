#!/usr/bin/env python3
"""Dựng crop các túi nền lớn trong nhóm từng bị gắn cờ 012b; chỉ ghi WORK mới."""
from collections import deque
import json
import tempfile
from pathlib import Path
from rebuild_012c import ART, STAGE, n


def main():
    obj=json.loads((STAGE/"manifest.json").read_text())
    outdir=Path(tempfile.mkdtemp(prefix="pocket-inspect-012c-",dir=n.WORK))
    selected=set(obj["prior_pocket_failures"])
    for record in obj["records"]:
        if record["kind"]!="tripo" or record["output"] not in selected:continue
        source=STAGE/"images"/record["output"]
        w,h,pixels=n.rgba(source)
        bg=n.background_color(*n.rgba(ART/record["input"]))
        import math
        candidate=bytearray(max(pixels[p*4:p*4+3])-min(pixels[p*4:p*4+3])<=6 and
                            math.dist(pixels[p*4:p*4+3],bg)<=.06*255*math.sqrt(3) for p in range(w*h))
        seen=bytearray(w*h);parts=[]
        for start in range(w*h):
            if not candidate[start] or seen[start]:continue
            queue=deque([start]);seen[start]=1;component=[];border=False
            while queue:
                p=queue.popleft();component.append(p);x,y=p%w,p//w
                border|=x in (0,w-1) or y in (0,h-1)
                for q in n.neighbours(p,w,h):
                    if candidate[q] and not seen[q]:seen[q]=1;queue.append(q)
            if not border and len(component)>=64:parts.append(component)
        for index,part in enumerate(sorted(parts,key=len,reverse=True)[:2]):
            x,y=max(0,min(p%w for p in part)-20),max(0,min(p//w for p in part)-20)
            right,bottom=min(w,max(p%w for p in part)+21),min(h,max(p//w for p in part)+21)
            crop=outdir/f"{source.stem}.{index}.png"
            n.output_guard(crop)
            with tempfile.TemporaryDirectory(prefix="inspect-",dir=n.WORK) as folder:
                staged=Path(folder)/"crop.png"
                n.im(source,"+repage","-crop",f"{right-x}x{bottom-y}+{x}+{y}","+repage","-filter","Point","-resize","200%",staged)
                n.publish(staged,crop)
            crop.with_suffix(".prompt.txt").write_text(f"Crop dẫn xuất 012c để kiểm túi nền; nguồn {record['output']}; vùng {right-x}x{bottom-y}+{x}+{y}; Point 200%.\n")
        print(record["output"],record["after"]["residue"],flush=True)
    print("Crop kiểm tra:",outdir)


if __name__=="__main__":main()
