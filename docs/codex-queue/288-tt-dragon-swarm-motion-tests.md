# Phiếu 288 · Tu Tiên · Code: test chống tái phát cho chuyển động bầy rồng khí (lab)

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn 05/11, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/288-report.md`.

**Worktree:** `games/.wt-ic-dragon-swarm`, nhánh `claude/dragon-swarm-lab`, HEAD `3294bed` (có thể có thay đổi nhỏ chưa commit của Claude trong `src/lab/dragon-swarm-energy.ts`: giữ nguyên). `?? art-src`, `?? node_modules` là link của Claude: không đụng. **Không lệnh git ghi** (Claude commit sau).

## Vì sao
Anh chê (05/11): rồng "bị vặn xoắn người khiến vỡ hình" khi quay đầu, rồi "hơi giật giật". Claude đã sửa trong `src/lab/dragon-swarm-energy.ts` và đo bằng tay:
- `steerPath()`: quỹ đạo bay từng bước 0,25 m, không rẽ gắt hơn `MIN_TURN_M` (4,5 m), trừ đoạn lao vào ngọc (bán kính co theo khoảng cách); bảng độ dài mịn 5 cm.
- `Dragon.update()`: xương đặt theo khung sống lưng (hướng lưng của đầu mang qua từng khung, rồi truyền đốt sang đốt), kẹp gập `MAX_BEND` giữ độ dài, xoắn không còn đổi theo độ cong.
Số đo sau sửa: gập giữa 2 đốt ≤ 20°, xoay của một đốt giữa 2 khung p99 4,8°, tối đa 31°, gia tốc thân p99 0,07 m/khung². Phiếu này khóa các tính chất đó bằng test.

## Việc
1. Trong `src/lab/dragon-swarm-energy.ts`, chỉ **export** những gì test cần (`steerPath`, `Dragon`, các hằng `MIN_TURN_M`, `MAX_BEND`, `LENGTH_M`, `PEARL`, `FIELD`). Không đổi hành vi, số hay nhịp.
2. Viết `tests/lab/dragon-swarm-motion.test.ts`:
   - **Quỹ đạo:** với ít nhất 20 bộ điểm đích sinh ngẫu nhiên có hạt cố định trong `FIELD` (độ cao 2,5–7 m, điểm cuối là `PEARL`), lấy mẫu mỗi 0,25 m:
     - bán kính quay ≥ 4,4 m ở mọi chỗ cách điểm cuối hơn 8 m;
     - độ dài ≤ 2,2 lần độ dài đường gấp khúc qua các điểm đích (không lượn vòng);
     - điểm cuối trùng `PEARL` (sai số ≤ 1 cm);
     - `getPointAt` với u đều cho khoảng cách đều trong ±3 %.
   - **Tư thế:** dựng một chuỗi 40 `THREE.Bone` thẳng (dài `LENGTH_M`, `+Y` mỗi xương hướng về đuôi), một `SkinnedMesh` nhỏ hoặc chỉ cây xương nếu `Dragon` cho phép, và một vật liệu giả có `uniforms` (`uTime`, `uFade`, `uReveal`, `uSink`). Cho `Dragon` bay theo `steerPath` qua ít nhất 3 lượt (một lượt có đoạn leo gần thẳng đứng), bước 1/60 s:
     - mọi đốt đang hiện (`(k+0.5)/39` giữa `uSink` và `uReveal`): góc giữa hai đoạn liền nhau ≤ `MAX_BEND` + 0,01;
     - xoay thế giới của mỗi xương giữa 2 khung liên tiếp ≤ 0,6 rad (không lật);
     - không có NaN, không đoạn nào dài hơn 3 lần bình thường.
3. Nếu một test lộ lỗi thật trong mã, **không sửa mã**: đánh dấu test `it.fails` kèm ghi chú, và ghi rõ trong báo cáo (khung, lượt, số đo).

### Được ghi
`src/lab/dragon-swarm-energy.ts` (chỉ thêm `export`), `tests/lab/dragon-swarm-motion.test.ts`, `docs/codex-queue/288-report.md` ở repo cha.

### Cấm
Mọi lệnh git ghi; sửa tệp khác; đổi hành vi; mở cổng mạng.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi.
2. Vitest đủ (`--no-cache --configLoader runner --maxWorkers 4`): mọi test qua; ghi tổng số test và thời gian riêng của tệp mới (mục tiêu dưới 5 s).
3. `git status --short` chỉ có các tệp được ghi (cộng thay đổi sẵn có của Claude).

## Claude làm sau
Đọc test, commit vào nhánh lab, dùng làm cổng khi đưa chiêu vào game.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
