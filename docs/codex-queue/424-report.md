# Phiếu 424 — hai flipbook dáng rộng Sét/Huyết -v3

Ngày 16/11/2026. **Đã xuất 2/2 bộ, nối lab; kiểm lề, schema, probe và kiểu dữ liệu PASS.** Không tạo ảnh/video AI mới.

## Tệp đã làm

Gốc `games/immortality-cultivation/art-src/lab/vfx/`:

- `thunder/thunder-impact-v3.{atlas.png,json,uastc.ktx2,prompt.txt}`, từ `thunder/firefly-raw/thunder-impact.v4-try2.mp4`.
- `blood/blood-big-burst-v3.{atlas.png,json,uastc.ktx2,prompt.txt}`, từ `blood/firefly-raw/blood-big-burst.v4-try1.mp4`.
- `games/.wt-ic-lab-all/src/lab/burst-v2.ts`: chỉ thêm lại hai hàng, hậu tố `-v3`; khôi phục hệ số trước 423: Huyết scale 0,401 / intensity 8,871, Sét scale 0,585 / intensity 1,15. Độc vẫn dùng nguồn cũ.
- `docs/games/tu-tien/skills/VFX_LIBRARY.md`: thêm mục 424 và các số đo, ghi rõ trạng thái mới thay phần chờ Sét/Huyết của 423.

Tổng **8 tệp asset mới, 1.777 MiB**. Không ghi đè bản cũ. Prompt cạnh từng bộ ghi thao tác chính xác, đường dẫn/SHA-256 nguồn, ảnh repo tham chiếu từ prompt Firefly nguyên văn, chỉ số khung, crop, pivot, fade và nén.

## Đóng gói và kết quả kiểm

Dùng trực tiếp `media.decode_crop`, `grade.crush_black`, `grade.neutral_fade`, `atlas.write_atlas`, `ktx2.encode` của `tools/vfx-flipbook/`; script điều phối chỉ nằm trong thư mục tạm, không sửa công cụ/cấu hình/manifest cũ.

Cả hai: **32 khung**, nguồn **0–62 bước 2**, phát **12 fps**, dài **2,667 s**, lưới **8×4**, ô **256×256**, atlas **2048×1024**; RGB additive, không premultiply, không loop. Giữ góc 55° bằng crop vuông cố định, thu nhỏ đồng nhất, `rotate=0`, `flipX=false`, `squashY=1`; không vignette hoặc che mép. Crush đen `t0=0.02`, `greyCut=0.15`, `whiteFix=off`. Tail fade smoothstep 10 khung cuối, kết thúc RGB 0.

| Bộ | Crop nguồn | Điểm chạm nguồn / pivot ô | Lề PNG và KTX2 giải mã trái/phải/trên/dưới |
| --- | --- | --- | --- |
| Sét | `[-96,-96,1272,1272]` | `[540,675]` / `[0.5,0.606132]` | **65 / 56 / 43 / 45 px; 16,80%** |
| Huyết | `[-182,-182,1444,1444]` | `[540,690]` / `[0.5,0.603878]` | **40 / 48 / 46 / 71 px; 15,62%** |

Đã đo mép toàn bộ video trước xử lý: Sét không có pixel >12 chạm mép; Huyết chạm mép đầu tiên ở khung **66**, nên dừng khung 62. Mép nguồn trong đoạn chọn tối đa **3/255**. Đã xem hai bảng nguồn 12 khung: chỉ năng lượng nền đen, không sinh vật, đồ vật hoặc cảnh nền; owner đã chọn A/B theo phiếu. Ghi kiểm nội dung trong prompt cạnh asset, không tự sửa manifest ngoài phạm vi.

**128 lượt kiểm khung PASS:** 64 PNG + 64 KTX2 giải mã mức 0, ngưỡng `maxRGB>12`, yêu cầu lề ít nhất 26 px mỗi cạnh. Toàn dải lề 10% có RGB tối đa **0**. JSON có đúng tập khoá gốc, `source`, `trim` như atlas cũ; fps/chỉ số/crop/pivot/phiên bản phản ánh bộ mới. KTX2 UASTC mức 2, sRGB, Zstd, Y-flip, **12 mip**; giải mã và đảo Y về PNG trước khi đo. SHA-256 xác nhận **8 tệp nguồn/bản cũ** không đổi.

Probe chạy module TypeScript thực, đọc manifest/JSON thật và kiểm tệp PNG/KTX2: **16 hàng, 16 JSON, không cảnh báo/404**; Sét/Huyết nạp đúng `-v3` ở JSON, PNG, KTX2 và grid; từ chối JSON `-v2` cũ cho hai tên. Kiểm cache, `burst=old`, fallback 404 và nguồn Độc giữ nguyên đều đạt. Fetch được mô phỏng bằng đọc tệp, không phải kiểm HTTP qua trình duyệt.

`node games/.wt-ic-lab-all/node_modules/typescript/bin/tsc --noEmit -p games/.wt-ic-lab-all/tsconfig.json`: **exit 0, 0 lỗi**. Không chạy build hoặc bộ test game.

## Bằng chứng và chạy lại

Thư mục yêu cầu trên SSD nằm ngoài quyền ghi. Dùng fallback được phiếu cho phép: **`/private/tmp/424-burst-v3/`**, có `ABOUT.md`.

- `thunder-impact-before-after.jpg`, `blood-big-burst-before-after.jpg`: tám cặp khung **atlas cũ đang dùng | -v3**, cùng phần trăm thời lượng; khung xanh lề 10%, dấu cam pivot, font Arial. Đã mở xem cả hai.
- Hai `*-source-qa.jpg` có 12 mốc/clip; mọi ảnh có `.prompt.txt` mô tả phép ghép.
- `audit.py`, `package.py`, `verify.py`, `probe.mts`; số đo `source-audit.json`, `metrics.json`, `final-validation.json`, `probe.json`, `original-sha256.json`, log `typecheck.txt`.
- Không lưu khung thô; đã xoá staging atlas trùng do phiên này tạo. Chỉ giữ asset chính và bằng chứng cần dùng.

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game
PYTHONDONTWRITEBYTECODE=1 tools/vfx-flipbook/.venv/bin/python -B /private/tmp/424-burst-v3/verify.py
node --import ./games/.wt-ic-lab-all/node_modules/tsx/dist/loader.mjs /private/tmp/424-burst-v3/probe.mts
```

Coordinator có thể chuyển bằng chứng khi ở ngoài sandbox rồi cập nhật chỉ mục:

```sh
mkdir -p /Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/burst-v3
cp -Rn /private/tmp/424-burst-v3/. /Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/burst-v3/
cd /Volumes/SS990TPRO/htdocs/typing-game
node scripts/review-index.mjs
```

## Bỏ qua và việc owner cần xem

**Không bỏ clip nào.** Chưa chuyển review SSD/cập nhật chỉ mục do ngoài quyền ghi; chưa kiểm host/trình duyệt/GPU hoặc chấm hiệu ứng tổng hợp 8,5. Owner/coordinator cần xem hai ảnh và cỡ/độ sáng/điểm chạm trong lab: các hệ số hiển thị giữ từ trước 423, chưa hiệu chỉnh lại cho nguồn dáng rộng; Huyết có vành/tia dựng lên từ đoạn sau theo chính video nguồn. Không sửa các thuộc tính này ngoài yêu cầu thêm hai dòng ánh xạ.

Chỉ ghi tám asset mới, hai tệp sửa được phép, báo cáo này và thư mục tạm. Không sửa src/scripts/tests/docs khác của game; không đổi nhánh, stage media, commit, push, reset, clean hoặc stash. Một luồng, không subagent; quota đọc lúc bắt đầu còn **17%**.
