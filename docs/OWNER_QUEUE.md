# Việc chờ chủ dự án xác nhận

Chủ dự án, 01/11/2026 khoảng 03:00: "tôi sẽ treo máy đến tầm 9h sáng, vì vậy nếu có gì cần tôi xác nhận thì hãy tạm note lại tầm 9h thì hãy báo, và làm những việc có thể để tránh bị block".

Claude ghi vào đây mọi việc cần chủ dự án quyết hay tự tay làm. Tới 9h, Claude báo cả danh sách một lần. Trong lúc chờ, Claude làm mọi việc khác không bị chặn.

## Đang chờ (báo lúc 9h)

| # | Việc | Vì sao cần chủ dự án | Claude làm gì trong lúc chờ |
|---|---|---|---|
| 1 | Model 3D nhân vật nữ cầm súng và drone hỗ trợ cho Last Line (như ảnh chủ dự án gửi) | Model 3D tạo bằng tay trên trang Tripo (bộ nhớ: không gọi Tripo qua API) | Soạn sẵn prompt Tripo, ảnh tham chiếu các góc, danh sách animation, chỗ gắn nòng súng; dựng sẵn khung code để gắn model khi có |
| 2 | Đăng ký cuối cho hệ thống dùng chung (chữ "sống" trên thẻ súng, hiệu ứng gõ) | Luật 29/10: hai giám khảo ≥ 9, chủ dự án ký sau cùng | Làm và cho hai giám khảo chấm trước; gửi bản chụp để chủ dự án xem lúc 9h |
| 3 | Wordwoven: dựng lại 6 nhà mái tranh trên Tripo (phiếu 129, khoảng 180 credit) hay giữ model hiện có | Tốn credit Tripo của chủ dự án | Đặt nhà hiện có, đợi ý tưởng map được ChatGPT duyệt |
| 4 | Wordwoven: Draconis dùng bản v2 của Dragonhold (đã có khung xương) hay dựng bản riêng trên Tripo | Model mới cần Tripo | Gắn tạm bản v2 để có nhân vật, coi là nợ tới 8,5 |
| 5 | Wordwoven: dời ngày xong map 1 từ 12/11 sang khoảng 15–16/11 | Lịch đã duyệt | Làm tiếp theo kế hoạch ba đợt |
| 6 | **O1–O10** của `docs/games/QUALITY_RESCUE_2026-11-01.md` §3 đợt 3 và §4.2. Đề xuất của Claude ghi ngay trong bảng ở đó. Các việc chính: bỏ kiểu vẽ "đồ chơi" của Dragonhold để theo hướng painterly-realistic (O1); sửa dòng "giữ bloom" trong VFX_STANDARD để đạn Last Line hết nhòe (O4); màu phe địch của Last Line (O5); ô súng bản A hay C (O7); model Tripo nhân vật nữ, drone và 5 súng (210–300 credit) | Đổi hướng mỹ thuật đã duyệt; đụng tài liệu chuẩn; tốn credit Tripo | Làm phần không cần duyệt (đợt 1): D1–D4, L2–L4 vào main. L1 (bloom) để sẵn trên nhánh `ts-wave1-bloom`. Có O1 và O4 thì gộp ngay |

## Đã tự quyết (không cần chờ), ghi để chủ dự án biết

- **Tải gói tài nguyên miễn phí** được phép thương mại, như Quaternius, KayKit, Kenney, Poly Haven, ambientCG.
  - Căn cứ: câu của chủ dự án 01/11, "có thể dùng các loại tài nguyên, thư viện, source có sẵn miễn sao nó miễn phí và được cho phép thương mại".
  - Giấy phép được kiểm trên trang nguồn và ghi vào `docs/games/THIRD_PARTY.md`. Gói có giới hạn (không thương mại, cấm phân phối trong game, phải trả tiền) thì không dùng.
- **Wordwoven sẽ bật 3D làm mặc định cho map 1**, vì bảng 2D vẽ bằng mã trái luật "không có hình vẽ bằng mã thay tranh". Thời điểm bật: xem dòng dưới. Map 3D vẫn là nợ phải làm lại tới 8,5.
- **Wordwoven chưa bật 3D làm mặc định** cho tới khi 3D vẽ được quái, lính, dân và cây. Chẩn đoán 01/11 cho thấy 3D hiện không vẽ con nào; bật lúc này thì game không chơi được.
  - Khi đã bật 3D, máy không có WebGL sẽ hiện màn "Cần WebGL", không lùi về bảng 2D vẽ bằng mã. `?view=2d` chỉ giữ cho bot và test.
- **Trần dòng 1C (16.500)** tạm vượt khi cần, ghi số mỗi lần vượt. Trần này là luật kế hoạch, không phải luật của chủ dự án; chủ dự án muốn giữ thì báo.
- **Camera Wordwoven** chọn kiểu nhìn chéo 40–45°, có dải trời và chân trời. Ý tưởng map gửi ChatGPT duyệt theo kiểu này.
