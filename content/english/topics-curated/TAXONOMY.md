# Bảng Phân Loại Từ Vựng Tiếng Anh Theo Chủ Đề (Curated Topics Taxonomy)

Hệ thống phân loại này được xây dựng nhằm phục vụ việc học từ vựng trực quan, thực hành phát âm và luyện gõ 10-ngón theo ngữ cảnh tự nhiên cho người học tiếng Anh (đặc biệt là người Việt Nam).

## 1. Nguyên Tắc Thiết Kế
1. **Gần gũi & Thực tế:** Ưu tiên các chủ đề gắn liền với sinh hoạt hàng ngày, gia đình, công sở, mua sắm, ẩm thực và sức khỏe.
2. **Xử lý từ đa nghĩa (Polysemy):** Cùng một `headword` nhưng nếu có các nghĩa khác nhau thuộc về các chủ đề khác nhau, hệ thống cho phép xuất hiện ở các topic tương ứng kèm theo trường `senseNote` giải thích nghĩa cụ thể trong topic đó (không gộp nhầm lẫn).
3. **Phân tầng CEFR & Độ ưu tiên:** Mỗi từ được ghi nhận `cefr` (A1, A2, B1, B2) và `priority` (`core` cho từ nòng cốt tần suất cao, `support` cho từ bổ trợ).
4. **Tích hợp văn bản hoàn chỉnh:** Mỗi chủ đề khi tích lũy 10–15 từ cùng cấp độ sẽ có các bài đọc ngắn ~250–350 từ lồng ghép mượt mà toàn bộ các từ này.

## 2. Danh Sách 18 Nhóm Chủ Đề & 100+ Topics Cụ Thể

| STT | Mã Nhóm (Group ID) | Tên Nhóm (Tiếng Anh / Tiếng Việt) | Các Chủ Đề Con (Topics) Tiêu Biểu |
| :---: | :--- | :--- | :--- |
| 1 | `everyday-life` | Everyday Life / Đời sống hàng ngày | Chào hỏi, thói quen sinh hoạt, thời gian, đồ dùng cá nhân, việc nhà, vệ sinh cá nhân, sở thích. |
| 2 | `food-drink` | Food & Drink / Ẩm thực & Đồ uống | Hoa quả, rau củ, thịt gia cầm, hải sản, lương thực & ngũ cốc, sữa & trứng, gia vị, đồ uống, bánh ngọt, nấu nướng, nhà hàng. |
| 3 | `home-living` | Home & Living / Nhà cửa & Đời sống gia đình | Phòng ốc, đồ nội thất, thiết bị gia dụng, dụng cụ bếp, đồ dùng bàn ăn, phòng ngủ & tắm, sửa chữa nhà cửa, vườn tược. |
| 4 | `clothing-fashion` | Clothing & Fashion / Trang phục & Thời trang | Quần áo thường ngày, đồ công sở/dự tiệc, áo khoác, giày dép, phụ kiện thời trang, trang sức, chất liệu & họa tiết. |
| 5 | `body-health` | Body & Health / Cơ thể & Sức khỏe | Bộ phận cơ thể ngoài, cơ quan nội tạng, triệu chứng cảm sốt, khám chữa bệnh & bệnh viện, thuốc men, thể dục & rèn luyện, sức khỏe tinh thần. |
| 6 | `people-family` | People & Relationships / Con người & Mối quan hệ | Gia đình & họ hàng, bạn bè & xã hội, tình yêu & hôn nhân, ngoại hình, tính cách, cảm xúc tâm trạng. |
| 7 | `travel-transport` | Travel & Transportation / Giao thông & Du lịch | Phương tiện đường bộ, xe buýt & tàu điện, hàng không & sân bay, đường sắt & ga tàu, lái xe & luật giao thông, khách sạn lưu trú, thắng cảnh du lịch, hành lý. |
| 8 | `education-learning` | Education & Learning / Giáo dục & Học tập | Trường học các cấp, lớp học & đồ dùng học tập, môn học, thi cử & điểm số, đại học & nghiên cứu, học ngoại ngữ. |
| 9 | `work-career` | Work & Career / Công việc & Sự nghiệp | Nghề nghiệp, môi trường văn phòng, công cụ lao động & thiết bị nghề, tuyển dụng & phỏng vấn, kinh doanh & vận hành, họp hành & email, quản lý dự án & nhiệm vụ. |
| 10 | `finance-shopping` | Finance & Shopping / Tài chính & Mua sắm | Tiền tệ & thanh toán, ngân hàng & tài khoản, chợ & siêu thị, mua sắm online & giao hàng, tiết kiệm & ngân sách, đầu tư & thương mại. |
| 11 | `technology-digital` | Technology & Digital Life / Công nghệ & Đời sống số | Thiết bị số & phần cứng, phần mềm & ứng dụng, internet & trang web, mạng xã hội, nhắn tin & email, an toàn thông tin & bảo mật. |
| 12 | `nature-environment` | Nature & Environment / Tự nhiên & Môi trường | Thời tiết & khí hậu, bốn mùa, địa lý núi sông biển rừng, cây cối hoa cỏ, bảo vệ môi trường & tái chế. |
| 13 | `animals-wildlife` | Animals & Wildlife / Động vật & Muông thú | Thú cưng, gia súc nông trại, động vật hoang dã, sinh vật biển, chim muông & côn trùng. |
| 14 | `sports-fitness` | Sports & Recreation / Thể thao & Vận động | Thể thao bóng & đồng đội, thể thao cá nhân, dụng cụ thi đấu, giải đấu & tỉ số. |
| 15 | `arts-culture` | Arts & Culture / Nghệ thuật & Văn hóa | Âm nhạc & nhạc cụ, hội họa & mỹ thuật, điện ảnh & kịch nghệ, văn học & sách truyện, lễ hội & phong tục. |
| 16 | `society-law` | Society & Public Life / Xã hội & Đời sống công cộng | Đô thị & đường phố, dịch vụ công cộng, luật pháp & quy tắc, cộng đồng & thiện nguyện. |
| 17 | `communication-speech` | Communication & Speech Acts / Giao tiếp & Tư duy ngôn ngữ | Bày tỏ quan điểm & đồng ý, thảo luận & tranh luận, nguyên nhân & kết quả, miêu tả tính chất & so sánh. |
| 18 | `abstract-core` | Core Concepts / Khái niệm cốt lõi & Từ chức năng | Hình khối & kích thước, màu sắc, số đếm & lượng từ, phương hướng & vị trí, động từ hành động cơ bản, tính từ thông dụng. |
