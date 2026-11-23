import json

items = [
    ("070403", "colonisers", "noun", "/ˈkɒləˌnaɪzərz/", "người thực dân; kẻ khai phá (Anh)"),
    ("070404", "confluxes", "noun", "/ˈkɒnflʌksɪz/", "dòng hợp lưu; đám đông tụ họp"),
    ("070405", "cornishmans", "noun", "/ˈkɔːrnɪʃmənz/", "người đàn ông vùng Cornwall (Anh)"),
    ("070406", "cotoneasters", "noun", "/kəˈtoʊniˌæstərz/", "cây bụi tuấn mai; cây quả táo gai"),
    ("070407", "cottiers", "noun", "/ˈkɒtiərz/", "nông dân tá điền thuê nhà đất nhỏ"),
    ("070408", "countertransferences", "noun", "/ˌkaʊntərˈtrænsfərənsɪz/", "sự chuyển di ngược (tâm lý học)"),
    ("070409", "cronyns", "noun", "/ˈkroʊnɪnz/", "diễn viên Hume Cronyn"),
    ("070410", "cullises", "noun", "/ˈkʌlɪsɪz/", "máng rãnh gỗ trượt; nước dùng lọc"),
    ("070411", "cumulations", "noun", "/ˌkjuːmjʊˈleɪʃənz/", "sự tích lũy chồng chất dần"),
    ("070412", "cytokinins", "noun", "/ˌsaɪtoʊˈkaɪnɪnz/", "hoóc-môn thực vật cytokinin"),
    ("070413", "demitasses", "noun", "/ˈdɛmɪˌtæsɪz/", "tách cà phê espresso cỡ nhỏ"),
    ("070414", "diastases", "noun", "/daɪˈæstəsiːz/", "men tiêu tinh bột; sự tách giãn cơ"),
    ("070415", "djinnis", "noun", "/dʒɪˈniːz/", "thần đèn hoặc tinh linh A-rập"),
    ("070416", "eisenstaedts", "noun", "/ˈaɪzənˌstɛts/", "nhiếp ảnh gia Alfred Eisenstaedt"),
    ("070417", "enbrels", "noun", "/ˈɛnbrɛlz/", "thuốc Enbrel trị viêm khớp"),
    ("070418", "ephemeralities", "noun", "/ɪˌfɛməˈrælɪtiz/", "tính phù du ngắn ngủi thoáng qua"),
    ("070419", "equilibrated", "verb", "/ɪˈkwɪlɪˌbreɪtɪd/", "đã đưa về trạng thái cân bằng"),
    ("070420", "equilibrates", "verb", "/ɪˈkwɪlɪˌbreɪts/", "cân bằng; giữ ở thế cân bằng"),
    ("070421", "equilibrating", "verb", "/ɪˈkwɪlɪˌbreɪtɪŋ/", "đang đưa về trạng thái cân bằng"),
    ("070422", "esotericas", "noun", "/ˌɛsəˈtɛrɪkəz/", "kiến thức bí truyền khó hiểu"),
    ("070423", "europeanizations", "noun", "/ˌjʊərəpiənaɪˈzeɪʃənz/", "quá trình Âu hóa theo văn hóa Âu"),
    ("070424", "feminisations", "noun", "/ˌfɛmɪnaɪˈzeɪʃənz/", "sự nữ tính hóa (cách viết Anh)"),
    ("070425", "fibreboards", "noun", "/ˈfaɪbərˌbɔːrdz/", "tấm ván gỗ ép công nghiệp (Anh)"),
    ("070426", "forewomen", "noun", "/ˈfɔːrˌwɪmɪn/", "nữ quản đốc; nữ trưởng bồi thẩm"),
    ("070427", "fugards", "noun", "/ˈfjuːɡɑːrdz/", "nhà soạn kịch Athol Fugard"),
    ("070428", "fungibilities", "noun", "/ˌfʌndʒəˈbɪlɪtiz/", "tính có thể thay thế ngang giá"),
    ("070429", "glanderses", "noun", "/ˈɡlændərzɪz/", "bệnh tị thư truyền nhiễm ở ngựa"),
    ("070430", "gourdes", "noun", "/ɡʊərdz/", "đồng tiền gourde của Haiti"),
    ("070431", "groundballs", "noun", "/ˈɡraʊndˌbɔːlz/", "bóng đánh lăn sệt (bóng chày)"),
    ("070432", "guarnieris", "noun", "/ɡwɑːrˈnjɛəriz/", "đàn vĩ cầm cổ Guarneri nổi tiếng"),
    ("070433", "habaneras", "noun", "/ˌhɑːbəˈnɛərəz/", "điệu nhảy và nhạc habanera Cuba"),
    ("070434", "haematites", "noun", "/ˈhiːməˌtaɪts/", "quặng sắt hematit đỏ nâu (Anh)"),
    ("070435", "helichrysa", "noun", "/ˌhɛlɪˈkraɪzə/", "chi Cúc bất tử (Helichrysum)"),
    ("070436", "holleriths", "noun", "/ˈhɒlərɪθs/", "hệ thống thẻ đục lỗ Hollerith"),
    ("070437", "hopers", "noun", "/ˈhoʊpərz/", "người ôm niềm hy vọng"),
    ("070438", "illuminants", "noun", "/ɪˈluːmɪnənts/", "nguồn phát sáng; chất thắp sáng"),
    ("070439", "inhomogeneities", "noun", "/ɪnˌhoʊmoʊdʒəˈniːɪtiz/", "tính không đồng nhất không đều"),
    ("070440", "katars", "noun", "/kəˈtɑːrz/", "dao găm đẩy tay katar Ấn Độ; Qatar"),
    ("070441", "kazakstans", "noun", "/ˌkæzækˈstænz/", "nước Kazakhstan (cách viết cũ)"),
    ("070442", "kilovolts", "noun", "/ˈkɪləˌvoʊlts/", "đơn vị điện áp kilôvôn (1000 V)"),
    ("070443", "kinyarwandas", "noun", "/ˌkɪnjɑːrˈwɑːndəz/", "tiếng Kinyarwanda của người Rwanda"),
    ("070444", "lacertas", "noun", "/ləˈsɜːrtəz/", "chi Thằn lằn thực Lacerta"),
    ("070445", "lahus", "noun", "/ˈlɑːhuːz/", "dân tộc và tiếng Lahu (Đông Nam Á)"),
    ("070446", "laseks", "noun", "/ˈleɪsɛks/", "phẫu thuật mắt bằng laser LASEK"),
    ("070447", "lensmans", "noun", "/ˈlɛnzmənz/", "nhiếp ảnh gia; thợ quay phim"),
    ("070448", "lorikeets", "noun", "/ˈlɔːrɪˌkiːts/", "vẹt mật cầu vồng lorikeet nhỏ"),
    ("070449", "mainers", "noun", "/ˈmeɪnərz/", "người dân bang Maine của Mỹ"),
    ("070450", "maleates", "noun", "/ˈmæliˌeɪts/", "muối hoặc este của axit maleic"),
    ("070451", "maracays", "noun", "/ˌmærəˈkaɪz/", "thành phố Maracay ở Venezuela"),
    ("070452", "marlinspikes", "noun", "/ˈmɑːrlɪnˌspaɪks/", "dùi nhọn tách tao dây thừng tàu"),
    ("070453", "metalworkses", "noun", "/ˈmɛtəlˌwɜːrksɪz/", "xưởng cơ khí kim loại; đồ kim khí"),
    ("070454", "miniums", "noun", "/ˈmɪniəmz/", "bột màu đỏ son oxit chì minium"),
    ("070455", "neopolitans", "noun", "/ˌniːəˈpɒlɪtənz/", "người Napoli; kem ba vị Neapolitan"),
    ("070456", "nervis", "noun", "/ˈnɜːrviz/", "bộ tộc Nervi cổ; dây thần kinh"),
    ("070457", "nitres", "noun", "/ˈnaɪtərz/", "muối diêm tiêu kali nitrat (Anh)"),
    ("070458", "numerated", "verb", "/ˈnjuːməˌreɪtɪd/", "đã đếm số; đã tính toán đếm"),
    ("070459", "numerates", "verb", "/ˈnjuːməˌreɪts/", "đếm số lượng; đọc tên con số"),
    ("070460", "numerating", "verb", "/ˈnjuːməˌreɪtɪŋ/", "đang đếm số lượng; đang liệt kê"),
    ("070461", "nutations", "noun", "/njuːˈteɪʃənz/", "chương động trục; sự uốn ngọn cây"),
    ("070462", "nutriments", "noun", "/ˈnjuːtrɪmənts/", "chất dinh dưỡng nuôi sống cơ thể"),
    ("070463", "ophthalmoscopes", "noun", "/ɒfˈθælməˌskoʊps/", "kính soi đáy mắt chuyên khoa"),
    ("070464", "overactivities", "noun", "/ˌoʊvərækˈtɪvɪtiz/", "tình trạng hoạt động thái quá"),
    ("070465", "overspreading", "verb", "/ˌoʊvərˈsprɛdɪŋ/", "đang phủ trùm lên khắp bề mặt"),
    ("070466", "overspreads", "verb", "/ˌoʊvərˈsprɛdz/", "phủ trùm lên lan rộng khắp nơi"),
    ("070467", "pasteurisations", "noun", "/ˌpæstʃəraɪˈzeɪʃənz/", "sự thanh trùng Pasteur (Anh)"),
    ("070468", "pentangles", "noun", "/ˈpɛnˌtæŋɡəlz/", "biểu tượng ngôi sao năm cánh"),
    ("070469", "pilseners", "noun", "/ˈpɪlzənərz/", "bia vàng tươi kiểu Pilsen (Séc)"),
    ("070470", "plugholes", "noun", "/ˈplʌɡˌhoʊlz/", "lỗ thoát nước bồn rửa có nút đậy"),
    ("070471", "premies", "noun", "/ˈpriːmiz/", "trẻ sinh non thiếu tháng (Mỹ)"),
    ("070472", "psychometries", "noun", "/saɪˈkɒmɪtriz/", "khoa học trắc nghiệm tâm lý"),
    ("070473", "pterygiums", "noun", "/təˈrɪdʒiəmz/", "bệnh mộng thịt ở mắt"),
    ("070474", "pulsatillas", "noun", "/ˌpʌlsəˈtɪləz/", "cây bạch đầu ông hoa tím"),
    ("070475", "rattails", "noun", "/ˈrætˌteɪlz/", "cá đuôi chuột biển sâu; dũa tròn"),
    ("070476", "redpolls", "noun", "/ˈrɛdˌpoʊlz/", "chim sẻ trán đỏ phương bắc"),
    ("070477", "resids", "noun", "/ˈrɛzɪdz/", "cặn dầu nặng sau chưng cất"),
    ("070478", "resolvents", "noun", "/rɪˈzɒlvənts/", "thuốc tiêu sưng; đa thức giải"),
    ("070479", "roues", "noun", "/ruːˈeɪz/", "kẻ ăn chơi trác táng phóng đãng"),
    ("070480", "roumanias", "noun", "/ruːˈmeɪniəz/", "nước Ru-ma-ni (cách viết cũ)"),
    ("070481", "sauries", "noun", "/ˈsɔːriz/", "cá thu đao (cá đao Nhật Bản)"),
    ("070482", "scofflaws", "noun", "/ˈskɒfˌlɔːz/", "kẻ xem thường trốn tránh pháp luật"),
    ("070483", "sexualised", "verb", "/ˈsɛkʃuəˌlaɪzd/", "đã tình dục hóa; đã gợi dục (Anh)"),
    ("070484", "sexualises", "verb", "/ˈsɛkʃuəˌlaɪzɪz/", "tình dục hóa (cách viết Anh)"),
    ("070485", "sexualising", "verb", "/ˈsɛkʃuəˌlaɪzɪŋ/", "đang tình dục hóa (cách viết Anh)"),
    ("070486", "sidesaddles", "noun", "/ˈsaɪdˌsædəlz/", "yên ngựa nữ ngồi một bên"),
    ("070487", "skinflints", "noun", "/ˈskɪnˌflɪnts/", "kẻ bủn xỉn keo kiệt vắt cổ chày"),
    ("070488", "smoothening", "verb", "/ˈsmuːðənɪŋ/", "đang làm trơn láng mịn hơn"),
    ("070489", "smoothens", "verb", "/ˈsmuːðənz/", "làm nhẵn mịn màng trơn tru"),
    ("070490", "spelters", "noun", "/ˈspɛltərz/", "hợp kim kẽm thô chưa tinh luyện"),
    ("070491", "striations", "noun", "/straɪˈeɪʃənz/", "đường sọc vân song song mảnh"),
    ("070492", "stumpers", "noun", "/ˈstʌmpərz/", "câu hỏi hóc búa làm bí; người bắt"),
    ("070493", "tabuks", "noun", "/təˈbʊks/", "thành phố Tabuk ở Ả Rập Xê Út"),
    ("070494", "thespises", "noun", "/ˈθɛspɪsɪz/", "thi sĩ bi kịch Hy Lạp Thespis"),
    ("070495", "threaders", "noun", "/ˈθrɛdərz/", "dụng cụ xâu chỉ qua lỗ kim"),
    ("070496", "timecards", "noun", "/ˈtaɪmˌkɑːrdz/", "thẻ bấm giờ chấm công nhân viên"),
    ("070497", "tisanes", "noun", "/tɪˈzænz/", "trà thảo mộc ngâm không lá trà"),
    ("070498", "topmasts", "noun", "/ˈtɒpˌmæsts/", "đoạn cột buồm tầng trên cùng"),
    ("070499", "towhees", "noun", "/ˈtoʊhiːz/", "chim sẻ đất towhee Bắc Mỹ"),
    ("070500", "tremblers", "noun", "/ˈtrɛmblərz/", "người run sợ; chim run Antilles"),
    ("070501", "triangulums", "noun", "/traɪˈæŋɡjʊləmz/", "chòm sao Tam Giác trên bầu trời"),
    ("070502", "tricornes", "noun", "/ˈtraɪˌkɔːrnz/", "mũ ba góc cổ điển thế kỷ 18"),
]

with open("scratch/b35_r01_raw_p5.json") as f:
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

with open("scratch/b35_r01_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r01_p5.json OK")
