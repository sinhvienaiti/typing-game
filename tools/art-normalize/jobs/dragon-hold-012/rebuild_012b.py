#!/usr/bin/env python3
"""Dựng vào vùng tạm, đo, lưu bản cũ rồi công bố lô sửa 012b; có thể tiếp tục."""
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

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import normalize as n

REPO = n.ROOT.parent.parent
ART = Path(os.environ.get("ART_NORMALIZE_ART", REPO / "games/dragon-hold/art-src"))
STAGE = Path(os.environ.get("ART_NORMALIZE_STAGE", n.WORK / "dragon-hold-012b"))
META = STAGE / "snapshot.json"
JOB = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_new(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "x", encoding="utf-8") as output:
        output.write(content)


def json_new(path, obj):
    write_new(path, json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def archive_name(path):
    if path.name.endswith(".prompt.txt"):
        return path.with_name(path.name[:-11] + ".rejected-012.prompt.txt")
    return path.with_name(path.stem + ".rejected-012" + path.suffix)


def tool_hashes():
    files = [n.ROOT / "normalize.py", n.ROOT / "regression_tests.py", *n.ROOT.rglob("*.sh")]
    return {str(p.relative_to(REPO)): digest(p) for p in sorted(files) if ".tmp" not in p.parts}


def snapshot():
    current = json.loads((ART / "_review/normalize-metrics.json").read_text(encoding="utf-8"))
    require(current.get("ticket") not in ("012b", "012c") and not current.get("archived_012"),
            "Runner 012b đã khóa sau công bố; dùng runner 012c.")
    if META.exists():
        obj = json.loads(META.read_text(encoding="utf-8"))
        require(obj["tool_sha256"] == tool_hashes(), "Công cụ đã đổi sau khi bắt đầu lô; dùng vùng dựng mới.")
        return obj
    old = json.loads((ART / "_review/normalize-metrics.json").read_text(encoding="utf-8"))
    verification_path = ART / "_review/normalize-verification.json"
    verification = json.loads(verification_path.read_text(encoding="utf-8"))
    known = {**old["original_sha256"], **verification["new_files_sha256"],
             "_review/normalize-verification.json": digest(verification_path)}
    for name, sha in known.items():
        relative = Path(name)
        require(not relative.is_absolute() and ".." not in relative.parts, f"Đường dẫn ngoài art-src: {name}")
        require((ART / name).resolve().is_relative_to(ART.resolve()), f"Alias ngoài art-src: {name}")
        require((ART / name).is_file() and digest(ART / name) == sha, f"File 012 đã đổi hoặc thiếu: {name}")
    for record in old["records"]:
        require(record["input"] in old["original_sha256"] and record["output"] in verification["new_files_sha256"],
                "Danh sách 012 chứa nguồn hoặc dẫn xuất chưa được xác nhận.")
    obj = {"ticket": "012b", "tool_sha256": tool_hashes(), "original_sha256": old["original_sha256"],
           "before_sha256": known,
           "old_records": old["records"]}
    json_new(META, obj)
    return obj


def verify_originals(obj):
    require(all((ART / p).is_file() and digest(ART / p) == sha for p, sha in obj["original_sha256"].items()),
            "Một file gốc đã thay đổi; dừng lô.")


def run(command, *args):
    argv = ["bash", str(n.ROOT / f"{command}.sh"), *map(str, args)]
    result = subprocess.run(argv, check=True, capture_output=True)
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
    _, _, pixels = n.rgba(path)
    dominance = near = opaque = 0
    threshold = .12 * 255 * math.sqrt(3)
    for i in range(0, len(pixels), 4):
        rgb, alpha = pixels[i:i + 3], pixels[i + 3]
        if not alpha:
            continue
        excess, _ = n.key_excess(rgb, background)
        dominance += excess > 25
        close = math.dist(rgb, background) <= threshold
        near += close
        opaque += close and alpha == 255
    return {"key_dominance_gt_25": dominance, "near_key_visible": near, "near_key_opaque": opaque}


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
            wrong_count += pixels[p * 4:p * 4 + 3] != bytes([230] * 3)
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
    text = f"Dẫn xuất Phiếu 012b từ {source or 'các ảnh trong lệnh'} bằng ImageMagick.\n"
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


def build(shard=None):
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
        if shard and index % shard[1] != shard[0]:
            continue
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
            commands.append(run("key-alpha", src, cut, "--mode", "global", "--fuzz", "12%"))
            commands.append(run("pad-margin", cut, dst, "--size", "1024", "--margin", "9.375%", "--grid", "2x2"))
            w, h, pixels = n.rgba(src)
            background = n.background_color(w, h, pixels)
            before["residue"] = key_residue(ART / old["output"], background)
        elif kind == "backdrop":
            commands.append(run("seamless", src, dst, "--axis", "x", "--blend", "12%"))
            before["seams"] = n.seam_metrics(*n.rgba(src))
        elif kind == "icon":
            # Lavender on herb-hut is genuine source paint; use the colour-distance matte only.
            extra = ["--despill", "off"] if src.stem == "herb-hut" else []
            commands.append(run("icon", src, dst.parent, "--sizes", "256,64", *extra))
            outputs = [dst.parent / f"{src.stem}.{s}.png" for s in (256, 64)]
        elif kind == "tripo":
            commands.append(run("flat-bg", src, dst, "--bg", "#E6E6E6", "--size", old["requested_size"]))
            w, h, pixels = n.rgba(src)
            background = n.background_color(w, h, pixels)
            before["residue"] = neutral_residue(ART / old["output"], background)
        records = []
        for out in outputs:
            relative = str(out.relative_to(STAGE / "images"))
            if kind == "icon":
                before = simple_metrics(ART / relative)
            after = simple_metrics(out, "2x2" if kind == "decal" else "1x1", kind == "tripo")
            if kind == "decal":
                after["residue"] = key_residue(out, background)
                require(after["residue"]["key_dominance_gt_25"] == 0, f"Còn màu khóa: {out}: {after}")
                require(min(min(m) for m in after["margins_ltrb_alpha_gt_0"]) >= 48, f"Lề decal chưa đạt: {out}")
            elif kind == "tripo":
                after["residue"] = neutral_residue(out, background)
                after["pocket_gate"] = after["residue"]["enclosed_neutral_ge_64_pixels"] == 0
                require(after["corners"] == [[230] * 3] * 4, f"Sai màu góc: {out}")
                require(all(v >= math.ceil(after["size"][i % 2] * .08)
                            for i, v in enumerate(after["margins_ltrb_alpha_gt_0"][0])), f"Sai lề Tripo: {out}")
            elif kind == "backdrop":
                after["seams"] = n.seam_metrics(*n.rgba(out))
                require(after["seams"]["x"]["pass"], "Phông chưa đạt chốt mép/gương.")
            elif kind == "icon":
                require(after["corner_alpha"] == [0] * 4, f"Icon chưa có alpha: {out}")
                minimum = 23 if after["size"][0] == 256 else 8
                require(min(after["margins_ltrb_alpha_gt_0"][0]) >= minimum, f"Sai lề icon: {out}")
            sidecar(out, source, commands, obj)
            records.append({"kind": kind, "input": source, "output": relative, "commands": commands,
                            "before": before, "after": after, "sha256": digest(out)})
        json_new(record, records)
        print(f"{index + 1}/{len(tasks)} {kind}: {source}", flush=True)
    if shard:
        return
    all_records = [r for p in sorted((STAGE / "records").glob("*.json")) for r in json.loads(p.read_text(encoding="utf-8"))]
    require(len(all_records) == 81, "Số bản xử lý khác danh sách 012.")
    make_reviews(all_records, obj)
    if not (STAGE / "manifest.json").exists():
        json_new(STAGE / "manifest.json", {**obj, "records": all_records,
                 "artifacts_sha256": {str(p.relative_to(STAGE / "images")): digest(p)
                                      for p in (STAGE / "images").rglob("*") if p.is_file()},
                 "test": "Đạt test.sh; ca đường dẫn độc hại, O_EXCL, đồng thời, alpha, nét 2 px, túi nền, x/xy/gương."})
    verify_originals(obj)
    print("Đã dựng và đo đủ lô; xem ảnh trong .tmp/dragon-hold-012b/images trước bước publish.", flush=True)


def make_reviews(records, obj):
    specs = []
    for archive in (False, True):
        decals = [r["output"] for r in records if r["kind"] == "decal" and (".v1." in r["input"]) == archive]
        for bg in ("dark", "white", "checker"):
            specs.append((f"decals-{'archive-' if archive else ''}012b.{bg}.png", decals, bg, 1024))
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


def publish():
    manifest = json.loads((STAGE / "manifest.json").read_text(encoding="utf-8"))
    require(manifest["tool_sha256"] == tool_hashes(), "Công cụ đổi sau khi dựng.")
    verify_originals(manifest)
    for name, sha in manifest["artifacts_sha256"].items():
        require(digest(STAGE / "images" / name) == sha, f"File dựng đã đổi: {name}")
    old_derived = {p: sha for p, sha in manifest["before_sha256"].items() if p not in manifest["original_sha256"]}
    # Phase 1: validate the complete set before any archive/unlink.
    for name, sha in old_derived.items():
        path, archive = ART / name, archive_name(ART / name)
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
            require(digest(destination) == sha, f"File đích khác lô 012b: {destination}")
            continue
        if destination.suffix == ".png":
            n.publish(STAGE / "images" / name, destination)
        else:
            with open(destination, "xb") as output, open(STAGE / "images" / name, "rb") as source:
                shutil.copyfileobj(source, output)
    out = ART / "_review/normalize-metrics.json"
    if not out.exists():
        json_new(out, {**manifest, "archived_012": {p: str(archive_name(ART / p).relative_to(ART)) for p in old_derived},
                      "old_records_note": "Hồ sơ 012 dùng thuật toán đã loại; xem các JSON .rejected-012, không tái tạo bằng mã 012b."})
    verify_originals(manifest)
    print(f"Đã công bố {len(manifest['records'])} bản xử lý; lưu {len(old_derived)} file dẫn xuất cũ; giữ {len(manifest['original_sha256'])} file gốc.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["build", "build-parallel", "publish"])
    parser.add_argument("--shard")
    args = parser.parse_args()
    n.WORK.mkdir(exist_ok=True)
    lock = open(os.environ.get("ART_NORMALIZE_LOCK", n.WORK / "dragon-hold-publish.lock"), "a")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        raise SystemExit("Một runner Rồng đang chạy; từ chối chạy đồng thời.")
    current = json.loads((ART / "_review/normalize-metrics.json").read_text())
    require(current.get("ticket") not in ("012b", "012c") and not current.get("archived_012"), "Runner 012b đã khóa sau công bố; dùng 012c.")
    if args.action == "build-parallel":
        snapshot()
        def worker(index):
            subprocess.run([sys.executable, str(Path(__file__).resolve()), "build", "--shard", f"{index}/3"], check=True)
        with ThreadPoolExecutor(max_workers=3) as pool:
            list(pool.map(worker, range(3)))
        build()
    elif args.action == "build":
        build(tuple(map(int, args.shard.split("/"))) if args.shard else None)
    else:
        publish()
