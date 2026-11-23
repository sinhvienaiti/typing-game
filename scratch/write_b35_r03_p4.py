import json

items = [
    ("071303", "maffias", "noun", "/ˈmɑːfiəz/", "băng đảng tội phạm ngầm Mafia"),
    ("071304", "malvaceaes", "noun", "/mælˈveɪʃiˌiːz/", "họ Bông cẩm quỳ (Malvaceae)"),
    ("071305", "marmotas", "noun", "/mɑːrˈmoʊtəz/", "chi Chuột marmot (sóc đất lớn)"),
    ("071306", "metalwares", "noun", "/ˈmɛtəlˌwɛərz/", "hàng hóa chế tác bằng kim loại"),
    ("071307", "metazoas", "noun", "/ˌmɛtəˈzoʊəz/", "nhóm Động vật đa bào Metazoa"),
    ("071308", "miconazoles", "noun", "/mɪˈkɒnəˌzoʊlz/", "thuốc kháng nấm miconazole"),
    ("071309", "morticed", "verb", "/ˈmɔːrtɪst/", "đã đục lỗ mộng ghép gỗ (Anh)"),
    ("071310", "mortices", "noun", "/ˈmɔːrtɪsɪz/", "lỗ mộng ghép gỗ (mộc, Anh)"),
    ("071311", "morticing", "verb", "/ˈmɔːrtɪsɪŋ/", "đang đục lỗ mộng ghép gỗ (Anh)"),
    ("071312", "mucors", "noun", "/ˈmjuːkɔːrz/", "nấm mốc trắng thuộc chi Mucor"),
    ("071313", "muscatels", "noun", "/ˌmʌskəˈtɛlz/", "rượu vang ngọt nho xạ muscatel"),
    ("071314", "nereides", "noun", "/nɪˈriːɪˌdiːz/", "nữ thần biển Nereid Hy Lạp cổ"),
    ("071315", "nereids", "noun", "/ˈnɪəriɪdz/", "nữ thần biển Nereid; giun nhiều tơ"),
    ("071316", "nevadans", "noun", "/nəˈvædənz/", "người dân bang Nevada của Mỹ"),
    ("071317", "omphaloses", "noun", "/ˈɒmfəlɒsɪz/", "điểm trung tâm rốn (Hy Lạp cổ)"),
    ("071318", "outstayed", "verb", "/ˌaʊtˈsteɪd/", "đã nán ở lại quá lâu quá hạn"),
    ("071319", "outstaying", "verb", "/ˌaʊtˈsteɪɪŋ/", "đang nán ở lại quá lâu quá hạn"),
    ("071320", "outstays", "verb", "/ˌaʊtˈsteɪz/", "nán ở lại quá lâu quá giờ"),
    ("071321", "parallelepipeds", "noun", "/ˌpærəlɛləˈpaɪpɛdz/", "hình hộp bình hành (toán học)"),
    ("071322", "parallelized", "verb", "/ˈpærəleˌlaɪzd/", "đã song song hóa; đặt song song"),
    ("071323", "parallelizes", "verb", "/ˈpærəleˌlaɪzɪz/", "song song hóa; đặt song song nhau"),
    ("071324", "parallelizing", "verb", "/ˈpærəleˌlaɪzɪŋ/", "đang song song hóa; đặt song song"),
    ("071325", "pardoners", "noun", "/ˈpɑːrdənərz/", "người ban phép xá tội trung cổ"),
    ("071326", "pentads", "noun", "/ˈpɛntædz/", "nhóm năm vật; chu kỳ năm ngày"),
    ("071327", "pluralized", "verb", "/ˈplʊərəˌlaɪzd/", "đã chuyển sang dạng số nhiều"),
    ("071328", "pluralizes", "verb", "/ˈplʊərəˌlaɪzɪz/", "chuyển số nhiều; đa nguyên hóa"),
    ("071329", "pluralizing", "verb", "/ˈplʊərəˌlaɪzɪŋ/", "đang chuyển số nhiều; đa nguyên hóa"),
    ("071330", "polydipsias", "noun", "/ˌpɒlɪˈdɪpsiəz/", "chứng khát nước nhiều bất thường"),
    ("071331", "polymyositises", "noun", "/ˌpɒlimaɪəˈsaɪtɪsɪz/", "bệnh viêm đa cơ tự miễn"),
    ("071332", "progressivities", "noun", "/ˌprɒɡrɛˈsɪvɪtiz/", "tính lũy tiến (thuế); tính tiến bộ"),
    ("071333", "radicles", "noun", "/ˈrædɪkəlz/", "rễ mầm phôi hạt thực vật"),
    ("071334", "reductants", "noun", "/rɪˈdʌktənts/", "chất khử cho electron (hóa học)"),
    ("071335", "rhizopuses", "noun", "/raɪˈzoʊpəsɪz/", "nấm mốc bánh mì chi Rhizopus"),
    ("071336", "rhizotomies", "noun", "/raɪˈzɒtəmiz/", "phẫu thuật cắt rễ thần kinh sống"),
    ("071337", "rhombs", "noun", "/rɒmz/", "hình thoi bốn cạnh bằng nhau"),
    ("071338", "rhythmicities", "noun", "/rɪðˈmɪsɪtiz/", "tính nhịp điệu chu kỳ đều đặn"),
    ("071339", "sackfuls", "noun", "/ˈsækˌfʊlz/", "lượng chứa đầy một bao tải"),
    ("071340", "sarracenias", "noun", "/ˌsærəˈsiːniəz/", "cây bình bắt mồi Bắc Mỹ"),
    ("071341", "satinwoods", "noun", "/ˈsætɪnˌwʊdz/", "gỗ sa-tanh bóng vân vàng quý"),
    ("071342", "scantlings", "noun", "/ˈskæntlɪŋz/", "xà gỗ xẻ tiết diện nhỏ; kích thước"),
    ("071343", "selaginellas", "noun", "/ˌsɛlədʒɪˈnɛləz/", "cây quyển bá (trường sinh thảo)"),
    ("071344", "sherds", "noun", "/ʃɜːrdz/", "mảnh gốm sứ vỡ khai quật khảo cổ"),
    ("071345", "silvertips", "noun", "/ˈsɪlvərˌtɪps/", "gấu xám lông ngả bạc Bắc Mỹ"),
    ("071346", "snowberries", "noun", "/ˈsnoʊˌbɛriz/", "cây bụi tuyết mai quả mọng trắng"),
    ("071347", "soubises", "noun", "/suːˈbiːzɪz/", "xốt hành tây bơ sữa soubise Pháp"),
    ("071348", "sparged", "verb", "/spɑːrdʒd/", "đã sục khí; đã tưới rưới nước nóng"),
    ("071349", "sparges", "noun", "/ˈspɑːrdʒɪz/", "sự sục khí; vữa trát sần (xây dựng)"),
    ("071350", "sparging", "verb", "/ˈspɑːrdʒɪŋ/", "đang sục khí; đang rưới nước ấm"),
    ("071351", "spatchcocked", "verb", "/ˈspætʃˌkɒkt/", "đã mổ phanh ép dẹp gia cầm nướng"),
    ("071352", "spatchcocking", "verb", "/ˈspætʃˌkɒkɪŋ/", "đang mổ phanh ép dẹp gia cầm nướng"),
    ("071353", "spatchcocks", "noun", "/ˈspætʃˌkɒks/", "gà vịt mổ phanh ép dẹp nướng nhanh"),
    ("071354", "sphygmomanometers", "noun", "/ˌsfɪɡmoʊməˈnɒmɪtərz/", "máy đo huyết áp băng quấn tay"),
    ("071355", "sportscasting", "verb", "/ˈspɔːrtsˌkæstɪŋ/", "đang bình luận tường thuật thể thao"),
    ("071356", "sportscasts", "noun", "/ˈspɔːrtsˌkæsts/", "chương trình phát thanh thể thao"),
    ("071357", "stemmers", "noun", "/ˈstɛmərz/", "người hoặc máy ngắt cuống trái cây"),
    ("071358", "substantialities", "noun", "/səbˌstænʃiˈælɪtiz/", "tính thực chất vững chắc có thật"),
    ("071359", "sucralfates", "noun", "/suːˈkrælfeɪts/", "thuốc bảo vệ dạ dày sucralfat"),
    ("071360", "sunhats", "noun", "/ˈsʌnˌhæts/", "mũ rộng vành che nắng"),
    ("071361", "suppliants", "noun", "/ˈsʌpliənts/", "người khẩn cầu nài xin khẩn thiết"),
    ("071362", "svizzeras", "noun", "/ˈsvɪtsərəz/", "nước Thụy Sĩ (tiếng Ý Svizzera)"),
    ("071363", "tailraces", "noun", "/ˈteɪlˌreɪsɪz/", "kênh xả nước sau tua-bin thủy điện"),
    ("071364", "terbinafines", "noun", "/tɜːrˈbɪnəfiːnz/", "thuốc kháng nấm da terbinafine"),
    ("071365", "ticals", "noun", "/tɪˈkɑːlz/", "đồng baht Thái Lan (tên cũ tical)"),
    ("071366", "transfixt", "verb", "/trænsˈfɪkst/", "đã đâm xuyên qua; làm chết lặng"),
    ("071367", "trochlears", "noun", "/ˈtrɒkliərz/", "dây thần kinh ròng rọc (sọ IV)"),
    ("071368", "tunguses", "noun", "/tʊŋˈɡuːzɪz/", "người dân tộc Tungus vùng Siberia"),
    ("071369", "unattractivenesses", "noun", "/ˌʌnəˈtræktɪvnəsɪz/", "sự kém hấp dẫn; vẻ thiếu lôi cuốn"),
    ("071370", "victimizers", "noun", "/ˈvɪktɪˌmaɪzərz/", "kẻ hãm hại áp bức nạn nhân"),
    ("071371", "waterbirds", "noun", "/ˈwɔːtərˌbɜːrdz/", "loài chim sống gần vùng nước"),
    ("071372", "weathercocks", "noun", "/ˈwɛðərˌkɒks/", "chong chóng chỉ gió; kẻ hay đổi"),
    ("071373", "zoonoses", "noun", "/ˌzoʊəˈnoʊsiːz/", "bệnh truyền từ động vật sang người"),
    ("071374", "adjustors", "noun", "/əˈdʒʌstərz/", "thẩm định viên bảo hiểm; bộ chỉnh"),
    ("071375", "adulterants", "noun", "/əˈdʌltərənts/", "chất pha tạp làm giảm chất lượng"),
    ("071376", "agglutinins", "noun", "/əˈɡluːtɪnɪnz/", "kháng thể gây ngưng kết hồng cầu"),
    ("071377", "algonkians", "noun", "/ælˈɡɒŋkiənz/", "người bản địa Algonquian Bắc Mỹ"),
    ("071378", "allophones", "noun", "/ˈæləˌfoʊnz/", "tha âm vị biến thể phát âm"),
    ("071379", "alulae", "noun", "/ˈæljʊˌliː/", "lông cánh phụ chim; thùy cánh bọ"),
    ("071380", "alulas", "noun", "/ˈæljʊləz/", "lông cánh phụ chim; thùy cánh bọ"),
    ("071381", "andropogons", "noun", "/ænˈdrɒpəˌɡɒnz/", "cỏ rậm thân cao chi Andropogon"),
    ("071382", "annons", "noun", "/ˈænənz/", "quả na; cây thuộc họ Na (Annona)"),
    ("071383", "antiquarks", "noun", "/ˈæntiˌkwɑːrks/", "hạt phản quark (vật lý hạt)"),
    ("071384", "arguers", "noun", "/ˈɑːrɡjuːərz/", "người tranh luận biện bác"),
    ("071385", "asterions", "noun", "/əˈstɪəriɒnz/", "điểm khớp sọ asterion sau tai"),
    ("071386", "aztecans", "noun", "/ˈæztɛkənz/", "nhóm ngôn ngữ và người Aztec"),
    ("071387", "bedframes", "noun", "/ˈbɛdˌfreɪmz/", "khung đỡ nệm giường ngủ"),
    ("071388", "bioscopes", "noun", "/ˈbaɪəˌskoʊps/", "máy chiếu phim đời đầu; rạp phim"),
    ("071389", "blebs", "noun", "/blɛbz/", "bóng khí phổi hoặc mụn phồng rộp"),
    ("071390", "bodensees", "noun", "/ˈboʊdənˌzeɪz/", "hồ Constance (Bodensee Đức-Thụy Sĩ)"),
    ("071391", "bottlebrushes", "noun", "/ˈbɒtəlˌbrʌʃɪz/", "cọ rửa chai; cây hoa tràm liễu"),
    ("071392", "briquets", "noun", "/brɪˈkɛts/", "viên than ép; thỏi kim loại ép"),
    ("071393", "cannoneers", "noun", "/ˌkænəˈnɪərz/", "pháo thủ điều khiển súng đại bác"),
    ("071394", "catechus", "noun", "/ˈkætɪˌtʃuːz/", "cao nhựa chiết cây keo cau catechu"),
    ("071395", "celtises", "noun", "/ˈsɛltɪsɪz/", "cây cơm nguội thuộc chi Celtis"),
    ("071396", "centavos", "noun", "/sɛnˈtɑːvoʊz/", "đồng xu centavo (Mỹ Latinh)"),
    ("071397", "chinches", "noun", "/ˈtʃɪntʃɪz/", "rệp giường hoặc bọ xít hút nhựa"),
    ("071398", "chloroprenes", "noun", "/ˈklɔːrəˌpriːnz/", "monome cloropren sản xuất cao su"),
    ("071399", "coccidioses", "noun", "/kɒkˌsɪdiˈoʊsiːz/", "bệnh cầu trùng ở gia súc gia cầm"),
    ("071400", "cockspurs", "noun", "/ˈkɒkˌspɜːrz/", "cựa gà trống; cỏ lồng vực chân gà"),
    ("071401", "crampons", "noun", "/ˈkræmpɒnz/", "đế đinh sắt kẹp giày leo băng núi"),
    ("071402", "danseuses", "noun", "/dɑːnˈsɜːrzɪz/", "nữ vũ công múa ba lê chuyên nghiệp"),
]

with open("scratch/b35_r03_raw_p4.json") as f:
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

with open("scratch/b35_r03_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r03_p4.json OK")
