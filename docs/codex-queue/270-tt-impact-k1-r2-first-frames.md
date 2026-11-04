# Phiếu 270 · Tu Tiên · Khung đầu va chạm phím 1 (Brushfire), lượt sửa: 3 lần gọi `image_gen`

**Vì sao Codex vẽ:** lúc 14:10 ngày 04/11/2026 trình duyệt trong app mất đăng nhập ChatGPT, Gemini và Firefly. Luật `agent-orchestration` (bước 9): khi ChatGPT và Gemini không vào được thì Codex `image_gen` vẽ theo thiết kế đã chốt. Thiết kế và prompt đã qua duyệt hai lần (ChatGPT FAIL, FAIL, PASS, PASS; Gemini FAIL, PASS, PASS) và Claude đã đo lượt đầu.

**Model `gpt-6.1-sol`, mức `high`. Đúng 3 lần gọi `image_gen`, không gọi thêm.** Không tự sửa lại, không vẽ biến thể khác. Claude đo và quyết lượt sau.

**Báo cáo:** `docs/codex-queue/270-report.md` (tiếng Việt, ngắn).

## Đường dẫn

**Được ghi:**
- `games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/` (chỉ thêm file mới, không ghi đè file có sẵn);
- `docs/codex-queue/270-report.md`.

**Cấm:** mọi lệnh git trừ `status`, `diff`, `log`, `show`; sửa bất cứ file nào khác; mở trình duyệt; chạy dev server, build hay test; đính kèm vào `image_gen` bất cứ ảnh nào ngoài ảnh nguồn ghi trong bảng dưới.

## Việc: 3 ảnh, mỗi ảnh một lần gọi `image_gen` ở chế độ sửa ảnh (edit)

Thư mục `D = games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2`.

| Tên ra | Ảnh nguồn (chỉ đính kèm ảnh này, vai trò: edit target) | Prompt |
|---|---|---|
| `fire-impact-k1-r2-v1a.try2` | `D/fire-impact-k1-r2-v1a.try1.src1254.png` | Prompt R1 |
| `fire-impact-k1-r2-v1b.try2` | `D/fire-impact-k1-r2-v1b.try1.src1254.png` | Prompt R2 |
| `fire-impact-k1-r2-v3.try1` | `games/immortality-cultivation/art-src/lab/vfx/first-frames/fire-impact-k1/fire-impact-k1-v3.try1.png` | Prompt V3 |

Cách làm mỗi ảnh:
1. Mở ảnh nguồn bằng `view_image`, rồi gọi `image_gen` sửa đúng ảnh đó, khổ vuông 1:1. **Prompt dán nguyên văn**, không thêm, không bớt, không viết lại theo khung mẫu của skill `imagegen`.
2. Chép ảnh trả về từ `~/.codex/generated_images/...` bằng `cp -n` thành `D/<tên ra>.src.png` (giữ nguyên khổ thật nhận được, ghi khổ vào báo cáo).
3. Thu về 1080×1080, không kéo giãn:
   `magick D/<tên ra>.src.png -alpha off -colorspace sRGB -filter Lanczos -define filter:clamp=true -resize 1080x1080 -background '#000000' -gravity center -extent 1080x1080 -depth 8 PNG24:D/<tên ra>.png`
4. Ghi prompt nguyên văn vào `D/<tên ra>.prompt.txt`.
5. Đo tự động: `/Applications/Blender.app/Contents/Resources/5.2/python/bin/python3.13 -I docs/codex-queue/270/auto.py D/<tên ra>.png`, chép dòng JSON vào báo cáo. Không sửa ảnh theo kết quả đo.

Nếu `image_gen` báo hết lượt (429, "try later"), làm theo luật chờ trong phần đầu phiếu; không đổi sang công cụ khác.

### Prompt R1 (nguyên văn)

```text
Edit the attached image, our own painting. Keep the square opaque pure-black canvas, the framing, the lower-left strike root, the flame colours, the soft living flame texture and the paths of the long and middle strokes. Change only these four things. 1) Move the white-gold line to the OUTER convex edge of each of the three strokes, the edge that faces away from the centre of its curve (the upper-left side of each arc): a razor-thin, slightly broken white-gold line running along that outer edge for most of each stroke's length, about 3 to 4 percent of the flame area, plus two or three tiny pinpoint glints. Remove the white line from the middle and from the inner concave side; the inner side stays orange and red, and its flame tongues peel inward toward the centre of the curve. 2) Keep the longest stroke heaviest in its lower-left third, then narrow it steadily so its upper-right third is a slim curved blade no more than a quarter as wide as its widest part, ending in a needle tip; trim the flame tongues along that last third. 3) Make the shortest inner stroke curl more, like a small hook: it rises from the root, bends over to the right and its needle tip ends pointing down-right, a curve of about 140 degrees. 4) Separate the short stroke from the middle stroke with a clear black gap everywhere except right at the shared root. No fourth stroke, C-shape, ring, lotus, bird, smoke, bloom, lens flare, bokeh, ground, sword or text.
```

### Prompt R2 (nguyên văn)

```text
Edit the attached image, our own painting. Keep the square opaque pure-black canvas, the framing, the lower-left strike root, the flame colours, the soft living flame texture and the paths of the long and middle strokes. Change only these five things. 1) Reduce the white: replace the wide white-hot areas, including the white patch at the root, with orange and amber, and keep white-gold only as a razor-thin, slightly broken line along the OUTER convex edge of each of the three strokes, the edge that faces away from the centre of its curve (the upper-left side of each arc), about 3 to 4 percent of the flame area, plus two or three tiny pinpoint glints. The inner concave side stays orange and red, and its flame tongues peel inward toward the centre of the curve. 2) Keep the longest stroke heaviest in its lower-left third, then narrow it steadily so its upper-right third is a slim curved blade no more than a quarter as wide as its widest part, ending in a needle tip; trim the flame tongues along that last third. 3) Make the shortest inner stroke curl more, like a small hook: it rises from the root, bends over to the right and its needle tip ends pointing down-right, a curve of about 140 degrees. 4) Separate the short stroke from the middle stroke with a clear black gap everywhere except right at the shared root. 5) Keep at most two small detached ember specks and remove every other loose spark. No fourth stroke, C-shape, ring, lotus, bird, smoke, bloom, lens flare, bokeh, ground, sword or text.
```

### Prompt V3 (nguyên văn; prompt A2-v3 đã qua duyệt hai lần)

```text
Edit the attached painting into a 1:1 square opaque pure-black canvas by reframing the entire flame fan inward so at least 10 percent pure-black margin surrounds all four sides, without cropping, stretching, rotating or mirroring. Keep the lower-left strike root and resolve the flame into exactly three separate OPEN strokes: two long crescents sweeping up-right (curving between 120 and 160 degrees, never closing into a C or ring) and one short counter-stroke flicking sharply left at the root. Do not lengthen the short left flick into a third crescent. Give all three strokes heavy irregular roots that taper smoothly to needle-fine tips at most one-third of their root width. Use a stepped anime/donghua fire palette of deep crimson, vermilion, bright tangerine and warm amber with soft living interior tongues. Narrow the existing pale ivory white-gold highlights into a razor-thin, slightly broken line strictly hugging each convex leading outer edge (covering only 3 to 4 percent of the flame area) plus two or three tiny pinpoint glints. Include at most two small detached ember specks; merge any other loose bits into the three strokes. No fourth stroke, C-shape, ring, lotus, bird, smoke, bloom, lens flare, bokeh, ground, sword or text.
```

## Xong khi
- Có đủ 3 bộ `<tên ra>.src.png`, `<tên ra>.png` (1080×1080), `<tên ra>.prompt.txt` trong `D`.
- Báo cáo ghi: khổ thật của từng ảnh trả về, dòng JSON đo tự động, số lần gọi `image_gen` (phải là 3), và một câu nhận xét ngắn mỗi ảnh (có giữ ba nét mở không, đường trắng vàng nằm ở mép nào).
