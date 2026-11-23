import json

items = [
  {"id": "lex.en.200k.060903", "hw": "boaters", "pos": "noun", "ipa": "/ˈboʊtərz/", "vi": "mũ cói rơm phẳng; người chèo thuyền"},
  {"id": "lex.en.200k.060904", "hw": "borosilicates", "pos": "noun", "ipa": "/ˌbɔːroʊˈsɪləkeɪts/", "vi": "thủy tinh borosilicat chịu nhiệt"},
  {"id": "lex.en.200k.060905", "hw": "bosporuses", "pos": "noun", "ipa": "/ˈbɑːspərəsɪz/", "vi": "eo biển chiến lược Bosphorus"},
  {"id": "lex.en.200k.060906", "hw": "bourgognes", "pos": "noun", "ipa": "/bʊərˈɡɔːnjəz/", "vi": "vùng rượu vang Bourgogne của Pháp"},
  {"id": "lex.en.200k.060907", "hw": "campaniles", "pos": "noun", "ipa": "/ˌkæmpəˈniːliz/", "vi": "tháp chuông độc lập kiến trúc Ý"},
  {"id": "lex.en.200k.060908", "hw": "chassed", "pos": "verb", "ipa": "/ʃæˈseɪd/", "vi": "đã nhảy bước trượt lướt chassé"},
  {"id": "lex.en.200k.060909", "hw": "chasses", "pos": "noun", "ipa": "/ʃæˈseɪz/", "vi": "bước nhảy trượt ba nhịp chassé"},
  {"id": "lex.en.200k.060910", "hw": "chassing", "pos": "verb", "ipa": "/ʃæˈseɪɪŋ/", "vi": "đang nhảy bước lướt trượt chassé"},
  {"id": "lex.en.200k.060911", "hw": "coiffed", "pos": "verb", "ipa": "/kwɑːft/", "vi": "đã làm tóc; chải tạo kiểu tóc đẹp"},
  {"id": "lex.en.200k.060912", "hw": "coiffing", "pos": "verb", "ipa": "/ˈkwɑːfɪŋ/", "vi": "đang chải vấn tạo kiểu tóc cầu kỳ"},
  {"id": "lex.en.200k.060913", "hw": "coifs", "pos": "noun", "ipa": "/kwɑːfs/", "vi": "mũ trùm đầu cổ; kiểu tóc vấn"},
  {"id": "lex.en.200k.060914", "hw": "croakers", "pos": "noun", "ipa": "/ˈkroʊkərz/", "vi": "loài cá đù; ếch nhái kêu ộp oạp"},
  {"id": "lex.en.200k.060915", "hw": "culexes", "pos": "noun", "ipa": "/ˈkjuːlɛksɪz/", "vi": "chi muỗi vằn truyền bệnh Culex"},
  {"id": "lex.en.200k.060916", "hw": "culices", "pos": "noun", "ipa": "/ˈkjuːlɪsiːz/", "vi": "các loài muỗi nâu chi Culex"},
  {"id": "lex.en.200k.060917", "hw": "cultists", "pos": "noun", "ipa": "/ˈkʌltɪsts/", "vi": "tín đồ cuồng tín giáo phái dị đoan"},
  {"id": "lex.en.200k.060918", "hw": "cyclamens", "pos": "noun", "ipa": "/ˈsɪkləmənz/", "vi": "cây hoa anh thảo tiên khách lai"},
  {"id": "lex.en.200k.060919", "hw": "declarers", "pos": "noun", "ipa": "/dɪˈklɛərərz/", "vi": "người khai báo; tay đánh bài chính"},
  {"id": "lex.en.200k.060920", "hw": "deimoses", "pos": "noun", "ipa": "/ˈdaɪməsɪz/", "vi": "vệ tinh Deimos; thần kinh hoàng"},
  {"id": "lex.en.200k.060921", "hw": "derringers", "pos": "noun", "ipa": "/ˈdɛrɪndʒərz/", "vi": "súng lục bỏ túi mini Derringer"},
  {"id": "lex.en.200k.060922", "hw": "didions", "pos": "noun", "ipa": "/ˈdɪdiənz/", "vi": "nữ nhà văn Mỹ Joan Didion"},
  {"id": "lex.en.200k.060923", "hw": "digitalizations", "pos": "noun", "ipa": "/ˌdɪdʒɪtələˈzeɪʃənz/", "vi": "sự số hóa; phép trị bệnh digitalis"},
  {"id": "lex.en.200k.060924", "hw": "discontinuances", "pos": "noun", "ipa": "/ˌdɪskənˈtɪnjuənsɪz/", "vi": "sự ngừng kiện tụng; sự gián đoạn"},
  {"id": "lex.en.200k.060925", "hw": "dles", "pos": "noun", "ipa": "/diː ɛl iːz/", "vi": "bệnh lupus ban đỏ dạng đĩa DLE"},
  {"id": "lex.en.200k.060926", "hw": "drydocked", "pos": "verb", "ipa": "/ˈdraɪdɑːkt/", "vi": "đã đưa tàu lên ụ khô để sửa chữa"},
  {"id": "lex.en.200k.060927", "hw": "drydocking", "pos": "verb", "ipa": "/ˈdraɪdɑːkɪŋ/", "vi": "đang đưa tàu vào ụ cạn bảo dưỡng"},
  {"id": "lex.en.200k.060928", "hw": "drydocks", "pos": "noun", "ipa": "/ˈdraɪdɑːks/", "vi": "ụ tàu khô đóng sửa chữa tàu thủy"},
  {"id": "lex.en.200k.060929", "hw": "dukedoms", "pos": "noun", "ipa": "/ˈduːkdəmz/", "vi": "công quốc; tước vị công tước"},
  {"id": "lex.en.200k.060930", "hw": "elutions", "pos": "noun", "ipa": "/ɪˈluːʃənz/", "vi": "sự rửa giải tách sắc ký hóa học"},
  {"id": "lex.en.200k.060931", "hw": "emollients", "pos": "noun", "ipa": "/ɪˈmɑːliənts/", "vi": "chất làm mềm da; kem dưỡng dịu da"},
  {"id": "lex.en.200k.060932", "hw": "encases", "pos": "verb", "ipa": "/ɪnˈkeɪsɪz/", "vi": "bọc kín trong vỏ; bao bọc bảo vệ"},
  {"id": "lex.en.200k.060933", "hw": "encasing", "pos": "verb", "ipa": "/ɪnˈkeɪsɪŋ/", "vi": "đang bọc vỏ kín; lồng vào hộp vỏ"},
  {"id": "lex.en.200k.060934", "hw": "engrams", "pos": "noun", "ipa": "/ˈɛnɡræmz/", "vi": "dấu vết ký ức lưu trong mô não"},
  {"id": "lex.en.200k.060935", "hw": "falchions", "pos": "noun", "ipa": "/ˈfɔːltʃənz/", "vi": "thanh đoản đao lưỡi rộng cong nhẹ"},
  {"id": "lex.en.200k.060936", "hw": "fenugreeks", "pos": "noun", "ipa": "/ˈfɛnjʊɡriːks/", "vi": "cây cỏ cà ri thảo mộc hạt thơm"},
  {"id": "lex.en.200k.060937", "hw": "ferbers", "pos": "noun", "ipa": "/ˈfɜːrbərz/", "vi": "nữ nhà văn Mỹ Edna Ferber"},
  {"id": "lex.en.200k.060938", "hw": "forefeet", "pos": "noun", "ipa": "/ˈfɔːrfiːt/", "vi": "đôi chân trước của loài thú"},
  {"id": "lex.en.200k.060939", "hw": "gatefolds", "pos": "noun", "ipa": "/ˈɡeɪtfoʊldz/", "vi": "trang gấp mở rộng trong sách báo"},
  {"id": "lex.en.200k.060940", "hw": "gaurs", "pos": "noun", "ipa": "/ɡaʊərz/", "vi": "loài bò tót rừng khổng lồ châu Á"},
  {"id": "lex.en.200k.060941", "hw": "globetrotters", "pos": "noun", "ipa": "/ˈɡloʊbtrɑːtərz/", "vi": "người ưa chu du khắp hoàn cầu"},
  {"id": "lex.en.200k.060942", "hw": "hagiographies", "pos": "noun", "ipa": "/ˌhæɡiˈɑːɡrəfiz/", "vi": "tiểu sử thánh nhân; văn ca tụng quá"},
  {"id": "lex.en.200k.060943", "hw": "hearers", "pos": "noun", "ipa": "/ˈhɪərərz/", "vi": "người lắng nghe; khán thính giả"},
  {"id": "lex.en.200k.060944", "hw": "heimdalls", "pos": "noun", "ipa": "/ˈheɪmdɑːlz/", "vi": "thần canh gác cầu vồng Heimdall"},
  {"id": "lex.en.200k.060945", "hw": "hellions", "pos": "noun", "ipa": "/ˈhɛljənz/", "vi": "đứa trẻ ngỗ ngược; kẻ gây rối loạn"},
  {"id": "lex.en.200k.060946", "hw": "homegirls", "pos": "noun", "ipa": "/ˈhoʊmɡɜːrlz/", "vi": "cô bạn gái cùng khu phố thân thiết"},
  {"id": "lex.en.200k.060947", "hw": "hypotensives", "pos": "noun", "ipa": "/ˌhaɪpoʊˈtɛnsɪvz/", "vi": "thuốc hạ huyết áp; người tụt áp"},
  {"id": "lex.en.200k.060948", "hw": "ilexes", "pos": "noun", "ipa": "/ˈaɪlɛksɪz/", "vi": "chi cây nhựa ruồi lá bóng quả đỏ"},
  {"id": "lex.en.200k.060949", "hw": "ingreses", "pos": "noun", "ipa": "/ˈæ̃ɡrəz/", "vi": "họa sĩ cổ điển Pháp Jean Ingres"},
  {"id": "lex.en.200k.060950", "hw": "jagannaths", "pos": "noun", "ipa": "/ˈdʒʌɡərnɑːts/", "vi": "thần Jagannath Ấn Độ giáo; cỗ xe"},
  {"id": "lex.en.200k.060951", "hw": "javans", "pos": "noun", "ipa": "/ˈdʒɑːvənz/", "vi": "người bản địa đảo Java Indonesia"},
  {"id": "lex.en.200k.060952", "hw": "judaicas", "pos": "noun", "ipa": "/dʒuːˈdeɪɪkəz/", "vi": "văn vật truyền thống Do Thái giáo"},
  {"id": "lex.en.200k.060953", "hw": "kameezes", "pos": "noun", "ipa": "/kəˈmiːzɪz/", "vi": "áo dài truyền thống kameez Nam Á"},
  {"id": "lex.en.200k.060954", "hw": "kaundas", "pos": "noun", "ipa": "/kɑːˈʊndəz/", "vi": "tổng thống đầu tiên Zambia Kaunda"},
  {"id": "lex.en.200k.060955", "hw": "kebles", "pos": "noun", "ipa": "/ˈkiːbəlz/", "vi": "nhà thơ mục sư Anh John Keble"},
  {"id": "lex.en.200k.060956", "hw": "lantanas", "pos": "noun", "ipa": "/lænˈtɑːnəz/", "vi": "cây hoa ngũ sắc bông ổi sặc sỡ"},
  {"id": "lex.en.200k.060957", "hw": "laughers", "pos": "noun", "ipa": "/ˈlæfərz/", "vi": "người hay cười; trận thắng dễ dàng"},
  {"id": "lex.en.200k.060958", "hw": "lederhosens", "pos": "noun", "ipa": "/ˈleɪdərˌhoʊzənz/", "vi": "quần yếm da ngắn truyền thống Đức"},
  {"id": "lex.en.200k.060959", "hw": "lenards", "pos": "noun", "ipa": "/ˈleɪnɑːrdz/", "vi": "nhà vật lý Nobel Philipp Lenard"},
  {"id": "lex.en.200k.060960", "hw": "levellers", "pos": "noun", "ipa": "/ˈlɛvələrz/", "vi": "phái bình quyền Levellers nước Anh"},
  {"id": "lex.en.200k.060961", "hw": "lumberyards", "pos": "noun", "ipa": "/ˈlʌmbərjɑːrdz/", "vi": "bãi kho chứa bán gỗ xẻ xây dựng"},
  {"id": "lex.en.200k.060962", "hw": "lycopenes", "pos": "noun", "ipa": "/ˈlaɪkəpiːnz/", "vi": "sắc tố đỏ lycopene trong cà chua"},
  {"id": "lex.en.200k.060963", "hw": "lydians", "pos": "noun", "ipa": "/ˈlɪdiənz/", "vi": "người dân xứ cổ đại Lydia"},
  {"id": "lex.en.200k.060964", "hw": "lysenkos", "pos": "noun", "ipa": "/lɪˈsɛŋkoʊz/", "vi": "nhà nông học Liên Xô Lysenko"},
  {"id": "lex.en.200k.060965", "hw": "maitreyas", "pos": "noun", "ipa": "/maɪˈtreɪəz/", "vi": "Đức Phật Di Lặc vị lai Phật giáo"},
  {"id": "lex.en.200k.060966", "hw": "mansis", "pos": "noun", "ipa": "/ˈmɑːnsiz/", "vi": "người bản địa Mansi vùng Siberia"},
  {"id": "lex.en.200k.060967", "hw": "mcalesters", "pos": "noun", "ipa": "/məˈkælɪstərz/", "vi": "thành phố McAlester bang Oklahoma"},
  {"id": "lex.en.200k.060968", "hw": "musicologists", "pos": "noun", "ipa": "/ˌmjuːzɪˈkɑːlədʒɪsts/", "vi": "nhà âm nhạc học nghiên cứu lý luận"},
  {"id": "lex.en.200k.060969", "hw": "narcans", "pos": "noun", "ipa": "/ˈnɑːrkænz/", "vi": "thuốc giải độc quá liều Narcan"},
  {"id": "lex.en.200k.060970", "hw": "ndebeles", "pos": "noun", "ipa": "/ˌɛndəˈbiːliz/", "vi": "người tộc Ndebele miền nam châu Phi"},
  {"id": "lex.en.200k.060971", "hw": "nervas", "pos": "noun", "ipa": "/ˈnɜːrvəz/", "vi": "Hoàng đế La Mã cổ đại Nerva"},
  {"id": "lex.en.200k.060972", "hw": "nighties", "pos": "noun", "ipa": "/ˈnaɪtiz/", "vi": "váy đầm ngủ mỏng mặc ban đêm"},
  {"id": "lex.en.200k.060973", "hw": "octahedra", "pos": "noun", "ipa": "/ˌɑːktəˈhiːdrə/", "vi": "khối hình tám mặt đều bát diện"},
  {"id": "lex.en.200k.060974", "hw": "octahedrons", "pos": "noun", "ipa": "/ˌɑːktəˈhiːdrənz/", "vi": "hình khối bát diện tám mặt phẳng"},
  {"id": "lex.en.200k.060975", "hw": "papillomas", "pos": "noun", "ipa": "/ˌpæpɪˈloʊməz/", "vi": "khối u nhú lành tính ở da niêm mạc"},
  {"id": "lex.en.200k.060976", "hw": "papillomata", "pos": "noun", "ipa": "/ˌpæpɪˈloʊmətə/", "vi": "nhiều khối u nhú lành tính trên da"},
  {"id": "lex.en.200k.060977", "hw": "perianths", "pos": "noun", "ipa": "/ˈpɛriænθs/", "vi": "bao hoa gồm đài và tràng hoa"},
  {"id": "lex.en.200k.060978", "hw": "philologists", "pos": "noun", "ipa": "/fɪˈlɑːlədʒɪsts/", "vi": "nhà ngữ văn học nghiên cứu cổ ngữ"},
  {"id": "lex.en.200k.060979", "hw": "playbills", "pos": "noun", "ipa": "/ˈpleɪbɪlz/", "vi": "tờ áp phích chương trình vở kịch"},
  {"id": "lex.en.200k.060980", "hw": "pomos", "pos": "noun", "ipa": "/ˈpoʊmoʊz/", "vi": "tộc người bản địa Pomo California"},
  {"id": "lex.en.200k.060981", "hw": "prostrations", "pos": "noun", "ipa": "/prɑːˈstreɪʃənz/", "vi": "sự kiệt sức suy sụp; lễ phủ phục"},
  {"id": "lex.en.200k.060982", "hw": "pushcarts", "pos": "noun", "ipa": "/ˈpʊʃkɑːrts/", "vi": "xe đẩy hàng rong bằng tay hai bánh"},
  {"id": "lex.en.200k.060983", "hw": "rami", "pos": "noun", "ipa": "/ˈreɪmaɪ/", "vi": "nhánh xương hàm; nhánh thần kinh"},
  {"id": "lex.en.200k.060984", "hw": "ramuses", "pos": "noun", "ipa": "/ˈreɪməsɪz/", "vi": "nhánh xương hàm; nhánh mô sinh học"},
  {"id": "lex.en.200k.060985", "hw": "rastafarians", "pos": "noun", "ipa": "/ˌræstəˈfɛriənz/", "vi": "tín đồ đạo Rastafari Jamaica"},
  {"id": "lex.en.200k.060986", "hw": "reanimates", "pos": "verb", "ipa": "/riːˈænɪmeɪts/", "vi": "làm hồi sinh lại; truyền sức sống"},
  {"id": "lex.en.200k.060987", "hw": "reanimating", "pos": "verb", "ipa": "/riːˈænɪmeɪtɪŋ/", "vi": "đang hồi sinh lại; phục hồi sự sống"},
  {"id": "lex.en.200k.060988", "hw": "renins", "pos": "noun", "ipa": "/ˈriːnɪnz/", "vi": "men renin điều hòa huyết áp thận"},
  {"id": "lex.en.200k.060989", "hw": "reshooted", "pos": "verb", "ipa": "/riːˈʃʊt/", "vi": "đã quay phim lại cảnh quay bị hỏng"},
  {"id": "lex.en.200k.060990", "hw": "reshooting", "pos": "verb", "ipa": "/riːˈʃuːtɪŋ/", "vi": "đang quay phim lại; đâm chồi mới"},
  {"id": "lex.en.200k.060991", "hw": "reshoots", "pos": "verb", "ipa": "/riːˈʃuːts/", "vi": "quay lại cảnh phim; chụp ảnh lại"},
  {"id": "lex.en.200k.060992", "hw": "ribands", "pos": "noun", "ipa": "/ˈrɪbəndz/", "vi": "dải ruy-băng lụa trang trí cổ điển"},
  {"id": "lex.en.200k.060993", "hw": "scrublands", "pos": "noun", "ipa": "/ˈskrʌblændz/", "vi": "vùng đất hoang mọc đầy cây bụi thấp"},
  {"id": "lex.en.200k.060994", "hw": "semifinalists", "pos": "noun", "ipa": "/ˌsɛmiˈfaɪnəlɪsts/", "vi": "vận động viên lọt vào vòng bán kết"},
  {"id": "lex.en.200k.060995", "hw": "sexualized", "pos": "verb", "ipa": "/ˈsɛkʃuəlaɪzd/", "vi": "đã gợi dục hóa; gắn tính dục vào"},
  {"id": "lex.en.200k.060996", "hw": "sexualizes", "pos": "verb", "ipa": "/ˈsɛkʃuəlaɪzɪz/", "vi": "tình dục hóa; làm mang tính gợi dục"},
  {"id": "lex.en.200k.060997", "hw": "sexualizing", "pos": "verb", "ipa": "/ˈsɛkʃuəlaɪzɪŋ/", "vi": "đang tình dục hóa; đang gợi dục hóa"},
  {"id": "lex.en.200k.060998", "hw": "shopaholics", "pos": "noun", "ipa": "/ˌʃɑːpəˈhɑːlɪks/", "vi": "người nghiện mua sắm mất kiểm soát"},
  {"id": "lex.en.200k.060999", "hw": "shoplifted", "pos": "verb", "ipa": "/ˈʃɑːplɪftɪd/", "vi": "đã ăn trộm đồ bày bán ở cửa hàng"},
  {"id": "lex.en.200k.061000", "hw": "shoplifts", "pos": "verb", "ipa": "/ˈʃɑːplɪfts/", "vi": "ăn cắp vặt hàng hóa trong siêu thị"},
  {"id": "lex.en.200k.061001", "hw": "sikas", "pos": "noun", "ipa": "/ˈsiːkəz/", "vi": "loài hươu sao chấm trắng Đông Á"},
  {"id": "lex.en.200k.061002", "hw": "sleepwalked", "pos": "verb", "ipa": "/ˈsliːpwɔːkt/", "vi": "đã đi mộng du trong khi ngủ say"}
]

with open('scratch/b33_r02_raw_p5.json') as f:
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

with open('scratch/b33_r02_p5.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 2 Part 5 validated and written successfully.")
