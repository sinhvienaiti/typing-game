import json

items = [
  {"id": "lex.en.200k.060003", "hw": "proudhons", "pos": "noun", "ipa": "/ˈpruːdoʊnz/", "vi": "triết gia vô chính phủ Proudhon"},
  {"id": "lex.en.200k.060004", "hw": "pyrophosphates", "pos": "noun", "ipa": "/ˌpaɪroʊˈfɑːsfeɪts/", "vi": "muối este axit pyrophosphat"},
  {"id": "lex.en.200k.060005", "hw": "racketeered", "pos": "verb", "ipa": "/ˌrækəˈtɪərd/", "vi": "đã hoạt động tống tiền phi pháp"},
  {"id": "lex.en.200k.060006", "hw": "racketeers", "pos": "noun", "ipa": "/ˌrækəˈtɪərz/", "vi": "kẻ tống tiền; trùm buôn gian lận"},
  {"id": "lex.en.200k.060007", "hw": "recencies", "pos": "noun", "ipa": "/ˈriːsənsiz/", "vi": "tính cách gần đây; sự mới xảy ra"},
  {"id": "lex.en.200k.060008", "hw": "recusals", "pos": "noun", "ipa": "/rɪˈkjuːzəlz/", "vi": "sự tự rút lui khỏi vụ án của tòa"},
  {"id": "lex.en.200k.060009", "hw": "rehearings", "pos": "noun", "ipa": "/riːˈhɪərɪŋz/", "vi": "phiên xử lại; sự phúc thẩm lại"},
  {"id": "lex.en.200k.060010", "hw": "rigels", "pos": "noun", "ipa": "/ˈraɪdʒəlz/", "vi": "ngôi sao Rigel chòm sao Lạp Hộ"},
  {"id": "lex.en.200k.060011", "hw": "schoolcrafts", "pos": "noun", "ipa": "/ˈskuːlkræfts/", "vi": "nhà địa lý Henry Schoolcraft"},
  {"id": "lex.en.200k.060012", "hw": "septicaemias", "pos": "noun", "ipa": "/ˌsɛptɪˈsiːmiəz/", "vi": "chứng nhiễm trùng máu nguy kịch"},
  {"id": "lex.en.200k.060013", "hw": "sertralines", "pos": "noun", "ipa": "/ˈsɜːrtrəliːnz/", "vi": "thuốc chống trầm cảm sertraline"},
  {"id": "lex.en.200k.060014", "hw": "shuffleboards", "pos": "noun", "ipa": "/ˈʃʌflbɔːrdz/", "vi": "trò chơi đẩy đĩa trượt trên bàn"},
  {"id": "lex.en.200k.060015", "hw": "skinks", "pos": "noun", "ipa": "/skɪŋks/", "vi": "con thằn lằn bóng đuôi dài"},
  {"id": "lex.en.200k.060016", "hw": "spics", "pos": "noun", "ipa": "/spɪks/", "vi": "từ lăng mạ người gốc Mỹ Latinh"},
  {"id": "lex.en.200k.060017", "hw": "spondylitises", "pos": "noun", "ipa": "/ˌspɑːndɪˈlaɪtɪsɪz/", "vi": "bệnh viêm đốt sống lưng"},
  {"id": "lex.en.200k.060018", "hw": "spotsylvanias", "pos": "noun", "ipa": "/ˌspɑːtsəlˈveɪniəz/", "vi": "vùng đồi Spotsylvania ở Virginia"},
  {"id": "lex.en.200k.060019", "hw": "stieglitzes", "pos": "noun", "ipa": "/ˈstiːɡlɪtsɪz/", "vi": "nhiếp ảnh gia Alfred Stieglitz"},
  {"id": "lex.en.200k.060020", "hw": "substantiations", "pos": "noun", "ipa": "/səbˌstænʃiˈeɪʃənz/", "vi": "chứng cứ xác thực; sự chứng minh"},
  {"id": "lex.en.200k.060021", "hw": "summerhouses", "pos": "noun", "ipa": "/ˈsʌmərhɑʊzɪz/", "vi": "nhà mát nghỉ hè trong vườn"},
  {"id": "lex.en.200k.060022", "hw": "sympathisers", "pos": "noun", "ipa": "/ˈsɪmpəθaɪzərz/", "vi": "người có cảm tình; người ủng hộ"},
  {"id": "lex.en.200k.060023", "hw": "taggers", "pos": "noun", "ipa": "/ˈtæɡərz/", "vi": "người vẽ graffiti; người gắn nhãn"},
  {"id": "lex.en.200k.060024", "hw": "taichungs", "pos": "noun", "ipa": "/taɪˈtʃʊŋz/", "vi": "thành phố Đài Trung ở Đài Loan"},
  {"id": "lex.en.200k.060025", "hw": "tarawas", "pos": "noun", "ipa": "/təˈrɑːwəz/", "vi": "đảo san hô Tarawa ở Kiribati"},
  {"id": "lex.en.200k.060026", "hw": "ticklers", "pos": "noun", "ipa": "/ˈtɪklərz/", "vi": "hồ sơ nhắc việc; câu đố mẹo vui"},
  {"id": "lex.en.200k.060027", "hw": "typhons", "pos": "noun", "ipa": "/ˈtaɪfɑːnz/", "vi": "quái vật thần thoại bão tố Typhon"},
  {"id": "lex.en.200k.060028", "hw": "umayyads", "pos": "noun", "ipa": "/ʊˈmaɪjædz/", "vi": "vương triều Hồi giáo Umayyad"},
  {"id": "lex.en.200k.060029", "hw": "updrafts", "pos": "noun", "ipa": "/ˈʌpdræfts/", "vi": "luồng gió thổi bốc ngược lên cao"},
  {"id": "lex.en.200k.060030", "hw": "velveetas", "pos": "noun", "ipa": "/vɛlˈviːtəz/", "vi": "loại phô mai mềm béo Velveeta"},
  {"id": "lex.en.200k.060031", "hw": "viragoes", "pos": "noun", "ipa": "/vɪˈrɑːɡoʊz/", "vi": "người đàn bà hung dữ chanh chua"},
  {"id": "lex.en.200k.060032", "hw": "wellheads", "pos": "noun", "ipa": "/ˈwɛlhɛdz/", "vi": "miệng giếng khoan dầu; đầu nguồn"},
  {"id": "lex.en.200k.060033", "hw": "wheezier", "pos": "adj", "ipa": "/ˈwiːziər/", "vi": "thở khò khè hơn; hen suyễn hơn"},
  {"id": "lex.en.200k.060034", "hw": "wheeziest", "pos": "adj", "ipa": "/ˈwiːziɪst/", "vi": "thở khò khè nhất; thở dốc nhất"},
  {"id": "lex.en.200k.060035", "hw": "wodens", "pos": "noun", "ipa": "/ˈwoʊdənz/", "vi": "thần chiến tranh tối cao Woden"},
  {"id": "lex.en.200k.060036", "hw": "acquired hemochromatosis", "pos": "phrase", "ipa": "/əˈkwaɪərd ˌhiːmoʊˌkroʊməˈtoʊsɪs/", "vi": "bệnh ứ sắt mô do mắc phải"},
  {"id": "lex.en.200k.060037", "hw": "actinic radiation", "pos": "phrase", "ipa": "/ækˈtɪnɪk ˌreɪdiˈeɪʃən/", "vi": "bức xạ tia quang hóa mặt trời"},
  {"id": "lex.en.200k.060038", "hw": "actinic ray", "pos": "phrase", "ipa": "/ækˈtɪnɪk reɪ/", "vi": "tia quang hóa bức xạ"},
  {"id": "lex.en.200k.060039", "hw": "africanized bee", "pos": "phrase", "ipa": "/ˈæfrɪkənaɪzd biː/", "vi": "ong sát thủ châu Phi lai hung dữ"},
  {"id": "lex.en.200k.060040", "hw": "africanized honey bee", "pos": "phrase", "ipa": "/ˈæfrɪkənaɪzd ˈhʌni biː/", "vi": "ong mật châu Phi hung dữ sát thủ"},
  {"id": "lex.en.200k.060041", "hw": "aletta jacobs", "pos": "phrase", "ipa": "/əˈlɛtə ˈdʒeɪkəbz/", "vi": "nữ bác sĩ Aletta Jacobs Hà Lan"},
  {"id": "lex.en.200k.060042", "hw": "anglesea island", "pos": "phrase", "ipa": "/ˈæŋɡəlsiː ˈaɪlənd/", "vi": "hòn đảo Anglesey ở xứ Wales"},
  {"id": "lex.en.200k.060043", "hw": "antonine wall", "pos": "phrase", "ipa": "/ˈæntənaɪn wɔːl/", "vi": "bức tường thành Antonine Scotland"},
  {"id": "lex.en.200k.060044", "hw": "aplastic anaemia", "pos": "phrase", "ipa": "/eɪˈplæstɪk əˈniːmiə/", "vi": "chứng bệnh thiếu máu bất sản tủy"},
  {"id": "lex.en.200k.060045", "hw": "belleau wood", "pos": "phrase", "ipa": "/bɛˈloʊ wʊd/", "vi": "trận đánh đẫm máu rừng Belleau"},
  {"id": "lex.en.200k.060046", "hw": "canna edulis", "pos": "phrase", "ipa": "/ˈkænə ˈɛdjʊlɪs/", "vi": "cây dong riềng củ ăn được"},
  {"id": "lex.en.200k.060047", "hw": "cantering rhythm", "pos": "phrase", "ipa": "/ˈkæntərɪŋ ˈrɪðəm/", "vi": "tiếng ngựa phi nước kiệu nhịp ba"},
  {"id": "lex.en.200k.060048", "hw": "carolus linnaeus", "pos": "phrase", "ipa": "/kəˈroʊləs lɪˈniːəs/", "vi": "nhà thực vật học Carl Linnaeus"},
  {"id": "lex.en.200k.060049", "hw": "ceiba tree", "pos": "phrase", "ipa": "/ˈseɪbə triː/", "vi": "cây bông gòn nhiệt đới"},
  {"id": "lex.en.200k.060050", "hw": "cinema verite", "pos": "phrase", "ipa": "/ˌsɪnɪmə ˌvɛrɪˈteɪ/", "vi": "phong cách điện ảnh tài liệu thực"},
  {"id": "lex.en.200k.060051", "hw": "class insecta", "pos": "phrase", "ipa": "/klæs ɪnˈsɛktə/", "vi": "lớp động vật Côn trùng lục túc"},
  {"id": "lex.en.200k.060052", "hw": "classic hemochromatosis", "pos": "phrase", "ipa": "/ˈklæsɪk ˌhiːmoʊˌkroʊməˈtoʊsɪs/", "vi": "bệnh ứ đọng sắt di truyền cổ điển"},
  {"id": "lex.en.200k.060053", "hw": "common comfrey", "pos": "phrase", "ipa": "/ˈkɑːmən ˈkʌmfri/", "vi": "cây liên mộc thảo dược hoa chuông"},
  {"id": "lex.en.200k.060054", "hw": "derivational morphology", "pos": "phrase", "ipa": "/ˌdɛrɪˈveɪʃənəl mɔːrˈfɑːlədʒi/", "vi": "ngữ pháp hình thái học phái sinh"},
  {"id": "lex.en.200k.060055", "hw": "explication de texte", "pos": "phrase", "ipa": "/ˌɛksplɪkəˈsjoʊn də ˈtɛkst/", "vi": "phương pháp phân tích kỹ văn bản"},
  {"id": "lex.en.200k.060056", "hw": "ferenc molnar", "pos": "phrase", "ipa": "/ˈfɛrɛnk ˈmoʊlnɑːr/", "vi": "nhà viết kịch Ferenc Molnár"},
  {"id": "lex.en.200k.060057", "hw": "genus helianthus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌhiːliˈænθəs/", "vi": "chi thực vật hoa hướng dương"},
  {"id": "lex.en.200k.060058", "hw": "genus hypericum", "pos": "phrase", "ipa": "/ˈdʒiːnəs haɪˈpɛrɪkəm/", "vi": "chi cây thảo mộc ban âu vàng"},
  {"id": "lex.en.200k.060059", "hw": "gooseneck barnacle", "pos": "phrase", "ipa": "/ˈɡuːsnɛk ˈbɑːrnəkl/", "vi": "con hà ngỗng; đằng hồ cổ ngỗng"},
  {"id": "lex.en.200k.060060", "hw": "gray catbird", "pos": "phrase", "ipa": "/ɡreɪ ˈkætbɜːrd/", "vi": "loài chim nhại mèo xám Bắc Mỹ"},
  {"id": "lex.en.200k.060061", "hw": "grey catbird", "pos": "phrase", "ipa": "/ɡreɪ ˈkætbɜːrd/", "vi": "chim nhại giọng mèo xám Bắc Mỹ"},
  {"id": "lex.en.200k.060062", "hw": "hoi polloi", "pos": "phrase", "ipa": "/ˌhɔɪ pəˈlɔɪ/", "vi": "quần chúng bình dân; giới bình dân"},
  {"id": "lex.en.200k.060063", "hw": "hottentot bread", "pos": "phrase", "ipa": "/ˈhɑːtntɑːt brɛd/", "vi": "cây củ chân voi dại châu Phi"},
  {"id": "lex.en.200k.060064", "hw": "hottentot fig", "pos": "phrase", "ipa": "/ˈhɑːtntɑːt fɪɡ/", "vi": "cây mọng nước sung Hottentot"},
  {"id": "lex.en.200k.060065", "hw": "jean baptiste lully", "pos": "phrase", "ipa": "/ʒɑ̃ː bɑːˈtiːst lyˈli/", "vi": "nhạc trưởng Jean-Baptiste Lully"},
  {"id": "lex.en.200k.060066", "hw": "jules de goncourt", "pos": "phrase", "ipa": "/ʒyːl də ɡɔ̃ˈkuːr/", "vi": "nhà văn Pháp Jules de Goncourt"},
  {"id": "lex.en.200k.060067", "hw": "large crabgrass", "pos": "phrase", "ipa": "/lɑːrdʒ ˈkræbɡræs/", "vi": "cây cỏ gà; cỏ chỉ lá lớn bò lan"},
  {"id": "lex.en.200k.060068", "hw": "mahalia jackson", "pos": "phrase", "ipa": "/məˈheɪliə ˈdʒæksən/", "vi": "nữ hoàng ca nhạc Phúc âm Jackson"},
  {"id": "lex.en.200k.060069", "hw": "multifocal iol", "pos": "phrase", "ipa": "/ˌmʌltiˈfoʊkəl aɪ oʊ ɛl/", "vi": "thủy tinh thể nhân tạo đa tiêu cự"},
  {"id": "lex.en.200k.060070", "hw": "nevil shute", "pos": "phrase", "ipa": "/ˈnɛvəl ʃuːt/", "vi": "tiểu thuyết gia Anh Nevil Shute"},
  {"id": "lex.en.200k.060071", "hw": "nevil shute norway", "pos": "phrase", "ipa": "/ˈnɛvəl ʃuːt ˈnɔːrweɪ/", "vi": "nhà văn phi công Nevil Shute Norway"},
  {"id": "lex.en.200k.060072", "hw": "newel post", "pos": "phrase", "ipa": "/ˈnjuːəl poʊst/", "vi": "trụ lớn đỡ tay vịn chân cầu thang"},
  {"id": "lex.en.200k.060073", "hw": "nucleolar organizer", "pos": "phrase", "ipa": "/nuːˈkliːələr ˈɔːrɡənaɪzər/", "vi": "vùng tổ chức hạch nhân tế bào"},
  {"id": "lex.en.200k.060074", "hw": "osseous tissue", "pos": "phrase", "ipa": "/ˈɑːsiəs ˈtɪʃuː/", "vi": "mô xương cứng của bộ xương"},
  {"id": "lex.en.200k.060075", "hw": "owen wister", "pos": "phrase", "ipa": "/ˈoʊɪn ˈwɪstər/", "vi": "nhà văn truyện cao bồi Owen Wister"},
  {"id": "lex.en.200k.060076", "hw": "permanganate of potash", "pos": "phrase", "ipa": "/pərˈmæŋɡəneɪt əv ˈpɑːtæʃ/", "vi": "thuốc tím pemanganat kali"},
  {"id": "lex.en.200k.060077", "hw": "pingpong table", "pos": "phrase", "ipa": "/ˈpɪŋpɑːŋ ˈteɪbl/", "vi": "bàn đánh bóng bàn tiêu chuẩn"},
  {"id": "lex.en.200k.060078", "hw": "pinon nut", "pos": "phrase", "ipa": "/ˈpɪnjɑːn nʌt/", "vi": "hạt thông ăn được ngọt bùi pinon"},
  {"id": "lex.en.200k.060079", "hw": "pinon pine", "pos": "phrase", "ipa": "/ˈpɪnjɑːn paɪn/", "vi": "cây thông pinon lùn Bắc Mỹ"},
  {"id": "lex.en.200k.060080", "hw": "pinus sylvestris", "pos": "phrase", "ipa": "/ˈpaɪnəs sɪlˈvɛstrɪs/", "vi": "loài thông đỏ thông Scots châu Âu"},
  {"id": "lex.en.200k.060081", "hw": "pouf paste", "pos": "phrase", "ipa": "/puːf peɪst/", "vi": "bột nhào làm bánh su vỏ phồng"},
  {"id": "lex.en.200k.060082", "hw": "prix goncourt", "pos": "phrase", "ipa": "/priː ɡɔ̃ˈkuːr/", "vi": "giải thưởng văn học Goncourt Pháp"},
  {"id": "lex.en.200k.060083", "hw": "probiotic microflora", "pos": "phrase", "ipa": "/ˌproʊbaɪˈɑːtɪk ˈmaɪkroʊˌflɔːrə/", "vi": "hệ lợi khuẩn đường ruột probiotic"},
  {"id": "lex.en.200k.060084", "hw": "quercus laevis", "pos": "phrase", "ipa": "/ˈkwɜːrkəs ˈliːvɪs/", "vi": "cây sồi tây lá nhẵn Bắc Mỹ"},
  {"id": "lex.en.200k.060085", "hw": "quercus palustris", "pos": "phrase", "ipa": "/ˈkwɜːrkəs pəˈlʌstrɪs/", "vi": "loài sồi đầm lầy vỏ bóng Bắc Mỹ"},
  {"id": "lex.en.200k.060086", "hw": "rocky mountain pinon", "pos": "phrase", "ipa": "/ˈrɑːki ˈmaʊntn ˈpɪnjɑːn/", "vi": "loài thông pinon núi Rocky"},
  {"id": "lex.en.200k.060087", "hw": "roentgen ray", "pos": "phrase", "ipa": "/ˈrɛntɡən reɪ/", "vi": "tia X rơnghen bức xạ ion hóa"},
  {"id": "lex.en.200k.060088", "hw": "rubus canadensis", "pos": "phrase", "ipa": "/ˈruːbəs ˌkænəˈdɛnsɪs/", "vi": "cây mâm xôi gai trơn Canada"},
  {"id": "lex.en.200k.060089", "hw": "saddle hackle", "pos": "phrase", "ipa": "/ˈsædl ˈhækl/", "vi": "chùm lông cổ đuôi gà trống làm mồi"},
  {"id": "lex.en.200k.060090", "hw": "salix purpurea", "pos": "phrase", "ipa": "/ˈseɪlɪks pɜːrˈpjʊəriə/", "vi": "cây liễu cành tím đan rổ"},
  {"id": "lex.en.200k.060091", "hw": "smooth crabgrass", "pos": "phrase", "ipa": "/smuːð ˈkræbɡræs/", "vi": "cỏ gà trơn mọc dại sân cỏ"},
  {"id": "lex.en.200k.060092", "hw": "spring peeper", "pos": "phrase", "ipa": "/sprɪŋ ˈpiːpər/", "vi": "loài nhái nhỏ kêu râm ran mùa xuân"},
  {"id": "lex.en.200k.060093", "hw": "striate cortex", "pos": "phrase", "ipa": "/ˈstraɪeɪt ˈkɔːrtɛks/", "vi": "vỏ não thị giác vân sơ cấp"},
  {"id": "lex.en.200k.060094", "hw": "striate vein", "pos": "phrase", "ipa": "/ˈstraɪeɪt veɪn/", "vi": "tĩnh mạch vân dưới đồi não"},
  {"id": "lex.en.200k.060095", "hw": "suffragan bishop", "pos": "phrase", "ipa": "/ˈsʌfrəɡən ˈbɪʃəp/", "vi": "giám mục phụ tá giáo phận"},
  {"id": "lex.en.200k.060096", "hw": "thermosetting compositions", "pos": "phrase", "ipa": "/ˌθɜːrmoʊˈsɛtɪŋ ˌkɑːmpəˈzɪʃənz/", "vi": "vật liệu hợp chất nhựa nhiệt rắn"},
  {"id": "lex.en.200k.060097", "hw": "thermosetting resin", "pos": "phrase", "ipa": "/ˌθɜːrmoʊˈsɛtɪŋ ˈrɛzɪn/", "vi": "nhựa nhiệt rắn không nóng chảy lại"},
  {"id": "lex.en.200k.060098", "hw": "toreador pants", "pos": "phrase", "ipa": "/ˈtɔːriədɔːr pænts/", "vi": "quần lửng bó sát kiểu đấu bò tót"},
  {"id": "lex.en.200k.060099", "hw": "tuberous vetch", "pos": "phrase", "ipa": "/ˈtuːbərəs vɛtʃ/", "vi": "cây đậu vảy củ ngọt ăn được"},
  {"id": "lex.en.200k.060100", "hw": "ultrahigh frequency", "pos": "phrase", "ipa": "/ˌʌltrəˈhaɪ ˈfriːkwənsi/", "vi": "tần số vô tuyến siêu cao UHF"},
  {"id": "lex.en.200k.060101", "hw": "vicomte de chateaubriand", "pos": "phrase", "ipa": "/viːˈkɔ̃ːt də ʃæˌtoʊbriːˈɑ̃ː/", "vi": "Đại văn hào tử tước Chateaubriand"},
  {"id": "lex.en.200k.060102", "hw": "vocative case", "pos": "phrase", "ipa": "/ˈvɑːkətɪv keɪs/", "vi": "hô cách xưng hô ngữ pháp"}
]

with open('scratch/b33_r01_raw_p1.json') as f:
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

with open('scratch/b33_r01_p1.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 1 Part 1 validated and written successfully.")
