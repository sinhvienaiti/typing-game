import json

items = [
  {"id": "lex.en.200k.062303", "hw": "penknives", "pos": "noun", "ipa": "/ˈpɛnnaɪvz/", "vi": "dao nhíp gấp bỏ túi; dao rọc nhỏ"},
  {"id": "lex.en.200k.062304", "hw": "perfidies", "pos": "noun", "ipa": "/ˈpɜːrfɪdiz/", "vi": "sự bội tín; lòng phản bội tráo trở"},
  {"id": "lex.en.200k.062305", "hw": "pestises", "pos": "noun", "ipa": "/ˈpɛstɪsɪz/", "vi": "trực khuẩn gây bệnh dịch hạch"},
  {"id": "lex.en.200k.062306", "hw": "phrygias", "pos": "noun", "ipa": "/ˈfrɪdʒiəz/", "vi": "vương quốc cổ Phrygia Tiểu Á"},
  {"id": "lex.en.200k.062307", "hw": "pocketfuls", "pos": "noun", "ipa": "/ˈpɑːkɪtfʊlz/", "vi": "lượng chứa đầy một túi áo quần"},
  {"id": "lex.en.200k.062308", "hw": "rammers", "pos": "noun", "ipa": "/ˈræmərz/", "vi": "búa đầm nền đất; que nạp nòng pháo"},
  {"id": "lex.en.200k.062309", "hw": "reabsorptions", "pos": "noun", "ipa": "/ˌriːəbˈzɔːrpʃənz/", "vi": "sự tái hấp thu sinh học vào máu"},
  {"id": "lex.en.200k.062310", "hw": "redacted", "pos": "verb", "ipa": "/rɪˈdæktɪd/", "vi": "đã biên tập; đã che phần tin mật"},
  {"id": "lex.en.200k.062311", "hw": "reformulated", "pos": "verb", "ipa": "/ˌriːˈfɔːrmjʊleɪtɪd/", "vi": "đã điều chỉnh công thức; viết lại"},
  {"id": "lex.en.200k.062312", "hw": "reformulates", "pos": "verb", "ipa": "/ˌriːˈfɔːrmjʊleɪts/", "vi": "điều chỉnh công thức; diễn đạt lại"},
  {"id": "lex.en.200k.062313", "hw": "reformulating", "pos": "verb", "ipa": "/ˌriːˈfɔːrmjʊleɪtɪŋ/", "vi": "đang điều chỉnh công thức; viết lại"},
  {"id": "lex.en.200k.062314", "hw": "relaxers", "pos": "noun", "ipa": "/rɪˈlæksərz/", "vi": "thuốc duỗi thẳng tóc; chất giãn cơ"},
  {"id": "lex.en.200k.062315", "hw": "roadbeds", "pos": "noun", "ipa": "/ˈroʊdbɛdz/", "vi": "nền móng đường ray và mặt đường bộ"},
  {"id": "lex.en.200k.062316", "hw": "rubuses", "pos": "noun", "ipa": "/ˈruːbəsɪz/", "vi": "chi cây mâm xôi dâu tây gai Rubus"},
  {"id": "lex.en.200k.062317", "hw": "scabbier", "pos": "adj", "ipa": "/ˈskæbiər/", "vi": "đầy vảy ghẻ lở hơn; đê tiện hơn"},
  {"id": "lex.en.200k.062318", "hw": "scabbiest", "pos": "adj", "ipa": "/ˈskæbiɪst/", "vi": "nhiều vảy ghẻ lở nhất; tồi tệ nhất"},
  {"id": "lex.en.200k.062319", "hw": "scheldts", "pos": "noun", "ipa": "/skɛlts/", "vi": "dòng sông Scheldt chảy qua Tây Âu"},
  {"id": "lex.en.200k.062320", "hw": "shakespearians", "pos": "noun", "ipa": "/ʃeɪkˈspɪriənz/", "vi": "học giả nghiên cứu về Shakespeare"},
  {"id": "lex.en.200k.062321", "hw": "sibilants", "pos": "noun", "ipa": "/ˈsɪbələnts/", "vi": "phụ âm xuýt rít gió như s và sh"},
  {"id": "lex.en.200k.062322", "hw": "socialities", "pos": "noun", "ipa": "/ˌsoʊʃiˈælətiz/", "vi": "tính thích giao lưu bầy đàn xã hội"},
  {"id": "lex.en.200k.062323", "hw": "solidi", "pos": "noun", "ipa": "/ˈsɑːlɪdi/", "vi": "tiền vàng cổ La Mã; dấu gạch chéo"},
  {"id": "lex.en.200k.062324", "hw": "sonographies", "pos": "noun", "ipa": "/səˈnɑːɡrəfiz/", "vi": "kỹ thuật chụp chẩn đoán siêu âm"},
  {"id": "lex.en.200k.062325", "hw": "speakerships", "pos": "noun", "ipa": "/ˈspiːkərʃɪps/", "vi": "chức vụ chủ tịch hạ viện quốc hội"},
  {"id": "lex.en.200k.062326", "hw": "spillanes", "pos": "noun", "ipa": "/spɪˈleɪnz/", "vi": "nhà văn trinh thám Mickey Spillane"},
  {"id": "lex.en.200k.062327", "hw": "streakers", "pos": "noun", "ipa": "/ˈstriːkərz/", "vi": "người chạy khỏa thân nơi đông người"},
  {"id": "lex.en.200k.062328", "hw": "strictures", "pos": "noun", "ipa": "/ˈstrɪktʃərz/", "vi": "lời phê bình gay gắt; chứng hẹp ống"},
  {"id": "lex.en.200k.062329", "hw": "studentships", "pos": "noun", "ipa": "/ˈstjuːdntʃɪps/", "vi": "suất học bổng nghiên cứu bậc cao"},
  {"id": "lex.en.200k.062330", "hw": "sunrays", "pos": "noun", "ipa": "/ˈsʌnreɪz/", "vi": "những tia nắng mặt trời rực rỡ"},
  {"id": "lex.en.200k.062331", "hw": "swedenborgs", "pos": "noun", "ipa": "/ˈswiːdnbɔːrɡz/", "vi": "nhà khoa học thần bí Swedenborg"},
  {"id": "lex.en.200k.062332", "hw": "tearjerkers", "pos": "noun", "ipa": "/ˈtɪərdʒɜːrkərz/", "vi": "phim chuyện bi lụy đẫm nước mắt"},
  {"id": "lex.en.200k.062333", "hw": "temporalities", "pos": "noun", "ipa": "/ˌtɛmpəˈrælɪtiz/", "vi": "tài sản trần thế của giáo hội"},
  {"id": "lex.en.200k.062334", "hw": "tercentenaries", "pos": "noun", "ipa": "/ˌtɜːrsɛnˈtɛnəriz/", "vi": "lễ kỷ niệm trọng thể ba trăm năm"},
  {"id": "lex.en.200k.062335", "hw": "tippets", "pos": "noun", "ipa": "/ˈtɪpɪts/", "vi": "khăn choàng cổ lông thú dài hẹp"},
  {"id": "lex.en.200k.062336", "hw": "toscanas", "pos": "noun", "ipa": "/tɔːˈskɑːnəz/", "vi": "vùng đồi nho lịch sử Tuscany ở Ý"},
  {"id": "lex.en.200k.062337", "hw": "tradecrafts", "pos": "noun", "ipa": "/ˈtreɪdkræfts/", "vi": "nghiệp vụ điệp viên; kỹ năng nghề"},
  {"id": "lex.en.200k.062338", "hw": "vertus", "pos": "noun", "ipa": "/vɜːrˈtuːz/", "vi": "niềm say mê sưu tầm cổ vật mỹ nghệ"},
  {"id": "lex.en.200k.062339", "hw": "wagtails", "pos": "noun", "ipa": "/ˈwæɡteɪlz/", "vi": "loài chim chìa vôi hay vẫy đuôi dài"},
  {"id": "lex.en.200k.062340", "hw": "whished", "pos": "verb", "ipa": "/wɪʃt/", "vi": "đã vụt qua kêu vù vù; rít nhẹ"},
  {"id": "lex.en.200k.062341", "hw": "whishes", "pos": "verb", "ipa": "/ˈwɪʃɪz/", "vi": "bay vụt qua kêu tiếng vù vù nhẹ"},
  {"id": "lex.en.200k.062342", "hw": "whishing", "pos": "verb", "ipa": "/ˈwɪʃɪŋ/", "vi": "đang lướt vút qua kêu tiếng vù"},
  {"id": "lex.en.200k.062343", "hw": "zinnias", "pos": "noun", "ipa": "/ˈzɪniəz/", "vi": "cây hoa cúc bách nhật sắc rực rỡ"},
  {"id": "lex.en.200k.062344", "hw": "american merganser", "pos": "phrase", "ipa": "/əˈmɛrɪkən mərˈɡænsər/", "vi": "loài vịt mỏ nhọn lớn ăn cá Bắc Mỹ"},
  {"id": "lex.en.200k.062345", "hw": "attributive genitive", "pos": "phrase", "ipa": "/əˈtrɪbjətɪv ˈdʒɛnətɪv/", "vi": "sở hữu cách đóng vai trò định ngữ"},
  {"id": "lex.en.200k.062346", "hw": "attributive genitive case", "pos": "phrase", "ipa": "/əˈtrɪbjətɪv ˈdʒɛnətɪv keɪs/", "vi": "biến cách sở hữu làm từ bổ nghĩa"},
  {"id": "lex.en.200k.062347", "hw": "avena sativa", "pos": "phrase", "ipa": "/əˈviːnə səˈtaɪvə/", "vi": "cây ngũ cốc yến mạch dinh dưỡng"},
  {"id": "lex.en.200k.062348", "hw": "battle of fontenoy", "pos": "phrase", "ipa": "/ˈbætl əv ˌfɔːntəˈnwɑː/", "vi": "trận quyết chiến Fontenoy năm 1745"},
  {"id": "lex.en.200k.062349", "hw": "bean tostada", "pos": "phrase", "ipa": "/biːn toʊˈstɑːdə/", "vi": "bánh ngô giòn phủ đậu nghiền Mexico"},
  {"id": "lex.en.200k.062350", "hw": "bernard mannes baruch", "pos": "phrase", "ipa": "/bərˈnɑːrd ˈmænəs bəˈruːk/", "vi": "nhà tài chính Mỹ Bernard Baruch"},
  {"id": "lex.en.200k.062351", "hw": "betsy griscom ross", "pos": "phrase", "ipa": "/ˈbɛtsi ˈɡrɪskəm rɔːs/", "vi": "nữ thợ may quốc kỳ Mỹ Betsy Ross"},
  {"id": "lex.en.200k.062352", "hw": "brooder pneumonia", "pos": "phrase", "ipa": "/ˈbruːdər nuːˈmoʊniə/", "vi": "bệnh viêm phổi nấm ở gà vịt con"},
  {"id": "lex.en.200k.062353", "hw": "campanula medium", "pos": "phrase", "ipa": "/kæmˈpænjʊlə ˈmiːdiəm/", "vi": "hoa chuông Canterbury nở rộ sặc sỡ"},
  {"id": "lex.en.200k.062354", "hw": "chao phraya", "pos": "phrase", "ipa": "/tʃaʊ ˈpraɪə/", "vi": "dòng sông lớn Chao Phraya Thái Lan"},
  {"id": "lex.en.200k.062355", "hw": "charles bullfinch", "pos": "phrase", "ipa": "/tʃɑːrlz ˈbʊlfɪntʃ/", "vi": "kiến trúc sư Mỹ Charles Bulfinch"},
  {"id": "lex.en.200k.062356", "hw": "coitus interruptus", "pos": "phrase", "ipa": "/ˈkoʊɪtəs ˌɪntəˈrʌptəs/", "vi": "biện pháp tránh thai tự nhiên"},
  {"id": "lex.en.200k.062357", "hw": "cornus canadensis", "pos": "phrase", "ipa": "/ˈkɔːrnəs ˌkænəˈdɛnsɪs/", "vi": "cây sơn thù du lùn Canada quả đỏ"},
  {"id": "lex.en.200k.062358", "hw": "cyano group", "pos": "phrase", "ipa": "/saɪˈænoʊ ɡruːp/", "vi": "nhóm chức hóa học xyanua -CN"},
  {"id": "lex.en.200k.062359", "hw": "cyano radical", "pos": "phrase", "ipa": "/saɪˈænoʊ ˈrædɪkl/", "vi": "gốc tự do hóa học xyanua hoạt động"},
  {"id": "lex.en.200k.062360", "hw": "erythema multiforme", "pos": "phrase", "ipa": "/ˌɛrɪˈθiːmə ˌmʌltɪˈfɔːrmi/", "vi": "bệnh da liễu hồng ban đa dạng bia"},
  {"id": "lex.en.200k.062361", "hw": "felis serval", "pos": "phrase", "ipa": "/ˈfiːlɪs ˈsɜːrvəl/", "vi": "loài linh miêu mèo đồng cỏ châu Phi"},
  {"id": "lex.en.200k.062362", "hw": "frederic goudy", "pos": "phrase", "ipa": "/ˈfrɛdərɪk ˈɡaʊdi/", "vi": "nhà thiết kế chữ in Frederic Goudy"},
  {"id": "lex.en.200k.062363", "hw": "frederic william goudy", "pos": "phrase", "ipa": "/ˈfrɛdərɪk ˈwɪljəm ˈɡaʊdi/", "vi": "tác giả kiểu chữ Mỹ Frederic Goudy"},
  {"id": "lex.en.200k.062364", "hw": "giant puffball", "pos": "phrase", "ipa": "/ˈdʒaɪənt ˈpʌfbɔːl/", "vi": "nấm bóng tròn trắng khổng lồ"},
  {"id": "lex.en.200k.062365", "hw": "hans jurgen eysenck", "pos": "phrase", "ipa": "/hɑːnz ˈjʊərɡən ˈaɪzɛŋk/", "vi": "nhà tâm lý học Hans Jürgen Eysenck"},
  {"id": "lex.en.200k.062366", "hw": "heaviside layer", "pos": "phrase", "ipa": "/ˈhɛvisɪd ˈleɪər/", "vi": "tầng điện ly phản xạ sóng vô tuyến"},
  {"id": "lex.en.200k.062367", "hw": "heinrich engelhard steinway", "pos": "phrase", "ipa": "/ˈhaɪnrɪk ˈɛŋɡəlhɑːrt ˈstaɪnweɪ/", "vi": "nhà chế tạo đàn dương cầm Steinway"},
  {"id": "lex.en.200k.062368", "hw": "identikit picture", "pos": "phrase", "ipa": "/aɪˈdɛntɪkɪt ˈpɪktʃər/", "vi": "bức ảnh dựng chân dung nghi phạm"},
  {"id": "lex.en.200k.062369", "hw": "imperfective aspect", "pos": "phrase", "ipa": "/ˌɪmpərˈfɛktɪv ˈæspɛkt/", "vi": "thể chưa hoàn thành trong ngữ pháp"},
  {"id": "lex.en.200k.062370", "hw": "imperforate hymen", "pos": "phrase", "ipa": "/ɪmˈpɜːrfərət ˈhaɪmən/", "vi": "dị tật y khoa màng trinh bịt kín"},
  {"id": "lex.en.200k.062371", "hw": "inkblot test", "pos": "phrase", "ipa": "/ˈɪŋkblɑːt tɛst/", "vi": "bài trắc nghiệm vết mực Rorschach"},
  {"id": "lex.en.200k.062372", "hw": "lake urmia", "pos": "phrase", "ipa": "/leɪk ˈʊərmiə/", "vi": "hồ nước mặn lớn Urmia tây bắc Iran"},
  {"id": "lex.en.200k.062373", "hw": "laskar jihad", "pos": "phrase", "ipa": "/ˈlɑːskɑːr dʒɪˈhɑːd/", "vi": "tổ chức Hồi giáo Indonesia Laskar"},
  {"id": "lex.en.200k.062374", "hw": "leopold kronecker", "pos": "phrase", "ipa": "/ˈliːəpoʊld ˈkrɑːnɛkər/", "vi": "nhà toán học Đức Leopold Kronecker"},
  {"id": "lex.en.200k.062375", "hw": "lubber line", "pos": "phrase", "ipa": "/ˈlʌbər laɪn/", "vi": "vạch chuẩn hướng mũi tàu la bàn"},
  {"id": "lex.en.200k.062376", "hw": "mesabi range", "pos": "phrase", "ipa": "/məˈsɑːbi reɪndʒ/", "vi": "vùng mỏ quặng sắt Mesabi Minnesota"},
  {"id": "lex.en.200k.062377", "hw": "michael ondaatje", "pos": "phrase", "ipa": "/ˈmaɪkl ɑːnˈdɑːtʃi/", "vi": "nhà văn Canada Michael Ondaatje"},
  {"id": "lex.en.200k.062378", "hw": "milking shorthorn", "pos": "phrase", "ipa": "/ˈmɪlkɪŋ ˈʃɔːrthɔːrn/", "vi": "giống bò sữa sừng ngắn nước Anh"},
  {"id": "lex.en.200k.062379", "hw": "mirabilis laevis", "pos": "phrase", "ipa": "/mɪˈræbəlɪs ˈliːvɪs/", "vi": "cây hoa bốn giờ dại California"},
  {"id": "lex.en.200k.062380", "hw": "muhammadan calendar", "pos": "phrase", "ipa": "/moʊˈhæmədn ˈkælɪndər/", "vi": "lịch âm truyền thống của Hồi giáo"},
  {"id": "lex.en.200k.062381", "hw": "naiad family", "pos": "phrase", "ipa": "/ˈnaɪæd ˈfæməli/", "vi": "họ thực vật rong đuôi chồn nước"},
  {"id": "lex.en.200k.062382", "hw": "nilgiri hills", "pos": "phrase", "ipa": "/nɪlˈɡɪri hɪlz/", "vi": "dãy núi Đồi Xanh Nilgiri nam Ấn Độ"},
  {"id": "lex.en.200k.062383", "hw": "nyssa aquatica", "pos": "phrase", "ipa": "/ˈnɪsə əˈkwætɪkə/", "vi": "cây tupelo thủy sinh mọc vùng ngập"},
  {"id": "lex.en.200k.062384", "hw": "oliver heaviside", "pos": "phrase", "ipa": "/ˈɑːlɪvər ˈhɛvisɪd/", "vi": "nhà vật lý kỹ sư điện Heaviside"},
  {"id": "lex.en.200k.062385", "hw": "otitis interna", "pos": "phrase", "ipa": "/oʊˈtaɪtɪs ɪnˈtɜːrnə/", "vi": "bệnh lý viêm mê đạo tai trong"},
  {"id": "lex.en.200k.062386", "hw": "philip michael ondaatje", "pos": "phrase", "ipa": "/ˈfɪlɪp ˈmaɪkl ɑːnˈdɑːtʃi/", "vi": "tiểu thuyết gia Michael Ondaatje"},
  {"id": "lex.en.200k.062387", "hw": "plantago major", "pos": "phrase", "ipa": "/plænˈteɪɡoʊ ˈmeɪdʒər/", "vi": "cây thảo dược mã đề lá to lợi tiểu"},
  {"id": "lex.en.200k.062388", "hw": "plantago media", "pos": "phrase", "ipa": "/plænˈteɪɡoʊ ˈmiːdiə/", "vi": "cây mã đề lá trung hoa tím nhạt"},
  {"id": "lex.en.200k.062389", "hw": "plumed tussock", "pos": "phrase", "ipa": "/pluːmd ˈtʌsək/", "vi": "cây cỏ bụi lông vũ New Zealand"},
  {"id": "lex.en.200k.062390", "hw": "quitclaim deed", "pos": "phrase", "ipa": "/ˈkwɪtkleɪm diːd/", "vi": "chứng thư nhượng lại quyền sở hữu"},
  {"id": "lex.en.200k.062391", "hw": "ragged orchis", "pos": "phrase", "ipa": "/ˈræɡɪd ˈɔːrkɪs/", "vi": "cây địa lan môi tua rách xanh lục"},
  {"id": "lex.en.200k.062392", "hw": "rambutan tree", "pos": "phrase", "ipa": "/ræmˈbuːtən triː/", "vi": "cây chôm chôm nhiệt đới quả có râu"},
  {"id": "lex.en.200k.062393", "hw": "samuel rosenstock", "pos": "phrase", "ipa": "/ˈsæmjuəl ˈroʊzənstɑːk/", "vi": "nhà thơ sáng lập Dada Tristan Tzara"},
  {"id": "lex.en.200k.062394", "hw": "sodium dichromate", "pos": "phrase", "ipa": "/ˈsoʊdiəm daɪˈkroʊmeɪt/", "vi": "tinh thể cam đậm natri đicromat"},
  {"id": "lex.en.200k.062395", "hw": "sparkplug wrench", "pos": "phrase", "ipa": "/ˈspɑːrkplʌɡ rɛntʃ/", "vi": "tuýp vặn tháo lắp bugi động cơ"},
  {"id": "lex.en.200k.062396", "hw": "stratum corneum", "pos": "phrase", "ipa": "/ˈstrætəm ˈkɔːrniəm/", "vi": "lớp sừng bảo vệ ngoài cùng biểu bì"},
  {"id": "lex.en.200k.062397", "hw": "suction curettage", "pos": "phrase", "ipa": "/ˈsʌkʃən ˈkjʊərətɑːʒ/", "vi": "thủ thuật hút buồng tử cung y khoa"},
  {"id": "lex.en.200k.062398", "hw": "sulfonic acid", "pos": "phrase", "ipa": "/sʌlˈfɑːnɪk ˈæsɪd/", "vi": "nhóm axit hữu cơ mạnh axit sulfonic"},
  {"id": "lex.en.200k.062399", "hw": "superordinate word", "pos": "phrase", "ipa": "/ˌsuːpərˈɔːrdɪnət wɜːrd/", "vi": "từ thượng vị bao hàm nghĩa từ hẹp"},
  {"id": "lex.en.200k.062400", "hw": "synodic month", "pos": "phrase", "ipa": "/sɪˈnɑːdɪk mʌnθ/", "vi": "tháng giao hội chu kỳ trăng tròn"},
  {"id": "lex.en.200k.062401", "hw": "tamarisk gerbil", "pos": "phrase", "ipa": "/ˈtæmərɪsk ˈdʒɜːrbəl/", "vi": "chuột nhảy sa mạc vùng Trung Á"},
  {"id": "lex.en.200k.062402", "hw": "temporal arteritis", "pos": "phrase", "ipa": "/ˈtɛmpərəl ˌɑːrtəˈraɪtɪs/", "vi": "bệnh viêm động mạch thái dương đầu"}
]

with open('scratch/b33_r05_raw_p4.json') as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"Mismatch id at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"Mismatch hw at {i}: {item['hw']} vs {r['hw']}"
    assert len(item['vi']) <= 35, f"vi length > 35 at {i} ({item['hw']}): {len(item['vi'])}"
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {item['pos']}"
    if ' ' not in item['hw']:
        assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Invalid ipa at {i}: {item['ipa']}"
    r['pos'] = item['pos']
    r['ipa'] = item['ipa']
    r['vi'] = item['vi']
    r['status'] = 'reviewed'

with open('scratch/b33_r05_p4.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 5 Part 4 validated and written successfully.")
