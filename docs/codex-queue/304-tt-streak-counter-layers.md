# Phiếu 304 · Tu Tiên · Ảnh 2D: tách lớp bộ đếm chuỗi từ, hướng mực vàng (D60), 4 lần gọi `image_gen`

Anh chọn hướng bộ đếm (05/11 22:45): "Hàng 1: mực vàng", tức `streak-ink-edict` (phiếu 303). Ảnh chuẩn: `D/streak-ink-edict.v1-try1.png`; tham chiếu phụ: `D/streak-ink-edict.v1-try2.png`. Trong game, số được vẽ bằng font, nên cần các lớp **không có số**, nền trong suốt, để code đặt số, đổi mốc và cho mực tan. Phiếu ảnh ngắn, prompt đã chốt.

**Model `gpt-6.1-sol`, mức `high`. Đúng 4 lần gọi `image_gen`, không gọi thêm, không tự sửa lại.**

**Báo cáo:** `docs/codex-queue/304-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/ui/streak-counter`. **Được ghi:** chỉ thêm file mới vào `D` (`cp -n`) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Cách làm mỗi ảnh
1. Mở `D/streak-ink-edict.v1-try1.png` và `D/streak-ink-edict.v1-try2.png` bằng `view_image`. Đó là hướng anh đã chọn: giữ đúng nét mực, vàng lá, ánh sáng và độ hoàn thiện.
2. Gọi `image_gen` tạo mới, kèm hai ảnh đó, **bật nền trong suốt**. Prompt dán nguyên văn.
3. Chép kết quả bằng `cp -n` thành `D/<tên ra>.png`, giữ kênh alpha.
4. Ghi `D/<tên ra>.prompt.txt`: công cụ, hai ảnh tham chiếu, prompt đã gửi, khổ thật, có alpha hay không.
5. Nếu công cụ không cho nền trong suốt: dừng sau lần gọi đầu, ghi rõ vào báo cáo, không gọi tiếp.

| Tên ra | Prompt |
|---|---|
| `streak-plates-row.v1-try1` | Prompt A |
| `streak-plates-row.v1-try2` | Prompt A |
| `streak-flakes-sheet.v1-try1` | Prompt B |
| `streak-ribbons-t4.v1-try1` | Prompt C |

### Prompt A (nguyên văn)
```text
Use the attached images as the exact style to match: the same dry-brush sumi-ink slashes, paper-grain edges, mineral gold-leaf filigree, light, sparkle and finish. Paint the SAME five counter emblems in one horizontal row, left to right from the plainest to the richest tier, but with NO numbers at all: the centre of each emblem is left calm and clear, a soft dark ink area where a large numeral will be placed later. Tier 1: a single asymmetric vertical dry-brush ink slash. Tier 2: the slash with a hairline gold crescent on its outer edge. Tier 3: adds drifting gold-leaf flakes and a faint silver-white rim on the wet ink edges. Tier 4: adds a thin rotating ink ring and a brighter burnished gold crescent. Tier 5: the slash splits into twin floating celestial ribbons edged in pale cyan-white starlight and gold with micro-glints. Each emblem the same size and position in its fifth of the frame, evenly spaced, nothing touching. Transparent background, no text, no letters, no digits.
```

### Prompt B (nguyên văn)
```text
Use the attached images as the exact style to match: the same mineral gold leaf, ink and sparkle. A sprite sheet on a transparent background: a loose grid of separate small elements with wide empty gaps, nothing touching: twelve curled gold-leaf flakes of different sizes and angles, eight four-point star glints of gold-white light, eight small dry-ink flecks and droplets, and six thin wisps of dissolving ink smoke. No text, no letters, no digits.
```

### Prompt C (nguyên văn)
```text
Use the attached images as the exact style to match: the twin floating celestial ribbons of the richest emblem, edged in pale cyan-white starlight and gold with micro-glints. Paint ONLY the two ribbons as one isolated element: two long flowing silk-like light ribbons curving around an empty centre in an S-shaped embrace, translucent, soft glowing edges, gold filigree edge lines and tiny sparkles along them. Centred with wide empty margins. Transparent background, no ink slash, no text, no letters, no digits.
```

## Xong khi
- Có đủ 4 bộ `.png` (có alpha) và `.prompt.txt` trong `D`.
- Báo cáo ghi khổ thật, có alpha thật không (đo bằng ImageMagick: góc ảnh trong suốt), số lần gọi (phải là 4), và một câu mỗi ảnh: có số hay chữ lọt vào không, các phần có tách rời không.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
