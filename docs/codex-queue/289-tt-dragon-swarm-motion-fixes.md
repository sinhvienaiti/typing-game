# Phiếu 289 · Tu Tiên · Code: sửa 2 lỗi chuyển động bầy rồng mà test 288 tìm ra

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn 05/11, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/289-report.md`.

**Worktree:** `games/.wt-ic-dragon-swarm`, nhánh `claude/dragon-swarm-lab`, HEAD là commit test 288 của Claude. `?? art-src`, `?? node_modules` là link của Claude: không đụng. **Không lệnh git ghi.**

## Việc
Đọc `docs/codex-queue/288-report.md` (mục "Lỗi thật giữ bằng `it.fails`").
1. **Bán kính quay dưới 4,4 m** (3,0–3,8 m ở 24 bộ điểm): `steerPath()` trong `src/lab/dragon-swarm-energy.ts`. Lái bay đã giới hạn đúng 4,5 m; nghi phần nội suy (Catmull-Rom qua điểm cách 0,5 m dồn độ cong quanh điểm). Tìm nguyên nhân bằng số đo, rồi sửa sao cho đường trả ra giữ bán kính ≥ 4,4 m ở mọi chỗ cách ngọc hơn 8 m (ví dụ: lấy điểm mỗi bước 0,25 m, hay đường gấp khúc mịn thay cho Catmull-Rom, hay chuẩn hóa tham số). Giữ: điểm cuối là ngọc, độ dài như cũ trong ±5 %, tốc độ đều (test khoảng cách ±3 %), chi phí dựng đường dưới 2 ms mỗi con.
2. **Lật khi leo gần thẳng đứng lúc xuất phát** (xương 2 xoay 0,74 rad giữa khung 11 và 12): trong `Dragon.update()`, khi hướng đầu gần song song phương thẳng đứng mà chưa có "lưng" tin được (đầu chuyến bay), lấy lưng từ hướng ngang tới đích kế tiếp hay từ khung trước, sao cho không khung nào xoay quá 0,6 rad. Không đổi tư thế lúc bay bình thường (so: test lượt `sweep` và `turn-back` giữ số đo như trước trong 1 %).
3. Đổi các ca `it.fails` trong `tests/lab/dragon-swarm-motion.test.ts` thành `it` thường, giữ nguyên ngưỡng.

### Được ghi
`src/lab/dragon-swarm-energy.ts` (chỉ `steerPath`, `Dragon.update`, `Dragon.start` nếu cần), `tests/lab/dragon-swarm-motion.test.ts`, `docs/codex-queue/289-report.md` ở repo cha.

### Cấm
Mọi lệnh git ghi; đổi shader, nhìn, số nhịp chiêu, tốc độ mặc định; sửa tệp khác; mở cổng mạng.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi.
2. Vitest đủ (`--no-cache --configLoader runner --maxWorkers 4`): mọi test qua, **không còn `it.fails`** trong tệp chuyển động; ghi tổng số test.
3. Bảng trước/sau: bán kính nhỏ nhất của 24 bộ điểm; xoay lớn nhất mỗi khung của 3 lượt.

## Claude làm sau
Đo lại trong lab (gập, xoay, gia tốc), quay video, commit.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
