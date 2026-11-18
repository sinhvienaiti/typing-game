import sys, os, numpy as np, librosa, librosa.display, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
files=sys.argv[2:]; out=sys.argv[1]
fig,axs=plt.subplots(3,len(files),figsize=(5*len(files),8),squeeze=False)
for j,f in enumerate(files):
    y,sr=librosa.load(f,sr=None,mono=True); t=np.arange(len(y))/sr
    axs[0][j].plot(t,y,lw=0.5); axs[0][j].axhline(0.999,color='r',lw=0.6); axs[0][j].axhline(-0.999,color='r',lw=0.6); axs[0][j].set_ylim(-1.05,1.05); axs[0][j].set_title(os.path.basename(f)+"\nwaveform (red = full scale)",fontsize=9)
    rms=librosa.feature.rms(y=y,frame_length=512,hop_length=128)[0]; db=20*np.log10(rms/ (rms.max()+1e-12)+1e-9); tt=librosa.frames_to_time(np.arange(len(db)),sr=sr,hop_length=128)
    axs[1][j].plot(tt,db); axs[1][j].axhline(-60,color='r',ls='--',lw=0.6); axs[1][j].set_ylim(-80,3); axs[1][j].set_title("envelope dB re max (dashed = -60 dB tail end)",fontsize=9)
    S=librosa.feature.melspectrogram(y=y,sr=sr,n_mels=128,fmax=sr/2,hop_length=256); librosa.display.specshow(librosa.power_to_db(S,ref=np.max),sr=sr,hop_length=256,x_axis='time',y_axis='mel',fmax=sr/2,ax=axs[2][j]); axs[2][j].axhline(8000,color='w',ls=':',lw=0.8); axs[2][j].set_title("mel spectrogram to 24 kHz (dotted = 8 kHz, audio-LLM limit)",fontsize=9)
plt.tight_layout(); plt.savefig(out,dpi=80)
