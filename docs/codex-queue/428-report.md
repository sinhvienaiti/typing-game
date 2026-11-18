# Phiếu 428 — vương miện máu -v4 từ hai giây đầu

Ngày 16/11/2026. **Đã tạo bộ -v4, thay vào lab; kiểm lề, luma, schema, probe và kiểu dữ liệu PASS.** Phiếu có PASS của Sonnet và miễn luật hạn mức riêng của owner; làm một luồng, không gọi trợ lý hoặc tạo nội dung AI mới.

## Tệp đã làm

Trong `games/immortality-cultivation/art-src/lab/vfx/blood/`, bốn tệp mới:

- `blood-big-burst-v4.atlas.png`
- `blood-big-burst-v4.json`
- `blood-big-burst-v4.uastc.ktx2`
- `blood-big-burst-v4.prompt.txt`

Nguồn duy nhất: `firefly-raw/blood-big-burst.v5-try2.mp4`, từ ảnh repo owner chọn `stills-55/blood-crown.v2-try1.png`. Prompt cạnh asset ghi đầy đủ thao tác, ảnh tham chiếu, SHA-256 nguồn và nguyên văn prompt Firefly. Không ghi đè atlas cũ.

`games/.wt-ic-lab-all/src/lab/burst-v2.ts`: chỉ đổi hậu tố dòng `blood-big-burst` từ `-v3` sang `-v4`. Giữ gradient đỏ thẫm `[[0.4,0,0.02],[0.9,0.32,0.28]]`, scale **0,401**, intensity **2,2**, occlude **0,85**; không sửa `burst-layers.ts` hoặc các lớp giọt/vũng máu. Đã so sánh toàn tệp với bản chụp trước thao tác để xác nhận chỉ thay hậu tố này.

`docs/games/tu-tien/skills/VFX_LIBRARY.md`: bổ sung mục 428, nguồn, thông số, số đo và giới hạn.

## Đóng gói và kiểm

Dùng trực tiếp `media.decode_crop`, `grade.crush_black`, `grade.neutral_fade`, `atlas.write_atlas`, `ktx2.encode` của `tools/vfx-flipbook/`; script điều phối trong thư mục tạm, không sửa công cụ.

- **32 khung**, lưới **8×4**, ô **256²**, atlas **2048×1024**; RGB additive, không premultiply, không loop. Nguồn 24 fps, chỉ lấy mốc trong **[0;2,0) s**; phát **16 fps**, dài **2,0 s**.
- Chỉ số nguồn: `0,2,3,5,6,8,9,11,12,14,15,17,18,20,21,23,24,26,27,29,30,32,33,35,36,38,39,41,42,44,45,47`. Lấy mẫu gần nhất, không nội suy hoặc lặp khung; `trim.step=1.5`, `trim.end=48` là cận loại trừ. Mốc hiển thị trên ảnh atlas là thời gian phát, lệch thời gian mẫu nguồn tối đa nửa khung nguồn.
- Một crop **`[-180,-180,1440,1440]`** chung, đệm đen, thu nhỏ đồng nhất; `rotate=0`, `flipX=false`, `squashY=1`. Giữ phối cảnh 55°, không vignette hoặc che mép. Pivot **`[0.5,0.590278]`**, từ điểm hội tụ/chạm đất **`[540,670]`** của khung đầu.
- Crush đen `t0=0.02`, `greyCut=0.15`, không đổi tông. Tail fade chỉ **8 khung cuối 24–31**, theo `1−smoothstep(0,1,(i−23)/8)`; khung cuối tắt hoàn toàn. Kiểm dựng lại từng pixel từ nguồn xác nhận 24 khung đầu không fade và 8 khung cuối đúng đường fade.
- **64 lượt kiểm khung PASS:** 32 PNG + 32 KTX2 giải mã mức 0. Ngưỡng có hình `maxRGB>12`; lề trái/phải/trên/dưới **32 / 32 / 36 / 83 px** cho cả hai định dạng, tối thiểu **12,5%**. Toàn dải lề `ceil(10%×256)=26 px` có RGB tối đa **0**. Luma trung bình và cực đại khung cuối **0**, thấp hơn 0,02.
- JSON có đúng tập khoá gốc và toàn bộ khoá lồng của `blood-big-burst-v3.json`. UASTC mức 2, sRGB, Zstd, Y-flip, **12 mip**; giải mã lại và trả Y về chiều PNG trước khi đo. Sai số RGB trung bình sau nén **0,154/255**.
- SHA-256 xác nhận **78 tệp đã có** giữ nguyên, gồm các tệp trực tiếp trong thư mục blood, video nguồn, ảnh tham chiếu và `burst-layers.ts`; checksum bốn tệp mới cũng khớp.

Probe chạy module TypeScript thật, manifest thật, qua symlink `art-src` thực của lab: cả JSON/PNG/KTX2 `-v4` có tệp và trả 200 trong fetch mô phỏng, **0 cảnh báo/404**. Xác nhận 32 khung/16 fps/2,0 s/pivot, grid `-v4`, từ chối JSON `-v3`, cache, `burst=old` và fallback khi 404. Đây là **probe đọc tệp, chưa kiểm HTTP hoặc trình duyệt/GPU**.

`node games/.wt-ic-lab-all/node_modules/typescript/bin/tsc --noEmit -p games/.wt-ic-lab-all/tsconfig.json`: **exit 0, 0 lỗi**. Không chạy build hoặc bộ test game.

## Bằng chứng và chạy lại

Đích `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/burst-v4/` ngoài quyền ghi của phiên. Dùng fallback được phiếu cho phép: **`/private/tmp/428-burst-v4/`**, có `ABOUT.md`.

- `blood-big-burst-v4-8-frames.jpg`: tám khung **0,4,8,13,18,24,28,31**, gồm đoạn tan; viền xanh lề 10%, dấu cam pivot, font Arial.
- `blood-big-burst-source-8.jpg`: tám mốc nguồn trước xử lý, tới 1,958 s. Đã mở xem cả hai ảnh; mỗi ảnh có `.prompt.txt` mô tả phép ghép.
- `audit.py`, `package.py`, `verify.py`, `probe.mts`; `source-audit.json`, `packaging.json`, `original-sha256.json`, `final-validation.json`, `probe.json`, `probe.txt`, `typecheck.txt`, bản chụp code trước thay hậu tố. Không xuất hoặc giữ khung thô; đã xoá bốn bản staging trùng với asset chính, không có chuỗi PNG thô cần prune.

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game
PYTHONDONTWRITEBYTECODE=1 tools/vfx-flipbook/.venv/bin/python -B /private/tmp/428-burst-v4/verify.py
node --import ./games/.wt-ic-lab-all/node_modules/tsx/dist/loader.mjs /private/tmp/428-burst-v4/probe.mts
```

Coordinator có thể chuyển bằng chứng khi ngoài sandbox, giữ các tệp đích đã có rồi cập nhật chỉ mục:

```sh
mkdir -p /Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/burst-v4
cp -Rn /private/tmp/428-burst-v4/. /Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/burst-v4/
cd /Volumes/SS990TPRO/htdocs/typing-game
node scripts/review-index.mjs
```

## Giới hạn và việc owner cần xem

**Nguồn đã cắt một số giọt nhỏ từ khung 36, 1,5 s**, ngay lúc bắt đầu tail fade; mép RGB nguồn cực đại trong 0–2 s là **172/255**. Vẫn giữ đúng đoạn owner yêu cầu, không loại khung hoặc đổi thời lượng để né phần này. Thu nhỏ tạo lề atlas đúng yêu cầu nhưng **không khôi phục phần nguồn đã mất**; không tuyên bố nguồn nguyên vẹn. Trong bảng tám mốc, thân vương miện còn trong khung.

Owner/coordinator cần xem ảnh tám khung, đoạn tan và điểm chạm/cỡ vương miện trong lab. Chưa kiểm host/trình duyệt/GPU hoặc chấm hiệu ứng tổng hợp 8,5. Chưa ghi review SSD hoặc cập nhật chỉ mục do ngoài quyền ghi; đã dùng fallback. Không bỏ bước xử lý nào của phiếu; không tạo ảnh/clip mới, không chỉnh màu lab, không sửa lớp phụ. Không đổi nhánh, stage media, commit, push, reset, clean hoặc stash.
