# Nghiên cứu thiết kế boss thú vương (Thiết Bối Lang Vương) — 12/11/2026

Lưu ý trung thực: tìm kiếm cho ra rất ít bài phân tích thiết kế thật sự. Phần lớn nguyên tắc dưới đây là **suy luận từ nguồn mỏng + kiến thức nghề**, đã gắn nhãn. Không tải hay nhúng ảnh bên thứ ba.

## 1. Nguồn

Nhãn: **[V]** = đã mở trang; **[S]** = chỉ thấy đoạn trích kết quả tìm kiếm (chưa xác minh).

| Nguồn | Cho thấy gì | |
|---|---|---|
| https://blackmythwukong.vercel.app/docs/lingxuzi | Lingxuzi: "linh hồn sói xám khổng lồ", lông dày (yếu lửa), đòn bằng vuốt trước, quét và cắn lao tới, tiếng hú gây sát thương diện rộng; bạn đồng hành của Hắc Phong Đại Vương; dựa trên sói linh trong thần thoại. Không mô tả mặt. | [V] (fan-wiki, mỏng) |
| https://gamerguides.com/black-myth-wukong/database/enemies/yaoguai-chiefs/guangzhi | Quảng Trí: sói nhỏ muốn làm người, giả thành nhà sư. | [S] (403 khi mở) |
| https://mp1st.com/news/black-myth-wukong-boss-fight-gameplay-features-red-loong-and-guangzhi | Quảng Trí: thú giống sói, tu ở tự viện, cầm giáo hai đầu lửa. | [S] |
| https://www.gameinformer.com/preview/2024/06/16/a-classic-tale-retold | Đánh bại Quảng Trí mở phép biến sói + Scorch Bane. | [S] |
| https://80.lv/articles/30-of-black-myth-wukong-players-aren-t-from-china-the-game-s-art-director-says/ ; https://thegameswiki.com/black-myth-zhong-kui/wiki/yang-qi | Yang Qi (hoạ sĩ sơn dầu, học tranh thuỷ mặc) dẫn đoàn khảo sát ≥36 địa điểm thật (chùa, tượng đá Đại Túc); mục tiêu "vẻ đẹp kỳ dị" của yêu quái. | [S] (nguồn thứ cấp) |
| https://abookofcreatures.com/2016/08/08/qiongqi/ | Cùng Kỳ theo Sơn Hải Kinh: thân bò phủ gai nhím, tiếng như chó sủa; biến thể hổ có cánh; biến thể người đầu chó. Ăn thịt từ đầu/chân, săn người tóc dài, ác nhưng cũng ăn độc trùng. | [V] |
| https://en.wikipedia.org/wiki/Tiangou (qua kết quả tìm kiếm) | Thiên Cẩu: giống chó đen hoặc sao băng, nuốt nhật/nguyệt; về sau là thần giữ cổng. Có biến thể lành (giống cáo đầu trắng). | [S] |
| Dịch Sơn Hải Kinh (Wikipedia/ipfs mirror) | Chúc Âm/Chúc Long: thần đỏ rực, mặt người, thân rắn, mắt dọc, mở mắt là ngày, nhắm là đêm. Dịch thuật không thống nhất. | [S] |
| https://sportskeeda.com/esports/genshin-impact-developers-reveal-making-azhdaha-latest-weekly-boss | Azhdaha: nhóm không muốn rồng Đông hay Tây thuần; thử cá sấu, Komodo, rùa cắn, rồi chọn **khủng long Stegosaurus**; cơ chế khiên Geo; đuôi là vấn đề lớn khi dựng/animation. | [S] (mở lỗi mạng) |
| https://gamerant.com/monster-hunter-rise-magnamalo-concept-art-twitter/ (+ tìm kiếm) | Magnamalo: nền là hồn ma võ sĩ giáp, ảnh hưởng hổ, mặt giống mặt nạ oni, hoả ma (onibi). | [S] |
| https://gamingcypher.com/naraka-bladepoint-interview | Naraka: phong cách nhắm tới nét bút và khoảng trống của tranh Trung Hoa. Không có tư liệu quái vật. | [S] |

Không tìm được: concept art/giải thích thiết kế của Lingxuzi, Hắc Phong Đại Vương, Swallowed Star, Where Winds Meet, Perfect World donghua. Cần xin chủ dự án ảnh tham chiếu tay nếu muốn đào sâu.

## 2. Nguyên tắc thiết kế

1. **Lai giữa các loài, đừng một loài.** Cùng Kỳ là bò + gai nhím + tiếng chó; Taotie là cừu + mặt người + răng hổ; Azhdaha lấy khủng long làm xương sống. Boss đáng sợ khi có 1 loài chủ và 1–2 phần lạ lẫm, không phải "chó thật + giáp". (Qiongqi [V]; Azhdaha [S]; Taotie [S])
2. **Đối lập của nó là "lạ", không phải "to".** Mắt dưới nách (Taotie), mắt dọc (Chúc Âm), mặt người trên thân thú: sự sai lệch đáng sợ hơn kích thước. (Sơn Hải Kinh [S])
3. **Vương giả = đối xứng + khối lớn + tư thế.** Đầu giữ cao, vai nặng, đứng bất động. Vẻ "thú cưng" đến từ tư thế cúi thấp hoặc ngồi, cổ mảnh, đầu nhỏ trên thân dày lông. (suy luận, chưa có nguồn trực tiếp)
4. **Danh tính tu tiên = đã từng là thứ gì đó khác.** Quảng Trí là sói muốn làm người mặc áo sư; Lingxuzi là "linh hồn sói". Biến dị do khí/linh phải thể hiện bằng một đặc điểm cụ thể (mặt nạ, đá, hương, bùa), không phải thêm vòng sáng. (Quảng Trí [S]; Lingxuzi [V])
5. **Chất liệu địa phương hoá.** Thiết kế dựa trên điêu khắc đá, chùa, tượng thật; yêu quái có cảm giác cổ, mài mòn, "đẹp kỳ dị". Một bộ lông "đá + mực" nhất quán hơn cả bộ giáp rời. (Yang Qi [S, thứ cấp])
6. **Giáp phải là một phần cơ thể.** Magnamalo: giáp ma, mặt oni nằm ngay trong khối đầu. Giáp "gắn thêm" như yên cương làm thú giống vật nuôi. (Magnamalo [S])
7. **Khuôn mặt mang 80% sự đáng sợ.** Mặt nạ oni (Magnamalo), mắt dọc (Chúc Âm), hàm lệch. Mắt phát sáng tròn đối xứng = "dễ thương/ngầu rẻ". (Magnamalo [S]; Chúc Âm [S])
8. **Một điểm nhấn màu, phần còn lại giá trị thấp.** Lingxuzi chỉ nhắc "xám"; Chúc Âm chỉ nhắc đỏ. Boss đọc được ở cỡ nhỏ nhờ một vùng tương phản (đầu/mắt) trên thân phẳng màu. (Lingxuzi [V]; Chúc Âm [S]; kết hợp nguyên tắc "một điểm nhấn" của dự án)
9. **Đuôi, tóc, dây xích là vấn đề.** Dự án Azhdaha báo đuôi gây khó khi dựng/animation; với Tripo, dải mảnh sẽ vỡ. Thay bằng khối đặc (bờm đá tảng, gai cứng). (Azhdaha [S]; thực tế Tripo)
10. **Bóng thú phải đổi theo góc nhìn trên cao.** Nhìn từ 55° thấy lưng, vai, đỉnh đầu, không thấy mặt: nhận dạng phải nằm ở **hình lưng + hình đầu từ trên xuống**. (suy luận kỹ thuật, chưa có nguồn)
11. **Hành vi định hình thiết kế.** Cùng Kỳ ăn từ đầu, săn người tóc dài; Lingxuzi hú gây sát thương diện rộng: thú vương cần một "đặc ngữ" (hú, nuốt, bẻ). (Qiongqi [V]; Lingxuzi [V])
12. **Thần thoại cho phép khuyết tật.** Thiên Cẩu là chó đen nuốt trăng; thú ác trong Sơn Hải Kinh thường thiếu/dư bộ phận. Đối xứng hoàn hảo + thiếu một vật là cách vừa vương vừa ma. (Thiên Cẩu [S])

## 3. Ba hướng cho Thiết Bối Lang Vương (chỉ mô tả bằng lời)

Chung: thú bốn chân lực lưỡng, đứng thẳng cao, **không xích, không tóc sợi, không bờm xơ**. Không dùng đỏ mạnh, cam, vàng sáng, xanh ngọc.

### A. "Sói Núi Đá" — lưng là dãy núi
- **Bóng:** thân thấp ngang vai nhưng lưng nhô lên thành dãy 5–7 tảng đá tù xếp dọc sống lưng, như dãy núi thu nhỏ; đầu cao, thẳng.
- **Tỉ lệ:** đầu ≈ 1/4 thân, cổ ngắn rất dày, vai cao hơn mông, chân trước to gấp rưỡi chân sau.
- **Vương miện/bờm:** vương miện là một vòng sừng đá mọc từ xương trán, 3 chóp lớn; bờm là các tấm vảy đá đặc.
- **Mặt:** mõm dài, hàm dưới lệch, một mắt đóng bằng vảy đá, mắt kia mở. Không tròn đều.
- **Biến dị:** nứt chạy ngang sống lưng, bên trong là mực than loãng.
- **Màu:** xám than (nền), xám nhạt ấm (tảng đá), điểm nhấn **trắng ngà ở mắt mở + sừng**.
- **Đọc ở 66 px:** hình dãy tảng lồi trên lưng, đầu có ba chóp, mảng sáng ở mắt. Tripo: khối đặc, dễ.

### B. "Thiên Cẩu Hắc Mực" — nuốt trăng
- **Bóng:** thân dài dạng chó săn gầy cơ bắp, lưng có một vòng tròn mặt trăng bị cắn khuyết đặt đứng sau vai (mảng đá dẹt).
- **Tỉ lệ:** vai rộng, hông hẹp, đầu thấp nhưng sọ rất lớn.
- **Vương miện:** vòng tròn khuyết thay cho vòng sáng; sừng ngắn hình lưỡi liềm.
- **Mặt:** không mắt, hai hốc mắt đen; hàm mở như đang nuốt.
- **Biến dị:** lông mực chảy nhỏ giọt thành vệt đặc (khối, không sợi); dấu bùa chỉ khắc nông trên vòng trăng.
- **Màu:** đen xanh than, xám lạnh, nhấn **trắng bạc ở mép trăng khuyết**.
- **Đọc ở 66 px:** vòng khuyết trên lưng đọc rõ từ trên xuống. Tripo: vòng mỏng cần dày ≥ 8% thân.

### C. "Sói Mặt Nạ Oni" — vương mặc mặt quỷ
- **Bóng:** thân vạm vỡ hình chữ nhật, vai gù, đầu thấp trước thân, hai vai gai cong.
- **Tỉ lệ:** đầu lớn như 1/3 thân; mõm ngắn, mặt rộng.
- **Vương miện:** mặt nạ sừng hai chóp phủ nửa mặt trên, như "mặt thứ hai" nằm dựng.
- **Mặt:** mặt nạ nhăn nhúm, mắt chéo, răng nanh lệch; sói thật ẩn phía sau.
- **Biến dị:** hai chân trước dài hơn, đầu gối xương lồi; một vai bị khoá bằng tảng đá.
- **Màu:** nâu bùn đậm, xám đất, nhấn **xanh lam xám nhạt ở mắt mặt nạ**.
- **Đọc ở 66 px:** hình đầu lớn + vai gai cho bóng "thú dữ" khác hẳn chó. Tripo: gai thô dày.

Khuyến nghị: bắt đầu với **A** (đá + tư thế vương), mượn phần mắt không đều của C.

## 4. v3–v5 sai ở đâu

- **v3** (sói xám xù lông, cúi thấp, giáp vai chạm khắc, xích đồng treo thẻ ngọc, gân tím mờ):
  - nguyên tắc 3: cúi thấp không vương giả;
  - nguyên tắc 6: giáp vai/xích là đồ đeo thêm;
  - nguyên tắc 9: xích + thẻ ngọc là mảnh treo, Tripo vỡ, và ngọc là màu tín hiệu;
  - nguyên tắc 8: gân tím mờ quá yếu, không có điểm nhấn;
  - lông xù làm bóng mờ khi nhìn từ trên.
- **v5** (sói xù lông đứng thẳng, có vòng cổ):
  - nguyên tắc 1, 2: không có phần lạ; chỉ là chó/sói đẹp;
  - nguyên tắc 6: vòng cổ = thú cưng;
  - nguyên tắc 3: đứng thẳng nhưng đầu nhỏ trên lông dày;
  - nguyên tắc 10: không có hình lưng đặc trưng cho góc 55°.
- Cả hai thiếu: mặt khác thường, hình lưng riêng và một điểm nhấn màu rõ.
