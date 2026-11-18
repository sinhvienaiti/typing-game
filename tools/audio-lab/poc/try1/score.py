import sys, os, glob, time, json, numpy as np, soundfile as sf, pyloudnorm as pyln
d=sys.argv[1]; files=sorted(glob.glob(os.path.join(d,'*.wav')))
from audiobox_aesthetics.infer import initialize_predictor
t0=time.time(); p=initialize_predictor(); t1=time.time()
res=p.forward([{"path":f} for f in files]); t2=time.time()
print(f"load {t1-t0:.1f}s, score {len(files)} files {t2-t1:.2f}s")
for f,r in zip(files,res):
    y,sr=sf.read(f); m=pyln.Meter(sr,block_size=0.1)
    pk=np.abs(y).max(); rms=np.sqrt((y**2).mean())
    thr=10**(-60/20)*pk; lead=np.argmax(np.abs(y)>max(thr,1e-4))/sr*1000
    clip=int((np.abs(y)>=0.999).sum())
    print(os.path.basename(f), {k:round(v,2) for k,v in r.items()} if isinstance(r,dict) else r, f"LUFS(100ms blocks)={m.integrated_loudness(y):.1f} peak={20*np.log10(pk):.1f}dBFS crest={20*np.log10(pk/rms):.1f}dB lead={lead:.1f}ms clipped_samples={clip}")
