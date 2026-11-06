# Phiếu 293 · Tu Tiên · Code: sim bầy rồng khí, phần A (đường bay, nhịp, sự kiện)

**Loại việc:** code và logic (`gpt-6.1-sol`, mức `ultra`). Phiếu theo luật làm gọn 05/11.

**Báo cáo:** `docs/codex-queue/293-report.md`.

**Worktree:** `games/.wt-ic-swarm-sim`, nhánh `codex/key2-swarm-sim`, tách từ `main` của game `bbb46d8`. `?? node_modules` là link của Claude: không đụng. **Không lệnh git ghi** (Claude commit).

**Thiết kế đã chốt (đọc trước, là nguồn duy nhất về luật và số):** `docs/games/tu-tien/skills/DRAGON_SKILL.md` **§10** (anh duyệt 05/11 16:00). Mã hiện có của biến thể cũ: `src/sim/twin-pearl.ts`, `src/content/data/twin-pearl.ts`, `src/sim/skills.ts` (cổng cờ, dòng 76, 222, 436), `src/sim/cast.ts`, `src/app/app.ts` (header, rulesHash 146–188), `src/sim/fixed.ts` (`mulDiv`), `src/content/types.ts` (`SimEvent`, `skill-fx` dòng 650–661), `src/sim/events.ts` (hợp đồng sự kiện). Bản đồ chi tiết: `docs/work/consult/key2-qi-swarm-wiring-study.md`.

## Phạm vi phiếu này (phần A)
Biến thể mới **`swarm`** của phím 2 sau cờ header `swordKey2` (giá trị mới `"swarm"`, giữ nguyên `"twin-pearl"` và đường `line` mặc định). **Chưa có sát thương** ở phiếu này (phiếu 294 làm): lần tung vẫn giải, tính hồi chiêu, chờ tung 3 s như cũ, phát sự kiện, rồi kết thúc ở F300.

1. **Dữ liệu** `src/content/data/swarm.ts`: mọi số của §10.2–10.3 (5 rồng, ô 4 m, điểm đám = số quái đất + số quái trời + 2 × số boss, tức một boss tính đúng 2 điểm chứ không phải 3; tối đa 2 đám, ngọc 3/5 · 12 m · lùi 2 m · 60 m, bước 0,25 m, 4096 hướng, rẽ 36 đơn vị, 75 m, 301 mẫu, thân 16 m, xoắn 1,8/0,8/15 m, thả F2 + 6i, lao F180 + 12i, rút 30 tick, nổ F260, hết F300, tốc độ 13–20 m/s) và chỗ sẵn cho số sát thương §10.4 (phiếu 294 dùng). Thêm `"swarm"` vào `SwordKey2` và `SWORD_KEY2_VARIANTS` ở `src/content/data/twin-pearl.ts`.
2. **Hình học nguyên** `src/sim/swarm-geometry.ts`:
   - **Bảng hướng 4096 và bảng sin nguyên là hằng số viết sẵn trong mã** (sinh một lần ngoài sim bằng script, dán vào làm mảng số), có số phiên bản. Test thuần sim cấm `Math.sin/cos/atan2` nên không được tính bảng lúc chạy.
   - Lái từng bước 0,25 m về đích với giới hạn rẽ. **Đoạn lặn vào ngọc** như lab (`git show claude/dragon-swarm-lab:src/lab/dragon-swarm-energy.ts`, `steerPath`, dòng 1124): trong khoảng 7,8 m cuối trước P, bán kính rẽ cho phép giảm còn min(4,5 m, khoảng cách còn lại / 2), để rồng lao thẳng vào ngọc chứ không bay vòng quanh nó.
   - Làm trơn B-spline bậc hai rồi nướng thành mẫu nguyên (như `steerPath` của lab sau phiếu 289, nhưng số nguyên).
   - **Kiểm bán kính** trên đường nền đã nướng (trước khi cộng xoắn), chỉ theo mặt ngang, bằng ba mẫu liên tiếp cách nhau 1 m, chỉ ở các mẫu cách P hơn 8 m; ngưỡng **4,4 m** (cùng một số cho sim và test). Sai thì giữ đường lái chưa làm trơn.
   - Kiểm trong sân, ≤ 75 m, ≤ 301 mẫu.
3. **Đường xoắn khóa theo quỹ đạo:** mỗi mẫu đường s lưu điểm xoắn C(s) = đường(s) + ngang(s)·A(s)·sin(2πs/15 m + φᵢ) + lên·B(s)·cos(2πs/15 m + φᵢ). **Biên độ chỉ phụ thuộc s** (tăng dần trong 3 m đầu từ người ra chiêu, giảm dần trong 8 m cuối trước ngọc), không phụ thuộc vị trí trên thân, không trôi theo thời gian. φᵢ = ⌊i·4096/5⌋ đơn vị hướng. Thân rồng ở tick t chiếm C(s) với s ∈ [s_đầu(t) − 16 m, s_đầu(t)]; trước khi thả thì ẩn. **Rút:** đầu dừng ở P tại tick lao; đuôi chạy tiếp dọc đường vào P, 16 m trong 30 tick; rồng 4 rút xong ở F258, trước nổ F260.
4. **Vạch đường** `src/sim/swarm.ts`:
   - Vùng (5 dải theo trục dài), chọn đám (ô 4 m, điểm, xếp, medoid, hòa theo id), thử [2 đích, 1 đích, không đích].
   - **Ngọc P (theo §10.2, không dùng `heartPoint()` của 271):** H = medoid của ô 4 m điểm cao nhất toàn sân (xếp như §10.2); G = trọng tâm quái đất (không có quái đất thì mọi quái); đi từ H về G 3/5 quãng, tối đa 12 m; kẹp trong sân lùi 2 m (trục nào hẹp hơn 4 m thì lấy giữa trục đó); cuối cùng kẹp trong 60 m quanh người ra chiêu.
   - **Chi phí đường** khi xếp đám = khoảng cách từ người ra chiêu C tới medoid. **Hai đám tách rời** khi ô của chúng cách nhau Chebyshev ≥ 2 ô.
   - **Tuần tra và bay cảnh** (vùng trống, rồng không có đích): một điểm lái ở tâm dải của rồng đó rồi về P.
   - Đòn đầu §10.4 (không quái trong 6 m thì đích đầu của rồng 0 là đám gần người ra chiêu nhất).
   - **Độ cao:** đám đất bay ở y = 1,2 m; đám trời bay ở độ cao của đám; dốc lên xuống tối đa 1:2 theo độ dài đường; không đạt dốc đó thì bỏ đích.
   - Mọi trường hợp biên §10.2.
   - **Thời gian:** T = (tick lao − tick thả)/60 s; L = độ dài đường tới điểm 2 m trước ngọc; tốc độ = L/T, phải nằm trong 13–20 m/s.
     - L > 20T: bỏ bớt đích (thử danh sách tiếp theo).
     - L < 13T: chèn thêm từng điểm lái trên vòng bán kính 6 m quanh P, cách nhau 90° theo chiều rẽ cuối (khoảng 9,4 m mỗi điểm), trước đoạn lặn, tới khi L ≥ 13T. Cửa sổ [13T, 20T] rộng ít nhất 20,7 m nên luôn vào được.
     - **Cả ba lần thử đều hỏng:** dùng đường lái thẳng từ C tới P (vẫn chèn vòng chờ nếu quá ngắn), tốc độ kẹp 20 m/s, ghi cờ `fallback` trong gói sự kiện.
5. **Sự kiện** (`src/content/types.ts`, `src/sim/events.ts`): `skill-fx` giai đoạn `swarm-cast` ở F0 với gói `SwarmCastV1` §10.5. **Mã hóa:** một `Int32Array`, đơn vị mm; mỗi mẫu đường xoắn là 3 số x, y, z; đầu gói là các trường cố định §10.5 theo thứ tự ghi trong mã; kích thước = 4 × số phần tử, trần 24 KiB (24.576 B), quá thì lỗi. `swarm-burst` ở F260, `swarm-end` ở F300. Khóa `rulesHash` của biến thể có phiên bản hình học, bảng, lược đồ. View chưa dùng (phiếu 296); `fx.ts` thêm nhánh để giai đoạn mới **không** bắn loạt kiếm chung (`fx.ts:301-313`).
6. **Cổng cờ:** `createSkillsState` và `resolveCast` định tuyến slot 2 theo dữ liệu: `"swarm"` → `resolveSwarm`. Cờ tắt hay `"twin-pearl"`: hành vi và băm replay **không đổi**. Test ghim băm có sẵn `tests/sim/twin-pearl.test.ts` dòng 674–675 (`scripted(5)`, `scripted(9)`) phải còn xanh; **thêm** dòng ghim `scripted(5, true)` và `scripted(9, true)` với giá trị tính trên mã `bbb46d8` **trước khi sửa gì**.

## Test bắt buộc (`tests/sim/swarm-*.test.ts`)
- Tất định: 200 bố cục ngẫu nhiên có hạt cố định → mẫu đường và gói sự kiện giống hệt byte sau 3 lần chạy lại và sau khi chạy lại cả trận.
- Hình học: bán kính ≥ 4,4 m (cách đo ở mục 2) mọi mẫu nướng cách ngọc hơn 8 m; trong sân; ≤ 75 m; ≤ 301 mẫu; C(s) liền (bước mẫu ≤ 0,6 m); trong 7,8 m cuối đường lặn thẳng vào P, không vòng quanh ngọc.
- Thời gian: bố cục có đường ngắn (quái sát người ra chiêu) vẫn cho tốc độ ≥ 13 m/s nhờ vòng chờ; bố cục ép cả ba lần thử hỏng ra cờ `fallback`.
- Vạch đường: vùng sở hữu đúng; đám xếp đúng (boss ×2, hòa theo id); ngọc đúng luật 271 với ca sân hẹp; đòn đầu: không quái trong 6 m thì đích đầu rồng 0 là đám gần nhất.
- Trường hợp biên §10.2: không quái (chờ tung), 1 quái, 2 quái, mọi quái một vùng, vùng trống, chỉ quái trời, boss, sân hẹp, góc sân, hai lần tung chồng (castId riêng).
- Nhịp: tick thả/lao/nổ/hết đúng bảng; tốc độ trong 13–20 m/s; đầu tới điểm 2 m trước ngọc đúng tick lao (±1).
- Gói `SwarmCastV1` ≤ 24 KiB ở bố cục xấu nhất; cờ tắt: băm replay ghim không đổi; `"twin-pearl"` không đổi.
- Hiệu năng: dựng 5 đường cho 60 quái ≤ 2 ms (Node, đo trung bình) ghi vào báo cáo.

### Được ghi
`src/content/data/swarm.ts`, `src/content/data/twin-pearl.ts` (chỉ thêm `"swarm"` vào `SwordKey2` và `SWORD_KEY2_VARIANTS`), `src/sim/swarm-geometry.ts`, `src/sim/swarm.ts`, `src/sim/skills.ts` (chỉ cổng biến thể), `tests/sim/twin-pearl.test.ts` (chỉ thêm hai dòng ghim băm ở mục 6), script sinh bảng (nếu cần) trong `scripts/`, `src/content/types.ts` (sự kiện), `src/sim/events.ts` (nếu cần), `src/app/app.ts` (chỉ rulesHash biến thể), `src/view/fx.ts` (chỉ nhánh chặn loạt kiếm), test mới `tests/sim/swarm-*.test.ts`, `docs/codex-queue/293-report.md` ở repo cha.

### Cấm
Mọi lệnh git ghi; sửa `twin-pearl` cũ ngoài phần cổng; sát thương (phiếu 294); view/presenter (phiếu 296); float hay `Math.sin/cos/atan2/random` trong sim; mở cổng mạng.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi. 2. Vitest đủ (`--no-cache --configLoader runner --maxWorkers 4`): mọi test qua, ghi tổng. 3. Bảng trong báo cáo: bán kính nhỏ nhất, độ dài, số mẫu, kích thước gói, thời gian dựng cho 200 bố cục; các chỗ Codex phải tự quyết (ghi rõ để Claude duyệt).

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).

## Vòng 3 (Claude chốt 06/11 21:50; phần này thắng mọi chỗ mâu thuẫn ở trên)
Phản biện vòng 2 trượt vì: vòng lượn chờ 6 m quanh ngọc ra ngoài sân thật (40 × 26 m, ngọc chỉ lùi 2 m khỏi biên; đường C→P thường 15–25 m < 13T ≈ 39 m nên vòng chờ là ca thường); đầu rồng ở tick lao mâu thuẫn (điểm 2 m trước ngọc hay ngọc); bộ ba kiểm bán kính lấn vào vùng lặn. Cách sửa đã chốt:
1. **Bỏ hẳn vòng chờ** (mục 4, ý "L < 13T" và "vẫn chèn vòng chờ"): không chèn điểm lái quanh P trong mọi trường hợp.
2. **Nhịp theo độ dài đường, tốc độ cố định:** v = 16 m/s cho mọi rồng. L = độ dài đường nền tới **chính tâm ngọc P**. Tick lao của rồng i = tick thả i + ⌈L_i · 60 / 16⌉ (số nguyên, đơn vị mm và tick). Tick nổ ngọc = max(tick lao) + 32. Tick hết = tick nổ + 40. Tick thả giữ F2 + 6i; rút vẫn 30 tick (nên rút xong trước nổ 2 tick). Bỏ các số cố định "lao F180 + 12i", "nổ F260", "hết F300" ở mục 1 và mục 5; gói `SwarmCastV1` ghi tick lao từng rồng, tick nổ, tick hết. Giới hạn: L ≤ 75 m nên tick hết ≤ F379. Ý "L > 20T: bỏ bớt đích" đổi thành: L > 75 m thì bỏ bớt đích (thử danh sách tiếp theo).
3. **Đầu rồng ở tick lao = P** (không phải điểm 2 m trước ngọc). Test mục "Nhịp" đổi thành: đầu tới P đúng tick lao (±1); tốc độ thực mỗi rồng 16 m/s (±0,2).
4. **Kiểm bán kính:** chỉ dùng bộ ba mẫu mà **cả ba mẫu** cách P hơn 8 m (không bộ ba nào chạm vùng lặn 7,8 m cuối).
5. **Kiểm trong sân** trên đường nền đã nướng, với lề 1,8 m (biên độ xoắn lớn nhất), thay cho kiểm trên đường xoắn.
6. **Ca hỏng cả ba lần thử:** đường lái thẳng C → P, v = 16 m/s như mọi ca, ghi cờ `fallback`.
7. **Test mục "Thời gian"** đổi thành: bố cục đường ngắn (quái sát người ra chiêu) cho tick lao sớm và nổ = max(lao) + 32, không có điểm lái nào ngoài sân; bố cục ép cả ba lần thử hỏng ra cờ `fallback`.
8. **Hết hạn mức:** chỉ ghi dòng `CODEX-WAIT-UNTIL` khi thật sự hết hạn mức; làm xong thì không ghi.
