import json

rows = [
    ("078503", "preceptive", "adj", "/prɪˈsɛptɪv/", "mang tính răn dạy, giáo huấn"),
    ("078504", "preceptively", "adv", "/prɪˈsɛptɪvli/", "theo cách răn dạy, khuyên bảo"),
    ("078505", "preceptorial", "adj", "/ˌpriːsɛpˈtɔːriəl/", "thuộc người giảng dạy, gia sư"),
    ("078506", "preceptorially", "adv", "/ˌpriːsɛpˈtɔːriəli/", "với tư cách thầy giáo, gia sư"),
    ("078507", "preceptress", "noun", "/prɪˈsɛptrɪs/", "nữ giáo viên, cô giáo kèm riêng"),
    ("078508", "precepts", "noun", "/ˈpriːsɛpts/", "lời răn dạy, quy tắc đạo đức"),
    ("078509", "precessional", "adj", "/prɪˈsɛʃənəl/", "thuộc sự tiến động (thiên văn học)"),
    ("078510", "prechlorination", "noun", "/ˌpriːklɔːrɪˈneɪʃən/", "sự khử trùng nước bằng clo sơ bộ"),
    ("078511", "precincts", "noun", "/ˈpriːsɪŋkts/", "khu vực ranh giới; đồn cảnh sát"),
    ("078512", "preciosity", "noun", "/ˌprɛʃiˈɒsɪti/", "sự cầu kỳ, kiểu cách văn chương"),
    ("078513", "precipitability", "noun", "/prɪˌsɪpɪtəˈbɪlɪti/", "khả năng kết tủa, khả năng lắng"),
    ("078514", "precipitable", "adj", "/prɪˈsɪpɪtəbəl/", "có thể kết tủa được (hóa học)"),
    ("078515", "precipitance", "noun", "/prɪˈsɪpɪtəns/", "sự hấp tấp, vội vã thiếu cân nhắc"),
    ("078516", "precipitancy", "noun", "/prɪˈsɪpɪtənsi/", "tính hấp tấp, vội vàng nóng nảy"),
    ("078517", "precipitantly", "adv", "/prɪˈsɪpɪtəntli/", "một cách hấp tấp, vội vã đâm đầu"),
    ("078518", "precipitated", "verb", "/prɪˈsɪpɪˌteɪtɪd/", "đã gây ra đột ngột; đã kết tủa"),
    ("078519", "precipitateness", "noun", "/prɪˈsɪpɪtɪtnəs/", "tính hấp tấp, sự vội vã bồng bột"),
    ("078520", "precipitates", "verb", "/prɪˈsɪpɪˌteɪts/", "gây ra đột ngột; kết tủa (hóa học)"),
    ("078521", "precipitations", "noun", "/prɪˌsɪpɪˈteɪʃənz/", "lượng mưa; sự kết tủa (hóa học)"),
    ("078522", "precipitative", "adj", "/prɪˈsɪpɪˌteɪtɪv/", "có tác dụng gây kết tủa"),
    ("078523", "precipitin", "noun", "/prɪˈsɪpɪtɪn/", "kháng thể kết tủa (miễn dịch học)"),
    ("078524", "precipitousness", "noun", "/prɪˈsɪpɪtəsnəs/", "độ dốc đứng cheo leo; sự vội vàng"),
    ("078525", "precised", "verb", "/ˈpreɪsiːd/", "đã tóm tắt cô đọng văn bản"),
    ("078526", "precises", "verb", "/ˈpreɪsiːz/", "tóm tắt cô đọng văn bản"),
    ("078527", "precisian", "noun", "/prɪˈsɪʒən/", "người câu nệ quy tắc đạo đức (cổ)"),
    ("078528", "precisianism", "noun", "/prɪˈsɪʒənɪzəm/", "thói câu nệ nghi thức, đạo đức"),
    ("078529", "precising", "verb", "/ˈpreɪsiːɪŋ/", "tóm tắt cô đọng văn bản"),
    ("078530", "precisions", "noun", "/prɪˈsɪʒənz/", "độ chính xác, tính chuẩn xác"),
    ("078531", "precisive", "adj", "/prɪˈsaɪsɪv/", "chính xác rõ ràng; tách biệt hẳn"),
    ("078532", "precluded", "verb", "/prɪˈkluːdɪd/", "đã ngăn ngừa, loại trừ khả năng"),
    ("078533", "precludes", "verb", "/prɪˈkluːdz/", "ngăn ngừa, loại trừ khả năng"),
    ("078534", "precluding", "verb", "/prɪˈkluːdɪŋ/", "ngăn ngừa, loại trừ khả năng"),
    ("078535", "preclusive", "adj", "/prɪˈkluːsɪv/", "có tác dụng ngăn ngừa, loại trừ"),
    ("078536", "preclusively", "adv", "/prɪˈkluːsɪvli/", "nhằm ngăn ngừa hoặc loại trừ"),
    ("078537", "precoat", "noun", "/ˈpriːkoʊt/", "lớp sơn lót; lớp lọc trợ lắng"),
    ("078538", "precogitate", "verb", "/ˌpriːˈkɒdʒɪteɪt/", "suy tính trước, cân nhắc trước"),
    ("078539", "precolonial", "adj", "/ˌpriːkəˈloʊniəl/", "trước thời kỳ thuộc địa"),
    ("078540", "precombustion", "noun", "/ˌpriːkəmˈbʌstʃən/", "sự tiền cháy (buồng đốt phụ)"),
    ("078541", "precommissioning", "noun", "/ˌpriːkəˈmɪʃənɪŋ/", "công tác chuẩn bị nghiệm thu máy"),
    ("078542", "precommunity", "noun", "/ˌpriːkəˈmjuːnəti/", "quần xã sinh vật tiên khởi"),
    ("078543", "precomposed", "adj", "/ˌpriːkəmˈpoʊzd/", "được dựng sẵn, ghép sẵn (ký tự)"),
    ("078544", "precompression", "noun", "/ˌpriːkəmˈprɛʃən/", "sự nén sơ bộ, nén trước"),
    ("078545", "preconceive", "verb", "/ˌpriːkənˈsiːv/", "hình dung trước, định kiến trước"),
    ("078546", "preconcert", "verb", "/ˌpriːkənˈsɜːrt/", "thỏa thuận trước, thu xếp từ trước"),
    ("078547", "preconcerted", "adj", "/ˌpriːkənˈsɜːrtɪd/", "đã thỏa thuận trước, dàn xếp sẵn"),
    ("078548", "precondemn", "verb", "/ˌpriːkənˈdɛm/", "kết tội từ trước, định kiến trước"),
    ("078549", "precondenser", "noun", "/ˌpriːkənˈdɛnsər/", "bộ ngưng tụ sơ bộ (kỹ thuật)"),
    ("078550", "preconise", "verb", "/ˈprɛkənaɪz/", "công bố sắc phong giám mục; ca ngợi"),
    ("078551", "preconization", "noun", "/ˌprɛkənaɪˈzeɪʃən/", "sự công bố sắc phong (Giáo hội)"),
    ("078552", "preconize", "verb", "/ˈprɛkənaɪz/", "công bố sắc phong giám mục; ca ngợi"),
    ("078553", "preconquest", "adj", "/ˌpriːˈkɒŋkwɛst/", "trước cuộc chinh phạt Norman (Anh)"),
    ("078554", "preconscious", "adj", "/ˌpriːˈkɒnʃəs/", "thuộc tiền ý thức (tâm lý học)"),
    ("078555", "preconsider", "verb", "/ˌpriːkənˈsɪdər/", "xem xét trước, cân nhắc trước"),
    ("078556", "preconsign", "verb", "/ˌpriːkənˈsaɪn/", "ủy thác trước, giao phó từ trước"),
    ("078557", "preconsonantal", "adj", "/ˌpriːkɒnsəˈnæntəl/", "đứng ngay trước phụ âm (ngữ âm)"),
    ("078558", "preconstitute", "verb", "/ˌpriːˈkɒnstɪtjuːt/", "thiết lập từ trước, định sẵn"),
    ("078559", "precontract", "verb", "/ˌpriːkənˈtrækt/", "lập giao ước trước (hôn ước cũ)"),
    ("078560", "precontrive", "verb", "/ˌpriːkənˈtraɪv/", "trù tính trước, sắp đặt từ trước"),
    ("078561", "precook", "verb", "/ˌpriːˈkʊk/", "nấu sơ qua, luộc sơ chế biến sẵn"),
    ("078562", "precooking", "verb", "/ˌpriːˈkʊkɪŋ/", "nấu sơ qua, luộc sơ chế biến sẵn"),
    ("078563", "precooks", "verb", "/ˌpriːˈkʊks/", "nấu sơ qua, luộc sơ chế biến sẵn"),
    ("078564", "precool", "verb", "/ˌpriːˈkuːl/", "làm nguội sơ bộ, hạ nhiệt trước"),
    ("078565", "precooled", "adj", "/ˌpriːˈkuːld/", "đã được làm lạnh sơ bộ trước"),
    ("078566", "precooler", "noun", "/ˌpriːˈkuːlər/", "bộ làm lạnh sơ bộ, giàn làm mát"),
    ("078567", "precopulary", "adj", "/ˌpriːˈkɒpjʊləri/", "trước khi giao phối (sinh học)"),
    ("078568", "precordia", "noun", "/priˈkɔːrdiə/", "vùng trước tim (ngực trái)"),
    ("078569", "precordium", "noun", "/priˈkɔːrdiəm/", "vùng trước tim (vùng ngực trên tim)"),
    ("078570", "precornu", "noun", "/ˌpriːˈkɔːrnjuː/", "sừng trước não thất bên (y học)"),
    ("078571", "precostal", "adj", "/ˌpriːˈkɒstəl/", "ở phía trước xương sườn (giải phẫu)"),
    ("078572", "precranial", "adj", "/ˌpriːˈkreɪniəl/", "ở phía trước hộp sọ (giải phẫu)"),
    ("078573", "precritical", "adj", "/ˌpriːˈkrɪtɪkəl/", "tiền phê phán (Kant; chưa tới hạn)"),
    ("078574", "precrural", "adj", "/ˌpriːˈkrʊrəl/", "ở phía trước đùi (giải phẫu)"),
    ("078575", "precuring", "noun", "/ˌpriːˈkjʊrɪŋ/", "sự lưu hóa sơ bộ (cao su)"),
    ("078576", "precursive", "adj", "/prɪˈkɜːrsɪv/", "báo hiệu trước, mở đường cho"),
    ("078577", "precystic", "adj", "/ˌpriːˈsɪstɪk/", "trước giai đoạn đóng kén (ký sinh)"),
    ("078578", "predacean", "noun", "/prɪˈdeɪʃən/", "động vật ăn thịt săn mồi"),
    ("078579", "predacity", "noun", "/prɪˈdæsɪti/", "tập tính ăn thịt săn mồi sống"),
    ("078580", "predal", "adj", "/ˈpriːdəl/", "thuộc động vật săn mồi ăn thịt"),
    ("078581", "predated", "verb", "/ˌpriːˈdeɪtɪd/", "đã có từ trước; đã ghi lùi ngày"),
    ("078582", "predates", "verb", "/ˌpriːˈdeɪts/", "có từ trước; ghi lùi ngày; săn mồi"),
    ("078583", "predating", "verb", "/ˌpriːˈdeɪtɪŋ/", "có từ trước; ghi lùi ngày; săn mồi"),
    ("078584", "predatism", "noun", "/ˈprɛdətɪzəm/", "tập tính săn mồi ăn thịt"),
    ("078585", "predatorily", "adv", "/ˈprɛdətərɪli/", "theo lối săn mồi, bóc lột tàn bạo"),
    ("078586", "predatoriness", "noun", "/ˈprɛdətərinəs/", "bản tính săn mồi, tham lam tàn bạo"),
    ("078587", "predawn", "noun", "/ˌpriːˈdɔːn/", "lúc chạng vạng trước bình minh"),
    ("078588", "predeceased", "verb", "/ˌpriːdɪˈsiːst/", "đã qua đời trước (ai đó)"),
    ("078589", "predeceases", "verb", "/ˌpriːdɪˈsiːsɪz/", "qua đời trước (ai đó)"),
    ("078590", "predeceasing", "verb", "/ˌpriːdɪˈsiːsɪŋ/", "qua đời trước (ai đó)"),
    ("078591", "predeclare", "verb", "/ˌpriːdɪˈklɛr/", "khai báo trước, công bố từ trước"),
    ("078592", "predella", "noun", "/prɪˈdɛlə/", "bệ bàn thờ vẽ tranh (kiến trúc)"),
    ("078593", "predesign", "verb", "/ˌpriːdɪˈzaɪn/", "thiết kế sẵn, hoạch định trước"),
    ("078594", "predesignate", "verb", "/ˌpriːˈdɛzɪɡneɪt/", "chỉ định trước, định sẵn từ trước"),
    ("078595", "predesignated", "verb", "/ˌpriːˈdɛzɪɡneɪtɪd/", "đã chỉ định trước, định sẵn"),
    ("078596", "predesignates", "verb", "/ˌpriːˈdɛzɪɡneɪts/", "chỉ định trước, định sẵn từ trước"),
    ("078597", "predesignating", "verb", "/ˌpriːˈdɛzɪɡneɪtɪŋ/", "chỉ định trước, định sẵn từ trước"),
    ("078598", "predesterminate", "adj", "/ˌpriːdɪˈtɜːrmɪnɪt/", "được tiền định trước (biến thể)"),
    ("078599", "predestermination", "noun", "/ˌpriːdɪˌtɜːrmɪˈneɪʃən/", "sự định đoạt trước, tiền định"),
    ("078600", "predestinarianism", "noun", "/ˌpriːdɛstɪˈnɛriənɪzəm/", "thuyết tiền định (thần học)"),
    ("078601", "predestinationist", "noun", "/ˌpriːdɛstɪˈneɪʃənɪst/", "người tin vào thuyết tiền định"),
    ("078602", "predestine", "verb", "/priˈdɛstɪn/", "định sẵn số phận, tiền định an bài"),
]

with open("scratch/b36_r08_raw_p1.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r08_p1.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r08_p1 saved OK")
