import json

items = [
  {"id": "lex.en.200k.062703", "hw": "polestars", "pos": "noun", "ipa": "/ˈpoʊlstɑːrz/", "vi": "sao Bắc Cực; kim chỉ nam dẫn hướng"},
  {"id": "lex.en.200k.062704", "hw": "potassium dichromate", "pos": "phrase", "ipa": "/pəˈtæsiəm daɪˈkroʊmeɪt/", "vi": "hợp chất kali đicromat oxi hóa"},
  {"id": "lex.en.200k.062705", "hw": "potbellies", "pos": "noun", "ipa": "/ˈpɑːtbɛliz/", "vi": "bụng phệ tròn; bếp lò bụng phình"},
  {"id": "lex.en.200k.062706", "hw": "prebends", "pos": "noun", "ipa": "/ˈprɛbəndz/", "vi": "bổng lộc chức sắc nhà thờ"},
  {"id": "lex.en.200k.062707", "hw": "prizefighters", "pos": "noun", "ipa": "/ˈpraɪzfaɪtərz/", "vi": "võ sĩ quyền anh đấu giải chuyên"},
  {"id": "lex.en.200k.062708", "hw": "prohibitionists", "pos": "noun", "ipa": "/ˌproʊəˈbɪʃənɪsts/", "vi": "người ủng hộ lệnh cấm rượu bia"},
  {"id": "lex.en.200k.062709", "hw": "pronghorns", "pos": "noun", "ipa": "/ˈprɔːŋhɔːrnz/", "vi": "linh dương sừng nhánh Bắc Mỹ"},
  {"id": "lex.en.200k.062710", "hw": "propionic acid", "pos": "phrase", "ipa": "/ˌproʊpiˈɑːnɪk ˈæsɪd/", "vi": "axit hữu cơ propionic bảo quản"},
  {"id": "lex.en.200k.062711", "hw": "proteolyses", "pos": "noun", "ipa": "/ˌproʊtiˈɑːləsiːz/", "vi": "quá trình thủy phân phân giải đạm"},
  {"id": "lex.en.200k.062712", "hw": "ray floret", "pos": "phrase", "ipa": "/reɪ ˈflɔːrət/", "vi": "hoa hình tia cánh ngoài họ Cúc"},
  {"id": "lex.en.200k.062713", "hw": "roeblings", "pos": "noun", "ipa": "/ˈroʊblɪŋz/", "vi": "kỹ sư cầu treo John Roebling"},
  {"id": "lex.en.200k.062714", "hw": "rosehips", "pos": "noun", "ipa": "/ˈroʊzhɪps/", "vi": "quả tầm xuân giàu vitamin C"},
  {"id": "lex.en.200k.062715", "hw": "rumanias", "pos": "noun", "ipa": "/ruˈmeɪniəz/", "vi": "quốc gia Rumani (cách viết cũ)"},
  {"id": "lex.en.200k.062716", "hw": "saties", "pos": "noun", "ipa": "/ˈsætiːz/", "vi": "nhà soạn nhạc Pháp Erik Satie"},
  {"id": "lex.en.200k.062717", "hw": "sedums", "pos": "noun", "ipa": "/ˈsiːdəmz/", "vi": "cây sen đá trường sinh mọng nước"},
  {"id": "lex.en.200k.062718", "hw": "sennacheribs", "pos": "noun", "ipa": "/səˈnækərɪbz/", "vi": "vua Assyria cổ đại Sennacherib"},
  {"id": "lex.en.200k.062719", "hw": "sergei mikhailovich eisenstein", "pos": "phrase", "ipa": "/ˈsɛrɡeɪ mɪˈxaɪləvɪtʃ ˈaɪzənstaɪn/", "vi": "đạo diễn Xô Viết Sergei Eisenstein"},
  {"id": "lex.en.200k.062720", "hw": "sesquicentennials", "pos": "noun", "ipa": "/ˌsɛskwɪsɛnˈtɛniəlz/", "vi": "lễ kỷ niệm tròn 150 năm thành lập"},
  {"id": "lex.en.200k.062721", "hw": "seventieths", "pos": "noun", "ipa": "/ˈsɛvəntiəθs/", "vi": "phần thứ bảy mươi (1/70); hạng 70"},
  {"id": "lex.en.200k.062722", "hw": "shibboleths", "pos": "noun", "ipa": "/ˈʃɪbəlɛθs/", "vi": "từ nhận diện nhóm; tín điều cũ"},
  {"id": "lex.en.200k.062723", "hw": "sodium lauryl sulphate", "pos": "phrase", "ipa": "/ˈsoʊdiəm ˈlɔːrəl ˈsʌlfeɪt/", "vi": "chất tạo bọt tẩy rửa natri lauryl"},
  {"id": "lex.en.200k.062724", "hw": "stamens", "pos": "noun", "ipa": "/ˈsteɪmənz/", "vi": "nhị hoa sinh hạt phấn đực ở cây"},
  {"id": "lex.en.200k.062725", "hw": "supergrasses", "pos": "noun", "ipa": "/ˈsuːpərɡræsɪz/", "vi": "kẻ chỉ điểm băng đảng cho cảnh sát"},
  {"id": "lex.en.200k.062726", "hw": "surinamese monetary unit", "pos": "phrase", "ipa": "/ˌsʊrəˈnɑːmiːz ˈmɑːnəˌtɛri ˈjuːnɪt/", "vi": "đơn vị tiền tệ nước Suriname"},
  {"id": "lex.en.200k.062727", "hw": "synecdoches", "pos": "noun", "ipa": "/sɪˈnɛkdəkiz/", "vi": "phép hoán dụ bộ phận chỉ toàn thể"},
  {"id": "lex.en.200k.062728", "hw": "tablatures", "pos": "noun", "ipa": "/ˈtæblətʃərz/", "vi": "bản nhạc ký âm bấm dây đàn (tab)"},
  {"id": "lex.en.200k.062729", "hw": "tammy wynette", "pos": "phrase", "ipa": "/ˈtæmi waɪˈnɛt/", "vi": "nữ ca sĩ đồng quê Tammy Wynette"},
  {"id": "lex.en.200k.062730", "hw": "tancreds", "pos": "noun", "ipa": "/ˈtæŋkrɪdz/", "vi": "thủ lĩnh thập tự chinh Tancred"},
  {"id": "lex.en.200k.062731", "hw": "tannoys", "pos": "noun", "ipa": "/ˈtænɔɪz/", "vi": "hệ thống loa phát thanh công cộng"},
  {"id": "lex.en.200k.062732", "hw": "tetrachlorides", "pos": "noun", "ipa": "/ˌtɛtrəˈklɔːraɪdz/", "vi": "hợp chất hóa học bốn nguyên tử clo"},
  {"id": "lex.en.200k.062733", "hw": "thematic apperception test", "pos": "phrase", "ipa": "/θɪˈmætɪk ˌæpərˈsɛpʃən tɛst/", "vi": "trắc nghiệm tâm lý kể chuyện tranh"},
  {"id": "lex.en.200k.062734", "hw": "therms", "pos": "noun", "ipa": "/θɜːrmz/", "vi": "đơn vị đo nhiệt lượng khí đốt"},
  {"id": "lex.en.200k.062735", "hw": "thyroiditides", "pos": "noun", "ipa": "/ˌθaɪrɔɪˈdaɪtɪdiːz/", "vi": "chứng bệnh viêm nhiễm tuyến giáp"},
  {"id": "lex.en.200k.062736", "hw": "tiger cowrie", "pos": "phrase", "ipa": "/ˈtaɪɡər ˈkaʊri/", "vi": "ốc sứ đốm da báo vùng nhiệt đới"},
  {"id": "lex.en.200k.062737", "hw": "titers", "pos": "noun", "ipa": "/ˈtaɪtərz/", "vi": "nồng độ chuẩn độ kháng thể"},
  {"id": "lex.en.200k.062738", "hw": "toccatas", "pos": "noun", "ipa": "/təˈkɑːtəz/", "vi": "bản nhạc nhanh phô diễn đàn phím"},
  {"id": "lex.en.200k.062739", "hw": "tontine insurance", "pos": "phrase", "ipa": "/ˈtɑːntiːn ɪnˈʃʊrəns/", "vi": "bảo hiểm chia phần người sống sót"},
  {"id": "lex.en.200k.062740", "hw": "tunguskas", "pos": "noun", "ipa": "/tʊŋˈɡʊskəz/", "vi": "vùng sông Tunguska ở Siberia"},
  {"id": "lex.en.200k.062741", "hw": "underachievers", "pos": "noun", "ipa": "/ˌʌndərəˈtʃiːvərz/", "vi": "người đạt kết quả dưới mức năng lực"},
  {"id": "lex.en.200k.062742", "hw": "underpayments", "pos": "noun", "ipa": "/ˌʌndərˈpeɪmənts/", "vi": "khoản thanh toán thiếu dưới mức nợ"},
  {"id": "lex.en.200k.062743", "hw": "ustinovs", "pos": "noun", "ipa": "/ˈjuːstənɑːfs/", "vi": "diễn viên nhà văn Peter Ustinov"},
  {"id": "lex.en.200k.062744", "hw": "variorum edition", "pos": "phrase", "ipa": "/ˌvɛriˈɔːrəm ɪˈdɪʃən/", "vi": "ấn bản tổng hợp nhiều chú giải"},
  {"id": "lex.en.200k.062745", "hw": "varunas", "pos": "noun", "ipa": "/vəˈruːnəz/", "vi": "thần nước và trật tự vũ trụ Varuna"},
  {"id": "lex.en.200k.062746", "hw": "viburnum lantana", "pos": "phrase", "ipa": "/vaɪˈbɜːrnəm lænˈtænə/", "vi": "cây bụi quả mọng Viburnum lantana"},
  {"id": "lex.en.200k.062747", "hw": "viniferas", "pos": "noun", "ipa": "/vəˈnɪfərəz/", "vi": "giống nho rượu vang Vitis vinifera"},
  {"id": "lex.en.200k.062748", "hw": "wallahs", "pos": "noun", "ipa": "/ˈwɑːləz/", "vi": "người chuyên làm dịch vụ (Ấn Độ)"},
  {"id": "lex.en.200k.062749", "hw": "wankel rotary engine", "pos": "phrase", "ipa": "/ˈwæŋkəl ˈroʊtəri ˈɛndʒɪn/", "vi": "động cơ piston xoay tam giác Wankel"},
  {"id": "lex.en.200k.062750", "hw": "algonquians", "pos": "noun", "ipa": "/ælˈɡɑːŋkiənz/", "vi": "người bản địa Bắc Mỹ Algonquian"},
  {"id": "lex.en.200k.062751", "hw": "asclepii", "pos": "noun", "ipa": "/əˈskliːpiaɪ/", "vi": "thần y học Hy Lạp cổ Asclepius"},
  {"id": "lex.en.200k.062752", "hw": "atrazines", "pos": "noun", "ipa": "/ˈætrəziːnz/", "vi": "thuốc diệt cỏ nông nghiệp atrazine"},
  {"id": "lex.en.200k.062753", "hw": "automats", "pos": "noun", "ipa": "/ˈɔːtəmæts/", "vi": "quán ăn tự phục vụ bán tự động"},
  {"id": "lex.en.200k.062754", "hw": "backbeats", "pos": "noun", "ipa": "/ˈbækbiːts/", "vi": "nhịp nhấn phách chẵn trong âm nhạc"},
  {"id": "lex.en.200k.062755", "hw": "barillas", "pos": "noun", "ipa": "/bəˈriːəz/", "vi": "cây cỏ muối giàu kiềm; tro xút kiềm"},
  {"id": "lex.en.200k.062756", "hw": "bellboys", "pos": "noun", "ipa": "/ˈbɛlbɔɪz/", "vi": "nhân viên xách hành lý khách sạn"},
  {"id": "lex.en.200k.062757", "hw": "blowpipes", "pos": "noun", "ipa": "/ˈbloʊpaɪps/", "vi": "ống thổi tiêu săn; ống thổi lửa"},
  {"id": "lex.en.200k.062758", "hw": "butties", "pos": "noun", "ipa": "/ˈbʌtiz/", "vi": "bánh mì kẹp bơ (tiếng lóng Anh)"},
  {"id": "lex.en.200k.062759", "hw": "caciques", "pos": "noun", "ipa": "/kəˈsiːks/", "vi": "tù trưởng bản địa; chim sáo châu Mỹ"},
  {"id": "lex.en.200k.062760", "hw": "caracals", "pos": "noun", "ipa": "/ˈkærəkælz/", "vi": "linh miêu tai đen sa mạc châu Phi"},
  {"id": "lex.en.200k.062761", "hw": "carcinoids", "pos": "noun", "ipa": "/ˈkɑːrsənɔɪdz/", "vi": "khối u nội tiết phát triển chậm"},
  {"id": "lex.en.200k.062762", "hw": "carloads", "pos": "noun", "ipa": "/ˈkɑːrloʊdz/", "vi": "lượng hàng chất đầy một toa xe"},
  {"id": "lex.en.200k.062763", "hw": "carpetbaggers", "pos": "noun", "ipa": "/ˈkɑːrpɪtbæɡərz/", "vi": "kẻ cơ hội chính trị phương xa tới"},
  {"id": "lex.en.200k.062764", "hw": "caudates", "pos": "noun", "ipa": "/ˈkɔːdeɪts/", "vi": "động vật có đuôi; nhân đuôi ở não"},
  {"id": "lex.en.200k.062765", "hw": "clozapines", "pos": "noun", "ipa": "/ˈkloʊzəpiːnz/", "vi": "thuốc chống loạn thần clozapine"},
  {"id": "lex.en.200k.062766", "hw": "contractures", "pos": "noun", "ipa": "/kənˈtræktʃərz/", "vi": "chứng co rút cứng cơ khớp bất động"},
  {"id": "lex.en.200k.062767", "hw": "cottonseeds", "pos": "noun", "ipa": "/ˈkɑːtənsiːdz/", "vi": "hạt cây bông ép lấy dầu và thức ăn"},
  {"id": "lex.en.200k.062768", "hw": "dacrons", "pos": "noun", "ipa": "/ˈdeɪkrɑːnz/", "vi": "sợi vải tổng hợp polyester Dacron"},
  {"id": "lex.en.200k.062769", "hw": "danmarks", "pos": "noun", "ipa": "/ˈdænmɑːrks/", "vi": "quốc gia Đan Mạch (tên bản địa)"},
  {"id": "lex.en.200k.062770", "hw": "donizettis", "pos": "noun", "ipa": "/ˌdɑːnɪˈzɛtiz/", "vi": "nhà soạn nhạc opera Donizetti"},
  {"id": "lex.en.200k.062771", "hw": "dozier", "pos": "adj", "ipa": "/ˈdoʊziər/", "vi": "buồn ngủ lơ mơ hơn; ngái ngủ hơn"},
  {"id": "lex.en.200k.062772", "hw": "doziest", "pos": "adj", "ipa": "/ˈdoʊziɪst/", "vi": "buồn ngủ ngái ngủ lơ mơ nhất"},
  {"id": "lex.en.200k.062773", "hw": "dramaturgies", "pos": "noun", "ipa": "/ˈdræmətɜːrdʒiz/", "vi": "nghệ thuật sáng tác và dựng kịch"},
  {"id": "lex.en.200k.062774", "hw": "drogues", "pos": "noun", "ipa": "/droʊɡz/", "vi": "dù hãm tốc; phao nón ổn định tàu"},
  {"id": "lex.en.200k.062775", "hw": "electrums", "pos": "noun", "ipa": "/ɪˈlɛktrəmz/", "vi": "hợp kim vàng bạc tự nhiên cổ đại"},
  {"id": "lex.en.200k.062776", "hw": "endotoxins", "pos": "noun", "ipa": "/ˌɛndoʊˈtɑːksɪnz/", "vi": "nội độc tố vách tế bào vi khuẩn"},
  {"id": "lex.en.200k.062777", "hw": "eproms", "pos": "noun", "ipa": "/ˈiːprɑːmz/", "vi": "bộ nhớ chỉ đọc xóa bằng tia cực tím"},
  {"id": "lex.en.200k.062778", "hw": "ethelberts", "pos": "noun", "ipa": "/ˈɛθəlbɜːrts/", "vi": "vua Kent cổ đại Ethelbert (Anh)"},
  {"id": "lex.en.200k.062779", "hw": "fantasised", "pos": "verb", "ipa": "/ˈfæntəsaɪzd/", "vi": "đã mơ mộng viển vông; tưởng tượng"},
  {"id": "lex.en.200k.062780", "hw": "fantasises", "pos": "verb", "ipa": "/ˈfæntəsaɪzɪz/", "vi": "mơ mộng; tưởng tượng viển vông"},
  {"id": "lex.en.200k.062781", "hw": "fantasising", "pos": "verb", "ipa": "/ˈfæntəsaɪzɪŋ/", "vi": "đang mơ mộng tưởng tượng viển vông"},
  {"id": "lex.en.200k.062782", "hw": "fenrirs", "pos": "noun", "ipa": "/ˈfɛnrɪrz/", "vi": "sói khổng lồ Fenrir thần thoại"},
  {"id": "lex.en.200k.062783", "hw": "frappes", "pos": "noun", "ipa": "/fræˈpeɪz/", "vi": "thức uống kem đá xay lạnh frappé"},
  {"id": "lex.en.200k.062784", "hw": "golcondas", "pos": "noun", "ipa": "/ɡɑːlˈkɑːndəz/", "vi": "mỏ vàng kho báu giàu có vô tận"},
  {"id": "lex.en.200k.062785", "hw": "gomperses", "pos": "noun", "ipa": "/ˈɡɑːmpərzɪz/", "vi": "lãnh tụ công đoàn Mỹ Samuel Gompers"},
  {"id": "lex.en.200k.062786", "hw": "gropiuses", "pos": "noun", "ipa": "/ˈɡroʊpiəsɪz/", "vi": "kiến trúc sư Bauhaus Walter Gropius"},
  {"id": "lex.en.200k.062787", "hw": "halftones", "pos": "noun", "ipa": "/ˈhæftoʊnz/", "vi": "bản in chấm lưới nửa tông màu ảnh"},
  {"id": "lex.en.200k.062788", "hw": "haymakers", "pos": "noun", "ipa": "/ˈheɪmeɪkərz/", "vi": "cú đấm móc cực mạnh; máy phơi cỏ"},
  {"id": "lex.en.200k.062789", "hw": "hellenisms", "pos": "noun", "ipa": "/ˈhɛləˌnɪzəmz/", "vi": "văn hóa Hy Lạp cổ; từ vay Hy Lạp"},
  {"id": "lex.en.200k.062790", "hw": "hurlers", "pos": "noun", "ipa": "/ˈhɜːrlərz/", "vi": "người ném mạnh; cầu thủ gậy Ai-len"},
  {"id": "lex.en.200k.062791", "hw": "hypercholesterolemias", "pos": "noun", "ipa": "/ˌhaɪpərkəˌlɛstərəˈliːmiəz/", "vi": "chứng tăng cholesterol trong máu"},
  {"id": "lex.en.200k.062792", "hw": "inerrancies", "pos": "noun", "ipa": "/ɪnˈɛrənsiz/", "vi": "tính hoàn toàn không thể sai lầm"},
  {"id": "lex.en.200k.062793", "hw": "instantiated", "pos": "verb", "ipa": "/ɪnˈstænʃiˌeɪtɪd/", "vi": "đã khởi tạo thể hiện; đã ví dụ hóa"},
  {"id": "lex.en.200k.062794", "hw": "instantiates", "pos": "verb", "ipa": "/ɪnˈstænʃiˌeɪts/", "vi": "khởi tạo đối tượng; minh họa ví dụ"},
  {"id": "lex.en.200k.062795", "hw": "instantiating", "pos": "verb", "ipa": "/ɪnˈstænʃiˌeɪtɪŋ/", "vi": "đang khởi tạo thực thể; đang ví dụ"},
  {"id": "lex.en.200k.062796", "hw": "jailbirds", "pos": "noun", "ipa": "/ˈdʒeɪlbɜːrdz/", "vi": "tù nhân có nhiều tiền án tù tội"},
  {"id": "lex.en.200k.062797", "hw": "jujutsus", "pos": "noun", "ipa": "/dʒuːˈdʒuːtsuːz/", "vi": "môn võ nhu thuật cổ truyền Nhật Bản"},
  {"id": "lex.en.200k.062798", "hw": "kiangs", "pos": "noun", "ipa": "/kiˈɑːŋz/", "vi": "lừa hoang lớn cao nguyên Tây Tạng"},
  {"id": "lex.en.200k.062799", "hw": "landmans", "pos": "noun", "ipa": "/ˈlændmənz/", "vi": "người tìm đất dầu khí; nông dân"},
  {"id": "lex.en.200k.062800", "hw": "lebensraums", "pos": "noun", "ipa": "/ˈleɪbənsraʊmz/", "vi": "thuyết không gian sinh tồn mở rộng"},
  {"id": "lex.en.200k.062801", "hw": "lessepses", "pos": "noun", "ipa": "/ləˈsɛpsɪz/", "vi": "nhà ngoại giao đào kênh đào Suez"},
  {"id": "lex.en.200k.062802", "hw": "ludas", "pos": "noun", "ipa": "/ˈluːdəz/", "vi": "thành phố Lữ Đại cũ ở Trung Quốc"}
]

with open('scratch/b33_r06_raw_p3.json') as f:
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

with open('scratch/b33_r06_p3.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r06_p3.json OK")
