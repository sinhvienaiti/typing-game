#!/usr/bin/env python3
"""Dựng vào vùng tạm, đo, lưu bản cũ rồi công bố lô sửa 012d; có thể tiếp tục."""
import argparse
import fcntl
from collections import deque
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import math
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import normalize as n

REPO = n.ROOT.parent.parent
ART = Path(os.environ.get("ART_NORMALIZE_ART", REPO / "games/dragon-hold/art-src"))
STAGE = Path(os.environ.get("ART_NORMALIZE_STAGE", n.WORK / "dragon-hold-012d"))
META = STAGE / "snapshot.json"
JOB = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new(path, content):
    path=n.safe_path(path)
    require(not path.exists() and not path.is_symlink(),f"Từ chối ghi đè: {path}")
    n.WORK.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="job-text-",dir=n.WORK) as folder:
        staged=Path(folder)/"text.txt"
        staged.write_text(content,encoding="utf-8")
        n.publish_file(staged,path)


def json_new(path, obj):
    write_new(path, json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def archive_name(path):
    if path.name.endswith(".prompt.txt"):
        return path.with_name(path.name[:-11] + ".rejected-012c.prompt.txt")
    return path.with_name(path.stem + ".rejected-012c" + path.suffix)


def tool_hashes():
    files = []
    for folder, directories, names in os.walk(n.ROOT):
        directories[:] = [name for name in directories if name not in (".tmp", "__pycache__")]
        files.extend(Path(folder)/name for name in names if Path(name).suffix in (".py", ".sh"))
    return {str(p.relative_to(REPO)): digest(p) for p in sorted(files)}


def snapshot():
    if META.exists():
        obj=json.loads(META.read_text())
        require(obj["tool_sha256"]==tool_hashes(),"Công cụ đổi giữa lô; dùng vùng dựng mới.")
        return obj
    old=json.loads((ART/"_review/normalize-metrics.json").read_text())
    require(old.get("ticket")=="012c","012d chỉ dựng từ lô 012c đã xác nhận.")
    verification_path=ART/"_review/normalize-verification.json"
    verification=json.loads(verification_path.read_text())
    known={**old["original_sha256"],**verification["new_files_sha256"],
           "_review/normalize-verification.json":digest(verification_path)}
    for name,sha in known.items():
        path=n.safe_path(ART/name)
        require(path.resolve().is_relative_to(ART.resolve()),f"Ngoài art-src: {name}")
        require(not path.is_symlink() and path.is_file() and digest(path)==sha,f"File 012d đã đổi: {name}")
    historical={str(p.relative_to(ART)):digest(p) for p in ART.rglob("*") if p.is_file() and any(tag in p.name for tag in (".rejected-012.",".rejected-012b."))}
    obj={"ticket":"012d","tool_sha256":tool_hashes(),"original_sha256":old["original_sha256"],
         "before_sha256":known,"old_records":old["records"],"historical_sha256":historical,
         "prior_pocket_failures":[r["output"] for r in old["records"] if r["kind"]=="tripo" and not r["after"]["pocket_gate"]]}
    json_new(META,obj)
    return obj


def verify_originals(obj):
    require(all((ART / p).is_file() and digest(ART / p) == sha for p, sha in obj["original_sha256"].items()),
            "Một file gốc đã thay đổi; dừng lô.")


def run(command, *args):
    argv = ["bash", str(n.ROOT / f"{command}.sh"), *map(str, args)]
    result = subprocess.run(argv, check=True, capture_output=True, cwd=REPO)
    # Save exactly what ran as argv; the shell replay uses logical final paths.
    replay = []
    for a in argv:
        if a.startswith(str(STAGE / "images") + "/"):
            replay.append(str(ART / Path(a).relative_to(STAGE / "images").as_posix()).replace(str(REPO) + "/", ""))
        elif a.startswith(str(STAGE / "work") + "/"):
            replay.append("$WORK/" + str(Path(a).relative_to(STAGE / "work")))
        else:
            replay.append(a.replace(str(REPO) + "/", ""))
    shell = " ".join(('"' + a + '"') if a.startswith("$WORK/") else shlex.quote(a) for a in replay)
    return {"argv": argv, "replay": shell, "stdout": result.stdout.decode().strip()}


def simple_metrics(path, grid="1x1", flat=False):
    w, h, pixels = n.rgba(path)
    alpha = pixels[3::4]
    result = {"size": [w, h], "corner_alpha": [alpha[p] for p in (0, w - 1, (h - 1) * w, w * h - 1)],
              "corners": [list(c) for c in n.corners(w, h, pixels)]}
    if flat:
        pixels = bytearray(pixels)
        for i in range(0, len(pixels), 4):
            pixels[i + 3] = 0 if pixels[i:i + 3] == bytes([230] * 3) else 255
    regions = [(0, 0, w, h)] if grid == "1x1" else [
        (x * w // 2, y * h // 2, w // 2, h // 2) for y in range(2) for x in range(2)]
    result["margins_ltrb_alpha_gt_0"] = []
    for region in regions:
        x, y, bw, bh = n.bounds(w, h, pixels, region, cutoff=0)
        result["margins_ltrb_alpha_gt_0"].append([x, y, region[2] - x - bw, region[3] - y - bh])
    return result


def key_residue(path, background):
    w,h,pixels=n.rgba(path)
    alpha=pixels[3::4]
    empty=bytes(255 if a<=8 else 0 for a in alpha)
    edge=n.im("-size",f"{w}x{h}","-depth","8","gray:-","-morphology","Dilate","Diamond:4","-depth","8","gray:-",data=empty)
    strong=far=moderate=fringe=0
    bg_excess,_=n.key_excess(background,background)
    for p,a in enumerate(alpha):
        excess,_=n.key_excess(pixels[p*4:p*4+3],background)
        saturated=n.strong_key(pixels[p*4:p*4+3],background,absolute=.7) and a>8
        strong+=saturated;far+=saturated and not edge[p]
        moderate+=a>=128 and excess>40 and not edge[p]
        fringe+=9<=a<=249 and excess>25 and bool(edge[p])
    interior=n.im("-size",f"{w}x{h}","-depth","8","gray:-","-morphology","Erode","Diamond:5","-depth","8","gray:-",data=bytes(255 if a>8 else 0 for a in alpha))
    return {"moderate_key_interior":moderate,"key_fringe":fringe,"strong_key_visible":strong,"strong_key_far_from_edge":far,
            "interior_semitransparent":sum(9<=a<250 and interior[p]>0 for p,a in enumerate(alpha))}


def fringe_metrics(path):
    w,h,pixels=n.rgba(path)
    alpha=pixels[3::4]
    total=count=0
    for p,a in enumerate(alpha):
        if not 32<=a<=224:continue
        x,y=p%w,p//w
        luminance=lambda q:sum(pixels[q*4+c]*v for c,v in enumerate((.2126,.7152,.0722)))
        samples=[luminance(yy*w+xx) for yy in range(max(0,y-3),min(h,y+4))
                 for xx in range(max(0,x-3),min(w,x+4)) if alpha[yy*w+xx]==255]
        if samples and sum(samples)>0:
            total+=luminance(p)/(sum(samples)/len(samples));count+=1
    return {"fringe_pixels_compared":count,"luminance_ratio":round(total/count,6) if count else None}


def preserve_interior(source, cut, background, no_key_hue=False):
    w,h,src=n.rgba(source);cw,ch,out=n.rgba(cut)
    require((w,h)==(cw,ch),"Khổ key khác nguồn.")
    high=.12*255*math.sqrt(3)*1.5
    bg=bytes(255 if (math.dist(src[p*4:p*4+3],background)<=high or n.strong_key(src[p*4:p*4+3],background)) else 0 for p in range(w*h))
    near=n.im("-size",f"{w}x{h}","-depth","8","gray:-","-morphology","Dilate","Diamond:5","-depth","8","gray:-",data=bg)
    bright=bytes(255 if math.dist(src[p*4:p*4+3],background)<=high else 0 for p in range(w*h))
    bright_near=n.im("-size",f"{w}x{h}","-depth","8","gray:-","-morphology","Dilate","Diamond:5","-depth","8","gray:-",data=bright)
    key_count=key_removed=key_partial=0
    for p in range(w*h):
        if bright_near[p] or not n.strong_key(src[p*4:p*4+3],background):continue
        key_count+=1; key_removed+=out[p*4+3]<=8;key_partial+=9<=out[p*4+3]<=249
    count=changed=alpha_changed=allowed_hue=0
    for p in range(w*h):
        if near[p] or src[p*4+3]!=255:continue
        count+=1
        hue_change=no_key_hue and n.key_excess(src[p*4:p*4+3],background)[0]>50
        allowed_hue+=hue_change and src[p*4:p*4+3]!=out[p*4:p*4+3]
        changed+=(not hue_change) and src[p*4:p*4+3]!=out[p*4:p*4+3]
        alpha_changed+=out[p*4+3]!=255
    return {"allowed_hue_changes":allowed_hue,"strong_key_away_from_bright":key_count,"strong_key_removed":key_removed,"strong_key_partial":key_partial,"pixels":count,"rgb_changed":changed,"alpha_changed":alpha_changed,"source_sha256":digest(source),"key_sha256":digest(cut)}


def neutral_residue(path, source_background):
    w, h, pixels = n.rgba(path)
    candidate = bytearray(w * h)
    wrong = 0
    for p in range(w * h):
        rgb = pixels[p * 4:p * 4 + 3]
        candidate[p] = max(rgb) - min(rgb) <= 6 and math.dist(rgb, source_background) <= .06 * 255 * math.sqrt(3)
        wrong += candidate[p] and rgb != bytes([230] * 3)
    seen = bytearray(w * h)
    largest = total = 0
    for start in range(w * h):
        if not candidate[start] or seen[start]:
            continue
        queue = deque([start])
        seen[start] = 1
        count = 0
        wrong_count = 0
        border = False
        while queue:
            p = queue.popleft()
            count += 1
            wrong_count += (pixels[p*4:p*4+3] != bytes([230]*3) and
                            all(candidate[q] for q in n.neighbours(p,w,h)))
            border |= p < w or p >= w * (h - 1) or p % w in (0, w - 1)
            for q in n.neighbours(p, w, h):
                if candidate[q] and not seen[q]:
                    seen[q] = 1
                    queue.append(q)
        # An already-correct E6 hole is not residue. Allow only its thin AA rim:
        # at least 95% of this near-background component must be exactly E6.
        if not border and wrong_count > .05 * count:
            largest = max(largest, wrong_count)
            if wrong_count >= 64:
                total += wrong_count
    return {"near_bg_not_E6": wrong, "enclosed_neutral_largest": largest, "enclosed_neutral_ge_64_pixels": total}


def sidecar(output, source, commands, obj):
    prompt = output.with_suffix(".prompt.txt")
    text = f"Dẫn xuất Phiếu 012d từ {source or 'các ảnh trong lệnh'} bằng ImageMagick.\n"
    text += "SHA-256 công cụ normalize.py: " + obj["tool_sha256"]["tools/art-normalize/normalize.py"] + "\n"
    text += "Lệnh thực tế (argv):\n" + "\n".join(json.dumps(c["argv"], ensure_ascii=False) for c in commands)
    text += "\nLệnh tái tạo từ gốc repo (WORK là thư mục tạm mới):\n" + "\n".join(c["replay"] for c in commands) + "\n"
    original = ART / source if source else None
    if original and original.with_suffix(".prompt.txt").is_file() and not original.stem.endswith(".v1"):
        text += "\nPrompt sinh ảnh nguồn đã lưu (nguyên văn):\n" + original.with_suffix(".prompt.txt").read_text(encoding="utf-8")
    elif original:
        text += "\nPrompt chính xác của bản nguồn này chưa được lưu riêng; không dùng prompt của phiên bản khác thay thế.\n"
    else:
        text += "\nẢnh ghép để duyệt; nguồn và kích thước hiển thị ghi trong lệnh.\n"
    write_new(prompt, text)


def record_path(index):
    return STAGE / "records" / f"{index:03}.json"


def build():
    obj = snapshot()
    verify_originals(obj)
    (STAGE / "work").mkdir(exist_ok=True)
    old_records = obj["old_records"]
    tasks = []
    seen_icons = set()
    for r in old_records:
        if r["kind"] == "icon":
            if r["input"] in seen_icons:
                continue
            seen_icons.add(r["input"])
        tasks.append(r)
    for index, old in enumerate(tasks):
        require(obj["tool_sha256"]==tool_hashes(),"Công cụ đổi giữa lô; dừng trước mục kế tiếp.")
        record = record_path(index)
        if record.exists():
            continue
        kind, source = old["kind"], old["input"]
        src, dst = ART / source, STAGE / "images" / old["output"]
        dst.parent.mkdir(parents=True, exist_ok=True)
        require(not dst.exists(), f"Lần dựng trước bị ngắt giữa ảnh/biên bản: {dst}; kiểm tra vùng tạm.")
        commands = []
        outputs = [dst]
        before = simple_metrics(ART / old["output"], "2x2" if kind == "decal" else "1x1", kind == "tripo")
        if kind == "decal":
            cut = STAGE / "work" / f"decal-{index}.png"
            no_hue=any(stem in source for stem in ("dirt-patches","forest-litter"))
            commands.append(run("key-alpha", src, cut, "--mode", "global", "--fuzz", "12%", "--despill", "protect-interior", *(["--no-key-hue"] if no_hue else [])))
            commands.append(run("pad-margin", cut, dst, "--size", "1024", "--margin", "9.375%", "--grid", "2x2"))
            w, h, pixels = n.rgba(src)
            background = n.background_color(w, h, pixels)
            before["residue"] = key_residue(ART / old["output"], background)
            before["fringe"]=fringe_metrics(ART/old["output"])
            preservation=preserve_interior(src,cut,background,no_hue)
            require(preservation["rgb_changed"]==preservation["alpha_changed"]==0,"Nội thất decal bị đổi màu/alpha.")
        elif kind == "backdrop":
            commands.append(run("seamless", src, dst, "--axis", "x", "--blend", "12%"))
            before["seams"] = n.reference_metrics(*n.rgba(ART/old["output"]),*n.rgba(src))
            rejected=n.reference_metrics(*n.rgba(ART/"backdrops/pine-river-far.seamless.rejected-012.png"),*n.rgba(src))["x"]
            require(not rejected["pass"],"Bản sọc 012 lọt chốt.")
        elif kind == "icon":
            cut=STAGE/"work"/f"icon-{index}.png"
            commands.append(run("key-alpha",src,cut,"--despill","protect-interior"))
            for sz in (256,64):
                commands.append(run("pad-margin",cut,dst.parent/f"{src.stem}.{sz}.png","--size",str(sz),"--margin","8%"))
            background=n.background_color(*n.rgba(src))
            preservation=preserve_interior(src,cut,background)
            require(preservation["rgb_changed"]==preservation["alpha_changed"]==0,"Nội thất icon bị đổi màu/alpha.")
            outputs = [dst.parent / f"{src.stem}.{s}.png" for s in (256, 64)]
        elif kind == "tripo":
            # Canvas aspect follows subject; nearest standard canvas in the 012 table.
            cut=STAGE/"work"/f"tripo-{index}.png"
            commands.append(run("key-alpha",src,cut,"--fuzz","6%","--despill","protect-interior"))
            bw,bh=n.bounds(*n.rgba(cut))[2:]
            canvases=sorted({n.size(r["requested_size"]) for r in old_records if r["kind"]=="tripo"})
            target=min(canvases,key=lambda t:abs(math.log((t[0]/t[1])/(bw/bh))))
            requested=f"{target[0]}x{target[1]}"
            commands.append(run("flat-bg",cut,dst,"--keep-alpha","--bg","#E6E6E6","--size",requested))
            w, h, pixels = n.rgba(src)
            background = n.background_color(w, h, pixels)
            cut_pixels=n.rgba(cut)[2]
            colored_highlights=[p for p in range(w*h)
                if max(pixels[p*4:p*4+3])-min(pixels[p*4:p*4+3])>8
                and math.dist(pixels[p*4:p*4+3],background)<=.06*255*math.sqrt(3)]
            highlight_check={"near_bg_colored_source":len(colored_highlights),
                             "removed_at_key":sum(cut_pixels[p*4+3]<=8 for p in colored_highlights)}
            before["residue"] = neutral_residue(ART / old["output"], background)
        records = []
        for out in outputs:
            relative = str(out.relative_to(STAGE / "images"))
            if kind == "icon":
                before = simple_metrics(ART / relative)
            after = simple_metrics(out, "2x2" if kind == "decal" else "1x1", kind == "tripo")
            if kind == "decal":
                after["residue"] = key_residue(out, background)
                after["fringe"]=fringe_metrics(out)
                after["interior_preservation"]=preservation
                require(after["residue"]["strong_key_far_from_edge"] == 0, f"Còn màu khóa: {out}: {after}")
                require(min(min(m) for m in after["margins_ltrb_alpha_gt_0"]) >= 48, f"Lề decal chưa đạt: {out}")
            elif kind == "tripo":
                after["residue"] = neutral_residue(out, background)
                after["highlight_check"]=highlight_check
                for measured in (before, after):
                    left,top,right,bottom=measured["margins_ltrb_alpha_gt_0"][0]
                    measured["subject_scale"]=round(min((measured["size"][0]-left-right)/bw,
                                                       (measured["size"][1]-top-bottom)/bh),6)
                after["source_subject_size"]=[bw,bh]
                after["pocket_gate"] = after["residue"]["enclosed_neutral_ge_64_pixels"] == 0
                require(after["corners"] == [[230] * 3] * 4, f"Sai màu góc: {out}")
                require(all(v >= math.ceil(after["size"][i % 2] * .08)
                            for i, v in enumerate(after["margins_ltrb_alpha_gt_0"][0])), f"Sai lề Tripo: {out}")
            elif kind == "backdrop":
                after["seams"] = n.reference_metrics(*n.rgba(out),*n.rgba(src))
                require(after["seams"]["x"]["pass"], "Phông chưa đạt chốt mép/gương.")
            elif kind == "icon":
                after["interior_preservation"]=preservation
                require(after["corner_alpha"] == [0] * 4, f"Icon chưa có alpha: {out}")
                minimum = 23 if after["size"][0] == 256 else 8
                require(min(after["margins_ltrb_alpha_gt_0"][0]) >= minimum, f"Sai lề icon: {out}")
            sidecar(out, source, commands, obj)
            records.append({"kind": kind, "input": source, "output": relative, "commands": commands,
                            "evidence": {"backdrop_012d":before["seams"]["x"],"backdrop_rejected_012":rejected} if kind=="backdrop" else {},
                            "before": before, "after": after, "requested_size": requested if kind=="tripo" else old.get("requested_size"), "sha256": digest(out)})
        json_new(record, records)
        print(f"{index + 1}/{len(tasks)} {kind}: {source}", flush=True)
    all_records = [r for p in sorted((STAGE / "records").glob("*.json")) for r in json.loads(p.read_text(encoding="utf-8"))]
    require(len(all_records) == len(obj["old_records"]), "Số bản xử lý khác danh sách 012.")
    make_reviews(all_records, obj)
    validation={}
    for script in (n.ROOT/"test.sh",JOB/"verify-code.sh"):
        result=subprocess.run(["bash",str(script)],cwd=REPO,capture_output=True,text=True)
        validation[script.name]={"exit_code":result.returncode,"stdout":result.stdout.strip(),"stderr":result.stderr.strip(),"sha256":digest(script)}
        require(result.returncode==0,f"Kiểm tra không đạt: {script}: {result.stderr}")
    if not (STAGE / "manifest.json").exists():
        json_new(STAGE / "manifest.json", {**obj, "records": all_records,
                 "artifacts_sha256": {str(p.relative_to(STAGE / "images")): digest(p)
                                      for p in (STAGE / "images").rglob("*") if p.is_file()},
                 "validation":validation,"evidence":next(r["evidence"] for r in all_records if r["kind"]=="backdrop")})
    verify_originals(obj)
    print("Đã dựng và đo đủ lô; xem ảnh trong .tmp/dragon-hold-012d/images trước bước publish.", flush=True)


def make_reviews(records, obj):
    specs = []
    for archive in (False, True):
        decals = [r["output"] for r in records if r["kind"] == "decal" and (".v1." in r["input"]) == archive]
        for bg in ("dark", "white", "checker"):
            specs.append((f"decals-{'archive-' if archive else ''}012d.{bg}.png", decals, bg, 1024))
    icons = [r["output"] for r in records if r["kind"] == "icon"]
    for tile in (256, 64, 32):
        for bg in ("dark", "light", "checker"):
            files = [p for p in icons if p.endswith(f".{256 if tile == 256 else 64}.png")]
            specs.append((f"icons-{tile}.{bg}.png", files, bg, tile))
    for group in ("enemies", "generals", "units", "houses", "traps", "props"):
        files = [r["output"] for r in records if r["kind"] == "tripo" and r["input"].startswith(group + "/")]
        specs.append((f"tripo-{group}.output.png", files, "light", 256))
    for name, files, bg, tile in specs:
        dst = STAGE / "images/_review" / name
        if dst.with_suffix(".prompt.txt").exists():
            continue
        command = run("sheet", dst, *[STAGE / "images" / p for p in files], "--bg", bg, "--tile", tile)
        sidecar(dst, None, [command], obj)
        print("Sheet:", name, flush=True)
    for phase in ("before", "after"):
        dst = STAGE / "images/_review" / ("pine-river-far.before.seam.png" if phase == "before" else "pine-river-far.seam.png")
        if dst.with_suffix(".prompt.txt").exists():
            continue
        src = ART / "backdrops/pine-river-far.png" if phase == "before" else STAGE / "images/backdrops/pine-river-far.seamless.png"
        commands = [run("seam-check", src, dst, "--axis", "x", "--reference", ART / "backdrops/pine-river-far.png")]
        sidecar(dst, None, commands, obj)

    for phase in ("before", "after"):
        dst=STAGE/"images/_review"/f"b1-cut-{phase}-012d.png"
        if dst.with_suffix(".prompt.txt").exists():continue
        src=ART/"backdrops/pine-river-far.seamless.png" if phase=="before" else STAGE/"images/backdrops/pine-river-far.seamless.png"
        width=n.dimensions(src)[0]
        argv=[n.input_image(src),n.input_image(src),"+append","-crop",f"255x600+{width-30}+0","+repage","-strip",f"PNG24:{dst}"]
        n.im(*argv)
        sidecar(dst,None,[{"argv":[n.MAGICK,*map(str,argv)],"replay":"ImageMagick: "+" ".join(shlex.quote(str(a)) for a in argv)}],obj)


def publish():
    manifest = json.loads((STAGE / "manifest.json").read_text(encoding="utf-8"))
    require(manifest["tool_sha256"] == tool_hashes(), "Công cụ đổi sau khi dựng.")
    verify_originals(manifest)
    require(all(digest(ART/p)==sha for p,sha in manifest["historical_sha256"].items()),"Lịch sử 012 đã đổi.")
    for name, sha in manifest["artifacts_sha256"].items():
        require(digest(STAGE / "images" / name) == sha, f"File dựng đã đổi: {name}")
    old_derived = {p: sha for p, sha in manifest["before_sha256"].items() if p not in manifest["original_sha256"]}
    # Phase 1: validate the complete set before any archive/unlink.
    for name, sha in old_derived.items():
        path, archive = ART / name, archive_name(ART / name)
        require(not path.is_symlink() and not archive.is_symlink(), f"Symlink trong pha kiểm: {name}")
        require(path.resolve().is_relative_to(ART.resolve()) and archive.resolve().is_relative_to(ART.resolve()), f"Ngoài art-src: {name}")
        if archive.exists():
            require(digest(archive) == sha, f"Bản lưu không đúng hash: {archive}")
        else:
            require(path.is_file() and digest(path) == sha, f"Bản cũ đã đổi: {name}")
        if path.exists():
            require(digest(path) in (sha, manifest["artifacts_sha256"].get(name)), f"Đích đã đổi: {name}")
    for name, sha in manifest["artifacts_sha256"].items():
        path = ART / name
        require(not path.is_symlink(), f"Đích là symlink: {name}")
        if path.exists():
            require(digest(path) in (sha, old_derived.get(name)), f"Đích không thuộc lô: {name}")
    # Phase 2: archive validated derivatives, then publish.
    for name, sha in old_derived.items():
        path = ART / name
        archive = archive_name(path)
        if archive.exists():
            require(digest(archive) == sha, f"Bản lưu không đúng hash: {archive}")
        else:
            require(path.is_file() and digest(path) == sha, f"Bản 012 đã đổi trước khi lưu: {name}")
            n.publish_file(path, archive)
            require(digest(archive) == sha, f"Bản lưu không nguyên vẹn: {archive}")
        # Resume safely if interrupted after the archive copy, before unlinking.
        if path.exists():
            current = digest(path)
            if current == sha:
                path.unlink()
            else:
                require(current == manifest["artifacts_sha256"].get(name),
                        f"File đã đổi sau khi lưu bản 012: {name}")
    for name, sha in manifest["artifacts_sha256"].items():
        destination = ART / name
        if destination.exists():
            require(digest(destination) == sha, f"File đích khác lô 012d: {destination}")
            continue
        if destination.suffix == ".png":
            n.publish(STAGE / "images" / name, destination)
        else:
            n.publish_file(STAGE / "images" / name, destination)
    out = ART / "_review/normalize-metrics.json"
    if not out.exists():
        json_new(out, {**manifest, "archived_012c": {p: str(archive_name(ART / p).relative_to(ART)) for p in old_derived},
                      "old_records_note": "Hồ sơ 012 dùng thuật toán đã loại; xem các JSON .rejected-012, không tái tạo bằng mã 012d."})
    verify_originals(manifest)
    print(f"Đã công bố {len(manifest['records'])} bản xử lý; lưu {len(old_derived)} file dẫn xuất cũ; giữ {len(manifest['original_sha256'])} file gốc.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["build", "build-parallel", "publish"])
    args = parser.parse_args()
    n.WORK.mkdir(exist_ok=True)
    n.install_signal_handlers()
    lock = open(os.environ.get("ART_NORMALIZE_LOCK", n.WORK / "dragon-hold-publish.lock"), "a")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        raise SystemExit("Một runner Rồng đang chạy; từ chối chạy đồng thời.")

    if args.action in ("build", "build-parallel"):
        build()
    else:
        publish()
