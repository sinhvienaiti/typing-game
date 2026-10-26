#!/usr/bin/env python3
"""Tạo texture tổng hợp xác định cho ví dụ xy; chỉ ghi trong WORK."""
import random
import sys
from pathlib import Path
import normalize as n

folder=n.safe_path(sys.argv[1]);folder.mkdir(parents=True,exist_ok=True)
if not folder.resolve().is_relative_to(n.WORK.resolve()):raise ValueError('Ví dụ phải nằm trong WORK.')
rng=random.Random(12012);w,h=320,288
pixels=bytearray(v for _ in range(w*h) for v in (rng.randrange(90,166),rng.randrange(90,166),rng.randrange(90,166),255))
raw=folder/'noise.png';out=folder/'ground.png'
n.save_rgba(w,h,pixels,raw)
n.output_guard(out)
n.im(n.input_image(raw),'-blur','0x1',f'PNG24:{out}')
