# Tuyến Cuối: báo cáo cân bằng (2 seed mỗi ô, seed 1–2)

Dải đích (BALANCE.md §3):

| Chế độ | Win | Safety S | Pressure P | Idle I | Overload O | Near misses N | Distance Q |
|---|---|---|---|---|---|---|---|
| Relaxed | ≥ 92% | ≥ 70% | 5–15% | ≤ 20% | ≤ 3% | ≤ 0.2 | ≤ 45% |
| Balanced | 75–90% | 35–65% | 15–35% | ≤ 10% | ≤ 8% | 0.3–1 | 50–70% |
| Challenge | 50–75% | 15–45% | 30–50% | ≤ 5% | ≤ 15% | 1–2 | 60–80% |

## c1-s1 · First Shift

| Bot | Chế độ | k | E từ | Win | Safety S | Pressure P | Idle I | Overload O | Near misses N | Distance Q | Hạ quái (s) | Bậc/đợt (khoảng sinh) | Mất giáp: rỉ/chạm/đạn | Quái tối đa | E · a đo · từ/phút | Học | Dài (s) | Súng chọn |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| child | Relaxed | 0,750 | 15 | 100% | 50% ↓ | 18% ↑ | 0.2% | 0% | 0,50 | 77% | 2,8 | 1,17 (93%–100%) | 22/21/8 | 89 | 15,0 · 88% · 17,2 | đạt | 150 | Pulse Gun+Heat Beam 100% |
| novice | Relaxed | 0,750 | 25 | 100% | 98% | 1.3% ↓ | 7.3% | 0% | 0,00 | 51% | 0,5 | 1,50 (86%–100%) | 2/0/0 | 70 | 25,3 · 90% · 20,6 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| steady | Relaxed | 0,790 | 25 | 100% | 99% | 1% ↓ | 6.8% | 0% | 0,00 | 49% | 0,4 | 1,67 (86%–100%) | 2/0/0 | 64 | 24,7 · 98% · 23,0 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard | Relaxed | 1,000 | 35 | 100% | 98% | 1.7% ↓ | 16% | 0% | 0,00 | 49% | 0,5 | 1,33 (93%–100%) | 3/0/0 | 83 | 34,7 · 94% · 26,2 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| skilled | Relaxed | 1,202 | 50 | 100% | 96% | 2.7% ↓ | 23% ↑ | 0% | 0,00 | 50% | 0,6 | 1,50 (86%–100%) | 4/0/0 | 101 | 50,6 · 95% · 26,8 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| sloppy | Relaxed | 1,045 | 50 | 100% | 98% | 1.7% ↓ | 22% ↑ | 0% | 0,00 | 48% | 0,4 | 1,50 (86%–100%) | 3/0/0 | 92 | 48,0 · 86% · 24,6 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| fast | Relaxed | 1,248 | 70 | 100% | 96% | 2.7% ↓ | 23% ↑ | 0% | 0,00 | 50% | 0,5 | 1,50 (86%–100%) | 4/0/0 | 123 | 69,7 · 96% · 26,2 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| no-type | Relaxed | 0,750 | 10 | 0% ↓ | 0% ↓ | 72% ↑ | 0% | 0% | 0,00 | — | — | 0,50 (100%–100%) | 17/95/0 | 67 | — · — · 0,0 | — | 32 | Pulse Gun+Star Mortar 100% |
| type-only | Relaxed | 1,000 | 35 | 100% | 98% | 1.7% ↓ | 16% | 0% | 0,00 | 49% | 0,5 | 1,33 (93%–100%) | 3/0/0 | 83 | 34,7 · 94% · 26,2 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@good | Relaxed | 1,000 | 35 | 100% | 97% | 2.1% ↓ | 23% ↑ | 0% | 0,00 | 48% | 0,5 | 1,50 (86%–100%) | 3/0/0 | 83 | 34,6 · 94% · 23,2 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@poor | Relaxed | 1,000 | 35 | 100% | 88% | 8.4% | 6.1% | 0% | 0,00 | 76% | 1,9 | 0,33 (93%–100%) | 12/0/0 | 109 | 34,2 · 94% · 30,6 | đạt | 150 | Pulse Gun+Heat Beam 100% |
| standard (tắt nhịp) | Relaxed | 1,000 | 35 | 100% | 98% | 1.7% ↓ | 16% | 0% | 0,00 | 50% | 0,5 | 0,00 (100%–100%) | 3/0/0 | 91 | 34,1 · 92% · 25,4 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| child | Balanced | 0,750 | 15 | 0% ↓ | 0% ↓ | 57% ↑ | 0% | 0% | 0,50 | 79% | 3,5 | 2,00 (100%–107%) | 62/44/5 | 93 | 13,3 · 87% · 15,7 | đạt | 125 | Pulse Gun+Heat Beam 100% |
| novice | Balanced | 0,750 | 25 | 100% ↑ | 60% | 14% ↓ | 2% | 0% | 0,00 | 63% | 1,1 | 1,50 (86%–100%) | 28/3/9 | 127 | 25,0 · 90% · 22,2 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| steady | Balanced | 0,790 | 25 | 100% ↑ | 80% ↑ | 12% ↓ | 3.6% | 0% | 0,00 | 60% | 0,9 | 1,50 (86%–100%) | 20/0/0 | 147 | 24,7 · 99% · 24,4 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard | Balanced | 1,000 | 35 | 100% ↑ | 37% | 23% | 8.6% | 0% | 0,50 | 65% | 1,3 | 1,67 (93%–100%) | 50/23/2 | 162 | 34,8 · 93% · 28,6 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| skilled | Balanced | 1,202 | 50 | 50% ↓ | 34% ↓ | 27% | 13% ↑ | 0.3% | 0,50 | 63% | 1,3 | 1,50 (93%–100%) | 49/21/6 | 230 | 50,6 · 94% · 30,3 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| sloppy | Balanced | 1,045 | 50 | 100% ↑ | 46% | 28% | 7.9% | 0% | 0,00 | 67% | 1,3 | 1,67 (93%–100%) | 53/0/2 | 181 | 51,9 · 86% · 30,2 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| fast | Balanced | 1,248 | 70 | 50% ↓ | 26% ↓ | 25% | 8.5% | 0% | 0,00 | 60% | 1,1 | 1,00 (93%–100%) | 45/29/2 | 191 | 69,4 · 96% · 32,2 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| no-type | Balanced | 0,750 | 10 | 0% ↓ | 0% ↓ | 71% ↑ | 0% | 0% | 0,00 | — | — | 0,00 (100%–100%) | 28/72/0 | 90 | — · — · 0,0 | — | 24 | Pulse Gun+Star Mortar 100% |
| type-only | Balanced | 1,000 | 35 | 100% ↑ | 37% | 23% | 8.6% | 0% | 0,50 | 65% | 1,3 | 1,67 (93%–100%) | 50/23/2 | 162 | 34,8 · 93% · 28,6 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@good | Balanced | 1,000 | 35 | 50% ↓ | 17% ↓ | 19% | 9.4% | 0% | 0,00 | 59% | 1,1 | 1,50 (93%–100%) | 40/36/8 | 163 | 34,9 · 94% · 28,2 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@poor | Balanced | 1,000 | 35 | 100% ↑ | 27% ↓ | 39% ↑ | 1.6% | 0% | 1,50 | 77% | 2,3 | 1,00 (100%–107%) | 73/21/0 | 175 | 35,3 · 94% · 32,4 | đạt | 150 | Pulse Gun+Heat Beam 100% |
| standard (tắt nhịp) | Balanced | 1,000 | 35 | 50% ↓ | 23% ↓ | 21% | 8% | 0% | 0,00 | 64% | 1,2 | 0,00 (100%–100%) | 40/33/5 | 177 | 35,3 · 92% · 27,4 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| child | Challenge | 0,750 | 15 | 0% ↓ | 0% ↓ | 65% ↑ | 0% | 0% | 0,50 | 81% | 3,4 | 2,00 (100%–107%) | 71/27/14 | 101 | 14,0 · 88% · 15,9 | đạt | 105 | Pulse Gun+Heat Beam 100% |
| novice | Challenge | 0,750 | 25 | 50% | 27% | 24% ↓ | 1.7% | 0% | 0,00 | 66% | 1,3 | 1,33 (93%–100%) | 47/23/5 | 150 | 24,3 · 91% · 22,2 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| steady | Challenge | 0,790 | 25 | 50% | 1% ↓ | 24% ↓ | 1.3% | 0% | 0,50 | 69% | 1,3 | 1,50 (93%–100%) | 56/29/15 | 157 | 24,9 · 99% · 24,8 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard | Challenge | 1,000 | 35 | 0% ↓ | 0% ↓ | 26% ↓ | 6.2% ↑ | 0% | 0,50 | 67% | 1,3 | 1,50 (93%–100%) | 59/50/3 | 186 | 34,8 · 93% · 28,5 | đạt | 149 | Pulse Gun+Star Mortar 100% |
| skilled | Challenge | 1,202 | 50 | 0% ↓ | 0% ↓ | 37% | 11% ↑ | 0.3% | 0,50 | 63% | 1,4 | 1,50 (93%–100%) | 74/35/3 | 232 | 51,2 · 95% · 32,9 | đạt | 133 | Pulse Gun+Star Mortar 100% |
| sloppy | Challenge | 1,045 | 50 | 50% | 14% ↓ | 33% | 8.2% ↑ | 0.1% | 1,00 | 70% | 1,6 | 1,67 (93%–100%) | 75/23/0 | 223 | 49,3 · 84% · 30,0 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| fast | Challenge | 1,248 | 70 | 0% ↓ | 0% ↓ | 34% | 9.3% ↑ | 0.3% | 0,00 | 63% | 1,3 | 1,50 (93%–100%) | 70/30/2 | 259 | 69,4 · 96% · 32,2 | đạt | 137 | Pulse Gun+Star Mortar 100% |
| no-type | Challenge | 0,750 | 10 | 0% ↓ | 0% ↓ | 70% ↑ | 0% | 0% | 0,00 | — | — | 0,00 (100%–100%) | 29/72/0 | 91 | — · — · 0,0 | — | 22 | Pulse Gun+Star Mortar 100% |
| type-only | Challenge | 1,000 | 35 | 0% ↓ | 0% ↓ | 26% ↓ | 6.2% ↑ | 0% | 0,50 | 67% | 1,3 | 1,50 (93%–100%) | 59/50/3 | 186 | 34,8 · 93% · 28,5 | đạt | 149 | Pulse Gun+Star Mortar 100% |
| standard@good | Challenge | 1,000 | 35 | 50% | 4% ↓ | 24% ↓ | 6.7% ↑ | 0% | 0,50 | 61% | 1,1 | 1,50 (93%–100%) | 55/35/8 | 175 | 35,0 · 94% · 28,6 | đạt | 150 | Pulse Gun+Star Mortar 100% |
| standard@poor | Challenge | 1,000 | 35 | 0% ↓ | 0% ↓ | 47% | 0.5% | 0% | 0,00 | 77% | 2,2 | 1,75 (93%–100%) | 73/27/0 | 196 | 35,1 · 95% · 32,7 | đạt | 125 | Pulse Gun+Heat Beam 100% |
| standard (tắt nhịp) | Challenge | 1,000 | 35 | 50% | 26% | 24% ↓ | 7.1% ↑ | 0% | 0,00 | 65% | 1,2 | 0,00 (100%–100%) | 51/23/2 | 180 | 34,8 · 93% · 28,3 | đạt | 150 | Pulse Gun+Star Mortar 100% |

| # | Gate | Result | Measurements |
|---|---|---|---|
| B1 | Shared flow band | FAIL | ✗ novice: Win 100%, Safety S 60%, Pressure P 14%, Idle I 2%, Overload O 0% (deviation: Win high, Pressure P low); ✗ steady: Win 100%, Safety S 80%, Pressure P 12%, Idle I 3.6%, Overload O 0% (deviation: Win high, Safety S high, Pressure P low); ✗ standard: Win 100%, Safety S 37%, Pressure P 23%, Idle I 8.6%, Overload O 0% (deviation: Win high); ✗ skilled: Win 50%, Safety S 34%, Pressure P 27%, Idle I 13%, Overload O 0.3% (deviation: Win low, Safety S low, Idle I high); ✗ sloppy: Win 100%, Safety S 46%, Pressure P 28%, Idle I 7.9%, Overload O 0% (deviation: Win high); ✗ fast: Win 50%, Safety S 26%, Pressure P 25%, Idle I 8.5%, Overload O 0% (deviation: Win low, Safety S low) |
| B2 | Not too easy | PASS | ✓ child: S 0%, I 0% (not both S ≥ 90% and I ≥ 20%); ✓ novice: S 60%, I 2% (not both S ≥ 90% and I ≥ 20%); ✓ steady: S 80%, I 3.6% (not both S ≥ 90% and I ≥ 20%); ✓ standard: S 37%, I 8.6% (not both S ≥ 90% and I ≥ 20%); ✓ skilled: S 34%, I 13% (not both S ≥ 90% and I ≥ 20%); ✓ sloppy: S 46%, I 7.9% (not both S ≥ 90% and I ≥ 20%); ✓ fast: S 26%, I 8.5% (not both S ≥ 90% and I ≥ 20%); ✓ no-type: S 0%, I 0% (not both S ≥ 90% and I ≥ 20%); ✓ type-only: S 37%, I 8.6% (not both S ≥ 90% and I ≥ 20%); ✓ standard@good: S 17%, I 9.4% (not both S ≥ 90% and I ≥ 20%); ✓ standard@poor: S 27%, I 1.6% (not both S ≥ 90% and I ≥ 20%) |
| B3 | Not too hard | PASS | ✓ novice · Balanced: win 100% (≥ 70%); ✓ child · Relax: win 100% (≥ 85%) |
| B4 | Accuracy beats speed | PASS | ✓ steady vs sloppy: S 80% vs 46% (S steady > S sloppy); ✓ standard vs sloppy: kill time 1.34 s vs 1.35 s (standard is faster) |
| B5 | Typing drives combat | PASS | ✓ no-type · Relax: win 0% (≤ 0%); ✓ no-type · Balanced: win 0% (≤ 0%); ✓ no-type · Challenge: win 0% (≤ 0%) |
| B6 | Tactics matter | FAIL | ✗ Balanced: win 50% vs 100% (good beats poor by ≥ 10 percentage points); ✓ Challenge: win 50% vs 0% (good beats poor by ≥ 10 percentage points) |
| B7 | Gentle pace director | FAIL | ✓ child · Relax: 1.17 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ child · Balanced: 2.00 steps/wave, spawn scale 100%–107% (≤ 3 steps/wave, within ±15%); ✓ child · Challenge: 2.00 steps/wave, spawn scale 100%–107% (≤ 3 steps/wave, within ±15%); ✓ novice · Relax: 1.50 steps/wave, spawn scale 86%–100% (≤ 3 steps/wave, within ±15%); ✓ novice · Balanced: 1.50 steps/wave, spawn scale 86%–100% (≤ 3 steps/wave, within ±15%); ✓ novice · Challenge: 1.33 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ steady · Relax: 1.67 steps/wave, spawn scale 86%–100% (≤ 3 steps/wave, within ±15%); ✓ steady · Balanced: 1.50 steps/wave, spawn scale 86%–100% (≤ 3 steps/wave, within ±15%); ✓ steady · Challenge: 1.50 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ standard · Relax: 1.33 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ standard · Balanced: 1.67 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ standard · Challenge: 1.50 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ skilled · Relax: 1.50 steps/wave, spawn scale 86%–100% (≤ 3 steps/wave, within ±15%); ✓ skilled · Balanced: 1.50 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ skilled · Challenge: 1.50 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ sloppy · Relax: 1.50 steps/wave, spawn scale 86%–100% (≤ 3 steps/wave, within ±15%); ✓ sloppy · Balanced: 1.67 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ sloppy · Challenge: 1.67 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ fast · Relax: 1.50 steps/wave, spawn scale 86%–100% (≤ 3 steps/wave, within ±15%); ✓ fast · Balanced: 1.00 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ fast · Challenge: 1.50 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ no-type · Relax: 0.50 steps/wave, spawn scale 100%–100% (≤ 3 steps/wave, within ±15%); ✓ no-type · Balanced: 0.00 steps/wave, spawn scale 100%–100% (≤ 3 steps/wave, within ±15%); ✓ no-type · Challenge: 0.00 steps/wave, spawn scale 100%–100% (≤ 3 steps/wave, within ±15%); ✓ type-only · Relax: 1.33 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ type-only · Balanced: 1.67 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ type-only · Challenge: 1.50 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ standard@good · Relax: 1.50 steps/wave, spawn scale 86%–100% (≤ 3 steps/wave, within ±15%); ✓ standard@good · Balanced: 1.50 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ standard@good · Challenge: 1.50 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ standard@poor · Relax: 0.33 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✓ standard@poor · Balanced: 1.00 steps/wave, spawn scale 100%–107% (≤ 3 steps/wave, within ±15%); ✓ standard@poor · Challenge: 1.75 steps/wave, spawn scale 93%–100% (≤ 3 steps/wave, within ±15%); ✗ standard · director off: Win 50%, Safety S 23%, Pressure P 21%, Idle I 8%, Overload O 0% (deviation: Win low, Safety S low) |
| B8 | Learning stays clear | PASS | ✓ child · Relax: pass (game learning gate); ✓ child · Balanced: pass (game learning gate); ✓ child · Challenge: pass (game learning gate); ✓ novice · Relax: pass (game learning gate); ✓ novice · Balanced: pass (game learning gate); ✓ novice · Challenge: pass (game learning gate); ✓ steady · Relax: pass (game learning gate); ✓ steady · Balanced: pass (game learning gate); ✓ steady · Challenge: pass (game learning gate); ✓ standard · Relax: pass (game learning gate); ✓ standard · Balanced: pass (game learning gate); ✓ standard · Challenge: pass (game learning gate); ✓ skilled · Relax: pass (game learning gate); ✓ skilled · Balanced: pass (game learning gate); ✓ skilled · Challenge: pass (game learning gate); ✓ sloppy · Relax: pass (game learning gate); ✓ sloppy · Balanced: pass (game learning gate); ✓ sloppy · Challenge: pass (game learning gate); ✓ fast · Relax: pass (game learning gate); ✓ fast · Balanced: pass (game learning gate); ✓ fast · Challenge: pass (game learning gate); ✓ type-only · Relax: pass (game learning gate); ✓ type-only · Balanced: pass (game learning gate); ✓ type-only · Challenge: pass (game learning gate); ✓ standard@good · Relax: pass (game learning gate); ✓ standard@good · Balanced: pass (game learning gate); ✓ standard@good · Challenge: pass (game learning gate); ✓ standard@poor · Relax: pass (game learning gate); ✓ standard@poor · Balanced: pass (game learning gate); ✓ standard@poor · Challenge: pass (game learning gate); ✓ standard · Relax: pass (game learning gate); ✓ standard · Balanced: pass (game learning gate); ✓ standard · Challenge: pass (game learning gate) |
| B9 | Matches human play | MISSING DATA | missing: human playtest |

G3c (bot Chuẩn, Cân bằng, mọi bộ 2 súng):

| Bộ | Thắng | Biên S | P | I |
|---|---|---|---|---|
| Pulse Gun+Heat Beam | 100% | 22% | 38% | 1.7% |
| Pulse Gun+Star Mortar | 100% | 37% | 23% | 8.6% |
| Heat Beam+Scatter Gun | 100% | 45% | 40% | 3.8% |
| Heat Beam+Rail Gun | 100% | 49% | 28% | 1.1% |
| Scatter Gun+Rail Gun | 100% | 49% | 32% | 1% |
| Scatter Gun+Star Mortar | 100% | 39% | 30% | 3.1% |
| Rail Gun+Star Mortar | 100% | 35% | 32% | 0% |
| Pulse Gun+Rail Gun | 50% | 41% | 14% | 5% |
| Pulse Gun+Scatter Gun | 0% | 0% | 41% | 8.5% |
| Heat Beam+Star Mortar | 0% | 0% | 39% | 1.7% |

↓ / ↑: dưới / trên dải đích của chế độ (thắng, S, P, I, O). Mất giáp: trung bình mỗi trận, rỉ ở vòng gần / quái chạm vạch / đạn lính.

## Cổng S1

| # | Kiểm | Kết quả |
|---|---|---|
| G3m | Bảng khắc chế khớp số đo ở seed 1–16 và seed 17–32 (16 seed mỗi ô; trong ±8 % quanh ngưỡng thì cả hai dấu đều khớp): khớp; ràng buộc §5.2: đạt | đạt |
| G5 | Học: không lặp từ, chữ đầu khác nhau, không ẩn chữ đầu, bot Mới ≥ 8 từ (66 trận có gõ) | đạt |
| §7.6 | Hai báo trước cách nhau < 4 s: 0 lần | đạt |
| G8 | Chạy lại từ nhật ký phím ra cùng mã băm (2 trận, Node) | đạt |
| G3c | c1-s1: Pulse Gun+Heat Beam 100%, Pulse Gun+Star Mortar 100%, Heat Beam+Scatter Gun 100%, Heat Beam+Rail Gun 100%, Scatter Gun+Rail Gun 100%, Scatter Gun+Star Mortar 100%, Rail Gun+Star Mortar 100%, Pulse Gun+Rail Gun 50%, Pulse Gun+Scatter Gun 0%, Heat Beam+Star Mortar 0% · kém nhất ≥ 60 %, cách tốt nhất ≤ 30 điểm, tốt nhất ≤ 97 % | TRƯỢT |
| G2 (tạm) | Bộ đứng nhất theo ải: Pulse Gun+Heat Beam (chỉ in số ở R1) | — |
| B6 gộp | Balanced, Tốt − Kém gộp 1 ải: −50,0 điểm (từng ải −50,0; ≥ +10) | TRƯỢT |
| B6 gộp | Challenge, Tốt − Kém gộp 1 ải: +50,0 điểm (từng ải +50,0; ≥ +10) | đạt |
| B1/B7 chạy lại | Ô lệch ≤ 3 điểm, chạy lại seed 3–4 trước khi tính là trượt: không có | — |

Bước sim không đo (thêm --time); quái trên sân tối đa 259. 72 trận bot, 20 trận G3c; cả lệnh 6 s.
