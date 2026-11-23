import json

items = [
  {"id": "lex.en.200k.062803", "hw": "malses", "pos": "noun", "ipa": "/ˈmælsɪz/", "vi": "bằng thạc sĩ khoa học thư viện"},
  {"id": "lex.en.200k.062804", "hw": "manumissions", "pos": "noun", "ipa": "/ˌmænjəˈmɪʃənz/", "vi": "sự trả tự do giải phóng nô lệ"},
  {"id": "lex.en.200k.062805", "hw": "masefields", "pos": "noun", "ipa": "/ˈmeɪsfiːldz/", "vi": "thi sĩ hoàng gia Anh John Masefield"},
  {"id": "lex.en.200k.062806", "hw": "misstatements", "pos": "noun", "ipa": "/ˌmɪsˈsteɪtmənts/", "vi": "lời phát biểu sai lệch thông tin"},
  {"id": "lex.en.200k.062807", "hw": "moires", "pos": "noun", "ipa": "/mwɑːˈreɪz/", "vi": "vải lụa dập hoa văn gợn sóng nước"},
  {"id": "lex.en.200k.062808", "hw": "monnets", "pos": "noun", "ipa": "/moʊˈneɪz/", "vi": "chính khách Pháp Jean Monnet"},
  {"id": "lex.en.200k.062809", "hw": "motormen", "pos": "noun", "ipa": "/ˈmoʊtərmən/", "vi": "người lái tàu điện hoặc đầu máy"},
  {"id": "lex.en.200k.062810", "hw": "moultings", "pos": "noun", "ipa": "/ˈmoʊltɪŋz/", "vi": "quá trình thay lông; sự lột xác"},
  {"id": "lex.en.200k.062811", "hw": "myoglobins", "pos": "noun", "ipa": "/ˈmaɪəˌɡloʊbɪnz/", "vi": "protein dự trữ oxy cơ myoglobin"},
  {"id": "lex.en.200k.062812", "hw": "neurochemicals", "pos": "noun", "ipa": "/ˌnjʊroʊˈkɛmɪkəlz/", "vi": "chất dẫn truyền hóa học thần kinh"},
  {"id": "lex.en.200k.062813", "hw": "noemis", "pos": "noun", "ipa": "/noʊˈiːmiz/", "vi": "nhân vật Na-ô-mi trong Kinh Thánh"},
  {"id": "lex.en.200k.062814", "hw": "norsemans", "pos": "noun", "ipa": "/ˈnɔːrsmənz/", "vi": "người Bắc Âu cổ đại; người Viking"},
  {"id": "lex.en.200k.062815", "hw": "ojibwas", "pos": "noun", "ipa": "/oʊˈdʒɪbwəz/", "vi": "người bản địa Bắc Mỹ Ojibwa"},
  {"id": "lex.en.200k.062816", "hw": "orreries", "pos": "noun", "ipa": "/ˈɔːrəriz/", "vi": "mô hình cơ học hệ Mặt Trời quay"},
  {"id": "lex.en.200k.062817", "hw": "osmunds", "pos": "noun", "ipa": "/ˈɑːzməndz/", "vi": "cây dương xỉ hoàng gia Osmunda"},
  {"id": "lex.en.200k.062818", "hw": "parvoviruses", "pos": "noun", "ipa": "/ˈpɑːrvoʊˌvaɪrəsɪz/", "vi": "virus ADN nhỏ gây bệnh parvovirus"},
  {"id": "lex.en.200k.062819", "hw": "patentees", "pos": "noun", "ipa": "/ˌpætənˈtiːz/", "vi": "người được cấp bằng sáng chế"},
  {"id": "lex.en.200k.062820", "hw": "patronymics", "pos": "noun", "ipa": "/ˌpætrəˈnɪmɪks/", "vi": "tên đệm hoặc họ đặt theo tên cha"},
  {"id": "lex.en.200k.062821", "hw": "pentecostalisms", "pos": "noun", "ipa": "/ˌpɛntɪˈkɔːstəˌlɪzəmz/", "vi": "phong trào Tin Lành Ngũ Tuần"},
  {"id": "lex.en.200k.062822", "hw": "percolators", "pos": "noun", "ipa": "/ˈpɜːrkəˌleɪtərz/", "vi": "bình đun pha cà phê lọc tuần hoàn"},
  {"id": "lex.en.200k.062823", "hw": "pflps", "pos": "noun", "ipa": "/ˌpiːˌɛfˌɛlˈpiːz/", "vi": "Mặt trận Giải phóng Palestine PFLP"},
  {"id": "lex.en.200k.062824", "hw": "pinpricks", "pos": "noun", "ipa": "/ˈpɪnprɪks/", "vi": "vết châm kim; điều phiền toái nhỏ"},
  {"id": "lex.en.200k.062825", "hw": "polygynies", "pos": "noun", "ipa": "/pəˈlɪdʒəniz/", "vi": "chế độ một chồng nhiều vợ; đa thê"},
  {"id": "lex.en.200k.062826", "hw": "progerias", "pos": "noun", "ipa": "/proʊˈdʒɪriəz/", "vi": "hội chứng lão hóa sớm ở trẻ em"},
  {"id": "lex.en.200k.062827", "hw": "propagators", "pos": "noun", "ipa": "/ˈprɑːpəˌɡeɪtərz/", "vi": "người truyền bá; hộp ươm giâm cây"},
  {"id": "lex.en.200k.062828", "hw": "propyls", "pos": "noun", "ipa": "/ˈproʊpəlz/", "vi": "nhóm gốc hiđrocacbon propyl"},
  {"id": "lex.en.200k.062829", "hw": "ragamuffins", "pos": "noun", "ipa": "/ˈræɡəˌmʌfɪnz/", "vi": "đứa trẻ ăn mặc rách rưới bụi đời"},
  {"id": "lex.en.200k.062830", "hw": "ragusas", "pos": "noun", "ipa": "/rəˈɡuːzəz/", "vi": "thành phố cổ Ragusa ở Croatia"},
  {"id": "lex.en.200k.062831", "hw": "rattigans", "pos": "noun", "ipa": "/ˈrætɪɡənz/", "vi": "nhà viết kịch Anh Terence Rattigan"},
  {"id": "lex.en.200k.062832", "hw": "redbones", "pos": "noun", "ipa": "/ˈrɛdboʊnz/", "vi": "chó săn gấu mèo Redbone lông đỏ"},
  {"id": "lex.en.200k.062833", "hw": "repasts", "pos": "noun", "ipa": "/rɪˈpæsts/", "vi": "bữa ăn thịnh soạn; bữa tiệc ăn uống"},
  {"id": "lex.en.200k.062834", "hw": "rivulets", "pos": "noun", "ipa": "/ˈrɪvjʊlɪts/", "vi": "dòng suối nhỏ chảy róc rách"},
  {"id": "lex.en.200k.062835", "hw": "ryegrasses", "pos": "noun", "ipa": "/ˈraɪɡræsɪz/", "vi": "cỏ lúa mạch đen làm thức ăn gia súc"},
  {"id": "lex.en.200k.062836", "hw": "saarinens", "pos": "noun", "ipa": "/ˈsɑːrənənz/", "vi": "kiến trúc sư Phần Lan Eero Saarinen"},
  {"id": "lex.en.200k.062837", "hw": "scows", "pos": "noun", "ipa": "/skaʊz/", "vi": "xà lan chở hàng đáy bằng đầu vuông"},
  {"id": "lex.en.200k.062838", "hw": "sequoyahs", "pos": "noun", "ipa": "/sɪˈkwɔɪəz/", "vi": "học giả bản địa Cherokee Sequoyah"},
  {"id": "lex.en.200k.062839", "hw": "sifters", "pos": "noun", "ipa": "/ˈsɪftərz/", "vi": "cái rây lọc bột; người sàng lọc"},
  {"id": "lex.en.200k.062840", "hw": "solitons", "pos": "noun", "ipa": "/ˈsɑːlɪtɑːnz/", "vi": "sóng đơn cô lập ổn định hình dạng"},
  {"id": "lex.en.200k.062841", "hw": "spinneys", "pos": "noun", "ipa": "/ˈspɪniz/", "vi": "lùm cây rậm nhỏ có nhiều bụi rậm"},
  {"id": "lex.en.200k.062842", "hw": "sportswomen", "pos": "noun", "ipa": "/ˈspɔːrtsˌwʊmən/", "vi": "nữ vận động viên thể thao"},
  {"id": "lex.en.200k.062843", "hw": "steinmans", "pos": "noun", "ipa": "/ˈstaɪnmənz/", "vi": "kỹ sư thiết kế cầu David Steinman"},
  {"id": "lex.en.200k.062844", "hw": "stiper", "pos": "noun", "ipa": "/ˈstaɪpər/", "vi": "binh sĩ có vạch quân hàm (biến thể)"},
  {"id": "lex.en.200k.062845", "hw": "stripers", "pos": "noun", "ipa": "/ˈstraɪpərz/", "vi": "lính hạ sĩ quan có vạch quân hàm"},
  {"id": "lex.en.200k.062846", "hw": "tablelands", "pos": "noun", "ipa": "/ˈteɪbəlˌlændz/", "vi": "vùng cao nguyên bằng phẳng rộng lớn"},
  {"id": "lex.en.200k.062847", "hw": "tereses", "pos": "noun", "ipa": "/ˈtɛrəsiːz/", "vi": "cơ tròn bả vai cánh tay (giải phẫu)"},
  {"id": "lex.en.200k.062848", "hw": "tessellations", "pos": "noun", "ipa": "/ˌtɛsəˈleɪʃənz/", "vi": "họa tiết lát khít mặt phẳng đều"},
  {"id": "lex.en.200k.062849", "hw": "theremins", "pos": "noun", "ipa": "/ˈθɛrəmɪnz/", "vi": "nhạc cụ điện tử không chạm theremin"},
  {"id": "lex.en.200k.062850", "hw": "thermistors", "pos": "noun", "ipa": "/ˈθɜːrmɪstərz/", "vi": "nhiệt điện trở cảm biến nhiệt độ"},
  {"id": "lex.en.200k.062851", "hw": "toastmasters", "pos": "noun", "ipa": "/ˈtoʊstˌmæstərz/", "vi": "người chủ trì dẫn dắt tiệc nâng ly"},
  {"id": "lex.en.200k.062852", "hw": "townsmen", "pos": "noun", "ipa": "/ˈtaʊnzmən/", "vi": "người đồng hương; dân thị trấn"},
  {"id": "lex.en.200k.062853", "hw": "transgenes", "pos": "noun", "ipa": "/trænzˈdʒiːnz/", "vi": "gen ngoại lai cấy chuyển vào cơ thể"},
  {"id": "lex.en.200k.062854", "hw": "trueloves", "pos": "noun", "ipa": "/ˈtruːlʌvz/", "vi": "người yêu chung thủy đích thực"},
  {"id": "lex.en.200k.062855", "hw": "unkindlier", "pos": "adj", "ipa": "/ʌnˈkaɪndliər/", "vi": "khắc nghiệt lạnh lùng tàn nhẫn hơn"},
  {"id": "lex.en.200k.062856", "hw": "unkindliest", "pos": "adj", "ipa": "/ʌnˈkaɪndliɪst/", "vi": "tệ bạc khắc nghiệt tàn nhẫn nhất"},
  {"id": "lex.en.200k.062857", "hw": "vireos", "pos": "noun", "ipa": "/ˈvɪrioʊz/", "vi": "chim sâu nhỏ châu Mỹ hót líu lo"},
  {"id": "lex.en.200k.062858", "hw": "whitefaces", "pos": "noun", "ipa": "/ˈwaɪtfeɪsɪz/", "vi": "bò thịt Hereford đầu trắng; sếu"},
  {"id": "lex.en.200k.062859", "hw": "wolfhounds", "pos": "noun", "ipa": "/ˈwʊlfhaʊndz/", "vi": "chó săn sói thân cao lớn nhanh nhẹn"},
  {"id": "lex.en.200k.062860", "hw": "zitis", "pos": "noun", "ipa": "/ˈziːtiz/", "vi": "mì ống Ý cỡ vừa dáng thẳng ziti"},
  {"id": "lex.en.200k.062861", "hw": "acellular slime mold", "pos": "phrase", "ipa": "/eɪˈsɛljələr slaɪm moʊld/", "vi": "nấm nhầy đơn bào cộng bào khổng lồ"},
  {"id": "lex.en.200k.062862", "hw": "alnus vulgaris", "pos": "phrase", "ipa": "/ˈælnəs vʌlˈɡɛrɪs/", "vi": "cây tống quán sủi đen vùng đầm lầy"},
  {"id": "lex.en.200k.062863", "hw": "american redstart", "pos": "phrase", "ipa": "/əˈmɛrɪkən ˈrɛdstɑːrt/", "vi": "chim chích Mỹ đuôi cam đỏ"},
  {"id": "lex.en.200k.062864", "hw": "amoebic dysentery", "pos": "phrase", "ipa": "/əˈmiːbɪk ˈdɪsənˌtɛri/", "vi": "bệnh kiết lỵ do ký sinh trùng amip"},
  {"id": "lex.en.200k.062865", "hw": "auditory meatus", "pos": "phrase", "ipa": "/ˈɔːdɪtɔːri miˈeɪtəs/", "vi": "ống tai dẫn âm thanh tới màng nhĩ"},
  {"id": "lex.en.200k.062866", "hw": "black fritillary", "pos": "phrase", "ipa": "/blæk ˈfrɪtəˌlɛri/", "vi": "cây hoa loa kèn chuông tím đen"},
  {"id": "lex.en.200k.062867", "hw": "bruno of toul", "pos": "phrase", "ipa": "/ˈbruːnoʊ əv tuːl/", "vi": "Giáo hoàng Lêô IX Brunô thành Toul"},
  {"id": "lex.en.200k.062868", "hw": "bufo americanus", "pos": "phrase", "ipa": "/ˈbjuːfoʊ əˌmɛrɪˈkænəs/", "vi": "cóc đất sần Bắc Mỹ Bufo americanus"},
  {"id": "lex.en.200k.062869", "hw": "campanula americana", "pos": "phrase", "ipa": "/kæmˈpænjʊlə əˌmɛrɪˈkænə/", "vi": "cây hoa chuông cao xanh Bắc Mỹ"},
  {"id": "lex.en.200k.062870", "hw": "cardioid microphone", "pos": "phrase", "ipa": "/ˈkɑːrdiɔɪd ˈmaɪkrəfoʊn/", "vi": "micro thu âm định hướng phía trước"},
  {"id": "lex.en.200k.062871", "hw": "cardioid mike", "pos": "phrase", "ipa": "/ˈkɑːrdiɔɪd maɪk/", "vi": "micro định hướng một chiều hình tim"},
  {"id": "lex.en.200k.062872", "hw": "choroidal artery", "pos": "phrase", "ipa": "/kəˈrɔɪdəl ˈɑːrtəri/", "vi": "động mạch màng mạch nuôi võng mạc"},
  {"id": "lex.en.200k.062873", "hw": "convolution of broca", "pos": "phrase", "ipa": "/ˌkɑːnvəˈluːʃən əv ˈbroʊkə/", "vi": "hồi trán dưới Broca vùng ngôn ngữ"},
  {"id": "lex.en.200k.062874", "hw": "dalmatian laburnum", "pos": "phrase", "ipa": "/dælˈmeɪʃən ləˈbɜːrnəm/", "vi": "cây bụi hoa vàng chùm Dalmatia"},
  {"id": "lex.en.200k.062875", "hw": "dilation and curettage", "pos": "phrase", "ipa": "/daɪˈleɪʃən ənd ˌkjʊrəˈtɑːʒ/", "vi": "thủ thuật nong và nạo buồng tử cung"},
  {"id": "lex.en.200k.062876", "hw": "engelbert humperdinck", "pos": "phrase", "ipa": "/ˈɛŋɡəlbɛrt ˈhʊmpərdɪŋk/", "vi": "nhà soạn nhạc Đức Humperdinck"},
  {"id": "lex.en.200k.062877", "hw": "equus quagga", "pos": "phrase", "ipa": "/ˈiːkwəs ˈkwɑːɡə/", "vi": "loài ngựa vằn Quagga đã tuyệt chủng"},
  {"id": "lex.en.200k.062878", "hw": "exfiltration operation", "pos": "phrase", "ipa": "/ˌɛksfɪlˈtreɪʃən ˌɑːpəˈreɪʃən/", "vi": "chiến dịch rút quân giải cứu bí mật"},
  {"id": "lex.en.200k.062879", "hw": "fen orchis", "pos": "phrase", "ipa": "/fɛn ˈɔːrkɪs/", "vi": "hoa lan đầm lầy nhỏ màu vàng lục"},
  {"id": "lex.en.200k.062880", "hw": "fenestra rotunda", "pos": "phrase", "ipa": "/fəˈnɛstrə roʊˈtʌndə/", "vi": "cửa sổ tròn tai trong thông ốc tai"},
  {"id": "lex.en.200k.062881", "hw": "fin de siecle", "pos": "phrase", "ipa": "/ˌfæn də siˈɛklə/", "vi": "phong cách nghệ thuật cuối thế kỷ"},
  {"id": "lex.en.200k.062882", "hw": "fines herbes", "pos": "phrase", "ipa": "/fiːnz ˈɛərb/", "vi": "hỗn hợp bốn rau thơm Pháp băm nhỏ"},
  {"id": "lex.en.200k.062883", "hw": "fringed orchis", "pos": "phrase", "ipa": "/frɪndʒd ˈɔːrkɪs/", "vi": "lan cánh viền tua đẹp Bắc Mỹ"},
  {"id": "lex.en.200k.062884", "hw": "gamma hydroxybutyrate", "pos": "phrase", "ipa": "/ˈɡæmə haɪˌdrɑːksiˈbjuːtəreɪt/", "vi": "hợp chất ức chế thần kinh GHB"},
  {"id": "lex.en.200k.062885", "hw": "gaston lachaise", "pos": "phrase", "ipa": "/ɡæsˈtɔːn ləˈʃɛz/", "vi": "nhà điêu khắc Mỹ Gaston Lachaise"},
  {"id": "lex.en.200k.062886", "hw": "genus hepatica", "pos": "phrase", "ipa": "/ˈdʒiːnəs hɪˈpætɪkə/", "vi": "chi cây hoa lá gan Hepatica"},
  {"id": "lex.en.200k.062887", "hw": "genus ixodes", "pos": "phrase", "ipa": "/ˈdʒiːnəs ɪkˈsoʊdiːz/", "vi": "chi ve bét hút máu truyền bệnh"},
  {"id": "lex.en.200k.062888", "hw": "genus martes", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈmɑːrtiːz/", "vi": "chi chồn vàng ăn thịt họ Chồn"},
  {"id": "lex.en.200k.062889", "hw": "genus microtus", "pos": "phrase", "ipa": "/ˈdʒiːnəs maɪˈkroʊtəs/", "vi": "chi chuột đồng đuôi ngắn Microtus"},
  {"id": "lex.en.200k.062890", "hw": "genus peromyscus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌpɛrəˈmɪskəs/", "vi": "chi chuột hươu Bắc Mỹ Peromyscus"},
  {"id": "lex.en.200k.062891", "hw": "genus sabal", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈseɪbəl/", "vi": "chi cây cọ lùn lá quạt Sabal"},
  {"id": "lex.en.200k.062892", "hw": "genus saccharum", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈsækərəm/", "vi": "chi thực vật cây mía đường"},
  {"id": "lex.en.200k.062893", "hw": "genus schistosoma", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌʃɪstəˈsoʊmə/", "vi": "chi ký sinh trùng sán máng huyết"},
  {"id": "lex.en.200k.062894", "hw": "genus testudo", "pos": "phrase", "ipa": "/ˈdʒiːnəs tɛsˈtuːdoʊ/", "vi": "chi rùa cạn Địa Trung Hải Testudo"},
  {"id": "lex.en.200k.062895", "hw": "globus pallidus", "pos": "phrase", "ipa": "/ˈɡloʊbəs ˈpælɪdəs/", "vi": "nhân cầu nhạt trong hạch nền não"},
  {"id": "lex.en.200k.062896", "hw": "golden ragwort", "pos": "phrase", "ipa": "/ˈɡoʊldən ˈræɡwɜːrt/", "vi": "cây cúc dại hoa vàng Bắc Mỹ"},
  {"id": "lex.en.200k.062897", "hw": "gottfried wilhelm leibnitz", "pos": "phrase", "ipa": "/ˈɡɑːtfriːt ˈvɪlhɛlm ˈlaɪbnɪts/", "vi": "triết gia toán học Đức Leibniz"},
  {"id": "lex.en.200k.062898", "hw": "green fringed orchis", "pos": "phrase", "ipa": "/ɡriːn frɪndʒd ˈɔːrkɪs/", "vi": "hoa lan cánh tua màu xanh lục nhạt"},
  {"id": "lex.en.200k.062899", "hw": "greenhouse whitefly", "pos": "phrase", "ipa": "/ˈɡriːnhaʊs ˈwaɪtflaɪ/", "vi": "bọ phấn trắng hại cây nhà kính"},
  {"id": "lex.en.200k.062900", "hw": "hemangioma simplex", "pos": "phrase", "ipa": "/hɪˌmændʒiˈoʊmə ˈsɪmplɛks/", "vi": "u máu lành tính ngoài da ở trẻ em"},
  {"id": "lex.en.200k.062901", "hw": "hightail it", "pos": "phrase", "ipa": "/ˈhaɪteɪl ɪt/", "vi": "chạy thục mạng; chuồn lẹ khẩn cấp"},
  {"id": "lex.en.200k.062902", "hw": "in loco parentis", "pos": "phrase", "ipa": "/ɪn ˈloʊkoʊ pəˈrɛntɪs/", "vi": "thay mặt giữ vai trò như cha mẹ"}
]

with open('scratch/b33_r06_raw_p4.json') as f:
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

with open('scratch/b33_r06_p4.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r06_p4.json OK")
