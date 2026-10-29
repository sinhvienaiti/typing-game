# Phiếu 161 · Dragonhold · Vẽ lại bốn icon (137, 139)

**Nguồn:** chấm nhận ảnh 29/10 của Claude (`docs/codex-queue/accept-29-10/verdict.md`): ảnh của phiếu gốc chưa đạt M ≥ 8 theo mức chợ. Phiếu này sửa đúng các ảnh bị trả.

**Báo cáo:** `docs/codex-queue/161-report.md`.

## Luật chung (phiếu làm lại)

- **Luật gốc:** theo nguyên văn mục "Luật chung" của phiếu gốc (`docs/codex-queue/137-dh-ui-hud.md` (với `armour`, `danger`) và `docs/codex-queue/139-dh-ui-map-cards.md` (với `flag-pull`, `swarm`)), trừ những điểm ghi dưới đây. Đọc phiếu gốc và báo cáo gốc (`docs/codex-queue/137-report.md`) trước.
- **Chỉ dẫn sửa:** `docs/codex-queue/accept-29-10/verdict.md`, mục "137 `armour`", "137 `danger`", "139 `flag-pull`" và "139 `swarm`". Prompt tiếng Anh ở đó dán nguyên văn vào lượt sinh. Tờ so của người chấm: `docs/codex-queue/accept-29-10/dh-icons-137-139.jpg`.
- **Không ghi đè:** bản mới ghi thành `<tên>.v2.png` (và các bản thu, `.v2.alpha.png`, `.v2.tryN.*`) cạnh bản cũ. Claude đổi sang khi nhận.
- **Hậu kỳ không được phá tranh (luật mới 29/10, người chấm nhận ảnh):** ở 4/6 phiếu vừa chấm, lượt sinh đã đạt nhưng bước công cụ làm hỏng nó (hộp tối nung vào trời, mép núi san phẳng, khung bị bỏ phần vẽ, gamma làm phai), và bản tự chấm vẫn ghi 8. Từ nay:
  - mỗi ảnh giao có một tờ **"bản sinh | bản hậu kỳ"** cạnh nhau, cùng cỡ, ở `_review/161/raw-vs-final/`;
  - bước công cụ chỉ được cắt, tách nền, đổi cỡ, sửa mép, làm liền mép, chỉnh sáng nhẹ toàn ảnh (±10 %); không được xóa, san phẳng, phủ mảng màu hay thay phần vẽ;
  - khi một ngưỡng số trong phiếu mâu thuẫn với tranh (muốn đạt số phải làm bẩn tranh), **dừng lại**, giữ tranh đẹp, ghi rõ mâu thuẫn trong báo cáo để Claude quyết;
  - tự chấm M trên bản hậu kỳ, không trên bản sinh.
- **Bố cục (Wordwoven):** tránh "dày kiểu AI". Mỗi tranh có một trọng tâm và khoảng 40 % khung là vùng yên (trời rộng, sương, mặt nước). Ruộng bậc thang không vàng chanh rực: xanh ngọc và vàng lúa chín trầm.

## Việc

1. **`armour.v2`** (137): áo giáp ngực rộng có vai, viền sắt sẫm; ở 12–18 px không được thành một que.
2. **`danger.v2`** (137): huy hiệu tam giác sắt, men cam đỏ, vết nứt than hồng (không phải tia sét, vì tia sét đọc thành "điện, choáng"); gamma ≤ 1,3, không làm phai.
3. **`flag-pull.v2`** (139): lá cờ Héo tím xám chiếm nửa icon, bị giật lên khỏi cục đất; không thành "nắm tay cầm giáo".
4. **`swarm.v2`** (139): theo màu model kiến gai (nâu sẫm, mai đá xám), đính kèm `games/dragon-hold/art-src/enemies/thorn-ant.tripo.png`; thân to chân ngắn; không kem vàng (trùng màu phe ta).

**Kiểm:** như phiếu gốc, cộng tờ `raw-vs-final`, cộng `_review/161-sheet.jpg`: bốn icon mới cạnh bộ đã nhận của 137–139 ở cỡ trong game 720p và 1080p trên nền HUD; IoU dáng với mọi icon cùng chỗ hiện ≤ 0,80.
