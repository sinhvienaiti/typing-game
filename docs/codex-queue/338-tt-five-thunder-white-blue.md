# Phiếu 338 · Tu Tiên · Ảnh 2D: bộ Ngũ Lôi Oanh Đỉnh bản trắng xanh (để anh so với bản tím), có tự chấm

Anh (11/11 tối): "Vẽ bản trắng xanh". Bộ hiện tại ngả tím nhiều; anh muốn xem bộ sét **trắng nóng và xanh điện**. Phiếu này chỉ vẽ ảnh, không sửa mã.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 13 lần gọi `image_gen`** (10 ảnh × 1, cộng tối đa 3 lần vẽ lại cho ảnh tự chấm dưới 8). Mở tối đa 24 ảnh bằng `view_image`. Báo cáo: `docs/codex-queue/338-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.
**Được ghi:** chỉ thêm file mới vào `S` (`cp -n`), đúng tên ở dưới, và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo làm tham chiếu; sửa mã.

## Việc
Với **mỗi** ảnh nguồn dưới đây: mở nó bằng `view_image`, rồi vẽ lại **đúng thiết kế, bố cục, góc nhìn, khổ và lề đó**, chỉ **đổi bảng màu**. Tên ảnh mới = tên ảnh nguồn, thay phần `.v1-try…` bằng `.v2-try1.png` (ví dụ `thunder-five-strike.v2-try1.png`).

| # | Ảnh nguồn (trong `S/`) | Khổ |
|---|---|---|
| 1 | `thunder-five-strike.v1-try1.png` | 9:16 dọc |
| 2 | `thunder-five-cloud-vortex-top.v1-try1.png` | 1:1 |
| 3 | `thunder-five-caster-seal.v1-try1.png` | 1:1 |
| 4 | `thunder-five-impact-burst.v1-try1.png` | 1:1 |
| 5 | `thunder-five-shock-ring-top.v1-try2.png` | 1:1 |
| 6 | `thunder-five-lingering-arcs.v1-try1.png` | 16:9 |
| 7–10 | `thunder-single-bolt-a.v1-try1.png`, `-b`, `-c`, `-d` | 9:16 dọc |

**Bảng màu mới (bắt buộc, giống nhau cho cả 10 ảnh):**
- lõi tia: trắng nóng, rộng và rõ hơn bản tím;
- thân và viền tia: xanh điện sáng (khoảng `#4FB6FF` tới `#9FE0FF`), ánh lam băng;
- quầng ngoài và mây: xanh lam thẫm tới chàm; **tím chỉ còn là ánh rất nhẹ ở rìa ngoài cùng, dưới 10 % diện tích sáng**;
- không cam, không vàng, không hồng, không tàn lửa.

Riêng ảnh 3 (ấn tay): năm ký hiệu hiện trông hơi giống biểu tượng tia chớp; vẽ chúng **thành nét sét thật, gãy khúc, mảnh và sắc hơn**, bớt chất biểu tượng, vẫn giữ vòng ấn và năm vị trí.

## Cách làm mỗi ảnh
1. `view_image` ảnh nguồn.
2. `image_gen`: tả lại đúng hình của ảnh nguồn bằng tiếng Anh, rồi thêm:
   `Same design, composition, camera angle and margins as the reference image; change only the palette. Palette: broad white-hot cores, bright electric blue and ice-blue bodies and edges, deep blue to indigo outer glow and clouds, at most a faint trace of violet at the outermost rim. No purple-dominant areas, no magenta, no orange, no gold, no embers. Uniform pure black background, wide black margins, no characters, no text, no watermark. Premium Chinese donghua xianxia game VFX source layer, thick jagged lightning, rich layered detail, glints, fine motes and soft halos.`
   Ảnh nhìn từ trên (2, 5) thêm: `Seen straight from above, orthographic top-down, a perfect circle.` Ảnh tia (1, 7–10) thêm: `No cylinder, no tube, no smooth pillar.`
3. Chép `cp -n` vào `S/` đúng tên. Ghi `.prompt.txt` cùng tên: công cụ, ảnh tham chiếu (đường dẫn), prompt nguyên văn, khổ thật.
4. Kiểm bằng `magick`: nền 4 góc gần đen thuần; lề trống ≥ 6 % (với tia dọc: lề trái phải). Thiếu thì đệm bằng `magick -extent` vào file mới `-pad.png`. **Đo màu:** trong các điểm sáng (độ sáng > 35 %), tỉ lệ điểm có sắc độ 255–330° (tím, hồng tím) phải **≤ 15 %**; ghi con số. Quá 15 % thì tính là chưa đạt và vẽ lại.
5. **Tự chấm** 0–10 theo mặt yếu nhất: đúng bảng màu trắng xanh; giữ thiết kế của ảnh nguồn; cuốn hút, sang, có lực; nền đen, không chữ; dùng làm khung đầu video được. Dưới 8: vẽ lại một lần (`.v2-try2.png`).

## Xong khi
- Đủ 10 ảnh cùng `.prompt.txt`.
- Tấm ghép `S/thunder-five-338-compare.jpg`: 10 cặp, mỗi cặp bản tím (trái) cạnh bản trắng xanh (phải), có tên.
- Báo cáo có bảng: ảnh, tỉ lệ tím đo được, điểm từng tiêu chí, lề, nhận xét, có vẽ lại không.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
