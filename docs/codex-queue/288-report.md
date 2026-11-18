# Báo cáo phiếu 288 · Test chuyển động bầy rồng khí

Đã hoàn tất phần test: **kiểm kiểu qua; 1085/1085 test, 89/89 tệp qua**. Tệp mới có **106 ca**, chạy **240 ms** trong toàn bộ suite, dưới mục tiêu 5 giây. Trong đó **81 ca qua ngưỡng thật, 25 ca `it.fails` ghi nhận hai lỗi còn tồn tại**; không skip ca nào. Kết quả xanh của Vitest không có nghĩa hai lỗi này đã được sửa.

Worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-dragon-swarm`, nhánh `claude/dragon-swarm-lab`, HEAD `3294bed`. Không commit hoặc chạy lệnh Git ghi.

## Tệp đã ghi

- `games/.wt-ic-dragon-swarm/src/lab/dragon-swarm-energy.ts`: phần Codex chỉ thêm bảy `export`: `steerPath`, `Dragon`, `MIN_TURN_M`, `MAX_BEND`, `LENGTH_M`, `PEARL`, `FIELD`.
- `games/.wt-ic-dragon-swarm/tests/lab/dragon-swarm-motion.test.ts`: 24 bộ điểm với seed `0x288d0000`–`0x288d0017`, mỗi bộ có bốn đích ngẫu nhiên trong `FIELD`, cao 2,5–7 m, kết thúc tại `PEARL`. Đo bán kính bằng đường tròn qua ba mẫu liên tiếp cách nhau 0,25 m; kiểm chiều dài, điểm cuối và khoảng cách tại các bước `u` đều, kể cả hai đầu.
- `docs/codex-queue/288-report.md`: báo cáo này trong repo cha.

Tư thế dùng một cây 40 `THREE.Bone`, trục `+Y` hướng đuôi, 39 khoảng tổng cộng `LENGTH_M` (mỗi khoảng `16/39` m), vật liệu giả có đủ bốn uniform. Cùng một `Dragon` bay ba lượt `sweep`, `turn-back`, `near-vertical climb`, bước 1/60 giây tới khi kết thúc. Kiểm góc gập trên cả điểm bộ giải và vị trí xương thế giới, với tâm hai đoạn đều nằm giữa `uSink` và `uReveal`; có mẫu lúc hiện ra và lúc chìm vào ngọc. Kiểm xoay của cả 40 xương, tính hữu hạn của ma trận/quaternion/điểm/uniform và chiều dài đoạn. Khung 0 khởi tạo tư thế bay, phép so xoay bắt đầu từ khung 1. URL giả rỗng chỉ tồn tại lúc import, được khôi phục ngay sau đó.

Giữ nguyên sửa halo `poolTex` có sẵn của Claude. Trong lúc làm, Claude thêm shader `uManeCut`, điều kiện `pools=1` và núm tốc độ `SPEED_K` mặc định 1; các phần này cũng được giữ nguyên. Đối chiếu xác nhận các hằng và mã chuyển động khớp HEAD sau khi bỏ bảy export và tính riêng phép nhân `SPEED_K` của Claude.

## Lỗi thật giữ bằng `it.fails`

**1. Bán kính đường cong trả ra dưới 4,4 m ở cả 24 bộ điểm.** Mỗi ca chỉ đánh dấu thất bại dự kiến cho phép kiểm bán kính; các phép kiểm còn lại vẫn là test thường. Quỹ đạo tĩnh không có khung thời gian, nên bảng ghi lượt/seed, chỉ số mẫu tính từ 0, vị trí theo chiều dài và khoảng cách tới ngọc. Các vị trí dưới đây đều cách ngọc hơn 8 m.

| Seed | Mẫu | Dọc đường (m) | Bán kính nhỏ nhất (m) | Cách ngọc (m) |
| --- | ---: | ---: | ---: | ---: |
| `0x288d0000` | 286 | 71,50 | 3,482605 | 8,337 |
| `0x288d0001` | 216 | 54,00 | 3,779753 | 14,914 |
| `0x288d0002` | 120 | 30,00 | 3,797712 | 13,570 |
| `0x288d0003` | 66 | 16,50 | 4,227765 | 17,756 |
| `0x288d0004` | 122 | 30,50 | 3,970617 | 12,171 |
| `0x288d0005` | 355 | 88,75 | 4,029216 | 8,035 |
| `0x288d0006` | 46 | 11,50 | 3,783969 | 14,712 |
| `0x288d0007` | 42 | 10,50 | 3,783970 | 13,724 |
| `0x288d0008` | 38 | 9,50 | 3,783973 | 9,975 |
| `0x288d0009` | 288 | 72,00 | 4,057402 | 8,133 |
| `0x288d000a` | 300 | 75,00 | 3,997446 | 8,006 |
| `0x288d000b` | 128 | 32,00 | 3,780452 | 12,372 |
| `0x288d000c` | 192 | 48,00 | 3,853716 | 9,840 |
| `0x288d000d` | 74 | 18,50 | 3,783979 | 12,503 |
| `0x288d000e` | 228 | 57,00 | 3,991082 | 18,438 |
| `0x288d000f` | 278 | 69,50 | 3,775488 | 9,698 |
| `0x288d0010` | 80 | 20,00 | 3,783135 | 13,131 |
| `0x288d0011` | 72 | 18,00 | 3,782980 | 14,640 |
| `0x288d0012` | 112 | 28,00 | 3,600411 | 8,411 |
| `0x288d0013` | 246 | 61,50 | 3,596062 | 8,513 |
| `0x288d0014` | 228 | 57,00 | 3,774347 | 9,777 |
| `0x288d0015` | 223 | 55,75 | 4,054450 | 8,088 |
| `0x288d0016` | 366 | 91,50 | 3,773214 | 14,051 |
| `0x288d0017` | 26 | 6,50 | 3,783981 | 8,895 |

Đối chiếu riêng công thức trên đường tròn bán kính 4,5 m cho 4,49999999999995 m. Với seed đầu, giữ tâm tại 71,50 m và giảm bước xuống 0,05 m vẫn đo được 2,992124 m: vi phạm không phải do làm tròn ngưỡng.

**2. Lượt leo gần thẳng đứng có xoay quá 0,6 rad/khung.** Từ `(-12; 2,5; 3)` tới đích đầu `(-11,97; 7; 2,97)`, pha `1,3π`; tiếp tuyến khởi đầu lệch phương thẳng đứng dưới 1°. Giữa **khung 11 → 12**, **xương số 2** xoay **0,7402898821 rad**, khoảng 42,415°. Khung 12 là 0,20 giây sau khi bay, thời gian truyền cho `update` là 0,80 giây do trễ 0,60 giây. Đốt đã hiện: tâm `2,5/39 = 0,064103`, `uReveal = 0,147036`, `uSink = -3,528867`, `uFade = 1`. Dựng cây xương mới rồi chạy riêng lượt này vẫn tái hiện cùng số đo. Chỉ ca xoay của lượt này dùng `it.fails`; hai lượt còn lại kiểm bình thường.

Không sửa hai lỗi, không nới ngưỡng. Các ca `it.fails` sẽ báo lỗi nếu bất ngờ qua, để Claude chuyển lại thành test thường khi sửa chuyển động.

## Kiểm bắt buộc

Chạy trong worktree qua `.local/bin/heavy.sh` của repo cha:

1. `node node_modules/typescript/bin/tsc --noEmit -p .`: **PASS**, thoát 0, đã chạy lại sau khi hoàn tất test.
2. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: **PASS**, thoát 0; lần cuối **1085/1085 test, 89/89 tệp**, **11,97 giây**; tệp mới **106 ca, 240 ms**. SHA-256 source trước/sau lần chạy cuối giữ nguyên: `ac00f8a9bcd31becd2f56c1019acf09f938d2be6fc30d03f86fe24f495f4db0d`.
3. `git diff --check` sạch; tệp test mới không có khoảng trắng cuối dòng. Trạng thái worktree chỉ gồm source của Claude cộng export, test mới và hai link có sẵn:

```text
 M src/lab/dragon-swarm-energy.ts
?? art-src
?? node_modules
?? tests/lab/dragon-swarm-motion.test.ts
```

Repo cha vốn có nhiều thay đổi của các việc khác; phiếu này chỉ thêm báo cáo `docs/codex-queue/288-report.md` tại đó. Không đụng hai link, không chạy build, mở cổng, tải model hoặc tạo media.

## Bàn giao

Claude cần xem **hai lỗi còn mở** ở trên trước khi dùng test làm cổng đưa chiêu vào game. Không còn phần test nào bỏ dở. Không gặp hạn mức công cụ hoặc mốc giờ phải đợi.
