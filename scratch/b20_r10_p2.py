import json

# Manual QA review for Batch 20 Round 10 Part 2 (099602 to 099701)
part2_data = [
  {"id": "lex.en.100k.099602", "hw": "participially", "pos": "adv", "ipa": "/ˌpɑːrtɪˈsɪpiəli/", "vi": "theo dạng phân từ ngữ pháp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099603", "hw": "particolored", "pos": "adj", "ipa": "/ˈpɑːrtiˌkʌlərd/", "vi": "nhiều màu sắc; lốm đốm màu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099604", "hw": "particoloured", "pos": "adj", "ipa": "/ˈpɑːrtiˌkʌlərd/", "vi": "nhiều màu sắc; lốm đốm màu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099605", "hw": "particularisation", "pos": "noun", "ipa": "/pərˌtɪkjələraɪˈzeɪʃən/", "vi": "sự nêu chi tiết; sự cụ thể hóa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099606", "hw": "particularise", "pos": "verb", "ipa": "/pərˈtɪkjələraɪz/", "vi": "nêu cụ thể; kể rõ từng chi tiết", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099607", "hw": "particularised", "pos": "adj", "ipa": "/pərˈtɪkjələraɪzd/", "vi": "được nêu chi tiết; cụ thể hóa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099608", "hw": "particularises", "pos": "verb", "ipa": "/pərˈtɪkjələraɪzɪz/", "vi": "kể rõ chi tiết; nêu cụ thể", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099609", "hw": "particularising", "pos": "verb", "ipa": "/pərˈtɪkjələraɪzɪŋ/", "vi": "đang nêu rõ từng chi tiết", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099610", "hw": "particularist", "pos": "noun", "ipa": "/pərˈtɪkjələrɪst/", "vi": "người theo chủ nghĩa địa phương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099611", "hw": "particularizer", "pos": "noun", "ipa": "/pərˈtɪkjələraɪzər/", "vi": "người nêu rõ từng chi tiết", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099612", "hw": "particularizes", "pos": "verb", "ipa": "/pərˈtɪkjələraɪzɪz/", "vi": "nêu cụ thể; kể rõ từng chi tiết", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099613", "hw": "particularizing", "pos": "verb", "ipa": "/pərˈtɪkjələraɪzɪŋ/", "vi": "đang nói rõ từng chi tiết", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099614", "hw": "partite", "pos": "adj", "ipa": "/ˈpɑːrtaɪt/", "vi": "chia nhánh sâu; xẻ thùy sâu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099615", "hw": "partitioned", "pos": "verb", "ipa": "/pɑːrˈtɪʃənd/", "vi": "đã ngăn chia; đã chia cắt", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099616", "hw": "partitionist", "pos": "noun", "ipa": "/pɑːrˈtɪʃənɪst/", "vi": "người chủ trương chia cắt lãnh thổ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099617", "hw": "partitions", "pos": "noun", "ipa": "/pɑːrˈtɪʃənz/", "vi": "các vách ngăn; sự chia cắt", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099618", "hw": "partitively", "pos": "adv", "ipa": "/ˈpɑːrtɪtɪvli/", "vi": "theo nghĩa bộ phận; chỉ một phần", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099619", "hw": "partlet", "pos": "noun", "ipa": "/ˈpɑːrtlɪt/", "vi": "yếm che ngực phụ nữ thời xưa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099620", "hw": "partnered", "pos": "verb", "ipa": "/ˈpɑːrtnərd/", "vi": "đã hợp tác; đã kết đôi", "cefr": "B1", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099621", "hw": "partnering", "pos": "noun", "ipa": "/ˈpɑːrtnərɪŋ/", "vi": "sự hợp tác đối tác; sự kết đôi", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099622", "hw": "partners", "pos": "noun", "ipa": "/ˈpɑːrtnərz/", "vi": "các đối tác; các bạn đời", "cefr": "A2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099623", "hw": "partnerships", "pos": "noun", "ipa": "/ˈpɑːrtnərʃɪps/", "vi": "các quan hệ đối tác; sự cộng tác", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099624", "hw": "parton", "pos": "noun", "ipa": "/ˈpɑːrtɑːn/", "vi": "hạt parton (vật lý lượng tử)", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099625", "hw": "partook", "pos": "verb", "ipa": "/pɑːrˈtʊk/", "vi": "đã cùng ăn uống; đã dự phần", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099626", "hw": "partridgeberry", "pos": "noun", "ipa": "/ˈpɑːrtrɪdʒˌbɛri/", "vi": "cây mọng Mitchella repens", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099627", "hw": "partsong", "pos": "noun", "ipa": "/ˈpɑːrtˌsɔːŋ/", "vi": "bài hát nhiều bè", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099628", "hw": "parturiency", "pos": "noun", "ipa": "/pɑːrˈtʊriənsi/", "vi": "giai đoạn cận sinh đẻ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099629", "hw": "parturifacient", "pos": "noun", "ipa": "/ˌpɑːrtjʊrɪˈfeɪʃənt/", "vi": "thuốc trợ sinh; thuốc gây chuyển dạ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099630", "hw": "partway", "pos": "adv", "ipa": "/ˈpɑːrtweɪ/", "vi": "được một đoạn đường; phần nào", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099631", "hw": "partyism", "pos": "noun", "ipa": "/ˈpɑːrtiɪzəm/", "vi": "óc bè phái; lòng trung đảng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099632", "hw": "parulidae", "pos": "noun", "ipa": "/pəˈruːlɪdiː/", "vi": "họ chim chích rừng Parulidae", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099633", "hw": "parvenue", "pos": "noun", "ipa": "/ˈpɑːrvənuː/", "vi": "nữ trọc phú; người mới phất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099634", "hw": "parvenus", "pos": "noun", "ipa": "/ˈpɑːrvənuːz/", "vi": "những kẻ mới phất; giới trọc phú", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099635", "hw": "parvise", "pos": "noun", "ipa": "/ˈpɑːrvɪs/", "vi": "sân trước cổng nhà thờ lớn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099636", "hw": "pase", "pos": "noun", "ipa": "/ˈpɑːseɪ/", "vi": "động tác vung khăn né bò tót", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099637", "hw": "pash", "pos": "noun", "ipa": "/pæʃ/", "vi": "sự say mê cuồng nhiệt; sự phải lòng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099638", "hw": "pashalic", "pos": "noun", "ipa": "/pəˈʃɑːlɪk/", "vi": "khu vực cai quản của pasha", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099639", "hw": "pashm", "pos": "noun", "ipa": "/pʌʃm/", "vi": "lớp lông tơ mịn dê Tây Tạng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099640", "hw": "pasigraphy", "pos": "noun", "ipa": "/pəˈsɪɡrəfi/", "vi": "hệ ký tự chữ viết toàn cầu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099641", "hw": "pasqueflower", "pos": "noun", "ipa": "/ˈpæskˌflaʊər/", "vi": "hoa cúc thảo Phục Sinh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099642", "hw": "pasquinade", "pos": "noun", "ipa": "/ˌpæskwɪˈneɪd/", "vi": "bài văn châm biếm công khai", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099643", "hw": "pasquinader", "pos": "noun", "ipa": "/ˌpæskwɪˈneɪdər/", "vi": "người viết văn thơ châm biếm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099644", "hw": "passableness", "pos": "noun", "ipa": "/ˈpæsəbəlnəs/", "vi": "mức độ tươm tất; có thể chấp nhận", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099645", "hw": "passacaglia", "pos": "noun", "ipa": "/ˌpɑːsəˈkɑːljə/", "vi": "khúc nhạc biến tấu passacaglia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099646", "hw": "passageways", "pos": "noun", "ipa": "/ˈpæsɪdʒweɪz/", "vi": "các lối đi; các hành lang", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099647", "hw": "passamaquody", "pos": "noun", "ipa": "/ˌpæsəməˈkwɑːdi/", "vi": "người bản địa Passamaquoddy", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099648", "hw": "passcode", "pos": "noun", "ipa": "/ˈpæskoʊd/", "vi": "mã xác thực; mật khẩu số", "cefr": "B1", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099649", "hw": "passcodes", "pos": "noun", "ipa": "/ˈpæskoʊdz/", "vi": "các mã xác thực bảo mật", "cefr": "B1", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099650", "hw": "passed", "pos": "verb", "ipa": "/pæst/", "vi": "đã vượt qua; đã thi đỗ; đã qua", "cefr": "A1", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099651", "hw": "passee", "pos": "adj", "ipa": "/pæˈseɪ/", "vi": "tàn phai; lỗi thời; quá thì", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099652", "hw": "passement", "pos": "noun", "ipa": "/ˈpæsmənt/", "vi": "dải đăng ten thêu trang trí", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099653", "hw": "passengers", "pos": "noun", "ipa": "/ˈpæsəndʒərz/", "vi": "các hành khách", "cefr": "A2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099654", "hw": "passeres", "pos": "noun", "ipa": "/ˈpæsəriːz/", "vi": "phân bộ chim sẻ hót", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099655", "hw": "passeridae", "pos": "noun", "ipa": "/pəˈsɛrɪdiː/", "vi": "họ chim sẻ Passeridae", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099656", "hw": "passerina", "pos": "noun", "ipa": "/ˌpæsəˈraɪnə/", "vi": "chi chim sẻ chàm Passerina", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099657", "hw": "passes", "pos": "noun", "ipa": "/ˈpæsɪz/", "vi": "các con đèo; thẻ ra vào; sự chuyền", "cefr": "A2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099658", "hw": "passibility", "pos": "noun", "ipa": "/ˌpæsəˈbɪləti/", "vi": "tính dễ xúc cảm; khả năng cảm thụ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099659", "hw": "passible", "pos": "adj", "ipa": "/ˈpæsəbəl/", "vi": "dễ chịu nỗi đau; dễ cảm thụ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099660", "hw": "passifloraceae", "pos": "noun", "ipa": "/ˌpæsəflɔːˈreɪsiːˌaɪ/", "vi": "họ thực vật Lạc tiên", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099661", "hw": "passimeter", "pos": "noun", "ipa": "/pæˈsɪmɪtər/", "vi": "cổng soát vé quay tự động", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099662", "hw": "passingly", "pos": "adv", "ipa": "/ˈpæsɪŋli/", "vi": "thoáng qua; ngẫu nhiên nhắc tới", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099663", "hw": "passional", "pos": "adj", "ipa": "/ˈpæʃənəl/", "vi": "thuộc tình cảm; do dục vọng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099664", "hw": "passionary", "pos": "noun", "ipa": "/ˈpæʃənɛri/", "vi": "sách kể sự tử đạo của các thánh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099665", "hw": "passionateness", "pos": "noun", "ipa": "/ˈpæʃənɪtnəs/", "vi": "sự sôi nổi; tính nồng nhiệt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099666", "hw": "passioned", "pos": "adj", "ipa": "/ˈpæʃənd/", "vi": "đầy say mê nồng cháy; xúc động", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099667", "hw": "passioning", "pos": "verb", "ipa": "/ˈpæʃənɪŋ/", "vi": "bộc lộ xúc cảm say mê", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099668", "hw": "passionists", "pos": "noun", "ipa": "/ˈpæʃənɪsts/", "vi": "các tu sĩ dòng Thương Khó", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099669", "hw": "passions", "pos": "noun", "ipa": "/ˈpæʃənz/", "vi": "những đam mê nồng nhiệt; xúc cảm", "cefr": "B1", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099670", "hw": "passiontide", "pos": "noun", "ipa": "/ˈpæʃəntaɪd/", "vi": "hai tuần mùa Thương Khó", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099671", "hw": "passivation", "pos": "noun", "ipa": "/ˌpæsɪˈveɪʃən/", "vi": "sự thụ động hóa màng kim loại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099672", "hw": "passivism", "pos": "noun", "ipa": "/ˈpæsɪvɪzəm/", "vi": "chủ nghĩa thụ động; bất kháng cự", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099673", "hw": "passivist", "pos": "noun", "ipa": "/ˈpæsɪvɪst/", "vi": "người theo chủ nghĩa thụ động", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099674", "hw": "passman", "pos": "noun", "ipa": "/ˈpæsmən/", "vi": "sinh viên tốt nghiệp hạng đạt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099675", "hw": "passmark", "pos": "noun", "ipa": "/ˈpæsmɑːrk/", "vi": "điểm đạt chuẩn để đỗ", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099676", "hw": "passphrase", "pos": "noun", "ipa": "/ˈpæsfreɪz/", "vi": "cụm từ mật khẩu", "cefr": "B2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099677", "hw": "passports", "pos": "noun", "ipa": "/ˈpæspɔːrts/", "vi": "các cuốn hộ chiếu", "cefr": "A1", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099678", "hw": "pastelike", "pos": "adj", "ipa": "/ˈpeɪstlaɪk/", "vi": "như hồ nhão; sền sệt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099679", "hw": "pastelist", "pos": "noun", "ipa": "/pæˈstɛlɪst/", "vi": "họa sĩ chuyên vẽ phấn màu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099680", "hw": "pastellist", "pos": "noun", "ipa": "/pæˈstɛlɪst/", "vi": "họa sĩ chuyên vẽ tranh phấn màu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099681", "hw": "pastes", "pos": "verb", "ipa": "/peɪsts/", "vi": "dán; phết hồ dán", "cefr": "A2", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099682", "hw": "pasteurellosis", "pos": "noun", "ipa": "/pæstərɛˈloʊsɪs/", "vi": "bệnh tụ huyết trùng động vật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099683", "hw": "pasteurian", "pos": "adj", "ipa": "/pæˈstɜːriən/", "vi": "thuộc nhà khoa học Pasteur", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099684", "hw": "pasteurise", "pos": "verb", "ipa": "/ˈpæstʃəraɪz/", "vi": "khử trùng Pasteur; thanh trùng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099685", "hw": "pasteurises", "pos": "verb", "ipa": "/ˈpæstʃəraɪzɪz/", "vi": "thanh trùng nhiệt theo Pasteur", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099686", "hw": "pasteurising", "pos": "verb", "ipa": "/ˈpæstʃəraɪzɪŋ/", "vi": "đang thanh trùng Pasteur", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099687", "hw": "pasteurism", "pos": "noun", "ipa": "/ˈpæstʃərɪzəm/", "vi": "phương pháp chủng ngừa Pasteur", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099688", "hw": "pasteurizer", "pos": "noun", "ipa": "/ˈpæstʃəraɪzər/", "vi": "máy khử trùng Pasteur", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099689", "hw": "pasteurizes", "pos": "verb", "ipa": "/ˈpæstʃəraɪzɪz/", "vi": "thanh trùng nhiệt Pasteur", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099690", "hw": "pasteurizing", "pos": "verb", "ipa": "/ˈpæstʃəraɪzɪŋ/", "vi": "đang xử lý thanh trùng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099691", "hw": "pasticco", "pos": "noun", "ipa": "/pæˈstiːtʃoʊ/", "vi": "tác phẩm chắp vá phong cách", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099692", "hw": "pastil", "pos": "noun", "ipa": "/ˈpæstəl/", "vi": "viên kẹo ngậm thơm họng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099693", "hw": "pastinaca", "pos": "noun", "ipa": "/ˌpæstɪˈneɪkə/", "vi": "chi củ cải trắng Pastinaca", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099694", "hw": "pastiness", "pos": "noun", "ipa": "/ˈpeɪstinəs/", "vi": "vẻ mặt xanh xao; độ nhão", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099695", "hw": "pasting", "pos": "noun", "ipa": "/ˈpeɪstɪŋ/", "vi": "trận đòn nhừ tử; sự thất bại đậm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099696", "hw": "pastness", "pos": "noun", "ipa": "/ˈpæstnəs/", "vi": "tính chất dĩ vãng; chuyện đã qua", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099697", "hw": "pastorali", "pos": "noun", "ipa": "/ˌpæstəˈrɑːli/", "vi": "khúc nhạc đồng quê thơ mộng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099698", "hw": "pastoralia", "pos": "noun", "ipa": "/ˌpæstəˈreɪliə/", "vi": "các công việc mục vụ tôn giáo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099699", "hw": "pastoralism", "pos": "noun", "ipa": "/ˈpæstərəlɪzəm/", "vi": "lối sống chăn thả du mục", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099700", "hw": "pastoralist", "pos": "noun", "ipa": "/ˈpæstərəlɪst/", "vi": "người du mục chăn thả gia súc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099701", "hw": "pastoralists", "pos": "noun", "ipa": "/ˈpæstərəlɪsts/", "vi": "những người chăn thả gia súc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Validation
raw_items = json.load(open('scratch/b20_r10_raw_p2.json', 'r', encoding='utf-8'))
assert len(part2_data) == 100
assert len(raw_items) == 100

for i, item in enumerate(part2_data):
    raw = raw_items[i]
    assert item["id"] == raw["id"], f"ID mismatch at {i}: {item['id']} vs {raw['id']}"
    assert item["hw"] == raw["hw"], f"HW mismatch at {i}: {item['hw']} vs {raw['hw']}"
    assert len(item["vi"]) <= 35, f"vi too long at {i} ({item['hw']}): {item['vi']} ({len(item['vi'])} chars)"
    assert item["pos"] in ["noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num"], f"Invalid pos at {i}: {item['pos']}"
    assert item["ipa"].startswith("/") and item["ipa"].endswith("/") and item["ipa"].count("/") == 2, f"Invalid ipa at {i}: {item['ipa']}"
    assert item["status"] == "reviewed"
    item["cefr"] = raw.get("cefr", "C2")
    item["tier"] = raw.get("tier", "expanded")
    item["notes"] = raw.get("notes", "")

with open('scratch/b20_r10_p2.json', 'w', encoding='utf-8') as f:
    json.dump(part2_data, f, ensure_ascii=False, indent=2)

print("b20_r10_p2.json created successfully and validated!")
