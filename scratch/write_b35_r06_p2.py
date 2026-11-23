import json

items = [
    ("072603", "eggbeaters", "noun", "/ˈɛɡˌbiːtərz/", "máy đánh trứng cầm tay"),
    ("072604", "elytrons", "noun", "/ˈɛlɪtrɒnz/", "cánh cứng che ngoài (bọ cánh cứng)"),
    ("072605", "enkindles", "verb", "/ɪnˈkɪndəlz/", "nhóm lửa đốt cháy; khơi dậy (cổ)"),
    ("072606", "enkindling", "verb", "/ɪnˈkɪndlɪŋ/", "đang đốt cháy; đang khơi dậy"),
    ("072607", "ergodicities", "noun", "/ˌɜːrɡəˈdɪsɪtiz/", "tính ergodic (lý thuyết xác suất)"),
    ("072608", "ergotisms", "noun", "/ˈɜːrɡəˌtɪzəmz/", "chứng ngộ độc nấm cựa gà"),
    ("072609", "euphrosynes", "noun", "/juːˈfrɒzɪˌniːz/", "nữ thần vui tươi Euphrosyne Hy Lạp"),
    ("072610", "factorisations", "noun", "/ˌfæktəraɪˈzeɪʃənz/", "sự phân tích thành thừa số (Anh)"),
    ("072611", "fireguards", "noun", "/ˈfaɪərˌɡɑːrdz/", "tấm lưới chắn lò sưởi; lính trực"),
    ("072612", "gabfests", "noun", "/ˈɡæbˌfɛsts/", "buổi tụ tập tán gẫu trò chuyện"),
    ("072613", "gallinules", "noun", "/ˈɡælɪˌnjuːlz/", "chim trích cồ gà nước đầm lầy"),
    ("072614", "ganesas", "noun", "/ɡəˈneɪʃəz/", "thần đầu voi Ganesha Ấn Độ giáo"),
    ("072615", "garrotted", "verb", "/ɡəˈrɒtɪd/", "đã siết cổ hành quyết (biến thể)"),
    ("072616", "garrottes", "noun", "/ɡəˈrɒts/", "vòng siết cổ tử hình; dây siết cổ"),
    ("072617", "garrotting", "verb", "/ɡəˈrɒtɪŋ/", "đang siết cổ bằng dây hành quyết"),
    ("072618", "gascognes", "noun", "/ɡæsˈkɒnjəz/", "vùng đất Gascony ở tây nam Pháp"),
    ("072619", "gasmasks", "noun", "/ˈɡæsˌmæsks/", "mặt nạ phòng độc lọc khí"),
    ("072620", "geans", "noun", "/dʒiːnz/", "cây hoặc quả anh đào dại ngọt"),
    ("072621", "gimels", "noun", "/ˈɡɪməlz/", "chữ cái thứ ba gimel bảng Do Thái"),
    ("072622", "grunters", "noun", "/ˈɡrʌntərz/", "người cằn nhằn; cá sạo biển; lợn"),
    ("072623", "hadrosaurs", "noun", "/ˈhædrəˌsɔːrz/", "khủng long mỏ vịt (Hadrosaur)"),
    ("072624", "headstalls", "noun", "/ˈhɛdˌstɔːlz/", "dây rọ đầu giữ cương ngựa"),
    ("072625", "heptagons", "noun", "/ˈhɛptəˌɡɒnz/", "hình thất giác có bảy cạnh"),
    ("072626", "houyhnhnmses", "noun", "/ˈhwɪnɪmzɪz/", "giống ngựa thông minh Houyhnhnm"),
    ("072627", "inclinometers", "noun", "/ˌɪnklɪˈnɒmɪtərz/", "máy đo độ nghiêng; từ khuynh kế"),
    ("072628", "incorruptions", "noun", "/ˌɪnkəˈrʌpʃənz/", "tính thanh liêm; sự bất hoại"),
    ("072629", "indistinguishabilities", "noun", "/ˌɪndɪstɪŋɡwɪʃəˈbɪlɪtiz/", "tính không thể phân biệt rạch ròi"),
    ("072630", "instrumentalisms", "noun", "/ˌɪnstrəˈmɛntəˌlɪzəmz/", "chủ nghĩa công cụ (triết học)"),
    ("072631", "jalousies", "noun", "/ˈdʒæləsiz/", "cửa chớp lá sách chỉnh sáng gió"),
    ("072632", "jingoists", "noun", "/ˈdʒɪŋɡoʊɪsts/", "kẻ sô vanh hiếu chiến cuồng tín"),
    ("072633", "keratoconjunctivitides", "noun", "/ˌkɛrətoʊkənˌdʒʌŋktɪˈvaɪtɪdiːz/", "viêm kết-giác mạc ở mắt (y học)"),
    ("072634", "kunzites", "noun", "/ˈkʊntsaɪts/", "đá quý kunzit sắc hồng tím nhạt"),
    ("072635", "lamiaceaes", "noun", "/ˌleɪmiˈeɪʃiˌiːz/", "họ Hoa môi (húng quế, bạc hà)"),
    ("072636", "liriodendra", "noun", "/ˌlɪrioʊˈdɛndrə/", "chi Cây hoàng dương tulip (cổ thụ)"),
    ("072637", "liriodendrons", "noun", "/ˌlɪrioʊˈdɛndrənz/", "chi Cây hoàng dương tulip gỗ quý"),
    ("072638", "lunulae", "noun", "/ˈluːnjʊˌliː/", "vùng trăng lưỡi liềm gốc móng tay"),
    ("072639", "lunulas", "noun", "/ˈluːnjʊləz/", "vùng trăng lưỡi liềm gốc móng tay"),
    ("072640", "lusatians", "noun", "/luːˈzeɪʃənz/", "người và tiếng Sorbia (Lusatia)"),
    ("072641", "lyophilizations", "noun", "/laɪˌɒfɪlaɪˈzeɪʃənz/", "kỹ thuật sấy đông khô bảo quản"),
    ("072642", "measurabilities", "noun", "/ˌmɛʒərəˈbɪlɪtiz/", "tính khả đo có thể đo lường được"),
    ("072643", "meleagrises", "noun", "/ˌmɛliˈæɡrɪsɪz/", "chi Gà tây Bắc Mỹ (Meleagris)"),
    ("072644", "mimamsas", "noun", "/mɪˈmɑːmsəz/", "trường phái triết học Mimamsa Ấn"),
    ("072645", "mocambiques", "noun", "/ˌmoʊsæmˈbiːks/", "nước Mozambique (cách viết cũ)"),
    ("072646", "monardas", "noun", "/məˈnɑːrdəz/", "cây bạc hà ong hoa đỏ Monarda"),
    ("072647", "monistats", "noun", "/ˈmɒnɪstæts/", "thuốc trị nấm phụ khoa Monistat"),
    ("072648", "mrems", "noun", "/ˈmɪlɪˌrɛmz/", "đơn vị bức xạ millirem (mrem)"),
    ("072649", "myriophyllums", "noun", "/ˌmɪriəˈfɪləmz/", "cây rong thủy sinh Myriophyllum"),
    ("072650", "naggers", "noun", "/ˈnæɡərz/", "người hay cằn nhằn than phiền dai"),
    ("072651", "neoplatonists", "noun", "/ˌniːoʊˈpleɪtənɪsts/", "triết gia theo thuyết Tân Plato"),
    ("072652", "numerosities", "noun", "/ˌnjuːməˈrɒsɪtiz/", "số lượng đông đúc; lực lượng"),
    ("072653", "octoroons", "noun", "/ˌɒktəˈruːnz/", "người lai một phần tám gốc Phi"),
    ("072654", "otoscleroses", "noun", "/ˌoʊtoʊsklɪˈroʊsiːz/", "bệnh xơ cứng xương bàn đạp tai"),
    ("072655", "peronosporas", "noun", "/ˌpɛrənˈɒspərəz/", "nấm sương mai hại cây Peronospora"),
    ("072656", "petcocks", "noun", "/ˈpɛtˌkɒks/", "van xả khí hoặc xả nước cỡ nhỏ"),
    ("072657", "pianisms", "noun", "/piˈænɪzəmz/", "kỹ thuật biểu diễn đàn dương cầm"),
    ("072658", "plecopteras", "noun", "/plɪˈkɒptərəz/", "bộ Cánh úp (bọ đá sống gần suối)"),
    ("072659", "portrayers", "noun", "/pɔːrˈtreɪərz/", "người khắc họa mô tả; diễn viên"),
    ("072660", "precipitators", "noun", "/prɪˈsɪpɪˌteɪtərz/", "máy lọc bụi tĩnh điện; tác nhân"),
    ("072661", "pronators", "noun", "/proʊˈneɪtərz/", "cơ quay sấp cẳng tay (giải phẫu)"),
    ("072662", "protistas", "noun", "/proʊˈtɪstəz/", "giới Nguyên sinh vật (Protista)"),
    ("072663", "protoplasts", "noun", "/ˈproʊtəˌplæsts/", "tế bào trần mất vách; nguyên sinh"),
    ("072664", "pyracanthas", "noun", "/ˌpaɪrəˈkænθəz/", "cây táo gai lửa (chi Pyracantha)"),
    ("072665", "reaved", "verb", "/riːvd/", "đã cướp đoạt, chia lìa (từ cổ)"),
    ("072666", "reaves", "verb", "/riːvz/", "cướp đoạt, làm chia lìa (từ cổ)"),
    ("072667", "reaving", "verb", "/ˈriːvɪŋ/", "đang cướp đoạt, làm chia lìa (cổ)"),
    ("072668", "reticulocytes", "noun", "/rɪˈtɪkjʊloʊˌsaɪts/", "hồng cầu lưới (hồng cầu non máu)"),
    ("072669", "roseolas", "noun", "/roʊˈziːələz/", "bệnh sốt phát ban đào ở trẻ nhỏ"),
    ("072670", "rutiluses", "noun", "/ˈruːtɪləsɪz/", "chi Cá roach châu Âu (Rutilus)"),
    ("072671", "saltworkses", "noun", "/ˈsɔːltˌwɜːrksɪz/", "xưởng sản xuất muối công nghiệp"),
    ("072672", "sawbucks", "noun", "/ˈsɔːˌbʌks/", "giá chữ X kê cưa gỗ; tờ 10 đô la"),
    ("072673", "scathes", "noun", "/skeɪðz/", "thiệt hại; làm tổn thương nặng"),
    ("072674", "scrutineers", "noun", "/ˌskruːtɪˈnɪərz/", "người giám sát kiểm phiếu bầu cử"),
    ("072675", "shawwals", "noun", "/ʃɑːˈwɑːlz/", "tháng thứ mười lịch Hồi giáo"),
    ("072676", "shirkers", "noun", "/ˈʃɜːrkərz/", "kẻ trốn tránh đùn đẩy trách nhiệm"),
    ("072677", "spoonerisms", "noun", "/ˈspuːnəˌrɪzəmz/", "lỗi nói lái đảo âm đầu hài hước"),
    ("072678", "staels", "noun", "/stɑːlz/", "nữ văn sĩ Pháp Madame de Staël"),
    ("072679", "streptokinases", "noun", "/ˌstrɛptoʊˈkaɪneɪsɪz/", "thuốc tan huyết khối streptokinase"),
    ("072680", "sundogs", "noun", "/ˈsʌnˌdɒɡz/", "hiện tượng mặt trời giả ảo ảnh"),
    ("072681", "synergists", "noun", "/ˈsɪnərdʒɪsts/", "chất hiệp đồng tăng tác dụng; cơ"),
    ("072682", "syphs", "noun", "/sɪfs/", "bệnh giang mai (viết tắt lóng)"),
    ("072683", "syzygiums", "noun", "/sɪˈzɪdʒiəmz/", "chi Trâm (cây mận roi, đinh hương)"),
    ("072684", "tanaches", "noun", "/tɑːˈnɑːks/", "Kinh Thánh Do Thái Tanakh"),
    ("072685", "taxodiums", "noun", "/tækˈsoʊdiəmz/", "cây bụt mọc bách đầm lầy Taxodium"),
    ("072686", "teths", "noun", "/tɛθs/", "chữ cái thứ chín teth bảng Do Thái"),
    ("072687", "tortfeasors", "noun", "/ˈtɔːrtˌfiːzərz/", "người vi phạm gây thiệt hại dân sự"),
    ("072688", "triboliums", "noun", "/traɪˈboʊliəmz/", "chi Mọt bột đỏ hại ngũ cốc"),
    ("072689", "ugrians", "noun", "/ˈjuːɡriənz/", "người và nhóm ngôn ngữ Ugria"),
    ("072690", "ullrs", "noun", "/ˈʊlərz/", "thần săn bắn Ullr thần thoại Bắc Âu"),
    ("072691", "ultramontanes", "noun", "/ˌʌltrəˈmɒnteɪnz/", "người ủng hộ quyền Giáo hoàng"),
    ("072692", "unguiculatas", "noun", "/ʌŋˌɡwɪkjʊˈleɪtəz/", "nhóm Thú có móng vuốt (cổ điển)"),
    ("072693", "vaporisations", "noun", "/ˌveɪpəraɪˈzeɪʃənz/", "sự bốc hơi hóa thành hơi (Anh)"),
    ("072694", "vernixes", "noun", "/ˈvɜːrnɪksɪz/", "lớp chất gây phủ da trẻ sơ sinh"),
    ("072695", "viperas", "noun", "/ˈvaɪpərəz/", "chi Rắn lục độc châu Âu (Vipera)"),
    ("072696", "volanses", "noun", "/ˈvoʊlænzɪz/", "chòm sao Phi Ngư (Cá Chuồn)"),
    ("072697", "watercolorists", "noun", "/ˈwɔːtərˌkʌlərɪsts/", "họa sĩ chuyên vẽ tranh màu nước"),
    ("072698", "webworms", "noun", "/ˈwɛbˌwɜːrmz/", "sâu tơ nhả màng ăn lá cây"),
    ("072699", "xanthia", "noun", "/ˈzænθiə/", "cây ké đầu ngựa (chi Xanthium)"),
    ("072700", "zymogens", "noun", "/ˈzaɪmədʒənz/", "tiền chất enzym bất hoạt (zymogen)"),
    ("072701", "abbacies", "noun", "/ˈæbəsiz/", "chức vụ tu viện trưởng (bề trên)"),
    ("072702", "abdominoplasties", "noun", "/æbˈdɒmɪnoʊˌplæstiz/", "phẫu thuật tạo hình thẩm mỹ bụng"),
]

with open("scratch/b35_r06_raw_p2.json") as f:
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

with open("scratch/b35_r06_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r06_p2.json OK")
