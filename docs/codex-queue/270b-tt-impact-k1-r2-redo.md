# Phiếu 270b · Tu Tiên · Khung đầu va chạm phím 1 (Brushfire), lượt sửa cuối: 3 lần gọi `image_gen`

Tiếp phiếu 270 (cùng lý do: trình duyệt trong app mất đăng nhập ChatGPT và Gemini). Claude đã đo ba ảnh của phiếu 270; mỗi prompt dưới đây chỉ sửa đúng chỗ còn trượt. Đây là lượt sửa cuối của mỗi khung.

**Model `gpt-6.1-sol`, mức `high`. Đúng 3 lần gọi `image_gen`, không gọi thêm, không tự sửa lại.**

**Báo cáo:** `docs/codex-queue/270b-report.md` (tiếng Việt, ngắn).

## Đường dẫn

**Được ghi:** `games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/` (chỉ thêm file mới, không ghi đè) và `docs/codex-queue/270b-report.md`.

**Cấm:** như phiếu 270 (git chỉ `status`, `diff`, `log`, `show`; không sửa file khác; không trình duyệt, dev server, build, test; không đính kèm ảnh nào ngoài ảnh nguồn trong bảng).

## Việc

Thư mục `D = games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2`. Cách làm mỗi ảnh giống hệt phiếu 270, bước 1–5 (`view_image` ảnh nguồn, `image_gen` sửa đúng ảnh đó ở khổ vuông với prompt dán nguyên văn, `cp -n` thành `.src.png`, thu về 1080×1080 bằng đúng lệnh `magick` của phiếu 270, ghi `.prompt.txt`, chạy `docs/codex-queue/270/auto.py`).

| Tên ra | Ảnh nguồn (edit target, chỉ ảnh này) | Prompt |
|---|---|---|
| `fire-impact-k1-r2-v1a.try3` | `D/fire-impact-k1-r2-v1a.try2.src.png` | Prompt S1 |
| `fire-impact-k1-r2-v1b.try3` | `D/fire-impact-k1-r2-v1b.try2.src.png` | Prompt S2 |
| `fire-impact-k1-r2-v3.try2` | `D/fire-impact-k1-r2-v3.try1.src.png` | Prompt S3 |

### Prompt S1 (nguyên văn)

```text
Edit the attached image, our own painting. Keep the square opaque pure-black canvas, the framing, the lower-left strike root, the long stroke, the flame colours and the soft living flame texture. Change only these four things. 1) The short inner hook curls too far: open it so it bends through only about 150 degrees; it rises from the root, arches over to the right, and its needle tip ends pointing to the right and slightly down, not straight down. 2) Narrow the right half of the middle stroke into a slim curved blade no more than a third as wide as its root, ending in a needle tip; trim the flame tongues along that right half. 3) Make the white-gold line along the OUTER convex edge of each stroke (the upper-left side of each arc) a clearly visible bright line 2 to 3 pixels thick, slightly broken, running along most of each stroke's length and only on that outer edge, about 3 percent of the flame area. 4) Open a clear thin black gap between the short hook and the middle stroke starting just above the shared root. No fourth stroke, C-shape, ring, lotus, bird, smoke, bloom, lens flare, bokeh, ground, sword or text.
```

### Prompt S2 (nguyên văn)

```text
Edit the attached image, our own painting. Keep the square opaque pure-black canvas, the framing, the lower-left strike root, the long and middle strokes, the flame colours and the soft living flame texture. Change only these three things. 1) The short inner hook curls too far: open it so it bends through only about 150 degrees; it rises from the root, arches over to the right, and its needle tip ends pointing to the right and slightly down, not straight down. 2) Make the white-gold line along the OUTER convex edge of each stroke (the upper-left side of each arc) a clearly visible bright line 2 to 3 pixels thick, slightly broken, running along most of each stroke's length and only on that outer edge, about 3 percent of the flame area; no white inside the stroke bodies. 3) Open a clear thin black gap between the short hook and the middle stroke starting just above the shared root. No fourth stroke, C-shape, ring, lotus, bird, smoke, bloom, lens flare, bokeh, ground, sword or text.
```

### Prompt S3 (nguyên văn)

```text
Edit the attached image, our own painting. Keep the square opaque pure-black canvas, the framing, the lower-left strike root, the short counter-stroke flicking left at the root, the flame colours and the soft living flame texture. Change only these three things. 1) Curve both long strokes more, like crescent moons, about 140 degrees each: the upper long stroke leaves the root heading up and slightly left, bends over the top and ends in a needle tip heading right and slightly down; the lower long stroke leaves the root heading straight up, bends to the right and ends in a needle tip heading right and slightly down. They stay open fans, never closing into a C or ring. 2) Move the white-gold line to the OUTER convex edge of each long stroke (the upper-left side of each arc): a clearly visible bright line 2 to 3 pixels thick, slightly broken, along most of each stroke's length, about 3 percent of the flame area; remove the white line from inside the stroke bodies, and let the flame tongues peel off the inner concave side. 3) Keep a clear black gap between the two long strokes from just above the shared root. No fourth stroke, C-shape, ring, lotus, bird, smoke, bloom, lens flare, bokeh, ground, sword or text.
```

## Xong khi
- Có đủ 3 bộ `.src.png`, `.png` (1080×1080), `.prompt.txt` trong `D`.
- Báo cáo ghi khổ thật, dòng JSON đo tự động, số lần gọi `image_gen` (phải là 3) và một câu nhận xét mỗi ảnh.
