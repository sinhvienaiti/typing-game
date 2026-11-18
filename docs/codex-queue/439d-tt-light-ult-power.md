# Phiếu 439d — Quang: tia mềm, bùng nổ mạnh, chiêu có lực (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
Bản 439c (`typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-c.jpg`). Owner 17/11: "dù đã tốt hơn nhưng vẫn thiếu về chất lượng bùng nổ, kỹ năng cũng chưa gọi là đẹp, nhìn cảm giác khá yếu, các tia cũng đang bị quá cứng, nhìn không được như ảnh demo". Ảnh demo = phân cảnh `games/immortality-cultivation/art-src/concept/ult-storyboards/light-storyboard.v1-try1.png`. Quyền, server 3148, cách đo và probe giữ như `docs/codex-queue/439c-tt-light-ult-center-beam.md` (và 439b, 439). Giữ tia cuối ở giữa trục (owner đã chọn). Chỉ sửa `src/lab/light-ult-*`.

## Việc (worktree `games/.wt-ic-lab-all`)
1. **Tia mềm, không cứng:** mỗi tia thuôn hai đầu (gốc mảnh sáng → giữa rộng → đầu tan mờ dần 25–35 % chiều dài cuối), bề rộng dao động nhẹ theo thời gian, nhiễu chảy rõ hơn, cạnh quầng mờ theo hàm mũ (không cạnh cứng); tia vươn ra (grow) 0,15–0,25 s thay vì bật ngay, rung sáng nhẹ. Tia hội tụ: thuôn từ thấu kính, thân có xoắn sáng/nhiễu, đầu không phải đoạn cụt.
2. **Bùng nổ đủ lực ở điểm trúng tia cuối (điểm nhấn duy nhất):**
   - lóe 2 khung ≤ 6 % trắng toàn khung; `light-big-burst` cỡ 4–6 m;
   - tia lửa lăng kính bắn tỏa 30–60 hạt có vệt;
   - các tia sáng tỏa (starburst) ngắn quanh điểm trúng, mềm;
   - ánh sáng điểm (point light hoặc decal sáng hình nêm/đốm mềm, **không vòng hay đĩa tròn**) rọi quái và đất xung quanh 0,3 s;
   - quái gần điểm trúng giật lùi rõ, lóe viền vàng;
   - import (không sửa) `UltCameraPunch` từ `ult-camera-punch.ts` (rung nhẹ + đẩy camera); lab chưa có hook hit-stop nên bỏ dừng hình; âm `tt-sfx-ult-light` khớp khung.
3. **Cả chiêu có lực hơn:** lúc tụ lực thấu kính lóe và có hạt hút vào; khi quạt bắn, quái trong quạt lóe viền vàng; ánh sáng ấm hắt lên đất theo hình nêm mạnh hơn (kênh ≤ 0,9).
4. Bụi đốm dư âm sáng rõ hơn trên nền lab ở camera chơi.

## Đo
Giữ toàn bộ số đo của 439c; thêm: độ phủ nêm ở 0,9 s ≥ 25 %; ở khung bùng nổ (đo thời điểm, in ra): độ phủ sáng trong hình tròn màn hình bán kính 120 px quanh điểm trúng ≥ 45 %, vùng trắng toàn khung ≤ 6 %; độ thuôn: probe cắt ngang tia giữa ở 20 %, 50 %, 85 % chiều dài, bề rộng quầng ở 85 % ≤ 0,6 lần ở 50 %.
Vòng lặp sửa → chụp → mở ảnh → so phân cảnh từng khung và nhận xét owner → sửa, tối đa 5 vòng.

## Nghiệm thu
Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms. Lưu `light-ult-codex-d.jpg/.mp4` mới (giữ file cũ), dòng `ABOUT.md`. Xoá khung thô. Không commit.

## Giao nộp
`docs/codex-queue/439d-report.md`.
