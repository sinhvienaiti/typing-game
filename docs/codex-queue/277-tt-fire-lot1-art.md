# Phiếu 277 · Tu Tiên · Code: lô 1 thay hình vẽ bằng mã của Hỏa bằng art có sẵn

**Loại việc:** code phần nhìn (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn 05/11, không đụng sim, canon hay cân bằng, nên không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/277-report.md`.

**Nguồn:**
- `docs/games/tu-tien/skills/CODE_DRAWN_AUDIT_2026-11-05.md` §3: mục "Luật chung cho mọi lô", "Kiểm chung" và "Lô 1". Đọc đúng ba mục đó.
- Anh đã chọn (05/11 00:20, `docs/work/DECISIONS.md`):
  - vòng ở tay: `fire-halo-ring`;
  - vòng dưới đất: `fire-halo-seal-loop`;
  - sao: `fire-twinkle-set`.
- Dải lửa: `strip-fire-sheath` (anh chọn fire-sheath cho Hỏa ngày 04/11). Nếu có cả bản thường và `-v2`, dùng bản `-v2`, và ghi trong báo cáo lý do.

**Vì sao:** anh chê lửa gai nhọn do mã vẽ (04/11 23:50): "nhìn thực sự rất xấu". Luật mới: hình lấy từ art thật, mã chỉ đặt, căn nhịp và cho chạy.

## Worktree
- `games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, nền `ee3ee97`. Nền này là phiếu 264 đã commit; 264 sửa `impact()` trong cùng tệp, nên lô 1 phải đi sau nó.
- `node_modules` là symlink sang game: không cài thêm gói. `git status --short` lúc giao chỉ in `?? node_modules`.

## Art (chỉ đọc, ở thư mục game chính)
`games/immortality-cultivation/art-src/lab/vfx/`:
- `fire/fire-halo-ring.atlas.png` + `.json`;
- `fire/fire-halo-seal-loop.atlas.png` + `.json`;
- `fire/fire-twinkle-set.atlas.png` + `.json`;
- `aura/strips/strip-fire-sheath(-v2).rgba.png` + `.json`.

Đọc file `.json` để biết lưới, số khung và fps. Nạp ảnh theo cùng đường `FlipbookPool` mà `fire-brush-slash` đang dùng trong `src/view/skills/element-fire.ts`: cùng cách tạo URL, cùng `library()` và `load()`. Không chép ảnh vào worktree.

## Việc
Làm đúng mục "Thay" của Lô 1 trong audit:
1. **`point()`** (`element-fire.ts:310`) thành thẻ một lần của `FlipbookPool` với tấm `fire-twinkle-set`:
   - chọn một hàng ngẫu nhiên từ luồng ngẫu nhiên của view;
   - cỡ = 2 × `reach`;
   - nhát kiếm sông phím 7 giữ cỡ nhỏ như hiện tại.
2. **Vòng ở tay trong `release()`** (`:678`) thành `fire-halo-ring`: quay về camera, chạy một lần, giữ nhịp 0,3 s.
3. **Vòng đất trong `plant()`** thành `fire-halo-seal-loop`: nằm phẳng trên đất, 0,62 s, tắt bằng xói. Nếu pool chưa có xói thì tắt mờ dần trong 3 khung cuối, và ghi trong báo cáo.
4. **Vạch trong `finisher()` và `cutSeam()`** thành dải `strip-fire-sheath` nằm phẳng, cuộn dọc vạch, dùng `dir` và `span` như `sheathAt()` (`:549`).
5. **Bỏ `FirePointPool` và `HeatRingPool` khỏi đường Hỏa mặc định.** Giữ tệp và đường cũ sau cờ lab `?fxcode=1` để so A/B: có cờ thì chạy y như `ee3ee97`.
6. **Khung đầu:** mỗi thẻ mới sáng đủ ngay ở tuổi 0 (ít nhất 95 % đỉnh). Không trễ một khung.
7. **Ngân sách:** không cấp phát mỗi khung; mỗi pool một lệnh vẽ; phím 7 vẫn dưới trần pool 256 điểm.

### Được ghi
- `src/view/skills/element-fire.ts`;
- `src/view/skills/element-stage.ts`, chỉ phần đăng ký pool;
- một test mới `tests/view/fire-lot1-art.test.ts`;
- một changelog `docs/changelog/2026-11-05-fire-lot1-art.md`;
- `docs/codex-queue/277-report.md` ở repo cha.

### Cấm
- Lệnh git ghi.
- Sửa file khác: kit, sim, nội dung, test có sẵn, `art-src`.
- Vitest hay Vite thiếu `--no-cache --configLoader runner`; Vite thiếu `IC_VITE_CACHE_DIR`.
- Mở cổng mạng; tạo ảnh hay âm.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi.
2. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: mọi test qua. Mốc trước là 985 test / 89 tệp ở `ee3ee97`.
3. Test mới, không đọc ảnh, dùng clip giả như test 264:
   - (a) không có `?fxcode`, sau một lượt phím 1 đến 7 với Hỏa, `FirePointPool` và `HeatRingPool` có `count = 0`;
   - (b) có cờ, đường cũ chạy như trước;
   - (c) thẻ sao, vòng tay và vòng đất có độ sáng ở tuổi 0 bằng đỉnh;
   - (d) phím 7 không vượt 256 điểm.
4. Build tạm như phiếu 264, đủ cờ. Grep bundle không thấy chuỗi chỉ dùng trong lab (`fxcode`). Xóa thư mục build.
5. `git diff --stat` và `git status --short` chỉ có các tệp được ghi, cộng `?? node_modules`.

## Claude làm sau
- Chạy `lab-element-parity.mjs` (ONLY theo lô 1) và `lab-element-perf.mjs`.
- Quay video trước và sau ở camera chơi, gửi anh.
- Hai giám khảo mù chấm, mức nhận 8,5.
- Gộp sau 264.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
