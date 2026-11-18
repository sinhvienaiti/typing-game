# Phiếu 293 · Sim bầy rồng khí, phần A

**Trạng thái:** đã triển khai và qua kiểm tra; có các lựa chọn kỹ thuật bên dưới để Claude duyệt. Chưa bật biến thể trong bản chơi.

- Worktree: `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-swarm-sim`.
- Nhánh: `codex/key2-swarm-sim`; nền nguyên vẹn trước sửa: `bbb46d8e20c6d340df214ad10dbb889271d19dd5`.
- Theo §10 và phần **Vòng 3, 06/11 21:50** của phiếu: bỏ hoàn toàn vòng chờ, tốc độ 16 m/s, đầu tới chính P, nhịp nổ/hết tính từ đường.
- Không chạy lệnh Git ghi; không đổi link `node_modules`; không sửa cây game chính; không chạy build hay mở cổng mạng.

## Đã làm

Đường dẫn sau tính từ worktree:

| File | Kết quả |
|---|---|
| `src/content/data/swarm.ts` | Số vạch đường, hình học, xoắn, nhịp, phiên bản và số sát thương dự trữ cho 294. |
| `src/sim/swarm-geometry.ts` | Bảng sin/hướng nguyên viết sẵn, có phiên bản; lái lượng tử; lặn thu hẹp bán kính; B-spline bậc hai; nướng 250 mm; kiểm bán kính, sân, độ dài, số mẫu và liên tục; xoắn cố định C(s). |
| `scripts/generate-swarm-tables.mjs` | Sinh bảng ngoài sim; lượng giác chỉ có trong script này. |
| `src/sim/swarm.ts` | Chụp F0; 5 dải; ô 4 m; boss đúng 2 điểm; medoid, xếp đám, tách Chebyshev; P theo H/G; thử 2/1/0 đích; tuần tra; độ cao; fallback thẳng; nhịp, thân/rút và sự kiện. |
| `src/content/data/twin-pearl.ts` | Chỉ thêm `swarm` vào kiểu và danh sách biến thể. |
| `src/sim/skills.ts` | Chỉ cổng tạo trạng thái, giải slot 2 và bước biến thể mới. |
| `src/content/types.ts` | `SwarmCastV1 = Int32Array`, ba giai đoạn sự kiện, `castId` và gói `swarm`. |
| `src/app/app.ts` | Chỉ khóa rulesHash của `swarm`: dữ liệu, phiên bản hình học/bảng/lược đồ/va chạm/sát thương. |
| `src/view/fx.ts` | Chỉ chặn ba giai đoạn mới khỏi loạt kiếm chung, kể cả đồng đội. |
| `tests/sim/twin-pearl.test.ts` | Đúng hai dòng ghim mới, lấy trước khi sửa mã. |
| `tests/sim/swarm-sim.test.ts` | 37 test mới, gồm các lượt quét 200 bố cục, tái chạy và trận thật. |

Báo cáo duy nhất ở repo cha: `docs/codex-queue/293-report.md`.

## Kiểm tra

Chạy trực tiếp trong worktree:

```sh
./node_modules/.bin/tsc --noEmit -p .
./node_modules/.bin/vitest run --no-cache --configLoader runner --maxWorkers 4
```

- TypeScript: **PASS**, không lỗi.
- Vitest cuối: **90 file, 1.026 test PASS**, 50,16 s; gồm 37 test mới. Boundary kiểm sim thuần và số nguyên cũng PASS.
- 200 bố cục, mỗi bố cục 60 quái: đường nền, đường xoắn và gói giống byte qua **3 lần chạy lại**.
- 200 kịch bản dùng các hệ thống thật, mỗi kịch bản 390 tick và hai lần tung chồng: chạy lại từ đầu cho cùng gói, sự kiện và băm thế giới cuối. Không có số thực trong trạng thái băm.
- Thêm **200 trận hoàn chỉnh tới kết thúc thua** (phần A chưa gây sát thương), hạt 1–200, gõ phím 2 qua match runner: dựng lại từ header/log cho cùng byte gói và cả hai băm world/local; `officialCheck` chạy qua `runLog` cũng PASS ở cả 200 trận. Test này mất 31,72 s.
- Bán kính được kiểm độc lập bằng bình phương khoảng cách và `BigInt`; cả ba mẫu đều phải ngoài bán kính 8 m quanh P. Bước xoắn, đoạn lặn, sân lùi 1,8 m, độ dài/số mẫu, độ cao và rút cũng có test.
- Hồi chiêu 480 tick, chờ 180 tick, đích tới muộn, quái chết/miễn nhiễm/ngoài sân, vùng rỗng, 1–2 quái, chỉ trời, boss, sân hẹp và góc sân có test.
- Tốc độ danh nghĩa đúng 16.000 mm/s; đầu tới P theo `launch + ceil(L*60/16000)`. Phần tick cuối bị cắt tại P; test kiểm riêng sai số lượng tử và tốc độ trung bình ±0,2 m/s khi đủ 80 tick bay.

### Băm ghim trước khi sửa

Lấy từ chính hàm `scripted` trên nền `bbb46d8`, chạy bằng Node + loader tsx, trước khi chỉnh file nguồn. Bốn dãy đều PASS sau sửa:

| Chế độ | Seed | Dãy băm/số quái sống sau mỗi 300 tick |
|---|---:|---|
| Mặc định, đã ghim sẵn | 5 | `844c012d@22`, `1cb00f08@36`, `527f8f69@58`, `7b865d13@35` |
| Mặc định, đã ghim sẵn | 9 | `aa8ae3cc@23`, `4ba2160f@38`, `753240f5@56`, `29c48d76@34` |
| `twin-pearl`, ghim mới | 5 | `437bec75@15`, `bc834bd0@32`, `4460fd77@50`, `a62359ab@26` |
| `twin-pearl`, ghim mới | 9 | `7008606f@20`, `c872e613@27`, `04617d12@44`, `a089faa5@22` |

## Số đo

Sân thật 40 × 26 m: X −20.000…20.000 mm, Z −18.000…8.000 mm; C = (0, 1.200, 3.000) mm. LCG hạt 293, công thức và thứ tự sinh được giữ trong test. Tổng 200 bố cục × 5 đường = 1.000 đường, mỗi bố cục 60 quái.

| Chỉ số | Kết quả | Ngưỡng |
|---|---:|---:|
| Bán kính nhỏ nhất ngoài vùng loại trừ | 4.443 mm | ≥ 4.400 mm |
| Đường nền dài nhất | 65.312 mm | ≤ 75.000 mm |
| Số mẫu lớn nhất một đường | 263 | ≤ 301 |
| Bước xoắn lớn nhất | 477 mm | ≤ 600 mm |
| Gói lớn nhất trong quét | 11.968 B | ≤ 24.576 B |
| Gói với đủ 5 × 301 mẫu | 18.280 B | ≤ 24.576 B |
| Tick hết lớn nhất trong quét | F331 | ≤ F379 |
| Dựng 5 đường/60 quái, trung bình trong Vitest đủ | 0,590 ms | ≤ 2 ms |
| Lần dựng chậm nhất trong Vitest đủ | 1,059 ms | Ngưỡng phiếu áp dụng cho trung bình |
| Đường fallback | 27/1.000 (2,7 %) | Có cờ trong gói |
| Dựng độc lập bằng Node, trung bình | 0.238 ms | ≤ 2 ms |
| Trung bình chậm nhất một bố cục bằng Node | 0.526 ms | 5 lượt/bố cục |

## Các chỗ tự quyết để Claude duyệt

1. **Trần F379 và phép ceil:** công thức trong phiếu cho rồng 4 dài đúng 75 m kết thúc ở F380: `26 + ceil(75000*60/16000) + 32 + 40 = 380`. Giữ cả công thức lẫn trần F379 bằng cách loại một đường tùy chọn nếu lịch hết vượt trần, rồi thử danh sách đích tiếp theo. Riêng rồng 4 vì vậy dùng tối đa **74.933 mm**; bốn con trước vẫn được đủ 75 m. Fallback thẳng dài tối đa 60 m nên vẫn kịp. Có test ghim phép tính; cần Claude xác nhận cách xử lý 67 mm cuối này.
2. **C sát biên hoặc sân quá hẹp:** không thể vừa giữ C thật ở góc sân vừa cho mọi mẫu nằm trong lề 1,8 m. Không dời C. Ba lần thử bị loại thì dùng đúng fallback C→P, giữ cờ `fallback`; đoạn đầu của fallback này có thể không đạt lề 1,8 m. Với trục hẹp hơn 3,6 m, miền kiểm lề thu về giữa trục; ngọc vẫn theo luật giữa trục khi hẹp hơn 4 m. Có test tách riêng, không tính các ca ngoại lệ này là đạt lề thông thường.
3. **Đường rất ngắn và ±0,2 m/s:** giữ v danh nghĩa 16 m/s và công thức ceil như chốt. Với vài tick bay, tốc độ trung bình L/T không thể luôn nằm trong ±0,2 do một tick cuối; không thêm vòng chờ hay kéo dài đường để che sai số này. Đầu vẫn tới đúng tick, rút đúng 30 tick.
4. **Đơn vị và ID:** hình học, đường và gói dùng mm nguyên. Tích lũy chiều dài spline ở 60 đơn vị/mm, rồi làm tròn lên, tránh mất chiều dài khi cộng các đoạn nhỏ. Bao biên xoắn tăng/giảm tuyến tính theo s, lấy hệ số nhỏ hơn của hai đoạn đầu/cuối; không trôi theo thời gian. ID hòa là `serial` quái; medoid tối thiểu tổng khoảng cách Euclid ngang, không nhân trọng số boss vào medoid.
5. **Ô và độ cao:** lưới 4 m neo vào min sân; khi chọn đích thì giao ô với dải sở hữu. Biên max thuộc ô cuối, không tạo ô rỗng mới. Quái trời nhận theo cổng trời hoặc y > 0; độ cao đích là y của medoid trời, còn medoid đất/C/P là 1.200 mm. Điểm tuần tra là tâm dải đã kẹp lề.
6. **Kiểm thêm để giữ đường đẹp và liền:** đường lặn cuối không được tăng khoảng cách ngang tới P quá 1 mm giữa hai mẫu do làm tròn; đường xoắn không được có bước >600 mm. Vi phạm thì thử ít đích hơn, hết lựa chọn mới fallback. Không có vòng quanh P để chờ.
7. **Gói:** số nguyên Int32 theo thứ tự `SWARM_PACKET` trong mã, header 30 phần tử; tiếp 5 bản ghi `[launch, dive, count, lengthMm, flags, x,y,z…]`. Tick là độ lệch F0, `castTick` là tick tuyệt đối. Checksum FNV-1a theo byte little-endian, trường checksum được coi là 0 khi tính; lưu dưới dạng Int32 có dấu. Các vị trí chung `x/z/toX/toZ` của sự kiện vẫn là mét cho hợp đồng cũ, chỉ gói là mm. Chưa cần đổi `events.ts` vì `EventBody` đã phân phối đúng kiểu.

## Chưa làm theo phạm vi phiếu

- Không gây sát thương, không sóng trúng F1, không mở rộng `hit`: để phiếu 294.
- Không presenter, model, asset, âm thanh, lab hay bật header của bản chơi: để các phiếu sau.
- Không có video hay nghiệm thu hình ảnh: đây là sim A, view mới chỉ chặn loạt kiếm chung; Claude kiểm tích hợp presenter sau 296.

## Bảng 200 bố cục

Mỗi dòng: bán kính nhỏ nhất trong 5 đường, độ dài/số mẫu lớn nhất một đường, kích thước gói toàn bầy, trung bình dựng bằng Node sau 400 lượt làm nóng và 5 lượt đo/bố cục. Thời gian này chỉ đo dựng đường, không tính đóng gói. Cột fallback là số rồng dùng đường thẳng. Các bản tái chạy không tính thêm thành bố cục mới.

| Bố cục | R nhỏ nhất (mm) | L lớn nhất (mm) | Mẫu lớn nhất | Gói (B) | Dựng (ms) | Fallback |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 4460 | 39724 | 160 | 6244 | 0.172 | 0 |
| 2 | 4464 | 45202 | 182 | 7168 | 0.210 | 0 |
| 3 | 4465 | 53132 | 214 | 8308 | 0.243 | 1 |
| 4 | 4461 | 46321 | 187 | 7924 | 0.193 | 0 |
| 5 | 4456 | 45583 | 184 | 8116 | 0.282 | 1 |
| 6 | 4460 | 54734 | 220 | 10528 | 0.278 | 0 |
| 7 | 4466 | 58395 | 235 | 10696 | 0.272 | 0 |
| 8 | 4465 | 45695 | 184 | 7288 | 0.243 | 1 |
| 9 | 4474 | 56628 | 228 | 8524 | 0.251 | 0 |
| 10 | 4470 | 52609 | 212 | 8932 | 0.227 | 0 |
| 11 | 4465 | 41573 | 168 | 8020 | 0.230 | 0 |
| 12 | 4463 | 46604 | 188 | 9304 | 0.228 | 0 |
| 13 | 4474 | 46277 | 187 | 8224 | 0.225 | 0 |
| 14 | 4471 | 57548 | 232 | 9604 | 0.237 | 0 |
| 15 | 4463 | 45232 | 182 | 10324 | 0.245 | 0 |
| 16 | 4451 | 48420 | 195 | 8128 | 0.253 | 0 |
| 17 | 4471 | 45599 | 184 | 7984 | 0.251 | 0 |
| 18 | 4469 | 64441 | 259 | 10396 | 0.301 | 0 |
| 19 | 4460 | 41937 | 169 | 7588 | 0.209 | 0 |
| 20 | 4465 | 43214 | 174 | 7528 | 0.205 | 1 |
| 21 | 4453 | 61891 | 249 | 9484 | 0.270 | 0 |
| 22 | 4458 | 52758 | 213 | 8164 | 0.244 | 0 |
| 23 | 4466 | 45197 | 182 | 6820 | 0.224 | 0 |
| 24 | 4474 | 42508 | 172 | 6316 | 0.219 | 1 |
| 25 | 4454 | 46757 | 189 | 10960 | 0.274 | 0 |
| 26 | 4462 | 62803 | 253 | 9112 | 0.303 | 0 |
| 27 | 4466 | 50399 | 203 | 9664 | 0.280 | 0 |
| 28 | 4449 | 51104 | 206 | 9892 | 0.239 | 0 |
| 29 | 4456 | 45814 | 185 | 10120 | 0.251 | 0 |
| 30 | 4469 | 54683 | 220 | 7852 | 0.277 | 0 |
| 31 | 4457 | 43948 | 177 | 6712 | 0.194 | 0 |
| 32 | 4474 | 39606 | 160 | 7636 | 0.210 | 0 |
| 33 | 4451 | 46267 | 187 | 9472 | 0.283 | 0 |
| 34 | 4460 | 49531 | 200 | 10072 | 0.243 | 0 |
| 35 | 4474 | 46394 | 187 | 8500 | 0.227 | 0 |
| 36 | 4454 | 49193 | 198 | 7288 | 0.200 | 1 |
| 37 | 4470 | 44128 | 178 | 6496 | 0.197 | 1 |
| 38 | 4465 | 55300 | 223 | 8632 | 0.239 | 0 |
| 39 | 4462 | 43934 | 177 | 9244 | 0.235 | 0 |
| 40 | 4472 | 50176 | 202 | 7756 | 0.187 | 0 |
| 41 | 4460 | 48457 | 195 | 9148 | 0.225 | 0 |
| 42 | 4468 | 65116 | 262 | 9784 | 0.232 | 0 |
| 43 | 4467 | 38216 | 154 | 6196 | 0.194 | 0 |
| 44 | 4464 | 48122 | 194 | 8260 | 0.324 | 0 |
| 45 | 4474 | 46904 | 189 | 9112 | 0.276 | 0 |
| 46 | 4453 | 43075 | 174 | 9580 | 0.279 | 0 |
| 47 | 4471 | 45426 | 183 | 6772 | 0.230 | 1 |
| 48 | 4468 | 59478 | 239 | 10240 | 0.291 | 0 |
| 49 | 4466 | 41464 | 167 | 7360 | 0.182 | 0 |
| 50 | 4469 | 39689 | 160 | 6172 | 0.198 | 0 |
| 51 | 4454 | 57057 | 230 | 11524 | 0.360 | 0 |
| 52 | 4470 | 54395 | 219 | 7948 | 0.435 | 0 |
| 53 | 4466 | 40909 | 165 | 5668 | 0.227 | 0 |
| 54 | 4470 | 46124 | 186 | 9028 | 0.268 | 0 |
| 55 | 4466 | 43582 | 176 | 6508 | 0.352 | 0 |
| 56 | 4464 | 45411 | 183 | 7516 | 0.210 | 0 |
| 57 | 4470 | 45341 | 183 | 7336 | 0.235 | 0 |
| 58 | 4465 | 45902 | 185 | 8908 | 0.302 | 0 |
| 59 | 4468 | 49725 | 200 | 10096 | 0.526 | 0 |
| 60 | 4474 | 45166 | 182 | 7096 | 0.228 | 1 |
| 61 | 4462 | 49247 | 198 | 8308 | 0.275 | 0 |
| 62 | 4465 | 46323 | 187 | 7816 | 0.245 | 1 |
| 63 | 4471 | 53383 | 215 | 10528 | 0.303 | 0 |
| 64 | 4454 | 43031 | 174 | 9784 | 0.277 | 0 |
| 65 | 4474 | 47066 | 190 | 7984 | 0.261 | 0 |
| 66 | 4470 | 64072 | 258 | 9592 | 0.426 | 0 |
| 67 | 4474 | 38322 | 155 | 7924 | 0.197 | 0 |
| 68 | 4470 | 42976 | 173 | 7852 | 0.257 | 0 |
| 69 | 4474 | 45914 | 185 | 8548 | 0.297 | 0 |
| 70 | 4457 | 48946 | 197 | 8584 | 0.259 | 0 |
| 71 | 4467 | 43249 | 174 | 6712 | 0.192 | 0 |
| 72 | 4473 | 47577 | 192 | 9292 | 0.230 | 0 |
| 73 | 4458 | 62077 | 250 | 10204 | 0.232 | 0 |
| 74 | 4474 | 45938 | 185 | 7348 | 0.197 | 0 |
| 75 | 4462 | 43981 | 177 | 7792 | 0.195 | 1 |
| 76 | 4470 | 51382 | 207 | 8272 | 0.199 | 0 |
| 77 | 4474 | 46348 | 187 | 8056 | 0.231 | 0 |
| 78 | 4467 | 65312 | 263 | 9472 | 0.238 | 0 |
| 79 | 4466 | 52423 | 211 | 9400 | 0.327 | 0 |
| 80 | 4465 | 40186 | 162 | 6568 | 0.213 | 0 |
| 81 | 4462 | 47684 | 192 | 6700 | 0.198 | 0 |
| 82 | 4471 | 40972 | 165 | 7636 | 0.216 | 1 |
| 83 | 4460 | 42927 | 173 | 8104 | 0.205 | 0 |
| 84 | 4457 | 50027 | 202 | 9124 | 0.204 | 0 |
| 85 | 4474 | 45423 | 183 | 8536 | 0.234 | 0 |
| 86 | 4470 | 52966 | 213 | 8896 | 0.219 | 0 |
| 87 | 4443 | 52221 | 210 | 8644 | 0.211 | 0 |
| 88 | 4467 | 53649 | 216 | 8356 | 0.194 | 0 |
| 89 | 4471 | 41675 | 168 | 7192 | 0.184 | 0 |
| 90 | 4459 | 54116 | 218 | 8896 | 0.263 | 0 |
| 91 | 4474 | 43607 | 176 | 7996 | 0.233 | 0 |
| 92 | 4471 | 47715 | 192 | 7132 | 0.171 | 0 |
| 93 | 4459 | 54071 | 218 | 11104 | 0.319 | 0 |
| 94 | 4467 | 45134 | 182 | 9364 | 0.245 | 0 |
| 95 | 4473 | 45441 | 183 | 9772 | 0.245 | 0 |
| 96 | 4472 | 47955 | 193 | 6964 | 0.179 | 1 |
| 97 | 4473 | 44553 | 180 | 7000 | 0.182 | 1 |
| 98 | 4466 | 47143 | 190 | 7924 | 0.206 | 0 |
| 99 | 4470 | 45948 | 185 | 8152 | 0.206 | 0 |
| 100 | 4464 | 49220 | 198 | 7492 | 0.247 | 0 |
| 101 | 4465 | 39600 | 160 | 7156 | 0.200 | 0 |
| 102 | 4473 | 46190 | 186 | 9316 | 0.226 | 0 |
| 103 | 4461 | 43063 | 174 | 8752 | 0.309 | 0 |
| 104 | 4474 | 43999 | 177 | 7624 | 0.266 | 0 |
| 105 | 4448 | 42118 | 170 | 8104 | 0.200 | 0 |
| 106 | 4453 | 53383 | 215 | 10504 | 0.364 | 0 |
| 107 | 4448 | 42242 | 170 | 8080 | 0.204 | 0 |
| 108 | 4448 | 43336 | 175 | 8836 | 0.241 | 0 |
| 109 | 4459 | 46674 | 188 | 9304 | 0.209 | 0 |
| 110 | 4456 | 49179 | 198 | 6916 | 0.219 | 0 |
| 111 | 4468 | 53271 | 215 | 10252 | 0.293 | 0 |
| 112 | 4458 | 48520 | 196 | 7372 | 0.208 | 1 |
| 113 | 4471 | 56957 | 229 | 10012 | 0.277 | 0 |
| 114 | 4471 | 43391 | 175 | 7084 | 0.216 | 1 |
| 115 | 4467 | 49775 | 201 | 9736 | 0.247 | 0 |
| 116 | 4457 | 56372 | 227 | 10036 | 0.240 | 0 |
| 117 | 4464 | 62900 | 253 | 11968 | 0.270 | 0 |
| 118 | 4461 | 54767 | 221 | 8884 | 0.347 | 0 |
| 119 | 4471 | 47453 | 191 | 6532 | 0.236 | 1 |
| 120 | 4466 | 54293 | 219 | 9016 | 0.270 | 0 |
| 121 | 4463 | 49732 | 200 | 7420 | 0.214 | 0 |
| 122 | 4454 | 53399 | 215 | 9124 | 0.232 | 0 |
| 123 | 4466 | 45932 | 185 | 8428 | 0.226 | 0 |
| 124 | 4472 | 47496 | 191 | 9604 | 0.243 | 0 |
| 125 | 4453 | 47022 | 190 | 7504 | 0.197 | 0 |
| 126 | 4473 | 41108 | 166 | 7540 | 0.239 | 1 |
| 127 | 4451 | 47075 | 190 | 8296 | 0.250 | 0 |
| 128 | 4472 | 55389 | 223 | 8152 | 0.209 | 0 |
| 129 | 4473 | 41896 | 169 | 9052 | 0.262 | 0 |
| 130 | 4471 | 45588 | 184 | 6328 | 0.194 | 1 |
| 131 | 4474 | 52164 | 210 | 8176 | 0.227 | 0 |
| 132 | 4457 | 47186 | 190 | 8644 | 0.218 | 0 |
| 133 | 4461 | 55279 | 223 | 9940 | 0.278 | 0 |
| 134 | 4467 | 56989 | 229 | 9580 | 0.289 | 0 |
| 135 | 4468 | 55570 | 224 | 8380 | 0.212 | 0 |
| 136 | 4463 | 47490 | 191 | 8284 | 0.244 | 0 |
| 137 | 4458 | 42271 | 171 | 6688 | 0.202 | 1 |
| 138 | 4474 | 47738 | 192 | 6868 | 0.204 | 0 |
| 139 | 4474 | 46996 | 189 | 7792 | 0.297 | 0 |
| 140 | 4462 | 50121 | 202 | 9664 | 0.272 | 0 |
| 141 | 4451 | 48236 | 194 | 9088 | 0.229 | 0 |
| 142 | 4462 | 44638 | 180 | 7768 | 0.220 | 0 |
| 143 | 4460 | 43085 | 174 | 7876 | 0.199 | 0 |
| 144 | 4459 | 44712 | 180 | 8344 | 0.210 | 0 |
| 145 | 4466 | 50342 | 203 | 7276 | 0.198 | 0 |
| 146 | 4462 | 52642 | 212 | 8236 | 0.205 | 0 |
| 147 | 4469 | 48066 | 194 | 7516 | 0.244 | 0 |
| 148 | 4474 | 41483 | 167 | 7252 | 0.201 | 0 |
| 149 | 4472 | 41650 | 168 | 6820 | 0.179 | 0 |
| 150 | 4471 | 47287 | 191 | 7636 | 0.182 | 0 |
| 151 | 4465 | 51379 | 207 | 10336 | 0.251 | 0 |
| 152 | 4461 | 47764 | 193 | 7840 | 0.201 | 0 |
| 153 | 4459 | 45348 | 183 | 9244 | 0.252 | 0 |
| 154 | 4474 | 47865 | 193 | 8584 | 0.221 | 0 |
| 155 | 4456 | 63150 | 254 | 9280 | 0.242 | 0 |
| 156 | 4471 | 50785 | 205 | 10612 | 0.251 | 0 |
| 157 | 4469 | 45056 | 182 | 8032 | 0.197 | 0 |
| 158 | 4457 | 56178 | 226 | 8524 | 0.253 | 1 |
| 159 | 4474 | 49707 | 200 | 9580 | 0.231 | 0 |
| 160 | 4460 | 44660 | 180 | 7828 | 0.217 | 0 |
| 161 | 4450 | 49255 | 199 | 8668 | 0.276 | 0 |
| 162 | 4463 | 49014 | 198 | 8140 | 0.223 | 0 |
| 163 | 4457 | 42516 | 172 | 9220 | 0.238 | 0 |
| 164 | 4462 | 52122 | 210 | 8944 | 0.206 | 0 |
| 165 | 4471 | 54481 | 219 | 9436 | 0.210 | 0 |
| 166 | 4476 | 46228 | 186 | 8008 | 0.188 | 0 |
| 167 | 4469 | 43393 | 175 | 6964 | 0.189 | 0 |
| 168 | 4471 | 48068 | 194 | 7840 | 0.201 | 0 |
| 169 | 4470 | 48772 | 197 | 9292 | 0.202 | 0 |
| 170 | 4464 | 56344 | 227 | 9232 | 0.215 | 0 |
| 171 | 4472 | 51239 | 206 | 9256 | 0.225 | 0 |
| 172 | 4453 | 64680 | 260 | 8836 | 0.226 | 0 |
| 173 | 4462 | 45330 | 183 | 8764 | 0.246 | 0 |
| 174 | 4472 | 48062 | 194 | 8800 | 0.229 | 0 |
| 175 | 4474 | 52566 | 212 | 8752 | 0.223 | 0 |
| 176 | 4464 | 59619 | 240 | 9844 | 0.288 | 1 |
| 177 | 4473 | 46073 | 186 | 6364 | 0.206 | 0 |
| 178 | 4458 | 46492 | 187 | 8368 | 0.212 | 1 |
| 179 | 4467 | 37493 | 151 | 7300 | 0.191 | 1 |
| 180 | 4473 | 53175 | 214 | 8572 | 0.248 | 0 |
| 181 | 4474 | 43100 | 174 | 7576 | 0.204 | 1 |
| 182 | 4464 | 47318 | 191 | 7324 | 0.182 | 0 |
| 183 | 4457 | 41817 | 169 | 7360 | 0.198 | 0 |
| 184 | 4460 | 50552 | 204 | 9244 | 0.229 | 1 |
| 185 | 4474 | 44770 | 181 | 7060 | 0.185 | 0 |
| 186 | 4465 | 48153 | 194 | 10108 | 0.232 | 0 |
| 187 | 4467 | 44190 | 178 | 6052 | 0.162 | 0 |
| 188 | 4459 | 50078 | 202 | 10228 | 0.230 | 0 |
| 189 | 4459 | 59283 | 239 | 8176 | 0.197 | 0 |
| 190 | 4469 | 48804 | 197 | 7648 | 0.189 | 0 |
| 191 | 4452 | 51582 | 208 | 8932 | 0.272 | 0 |
| 192 | 4467 | 47188 | 190 | 7948 | 0.272 | 0 |
| 193 | 4457 | 44649 | 180 | 8944 | 0.247 | 0 |
| 194 | 4467 | 43905 | 177 | 6112 | 0.149 | 0 |
| 195 | 4463 | 49206 | 198 | 8308 | 0.242 | 1 |
| 196 | 4464 | 43651 | 176 | 7768 | 0.208 | 0 |
| 197 | 4457 | 45815 | 185 | 10576 | 0.260 | 0 |
| 198 | 4457 | 56992 | 229 | 11764 | 0.266 | 0 |
| 199 | 4471 | 45752 | 185 | 6772 | 0.199 | 0 |
| 200 | 4472 | 63608 | 256 | 11968 | 0.307 | 0 |
