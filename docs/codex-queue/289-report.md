# Báo cáo phiếu 289 · Sửa chuyển động bầy rồng khí

Đã sửa hai lỗi được phiếu 288 giữ bằng test thất bại dự kiến. **TypeScript qua; 1085/1085 test, 89/89 tệp qua**. Tệp chuyển động có **106 ca thường**, không còn `it.fails`, không nới ngưỡng.

Worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-dragon-swarm`, nhánh `claude/dragon-swarm-lab`, HEAD lúc bắt đầu và kết thúc `a143db2` (commit test 288). Số trước sửa được đo lại từ đúng HEAD này; không lấy tên commit cũ trong báo cáo 288 làm giả định.

## Tệp đã ghi

- `games/.wt-ic-dragon-swarm/src/lab/dragon-swarm-energy.ts`: chỉ thân `steerPath()` và `Dragon.start()`.
- `games/.wt-ic-dragon-swarm/tests/lab/dragon-swarm-motion.test.ts`: chuyển các ca thất bại dự kiến thành test thường; thêm đo bán kính bước 0,05 m và cổng chiều dài ±5% so với 24 đường của HEAD.
- `docs/codex-queue/289-report.md` trong repo cha.

## Nguyên nhân và cách sửa

**Bán kính.** Lái tích phân bước 0,25 m, lưu điểm mỗi 0,5 m. Ba điểm đều trên phần quay hết mức cho bán kính khoảng 4,500579 m, nhưng Catmull–Rom xuyên qua các điểm làm độ cong vọt lên tại chỗ bắt đầu hoặc ngừng lái. Đo đường cũ mỗi 0,25 m cho 3,482605–4,227765 m; quét mỗi 0,01 m còn tìm được 2,250053 m. Đây là lỗi hình học, không phải sai công thức đo. Ngoài ra, công thức homing `min(minTurn, dist * 0.5)` bắt đầu giảm bán kính từ 9 m, sớm hơn vùng miễn ngưỡng 8 m.

Giữ bước lái, khoảng lưu điểm và các đích; thay nội suy bằng B-spline bậc hai liên tục tiếp tuyến, có tiếp tuyến giải tích. Các đoạn đi qua trung điểm hai cạnh liên tiếp, làm tròn góc mà không vọt độ cong. Lớp đường nằm trong `steerPath()`, giữ giao diện `getPointAt/getTangentAt` và bảng độ dài mỗi khoảng 5 cm. Hai đầu giữ đúng tọa độ gốc. Homing giữ bán kính đầy đủ tới 7,8 m, chuyển êm về công thức cũ từ 7,8 xuống 7 m; khoảng đệm bảo vệ cả đoạn nội suy sát biên 8 m.

**Lưng khi xuất phát gần thẳng đứng.** `headUp = worldUp` gần song song hướng thân nên hình chiếu vuông góc rất nhỏ, không xác định được lưng ổn định. `Dragon.start()` nay dùng hướng ngang tới đích kế tiếp khi tiếp tuyến đầu có `abs(y) > 0.95`, với trục ngang dự phòng nếu đích trùng theo phương ngang. `Dragon.update()` tiếp tục mang lưng từ khung trước và truyền xuống chuỗi xương bằng cơ chế có sẵn. Các chuyến xuất phát bình thường giữ world-up như cũ.

## Bán kính trước/sau

Cùng 24 seed, cùng điểm và pha như phiếu 288; đo đường tròn qua ba mẫu liên tiếp, chỉ tính tâm cách ngọc hơn 8 m. Đơn vị bán kính: mét. Δ dài so với HEAD.

| Seed | Trước, bước 0,25 m | Sau, bước 0,25 m | Sau, bước 0,05 m | Δ dài |
| --- | ---: | ---: | ---: | ---: |
| `0x288d0000` | 3.482605 | 4.490182 | 4.486842 | 0.474% |
| `0x288d0001` | 3.779753 | 4.490182 | 4.486842 | 0.280% |
| `0x288d0002` | 3.797712 | 4.490182 | 4.486842 | -0.140% |
| `0x288d0003` | 4.227765 | 4.490182 | 4.486842 | -0.120% |
| `0x288d0004` | 3.970617 | 4.490182 | 4.486842 | -0.143% |
| `0x288d0005` | 4.029216 | 4.489460 | 4.460763 | -0.082% |
| `0x288d0006` | 3.783969 | 4.490181 | 4.486842 | -0.188% |
| `0x288d0007` | 3.783970 | 4.490181 | 4.486842 | 2.077% |
| `0x288d0008` | 3.783973 | 4.490181 | 4.486842 | 2.342% |
| `0x288d0009` | 4.057402 | 4.490182 | 4.486842 | 0.707% |
| `0x288d000a` | 3.997446 | 4.490182 | 4.486842 | 1.523% |
| `0x288d000b` | 3.780452 | 4.490182 | 4.486842 | -0.232% |
| `0x288d000c` | 3.853716 | 4.490204 | 4.486857 | -0.187% |
| `0x288d000d` | 3.783979 | 4.490182 | 4.486843 | 1.607% |
| `0x288d000e` | 3.991082 | 4.490184 | 4.486842 | -0.043% |
| `0x288d000f` | 3.775488 | 4.490184 | 4.486842 | -0.038% |
| `0x288d0010` | 3.783135 | 4.490208 | 4.486869 | -0.071% |
| `0x288d0011` | 3.782980 | 4.490197 | 4.486844 | -0.062% |
| `0x288d0012` | 3.600411 | 4.490186 | 4.486842 | -0.110% |
| `0x288d0013` | 3.596062 | 4.490181 | 4.486842 | -0.074% |
| `0x288d0014` | 3.774347 | 4.490349 | 4.486842 | -0.021% |
| `0x288d0015` | 4.054450 | 4.474221 | 4.468166 | -0.097% |
| `0x288d0016` | 3.773214 | 4.490182 | 4.486842 | -0.075% |
| `0x288d0017` | 3.783981 | 4.490181 | 4.486842 | -0.072% |

Bán kính nhỏ nhất sau sửa: **4,474221 m** ở bước 0,25 m; **4,460763 m** ở bước 0,05 m; quét bổ sung mỗi 0,01 m: **4,454508 m**. Kiểm thêm cực trị độ cong giải tích từng đoạn bậc hai: xét cả đoạn nếu bao lồi các điểm điều khiển có thể ra ngoài cầu 8 m, lấy cực tiểu của `|P'|³ / |P' × P''|` trên toàn đoạn. Cận bảo thủ nhỏ nhất của 24 đường là **4,437104 m**, nên cổng 4,4 m không chỉ dựa vào các mẫu rời rạc.

Chiều dài đổi **−0,231600% đến +2,341774%**, trong ±5%. Sai số khoảng cách lớn nhất ở các bước `u` đều tương ứng 0,25 m là **0,434050%**; đo thêm ở khoảng 0,05 m là **2,364483%**, đều dưới 3%. Sai số tọa độ đầu và cuối đều **0 m**.

## Xoay lớn nhất mỗi khung

Cùng cây 40 xương, ba lượt liên tiếp, 60 Hz; phép đo dùng quaternion thế giới và tính mọi xương như test 288.

| Lượt | Trước (rad/khung) | Sau (rad/khung) | Vị trí cực đại sau |
| --- | ---: | ---: | --- |
| sweep | 0.1854587363 | 0.1174171161 | frame 157, bone 10, world rotation (rad/frame) |
| turn-back | 0.2009008862 | 0.1382402564 | frame 407, bone 39, world rotation (rad/frame) |
| near-vertical climb | 0.7402898821 | 0.5030257225 | frame 41, bone 16, world rotation (rad/frame) |

Cả ba dưới **0,6 rad/khung**. Lượt leo vẫn hoàn tất, hữu hạn; gập cực đại 0,35 rad. Hai lượt thường có gập cực đại lần lượt **0,264561** và **0,242581 rad**; mọi cổng gập, độ dài đốt, hiện ra và chìm vào ngọc đều qua.

**Đối chiếu mốc 1% cho riêng sửa tư thế:** chạy cùng đường đã sửa, một lần với khởi tạo world-up cũ và một lần với khởi tạo mới:

| Lượt | Đường mới + lưng cũ | Đường mới + lưng mới | Sai khác |
| --- | ---: | ---: | ---: |
| sweep | 0.1174171161 | 0.1174171161 | 0,000% |
| turn-back | 0.1382402564 | 0.1382402564 | 0,000% |

Gập và độ giãn cực đại của hai lượt này cũng bằng nhau chính xác trong phép đối chiếu trên. Đối chiếu ngược trên đường HEAD cũ cho kết quả tương tự: riêng sửa lưng đổi **0%** các số đo thường. Khi tính **cả sửa đường**, cực đại xoay giảm **36,688%** ở sweep và **31,190%** ở turn-back; vì vậy số tổng sau sửa **không bằng số HEAD trong ±1%**. Đây là ảnh hưởng của việc bỏ vọt độ cong, không phải thay đổi cách dựng tư thế cho lượt thường. Claude cần lưu ý điểm này khi diễn giải yêu cầu 1%.

## Chi phí và kiểm bắt buộc

Đo trên Mac mini M4 qua `.local/bin/heavy.sh`: khởi động nóng 5 vòng × 24 đường, sau đó 20 lần dựng/seed, bao gồm `getLength()`. Trung bình cao nhất theo seed **0,088758 ms**, p95 cao nhất **0,091750 ms**, lần dựng chậm nhất trong 480 lần **0,986667 ms**, dưới 2 ms/con. Đây là số đo dựng đường bằng Node; không thay cho đo khung hình trong lab.

Các lệnh chạy từ worktree:

```sh
../../.local/bin/heavy.sh node node_modules/typescript/bin/tsc --noEmit -p .
../../.local/bin/heavy.sh env VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4
git diff --check
```

- TypeScript: **PASS**, thoát 0.
- Vitest: **PASS**, thoát 0; **1085 test / 89 tệp**, 13,72 giây. Tệp chuyển động: **106 ca**, 470 ms.
- `it.fails` trong tệp chuyển động: **0**. Các ngưỡng 4,4 m, 0,6 rad, `MAX_BEND + 0.01`, ±3%, điểm cuối 1 cm và tỷ lệ dài 2,2 đều giữ nguyên.
- `git diff --check`: sạch.
- SHA-256 source: `dc047909830e257a3b4b05129be19fc551047108ca1d7c9051fac0979b26f048`.
- SHA-256 test: `c044e600c2c681794e2d5c1e7d4541b326b7dfb0e9ff0c434ac935883d962df0`.

## Bàn giao

Claude đo lại gập, xoay, gia tốc trong lab và quay video theo phiếu. Chưa xác nhận thị giác hoặc gia tốc trong trình duyệt. Không chạy build, mở cổng, tạo media hoặc chạy lệnh Git ghi; giữ nguyên hai link `art-src`, `node_modules`, shader, hình thức, nhịp chiêu và tốc độ mặc định. Không có phần bị dừng vì hạn mức hoặc mốc giờ phải đợi.

