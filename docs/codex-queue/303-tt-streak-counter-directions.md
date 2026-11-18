# Phiếu 303 · Tu Tiên · Ảnh 2D: ba hướng cho bộ đếm chuỗi từ (D60), 6 lần gọi `image_gen`

Anh duyệt bộ đếm chuỗi từ (05/11 22:20, canon D60). Gemini đề xuất ba hướng hình (`docs/work/consult/streak-channel-gemini.md`). Theo luật, giao diện chính phải cho anh xem vài hướng trước khi dựng. Gemini hết lượt ảnh, nên Codex vẽ (anh cho phép 18:20). Phiếu ảnh ngắn, prompt đã chốt.

**Model `gpt-6.1-sol`, mức `high`. Đúng 6 lần gọi `image_gen`, không gọi thêm, không tự sửa lại.**

**Báo cáo:** `docs/codex-queue/303-report.md` (tiếng Việt, ngắn).

## Đường dẫn
- `S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills` (ảnh tham chiếu).
- `C = games/immortality-cultivation/art-src/skills/cutin` (ảnh tham chiếu).
- `D = games/immortality-cultivation/art-src/lab/ui/streak-counter` (thư mục ra; tạo mới nếu chưa có).

**Được ghi:** chỉ thêm file mới vào `D` (`cp -n`) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Cách làm mỗi ảnh
1. Mở hai ảnh tham chiếu của hướng đó bằng `view_image`. Đó là ảnh anh đã duyệt; chỉ lấy ánh sáng, chất liệu, độ phát sáng, độ lấp lánh và độ hoàn thiện, không chép dáng.
2. Gọi `image_gen` tạo mới, khổ ngang 16:9, kèm hai ảnh đó. Prompt dán nguyên văn: lấy **Prompt chung**, thay `<LOOK>` bằng đoạn của hướng đó.
3. Chép kết quả bằng `cp -n` thành `D/<tên ra>.png`.
4. Ghi `D/<tên ra>.prompt.txt`: công cụ, hai ảnh tham chiếu, prompt đã gửi, khổ thật.

| Tên ra | Ảnh tham chiếu | Hướng |
|---|---|---|
| `streak-ink-edict.v1-try1`, `streak-ink-edict.v1-try2` | `C/tt-cutin-c-gather.v1-try1.png`, `S/light-crescent-sym.v1-try1.png` | 1 |
| `streak-jade-seal.v1-try1`, `streak-jade-seal.v1-try2` | `S/wood-crescent-sym.v1-try1.png`, `S/metal-crescent-sym.v1-try1.png` | 2 |
| `streak-astrolabe.v1-try1`, `streak-astrolabe.v1-try2` | `S/star-crescent-sym.v1-try1.png`, `S/astral-meteor-constellation.v1-try1.png` | 3 |

### Prompt chung (nguyên văn)

```text
Use the attached images only as the style reference for light, material, glow, sparkle and finish; do not copy their shapes. A premium game HUD element for a Chinese xianxia action game: a word-streak counter, shown as one horizontal row of FIVE states of the same counter from left to right, each a little richer than the last, displaying the numbers 7, 12, 31, 64 and 128. Each state is a compact emblem (about 4:3), with a tall elegant numeral in the centre that is instantly readable. <LOOK> Luxurious, stylish, modern Chinese donghua game UI with rich detail, crisp edges, halos and glints that never wash out the numeral. Even spacing, solid very dark charcoal background, no other text, no letters, no words, only the five numbers.
```

### `<LOOK>` của từng hướng (nguyên văn)

**Hướng 1:**
```text
Style "gilded ink edict": behind each numeral an asymmetric vertical dry-brush sumi-ink slash with paper-grain edges, a hairline mineral-gold filigree crescent on its outer edge; numerals in a high-contrast serif-calligraphic hybrid, vertical strokes like a sword blade, warm ivory with a charcoal drop shadow, turning burnished champagne gold at the fourth state. Rising tiers add a gold crescent rim, drifting gold-leaf flakes, a rotating thin ink ring, and at the last state twin floating celestial ribbons edged in pale cyan-white starlight and gold with micro-glints.
```

**Hướng 2:**
```text
Style "imperial nephrite seal": each numeral sits on a sleek lozenge-cut tablet of translucent smoked dark celadon jade split horizontally by a glowing qi fissure, with brushed antique-brass cloud-scroll brackets at the corners; chiselled faceted numerals with clean 45-degree chamfers, pale celadon at first and gold-inlaid at the fourth state. Rising tiers light the fissure with celadon mist, illuminate inner jade veins with orbiting jade-dust motes, unfold the brass brackets to reveal a gold-and-celadon lattice, and at the last state add a translucent jade halo with rotating notches and celadon-gold sparkles.
```

**Hướng 3:**
```text
Style "celestial astrolabe": each numeral floats inside an angled armillary ring of fine star-brass needles and constellation nodes over a soft deep-indigo vignette, no heavy backplate; tall slender high-fashion astronomical numerals with hairline crossbars and diamond-shaped counters, pearl-white, gaining a champagne-gold to pearl gradient at the fourth state. Rising tiers ignite star nodes on the ring, add a counter-rotating gold filigree outer ring with constellation lines, trail luminous qi silk ribbons from the ring tips, and at the last state bloom an eight-pointed compass star behind the rings with fine starlight motes falling like golden rain.
```

## Xong khi
- Có đủ 6 bộ `.png` và `.prompt.txt` trong `D`.
- Báo cáo ghi khổ thật mỗi ảnh, số lần gọi (phải là 6), và một câu mỗi ảnh: số có đọc được không, đúng 5 trạng thái không, có chữ thừa không.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
