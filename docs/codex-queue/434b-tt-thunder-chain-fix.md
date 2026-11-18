# Phiếu 434b: Lôi sét dây chuyền — sửa cho giống phân cảnh


Phản biện: PASS (Sonnet, 17/11)
## Bối cảnh
Chụp 434 ở camera chơi (`typing-game-review/owner-review/2026-11-17/tu-tien/thunder-chain-r1.jpg`, clip `.mp4` cùng tên), so phân cảnh nửa phải `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`: 3,5/10. Lỗi: (1) mây chỉ là dải tím mỏng ở mép xa sân, không phủ trên đầu đám quái, không có ánh tím xuống đất; (2) sét nhảy giữa quái không thấy ở camera chơi, chỉ có tia lửa nhỏ và số sát thương; (3) sét lớn là cột tím vuông hẹp, không xuất phát từ mây, không có nhánh toả; (4) dư âm gần như trống. Owner 17/11 về góc nhìn: mọi thứ trên trời hoặc nằm phẳng phải là hình 3D thật trong không gian, nhìn đúng ở camera chơi, góc trên và góc sau lưng.

## Việc (worktree `games/.wt-ic-lab-all`, `src/lab/thunder-ult-chain.ts`)
1. **Mây:** khối mây 3D (nhiều mặt phẳng nằm ngang chồng lớp hoặc khối thể tích giả) đặt ở độ cao 10–14 m ngay trên đám quái, phủ ≥ 60 % bề ngang khung camera chơi, nằm trong khung (không ra mép trên); texture mây sét có sẵn trong `art-src/lab/vfx/thunder/`; chớp sáng bên trong theo nhịp; ánh tím hắt xuống mặt đất dưới mây (decal hoặc đèn).
2. **Sét dây chuyền:** tia dày 0,25–0,45 m ở camera chơi, sáng lõi trắng viền tím, răng cưa rõ, có 2–4 nhánh phụ mỗi bước; mỗi bước giữ 0,18–0,25 s rồi mờ; vẽ bằng ribbon/mesh 3D nối từ ngực quái này sang quái kia (không phẳng theo màn hình). Tổng 8–14 bước, có thể nhìn rõ từng bước ở 1280×720.
3. **Sét lớn:** từ đáy mây xuống quái cuối/cụm đông nhất: thân sét răng cưa dày 1–1,5 m, nhiều nhánh toả ra đất quanh điểm đánh (6–10 nhánh dài 3–6 m), lóe trắng ngắn 2 khung (không cháy trắng màn), nổ `thunder-big-burst`, vết cháy `thunder-ground-mark` hoặc tương đương có sẵn nằm phẳng trên đất.
4. **Dư âm:** 4–8 quái còn dư điện chớp nhỏ trong 1 s, mây tan dần.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; probe in: vị trí/độ cao/bề rộng mây theo khung camera chơi 1280×720 (≥ 60 % bề ngang, không ra mép trên), độ dày tia ở màn hình (px), số bước nhảy và thời gian giữ, số nhánh sét lớn; pool trả về sau 4 s.
- Để lệnh chụp cho Claude ở camera chơi, góc trên, góc sau lưng tại 0,4/1,2/2,2/3,0 s và clip 4 s. p95 `stress.html` 100 quái ≤ 16,7 ms.
- Chỉ sửa `src/lab/thunder-ult-chain.ts` (và file mới cùng tiền tố nếu cần). Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/434b-report.md`.
