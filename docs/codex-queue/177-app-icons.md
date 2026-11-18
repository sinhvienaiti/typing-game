# Phiếu 177 · Ba game · Biểu tượng ứng dụng và favicon (3 bộ)

**Vì sao:** tab trình duyệt và lối tắt của ba game cần biểu tượng thật theo hướng mỹ thuật mới (luật 28/10: không hình vẽ bằng mã). Chủ dự án 29/10: Codex còn nhiều hạn mức, giao thêm việc.

**Báo cáo:** `docs/codex-queue/177-report.md`.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5.

## Luật chung

Như phiếu 176 (đọc phiếu đó), với các điểm khác: thư mục `games/<id>/art-src/ui/app-icon/`; tờ `games/typing-defense/art-src/_review/177-icons.jpg`.

## Ảnh

Mỗi game: `app-icon` 1024 × 1024 nền đặc (góc vuông, hệ điều hành tự bo), cộng các bản thu Lanczos `512`, `192`, `180`, `64`, `32`, `16` (bản 32 và 16 được vẽ lại đơn giản hơn nếu bản thu không đọc được: một lượt sinh riêng `app-icon-small` 256 × 256, chỉ còn dáng chính).

| Game | Nội dung |
|---|---|
| Dragonhold | đầu rồng lửa nhìn nghiêng ba phần tư trên khiên hoa cương, viền vàng búa |
| Wordwoven | huy hiệu đã nhận `ui/title-epic/emblem.png` làm gốc, đặt trên nền ngọc sẫm |
| Last Line | mũ có khe sáng lam của Lightbearer trên nền hố đen cam |

## Kiểm (ghi số)

1. Khổ đúng mọi bản; không chữ.
2. Ở 32 và 16 px: ba biểu tượng khác dáng nhau và đọc ra được; đặt thử trên nền tab sáng và tối.
3. KA5: M và Q cho bản 1024 và bản 32.

**Xong khi:** ba bộ đủ bản thu, qua mục 1–2, tự chấm M ≥ 8 và Q ≥ 8.
