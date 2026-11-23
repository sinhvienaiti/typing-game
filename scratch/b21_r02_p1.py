import json

# Manual QA review for Batch 21 Round 2 Part 1 (000502 to 000601)
part1_data = [
  {"id": "lex.en.200k.000502", "hw": "set back", "pos": "phrase", "ipa": "/sɛt bæk/", "vi": "lùi lại; làm chậm trễ; tốn kém", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000503", "hw": "so far", "pos": "phrase", "ipa": "/soʊ fɑːr/", "vi": "cho đến nay; tới mức đó", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000504", "hw": "call out", "pos": "phrase", "ipa": "/kɔːl aʊt/", "vi": "kêu to; gọi đích danh; điều động", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000505", "hw": "come into being", "pos": "phrase", "ipa": "/kʌm ˈɪntuː ˈbiːɪŋ/", "vi": "ra đời; được hình thành", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000506", "hw": "going away", "pos": "phrase", "ipa": "/ˈɡoʊɪŋ əˈweɪ/", "vi": "sự ra đi; sự khởi hành đi xa", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000507", "hw": "good person", "pos": "phrase", "ipa": "/ɡʊd ˈpɜːrsn/", "vi": "người tốt bụng; người tử tế", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000508", "hw": "in so far", "pos": "phrase", "ipa": "/ɪn soʊ fɑːr/", "vi": "trong chừng mực mà; đến mức mà", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000509", "hw": "keep down", "pos": "phrase", "ipa": "/kiːp daʊn/", "vi": "kìm hãm; đè nén; nuốt trôi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000510", "hw": "kind of", "pos": "phrase", "ipa": "/kaɪnd əv/", "vi": "hơi hơi; kiểu như; loại hình", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000511", "hw": "let it go", "pos": "phrase", "ipa": "/lɛt ɪt ɡoʊ/", "vi": "bỏ qua đi; không bận tâm nữa", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000512", "hw": "name day", "pos": "phrase", "ipa": "/neɪm deɪ/", "vi": "ngày lễ thánh bổn mạng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000513", "hw": "put down", "pos": "phrase", "ipa": "/pʊt daʊn/", "vi": "đặt xuống; dẹp tan; chê bai", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000514", "hw": "put through", "pos": "phrase", "ipa": "/pʊt θruː/", "vi": "chuyển máy điện thoại; hoàn tất", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000515", "hw": "try out", "pos": "phrase", "ipa": "/traɪ aʊt/", "vi": "thử nghiệm; thi tuyển thử sức", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000516", "hw": "trying on", "pos": "phrase", "ipa": "/ˈtraɪɪŋ ɑːn/", "vi": "việc mặc thử đồ; ướm thử", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000517", "hw": "two times", "pos": "phrase", "ipa": "/tuː taɪmz/", "vi": "hai lần; gấp đôi", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000518", "hw": "white out", "pos": "phrase", "ipa": "/waɪt aʊt/", "vi": "bão tuyết mù mịt; bôi bút xóa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000519", "hw": "end man", "pos": "phrase", "ipa": "/ɛnd mæn/", "vi": "diễn viên hài ngồi mép hàng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000520", "hw": "first person", "pos": "phrase", "ipa": "/fɜːrst ˈpɜːrsn/", "vi": "ngôi thứ nhất (ngữ pháp)", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000521", "hw": "free world", "pos": "phrase", "ipa": "/friː wɜːrld/", "vi": "thế giới tự do phi cộng sản", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000522", "hw": "good enough", "pos": "phrase", "ipa": "/ɡʊd ɪˈnʌf/", "vi": "đủ tốt; tạm ổn thỏa", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000523", "hw": "in kind", "pos": "phrase", "ipa": "/ɪn kaɪnd/", "vi": "bằng hiện vật; trả đũa y hệt", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000524", "hw": "know nothing", "pos": "phrase", "ipa": "/noʊ ˈnʌθɪŋ/", "vi": "kẻ dốt đặc; người không biết gì", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000525", "hw": "line up", "pos": "phrase", "ipa": "/laɪn ʌp/", "vi": "xếp hàng ngũ; sắp xếp dàn dựng", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000526", "hw": "on the whole", "pos": "phrase", "ipa": "/ɑːn ðə hoʊl/", "vi": "nhìn chung; tóm lại tổng thể", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000527", "hw": "people in power", "pos": "phrase", "ipa": "/ˈpiːpəl ɪn ˈpaʊər/", "vi": "những người nắm giữ quyền lực", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000528", "hw": "play off", "pos": "phrase", "ipa": "/pleɪ ɔːf/", "vi": "khích bác đối đầu; trận đấu phụ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000529", "hw": "point after", "pos": "phrase", "ipa": "/pɔɪnt ˈæftər/", "vi": "cú đá cộng điểm sau touchdown", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000530", "hw": "run out", "pos": "phrase", "ipa": "/rʌn aʊt/", "vi": "cạn kiệt hết sạch; hết hạn", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000531", "hw": "run up", "pos": "phrase", "ipa": "/rʌn ʌp/", "vi": "chồng chất nợ nần; kéo cờ lên", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000532", "hw": "take away", "pos": "phrase", "ipa": "/teɪk əˈweɪ/", "vi": "mang đi; loại bỏ; bài học rút ra", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000533", "hw": "together with", "pos": "phrase", "ipa": "/təˈɡɛðər wɪð/", "vi": "cùng với; đồng hành bên cạnh", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000534", "hw": "two year old", "pos": "phrase", "ipa": "/tuː jɪər oʊld/", "vi": "ngựa hai tuổi; đứa bé hai tuổi", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000535", "hw": "us government", "pos": "phrase", "ipa": "/juː ɛs ˈɡʌvənmənt/", "vi": "chính phủ Hợp chúng quốc Hoa Kỳ", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000536", "hw": "change over", "pos": "phrase", "ipa": "/tʃeɪndʒ ˈoʊvər/", "vi": "sự chuyển đổi; đổi phiên đổi ca", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000537", "hw": "family man", "pos": "phrase", "ipa": "/ˈfæməli mæn/", "vi": "người đàn ông vì gia đình", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000538", "hw": "getting even", "pos": "phrase", "ipa": "/ˈɡɛtɪŋ ˈiːvən/", "vi": "hành vi trả thù trả đũa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000539", "hw": "high school", "pos": "phrase", "ipa": "/haɪ skuːl/", "vi": "trường trung học phổ thông", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000540", "hw": "in any case", "pos": "phrase", "ipa": "/ɪn ˈɛni keɪs/", "vi": "dù trong trường hợp nào; dù sao", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000541", "hw": "in the least", "pos": "phrase", "ipa": "/ɪn ðə liːst/", "vi": "chút nào; dẫu chỉ một chút", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000542", "hw": "let off", "pos": "phrase", "ipa": "/lɛt ɔːf/", "vi": "tha tội; không phạt; nổ súng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000543", "hw": "live over", "pos": "phrase", "ipa": "/lɪv ˈoʊvər/", "vi": "sống lại ký ức; trải nghiệm lại", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000544", "hw": "make full", "pos": "phrase", "ipa": "/meɪk fʊl/", "vi": "làm cho đầy; bù đủ số lượng", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000545", "hw": "night life", "pos": "phrase", "ipa": "/naɪt laɪf/", "vi": "nhịp sống giải trí về đêm", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000546", "hw": "of course", "pos": "phrase", "ipa": "/əv kɔːrs/", "vi": "dĩ nhiên; tất nhiên rồi", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000547", "hw": "old school", "pos": "phrase", "ipa": "/oʊld skuːl/", "vi": "trường phái cổ điển; lối xưa cũ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000548", "hw": "open up", "pos": "phrase", "ipa": "/ˈoʊpən ʌp/", "vi": "mở lòng chia sẻ; khai trương", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000549", "hw": "set off", "pos": "phrase", "ipa": "/sɛt ɔːf/", "vi": "khởi hành; kích nổ; làm tôn lên", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000550", "hw": "all together", "pos": "phrase", "ipa": "/ɔːl təˈɡɛðər/", "vi": "cùng nhau; đồng loạt cùng lúc", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000551", "hw": "at least", "pos": "phrase", "ipa": "/æt liːst/", "vi": "ít nhất; tối thiểu là", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000552", "hw": "early on", "pos": "phrase", "ipa": "/ˈɜːrli ɑːn/", "vi": "ngay từ giai đoạn đầu", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000553", "hw": "first water", "pos": "phrase", "ipa": "/fɜːrst ˈwɔːtər/", "vi": "ngọc nước nhất phẩm chất lượng cao", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000554", "hw": "last name", "pos": "phrase", "ipa": "/læst neɪm/", "vi": "họ gia đình", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000555", "hw": "let down", "pos": "phrase", "ipa": "/lɛt daʊn/", "vi": "làm thất vọng; hạ thấp xuống", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000556", "hw": "little by little", "pos": "phrase", "ipa": "/ˈlɪtl baɪ ˈlɪtl/", "vi": "từng li từng tí; dần dần", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000557", "hw": "new line", "pos": "phrase", "ipa": "/nuː laɪn/", "vi": "ký tự xuống dòng mới", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000558", "hw": "play down", "pos": "phrase", "ipa": "/pleɪ daʊn/", "vi": "nói giảm nhẹ tầm quan trọng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000559", "hw": "real life", "pos": "phrase", "ipa": "/riːl laɪf/", "vi": "đời sống thực tế hàng ngày", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000560", "hw": "real world", "pos": "phrase", "ipa": "/riːl wɜːrld/", "vi": "thế giới hiện thực", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000561", "hw": "second best", "pos": "phrase", "ipa": "/ˈsɛkənd bɛst/", "vi": "đứng thứ nhì; phương án thứ hai", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000562", "hw": "using up", "pos": "phrase", "ipa": "/ˈjuːzɪŋ ʌp/", "vi": "việc tiêu dùng cạn kiệt", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000563", "hw": "well point", "pos": "phrase", "ipa": "/wɛl pɔɪnt/", "vi": "mũi giếng kim hút nước ngầm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000564", "hw": "while away", "pos": "phrase", "ipa": "/waɪl əˈweɪ/", "vi": "giết thời gian nhàn rỗi", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000565", "hw": "at the least", "pos": "phrase", "ipa": "/æt ðə liːst/", "vi": "tối thiểu là; ít nhất", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000566", "hw": "black out", "pos": "phrase", "ipa": "/blæk aʊt/", "vi": "mất điện toàn bộ; ngất xỉu", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000567", "hw": "country people", "pos": "phrase", "ipa": "/ˈkʌntri ˈpiːpəl/", "vi": "người dân quê; người nông thôn", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000568", "hw": "day care", "pos": "phrase", "ipa": "/deɪ kɛr/", "vi": "nhà trẻ; dịch vụ giữ trẻ ngày", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000569", "hw": "free love", "pos": "phrase", "ipa": "/friː lʌv/", "vi": "tình yêu tự do phóng khoáng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000570", "hw": "go bad", "pos": "phrase", "ipa": "/ɡoʊ bæd/", "vi": "bị ôi thiu; hỏng hóc thoái hóa", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000571", "hw": "have young", "pos": "phrase", "ipa": "/hæv jʌŋ/", "vi": "sinh con non; đẻ con", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000572", "hw": "make believe", "pos": "phrase", "ipa": "/meɪk bɪˈliːv/", "vi": "giả vờ đóng vai; tưởng tượng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000573", "hw": "make water", "pos": "phrase", "ipa": "/meɪk ˈwɔːtər/", "vi": "đi tiểu tiện; rò rỉ nước vào tàu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000574", "hw": "point the way", "pos": "phrase", "ipa": "/pɔɪnt ðə weɪ/", "vi": "chỉ đường dẫn lối; định hướng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000575", "hw": "set down", "pos": "phrase", "ipa": "/sɛt daʊn/", "vi": "ghi chép lại; đặt xuống đất", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000576", "hw": "stop over", "pos": "phrase", "ipa": "/stɑːp ˈoʊvər/", "vi": "nghỉ quá cảnh giữa chuyến bay", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000577", "hw": "talk of", "pos": "phrase", "ipa": "/tɔːk əv/", "vi": "nói về; bàn tán về tin đồn", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000578", "hw": "top off", "pos": "phrase", "ipa": "/tɑːp ɔːf/", "vi": "đổ đầy bình; hoàn tất mỹ mãn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000579", "hw": "well thought out", "pos": "phrase", "ipa": "/wɛl θɔːt aʊt/", "vi": "được toan tính suy xét thấu đáo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000580", "hw": "all important", "pos": "phrase", "ipa": "/ɔːl ɪmˈpɔːrtnt/", "vi": "tối quan trọng; thiết yếu nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000581", "hw": "call back", "pos": "phrase", "ipa": "/kɔːl bæk/", "vi": "gọi lại điện thoại; triệu hồi", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000582", "hw": "city man", "pos": "phrase", "ipa": "/ˈsɪti mæn/", "vi": "chuyên gia tài chính Luân Đôn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000583", "hw": "end game", "pos": "phrase", "ipa": "/ɛnd ɡeɪm/", "vi": "giai đoạn tàn cuộc cờ; hồi kết", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000584", "hw": "face up", "pos": "phrase", "ipa": "/feɪs ʌp/", "vi": "lật ngửa mặt bài; ngửa mặt lên", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000585", "hw": "free state", "pos": "phrase", "ipa": "/friː steɪt/", "vi": "tỉnh Free State (Nam Phi)", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000586", "hw": "game show", "pos": "phrase", "ipa": "/ɡeɪm ʃoʊ/", "vi": "chương trình trò chơi truyền hình", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000587", "hw": "get together", "pos": "phrase", "ipa": "/ɡɛt təˈɡɛðər/", "vi": "buổi tụ họp gặp mặt; họp bàn", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000588", "hw": "in fact", "pos": "phrase", "ipa": "/ɪn fækt/", "vi": "trên thực tế; thật ra là", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000589", "hw": "in hand", "pos": "phrase", "ipa": "/ɪn hænd/", "vi": "nắm trong tầm tay; sẵn có", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000590", "hw": "least of all", "pos": "phrase", "ipa": "/liːst əv ɔːl/", "vi": "ít nhất; tuyệt nhiên không", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000591", "hw": "look away", "pos": "phrase", "ipa": "/lʊk əˈweɪ/", "vi": "ngoảnh mặt đi; quay đi chỗ khác", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000592", "hw": "more or less", "pos": "phrase", "ipa": "/mɔːr ɔːr lɛs/", "vi": "xấp xỉ khoảng chừng; gần như", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000593", "hw": "on hand", "pos": "phrase", "ipa": "/ɑːn hænd/", "vi": "sẵn có để dùng; có mặt ngay", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000594", "hw": "run into", "pos": "phrase", "ipa": "/rʌn ˈɪntuː/", "vi": "tình cờ bắt gặp; đâm sầm vào", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000595", "hw": "take care", "pos": "phrase", "ipa": "/teɪk kɛr/", "vi": "chăm sóc; cẩn thận bảo trọng", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000596", "hw": "the true", "pos": "phrase", "ipa": "/ðə truː/", "vi": "chân lý; cái đúng đắn chân thật", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000597", "hw": "true to", "pos": "phrase", "ipa": "/truː tuː/", "vi": "trung thành với; đúng bản chất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000598", "hw": "water back", "pos": "phrase", "ipa": "/ˈwɔːtər bæk/", "vi": "bình đun nước nối sau bếp lò", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000599", "hw": "well water", "pos": "phrase", "ipa": "/wɛl ˈwɔːtər/", "vi": "nước giếng khơi đào", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000600", "hw": "working out", "pos": "phrase", "ipa": "/ˈwɜːrkɪŋ aʊt/", "vi": "việc tính toán chi tiết; tập gym", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000601", "hw": "again and again", "pos": "phrase", "ipa": "/əˈɡɛn ænd əˈɡɛn/", "vi": "lặp đi lặp lại nhiều lần", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Validation
raw_items = json.load(open('scratch/b21_r02_raw_p1.json', 'r', encoding='utf-8'))
assert len(part1_data) == 100
assert len(raw_items) == 100

for i, item in enumerate(part1_data):
    raw = raw_items[i]
    assert item["id"] == raw["id"], f"ID mismatch at {i}: {item['id']} vs {raw['id']}"
    assert item["hw"] == raw["hw"], f"HW mismatch at {i}: {item['hw']} vs {raw['hw']}"
    assert len(item["vi"]) <= 35, f"vi too long at {i} ({item['hw']}): {item['vi']} ({len(item['vi'])} chars)"
    assert item["pos"] in ["noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"], f"Invalid pos at {i}: {item['pos']}"
    assert item["ipa"].startswith("/") and item["ipa"].endswith("/") and item["ipa"].count("/") == 2, f"Invalid ipa at {i}: {item['ipa']}"
    assert item["status"] == "reviewed"
    item["cefr"] = raw.get("cefr", "C2")
    item["tier"] = raw.get("tier", "expanded")
    item["notes"] = raw.get("notes", "")

with open('scratch/b21_r02_p1.json', 'w', encoding='utf-8') as f:
    json.dump(part1_data, f, ensure_ascii=False, indent=2)

print("b21_r02_p1.json created successfully and validated!")
