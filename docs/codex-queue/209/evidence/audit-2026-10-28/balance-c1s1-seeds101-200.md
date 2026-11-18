# Tuyến Cuối: báo cáo cân bằng (100 seed mỗi ô, seed 101–200)

Dải đích (BALANCE.md §3):

| Chế độ | Thắng | Biên S | Áp lực P | Nhàn I | Ngộp O | Gần thua N | Quãng Q |
|---|---|---|---|---|---|---|---|
| Thư giãn | ≥ 92 % | ≥ 70 % | 5–15 % | ≤ 20 % | ≤ 3 % | ≤ 0.2 | ≤ 45 % |
| Cân bằng | 75–90 % | 35–65 % | 15–35 % | ≤ 10 % | ≤ 8 % | 0.3–1 | 50–70 % |
| Thử thách | 50–75 % | 15–45 % | 30–50 % | ≤ 5 % | ≤ 15 % | 1–2 | 60–80 % |

## c1-s1 · Ca trực đầu

| Bot | Chế độ | k | E từ | Thắng | Biên S | Áp lực P | Nhàn I | Ngộp O | Gần thua N | Quãng Q | Hạ quái (s) | Bậc/đợt (khoảng sinh) | Mất giáp: rỉ/chạm/đạn | Quái tối đa | E · a đo · từ/phút | Học | Dài (s) | Súng chọn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| child | Thư giãn | 0,750 | 15 | 91 % ↓ | 66 % ↓ | 22 % ↑ | 1.5 % | 0 % | 0,16 | 77 % | 3,0 | 1,22 (93 %–114 %) | 23/16/6 | 59 | 15,0 · 88 % · 16,1 | đạt | 150 | Pulse Gun+Heat Beam 100% |
| novice | Thư giãn | 0,750 | 25 | 100 % | 98 % | 2.8 % ↓ | 9.9 % | 0 % | 0,01 | 48 % | 0,7 | 1,44 (86 %–100 %) | 3/1/0 | 47 | 25,1 · 92 % · 20,9 | đạt | 150 | Pulse Gun+Star Mortar 56%, Pulse Gun+Rail Gun 8% |
| steady | Thư giãn | 0,790 | 25 | 100 % | 99 % | 2 % ↓ | 11 % | 0 % | 0,00 | 47 % | 0,6 | 1,46 (86 %–100 %) | 3/0/0 | 47 | 25,0 · 99 % · 22,4 | đạt | 150 | Pulse Gun+Star Mortar 56%, Pulse Gun+Rail Gun 8% |
| standard | Thư giãn | 1,000 | 35 | 100 % | 98 % | 2.5 % ↓ | 16 % | 0 % | 0,00 | 48 % | 0,6 | 1,34 (86 %–100 %) | 4/0/0 | 54 | 35,1 · 95 % · 26,2 | đạt | 150 | Pulse Gun+Star Mortar 56%, Pulse Gun+Rail Gun 8% |
| skilled | Thư giãn | 1,202 | 50 | 100 % | 97 % | 2.2 % ↓ | 30 % ↑ | 0 % | 0,00 | 49 % | 0,5 | 1,53 (86 %–100 %) | 3/0/0 | 61 | 50,1 · 96 % · 25,7 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| sloppy | Thư giãn | 1,045 | 50 | 100 % | 97 % | 3.4 % ↓ | 17 % | 0.5 % | 0,00 | 49 % | 0,7 | 1,31 (86 %–107 %) | 5/1/0 | 57 | 50,2 · 85 % · 26,6 | đạt | 150 | Pulse Gun+Star Mortar 56%, Pulse Gun+Rail Gun 8% |
| fast | Thư giãn | 1,248 | 70 | 100 % | 96 % | 2.6 % ↓ | 25 % ↑ | 0 % | 0,00 | 50 % | 0,6 | 1,36 (86 %–100 %) | 4/0/0 | 64 | 69,8 · 97 % · 26,0 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| no-type | Thư giãn | 0,750 | 10 | 0 % ↓ | 0 % ↓ | 74 % ↑ | 0 % | 0 % | 0,05 | — | — | 0,85 (100 %–100 %) | 18/100/0 | 62 | — · — · 0,0 | — | 33 | Pulse Gun+Star Mortar 100% |
| type-only | Thư giãn | 1,000 | 35 | 100 % | 98 % | 1.5 % ↓ | 19 % | 0 % | 0,00 | 48 % | 0,4 | 1,45 (86 %–100 %) | 2/0/0 | 54 | 35,1 · 95 % · 25,2 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@good | Thư giãn | 1,000 | 35 | 100 % | 98 % | 1.2 % ↓ | 24 % ↑ | 0 % | 0,00 | 47 % | 0,4 | 1,53 (86 %–100 %) | 2/0/0 | 53 | 35,3 · 95 % · 23,5 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@poor | Thư giãn | 1,000 | 35 | 100 % | 91 % | 7.1 % | 7.7 % | 0 % | 0,00 | 76 % | 1,8 | 0,47 (93 %–100 %) | 10/0/0 | 65 | 34,9 · 95 % · 30,1 | đạt | 150 | Pulse Gun+Heat Beam 100% |
| standard (tắt nhịp) | Thư giãn | 1,000 | 35 | 100 % | 98 % | 1.9 % ↓ | 17 % | 0 % | 0,00 | 47 % | 0,6 | 0,00 (100 %–100 %) | 3/0/0 | 50 | 35,1 · 95 % · 25,7 | đạt | 150 | Pulse Gun+Star Mortar 56%, Pulse Gun+Rail Gun 8% |
| child | Cân bằng | 0,750 | 15 | 0 % ↓ | 0 % ↓ | 50 % ↑ | 0.4 % | 0.1 % | 0,13 | 78 % | 3,5 | 1,36 (93 %–107 %) | 58/38/13 | 86 | 15,5 · 88 % · 16,2 | đạt | 81 | Pulse Gun+Heat Beam 100% |
| novice | Cân bằng | 0,750 | 25 | 87 % | 63 % | 23 % | 3.2 % | 0 % | 0,19 | 65 % | 1,5 | 1,47 (86 %–107 %) | 35/9/5 | 78 | 25,1 · 92 % · 22,9 | đạt | 150 | Pulse Gun+Star Mortar 56%, Pulse Gun+Rail Gun 8% |
| steady | Cân bằng | 0,790 | 25 | 92 % ↑ | 69 % ↑ | 19 % | 3.5 % | 0 % | 0,09 | 63 % | 1,3 | 1,47 (86 %–100 %) | 31/7/3 | 78 | 25,0 · 99 % · 24,8 | đạt | 150 | Pulse Gun+Star Mortar 56%, Pulse Gun+Rail Gun 8% |
| standard | Cân bằng | 1,000 | 35 | 82 % | 66 % ↑ | 22 % | 6.5 % | 0 % | 0,13 | 62 % | 1,3 | 1,32 (86 %–107 %) | 35/12/2 | 98 | 35,1 · 95 % · 29,6 | đạt | 150 | Pulse Gun+Star Mortar 56%, Pulse Gun+Rail Gun 8% |
| skilled | Cân bằng | 1,202 | 50 | 84 % | 69 % ↑ | 19 % | 15 % ↑ | 0 % | 0,08 | 62 % | 1,0 | 1,35 (86 %–100 %) | 33/10/1 | 111 | 49,9 · 96 % · 31,6 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| sloppy | Cân bằng | 1,045 | 50 | 82 % | 51 % | 26 % | 7.1 % | 0.5 % | 0,27 | 65 % | 1,4 | 1,44 (93 %–107 %) | 41/14/3 | 103 | 50,0 · 85 % · 30,1 | đạt | 150 | Pulse Gun+Star Mortar 56%, Pulse Gun+Rail Gun 8% |
| fast | Cân bằng | 1,248 | 70 | 82 % | 63 % | 22 % | 11 % ↑ | 0 % | 0,09 | 63 % | 1,1 | 1,21 (93 %–100 %) | 38/12/1 | 116 | 69,9 · 97 % · 31,9 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| no-type | Cân bằng | 0,750 | 10 | 0 % ↓ | 0 % ↓ | 72 % ↑ | 0 % | 0 % | 0,00 | — | — | 0,00 (100 %–100 %) | 28/73/0 | 84 | — · — · 0,0 | — | 24 | Pulse Gun+Star Mortar 100% |
| type-only | Cân bằng | 1,000 | 35 | 86 % | 78 % ↑ | 16 % | 8.1 % | 0 % | 0,09 | 61 % | 1,1 | 1,31 (86 %–100 %) | 29/10/1 | 97 | 35,1 · 95 % · 29,0 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@good | Cân bằng | 1,000 | 35 | 91 % ↑ | 79 % ↑ | 15 % | 10 % ↑ | 0 % | 0,08 | 58 % | 1,0 | 1,39 (86 %–100 %) | 27/8/2 | 97 | 35,0 · 95 % · 28,0 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@poor | Cân bằng | 1,000 | 35 | 82 % | 36 % | 35 % ↑ | 2.1 % | 0 % | 0,38 | 77 % | 2,4 | 1,04 (93 %–107 %) | 59/13/1 | 103 | 35,0 · 95 % · 32,1 | đạt | 150 | Pulse Gun+Heat Beam 100% |
| standard (tắt nhịp) | Cân bằng | 1,000 | 35 | 92 % ↑ | 73 % ↑ | 18 % | 7.4 % | 0 % | 0,09 | 59 % | 1,1 | 0,00 (100 %–100 %) | 29/7/2 | 90 | 35,1 · 95 % · 29,2 | đạt | 150 | Pulse Gun+Star Mortar 56%, Pulse Gun+Rail Gun 8% |
| child | Thử thách | 0,750 | 15 | 0 % ↓ | 0 % ↓ | 56 % ↑ | 0.1 % | 0.1 % | 0,14 | 79 % | 3,5 | 1,29 (93 %–107 %) | 58/38/12 | 94 | 15,4 · 87 % · 16,0 | đạt | 69 | Pulse Gun+Heat Beam 100% |
| novice | Thử thách | 0,750 | 25 | 51 % | 5 % ↓ | 33 % | 2.5 % | 0 % | 0,34 | 70 % | 1,7 | 1,54 (86 %–107 %) | 54/20/8 | 89 | 25,2 · 92 % · 23,1 | đạt | 150 | Pulse Gun+Star Mortar 56%, Pulse Gun+Rail Gun 8% |
| steady | Thử thách | 0,790 | 25 | 73 % | 39 % | 29 % ↓ | 2.4 % | 0 % | 0,26 | 70 % | 1,5 | 1,48 (86 %–107 %) | 48/15/5 | 89 | 24,9 · 99 % · 25,1 | đạt | 150 | Pulse Gun+Star Mortar 56%, Pulse Gun+Rail Gun 8% |
| standard | Thử thách | 1,000 | 35 | 53 % | 8.5 % ↓ | 35 % | 4.4 % | 0 % | 0,33 | 68 % | 1,5 | 1,51 (86 %–107 %) | 60/20/5 | 107 | 34,9 · 95 % · 30,2 | đạt | 150 | Pulse Gun+Star Mortar 56%, Pulse Gun+Rail Gun 8% |
| skilled | Thử thách | 1,202 | 50 | 58 % | 16 % | 32 % | 12 % ↑ | 0.1 % | 0,37 | 66 % | 1,3 | 1,58 (86 %–100 %) | 64/21/2 | 125 | 49,8 · 96 % · 33,1 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| sloppy | Thử thách | 1,045 | 50 | 36 % ↓ | 0 % ↓ | 35 % | 5.9 % ↑ | 0.7 % | 0,18 | 68 % | 1,5 | 1,44 (86 %–107 %) | 59/24/5 | 116 | 49,9 · 85 % · 30,3 | đạt | 136 | Pulse Gun+Star Mortar 56%, Pulse Gun+Rail Gun 8% |
| fast | Thử thách | 1,248 | 70 | 44 % ↓ | 0 % ↓ | 35 % | 8.5 % ↑ | 0.1 % | 0,39 | 67 % | 1,3 | 1,53 (86 %–100 %) | 69/24/2 | 131 | 69,9 · 97 % · 33,1 | đạt | 144 | Pulse Gun+Star Mortar 100% |
| no-type | Thử thách | 0,750 | 10 | 0 % ↓ | 0 % ↓ | 71 % ↑ | 0 % | 0 % | 0,00 | — | — | 0,00 (100 %–100 %) | 29/72/0 | 88 | — · — · 0,0 | — | 22 | Pulse Gun+Star Mortar 100% |
| type-only | Thử thách | 1,000 | 35 | 67 % | 33 % | 28 % ↓ | 5.6 % ↑ | 0.1 % | 0,27 | 66 % | 1,3 | 1,52 (86 %–100 %) | 55/17/3 | 108 | 35,0 · 95 % · 29,8 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@good | Thử thách | 1,000 | 35 | 71 % | 35 % | 25 % ↓ | 7.8 % ↑ | 0 % | 0,27 | 62 % | 1,2 | 1,52 (86 %–100 %) | 49/16/3 | 108 | 35,1 · 95 % · 29,0 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@poor | Thử thách | 1,000 | 35 | 46 % ↓ | 0 % ↓ | 49 % | 1.3 % | 0.2 % | 0,49 | 78 % | 2,4 | 1,47 (93 %–107 %) | 82/19/1 | 115 | 35,0 · 95 % · 32,4 | đạt | 146 | Pulse Gun+Heat Beam 100% |
| standard (tắt nhịp) | Thử thách | 1,000 | 35 | 61 % | 33 % | 29 % ↓ | 4.9 % | 0 % | 0,09 | 66 % | 1,3 | 0,00 (100 %–100 %) | 48/14/3 | 100 | 34,8 · 95 % · 30,0 | đạt | 150 | Pulse Gun+Star Mortar 56%, Pulse Gun+Rail Gun 8% |

| # | Cổng | Kết quả | Số đo |
|---|---|---|---|
| B1 | Cùng vùng cuốn | TRƯỢT | ✓ novice: Thắng 87 %, Biên S 63 %, Áp lực P 23 %, Nhàn I 3.2 %, Ngộp O 0 % (trong dải); ✗ steady: Thắng 92 %, Biên S 69 %, Áp lực P 19 %, Nhàn I 3.5 %, Ngộp O 0 % (lệch: Thắng cao, Biên S cao); ✗ standard: Thắng 82 %, Biên S 66 %, Áp lực P 22 %, Nhàn I 6.5 %, Ngộp O 0 % (lệch: Biên S cao); ✗ skilled: Thắng 84 %, Biên S 69 %, Áp lực P 19 %, Nhàn I 15 %, Ngộp O 0 % (lệch: Biên S cao, Nhàn I cao); ✓ sloppy: Thắng 82 %, Biên S 51 %, Áp lực P 26 %, Nhàn I 7.1 %, Ngộp O 0.5 % (trong dải); ✗ fast: Thắng 82 %, Biên S 63 %, Áp lực P 22 %, Nhàn I 11 %, Ngộp O 0 % (lệch: Nhàn I cao) |
| B2 | Không quá dễ | ĐẠT | ✓ child: S 0 %, I 0.4 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ novice: S 63 %, I 3.2 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ steady: S 69 %, I 3.5 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ standard: S 66 %, I 6.5 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ skilled: S 69 %, I 15 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ sloppy: S 51 %, I 7.1 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ fast: S 63 %, I 11 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ no-type: S 0 %, I 0 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ type-only: S 78 %, I 8.1 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ standard@good: S 79 %, I 10 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ standard@poor: S 36 %, I 2.1 % (không đồng thời S ≥ 90 % và I ≥ 20 %) |
| B3 | Không quá khó | ĐẠT | ✓ novice · Cân bằng: thắng 87 % (≥ 70 %); ✓ child · Thư giãn: thắng 91 % (≥ 85 %) |
| B4 | Chuẩn thắng ẩu | ĐẠT | ✓ steady vs sloppy: S 69 % vs 51 % (S chậm chắc > S ẩu); ✓ standard vs sloppy: hạ quái 1.25 s vs 1.36 s (chuẩn nhanh hơn) |
| B5 | Gõ là sức chính | ĐẠT | ✓ no-type · Thư giãn: thắng 0 % (≤ 0 %); ✓ no-type · Cân bằng: thắng 0 % (≤ 0 %); ✓ no-type · Thử thách: thắng 0 % (≤ 0 %) |
| B6 | Chiến thuật có nghĩa | TRƯỢT | ✗ Cân bằng: thắng 91 % vs 82 % (Tốt hơn Kém ≥ 10 điểm %); ✓ Thử thách: thắng 71 % vs 46 % (Tốt hơn Kém ≥ 10 điểm %) |
| B7 | Bộ điều nhịp nhẹ tay | TRƯỢT | ✓ child · Thư giãn: 1.22 bậc/đợt, khoảng sinh 93 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ child · Cân bằng: 1.36 bậc/đợt, khoảng sinh 93 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ child · Thử thách: 1.29 bậc/đợt, khoảng sinh 93 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ novice · Thư giãn: 1.44 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ novice · Cân bằng: 1.47 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ novice · Thử thách: 1.54 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ steady · Thư giãn: 1.46 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ steady · Cân bằng: 1.47 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ steady · Thử thách: 1.48 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard · Thư giãn: 1.34 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard · Cân bằng: 1.32 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard · Thử thách: 1.51 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ skilled · Thư giãn: 1.53 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ skilled · Cân bằng: 1.35 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ skilled · Thử thách: 1.58 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ sloppy · Thư giãn: 1.31 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ sloppy · Cân bằng: 1.44 bậc/đợt, khoảng sinh 93 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ sloppy · Thử thách: 1.44 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ fast · Thư giãn: 1.36 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ fast · Cân bằng: 1.21 bậc/đợt, khoảng sinh 93 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ fast · Thử thách: 1.53 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type · Thư giãn: 0.85 bậc/đợt, khoảng sinh 100 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type · Cân bằng: 0.00 bậc/đợt, khoảng sinh 100 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type · Thử thách: 0.00 bậc/đợt, khoảng sinh 100 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ type-only · Thư giãn: 1.45 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ type-only · Cân bằng: 1.31 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ type-only · Thử thách: 1.52 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@good · Thư giãn: 1.53 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@good · Cân bằng: 1.39 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@good · Thử thách: 1.52 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@poor · Thư giãn: 0.47 bậc/đợt, khoảng sinh 93 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@poor · Cân bằng: 1.04 bậc/đợt, khoảng sinh 93 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@poor · Thử thách: 1.47 bậc/đợt, khoảng sinh 93 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✗ standard · tắt nhịp: Thắng 92 %, Biên S 73 %, Áp lực P 18 %, Nhàn I 7.4 %, Ngộp O 0 % (lệch: Thắng cao, Biên S cao) |
| B8 | Học không bị lấn | ĐẠT | ✓ child · Thư giãn: đạt (cổng học của game); ✓ child · Cân bằng: đạt (cổng học của game); ✓ child · Thử thách: đạt (cổng học của game); ✓ novice · Thư giãn: đạt (cổng học của game); ✓ novice · Cân bằng: đạt (cổng học của game); ✓ novice · Thử thách: đạt (cổng học của game); ✓ steady · Thư giãn: đạt (cổng học của game); ✓ steady · Cân bằng: đạt (cổng học của game); ✓ steady · Thử thách: đạt (cổng học của game); ✓ standard · Thư giãn: đạt (cổng học của game); ✓ standard · Cân bằng: đạt (cổng học của game); ✓ standard · Thử thách: đạt (cổng học của game); ✓ skilled · Thư giãn: đạt (cổng học của game); ✓ skilled · Cân bằng: đạt (cổng học của game); ✓ skilled · Thử thách: đạt (cổng học của game); ✓ sloppy · Thư giãn: đạt (cổng học của game); ✓ sloppy · Cân bằng: đạt (cổng học của game); ✓ sloppy · Thử thách: đạt (cổng học của game); ✓ fast · Thư giãn: đạt (cổng học của game); ✓ fast · Cân bằng: đạt (cổng học của game); ✓ fast · Thử thách: đạt (cổng học của game); ✓ type-only · Thư giãn: đạt (cổng học của game); ✓ type-only · Cân bằng: đạt (cổng học của game); ✓ type-only · Thử thách: đạt (cổng học của game); ✓ standard@good · Thư giãn: đạt (cổng học của game); ✓ standard@good · Cân bằng: đạt (cổng học của game); ✓ standard@good · Thử thách: đạt (cổng học của game); ✓ standard@poor · Thư giãn: đạt (cổng học của game); ✓ standard@poor · Cân bằng: đạt (cổng học của game); ✓ standard@poor · Thử thách: đạt (cổng học của game); ✓ standard · Thư giãn: đạt (cổng học của game); ✓ standard · Cân bằng: đạt (cổng học của game); ✓ standard · Thử thách: đạt (cổng học của game) |
| B9 | Khớp người thật | THIẾU SỐ | thiếu: buổi chơi thử của người thật |

G3c (bot Chuẩn, Cân bằng, mọi bộ 2 súng):

| Bộ | Thắng | Biên S | P | I |
|---|---|---|---|---|
| Heat Beam+Scatter Gun | 94 % | 39 % | 39 % | 5.4 % |
| Heat Beam+Rail Gun | 90 % | 41 % | 32 % | 1.4 % |
| Scatter Gun+Star Mortar | 89 % | 55 % | 29 % | 4.4 % |
| Scatter Gun+Rail Gun | 88 % | 66 % | 25 % | 1.7 % |
| Pulse Gun+Heat Beam | 86 % | 42 % | 33 % | 3.3 % |
| Pulse Gun+Star Mortar | 86 % | 78 % | 16 % | 8.1 % |
| Pulse Gun+Rail Gun | 84 % | 85 % | 14 % | 4.5 % |
| Heat Beam+Star Mortar | 79 % | 31 % | 37 % | 4 % |
| Rail Gun+Star Mortar | 75 % | 45 % | 24 % | 0 % |
| Pulse Gun+Scatter Gun | 65 % | 33 % | 39 % | 13 % |

↓ / ↑: dưới / trên dải đích của chế độ (thắng, S, P, I, O). Mất giáp: trung bình mỗi trận, rỉ ở vòng gần / quái chạm vạch / đạn lính.

## Cổng S1

| # | Kiểm | Kết quả |
|---|---|---|
| G3m | Bảng khắc chế khớp số đo ở seed 1–16 và seed 17–32 (16 seed mỗi ô; trong ±8 % quanh ngưỡng thì cả hai dấu đều khớp): khớp; ràng buộc §5.2: đạt | đạt |
| G5 | Học: không lặp từ, chữ đầu khác nhau, không ẩn chữ đầu, bot Mới ≥ 8 từ (3300 trận có gõ) | đạt |
| §7.6 | Hai báo trước cách nhau < 4 s: 0 lần | đạt |
| G8 | Chạy lại từ nhật ký phím ra cùng mã băm (2 trận, Node) | đạt |
| G3c | c1-s1: Heat Beam+Scatter Gun 94 %, Heat Beam+Rail Gun 90 %, Scatter Gun+Star Mortar 89 %, Scatter Gun+Rail Gun 88 %, Pulse Gun+Heat Beam 86 %, Pulse Gun+Star Mortar 86 %, Pulse Gun+Rail Gun 84 %, Heat Beam+Star Mortar 79 %, Rail Gun+Star Mortar 75 %, Pulse Gun+Scatter Gun 65 % · kém nhất ≥ 60 %, cách tốt nhất ≤ 30 điểm, tốt nhất ≤ 97 % | đạt |
| G2 (tạm) | Bộ đứng nhất theo ải: Heat Beam+Scatter Gun (chỉ in số ở R1) | — |
| B6 gộp | Cân bằng, Tốt − Kém gộp 1 ải: +9,0 điểm (từng ải +9,0; ≥ +10) | TRƯỢT |
| B6 gộp | Thử thách, Tốt − Kém gộp 1 ải: +25,0 điểm (từng ải +25,0; ≥ +10) | đạt |
| B1/B7 chạy lại | Ô lệch ≤ 3 điểm, chạy lại seed 201–300 trước khi tính là trượt: c1-s1 standard (s +0,5); c1-s1 fast (i +1,2) | — |

Bước sim không đo (thêm --time); quái trên sân tối đa 286. 3600 trận bot, 1000 trận G3c; cả lệnh 239 s.
