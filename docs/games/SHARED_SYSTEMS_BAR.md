# Hệ dùng chung: mức nhận từ 9 điểm

Chủ dự án, 29/10/2026: "với tiếng phím Audio Lab và hiệu ứng gõ chữ, animation của nhân vật, tôi muốn đạt phải trên 9 điểm chứ không phải chỉ 7, 8 là được. Những phần này sẽ phục vụ cho nhiều game, sẽ được tái sử dụng cho nhiều nơi, nên bạn phải xây dựng nó tốt nhất."

## 1. Áp cho

| Hệ | Ở đâu | Mốc so sánh |
|---|---|---|
| Hiệu ứng gõ chữ: dải chữ giữa màn, sáu kiểu chữ, gõ sai, xong từ, combo | `shared/game-kit/feedback/typing-fx/`, Lab `tools/typing-feedback-lab/` | Typing Break (`docs/games/TYPING_BREAK_STUDY.md` và tờ khung), game hành động thương mại |
| Tiếng phím: năm hồ sơ bàn phím (Creamy, Thock, Clicky, Soft Dome, Classic Spring) | Audio Lab (`tools/audio-lab/`, `~/AudioLab/`) | bản thu bàn phím cao cấp thật (tai chủ dự án là cổng cuối) |
| Animation nhân vật: rồng, Lightbearer, người làng, lính, quái, chuyển động đám đông | kit `shared/game-kit/three/` và mã view của từng game | game thương mại cùng thể loại; nguyên tắc hoạt hình (chuẩn bị, theo đà, chồng lớp, nặng nhẹ) |

Mọi game sau này dùng lại các hệ này, nên chúng là nền chất lượng chung.

## 2. Mức nhận

- **Đạt khi cả hai giám khảo độc lập chấm từ 9 trở lên**, và không hạng mục con nào dưới 8,5.
- Mức 7–8 của các luật khác (VFX_STANDARD §5.6 là 8, ảnh 2D là 8) **không đủ** cho ba hệ này.
- Chủ dự án là cổng cuối: nghe hay xem trực tiếp, đồng ý thì mới gắn rộng ra các game.
- **Riêng âm thanh:** agent không nghe được bằng tai. Hai "giám khảo" của tiếng phím là (1) bộ phê bình nhiều lớp của Audio Lab (L1–L6, `docs/games/AUDIO_PIPELINE.md` §4) phải đạt mọi cổng, và (2) chủ dự án nghe mù trên Bảng Nghe, chấm từ 9. Khi có bản thu bàn phím thật được duyệt, bài nghe mù đặt xen bản thật.
- **Hai chỗ lệch của tiếng phím đã nhận (điều phối 29/10):** thời gian lên của phím ≤ 10 ms (đầu tiếng ≤ 2 ms, tiếng chính tới trong 15 ms) thay cho 3 ms, vì cú gõ thật có tiếng chạm keycap trước tiếng chạm đáy; mức chung −27 LUFS-M max thay cho −20, vì nén lên −20 làm mềm tiếng click.

## 3. Cách chấm

- **Hai giám khảo độc lập**, không phải làn làm. Mỗi người viết điểm trước khi đọc số đo của làn.
- **So cạnh mốc**, không so với bản cũ của ta:
  - hiệu ứng gõ: tờ khung cạnh tờ Typing Break, cùng thời điểm, cùng cỡ;
  - tiếng phím: nghe mù, cân độ to, xen với bản thu bàn phím thật nếu có trong thư viện CC0 trên máy; bài lặp 20 lần cho độ mỏi tai;
  - animation: dải khung và clip nửa tốc độ cạnh tham chiếu thương mại.
- **Thang 0–10:** 9 là "ngang game thương mại tốt nhất cùng loại, người chơi muốn bật"; 8 là "phát hành được nhưng thường"; 7 là "ổn, không ấn tượng".
- Mỗi lần chấm ghi năm sửa cụ thể nhất nếu chưa đạt.

## 4. Hạng mục con

- **Hiệu ứng gõ:** độ trễ (hiện ngay khung đầu), độ đẹp của từng kiểu, đọc được chữ kế tiếp, xong từ, gõ sai, combo, đồng bộ hình và tiếng, độ mỏi mắt sau năm phút, hiệu năng (60 FPS ở 15 phím/giây).
- **Tiếng phím:** độ thật, độ "sang", độ đều giữa các biến thể, không mỏi tai sau 20 lần, độ trễ, độ to đúng mức so với nhạc và tiếng trận.
- **Animation:** chuẩn bị và theo đà, cảm giác khối lượng, chuyển tiếp mượt giữa các clip, phản ứng khi bị đánh, chết, đi và đứng, đám đông không đồng bộ máy móc, nhìn rõ ở camera chơi.

## 5. Dùng thư viện có sẵn trước (chủ dự án, 29/10/2026)

"Với 3 phần này, hãy ưu tiên nếu có thư viện nào hỗ trợ thì nên tái sử dụng để áp dụng nó, miễn sao nó miễn phí và không làm vi phạm bản quyền hay gì khác khi tôi đưa site public là được, vì khả năng nếu để bạn tự làm sẽ khó đạt hay, đẹp, mượt, phù hợp được."

- **Trước khi tự viết**, mỗi làn tìm thư viện mã và kho tài sản đã được dùng rộng rãi, chọn cái giúp đạt 9 nhanh nhất. Tự viết chỉ khi không có thư viện phù hợp, hoặc thư viện làm game chậm hay khó hợp phong cách.
- **Giấy phép được dùng khi đưa site công khai:**
  - mã: MIT, BSD, ISC, Apache-2.0, MPL-2.0 (chỉ dùng nguyên, không sửa file của thư viện);
  - tài sản (âm thanh, animation, texture): CC0; CC-BY được dùng nếu ghi công đầy đủ trong trang Credits của game.
- **Không dùng:** GPL, AGPL, LGPL khi phải sửa hay gộp tĩnh; mọi giấy phép "phi thương mại" (NC), "không phái sinh" (ND); tài sản chỉ ghi "free", "royalty-free" mà không có giấy phép rõ; tài sản của game khác (kể cả Monkeytype, GPL-3.0); dịch vụ cấm dùng trong sản phẩm (đọc điều khoản trước).
- **Kiểm giấy phép tại nguồn** (file LICENSE trong repo, trang giấy phép của gói), không tin mô tả của bên thứ ba. Ghi mọi thư viện và tài sản vào `docs/games/THIRD_PARTY.md`: tên, phiên bản, nguồn, giấy phép, cách dùng, ghi công cần có.
- **Tải tài sản (âm thanh, animation, texture) về máy cần chủ dự án đồng ý từng gói** (tên, nguồn, giấy phép, dung lượng). Cài gói mã qua pnpm là việc làm thường ngày, theo chỉ thị này.
- Thư viện là công cụ, không thay mức nhận: vẫn phải có hai giám khảo từ 9.
- **Mở rộng ngày 01/11/2026, theo lời chủ dự án:** "có thể dùng các loại tài nguyên, thư viện, source có sẵn miễn sao nó miễn phí và được cho phép thương mại ở game của chúng ta, chứ k dùng các loại bị giới hạn". Từ ngày này, áp dụng cho mọi phần của ba game, không chỉ ba hệ dùng chung:
  - **mã:** thêm Zlib, ví dụ pmndrs `postprocessing`. Zlib cho dùng thương mại; chỉ cần giữ thông báo bản quyền trong file nguồn;
  - **tài sản:** thêm các giấy phép riêng miễn phí, cho dùng thương mại, không bắt trả tiền hay ghi công trong game, và chỉ cấm bán lại chính tài sản đó thành gói. Ví dụ Quaternius Asset License v1.0 (QAL). Ghi ngày tải và nguyên văn giấy phép vào `THIRD_PARTY.md`, vì QAL §7 áp dụng bản giấy phép có hiệu lực lúc tải;
  - **model của bên thứ ba** (gói CC0 hoặc QAL) được đưa vào game. Câu "Real models come from the owner as GLB" của `games/dragon-hold/AGENTS.md` không còn chặn chúng;
  - **tải gói miễn phí hợp các điều trên** không cần xin từng gói nữa; vẫn ghi đủ vào `THIRD_PARTY.md`;
  - **vẫn không dùng:** NC, ND, GPL khi sửa hay gộp tĩnh; Mixamo (điều khoản Adobe chưa kiểm được); "Fab Standard" và "Sketchfab Standard" (giấy phép thương mại riêng, có điều kiện); mọi tài sản không có giấy phép rõ.
