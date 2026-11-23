import json

items = [
  {"id": "lex.en.200k.064703", "hw": "kenzo tange", "pos": "phrase", "ipa": "/ˈkɛnzoʊ ˈtɑːŋɡeɪ/", "vi": "kiến trúc sư Nhật Bản Kenzo Tange"},
  {"id": "lex.en.200k.064704", "hw": "morus nigra", "pos": "phrase", "ipa": "/ˈmɔːrəs ˈnaɪɡrə/", "vi": "cây dâu tằm quả đen vị ngọt đậm"},
  {"id": "lex.en.200k.064705", "hw": "myna bird", "pos": "phrase", "ipa": "/ˈmaɪnə bɜːrd/", "vi": "chim sáo nâu; chim nhồng biết nói"},
  {"id": "lex.en.200k.064706", "hw": "necrotizing enteritis", "pos": "phrase", "ipa": "/ˈnɛkrəˌtaɪzɪŋ ˌɛntəˈraɪtɪs/", "vi": "bệnh viêm ruột hoại tử cấp tính"},
  {"id": "lex.en.200k.064707", "hw": "nicholas vachel lindsay", "pos": "phrase", "ipa": "/ˈnɪkələs ˈveɪtʃəl ˈlɪndzi/", "vi": "nhà thơ hiện đại Mỹ Vachel Lindsay"},
  {"id": "lex.en.200k.064708", "hw": "ojos del salado", "pos": "phrase", "ipa": "/ˈoʊhoʊs dɛl səˈlɑːdoʊ/", "vi": "núi lửa cao nhất thế giới ở Chile"},
  {"id": "lex.en.200k.064709", "hw": "order rodentia", "pos": "phrase", "ipa": "/ˈɔːrdər roʊˈdɛnʃə/", "vi": "bộ Gặm nhấm gồm chuột và sóc"},
  {"id": "lex.en.200k.064710", "hw": "paraboloid reflector", "pos": "phrase", "ipa": "/pəˈræbəˌlɔɪd rɪˈflɛktər/", "vi": "chảo gương phản xạ parabol hội tụ"},
  {"id": "lex.en.200k.064711", "hw": "paraquat poisoning", "pos": "phrase", "ipa": "/ˈpɛrəˌkwɑːt ˈpɔɪzənɪŋ/", "vi": "ngộ độc thuốc diệt cỏ paraquat"},
  {"id": "lex.en.200k.064712", "hw": "phanerozoic eon", "pos": "phrase", "ipa": "/ˌfænərəˈzoʊɪk ˈiːɑːn/", "vi": "liên đại Hiển sinh trong địa chất"},
  {"id": "lex.en.200k.064713", "hw": "pine siskin", "pos": "phrase", "ipa": "/paɪn ˈsɪskɪn/", "vi": "chim sẻ thông siskin vạch nâu Mỹ"},
  {"id": "lex.en.200k.064714", "hw": "prunus pumila", "pos": "phrase", "ipa": "/ˈpruːnəs ˈpjuːmələ/", "vi": "cây anh đào cát mọc bụi Bắc Mỹ"},
  {"id": "lex.en.200k.064715", "hw": "qatari riyal", "pos": "phrase", "ipa": "/kəˈtɑːri riˈɑːl/", "vi": "đơn vị tiền tệ riyal của Qatar"},
  {"id": "lex.en.200k.064716", "hw": "red siskin", "pos": "phrase", "ipa": "/rɛd ˈsɪskɪn/", "vi": "chim sẻ lông đỏ đầu đen Nam Mỹ"},
  {"id": "lex.en.200k.064717", "hw": "sigmoid flexure", "pos": "phrase", "ipa": "/ˈsɪɡmɔɪd ˈflɛkʃər/", "vi": "đoạn kết tràng sigma cong chữ S"},
  {"id": "lex.en.200k.064718", "hw": "supraorbital torus", "pos": "phrase", "ipa": "/ˌsuːprəˈɔːrbɪtəl ˈtɔːrəs/", "vi": "gờ xương nổi trên hốc mắt người cổ"},
  {"id": "lex.en.200k.064719", "hw": "trygve lie", "pos": "phrase", "ipa": "/ˈtrɪɡvə ˈliː/", "vi": "Tổng thư ký đầu tiên của LHQ"},
  {"id": "lex.en.200k.064720", "hw": "whorled caraway", "pos": "phrase", "ipa": "/wɜːrld ˈkærəweɪ/", "vi": "cây thì là lá mọc vòng châu Âu"},
  {"id": "lex.en.200k.064721", "hw": "whorled milkweed", "pos": "phrase", "ipa": "/wɜːrld ˈmɪlkwiːd/", "vi": "cây bông tai lá mọc vòng Bắc Mỹ"},
  {"id": "lex.en.200k.064722", "hw": "wilde dagga", "pos": "phrase", "ipa": "/ˈwɪldə ˈdɑːɡə/", "vi": "cây tai sư tử hoa cam Nam Phi"},
  {"id": "lex.en.200k.064723", "hw": "aeoluses", "pos": "noun", "ipa": "/iˈoʊləsɪz/", "vi": "thần cai quản gió Hy Lạp cổ Aeolus"},
  {"id": "lex.en.200k.064724", "hw": "agouties", "pos": "noun", "ipa": "/əˈɡuːtiz/", "vi": "loài chuột lang agouti rừng Nam Mỹ"},
  {"id": "lex.en.200k.064725", "hw": "agoutis", "pos": "noun", "ipa": "/əˈɡuːtiz/", "vi": "thú gặm nhấm agouti rừng Nam Mỹ"},
  {"id": "lex.en.200k.064726", "hw": "angleseas", "pos": "noun", "ipa": "/ˈæŋɡəlsiz/", "vi": "đảo Anglesey phía tây bắc xứ Wales"},
  {"id": "lex.en.200k.064727", "hw": "antwerpens", "pos": "noun", "ipa": "/ˈɑːntwɛrpənz/", "vi": "thành phố cảng Antwerp nước Bỉ"},
  {"id": "lex.en.200k.064728", "hw": "aristarchuses", "pos": "noun", "ipa": "/ˌærɪˈstɑːrkəsɪz/", "vi": "nhà thiên văn Hy Lạp Aristarchus"},
  {"id": "lex.en.200k.064729", "hw": "arminianisms", "pos": "noun", "ipa": "/ɑːrˈmɪniəˌnɪzəmz/", "vi": "thuyết thần học Tin Lành Arminius"},
  {"id": "lex.en.200k.064730", "hw": "aspers", "pos": "noun", "ipa": "/ˈæspərz/", "vi": "đồng tiền bạc nhỏ Thổ Nhĩ Kỳ xưa"},
  {"id": "lex.en.200k.064731", "hw": "banjuls", "pos": "noun", "ipa": "/ˈbændʒuːlz/", "vi": "thủ đô cảng Banjul của nước Gambia"},
  {"id": "lex.en.200k.064732", "hw": "basutolands", "pos": "noun", "ipa": "/bəˈsuːtoʊˌlændz/", "vi": "nước Lesotho (tên thuộc địa cũ)"},
  {"id": "lex.en.200k.064733", "hw": "boeotias", "pos": "noun", "ipa": "/biˈoʊʃəz/", "vi": "vùng lịch sử Boeotia ở Hy Lạp"},
  {"id": "lex.en.200k.064734", "hw": "brummies", "pos": "noun", "ipa": "/ˈbrʌmiz/", "vi": "người gốc thành phố Birmingham Anh"},
  {"id": "lex.en.200k.064735", "hw": "cadastres", "pos": "noun", "ipa": "/kəˈdæstərz/", "vi": "sổ địa chính đo đạc thửa đất (Anh)"},
  {"id": "lex.en.200k.064736", "hw": "calcitonins", "pos": "noun", "ipa": "/ˌkælsəˈtoʊnɪnz/", "vi": "hoóc môn tuyến giáp hạ canxi máu"},
  {"id": "lex.en.200k.064737", "hw": "carbonizations", "pos": "noun", "ipa": "/ˌkɑːrbənəˈzeɪʃənz/", "vi": "quá trình than hóa chất hữu cơ"},
  {"id": "lex.en.200k.064738", "hw": "catalpas", "pos": "noun", "ipa": "/kəˈtælpəz/", "vi": "cây gỗ hoa chùm quả dài catalpa"},
  {"id": "lex.en.200k.064739", "hw": "catbirds", "pos": "noun", "ipa": "/ˈkætbɜːrdz/", "vi": "chim mèo xám nhại tiếng mèo Bắc Mỹ"},
  {"id": "lex.en.200k.064740", "hw": "ceibas", "pos": "noun", "ipa": "/ˈseɪbəz/", "vi": "cây gòn cổ thụ lấy sợi bông êm"},
  {"id": "lex.en.200k.064741", "hw": "centauruses", "pos": "noun", "ipa": "/sɛnˈtɔːrəsɪz/", "vi": "chòm sao Bán Nhân Mã phương nam"},
  {"id": "lex.en.200k.064742", "hw": "chaldeas", "pos": "noun", "ipa": "/kælˈdiːəz/", "vi": "vùng cổ Can-đê miền nam Lưỡng Hà"},
  {"id": "lex.en.200k.064743", "hw": "chlorpromazines", "pos": "noun", "ipa": "/klɔːrˈprɑːməziːnz/", "vi": "thuốc an thần điều trị loạn thần"},
  {"id": "lex.en.200k.064744", "hw": "chlorpyrifoses", "pos": "noun", "ipa": "/ˌklɔːrˈpɪrəˌfɑːsɪz/", "vi": "thuốc trừ sâu lân hữu cơ chlorpy"},
  {"id": "lex.en.200k.064745", "hw": "coleuses", "pos": "noun", "ipa": "/ˈkoʊliəsɪz/", "vi": "cây tía tô cảnh lá ngũ sắc rực rỡ"},
  {"id": "lex.en.200k.064746", "hw": "collodions", "pos": "noun", "ipa": "/kəˈloʊdiənz/", "vi": "dung dịch keo băng vết thương xưa"},
  {"id": "lex.en.200k.064747", "hw": "comfreys", "pos": "noun", "ipa": "/ˈkʌmfriz/", "vi": "cây thảo dược liên mộc hoa tím rủ"},
  {"id": "lex.en.200k.064748", "hw": "counteroffers", "pos": "noun", "ipa": "/ˈkaʊntərˌɔːfərz/", "vi": "lời chào giá trả ngược thương lượng"},
  {"id": "lex.en.200k.064749", "hw": "demyelinations", "pos": "noun", "ipa": "/diːˌmaɪəlɪˈneɪʃənz/", "vi": "tình trạng thoái hóa mất bao myelin"},
  {"id": "lex.en.200k.064750", "hw": "dilaudids", "pos": "noun", "ipa": "/dɪˈlɔːdɪdz/", "vi": "thuốc giảm đau gây nghiện Dilaudid"},
  {"id": "lex.en.200k.064751", "hw": "dowsed", "pos": "verb", "ipa": "/daʊzd/", "vi": "đã dội ướt sũng; đã dò mạch nước"},
  {"id": "lex.en.200k.064752", "hw": "dowses", "pos": "noun", "ipa": "/daʊzɪz/", "vi": "thuật dò mạch nước khoáng bằng que"},
  {"id": "lex.en.200k.064753", "hw": "doxies", "pos": "noun", "ipa": "/ˈdɑːksiz/", "vi": "nhân tình (từ cổ); tín điều riêng"},
  {"id": "lex.en.200k.064754", "hw": "dreisers", "pos": "noun", "ipa": "/ˈdraɪzərz/", "vi": "nhà văn hiện thực Mỹ Dreiser"},
  {"id": "lex.en.200k.064755", "hw": "dryases", "pos": "noun", "ipa": "/ˈdraɪəsɪz/", "vi": "cây hoa hồng đá Bắc Cực Dryas"},
  {"id": "lex.en.200k.064756", "hw": "electroencephalograms", "pos": "noun", "ipa": "/ɪˌlɛktroʊɛnˈsɛfələˌɡræmz/", "vi": "bản ghi điện não đồ sóng não EEG"},
  {"id": "lex.en.200k.064757", "hw": "ellases", "pos": "noun", "ipa": "/ˈɛləsɪz/", "vi": "tên bản địa đất nước Hy Lạp Hellas"},
  {"id": "lex.en.200k.064758", "hw": "embalmers", "pos": "noun", "ipa": "/ɪmˈbɑːmərz/", "vi": "người chuyên ướp xác giữ thi hài"},
  {"id": "lex.en.200k.064759", "hw": "etchers", "pos": "noun", "ipa": "/ˈɛtʃərz/", "vi": "nghệ nhân khắc bản kẽm bằng axit"},
  {"id": "lex.en.200k.064760", "hw": "exudated", "pos": "verb", "ipa": "/ˈɛksjʊˌdeɪtɪd/", "vi": "đã rỉ tiết dịch nhựa ra bề mặt"},
  {"id": "lex.en.200k.064761", "hw": "exudates", "pos": "noun", "ipa": "/ˈɛksjʊˌdeɪts/", "vi": "dịch tiết rỉ ra từ vết thương cây"},
  {"id": "lex.en.200k.064762", "hw": "exudating", "pos": "verb", "ipa": "/ˈɛksjʊˌdeɪtɪŋ/", "vi": "đang rỉ dịch nhựa qua khe bề mặt"},
  {"id": "lex.en.200k.064763", "hw": "fibbers", "pos": "noun", "ipa": "/ˈfɪbərz/", "vi": "kẻ hay nói dối vặt bịa chuyện nhỏ"},
  {"id": "lex.en.200k.064764", "hw": "foremasts", "pos": "noun", "ipa": "/ˈfɔːrmæsts/", "vi": "cột buồm trước đứng gần mũi tàu"},
  {"id": "lex.en.200k.064765", "hw": "fpds", "pos": "noun", "ipa": "/ˌɛfˌpiːˈdiːz/", "vi": "màn hình hiển thị phẳng FPD mỏng"},
  {"id": "lex.en.200k.064766", "hw": "frangipanis", "pos": "noun", "ipa": "/ˌfrændʒəˈpɑːniz/", "vi": "cây hoa sứ đại thơm vùng nhiệt đới"},
  {"id": "lex.en.200k.064767", "hw": "freesias", "pos": "noun", "ipa": "/ˈfriːʒəz/", "vi": "hoa lan nam phi dáng chuông thơm"},
  {"id": "lex.en.200k.064768", "hw": "fuschias", "pos": "noun", "ipa": "/ˈfjuːʃəz/", "vi": "hoa lồng đèn; màu hồng tím rực"},
  {"id": "lex.en.200k.064769", "hw": "gateaux", "pos": "noun", "ipa": "/ɡæˈtoʊz/", "vi": "bánh kem ga-tô nhiều lớp trang trí"},
  {"id": "lex.en.200k.064770", "hw": "gonads", "pos": "noun", "ipa": "/ˈɡoʊnædz/", "vi": "tuyến sinh dục tạo giao tử cơ thể"},
  {"id": "lex.en.200k.064771", "hw": "groks", "pos": "verb", "ipa": "/ɡrɑːks/", "vi": "hiểu thấu đáo tận gốc (tiếng lóng)"},
  {"id": "lex.en.200k.064772", "hw": "hardliners", "pos": "noun", "ipa": "/ˈhɑːrdˌlaɪnərz/", "vi": "người theo đường lối cứng rắn"},
  {"id": "lex.en.200k.064773", "hw": "hemochromatoses", "pos": "noun", "ipa": "/ˌhiːməˌkroʊməˈtoʊsiːz/", "vi": "bệnh rối loạn tích tụ thừa sắt gan"},
  {"id": "lex.en.200k.064774", "hw": "hottentots", "pos": "noun", "ipa": "/ˈhɑːtəntɑːts/", "vi": "tên cũ chỉ người Khoekhoe Nam Phi"},
  {"id": "lex.en.200k.064775", "hw": "hymies", "pos": "noun", "ipa": "/ˈhaɪmiz/", "vi": "từ miệt thị người Do Thái (lóng)"},
  {"id": "lex.en.200k.064776", "hw": "hyperhidroses", "pos": "noun", "ipa": "/ˌhaɪpərhaɪˈdroʊsiːz/", "vi": "chứng tăng tiết mồ hôi quá mức"},
  {"id": "lex.en.200k.064777", "hw": "igds", "pos": "noun", "ipa": "/ˌaɪˌdʒiːˈdiːz/", "vi": "kháng thể miễn dịch lớp IgD máu"},
  {"id": "lex.en.200k.064778", "hw": "indabas", "pos": "noun", "ipa": "/ɪnˈdɑːbəz/", "vi": "cuộc họp hội nghị bàn bạc (Nam Phi)"},
  {"id": "lex.en.200k.064779", "hw": "inglenooks", "pos": "noun", "ipa": "/ˈɪŋɡəlnʊks/", "vi": "hốc ghế ấm cúng ngay cạnh lò sưởi"},
  {"id": "lex.en.200k.064780", "hw": "inhalants", "pos": "noun", "ipa": "/ɪnˈheɪlənts/", "vi": "thuốc xịt hít; dung môi hít gây mê"},
  {"id": "lex.en.200k.064781", "hw": "insectas", "pos": "noun", "ipa": "/ɪnˈsɛktəz/", "vi": "lớp động vật Côn trùng chân khớp"},
  {"id": "lex.en.200k.064782", "hw": "ironmongers", "pos": "noun", "ipa": "/ˈaɪərnˌmʌŋɡərz/", "vi": "người bán đồ ngũ kim kim khí (Anh)"},
  {"id": "lex.en.200k.064783", "hw": "ivps", "pos": "noun", "ipa": "/ˌaɪˌviːˈpiːz/", "vi": "chụp X-quang thận thuốc cản quang"},
  {"id": "lex.en.200k.064784", "hw": "juncos", "pos": "noun", "ipa": "/ˈdʒʌŋkoʊz/", "vi": "chim sẻ tuyết nhỏ lưng xám Bắc Mỹ"},
  {"id": "lex.en.200k.064785", "hw": "juntos", "pos": "noun", "ipa": "/ˈdʒʌntoʊz/", "vi": "bè phái chính trị bí mật kết hợp"},
  {"id": "lex.en.200k.064786", "hw": "kabobs", "pos": "noun", "ipa": "/kəˈbɑːbz/", "vi": "món thịt rau củ xiên que nướng than"},
  {"id": "lex.en.200k.064787", "hw": "kachinas", "pos": "noun", "ipa": "/kəˈtʃiːnəz/", "vi": "linh hồn và búp bê gỗ người Hopi"},
  {"id": "lex.en.200k.064788", "hw": "knuckleballs", "pos": "noun", "ipa": "/ˈnʌkəlˌbɔːlz/", "vi": "cú ném bóng chày lắc lư không xoáy"},
  {"id": "lex.en.200k.064789", "hw": "leathernecks", "pos": "noun", "ipa": "/ˈlɛðərˌnɛks/", "vi": "lính Thủy quân Lục chiến Hoa Kỳ"},
  {"id": "lex.en.200k.064790", "hw": "librevilles", "pos": "noun", "ipa": "/ˌliːbrəˈviːlz/", "vi": "thủ đô cảng Libreville nước Gabon"},
  {"id": "lex.en.200k.064791", "hw": "lubitsches", "pos": "noun", "ipa": "/ˈluːbɪtʃɪz/", "vi": "đạo diễn điện ảnh Ernst Lubitsch"},
  {"id": "lex.en.200k.064792", "hw": "luggers", "pos": "noun", "ipa": "/ˈlʌɡərz/", "vi": "thuyền buồm đánh cá cỡ nhỏ hai cột"},
  {"id": "lex.en.200k.064793", "hw": "malinoides", "pos": "noun", "ipa": "/ˌmælənˈwɑːz/", "vi": "chó nghiệp vụ chăn cừu Bỉ Malinois"},
  {"id": "lex.en.200k.064794", "hw": "mandes", "pos": "noun", "ipa": "/ˈmɑːndeɪz/", "vi": "ngôn ngữ và dân tộc Mande Tây Phi"},
  {"id": "lex.en.200k.064795", "hw": "meconiums", "pos": "noun", "ipa": "/mɪˈkoʊniəmz/", "vi": "phân su đầu tiên của trẻ sơ sinh"},
  {"id": "lex.en.200k.064796", "hw": "metaphases", "pos": "noun", "ipa": "/ˈmɛtəˌfeɪzɪz/", "vi": "kỳ giữa của quá trình phân bào"},
  {"id": "lex.en.200k.064797", "hw": "meyerbeers", "pos": "noun", "ipa": "/ˈmaɪərbɪərz/", "vi": "nhà soạn nhạc opera Đức Meyerbeer"},
  {"id": "lex.en.200k.064798", "hw": "millipedes", "pos": "noun", "ipa": "/ˈmɪləpiːdz/", "vi": "động vật chân khớp cuốn chiếu hiền"},
  {"id": "lex.en.200k.064799", "hw": "mullions", "pos": "noun", "ipa": "/ˈmʌljənz/", "vi": "thanh đố dọc chia ô khung cửa sổ"},
  {"id": "lex.en.200k.064800", "hw": "multinomials", "pos": "noun", "ipa": "/ˌmʌltiˈnoʊmiəlz/", "vi": "đa thức đại số gồm nhiều hạng tử"},
  {"id": "lex.en.200k.064801", "hw": "mutisms", "pos": "noun", "ipa": "/ˈmjuːtɪzəmz/", "vi": "chứng câm lặng không nói do tâm lý"},
  {"id": "lex.en.200k.064802", "hw": "newels", "pos": "noun", "ipa": "/ˈnuːəlz/", "vi": "trụ cái đỡ tay vịn đầu cầu thang"}
]

with open('scratch/b33_r10_raw_p3.json') as f:
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

with open('scratch/b33_r10_p3.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r10_p3.json OK")
