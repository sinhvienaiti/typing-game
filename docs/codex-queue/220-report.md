# Phiếu 220 · Last Line · Luật bến đầy §5.1

**Chưa ứng viên nào bot đạt đủ các cổng trên cả hai bộ seed.** F4 (`FULL_BAY.boost=0.3`) đứng đầu ở c1-s1 theo luật chọn của phiếu, nhưng còn 4 điều kiện trượt cộng hai bộ. Khuyến nghị giữ mặc định tắt; dùng F4 làm ứng viên để Claude xem tiếp, chưa áp V6 hay luật mới vào game. Ở bốn ải, F4 làm B6 Cân bằng ải 2 giảm từ +10/+10 xuống +8/+8 điểm; ải 4 bộ sau còn đảo Thử thách −8 điểm (Nhanh − Mới). Vì vậy chưa khuyến nghị áp luật nào.

Mốc `ba6d70e9d6978eb4b430d119c409f3d47f9a364e`, nhánh `ts-codex`. [Quyết định trước khi chạy bốn ải](220/decision.md), [phương pháp](220/method.md), [bảng đầy đủ](220/summary.md), [JSON](220/summary.json), [kiểm chứng](220/verification.json), [đầu ra nguyên](220/runs/). Mọi kết luận là số bot; B9: **THIẾU SỐ: cần người thật chơi**.

## Ba luật và phạm vi mã

- `FULL_BAY = { extra: 0, spill: 0, boost: 0 }`: chỉ ải chương. S0 giữ nguyên luật đầy bến. R1 thêm sức chứa đã lấy sàn, chặn 0–MAG_CAP; R2 tràn sang bến ít băng nhất, hòa chọn chỉ số nhỏ; R3 nhân sát thương băng cuối đúng một lần. Ghép luật: R2 trước R3. Bến không súng không được tính đầy.
- Luật và giá trị bến dùng chung helper trong `src/sim/weapons.ts`; đọc núm lúc gọi. `loadMagazine` vẫn trả false khi đầy. `words.ts` chỉ sửa trong `finish`; gọi helper qua thuộc tính hàm `loadMagazine.fullBayWord` để giữ nguyên import theo phạm vi phiếu. R2 phát `EV.load` ngay sau `EV.word` với bến nhận; R3 không phát sự kiện mới.
- Dấu R3 ở `guns.fullBay.boosted`, nằm **ngoài hashWorld**. Nạp đặt lại dấu, hết băng dời dấu cùng các thông số. Nếu chọn R3, cần phiếu sau đưa dấu vào mã băm và cập nhật 152 mã băm có chủ đích.
- Các file sim/bot thay đổi: `src/content/guns.ts`, `src/sim/weapons.ts`, `src/sim/words.ts`, `src/sim/pace.ts`, đúng một dòng `src/sim/world.ts`, `tests/survival/typist-bot.ts`; thêm `tests/full-bay.test.ts` và `docs/changelog/2026-10-30-full-bay-knobs.md`. Tất cả trong `games/.wt-ts-codex`.

## Test và bất biến

| Kiểm | Số đo |
|---|---|
| Test mới trước mã | 21 đỏ / 0 xanh; exit 1; FULL_BAY chưa có (`tests-red.txt`) |
| Test mới sau mã | 21 xanh / 0 đỏ; exit 0 (`tests-green.txt`) |
| Đột biến R2 | 6 đỏ / 15 xanh; exit 1 |
| Đột biến R3 | 4 đỏ / 17 xanh; exit 1 |
| Đột biến R1 | 5 đỏ / 16 xanh; exit 1 |
| Trả mã sau ba đột biến | 21 xanh / 0 đỏ; exit 0 |
| pnpm check trước | 296 test / 26 file, kit 61/61; exit 0 |
| pnpm check sau | 317 test / 27 file, kit 61/61; TypeScript và build xanh; exit 0 |
| Golden S0 trước/sau | `42e4e5a9534bc78a0c252353ea7ee4670a1bec9e43eb42ef38c886aade530eea` / cùng SHA |
| Mã băm chương trước/sau | 152 / 152 dòng, diff exit 0 |

Log nằm trong [220/logs](220/logs/). Lượt `check-after-initial.txt` có 317 test xanh nhưng tsc đỏ vì kiểu `readonly number[]` không nhận Float64Array; đã đổi sang `ArrayLike<number>`, chạy lại check xanh. Không có test thời gian đỏ nên không cần chạy lại riêng. Kiểm mã băm cuối thực hiện trên mã đã trả lại sau đột biến.

## Tái tạo V6 và kiểm lại khi núm tắt

Trước sửa: **0/72 ô lệch, 0 trường summary lệch**, hai SHA-256 JSON trùng 209. Sau sửa, phần c1-s1 của x-v0 / x-v6 / x-f4 khớp mốc tương ứng, **0/216 ô lệch, 0 trường lệch**. [V6](220/evidence/v6-repro.json), [bốn ải](220/evidence/four-stage-repro.json). So mọi trường summary, gồm killSeconds, stepsPerWave, spawnMin/Max, learnOk; không chỉ số thắng.

## Tổng biến thể · c1-s1

| Bản · seed | B1 ô (chỉ số) | I Khá / Nhanh CB | B3 Mới / Trẻ | B6 CB / TT | B7 sát mép | G3c kém / tốt | TT Nhanh − Mới | Chặn |
|---|---|---|---|---|---|---|---|---|
| V6 · 1–100 | 4 (7) | 14,9 / 10,9 | 86 / 91 | +12 / +35 | TRƯỢT | 73 / 98 | +3 | B1, B7, G3c |
| V6 · 101–200 | 3 (3) | 15,1 / 11,2 | 85 / 89 | +11 / +32 | TRƯỢT | 62 / 90 | +3 | B1, B7 |
| F1 · 1–100 | 6 (11) | 12,7 / 9,2 | 89 / 91 | +7 / +23 | TRƯỢT | 76 / 100 | +13 | B1, B6, B7, G3c |
| F1 · 101–200 | 6 (9) | 12,6 / 9,2 | 85 / 90 | +14 / +38 | TRƯỢT | 71 / 97 | +10 | B1, B7 |
| F2 · 1–100 | 6 (11) | 17,8 / 13,6 | 88 / 89 | +6 / +23 | TRƯỢT | 72 / 97 | -4 | B1, B6, B7 |
| F2 · 101–200 | 6 (8) | 17,7 / 14 | 87 / 90 | +10 / +28 | TRƯỢT | 62 / 95 | -6 | B1, B7, G3c, Thứ bậc Thử thách |
| F3 · 1–100 | 3 (4) | 1,1 / 0,6 | 84 / 86 | +13 / +32 | TRƯỢT | 71 / 98 | +12 | B1, B7, G3c |
| F3 · 101–200 | 1 (1) | 1,2 / 0,6 | 86 / 88 | +14 / +23 | TRƯỢT | 68 / 92 | +0 | B1, B7 |
| F4 · 1–100 | 3 (4) | 1,2 / 0,7 | 85 / 88 | +11 / +34 | TRƯỢT | 67 / 96 | +7 | B1, B7 |
| F4 · 101–200 | 1 (1) | 1,3 / 0,7 | 81 / 89 | +14 / +23 | TRƯỢT | 68 / 91 | +2 | B1, B7 |

G3m, B2–B5, B8, G5, G8 và §7.6 có đủ số/pass trong bảng chi tiết; không bỏ cổng trượt khi xếp hạng. **G3m chỉ thấy R1** qua sức chứa 3 trong cảnh một súng nạp thẳng; R2/R3 không chạy ở đó, nên không lấy G3m làm bằng chứng cho hai luật này.

I đếm `live <= 0 && !busy`: R2 không thay việc mọi bến đầy là hết chữ hữu ích, chỉ đổi I gián tiếp qua chọn bến và trận đấu. R3 cho bến đầy chưa tăng được tính live, nên một phần I giảm là do còn một lần gõ hữu ích theo định nghĩa mới.

## Δ so với V6 (cùng seed)

Thứ tự trong mỗi ô: **1–100 / 101–200**; đơn vị điểm phần trăm.

| Bản | Chế độ | Bot | Δ thắng | Δ S | Δ P | Δ I | Δ O |
|---|---|---|---|---|---|---|---|
| F1 | Cân bằng | Mới | +3 / +0 | +12 / +15 | -2,9 / -3,5 | -2,1 / -2,3 | +0 / +0 |
| F1 | Cân bằng | Chậm chắc | -2 / +3 | +9 / +16 | -2,7 / -3,1 | -2,3 / -2,2 | +0 / +0 |
| F1 | Cân bằng | Chuẩn | +3 / +13 | +14 / +11,5 | -3,8 / -3,2 | -2,4 / -2,8 | +0 / +0 |
| F1 | Cân bằng | Khá | +1 / +5 | +8 / +8 | -3,2 / -2,2 | -2,2 / -2,5 | +0 / +0 |
| F1 | Cân bằng | Ẩu | +9 / +6 | +8 / +23,5 | -3,6 / -4,4 | -2,9 / -2,7 | -0,1 / +0,3 |
| F1 | Cân bằng | Nhanh | +0 / +3 | +8,5 / +13 | -3,1 / -3,1 | -1,7 / -2 | +0 / +0,1 |
| F1 | Thử thách | Mới | +8 / +8 | +8,5 / +26 | -2,5 / -6,2 | -1,8 / -2 | +0 / +0 |
| F1 | Thử thách | Chậm chắc | +5 / +6 | +17,5 / +14 | -3,5 / -4,4 | -1,8 / -1,8 | +0 / +0 |
| F1 | Thử thách | Chuẩn | +7 / +13 | +22 / +22,5 | -5 / -5,3 | -2 / -2,4 | +0 / +0 |
| F1 | Thử thách | Khá | +8 / +3 | +15 / +14 | -3,3 / -3,3 | -2,5 / -1,9 | +0 / -0,1 |
| F1 | Thử thách | Ẩu | +16 / +20 | +20,5 / +32,5 | -3,4 / -3,2 | -2,7 / -2,8 | -0,2 / +0,1 |
| F1 | Thử thách | Nhanh | +18 / +15 | +19,5 / +22 | -3,1 / -3,6 | -1,8 / -2,1 | +0 / +0 |
| F2 | Cân bằng | Mới | +2 / +2 | +12,5 / +10,5 | -2,4 / -3,5 | +2,6 / +2,5 | +0 / +0 |
| F2 | Cân bằng | Chậm chắc | +2 / +2 | +11 / +11 | -3 / -2,9 | +3,3 / +3,4 | +0 / +0 |
| F2 | Cân bằng | Chuẩn | -2 / +3 | +10 / +9 | -2,6 / -2 | +4,1 / +4 | +0 / +0 |
| F2 | Cân bằng | Khá | +1 / +0 | +4,5 / -2 | -1,5 / +0 | +2,9 / +2,6 | +0 / +0 |
| F2 | Cân bằng | Ẩu | +1 / -1 | +1 / +9,5 | -1,4 / -2,3 | +3,8 / +3,9 | +0 / +0,1 |
| F2 | Cân bằng | Nhanh | -2 / +0 | -0,5 / -3 | -0,4 / -0,3 | +2,7 / +2,8 | +0 / +0 |
| F2 | Thử thách | Mới | +7 / +11 | +4,5 / +19 | -3,2 / -4,3 | +2,2 / +2,2 | +0 / +0 |
| F2 | Thử thách | Chậm chắc | +4 / +0 | +13,5 / +16 | -3,7 / -3,8 | +2,8 / +2,8 | +0 / +0 |
| F2 | Thử thách | Chuẩn | +2 / +6 | +10 / +8,5 | -3,7 / -2,6 | +4 / +3,3 | +0 / +0 |
| F2 | Thử thách | Khá | -3 / +2 | -1,5 / +9,5 | -0,3 / -0,7 | +2,3 / +2,7 | +0 / +0 |
| F2 | Thử thách | Ẩu | +12 / +10 | +13 / +20 | -1,9 / -1,6 | +3,5 / +3,3 | -0,2 / +0 |
| F2 | Thử thách | Nhanh | +0 / +2 | +5,5 / +2 | -0,2 / -0,2 | +2 / +2,3 | +0 / +0 |
| F3 | Cân bằng | Mới | -2 / +1 | -2,5 / -2 | +0,3 / +0,5 | -2,8 / -3,2 | +0 / +0 |
| F3 | Cân bằng | Chậm chắc | +1 / -3 | -2 / +8 | -0,1 / -0,9 | -3,3 / -3,5 | +0 / +0 |
| F3 | Cân bằng | Chuẩn | +0 / +3 | -3,5 / +2,5 | -0,5 / -1,3 | -5,9 / -6,5 | +0 / +0 |
| F3 | Cân bằng | Khá | -1 / -2 | +2 / -3,5 | -0,8 / +0,8 | -13,8 / -13,9 | +0 / +0,1 |
| F3 | Cân bằng | Ẩu | +0 / -2 | -4,5 / +2,5 | +0,2 / -0,8 | -6,9 / -7 | +0,1 / +0 |
| F3 | Cân bằng | Nhanh | -4 / +3 | -5 / -3 | +1,1 / +1,7 | -10,3 / -10,6 | +0 / +0 |
| F3 | Thử thách | Mới | -4 / +1 | -1 / +8 | +3,1 / -0,7 | -2,3 / -2,7 | +0 / +0 |
| F3 | Thử thách | Chậm chắc | -2 / +0 | -2 / +3 | -0,4 / -0,7 | -2,3 / -2,8 | +0 / +0 |
| F3 | Thử thách | Chuẩn | -4 / +5 | +7 / +3 | -0,3 / -0,2 | -4,6 / -5,2 | +0 / +0 |
| F3 | Thử thách | Khá | +0 / -3 | -3,5 / +2 | +1,6 / +1,4 | -12 / -11,7 | +0 / +0 |
| F3 | Thử thách | Ẩu | +12 / +3 | +8,5 / +4 | +1 / +1,2 | -5,7 / -6,1 | -0,1 / +0 |
| F3 | Thử thách | Nhanh | +5 / -2 | +7,5 / +2,5 | +1,6 / +1,7 | -8,8 / -9,1 | +0 / +0 |
| F4 | Cân bằng | Mới | -1 / -4 | -4 / -1,5 | +0,5 / +0,4 | -2,8 / -3,2 | +0 / +0 |
| F4 | Cân bằng | Chậm chắc | +0 / -3 | -0,5 / +4 | -0,3 / -0,6 | -3,3 / -3,5 | +0 / +0 |
| F4 | Cân bằng | Chuẩn | -3 / +6 | -5 / -0,5 | -0,2 / -0,7 | -5,9 / -6,5 | +0 / +0 |
| F4 | Cân bằng | Khá | +2 / +3 | +0 / +0 | +0 / +0,7 | -13,7 / -13,8 | +0 / +0 |
| F4 | Cân bằng | Ẩu | -5 / +2 | -8 / +7 | +0,4 / -0,6 | -6,9 / -6,9 | +0,3 / +0 |
| F4 | Cân bằng | Nhanh | -3 / +2 | -5,5 / -7,5 | +1,4 / +2 | -10,2 / -10,5 | +0 / +0 |
| F4 | Thử thách | Mới | -1 / +2 | -1,5 / +6,5 | +1,9 / -0,9 | -2,3 / -2,7 | +0 / +0 |
| F4 | Thử thách | Chậm chắc | -1 / -1 | +10 / +2 | -0,5 / -0,2 | -2,3 / -2,8 | +0 / +0 |
| F4 | Thử thách | Chuẩn | -2 / +7 | +7,5 / +3,5 | -1 / +0,2 | -4,6 / -5,2 | +0 / +0 |
| F4 | Thử thách | Khá | +5 / -7 | -5 / +3,5 | +1,6 / +1,2 | -11,9 / -11,7 | +0 / -0,1 |
| F4 | Thử thách | Ẩu | +10 / +9 | +14 / +21 | +0,6 / +1,2 | -5,8 / -6,1 | -0,2 / +0,1 |
| F4 | Thử thách | Nhanh | +3 / +1 | +2 / +4 | +2,4 / +2 | -8,8 / -9,1 | +0 / +0 |

## Bốn ải · V0 / V6 / ứng viên

Mỗi ải chạy độc lập, đủ hai bộ seed. Bảng dưới có cả ải 1 để đối chiếu. B6 trong bảng là hiệu từng ải; cổng B6 chung đọc số gộp bốn ải ở bảng kế tiếp. Các dấu B6 xấu hơn chỉ ra suy giảm cục bộ, không gọi số gộp là trượt.

| Ải · seed | Bản | B1 ô (chỉ số) | I Khá / Nhanh | B3 Mới / Trẻ | B6 CB / TT | B7 | G3c kém / tốt | TT Nhanh − Mới |
|---|---|---|---|---|---|---|---|---|
| c1-s1 · 1–100 | x-v0 | 4 (10) | 14,8 / 10,9 | 86 / 90 | +6 / +40 | TRƯỢT | 72 / 95 | -23 |
| c1-s1 · 1–100 | x-v6 | 4 (7) | 14,9 / 10,9 | 86 / 91 | +12 / +35 | TRƯỢT | 73 / 98 | +3 |
| c1-s1 · 1–100 | x-f4 | 3 (4) | 1,2 / 0,7 | 85 / 88 | +11 / +34 | TRƯỢT | 67 / 96 | +7 |
| c1-s1 · 101–200 | x-v0 | 4 (6) | 15 / 11,2 | 87 / 91 | +9 / +25 | TRƯỢT | 65 / 94 | -7 |
| c1-s1 · 101–200 | x-v6 | 3 (3) | 15,1 / 11,2 | 85 / 89 | +11 / +32 | TRƯỢT | 62 / 90 | +3 |
| c1-s1 · 101–200 | x-f4 | 1 (1) | 1,3 / 0,7 | 81 / 89 | +14 / +23 | TRƯỢT | 68 / 91 | +2 |
| c1-s2 · 1–100 | x-v0 | 6 (17) | 12 / 8,2 | 93 / 90 | +10 / +29 | TRƯỢT | 77 / 99 | +9 |
| c1-s2 · 1–100 | x-v6 | 6 (17) | 12 / 8,2 | 93 / 90 | +10 / +18 | TRƯỢT | 77 / 99 | +4 |
| c1-s2 · 1–100 | x-f4 | 6 (16) | 0,2 / 0 | 92 / 89 | +8 / +15 | TRƯỢT | 84 / 100 | +6 |
| c1-s2 · 101–200 | x-v0 | 6 (15) | 12,2 / 8 | 88 / 93 | +10 / +19 | TRƯỢT | 78 / 100 | +2 |
| c1-s2 · 101–200 | x-v6 | 6 (15) | 12,2 / 8 | 88 / 93 | +10 / +1 | TRƯỢT | 78 / 100 | -1 |
| c1-s2 · 101–200 | x-f4 | 6 (13) | 0,2 / 0 | 90 / 88 | +8 / +9 | TRƯỢT | 77 / 100 | -2 |
| c1-s3 · 1–100 | x-v0 | 6 (10) | 9,4 / 6 | 88 / 90 | +9 / +47 | TRƯỢT | 68 / 94 | +8 |
| c1-s3 · 1–100 | x-v6 | 6 (10) | 9,4 / 6 | 88 / 90 | +9 / +29 | TRƯỢT | 68 / 94 | +4 |
| c1-s3 · 1–100 | x-f4 | 6 (11) | 0,1 / 0 | 87 / 88 | +6 / +31 | TRƯỢT | 71 / 97 | +6 |
| c1-s3 · 101–200 | x-v0 | 6 (11) | 9,5 / 6,2 | 87 / 88 | +5 / +34 | TRƯỢT | 66 / 94 | +5 |
| c1-s3 · 101–200 | x-v6 | 6 (11) | 9,5 / 6,2 | 87 / 88 | +5 / +16 | TRƯỢT | 66 / 94 | -7 |
| c1-s3 · 101–200 | x-f4 | 5 (10) | 0,1 / 0 | 84 / 87 | +1 / +15 | TRƯỢT | 73 / 94 | -5 |
| c1-s4 · 1–100 | x-v0 | 4 (6) | 16,1 / 12,4 | 89 / 94 | +19 / +34 | TRƯỢT | 72 / 100 | -12 |
| c1-s4 · 1–100 | x-v6 | 4 (6) | 16,1 / 12,4 | 89 / 94 | +19 / +22 | TRƯỢT | 72 / 100 | -9 |
| c1-s4 · 1–100 | x-f4 | 3 (4) | 1,2 / 0,6 | 90 / 93 | +19 / +29 | TRƯỢT | 78 / 98 | -2 |
| c1-s4 · 101–200 | x-v0 | 5 (8) | 16,5 / 11,9 | 92 / 96 | +21 / +37 | TRƯỢT | 72 / 98 | -34 |
| c1-s4 · 101–200 | x-v6 | 5 (8) | 16,5 / 11,9 | 92 / 96 | +21 / +29 | TRƯỢT | 72 / 98 | -22 |
| c1-s4 · 101–200 | x-f4 | 3 (4) | 1,2 / 0,5 | 90 / 96 | +23 / +37 | TRƯỢT | 73 / 98 | -8 |

### B6 gộp bốn ải

| Bản · seed | CB | TT |
|---|---|---|
| x-v0 · 1 | +11 | +37,5 |
| x-v0 · 101 | +11,25 | +28,75 |
| x-v6 · 1 | +12,5 | +26 |
| x-v6 · 101 | +11,75 | +19,5 |
| x-f4 · 1 | +11 | +27,25 |
| x-f4 · 101 | +11,5 | +21 |

### Cổng và số làm xấu hơn ở ải 2–4

So ứng viên với từng nền cùng seed. “Mất cổng” chỉ việc từ đạt sang trượt; “số xấu hơn” ghi thêm dù cổng vốn đã đỏ. B1 dùng số ô/chỉ số lệch; B3 dùng biên tối thiểu; B6 dùng cả hai chế độ; G3c dùng khoảng cách tới ba ngưỡng.

| Ải · seed | So với | Mất cổng | Số xấu hơn |
|---|---|---|---|
| c1-s2 · 1 | x-v0 | B6 | B3, B6, G3c, TT Nhanh − Mới |
| c1-s2 · 1 | x-v6 | B6 | B3, B6, G3c |
| c1-s2 · 101 | x-v0 | B6 | B3, B6, B7 tắt nhịp, TT Nhanh − Mới |
| c1-s2 · 101 | x-v6 | không | B3, B6, B7 tắt nhịp, TT Nhanh − Mới |
| c1-s3 · 1 | x-v0 | không | B1, B3, B6, B7 tắt nhịp, TT Nhanh − Mới |
| c1-s3 · 1 | x-v6 | không | B1, B3, B6, B7 tắt nhịp |
| c1-s3 · 101 | x-v0 | không | B3, B6, B7 tắt nhịp, TT Nhanh − Mới |
| c1-s3 · 101 | x-v6 | không | B3, B6, B7 tắt nhịp |
| c1-s4 · 1 | x-v0 | không | B3, B6 |
| c1-s4 · 1 | x-v6 | không | B3 |
| c1-s4 · 101 | x-v0 | không | B7 tắt nhịp |
| c1-s4 · 101 | x-v6 | không | B7 tắt nhịp |

## View cần gì nếu chọn luật này

- **R1:** `hud.ts:173` vẽ 3 ô và `:333` (`is-full`) tự theo cap; cần kiểm bố cục thẻ bến với 3 ô.
- **R2:** `typing-feel.ts:140` chỉ nhận nạp khi EV.load cùng bến, nên từ tràn hiện FULL và tiếng full. Cần hiệu ứng nối bến đầy tới bến nhận và nhãn tiếng Anh mới. `shots.ts:137` lấy bến từ R.slot nên đã đúng bến nhận.
- **R3:** chưa có sự kiện nên người chơi chưa thấy gì. Cần sự kiện hay cờ, nhãn tiếng Anh trên dải chữ và một tiếng; qua phiếu ảnh/âm thật, không vẽ thay bằng mã.

Không sửa view, HUD, app, audio; giữ nhãn FULL. Không mở dev server hay trình duyệt theo lệnh cấm của phiếu.

## Kiểm đầu ra, tải và dọn

| Mục | Số thật |
|---|---|
| Báo cáo | 10 một ải = 2 + 2 × 4; 6 bốn ải; 16 JSON/MD/ERR |
| Ma trận | Mỗi JSON một ải 36 ô, bốn ải 144 ô; mọi ô runs=100; G3c 10 cặp mỗi ải |
| Bản chép raw | 48/48 file khớp SHA-256 giữa tmp và 220/runs |
| Exit / overrides | Mọi lệnh đo exit 0; từng đường old→new đúng variants.json; x-v0 không --set |
| Đồng thời | Peak 4, đúng trần theo tải từng đợt |
| Giờ máy | 7466 s = 2.0739 giờ; cộng wall tiến trình 7468.225 s |
| Thời gian vòng đo | 2770.307 s, từ đầu tái tạo V6 đến cuối bốn ải, gồm quãng kiểm/chọn |
| Toàn phiếu đến kiểm cuối | 2995.602 s; bắt đầu 2026-10-30T06:25:55.892443+00:00 |
| nice | 16/16 báo cáo có cảnh báo setpriority; vẫn exit 0; không khẳng định đã đổi ưu tiên |
| TMPDIR | `/Users/toandx/htdocs/typing-game/games/.wt-ts-codex/tmp/codex-220/tmpdir` |
| Git worktree | Chỉ đường dẫn được phép; protected diff exit 0; content chỉ guns.ts; world.ts numstat 1/1; diff --check exit 0; HEAD vẫn ba6d70e |
| Dọn | Đã xóa đúng tmpdir do phiếu tạo; giữ tmp/codex-220/runs và bản chapter trước/sau |

| Đợt (UTC) | Bắt đầu → kết thúc | Uptime đầu đợt | Peak |
|---|---|---|---|
| A | 2026-10-30T06:33:19.698Z → 2026-10-30T06:36:47.004Z | 13:33  2 users, load averages: 4.65 4.72 4.36 | 4 |
| B | 2026-10-30T06:37:32.505Z → 2026-10-30T06:41:10.156Z | 13:37  2 users, load averages: 5.21 5.44 4.80 | 4 |
| C | 2026-10-30T06:43:05.475Z → 2026-10-30T07:12:37.034Z | 13:43  2 users, load averages: 2.94 5.33 5.10 | 4 |
| repro | 2026-10-30T06:26:26.727Z → 2026-10-30T06:29:40.180Z | 13:26  2 users, load averages: 5.27 4.03 4.03 | 2 |

**Giới hạn điều phối giữa đợt:** C mở lúc tải 2,94, trần đầu đợt 4. Lúc 13:49 tải tăng 15,29 khi bốn báo cáo đã chạy. Sandbox từ chối SIGSTOP (`Operation not permitted`); không giảm được xuống 2. Giữ nguyên sáu báo cáo, không mở lại seed hay đổi cấu hình. Vì vậy chỉ xác nhận trần theo tải đầu đợt; không tuyên bố đáp ứng trần 2 tại mọi thời điểm tải tăng. Bằng chứng: `220/evidence/load-rise.json`, `220/logs/load-guard.txt`. Claude cần xem ngoại lệ tài nguyên này khi duyệt Kiểm 8.

Trạng thái repo cha trước/sau ở `220/evidence/parent-status-*.txt`; diff chi tiết ở `parent-status-changes.json`. Phiếu chỉ ghi `220-report.md` và `220/` ở repo cha. Thay đổi ngoài phiếu của các làn khác (chỉ liệt kê, không đụng):

```json
{
  "added": [
    "?? docs/codex-queue/199/build-second.json",
    "?? docs/codex-queue/199/decoded-dimensions.json",
    "?? docs/codex-queue/199/manifest-final.json",
    "?? docs/codex-queue/199/media-push.json",
    "?? docs/codex-queue/199/preflight-1328.json",
    "?? docs/codex-queue/199/prune-1328-apply.json",
    "?? docs/codex-queue/199/prune-1328-dry.json",
    "?? docs/codex-queue/199/test-first-1328.md",
    "?? docs/codex-queue/202/manifest-contract.json",
    "?? docs/codex-queue/221-report.md",
    "?? docs/codex-queue/221/check-selftest.json",
    "?? docs/codex-queue/221/check-selftest.txt",
    "?? docs/codex-queue/221/check.json",
    "?? docs/codex-queue/221/check.mjs",
    "?? docs/codex-queue/221/check.txt",
    "?? docs/codex-queue/221/fired-ids.json",
    "?? docs/codex-queue/221/game-after.txt",
    "?? docs/codex-queue/221/make-data.mjs",
    "?? docs/codex-queue/221/make-report.py",
    "?? docs/codex-queue/221/source-checks.txt",
    "?? docs/codex-queue/221/source-evidence.json",
    "?? docs/codex-queue/221/state-check.json",
    "?? docs/codex-queue/221/status-after.txt",
    "?? docs/codex-queue/224/audit.py",
    "?? docs/codex-queue/224/before.json",
    "?? docs/codex-queue/224/build-only.json",
    "?? docs/codex-queue/224/check-170-run.json",
    "?? docs/codex-queue/224/check-run.json",
    "?? docs/codex-queue/224/copy.json",
    "?? docs/codex-queue/224/deploy-170-run.json",
    "?? docs/codex-queue/224/deploy-absent-run.json",
    "?? docs/codex-queue/224/deploy-empty-run.json",
    "?? docs/codex-queue/224/deploy-local-run.json",
    "?? docs/codex-queue/224/dist-170-comparison.json",
    "?? docs/codex-queue/224/dist-170.json",
    "?? docs/codex-queue/224/dist-absent.json",
    "?? docs/codex-queue/224/dist-empty-comparison.json",
    "?? docs/codex-queue/224/dist-empty.json",
    "?? docs/codex-queue/224/dist-local.json",
    "?? docs/codex-queue/224/findings.json",
    "?? docs/codex-queue/224/golden-run.json",
    "?? docs/codex-queue/224/kit-generator-attempt1-run.json",
    "?? docs/codex-queue/224/kit-generator-run.json",
    "?? docs/codex-queue/224/kit.json",
    "?? docs/codex-queue/224/manifest-paths.json",
    "?? docs/codex-queue/224/mutate.py",
    "?? docs/codex-queue/224/mutation-M1-run.json",
    "?? docs/codex-queue/224/mutation-M2-run.json",
    "?? docs/codex-queue/224/mutation-M3-run.json",
    "?? docs/codex-queue/224/mutation-M4-run.json",
    "?? docs/codex-queue/224/mutation-M5-run.json",
    "?? docs/codex-queue/224/mutation-M6-run.json",
    "?? docs/codex-queue/224/mutations.json",
    "?? docs/codex-queue/224/pack-170-local-run.json",
    "?? docs/codex-queue/224/pack-170-local.json",
    "?? docs/codex-queue/224/pack-170-run.json",
    "?? docs/codex-queue/224/pack-170.json",
    "?? docs/codex-queue/224/pack-absent-run.json",
    "?? docs/codex-queue/224/pack-absent.json",
    "?? docs/codex-queue/224/pack-empty-run.json",
    "?? docs/codex-queue/224/pack-empty.json",
    "?? docs/codex-queue/224/pack-local-production-run.json",
    "?? docs/codex-queue/224/pack-local-production.json",
    "?? docs/codex-queue/224/pack-local-run.json",
    "?? docs/codex-queue/224/pack-local.json",
    "?? docs/codex-queue/224/parent-before.txt",
    "?? docs/codex-queue/224/paths.json",
    "?? docs/codex-queue/224/preflight.txt",
    "?? docs/codex-queue/224/probe.mts",
    "?? docs/codex-queue/224/prune-probes.json",
    "?? docs/codex-queue/224/requirements.md",
    "?? docs/codex-queue/224/restored-M1-run.json",
    "?? docs/codex-queue/224/restored-M2-run.json",
    "?? docs/codex-queue/224/restored-M3-run.json",
    "?? docs/codex-queue/224/restored-M4-run.json",
    "?? docs/codex-queue/224/restored-M5-run.json",
    "?? docs/codex-queue/224/restored-M6-run.json",
    "?? docs/codex-queue/224/run.py",
    "?? docs/codex-queue/224/scan.json",
    "?? docs/codex-queue/224/split.json",
    "?? docs/codex-queue/224/tree-restored.json",
    "?? docs/codex-queue/224/vite-probes-attempt1-run.json",
    "?? docs/codex-queue/224/vite-probes-prior-run.json",
    "?? docs/codex-queue/224/vite-probes-prior.json",
    "?? docs/codex-queue/224/vite-probes-run.json",
    "?? docs/codex-queue/224/vite-probes.json",
    "?? docs/codex-queue/226-report.md",
    "?? docs/codex-queue/226/a2-package-v2.patch",
    "?? docs/codex-queue/226/base-pkg.diff",
    "?? docs/codex-queue/226/check2.json",
    "?? docs/codex-queue/226/cleanup-check.txt",
    "?? docs/codex-queue/226/delete-list.txt",
    "?? docs/codex-queue/226/diff-lines.txt",
    "?? docs/codex-queue/226/execution-checks.json",
    "?? docs/codex-queue/226/execution-limitations.txt",
    "?? docs/codex-queue/226/git-after.txt",
    "?? docs/codex-queue/226/git-before.txt",
    "?? docs/codex-queue/226/git-final.txt",
    "?? docs/codex-queue/226/git-parent-after.txt",
    "?? docs/codex-queue/226/old-runs.sha256",
    "?? docs/codex-queue/226/old-runs/base-night1.md",
    "?? docs/codex-queue/226/old-runs/r22-balance.md",
    "?? docs/codex-queue/226/old-runs/r22-g12x20.md",
    "?? docs/codex-queue/226/old-runs/r22-pn-balanced.md",
    "?? docs/codex-queue/226/old-runs/r22-pn-challenge.md",
    "?? docs/codex-queue/226/old-runs/r22-pn-relax.md",
    "?? docs/codex-queue/226/old-runs/v1-g12x20.md",
    "?? docs/codex-queue/226/old-runs/v1-night1.md",
    "?? docs/codex-queue/226/old-runs/v1-pn-balanced.md",
    "?? docs/codex-queue/226/old-runs/v1-pn-challenge.md",
    "?? docs/codex-queue/226/old-runs/v1-pn-relax.md",
    "?? docs/codex-queue/226/old-runs/v2-balance.md",
    "?? docs/codex-queue/226/patch-lines.txt",
    "?? docs/codex-queue/226/patch-log.txt",
    "?? docs/codex-queue/226/pct-check.json",
    "?? docs/codex-queue/226/preflight.txt",
    "?? docs/codex-queue/226/runs.sha256",
    "?? docs/codex-queue/226/runs/base-balance160.err",
    "?? docs/codex-queue/226/runs/base-balance160.md",
    "?? docs/codex-queue/226/runs/base-g12x20.err",
    "?? docs/codex-queue/226/runs/base-g12x20.md",
    "?? docs/codex-queue/226/runs/base-night1-160.md",
    "?? docs/codex-queue/226/runs/base-night1-40.md",
    "?? docs/codex-queue/226/runs/base-pn-balanced.md",
    "?? docs/codex-queue/226/runs/base-pn-challenge.md",
    "?? docs/codex-queue/226/runs/base-pn-relax.md",
    "?? docs/codex-queue/226/runs/base-smoke.err",
    "?? docs/codex-queue/226/runs/base-smoke.md",
    "?? docs/codex-queue/226/runs/commands.json",
    "?? docs/codex-queue/226/runs/pkg-balance160.err",
    "?? docs/codex-queue/226/runs/pkg-balance160.md",
    "?? docs/codex-queue/226/runs/pkg-g12x20.err",
    "?? docs/codex-queue/226/runs/pkg-g12x20.md",
    "?? docs/codex-queue/226/runs/pkg-night1-160.md",
    "?? docs/codex-queue/226/runs/pkg-night1-40.md",
    "?? docs/codex-queue/226/runs/pkg-pn-balanced.md",
    "?? docs/codex-queue/226/runs/pkg-pn-challenge.md",
    "?? docs/codex-queue/226/runs/pkg-pn-relax.md",
    "?? docs/codex-queue/226/runs/pkg-smoke.err",
    "?? docs/codex-queue/226/runs/pkg-smoke.md",
    "?? docs/codex-queue/226/runs/refs.txt",
    "?? docs/codex-queue/226/runs/timeline.txt",
    "?? docs/codex-queue/226/summary-repro.json",
    "?? docs/codex-queue/226/summary.json",
    "?? docs/codex-queue/226/summary.md",
    "?? docs/codex-queue/226/tools/collect.py",
    "?? docs/codex-queue/226/tools/measure.py",
    "?? docs/codex-queue/226/tools/report.py",
    "?? docs/codex-queue/226/tools/summarize.mjs",
    "?? docs/codex-queue/227-report.md",
    "?? docs/codex-queue/227/audio-summary.json",
    "?? docs/codex-queue/227/audit-214.json",
    "?? docs/codex-queue/227/audit-215.json",
    "?? docs/codex-queue/227/audit-217.json",
    "?? docs/codex-queue/227/audit-sources/audit-214-215.mjs.txt",
    "?? docs/codex-queue/227/audit-sources/audit-216.py.txt",
    "?? docs/codex-queue/227/audit-sources/audit-217.py.txt",
    "?? docs/codex-queue/227/audit-sources/paths.py.txt",
    "?? docs/codex-queue/227/audit-sources/run-commands.py.txt",
    "?? docs/codex-queue/227/audit-sources/run-tests-217.py.txt",
    "?? docs/codex-queue/227/audit-sources/snap.mjs.txt",
    "?? docs/codex-queue/227/bundle-bytes.json",
    "?? docs/codex-queue/227/cleanup.json",
    "?? docs/codex-queue/227/core-now.json",
    "?? docs/codex-queue/227/diff-stat.txt",
    "?? docs/codex-queue/227/newer.txt",
    "?? docs/codex-queue/227/nginx-blocks.json",
    "?? docs/codex-queue/227/nginx-validator.json",
    "?? docs/codex-queue/227/paths.json",
    "?? docs/codex-queue/227/paths.md",
    "?? docs/codex-queue/227/preflight.txt",
    "?? docs/codex-queue/227/product-diff.txt",
    "?? docs/codex-queue/227/product-paths.json",
    "?? docs/codex-queue/227/runs/audio-all.json",
    "?? docs/codex-queue/227/runs/audio-all.txt",
    "?? docs/codex-queue/227/runs/audio-new.json",
    "?? docs/codex-queue/227/runs/audio-new.txt",
    "?? docs/codex-queue/227/runs/audit-214-215.txt",
    "?? docs/codex-queue/227/runs/audit-216.txt",
    "?? docs/codex-queue/227/runs/audit-217.txt",
    "?? docs/codex-queue/227/runs/bootstrap-syntax.json",
    "?? docs/codex-queue/227/runs/bootstrap-syntax.txt",
    "?? docs/codex-queue/227/runs/core-snapshot.json",
    "?? docs/codex-queue/227/runs/game-dir-syntax.json",
    "?? docs/codex-queue/227/runs/game-dir-syntax.txt",
    "?? docs/codex-queue/227/runs/learning-check.json",
    "?? docs/codex-queue/227/runs/learning-check.txt",
    "?? docs/codex-queue/227/runs/learning-test.json",
    "?? docs/codex-queue/227/runs/learning-test.txt",
    "?? docs/codex-queue/227/runs/nginx-injected-dev.txt",
    "?? docs/codex-queue/227/runs/nginx-injected-play.txt",
    "?? docs/codex-queue/227/runs/nginx-structure.txt",
    "?? docs/codex-queue/227/runs/play-mode.json",
    "?? docs/codex-queue/227/runs/play-mode.txt",
    "?? docs/codex-queue/227/runs/portal-test.json",
    "?? docs/codex-queue/227/runs/portal-test.txt",
    "?? docs/codex-queue/227/runs/space-integration.json",
    "?? docs/codex-queue/227/runs/space-integration.txt",
    "?? docs/codex-queue/227/runs/test-216.json",
    "?? docs/codex-queue/227/runs/test-216.txt",
    "?? docs/codex-queue/227/runs/tsc.json",
    "?? docs/codex-queue/227/runs/tsc.txt",
    "?? docs/codex-queue/227/runs/vite.json",
    "?? docs/codex-queue/227/runs/vite.txt",
    "?? docs/codex-queue/227/runs/whitespace-all-new.json",
    "?? docs/codex-queue/227/runs/whitespace.json",
    "?? docs/codex-queue/227/snap-after.json",
    "?? docs/codex-queue/227/snap-before.json",
    "?? docs/codex-queue/227/snap-delta.json",
    "?? docs/codex-queue/227/tmp-inventory.txt",
    "?? docs/codex-queue/227/tmp-summary.json",
    "?? docs/codex-queue/227/vocab-self-serve.json",
    "?? docs/games/audio/firefly/typing-defense.json",
    "?? docs/games/audio/firefly/typing-defense.md"
  ],
  "removed": []
}
```

Không commit, push hay lệnh Git có ghi. Không sửa mặc định, chapter-1.ts, MODE_SPECS, kit, golden, scripts game, view/app/audio, checkout chính, worktree khác hay Tu Tiên. Không tạo ảnh/âm vì phiếu này chỉ yêu cầu luật sim và số bot. Không làm B9 vì cần người thật; không áp luật được khuyến nghị vì Claude chọn sau duyệt.
