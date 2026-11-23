import json

items = [
  {"id": "lex.en.200k.061503", "hw": "overplaying", "pos": "verb", "ipa": "/ˌoʊvərˈpleɪɪŋ/", "vi": "đang diễn quá lố; đang làm quá đà"},
  {"id": "lex.en.200k.061504", "hw": "overplays", "pos": "verb", "ipa": "/ˌoʊvərˈpleɪz/", "vi": "diễn quá lố đà; đánh giá quá cao"},
  {"id": "lex.en.200k.061505", "hw": "papooses", "pos": "noun", "ipa": "/pəˈpuːsɪz/", "vi": "trẻ sơ sinh da đỏ; túi địu trẻ"},
  {"id": "lex.en.200k.061506", "hw": "passbooks", "pos": "noun", "ipa": "/ˈpæsbʊks/", "vi": "sổ tiết kiệm giao dịch ngân hàng"},
  {"id": "lex.en.200k.061507", "hw": "pawpaws", "pos": "noun", "ipa": "/ˈpɔːpɔːz/", "vi": "quả đu đủ dại; quả na Mỹ pawpaw"},
  {"id": "lex.en.200k.061508", "hw": "pedicles", "pos": "noun", "ipa": "/ˈpɛdɪkəlz/", "vi": "cuống nhỏ mô; cung sau đốt sống"},
  {"id": "lex.en.200k.061509", "hw": "photoelectrons", "pos": "noun", "ipa": "/ˌfoʊtoʊɪˈlɛktrɑːnz/", "vi": "quang điện tử giải phóng do sáng"},
  {"id": "lex.en.200k.061510", "hw": "plagioclases", "pos": "noun", "ipa": "/ˈpleɪdʒioʊkleɪsɪz/", "vi": "nhóm khoáng vật fenspat plagiocla"},
  {"id": "lex.en.200k.061511", "hw": "plasticines", "pos": "noun", "ipa": "/ˈplæstəsiːnz/", "vi": "đất sét nặn tạo hình không khô"},
  {"id": "lex.en.200k.061512", "hw": "polyhedrons", "pos": "noun", "ipa": "/ˌpɑːliˈhiːdrənz/", "vi": "hình khối đa diện nhiều mặt phẳng"},
  {"id": "lex.en.200k.061513", "hw": "prebendaries", "pos": "noun", "ipa": "/ˈprɛbəndɛriz/", "vi": "tu sĩ hưởng bổng lộc nhà thờ lớn"},
  {"id": "lex.en.200k.061514", "hw": "preemies", "pos": "noun", "ipa": "/ˈpriːmiz/", "vi": "trẻ sơ sinh đẻ non thiếu tháng"},
  {"id": "lex.en.200k.061515", "hw": "prioresses", "pos": "noun", "ipa": "/ˈpraɪərəsɪz/", "vi": "nữ tu viện trưởng cai quản nữ tu"},
  {"id": "lex.en.200k.061516", "hw": "protractors", "pos": "noun", "ipa": "/proʊˈtræktərz/", "vi": "thước đo góc; cơ duỗi giải phẫu"},
  {"id": "lex.en.200k.061517", "hw": "pushups", "pos": "noun", "ipa": "/ˈpʊʃʌps/", "vi": "động tác tập thể lực chống đẩy"},
  {"id": "lex.en.200k.061518", "hw": "quadrilles", "pos": "noun", "ipa": "/kwɑːˈdrɪlz/", "vi": "điệu nhảy đôi bốn cặp cổ điển"},
  {"id": "lex.en.200k.061519", "hw": "quiffs", "pos": "noun", "ipa": "/kwɪfs/", "vi": "kiểu tóc mái nam vuốt phồng ngược"},
  {"id": "lex.en.200k.061520", "hw": "quintals", "pos": "noun", "ipa": "/ˈkwɪntlz/", "vi": "đơn vị khối lượng tạ (100 kg)"},
  {"id": "lex.en.200k.061521", "hw": "sabots", "pos": "noun", "ipa": "/ˈsæboʊz/", "vi": "đôi guốc gỗ nông dân châu Âu; guốc"},
  {"id": "lex.en.200k.061522", "hw": "salafisms", "pos": "noun", "ipa": "/ˈsɑːləfɪzəmz/", "vi": "phong trào Hồi giáo dòng Salafi"},
  {"id": "lex.en.200k.061523", "hw": "sargassos", "pos": "noun", "ipa": "/sɑːrˈɡæsoʊz/", "vi": "rong mơ tảo nâu trôi nổi biển"},
  {"id": "lex.en.200k.061524", "hw": "savonarolas", "pos": "noun", "ipa": "/ˌsævənəˈroʊləz/", "vi": "tu sĩ cải cách Ý Savonarola"},
  {"id": "lex.en.200k.061525", "hw": "scintillas", "pos": "noun", "ipa": "/sɪnˈtɪləz/", "vi": "chút xíu tia hy vọng; mảy may nhỏ"},
  {"id": "lex.en.200k.061526", "hw": "sherringtons", "pos": "noun", "ipa": "/ˈʃɛrɪŋtənz/", "vi": "nhà sinh lý học Nobel Sherrington"},
  {"id": "lex.en.200k.061527", "hw": "shipmates", "pos": "noun", "ipa": "/ˈʃɪpmeɪts/", "vi": "bạn đồng nghiệp thủy thủ cùng tàu"},
  {"id": "lex.en.200k.061528", "hw": "skagways", "pos": "noun", "ipa": "/ˈskæɡweɪz/", "vi": "cảng du lịch Skagway ở Alaska"},
  {"id": "lex.en.200k.061529", "hw": "spermatogeneses", "pos": "noun", "ipa": "/spərˌmætoʊˈdʒɛnəsɪz/", "vi": "quá trình sinh tạo tinh trùng đực"},
  {"id": "lex.en.200k.061530", "hw": "stripier", "pos": "adj", "ipa": "/ˈstraɪpiər/", "vi": "có nhiều sọc kẻ rõ nét hơn"},
  {"id": "lex.en.200k.061531", "hw": "stripiest", "pos": "adj", "ipa": "/ˈstraɪpiɪst/", "vi": "có nhiều sọc kẻ vằn rõ nét nhất"},
  {"id": "lex.en.200k.061532", "hw": "sustainers", "pos": "noun", "ipa": "/səˈsteɪnərz/", "vi": "người nâng đỡ duy trì; tên lửa đẩy"},
  {"id": "lex.en.200k.061533", "hw": "swazis", "pos": "noun", "ipa": "/ˈswɑːziz/", "vi": "người dân tộc Swazi ở Eswatini"},
  {"id": "lex.en.200k.061534", "hw": "switcheroos", "pos": "noun", "ipa": "/ˌswɪtʃəˈruːz/", "vi": "màn tráo đổi bất ngờ lật kèo"},
  {"id": "lex.en.200k.061535", "hw": "tarbells", "pos": "noun", "ipa": "/ˈtɑːrbɛlz/", "vi": "nữ nhà báo điều tra Ida Tarbell"},
  {"id": "lex.en.200k.061536", "hw": "tegs", "pos": "noun", "ipa": "/tɛɡz/", "vi": "con cừu non hai tuổi năm thứ hai"},
  {"id": "lex.en.200k.061537", "hw": "terrines", "pos": "noun", "ipa": "/təˈriːnz/", "vi": "món pa-tê thịt hầm khuôn gốm Pháp"},
  {"id": "lex.en.200k.061538", "hw": "tetrads", "pos": "noun", "ipa": "/ˈtɛtrædz/", "vi": "nhóm bốn; bộ bốn nhiễm sắc thể"},
  {"id": "lex.en.200k.061539", "hw": "thickeners", "pos": "noun", "ipa": "/ˈθɪkənərz/", "vi": "chất phụ gia làm đặc sánh món ăn"},
  {"id": "lex.en.200k.061540", "hw": "tpns", "pos": "noun", "ipa": "/tiː piː ɛnz/", "vi": "nuôi dưỡng hoàn toàn qua tĩnh mạch"},
  {"id": "lex.en.200k.061541", "hw": "trekkers", "pos": "noun", "ipa": "/ˈtrɛkərz/", "vi": "người leo núi đi bộ đường dài"},
  {"id": "lex.en.200k.061542", "hw": "trolleybuses", "pos": "noun", "ipa": "/ˈtrɑːlibʌsɪz/", "vi": "xe buýt điện lấy điện dây trần"},
  {"id": "lex.en.200k.061543", "hw": "trombonists", "pos": "noun", "ipa": "/trɑːmˈboʊnɪsts/", "vi": "nhạc công thổi kèn đồng trombone"},
  {"id": "lex.en.200k.061544", "hw": "undercoating", "pos": "verb", "ipa": "/ˈʌndərkoʊtɪŋ/", "vi": "đang sơn lớp lót chống gỉ gầm xe"},
  {"id": "lex.en.200k.061545", "hw": "undercoats", "pos": "noun", "ipa": "/ˈʌndərkoʊts/", "vi": "lớp sơn lót nền; lớp lông tơ mịn"},
  {"id": "lex.en.200k.061546", "hw": "wrasses", "pos": "noun", "ipa": "/ˈræsɪz/", "vi": "loài cá bàng chài biển sặc sỡ"},
  {"id": "lex.en.200k.061547", "hw": "zbs", "pos": "noun", "ipa": "/zɛt biːz/", "vi": "đơn vị dung lượng dữ liệu zettabit"},
  {"id": "lex.en.200k.061548", "hw": "zwinglis", "pos": "noun", "ipa": "/ˈtsvɪŋɡliz/", "vi": "nhà cải cách tôn giáo Zwingli"},
  {"id": "lex.en.200k.061549", "hw": "acer japonicum", "pos": "phrase", "ipa": "/ˈeɪsər dʒəˈpɑːnɪkəm/", "vi": "cây phong lá xẻ tán tròn Nhật Bản"},
  {"id": "lex.en.200k.061550", "hw": "altaic language", "pos": "phrase", "ipa": "/ælˈteɪɪk ˈlæŋɡwɪdʒ/", "vi": "ngữ hệ các ngôn ngữ vùng Altai"},
  {"id": "lex.en.200k.061551", "hw": "ankylosing spondylitis", "pos": "phrase", "ipa": "/ˌæŋkəˈloʊsɪŋ ˌspɑːndɪˈlaɪtɪs/", "vi": "bệnh viêm cột sống dính khớp mạn"},
  {"id": "lex.en.200k.061552", "hw": "antoine henri becquerel", "pos": "phrase", "ipa": "/ɑːnˈtwɑːn ɑːnˈri ˌbɛkəˈrɛl/", "vi": "nhà vật lý tìm phóng xạ Becquerel"},
  {"id": "lex.en.200k.061553", "hw": "arachnoid membrane", "pos": "phrase", "ipa": "/əˈræknɔɪd ˈmɛmbreɪn/", "vi": "lớp màng nhện bao bọc não tủy"},
  {"id": "lex.en.200k.061554", "hw": "belly whop", "pos": "phrase", "ipa": "/ˈbɛli wɑːp/", "vi": "cú nhảy lao đập bụng xuống mặt nước"},
  {"id": "lex.en.200k.061555", "hw": "bercy butter", "pos": "phrase", "ipa": "/bɛərˈsi ˈbʌtər/", "vi": "sốt bơ hành rượu vang kiểu Pháp"},
  {"id": "lex.en.200k.061556", "hw": "black marketeer", "pos": "phrase", "ipa": "/blæk ˌmɑːrkəˈtɪər/", "vi": "kẻ đầu cơ buôn lậu ngoài chợ đen"},
  {"id": "lex.en.200k.061557", "hw": "caper spurge", "pos": "phrase", "ipa": "/ˈkeɪpər spɜːrdʒ/", "vi": "cây đại kích hạt giống nụ bạch hoa"},
  {"id": "lex.en.200k.061558", "hw": "cause celebre", "pos": "phrase", "ipa": "/kɔːz səˈlɛbrə/", "vi": "vụ việc gây tranh cãi chấn động"},
  {"id": "lex.en.200k.061559", "hw": "chamfer bit", "pos": "phrase", "ipa": "/ˈtʃæmfər bɪt/", "vi": "mũi phay đánh vát mép cạnh gỗ"},
  {"id": "lex.en.200k.061560", "hw": "chamfer plane", "pos": "phrase", "ipa": "/ˈtʃæmfər pleɪn/", "vi": "chiếc bào thợ mộc chuyên vát cạnh"},
  {"id": "lex.en.200k.061561", "hw": "chian turpentine", "pos": "phrase", "ipa": "/ˈkaɪən ˈtɜːrpəntaɪn/", "vi": "nhựa thơm cây hồ trăn đảo Chios"},
  {"id": "lex.en.200k.061562", "hw": "chicken cacciatore", "pos": "phrase", "ipa": "/ˈtʃɪkɪn ˌkɑːtʃəˈtɔːri/", "vi": "món gà hầm sốt cà chua kiểu Ý"},
  {"id": "lex.en.200k.061563", "hw": "chirk up", "pos": "phrase", "ipa": "/tʃɜːrk ʌp/", "vi": "làm phấn chấn vui vẻ hơn; vui lên"},
  {"id": "lex.en.200k.061564", "hw": "common laburnum", "pos": "phrase", "ipa": "/ˈkɑːmən ləˈbɜːrnəm/", "vi": "cây muồng hoàng yến hoa vàng rũ độc"},
  {"id": "lex.en.200k.061565", "hw": "copepod crustacean", "pos": "phrase", "ipa": "/ˈkoʊpɪpɑːd krʌˈsteɪʃən/", "vi": "loài giáp xác chân chèo phù du nhỏ"},
  {"id": "lex.en.200k.061566", "hw": "corbel arch", "pos": "phrase", "ipa": "/ˈkɔːrbl ɑːrtʃ/", "vi": "kiểu vòm đá xây giật cấp nhô dần"},
  {"id": "lex.en.200k.061567", "hw": "corbel step", "pos": "phrase", "ipa": "/ˈkɔːrbl stɛp/", "vi": "bậc giật cấp đầu hồi mái nhà cổ"},
  {"id": "lex.en.200k.061568", "hw": "corpus luteum", "pos": "phrase", "ipa": "/ˈkɔːrpəs ˈluːtiəm/", "vi": "thể vàng hoàng thể buồng trứng"},
  {"id": "lex.en.200k.061569", "hw": "crape fern", "pos": "phrase", "ipa": "/kreɪp fɜːrn/", "vi": "loài dương xỉ lá nhăn màng mỏng"},
  {"id": "lex.en.200k.061570", "hw": "daddy longlegs", "pos": "phrase", "ipa": "/ˈdædi ˈlɔːŋlɛɡz/", "vi": "con nhện chân dài; ruồi hạc đồng"},
  {"id": "lex.en.200k.061571", "hw": "dame margot fonteyn", "pos": "phrase", "ipa": "/deɪm ˈmɑːrɡoʊ fɑːnˈteɪn/", "vi": "nghệ sĩ ba lê Anh Margot Fonteyn"},
  {"id": "lex.en.200k.061572", "hw": "diacritical mark", "pos": "phrase", "ipa": "/ˌdaɪəˈkrɪtɪkl mɑːrk/", "vi": "dấu phụ âm thanh trên chữ cái viết"},
  {"id": "lex.en.200k.061573", "hw": "eugene ionesco", "pos": "phrase", "ipa": "/juːˈʒɛn iəˈnɛskoʊ/", "vi": "nhà viết kịch Pháp Eugène Ionesco"},
  {"id": "lex.en.200k.061574", "hw": "eysenck personality inventory", "pos": "phrase", "ipa": "/ˈaɪzɛŋk ˌpɜːrsəˈnælɪti ˈɪnvəntɔːri/", "vi": "bài trắc nghiệm nhân cách Eysenck"},
  {"id": "lex.en.200k.061575", "hw": "fidel castro ruz", "pos": "phrase", "ipa": "/fiˈdɛl ˈkæstroʊ ruːs/", "vi": "nhà lãnh đạo Cuba Fidel Castro"},
  {"id": "lex.en.200k.061576", "hw": "fluorocarbon plastic", "pos": "phrase", "ipa": "/ˌflʊəroʊˈkɑːrbən ˈplæstɪk/", "vi": "nhựa dẻo chống dính fluorocarbon"},
  {"id": "lex.en.200k.061577", "hw": "fulminate of mercury", "pos": "phrase", "ipa": "/ˈfʊlmɪneɪt əv ˈmɜːrkjəri/", "vi": "hợp chất kíp nổ thủy ngân fulminat"},
  {"id": "lex.en.200k.061578", "hw": "gambrel roof", "pos": "phrase", "ipa": "/ˈɡæmbrəl ruːf/", "vi": "kiểu mái gãy hai độ dốc kho thóc"},
  {"id": "lex.en.200k.061579", "hw": "genus arethusa", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌærəˈθjuːzə/", "vi": "chi phong lan đầm lầy Arethusa"},
  {"id": "lex.en.200k.061580", "hw": "genus crataegus", "pos": "phrase", "ipa": "/ˈdʒiːnəs krəˈtiːɡəs/", "vi": "chi thực vật cây táo gai sơn tra"},
  {"id": "lex.en.200k.061581", "hw": "genus eira", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈeɪrə/", "vi": "chi thú ăn thịt chồn tayra Eira"},
  {"id": "lex.en.200k.061582", "hw": "genus polygonum", "pos": "phrase", "ipa": "/ˈdʒiːnəs pəˈlɪɡənəm/", "vi": "chi thực vật cây rau răm cây nghể"},
  {"id": "lex.en.200k.061583", "hw": "glen gebhard", "pos": "phrase", "ipa": "/ɡlɛn ˈɡɛbhɑːrd/", "vi": "tác giả giáo sư Mỹ Glen Gebhard"},
  {"id": "lex.en.200k.061584", "hw": "great saphenous vein", "pos": "phrase", "ipa": "/ɡreɪt səˈfiːnəs veɪn/", "vi": "tĩnh mạch hiển lớn của chân người"},
  {"id": "lex.en.200k.061585", "hw": "hans eysenck", "pos": "phrase", "ipa": "/hɑːnz ˈaɪzɛŋk/", "vi": "nhà tâm lý học Anh Hans Eysenck"},
  {"id": "lex.en.200k.061586", "hw": "hoisin sauce", "pos": "phrase", "ipa": "/ˈhɔɪzɪn sɔːs/", "vi": "tương đen ngọt sệt ăn kèm món Á"},
  {"id": "lex.en.200k.061587", "hw": "idiopathic hemochromatosis", "pos": "phrase", "ipa": "/ˌɪdiəˈpæθɪk ˌhiːmoʊˌkroʊməˈtoʊsɪs/", "vi": "bệnh ứ đọng sắt vô căn di truyền"},
  {"id": "lex.en.200k.061588", "hw": "isidor feinstein stone", "pos": "phrase", "ipa": "/ˈɪzɪdɔːr ˈfaɪnstaɪn stoʊn/", "vi": "nhà báo điều tra Mỹ I. F. Stone"},
  {"id": "lex.en.200k.061589", "hw": "isthmus of tehuantepec", "pos": "phrase", "ipa": "/ˈɪsməs əv təˈwɑːntəpɛk/", "vi": "eo đất Tehuantepec ở nam Mexico"},
  {"id": "lex.en.200k.061590", "hw": "juniperus sabina", "pos": "phrase", "ipa": "/dʒuːˈnɪpərəs səˈbaɪnə/", "vi": "cây bách xù Sabina bò thấp châu Âu"},
  {"id": "lex.en.200k.061591", "hw": "kublai kaan", "pos": "phrase", "ipa": "/ˈkuːblaɪ kɑːn/", "vi": "Hoàng đế nhà Nguyên Hốt Tất Liệt"},
  {"id": "lex.en.200k.061592", "hw": "long saphenous vein", "pos": "phrase", "ipa": "/lɔːŋ səˈfiːnəs veɪn/", "vi": "tĩnh mạch hiển dài nông chi dưới"},
  {"id": "lex.en.200k.061593", "hw": "macula lutea", "pos": "phrase", "ipa": "/ˈmækjʊlə ˈluːtiə/", "vi": "điểm vàng nhạy sáng trên võng mạc"},
  {"id": "lex.en.200k.061594", "hw": "magnolia acuminata", "pos": "phrase", "ipa": "/mæɡˈnoʊliə əˌkjuːmɪˈneɪtə/", "vi": "cây mộc lan lá nhọn quả dưa leo"},
  {"id": "lex.en.200k.061595", "hw": "makarios iii", "pos": "phrase", "ipa": "/mɑːˈkɑːriəs ðə θɜːrd/", "vi": "Tổng thống Síp Đức Cha Makarios III"},
  {"id": "lex.en.200k.061596", "hw": "max beerbohm", "pos": "phrase", "ipa": "/mæks ˈbɪərboʊm/", "vi": "họa sĩ châm biếm Anh Max Beerbohm"},
  {"id": "lex.en.200k.061597", "hw": "mercury fulminate", "pos": "phrase", "ipa": "/ˈmɜːrkjəri ˈfʊlmɪneɪt/", "vi": "chất kíp nổ mạnh thủy ngân fulminat"},
  {"id": "lex.en.200k.061598", "hw": "michelangelo buonarroti", "pos": "phrase", "ipa": "/ˌmaɪkəlˈændʒəloʊ ˌbwɔːnɑːˈrɔːti/", "vi": "bậc thầy Phục hưng Michelangelo"},
  {"id": "lex.en.200k.061599", "hw": "musa acuminata", "pos": "phrase", "ipa": "/ˈmjuːzə əˌkjuːmɪˈneɪtə/", "vi": "loài chuối rừng tổ tiên chuối trồng"},
  {"id": "lex.en.200k.061600", "hw": "neckar river", "pos": "phrase", "ipa": "/ˈnɛkɑːr ˈrɪvər/", "vi": "dòng sông Neckar chảy ở tây nam Đức"},
  {"id": "lex.en.200k.061601", "hw": "nicola amati", "pos": "phrase", "ipa": "/nɪˈkoʊlə əˈmɑːti/", "vi": "nghệ nhân làm đàn Ý Nicola Amati"},
  {"id": "lex.en.200k.061602", "hw": "nucleolus organizer", "pos": "phrase", "ipa": "/nuːˈkliːələs ˈɔːrɡənaɪzər/", "vi": "vùng tổ chức hạch nhân trên NST"}
]

with open('scratch/b33_r04_raw_p1.json') as f:
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

with open('scratch/b33_r04_p1.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 4 Part 1 validated and written successfully.")
