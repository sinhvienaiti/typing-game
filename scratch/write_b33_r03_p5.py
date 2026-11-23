import json

items = [
  {"id": "lex.en.200k.061403", "hw": "serrate leaf", "pos": "phrase", "ipa": "/ˈsɛrət liːf/", "vi": "chiếc lá có mép khía răng cưa"},
  {"id": "lex.en.200k.061404", "hw": "sir john cockcroft", "pos": "phrase", "ipa": "/sɜːr dʒɑːn ˈkɑːkkrɔːft/", "vi": "nhà vật lý hạt nhân John Cockcroft"},
  {"id": "lex.en.200k.061405", "hw": "superoxide dismutase", "pos": "phrase", "ipa": "/ˌsuːpərˈɑːksaɪd dɪsˈmjuːteɪs/", "vi": "enzyme chống oxy hóa tế bào SOD"},
  {"id": "lex.en.200k.061406", "hw": "tocantins river", "pos": "phrase", "ipa": "/ˌtoʊkənˈtiːnz ˈrɪvər/", "vi": "dòng sông lớn Tocantins Brazil"},
  {"id": "lex.en.200k.061407", "hw": "toothed spurge", "pos": "phrase", "ipa": "/tuːθt spɜːrdʒ/", "vi": "cỏ sữa lá có mép khía răng cưa"},
  {"id": "lex.en.200k.061408", "hw": "tussock bellflower", "pos": "phrase", "ipa": "/ˈtʌsək ˈbɛlflaʊər/", "vi": "cây hoa chuông bụi mọc thành khóm"},
  {"id": "lex.en.200k.061409", "hw": "unacquainted with", "pos": "phrase", "ipa": "/ˌʌnəˈkweɪntɪd wɪð/", "vi": "chưa từng quen biết; xa lạ với"},
  {"id": "lex.en.200k.061410", "hw": "variegated horsetail", "pos": "phrase", "ipa": "/ˈvɛriəɡeɪtɪd ˈhɔːrsteɪl/", "vi": "cây cỏ tháp bút đốt vằn xanh trắng"},
  {"id": "lex.en.200k.061411", "hw": "viola striata", "pos": "phrase", "ipa": "/vaɪˈoʊlə straɪˈeɪtə/", "vi": "cây hoa violet kem sọc tím Bắc Mỹ"},
  {"id": "lex.en.200k.061412", "hw": "water of crystallisation", "pos": "phrase", "ipa": "/ˈwɔːtər əv ˌkrɪstələˈzeɪʃən/", "vi": "nước ngậm kết tinh trong tinh thể"},
  {"id": "lex.en.200k.061413", "hw": "wayfaring tree", "pos": "phrase", "ipa": "/ˈweɪfɛərɪŋ triː/", "vi": "cây bụi tú cầu dại hoa chùm trắng"},
  {"id": "lex.en.200k.061414", "hw": "whirligig beetle", "pos": "phrase", "ipa": "/ˈwɜːrlɪɡɪɡ ˈbiːtl/", "vi": "bọ niềng niễng xoay tròn mặt nước"},
  {"id": "lex.en.200k.061415", "hw": "wilhelm konrad roentgen", "pos": "phrase", "ipa": "/ˈvɪlhɛlm ˈkɑːnræd ˈrɛntɡən/", "vi": "nhà vật lý tìm ra tia X Röntgen"},
  {"id": "lex.en.200k.061416", "hw": "actualized", "pos": "verb", "ipa": "/ˈæktʃuəlaɪzd/", "vi": "đã hiện thực hóa; biến thành thực"},
  {"id": "lex.en.200k.061417", "hw": "albuterols", "pos": "noun", "ipa": "/ælˈbjuːtərɑːlz/", "vi": "thuốc giãn phế quản trị hen suyễn"},
  {"id": "lex.en.200k.061418", "hw": "amaterasus", "pos": "noun", "ipa": "/ˌɑːməteɪˈrɑːsuz/", "vi": "Nữ thần Mặt Trời Amaterasu Nhật"},
  {"id": "lex.en.200k.061419", "hw": "amoys", "pos": "noun", "ipa": "/əˈmɔɪz/", "vi": "thành phố Hạ Môn; tiếng Hạ Môn"},
  {"id": "lex.en.200k.061420", "hw": "anoraks", "pos": "noun", "ipa": "/ˈænəræks/", "vi": "áo khoác mũ chống rét; kẻ lập dị"},
  {"id": "lex.en.200k.061421", "hw": "antigonuses", "pos": "noun", "ipa": "/ænˈtɪɡənəsɪz/", "vi": "tướng kế vị Alexander Antigonus"},
  {"id": "lex.en.200k.061422", "hw": "arminiuses", "pos": "noun", "ipa": "/ɑːrˈmɪniəsɪz/", "vi": "nhà thần học Hà Lan Jacob Arminius"},
  {"id": "lex.en.200k.061423", "hw": "arrowsmiths", "pos": "noun", "ipa": "/ˈæroʊsmɪθs/", "vi": "người thợ chế tác mũi tên cung"},
  {"id": "lex.en.200k.061424", "hw": "atens", "pos": "noun", "ipa": "/ˈɑːtənz/", "vi": "thần đĩa Mặt Trời Aten Ai Cập cổ"},
  {"id": "lex.en.200k.061425", "hw": "audiotapes", "pos": "noun", "ipa": "/ˈɔːdioʊteɪps/", "vi": "cuộn băng cassette ghi âm thanh"},
  {"id": "lex.en.200k.061426", "hw": "australopithecuses", "pos": "noun", "ipa": "/ˌɔːstreɪloʊˈpɪθəkəsɪz/", "vi": "chi vượn người cổ phương nam"},
  {"id": "lex.en.200k.061427", "hw": "azides", "pos": "noun", "ipa": "/ˈeɪzaɪdz/", "vi": "hợp chất muối azua dễ phát nổ"},
  {"id": "lex.en.200k.061428", "hw": "badmouthed", "pos": "verb", "ipa": "/ˈbædmaʊθt/", "vi": "đã nói xấu sau lưng; đã gièm pha"},
  {"id": "lex.en.200k.061429", "hw": "badmouthing", "pos": "verb", "ipa": "/ˈbædmaʊθɪŋ/", "vi": "đang nói xấu gièm pha sau lưng"},
  {"id": "lex.en.200k.061430", "hw": "badmouths", "pos": "verb", "ipa": "/ˈbædmaʊθs/", "vi": "nói xấu sau lưng; gièm pha chê bai"},
  {"id": "lex.en.200k.061431", "hw": "bagmans", "pos": "noun", "ipa": "/ˈbæɡmənz/", "vi": "người chào hàng; tay chân thu tiền"},
  {"id": "lex.en.200k.061432", "hw": "baryshnikovs", "pos": "noun", "ipa": "/bəˈrɪʃnɪkɔːvz/", "vi": "nghệ sĩ múa ba lê Baryshnikov"},
  {"id": "lex.en.200k.061433", "hw": "betaines", "pos": "noun", "ipa": "/ˈbiːtəiːnz/", "vi": "hợp chất sinh học betaine củ cải"},
  {"id": "lex.en.200k.061434", "hw": "borates", "pos": "noun", "ipa": "/ˈbɔːreɪts/", "vi": "hợp chất muối axit boric borat"},
  {"id": "lex.en.200k.061435", "hw": "bourguignons", "pos": "noun", "ipa": "/ˌbʊərɡiːnˈjɔːnz/", "vi": "món bò hầm rượu vang đỏ Pháp"},
  {"id": "lex.en.200k.061436", "hw": "breadcrumbs", "pos": "noun", "ipa": "/ˈbrɛdkrʌmz/", "vi": "vụn bánh mì khô; thanh định hướng"},
  {"id": "lex.en.200k.061437", "hw": "brionies", "pos": "noun", "ipa": "/ˈbraɪəniz/", "vi": "cây dây leo củ độc họ Bầu bí"},
  {"id": "lex.en.200k.061438", "hw": "brollies", "pos": "noun", "ipa": "/ˈbrɑːliz/", "vi": "cây dù; chiếc ô che mưa nắng Anh"},
  {"id": "lex.en.200k.061439", "hw": "brucelloses", "pos": "noun", "ipa": "/ˌbruːsəˈloʊsiːz/", "vi": "bệnh sốt nhiễm khuẩn Brucella"},
  {"id": "lex.en.200k.061440", "hw": "calvinos", "pos": "noun", "ipa": "/kælˈviːnoʊz/", "vi": "nhà văn Ý Italo Calvino"},
  {"id": "lex.en.200k.061441", "hw": "candidiasises", "pos": "noun", "ipa": "/ˌkændɪˈdaɪəsɪsɪz/", "vi": "bệnh nhiễm nấm men Candida"},
  {"id": "lex.en.200k.061442", "hw": "carotenoids", "pos": "noun", "ipa": "/kəˈrɑːtənɔɪdz/", "vi": "sắc tố hữu cơ màu cam carotenoid"},
  {"id": "lex.en.200k.061443", "hw": "centenarians", "pos": "noun", "ipa": "/ˌsɛntəˈnɛriənz/", "vi": "người sống thọ tròn trăm tuổi"},
  {"id": "lex.en.200k.061444", "hw": "chemnitzes", "pos": "noun", "ipa": "/ˈkɛmnɪtsɪz/", "vi": "thành phố Chemnitz miền đông Đức"},
  {"id": "lex.en.200k.061445", "hw": "chichas", "pos": "noun", "ipa": "/ˈtʃiːtʃəz/", "vi": "thức uống ngô lên men vùng Andes"},
  {"id": "lex.en.200k.061446", "hw": "chollas", "pos": "noun", "ipa": "/ˈtʃɔɪjəz/", "vi": "cây xương rồng gai cholla sa mạc"},
  {"id": "lex.en.200k.061447", "hw": "clytemnestras", "pos": "noun", "ipa": "/ˌklaɪtəmˈnɛstrəz/", "vi": "hoàng hậu Hy Lạp cổ Clytemnestra"},
  {"id": "lex.en.200k.061448", "hw": "concessionaires", "pos": "noun", "ipa": "/kənˌsɛʃəˈnɛərz/", "vi": "chủ cửa hàng được nhượng quyền"},
  {"id": "lex.en.200k.061449", "hw": "corregidors", "pos": "noun", "ipa": "/kəˈrɛɡɪdɔːrz/", "vi": "đảo pháo đài Corregidor Manila"},
  {"id": "lex.en.200k.061450", "hw": "crematories", "pos": "noun", "ipa": "/ˈkriːmətɔːriz/", "vi": "lò hỏa táng; nhà hỏa thiêu xác"},
  {"id": "lex.en.200k.061451", "hw": "croesuses", "pos": "noun", "ipa": "/ˈkriːsəsɪz/", "vi": "đại phú hào giàu nứt đố đổ vách"},
  {"id": "lex.en.200k.061452", "hw": "dhows", "pos": "noun", "ipa": "/daʊz/", "vi": "thuyền buồm tam giác Ả Rập dhow"},
  {"id": "lex.en.200k.061453", "hw": "diebacks", "pos": "noun", "ipa": "/ˈdaɪbæks/", "vi": "bệnh khô chết ngọn cành cây trồng"},
  {"id": "lex.en.200k.061454", "hw": "diphenhydramines", "pos": "noun", "ipa": "/ˌdaɪfɛnˈhaɪdrəmiːnz/", "vi": "thuốc kháng dị ứng gây buồn ngủ"},
  {"id": "lex.en.200k.061455", "hw": "discolourations", "pos": "noun", "ipa": "/dɪsˌkʌləˈreɪʃənz/", "vi": "vết ố biến màu; sự phai bạc màu"},
  {"id": "lex.en.200k.061456", "hw": "dromedaries", "pos": "noun", "ipa": "/ˈdrɑːmədɛriz/", "vi": "loài lạc đà một bướu Ả Rập"},
  {"id": "lex.en.200k.061457", "hw": "erythropoietins", "pos": "noun", "ipa": "/ɪˌrɪθroʊˈpɔɪətɪnz/", "vi": "hoóc-môn kích thích tạo hồng cầu"},
  {"id": "lex.en.200k.061458", "hw": "fetishists", "pos": "noun", "ipa": "/ˈfɛtɪʃɪsts/", "vi": "người tôn sùng vật; người ám ảnh"},
  {"id": "lex.en.200k.061459", "hw": "firebugs", "pos": "noun", "ipa": "/ˈfaɪərbʌɡz/", "vi": "kẻ nghiện đốt phá; con bọ cánh lửa"},
  {"id": "lex.en.200k.061460", "hw": "fiscs", "pos": "noun", "ipa": "/fɪsks/", "vi": "ngân khố nhà nước; kho bạc công"},
  {"id": "lex.en.200k.061461", "hw": "fishbones", "pos": "noun", "ipa": "/ˈfɪʃboʊnz/", "vi": "chiếc xương cá; họa tiết xương cá"},
  {"id": "lex.en.200k.061462", "hw": "flakeyer", "pos": "adj", "ipa": "/ˈfleɪkiər/", "vi": "dễ bong vảy hơn; hay thất hẹn hơn"},
  {"id": "lex.en.200k.061463", "hw": "flakeyest", "pos": "adj", "ipa": "/ˈfleɪkiɪst/", "vi": "dễ bong vảy nhất; thất thường nhất"},
  {"id": "lex.en.200k.061464", "hw": "flashcards", "pos": "noun", "ipa": "/ˈflæʃkɑːrdz/", "vi": "thẻ học từ vựng ghi nhớ flashcard"},
  {"id": "lex.en.200k.061465", "hw": "fricatives", "pos": "noun", "ipa": "/ˈfrɪkətɪvz/", "vi": "phụ âm xát phát ra qua khe hẹp"},
  {"id": "lex.en.200k.061466", "hw": "gehennas", "pos": "noun", "ipa": "/ɡəˈhɛnəz/", "vi": "chốn hỏa ngục đày đọa; địa ngục"},
  {"id": "lex.en.200k.061467", "hw": "geisels", "pos": "noun", "ipa": "/ˈɡaɪzəlz/", "vi": "nhà văn thiếu nhi Dr. Seuss Mỹ"},
  {"id": "lex.en.200k.061468", "hw": "geneves", "pos": "noun", "ipa": "/dʒəˈniːvz/", "vi": "thành phố Geneva bên hồ Thụy Sĩ"},
  {"id": "lex.en.200k.061469", "hw": "geodes", "pos": "noun", "ipa": "/ˈdʒiːoʊdz/", "vi": "hốc đá tinh thể thạch anh lấp lánh"},
  {"id": "lex.en.200k.061470", "hw": "glucosides", "pos": "noun", "ipa": "/ˈɡluːkəsaɪdz/", "vi": "hợp chất đường thực vật glucozit"},
  {"id": "lex.en.200k.061471", "hw": "goiters", "pos": "noun", "ipa": "/ˈɡɔɪtərz/", "vi": "bệnh bướu cổ sưng tuyến giáp"},
  {"id": "lex.en.200k.061472", "hw": "gruyeres", "pos": "noun", "ipa": "/ɡruːˈjɛərz/", "vi": "loại phô mai cứng vàng Gruyère"},
  {"id": "lex.en.200k.061473", "hw": "guldens", "pos": "noun", "ipa": "/ˈɡʊldənz/", "vi": "đồng tiền cổ gulden của Hà Lan"},
  {"id": "lex.en.200k.061474", "hw": "highlifes", "pos": "noun", "ipa": "/ˈhaɪlaɪfs/", "vi": "lối sống thượng lưu; nhạc highlife"},
  {"id": "lex.en.200k.061475", "hw": "honiaras", "pos": "noun", "ipa": "/ˌhɑːniˈɑːrəz/", "vi": "thủ đô Honiara quần đảo Solomon"},
  {"id": "lex.en.200k.061476", "hw": "honorariums", "pos": "noun", "ipa": "/ˌɑːnəˈrɛriəmz/", "vi": "khoản tiền thù lao tri ân danh dự"},
  {"id": "lex.en.200k.061477", "hw": "hydrofoils", "pos": "noun", "ipa": "/ˈhaɪdrəfɔɪlz/", "vi": "tàu thủy cánh ngầm lướt sóng nhanh"},
  {"id": "lex.en.200k.061478", "hw": "hypatias", "pos": "noun", "ipa": "/haɪˈpeɪʃəz/", "vi": "nữ triết gia toán học Hypatia"},
  {"id": "lex.en.200k.061479", "hw": "hyponatremias", "pos": "noun", "ipa": "/ˌhaɪpoʊnəˈtriːmiəz/", "vi": "tình trạng hạ nồng độ natri máu"},
  {"id": "lex.en.200k.061480", "hw": "immortalized", "pos": "verb", "ipa": "/ɪˈmɔːrtəlaɪzd/", "vi": "đã làm bất tử; ghi danh muôn đời"},
  {"id": "lex.en.200k.061481", "hw": "infarcts", "pos": "noun", "ipa": "/ˈɪnfɑːrkts/", "vi": "vùng mô hoại tử do tắc mạch máu"},
  {"id": "lex.en.200k.061482", "hw": "interlakens", "pos": "noun", "ipa": "/ˈɪntərlɑːkənz/", "vi": "thị trấn du lịch Interlaken"},
  {"id": "lex.en.200k.061483", "hw": "intermediations", "pos": "noun", "ipa": "/ˌɪntərˌmiːdiˈeɪʃənz/", "vi": "hoạt động trung gian hòa giải"},
  {"id": "lex.en.200k.061484", "hw": "jailors", "pos": "noun", "ipa": "/ˈdʒeɪlərz/", "vi": "người cai ngục canh giữ trại giam"},
  {"id": "lex.en.200k.061485", "hw": "kampongs", "pos": "noun", "ipa": "/ˈkæmpɔːŋz/", "vi": "ngôi làng truyền thống vùng Mã Lai"},
  {"id": "lex.en.200k.061486", "hw": "khamas", "pos": "noun", "ipa": "/ˈkɑːməz/", "vi": "vua tộc trưởng Khama ở Botswana"},
  {"id": "lex.en.200k.061487", "hw": "koans", "pos": "noun", "ipa": "/ˈkoʊɑːnz/", "vi": "công án thiền ngộ đạo Thiền tông"},
  {"id": "lex.en.200k.061488", "hw": "laris", "pos": "noun", "ipa": "/ˈlɑːriz/", "vi": "đơn vị tiền tệ lari nước Gruzia"},
  {"id": "lex.en.200k.061489", "hw": "leatherbacks", "pos": "noun", "ipa": "/ˈlɛðərbæks/", "vi": "loài rùa da biển khổng lồ mai mềm"},
  {"id": "lex.en.200k.061490", "hw": "loonies", "pos": "noun", "ipa": "/ˈluːniz/", "vi": "đồng xu 1 đô Canada; kẻ điên rồ"},
  {"id": "lex.en.200k.061491", "hw": "magnificats", "pos": "noun", "ipa": "/mæɡˈnɪfɪkæts/", "vi": "bài thánh ca Ngợi Khen Đức Mẹ"},
  {"id": "lex.en.200k.061492", "hw": "malthusians", "pos": "noun", "ipa": "/mælˈθuːʒənz/", "vi": "người theo thuyết dân số Malthus"},
  {"id": "lex.en.200k.061493", "hw": "margraves", "pos": "noun", "ipa": "/ˈmɑːrɡreɪvz/", "vi": "chức hầu tước trấn giữ biên cương"},
  {"id": "lex.en.200k.061494", "hw": "misapprehensions", "pos": "noun", "ipa": "/ˌmɪsæprɪˈhɛnʃənz/", "vi": "sự hiểu lầm sai lệch; nỗi lo ngại"},
  {"id": "lex.en.200k.061495", "hw": "mixologies", "pos": "noun", "ipa": "/mɪkˈsɑːlədʒiz/", "vi": "nghệ thuật pha chế rượu cocktail"},
  {"id": "lex.en.200k.061496", "hw": "mortgagees", "pos": "noun", "ipa": "/ˌmɔːrɡəˈdʒiːz/", "vi": "bên nhận thế chấp cho vay tài sản"},
  {"id": "lex.en.200k.061497", "hw": "mundas", "pos": "noun", "ipa": "/ˈmʊndəz/", "vi": "dân tộc bản địa và ngữ hệ Munda Ấn"},
  {"id": "lex.en.200k.061498", "hw": "noblewomen", "pos": "noun", "ipa": "/ˈnoʊblwɪmɪn/", "vi": "phụ nữ thuộc dòng dõi quý tộc"},
  {"id": "lex.en.200k.061499", "hw": "norns", "pos": "noun", "ipa": "/nɔːrnz/", "vi": "ba nữ thần số mệnh Norn Bắc Âu"},
  {"id": "lex.en.200k.061500", "hw": "nureyevs", "pos": "noun", "ipa": "/nʊəˈreɪjəvz/", "vi": "vũ công ba lê huyền thoại Nureyev"},
  {"id": "lex.en.200k.061501", "hw": "occultations", "pos": "noun", "ipa": "/ˌɑːkʌlˈteɪʃənz/", "vi": "hiện tượng thiên thể che khuất nhau"},
  {"id": "lex.en.200k.061502", "hw": "overplayed", "pos": "verb", "ipa": "/ˌoʊvərˈpleɪd/", "vi": "đã diễn xuất lố đà; làm quá mức"}
]

with open('scratch/b33_r03_raw_p5.json') as f:
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

with open('scratch/b33_r03_p5.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 3 Part 5 validated and written successfully.")
