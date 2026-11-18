# Phiếu 434f — Lôi dùng lại sét dày Ngũ Lôi

Ngày 17/11/2026. **Chưa đạt toàn bộ nghiệm thu.** Đã làm đủ 4 vòng sửa → chụp → mở ảnh → đối chiếu, rồi dừng đúng giới hạn phiếu. Cột chính đạt 40 px; dây chuyền đạt ở 6/8 bước, nhưng hai bước cuối còn dưới 14 px. Không ghi PASS mỹ thuật hoặc coi đây là bản được chấp nhận tạm.

## Giao nộp

- [Ảnh thunder-codex-f.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-f.jpg): phân cảnh 431 cạnh camera chơi và sau lưng, các mốc 0,4 / 1,2 / 2,2 / 3,0 s.
- [Video thunder-codex-f.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-f.mp4): 1280×720, H.264, 30 fps, 120 khung, 4,000 giây; giữ AAC 4,000 giây của 434e, cùng mốc đánh 2,0 s.
- [Từng bước dây chuyền](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434f/round-4/hop-check-sheet.jpg), [diễn tiến đất](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434f/round-4/ground-sheet.jpg), [khung giải mã video](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434f/round-4/video-decoded-sheet.jpg).
- [Đối chiếu Ngũ Lôi và nguồn của nó](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434f/nguloi-reference-sheet.jpg).
- [Số đo cuối](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434f/round-4/measure.json), [cổng nghiệm thu](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434f/final-gates.json), [vòng đời tài nguyên](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434f/lifecycle.json).

Đã thêm dòng 434f vào `owner-review/2026-11-17/tu-tien/ABOUT.md`; giữ toàn bộ ảnh/video cũ.

## Mã đã ghi

Chỉ bốn file dưới `games/.wt-ic-lab-all/src/lab/`:

| File | Thay đổi |
| --- | --- |
| `thunder-ult-nguloi.ts` | Nạp trực tiếp nguồn, lưới atlas và pivot từ các export của `five-thunder.ts`. Đặt card giữa hai đầu thế giới; nhuộm tím–trắng lúc render. Cột dùng `columnA` + `columnCoreA` từ `thunder-columns-mix`, ping-pong hàng video đầu ở 12 fps. Chân có `burst`, `lichtenberg`, `scarHot` chuyển sang `scarCold`. |
| `thunder-ult-chain.ts` | Thay thân sét lớn, dây chuyền và nhánh đất bằng lớp art mới; bỏ nạp vết nứt cũ và burst cũ không còn dùng. Giữ lựa chọn quái, nhịp zíc zắc, mây, ánh hắt tím, âm và dư điện. |
| `thunder-ult-review-f.mjs` | Chụp hai camera, ảnh đối chứng tắt art/tắt riêng từng tia, probe cắt ngang, alpha mây, stress 100 quái và quét trắng 480 khung. |
| `thunder-ult-probe-f.mjs` | Kiểm nạp nguồn thật, không nạp decal cũ, hủy/lặp, pool ổn định và giải phóng đủ texture. |

Không sửa `five-thunder.ts`, flipbook, file ảnh nguồn hay `cloud-volume*`. Công cụ tạo hình là **art Ngũ Lôi đã có**, theo `game-vfx-production` và `game-vfx-layered`; không tạo ảnh hoặc âm mới, nên không dùng image_gen. Không sửa mã game chính, `skills-main.ts`, tài liệu Tu Tiên hay audio-lab.

Bản cuối dùng `boltA`/`boltB` luân phiên cho thân dây chuyền. C/D đã thử ở vòng 1–3 nhưng không giữ làm thân vì quá mảnh khi kéo theo đoạn nối. Bốn nguồn A–D vẫn dùng cho `crawlA`–`crawlD`; crawl chia sẻ texture với bolt, không nạp hai lần. Hai atlas A/C có phần đệm chân lớn: hiệu chỉnh pivot khi gắn vào pool, không đổi file nguồn.

Cột rộng card 4,2 m, nối từ gốc mây Y = 7 m xuống Y = 0,08 m; độ rộng card chỉ là tham số đặt hình, **không dùng thay số đo pixel**. Tám nhánh crawl dài 3,67–5,80 m nằm trên Y = 0,08 m; giữ sáng 0,18 s và mờ 0,32 s, lệch khởi đầu tối đa 1/60 s. Hot scar chuyển lạnh trong khoảng 0,15–0,70 s sau đánh; dư âm đất mờ trong 1,5 s và hết ở 4,0 s. Không dựng sao hay vòng cho vết đất.

## Bốn vòng

Mọi vòng: Chrome headless, localhost:3148, High, DPR 1, 1280×720, nền `#353a40`. Mỗi vòng đều đo p95 trên stress đủ 87 TargetField + 13 walker, 4×240 mẫu; bỏ lượt đầu, gộp 720 mẫu. `total` gồm CPU và chờ GPU qua `readPixels`.

Probe cắt vuông góc đoạn nối tại 35%, 50%, 65%; đếm **dải liên tục dài nhất có Rec.709 tăng ≥0,1** so với ảnh cùng khung tắt art. Không lấy toàn khoảng giữa các nhánh rời nhau. Vòng 3–4 tắt riêng từng nguồn khi đo để loại ảnh hưởng của tia khác; đây là phép đo chặt hơn vòng 1–2. Các số trong bảng là min–max của những lát cắt đã chụp, không khẳng định là độ rộng mọi khung trong lúc tan.

| Vòng | Thân cột (px) | Thân dây tại các mốc pha (px) | Trắng tối đa tại mốc pha | p95 (ms) | Kết quả nhìn/đo |
| --- | --- | --- | --- | --- | --- |
| [1](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434f/round-1/comparison-sheet.jpg) | 92–225 | 1–8 | 1,106228% | 15,70 | Cột đã dày, dây còn mảnh; probe bật/tắt được sửa đúng tiền tố mesh và đo lại trước vòng 2. |
| [2](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434f/round-2/comparison-sheet.jpg) | 74–183 | 7–70 | 0,768772% | 6,20 | Giảm bề ngang cột, tăng thân và lõi dây; D còn dưới ngưỡng. |
| [3](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434f/round-3/comparison-sheet.jpg) | 74–183 | 0–70 | 0,768772% | 6,00 | Tăng riêng D; đo từng bước phát hiện C/D cuối vẫn thiếu. |
| [4](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434f/round-4/comparison-sheet.jpg) | 74–183 | 1–70 | 0,768772% | 7,50 | Dùng A/B cho dây; 6 bước đạt, 2 bước cuối chưa đạt. Dừng ở giới hạn bốn vòng. |

Vòng 4, tắt riêng nguồn, lấy giá trị nhỏ nhất của ba lát cắt tại 0,05 s sau mỗi bước:

| Bước | Nguồn | Mốc (s) | Thân nhỏ nhất (px) | ≥14 px |
| --- | --- | --- | --- | --- |
| 1 | A | 0,65 | 81 | Đạt |
| 2 | B | 0,75 | 17 | Đạt |
| 3 | A | 0,85 | 31 | Đạt |
| 4 | B | 0,95 | 35 | Đạt |
| 5 | A | 1,05 | 29 | Đạt |
| 6 | B | 1,15 | 32 | Đạt |
| 7 | A | 1,25 | 3 | **Chưa đạt** |
| 8 | B | 1,35 | 1 | **Chưa đạt** |

Góc đổi hướng giữ nguyên: +52,40 / −63,71 / +45,47 / −52,31 / +76,49 / −64,54 / +48,10°. Không đổi thuật toán chọn quái để làm đẹp số đo.

## Kiểm tra và phần còn lại

- `./node_modules/.bin/tsc --noEmit --incremental false`: **0 lỗi**.
- `node --import tsx src/lab/thunder-ult-probe-f.mjs`: **PASS**. Hủy/lặp 5 lần, không tăng hình học/vật liệu, không rơi pool; 16 texture được giải phóng đúng một lần, dispose lặp an toàn.
- GPU: **ANGLE Metal Renderer: Apple M4**; p95 cuối **7,50 ms ≤16,7 ms**.
- Quét đủ **480 PNG không mất dữ liệu**: 240 khung/60 Hz cho mỗi camera. Gộp cả các mốc pha, trắng cả RGB ≥0,95 tối đa **0,768772%**, Rec.709 ≥0,95 tối đa **0,829753%**, đều dưới 6%.
- Mây alpha ≥0,5 vẫn chiếm **15,56–22,78%** trên khung chơi; phủ tâm quái **0** tại bốn mốc. Sau lưng **31,11–31,67%**. Giữ nguyên bố trí 434e.
- Không exception trong lượt cuối. Còn cảnh báo host về nhiều KTX2Loader, atlas Kim và nhiều bản Three trong probe; không sửa lane khác.
- Đã mở ảnh cả bốn vòng, Ngũ Lôi trong lab, từng bước dây, diễn tiến đất và sheet giải mã MP4. Clip đã kiểm đúng 120 khung/4 giây.

**Owner cần xem:** cột chính dày hơn rõ rệt, nhưng dây chuyền còn không đều; hai bước cuối chưa đạt và cách nối card còn cần xử lý tiếp. Vết đất mới dùng đúng art Ngũ Lôi nhưng khá chìm ở camera chơi, chưa có hai giám khảo mù chấm 8,5.

Ở khung đánh còn một đốm nổ xanh–đen hình sao của lớp khác trong host. [Đối chứng bật/tắt toàn bộ art 434f](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434f/round-4/host-control-sheet.jpg) cho thấy nó vẫn còn khi tắt cột, burst, crawl và scar mới. Không sửa lớp ngoài phạm vi phiếu; không gọi đốm đó là vết đất Ngũ Lôi.

Không chạy build hoặc bộ test game, không khởi động/dừng server, không commit/push/reset/clean/stash. Không làm vòng thứ năm. Chưa hoàn thành điều kiện dây chuyền nên **không đề nghị nghiệm thu**.

## Dọn khung

Đã chạy capture-prune khô rồi áp dụng: xóa **744 ảnh thô, 663,511 MB**, không mục nào bị từ chối. Hai ảnh mẫu nguồn đã được ghép vào sheet rồi xóa. Các khung thô của riêng 434f được xóa bằng capture-prune sau khi ghép sheet, xuất clip và lưu số đo; giữ sheet, MP4, JSON và ABOUT. Đã dựng lại chỉ mục review. Số lượng xóa được ghi trong `captures/tu-tien/thunder-ult-434f/prune-apply.json`.
