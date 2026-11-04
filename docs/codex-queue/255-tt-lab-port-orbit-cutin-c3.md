# Phiếu 255 · Tu Tiên · Code: đưa camera xoay phím O và cut-in mặt C3 từ bản xem của chủ dự án vào mã chính của lab

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`). Lời giải đã đủ: đây là bản vá chủ dự án đã thử trên bản lab cố định tối 03/11. Codex chỉ áp nó vào mã hiện tại. Không thiết kế lại gì.

**Báo cáo:** `docs/codex-queue/255-report.md` (tiếng Việt).

## Bối cảnh
- Tối 03/11 chủ dự án thử lab ở bản cố định `games/immortality-cultivation/tmp/owner-preview/`, dựng từ commit `9cb7bcd` cộng bản vá.
  - Anh đã dùng phím **O** để xoay camera quanh sân 360° ("game lab đang không cho thay đổi góc nhìn kiểu 360 độ").
  - Anh đã chọn mặt hô **C3** ("Radiant Resolve") cho cut-in tuyệt kỹ.
- Mã chính của game (`games/immortality-cultivation`) chưa có hai thứ này. Từ `9cb7bcd` tới nay (`1a78a82`), `src/lab/skills-main.ts` và `src/lab/cutin.ts` đã đổi nhiều (hào quang kiếm vòng 1).
- **Bản vá chuẩn:** `docs/codex-queue/255/owner-preview-port.diff`. Ba file, 10 khối, tính từ `9cb7bcd`:
  - `src/lab/orbit.ts` là file mới, lớp `LabOrbit`;
  - `src/lab/cutin.ts` thêm điểm neo và hộp giữ cho khung B, và `CUTIN_SHOUT_CANDIDATES` gồm c1–c4 và b1–b3;
  - `src/lab/skills-main.ts` thêm `freeOrbit`, phím O, các cờ `?cutinArt=a|b|c` và `?cutinShout=c1..c4|b1..b3` (mặc định `c3`).
- Bản gốc đầy đủ của ba file ở `games/immortality-cultivation/tmp/owner-preview/src/lab/` (chỉ đọc).

## Làm ở đâu
- **Worktree riêng của Codex:** `games/.wt-immortality-cultivation-codex`, nhánh `codex/lab-orbit-cutin-port`, gốc `1a78a82`.
  - Một agent Claude đang sửa chính `games/immortality-cultivation/src/lab/skills-main.ts` cho việc khác. Vì vậy **không được ghi gì trong `games/immortality-cultivation/`**.
- `node_modules` trong worktree là symlink sang thư mục của game. Không sửa, không cài thêm gói.

### Được ghi
- `games/.wt-immortality-cultivation-codex/src/lab/orbit.ts` (tạo mới), `src/lab/cutin.ts`, `src/lab/skills-main.ts`;
- `games/.wt-immortality-cultivation-codex/tests/lab/` (test mới);
- `games/.wt-immortality-cultivation-codex/docs/changelog/2026-11-04-lab-orbit-cutin-c3.md`;
- `docs/codex-queue/255-report.md`.

### Cấm
- Mọi lệnh git, trừ `status`, `diff`, `log`, `show`, `ls-files`.
- Sửa file khác những file trên, nhất là `src/kit/**`, `src/sim/**`, `src/view/**` và file trong `games/immortality-cultivation/`.
- Chạy dev server. Tải gói hay ảnh.

## Việc
1. **Áp bản vá lên mã hiện tại,** giữ đúng ý nghĩa của từng khối:
   - `orbit.ts`: chép nguyên.
   - `cutin.ts`: thêm `CUTIN_SHOUT_CANDIDATES`, `C_SHOUT_KEEP`, `B_HAND_KEEP`, điểm neo và hộp mới của khung B. Nếu hàm `frame(...)` hiện tại chưa nhận tham số hộp giữ, làm theo đúng chữ ký trong bản `owner-preview` và giữ tương thích với mọi lời gọi đang có.
   - `skills-main.ts`:
     - import `LabOrbit` và `CUTIN_SHOUT_CANDIDATES`;
     - tạo `freeOrbit` trên `view.stage.renderer.domElement`;
     - phím `O` gọi `freeOrbit.toggle()`;
     - gọi `freeOrbit.apply(camera, dt)` **sau** chỗ zoom, rung và độ giật đặt camera mỗi khung, như trong bản `owner-preview`;
     - đọc `?cutinArt` và `?cutinShout` (mặc định `c3`), chọn style và khung hô đúng như bản `owner-preview`.

   Tìm đúng chỗ tương ứng trong mã mới, đừng dán theo số dòng cũ. Nếu một chỗ không còn tồn tại thì ghi vào báo cáo và làm theo ý của khối đó.
2. **Không đổi gì khác.** Không đổi hành vi khi không bật O. Không đổi khung cut-in của style A, và không đổi khung hô C khi `?cutinShout` không hợp lệ (vẫn dùng mặc định `c3`). Không cấp phát bộ nhớ mỗi khung trong `apply`.
3. **Test mới** `tests/lab/orbit-cutin.test.ts`, chạy được không cần trình duyệt:
   - `LabOrbit`: tắt thì `apply` không đổi camera. Bật, với yaw 0 và độ cao NaN, thì `apply` giữ vị trí camera (sai số ≤ 1e-6). Kéo 100 px ngang thì camera quay quanh điểm nhìn trên mặt đất mà khoảng cách giữ nguyên (sai số ≤ 1e-6). Độ cao kẹp trong 4–89°.
   - `CUTIN_SHOUT_CANDIDATES` có đủ c1–c4 (style `c`) và b1–b3 (style `b`); `c3` dùng file `tt-cutin-c-shout-e3-head-skin-up2x.v2-try1.png`.

   Theo cách viết test đang có trong `tests/`; dùng DOM giả nếu bộ test đã có, nếu chưa thì tạo phần tử tối thiểu có `addEventListener` và `style`.
4. **Changelog** tiếng Việt: làm gì, các cờ, phím O, mặc định C3, cách thử.

## Kiểm bắt buộc (chạy trong `games/.wt-immortality-cultivation-codex`, ghi lệnh và kết quả vào báo cáo)
1. `node node_modules/typescript/bin/tsc --noEmit -p .`: không lỗi.
2. `node node_modules/vitest/vitest.mjs run`:
   - mọi test qua;
   - ghi số test trước và sau (trước: 753 ở `1a78a82`);
   - test golden không đổi.
3. `node node_modules/vite/bin/vite.js build --outDir /private/tmp/codex-255-dist`, rồi `grep -rl "LabOrbit\|cutinShout" /private/tmp/codex-255-dist` phải không ra gì: lab không lọt vào bản build. Xóa thư mục build sau khi kiểm.
4. `git -C games/.wt-immortality-cultivation-codex diff --stat`: chỉ có các file được ghi.

## Hết hạn mức
Giữ mọi file, viết báo cáo phần đã xong. Dòng cuối của tin nhắn cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).

## Nhận
- Các thay đổi trong worktree, chưa commit. Claude đọc diff, chạy lại các lệnh kiểm, thử phím O và C3 trong trình duyệt, rồi mới commit và gộp vào `main`.
- Báo cáo ghi:
  - từng khối của bản vá đã áp vào đâu (file và hàm);
  - chỗ nào phải làm khác và vì sao;
  - kết quả Kiểm 1–4.
