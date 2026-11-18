"""Kiểm tra riêng công cụ trạng thái; không mở máy chủ hoặc chạy game."""

import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import Mock, patch
from urllib.error import HTTPError

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import status


CLOSED_URL = "http://127.0.0.1:0"


class StatusTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write_jobs(self, jobs):
        path = self.root / "jobs.json"
        path.write_text(json.dumps({"jobs": jobs}), encoding="utf-8")
        return path

    def test_closed_ports_and_missing_files_do_not_raise(self):
        video = status.read_video(self.root, CLOSED_URL)
        sound = status.read_sound(self.root, CLOSED_URL)
        lab = status.read_lab(self.root, CLOSED_URL, CLOSED_URL)
        self.assertEqual(video["status"], "down")
        self.assertEqual(sound["status"], "down")
        self.assertTrue(all(item["status"] == "down" for item in lab.values()))
        self.assertEqual(video["jobs_status"], "missing")
        self.assertEqual(sound["jobs_status"], "missing")
        self.assertIsNone(video["remaining_jobs"])
        self.assertIsNone(sound["counts"])

    def test_remaining_video_jobs_use_files_not_done_endpoint(self):
        jobs = self.write_jobs([{"id": "water"}, {"id": "fire"}])
        output = self.root / "video"
        (output / "water").mkdir(parents=True)
        (output / "fire").mkdir()
        (output / "water" / "take1.mp4").write_bytes(b"video")
        (output / "fire" / "take1.mp4").mkdir()  # Thư mục không phải video.
        with patch.object(status, "_http", return_value=(200, b'{"old-job":[1,2]}')):
            result = status.read_video(self.root, jobs_path=jobs, output_path=output)
        self.assertEqual(result["remaining_jobs"], 1)
        self.assertEqual(result["done_jobs"], 1)
        self.assertEqual(result["done_takes"], 2)
        self.assertEqual(result["status"], "up")

    def test_sound_states_and_round_done_are_distinct(self):
        jobs = self.write_jobs([{"state": "done"}, {"state": "failed (3 tries)"},
                                {}, {"state": "round 1 done"},
                                {"state": "round 2 failed"}])
        with patch.object(status, "_http", return_value=(200, b"ok\n")):
            result = status.read_sound(self.root, jobs_path=jobs)
        self.assertEqual(result["counts"],
                         dict(done=1, failed=2, in_progress=1, pending=1))
        self.assertEqual(result["status"], "up")

    def test_missing_video_directory_means_all_jobs_remaining(self):
        jobs = self.write_jobs([{"id": "a"}, {"id": "b"}])
        result = status.read_video(self.root, CLOSED_URL, jobs, self.root / "absent")
        self.assertEqual(result["remaining_jobs"], 2)
        self.assertEqual(result["output_status"], "missing")

    def test_latest_directory_uses_directory_modification_time(self):
        output = self.root / "video"
        older, newer = output / "older", output / "water-ribbon-loop"
        older.mkdir(parents=True)
        newer.mkdir()
        stamp = time.time() - 60
        os.utime(older, (stamp - 60, stamp - 60))
        os.utime(newer, (stamp, stamp))
        (output / "ignore.mp4").write_bytes(b"newer file")
        result = status.read_video(self.root, CLOSED_URL, output_path=output)
        self.assertEqual(result["latest"], {
            "name": newer.name, "time": time.strftime("%H:%M", time.localtime(stamp))})

    def test_malformed_json_and_job_id_are_reported(self):
        jobs = self.root / "broken.json"
        jobs.write_text("{", encoding="utf-8")
        with patch.object(status, "_http", return_value=(200, b"not JSON")):
            result = status.read_video(self.root, jobs_path=jobs)
            self.assertEqual(result["status"], "down")
            self.assertEqual(result["jobs_status"], "missing")
            self.assertIsNone(status.read_sound(self.root, jobs_path=jobs)["counts"])
        jobs = self.write_jobs([{"id": "../outside"}])
        result = status.read_video(self.root, CLOSED_URL, jobs)
        self.assertEqual(result["jobs_status"], "missing")

    def test_http_timeout_proxy_and_redirect_guards(self):
        response = Mock()
        response.getcode.return_value = 200
        response.read.return_value = b"ok"
        opener = Mock()
        opener.open.return_value.__enter__ = Mock(return_value=response)
        opener.open.return_value.__exit__ = Mock(return_value=False)
        with patch.object(status, "build_opener", return_value=opener) as build:
            self.assertEqual(status._http(status.SOUND_URL, True), (200, b"ok"))
            opener.open.assert_called_once_with(status.SOUND_URL, timeout=2)
            self.assertEqual(build.call_args[0][0].proxies, {})
            redirect = build.call_args[0][1]
            self.assertIsNone(redirect.redirect_request(
                None, None, 302, "redirect", {}, "http://example.com"))
            build.reset_mock()
            for url in ("http://example.com", "http://localhost:8791",
                        "https://127.0.0.1", "http://127.0.0.1@elsewhere"):
                self.assertEqual(status._http(url), (None, b""))
            build.assert_not_called()

    def test_lab_http_errors_keep_the_status_code(self):
        error = HTTPError(status.SKILLS_URL, 404, "missing", {}, None)
        opener = Mock()
        opener.open.side_effect = error
        with patch.object(status, "build_opener", return_value=opener):
            result = status.read_lab(self.root)
        self.assertEqual(result["skills"], {"status": "down", "http": 404})
        self.assertEqual(result["gallery"], {"status": "down", "http": 404})

    def test_codex_only_three_recent_logs_and_last_nonempty_line(self):
        logs = self.root / "logs"
        logs.mkdir()
        now = time.time()
        for index in range(5):
            path = logs / "codex-lane-mac-{}.out".format(index)
            path.write_text("old\n" + "x" * 9000 + "\nlast {}\n \n\n".format(index))
            stamp = now - (90000 if index == 4 else index * 60)
            os.utime(path, (stamp, stamp))
        (logs / "unrelated.out").write_text("ignore")
        process = Mock(returncode=0, stdout="/bin/bash tools/codex-run/queue.sh\n")
        with patch.object(status.subprocess, "run", return_value=process):
            result = status.read_codex(self.root, log_path=logs, now=now)
        self.assertEqual([entry["last_line"] for entry in result["logs"]],
                         ["last 0", "last 1", "last 2"])
        self.assertTrue(result["queue"]["running"])

    def test_codex_empty_log_and_process_unavailable(self):
        logs = self.root / ".local"
        logs.mkdir()
        (logs / "codex-lane-mac-empty.out").write_text("\n \n")
        with patch.object(status.subprocess, "run", side_effect=OSError):
            result = status.read_codex(self.root)
        self.assertEqual(result["logs"][0]["last_line"], "missing")
        self.assertEqual(result["queue"]["status"], "missing")
        process = Mock(returncode=0, stdout="/usr/bin/python3 other.py\n")
        with patch.object(status.subprocess, "run", return_value=process):
            self.assertFalse(status.read_codex(self.root)["queue"]["running"])

    def test_swap_units_used_value_and_warning_boundaries(self):
        for swap, free, warnings in (("13312.00M", 9, ["RAM!", "ĐĨA!"]),
                                     ("12.00G", 10, []), ("0.00M", 20, [])):
            with self.subTest(swap=swap, free=free):
                process = Mock(returncode=0, stdout=(
                    "vm.swapusage: total = 32768.00M used = " + swap
                    + " free = 100.00M (encrypted)"))
                disk = Mock(free=free * status.GB)
                with patch.object(status.subprocess, "run", return_value=process), \
                        patch.object(status.shutil, "disk_usage", return_value=disk):
                    result = status.read_machine(self.root, disk_path=self.root)
                self.assertEqual(result["warnings"], warnings)
                if swap == "13312.00M":
                    self.assertEqual(result["swap_used_gb"], 13)

    def test_machine_missing_commands_and_disk_are_safe(self):
        with patch.object(status.subprocess, "run", side_effect=OSError), \
                patch.object(status.shutil, "disk_usage", side_effect=OSError):
            result = status.read_machine(self.root)
        self.assertEqual(result["swap_status"], "missing")
        self.assertEqual(result["disk_status"], "missing")
        self.assertEqual(result["warnings"], [])

    def test_text_line_limit_and_source_failure_isolation(self):
        with patch.object(status, "read_video", side_effect=OSError), \
                patch.object(status, "read_sound", side_effect=OSError), \
                patch.object(status, "read_lab", side_effect=OSError), \
                patch.object(status, "read_codex", side_effect=OSError), \
                patch.object(status, "read_machine", side_effect=OSError):
            data = status.collect_status(self.root)
            data["codex"] = {"logs_status": "ok", "logs": [
                {"name": "lane\n{}".format(i), "last_line": "end\rtext"}
                for i in range(3)]}
            self.assertLessEqual(len(status.format_text(data).splitlines()), 15)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(status.main(["--json"]), 0)
            self.assertEqual(set(json.loads(output.getvalue())),
                             {"time", "video", "sound", "lab", "codex", "machine"})

    def test_json_cli_from_another_working_directory(self):
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        result = subprocess.run([sys.executable, str(Path(status.__file__)), "--json"],
                                cwd=self.root, capture_output=True, text=True,
                                timeout=20, env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        data = json.loads(result.stdout)
        self.assertEqual(set(data), {"time", "video", "sound", "lab", "codex", "machine"})
        self.assertRegex(data["time"], r"^\d{2}:\d{2}$")


if __name__ == "__main__":
    unittest.main()
