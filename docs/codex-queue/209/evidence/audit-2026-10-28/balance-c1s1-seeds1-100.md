# Tuyến Cuối: báo cáo cân bằng (100 seed mỗi ô, seed 1–100)

Dải đích (BALANCE.md §3):

| Chế độ | Thắng | Biên S | Áp lực P | Nhàn I | Ngộp O | Gần thua N | Quãng Q |
|---|---|---|---|---|---|---|---|
| Thư giãn | ≥ 92 % | ≥ 70 % | 5–15 % | ≤ 20 % | ≤ 3 % | ≤ 0.2 | ≤ 45 % |
| Cân bằng | 75–90 % | 35–65 % | 15–35 % | ≤ 10 % | ≤ 8 % | 0.3–1 | 50–70 % |
| Thử thách | 50–75 % | 15–45 % | 30–50 % | ≤ 5 % | ≤ 15 % | 1–2 | 60–80 % |

## c1-s1 · Ca trực đầu

| Bot | Chế độ | k | E từ | Thắng | Biên S | Áp lực P | Nhàn I | Ngộp O | Gần thua N | Quãng Q | Hạ quái (s) | Bậc/đợt (khoảng sinh) | Mất giáp: rỉ/chạm/đạn | Quái tối đa | E · a đo · từ/phút | Học | Dài (s) | Súng chọn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| child | Thư giãn | 0,750 | 15 | 90 % ↓ | 67 % ↓ | 21 % ↑ | 1.6 % | 0 % | 0,15 | 77 % | 2,9 | 1,28 (93 %–107 %) | 23/16/7 | 58 | 15,0 · 88 % · 16,2 | đạt | 150 | Pulse Gun+Heat Beam 100% |
| novice | Thư giãn | 0,750 | 25 | 100 % | 99 % | 2.2 % ↓ | 9.9 % | 0 % | 0,00 | 48 % | 0,6 | 1,44 (86 %–100 %) | 3/0/0 | 43 | 25,2 · 92 % · 21,0 | đạt | 150 | Pulse Gun+Star Mortar 62%, Heat Beam+Scatter Gun 7% |
| steady | Thư giãn | 0,790 | 25 | 100 % | 99 % | 1.7 % ↓ | 11 % | 0 % | 0,00 | 47 % | 0,6 | 1,42 (86 %–100 %) | 2/0/0 | 44 | 24,9 · 99 % · 22,5 | đạt | 150 | Pulse Gun+Star Mortar 62%, Heat Beam+Scatter Gun 7% |
| standard | Thư giãn | 1,000 | 35 | 100 % | 98 % | 2.5 % ↓ | 16 % | 0 % | 0,00 | 48 % | 0,6 | 1,35 (86 %–100 %) | 4/0/0 | 52 | 35,0 · 95 % · 26,2 | đạt | 150 | Pulse Gun+Star Mortar 62%, Heat Beam+Scatter Gun 7% |
| skilled | Thư giãn | 1,202 | 50 | 100 % | 97 % | 2.2 % ↓ | 30 % ↑ | 0 % | 0,00 | 50 % | 0,5 | 1,54 (86 %–100 %) | 3/0/0 | 62 | 49,9 · 96 % · 25,6 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| sloppy | Thư giãn | 1,045 | 50 | 100 % | 97 % | 3.3 % ↓ | 17 % | 0.4 % | 0,00 | 49 % | 0,7 | 1,34 (86 %–107 %) | 4/0/0 | 56 | 50,2 · 85 % · 26,5 | đạt | 150 | Pulse Gun+Star Mortar 62%, Heat Beam+Scatter Gun 7% |
| fast | Thư giãn | 1,248 | 70 | 100 % | 97 % | 2.4 % ↓ | 25 % ↑ | 0 % | 0,00 | 50 % | 0,5 | 1,35 (86 %–100 %) | 4/0/0 | 64 | 69,8 · 97 % · 26,1 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| no-type | Thư giãn | 0,750 | 10 | 0 % ↓ | 0 % ↓ | 73 % ↑ | 0 % | 0 % | 0,01 | — | — | 0,71 (100 %–100 %) | 18/97/0 | 62 | — · — · 0,0 | — | 33 | Pulse Gun+Star Mortar 100% |
| type-only | Thư giãn | 1,000 | 35 | 100 % | 98 % | 1.4 % ↓ | 18 % | 0 % | 0,00 | 48 % | 0,4 | 1,46 (86 %–100 %) | 2/0/0 | 52 | 35,0 · 95 % · 25,2 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@good | Thư giãn | 1,000 | 35 | 100 % | 98 % | 1.2 % ↓ | 23 % ↑ | 0 % | 0,00 | 47 % | 0,4 | 1,53 (86 %–100 %) | 2/0/0 | 50 | 35,0 · 95 % · 23,4 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@poor | Thư giãn | 1,000 | 35 | 100 % | 91 % | 6.6 % | 7.7 % | 0 % | 0,00 | 76 % | 1,7 | 0,42 (93 %–107 %) | 10/0/0 | 63 | 35,1 · 95 % · 30,1 | đạt | 150 | Pulse Gun+Heat Beam 100% |
| standard (tắt nhịp) | Thư giãn | 1,000 | 35 | 100 % | 99 % | 1.9 % ↓ | 17 % | 0 % | 0,00 | 47 % | 0,6 | 0,00 (100 %–100 %) | 3/0/0 | 49 | 35,0 · 95 % · 25,8 | đạt | 150 | Pulse Gun+Star Mortar 62%, Heat Beam+Scatter Gun 7% |
| child | Cân bằng | 0,750 | 15 | 1 % ↓ | 0 % ↓ | 52 % ↑ | 0.4 % | 0 % | 0,19 | 79 % | 3,6 | 1,45 (93 %–107 %) | 62/36/12 | 84 | 15,0 · 88 % · 16,1 | đạt | 90 | Pulse Gun+Heat Beam 100% |
| novice | Cân bằng | 0,750 | 25 | 86 % | 65 % | 22 % | 2.7 % | 0 % | 0,15 | 66 % | 1,4 | 1,44 (86 %–114 %) | 34/9/5 | 78 | 25,1 · 92 % · 22,7 | đạt | 150 | Pulse Gun+Star Mortar 62%, Heat Beam+Scatter Gun 7% |
| steady | Cân bằng | 0,790 | 25 | 96 % ↑ | 76 % ↑ | 18 % | 3.3 % | 0 % | 0,09 | 62 % | 1,2 | 1,46 (86 %–107 %) | 27/4/3 | 77 | 24,9 · 99 % · 24,7 | đạt | 150 | Pulse Gun+Star Mortar 62%, Heat Beam+Scatter Gun 7% |
| standard | Cân bằng | 1,000 | 35 | 93 % ↑ | 69 % ↑ | 22 % | 6 % | 0 % | 0,16 | 63 % | 1,2 | 1,30 (86 %–114 %) | 34/8/2 | 95 | 34,9 · 95 % · 29,6 | đạt | 150 | Pulse Gun+Star Mortar 62%, Heat Beam+Scatter Gun 7% |
| skilled | Cân bằng | 1,202 | 50 | 92 % ↑ | 71 % ↑ | 20 % | 15 % ↑ | 0 % | 0,09 | 62 % | 1,0 | 1,40 (86 %–100 %) | 34/5/1 | 110 | 50,0 · 96 % · 31,7 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| sloppy | Cân bằng | 1,045 | 50 | 86 % | 60 % | 24 % | 6.9 % | 0.6 % | 0,20 | 65 % | 1,3 | 1,34 (86 %–107 %) | 39/10/3 | 100 | 50,1 · 85 % · 30,2 | đạt | 150 | Pulse Gun+Star Mortar 62%, Heat Beam+Scatter Gun 7% |
| fast | Cân bằng | 1,248 | 70 | 92 % ↑ | 68 % ↑ | 22 % | 11 % ↑ | 0 % | 0,11 | 62 % | 1,1 | 1,21 (93 %–100 %) | 38/6/1 | 114 | 69,9 · 97 % · 32,1 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| no-type | Cân bằng | 0,750 | 10 | 0 % ↓ | 0 % ↓ | 72 % ↑ | 0 % | 0 % | 0,00 | — | — | 0,00 (100 %–100 %) | 28/73/0 | 85 | — · — · 0,0 | — | 24 | Pulse Gun+Star Mortar 100% |
| type-only | Cân bằng | 1,000 | 35 | 95 % ↑ | 76 % ↑ | 17 % | 7.5 % | 0 % | 0,12 | 61 % | 1,0 | 1,27 (86 %–100 %) | 29/5/1 | 95 | 34,9 · 95 % · 29,0 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@good | Cân bằng | 1,000 | 35 | 96 % ↑ | 80 % ↑ | 15 % ↓ | 10 % ↑ | 0 % | 0,04 | 57 % | 0,9 | 1,35 (86 %–100 %) | 26/4/1 | 96 | 35,1 · 95 % · 28,0 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@poor | Cân bằng | 1,000 | 35 | 90 % | 44 % | 35 % | 1.9 % | 0 % | 0,32 | 77 % | 2,3 | 1,04 (93 %–107 %) | 57/8/0 | 100 | 35,0 · 95 % · 32,1 | đạt | 150 | Pulse Gun+Heat Beam 100% |
| standard (tắt nhịp) | Cân bằng | 1,000 | 35 | 90 % | 78 % ↑ | 18 % | 6.9 % | 0 % | 0,06 | 60 % | 1,1 | 0,00 (100 %–100 %) | 28/6/2 | 88 | 34,9 · 95 % · 29,3 | đạt | 150 | Pulse Gun+Star Mortar 62%, Heat Beam+Scatter Gun 7% |
| child | Thử thách | 0,750 | 15 | 0 % ↓ | 0 % ↓ | 57 % ↑ | 0.2 % | 0.1 % | 0,17 | 79 % | 3,6 | 1,42 (93 %–107 %) | 61/37/12 | 93 | 15,1 · 88 % · 16,1 | đạt | 69 | Pulse Gun+Heat Beam 100% |
| novice | Thử thách | 0,750 | 25 | 59 % | 16 % | 34 % | 2.1 % | 0 % | 0,34 | 71 % | 1,7 | 1,57 (86 %–107 %) | 56/17/8 | 86 | 25,0 · 92 % · 23,0 | đạt | 150 | Pulse Gun+Star Mortar 62%, Heat Beam+Scatter Gun 7% |
| steady | Thử thách | 0,790 | 25 | 75 % | 34 % | 30 % ↓ | 2.1 % | 0 % | 0,32 | 70 % | 1,5 | 1,54 (86 %–107 %) | 49/13/5 | 88 | 24,8 · 99 % · 25,0 | đạt | 150 | Pulse Gun+Star Mortar 62%, Heat Beam+Scatter Gun 7% |
| standard | Thử thách | 1,000 | 35 | 65 % | 26 % | 34 % | 4.1 % | 0 % | 0,38 | 69 % | 1,5 | 1,53 (86 %–107 %) | 59/17/4 | 106 | 35,0 · 95 % · 30,3 | đạt | 150 | Pulse Gun+Star Mortar 62%, Heat Beam+Scatter Gun 7% |
| skilled | Thử thách | 1,202 | 50 | 57 % | 20 % | 32 % | 11 % ↑ | 0 % | 0,28 | 66 % | 1,3 | 1,61 (86 %–100 %) | 65/17/2 | 124 | 49,8 · 96 % · 33,2 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| sloppy | Thử thách | 1,045 | 50 | 49 % ↓ | 0 % ↓ | 36 % | 5.3 % ↑ | 0.7 % | 0,33 | 69 % | 1,6 | 1,50 (86 %–107 %) | 62/19/5 | 112 | 49,8 · 85 % · 30,4 | đạt | 146 | Pulse Gun+Star Mortar 62%, Heat Beam+Scatter Gun 7% |
| fast | Thử thách | 1,248 | 70 | 36 % ↓ | 0 % ↓ | 36 % | 8.6 % ↑ | 0 % | 0,36 | 67 % | 1,4 | 1,54 (93 %–100 %) | 73/22/2 | 131 | 69,8 · 97 % · 33,1 | đạt | 144 | Pulse Gun+Star Mortar 100% |
| no-type | Thử thách | 0,750 | 10 | 0 % ↓ | 0 % ↓ | 70 % ↑ | 0 % | 0 % | 0,00 | — | — | 0,00 (100 %–100 %) | 29/72/0 | 89 | — · — · 0,0 | — | 22 | Pulse Gun+Star Mortar 100% |
| type-only | Thử thách | 1,000 | 35 | 69 % | 35 % | 28 % ↓ | 5.6 % ↑ | 0 % | 0,30 | 67 % | 1,3 | 1,54 (86 %–100 %) | 54/14/3 | 106 | 34,9 · 95 % · 29,7 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@good | Thử thách | 1,000 | 35 | 78 % ↑ | 41 % | 26 % ↓ | 7.5 % ↑ | 0 % | 0,32 | 63 % | 1,2 | 1,56 (86 %–100 %) | 50/13/3 | 105 | 35,0 · 95 % · 28,9 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@poor | Thử thách | 1,000 | 35 | 38 % ↓ | 0 % ↓ | 52 % ↑ | 1.2 % | 0.1 % | 0,59 | 78 % | 2,5 | 1,52 (93 %–107 %) | 87/16/1 | 113 | 35,1 · 95 % · 32,2 | đạt | 134 | Pulse Gun+Heat Beam 100% |
| standard (tắt nhịp) | Thử thách | 1,000 | 35 | 73 % | 47 % ↑ | 28 % ↓ | 4.7 % | 0 % | 0,12 | 66 % | 1,3 | 0,00 (100 %–100 %) | 46/11/3 | 97 | 34,9 · 95 % · 30,1 | đạt | 150 | Pulse Gun+Star Mortar 62%, Heat Beam+Scatter Gun 7% |

| # | Cổng | Kết quả | Số đo |
|---|---|---|---|
| B1 | Cùng vùng cuốn | TRƯỢT | ✓ novice: Thắng 86 %, Biên S 65 %, Áp lực P 22 %, Nhàn I 2.7 %, Ngộp O 0 % (trong dải); ✗ steady: Thắng 96 %, Biên S 76 %, Áp lực P 18 %, Nhàn I 3.3 %, Ngộp O 0 % (lệch: Thắng cao, Biên S cao); ✗ standard: Thắng 93 %, Biên S 69 %, Áp lực P 22 %, Nhàn I 6 %, Ngộp O 0 % (lệch: Thắng cao, Biên S cao); ✗ skilled: Thắng 92 %, Biên S 71 %, Áp lực P 20 %, Nhàn I 15 %, Ngộp O 0 % (lệch: Thắng cao, Biên S cao, Nhàn I cao); ✓ sloppy: Thắng 86 %, Biên S 60 %, Áp lực P 24 %, Nhàn I 6.9 %, Ngộp O 0.6 % (trong dải); ✗ fast: Thắng 92 %, Biên S 68 %, Áp lực P 22 %, Nhàn I 11 %, Ngộp O 0 % (lệch: Thắng cao, Biên S cao, Nhàn I cao) |
| B2 | Không quá dễ | ĐẠT | ✓ child: S 0 %, I 0.4 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ novice: S 65 %, I 2.7 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ steady: S 76 %, I 3.3 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ standard: S 69 %, I 6 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ skilled: S 71 %, I 15 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ sloppy: S 60 %, I 6.9 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ fast: S 68 %, I 11 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ no-type: S 0 %, I 0 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ type-only: S 76 %, I 7.5 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ standard@good: S 80 %, I 10 % (không đồng thời S ≥ 90 % và I ≥ 20 %); ✓ standard@poor: S 44 %, I 1.9 % (không đồng thời S ≥ 90 % và I ≥ 20 %) |
| B3 | Không quá khó | ĐẠT | ✓ novice · Cân bằng: thắng 86 % (≥ 70 %); ✓ child · Thư giãn: thắng 90 % (≥ 85 %) |
| B4 | Chuẩn thắng ẩu | ĐẠT | ✓ steady vs sloppy: S 76 % vs 60 % (S chậm chắc > S ẩu); ✓ standard vs sloppy: hạ quái 1.22 s vs 1.29 s (chuẩn nhanh hơn) |
| B5 | Gõ là sức chính | ĐẠT | ✓ no-type · Thư giãn: thắng 0 % (≤ 0 %); ✓ no-type · Cân bằng: thắng 0 % (≤ 0 %); ✓ no-type · Thử thách: thắng 0 % (≤ 0 %) |
| B6 | Chiến thuật có nghĩa | TRƯỢT | ✗ Cân bằng: thắng 96 % vs 90 % (Tốt hơn Kém ≥ 10 điểm %); ✓ Thử thách: thắng 78 % vs 38 % (Tốt hơn Kém ≥ 10 điểm %) |
| B7 | Bộ điều nhịp nhẹ tay | TRƯỢT | ✓ child · Thư giãn: 1.28 bậc/đợt, khoảng sinh 93 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ child · Cân bằng: 1.45 bậc/đợt, khoảng sinh 93 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ child · Thử thách: 1.42 bậc/đợt, khoảng sinh 93 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ novice · Thư giãn: 1.44 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ novice · Cân bằng: 1.44 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ novice · Thử thách: 1.57 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ steady · Thư giãn: 1.42 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ steady · Cân bằng: 1.46 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ steady · Thử thách: 1.54 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard · Thư giãn: 1.35 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard · Cân bằng: 1.30 bậc/đợt, khoảng sinh 86 %–114 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard · Thử thách: 1.53 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ skilled · Thư giãn: 1.54 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ skilled · Cân bằng: 1.40 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ skilled · Thử thách: 1.61 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ sloppy · Thư giãn: 1.34 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ sloppy · Cân bằng: 1.34 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ sloppy · Thử thách: 1.50 bậc/đợt, khoảng sinh 86 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ fast · Thư giãn: 1.35 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ fast · Cân bằng: 1.21 bậc/đợt, khoảng sinh 93 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ fast · Thử thách: 1.54 bậc/đợt, khoảng sinh 93 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type · Thư giãn: 0.71 bậc/đợt, khoảng sinh 100 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type · Cân bằng: 0.00 bậc/đợt, khoảng sinh 100 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ no-type · Thử thách: 0.00 bậc/đợt, khoảng sinh 100 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ type-only · Thư giãn: 1.46 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ type-only · Cân bằng: 1.27 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ type-only · Thử thách: 1.54 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@good · Thư giãn: 1.53 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@good · Cân bằng: 1.35 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@good · Thử thách: 1.56 bậc/đợt, khoảng sinh 86 %–100 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@poor · Thư giãn: 0.42 bậc/đợt, khoảng sinh 93 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@poor · Cân bằng: 1.04 bậc/đợt, khoảng sinh 93 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✓ standard@poor · Thử thách: 1.52 bậc/đợt, khoảng sinh 93 %–107 % (≤ 3 bậc/đợt, trong ±15 %); ✗ standard · tắt nhịp: Thắng 90 %, Biên S 78 %, Áp lực P 18 %, Nhàn I 6.9 %, Ngộp O 0 % (lệch: Biên S cao) |
| B8 | Học không bị lấn | ĐẠT | ✓ child · Thư giãn: đạt (cổng học của game); ✓ child · Cân bằng: đạt (cổng học của game); ✓ child · Thử thách: đạt (cổng học của game); ✓ novice · Thư giãn: đạt (cổng học của game); ✓ novice · Cân bằng: đạt (cổng học của game); ✓ novice · Thử thách: đạt (cổng học của game); ✓ steady · Thư giãn: đạt (cổng học của game); ✓ steady · Cân bằng: đạt (cổng học của game); ✓ steady · Thử thách: đạt (cổng học của game); ✓ standard · Thư giãn: đạt (cổng học của game); ✓ standard · Cân bằng: đạt (cổng học của game); ✓ standard · Thử thách: đạt (cổng học của game); ✓ skilled · Thư giãn: đạt (cổng học của game); ✓ skilled · Cân bằng: đạt (cổng học của game); ✓ skilled · Thử thách: đạt (cổng học của game); ✓ sloppy · Thư giãn: đạt (cổng học của game); ✓ sloppy · Cân bằng: đạt (cổng học của game); ✓ sloppy · Thử thách: đạt (cổng học của game); ✓ fast · Thư giãn: đạt (cổng học của game); ✓ fast · Cân bằng: đạt (cổng học của game); ✓ fast · Thử thách: đạt (cổng học của game); ✓ type-only · Thư giãn: đạt (cổng học của game); ✓ type-only · Cân bằng: đạt (cổng học của game); ✓ type-only · Thử thách: đạt (cổng học của game); ✓ standard@good · Thư giãn: đạt (cổng học của game); ✓ standard@good · Cân bằng: đạt (cổng học của game); ✓ standard@good · Thử thách: đạt (cổng học của game); ✓ standard@poor · Thư giãn: đạt (cổng học của game); ✓ standard@poor · Cân bằng: đạt (cổng học của game); ✓ standard@poor · Thử thách: đạt (cổng học của game); ✓ standard · Thư giãn: đạt (cổng học của game); ✓ standard · Cân bằng: đạt (cổng học của game); ✓ standard · Thử thách: đạt (cổng học của game) |
| B9 | Khớp người thật | THIẾU SỐ | thiếu: buổi chơi thử của người thật |

G3c (bot Chuẩn, Cân bằng, mọi bộ 2 súng):

| Bộ | Thắng | Biên S | P | I |
|---|---|---|---|---|
| Pulse Gun+Star Mortar | 95 % | 76 % | 17 % | 7.5 % |
| Heat Beam+Scatter Gun | 95 % | 38 % | 40 % | 5 % |
| Scatter Gun+Rail Gun | 95 % | 67 % | 25 % | 1.5 % |
| Pulse Gun+Heat Beam | 93 % | 45 % | 33 % | 2.9 % |
| Scatter Gun+Star Mortar | 93 % | 57 % | 29 % | 4.2 % |
| Heat Beam+Rail Gun | 91 % | 44 % | 31 % | 1.2 % |
| Pulse Gun+Rail Gun | 89 % | 86 % | 13 % | 4.5 % |
| Rail Gun+Star Mortar | 82 % | 45 % | 27 % | 0 % |
| Heat Beam+Star Mortar | 76 % | 32 % | 36 % | 3.9 % |
| Pulse Gun+Scatter Gun | 72 % | 32 % | 40 % | 12 % |

↓ / ↑: dưới / trên dải đích của chế độ (thắng, S, P, I, O). Mất giáp: trung bình mỗi trận, rỉ ở vòng gần / quái chạm vạch / đạn lính.

## Cổng S1

| # | Kiểm | Kết quả |
|---|---|---|
| G3m | Bảng khắc chế khớp số đo ở seed 1–16 và seed 17–32 (16 seed mỗi ô; trong ±8 % quanh ngưỡng thì cả hai dấu đều khớp): khớp; ràng buộc §5.2: đạt | đạt |
| G5 | Học: không lặp từ, chữ đầu khác nhau, không ẩn chữ đầu, bot Mới ≥ 8 từ (3300 trận có gõ) | đạt |
| §7.6 | Hai báo trước cách nhau < 4 s: 0 lần | đạt |
| G8 | Chạy lại từ nhật ký phím ra cùng mã băm (2 trận, Node) | đạt |
| G3c | c1-s1: Pulse Gun+Star Mortar 95 %, Heat Beam+Scatter Gun 95 %, Scatter Gun+Rail Gun 95 %, Pulse Gun+Heat Beam 93 %, Scatter Gun+Star Mortar 93 %, Heat Beam+Rail Gun 91 %, Pulse Gun+Rail Gun 89 %, Rail Gun+Star Mortar 82 %, Heat Beam+Star Mortar 76 %, Pulse Gun+Scatter Gun 72 % · kém nhất ≥ 60 %, cách tốt nhất ≤ 30 điểm, tốt nhất ≤ 97 % | đạt |
| G2 (tạm) | Bộ đứng nhất theo ải: Pulse Gun+Star Mortar (chỉ in số ở R1) | — |
| B6 gộp | Cân bằng, Tốt − Kém gộp 1 ải: +6,0 điểm (từng ải +6,0; ≥ +10) | TRƯỢT |
| B6 gộp | Thử thách, Tốt − Kém gộp 1 ải: +40,0 điểm (từng ải +40,0; ≥ +10) | đạt |
| B1/B7 chạy lại | Ô lệch ≤ 3 điểm, chạy lại seed 101–200 trước khi tính là trượt: c1-s1 fast (win +2,0, s +2,5, i +0,9) | — |

Bước sim không đo (thêm --time); quái trên sân tối đa 283. 3600 trận bot, 1000 trận G3c; cả lệnh 204 s.
