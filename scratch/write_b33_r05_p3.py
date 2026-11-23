import json

items = [
  {"id": "lex.en.200k.062203", "hw": "trondheim fiord", "pos": "phrase", "ipa": "/ˈtrɑːndheɪm fjɔːrd/", "vi": "vịnh hẹp Trondheim ở Na Uy"},
  {"id": "lex.en.200k.062204", "hw": "tump over", "pos": "phrase", "ipa": "/tʌmp ˈoʊvər/", "vi": "làm lật úp; đổ nhào lộn xuống"},
  {"id": "lex.en.200k.062205", "hw": "visual percept", "pos": "phrase", "ipa": "/ˈvɪʒuəl ˈpɜːrsɛpt/", "vi": "hình ảnh tri giác nhận thức mắt"},
  {"id": "lex.en.200k.062206", "hw": "wassermann test", "pos": "phrase", "ipa": "/ˈvɑːsərmɑːn tɛst/", "vi": "xét nghiệm giang mai Wassermann"},
  {"id": "lex.en.200k.062207", "hw": "western mugwort", "pos": "phrase", "ipa": "/ˈwɛstərn ˈmʌɡwɜːrt/", "vi": "cây ngải cứu bạc miền tây Bắc Mỹ"},
  {"id": "lex.en.200k.062208", "hw": "western redbud", "pos": "phrase", "ipa": "/ˈwɛstərn ˈrɛdbʌd/", "vi": "cây bụi hoa ban hồng miền tây Mỹ"},
  {"id": "lex.en.200k.062209", "hw": "adducted", "pos": "verb", "ipa": "/əˈdʌktɪd/", "vi": "đã khép vào sát trục cơ thể"},
  {"id": "lex.en.200k.062210", "hw": "adducts", "pos": "noun", "ipa": "/ˈædʌkts/", "vi": "sản phẩm cộng hóa học trực tiếp"},
  {"id": "lex.en.200k.062211", "hw": "afterbirths", "pos": "noun", "ipa": "/ˈæftərbɜːrθs/", "vi": "nhau thai và màng bọc tống ra sau"},
  {"id": "lex.en.200k.062212", "hw": "ahrimans", "pos": "noun", "ipa": "/ˈɑːrəmənz/", "vi": "ác thần bóng tối Ahriman Ba Tư"},
  {"id": "lex.en.200k.062213", "hw": "airedales", "pos": "noun", "ipa": "/ˈɛərdeɪlz/", "vi": "giống chó sục lớn Airedale Anh"},
  {"id": "lex.en.200k.062214", "hw": "ambassadorships", "pos": "noun", "ipa": "/æmˈbæsədərʃɪps/", "vi": "chức vụ và nhiệm kỳ đại sứ"},
  {"id": "lex.en.200k.062215", "hw": "amiodarones", "pos": "noun", "ipa": "/ˌæmiˈoʊdəroʊnz/", "vi": "thuốc chống loạn nhịp amiodarone"},
  {"id": "lex.en.200k.062216", "hw": "archeans", "pos": "noun", "ipa": "/ɑːrˈkiːənz/", "vi": "liên đại Thái Cổ sơ khai địa chất"},
  {"id": "lex.en.200k.062217", "hw": "artaxerxeses", "pos": "noun", "ipa": "/ˌɑːrtəˈzɜːrksiːzɪz/", "vi": "vua Ba Tư cổ đại Artaxerxes"},
  {"id": "lex.en.200k.062218", "hw": "ballistae", "pos": "noun", "ipa": "/bəˈlɪstiː/", "vi": "nỏ bắn đá công thành cổ La Mã"},
  {"id": "lex.en.200k.062219", "hw": "ballistas", "pos": "noun", "ipa": "/bəˈlɪstəz/", "vi": "máy bắn tên đá hạng nặng La Mã"},
  {"id": "lex.en.200k.062220", "hw": "baryons", "pos": "noun", "ipa": "/ˈbɛriɑːnz/", "vi": "hạt hạ nguyên tử nặng baryon"},
  {"id": "lex.en.200k.062221", "hw": "bolzanos", "pos": "noun", "ipa": "/boʊlˈtsɑːnoʊz/", "vi": "nhà toán học Séc Bernard Bolzano"},
  {"id": "lex.en.200k.062222", "hw": "boulezes", "pos": "noun", "ipa": "/buːˈlɛzɪz/", "vi": "nhạc sĩ nhạc trưởng Pierre Boulez"},
  {"id": "lex.en.200k.062223", "hw": "breadbaskets", "pos": "noun", "ipa": "/ˈbrɛdbæskɪts/", "vi": "vựa lúa lương thực; giỏ bánh mì"},
  {"id": "lex.en.200k.062224", "hw": "bugaboos", "pos": "noun", "ipa": "/ˈbʌɡəbuːz/", "vi": "ông kẹ đáng sợ; nỗi ám ảnh vô cớ"},
  {"id": "lex.en.200k.062225", "hw": "cabochons", "pos": "noun", "ipa": "/ˈkæbəʃɑːnz/", "vi": "viên đá quý mài bóng vòm tròn"},
  {"id": "lex.en.200k.062226", "hw": "carabaos", "pos": "noun", "ipa": "/ˌkɑːrəˈbaʊz/", "vi": "loài trâu nước đầm lầy Đông Nam Á"},
  {"id": "lex.en.200k.062227", "hw": "cariocas", "pos": "noun", "ipa": "/ˌkæriˈoʊkəz/", "vi": "cư dân thành phố Rio de Janeiro"},
  {"id": "lex.en.200k.062228", "hw": "chloramphenicols", "pos": "noun", "ipa": "/ˌklɔːræmˈfɛnɪkɑːlz/", "vi": "thuốc kháng sinh chloramphenicol"},
  {"id": "lex.en.200k.062229", "hw": "circlets", "pos": "noun", "ipa": "/ˈsɜːrklɪts/", "vi": "vòng đội đầu quý tộc; nhẫn tròn nhỏ"},
  {"id": "lex.en.200k.062230", "hw": "cloverleafs", "pos": "noun", "ipa": "/ˈkloʊvərliːfs/", "vi": "nút giao thông cầu vượt cỏ ba lá"},
  {"id": "lex.en.200k.062231", "hw": "cloverleaves", "pos": "noun", "ipa": "/ˈkloʊvərliːvz/", "vi": "nút giao thông cầu vượt hình lá"},
  {"id": "lex.en.200k.062232", "hw": "collocations", "pos": "noun", "ipa": "/ˌkɑːləˈkeɪʃənz/", "vi": "cụm từ kết hợp cố định ngôn ngữ"},
  {"id": "lex.en.200k.062233", "hw": "colloquialisms", "pos": "noun", "ipa": "/kəˈloʊkwiəlɪzəmz/", "vi": "cách nói thông tục đời thường"},
  {"id": "lex.en.200k.062234", "hw": "commensals", "pos": "noun", "ipa": "/kəˈmɛnsəlz/", "vi": "sinh vật hội sinh nương tựa"},
  {"id": "lex.en.200k.062235", "hw": "coosas", "pos": "noun", "ipa": "/ˈkuːsəz/", "vi": "dòng sông Coosa ở miền nam Hoa Kỳ"},
  {"id": "lex.en.200k.062236", "hw": "daphnias", "pos": "noun", "ipa": "/ˈdæfniəz/", "vi": "con bọ nước daphnia nuôi cá cảnh"},
  {"id": "lex.en.200k.062237", "hw": "ddis", "pos": "noun", "ipa": "/diː diː aɪz/", "vi": "thuốc kháng HIV didanosine ddI"},
  {"id": "lex.en.200k.062238", "hw": "decalogues", "pos": "noun", "ipa": "/ˈdɛkəlɔːɡz/", "vi": "Mười Điều Răn của Chúa; quy tắc"},
  {"id": "lex.en.200k.062239", "hw": "deckhands", "pos": "noun", "ipa": "/ˈdɛkhændz/", "vi": "thủy thủ làm việc trên boong tàu"},
  {"id": "lex.en.200k.062240", "hw": "democrituses", "pos": "noun", "ipa": "/dɪˈmɑːkrɪtəsɪz/", "vi": "triết gia nguyên tử Democritus"},
  {"id": "lex.en.200k.062241", "hw": "dirhams", "pos": "noun", "ipa": "/ˈdɪərəmz/", "vi": "đơn vị tiền tệ dirham UAE Ma-rốc"},
  {"id": "lex.en.200k.062242", "hw": "docudramas", "pos": "noun", "ipa": "/ˈdɑːkjʊdrɑːməz/", "vi": "phim truyện tái hiện sự kiện thật"},
  {"id": "lex.en.200k.062243", "hw": "dolmans", "pos": "noun", "ipa": "/ˈdoʊlmənz/", "vi": "áo choàng dài cổ điển Thổ Nhĩ Kỳ"},
  {"id": "lex.en.200k.062244", "hw": "drachmae", "pos": "noun", "ipa": "/ˈdrækmiː/", "vi": "đồng tiền cổ drachma của Hy Lạp"},
  {"id": "lex.en.200k.062245", "hw": "drachmas", "pos": "noun", "ipa": "/ˈdrækməz/", "vi": "đồng tiền tệ cũ drachma Hy Lạp"},
  {"id": "lex.en.200k.062246", "hw": "dubyas", "pos": "noun", "ipa": "/ˈdʌbjəz/", "vi": "biệt danh cựu Tổng thống G. W. Bush"},
  {"id": "lex.en.200k.062247", "hw": "dyskinesias", "pos": "noun", "ipa": "/ˌdɪskɪˈniːʒəz/", "vi": "chứng rối loạn vận động cơ bắp"},
  {"id": "lex.en.200k.062248", "hw": "echocardiograms", "pos": "noun", "ipa": "/ˌɛkoʊˈkɑːrdioʊɡræmz/", "vi": "bản ghi hình ảnh siêu âm tim mạch"},
  {"id": "lex.en.200k.062249", "hw": "emigres", "pos": "noun", "ipa": "/ˈɛmɪɡreɪz/", "vi": "người di cư tị nạn chính trị"},
  {"id": "lex.en.200k.062250", "hw": "enls", "pos": "noun", "ipa": "/iː ɛn ɛlz/", "vi": "nút hồng ban do bệnh phong ENL"},
  {"id": "lex.en.200k.062251", "hw": "enzymologies", "pos": "noun", "ipa": "/ˌɛnzaɪˈmɑːlədʒiz/", "vi": "ngành khoa học nghiên cứu enzyme"},
  {"id": "lex.en.200k.062252", "hw": "ethnographers", "pos": "noun", "ipa": "/ɛθˈnɑːɡrəfərz/", "vi": "nhà nghiên cứu dân tộc chí học"},
  {"id": "lex.en.200k.062253", "hw": "fatimahs", "pos": "noun", "ipa": "/ˈfætɪməz/", "vi": "con gái Tiên tri Hồi giáo Fatimah"},
  {"id": "lex.en.200k.062254", "hw": "ferryboats", "pos": "noun", "ipa": "/ˈfɛriboʊts/", "vi": "chiếc phà chuyên chở qua sông biển"},
  {"id": "lex.en.200k.062255", "hw": "flambeaus", "pos": "noun", "ipa": "/flæmˈboʊz/", "vi": "ngọn đuốc sáng; chân nến trang trí"},
  {"id": "lex.en.200k.062256", "hw": "flavonoids", "pos": "noun", "ipa": "/ˈfleɪvənɔɪdz/", "vi": "hợp chất chống oxy hóa flavonoid"},
  {"id": "lex.en.200k.062257", "hw": "flintier", "pos": "adj", "ipa": "/ˈflɪntiər/", "vi": "cứng rắn như đá hơn; lạnh lùng hơn"},
  {"id": "lex.en.200k.062258", "hw": "flintiest", "pos": "adj", "ipa": "/ˈflɪntiɪst/", "vi": "rắn như đá lửa nhất; sắt đá nhất"},
  {"id": "lex.en.200k.062259", "hw": "foveas", "pos": "noun", "ipa": "/ˈfoʊviəz/", "vi": "hố trung tâm điểm vàng võng mạc"},
  {"id": "lex.en.200k.062260", "hw": "freyjas", "pos": "noun", "ipa": "/ˈfreɪəz/", "vi": "nữ thần sắc đẹp Freya Bắc Âu"},
  {"id": "lex.en.200k.062261", "hw": "fundi", "pos": "noun", "ipa": "/ˈfʌndaɪ/", "vi": "đáy cơ quan giải phẫu; chuyên gia"},
  {"id": "lex.en.200k.062262", "hw": "funduses", "pos": "noun", "ipa": "/ˈfʌndəsɪz/", "vi": "vùng đáy nhãn cầu; đáy cơ quan rỗng"},
  {"id": "lex.en.200k.062263", "hw": "grotiuses", "pos": "noun", "ipa": "/ˈɡroʊʃiəsɪz/", "vi": "luật gia quốc tế học Hugo Grotius"},
  {"id": "lex.en.200k.062264", "hw": "guilders", "pos": "noun", "ipa": "/ˈɡɪldərz/", "vi": "đồng tiền cũ guilder của Hà Lan"},
  {"id": "lex.en.200k.062265", "hw": "haematomas", "pos": "noun", "ipa": "/ˌhiːməˈtoʊməz/", "vi": "khối tụ máu bầm dưới mô cơ thể"},
  {"id": "lex.en.200k.062266", "hw": "haematomata", "pos": "noun", "ipa": "/ˌhiːməˈtoʊmətə/", "vi": "các khối máu tụ xuất huyết mô"},
  {"id": "lex.en.200k.062267", "hw": "haganahs", "pos": "noun", "ipa": "/ˌhɑːɡəˈnɑːz/", "vi": "lực lượng tự vệ Haganah Do Thái"},
  {"id": "lex.en.200k.062268", "hw": "hemostases", "pos": "noun", "ipa": "/ˌhiːmoʊˈsteɪsiːz/", "vi": "cơ chế cầm máu ngăn chảy máu"},
  {"id": "lex.en.200k.062269", "hw": "herzbergs", "pos": "noun", "ipa": "/ˈhɜːrtsbɜːrɡz/", "vi": "nhà khoa học Nobel Gerhard Herzberg"},
  {"id": "lex.en.200k.062270", "hw": "hybridisations", "pos": "noun", "ipa": "/ˌhaɪbrɪdaɪˈzeɪʃənz/", "vi": "sự lai giống loài; sự lai hóa gen"},
  {"id": "lex.en.200k.062271", "hw": "immunologists", "pos": "noun", "ipa": "/ˌɪmjʊˈnɑːlədʒɪsts/", "vi": "chuyên gia bác sĩ miễn dịch học"},
  {"id": "lex.en.200k.062272", "hw": "inocula", "pos": "noun", "ipa": "/ɪˈnɑːkjʊlə/", "vi": "mẫu vi sinh cấy; chất tiêm chủng"},
  {"id": "lex.en.200k.062273", "hw": "inoculums", "pos": "noun", "ipa": "/ɪˈnɑːkjʊləmz/", "vi": "dịch cấy vi khuẩn; chế phẩm tiêm"},
  {"id": "lex.en.200k.062274", "hw": "jokesters", "pos": "noun", "ipa": "/ˈdʒoʊkstərz/", "vi": "người hay pha trò trêu chọc đùa vui"},
  {"id": "lex.en.200k.062275", "hw": "kashas", "pos": "noun", "ipa": "/ˈkɑːʃəz/", "vi": "món cháo kiều mạch rang kiểu Nga"},
  {"id": "lex.en.200k.062276", "hw": "keseys", "pos": "noun", "ipa": "/ˈkiːsiz/", "vi": "nhà văn Mỹ Ken Kesey (Bay trên tổ)"},
  {"id": "lex.en.200k.062277", "hw": "koestlers", "pos": "noun", "ipa": "/ˈkɛstlərz/", "vi": "nhà văn nhà báo Arthur Koestler"},
  {"id": "lex.en.200k.062278", "hw": "kotokos", "pos": "noun", "ipa": "/koʊˈtoʊkoʊz/", "vi": "người dân và tiếng Kotoko Trung Phi"},
  {"id": "lex.en.200k.062279", "hw": "levites", "pos": "noun", "ipa": "/ˈliːvaɪts/", "vi": "bộ tộc Lê-vi phụng sự đền Do Thái"},
  {"id": "lex.en.200k.062280", "hw": "literalisms", "pos": "noun", "ipa": "/ˈlɪtərəlɪzəmz/", "vi": "chủ nghĩa hiểu sát nghĩa đen"},
  {"id": "lex.en.200k.062281", "hw": "loudened", "pos": "verb", "ipa": "/ˈlaʊdnd/", "vi": "đã làm vang to hơn; đã rền vang lên"},
  {"id": "lex.en.200k.062282", "hw": "loudening", "pos": "verb", "ipa": "/ˈlaʊdnɪŋ/", "vi": "đang trở nên to tiếng rền vang hơn"},
  {"id": "lex.en.200k.062283", "hw": "loudens", "pos": "verb", "ipa": "/ˈlaʊdnz/", "vi": "làm âm thanh vang to lớn thêm"},
  {"id": "lex.en.200k.062284", "hw": "luoyangs", "pos": "noun", "ipa": "/lwɔːˈjɑːŋz/", "vi": "cố đô lịch sử Lạc Dương Trung Quốc"},
  {"id": "lex.en.200k.062285", "hw": "malrauxes", "pos": "noun", "ipa": "/mælˈroʊz/", "vi": "nhà văn nổi tiếng André Malraux"},
  {"id": "lex.en.200k.062286", "hw": "matais", "pos": "noun", "ipa": "/ˈmɑːtaɪz/", "vi": "cây gỗ thông matai New Zealand"},
  {"id": "lex.en.200k.062287", "hw": "maundies", "pos": "noun", "ipa": "/ˈmɔːndiz/", "vi": "lễ rửa chân thứ Năm Tuần Thánh"},
  {"id": "lex.en.200k.062288", "hw": "melanchthons", "pos": "noun", "ipa": "/məˈlæŋkθənz/", "vi": "nhà thần học Đức Melanchthon"},
  {"id": "lex.en.200k.062289", "hw": "mokes", "pos": "noun", "ipa": "/moʊks/", "vi": "con lừa (từ lóng Anh); người khờ"},
  {"id": "lex.en.200k.062290", "hw": "multiprocessors", "pos": "noun", "ipa": "/ˌmʌltiˈprɑːsɛsərz/", "vi": "máy tính đa bộ vi xử lý song song"},
  {"id": "lex.en.200k.062291", "hw": "ngfs", "pos": "noun", "ipa": "/ɛn dʒiː ɛfs/", "vi": "yếu tố tăng trưởng thần kinh NGF"},
  {"id": "lex.en.200k.062292", "hw": "nightjars", "pos": "noun", "ipa": "/ˈnaɪtdʒɑːrz/", "vi": "loài chim cú muỗi săn mồi ban đêm"},
  {"id": "lex.en.200k.062293", "hw": "nijinskies", "pos": "noun", "ipa": "/nəˈʒɪnskiz/", "vi": "vũ công ba lê Nga Vaslav Nijinsky"},
  {"id": "lex.en.200k.062294", "hw": "niobraras", "pos": "noun", "ipa": "/ˌnaɪəˈbrærəz/", "vi": "con sông Niobrara bang Nebraska"},
  {"id": "lex.en.200k.062295", "hw": "notabilities", "pos": "noun", "ipa": "/ˌnoʊtəˈbɪlətiz/", "vi": "nhân vật trứ danh; điều đáng chú ý"},
  {"id": "lex.en.200k.062296", "hw": "ostomies", "pos": "noun", "ipa": "/ˈɑːstəmiz/", "vi": "phẫu thuật mở thông đường dẫn tạng"},
  {"id": "lex.en.200k.062297", "hw": "palestrinas", "pos": "noun", "ipa": "/ˌpælɪˈstriːnəz/", "vi": "nhà soạn nhạc Phục hưng Palestrina"},
  {"id": "lex.en.200k.062298", "hw": "pavans", "pos": "noun", "ipa": "/pəˈvɑːnz/", "vi": "điệu múa cung đình chậm rãi pavane"},
  {"id": "lex.en.200k.062299", "hw": "paxils", "pos": "noun", "ipa": "/ˈpæksɪlz/", "vi": "thuốc chống trầm cảm lo âu Paxil"},
  {"id": "lex.en.200k.062300", "hw": "pedagogues", "pos": "noun", "ipa": "/ˈpɛdəɡɑːɡz/", "vi": "nhà giáo; giáo viên cổ hủ giáo điều"},
  {"id": "lex.en.200k.062301", "hw": "pelagiuses", "pos": "noun", "ipa": "/pəˈleɪdʒiəsɪz/", "vi": "nhà thần học cổ đại Anh Pelagius"},
  {"id": "lex.en.200k.062302", "hw": "penetrators", "pos": "noun", "ipa": "/ˈpɛnətreɪtərz/", "vi": "đầu đạn xuyên giáp; kẻ xâm nhập vào"}
]

with open('scratch/b33_r05_raw_p3.json') as f:
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

with open('scratch/b33_r05_p3.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 5 Part 3 validated and written successfully.")
