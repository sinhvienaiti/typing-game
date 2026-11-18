# Phiếu 318 · Tu Tiên · Ảnh 2D: 3 vệt chém cận chiến Ám bản nền trắng (thân khói), 3 lần gọi `image_gen`, có tự chấm

Vệt chém Ám nền đen (phiếu 317) chỉ còn viền đỏ thẫm, mất thân khói đen, nên dễ lẫn với Huyết. Như sao băng Ám (phiếu 308), cần bản **nền trắng** cùng dáng để làm lớp thân khói (trộn thường). Ảnh dáng: `D/dark-slash-quick.v1-try1.png`, `D/dark-slash-heavy.v1-try1.png`, `D/dark-slash-thrust.v1-try1.png`.

**Model `gpt-6.1-sol`, mức `high`. Đúng 3 lần gọi `image_gen`, cộng tối đa 2 lần vẽ lại cho ảnh tự chấm dưới 8.** Báo cáo: `docs/codex-queue/318-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. **Được ghi:** chỉ thêm file mới vào `D` (`cp -n`) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Cách làm mỗi ảnh
1. Mở bằng `view_image` ảnh Ám nền đen cùng dáng (lấy dáng, góc, bố cục) và `D/dark-comet-white.v1-try1.png` (chất khói đen trên nền trắng).
2. Gọi `image_gen` tạo mới, khổ ngang, **nền trắng thuần**, kèm các ảnh đó. Prompt = câu của dáng (thay `<MATTER>`) + đuôi chung, dán nguyên văn.
3. Chép `cp -n` thành `D/dark-slash-<dáng>-white.v1-try1.png`, ghi `.prompt.txt`.
4. **Tự chấm** như phiếu 315 (độ cuốn hút, đúng dáng, rõ ở 200 px, sạch). Dưới 8 thì vẽ lại một lần (`-try2`).

**quick:** `A single quick, thin sword slash of <MATTER>: a narrow, sharply tapered arc swept from one side, a razor-thin blazing leading edge, a short trail of particles and glints behind it, as if made by a fast light sword.`
**heavy:** `A single wide, heavy sabre sweep of <MATTER>: a broad thick crescent arc swept across with great force, a thick blazing leading edge, a heavy rolling mass of the same matter and flying particles behind it, as if made by a heavy curved sabre.`
**thrust:** `A single straight spear thrust of <MATTER>: a long narrow spike shooting forward to a needle-sharp point, a spiralling ring of the same matter around the shaft near the base, particles streaming back along it.`

**Đuôi chung (nguyên văn):**
```text
Use the attached images only as the reference for material, light, glow and finish; do not copy their shapes. Seen from a high three-quarter game camera about 55 degrees down. Premium Chinese donghua xianxia skill effect, mythic and radiant, translucent energy, fine luminous detail, glints and star twinkles, soft halos; anime-mythic, not realistic. Centred with a wide empty border, solid pure black background, no sword, no character, no text, no letters, no watermark.
```
Thay `<MATTER>` bằng "black shadow smoke and ink with a thin blazing dark-crimson ember edge". Trong đuôi chung đổi "solid pure black background" thành "solid pure white background", và thêm cuối prompt "Black and dark-crimson only; no purple, no violet."

## Xong khi
Đủ 3 ảnh (cộng bản vẽ lại nếu có). Báo cáo có bảng: ảnh, điểm tự chấm, một câu nhận xét; ghi số lần gọi.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
