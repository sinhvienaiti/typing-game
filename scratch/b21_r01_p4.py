import json

# Manual QA review for Batch 21 Round 1 Part 4 (000302 to 000401)
part4_data = [
  {"id": "lex.en.200k.000302", "hw": "very much like", "pos": "phrase", "ipa": "/ˈvɛri mʌtʃ laɪk/", "vi": "rất giống với; y hệt như", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000303", "hw": "after part", "pos": "phrase", "ipa": "/ˈæftər pɑːrt/", "vi": "phần đuôi tàu thuyền phía sau", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000304", "hw": "come after", "pos": "phrase", "ipa": "/kʌm ˈæftər/", "vi": "theo đuổi; diễn ra sau", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000305", "hw": "come into", "pos": "phrase", "ipa": "/kʌm ˈɪntuː/", "vi": "thừa hưởng gia sản; bước vào", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000306", "hw": "day by day", "pos": "phrase", "ipa": "/deɪ baɪ deɪ/", "vi": "ngày qua ngày; từng ngày một", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000307", "hw": "first state", "pos": "phrase", "ipa": "/fɜːrst steɪt/", "vi": "tiểu bang Delaware (Mỹ)", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000308", "hw": "for each one", "pos": "phrase", "ipa": "/fɔːr iːtʃ wʌn/", "vi": "dành cho từng người một", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000309", "hw": "for free", "pos": "phrase", "ipa": "/fɔːr friː/", "vi": "miễn phí; không tính tiền", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000310", "hw": "go home", "pos": "phrase", "ipa": "/ɡoʊ hoʊm/", "vi": "đi về nhà; đánh trúng trọng tâm", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000311", "hw": "look back", "pos": "phrase", "ipa": "/lʊk bæk/", "vi": "nhìn lại quá khứ; ngoái nhìn", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000312", "hw": "the city", "pos": "phrase", "ipa": "/ðə ˈsɪti/", "vi": "trung tâm tài chính Luân Đôn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000313", "hw": "work through", "pos": "phrase", "ipa": "/wɜːrk θruː/", "vi": "giải quyết lần lượt từng việc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000314", "hw": "come over", "pos": "phrase", "ipa": "/kʌm ˈoʊvər/", "vi": "ghé chơi nhà; bất chợt xâm chiếm", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000315", "hw": "end up", "pos": "phrase", "ipa": "/ɛnd ʌp/", "vi": "rốt cuộc trở thành; kết cục là", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000316", "hw": "ever so", "pos": "phrase", "ipa": "/ˈɛvər soʊ/", "vi": "vô cùng; hết sức là", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000317", "hw": "feel like", "pos": "phrase", "ipa": "/fiːl laɪk/", "vi": "muốn làm gì; cảm giác như là", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000318", "hw": "in name", "pos": "phrase", "ipa": "/ɪn neɪm/", "vi": "trên danh nghĩa; chỉ có tiếng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000319", "hw": "last day", "pos": "phrase", "ipa": "/læst deɪ/", "vi": "ngày phán xét cuối cùng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000320", "hw": "no end", "pos": "phrase", "ipa": "/noʊ ɛnd/", "vi": "vô cùng nhiều; khôn xiết", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000321", "hw": "show up", "pos": "phrase", "ipa": "/ʃoʊ ʌp/", "vi": "xuất hiện; lộ diện; vạch trần", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000322", "hw": "still life", "pos": "phrase", "ipa": "/stɪl laɪf/", "vi": "tranh vẽ tĩnh vật", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000323", "hw": "take down", "pos": "phrase", "ipa": "/teɪk daʊn/", "vi": "tháo dỡ; ghi chép lại; hạ gục", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000324", "hw": "come back", "pos": "phrase", "ipa": "/kʌm bæk/", "vi": "quay trở lại; phản hồi", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000325", "hw": "feel out", "pos": "phrase", "ipa": "/fiːl aʊt/", "vi": "thăm dò ý kiến kín đáo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000326", "hw": "keep up", "pos": "phrase", "ipa": "/kiːp ʌp/", "vi": "theo kịp tiến độ; duy trì", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000327", "hw": "let in", "pos": "phrase", "ipa": "/lɛt ɪn/", "vi": "cho vào trong; thấm nước", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000328", "hw": "put up", "pos": "phrase", "ipa": "/pʊt ʌp/", "vi": "dựng lên; cho ở nhờ; tăng giá", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000329", "hw": "team up", "pos": "phrase", "ipa": "/tiːm ʌp/", "vi": "hợp tác chung nhóm; kết hợp", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000330", "hw": "time and again", "pos": "phrase", "ipa": "/taɪm ænd əˈɡɛn/", "vi": "hết lần này đến lần khác", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000331", "hw": "against time", "pos": "phrase", "ipa": "/əˈɡɛnst taɪm/", "vi": "chạy đua với thời gian", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000332", "hw": "big time", "pos": "phrase", "ipa": "/bɪɡ taɪm/", "vi": "đỉnh cao danh vọng; thời hoàng kim", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000333", "hw": "from each one", "pos": "phrase", "ipa": "/frʌm iːtʃ wʌn/", "vi": "từ mỗi người; từ mỗi cái", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000334", "hw": "go around", "pos": "phrase", "ipa": "/ɡoʊ əˈraʊnd/", "vi": "đủ chia mọi người; đi vòng quanh", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000335", "hw": "keep out", "pos": "phrase", "ipa": "/kiːp aʊt/", "vi": "không cho vào; cấm vào", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000336", "hw": "let on", "pos": "phrase", "ipa": "/lɛt ɑːn/", "vi": "tiết lộ bí mật; vờ như", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000337", "hw": "put out", "pos": "phrase", "ipa": "/pʊt aʊt/", "vi": "dập tắt lửa; gây phiền toái", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000338", "hw": "set in", "pos": "phrase", "ipa": "/sɛt ɪn/", "vi": "bắt đầu ập đến (thời tiết)", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000339", "hw": "show time", "pos": "phrase", "ipa": "/ʃoʊ taɪm/", "vi": "giờ bắt đầu biểu diễn; giờ chiếu", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000340", "hw": "this night", "pos": "phrase", "ipa": "/ðɪs naɪt/", "vi": "đêm nay; tối hôm nay", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000341", "hw": "every year", "pos": "phrase", "ipa": "/ˈɛvri jɪər/", "vi": "mỗi năm; thường niên", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000342", "hw": "free will", "pos": "phrase", "ipa": "/friː wɪl/", "vi": "ý chí tự do; tự nguyện", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000343", "hw": "have it away", "pos": "phrase", "ipa": "/hæv ɪt əˈweɪ/", "vi": "quan hệ tình dục", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000344", "hw": "now and again", "pos": "phrase", "ipa": "/naʊ ænd əˈɡɛn/", "vi": "thỉnh thoảng; đôi lúc", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000345", "hw": "set on", "pos": "phrase", "ipa": "/sɛt ɑːn/", "vi": "xúi giục tấn công; quyết tâm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000346", "hw": "before long", "pos": "phrase", "ipa": "/bɪˈfɔːr lɔːŋ/", "vi": "chẳng bao lâu nữa; sớm thôi", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000347", "hw": "done for", "pos": "phrase", "ipa": "/dʌn fɔːr/", "vi": "tiêu đời; kiệt sức hoàn toàn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000348", "hw": "done with", "pos": "phrase", "ipa": "/dʌn wɪð/", "vi": "dứt điểm; không còn dính dáng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000349", "hw": "in public", "pos": "phrase", "ipa": "/ɪn ˈpʌblɪk/", "vi": "ở nơi công cộng; công khai", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000350", "hw": "looking for", "pos": "phrase", "ipa": "/ˈlʊkɪŋ fɔːr/", "vi": "việc tìm kiếm; đang tìm", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000351", "hw": "number one", "pos": "phrase", "ipa": "/ˈnʌmbər wʌn/", "vi": "số một; hạng nhất; bản thân mình", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000352", "hw": "take home", "pos": "phrase", "ipa": "/teɪk hoʊm/", "vi": "mang về nhà; kiếm được thực nhận", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000353", "hw": "through and through", "pos": "phrase", "ipa": "/θruː ænd θruː/", "vi": "hoàn toàn; từ đầu đến chân", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000354", "hw": "care for", "pos": "phrase", "ipa": "/kɛr fɔːr/", "vi": "chăm sóc; ưa thích điều gì", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000355", "hw": "come before", "pos": "phrase", "ipa": "/kʌm bɪˈfɔːr/", "vi": "đứng trước; ưu tiên hơn; hầu tòa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000356", "hw": "come off", "pos": "phrase", "ipa": "/kʌm ɔːf/", "vi": "bong ra; thành công; ngã xe", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000357", "hw": "go game", "pos": "phrase", "ipa": "/ɡoʊ ɡeɪm/", "vi": "môn cờ vây", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000358", "hw": "go under", "pos": "phrase", "ipa": "/ɡoʊ ˈʌndər/", "vi": "chìm đắm; phá sản vỡ nợ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000359", "hw": "look out over", "pos": "phrase", "ipa": "/lʊk aʊt ˈoʊvər/", "vi": "hướng tầm nhìn bao quát ra", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000360", "hw": "love life", "pos": "phrase", "ipa": "/lʌv laɪf/", "vi": "đời sống tình cảm lứa đôi", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000361", "hw": "over again", "pos": "phrase", "ipa": "/ˈoʊvər əˈɡɛn/", "vi": "làm lại một lần nữa", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000362", "hw": "then again", "pos": "phrase", "ipa": "/ðɛn əˈɡɛn/", "vi": "nhưng mặt khác; vả lại", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000363", "hw": "under way", "pos": "phrase", "ipa": "/ˈʌndər weɪ/", "vi": "đang được tiến hành; khởi hành", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000364", "hw": "better off", "pos": "phrase", "ipa": "/ˈbɛtər ɔːf/", "vi": "khá giả hơn; thuận lợi hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000365", "hw": "first team", "pos": "phrase", "ipa": "/fɜːrst tiːm/", "vi": "đội hình chính thức thi đấu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000366", "hw": "for anything", "pos": "phrase", "ipa": "/fɔːr ˈɛniθɪŋ/", "vi": "trong bất cứ hoàn cảnh nào", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000367", "hw": "free people", "pos": "phrase", "ipa": "/friː ˈpiːpəl/", "vi": "những con người tự do", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000368", "hw": "free time", "pos": "phrase", "ipa": "/friː taɪm/", "vi": "thời gian rảnh rỗi", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000369", "hw": "give back", "pos": "phrase", "ipa": "/ɡɪv bæk/", "vi": "trả lại; đóng góp cho xã hội", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000370", "hw": "in case", "pos": "phrase", "ipa": "/ɪn keɪs/", "vi": "phòng khi; lỡ như", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000371", "hw": "in person", "pos": "phrase", "ipa": "/ɪn ˈpɜːrsn/", "vi": "đích thân; gặp trực tiếp", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000372", "hw": "let up", "pos": "phrase", "ipa": "/lɛt ʌp/", "vi": "dịu đi; ngớt mưa; giảm cường độ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000373", "hw": "looking at", "pos": "phrase", "ipa": "/ˈlʊkɪŋ æt/", "vi": "hành động nhìn ngắm; xem xét", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000374", "hw": "out and away", "pos": "phrase", "ipa": "/aʊt ænd əˈweɪ/", "vi": "vượt trội hơn hẳn; bỏ xa", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000375", "hw": "out of play", "pos": "phrase", "ipa": "/aʊt əv pleɪ/", "vi": "bóng ra ngoài sân; ngoài cuộc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000376", "hw": "play out", "pos": "phrase", "ipa": "/pleɪ aʊt/", "vi": "diễn tiến; làm cạn kiệt tài lực", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000377", "hw": "play up", "pos": "phrase", "ipa": "/pleɪ ʌp/", "vi": "làm nổi bật; giở chứng quấy rầy", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000378", "hw": "take part", "pos": "phrase", "ipa": "/teɪk pɑːrt/", "vi": "tham gia; góp mặt vào", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000379", "hw": "take time off", "pos": "phrase", "ipa": "/teɪk taɪm ɔːf/", "vi": "nghỉ phép; tạm dừng công việc", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000380", "hw": "us house", "pos": "phrase", "ipa": "/juː ɛs haʊs/", "vi": "Hạ viện Hoa Kỳ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000381", "hw": "all day long", "pos": "phrase", "ipa": "/ɔːl deɪ lɔːŋ/", "vi": "suốt cả ngày; cả ngày dài", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000382", "hw": "at times", "pos": "phrase", "ipa": "/æt taɪmz/", "vi": "đôi khi; có những lúc", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000383", "hw": "best man", "pos": "phrase", "ipa": "/bɛst mæn/", "vi": "phù rể chính", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000384", "hw": "come down", "pos": "phrase", "ipa": "/kʌm daʊn/", "vi": "đi xuống; giảm giá; hạ cánh", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000385", "hw": "come to life", "pos": "phrase", "ipa": "/kʌm tuː laɪf/", "vi": "trở nên sống động; hồi sinh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000386", "hw": "do away with", "pos": "phrase", "ipa": "/duː əˈweɪ wɪð/", "vi": "bãi bỏ; thủ tiêu loại bỏ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000387", "hw": "get away", "pos": "phrase", "ipa": "/ɡɛt əˈweɪ/", "vi": "trốn thoát; đi nghỉ ngơi", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000388", "hw": "give way", "pos": "phrase", "ipa": "/ɡɪv weɪ/", "vi": "nhường đường; gãy sụp; khuất phục", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000389", "hw": "in full", "pos": "phrase", "ipa": "/ɪn fʊl/", "vi": "toàn bộ; đầy đủ không thiếu", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000390", "hw": "let out", "pos": "phrase", "ipa": "/lɛt aʊt/", "vi": "buông lời; thả ra; nới rộng áo", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000391", "hw": "live in", "pos": "phrase", "ipa": "/lɪv ɪn/", "vi": "ở nội trú tại chỗ làm việc", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000392", "hw": "make sure", "pos": "phrase", "ipa": "/meɪk ʃʊr/", "vi": "đảm bảo chắc chắn; kiểm tra kỹ", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000393", "hw": "one after another", "pos": "phrase", "ipa": "/wʌn ˈæftər əˈnʌðər/", "vi": "hết người này đến người khác", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000394", "hw": "set about", "pos": "phrase", "ipa": "/sɛt əˈbaʊt/", "vi": "bắt tay vào khởi sự làm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000395", "hw": "set out", "pos": "phrase", "ipa": "/sɛt aʊt/", "vi": "khởi hành; đặt ra mục tiêu", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000396", "hw": "set up", "pos": "phrase", "ipa": "/sɛt ʌp/", "vi": "thiết lập; thành lập; cài đặt", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000397", "hw": "to the full", "pos": "phrase", "ipa": "/tuː ðə fʊl/", "vi": "đầy đủ hết mức; trọn vẹn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000398", "hw": "gets", "pos": "noun", "ipa": "/ɡɛts/", "vi": "các cú cứu bóng khó; đàn con", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000399", "hw": "back end", "pos": "phrase", "ipa": "/bæk ɛnd/", "vi": "phần phụ trợ máy chủ; đuôi sau", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000400", "hw": "be full", "pos": "phrase", "ipa": "/biː fʊl/", "vi": "no bụng; đầy ắp tràn ngập", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000401", "hw": "come through", "pos": "phrase", "ipa": "/kʌm θruː/", "vi": "vượt qua hoạn nạn; hoàn thành tốt", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Validation
raw_items = json.load(open('scratch/b21_r01_raw_p4.json', 'r', encoding='utf-8'))
assert len(part4_data) == 100
assert len(raw_items) == 100

for i, item in enumerate(part4_data):
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

with open('scratch/b21_r01_p4.json', 'w', encoding='utf-8') as f:
    json.dump(part4_data, f, ensure_ascii=False, indent=2)

print("b21_r01_p4.json created successfully and validated!")
