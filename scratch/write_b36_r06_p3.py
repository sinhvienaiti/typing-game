import json

rows = [
    ("077703", "politicker", "noun", "/ˈpɑːlɪtɪkər/", "chính khách chạy chọt vận động"),
    ("077704", "politicking", "noun", "/ˈpɑːlɪˌtɪkɪŋ/", "hoạt động vận động chính trị"),
    ("077705", "politicly", "adv", "/ˈpɒlɪtɪkli/", "một cách khôn ngoan, khéo léo"),
    ("077706", "politicomania", "noun", "/pəˌlɪtɪkoʊˈmeɪniə/", "chứng cuồng chính trị"),
    ("077707", "pollachius", "noun", "/pɒˈleɪkiəs/", "chi cá minh thái (Pollachius)"),
    ("077708", "pollakanthic", "adj", "/ˌpɒləˈkænθɪk/", "nở hoa nhiều lần trong đời (cây)"),
    ("077709", "polled", "verb", "/poʊld/", "đã thăm dò ý kiến; đã bỏ phiếu"),
    ("077710", "pollenate", "verb", "/ˈpɑːləneɪt/", "thụ phấn (thực vật)"),
    ("077711", "pollenation", "noun", "/ˌpɑːləˈneɪʃən/", "sự thụ phấn (thực vật)"),
    ("077712", "polleniser", "noun", "/ˈpɒlənaɪzər/", "cây thụ phấn; tác nhân thụ phấn"),
    ("077713", "pollenizer", "noun", "/ˈpɑːlənaɪzər/", "cây thụ phấn; tác nhân thụ phấn"),
    ("077714", "pollenless", "adj", "/ˈpɑːlɪnləs/", "không có phấn hoa"),
    ("077715", "pollenosis", "noun", "/ˌpɒlɪˈnoʊsɪs/", "bệnh dị ứng phấn hoa theo mùa"),
    ("077716", "poller", "noun", "/ˈpoʊlər/", "cử tri đi bầu; người thăm dò ý kiến"),
    ("077717", "pollical", "adj", "/ˈpɒlɪkəl/", "thuộc ngón tay cái (giải phẫu)"),
    ("077718", "pollicitation", "noun", "/pəˌlɪsɪˈteɪʃən/", "lời hứa đơn phương (luật La Mã)"),
    ("077719", "pollinarium", "noun", "/ˌpɒlɪˈnɛriəm/", "khối phấn có gót dính (hoa lan)"),
    ("077720", "pollinated", "verb", "/ˈpɑːlɪˌneɪtɪd/", "đã thụ phấn (hoa)"),
    ("077721", "pollinates", "verb", "/ˈpɑːlɪˌneɪts/", "thụ phấn (cho hoa)"),
    ("077722", "pollinating", "verb", "/ˈpɑːlɪˌneɪtɪŋ/", "thụ phấn (cho hoa)"),
    ("077723", "polling", "verb", "/ˈpoʊlɪŋ/", "thăm dò ý kiến; bỏ phiếu bầu cử"),
    ("077724", "pollinic", "adj", "/pəˈlɪnɪk/", "thuộc phấn hoa"),
    ("077725", "polliniferous", "adj", "/ˌpɒlɪˈnɪfərəs/", "có sinh phấn hoa (thực vật)"),
    ("077726", "pollinium", "noun", "/pəˈlɪniəm/", "khối phấn hoa (hoa lan, thiên lý)"),
    ("077727", "pollinization", "noun", "/ˌpɑːlɪnaɪˈzeɪʃən/", "sự thụ phấn (thực vật học)"),
    ("077728", "pollinize", "verb", "/ˈpɑːlɪnaɪz/", "thụ phấn nhân tạo cho hoa"),
    ("077729", "pollinizer", "noun", "/ˈpɑːlɪnaɪzər/", "cây cung cấp phấn hoa thụ phấn"),
    ("077730", "pollinodium", "noun", "/ˌpɒlɪˈnoʊdiəm/", "cơ quan sinh giao tử đực (nấm, tảo)"),
    ("077731", "pollinoid", "noun", "/ˈpɒlɪnɔɪd/", "giao tử đực không roi (nấm, tảo)"),
    ("077732", "pollinose", "adj", "/ˈpɒlɪnoʊs/", "phủ bụi phấn trắng (côn trùng)"),
    ("077733", "pollinosis", "noun", "/ˌpɒlɪˈnoʊsɪs/", "viêm mũi dị ứng phấn hoa theo mùa"),
    ("077734", "polliwog", "noun", "/ˈpɑːliˌwɒɡ/", "con nòng nọc"),
    ("077735", "polloi", "noun", "/pəˈlɔɪ/", "dân thường, quần chúng (hoi polloi)"),
    ("077736", "pollucite", "noun", "/ˈpɒljuːsaɪt/", "khoáng vật pollucit (quặng xesi)"),
    ("077737", "pollutes", "verb", "/pəˈluːts/", "gây ô nhiễm, làm nhiễm bẩn"),
    ("077738", "polluting", "verb", "/pəˈluːtɪŋ/", "gây ô nhiễm, làm nhiễm bẩn"),
    ("077739", "pollyanna", "noun", "/ˌpɑːliˈænə/", "người lạc quan mù quáng thái quá"),
    ("077740", "pollyannaish", "adj", "/ˌpɑːliˈænəɪʃ/", "lạc quan ngây thơ thái quá"),
    ("077741", "pollyfish", "noun", "/ˈpɑːliˌfɪʃ/", "cá vẹt biển; cá mó rạn san hô"),
    ("077742", "poloist", "noun", "/ˈpoʊloʊɪst/", "vận động viên chơi môn polo"),
    ("077743", "polonian", "adj", "/pəˈloʊniən/", "thuộc Ba Lan hoặc người Ba Lan"),
    ("077744", "poloniums", "noun", "/pəˈloʊniəmz/", "nguyên tố phóng xạ poloni (Po)"),
    ("077745", "polospore", "noun", "/ˈpoʊloʊspɔːr/", "hạt phấn hóa thạch cổ sinh"),
    ("077746", "polster", "noun", "/ˈpoʊlstər/", "cây bụi dạng gối sát mặt đất"),
    ("077747", "poltergeister", "noun", "/ˈpɔːltərˌɡaɪstər/", "ma quái gõ phá đồ (số nhiều Đức)"),
    ("077748", "poltroonery", "noun", "/pɑːlˈtruːnəri/", "sự hèn nhát, thói nhát gan"),
    ("077749", "poly", "noun", "/ˈpɑːli/", "trường bách khoa; đa (viết tắt)"),
    ("077750", "polyadelphous", "adj", "/ˌpɒliəˈdɛlfəs/", "có nhị tụ thành nhiều bó (thực vật)"),
    ("077751", "polyadenous", "adj", "/ˌpɒliˈædɪnəs/", "có nhiều tuyến (sinh học)"),
    ("077752", "polyadic", "adj", "/ˌpɒliˈædɪk/", "có nhiều ngôi, nhiều tham số (toán)"),
    ("077753", "polyandric", "adj", "/ˌpɒliˈændrɪk/", "thuộc chế độ đa phu (nhiều chồng)"),
    ("077754", "polyandrist", "noun", "/ˌpɒliˈændrɪst/", "phụ nữ theo chế độ đa phu"),
    ("077755", "polyangiaceae", "noun", "/ˌpɒliændʒiˈeɪsiː/", "họ Vi khuẩn nhầy Polyangiaceae"),
    ("077756", "polyangium", "noun", "/ˌpɒliˈændʒiəm/", "chi vi khuẩn nhầy Polyangium"),
    ("077757", "polybasic", "adj", "/ˌpɒliˈbeɪsɪk/", "đa bazơ (axit nhiều chức)"),
    ("077758", "polyblast", "noun", "/ˈpɒlɪblæst/", "đại thực bào mô (y học)"),
    ("077759", "polyborus", "noun", "/pəˈlɪbərəs/", "chi chim ưng ăn xác Polyborus"),
    ("077760", "polybotria", "noun", "/ˌpɒlɪˈbɒtriə/", "chi dương xỉ leo Polybotrya"),
    ("077761", "polybotrya", "noun", "/ˌpɒlɪˈbɒtriə/", "chi dương xỉ leo Polybotrya"),
    ("077762", "polybutene", "noun", "/ˌpɒlɪˈbjuːtiːn/", "nhựa dẻo polybuten"),
    ("077763", "polycarpellary", "adj", "/ˌpɒlɪˈkɑːrpəˌlɛri/", "có nhiều lá noãn (thực vật)"),
    ("077764", "polycarpous", "adj", "/ˌpɒlɪˈkɑːrpəs/", "có nhiều lá noãn; kết quả nhiều mùa"),
    ("077765", "polycellular", "adj", "/ˌpɒlɪˈsɛljələr/", "đa bào (gồm nhiều tế bào)"),
    ("077766", "polycentric", "adj", "/ˌpɒlɪˈsɛntrɪk/", "đa tâm, có nhiều trung tâm"),
    ("077767", "polycentrism", "noun", "/ˌpɒlɪˈsɛntrɪzəm/", "thuyết đa trung tâm (chính trị)"),
    ("077768", "polycephalous", "adj", "/ˌpɒlɪˈsɛfələs/", "có nhiều đầu (sinh học, thần thoại)"),
    ("077769", "polychaetous", "adj", "/ˌpɒlɪˈkiːtəs/", "thuộc lớp Giun nhiều tơ"),
    ("077770", "polychasial", "adj", "/ˌpɒlɪˈkeɪʒəl/", "thuộc cụm hoa xim nhiều ngả"),
    ("077771", "polychasium", "noun", "/ˌpɒlɪˈkeɪʒəm/", "cụm hoa xim nhiều ngả (thực vật)"),
    ("077772", "polychete", "noun", "/ˈpɒlɪkiːt/", "giun nhiều tơ (biển)"),
    ("077773", "polychord", "noun", "/ˈpɒlɪkɔːrd/", "đàn nhiều dây (âm nhạc)"),
    ("077774", "polychromic", "adj", "/ˌpɒlɪˈkroʊmɪk/", "nhiều màu sắc, đa sắc"),
    ("077775", "polychromise", "verb", "/ˈpɒlɪkroʊmaɪz/", "tô nhiều màu, làm cho đa sắc"),
    ("077776", "polychromize", "verb", "/ˈpɒlɪkroʊmaɪz/", "tô nhiều màu, làm cho đa sắc"),
    ("077777", "polychromy", "noun", "/ˈpɒlɪkroʊmi/", "nghệ thuật trang trí đa sắc"),
    ("077778", "polychronism", "noun", "/pəˈlɪkrənɪzəm/", "hiện tượng tồn tại qua nhiều kỷ"),
    ("077779", "polycillin", "noun", "/ˌpɒlɪˈsɪlɪn/", "kháng sinh ampicillin (Polycillin)"),
    ("077780", "polycirrus", "noun", "/ˌpɒlɪˈsɪrəs/", "chi giun nhiều tơ Polycirrus"),
    ("077781", "polyclinic", "noun", "/ˌpɒlɪˈklɪnɪk/", "phòng khám đa khoa"),
    ("077782", "polycondensation", "noun", "/ˌpɒlɪˌkɒndɛnˈseɪʃən/", "phản ứng đa trùng ngưng (hóa học)"),
    ("077783", "polyconic", "adj", "/ˌpɒlɪˈkɒnɪk/", "thuộc phép chiếu bản đồ đa nón"),
    ("077784", "polycot", "noun", "/ˈpɒlɪkɒt/", "cây có nhiều hơn hai lá mầm"),
    ("077785", "polycotyl", "noun", "/ˌpɒlɪˈkɒtɪl/", "cây có nhiều hơn hai lá mầm"),
    ("077786", "polycotyledon", "noun", "/ˌpɒlɪˌkɒtɪˈliːdən/", "cây nhiều lá mầm (như cây thông)"),
    ("077787", "polycracy", "noun", "/pəˈlɪkrəsi/", "chính thể nhiều người cùng cai trị"),
    ("077788", "polycrystal", "adj", "/ˌpɒlɪˈkrɪstəl/", "có cấu trúc đa tinh thể"),
    ("077789", "polycyclic", "adj", "/ˌpɒlɪˈsaɪklɪk/", "đa vòng (hóa học); nhiều chu kỳ"),
    ("077790", "polycystic", "adj", "/ˌpɒlɪˈsɪstɪk/", "đa nang, có nhiều u nang (y học)"),
    ("077791", "polycythaemia", "noun", "/ˌpɒlɪsaɪˈθiːmiə/", "bệnh đa hồng cầu (y học)"),
    ("077792", "polycythaemic", "adj", "/ˌpɒlɪsaɪˈθiːmɪk/", "mắc bệnh đa hồng cầu (y học)"),
    ("077793", "polydactylism", "noun", "/ˌpɒlɪˈdæktɪlɪzəm/", "tật thừa ngón tay, ngón chân"),
    ("077794", "polydactylous", "adj", "/ˌpɒlɪˈdæktɪləs/", "mắc tật thừa ngón tay, ngón chân"),
    ("077795", "polydactylus", "noun", "/ˌpɒlɪˈdæktɪləs/", "chi cá nhụ (Polydactylus)"),
    ("077796", "polydaemonism", "noun", "/ˌpɒlɪˈdiːmənɪzəm/", "tín ngưỡng đa thần linh, đa ma quỷ"),
    ("077797", "polydelphous", "adj", "/ˌpɒlɪˈdɛlfəs/", "có nhị tụ thành nhiều bó"),
    ("077798", "polydemonism", "noun", "/ˌpɒlɪˈdiːmənɪzəm/", "tín ngưỡng đa thần linh, đa ma quỷ"),
    ("077799", "polydimensional", "adj", "/ˌpɒlɪdɪˈmɛnʃənəl/", "nhiều chiều, đa chiều"),
    ("077800", "polydodecahedrons", "noun", "/ˌpɒlɪˌdoʊdɛkəˈhiːdrənz/", "hình khối đa thập nhị diện"),
    ("077801", "polyembryonic", "adj", "/ˌpɒlɪˌɛmbriˈɒnɪk/", "đa phôi (tạo nhiều phôi một hạt)"),
    ("077802", "polyembryony", "noun", "/ˌpɒlɪˈɛmbriəni/", "hiện tượng đa phôi (sinh học)"),
]

with open("scratch/b36_r06_raw_p3.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

assert len(raw) == len(rows) == 100
out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, rows):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} vs {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} vs {hw}"
    assert len(vi) <= 35, f"vi too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.count("/") == 2 and not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"bad ipa: {hw} -> {ipa}"
    r["pos"] = pos
    r["ipa"] = ipa
    r["vi"] = vi
    r["status"] = "reviewed"
    out.append(r)

with open("scratch/b36_r06_p3.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r06_p3 saved OK")
