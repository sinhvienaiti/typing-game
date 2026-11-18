# Phiếu 315 · Tu Tiên · Ảnh 2D: 3 mẫu dáng vệt chém cận chiến hệ Hỏa, 3 lần gọi `image_gen`, có tự chấm

Anh (06/11 ~13:00) muốn đánh thường liên hoàn: chém nhiều góc, mỗi nhát một vệt chém hợp vũ khí và hệ (`docs/work/tasks/melee-combo.md`). Hiện mỗi hệ chỉ có một vệt lệch (vung). Phiếu này vẽ **3 dáng mới cho hệ Hỏa** làm mẫu cho anh duyệt. Phiếu ảnh ngắn, prompt đã chốt.

**Model `gpt-6.1-sol`, mức `high`. Đúng 3 lần gọi `image_gen`, cộng tối đa 2 lần vẽ lại cho mẫu tự chấm dưới 8.** Báo cáo: `docs/codex-queue/315-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. **Được ghi:** chỉ thêm file mới vào `D` (`cp -n`) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Cách làm
1. Mở bằng `view_image`:
   - `D/fire-slash-arc.v1-try1.jpg`: vệt chém Hỏa anh đã duyệt; lấy chất lửa, ánh sáng, độ hoàn thiện.
   - `D/fire-crescent-sym.v1-try1.png`: độ sắc của mép.
2. Gọi `image_gen` tạo mới, khổ ngang, nền đen, kèm hai ảnh đó. Prompt là câu của dáng cộng đuôi chung, dán nguyên văn.
3. Chép `cp -n` thành `D/<tên ra>.png`, ghi `.prompt.txt`.
4. **Tự chấm** bằng `view_image`, thang 0–10, trên 4 mặt:
   - độ cuốn hút so với game thương mại;
   - đúng dáng;
   - đọc rõ khi nhỏ (khoảng 150–250 px);
   - sạch (nền đen, không chữ).

   Dưới 8 thì vẽ lại một lần (`-try2`), chọn bản điểm cao hơn.

| Tên ra | Dáng (nguyên văn) |
|---|---|
| `fire-slash-quick.v1-try1` | A single quick, thin sword slash of dense white-gold, amber and vermilion flame: a narrow, sharply tapered arc swept from one side, razor-thin blazing leading edge, a short trail of embers and sparks behind it, as if made by a fast light sword. |
| `fire-slash-heavy.v1-try1` | A single wide, heavy sabre sweep of dense white-gold, amber and vermilion flame: a broad thick crescent arc swept across with great force, a thick blazing leading edge, heavy rolling flame mass and flying embers behind it, as if made by a heavy curved sabre. |
| `fire-slash-thrust.v1-try1` | A single straight spear thrust of dense white-gold, amber and vermilion flame: a long narrow spike of fire shooting forward to a needle-sharp point, a spiralling ring of flame around the shaft near the base, sparks streaming back along it. |

**Đuôi chung (nguyên văn):**
```text
Use the attached images only as the reference for material, light, glow and finish; do not copy their shapes. Seen from a high three-quarter game camera about 55 degrees down. Premium Chinese donghua xianxia skill effect, mythic and radiant, translucent energy, fine luminous detail, glints and star twinkles, soft halos; anime-mythic, not realistic. Centred with a wide empty border, solid pure black background, no sword, no character, no text, no letters, no watermark.
```

## Xong khi
Có đủ 3 ảnh (cộng bản vẽ lại nếu có). Báo cáo có bảng: ảnh, khổ thật, điểm tự chấm, một câu nhận xét.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
