import json

items = [
  {"id": "lex.en.200k.064003", "hw": "iris persica", "pos": "phrase", "ipa": "/ˈaɪrɪs ˈpɜːrsɪkə/", "vi": "hoa diên vĩ thấp Ba Tư"},
  {"id": "lex.en.200k.064004", "hw": "kit and caboodle", "pos": "phrase", "ipa": "/kɪt ənd kəˈbuːdəl/", "vi": "tất tần tật toàn bộ mọi thứ"},
  {"id": "lex.en.200k.064005", "hw": "konrad von gesner", "pos": "phrase", "ipa": "/ˈkɑːnræd vɑːn ˈɡɛsnər/", "vi": "nhà tự nhiên học Thụy Sĩ Gesner"},
  {"id": "lex.en.200k.064006", "hw": "lateral geniculate", "pos": "phrase", "ipa": "/ˈlætərəl dʒəˈnɪkjəlɪt/", "vi": "nhân thể gối bên vùng đồi thị"},
  {"id": "lex.en.200k.064007", "hw": "lateral geniculate body", "pos": "phrase", "ipa": "/ˈlætərəl dʒəˈnɪkjəlɪt ˈbɑːdi/", "vi": "thể gối bên đồi thị xử lý thị giác"},
  {"id": "lex.en.200k.064008", "hw": "lise meitner", "pos": "phrase", "ipa": "/ˈliːzə ˈmaɪtnər/", "vi": "nhà vật lý hạt nhân Lise Meitner"},
  {"id": "lex.en.200k.064009", "hw": "longtail weasel", "pos": "phrase", "ipa": "/ˈlɔːŋteɪl ˈwiːzəl/", "vi": "chồn đuôi dài Bắc Mỹ săn mồi"},
  {"id": "lex.en.200k.064010", "hw": "lucius licinius lucullus", "pos": "phrase", "ipa": "/ˈluːʃəs lɪˈsɪniəs luːˈkʌləs/", "vi": "tướng La Mã nổi danh sành ăn"},
  {"id": "lex.en.200k.064011", "hw": "major tranquilliser", "pos": "phrase", "ipa": "/ˈmeɪdʒər ˈtræŋkwəˌlaɪzər/", "vi": "thuốc an thần mạnh chống loạn (Anh)"},
  {"id": "lex.en.200k.064012", "hw": "manganese tetroxide", "pos": "phrase", "ipa": "/ˈmæŋɡəniːz tɛˈtrɑːksaɪd/", "vi": "hợp chất hóa học mangan tetroxit"},
  {"id": "lex.en.200k.064013", "hw": "microcosmic salt", "pos": "phrase", "ipa": "/ˌmaɪkrəˈkɑːzmɪk sɔːlt/", "vi": "muối natri amoni hydro photphat"},
  {"id": "lex.en.200k.064014", "hw": "minor tranquilliser", "pos": "phrase", "ipa": "/ˈmaɪnər ˈtræŋkwəˌlaɪzər/", "vi": "thuốc an thần nhẹ giải lo âu (Anh)"},
  {"id": "lex.en.200k.064015", "hw": "mya arenaria", "pos": "phrase", "ipa": "/ˈmaɪə ˌærəˈnɛriə/", "vi": "loài ngao vỏ mềm vòi dài đáy bùn"},
  {"id": "lex.en.200k.064016", "hw": "neutralisation reaction", "pos": "phrase", "ipa": "/ˌnuːtrələˈzeɪʃən riˈækʃən/", "vi": "phản ứng trung hòa axit bazơ (Anh)"},
  {"id": "lex.en.200k.064017", "hw": "nilotic language", "pos": "phrase", "ipa": "/naɪˈlɑːtɪk ˈlæŋɡwɪdʒ/", "vi": "ngôn ngữ nhóm sông Nile Đông Phi"},
  {"id": "lex.en.200k.064018", "hw": "nusa tenggara", "pos": "phrase", "ipa": "/ˈnuːsə tɛŋˈɡɑːrə/", "vi": "quần đảo Nusa Tenggara Indonesia"},
  {"id": "lex.en.200k.064019", "hw": "pisang wax", "pos": "phrase", "ipa": "/pɪˈsɑːŋ wæks/", "vi": "sáp thiên nhiên chiết xuất lá chuối"},
  {"id": "lex.en.200k.064020", "hw": "pneumocystis pneumonia", "pos": "phrase", "ipa": "/ˌnuːmoʊˈsɪstɪs nuːˈmoʊnjə/", "vi": "bệnh viêm phổi do nấm Pneumocystis"},
  {"id": "lex.en.200k.064021", "hw": "polychaete worm", "pos": "phrase", "ipa": "/ˈpɑːlɪkiːt wɜːrm/", "vi": "loài giun đốt biển có nhiều tơ"},
  {"id": "lex.en.200k.064022", "hw": "pulmonic plague", "pos": "phrase", "ipa": "/pʊlˈmɑːnɪk pleɪɡ/", "vi": "bệnh dịch hạch thể phổi lây hô hấp"},
  {"id": "lex.en.200k.064023", "hw": "salvia pratensis", "pos": "phrase", "ipa": "/ˈsælviə prəˈtɛnsɪs/", "vi": "cây xô thơm đồng cỏ hoa tím lam"},
  {"id": "lex.en.200k.064024", "hw": "senna alexandrina", "pos": "phrase", "ipa": "/ˈsɛnə ˌælɪɡzænˈdriːnə/", "vi": "cây phan tả diệp thuốc nhuận tràng"},
  {"id": "lex.en.200k.064025", "hw": "sesamoid bone", "pos": "phrase", "ipa": "/ˈsɛsəˌmɔɪd boʊn/", "vi": "xương vừng nằm bọc trong gân khớp"},
  {"id": "lex.en.200k.064026", "hw": "sida spinosa", "pos": "phrase", "ipa": "/ˈsaɪdə spɪˈnoʊsə/", "vi": "cây ké hoa vàng gai nhỏ Sida"},
  {"id": "lex.en.200k.064027", "hw": "solanum nigrum", "pos": "phrase", "ipa": "/səˈleɪnəm ˈnaɪɡrəm/", "vi": "cây lu lu đực họ Cà quả mọng đen"},
  {"id": "lex.en.200k.064028", "hw": "star ipomoea", "pos": "phrase", "ipa": "/stɑːr ˌaɪpəˈmiːə/", "vi": "dây leo bìm bìm hoa đỏ hình sao"},
  {"id": "lex.en.200k.064029", "hw": "undreamed of", "pos": "phrase", "ipa": "/ʌnˈdriːmd ʌv/", "vi": "chưa từng mơ tới; không ngờ tới"},
  {"id": "lex.en.200k.064030", "hw": "virginia cowslip", "pos": "phrase", "ipa": "/vərˈdʒɪnjə ˈkaʊslɪp/", "vi": "cây chuông xanh Bắc Mỹ Virginia"},
  {"id": "lex.en.200k.064031", "hw": "whole caboodle", "pos": "phrase", "ipa": "/hoʊl kəˈbuːdəl/", "vi": "tất thảy toàn bộ không sót thứ gì"},
  {"id": "lex.en.200k.064032", "hw": "william holmes mcguffey", "pos": "phrase", "ipa": "/ˈwɪliəm hoʊlmz məˈɡʌfi/", "vi": "nhà giáo dục tác giả sách McGuffey"},
  {"id": "lex.en.200k.064033", "hw": "abridgments", "pos": "noun", "ipa": "/əˈbrɪdʒmənts/", "vi": "bản rút gọn; sự cắt giảm quyền lợi"},
  {"id": "lex.en.200k.064034", "hw": "acuminated", "pos": "verb", "ipa": "/əˈkjuːməˌneɪtɪd/", "vi": "đã vót nhọn đầu; đã làm thuôn nhọn"},
  {"id": "lex.en.200k.064035", "hw": "acuminates", "pos": "verb", "ipa": "/əˈkjuːməˌneɪts/", "vi": "vót thuôn nhọn đầu; làm sắc nhọn"},
  {"id": "lex.en.200k.064036", "hw": "acuminating", "pos": "verb", "ipa": "/əˈkjuːməˌneɪtɪŋ/", "vi": "đang vót thuôn nhọn ở phần đầu chóp"},
  {"id": "lex.en.200k.064037", "hw": "advections", "pos": "noun", "ipa": "/ædˈvɛkʃənz/", "vi": "sự bình lưu truyền ngang khí biển"},
  {"id": "lex.en.200k.064038", "hw": "aleves", "pos": "noun", "ipa": "/əˈliːvz/", "vi": "thuốc giảm đau kháng viêm Aleve"},
  {"id": "lex.en.200k.064039", "hw": "amniocenteses", "pos": "noun", "ipa": "/ˌæmnioʊsɛnˈtiːsiːz/", "vi": "thủ thuật chọc dò dịch ối thai kỳ"},
  {"id": "lex.en.200k.064040", "hw": "amortisations", "pos": "noun", "ipa": "/ˌæmərtaɪˈzeɪʃənz/", "vi": "sự khấu hao; trả góp dần nợ (Anh)"},
  {"id": "lex.en.200k.064041", "hw": "amphotericins", "pos": "noun", "ipa": "/ˌæmfəˈtɛrəsɪnz/", "vi": "thuốc kháng nấm mạnh amphotericin"},
  {"id": "lex.en.200k.064042", "hw": "applewoods", "pos": "noun", "ipa": "/ˈæpəlˌwʊdz/", "vi": "gỗ cây táo cứng mịn dùng tiện khảm"},
  {"id": "lex.en.200k.064043", "hw": "aretes", "pos": "noun", "ipa": "/əˈrɛts/", "vi": "sống núi đá hẹp sắc như lưỡi dao"},
  {"id": "lex.en.200k.064044", "hw": "atons", "pos": "noun", "ipa": "/ˈɑːtənz/", "vi": "thần Mặt Trời Aton Ai Cập cổ đại"},
  {"id": "lex.en.200k.064045", "hw": "bahais", "pos": "noun", "ipa": "/bɑːˈhaɪz/", "vi": "tín đồ tôn giáo Baha'i Ba Tư"},
  {"id": "lex.en.200k.064046", "hw": "bigheads", "pos": "noun", "ipa": "/ˈbɪɡhɛdz/", "vi": "kẻ tự phụ; bệnh sưng đầu ở gia súc"},
  {"id": "lex.en.200k.064047", "hw": "bines", "pos": "noun", "ipa": "/baɪnz/", "vi": "thân dây quấn leo; cây hoa bia"},
  {"id": "lex.en.200k.064048", "hw": "briarwoods", "pos": "noun", "ipa": "/ˈbraɪərˌwʊdz/", "vi": "gỗ rễ cây thạch nam làm tẩu thuốc"},
  {"id": "lex.en.200k.064049", "hw": "briquettes", "pos": "noun", "ipa": "/brɪˈkɛts/", "vi": "viên than ép; cục mùn cưa nén đốt"},
  {"id": "lex.en.200k.064050", "hw": "browbeating", "pos": "verb", "ipa": "/ˈbraʊˌbiːtɪŋ/", "vi": "đang quát nạt hăm dọa bắt nạt ép"},
  {"id": "lex.en.200k.064051", "hw": "browbeats", "pos": "verb", "ipa": "/ˈbraʊbiːts/", "vi": "nạt nộ đe dọa ức hiếp ép buộc"},
  {"id": "lex.en.200k.064052", "hw": "butanols", "pos": "noun", "ipa": "/ˈbjuːtənɔːlz/", "vi": "cồn công nghiệp dung môi butanol"},
  {"id": "lex.en.200k.064053", "hw": "cabgs", "pos": "noun", "ipa": "/ˌsiːˌeɪˌbiːˈdʒiːz/", "vi": "phẫu thuật bắc cầu mạch vành tim"},
  {"id": "lex.en.200k.064054", "hw": "canonisations", "pos": "noun", "ipa": "/ˌkænənaɪˈzeɪʃənz/", "vi": "nghi lễ phong thánh giáo hội (Anh)"},
  {"id": "lex.en.200k.064055", "hw": "chapultepecs", "pos": "noun", "ipa": "/tʃəˈpʊltəˌpɛks/", "vi": "công viên lâu đài Chapultepec"},
  {"id": "lex.en.200k.064056", "hw": "cnuts", "pos": "noun", "ipa": "/kəˈnuːts/", "vi": "vua Đan Mạch và Anh Canute Đại đế"},
  {"id": "lex.en.200k.064057", "hw": "complementations", "pos": "noun", "ipa": "/ˌkɑːmpləmɛnˈteɪʃənz/", "vi": "sự bổ sung kết hợp hoàn thiện gen"},
  {"id": "lex.en.200k.064058", "hw": "conspecifics", "pos": "noun", "ipa": "/ˌkɑːnspəˈsɪfɪks/", "vi": "các cá thể sinh vật cùng một loài"},
  {"id": "lex.en.200k.064059", "hw": "crinolines", "pos": "noun", "ipa": "/ˈkrɪnəlɪnz/", "vi": "váy phồng khung cứng thời Victoria"},
  {"id": "lex.en.200k.064060", "hw": "crossbenches", "pos": "noun", "ipa": "/ˈkrɔːsˌbɛntʃɪz/", "vi": "hàng ghế nghị sĩ độc lập nghị viện"},
  {"id": "lex.en.200k.064061", "hw": "daydreamers", "pos": "noun", "ipa": "/ˈdeɪˌdriːmərz/", "vi": "người hay mơ mộng viển vông"},
  {"id": "lex.en.200k.064062", "hw": "deathwatches", "pos": "noun", "ipa": "/ˈdɛθˌwɑːtʃɪz/", "vi": "bọ đục gỗ gõ tích tắc; phiên canh"},
  {"id": "lex.en.200k.064063", "hw": "dentines", "pos": "noun", "ipa": "/ˈdɛntiːnz/", "vi": "lớp ngà răng nằm dưới men răng"},
  {"id": "lex.en.200k.064064", "hw": "dingdonged", "pos": "verb", "ipa": "/ˈdɪŋdɔːŋd/", "vi": "đã rung chuông kêu đinh đoong"},
  {"id": "lex.en.200k.064065", "hw": "dingdonging", "pos": "verb", "ipa": "/ˈdɪŋdɔːŋɪŋ/", "vi": "đang ngân tiếng chuông đinh đoong"},
  {"id": "lex.en.200k.064066", "hw": "dingdongs", "pos": "verb", "ipa": "/ˈdɪŋdɔːŋz/", "vi": "kêu đinh đoong; cãi vã quyết liệt"},
  {"id": "lex.en.200k.064067", "hw": "diplodocuses", "pos": "noun", "ipa": "/dɪˈplɑːdəkəsɪz/", "vi": "khủng long cổ dài Diplodocus"},
  {"id": "lex.en.200k.064068", "hw": "disproportions", "pos": "noun", "ipa": "/ˌdɪsprəˈpɔːrʃənz/", "vi": "sự chênh lệch mất cân đối tỷ lệ"},
  {"id": "lex.en.200k.064069", "hw": "downslopes", "pos": "noun", "ipa": "/ˈdaʊnsloʊps/", "vi": "sườn dốc thoai thoải đi xuống"},
  {"id": "lex.en.200k.064070", "hw": "elisions", "pos": "noun", "ipa": "/ɪˈlɪʒənz/", "vi": "sự lược bỏ âm tiết khi phát âm"},
  {"id": "lex.en.200k.064071", "hw": "encephalomyelitides", "pos": "noun", "ipa": "/ɛnˌsɛfəloʊˌmaɪəˈlaɪtɪdiːz/", "vi": "bệnh lý viêm não và tủy sống"},
  {"id": "lex.en.200k.064072", "hw": "enkidus", "pos": "noun", "ipa": "/ɛŋˈkiːduːz/", "vi": "nhân vật sử thi Enkidu (Gilgamesh)"},
  {"id": "lex.en.200k.064073", "hw": "enlargers", "pos": "noun", "ipa": "/ɪnˈlɑːrdʒərz/", "vi": "máy phóng ảnh phim buồng tối"},
  {"id": "lex.en.200k.064074", "hw": "entablatures", "pos": "noun", "ipa": "/ɛnˈtæblətʃərz/", "vi": "dầm bộ diềm mái đặt trên đầu cột"},
  {"id": "lex.en.200k.064075", "hw": "equilibrations", "pos": "noun", "ipa": "/ɪˌkwɪlɪˈbreɪʃənz/", "vi": "sự đạt trạng thái cân bằng ổn định"},
  {"id": "lex.en.200k.064076", "hw": "ewers", "pos": "noun", "ipa": "/ˈjuːərz/", "vi": "bình gốm sứ miệng rộng có vòi rót"},
  {"id": "lex.en.200k.064077", "hw": "farragoes", "pos": "noun", "ipa": "/fəˈrɑːɡoʊz/", "vi": "mớ hỗn tạp lộn xộn nhiều thứ"},
  {"id": "lex.en.200k.064078", "hw": "fingerlings", "pos": "noun", "ipa": "/ˈfɪŋɡərlɪŋz/", "vi": "cá hương giống nhỏ bằng ngón tay"},
  {"id": "lex.en.200k.064079", "hw": "flattops", "pos": "noun", "ipa": "/ˈflættɑːps/", "vi": "tóc húi cua đầu bằng; tàu sân bay"},
  {"id": "lex.en.200k.064080", "hw": "fugus", "pos": "noun", "ipa": "/ˈfuːɡuːz/", "vi": "cá nóc Nhật Bản độc tố mạnh fugu"},
  {"id": "lex.en.200k.064081", "hw": "garroted", "pos": "verb", "ipa": "/ɡəˈroʊtɪd/", "vi": "đã hành quyết bằng cách siết cổ"},
  {"id": "lex.en.200k.064082", "hw": "garrotes", "pos": "noun", "ipa": "/ɡəˈroʊts/", "vi": "dụng cụ dây siết cổ; án siết cổ"},
  {"id": "lex.en.200k.064083", "hw": "garroting", "pos": "verb", "ipa": "/ɡəˈroʊtɪŋ/", "vi": "đang siết cổ cướp hoặc hành quyết"},
  {"id": "lex.en.200k.064084", "hw": "glycosides", "pos": "noun", "ipa": "/ˈɡlaɪkəˌsaɪdz/", "vi": "hợp chất hữu cơ đường glycosid"},
  {"id": "lex.en.200k.064085", "hw": "godowns", "pos": "noun", "ipa": "/ˈɡoʊdaʊnz/", "vi": "nhà kho chứa hàng cảng biển châu Á"},
  {"id": "lex.en.200k.064086", "hw": "gorkis", "pos": "noun", "ipa": "/ˈɡɔːrkiz/", "vi": "đại văn hào Xô Viết Maxim Gorky"},
  {"id": "lex.en.200k.064087", "hw": "greensands", "pos": "noun", "ipa": "/ˈɡriːnsændz/", "vi": "cát lục giàu khoáng chất glauconit"},
  {"id": "lex.en.200k.064088", "hw": "gubbinses", "pos": "noun", "ipa": "/ˈɡʌbɪnzɪz/", "vi": "đồ lặt vặt linh tinh vụn vặt (Anh)"},
  {"id": "lex.en.200k.064089", "hw": "gudgeons", "pos": "noun", "ipa": "/ˈɡʌdʒənz/", "vi": "cá đục nước ngọt; chốt xoay trục"},
  {"id": "lex.en.200k.064090", "hw": "gulas", "pos": "noun", "ipa": "/ˈɡuːləz/", "vi": "nữ thần y học Lưỡng Hà cổ đại Gula"},
  {"id": "lex.en.200k.064091", "hw": "homebuilders", "pos": "noun", "ipa": "/ˈhoʊmˌbɪldərz/", "vi": "nhà thầu xây dựng nhà ở dân dụng"},
  {"id": "lex.en.200k.064092", "hw": "homonyms", "pos": "noun", "ipa": "/ˈhɑːmənɪmz/", "vi": "từ đồng âm khác nghĩa với nhau"},
  {"id": "lex.en.200k.064093", "hw": "hornbills", "pos": "noun", "ipa": "/ˈhɔːrnbɪlz/", "vi": "chim hồng hoàng mỏ sừng lớn"},
  {"id": "lex.en.200k.064094", "hw": "hydrochlorothiazides", "pos": "noun", "ipa": "/ˌhaɪdroʊˌklɔːrəˈθaɪəˌzaɪdz/", "vi": "thuốc lợi tiểu hạ áp thiazide"},
  {"id": "lex.en.200k.064095", "hw": "impactions", "pos": "noun", "ipa": "/ɪmˈpækʃənz/", "vi": "răng mọc ngầm kẹt; sự nén tắc ruột"},
  {"id": "lex.en.200k.064096", "hw": "inflators", "pos": "noun", "ipa": "/ɪnˈfleɪtərz/", "vi": "bơm hơi lốp bóng; bộ kích túi khí"},
  {"id": "lex.en.200k.064097", "hw": "jaybirds", "pos": "noun", "ipa": "/ˈdʒeɪbɜːrdz/", "vi": "chim giẻ cùi kêu to họ Quạ Bắc Mỹ"},
  {"id": "lex.en.200k.064098", "hw": "johores", "pos": "noun", "ipa": "/dʒəˈhɔːrz/", "vi": "bang Johor cực nam bán đảo Mã Lai"},
  {"id": "lex.en.200k.064099", "hw": "kroebers", "pos": "noun", "ipa": "/ˈkroʊbərz/", "vi": "nhà nhân học Mỹ Alfred Kroeber"},
  {"id": "lex.en.200k.064100", "hw": "languors", "pos": "noun", "ipa": "/ˈlæŋɡərz/", "vi": "trạng thái uể oải mệt lả mơ màng"},
  {"id": "lex.en.200k.064101", "hw": "leftfields", "pos": "noun", "ipa": "/ˈlɛftfiːldz/", "vi": "khu vực cánh trái sân bóng chày"},
  {"id": "lex.en.200k.064102", "hw": "leishmanias", "pos": "noun", "ipa": "/liːʃˈmeɪniəz/", "vi": "ký sinh trùng đơn bào Leishmania"}
]

with open('scratch/b33_r09_raw_p1.json') as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"Mismatch id at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"Mismatch hw at {i}: {item['hw']} vs {r['hw']}"
    assert len(item['vi']) <= 35, f"vi length > 35 at {i} ({item['hw']}): {len(item['vi'])}"
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {item['pos']}"
    assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Invalid ipa at {i}: {item['ipa']}"
    assert not item['ipa'][1:-1].startswith(' ') and not item['ipa'][1:-1].endswith(' '), f"Space in ipa at {i}: {item['ipa']}"
    r['pos'] = item['pos']
    r['ipa'] = item['ipa']
    r['vi'] = item['vi']
    r['status'] = 'reviewed'

with open('scratch/b33_r09_p1.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r09_p1.json OK")
