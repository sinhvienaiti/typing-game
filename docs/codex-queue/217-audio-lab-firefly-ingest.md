# Phiếu 217 · Ba game (Audio Lab) · Nhận âm Firefly: ingest, listen, status và lớp giấy phép Adobe Firefly

**Nguồn:**
- `docs/HANDOFF_CURRENT.md` §3, hàng "Âm thanh: đường Firefly": làn FF "dựng bước `run.sh firefly ingest` / `listen`"; "Chủ dự án thả WAV vào `~/AudioLab/inbox/firefly/<game>/<mã>/`; điều phối chạy ingest, gửi bản nghe 20 s, gắn vào game sau khi chủ dự án duyệt". Bước này chưa dựng: `tools/audio-lab/firefly/` chưa có.
- Quyết định của chủ dự án 29/10 (cùng hàng đó): Adobe cho dùng thương mại với model của Adobe; không dùng model đối tác; không bán lại gói.
- `tools/audio-lab/build/policy.py` chưa có lớp giấy phép cho âm Firefly. Vì vậy `build render` và `release` sẽ từ chối file của chủ dự án như giấy phép lạ (`build/README.md`).
- Chủ dự án 30/10: "tăng thêm việc cho codex cho tôi".

Không trùng 189 (chỉ bộ phím), 182 hay 190.

**Báo cáo:** `docs/codex-queue/217-report.md` (tiếng Việt), thư mục `docs/codex-queue/217/` (chỉ JSON, TXT, MD và script; không file âm).

**Làn:** P10, chạy sau 212 (để đọc định dạng danh sách nếu đã có). Không chờ 213–216: không phiếu nào trong đó sửa `tools/audio-lab/`.

**Sau phiếu này:** Claude duyệt mã, xác nhận lớp giấy phép, commit. Khi chủ dự án thả WAV, điều phối chạy ingest ngoài sandbox và gửi bản nghe.

## Nơi làm

- Repo cha, thư mục gốc (`.`), nhánh `feat/space-typing-admin-uiux`. Ghi `git status --short -uall` lúc bắt đầu vào `217/status-before.txt`. Repo đang có sửa dở của làn khác: không đụng chúng.
- Chỉ được ghi các đường sau:
  - `tools/audio-lab/firefly/` (mới): mã, `README.md`, `tests/`, `licences/adobe-firefly-owner-2026-10-29.txt`;
  - `tools/audio-lab/build/policy.py`: lớp giấy phép mới;
  - `tools/audio-lab/build/licence_check.py`: chỉ một nhánh cho điều kiện của lớp mới;
  - `tools/audio-lab/build/tests/test_build_firefly_licence.py` (mới);
  - `tools/audio-lab/common/launch.py`: một dòng `"firefly": "firefly"` trong `ENTRYPOINTS`;
  - `tools/audio-lab/pytest.ini`: thêm `firefly` vào `testpaths`;
  - `docs/changelog/<ngày>-audio-lab-firefly-ingest.md`;
  - báo cáo, thư mục `217/`, và `tmp/firefly-ingest/` (git bỏ qua) cho fixture, cache và đầu ra chạy thử.

## Đọc trước

- `tools/audio-lab/build/README.md`; `build/recipe.py`, `render.py`, `release.py`, `ledger.py`, `licence_check.py`, `policy.py`, `sources.py` (cách dòng sổ và bản lưu giấy phép `copies` đi theo lớp, rồi qua `licenceCopies` của `render.json` tới `ledger.copy_licence_texts` khi `release`); schema trong `build/schemas/` (`recipe`, `sources`, `licences`).
- `tools/audio-lab/run.sh`, `common/env.sh`, `common/launch.py`: venv nằm ở `$AUDIOLAB_HOME/.venv`, `launch.py` đặt `sys.pycache_prefix` dưới `$AUDIOLAB_HOME/cache`.
- `tools/audio-lab/critic/hygiene.py` (cổng L1, `gate(..., stage="raw" | "final")`, `UNFIXABLE`).
- `tools/audio-lab/keys/firefly.py`, `keys/firefly_build.py` (phiếu 189): cách tách cú theo onset, hàm `mp3()`, chuỗi `LICENCE` ở dòng 28. Chỉ đọc và import; không sửa `keys/**`.
- `tools/audio-lab/context/README.md`, `context/scenes.py`, `ts_scenes.py`, `td_scenes.py`: bản trộn như trong trận.
- Thẻ spec `tools/audio-lab/specs/<game>/<id>.yaml`: `duration` (`target_ms`, `min_ms`, `max_ms`), `loudness.proposal` (`metric`, `target`, `true_peak_max_dbtp`), `playback` (`mode`, `channels`, `min_gap_ms`), `variants`, `randomisation.group`.
- Danh sách của 212/213, nếu đã có: `docs/games/audio/firefly/*.json`. Đọc định dạng thật của file; không đoán. Chưa có thì dùng thẻ spec và ghi lại trong báo cáo.
- `docs/codex-queue/189/run-tests.py`: mẫu chạy test trong sandbox.

## Việc

Test trước, mã sau. Chú thích tiếng Anh. Mọi đường inbox và đầu ra là tham số bắt buộc. Không có đường mặc định trỏ vào `~/AudioLab`.

1. **`run.sh firefly ingest --game G [--id X] --inbox DIR --out DIR [--run NAME] [--list FILE]`**
   - Đọc `<inbox>/<game>/<id>/*.wav`. Inbox chỉ đọc: không sửa, đổi tên, chuyển hay xóa. Kiểm SHA-256 mỗi file trước và sau.
   - Thư mục id không có trong danh sách hay thẻ spec thì bỏ qua, ghi lý do. File không phải WAV thì bỏ qua, ghi lý do.
   - **Tách take**, cấu hình được bằng tham số:
     - `--split auto|onset|whole`. `auto`: thẻ có `playback.mode: loop` hay `source_class` là ambience, music thì `whole` (cả file là một take); còn lại `onset`.
     - `--threshold-db` (gợi ý −35 dB dưới đỉnh file), `--min-gap-ms` (gợi ý 150), `--pre-ms` (gợi ý 5), `--tail-floor-db` (gợi ý −60 dB dưới đỉnh take). Ghi giá trị đã dùng vào `takes.json`.
     - Mỗi take cắt đúng mẫu từ file gốc vào `<out>/<game>/<id>/takes/<id>-tNN.wav`, cùng định dạng gốc, không xử lý gì thêm.
   - **Cổng L1** trên từng take: `critic.hygiene.gate(..., stage="raw")`. Take trượt một kiểm trong `UNFIXABLE` (clip, đỉnh phẳng, im lặng) thì loại. Không đổi ngưỡng trong `critic/`.
   - **Loại take chồng:** cú sau đến trước khi take tắt 40 dB.
   - **Xếp hạng:** một bảng trọng số duy nhất trong mã. Thành phần: lệch độ dài so với `duration.target_ms`, độ lặng trước onset, nền sau đuôi. Ghi từng thành phần và điểm vào `takes.json`.
   - **Chọn:** lấy N = `variants.target` của thẻ, không cặp nào có tương quan dạng sóng > 0,95 (như 189). Thiếu take thì dựng số có được và ghi "dưới min" nếu < `variants.min`. Không nhân bản hay đổi cao độ để bù.
   - **Công thức** (`audiolab.recipe/1`), một file mỗi id:
     - một lớp; `source.file` là take 1; `vary.swap` là các take còn lại; `swapMode: "cycle"`, nên biến thể n dùng take n;
     - `source.ledger` là dòng sổ Firefly của take (mục 4);
     - `group`, `channels`, `chain.normalise`, `chain.limiter`, `chain.maxLengthMs`, `loop` lấy từ thẻ;
     - `export.path` lấy từ danh sách nếu có; không thì `firefly/<id>` và ghi trong `description` rằng đây là đường tạm.
   - **Dựng:** gọi `build.render` với `--spec` là thẻ, đầu ra `<out>/<game>/<id>/<run>/`. Mỗi lần chạy có `masters/`, `runtime/*.ogg`, `render.json`, `SOURCES.json`, `licences.rows.jsonl`, `manifest.fragment.json`, `recipe.json`.
   - **Cổng final:** `gate(..., stage="final")` trên từng master. Biến thể bị chặn thì giữ file để xem, đánh dấu id "chặn".
   - Mã thoát: 0 khi mọi id đạt; 1 khi có id chặn hay lỗi; 2 khi sai tham số.
2. **`run.sh firefly listen --game G [--id X] --out DIR [--slot sid=FILE ...]`**
   - Mỗi id một `<out>/listen/<game>/<id>-20s.mp3` (192 kbps, dùng cách của `firefly_build.mp3`) và một `.json` cùng tên.
   - Dài 20,0 s ± 50 ms; tắt dần 50 ms cuối, không cụt.
   - **Chế độ `context`:** khi một kịch bản trong `context/` có chỗ cho id. Dùng `--focus <id>`; chỗ khác im, trừ khi có `--slot`. Giọng đọc chỉ đọc từ cache có sẵn. Thiếu file giọng thì không ghi giọng mới, chuyển sang `sequence`.
   - **Chế độ `sequence`:** các biến thể lần lượt; khoảng cách = max(`min_gap_ms`, độ dài + 400 ms); mức ở giữa `mix_target` của thẻ.
   - JSON ghi chế độ, kịch bản, dòng thời gian, LUFS, đỉnh thật.
3. **`run.sh firefly status --game G --inbox DIR --out DIR [--list FILE] [--json FILE]`**
   - Danh sách id lấy từ `--list` (danh sách 212/213) hay thẻ spec của game.
   - Mỗi id một hàng: số file trong inbox, lần chạy mới nhất, take tìm thấy, qua cổng, được chọn, số biến thể so với thẻ, kết luận cổng final, có MP3 nghe chưa.
   - Liệt kê riêng id lạ trong inbox và file bị bỏ qua.
   - In bảng ra màn hình; `--json` ghi file.
4. **Lớp giấy phép** trong `policy.py`:
   - tên gợi ý `LicenseRef-Adobe-Firefly-owner`, `cond: "adobe-model"`, `attribution: False`;
   - `url` trỏ tới `licences/adobe-firefly-owner-2026-10-29.txt`, như `LicenseRef-owner-recording`;
   - chú thích: `owner decision 29/10, Claude confirms` (docstring nói bảng chỉ đổi khi chủ dự án duyệt).
   - File ghi chú (tiếng Anh): ai tạo, ngày 29/10/2026, Adobe Firefly Generate Sound Effects, chỉ model của Adobe, dùng thương mại, không model đối tác, không phát lại hay bán file thô. Ghi rằng bản lưu có ngày của điều khoản Adobe do Claude thêm (Codex không có mạng).
   - **Dòng sổ của mỗi take:** `kind: "source"`, `origin: "generated"`, `licence` là lớp mới, `licenceCopy` là `licences/adobe-firefly-owner-2026-10-29.txt` (tương đối với `art-src/audio/` như mọi dòng khác; bản gốc ở `tools/audio-lab/firefly/licences/`, đi qua `copies` để `release` chép), `commercial_ok: true`, `attribution_required: false`, `raw_redistribution_allowed: false`, `ai_input_allowed: true` (chỉ bộ chấm chạy trên máy; ghi vào báo cáo để Claude xác nhận), `generator: "Adobe Firefly Generate Sound Effects"`, `model` (mặc định `Adobe Firefly Audio Model`, đổi bằng `--model`), `author: "project owner"`, `derivedFrom` (SHA-256 và tên file gốc, `startMs`, `endMs`), `prompt` nếu danh sách có. Ngày lấy từ mtime file gốc, hay `--date`.
   - **Nhánh trong `licence_check.py`** cho `cond == "adobe-model"`: báo lỗi khi thiếu `model`, khi `model` không khớp danh sách cho phép (chỉ model của Adobe, so khớp từ đầu chuỗi), hay khi `raw_redistribution_allowed` là true. Không sửa gì khác ở file đó.
5. **README** `tools/audio-lab/firefly/README.md` (tiếng Việt): ba lệnh, tham số tách, bố cục đầu ra, lệnh mẫu cho điều phối ngoài sandbox:
   `bash tools/audio-lab/run.sh firefly ingest --game dragon-hold --inbox ~/AudioLab/inbox/firefly --out ~/AudioLab/work/firefly`.
6. **Changelog:** `docs/changelog/<ngày>-audio-lab-firefly-ingest.md`.

## Test (viết trước mã)

Fixture sinh lúc chạy test: WAV 48 kHz stereo 16-bit, khoảng 12 s, nhiều cú (dùng `build/tests/helpers.impact()`). Không file âm nào vào Git.

1. Tách: 6 cú ở onset đã biết cho 6 take, onset lệch ≤ 2 ms; `--min-gap-ms` lớn thì gộp; `whole` cho 1 take.
2. Chồng: cú thứ hai đến sau 40 ms thì bị đánh dấu, không được chọn.
3. Cổng: cú đỉnh phẳng bị loại ở cổng raw; file im lặng cho 0 take, `status` ghi rõ.
4. Xếp hạng: chọn đúng N; một cú lặp lại y hệt chỉ được chọn một lần.
5. Công thức hợp lệ theo `recipe.schema.json`; có `source.file`, dòng sổ đúng lớp, `swapMode: "cycle"`.
6. Đầu ra đủ file; cổng final đạt; LUFS-M max trong ±0,5 dB của mức đích (hay `idLevel` mà build báo); đỉnh thật ≤ −1 dBTP; độ dài ≤ `max_ms`.
7. Chạy lại: SHA-256 master và OGG giống hệt.
8. Inbox: mã băm và mtime không đổi.
9. Không ghi ra ngoài `--out`: gọi ba lệnh trong tiến trình test (hàm `main(argv)` của `firefly`, không qua `run.sh`, vì venv nằm dưới `AUDIOLAB_HOME`), với `AUDIOLAB_HOME` và các đường của `common.env` (`HOME`, `CACHE`, `WORK`, `STAGING`…) trỏ vào một thư mục tạm rỗng dưới `tmp/firefly-ingest/`. Sau ba lệnh thư mục đó vẫn rỗng.
10. `listen`: MP3 giải mã dài 20,0 s ± 50 ms; JSON ghi đúng chế độ.
11. `status`: id có take, id chưa có, id lạ, file không phải WAV.
12. `build/tests/test_build_firefly_licence.py`: `classify()` cho lớp mới là `allowed`; render rồi `release` vào `art-src` và `public` tạm, `licence-check` 0 lỗi; dòng có `model` đối tác thì lỗi; thiếu `model` thì lỗi; `raw_redistribution_allowed: true` thì lỗi.

Chạy test qua wrapper `docs/codex-queue/217/run-tests.py` theo mẫu 189. Cache numba, matplotlib và pytest, `--basetemp`, `sys.pycache_prefix` đều nằm trong `tmp/firefly-ingest/`.

## Cấm

- Mọi lệnh git có ghi; mạng; dev server, trình duyệt.
- Ghi ra ngoài repo (`~/AudioLab`, `~/Downloads`…): sandbox đã từ chối ở phiếu 189.
- Sửa `games/**`, `shared/**`, `keys/**`, `critic/**`, `build/render.py`, `release.py`, `chain.py`; đụng Tu Tiên.
- Nới hay đổi ngưỡng L1; thêm gói Python mới.
- Đưa WAV, OGG, MP3 hay ảnh vào Git hoặc vào `docs/`.
- Tổng hợp âm hay đổi cao độ để bù take thiếu.

## Kiểm (ghi số)

1. Trước khi sửa: chạy cả bộ test Audio Lab qua wrapper. Ghi số qua, lỗi, bỏ qua vào `217/tests-before.txt`.
2. Sau: số test mới qua và lỗi; cả bộ qua, lỗi, bỏ qua (`217/tests-after.txt`). Không test nào trước qua mà nay lỗi.
3. `217/demo.py` sinh fixture vào `tmp/firefly-ingest/inbox/` cho hai id thật: `dragon-hold/fire.impact.a` (một phát, có chỗ trong `dh-cast-chain`) và `dragon-hold/amb.forest` (vòng lặp). Chạy ingest, listen, status. Ghi `217/demo.json`: mỗi id số take tìm thấy, qua cổng, được chọn; số biến thể so với thẻ; LUFS-M max, đỉnh thật, độ dài từng biến thể; kết luận cổng final; chế độ và độ dài MP3.
4. Chạy ingest lần hai: số file master và OGG giống SHA-256 trên tổng.
5. Inbox mẫu: mã băm và mtime trước, sau giống hệt.
6. `pnpm audio:licence-check` (mặc định): kết quả như trước khi sửa. Sandbox chặn thì ghi lý do.
7. `git status --short -uall` sau (`217/status-after.txt`). Phần chênh so với `status-before.txt` chỉ là các đường ở mục Nơi làm. Báo cáo liệt kê đúng từng đường đã đổi.
8. Mục "Claude cần xác nhận": tên lớp, điều kiện `adobe-model`, danh sách model cho phép, `ai_input_allowed`, URL và file ghi chú.

**Lưu ý:** hình dạng file Firefly (WAV 48 kHz stereo, khoảng 12 s, nhiều cú mỗi file) suy từ lô bàn phím của chủ dự án. Vì vậy tách take phải cấu hình được, và báo cáo ghi rõ mặc định đã chọn và lý do.

**Xong khi:** ba lệnh chạy được trên fixture; lớp giấy phép có và `licence-check` nhận nó; test mới xanh; bộ test cũ không lùi; báo cáo liệt kê đúng đường đã đổi. Claude duyệt rồi commit.
