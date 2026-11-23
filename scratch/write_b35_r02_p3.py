import json

items = [
    ("070703", "plicas", "noun", "/ˈplaɪkəz/", "nếp gấp niêm mạc; nếp gấp da"),
    ("070704", "polyurias", "noun", "/ˌpɒliˈjʊəriəz/", "chứng đa niệu (tiểu nhiều lần)"),
    ("070705", "pottos", "noun", "/ˈpɒtoʊz/", "vượn cáo potto sống về đêm"),
    ("070706", "pressors", "noun", "/ˈprɛsərz/", "thuốc làm tăng huyết áp co mạch"),
    ("070707", "pylori", "noun", "/paɪˈlɔːraɪ/", "môn vị dạ dày; vi khuẩn H. pylori"),
    ("070708", "questers", "noun", "/ˈkwɛstərz/", "người đi tìm kiếm phiêu lưu"),
    ("070709", "radiosensitivities", "noun", "/ˌreɪdioʊsɛnsɪˈtɪvɪtiz/", "độ nhạy cảm với bức xạ ion hóa"),
    ("070710", "resters", "noun", "/ˈrɛstərz/", "người đang nghỉ ngơi thư giãn"),
    ("070711", "rewriters", "noun", "/riːˈraɪtərz/", "người viết lại sửa lại văn bản"),
    ("070712", "rhamnuses", "noun", "/ˈræmnəsɪz/", "cây táo gai hắc mai chi Rhamnus"),
    ("070713", "riparias", "noun", "/rɪˈpɛəriəz/", "chi Chim nhạn cát Riparia"),
    ("070714", "romanisms", "noun", "/ˈroʊməˌnɪzəmz/", "Công giáo La Mã; tập tục La Mã"),
    ("070715", "rubiaceaes", "noun", "/ˌruːbiˈeɪʃiˌiːz/", "họ Cà phê thực vật (Rubiaceae)"),
    ("070716", "sabaoths", "noun", "/ˈsæbiˌɒθs/", "đạo quân thiên binh (Kinh Thánh)"),
    ("070717", "salaahs", "noun", "/sɑːˈlɑːz/", "lễ cầu nguyện Hồi giáo (Salah)"),
    ("070718", "sawhorses", "noun", "/ˈsɔːˌhɔːrsɪz/", "giá kê gỗ chữ A để cưa"),
    ("070719", "saxifragas", "noun", "/sækˈsɪfrəɡəz/", "cây tai hùm phá thạch Saxifraga"),
    ("070720", "scirpuses", "noun", "/ˈsɜːrpəsɪz/", "cây cói lác thuộc chi Scirpus"),
    ("070721", "sebses", "noun", "/ˌɛs iː biː ˈɛsɪz/", "hướng đông-nam chếch nam (SEbS)"),
    ("070722", "setubals", "noun", "/səˈtuːbəlz/", "thành phố cảng Setúbal Bồ Đào Nha"),
    ("070723", "silverplated", "verb", "/ˌsɪlvərˈpleɪtɪd/", "đã mạ bạc lên bề mặt kim loại"),
    ("070724", "silverplates", "verb", "/ˈsɪlvərˌpleɪts/", "mạ bạc phủ lên bề mặt kim loại"),
    ("070725", "silverplating", "verb", "/ˈsɪlvərˌpleɪtɪŋ/", "đang mạ bạc lên bề mặt kim loại"),
    ("070726", "skagerraks", "noun", "/ˈskæɡəˌræks/", "eo biển Skagerrak vùng Bắc Âu"),
    ("070727", "slatterns", "noun", "/ˈslætərnz/", "người phụ nữ lôi thôi luộm thuộm"),
    ("070728", "sorexes", "noun", "/ˈsɔːrɛksɪz/", "chuột chù mõm nhọn thuộc chi Sorex"),
    ("070729", "spatialities", "noun", "/ˌspeɪʃiˈælɪtiz/", "tính chất thuộc về không gian"),
    ("070730", "stentors", "noun", "/ˈstɛntərz/", "người có giọng vang rền; trùng loa"),
    ("070731", "stopcocks", "noun", "/ˈstɒpˌkɒks/", "van khóa vặn điều chỉnh dòng chảy"),
    ("070732", "tangencies", "noun", "/ˈtændʒənsiz/", "điểm hoặc trạng thái tiếp xúc"),
    ("070733", "taraxacums", "noun", "/təˈræksəkəmz/", "cây bồ công anh chi Taraxacum"),
    ("070734", "teacakes", "noun", "/ˈtiːˌkeɪks/", "bánh ngọt nướng phết bơ uống trà"),
    ("070735", "tebaldis", "noun", "/tɛˈbɑːldiz/", "ca sĩ opera Ý Renata Tebaldi"),
    ("070736", "tepics", "noun", "/tɛˈpiːks/", "thành phố Tepic ở tây Mexico"),
    ("070737", "tesserae", "noun", "/ˈtɛsəˌriː/", "mảnh đá gạch khảm tranh mosaic"),
    ("070738", "tesseras", "noun", "/ˈtɛsərəz/", "mảnh đá gạch khảm tranh mosaic"),
    ("070739", "teutons", "noun", "/ˈtjuːtənz/", "người German cổ bộ tộc Teuton"),
    ("070740", "thalassaemias", "noun", "/ˌθæləˈsiːmiəz/", "bệnh tan máu bẩm sinh (Anh)"),
    ("070741", "thermometries", "noun", "/θɜːrˈmɒmɪtriz/", "kỹ thuật đo lường nhiệt độ"),
    ("070742", "underskirts", "noun", "/ˈʌndərˌskɜːrts/", "váy lót mặc bên trong chân váy"),
    ("070743", "upchucked", "verb", "/ˈʌpˌtʃʌkt/", "đã nôn mửa (tiếng lóng Mỹ)"),
    ("070744", "upchucking", "verb", "/ˈʌpˌtʃʌkɪŋ/", "đang nôn mửa (tiếng lóng Mỹ)"),
    ("070745", "upchucks", "verb", "/ˈʌpˌtʃʌks/", "nôn mửa, ói ra (tiếng lóng Mỹ)"),
    ("070746", "uveas", "noun", "/ˈjuːviəz/", "màng bồ đào nằm giữa nhãn cầu"),
    ("070747", "vernonias", "noun", "/vɜːrˈnoʊniəz/", "cây cúc sắt hoa tím chi Vernonia"),
    ("070748", "vocalisations", "noun", "/ˌvoʊkəlaɪˈzeɪʃənz/", "sự phát âm thành tiếng (Anh)"),
    ("070749", "voltarens", "noun", "/vɒlˈtɛərənz/", "thuốc giảm đau kháng viêm Voltaren"),
    ("070750", "zangwills", "noun", "/ˈzæŋɡwɪlz/", "nhà văn Anh Israel Zangwill"),
    ("070751", "accipiters", "noun", "/ækˈsɪpɪtərz/", "chim ưng cắt thuộc chi Accipiter"),
    ("070752", "adnexas", "noun", "/ædˈnɛksəz/", "phần phụ thuộc cơ quan (y học)"),
    ("070753", "aesculapiuses", "noun", "/ˌɛskjʊˈleɪpiəsɪz/", "thần y học Hy Lạp Aesculapius"),
    ("070754", "appeasers", "noun", "/əˈpiːzərz/", "người xoa dịu nhượng bộ kẻ gây hấn"),
    ("070755", "arborvitaes", "noun", "/ˌɑːrbərˈvaɪtiz/", "cây trắc bách diệp; cây sống đời"),
    ("070756", "archaisms", "noun", "/ˈɑːrkeɪˌɪzəmz/", "từ ngữ cổ; lối hành văn cổ xưa"),
    ("070757", "attoseconds", "noun", "/ˈætoʊˌsɛkəndz/", "đơn vị át-tô giây (10^-18 giây)"),
    ("070758", "backdowns", "noun", "/ˈbækˌdaʊnz/", "sự chùn bước nhượng bộ rút lui"),
    ("070759", "baldachins", "noun", "/ˈbɔːldəkɪnz/", "màn tán che phía trên bàn thờ ngai"),
    ("070760", "bmuses", "noun", "/ˌbiː ˈmjuːzɪz/", "bằng Cử nhân Âm nhạc (B.Mus.)"),
    ("070761", "bookfairs", "noun", "/ˈbʊkˌfɛərz/", "hội chợ triển lãm mua bán sách"),
    ("070762", "cablegrams", "noun", "/ˈkeɪbəlˌɡræmz/", "bức điện tín truyền qua cáp biển"),
    ("070763", "canonists", "noun", "/ˈkænənɪsts/", "chuyên gia nghiên cứu giáo luật"),
    ("070764", "cantles", "noun", "/ˈkæntəlz/", "vành hậu yên ngựa; miếng cắt ra"),
    ("070765", "capitates", "noun", "/ˈkæpɪˌteɪts/", "xương cả cổ tay"),
    ("070766", "carked", "verb", "/kɑːrkt/", "đã làm phiền muộn lo âu (cổ)"),
    ("070767", "carks", "verb", "/kɑːrks/", "làm phiền muộn lo âu (cổ)"),
    ("070768", "castillians", "noun", "/kæˈstɪliənz/", "người dân xứ Castile Tây Ban Nha"),
    ("070769", "cefotaximes", "noun", "/ˌsɛfoʊˈtæksiːmz/", "thuốc kháng sinh cefotaxime"),
    ("070770", "chordatas", "noun", "/kɔːrˈdeɪtəz/", "ngành Động vật có dây sống"),
    ("070771", "cinquefoils", "noun", "/ˈsɪŋkˌfɔɪlz/", "cây ỷ lăng năm lá (Potentilla)"),
    ("070772", "clomped", "verb", "/klɒmpt/", "đã bước nặng nề lộp cộp"),
    ("070773", "clomping", "verb", "/ˈklɒmpɪŋ/", "đang bước nặng nề lộp cộp"),
    ("070774", "clomps", "verb", "/klɒmps/", "bước nặng nề phát tiếng lộp cộp"),
    ("070775", "cloyed", "verb", "/klɔɪd/", "đã làm ngấy ngán vì quá ngọt ngào"),
    ("070776", "cloys", "verb", "/klɔɪz/", "làm ngấy ngán vì quá mức ngọt"),
    ("070777", "cocobolos", "noun", "/ˌkoʊkəˈboʊloʊz/", "gỗ cứng quý cocobolo Trung Mỹ"),
    ("070778", "cocottes", "noun", "/koʊˈkɒts/", "gái bao sang trọng (Pháp); nồi sứ"),
    ("070779", "cognized", "verb", "/ˈkɒɡnaɪzd/", "đã nhận thức thấu hiểu (triết)"),
    ("070780", "cognizes", "verb", "/ˈkɒɡnaɪzɪz/", "nhận thức; nhận biết rõ ràng"),
    ("070781", "cognizing", "verb", "/ˈkɒɡnaɪzɪŋ/", "đang nhận thức; đang nhận biết"),
    ("070782", "cordgrasses", "noun", "/ˈkɔːrdˌɡræsɪz/", "cỏ đầm lầy mặn Spartina"),
    ("070783", "crassostreas", "noun", "/ˌkræsɒˈstriːəz/", "chi Hàu Thái Bình Dương và Mỹ"),
    ("070784", "cresols", "noun", "/ˈkriːsɒlz/", "hợp chất sát khuẩn phenol cresol"),
    ("070785", "cromleches", "noun", "/ˈkrɒmlɛks/", "mộ đá cổ cự thạch vòng tròn đá"),
    ("070786", "crossheads", "noun", "/ˈkrɒsˌhɛdz/", "đầu chữ thập pít-tông; tiểu mục"),
    ("070787", "cyperaceaes", "noun", "/ˌsaɪpəˈreɪʃiˌiːz/", "họ Cói thực vật đơn tử diệp"),
    ("070788", "degaussings", "noun", "/diːˈɡaʊsɪŋz/", "quá trình khử từ tính thiết bị"),
    ("070789", "deinonychuses", "noun", "/daɪˈnɒnɪkəsɪz/", "khủng long ăn thịt Deinonychus"),
    ("070790", "democratised", "verb", "/dɪˈmɒkrəˌtaɪzd/", "đã dân chủ hóa thể chế (Anh)"),
    ("070791", "democratises", "verb", "/dɪˈmɒkrəˌtaɪzɪz/", "dân chủ hóa; phổ cập (Anh)"),
    ("070792", "democratising", "verb", "/dɪˈmɒkrəˌtaɪzɪŋ/", "đang dân chủ hóa; phổ cập (Anh)"),
    ("070793", "depilations", "noun", "/ˌdɛpɪˈleɪʃənz/", "sự tẩy rụng lông trên cơ thể"),
    ("070794", "embassadors", "noun", "/ɛmˈbæsədərz/", "đại sứ ngoại giao (cách viết cũ)"),
    ("070795", "envois", "noun", "/ˈɛnvɔɪz/", "khổ thơ kết bài tóm ý; đặc sứ"),
    ("070796", "epistases", "noun", "/ɪˈpɪstəsiːz/", "tương tác gen át chế (di truyền)"),
    ("070797", "espaliers", "noun", "/ɪˈspæljərz/", "giàn khung uốn cây sát tường"),
    ("070798", "foehns", "noun", "/fɜːrnz/", "gió phơn nóng khô thổi xuống sườn"),
    ("070799", "fusees", "noun", "/fjuːˈziːz/", "trục xoắn ốc đồng hồ; pháo sáng"),
    ("070800", "geoducks", "noun", "/ˈɡuːiˌdʌks/", "tu hài vòi voi khổng lồ geoduck"),
    ("070801", "ghostwrites", "verb", "/ˈɡoʊstˌraɪts/", "viết thuê đứng tên người khác"),
    ("070802", "ghostwriting", "verb", "/ˈɡoʊstˌraɪtɪŋ/", "đang viết thuê cho người khác"),
]

with open("scratch/b35_r02_raw_p3.json") as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100
allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}
out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, items):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} != {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} != {hw}"
    assert pos in allowed_pos, f"Bad POS: {pos}"
    assert len(vi) <= 35, f"VI too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA: {hw} -> {ipa}"
    assert not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"Space in IPA: {hw} -> {ipa}"
    out.append({**r, "pos": pos, "ipa": ipa, "vi": vi, "status": "reviewed"})

with open("scratch/b35_r02_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r02_p3.json OK")
