# Phiếu 308 · Tu Tiên · Ảnh 2D: sao băng Ám nền trắng (thân khói), 1 lần gọi `image_gen`

Sao băng Ám nền đen (`D/dark-comet.v1-try1.png`, Codex 307) mất thân khói đen, chỉ còn viền đỏ thẫm, nên dễ lẫn với Huyết. Như bộ Ám A, cần thêm một bản **nền trắng** cùng dáng để làm lớp thân khói (trộn thường). Phiếu ảnh ngắn, prompt đã chốt.

**Model `gpt-6.1-sol`, mức `high`. Đúng 1 lần gọi `image_gen`, không gọi thêm, không tự sửa lại.** Báo cáo: `docs/codex-queue/308-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. **Được ghi:** chỉ thêm file mới vào `D` (`cp -n`) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Cách làm mỗi ảnh
1. Mở hai ảnh tham chiếu bằng `view_image`: ảnh đầu lấy dáng, góc và bố cục sao băng; ảnh sau chỉ lấy chất khói đen và viền than đỏ thẫm.
2. Gọi `image_gen` tạo mới, khổ ngang, kèm hai ảnh đó, **nền trắng** (không bật nền trong suốt). Prompt dán nguyên văn.
3. Chép bằng `cp -n` thành `D/<tên ra>.png`.
4. Ghi `D/<tên ra>.prompt.txt`: công cụ, ảnh tham chiếu, prompt đã gửi, khổ thật.

```text
Use the attached images: the first for the meteor's exact shape, angle and composition; the second only for the black-smoke and dark-crimson ember material. Repaint the same meteor of black shadow smoke and ink with a thin blazing dark-crimson ember edge, falling diagonally from the upper left toward the lower right: a dense rounded head of churning black smoke with a dark-crimson glowing rim, followed by a long tapering tail of black smoke and ink wisps that thins and breaks into dark-crimson embers. Seen from a high three-quarter game camera about 55 degrees down. Premium Chinese donghua xianxia skill effect, mythic, anime-mythic, not realistic. The whole meteor inside the frame with a wide empty border, solid pure white background, no ground, no crescent, no sword, no text. No purple, no violet.
```

| Tên ra | Ảnh tham chiếu |
|---|---|
| `dark-comet-white.v1-try1` | `D/dark-comet.v1-try1.png` (dáng), `D/dark-slash-arc-a.v1-try2.png` (chất khói đen nền trắng của bộ Ám A, nếu không có thì dùng `D/dark-crescent-sym.v1-try1.png`) |

## Xong khi
Có đủ 1 bộ `.png` và `.prompt.txt`. Báo cáo ghi khổ thật, số lần gọi (phải là 1), và một câu mỗi ảnh: đầu sao băng có rõ không, đuôi có thon dần không, có dáng lưỡi liềm hay chữ lọt vào không.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
