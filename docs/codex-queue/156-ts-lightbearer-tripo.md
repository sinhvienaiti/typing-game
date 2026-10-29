# Phiếu 156 · Last Line · Ảnh nguồn Tripo: Lightbearer (3 góc) và 5 súng canh

**Nguồn:** chủ dự án chọn hướng B · Lightbearer ngày 29/10/2026 sáng. Bible ở `docs/games/ART_DIRECTION_2026-10-28.md` §4.3, mục "Model": chủ dự án dựng trên Tripo (bằng tay trên web) nhân vật Lightbearer có rig người và 5 súng canh bay, mỗi súng một dáng theo icon súng có sẵn. Phiếu này vẽ ảnh nguồn cho các model đó. Con tàu Vanguard bị bỏ.

**Báo cáo:** `docs/codex-queue/156-report.md`.

## Luật chung (phiếu ảnh, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Mức nhận:** chấm theo game thương mại. Ảnh tham chiếu của chủ dự án: `games/typing-survival/art-src/_refs/owner-epic-2026-10-28.webp` (nhân vật áo choàng: dáng rõ, chất liệu giáp và vải thật). Không chép nội dung.
- **Ảnh hướng đã chọn (bắt buộc đính kèm):** `games/typing-survival/art-src/concepts/b-lightbearer-fight.png` và `b-lightbearer-keyart.png`, với dòng `Use the attached images only to keep the same hero design, armour, cape, visor, colours and the sentinel guns' look. Draw the new view as described.`
- **Tối đa 3 lượt sinh mỗi ảnh.** Mỗi lượt sửa prompt đúng chỗ thiếu. Lỗi sửa được bằng công cụ thì sửa bằng công cụ trước.
- **Mọi lượt sinh** giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt`. Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **Script đã dùng** lưu ở `_review/156/`, chạy lại được.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
  - mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo của phiếu);
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex; gọi Tripo, Meshy hay API 3D nào;
  - ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, hình hiệu trong ảnh.
- **KA1 md5:** `md5 -r` mọi file trong `games/typing-survival/art-src/` (đệ quy) trước khi ghi (`_review/156/md5-before.txt`) và sau khi giao. `diff` chỉ có dòng thêm.
- **KA5 mức chợ:** M (ART_DIRECTION §1.3) và Q (`ART_ACCEPTANCE.md` §2.2; "Dùng tiếp" được 2 khi ảnh dựng 3D được: một khối liền, đúng góc, không bị cắt). Đạt khi **M ≥ 8 và Q ≥ 8**.
- **Báo cáo** tiếng Việt: prompt đã sửa gì từng lượt; bảng số đo; điểm M và Q; đường dẫn ảnh kiểm; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chấm lại M ≥ 8 và Q ≥ 8. Sau đó Claude gửi chủ dự án danh sách dựng Tripo.

## Phiếu

**Nơi ghi:** `games/typing-survival/art-src/models-src/` (thư mục mới).

**Chỉ được ghi:**
- `models-src/<tên>.tryN.png`, `.tryN.prompt.txt`, bản chọn `<tên>.png`, `<tên>.prompt.txt`;
- `games/typing-survival/art-src/_review/156-*.jpg`, `games/typing-survival/art-src/_review/156/`;
- `docs/codex-queue/156-report.md`.

**Đọc trước (chỉ đọc):** hai ảnh hướng B ở trên; năm icon súng `games/typing-survival/art-src/ui/icons/gun-xung.png` (Pulse Gun), `gun-tia.png` (Heat Beam), `gun-tan.png` (Scatter Gun), `gun-ray.png` (Rail Gun), `gun-phao-sao.png` (Star Mortar); tên súng trong `games/typing-survival/src/content/guns.ts`; prompt Tripo cũ của Dragonhold `games/dragon-hold/art-src/houses/herb-hut.prompt.txt` (để xem cách viết View, Framing, Light, Build).

### Khối prompt (nguyên văn)

Mỗi prompt = **MODEL** + phần riêng + **TAIL** của loại đó + dòng nền.

**MODEL**
```text
Image-to-3D source picture of ONE object for a stylized 3D science-fiction action game; it will become a 3D model. Stylized painterly-realistic 3D game asset for Last Line, a mythic sci-fi world at the edge of a black hole, like a premium hero asset of a top commercial sci-fi action game: crisp hard-surface armour of white-gold ceramic plates over dark graphite under-suit, fine electric-cyan light lines, clean bevels, big readable shapes with a few large details instead of many small ones, a silhouette that reads from a high camera behind the hero; matte surfaces with soft sheen, no mirror shine.
```

**TAIL-HERO** (nhân vật, để rig)
```text
Pose: neutral A-pose for rigging, standing straight, feet shoulder-width apart and flat, arms held out and down at 45 degrees from the body, palms facing down, fingers slightly apart, head looking straight ahead. The cape hangs straight down behind the body to knee height and does not cover the arms or legs. Framing: the whole figure from feet to the top of the head, centred, with a small even empty margin on every side; nothing cut off. No ground, no shadow under the feet, no props, no weapons in the hands. Light: flat, even and frontal; no cast shadows, no rim light, no glow halo around the body. Build: one connected figure; nothing floats. No text, letters, numbers, emblems, signature or watermark.
```

**TAIL-GUN** (súng canh)
```text
View: three-quarter view, the gun turned about 30 degrees so its front and its right side both show, seen from slightly above, near-orthographic, no perspective distortion. A floating sentinel gun drone with no legs, no stand, no mount and no hand holding it. Framing: the whole object, centred, with a small even empty margin on every side; nothing cut off. No ground and no shadow under it. Light: flat, even and frontal; no cast shadows, no strong highlights, no glow halo. Build: one connected solid object; every part touches the main body and nothing floats apart. No text, letters, numbers, emblems, signature or watermark.
```

**Dòng nền:** vật không có xanh lá → `Flat pure #00FF00 green background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no green at all.` Ghi nền đã dùng.

### Tám ảnh, vuông, cạnh 1254 px

| Tên | Phần riêng |
|---|---|
| `lightbearer-front` | `The Lightbearer seen from the front: a lone guardian of the last causeway, slim armoured figure in white-gold ceramic armour over a dark graphite suit, a smooth helmet with a glowing electric-cyan visor slit, a long deep-navy cape with a white-gold inner lining, thin cyan light lines along the armour seams, a small glowing core on the chest.` |
| `lightbearer-back` | Như `front` nhưng `seen from directly behind`: thấy áo choàng, lưng giáp, gáy mũ. Đính kèm `lightbearer-front` đã chọn với dòng `Same character as the attached image, same pose and proportions, seen from directly behind.` |
| `lightbearer-left` | Như `front` nhưng `seen from her left side, exact profile`. Đính kèm `lightbearer-front` đã chọn với dòng như trên, đổi thành `seen from her left side, exact profile`. |
| `sentinel-pulse` | Pulse Gun: dáng theo `gun-xung.png`. `A compact floating sentinel gun with a short twin barrel and a cyan energy ring around the muzzle, white-gold shell over graphite.` |
| `sentinel-heat` | Heat Beam: dáng theo `gun-tia.png`. `A floating sentinel beam emitter with a long focusing lens barrel and a glowing orange-gold core inside a white-gold shell.` |
| `sentinel-scatter` | Scatter Gun: dáng theo `gun-tan.png`. `A floating sentinel shotgun with a wide flat muzzle of five short barrels in a fan, white-gold shell over graphite, cyan vents.` |
| `sentinel-rail` | Rail Gun: dáng theo `gun-ray.png`. `A floating sentinel railgun with two long parallel rails and cyan coils between them, a slim white-gold body.` |
| `sentinel-mortar` | Star Mortar: dáng theo `gun-phao-sao.png`. `A floating sentinel mortar with a short wide upward barrel ringed by small star-shaped vents, heavy white-gold armour over graphite.` |

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1 md5** trên `games/typing-survival/art-src/` (đệ quy).
2. **Khổ:** vuông, cạnh 1254 px (công cụ trả khác thì cắt giữa rồi đổi cỡ, ghi lệnh).
3. **Nền sạch:** 10 px mép bốn phía là màu nền, mỗi kênh lệch ≤ 12; trong vật, px có hue trong ±12° của màu nền và S > 0,5 chiếm ≤ 0,5 %.
4. **Một vật, đủ khung:** tách nền (ghi lệnh); lề bốn phía ≥ 3 %; đúng một vùng liền có diện tích > 1 % ảnh.
5. **Ba góc của Lightbearer khớp nhau:** chiều cao hộp bao lệch ≤ 3 %; đỉnh đầu, vai, hông, gối, chân ở cùng độ cao (ghi năm độ cao cho mỗi góc, lệch ≤ 3 % chiều cao); tay ở A-pose 40–50° trong ảnh trước. Ghi số.
6. **Súng khác dáng nhau:** ở 64 px, mặt nạ alpha của hai súng bất kỳ có IoU ≤ 0,80. Ghi bảng.
7. **Tờ so** `_review/156-sheet.jpg`: ba góc Lightbearer cạnh `b-lightbearer-fight.png` (cắt vùng nhân vật); năm súng cạnh năm icon súng cùng cao; một hàng cạnh ảnh tham chiếu của chủ dự án. Ghi một dòng: "đúng nhân vật của hướng B" hay chỉ chỗ lệch.
8. **KA5 mức chợ:** M và Q cho tám bản chọn, ở cỡ đầy đủ và ở 256 px.

**Xong khi:** tám ảnh có bản chọn, qua mục 2–6, mỗi ảnh tự chấm M ≥ 8 và Q ≥ 8. Việc dựng 3D và rig là của chủ dự án trên Tripo.
