# Việc chờ chủ dự án xác nhận

Chủ dự án, 01/11/2026 khoảng 03:00: "tôi sẽ treo máy đến tầm 9h sáng, vì vậy nếu có gì cần tôi xác nhận thì hãy tạm note lại tầm 9h thì hãy báo, và làm những việc có thể để tránh bị block".

Claude ghi vào đây mọi việc cần chủ dự án quyết hay tự tay làm. Tới 9h, Claude báo cả danh sách một lần. Trong lúc chờ, Claude làm mọi việc khác không bị chặn.

## Chủ dự án đã chốt (01/11 khoảng 03:45, trước khi treo máy)

| Mục | Quyết định |
|---|---|
| O1 Kiểu vẽ Dragonhold | Bỏ kiểu "đồ chơi", chuyển sang painterly-realistic. Claude đưa ảnh so cùng camera trước khi bật mặc định |
| O4 Bloom Last Line | Cho sửa VFX_STANDARD (đã sửa); gộp bản hạ bloom |
| O5 Màu phe quái Last Line | Tím |
| O7 Ô súng Last Line | Bản A (30–58 % chiều cao, ngoài hai tường) |
| Nhân vật Last Line | **Chủ dự án dựng 7 model trên Tripo** (nữ xạ thủ, drone, 5 súng); prompt ở `QUALITY_RESCUE_2026-11-01.md` §4.4; Claude kiểm prompt và ảnh nguồn trước |
| O2 Model Dragonhold | Cây và đá thử gói miễn phí trước; **6 mốc lớn dựng trên Tripo** (khoảng 180 credit, chủ dự án dựng) |
| Wordwoven | Draconis dùng lại bản v2 của Dragonhold; nhà giữ bản hiện có, quyết sau khi ChatGPT duyệt concept map |
| Tripo dựng thử (01/11, 9h) | **Chờ ảnh đạt 8,5.** Không dựng thử tượng rồng v2b (8,0 / 8,3). Chỉ tiêu credit khi ảnh nguồn được hai giám khảo cùng cho từ 8,5 |
| Nhân vật Last Line (01/11, khoảng 17:00) | **Đủ 4 góc** cho nữ xạ thủ và drone (Tripo multiview). Vẽ bằng ChatGPT (chế độ Chat), vì Firefly không giữ được một thiết kế qua 4 góc |
| Gemini (01/11, khoảng 17:20) | Chủ dự án đã đăng nhập gemini.google.com. Khi ChatGPT hết hạn mức tạo ảnh, Claude dùng Gemini để tạo ảnh hoặc media khác |
| Còn lại | Duyệt hết theo đề xuất: dời Wordwoven sang 15–16/11; Claude thử camera Dragonhold rồi gửi ảnh; 6 loại flipbook đạn bằng Firefly; cây xa dùng bậc 4.000 tam giác |

## Còn chờ

| # | Việc | Ghi chú |
|---|---|---|
| 1 | ~~Chủ dự án dựng model Tripo~~ **Không cần nữa**: theo lời chủ dự án 01/11 khoảng 03:50, Claude dựng qua API (ví 970 credit), sau khi ảnh nguồn qua hai giám khảo 8,5 và chạy `--dry-run` | Tiến độ ở `docs/games/TRIPO_TODO.md`. 07:50: sáu mốc Dragonhold đã vẽ hai vòng, chưa vòng nào đạt 8,5 (tốt nhất là tượng rồng M 8,0/8,3), nên **chưa tốn credit**. Vòng 3 đang vẽ, lần này cả bộ dùng một chuẩn chất liệu. Nữ xạ thủ, drone và 5 súng đang vẽ vòng 1 (ngà sứ, không vàng) |
| 2 | Ký cuối cho chữ "sống" trên thẻ súng (hệ thống dùng chung) | Sau khi hai giám khảo cùng từ 9 |
| 3 | Đính kèm ba ảnh nền vào ba cuộc chat ChatGPT để nó vẽ concept đè lên ảnh thật. Trình duyệt trong app không gửi được ảnh: trang https chặn ảnh từ máy, và phím dán giả lập không lấy được clipboard. Ảnh ở `games/<game>/art-src/_review/maps/map1-base-1280x720.png`; chat Dragonhold, Wordwoven, Last Line (link trong `docs/games/maps/*-CHATGPT_REVIEW.md`). Kéo thả ảnh vào chat rồi gõ: "Now paint the concept over this base image using your prompt" | Khoảng 1 phút mỗi game. Trong lúc chờ, Claude vẽ thử bằng Firefly với ảnh nền làm tham chiếu (lượt 1 của Dragonhold còn kiểu cũ của ảnh chụp, chưa đạt) **08:10 ChatGPT báo "1% usage remaining"; chủ dự án 9h: đó là hạn mức của Work, chế độ Chat dùng bình thường.** Claude nhờ ChatGPT (Chat, High) vẽ concept từ prompt và tọa độ legend; ảnh nền thật vẫn cần anh đính kèm nếu muốn khớp khung từng pixel |

## Đã tự quyết (không cần chờ), ghi để chủ dự án biết

- **Tải gói tài nguyên miễn phí** được phép thương mại, như Quaternius, KayKit, Kenney, Poly Haven, ambientCG.
  - Căn cứ: câu của chủ dự án 01/11, "có thể dùng các loại tài nguyên, thư viện, source có sẵn miễn sao nó miễn phí và được cho phép thương mại".
  - Giấy phép được kiểm trên trang nguồn và ghi vào `docs/games/THIRD_PARTY.md`. Gói có giới hạn (không thương mại, cấm phân phối trong game, phải trả tiền) thì không dùng.
- **Wordwoven sẽ bật 3D làm mặc định cho map 1**, vì bảng 2D vẽ bằng mã trái luật "không có hình vẽ bằng mã thay tranh". Thời điểm bật: xem dòng dưới. Map 3D vẫn là nợ phải làm lại tới 8,5.
- **Wordwoven chưa bật 3D làm mặc định** cho tới khi 3D vẽ được quái, lính, dân và cây. Chẩn đoán 01/11 cho thấy 3D hiện không vẽ con nào; bật lúc này thì game không chơi được.
  - Khi đã bật 3D, máy không có WebGL sẽ hiện màn "Cần WebGL", không lùi về bảng 2D vẽ bằng mã. `?view=2d` chỉ giữ cho bot và test.
- **Trần dòng 1C (16.500)** tạm vượt khi cần, ghi số mỗi lần vượt. Trần này là luật kế hoạch, không phải luật của chủ dự án; chủ dự án muốn giữ thì báo.
- **Camera Wordwoven** chọn kiểu nhìn chéo 42°, **không có trời**: ở góc này mép trên khung thấp hơn chân trời 21°, nên không vẽ dải trời (sửa lại quyết định ban đầu "có dải trời", vốn sai về hình học). Ý tưởng map gửi ChatGPT duyệt theo kiểu này.
- **Giấy phép, theo lời chủ dự án 01/11** (ghi ở `SHARED_SYSTEMS_BAR.md` §5): được dùng Zlib (thư viện hậu kỳ pmndrs `postprocessing`), Quaternius Asset License (miễn phí, dùng thương mại, chỉ cấm bán lại thành gói) và model bên thứ ba CC0 hoặc QAL. Tải gói miễn phí không cần xin từng gói. Vẫn không dùng NC, ND, GPL, Mixamo, Fab hay Sketchfab Standard. Chủ dự án muốn chặt hơn thì báo lúc 9h.
