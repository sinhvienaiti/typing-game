# Phiếu 317 · Tu Tiên · Ảnh 2D: 3 dáng vệt chém cận chiến cho 13 hệ còn lại, 39 lần gọi `image_gen`, có tự chấm

Anh duyệt 3 mẫu Hỏa của phiếu 315 (06/11: "Đạt, làm 14 hệ"). Phiếu này vẽ đúng 3 dáng đó cho 13 hệ còn lại (`docs/work/tasks/melee-combo.md`). Mẫu đạt để giữ cùng chuẩn: `D/fire-slash-quick.v1-try1.png`, `D/fire-slash-heavy.v1-try1.png`, `D/fire-slash-thrust.v1-try1.png`.

**Model `gpt-6.1-sol`, mức `high`. Đúng 39 lần gọi `image_gen`, cộng tối đa 8 lần vẽ lại cho ảnh tự chấm dưới 8.** Báo cáo: `docs/codex-queue/317-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. **Được ghi:** chỉ thêm file mới vào `D` (`cp -n`) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Cách làm mỗi ảnh
1. Mở bằng `view_image`:
   - ảnh mẫu Hỏa cùng dáng: lấy dáng và độ hoàn thiện;
   - ảnh vệt chém hoặc lưỡi liềm của hệ: chỉ lấy chất liệu.
2. Gọi `image_gen` tạo mới, khổ ngang, nền đen, kèm các ảnh đó. Prompt = câu của dáng (thay `<MATTER>`) + đuôi chung, dán nguyên văn.
3. Chép `cp -n` thành `D/<hệ>-slash-<dáng>.v1-try1.png`, ghi `.prompt.txt`.
4. **Tự chấm** như phiếu 315 (độ cuốn hút, đúng dáng, rõ ở 200 px, sạch). Dưới 8 thì vẽ lại một lần (`-try2`).

**quick:** `A single quick, thin sword slash of <MATTER>: a narrow, sharply tapered arc swept from one side, a razor-thin blazing leading edge, a short trail of particles and glints behind it, as if made by a fast light sword.`
**heavy:** `A single wide, heavy sabre sweep of <MATTER>: a broad thick crescent arc swept across with great force, a thick blazing leading edge, a heavy rolling mass of the same matter and flying particles behind it, as if made by a heavy curved sabre.`
**thrust:** `A single straight spear thrust of <MATTER>: a long narrow spike shooting forward to a needle-sharp point, a spiralling ring of the same matter around the shaft near the base, particles streaming back along it.`

**Đuôi chung (nguyên văn):**
```text
Use the attached images only as the reference for material, light, glow and finish; do not copy their shapes. Seen from a high three-quarter game camera about 55 degrees down. Premium Chinese donghua xianxia skill effect, mythic and radiant, translucent energy, fine luminous detail, glints and star twinkles, soft halos; anime-mythic, not realistic. Centred with a wide empty border, solid pure black background, no sword, no character, no text, no letters, no watermark.
```
Ám: thêm vào cuối prompt "Black and dark-crimson only; no purple, no violet."

| Hệ | Ảnh tham chiếu | `<MATTER>` |
|---|---|---|
| metal | `D/metal-slash-arc*.jpg` hoặc `.png` (bản anh đã duyệt; Ám dùng `D/dark-slash-arc-a.v1-try2.png`), `D/metal-crescent-sym.v1-try1.png` | razor-sharp white-silver metal light with pale jade edges and star glints |
| water | `D/water-slash-arc*.jpg` hoặc `.png` (bản anh đã duyệt; Ám dùng `D/dark-slash-arc-a.v1-try2.png`), `D/water-crescent-sym.v1-try1.png` | clear deep-blue spirit water with a bright white pressure edge, thin foam and caustic light |
| thunder | `D/thunder-slash-arc*.jpg` hoặc `.png` (bản anh đã duyệt; Ám dùng `D/dark-slash-arc-a.v1-try2.png`), `D/thunder-crescent-sym.v1-try1.png` | violet-white lightning with a blinding white core line and crackling branching arcs |
| wind | `D/wind-slash-arc*.jpg` hoặc `.png` (bản anh đã duyệt; Ám dùng `D/dark-slash-arc-a.v1-try2.png`), `D/wind-crescent-sym.v1-try1.png` | almost invisible compressed air outlined by bright mint-white pressure rims and helical eddies, carrying small leaves |
| ice | `D/ice-slash-arc*.jpg` hoặc `.png` (bản anh đã duyệt; Ám dùng `D/dark-slash-arc-a.v1-try2.png`), `D/ice-crescent-sym.v1-try1.png` | glassy faceted ice crystal with a cold-white razor edge, pale blue to cold violet, frost particles |
| earth | `D/earth-slash-arc*.jpg` hoặc `.png` (bản anh đã duyệt; Ám dùng `D/dark-slash-arc-a.v1-try2.png`), `D/earth-crescent-sym.v1-try1.png` | heavy compressed sandstone and granite with glowing amber mineral seams and trailing dust |
| wood | `D/wood-slash-arc*.jpg` hoặc `.png` (bản anh đã duyệt; Ám dùng `D/dark-slash-arc-a.v1-try2.png`), `D/wood-crescent-sym.v1-try1.png` | living celadon spiritwood with glowing lime sap-veins, small leaves and pollen sparkles |
| dark | `D/dark-slash-arc*.jpg` hoặc `.png` (bản anh đã duyệt; Ám dùng `D/dark-slash-arc-a.v1-try2.png`), `D/dark-crescent-sym.v1-try1.png` | black shadow smoke and ink with a thin blazing dark-crimson ember edge; no purple, no violet |
| light | `D/light-slash-arc*.jpg` hoặc `.png` (bản anh đã duyệt; Ám dùng `D/dark-slash-arc-a.v1-try2.png`), `D/light-crescent-sym.v1-try1.png` | radiant holy white-gold light with warm halos, crisp rays and light feathers |
| poison | `D/poison-slash-arc*.jpg` hoặc `.png` (bản anh đã duyệt; Ám dùng `D/dark-slash-arc-a.v1-try2.png`), `D/poison-crescent-sym.v1-try1.png` | luminous toxic green and violet miasma with acid droplets and spores |
| blood | `D/blood-slash-arc*.jpg` hoặc `.png` (bản anh đã duyệt; Ám dùng `D/dark-slash-arc-a.v1-try2.png`), `D/blood-crescent-sym.v1-try1.png` | deep crimson liquid blood energy with glossy droplets and red crystal shards |
| void | `D/void-slash-arc*.jpg` hoặc `.png` (bản anh đã duyệt; Ám dùng `D/dark-slash-arc-a.v1-try2.png`), `D/void-crescent-sym.v1-try1.png` | spatial void energy, cracks like broken glass with indigo-white edges, floating shards of space |
| star | `D/star-slash-arc*.jpg` hoặc `.png` (bản anh đã duyệt; Ám dùng `D/dark-slash-arc-a.v1-try2.png`), `D/star-crescent-sym.v1-try1.png` | cosmic star energy, constellation lines of white-blue light and glittering star dust |

## Xong khi
Đủ 39 ảnh (cộng bản vẽ lại nếu có). Báo cáo có bảng: ảnh, điểm tự chấm, một câu nhận xét; ghi số lần gọi.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
