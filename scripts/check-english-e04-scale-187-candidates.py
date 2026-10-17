#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
source=(ROOT/'scripts/check-english-e04-scale-186-candidates.py').read_text(encoding='utf-8').replace('scale-186','scale-187').replace('scale186','scale187')
exec(compile(source,str(Path(__file__)),'exec'),{'__name__':'__main__','__file__':__file__})
