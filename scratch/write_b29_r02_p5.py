import json

# Manual cognitive QA review for Batch 29 Round 2 Part 5 (IDs 040902 to 041001)
reviewed_items = [
    {"id": "lex.en.200k.040902", "hw": "actuarial table", "pos": "phrase", "ipa": "", "vi": "bảng thống kê định phí bảo hiểm", "cefr": "C2", "tier": "business", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040903", "hw": "adirondack mountains", "pos": "phrase", "ipa": "", "vi": "dãy núi Adirondack bang New York", "cefr": "B2", "tier": "geography", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040904", "hw": "american woodcock", "pos": "phrase", "ipa": "", "vi": "chim dẽ gà Bắc Mỹ mỏ dài", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040905", "hw": "ant thrush", "pos": "phrase", "ipa": "", "vi": "chim hoét ăn kiến nhiệt đới", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040906", "hw": "big bill haywood", "pos": "phrase", "ipa": "", "vi": "nhà lãnh đạo công đoàn Haywood", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040907", "hw": "black cottonwood", "pos": "phrase", "ipa": "", "vi": "cây dương đen gỗ mềm Bắc Mỹ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040908", "hw": "bock beer", "pos": "phrase", "ipa": "", "vi": "bia bock đậm đà truyền thống Đức", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040909", "hw": "body politic", "pos": "phrase", "ipa": "", "vi": "chính thể quốc gia nhân dân", "cefr": "C2", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040910", "hw": "bombardier beetle", "pos": "phrase", "ipa": "", "vi": "bọ cánh cứng pháo thủ xịt hơi", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040911", "hw": "bosworth field", "pos": "phrase", "ipa": "", "vi": "trận đánh lịch sử Bosworth Field", "cefr": "C2", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040912", "hw": "buckwheat family", "pos": "phrase", "ipa": "", "vi": "họ thực vật rau răm kiều mạch", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040913", "hw": "buckwheat tree", "pos": "phrase", "ipa": "", "vi": "cây kiều mạch gỗ nhỏ hoa trắng", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040914", "hw": "buttercup family", "pos": "phrase", "ipa": "", "vi": "họ mao lương hoa vàng dại", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040915", "hw": "california buckwheat", "pos": "phrase", "ipa": "", "vi": "cây kiều mạch hoang California", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040916", "hw": "canton crepe", "pos": "phrase", "ipa": "", "vi": "vải crêp Quảng Châu dệt lụa", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040917", "hw": "cape canaveral", "pos": "phrase", "ipa": "", "vi": "mũi Canaveral bãi phóng tàu Mỹ", "cefr": "B2", "tier": "geography", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040918", "hw": "cerebral thrombosis", "pos": "phrase", "ipa": "", "vi": "chứng huyết khối động mạch não", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040919", "hw": "chain tongs", "pos": "phrase", "ipa": "", "vi": "kìm xích vặn ống nước kim loại", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040920", "hw": "charles eames", "pos": "phrase", "ipa": "", "vi": "nhà thiết kế Charles Eames", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040921", "hw": "china jute", "pos": "phrase", "ipa": "", "vi": "cây đay Trung Quốc vỏ dai", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040922", "hw": "clove hitch", "pos": "phrase", "ipa": "", "vi": "nút thắt thuyền kép buộc cọc", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040923", "hw": "coal tongs", "pos": "phrase", "ipa": "", "vi": "cái kẹp than lò sưởi gia đình", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040924", "hw": "common buttercup", "pos": "phrase", "ipa": "", "vi": "cây mao lương hoa vàng đồng cỏ", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040925", "hw": "conveyance of title", "pos": "phrase", "ipa": "", "vi": "sự chuyển nhượng quyền sở hữu", "cefr": "C1", "tier": "legal", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040926", "hw": "cosmological constant", "pos": "phrase", "ipa": "", "vi": "hằng số vũ trụ học Einstein", "cefr": "C2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040927", "hw": "count palatine", "pos": "phrase", "ipa": "", "vi": "bá tước có đặc quyền hoàng gia", "cefr": "C2", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040928", "hw": "county palatine", "pos": "phrase", "ipa": "", "vi": "hạt bá tước có quyền tài phán", "cefr": "C2", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040929", "hw": "demarcation line", "pos": "phrase", "ipa": "", "vi": "đường ranh giới phân định chia", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040930", "hw": "diffraction grating", "pos": "phrase", "ipa": "", "vi": "cách tử nhiễu xạ tán sắc sáng", "cefr": "C2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040931", "hw": "dinner pail", "pos": "phrase", "ipa": "", "vi": "cặp lồng cơm trưa đựng đồ ăn", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040932", "hw": "eastern cottonwood", "pos": "phrase", "ipa": "", "vi": "cây dương lá rụng miền Đông Mỹ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040933", "hw": "edward gibbon", "pos": "phrase", "ipa": "", "vi": "sử gia Edward Gibbon La Mã", "cefr": "C2", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040934", "hw": "elvis aron presley", "pos": "phrase", "ipa": "", "vi": "vua nhạc rock Elvis Presley", "cefr": "B1", "tier": "music", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040935", "hw": "emissary vein", "pos": "phrase", "ipa": "", "vi": "tĩnh mạch nối thông sọ não", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040936", "hw": "erskine preston caldwell", "pos": "phrase", "ipa": "", "vi": "nhà văn Erskine Caldwell", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040937", "hw": "euclidean space", "pos": "phrase", "ipa": "", "vi": "không gian hình học Euclid", "cefr": "C1", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040938", "hw": "francis crick", "pos": "phrase", "ipa": "", "vi": "nhà sinh học Francis Crick DNA", "cefr": "B2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040939", "hw": "franklin delano roosevelt", "pos": "phrase", "ipa": "", "vi": "tổng thống Franklin D. Roosevelt", "cefr": "B1", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040940", "hw": "gai choi", "pos": "phrase", "ipa": "", "vi": "rau cải bẹ xanh; cải canh cay", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040941", "hw": "garden centipede", "pos": "phrase", "ipa": "", "vi": "con rết nhỏ trong vườn rau", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040942", "hw": "goose pimple", "pos": "phrase", "ipa": "", "vi": "nổi gai ốc; sởn gai ốc da gà", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040943", "hw": "gum kino", "pos": "phrase", "ipa": "", "vi": "nhựa mủ cây gôm kino đỏ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040944", "hw": "heart urchin", "pos": "phrase", "ipa": "", "vi": "nhím biển hình tim dưới đáy cát", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040945", "hw": "hemorrhagic fever", "pos": "phrase", "ipa": "", "vi": "bệnh sốt xuất huyết truyền nhiễm", "cefr": "B2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040946", "hw": "henri matisse", "pos": "phrase", "ipa": "", "vi": "danh họa dã thú Henri Matisse", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040947", "hw": "herbaceous plant", "pos": "phrase", "ipa": "", "vi": "loại thực vật thân thảo mềm", "cefr": "B2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040948", "hw": "herbert blythe", "pos": "phrase", "ipa": "", "vi": "diễn viên Maurice Barrymore", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040949", "hw": "house centipede", "pos": "phrase", "ipa": "", "vi": "con rết nhà chân dài bò nhanh", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040950", "hw": "human paleontology", "pos": "phrase", "ipa": "", "vi": "ngành cổ nhân loại học nghiên cứu", "cefr": "C2", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040951", "hw": "humber bridge", "pos": "phrase", "ipa": "", "vi": "cầu treo Humber nước Anh", "cefr": "B2", "tier": "geography", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040952", "hw": "hunan province", "pos": "phrase", "ipa": "", "vi": "tỉnh Hồ Nam Trung Quốc", "cefr": "B2", "tier": "geography", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040953", "hw": "in the lurch", "pos": "phrase", "ipa": "", "vi": "bị bỏ rơi trong lúc nguy nan", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040954", "hw": "infantile autism", "pos": "phrase", "ipa": "", "vi": "chứng tự kỷ ở trẻ em nhỏ", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040955", "hw": "inhalation anesthetic", "pos": "phrase", "ipa": "", "vi": "thuốc gây mê qua đường hô hấp", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040956", "hw": "inhalation general anesthetic", "pos": "phrase", "ipa": "", "vi": "thuốc mê toàn thân đường thở hít", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040957", "hw": "intravenous anesthetic", "pos": "phrase", "ipa": "", "vi": "thuốc gây mê qua tĩnh mạch", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040958", "hw": "isometric line", "pos": "phrase", "ipa": "", "vi": "đường đẳng tích; đường đẳng trị", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040959", "hw": "johnny reb", "pos": "phrase", "ipa": "", "vi": "lính liên minh miền Nam thời chiến", "cefr": "C2", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040960", "hw": "kino gum", "pos": "phrase", "ipa": "", "vi": "nhựa gôm kino thuộc da nhuộm", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040961", "hw": "laughing hyena", "pos": "phrase", "ipa": "", "vi": "linh cẩu đốm phát tiếng kêu cười", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040962", "hw": "lorenz hart", "pos": "phrase", "ipa": "", "vi": "nhà soạn lời bài hát Lorenz Hart", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040963", "hw": "lounging robe", "pos": "phrase", "ipa": "", "vi": "áo choàng rộng mặc thư giãn nhà", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040964", "hw": "magnetic dipole", "pos": "phrase", "ipa": "", "vi": "lưỡng cực từ trường nam châm", "cefr": "C2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040965", "hw": "magnetic dipole moment", "pos": "phrase", "ipa": "", "vi": "mô-men lưỡng cực từ học", "cefr": "C2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040966", "hw": "malacca cane", "pos": "phrase", "ipa": "", "vi": "gậy ba-toong bằng cây mây Malacca", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040967", "hw": "manna from heaven", "pos": "phrase", "ipa": "", "vi": "món quà trời cho cứu cánh bất ngờ", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040968", "hw": "manna grass", "pos": "phrase", "ipa": "", "vi": "cây cỏ ngọt manna đầm lầy", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040969", "hw": "marlene dietrich", "pos": "phrase", "ipa": "", "vi": "minh tinh Đức Marlene Dietrich", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040970", "hw": "maryland golden aster", "pos": "phrase", "ipa": "", "vi": "hoa cúc sao vàng bang Maryland", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040971", "hw": "matinee idol", "pos": "phrase", "ipa": "", "vi": "nam tài tử thần tượng giới trẻ", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040972", "hw": "mexican husk tomato", "pos": "phrase", "ipa": "", "vi": "cây cà chua bọc vỏ tomatillo", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040973", "hw": "migratory locust", "pos": "phrase", "ipa": "", "vi": "loài cào cào di cư phá hoại", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040974", "hw": "minstrel show", "pos": "phrase", "ipa": "", "vi": "chương trình tạp kỹ bôi mặt đen", "cefr": "C1", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040975", "hw": "mistletoe fig", "pos": "phrase", "ipa": "", "vi": "cây si tầm gửi trồng làm cảnh", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040976", "hw": "mistletoe rubber plant", "pos": "phrase", "ipa": "", "vi": "cây đa tầm gửi lá dày xanh", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040977", "hw": "moray firth", "pos": "phrase", "ipa": "", "vi": "vịnh hẹp Moray Firth Scotland", "cefr": "B2", "tier": "geography", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040978", "hw": "nicaraguan monetary unit", "pos": "phrase", "ipa": "", "vi": "đơn vị tiền tệ của Nicaragua", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040979", "hw": "ooze leather", "pos": "phrase", "ipa": "", "vi": "da bê lộn thuộc mềm mịn", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040980", "hw": "overflow incontinence", "pos": "phrase", "ipa": "", "vi": "tiểu không tự chủ do bàng quang đầy", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040981", "hw": "pair of tongs", "pos": "phrase", "ipa": "", "vi": "cái kẹp lò sưởi; cặp kẹp gắp", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040982", "hw": "pare down", "pos": "phrase", "ipa": "", "vi": "gọt tỉa bớt; cắt giảm quy mô", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040983", "hw": "pet peeve", "pos": "phrase", "ipa": "", "vi": "nỗi bực mình quen thuộc riêng", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040984", "hw": "pleistocene epoch", "pos": "phrase", "ipa": "", "vi": "thế Canh Tân thời kỳ băng hà", "cefr": "C1", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040985", "hw": "preemptive bid", "pos": "phrase", "ipa": "", "vi": "cú ra giá chặn trong bài bridge", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040986", "hw": "prickly custard apple", "pos": "phrase", "ipa": "", "vi": "quả na gai; mãng cầu xiêm chua", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040987", "hw": "public easement", "pos": "phrase", "ipa": "", "vi": "quyền đi lại trên lối công cộng", "cefr": "C2", "tier": "legal", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040988", "hw": "racetrack tout", "pos": "phrase", "ipa": "", "vi": "kẻ bán tin mật ở trường đua ngựa", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040989", "hw": "radium therapy", "pos": "phrase", "ipa": "", "vi": "liệu pháp xạ trị bằng radi", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040990", "hw": "rectal reflex", "pos": "phrase", "ipa": "", "vi": "phản xạ co bóp trực tràng tống phân", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040991", "hw": "reflexive verb", "pos": "phrase", "ipa": "", "vi": "động từ phản thân ngữ pháp", "cefr": "B1", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040992", "hw": "ruffle up", "pos": "phrase", "ipa": "", "vi": "xù lông lên; làm nhăn nhúm áo", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040993", "hw": "sea urchin", "pos": "phrase", "ipa": "", "vi": "nhím biển có gai; con cầu gai", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040994", "hw": "second adventist", "pos": "phrase", "ipa": "", "vi": "tín đồ mong đợi Chúa tái lâm", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040995", "hw": "sex chromatin", "pos": "phrase", "ipa": "", "vi": "chất nhiễm sắc giới tính Barr", "cefr": "C2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040996", "hw": "shamrock pea", "pos": "phrase", "ipa": "", "vi": "cây đậu hoa xanh ba lá shamrock", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040997", "hw": "sir thomas gresham", "pos": "phrase", "ipa": "", "vi": "thương gia Thomas Gresham", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040998", "hw": "sir william huggins", "pos": "phrase", "ipa": "", "vi": "nhà thiên văn William Huggins", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040999", "hw": "street urchin", "pos": "phrase", "ipa": "", "vi": "trẻ em lang thang đường phố", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041000", "hw": "strobe light", "pos": "phrase", "ipa": "", "vi": "đèn chớp sáng nhấp nháy nhịp", "cefr": "B2", "tier": "technology", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041001", "hw": "superlative degree", "pos": "phrase", "ipa": "", "vi": "cấp so sánh cao nhất ngữ pháp", "cefr": "B1", "tier": "academic", "status": "reviewed", "notes": ""}
]

# Validation
ALLOWED_POS = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}
with open('scratch/b29_r02_raw_p5.json', 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

assert len(reviewed_items) == 100, f"Expected 100 items, got {len(reviewed_items)}"
for r, rev in zip(raw_items, reviewed_items):
    assert r["id"] == rev["id"], f"ID mismatch: {r['id']} vs {rev['id']}"
    assert r["hw"] == rev["hw"], f"HW mismatch: {r['hw']} vs {rev['hw']}"
    assert rev["pos"] in ALLOWED_POS, f"Invalid POS for {rev['id']}: {rev['pos']}"
    assert 0 < len(rev["vi"]) <= 35, f"Invalid VI length ({len(rev['vi'])}) for {rev['id']}: {rev['vi']}"
    assert rev["status"] == "reviewed", f"Status must be reviewed: {rev['id']}"
    if " " not in rev["hw"]:
        assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/") and rev["ipa"].count("/") == 2, f"Invalid single-word IPA: {rev['id']}: {rev['ipa']}"

with open('scratch/b29_r02_p5.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 2 Part 5 validated and written successfully. Total items:", len(reviewed_items))
