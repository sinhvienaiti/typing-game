# Phiếu 369 · Bộ UI jewel-crest

Hoàn tất **19/19 ảnh**; **19/28 image_gen**, **24/30 view_image**. Tham chiếu Bàn Quyết, Ám jewel-crest và 12 icon `try1` của 363; giữ vật thể và màu nhận diện.

Đường dẫn tính từ `games/immortality-cultivation/art-src/`:

- `ui/frames/{hud-bar,wave-card,shop,harvest,menu,settings,sound}-jewel-crest.v1-try1.png`: đủ bảy khung, đúng khổ phiếu.
- `ui/icons/hud-<tên>-jewel-crest.v1-try1.png`: đủ 12 tên; mỗi icon có `-48.png`, `-32.png`.
- `ui/ui-369-sheet.jpg`: tám khung kể cả mẫu Bàn Quyết, cùng tỉ lệ 40%; 12 icon ở 256/48/32 px.
- Mỗi ảnh có `.prompt.txt` ghi prompt, tham chiếu, hậu xử lý; tấm ghép có mô tả.

**Kiểm bằng Python nội tuyến + ImageMagick 7:** 43 PNG đúng kích thước, có alpha, lề ≥8%; đã nhìn mép và bản 32 px. Khung được flood-fill nền xanh, khử spill; icon bỏ nhiễu alpha dưới 8/255. Cạnh lặp hoà mép 8 px bằng chính ảnh vẽ; so cột/hàng đầu-cuối: ΔRGBA tối đa **0/255**. Inset từng khung ghi trong prompt. Tương phản chữ trắng ở vùng giữa: **≥18,3:1**.

Tự chấm theo mặt yếu nhất:

| Nhóm / tên | Điểm |
|---|---:|
| HUD / wave / shop / harvest / menu / settings / sound | 8,2 / 8,4 / 8,5 / 8,5 / 8,4 / 8,5 / 8,5 |
| Heal / shield / haste | 8,3 / 8,5 / 8,3 |
| Sword-stake / thunder-pillar / seal-net | 8,0 / 8,3 / 8,4 |
| Spirit-stone / jade / merit | 8,5 / 8,6 / 8,4 |
| Settings / sound / sound-muted | 8,0 / 8,3 / 8,3 |

Không mẫu dưới 8. Anh xem kỹ **Kiếm Thung và Settings ở 32 px**. Không bỏ ảnh nào; chưa tích hợp hoặc nghiệm thu độc lập trong game. Giữ nguyên 363; không sửa mã, chạy build/test hay ghi Git.
