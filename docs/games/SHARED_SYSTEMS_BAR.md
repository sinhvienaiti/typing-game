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
