# Làn 1d · Ấn vẽ tay theo hệ

Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`.

## Việc 1 — Đạt

Đã tạo **91 PNG + 13 manifest** tại `games/immortality-cultivation/art-src/lab/vfx/sigils/{fire,water,thunder,wind,ice,earth,wood,light,dark,poison,blood,void,star}/`. Dùng đúng bản `try1` trong `lane3-report.md`, gồm hex/line Hỏa của phiếu 327. Cả 13 bộ mới là hệ khác Kim, nên đều ghi `mode: "color"`; giữ RGB tranh, chỉ xóa nhiễu nền ≤2/255 và viền đệm 2 px. Bộ Kim và ảnh nguồn không đổi.

Đã kiểm nét ≥13/255 không chạm viền trước khi đóng gói; đủ 91 ảnh, đúng kích thước/MD5. Chạy lại toàn bộ: **104/104 file giống từng byte (SHA-256)**. 70 test mặt nạ hiện có/mới đều qua.

Bộ nhớ GPU tính theo RGBA8 gồm toàn bộ mipmap: **Hỏa, Lôi: 29.709.668 byte/bộ (28,33 MiB)**; **Thủy, Phong, Băng, Thổ, Mộc, Quang, Ám, Độc, Huyết, Hư Không, Tinh Tú: 26.913.476 byte/bộ (25,67 MiB)**.

Lệnh tái tạo (trong worktree): `ART_MAGICK=/opt/homebrew/bin/magick node --import tsx scripts/vfx/sigil-masks.ts --all-colors --force`. Dùng `node --import tsx` vì CLI `tsx` mở IPC pipe bị sandbox từ chối.

## Việc 2 — Đạt

Đã nối qua `SwordSkillFx.setElement()` hiện có: phím E và ô Element đổi cả ấn, nứt sao, rãnh của phím 2–6. Nạp lười theo hệ; giữ Kim và bộ đang chọn, tháo texture khỏi vật liệu trước khi `dispose` bộ cũ. Hàng đợi nạp tuần tự loại bỏ kết quả đã lỗi thời khi đổi nhanh; từng ảnh thiếu/lỗi dùng Kim rồi hình code, có cảnh báo console. `?sigil=code` không nạp bộ nào.

Shader `color` cộng RGB từ tranh, nền đen không che nền đất, giữ hiện dần/nhịp sáng và ăn mòn theo `(1 − fade) · 1.1 − 0.1`, về 0 khi hết fade; không tô thêm màu. Kim giữ nhánh mặt nạ/tô màu cũ. Bộ nhớ texture tối đa khoảng **54,00 MiB** (Kim + Hỏa/Lôi).

Đã sửa đúng sáu file được phép: `src/view/skills/{painted-sigils,fxkit,sword-rain,sword-skills}.ts`, `scripts/vfx/{sigil-masks-lib,sigil-masks}.ts`; thêm/sửa `tests/view/painted-sigil-elements.test.ts`, `tests/view/painted-sigils.test.ts`. **Không sửa `src/lab/skills-main.ts`**.

Kiểm tra cuối trong worktree:

- `npx --no-install tsc --noEmit`: sạch.
- `npx --no-install vitest run --maxWorkers=4 --no-cache`: **114 file, 1.311 test qua** (nền 113 file/1.270 test; thêm 41 test). Bao gồm chọn đủ 13 hệ, manifest màu, dự phòng, giới hạn hai bộ, đổi nhanh, giải phóng texture và nối thật qua `setElement()`.
- `git diff --check`: sạch.

Không bỏ hạng mục triển khai nào. Không tạo ảnh mới, mở cổng, mở trình duyệt, chạy build hoặc ghi Git. Theo ranh giới phiếu, chưa kiểm hình/GPU trong trình duyệt; anh cần xem lab khi đổi E/Element và dùng phím 2–6, nhất là độ đọc bộ Ám và sắc độ Hư Không/Lôi/Tinh Tú. Đây là xác nhận mã và media, chưa phải nghiệm thu hình ảnh runtime.
