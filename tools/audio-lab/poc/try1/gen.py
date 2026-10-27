import numpy as np, soundfile as sf, sys, os
out=sys.argv[1]; sr=48000; rng=np.random.default_rng(0)
def t(d): return np.arange(int(sr*d))/sr
def env(d,a=0.002,dec=0.25):
    x=t(d); e=np.minimum(x/a,1)*np.exp(-np.maximum(x-a,0)/dec); return e
# 1 punchy impact: low sine sweep + filtered noise crack, fast attack
d=0.8; x=t(d)
body=np.sin(2*np.pi*(120*np.exp(-x*6)+45)*x)*env(d,0.001,0.18)
from scipy.signal import butter,lfilter
b,a=butter(2,[1500/(sr/2),9000/(sr/2)],'band'); crack=lfilter(b,a,rng.standard_normal(len(x)))*env(d,0.0005,0.03)
imp=0.8*body+0.6*crack; imp/=np.abs(imp).max()*1.12; sf.write(os.path.join(out,'01_impact_good.wav'),imp,sr)
# 2 same but hard clipped +12 dB
cl=np.clip(imp*4,-1,1); sf.write(os.path.join(out,'02_impact_clipped.wav'),cl,sr)
# 3 same with 250 ms leading silence
sf.write(os.path.join(out,'03_impact_lateonset.wav'),np.concatenate([np.zeros(int(0.25*sr)),imp]),sr)
# 4 dull: low-passed at 300 Hz, slow attack
b,a=butter(4,300/(sr/2)); dull=lfilter(b,a,imp)*np.minimum(x/0.08,1); dull/=np.abs(dull).max()*1.12; sf.write(os.path.join(out,'04_impact_dull_slow.wav'),dull,sr)
# 5 pure 1 kHz beep
bp=0.5*np.sin(2*np.pi*1000*x); sf.write(os.path.join(out,'05_sine_beep.wav'),bp,sr)
# 6 white noise burst 0.8 s
sf.write(os.path.join(out,'06_white_noise.wav'),0.3*rng.standard_normal(len(x)),sr)
