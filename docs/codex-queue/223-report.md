# Phiếu 223 · Dragonhold · DH-08

**B35cdp giống lượt CDP nhất về máu: đạt 8/10 đợt trong ±15 HP ở lần hiệu chỉnh thứ ba.** Trên 2 × 20 seed mức Thường, G1 b35 cũ **85,0 %**, b35cdp **100,0 %**, b35human **100,0 %**; hai bot mới vượt trần 90 %. B4 vẫn đạt: thời gian hạ quái lần lượt **4,186 / 2,197 / 3,560 s**, đều nhỏ hơn sloppy **5,234 s**; steady S **63,6 %** vẫn hơn sloppy **57,7 %**. Đề xuất Claude chọn **b35human** làm ứng viên đại diện G1 và nhánh Chuẩn của B4, vì giữ đúng tay 35 WPM/95 %/CV 0,25 và chỉ sửa hai điểm DH-08; dùng b35cdp đối chiếu bản ghi. Chưa tự đổi bot/gate mặc định. Các thử sức ép ±10 % và Héo lan ×1,1 vẫn thắng 40/40, nên chưa đề xuất đổi dữ liệu gameplay.

## 1. Mốc và điều kiện chạy

- Dùng **`222/attribution.json`**, không dùng danh sách dự phòng. Có `222-report.md`; danh sách 51 đường dẫn, 0 `unattributed`; đầu lượt status 51/51 thuộc danh sách, 0 lạ.
- Nhánh `dh-codex`, HEAD đầu/cuối **`6aa593a2dce6637cccbe24a58709b86f7127f607`**, không có commit mới cần xét. Không chạy Git ghi.
- `pnpm check` được chạy vì điều kiện số 4 và mục kiểm của chính phiếu yêu cầu, là ngoại lệ cụ thể với house rule chung không chạy build/test. Trước mọi sửa mã: mã **0**, **69 file / 593 test**, kit **75**, golden **10/10**, TypeScript và Vite xanh. Không sửa lỗi của 187/194/195/197.
- Năm JSON trình duyệt đọc/parse được. SHA-256 samples đúng `d9e4220369c0f6131db82c2ed41073ff108b58e5f40a79b86abc79246ce1f0f7`. MD5 golden đầu/cuối đúng `75f74947dac170d05fd659f99417940e`.
- Baseline b35 seed 1 khớp **10/10** `heroDamage`: **0, 107, 229, 101, 50, 188, 160, 75, 117, 183**, tổng **1.210**. G1 b35 40 seed khớp **85,0 %** tham chiếu.
- TMPDIR tuyệt đối: `/Users/toandx/htdocs/typing-game/games/.wt-dh-codex/tmp/codex-223/tmpdir`. Đã xóa sau khi kết thúc các tiến trình.
- CLI `pnpm dh:balance` đầu gặp `listen EPERM`, không phải lỗi sim; log giữ trong `default-before.log`. Các lượt tiếp dùng nhánh dự phòng đã cho: `TSX_DISABLE_CACHE=1 node --import=tsx scripts/balance/run.ts` với cùng tham số. Không chạy server, trình duyệt hay mạng.

Bằng chứng: [prerequisites.json](223/prerequisites.json), [start-status.txt](223/start-status.txt), [start.diff](223/start.diff), [check-before.log](223/check-before.log), [trace-b35.json](223/trace-b35.json).

## 2. Cách đo dữ liệu trình duyệt

[Browser script](223/browser.mjs) chỉ đọc năm JSON, không mở ảnh. Cửa sổ đợt bắt đầu ở mẫu đầu phase=2 của đợt, kết thúc ở mẫu đầu sau mẫu phase=2 cuối; sai số cửa sổ khoảng 100 ms. Máu đầu lấy mẫu đầu, min lấy mọi mẫu wave. Chữ cái lấy theo `letters.t` trong cửa sổ; chữ/phút = số chữ × 60 / số giây. Tổng **745 phím trong wave** khớp `end.keys=745`; 905 phím ghi được gồm cả 160 phím panel/prelearn/review. Không dùng `rc-raw.hurt`.

**Không đo được số từ hoàn tất từng đợt từ các dữ liệu này.** `timeline.kills` gồm bẫy và kỹ năng; `words` là số từ sống, còn từ có thể biến mất vì quái chết; `stats.words=168` đếm lượt vòng gõ, có thể bỏ dở sau trượt. Không đổi chúng thành số từ hoàn tất. Bot headless đo trực tiếp sự kiện `word-complete`.

Phản xạ đúng phép đo phiếu: mỗi chuyển 0→≥1 visibleWords trong wave, tìm phím chữ đầu sau mốc mẫu. Có **144 mẫu**, **0 thiếu phím kế tiếp**. Ghi cả khi giữ/bỏ các mẫu có khoảng [mốc chữ hiện, phím kế] giao với khoảng dừng ước tính. Sai số lấy mẫu **±100 ms**; phép đo không phải thời gian nhận thức của người. Có thể mẫu 100 ms đã lỡ phím đầu của một từ, nên chỉ diễn giải theo định nghĩa của phiếu. `words===visibleWords` trong wave. Tỷ lệ gần nhất của trình duyệt theo mã PICK là **100 % lần chọn tự do**, khóa và urgent được xét trước; không ước lượng từ ảnh/timeline.

| Đợt | HP đầu | HP min | Tụt | Chữ | Chữ/phút | Từ xong | PX p50/p90 ms (n) | Bỏ dừng p50/p90 ms (n) |
|---|---|---|---|---|---|---|---|---|
| 1 | 469 | 469 | 0 | 49 | 60.7 | không đo được | 35/241 (12) | 35/127 (11) |
| 2 | 492 | 492 | 0 | 71 | 82.6 | không đo được | 194/407 (13) | 154/363 (11) |
| 3 | 515 | 515 | 0 | 66 | 80.5 | không đo được | 216/571 (14) | 216/571 (12) |
| 4 | 538 | 538 | 0 | 77 | 91.7 | không đo được | 186/450 (15) | 42/326 (12) |
| 5 | 561 | 551 | 10 | 99 | 97.2 | không đo được | 198/648 (20) | 198/413 (17) |
| 6 | 584 | 584 | 0 | 63 | 78.4 | không đo được | 142/392 (14) | 142/392 (13) |
| 7 | 607 | 574 | 33 | 74 | 94.5 | không đo được | 256/657 (13) | 78/368 (8) |
| 8 | 607 | 592 | 15 | 68 | 80.3 | không đo được | 307/585 (12) | 303/355 (9) |
| 9 | 630 | 583 | 47 | 67 | 81.4 | không đo được | 308/605 (11) | 37/449 (7) |
| 10 | 630 | 630 | 0 | 111 | 102.5 | không đo được | 194/717 (20) | 184/395 (15) |

Dữ liệu thô cho thấy **đợt 9 tụt 47 HP** (630→583), không phải tối đa 33 như diễn giải nguồn. Kết thúc vẫn **653/653 HP**; hồi máu trong đợt và tăng mức HP có thể che tổng sát thương. Tỷ số tick/(ms×0,06) từng đợt nằm trong khoảng 0.9935–0.9965. Xem [browser-waves.json](223/browser-waves.json) cho từng mẫu phản xạ và nhãn dừng.

## 3. Khoảng dừng của kịch bản và giả định b35cdp

Không có log bắt đầu/kết thúc mọi lần PNG, PICK hay eval. Không thể nhận diện chính xác phân bố chu kỳ hỏi từ khoảng giữa hai phím vì còn ngủ sau từ, kỹ năng, ảnh và không có từ. Đã giữ giới hạn này thay vì coi khoảng phím là chu kỳ hỏi. Giả định poll là **90 ms + proxy hai eval 16–20 ms**, lấy chín số đo SNAP→mark ở warning: **110, 109, 107, 107, 107, 107, 106, 107, 106 ms**. Đây là phân bố thay thế có căn cứ, chưa phải phân bố poll được đo trực tiếp. Phản xạ p50 khi bỏ dừng **154 ms**, p90 **392 ms**.

Các `moments.at` gần `timeline.t` cùng warning (chênh 16–20 ms cho hai SNAP); dùng offset đồng hồ 0, sai số căn chỉnh ước tính ±25 ms. Mỗi mark/shot **giả định 100 ms**, không khẳng định đã đo thời gian PNG. Mốc peak chỉ làm tròn giây, sai số ±0,5 s. Bảng dưới cộng hợp các khoảng (không đếm chồng); phần montage và ghi sheet không có timestamp riêng nên tổng là xấp xỉ. Burst letters ở đợt 2 chạy song song, không cộng toàn bộ 1.626 ms vào dừng; không thấy đuôi chờ sau chữ cuối từ dữ liệu.

| Đợt | Các dừng: tên = ms | Tổng xấp xỉ (s) |
|---|---|---|
| 1 | start-banner=1511; 02-start=100; ff-sleep=250; 08-ff-try=100; 03-first-word=100; complete-place-moss-grunt=1112; 05-peak-6foes-15s=100; 09-mid20s=100; 05-peak-6foes-30s=100; 05-peak-8foes-43s=100; 10-mid45s=100 | 3.673 |
| 2 | start-banner=1512; 02-start=100; 11-first-trap-trigger=100; ff-sleep=250; 08-ff-try=100; 03-first-word=100; 09-mid20s=100; 05-peak-9foes-109s=100; 10-mid45s=100 | 2.462 |
| 3 | start-banner=1535; 02-start=100; 11-first-trap-trigger=100; ff-sleep=250; 08-ff-try=100; 03-first-word=100; 09-mid20s=100; 05-peak-9foes-174s=100; 10-mid45s=100 | 2.485 |
| 4 | start-banner=1555; 02-start=100; ff-sleep=250; 08-ff-try=100; 11-first-trap-trigger=100; 03-first-word=100; 09-mid20s=100; 05-peak-9foes-244s=100; 10-mid45s=100 | 2.505 |
| 5 | start-banner=1517; 02-start=100; ff-sleep=250; 08-ff-try=100; 11-first-trap-trigger=100; 03-first-word=100; 06-general=100; 09-mid20s=100; general-move=1160; 10-mid45s=100; 05-peak-9foes-321s=100 | 3.727 |
| 6 | start-banner=1519; 02-start=100; 11-first-trap-trigger=100; 03-first-word=100; ff-sleep=250; 08-ff-try=100; 09-mid20s=100; 05-peak-9foes-386s=100; 10-mid45s=100 | 2.469 |
| 7 | start-banner=1548; 02-start=100; 11-first-trap-trigger=100; ff-sleep=250; 08-ff-try=100; 03-first-word=100; 09-mid20s=100; 04-first-damage=100; hp-loss=1734; 05-peak-9foes-456s=100; 10-mid45s=100 | 4.332 |
| 8 | start-banner=1537; 02-start=100; 11-first-trap-trigger=100; 03-first-word=100; 04-first-damage=100; hp-loss=1711; ff-sleep=250; 08-ff-try=100; 09-mid20s=100; 05-peak-9foes-519s=100; 10-mid45s=100 | 4.298 |
| 9 | start-banner=1535; 02-start=100; 11-first-trap-trigger=100; ff-sleep=250; 08-ff-try=100; 03-first-word=100; 04-first-damage=100; hp-loss=1650; 09-mid20s=100; 05-peak-9foes-591s=100; 10-mid45s=100 | 4.235 |
| 10 | start-banner=1542; 02-start=100; complete-cold-blight-wolf=1132; 11-first-trap-trigger=100; 03-first-word=100; ff-sleep=250; 08-ff-try=100; 09-mid20s=100; 10-mid45s=100; 05-peak-9foes-666s=100 | 3.624 |

| Mốc sim của b35cdp | Độ dài và cách áp dụng |
|---|---|
| Vào wave | Start-banner đúng đợt 1.511–1.555 ms + mark 100 ms |
| Máu giảm lần đầu, xét giữa các từ | Mark 100 ms + hp-loss 1.734/1.711/1.650 ms ở đợt 7/8/9; nếu phát sinh ở đợt không có burst ghi được thì dùng median 1.711 ms |
| Từ đầu; 20 s; 45 s; trap-trigger đầu; house-pulse đầu; banner plant | 100 ms/mốc, sự kiện phát sinh lúc gõ được chờ tới ranh giới hai từ |
| G01 sống lần đầu; G01 vào dưới 20 m | Mark 100 ms; general-move 1.160 ms, một lần cả lượt |
| Đỉnh số quái ≥max(6, maxLive), cách shot trước >9 s | 100 ms/shot, giữ maxLive toàn lượt như script |
| Không từ, có quái trong 26 m | 250 ms thử FF + mark 100 ms, một lần/đợt; không tăng tốc sim |
| Burst chữ | Từ đầu dài ≥6, 1.626 ms chạy song song; chỉ chờ đuôi sau chữ cuối |
| Burst hoàn tất đợt 1/10 | Từ có quái dài 2–5; chờ 120 ms trước chữ cuối, 200 ms sau; tổng burst 1.112/1.132 ms, chờ phần đuôi rồi gap từ |
| Sau mỗi phím thường | max(5, KEY_MS×(0,6+0,8r)−6), KEY_MS=342,857 ms; có cả gap sau phím cuối trước gap từ |
| Sau từ | KEY_MS×(0,5+r), độc lập với gap phím cuối |
| Phần eval/chọn từ còn thiếu | Lần 1: 0; lần 2: 50; lần 3 giữ: **100 ms** trước phím đầu. Đây là hiệu chỉnh trong dải phản xạ đo được, không đổi nhóm khác |
| Lượt nghỉ | Plan b35, skills=false; chờ **không có lệnh Plan trong 1 s**, gồm kiểm cả hàng lệnh của tick hiện tại, rồi call-early |

Kỹ năng được xét giữa hai từ: breath mỗi ≥8 s khi live≥3; skyfire mỗi ≥11 s khi live≥5; inferno khi rage≥1000; small-potion khi HP<45 %. Một vòng xét đủ các phím rồi mới chọn từ, tránh lặp inferno/potion bị từ chối ở mỗi tick và chặn gõ. Skill không có tọa độ giống lệnh phím. Plan vẫn có thể uống thuốc dù skills=false. Trên 40 lượt: **Plan consumable=0, typist consumable=0, rejected consumable=0**; lượt trình duyệt cũng potions=0. Số sent/rejected theo loại và từng lượt ở `measure-waves.json → results.b35cdp.runs[].cdp`.

## 4. Test trước và thiết kế hai bot

`tests-red.log`: **mã 1**, **1 suite đỏ**, **0 test nạp được** vì chưa có `scripts/balance/human.ts`. Trước mã đã khai báo 13 ca bao phủ bảy nhóm bắt buộc. Sau đó thêm một ca kiểm hàm đo không đổi log/hash và đo gần nhất tại lúc chọn. Sau cùng **14/14**, thời gian test **0,320 s**, toàn lệnh **0,683 s <10 s**.

B35human giữ `BOTS.b35.hands`, policy và logic khóa/trượt/backspace/crowd; bỏ standard. Trọng số danger/nearest/first = **0,2/0,7/0,1**: nearest 70 % vượt mức ≥60 %, còn 30 % giữ phản ứng với nguy hiểm và từ xuất hiện trước. Phản xạ dùng `Hands.reactionMs`/RECOGNIZE: known 0,35–0,6 s, learning/due 0,5–0,9 s, new 0,8–1,6 s; không rõ nhóm dùng 450×(0,6–1,4) ms. Mốc sẵn sàng = max(lúc rảnh, bornTick×TICK_MS + nhận ra) + một khoảng phím. Từ đã hiện đủ lâu không bị cộng thêm thời gian nhận ra.

Hai spec không nằm trong BOTS/BOT_NAMES/M0_BOTS, không có standard; xúc xắc vẫn là seed XOR hash tên bot như runBot. `findBot` tra được cả worker/trace/--bots, tên lạ (kể cả toString) trả undefined. Không có --bots thì vẫn 15 bot cũ theo thứ tự. Hai thế giới có pace bằng createWorld với 35 WPM và mặc định 950/250, đã test.

Phép đo dùng `WaveMeasure` trên các frame onTick, `bornTick` và sự kiện word-progress/word-complete. Switch+advance cùng phím chỉ đếm một lần. Mốc chọn mục tiêu lấy **lúc typist nhận mục tiêu**, không lấy khoảng cách lúc phím đầu (quái có thể đã đổi thứ tự). Decorator chỉ đọc target TS-private của Typist cũ, không rút xúc xắc hay gửi thêm lệnh; test so cả log/hash với runBot trực tiếp của ba bot. Đổi cấu trúc private target sau này cần cập nhật riêng phép đo này. Phiếu không sửa Typist cũ.

Không dùng label, capacityWpm=0 hay learnOk của hai bot mới để kết luận. `run.sent` của mã cũ chỉ đếm Plan; hành động của typist riêng được đọc ở log cdp riêng, không diễn giải run.sent là tổng lệnh mới.

## 5. Hiệu chỉnh seed 1

Giữ nguyên bộ từ botDeck và cách mua Plan. Chỉ thay một nhóm sau lần 1: trễ chọn/eval **0→50→100 ms**. Không thử thay bộ từ hoặc shop. Có một lượt dò triển khai trước bảng hiệu chỉnh, phát hiện call-early kiểm 1 s trước khi thấy lệnh Plan của chính tick đó. Đã sửa để xét cả hàng lệnh hiện tại; giữ [diagnostic-before-early-fix.json](223/diagnostic-before-early-fix.json), không dùng nó làm bằng chứng đạt. **Có 4 lượt b35cdp seed 1 đầy đủ nếu tính cả lượt dò lỗi này; ba lượt hiệu chỉnh có bảng bên dưới.** Đây là giới hạn quy trình cần Claude thấy rõ khi hiểu “tối đa 3 lần” là tổng mọi lượt dò, thay vì ba lần hiệu chỉnh cấu hình.

### Lần 1 · trễ chọn 0 ms · 7/10 đợt trong ±15 HP

| Đợt | Tụt CDP gốc | Tụt b35 cũ | Tụt b35cdp | Chênh mới−gốc | Từ xong mới | Chữ/phút mới | PX mới p50/p90 ms |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 12 | 43.9 | 66.7/133.3 |
| 2 | 0 | 74 | 0 | 0 | 16 | 62.8 | 83.3/383.3 |
| 3 | 0 | 185 | 0 | 0 | 15 | 67.3 | 83.3/216.7 |
| 4 | 0 | 56 | 0 | 0 | 16 | 73.8 | 83.3/466.7 |
| 5 | 10 | 27 | 0 | -10 | 18 | 81.4 | 83.3/616.7 |
| 6 | 0 | 117 | 0 | 0 | 15 | 64.8 | 116.7/583.3 |
| 7 | 33 | 160 | 13 | -20 | 17 | 77.7 | 116.7/383.3 |
| 8 | 15 | 52 | 15 | 0 | 13 | 68.0 | 100.0/650.0 |
| 9 | 47 | 117 | 68 | 21 | 18 | 71.2 | 83.3/300.0 |
| 10 | 0 | 54 | 18 | 18 | 23 | 88.1 | 383.3/2233.3 |

### Lần 2 · trễ chọn 50 ms · 7/10 đợt trong ±15 HP

| Đợt | Tụt CDP gốc | Tụt b35 cũ | Tụt b35cdp | Chênh mới−gốc | Từ xong mới | Chữ/phút mới | PX mới p50/p90 ms |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 12 | 41.3 | 133.3/183.3 |
| 2 | 0 | 74 | 0 | 0 | 16 | 62.8 | 133.3/266.7 |
| 3 | 0 | 185 | 0 | 0 | 16 | 76.9 | 166.7/550.0 |
| 4 | 0 | 56 | 0 | 0 | 16 | 70.2 | 133.3/466.7 |
| 5 | 10 | 27 | 12 | 2 | 21 | 85.1 | 316.7/1600.0 |
| 6 | 0 | 117 | 0 | 0 | 15 | 72.1 | 166.7/516.7 |
| 7 | 33 | 160 | 14 | -19 | 17 | 74.2 | 166.7/883.3 |
| 8 | 15 | 52 | 0 | -15 | 15 | 69.6 | 133.3/383.3 |
| 9 | 47 | 117 | 25 | -22 | 18 | 81.7 | 366.7/683.3 |
| 10 | 0 | 54 | 43 | 43 | 24 | 91.3 | 150.0/716.7 |

### Lần 3 · trễ chọn 100 ms · 8/10 đợt trong ±15 HP

| Đợt | Tụt CDP gốc | Tụt b35 cũ | Tụt b35cdp | Chênh mới−gốc | Từ xong mới | Chữ/phút mới | PX mới p50/p90 ms |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 12 | 42.6 | 166.7/233.3 |
| 2 | 0 | 74 | 0 | 0 | 16 | 63.0 | 183.3/316.7 |
| 3 | 0 | 185 | 0 | 0 | 16 | 70.9 | 183.3/333.3 |
| 4 | 0 | 56 | 0 | 0 | 16 | 76.5 | 216.7/616.7 |
| 5 | 10 | 27 | 10 | 0 | 19 | 81.2 | 366.7/883.3 |
| 6 | 0 | 117 | 0 | 0 | 15 | 72.3 | 216.7/583.3 |
| 7 | 33 | 160 | 22 | -11 | 18 | 78.3 | 216.7/783.3 |
| 8 | 15 | 52 | 71 | 56 | 17 | 80.8 | 183.3/750.0 |
| 9 | 47 | 117 | 0 | -47 | 16 | 75.0 | 183.3/700.0 |
| 10 | 0 | 54 | 6 | 6 | 24 | 86.6 | 250.0/666.7 |

### B35 cũ trên seed 1 · cùng các cột đo

| Đợt | HP đầu | HP min | Tụt | heroDamage | Từ xong | Chữ/phút | PX p50/p90 ms | Gần nhất % |
|---|---|---|---|---|---|---|---|---|
| 1 | 469 | 469 | 0 | 0 | 12 | 45.1 | 1100.0/2183.3 | 100.0 |
| 2 | 492 | 418 | 74 | 107 | 16 | 64.2 | 1433.3/1700.0 | 100.0 |
| 3 | 470 | 285 | 185 | 229 | 15 | 54.9 | 1200.0/1966.7 | 92.9 |
| 4 | 339 | 283 | 56 | 101 | 15 | 58.3 | 1383.3/1800.0 | 100.0 |
| 5 | 339 | 312 | 27 | 50 | 18 | 63.9 | 1183.3/1683.3 | 100.0 |
| 6 | 370 | 253 | 117 | 188 | 14 | 60.9 | 1166.7/2466.7 | 100.0 |
| 7 | 412 | 252 | 160 | 160 | 16 | 59.5 | 933.3/1566.7 | 100.0 |
| 8 | 465 | 413 | 52 | 75 | 14 | 61.1 | 1250.0/1716.7 | 91.7 |
| 9 | 476 | 359 | 117 | 117 | 15 | 67.2 | 966.7/1300.0 | 93.3 |
| 10 | 422 | 368 | 54 | 183 | 17 | 68.9 | 966.7/1450.0 | 100.0 |

Lần 3 còn lệch đợt 8 (**71 so với 15**, +56) và 9 (**0 so với 47**, −47). Không chỉnh tiếp. Đạt mục tiêu 8/10 không có nghĩa tái hiện mọi hit/hồi máu: botDeck khác từ vựng ghim; shop Plan khác script; mốc chụp chỉ gần đúng và RNG tay gõ khác. Bảng cơ chế dưới dùng sự kiện sim, không dùng rc-raw.hurt hỏng. Hồi máu là mức tăng HP ròng từng tick sau bù hit (gồm tăng cấp/hồi thuốc/nhà), không chỉ heal event. Trap-trigger là số sự kiện, không suy thành số quái chết.

| Đợt | B35 Héo/đòn quái/hồi | B35cdp Héo/đòn quái/hồi | Trap trigger cũ/mới | Trap kill cũ/mới |
|---|---|---|---|---|
| 1 | 0/0/23 | 0/0/23 | 1/0 | 2/0 |
| 2 | 107/0/85 | 0/0/23 | 1/0 | 2/0 |
| 3 | 229/0/98 | 0/0/23 | 91/0 | 1/0 |
| 4 | 101/0/101 | 0/0/23 | 100/50 | 0/0 |
| 5 | 50/0/81 | 10/0/33 | 102/50 | 2/1 |
| 6 | 188/0/230 | 0/0/23 | 106/72 | 4/0 |
| 7 | 160/0/135 | 53/0/53 | 123/104 | 5/9 |
| 8 | 75/0/86 | 91/0/114 | 94/88 | 2/8 |
| 9 | 117/0/63 | 0/0/0 | 109/92 | 2/3 |
| 10 | 183/0/153 | 37/0/60 | 105/123 | 1/2 |

`stepBlight` chỉ xét đợt wave, mỗi nhịp: từ quá graceTicks×graceX10/10; hoặc quái trong word zone đứng blocked/attack/hold mà không có từ. Nó cộng các suất mạnh nhất tới maxTargets, nhân √k và ramp đợt. Do đó giảm chờ chữ có thể giảm Héo rất nhiều dù luật sim không đổi. Đòn quái và bẫy/hồi làm thời điểm HP min khác tổng heroDamage. Browser không log đủ từng hit/word-complete để phân rã cùng bốn cơ chế theo đợt; không bịa số đối chiếu cơ chế cho browser. `exposure` trong JSON là proxy tick-quái trong vòng 26 m, không thay cho tính suất Héo thực.

## 6. Đo 2 × 20 seed mức Thường

Seed **20261023…20261042**, **21261026…21261045**; 20/bộ, 40/bot. Năm bot b35, b35cdp, b35human, steady, sloppy; chỉ balanced/normal. CLI **200 lượt / 4 jobs**, load trước **3,26**, thời gian **6,7 s**. Script onTick **200 lượt / 1 job**, load và thời gian chính xác ở bảng lượt chạy. G1 script khớp winPct CLI **5/5 bot**, không dùng trường G1 có sẵn để giả vờ nó đã chọn hai bot mới. Các bộ seed đều dùng 35 WPM thế giới đúng spec tương ứng.

| Bot | Bộ 20261023 | Bộ 21261026 | G1 gộp | G1 [75–90] | B4 killSeconds < sloppy | Tụt HP p50/p90 | heroDamage p50/p90 |
|---|---|---|---|---|---|---|---|
| b35 | 90.0 % | 80.0 % | 85.0 % | đạt | 4.186 · đạt | 84/228 | 125/320 |
| b35cdp | 100.0 % | 100.0 % | 100.0 % | vượt trần | 2.197 · đạt | 0/26 | 0/50 |
| b35human | 100.0 % | 100.0 % | 100.0 % | vượt trần | 3.560 · đạt | 40/140 | 67/184 |
| steady | 90.0 % | 90.0 % | 90.0 % | đạt | 4.971 · đạt | 67/214 | 118/302 |
| sloppy | 75.0 % | 75.0 % | 75.0 % | đạt | 5.234 · mốc | 63/242 | 95/387 |

| Bot | Mất khóa % | I % | S % | Chọn gần nhất n/tổng (%) | PX gộp p50/p90 ms |
|---|---|---|---|---|---|
| b35 | 1.020 | 20.5 | 57.2 | 5336/5448 (97.9) | 1166.7/1750.0 |
| b35cdp | 0.724 | 45.5 | 100.0 | 6082/6082 (100.0) | 200.0/633.3 |
| b35human | 0.931 | 24.6 | 81.8 | 5694/5757 (98.9) | 1100.0/1600.0 |
| steady | 2.740 | 18.8 | 63.6 | 5339/5436 (98.2) | 1350.0/1983.3 |
| sloppy | 1.848 | 16.4 | 57.7 | 4983/5204 (95.8) | 1050.0/1583.3 |

B35human phản xạ p50 **1.100 ms ≥154 ms** của browser khi bỏ dừng (và ≥phân vị gộp khi giữ dừng); không tạo tay phản xạ nhanh hơn bản ghi. Gần nhất thực tế của bot cũ cũng cao vì phần lớn thời gian chỉ có một từ; đó không phải trọng số target mix. Trọng số mới vẫn đo được ảnh hưởng trên nhiều seed cùng mốc born.

[Toàn bộ phân vị mỗi đợt](223/wave-quantiles.md): từng bot, số lượt tới đợt, HP đầu/min, độ tụt, heroDamage, số từ, chữ/phút, phản xạ và tỷ lệ gần nhất. `measure-waves.json` có từng lượt thô. Phân vị nearest-rank; gộp các đợt đã tới, không chèn 0 cho đợt chưa tới sau defeat. Vì vậy các đợt cuối của bot thua có ít mẫu hơn 40. B4 steady/sloppy giữ đúng code và được xác nhận bằng baseline default trước/sau 270 lượt; S=636/577 ở mẫu 40 seed này không được đánh đồng với mẫu default 3 seed.

### b35 · máu mất/phản xạ từng đợt

| Đợt | n | Tụt p50/p90 | heroDamage p50/p90 | PX ms p50/p90 |
|---|---|---|---|---|
| 1 | 40 | 6/13 | 13/24 | 1300/1967 |
| 2 | 40 | 54/151 | 87/184 | 1283/1933 |
| 3 | 40 | 142/249 | 179/327 | 1300/1883 |
| 4 | 40 | 132/333 | 219/544 | 1367/2133 |
| 5 | 40 | 62/132 | 91/195 | 1150/1517 |
| 6 | 39 | 70/240 | 117/297 | 1133/1467 |
| 7 | 39 | 134/294 | 187/432 | 1067/1517 |
| 8 | 37 | 96/187 | 136/271 | 1200/1533 |
| 9 | 36 | 85/201 | 133/388 | 1017/1467 |
| 10 | 35 | 51/149 | 147/294 | 1067/1517 |

### b35cdp · máu mất/phản xạ từng đợt

| Đợt | n | Tụt p50/p90 | heroDamage p50/p90 | PX ms p50/p90 |
|---|---|---|---|---|
| 1 | 40 | 0/0 | 0/0 | 167/233 |
| 2 | 40 | 0/0 | 0/0 | 183/283 |
| 3 | 40 | 0/0 | 0/0 | 200/517 |
| 4 | 40 | 0/0 | 0/0 | 217/617 |
| 5 | 40 | 0/20 | 0/30 | 217/733 |
| 6 | 40 | 0/0 | 0/0 | 200/550 |
| 7 | 40 | 13/40 | 14/67 | 217/683 |
| 8 | 40 | 15/30 | 30/45 | 217/667 |
| 9 | 40 | 17/50 | 17/66 | 200/567 |
| 10 | 40 | 0/65 | 37/92 | 317/900 |

### b35human · máu mất/phản xạ từng đợt

| Đợt | n | Tụt p50/p90 | heroDamage p50/p90 | PX ms p50/p90 |
|---|---|---|---|---|
| 1 | 40 | 0/7 | 6/20 | 1267/1933 |
| 2 | 40 | 15/63 | 40/96 | 1200/1833 |
| 3 | 40 | 61/190 | 98/230 | 1200/1833 |
| 4 | 40 | 56/232 | 84/298 | 1183/1917 |
| 5 | 40 | 57/107 | 71/130 | 1083/1367 |
| 6 | 40 | 57/141 | 70/164 | 1083/1383 |
| 7 | 40 | 54/120 | 54/133 | 1033/1467 |
| 8 | 40 | 44/121 | 75/165 | 1133/1417 |
| 9 | 40 | 34/151 | 50/151 | 983/1333 |
| 10 | 40 | 48/123 | 115/239 | 983/1383 |

### steady · máu mất/phản xạ từng đợt

| Đợt | n | Tụt p50/p90 | heroDamage p50/p90 | PX ms p50/p90 |
|---|---|---|---|---|
| 1 | 40 | 0/12 | 6/15 | 1467/2167 |
| 2 | 40 | 31/129 | 63/162 | 1433/2183 |
| 3 | 40 | 202/290 | 245/441 | 1467/2100 |
| 4 | 40 | 112/282 | 233/474 | 1550/2400 |
| 5 | 37 | 66/129 | 116/196 | 1367/1867 |
| 6 | 37 | 42/125 | 72/145 | 1367/1767 |
| 7 | 37 | 95/180 | 118/214 | 1200/1667 |
| 8 | 37 | 107/214 | 147/320 | 1383/1817 |
| 9 | 36 | 59/220 | 119/338 | 1217/1667 |
| 10 | 36 | 43/189 | 147/264 | 1200/1783 |

### sloppy · máu mất/phản xạ từng đợt

| Đợt | n | Tụt p50/p90 | heroDamage p50/p90 | PX ms p50/p90 |
|---|---|---|---|---|
| 1 | 40 | 0/17 | 3/17 | 1150/1850 |
| 2 | 40 | 110/265 | 140/319 | 1183/1817 |
| 3 | 40 | 80/236 | 121/401 | 1117/1717 |
| 4 | 40 | 150/370 | 287/611 | 1250/1950 |
| 5 | 33 | 73/170 | 103/255 | 1017/1400 |
| 6 | 33 | 48/144 | 72/183 | 1017/1350 |
| 7 | 33 | 90/187 | 113/356 | 933/1317 |
| 8 | 33 | 80/229 | 108/369 | 1050/1367 |
| 9 | 31 | 51/203 | 85/435 | 917/1317 |
| 10 | 30 | 52/188 | 94/286 | 950/1350 |

## 7. Thử pace và Héo lan với bot đề xuất b35human

| Biến thể | Bộ 1 | Bộ 2 | G1 gộp | Tụt HP p50/p90 | heroDamage p50/p90 |
|---|---|---|---|---|---|
| pace ×1,1 | 100.0 % | 100.0 % | 100.0 % | 41/153 | 67/220 |
| pace ×0,9 | 100.0 % | 100.0 % | 100.0 % | 32/107 | 54/147 |
| Héo Thường 1000→1100 | 100.0 % | 100.0 % | 100.0 % | 43/143 | 73/183 |

Mỗi biến thể 2×20 seed, balanced; pace chạy cả CLI có `--pace=1.1`/`--pace=0.9` và script onTick, winPct khớp cả hai. Héo chỉ đổi `PRESSURE.difficultyPm.normal=1100` **trong tiến trình measure.ts**, không dùng worker và không sửa nguồn; mỗi lần chạy mới đặt lại giá trị đã ghi. Không phối hợp các biến thể. Các kết quả đều vượt trần G1; chưa chọn một chỉnh gameplay để giữ lại.

## 8. Thời gian, tải và lệnh

Các lượt có 4 jobs đều load 1 phút <10; script đo dùng 1 job. Uptime được lưu trước mỗi lượt; script ghi trực tiếp vào JSON, CLI lưu `uptime-before-*.txt`. Không chạy nhiều nhóm balance 4 jobs đồng thời. Những lượt đo onTick đầu trước khi đổi phép đo khoảng cách sang thời điểm chọn đã được đo lại; số thắng và máu không đổi, không dùng lượt cũ cho tỷ lệ gần nhất.

| Lượt script cuối | uptime trước | jobs | số lượt | giây |
|---|---|---|---|---|
| calibration-1 | 14:59  2 users, load averages: 3.05 4.88 5.02 | 1 | 3 | 0.494 |
| calibration-2 | 15:00  2 users, load averages: 3.71 4.67 4.93 | 1 | 3 | 0.481 |
| calibration-3 | 15:00  2 users, load averages: 4.10 4.73 4.95 | 1 | 3 | 0.559 |
| measure-waves | 15:06  2 users, load averages: 7.52 5.95 5.36 | 1 | 200 | 20.315 |
| pace-1.1-waves | 15:06  2 users, load averages: 6.03 5.71 5.29 | 1 | 40 | 4.395 |
| pace-0.9-waves | 15:06  2 users, load averages: 5.71 5.65 5.27 | 1 | 40 | 4.472 |
| pressure-1.1-waves | 15:07  2 users, load averages: 5.73 5.65 5.27 | 1 | 40 | 4.546 |

| CLI | uptime trước | jobs | giây theo log |
|---|---|---|---|
| measure | 15:01  2 users, load averages: 3.26 4.47 4.84 | 4 | 6.7 |
| pace ×1,1 | 15:02  2 users, load averages: 3.06 4.16 4.69 | 4 | 2.1 |
| pace ×0,9 | 15:02  2 users, load averages: 6.74 4.90 4.95 | 4 | 2.1 |
| default-after | 15:05  2 users, load averages: 6.32 5.51 5.17 | 4 | 7.6 |

Default-before: load 1 phút **6,68**, 4 jobs, 15 bot×2 bộ×3 seed×3 mode=**270 lượt**; default-after cùng tham số và 270 lượt. Cả hai bỏ riêng steps rồi `cmp` **mã 0**. Check-before load 5,83; check-after lưu uptime riêng. Lệnh đo chính (thực thi qua nhánh node --import thay tsx CLI):

```sh
pnpm dh:balance --bots=b35,b35cdp,b35human,steady,sloppy --seed-sets=2 --seeds=20 --modes=balanced --jobs=4 --json=tmp/codex-223/measure.json
TSX_DISABLE_CACHE=1 node --import=tsx tmp/codex-223/measure.ts --bots=b35,b35cdp,b35human,steady,sloppy --out=measure-waves
```

## 9. Các dòng đã đổi trong bot.ts và run.ts

`bot.ts`: **15 thêm + 4 xóa = 19 ≤40**. `run.ts`: **8 thêm + 7 xóa = 15 ≤16**. Chép nguyên diff bên dưới; file mới không nằm trong giới hạn hai file này. Móc nhận queue hiện tại để call-early không chen trước lệnh mua của cùng tick; observe đọc sự kiện sau step; meter.scan vẫn nhận busy/releases.

```diff
diff --git a/scripts/balance/bot.ts b/scripts/balance/bot.ts
index e246b7f..016d656 100644
--- a/scripts/balance/bot.ts
+++ b/scripts/balance/bot.ts
@@ -8,7 +8,7 @@
  * (a system that does nothing yet: the report says which).
  * Owner: bot-balance (LANES.md).
  */
-import { createRng } from "../../src/kit/platform";
+import { createRng, type RngStream } from "../../src/kit/platform";
 import { RECOGNIZE, STANDARD_BOTS, TARGET_MIX, type BotSpec as KitBotSpec, type PaceSummary } from "../../src/kit/balance";
 import { STAGE_M0 } from "../../src/content/data/stages";
 import { FLOW } from "../../src/content/rules";
@@ -19,11 +19,19 @@ import { BASE_LATENCY_MS, Hands, type HandsSpec } from "./hands";
 import type { Arrival } from "./load";
 import { Meter, type RunMetrics } from "./meter";
 import { Plan, type PolicySpec } from "./policy";
-import { readTyping, type Aim } from "./reader";
+import { readTyping, type Aim, type TypingView } from "./reader";
 import { Typist, type TargetMix, type TypistStats } from "./typist";
 
 export const TICK_MS = 1000 / 60;
 
+export interface BotTypist {
+  readonly busy: boolean;
+  readonly stats: TypistStats;
+  hold(nowMs: number, ms: number): void;
+  act(view: TypingView, nowMs: number, world: World, commands: readonly SimCommand[]): SimCommand | null;
+  observe?(world: World, events: readonly SimEvent[], commands: readonly SimCommand[]): void;
+}
+
 export interface BotSpec {
   readonly name: string;
   readonly label: string;
@@ -37,6 +45,8 @@ export interface BotSpec {
   readonly directorOff?: boolean;
   /** BALANCE.md §6 id this bot stands for in the B gates (with "@good", "@poor", "@off" variants). */
   readonly standard?: string;
+  /** Opt-in typist; absent preserves the original dice and typing path. */
+  readonly typist?: (rng: RngStream) => BotTypist;
 }
 
 /** A human-like typist (BALANCE.md §6): raw E (slips cost key time), a, CV, recognition by familiarity, crowd drop, drops a lock now and then. */
@@ -195,7 +205,7 @@ export function createBotWorld(spec: BotSpec, options: RunOptions): World {
 export function runBot(spec: BotSpec, options: RunOptions): BotRun {
   const world = createBotWorld(spec, options);
   const dice = createRng((options.seed ^ nameSeed(spec.name)) >>> 0);
-  const typist = spec.hands === null ? null : new Typist(new Hands(spec.hands, dice.ai), spec.mix ?? null);
+  const typist: BotTypist | null = spec.typist ? spec.typist(dice.ai) : spec.hands === null ? null : new Typist(new Hands(spec.hands, dice.ai), spec.mix ?? null);
   const plan = new Plan(spec.policy);
   const meter = new Meter(world);
   const maxTicks = options.maxTicks ?? DEFAULT_MAX_TICKS;
@@ -222,7 +232,7 @@ export function runBot(spec: BotSpec, options: RunOptions): BotRun {
     view.nowMs = world.tick * TICK_MS;
     plan.tick(view);
     if (typist && world.phase !== "prep") {
-      const key = typist.act(readTyping(world, spec.aim, pair), view.nowMs);
+      const key = typist.act(readTyping(world, spec.aim, pair), view.nowMs, world, queue);
       if (key) queue.push(key);
     }
     const commands = queue.splice(0);
@@ -238,6 +248,7 @@ export function runBot(spec: BotSpec, options: RunOptions): BotRun {
       if (event.type === "wave-end") wavesEnded += 1;
       if (event.type === "victory") stars = event.stars;
     }
+    typist?.observe?.(world, events, commands);
     meter.read(world, events);
     meter.scan(world, typist?.busy ?? false, typist?.stats.releases ?? 0);
     options.onTick?.(world, events, typist?.busy ?? false);
diff --git a/scripts/balance/run.ts b/scripts/balance/run.ts
index 2edce8b..4fa26dc 100644
--- a/scripts/balance/run.ts
+++ b/scripts/balance/run.ts
@@ -25,12 +25,13 @@ import { M0_GATES } from "../../src/content/rules";
 import type { Difficulty } from "../../src/content/types";
 import { BAND_MODES, type BandMode } from "../../src/kit/balance";
 import { BAND_MODE } from "../../src/sim/director";
+import { findBot, type HumanBotName } from "./human";
 import { BOT_NAMES, BOTS, M0_BOTS, createBotWorld, runBot, type BotName, type BotRun } from "./bot";
 import { pacedStage } from "./variants";
 import { bandGates, m0Gates, mapNotes, markdown, planRows, readiness, summarize, type BotSummary } from "./report";
 
 interface Task {
-  readonly bot: BotName;
+  readonly bot: BotName | HumanBotName;
   readonly seed: number;
   readonly difficulty: Difficulty;
 }
@@ -53,7 +54,7 @@ const num = (name: string, fallback: number): number => {
 
 /** One run with its log dropped (reports never need it). */
 function runTask(task: Task, maxTicks: number, pace: number): BotRun & { difficulty: Difficulty } {
-  return { ...runBot(BOTS[task.bot], { seed: task.seed, maxTicks, timeSteps: true, stage: pacedStage(STAGE_M0, pace), difficulty: task.difficulty }), difficulty: task.difficulty };
+  return { ...runBot(findBot(task.bot)!, { seed: task.seed, maxTicks, timeSteps: true, stage: pacedStage(STAGE_M0, pace), difficulty: task.difficulty }), difficulty: task.difficulty };
 }
 
 const trace = arg("trace");
@@ -69,8 +70,8 @@ if (args.includes("--worker")) {
   });
 } else if (trace) {
   const [bot, seed] = trace.split(":") as [BotName, string?];
-  if (!(bot in BOTS)) throw new Error("không có bot " + bot + "; có: " + BOT_NAMES.join(", "));
-  const run = runBot(BOTS[bot], { seed: Number(seed ?? STAGE_M0.seed), maxTicks: Math.round(num("max-minutes", 60) * 3600), timeSteps: true });
+  if (!findBot(bot)) throw new Error("không có bot " + bot + "; có: " + BOT_NAMES.join(", "));
+  const run = runBot(findBot(bot)!, { seed: Number(seed ?? STAGE_M0.seed), maxTicks: Math.round(num("max-minutes", 60) * 3600), timeSteps: true });
   const { arrivals, log, hashes, ...rest } = run;
   console.log(JSON.stringify({ ...rest, arrivals: arrivals.length, w: arrivals.reduce((sum, a) => sum + a.w, 0) }, null, 1));
 } else {
@@ -87,9 +88,9 @@ async function main(): Promise<void> {
   const pace = num("pace", 1);
   const modes = (arg("modes")?.split(",") ?? [...BAND_MODES]).filter((mode): mode is BandMode => (BAND_MODES as readonly string[]).includes(mode));
   // Every bot by default: the M0 gate bots and BALANCE.md §6's set with the B6, B7 variants (`--set=m0`: the gate bots only).
-  const bots = (arg("bots")?.split(",") ?? (arg("set") === "m0" ? [...M0_BOTS] : BOT_NAMES)).filter((name): name is BotName => {
-    if (!(name in BOTS)) console.error("không có bot " + name + "; có: " + BOT_NAMES.join(", "));
-    return name in BOTS;
+  const bots = (arg("bots")?.split(",") ?? (arg("set") === "m0" ? [...M0_BOTS] : BOT_NAMES)).filter((name): name is BotName | HumanBotName => {
+    if (!findBot(name)) console.error("không có bot " + name + "; có: " + BOT_NAMES.join(", "));
+    return !!findBot(name);
   });
   const tasks: Task[] = modes.flatMap((mode) =>
     bots.flatMap((bot) => bases.flatMap((first) => Array.from({ length: seeds }, (_, k) => ({ bot, seed: first + k, difficulty: DIFFICULTY_OF[mode] })))),
```

## 10. Bảy mục kiểm và bàn giao

| Mục | Kết quả có số |
|---|---|
| 1 · Golden | MD5 trước/sau 75f74947dac170d05fd659f99417940e; golden 10/10 trong cả hai check; b35/noTyping/sloppy giữ log cũ |
| 2 · Phạm vi | 181 file src/golden trước/sau; 0 khác; status 56=51 cũ+5 cho 223; 0 lạ; diff cũ giữ nguyên=True; HEAD giữ nguyên=True; bot.ts 19/40, run.ts 15/16 |
| 3 · pnpm check | Trước mã 0: 69 file/593 test; sau mã 0: 70 file/607 test=593+14; 0 đỏ; kit 75; TypeScript/build xanh. Đỏ trước mã: 1 suite thiếu module, 0 test được nạp. |
| 4 · Bot cũ | 15 BOT_NAMES, 6 M0_BOTS và Object.keys giữ thứ tự; bots-before/after giống; default trước/sau 270 lượt bằng nhau sau bỏ steps, cmp=0. |
| 5 · Hiệu chỉnh | Ba cấu hình 0/50/100 ms đạt 7/10, 7/10, 8/10. Có thêm 1 lượt dò lỗi call-early trước hiệu chỉnh (4 lượt đầy đủ nếu tính tất cả); đã công khai ở §5. Từ browser không đo được số hoàn tất; poll và PNG chỉ xấp xỉ. |
| 6 · Đo | 5 bot ×2×20 balanced=200 lượt mỗi đường CLI/onTick; G1 khớp 5/5. B4 4,186/2,197/3,560 <5,234 s, steady S 636>577. Ba biến thể mỗi cái40seed,100% thắng. |
| 7 · Dọn | tmpdir đã xóa; 16 JSON thô chép vào 223, 0 SHA-256 lệch; 0 ảnh chụp nên không chạy capture-prune. |

Không sửa source gameplay, golden, file 187/194/195/197, bot mặc định hoặc game/worktree khác; không Git ghi. Diff cũ giữ byte-for-byte. Không cần tạo ảnh/âm thanh trong nhiệm vụ này. Bỏ qua thử shop và bộ từ ghim vì đã đủ ba cấu hình hiệu chỉnh; không tăng số thử để ép đợt 8/9 khớp. Không có dữ liệu trực tiếp để đo chính xác poll/PNG và từ hoàn tất browser, nên giữ `null`/giả định có nhãn.

**Claude cần xem:** diff hai móc và human.ts; mức gần đúng của các khoảng dừng; lượt dò lỗi thêm ngoài ba cấu hình hiệu chỉnh; chấp thuận bot đại diện G1/B4. G1 mới 100 % không đạt dải 75–90 %, nên không coi phiếu là đã cân bằng gameplay. Owner vẫn là người duyệt cuối. Chưa commit.

Bằng chứng tối thiểu đã đủ file yêu cầu: start-status/start.diff/src-before/src-after; bots-before/bots-after; default-before/default-after; check-before/check-after/tests-red; browser.mjs/measure.ts/browser-waves; calibration-1/2/3; measure.json; status-final. Bổ sung measure-waves và ba bộ pace/pressure, [wave-quantiles.md](223/wave-quantiles.md), [verification.json](223/verification.json), [raw-sha256.json](223/raw-sha256.json). JSON trong repo cha khớp bản tmp; script và log chỉ nằm trong các đường được phép. Các kiểm kỹ thuật đạt như bảng; phần cần duyệt và giới hạn dữ liệu/quy trình nêu rõ, không tuyên bố nghiệm thu hoàn hảo toàn bộ phiếu.
