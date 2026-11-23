import json

records = [
    {"id": "lex.en.200k.057802", "hw": "pari passu", "pos": "phrase", "ipa": "", "vi": "ngang hàng bình đẳng; cùng tỷ lệ"},
    {"id": "lex.en.200k.057803", "hw": "pearl hominy", "pos": "phrase", "ipa": "", "vi": "hạt bắp ngô ninh vôi xát ngọc"},
    {"id": "lex.en.200k.057804", "hw": "potbelly stove", "pos": "phrase", "ipa": "", "vi": "bếp lò sưởi gang hình bụng phệ"},
    {"id": "lex.en.200k.057805", "hw": "propyl alcohol", "pos": "phrase", "ipa": "", "vi": "cồn propyl alcohol; propanol"},
    {"id": "lex.en.200k.057806", "hw": "propyl group", "pos": "phrase", "ipa": "", "vi": "gốc hóa học propyl"},
    {"id": "lex.en.200k.057807", "hw": "propyl radical", "pos": "phrase", "ipa": "", "vi": "gốc tự do propyl trong hóa học"},
    {"id": "lex.en.200k.057808", "hw": "raja laevis", "pos": "phrase", "ipa": "", "vi": "loài cá đuối gai Raja laevis"},
    {"id": "lex.en.200k.057809", "hw": "restriction nuclease", "pos": "phrase", "ipa": "", "vi": "enzim cắt giới hạn endonuclease"},
    {"id": "lex.en.200k.057810", "hw": "royal osmund", "pos": "phrase", "ipa": "", "vi": "dương xỉ hoàng gia Osmunda regalis"},
    {"id": "lex.en.200k.057811", "hw": "rudolf wurlitzer", "pos": "phrase", "ipa": "", "vi": "nhà sản xuất đàn Rudolf Wurlitzer"},
    {"id": "lex.en.200k.057812", "hw": "russian wolfhound", "pos": "phrase", "ipa": "", "vi": "chó săn sói Borzoi nước Nga"},
    {"id": "lex.en.200k.057813", "hw": "samuel gompers", "pos": "phrase", "ipa": "", "vi": "lãnh tụ công đoàn Samuel Gompers"},
    {"id": "lex.en.200k.057814", "hw": "sedum acre", "pos": "phrase", "ipa": "", "vi": "cây bỏng vàng Sedum acre mọng nước"},
    {"id": "lex.en.200k.057815", "hw": "skeen arch", "pos": "phrase", "ipa": "", "vi": "vòm cuốn dẹp; vòm cung thoai thoải"},
    {"id": "lex.en.200k.057816", "hw": "soliton wave", "pos": "phrase", "ipa": "", "vi": "sóng độc hành soliton trong vật lý"},
    {"id": "lex.en.200k.057817", "hw": "teres major", "pos": "phrase", "ipa": "", "vi": "cơ tròn lớn ở bả vai"},
    {"id": "lex.en.200k.057818", "hw": "teres major muscle", "pos": "phrase", "ipa": "", "vi": "bắp cơ tròn lớn giải phẫu bả vai"},
    {"id": "lex.en.200k.057819", "hw": "teres minor", "pos": "phrase", "ipa": "", "vi": "cơ tròn bé ở bả vai cánh tay"},
    {"id": "lex.en.200k.057820", "hw": "teres minor muscle", "pos": "phrase", "ipa": "", "vi": "bắp cơ tròn bé khớp vai"},
    {"id": "lex.en.200k.057821", "hw": "teres muscle", "pos": "phrase", "ipa": "", "vi": "các nhóm cơ tròn bả vai"},
    {"id": "lex.en.200k.057822", "hw": "trigeminal neuralgia", "pos": "phrase", "ipa": "", "vi": "chứng đau dây thần kinh sinh ba"},
    {"id": "lex.en.200k.057823", "hw": "tunisian dirham", "pos": "phrase", "ipa": "", "vi": "đồng tiền tệ dirham Tunisia"},
    {"id": "lex.en.200k.057824", "hw": "vena gluteus", "pos": "phrase", "ipa": "", "vi": "tĩnh mạch vùng mông chậu"},
    {"id": "lex.en.200k.057825", "hw": "vinifera grape", "pos": "phrase", "ipa": "", "vi": "giống nho làm rượu Vitis vinifera"},
    {"id": "lex.en.200k.057826", "hw": "walter gropius", "pos": "phrase", "ipa": "", "vi": "kiến trúc sư Walter Gropius Bauhaus"},
    {"id": "lex.en.200k.057827", "hw": "writ of mandamus", "pos": "phrase", "ipa": "", "vi": "lệnh tư pháp mandamus của tòa án"},
    {"id": "lex.en.200k.057828", "hw": "adenoviruses", "pos": "noun", "ipa": "/ˌædənoʊˈvaɪrəsɪz/", "vi": "các vi-rút adenovirus gây bệnh"},
    {"id": "lex.en.200k.057829", "hw": "akkas", "pos": "noun", "ipa": "/ˈɑːkəz/", "vi": "thành phố cổ Akka; bộ tộc Akka"},
    {"id": "lex.en.200k.057830", "hw": "ammonites", "pos": "noun", "ipa": "/ˈæmənaɪts/", "vi": "hóa thạch cúc đá cúc biển xoắn"},
    {"id": "lex.en.200k.057831", "hw": "andesites", "pos": "noun", "ipa": "/ˈændəsaɪts/", "vi": "các loại đá mác-ma andesit núi lửa"},
    {"id": "lex.en.200k.057832", "hw": "anhydrides", "pos": "noun", "ipa": "/ænˈhaɪdraɪdz/", "vi": "các hợp chất anhiđrit axit khan"},
    {"id": "lex.en.200k.057833", "hw": "annuli", "pos": "noun", "ipa": "/ˈænjʊlaɪ/", "vi": "hình vành khăn; vòng tròn đốt thân"},
    {"id": "lex.en.200k.057834", "hw": "aperitifs", "pos": "noun", "ipa": "/əˌpɛrəˈtiːfs/", "vi": "các loại rượu khai vị nhẹ bữa ăn"},
    {"id": "lex.en.200k.057835", "hw": "autoclaves", "pos": "noun", "ipa": "/ˈɔːtoʊkleɪvz/", "vi": "nồi hấp tiệt trùng áp suất cao"},
    {"id": "lex.en.200k.057836", "hw": "balanchines", "pos": "noun", "ipa": "/ˈbæləntʃiːnz/", "vi": "biên đạo ba lê George Balanchine"},
    {"id": "lex.en.200k.057837", "hw": "bivouacked", "pos": "verb", "ipa": "/ˈbɪvuækt/", "vi": "đã cắm trại dã chiến lộ thiên"},
    {"id": "lex.en.200k.057838", "hw": "bivouacs", "pos": "noun", "ipa": "/ˈbɪvuæks/", "vi": "trại dã chiến tạm thời ngoài trời"},
    {"id": "lex.en.200k.057839", "hw": "blarneyed", "pos": "verb", "ipa": "/ˈblɑːrnid/", "vi": "đã khéo nịnh hót; đã dỗ ngọt"},
    {"id": "lex.en.200k.057840", "hw": "blarneying", "pos": "verb", "ipa": "/ˈblɑːrniɪŋ/", "vi": "đang khéo nịnh hót dỗ ngọt"},
    {"id": "lex.en.200k.057841", "hw": "blarneys", "pos": "noun", "ipa": "/ˈblɑːrniz/", "vi": "những lời tán tụng dỗ ngọt bùi tai"},
    {"id": "lex.en.200k.057842", "hw": "blowhards", "pos": "noun", "ipa": "/ˈbloʊhɑːrdz/", "vi": "những kẻ huênh hoang khoác lác"},
    {"id": "lex.en.200k.057843", "hw": "bocces", "pos": "noun", "ipa": "/ˈbɑːtʃiz/", "vi": "trò chơi ném bi sắt bocce kiểu Ý"},
    {"id": "lex.en.200k.057844", "hw": "breadfruits", "pos": "noun", "ipa": "/ˈbrɛdfruːts/", "vi": "quả sa kê; cây sa kê nhiệt đới"},
    {"id": "lex.en.200k.057845", "hw": "bunces", "pos": "noun", "ipa": "/ˈbʌnsɪz/", "vi": "những món tiền hời bất ngờ may mắn"},
    {"id": "lex.en.200k.057846", "hw": "camorras", "pos": "noun", "ipa": "/kəˈmɔːrəz/", "vi": "băng đảng mafia Camorra xứ Napoli"},
    {"id": "lex.en.200k.057847", "hw": "cannaes", "pos": "noun", "ipa": "/ˈkæniːz/", "vi": "chiến trường trận Cannae cổ đại"},
    {"id": "lex.en.200k.057848", "hw": "categorisations", "pos": "noun", "ipa": "/ˌkætəɡəraɪˈzeɪʃənz/", "vi": "sự phân loại; xếp đặt vào danh mục"},
    {"id": "lex.en.200k.057849", "hw": "cheapskates", "pos": "noun", "ipa": "/ˈtʃiːpskeɪts/", "vi": "những kẻ keo kiệt bủn xỉn kẹt xỉ"},
    {"id": "lex.en.200k.057850", "hw": "circumnavigated", "pos": "verb", "ipa": "/ˌsɜːrkəmˈnævɪɡeɪtɪd/", "vi": "đã đi vòng quanh trái đất bằng tàu"},
    {"id": "lex.en.200k.057851", "hw": "circumnavigates", "pos": "verb", "ipa": "/ˌsɜːrkəmˈnævɪɡeɪts/", "vi": "đi thuyền vòng quanh quả đất"},
    {"id": "lex.en.200k.057852", "hw": "circumnavigating", "pos": "verb", "ipa": "/ˌsɜːrkəmˈnævɪɡeɪtɪŋ/", "vi": "đang đi vòng quanh thế giới"},
    {"id": "lex.en.200k.057853", "hw": "compotes", "pos": "noun", "ipa": "/ˈkɑːmpoʊts/", "vi": "món mứt hoa quả hầm nước đường"},
    {"id": "lex.en.200k.057854", "hw": "continuos", "pos": "noun", "ipa": "/kənˈtɪnjuoʊz/", "vi": "phần bè trầm đệm liên tục basso"},
    {"id": "lex.en.200k.057855", "hw": "costumers", "pos": "noun", "ipa": "/ˈkɑːstuːmɚz/", "vi": "nhà thiết kế trang phục sân khấu"},
    {"id": "lex.en.200k.057856", "hw": "cremonas", "pos": "noun", "ipa": "/krəˈmoʊnəz/", "vi": "thành phố Cremona cái nôi violin"},
    {"id": "lex.en.200k.057857", "hw": "cudgeled", "pos": "verb", "ipa": "/ˈkʌdʒəld/", "vi": "đã giáng đòn bằng gậy gộc dùi cui"},
    {"id": "lex.en.200k.057858", "hw": "cudgeling", "pos": "verb", "ipa": "/ˈkʌdʒəlɪŋ/", "vi": "đang đánh đập bằng gậy gộc dùi cui"},
    {"id": "lex.en.200k.057859", "hw": "culbertsons", "pos": "noun", "ipa": "/ˈkʌlbɚtsənz/", "vi": "chuyên gia bài Ely Culbertson"},
    {"id": "lex.en.200k.057860", "hw": "dimwits", "pos": "noun", "ipa": "/ˈdɪmwɪts/", "vi": "những kẻ ngu si đầu óc đần độn"},
    {"id": "lex.en.200k.057861", "hw": "dipsticks", "pos": "noun", "ipa": "/ˈdɪpstɪks/", "vi": "que thăm dò mức dầu nhớt động cơ"},
    {"id": "lex.en.200k.057862", "hw": "dissenters", "pos": "noun", "ipa": "/dɪˈsɛntɚz/", "vi": "người bất đồng chính kiến quan điểm"},
    {"id": "lex.en.200k.057863", "hw": "diviners", "pos": "noun", "ipa": "/dɪˈvaɪnɚz/", "vi": "thầy bói; người dò tìm mạch nước"},
    {"id": "lex.en.200k.057864", "hw": "doulas", "pos": "noun", "ipa": "/ˈduːləz/", "vi": "người hỗ trợ sản phụ chuyển dạ sinh"},
    {"id": "lex.en.200k.057865", "hw": "earldoms", "pos": "noun", "ipa": "/ˈɜːrldəmz/", "vi": "lãnh địa và tước hiệu bá tước Anh"},
    {"id": "lex.en.200k.057866", "hw": "eires", "pos": "noun", "ipa": "/ˈɛərəz/", "vi": "quốc gia đảo Ireland tươi đẹp"},
    {"id": "lex.en.200k.057867", "hw": "ekmans", "pos": "noun", "ipa": "/ˈɛkmənz/", "vi": "nhà hải dương học Vagn Ekman"},
    {"id": "lex.en.200k.057868", "hw": "fingerboards", "pos": "noun", "ipa": "/ˈfɪŋɡɚbɔːrdz/", "vi": "bàn phím cần đàn guitar vĩ cầm"},
    {"id": "lex.en.200k.057869", "hw": "footsteps", "pos": "noun", "ipa": "/ˈfʊtstɛps/", "vi": "tiếng bước chân dồn dập; dấu chân"},
    {"id": "lex.en.200k.057870", "hw": "forecastles", "pos": "noun", "ipa": "/ˈfoʊksəlz/", "vi": "phần boong mũi phía trước thuyền"},
    {"id": "lex.en.200k.057871", "hw": "gabapentins", "pos": "noun", "ipa": "/ˌɡæbəˈpɛntɪnz/", "vi": "thuốc chống co giật đau thần kinh"},
    {"id": "lex.en.200k.057872", "hw": "galactoses", "pos": "noun", "ipa": "/ɡəˈlæktoʊsɪz/", "vi": "đường đơn galactose trong sữa"},
    {"id": "lex.en.200k.057873", "hw": "glaziers", "pos": "noun", "ipa": "/ˈɡleɪʒɚz/", "vi": "thợ chuyên cắt lắp kính cửa sổ"},
    {"id": "lex.en.200k.057874", "hw": "goalposts", "pos": "noun", "ipa": "/ˈɡoʊlpoʊsts/", "vi": "các cột gôn khung thành bóng đá"},
    {"id": "lex.en.200k.057875", "hw": "guars", "pos": "noun", "ipa": "/ɡwɑːrz/", "vi": "cây họ đậu guar lấy chất kết dính"},
    {"id": "lex.en.200k.057876", "hw": "handlooms", "pos": "noun", "ipa": "/ˈhændluːmz/", "vi": "khung cửi dệt vải thủ công bằng tay"},
    {"id": "lex.en.200k.057877", "hw": "hecates", "pos": "noun", "ipa": "/ˈhɛkətiːz/", "vi": "nữ thần phép thuật ma thuật Hecate"},
    {"id": "lex.en.200k.057878", "hw": "iditarods", "pos": "noun", "ipa": "/aɪˈdɪtərɑːdz/", "vi": "cuộc đua xe chó kéo tuyết Alaska"},
    {"id": "lex.en.200k.057879", "hw": "ious", "pos": "noun", "ipa": "/ˌaɪ.oʊˈjuːz/", "vi": "các tờ giấy ghi nhận nợ IOU"},
    {"id": "lex.en.200k.057880", "hw": "keystrokes", "pos": "noun", "ipa": "/ˈkiːstroʊks/", "vi": "cú nhấn phím trên bàn phím"},
    {"id": "lex.en.200k.057881", "hw": "killjoys", "pos": "noun", "ipa": "/ˈkɪldʒɔɪz/", "vi": "những kẻ phá đám làm mất vui tiệc"},
    {"id": "lex.en.200k.057882", "hw": "kinas", "pos": "noun", "ipa": "/ˈkiːnəz/", "vi": "đồng tiền kina Papua New Guinea"},
    {"id": "lex.en.200k.057883", "hw": "kitchenettes", "pos": "noun", "ipa": "/ˌkɪtʃəˈnɛts/", "vi": "gian bếp mini nhỏ gọn tiện ích"},
    {"id": "lex.en.200k.057884", "hw": "legionellas", "pos": "noun", "ipa": "/ˌliːdʒəˈnɛləz/", "vi": "vi khuẩn phế cầu gây sốt Legionella"},
    {"id": "lex.en.200k.057885", "hw": "longbows", "pos": "noun", "ipa": "/ˈlɔːŋboʊz/", "vi": "những cây đại cung trường cung cổ"},
    {"id": "lex.en.200k.057886", "hw": "melias", "pos": "noun", "ipa": "/ˈmiːliəz/", "vi": "các loài cây thuộc chi xoan Melia"},
    {"id": "lex.en.200k.057887", "hw": "metterniches", "pos": "noun", "ipa": "/ˈmɛtɚnɪkɪz/", "vi": "chính khách Áo Klemens Metternich"},
    {"id": "lex.en.200k.057888", "hw": "montesquieus", "pos": "noun", "ipa": "/ˈmɑːntəskjuːz/", "vi": "triết gia Montesquieu nước Pháp"},
    {"id": "lex.en.200k.057889", "hw": "moselles", "pos": "noun", "ipa": "/moʊˈzɛlz/", "vi": "rượu vang trắng vùng sông Moselle"},
    {"id": "lex.en.200k.057890", "hw": "muharrams", "pos": "noun", "ipa": "/muːˈhɑːrəmz/", "vi": "tháng đầu Muharram năm Hồi giáo"},
    {"id": "lex.en.200k.057891", "hw": "neguses", "pos": "noun", "ipa": "/ˈniːɡəsɪz/", "vi": "vua Ethiopia; rượu negus nóng"},
    {"id": "lex.en.200k.057892", "hw": "neoconservatives", "pos": "noun", "ipa": "/ˌniːoʊkənˈsɜːrvətɪvz/", "vi": "những người phái tân bảo thủ"},
    {"id": "lex.en.200k.057893", "hw": "nnes", "pos": "noun", "ipa": "/ˌɛn.ɛnˈiːz/", "vi": "hướng bắc-đông bắc la bàn hải đồ"},
    {"id": "lex.en.200k.057894", "hw": "occultists", "pos": "noun", "ipa": "/əˈkʌltɪsts/", "vi": "người theo môn thần bí huyền bí"},
    {"id": "lex.en.200k.057895", "hw": "oorts", "pos": "noun", "ipa": "/ɔːrts/", "vi": "nhà thiên văn học Jan Oort đám mây"},
    {"id": "lex.en.200k.057896", "hw": "ornithologists", "pos": "noun", "ipa": "/ˌɔːrnəˈθɑːlədʒɪsts/", "vi": "các nhà khoa học điểu học loài chim"},
    {"id": "lex.en.200k.057897", "hw": "oxidizers", "pos": "noun", "ipa": "/ˈɑːksɪdaɪzɚz/", "vi": "các chất oxy hóa mạnh kích nổ cháy"},
    {"id": "lex.en.200k.057898", "hw": "peroxidases", "pos": "noun", "ipa": "/pəˈrɑːksɪdeɪsɪz/", "vi": "các enzym phân giải hydro peroxit"},
    {"id": "lex.en.200k.057899", "hw": "pinatas", "pos": "noun", "ipa": "/pɪnˈjɑːtəz/", "vi": "hình nộm đập kẹo piñata lễ hội"},
    {"id": "lex.en.200k.057900", "hw": "polychromed", "pos": "verb", "ipa": "/ˈpɑːlikroʊmd/", "vi": "đã tô vẽ nhiều màu sắc sặc sỡ"},
    {"id": "lex.en.200k.057901", "hw": "polychromes", "pos": "noun", "ipa": "/ˈpɑːlikroʊmz/", "vi": "các tác phẩm điêu khắc vẽ nhiều màu"}
]

# Validation
with open('scratch/b32_r06_raw_p4.json') as f:
    raw = json.load(f)

assert len(records) == 100, f"Expected 100 records, got {len(records)}"
for i, (r, raw_r) in enumerate(zip(records, raw)):
    assert r['id'] == raw_r['id'], f"Mismatch id at {i}: {r['id']} vs {raw_r['id']}"
    assert r['hw'] == raw_r['hw'], f"Mismatch hw at {i}: {r['hw']} vs {raw_r['hw']}"
    assert len(r['vi']) <= 35, f"Length violation at {i} ({r['hw']}): len={len(r['vi'])}: {r['vi']}"
    assert r['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {r['pos']}"
    if ' ' not in r['hw']:
        assert r['ipa'].startswith('/') and r['ipa'].endswith('/') and r['ipa'].count('/') == 2, f"Invalid ipa at {i}: {r['ipa']}"

# Merge with raw
final_p4 = []
for r, raw_r in zip(records, raw):
    item = dict(raw_r)
    item['pos'] = r['pos']
    item['ipa'] = r['ipa']
    item['vi'] = r['vi']
    item['status'] = 'reviewed'
    final_p4.append(item)

with open('scratch/b32_r06_p4.json', 'w') as f:
    json.dump(final_p4, f, ensure_ascii=False, indent=2)
print("Part 4 validated and written successfully.")
