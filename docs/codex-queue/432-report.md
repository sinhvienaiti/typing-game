# Phiếu 432 — giữ khối khói độc lan rộng

Ngày 17/11/2026. **Đã tạo -v5 và bật trong lab. Đo PNG/KTX2, probe đọc tệp và kiểm kiểu PASS; HTTP/trình duyệt còn cần coordinator kiểm.** Phiếu có PASS Sonnet và miễn hạn mức của owner. Làm một luồng, không sinh nội dung AI mới.

## Tệp đã làm

Trong `games/immortality-cultivation/art-src/lab/vfx/poison/`, bốn tệp mới:

- `poison-big-burst-v5.atlas.png`
- `poison-big-burst-v5.json`
- `poison-big-burst-v5.uastc.ktx2`
- `poison-big-burst-v5.prompt.txt`

Nguồn duy nhất: `firefly-raw/poison-big-burst.v3-try2.mp4` (take B của phiếu), từ ảnh repo `stills-55/poison-big-burst.v1-try1.png`. Prompt cạnh asset ghi nguồn/SHA-256, nguyên văn prompt Firefly và công thức xử lý. Không ghi đè phiên bản khác.

`games/.wt-ic-lab-all/src/lab/burst-v2.ts`: chỉ thay dòng độc đang bị comment bằng dòng hoạt động có hậu tố **`-v5`**; giữ ground, scale **1,4**, intensity **1**. `docs/games/tu-tien/skills/VFX_LIBRARY.md`: thêm mục 432, thông số, số đo và giới hạn.

## Chọn đoạn và đóng gói

Dùng `media.decode_analysis/decode_crop`, `grade.crush_black/neutral_fade`, `atlas.write_atlas`, `ktx2.encode` của `tools/vfx-flipbook`; không sửa công cụ.

- Đo đủ **121 khung nguồn 1080²**. Trong 1–3,5 s, diện tích luma BT.709 > 0,05 lớn nhất tại **khung 84, 3,5 s: 520.128 px**. Bbox `maxRGB>12` của khói là `[90,0,1009,967]`, rộng **919 px**; scale theo toàn khối khói, không theo cột giữa.
- Lấy **32 khung 22,24,…,84**, mốc nguồn **0,917–3,5 s** (quanh cửa sổ phiếu yêu cầu); phát **12 fps, 2,667 s**. Lưới **8×4**, ô **256²**, atlas **2048×1024**. Không nội suy hoặc lặp khung.
- Crop cố định **`[-80,-140,1260,1260]`**, đệm đen và thu đồng nhất. Không xoay, ép hình, vignette hoặc mask mép. Pivot cố định **`[0.5,0.65873]`**, từ chân lõi độc **`[550,690]`** của nguồn.
- RGB additive thẳng, không premultiply, không loop; crush `t0=0.02`, `k=0.05`, `greyCut=0.15`, không đổi tông. Khung 0–23 không fade; chỉ **24–31** fade theo `1−smoothstep(0,1,(i−23)/8)`, khung cuối tắt hoàn toàn.
- KTX2 **UASTC mức 2, sRGB, Zstd, Y-flip, 12 mip**; đã giải mã mức 0 và trả Y về hướng PNG trước khi đo.

## Kết quả

| Phép kiểm | PNG | KTX2 giải mã |
| --- | --- | --- |
| Lề nhỏ nhất trái / phải / trên / dưới | 37 / 37 / 33 / 35 px | 37 / 37 / 33 / 35 px |
| Lề tối thiểu, yêu cầu ≥10% | **12,89%** | **12,89%** |
| RGB tối đa trong dải lề 26 px | **0** | **0** |
| Khung đỉnh diện tích sáng sau fade | 25, nguồn 72 / 3,0 s | 25, nguồn 72 / 3,0 s |
| Bề rộng vùng luma >0,05 tại đỉnh, yêu cầu ≥60% | **175/256 = 68,36%** | **175/256 = 68,36%** |
| Luma trung bình và cực đại khung cuối, yêu cầu ≤0,02 | **0 / 0** | **0 / 0** |

**64 lượt kiểm khung đạt**. Dựng lại từng pixel từ nguồn xác nhận crop, 24 khung đầu và đúng tám khung fade; schema cùng toàn bộ khoá với `-v2`. Sai số RGB trung bình sau nén **0,245/255**. SHA-256 xác nhận **78 tệp cũ/nguồn không đổi**, gồm các asset trực tiếp trong poison, video, prompt nguồn và `burst-layers.ts`.

Probe module TypeScript/manifest thật qua symlink `art-src` của lab: JSON/PNG/KTX2 `-v5` đều đọc được, fetch mô phỏng trả **200**, **0 cảnh báo/thiếu tệp**; xác nhận grid `-v5`, cache, từ chối JSON `-v2`, chế độ cũ và fallback 404. **Chưa phải HTTP thật**: thử kết nối `127.0.0.1:3148` thất bại trong sandbox; browser host cũng không khả dụng.

`node games/.wt-ic-lab-all/node_modules/typescript/bin/tsc --noEmit -p games/.wt-ic-lab-all/tsconfig.json`: **exit 0, 0 lỗi**. Không chạy build hoặc bộ test game.

## Bằng chứng và phần cần xem

`/private/tmp/432-poison-v5/` có `ABOUT.md`, `source-12.jpg`, `contact-source.jpg`, **`poison-big-burst-v5-8.jpg`**, script `audit.py`, `full-audit.py`, `package.py`, `verify.py`, `probe.mts`, số đo, checksum, bản chụp code/docs trước sửa và log kiểm kiểu. Đã mở xem các ảnh. Thư mục review SSD ngoài quyền ghi, nên chưa chuyển bằng chứng hoặc cập nhật chỉ mục. Không giữ chuỗi khung thô; RGBA giải mã và các bản staging trùng asset đã xoá.

Chạy lại phép đo và probe:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game
PYTHONDONTWRITEBYTECODE=1 tools/vfx-flipbook/.venv/bin/python -B /private/tmp/432-poison-v5/verify.py
node --import ./games/.wt-ic-lab-all/node_modules/tsx/dist/loader.mjs /private/tmp/432-poison-v5/probe.mts
```

**Giới hạn nguồn:** vài sợi khói mảnh trên đỉnh chạm mép video từ **khung 78, 3,25 s**, trong tail fade đầu ra; khói thấp còn nguyên. Đệm đen tạo lề atlas, không khôi phục phần nguồn đã mất. Owner/coordinator cần xem cỡ, điểm chạm đất và đoạn tan trong lab, xác nhận HTTP/GPU. Chưa chấm hiệu ứng tổng hợp 8,5.

Không bỏ bước xử lý asset nào; phần HTTP/trình duyệt và lưu review SSD chưa làm được vì giới hạn môi trường nêu trên. Không sửa lớp phụ, game khác hoặc công cụ; không stage media, đổi nhánh, commit, push, reset, clean hoặc stash.
