# Phiếu 217 · Nhận âm Adobe Firefly cho ba game

Ngày 30/10/2026, repo cha `/Users/toandx/htdocs/typing-game`, nhánh `feat/space-typing-admin-uiux`. Đã dựng ba lệnh `firefly ingest`, `listen`, `status`, lớp giấy phép có điều kiện, test và demo kỹ thuật. Chưa gắn âm vào game; chờ Claude duyệt mã và giấy phép rồi commit.

## Kết quả và số kiểm

| Lượt | Qua | Lỗi kiểm thử | Lỗi thiết lập | Bỏ qua |
|---|---:|---:|---:|---:|
| Audio Lab trước sửa, theo `pytest.ini` | 519 | 6 | 10 | 6 |
| Test mới của 217 | 20 | 0 | 0 | 0 |
| Audio Lab sau sửa, theo `pytest.ini` | 539 | 6 | 10 | 6 |
| Context và Keys hiện có, chạy bổ sung | 74 | 0 | 0 | 0 |

Lượt bổ sung còn có **5 subtest qua**. `context` và `keys` không nằm trong `testpaths` có sẵn; không sửa cấu hình ngoài việc thêm `firefly` theo phiếu. Log: [trước](217/tests-before.txt), [test mới](217/tests-new.txt), [sau](217/tests-after.txt), [Context/Keys](217/tests-existing-context-keys.txt). Test mới viết trước mã; log đỏ ban đầu ở [tests-red.txt](217/tests-red.txt), và các ca bổ sung trước khi sửa ở `tests-loop-red.txt`, `tests-context-red.txt`, `tests-runtime-red.txt`.

Các lỗi cũ được giữ nguyên, không lách bằng bỏ test:

- Ba lỗi `common/tests/test_env.py`: test đòi home ngoài repo, môi trường shell mặc định và venv trùng `env.VENV`; wrapper của phiếu cố ý đặt `AUDIOLAB_HOME` trong `tmp/firefly-ingest/` trong khi Python chạy từ venv thật. Đây là hệ quả của yêu cầu cô lập cache trong sandbox.
- Một lỗi kiểm thử và 10 lỗi thiết lập Board: sandbox cấm mở socket (`PermissionError: [Errno 1] Operation not permitted`). Không chạy dev server hoặc trình duyệt.
- Hai lỗi Specs đã có trước: 16 lỗi phân loại ở các id `gun.ray.armed`, `gun.tia.loop`, `streak.up`, `word.full` của Last Line. Không sửa thẻ hoặc mã làn khác.

Wrapper [run-tests.py](217/run-tests.py) đặt cwd đúng Audio Lab, pycache, numba, matplotlib, pytest cache và basetemp dưới `tmp/firefly-ingest/`; test gọi trực tiếp `firefly.main(argv)`. Ca cô lập đặt `AUDIOLAB_HOME` và các đường `common.env` vào thư mục rỗng tạm, chạy cả ba lệnh, rồi xác nhận thư mục đó vẫn rỗng. Test cũng kiểm bản ghi WAV nguyên mẫu, schema công thức, tương quan, cú chồng, final bị chặn vẫn giữ master, cache giọng thiếu, menu không cần giọng, đường xuất vượt phạm vi và symlink ngược vào inbox.

`pnpm audio:licence-check` mặc định trả **0** cả trước/sau, đầu ra **giống hệt từng byte**: trạng thái **BỎ QUA**, chưa game nào nhận đường ống SOURCES/licences; 116 file Space Typing cũ được miễn. Không gọi đây là kiểm giấy phép thật đã đạt cho các game. Cây art-src/public tạm của test render → release thì `licence-check` **0 lỗi**; bản lưu giấy phép được chép nguyên byte. Xem [licence-before.txt](217/licence-before.txt), [licence-after.txt](217/licence-after.txt).

## Demo hai id thật

[demo.py](217/demo.py) sinh fixture dưới `tmp/firefly-ingest/inbox/`, chạy ingest hai lần, listen và status; cả bốn mã thoát đều **0**. Số đầy đủ ở [demo.json](217/demo.json), log ở [demo.txt](217/demo.txt). Dùng cache giọng đã có tại `/Users/toandx/AudioLab/work/_context/voices`, chỉ đọc; không gọi `say`, không ghi giọng. Fixture là tín hiệu kỹ thuật, không phải âm Q6 để phát hành.

| Id | Tìm thấy / qua raw / chọn | Biến thể so với thẻ | Final | Bản nghe |
|---|---|---|---|---|
| `dragon-hold/fire.impact.a` | 6 / 6 / 4 | 4; min 3, target 4 | PASS cả 4 | context `dh-cast-chain`, 20,000 s |
| `dragon-hold/amb.forest` | 1 / 1 / 1 | 1; min và target 1 | PASS | context `dh-cast-chain`, 20,000 s |

| Id / biến thể | LUFS-M max WAV | LUFS-M max OGG | Đỉnh thật WAV / OGG (dBTP) | Độ dài master (ms) |
|---|---:|---:|---:|---:|
| fire.impact.a / 1 | −20,3800 | −20,3266 | −1,9595 / −1,9727 | 513,9375 |
| fire.impact.a / 2 | −20,3800 | −20,3176 | −1,4598 / −1,3484 | 508,3333 |
| fire.impact.a / 3 | −20,4633 | −20,4315 | −1,2945 / −1,3453 | 502,9375 |
| fire.impact.a / 4 | −20,6673 | −20,6140 | −1,2953 / −1,3597 | 494,3542 |
| amb.forest / 1 | −25,9609 | −25,9686 | −18,2860 / −18,1933 | 5950,0000 |

`fire.impact.a`: `idLevel` build báo −20,38, mức đích thẻ −20; sai lệch master tối đa 0,2873 dB, OGG tối đa 0,2340 dB so với idLevel, độ dài đều ≤720 ms. `amb.forest`: thẻ có `loudness.proposal: null`, nên dùng `loudness.file`, LUFS-I −26; WAV đo LUFS-I −26,0000, vòng 6000 ms qua crossfade 50 ms của build còn 5950 ms, dưới max 7200 ms. Take vòng gốc vẫn nguyên 6000 ms.

OGG quality **1,0** được ghi trong công thức. Test bổ sung phát hiện quality 0,6 mặc định của build làm một OGG lệch 0,5739 dB so với idLevel, dù master đạt. Tăng quality của công thức Firefly làm cả WAV và OGG đạt ±0,5 dB mà không sửa render/chain hoặc nới cổng.

Dựng lần hai: **10/10 file** giống SHA-256 (5 master, 5 OGG). Hai WAV inbox giữ nguyên **cả SHA-256 và mtime_ns** trước/sau. Take cắt giữ nguyên mẫu, sample rate, kênh, subtype và endian. `ingest.json` còn ghi hash/mtime toàn inbox, kể cả nguồn bị bỏ qua.

Hai MP3 decode đúng 20,000 giây, 192 kbps, fade cuối 50 ms; đỉnh thật lần lượt −6,2216 và −6,0207 dBTP. Context dùng biến thể đầu làm focus và lặp cảnh đủ 20 giây; sequence phát xoay vòng mọi biến thể. Ca thiếu giọng cache chuyển sequence đã được test. Chưa nghe/chấm chất lượng cảm nhận, không tuyên bố âm đạt mức thương mại hoặc 9+.

## Lựa chọn triển khai

- `auto` dùng whole cho loop/ambience/music, onset cho tiếng lẻ. Mặc định: threshold −35 dB theo đỉnh file, gap 150 ms, pre 5 ms, tail floor −60 dB theo đỉnh take. Đây là điểm xuất phát từ hình dạng lô phím 189 (48 kHz stereo, khoảng 12 s, nhiều cú), cần xem lại theo WAV thật. Fixture tiếng lẻ dài 12 s; fixture nền dài 6 s để đúng thẻ thật.
- Dò hoạt động khung 1 ms và tăng năng lượng trên đuôi còn chạy để tìm cú chồng. Cú thứ hai ở 40 ms được đánh dấu; cả hai cú liên quan không được chọn. Test 6 đầu tiếng đã biết lệch không quá 2 ms; tăng gap gộp được; whole giữ 1 take.
- Raw gate dùng nguyên `UNFIXABLE`; không đổi ngưỡng Critic. Một bảng trọng số: độ dài 0,60; lặng trước onset 0,20; nền cuối đuôi 0,20. Lưu mọi thành phần và điểm. Dùng tương quan chéo của 189, ngưỡng 0,95; không nhân bản hoặc đổi cao độ để bù thiếu.
- Công thức một lớp, `source.file` + dòng sổ take, các nguồn còn lại qua `vary.swap`, `swapMode: cycle`, không lệch pitch/gain ngẫu nhiên. `build.render(..., spec=thẻ)` tạo đủ master/runtime và hồ sơ. Final L1 kiểm từng master, giữ file chặn để điều phối xem.
- Đọc định dạng thật `docs/games/audio/firefly/typing-survival.json` của 212 và schema/README cùng thư mục. Hiện chỉ có danh sách Last Line; không có danh sách Dragonhold/Wordwoven. Demo dùng thẻ Dragonhold. Danh sách hiện chưa có export path, nên dùng `firefly/<id>` và ghi đường tạm trong description. Nếu hàng sau này có `export.path`/`exportPath`, công cụ nhận trực tiếp, kiểm không vượt thư mục runtime.
- Giọng chỉ đọc cache, không tạo mới; các chỗ âm khác im nếu không có `--slot`. Thông số và dòng thời gian của bộ trộn context hiện có được dùng lại; ghi rõ xấp xỉ bộ nén không có nhìn trước 6 ms. Không tự release hoặc gắn game.

## Claude cần xác nhận

1. Tên lớp **`LicenseRef-Adobe-Firefly-owner`** và điều kiện **`adobe-model`**; chú thích mã đúng “owner decision 29/10, Claude confirms”.
2. Allowlist tập trung `policy.ADOBE_AUDIO_MODELS`: tên chính xác `Adobe Firefly Audio Model`, có thể kèm phiên bản số (`v2`, `2.1`, có khoảng trắng hoặc dấu gạch nối). So khớp từ đầu và hết chuỗi, không chấp nhận tên đối tác hoặc tên chỉ chứa Adobe ở giữa.
3. `ai_input_allowed: true` chỉ cho **bộ chấm cục bộ trên máy** theo yêu cầu phiếu; không suy ra quyền huấn luyện, upload hay generation input. Claude xác nhận cờ này trước commit.
4. `licenceUrl`/`policy.url` hiện trỏ tương đối tới **`licences/adobe-firefly-owner-2026-10-29.txt`**, như lớp owner-recording. Bản gốc ở `tools/audio-lab/firefly/licences/`; test chứng minh luồng `licenceText` → `copies` → `licenceCopies` → `ledger.copy_licence_texts` hoạt động.
5. Ghi chú tiếng Anh là quyết định chủ dự án ngày 29/10/2026: chủ dự án tạo bằng Adobe Firefly Generate Sound Effects, chỉ model Adobe, dùng thương mại, không model đối tác, không phát lại/bán file thô hoặc gói âm. **Claude bổ sung bản lưu điều khoản Adobe có ngày và URL chính thức**. Codex không dùng mạng và chưa kiểm điều khoản; không ghi giả rằng đã có bản lưu Adobe.

## Phạm vi và việc bỏ qua

Không sửa `games/**`, `shared/**`, `keys/**`, `critic/**`, render/release/chain, Tu Tiên hoặc tài liệu của làn khác. Không cài gói Python, không gọi mạng, không chạy build/test game, dev server, trình duyệt hay bất kỳ lệnh Git ghi nào. Không tạo ảnh; không có WAV/OGG/MP3 trong docs hoặc đường Git của phiếu. Toàn bộ âm và cache thử nằm ở `tmp/firefly-ingest/` đã xác nhận bị Git bỏ qua.

Chưa nhận WAV thật từ chủ dự án; chưa nghe duyệt, chưa gắn game, chưa release thật và chưa lưu điều khoản Adobe vì đó là bước Claude/điều phối sau phiếu. Chủ dự án cần nghe nguồn thật sau ingest; điều phối cần chốt đường xuất tạm trước khi release.

Ảnh chụp trạng thái đầy đủ ở [status-before.txt](217/status-before.txt) và [status-after.txt](217/status-after.txt). Repo có agent khác chạy đồng thời: phần chênh trạng thái toàn repo có thể gồm các file mới của 195/197/202; giữ nguyên và ghi tách trong [scope.json](217/scope.json), không nhận là thay đổi của 217. Mọi đường **217 tự ghi** đều thuộc danh sách cho phép; không thể ép phần chênh toàn repo chỉ còn phiếu này bằng cách xóa việc của agent khác.

## Từng đường đã đổi của phiếu 217

Danh sách chính xác được ghi bên dưới và trong `217/scope.json`; `tmp/firefly-ingest/**` là dữ liệu thử bỏ qua bởi Git.

<!-- PATHS -->

- `docs/changelog/2026-10-30-audio-lab-firefly-ingest.md`
- `docs/codex-queue/217-report.md`
- `docs/codex-queue/217/demo.json`
- `docs/codex-queue/217/demo.py`
- `docs/codex-queue/217/demo.txt`
- `docs/codex-queue/217/licence-after.txt`
- `docs/codex-queue/217/licence-before.txt`
- `docs/codex-queue/217/run-tests.py`
- `docs/codex-queue/217/scope.json`
- `docs/codex-queue/217/status-after.txt`
- `docs/codex-queue/217/status-before.txt`
- `docs/codex-queue/217/test-summary.json`
- `docs/codex-queue/217/tests-after.txt`
- `docs/codex-queue/217/tests-before.txt`
- `docs/codex-queue/217/tests-context-red.txt`
- `docs/codex-queue/217/tests-existing-context-keys.txt`
- `docs/codex-queue/217/tests-loop-red.txt`
- `docs/codex-queue/217/tests-new.txt`
- `docs/codex-queue/217/tests-red.txt`
- `docs/codex-queue/217/tests-runtime-red.txt`
- `docs/codex-queue/217/verify.py`
- `tools/audio-lab/build/licence_check.py`
- `tools/audio-lab/build/policy.py`
- `tools/audio-lab/build/tests/test_build_firefly_licence.py`
- `tools/audio-lab/common/launch.py`
- `tools/audio-lab/firefly/README.md`
- `tools/audio-lab/firefly/__init__.py`
- `tools/audio-lab/firefly/__main__.py`
- `tools/audio-lab/firefly/cli.py`
- `tools/audio-lab/firefly/licences/adobe-firefly-owner-2026-10-29.txt`
- `tools/audio-lab/firefly/listening.py`
- `tools/audio-lab/firefly/pipeline.py`
- `tools/audio-lab/firefly/tests/test_firefly.py`
- `tools/audio-lab/pytest.ini`
