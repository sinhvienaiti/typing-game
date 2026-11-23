import json

items = [
    ("070303", "germanisms", "noun", "/ˈdʒɜːrməˌnɪzəmz/", "từ ngữ gốc Đức; nét đặc trưng Đức"),
    ("070304", "gossypiums", "noun", "/ɡɒˈsɪpiəmz/", "cây bông vải thuộc chi Gossypium"),
    ("070305", "greybeards", "noun", "/ˈɡreɪˌbɪərdz/", "cụ ông râu bạc; bình gốm có râu"),
    ("070306", "hamates", "noun", "/ˈhæmeɪts/", "xương móc ở cổ tay"),
    ("070307", "hinayanas", "noun", "/ˌhiːnəˈjɑːnəz/", "Phật giáo Tiểu thừa (nguyên thủy)"),
    ("070308", "hydrolysates", "noun", "/haɪˈdrɒlɪˌseɪts/", "sản phẩm thu được sau thủy phân"),
    ("070309", "hydroxyprolines", "noun", "/haɪˌdrɒksiˈproʊliːnz/", "axit amin hydroxyproline"),
    ("070310", "hygeias", "noun", "/haɪˈdʒiːəz/", "nữ thần sức khỏe Hygeia Hy Lạp"),
    ("070311", "initialisations", "noun", "/ɪˌnɪʃəlaɪˈzeɪʃənz/", "sự khởi tạo giá trị ban đầu (Anh)"),
    ("070312", "jagannathas", "noun", "/ˌdʒʌɡəˈnɑːtəz/", "thần Jagannatha Ấn Độ giáo"),
    ("070313", "jerboas", "noun", "/dʒɜːrˈboʊəz/", "chuột nhảy chân dài vùng sa mạc"),
    ("070314", "kanchenjungas", "noun", "/ˌkɑːntʃənˈdʒʌŋɡəz/", "núi Kanchenjunga dãy Himalaya"),
    ("070315", "knowingnesses", "noun", "/ˈnoʊɪŋnəsɪz/", "vẻ am hiểu tinh tường; sự láu lỉnh"),
    ("070316", "kopjes", "noun", "/ˈkɒpiz/", "đồi đá nhô lẻ loi (Nam Phi)"),
    ("070317", "loyangs", "noun", "/ˈlɔɪˌæŋz/", "thành phố cổ Lạc Dương Trung Quốc"),
    ("070318", "maidus", "noun", "/ˈmaɪduːz/", "bộ tộc Maidu bản địa California"),
    ("070319", "makalus", "noun", "/ˈmɑːkəˌluːz/", "đỉnh núi Makalu dãy Himalaya"),
    ("070320", "malangas", "noun", "/məˈlæŋɡəz/", "cây hoặc củ khoai sáp (môn)"),
    ("070321", "mantlepieces", "noun", "/ˈmæntəlˌpiːsɪz/", "bệ mặt kệ phía trên lò sưởi"),
    ("070322", "mauroises", "noun", "/moʊˈrwɑːz/", "nhà văn Pháp André Maurois"),
    ("070323", "milliards", "noun", "/ˈmɪljərdz/", "số một tỷ (10^9, kiểu Anh/Pháp)"),
    ("070324", "molises", "noun", "/moʊˈliːzeɪz/", "vùng Molise ở miền nam nước Ý"),
    ("070325", "molluscums", "noun", "/məˈlʌskəmz/", "u mềm lây da (nhiễm vi-rút)"),
    ("070326", "monocots", "noun", "/ˈmɒnəˌkɒts/", "thực vật một lá mầm"),
    ("070327", "morulae", "noun", "/ˈmɔːrjʊˌliː/", "phôi dâu (giai đoạn phân cắt)"),
    ("070328", "morulas", "noun", "/ˈmɔːrjʊləz/", "phôi dâu (giai đoạn phân cắt)"),
    ("070329", "nacimientos", "noun", "/ˌnɑːsɪmiˈɛntoʊz/", "dãy núi Nacimiento ở New Mexico"),
    ("070330", "nickered", "verb", "/ˈnɪkərd/", "đã hí khe khẽ (ngựa)"),
    ("070331", "nickering", "verb", "/ˈnɪkərɪŋ/", "đang hí khe khẽ (ngựa)"),
    ("070332", "nickers", "noun", "/ˈnɪkərz/", "tiếng ngựa hí khe khẽ; đồng bảng"),
    ("070333", "oligodendrocytes", "noun", "/ˌɒlɪɡoʊˈdɛndrəˌsaɪts/", "tế bào thần kinh đệm ít nhánh"),
    ("070334", "overcomers", "noun", "/ˌoʊvərˈkʌmərz/", "người vượt qua nghịch cảnh"),
    ("070335", "overflew", "verb", "/ˌoʊvərˈfluː/", "đã bay vượt qua bên trên"),
    ("070336", "overflies", "verb", "/ˌoʊvərˈflaɪz/", "bay vượt qua phía bên trên"),
    ("070337", "overflying", "verb", "/ˌoʊvərˈflaɪɪŋ/", "đang bay vượt qua phía bên trên"),
    ("070338", "palaeoecologies", "noun", "/ˌpælioʊɪˈkɒlədʒiz/", "ngành cổ sinh thái học (Anh)"),
    ("070339", "parousias", "noun", "/ˌpærʊˈziːəz/", "sự tái lâm của Chúa Giê-su"),
    ("070340", "peckerwoods", "noun", "/ˈpɛkərˌwʊdz/", "chim gõ kiến; từ lóng chỉ dân nghèo"),
    ("070341", "pelotas", "noun", "/pəˈloʊtəz/", "môn bóng tường Basque pelota"),
    ("070342", "periodontists", "noun", "/ˌpɛriəˈdɒntɪsts/", "bác sĩ chuyên khoa nha chu"),
    ("070343", "pharmacogeneticses", "noun", "/ˌfɑːrməkoʊdʒəˈnɛtɪksɪz/", "ngành di truyền học dược lý"),
    ("070344", "phenelzines", "noun", "/fəˈnɛlziːnz/", "thuốc chống trầm cảm phenelzine"),
    ("070345", "pinfolds", "noun", "/ˈpɪnˌfoʊldz/", "chuồng nhốt gia súc đi lạc"),
    ("070346", "pirogues", "noun", "/pɪˈroʊɡz/", "thuyền độc mộc dài và hẹp"),
    ("070347", "planarians", "noun", "/pləˈnɛəriənz/", "sán lông nước ngọt (chi Dugesia)"),
    ("070348", "plasseys", "noun", "/ˈplæsiz/", "trận chiến Plassey năm 1757 Ấn Độ"),
    ("070349", "plodders", "noun", "/ˈplɒdərz/", "người làm việc chậm chạp kiên trì"),
    ("070350", "poriferas", "noun", "/pəˈrɪfərəz/", "ngành Thân lỗ (hải miên bọt biển)"),
    ("070351", "romanshes", "noun", "/roʊˈmɑːnʃɪz/", "tiếng Romansh ở Thụy Sĩ"),
    ("070352", "ropier", "adj", "/ˈroʊpiər/", "nhiều dây sợi hơn; kém hơn (Anh)"),
    ("070353", "ropiest", "adj", "/ˈroʊpiɪst/", "nhiều dây sợi nhất; kém nhất (Anh)"),
    ("070354", "samnites", "noun", "/ˈsæmnaɪts/", "người bộ tộc Samnite cổ đại ở Ý"),
    ("070355", "scnts", "noun", "/ˌɛs siː ɛn ˈtiːz/", "chuyển nhân tế bào soma (SCNT)"),
    ("070356", "snorers", "noun", "/ˈsnɔːrərz/", "người hay ngủ ngáy"),
    ("070357", "soursops", "noun", "/ˈsaʊərˌsɒps/", "quả mãng cầu xiêm (mãng cầu gai)"),
    ("070358", "soutines", "noun", "/suːˈtiːnz/", "họa sĩ biểu hiện Chaïm Soutine"),
    ("070359", "splodges", "noun", "/ˈsplɒdʒɪz/", "vết loang lổ nhòe; mảng bết"),
    ("070360", "staysails", "noun", "/ˈsteɪˌseɪlz/", "cánh buồm căng trên dây néo"),
    ("070361", "tangrams", "noun", "/ˈtæŋˌɡræmz/", "trò xếp hình bảy mảnh tangram"),
    ("070362", "taxonomists", "noun", "/tækˈsɒnəmɪsts/", "nhà phân loại học sinh vật"),
    ("070363", "teashops", "noun", "/ˈtiːˌʃɒps/", "quán trà bánh ngọt truyền thống"),
    ("070364", "thymols", "noun", "/ˈθaɪmɒlz/", "hợp chất sát khuẩn thymol cỏ xạ"),
    ("070365", "tierces", "noun", "/ˈtɪərsɪz/", "kinh giờ thứ ba; thế thủ thứ ba"),
    ("070366", "tonuses", "noun", "/ˈtoʊnəsɪz/", "trương lực cơ bắp bình thường"),
    ("070367", "topgallants", "noun", "/tɒpˈɡælənts/", "buồm tầng trên cột buồm thuyền"),
    ("070368", "triggermans", "noun", "/ˈtrɪɡərmənz/", "tay súng sát thủ; kẻ bóp cò"),
    ("070369", "unionisations", "noun", "/ˌjuːnjənaɪˈzeɪʃənz/", "sự thành lập công đoàn (Anh)"),
    ("070370", "vaduzes", "noun", "/vɑːˈduːtsɪz/", "thủ đô Vaduz của Liechtenstein"),
    ("070371", "vibraphonists", "noun", "/ˈvaɪbrəˌfoʊnɪsts/", "nghệ sĩ chơi đàn phiến vibraphone"),
    ("070372", "visitants", "noun", "/ˈvɪzɪtənts/", "khách viếng thăm; chim di trú ghé"),
    ("070373", "warehousemans", "noun", "/ˈwɛərˌhaʊsmənz/", "nhân viên quản lý kho hàng"),
    ("070374", "admen", "noun", "/ˈædmɛn/", "nhân viên làm ngành quảng cáo"),
    ("070375", "aenguses", "noun", "/ˈeɪŋɡəsɪz/", "thần Aengus (thần thoại Ireland)"),
    ("070376", "airdromes", "noun", "/ˈɛərˌdroʊmz/", "sân bay cỡ nhỏ (từ cũ Mỹ)"),
    ("070377", "anaglyphs", "noun", "/ˈænəˌɡlɪfs/", "ảnh nổi 3D hai màu; phù điêu chạm"),
    ("070378", "aneroids", "noun", "/ˈænəˌrɔɪdz/", "khí áp kế hộp kim loại không lỏng"),
    ("070379", "angularities", "noun", "/ˌæŋɡjʊˈlærɪtiz/", "tính góc cạnh; vẻ gầy guộc xương"),
    ("070380", "antidiuretics", "noun", "/ˌæntidaɪjʊˈrɛtɪks/", "thuốc hoặc hoóc-môn chống bài niệu"),
    ("070381", "antineutrinos", "noun", "/ˌæntinuːˈtriːnoʊz/", "hạt phản neutrino (vật lý hạt)"),
    ("070382", "appalls", "verb", "/əˈpɔːlz/", "làm kinh hãi; làm choáng váng"),
    ("070383", "areopagites", "noun", "/ˌæriˈɒpəˌɡaɪts/", "thẩm phán hội đồng Areopagus cổ"),
    ("070384", "ascuses", "noun", "/ˈæskəsɪz/", "túi bào tử của nấm ngành Túi"),
    ("070385", "aspidistras", "noun", "/ˌæspɪˈdɪstrəz/", "cây tỏi rừng (cây lá gang bền bỉ)"),
    ("070386", "asterisms", "noun", "/ˈæstəˌrɪzəmz/", "nhóm sao định hình; hiện tượng sao"),
    ("070387", "atomisers", "noun", "/ˈætəˌmaɪzərz/", "bình xịt phun sương (Anh)"),
    ("070388", "baldrs", "noun", "/ˈbɑːldərz/", "thần ánh sáng Baldr Bắc Âu"),
    ("070389", "barthelmes", "noun", "/bɑːrˈtɛlmiz/", "nhà văn Mỹ Donald Barthelme"),
    ("070390", "bollixed", "verb", "/ˈbɒlɪkst/", "đã làm rối tung hỏng bét (khẩu ngữ)"),
    ("070391", "bollixes", "verb", "/ˈbɒlɪksɪz/", "làm rối tung hỏng bét (khẩu ngữ)"),
    ("070392", "bollixing", "verb", "/ˈbɒlɪksɪŋ/", "đang làm rối tung hỏng bét"),
    ("070393", "cabalas", "noun", "/kəˈbɑːləz/", "học thuyết thần bí Kabbalah"),
    ("070394", "calomels", "noun", "/ˈkælənˌmɛlz/", "muối calomel (thủy ngân I clorua)"),
    ("070395", "centals", "noun", "/ˈsɛntəlz/", "đơn vị tạ Anh bằng 100 pound"),
    ("070396", "chapterhouses", "noun", "/ˈtʃæptərˌhaʊsɪz/", "phòng họp hội đồng giáo sĩ; nhà hội"),
    ("070397", "cheerleaded", "verb", "/ˈtʃɪərˌliːdɪd/", "đã cổ vũ đội hình hoạt náo viên"),
    ("070398", "cheerleading", "verb", "/ˈtʃɪərˌliːdɪŋ/", "đang cổ vũ hoạt náo viên"),
    ("070399", "cheerleads", "verb", "/ˈtʃɪərˌliːdz/", "dẫn cổ vũ đội hình hoạt náo viên"),
    ("070400", "chokeys", "noun", "/ˈtʃoʊkiz/", "nhà tù, buồng giam (lóng Anh cổ)"),
    ("070401", "chophouses", "noun", "/ˈtʃɒpˌhaʊsɪz/", "tiệm ăn chuyên sườn nướng bít tết"),
    ("070402", "churls", "noun", "/tʃɜːrlz/", "kẻ thô lỗ cộc cằn; nông dân tự do"),
]

with open("scratch/b35_r01_raw_p4.json") as f:
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

with open("scratch/b35_r01_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r01_p4.json OK")
