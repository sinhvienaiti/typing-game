# Phiếu 014 · Tu Tiên Thủ Ải · 8 avatar vẽ tay thử nghiệm (mặt khác hẳn nhau)

**Yêu cầu của chủ dự án (25/10):**
1. Gương mặt hiện tại là "mặt AI" tràn lan, giống các game khác.
2. Gương mặt chủ yếu dùng làm **avatar**, nên làm **dạng vẽ**: đẹp và phong phú hơn.
3. Các mặt hiện tại y như nhau, chỉ khác màu da và cái áo. Phải khác thật ở **khuôn mặt**, nhiều hướng: rất đẹp, rất tà ác, rất mạnh mẽ…; có người **trẻ** và **trung niên**.

Làm **vài mẫu xem thử trước**. Chưa sửa danh sách nhân vật, chưa làm ảnh nguồn 3D.

**Nguyên nhân mặt giống nhau:**
- prompt cũ dùng "strikingly beautiful, delicate harmonious features, luminous skin";
- mọi ảnh đính kèm cùng chân dung A.

**Ở phiếu này:**
- **Không đính kèm ảnh chân dung cũ nào.**
- Mỗi người tả khuôn mặt riêng: dáng mặt, xương gò má, mũi, mắt, mày, môi, tuổi, nếp nhăn, sẹo, nốt ruồi, biểu cảm.

**Thư mục làm việc:** gốc repo `D:\typing-game`. Chỉ được ghi vào:
- `games/immortality-cultivation/art-src/avatar-test/` (ảnh và prompt);
- `games/immortality-cultivation/art-src/_review/014-avatar-test.jpg`;
- `games/immortality-cultivation/art-src/README-014.md`.

Không chạy git, không sửa ảnh có sẵn.

## Phong cách chung (vẽ tay, không phải ảnh)

- Tranh **minh họa vẽ tay**: nét mực rõ, có nhấn nhá; tô màu kiểu màu nước và gouache trên giấy dó.
- Sắc độ thủy mặc; ánh sáng có chủ ý, hợp tính cách.
- Chất **sơn thủy huyền ảo Việt**: trang phục và trang sức cổ, chi tiết hoa văn Việt (mây, sóng, hạc, rồng thời Lý).
- **Tránh:** da sứ bóng, mắt to quá cỡ, cằm V nhọn, môi bóng, mặt đối xứng hoàn hảo, nét idol; kiểu anime hay ảnh 3D bóng bẩy.
- Mỗi người phải nhận ra ngay khi chỉ còn bóng đầu.
- **Khung avatar:** bán thân từ ngực lên, mặt chiếm khoảng 40 % chiều cao, nền đơn giản theo màu tính cách. Ảnh 1024 × 1024. Không chữ, không khung.
- **Luật canon D47:** kín đáo, không gợi cảm, không máu, hợp mọi lứa tuổi. Nhân vật tà ác thể hiện bằng ánh mắt, dáng, ánh sáng, không bằng máu hay kinh dị.

## 8 mẫu

| Tệp | Người | Hướng khuôn mặt (tả riêng, khác hẳn nhau) |
|---|---|---|
| `a01-nu-kiem-tre` | Nữ kiếm tu, ~20 | **Rất đẹp, thanh cao:** mặt trái xoan dài, mắt một mí dài và sắc, mày lá liễu, sống mũi thẳng nhỏ, nốt ruồi dưới mắt; tóc búi cao, trâm ngọc |
| `a02-nam-kiem-trung-nien` | Nam kiếm khách, ~45 | **Mạnh mẽ, từng trải:** mặt vuông, xương gò má cao, sẹo chéo qua mày, râu quai nón tỉa ngắn có sợi bạc, mắt sâu nheo, môi mím |
| `a03-nu-ta-tu` | Nữ tà tu, ~32 | **Đẹp nhưng tà ác:** mặt hẹp, gò má nhô, mắt xếch nửa khép, ánh nhìn lạnh, môi mỏng nhếch một bên, móng dài sẫm; khói mực tím quanh vai |
| `a04-nam-ma-dau` | Ma đầu, ~50 | **Rất tà ác, uy hiếp:** mặt gầy dài, má hóp, mũi khoằm, mày rậm xếch, mắt ánh đỏ sẫm mờ, tóc xám búi lệch; ánh sáng từ dưới lên |
| `a05-nam-the-tu-tre` | Thổ thể tu, ~24 | **Mạnh mẽ, chất phác:** mặt tròn bè, hàm rộng, mũi to, mày đậm thẳng, da rám nắng, nụ cười rộng thật thà, cổ to; giáp ngọc thổ |
| `a06-nu-truong-lao` | Nữ trưởng lão, ~55 | **Uy nghiêm, sắc sảo:** mặt dài, nếp nhăn khóe mắt và hai bên mũi, tóc muối tiêu búi chặt, mắt nhỏ sáng, cằm nhọn ngẩng cao; áo chàm thêu bạc |
| `a07-thieu-nien-phu-tu` | Thiếu niên phù tu, ~17 | **Lanh lợi, tinh nghịch:** mặt tròn, má phúng phính, răng khểnh, mắt tròn sáng, tóc rối buộc dở, vết mực trên má; cầm bút phù |
| `a08-nam-hoa-tu` | Hỏa tu, ~38 | **Kiêu ngạo, nóng nảy:** mặt chữ điền góc cạnh, mày rậm cau, mắt hổ phách, râu ria nhọn, tóc dựng kiểu ngọn lửa buộc cao; ánh lửa hắt một bên mặt |

## Việc

1. **Viết 8 prompt** theo bảng trên. Mỗi prompt có:
   - phong cách chung;
   - tả khuôn mặt chi tiết;
   - trang phục theo trường phái;
   - một câu tránh mặt AI phổ biến.

   Lưu `avatar-test/<tệp>.png` và `<tệp>.prompt.txt` cạnh ảnh.
2. **Mở xem từng ảnh.** Nếu mặt còn giống mặt idol AI, hoặc giống một ảnh trước đó, sửa prompt và tạo lại, tối đa 1 lần.
3. **Ảnh xem nhanh** `_review/014-avatar-test.jpg`, dùng ImageMagick trong WSL (`~/.local/bin/magick montage`, font `/mnt/c/Windows/Fonts/arial.ttf` để có dấu):
   - lưới 4 × 2, có nhãn tiếng Việt (tên vai, tuổi);
   - thêm một hàng thu nhỏ 128 px, cỡ avatar trong game.
4. **Viết `README-014.md`:** mỗi ảnh một dòng (đạt chưa, khác các ảnh khác ở đâu), và nhận xét chung về phong cách.

**Xong khi:** 8 ảnh, ảnh xem nhanh và README đã có.
