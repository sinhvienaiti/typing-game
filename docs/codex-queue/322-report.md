# Báo cáo phiếu 322 · Thanh chiêu có biểu tượng trong lab

**Hoàn tất mã và ba lệnh kiểm.** Worktree `games/.wt-ic-lab-skillbar`, nhánh `codex/lab-skill-bar`, HEAD giữ `b8ebd51`.

## Tệp đã ghi

Các đường dưới tính từ worktree; báo cáo ở repo cha: `docs/codex-queue/322-report.md`.

| Tệp | Dòng thêm / xóa | Nội dung |
| --- | --- | --- |
| `src/lab/skill-bar.ts` (mới) | +145 / −0 | Mười ô 0–9, ảnh 48×48 CSS px, hai kiểu, tooltip, “no icon” khi thiếu/lỗi, nhấp sáng 350 ms, né panel khi resize, hàm đọc trạng thái. |
| `src/lab/skills-main.ts` | +63 / −5 | Phím/nút I, `?icons=jewel`, `?bar=0`, giữ `ui=0`, ánh xạ 0–7, đồng bộ 8/9 sau manifest/chọn/tung, đọc cut-in trước `type()`, `__lab.skillBar()`. |
| `src/lab/clip-skills.ts` | +4 / −0 | Chỉ thêm hàm đọc `selectedId()`. |
| `tests/lab/skill-bar.test.ts` (mới) | +53 / −0 | Tám test thuần chạy Node: tên ảnh, ánh xạ, ngoại lệ try2 và tệp ảnh thật ở cả hai kiểu. |

Tổng mã và test: **+265 / −5 dòng**. Không sửa ảnh; dùng lại các ảnh đã có của phiếu 316/319.

## Kết quả kiểm

Chạy trong worktree được giao; cả ba lệnh thoát 0:

- `npx tsc --noEmit`: **PASS**, không lỗi.
- `npx vitest run tests/lab/skill-bar.test.ts tests/lab/clip-skills.test.ts tests/lab/showcase.test.ts`: **PASS**, 3 tệp, 26/26 test; test ảnh thật đã chạy, không bị bỏ qua.
- `npx vitest run tests/lab`: **PASS**, 14 tệp, 79/79 test.
- `git diff --check`: sạch.

## Biểu tượng còn thiếu và bàn giao

Đọc hai manifest `art-src/lab/vfx/{ult,expansion}/manifest.json`, lọc `role` bằng `roles` và bỏ `rejected` đúng theo `ULT_SHOWCASE`/`EXPANSION_SHOWCASE`, rồi kiểm tệp 48 px theo quy tắc try1/try2 ở cả hai kiểu:

- Phím 8: 18 id hợp lệ; chỉ thiếu **`sky-gate-open-close`** ở cả hai kiểu. `ult-dark` đã bị loại, không tính thiếu.
- Phím 9: 30 id hợp lệ; **không thiếu** ở cả hai kiểu.
- Phím 2 mặc định để trống; `?key2=twin-pearl` dùng `twin-dragons`. Tên phím 7 và tên biểu tượng sản xuất còn chờ anh chốt, đã ghi chú trong mã.

Thanh rộng **628 CSS px** (10×56 + 9×6 + 2×6 padding + 2 viền). Khi panel giao vùng đáy và mép phải panel khoảng 982 px, cửa sổ cần rộng ít nhất khoảng **1.634 CSS px**: 982 + 12 + 628 + 12. Hẹp hơn, phép kẹp giữ thanh trong cửa sổ nên panel vẫn có thể phủ thanh. Với `?key2=twin-pearl`, Claude kiểm thêm hộp thống kê góc dưới phải có phủ các ô cuối hay không.

**DPR 2:** ảnh nguồn 48 px hiện ở 48 CSS px = 96 điểm ảnh thiết bị, tức phóng hai lần. Claude xem hai kiểu đúng cỡ trong lab, kiểm nhấp sáng phím 6, cut-in và né panel/resize. Theo phiếu, không chạy trình duyệt, mở cổng, build hay bộ test toàn game; không dùng lệnh Git ghi. Không còn phần mã bỏ dở, không gặp hạn mức.
