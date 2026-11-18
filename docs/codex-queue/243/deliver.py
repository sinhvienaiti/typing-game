#!/usr/bin/env python3
"""Giao bản chọn, từ chối ghi đè bất kỳ file nào."""
import json, shutil
from pathlib import Path
R=Path(__file__).resolve().parents[3];D=Path(__file__).parent;C=D/'candidates-final'
A=json.loads((D/'assets-check.json').read_text());M=json.loads((C/'metrics.json').read_text());made=[]
for a in A:
 base=Path(a['final']).name
 prompt=(R/M[a['name']]['source']).with_suffix('.prompt.txt').read_bytes()
 for size in [1024,256,128,64]:
  src=C/(base+('.clean' if size==1024 else '.'+str(size))+'.png')
  dst=R/(a['final']+('' if size==1024 else '.'+str(size))+'.png')
  pp=dst.with_suffix('.prompt.txt')
  assert not dst.exists() and not pp.exists(),dst
  with dst.open('xb') as w:w.write(src.read_bytes())
  with pp.open('xb') as w:w.write(prompt)
  made.append(str(dst.relative_to(R)))
with (D/'delivered.json').open('x') as w:json.dump(made,w,ensure_ascii=False,indent=2);w.write('\n')
print(len(made),'PNG; exact generation prompts beside every delivered PNG')
