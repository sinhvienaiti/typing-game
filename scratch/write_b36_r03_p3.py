import json

rows = [
    ("076203", "phonologically", "adv", "/ˌfoʊnəˈlɒdʒɪkli/", "về mặt âm vị học"),
    ("076204", "phonologist", "noun", "/fəˈnɒlədʒɪst/", "nhà âm vị học"),
    ("076205", "phonometer", "noun", "/fəˈnɒmɪtər/", "âm lượng kế (máy đo cường độ âm)"),
    ("076206", "phonopathy", "noun", "/fəˈnɒpəθi/", "chứng rối loạn giọng nói, phát âm"),
    ("076207", "phonophobia", "noun", "/ˌfoʊnoʊˈfoʊbiə/", "chứng sợ âm thanh lớn (y học)"),
    ("076208", "phonoreception", "noun", "/ˌfoʊnoʊrɪˈsɛpʃən/", "sự cảm nhận sóng âm (thính giác)"),
    ("076209", "phonoreceptor", "noun", "/ˌfoʊnoʊrɪˈsɛptər/", "thụ thể tiếp nhận âm thanh"),
    ("076210", "phonoscope", "noun", "/ˈfoʊnəskoʊp/", "máy soi sóng âm; máy thử dây đàn"),
    ("076211", "phonotelemeter", "noun", "/ˌfoʊnoʊtɪˈlɛmɪtər/", "máy đo cự ly bằng âm thanh"),
    ("076212", "phonotype", "noun", "/ˈfoʊnətaɪp/", "chữ in phiên âm; bản in phiên âm"),
    ("076213", "phonotypic", "adj", "/ˌfoʊnəˈtɪpɪk/", "thuộc chữ in phiên âm"),
    ("076214", "phonotypical", "adj", "/ˌfoʊnəˈtɪpɪkəl/", "thuộc chữ in phiên âm"),
    ("076215", "phonotypically", "adv", "/ˌfoʊnəˈtɪpɪkli/", "theo lối chữ in phiên âm"),
    ("076216", "phonotypist", "noun", "/fəˈnɒtɪpɪst/", "người dùng hệ chữ phiên âm"),
    ("076217", "phoradendron", "noun", "/ˌfɔːrəˈdɛndrɒn/", "chi tầm gửi giả (Phoradendron)"),
    ("076218", "phormium", "noun", "/ˈfɔːrmiəm/", "cây gai dầu New Zealand (Phormium)"),
    ("076219", "phoronid", "noun", "/fəˈrɒnɪd/", "giun móng ngựa (ngành Phoronida)"),
    ("076220", "phoronida", "noun", "/ˌfɒrəˈnaɪdə/", "ngành Giun móng ngựa (Phoronida)"),
    ("076221", "phoronidea", "noun", "/ˌfɒrəˈnɪdiə/", "lớp Giun móng ngựa (Phoronidea)"),
    ("076222", "phosphatic", "adj", "/fɒsˈfætɪk/", "chứa phốt phát; thuộc phân lân"),
    ("076223", "phosphatise", "verb", "/ˈfɒsfətaɪz/", "xử lý phốt phát hóa (chống gỉ)"),
    ("076224", "phosphatize", "verb", "/ˈfɒsfətaɪz/", "xử lý phốt phát hóa (chống gỉ)"),
    ("076225", "phosphaturia", "noun", "/ˌfɒsfəˈtjʊriə/", "chứng tiểu ra phốt phát (y học)"),
    ("076226", "phosphene", "noun", "/ˈfɒsfiːn/", "hiện tượng đom đóm mắt (nhãn khoa)"),
    ("076227", "phosphide", "noun", "/ˈfɒsfaɪd/", "hợp chất phốt phua (hóa học)"),
    ("076228", "phosphines", "noun", "/ˈfɒsfiːnz/", "khí độc phốt phin (PH3)"),
    ("076229", "phosphinic", "adj", "/fɒsˈfɪnɪk/", "thuộc axit phốt phinic (hóa học)"),
    ("076230", "phosphite", "noun", "/ˈfɒsfaɪt/", "muối phốt phit (hóa học)"),
    ("076231", "phospholysis", "noun", "/fɒsˈfɒlɪsɪs/", "sự phân giải bằng phốt phát"),
    ("076232", "phosphorate", "verb", "/ˈfɒsfəreɪt/", "kết hợp với phốt pho"),
    ("076233", "phosphoresce", "verb", "/ˌfɒsfəˈrɛs/", "phát lân quang (phát sáng yếu)"),
    ("076234", "phosphorescently", "adv", "/ˌfɒsfəˈrɛsəntli/", "bằng ánh sáng lân quang"),
    ("076235", "phosphoreted", "adj", "/ˈfɒsfərɛtɪd/", "đã kết hợp với phốt pho"),
    ("076236", "phosphorise", "verb", "/ˈfɒsfəraɪz/", "tẩm hoặc kết hợp với phốt pho"),
    ("076237", "phosphorised", "verb", "/ˈfɒsfəraɪzd/", "đã tẩm hoặc kết hợp với phốt pho"),
    ("076238", "phosphorises", "verb", "/ˈfɒsfəraɪzɪz/", "tẩm hoặc kết hợp với phốt pho"),
    ("076239", "phosphorising", "verb", "/ˈfɒsfəraɪzɪŋ/", "tẩm hoặc kết hợp với phốt pho"),
    ("076240", "phosphorism", "noun", "/ˈfɒsfərɪzəm/", "chứng ngộ độc phốt pho mãn tính"),
    ("076241", "phosphorite", "noun", "/ˈfɒsfəˌraɪt/", "quặng đá lân phốt phorit"),
    ("076242", "phosphorize", "verb", "/ˈfɒsfəraɪz/", "tẩm hoặc kết hợp với phốt pho"),
    ("076243", "phosphorized", "verb", "/ˈfɒsfəraɪzd/", "đã tẩm hoặc kết hợp với phốt pho"),
    ("076244", "phosphorizes", "verb", "/ˈfɒsfəraɪzɪz/", "tẩm hoặc kết hợp với phốt pho"),
    ("076245", "phosphorizing", "verb", "/ˈfɒsfəraɪzɪŋ/", "tẩm hoặc kết hợp với phốt pho"),
    ("076246", "phosphorograph", "noun", "/ˈfɒsfərəɡræf/", "ảnh chụp bằng ánh sáng lân quang"),
    ("076247", "phosphorography", "noun", "/ˌfɒsfəˈrɒɡrəfi/", "kỹ thuật chụp ảnh bằng lân quang"),
    ("076248", "phosphoroscope", "noun", "/fɒsˈfɒrəskoʊp/", "lân quang kế (dụng cụ đo lân quang)"),
    ("076249", "phossy", "adj", "/ˈfɒsi/", "hoại tử xương hàm do phốt pho"),
    ("076250", "photalgia", "noun", "/foʊˈtældʒə/", "chứng đau mắt do ánh sáng chói"),
    ("076251", "photism", "noun", "/ˈfoʊtɪzəm/", "ảo giác thấy ánh sáng (y học)"),
    ("076252", "photoactive", "adj", "/ˌfoʊtoʊˈæktɪv/", "có tính quang hoạt (nhạy sáng)"),
    ("076253", "photoautotroph", "noun", "/ˌfoʊtoʊˈɔːtətrɒf/", "sinh vật quang tự dưỡng (sinh học)"),
    ("076254", "photoautotrophic", "adj", "/ˌfoʊtoʊˌɔːtəˈtrɒfɪk/", "thuộc sinh vật quang tự dưỡng"),
    ("076255", "photobiologic", "adj", "/ˌfoʊtoʊˌbaɪəˈlɒdʒɪk/", "thuộc quang sinh học"),
    ("076256", "photobiologist", "noun", "/ˌfoʊtoʊbaɪˈɒlədʒɪst/", "nhà quang sinh học"),
    ("076257", "photobiology", "noun", "/ˌfoʊtoʊbaɪˈɒlədʒi/", "ngành quang sinh học"),
    ("076258", "photobiotic", "adj", "/ˌfoʊtoʊbaɪˈɒtɪk/", "chỉ sống được nơi có ánh sáng"),
    ("076259", "photoblepharon", "noun", "/ˌfoʊtoʊˈblɛfərɒn/", "cá mắt phát sáng (Photoblepharon)"),
    ("076260", "photocall", "noun", "/ˈfoʊtoʊˌkɔːl/", "buổi chụp ảnh báo chí (thảm đỏ)"),
    ("076261", "photochemically", "adv", "/ˌfoʊtoʊˈkɛmɪkli/", "bằng phản ứng quang hóa học"),
    ("076262", "photochemist", "noun", "/ˌfoʊtoʊˈkɛmɪst/", "nhà quang hóa học"),
    ("076263", "photochlorination", "noun", "/ˌfoʊtoʊˌklɔːrɪˈneɪʃən/", "phản ứng quang clo hóa (hóa học)"),
    ("076264", "photochromatic", "adj", "/ˌfoʊtoʊkroʊˈmætɪk/", "thuộc ảnh màu; đổi màu theo sáng"),
    ("076265", "photochrome", "noun", "/ˈfoʊtəkroʊm/", "ảnh chụp màu; vật liệu đổi màu sáng"),
    ("076266", "photochromic", "adj", "/ˌfoʊtoʊˈkroʊmɪk/", "đổi màu theo ánh sáng (kính râm)"),
    ("076267", "photochromism", "noun", "/ˌfoʊtoʊˈkroʊmɪzəm/", "hiện tượng đổi màu theo ánh sáng"),
    ("076268", "photochromy", "noun", "/ˈfoʊtəkroʊmi/", "kỹ thuật chụp ảnh màu"),
    ("076269", "photocoagulator", "noun", "/ˌfoʊtoʊkoʊˈæɡjəleɪtər/", "máy quang đông laser (nhãn khoa)"),
    ("076270", "photocombustion", "noun", "/ˌfoʊtoʊkəmˈbʌstʃən/", "sự đốt cháy kích hoạt bằng sáng"),
    ("076271", "photocompose", "verb", "/ˌfoʊtoʊkəmˈpoʊz/", "sắp chữ quang học (in ấn)"),
    ("076272", "photocomposer", "noun", "/ˌfoʊtoʊkəmˈpoʊzər/", "máy hoặc thợ sắp chữ quang học"),
    ("076273", "photocomposition", "noun", "/ˌfoʊtoʊˌkɒmpəˈzɪʃən/", "kỹ thuật sắp chữ quang học"),
    ("076274", "photoconduction", "noun", "/ˌfoʊtoʊkənˈdʌkʃən/", "hiện tượng quang dẫn (vật lý)"),
    ("076275", "photoconductor", "noun", "/ˌfoʊtoʊkənˈdʌktər/", "chất bán dẫn quang dẫn"),
    ("076276", "photocopied", "verb", "/ˈfoʊtoʊˌkɑːpid/", "đã sao chụp tài liệu (photocopy)"),
    ("076277", "photocopies", "noun", "/ˈfoʊtoʊˌkɑːpiz/", "bản sao chụp (photocopy)"),
    ("076278", "photocopying", "verb", "/ˈfoʊtoʊˌkɑːpiɪŋ/", "sao chụp tài liệu (photocopy)"),
    ("076279", "photocurrent", "noun", "/ˈfoʊtoʊˌkɜːrənt/", "dòng quang điện (vật lý)"),
    ("076280", "photodecomposition", "noun", "/ˌfoʊtoʊˌdiːkɒmpəˈzɪʃən/", "sự quang phân hủy (hóa học)"),
    ("076281", "photodetector", "noun", "/ˌfoʊtoʊdɪˈtɛktər/", "cảm biến ánh sáng; bộ tách quang"),
    ("076282", "photodisintegrate", "verb", "/ˌfoʊtoʊdɪsˈɪntɪɡreɪt/", "quang phân rã hạt nhân (vật lý)"),
    ("076283", "photodisintegration", "noun", "/ˌfoʊtoʊdɪsˌɪntɪˈɡreɪʃən/", "sự quang phân rã hạt nhân"),
    ("076284", "photodissociate", "verb", "/ˌfoʊtoʊdɪˈsoʊʃieɪt/", "quang phân ly phân tử (hóa học)"),
    ("076285", "photodissociation", "noun", "/ˌfoʊtoʊdɪˌsoʊsiˈeɪʃən/", "sự quang phân ly phân tử"),
    ("076286", "photodrama", "noun", "/ˈfoʊtoʊˌdrɑːmə/", "kịch bản hoặc phim điện ảnh câm"),
    ("076287", "photodramatic", "adj", "/ˌfoʊtoʊdrəˈmætɪk/", "thuộc kịch điện ảnh"),
    ("076288", "photodramatist", "noun", "/ˌfoʊtoʊˈdræmətɪst/", "tác giả kịch bản điện ảnh"),
    ("076289", "photoed", "verb", "/ˈfoʊtoʊd/", "đã chụp ảnh, chụp hình"),
    ("076290", "photoelectrical", "adj", "/ˌfoʊtoʊɪˈlɛktrɪkəl/", "thuộc hiệu ứng quang điện"),
    ("076291", "photoelectrically", "adv", "/ˌfoʊtoʊɪˈlɛktrɪkli/", "bằng phương pháp quang điện"),
    ("076292", "photoelectricity", "noun", "/ˌfoʊtoʊɪlɛkˈtrɪsɪti/", "hiện tượng quang điện"),
    ("076293", "photoelectronics", "noun", "/ˌfoʊtoʊɪlɛkˈtrɒnɪks/", "ngành quang điện tử học"),
    ("076294", "photoemissive", "adj", "/ˌfoʊtoʊɪˈmɪsɪv/", "có tính phát xạ quang điện"),
    ("076295", "photofinish", "noun", "/ˌfoʊtoʊˈfɪnɪʃ/", "ảnh phân thắng thua sát nút về đích"),
    ("076296", "photofit", "noun", "/ˈfoʊtoʊfɪt/", "ảnh ghép nhận dạng nghi phạm"),
    ("076297", "photoflash", "noun", "/ˈfoʊtoʊflæʃ/", "đèn chớp chụp ảnh (flash)"),
    ("076298", "photoflood", "noun", "/ˈfoʊtoʊflʌd/", "đèn rọi công suất lớn (nhiếp ảnh)"),
    ("076299", "photofluorographic", "adj", "/ˌfoʊtoʊˌflʊərəˈɡræfɪk/", "thuộc chụp X-quang huỳnh quang"),
    ("076300", "photogenically", "adv", "/ˌfoʊtəˈdʒɛnɪkli/", "lên ảnh đẹp, ăn ảnh"),
    ("076301", "photoglyph", "noun", "/ˈfoʊtəɡlɪf/", "bản khắc kẽm bằng ánh sáng"),
    ("076302", "photoglyphy", "noun", "/foʊˈtɒɡlɪfi/", "kỹ thuật khắc kẽm bằng ánh sáng"),
]

with open("scratch/b36_r03_raw_p3.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r03_p3.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r03_p3 saved OK")
