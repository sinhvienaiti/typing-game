# Bảng Nghe (Listening Board) v1

Trang web chạy trên máy để chủ dự án **nghe mù** các ứng viên âm thanh và chấm điểm. Hợp đồng: mục 7 của [`docs/games/AUDIO_PIPELINE.md`](../../../docs/games/AUDIO_PIPELINE.md), cùng mục 4.6 (bản dò, cặp mốc), 5.3 (độ ngẫu nhiên khi chơi) và 5.4 (nhãn).

- Chỉ nghe ở `127.0.0.1:3191`. Cổng bận thì dùng `3192` và in cảnh báo. Không mở ra mạng, không tải gì từ Internet: trang chạy offline.
- Server dùng `http.server` của thư viện chuẩn Python. Phần đo độ to dùng numpy, scipy, soundfile, pyloudnorm trong venv chung.
- Trang chỉ biết nhãn A, B, C… Đường dẫn file, vai trò (top, distinct, probe), cờ cặp mốc và điểm máy không bao giờ tới trình duyệt. Thẻ ảnh và số đo bị server chặn (HTTP 403) cho đến khi id đó đã được chấm.

## Chạy

```bash
pnpm audio:board                                   # mọi phiên trong ~/AudioLab/review/*/sessions/
pnpm audio:board --game dragon-hold --batch b1     # lọc theo game và lô
bash tools/audio-lab/run.sh board --session ĐƯỜNG/DẪN/phiên.json --open
bash tools/audio-lab/run.sh board demo --serve     # phiên demo bằng âm tổng hợp
bash tools/audio-lab/run.sh board calib-0a         # tạo 2 phiên lô 0a từ 40 âm thử (mục 4.6 bước 1)
bash tools/audio-lab/run.sh board calib-0a --critic-dir ~/AudioLab/work/_critic/<lần chạy>   # dùng thẻ của bộ phê bình mới
bash tools/audio-lab/run.sh board from-critic ~/AudioLab/work/<game>/<id>/r1 --game dragon-hold --batch b1 --session s1
                                                   # phiên từ danh sách nghe của bộ phê bình (_batch.json)
bash tools/audio-lab/run.sh board make-session OUT... --game G --batch B --session S [--anchors N]   # tên khác của from-critic
bash tools/audio-lab/run.sh board calib-0a --critic-dir DIR --batch 0a-them   # đặt nhãn lô riêng cho bộ hiệu chỉnh đầy đủ
bash tools/audio-lab/run.sh board check            # kiểm file phiên
bash tools/audio-lab/run.sh board prepare          # in độ to đo được và mức chỉnh của từng file
bash tools/audio-lab/run.sh board summary --game dragon-hold   # tóm tắt ratings.jsonl theo vai trò
bash tools/audio-lab/run.sh board browser-check    # thử bằng Chrome thật, chụp 1280x720 và 1920x1080
```

Tùy chọn chung: `--review-root DIR` (mặc định `~/AudioLab/review`), `--port N` (cổng cố định, không tự đổi), `--verbose`.

## Dữ liệu

| Ở đâu | Có gì |
|---|---|
| `~/AudioLab/review/<game>/sessions/<phiên>.json` | File phiên (do Claude hoặc script lập danh sách nghe viết) |
| `~/AudioLab/review/<game>/ratings.jsonl` | Điểm chấm, **chỉ ghi thêm**, mỗi lượt một dòng |
| `~/AudioLab/review/<game>/state/<phiên>.json` | Trạng thái để làm tiếp: thời gian đã nghe, thiết bị, vị trí, cặp mốc đã chọn |
| `~/AudioLab/cache/board/measure-v1.json` | Độ to đã đo, theo SHA-256 của file |
| `~/AudioLab/work/_board-check/shots/` | Ảnh chụp của lần thử bằng trình duyệt gần nhất |

`game` là tên thư mục, ví dụ `dragon-hold`, `typing-defense`, `typing-survival`, `space-typing`; `_demo` cho phiên demo và `_calib` cho lô 0a.

## Từ bộ phê bình tới phiên nghe

`from-critic` đọc `_batch.json` của một hay nhiều lần chạy `run.sh critic ... --out DIR`. Với mỗi nhóm xếp hạng, danh sách nghe của mục 4.6 bước 2 (`listen`: `top`, `distinct`, `probe`) thành một id. Các mục của danh sách nghe là `stem` duy nhất của lần chấm (`gun.xung-v1`, `gun.xung-v1__2`), nên hai file trùng tên ở `r1/masters` và `r2/masters` không lẫn nhau; kết quả cũ ghi theo tên file vẫn đọc được, trừ khi tên đó trùng (khi ấy lệnh báo lỗi và yêu cầu chấm lại). Đường dẫn file, JSON và thẻ ảnh lấy từ JSON của từng file; `family`, `group`, mô tả (`group_name_vi`) và nhịp chơi (`rate_hz` → khoảng cách của "Lặp 20 lần") lấy từ `spec`. Id không còn bản nào qua cổng L1 bị bỏ và được in ra. Hơn 10 id thì tách thành `s1-1`, `s1-2`… (mục 7). File phiên đã có thì không ghi đè nếu thiếu `--force`. Tùy chọn: `--id` (chỉ lấy id này), `--title`, `--seed`, `--max-items`.

Nhóm của bộ phê bình (`key_ok`, `hit_small`, `explosion`, `ambience`…) được đổi sang luật lặp tương ứng của mục 5.3 (xem `group` ở mục sau), nên file phiên dùng thẳng tên nhóm đó được.

## File phiên (`audiolab.board.session/1`)

```json
{
  "schema": "audiolab.board.session/1",
  "session": "s3", "game": "typing-survival", "batch": "b1",
  "title": "Tuyến Cuối · lô 1 · phiên 3",
  "seed": 20261024, "max_minutes": 20, "anchors": 4,
  "items": [
    {"id": "gun.xung", "family": "ban", "desc": "Súng xung, phát 5 lần mỗi giây",
     "probe": true,
     "candidates": [
       {"file": "audiolab:work/typing-survival/gun.xung/r1/c07.wav", "role": "top",
        "card": "audiolab:work/typing-survival/gun.xung/r1/c07.png",
        "critic": "audiolab:work/typing-survival/gun.xung/r1/c07.json"},
       {"file": "audiolab:work/typing-survival/gun.xung/r1/c12.wav", "role": "distinct"},
       {"files": ["…/c03-v1.wav", "…/c03-v2.wav"], "role": "probe"}
     ]}
  ]
}
```

- Đường dẫn: tuyệt đối, `~/…`, `audiolab:<đường dẫn trong ~/AudioLab>`, hoặc tương đối so với file phiên.
- Ứng viên có thể là một chuỗi (đường dẫn), một object có `file`, hoặc `files` (một bộ biến thể; "Một mình" phát lần lượt từng biến thể, "Lặp 20 lần" xoay vòng).
- `card` và `critic` có thể bỏ trống: bảng tự tìm `<tên>.critic.json` / `<tên>.json` cạnh file âm, rồi trong `critic_dir` (của item, rồi của phiên; một chuỗi hoặc danh sách thư mục, ví dụ thư mục `--out` của `run.sh critic`). Thẻ ảnh: trường `card` trong JSON của bộ phê bình, nếu không có thì `<tên>.png` / `<tên>.card.png` ở cùng các chỗ đó.
- JSON của bộ phê bình có `sha256` (hoặc `file.sha256`) khác file âm thì bị bỏ, kèm thẻ ảnh của nó: số đo cũ không bao giờ hiện cạnh âm mới.
- Có `card_blind` (bộ phê bình chạy với `--blind-cards`) thì bảng dùng thẻ mù đó: chỉ số đo và lỗi vệ sinh L1; không tên file, định dạng, kết luận, điểm, thanh mục tiêu L2 hay cờ L1b/L4/L5.
- `reveal`: `"item"` (mặc định) mở thẻ ảnh và số đo ngay sau khi chấm id đó; `"end"` chỉ mở khi đã chấm **mọi** id của phiên (API `reveal`, `card` trả 403 trước đó). Lô 0a và các phiên hiệu chỉnh dùng `"end"`, để phán quyết của máy không dạy tai ở các id sau.
- `source_id` (tùy chọn): tên thật của item có id trung tính (phiên hiệu chỉnh dùng `calib-1`, `calib-2`…). Trường này chỉ ghi vào dòng điểm, không gửi lên trang.
- `role` mặc định theo danh sách nghe của mục 4.6: bản 1 `top`, bản 2 `distinct`, bản cuối `probe` khi item có `"probe": true`, còn lại `other`. Lượt biến thể: `variant`.
- `mode`: `hero` (mặc định), `variants`, `pair`, `style`. `contexts`: `alone`, `loop`, `small`, `mix` (`mix` được thay bằng `loop` cho đến giai đoạn 3). Mặc định theo họ âm như mục 7.
- `family`: 8 họ chung của mục 4.6 (`phim-ui`, `thuong`, `ban`, `trung`, `no`, `chet`, `sinh-vat`, `nen`). `group` (tùy chọn) chọn luật lặp chi tiết hơn: `phim-dung`, `phim-sai`, `ui`, `thuong-tu`, `thuong-hiem`, `ban`, `trung-nho`, `trung-nang`, `no`, `chet-bay`, `chet-lon`, `sinh-vat`, `nen`, hoặc tên nhóm của bộ phê bình (`board/config.py`, `CRITIC_GROUP_PRESET`). Chỉ luật `nen` (nền lặp) phát liền mạch; báo nguy và stinger lặp theo nhịp, không đổi cao độ.
- `loop` (tùy chọn) ghi đè: `interval_ms`, `jitter`, `cents`, `db`, `offset_ms`, `gap_ms`, `avoid`, `count`, `seamless`, `preset`. Không ghi `count` thì item phát cách nhau từ 1 s trở lên lặp 8 lần, còn lại 20 lần: một nốt thưởng 1,5 s lặp 20 lần mất 30 s cho mỗi bản. Nút bối cảnh hiện đúng số lần ("Lặp 8 lần").
- `anchors: N` (mặc định 4, `0` để tắt) chèn N cặp mốc lấy từ các phiên trước của cùng game (bản tốt nhất và bản kém nhất của một lượt cũ, chỉ khi file còn nguyên SHA-256). Cặp mốc được chọn lúc chủ dự án mở phiên lần đầu (không phải lúc server khởi động) và ghi vào file trạng thái, nên lần mở sau vẫn giống hệt. Phiên đã có điểm mà chưa có cặp mốc thì không bị chèn thêm, để vị trí làm tiếp không đổi. Cặp mốc giữ chế độ và mô tả của id gốc: trang không biết item nào là cặp mốc. Phiên demo và lô 0a đặt `anchors: 0`.
- Nhãn A, B, C xếp ngẫu nhiên cho từng item, cố định theo `seed` và khóa item.

## Cân độ to

Mỗi file có một mức chỉnh (`gainDb`) để mọi bản trong cùng item nghe to như nhau:

1. Nếu **mọi** file của item có JSON của bộ phê bình với cùng một khóa: dùng LUFS-M max (`metrics.lufs_m_max` của bộ phê bình, hoặc `lufs_momentary_max` của bản thử; như mục 4.3.3 và 7), nếu không có thì độ to ngắn hạn (`lufs_s_max`, `lufs_short_term_max`).
2. Nếu không: bảng tự đo LUFS-M max (lọc K, cửa sổ 400 ms, đệm im lặng như bộ phê bình).
3. Đo LUFS không được thì dùng RMS cửa sổ 400 ms.

Mức đích là −23 LUFS-M (`target_lufs` trong file phiên). Cả item hạ xuống cùng nhau nếu cần, để không file nào vượt −1 dBTP sau khi chỉnh, và để bản nhỏ nhất chỉ cần tăng tối đa 36 dB (item không xuống dưới −32 LUFS-M vì lý do này). Bản gần như im lặng mà vẫn không theo kịp thì dòng điểm ghi `loudness_short_db` > 0, và `prepare` in cảnh báo. Nguồn đo được ghi vào trường `loudness` của mỗi dòng điểm.

- **Độ to đầu tiếng (100 ms):** cân theo LUFS-M (400 ms) vẫn để một bản có đầu tiếng sáng (kẻng) to hơn bản nở chậm (cồng) tới 4 dB trong 100 ms đầu. Khi độ to cửa sổ 100 ms của các bản còn lệch quá 2 dB sau khi cân, bảng cân theo trung bình của LUFS-M và LUFS 100 ms (nguồn ghi thêm `+100ms`). Độ lệch còn lại ghi vào `loudness_spread_100ms_db` của dòng điểm, để khi phân tích còn trừ đi được. Lô 0a: `leak` 4,1 → 2,1 dB, `ui-pick` 4,2 → 2,1 dB, `wave.horn` 3,1 → 1,6 dB.
- **Id phát nhỏ hơn mức chung:** khi giới hạn đỉnh thật buộc cả item phát dưới −23 LUFS-M hơn 3 dB, mô tả của item có thêm một câu dặn chủ dự án đừng chỉnh âm lượng máy và đừng gắn "quá nhỏ" vì bảng (dòng điểm có `quiet_db`).
- **Mọi bản phát ra dưới dạng WAV:** file OGG được giải mã rồi gửi như WAV số thực. Trước đây bản gốc Kenney (`audio/ogg`) đứng cạnh các bản làm hỏng (`audio/wav`), nên chỉ cần xem header là biết bản nào là gốc.

## Bối cảnh nghe

| Bối cảnh | Cách phát |
|---|---|
| Một mình | Phát riêng bản đang chọn |
| Lặp 20 lần (8 lần với âm phát thưa) | 20 lần, hoặc 8 lần khi item phát cách nhau từ 1 s, theo nhịp chơi thật và độ ngẫu nhiên của mục 5.3 (cao độ đổi bằng `playbackRate` như kit, mức ±dB, lệch thời điểm, khoảng nghỉ tối thiểu, không lặp lại biến thể vừa phát). Mẫu ngẫu nhiên giống hệt cho mọi bản của cùng item, nên chỉ âm là khác. Nền (`nen`) lặp liền mạch để nghe mối nối |
| Loa nhỏ | Như "Một mình", qua bộ lọc cao 200 Hz (`BiquadFilter`) |
| Trong trận | Tắt, có từ giai đoạn 3 (Bảng Nghe v2) |

## Phím tắt

| Phím | Việc |
|---|---|
| `Space` | Phát hoặc dừng bản đang chọn. Lượt biến thể + "Lặp 20 lần": phát cả bộ |
| `1`–`9` | Chọn bản A, B, C… và phát |
| `←` `→` | Chọn bản, không phát |
| `⇧1`–`⇧5` | 1–5 sao cho bản đang chọn (`⇧0` xóa) |
| `V` | Bản tốt nhất. Không bấm thì bản có nhiều sao nhất được tự chọn khi không hòa (`pick_auto`) |
| `0` | Không bản nào đạt |
| `X` | Lượt biến thể: bỏ hoặc giữ bản đang chọn |
| `H` `G` `C` `D` `R` `Y` `K` `T` `N` `M` `S` `L` `P` `E` `O` | hay, hợp game, chói, đục, rè/lỗi, yếu/mỏng, quá dài, quá to, quá nhỏ, chậm, sai chất liệu, lạc thể loại, nhàm khi lặp, rẻ tiền, khó nghe tiếng đọc |
| `↑` `↓` | Đổi bối cảnh |
| `Enter` | Lưu (thẻ ảnh và số đo hiện ra), Enter lần nữa sang id tiếp. `⇧Enter`: bỏ qua |
| `⌫` | Id trước |
| `/` | Ghi chú (gõ tiếng Việt được, Enter để lưu) |
| `I` | Phóng to thẻ ảnh và xem đủ số đo (sau khi chấm) |
| `?` | Trợ giúp |

Kế hoạch mục 7 ghi "A, B, C để phát; 1–5 để chấm". Bản này theo yêu cầu của làn: số để chọn bản, `⇧` + số để chấm sao, vì hai việc dùng chung hàng số.

## Một dòng `ratings.jsonl` (schema 1)

Giống ví dụ ở mục 7, thêm vài trường. Khóa của ứng viên là SHA-256 của file (bộ biến thể: SHA-256 của các SHA-256 nối lại).

| Trường | Ý nghĩa |
|---|---|
| `schema`, `kind` | `1`, `"rating"` |
| `ts`, `game`, `id`, `item`, `family`, `group`, `desc`, `batch`, `session`, `mode` | Định danh (`desc` để cặp mốc về sau hiện giống id gốc) |
| `context`, `contexts_heard`, `device` | Bối cảnh lúc lưu, các bối cảnh đã nghe, `headphones` hoặc `speakers` |
| `shown`, `order` | Ứng viên theo thứ tự trong file phiên, và nhãn đã hiện cho từng bản |
| `roles` | Vai trò (chỉ có trong file) |
| `stars`, `pick`, `pick_auto`, `none`, `tags`, `note` | Điểm của chủ dự án |
| `dropped` | Lượt biến thể: các bản bị bỏ |
| `anchor`, `anchor_of`, `probe` | Cặp mốc và nguồn của nó; item có bản dò |
| `listens`, `item_ms`, `session_ms` | Số lần nghe mỗi bản, thời gian trên item và cả phiên |
| `rev`, `revealed_before` | Lần chấm thứ mấy của item này; đã thấy thẻ trước khi chấm lại chưa |
| `files`, `gain_db`, `loudness`, `loudness_short_db`, `seed`, `board` | Đường dẫn (dạng `audiolab:…`, không lộ thư mục nhà), mức chỉnh, nguồn đo độ to, số dB bản nhỏ nhất còn thiếu, seed, phiên bản bảng |
| `loudness_spread_100ms_db`, `quiet_db` | Độ lệch độ to 100 ms còn lại sau khi cân; số dB item phát dưới mức chung |
| `reveal_at`, `source_id` | `item` hoặc `end` (thẻ mở khi nào); tên thật của id trung tính |

Dòng cuối của mỗi cặp (`session`, `item`) là kết quả hiện hành. Không sửa hay xóa dòng cũ.

## Kiểm thử

- `pnpm audio:test` chạy `board/tests/` (`test_server.py`, `test_make_session.py`, `test_review_fixes.py`: thẻ mở cuối phiên, id trung tính, chỉ WAV, độ lệch 100 ms, câu dặn id nhỏ, lặp 8 lần, danh sách nghe theo stem; cộng 1 test Chrome bật bằng biến môi trường): tạo phiên từ `_batch.json` của bộ phê bình, nhãn mù cố định theo seed, cân độ to (bản to hơn 10 dB bị hạ đúng 10 dB, bản rất nhỏ vẫn cân được), dùng số đo của bộ phê bình (định dạng bản thử và `audiolab.critic.file/1` qua `critic_dir`, bỏ JSON cũ theo SHA-256), số đo và cờ hiện sau khi chấm không có điểm máy, toàn bộ API, luật an toàn (Host, Origin, Content-Type, đường dẫn), đổi cổng khi bận, cặp mốc (chèn lúc mở, không chèn giữa phiên), phiên lô 0a.
- `AUDIOLAB_BROWSER=1 pnpm audio:test` hoặc `run.sh board browser-check`: dựng phiên demo, mở Chrome qua `tools/cdp-run.mjs` (bản chép nguyên của `shared/game-kit/tools/cdp-run.mjs`), chấm 2 id và một lượt biến thể chỉ bằng phím, kiểm `ratings.jsonl`, kiểm trang không lộ tên file trước khi chấm, kiểm trang không tràn màn hình, chụp ảnh ở 1280x720 và 1920x1080.

## Việc còn lại cho người ghép

- Khi `games/**` được ghi: chép `~/AudioLab/review/<game>/ratings.jsonl` sang `games/<game>/art-src/audio/review/ratings.jsonl` (mục 11), hoặc thêm chế độ ghi thẳng vào đó.
- Danh sách nghe của bộ phê bình đi vào bảng qua `board from-critic` (định dạng `_batch.json` và `audiolab.critic.file/1` ngày 2026-10-23). Nếu làn bộ phê bình đổi tên trường (`listen`, `files[].json`, `file.path`, `file.sha256`, `metrics.lufs_m_max`, `card`, `spec.rate_hz`), sửa `board/from_critic.py` và `board/loudness.py` cho khớp; test `test_from_critic_listening_list` và `test_critic_module_output` mô tả hợp đồng này.
- Thẻ PNG đầy đủ của bộ phê bình (`critic/card.py`) in tên file, điểm tổng và thứ hạng ở đầu ảnh; Bảng Nghe dùng thẻ mù (`--blind-cards`) thay cho nó. Phần số đo và cờ do bảng hiện chỉ gồm số đo và lỗi vệ sinh L1 (không còn cờ L1b, L4, L5); "Dải đục" không hiện với âm có cao độ, vì dải 200–500 Hz chứa nốt gốc.
- Bối cảnh "Trong trận" và chế độ "Cuối phiên" (đoạn mật độ, đoạn mỏi tai) chờ giai đoạn 3. Trước đó có thể đưa các đoạn này vào phiên như item `mode: "style"` với một ứng viên.
