# Automatic checks for one 1080x1080 first or end frame (ticket 270). numpy + ImageMagick 7 only.
# Run: /Applications/Blender.app/Contents/Resources/5.2/python/bin/python3.13 -I docs/codex-queue/270/auto.py <img.png>
# Prints JSON: size, corner black (max of the four 32x32 corners, 0-255), bbox of luma > 8/255 (parts >= 0.05 % of lit),
# margin ok (bbox inside 87..992), lit share (luma > 0.10), hot share of lit (luma >= 0.85; target 0.02-0.06).
import sys, json, subprocess
import numpy as np
p = sys.argv[1]
w, h = map(int, subprocess.check_output(['magick', 'identify', '-format', '%w %h', p + '[0]']).split())
a = np.frombuffer(subprocess.check_output(['magick', p + '[0]', '-depth', '8', 'rgba:-']), np.uint8).reshape(h, w, 4)[..., :3].astype(float)
Y = (a / 255.0) @ np.array([0.2126, 0.7152, 0.0722])
lit = Y > 0.10; hot = Y >= 0.85; n = int(lit.sum())
corner = float(max(a[:32, :32].max(), a[:32, -32:].max(), a[-32:, :32].max(), a[-32:, -32:].max()))
m8 = (Y > 8 / 255).astype(np.uint8) * 255
out = subprocess.run(['magick', '-size', f'{w}x{h}', '-depth', '8', 'gray:-', '-define', 'connected-components:verbose=true',
                      '-connected-components', '8', 'null:'], input=m8.tobytes(), capture_output=True).stdout.decode()
x0 = y0 = 10 ** 9; x1 = y1 = -1
for line in out.splitlines()[1:]:
    parts = line.split()
    if len(parts) < 5 or not (parts[-1].startswith('gray(255') or parts[-1].startswith('srgb(255') or parts[-1] == 'white'):
        continue
    geo, area = parts[1], int(parts[3])
    if area < 0.0005 * max(n, 1):
        continue
    gw, rest = geo.split('x'); gh, gx, gy = rest.split('+'); gw, gh, gx, gy = int(gw), int(gh), int(gx), int(gy)
    x0, y0, x1, y1 = min(x0, gx), min(y0, gy), max(x1, gx + gw - 1), max(y1, gy + gh - 1)
res = dict(image=p, size=[w, h], corner_black_max=corner, lit_share=round(n / (w * h), 4),
           hot_share_of_lit=round(float(hot.sum()) / max(n, 1), 4), bbox=[x0, y0, x1, y1],
           margin_ok=bool(x0 >= 87 and y0 >= 87 and x1 <= 992 and y1 <= 992))
res['pass'] = dict(size=(w, h) == (1080, 1080), black=corner <= 8, margin=res['margin_ok'], hot=0.02 <= res['hot_share_of_lit'] <= 0.06)
print(json.dumps(res))
