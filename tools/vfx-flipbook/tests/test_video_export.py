"""Video-export planning, manifest preservation and frame-exact ffmpeg integration."""
from __future__ import annotations

import copy
import json
import subprocess
import threading
from pathlib import Path

import pytest

from vfxflip import video_export
from vfxflip.__main__ import main


def _entry(**overrides):
    entry = {"source": "source.mp4", "take": 2, "loop": False,
             "trim": {"start": 5, "end": 41, "step": 4},
             "timing": {"peak": 7, "holdEnd": 7}, "sourceFps": 24,
             "pivot": [0.3, 0.6], "note": "Giữ nguyên dấu tiếng Việt", "custom": {"a": [1, 2]}}
    entry.update(overrides)
    return entry


def _metadata(width=1000, height=600):
    return {"source": {"crop": [90, 40, 600, 300], "width": width, "height": height}}


def _manifest(tmp_path, entries, metadata=None):
    repo = tmp_path / "repo có dấu"
    folder = repo / "nested" / "vfx"
    folder.mkdir(parents=True)
    (repo / "source.mp4").write_bytes(b"not encoded in planning tests")
    data = {"version": 1, "note": "Thông tin đầu manifest", "flipbooks": entries,
            "textures": {"another": {"file": "other.png"}}, "custom": [None, 17, "giữ"]}
    manifest = folder / "manifest.json"
    manifest.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    for cid in entries:
        (folder / f"{cid}.json").write_text(json.dumps(metadata or _metadata()), encoding="utf-8")
    return repo, manifest, data


@pytest.mark.parametrize("start,end,peak,source_fps,expected", [
    (0, 121, 0, 24, 0.0),
    (12, 120, 7, 24, 1.167),
    (5, 41, 7, None, 1.167),
])
def test_calculate_cut(start, end, peak, source_fps, expected):
    entry = _entry(trim={"start": start, "end": end, "step": 4},
                   timing={"peak": peak, "holdEnd": 1})
    if source_fps is None:
        entry.pop("sourceFps")
    else:
        entry["sourceFps"] = source_fps
    cut = video_export.calculate_cut(entry)
    assert (cut.start, cut.end, cut.frames) == (start, end, end - start)
    assert cut.duration == round((end - start) / 24, 3)
    assert cut.peak_time == expected  # holdEnd does not shorten the tail


def test_peak_time_uses_source_fps_and_duration_uses_output_fps():
    cut = video_export.calculate_cut(_entry(sourceFps=30))
    assert cut.peak_time == 0.933
    assert cut.duration == 1.5


def test_pivot_maps_crop_to_full_source():
    assert video_export.calculate_pivot(_entry(), _metadata()) == [0.27, 0.3667]


def test_pivot_matches_real_myriad_lotus_domain():
    folder = Path(__file__).resolve().parents[3] / "games/immortality-cultivation/art-src/lab/vfx/expansion"
    if not (folder / "manifest.json").is_file():
        pytest.skip("ảnh nguồn và manifest lab không được phân phối cùng công cụ")
    entry = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))["flipbooks"]["myriad-lotus-domain"]
    metadata = json.loads((folder / "myriad-lotus-domain.json").read_text(encoding="utf-8"))
    pivot = video_export.calculate_pivot(entry, metadata)
    assert pivot == pytest.approx(entry["video"]["pivot"], abs=0.0001)
    assert pivot != entry["pivot"]


@pytest.mark.parametrize("changes,removed,force,reason", [
    ({"loop": True}, (), False, "loop: true"),
    ({"loop": True}, (), True, "loop: true"),
    ({"video": {"take": 2}}, (), False, "đã có video"),
    ({"video": {"take": 2}}, (), True, None),
    ({"video": {"take": 1}}, (), False, None),
    ({"video": {"file": "legacy.mp4"}}, (), False, "đã có video"),
    ({"video": {"file": "legacy.mp4"}}, (), True, None),
    ({}, ("trim",), False, "thiếu trim"),
    ({}, ("timing",), False, "thiếu timing"),
    ({"source": "Firefly clip try1"}, (), False, "source không phải file .mp4"),
    ({"source": "source.png"}, (), False, "source không phải file .mp4"),
    ({"source": "missing.mp4"}, (), False, "không tìm thấy file source .mp4"),
    ({}, ("source",), False, "source không phải file .mp4"),
])
def test_skip_rules(tmp_path, changes, removed, force, reason):
    (tmp_path / "source.mp4").write_bytes(b"source")
    entry = _entry(**changes)
    for field in removed:
        entry.pop(field)
    actual = video_export.skip_reason(entry, tmp_path, force=force)
    assert actual is None if reason is None else actual.startswith(reason)


def test_cli_dry_run_filters_ids_and_writes_nothing(tmp_path, monkeypatch, capsys):
    repo, manifest, _ = _manifest(tmp_path, {"selected": _entry(), "other": _entry()})
    before = {p: p.read_bytes() for p in repo.rglob("*") if p.is_file()}

    def unexpected_process(*args, **kwargs):
        pytest.fail("dry-run không được chạy ffmpeg/ffprobe")

    monkeypatch.setattr(video_export.subprocess, "run", unexpected_process)
    assert main(["export-video", "--manifest", str(manifest), "--repo-root", str(repo),
                 "--ids", " selected, ", "--jobs", "2", "--dry-run"]) == 0
    output = capsys.readouterr().out
    assert "plan selected: START=5 END=41 duration=1.500s peakTime=1.167s" in output
    assert "other" not in output
    assert "dry-run: 1 mục cần xuất" in output
    assert {p: p.read_bytes() for p in repo.rglob("*") if p.is_file()} == before


def test_cli_default_repo_root(monkeypatch):
    calls = []
    monkeypatch.setattr(video_export, "export_manifest", lambda *args, **kwargs: calls.append(kwargs))
    assert main(["export-video", "--manifest", "manifest.json", "--dry-run"]) == 0
    assert calls[0]["repo_root"] == Path(__file__).resolve().parents[3]
    assert calls[0]["jobs"] == 3


@pytest.mark.parametrize("jobs", ["0", "-1", "abc"])
def test_cli_rejects_invalid_jobs(jobs):
    with pytest.raises(SystemExit) as exc:
        main(["export-video", "--manifest", "manifest.json", "--jobs", jobs])
    assert exc.value.code == 2


def test_skipped_entries_do_not_need_sidecars(tmp_path, capsys):
    entries = {"loop": _entry(loop=True), "existing": _entry(video={"take": 2}),
               "legacy": _entry(video={"file": "old.mp4"}), "no-trim": _entry(),
               "no-timing": _entry(), "not-mp4": _entry(source="old text"),
               "missing": _entry(source="missing.mp4")}
    entries["no-trim"].pop("trim")
    entries["no-timing"].pop("timing")
    repo, manifest, _ = _manifest(tmp_path, entries)
    for sidecar in manifest.parent.glob("*.json"):
        if sidecar != manifest:
            sidecar.unlink()
    before = manifest.read_bytes()
    assert video_export.export_manifest(manifest, repo_root=repo) == 0
    output = capsys.readouterr().out
    for cid in entries:
        assert f"skip {cid}: " in output
    assert manifest.read_bytes() == before


def test_parallel_exports_respect_jobs_and_preserve_other_fields(tmp_path, monkeypatch):
    entries = {f"clip-{i}": _entry(video={"take": 1}) for i in range(4)}
    entries["untouched"] = _entry(video={"take": 2, "custom": "keep"})
    repo, manifest, original = _manifest(tmp_path, entries)
    active = maximum = 0
    lock = threading.Lock()
    barrier = threading.Barrier(2, timeout=10)

    def export(plan):
        nonlocal active, maximum
        with lock:
            active += 1
            maximum = max(maximum, active)
        barrier.wait()  # two workers must run; each pair finishes before the next pair
        with lock:
            active -= 1
        return {"take": plan.take, "bytes": 7, "frames": 36, "w": 1000, "h": 600}

    monkeypatch.setattr(video_export, "_export_one", export)
    assert video_export.export_manifest(manifest, repo_root=repo, jobs=2) == 4
    assert maximum == 2
    data = json.loads(manifest.read_text(encoding="utf-8"))
    for cid, entry in data["flipbooks"].items():
        if cid != "untouched":
            assert entry["video"]["take"] == 2
            entry["video"] = original["flipbooks"][cid]["video"]
    assert data == original


@pytest.fixture(params=[(320, 180), (160, 160)], ids=["wide", "square"])
def encoded_manifest(tmp_path, request):
    width, height = request.param
    repo, manifest, original = _manifest(
        tmp_path, {"effect": _entry(), "untouched": _entry(loop=True)},
        _metadata(width, height))
    subprocess.run(
        ["ffmpeg", "-v", "error", "-nostdin", "-y", "-f", "lavfi", "-i",
         f"testsrc=size={width}x{height}:rate=24:duration=2", "-f", "lavfi", "-i",
         "sine=frequency=440:duration=2", "-c:v", "libx264", "-preset", "veryfast",
         "-pix_fmt", "yuv420p", "-threads", "2", "-c:a", "aac", str(repo / "source.mp4")],
        capture_output=True, check=True)
    return repo, manifest, original, width, height


def test_export_video_end_to_end(encoded_manifest):
    repo, manifest, original, width, height = encoded_manifest
    assert main(["export-video", "--manifest", str(manifest), "--repo-root", str(repo)]) == 0
    text = manifest.read_text(encoding="utf-8")
    data = json.loads(text)
    video = data["flipbooks"]["effect"].pop("video")
    assert data == original
    output = manifest.parent / "effect.mp4"
    assert video == {"file": "effect.mp4", "w": width, "h": height, "fps": 24.0,
                     "frames": 36, "start": 0.0, "peakTime": 1.167,
                     "pivot": video_export.calculate_pivot(original["flipbooks"]["effect"],
                                                          _metadata(width, height)),
                     "bytes": output.stat().st_size, "take": 2, "source": "source.mp4"}
    streams = json.loads(subprocess.run(
        ["ffprobe", "-v", "error", "-count_frames", "-show_streams", "-of", "json", str(output)],
        capture_output=True, text=True, check=True).stdout)["streams"]
    assert len(streams) == 1 and streams[0]["codec_type"] == "video"
    assert streams[0]["codec_name"] == "h264" and streams[0]["pix_fmt"] == "yuv420p"
    assert streams[0]["r_frame_rate"] == "24/1" and int(streams[0]["nb_read_frames"]) == 36
    binary = output.read_bytes()
    assert 0 <= binary.find(b"moov") < binary.find(b"mdat")
    assert binary.find(b"moov") < 65536
    assert not list(manifest.parent.glob("*.tmp*"))
    assert not list(manifest.parent.glob(".*.tmp"))
    assert text == json.dumps(json.loads(text), indent=1, ensure_ascii=False) + "\n"


def test_failed_export_preserves_old_video_and_manifest(tmp_path, capsys):
    repo, manifest, _ = _manifest(tmp_path, {"effect": _entry(video={"take": 1})})
    before = manifest.read_bytes()
    output = manifest.parent / "effect.mp4"
    output.write_bytes(b"previous video")
    assert main(["export-video", "--manifest", str(manifest), "--repo-root", str(repo)]) == 3
    assert "effect: ffmpeg lỗi" in capsys.readouterr().err
    assert manifest.read_bytes() == before
    assert output.read_bytes() == b"previous video"
    assert not (manifest.parent / "effect.tmp.mp4").exists()


def test_short_source_does_not_replace_existing_video(encoded_manifest):
    repo, manifest, original, _, _ = encoded_manifest
    data = copy.deepcopy(original)
    data["flipbooks"]["effect"]["trim"]["end"] = 60  # the source has only 48 frames
    manifest.write_text(json.dumps(data), encoding="utf-8")
    before = manifest.read_bytes()
    output = manifest.parent / "effect.mp4"
    output.write_bytes(b"previous video")
    with pytest.raises(video_export.VideoExportError, match="không đúng số khung"):
        video_export.export_manifest(manifest, repo_root=repo)
    assert manifest.read_bytes() == before
    assert output.read_bytes() == b"previous video"
    assert not (manifest.parent / "effect.tmp.mp4").exists()
