import json

items = [
  {"id": "lex.en.200k.064203", "hw": "immunosuppressants", "pos": "noun", "ipa": "/ˌɪmjʊnoʊsəˈprɛsənts/", "vi": "thuốc ức chế hệ miễn dịch ghép tạng"},
  {"id": "lex.en.200k.064204", "hw": "ismailis", "pos": "noun", "ipa": "/ɪzˈmaɪliz/", "vi": "tín đồ nhánh Hồi giáo Shia Ismaili"},
  {"id": "lex.en.200k.064205", "hw": "kukis", "pos": "noun", "ipa": "/ˈkuːkiz/", "vi": "nhóm dân tộc và tiếng Kuki Ấn-Miến"},
  {"id": "lex.en.200k.064206", "hw": "kyanites", "pos": "noun", "ipa": "/ˈkaɪənaɪts/", "vi": "khoáng vật đá xanh lam kyanite"},
  {"id": "lex.en.200k.064207", "hw": "limonenes", "pos": "noun", "ipa": "/ˈlɪməniːnz/", "vi": "tinh dầu hương cam chanh limonene"},
  {"id": "lex.en.200k.064208", "hw": "lycias", "pos": "noun", "ipa": "/ˈlɪʃəz/", "vi": "vùng cổ Lycia ở tây nam Thổ Nhĩ Kỳ"},
  {"id": "lex.en.200k.064209", "hw": "lysosomes", "pos": "noun", "ipa": "/ˈlaɪsəˌsoʊmz/", "vi": "bào quan tiêu thể phân hủy tế bào"},
  {"id": "lex.en.200k.064210", "hw": "macguffins", "pos": "noun", "ipa": "/məˈɡʌfɪnz/", "vi": "yếu tố mồi dẫn dắt cốt truyện phim"},
  {"id": "lex.en.200k.064211", "hw": "maharanis", "pos": "noun", "ipa": "/ˌmɑːhəˈrɑːniz/", "vi": "hoàng hậu hoặc nữ vương Ấn Độ xưa"},
  {"id": "lex.en.200k.064212", "hw": "maserus", "pos": "noun", "ipa": "/məˈsɛruːz/", "vi": "thủ đô Maseru của nước Lesotho"},
  {"id": "lex.en.200k.064213", "hw": "milquetoasts", "pos": "noun", "ipa": "/ˈmɪlktoʊsts/", "vi": "người nhút nhát rụt rè nhu nhược"},
  {"id": "lex.en.200k.064214", "hw": "misapplications", "pos": "noun", "ipa": "/ˌmɪsæpləˈkeɪʃənz/", "vi": "sự dùng sai mục đích; áp dụng nhầm"},
  {"id": "lex.en.200k.064215", "hw": "misdeeds", "pos": "noun", "ipa": "/ˌmɪsˈdiːdz/", "vi": "hành vi sai trái tội lỗi bất chính"},
  {"id": "lex.en.200k.064216", "hw": "monods", "pos": "noun", "ipa": "/moʊˈnɑːdz/", "vi": "nhà sinh học Nobel Jacques Monod"},
  {"id": "lex.en.200k.064217", "hw": "mouseyer", "pos": "adj", "ipa": "/ˈmaʊsiər/", "vi": "rụt rè lặng lẽ hơn; xám xịt hơn"},
  {"id": "lex.en.200k.064218", "hw": "mouseyest", "pos": "adj", "ipa": "/ˈmaʊsiɪst/", "vi": "nhút nhát rụt rè nhất; xám xịt nhất"},
  {"id": "lex.en.200k.064219", "hw": "muybridges", "pos": "noun", "ipa": "/ˈmaɪbrɪdʒɪz/", "vi": "nhiếp ảnh gia tiên phong Muybridge"},
  {"id": "lex.en.200k.064220", "hw": "nincompoops", "pos": "noun", "ipa": "/ˈnɪŋkəmˌpuːps/", "vi": "kẻ khờ khạo ngốc nghếch ngu dốt"},
  {"id": "lex.en.200k.064221", "hw": "opuntias", "pos": "noun", "ipa": "/oʊˈpʌntiəz/", "vi": "chi cây xương rồng tai thỏ lê gai"},
  {"id": "lex.en.200k.064222", "hw": "osteotomies", "pos": "noun", "ipa": "/ˌɑːstiˈɑːtəmiz/", "vi": "phẫu thuật cắt chỉnh hình xương"},
  {"id": "lex.en.200k.064223", "hw": "persuaders", "pos": "noun", "ipa": "/pərˈsweɪdərz/", "vi": "người thuyết phục giỏi; vũ khí ép"},
  {"id": "lex.en.200k.064224", "hw": "phlebotomists", "pos": "noun", "ipa": "/flɪˈbɑːtəmɪsts/", "vi": "kỹ thuật viên lấy máu xét nghiệm"},
  {"id": "lex.en.200k.064225", "hw": "phosgenes", "pos": "noun", "ipa": "/ˈfɑːzdʒiːnz/", "vi": "khí độc công nghiệp phosgene"},
  {"id": "lex.en.200k.064226", "hw": "physicalisms", "pos": "noun", "ipa": "/ˈfɪzɪkəˌlɪzəmz/", "vi": "học thuyết triết học duy vật lý"},
  {"id": "lex.en.200k.064227", "hw": "pistils", "pos": "noun", "ipa": "/ˈpɪstəlz/", "vi": "bộ phận nhụy cái chứa bầu noãn hoa"},
  {"id": "lex.en.200k.064228", "hw": "pkds", "pos": "noun", "ipa": "/ˌpiːˌkeɪˈdiːz/", "vi": "bệnh thận đa nang di truyền PKD"},
  {"id": "lex.en.200k.064229", "hw": "planetoids", "pos": "noun", "ipa": "/ˈplænətɔɪdz/", "vi": "tiểu hành tinh quay quanh Mặt Trời"},
  {"id": "lex.en.200k.064230", "hw": "polonaises", "pos": "noun", "ipa": "/ˌpɑːləˈneɪzɪz/", "vi": "điệu múa Ba Lan; kiểu váy polonaise"},
  {"id": "lex.en.200k.064231", "hw": "premolars", "pos": "noun", "ipa": "/priːˈmoʊlərz/", "vi": "răng tiền hàm nằm giữa nanh và hàm"},
  {"id": "lex.en.200k.064232", "hw": "psoases", "pos": "noun", "ipa": "/ˈsoʊəsɪz/", "vi": "cơ thắt lưng chậu nối cột sống đùi"},
  {"id": "lex.en.200k.064233", "hw": "psylliums", "pos": "noun", "ipa": "/ˈsɪliəmz/", "vi": "vỏ hạt mã đề giàu chất xơ tiêu hóa"},
  {"id": "lex.en.200k.064234", "hw": "rambouillets", "pos": "noun", "ipa": "/ˌræmbuˈjeɪz/", "vi": "giống cừu lấy len thịt Rambouillet"},
  {"id": "lex.en.200k.064235", "hw": "rangier", "pos": "adj", "ipa": "/ˈreɪndʒiər/", "vi": "cao gầy chân dài thon gọn hơn"},
  {"id": "lex.en.200k.064236", "hw": "rangiest", "pos": "adj", "ipa": "/ˈreɪndʒiɪst/", "vi": "cao gầy chân tay dài thon nhất"},
  {"id": "lex.en.200k.064237", "hw": "resisters", "pos": "noun", "ipa": "/rɪˈzɪstərz/", "vi": "người kháng cự chống đối; điện trở"},
  {"id": "lex.en.200k.064238", "hw": "revolutionists", "pos": "noun", "ipa": "/ˌrɛvəˈluːʃənɪsts/", "vi": "nhà cách mạng đấu tranh lật đổ cũ"},
  {"id": "lex.en.200k.064239", "hw": "rhomboids", "pos": "noun", "ipa": "/ˈrɑːmbɔɪdz/", "vi": "hình bình hành lệch; cơ trám lưng"},
  {"id": "lex.en.200k.064240", "hw": "rondeaus", "pos": "noun", "ipa": "/ˈrɑːndoʊz/", "vi": "thể thơ rondo; khúc nhạc điệp khúc"},
  {"id": "lex.en.200k.064241", "hw": "rondeaux", "pos": "noun", "ipa": "/ˈrɑːndoʊz/", "vi": "các bài thơ cổ Pháp 15 câu rondo"},
  {"id": "lex.en.200k.064242", "hw": "rumanians", "pos": "noun", "ipa": "/ruˈmeɪniənz/", "vi": "người dân và tiếng nước Romania"},
  {"id": "lex.en.200k.064243", "hw": "sauropods", "pos": "noun", "ipa": "/ˈsɔːrəpɑːdz/", "vi": "khủng long cổ dài bốn chân ăn cỏ"},
  {"id": "lex.en.200k.064244", "hw": "sbws", "pos": "noun", "ipa": "/ˌɛsˌbiːˈdʌbəljuːz/", "vi": "hướng la bàn Nam lệch Tây (SbW)"},
  {"id": "lex.en.200k.064245", "hw": "sephardim", "pos": "noun", "ipa": "/səˈfɑːrdɪm/", "vi": "cộng đồng Do Thái gốc Tây Ban Nha"},
  {"id": "lex.en.200k.064246", "hw": "sephardis", "pos": "noun", "ipa": "/səˈfɑːrdiz/", "vi": "người Do Thái gốc bán đảo Iberia"},
  {"id": "lex.en.200k.064247", "hw": "solans", "pos": "noun", "ipa": "/ˈsoʊlənz/", "vi": "chim ó biển trắng gannet phương Bắc"},
  {"id": "lex.en.200k.064248", "hw": "subheadings", "pos": "noun", "ipa": "/ˈsʌbˌhɛdɪŋz/", "vi": "tiêu đề phụ chia mục nhỏ văn bản"},
  {"id": "lex.en.200k.064249", "hw": "taipans", "pos": "noun", "ipa": "/ˈtaɪpænz/", "vi": "rắn độc taipan Úc; trùm buôn lớn"},
  {"id": "lex.en.200k.064250", "hw": "tairas", "pos": "noun", "ipa": "/ˈtaɪrəz/", "vi": "chồn đen rừng nhiệt đới Nam Mỹ"},
  {"id": "lex.en.200k.064251", "hw": "tartuffes", "pos": "noun", "ipa": "/tɑːrˈtuːfs/", "vi": "kẻ đạo đức giả dối xảo trá"},
  {"id": "lex.en.200k.064252", "hw": "tenderfoots", "pos": "noun", "ipa": "/ˈtɛndərfʊts/", "vi": "lính mới non kinh nghiệm chân ướt"},
  {"id": "lex.en.200k.064253", "hw": "tennos", "pos": "noun", "ipa": "/ˈtɛnoʊz/", "vi": "Thiên hoàng hoàng đế nước Nhật Bản"},
  {"id": "lex.en.200k.064254", "hw": "tilers", "pos": "noun", "ipa": "/ˈtaɪlərz/", "vi": "thợ lát gạch men ngói; bảo vệ hội"},
  {"id": "lex.en.200k.064255", "hw": "torchbearers", "pos": "noun", "ipa": "/ˈtɔːrtʃˌbɛrərz/", "vi": "người rước đuốc; người dẫn đường"},
  {"id": "lex.en.200k.064256", "hw": "tuskers", "pos": "noun", "ipa": "/ˈtʌskərz/", "vi": "voi đực ngà dài; thú có ngà lớn"},
  {"id": "lex.en.200k.064257", "hw": "unnerves", "pos": "verb", "ipa": "/ʌnˈnɜːrvz/", "vi": "làm bủn rủn mất bình tĩnh can đảm"},
  {"id": "lex.en.200k.064258", "hw": "valguses", "pos": "noun", "ipa": "/ˈvælɡəsɪz/", "vi": "dị tật khớp gối hay ngón vẹo ngoài"},
  {"id": "lex.en.200k.064259", "hw": "vanillins", "pos": "noun", "ipa": "/vəˈnɪlɪnz/", "vi": "chất tạo hương thơm vani vanilin"},
  {"id": "lex.en.200k.064260", "hw": "veldts", "pos": "noun", "ipa": "/vɛlts/", "vi": "thảo nguyên cỏ bụi rộng ở Nam Phi"},
  {"id": "lex.en.200k.064261", "hw": "vendees", "pos": "noun", "ipa": "/vɛnˈdiːz/", "vi": "bên mua tài sản hoặc bất động sản"},
  {"id": "lex.en.200k.064262", "hw": "vesaliuses", "pos": "noun", "ipa": "/vəˈseɪliəsɪz/", "vi": "cha đẻ giải phẫu hiện đại Vesalius"},
  {"id": "lex.en.200k.064263", "hw": "volcanologies", "pos": "noun", "ipa": "/ˌvɑːlkəˈnɑːlədʒiz/", "vi": "ngành khoa học nghiên cứu núi lửa"},
  {"id": "lex.en.200k.064264", "hw": "artemisia annua", "pos": "phrase", "ipa": "/ˌɑːrtəˈmiːʒə ˈænjuə/", "vi": "cây thanh hao hoa vàng trị sốt rét"},
  {"id": "lex.en.200k.064265", "hw": "atrial auricle", "pos": "phrase", "ipa": "/ˈeɪtriəl ˈɔːrɪkəl/", "vi": "tiểu nhĩ phần phụ nhỏ của tâm nhĩ"},
  {"id": "lex.en.200k.064266", "hw": "balas ruby", "pos": "phrase", "ipa": "/ˈbælɪs ˈruːbi/", "vi": "đá quý spinel hồng giống hồng ngọc"},
  {"id": "lex.en.200k.064267", "hw": "black bindweed", "pos": "phrase", "ipa": "/blæk ˈbaɪndwiːd/", "vi": "dây leo cỏ kiều mạch đen hại ruộng"},
  {"id": "lex.en.200k.064268", "hw": "black salsify", "pos": "phrase", "ipa": "/blæk ˈsælsəfi/", "vi": "cây rễ đen ăn củ bổ dưỡng châu Âu"},
  {"id": "lex.en.200k.064269", "hw": "bobwhite quail", "pos": "phrase", "ipa": "/ˈbɑːbwaɪt kweɪl/", "vi": "chim cút đồng cỏ cổ trắng Bắc Mỹ"},
  {"id": "lex.en.200k.064270", "hw": "bufo bufo", "pos": "phrase", "ipa": "/ˈbjuːfoʊ ˈbjuːfoʊ/", "vi": "loài cóc nâu phổ biến khắp châu Âu"},
  {"id": "lex.en.200k.064271", "hw": "carline thistle", "pos": "phrase", "ipa": "/ˈkɑːrlaɪn ˈθɪsəl/", "vi": "cây kế gai lùn Carlina mọc đồng khô"},
  {"id": "lex.en.200k.064272", "hw": "carnauba palm", "pos": "phrase", "ipa": "/kɑːrˈnɔːbə pɑːm/", "vi": "cây cọ lá phủ sáp carnauba Brazil"},
  {"id": "lex.en.200k.064273", "hw": "carnauba wax", "pos": "phrase", "ipa": "/kɑːrˈnɔːbə wæks/", "vi": "sáp thực vật bóng cứng carnauba"},
  {"id": "lex.en.200k.064274", "hw": "chickweed phlox", "pos": "phrase", "ipa": "/ˈtʃɪkwiːd flɑːks/", "vi": "cây hoa phlox thảm mọc bò thấp"},
  {"id": "lex.en.200k.064275", "hw": "common carline thistle", "pos": "phrase", "ipa": "/ˈkɑːmən ˈkɑːrlaɪn ˈθɪsəl/", "vi": "cây kế gai lùn châu Âu Carlina"},
  {"id": "lex.en.200k.064276", "hw": "common scoter", "pos": "phrase", "ipa": "/ˈkɑːmən ˈskoʊtər/", "vi": "vịt biển lông đen tuyền lặn sâu"},
  {"id": "lex.en.200k.064277", "hw": "creeping oxalis", "pos": "phrase", "ipa": "/ˈkriːpɪŋ ɑːkˈseɪlɪs/", "vi": "cây chua me đất hoa vàng mọc bò"},
  {"id": "lex.en.200k.064278", "hw": "desiderius erasmus", "pos": "phrase", "ipa": "/ˌdɛzəˈdɪriəs ɪˈræzməs/", "vi": "học giả nhân văn Phục Hưng Erasmus"},
  {"id": "lex.en.200k.064279", "hw": "dishcloth gourd", "pos": "phrase", "ipa": "/ˈdɪʃklɔːθ ɡʊərd/", "vi": "cây quả mướp hương lấy xơ cọ rửa"},
  {"id": "lex.en.200k.064280", "hw": "edmond rostand", "pos": "phrase", "ipa": "/ˈɛdmɑːn rɔːˈstɑːn/", "vi": "nhà viết kịch Pháp Edmond Rostand"},
  {"id": "lex.en.200k.064281", "hw": "family poaceae", "pos": "phrase", "ipa": "/ˈfæməli poʊˈeɪsiˌiː/", "vi": "họ thực vật Hòa thảo gồm lúa và cỏ"},
  {"id": "lex.en.200k.064282", "hw": "field bindweed", "pos": "phrase", "ipa": "/fiːld ˈbaɪndwiːd/", "vi": "cỏ bìm bìm đồng hoa trắng hồng"},
  {"id": "lex.en.200k.064283", "hw": "gefilte fish", "pos": "phrase", "ipa": "/ɡəˈfɪltə fɪʃ/", "vi": "món chả cá viên luộc Do Thái"},
  {"id": "lex.en.200k.064284", "hw": "genus aconitum", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌækəˈnaɪtəm/", "vi": "chi cây phụ tử ô đầu chứa độc tố"},
  {"id": "lex.en.200k.064285", "hw": "genus agapanthus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌæɡəˈpænθəs/", "vi": "chi hoa huệ xanh sông Nile đẹp"},
  {"id": "lex.en.200k.064286", "hw": "genus eumenes", "pos": "phrase", "ipa": "/ˈdʒiːnəs juːˈmiːniːz/", "vi": "chi ong tò vò thợ nề xây tổ đất"},
  {"id": "lex.en.200k.064287", "hw": "genus hyla", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈhaɪlə/", "vi": "chi nhái bén cây có giác bám chân"},
  {"id": "lex.en.200k.064288", "hw": "genus indri", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈɪndri/", "vi": "chi vượn cáo lớn không đuôi Indri"},
  {"id": "lex.en.200k.064289", "hw": "genus jabiru", "pos": "phrase", "ipa": "/ˈdʒiːnəs dʒəˈbɪruː/", "vi": "chi chim hạc cổ trụi lớn Jabiru"},
  {"id": "lex.en.200k.064290", "hw": "genus larix", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈlɛrɪks/", "vi": "chi cây thông rụng lá vùng ôn đới"},
  {"id": "lex.en.200k.064291", "hw": "genus mustela", "pos": "phrase", "ipa": "/ˈdʒiːnəs mʌˈstɛlə/", "vi": "chi động vật chồn hôi chồn triết"},
  {"id": "lex.en.200k.064292", "hw": "genus sitta", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈsɪtə/", "vi": "chi chim trèo cây mỏ nhọn Sitta"},
  {"id": "lex.en.200k.064293", "hw": "glenoid fossa", "pos": "phrase", "ipa": "/ˈɡliːnɔɪd ˈfɑːsə/", "vi": "hõm chảo khớp xương bả vai và hàm"},
  {"id": "lex.en.200k.064294", "hw": "golfo de campeche", "pos": "phrase", "ipa": "/ˈɡɔːlfoʊ deɪ kɑːmˈpeɪtʃeɪ/", "vi": "vịnh Campeche phía nam vịnh Mexico"},
  {"id": "lex.en.200k.064295", "hw": "hedge bindweed", "pos": "phrase", "ipa": "/hɛdʒ ˈbaɪndwiːd/", "vi": "dây bìm bìm rào hoa loa kèn trắng"},
  {"id": "lex.en.200k.064296", "hw": "honore daumier", "pos": "phrase", "ipa": "/ɔːnɔːˈreɪ doʊˈmjeɪ/", "vi": "họa sĩ biếm họa Pháp Daumier"},
  {"id": "lex.en.200k.064297", "hw": "ipomoea alba", "pos": "phrase", "ipa": "/ˌaɪpəˈmiːə ˈælbə/", "vi": "dây hoa dạ quỳnh bìm bìm nở đêm"},
  {"id": "lex.en.200k.064298", "hw": "ipomoea nil", "pos": "phrase", "ipa": "/ˌaɪpəˈmiːə nɪl/", "vi": "cây bìm bìm xanh hạt làm thuốc"},
  {"id": "lex.en.200k.064299", "hw": "johann winckelmann", "pos": "phrase", "ipa": "/ˈjoʊhɑːn ˈvɪŋkəlmɑːn/", "vi": "nhà sử học nghệ thuật Winckelmann"},
  {"id": "lex.en.200k.064300", "hw": "jook house", "pos": "phrase", "ipa": "/dʒuːk haʊs/", "vi": "quán bar bình dân có nhạc nhảy (Mỹ)"},
  {"id": "lex.en.200k.064301", "hw": "jook joint", "pos": "phrase", "ipa": "/dʒuːk dʒɔɪnt/", "vi": "quán rượu nhạc nhảy bình dân (Mỹ)"},
  {"id": "lex.en.200k.064302", "hw": "leydig cell", "pos": "phrase", "ipa": "/ˈlaɪdɪɡ sɛl/", "vi": "tế bào kẽ Leydig tiết testosterone"}
]

with open('scratch/b33_r09_raw_p3.json') as f:
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

with open('scratch/b33_r09_p3.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r09_p3.json OK")
