# Tu Tiên Thủ Ải — 00. Luật chuẩn, số chuẩn, từ điển (25/10/2026)

> **Vai của tài liệu này:** nguồn chân lý duy nhất của game trước khi có mã: tên, quyết định, luật, công thức, bảng số, bảng phím, ngân sách chữ, cổng bot, ngân sách hiệu năng.
> **Thứ tự ưu tiên khi lệch:** tệp này → [`DANH_GIA_2026-10-24.md`](DANH_GIA_2026-10-24.md) (lý do, đánh giá) → `analysis/01–08` (đầu vào). Mục 8 và Phụ lục A của tệp đánh giá đã vào tệp này. Ai thấy lệch thì sửa tệp thua, không thêm luật mới.
> **Lượt sửa 25/10 theo phản biện** [`analysis/09-phan-bien-canon.md`](analysis/09-phan-bien-canon.md): mọi mục **chặn** và **lớn** (PB-01 đến PB-26) và mọi mục **nhỏ** (PB-27 đến PB-37) đã vào tệp này; quyết định mới là D32–D46 ở mục 3. Chỗ sửa ghi mã `PB-xx` để dò lại.
> **Số:** mọi số là **số thử** cho tới khi bot (`kit/balance`) và buổi chơi thử của anh chốt. Khi viết mã, số chuyển vào `src/content/rules.ts` của `games/immortality-cultivation`, mỗi khóa trỏ về mục ở đây. Bot chỉnh số trong dữ liệu; luật không đổi khi chỉnh số.
> **Ký hiệu:** "(nguồn: …)" là luật chép từ tài liệu khác. **Anh chọn** là quyết định của chủ dự án. **Đã chọn theo đề xuất** là quyết định theo luật "làm theo đề xuất" của anh (17/10); anh đổi được bất cứ lúc nào.
> **Không chép** tên, UI, hình, cốt truyện của Quỷ Cốc Bát Hoang (QCBH, Tale of Immortal). Mọi tên ở đây là tên của dự án, tạm.

## 0. Định danh

| Mục | Giá trị |
|---|---|
| Tên | **Tu Tiên Thủ Ải** (tên tạm; chốt khi anh duyệt 2 ảnh bản sắc ở M0b) |
| Repo | `sinhvienaiti/immortality-cultivation` (anh tạo 25/10), submodule `games/immortality-cultivation` của repo cha |
| `gameId` | `immortality-cultivation`. Ghi vĩnh viễn vào sự kiện học; không đổi khi đổi tên game |
| Cổng dev | **3008** (`--strictPort`; 3000–3007 đã dùng) |
| Host | `tutien.typing-game.local` (dev qua nginx và play) |
| Tài liệu thiết kế | `docs/games/tu-tien/` ở repo cha (như `dragon-lane/` của Rồng Giữ Ải); chuyển vào `games/immortality-cultivation/docs/design/` ở M1, repo cha giữ một dòng trỏ |
| Khóa lưu cục bộ | `immortality-cultivation.save`, `.skill`, `.settings`, `.newwords` (cấu trúc và chuyển đổi: mục 23.1) |
| Đối tượng | Thiếu niên trở lên. Hồ sơ trẻ em: preset Thư giãn, giọng nhẹ, không chat |
| Giọng | Tu sĩ trấn ải: nghiêm mà ấm. Không máu, không kinh dị. Tâm ma, thiên kiếp là hình tượng, không dọa |
| Bối cảnh | **Biên Ải**: dải ải giữa nhân giới và vùng hoang thú; tông môn của người chơi trấn giữ. Phe địch là linh thú nhiễm **trọc khí**. Chỉ là bối cảnh cho màn chọn trận, không có bản đồ du hành |
| Hướng hình | **3D trước, có đo** (anh chọn 25/10, D03; mục 20–21) |
| Bản sắc (chờ anh duyệt 2 ảnh) | "Sơn thủy huyền ảo" chất Việt: hẻm đá vôi dựng đứng, sương chàm, mực và giấy dó; điểm sáng linh quang trắng ngà; đỏ son chỉ ở dấu triện UI |

**Ba điểm khác các game hiện có** (lý do là game riêng; mọi luật khác chép có nguồn):

1. Nhân vật **tự đi** trên sân (chuột phải, mũi tên).
2. Gõ vào **Bàn Quyết** (thanh kỹ năng), không gõ lên từng con quái. Quái thường không mang chữ.
3. **Chơi đội 2–3 người**, bot lấp ghế. Solo làm trước.

So với Rồng Giữ Ải (cùng "giữ ải theo đợt, cửa hàng, cơ quan"): Rồng là rừng ấm cho trẻ nhỏ, Rồng đứng yên, chữ trên quái, một người. Tu Tiên cho thiếu niên trở lên, người đi lại, chữ trên Bàn Quyết, có đội.

## 1. Ai giữ hệ nào

| Tệp | Giữ |
|---|---|
| `00-canon.md` (tệp này) | Mọi luật, số, phím, ngân sách chữ, cổng, ngân sách hiệu năng. Thắng mọi tệp khác |
| [`M0A_PLAN.md`](M0A_PLAN.md) | Kế hoạch xây M0a và bản thử Tĩnh Tu: khung repo, nối repo cha, làn, thứ tự, cổng |
| [`DANH_GIA_2026-10-24.md`](DANH_GIA_2026-10-24.md) | Lý do, đánh giá Codex V2.2, rủi ro, câu hỏi đã trả lời |
| `analysis/01–08` | Đầu vào đã giải mâu thuẫn; không còn là luật |
| [`analysis/09-phan-bien-canon.md`](analysis/09-phan-bien-canon.md) | Phản biện tệp này và kế hoạch M0a (25/10); đã áp vào cả hai, giữ làm nhật ký lý do |
| `games/immortality-cultivation/{AGENTS,LANES}.md` | Luật làm việc trong repo game (viết ở bước dựng khung) |

Tệp hệ chi tiết (chiến đấu, thú, kinh tế…) chỉ viết khi M0a có số đo. Tới lúc đó tệp này giữ mọi luật.

## 2. Từ điển

| Dùng | Không dùng nữa | Nghĩa |
|---|---|---|
| Tu Tiên Thủ Ải, `immortality-cultivation` | `tu-tien` làm `gameId` hay tên repo | Tên tạm và id. Thư mục tài liệu giữ tên `tu-tien/` |
| Biên Ải | — | Bối cảnh: dải ải giữa nhân giới và vùng hoang thú |
| Ải | "Thú Triều" như một lượt nhiều trận (`01`) | Một địa danh. **Một ải = một chương = một cảnh giới** |
| Trận | lượt, ván, run | Một lần chơi một màn gồm các đợt |
| Đợt | sóng | Một nhịp thú tràn vào (40–60 s) |
| Thú triều | — | Thú tràn vào theo đợt |
| Đại Triều | — | Trận cuối chương: 7 đợt, Thú Vương, Thiên Kiếp (D37) |
| Trận Tâm | Hộ Ải Đại Trận, trận bàn | Lõi trận giữa ải, giữ Trận Lực |
| Trận Lực | Hộ trận, máu lõi | Thanh máu chung. Về 0 là thua |
| Kết Giới | vùng trận | Vùng r 9 m quanh Trận Tâm có gia trì |
| Trận nhãn (Công, Thủ, Dưỡng) | trận vị (tọa độ), cung ải | Vai của một ghế. Có một điểm trên đất để thú chiếm; **không khóa vị trí người** |
| Tâm nhãn | — | Nhãn gộp ba tác dụng khi chơi một mình |
| Trận Trụ | đá trụ, Thạch Bích (nay là chiêu của Thổ thể) | 2 cột đá làm vật che |
| Ô cơ quan | ô đặt | 6 ô cố định trên sân |
| Cơ quan | bẫy, trận kỳ | Vật đặt lúc bày trận và lúc nghỉ, tự kích hoạt |
| Kiếm Thung, Lôi Phù Trụ, Phong Ấn Võng, Mê Vụ Trận | — | Bốn cơ quan MVP (mục 8.3) |
| Hợp Trận | hợp kích, Kết Ấn (ô 6 của `05`) | Đòn chung của đội khi đủ nhãn (từ M1) |
| Trận Quyết | Kết Ấn | 2 từ riêng mỗi người gõ để kích Hợp Trận |
| Nạp nhãn | Trận Ý | Số từ người giữ nhãn cần gõ để nhãn sẵn sàng |
| Bàn Quyết | Bàn Ấn (`07`), thanh kỹ năng | Dải DOM ở đáy màn chứa từ của các ô |
| Ô 1–5 | — | Liên tục, Chiêu A, Hộ thân hoặc thân pháp, Chiêu B, Tuyệt kỹ (mục 6.3) |
| Đánh nền | auto attack, võ kỹ | Đòn tự động không chữ của trường phái |
| Chân Nguyên | Linh lực, Định Tâm, Niệm lực | Thanh duy nhất trong trận, dùng cho tuyệt kỹ |
| Ấn | Ấn chữ, Cụm Ấn, Ấn Phá | Từ trên tinh anh, thú tướng, Thú Vương; gõ để giảm Thế |
| Thế, phá thế | vỡ thế | Thanh tư thế của địch; về 0 thì địch ngã 6 s |
| Tẩy | — | Từ ngắn lấy lại nhãn bị thú chiếm (không bắt buộc) |
| Chữ khẩn | Từ Khẩn | Suất chữ gấp, tối đa 1. MVP chỉ có Tẩy |
| Chữ sống | — | Từ gõ được ngay lúc đó. Từ mờ của ô đang hồi **không** là chữ sống |
| Bàn Quyết sống | — | Khoảng Bàn Quyết nhận phím: từ báo đợt tới hết đợt, và pha Vương (mục 6.1, D42) |
| Cast | — | Giao dịch tung chiêu của một từ (mục 6.1) |
| `ward` | vùng Hộ thân | Vật thế giới Hộ thân đặt tại `origin` của Cast: r 2 m, 5 s, 3 lần đỡ (mục 12.1, D34) |
| Từ nền | từ "đã thuộc" giả định | ≤ 40 từ dễ dùng cho hồ sơ trống, cờ `assumed` (mục 17.1, D35) |
| Sổ cái từ mới | ngân sách từ mới, `budgetLedger` | `NewWordLedger`: đếm từ mới trong cửa sổ trượt 20 phút (mục 6.4, D39). Khác `BudgetLedger` của kit (trần chữ sống) |
| Chế độ cửa hàng | — | Lúc bày trận và nghỉ, phím `` ` `` mở; mũi tên chọn món và ô (mục 5.1, D45) |
| Chớp, Hoàn hảo, Tốt, Vừa, Ẩu | Chuẩn/Nhanh (`03`), Bạo kích, Hội tâm | Kết quả một từ (mục 6.5) |
| Bầy, Nhỏ, Vừa | Tiểu yêu, T1/T2 | Bậc thú thường |
| Tinh anh | tinh thú, yêu tướng (`03`) | Thú thường mang 1 thuộc tính tinh anh, Thế 40, 1 Ấn |
| Thú tướng | Đội trưởng (Rồng) | Thú chỉ huy có hào quang, Thế 60, 1 Ấn |
| Thú Vương | boss | Boss cuối Đại Triều: 3 pha, thanh Thế |
| Biến chủng hệ | — | Bản đổi hệ của một họ thú: cùng GLB, đổi dữ liệu và chất liệu (D23) |
| Trọc khí | Hắc Vụ (Rồng) | Khí làm linh thú hóa dữ. Thú chết tan thành khói mực và đốm linh quang |
| Thiên Kiếp | Độ Kiếp, Độ Kiếp Đài (`01`) | Pha đột phá gộp vào cuối Đại Triều |
| Lôi Kiếp | — | Sét đánh vào ô đất có báo trước, trong Thiên Kiếp |
| Chấp Ảnh | tâm ma của Độ Kiếp (`01`) | Bóng mang từ yếu của chính người chơi, trong Thiên Kiếp |
| Kiếp Lực | — | Thanh riêng của pha Thiên Kiếp |
| Cảnh giới, kỳ | — | 7 cảnh giới × 3 kỳ (sơ, trung, hậu) |
| Tu vi | — | Thanh kinh nghiệm để lên kỳ. Không phải tiền |
| Đạo Quả | Đạo Ấn (`01`), Mệnh cách, Khí Vận, Hung Cát | Lựa chọn vĩnh viễn khi đột phá: 1 trong 3 |
| Cơ Duyên | — | Lựa chọn 1 trong 3, chỉ sống trong một trận |
| Công pháp | bí kíp, sách kỹ năng | Bài 6 từ gắn với một chiêu; lớn lên 3 tầng |
| Khẩu Quyết | — | 6 từ mới của một công pháp; thẻ học trước phiên Tĩnh Tu |
| Lĩnh ngộ | — | Đạt 100 điểm Tĩnh Tu: công pháp lên tầng 1 |
| Ngộ Chiêu | "Tham ngộ" khi nói về biến chiêu | Chọn 1 trong 2 biến chiêu ở tầng 2 (D24) |
| Tâm pháp | — | Ô bị động, không chữ |
| Tĩnh Tu | tĩnh tọa, mini-game tu luyện | Mini-game học 6 từ của công pháp |
| Nhập Môn, Tham Ngộ, Minh Tâm | Ngộ Đạo (`07`, là tên cảnh giới của QCBH) | Ba bậc Tĩnh Tu |
| Minh, Thường, Tâm ma | Tạp Niệm (`01`), cầu ngộ, cầu ma | Ba loại chữ trong Tĩnh Tu |
| Linh Sa | Trận Nguyên (`05`), Vàng | Tiền trong ải, mất khi hết ải |
| Văn Khí | Tri Thức (Rồng) | Tiền giữ mãi, chỉ từ học |
| Thú Hạch | Linh Thạch, Yêu Đan, Thú hồn, Tàn trang, Công Huân | Tiền giữ mãi, từ thắng và boss |
| Linh Dịch | bình máu (Rồng) | Vật bộ điều nhịp thả khi gần thua: +5 % Trận Lực |
| Sơn Môn | Doanh Trại, Làng | Hub: một màn tĩnh 4 điểm |
| Trận Đài, Tĩnh Thất, Thư Lâu, Bảo Khí Lò | Tàng Kinh Các, Đan Các, Luyện Khí Phòng, Độ Kiếp Đài | Bốn điểm của Sơn Môn |
| Pháp bảo | pháp khí | 1 ô Pháp Bảo Bản Mệnh, món cố định, cấp 1–5 |
| Đan, phù | Hành Nang (bộ mang theo) | Đồ tiêu hao dùng bằng phím 1/2/3, không chữ |
| Học trước, Thẻ Ôn, Sổ Từ | Chợ Học | Học trước trận; ôn lúc nghỉ; sổ từ khi kết trận |
| Thu Hoạch | Kết trận | Màn kết: học và RPG báo tách dòng |
| Độc tu, Lưỡng Nghi, Tam Tài, Thất Tinh | Tứ Tượng, Ngũ Hành (bỏ) | Trận 1, 2, 3, 7 ghế |
| Ghế | vị | Chỗ của một người thật hoặc một bot |
| Bot đạo đồng | — | Bot lấp ghế trống |
| Phân thân bạn đạo | — | Bản sao bất đồng bộ của bạn ngồi ghế bot (M2) |
| Thư giãn, Cân bằng, Thử thách, Học | tên preset riêng của `01`, `04` | Bốn preset, theo `BALANCE.md` |
| Nhàn quyết định | — | Cách game đo Nhàn I (mục 18.2) |
| D_ref, D_đơn | W_gõ dùng làm tải đợt | Sức ra đòn chuẩn trên sân trộn và lên một mục tiêu (mục 7.4) |
| HN0, HN1 | — | Cổng bench 3D (M0a) và cổng hiệu năng có hình thật (M0b) |
| Ngân sách con, phần vượt | — | Phần khung p95 dành cho nền, đám đông, kiếm và VFX, có xương; phần nào vượt thì phần đó lùi (mục 20.3, D36) |
| ĐĐ (phần đe dọa) | — | Trọng số chia 60 % Linh Sa hạ thú (mục 14.2) |
| VAT | — | Kết cấu hoạt ảnh đỉnh (vertex animation texture) cho đám đông |
| Impostor | sprite nướng | Ảnh 2D nhiều hướng nướng từ cùng GLB, vẽ bằng quad instanced |

## 3. Sổ quyết định (24–25/10/2026)

| # | Quyết định | Nguồn, lý do |
|---|---|---|
| D01 | Định danh ở mục 0: repo `sinhvienaiti/immortality-cultivation`, thư mục `games/immortality-cultivation`, `gameId` `immortality-cultivation`, cổng 3008, host `tutien.typing-game.local`, tài liệu ở `docs/games/tu-tien/` | Anh tạo repo (25/10). Thay `games/tu-tien`, `gameId` `tu-tien` của tệp đánh giá. `gameId` phải chốt trước sự kiện học đầu tiên |
| D02 | **Làm ngay** (anh chọn 24–25/10): M0 canon → M0a hộp xám → bản thử Tĩnh Tu song song. Việc cần giờ của anh (Tripo, Bảng Nghe, chơi thử) xếp sau Rồng Giữ Ải qua B9 | Câu 1 mục 8 tệp đánh giá; giờ của anh là nút thắt chung |
| D03 | **Hướng hình 3D trước, có đo** (anh chọn 25/10, hai tin, ý chính: 2D làm nền vì nhẹ và mạnh hiệu ứng, chỗ nào làm được 3D thì đề xuất và triển khai; rồi: skill, quái sẽ nhiều và rộng, như "vạn kiếm quy tông" triển khai rất nhiều kiếm, nếu đo được vẫn ổn khi là 3D thì cứ triển khai, vì anh cũng thích 3D). Một renderer Three.js chung (kit `three`), camera 3/4 cố định thấy cả ải, vẻ thủy mặc bằng shading, hậu kỳ và VFX. **Bench HN0 làm trước mọi hình.** Phần nào trượt ngân sách (nhiều khả năng là đám đông) xuống impostor 2D nướng từ cùng GLB; phần còn lại giữ 3D (cách đo từng phần: D36). Người chơi, bot, thú tướng, Thú Vương và chiêu lớn luôn là 3D thật (có xương) | Thay câu 3 mục 8 và mã E2 Phụ lục A của tệp đánh giá (đề xuất lai, chờ A/B). Mục 20–21 |
| D04 | Game mới, không phải mode của Rồng Giữ Ải | Tệp đánh giá §1.2 |
| D05 | Không làm "QCBH bỏ bản đồ": tối đa **4 hệ lâu dài** (cảnh giới, công pháp, pháp bảo cố định, Thư Lâu); Sơn Môn một màn tĩnh 4 điểm; **3 tiền**. Muốn thêm hệ hay tiền thì phải bỏ một cái cũ | Tệp đánh giá §1.3, R9 |
| D06 | Phạm vi MVP (hết M1): Độc tu và Độc tu + 2 bot (Tam Tài); 1 chương = 1 ải (3 trận dạy, 2 trận trộn, Đại Triều); 2 trường phái (Kiếm ở M0a, Thổ thể ở M1); 2 cảnh giới (K0, K1); Tĩnh Tu Nhập Môn + Tham Ngộ; **chỉ Typing** | Tệp đánh giá §1.4, câu 16, 21 |
| D07 | **Luật nhắm mục tiêu:** thú không bao giờ đuổi theo hay va chạm với người thật; solo dùng cùng luật (mục 10.1) | Câu 7; mã D1 |
| D08 | **Hợp đồng Cast** có ID làm từ M0a; một từ = một Cast (mục 6.1) | Codex §1.4 |
| D09 | Đòn gõ bỏ qua Giáp. **Không có chí mạng ngẫu nhiên.** Chớp tính theo nhịp riêng của từng người | (nguồn: Rồng D03); câu 15 |
| D10 | **Một công thức báo trước** cho mọi đòn có đáp án gõ, có test dữ liệu (mục 10.6) | Tệp đánh giá §3.4; mã C5 |
| D11 | **Ngân sách từ mới chung** ≤ 8 từ mỗi 20 phút, tính chung Học trước, Tĩnh Tu, Chiêu B (mục 6.4) | Câu 18; mã C1 |
| D12 | Bậc hình (Low, Medium, High) **không đổi luật sim**: trần chữ, trần thú sống, máu, nhịp là hằng số | (nguồn: Rồng D10) |
| D13 | **Tải đợt tính theo sức ra đòn chuẩn D_ref**, không theo số từ (đã chọn theo đề xuất, 25/10). Dải tải L của Rồng giữ nguyên; mẫu số là sức ra đòn đo bằng bot (mục 7.4, 13) | Rồng tính W_gõ vì một từ hạ một quái. Ở đây một từ trúng nhiều thú, còn đánh nền và cơ quan gánh phần khác, nên "W_gõ = L × 22,7 × phút" của tệp đánh giá §3.1 đếm sai tải |
| D14 | **Nhàn I đo theo "nhàn quyết định"** (mục 18.2). Dải I là dải chung của BALANCE | Câu 24 |
| D15 | **Không bao giờ chấm một cổng chung bằng dải riêng của game.** Nếu sau này có đề xuất dải riêng, báo cáo in cả hai, dải chung trước, cổng chính thức vẫn là dải chung | (nguồn: `games/dragon-hold/AGENTS.md`; Rồng D27) |
| D16 | Chép sim của Rồng Giữ Ải: mỗi tệp có header `// Source: games/dragon-hold/… @<commit>`; kèm **vé nợ đồng bộ** `docs/SYNC_DEBT.md` của repo game. Không chờ Rồng chốt cách sửa Nhàn I | Câu 24; mã F1 |
| D17 | **Một sự kiện học có chấm cho mỗi từ mỗi trận.** Học trước gửi `review-card` kèm `hintUsed: true`, **không bao giờ là lần nhớ**. Nghĩa ẩn theo số lần nhớ đúng | (nguồn: Rồng D14, D25) |
| D18 | **Tốc độ gõ không bao giờ ngầm là 35.** Chưa có số đo thì thẻ tốc độ hỏi trước trận; `?wpm=` dùng số đó; hồ sơ cập nhật sau mỗi trận | (nguồn: Rồng D26) |
| D19 | **Esc nhả khóa và bỏ chữ đã gõ; số phím sai vẫn giữ** trên từ (kit `RouterRules.unlockErrors: "keep"`) | (nguồn: Rồng D24) |
| D20 | Lọc từ nhạy cảm (`sensitive`) mọi chỗ; hồ sơ trẻ em lọc thêm `mature` | (nguồn: Rồng D15) |
| D21 | **Ba tiền** Linh Sa, Văn Khí, Thú Hạch. Tu vi là thanh kinh nghiệm. **Học không bao giờ tốn tiền.** Tên đồ rơi chỉ là hình của khoản đã ghi sổ | Câu 13; mã A2 |
| D22 | **Không tỉ lệ thất bại khi đột phá.** Thiên Kiếp là pha cuối Đại Triều; thua thì đánh lại pha đó ngay, không mất gì | Câu 11 |
| D23 | Ngũ hành MVP chỉ có **khắc** ×1,30 / ×0,80. Hệ người chơi = hệ trường phái (Kiếm = Kim, Thổ thể = Thổ, Phù = Hỏa). Thú chương 1 vô hệ ở trận dạy; **khắc dạy ở trận 4 bằng biến chủng hệ** dùng chung GLB (đã chọn theo đề xuất, 25/10) | Tệp đánh giá vừa ghi "dạy khắc ở trận 4" vừa xếp thú hệ Thủy, Mộc sau MVP, trong khi Kim chỉ khắc Mộc, Thổ chỉ khắc Thủy. Họ thú Thủy, Mộc mới vẫn sau MVP (mục 11) |
| D24 | "Tham ngộ" biến chiêu đổi tên thành **Ngộ Chiêu** (đã chọn theo đề xuất) | Khỏi trùng tên bậc Tham Ngộ của Tĩnh Tu |
| D25 | **Ấn không cần tầm**: gõ Ấn có tác dụng ở mọi chỗ trên sân (đã chọn theo đề xuất) | Đứng trận phải chơi trọn vẹn (CB4). Thay "16 m" của `05` §4.5 |
| D26 | Âm theo **Q6** (`tools/audio-lab/DECISIONS.md`): có chuẩn bị, phát, thân, đuôi vang; cỡ âm theo cỡ hành động; cấm bụp, thụp, pop, đồ chơi. Nguồn: thu âm CC0 hoặc Audio Lab qua Bảng Nghe của anh. Không âm tổng hợp thuần. **M0a để móc âm im lặng** (mục 22) | Q1, Q6; mã E3 |
| D27 | Không media trong Git (ảnh, âm, video, `.glb`, `.gltf`, `.bin`, `.ktx2`). Model do anh tạo bằng Tripo/Meshy từ ảnh 2D; Claude viết prompt, dọn, rig, làm clip, nướng VAT và impostor bằng Blender. Không dựng sinh vật, nhân vật, công trình bằng mã (khối tạm thì được) | (nguồn: `games/dragon-hold/AGENTS.md`) |
| D28 | Online chỉ dùng **Cloudflare Free**: Durable Object không timer, chỉ đóng dấu tick và phát lại lệnh (relay lockstep); vị trí người thật không vào sim (mục 19) | Luật của anh; mã D1, D2 |
| D29 | Thưởng đội chỉ là danh hiệu. Loot và ví cá nhân (ví theo ghế, nằm trong thế giới, D34). Bot không có thưởng ngoài ải, không gửi sự kiện học (D43) | Câu 20; mã D4 |
| D30 | Khó lên bằng thành phần thú, hệ, cơ chế, luật ải; **không bao giờ** bắt người chơi gõ nhanh hơn sức mình | (nguồn: `BALANCE.md` §1.7) |
| D31 | Các câu 2, 4–10, 12–26 ở mục 8 tệp đánh giá: **đã chọn theo đề xuất** (25/10). Nội dung đã vào các mục dưới | Luật "làm theo đề xuất" của anh |
| D32 | **Pháp bảo: 1 món mỗi trường phái ở MVP**, món thứ hai sau MVP (đã chọn theo đề xuất, 25/10) | Tệp đánh giá §4 ghi 2 món, §6 ghi 1; chọn theo §6 (phạm vi MVP). PB-29 |
| D33 | **Tu vi theo đợt:** trả **một lần cho mỗi đợt của mỗi trận** trong chương, mọi preset tính chung ("mỗi bậc ải" của tệp đánh giá đọc là "mỗi đợt của trận đó"; đổi preset rồi chơi lại không trả lần nữa, chỉ trả 30 % như chơi lại). **9 tu vi mỗi đợt ở K0, 15 ở K1** (đã chọn theo đề xuất, 25/10) | Đánh giá §3.1, Phụ lục A4. Chương còn 34 đợt (D37): 34 × 9 + 80 = 386 = 1,08 lần 357, không cần học tùy chọn; biến thể ít đợt vẫn ≥ 357 (mục 15.2). PB-04, PB-29 |
| D34 | **Ranh giới `local` và thế giới:** `local` chỉ giữ vị trí, Sinh lực, khiên, trạng thái gục của chính mình. Ví (Linh Sa, Thú Hạch), loot, kho đan phù (số viên, hồi chung) là thế giới. Hộ thân là **vật thế giới `ward`** đặt tại `origin` của Cast; tác dụng lên thế giới tính từ `ward`, tác dụng lên chính mình do `local` tính (đã chọn theo đề xuất, 25/10) | D28 không cho vị trí người thật vào sim, nên "đứng trên vạch lúc chạm" không tính được trong sim. Mục 9.1, 12.1, 12.3. PB-01 |
| D35 | **Khởi đầu lạnh:** hồ sơ trống dùng ≤ 40 **từ nền** cờ `assumed`, dùng thẳng ở ô 1, ô 3, Tẩy (ô 2, ô 5, Ấn chỉ qua bước lùi "quen hơn"); mọi từ chưa có bản ghi khác là **từ mới**. Chép `deck.ts` của Rồng thì bỏ nhánh đổi nhãn từ chưa ghi thành "đang học" (đã chọn theo đề xuất, 25/10) | `games/dragon-hold/src/typing/deck.ts` gắn "đã thuộc" cho 50 từ chưa gặp và "đang học" cho từ lấp chỗ; HC1 đếm theo nhãn nên không bắt. Mục 17.1. PB-02 |
| D36 | **HN0 lùi theo phần vượt** (theo đúng chữ của anh ở D03): đo thêm ca nền, quy chi phí cho đám đông, kiếm và VFX, có xương; khi bậc trượt, chỉ phần vượt ngân sách con mới lùi, theo thang của chính nó; phán quyết theo **số thú của luật** (60 ở M0a, 120 cho M1), 300 chỉ là dư địa. Số ngân sách con: đã chọn theo đề xuất (25/10) | Thang cũ cắt kiếm trước đám đông dù kiếm không trượt, và 300 thú có thể đẩy đám đông xuống 2D ở mức game không bao giờ vẽ. Mục 20.3, 20.4. PB-03, PB-19 |
| D37 | **Thời lượng:** trận trộn 6 đợt × 40–45 s (Thư giãn 5 đợt); Đại Triều 7 đợt × 40–50 s, nghỉ 15 s ở Cân bằng; Thú Vương t đích **120 s** ở mọi trận có Vương; cổng **CB9** (đã chọn theo đề xuất, 25/10) | Tính lại ở 35 WPM: Đại Triều cũ 13,0–15,5 phút > 12; trận trộn ở Thư giãn với bot Trẻ em 8,1–10,1 phút > 7 (đánh giá §3.1, câu 8). Mục 4.1, 10.5. PB-04 |
| D38 | **Máu và sát thương số nguyên:** máu thú lưu bằng máu nguyên; sát thương tính theo thứ tự cố định, làm tròn nửa lên sau mỗi hệ số; ô 1 tính một lần mỗi từ rồi chia 3 kiếm (đã chọn theo đề xuất, 25/10) | "Một từ ô 1 hạ Phong Lang" ra 0,999 W và phụ thuộc cách làm tròn. Mục 7.1, 7.2. PB-06, PB-24 |
| D39 | **Sổ cái từ mới thuần, cửa sổ trượt 20 phút, mỗi từ tính một lần**; trận chụp số còn lại vào đầu replay. Mỗi từ mới của trận gặp **≥ 3 lần** (cổng HC8) (đã chọn theo đề xuất, 25/10) | Cửa sổ và lưu cần đồng hồ và `localStorage`, bị cấm trong `src/typing`; tên cũ trùng `BudgetLedger` của kit. Từ mới chỉ gặp một lần thì học yếu (nguồn cổng: Rồng G12). Mục 6.4. PB-10, PB-11 |
| D40 | **Tĩnh Tu:** "hoàn thành phiên" = gõ xong mỗi từ Minh ít nhất một lần; phiên chưa hoàn thành không có sàn 40. Tham Ngộ hiện nhóm chủ đề, Thường không nhãn chỉ lấy cùng nhóm, Tâm ma lấy nhóm cách ≥ 3 bậc (đã chọn theo đề xuất, 25/10) | Ba phiên không gõ phím nào vẫn lĩnh ngộ; Tâm ma không nhãn không phân biệt được với Thường. Mục 16. PB-12, PB-13 |
| D41 | **Hồ sơ gõ:** trần đổi 10 % mỗi phiên chỉ áp **chiều giảm** và chỉ khi độ tin đủ; trận đầu của hồ sơ "chưa biết" tính lại k sau đợt 1 (đã chọn theo đề xuất, 25/10) | Người 60 WPM chọn "chưa biết" mất ~9 phiên mới tới số thật. Mục 6.5. PB-14 |
| D42 | **Bàn Quyết chỉ sống trong đợt và pha Vương.** Chân Nguyên, Dưỡng, điểm luyện công pháp chỉ tính cho Cast `resolved` (đã chọn theo đề xuất, 25/10) | Gõ ô 1 không đích lúc nghỉ để nạp tài nguyên. Mục 6.1. PB-15 |
| D43 | **Bot không gửi sự kiện học**, nhưng dựng sự kiện nháp (`dryRun: true`, không bao giờ gửi) để chấm cổng học B8, HC1–HC3, HC7, HC8 (đã chọn theo đề xuất, 25/10) | Không có nháp thì cổng học chạy bằng bot không có gì để chấm. Mục 17, 18.3. PB-18 |
| D44 | **M0a không sửa kit chung:** hồ sơ phản hồi cục bộ (`src/view/feedback-profile.ts`), nhân vật đi bộ cục bộ (`src/view/walker-rig.ts`), hợp đồng model cục bộ (`src/content/model-contracts.ts`); **cấm import** `kit/feedback/audio-cues` và `kit/audio/dragon-voice` (phát âm tổng hợp). Đưa lên kit ở M0b khi số ổn, là việc riêng của repo cha (đã chọn theo đề xuất, 25/10) | Kit `feedback` phát âm bằng `OscillatorNode` (trái Q6); `Hero` của kit là nhân vật bay, hợp đồng model đòi `Hero_Fly`, `Boss_Idle_Hover`. Mục 21, 22. PB-20, PB-21 |
| D45 | **Chế độ cửa hàng bằng bàn phím:** `` ` `` mở, mũi tên chọn, Enter mua hoặc đặt, `=` nâng và `-` bán (bấm hai lần), Esc thoát (đã chọn theo đề xuất, 25/10; nguồn: Rồng 00 §6 chế độ sửa) | Không có phím thì không viết được `ic-keyboard-only`. Mục 5.1. PB-23 |
| D46 | **Nhàn I tính từ Trận Tâm và không trùng P;** 9 bot chuẩn của B1–B8 dùng chính sách đi Đứng yên (đã chọn theo đề xuất, 25/10) | Đo theo chỗ người đứng làm I đổi theo cách bot đi. Mục 18.2, 18.3. PB-17 |

## 4. Vòng chơi

### 4.1 Một trận

```text
Bày trận 20 s (đồng hồ dừng khi có bảng mở): thẻ đợt, Học trước (tùy chọn), đặt cơ quan,
  chọn Hộ thân hay thân pháp cho ô 3, chọn tâm pháp
→ [ Báo đợt 5 s → Đợt 40–60 s → Nghỉ: cửa hàng, Thẻ Ôn; Cơ Duyên sau đợt 2 và 4 (M1) ] × N
→ Lặng 8 s → Thú Vương (nếu có) → Thiên Kiếp (chỉ cuối Đại Triều, nếu đủ điều kiện) → Thu Hoạch
```

| Loại trận | Đợt | Dài mỗi đợt | Thời lượng đích (35 WPM, k = 1, Cân bằng) | Ghi chú |
|---|---|---|---|---|
| Trận dạy (3 mỗi chương) | 5 | 40–50 s | 5–6,5 phút (tính: 5,4–6,3) | Mỗi trận một ý mới (mục 4.3) |
| Trận trộn (2 mỗi chương) | 6 (Thư giãn, Học: 5, bỏ đợt giữa cuối) | 40–45 s | 6–7 phút (tính: 6,5–7,0) | Mỗi trận một luật ải |
| Đại Triều (cuối chương) | 7 + Thú Vương + Thiên Kiếp | 40–50 s | ≤ 12 phút (tính: 10,2–11,9) | Nghỉ 15 s ở Cân bằng. Mốc lưu sau đợt 4. Hồ sơ trẻ em dùng bản 6 đợt |
| Ải hộp xám M0a | 6 + Thú Vương | 40–60 s | 9–10,5 phút (tính: 9,7) | Ngoại lệ M0 (mục 25) |

- **Cách tính** (D37, PB-04): bày trận 20 + đợt × (báo 5 + dài đợt) + (đợt − 1) × nghỉ + lặng 8 + Vương 120 + Thiên Kiếp 60–90 s. Ví dụ Đại Triều: 20 + 7 × 5 + 280–350 + 6 × 15 + 8 + 120 + 60–90 = 613–713 s. Ở Thư giãn với bot Trẻ em (k 0,75, giờ đợt × 1,33, bấm Enter sau ~15 s): trận dạy 20 + 25 + 5 × 45 × 1,33 + 4 × 15 = 404 s = 6,7 phút; trận trộn 5 đợt 388 s = 6,5 phút. Cổng **CB9** (mục 18.4) đo thời lượng thật, không tính thời gian có bảng mở.
- **Nghỉ đợt:** Thư giãn chờ Enter (tự vào sau 60 s), Cân bằng 20 s (Đại Triều 15 s), Thử thách 15 s. Đồng hồ nghỉ chỉ chạy khi **không có bảng nào mở** (nguồn: Rồng 00 §4.5). Sinh lực người chơi hồi 30 % lúc nghỉ. Trận Lực không hồi lúc nghỉ.
- **Người gõ chậm:** nhịp k < 1 giãn khoảng sinh và giờ đợt, không đổi máu thú (mục 7.5). Ví dụ k 0,75: trận dài ×1,33.
- **Hết đợt** (nguồn: Rồng `games/dragon-hold/src/sim/waves.ts`): đồng hồ đợt chỉ điều khiển lịch sinh. Đợt **kết thúc khi mọi toán của đợt đã sinh và không còn thú sống của đợt**; toán phải chờ ở cổng vì trần thú sống thì sinh ngay khi có suất, kể cả sau khi đồng hồ đợt hết. Nghỉ bắt đầu khi đợt kết thúc. Thú gọi thêm (Tru Đàn) thuộc đợt đang chạy. **Trận có Vương:** lặng 8 s bắt đầu khi đợt cuối đã sinh hết toán (thú cũ vẫn đi, không nghỉ), rồi Vương vào.
- **Thắng:** trận không Vương: đợt cuối kết thúc; trận có Vương: Vương ngã và không còn thú sống; luôn khi Trận Lực > 0. **Sao** theo Trận Lực còn lại: ≥ 70 % ★★★, ≥ 40 % ★★, > 0 ★.
- **Gục:** Sinh lực người chơi về 0. Solo: nằm 8 s rồi dậy ở Trận Tâm, Trận Lực −5 %. Đội (M1+): đồng đội đứng trong 3 m và gõ xong **một từ bất kỳ** là cứu (không mất Trận Lực); không ai cứu thì tự dậy sau 15 s, Trận Lực −5 %. Không có đan hồi sinh, không Mệnh Đăng. **Lúc gục:** Bàn Quyết mờ, không gõ được (phím chữ bị bỏ, từ đang gõ dở nhả như Esc); Dưỡng tắt; đánh nền dừng; đan phù không dùng được (PB-24).
- **Thua** (Trận Lực về 0) hoặc **Rút lui** (menu dừng): giữ 50 % Thú Hạch của trận, không sao. **Văn Khí và mọi kết quả học không bao giờ mất.** Tu vi đã nhận theo đợt không mất.
- **Tu vi** trả theo đợt đã giữ, một lần cho mỗi đợt của mỗi trận, mọi preset tính chung (D33); chơi lại 30 % (mục 15.2).

### 4.2 Vòng ngoài

```text
SƠN MÔN (một màn tĩnh, 4 điểm, phím 1–4 hoặc chuột)
  1 Trận Đài   chọn trận, xem thẻ triều, đổi pháp bảo, Học trước
  2 Tĩnh Thất  Tĩnh Tu lĩnh ngộ công pháp, chọn Ngộ Chiêu, đổi Đạo Quả (miễn phí)
  3 Thư Lâu    tiêu Văn Khí
  4 Bảo Khí Lò tiêu Thú Hạch
→ trận → Thu Hoạch → về Sơn Môn
```

- **Chương = 1 ải = 1 cảnh giới.** Chương 1 (MVP) là ải **Thanh Thạch Ải**, cảnh giới K0 Luyện Khí: 3 trận dạy, 2 trận trộn, Đại Triều. Qua Thiên Kiếp cuối chương thì lên K1 Trúc Cơ: đó là đích cuối của MVP.
- **Phiên mẫu khoảng 25 phút:** Sơn Môn 2' → trận 6' → Thu Hoạch → Tĩnh Thất 3' → trận 6' → trận 7' → nhắc nghỉ. (Tu vi theo đợt là 34 đợt mỗi chương: 3 × 5 + 2 × 6 + 7; D33.) **Nhắc nghỉ** sau 30 phút (20 phút với hồ sơ trẻ em). Lưu sau mỗi trận.

### 4.3 Mười phút đầu và lịch dạy

- Mở game → thẻ tốc độ (một bấm; "chưa biết" thì dùng 25 WPM và đo ở đợt 1, D18; hết đợt 1 thì k tính lại, D41) → **trận dạy 1 trong ≤ 60 s**, không có lựa chọn build. Hồ sơ trống dùng từ nền (mục 17.1).
- **Dò bộ gõ tiếng Việt** khi vào trận (mục 5.2).
- Mỗi loài thú mới ra lẻ ít nhất 3 lần trước khi trộn (nguồn: Rồng 02 §5.6). Mỗi trận dạy đúng **một ý mới**:

| Trận | Ý mới | Thú mới |
|---|---|---|
| Dạy 1 | Ô 1–3, Trận Tâm, Kết Giới | Thạch Thử (bầy), Phong Lang |
| Dạy 2 | Ô 4 (Chiêu B), cơ quan, Trận Trụ chặn đá | Nham Viên |
| Dạy 3 | Ô 5 (Tuyệt kỹ), tinh anh, Ấn, Thế | Hỏa Nha (đường trời) |
| Trộn 1 (trận 4) | Khắc hệ (biến chủng Đằng Thử), Cơ Duyên, pháp bảo, công pháp; luật ải "Song Môn" (hai cổng cùng ra) | Thiết Giáp Trư (chiếm nhãn, Tẩy) |
| Trộn 2 (trận 5) | Thú tướng, luật ải "Sương Chàm" (thú hiện mờ tới khi cách Trận Tâm ≤ 14 m; chữ không bao giờ bị che) | Lang Đầu Đàn |
| Đại Triều | Thú Vương, Thiên Kiếp | Thiết Bối Lang Vương |

## 5. Điều khiển và bảng phím (nguồn duy nhất)

### 5.1 Bảng phím

Phím lệnh đọc theo `event.code` (máy chính của anh có Mac). Không dùng Tab, F1–F12, Insert, Delete, PageUp, Pause ở MVP. **Không có WASD ở MVP** (gõ cần hai tay trên hàng phím chữ).

| Việc | Phím, chuột | Ghi chú |
|---|---|---|
| Gõ | a–z | **Chỉ để gõ.** Phím IME đang soạn, phím giữ lặp, phím có Ctrl hoặc Cmd bị bỏ |
| Xóa một chữ của từ đang khóa | Backspace (Mac: delete) | |
| Nhả khóa → đóng bảng → menu dừng | Esc | Theo thứ tự. Esc khi đang khóa chỉ nhả khóa (D19); Esc khi không khóa mới đóng bảng hoặc mở menu |
| Đi tới điểm | Chuột phải lên đất | Tìm đường trên lưới 0,5 m (nguồn: `games/typing-defense/src/sim/nav`) |
| Đi trực tiếp | ← → ↑ ↓ | Thả phím thì dừng. Mũi tên không đụng hàng phím chữ |
| Đặt mục tiêu mềm | Chuột trái lên một thú | Giữ tới khi thú chết hoặc chuột trái lên đất |
| Điểm đặt chiêu đất | Vị trí con trỏ trên sân | Ô 4, ô 5, phù ném: con trỏ trên sân thì đặt ở đó, không thì cụm đông nhất |
| Đan, phù | 1 / 2 / 3 (không phím phụ) hoặc click ô | Hồi chung 8 s. Khi một bảng mở (Thẻ Ôn, Cơ Duyên), phím số thuộc bảng |
| Mở, đóng **chế độ cửa hàng** | `` ` `` (Backquote) | Chỉ lúc bày trận và nghỉ (D45; nguồn: Rồng 00 §6 "chế độ sửa"). Người chơi không đi trong chế độ này; mũi tên thuộc cửa hàng |
| Trong chế độ cửa hàng | ← → chọn món · ↑ ↓ chọn ô (6 ô cơ quan, rồi ô đan phù) · Enter mua hoặc đặt · `=` nâng (bấm hai lần) · `-` bán (bấm hai lần) · Esc thoát | Mọi việc này chuột cũng làm được. Không gõ để mua, đặt, nâng (mục 14.3) |
| Bắt đầu đợt (ngoài chế độ cửa hàng); nộp ô trả lời | Enter | |
| Chọn điểm Sơn Môn | 1–4, chuột | Ngoài trận |
| Bánh xe câu soạn sẵn (M3) | Giữ chuột giữa | Câu tiếng Anh soạn sẵn; không chat gõ tự do |

- Camera **cố định**, không xoay, không zoom ở MVP.
- Màn cài đặt có **đổi phím** cho mọi phím lệnh không phải chữ.
- Mọi việc có đường bàn phím, trừ đi tới điểm (mũi tên thay được) và đặt mục tiêu mềm (không bắt buộc). Kịch bản `ic-keyboard-only` chơi cả ải chỉ bằng bảng này.

### 5.2 Bộ gõ tiếng Việt và chế độ đầu vào

- Khi vào trận, game dò bộ gõ (`keydown` có `isComposing`, `key` là `Process`/229, hoặc ký tự có dấu) và hiện dải báo rõ: Unikey hay EVKey đang bật ở Telex/VNI, cách tắt (chuyển sang E). Dùng xử lý composition và `typedLetter` của kit (`kit/input`). Không đổi độ khó (yếu tố 13 của BALANCE).
- **Voice, Hybrid** sau MVP (M4), khi `shared/voice` có bộ giải mã chạy thật. Khi đó chế độ Voice được dùng WASD vì chữ cái không dùng để gõ.

## 6. Gõ

### 6.1 Hợp đồng Cast

- **Một từ hoàn thành = đúng một giao dịch** `Cast{seat, slot, actionId, wordId, tick, channel, quality, origin}`:
  - `actionId`: số tăng dần riêng mỗi ghế (`seat × 2^20 + n`). Bản trùng bị bỏ.
  - `channel`: `typing` (MVP), `voice`, `hybrid`.
  - `origin`: vị trí người chơi lúc chữ cuối, lượng tử **100 mm = 6.000 u** (đơn vị sim, mục 7.1), lấy từ lệnh phím (mục 9.1).
- Phím đầu **khóa mềm** ô đó. Chữ cuối đúng tạo Cast. Hoạt ảnh, dừng hình, mạng không bao giờ nhân Cast.
- **Bàn Quyết sống** (D42, PB-15) chỉ từ lúc **báo đợt** tới khi đợt kết thúc, và trong pha Vương (gồm lặng 8 s trước Vương). Lúc bày trận, nghỉ, Thu Hoạch và lúc gục: ô hiện mờ, không có chữ sống; phím chữ đi vào bảng đang mở, không thì bị bỏ.
- **Không có đích hợp lệ:** ô giữ trạng thái "đã gõ" (`held`) 3 s, **không tốn hồi chiêu**. Có đích trong 3 s thì Cast chạy (`resolved`); hết 3 s thì Cast tắt (`fizzled`), ô nhận từ kế ngay, không hồi. Sự kiện học của từ đó vẫn ghi (từ đã được gõ; vẫn một sự kiện có chấm mỗi từ mỗi trận).
- **Chỉ Cast `resolved` cho tài nguyên:** Chân Nguyên, Dưỡng của Tâm nhãn, điểm luyện công pháp, Kiếm Tâm. Cast `fizzled` chỉ ghi sự kiện học (D42).
- **Từ không bao giờ đổi khi đang gõ dở.** Ô chỉ nhận từ mới khi từ cũ có 0 chữ đã gõ (sau Cast, hồi xong, hoặc Esc).
- **Sẵn cho Voice:** kết quả tạm của nhận giọng nói chỉ tô sáng ô, không cast; kết quả muộn (từ không còn sống hoặc `actionId` cũ) bị bỏ; hai kênh cùng xong chỉ chốt một; âm phát của game và phát âm mẫu không bao giờ kích chiêu.
- Dừng hình chỉ làm chậm thế giới, **không bao giờ** làm chậm hay nuốt phím (nguồn: Rồng LANES "Integration").

### 6.2 Luật chữ

- **Chữ đầu** của mọi chữ sống khác nhau (kit `typing/letters.ts`, bậc 1). Bậc 2 (chung chữ đầu, khác chữ thứ hai) **không dùng** trong trận vì chữ sống ≤ 8; bot ghi mỗi lần thiếu chữ đầu thành "nghẽn chữ đầu".
- Không chữ sống nào là **tiền tố** của chữ sống khác; không hai chữ sống cách nhau ≤ 1 phép sửa (kit `typing/distance.ts`).
- Chữ nhả ra nghỉ 1 s rồi mới được làm chữ đầu lại (kit `TypingRules`).
- **Trần chữ sống** (mọi tick, mọi bot) = **min(trần preset; A − 3)**, với A = số chữ cái có ≥ 3 từ hợp lệ trong bộ từ của trận (nguồn: Rồng 00 §5 `N_max = min(16 ; A − 3)`; PB-26). Đếm suất theo nguồn bằng `BudgetLedger` của kit (`typing/budget.ts`):

| Preset | Trần preset | Gồm |
|---|---|---|
| Cân bằng, Thử thách | **≤ 8** | 5 ô + ≤ 2 Ấn + ≤ 1 chữ khẩn |
| Thư giãn, Học, hồ sơ trẻ em | **≤ 5** | Thứ tự ưu tiên khi vượt trần: chữ khẩn > Ấn (≤ 1) > ô 3 > ô 1 > ô 2 > ô 5 > ô 4; **Học: … > ô 2 > ô 4 > ô 5** (ô 4 là ô duy nhất nhận từ mới, PB-32). Ô thua chờ (hiện mờ) tới khi có suất |

- **Không có từ thỏa luật** (chữ đầu, tiền tố, khoảng sửa, loại từ, độ dài của ô; PB-26), lùi theo thứ tự: (1) nới độ dài ±1, vẫn trong 3–8; (2) nới loại về phía **quen hơn** (mới → đang học → đến hạn → đã thuộc, từ nền tính là đã thuộc), **không bao giờ về phía từ mới**; (3) ô chờ mờ, ghi "nghẽn" vào báo cáo bot. Không bao giờ lấy từ mới để lấp.
- Thú thường **không mang chữ**. Kể cả khi trần thú sống lên 120 (M1), chữ sống vẫn ≤ 8.
- **M1:** trong Thiên Kiếp và trong cửa sổ Trận Quyết, ô 2–5 tạm mờ (không là chữ sống), để Chấp Ảnh và Trận Quyết nằm trong trần (PB-33).
- Ô đang hồi hiện **mờ 50 %** từ kế tiếp để đọc trước; từ mờ không phải chữ sống, không giữ chữ đầu. Ô hồi xong không giành phím đang gõ.

### 6.3 Ô và loại từ

| Ô | Vai | Hồi (thử) | Loại từ | Độ dài | Mở ở |
|---|---|---|---|---|---|
| 1 Liên tục | Mỗi từ nạp một băng chiêu nhỏ; băng tự xả | 0 (từ mới hiện ngay) | Đã thuộc, đến hạn, hoặc từ nền | 3–5 | Dạy 1 |
| 2 Chiêu A | Chiêu chính | 8 s | Đang học, đến hạn; **lần gặp lại của từ mới của trận** (mục 6.4) | 4–7 | Dạy 1 |
| 3 Hộ thân **hoặc** thân pháp | Tự cứu / lướt 5 m (chọn trước trận) | 15 s / 8 s | Đã thuộc hoặc từ nền | 3–5 | Dạy 1 |
| 4 Chiêu B | Chiêu phụ. **Ô duy nhất trong trận nhận từ mới**, chỉ ở đợt 1–2, luôn hiện nghĩa và IPA khi mới | 12 s | Mới (đợt 1–2) hoặc đang học | 4–7 | Dạy 2 |
| 5 Tuyệt kỹ | Hiện chữ khi Chân Nguyên đầy; dùng hết thanh | Thanh 100 | Đến hạn, yếu | 5–8 | Dạy 3 |
| Ấn | Trên tinh anh, thú tướng, Thú Vương | — | Đã thuộc hoặc đến hạn, **không bao giờ từ mới** (từ nền chỉ qua bước lùi, mục 17.1) | Thư giãn và Học 3–5 · Cân bằng 4–6 · Thử thách 4–7 | Dạy 3 |
| Tẩy (chữ khẩn) | Lấy lại nhãn bị chiếm | — | Đã thuộc hoặc từ nền | 3–4 | Trộn 1 |
| Trận Quyết (M1) | 2 từ riêng mỗi người; cửa sổ mỗi ghế theo T₂ của mục 8.4 | — | Đã thuộc hoặc đến hạn | **3–4** | M1 |
| Chấp Ảnh | Trong Thiên Kiếp | — | Từ yếu của chính người chơi **trong game này**, luôn hiện nghĩa và IPA | 4–7 | Đại Triều |
| Ô 6 Thần thông | — | 45–75 s | Cụm 2 từ | — | Sau MVP (K2) |

- Độ dài trong dải của ô chọn theo E của người chơi (nguồn: Rồng 01 §3.4: ℓ̄ 4,5 khi E < 45; 5,5 khi 45–64; 6,0 khi ≥ 65).
- Ô không bao giờ nhận từ dài hơn chỉ vì đúng hệ (nguồn: `02` §4.6).
- **Ô gấp** (không bao giờ nhận từ mới): ô 1, ô 3, ô 5, Ấn, Tẩy, Trận Quyết, mọi chữ vật phẩm. Cổng HC1 đếm theo **bản ghi học**, không theo nhãn: một từ không có bản ghi trước trận và không thuộc danh sách từ nền mà lên ô gấp là lỗi (PB-02).
- Ô 2 nhận từ mới của trận **chỉ** ở lần gặp thứ hai trở đi (sau Học trước hoặc ô 4), nhãn "đang học"; ô 2 không bao giờ là lần gặp đầu.
- Đan, phù dùng phím: không chữ, không thưởng học.

### 6.4 Ngân sách từ mới

- **≤ 8 từ mới trong mọi cửa sổ trượt 20 phút**, tính chung **Học trước, Tĩnh Tu, Chiêu B** (D11, D39; PB-10).
- **Sổ cái** `src/typing/new-word-ledger.ts`, kiểu `NewWordLedger`, **thuần** (không đồng hồ, không lưu):
  - `createNewWordLedger(snapshot)` với `snapshot = { v: 1, entries: { wordId, firstSeenMs, channel: "learn-ahead" | "tinh-tu" | "slot4" }[] }`; `remaining(nowMs)`; `take(wordId, nowMs, channel)`. Giờ do người gọi đưa vào.
  - Đọc, ghi khóa `immortality-cultivation.newwords` ở `src/app/storage.ts` qua kit `safe-storage` (mục 23.1), dùng chung giữa trận và trang Tĩnh Tu.
  - Một từ tính **một lần**, ở lần gặp đầu, kênh nào cũng vậy (Học trước rồi ô 4 của cùng từ = 1). `take` lặp lại cùng `wordId` không trừ thêm. Không có khái niệm "phiên chơi": chỉ có cửa sổ trượt theo `firstSeenMs`.
  - Tên khác `BudgetLedger` của kit (đó là trần chữ sống).
- **Trận:** lúc nạp trận đọc `remaining` **một lần**, ghi vào đầu replay là `newWordAllowance`; sim chỉ dùng số đó (replay và golden tất định). Lớp app (ngoài sim) gọi `take` khi sim báo một từ mới được gặp lần đầu, với giờ tường của app. Khi hồ sơ có **> 80 từ đến hạn ôn**: `newWordAllowance = min(remaining; 4)`. Đã dùng hết ở Tĩnh Tu thì trận không đưa từ mới.
- **Tĩnh Tu:** còn < 6 thì không mở bài mới; Tĩnh Thất hiện "còn N phút nữa đủ 6 từ" và cho phiên ôn (chỉ Thường). Không bao giờ dạy nửa bài.
- Từ mới chỉ ở **Học trước, Tĩnh Tu, Chiêu B (đợt 1–2)**. Mọi chỗ khác chỉ dùng từ đã thuộc, đang học, đến hạn hoặc từ nền (mục 17.1).
- **Gặp lại trong trận** (D39, PB-11; nguồn cổng: Rồng G12): mỗi từ mới của trận gặp **≥ 3 lần**: lần đầu ở Học trước (nếu làm) hoặc ở ô 4; rồi ≥ 2 lần nữa ở ô 2 hoặc ô 4 với nhãn "đang học", hai lần gặp cách nhau ≥ 45 s, xong trước đợt 4. `WordPicker` ưu tiên trả từ mới của trận cho ô 2, ô 4 tới khi đủ lần. Cổng HC8.
- Tỉ lệ từ mới giảm khi độ chính xác < 90 % hoặc thời gian nhận từ mới > 1,5 s (nguồn: `BALANCE.md` §4.1). Không đưa từ mới vào đợt có tải > 1,0.

### 6.5 Chất lượng từ và Chớp

| Kết quả | Điều kiện | M_q |
|---|---|---|
| **Chớp** | 0 lỗi và t ≤ 0,85 × t_kỳ_vọng **theo hồ sơ của chính người đó** | ×1,25 |
| Hoàn hảo | 0 lỗi | ×1,10 |
| Tốt | 1 lỗi, từ ≥ 6 chữ | ×1,00 |
| Vừa | 1 lỗi, từ ≤ 5 chữ | ×0,90 |
| Ẩu | ≥ 2 lỗi | ×0,60 |

(nguồn: Rồng 00 §4.2)

- `t_kỳ_vọng` lấy từ E hiệu dụng của hồ sơ (`kit/balance` `SkillProfile`): phân vị bền nhiều phiên. **Trần đổi 10 % mỗi phiên chỉ áp chiều giảm**, và chỉ khi E đã có độ tin ≥ 60 từ đo được qua ≥ 3 phiên; chiều tăng, và mọi chiều khi độ tin còn thấp, dùng `blendSkill` của kit, không trần (D41, PB-14). Ngưỡng Chớp có **sàn** ứng với E hồ sơ của 5 phiên gần nhất, nên cố ý gõ chậm một phiên không làm Chớp dễ hơn.
- **Trận đầu của hồ sơ "chưa biết"** (25 WPM giả định, D18): hết đợt 1, k của ghế tính lại từ số đo của đợt 1 bằng lệnh `pace-update{seat, kPm}` ghi vào replay, áp từ đợt 2. Máu và thành phần không đổi (k chỉ đổi thời gian).
- Người 25 và 60 WPM gõ đều tay có **cùng tỉ lệ Chớp**. Voice (M4) có hồ sơ kênh riêng, cùng tỉ lệ Chớp mục tiêu.
- **Không có chí mạng ngẫu nhiên** ở bất kỳ đâu. Bạo kích (nâng Chớp tới trần ×1,45) là chỉ số sau MVP.

### 6.6 Chân Nguyên

- +5 mỗi từ Chớp hoặc Hoàn hảo · +3 mỗi từ có lỗi · +2 mỗi Ấn (cộng thêm), **nhân 1 / k_ghế** (lưu phần nghìn, làm tròn nửa lên), để thời gian đầy bằng nhau trong khoảng k 0,75–1,30 (PB-32). Chỉ Cast `resolved` (D42). Đầy 100 sau khoảng **55–70 s ở 35 WPM**; ở 90 WPM (k 1,30) khoảng 48 s; bot Trẻ em (~8 từ/phút, k kẹp 0,75) khoảng 2–2,5 phút.
- Đầy thì ô 5 hiện chữ. Tuyệt kỹ dùng hết thanh. Thanh giữ qua nghỉ đợt; về 0 khi hết trận.
- HUD trong trận **chỉ có**: Sinh lực (khiên hiện đè trên thanh này), Chân Nguyên, Trận Lực, và thanh Thế khi có tinh anh, thú tướng hoặc Thú Vương. Không có Linh lực tiêu theo chiêu: chi phí thật của chiêu là thời gian gõ.

## 7. Đơn vị, sát thương, nhịp

### 7.1 Đơn vị

```text
g(K)     = 1,12^K                      // sức theo cảnh giới, cả hai phe: K0 1,00 · K1 1,12 · K2 1,254 · … · K6 1,974
P_ref(K) = 100 × g(K)                  // sức "bộ đồ trung bình" ở cảnh giới K
1 W      = 0,9 × P_ref(K) = 90 × g(K)  // sát thương một từ Vừa ở ô 1 (máu)
máu thú  = round(W × 90 × g(K) × hệ số preset)   // số nguyên máu (D38)
```

- K của trận là cảnh giới của chương (chương 1: K0). Sức người chơi nhân g(K) của chính người đó; người K1 chơi lại chương 1 mạnh hơn 12 %, vẫn trong trần +25 % (mục 14.6).
- Thời gian khống chế, tầm, tốc **không** nhân g(K).
- **Trạng thái sim chỉ có số nguyên** (nguồn: Rồng LANES "Units", `games/dragon-hold/src/sim/fixed.ts`): **máu và sát thương bằng máu nguyên**; phần nghìn (`…Pm`); tick 60 Hz; không gian **u, 1 m = 60.000 u**. **Dữ liệu** (`rules.ts`, `data/*.ts`) ghi mm (`…Mm`), ms (`…Ms`), W × 100 (`w100`); bước nạp đổi sang u, tick, máu. `w100` không nằm trong trạng thái (PB-06, PB-30).
- Ví dụ K0 Cân bằng: Thạch Thử 0,33 W = 30 máu; Phong Lang 1 W = 90; Nham Viên 2 W = 180; Thiết Giáp Trư 3 W = 270.

### 7.2 Công thức sát thương

```text
D = P × M_q × M_hệ × (1 + Σ tăng cùng bucket, trần +50 %) × M_dễ_tổn_thương
giảm = G / (G + 100), trần 75 %        bậc giáp G0 / G1 / G2 / G3 = G 0 / 43 / 122 / 300 = giảm 0 / 30 / 55 / 75 %
```

| Loại | Ai gây | Bị chặn bởi |
|---|---|---|
| **Gõ** | Mọi Cast từ chữ (ô 1–5, Ấn, Tẩy, Trận Quyết) | Không gì. **Đòn gõ bỏ qua Giáp** |
| Vật lý | Đánh nền, Kiếm Thung, đòn thú | Giáp |
| Phép | Lôi Phù Trụ, phù ném, Hợp Trận | Kháng (cùng thang G) |

- Dễ tổn thương: phá thế ×1,5. Khác nguồn thì nhân, cùng nguồn lấy mạnh nhất.
- **Trần cụm:** một đòn vùng gây tối đa 60 % tổng máu một cụm bầy (nguồn: `BALANCE.md` §9.1).
- **Trần bucket** (Codex §21): Σ tăng sát thương ≤ +50 %; giảm hồi chiêu ≤ 30 %; hệ số hệ tổng ≤ 1,60, ≥ 0,60; giảm sát thương nhận ≤ 75 %; khiên có trần theo đối tượng; cùng ID lấy mạnh nhất (Codex §12.5).
- Thú chết trước khi đòn chạm: đòn rẽ sang thú gần nhất trong 4 m, 50 % (nguồn: Rồng 00 §4.2).
- **Thứ tự tính và làm tròn** (D38, PB-24): `P → × M_q → × M_hệ → × (1 + Σ bucket) → × M_dễ_tổn_thương → giáp hoặc kháng (chỉ đòn không gõ) → trần cụm → trần máu còn lại`. Mỗi bước là `mulDiv` số nguyên, **làm tròn nửa lên**. Sổ phần sát thương (CB2, CB3, mục 7.3) cộng **sát thương hiệu dụng** (≤ máu còn), không cộng phần thừa.
- **Chồng làm chậm:** khác nguồn thì nhân (Kết Giới 15 %, Kiếm Thung 25 %, Lạc Kiếm Trận 20 %, Định Thân Phù 40 %), cùng nguồn lấy mạnh nhất; tổng chậm ≤ 60 %. Khống chế cứng (trói, choáng, ngã) tính vào trần 35 % thời gian sống (mục 8.3).

### 7.3 Phần sát thương (đo ở bot Chuẩn, Cân bằng)

| Nguồn | Đích | Cổng |
|---|---|---|
| Gõ (mọi Cast từ chữ) | **≥ 60 %**, dải thiết kế 60–70 % | CB2: ≥ 55 % |
| Đánh nền | 12–18 % | Báo cáo |
| Cơ quan + đan, phù + trận pháp (Tâm nhãn, Hợp Trận) | ≤ 25 % | Báo cáo |
| Ô liên tục | **≤ 30 % sát thương gõ** | CB3 |
| Hợp Trận (M1) | ≤ 12 % sát thương cả trận | Báo cáo M1 |
| Mỗi chiêu vùng | ≤ 20 % sát thương cả trận | Báo cáo |

- Bucket của một sát thương theo **nguồn** của nó; hệ số nhân (Tâm nhãn Công, pháp bảo) không chuyển sát thương sang bucket khác. Sổ cộng sát thương hiệu dụng (mục 7.2).
- **Rủi ro CB3 đã biết** (PB-05): ô 2, ô 4 bị hồi chiêu chặn, nên mọi từ dư của người nhanh đổ vào ô 1 (ở 70 WPM khoảng 18 từ/phút vào ô 1). Làn bot in phần ô 1 theo **từng bot** ngay vòng đầu; nếu Khá, Nhanh vượt 30 % thì trước hết tăng sức ô 2, ô 4, sau mới hạ sát thương mỗi từ ô 1 (giữ bất biến mục 10.2 trong phạm vi của nó); làm việc này **trước** khi tăng tải (câu hỏi mở 10).

### 7.4 Sức ra đòn chuẩn D_ref (D13)

- **D_ref(trường phái, K)**: tổng sát thương mỗi phút của bot Chuẩn (35 WPM, 95 %, CV 0,25, chiến thuật Vừa) với bộ đồ trung bình, trên **sân thử trộn** (sim chạy mật độ chuẩn: 35 % máu là bầy, 35 % thú Nhỏ, 30 % thú Vừa, luôn đủ đích trong tầm). **D_đơn**: cùng bot, lên một mục tiêu Thú Vương đứng yên.
- Số thử cho Kiếm, K0 (ước từ bảng 12.1): **D_ref ≈ 75 W/phút** (gõ ~47, đánh nền ~12, cơ quan và trận pháp ~16), **D_đơn ≈ 46 W/phút**. Phần gõ ước theo chính sách chọn ô của bot (mục 18.3): ô 1 ~10, ô 2 ~18, ô 4 ~11, tuyệt kỹ ~8 (PB-05).
- Làn bot đo D_ref, D_đơn **trước** khi chỉnh đợt (`scripts/balance/calibrate.ts`), ghi vào `rules.ts` `REF_OUTPUT`; máu đợt và máu Vương tính lại từ số đo (mục 13).
- Trường phái tham chiếu là **Kiếm**. Thổ thể (M1) không có D_ref riêng cho đợt; nó phải đạt cùng dải thắng (CB7).

### 7.5 Sức gõ và nhịp k (nguồn: Rồng 00 §4.3–4.4, `BALANCE.md` §4.1)

```text
C(E)  = 60 / (0,45 + 12 × (ℓ̄ + 1) / (E × 0,86))      từ mỗi phút; ℓ̄ theo dải E (mục 6.3)
E_eff = E × (0,6 + 0,4 × a²) × (1 − 0,5 × CV), giữ trong [0,7 E ; E]
k     = clamp(C(E_eff) / C_ref ; 0,75 ; 1,30)       C_ref = C(E_eff của bot Chuẩn) ≈ 19,6 từ/phút
```

- k **theo từng ghế**, theo hồ sơ của người ngồi ghế đó. k chỉ giãn hoặc nén **thời gian** (khoảng sinh, giờ đợt, thời gian nạp đòn có báo); máu, thành phần, mã băm giữ nguyên.
- Trần k là 1,30 của BALANCE. Nếu bot Nhanh thắng quá dải (như Rồng M0a), đề xuất nâng trần ghi thành quyết định riêng; không tự đổi.
- E, a, CV lấy từ `?wpm=`, thẻ tốc độ hoặc hồ sơ (D18). Thiếu a, CV thì dùng 95 % và 0,25.

## 8. Trận pháp và cơ quan

### 8.1 Sân ải mẫu Thanh Thạch Ải

```text
    [Cổng A]                ~ đường trời (Hỏa Nha) ~                [Cổng B]
        \      ô1         ô2                         ô3        ô4      /
         \______    ▲ Trận Trụ T      (hẻm giữa)      ▲ Trận Trụ P ______/
                \_____________________     _____________________/
                     ô5         (  Kết Giới r 9 m  )         ô6
                                  ◎ TRẬN TÂM  · Tâm nhãn
              ═════════════ Sơn Môn (nền phía sau, không đánh) ═════════════
```

- Sân **40 × 26 m**. Tọa độ (x đông, z nam; mét): **Trận Tâm ở gốc (0; 0)**; mép sau z = +8, mép trên z = −18, hai mép bên x = ±20. **Cổng đất A, B ở (∓15; −18)**, đường đi ~24 m. **Đường trời** vào từ hai góc trên (±20; −18), bay thẳng 26,9 m về Trận Tâm (PB-08).
- Thời gian tới mép Kết Giới (r 9 m) ở k = 1, Cân bằng: Phong Lang (24 − 9) / 1,4 = **10,7 s**; Thạch Thử 9,4 s; Hỏa Nha (26,9 − 9) / 2,0 = **9,0 s**. Thú Nhỏ trong **8–12 s** (để bot Chuẩn hạ thú ở quãng Q 55–70 %, nguồn: `BALANCE.md` §9.1). Ngoại lệ có chủ ý: Phong Lang Cuồng 8,2 s; trong hào quang tướng 9,3 s; cả hai 7,2 s; luôn ≥ 6 s. Thú Vừa chậm hơn theo vai (Nham Viên dừng ném ở 11 m sau ~13 s).
- Thú đi theo **trường hướng** (flow field) từ mỗi cổng tới Trận Tâm, trong hành lang đọc được; không bị buộc vào làn hẹp. Đường trời bỏ qua cơ quan đất.
- **Không** có tường, cổng hay nhà có máu riêng (Codex §14.3).

### 8.2 Trận Tâm, Kết Giới, Tâm nhãn, Trận Trụ

| Thành phần | Luật (số thử) |
|---|---|
| **Trận Tâm** | Giữ **Trận Lực**: solo 1.000 · Lưỡng Nghi 1.400 · Tam Tài 1.800 · Thất Tinh 3.500. Về 0 là thua. Không hồi lúc nghỉ |
| **Kết Giới** (r 9 m) | Thú trong vùng chậm 15 %. Người chơi trong vùng nhận −10 % sát thương. Ra khỏi vùng: đệm 1,5 s rồi phần gia trì phai trong 3 s. Vào lại: nối sau 1 s. Ra vào nhiều lần không cộng dồn |
| **Tâm nhãn** (solo; điểm trên đất cạnh Trận Tâm) | Gộp ba nhãn ở mức 2/3: **Công** +8 % sát thương chiêu gõ · **Thủ** Trận Tâm nhận −15 % sát thương · **Dưỡng** hồi 0,1 % Trận Lực mỗi giây khi người chơi có một Cast `resolved` trong **3 s / k_ghế** gần nhất (PB-32, D42), trần 15 % Trận Lực mỗi trận; tắt lúc gục và khi Bàn Quyết không sống. Tác dụng theo ghế, không theo chỗ người đứng |
| **Ba nhãn** (M1, khi có bot hoặc đội) | Công +12 % · Thủ −25 % sát thương lên Trận Tâm từ hướng của nhãn · Dưỡng 0,15 %/s, trần 20 %. Mỗi ghế giữ một nhãn và chịu chính một hướng thú |
| **Chiếm nhãn** | Thú loại chiếm chốt (Thiết Giáp Trư) đứng trên điểm nhãn 3 s thì nhãn **tắt tới khi thú đó chết**. Đồng thời hiện **Tẩy** trên nhãn: ai gõ xong thì nhãn sáng lại sau 1 s, thú bị đẩy ra 2 m. Nhãn không có máu |
| **Trận Trụ** (2 cột đá) | Chặn đá ném và đường húc. Mỗi cột chịu **2 cú húc của Thú Vương** rồi nứt tới hết trận (nứt thì không chặn húc, vẫn chặn đá). Đứng trong 1,5 m của cột là chỗ an toàn khỏi Lôi Kiếp |
| **Ô cơ quan** | 6 ô cố định, chỉ hiện lúc bày trận và lúc nghỉ (nguồn: Rồng DESIGN §11 câu 8) |

### 8.3 Cơ quan

Đặt lúc bày trận và lúc nghỉ, **tự kích hoạt, không cần gõ ở MVP** (nguồn: Rồng D13). Mua bằng Linh Sa.

| Cơ quan | Ô | Tác dụng cấp 1 (số thử, × g(K)) | Giá | Mạnh với | Mốc |
|---|---|---|---|---|---|
| Kiếm Thung | Dải đất 4 × 2 m | Chậm 25 %; 0,05 W/s vật lý lên mỗi thú trong dải | 150 | Bầy, sói | M0a |
| Lôi Phù Trụ | Trụ | Mỗi 4 s đánh xích 3 mục tiêu trong 7 m, 0,25 W phép mỗi mục tiêu | 300 | Cụm bầy | M0a |
| Phong Ấn Võng | Trụ | Mỗi 10 s trói thú có W lớn nhất trong 7 m trong 3 s (thú bay bị kéo xuống); −15 Thế | 250 | Giáp, tướng, Vương | M0a |
| Mê Vụ Trận | Vùng r 4 m | Chậm 30 %; thú bay mất mục tiêu 2 s; thú ném trong vùng trượt 50 % | 220 | Bay, ném xa | M1 |

- **Nâng cấp:** cấp 2 giá 70 % giá gốc, hiệu lực chính +45 %; cấp 3 giá 100 % giá gốc, thêm +35 % (tổng 2,7 × giá gốc). **Bán** hoàn 70 %, bán trong cùng lần nghỉ hoàn 100 %. Hiệu ứng cùng loại chồng vùng lấy mạnh nhất (nguồn: `04` §4.6).
- Dựng tối đa (6 ô cấp 3, giá TB 230): ~3.700 Linh Sa. Linh Sa ải chỉ đủ **15–35 %**: mỗi lần mua là một quyết định.
- Khống chế cứng ≤ 35 % thời gian sống của mỗi thú (nguồn: Rồng G15).

### 8.4 Hợp Trận (từ M1, khi có bot hoặc đội)

- Mỗi nhãn tự nạp bằng từ của người giữ: cần `round(24 × k_ghế)` từ hoàn thành (khoảng 70 s ở 35 WPM, cùng thời gian cho mọi tốc gõ **trong khoảng k 0,75–1,30**; ngoài khoảng kẹp thì người rất chậm nạp lâu hơn, PB-32). Bot, pet, đánh nền không nạp.
- Khi **đủ mọi nhãn**, mỗi người nhận **Trận Quyết 2 từ 3–4 chữ của riêng mình**. Cửa sổ của mỗi ghế = **max(T₂; max(8 s; T₂) / k_ghế)** (người chậm được dài hơn, không ai dưới T₂, đúng luật kẹp của mục 10.6) với `T₂ = 1,6 × (0,4 + 2 × (0,5 + 12 × (ℓ + 1) / (0,86 × E_sàn)) + 0,2)`, ℓ = 4: Thư giãn 17,4 s · Cân bằng 11,5 s · Thử thách 8,9 s (PB-16; công thức mục 10.6 cho hai từ). CB5 phủ Trận Quyết. Sức = **40 % + 20 % cho mỗi người gõ xong**. Người chậm làm Hợp Trận yếu đi, không hủy nó; không ai "chốt hộ" cả đội. Trong cửa sổ, ô 2–5 tạm mờ (mục 6.2).
- Ở 100 %: 2,5 W phép lên mọi thú trong Kết Giới (trần cụm 60 %), −30 Thế lên tinh anh, tướng, Vương trong vùng. Hợp Trận ≤ 12 % sát thương cả trận.

## 9. Người chơi

### 9.1 Vị trí, di chuyển, quyền

- **Vị trí, Sinh lực, khiên và trạng thái gục của chính mình do máy mình giữ** (lớp `local`, tất định, có trong replay, băm bằng `hashLocal`). Thế giới chung (thú, Trận Lực, nhãn, cơ quan, `ward`, Hợp Trận, bot, **ví Linh Sa và Thú Hạch theo ghế, loot theo seed, kho đan phù**) nằm trong sim. Thế giới chung **không giữ vị trí người thật**; mọi tác động của người chơi lên thế giới đi qua lệnh có `origin` (phím, đánh nền, đan phù, cứu). Solo dùng cùng kiến trúc (D28, D34; PB-01).
- **Bảng tách quyền** (D34):

| Việc | Thế giới (sim) | `local` |
|---|---|---|
| Hộ thân (ô 3) | Tạo `ward{seat, origin, r 2 m, đến tick, còn 3 lần}` tại `origin` của Cast, đứng yên 5 s; đỡ đòn vào bot, điểm nhãn nằm trong vòng; Thiết Bối Xung mất một nửa nếu vòng `ward` cắt vạch ở tick chạm | Đỡ đòn vào mình khi người đứng trong vòng `ward` ở tick chạm (mỗi lần đỡ trừ một lần của `ward` qua lệnh `ward-use`) |
| Đan, phù | Lệnh `consumable`: kiểm số viên, hồi chung, trừ Linh Sa khi mua; phát `consumable{seat, kind}`; áp tác dụng lên thế giới (Lôi Hỏa Phù, Định Thân Phù) | Áp tác dụng lên mình khi nhận `consumable` của ghế mình (Hồi Xuân Đan hồi, Kim Thân Phù khiên) |
| Đòn trúng vùng | Phát `telegraph strike` (hình, tick) | Tự tính mình có đứng trong vùng ở tick chạm không; trừ Sinh lực, khiên |
| Gục | Nhận lệnh `down{seat, origin}`: Trận Lực −5 % (solo) | Sinh lực 0 → phát `down`; nằm 8 s; dậy ở Trận Tâm |
| Linh Sa, Thú Hạch, loot | Ghi sổ ngay tick thú chết, theo ghế | Chỉ vẽ hạt bay về HUD |

- Lệnh `ward-use{seat, wardId}` do `local` phát vào tick kế; sim trừ một lần đỡ (kẹp ở 0). `local` chỉ đỡ khi `ward` còn lần theo trạng thái thế giới nó đọc được; cùng tick mà thế giới và `local` cùng dùng lần cuối thì cả hai được đỡ (lệch tối đa một lần, chấp nhận). Sim không bao giờ hỏi vị trí người.
- Tốc chạy 5 m/s. Bán kính va chạm 0,4 m. Va chạm với địa hình và Trận Trụ; **không va chạm với thú** và với đồng đội.
- Chuột phải: đi tới điểm theo lưới 0,5 m. Mũi tên: đi thẳng theo hướng màn hình.
- **Đứng trận phải chơi trọn vẹn:** mọi đòn lớn có ít nhất một đáp án làm được khi đứng ở Trận Tâm (gõ Ấn, Hộ thân, cơ quan). Cổng CB4.

### 9.2 Chỉ số

- Sinh lực K0: **600** × g(K). Hồi 30 % lúc nghỉ đợt.
- Trang chỉ số 1 có 6 số: Công, Thủ, Thân pháp, Sinh lực, Giảm hồi (≤ 30 %), Linh căn (hệ = hệ trường phái). Trang 2: kháng hệ. Không có Thọ mệnh, Tâm tình, Niệm lực, May mắn, Ngộ tính, Mệnh cách, kỹ nghệ, tinh thông vũ khí.
- Kỳ nhỏ trong một cảnh giới **không cộng chỉ số**; sức nằm ở g(K) theo cảnh giới (mục 15).

### 9.3 Đánh nền, mục tiêu, nhặt

- **Đánh nền** tự động theo trường phái (bảng 12). Tự chọn thú gần Trận Tâm nhất trong tầm, trừ khi có mục tiêu mềm. Giáp chặn đánh nền.
- Lớp `local` phát lệnh `auto{seat, beast, origin}` theo nhịp của trường phái; sim kiểm tầm theo `origin` (mục 19.2).
- **Nhặt:** Linh Sa và Thú Hạch **ghi sổ ngay tick thú chết**, trong sim, vào ví của ghế (D34). Hạt bay về HUD chỉ là hình. Không có nhãn chữ trên đất cho đồ thường; đồ hiếm có biểu tượng và nhãn ngắn nằm **dưới** mọi lớp chữ.

## 10. Thú

### 10.1 Luật nhắm mục tiêu (bắt buộc)

- Thú chỉ nhắm: **Trận Tâm, điểm nhãn, cổng, bot, điểm khiêu khích** (chiêu của vai Hộ đặt một điểm cố định trên đất tại `origin`), hoặc **một vùng đất có báo trước**.
- Thú **không đuổi theo vị trí người thật** và **không va chạm thân** với người thật. Máy của mỗi người tự tính mình có đứng trong vùng trúng đòn không.
- Hòa điểm khi chọn đích ("gần Trận Tâm nhất", "cụm đông nhất"): mục 23.3.
- Test tính chất: qua 20 seed × mọi bot, 0 thú nào chọn đích là một người thật.

### 10.2 Năm họ thú chương 1

W ở K0, Cân bằng. Máu = round(W × 90 × g(K) × hệ số preset), số nguyên (mục 7.1). Tốc theo m/s.

| Mã | Tên | Họ · bậc · W | Tốc | Vai | Đòn chính (luôn có báo, trừ cắn) | Khắc chế |
|---|---|---|---|---|---|---|
| T01 | Thạch Thử | Thử · Bầy 0,33 W, cụm 6–8 | 1,6 | Bầy áp sát Trận Tâm | Cắn Trận Tâm 1/s mỗi con khi tới mép (r 2 m) | Chiêu vùng, Lôi Phù Trụ, Kiếm Thung |
| T02 | Phong Lang | Lang · Nhỏ 1 W, đàn 3–5 | 1,4 | Áp sát nhanh | Cắn Trận Tâm 2/s | Ô 1, Kiếm Thung, Phong Ấn Võng |
| T03 | Hỏa Nha | Điểu · Nhỏ 0,8 W, bay | 2,0 | Đường trời, bỏ qua cơ quan đất | Bổ nhào xuống vùng r 1,5 m quanh điểm nhãn hoặc mép Trận Tâm: báo 1,5 s; 30 Sinh lực người trong vùng, Trận Lực −3 nếu vùng chạm Trận Tâm | Ô 1, đánh nền, Phong Ấn Võng (kéo xuống), Mê Vụ (M1) |
| T04 | Nham Viên | Viên · Vừa 2 W | 1,0 | Ném xa vào điểm nhãn và Trận Tâm | Dừng cách đích **11 m** (để ô 1 với tới từ Trận Tâm, PB-17), ném mỗi 3 s; vòng báo **1,6 s** (= 1,2 + 2 m ÷ 5 m/s, PB-27); Trận Lực −12 (Trận Tâm) hoặc 40 Sinh lực người trong 2 m của điểm nhãn. **Trận Trụ chặn** | Ô 2 (xuyên tuyến), thân pháp để áp sát, Trận Trụ |
| T05 | Thiết Giáp Trư | Giáp · Vừa 3 W, giáp G2 | 1,0; húc 6 | Giáp dày, **chiếm nhãn** | Húc thẳng vào Trận Tâm: vạch đỏ **1,2 s + thời gian ra khỏi vạch** (PB-27), Trận Lực −40 | Đòn gõ (xuyên giáp), Phong Ấn Võng, Trận Trụ chắn đường |

- **Bậc** (nguồn: Rồng 00 §4.6): Bầy 0,3–0,5 · Nhỏ 0,8–1,2 · Vừa 2–3 · tinh anh W × 1,6 · thú tướng 5–7 · Thú Vương mục 10.5.
- **Hai bất biến hạ thú** (D38, PB-06), phạm vi: **không tâm pháp R (Tích Kiếm), không khắc hệ ×0,80**, mọi preset (bầy và Nhỏ không nhân hệ số máu preset, mục 13.4). Một từ ô 1 = P_ref × M_q = 100 máu × M_q ở K0, tính một lần rồi chia 3 kiếm (dư vào kiếm cuối): từ Vừa = 90 máu = 30 + 30 + 30.
  - Thú bầy (30 máu) chết với **một kiếm** của ô 1 không Ẩu (≥ 30 máu).
  - Thú Nhỏ 1 W (90 máu) chết với **một từ** ô 1 không Ẩu, khi cả 3 kiếm trúng nó (≥ 90 máu).
  - Test: `tests/sim/combat-kill-invariants.test.ts` kiểm cả hai ở Thư giãn, Cân bằng, Thử thách, Học.
- Chương 1 vô hệ ở trận dạy. Biến chủng hệ từ trận 4: **Đằng Thử** (Thạch Thử, Mộc) và, ở M1, **Khê Viên** (Nham Viên, Thủy) (D23, mục 11).
- Sau MVP: Huyễn Hồ, Độc Mãng, Nham Quy, Lôi Điêu, thú đào hang; họ Thủy, Mộc mới.

### 10.3 Tinh anh

- Thú thường mang **1 thuộc tính** tinh anh (MVP; 2 thuộc tính từ chương 3), W × 1,6, **Thế 40**, mang **1 Ấn** khi lộ. Hình: × 1,25 cỡ, chất liệu và hào quang, **không model mới**.
- Ba thuộc tính MVP: **Cuồng** (+30 % tốc) · **Thiết Bì** (+2 W, giáp +1 bậc) · **Hồi Nguyên** (hồi 1,5 % máu/s sau 3 s không trúng đòn).
- Tỉ lệ ở chương 1: 3–5 % số thú không phải bầy. Bộ điều nhịp có thể thêm hoặc bớt một thuộc tính ở toán kế (mục 13.2).
- Ấn: tối đa 2 Ấn sống mỗi người; tinh anh gần Trận Tâm nhất nhận Ấn trước.

### 10.4 Thú tướng: Lang Đầu Đàn

- 7 W, **Thế 60**, 1 Ấn. Hào quang 6 m: sói +15 % tốc.
- **Tru Đàn**: báo 1,5 s (sóng vòng), gọi 3 Phong Lang ở cổng gần nhất. Không có đáp án gõ trong lúc báo; giải bằng chiêu vùng, Kiếm Thung, Lôi Phù Trụ. Tối đa 1 lần mỗi 20 s và **2 lần mỗi đợt** (tối đa 6 W gọi thêm). Chỉ gọi khi trần thú sống còn đủ 3 suất; không thì **bỏ lượt** (không xếp hàng). W gọi tối đa tính vào máu đợt (mục 13.1; PB-09).
- W tướng ≤ 35 % máu đợt của đợt đó (nguồn: Rồng 00 §4.5).

### 10.5 Thú Vương: Thiết Bối Lang Vương

- Lang · Kim · **W 64** (máu 5.760 ở K0). `W_Vương = round(0,7 × D_đơn × t / 60)`, t đích **120 s ở 35 WPM** (~160 s ở k 0,75) ở mọi trận có Vương (D37; PB-04). Máu theo số ghế: × 1,0 / 1,7 / 2,4 cho 1 / 2 / 3 ghế; Thất Tinh × 5,0. Khóa lúc vào trận.
- **Tải phụ của Gọi Đàn ≤ 30 % W_Vương** (≤ 19 W ở K0 solo; PB-09): mỗi lần gọi 1 cụm Thạch Thử + 2 Phong Lang = 4,31 W; **P1 mỗi 30 s, P2 không gọi, P3 mỗi 18 s** (ước 4 lần, ~17 W). Chỉ gọi khi trần thú sống còn đủ suất; không thì bỏ lượt, không xếp hàng.
- **Thanh Thế 100** mỗi pha, đầy lại khi chuyển pha.
- Luật chung (nguồn: Rồng 02 §4.1): đòn thường báo trên đất ≥ 1,2 s; **tối đa 2 cơ chế cùng lúc, 1 Ấn mỗi người mỗi lúc**; không đòn ngẫu nhiên không báo. Chuyển pha: gầm 2,5 s, miễn sát thương, Ấn cũ bị hủy.

| Pha | Đòn và báo trước | Cách giải (≥ 2, ít nhất 1 không cần gõ) |
|---|---|---|
| P1 (100–60 %) | **Vồ Xé**: nón 6 m hướng về điểm nhãn hoặc bot gần nhất, báo 2,0 s; 60 Sinh lực người trong nón. **Tru Gọi Đàn** mỗi 30 s: 1 cụm Thạch Thử + 2 Phong Lang, sóng vòng báo 1,5 s | Ra khỏi nón; Hộ thân. Chiêu vùng, cơ quan cho đàn |
| P2 (60–30 %) | **Thiết Bối Xung**: vạch đỏ từ Vương tới Trận Tâm, nạp **T** (mục 10.6); Ấn hiện trên Vương. Không Gọi Đàn | (a) Gõ Ấn + chiêu có Thế để phá thế: hủy cú húc. (b) Vương đâm Trận Trụ còn lành nằm trên vạch: choáng 2 s (không tính phá thế), cột mất một lần chịu. (c) Hộ thân với vòng `ward` **cắt vạch ở tick chạm**: Trận Lực chỉ mất một nửa (tính trong sim từ `ward`, D34). (d) Phong Ấn Võng trói đúng lúc nạp: −15 Thế. Không giải: Trận Lực −8 %, người trong vạch bị hất 3 m (`local` tự tính) |
| P3 (< 30 %) | **Cuồng**: tốc +25 %. Gọi Đàn mỗi 18 s. Thiết Bối Xung mỗi 15 s (tính từ lúc cú trước xong) | Như P2 |

- Phong ấn Thú Vương lấy vật liệu pet: sau MVP, cùng pet.

### 10.6 Công thức báo trước (một công thức duy nhất)

```text
T = 1,6 × (0,4 đọc + 0,5 nhận từ + 12 × (ℓ + 1) / (0,86 × E_sàn) + 0,2 hoạt ảnh + t_kênh)
E_sàn: Thư giãn 15 · Cân bằng 25 · Thử thách 35 · Học 15 (WPM)    t_kênh = 0 với Typing; Voice dùng số đo thật
```

| ℓ (chữ) | Thư giãn (E 15) | Cân bằng (E 25) | Thử thách (E 35) |
|---|---|---|---|
| 4 | 9,2 s | 6,2 s | 4,9 s |
| 5 | **10,7 s** | **7,1 s** | **5,6 s** |
| 6 | 12,2 s | 8,0 s | 6,2 s |
| 7 | 13,7 s | 8,9 s | 6,9 s |

- Áp cho **mọi đòn có đáp án gõ**, với ℓ = độ dài lớn nhất của dải từ đáp án ở preset đó (Ấn: Thư giãn và Học 5, Cân bằng 6, Thử thách 7 → nạp Thiết Bối Xung tối thiểu 10,7 / 8,0 / 6,9 s).
- Thời gian nạp giãn theo nhịp k nhưng **không bao giờ dưới T**: `nạp = max(T_preset, nạp_gốc / k)`. Hàm runtime duy nhất: `chargeTicks(def, preset, k)`.
- **Test dữ liệu (CB5, PB-28):** gọi đúng `chargeTicks(def, preset, k)` với k ∈ {0,75; 1; 1,30} và ℓ lớn nhất của dải đáp án ở cả 4 preset; kết quả ≥ T. Phủ cả Trận Quyết (T₂, mục 8.4) từ M1.
- **`telegraphScale`** (kit `balance/pace.ts`, đòn bẩy "báo trước × 0,85–1,5" của BALANCE §4.1): **M0a không dùng**. Khi dùng: `nạp = max(T, nạp_gốc × telegraphScale / k)`, không bao giờ dưới T (đã chọn theo đề xuất, 25/10).
- Đòn **không** có đáp án gõ (né bằng chân, Hộ thân, cơ quan): báo **≥ 1,2 s + (nửa bề rộng vùng ÷ 5 m/s)**. Test dữ liệu `tests/sim/telegraph-floor.test.ts`: mọi `TelegraphDef` không có đáp án gõ đạt sàn này (PB-27). Hình dạng `TelegraphDef`: mục 23.3.
- Trong lúc có đòn cần đáp án gõ đang báo, không đưa từ mới lên ô nào.

### 10.7 Thế và phá thế

- Thế: tinh anh 40 · thú tướng 60 · Thú Vương 100 mỗi pha. Thế không tự hồi (trừ khi Vương chuyển pha).
- Giảm Thế: **Ấn −35** (solo; đội: −35 / √số ghế) · chiêu có nhãn Thế theo bảng 12 · Phong Ấn Võng −15 · mỗi 1 W sát thương gõ −1.
- Thế về 0: **phá thế** — địch ngã 6 s, nhận ×1,5 sát thương. Sau đó **15 s Thế không giảm** (chống khóa boss mãi), rồi đầy lại.

### 10.8 Áp lực liên tục (nguồn: `BALANCE.md` §5)

- Thú tới mép Trận Tâm cắn Trận Lực mỗi giây (bầy 1, Nhỏ 2, Vừa 4); Nham Viên ném khi trong tầm; Hỏa Nha bổ nhào vùng quanh nhãn; Thiết Giáp Trư húc. Gõ nhanh và chuẩn thì mất ít Trận Lực hơn một cách liên tục.
- Sát thương thú lên Trận Lực và người chơi × g(K) × hệ số preset (mục 13.4).

### 10.9 Trình bày thú

- Trúng đòn là **vệt mực**; chết tan thành **khói mực và đốm linh quang**. **Không có máu** ở mọi hồ sơ.
- Thú thường đọc được bằng dáng: bốn chân thấp dài, hai chân cao, bay lơ lửng, bầy là khối nhỏ đi cụm.

## 11. Ngũ hành

```text
Tương khắc (sát thương):  Kim → Mộc → Thổ → Thủy → Hỏa → Kim
Tương sinh (sau MVP):     Mộc → Hỏa → Thổ → Kim → Thủy → Mộc
```

- MVP **chỉ có khắc**: chiêu khắc hệ thú ×1,30; hệ thú khắc hệ chiêu ×0,80. Trần tổng hệ số hệ 1,60, sàn 0,60. Không miễn nhiễm tuyệt đối.
- **Hệ người chơi = hệ trường phái:** Kiếm = Kim, Thổ thể = Thổ, Phù = Hỏa (sau MVP). Ba ghế Hỏa → Thổ → Kim là một chuỗi tương sinh cho Tam Tài sau này. Đánh nền, cơ quan, đan **vô hệ**.
- Chương 1: mọi họ **vô hệ** ở trận dạy (Phong Lang vô hệ cả chương). Từ trận 4: biến chủng **Đằng Thử** (Mộc; Kiếm khắc ×1,30). M1 thêm **Khê Viên** (Thủy; Thổ thể khắc ×1,30). Thiết Bối Lang Vương hệ Kim (không ai trong MVP khắc nó). Biến chủng dùng chung GLB của họ, đổi dữ liệu và chất liệu.
- Hệ nhận bằng **hình trước màu**: Kim mũi kiếm, Mộc lá, Thủy giọt, Hỏa lửa, Thổ khối vuông. Viền ô sáng khi mục tiêu hiện tại bị hệ ô đó khắc.
- Sau MVP: tương sinh và dấu hệ, dị hệ Lôi (thuộc Kim), Phong (thuộc Mộc), Băng (thuộc Thủy), thú khắc người ×1,20, boss đổi hệ theo pha.

## 12. Trường phái, thân pháp, đan phù

Mỗi trường phái: đánh nền + 4 chiêu + tuyệt kỹ + 2 tâm pháp (chọn 1 trước trận ở MVP). Một trục vai: trường phái cấp bộ chiêu cho vai; hệ không phải vai. Số ở K0, × g(K).

### 12.1 Kiếm (vai Công, hệ Kim, M0a)

| Ô | Tên tạm | Tác dụng (số thử) | Hồi | Kiểu tung |
|---|---|---|---|---|
| Đánh nền | Phi Kiếm | 1 kiếm mỗi 1,2 s, 0,25 W vật lý, tầm 10 m | 1,2 s | Tự động |
| 1 Liên tục | Ngự Kiếm Quyết | Mỗi từ nạp 1 băng 3 kiếm. Sát thương gõ **tính một lần mỗi từ** (P_ref × M_q × …: 100 máu × M_q ở K0, ≈ 1,11 W × M_q) rồi chia 3 kiếm, dư vào kiếm cuối (D38); xả vào mục tiêu mềm hoặc thú gần Trận Tâm nhất trong 12 m; mỗi kiếm xuyên thêm 1 thú nhỏ (50 %). Chờ tối đa 2 băng | 0 | Khi đi |
| 2 Chiêu A | Nhất Tuyến Xuyên Vân | Đường 14 × 1,2 m về phía mục tiêu mềm hoặc cụm gần Trận Tâm: **2,5 W** thú đầu, −15 % mỗi thú sau (sàn 40 %); **Thế −20** (2,0 → 2,5 theo phần gõ mới, PB-05) | 8 s | Khi đi |
| 3 Hộ thân | Hồi Kiếm Hộ Thân | Đặt **`ward`** r 2 m tại `origin` của Cast, 5 s, **3 lần đỡ** (đá ném, bổ nhào, nón, sét): đỡ cho bot, điểm nhãn nằm trong vòng (sim) và cho mình khi đứng trong vòng (`local`); vòng cắt vạch đòn lớn ở tick chạm thì đòn đó mất một nửa (sim). Bảng tách quyền: mục 9.1 (D34) | 15 s | Khi đi |
| 3 Thân pháp (thay Hộ thân) | Lưu Quang Bộ (chung) | Lướt 5 m theo hướng đang đi hoặc hướng con trỏ; 0,3 s không bị đẩy; không miễn thương | 8 s | — |
| 4 Chiêu B | Lạc Kiếm Trận | Vùng r 3 m trong 5 s tại con trỏ hoặc cụm đông nhất trong 12 m: 0,3 W/s mỗi thú, chậm 20 %; **trần 4 W cho mỗi lần tung, cộng mọi thú** | 12 s | Đặt đất |
| 5 Tuyệt kỹ | Thiên Hà Kiếm Vũ | 3 loạt trong 2 s, vùng r 6 m tại con trỏ hoặc cụm đông nhất trong 14 m: tổng 10 W chia đều (≤ 2,5 W mỗi thú, trần cụm 60 %); **Thế −40**. Hình: cảnh "vạn kiếm", **150 / 300 / 500 kiếm** ở Low / Medium / High, chỉ là hình (bể kiếm chung với đồng đội, mục 20.2) | Chân Nguyên 100 | Đặt đất |
| Tâm pháp S | Kiếm Tâm | Từ Chớp ở ô 1 thêm 1 kiếm vào băng (tối đa 1 lần mỗi 3 s); kiếm thêm mang 1/3 sát thương của từ đó | — | Bị động |
| Tâm pháp R | Tích Kiếm | Đợt 1: −8 % sát thương chiêu; +4 % mỗi đợt giữ được, trần +24 %. Nằm ngoài phạm vi hai bất biến hạ thú (mục 10.2) | — | Bị động |

- **Ước ở 35 WPM (D_ref), theo chính sách chọn ô của bot (mục 18.3):** ô 1 ~10 W/phút (~8 từ/phút × ~1,2 W; ~21 % sát thương gõ, dưới trần CB3 30 %), ô 2 ~18, ô 4 ~11, tuyệt kỹ ~8 (gõ 47 = 63 % của 75), đánh nền ~12, cơ quan và trận pháp ~16. Đây là số để bot đo, không phải kết quả (PB-05: bản cũ ghi ô 1 ~14 là "~20 %" nhưng thật là 29,8 %).
- **Tick chạm** sau tick Cast (PB-24): ô 1 ba kiếm ở **+6, +36, +66** (băng sau nối sau băng trước); ô 2 ở **+12**; ô 4 vùng mở ở **+12**, mỗi 30 tick một nhịp 0,15 W; ô 5 ba loạt ở **+30, +75, +120**; đánh nền **+18** sau lệnh `auto`. Sim áp sát thương đúng tick đó; view đồng bộ theo sự kiện.
- Kiểu tung chỉ có 3: **khi đi** · **dừng ngắn có báo** (≤ 0,4 s) · **đặt đất** (Codex §1.5 rút gọn).

### 12.2 Thổ thể (vai Hộ, hệ Thổ, M1)

| Ô | Tên tạm | Tác dụng (số thử) | Hồi | Kiểu tung |
|---|---|---|---|---|
| Đánh nền | Trấn Quyền | 1 quyền mỗi 1,0 s, cung 120° r 2,5 m, 0,15 W vật lý mỗi thú, Thế −2 | 1,0 s | Tự động |
| 1 Liên tục | Chấn Địa Quyền | Nón 60° 4 m: 0,6 W gõ mỗi thú (≤ 5 thú), đẩy thú nhỏ 1 m, Thế −8 | 0 | Khi đi |
| 2 Chiêu A | Phá Sơn Chưởng | 3,0 W một mục tiêu, **Thế −35** | 8 s | Dừng ngắn có báo 0,4 s |
| 3 Hộ thân | Kim Cương Thân | 5 s: −50 % sát thương nhận; đặt **điểm khiêu khích** tại `origin` 5 s (thú nhỏ trong 6 m nhắm điểm đó); đội: nhận thay 30 % sát thương của đồng đội trong 4 m | 15 s | Khi đi |
| 4 Chiêu B | Thạch Bích | Tường 5 m chắn đường 6 s, máu 6 W; thú phải phá hoặc vòng | 12 s | Đặt đất |
| 5 Tuyệt kỹ | Sơn Hà Trấn | Nện đất r 7 m: tổng 4 W (≤ 1,5 W mỗi thú), choáng thú nhỏ 2 s (giảm dần), Trận Lực +5 % (tối đa 1 lần mỗi đợt) | Chân Nguyên 100 | Đặt đất |
| Tâm pháp | Hậu Thổ · Bàn Thạch | Hậu Thổ: đứng yên ≥ 1,5 s trong Kết Giới thì −15 % sát thương nhận · Bàn Thạch (R): mỗi lần phá thế +5 % sức khiên và tường, trần +20 % | — | Bị động |

- Thổ thể gây ít sát thương hơn Kiếm, giữ Trận Lực tốt hơn. Cổng CB7: thắng chênh ≤ 8 điểm % với Kiếm ở bot Chuẩn.
- Mỗi trường phái mới sau MVP (Phù trước M3; Hỏa; Ngự thú + pet) phải qua **cổng khác biệt**: CB7 + bộ VFX, âm, dáng riêng được anh duyệt.

### 12.3 Đan, phù

- **2 ô** (ô 3 mở ở Thư Lâu), mỗi ô tối đa **3 viên hoặc 3 lá**. Phím **1 / 2 / 3** hoặc click; **hồi chung 8 s**. Mua lúc nghỉ bằng Linh Sa; không mang sang trận sau; không xóa chữ đang gõ dở. **Không gõ để dùng đan, phù**; không thưởng học. Không có đan hồi sinh.
- **Tách quyền** (D34, PB-01): sim giữ số viên, hồi chung, Linh Sa, nhận lệnh `consumable{seat, slot, origin, aim}` và phát sự kiện `consumable{seat, kind}`; tác dụng lên thế giới (Lôi Hỏa Phù, Định Thân Phù) do sim áp; tác dụng lên chính mình (Hồi Xuân Đan, Kim Thân Phù) do `local` áp khi nhận sự kiện của ghế mình.

| Món | Tác dụng (× g(K)) | Giá | Mốc |
|---|---|---|---|
| Hồi Xuân Đan | Hồi 25 % Sinh lực trong 2 s | 30 | M0a |
| Kim Thân Phù | Khiên 20 % Sinh lực tối đa, 8 s | 40 | M0a |
| Lôi Hỏa Phù | Ném vùng r 3 m tại con trỏ hoặc cụm đông nhất trong 14 m: 1,6 W phép mỗi thú (trần cụm 60 %) | 50 | M0a |
| Định Thân Phù | Mọi thú chậm 40 % trong 4 s (Thú Vương 20 %) | 70 | M1 (mở ở Thư Lâu) |

- Đan, phù tính vào bucket và trần chung (mục 7.2). Sau MVP: Hộ Trận Phù, đan giải trạng thái; "Dẫn Dược" (gõ từ ôn thì đan +25 %) chỉ khi thử đạt.

## 13. Đợt, tải, bộ điều nhịp

### 13.1 Tải đợt (D13)

```text
Máu đợt (W) = L × D_ref × phút của đợt          // D_ref của bot Chuẩn, trường phái Kiếm, K của chương
```

| Đợt trong trận | Tải trung bình đợt | Đỉnh ngắn (6–10 s) |
|---|---|---|
| Đợt 1 | 0,55–0,65 | — |
| Đợt giữa | 0,75–1,00 | ≤ 1,15 |
| Đợt cuối | 1,05–1,25 | ≤ 1,30; trần cứng 1,40 |
| Trận dạy | ≤ 0,85 | ≤ 1,00 |

(nguồn dải: Rồng 00 §4.4)

- Mỗi đợt có 2–3 đỉnh dài 6–10 s và quãng lặng ≥ 8 s. Mỗi cổng ra tối đa một toán mỗi 1,5 s; hai cổng cách nhau ≥ 0,6 s; luật cổng chỉ giãn, không bao giờ ngắn hơn hai số này (nguồn: Rồng 02 §5.3, 01 §1.4).
- Dải tải **giống nhau ở mọi chương**. Chương sau khó hơn nhờ thành phần, hệ, cơ chế, luật ải (D30). Đầu chương sau dễ hơn đỉnh chương trước khoảng 25 % đe dọa.
- **Máu đợt gồm W gọi tối đa** của mọi thú triệu hồi trong đợt (Tru Đàn: tối đa 2 lần × 3 W); thành phần gốc giảm tương ứng. Lọc giải tích tính cả phần gọi (PB-09). Gọi Đàn của Thú Vương là tải phụ của pha Vương, có trần riêng (mục 10.5).
- Lọc giải tích trước khi chạy sim: máu đợt tính bằng công thức; đợt lệch > 25 % bị loại (nguồn: Rồng 00 §8). Kế hoạch đợt viết theo hình dạng `WaveDef` (mục 23.3).

### 13.2 Bộ điều nhịp (nguồn: `BALANCE.md` §4.2, kit `balance/director.ts`)

- Mỗi 5 s (300 tick) tính độ căng từ P, I, O và biên Trận Lực của 20 s gần nhất. Mỗi đợt đổi tối đa 2 bậc; trần cả trận: khoảng sinh ±15 %, máu và danh sách loài ±10 %.
- Một bậc là một trong: khoảng sinh toán kế ±7 % · thêm hoặc bớt một thuộc tính tinh anh ở toán kế · dời đỉnh ±3 s · quãng lặng ±3 s · thả một **Linh Dịch** (+5 % Trận Lực) khi gần thua, tối đa 1 lần mỗi đợt.
- **Không bao giờ:** đổi máu thú đang sống, cho thú tự chết, đổi pha boss, đổi từ, đổi cách chấm.
- Tắt ở bảng xếp hạng, Triều Vô Tận, đội xếp hạng. Cài đặt có dòng "Nhịp tự điều theo cách bạn gõ: Bật/Tắt" (mặc định Bật). Mỗi lần đổi ghi sự kiện `pace`.

### 13.3 Ải hộp xám M0a: Thanh Thạch Ải, 6 đợt + Thú Vương (số thử)

Cân bằng, k = 1, D_ref thử 75 W/phút. Cụm Thạch Thử = 7 con × 0,33 W = 2,31 W. Tinh anh thay một con cùng loài.

| Đợt | Dài | Cổng | L (đỉnh) | Máu đợt | Thành phần | Số con |
|---|---|---|---|---|---|---|
| 1 | 40 s | A | 0,60 | 30 W | 4 cụm Thạch Thử + 14 Phong Lang + 3 Nham Viên | 45 |
| 2 | 45 s | A, B | 0,75 | 42 W | 5 cụm + 16 Phong Lang + 4 Nham Viên + 2 Thiết Giáp Trư | 57 |
| 3 | 50 s | A, B, trời | 0,85 | 53 W | 6 cụm + 14 Phong Lang + 8 Hỏa Nha + 4 Nham Viên + 3 Thiết Giáp Trư; 1 tinh anh (Phong Lang Cuồng) | 71 |
| 4 | 55 s | A, B, trời | 0,93 (1,15) | 64 W (gồm ≤ 6 W gọi) | **Lang Đầu Đàn** + 7 cụm + 8 Phong Lang + 6 Hỏa Nha + 5 Nham Viên + 4 Thiết Giáp Trư; Tru Đàn ≤ 2 lần | 73 (+ ≤ 6 gọi) |
| 5 | 55 s | A, B, trời | 1,00 | 68,6 W | 9 cụm + 13 Phong Lang + 6 Hỏa Nha + 5 Nham Viên + 5 Thiết Giáp Trư; 2 tinh anh (Trư Thiết Bì, Viên Hồi Nguyên) | 92 |
| 6 | 60 s | A, B, trời | 1,13 (1,30) | 84,6 W (gồm ≤ 6 W gọi) | Lang Đầu Đàn + 11 cụm + 10 Phong Lang + 8 Hỏa Nha + 7 Nham Viên + 4 Thiết Giáp Trư; 2 tinh anh (Phong Lang Cuồng, Viên Thiết Bì); Tru Đàn ≤ 2 lần | 107 (+ ≤ 6 gọi) |
| Lặng | 8 s | — | — | — | Thú cũ vẫn đi | — |
| Vương | ~120 s | A | — | 64 W (+ Gọi Đàn ≤ 19 W) | Thiết Bối Lang Vương + Tru Gọi Đàn (mục 10.5) | — |
| **Cộng** | **~9,7 phút** | | TB 0,90 | **≈ 342 W + 64 W** | **445 con (+ ≤ 12 gọi), ~66 % là bầy** | |

- Sửa 25/10 (PB-09): đợt 5 hạ từ L 1,05 (72 W) về 1,00 (bỏ 1 Nham Viên, 1 Phong Lang) vì đợt 5 là đợt giữa (≤ 1,00); đợt 4 và 6 tính cả Tru Đàn tối đa (bớt 6 Phong Lang mỗi đợt), trước đây phần gọi đẩy đợt 6 lên L 1,27.
- **Trần thú sống của luật: 60** ở M0a, mọi bậc máy (D12). Chạm trần thì toán mới chờ ở cổng; đồng hồ đợt không dừng (nguồn: Rồng 00 §4.8); đợt chỉ kết thúc khi mọi toán đã sinh (mục 4.1). Nâng trần theo HN0 (mục 20.4): đề xuất **120 ở M1 nếu HN0 ở Low đạt với N = 120** (3D đầy đủ hoặc sau thang lùi theo phần vượt), rồi chạy lại bot (PB-19).
- Khi làn bot đo xong D_ref, máu đợt tính lại theo mục 13.1; số con trong bảng đổi theo.

### 13.4 Preset

| | Thư giãn | Cân bằng | Thử thách | Học |
|---|---|---|---|---|
| Máu thú (trừ bầy, Nhỏ) | ×0,85 | ×1,00 | ×1,15 | ×0,85 |
| Sát thương thú | ×0,7 | ×1,0 | ×1,2 | ×0,7 |
| Tốc thú | ×0,9 | ×1,0 | ×1,05 | ×0,9 |
| Nghỉ đợt | Chờ Enter | 20 s (Đại Triều 15 s) | 15 s | Chờ Enter |
| Đợt của trận trộn | 5 | 6 | 6 | 5 |
| E_sàn báo trước | 15 | 25 | 35 | 15 |
| Chữ sống | ≤ 5 | ≤ 8 | ≤ 8 | ≤ 5 |
| Dài Ấn (chữ) | 3–5 | 4–6 | 4–7 | 3–5 |
| Nghĩa trên Bàn Quyết | Luôn hiện | Theo số lần nhớ đúng | Chỉ lần gặp đầu | Luôn hiện; Thẻ Ôn mặc định 3 câu |
| Dải đích bộ điều nhịp | Thư giãn | Cân bằng | Thử thách | Thư giãn |
| Thú Hạch thưởng | ×0,8 | ×1,0 | ×1,25 | ×0,8 |

- Đổi preset ở Trận Đài trước mỗi trận; không đổi giữa trận. Sao tính như nhau. Hồ sơ trẻ em mặc định Thư giãn. Thua 2 lần liền một trận: gợi ý hạ một mức, không ép.

## 14. Kinh tế

### 14.1 Ba tiền (D21)

| Tiền | Phạm vi | Nguồn | Dùng cho |
|---|---|---|---|
| **Linh Sa** | Trong ải, mất khi hết ải | Quỹ ải (14.2) | Cơ quan, nâng, đan, phù |
| **Văn Khí** | Giữ mãi | **Chỉ từ học**: từ mới gõ đúng lần đầu +1 · **mỗi từ khác nhau** đến hạn, gõ đúng lần đầu trong trận +1 (không theo số lần gõ, PB-31) · Thẻ Ôn đúng +1 · lĩnh ngộ xong một công pháp +5. Trần mềm 300 mỗi ngày, phần vượt × 0,25 | Thư Lâu |
| **Thú Hạch** | Giữ mãi | Lần đầu đạt ★ / ★★ / ★★★ ở một trận: +3 / +2 / +3 (cộng 8) · Thú Vương lần đầu +20 · trong trận: tinh anh +1, thú tướng +2 · Linh Sa dư đổi `min(3; floor(dư / 100))` · chơi lại 30 % · thua, rút lui giữ 50 % | Bảo Khí Lò |

- Tên đồ rơi (nanh, lõi thú, lá linh thảo) chỉ là **hình** của khoản đã ghi sổ. Không túi vật liệu, không gộp phẩm, không tiền thật, không gacha, không thể lực.

### 14.2 Linh Sa (nguồn công thức: Rồng 00 §4.9)

```text
Linh Sa ải = 200 (đầu ải; Thư Lâu +20 / +40) + 900 × f_cổng × f_loại
f_cổng (cổng đất, không tính đường trời): 1 → 1,00 · 2 → 1,25 · 3 → 1,45
f_loại: trận dạy 0,6 · trận trộn 1,0 · Đại Triều 1,2 · ải hộp xám M0a 1,0
Chia 900 × f: hạ thú 60 % (theo ĐĐ; cụm bầy trả một lần khi con cuối chết)
              · hết đợt 25 % (đợt sau +10 % so với đợt trước)
              · học 15 %, tính từ quỹ (PB-07):
                  Thẻ Ôn mỗi câu đúng = round(0,15 × 900 × f × 0,8 / (3 × số lần nghỉ))   tối đa 3 câu mỗi lần nghỉ
                  Học trước mỗi từ     = round(0,15 × 900 × f × 0,2 / 8)                   tối đa 8 từ
```

- **ĐĐ** (phần đe dọa, PB-24) = W gốc của thú ở K0 Cân bằng; cụm bầy = tổng W cụm, trả khi con cuối chết; tinh anh W × 1,6; thú gọi thêm 50 % W của nó. Mỗi lần hạ trả `round(0,60 × 900 × f × ĐĐ / ΣĐĐ_trận)`; ΣĐĐ_trận tính từ `WaveDef` lúc nạp trận, gồm phần gọi tối đa, **không gồm Thú Vương** (Linh Sa sau Vương không còn chỗ tiêu). Quỹ cố định: gọi ít hơn tối đa thì nhận ít hơn, không bao giờ hơn quỹ.
- **Ví dụ ải M0a** (2 cổng, f = 1,25; 5 lần nghỉ): quỹ học 168,75 → Thẻ Ôn **9** mỗi câu đúng (tối đa 135), Học trước **4** mỗi từ (tối đa 32), cộng 167. Tổng tối đa 200 + 1.125 = **1.325 Linh Sa** (sai số làm tròn ≤ 3) ≈ 36 % mức dựng tối đa (~3.700), trừ đan, phù còn khoảng 30 %.
- **Trận dạy một cổng** (f = 0,6; 4 lần nghỉ): Thẻ Ôn 5, Học trước 2 (tối đa 60 + 16 = 76). Bot làm đủ học hơn bot bỏ qua: M0a +14,4 % (167 / 1.156), trận dạy +11,5 % (76 / 659): KT4 đúng theo cấu tạo.
- Khám phá (Linh Mạch, Bảo Hạp) là sau MVP; khi có, lấy từ quỹ 15 % và chênh giữa người đứng trận và người đi thu ≤ 10 %.
- Giá trong ải **không đổi theo chương**; hiệu lực nhân g(K). Mọi món có "điểm hiệu dụng mỗi Linh Sa" trong 0,8–1,2 lần món tham chiếu (KT2).

### 14.3 Cửa hàng lúc nghỉ

- Mở ở bày trận và lúc nghỉ đợt. Trong đợt chỉ dùng đồ đã có. Không mở bảng lớn khi thú đang tràn.
- Hàng cố định, không ngẫu nhiên. Mua, đặt, nâng, bán cơ quan; mua đan, phù. Bán hoàn 70 %, trong cùng lần nghỉ 100 %.
- Không gõ để mua, đặt, nâng. Bàn phím: chế độ cửa hàng (`` ` ``, mục 5.1, D45); chuột: dải cửa hàng.

### 14.4 Thư Lâu (Văn Khí; MVP 5 bậc)

Giá bậc k = `50 × 1,35^(k − 1)`: 50 · 68 · 91 · 123 · 166 (cộng 498).

| Bậc | Mở |
|---|---|
| 1 | Ô đan, phù thứ 3 |
| 2 | Linh Sa đầu ải +20 |
| 3 | Phù phương Định Thân Phù (vào cửa hàng) |
| 4 | Sinh lực hồi lúc nghỉ 30 % → 40 % |
| 5 | Linh Sa đầu ải +40 (thay +20) |

Sau MVP: 10 bậc, đan phương, thi lên cấp từ.

### 14.5 Bảo Khí Lò và pháp bảo (Thú Hạch)

- **Pháp bảo** (1 ô Pháp Bảo Bản Mệnh, món cố định, không độ hiếm, không dòng phụ): mở 40; cấp 2 / 3 / 4 / 5 = 30 / 50 / 80 / 120. MVP mỗi trường phái 1 món (món 2 sau MVP; D32):
  - Kiếm: **Thanh Phong Kiếm** — sát thương chiêu Kiếm +6 / +9 / +12 / +15 / +18 % theo cấp.
  - Thổ thể: **Hậu Thổ Ấn** — sức khiên, tường, giảm sát thương nhận +6 → +18 %.
  - Pháp bảo đổi màu VFX và tiếng của chiêu, không đổi model nhân vật. Khí Linh (ngoại hình, lời thoại) sau MVP.
- **Cấp cơ quan** (tài khoản): cấp 2 / 3 / 4 / 5 = 10 / 20 / 35 / 55 Thú Hạch, mỗi cấp +6 % hiệu lực chính (trần +24 %).

### 14.6 Chống cày

- Đường chính **không cần chơi lại**: bot 35 WPM với bộ đồ trung bình thắng ≥ 55 % mọi trận không phải boss (KT3).
- Tài khoản nâng hết chỉ mạnh hơn "bộ đồ trung bình" cùng cảnh giới **tối đa 25 %**, tính cả pháp bảo, cấp cơ quan, Thư Lâu, Đạo Quả, chênh cảnh giới khi chơi lại.
- "Bộ đồ trung bình": tài khoản đi đường chính một lần, tiêu tiền theo kịch bản mẫu, không chơi lại.

## 15. Tiến trình

### 15.1 Cảnh giới

| K | Cảnh giới | g(K) | Kỳ (k) | Tu vi cần mỗi kỳ (`100 × 1,18^(k − 1)`) | MVP |
|---|---|---|---|---|---|
| K0 | Luyện Khí | 1,00 | 1–3 | 100 · 118 · 139 (cộng 357) | Chương 1 |
| K1 | Trúc Cơ | 1,12 | 4–6 | 164 · 194 · 229 (cộng 587) | Đích cuối MVP (sơ kỳ) |
| K2–K6 | Kim Đan, Nguyên Anh, Hóa Thần, Luyện Hư, Hợp Thể | 1,254 → 1,974 | 7–21 | theo công thức | Sau MVP |

- Tên dùng chuỗi phổ biến của thể loại; **không** dùng các tên riêng trong chuỗi của QCBH (Kết Tinh, Cụ Linh, Ngộ Đạo, Vũ Hóa, Đăng Tiên).
- Lên kỳ nhỏ **tự động** khi đầy tu vi; kỳ nhỏ không cộng chỉ số. Lên cảnh giới chỉ qua Thiên Kiếp.

### 15.2 Tu vi

- Tu vi là thanh kinh nghiệm, không tiêu được. Đường chính cho **≈ 1,08 lần** tu vi cần của cảnh giới **mà không cần học tùy chọn** (D33, PB-29):
  - mỗi đợt giữ được lần đầu ở mỗi trận (D33): **9 tu vi** ở K0 (15 ở K1); chương 1 có **34 đợt** (3 × 5 + 2 × 6 + 7) → 306;
  - Thú Vương lần đầu: **80** (K1: 130). K0: 306 + 80 = 386 = 1,08 × 357. K1: 34 × 15 + 130 = 640 = 1,09 × 587;
  - học (thêm, không cần để mở Thiên Kiếp): Thẻ Ôn đúng +1 (tối đa 3 mỗi lần nghỉ), lĩnh ngộ một công pháp +5.
- Biến thể ít đợt vẫn đủ: Thư giãn (trận trộn 5 đợt) 32 đợt → 368; hồ sơ trẻ em (thêm Đại Triều 6 đợt) 31 đợt → 359 ≥ 357. Test dữ liệu kiểm mọi biến thể ≥ tu vi cần, **không tính học tùy chọn**.
- Chơi lại 30 %. Bot không nhận tu vi.
- Tu vi **không bao giờ** nâng độ thuộc từ hay cấp từ (Codex §17.1, §21.1).

### 15.3 Thiên Kiếp (D22)

- Pha cuối Đại Triều, sau khi Thú Vương ngã, **chỉ khi** người chơi đã đầy tu vi hậu kỳ của cảnh giới. Chưa đủ thì bỏ qua; đánh lại Đại Triều sau.
- 60–90 s, thanh **Kiếp Lực 100**:
  - **Lôi Kiếp**: sét đánh vào ô đất 3 × 3 m có báo ≥ 1,2 s + thời gian ra khỏi ô. Giải: ra khỏi ô, Hộ thân, đứng trong 1,5 m của Trận Trụ. Trúng: Kiếp Lực −10.
  - **3–4 Chấp Ảnh** đi chậm vào Trận Tâm, mỗi bóng mang một **từ yếu của chính người chơi trong game này**, **luôn hiện nghĩa và IPA**. Gõ xong là tan. Bóng chạm Trận Tâm: Kiếp Lực −15. **Đường giải không gõ** (PB-33; luật `08` C3): mỗi bóng có máu 1 W, nhận sát thương của chiêu vùng và cơ quan. Tốc đi tính để thời gian tới Trận Tâm ≥ T của preset với ℓ = 7 (mục 10.6). Trong Thiên Kiếp, ô 2–5 tạm mờ (mục 6.2).
- Kiếp Lực về 0: **đánh lại pha Thiên Kiếp ngay**, không mất gì. Không có tỉ lệ thất bại, không lưu/tải đổi kết quả.
- Qua: lên cảnh giới (kỳ 1 của cảnh giới mới) và chọn **1 trong 3 Đạo Quả**.
- Chớp sáng có trần và theo giảm chuyển động (mục 24).

### 15.4 Đạo Quả (bộ 6 ở MVP)

| Đạo Quả | Tác dụng (một dòng, trong bucket) |
|---|---|
| Kiếm Ý Bất Tán | Đánh nền +15 % |
| Kim Cương Bất Hoại | Hộ thân +1 s |
| Lưu Quang | Tốc chạy +10 %, thân pháp hồi −1 s |
| Trận Linh | Tâm nhãn 2/3 → 3/4 tác dụng; đội: nạp nhãn cần ít hơn 10 % từ |
| Tụ Nguyên | Mỗi đợt bắt đầu với 15 Chân Nguyên |
| Hữu Duyên | Linh Sa đầu ải +30 |

- Ba lựa chọn rút theo seed tài khoản từ bộ 6, ít nhất một hợp vai trường phái đang dùng. Đổi lại miễn phí ở Tĩnh Thất trong cùng bộ 3. Đạo Quả tính vào trần +25 % (mục 14.6).

### 15.5 Cơ Duyên (M1)

- Chỉ sống **trong một trận**: chọn 1 trong 3 sau đợt 2 và đợt 4. Kho MVP: 8 chung + 4 mỗi trường phái. Mọi Cơ Duyên đi qua bucket và trần (mục 7.2); không Cơ Duyên nào lợi riêng cho một kênh nhập.
- Ví dụ (tên tạm): ô 2 hồi −10 % · ô 1 xuyên thêm 1 thú · Kiếm Thung +1 ô dải · Hộ thân đỡ thêm 1 đòn · Thế phá xong +10 Chân Nguyên · Linh Sa hết đợt +15 %.

### 15.6 Công pháp (một mô hình lớn lên, 3 tầng)

- Mỗi công pháp gắn với **một chiêu** và **một bài 6 từ** (một chủ đề hoặc một lát cấp từ của hồ sơ). MVP: mỗi trường phái 3 công pháp, cho ô 2, ô 4, ô 5. **Chiêu dùng được đầy đủ khi chưa lĩnh ngộ** (mở theo trận dạy); công pháp chỉ thêm đường lớn lên.

| Tầng | Điều kiện | Được |
|---|---|---|
| 1 Sơ thành | Lĩnh ngộ: 100 điểm Tĩnh Tu (mục 16) | Chiêu +8 % hiệu lực chính; 6 từ của bài ưu tiên lên ô của chiêu đó khi đã đủ độ quen |
| 2 Tiểu thành | 100 điểm luyện: +1 mỗi lần tung (Cast `resolved`, D42) bằng từ sạch (0 lỗi), tối đa 20 mỗi trận; +10 khi hạ Thú Vương có công pháp đó trong bộ | **Ngộ Chiêu**: chọn 1 trong 2 biến chiêu (xem trước, đổi lại miễn phí) |
| 3 Đại thành (sau MVP) | Thêm ≥ 60 % từ của bài "đã nhớ" (≥ 2 lần nhớ đúng) | Nhánh F (mạnh ngay) hoặc R (tích theo đợt) |

- Phần sức đến từ điều kiện học có trần **≈ 10 % sức trường phái**, để người học chậm không bị bỏ lại. Độ thuộc từ không làm chiêu mạnh hơn (không ai có lý do né từ mới).

## 16. Tĩnh Tu

- **Chỉ bắt buộc khi lĩnh ngộ công pháp** (học 6 từ mới của bài). Không cần để lên tu vi. Miễn phí, không phí mỗi phiên.
- **Trước phiên:** thẻ **Khẩu Quyết** không tính giờ: 6 từ mới, IPA, nghĩa, nghe, gõ lại mỗi từ một lần (`review-card`, `hintUsed: true`, không là lần nhớ).
- **Phiên 60 s:** người tu ngồi trên mặt nước tĩnh; **lá phù giấy dó** trôi vào **3–4 điểm đọc cố định** (Nhập Môn 2–3 chữ cùng lúc, Tham Ngộ 3–4). Không dùng cầu tròn có chữ Hán. Đồng hồ không dừng khi gõ; không chỉ số nào rút ngắn hay kéo dài đồng hồ.

| Loại | Lấy từ | Nhận bằng (viền **và** biểu tượng, không chỉ màu) | Sống được (L = 1,0 + 1,6 × thời gian gõ từ ở E người chơi + 1,0 s; E = E_eff của hồ sơ) | Gõ kịp |
|---|---|---|---|---|
| **Minh** | 6 từ mới của bài; mỗi từ ≥ 2 lần mỗi phiên; lần đầu luôn hiện nghĩa | Viền trắng ngà có tia, biểu tượng mặt trời | L | +5 điểm |
| **Thường** | Từ đến hạn ôn. **Ở Tham Ngộ: chỉ từ cùng nhóm chủ đề với bài** mới để giấy trơn; từ đến hạn khác nhóm giữ dấu riêng (viền nhạt, biểu tượng giọt mực) | Giấy trơn (khác nhóm: viền nhạt, giọt mực) | 1,5 × L | +2 điểm |
| **Tâm ma** | Từ **đã thuộc** (độ thuộc ≥ 70) từ nhóm chủ đề **cách bài ≥ 3 bậc** trên bản đồ 15 nhóm (bảng khoảng cách trong dữ liệu `src/tinh-tu/sim/topics.ts`); bỏ từ đa nghĩa và **mọi từ thuộc ≥ 2 nhóm** (cả ở Thường); **không bao giờ từ mới** | Khói mực tím than, biểu tượng mắt nứt | 2 × L | Không được gõ. Gõ nhầm: ghi "chọn nhầm", −3 điểm phiên |

- **Bậc:** **Nhập Môn** (mọi chữ có nhãn) → **Tham Ngộ** (màn **hiện tên nhóm chủ đề của bài**; 1/3 Tâm ma không nhãn; người chơi nhận theo việc từ có thuộc nhóm của bài không, D40, PB-13) → **Minh Tâm** (sau MVP: chỉ hiện nghĩa Việt, gõ từ Anh).
- **Chấm** (D40, PB-12): **hoàn thành phiên** = đã gõ xong mỗi từ trong 6 từ Minh **ít nhất một lần** trong phiên. Phiên hoàn thành: điểm = `clamp(40 + 5 × Minh + 2 × Thường − 3 × chọn nhầm ; 40 ; 100)` (giữ chữ "≥ 40" của tệp đánh giá §3.6). Phiên chưa hoàn thành: điểm = `max(0 ; 5 × Minh + 2 × Thường − 3 × chọn nhầm)`, không sàn. Cộng dồn qua phiên; **100 là lĩnh ngộ**. Khả thi: 6 từ 4,5 chữ ở E 15 mất ~31 s, bot Trẻ em (E_eff 10,9) ~42 s, đều trong 60 s. Mọi bot 15–90 WPM đạt 100 trong **≤ 2 phiên** (HC4); bot Không gõ không bao giờ lĩnh ngộ (HC4b).
- **Mở bài mới** chỉ khi sổ cái từ mới còn ≥ 6 từ (mục 6.4); không thì phiên ôn (chỉ Thường).
- **Không hai Minh hết hạn trong cùng một cửa sổ 1,5 s** (HC5). Chữ đầu của mọi chữ đang sống khác nhau (kit `letters.ts` bậc 1).
- **Hết hạn khi đang gõ:** ân hạn khóa 1,2 s, rồi tha phím lạc kế tiếp (kit `typing/session.ts`).
- **Sự kiện học:** Minh gõ xong → `review-card` kèm `hintUsed: true` **ở mọi lần**, kể cả lần hai không hiện nghĩa (PB-31: vài giây sau thẻ Khẩu Quyết không phải lần nhớ) · Thường gõ xong → `typing-skill` (có chấm, không là lần nhớ) · Tâm ma gõ nhầm → **không có sự kiện học** (chỉ ghi cục bộ) · nhận đúng Tâm ma không nhãn → không có sự kiện (thuộc chủ đề không phải là hiểu nghĩa). **Không bao giờ tạo sự kiện học âm** (HC6).
- Từ mới của phiên tính vào ngân sách chung (mục 6.4).
- **Bỏ:** thanh Tâm Ma, chỉ số Ngộ tính điều khiển phiên, phí Thú Hạch mỗi phiên, năm hoạt động tu luyện khác của Codex §19.
- Âm nền tĩnh, không nhịp ép; không chuông chùa, không tụng (mục 22). M0a để im lặng.

## 17. Học

- Gửi qua `shared/game-kit/learning` với `gameId` `immortality-cultivation`. Chạy được khi không có portal (xếp hàng cục bộ). **Chỉ người thật gửi sự kiện học**; bot, phân thân, pet, đánh nền thì không (bot dựng nháp để chấm cổng, mục 17.2).
- **Một sự kiện có chấm cho mỗi từ mỗi trận**: lần gõ xong đầu tiên (kể cả Cast `fizzled`). Các lần sau chỉ ghi cục bộ (Sổ Từ, chọn câu Thẻ Ôn). Ngoại lệ luôn gửi: `meaning-recall`, `listening`, `review-card` (nguồn: Rồng 01 §6.6).
- Mọi sự kiện học có trường **`channel`** (`typing` ở MVP). Voice (M4) dùng `activityType` riêng do lõi học định nghĩa ở M4, **không** dùng `typing-*` (PB-31).

| Chỗ | `activityType` |
|---|---|
| Ô 1–5, Tẩy, Trận Quyết | `typing-skill` |
| Ấn trên tinh anh, thú tướng | `typing-elite` |
| Ấn trên Thú Vương, Chấp Ảnh | `typing-boss` |
| Học trước, Khẩu Quyết, Thẻ Ôn gõ lại | `review-card` (Học trước, Khẩu Quyết luôn `hintUsed: true`) |
| Thẻ Ôn chọn nghĩa | `meaning-recall` |
| Thẻ Ôn nghe rồi gõ | `listening` |

- **`hintUsed`** = nghĩa hoặc IPA **đang hiện** lúc gõ, kể cả do preset Thư giãn, Học, cài đặt "luôn hiện". **Ngoại lệ:** Tĩnh Tu Minh, Khẩu Quyết và Học trước **luôn** `hintUsed: true`, mọi lần (PB-31).
- **Lần nhớ đúng** = lần đúng ở `meaning-recall`, `listening`, hoặc `review-card` **không** có `hintUsed`. Nghĩa và IPA trên Bàn Quyết ẩn dần theo số lần nhớ đúng (nguồn: Rồng 01 §6.3).
- **Học trước** (Trận Đài, tùy chọn): từ mới của trận (trong ngân sách), từ, IPA, nghĩa, nghe, gõ lại mỗi từ một lần, không giới hạn giờ. Linh Sa mỗi từ đúng theo mục 14.2 (ải M0a: 4; tối đa 8 từ). Là lần gặp đầu của từ mới (mục 6.4).
- **Thẻ Ôn** (lúc nghỉ, tùy chọn, tắt được): tối đa 3 câu từ đợt vừa xong, thứ tự từ Ẩu → từ có `hintUsed` → từ mới; kiểu câu xoay vòng: nghe rồi gõ; xem nghĩa rồi gõ; chọn nghĩa 1 trong 3 bằng phím 1/2/3. Đồng hồ nghỉ dừng khi thẻ mở (solo). Lớp chữ chiến đấu ẩn khi thẻ mở (không lộ đáp án). Đúng: Linh Sa theo mục 14.2 (ải M0a: 9), +1 Văn Khí, +1 tu vi. Sai: không mất gì, hiện lại từ, nghĩa, IPA.
- **Sổ Từ** ở Thu Hoạch: mới học, gõ sai, cần ôn; bấm để nghe. **Học và RPG báo tách dòng** (Codex §17.1).
- **Phát âm:** luôn phát ở Học trước, Khẩu Quyết, Thẻ Ôn, Sổ Từ. Trong trận phát từ < 40 độ thuộc sau khi cast, từ ô 4 khi mới. Chỉ phát từ của chính mình, trên máy mình. Phát âm không bao giờ kích chiêu.

### 17.1 Bộ từ của trận và khởi đầu lạnh

- Bộ từ của trận: 70–100 từ dựng lúc nạp trận qua `typing-game:learning:v1:query`/`lookup` (nguồn: Rồng 01 §6.1); cấp từ theo hồ sơ (yếu tố 6 của BALANCE), **không theo cảnh giới**. Không lặp từ tới khi dùng hết nhóm (kit `WordPicker`, RNG theo seed), **trừ** từ mới của trận được trả lại cho ô 2, ô 4 tới khi đủ ≥ 3 lần gặp (mục 6.4). Bộ từ chụp vào đầu replay (mục 23.2).
- **Khởi đầu lạnh** (D35, PB-02): hồ sơ không có bản ghi học (trận đầu của người mới, và mọi trận M0a không có lõi học) dùng **từ nền**: tối đa **40 từ tần suất cao nhất của cấp thấp hơn cấp hồ sơ một bậc** (cấp thấp nhất thì 40 từ đầu danh sách A1), cờ `assumed: true`, **dùng thẳng ở ô 1, ô 3, Tẩy**. Từ nền tính là "đã thuộc" cho luật ô, nên ô 2, ô 5, Ấn chỉ nhận từ nền qua bước lùi "quen hơn" của mục 6.2 khi không còn từ đang học hoặc đến hạn (để trận lạnh vẫn chơi được đủ ô; từ nền là từ dễ, không phải từ chưa gặp). Mọi từ khác chưa có bản ghi là **từ mới** và đi qua sổ cái (mục 6.4). Báo cáo in số lần dùng từ nền theo ô.
- **Chép `deck.ts` của Rồng** (`games/dragon-hold/src/typing/deck.ts`): bỏ nhánh hồ sơ trống gắn "đã thuộc" cho 50 từ đầu (dòng 89–92) và nhánh lấp chỗ `candidate.isNew ? "learning"` (dòng 101–105). Nhóm thiếu từ thì **thu nhỏ bộ từ** (sàn 40 từ) và để `WordPicker` lặp sớm hơn; không bao giờ đổi nhãn từ chưa có bản ghi. Ghi vào `docs/SYNC_DEBT.md` của repo game là chỗ cố ý khác Rồng.

### 17.2 Bot và sự kiện nháp

- Bot **không gửi** sự kiện học (D29, D43). Báo cáo bot dựng sự kiện ở **chế độ nháp** (`dryRun: true`, không bao giờ gửi, không vào hàng đợi) theo đúng luật của mục này, để chấm cổng học B8, HC1–HC3, HC7, HC8 (PB-18).
- Hàng đợi học có kiểm cứng: một sự kiện có nguồn là bot hay `dryRun` thì bị chặn và ghi lỗi.

## 18. Cân bằng, bot, cổng

### 18.1 Khung chung

- Dùng nguyên `docs/games/BALANCE.md`: hồ sơ 13 yếu tố, dải đích §3, bộ điều nhịp §4.2, bot §6, cổng **B1–B9** §7. Kit `shared/game-kit/balance` (`SkillProfile`, `FlowMeter`, `PaceDirector`, `HumanTypist`, `runGates`).
- **Không bao giờ dùng dải riêng của game thay dải chung** (D15). Báo cáo in B1–B9 theo dải chung của BALANCE §3.
- Ma trận: bot × preset × **≥ 20 seed**. Bộ điều nhịp bật, trừ khi ghi khác. Chạy `--jobs=4` trên máy Dell.

### 18.2 Cách game đo chỉ số trải nghiệm

- **Áp lực P:** tick có ít nhất một: thú trong Kết Giới; Trận Lực mất máu trong 2 s gần nhất; đòn lớn đang báo.
- **Nhàn I = nhàn quyết định** (D14, D46; PB-17): tick trong đợt mà **cả ba** đúng: (a) không ô nào ngoài ô 1 có chữ sống (ô 2–5 đang hồi, Chân Nguyên chưa đầy, không có Ấn, Tẩy); (b) **tính từ Trận Tâm**, không theo chỗ người đứng: không thú nào trong 12 m của Trận Tâm và không thú nào trong tầm ô 1 (12 m) của người chơi; (c) tick đó **không phải P**. Đây là cách game cấp mẫu cho `FlowMeter`, chặt hơn nghĩa chữ của BALANCE §3 ("không có chữ để gõ và không có quyết định"), không phải dải mới.
- **Ngộp O:** tick có chữ sống chạm trần của preset, hoặc người chơi bỏ khóa ≥ 3 lần trong 5 s.
- **Biên S** = Trận Lực còn lại. **Quãng Q** = phần đường từ cổng tới mép Trận Tâm thú đã đi khi bị hạ (trung vị).

### 18.3 Bot

| Bot | E | a | CV | Chiến thuật | Dùng cho |
|---|---|---|---|---|---|
| Trẻ em | 15 | 88 % | 0,40 | Kém | HC3, B3 |
| Mới | 25 | 92 % | 0,35 | Vừa | B1, B3 |
| Chậm chắc | 25 | 99 % | 0,20 | Vừa | B1, B4 |
| **Chuẩn** | 35 | 95 % | 0,25 | Vừa | Tham chiếu, D_ref |
| Khá | 50 | 96 % | 0,20 | Tốt | B1 |
| Ẩu | 50 | 85 % | 0,35 | Vừa | B4 |
| Nhanh | 70 | 97 % | 0,15 | Tốt | B1 |
| Không gõ | 0 | — | — | Tốt (mua tối ưu) | B5, CB1 |
| Chỉ gõ | 35 | 95 % | 0,25 | Không mua | Báo cáo "hỗ trợ cần thiết" |
| **Đứng yên** | như Chuẩn | | | Vừa; không lệnh di chuyển (đứng ở Tâm nhãn), ô 3 là Hộ thân | CB4; **chính sách đi mặc định** của 9 bot đầu |
| **Cơ động** | như Chuẩn | | | Vừa; đi để giữ cụm đông trong 12 m, né vùng báo | CB4; báo cáo in thêm I của nó để so |
| Đạo đồng (M1) | theo ghế | | | Giữ vai, giữ nhãn | Tam Tài, CB8 |

(nguồn 9 bot đầu: `BALANCE.md` §6)

- **Chính sách đi** (D46): 9 bot đầu chấm B1–B8 bằng chính sách **Đứng yên**; báo cáo in thêm P, I, O của bot Chuẩn Cơ động để so, không dùng để chấm.
- **Chính sách chọn ô** (PB-05), khi có nhiều ô sẵn: **Tẩy → Ấn → ô 5 → ô 2 → ô 4 → ô 3** (Hộ thân chỉ khi có đòn đang báo trúng mình hoặc nhãn; thân pháp khi cần áp sát Nham Viên) **→ ô 1**. Ở preset Học: ô 4 trước ô 5. Chiến thuật "Vừa" bỏ một ô đã sẵn 1–2 s ngẫu nhiên theo seed (luồng `ai`); "Tốt" không bỏ; "Kém" chọn ô ngẫu nhiên trong số ô sẵn.
- Bot dùng `HumanTypist` của kit (nhận từ theo độ quen, Backspace, bỏ khóa, chú ý khi đông, mệt). Bot không biết trước, không có túi đồ, không gửi sự kiện học (chỉ dựng nháp, mục 17.2), không phản ứng 0 giây.
- **Hiệu chỉnh bằng người thật** (B9): mỗi buổi anh chơi thử, game xuất nhật ký (đầu replay mục 23.2 chứa bộ từ, k, `newWordAllowance`, nên chạy lại được); bot cùng E, a chạy lại cùng trận; chỉ số lệch ≤ 15 %.

### 18.4 Bảng cổng

| # | Cổng | Bot, phạm vi | Ngưỡng | Mốc |
|---|---|---|---|---|
| B1–B9 | Cổng chung | `BALANCE.md` §7; 9 bot đầu, chính sách đi Đứng yên | Theo BALANCE §7, dải chung §3. B8 chấm bằng sự kiện nháp (mục 17.2). B9 = buổi anh chơi thử: **M0a chốt có điều kiện, B9 mở** tới khi chạy được (sau Rồng B9, D02) | M0a |
| **CB1** | Gõ là sức chính | Không gõ; Cân bằng, Thử thách | Thua 20/20 seed **trước khi hết đợt 3**; Thư giãn: thua 20/20 | M0a |
| **CB2** | Phần gõ | Chuẩn; Cân bằng | Phần sát thương gõ trung bình **≥ 55 %** (đích ≥ 60 %), không seed nào < 50 % | M0a |
| **CB3** | Ô liên tục có trần | Mới → Nhanh; Cân bằng | Ô 1 **≤ 30 % sát thương gõ** ở mọi bot | M0a |
| **CB4** | Đứng trận chơi trọn vẹn | Đứng yên so với Cơ động, cùng E, a, CV | Chênh thắng **≤ 10 điểm %** ở Cân bằng | M0a |
| **CB5** | Báo trước đủ | Test dữ liệu (vitest) gọi `chargeTicks(def, preset, k)` | Mọi đòn có đáp án gõ, ℓ lớn nhất, k ∈ {0,75; 1; 1,30}, 4 preset: kết quả ≥ T. Từ M1 phủ cả Trận Quyết (T₂). Kèm `telegraph-floor.test.ts` cho đòn không có đáp án gõ (mục 10.6) | M0a |
| **CB6** | Không cast đôi | Replay mọi bot, kể cả dừng hình, tạm dừng, Esc, phím lặp | Mỗi `wordId` hoàn thành → **đúng một** Cast; 0 Cast không có từ hoàn thành | M0a |
| CB7 | Hai trường phái ngang nhau | Chuẩn, Kiếm so với Thổ thể | Chênh thắng ≤ 8 điểm % | M1 |
| CB8 | Đội bot công bằng | Solo + 2 bot so với 3 bot, cùng preset | Chênh thắng ≤ 5 điểm %; đội bot hỗn hợp 15/25/35/70 WPM: P, I, O từng ghế trong dải Cân bằng | M1 |
| **CB9** | Thời lượng (nguồn: Rồng G17; D37) | Chuẩn ở Cân bằng; Trẻ em ở Thư giãn; không tính thời gian có bảng mở | **M0a:** ải M0a 9–10,5 phút với bot Chuẩn; in số của bot Trẻ em (ải M0a là ngoại lệ, mục 25). **M1:** mỗi loại trận trong cột "thời lượng đích" mục 4.1; bot Trẻ em ở Thư giãn **≤ 7 phút** mỗi trận dạy và trận trộn; Đại Triều **≤ 12 phút** với bot Chuẩn | M0a, M1 |
| **HC1** | Từ mới không ở ô gấp | Replay mọi bot, sự kiện nháp | **0** lần một từ **không có bản ghi học trước trận và không thuộc danh sách từ nền** xuất hiện ở ô gấp (mục 6.3; đếm theo bản ghi, không theo nhãn, PB-02); từ mới ở ô 4 chỉ ở đợt 1–2; báo cáo in số lần dùng từ nền | M0a |
| **HC2** | Trần chữ sống | Mọi bot, mọi tick | ≤ 8 (Cân bằng, Thử thách), ≤ 5 (Thư giãn, Học); 0 lần dùng chữ đầu bậc 2 | M0a |
| **HC3** | Trẻ em đi được | Trẻ em; Thư giãn | Thắng **≥ 85 %** | M0a |
| **HC8** | Từ mới gặp lại (nguồn: Rồng G12; D39) | Replay, sự kiện nháp | Mỗi từ mới của trận gặp **≥ 3 lần** (≥ 45 s giữa hai lần, xong trước đợt 4) ở 100 % lượt bot Chuẩn; **≥ 2 lần** ở bot Trẻ em | M0a |
| HC4 | Tĩnh Tu đạt được | Bot 15 / 25 / 35 / 60 / 90 WPM; Nhập Môn và Tham Ngộ; 20 seed | Đạt 100 điểm trong **≤ 2 phiên** ở mọi bot, mọi seed | Tĩnh Tu thử |
| HC4b | Không lĩnh ngộ khi không học (D40) | Bot Không gõ; bot gõ mọi chữ (kể cả Tâm ma) | Bot Không gõ **không** lĩnh ngộ sau 10 phiên. Báo cáo (không chấm): điểm mỗi phiên của bot gõ mọi chữ thấp hơn bot Chuẩn cùng E | Tĩnh Tu thử |
| HC5 | Minh không dồn | Sim Tĩnh Tu, 20 seed | 0 lần hai Minh hết hạn trong cùng cửa sổ 1,5 s | Tĩnh Tu thử |
| HC6 | Không học âm | Sim Tĩnh Tu | 0 sự kiện học âm từ Tâm ma | Tĩnh Tu thử |
| HC6b | Tham Ngộ phân biệt được (D40) | Bot Chuẩn ở Tham Ngộ đoán theo nhóm chủ đề, có lỗi đọc theo `HumanTypist` | Tỉ lệ "chọn nhầm" **≤ 10 %** | Tĩnh Tu thử |
| HC7 | Sự kiện học đúng luật | Bộ kiểm sự kiện (activityType, `hintUsed`, một sự kiện có chấm mỗi từ, `channel`) trên sự kiện nháp; Tĩnh Tu và **trận M0a (bot Chuẩn × 20 seed)** | ≥ 90 % đúng luật (đích 100 %; mọi sự kiện sai được in), **và cứng:** 0 sự kiện `hintUsed: false` khi nghĩa đang hiện; 0 sự kiện có nguồn là bot đi vào hàng đợi (PB-18, PB-37) | Tĩnh Tu thử, M0a |
| KT1 | Linh Sa đúng công thức | Chuẩn; mọi trận | Linh Sa trận trong ±15 % công thức 14.2; dư ≤ 15 % | M1 |
| KT2 | Không món nào là đáp án duy nhất | Định giá dữ liệu + bot Tham một nhóm | Mọi món 0,8–1,2 điểm mỗi Linh Sa; bot Tham không thắng hơn bot Vừa quá 10 điểm % | M1 |
| KT3 | Không cày | 35 WPM, bộ đồ trung bình | Thắng ≥ 55 % mọi trận không phải boss | M1 |
| KT4 | Học có lời | Bot làm đủ Thẻ Ôn và Học trước so với bot bỏ qua | Hơn 10–15 % Linh Sa, không bao giờ > 15 % | M1 |
| NW1 | Tất định qua mạng | 2–3 máy, 20 seed × 15 phút | Mã băm khớp | M3 |
| NW2 | Chịu trễ | Trễ 150 ± 50 ms, mất 2 % gói | Không lệch sim | M3 |
| NW3 | Rớt mạng | Rớt 30 s | Bot thay trong 10 s; quay lại bắt kịp ≤ 3 s | M3 |
| NW4 | Vừa gói Free | Trận 3 người 12 phút | ≤ 250 request DO **và** GB-s đo trên Dashboard Cloudflare | M3 |
| NW5 | Công bằng đội hỗn hợp | Đội người + bot tốc khác nhau | Mỗi ghế trong dải Cân bằng; không ghế nào có thưởng ngoài ải khác solo | M3 |
| **HN0** | Bench 3D | Mục 20.3 | Ngưỡng mục 20.2; phán quyết ghi ở mục 20.4 | M0a |
| HN1 | Hiệu năng có hình thật | Game thật, hình M0b, đợt đông nhất | High: TB ≤ 8 ms, p95 ≤ 12 ms; Low ≤ 16 ms (M4 hoặc GPU tích hợp) | M0b |

- Golden: 20 seed của ải M0a, cùng seed, cùng đầu replay và cùng lệnh ra cùng `hashWorld` **và** `hashLocal` (mỗi 600 tick và cuối trận; mục 23.2, 25).
- Test bất biến: `tests/sim/combat-kill-invariants.test.ts` (mục 10.2), `tests/sim/telegraph-floor.test.ts` (mục 10.6) ở M0a; test dữ liệu tu vi theo biến thể (mục 15.2) ở M1.
- Trận không đạt: chỉnh hệ số trong dữ liệu (±10 %) hoặc đổi thành phần. Không sửa mã để qua cổng.
- Hiệu năng sim: một bước 60 Hz ở 300 thú ≤ 0,3 ms headless; trung bình ≥ 200 lần thời gian thực (nguồn: Rồng 00 §8).

## 19. Đội và online (các mốc sau)

### 19.1 Mô hình

- **Ghế là vai, không phải tọa độ.** Ba vai: **Công** (dọn bầy, phá giáp), **Hộ** (khiên, điểm khiêu khích, cứu người gục), **Trận** (nạp nhãn, Hợp Trận). Mỗi ghế giữ một nhãn và chịu chính một hướng thú (ải Tam Tài có 3 cổng đất).
- **k theo ghế**: thú thường của hướng nào sinh theo k của ghế đó; tinh anh và Vương dùng trung bình k các ghế. Người nhanh không làm cả đội khó lên.
- **Phiên bản trận khóa lúc vào** theo số ghế; bot lấp ghế trống trước trận; không co giãn giữa trận. Máu Vương × 1,0 / 1,7 / 2,4 / 5,0; Trận Lực 1.000 / 1.400 / 1.800 / 3.500.
- **Mỗi người một bộ từ riêng**, chỉ thấy chữ của mình, không tranh từ. Mỗi người tối đa 1 chữ khẩn. Ấn trên Vương: mỗi người một Ấn riêng, mỗi Ấn −35 / √(số ghế) Thế.
- **Loot cá nhân:** quay theo `hash(matchSeed, playerId, beastId)` bằng RNG có seed của kit; máy nào cũng ra cùng kết quả, không gửi qua mạng. Linh Sa mỗi ghế đủ ngân sách như solo, trả theo **tổng đe dọa cả đội đã hạ**, không theo đòn kết liễu. Bot có ví trong ải, không đổi ra thưởng ngoài ải.
- **Thưởng ngoài ải** mỗi người như solo. **Thưởng đội chỉ là danh hiệu.** Màn kết hiện đóng góp theo vai (khiên đã đỡ, Thế đã phá, nhãn đã nạp); không có bảng sát thương.
- **Liên lạc:** không chat gõ tự do ở v1; câu tiếng Anh soạn sẵn ("Hold the gate!", "Need a shield!") qua bánh xe chuột giữa. Chơi Voice trong đội thì gợi ý push-to-talk.

### 19.2 Kiến trúc online (Cloudflare Free, D28)

- **Máy chủ không chạy sim.** Mọi máy chạy cùng sim tất định số nguyên 60 Hz có mã băm. Một Durable Object `TideRoom` mỗi phòng chỉ **đóng dấu tick và phát lại lệnh**, dùng Hibernation. Lệnh gom theo khung, mỗi máy gửi ≤ 10 tin/s.
- **Tách quyền** (D34, bảng mục 9.1): thế giới chung trong sim, kể cả ví, loot, kho đan phù, `ward`; vị trí, Sinh lực, khiên, trạng thái gục của chính mình ở máy mình. Lệnh (phím, `auto`, đan, cứu) mang `origin`; DO từ chối `origin` không hợp lý so với vị trí báo gần nhất. Sự kiện gục mang vị trí; lệnh cứu mang `origin` của người cứu. Vị trí đồng đội gửi `MOVE_HINT` chỉ để vẽ.
- **DO không có timer nào.** Rớt mạng bắt bằng `webSocketClose`, đóng dấu tick rồi phát lại. Giữ ghế 10 s và luật AFK chạy **trong sim** (bot nhận ghế ở tick T + 600). Heartbeat dùng tự trả lời ping của runtime.
- **Ngân sách:** ước ~200 request DO cho trận 12 phút 3 người (tin gửi lên tính 20:1). Dành tối đa 50 % hạn mức Free dùng chung với Space cho co-op; đạt 80 % mức đó thì phòng mới tự chuyển sang "chơi cùng bot" và báo rõ. Không ghi SQLite theo lệnh, chỉ 1 dòng mỗi đợt. **Kiểm lại trang giá và đo GB-s trên Dashboard trước M3.**
- **Danh tính:** co-op dùng mã phòng và danh tính khách; Worker riêng `immortality-cultivation-coop`, token gửi trong `HELLO` như Duel.

### 19.3 Thứ tự

1. Độc tu (M0a). 2. Độc tu + 2 bot thành Tam Tài (M1). 3. Phân thân bạn đạo (M2): xuất mã gồm deck, vai, hồ sơ gõ; bạn nhập mã để mang phân thân vào ghế bot; kẹp ≤ 1,1 lần ngân sách; không tạo sự kiện học, không loot. 4. Lưỡng Nghi, Tam Tài phòng bạn bè, tối đa 3 người thật (M3). 5. Ghép nhanh khi giờ cao điểm có ≥ 20 người online; chờ tối đa 25 s rồi vào với bot. 6. Thất Tinh 7 ghế: sự kiện tuần, 1–3 người thật.

## 20. Hiệu năng, bậc hình, bench HN0

### 20.1 Luật

- Bậc hình chỉ đổi **cách vẽ**, không đổi luật (D12). Đo khoảng giữa hai khung (rAF → rAF) khi Chrome **bỏ khóa vsync** (`--disable-gpu-vsync --disable-frame-rate-limit`, thêm `--enable-precise-memory-info` để số bộ nhớ JS tin được); 60 Hz ứng với 16,7 ms. Ngân sách đặt thấp hơn để chừa chỗ cho hình thật ở M0b.
- **Bậc mặc định** (PB-24): lần đầu, High nếu chuỗi `renderer` là GPU rời, Medium nếu Apple, Low nếu khác. Sau 10 s đầu trận, p95 > ngân sách của bậc thì **gợi ý** hạ một bậc; không tự đổi giữa trận.
- Số GPU timer chỉ ghi khi tin được (trên ANGLE/Metal nó đọc dài hơn cả khung; nguồn: Rồng `bench.ts`).
- Chuỗi `renderer` của WebGL phải chứa tên GPU thật (Dell: "NVIDIA … RTX 3050 Ti"; M4: "Apple"). Lượt chạy bằng SwiftShader hay vẽ phần mềm **không hợp lệ**.

### 20.2 Ngân sách theo bậc

| Mục | Low | Medium | High |
|---|---|---|---|
| Độ phân giải đo (DPR 1) | 1280 × 720 | 1600 × 900 | 1920 × 1080 |
| Thú sống (luật sim, mọi bậc) | 60 ở M0a (120 đề xuất cho M1); bench đo N = 60, 120, 300 | như Low | như Low |
| `SkinnedMesh` (người, bot, thú tướng, Vương) | ≤ 6 | ≤ 6 | ≤ 8 (Thất Tinh: 10) |
| Kiếm hình của "vạn kiếm" | 150 | 300 | 500 |
| Tam giác mỗi thú đám đông (LOD) | ≤ 1.000 | ≤ 1.800 | ≤ 3.000 |
| Hạt sống / số sát thương sống | 600 / 50 | 1.500 / 100 | 3.000 / 160 |
| Draw call (**gồm lượt hậu kỳ**; bloom ~10–13 lượt ở High) | ≤ 80 | ≤ 110 | ≤ 150 |
| Bộ nhớ texture ước (VAT + atlas + ảnh) | ≤ 64 MB | ≤ 128 MB | ≤ 192 MB |
| **Khung, Dell** (Windows Chrome, RTX 3050 Ti) | p95 ≤ 8 ms (dư ×2 cho máy chỉ có GPU tích hợp, nơi đích là 16 ms) | TB ≤ 8, p95 ≤ 10 ms | **TB ≤ 8, p95 ≤ 12 ms** |
| **Ngân sách con, khung p95 Dell** (D36; nền + đám đông + kiếm, VFX, số + có xương) | 1,5 + 3 + 2 + 1,5 = 8 ms | 2 + 4 + 2,5 + 1,5 = 10 ms | 2 + 5 + 3,5 + 1,5 = 12 ms |
| **Khung, Apple M4** | p95 ≤ 16 ms | p95 ≤ 12 ms | TB ≤ 8, p95 ≤ 12 ms |
| CPU luồng chính p95 | ≤ 6 ms | ≤ 6 ms | ≤ 6 ms |

- Ngân sách con trên M4 nhân theo tỉ lệ tổng của bậc (Low 16 / 8 = × 2; Medium 12 / 10 = × 1,2; High × 1). Ngân sách con chỉ dùng để **quy lỗi** khi tổng trượt (mục 20.3), không phải cổng riêng.
- **Phím tới đòn ≤ 50 ms** = từ `keydown` của chữ cuối tới khung đầu tiên có nét thư pháp rời Bàn Quyết (mục 21.1; 0,15 s bay là hoạt ảnh, không tính). Đo bằng kịch bản `ic-hitstop-keys.mjs` (Source: `games/dragon-hold/scripts/visual/scenarios/dh-hitstop-keys.mjs`). Bàn Quyết cập nhật ≤ 0,3 ms mỗi khung. Không cấp phát mỗi khung trong đường nóng (đám đông, kiếm, hạt, số).
- Hệ số VFX đồng đội (M1+): Low 0,4 · Medium 0,6 · High 0,6; đồng đội −6 dB, đuôi ngắn. **Bể kiếm chung:** số kiếm hình của bậc (150 / 300 / 500) là một bể cho cả trận; "vạn kiếm" của đồng đội lấy từ bể theo hệ số 0,4–0,6, không cộng thêm (PB-34).
- **Bảng bậc trong mã** (PB-35): `TT_TIERS` khai đủ 4 khóa `low | medium | high | ultra` (ultra = high ở MVP) theo kiểu `StageTier` của kit (`dpr, particles, bloom, tipsPerSide, trail`); số kiếm, tam giác LOD, trần draw call, ngân sách con để ở bảng riêng `TT_BUDGETS` trong `rules.ts` (vì `StageTier` không có chỗ).

### 20.3 HN0: bench 3D (việc đầu tiên của M0a)

- **Cảnh:** sân 40 × 26 m, camera 3/4 cố định của game, renderer chung với hậu kỳ của bậc, nền phẳng tô màu.
- **Ca đo** (mỗi ca × 3 bậc × 3 lượt; số báo cáo là trung vị của 3 lượt; khởi động 2 s, đo 10 s). **N** là số thú: ca B, C, D, E chạy ở **N = 60, 120, 300** (PB-19):

| Ca | Nội dung |
|---|---|
| 0 `base` | Sân, camera, hậu kỳ, đất, decal; không thú, không kiếm. Mốc để quy chi phí (PB-03) |
| A `crowd-proc` | 300 thú instanced, dáng đi bằng shader (cách Rồng và Tuyến Cuối đang làm), làm mốc so |
| B `crowd-vat` | N thú instanced chạy **VAT**, 5 loài × N/5, mỗi con một clip và thời điểm clip riêng, trúng đòn liên tục (lóe, giật, nén), chết tan rồi sinh lại |
| C `vankiem` | B + cảnh "vạn kiếm" lặp mỗi 4 s: **kiếm 3D instanced theo bậc** (150 / 300 / 500) có vệt và quầng sáng, 3 loạt hội về vùng đích, ~60 lần trúng mỗi giây có tia và số sát thương (gộp số nhỏ mỗi mục tiêu mỗi 0,25 s) |
| D `impostor` | Như C nhưng thú vẽ bằng impostor nướng từ cùng nguồn (**16 hướng × 8 pha**, trộn mờ hai pha kề) |
| E `skinned` | C + `SkinnedMesh` **bằng trần của bậc** (Low, Medium 6; High 8) chạy clip thật qua `src/view/walker-rig.ts` (người, 2 bot, thú tướng, Vương, dự phòng); thêm một lượt High với 10 (Thất Tinh). Khối tạm có xương ghi số tam giác (người 15.000, Vương 45.000) và số xương (PB-21, PB-34) |

- **Quy chi phí từng phần** (D36, PB-03), ở mỗi N: nền = p95(0); đám đông = p95(B) − p95(0); kiếm, VFX, số = p95(C) − p95(B); có xương = p95(E) − p95(C). Ghi cả hiệu của CPU luồng chính p95 và của draw call. Hiệu của p95 là ước (không cộng chính xác), đủ để biết phần nào nặng.
- **Đo:** khung TB, p95, tối đa; CPU luồng chính TB, p95; draw call; tam giác; số instance theo kiểu vẽ; bộ nhớ texture ước; chuỗi `renderer`; DPR; giảm chuyển động (trang đặt `?motion=full` và ghi lại giá trị media query, vì Windows của máy Dell đang báo `prefers-reduced-motion: reduce`).
- **Nguồn hình:** M0a chưa có GLB của game. Bench đo bằng **khối tạm chia lưới tới đúng số tam giác của bậc**, VAT **nướng ngay trong trang** từ biến dạng thủ tục (đủ để đo giá mỗi đỉnh), impostor nướng ngay trong trang bằng render-to-texture. Nếu trên máy có sẵn một GLB có xương của anh (ví dụ Draconis v3 medium trong media của Rồng), chạy thêm một lượt xác nhận: nướng VAT bằng Blender (`bake_vat.py`), không commit. Phán quyết lấy kết quả **xấu hơn** của hai lượt.
- **Vì sao VAT cho đám đông** (đã chọn theo đề xuất, 25/10): `games/dragon-hold/src/view/crowd.ts` đã có một lớp instanced cho mỗi loài, mỗi instance mang sẵn clip và thời điểm clip, và để trống hai khe `vat`, `bones`; Tuyến Cuối dùng cùng kiểu instanced với chuyển động thủ tục; kit `three` chỉ có `Hero` (`SkinnedMesh` + `AnimationMixer`) cho từng nhân vật. Chọn **VAT** vì: **lợi chính là CPU**: không phải tính và tải lên ma trận xương cho mỗi instance mỗi khung (300 thú × ~25 xương × 64 byte ≈ 480 KB mỗi khung); ở GPU hai cách cùng cỡ (VAT đọc 2 khung × 2 kết cấu = 4 lần mỗi đỉnh, 8 khi trộn hai clip; da có trọng số đọc ~4 ma trận mỗi đỉnh) (PB-34 sửa lý lẽ cũ "1–2 lần đọc"); VAT giữ đúng biến dạng đã làm trong Blender, không phụ thuộc trọng số da lộn xộn của rig Tripo; bộ nhớ vừa (~4 MB mỗi loài ở High: ~1.800 đỉnh × 135 khung × 2 kết cấu RGBA16F; ~0,7 MB ở Low); nội suy giữa hai khung và trộn hai clip ngắn cho chuyển động mượt (anh không nhận chuyển động cứng). Khe `bones` giữ kiểu trong mã nhưng **không làm ở M0a**, trừ khi VAT vượt bộ nhớ của bậc. Người, bot, thú tướng, Vương dùng `SkinnedMesh` thật qua `walker-rig` cục bộ (mục 21.2, D44).
- **Bố cục VAT** (PB-34): texel = `khung × số đỉnh + đỉnh`, quấn dòng trong kết cấu rộng 1.024 hoặc 2.048. Không dùng "cột = đỉnh": mesh 3.000 tam giác có thể > 2.048 đỉnh sau khi tách đường may UV, vượt `MAX_TEXTURE_SIZE` tối thiểu của WebGL2 (2.048).
- **Impostor** (PB-34): **16 hướng × 8 pha** một chu kỳ đi, trộn mờ hai pha kề (4 pha là chuyển động giật, trái luật của anh). Bộ nhớ ở Low: 16 × 8 × 128² × 4 B = 8,4 MB mỗi loài, 5 loài 42 MB (< 64 MB của Low). Đổi một thú giữa VAT và impostor (L4) có trễ: chỉ đổi sau 1 s ở phía bên kia ngưỡng, trộn 0,2 s.
- **Phán quyết mỗi bậc** (D36, PB-19): đo theo **N của luật** (60 ở M0a; 120 để quyết trần M1); kết quả ở 300 chỉ ghi là dư địa (Thất Tinh, Triều Vô Tận). Bậc **đạt** khi ca E ở N đó qua mọi ngưỡng tổng của mục 20.2 (khung TB, p95, CPU, draw call, bộ nhớ). Đạt thì **3D đầy đủ, không lùi gì**, kể cả khi một phần vượt ngân sách con (chỉ ghi lại): đúng câu của anh "nếu đo được vẫn ổn khi là 3D thì cứ triển khai".
- **Luật lùi khi trượt** (chỉ khi ca E ở N của luật trượt; áp từng bậc; đo lại sau mỗi nấc; dừng ở nấc đầu tiên đạt):
  1. Phần nào **vượt ngân sách con** (mục 20.2) thì đi **thang của chính nó** trước: đám đông L3 → L4 → L5; kiếm, VFX, số L1 → L2; có xương: LOD (nửa tam giác cho người, bot, Vương) rồi bớt `SkinnedMesh` dự phòng; nền: hậu kỳ của bậc thấp hơn. Nhiều phần cùng vượt thì phần vượt nhiều ms nhất đi trước.
  2. Không phần nào vượt mà tổng vẫn trượt: **đám đông trước** (L3 → L5, đúng dự đoán của D03), rồi L1, **cuối cùng mới L2**.

| Nấc | Phần | Đổi gì |
|---|---|---|
| L1 | Kiếm, VFX | VFX trang trí: vệt kiếm ngắn một nửa, quầng sáng chỉ ở 1/2 số kiếm, hạt trúng × 0,5 |
| L2 | Kiếm | Số kiếm hình của bậc hạ một nấc (500 → 300 → 150 → 80); lõi chiêu luôn ≥ 80 kiếm 3D |
| L3 | Đám đông | **Bầy** (cụm Thạch Thử) vẽ bằng impostor; thú khác giữ VAT |
| L4 | Đám đông | Thú thường ngoài 100 con gần tâm màn (Low) / 160 con (Medium) vẽ bằng impostor |
| L5 | Đám đông | Mọi thú thường vẽ bằng impostor; tinh anh giữ VAT |
| Ngoài thang | — | Người chơi, bot, thú tướng, Thú Vương, chiêu lớn **luôn 3D**. Low vẫn trượt sau L5 thì hạ trần thú sống của luật rồi chạy lại bot (nguồn: Rồng DESIGN §9 M0) |

- Impostor của hình thật nướng bằng `bake_impostor.py` (nguồn: `games/space-typing/scripts/models/blender/bake_impostor.py`) từ **cùng GLB** với VAT, nên đổi kiểu vẽ không mất asset.

### 20.4 Phán quyết HN0 (làn bench ghi vào đây)

| Bậc | Máy | N đạt 3D đầy đủ (60 / 120 / 300) | Ca E ở N luật: TB / p95 (ms) | Phần vượt (nền · đám đông · kiếm, VFX · có xương, ms) | Nấc lùi dùng | Draw call | Ngày | Changelog |
|---|---|---|---|---|---|---|---|---|
| High | Dell | chưa đo | — | — | — | — | — | — |
| Medium | Dell | chưa đo | — | — | — | — | — | — |
| Low | Dell | chưa đo | — | — | — | — | — | — |
| High | Apple M4 | chưa đo | — | — | — | — | — | — |
| Medium | Apple M4 | chưa đo | — | — | — | — | — | — |
| Low | Apple M4 | chưa đo | — | — | — | — | — | — |

- Kết luận ghi một dòng: "3D đầy đủ ở mọi bậc tới N = …" hoặc "3D, trừ <phần> từ <nấc> ở <bậc>, vì <phần> vượt <x> ms". Phán quyết của M0a là **tạm** cho tới khi HN1 đo lại với 3 model mẫu của anh ở M0b.

## 21. Mỹ thuật

### 21.1 Hướng và cách làm (D03)

- **Một renderer:** `Stage3D` của kit `three` (như Tuyến Cuối) với bảng bậc riêng `TT_TIERS` (mục 20.2); tông màu `NeutralToneMapping`, đặt `stage.renderer.toneMapping` **sau khi dựng** (kit cố định `ACESFilmicToneMapping`; `OutputPass` đọc giá trị của renderer; PB-35). Camera 3/4 cố định thấy cả ải: nghiêng 50–55°, FOV 25–30° (gần trực giao). Không xoay, không zoom ở MVP.
- **Vẻ thủy mặc bằng shading và hậu kỳ:** ramp sáng 2–3 bậc; viền mực bằng vỏ lật 1,5–2 px cho người, tinh anh, tướng, Vương; hạt giấy phủ màn rẻ; sương theo khoảng cách; decal mực trên đất; chết tan khói mực. Lọc Kuwahara chỉ ở Ultra (sau MVP) và chỉ khi ≤ 1,5 ms.
- **Lớp:** phông xa 3 lớp tranh 2D → đất nướng từ ô tranh → decal mực → bóng tiếp đất → sinh vật 3D (VAT, `SkinnedMesh`, hoặc impostor theo HN0) → VFX → tiền cảnh thưa (giảm alpha khi che) → DOM (Bàn Quyết, HUD, khung học).
- **Cỡ ở 1080p** (đo bằng kịch bản kiểu `dh-scale`; được phóng cỡ vẽ, chỉ ở view): người chơi ≥ 64 px cao · bầy ≥ 20 px, một cụm đọc thành khối ≥ 60 px · thú Nhỏ ≥ 36 px · thú Vừa ≥ 48 px · tinh anh × 1,25 · thú tướng ≥ 80 px · Thú Vương ≥ 160 px.
- **Màu ngữ nghĩa của kit không dùng sai:** đỏ `#FF4A4A` chỉ cho nguy hiểm từ địch; cam `#FFB020` khẩn; vàng kim `#FFC83A` tiền và đồ rơi; xanh ngọc `#7FF5E0` sức gõ. Báo đòn địch là vạch đỏ đầy dần trên đất, có sọc và biểu tượng.
- **Chữ thành chiêu:** chốt từ thì chữ trên Bàn Quyết bật thành nét thư pháp xanh ngọc bay vào tay nhân vật trong 0,15 s, rồi chiêu phát; không che vùng chữ.
- Mỗi chiêu đi đủ 7 bước của Codex §26.6 (chuẩn bị, hình chính, đường đi, va chạm, phản ứng, dư âm, âm và số), qua bậc phản hồi T0–T5. **M0a:** hồ sơ phản hồi để **cục bộ** ở `src/view/feedback-profile.ts` (khung `FeedbackProfile` của kit với `id: "dragon"` rồi đè số), ghi vào `SYNC_DEBT.md`; chỉ dùng phần số, nhịp, dừng hình của `kit/feedback`, **không** dùng `AudioCues` (D44, PB-20). Đưa hồ sơ `tutien` lên kit ở M0b khi số ổn, như một việc riêng của repo cha.

### 21.2 Quy trình model (D27)

- Claude viết prompt 2D và 3D; anh tạo ảnh và model trong Tripo/Meshy; Claude dọn, rig, làm clip trong Blender (bản Linux trong WSL), kiểm theo **hợp đồng model cục bộ** `src/content/model-contracts.ts`, nướng VAT và impostor, ghi manifest. Media đẩy bằng `pnpm media:push` (anh chạy), không vào Git.
- **Hợp đồng model cục bộ** (D44, PB-21): `MODEL_CONTRACTS` của kit hợp game bay (`heroes` đòi `Hero_Fly`, `bosses` đòi `Boss_Idle_Hover` và ổ `FX_HALO`), không hợp tu sĩ đi bộ và sói. Game khai: `cultivators` (clip bắt buộc Idle, Run, Cast_Short, Hit; 8.000–30.000 tam giác), `beasts` (Idle, Move, Attack, Death; 800–3.000 tam giác theo LOD, nguồn của VAT), `beast-kings` (12.000–45.000 tam giác, 8–10 clip); `props` dùng của kit. Nhân vật có xương chạy bằng `src/view/walker-rig.ts` (Source: `kit/three/hero.ts`, chỉ lấy trộn clip và ổ cắm; locomotion `idle | run | dash`, không độ chúi bay). Đưa lên kit khi game thứ hai cần.
- **3 model mẫu duyệt trước lô lớn** (Kiếm tu, Phong Lang, Thú Vương): anh duyệt dáng và chuyển động (không chuyển động cứng) rồi mới làm phần còn lại.
- Bot dùng model của trường phái còn lại, đổi màu áo. Tinh anh, thú tướng, biến chủng hệ: cùng GLB, đổi cỡ, chất liệu, hào quang.

### 21.3 Danh sách asset M0b (ước)

| Nhóm | Số | Clip, ghi chú |
|---|---|---|
| Nhân vật (rig biped) | 2: Kiếm tu, Thổ thể tu | Idle, Run, Cast_Short, Cast_Heavy, Dash, Hit, Down, Victory |
| Thú thường | 5: Thạch Thử, Phong Lang, Hỏa Nha, Nham Viên, Thiết Giáp Trư | Idle, Move, Attack, Death → VAT; LOD theo bậc |
| Thú Vương | 1: Thiết Bối Lang Vương | 8–10 clip, `SkinnedMesh`, ≤ 45.000 tam giác |
| Prop lớn (không rig) | 5: cổng ải, Trận Tâm, Trận Trụ, đá vôi, tùng cổ | |
| Prop VFX | 1: phi kiếm (300–800 tam giác) | Dùng cho đánh nền, ô 1, "vạn kiếm" |
| **Cộng GLB** | **14** | Tripo ~75 credit mỗi sinh vật |
| Ảnh | ~100 | 28 ảnh nguồn cho GLB (2 góc) · 6 ô đất · 8 decal · 3 phông · 6 cỏ bụi · ~16 kết cấu VFX · ~24 biểu tượng · ~8 khung UI · ~5 Tĩnh Tu |
| Ảnh bản sắc | 2 | Anh duyệt trước khi làm hàng loạt; chốt tên game cùng lúc |

- Giờ của anh ước: ~13–20 giờ Tripo, ~2–3 giờ Bảng Nghe, ~2 giờ chơi thử mỗi mốc. Xếp sau Rồng qua B9 (D02).
- **Không giống QCBH:** không cầu chữ Hán, không cuộn giấy nhân vật, không nổ máu, không bố cục HUD, không tên riêng của QCBH; quy trình bản sắc 6 câu của Codex §20.

## 22. Âm thanh

- **Luật Q6** (`tools/audio-lab/DECISIONS.md`): mọi âm hành động có **chuẩn bị, phát, thân, đuôi vang** của hẻm núi; **cỡ âm theo cỡ hành động** (bầy nhỏ thì nhỏ; Vương, tuyệt kỹ, Lôi Kiếp to xác, có trọng lượng); **cấm** "puff", "pop", "balloon", "thump"/"thud" đứng một mình, "soft round whoomph", âm đồ chơi, hoạt hình, retro, 8-bit, một tiếng trầm ngắn không thân không đuôi. Lớp sub chỉ làm lớp dưới.
- **Luật giọng đọc** (`AUDIO_PIPELINE.md` §6.2): năng lượng 1–4 kHz tắt nhanh; đuôi vang dưới 1 kHz hoặc trên 4 kHz; âm sau mỗi từ (~1,5 s một lần) giữ đuôi thấp để lặp 20 lần không mệt.
- **Nguồn:** thu âm CC0 (Freesound, đọc giấy phép từng trang, ghi vào tệp giấy phép của game) hoặc Audio Lab (Stable Audio 3, công thức ghép lớp) theo Q1; **mọi âm qua Bảng Nghe mù của anh** trước khi dùng. Không âm tổng hợp thuần.
- **M0a: móc âm im lặng.** `src/audio/` có danh mục id (mục đích, hình 4 phần, cỡ, độ dài, bus, ưu tiên), đánh dấu `silent: true`, bộ trộn bus không phát gì. **Không viết âm tổng hợp mới.** Test ranh giới **cấm import** `kit/feedback/audio-cues` và `kit/audio/dragon-voice` (cả hai tạo âm bằng `OscillatorNode`/`createOscillator`) từ mọi tệp của game, và cấm `OscillatorNode`, `createOscillator` trong mọi tệp của game ngoài bản chép kit `src/kit/**` (D44, PB-20).
- **Danh sách âm** viết ở M0b (`docs/audio/SOUND_LIST.md` của repo game), mỗi id một thẻ như trên; ~55 id (phím 4; Kiếm 8; Thổ thể 8; thú theo lớp 14; Vương 6; triều 2; trận pháp 4; UI 4; Tĩnh Tu 5) và 3 bản nhạc (giữ ải 4 lớp cùng BPM; Thú Vương mỗi pha một stem; nền Tĩnh Tu không nhịp ép).
- **Bus:** music · ambience · world · enemies · self · allies · formation · typing · pronunciation · ui · warnings → limiter (nguồn: `games/dragon-hold/src/audio/{mixer,limiter}.ts`). **Ưu tiên:** phát âm từ của mình → báo đòn, Trận Lực < 30 % → phím → chiêu của mình → chiêu đồng đội, va chạm → bầy, môi trường. Tối đa 32 tiếng (Low 16); một tiếng ≤ 4 lần mỗi 100 ms.
- **Bầy** là một lớp nền "triều" theo mật độ, 3 tầng xa/gần/sát; tiếng chết gộp thành chuỗi "tan khói" (`AUDIO_PIPELINE.md` §8.5), không mỗi con một tiếng.
- **Nhạc:** đàn tranh, sáo trúc, trống, cello. **Không chuông chùa, không tụng.** Không dùng nhạc cụ Trung, Nhật dán nhãn Việt.

## 23. Lưu, replay, hợp đồng dữ liệu

### 23.1 Lưu

- v1 **lưu cục bộ** (kit `safe-storage`, chỉ qua `src/app/storage.ts`), có số phiên bản (`v: 1`) và hàm chuyển đổi; test chuyển đổi với tệp mẫu. Hỏng thì về khe dự phòng (nguồn: Rồng 06 §1).
- Lưu sau mỗi trận. Đại Triều có **mốc lưu sau đợt 4** (ảnh chụp đầu lần nghỉ).
- Kết quả học sống ở lõi học chung (portal) hoặc hàng đợi cục bộ; **không bao giờ mất** khi thua, rút lui, hay hỏng bản lưu game.
- Nối tài khoản khi portal có tài khoản chung (sau MVP).
- **Khóa lưu** (tiền tố `immortality-cultivation.`; PB-25). Mỗi khóa một hàm chuyển đổi và một tệp mẫu trong `tests/app/save-migrate.test.ts`:

| Khóa | Cấu trúc v1 | Mốc |
|---|---|---|
| `.save` | `{ v, realm, tuVi, congPhap[{ id, tier, points, ngoChieu }], daoQua, phapBao{ id, level }, mechLevels, thuLau, vanKhi, thuHach, stars{ [matchId]: 0–3 }, wavesPaid{ [matchId]: number[] } }` | M1 (M0a không lưu tiến trình, mục 25) |
| `.skill` | Hồ sơ gõ của kit (`serializeSkill`) | M0a |
| `.newwords` | `{ v: 1, entries: { wordId, firstSeenMs, channel }[] }` (mục 6.4); bỏ mục cũ hơn 20 phút khi ghi | M0a |
| `.settings` | `{ v, motion: "system" \| "full" \| "reduce", textScale: 100 \| 125 \| 150, keymap, pacing: boolean, quality: "low" \| "medium" \| "high" \| null }` | M0a |

- Không còn khóa `.pace`: nhịp là trường `pacing` của `.settings`.

### 23.2 Replay và nhật ký (PB-25)

- **Đầu replay:** `{ v: 1, gameId, rulesHash, seed, stageId, preset, pacing: boolean, seats: [{ seat, profile: { e, a, cv }, kPm }], deck: [{ wordId, text, group, mastery, recalls, assumed }], newWordAllowance, loadout: { guard: "ward" | "dash", tamPhap } }`. Mọi thứ đến từ ngoài sim (lõi học bất đồng bộ, hồ sơ, sổ cái) nằm ở đây, nên replay chạy lại được trên máy khác (B9) và golden không phụ thuộc máy.
- **Thân:** lệnh theo tick (`SimCommand`, kể cả `pace-update`, `ward-use`) và đầu vào của `local` (`move-to`, `arrows`).
- **Đuôi:** `hashWorld` và `hashLocal` mỗi 600 tick và cuối trận. `ic-replay` và golden so cả hai.
- Nhật ký buổi chơi thử của anh (B9) là replay này kèm `ms` đồng hồ tường của từng phím (chỉ cho học và đo, không vào băm).

### 23.3 Hợp đồng dữ liệu (bước 0 viết `src/content/types.ts` theo đây; PB-24)

| Mục | Luật |
|---|---|
| Đơn vị, làm tròn sát thương | Mục 7.1, 7.2 (máu nguyên, thứ tự cố định, nửa lên mỗi bước) |
| ĐĐ, trả Linh Sa hạ thú | Mục 14.2 |
| Trần 4 W của Lạc Kiếm Trận | Mỗi lần tung, cộng mọi thú (mục 12.1) |
| Tick chạm | Mục 12.1 (ô 1 +6/+36/+66; ô 2 +12; ô 4 +12 rồi mỗi 30 tick; ô 5 +30/+75/+120; đánh nền +18) |
| "Gần Trận Tâm nhất" | Thú đất theo khoảng cách trường hướng; thú bay theo khoảng cách thẳng; hòa thì `beastId` nhỏ hơn |
| "Cụm đông nhất trong r" | Ứng viên là vị trí các thú sống trong tầm; điểm = tổng W trong bán kính của chiêu; hòa thì gần Trận Tâm hơn, rồi `beastId` nhỏ hơn |
| Chồng chậm, khống chế cứng | Mục 7.2 |
| `WaveDef` | `{ id, durationMs, gates, peaks: { atMs, lenMs }[], groups: { atMs, gate, species, count, cluster?, elite?, general? }[], summonMaxW }`; `atMs` nhân 1 / k; luật cổng 1,5 s / 0,6 s kẹp **sau** khi nhân |
| `TelegraphDef` | `{ id, shape: "circle" \| "cone" \| "line" \| "cell", sizeMm, typedAnswer: boolean, answers: ("seal" \| "move" \| "ward" \| "pillar" \| "mech")[], chargeMs: number \| "T", strike }`; CB5 và `telegraph-floor` chạy trên mọi bản |
| `Ward` | `{ id, seat, originU, radiusU, untilTick, charges }` (mục 9.1) |
| Hết đợt, thắng | Mục 4.1 |
| Gọi Đàn ở P2 | Không gọi (mục 10.5) |
| Gục | Mục 4.1 |
| Bậc hình mặc định | Mục 20.1 |
| E của Tĩnh Tu | E_eff của hồ sơ (mục 16) |
| Trần chữ sống, lùi khi không có từ | Mục 6.2 |
| Trạng thái `World` | Bước 0 khai sẵn **mọi trường** theo canon (thú, chữ, Cast, `ward`, nhãn, cơ quan, ví theo ghế, kho đan phù, Thế, báo đòn, `newWordAllowance`); mỗi làn chỉ viết hàm khởi tạo và băm của phần mình (PB-36) |

## 24. Tiếp cận

- **Giảm chuyển động:** theo `prefers-reduced-motion` và cài đặt riêng trong game (ưu tiên cài đặt). Bật thì: không rung camera, không dừng hình dài, VFX ngắn, không chớp nền.
- **Lôi Kiếp không nhấp nháy:** mỗi tia sét ≤ 3 lần đổi sáng mỗi giây, vùng sáng ≤ 25 % màn, không đổi sáng đột ngột toàn màn (theo ngưỡng WCAG 2.3.1). Giảm chuyển động bật: sét thành vệt sáng tĩnh và viền ô, không chớp.
- **Preset** đặt tên theo BALANCE: Thư giãn, Cân bằng, Thử thách, Học. Hồ sơ trẻ em: Thư giãn, lọc `mature`, không chat, nhắc nghỉ 20 phút.
- Hệ, loại chữ Tĩnh Tu, loại thú: **hình và biểu tượng trước màu** (người mù màu).
- Chữ Bàn Quyết 28–32 px (Be Vietnam Pro 700), dòng IPA dùng font đủ glyph IPA (Noto Sans); cỡ chữ chỉnh được (100 % / 125 % / 150 %).
- Đổi phím cho mọi phím lệnh không phải chữ. Mọi việc có đường bàn phím (mục 5.1).

## 25. Ngoại lệ M0

- **Ải M0a** là một ải hộp xám 6 đợt + Thú Vương (~9,7 phút; Vương 64 W, t 120 s), không phải trận dạy hay Đại Triều; CB9 ở M0a chỉ chấm bot Chuẩn ở Cân bằng (9–10,5 phút), bot Trẻ em ở Thư giãn chỉ in số; đủ 5 ô Kiếm từ đầu (lịch mở ô theo trận dạy làm ở M1); thú **vô hệ** cả ải; không có Thiên Kiếp, Cơ Duyên, Hợp Trận, pháp bảo, Thư Lâu, Sơn Môn, lưu tiến trình (chỉ lưu hồ sơ gõ và sổ cái từ mới).
- Chỉ trường phái Kiếm; 3 cơ quan (Kiếm Thung, Lôi Phù Trụ, Phong Ấn Võng); 3 đan, phù (Hồi Xuân Đan, Kim Thân Phù, Lôi Hỏa Phù); chỉ Tâm nhãn (solo).
- **D_ref** dùng số thử 75 W/phút tới khi làn bot đo xong; sau đó máu đợt tính lại (mục 13.3).
- **Trần thú sống 60** (luật); bench đo N = 60, 120, 300: phán quyết theo 60 (và 120 cho M1), 300 là dư địa (mục 20.3).
- **HN0** đo bằng khối tạm (mục 20.3); phán quyết là tạm tới HN1 ở M0b.
- **B9** (anh chơi thử) chờ sau khi Rồng Giữ Ải qua B9 (D02); M0a vẫn in B1–B8 đầy đủ. **M0a chốt có điều kiện: B9 để mở** và chạy khi được (PB-37).
- Từ mới trong ải M0a chỉ qua Học trước và ô 4 (đợt 1–2), gặp lại ở ô 2, ô 4 (HC8); Tĩnh Tu chạy ở trang riêng (bản thử), dùng chung sổ cái từ mới.
- **Không có lõi học** thì mọi trận M0a là khởi đầu lạnh: bộ từ = ≤ 40 từ nền + từ mới trong `newWordAllowance` (sàn bộ từ 40); từ nền dùng thẳng ở ô 1, ô 3, Tẩy và qua bước lùi ở ô 2, ô 5, Ấn; mọi từ khác là từ mới qua sổ cái (mục 17.1). Bộ thử dự phòng có ghi nhãn rõ trong `src/content/data/`.
- Không có âm (móc im lặng), không có hình thật, không có nhạc.
- Golden: 20 seed của ải M0a, bot Chuẩn ở Cân bằng, cộng 3 ca ở Thư giãn, Thử thách, bộ điều nhịp tắt; băm `hashWorld` và `hashLocal` (mục 23.2).

## 26. Câu hỏi mở (mỗi câu có đề xuất; không trả lời thì làm theo đề xuất)

| # | Câu hỏi | Đề xuất |
|---|---|---|
| 1 | Tên game chính thức? | Giữ "Tu Tiên Thủ Ải" tới M0b; chốt cùng lúc duyệt 2 ảnh bản sắc. `gameId` không đổi |
| 2 | Tên tuyệt kỹ Kiếm: anh lấy ví dụ "Vạn Kiếm Quy Tông" | Giữ tên của dự án "Thiên Hà Kiếm Vũ"; "vạn kiếm" là kiểu trình diễn của nó. Anh muốn đúng tên ví dụ thì đổi trong dữ liệu |
| 3 | Đo bậc Low trên GPU tích hợp? | Anh bật Chrome chạy GPU tích hợp trong Cài đặt đồ họa Windows cho một lượt đo (agent không đổi cài đặt hệ thống); không làm được thì dùng luật dư ×2 trên RTX và số của M4 |
| 4 | Nâng trần thú sống sau HN0? | Lên 120 ở M1 nếu HN0 ở Low đạt với N = 120 (3D đầy đủ hoặc sau thang lùi theo phần vượt, mục 20.3); chạy lại toàn bộ bot |
| 5 | B1, B7 trượt Nhàn I như Rồng? | Không đổi dải chung (D15). Chỉnh trong game: thời gian đi tới Kết Giới, tải đợt giữa, phần không do gõ; ghi số từng lượt |
| 6 | Trần k 1,30 có đủ cho bot Nhanh? | Giữ 1,30 tới khi bot đo. Nếu Nhanh thắng quá dải, đề xuất nâng có số đo, ghi thành quyết định riêng |
| 7 | Hợp Trận Lưỡng Nghi tối đa 80 % (40 % + 2 × 20 %)? | Giữ; nạp nhãn của Lưỡng Nghi nhanh hơn vì chỉ 2 nhãn. Xem lại bằng bot ở M3 |
| 8 | Kiến trúc `local` (vị trí người ngoài sim) ngay từ solo? | Có, từ M0a: đổi sau tốn hơn nhiều (D28) |
| 9 | Các tệp `analysis/01–07` có cần dòng đầu trỏ về canon? | Có (việc còn lại của M0, tệp đánh giá §6); làm ở lượt sửa kế, chỉ thêm một dòng |
| 10 | CB3 ở bot Khá, Nhanh (ô 1 nhận mọi từ dư, PB-05) | Làn bot in phần ô 1 theo từng bot ngay vòng đầu. Vượt 30 % thì trước hết tăng sức ô 2, ô 4 (giữ bất biến hạ thú), sau mới hạ ô 1; không tăng tải để che |
| 11 | Bot "gõ bừa" ở Tĩnh Tu (gõ cả Tâm ma) vẫn có thể lĩnh ngộ trong 2 phiên vì Minh cho nhiều điểm | Theo dõi bằng báo cáo HC4b; nếu điểm phiên của bot gõ bừa ≥ bot Chuẩn thì nâng phạt chọn nhầm −3 → −5 (đổi số, không đổi luật) |
| 12 | `ward` cùng tick bị thế giới và `local` dùng lần cuối (mục 9.1) | Chấp nhận lệch tối đa một lần đỡ; nếu replay đội ở M3 cho thấy lệch thường xuyên thì chuyển phần đỡ cho mình sang đếm riêng của `local` (3 lần chung chia theo thứ tự tick) |
| 13 | Trận lạnh dùng từ nền qua bước lùi ở ô 2, ô 5, Ấn (mục 17.1) | Giữ ở M0a (không lõi học). Khi có lõi học, báo cáo in số lần từ nền lên ô 2, ô 5, Ấn; > 20 % số từ của các ô đó thì tăng phần "đến hạn" của bộ từ |

## 27. Nguồn

- Tệp đánh giá: [`DANH_GIA_2026-10-24.md`](DANH_GIA_2026-10-24.md) (mục 8, Phụ lục A, B). Đề xuất Codex V2.2: [`source/CODEX_V2_2_2026-10-24.md`](source/CODEX_V2_2_2026-10-24.md). Phân tích: `analysis/01–08`. Phản biện canon: [`analysis/09-phan-bien-canon.md`](analysis/09-phan-bien-canon.md) (đã áp, D32–D46).
- Khung chung: [`../BALANCE.md`](../BALANCE.md), [`../SPLIT_PLAN.md`](../SPLIT_PLAN.md), [`../AUDIO_PIPELINE.md`](../AUDIO_PIPELINE.md), [`../MEDIA_AND_MODELS.md`](../MEDIA_AND_MODELS.md), [`../../../tools/audio-lab/DECISIONS.md`](../../../tools/audio-lab/DECISIONS.md) (Q1, Q6).
- Rồng Giữ Ải (khuôn mẫu, chép có ghi nguồn): [`../dragon-lane/00-canon.md`](../dragon-lane/00-canon.md), [`../dragon-lane/DESIGN.md`](../dragon-lane/DESIGN.md), `dragon-lane/01`, `02`, `03`; mã `games/dragon-hold` (`AGENTS.md`, `LANES.md`, `src/sim`, `src/view/{crowd,bench}.ts`, `scripts/balance`, `scripts/visual`, `docs/changelog/2026-10-2*-m0a-*.md`).
- Kit: `shared/game-kit` (`typing`, `learning`, `vocab`, `balance`, `feedback`, `three`, `ui`, `input`, `audio`, `platform`, `tools`), README và `DRIFT.md`.
- Mã khác: `games/typing-defense/src/sim/nav` (tìm đường), `games/typing-survival/src/sim/weapons.ts` (nạp băng), `games/typing-survival/src/view/crowd.ts`, `games/space-typing/scripts/models/blender/bake_impostor.py`, `games/dragon-hold/src/typing/deck.ts` (chép có sửa, mục 17.1), `games/dragon-hold/src/sim/waves.ts` (luật hết đợt), `games/dragon-hold/scripts/visual/scenarios/dh-hitstop-keys.mjs`.
- Quyết định của anh: tin nhắn 24/10 (làm), 25/10 (hai tin về hướng hình), luật "làm theo đề xuất" (17/10), luật Cloudflare Free.
