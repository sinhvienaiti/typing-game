# Phiếu 270d · Tu Tiên · Va chạm phím 1 (Brushfire): khung cuối A3, lượt sửa, 3 lần gọi `image_gen`

Tiếp phiếu 270c (cùng lý do: trình duyệt trong app mất đăng nhập ChatGPT và Gemini). Claude đã đo hai khung cuối `v1a.end-a`, `v1a.end-b`: nét nằm đúng chỗ (98 % điểm sáng nằm trong 2 px quanh khung đầu), nhưng quá tối: vùng sáng (luma > 0,1) chỉ 7–8 % khung đầu, cần 15–35 %. Prompt A3-R dưới đây giữ nguyên prompt A3 đã duyệt, chỉ thêm yêu cầu phần còn lại vẫn cháy sáng. Khung đầu chính là `v1a.try3`, khung đầu phụ là `v3.try3`.

**Model `gpt-6.1-sol`, mức `high`. Đúng 3 lần gọi `image_gen`, không gọi thêm, không tự sửa lại.**

**Báo cáo:** `docs/codex-queue/270d-report.md` (tiếng Việt, ngắn).

## Đường dẫn

**Được ghi:** `games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/` (chỉ thêm file mới, không ghi đè) và `docs/codex-queue/270d-report.md`.

**Cấm:** như phiếu 270.

## Việc

Thư mục `D = games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2`. Cách làm mỗi ảnh giống hệt phiếu 270, bước 1–5. Mỗi ảnh đính kèm lại đúng khung đầu 1080 của nó, không sửa từ một khung cuối khác.

| Tên ra | Ảnh nguồn (edit target, chỉ ảnh này) | Prompt |
|---|---|---|
| `fire-impact-k1-r2-v1a.end-a.try2` | `D/fire-impact-k1-r2-v1a.try3.png` | Prompt A3-R |
| `fire-impact-k1-r2-v1a.end-b.try2` | `D/fire-impact-k1-r2-v1a.try3.png` | Prompt A3-R |
| `fire-impact-k1-r2-v3.end-a.try1` | `D/fire-impact-k1-r2-v3.try3.png` | Prompt A3-R |

### Prompt A3-R (nguyên văn, dùng cho cả ba)

```text
Edit the attached image in place on the exact same opaque pure-black 1:1 canvas. Keep the lower-left root and all three stroke paths locked at their exact pixel coordinates; do not shift, scale, rotate, extend or reconnect anything. Show the same three strokes late in their burn-down: needle tips vanished, middle sections broken into small separated islands, roots still burning. The surviving roots and islands must still glow clearly in orange-red and amber, not dim dark red, so the glowing area is about one quarter to one third of the attached image's flame area, densest at the roots and thinning toward the tips, with two or three tiny dying ember specks along the original paths and almost no white-gold. No new flames, arcs, C-shape, ring, lotus, bird, smoke, glow haze or text.
```

## Xong khi
- Có đủ 3 bộ `.src.png`, `.png` (1080×1080), `.prompt.txt` trong `D`.
- Báo cáo ghi khổ thật, dòng JSON đo tự động, số lần gọi `image_gen` (phải là 3) và một câu nhận xét mỗi ảnh.
