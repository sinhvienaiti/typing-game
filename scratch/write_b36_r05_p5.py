import json

rows = [
    ("077403", "plumulaceous", "adj", "/ˌpluːmjʊˈleɪʃəs/", "có lông măng, phủ lông tơ mịn"),
    ("077404", "plumular", "adj", "/ˈpluːmjʊlər/", "thuộc lông tơ mịn; thuộc chồi mầm"),
    ("077405", "plumule", "noun", "/ˈpluːmjuːl/", "lông tơ mịn; chồi mầm (hạt cây)"),
    ("077406", "plumulose", "adj", "/ˈpluːmjʊloʊs/", "phủ lông tơ mịn; dạng lông chim"),
    ("077407", "plumy", "adj", "/ˈpluːmi/", "có gắn lông vũ; mềm mượt như lông"),
    ("077408", "plun", "verb", "/plʌn/", "đánh rơi, buông rơi (biến thể cổ)"),
    ("077409", "plunderable", "adj", "/ˈplʌndərəbəl/", "có thể bị cướp bóc, bòn rút"),
    ("077410", "plunderage", "noun", "/ˈplʌndərɪdʒ/", "hành vi cướp bóc; tham ô hàng tàu"),
    ("077411", "plunderous", "adj", "/ˈplʌndərəs/", "có tính cướp bóc, cướp phá"),
    ("077412", "plunders", "verb", "/ˈplʌndərz/", "cướp bóc, cướp phá, bòn rút"),
    ("077413", "plunged", "verb", "/plʌndʒd/", "đã lao xuống mạnh; nhúng sâu; sụt"),
    ("077414", "plunges", "verb", "/ˈplʌndʒɪz/", "lao xuống mạnh; nhúng sâu; sụt giảm"),
    ("077415", "plunging", "verb", "/ˈplʌndʒɪŋ/", "lao xuống mạnh; nhúng sâu; sụt giảm"),
    ("077416", "plunker", "noun", "/ˈplʌŋkər/", "cú đánh mạnh (bóng chày); đồng xu"),
    ("077417", "pluralisation", "noun", "/ˌplʊərəlaɪˈzeɪʃən/", "sự chuyển sang dạng số nhiều"),
    ("077418", "pluralise", "verb", "/ˈplʊərəlaɪz/", "chuyển sang số nhiều; đa nguyên hóa"),
    ("077419", "pluralised", "verb", "/ˈplʊərəlaɪzd/", "đã chuyển sang số nhiều; đa nguyên"),
    ("077420", "pluralises", "verb", "/ˈplʊərəlaɪzɪz/", "chuyển sang số nhiều; đa nguyên hóa"),
    ("077421", "pluralising", "verb", "/ˈplʊərəlaɪzɪŋ/", "chuyển sang số nhiều; đa nguyên hóa"),
    ("077422", "pluralistically", "adv", "/ˌplʊərəˈlɪstɪkli/", "theo quan điểm đa nguyên"),
    ("077423", "plurally", "adv", "/ˈplʊərəli/", "theo nghĩa số nhiều; ở số nhiều"),
    ("077424", "pluriaxial", "adj", "/ˌplʊəriˈæksiəl/", "có nhiều trục (sinh trưởng cây)"),
    ("077425", "pluriform", "adj", "/ˈplʊərɪfɔːrm/", "đa dạng, có nhiều hình thái"),
    ("077426", "pluriglandular", "adj", "/ˌplʊərɪˈɡlændjələr/", "nhiều tuyến nội tiết (y học)"),
    ("077427", "pluriharmonic", "adj", "/ˌplʊərihɑːrˈmɒnɪk/", "đa điều hòa (toán giải tích phức)"),
    ("077428", "plurilocular", "adj", "/ˌplʊərɪˈlɒkjələr/", "có nhiều ngăn, nhiều ô (sinh học)"),
    ("077429", "plurinuclear", "adj", "/ˌplʊərɪˈnuːkliər/", "có nhiều nhân tế bào (đa nhân)"),
    ("077430", "pluriparous", "adj", "/plʊˈrɪpərəs/", "đã sinh nở nhiều lần (sản khoa)"),
    ("077431", "pluripartite", "adj", "/ˌplʊərɪˈpɑːrtaɪt/", "chia thành nhiều thùy, nhiều phần"),
    ("077432", "pluripary", "noun", "/plʊˈrɪpəri/", "tính trạng sinh nở nhiều lứa"),
    ("077433", "pluripolar", "adj", "/ˌplʊərɪˈpoʊlər/", "đa cực (có nhiều cực phân bào)"),
    ("077434", "plurisegmental", "adj", "/ˌplʊərɪsɛɡˈmɛntəl/", "gồm nhiều đốt, nhiều đoạn"),
    ("077435", "plurisporous", "adj", "/ˌplʊərɪˈspɔːrəs/", "có nhiều bào tử"),
    ("077436", "plurisubharmonic", "adj", "/ˌplʊərɪˌsʌbhɑːrˈmɒnɪk/", "đa điều hòa dưới (toán học)"),
    ("077437", "plurivalent", "adj", "/ˌplʊərɪˈveɪlənt/", "đa hóa trị; mang nhiều ý nghĩa"),
    ("077438", "plurivorous", "adj", "/plʊˈrɪvərəs/", "ăn tạp nhiều loài ký chủ khác nhau"),
    ("077439", "plushily", "adv", "/ˈplʌʃɪli/", "sang trọng, êm ái xa hoa"),
    ("077440", "plushiness", "noun", "/ˈplʌʃinəs/", "vẻ sang trọng, êm mượt xa hoa"),
    ("077441", "plushly", "adv", "/ˈplʌʃli/", "một cách sang trọng, êm mượt"),
    ("077442", "plushness", "noun", "/ˈplʌʃnəs/", "độ êm mượt như nhung; sự xa hoa"),
    ("077443", "plushsuits", "noun", "/ˈplʌʃsuːts/", "bộ đồ thú nhồi bông hóa trang"),
    ("077444", "plussage", "noun", "/ˈplʌsɪdʒ/", "phần dư thêm vào; giá trị cộng thêm"),
    ("077445", "plutarchy", "noun", "/ˈpluːtɑːrki/", "chế độ tài phiệt trị"),
    ("077446", "pluteaceae", "noun", "/ˌpluːtiˈeɪsiː/", "họ Nấm phiến hồng (Pluteaceae)"),
    ("077447", "plutocratical", "adj", "/ˌpluːtəˈkrætɪkəl/", "thuộc giới tài phiệt, chế độ giàu"),
    ("077448", "plutocratically", "adv", "/ˌpluːtəˈkrætɪkli/", "theo kiểu giới tài phiệt trị"),
    ("077449", "plutolatry", "noun", "/pluːˈtɒlətri/", "thói tôn sùng tiền bạc, giàu sang"),
    ("077450", "plutology", "noun", "/pluːˈtɒlədʒi/", "khoa học nghiên cứu sự giàu có"),
    ("077451", "plutonism", "noun", "/ˈpluːtənɪzəm/", "thuyết hỏa thành (địa chất học)"),
    ("077452", "plutonist", "noun", "/ˈpluːtənɪst/", "người theo thuyết hỏa thành"),
    ("077453", "plutonite", "noun", "/ˈpluːtənaɪt/", "đá xâm nhập sâu (địa chất)"),
    ("077454", "plutonomic", "adj", "/ˌpluːtəˈnɒmɪk/", "thuộc kinh tế chính trị (từ cũ)"),
    ("077455", "plutonomist", "noun", "/pluːˈtɒnəmɪst/", "nhà kinh tế chính trị học (cổ)"),
    ("077456", "plutonomy", "noun", "/pluːˈtɒnəmi/", "môn kinh tế chính trị (từ cổ)"),
    ("077457", "plutophile", "noun", "/ˈpluːtəfaɪl/", "người ham mê sự giàu có, tài sản"),
    ("077458", "plutus", "noun", "/ˈpluːtəs/", "thần tài Plutus (Hy Lạp cổ)"),
    ("077459", "pluvial", "adj", "/ˈpluːviəl/", "thuộc mưa; thời kỳ nhiều mưa"),
    ("077460", "pluvianus", "noun", "/pluːviˈeɪnəs/", "chi chim choi choi Ai Cập Pluvianus"),
    ("077461", "pluviograph", "noun", "/ˈpluːviəˌɡræf/", "vũ lượng ký tự ghi lượng mưa"),
    ("077462", "pluviometer", "noun", "/ˌpluːviˈɒmɪtər/", "vũ lượng kế (máy đo lượng mưa)"),
    ("077463", "pluviometric", "adj", "/ˌpluːviəˈmɛtrɪk/", "thuộc phép đo lượng mưa"),
    ("077464", "pluviometrical", "adj", "/ˌpluːviəˈmɛtrɪkəl/", "thuộc phép đo lượng mưa"),
    ("077465", "pluviometrically", "adv", "/ˌpluːviəˈmɛtrɪkli/", "bằng phép đo lượng mưa"),
    ("077466", "pluviometry", "noun", "/ˌpluːviˈɒmətri/", "phép đo lượng mưa"),
    ("077467", "pluviophile", "noun", "/ˈpluːviəfaɪl/", "người yêu mưa, thích ngày mưa"),
    ("077468", "pluviophilous", "adj", "/ˌpluːviˈɒfɪləs/", "ưa mưa, phát triển tốt nơi ẩm mưa"),
    ("077469", "pluvioscope", "noun", "/ˈpluːviəskoʊp/", "dụng cụ đo lượng mưa"),
    ("077470", "pluviose", "noun", "/pluːˈvjoʊz/", "tháng Mưa Pluviose (lịch Pháp cũ)"),
    ("077471", "pluviosity", "noun", "/ˌpluːviˈɒsɪti/", "tính nhiều mưa; lượng mưa"),
    ("077472", "pluvious", "adj", "/ˈpluːviəs/", "có nhiều mưa, ẩm ướt"),
    ("077473", "plyboard", "noun", "/ˈplaɪbɔːrd/", "gỗ ván ép, gỗ dán nhiều lớp"),
    ("077474", "plyer", "noun", "/ˈplaɪər/", "cần kéo cầu nâng; người hành nghề"),
    ("077475", "plying", "verb", "/ˈplaɪɪŋ/", "chăm chú làm; chạy tuyến; chập sợi"),
    ("077476", "plz", "adv", "/pliːz/", "làm ơn, xin vui lòng (viết tắt)"),
    ("077477", "pmt", "noun", "/ˌpiːɛmˈtiː/", "hội chứng tiền kinh nguyệt (PMT)"),
    ("077478", "pnenetration", "noun", "/ˌpɛnɪˈtreɪʃən/", "sự thâm nhập (dạng viết nhầm)"),
    ("077479", "pneuma", "noun", "/ˈnjuːmə/", "tinh thần sống; hơi thở (triết cổ)"),
    ("077480", "pneumas", "noun", "/ˈnjuːməz/", "tinh thần sống; hơi thở (triết cổ)"),
    ("077481", "pneumaticity", "noun", "/ˌnjuːməˈtɪsɪti/", "tính chứa khí nén; có túi khí"),
    ("077482", "pneumatised", "adj", "/ˈnjuːmətaɪzd/", "có khoang khí rỗng (xương chim)"),
    ("077483", "pneumatocyst", "noun", "/njuːˈmætəˌsɪst/", "túi khí nổi; bóng hơi cá"),
    ("077484", "pneumatogram", "noun", "/njuːˈmætəɡræm/", "biểu đồ ghi nhịp thở (y học)"),
    ("077485", "pneumatograph", "noun", "/njuːˈmætəɡræf/", "máy ghi đồ thị hô hấp (y học)"),
    ("077486", "pneumatologic", "adj", "/ˌnjuːmətəˈlɒdʒɪk/", "thuộc linh học hoặc khí học"),
    ("077487", "pneumatologist", "noun", "/ˌnjuːməˈtɒlədʒɪst/", "nhà nghiên cứu thần linh học"),
    ("077488", "pneumatology", "noun", "/ˌnjuːməˈtɒlədʒi/", "linh học (thần học); khí học"),
    ("077489", "pneumatolysis", "noun", "/ˌnjuːməˈtɒlɪsɪs/", "sự biến chất do khí nóng (địa chất)"),
    ("077490", "pneumatolytic", "adj", "/ˌnjuːmətəˈlɪtɪk/", "thuộc sự biến chất do khí mácma"),
    ("077491", "pneumatometer", "noun", "/ˌnjuːməˈtɒmɪtər/", "phế dung kế (đo áp lực hô hấp)"),
    ("077492", "pneumatophore", "noun", "/njuːˈmætəfɔːr/", "rễ thở (cây ngập mặn); phao khí"),
    ("077493", "pneumatotactic", "adj", "/ˌnjuːmətəˈtæktɪk/", "có tính hướng khí (sinh vật)"),
    ("077494", "pneumatotaxis", "noun", "/ˌnjuːmətəˈtæksɪs/", "tính hướng khí (di chuyển theo khí)"),
    ("077495", "pneumectomy", "noun", "/njuːˈmɛktəmi/", "phẫu thuật cắt bỏ phổi (y học)"),
    ("077496", "pneumobacillus", "noun", "/ˌnjuːmoʊbəˈsɪləs/", "trực khuẩn gây viêm phổi"),
    ("077497", "pneumococcic", "adj", "/ˌnjuːməˈkɒksɪk/", "thuộc phế cầu khuẩn (y học)"),
    ("077498", "pneumoconioses", "noun", "/ˌnjuːmoʊˌkoʊniˈoʊsiːz/", "bệnh bụi phổi (y học nghề nghiệp)"),
    ("077499", "pneumocytosis", "noun", "/ˌnjuːmoʊsaɪˈtoʊsɪs/", "bệnh viêm phổi do nấm Pneumocystis"),
    ("077500", "pneumoencephalogram", "noun", "/ˌnjuːmoʊɛnˈsɛfələɡræm/", "phim X-quang não bơm khí (cũ)"),
    ("077501", "pneumogastric", "adj", "/ˌnjuːmoʊˈɡæstrɪk/", "thuộc dây thần kinh phế vị"),
    ("077502", "pneumogram", "noun", "/ˈnjuːməɡræm/", "biểu đồ ghi nhịp thở (y học)"),
]

with open("scratch/b36_r05_raw_p5.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r05_p5.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r05_p5 saved OK")
