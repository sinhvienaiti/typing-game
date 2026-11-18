# Phiếu 414: Đóng gói lại 5 atlas bùng nổ bị chạm mép (thêm lề, không tạo lại)


Phản biện: PASS (Sonnet, 16/11, vòng 2)
## Bối cảnh
Kiểm 59 clip bùng nổ ngày 16/11 (`docs/work/tasks/burst-audit.md`): một số clip đạt về nội dung nhưng hình chạm hoặc bị cắt ở mép ô atlas. Những clip **không** nằm trong danh sách làm lại bằng Firefly (mục "Gộp hai giám khảo") có thể cứu bằng đóng gói lại. Công cụ: `tools/vfx-flipbook/` (`run.sh`, cấu hình `immortality-cultivation.json`).

## Việc
1. Đúng 5 clip sau (đều có trong `games/immortality-cultivation/art-src/lab/vfx/`): `thunder/thunder-impact`, `thunder/thunder-ground-impact`, `wood/wood-ring-burst` (chạm mép), `star/star-ring-burst`, `metal/metal-ring-burst` (lề hẹp ~96 %). Các clip chạm mép khác đều nằm trong 20 clip làm lại bằng Firefly nên không làm ở đây.
2. Với mỗi clip: đóng gói lại từ video nguồn (nếu còn) hoặc từ atlas hiện có, thu nhỏ hình trong ô để lề ≥ 10 % mọi cạnh ở mọi khung; giữ số khung, kích thước atlas, định dạng KTX2 và json như cũ. Nếu hình đã bị cắt trong nguồn (mất nội dung), không cứu được: ghi vào báo cáo để chuyển sang danh sách làm lại.
3. Ghi bản mới với hậu tố `-m` (ví dụ `thunder-impact-m.atlas.png`, `.json`, `.uastc.ktx2`); **không ghi đè** bản cũ (luật: giữ asset cũ trong thư viện). Cập nhật `docs/games/tu-tien/skills/VFX_LIBRARY.md`.
4. Tạo ảnh ghép trước/sau mỗi clip (6 khung) để kiểm lề.

## Nghiệm thu
- Script đo lề tự động: mọi khung của bản `-m` có lề ≥ 10 % (pixel sáng hơn ngưỡng nền không chạm vùng 10 % mép). Ghi số đo từng clip.
- Ảnh ghép trước/sau trong `typing-game-review/captures/tu-tien/burst-repack/` (nếu sandbox chặn ghi, để trong báo cáo đường dẫn tạm và lệnh copy).
- Chỉ ghi file mới trong `games/immortality-cultivation/art-src/lab/vfx/<hệ>/` và `VFX_LIBRARY.md`. Không sửa code game/lab, không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/414-report.md`.
