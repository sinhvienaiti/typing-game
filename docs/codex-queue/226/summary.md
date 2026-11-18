# Phiếu 226 · Bảng số

## Đối chiếu số cũ (đọc trước so base → pkg)

So 4948 ô: 4948 khớp ngưỡng, 4948 khớp nguyên văn, 0 lệch. Lệch lớn nhất: {"giây":0,"điểm %":0,"mạng":0,"ván":0,"khác":0}. Chi tiết từng ô nằm trong summary.json, trường known.

| Nhóm | Ô so | Khớp | Lệch | Lệch lớn nhất |
|---|---|---|---|---|
| base M1 1–80 | 12 | 12 | 0 | 0 |
| base §12 5 | 18 | 18 | 0 | 0 |
| base §12 20 | 18 | 18 | 0 | 0 |
| base M3 balanced | 800 | 800 | 0 | 0 |
| base M3 kết ải balanced | 32 | 32 | 0 | 0 |
| base M3 relax | 800 | 800 | 0 | 0 |
| base M3 kết ải relax | 32 | 32 | 0 | 0 |
| base M3 challenge | 800 | 800 | 0 | 0 |
| base M3 kết ải challenge | 32 | 32 | 0 | 0 |
| base M4 40 | 98 | 98 | 0 | 0 |
| pkg M1 1–80 | 12 | 12 | 0 | 0 |
| pkg §12 5 | 18 | 18 | 0 | 0 |
| pkg §12 20 | 18 | 18 | 0 | 0 |
| pkg M3 balanced | 720 | 720 | 0 | 0 |
| pkg M3 relax | 720 | 720 | 0 | 0 |
| pkg M3 challenge | 720 | 720 | 0 | 0 |
| pkg M4 40 | 98 | 98 | 0 | 0 |

## Dải chặt Cân bằng

Số ván suy duy nhất từ ô in của từng bộ 80 seed, cộng hai bộ rồi tính Math.round(k × 1000 / 160), dùng đúng pct của mã. Mỗi ô ghi ván / tổng, ‰, rồi % in. Biên S giữ ô in bộ 1 / bộ 2 / gộp. Đích gộp thắng 780–880 ‰, tức 125–140/160; S Chuẩn 40–60 %, bot khác 35–65 %. “Cách mép” là số kết quả thắng/thua tối thiểu phải đảo để bắt đầu trượt dải thắng; không áp cho S.

| Bot | base · Thắng bộ 1 | pkg · Thắng bộ 1 |
|---|---|---|
| Mới | 69/80; 863 ‰ (86 %) | 64/80; 800 ‰ (80 %) |
| Chậm chắc | 69/80; 863 ‰ (86 %) | 71/80; 888 ‰ (89 %) |
| Chuẩn | 64/80; 800 ‰ (80 %) | 65/80; 813 ‰ (81 %) |
| Khá | 67/80; 838 ‰ (84 %) | 68/80; 850 ‰ (85 %) |
| Ẩu | 66/80; 825 ‰ (83 %) | 63/80; 788 ‰ (79 %) |
| Nhanh | 66/80; 825 ‰ (83 %) | 68/80; 850 ‰ (85 %) |

| Bot | base · Thắng bộ 2 | pkg · Thắng bộ 2 |
|---|---|---|
| Mới | 70/80; 875 ‰ (88 %) | 66/80; 825 ‰ (83 %) |
| Chậm chắc | 70/80; 875 ‰ (88 %) | 75/80; 938 ‰ (94 %) |
| Chuẩn | 70/80; 875 ‰ (88 %) | 66/80; 825 ‰ (83 %) |
| Khá | 69/80; 863 ‰ (86 %) | 68/80; 850 ‰ (85 %) |
| Ẩu | 59/80; 738 ‰ (74 %) | 66/80; 825 ‰ (83 %) |
| Nhanh | 69/80; 863 ‰ (86 %) | 72/80; 900 ‰ (90 %) |

| Bot | base · Thắng gộp | pkg · Thắng gộp |
|---|---|---|
| Mới | 139/160; 869 ‰ (87 %) | 130/160; 813 ‰ (81 %) |
| Chậm chắc | 139/160; 869 ‰ (87 %) | 146/160; 913 ‰ (91 %) |
| Chuẩn | 134/160; 838 ‰ (84 %) | 131/160; 819 ‰ (82 %) |
| Khá | 136/160; 850 ‰ (85 %) | 136/160; 850 ‰ (85 %) |
| Ẩu | 125/160; 781 ‰ (78 %) | 129/160; 806 ‰ (81 %) |
| Nhanh | 135/160; 844 ‰ (84 %) | 140/160; 875 ‰ (88 %) |

| Bot | base · S 1 / 2 / gộp | pkg · S 1 / 2 / gộp | base · kết quả; cách mép | pkg · kết quả; cách mép |
|---|---|---|---|---|
| Mới | 60 % / 70 % / 70 % | 50 % / 60 % / 53 % | TRƯỢT S; dưới 15, trên 2 ván | Đạt; dưới 6, trên 11 ván |
| Chậm chắc | 65 % / 65 % / 65 % | 65 % / 65 % / 65 % | Đạt; dưới 15, trên 2 ván | TRƯỢT thắng; cần 6 ván đảo để về dải |
| Chuẩn | 55 % / 60 % / 55 % | 55 % / 60 % / 55 % | Đạt; dưới 10, trên 7 ván | Đạt; dưới 7, trên 10 ván |
| Khá | 45 % / 50 % / 50 % | 60 % / 58 % / 60 % | Đạt; dưới 12, trên 5 ván | Đạt; dưới 12, trên 5 ván |
| Ẩu | 55 % / 55 % / 55 % | 55 % / 55 % / 55 % | Đạt; dưới 1, trên 16 ván | Đạt; dưới 5, trên 12 ván |
| Nhanh | 60 % / 60 % / 60 % | 55 % / 60 % / 60 % | Đạt; dưới 11, trên 6 ván | Đạt; dưới 16, trên 1 ván |

Kiểm lại 12/12 ô thắng gộp: số bộ 1 + bộ 2, pct của ‰ gộp và đạt/trượt gồm S đều khớp báo cáo.

## B1–B8, B9

| Cổng | base · bộ 1 | pkg · bộ 1 | base · bộ 2 | pkg · bộ 2 | base · gộp | pkg · gộp |
|---|---|---|---|---|---|---|
| B1 | ĐẠT | ĐẠT | TRƯỢT | TRƯỢT | TRƯỢT | TRƯỢT |
| B2 | ĐẠT | ĐẠT | ĐẠT | ĐẠT | ĐẠT | ĐẠT |
| B3 | ĐẠT | ĐẠT | ĐẠT | ĐẠT | ĐẠT | ĐẠT |
| B4 | ĐẠT | ĐẠT | ĐẠT | ĐẠT | ĐẠT | ĐẠT |
| B5 | ĐẠT | ĐẠT | ĐẠT | ĐẠT | ĐẠT | ĐẠT |
| B6 | ĐẠT | ĐẠT | ĐẠT | ĐẠT | ĐẠT | ĐẠT |
| B7 | ĐẠT | ĐẠT | ĐẠT | ĐẠT | TRƯỢT | TRƯỢT |
| B8 | ĐẠT | ĐẠT | ĐẠT | ĐẠT | ĐẠT | ĐẠT |
| B9 | THIẾU SỐ | THIẾU SỐ | THIẾU SỐ | THIẾU SỐ | THIẾU SỐ | THIẾU SỐ |

Bộ 1 seed 1–80, bộ 2 seed 81–160 chấm BALANCE §3; gộp chấm đích chặt. B9 **THIẾU SỐ**, cần người thật chơi. Các cổng trượt dưới đây chép nguyên câu số đo trong báo cáo:

### base, bộ 2, B1

✗ novice: Thắng 88 %, Biên S 70 %, Áp lực P 22 %, Nhàn I 3 %, Ngộp O 0.1 % (lệch: Biên S cao); ✓ steady: Thắng 88 %, Biên S 65 %, Áp lực P 22 %, Nhàn I 2.9 %, Ngộp O 0.1 % (trong dải); ✓ standard: Thắng 88 %, Biên S 60 %, Áp lực P 24 %, Nhàn I 3.9 %, Ngộp O 0.1 % (trong dải); ✓ skilled: Thắng 86 %, Biên S 50 %, Áp lực P 25 %, Nhàn I 2.8 %, Ngộp O 0.1 % (trong dải); ✗ sloppy: Thắng 74 %, Biên S 55 %, Áp lực P 25 %, Nhàn I 4.1 %, Ngộp O 0.2 % (lệch: Thắng thấp); ✓ fast: Thắng 86 %, Biên S 60 %, Áp lực P 24 %, Nhàn I 2.3 %, Ngộp O 0 % (trong dải)

### base, gộp, B1

✗ novice: Thắng 87 %, Biên S 70 %, Áp lực P 23 %, Nhàn I 3 %, Ngộp O 0.1 % (lệch: Biên S cao); ✓ steady: Thắng 87 %, Biên S 65 %, Áp lực P 22 %, Nhàn I 2.8 %, Ngộp O 0.1 % (trong dải); ✓ standard: Thắng 84 %, Biên S 55 %, Áp lực P 24 %, Nhàn I 3.8 %, Ngộp O 0.1 % (trong dải); ✓ skilled: Thắng 85 %, Biên S 50 %, Áp lực P 26 %, Nhàn I 2.6 %, Ngộp O 0.1 % (trong dải); ✓ sloppy: Thắng 78 %, Biên S 55 %, Áp lực P 25 %, Nhàn I 4.1 %, Ngộp O 0.2 % (trong dải); ✓ fast: Thắng 84 %, Biên S 60 %, Áp lực P 24 %, Nhàn I 2 %, Ngộp O 0.1 % (trong dải); ✓ standard · Biên S chặt (gộp): 55 % (40–60 %)

### base, gộp, B7

✓ child · Thư giãn: 1.58 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ novice · Thư giãn: 1.87 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ steady · Thư giãn: 1.72 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard · Thư giãn: 1.61 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ skilled · Thư giãn: 1.45 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ sloppy · Thư giãn: 1.66 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ fast · Thư giãn: 1.21 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type · Thư giãn: 2.19 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ type-only · Thư giãn: 2.10 bậc/đợt, khoảng sinh 100 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@good · Thư giãn: 1.61 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@poor · Thư giãn: 1.60 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ child · Cân bằng: 1.95 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ novice · Cân bằng: 2.54 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ steady · Cân bằng: 2.38 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard · Cân bằng: 2.01 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ skilled · Cân bằng: 1.81 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ sloppy · Cân bằng: 1.95 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ fast · Cân bằng: 1.35 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type · Cân bằng: 2.18 bậc/đợt, khoảng sinh 93 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ type-only · Cân bằng: 1.71 bậc/đợt, khoảng sinh 100 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@good · Cân bằng: 2.00 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@poor · Cân bằng: 1.60 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type@kite · Cân bằng: 2.18 bậc/đợt, khoảng sinh 93 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@book20 · Cân bằng: 2.00 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ child · Thử thách: 1.71 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ novice · Thử thách: 1.85 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ steady · Thử thách: 1.66 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard · Thử thách: 1.52 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ skilled · Thử thách: 1.38 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ sloppy · Thử thách: 1.54 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ fast · Thử thách: 1.15 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type · Thử thách: 1.58 bậc/đợt, khoảng sinh 93 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ type-only · Thử thách: 1.14 bậc/đợt, khoảng sinh 100 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@good · Thử thách: 1.51 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@poor · Thử thách: 1.61 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type@kite · Thử thách: 1.58 bậc/đợt, khoảng sinh 93 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✗ standard · tắt nhịp: Thắng 88 %, Biên S 55 %, Áp lực P 24 %, Nhàn I 4.1 %, Ngộp O 0.1 % (lệch: Thắng cao); ✓ standard · tắt nhịp · Biên S chặt (gộp): 55 % (40–60 %)

### pkg, bộ 2, B1

✓ novice: Thắng 83 %, Biên S 60 %, Áp lực P 21 %, Nhàn I 3 %, Ngộp O 0 % (trong dải); ✗ steady: Thắng 94 %, Biên S 65 %, Áp lực P 21 %, Nhàn I 3.7 %, Ngộp O 0 % (lệch: Thắng cao); ✓ standard: Thắng 83 %, Biên S 60 %, Áp lực P 24 %, Nhàn I 5.3 %, Ngộp O 0 % (trong dải); ✓ skilled: Thắng 85 %, Biên S 58 %, Áp lực P 25 %, Nhàn I 2 %, Ngộp O 0 % (trong dải); ✓ sloppy: Thắng 83 %, Biên S 55 %, Áp lực P 25 %, Nhàn I 5.4 %, Ngộp O 0.1 % (trong dải); ✓ fast: Thắng 90 %, Biên S 60 %, Áp lực P 23 %, Nhàn I 2.1 %, Ngộp O 0 % (trong dải)

### pkg, gộp, B1

✓ novice: Thắng 81 %, Biên S 53 %, Áp lực P 22 %, Nhàn I 2.9 %, Ngộp O 0 % (trong dải); ✗ steady: Thắng 91 %, Biên S 65 %, Áp lực P 22 %, Nhàn I 3.7 %, Ngộp O 0 % (lệch: Thắng cao); ✓ standard: Thắng 82 %, Biên S 55 %, Áp lực P 25 %, Nhàn I 5.2 %, Ngộp O 0 % (trong dải); ✓ skilled: Thắng 85 %, Biên S 60 %, Áp lực P 25 %, Nhàn I 2.1 %, Ngộp O 0 % (trong dải); ✓ sloppy: Thắng 81 %, Biên S 55 %, Áp lực P 25 %, Nhàn I 5.4 %, Ngộp O 0.1 % (trong dải); ✓ fast: Thắng 88 %, Biên S 60 %, Áp lực P 24 %, Nhàn I 2 %, Ngộp O 0 % (trong dải); ✓ standard · Biên S chặt (gộp): 55 % (40–60 %)

### pkg, gộp, B7

✓ child · Thư giãn: 1.56 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ novice · Thư giãn: 1.84 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ steady · Thư giãn: 1.56 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard · Thư giãn: 1.42 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ skilled · Thư giãn: 1.35 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ sloppy · Thư giãn: 1.45 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ fast · Thư giãn: 1.21 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type · Thư giãn: 1.83 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ type-only · Thư giãn: 2.11 bậc/đợt, khoảng sinh 100 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@good · Thư giãn: 1.42 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@poor · Thư giãn: 1.45 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ child · Cân bằng: 1.94 bậc/đợt, khoảng sinh 93 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ novice · Cân bằng: 2.28 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ steady · Cân bằng: 2.16 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard · Cân bằng: 1.96 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ skilled · Cân bằng: 1.71 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ sloppy · Cân bằng: 1.96 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ fast · Cân bằng: 1.66 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type · Cân bằng: 2.28 bậc/đợt, khoảng sinh 93 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ type-only · Cân bằng: 1.65 bậc/đợt, khoảng sinh 100 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@good · Cân bằng: 1.91 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@poor · Cân bằng: 1.63 bậc/đợt, khoảng sinh 93 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type@kite · Cân bằng: 2.28 bậc/đợt, khoảng sinh 93 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@book20 · Cân bằng: 1.97 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ child · Thử thách: 1.64 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ novice · Thử thách: 1.96 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ steady · Thử thách: 1.66 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard · Thử thách: 1.44 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ skilled · Thử thách: 1.38 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ sloppy · Thử thách: 1.54 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ fast · Thử thách: 1.16 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type · Thử thách: 1.62 bậc/đợt, khoảng sinh 93 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ type-only · Thử thách: 1.12 bậc/đợt, khoảng sinh 100 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@good · Thử thách: 1.31 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@poor · Thử thách: 1.47 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type@kite · Thử thách: 1.62 bậc/đợt, khoảng sinh 93 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✗ standard · tắt nhịp: Thắng 89 %, Biên S 60 %, Áp lực P 24 %, Nhàn I 5.1 %, Ngộp O 0 % (lệch: Thắng cao); ✓ standard · tắt nhịp · Biên S chặt (gộp): 60 % (40–60 %)

| base · dải rộng gộp | pkg · dải rộng gộp |
|---|---|
| Để so, B1 và B7 gộp theo dải BALANCE §3 (75–90 %, 35–65 %): B1 trượt, B7 đạt. | Để so, B1 và B7 gộp theo dải BALANCE §3 (75–90 %, 35–65 %): B1 trượt, B7 đạt. |

B7 có thêm hàng Chuẩn tắt bộ điều nhịp; tái tính số ván từ hai bộ 80 để giải thích cổng trượt cả khi ô gộp in 88 %:

| Cây | Thắng bộ 1 | Thắng bộ 2 | Thắng gộp | Biên S gộp | Đích thắng chặt |
|---|---|---|---|---|---|
| base | 70/80 (88 %) | 71/80 (89 %) | 141/160; 881 ‰ (88 %) | 55 % | TRƯỢT |
| pkg | 70/80 (88 %) | 72/80 (90 %) | 142/160; 888 ‰ (89 %) | 60 % | TRƯỢT |

## Boss gộp, Cân bằng

| Bot | base · boss rút | pkg · boss rút | base · giao chiến p50 (s) | pkg · giao chiến p50 (s) | base · mạng mất đỉnh p50 | pkg · mạng mất đỉnh p50 |
|---|---|---|---|---|---|---|
| Mới | 87 % | 81 % | 54.7 | 52.3 | 3.0 | 6.0 |
| Chậm chắc | 88 % | 91 % | 52.6 | 51.1 | 2.0 | 3.0 |
| Chuẩn | 84 % | 82 % | 49.9 | 49.8 | 2.0 | 3.0 |
| Khá | 85 % | 85 % | 48.3 | 47.3 | 2.0 | 3.0 |
| Ẩu | 78 % | 81 % | 52.0 | 52.0 | 3.0 | 4.0 |
| Nhanh | 84 % | 88 % | 46.0 | 44.9 | 2.0 | 3.0 |

| Cây | G3 / G8 · bộ 1, bộ 2, gộp |
|---|---|
| base | G3 (bot Chuẩn, Cân bằng; giao chiến p50 45–75 s, núm là tốc boss §6.5 bước 1): bộ 1 50,2 s / bộ 2 49,4 s / gộp 49,9 s: đạt. G8 (bot Chuẩn, Cân bằng; trồi → trúng đầu p50 ≤ 35 s, Nhàn I đỉnh boss ≤ 10 %): bộ 1 32,1 s, 0,4 % / bộ 2 24,1 s, 0,3 % / gộp 24,1 s, 0,3 %: đạt. |
| pkg | G3 (bot Chuẩn, Cân bằng; giao chiến p50 45–75 s, núm là tốc boss §6.5 bước 1): bộ 1 51,9 s / bộ 2 48,5 s / gộp 49,8 s: đạt. G8 (bot Chuẩn, Cân bằng; trồi → trúng đầu p50 ≤ 35 s, Nhàn I đỉnh boss ≤ 10 %): bộ 1 32,1 s, 0,4 % / bộ 2 24,1 s, 0,7 % / gộp 24,1 s, 0,5 %: đạt. |

| Cây | R2 gộp · G2, G5, G6 (nguyên dòng) |
|---|---|
| base | R2 gộp: G2 (bot Chuẩn, Cân bằng): gõ Đêm 1–4 22,6 % (15–25 %), Đêm 5 24,2 % (≤ 35 %): đạt. G5 (mọi bot gõ, Cân bằng; lên boss / cả ải, ≤ 15 %, ≤ 15 %): Mới 1,2 % / 10,2 %; Chậm chắc 0,2 % / 13,6 %; Chuẩn 0,2 % / 13,7 %; Khá 0,1 % / 13,4 %; Ẩu 1,0 % / 10,6 %; Nhanh 0,4 % / 13,1 %: đạt. Thử thách (báo cáo): Mới 0,6 % / 10,2 %; Chậm chắc 0,3 % / 12,1 %; Chuẩn 0,8 % / 11,9 %; Khá 0,6 % / 10,7 %; Ẩu 1,4 % / 8,8 %; Nhanh 1,1 % / 9,4 %. G6 (bot Chuẩn, theo §9.1, BUILD_NOTES §7.3): một lời gọi trực tiếp mỗi 36.1 s ở Đêm 4 (25–40 s), mở cùng lúc tối đa 2 không boss (≤ 2), 0 có boss (≤ 3): đạt; mọi bot (s mỗi lời gọi): Mới 49.6, Chậm chắc 39.1, Chuẩn 36.1, Khá 27.4, Ẩu 33.6, Nhanh 33.5; từ trực tiếp 0,3 % số từ cả ải (5–10 % của TK 9.1 cần đủ ba động từ: **trượt**). |
| pkg | R2 gộp: G2 (bot Chuẩn, Cân bằng): gõ Đêm 1–4 16,9 % (15–25 %), Đêm 5 18,7 % (≤ 35 %): đạt. G5 (mọi bot gõ, Cân bằng; lên boss / cả ải, ≤ 15 %, ≤ 15 %): Mới 2,0 % / 6,5 %; Chậm chắc 0,9 % / 9,1 %; Chuẩn 0,4 % / 11,8 %; Khá 0,3 % / 12,1 %; Ẩu 1,6 % / 7,0 %; Nhanh 0,0 % / 14,0 %: đạt. Thử thách (báo cáo): Mới 1,0 % / 8,2 %; Chậm chắc 0,3 % / 11,3 %; Chuẩn 1,0 % / 9,9 %; Khá 0,2 % / 11,4 %; Ẩu 2,3 % / 5,4 %; Nhanh 0,3 % / 10,8 %. G6 (bot Chuẩn, theo §9.1, BUILD_NOTES §7.3): một lời gọi trực tiếp mỗi 36.6 s ở Đêm 4 (25–40 s), mở cùng lúc tối đa 2 không boss (≤ 2), 0 có boss (≤ 3): đạt; mọi bot (s mỗi lời gọi): Mới 51.9, Chậm chắc 43.2, Chuẩn 36.6, Khá 28.5, Ẩu 36.7, Nhanh 32.5; từ trực tiếp 0,4 % số từ cả ải (5–10 % của TK 9.1 cần đủ ba động từ: **trượt**). |

## §12 trên 20 seed

| Cổng | Đích | base · số | base · kết quả | pkg · số | pkg · kết quả |
|---|---|---|---|---|---|
| 4 | không thua | mạng 6 / 9 / 9 / 7 / 7 / 4 / 6 / 8 / 4 / 5 / 8 / 5 / 10 / 4 / 3 / 3 / 6 / 6 / 8 / 5 | Đạt | mạng 1 / 7 / 4 / 8 / 7 / 6 / 8 / 8 / 5 / 8 / 2 / 1 / 5 / 7 / 7 / 2 / 7 / 4 / 9 / 6 | Đạt |
| 5a | ≤ 8 s | 8.48 s | Hỏng | 7.95 s | Đạt |
| 5b | 30–45 % | 29.5 % | Hỏng | 30.1 % | Đạt |
| 5c | 15–25 % | 23.0 % | Đạt | 15.5 % | Đạt |
| 6 | 0 | 0 | Đạt | 0 | Đạt |
| 7 | ≥ +25 % | 550 / 398 = +38.0 % | Đạt | 553 / 397 = +39.2 % | Đạt |
| 5a Thư giãn | ≤ 6 s | 5.67 s | Đạt | 5.67 s | Đạt |
| 5a Thử thách | ≤ 10 s | 10.00 s | Đạt | 9.98 s | Đạt |
| 5a Học | ≤ 6 s | 5.67 s | Đạt | 5.67 s | Đạt |

| Cổng 4 | base | pkg |
|---|---|---|
| Thấp nhất; seed | 3 mạng; seed 15, 16 | 1 mạng; seed 1, 12 |

## §12 trên 5 seed

| Cổng | Đích | base · số | base · kết quả | pkg · số | pkg · kết quả |
|---|---|---|---|---|---|
| 4 | không thua | mạng 6 / 9 / 9 / 7 / 7 | Đạt | mạng 1 / 7 / 4 / 8 / 7 | Đạt |
| 5a | ≤ 8 s | 7.90 s | Đạt | 7.93 s | Đạt |
| 5b | 30–45 % | 30.2 % | Đạt | 30.5 % | Đạt |
| 5c | 15–25 % | 22.2 % | Đạt | 15.4 % | Đạt |
| 6 | 0 | 0 | Đạt | 0 | Đạt |
| 7 | ≥ +25 % | 552 / 399 = +38.2 % | Đạt | 552 / 399 = +38.2 % | Đạt |
| 5a Thư giãn | ≤ 6 s | 5.67 s | Đạt | 5.67 s | Đạt |
| 5a Thử thách | ≤ 10 s | 9.88 s | Đạt | 9.97 s | Đạt |
| 5a Học | ≤ 6 s | 5.67 s | Đạt | 5.67 s | Đạt |

| Cổng 4 | base | pkg |
|---|---|---|
| Thấp nhất; seed | 6 mạng; seed 1 | 1 mạng; seed 1 |

## Đêm 1 · mạng mất · seed 25–48

| Chế độ | Bot | base | pkg |
|---|---|---|---|
| Cân bằng | Trẻ em | 1.67 | 1.42 |
| Cân bằng | Mới | 0.63 | 0.42 |
| Cân bằng | Chậm chắc | 2.08 | 0.96 |
| Cân bằng | Chuẩn | 1.83 | 1.38 |
| Cân bằng | Khá | 4.08 | 2.38 |
| Cân bằng | Ẩu | 1.67 | 1.58 |
| Cân bằng | Nhanh | 2.63 | 2.29 |
| Cân bằng | Không gõ | 3.75 | 3.75 |
| Thư giãn | Trẻ em | 0.00 | 0.00 |
| Thư giãn | Mới | 0.04 | 0.04 |
| Thư giãn | Chậm chắc | 0.29 | 0.08 |
| Thư giãn | Chuẩn | 0.38 | 0.38 |
| Thư giãn | Khá | 0.54 | 0.50 |
| Thư giãn | Ẩu | 0.50 | 0.50 |
| Thư giãn | Nhanh | 0.79 | 0.67 |
| Thư giãn | Không gõ | 0.08 | 0.08 |
| Thử thách | Trẻ em | 1.96 | 1.96 |
| Thử thách | Mới | 2.46 | 1.71 |
| Thử thách | Chậm chắc | 3.17 | 1.38 |
| Thử thách | Chuẩn | 3.50 | 2.08 |
| Thử thách | Khá | 3.04 | 2.71 |
| Thử thách | Ẩu | 4.21 | 2.21 |
| Thử thách | Nhanh | 3.13 | 3.08 |
| Thử thách | Không gõ | 4.67 | 4.67 |

## Đêm 1 · Cân bằng · seed 1–40 và 1–160

| Seed | Bot | base · mạng mất | pkg · mạng mất | base · ván mất ≥ 3 | pkg · ván mất ≥ 3 |
|---|---|---|---|---|---|
| 1–40 | Mới | 0.47 | 0.55 | 0 | 1 |
| 1–40 | Chậm chắc | 1.82 | 0.72 | 17 | 1 |
| 1–40 | Chuẩn | 1.77 | 1.27 | 18 | 7 |
| 1–40 | Khá | 4.22 | 2.00 | 36 | 19 |
| 1–40 | Ẩu | 1.55 | 1.48 | 14 | 14 |
| 1–40 | Nhanh | 2.60 | 2.17 | 20 | 16 |
| 1–40 | Không gõ | 3.85 | 3.85 | 35 | 35 |
| 1–160 | Mới | 0.65 | 0.62 | 8 | 8 |
| 1–160 | Chậm chắc | 1.64 | 0.79 | 59 | 12 |
| 1–160 | Chuẩn | 1.71 | 1.18 | 56 | 25 |
| 1–160 | Khá | 4.19 | 1.94 | 137 | 65 |
| 1–160 | Ẩu | 1.51 | 1.43 | 49 | 43 |
| 1–160 | Nhanh | 2.44 | 2.06 | 76 | 59 |
| 1–160 | Không gõ | 3.74 | 3.74 | 141 | 141 |

## Đêm 3 · Nhàn I · seed 25–48

| Chế độ | Bot | base | pkg |
|---|---|---|---|
| Cân bằng | Trẻ em | 6.4 % | 6.0 % |
| Cân bằng | Mới | 12.1 % | 14.1 % |
| Cân bằng | Chậm chắc | 14.2 % | 24.5 % |
| Cân bằng | Chuẩn | 20.1 % | 31.1 % |
| Cân bằng | Khá | 9.9 % | 11.7 % |
| Cân bằng | Ẩu | 20.1 % | 34.6 % |
| Cân bằng | Nhanh | 6.0 % | 8.9 % |
| Cân bằng | Không gõ | 5.9 % | 7.6 % |
| Thư giãn | Trẻ em | 8.6 % | 14.3 % |
| Thư giãn | Mới | 1.4 % | 4.4 % |
| Thư giãn | Chậm chắc | 6.7 % | 7.1 % |
| Thư giãn | Chuẩn | 6.9 % | 15.3 % |
| Thư giãn | Khá | 8.1 % | 13.7 % |
| Thư giãn | Ẩu | 5.0 % | 14.7 % |
| Thư giãn | Nhanh | 7.1 % | 13.4 % |
| Thư giãn | Không gõ | 6.0 % | 6.6 % |
| Thử thách | Trẻ em | 6.0 % | 6.2 % |
| Thử thách | Mới | 19.6 % | 26.1 % |
| Thử thách | Chậm chắc | 7.3 % | 11.8 % |
| Thử thách | Chuẩn | 8.5 % | 15.5 % |
| Thử thách | Khá | 10.6 % | 24.5 % |
| Thử thách | Ẩu | 9.4 % | 15.0 % |
| Thử thách | Nhanh | 17.8 % | 21.6 % |
| Thử thách | Không gõ | 5.5 % | 10.6 % |

## Kết ải của đầu dò từng pha · seed 25–48

| Chế độ | Bot | base · qua 4 đêm / thắng 5 / S | pkg · qua 4 đêm / thắng 5 / S |
|---|---|---|---|
| Cân bằng | Trẻ em | 100 % / 0 % / 0 % | 100 % / 0 % / 0 % |
| Cân bằng | Mới | 100 % / 79 % / 30 % | 100 % / 83 % / 45 % |
| Cân bằng | Chậm chắc | 100 % / 75 % / 60 % | 100 % / 96 % / 65 % |
| Cân bằng | Chuẩn | 100 % / 75 % / 55 % | 100 % / 79 % / 50 % |
| Cân bằng | Khá | 100 % / 79 % / 50 % | 100 % / 75 % / 50 % |
| Cân bằng | Ẩu | 100 % / 67 % / 55 % | 100 % / 75 % / 50 % |
| Cân bằng | Nhanh | 100 % / 79 % / 55 % | 100 % / 88 % / 55 % |
| Cân bằng | Không gõ | 96 % / 0 % / 0 % | 100 % / 0 % / 0 % |
| Thư giãn | Trẻ em | 100 % / 96 % / 40 % | 100 % / 92 % / 30 % |
| Thư giãn | Mới | 100 % / 100 % / 90 % | 100 % / 100 % / 85 % |
| Thư giãn | Chậm chắc | 100 % / 100 % / 90 % | 100 % / 100 % / 85 % |
| Thư giãn | Chuẩn | 100 % / 100 % / 95 % | 100 % / 100 % / 90 % |
| Thư giãn | Khá | 100 % / 100 % / 90 % | 100 % / 100 % / 85 % |
| Thư giãn | Ẩu | 100 % / 100 % / 95 % | 100 % / 100 % / 85 % |
| Thư giãn | Nhanh | 100 % / 100 % / 95 % | 100 % / 100 % / 90 % |
| Thư giãn | Không gõ | 100 % / 100 % / 60 % | 100 % / 100 % / 55 % |
| Thử thách | Trẻ em | 100 % / 0 % / 0 % | 100 % / 0 % / 0 % |
| Thử thách | Mới | 100 % / 79 % / 40 % | 100 % / 79 % / 45 % |
| Thử thách | Chậm chắc | 100 % / 83 % / 50 % | 100 % / 83 % / 50 % |
| Thử thách | Chuẩn | 100 % / 83 % / 20 % | 100 % / 75 % / 45 % |
| Thử thách | Khá | 100 % / 63 % / 35 % | 100 % / 67 % / 35 % |
| Thử thách | Ẩu | 100 % / 79 % / 15 % | 100 % / 71 % / 25 % |
| Thử thách | Nhanh | 100 % / 42 % / 0 % | 100 % / 75 % / 40 % |
| Thử thách | Không gõ | 71 % / 0 % / 0 % | 50 % / 0 % / 0 % |

## Thử thách · thắng gộp 160 ván

| Bot | base · ván / 160; ‰; % in | pkg · ván / 160; ‰; % in |
|---|---|---|
| Trẻ em | 1/160; 6 ‰; 0.6 % | 3/160; 19 ‰; 1.9 % |
| Mới | 116/160; 725 ‰; 73 % | 128/160; 800 ‰; 80 % |
| Chậm chắc | 141/160; 881 ‰; 88 % | 143/160; 894 ‰; 89 % |
| Chuẩn | 115/160; 719 ‰; 72 % | 109/160; 681 ‰; 68 % |
| Khá | 108/160; 675 ‰; 68 % | 109/160; 681 ‰; 68 % |
| Ẩu | 103/160; 644 ‰; 64 % | 118/160; 738 ‰; 74 % |
| Nhanh | 91/160; 569 ‰; 57 % | 116/160; 725 ‰; 73 % |
| Không gõ | 0/160; 0 ‰; 0 % | 0/160; 0 ‰; 0 % |
| type-only | 0/160; 0 ‰; 0 % | 0/160; 0 ‰; 0 % |
| standard@good | 133/160; 831 ‰; 83 % | 139/160; 869 ‰; 87 % |
| standard@poor | 16/160; 100 ‰; 10 % | 18/160; 113 ‰; 11 % |
| no-type@kite | 0/160; 0 ‰; 0 % | 0/160; 0 ‰; 0 % |

## Thời gian, luồng, tải

Chạy tuần tự toàn bộ. Mọi lệnh gọi nice -n 15 nhưng sandbox từ chối setpriority ở cả 16 lệnh; không xác nhận được ưu tiên thực nice 15. TMPDIR trong bản chép. Sandbox chặn sysctl và ps; timeline giữ nguyên lỗi sysctl, tải lấy từ uptime, cùng số tải 1 phút. Không kiểm được tiến trình balance.ts của làn khác; phiếu chỉ chạy một lệnh tại mỗi thời điểm. Tải đầu lệnh > 10 dùng 2 luồng, còn lại 4; khói luôn 2, đầu dò luôn 1.

| Lệnh | Bắt đầu (+07:00) | Kết thúc | Giây | Luồng | Tải 1 phút | Mã | Seed đúng |
|---|---|---|---|---|---|---|---|
| base-smoke | 2026-10-30T13:45:10.717447+07:00 | 2026-10-30T13:45:23.136163+07:00 | 12.418 | 2 | 6.27 | 0 | Có |
| pkg-smoke | 2026-10-30T13:45:23.150721+07:00 | 2026-10-30T13:45:35.432160+07:00 | 12.282 | 2 | 7.37 | 0 | Có |
| base-balance160 | 2026-10-30T13:45:35.447865+07:00 | 2026-10-30T13:54:31.245793+07:00 | 535.795 | 4 | 7.98 | 0 | Có |
| base-g12x20 | 2026-10-30T13:54:31.264522+07:00 | 2026-10-30T13:55:21.923426+07:00 | 50.659 | 4 | 9.71 | 0 | Có |
| base-pn-balanced | 2026-10-30T13:55:21.939696+07:00 | 2026-10-30T13:56:14.083455+07:00 | 52.143 | 1 | 8.41 | 0 | Có |
| base-pn-relax | 2026-10-30T13:56:14.096113+07:00 | 2026-10-30T13:57:18.502896+07:00 | 64.416 | 1 | 8.05 | 0 | Có |
| base-pn-challenge | 2026-10-30T13:57:18.516166+07:00 | 2026-10-30T13:58:02.370326+07:00 | 43.857 | 1 | 7.47 | 0 | Có |
| base-night1-40 | 2026-10-30T13:58:02.384633+07:00 | 2026-10-30T13:58:10.990504+07:00 | 8.606 | 1 | 8.19 | 0 | Có |
| base-night1-160 | 2026-10-30T13:58:11.004039+07:00 | 2026-10-30T13:58:43.248369+07:00 | 32.244 | 1 | 7.93 | 0 | Có |
| pkg-balance160 | 2026-10-30T13:58:43.257678+07:00 | 2026-10-30T14:06:24.347039+07:00 | 461.088 | 4 | 7.23 | 0 | Có |
| pkg-g12x20 | 2026-10-30T14:06:24.355843+07:00 | 2026-10-30T14:07:12.296173+07:00 | 47.94 | 2 | 10.26 | 0 | Có |
| pkg-pn-balanced | 2026-10-30T14:07:12.305176+07:00 | 2026-10-30T14:07:55.393166+07:00 | 43.088 | 1 | 7.54 | 0 | Có |
| pkg-pn-relax | 2026-10-30T14:07:55.400580+07:00 | 2026-10-30T14:09:13.791383+07:00 | 78.391 | 1 | 5.85 | 0 | Có |
| pkg-pn-challenge | 2026-10-30T14:09:13.824755+07:00 | 2026-10-30T14:09:58.880964+07:00 | 45.057 | 1 | 16.76 | 0 | Có |
| pkg-night1-40 | 2026-10-30T14:09:58.890231+07:00 | 2026-10-30T14:10:05.880281+07:00 | 6.99 | 1 | 14.4 | 0 | Có |
| pkg-night1-160 | 2026-10-30T14:10:05.889130+07:00 | 2026-10-30T14:10:35.885332+07:00 | 29.996 | 1 | 12.96 | 0 | Có |
