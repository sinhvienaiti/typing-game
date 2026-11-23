import json

items = [
  {"id": "lex.en.200k.064603", "hw": "klicks", "pos": "noun", "ipa": "/klɪks/", "vi": "ki-lô-mét (tiếng lóng quân sự)"},
  {"id": "lex.en.200k.064604", "hw": "landholdings", "pos": "noun", "ipa": "/ˈlændˌhoʊldɪŋz/", "vi": "khu đất thuộc quyền sở hữu tư nhân"},
  {"id": "lex.en.200k.064605", "hw": "lanthanides", "pos": "noun", "ipa": "/ˈlænθəˌnaɪdz/", "vi": "nhóm nguyên tố đất hiếm họ Lantan"},
  {"id": "lex.en.200k.064606", "hw": "lightwoods", "pos": "noun", "ipa": "/ˈlaɪtwʊdz/", "vi": "cây keo gỗ đen quý miền đông Úc"},
  {"id": "lex.en.200k.064607", "hw": "limnologies", "pos": "noun", "ipa": "/lɪmˈnɑːlədʒiz/", "vi": "ngành thủy sinh học hồ ao nước ngọt"},
  {"id": "lex.en.200k.064608", "hw": "liniments", "pos": "noun", "ipa": "/ˈlɪnəmənts/", "vi": "dầu cao xoa bóp giảm đau nhức cơ"},
  {"id": "lex.en.200k.064609", "hw": "loblollies", "pos": "noun", "ipa": "/ˈlɑːblɑːliz/", "vi": "cháo đặc thô xưa; thông đầm lầy Mỹ"},
  {"id": "lex.en.200k.064610", "hw": "mankier", "pos": "adj", "ipa": "/ˈmæŋkiər/", "vi": "bẩn thỉu nhớp nhúa khó chịu hơn"},
  {"id": "lex.en.200k.064611", "hw": "mankiest", "pos": "adj", "ipa": "/ˈmæŋkiɪst/", "vi": "bẩn thỉu nhớp nhúa tồi tàn nhất"},
  {"id": "lex.en.200k.064612", "hw": "meddlers", "pos": "noun", "ipa": "/ˈmɛdlərz/", "vi": "kẻ hay tọc mạch xen vào việc người"},
  {"id": "lex.en.200k.064613", "hw": "mentalisms", "pos": "noun", "ipa": "/ˈmɛntəˌlɪzəmz/", "vi": "thuyết duy tâm; thuật đọc suy nghĩ"},
  {"id": "lex.en.200k.064614", "hw": "militiamen", "pos": "noun", "ipa": "/məˈlɪʃəmən/", "vi": "chiến sĩ dân quân địa phương"},
  {"id": "lex.en.200k.064615", "hw": "mispronunciations", "pos": "noun", "ipa": "/ˌmɪsprəˌnʌnsiˈeɪʃənz/", "vi": "lỗi phát âm sai chuẩn từ vựng"},
  {"id": "lex.en.200k.064616", "hw": "mohos", "pos": "noun", "ipa": "/ˈmoʊhoʊz/", "vi": "mặt ranh giới Moho; chim mật ong"},
  {"id": "lex.en.200k.064617", "hw": "moisturised", "pos": "verb", "ipa": "/ˈmɔɪstʃəraɪzd/", "vi": "đã dưỡng ẩm cấp ẩm cho da (Anh)"},
  {"id": "lex.en.200k.064618", "hw": "moisturises", "pos": "verb", "ipa": "/ˈmɔɪstʃəraɪzɪz/", "vi": "dưỡng ẩm làm mềm mịn da (Anh)"},
  {"id": "lex.en.200k.064619", "hw": "moisturising", "pos": "verb", "ipa": "/ˈmɔɪstʃəraɪzɪŋ/", "vi": "đang dưỡng ẩm làm dịu làn da (Anh)"},
  {"id": "lex.en.200k.064620", "hw": "munchers", "pos": "noun", "ipa": "/ˈmʌntʃərz/", "vi": "người hay thú nhai ngấu nghiến giòn"},
  {"id": "lex.en.200k.064621", "hw": "negligees", "pos": "noun", "ipa": "/ˌnɛɡləˈʒeɪz/", "vi": "váy áo ngủ lụa ren mỏng phụ nữ"},
  {"id": "lex.en.200k.064622", "hw": "ngus", "pos": "noun", "ipa": "/ˌɛnˌdʒiːˈjuːz/", "vi": "bệnh viêm niệu đạo không do lậu NGU"},
  {"id": "lex.en.200k.064623", "hw": "offerors", "pos": "noun", "ipa": "/ˈɔːfərərz/", "vi": "bên đưa ra lời đề nghị giao kết"},
  {"id": "lex.en.200k.064624", "hw": "offertories", "pos": "noun", "ipa": "/ˈɔːfərˌtɔːriz/", "vi": "nghi lễ dâng lễ vật trong nhà thờ"},
  {"id": "lex.en.200k.064625", "hw": "ovipositors", "pos": "noun", "ipa": "/ˌoʊvəˈpɑːzətərz/", "vi": "cơ quan ống đẻ trứng của côn trùng"},
  {"id": "lex.en.200k.064626", "hw": "panipats", "pos": "noun", "ipa": "/ˌpɑːnɪˈpɑːts/", "vi": "chiến trường lịch sử Panipat Ấn Độ"},
  {"id": "lex.en.200k.064627", "hw": "parkinsonisms", "pos": "noun", "ipa": "/ˈpɑːrkɪnsəˌnɪzəmz/", "vi": "hội chứng run cứng kiểu Parkinson"},
  {"id": "lex.en.200k.064628", "hw": "pedlars", "pos": "noun", "ipa": "/ˈpɛdlərz/", "vi": "người bán hàng rong dạo phố (Anh)"},
  {"id": "lex.en.200k.064629", "hw": "pfalzes", "pos": "noun", "ipa": "/pfɑːltsɪz/", "vi": "vùng lịch sử Pfalz ở miền tây Đức"},
  {"id": "lex.en.200k.064630", "hw": "piemontes", "pos": "noun", "ipa": "/piˈɛmɔːnteɪz/", "vi": "vùng Piedmont tây bắc nước Ý"},
  {"id": "lex.en.200k.064631", "hw": "pimplier", "pos": "adj", "ipa": "/ˈpɪmpliər/", "vi": "nhiều mụn nhọt trứng cá hơn"},
  {"id": "lex.en.200k.064632", "hw": "pimpliest", "pos": "adj", "ipa": "/ˈpɪmpliɪst/", "vi": "nhiều mụn nhọt trứng cá nổi nhất"},
  {"id": "lex.en.200k.064633", "hw": "pinatubos", "pos": "noun", "ipa": "/ˌpiːnəˈtuːboʊz/", "vi": "núi lửa Pinatubo ở Philippines"},
  {"id": "lex.en.200k.064634", "hw": "plasticizers", "pos": "noun", "ipa": "/ˈplæstəˌsaɪzərz/", "vi": "chất hóa dẻo tăng độ mềm uốn nhựa"},
  {"id": "lex.en.200k.064635", "hw": "pneumonitides", "pos": "noun", "ipa": "/ˌnuːməˈnaɪtədiːz/", "vi": "chứng bệnh viêm mô phổi dị ứng"},
  {"id": "lex.en.200k.064636", "hw": "pokier", "pos": "adj", "ipa": "/ˈpoʊkiər/", "vi": "chậm chạp lề mề hơn; chật chội hơn"},
  {"id": "lex.en.200k.064637", "hw": "pokiest", "pos": "adj", "ipa": "/ˈpoʊkiɪst/", "vi": "chậm chạp lề mề nhất; tù túng nhất"},
  {"id": "lex.en.200k.064638", "hw": "polytetrafluoroethylenes", "pos": "noun", "ipa": "/ˌpɑːliˌtɛtrəˌflʊroʊˈɛθəliːnz/", "vi": "nhựa chống dính chịu nhiệt Teflon"},
  {"id": "lex.en.200k.064639", "hw": "refinished", "pos": "verb", "ipa": "/ˌriːˈfɪnɪʃt/", "vi": "đã đánh bóng sơn phủ lại bề mặt"},
  {"id": "lex.en.200k.064640", "hw": "refinishes", "pos": "verb", "ipa": "/ˌriːˈfɪnɪʃɪz/", "vi": "tân trang sơn phủ bóng lại đồ gỗ"},
  {"id": "lex.en.200k.064641", "hw": "refinishing", "pos": "verb", "ipa": "/ˌriːˈfɪnɪʃɪŋ/", "vi": "đang sơn sửa đánh bóng lại đồ gỗ"},
  {"id": "lex.en.200k.064642", "hw": "resealed", "pos": "verb", "ipa": "/ˌriːˈsiːld/", "vi": "đã niêm phong lại; bịt kín lại"},
  {"id": "lex.en.200k.064643", "hw": "resealing", "pos": "verb", "ipa": "/ˌriːˈsiːlɪŋ/", "vi": "đang dán niêm phong bịt kín lại"},
  {"id": "lex.en.200k.064644", "hw": "reseals", "pos": "verb", "ipa": "/ˌriːˈsiːlz/", "vi": "niêm phong lại; đóng kín lại"},
  {"id": "lex.en.200k.064645", "hw": "rooiboses", "pos": "noun", "ipa": "/ˈrɔɪbɑːsɪz/", "vi": "trà hồng trà thảo mộc Nam Phi"},
  {"id": "lex.en.200k.064646", "hw": "roundworms", "pos": "noun", "ipa": "/ˈraʊndwɜːrmz/", "vi": "giun tròn ký sinh đường tiêu hóa"},
  {"id": "lex.en.200k.064647", "hw": "sachsens", "pos": "noun", "ipa": "/ˈzɑːksənz/", "vi": "bang lịch sử Sachsen ở nước Đức"},
  {"id": "lex.en.200k.064648", "hw": "satraps", "pos": "noun", "ipa": "/ˈseɪtræps/", "vi": "tổng trấn địa phương Ba Tư cổ đại"},
  {"id": "lex.en.200k.064649", "hw": "seanads", "pos": "noun", "ipa": "/ˈʃænədz/", "vi": "Thượng viện trong quốc hội Ireland"},
  {"id": "lex.en.200k.064650", "hw": "standpipes", "pos": "noun", "ipa": "/ˈstændpaɪps/", "vi": "trụ ống nước đứng chữa cháy; ống áp"},
  {"id": "lex.en.200k.064651", "hw": "stevedores", "pos": "noun", "ipa": "/ˈstiːvəˌdɔːrz/", "vi": "công nhân bốc xếp hàng hóa tàu biển"},
  {"id": "lex.en.200k.064652", "hw": "strasbergs", "pos": "noun", "ipa": "/ˈstrɑːsbɜːrɡz/", "vi": "đạo diễn diễn xuất Lee Strasberg"},
  {"id": "lex.en.200k.064653", "hw": "striates", "pos": "verb", "ipa": "/ˈstraɪeɪts/", "vi": "khía rãnh mảnh; tạo vân sọc nhỏ"},
  {"id": "lex.en.200k.064654", "hw": "striating", "pos": "verb", "ipa": "/ˈstraɪeɪtɪŋ/", "vi": "đang khía rãnh mảnh tạo vân sọc"},
  {"id": "lex.en.200k.064655", "hw": "tattletales", "pos": "noun", "ipa": "/ˈtætəlˌteɪlz/", "vi": "kẻ hay mách lẻo tố cáo bạn bè"},
  {"id": "lex.en.200k.064656", "hw": "tearaways", "pos": "noun", "ipa": "/ˈtɛərəweɪz/", "vi": "thanh niên ngỗ ngược bốc đồng (Anh)"},
  {"id": "lex.en.200k.064657", "hw": "tiptops", "pos": "noun", "ipa": "/ˈtɪptɑːps/", "vi": "đỉnh cao tuyệt hảo nhất; hạng nhất"},
  {"id": "lex.en.200k.064658", "hw": "tokays", "pos": "noun", "ipa": "/toʊˈkeɪz/", "vi": "rượu vang ngọt quý Tokaj Hungary"},
  {"id": "lex.en.200k.064659", "hw": "trachomas", "pos": "noun", "ipa": "/trəˈkoʊməz/", "vi": "bệnh đau mắt hột truyền nhiễm mạn"},
  {"id": "lex.en.200k.064660", "hw": "transferabilities", "pos": "noun", "ipa": "/ˌtrænsfərəˈbɪlətiz/", "vi": "tính có thể chuyển nhượng sang tên"},
  {"id": "lex.en.200k.064661", "hw": "trapezii", "pos": "noun", "ipa": "/trəˈpiːziaɪ/", "vi": "cơ thang vùng cổ vai lưng trên"},
  {"id": "lex.en.200k.064662", "hw": "tuckahoes", "pos": "noun", "ipa": "/ˈtʌkəˌhoʊz/", "vi": "củ nấm phục linh Mỹ tuckahoe"},
  {"id": "lex.en.200k.064663", "hw": "unbinding", "pos": "verb", "ipa": "/ʌnˈbaɪndɪŋ/", "vi": "đang tháo dây trói; gỡ ràng buộc"},
  {"id": "lex.en.200k.064664", "hw": "unbinds", "pos": "verb", "ipa": "/ʌnˈbaɪndz/", "vi": "cởi trói buộc; tháo rời gáy sách"},
  {"id": "lex.en.200k.064665", "hw": "underbosses", "pos": "noun", "ipa": "/ˈʌndərˌbɔːsɪz/", "vi": "phó trùm quyền lực trong băng đảng"},
  {"id": "lex.en.200k.064666", "hw": "vibraphones", "pos": "noun", "ipa": "/ˈvaɪbrəˌfoʊnz/", "vi": "nhạc cụ gõ thanh rung vibraphone"},
  {"id": "lex.en.200k.064667", "hw": "wolfsbanes", "pos": "noun", "ipa": "/ˈwʊlfsbeɪnz/", "vi": "cây ô đầu hoa tím chứa độc tố mạnh"},
  {"id": "lex.en.200k.064668", "hw": "yellowcakes", "pos": "noun", "ipa": "/ˈjɛloʊkeɪks/", "vi": "bột oxit urani cô đặc làm hạt nhân"},
  {"id": "lex.en.200k.064669", "hw": "adenosine deaminase", "pos": "phrase", "ipa": "/əˈdɛnəsiːn diˈæməneɪs/", "vi": "enzym chuyển hóa miễn dịch tế bào"},
  {"id": "lex.en.200k.064670", "hw": "aleksandr sergeyevich pushkin", "pos": "phrase", "ipa": "/ˌɑːlɪkˈsɑːndər ˈpʊʃkɪn/", "vi": "đại thi hào nước Nga Pushkin"},
  {"id": "lex.en.200k.064671", "hw": "altay mountains", "pos": "phrase", "ipa": "/ɑːlˈtaɪ ˈmaʊntənz/", "vi": "dãy núi Altai ở khu vực Trung Á"},
  {"id": "lex.en.200k.064672", "hw": "armata corsa", "pos": "phrase", "ipa": "/ɑːrˈmɑːtə ˈkɔːrsə/", "vi": "nhóm ly khai Armata Corsa đảo Corse"},
  {"id": "lex.en.200k.064673", "hw": "bohemian waxwing", "pos": "phrase", "ipa": "/boʊˈhiːmiən ˈwækswɪŋ/", "vi": "chim cánh sáp rừng lạnh phương Bắc"},
  {"id": "lex.en.200k.064674", "hw": "canopic jar", "pos": "phrase", "ipa": "/kəˈnoʊpɪk dʒɑːr/", "vi": "bình đựng nội tạng ướp xác Ai Cập"},
  {"id": "lex.en.200k.064675", "hw": "cantabrian mountains", "pos": "phrase", "ipa": "/kænˈteɪbriən ˈmaʊntənz/", "vi": "dãy núi Cantabria bắc Tây Ban Nha"},
  {"id": "lex.en.200k.064676", "hw": "cape verde escudo", "pos": "phrase", "ipa": "/keɪp vɜːrd ɛˈskuːduː/", "vi": "đồng tiền escudo nước Cabo Verde"},
  {"id": "lex.en.200k.064677", "hw": "cassia marginata", "pos": "phrase", "ipa": "/ˈkæʃə ˌmɑːrdʒəˈneɪtə/", "vi": "cây muồng hoa đỏ rực vùng Nam Á"},
  {"id": "lex.en.200k.064678", "hw": "commissaire maigret", "pos": "phrase", "ipa": "/ˌkɑːmɪˈsɛər mɛˈɡreɪ/", "vi": "thanh tra thám tử Jules Maigret"},
  {"id": "lex.en.200k.064679", "hw": "constantin brancusi", "pos": "phrase", "ipa": "/ˌkɑːnstænˈtiːn brænˈkuːʃ/", "vi": "nhà điêu khắc Romania Brâncuși"},
  {"id": "lex.en.200k.064680", "hw": "dhobi itch", "pos": "phrase", "ipa": "/ˈdoʊbi ɪtʃ/", "vi": "bệnh nấm hắc lào vùng bẹn (Ấn Độ)"},
  {"id": "lex.en.200k.064681", "hw": "donets basin", "pos": "phrase", "ipa": "/doʊˈnɛts ˈbeɪsən/", "vi": "lưu vực mỏ than công nghiệp Donbas"},
  {"id": "lex.en.200k.064682", "hw": "family fabaceae", "pos": "phrase", "ipa": "/ˈfæməli fəˈbeɪsiˌiː/", "vi": "họ thực vật cây họ Đậu Fabaceae"},
  {"id": "lex.en.200k.064683", "hw": "fluorescein isocyanate", "pos": "phrase", "ipa": "/flʊˈrɛsiːn ˌaɪsoʊˈsaɪəneɪt/", "vi": "chất nhuộm phát huỳnh quang y sinh"},
  {"id": "lex.en.200k.064684", "hw": "fraxinus nigra", "pos": "phrase", "ipa": "/ˈfræksɪnəs ˈnaɪɡrə/", "vi": "cây tần bì đen đan rổ vùng Bắc Mỹ"},
  {"id": "lex.en.200k.064685", "hw": "genus bacteroides", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌbæktəˈrɔɪdiːz/", "vi": "chi vi khuẩn kỵ khí Bacteroides"},
  {"id": "lex.en.200k.064686", "hw": "genus colchicum", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈkɑːltʃɪkəm/", "vi": "chi cây hoa nghệ tây thu Colchicum"},
  {"id": "lex.en.200k.064687", "hw": "genus coreopsis", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌkɔːriˈɑːpsɪs/", "vi": "chi hoa cúc mắt vàng Coreopsis"},
  {"id": "lex.en.200k.064688", "hw": "genus cyclopes", "pos": "phrase", "ipa": "/ˈdʒiːnəs saɪˈkloʊpiːz/", "vi": "chi thú ăn kiến lùn tơ Cyclopes"},
  {"id": "lex.en.200k.064689", "hw": "genus egeria", "pos": "phrase", "ipa": "/ˈdʒiːnəs ɪˈdʒɪriə/", "vi": "chi rong thủy sinh đuôi chó Egeria"},
  {"id": "lex.en.200k.064690", "hw": "genus laminaria", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌlæməˈnɛriə/", "vi": "chi tảo bẹ nâu lớn Laminaria"},
  {"id": "lex.en.200k.064691", "hw": "genus linum", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈlaɪnəm/", "vi": "chi cây lanh lấy sợi và hạt Linum"},
  {"id": "lex.en.200k.064692", "hw": "genus mytilus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈmɪtələs/", "vi": "chi con vẹm xanh vỏ đen ăn ngon"},
  {"id": "lex.en.200k.064693", "hw": "genus prosopis", "pos": "phrase", "ipa": "/ˈdʒiːnəs prəˈsoʊpɪs/", "vi": "chi cây gỗ gai chịu hạn mesquite"},
  {"id": "lex.en.200k.064694", "hw": "genus pythium", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈpɪθiəm/", "vi": "chi nấm thủy mi gây thối rễ cây"},
  {"id": "lex.en.200k.064695", "hw": "giant coreopsis", "pos": "phrase", "ipa": "/ˈdʒaɪənt ˌkɔːriˈɑːpsɪs/", "vi": "cây cúc thân gỗ lớn California"},
  {"id": "lex.en.200k.064696", "hw": "hill myna", "pos": "phrase", "ipa": "/hɪl ˈmaɪnə/", "vi": "chim nhồng biết nhại tiếng người"},
  {"id": "lex.en.200k.064697", "hw": "iris germanica", "pos": "phrase", "ipa": "/ˈaɪrɪs dʒɜːrˈmænɪkə/", "vi": "cây hoa diên vĩ râu tím châu Âu"},
  {"id": "lex.en.200k.064698", "hw": "isere river", "pos": "phrase", "ipa": "/iˈzɛər ˈrɪvər/", "vi": "dòng sông Isère vùng đông nam Pháp"},
  {"id": "lex.en.200k.064699", "hw": "jimson weed", "pos": "phrase", "ipa": "/ˈdʒɪmsən wiːd/", "vi": "cây cà độc dược hoa trắng chứa độc"},
  {"id": "lex.en.200k.064700", "hw": "judgement in personam", "pos": "phrase", "ipa": "/ˈdʒʌdʒmənt ɪn pərˈsoʊnəm/", "vi": "phán quyết ràng buộc cá nhân (Anh)"},
  {"id": "lex.en.200k.064701", "hw": "judgment in personam", "pos": "phrase", "ipa": "/ˈdʒʌdʒmənt ɪn pərˈsoʊnəm/", "vi": "phán quyết ràng buộc cá nhân bị đơn"},
  {"id": "lex.en.200k.064702", "hw": "karel capek", "pos": "phrase", "ipa": "/ˈkɑːrəl ˈtʃɑːpɛk/", "vi": "nhà văn Séc tác giả từ robot Čapek"}
]

with open('scratch/b33_r10_raw_p2.json') as f:
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

with open('scratch/b33_r10_p2.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r10_p2.json OK")
