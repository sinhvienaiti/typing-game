import sys, re
md, item, *parts = sys.argv[1:]
text = open(md, encoding="utf-8").read()
def code_after(marker):
    i = text.index(marker)
    j = text.index("```", i); j = text.index("\n", j) + 1
    k = text.index("```", j)
    lines = text[j:k].strip("\n").split("\n")
    if lines and re.match(r"^\[[A-Z ][^\]]*\]$", lines[0].strip()): lines = lines[1:]
    return "\n".join(lines).strip()
BG = {
 "BG-G": "Flat pure #00FF00 green background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no green at all.",
 "BG-M": "Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.",
 "BG-B": "Flat pure #0000FF blue background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no blue at all.",
}
assert BG["BG-G"] in text, "BG line drifted from the pack"
out = []
for p in parts:
    if p in BG: out.append(BG[p])
    elif p == "ITEM": out.append(code_after(item))
    elif p.startswith("TEXT:"): out.append(p[5:])
    elif p.startswith("VIEW "):
        block = text[text.index("### 3.5 Góc phụ"):]
        j = block.index("```"); j = block.index("\n", j) + 1; k = block.index("```", j)
        body = block[j:k]
        a = body.index("[" + p + "]"); b = body.find("[VIEW", a + 1)
        seg = body[a:b if b >= 0 else len(body)]
        out.append(" ".join(seg[len(p) + 2:].split()))
    else: out.append(code_after(p))
print("\n".join(out))
