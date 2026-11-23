import json

items = [
    ("073903", "depersonalisations", "noun", "/diːˌpɜːrsənəlaɪˈzeɪʃənz/", "hội chứng giải thể nhân cách (Anh)"),
    ("073904", "dripstones", "noun", "/ˈdrɪpˌstoʊnz/", "nhũ đá vôi hang động; gờ hắt nước"),
    ("073905", "electrosurgeries", "noun", "/ɪˌlɛktroʊˈsɜːrdʒəriz/", "phẫu thuật đốt cắt bằng dòng điện"),
    ("073906", "endecotts", "noun", "/ˈɛndɪkɒts/", "thống đốc John Endecott (Mỹ cổ)"),
    ("073907", "erythrodermas", "noun", "/ɪˌrɪθroʊˈdɜːrməz/", "chứng đỏ da toàn thân bong vảy"),
    ("073908", "escapologists", "noun", "/ˌɛskəˈpɒlədʒɪsts/", "nghệ sĩ ảo thuật thoát hiểm (Anh)"),
    ("073909", "febrifuges", "noun", "/ˈfɛbrɪˌfjuːdʒɪz/", "thuốc hạ sốt giải nhiệt"),
    ("073910", "fibroadenomas", "noun", "/ˌfaɪbroʊædɪˈnoʊməz/", "u xơ tuyến vú lành tính"),
    ("073911", "fomeses", "noun", "/ˈfoʊmiːzɪz/", "nấm gỗ mục lõi thuộc chi Fomes"),
    ("073912", "footbaths", "noun", "/ˈfʊtˌbɑːθs/", "chậu hoặc bồn ngâm rửa chân"),
    ("073913", "gnarling", "verb", "/ˈnɑːrlɪŋ/", "đang vặn xoắn tạo mấu sần sùi"),
    ("073914", "gnarls", "noun", "/nɑːrlz/", "mắt mấu sần sùi trên thân gỗ"),
    ("073915", "graticules", "noun", "/ˈɡrætɪˌkjuːlz/", "lưới vạch thị kính; lưới tọa độ"),
    ("073916", "guestimates", "noun", "/ˈɡɛstɪmɪts/", "ước lượng phỏng đoán đại khái"),
    ("073917", "hornfelses", "noun", "/ˈhɔːrnˌfɛlsɪz/", "đá biến chất sừng hornfels"),
    ("073918", "jasminums", "noun", "/ˈdʒæzmɪnəmz/", "chi Cây hoa nhài hương (Jasminum)"),
    ("073919", "kirgizes", "noun", "/ˈkɪərɡɪzɪz/", "người dân tộc Kyrgyz Trung Á"),
    ("073920", "korzybskis", "noun", "/kɔːrˈzɪbskiz/", "nhà ngữ nghĩa học Alfred Korzybski"),
    ("073921", "lavaboes", "noun", "/ləˈveɪboʊz/", "chậu rửa tay nghi lễ; bồn rửa (tôn)"),
    ("073922", "lavabos", "noun", "/ləˈveɪboʊz/", "bồn rửa mặt; nghi thức rửa tay lễ"),
    ("073923", "limaxes", "noun", "/ˈlaɪmæksɪz/", "chi Sên trần gây hại (Limax)"),
    ("073924", "lopressors", "noun", "/loʊˈprɛsərz/", "thuốc chẹn beta hạ áp Lopressor"),
    ("073925", "lothringens", "noun", "/ˈloʊtrɪŋənz/", "vùng Lorraine (tên Đức Lothringen)"),
    ("073926", "lullis", "noun", "/ˈlʊliz/", "nhà soạn nhạc Pháp Jean Lully"),
    ("073927", "malmseys", "noun", "/ˈmɑːmziz/", "rượu vang ngọt đậm Malmsey"),
    ("073928", "margays", "noun", "/ˈmɑːrɡeɪz/", "mèo rừng đốm leo cây Nam Mỹ margay"),
    ("073929", "medlarses", "noun", "/ˈmɛdlɑːrzɪz/", "hệ thống dữ liệu y khoa MEDLARS"),
    ("073930", "megachiles", "noun", "/ˌmɛɡəˈkaɪliːz/", "chi Ong cắt lá (Megachile)"),
    ("073931", "mesomorphs", "noun", "/ˈmɛzoʊˌmɔːrfs/", "người có tạng cơ bắp vạm vỡ"),
    ("073932", "migrators", "noun", "/ˈmaɪˌɡreɪtərz/", "người hoặc chim thú di cư theo mùa"),
    ("073933", "monodons", "noun", "/ˈmɒnəˌdɒnz/", "chi Kỳ lân biển một ngà (Monodon)"),
    ("073934", "multiprogrammings", "noun", "/ˌmʌltiˈproʊɡræmɪŋz/", "kỹ thuật đa chương trình (máy tính)"),
    ("073935", "mylantas", "noun", "/maɪˈlæntəz/", "thuốc kháng axit dạ dày Mylanta"),
    ("073936", "myomas", "noun", "/maɪˈoʊməz/", "khối u cơ lành tính (u xơ cơ)"),
    ("073937", "myomata", "noun", "/maɪˈoʊmətə/", "khối u cơ lành tính (y học)"),
    ("073938", "naprosyns", "noun", "/nəˈprɒsɪnz/", "thuốc kháng viêm giảm đau Naprosyn"),
    ("073939", "nebes", "noun", "/ˌɛn iː biː ˈiːz/", "hướng đông-bắc chếch đông (NEbE)"),
    ("073940", "neurolinguisticses", "noun", "/ˌnjʊəroʊlɪŋˈɡwɪstɪksɪz/", "ngành ngôn ngữ học thần kinh"),
    ("073941", "nilgais", "noun", "/ˈnɪlˌɡaɪz/", "linh dương sừng ngắn Ấn Độ nilgai"),
    ("073942", "oriflammes", "noun", "/ˈɒrɪˌflæmz/", "ngọn cờ hiệu tập hợp đỏ Pháp cổ"),
    ("073943", "ormers", "noun", "/ˈɔːrmərz/", "bào ngư châu Âu vỏ xà cừ"),
    ("073944", "ottars", "noun", "/ˈɒtərz/", "tinh dầu hoa hồng thơm (attar)"),
    ("073945", "palinuri", "noun", "/ˌpælɪˈnjʊəraɪ/", "chi Tôm hùm gai không càng"),
    ("073946", "palmists", "noun", "/ˈpɑːmɪsts/", "thầy bói xem đường chỉ bàn tay"),
    ("073947", "pearmains", "noun", "/ˈpɛərmeɪnz/", "giống táo cổ điển Pearmain"),
    ("073948", "phenothiazines", "noun", "/ˌfiːnoʊˈθaɪəziːnz/", "nhóm thuốc an thần phenothiazine"),
    ("073949", "precipitants", "noun", "/prɪˈsɪpɪtənts/", "tác nhân gây kết tủa (hóa học)"),
    ("073950", "procardias", "noun", "/proʊˈkɑːrdiəz/", "thuốc hạ huyết áp Procardia"),
    ("073951", "promisees", "noun", "/ˌprɒmɪˈsiːz/", "người được nhận lời hứa cam kết"),
    ("073952", "puerperiums", "noun", "/pjʊˈɜːrpiəmz/", "thời kỳ hậu sản sau sinh nở"),
    ("073953", "pumpkinseeds", "noun", "/ˈpʌmpkɪnˌsiːdz/", "cá thái dương Bắc Mỹ; hạt bí ngô"),
    ("073954", "pyridiums", "noun", "/paɪˈrɪdiəmz/", "thuốc giảm đau tiết niệu Pyridium"),
    ("073955", "raphias", "noun", "/ˈræfiəz/", "cọ lá sợi raphia châu Phi"),
    ("073956", "redeposited", "verb", "/ˌriːdɪˈpɒzɪtɪd/", "đã gửi tiền lại; đã lắng đọng lại"),
    ("073957", "redepositing", "verb", "/ˌriːdɪˈpɒzɪtɪŋ/", "đang gửi lại tiền; lắng đọng lại"),
    ("073958", "redeposits", "verb", "/ˌriːdɪˈpɒzɪts/", "gửi tiền lại; lắng đọng lại"),
    ("073959", "relativized", "verb", "/ˈrɛlətɪˌvaɪzd/", "đã tương đối hóa (triết, vật lý)"),
    ("073960", "relativizes", "verb", "/ˈrɛlətɪˌvaɪzɪz/", "tương đối hóa; áp thuyết tương đối"),
    ("073961", "relativizing", "verb", "/ˈrɛlətɪˌvaɪzɪŋ/", "đang tương đối hóa khái niệm"),
    ("073962", "roomettes", "noun", "/ruːˈmɛts/", "khoang giường nằm đơn trên tàu hỏa"),
    ("073963", "sabbatarians", "noun", "/ˌsæbəˈtɛəriənz/", "người giữ nghiêm ngày Sa-bát"),
    ("073964", "scarers", "noun", "/ˈskɛərərz/", "bù nhìn dọa chim; kẻ dọa dẫm"),
    ("073965", "seckels", "noun", "/ˈsɛkəlz/", "giống lê quả nhỏ ngọt Seckel"),
    ("073966", "semimonthlies", "noun", "/ˌsɛmiˈmʌnθliz/", "tạp chí xuất bản nửa tháng một kỳ"),
    ("073967", "sestets", "noun", "/sɛsˈtɛts/", "khổ thơ sáu dòng; bản hòa tấu sáu"),
    ("073968", "simooms", "noun", "/sɪˈmuːmz/", "gió bụi nóng sa mạc si-mum"),
    ("073969", "sinitics", "noun", "/sɪˈnɪtɪks/", "nhóm ngôn ngữ Hán (Hán ngữ)"),
    ("073970", "sirenias", "noun", "/saɪˈriːniəz/", "bộ Bò biển (lợn biển, cá cúi)"),
    ("073971", "sneezers", "noun", "/ˈsniːzərz/", "người đang hắt hơi nhảy mũi"),
    ("073972", "spadefishes", "noun", "/ˈspeɪdˌfɪʃɪz/", "cá tai tượng biển (họ Cá tai tượng)"),
    ("073973", "starvelings", "noun", "/ˈstɑːrvlɪŋz/", "người hoặc vật gầy đói tiều tụy"),
    ("073974", "stylisations", "noun", "/ˌstaɪlaɪˈzeɪʃənz/", "sự cách điệu hóa nghệ thuật (Anh)"),
    ("073975", "subserved", "verb", "/sʌbˈsɜːrvd/", "đã phụng sự hỗ trợ phục vụ cho"),
    ("073976", "subserves", "verb", "/sʌbˈsɜːrvz/", "hỗ trợ phụ trợ thúc đẩy mục đích"),
    ("073977", "subserving", "verb", "/sʌbˈsɜːrvɪŋ/", "đang phụ trợ thúc đẩy giúp ích cho"),
    ("073978", "syncytia", "noun", "/sɪnˈsɪʃə/", "hợp bào nhiều nhân (sinh học)"),
    ("073979", "syncytiums", "noun", "/sɪnˈsɪʃəmz/", "hợp bào nhiều nhân (sinh học)"),
    ("073980", "tagalongs", "noun", "/ˈtæɡəˌlɒŋz/", "kẻ bám đuôi lẽo đẽo đi theo sau"),
    ("073981", "tamanduas", "noun", "/təˈmændwəz/", "thú ăn kiến leo cây tamandua"),
    ("073982", "telemeters", "noun", "/tɪˈlɛmɪtərz/", "máy đo từ xa; thiết bị viễn trắc"),
    ("073983", "tellurians", "noun", "/tɛˈlʊəriənz/", "cư dân sống trên hành tinh Trái Đất"),
    ("073984", "terces", "noun", "/ˈtɜːrsɪz/", "kinh giờ thứ ba (biến thể tierce)"),
    ("073985", "tiburs", "noun", "/ˈtaɪbərz/", "thành cổ Tivoli (Tibur) gần Rome"),
    ("073986", "timbrels", "noun", "/ˈtɪmbrəlz/", "trống lắc tay nhỏ thời Kinh Thánh"),
    ("073987", "tortrixes", "noun", "/ˈtɔːrtrɪksɪz/", "bướm ngài cuốn lá hại cây"),
    ("073988", "trephined", "verb", "/trɪˈfaɪnd/", "đã khoan mở lỗ tròn trên xương sọ"),
    ("073989", "trephines", "noun", "/trɪˈfaɪnz/", "mũi khoan tròn mở xương sọ (y học)"),
    ("073990", "trephining", "verb", "/trɪˈfaɪnɪŋ/", "đang khoan mở lỗ tròn xương sọ"),
    ("073991", "unsexes", "verb", "/ʌnˈsɛksɪz/", "triệt sản; làm mất nét nữ hoặc nam"),
    ("073992", "unsexing", "verb", "/ʌnˈsɛksɪŋ/", "đang triệt sản; mất nét giới tính"),
    ("073993", "utahraptors", "noun", "/ˈjuːtɑːˌræptərz/", "khủng long săn mồi Utahraptor"),
    ("073994", "venires", "noun", "/vɪˈnaɪəriz/", "trát triệu tập danh sách bồi thẩm"),
    ("073995", "viverras", "noun", "/vɪˈvɛrəz/", "chi Cầy hương châu Á (Viverra)"),
    ("073996", "vocalisms", "noun", "/ˈvoʊkəˌlɪzəmz/", "sự phát âm giọng nói; hệ nguyên âm"),
    ("073997", "wainscottings", "noun", "/ˈweɪnˌskɒtɪŋz/", "ván gỗ ốp chân tường nội thất"),
    ("073998", "wodans", "noun", "/ˈwoʊdənz/", "thần tối cao Wodan (Odin Đức)"),
    ("073999", "zamias", "noun", "/ˈzeɪmiəz/", "cây tuế lá dày vùng Mỹ chi Zamia"),
    ("074000", "aestivations", "noun", "/ˌɛstɪˈveɪʃənz/", "trạng thái ngủ hè; tiền khai hoa"),
    ("074001", "anamorphoses", "noun", "/ˌænəmɔːrˈfoʊsiːz/", "ảnh biến hình méo góc (hội họa)"),
    ("074002", "appenzellers", "noun", "/ˈæpɛnˌtsɛlərz/", "giống bò, chó hoặc phô mai Thụy Sĩ"),
]

with open("scratch/b35_r08_raw_p5.json") as f:
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

with open("scratch/b35_r08_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r08_p5.json OK")
