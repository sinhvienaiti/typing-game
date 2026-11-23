import json

rows = [
    ("077203", "pledget", "noun", "/ˈplɛdʒɪt/", "miếng gạc nhỏ thấm thuốc (y tế)"),
    ("077204", "pledging", "verb", "/ˈplɛdʒɪŋ/", "cam kết, thề hứa; thế chấp, cầm cố"),
    ("077205", "pleiad", "noun", "/ˈpliːəd/", "nhóm Thất tinh; hội tao đàn 7 người"),
    ("077206", "pleinairist", "noun", "/ˌplɛnˈɛrɪst/", "họa sĩ trường phái vẽ ngoài trời"),
    ("077207", "pleioblastic", "adj", "/ˌplaɪoʊˈblæstɪk/", "có nhiều mầm phôi; nhiều chồi"),
    ("077208", "pleiochasim", "noun", "/ˌplaɪoʊˈkeɪʒəm/", "cụm hoa xim nhiều ngả (thực vật)"),
    ("077209", "pleiocotyl", "noun", "/ˌplaɪoʊˈkɒtɪl/", "cây có nhiều hơn hai lá mầm"),
    ("077210", "pleiocotyledonary", "adj", "/ˌplaɪoʊˌkɒtɪˈliːdənəri/", "có nhiều lá mầm (thực vật học)"),
    ("077211", "pleiocotyledony", "noun", "/ˌplaɪoʊˌkɒtɪˈliːdəni/", "tính trạng có nhiều lá mầm"),
    ("077212", "pleiocyclic", "adj", "/ˌplaɪoʊˈsaɪklɪk/", "sống nhiều chu kỳ, nhiều vụ mùa"),
    ("077213", "pleiomerous", "adj", "/plaɪˈɒmərəs/", "có số lượng bộ phận vượt chuẩn"),
    ("077214", "pleiomery", "noun", "/plaɪˈɒməri/", "tính tăng số bộ phận (thực vật)"),
    ("077215", "pleiomorphic", "adj", "/ˌplaɪoʊˈmɔːrfɪk/", "đa hình thái (tinh thể, sinh học)"),
    ("077216", "pleiomorphism", "noun", "/ˌplaɪoʊˈmɔːrfɪzəm/", "hiện tượng đa hình thái"),
    ("077217", "pleiomorphous", "adj", "/ˌplaɪoʊˈmɔːrfəs/", "đa hình thái (tinh thể, sinh học)"),
    ("077218", "pleione", "noun", "/plaɪˈoʊni/", "chi hoa lan Pleione (châu Á)"),
    ("077219", "pleiopetalous", "adj", "/ˌplaɪoʊˈpɛtələs/", "có nhiều cánh hoa (hoa kép)"),
    ("077220", "pleiophyllous", "adj", "/ˌplaɪoʊˈfɪləs/", "có nhiều lá trong một vòng đốt"),
    ("077221", "pleiospilos", "noun", "/ˌplaɪoʊˈspiːlɒs/", "chi cây xương rồng đá Pleiospilos"),
    ("077222", "pleiosporous", "adj", "/ˌplaɪoʊˈspɔːrəs/", "có nhiều bào tử (nấm học)"),
    ("077223", "pleiotaxis", "noun", "/ˌplaɪoʊˈtæksɪs/", "tính tăng số vòng hoa (thực vật)"),
    ("077224", "pleiotaxy", "noun", "/ˈplaɪoʊtæksi/", "tính tăng số vòng hoa (thực vật)"),
    ("077225", "pleiotropic", "adj", "/ˌplaɪəˈtrɒpɪk/", "đa hiệu (một gen nhiều tính trạng)"),
    ("077226", "pleiotropism", "noun", "/plaɪˈɒtrəpɪzəm/", "tính đa hiệu của gen (di truyền)"),
    ("077227", "pleiotropy", "noun", "/plaɪˈɒtrəpi/", "tính đa hiệu của gen (di truyền)"),
    ("077228", "pleistoseist", "noun", "/ˈplaɪstəsaɪst/", "vùng tâm chấn động đất mạnh nhất"),
    ("077229", "plenarily", "adv", "/ˈpliːnərəli/", "một cách đầy đủ, toàn diện"),
    ("077230", "plenariness", "noun", "/ˈpliːnərinəs/", "tính đầy đủ, toàn quyền, trọn vẹn"),
    ("077231", "plenilunar", "adj", "/ˌplɛnɪˈluːnər/", "thuộc kỳ trăng tròn"),
    ("077232", "plenilunary", "adj", "/ˌplɛnɪˈluːnəri/", "thuộc kỳ trăng tròn"),
    ("077233", "plenilune", "noun", "/ˈplɛnɪluːn/", "lúc trăng tròn (văn chương)"),
    ("077234", "plenish", "verb", "/ˈplɛnɪʃ/", "trang bị đầy đủ; thả gia súc nuôi"),
    ("077235", "plenism", "noun", "/ˈpliːnɪzəm/", "thuyết vũ trụ tràn đầy vật chất"),
    ("077236", "plenitudinous", "adj", "/ˌplɛnɪˈtjuːdɪnəs/", "tràn đầy, sung mãn, dồi dào"),
    ("077237", "plenteously", "adv", "/ˈplɛntiəsli/", "dồi dào, sung túc, phong phú"),
    ("077238", "plenteousness", "noun", "/ˈplɛntiəsnəs/", "sự dồi dào, sung túc, phong phú"),
    ("077239", "plentifulness", "noun", "/ˈplɛntɪfəlnəs/", "sự dồi dào, phong phú, dạt dào"),
    ("077240", "pleochroic", "adj", "/ˌpliːəˈkroʊɪk/", "có tính đa sắc (tinh thể học)"),
    ("077241", "pleochromatic", "adj", "/ˌpliːoʊkroʊˈmætɪk/", "có tính đa sắc (tinh thể học)"),
    ("077242", "pleochromatism", "noun", "/ˌpliːəˈkroʊmətɪzəm/", "tính đa sắc (quang học tinh thể)"),
    ("077243", "pleogamic", "adj", "/ˌpliːəˈɡæmɪk/", "thụ phấn nhiều đợt khác thời điểm"),
    ("077244", "pleogamy", "noun", "/pliˈɒɡəmi/", "hiện tượng thụ phấn nhiều đợt"),
    ("077245", "pleomastia", "noun", "/ˌpliːoʊˈmæstiə/", "dị tật thừa tuyến vú (y học)"),
    ("077246", "pleometrotic", "adj", "/ˌpliːoʊmɪˈtrɒtɪk/", "tạo đàn ong kiến có nhiều chúa"),
    ("077247", "pleon", "noun", "/ˈpliːɒn/", "phần bụng của loài giáp xác"),
    ("077248", "pleonaste", "noun", "/ˈpliːənæst/", "khoáng vật spinel đen (pleonast)"),
    ("077249", "pleonastically", "adv", "/ˌpliːəˈnæstɪkli/", "dùng từ thừa trùng lặp (tu từ)"),
    ("077250", "pleophagous", "adj", "/pliˈɒfəɡəs/", "ăn đa thực (ăn nhiều loài cây)"),
    ("077251", "pleophyletic", "adj", "/ˌpliːoʊfaɪˈlɛtɪk/", "đa nguồn gốc (tiến hóa)"),
    ("077252", "pleopod", "noun", "/ˈpliːəpɒd/", "chân bơi vùng bụng (giáp xác)"),
    ("077253", "pleotrophic", "adj", "/ˌpliːəˈtrɒfɪk/", "ăn nhiều loại thức ăn (sinh thái)"),
    ("077254", "pleotrophy", "noun", "/pliˈɒtrəfi/", "tập tính ăn tạp nhiều loại thức ăn"),
    ("077255", "plerocercoid", "noun", "/ˌplɪroʊˈsɜːrkɔɪd/", "ấu trùng sán dây plerocercoid"),
    ("077256", "plerocestoid", "noun", "/ˌplɪroʊˈsɛstɔɪd/", "ấu trùng sán dây plerocercoid"),
    ("077257", "plerome", "noun", "/ˈplɪroʊm/", "trụ giữa mô phân sinh ngọn (cây)"),
    ("077258", "plerotic", "adj", "/plɪˈrɒtɪk/", "lấp đầy, mang ý nghĩa hoàn chỉnh"),
    ("077259", "plesianthropus", "noun", "/ˌpliːziˈænθrəpəs/", "người vượn hóa thạch Plesianthropus"),
    ("077260", "plesiobiosis", "noun", "/ˌpliːzioʊbaɪˈoʊsɪs/", "sự cộng cư không phụ thuộc (kiến)"),
    ("077261", "plesiobiotic", "adj", "/ˌpliːzioʊbaɪˈɒtɪk/", "cộng cư gần nhau (hai loài kiến)"),
    ("077262", "plesiomorphous", "adj", "/ˌpliːzioʊˈmɔːrfəs/", "mang tính trạng tổ tiên (tiến hóa)"),
    ("077263", "plesiops", "noun", "/ˈpliːziɒps/", "chi cá rạn san hô Plesiops"),
    ("077264", "plesiosauri", "noun", "/ˌpliːziəˈsɔːraɪ/", "thằn lằn cổ rắn biển (Plesiosaur)"),
    ("077265", "plesiosauria", "noun", "/ˌpliːziəˈsɔːriə/", "bộ Thằn lằn cổ rắn (Plesiosauria)"),
    ("077266", "plesiotype", "noun", "/ˈpliːziətaɪp/", "mẫu chuẩn phụ bổ sung (phân loại)"),
    ("077267", "plessimeter", "noun", "/plɛˈsɪmɪtər/", "tấm gõ chẩn đoán (y học)"),
    ("077268", "plessor", "noun", "/ˈplɛsər/", "búa gõ khám phản xạ (y học)"),
    ("077269", "plethodont", "noun", "/ˈplɛθədɒnt/", "kỳ giông không phổi (Plethodont)"),
    ("077270", "plethodontidae", "noun", "/ˌplɛθəˈdɒntɪdiː/", "họ Kỳ giông không phổi"),
    ("077271", "plethorically", "adv", "/pləˈθɒrɪkli/", "quá thừa thãi, dư dật quá mức"),
    ("077272", "plethysmogram", "noun", "/pləˈθɪzməɡræm/", "biểu đồ biến thiên thể tích (y học)"),
    ("077273", "pleurae", "noun", "/ˈplʊriː/", "màng phổi (giải phẫu)"),
    ("077274", "pleuralgia", "noun", "/plʊˈrældʒə/", "đau màng phổi; đau cơ liên sườn"),
    ("077275", "pleuralia", "noun", "/plʊˈreɪliə/", "bộ gai bảo vệ quanh miệng bọt biển"),
    ("077276", "pleuranthous", "adj", "/plʊˈrænθəs/", "có hoa mọc từ nách lá bên (cành)"),
    ("077277", "pleuric", "adj", "/ˈplʊrɪk/", "thuộc màng phổi"),
    ("077278", "pleurite", "noun", "/ˈplʊraɪt/", "mảnh giáp bên (đốt thân chân khớp)"),
    ("077279", "pleuritic", "adj", "/plʊˈrɪtɪk/", "thuộc hoặc mắc bệnh viêm màng phổi"),
    ("077280", "pleuroblastic", "adj", "/ˌplʊroʊˈblæstɪk/", "có chồi mọc bên (nấm, thực vật)"),
    ("077281", "pleurobrachia", "noun", "/ˌplʊroʊˈbrækiə/", "chi sứa lược biển (Pleurobrachia)"),
    ("077282", "pleurobrachiidae", "noun", "/ˌplʊroʊbrəˈkaɪɪdiː/", "họ Sứa lược Pleurobrachiidae"),
    ("077283", "pleurobranchiae", "noun", "/ˌplʊroʊˈbræŋkiːiː/", "mang gắn bên thành thân (giáp xác)"),
    ("077284", "pleurocarp", "noun", "/ˈplʊrəkɑːrp/", "rêu mọc bò có túi bào tử bên"),
    ("077285", "pleurocarpic", "adj", "/ˌplʊrəˈkɑːrpɪk/", "thuộc rêu có túi bào tử mọc bên"),
    ("077286", "pleurocarpous", "adj", "/ˌplʊrəˈkɑːrpəs/", "có túi bào tử mọc ở nhánh bên"),
    ("077287", "pleuroccipital", "adj", "/ˌplʊrɒkˈsɪpɪtəl/", "xương bên chẩm (giải phẫu sọ)"),
    ("077288", "pleurocentesis", "noun", "/ˌplʊroʊsɛnˈtiːsɪs/", "thủ thuật chọc dò màng phổi"),
    ("077289", "pleurocerebral", "adj", "/ˌplʊroʊsəˈriːbrəl/", "thuộc hạch não bên (nhuyễn thể)"),
    ("077290", "pleurodont", "noun", "/ˈplʊrədɒnt/", "răng bám mặt trong hàm (bò sát)"),
    ("077291", "pleurodynia", "noun", "/ˌplʊroʊˈdɪniə/", "đau cơ liên sườn cấp (y học)"),
    ("077292", "pleurolith", "noun", "/ˈplʊrəlɪθ/", "sỏi màng phổi (y học)"),
    ("077293", "pleuronectes", "noun", "/ˌplʊrəˈnɛktiːz/", "chi cá bơn sao (Pleuronectes)"),
    ("077294", "pleuronectidae", "noun", "/ˌplʊrəˈnɛktɪdiː/", "họ Cá bơn mắt phải (Pleuronectes)"),
    ("077295", "pleurosorus", "noun", "/ˌplʊroʊˈsɔːrəs/", "chi dương xỉ Pleurosorus"),
    ("077296", "pleurothallis", "noun", "/ˌplʊroʊˈθælɪs/", "chi phong lan nhỏ Pleurothallis"),
    ("077297", "pleuston", "noun", "/ˈpluːstɒn/", "sinh vật nổi mặt nước (pleuston)"),
    ("077298", "plexal", "adj", "/ˈplɛksəl/", "thuộc đám rối thần kinh, mạch máu"),
    ("077299", "plexiform", "adj", "/ˈplɛksɪfɔːrm/", "có dạng mạng lưới đám rối"),
    ("077300", "pleximeter", "noun", "/plɛkˈsɪmɪtər/", "tấm gõ chẩn đoán (y học)"),
    ("077301", "pleximetric", "adj", "/ˌplɛksɪˈmɛtrɪk/", "thuộc tấm gõ chẩn đoán (y học)"),
    ("077302", "pleximetry", "noun", "/plɛkˈsɪmɪtri/", "phép gõ khám chẩn đoán (y học)"),
]

with open("scratch/b36_r05_raw_p3.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r05_p3.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r05_p3 saved OK")
