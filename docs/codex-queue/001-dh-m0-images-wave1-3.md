# Phiếu 001 · Rồng Giữ Ải · ảnh 2D M0, đợt 1 và đợt 3

**Làm trong:** `games/dragon-hold/art-src/` (gitignored, là media). Thư mục làm việc của lần chạy: `games/dragon-hold`.

**Nguồn prompt.** Mỗi khối ```text là một ảnh, dán nguyên văn, không rút gọn, không thêm bớt. Đọc trước:
- `../../docs/games/dragon-lane/art-requests/m0/README.md`: mục lục, khối "Instructions for the image tool", thứ tự làm §2;
- `../../docs/games/dragon-lane/art-requests/m0/01-creatures.md` §1–2: luật chung và bảng ảnh.

**Quyết định đã có:** dấu Héo **A**, là mặc định của thiết kế ("phủ một phần thân", 01 §1), đã chọn theo đề xuất. Mọi prompt trong các file đã viết theo A, giữ nguyên.

## Việc

1. **Chép các ảnh mẫu đã duyệt** từ `art-src/2d/samples/` sang đúng đường dẫn của bảng ảnh. Cột "File" bỏ tiền tố `games/dragon-hold/art-src/`.
   - Chép ảnh: `refs/heo-test-a.png`, `refs/heo-test-b.png`, `enemies/moss-grunt.png`, `enemies/blight-wolf.png`, `enemies/blight-wolf-front.png`, `enemies/thorn-wasp.png`.
   - Chép kèm file `.prompt.txt` của từng ảnh.
   - Không xóa gì trong `samples/`.
2. **Đợt 1** (01-creatures.md): tạo **E09-B** `enemies/moss-grunt-back.png`, đính kèm `enemies/moss-grunt.png`, và **E01-S** `enemies/thorn-wasp-side.png`, đính kèm `enemies/thorn-wasp.png`.
3. **Đợt 3:** tạo mọi ảnh của `03-pine-river-props.md` (12 prop) và `04-2d-ground-decals-backdrop.md` (8 ô đất, 4 decal, 1 phông xa). Đường dẫn lưu và khổ ảnh theo bảng của từng file.
4. **Cách lưu mỗi ảnh:**
   - Lưu đúng đường dẫn, kèm `<tên>.prompt.txt` ghi nguyên văn prompt.
   - Ảnh nào đã có thì **bỏ qua**, không tạo lại.
   - Khổ ảnh trả về khác yêu cầu thì vẫn lưu, và ghi lại trong báo cáo.
5. **Tự kiểm từng ảnh** theo bảng kiểm của file (ví dụ 01 §12): một chủ thể, đủ thân, nền `#E6E6E6`, không chữ, không bóng.
   - Ảnh hỏng rõ thì tạo lại **tối đa 1 lần**.
   - Vẫn hỏng thì giữ bản tốt hơn và ghi lý do.
6. **Viết `art-src/2d/README-m0-wave1-3.md`** (tiếng Việt), theo kiểu `README-samples.md`. Gồm bảng ảnh đã tạo, nhận xét "Đạt / Ghi chú" từng ảnh, và việc chủ dự án cần xem.

**Không được đụng:** mọi file ngoài `games/dragon-hold/art-src/`. Không sửa tài liệu trong `docs/`. Không chạy git.

**Xong khi:** đủ 2 + 25 ảnh mới (hoặc ghi rõ ảnh nào không tạo được), 6 ảnh mẫu đã chép, README đã viết. Báo cáo cuối liệt kê đường dẫn từng ảnh.
