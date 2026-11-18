"""Verify ticket 191's copies, media lock, ignored audio and built package offline."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[3]
SOURCE = Path.home() / "AudioLab/review/staging/keys-firefly"
BASE = Path("public/assets/typing-survival/audio/keys")
rows = json.loads((ROOT / "docs/codex-queue/191/copied-files.json").read_text())
lock = dict(line.split("  ", 1)[::-1] for line in (ROOT / "media.md5").read_text().splitlines())
groups = {}
for row in rows:
    relative = Path(row["path"]).relative_to(BASE)
    data = (ROOT / row["path"]).read_bytes()
    assert data == (SOURCE / relative).read_bytes()
    assert hashlib.sha256(data).hexdigest() == row["sha256"]
    assert hashlib.md5(data).hexdigest() == row["md5"]
    packed = ROOT / "dist/assets/typing-survival/audio/keys" / relative
    assert packed.read_bytes() == data
    ignored = subprocess.run(["git", "check-ignore", "-q", row["path"]], cwd=ROOT).returncode == 0
    assert ignored == (relative.suffix == ".ogg")
    if relative.suffix == ".ogg":
        assert lock[row["path"]] == row["md5"]
        assert data[:4] == b"OggS"
    group = relative.parts[0] if len(relative.parts) > 1 else "root"
    value = groups.setdefault(group, {"files": 0, "bytes": 0, "ogg": 0, "json": 0})
    value["files"] += 1
    value["bytes"] += len(data)
    value[relative.suffix[1:]] += 1
assert not list((ROOT / BASE).rglob("*.wav"))
protected = ["src/kit", "src/sim", "src/content", "tests/golden"]
assert not subprocess.check_output(["git", "diff", "HEAD", "--name-only", "--", *protected], cwd=ROOT).strip()
golden = "tests/golden/s0-trace.json"
assert (ROOT / golden).read_bytes() == subprocess.check_output(["git", "show", "HEAD:" + golden], cwd=ROOT)
report = {
    "files": len(rows), "bytes": sum(row["bytes"] for row in rows),
    "ogg": sum(row["path"].endswith(".ogg") for row in rows),
    "json": sum(row["path"].endswith(".json") for row in rows),
    "sourceCopiesMatch": True, "distCopiesMatch": True, "oggLockedAndIgnored": True,
    "jsonNotIgnored": True, "wavCopied": 0, "protectedPathsUnchanged": protected,
    "goldenSha256": hashlib.sha256((ROOT / golden).read_bytes()).hexdigest(), "groups": groups,
}
(ROOT / "docs/codex-queue/191/verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(report, ensure_ascii=False))
