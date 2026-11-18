# Chấm mù nguồn 2D nữ chính Tu Tiên, phiếu 436f (18/11/2026)

- **Mục đích:** kiểm tra cổng chất lượng trước khi đưa sang Tripo. Chuẩn: hai giám khảo mù độc lập, cả hai cùng ≥ 8.5 ở mọi trục.
- **Tờ nguồn:** `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/heroine-fashion-436f/heroine-turnarounds-436f.jpg`.
- **File chấm:** PNG gốc 1536×1024 trong `games/immortality-cultivation/art-src/heroine/fashion/`. Thân nền dùng `try1`, đúng bản trên tờ giao.
- **Cách làm:**
  - Hai agent mới, chưa xem vòng nào trước, mỗi agent chỉ thấy một thư mục có 5 ảnh nhãn trung tính và một README mô tả.
  - Khoá nhãn để ngoài thư mục chấm. Giám khảo không đọc prompt hay báo cáo.
  - Mốc so sánh là thị trường: các game tiên hiệp đang hot, tính là 9.
  - Trục chấm:
    - **M/A:** sức hút và mức thị trường;
    - **C:** nhất quán giữa ba góc;
    - **B:** mặt sau có phải lưng thật;
    - **T:** độ phù hợp với Tripo.
- **Lưu ý:** game chưa có bảng tham chiếu thương mại cho nhân vật trong repo, nên giám khảo chấm theo hiểu biết thị trường. Vòng sau nên bổ sung bảng tham chiếu.

## Khoá nhãn

| Nhãn | File |
|---|---|
| Board 1 | `jade-noble-turn.v1-try1.png` (Jade Noble) |
| Board 2 | `base-body.v3-turn.v1-try1.png` (thân nền v3) |
| Board 3 | `shadow-spider-turn.v1-try1.png` (Shadow Spider) |
| Board 4 | `crimson-bride-turn.v1-try1.png` (Crimson Bride) |
| Board 5 | `moon-blade-turn.v1-try1.png` (Moon Blade) |

## Điểm hai giám khảo

| Bộ | Giám khảo A (M/A · C · B · T) | Giám khảo B (M/A · C · B · T) |
|---|---|---|
| Thân nền v3 | 8.0 · 8.6 · 9.0 · 8.3 | 8.2 · 9.0 · 9.0 · 8.3 |
| Crimson Bride | 8.7 · 8.4 · 8.0 · 5.0 | 8.7 · 8.4 · 7.5 · 5.0 |
| Moon Blade | 8.2 · 8.7 · 8.8 · 6.5 | 7.9 · 8.6 · 8.8 · 6.0 |
| Jade Noble | 8.3 · 8.0 · 8.8 · 7.5 | 8.6 · 8.6 · 9.0 · 7.3 |
| Shadow Spider | 8.2 · 8.7 · 8.8 · 6.5 | 7.8 · 8.6 · 8.7 · 6.5 |

## Kết luận gộp theo bộ

Một bộ chỉ đạt khi cả hai giám khảo cho ≥ 8.5 ở mọi trục. **Không bộ nào đạt. Chưa bộ nào được đưa sang Tripo.**

| Bộ | Kết luận | Trục hỏng |
|---|---|---|
| Thân nền v3 | **Không đạt, sửa** | T 8.3/8.3 và M/A 8.0/8.2. Đây là bộ gần đạt nhất. |
| Crimson Bride | **Không đạt, vẽ lại bản nguồn Tripo** | T 5.0/5.0, B 8.0/7.5, C 8.4/8.4. Riêng M/A thì đạt (8.7/8.7). |
| Moon Blade | **Không đạt, sửa lớn** | T 6.5/6.0, M/A 8.2/7.9 |
| Jade Noble | **Không đạt, sửa** | T 7.5/7.3. Giám khảo A còn cho M/A 8.3 và C 8.0. |
| Shadow Spider | **Không đạt, vẽ lại** | T 6.5/6.5, M/A 8.2/7.8 |

**Lỗi chung của cả bộ:**
- Quá nhiều vật liệu xuyên thấu (ren, voan, kính) và vạt vải mỏng như giấy. Tripo sẽ dựng chúng thành mảng đặc loang lổ hoặc lỗ thủng.
- Góc mở tay A-pose khác nhau giữa các bảng, khoảng 20–30°.
- Thân nền nhỏ hơn các bảng trang phục khoảng 4–6 %, nên chưa khớp một bộ xương.

**Điểm tốt:** cả hai giám khảo đều nhận ra cùng một khuôn mặt và cùng tỷ lệ thân ở cả năm bảng. Các phụ kiện lệch một bên (vòng tay, nịt đùi, áo choàng, kiếm) đều đúng bên ở cả ba góc.

## Danh sách sửa

### Chung cho mọi bảng

1. Cùng một A-pose: tay mở 35–45°, lòng bàn tay hướng vào đùi, hai bàn chân cách nhau bằng chiều rộng hông, có khe rõ giữa hai đùi và hai gối.
2. Cùng chiều cao hình và vị trí chân như nhau ở mọi bảng. Lề trên và lề dưới mỗi bên tối thiểu 40 px.
3. Bản nguồn Tripo không dùng vật liệu xuyên thấu:
   - ren và lưới đổi thành vải đặc in hoạ tiết;
   - voan, kính, dây xích mảnh và đạo cụ rời làm riêng sau, bằng cloth, shader, VFX hoặc asset riêng.
4. Gót giày dày, không dùng gót nhọn như kim.

### Thân nền v3

- Mở tay 35–45° và dạng chân như mục chung 1.
- Vẽ ở cùng chiều cao hình như các bảng trang phục.
- Kéo sống mũi và cằm ở góc nghiêng gần với mặt trước.
- Tăng độ hoàn thiện của da và mặt.
- Xác nhận với chủ dự án tỷ lệ chân dài (khoảng 8,5 đầu) là có chủ ý.

### Crimson Bride

- Làm bản nguồn Tripo **không có khăn voan**. Voan làm riêng bằng cloth hoặc shader.
- Găng tay vàng đặc.
- Rút đuôi váy lên cách sàn để lộ gót. Mặt sau phải thấy rõ lưng váy, gáy và búi tóc.
- Vẽ khối sau của mũ phượng cùng độ lớn và có tua hai bên như mặt trước.
- Lề trên tối thiểu 40 px. Hiện mũ phượng chỉ cách mép trên khoảng 7 px.

### Moon Blade

- Bỏ dải che mắt trong suốt. Cả hai giám khảo đều đọc nó là kính sci-fi. Thay bằng lụa đặc thêu viền, hoặc bỏ hẳn.
- Áo choàng thành vải đặc màu xanh bạc in hoạ tiết, kết thúc trên gối, cách cánh tay tối thiểu 40 px.
- Bỏ kiếm khỏi bản nguồn và làm kiếm thành asset riêng.
- Cân nhắc thay quần short và quần tất bằng váy ngắn có vạt hoặc quần võ phục. Cả hai giám khảo cho rằng short và tất quá hiện đại.

### Jade Noble

- **Lưới vàng thủng ở tay áo và vai:** tô kín thành hoạ tiết nổi trên vải đặc.
- **Tay áo:** thu hẹp khoảng 25 % và tách khỏi thân tối thiểu 40 px. Làm dày mép tay áo và mép vạt áo.
- **Tua ngọc bội:** rút ngắn đến giữa đùi. Gắn chuỗi hạt của trâm sát vào tóc.
- **Nhất quán (giám khảo A):**
  - mặt sau phải thêu quần giống mặt trước;
  - thống nhất một kiểu gót vuông thấp ở cả ba góc (mặt trước đang gần như đế bằng).
- **Sức hút (giám khảo A):** thêm một điểm nhấn hình khối kiểu chiến binh, ví dụ đai lưng có giáp nhẹ.

### Shadow Spider

**Vẽ lại.** Cả hai giám khảo đọc bộ này là phù thuỷ gothic phương Tây, không ra tiên hiệp. Hướng mới:
- **Bảng màu:** đổi xanh rêu sang lục bảo hoặc xanh ngọc, thêm viền vàng mây và một điểm sáng ngọc ở ngực.
- **Ren:** đổi thành vải đặc in hoạ tiết ren.
- **Vạt váy:** gộp còn tối đa 2–3 lớp dày.
- **Xích:** bỏ hoặc gắn sát thân.
- **Gót:** to hơn.

## Bước tiếp

1. Sửa theo danh sách trên.
2. Chấm lại bằng **hai giám khảo mới**, không dùng lại hai giám khảo của vòng này.
3. Chỉ khi cả hai giám khảo cho ≥ 8.5 ở mọi trục mới được dựng 3D.
4. Trước khi sinh lại ảnh, chủ dự án duyệt hướng mới của Shadow Spider và việc bỏ dải che mắt của Moon Blade, vì đó là thay đổi thiết kế.
