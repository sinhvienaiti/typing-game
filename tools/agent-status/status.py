#!/usr/bin/env python3
"""Đọc trạng thái điều phối trong một lệnh; chỉ dùng thư viện chuẩn."""

import json
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, build_opener


REPO_ROOT = Path(__file__).resolve().parents[2]
VIDEO_URL = "http://127.0.0.1:8841/done"
SOUND_URL = "http://127.0.0.1:8791/ping"
SKILLS_URL = "http://127.0.0.1:4310/skills-lab.html"
GALLERY_URL = (
    "http://127.0.0.1:4330/typing-game-review/owner-review/"
    "2026-11-05/tu-tien/firefly-gallery/index.html"
)
VIDEO_JOBS = Path("docs/work/tasks/firefly-sprint-video.json")
SOUND_JOBS = Path("docs/work/tasks/firefly-sprint-sound.json")
SPRINT_OUTPUT = Path(
    "games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05"
)
DISK_PATH = Path("/Volumes/SS990TPRO")
HTTP_TIMEOUT = 2
GB = 1024 ** 3


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def _http(url, read_body=False):
    """Không dùng proxy và không theo redirect, kể cả sang máy khác."""
    try:
        parsed = urlsplit(url)
        if (parsed.scheme != "http" or parsed.hostname != "127.0.0.1"
                or parsed.username is not None or parsed.password is not None):
            return None, b""
        opener = build_opener(ProxyHandler({}), _NoRedirect())
        with opener.open(url, timeout=HTTP_TIMEOUT) as response:
            return response.getcode(), response.read() if read_body else b""
    except HTTPError as exc:
        code = exc.code
        try:
            exc.close()
        except Exception:
            pass
        return code, b""
    except Exception:
        return None, b""


def _up(code):
    return code is not None and 200 <= code < 300


def _jobs(repo_root, path):
    try:
        data = json.loads((Path(repo_root) / path).read_text(encoding="utf-8"))
        jobs = data["jobs"]
        if isinstance(jobs, list) and all(isinstance(job, dict) for job in jobs):
            return jobs
    except Exception:
        pass
    return None


def _latest_directory(path):
    try:
        newest = None
        for entry in path.iterdir():
            try:
                if entry.is_dir():
                    modified = entry.stat().st_mtime
                    if newest is None or (modified, entry.name) > newest[:2]:
                        newest = (modified, entry.name)
            except OSError:
                continue
        latest = None if newest is None else {
            "name": newest[1],
            "time": datetime.fromtimestamp(newest[0]).strftime("%H:%M"),
        }
        return "ok", latest
    except Exception:
        return "missing", None


def read_video(repo_root=REPO_ROOT, url=VIDEO_URL, jobs_path=VIDEO_JOBS,
               output_path=SPRINT_OUTPUT / "video"):
    code, body = _http(url, read_body=True)
    result = {"status": "down", "http": code, "done_jobs": None,
              "done_takes": None, "remaining_jobs": None}
    try:
        done = json.loads(body)
        if _up(code) and isinstance(done, dict) and all(
                isinstance(takes, list) for takes in done.values()):
            result.update(status="up", done_jobs=len(done),
                          done_takes=sum(len(takes) for takes in done.values()))
    except Exception:
        pass
    jobs = _jobs(repo_root, jobs_path)
    result["jobs_status"] = "missing" if jobs is None else "ok"
    output = Path(repo_root) / output_path
    result["output_status"], result["latest"] = _latest_directory(output)
    if jobs is not None:
        try:
            remaining = 0
            for job in jobs:
                job_id = job["id"]
                if (not isinstance(job_id, str) or not job_id
                        or job_id in (".", "..") or "/" in job_id or "\\" in job_id):
                    raise ValueError("id không phải tên thư mục")
                if not any(p.is_file() for p in (output / job_id).glob("*.mp4")):
                    remaining += 1
            result["remaining_jobs"] = remaining
        except Exception:
            result["jobs_status"] = "missing"
    return result


def read_sound(repo_root=REPO_ROOT, url=SOUND_URL, jobs_path=SOUND_JOBS,
               output_path=SPRINT_OUTPUT / "sound"):
    code, body = _http(url, read_body=True)
    result = {"status": "up" if _up(code) and body.strip() == b"ok" else "down",
              "http": code, "counts": None}
    jobs = _jobs(repo_root, jobs_path)
    result["jobs_status"] = "missing" if jobs is None else "ok"
    if jobs is not None:
        counts = dict(done=0, failed=0, in_progress=0, pending=0)
        for job in jobs:
            state = str(job.get("state", "")).strip().lower()
            if state == "done":
                key = "done"
            elif "failed" in state:
                key = "failed"
            elif "round" in state:
                key = "in_progress"
            else:
                key = "pending"
            counts[key] += 1
        result["counts"] = counts
    result["output_status"], result["latest"] = _latest_directory(
        Path(repo_root) / output_path)
    return result


def read_lab(repo_root=REPO_ROOT, skills_url=SKILLS_URL, gallery_url=GALLERY_URL):
    result = {}
    for name, url in (("skills", skills_url), ("gallery", gallery_url)):
        code, _ = _http(url)
        result[name] = {"status": "up" if _up(code) else "down", "http": code}
    return result


def _last_nonempty_line(path):
    """Đọc ngược để tránh nạp toàn bộ nhật ký của một phiên dài."""
    try:
        with path.open("rb") as stream:
            position = stream.seek(0, 2)
            pending = b""
            while position:
                size = min(position, 8192)
                position -= size
                stream.seek(position)
                lines = (stream.read(size) + pending).split(b"\n")
                pending = lines[0]
                for line in reversed(lines[1:]):
                    text = line.decode("utf-8", errors="replace").strip()
                    if text:
                        return text
            return pending.decode("utf-8", errors="replace").strip() or "missing"
    except Exception:
        return "missing"


def read_codex(repo_root=REPO_ROOT, log_path=Path(".local"),
               process_command=("ps", "-axo", "command="), now=None):
    result = {"logs_status": "missing", "logs": [],
              "queue": {"status": "missing", "running": None}}
    try:
        cutoff = (time.time() if now is None else now) - 24 * 60 * 60
        directory = Path(repo_root) / log_path
        if directory.is_dir():
            candidates = []
            for path in directory.glob("codex-lane-mac-*.out"):
                try:
                    if path.is_file() and path.stat().st_mtime >= cutoff:
                        candidates.append((path.stat().st_mtime, path.name, path))
                except OSError:
                    continue
            for modified, name, path in sorted(candidates, reverse=True)[:3]:
                result["logs"].append({"name": name,
                                       "last_line": _last_nonempty_line(path)})
            result["logs_status"] = "ok"
    except Exception:
        pass
    try:
        processes = subprocess.run(process_command, capture_output=True, text=True,
                                   timeout=2, check=False)
        if processes.returncode == 0:
            running = "tools/codex-run/queue.sh" in processes.stdout
            result["queue"] = {"status": "up" if running else "down",
                               "running": running}
    except Exception:
        pass
    return result


def read_machine(repo_root=REPO_ROOT, disk_path=DISK_PATH,
                 swap_command=("sysctl", "vm.swapusage")):
    result = {"swap_status": "missing", "swap_used_gb": None,
              "disk_status": "missing", "disk_free_gb": None, "warnings": []}
    try:
        swap = subprocess.run(swap_command, capture_output=True, text=True,
                              timeout=2, check=False)
        match = re.search(r"\bused\s*=\s*([0-9]+(?:\.[0-9]+)?)\s*([KMGT]?)"
                          r"(?:i?B)?\b", swap.stdout, re.IGNORECASE)
        if swap.returncode == 0 and match:
            value = float(match[1]) * 1024 ** (" KMGT".index(match[2].upper())) / GB
            result.update(swap_status="ok", swap_used_gb=value)
            if value > 12:
                result["warnings"].append("RAM!")
    except Exception:
        pass
    try:
        free = shutil.disk_usage(Path(repo_root) / disk_path).free / GB
        result.update(disk_status="ok", disk_free_gb=free)
        if free < 10:
            result["warnings"].append("ĐĨA!")
    except Exception:
        pass
    return result


def collect_status(repo_root=REPO_ROOT):
    data = {"time": datetime.now().strftime("%H:%M")}
    for name, reader in (("video", read_video), ("sound", read_sound),
                         ("lab", read_lab), ("codex", read_codex),
                         ("machine", read_machine)):
        try:
            data[name] = reader(repo_root=repo_root)
        except Exception:
            data[name] = {"status": "missing"}
    return data


def _shown(value):
    return "missing" if value is None else str(value)


def _latest_text(section):
    latest = section.get("latest")
    return "missing" if not latest else latest["name"] + " " + latest["time"]


def format_text(data):
    video, sound = data["video"], data["sound"]
    counts = sound.get("counts") or {}
    lines = [
        "giờ: " + data["time"],
        "video: {} · {} việc xong · {} take · còn {} · mới nhất {}".format(
            video.get("status", "missing"), _shown(video.get("done_jobs")),
            _shown(video.get("done_takes")), _shown(video.get("remaining_jobs")),
            _latest_text(video)),
        "âm: {} · {} xong · {} lỗi · {} dở · {} chờ · mới nhất {}".format(
            sound.get("status", "missing"), _shown(counts.get("done")),
            _shown(counts.get("failed")), _shown(counts.get("in_progress")),
            _shown(counts.get("pending")), _latest_text(sound)),
    ]
    for name, label in (("skills", "lab"), ("gallery", "thư viện")):
        lab = data["lab"].get(name, {})
        lines.append("{}: {} · HTTP {}".format(
            label, lab.get("status", "missing"), _shown(lab.get("http"))))
    codex = data["codex"]
    logs = codex.get("logs", [])
    lines.append("codex: " + ("missing" if codex.get("logs_status") != "ok"
                              else "{} nhật ký trong 24 giờ".format(len(logs))))
    for log in logs:
        lines.append("  {}: {}".format(log["name"], log["last_line"]))
    running = codex.get("queue", {}).get("running")
    lines.append("queue.sh: " + ("missing" if running is None else
                                 "chạy" if running else "không chạy"))
    machine = data["machine"]
    swap, free = machine.get("swap_used_gb"), machine.get("disk_free_gb")
    line = "máy: swap {} · SSD trống {}".format(
        "missing" if swap is None else "{:.2f} GB".format(swap),
        "missing" if free is None else "{:.2f} GB".format(free))
    if machine.get("warnings"):
        line += " · " + " · ".join(machine["warnings"])
    lines.append(line)
    return "\n".join(" ".join(line.split()) for line in lines)


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    try:
        data = collect_status()
        output = json.dumps(data, ensure_ascii=False, indent=2) if "--json" in args \
            else format_text(data)
    except Exception:
        data = dict(time="missing", video={"status": "down"},
                    sound={"status": "down"}, lab={"status": "down"},
                    codex={"status": "missing"}, machine={"status": "missing"})
        output = json.dumps(data) if "--json" in args else format_text(data)
    try:
        print(output)
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
