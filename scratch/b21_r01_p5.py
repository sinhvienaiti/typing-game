import json

# Manual QA review for Batch 21 Round 1 Part 5 (000402 to 000501)
part5_data = [
  {"id": "lex.en.200k.000402", "hw": "day after day", "pos": "phrase", "ipa": "/deɪ ˈæftər deɪ/", "vi": "ngày này qua ngày khác", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000403", "hw": "day game", "pos": "phrase", "ipa": "/deɪ ɡeɪm/", "vi": "trận đấu bóng ban ngày", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000404", "hw": "every last", "pos": "phrase", "ipa": "/ˈɛvri læst/", "vi": "tất cả mọi; không sót một ai", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000405", "hw": "go against", "pos": "phrase", "ipa": "/ɡoʊ əˈɡɛnst/", "vi": "chống lại; đi ngược quy định", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000406", "hw": "going under", "pos": "phrase", "ipa": "/ˈɡoʊɪŋ ˈʌndər/", "vi": "sự phá sản; sự chìm tàu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000407", "hw": "live on", "pos": "phrase", "ipa": "/lɪv ɑːn/", "vi": "sống dựa vào; sống mãi", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000408", "hw": "live with", "pos": "phrase", "ipa": "/lɪv wɪð/", "vi": "chấp nhận sống chung với", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000409", "hw": "look down on", "pos": "phrase", "ipa": "/lʊk daʊn ɑːn/", "vi": "coi thường; khinh rẻ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000410", "hw": "many another", "pos": "phrase", "ipa": "/ˈmɛni əˈnʌðər/", "vi": "biết bao nhiêu kẻ khác", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000411", "hw": "put over", "pos": "phrase", "ipa": "/pʊt ˈoʊvər/", "vi": "truyền đạt thành công ý tưởng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000412", "hw": "real time", "pos": "phrase", "ipa": "/riːl taɪm/", "vi": "thời gian thực", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000413", "hw": "school year", "pos": "phrase", "ipa": "/skuːl jɪər/", "vi": "năm học; niên khóa", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000414", "hw": "the states", "pos": "phrase", "ipa": "/ðə steɪts/", "vi": "nước Mỹ; Hợp chủng quốc Hoa Kỳ", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000415", "hw": "as yet", "pos": "phrase", "ipa": "/æz jɛt/", "vi": "cho đến nay; tính tới lúc này", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000416", "hw": "at long last", "pos": "phrase", "ipa": "/æt lɔːŋ læst/", "vi": "sau bao chờ đợi; rốt cuộc thì", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000417", "hw": "day school", "pos": "phrase", "ipa": "/deɪ skuːl/", "vi": "trường học bán trú ngày", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000418", "hw": "every which way", "pos": "phrase", "ipa": "/ˈɛvri wɪtʃ weɪ/", "vi": "khắp tứ phương tám hướng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000419", "hw": "give off", "pos": "phrase", "ipa": "/ɡɪv ɔːf/", "vi": "tỏa ra mùi hương; phát ra khí", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000420", "hw": "high life", "pos": "phrase", "ipa": "/haɪ laɪf/", "vi": "lối sống thượng lưu xa hoa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000421", "hw": "keep back", "pos": "phrase", "ipa": "/kiːp bæk/", "vi": "giữ khoảng cách; giấu kín tin", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000422", "hw": "old world", "pos": "phrase", "ipa": "/oʊld wɜːrld/", "vi": "Cựu Thế Giới (Á, Âu, Phi)", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000423", "hw": "put back", "pos": "phrase", "ipa": "/pʊt bæk/", "vi": "đặt lại chỗ cũ; hoãn lại", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000424", "hw": "school day", "pos": "phrase", "ipa": "/skuːl deɪ/", "vi": "ngày đến trường đi học", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000425", "hw": "tell on", "pos": "phrase", "ipa": "/tɛl ɑːn/", "vi": "mách tội; gây tác hại tiêu cực", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000426", "hw": "top out", "pos": "phrase", "ipa": "/tɑːp aʊt/", "vi": "chạm đỉnh; cất nóc công trình", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000427", "hw": "until now", "pos": "phrase", "ipa": "/ənˈtɪl naʊ/", "vi": "cho đến tận bây giờ", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000428", "hw": "all told", "pos": "phrase", "ipa": "/ɔːl toʊld/", "vi": "tổng cộng tất cả lại", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000429", "hw": "at once", "pos": "phrase", "ipa": "/æt wʌns/", "vi": "ngay lập tức; cùng một lúc", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000430", "hw": "believe in", "pos": "phrase", "ipa": "/bɪˈliːv ɪn/", "vi": "tin tưởng vào; tin có thật", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000431", "hw": "call for", "pos": "phrase", "ipa": "/kɔːl fɔːr/", "vi": "đòi hỏi yêu cầu; đón ai", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000432", "hw": "call in", "pos": "phrase", "ipa": "/kɔːl ɪn/", "vi": "mời chuyên gia đến; gọi điện vào", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000433", "hw": "each year", "pos": "phrase", "ipa": "/iːtʃ jɪər/", "vi": "hàng năm; mỗi một năm", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000434", "hw": "give and take", "pos": "phrase", "ipa": "/ɡɪv ænd teɪk/", "vi": "sự nhân nhượng tương hỗ lẫn nhau", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000435", "hw": "not bad", "pos": "phrase", "ipa": "/nɑːt bæd/", "vi": "khá ổn; cũng được đấy", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000436", "hw": "start out", "pos": "phrase", "ipa": "/stɑːrt aʊt/", "vi": "khởi đầu sự nghiệp; lên đường", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000437", "hw": "start up", "pos": "phrase", "ipa": "/stɑːrt ʌp/", "vi": "khởi nghiệp; khởi động máy móc", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000438", "hw": "take place", "pos": "phrase", "ipa": "/teɪk pleɪs/", "vi": "diễn ra; xảy ra", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000439", "hw": "call on", "pos": "phrase", "ipa": "/kɔːl ɑːn/", "vi": "kêu gọi; ghé thăm; mời phát biểu", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000440", "hw": "come home", "pos": "phrase", "ipa": "/kʌm hoʊm/", "vi": "về nhà; thấm thía sâu sắc", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000441", "hw": "first name", "pos": "phrase", "ipa": "/fɜːrst neɪm/", "vi": "tên gọi chính; tên riêng", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000442", "hw": "good night", "pos": "phrase", "ipa": "/ɡʊd naɪt/", "vi": "chúc ngủ ngon", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000443", "hw": "in name only", "pos": "phrase", "ipa": "/ɪn neɪm ˈoʊnli/", "vi": "trên danh nghĩa; hữu danh vô thực", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000444", "hw": "in one case", "pos": "phrase", "ipa": "/ɪn wʌn keɪs/", "vi": "trong một trường hợp nọ", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000445", "hw": "just in case", "pos": "phrase", "ipa": "/dʒʌst ɪn keɪs/", "vi": "phòng khi; để phòng hờ", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000446", "hw": "left over", "pos": "phrase", "ipa": "/lɛft ˈoʊvər/", "vi": "còn sót lại; thức ăn thừa", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000447", "hw": "look around", "pos": "phrase", "ipa": "/lʊk əˈraʊnd/", "vi": "nhìn quanh; đi thăm thú", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000448", "hw": "never again", "pos": "phrase", "ipa": "/ˈnɛvər əˈɡɛn/", "vi": "không bao giờ tái diễn nữa", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000449", "hw": "place down", "pos": "phrase", "ipa": "/pleɪs daʊn/", "vi": "đặt xuống; để xuống bàn", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000450", "hw": "show off", "pos": "phrase", "ipa": "/ʃoʊ ɔːf/", "vi": "khoe khoang; phô trương tài năng", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000451", "hw": "to order", "pos": "phrase", "ipa": "/tuː ˈɔːrdər/", "vi": "theo đơn đặt hàng riêng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000452", "hw": "try for", "pos": "phrase", "ipa": "/traɪ fɔːr/", "vi": "nỗ lực giành lấy; thi tuyển", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000453", "hw": "back away", "pos": "phrase", "ipa": "/bæk əˈweɪ/", "vi": "lùi bước; né tránh cam kết", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000454", "hw": "business people", "pos": "phrase", "ipa": "/ˈbɪznəs ˈpiːpəl/", "vi": "giới kinh doanh; giới doanh nhân", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000455", "hw": "call at", "pos": "phrase", "ipa": "/kɔːl æt/", "vi": "ghé cảng; ghé qua trạm dừng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000456", "hw": "go away", "pos": "phrase", "ipa": "/ɡoʊ əˈweɪ/", "vi": "rời đi; biến mất tan biến", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000457", "hw": "home from home", "pos": "phrase", "ipa": "/hoʊm frʌm hoʊm/", "vi": "nơi ấm cúng như ở nhà", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000458", "hw": "home help", "pos": "phrase", "ipa": "/hoʊm hɛlp/", "vi": "người giúp việc hỗ trợ tại gia", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000459", "hw": "in line", "pos": "phrase", "ipa": "/ɪn laɪn/", "vi": "xếp thành hàng; phù hợp với", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000460", "hw": "in order", "pos": "phrase", "ipa": "/ɪn ˈɔːrdər/", "vi": "ngăn nắp; hợp lệ; đúng mực", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000461", "hw": "keep going", "pos": "phrase", "ipa": "/kiːp ˈɡoʊɪŋ/", "vi": "tiếp tục tiến bước; kiên trì", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000462", "hw": "live out", "pos": "phrase", "ipa": "/lɪv aʊt/", "vi": "sống trọn đời; thực hiện giấc mơ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000463", "hw": "live up to", "pos": "phrase", "ipa": "/lɪv ʌp tuː/", "vi": "đáp ứng kỳ vọng; xứng đáng với", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000464", "hw": "long since", "pos": "phrase", "ipa": "/lɔːŋ sɪns/", "vi": "từ lâu lắm rồi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000465", "hw": "old man", "pos": "phrase", "ipa": "/oʊld mæn/", "vi": "ông lão; ông già; người cha", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000466", "hw": "on the job", "pos": "phrase", "ipa": "/ɑːn ðə dʒɑːb/", "vi": "trong khi làm việc; thực tế nghề", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000467", "hw": "on the side", "pos": "phrase", "ipa": "/ɑːn ðə saɪd/", "vi": "làm thêm ngoài luồng; ăn vụng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000468", "hw": "out of nothing", "pos": "phrase", "ipa": "/aʊt əv ˈnʌθɪŋ/", "vi": "từ con số không; tự nhiên có", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000469", "hw": "point out", "pos": "phrase", "ipa": "/pɔɪnt aʊt/", "vi": "chỉ ra; vạch rõ vấn đề", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000470", "hw": "point up", "pos": "phrase", "ipa": "/pɔɪnt ʌp/", "vi": "làm nổi bật; nhấn mạnh rõ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000471", "hw": "put right", "pos": "phrase", "ipa": "/pʊt raɪt/", "vi": "sửa chữa sai lầm; chấn chỉnh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000472", "hw": "put to work", "pos": "phrase", "ipa": "/pʊt tuː wɜːrk/", "vi": "đưa vào sử dụng; giao việc làm", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000473", "hw": "run for", "pos": "phrase", "ipa": "/rʌn fɔːr/", "vi": "tranh cử chức vụ; chạy đến", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000474", "hw": "try on", "pos": "phrase", "ipa": "/traɪ ɑːn/", "vi": "mặc thử quần áo; thử giở trò", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000475", "hw": "by far", "pos": "phrase", "ipa": "/baɪ fɑːr/", "vi": "vượt trội hơn hẳn; cách biệt xa", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000476", "hw": "come around", "pos": "phrase", "ipa": "/kʌm əˈraʊnd/", "vi": "hồi tỉnh; đổi ý thuận; ghé chơi", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000477", "hw": "hard up", "pos": "phrase", "ipa": "/hɑːrd ʌp/", "vi": "túng thiếu tiền bạc; cạn kiệt", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000478", "hw": "keep off", "pos": "phrase", "ipa": "/kiːp ɔːf/", "vi": "tránh xa; không giẫm lên; kiêng", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000479", "hw": "later on", "pos": "phrase", "ipa": "/ˈleɪtər ɑːn/", "vi": "về sau này; một lát nữa", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000480", "hw": "live it up", "pos": "phrase", "ipa": "/lɪv ɪt ʌp/", "vi": "ăn chơi xả láng; hưởng lạc", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000481", "hw": "once more", "pos": "phrase", "ipa": "/wʌns mɔːr/", "vi": "thêm một lần nữa", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000482", "hw": "play back", "pos": "phrase", "ipa": "/pleɪ bæk/", "vi": "phát lại video bản thu", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000483", "hw": "put off", "pos": "phrase", "ipa": "/pʊt ɔːf/", "vi": "hoãn lại; gây mất hứng; khó chịu", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000484", "hw": "put one over", "pos": "phrase", "ipa": "/pʊt wʌn ˈoʊvər/", "vi": "qua mặt lừa dối ai đó", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000485", "hw": "run on", "pos": "phrase", "ipa": "/rʌn ɑːn/", "vi": "chạy bằng nhiên liệu; nói dông dài", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000486", "hw": "stop up", "pos": "phrase", "ipa": "/stɑːp ʌp/", "vi": "bịt kín lỗ rò; thức khuya", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000487", "hw": "thank you", "pos": "phrase", "ipa": "/θæŋk juː/", "vi": "cảm ơn bạn; xin cám ơn", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000488", "hw": "will power", "pos": "phrase", "ipa": "/wɪl ˈpaʊər/", "vi": "nghị lực ý chí kiên định", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000489", "hw": "all at once", "pos": "phrase", "ipa": "/ɔːl æt wʌns/", "vi": "bất thình lình; cùng một lúc", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000490", "hw": "call up", "pos": "phrase", "ipa": "/kɔːl ʌp/", "vi": "gọi nhập ngũ; gọi điện thoại", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000491", "hw": "give or take", "pos": "phrase", "ipa": "/ɡɪv ɔːr teɪk/", "vi": "xấp xỉ khoảng chừng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000492", "hw": "hard time", "pos": "phrase", "ipa": "/hɑːrd taɪm/", "vi": "thời gian gian nan khó khăn", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000493", "hw": "head up", "pos": "phrase", "ipa": "/hɛd ʌp/", "vi": "đứng đầu lãnh đạo; ngẩng đầu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000494", "hw": "home game", "pos": "phrase", "ipa": "/hoʊm ɡeɪm/", "vi": "trận đấu trên sân nhà", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000495", "hw": "in general", "pos": "phrase", "ipa": "/ɪn ˈdʒɛnrəl/", "vi": "nói chung; nhìn chung tổng quát", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000496", "hw": "let go", "pos": "phrase", "ipa": "/lɛt ɡoʊ/", "vi": "buông tay; sa thải; từ bỏ", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000497", "hw": "let go of", "pos": "phrase", "ipa": "/lɛt ɡoʊ əv/", "vi": "buông tay thả ra; từ bỏ", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000498", "hw": "mean time", "pos": "phrase", "ipa": "/miːn taɪm/", "vi": "giờ mặt trời trung bình", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000499", "hw": "point in time", "pos": "phrase", "ipa": "/pɔɪnt ɪn taɪm/", "vi": "thời điểm cụ thể", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000500", "hw": "right away", "pos": "phrase", "ipa": "/raɪt əˈweɪ/", "vi": "ngay tức thì; ngay lập tức", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.000501", "hw": "run by", "pos": "phrase", "ipa": "/rʌn baɪ/", "vi": "hỏi ý kiến nhanh; chạy lướt qua", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Validation
raw_items = json.load(open('scratch/b21_r01_raw_p5.json', 'r', encoding='utf-8'))
assert len(part5_data) == 100
assert len(raw_items) == 100

for i, item in enumerate(part5_data):
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

with open('scratch/b21_r01_p5.json', 'w', encoding='utf-8') as f:
    json.dump(part5_data, f, ensure_ascii=False, indent=2)

print("b21_r01_p5.json created successfully and validated!")
