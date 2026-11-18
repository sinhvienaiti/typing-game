# Phiếu 434: Tuyệt kỹ Lôi — sét nhảy dây chuyền rồi sét lớn từ mây (bản lab đầu)


Phản biện: PASS (Sonnet, 17/11)
## Bối cảnh
Thiết kế: `docs/games/tu-tien/ULT_CHOREOGRAPHY.md` dòng Lôi. Phân cảnh owner đã xem 17/11: nửa phải `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`. Owner 17/11 chê kiểu "trồi lên từ mặt đất rồi vòng tròn lại". Nhịp camera dùng chung đã có: `games/.wt-ic-lab-all/src/lab/ult-camera-punch.ts` (phiếu 433c).

## Việc (worktree `games/.wt-ic-lab-all`, file mới `src/lab/thunder-ult-chain.ts`, nối vào chỗ tung tuyệt kỹ Lôi hiện có trong lab — mục Lôi là `ult-thunder-nine-heavens-v2` trong `showcase.ts` (phím 8), nối qua `skills-main.ts` hoặc `clip-skills.ts`; giữ bản cũ bật được bằng `?thunderUlt=old`)
1. **Tụ lực (0–0,6 s):** mây sét tím tối kéo tới che khoảng trời phía trên đám quái (dùng ảnh/flipbook mây sét có sẵn trong `art-src/lab/vfx/thunder/`; không vẽ bằng code), chớp lóe trong mây.
2. **Sét dây chuyền (0,6–2,0 s):** một tia từ tay người tung chiêu nhảy tới quái gần nhất rồi nhảy tiếp 8–14 quái, mỗi bước 0,08–0,12 s; tia là ribbon/mesh răng cưa tím-trắng (mỗi kênh ≤ 0,9 trừ lõi mảnh), có nhánh phụ ngắn, giữ 0,15 s rồi mờ; mỗi quái trúng lóe `thunder-impact-v3` hoặc `thunder-impact` có sẵn, giật tê.
3. **Điểm nhấn (2,0–2,4 s):** sét lớn từ mây đánh xuống quái cuối/cụm đông nhất — dùng cột sét đã owner duyệt trong lab (Thunder Pillar ở mục 8) hoặc tia lớn cùng kiểu; nổ `thunder-big-burst` + rung màn nhẹ + nhịp camera `ult-camera-punch.ts` (tâm = điểm đánh).
4. **Dư âm (2,4–3,5 s):** dư điện chớp trên vài quái, mây tan.
Âm thanh: dùng âm Lôi có sẵn trong lab.

## Nghiệm thu
- Kiểm kiểu strict 0 lỗi; probe CPU: số bước nhảy, thứ tự quái gần nhất, thời điểm sét lớn, mọi tài nguyên trả về pool sau 4 s, xoá/tung lại 5 lần không rò; `?thunderUlt=old` trả về bản cũ.
- p95 `stress.html` 100 quái ≤ 16,7 ms; để lệnh chụp cho Claude ở camera chơi 0,4/1,2/2,2/3,0 s và quay clip 4 s.
- Chỉ sửa trong worktree: file mới `src/lab/thunder-ult-chain.ts` và đúng chỗ nối tuyệt kỹ Lôi; không sửa `metal-ult-*`, `ult-camera-punch.ts` (chỉ gọi). Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/434-report.md`.
