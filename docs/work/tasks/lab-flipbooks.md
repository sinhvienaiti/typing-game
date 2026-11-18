# Việc: video Firefly tối 05/11 → flipbook cho lab, theo từng hệ (agent 1)

**Anh (05/11 18:30):** "tôi nghĩ bạn nên thêm 2 agent để xử lý cho hình ảnh vào lab dần đi cũng đc". Agent 1 làm phần tài nguyên; agent 2 (`tasks/lab-element-kits.md`) viết mã bộ chất. Hai việc chạy song song, chung một hợp đồng là manifest bên dưới.

## Đầu vào
- Video: `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/video/<job>/take<N>.mp4`, mỗi file kèm `take<N>.prompt.txt` (model, ảnh khung đầu, câu lệnh).
- Ý nghĩa từng việc: `docs/work/tasks/firefly-sprint-video.json` (danh sách đang chạy, trường `use`), `element-video-0511.json`, `element-video-0511b.json`, mục 3, 4, 7 của `docs/games/tu-tien/skills/PRODUCTION_LIST_2026-11-05.md`.
- **Hàng video Firefly vẫn chạy tới khoảng 23:00** (2 làn). Làm theo đợt: mỗi đợt lấy những bản đã có trên đĩa, bản mới tới thì đợt sau làm tiếp.
- Mỗi việc dùng `take1`, trừ khi anh đã chọn bản khác trong `docs/work/DECISIONS.md`.
- Bỏ các việc anh đã loại: `i2v-ult-water-profound-sea` và `i2v-ult-thunder-nine-heavens` (đôi mắt, cuộn giấy); tên có `style-` và `-w2` là đợt cũ, không làm.

## Công cụ
- `tools/vfx-flipbook/run.sh` (đọc đầu file): `ingest <game> <id>`, đầu vào ở `$VFXLAB_HOME/inbox/firefly/immortality-cultivation/<id>/<id>__vN.mp4`, đầu ra ở `$VFXLAB_HOME/out/immortality-cultivation/<id>/`. Python có numpy/scipy/Pillow: `~/AudioLab/.venv/bin/python` (mặc định của tool).
- Cấu hình từng clip: `tools/vfx-flipbook/immortality-cultivation.json` (`phase`, `aspect`, `loop`, `frames`, `cell`). Thêm mục mới, không sửa mục cũ.
- Định dạng manifest của lab: `src/view/skills/flipbook.ts` (`parseFlipbookManifest`, `FlipbookMeta`). Mẫu đang chạy: `art-src/lab/vfx/fire/manifest.json`.

## Ánh xạ việc → vai trò (hợp đồng với agent 2, không đổi tên)

| Việc video | `role` trong manifest | Ghi chú |
|---|---|---|
| `<hệ>-charge` | `charge` | gom vào, 1:1 |
| `<hệ>-release` | `release` | lóe ở người ra chiêu |
| `<hệ>-ribbon-loop` | `ribbon` | dải lặp ngang 16:9, `loop: true` |
| `<hệ>-sheath-loop` | `sheath` | dải dọc 9:16 quấn vũ khí, `loop: true` |
| `<hệ>-impact` | `impact` | trúng quái |
| `<hệ>-big-burst` | `burst` | nổ lớn |
| `<hệ>-ground-impact` | `groundImpact` | đòn đánh xuống đất (anh yêu cầu 17:08) |
| `<hệ>-sparkle` | `sparkle` | lớp lấp lánh, `loop: true` |
| `i2v-<hệ>-slash-arc` | `slash` | nhát chém lưỡi liềm, 16:9 |
| `i2v-<hệ>-ground-mark` | `groundMark` | dấu trên đất, nhìn từ trên |
| `i2v-pillar-*`, `i2v-ult-*` | `pillar`, `ultimate` | thư mục `art-src/lab/vfx/ult/` |
| `i2v-kiem-*`, `i2v-dao-*`, `i2v-thuong-*` | `weapon` | thư mục `art-src/lab/vfx/weapon/` |

Mã hệ (tên thư mục): `metal fire water thunder wind ice earth wood dark light poison blood void star`.

## Đầu ra
- `games/immortality-cultivation/art-src/lab/vfx/<hệ>/manifest.json` cùng atlas của hệ đó. Mỗi mục có thêm `role`, `job`, `take`, `source` (đường dẫn mp4).
- Hệ `fire`: chỉ **thêm** mục mới vào manifest có sẵn, không sửa mục cũ.
- Nền đen thì dùng chế độ `fire` (cộng sáng), như mẫu Hỏa.
- Media không vào Git (`art-src` bị bỏ qua).
- **Cho anh xem:** mỗi hệ một tấm ghép (mỗi vai trò một hàng khung hình) và một video xem trước dưới 30 MB, để ở `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-05/tu-tien/lab-flipbooks/`. Thư mục có `ABOUT.md`. Chạy `node scripts/review-index.mjs` sau khi thêm.

## Luật
- Không chạm các tab trình duyệt `seed`, `tab-3` tới `tab-7` (hàng Firefly, ChatGPT, Gemini đang chạy). Việc này không cần trình duyệt.
- Không sửa, chuyển hay xóa file video gốc. Không commit gì. Khung thô tự tạo thì dọn bằng `tools/capture-prune/prune.mjs`.
- Ghi tiến độ vào mục "Nhật ký" bên dưới sau mỗi đợt: hệ nào xong, bao nhiêu clip, lỗi gì.

## Xong khi
- Mọi bản video đã có của danh sách trên có atlas trong manifest đúng hệ.
- Tấm ghép và video xem trước từng hệ đã nằm trong thư mục cho anh xem.
- Đợt cuối chạy sau khi hàng video dừng (khoảng 23:00).

## Cách làm (agent 1, 05/11 18:50)
- Script chạy từng đợt: `~/AudioLab/.venv/bin/python /Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/lab-flipbooks/lab_batch.py build` (lấy mọi `take1.mp4` đã xong và chưa làm), rồi `... review` (tấm ghép và video từng thư mục), `... status`. Video gốc chỉ được liên kết (symlink) vào `inbox/` của công cụ, không đụng.
- Hàng 14 hệ + `ult` + `weapon`; id manifest bỏ tiền tố `i2v-` (ví dụ `water-slash-arc`, `ult-dark`, `kiem-guard-sword-dome`); atlas `<id>.atlas.png`, json `<id>.json` cạnh manifest. Mỗi mục: `role` (và `roles`), `job`, `take`, `source`, `mode`, `fps`, `cell`, `pivot`, `frames`, `loop`, `tileX`, `timing` (cho clip một lần: `peak` khung đỉnh, `holdEnd` khung cuối còn từ 60 % đỉnh trở lên, `endsHot` true khi clip gốc cắt đen cứng không có đuôi mờ; hiện chỉ `ice-ground-mark`, kit phải tự ăn mòn khung cuối), `flags`, `notes`.
- Mọi clip nền đen, nên `mode: "fire"` (cộng sáng, đen = không có năng lượng), atlas RGB không alpha. Clip `ribbon` là dải ghép ngang (`tileX: true`).
- Một việc khác với công cụ gốc: công cụ làm mờ đuôi theo kiểu lửa (xanh và lục tắt trước, đuôi ra đỏ) và ấm màu lõi trắng. Đúng cho Hỏa, sai cho nước, sét, băng. Nên chỉ Hỏa dùng nguyên công cụ; các hệ khác mờ giữ nguyên màu (`lab_batch.py` vá hai hàm `cool_fade`, `cool_dim` trong tiến trình riêng) và đặt `whiteFix: "off"` trong bảng `tools/vfx-flipbook/immortality-cultivation.json`. Mã công cụ không sửa. Sáng mai nên thêm tùy chọn này vào công cụ cho sạch.
- Kiểm bằng chính `parseFlipbookManifest` của lab (`validate-manifests.ts` cùng thư mục): 0 lỗi.
- Cỡ ô: 256×256 (vuông), 512×288 (dải, nhát chém, dấu đất), 180×320 (hào quang quấn vũ khí), 640×360 (cột trụ, tuyệt kỹ, hình vũ khí). Clip năm giây giữ rồi tan (nhát chém, dấu đất, cột trụ, tuyệt kỹ, hình vũ khí) lấy trọn 5 s: 6–8 khung/giây, lab trộn khung nên không giật.


## Cách xuất video 1080p cho chiêu lớn (để Codex làm thành công cụ)

**Vì sao:** atlas của `ult` và `expansion` là 32 ô 640×360 ở 6 khung/giây, còn nguồn Firefly là 1920×1080 ở 24 khung/giây, nên phím 8 và 9 nhìn mờ và giật. Lab phát thẳng video thay atlas cho các chiêu lớn; atlas giữ làm dự phòng. Bản chạy được để tham chiếu: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/lab-flipbooks/export_videos.py` (48 file, 2 phút 30 giây, 438 MB).

**1. Đầu vào (mọi thứ có sẵn trong mục manifest, không đoán):**

| Trường | Ý nghĩa |
|---|---|
| `source` | Đường dẫn video gốc tính từ gốc repo, đúng take đang dùng (`take` là số take) |
| `trim.start`, `trim.end`, `trim.step` | Đoạn nguồn mà atlas lấy: khung nguồn `start` tới `end - 1` (khung đếm ở 24 khung/giây), mỗi ô atlas cách nhau `step` khung nguồn |
| `sourceFps` | Tốc độ khung của nguồn (24). `fps` của mục là tốc độ phát atlas: `sourceFps / step` |
| `frames` | Số ô atlas |
| `timing.peak`, `timing.holdEnd` | Chỉ số **ô atlas** của khung đỉnh và khung cuối còn từ 60 % đỉnh trở lên (sau đó là phần tan) |
| `pivot` | Tâm lõi trong ô atlas (0–1 từ góc trên trái) |
| `<id>.json` cạnh manifest: `source.crop`, `source.width`, `source.height` | Hình chữ nhật đã cắt từ nguồn `[x, y, w, h]` (pixel nguồn) và kích thước nguồn |

**2. Tính đoạn cắt:**
- Đổi chỉ số ô atlas sang khung nguồn: `khungNguồn = trim.start + ô × trim.step`.
- **Đoạn xuất = từ `trim.start` tới hết `trim.end - 1`**, tức cả phần giữ và phần tan (đuôi). Không cắt ở `holdEnd`: `holdEnd` chỉ cho kit biết khi nào bắt đầu tan; lớp video cần cả đuôi để tan bằng erosion. Với mọi mục `ult` và `expansion` hiện nay `start = 0`, `end = 121`, `step = 4` nên đoạn xuất là cả clip 121 khung (5,04 s).
- Công thức: `soKhung = trim.end - trim.start`; `thoiLuong = soKhung / 24`.
- `peakTime` (giây từ đầu video xuất) = `timing.peak × trim.step / sourceFps`. Nhiều clip ra 0 vì clip đã đủ sức ngay khung đầu (đây không phải lỗi).
- Thời điểm bắt đầu tan (nếu kit cần) = `(timing.holdEnd + 1) × trim.step / sourceFps`.
- Clip lặp (`loop: true`, atlas đã trộn đầu cuối) **không** xuất video theo cách này.

**3. Lệnh ffmpeg (một mục):**

```bash
ffmpeg -v error -nostdin -y -i "<source>" \
  -vf "select='between(n,START,END-1)',setpts=N/(24*TB)" -r 24 -an \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -threads 4 \
  -movflags +faststart "<thư mục>/<id>.tmp.mp4" && mv "<thư mục>/<id>.tmp.mp4" "<thư mục>/<id>.mp4"
```

Trong đó `START = trim.start`, `END = trim.end`, `<thư mục>` là `art-src/lab/vfx/<folder>/`, tên file `<id>.mp4` ngang hàng với atlas và manifest. Lý do từng cờ:
- `select='between(n,…)'` rồi `setpts=N/(24*TB)`: cắt chính xác theo khung (không dùng `-ss`, vì `-ss` làm lệch một hai khung) và đánh lại dấu thời gian đều ở 24 khung/giây.
- `-an`: không âm thanh. `-pix_fmt yuv420p` và `+faststart`: phát được trong mọi trình duyệt và bắt đầu phát trước khi tải xong.
- `-crf 18`, `-preset medium`: gần như không mất chất lượng so với nguồn Firefly; mỗi file 1,8–16,3 MB.
- **Không đổi kích thước, không đệm, không chỉnh mức đen** (nền đen giữ nguyên): 47 clip ra 1920×1080, riêng `sky-gate-open-close` ra 1080×1080 vì nguồn vuông. Ghi `w`, `h` thật vào trường `video` thay vì ép 1920×1080.
- Chạy song song 3 tiến trình (mỗi tiến trình 4 luồng) trên máy này; ghi ra file tạm rồi đổi tên để tiến trình hỏng giữa chừng không để lại file cụt.

**4. Trường `video` ghi vào mục manifest** (ghi nguyên tử: viết file tạm rồi `os.replace`; định dạng manifest thụt 1 khoảng trắng, như các manifest khác):

```json
"video": {
  "file": "pillar-thunder-single.mp4",
  "w": 1920, "h": 1080, "fps": 24.0, "frames": 121,
  "start": 0.0,
  "peakTime": 0.0,
  "pivot": [0.5011, 0.4667],
  "bytes": 3737864,
  "take": 1,
  "source": "games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/video/i2v-pillar-thunder-single/take1.mp4"
}
```

- `w`, `h`, `fps`, `frames`: đọc lại bằng `ffprobe -count_frames -show_entries stream=width,height,r_frame_rate,nb_read_frames` trên **file đã xuất**, không lấy từ nguồn.
- `start`: giây trong video nơi clip bắt đầu (0,0 vì file đã cắt đúng đoạn).
- `pivot`: tâm lõi trên **khung đầy đủ** (0–1), khác `pivot` của ô atlas: `[(pivot.x × cropW + cropX) / srcW, (pivot.y × cropH + cropY) / srcH]` với `crop` và kích thước nguồn lấy từ `<id>.json`.
- `bytes`, `take`, `source`: để biết file tới từ đâu và phát hiện khi take đổi.

**5. Kiểm sau khi xuất:** mọi file đọc được bằng `ffprobe`; `moov` nằm trước `mdat` trong 64 KB đầu (faststart); không có luồng âm thanh; `frames = trim.end - trim.start`; manifest vẫn qua `parseFlipbookManifest` (trường lạ bị bỏ qua, nên không lỗi); tổng dung lượng báo lại.

**6. Hành vi cần có của công cụ:**
- Chạy lại được: bỏ qua mục đã có file `.mp4` và đúng `take` (cờ `--force` để làm lại).
- Dựng lại atlas (`lab_batch.py build`) giữ trường `video`, không xóa.
- Mục có đổi take thì xuất lại và cập nhật `video.take`.
- Lệnh đề nghị: `tools/vfx-flipbook/run.sh export-video <game> <thư-mục|id> [--crf N] [--force]`, đọc `art-src/lab/vfx/<thư mục>/manifest.json`.

**7. Bẫy đã gặp:**
- Nền nguồn khoảng 5/255 chứ không đen tuyệt đối: khi lab cộng sáng, nền đất sáng lên khoảng 2 %. Không xử lý ở đây (đúng lệnh "nền đen giữ nguyên"); nếu về sau cần, trừ mức đen bằng bộ lọc `lutrgb` khi xuất.
- Hầu hết clip chuyển từ ảnh tĩnh nên năng lượng gần phẳng cả 5 s; đừng coi `peakTime` là thời điểm va chạm (xem `clip-skills-expansion.json`, mục `how.clips`).

## Nhật ký

**Đợt 1 (18:40–18:50):** 39 clip, 0 lỗi, 161 MB atlas.
- Hệ: dark 2, earth 1, fire 1 (thêm `fire-ground-impact`, mục cũ giữ nguyên), ice 3, light 2, poison 1, thunder 4, water 3, wind 4, wood 2; `ult` 8 (4 cột trụ, 4 tuyệt kỹ: dark, ice, light, wind); `weapon` 8.
- Chưa có clip trên đĩa: charge, release, ribbon-loop, sheath-loop, impact (trừ `thunder-impact`), sparkle, mọi clip của metal, blood, void, star. Đợt sau lấy tiếp.
- Tấm ghép và video xem trước từng thư mục ở `owner-review/2026-11-05/tu-tien/lab-flipbooks/`.
- Lưu ý: tuyệt kỹ băng (`ult-ice-cold-silence`) và vài cảnh đầy khung cắt ra thấy mép khung video mờ dần (hiệu ứng chạm mép khung gốc, công cụ làm mờ 20–29 px). Hệ Ám: nền đen nên chỉ viền tím và đỏ thẫm hiện, phần đen thẫm mất khi cộng sáng; agent 2 cân nhắc blend thường kèm màu khói nếu cần.

**Claude 18:52 (điều phối):** đã thêm 4 việc video khói Ám trên nền trắng (`dark-impact-white`, `dark-big-burst-white`, `dark-ground-impact-white`, `dark-ribbon-loop-white`, 1 bản mỗi việc). Ghi vào manifest `dark` với `role` như bản nền đen nhưng thêm `"layer": "body"` và chế độ `smoke` (khói trên nền trắng, trộn thường); bản nền đen giữ `"layer": "rim"` (cộng sáng). Agent 2 vẽ lớp `body` dưới lớp `rim`.

**Đợt 2 (19:00):** +8 clip, 0 lỗi (tổng 47, `validate-manifests.ts` 0 lỗi).
- Mới: `fire-ground-mark` (fire, thêm vào manifest cũ), `metal-slash-arc` và `metal-ground-mark` (thư mục `metal` mới, trước đây chưa có manifest), `dao-guard-hold-the-pass`, `dao-k4-unseen-cross-cuts`, `dao-final-world-sever` (weapon), và hai tuyệt kỹ vẽ lại anh chọn lúc 18:45: `ult-water-profound-sea-v2`, `ult-thunder-nine-heavens-v2` (bản `-v2`, không phải hai bản anh đã loại).
- Việc của điều phối 18:52: đã thêm hỗ trợ bốn việc `dark-*-white` (nền trắng): `role` như bản nền đen, `mode: "smoke"`, `blend: "normal"`, `layer: "body"`; mọi clip nền đen của hệ Ám có `layer: "rim"`. Bản nền trắng chưa có trên đĩa, nên chưa thử; đợt có chúng sẽ kiểm kỹ trước khi báo.

**Đợt 3 (19:17):** +8 clip, 0 lỗi (tổng 55).
- Mới: `blood-slash-arc`, `earth-slash-arc`, `earth-ground-mark`, `fire-slash-arc`, `poison-ground-mark`, `wood-ground-mark`; `ult-earth-ink-peaks`, `ult-wood-primordial-tree`.
- Cờ `mustard` (màu vàng xám đục, quy tắc của Hỏa) ở `poison-ground-mark`, `wood-ground-mark`, `ult-wood-primordial-tree`: hệ lục có tông lục-vàng nên cờ này gần như chắc chắn là báo nhầm với chủ ý. Riêng `wood-ground-mark` thiên vàng chanh hơn lục ngọc (đúng "trắng chanh → lục non", thiếu "lục ngọc"): anh nên nhìn tấm ghép `wood.sheet.jpg` để quyết.

**19:25 (lệnh điều phối: Ám là đen viền đỏ thẫm, không tím):** đã gỡ `dark-slash-arc` và `dark-ground-mark` khỏi manifest `dark` (hiện `flipbooks` rỗng, hợp lệ) và `ult-dark` khỏi manifest `ult` (còn 11 mục). File atlas và json của ba clip này giữ trên đĩa, ngoài manifest; ba việc đã được đánh dấu "retired" nên không tự làm lại. Tấm ghép và video của `dark` đã xóa khỏi thư mục cho anh xem; `ult` làm mới.
- Việc Ám mới sẽ vào dưới cùng id việc: `dark-<đơn vị>` (nền đen, `layer: "rim"`), `dark-<đơn vị>-white` (`layer: "body"`, `mode: "smoke"`); sau này `i2v-dark-slash-arc-a`, `i2v-dark-ground-mark-a`, `i2v-ult-dark-a` vào cùng vai trò với bản cũ (`slash`, `groundMark`, `ultimate`), id manifest `dark-slash-arc-a`, `dark-ground-mark-a`, `ult-dark-a`.
- Cờ `mustard` và `white-core` chỉ giữ cho Hỏa; các hệ khác không còn ghi hai cờ này vào manifest (cờ cũ ở `poison`, `wood`, `ult` đã bỏ). Số đo `checks.whiteCore` vẫn còn.

**Đợt 4 (19:34):** +8 clip, 0 lỗi (tổng 60).
- Mới: `blood-ground-mark`, `poison-slash-arc`, `void-ground-mark`, `wood-slash-arc`; `ult-blood`, `ult-fire-one-spark`, `ult-metal-geng`, `ult-poison` (thư mục `ult` giờ 15 mục).
- Lưu ý màu: `void-ground-mark` ra tím lam gần tông Lôi; nếu hệ Không gian cần khác Lôi, anh nên nhìn `void.sheet.jpg`.

**Đợt 5 (19:43, theo lệnh điều phối, làm ngay vì anh đang thử lab phím 2):** +3 clip, 0 lỗi (tổng 63): `void-slash-arc`, `star-ground-mark`, `ult-void`. Clip `slash` giờ có ở 12/14 hệ (metal, fire, water, thunder, wind, ice, earth, wood, light, poison, blood, void); thiếu `star` (việc `i2v-star-slash-arc` chưa xong trên hàng Firefly) và `dark` (bản tím bị loại, chờ `-a`). Đã nhắn `lab-element-kits`. Đợt tiếp theo chạy ngay khi `i2v-star-slash-arc` và `i2v-ult-star` tới.

**Đợt 6 (19:55):** +3 clip, 0 lỗi (tổng 66): `star-slash-arc` (giờ `slash` có ở 13/14 hệ, chỉ thiếu dark), và hai clip Ám nền trắng đầu tiên: `dark-impact-white`, `dark-ground-impact-white`.
- Đường nền trắng chạy đúng: atlas RGBA 256×256, alpha thật (góc ô alpha 0, thân khói đen xám), `mode: "smoke"`, `blend: "normal"`, `alpha: "straight"`, `layer: "body"`. Tấm ghép của clip khói hiện trên nền sáng. Cờ `black-residue` bị bỏ cho clip khói (số đo chỉ có nghĩa với nền đen cộng sáng).
- Mô tả `look` của manifest `dark` đã đổi theo lệnh 19:20 (đen, viền đỏ thẫm, không tím).

**Đợt 7 (19:59):** +1 clip (tổng 67, 0 lỗi): `ult-star` (thư mục `ult` giờ 17 mục). Tuyệt kỹ của mọi hệ đã có trừ dark (chờ `ult-dark-a`).

**20:25 (lệnh điều phối: 30 kỹ năng mở rộng đã duyệt 20:20):** đã thêm vào script. Việc `i2v-<design>` (id thiết kế lấy từ phiếu Codex 300 và 301, tên và hệ từ `SKILLS_EXPANSION_2026-11-05.md`) vào thư mục mới `art-src/lab/vfx/expansion/manifest.json`, mỗi thiết kế một mục: `role` theo nhóm (A `area`, B `avatar`, C `beast`, D `treasure`), `code` (A1…D8), `design` (id), cộng `name` và `elements`. Nền đen, `mode: "fire"` (cộng sáng), ô 640×360 như tuyệt kỹ. Tấm ghép và video chia theo nhóm (`expansion-area`, `expansion-avatar`, `expansion-beast`, `expansion-treasure`) để mỗi file gọn. Chưa có clip nào trên đĩa; vòng chờ chạy ngay khi clip đầu tới, rồi nhắn `lab-element-kits`.

**Đợt 8 (20:58):** +1 clip (tổng 68, 0 lỗi): `myriad-lotus-domain` (A1, `area`), clip mở rộng đầu tiên, trong `expansion/manifest.json`. Đã nhắn `lab-element-kits` và điều phối. Các thiết kế sau vào theo đợt (5 clip mới hoặc 25 phút).

**Đợt 9 (21:08):** +5 clip mở rộng, 0 lỗi (tổng 73): `firmament-sundering-cleave` (A2), `nine-heavens-tribulation-net` (A3), `karmic-ember-tempest` (A4), `glacial-moon-tide` (A5), `samsara-blood-mandala` (A6). Nhóm A (`area`) có 6/8.

**Đợt 10 (21:18):** +5 clip mở rộng, 0 lỗi (tổng 78): `astral-meteor-constellation` (A7), `miasma-briar-abyss` (A8), `asura-six-arms-avatar` (B1), `myriad-palm-bodhi-avatar` (B2), `heaven-earth-titan-avatar` (B3). Nhóm A xong 8/8; nhóm B có 3/6. Chưa có clip Ám nền trắng mới ngoài hai clip đã vào; chưa có bản `-a`.

**Đợt 11 (21:27):** +5 clip mở rộng, 0 lỗi (tổng 83): `polar-star-emperor-avatar` (B4), `nether-samsara-monarch-avatar` (B5), `immortal-sword-progenitor-avatar` (B6), `azure-cloud-dragon` (C1), `white-fiend-tiger` (C2). Nhóm B xong 6/6; nhóm C có 2/8.
- Màu: B5 (màu Ám) ra đỏ rực trên nền đen, không tím nhưng đọc như hệ Huyết hơn Ám: thân đen không hiện khi cộng sáng, chỉ còn viền đỏ. B4 tím lam đúng thiết kế Tinh tú. Anh nên nhìn `expansion-avatar.sheet.jpg`.

**Đợt 12 (21:36):** +5 clip mở rộng, 0 lỗi (tổng 88): `vermilion-solar-phoenix` (C3), `abyssal-xuanwu-tortoise` (C4), `auspicious-thunder-qilin` (C5), `astral-kunpeng-leviathan` (C6), `all-knowing-baize-spirit` (C7). Nhóm C có 7/8 (thiếu `nine-tailed-celestial-fox`, C8); nhóm D chưa có.

**Đợt 13 (21:49):** +5 clip mở rộng, 0 lỗi (tổng 93): `nine-tailed-celestial-fox` (C8), `mountain-crushing-imperial-seal` (D1), `primordial-chaos-bell` (D2), `blade-swallowing-immortal-gourd` (D3), `nine-dragon-refining-cauldron` (D4). Nhóm C xong 8/8; nhóm D có 4/8.

**Đợt 14 (21:59):** +5 clip, 0 lỗi (tổng 98): `seven-treasure-suppressing-pagoda` (D5), `yin-yang-void-mirror` (D6), `five-element-heavenly-silk` (D7), `twelve-stem-nether-banners` (D8), và `dark-big-burst-white` (Ám nền trắng, `layer: "body"`). **Đủ 30/30 thiết kế mở rộng** (A 8, B 6, C 8, D 8). Mỗi nhóm có tấm ghép và video riêng (`expansion-<nhóm>`).
- 22:06 (điều phối) Thứ tự làn video: lưỡi liềm Kim → 8 clip Ám A (`dark-charge`, `-release`, `-ribbon-loop`, `-sheath-loop`, `-sparkle`, `-impact`, `-ground-impact`, `-big-burst`; id không có hậu tố `-a`, nền đen, vai `rim`) khoảng 22:08–22:25 → 13 lưỡi liềm `i2v-<hệ>-crescent-sym` (vai `slash`, thay ảnh tĩnh Codex 302) đến khoảng 22:52 → chạm đất. Clip Ám tím cũ ở `video-rejected-dark-purple/`, đừng dùng.

**Đợt 15 (22:14):** +5 clip Ám nền đen và nền trắng đầu tiên thuộc các vai trò lặp, 0 lỗi (tổng 103): `dark-charge`, `dark-release`, `dark-ribbon-loop`, `dark-ribbon-loop-white`, `dark-sheath-loop`. Đây là lần đầu các mẫu `charge`, `release`, `ribbon`, `sheath` chạy thật, nên xem kỹ và chỉnh hai chỗ:
- **Charge giữ khung cuối:** công cụ làm mờ đuôi khi clip bị cắt ở 2,67 s, khiến khung cuối đen, mà kit giữ khung cuối tới lúc phát chiêu. Nay clip `charge` không làm mờ đuôi; khung cuối là lúc năng lượng dồn tới đỉnh (`timing.endsHot: true`, đúng ý). Nếu về sau một clip charge tự tan sớm, `frames` sẽ cắt ở khung giữ (`framesInAtlas` ghi tổng số khung).
- **Sheath to hơn:** hào quang quấn vũ khí chỉ là một trục mảnh trong khung dọc, ô 180×320 cho trục chỉ khoảng 25 px. Đổi ô sheath thành 270×480 (atlas 2160×3840, dưới 4096). `dark-sheath-loop` đã làm lại.
- Dải ribbon (nền đen và trắng) ghép ngang liền, không cờ đường nối; hào quang Ám nền đen chỉ là hai đường đỏ thẫm mảnh, thân khói nằm ở bản nền trắng (`layer: "body"`).

**Đợt 16 (22:42):** +4 clip Ám nền đen, 0 lỗi (tổng 107): `dark-big-burst`, `dark-ground-impact`, `dark-impact`, `dark-sparkle`. Manifest `dark` giờ 12 mục: bộ nền đen (`layer: "rim"`) gồm charge, release, ribbon, sheath, impact, burst, groundImpact, sparkle; bộ nền trắng (`layer: "body"`) gồm impact, burst, groundImpact, ribbon.
- Lưu ý: ở `dark-big-burst` và `dark-ground-impact` (nền đen), Firefly vẽ thêm một nền đá lát vào clip dù đã dặn nền đen thuần, nên viền đỏ thẫm nằm trên nền đá xám; vụ nổ chiếm khoảng 40 % chiều cao ô, nhỏ hơn bản nền trắng. Khi cộng sáng, nền đá hiện thành lớp xám mờ dưới vụ nổ; agent 2 cân nhắc dùng bản nền trắng cho thân và chỉ lấy viền từ bản nền đen.

**Đợt 17 (23:03–23:05):** +18 clip, 0 lỗi (tổng 123 mục trong 17 thư mục).
- **Lưỡi liềm đối xứng** (lệnh điều phối 22:06): 14 clip `i2v-<hệ>-crescent-sym` đã vào manifest từng hệ với id `<hệ>-crescent-sym`, `role: "slash"` và `shape: "crescent-sym"` (blood, dark, earth, fire, ice, light, metal, poison, star, thunder, void, water, wind, wood). Vì cùng `role` với `<hệ>-slash-arc`, ai đọc theo `role` sẽ gặp `slash-arc` trước (đứng trước trong manifest); muốn lưỡi liềm đối xứng thì chọn theo `shape` hoặc id.
- **Làm lại của Ám:** `dark-big-burst-v2` và `dark-ground-impact-v2` (lời nhắc ghi rõ "không nền, không đá"): đúng, viền đỏ thẫm lơ lửng trên đen, vụ nổ lấp khoảng 70 % ô. Hai bản v1 (có nền đá) đã **gỡ khỏi manifest** (atlas giữ trên đĩa; quay lại bằng `lab_batch.py unretire dark-big-burst dark-ground-impact`). Mục v2 có `supersedes`.
- Manifest `dark` còn 13 mục; chưa có bản `-a` (slash-arc, ground-mark, ult).

**Đợt cuối (23:10, Firefly đã hết hạn 23:07, hàng video dừng):** không còn clip mới ngoài hai clip cuối `metal-ground-impact` và `water-ground-impact`, vốn đã vào ở 23:03. Cả hai vẽ nền đá lát; xem đủ sáu clip `ground-impact` thì **cả sáu** (fire, poison, wind, wood, metal, water) đều có nền đá lát dính vào clip (lời nhắc của chúng ghi "đánh xuống nền đá"). Theo lệnh điều phối 23:07 ("clip nào có nền đá thì không đưa vào manifest") tôi **gỡ cả sáu khỏi manifest**, không chỉ hai clip cuối: giữ bốn clip kia thì trái quy tắc. Atlas giữ trên đĩa; muốn hoàn lại: `lab_batch.py unretire <job>`. Hệ quả: `groundImpact` hiện chỉ còn ở Ám (`dark-ground-impact-v2` và bản nền trắng); các hệ khác để hook trả `false` cho lớp gốc vẽ.
- Gợi ý cho mai: bóc nền đá khỏi sáu clip này bằng trừ nền theo thời gian (nền đá đứng yên, hiệu ứng thì không), hoặc vẽ lại clip với câu lệnh "lơ lửng, không nền" như bản Ám v2 (Firefly mới cần gia hạn).

**Tổng kết:** 117 mục trong 17 thư mục, 0 lỗi kiểm (`validate-manifests.ts` bằng chính `parseFlipbookManifest` của lab); atlas 889 MB; 17 tấm ghép và 17 video xem trước (tổng 44 MB, lớn nhất 7,5 MB) ở thư mục cho anh xem.
- Theo vai trò: `slash` 13/14 hệ qua `slash-arc` và cả 14 hệ qua `crescent-sym`; `groundMark` 13/14 hệ (thiếu Ám, đợi bản `-a`); `burst` water, thunder, wind, ice, earth, wood và Ám; `impact` thunder và Ám; Ám đủ `charge`, `release`, `ribbon`, `sheath`, `sparkle`; `ult/` 4 cột trụ và 13 tuyệt kỹ (thiếu Ám, đợi `ult-dark-a`); `weapon/` 11; `expansion/` 30/30.
- Chưa bao giờ có trên đĩa (Firefly hết hạn trước khi tới): `charge`, `release`, `ribbon`, `sheath`, `sparkle`, `impact` của 13 hệ còn lại (metal, fire, water, thunder, wind, ice, earth, wood, light, poison, blood, void, star), trừ `thunder-impact`; bản `-a` của Ám (`dark-slash-arc-a`, `dark-ground-mark-a`, `ult-dark-a`). Hook của kit trả `false` ở các ô này.
- Việc còn lại sáng mai: thêm tùy chọn "không nhuộm lửa" vào `tools/vfx-flipbook` (hiện vá ở `lab_batch.py`); dọn thư mục `captures/tu-tien/lab-flipbooks/out/` khi anh chốt (atlas thật đã nằm trong `art-src/lab/vfx/`).

**23:55 (việc mới của điều phối: 27 clip W2 sáng 05/11 chưa vào lab):** đã cắt **cả 3 bản** của mỗi việc (qua bảng phụ `lab-<việc>`, không sửa dòng cũ), xem tấm so sánh (`captures/tu-tien/lab-flipbooks/w2-compare/w2-1..7.png`) rồi chọn **một bản mỗi việc**. Vào manifest 23/27 (tổng 140 mục, 0 lỗi kiểm). Bản không chọn chỉ còn trong `out/`.
- **Hỏa (9):** `fire-charge-gather-w2` bản 2 và `twin-fire-spiral-charge-w2` bản 2 (vai `charge`, đều **lặp**, `loop: true`: bản 1 là vòng đồng tâm tĩnh, bản 3 vòng rỗng); `fire-embers-rising-loop-w2` bản 2 (`sparkle`, tàn lửa bay lên, bản 1 có thêm đáy lửa); `fire-spark-spray-w2` bản 2 (`impact`); `fire-smoke-roll-white-w2` bản 2 (vai `smoke`, `layer: "body"`, `mode: "smoke"`, nền trắng, RGBA); `strip-fire-sheath-flow-w2` bản 3 (`sheath`, dải ngang ghép liền; bản 1 và 2 cờ `tile-seam`); `style-w2-fire-ribbon` (`ribbon`) và `style-w2-fire-qi-burst` (`burst`): kiểu W2 là kiểu anh chọn 05/11 02:50; `fire-ground-burn-loop-w2` bản 2 (vai mới `aftermath`; bản 1 là biểu tượng ngọn lửa hoạt hình, bản 3 nứt nham thạch).
- **Kim (3):** `metal-sword-light-streak-w2` bản 3 (`ribbon`, vệt dày, bản 1 cờ cắt mép trên); `strip-metal-silk-flow-w2` bản 2 (`sheath`, lụa trắng xanh sạch); `metal-light-pillar-hit-w2` bản 2 (`impact`, cột kèm vòng đất).
- **Quang (4):** `light-column-strike` bản 1 và `light-column-strike-w2` bản 2 (vai `pillar`, hai biến thể cột đánh khổ dọc); `light-column-loop-w2` bản 1 (`sheath`, cột lặp); `gold-dust-motes-loop-w2` bản 3 (`sparkle`, bụi vàng dày). Lưu ý: ba cột sáng này màu lam ngọc trắng, không phải trắng vàng của Quang; xếp vào `light` theo lệnh.
- **Khác (7):** `sword-rain-streaks-w2` bản 3 → `weapon/`; `sky-gate-open-close` bản 3 → `ult/` (vai `ultimate`, bản duy nhất mở từ nhỏ ra rồi đóng); `cutin-band-edge-light-loop-w2` bản 2, `cutin-callout-light-sweep-w2` bản 3, `cutin-sparkle-motes-drift-w2` bản 3 → thư mục mới `cutin/` (vai `cutin`); `death-soul-threads-w2` bản 1 → thư mục mới `death/`; `dragon-pearl-loop` bản 1 → `dragon/` (vai `pearl`).
- **Bỏ (4), đều là biến thể kiểu thử:** `style-w1-fire-ribbon` (dải mảnh hơn, kiểu W1 anh không chọn), `style-w3-fire-ribbon` (ra hoa văn vạn hoa tuyết vuông, không phải dải), `style-w1-fire-qi-burst` (kiểu W1 anh không chọn), `style-w3-fire-qi-burst` (khung vuông cứng). Không clip nào bị loại vì nền đá hay sai khung.

**06/11 (việc gấp của điều phối: phím 8, 9 mờ vì atlas 640×360 ở 6 khung/giây):** đã xuất **video đầy đủ chất lượng** cho cả 18 mục `ult` và 30 mục `expansion` (48 file, 438 MB, 0 lỗi): `art-src/lab/vfx/<thư mục>/<id>.mp4`, H.264 yuv420p, kích thước nguồn (47 file 1920×1080, riêng `sky-gate-open-close` 1080×1080 vì nguồn vuông), 24 khung/giây, CRF 18, `faststart`, không âm; cắt trọn đoạn atlas đang dùng (khung 0–120, 121 khung, 5,04 s) từ đúng take đang dùng. Nền đen giữ nguyên (không chỉnh mức đen; nền nguồn khoảng 5/255, cộng sáng sẽ nâng nền đất khoảng 2 %). Mỗi mục manifest có thêm `video: { file, w, h, fps, frames, start, peakTime, pivot, bytes, take, source }`; `peakTime` (giây) lấy từ `timing.peak` của atlas nên nhiều clip bằng 0 (clip đã đủ sức ngay khung đầu); `pivot` là tâm lõi trên khung đầy đủ (0–1), khác `pivot` của ô atlas. Atlas cũ giữ làm dự phòng; `lab_batch.py` giữ trường `video` khi dựng lại mục. Script: `captures/tu-tien/lab-flipbooks/export_videos.py`. Không còn tiến trình tạm nào chạy.

**06/11 (việc của điều phối: cắt lớp bộ đếm chuỗi từ D60):** từ ba ảnh Codex 304 trong `art-src/lab/ui/streak-counter/` đã cắt `cut-plate-t{0,10,25,50,100}.png` (cùng khung 538×788, tâm đặt số là tâm vùng mực tối của mỗi nền, đặt trùng ở (269, 394); các cạnh mềm chia chỗ quầng sáng chạm nhau), `cut-flakes-atlas.png` (38 hình: 13 vảy vàng, 8 tia, 11 giọt và vệt mực, 6 khói; thêm 4 giọt vệ tinh tách riêng nên nhiều hơn 34 của đề bài), `cut-ribbons.png` và `manifest.json` (file, khung, tâm, nhóm hình, uv từng hình). Tấm vảy và dải lụa vốn có một lớp mờ alpha 4–30/255 phủ khắp ảnh: tôi nâng ngưỡng lên 0,12 cho hai ảnh đó (nền 5 mốc dùng 8/255) để khỏi có màn sương xám. Script `captures/tu-tien/streak-counter-cut/cut.py`.

**06/11 08:55 (Firefly chạy lại từ 08:46, một làn):** vòng chờ chạy lại (đợt khi có 4 clip mới hoặc sau 20 phút). Hàng ưu tiên theo điều phối: `<hệ>-ribbon-loop`, `-sheath-loop`, `-charge`, `-release`, `-sparkle`, `-impact` cho 13 hệ, rồi `-ground-impact` (prompt đã bỏ nền đất), `-big-burst`, rồi 5 dạng mới `-pillar`, `-vortex-loop`, `-wave`, `-orb-loop`, `-ring-burst` (đã thêm vai `pillar` khổ dọc, `vortex`, `wave`, `orb`, `ringBurst` vào `lab_batch.py`, ô 256×456, 320×320, 512×288, 256×256, 320×320). Sáu clip `ground-impact` đã gỡ tối qua vì nền đá: nếu Firefly làm lại cùng id, `lab_batch.py` tự nhận ra file mới (chữ ký take1 đổi) và làm lại; tôi xem từng clip có nền đá không rồi mới giữ. Đã viết mục "Cách xuất video 1080p cho chiêu lớn" ở trên.

**06/11 08:55 (đợt A):** +4 clip, 0 lỗi (tổng 144): `ice-ribbon-loop`, `thunder-ribbon-loop`, `water-ribbon-loop`, `wind-ribbon-loop` (vai `ribbon`, dải ngang ghép liền 512×288, 48 khung 24 khung/giây, không cờ đường nối). Dải nước xanh đậm với hai mép trắng, đọc rõ.

**06/11 09:02 (đợt B):** +4 clip, 0 lỗi (tổng 148): `earth-ribbon-loop`, `light-ribbon-loop`, `poison-ribbon-loop`, `wood-ribbon-loop` (vai `ribbon`). `poison` và `wood` cờ `tile-seam` 1,09 và 1,13 (ngưỡng 1,0), xem tấm ghép thì chỉ lệch nhẹ ở chỗ nối, không thấy vệt; `wood` là dây leo mảnh (khoảng một phần tư chiều cao ô). Đã có ribbon của water, thunder, wind, ice, earth, light, poison, wood; còn blood, void, star (và metal, fire không có trong hàng).

**06/11 09:09 (đợt C):** +4 clip, 0 lỗi (tổng 152): `blood-ribbon-loop`, `star-ribbon-loop`, `void-ribbon-loop` (xong ribbon cho đủ 11 hệ trong hàng: water, thunder, wind, ice, earth, light, poison, wood, blood, void, star; metal và fire không có trong hàng) và `water-sheath-loop` (vai `sheath`, dải dọc 270×480, trục nước chiếm khoảng nửa bề ngang ô, đọc rõ, không cờ).

**06/11 09:18 (đợt D):** +4 clip, 0 lỗi (tổng 156): `earth-sheath-loop`, `ice-sheath-loop`, `thunder-sheath-loop`, `wind-sheath-loop` (vai `sheath`, dải dọc 270×480, không cờ nghiêm trọng). Sheath đã có water, earth, ice, thunder, wind (và Ám); còn light, wood, poison, blood, void, star.

**06/11 09:26 (đợt E):** +4 clip, 0 lỗi (tổng 160): `blood-sheath-loop`, `light-sheath-loop`, `poison-sheath-loop`, `wood-sheath-loop` (vai `sheath`, 270×480). `blood-sheath-loop` cờ `loop-seam` 1,10 (chỗ nối lặp lệch nhẹ so với nhịp đổi khung, ngưỡng 1,0; có thể thấy một nhịp giật rất nhỏ). Sheath còn thiếu void và star.

**06/11 09:35 (đợt F):** +4 clip, 0 lỗi (tổng 164): `star-sheath-loop`, `void-sheath-loop` (xong sheath cho đủ 13 hệ mới trừ metal và fire, tức water, thunder, wind, ice, earth, wood, dark, light, poison, blood, void, star) và hai clip `charge` đầu tiên của hệ mới: `water-charge`, `thunder-charge` (32 khung 12 khung/giây, một lần, khung cuối giữ ở đỉnh: `endsHot: true`, đúng ý kit giữ tới lúc phát chiêu).
- Lưu ý: `water-charge` là xoáy nước gần như không đổi suốt clip (khung đầu và khung cuối giống nhau), nên kéo thanh tiến độ gõ sẽ không thấy gom lại; `thunder-charge` có chuyển động (tia gom về giữa rồi nở ra, chu kỳ khoảng 17 khung), cũng không tăng dần. Cả hai đọc như "đang tụ lực", không như "càng gõ càng đầy".

**06/11 09:41 (đợt G):** +4 clip `charge`, 0 lỗi (tổng 168): `earth-charge`, `ice-charge`, `wind-charge`, `wood-charge` (32 khung, 12 khung/giây, một lần, khung cuối giữ ở đỉnh). `charge` đã có water, thunder, earth, ice, wind, wood và Ám; còn light, poison, blood, void, star.

**06/11 09:48 (đợt H):** +4 clip `charge`, 0 lỗi (tổng 172): `blood-charge`, `light-charge`, `poison-charge`, `void-charge`. `charge` còn thiếu star.

**06/11 09:55 (đợt I):** +4 clip, 0 lỗi (tổng 176): `star-charge` (xong `charge` cho đủ 12 hệ mới và Ám), và ba clip `release` đầu tiên: `ice-release`, `thunder-release`, `water-release` (32 khung, 12 khung/giây, một lần, bắt đầu ở khung chớp).

**06/11 10:03 (đợt J):** +4 clip `release`, 0 lỗi (tổng 180): `earth-release`, `light-release`, `wind-release`, `wood-release`. `release` đã có water, thunder, ice, earth, light, wind, wood và Ám; còn poison, blood, void, star.

**06/11 10:11 (đợt K):** +4 clip `release`, 0 lỗi (tổng 184): `blood-release`, `poison-release`, `star-release`, `void-release`. `release` đủ 12 hệ mới và Ám. Kế tiếp trong hàng: `sparkle`, `impact`, rồi `ground-impact` làm lại.

**06/11 10:18 (đợt L):** +4 clip `sparkle`, 0 lỗi (tổng 188): `ice-sparkle`, `thunder-sparkle`, `water-sparkle`, `wind-sparkle` (lặp 48 khung, 24 khung/giây, ô 256×256, lớp lấp lánh cộng sáng).

**06/11 10:26 (đợt M):** +4 clip `sparkle`, 0 lỗi (tổng 192): `earth-sparkle`, `light-sparkle`, `poison-sparkle`, `wood-sparkle`. `poison-sparkle` cờ `edge-cut top`: hạt sáng chạm mép trên ô, kit nên làm mờ mép trên khi đặt. `sparkle` còn thiếu blood, void, star.

**06/11 10:47 (đợt N):** +3 clip `sparkle`, 0 lỗi (tổng 195): `blood-sparkle`, `star-sparkle`, `void-sparkle`. `sparkle` đủ 12 hệ mới và Ám. Kế tiếp trong hàng: `impact`.

**06/11 11:08 (đợt O):** +1 clip, 0 lỗi (tổng 196): `water-impact` (vai `impact`, 32 khung, một lần). Trong 20 phút trước đó hàng Firefly chỉ ra một clip, chậm hơn nhiều so với buổi sáng.

**06/11 11:40 (sao băng rơi `comet`, anh duyệt 10:10):** đã vào manifest **15 clip** với vai mới `comet`: `fire-comet`, `water-comet`, `thunder-comet`, `wind-comet`, `ice-comet`, `earth-comet`, `wood-comet`, `light-comet`, `poison-comet`, `blood-comet`, `void-comet`, `star-comet`, `metal-comet`, `dark-comet` (nền đen, `layer: "rim"`) và `dark-comet-white` (khói nền trắng, `layer: "body"`, `mode: "smoke"`). Cũng vào: `earth-impact`, `ice-impact`, `wind-impact` (vai `impact`). Tổng 214 mục.
- **Atlas dự phòng:** lặp 32 khung, 24 khung/giây, ô 640×360.
- **Video 1080p (`video`):** 15 file `<id>.mp4` đã có sẵn trong thư mục từng hệ (một phiên khác cắt lúc 11:23, tôi không ghi đè): 109 khung nguồn 12–120, 24 khung/giây, 1920×1080. Tôi đo thấy khung cuối nối liền khung đầu (tỉ lệ nối trên bước thường 0,96–1,28), nên phát lặp nguyên file là liền. Trường `video`: `file`, `w`, `h`, `fps`, `frames` (109), `start` (0), `peakTime` (0), `sourceStart {frame: 12, seconds: 0.5}`, `loop {start 0, end 4.542, seamless, joinOverStep}`, `pivot`, `bytes`, `take`, `source`.
- **`head` và `dir` (đo trên video nguồn; sao băng đứng yên trong clip nên một kết quả đúng cho cả vòng lặp):**
  - `head`: `uv` (toạ độ đầu trên khung đầy đủ, 0–1, y xuống), `px` (pixel nguồn 1920×1080), `cellUv` (trong ô atlas).
  - `dir`: `deg` và `vec` là hướng từ đầu dọc theo đuôi (toạ độ màn hình, x sang phải, y xuống; 0° là đuôi hướng phải, 90° là đuôi hướng xuống); sao băng bay theo hướng ngược lại. Thêm `tailLengthPx`.
  - Cả 15 clip cùng bố cục: đầu ở khoảng (0,69–0,75; 0,66–0,76) của khung, đuôi chỉ lên trái, góc −143° tới −155° (tức đuôi hướng lên và sang trái khoảng 25–37° so với phương ngang), nên sao băng bay xuống và sang phải. `thunder-comet` đầu lệch trái hơn (0,586; 0,644). Đo trên tấm kiểm: vòng đỏ nằm trên lõi sáng của đầu với fire, water, star, wood, thunder. `dark-comet-white` không có lõi sáng, đầu lấy ở lõi đỏ thẫm (0,70; 0,67).
- Cờ: `star-comet` `edge-cut top` (đuôi chạm mép trên khung nguồn).

**06/11 11:42 (đợt P):** +4 clip `impact`, 0 lỗi (tổng 218): `blood-impact`, `light-impact`, `poison-impact`, `wood-impact`. `impact` đã có water, thunder, ice, wind, earth, blood, light, poison, wood và Ám; còn void, star.

**06/11 11:48 (đợt Q):** +3 clip, 0 lỗi (tổng 221): `star-impact`, `void-impact` (xong `impact` cho đủ 12 hệ mới và Ám) và `thunder-ground-impact`, clip `ground-impact` đầu tiên làm lại với prompt "không nền đất". Đã xem 7 khung (0–28): chỉ có tia sét tím trắng và vòng nổ trên nền đen, không nền đá, không lát đá; đạt, giữ trong manifest (vai `groundImpact`, một lần, đỉnh ở ô 13, bắt đầu tan từ ô 21). Sáu clip `ground-impact` cũ (fire, poison, wind, wood, metal, water) vẫn gỡ; bản làm lại sẽ tự được nhận khi tới.

**06/11 11:51 (đợt R):** +3 clip `ground-impact` làm lại, 0 lỗi (tổng 224): `earth-ground-impact`, `ice-ground-impact`, `light-ground-impact`. Đã xem 6 khung mỗi clip: không còn nền đá lát; đất là vòng đá vỡ viền vàng (earth), mảnh băng bắn ra (ice), vòng tia vàng xoáy (light), tất cả trên nền đen. Đạt, giữ trong manifest. `groundImpact` hiện có thunder, earth, ice, light và Ám.

**06/11 12:18 (đợt S):** +2 clip `ground-impact`, 0 lỗi (tổng 226): `blood-ground-impact`, `void-ground-impact`. Đã xem 6 khung mỗi clip: không có nền đá; máu là vụ bắn đỏ với mảnh tinh thể tối, không gian là khối tinh thể góc cạnh trắng xanh (không tím, nên khác hệ Lôi). Đạt, giữ trong manifest. `groundImpact` có thunder, earth, ice, light, blood, void và Ám; còn fire, poison, wind, wood, metal, water (làm lại, sẽ tự được nhận) và star.

**06/11 14:35 (đợt T, nhiều loại clip mới của hàng Firefly; tổng 260 mục):**
- `star-ground-impact` (14:25), `light-big-burst`, `poison-big-burst` vào. `groundImpact` có thunder, earth, ice, light, blood, void, star và Ám (mỗi clip đã xem khung: không nền đá).
- **Ám vẽ lại, hết tím:** `dark-slash-arc`, `dark-ground-mark`, `ult-dark` được làm lại với cùng id việc (`i2v-dark-slash-arc`, `i2v-dark-ground-mark`, `i2v-ult-dark`, không hậu tố `-a`); script tự nhận file mới và gỡ trạng thái "retired". Ba atlas tím cũ dời vào `art-src/lab/vfx/dark/_rejected-purple/` để không bị ghi đè. Bản mới đỏ thẫm trên đen, đúng bảng màu A; manifest `dark` giờ 19 mục. `ult-dark` đã có video 1080p.
- **Hai vai mới theo tên việc (tôi đặt tên, đổi được):** `i2v-<hệ>-caster-seal` → `casterSeal` (ấn trận dưới chân người ra chiêu, 14 hệ, lặp liền 32 khung, ô 512×288) và `i2v-<hệ>-hit-affliction` → `hitAffliction` (vòng tai ương bám quái bị trúng, 14 hệ, lặp liền 32 khung, ô 384×384). Chưa xuất video 1080p cho hai vai này (xuất được bằng `export_videos.py`, thêm vai vào `EXTRA_ROLES`). Cờ nhỏ: `fire-caster-seal` `edge-cut top`.
- **Sao băng làm lại (`comet-v2`, 8 hệ: blood, dark, earth, metal, poison, void, wind, wood; ghi trong prompt "redo after blind judges"):** vào manifest với id `<hệ>-comet-v2`, `supersedes: <hệ>-comet`, cùng `head`, `dir`, `video`. Tôi **gỡ tám bản `-comet` cũ** khỏi manifest (atlas và mp4 cũ còn trên đĩa; hoàn lại bằng `lab_batch.py unretire i2v-<hệ>-comet`); `dark-comet-white` giữ nguyên, `fire`, `water`, `thunder`, `ice`, `light`, `star` chưa có bản làm lại nên giữ bản đầu.
- **Video 1080p của `comet-v2` (cắt lặp dài nhất liền nhất, mp4 mới ghi trong thư mục từng hệ):** metal 115 khung (nối/bước 0,81), wind 111 (1,01), blood 75 (1,18), wood 74 (1,24) liền; `earth` 65 khung (2,93), `dark` 121 (1,92), `poison` 83 (2,26), `void` 71 (4,43) **không liền** (clip trôi dần, `loop.seamless: false`), lab nên trộn một đoạn ngắn ở chỗ nối.

**06/11 14:34 (đợt U):** +4 clip, 0 lỗi (tổng 264): `blood-big-burst`, `star-big-burst`, `void-big-burst` (vai `burst`) và `metal-pillar`, clip `pillar` đầu tiên của loạt dạng mới (khổ dọc 256×456, một lần; cột trắng bạc rơi từ mép trên xuống, mảnh kim loại bắn ở chân; đỉnh ở ô 22, bắt đầu tan từ ô 25; cột chạm mép trên khung đúng ý). Hai dạng mới đầu tiên của hàng Firefly còn lại: `vortex-loop`, `wave`, `orb-loop`, `ring-burst`.

**06/11 15:39 (đợt V):** +1 clip, 0 lỗi (tổng 265): `fire-pillar` (vai `pillar`, 256×456, một lần). Hàng Firefly chậm lại: một clip trong hơn một giờ.

**06/11 15:55 (đợt W):** +4 clip `pillar`, 0 lỗi (tổng 269): `ice-pillar`, `thunder-pillar`, `water-pillar`, `wind-pillar` (256×456, một lần). `pillar` đã có metal, fire, ice, thunder, water, wind.

**06/11 16:09 (đợt X):** +4 clip, 0 lỗi (tổng 273): `earth-pillar`, `wood-pillar` (vai `pillar`; đã có metal, fire, ice, thunder, water, wind, earth, wood) và `metal-charge`, `metal-release` (Kim vào hàng, `charge` và `release`; Kim giờ có charge, release, slash, groundMark, comet, pillar, các clip W2).

**06/11 16:27 (đợt Y):** +4 clip `pillar`, 0 lỗi (tổng 277): `blood-pillar`, `dark-pillar`, `light-pillar`, `poison-pillar`. `dark-pillar` đỏ thẫm, chỉ hai mép cột hiện khi cộng sáng (thân đen mất, như mọi clip Ám nền đen; nên ghép với bản nền trắng nếu có). Còn pillar của void và star.

**06/11 16:45 (đợt Z):** +4 clip, 0 lỗi (tổng 281): `star-pillar`, `void-pillar` (xong `pillar` cho đủ 14 hệ) và hai `vortex-loop` đầu tiên: `fire-vortex-loop`, `metal-vortex-loop` (vai `vortex`, lặp liền 48 khung 24 khung/giây, ô 320×320, trường xoáy nhìn từ trên). Lưu ý màu: `fire-vortex-loop` có viền tím ngoài (lệch bảng màu Hỏa trắng vàng, hổ phách, son); kit có thể hạ viền ngoài hoặc chấp nhận.

**06/11 17:00 (đợt AA):** +4 clip `vortex-loop`, 0 lỗi (tổng 285): `ice-vortex-loop`, `thunder-vortex-loop`, `water-vortex-loop`, `wind-vortex-loop` (vai `vortex`, lặp liền, 320×320). `vortex` đã có fire, metal, ice, thunder, water, wind.

**06/11 17:15 (đợt AB):** +4 clip `vortex-loop`, 0 lỗi (tổng 289): `dark-vortex-loop`, `earth-vortex-loop`, `light-vortex-loop`, `wood-vortex-loop`. `vortex` còn thiếu poison, blood, void, star.

**06/11 17:32 (đợt AC):** +4 clip `vortex-loop`, 0 lỗi (tổng 293): `blood-vortex-loop`, `poison-vortex-loop`, `star-vortex-loop`, `void-vortex-loop`. `vortex` đủ 14 hệ. Còn trong hàng: `wave`, `orb-loop`, `ring-burst` và các clip thiếu lẻ tẻ (`sheath` của metal, fire; ground-impact làm lại của fire, poison, wind, wood, metal, water).

**06/11 17:48 (đợt AD):** +4 clip `wave`, 0 lỗi (tổng 297): `fire-wave`, `metal-wave`, `thunder-wave`, `water-wave` (vai `wave`, một lần, 26 khung 8 khung/giây, ô 512×288, cắt ở 3,2 s). Đã xem khung: sóng là một dải ngang đầy bề rộng khung (không thấy đỉnh sóng chạy từ trái sang phải trong clip), nên kit tự trượt dải theo hướng bay. `fire-wave` có mép dưới tím (lệch bảng màu Hỏa, như `fire-vortex-loop`); `water-wave` là mặt nước xanh đậm với đường đỉnh sóng trắng.

**06/11 18:05 (đợt AE):** +4 clip `wave`, 0 lỗi (tổng 301): `earth-wave`, `ice-wave`, `wind-wave`, `wood-wave`. `wave` đã có fire, metal, thunder, water, earth, ice, wind, wood.

**06/11 18:20 (đợt AF):** +4 clip `wave`, 0 lỗi (tổng 305): `blood-wave`, `dark-wave`, `light-wave`, `poison-wave`. `wave` còn thiếu void và star.

**06/11 18:39 (đợt AG):** +4 clip, 0 lỗi (tổng 309): `star-wave`, `void-wave` (xong `wave` cho đủ 14 hệ) và hai `orb-loop` đầu tiên: `fire-orb-loop`, `metal-orb-loop` (vai `orb`, lặp liền 48 khung, ô 256×256, quả cầu đạn).

**06/11 18:46 (đợt AH):** +4 clip `orb-loop`, 0 lỗi (tổng 313): `ice-orb-loop`, `thunder-orb-loop`, `water-orb-loop`, `wind-orb-loop`. `orb` đã có fire, metal, ice, thunder, water, wind.

**06/11 18:53 (đợt AI):** +4 clip `orb-loop`, 0 lỗi (tổng 317): `dark-orb-loop`, `earth-orb-loop`, `light-orb-loop`, `wood-orb-loop` (`wood-orb-loop` cờ `edge-cut top`: một hạt chạm mép trên ô). `orb` còn thiếu poison, blood, void, star.

**06/11 19:11 (đợt AJ):** +4 clip `orb-loop`, 0 lỗi (tổng 321): `blood-orb-loop`, `poison-orb-loop`, `star-orb-loop`, `void-orb-loop`. `orb` đủ 14 hệ. Còn trong hàng: `ring-burst` (chưa clip nào về), cùng `sheath` của metal, fire và `ground-impact` làm lại của fire, poison, wind, wood, metal, water.

**06/11 19:19 (đợt AK):** +4 clip `ring-burst`, 0 lỗi (tổng 325): `fire-ring-burst`, `metal-ring-burst`, `thunder-ring-burst`, `water-ring-burst` (vai `ringBurst`, một lần, 32 khung 12 khung/giây, ô 320×320). Đã xem khung: không nền đá. Lửa, sét, kim loại là vòng nở ra; `water-ring-burst` là đĩa nước xanh đã đầy ô từ khung đầu (không nở), chỉ sáng rồi tan.

**06/11 19:28 (đợt AL):** +4 clip `ring-burst`, 0 lỗi (tổng 329): `earth-ring-burst`, `ice-ring-burst`, `wind-ring-burst`, `wood-ring-burst`. `ringBurst` đã có fire, metal, thunder, water, earth, ice, wind, wood.

**06/11 19:36 (đợt AM):** +4 clip `ring-burst`, 0 lỗi (tổng 333): `blood-ring-burst`, `dark-ring-burst`, `light-ring-burst`, `poison-ring-burst`. `ringBurst` còn thiếu void và star.

**06/11 20:09 (đợt AN):** +3 clip, 0 lỗi (tổng 336): `metal-big-burst`, `star-ring-burst`, `void-ring-burst` (`ringBurst` đủ 14 hệ).
- **Bảng thiếu so với danh sách của điều phối, tính trên manifest:** mọi vai `charge`, `release`, `ribbon`, `sheath`, `impact`, `burst`, `slash`, `groundMark`, `comet`, `pillar`, `vortex`, `wave`, `orb`, `ringBurst`, `casterSeal`, `hitAffliction` đã đủ 14 hệ (Hỏa và Kim dùng thêm clip W2 và clip có sẵn cho các ô không nằm trong hàng). Còn thiếu: `groundImpact` của metal, fire, water, wind, wood, poison (sáu clip làm lại chưa về; bản cũ có nền đá đã gỡ) và `sparkle` của metal.

**07/11 00:28 (đợt AO):** `void-wave` được Firefly làm lại và vào lại (tổng 336 mục của tôi). Ngoài ra thấy ở `art-src/lab/vfx/` các thư mục manifest không phải của phiên này (`world`, `boss`, `foe`, `foe-i2v`, `meta`, `hybrid`, `beast`, `expansion-phases`, `sigils`), do phiên khác tạo bằng cùng công cụ; tôi không đụng tới. `sigils/manifest.json` đang rỗng nên bộ đọc báo lỗi "no flipbooks" (dở dang của phiên đó, không ảnh hưởng 336 mục của tôi). Vẫn thiếu: `groundImpact` của metal, fire, water, wind, wood, poison và `sparkle` của metal.

**07/11 01:17 (đợt AP):** `dark-big-burst` được làm lại (file mới 01:16; hai bản cũ đã đổi tên `take1.wrong-dup.mp4`, `take1.wrong-ref.mp4`) nên script nhận ra, gỡ trạng thái "retired" và dựng lại. Đã xem 6 khung và so với `dark-big-burst-v2`: bản mới là khối khói xám mờ với vài đốm đỏ thưa, vòng đỏ chỉ hiện muộn, yếu hơn hẳn v2 (đỏ thẫm sáng, nở đầy ô). Cả hai đều ở manifest `dark`; `dark-big-burst-v2` đứng trước nên ai đọc theo `role` vẫn gặp v2. Nếu muốn bỏ bản mới: `lab_batch.py retire dark-big-burst`. `void-wave` đang có thư mục trống (có người đang làm lại), mục trong manifest vẫn là bản cũ.

**07/11 02:03 (đợt AQ):** `void-wave` làm lại xong và vào lại (bản mới thay bản cũ, cùng id; 26 khung, 8 khung/giây). Vẫn thiếu `groundImpact` của metal, fire, water, wind, wood, poison và `sparkle` của metal.

**07/11 02:12 (đợt AR):** +3 clip `ground-impact` làm lại, 0 lỗi: `fire-ground-impact`, `metal-ground-impact`, `water-ground-impact` (cùng id việc cũ nên script tự nhận file mới và gỡ trạng thái "retired"; atlas bản có nền đá cũ bị bản mới ghi đè). Đã xem 6 khung mỗi clip: không còn nền đá. Lửa là vòng lửa vỡ vàng cam, kim loại là mảnh vỡ trắng bạc bắn ra, nước là hoa băng xanh nở; đều đạt, giữ trong manifest. `groundImpact` còn thiếu poison, wind, wood (thư mục đang trống, có người đang làm lại) và `sparkle` của metal.

**07/11 02:17 (đợt AS):** +3 clip `ground-impact` làm lại, 0 lỗi: `poison-ground-impact`, `wind-ground-impact`, `wood-ground-impact`. Đã xem 6 khung mỗi clip: không nền đá; độc là hoa xanh lục chuyển tím, gió là hoa ngọc bạc hà kèm lá, gỗ là vòng rễ vàng cam (không phải lục, lệch so với "lục non, lục ngọc" của Mộc; rễ có thêm vài chiếc lá lục nhỏ ở khung muộn). Đạt, giữ trong manifest. **`groundImpact` đủ 14 hệ.** Chỉ còn thiếu `sparkle` của metal.

**07/11 02:21 (đợt AT, xong danh sách):** `metal-sparkle` vào (48 khung lặp, 256×256), hết ô trống cuối cùng. Kiểm trên manifest: **18 vai × 14 hệ không còn ô trống** (`charge`, `release`, `ribbon`, `sheath`, `impact`, `burst`, `groundImpact`, `sparkle`, `slash`, `groundMark`, `comet`, `pillar`, `vortex`, `wave`, `orb`, `ringBurst`, `casterSeal`, `hitAffliction`; Hỏa và Kim dùng thêm clip W2 và clip có sẵn cho các ô không nằm trong hàng). Phiên này quản **344 mục** đang dùng (9 mục đã gỡ: Ám tím, sao băng bản 1 của 8 hệ có bản làm lại, hai clip `ground-impact` nền đá đã được thay bằng bản làm lại). Bộ đọc của lab đọc được mọi manifest của phiên này; riêng `sigils/manifest.json` (phiên khác) rỗng nên báo lỗi. Vòng chờ nền đã dừng, không còn tiến trình nào chạy; chạy lại bằng `lab_batch.py wait` khi hàng Firefly có clip mới.

**11/11 (việc điều phối: thay nguồn clip lab bằng video Firefly làm lại `i2v3`, 53 mục anh chọn, 6 mục `redo` bỏ qua):** đã thay **53/53**, 0 lỗi; manifest vẫn qua bộ đọc của lab; lab 3146 phát được (`ult-star` thử bằng `__lab.showcase`, không lỗi console ngoài 403 có sẵn của `typing-feel/keys-manifest.json`).
- Mỗi mục giữ nguyên id, vai, thư mục, kích thước ô; `job` đổi sang `i2v-<base>-i2v3`, `take` theo lựa chọn, `previous` ghi job/take/file cũ. File cũ giữ dưới tên `<id>.old.atlas.png`, `<id>.old.json` (và `<id>.old.mp4` với 38 mục có `video`); không xóa gì.
- `i2v-ult-water-profound-sea-i2v3` thay cho mục `ult-water-profound-sea-v2` (manifest không còn id gốc). `azure-cloud-dragon` chỉ thay ở `expansion`, không đụng bản `hybrid` (phiên khác).
- 38 mục `ult` và `expansion` có `video` đã xuất lại mp4 1080p từ take mới (cùng công thức `export_videos.py`). Mọi mục được nén lại `.uastc.ktx2` bằng `run.sh ktx2 --force` (manifest đã có ktx2 do phiên khác thêm; nén cũ là từ atlas cũ nên phải làm lại).
- Script `captures/tu-tien/i2v3-flipbooks/i2v3.py`; tấm trước/sau từng clip `<id>.before-after.jpg` và 6 tấm gộp `sheet-1..6.jpg`; ảnh lab sau khi thay: `lab-after-ult-star.jpg` (ult mới phát trong lab), `lab-after-thunder-key1-hit.jpg`, `lab-after-fire-typed-charge.jpg` (hai ảnh sau không bắt được riêng lớp hit-affliction và charge-fill; so sánh bằng tấm atlas). Không có ảnh lab "trước" vì atlas đã thay trước khi chụp; phần "trước" là hàng trên của tấm so sánh.
- Lưu ý ngoài phạm vi: `clip-skills.ts` của lab gọi `ult-dark-a` nhưng manifest `ult` chỉ có `ult-dark` (vừa thay bằng i2v3).

### Đợt AV · 11/11 23:00–00:00 · dấu đất nhìn từ trên (phiếu `ground-marks-top-lab.md`)
`dark-ground-mark`, `light-ground-mark` thay bằng clip i2v3 nhìn thẳng từ trên (take1, ô 512², 31 khung @ 6 fps, mp4 1080², ktx2, file cũ `.old`); thêm `thunder-scorch-crack-top` (`thunder/`, vai `scorch`, chưa nối chiêu). Script `captures/tu-tien/ground-marks-top/gm_top.py`; tấm trước/sau cùng thư mục. Ghi chú: ô vuông 512² chỉ được tối đa 36 khung (giới hạn 12 Mpix của KTX2).

### Đợt AW · 12/11 00:10–00:40 · bộ Lôi bạch kim (i2v5) cho chiêu Ngũ Lôi
8 mục mới trong `thunder/manifest.json`, vai là tên để phiên chiêu sét nối (không phải ClipRole nên element-clips bỏ qua): `thunder-five-strike-wg` (strike, 405×720, 32 khung @24, nguồn 48–80), `thunder-single-bolt-{a,b,c,d}-wg` (bolt, 405×720, 32 khung @24, cửa sổ đổi hình nhiều nhất: 55–87, 71–103, 45–77, 84–116), `thunder-five-impact-burst-wg` (impactBurst, 448², 26 khung @6, flash), `thunder-five-lingering-arcs-wg` (arcs, lặp 48 @24, 512×288, mp4 liền mạch), `thunder-five-cloud-ink-wg` (cloudInk, take2, lặp 48 @24, 512×288, mp4 `loop.seamless:false`). Mỗi mục có `.uastc.ktx2` (md5 khớp) và mp4 1080p (`video`). Đo: 0 % xanh tím ở cả 8, sắc trung bình 29–37° (vàng kim), nền đen, không vật lạ (`captures/tu-tien/thunder-wg-flipbooks/measure.json`). Lưới atlas của công cụ là luỹ thừa 2, nên 36 khung thành 64 ô vượt 12 Mpix của KTX2: tia cao 32 khung, cung và mây ô 512×288. Script `wg.py`, tấm `atlas-sheet.jpg`, dải nguồn `source-*.strip.jpg` cùng thư mục.

### Đợt AX · 12/11 13:05–13:25 · tia Lôi bạch kim bản -hi (ô cao gấp đôi)
5 mục cũ đổi thành `*-wg-lo` (tệp đổi tên theo; `*-wg` giữ làm bí danh trỏ cùng tệp vì `five-thunder.ts` còn gọi tên đó). 5 mục mới `thunder-five-strike-wg-hi`, `thunder-single-bolt-{a,b,c,d}-wg-hi`: ô 540×960, 16 khung = cùng cửa sổ 32 khung lấy cách 1 (fps 12, giữ thời gian thật), atlas 2160×3840, ktx2 md5 khớp; mp4 1080×1920 đúng cửa sổ 32 khung @24 fps (`video.sourceWindow`, `video.crop`). Đo (`captures/tu-tien/thunder-wg-flipbooks/measure-lo-hi.json`, tấm `lo-hi-66px.jpg`, `lo-hi-250px.jpg`): độ dốc cạnh lõi hi/lo = 0,96–1,00 ở 66 và 250 px, +1 % ở 720 px, +2–5 % ở 960 px; 0 % xanh tím. Kết luận: atlas 405×720 đã dư mẫu ở cỡ hiển thị ≤ 250 px, độ "mềm" nằm ở nét Firefly (quầng 1,3–3× lõi) và ở cách vẽ (blur/softM, cộng sáng, bloom), không phải ở việc thu nhỏ atlas. Test 62/62 qua.

### Đợt AY · 12/11 14:40–15:10 · âm thanh Ngũ Lôi (phiếu `five-thunder-sound.md`)
13 sự kiện từ 62 take Firefly kiểm máy; wav+ogg+manifest ở `art-src/lab/audio/five-thunder/`; clip nghe thử `owner-review/2026-11-12/tu-tien/five-thunder-lab/ngu-loi-v16-sound-preview.mp4` (I −17,4 LUFS, TP −2,8 dBTP). Thiếu: tiếng "rắc" khô dải cao cho tia đơn, IR hồi vang.

### Đợt AZ · 12/11 15:15–15:40 · gói âm quái, tinh anh, boss (phiếu `foe-sound-pack.md`)
75 sự kiện từ 456 take kiểm máy → `art-src/lab/audio/foes/` (wav+ogg+manifest với bản đồ loài/cấp, bucket); clip `foe-sound-preview.mp4` (−18,9 LUFS, TP −6,7) và bản kèm Ngũ Lôi. Thiếu: rat hurt/death riêng, spawn sói/quạ/vượn, gầm tinh anh và captain theo loài, boss-charge-launch không clip, IR.

### Đợt BA · 12/11 16:00–16:50 · gói âm quái v2 (25 job "gap foe-pack")
100 take mới đo (takes-foe.json 556 take); `art-src/lab/audio/foes/` dựng lại 98 sự kiện, 73 có `variants`, mọi sự kiện có `layers` và `pitchJitter` 0,03; âm thật thay mọi chỗ dùng tạm (bảng "Thiếu" bỏ). Nối lab: `foe-levels.ts` (sinh), `FIREFLY_LEVELS` gộp, `LabSound.foe`/`prepareFoes`, `tests/lab/foe-sounds.test.ts`; 420/420 test lab qua. Clip `foe-sound-v2-web.mp4` (−20,7 LUFS tích hợp, TP −5,8).

### Đợt BB · 15/11 · video Firefly 13/11 (perf-stress vòng 3, việc 3)
62 việc / 122 take kiểm máy (`captures/tu-tien/firefly-picks-1113/pick_takes.py`, `takes-1113.json`), picks `.local/s2/picks-2026-11-13.json`; flipbook 61 (53 thay, 8 mới) bằng `flipbooks_1113.py` (công cụ và cách của 53 clip i2v3), ktx2 nén lại, 10 mp4. Cờ: `foe-crow-dive` vệt đen, `foe-seal-an` sát mép dưới; vài bản manifest có khối hạt cạnh cứng ở cuối clip (phát ngược nên thành đầu) — anh xem tấm.
