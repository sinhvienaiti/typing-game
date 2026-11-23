import json

items = [
  {"id": "lex.en.200k.065603", "hw": "corneums", "pos": "noun", "ipa": "/ˈkɔːrniəmz/", "vi": "lớp sừng ngoài cùng biểu bì da"},
  {"id": "lex.en.200k.065604", "hw": "cowpenses", "pos": "noun", "ipa": "/ˈkaʊpɛnzɪz/", "vi": "trận Cowpens năm 1781 Cách mạng Mỹ"},
  {"id": "lex.en.200k.065605", "hw": "crapes", "pos": "noun", "ipa": "/kreɪps/", "vi": "vải kếp đen để tang; bánh kếp mỏng"},
  {"id": "lex.en.200k.065606", "hw": "crowfoots", "pos": "noun", "ipa": "/ˈkroʊfʊts/", "vi": "cây hoa mao lương vàng đồng cỏ"},
  {"id": "lex.en.200k.065607", "hw": "culms", "pos": "noun", "ipa": "/kʌlmz/", "vi": "thân rạ rỗng của cây cỏ lúa tre"},
  {"id": "lex.en.200k.065608", "hw": "daystars", "pos": "noun", "ipa": "/ˈdeɪstɑːrz/", "vi": "sao Mai rạng sáng; vầng thái dương"},
  {"id": "lex.en.200k.065609", "hw": "dendrobiums", "pos": "noun", "ipa": "/dɛnˈdroʊbiəmz/", "vi": "chi hoa phong lan hoàng thảo đẹp"},
  {"id": "lex.en.200k.065610", "hw": "dinettes", "pos": "noun", "ipa": "/daɪˈnɛts/", "vi": "góc phòng ăn nhỏ kèm bàn ghế gọn"},
  {"id": "lex.en.200k.065611", "hw": "druses", "pos": "noun", "ipa": "/ˈdruːzɪz/", "vi": "tín đồ Druze; tinh thể hốc đá; màng"},
  {"id": "lex.en.200k.065612", "hw": "durers", "pos": "noun", "ipa": "/ˈdʊrərz/", "vi": "danh họa Phục Hưng Đức Dürer"},
  {"id": "lex.en.200k.065613", "hw": "eelgrasses", "pos": "noun", "ipa": "/ˈiːlˌɡræsɪz/", "vi": "cỏ lươn thủy sinh mọc dưới đáy biển"},
  {"id": "lex.en.200k.065614", "hw": "ehfs", "pos": "noun", "ipa": "/ˌiːˌeɪtʃˈɛfs/", "vi": "băng tần vô tuyến cực cao EHF"},
  {"id": "lex.en.200k.065615", "hw": "enantiomers", "pos": "noun", "ipa": "/ɪˈnæntiəˌmɜːrz/", "vi": "cặp đồng phân quang học đối ảnh"},
  {"id": "lex.en.200k.065616", "hw": "enols", "pos": "noun", "ipa": "/ˈiːnɔːlz/", "vi": "hợp chất hữu cơ dạng ancol nối đôi"},
  {"id": "lex.en.200k.065617", "hw": "exigencies", "pos": "noun", "ipa": "/ˈɛksədʒənsɪz/", "vi": "nhu cầu cấp bách; tình huống khẩn"},
  {"id": "lex.en.200k.065618", "hw": "festucas", "pos": "noun", "ipa": "/fɛˈstjuːkəz/", "vi": "chi cỏ chổi đồng cỏ bãi ôn đới"},
  {"id": "lex.en.200k.065619", "hw": "folksongs", "pos": "noun", "ipa": "/ˈfoʊksɔːŋz/", "vi": "bài dân ca truyền thống dân gian"},
  {"id": "lex.en.200k.065620", "hw": "fonteyns", "pos": "noun", "ipa": "/fɑːnˈteɪnz/", "vi": "nữ nghệ sĩ ba lê Margot Fonteyn"},
  {"id": "lex.en.200k.065621", "hw": "ghillies", "pos": "noun", "ipa": "/ˈɡɪliz/", "vi": "giày da Scotland; người hầu săn bắn"},
  {"id": "lex.en.200k.065622", "hw": "glissandi", "pos": "noun", "ipa": "/ɡlɪˈsɑːndi/", "vi": "các đoạn nhạc lướt phím mượt mà"},
  {"id": "lex.en.200k.065623", "hw": "haiphongs", "pos": "noun", "ipa": "/ˈhaɪfɔːŋz/", "vi": "thành phố cảng Hải Phòng Việt Nam"},
  {"id": "lex.en.200k.065624", "hw": "halachas", "pos": "noun", "ipa": "/hɑːləˈxɑːz/", "vi": "bộ luật tôn giáo Do Thái Halakha"},
  {"id": "lex.en.200k.065625", "hw": "haldols", "pos": "noun", "ipa": "/ˈhældɔːlz/", "vi": "thuốc an thần trị loạn thần Haldol"},
  {"id": "lex.en.200k.065626", "hw": "harmsworths", "pos": "noun", "ipa": "/ˈhɑːrmzwɜːrθs/", "vi": "ông trùm báo chí Anh Harmsworth"},
  {"id": "lex.en.200k.065627", "hw": "hatfuls", "pos": "noun", "ipa": "/ˈhætfʊlz/", "vi": "lượng đồ vật đựng đầy một chiếc mũ"},
  {"id": "lex.en.200k.065628", "hw": "haunches", "pos": "noun", "ipa": "/ˈhɔːntʃɪz/", "vi": "vùng hông đùi sau; thế ngồi xổm"},
  {"id": "lex.en.200k.065629", "hw": "horninesses", "pos": "noun", "ipa": "/ˈhɔːrninəsɪz/", "vi": "tính cứng như sừng; cơn kích thích"},
  {"id": "lex.en.200k.065630", "hw": "horsemeats", "pos": "noun", "ipa": "/ˈhɔːrsmiːts/", "vi": "thịt ngựa dùng làm thực phẩm"},
  {"id": "lex.en.200k.065631", "hw": "hydrophobicities", "pos": "noun", "ipa": "/ˌhaɪdrəfoʊˈbɪsətiz/", "vi": "tính chất kỵ đẩy nước của bề mặt"},
  {"id": "lex.en.200k.065632", "hw": "hyperemeses", "pos": "noun", "ipa": "/ˌhaɪpərˈɛməsiːz/", "vi": "chứng nôn ói dữ dội quá mức"},
  {"id": "lex.en.200k.065633", "hw": "inrushes", "pos": "noun", "ipa": "/ˈɪnrʌʃɪz/", "vi": "dòng nước hay điện tràn ùa vào mạnh"},
  {"id": "lex.en.200k.065634", "hw": "interdependencies", "pos": "noun", "ipa": "/ˌɪntərdɪˈpɛndənsiz/", "vi": "mối quan hệ phụ thuộc tương hỗ nhau"},
  {"id": "lex.en.200k.065635", "hw": "internalised", "pos": "verb", "ipa": "/ɪnˈtɜːrnəˌlaɪzd/", "vi": "đã nội tâm hóa thấm nhuần (Anh)"},
  {"id": "lex.en.200k.065636", "hw": "internalises", "pos": "verb", "ipa": "/ɪnˈtɜːrnəˌlaɪzɪz/", "vi": "nội tâm hóa tiếp thu sâu sắc (Anh)"},
  {"id": "lex.en.200k.065637", "hw": "internalising", "pos": "verb", "ipa": "/ɪnˈtɜːrnəˌlaɪzɪŋ/", "vi": "đang tiếp thu nội tâm hóa (Anh)"},
  {"id": "lex.en.200k.065638", "hw": "inulins", "pos": "noun", "ipa": "/ˈɪnjʊlɪnz/", "vi": "chất xơ hòa tan thực vật inulin"},
  {"id": "lex.en.200k.065639", "hw": "isopropanols", "pos": "noun", "ipa": "/ˌaɪsoʊˈproʊpənɔːlz/", "vi": "cồn sát trùng tẩy rửa isopropanol"},
  {"id": "lex.en.200k.065640", "hw": "kindergarteners", "pos": "noun", "ipa": "/ˈkɪndərˌɡɑːrtnərz/", "vi": "học sinh nhỏ đang học lớp mẫu giáo"},
  {"id": "lex.en.200k.065641", "hw": "kohlrabies", "pos": "noun", "ipa": "/ˌkoʊlˈrɑːbiz/", "vi": "cây và củ su hào xanh thuộc họ Cải"},
  {"id": "lex.en.200k.065642", "hw": "kunluns", "pos": "noun", "ipa": "/ˈkʊnlʊnz/", "vi": "dãy núi cao Côn Lôn phía tây TQ"},
  {"id": "lex.en.200k.065643", "hw": "laniuses", "pos": "noun", "ipa": "/ˈleɪniəsɪz/", "vi": "chi chim bách thanh mỏ quặp Lanius"},
  {"id": "lex.en.200k.065644", "hw": "lazarettos", "pos": "noun", "ipa": "/ˌlæzəˈrɛtoʊz/", "vi": "bệnh viện cách ly dịch; trại phong"},
  {"id": "lex.en.200k.065645", "hw": "liverpudlians", "pos": "noun", "ipa": "/ˌlɪvərˈpʌdliənz/", "vi": "người dân thành phố cảng Liverpool"},
  {"id": "lex.en.200k.065646", "hw": "lotis", "pos": "noun", "ipa": "/ˈloʊtiz/", "vi": "đơn vị tiền tệ loti của Lesotho"},
  {"id": "lex.en.200k.065647", "hw": "lovebirds", "pos": "noun", "ipa": "/ˈlʌvbɜːrdz/", "vi": "vẹt uyên ương nhỏ gắn bó; đôi tình"},
  {"id": "lex.en.200k.065648", "hw": "majoranas", "pos": "noun", "ipa": "/ˌmædʒəˈreɪnəz/", "vi": "chi cây kinh giới ngọt Majorana"},
  {"id": "lex.en.200k.065649", "hw": "maloti", "pos": "noun", "ipa": "/məˈloʊti/", "vi": "các đồng tiền loti nước Lesotho"},
  {"id": "lex.en.200k.065650", "hw": "marabous", "pos": "noun", "ipa": "/ˈmærəbuːz/", "vi": "chim cò già đầu trọc lớn châu Phi"},
  {"id": "lex.en.200k.065651", "hw": "medivacs", "pos": "noun", "ipa": "/ˈmɛdɪˌvæks/", "vi": "trực thăng vận chuyển cấp cứu y tế"},
  {"id": "lex.en.200k.065652", "hw": "mifepristones", "pos": "noun", "ipa": "/ˌmɪfəˈprɪstoʊnz/", "vi": "thuốc nội tiết mifepristone y khoa"},
  {"id": "lex.en.200k.065653", "hw": "minyanim", "pos": "noun", "ipa": "/mɪnˈjɑːnɪm/", "vi": "túc số 10 người Do Thái cầu nguyện"},
  {"id": "lex.en.200k.065654", "hw": "minyans", "pos": "noun", "ipa": "/ˈmɪnjənz/", "vi": "các nhóm 10 người Do Thái cầu lễ"},
  {"id": "lex.en.200k.065655", "hw": "motormouths", "pos": "noun", "ipa": "/ˈmoʊtərˌmaʊðz/", "vi": "người nói liến thoắng không ngừng"},
  {"id": "lex.en.200k.065656", "hw": "nateses", "pos": "noun", "ipa": "/ˈneɪtiːzɪz/", "vi": "hai bên cặp mông (thuật ngữ y học)"},
  {"id": "lex.en.200k.065657", "hw": "nebraskans", "pos": "noun", "ipa": "/nəˈbræskənz/", "vi": "người dân sinh sống bang Nebraska"},
  {"id": "lex.en.200k.065658", "hw": "noneses", "pos": "noun", "ipa": "/ˈnoʊnzɪz/", "vi": "giờ kinh thứ chín; ngày Nones La Mã"},
  {"id": "lex.en.200k.065659", "hw": "nouakchotts", "pos": "noun", "ipa": "/nwɑːkˈʃɑːts/", "vi": "thủ đô Nouakchott của Mauritania"},
  {"id": "lex.en.200k.065660", "hw": "nucleosyntheses", "pos": "noun", "ipa": "/ˌnjuːklioʊˈsɪnθəsiːz/", "vi": "sự tổng hợp hạt nhân trong sao"},
  {"id": "lex.en.200k.065661", "hw": "oryzas", "pos": "noun", "ipa": "/ɔːˈraɪzəz/", "vi": "chi thực vật cây lúa gạo Oryza"},
  {"id": "lex.en.200k.065662", "hw": "paddlers", "pos": "noun", "ipa": "/ˈpædlərz/", "vi": "người chèo xuồng bằng mái chèo tay"},
  {"id": "lex.en.200k.065663", "hw": "pantographs", "pos": "noun", "ipa": "/ˈpæntəˌɡræfs/", "vi": "thước vẽ phóng hình; cần tiếp điện"},
  {"id": "lex.en.200k.065664", "hw": "peacoats", "pos": "noun", "ipa": "/ˈpiːkoʊts/", "vi": "áo khoác dạ len ngắn hai hàng khuy"},
  {"id": "lex.en.200k.065665", "hw": "portraitists", "pos": "noun", "ipa": "/ˈpɔːrtrətɪsts/", "vi": "họa sĩ chuyên vẽ tranh chân dung"},
  {"id": "lex.en.200k.065666", "hw": "purgatives", "pos": "noun", "ipa": "/ˈpɜːrɡətɪvz/", "vi": "thuốc xổ mạnh làm sạch đường ruột"},
  {"id": "lex.en.200k.065667", "hw": "raphae", "pos": "noun", "ipa": "/ˈreɪfiː/", "vi": "đường gờ ráp nối giữa hai nửa cơ"},
  {"id": "lex.en.200k.065668", "hw": "raphes", "pos": "noun", "ipa": "/reɪfs/", "vi": "đường ráp nối giải phẫu hai nửa cơ"},
  {"id": "lex.en.200k.065669", "hw": "respecters", "pos": "noun", "ipa": "/rɪˈspɛktərz/", "vi": "người nể nang; người biết tôn trọng"},
  {"id": "lex.en.200k.065670", "hw": "reticulations", "pos": "noun", "ipa": "/rɪˌtɪkjəˈleɪʃənz/", "vi": "họa tiết mạng lưới; rạn nứt men gốm"},
  {"id": "lex.en.200k.065671", "hw": "rifampins", "pos": "noun", "ipa": "/rɪˈfæmpɪnz/", "vi": "kháng sinh trị lao phong rifampin"},
  {"id": "lex.en.200k.065672", "hw": "ritonavirs", "pos": "noun", "ipa": "/rɪˈtɑːnəvɪrz/", "vi": "thuốc kháng virus HIV ritonavir"},
  {"id": "lex.en.200k.065673", "hw": "rockeries", "pos": "noun", "ipa": "/ˈrɑːkəriz/", "vi": "hòn non bộ vườn đá trồng cây cảnh"},
  {"id": "lex.en.200k.065674", "hw": "rundstedts", "pos": "noun", "ipa": "/ˈrʊntʃtɛts/", "vi": "thống chế Đức Thế chiến Rundstedt"},
  {"id": "lex.en.200k.065675", "hw": "saltpetres", "pos": "noun", "ipa": "/ˌsɔːltˈpiːtərz/", "vi": "muối diêm tiêu kali nitrat (Anh)"},
  {"id": "lex.en.200k.065676", "hw": "scriabins", "pos": "noun", "ipa": "/skriˈɑːbɪnz/", "vi": "nhà soạn nhạc piano Nga Scriabin"},
  {"id": "lex.en.200k.065677", "hw": "shakeouts", "pos": "noun", "ipa": "/ˈʃeɪkaʊts/", "vi": "đợt thanh lọc đào thải doanh nghiệp"},
  {"id": "lex.en.200k.065678", "hw": "siracusas", "pos": "noun", "ipa": "/ˌsɪrəˈkjuːsəz/", "vi": "thành phố cổ Syracuse đảo Sicily Ý"},
  {"id": "lex.en.200k.065679", "hw": "slipcovers", "pos": "noun", "ipa": "/ˈslɪpˌkʌvərz/", "vi": "vỏ vải bọc tháo rời cho ghế sofa"},
  {"id": "lex.en.200k.065680", "hw": "songhais", "pos": "noun", "ipa": "/sɔːŋˈɡaɪz/", "vi": "đế chế dân tộc ngôn ngữ Songhai"},
  {"id": "lex.en.200k.065681", "hw": "stanislavskies", "pos": "noun", "ipa": "/ˌstænɪˈslɑːfskiz/", "vi": "đạo diễn sân khấu Nga Stanislavski"},
  {"id": "lex.en.200k.065682", "hw": "steelmans", "pos": "noun", "ipa": "/ˈstiːlmənz/", "vi": "thợ thép; lập luận phản biện mạnh"},
  {"id": "lex.en.200k.065683", "hw": "steganographies", "pos": "noun", "ipa": "/ˌstɛɡəˈnɑːɡrəfiz/", "vi": "kỹ thuật giấu tin mật trong tệp tin"},
  {"id": "lex.en.200k.065684", "hw": "syrinxes", "pos": "noun", "ipa": "/ˈsɪrɪŋksɪz/", "vi": "ống sáo pan; cơ quan hót của chim"},
  {"id": "lex.en.200k.065685", "hw": "tetrodotoxins", "pos": "noun", "ipa": "/ˌtɛtrədoʊˈtɑːksɪnz/", "vi": "độc tố thần kinh cực độc cá nóc"},
  {"id": "lex.en.200k.065686", "hw": "thatcherites", "pos": "noun", "ipa": "/ˈθætʃəraɪts/", "vi": "người ủng hộ chính sách bà Thatcher"},
  {"id": "lex.en.200k.065687", "hw": "theias", "pos": "noun", "ipa": "/ˈθiːəz/", "vi": "nữ thần ánh sáng Titan Hy Lạp Theia"},
  {"id": "lex.en.200k.065688", "hw": "thiamins", "pos": "noun", "ipa": "/ˈθaɪəmɪnz/", "vi": "vitamin B1 thiamin chuyển hóa đường"},
  {"id": "lex.en.200k.065689", "hw": "tiflises", "pos": "noun", "ipa": "/tɪˈfliːsɪz/", "vi": "thành phố Tbilisi Gruzia (tên cũ)"},
  {"id": "lex.en.200k.065690", "hw": "turkistans", "pos": "noun", "ipa": "/ˈtɜːrkɪstænz/", "vi": "khu vực lịch sử Turkestan Trung Á"},
  {"id": "lex.en.200k.065691", "hw": "valencies", "pos": "noun", "ipa": "/ˈveɪlənsiz/", "vi": "hóa trị nguyên tử; kết trị từ (Anh)"},
  {"id": "lex.en.200k.065692", "hw": "vanbrughs", "pos": "noun", "ipa": "/vænˈbrʌfs/", "vi": "kiến trúc sư và kịch tác gia Anh"},
  {"id": "lex.en.200k.065693", "hw": "weathervanes", "pos": "noun", "ipa": "/ˈwɛðərveɪnz/", "vi": "chong chóng chỉ hướng gió trên mái"},
  {"id": "lex.en.200k.065694", "hw": "werfels", "pos": "noun", "ipa": "/ˈvɛrfəlz/", "vi": "nhà văn kịch Áo-Séc Franz Werfel"},
  {"id": "lex.en.200k.065695", "hw": "whanged", "pos": "verb", "ipa": "/wæŋd/", "vi": "đã đập mạnh vang; quất vụt mạnh"},
  {"id": "lex.en.200k.065696", "hw": "whanging", "pos": "verb", "ipa": "/ˈwæŋɪŋ/", "vi": "đang đập đánh quất mạnh vang tiếng"},
  {"id": "lex.en.200k.065697", "hw": "whangs", "pos": "noun", "ipa": "/wæŋz/", "vi": "cú đập đánh mạnh; tiếng va vang to"},
  {"id": "lex.en.200k.065698", "hw": "whirligigs", "pos": "noun", "ipa": "/ˈwɜːrlɪˌɡɪɡz/", "vi": "con quay đồ chơi; vòng đu quay; bọ"},
  {"id": "lex.en.200k.065699", "hw": "wineglasses", "pos": "noun", "ipa": "/ˈwaɪnˌɡlæsɪz/", "vi": "ly thủy tinh chân cao uống rượu"},
  {"id": "lex.en.200k.065700", "hw": "yacked", "pos": "verb", "ipa": "/jækt/", "vi": "đã ba hoa tán gẫu huyên thuyên"},
  {"id": "lex.en.200k.065701", "hw": "yacking", "pos": "verb", "ipa": "/ˈjækɪŋ/", "vi": "đang tán gẫu nói luyên thuyên mãi"},
  {"id": "lex.en.200k.065702", "hw": "yacks", "pos": "noun", "ipa": "/jæks/", "vi": "cuộc tán gẫu huyên thuyên ầm ĩ"}
]

with open('scratch/b34_r02_raw_p2.json') as f:
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

with open('scratch/b34_r02_p2.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r02_p2.json OK")
