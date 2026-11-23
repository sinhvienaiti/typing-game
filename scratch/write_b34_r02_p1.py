import json

items = [
  {"id": "lex.en.200k.065503", "hw": "helminths", "pos": "noun", "ipa": "/ˈhɛlmɪnθs/", "vi": "giun sán ký sinh trong cơ thể"},
  {"id": "lex.en.200k.065504", "hw": "hesperuses", "pos": "noun", "ipa": "/ˈhɛspərəsɪz/", "vi": "sao Hôm mọc buổi chiều tối"},
  {"id": "lex.en.200k.065505", "hw": "icteruses", "pos": "noun", "ipa": "/ˈɪktərəsɪz/", "vi": "chứng bệnh vàng da; chim vàng anh"},
  {"id": "lex.en.200k.065506", "hw": "jiujitsus", "pos": "noun", "ipa": "/dʒuːˈdʒuːtsuːz/", "vi": "môn võ nhu thuật tự vệ Nhật Bản"},
  {"id": "lex.en.200k.065507", "hw": "kbits", "pos": "noun", "ipa": "/ˈkɪləbɪts/", "vi": "đơn vị dữ liệu kilobit (1000 bit)"},
  {"id": "lex.en.200k.065508", "hw": "kleptomaniacs", "pos": "noun", "ipa": "/ˌklɛptəˈmeɪniˌæks/", "vi": "người mắc chứng bệnh cuồng ăn cắp"},
  {"id": "lex.en.200k.065509", "hw": "krooni", "pos": "noun", "ipa": "/ˈkruːni/", "vi": "tiền tệ cũ kroon của nước Estonia"},
  {"id": "lex.en.200k.065510", "hw": "kroons", "pos": "noun", "ipa": "/kruːnz/", "vi": "các đồng tiền cũ kroon Estonia"},
  {"id": "lex.en.200k.065511", "hw": "kwachas", "pos": "noun", "ipa": "/ˈkwɑːtʃəz/", "vi": "đơn vị tiền tệ Zambia và Malawi"},
  {"id": "lex.en.200k.065512", "hw": "latchkeys", "pos": "noun", "ipa": "/ˈlætʃkiːz/", "vi": "chìa khóa mở cửa chính nhà riêng"},
  {"id": "lex.en.200k.065513", "hw": "lingonberries", "pos": "noun", "ipa": "/ˈlɪŋɡənˌbɛriz/", "vi": "quả mọng đỏ vùng Bắc Âu làm mứt"},
  {"id": "lex.en.200k.065514", "hw": "litchis", "pos": "noun", "ipa": "/ˈlaɪtʃiz/", "vi": "cây và quả vải thiều ngọt mọng"},
  {"id": "lex.en.200k.065515", "hw": "loveseats", "pos": "noun", "ipa": "/ˈlʌvsiːts/", "vi": "ghế sô pha đôi dành cho hai người"},
  {"id": "lex.en.200k.065516", "hw": "lubecks", "pos": "noun", "ipa": "/ˈluːbɛks/", "vi": "thành phố cảng cổ Lübeck nước Đức"},
  {"id": "lex.en.200k.065517", "hw": "lymphadenopathies", "pos": "noun", "ipa": "/lɪmˌfædənˈɑːpəθiz/", "vi": "bệnh lý sưng viêm hạch bạch huyết"},
  {"id": "lex.en.200k.065518", "hw": "mansards", "pos": "noun", "ipa": "/ˈmænsɑːrdz/", "vi": "kiểu mái nhà hai độ dốc Pháp"},
  {"id": "lex.en.200k.065519", "hw": "mapquested", "pos": "verb", "ipa": "/ˈmæpkwɛstɪd/", "vi": "đã tra chỉ đường bằng MapQuest"},
  {"id": "lex.en.200k.065520", "hw": "mapquesting", "pos": "verb", "ipa": "/ˈmæpkwɛstɪŋ/", "vi": "đang tra cứu bản đồ chỉ đường"},
  {"id": "lex.en.200k.065521", "hw": "mapquests", "pos": "noun", "ipa": "/ˈmæpkwɛsts/", "vi": "dịch vụ bản đồ chỉ đường MapQuest"},
  {"id": "lex.en.200k.065522", "hw": "mazurkas", "pos": "noun", "ipa": "/məˈzɜːrkəz/", "vi": "điệu nhảy dân gian và nhạc Ba Lan"},
  {"id": "lex.en.200k.065523", "hw": "metoprolols", "pos": "noun", "ipa": "/mɛˈtoʊprəlɔːlz/", "vi": "thuốc chẹn beta hạ áp metoprolol"},
  {"id": "lex.en.200k.065524", "hw": "midafternoons", "pos": "noun", "ipa": "/ˌmɪdˌæftərˈnuːnz/", "vi": "khoảng thời gian giữa buổi chiều"},
  {"id": "lex.en.200k.065525", "hw": "miniaturists", "pos": "noun", "ipa": "/ˈmɪniətʃərɪsts/", "vi": "họa sĩ vẽ tranh tiểu họa siêu nhỏ"},
  {"id": "lex.en.200k.065526", "hw": "monopolised", "pos": "verb", "ipa": "/məˈnɑːpəˌlaɪzd/", "vi": "đã độc chiếm độc quyền (cách Anh)"},
  {"id": "lex.en.200k.065527", "hw": "monopolises", "pos": "verb", "ipa": "/məˈnɑːpəˌlaɪzɪz/", "vi": "độc chiếm nắm trọn độc quyền (Anh)"},
  {"id": "lex.en.200k.065528", "hw": "monopolising", "pos": "verb", "ipa": "/məˈnɑːpəˌlaɪzɪŋ/", "vi": "đang nắm giữ độc quyền (cách Anh)"},
  {"id": "lex.en.200k.065529", "hw": "mothballed", "pos": "verb", "ipa": "/ˈmɔːθbɔːld/", "vi": "đã niêm cất bảo quản; xếp xó dừng"},
  {"id": "lex.en.200k.065530", "hw": "mothballing", "pos": "verb", "ipa": "/ˈmɔːθbɔːlɪŋ/", "vi": "đang niêm cất kho; tạm dừng dự án"},
  {"id": "lex.en.200k.065531", "hw": "mothballs", "pos": "noun", "ipa": "/ˈmɔːθbɔːlz/", "vi": "viên băng phiến đuổi sâu bướm gián"},
  {"id": "lex.en.200k.065532", "hw": "mushers", "pos": "noun", "ipa": "/ˈmʌʃərz/", "vi": "người điều khiển xe chó kéo tuyết"},
  {"id": "lex.en.200k.065533", "hw": "nasturtiums", "pos": "noun", "ipa": "/nəˈstɜːrʃəmz/", "vi": "cây hoa sen cạn lá tròn ăn được"},
  {"id": "lex.en.200k.065534", "hw": "neonatologies", "pos": "noun", "ipa": "/ˌniːoʊneɪˈtɑːlədʒiz/", "vi": "chuyên ngành y học trẻ sơ sinh"},
  {"id": "lex.en.200k.065535", "hw": "nereuses", "pos": "noun", "ipa": "/ˈnɪriəsɪz/", "vi": "thần biển hiền lành Hy Lạp Nereus"},
  {"id": "lex.en.200k.065536", "hw": "nergals", "pos": "noun", "ipa": "/ˈnɜːrɡɑːlz/", "vi": "thần chiến tranh âm phủ Babylon"},
  {"id": "lex.en.200k.065537", "hw": "nonentities", "pos": "noun", "ipa": "/nɑːnˈɛntətiz/", "vi": "kẻ tầm thường vô danh; vật hư vô"},
  {"id": "lex.en.200k.065538", "hw": "orrises", "pos": "noun", "ipa": "/ˈɔːrəsɪz/", "vi": "cây diên vĩ thơm rễ làm nước hoa"},
  {"id": "lex.en.200k.065539", "hw": "overvaluations", "pos": "noun", "ipa": "/ˌoʊvərˌvæljuˈeɪʃənz/", "vi": "sự định giá quá cao vượt giá trị"},
  {"id": "lex.en.200k.065540", "hw": "pangas", "pos": "noun", "ipa": "/ˈpæŋɡəz/", "vi": "dao rựa bản rộng chặt cây châu Phi"},
  {"id": "lex.en.200k.065541", "hw": "parterres", "pos": "noun", "ipa": "/pɑːrˈtɛərz/", "vi": "vườn hoa cắt tỉa; hàng ghế trệt rạp"},
  {"id": "lex.en.200k.065542", "hw": "plevens", "pos": "noun", "ipa": "/ˈplɛvənz/", "vi": "thành phố Pleven ở Bulgaria"},
  {"id": "lex.en.200k.065543", "hw": "ploughmen", "pos": "noun", "ipa": "/ˈplaʊmən/", "vi": "thợ cày ruộng đồng (cách viết Anh)"},
  {"id": "lex.en.200k.065544", "hw": "plowmen", "pos": "noun", "ipa": "/ˈplaʊmən/", "vi": "người nông dân cày bừa đồng ruộng"},
  {"id": "lex.en.200k.065545", "hw": "puccinias", "pos": "noun", "ipa": "/pʌkˈsɪniəz/", "vi": "chi nấm gây bệnh gỉ sắt cây trồng"},
  {"id": "lex.en.200k.065546", "hw": "racemes", "pos": "noun", "ipa": "/reɪˈsiːmz/", "vi": "cụm hoa chùm mọc dọc trục chính"},
  {"id": "lex.en.200k.065547", "hw": "recidivists", "pos": "noun", "ipa": "/rɪˈsɪdɪvɪsts/", "vi": "người phạm tội tái phạm nhiều lần"},
  {"id": "lex.en.200k.065548", "hw": "rheinlands", "pos": "noun", "ipa": "/ˈraɪnlændz/", "vi": "vùng Rhineland dọc sông Rhine Đức"},
  {"id": "lex.en.200k.065549", "hw": "rotarians", "pos": "noun", "ipa": "/roʊˈtɛriənz/", "vi": "thành viên câu lạc bộ thiện nguyện"},
  {"id": "lex.en.200k.065550", "hw": "roughnecks", "pos": "noun", "ipa": "/ˈrʌfnɛks/", "vi": "công nhân giàn khoan dầu; kẻ thô lỗ"},
  {"id": "lex.en.200k.065551", "hw": "septuagenarians", "pos": "noun", "ipa": "/ˌsɛptʃuədʒəˈnɛriənz/", "vi": "người cao tuổi trong độ tuổi 70-79"},
  {"id": "lex.en.200k.065552", "hw": "skewnesses", "pos": "noun", "ipa": "/ˈskjuːnəsɪz/", "vi": "độ lệch bất đối xứng của phân phối"},
  {"id": "lex.en.200k.065553", "hw": "skuas", "pos": "noun", "ipa": "/ˈskjuːəz/", "vi": "chim cướp biển lớn vùng biển lạnh"},
  {"id": "lex.en.200k.065554", "hw": "snits", "pos": "noun", "ipa": "/snɪts/", "vi": "cơn bực bội hờn dỗi khó chịu (Mỹ)"},
  {"id": "lex.en.200k.065555", "hw": "somans", "pos": "noun", "ipa": "/ˈsoʊmənz/", "vi": "chất độc thần kinh quân sự soman"},
  {"id": "lex.en.200k.065556", "hw": "spanged", "pos": "verb", "ipa": "/spæŋd/", "vi": "đã xin tiền lẻ; đã phóng vụt qua"},
  {"id": "lex.en.200k.065557", "hw": "spanging", "pos": "verb", "ipa": "/ˈspæŋɪŋ/", "vi": "đang đi xin tiền lẻ trên phố (Mỹ)"},
  {"id": "lex.en.200k.065558", "hw": "spangs", "pos": "verb", "ipa": "/spæŋz/", "vi": "xin tiền lẻ qua đường; lao vụt qua"},
  {"id": "lex.en.200k.065559", "hw": "spirted", "pos": "verb", "ipa": "/ˈspɜːrtɪd/", "vi": "đã phun vọt tia mạnh ra ngoài"},
  {"id": "lex.en.200k.065560", "hw": "spirting", "pos": "verb", "ipa": "/ˈspɜːrtɪŋ/", "vi": "đang phun vọt thành tia mạnh"},
  {"id": "lex.en.200k.065561", "hw": "spirts", "pos": "noun", "ipa": "/spɜːrts/", "vi": "tia nước vọt mạnh; đợt bùng phát"},
  {"id": "lex.en.200k.065562", "hw": "strumpets", "pos": "noun", "ipa": "/ˈstrʌmpɪts/", "vi": "gái bán hoa; phụ nữ lẳng lơ (từ cổ)"},
  {"id": "lex.en.200k.065563", "hw": "styes", "pos": "noun", "ipa": "/staɪz/", "vi": "lẹo mắt sưng đỏ; chuồng nuôi lợn"},
  {"id": "lex.en.200k.065564", "hw": "synchronizers", "pos": "noun", "ipa": "/ˈsɪŋkrəˌnaɪzərz/", "vi": "bộ đồng bộ hộp số; mạch đồng bộ"},
  {"id": "lex.en.200k.065565", "hw": "syntagmas", "pos": "noun", "ipa": "/ˈsɪntæɡməz/", "vi": "cụm cú đoạn kết hợp từ ngữ pháp"},
  {"id": "lex.en.200k.065566", "hw": "syntagmata", "pos": "noun", "ipa": "/sɪnˈtæɡmətə/", "vi": "các cụm từ ngữ kết hợp cú đoạn"},
  {"id": "lex.en.200k.065567", "hw": "telemarks", "pos": "noun", "ipa": "/ˈtɛləmɑːrks/", "vi": "kỹ thuật cua rẽ và đáp trượt tuyết"},
  {"id": "lex.en.200k.065568", "hw": "teleprinters", "pos": "noun", "ipa": "/ˈtɛlɪˌprɪntərz/", "vi": "máy điện báo in chữ truyền tin xa"},
  {"id": "lex.en.200k.065569", "hw": "theophyllines", "pos": "noun", "ipa": "/θiˈɑːfəlɪnz/", "vi": "thuốc giãn phế quản trị hen suyễn"},
  {"id": "lex.en.200k.065570", "hw": "titrated", "pos": "verb", "ipa": "/ˈtaɪtreɪtɪd/", "vi": "đã chuẩn độ đo nồng độ dung dịch"},
  {"id": "lex.en.200k.065571", "hw": "titrates", "pos": "verb", "ipa": "/ˈtaɪtreɪts/", "vi": "chuẩn độ xác định nồng độ hóa chất"},
  {"id": "lex.en.200k.065572", "hw": "titrating", "pos": "verb", "ipa": "/ˈtaɪtreɪtɪŋ/", "vi": "đang chuẩn độ phân tích dung dịch"},
  {"id": "lex.en.200k.065573", "hw": "transcendentalists", "pos": "noun", "ipa": "/ˌtrænsənˈdɛntəlɪsts/", "vi": "người theo thuyết siêu nghiệm"},
  {"id": "lex.en.200k.065574", "hw": "upsalas", "pos": "noun", "ipa": "/ˈʊpsɑːləz/", "vi": "thành phố Uppsala của Thụy Điển"},
  {"id": "lex.en.200k.065575", "hw": "wampanoags", "pos": "noun", "ipa": "/ˌwɑːmpəˈnoʊəɡz/", "vi": "bộ tộc bản địa Wampanoag Lễ Tạ ơn"},
  {"id": "lex.en.200k.065576", "hw": "acromegalies", "pos": "noun", "ipa": "/ˌækroʊˈmɛɡəliz/", "vi": "bệnh to đầu chi do thừa hoóc môn"},
  {"id": "lex.en.200k.065577", "hw": "alexandrites", "pos": "noun", "ipa": "/ˌælɪɡˈzændraɪts/", "vi": "đá quý alexandrite biến đổi màu"},
  {"id": "lex.en.200k.065578", "hw": "antakyas", "pos": "noun", "ipa": "/ɑːnˈtɑːkjəz/", "vi": "thành phố Antakya (Antioch) Thổ Nhĩ"},
  {"id": "lex.en.200k.065579", "hw": "autarkies", "pos": "noun", "ipa": "/ˈɔːtɑːrkiz/", "vi": "chính sách kinh tế tự cung tự cấp"},
  {"id": "lex.en.200k.065580", "hw": "autodidacts", "pos": "noun", "ipa": "/ˌɔːtoʊˈdaɪdækts/", "vi": "người tự học không qua trường lớp"},
  {"id": "lex.en.200k.065581", "hw": "avocets", "pos": "noun", "ipa": "/ˈævəsɛts/", "vi": "chim mỏ hếch chân cao kiếm ăn đầm"},
  {"id": "lex.en.200k.065582", "hw": "backpedaled", "pos": "verb", "ipa": "/ˈbækˌpɛdəld/", "vi": "đã đạp lùi lại; đã rút lui ý kiến"},
  {"id": "lex.en.200k.065583", "hw": "backpedaling", "pos": "verb", "ipa": "/ˈbækˌpɛdəlɪŋ/", "vi": "đang đạp xe lùi; đang rút lại lời"},
  {"id": "lex.en.200k.065584", "hw": "backpedals", "pos": "verb", "ipa": "/ˈbækˌpɛdəlz/", "vi": "đạp lùi xe; rút lui khỏi lập trường"},
  {"id": "lex.en.200k.065585", "hw": "balatons", "pos": "noun", "ipa": "/ˈbɑːlətɑːnz/", "vi": "hồ nước ngọt lớn Balaton ở Hungary"},
  {"id": "lex.en.200k.065586", "hw": "bayas", "pos": "noun", "ipa": "/ˈbaɪəz/", "vi": "chim rồng rộc vàng dệt tổ rủ baya"},
  {"id": "lex.en.200k.065587", "hw": "belabored", "pos": "verb", "ipa": "/bɪˈleɪbərd/", "vi": "đã giảng dông dài; đã đánh tơi bời"},
  {"id": "lex.en.200k.065588", "hw": "belaboring", "pos": "verb", "ipa": "/bɪˈleɪbərɪŋ/", "vi": "đang nói mãi dông dài; đánh tơi bời"},
  {"id": "lex.en.200k.065589", "hw": "belabors", "pos": "verb", "ipa": "/bɪˈleɪbərz/", "vi": "bàn mãi không dứt; chỉ trích đánh"},
  {"id": "lex.en.200k.065590", "hw": "bestowals", "pos": "noun", "ipa": "/bɪˈstoʊəlz/", "vi": "sự ban tặng trao tặng danh hiệu"},
  {"id": "lex.en.200k.065591", "hw": "blancmanges", "pos": "noun", "ipa": "/bləˈmɑːndʒɪz/", "vi": "món tráng miệng kem sữa hạnh nhân"},
  {"id": "lex.en.200k.065592", "hw": "bovrils", "pos": "noun", "ipa": "/ˈbɒvrɪlz/", "vi": "cao thịt bò đậm đặc Bovril (Anh)"},
  {"id": "lex.en.200k.065593", "hw": "bracts", "pos": "noun", "ipa": "/brækts/", "vi": "lá bắc biến đổi mọc dưới cụm hoa"},
  {"id": "lex.en.200k.065594", "hw": "carthusians", "pos": "noun", "ipa": "/kɑːrˈθuːʒənz/", "vi": "tu sĩ khổ hạnh dòng Carthusian"},
  {"id": "lex.en.200k.065595", "hw": "chaffinches", "pos": "noun", "ipa": "/ˈtʃæfɪntʃɪz/", "vi": "chim sẻ rừng chaffinch hót hay Âu"},
  {"id": "lex.en.200k.065596", "hw": "chitons", "pos": "noun", "ipa": "/ˈkaɪtənz/", "vi": "ốc song kinh tám mảnh vỏ; áo cổ Hy"},
  {"id": "lex.en.200k.065597", "hw": "churchwardens", "pos": "noun", "ipa": "/ˌtʃɜːrtʃˈwɔːrdənz/", "vi": "người quản lý tài sản giáo xứ Anh"},
  {"id": "lex.en.200k.065598", "hw": "clothespins", "pos": "noun", "ipa": "/ˈkloʊðzpɪnz/", "vi": "kẹp gỗ hoặc nhựa phơi giữ quần áo"},
  {"id": "lex.en.200k.065599", "hw": "colchides", "pos": "noun", "ipa": "/ˈkɑːlkədiːz/", "vi": "vùng cổ Colchis bờ đông Biển Đen"},
  {"id": "lex.en.200k.065600", "hw": "conciliators", "pos": "noun", "ipa": "/kənˈsɪliˌeɪtərz/", "vi": "người hòa giải đứng ra dàn xếp êm"},
  {"id": "lex.en.200k.065601", "hw": "consistences", "pos": "noun", "ipa": "/kənˈsɪstənsɪz/", "vi": "độ đặc sệt; tính nhất quán (từ ít)"},
  {"id": "lex.en.200k.065602", "hw": "coquilles", "pos": "noun", "ipa": "/koʊˈkiːz/", "vi": "vỏ sò điệp; món sò điệp nướng phô"}
]

with open('scratch/b34_r02_raw_p1.json') as f:
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

with open('scratch/b34_r02_p1.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r02_p1.json OK")
