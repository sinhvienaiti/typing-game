# Phiếu 354 · Tu Tiên · Ảnh 2D: trận pháp lôi bản bạc lam nhạt (nền cho bạch kim lôi, D65)

Theo D65 (12/11): tia sét giờ là trắng ngà và vàng kim nhạt, nên trận pháp (lớp nền) chuyển sang **bạc lam nhạt, mờ** để tương phản ấm lạnh và giữ thứ bậc (D64: trận nhạt hơn tia rõ rệt). Chỉ vẽ ảnh, không sửa mã. Chạy sau phiếu 353.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 4 lần gọi `image_gen`** (A bạc, vành rời bạc, tối đa 2 vẽ lại). `view_image` tối đa 6. Báo cáo: `docs/codex-queue/354-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-array-silver-*.v1-try*.png`, `.prompt.txt`, tấm ghép. Cấm git ghi, sửa file có sẵn, mở cổng, ảnh ngoài repo, sửa mã.

## Tham chiếu (`view_image`)
`S/thunder-array-a.v1-try2.png` (bố cục A bát quái, chữ triện: **giữ nguyên bố cục**), `S/thunder-array-ring.v1-try1.png` (vành rời), và tia mới `S/thunder-five-strike.v3-try1.png` (tia sẽ đè lên; trận phải lạnh và nhạt hơn hẳn).

## Màu mới
Nét khắc **bạc lam nhạt** (khoảng `#9FB3C8` tới `#C9D6E3`), bão hoà thấp (S ≤ 0,3), lõi và năm nút sáng trắng bạc dịu; quầng mềm rất nhẹ; hạt sáng thưa. Độ sáng trung vị của trận ≤ 0,6 lần lõi tia tham chiếu. Không xanh điện bão hoà, không tím, không vàng. Nền đen thuần, lề ≥ 10 %, tròn hoàn hảo, 1:1, tâm thoáng.

## Hai ảnh
`S/thunder-array-silver-a.v1-try1.png` (bố cục A), `S/thunder-array-silver-ring.v1-try1.png` (vành chữ triện rời, tâm đen thuần ≥ 55 % đường kính).

## Kiểm và tự chấm
Nền, lề, tròn; đo: tỉ lệ sáng trận/tia ≤ 0,6; S trung vị ≤ 0,3; không có điểm sắc 45–60° bão hoà. Tự chấm theo mặt yếu nhất: lùi về nền nhưng vẫn huyền bí tu tiên; giữ bố cục; tâm thoáng; hợp với tia bạch kim. Dưới 8 vẽ lại một lần.

## Xong khi
2 ảnh + prompt + `S/thunder-array-354-sheet.jpg` (trận bạc, vành, và ô ghép thử tia v3 thu nhỏ đè lên) + báo cáo có bảng số.
