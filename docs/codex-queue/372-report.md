# Phiếu 372 · Cổng ải v2 · 12/11/2026

Đã tạo bằng image_gen **2/8 lượt**, xem ảnh **5/10 lượt**. Giữ nguyên cổng cũ.

Trong `games/immortality-cultivation/art-src/props/`:
- `cong-ai.v2-{q,front}-raw.png`: đầu ra nguyên bản.
- `cong-ai.v2-{q,front}-final.png`: hai góc 2048 × 1152.
- `cong-ai.v2-{q,front}-final.prompt.txt`: prompt nguyên văn, đường dẫn tham chiếu và hậu kỳ.
- `cong-ai-372-sheet.jpg`: cũ | mới hai góc, bản cao 90 px, cặp raw | final.

Cổng mới rộng, thấp; một vòm đá mở, hai bệ tường, mái ngói chàm hai tầng, đầu đao cong, phù điêu vân mây/hồi văn và phướn chàm gắn sát thân. Kiến trúc lấy từ tranh màn tựa đã chọn; chất liệu theo ảnh vua sói v7.

**Kiểm script:** khối q/front rộng **1483/1637 px**, cao **739/740 px**, lệch chiều cao **0,14%**. Chính diện rộng/cao **2,21**. Lề L/R/T/B: q **13,77/13,82/17,88/17,97%**; front **10,01/10,06/17,88/17,88%**. Mỗi ảnh một khối 8-liên thông, không mảnh rời. Nền góc đúng `#00FF00`; alpha **255** toàn ảnh, theo chuẩn nền xanh đục v7. Matte được tách và khử tràn xanh trước khi căn giữa; không kéo méo, không vẽ thêm.

**Tự chấm ảnh nguồn:** cùng bộ **8,7**; đẹp từ trên **8,8**; trọn khung nguồn **9,0**; phù hợp Tripo **8,6**; chất Việt **8,7**. Mặt yếu nhất **8,6/10**. Ở 90 px, vòm mở và hai tầng mái vẫn đọc rõ. Đây là tự chấm nguồn, chưa thay hai giám khảo độc lập trong play host.

Không dựng Tripo, tích hợp, build hay test game vì ngoài phiếu. Chưa xác nhận cắt khung tại camera 55° trong runtime. Anh xem tấm ghép, nhất là độ thấp và dáng mái ở 90 px.
