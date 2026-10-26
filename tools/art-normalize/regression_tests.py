#!/usr/bin/env python3
"""Ca hồi quy độc lập bộ ảnh game; chạy cả với python -O."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import math
import os
import signal
import time
import sys
from pathlib import Path
import random
import subprocess
import tempfile
from unittest.mock import patch
import normalize as n


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


def run(name, *args, ok=True):
    argv = (["python3", str(n.ROOT / "normalize.py"), name] if name == "measure" else
            ["bash", str(n.ROOT / (name + ".sh"))])
    result = subprocess.run([*argv, *map(str, args)], capture_output=True, cwd=TEST_CWD)
    check((result.returncode == 0) == ok, f"{name} {args}: {result.returncode}: {result.stderr.decode()}")
    return result


def main():
    n.WORK.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="test-", dir=n.WORK) as directory:
        d = Path(directory)
        global TEST_CWD
        TEST_CWD = d
        src = d / "source with space.png"
        n.im("-size", "160x120", "xc:#00FF00", "-fill", "#704020", "-draw", "rectangle 10,10 140,110", src)
        original = hashlib.sha256(src.read_bytes()).hexdigest()
        cut, padded = d / "cut.png", d / "pad.png"
        run("key-alpha", src, cut)
        w, h, data = n.rgba(cut)
        check((w, h) == (160, 120) and data[3] == 0 and data[(50 * w + 50) * 4 + 3] == 255, "Tách nền sai.")
        run("pad-margin", cut, padded, "--size", "128", "--margin", "8%")
        w, h, data = n.rgba(padded)
        x, y, bw, bh = n.bounds(w, h, data, cutoff=0)
        check((w, h) == (128, 128) and min(x, y, w - x - bw, h - y - bh) >= 11, "Sai khổ/lề.")
        w, h, pixels = n.rgba(src)
        pixels[3] = 254
        stray = d / "stray.png"
        n.save_rgba(w, h, pixels, stray)
        run("key-alpha", stray, d / "stray-cut.png")
        check(n.rgba(d / "stray-cut.png")[2][(20 * w + 2) * 4 + 3] == 0, "Một alpha rời rạc bỏ qua tách nền.")
        run("key-alpha", stray, d / "keep.png", "--keep-alpha")
        check(n.rgba(d / "keep.png")[2] == pixels, "--keep-alpha không giữ dữ liệu.")
        run("key-alpha", cut, d / "already.png")
        check(n.rgba(d / "already.png")[2] == n.rgba(cut)[2], "Alpha bị tách lần hai.")

        for kind,points in (("one",[10]),("corner",[0]),("four-corners",[0,w-1,(h-1)*w,w*h-1]),
                            ("below-one-percent",list(range(w+10,w+10+math.ceil(w*h*.01)-1))),
                            ("one-percent",list(range(w+10,w+10+math.ceil(w*h*.01)))),
                            ("two-percent",list(range(w+10,w+10+math.ceil(w*h*.02))))):
            aa=bytearray(n.rgba(src)[2])
            for point in points:aa[point*4+3]=0
            inp=d/f"alpha-{kind}.png";out=d/f"alpha-{kind}-cut.png"
            n.save_rgba(w,h,aa,inp);run("key-alpha",inp,out)
            oo=n.rgba(out)[2]
            check(oo==aa if kind in ("one-percent","two-percent") else oo[(20*w+2)*4+3]==0,"Ngưỡng alpha có ý nghĩa sai.")
        for bg,paint in (("#0000FF",(150,130,200)),("#00FF00",(90,140,60))):
            name="violet" if bg=="#0000FF" else "moss"
            inp=d/f"interior-{name}.png"
            n.im("-size","100x100",f"xc:{bg}","-fill","#604020","-draw","rectangle 10,10 90,90",
                 "-fill","rgb(%d,%d,%d)"%paint,"-draw","rectangle 30,30 70,70",inp)
            for mode in ("connected","global"):
                out=d/f"interior-{name}-{mode}.png";run("key-alpha",inp,out,"--mode",mode)
                check(n.rgba(out)[2][(50*100+50)*4:(50*100+50)*4+4]==bytes([*paint,255]),"Mất màu/alpha trong lòng vật.")
        for bg in ("#E0E0E0","#00FF00"):
            for area,bw,bh in ((63,9,7),(64,8,8)):
                inp=d/f"pocket-{bg[1:]}-{area}.png";out=inp.with_name(inp.stem+"-out.png")
                n.im("-size","60x60",f"xc:{bg}","-fill","#604020","-draw","rectangle 10,10 50,50",
                     "-fill",bg,"-draw",f"rectangle 20,20 {19+bw},{19+bh}",inp)
                run("key-alpha",inp,out)
                check(n.rgba(out)[2][(22*60+22)*4+3]==(0 if area==64 else 255),"Sai ngưỡng túi kín 63/64 hoặc nền bão hòa.")
        dark_key=d/"dark-key.png"
        n.im("-size","80x80","xc:#00FF00","-fill","#604020","-draw","rectangle 10,10 70,70",
             "-fill","rgb(18,102,0)","-draw","rectangle 25,25 40,40",dark_key)
        run("key-alpha",dark_key,d/"dark-key-cut.png")
        check(n.rgba(d/"dark-key-cut.png")[2][(30*80+30)*4+3]==0,"Túi khóa bão hòa tối bị coi là màu vật.")
        wrong=run("key-alpha",src,d/"wrong-bg.png","--bg","#FF0000")
        check("mảng góc" in wrong.stderr.decode(),"Không cảnh báo nền không được tách.")
        for command in ("flat-bg","icon"):
            args=["--bg","#E6E6E6","--size","128"] if command=="flat-bg" else ["--sizes","64"]
            run(command,src,d/("src-bg.png" if command=="flat-bg" else "src-bg-icons"),"--src-bg","#00FF00",*args)
        for ext,content in (("svg",b'<svg xmlns="http://www.w3.org/2000/svg"/>'),("png",b'<image><read filename="msl:x"/></image>'),("mvg",b'push graphic-context')):
            inp=d/f"script.{ext}";inp.write_bytes(content)
            check("PNG, JPEG" in run("key-alpha",inp,d/f"script-{ext}-out.png",ok=False).stderr.decode(),"Không chặn nội dung script trước decoder.")
        for writer in (lambda dst:n.key(src,dst),lambda dst:n.fit(cut,dst,(64,64),.08),
                       lambda dst:n.pad(cut,dst,(64,64),.08,"1x1",d),lambda dst:n.seamless(src,dst,"x",.12),
                       lambda dst:n.sheet([cut],dst,"white",32,d),lambda dst:n.save_rgba(*n.rgba(cut),dst)):
            for dst in (cut,d/"victim%d.png",d/"victim[0].png"):
                try:writer(dst)
                except ValueError:pass
                else:raise RuntimeError("Hàm thư viện bỏ qua chốt ghi.")

        lines = d / "lines.png"
        w, h = 80, 64
        pixels = bytearray([0, 255, 0, 255] * (w * h))
        for y in range(12, 52):
            for x, rgb in ((20, (112, 64, 32)), (21, (112, 64, 32)), (35, (112, 64, 32)),
                           (45, (96, 152, 24)), (46, (173, 69, 43))):
                pixels[(y * w + x) * 4:(y * w + x) * 4 + 4] = bytes([*rgb, 255])
        n.save_rgba(w, h, pixels, lines)
        run("key-alpha", lines, d / "lines-cut.png")
        output = n.rgba(d / "lines-cut.png")[2]
        check(all(output[(30 * w + x) * 4 + 3] == 255 for x in (20, 21, 35)), "Mất nét 1–2 px.")
        for x in (45, 46):
            i = (30 * w + x) * 4
            check(0 < output[i + 3] <= 255 and output[i + 1] <= max(output[i], output[i + 2]), "Còn xanh loang.")
        run("pad-margin", d / "lines-cut.png", d / "lines-pad.png", "--size", "73", "--margin", "8%")
        resized = n.rgba(d / "lines-pad.png")[2]
        check(all(resized[i + 1] - max(resized[i], resized[i + 2]) <= 25
                  for i in range(0, len(resized), 4) if resized[i + 3]), "Resize tái tạo màu khóa.")

        # Opaque red-dominant rim: dominance alone cannot detect the green spill.
        rim = d / "red-rim.png"
        w, h = 80, 64
        pixels = bytearray([0, 255, 0, 255] * (w * h))
        for y in range(12, 52):
            for x in range(20, 60):
                pixels[(y * w + x) * 4:(y * w + x) * 4 + 4] = bytes([192, 48, 48, 255])
            pixels[(y * w + 19) * 4:(y * w + 19) * 4 + 4] = bytes([160, 82, 40, 255])
        n.save_rgba(w, h, pixels, rim)
        run("key-alpha", rim, d / "red-rim-cut.png")
        output = n.rgba(d / "red-rim-cut.png")[2]
        rgba = output[(30 * w + 19) * 4:(30 * w + 19) * 4 + 4]
        check(all(abs(a - b) <= 2 for a, b in zip(rgba[:3], (192, 48, 48)))
              and 205 <= rgba[3] <= 220, f"Rim đỏ còn màu nền hoặc sai alpha: {list(rgba)}")

        neutral = d / "neutral.png"
        n.im("-size", "100x100", "xc:#E0E0E0", "-fill", "#604020", "-draw", "rectangle 10,10 90,90",
             "-fill", "#E0E0E0", "-draw", "rectangle 30,30 50,50", "-fill", "#EDE4D0",
             "-draw", "rectangle 65,30 80,50", neutral)
        run("key-alpha", neutral, d / "neutral-cut.png")
        output = n.rgba(d / "neutral-cut.png")[2]
        check(output[(40 * 100 + 40) * 4 + 3] == 0, "Túi nền kín còn nguyên.")
        check(output[(40 * 100 + 70) * 4 + 3] == 255, "Chi tiết kem bị xóa.")
        # A coloured fringe must not disqualify a neutral enclosed pocket.
        pocket = d / "pocket-colour-rim.png"
        n.im("-size", "120x120", "xc:#E0E0E0", "-fill", "#604020", "-draw", "rectangle 10,10 110,110",
             "-fill", "#E0DAD4", "-draw", "rectangle 35,35 65,65", "-fill", "#E0E0E0",
             "-draw", "rectangle 40,40 60,60", pocket)
        run("key-alpha", pocket, d / "pocket-colour-cut.png")
        check(n.rgba(d / "pocket-colour-cut.png")[2][(50 * 120 + 50) * 4 + 3] == 0, "Viền có màu làm bỏ qua túi nền trung tính.")
        run("flat-bg", neutral, d / "flat.png", "--bg", "#E6E6E6", "--size", "128")
        w, h, data = n.rgba(d / "flat.png")
        check(data[:4] == bytes([230, 230, 230, 255]) and data[(52 * w + 52) * 4:(52 * w + 52) * 4 + 3] == bytes([230] * 3), "Lỗ kín không đúng E6.")

        atlas = d / "atlas.png"
        n.im("(", cut, cut, "+append", ")", "(", cut, cut, "+append", ")", "-append", atlas)
        run("pad-margin", atlas, d / "atlas-out.png", "--size", "256", "--margin", "9.375%", "--grid", "2x2")
        n.im(atlas, "-set", "page", "800x800+50+50", d / "atlas-offset.png")
        run("pad-margin", d / "atlas-offset.png", d / "atlas-offset-out.png", "--size", "256",
            "--margin", "9.375%", "--grid", "2x2")
        check(n.rgba(d / "atlas-offset-out.png")[2] == n.rgba(d / "atlas-out.png")[2],
              "Page offset làm sai crop atlas 2×2.")
        crossing = d / "crossing.png"
        n.im("-size", "100x100", "xc:none", "-fill", "red", "-draw", "circle 50,50 75,50", crossing)
        run("pad-margin", crossing, d / "crossed.png", "--size", "256", "--margin", "8%", "--grid", "2x2", ok=False)
        check(not (d / "crossed.png").exists(), "Đã xuất vật bị cắt ngang ô.")
        offset = d / "offset.png"
        n.im(cut, "-set", "page", "400x400+50+50", offset)
        run("pad-margin", offset, d / "offset-out.png", "--size", "128", "--margin", "8%")
        check(n.rgba(d / "offset-out.png")[2] == n.rgba(padded)[2], "Page offset làm sai crop.")
        w, h, pixels = n.rgba(cut)
        pixels[3] = 3
        n.save_rgba(w, h, pixels, d / "speck.png")
        run("pad-margin", d / "speck.png", d / "speck-out.png", "--size", "128", "--margin", "8%")
        check(n.rgba(d / "speck-out.png")[2] == n.rgba(padded)[2], "Đốm alpha=3 làm sai trim.")

        # Asymmetric, reproducible, >=256px fixture. No mirror construction.
        rng = random.Random(12012)
        nw, nh = 320, 288
        noise = bytearray(v for _ in range(nw*nh) for v in (rng.randrange(90,166),rng.randrange(90,166),rng.randrange(90,166),255))
        n.save_rgba(nw,nh,noise,d/"noise.png")
        n.im(d/"noise.png","-blur","0x1",d/"texture.png")
        for axis in ("x","xy"):
            out=d/f"seam-{axis}.png"
            run("seamless",d/"texture.png",out,"--axis",axis)
            report=json.loads(run("seam-check",out,d/f"check-{axis}.png","--axis",axis,
                                  "--reference",d/"texture.png").stdout)
            check(report["pass"],f"Mép {axis} chưa đạt: {report}")
            ow,oh=n.dimensions(out)
            check((ow,oh)==(nw-math.ceil(nw*.12),nh-math.ceil(nh*.12) if axis=="xy" else nh),"Seamless tự co giãn.")
            check(n.dimensions(d/f"check-{axis}.png")== (ow*2,oh*2 if axis=="xy" else oh),"Sai khổ ảnh ghép.")
        run("seamless",d/"texture.png",d/"keep-size.png","--axis","x","--keep-size")
        check(n.dimensions(d/"keep-size.png")== (nw,nh),"--keep-size sai khổ.")
        ww,hh,base=n.rgba(d/"seam-x.png")
        # Blur only ONE inner part of the blend band; keep wrap and mirror healthy.
        n.im(d/"seam-x.png","-blur","0x5",d/"blurred.png")
        soft=n.rgba(d/"blurred.png")[2]
        lost=bytearray(base)
        for y in range(hh):
            for x in range(8,37):
                i=(y*ww+x)*4;lost[i:i+3]=soft[i:i+3]
        detail=n.seam_metrics(ww,hh,lost)["x"]
        check(detail["criteria"]["edge"] and detail["criteria"]["mirror"],f"Fixture chi tiết bị chốt khác bắt: {detail}")
        check(not detail["pass"] and not detail["criteria"]["detail"],"Chốt chi tiết không có tác dụng độc lập.")
        n.save_rgba(ww,hh,lost,d/"detail-lost.png")
        rr=json.loads(run("seam-check",d/"detail-lost.png",d/"detail-check.png","--axis","x","--reference",d/"texture.png").stdout)
        check(not rr["pass"],"CLI bỏ qua chi tiết --reference.")
        # Contrast loss leaves intrinsic ratios unchanged, only reference catches it.
        contrast=bytearray(base)
        for i in range(len(contrast)):
            if i%4!=3: contrast[i]=round(128+(contrast[i]-128)*.55)
        n.save_rgba(ww,hh,contrast,d/"contrast.png")
        intrinsic=n.seam_metrics(ww,hh,contrast)["x"]
        check(intrinsic["pass"],f"Fixture reference tự trượt: {intrinsic}")
        rr=json.loads(run("seam-check",d/"contrast.png",d/"contrast-check.png","--axis","x","--reference",d/"seam-x.png").stdout)
        check(not rr["pass"] and not rr["seams"]["x"]["criteria"]["reference_detail"],"--reference không bắt mất chi tiết cả ảnh.")
        folded=bytearray(base)
        for y in range(hh):
            for x in range(40):
                a,b=(y*ww+x)*4,(y*ww+ww-1-x)*4;folded[b:b+4]=folded[a:a+4]
        n.save_rgba(ww,hh,folded,d/"folded.png")
        rr=json.loads(run("seam-check",d/"folded.png",d/"fold-check.png","--axis","x").stdout)
        check(not rr["pass"] and not rr["seams"]["x"]["criteria"]["mirror"],"Gập gương >=256 không reference vẫn qua.")
        # 50% cross-fade strips and row-wise offset compensation must fail.
        cross=bytearray(base)
        for y in range(hh):
            for x in range(40):
                a,b=(y*ww+x)*4,(y*ww+ww-40+x)*4
                for c in range(3):cross[a+c]=round((base[a+c]+base[b+c])/2)
        check(not n.reference_metrics(ww,hh,cross,ww,hh,base)["x"]["pass"],"Trộn chéo 50% vẫn qua.")
        tw,th,tex=n.rgba(d/"texture.png")
        compensation=bytearray(tex)
        for y in range(th):
            for c in range(3):
                delta=tex[(y*tw+tw-1)*4+c]-tex[y*tw*4+c]
                for k in range(30):
                    f=(1+math.cos(math.pi*k/30))*.25
                    a,b=(y*tw+k)*4+c,(y*tw+tw-1-k)*4+c
                    compensation[a]=max(0,min(255,round(tex[a]+f*delta)))
                    compensation[b]=max(0,min(255,round(tex[b]-f*delta)))
        check(not n.reference_metrics(tw,th,compensation,tw,th,tex)["x"]["pass"],"Ảnh bù lệch vẫn qua.")
        # Equivalent visible row streaks, while each x edge remains seamless.
        streak=bytearray(base)
        for y in range(60,hh,60):
            for x in list(range(30))+list(range(ww-30,ww)):
                for c in range(3):streak[(y*ww+x)*4+c]=min(255,streak[(y*ww+x)*4+c]+35)
        check(not n.seam_metrics(ww,hh,streak)["x"]["criteria"]["row_streak"],"Sọc ngang không bị bắt.")
        # Source has a real non-periodic colour ramp. A correct overlap must not
        # preserve its inflated wrap difference just to satisfy --reference.
        ramp=bytearray(tex)
        for y in range(th):
            for x in range(tw):
                for c in range(3):
                    i=(y*tw+x)*4+c
                    ramp[i]=max(0,min(255,round(tex[i]+80*x/(tw-1)-40)))
        n.save_rgba(tw,th,ramp,d/"nonperiodic.png")
        run("seamless",d/"nonperiodic.png",d/"nonperiodic-tile.png","--axis","x")
        rr=json.loads(run("seam-check",d/"nonperiodic-tile.png",d/"nonperiodic-check.png",
                          "--axis","x","--reference",d/"nonperiodic.png").stdout)
        check(not rr["pass"] and rr["seams"]["x"]["reference_mirror_exempt"]
              and rr["seams"]["x"]["mirror_source_ratio"]<.5,"Reference phạt bước nhảy vốn có của nguồn.")
        for width,height in ((1,40),(40,1),(3,20)):
            tiny=d/f"tiny-{width}-{height}.png";n.im("-size",f"{width}x{height}","xc:red",tiny)
            result=run("measure",tiny,ok=False)
            check("≥4" in result.stderr.decode() and "Traceback" not in result.stderr.decode(),"Ảnh <4px lỗi không rõ.")
        for width,height in ((4,4),(5,20),(20,6),(7,4),(8,8)):
            tiny=d/f"valid-small-{width}-{height}.png"
            n.im("-size",f"{width}x{height}","xc:red",tiny)
            check(json.loads(run("measure",tiny).stdout)["size"]==[width,height],"Ảnh ≥4px rơi vào cửa sổ rỗng.")
            small=json.loads(run("seam-check",tiny,d/f"valid-small-check-{width}-{height}.png","--axis","xy").stdout)
            check(small["pass"],"Ảnh phẳng nhỏ bị chốt mép từ chối.")

        run("icon", src, d / "icons", "--sizes", "256,64")
        run("icon", src, d / "bad-icons", "--sizes", "256,4", ok=False)
        check(not (d / "bad-icons").exists(), "Bộ icon lỗi vẫn xuất một phần.")
        for bg in ("dark", "light", "white", "checker"):
            run("sheet", d / f"sheet-{bg}.png", padded, "--bg", bg, "--tile", "32")
        real_im = n.im
        real_isfile=Path.is_file
        for branch,listing in (("dejavu","Font: DejaVu-Sans"),("listed","Font: Arial"),("default","")):
            def fonts(*args,**kwargs):
                if args==("-list","font"):return listing.encode()
                # Default font may not be configured by Homebrew: observe the
                # chosen arguments, then supply installed Arial to render labels.
                if "-annotate" in args:
                    if branch=="default":
                        check("-font" not in args,"Nhánh font mặc định không được chạy.")
                        args=("-font","/System/Library/Fonts/Supplemental/Arial.ttf",*args)
                    else:
                        args=list(args); idx=args.index("-font")+1
                        check(args[idx]==("DejaVu-Sans" if branch=="dejavu" else "Arial"),"Sai font dự phòng.")
                        args[idx]="/System/Library/Fonts/Supplemental/Arial.ttf"
                return real_im(*args,**kwargs)
            with patch.object(Path,"is_file",lambda self: False if str(self)=="/System/Library/Fonts/Supplemental/Arial.ttf" else real_isfile(self)),patch.object(n,"im",side_effect=fonts):
                out=d/f"font-{branch}.png";n.sheet([padded],out,"white",32,d)
            check(out.is_file() and n.dimensions(out)==(168,70),"Sheet font thiếu hoặc sai khổ.")
        # Raise during the second fit AFTER validation and first successful fit.
        fit=n.fit; count=0
        def fail_second(*args,**kwargs):
            nonlocal count
            count+=1
            if count==2:raise ValueError("Lỗi dựng cỡ thứ hai")
            return fit(*args,**kwargs)
        with patch.object(sys,"argv",["normalize.py","icon",str(src),str(d/"mid-build"),"--sizes","256,64"]),patch.object(n,"fit",side_effect=fail_second):
            try:n.main()
            except ValueError:pass
            else:raise RuntimeError("Không chạy nhánh lỗi giữa lô icon.")
        check(count==2 and not (d/"mid-build").exists(),"Lỗi giữa lô vẫn công bố icon.")
        for suffix in ("16", "gray"):
            special = d / f"{suffix}.png"
            n.im(neutral, *(["-colorspace", "Gray"] if suffix == "gray" else []), "-depth", "16",
                 "-define", "png:bit-depth=16", special)
            check(special.read_bytes()[24] == 16, "Fixture không thật sự là PNG 16-bit.")
            run("key-alpha", special, d / f"{suffix}-out.png")
            check((d / f"{suffix}-out.png").read_bytes()[24] == 8, "Đầu ra không lượng tử hóa 8-bit như tài liệu.")
        multi = d / "multi.gif"
        n.im(src, src, multi)
        result = run("key-alpha", multi, d / "new-multi/out.png", ok=False)
        check("ảnh đơn" in result.stderr.decode() and not (d / "new-multi").exists(), "Lỗi nhiều frame không rõ.")
        run("key-alpha", d / "missing.png", d / "new-missing/out.png", ok=False)
        check(not (d / "new-missing").exists(), "Tạo thư mục trước khi kiểm file vào.")
        run("key-alpha", lines, d / "eroded.png", "--shrink", "5", ok=False)
        check(not (d / "eroded.png").exists(), "Xuất ảnh rỗng sau co mask.")
        run("key-alpha", src, src, ok=False)
        alias = d / "source-alias.png"
        alias.symlink_to(src)
        run("key-alpha", src, alias, ok=False)
        run("key-alpha", src, cut, ok=False)
        dash = d / "-source.png"
        dash.write_bytes(src.read_bytes())
        result = subprocess.run(["bash", str(n.ROOT / "key-alpha.sh"), "--", "-source.png", "dash-out.png"], cwd=d, capture_output=True)
        check(result.returncode == 0, "Dấu -- không bảo vệ tên bắt đầu bằng dấu -.")
        run("pad-margin", cut, d / "bad.png", "--size", "0", "--margin", "8%", ok=False)

        def arguments(command, input_path, destination):
            if command == "sheet":
                return [destination, input_path]
            if command == "measure":
                return [input_path]
            opts = {"pad-margin": ["--size", "128", "--margin", "8%"],
                    "flat-bg": ["--bg", "#E6E6E6", "--size", "128"],
                    "seamless": ["--axis", "x"], "seam-check": ["--axis", "x"]}.get(command, [])
            return [input_path, destination, *opts]
        for name in ("x%d.png", "x[0].png"):
            (d/name).write_bytes(src.read_bytes())
        for command in ("key-alpha", "pad-margin", "flat-bg", "seamless", "seam-check", "icon", "sheet", "measure"):
            for bad in (str(d / "x%d.png"), str(d / "x[0].png"), "png:" + str(src), "PNG32:" + str(cut)):
                if command != "measure":
                    run(command, *arguments(command, src, bad), ok=False)
                refusal = run(command, *arguments(command, bad, d / "invalid.png"), ok=False)
                check("cú pháp đặc biệt" in refusal.stderr.decode(), "Đường dẫn đầu vào chỉ trượt vì file thiếu.")
        late = d / "late.png"
        n.output_guard(late)
        late.write_bytes(b"victim")
        try:
            n.publish(cut, late)
        except (ValueError, FileExistsError):
            pass
        else:
            raise RuntimeError("Ghi đè đích xuất hiện muộn.")
        check(late.read_bytes() == b"victim", "Nạn nhân bị thay đổi.")
        race = d / "race.png"
        def competitor(_):
            return subprocess.run(["bash", str(n.ROOT / "key-alpha.sh"), str(src), str(race)], capture_output=True, cwd=TEST_CWD).returncode
        with ThreadPoolExecutor(max_workers=2) as pool:
            codes = list(pool.map(competitor, range(2)))
        check(sorted(codes) == [0, 1] and n.rgba(race)[2] == n.rgba(cut)[2], "Ghi đồng thời không độc quyền.")
        with patch.object(n, "output_guard", return_value=late):
            try:
                n.publish(cut, late)
            except FileExistsError:
                pass
            else:
                raise RuntimeError("Thiếu O_EXCL ở bước ghi cuối.")
        # A late contender specifically reaches os.link, even if guards passed.
        real_link=n.os.link;victim=d/"link-race.png"
        def race_link(partial,destination):
            Path(destination).write_bytes(b"victim")
            return real_link(partial,destination)
        with patch.object(n.os,"link",side_effect=race_link):
            try:n.publish(cut,victim)
            except FileExistsError:pass
            else:raise RuntimeError("os.link đã ghi đè đích xuất hiện muộn.")
        check(victim.read_bytes()==b"victim" and not list(d.glob(".normalize-*.partial")),"Race công bố làm đổi nạn nhân hoặc sót partial.")
        for sig in (signal.SIGTERM,signal.SIGHUP):
            ready=d/f"ready-{sig}.txt";destination=d/f"signal-{sig}.png"
            script="""import sys,time,tempfile
from pathlib import Path
sys.path.insert(0,sys.argv[1]);import normalize as n
n.install_signal_handlers()
real=n.shutil.copyfileobj
def slow(source,out):
    out.write(source.read(10));out.flush();Path(sys.argv[4]).write_text('ready');time.sleep(30)
n.shutil.copyfileobj=slow
with tempfile.TemporaryDirectory(prefix='signal-',dir=Path(sys.argv[4]).parent) as folder:
    n.publish(Path(sys.argv[2]),Path(sys.argv[3]))
"""
            child=subprocess.Popen([sys.executable,"-c",script,str(n.ROOT),str(cut),str(destination),str(ready)],cwd=d,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            deadline=time.monotonic()+10
            while not ready.exists() and child.poll() is None and time.monotonic()<deadline:time.sleep(.01)
            check(ready.exists(),"Không tới bước partial trong test tín hiệu.")
            child.send_signal(sig);child.communicate(timeout=10)
            check(not destination.exists() and not list(d.glob(".normalize-*.partial")) and not list(d.glob("signal-*/*")),"Tín hiệu để lại đích dở hoặc không dọn tạm.")
        with patch.object(n,"WORK",d/"bad%d"):
            try:n.save_rgba(*n.rgba(cut),d/"bad-work.png")
            except ValueError:pass
            else:raise RuntimeError("WORK bỏ qua chốt đường dẫn.")
        # Late invalid archive must be caught before the first valid file moves.
        import importlib.util
        job_path=n.ROOT/"jobs/dragon-hold-012/rebuild_012c.py"
        if job_path.exists():
            spec=importlib.util.spec_from_file_location("job012c",job_path);job=importlib.util.module_from_spec(spec);spec.loader.exec_module(job)
            art=d/"fake-art";stage=d/"fake-stage";art.mkdir();(stage/"images").mkdir(parents=True)
            before={}
            for name in ("a.png","z.png"):
                (art/name).write_bytes(cut.read_bytes());before[name]=job.digest(art/name)
            (art/"z.rejected-012b.png").write_bytes(b"invalid late archive")
            (stage/"images/a.png").write_bytes(padded.read_bytes())
            manifest={"tool_sha256":{},"original_sha256":{},"historical_sha256":{},"before_sha256":before,
                      "artifacts_sha256":{"a.png":job.digest(stage/"images/a.png")}}
            (stage/"manifest.json").write_text(json.dumps(manifest))
            with patch.object(job,"ART",art),patch.object(job,"STAGE",stage),patch.object(job,"tool_hashes",return_value={}):
                try:job.publish()
                except ValueError:pass
                else:raise RuntimeError("Không chặn bản lưu sai hash.")
            check(job.digest(art/"a.png")==before["a.png"] and not (art/"a.rejected-012b.png").exists(),"Công bố đã sửa file trước khi kiểm hết.")
            import fcntl
            with open(d/"private-runner.lock","a") as lock:
                fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
                for runner in ("rebuild_012b.py","rebuild_012c.py","report_012c.py","rebuild_012d.py","report_012d.py"):
                    blocked=subprocess.run([sys.executable,str(job_path.with_name(runner)),"build"],cwd=d,capture_output=True,env={**os.environ,"ART_NORMALIZE_LOCK":str(d/"private-runner.lock"),"ART_NORMALIZE_ART":str(d/"fake-art"),"ART_NORMALIZE_STAGE":str(d/"fake-stage")})
                    check(blocked.returncode!=0 and ("đồng thời" in blocked.stderr.decode() or "chưa thể" in blocked.stderr.decode()),"Runner không giữ khóa chống chạy đôi.")
        import regression_012d
        regression_012d.run(d)
        check(hashlib.sha256(src.read_bytes()).hexdigest() == original, "Ảnh nguồn bị thay đổi.")
    print("ĐẠT: đường dẫn độc hại/tạo độc quyền/đồng thời, alpha, nét mảnh, khử màu loang, túi nền kín, page offset, atlas, mép x/xy/chống gương, icon, sheet, lỗi đầu vào và hash nguồn.")


if __name__ == "__main__":
    main()
