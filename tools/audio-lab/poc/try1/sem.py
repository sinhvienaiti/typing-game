import sys, os, glob, time, numpy as np, librosa, torch
from transformers import ClapModel, ClapProcessor, ASTForAudioClassification, ASTFeatureExtractor
d=sys.argv[1]; files=sorted(glob.glob(os.path.join(d,'*.wav')))
t0=time.time()
cm=ClapModel.from_pretrained("laion/larger_clap_general").eval(); cp=ClapProcessor.from_pretrained("laion/larger_clap_general")
prompts=["a punchy explosion impact","a heavy gunshot","a sharp electronic beep","static white noise hiss","a wooden bamboo knock","a distorted crackling sound"]
am=ASTForAudioClassification.from_pretrained("MIT/ast-finetuned-audioset-10-10-0.4593").eval(); af=ASTFeatureExtractor.from_pretrained("MIT/ast-finetuned-audioset-10-10-0.4593")
print(f"load {time.time()-t0:.1f}s")
with torch.no_grad():
  ti=cp(text=prompts,return_tensors="pt",padding=True); te=cm.get_text_features(**ti); te=te/te.norm(dim=-1,keepdim=True)
  for f in files:
    y48,_=librosa.load(f,sr=48000); y16,_=librosa.load(f,sr=16000)
    ai=cp(audios=[y48],sampling_rate=48000,return_tensors="pt"); ae=cm.get_audio_features(**ai); ae=ae/ae.norm(dim=-1,keepdim=True)
    sims=(ae@te.T)[0].numpy()
    top=np.argsort(-sims)[:2]
    lg=am(**af(y16,sampling_rate=16000,return_tensors="pt")).logits[0].sigmoid().numpy()
    tags=np.argsort(-lg)[:4]
    print(os.path.basename(f),"| CLAP:",", ".join(f"{prompts[i]}={sims[i]:.2f}" for i in top),"| AST:",", ".join(f"{am.config.id2label[int(i)]}={lg[i]:.2f}" for i in tags))
print(f"total {time.time()-t0:.1f}s")
