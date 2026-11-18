# Phiếu 209 · Last Line · Một vòng chỉnh cân bằng c1-s1

**Chưa có biến thể nào bot đạt đủ điều kiện trên cả hai bộ seed.** Đã đo V0 và đúng **6 biến thể**, mỗi bản đủ seed **1–100 và 101–200**, chỉ `c1-s1`, không sửa game. V6 gần nhất: giữ B3, B6 và hết đảo thứ bậc Thử thách theo tiêu chí phiếu, nhưng còn B1, B7 và G3c. **Cần xử lý luật bến đầy §5.1** ở phiếu sau. TS-M1-12 / N13 chưa đóng; B9 vẫn cần người thật.

Bằng chứng: [bảng tổng, §3, B1–B9 và các cổng S1](209/summary.md), [số liệu đầy đủ](209/summary.json), [bảy mục kiểm](209/verification.json), [phương pháp và cách tái tạo](209/method.md), [đầu ra nguyên](209/runs/). Mọi kết luận dưới đây là của bot, không phải “người chơi thấy vừa”.

## Mốc và chọn nền B

Bản chép `main` ghim tại **`79db62851e00eadeca7bfd44c10c0c682a9cec8d`**. V0 khớp mốc 28/10 ở **24/24 ô Cân bằng + Thử thách mỗi bộ** (kể cả Chuẩn tắt nhịp): thắng, S, P, I không đổi; lệch lớn nhất thắng **0**, S **0** điểm trên từng bộ. JSON seed 1–100 cũng khớp chính xác cả bốn chỉ số ở 24 ô. Bộ 101–200 của mốc cũ chỉ có Markdown. [Lịch sử Git chỉ đọc](209/evidence/main-since-audit.txt) có thay nhãn tiếng Anh, bộ từ ghim và kịch bản hình; không cần đổi mốc vì số khớp.

Chọn nền theo số **ô bot B1 lệch thô** cộng hai bộ; ghi thêm số chỉ số lệch để không lẫn cách đếm. Hòa mới xét B6 Cân bằng trung bình rồi biên B3 nhỏ nhất. Không có hòa ở tiêu chí đầu.

| Hạng | Bản | Ô B1 lệch (chỉ số) | B6 Cân bằng trung bình | Biên B3 nhỏ nhất |
|---|---|---|---|---|
| 1 | **V2 → nền B** | **5 (5)** | +7 | −1 |
| 2 | V3 | 6 (7) | +8,5 | −5 |
| 3 | V1 | 7 (10) | +11,5 | +4 |
| 4 | V0 | 8 (16) | +7,5 | +5 |

V4 và V5 chạy đúng trên V2. [Quyết định nền B](209/decision-B.json) và [lý do chọn V6, ghi trước khi chạy](209/decision-v6.md) giữ nguyên dấu vết quyết định. V6 ghép rỉ của V1 với hai hệ số Thử thách của V4; bỏ dòng nền 4,8 vì nó làm Trẻ em chỉ thắng 84/84 %. V1 giữ B3 và B6 ở cả hai bộ; V4 nâng Nhanh Thử thách so V2 thêm 27/25 điểm, V5 chỉ +0/−4.

## Vì sao V6 gần nhất nhưng chưa được đưa vào game

“Gần nhất” ở đây là ít điều kiện bắt buộc còn trượt nhất khi xét riêng từng bộ: V6 còn **3 + 2 = 5**; V1 còn 7; V0 còn 8; V2–V5 mỗi bản còn 10. Đây chỉ là cách chọn bản để bàn giao, không phải điểm gộp cho phép vượt cổng. B1/B7 đã xét luật sát mép của phiếu: chỉ miễn cả ô lệch ≤ 3 điểm ở đúng một bộ, bộ còn lại phải trong dải. V6 không có ô được miễn.

| Chỉ số / cổng V6 | Seed 1–100 | Seed 101–200 |
|---|---|---|
| B1 | **4 ô, 7 chỉ số lệch** | **3 ô, 3 chỉ số lệch** |
| B1 · Chậm chắc | thắng 95 % (>90), S 74,5 % (>65) | thắng 92 % (>90); ô vẫn lệch cả hai bộ |
| B1 · Chuẩn | thắng 94 % (>90) | trong dải |
| B1 · Khá | thắng 91 % (>90), **I 14,9 % (>10)** | **I 15,1 % (>10)** |
| B1 · Nhanh | thắng 92 % (>90), **I 10,9 % (>10)** | **I 11,2 % (>10)** |
| B3 · Mới CB / Trẻ em TG | 86 / 91 % · đạt | 85 / 89 % · đạt |
| B6 · Tốt − Kém CB / TT | **+12 / +35 điểm · đạt** | **+11 / +32 điểm · đạt** |
| B7 · bậc/đợt lớn nhất; khoảng sinh | 1,557; 86–114 % · đạt phần trần | 1,583; 86–114 % · đạt phần trần |
| B7 · Chuẩn tắt nhịp CB: thắng / S | 89 / **72,5 %**; S vượt 7,5 điểm | 90 / **67,5 %**; S vượt 2,5 điểm, cùng ô bộ kia cũng lệch nên không miễn |
| G3c · kém / tốt / khoảng cách | 73 / **98** / 25 điểm · **trượt trần 97** | 62 / 90 / 28 điểm · đạt |
| Thử thách · Mới / Khá / Nhanh | 63 / 78 / 66 % | 58 / 77 / 61 % |
| Thử thách · Nhanh − Mới | **+3 điểm** · không đảo theo phiếu | **+3 điểm** · không đảo theo phiếu |
| Thử thách · số ô Mới–Nhanh dưới 50 % | 0/6 | 1/6: Ẩu 47 % |

B2, B4, B5, B8, G3m, G5, G8 và §7.6 đều đạt trên cả hai bộ ở V6; các cổng này cũng đạt ở cả 14 báo cáo. B4 V6: S Chậm chắc / Ẩu **74,5/53,5** và **63/43,5 %**; thời gian hạ quái Chuẩn / Ẩu **1,207/1,261** và **1,231/1,325 s** (xem số chính xác trong JSON). §7.6 có 0 báo trước chồng; G8 phát lại 2 trận Node mỗi báo cáo; G3m giữ hai bộ cảnh 1–16, 17–32. B9: **THIẾU SỐ: cần người thật chơi**.

Thử thách hết đảo không có nghĩa mọi chỉ số đã vào dải: riêng thắng Chậm chắc V6 là 83/83 % (>75), Khá 78/77 % (>75). Bảng §3 vẫn đánh dấu toàn bộ thắng/S/P/I/O lệch ở mọi bot và mọi chế độ; không dùng riêng tỉ lệ thắng để tuyên bố cân bằng.

G3c tốt nhất V6 ở bộ đầu là **Scatter Gun + Rail Gun, 98 %**, không có Heat Beam. Vì vậy không dùng `TIA_DUTY` như một cách sửa cặp vượt trần này. Không có thay đổi súng hay vết vàng `s0-trace`.

## Những núm kéo hai phía khác nhau

- **Rỉ 2→2,4 (V1 so V0):** Mới Thử thách 59/51 → 50/47 %, nhưng Nhanh 36/44 → 38/37 %. Ở bộ đầu, Mới khó hơn 9 điểm trong khi Nhanh dễ hơn 2 điểm. Ở Cân bằng bộ sau, Khá 84→85 % nhưng Mới 87→85 %. Tác động không đơn điệu theo tốc gõ và không giải quyết nhàn.
- **Nền 4,4→4,8 (V2):** I Khá 14,8/15,0 → 13,1/13,2 %, nhưng Trẻ em TG 90/91 → 84/84 % và Mới CB 86/87 → 81/70 %. Tăng việc cho người nhanh đã làm phía chậm mất biên trước khi đưa I Khá về 10 %.
- **Đỉnh dài hơn, lặng ngắn hơn (V3):** Trẻ em TG 82/80 %, I Khá vẫn 14,3/14,7 %; không lấy thêm đỉnh tràn để bù.
- **`PACE_GAIN.surge` 1→0,7 (V5 so V2):** cùng seed 1–100, Mới CB 81→79 % trong khi Khá 89→92 %. Ở TT, Mới 40/45→36/34 %, Khá 37/43→45/44 %, Nhanh 17/25→17/21 %. Công thức `1 + gain × (k − 1)` tăng sức đỉnh ở k=0,75 từ 0,75 lên 0,825 (+10 %), giảm ở k=1,248 từ 1,248 xuống 1,1736 (−6 %). Có đối trọng theo tốc gõ nhưng không đủ sửa cả hai phía; không chọn ý này cho V6.
- **Nới hai hệ số TT (V4 so V2):** Nhanh tăng 17/25→44/50 %, Mới tăng 40/45→64/59 %; vẫn đảo −20/−9 điểm. Chỉ khi ghép với nền rỉ V1 ở V6 mới hết đảo theo tiêu chí đã giao. Không suy kết quả ghép từ từng núm riêng.

[Tác động từng ý](209/summary.md#tác-động-từng-ý-so-cùng-seed) có đủ Δ thắng/S/P/I/O cho cả sáu bot ở CB và TT.

## Khuyến nghị và việc sau

**Không đưa bộ số nào vào `src/content` từ phiếu này.** V6 là ứng viên gần nhất để Claude xem tiếp, chưa phải số được duyệt:

| File nếu mở phiếu áp số sau | Đường thử nghiệm | Cũ → V6 | Phạm vi |
|---|---|---|---|
| `games/typing-survival/src/content/chapter-1.ts` | `c1-s1.drainRate` | 2 → 2,4 | đổi băm chương của ải 1 |
| `games/typing-survival/src/content/balance.ts` | `MODE_SPECS.challenge.surge` | 1,1 → 1,0 | mọi ải ở Thử thách |
| cùng file | `MODE_SPECS.challenge.rate` | 1,12 → 1,06 | mọi ải ở Thử thách |

Nếu tiếp tục ứng viên có hằng toàn cục, cần báo cáo `--stages=c1-s1,c1-s2,c1-s3,c1-s4` trước khi commit ở phiếu sau. V5 có `PACE_GAIN` thì ảnh hưởng mọi ải, mọi chế độ; vòng này không chọn nó. Nếu sau này đổi `TIA_DUTY`, phải kiểm cả vết vàng `s0-trace`; vòng này không đổi.

**Luật bến đầy §5.1: cần.** V6 còn I Khá **14,9/15,1 %**, Nhanh **10,9/11,2 %**, đều trên 10 % ở cả hai bộ dù đã hết đảo TT. Đúng điều kiện “Khá hay Nhanh còn I >10 % trên một bộ” của phiếu. Điều này yêu cầu đặc tả/đo luật bến đầy tiếp theo, không chứng minh sẵn rằng tăng sức chứa hay băng nhanh sẽ đạt. Không sửa luật, bộ người chơi, nhịp bắn nền, bot hay dải đích trong vòng này. B9 phải có người thật chơi và đối chiếu bot cùng hồ sơ trước khi nói về trải nghiệm người chơi.

## Bảy mục kiểm

| # | Kết quả có số |
|---|---|
| 1 · Mốc | `79db62851e00eadeca7bfd44c10c0c682a9cec8d`; mỗi bộ 0/24 ô V0 đổi so 28/10; thắng lệch tối đa 0, S lệch tối đa 0 điểm; 0 ô lệch thắng >4 điểm. |
| 2 · Ma trận và ngân sách | **14/14 JSON**, mỗi JSON **36 ô**; **504 ô, 50.400 trận bot**. **14/14 Markdown** đủ **10 cặp G3c**, tổng 14.000 trận cặp. **6/6 biến thể**, không lượt ngắn đổi số. Khói V0 2 seed: 72 trận bot + 20 trận cặp, không vào bảng. |
| 3 · `--set` | **14/14 báo cáo khớp** số đường và từng `old→new`. Hai V0 có **0** dòng `--set`; 12 báo cáo biến thể có đủ đường tương ứng. **42/42 file raw** chép khớp SHA-256 với `tmp/codex-209/runs/`. |
| 4 · Tài nguyên / thời gian | Tối đa **6 báo cáo đồng thời** (V0/A/B/C: 2/6/4/2). Tổng dòng “cả lệnh” **3.425 s = 57 phút 05 s = 0,9514 giờ máy**; cộng khói 6 s là 3.431 s. Tổng thời gian ngoài đo bằng đồng hồ của 14 tiến trình 3.427,642 s; toàn vòng V0–C, kể cả quãng chọn số, 1.085,804 s (18 phút 05,804 s). `TMPDIR` mọi lệnh đo: `/Users/toandx/htdocs/typing-game/games/typing-survival/tmp/codex-209/tmpdir`. |
| 5 · Bản chép | Giải nén lại đúng commit vào `verify/`; `diff -r -x node_modules main verify`: **exit 0, 0 byte đầu ra**. Chạy lại script tổng hợp: **2/2 file cùng SHA-256**. Kiểm này làm trước khi dọn. |
| 6 · Git game | `git -C games/typing-survival status --short -uall` trước và sau đều **0 dòng**; **0 file phiếu này** hiện trong Git game. |
| 7 · Git repo cha | Phần của phiếu chỉ là **`209-report.md` và `209/`**. Repo đã có **401 dòng trạng thái khác** trước lúc làm và vẫn 401 sau kiểm, **0 dòng ngoài phiếu thêm/bớt**. Vì vậy trạng thái toàn `docs/codex-queue` không thể chỉ có 209; không xóa hay thay đổi các mục đã có của làn khác. |

Thời gian mỗi báo cáo, đúng dòng “cả lệnh” (giây; seed 1–100 / 101–200):

| V0 | V1 | V2 | V3 | V4 | V5 | V6 |
|---|---|---|---|---|---|---|
| 203 / 204 | 269 / 274 | 288 / 290 | 283 / 289 | 233 / 237 | 234 / 238 | 190 / 193 |

Các đợt ngày **30/10/2026, UTC+7**; không chồng nhau:

| Đợt | Bắt đầu → kết thúc | `uptime` đầu đợt (nguyên văn) | Số báo cáo đồng thời |
|---|---|---|---|
| V0 | 10:02:36 → 10:06:00 | `10:02  2 users, load averages: 5.10 4.70 4.37` | 2 |
| A | 10:07:05 → 10:11:55 | `10:07  2 users, load averages: 4.98 5.34 4.79` | 6 |
| B | 10:12:22 → 10:16:21 | `10:12  2 users, load averages: 6.25 7.05 5.85` | 4 |
| C | 10:17:29 → 10:20:42 | `10:17  2 users, load averages: 4.74 6.36 5.94` | 2 |

Đã gọi `nice -n 15` ở mọi lệnh đo; sandbox macOS báo `setpriority: Operation not permitted` ở cả **14/14 báo cáo** và khói, nhưng vẫn chạy xong, exit 0. Không khẳng định ưu tiên thực là 15. Không dùng `heavy.sh`, không cài gói, không dùng mạng, dev server, trình duyệt, build hay test suite game. Toàn bộ lệnh và mốc UTC có trong `209/evidence/wave-*.json` để làn khác đối chiếu test thời gian.

## Dọn và bàn giao

Sau Kiểm 5 và khi đã chép raw: xóa đúng `games/typing-survival/tmp/codex-209/main/`, `tmpdir/`, `verify/`; giữ `runs/` và `main.commit`. Không xóa file của người khác. Không có changelog trong game vì game không đổi; không commit/push hay thao tác Git có ghi.

Chủ dự án/Claude cần xem ba việc: **không áp V6 khi còn cổng đỏ**, chốt phiếu luật bến đầy §5.1, và bố trí chơi thật cho B9. Bảng đầy đủ cùng script `209/tools/summarize.mjs` đã sẵn để Claude duyệt rồi commit riêng tài liệu phiếu này.
