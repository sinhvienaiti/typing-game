# Vòng 4 · Bước 1 · Cột Lôi: khung va chạm của hệ Lôi thay ngôi sao mực (sau `tp2=1`)

Anh duyệt vòng 4 lúc 07/11 17:55 ("Làm vòng 4"). Cả bốn giám khảo vòng 3 cùng chê một chỗ: ở 1,03 s có một **ngôi sao viền đen kiểu hoạt hình**, lệch phong cách với sét vẽ tay, và nó che kín các quái bị đánh (`docs/work/consult/r3-step1b-panel.md`, `r3-step3-verdict.md`). Luật: `.agents/skills/game-vfx-production/references/path-to-8.md` §7. Đọc §7 trước.

## Nguồn của ngôi sao
- Đây là **khung va chạm cục bộ** dùng chung: `ScreenFx.localFlash()` trong `src/view/screen-fx.ts`, `LOCAL_STEP` (mặt nạ `burst` + `slash`, chế độ `IMPACT_INVERT`), 3 khung (50 ms).
- Lab gọi nó từ `bus.on` trong `src/lab/skills-main.ts` (khoảng dòng 408, `screen.localFlash(...)`).
- Mặc định vẽ thành ngôi sao **mực** trên nền giấy, viền xanh. Hệ Hỏa đã có biến thể riêng qua `ScreenAccent.frames` trong `src/view/skills/element-kit.ts` và nhánh `#ifdef ROLES` (`fireBurst`, `fireSparks`) trong shader của `screen-fx.ts`. Hệ Lôi chưa có, nên rơi về ngôi sao mực.

## Việc (chỉ điểm này)
- Cho hệ Lôi một khung va chạm cục bộ **của riêng nó**, theo đúng cách hệ Hỏa đã làm (vai trò màu riêng và hình riêng trong nhánh `ROLES`):
  - hình: **sét phân nhánh** tỏa ra từ một tâm trắng nhỏ, tím–trắng, đầu nhánh mảnh; không có viền mực đen, không có nền giấy đặc;
  - quái trong vùng khung giữ đọc được: bóng thân tối tím với viền lila sáng mảnh (đừng phủ trắng hay mực lên thân);
  - giữ đúng thời lượng 3 khung và kích thước theo `localPx` hiện có; góc xoay **cố định theo hướng đòn** (không thêm xoay ngẫu nhiên giữa các lần tung).
- Có thể dùng mặt nạ đã có trong `art-src/skills/impact-tex/` làm nền hình; nếu thêm hàm hình mới thì viết như `fireBurst`, trong cùng shader, sau `ROLES`.
- **Chỉ bật khi `tp2=1`** cho Cột Lôi trong lab (A/B); `tp2` tắt thì mọi hệ, kể cả Lôi, giữ nguyên từng điểm ảnh. Hệ Hỏa và các hệ khác không đổi trong mọi trường hợp.
- Quầng ≤ 0,9 mỗi kênh; không tăng bloom chung.

## Ngân sách (bắt buộc, §7)
- Cả Cột Lôi khi bật `tp2`: thêm ≤ 1,0 ms p95 so với khi tắt; không thêm draw call (cùng pass); không cấp phát mỗi khung.
- Mã gọn, khoảng ≤ 150 dòng không tính test. Không shader mới: chỉ thêm nhánh trong shader `screen-fx` hiện có, như hệ Hỏa.

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`.
- **Được ghi:** `src/view/screen-fx.ts`, `src/view/skills/element-kit.ts` (phần Lôi), chỗ nối trong `src/lab/skills-main.ts`, test trong `tests/`, báo cáo `docs/codex-queue/laneL1-report.md`.
- **Không:** sửa media hay manifest; lệnh git ghi; mở cổng mạng; mở trình duyệt.

## Đạt khi
- Test node: Lôi + `tp2` dùng vai trò và hình Lôi; `tp2` tắt thì shader định nghĩa và uniform của mọi hệ y như cũ; Hỏa không đổi; không cấp phát mỗi khung.
- `npx --no-install tsc --noEmit` sạch; chạy riêng các file test liên quan. Claude chạy toàn bộ vitest.
- Báo cáo ≤ 6 dòng: số dòng mã thêm, Claude cần quay gì.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
