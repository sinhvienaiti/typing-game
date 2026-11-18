# Phiếu 313 · Tu Tiên · Ảnh 2D: vòng tụ lực đầy dần khi gõ cho 14 hệ, 14 lần gọi `image_gen`, có tự chấm

Anh (06/11): "codex vẽ ảnh rất tốt, nếu nó vẽ và tự chấm đạt thì cho pass luôn, ưu tiên dùng codex vẽ trước". Phần tụ lực của 5 pha cần một vòng bùa đầy dần theo từng chữ gõ, thay cho kiểu "đang tụ lực" chung chung. Phiếu ảnh ngắn, prompt đã chốt.

**Model `gpt-6.1-sol`, mức `high`. Đúng 14 lần gọi `image_gen`, cộng tối đa 4 lần vẽ lại cho ảnh tự chấm dưới 8. Không gọi thêm.** Báo cáo: `docs/codex-queue/313-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. **Được ghi:** chỉ thêm file mới vào `D` (`cp -n`) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Cách làm mỗi ảnh
1. Mở bằng `view_image` ảnh lưỡi liềm của hệ: chỉ lấy chất liệu, ánh sáng, độ hoàn thiện, không lấy dáng.
2. Gọi `image_gen` tạo mới, khổ ngang, nền đen, kèm ảnh đó. Prompt = câu Fill (thay `<MATTER>`) + đuôi chung, dán nguyên văn.
3. Chép `cp -n` thành `D/<hệ>-charge-fill.v1-try1.png`; ghi `.prompt.txt` (công cụ, ảnh tham chiếu, prompt, khổ thật).
4. **Tự chấm** bằng `view_image`, thang 0–10, trên 4 mặt: độ cuốn hút so với game thương mại, đúng đề (12 đoạn, 8 sáng, 4 tối, tâm trống), đọc rõ khi nhỏ (khoảng 150 px), sạch (nền đen, không chữ). Dưới 8 thì vẽ lại một lần thành `-try2`, chọn bản điểm cao hơn.

**Fill (nguyên văn):**
```text
A talisman charging ring that fills up as the cultivator types, seen lying on the ground at the play camera angle: a circular ring of twelve segments made of <MATTER>; the first eight segments blazing and full, the last four dark and unlit with only a faint outline, bright sparks and glints at the leading edge of the fill, fine runes engraved along the ring, the centre left empty.
```
**Đuôi chung (nguyên văn):**
```text
Use the attached image only as the reference for material, light, glow and finish; do not copy its crescent shape. Premium Chinese donghua xianxia skill effect, mythic and radiant, translucent energy, fine luminous detail, glints and star twinkles, soft halos; anime-mythic, not realistic. Seen from a high three-quarter game camera about 55 degrees down. Centred with a wide empty border, solid pure black background, no text, no letters, no watermark.
```

| Hệ | Ảnh tham chiếu | `<MATTER>` |
|---|---|---|
| metal | `D/metal-crescent-sym.v1-try1.png` | razor-sharp white-silver metal light with pale jade edges and star glints |
| fire | `D/fire-crescent-sym.v1-try1.png` | dense white-gold, amber and vermilion flame with embers and sparks |
| water | `D/water-crescent-sym.v1-try1.png` | clear deep-blue spirit water with a bright white pressure edge, thin foam and caustic light |
| thunder | `D/thunder-crescent-sym.v1-try1.png` | violet-white lightning with a blinding white core line and crackling branching arcs |
| wind | `D/wind-crescent-sym.v1-try1.png` | almost invisible compressed air outlined by bright mint-white pressure rims and helical eddies, carrying small leaves |
| ice | `D/ice-crescent-sym.v1-try1.png` | glassy faceted ice crystal with a cold-white razor edge, pale blue to cold violet, frost particles |
| earth | `D/earth-crescent-sym.v1-try1.png` | heavy compressed sandstone and granite with glowing amber mineral seams and trailing dust |
| wood | `D/wood-crescent-sym.v1-try1.png` | living celadon spiritwood with glowing lime sap-veins, small leaves and pollen sparkles |
| dark | `D/dark-crescent-sym.v1-try1.png` | black shadow smoke and ink with a thin blazing dark-crimson ember edge; no purple, no violet |
| light | `D/light-crescent-sym.v1-try1.png` | radiant holy white-gold light with warm halos, crisp rays and light feathers |
| poison | `D/poison-crescent-sym.v1-try1.png` | luminous toxic green and violet miasma with acid droplets and spores |
| blood | `D/blood-crescent-sym.v1-try1.png` | deep crimson liquid blood energy with glossy droplets and red crystal shards |
| void | `D/void-crescent-sym.v1-try1.png` | spatial void energy, cracks like broken glass with indigo-white edges, floating shards of space |
| star | `D/star-crescent-sym.v1-try1.png` | cosmic star energy, constellation lines of white-blue light and glittering star dust |

## Xong khi
Có đủ 14 ảnh. Báo cáo có bảng: ảnh, khổ thật, điểm tự chấm, một câu nhận xét. Ghi số lần gọi `image_gen` (14 đến 18).

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
