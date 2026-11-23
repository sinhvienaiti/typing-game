import json

items = [
  {"id": "lex.en.200k.059002", "hw": "turkish hizballah", "pos": "phrase", "ipa": "/ˈtɜːrkɪʃ ˌhɪzbəˈlɑː/", "vi": "nhánh Hezbollah tại Thổ Nhĩ Kỳ"},
  {"id": "lex.en.200k.059003", "hw": "unary operation", "pos": "phrase", "ipa": "/ˈjuːnəri ˌɑːpəˈreɪʃən/", "vi": "phép toán một ngôi"},
  {"id": "lex.en.200k.059004", "hw": "urogenital cleft", "pos": "phrase", "ipa": "/ˌjʊroʊˈdʒɛnɪtl klɛft/", "vi": "khe niệu sinh dục"},
  {"id": "lex.en.200k.059005", "hw": "vernier micrometer", "pos": "phrase", "ipa": "/ˈvɜːrniər maɪˈkrɑːmɪtər/", "vi": "thước pan-me có du xích vi sai"},
  {"id": "lex.en.200k.059007", "hw": "western tanager", "pos": "phrase", "ipa": "/ˈwɛstərn ˈtænədʒər/", "vi": "chim hồng y vàng phương Tây"},
  {"id": "lex.en.200k.059008", "hw": "whalebone whale", "pos": "phrase", "ipa": "/ˈweɪlboʊn weɪl/", "vi": "loài cá voi tấm sừng hàm"},
  {"id": "lex.en.200k.059009", "hw": "william styron", "pos": "phrase", "ipa": "/ˈwɪljəm ˈstaɪrən/", "vi": "nhà văn William Styron"},
  {"id": "lex.en.200k.059010", "hw": "aaltos", "pos": "noun", "ipa": "/ˈɑːltoʊz/", "vi": "kiến trúc sư Alvar Aalto"},
  {"id": "lex.en.200k.059011", "hw": "ableisms", "pos": "noun", "ipa": "/ˈeɪbəlɪzəmz/", "vi": "thành kiến với người khuyết tật"},
  {"id": "lex.en.200k.059012", "hw": "analysers", "pos": "noun", "ipa": "/ˈænəlaɪzɚz/", "vi": "máy phân tích dữ liệu"},
  {"id": "lex.en.200k.059013", "hw": "barites", "pos": "noun", "ipa": "/bˈɛraɪts/", "vi": "khoáng vật bari sunfat barit"},
  {"id": "lex.en.200k.059014", "hw": "berberses", "pos": "noun", "ipa": "/bˈɜːrbɚzɪz/", "vi": "người bản địa Berber Bắc Phi"},
  {"id": "lex.en.200k.059015", "hw": "brigands", "pos": "noun", "ipa": "/brˈɪɡəndz/", "vi": "kẻ cướp đường sơn tặc"},
  {"id": "lex.en.200k.059016", "hw": "bristlier", "pos": "adj", "ipa": "/brˈɪsliɚ/", "vi": "lởm chởm gai hơn; dễ cáu bẳn hơn"},
  {"id": "lex.en.200k.059017", "hw": "bristliest", "pos": "adj", "ipa": "/brˈɪsliɪst/", "vi": "lởm chởm gai nhất; dễ cáu nhất"},
  {"id": "lex.en.200k.059018", "hw": "broadleaves", "pos": "noun", "ipa": "/brˈɔːdliːvz/", "vi": "cây thân gỗ tán lá rộng"},
  {"id": "lex.en.200k.059019", "hw": "bullfights", "pos": "noun", "ipa": "/bˈʊlfˌaɪtz/", "vi": "trận đấu bò tót"},
  {"id": "lex.en.200k.059020", "hw": "bursars", "pos": "noun", "ipa": "/bˈɜːrsɚz/", "vi": "viên thủ quỹ trường đại học"},
  {"id": "lex.en.200k.059021", "hw": "busked", "pos": "verb", "ipa": "/bˈʌskt/", "vi": "đã biểu diễn nghệ thuật đường phố"},
  {"id": "lex.en.200k.059022", "hw": "busks", "pos": "verb", "ipa": "/bˈʌsks/", "vi": "biểu diễn nghệ thuật đường phố"},
  {"id": "lex.en.200k.059023", "hw": "bustiers", "pos": "noun", "ipa": "/buːstjˈeɪz/", "vi": "áo nịt cúp ngực không dây"},
  {"id": "lex.en.200k.059024", "hw": "caesiums", "pos": "noun", "ipa": "/sˈiːziəmz/", "vi": "nguyên tố kim loại xê-si"},
  {"id": "lex.en.200k.059025", "hw": "candelas", "pos": "noun", "ipa": "/kændˈiːləz/", "vi": "đơn vị cường độ sáng candela"},
  {"id": "lex.en.200k.059026", "hw": "capons", "pos": "noun", "ipa": "/kˈeɪpɑːnz/", "vi": "gà trống thiến vỗ béo thịt"},
  {"id": "lex.en.200k.059027", "hw": "caribes", "pos": "noun", "ipa": "/kərˈiːbiz/", "vi": "loài cá hổ ăn thịt piranha"},
  {"id": "lex.en.200k.059028", "hw": "cetaceans", "pos": "noun", "ipa": "/sɪtˈeɪʃənz/", "vi": "động vật có vú bộ cá voi"},
  {"id": "lex.en.200k.059029", "hw": "cezannes", "pos": "noun", "ipa": "/seɪzˈɑːnz/", "vi": "danh họa Paul Cézanne"},
  {"id": "lex.en.200k.059030", "hw": "chatterboxes", "pos": "noun", "ipa": "/tʃˈætɚbˌɑksɪz/", "vi": "kẻ ba hoa lắm mồm; người lắm lời"},
  {"id": "lex.en.200k.059031", "hw": "chromites", "pos": "noun", "ipa": "/krˈoʊmaɪts/", "vi": "quặng crômit sắt oxit"},
  {"id": "lex.en.200k.059032", "hw": "circumnavigations", "pos": "noun", "ipa": "/sˌɜːrkəmnˌævɪɡˈeɪʃənz/", "vi": "chuyến đi vòng quanh thế giới"},
  {"id": "lex.en.200k.059033", "hw": "clampdowns", "pos": "noun", "ipa": "/klˈæmpdaʊnz/", "vi": "biện pháp siết chặt kiểm soát"},
  {"id": "lex.en.200k.059034", "hw": "colloids", "pos": "noun", "ipa": "/kˈɑːlɔɪdz/", "vi": "hệ keo hạt lơ lửng"},
  {"id": "lex.en.200k.059035", "hw": "columellae", "pos": "noun", "ipa": "/kˌɑːljʊmˈɛliː/", "vi": "cột trụ giải phẫu nhỏ"},
  {"id": "lex.en.200k.059036", "hw": "columellas", "pos": "noun", "ipa": "/kˌɑːljʊmˈɛləz/", "vi": "trụ vách mũi; cột trụ nhỏ nhụy"},
  {"id": "lex.en.200k.059037", "hw": "compunctions", "pos": "noun", "ipa": "/kəmpˈʌŋkʃənz/", "vi": "sự cắn rứt lương tâm; nỗi ân hận"},
  {"id": "lex.en.200k.059038", "hw": "confectionaries", "pos": "noun", "ipa": "/kənfˈɛkʃənˌɛriz/", "vi": "cửa hàng bán đồ bánh kẹo mứt"},
  {"id": "lex.en.200k.059039", "hw": "corellis", "pos": "noun", "ipa": "/kɔːrˈɛliz/", "vi": "nhạc sĩ Arcangelo Corelli"},
  {"id": "lex.en.200k.059040", "hw": "courgettes", "pos": "noun", "ipa": "/kʊərʒˈɛts/", "vi": "trái bí ngòi xanh vỏ non"},
  {"id": "lex.en.200k.059041", "hw": "czechoslovakians", "pos": "noun", "ipa": "/tʃˌɛkoʊsloʊvˈɑːkiənz/", "vi": "người dân nước Tiệp Khắc"},
  {"id": "lex.en.200k.059042", "hw": "damocleses", "pos": "noun", "ipa": "/dˈæməkliːzɪz/", "vi": "thanh gươm treo tóc Damocles"},
  {"id": "lex.en.200k.059043", "hw": "digitisations", "pos": "noun", "ipa": "/dˌɪdʒɪtəlaɪzˈeɪʃənz/", "vi": "quá trình số hóa tài liệu"},
  {"id": "lex.en.200k.059044", "hw": "dodgsons", "pos": "noun", "ipa": "/dˈɑːdʒsənz/", "vi": "nhà văn Charles Dodgson"},
  {"id": "lex.en.200k.059045", "hw": "doughboys", "pos": "noun", "ipa": "/dˈoʊbɔɪz/", "vi": "lính bộ binh Mỹ trong Thế chiến 1"},
  {"id": "lex.en.200k.059046", "hw": "earthlings", "pos": "noun", "ipa": "/ˈɜːrθlɪŋz/", "vi": "cư dân Trái Đất; người trần"},
  {"id": "lex.en.200k.059047", "hw": "electrocardiograms", "pos": "noun", "ipa": "/ˌɪlˌɛktroʊkˈɑrdiəɡrˌæmz/", "vi": "bản ghi đo điện tâm đồ"},
  {"id": "lex.en.200k.059048", "hw": "epigraphs", "pos": "noun", "ipa": "/ˈɛpɪɡræfs/", "vi": "câu đề từ đầu sách; văn khắc"},
  {"id": "lex.en.200k.059049", "hw": "epitopes", "pos": "noun", "ipa": "/ˈɛpɪtoʊps/", "vi": "vị trí quyết định kháng nguyên"},
  {"id": "lex.en.200k.059050", "hw": "faceplates", "pos": "noun", "ipa": "/fˈeɪspleɪts/", "vi": "mặt bích máy tiện; tấm chắn mặt"},
  {"id": "lex.en.200k.059051", "hw": "fluors", "pos": "noun", "ipa": "/flˈʊərz/", "vi": "khoáng thạch fluorit phát quang"},
  {"id": "lex.en.200k.059052", "hw": "fwses", "pos": "noun", "ipa": "/ˌɛfdʌbəljuːˈɛsɪz/", "vi": "Cơ quan Bảo tồn Cá Động vật hoang"},
  {"id": "lex.en.200k.059053", "hw": "gaborones", "pos": "noun", "ipa": "/ɡˌæbərˈoʊniz/", "vi": "thủ đô Gaborone của Botswana"},
  {"id": "lex.en.200k.059054", "hw": "gangplanks", "pos": "noun", "ipa": "/ɡˈæŋplæŋks/", "vi": "cầu ván bắt lên boong tàu"},
  {"id": "lex.en.200k.059055", "hw": "gilders", "pos": "noun", "ipa": "/ɡˈɪldɚz/", "vi": "thợ thiếp vàng; thợ dát vàng lá"},
  {"id": "lex.en.200k.059056", "hw": "gleaners", "pos": "noun", "ipa": "/ɡlˈiːnɚz/", "vi": "người mót lúa rơi; người lượm lặt"},
  {"id": "lex.en.200k.059057", "hw": "hallucinogens", "pos": "noun", "ipa": "/həlˈuːsɪnədʒənz/", "vi": "chất kích thích gây ảo giác"},
  {"id": "lex.en.200k.059058", "hw": "handmaids", "pos": "noun", "ipa": "/hˈændmeɪdz/", "vi": "người hầu gái; nữ tì tùng phục"},
  {"id": "lex.en.200k.059059", "hw": "harkened", "pos": "verb", "ipa": "/hˈɑːrkənd/", "vi": "đã lắng tai nghe kỹ"},
  {"id": "lex.en.200k.059060", "hw": "harkening", "pos": "verb", "ipa": "/hˈɑːrkənɪŋ/", "vi": "đang lắng tai nghe; hướng về xưa"},
  {"id": "lex.en.200k.059061", "hw": "harkens", "pos": "verb", "ipa": "/hˈɑrkənz/", "vi": "lắng tai nghe; gợi nhắc chuyện xưa"},
  {"id": "lex.en.200k.059062", "hw": "harmoniums", "pos": "noun", "ipa": "/hɑːrmˈoʊniəmz/", "vi": "đàn ống đạp chân harmonium"},
  {"id": "lex.en.200k.059063", "hw": "horneys", "pos": "noun", "ipa": "/hˈɔːrniz/", "vi": "nhà phân tâm học Karen Horney"},
  {"id": "lex.en.200k.059064", "hw": "hotheads", "pos": "noun", "ipa": "/hˈɑːthɛdz/", "vi": "kẻ nóng nảy bốc đồng hấp tấp"},
  {"id": "lex.en.200k.059065", "hw": "husserls", "pos": "noun", "ipa": "/hˈʊsərlz/", "vi": "triết gia hiện tượng học Husserl"},
  {"id": "lex.en.200k.059066", "hw": "immunosuppressions", "pos": "noun", "ipa": "/ɪmjˌuːnoʊsəprˈɛʃənz/", "vi": "sự ức chế hệ miễn dịch"},
  {"id": "lex.en.200k.059067", "hw": "indics", "pos": "noun", "ipa": "/ˈɪndɪks/", "vi": "nhánh ngôn ngữ Ấn-Arya"},
  {"id": "lex.en.200k.059068", "hw": "jerkins", "pos": "noun", "ipa": "/dʒˈɜːrkɪnz/", "vi": "áo chẽn da cộc tay thời xưa"},
  {"id": "lex.en.200k.059069", "hw": "juvenals", "pos": "noun", "ipa": "/dʒˈuːvənəlz/", "vi": "nhà thơ châm biếm Juvenal"},
  {"id": "lex.en.200k.059070", "hw": "kaunases", "pos": "noun", "ipa": "/kˈaʊnəsɪz/", "vi": "thành phố Kaunas ở Litva"},
  {"id": "lex.en.200k.059071", "hw": "kedahs", "pos": "noun", "ipa": "/kˈeɪdɑːz/", "vi": "bang Kedah của Malaysia"},
  {"id": "lex.en.200k.059072", "hw": "kelantans", "pos": "noun", "ipa": "/kəlˈæntænz/", "vi": "bang Kelantan của Malaysia"},
  {"id": "lex.en.200k.059073", "hw": "kropotkins", "pos": "noun", "ipa": "/kroʊpˈɑːtkɪnz/", "vi": "nhà lý luận Pyotr Kropotkin"},
  {"id": "lex.en.200k.059074", "hw": "kutches", "pos": "noun", "ipa": "/kˈʌtʃɪz/", "vi": "chất nhuộm vỏ cây; bao ép vàng lá"},
  {"id": "lex.en.200k.059075", "hw": "leghorns", "pos": "noun", "ipa": "/lˈɛɡhɔrnz/", "vi": "giống gà đẻ trứng Leghorn"},
  {"id": "lex.en.200k.059076", "hw": "ligurias", "pos": "noun", "ipa": "/lɪɡjˈʊəriəz/", "vi": "vùng duyên hải Liguria nước Ý"},
  {"id": "lex.en.200k.059077", "hw": "lockboxes", "pos": "noun", "ipa": "/lˈɑːkbɑːksɪz/", "vi": "hộp kim loại có khóa an toàn"},
  {"id": "lex.en.200k.059078", "hw": "loincloths", "pos": "noun", "ipa": "/lˈɔɪnklɔːθs/", "vi": "mảnh khố đóng che hạ thân"},
  {"id": "lex.en.200k.059079", "hw": "lowbrows", "pos": "noun", "ipa": "/lˈoʊbraʊz/", "vi": "người có thị hiếu bình dân ít học"},
  {"id": "lex.en.200k.059080", "hw": "mackinaws", "pos": "noun", "ipa": "/mˈækənɔːz/", "vi": "áo khoác len dạ ca rô dày"},
  {"id": "lex.en.200k.059081", "hw": "maluses", "pos": "noun", "ipa": "/mˈeɪləsɪz/", "vi": "chi thực vật cây táo tây malus"},
  {"id": "lex.en.200k.059082", "hw": "mamos", "pos": "noun", "ipa": "/mˈɑːmoʊz/", "vi": "loài chim hút mật mamo Hawaii"},
  {"id": "lex.en.200k.059083", "hw": "marginalisations", "pos": "noun", "ipa": "/mˌɑːrdʒɪnəlaɪzˈeɪʃənz/", "vi": "sự đẩy ra bên lề xã hội"},
  {"id": "lex.en.200k.059084", "hw": "matchsticks", "pos": "noun", "ipa": "/mˈætʃstɪks/", "vi": "que diêm quẹt lửa"},
  {"id": "lex.en.200k.059085", "hw": "mdis", "pos": "noun", "ipa": "/ˌɛmdiːˈaɪz/", "vi": "bình xịt định liều hen suyễn"},
  {"id": "lex.en.200k.059086", "hw": "mesoderms", "pos": "noun", "ipa": "/mˈɛzoʊdɜːrmz/", "vi": "lá phôi trung bì giữa"},
  {"id": "lex.en.200k.059087", "hw": "millworks", "pos": "noun", "ipa": "/mˈɪlwɜːrks/", "vi": "đồ mộc gia công thành phẩm"},
  {"id": "lex.en.200k.059088", "hw": "mirabeaus", "pos": "noun", "ipa": "/mˌɪrəbˈoʊz/", "vi": "Bá tước Mirabeau thời Cách mạng"},
  {"id": "lex.en.200k.059089", "hw": "myopathies", "pos": "noun", "ipa": "/maɪˈɑːpəθiz/", "vi": "các chứng bệnh lý thoái hóa cơ"},
  {"id": "lex.en.200k.059090", "hw": "nampas", "pos": "noun", "ipa": "/nˈæmpəz/", "vi": "thành phố Nampa bang Idaho"},
  {"id": "lex.en.200k.059091", "hw": "nihils", "pos": "noun", "ipa": "/nˈaɪhɪlz/", "vi": "hư vô; điều hoàn toàn vô nghĩa"},
  {"id": "lex.en.200k.059092", "hw": "niobes", "pos": "noun", "ipa": "/naɪˈoʊbiz/", "vi": "nàng Niobe hóa đá trong thần thoại"},
  {"id": "lex.en.200k.059093", "hw": "noshed", "pos": "verb", "ipa": "/nˈɑːʃt/", "vi": "đã ăn vặt giữa bữa"},
  {"id": "lex.en.200k.059094", "hw": "noshes", "pos": "noun", "ipa": "/nˈɑːʃɪz/", "vi": "món ăn vặt lót dạ; bữa nhẹ"},
  {"id": "lex.en.200k.059095", "hw": "noshing", "pos": "verb", "ipa": "/nˈɑːʃɪŋ/", "vi": "đang ăn vặt; dùng đồ ăn nhẹ"},
  {"id": "lex.en.200k.059096", "hw": "operands", "pos": "noun", "ipa": "/ˈɑːpərændz/", "vi": "các số toán hạng trong phép tính"},
  {"id": "lex.en.200k.059097", "hw": "oportos", "pos": "noun", "ipa": "/oʊpˈɔːrtoʊz/", "vi": "thành phố cảng Porto Bồ Đào Nha"},
  {"id": "lex.en.200k.059098", "hw": "overcompensated", "pos": "verb", "ipa": "/ˌoʊvərkˈɑːmpənseɪtɪd/", "vi": "đã bù đắp thái quá"},
  {"id": "lex.en.200k.059099", "hw": "overcompensates", "pos": "verb", "ipa": "/ˌoʊvərkˈɑːmpənseɪts/", "vi": "bù đắp thái quá để che lấp"},
  {"id": "lex.en.200k.059100", "hw": "overcompensating", "pos": "verb", "ipa": "/ˌoʊvərkˈɑːmpənseɪtɪŋ/", "vi": "đang bù đắp thái quá"},
  {"id": "lex.en.200k.059101", "hw": "panellists", "pos": "noun", "ipa": "/pˈænəlɪsts/", "vi": "thành viên đoàn chủ tọa toạ đàm"},
  {"id": "lex.en.200k.059102", "hw": "parangs", "pos": "noun", "ipa": "/pˈæræŋz/", "vi": "dao rựa phát cỏ parang Mã Lai"}
]

with open('scratch/b32_r09_raw_p1.json') as f:
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

with open('scratch/b32_r09_p1.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Part 1 validated and written successfully.")
