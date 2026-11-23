import json

rows = [
    ("074403", "fascistas", "noun", "/fəˈʃiːstəz/", "người phát xít Ý"),
    ("074404", "galerases", "noun", "/ɡəˈlɛrəsɪz/", "núi lửa Galeras (Colombia)"),
    ("074405", "germicides", "noun", "/ˈdʒɜːrmɪsaɪdz/", "chất diệt khuẩn"),
    ("074406", "gladiolas", "noun", "/ˌɡlædiˈoʊləz/", "hoa lay ơn; cây lay ơn"),
    ("074407", "gordiuses", "noun", "/ˈɡɔːrdiəsɪz/", "vua Gordius; giun bờm ngựa"),
    ("074408", "gulpers", "noun", "/ˈɡʌlpərz/", "người uống ừng ực; kẻ nuốt chửng"),
    ("074409", "haemophiliacs", "noun", "/ˌhiːməˈfɪliæks/", "người mắc bệnh máu khó đông"),
    ("074410", "homopteras", "noun", "/hoʊˈmɒptərəz/", "côn trùng bộ cánh đều"),
    ("074411", "humates", "noun", "/ˈhjuːmeɪts/", "muối humat; chất tạo mùn humat"),
    ("074412", "ideated", "verb", "/ˈaɪdieɪtɪd/", "đã hình thành ý niệm; tưởng tượng"),
    ("074413", "ideates", "verb", "/ˈaɪdieɪts/", "hình thành ý niệm; tưởng tượng"),
    ("074414", "ideating", "verb", "/ˈaɪdieɪtɪŋ/", "hình thành ý niệm; tưởng tượng"),
    ("074415", "indigoferas", "noun", "/ˌɪndɪˈɡɒfərəz/", "chi cây chàm (Indigofera)"),
    ("074416", "intertrigos", "noun", "/ˌɪntərˈtraɪɡoʊz/", "bệnh hăm kẽ da"),
    ("074417", "iodoforms", "noun", "/aɪˈɒdəfɔːrmz/", "hợp chất sát trùng iôđôfom"),
    ("074418", "itemised", "verb", "/ˈaɪtəmaɪzd/", "đã liệt kê chi tiết từng mục"),
    ("074419", "itemises", "verb", "/ˈaɪtəmaɪzɪz/", "liệt kê chi tiết từng mục"),
    ("074420", "itemising", "verb", "/ˈaɪtəmaɪzɪŋ/", "liệt kê chi tiết từng mục"),
    ("074421", "jaguas", "noun", "/ˈhɑːɡwəz/", "cây jagua (nhuộm da Nam Mỹ)"),
    ("074422", "lactalbumins", "noun", "/ˌlæktˈælbjəmɪnz/", "protein sữa lactalbumin"),
    ("074423", "limosas", "noun", "/laɪˈmoʊsəz/", "chi chim choắt mỏ thẳng"),
    ("074424", "linins", "noun", "/ˈlaɪnɪnz/", "sợi linin (trong nhân tế bào)"),
    ("074425", "lipchitzes", "noun", "/ˈlɪpʃɪtsɪz/", "nhà điêu khắc Jacques Lipchitz"),
    ("074426", "lumpers", "noun", "/ˈlʌmpərz/", "phu bốc vác cảng; người gộp nhóm"),
    ("074427", "lxxxes", "noun", "/ˈɛksɪz/", "số La Mã tám mươi (LXXX)"),
    ("074428", "macrocephalies", "noun", "/ˌmækroʊˈsɛfəliz/", "chứng đầu to bất thường"),
    ("074429", "mandaeans", "noun", "/mænˈdiːənz/", "tín đồ Mandae; tiếng Mandae"),
    ("074430", "midplanes", "noun", "/ˈmɪdpleɪnz/", "mặt phẳng giữa; mặt trung tuyến"),
    ("074431", "monoclines", "noun", "/ˈmɒnəklaɪnz/", "nếp uốn đơn nghiêng (địa chất)"),
    ("074432", "motacillas", "noun", "/ˌmoʊtəˈsɪləz/", "chi chim chìa vôi (Motacilla)"),
    ("074433", "muleteers", "noun", "/ˌmjuːlɪˈtɪrz/", "người đánh thồ xe la"),
    ("074434", "octopods", "noun", "/ˈɒktəpɒdz/", "bạch tuộc; động vật chân đầu 8 tua"),
    ("074435", "orczies", "noun", "/ˈɔːrtsiz/", "nữ văn sĩ Emma Orczy"),
    ("074436", "oxidisations", "noun", "/ˌɒksɪdaɪˈzeɪʃənz/", "sự ôxy hóa"),
    ("074437", "perseverations", "noun", "/pərˌsɛvəˈreɪʃənz/", "chứng lặp lời lặp hành vi (y học)"),
    ("074438", "pharsaluses", "noun", "/fɑːrˈseɪləsɪz/", "trận Pharsalus (La Mã cổ đại)"),
    ("074439", "photoconductivities", "noun", "/ˌfoʊtoʊˌkɒndʌkˈtɪvətiz/", "tính quang dẫn"),
    ("074440", "pinworms", "noun", "/ˈpɪnwɜːrmz/", "giun kim"),
    ("074441", "plosions", "noun", "/ˈploʊʒənz/", "sự bật hơi (ngữ âm học)"),
    ("074442", "pollexes", "noun", "/ˈpɒlɛksɪz/", "ngón tay cái (giải phẫu)"),
    ("074443", "pollices", "noun", "/ˈpɒlɪsiːz/", "ngón tay cái (giải phẫu)"),
    ("074444", "premissed", "verb", "/ˈprɛmɪst/", "đã đặt làm tiền đề; giả định trước"),
    ("074445", "premisses", "noun", "/ˈprɛmɪsɪz/", "tiền đề lập luận; bất động sản"),
    ("074446", "premissing", "verb", "/ˈprɛmɪsɪŋ/", "đặt làm tiền đề; giả định trước"),
    ("074447", "prickers", "noun", "/ˈprɪkərz/", "dùi nhọn; gai nhọn; kim chích"),
    ("074448", "pronated", "verb", "/ˈproʊneɪtɪd/", "đã xoay sấp cẳng tay hoặc bàn chân"),
    ("074449", "pronating", "verb", "/ˈproʊneɪtɪŋ/", "xoay sấp cẳng tay hoặc bàn chân"),
    ("074450", "protiums", "noun", "/ˈproʊtiəmz/", "hyđrô nhẹ H-1; chi cây trám hương"),
    ("074451", "pteridophytas", "noun", "/ˌtɛrɪdəˈfaɪtəz/", "ngành dương xỉ (Pteridophyta)"),
    ("074452", "pushpins", "noun", "/ˈpʊʃpɪnz/", "đinh ghim bảng; trò đẩy ghim"),
    ("074453", "putouts", "noun", "/ˈpʊtaʊts/", "pha loại cầu thủ (bóng chày)"),
    ("074454", "ragpickers", "noun", "/ˈræɡˌpɪkərz/", "người nhặt giẻ rách phế liệu"),
    ("074455", "readapted", "verb", "/ˌriːəˈdæptɪd/", "đã thích nghi lại; phóng tác lại"),
    ("074456", "readapting", "verb", "/ˌriːəˈdæptɪŋ/", "thích nghi lại; phóng tác lại"),
    ("074457", "readapts", "verb", "/ˌriːəˈdæpts/", "thích nghi lại; phóng tác lại"),
    ("074458", "reproducers", "noun", "/ˌriːprəˈduːsərz/", "loa tái tạo âm; sinh vật sinh sản"),
    ("074459", "resorbed", "verb", "/rɪˈzɔːrbd/", "đã tái hấp thu; đã tiêu biến"),
    ("074460", "resorbing", "verb", "/rɪˈzɔːrbɪŋ/", "tái hấp thu; tiêu biến"),
    ("074461", "resorbs", "verb", "/rɪˈzɔːrbz/", "tái hấp thu; tiêu biến"),
    ("074462", "rhinorrheas", "noun", "/ˌraɪnəˈriːəz/", "chứng chảy nước mũi (y học)"),
    ("074463", "rosicrucianisms", "noun", "/ˌroʊzɪˈkruːʃənɪzəmz/", "học thuyết bí truyền Hoa Hồng Thập"),
    ("074464", "sadducees", "noun", "/ˈsædjəsiːz/", "tín đồ phái Sa-đu-sê (Do Thái cổ)"),
    ("074465", "sannyasins", "noun", "/sənˈjɑːsɪnz/", "tu sĩ khổ hạnh Ấn Độ giáo"),
    ("074466", "schistosomes", "noun", "/ˈʃɪstəsoʊmz/", "sán máng (ký sinh trùng)"),
    ("074467", "scuppernongs", "noun", "/ˈskʌpərnɒŋz/", "nho xạ vàng Scuppernong (Mỹ)"),
    ("074468", "sensitisings", "noun", "/ˈsɛnsɪtaɪzɪŋz/", "sự gây mẫn cảm; sự làm nhạy sáng"),
    ("074469", "smelteries", "noun", "/ˈsmɛltəriz/", "xưởng luyện kim; lò nấu quặng"),
    ("074470", "sortitions", "noun", "/sɔːrˈtɪʃənz/", "sự bốc thăm chọn cử"),
    ("074471", "stoolies", "noun", "/ˈstuːliz/", "kẻ chỉ điểm mật báo (tiếng lóng)"),
    ("074472", "tachymeters", "noun", "/təˈkɪmɪtərz/", "máy toàn đạc; đồng hồ đo tốc độ"),
    ("074473", "tatous", "noun", "/tɑːˈtuːz/", "con ta-tu, thú có mai (Nam Mỹ)"),
    ("074474", "terazosins", "noun", "/təˈræzəsɪnz/", "thuốc hạ huyết áp terazosin"),
    ("074475", "terpsichoreans", "noun", "/ˌtɜːrpsɪkəˈriːənz/", "vũ công múa ba-lê"),
    ("074476", "thermotherapies", "noun", "/ˌθɜːrmoʊˈθɛrəpiz/", "nhiệt trị liệu (y học)"),
    ("074477", "trepangs", "noun", "/trɪˈpæŋz/", "hải sâm sấy khô; hải sâm"),
    ("074478", "trusters", "noun", "/ˈtrʌstərz/", "người tin tưởng; bên ủy thác"),
    ("074479", "watercolourists", "noun", "/ˈwɔːtərˌkʌlərɪsts/", "họa sĩ vẽ màu nước"),
    ("074480", "wbns", "noun", "/ˌdʌbəljuːbiːˈɛnz/", "hướng tây chếch bắc (WbN)"),
    ("074481", "actinomycins", "noun", "/ˌæktɪnoʊˈmaɪsɪnz/", "kháng sinh actinomycin"),
    ("074482", "aleps", "noun", "/əˈlɛps/", "thành phố Aleppo (Syria)"),
    ("074483", "aramaeans", "noun", "/ˌærəˈmiːənz/", "người Aram; tiếng Aram (cổ đại)"),
    ("074484", "arbitrageurs", "noun", "/ˌɑːrbɪtrɑːˈʒɜːrz/", "người kinh doanh chênh lệch giá"),
    ("074485", "arianrhods", "noun", "/ˌærɪænˈrɒdz/", "nữ thần Arianrhod (thần thoại Celt)"),
    ("074486", "autotomies", "noun", "/ɔːˈtɒtəmiz/", "sự tự cắt bỏ bộ phận tự vệ"),
    ("074487", "backscratchers", "noun", "/ˈbækˌskrætʃərz/", "cây gãi lưng; người nịnh hót"),
    ("074488", "bandoleers", "noun", "/ˌbændəˈlɪrz/", "dây đeo đạn qua vai"),
    ("074489", "beduins", "noun", "/ˈbɛduɪnz/", "người du mục Bedouin"),
    ("074490", "bowknots", "noun", "/ˈboʊnɒts/", "nút thắt nơ dễ mở"),
    ("074491", "brachiopodas", "noun", "/ˌbrækiˈɒpədəz/", "ngành động vật tay cuộn"),
    ("074492", "brages", "noun", "/ˈbrɑːɡəz/", "thần thi ca Brage (Bắc Âu)"),
    ("074493", "callisthenicses", "noun", "/ˌkælɪsˈθɛnɪksɪz/", "bài thể dục tay không nhịp điệu"),
    ("074494", "carthamuses", "noun", "/ˈkɑːrθəməsɪz/", "chi cây rum (cây hồng hoa)"),
    ("074495", "cataphracts", "noun", "/ˈkætəfrækts/", "kỵ binh thiết giáp nặng cổ đại"),
    ("074496", "cathas", "noun", "/ˈkæθəz/", "chi cây lá khát (Catha)"),
    ("074497", "catmints", "noun", "/ˈkætmɪnts/", "cây bạc hà mèo"),
    ("074498", "cercises", "noun", "/ˈsɜːrsɪsiːz/", "chi cây tử kinh (Cercis)"),
    ("074499", "chaggas", "noun", "/ˈtʃɑːɡəz/", "người Chagga; tiếng Chagga"),
    ("074500", "chelones", "noun", "/kɪˈloʊniːz/", "chi hoa đầu rùa (Chelone)"),
    ("074501", "cherimoyas", "noun", "/ˌtʃɛrɪˈmɔɪəz/", "quả na rừng (mãng cầu xiêm Peru)"),
    ("074502", "chiasmas", "noun", "/kaɪˈæzməz/", "giao thoa NST; chéo thị giác"),
]

with open("scratch/b35_r09_raw_p5.json", "r", encoding="utf-8") as f:
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

with open("scratch/b35_r09_p5.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b35_r09_p5 saved OK")
