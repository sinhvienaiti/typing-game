# Phiếu 019 · Lời Gọi · kiểm lại độc lập lượt sửa sau đợt test 27/10 (chỉ đọc)

**Bối cảnh:** ba người test của Claude chơi Lời Gọi ngày 27/10 và tìm ra 13 lỗi nặng, 34 lỗi nhẹ. Một agent Claude đã sửa phần lớn, ở các commit `dfd574f`, `fe5186a`, `f7d43fc`, `d6c98cf` và commit giấy tờ sau đó. Bảng lỗi nằm ở `games/typing-defense/docs/changelog/2026-10-27-test-pass.md`. Phiếu này là lượt kiểm lại độc lập, thay cho agent kiểm lại của Claude. Codex không viết bản sửa nào nên nhìn không bị lệch theo người sửa (giống phiếu 011).

Chủ dự án (27/10) giao một phần việc cho Codex và yêu cầu làm đúng, không sai sót. Mọi kết luận phải có bằng chứng: ảnh đã xem, số đo, đầu ra lệnh. Không chắc thì ghi "chưa chắc", không đoán.

**Thư mục làm việc:** `games/typing-defense`. **Chỉ đọc mã.**

**Được ghi:**
- `tmp/codex-019/` (bằng chứng, không vào Git);
- `docs/codex-queue/019-report.md` ở repo cha.

**Cấm:**
- sửa mã, tài liệu hay test của game;
- lệnh git có ghi (chỉ được `log`, `show`, `diff`);
- đụng media, game khác, Tu Tiên.

**Máy dùng chung:** mọi lệnh nặng chạy qua `../../.local/bin/heavy.sh` (`--gpu` cho trình duyệt). Dev server riêng ở cổng 4291 (`pnpm exec vite --host 127.0.0.1 --port 4291 --strictPort`, chạy nền), tắt khi xong.

## Việc

1. **Đối chiếu changelog với diff.** Với mỗi dòng "Đã sửa" trong bảng của `2026-10-27-test-pass.md`, tìm đoạn mã trong diff `5c3b939..HEAD` làm đúng điều dòng đó nói. Mỗi dòng ghi: khớp, khớp một phần (thiếu gì) hoặc không thấy mã.
2. **Cổng.**
   - `pnpm check`: số test, kích thước gói "/" so với trần 85 kB, số dòng so với trần 10.500.
   - `pnpm td:golden:check`: hai file phải `same: true`.
   - Ghi đầu ra rút gọn của cả hai.
3. **Tái hiện từng lỗi nặng đã sửa** (dòng 1, 2, 3, 5, 6, 7, 8 phần gợi ý, 9, 10, 11 của bảng, cùng mọi dòng nặng khác ghi "Đã sửa"). Dùng repro ở mục "Repro của người sửa" bên dưới, hoặc cách của người test trong bảng. Mỗi lỗi ghi:
   - **đã hết**, **còn** hoặc **không tái hiện được**;
   - bằng chứng: ảnh trong `tmp/codex-019/` và số đo.
   - Những lỗi về chữ đè, thẻ che phải đo ở cả 1280×720 và 1920×1080.
4. **Chơi hồi quy.** Mỗi màn bị đụng, chơi một lượt đủ ở 1280×720, gõ phím thật qua CDP. Dùng lại `scripts/visual/scenarios` và thư viện của nó; script tạm để trong `tmp/codex-019/`.
   - Màn cần chơi: Ngày/Đêm 1–4, Đêm 5 cùng boss, hộp cát.
   - Ghi: lỗi console, chữ tràn hoặc bị cắt, thẻ che hành động, phím mất (số phím gửi so với số phím game đếm).
5. **Kịch bản sẵn có.** Ở hai cỡ chạy: `td-1b-learn`, `td-1b-story`, `td-1b-boss`, `td-1b-night5`, `td-1b-build`, `td-1b-chunks`, `td-theme`, cùng kịch bản mới của lượt sửa nếu có (xem `git show --stat` của các commit). Ghi đạt hay trượt.

## Báo cáo `docs/codex-queue/019-report.md`

- Bảng 1 (mục 1): `| # | Lỗi | Changelog nói | Mã thấy ở | Khớp? |`.
- Bảng 2 (mục 3): `| # | Lỗi | Cỡ | Kết quả | Bằng chứng |`.
- Mục 2, 4, 5: đầu ra rút gọn và danh sách lỗi mới, mỗi lỗi có mức (nặng, nhẹ), cách tái hiện, ảnh.
- Cuối báo cáo: lỗi nào Claude cần sửa tiếp, xếp theo mức.

**Xong khi:** mọi dòng "Đã sửa" đều có kết luận kèm bằng chứng, và có đủ mục 2, 4, 5.

## Repro của người sửa

(Claude điền sau khi lượt sửa xong.)
