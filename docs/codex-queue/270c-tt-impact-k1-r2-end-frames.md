# Phiếu 270c · Tu Tiên · Va chạm phím 1 (Brushfire): khung cuối A3 cho v1a và lượt sửa cuối v3, 3 lần gọi `image_gen`

Tiếp phiếu 270 và 270b (cùng lý do: trình duyệt trong app mất đăng nhập ChatGPT và Gemini). Claude đã đo các khung đầu và chọn `v1a.try3` làm khung đầu chính. Prompt A3 là bản cuối đã qua duyệt hai lần (ChatGPT, rồi Gemini).

**Model `gpt-6.1-sol`, mức `high`. Đúng 3 lần gọi `image_gen`, không gọi thêm, không tự sửa lại.**

**Báo cáo:** `docs/codex-queue/270c-report.md` (tiếng Việt, ngắn).

## Đường dẫn

**Được ghi:** `games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/` (chỉ thêm file mới, không ghi đè) và `docs/codex-queue/270c-report.md`.

**Cấm:** như phiếu 270.

## Việc

Thư mục `D = games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2`. Cách làm mỗi ảnh giống hệt phiếu 270, bước 1–5 (`view_image` ảnh nguồn, `image_gen` sửa đúng ảnh đó ở khổ vuông với prompt dán nguyên văn, `cp -n` thành `.src.png`, thu về 1080×1080 bằng đúng lệnh `magick` của phiếu 270, ghi `.prompt.txt`, chạy `docs/codex-queue/270/auto.py`).

| Tên ra | Ảnh nguồn (edit target, chỉ ảnh này) | Prompt |
|---|---|---|
| `fire-impact-k1-r2-v1a.end-a.try1` | `D/fire-impact-k1-r2-v1a.try3.png` (bản 1080) | Prompt A3 |
| `fire-impact-k1-r2-v1a.end-b.try1` | `D/fire-impact-k1-r2-v1a.try3.png` (bản 1080), đính kèm lại, **không** sửa từ `end-a` | Prompt A3 |
| `fire-impact-k1-r2-v3.try3` | `D/fire-impact-k1-r2-v3.try2.src.png` | Prompt S4 |

### Prompt A3 (nguyên văn, dùng cho cả `end-a` và `end-b`)

```text
Edit the attached image in place on the exact same opaque pure-black 1:1 canvas. Keep the lower-left root and all three stroke paths locked at their exact pixel coordinates; do not shift, scale, rotate, extend or reconnect anything. Show the same three strokes late in their burn-down: needle tips completely vanished, middle sections broken into small separated orange-red islands, and thick roots cooled into dark crimson and muted ember cores, with two or three tiny dying ember specks along the original paths. Total lit flame area must be about one-quarter of the attached image, with almost no white-gold remaining. No new flames, arcs, C-shape, ring, lotus, bird, smoke, glow haze or text.
```

### Prompt S4 (nguyên văn)

```text
Edit the attached image, our own painting. Keep the square opaque pure-black canvas, the lower-left strike root, the short counter-stroke flicking left at the root, the lower long stroke, the white-gold outer edge lines, the flame colours and the soft living flame texture. Change only one thing: the upper long stroke curls too far and makes the fan read like a letter C. Open it so it bends through only about 130 degrees: it leaves the root heading up, bends over to the right, and its needle tip ends heading right and level, ending well above the lower stroke's tip instead of curling down toward it. The two long strokes stay an open fan with wide black air between their tips. No fourth stroke, C-shape, ring, lotus, bird, smoke, bloom, lens flare, bokeh, ground, sword or text.
```

## Xong khi
- Có đủ 3 bộ `.src.png`, `.png` (1080×1080), `.prompt.txt` trong `D`.
- Báo cáo ghi khổ thật, dòng JSON đo tự động, số lần gọi `image_gen` (phải là 3) và một câu nhận xét mỗi ảnh (khung cuối: nét có nằm đúng chỗ cũ không, mũi kim đã tắt chưa).
