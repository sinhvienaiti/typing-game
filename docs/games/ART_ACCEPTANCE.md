# Luật duyệt ảnh 2D và model 3D

Từ 26/10/2026, áp dụng cho mọi game. Chủ dự án:
- chi phí làm 2D và 3D rất đắt, nên ảnh đạt từ 7 điểm trở lên vẫn chấp nhận;
- chỉ tạo lại khi ảnh sai quá, không sửa được;
- ảnh tạm chấp nhận phải ghi lại, để sau có kinh phí thì thay;
- ưu tiên ảnh cần thiết.

**Sửa ngày 27/10/2026 (chủ dự án):** "chỉ tiết kiệm chi phí với ảnh 3D, còn ảnh 2D thì cứ phải đạt trên 8 điểm thì mới cho pass, vì ảnh 2D chi phí sẽ luôn rẻ hơn".
- **Model 3D** (Tripo, Meshy) giữ luật 7 điểm ở trên.
- **Ảnh 2D** (sprite, icon, ô đất, decal, chân dung, phông, và cả ảnh nguồn gửi Tripo) phải **từ 8 điểm** mới đạt. Ảnh 2D dưới 8 thì sửa bằng công cụ, sửa không lên được thì tạo lại.
- "Trên 8" hiểu như "trên 7" của luật 26/10, tức là từ 8 điểm. Chủ dự án muốn chặt hơn (từ 8,5) thì sửa dòng này.

Mục 2 có bảng mức riêng cho hai loại.

Luật này thay mọi câu "chưa đạt thì tạo lại" trong phiếu Codex, bộ prompt và báo cáo kiểm ảnh cũ. Danh sách ảnh tạm chấp nhận: [ART_REPLACE_LATER.md](ART_REPLACE_LATER.md).

## 1. Thang 10 điểm

Năm tiêu chí, mỗi tiêu chí 0–2 điểm. Chấm theo cỡ ảnh hiện trong game, không soi ở 400 %.

| Tiêu chí | 2 điểm | 1 điểm | 0 điểm |
|---|---|---|---|
| **Đúng đề** | Đúng nhân vật, vật, nét nhận diện bắt buộc | Đúng đề, thiếu một nét phụ | Sai đề |
| **Đọc được trong game** | Dáng và màu rõ ở cỡ thật, không lẫn màu tín hiệu | Hơi rối hoặc hơi chìm | Không nhận ra |
| **Hợp bộ** | Cùng phong cách, ánh sáng, bảng màu với ảnh cùng game | Lệch nhẹ | Lệch hẳn |
| **Hình khối** | Giải phẫu, số chi, phối cảnh đúng | Lỗi nhỏ ở chỗ ít thấy | Thừa/thiếu chi, méo ở chỗ người chơi thấy |
| **Dùng được cho bước sau** | Khung, nền, tư thế, mép nối đúng quy cách | Lỗi sửa được bằng công cụ | Không dựng 3D, rig hay ghép được |

Số lượng chi tiết lệch nhẹ so với prompt (7 thân tre thay vì 9, 6 bông lau thay vì 8) không trừ điểm, trừ khi game cần đúng số đó.

## 2. Các mức

### 2.1 Model 3D (tốn tiền: luật 7 điểm)

| Điểm | Mức | Làm gì |
|---|---|---|
| 9–10 | **Đạt** | Dùng. |
| 7–8,5 | **Tạm chấp nhận** | Dùng ngay. Ghi vào `ART_REPLACE_LATER.md`: điểm, thiếu gì, mức cần, cách thay. |
| Dưới 7, sửa được | **Sửa** | Sửa bằng preset hoặc Blender; **không tạo lại**. Chấm lại sau khi sửa. |
| Dưới 7, không sửa được | **Tạo lại** | Chỉ mức cần P1 hoặc P2 (mục 3). Tối đa 1 lần. Lần mới vẫn dưới 7 thì dùng bản tốt hơn nếu từ 5 điểm, ghi vào danh sách thay sau; dưới 5 thì báo chủ dự án. |

### 2.2 Ảnh 2D (rẻ: từ 8 điểm, 27/10)

| Điểm | Mức | Làm gì |
|---|---|---|
| 9–10 | **Đạt** | Dùng. |
| 8–8,5 | **Đạt** | Dùng. Ghi điểm và thiếu gì vào `ART_REPLACE_LATER.md` (dòng ảnh 2D ở đó là việc nâng khi tiện, không chờ kinh phí). Có cách sửa miễn phí (`ART_FIX_QUEUE.md` §5) thì làm khi tiện. |
| Dưới 8, sửa được | **Sửa** | Sửa bằng công cụ trước (rẻ nhất). Chấm lại; vẫn dưới 8 thì tạo lại. |
| Dưới 8, không sửa được | **Tạo lại** | Tạo lại tới khi từ 8 điểm, tối đa 3 lượt một ảnh. Mỗi lượt sửa prompt theo đúng chỗ thiếu. Sau 3 lượt vẫn dưới 8: dùng bản tốt nhất nếu từ 7, báo Claude để đổi cách (prompt khác, ảnh mẫu, ghép); dưới 7 thì báo chủ dự án. |

Mức cần (mục 3) vẫn quyết **làm ảnh nào trước**: P1, rồi P2; P3 chờ. Luật 2D chỉ đổi **ngưỡng đạt**.

**Sửa được:**
- 2D: tách nền, khóa màu (`tools/art-normalize`), cắt khung, đổi khổ, thêm lề; chỉnh màu, độ sáng; xóa vật thừa nhỏ; lật ngang; ghép từ hai ứng viên; dùng một góc nhìn khác đã có.
- 3D: chỉnh hướng, tỉ lệ, số tam giác bằng preset; sửa nhỏ, tô lại màu trong Blender.

**Không sửa được:**
- sai đề (sai con vật, nhân vật, công trình);
- giải phẫu sai lớn ở chỗ người chơi thấy;
- phong cách lệch hẳn bộ ảnh;
- tư thế không dựng hoặc rig được;
- model Tripo vỡ hình.

## 3. Mức cần

| Mức | Nghĩa | Khi nào làm |
|---|---|---|
| **P1** | Game đang dùng hoặc cần cho bản chơi, mốc đang làm. Thiếu thì game hiện hình tạm hoặc hỏng. | Làm trước. |
| **P2** | Cần cho mốc kế tiếp đã lên lịch. | Sau P1. |
| **P3** | Trang trí, biến thể thêm, tùy chọn, mốc xa. | Chỉ khi có kinh phí. |

- Tạo mới theo thứ tự P1 rồi P2; P3 chờ.
- Thay ảnh trong danh sách tạm chấp nhận: P1 trước, và chỉ khi có kinh phí.

## 4. Ai chấm, ghi ở đâu

- **Codex** tự chấm từng ảnh khi giao, ghi điểm và mức vào README giao nhận của phiếu.
- **Claude** chấm lại khi duyệt. Ảnh sát ngưỡng thì hai người chấm độc lập: model 3D từ 6 tới 7,5 hoặc mức "Tạo lại", ảnh 2D từ 7,5 tới 8,5. Lệch nhau từ 2 điểm thì có người thứ ba.
- **Model Tripo** (chủ dự án tạo tay trên web) chấm theo cùng thang, trên ảnh render ba góc. Claude chỉ đề nghị tạo lại khi model dưới 7 và không sửa được bằng preset hay Blender.
- Báo cáo kiểm ảnh ghi **điểm và mức**, không chỉ "đạt" hay "chưa đạt".
