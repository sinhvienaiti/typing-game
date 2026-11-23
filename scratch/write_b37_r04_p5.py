import json

records = [
    ("081903", "receptions", "noun", "/rɪˈsɛpʃənz/", "lễ tiếp đón; sự thu sóng"),
    ("081904", "receptively", "adv", "/rɪˈsɛptɪvli/", "với thái độ cởi mở, dễ tiếp thu"),
    ("081905", "receptrix", "noun", "/rɪˈsɛptrɪks/", "máy thu động cơ điện (thuật ngữ cũ)"),
    ("081906", "recesses", "verb", "/rɪˈsɛsɪz/", "khoét hốc; đặt lùi; tạm nghỉ họp"),
    ("081907", "recessing", "verb", "/rɪˈsɛsɪŋ/", "khoét lõm lùi vào; tạm nghỉ họp"),
    ("081908", "recessus", "noun", "/rɪˈsɛsəs/", "ngách, hốc lõm sâu (giải phẫu học)"),
    ("081909", "rechange", "verb", "/riˈtʃeɪndʒ/", "thay đổi lại lần nữa; đổi mới lại"),
    ("081910", "recharged", "verb", "/ˌriːˈtʃɑːrdʒd/", "đã sạc lại pin; đã hồi phục sức lực"),
    ("081911", "recharges", "verb", "/ˌriːˈtʃɑːrdʒɪz/", "sạc lại điện; nạp lại; lấy lại sức"),
    ("081912", "recharging", "verb", "/ˌriːˈtʃɑːrdʒɪŋ/", "sạc lại pin; nghỉ ngơi hồi phục sức"),
    ("081913", "rechauffe", "noun", "/ˌreɪʃoʊˈfeɪ/", "món hâm lại; bài xào nấu lại"),
    ("081914", "rechristen", "verb", "/ˌriːˈkrɪsən/", "rửa tội lại; đặt tên mới cho"),
    ("081915", "rechristened", "verb", "/ˌriːˈkrɪsənd/", "đã rửa tội lại; đã đổi sang tên mới"),
    ("081916", "rechristening", "verb", "/ˌriːˈkrɪsənɪŋ/", "rửa tội lại; đặt lại tên gọi mới"),
    ("081917", "rechristens", "verb", "/ˌriːˈkrɪsənz/", "rửa tội lại; đặt tên mới cho"),
    ("081918", "recidivate", "verb", "/rɪˈsɪdəˌveɪt/", "tái phạm tội, tái phát tật xấu"),
    ("081919", "recidivous", "adj", "/rɪˈsɪdɪvəs/", "hay tái phạm tội, tái diễn thói xấu"),
    ("081920", "reciprocality", "noun", "/rɪˌsɪprəˈkæləti/", "tính tương hỗ, sự tác động qua lại"),
    ("081921", "reciprocated", "verb", "/rɪˈsɪprəˌkeɪtɪd/", "đã đáp lại; chạy tịnh tiến"),
    ("081922", "reciprocates", "verb", "/rɪˈsɪprəˌkeɪts/", "đáp lại tương xứng; chạy khứ hồi"),
    ("081923", "reciprocating", "verb", "/rɪˈsɪprəˌkeɪtɪŋ/", "đáp lại nhau; chạy tịnh tiến"),
    ("081924", "reciprocative", "adj", "/rɪˈsɪprəˌkeɪtɪv/", "có tính qua lại, đáp lại tương hỗ"),
    ("081925", "reciprocatory", "adj", "/rɪˈsɪprəkəˌtɔːri/", "có tính chất tương hỗ, qua lại"),
    ("081926", "recision", "noun", "/rɪˈsɪʒən/", "sự cắt bỏ; sự hủy bỏ (biến thể)"),
    ("081927", "recission", "noun", "/rɪˈsɪʒən/", "sự hủy bỏ hợp đồng (biến thể)"),
    ("081928", "recited", "verb", "/rɪˈsaɪtɪd/", "đã đọc thuộc lòng, ngâm thơ"),
    ("081929", "recites", "verb", "/rɪˈsaɪts/", "đọc thuộc lòng, ngâm thơ; kể lại"),
    ("081930", "reciting", "verb", "/rɪˈsaɪtɪŋ/", "đọc thuộc lòng, ngâm thơ; kể lại"),
    ("081931", "reck", "verb", "/rɛk/", "bận tâm, để ý lo ngại (từ cổ)"),
    ("081932", "recker", "noun", "/ˈrɛkər/", "tên họ Recker (tiếng Anh)"),
    ("081933", "reckers", "noun", "/ˈrɛkərz/", "gia đình họ Recker"),
    ("081934", "reckonable", "adj", "/ˈrɛkənəbəl/", "có thể tính toán, có thể đếm được"),
    ("081935", "reckoned", "verb", "/ˈrɛkənd/", "đã tính toán; đã cho rằng, đánh giá"),
    ("081936", "reckons", "verb", "/ˈrɛkənz/", "tính toán; ước chừng; cho rằng"),
    ("081937", "reclaimable", "adj", "/rɪˈkleɪməbəl/", "có thể đòi lại; cải tạo, tái chế"),
    ("081938", "reclaimation", "noun", "/ˌrɛkləˈmeɪʃən/", "sự cải tạo đất; sự đòi lại (lỗi)"),
    ("081939", "reclaiming", "verb", "/rɪˈkleɪmɪŋ/", "đòi lại, thu hồi; khai hoang"),
    ("081940", "reclaims", "verb", "/rɪˈkleɪmz/", "đòi lại, thu hồi; cải tạo tái chế"),
    ("081941", "reclassified", "verb", "/ˌriːˈklæsəˌfaɪd/", "đã phân loại lại, xếp hạng lại"),
    ("081942", "reclassifies", "verb", "/ˌriːˈklæsəˌfaɪz/", "phân loại lại, giải mật tài liệu"),
    ("081943", "reclassifying", "verb", "/ˌriːˈklæsəˌfaɪɪŋ/", "phân loại lại, sắp xếp lại danh mục"),
    ("081944", "recleaning", "noun", "/riˈkliːnɪŋ/", "sự làm sạch lại, sự lọc rửa lại"),
    ("081945", "reclinate", "adj", "/ˈrɛkləˌneɪt/", "uốn cong rũ xuống (lá, cành)"),
    ("081946", "reclines", "verb", "/rɪˈklaɪnz/", "ngả lưng nằm dựa, ngả thư giãn"),
    ("081947", "reclothe", "verb", "/ˌriːˈkloʊð/", "mặc quần áo lại cho; trang bị lại"),
    ("081948", "reclusion", "noun", "/rɪˈkluːʒən/", "đời sống ẩn dật; giam biệt lập"),
    ("081949", "reclusory", "noun", "/rɪˈkluːsəri/", "am ẩn tu của nhà tu hành ẩn dật"),
    ("081950", "recoal", "verb", "/ˌriːˈkoʊl/", "tiếp thêm than đá (tàu thủy, lò)"),
    ("081951", "recoat", "verb", "/ˌriːˈkoʊt/", "sơn phủ thêm một lớp sơn mới"),
    ("081952", "recognisability", "noun", "/ˌrɛkəɡnaɪzəˈbɪləti/", "tính dễ nhận biết, khả năng nhận ra"),
    ("081953", "recognisably", "adv", "/ˈrɛkəɡˌnaɪzəbli/", "rõ rệt đến mức dễ nhận ra (Anh)"),
    ("081954", "recognises", "verb", "/ˈrɛkəɡˌnaɪzɪz/", "nhận ra; công nhận, thừa nhận (Anh)"),
    ("081955", "recognising", "verb", "/ˈrɛkəɡˌnaɪzɪŋ/", "nhận ra; công nhận, ghi nhận (Anh)"),
    ("081956", "recognitions", "noun", "/ˌrɛkəɡˈnɪʃənz/", "những sự công nhận, ghi nhận"),
    ("081957", "recognizability", "noun", "/ˌrɛkəɡnaɪzəˈbɪləti/", "tính chất có thể nhận ra, nhận diện"),
    ("081958", "recognizer", "noun", "/ˈrɛkəɡˌnaɪzər/", "bộ nhận dạng (giọng nói, chữ viết)"),
    ("081959", "recognizes", "verb", "/ˈrɛkəɡˌnaɪzɪz/", "nhận ra, nhận diện; công nhận"),
    ("081960", "recognizing", "verb", "/ˈrɛkəɡˌnaɪzɪŋ/", "nhận ra, nhận diện; công nhận"),
    ("081961", "recoiless", "adj", "/ˈriːkɔɪlɪs/", "không giật khi bắn (biến thể)"),
    ("081962", "recoin", "verb", "/ˌriːˈkɔɪn/", "đúc lại (tiền); sáng tác lại"),
    ("081963", "recoinage", "noun", "/ˌriːˈkɔɪnɪdʒ/", "việc đúc lại tiền; tiền đúc lại"),
    ("081964", "recollected", "verb", "/ˌrɛkəˈlɛktɪd/", "đã nhớ lại, đã hồi tưởng lại"),
    ("081965", "recollecting", "verb", "/ˌrɛkəˈlɛktɪŋ/", "nhớ lại, hồi tưởng lại ký ức cũ"),
    ("081966", "recollective", "adj", "/ˌrɛkəˈlɛktɪv/", "có trí nhớ tốt, mang tính hồi tưởng"),
    ("081967", "recollects", "verb", "/ˌrɛkəˈlɛkts/", "nhớ lại, hồi tưởng lại điều đã qua"),
    ("081968", "recolonization", "noun", "/riˌkɑːlənaɪˈzeɪʃən/", "sự tái thực dân hóa, tái định cư"),
    ("081969", "recolonize", "verb", "/riˈkɑːləˌnaɪz/", "tái lập thuộc địa; tái định cư"),
    ("081970", "recolonized", "verb", "/riˈkɑːləˌnaɪzd/", "đã tái lập thuộc địa; tái định cư"),
    ("081971", "recolonizes", "verb", "/riˈkɑːləˌnaɪzɪz/", "tái lập thuộc địa; tái định cư"),
    ("081972", "recolonizing", "verb", "/riˈkɑːləˌnaɪzɪŋ/", "tái lập thuộc địa; tái định cư"),
    ("081973", "recombined", "verb", "/ˌriːkəmˈbaɪnd/", "đã tái tổ hợp, đã kết hợp trở lại"),
    ("081974", "recombines", "verb", "/ˌriːkəmˈbaɪnz/", "tái tổ hợp (ADN), kết hợp trở lại"),
    ("081975", "recombining", "verb", "/ˌriːkəmˈbaɪnɪŋ/", "tái tổ hợp, kết hợp lại với nhau"),
    ("081976", "recommenced", "verb", "/ˌriːkəˈmɛnst/", "đã bắt đầu lại, đã khởi động lại"),
    ("081977", "recommences", "verb", "/ˌriːkəˈmɛnsɪz/", "bắt đầu lại, khởi sự lại từ đầu"),
    ("081978", "recommencing", "verb", "/ˌriːkəˈmɛnsɪŋ/", "bắt đầu lại, tiếp tục lại"),
    ("081979", "recommendable", "adj", "/ˌrɛkəˈmɛndəbəl/", "đáng giới thiệu, đáng khen ngợi"),
    ("081980", "recommendatory", "adj", "/ˌrɛkəˈmɛndəˌtɔːri/", "có tính giới thiệu, tiến cử"),
    ("081981", "recommended", "verb", "/ˌrɛkəˈmɛndɪd/", "đã giới thiệu, khuyên, đề xuất"),
    ("081982", "recommender", "noun", "/ˌrɛkəˈmɛndər/", "người giới thiệu; hệ thống gợi ý"),
    ("081983", "recommending", "verb", "/ˌrɛkəˈmɛndɪŋ/", "giới thiệu, tiến cử; khuyên nên làm"),
    ("081984", "recommends", "verb", "/ˌrɛkəˈmɛndz/", "giới thiệu, tiến cử; khuyên nên làm"),
    ("081985", "recommitment", "noun", "/ˌriːkəˈmɪtmənt/", "sự tái cam kết; sự tống giam lại"),
    ("081986", "recommittal", "noun", "/ˌriːkəˈmɪtəl/", "sự tống giam lại; chuyển ủy ban"),
    ("081987", "recompensed", "verb", "/ˈrɛkəmˌpɛnst/", "đã đền bù, đã trả công xứng đáng"),
    ("081988", "recompenses", "verb", "/ˈrɛkəmˌpɛnsɪz/", "đền bù, bồi thường; trả công đáp lễ"),
    ("081989", "recompensing", "verb", "/ˈrɛkəmˌpɛnsɪŋ/", "đền bù, bồi thường; báo đáp công ơn"),
    ("081990", "recompilation", "noun", "/riˌkɑːmpəˈleɪʃən/", "sự biên dịch lại; biên soạn lại"),
    ("081991", "recompile", "verb", "/ˌriːkəmˈpaɪl/", "biên dịch lại mã; biên soạn lại"),
    ("081992", "recompiled", "verb", "/ˌriːkəmˈpaɪld/", "đã biên dịch lại; đã biên soạn lại"),
    ("081993", "recompiling", "verb", "/ˌriːkəmˈpaɪlɪŋ/", "biên dịch lại mã; biên soạn lại"),
    ("081994", "recompose", "verb", "/ˌriːkəmˈpoʊz/", "tái cấu tạo; lấy lại bình tĩnh"),
    ("081995", "recomposed", "verb", "/ˌriːkəmˈpoʊzd/", "đã tạo lại; đã lấy lại bình tĩnh"),
    ("081996", "recomposes", "verb", "/ˌriːkəmˈpoʊzɪz/", "tạo lại; lấy lại bình tĩnh"),
    ("081997", "recomposing", "verb", "/ˌriːkəmˈpoʊzɪŋ/", "tạo lại; lấy lại sự điềm tĩnh"),
    ("081998", "reconcentrate", "verb", "/ˌriːˈkɑːnsənˌtreɪt/", "tập trung lại, cô đặc lại"),
    ("081999", "reconcilability", "noun", "/ˌrɛkənsaɪləˈbɪləti/", "khả năng có thể hòa giải, dung hòa"),
    ("082000", "reconcilement", "noun", "/ˈrɛkənsaɪlmənt/", "sự hòa giải, sự giảng hòa"),
    ("082001", "reconciles", "verb", "/ˈrɛkənˌsaɪlz/", "hòa giải, giảng hòa; dung hòa"),
    ("082002", "reconciliatory", "adj", "/ˌrɛkənˈsɪliəˌtɔːri/", "nhằm hòa giải, mang tính giảng hòa"),
]

raw = json.load(open("scratch/b37_r04_raw_p5.json"))
by_id = {f"lex.en.200k.{r[0]}": r for r in records}
out = []
for orig in raw:
    sid, hw, pos, ipa, vi = by_id[orig["id"]]
    assert orig["hw"] == hw, f"{orig['id']}: {orig['hw']} vs {hw}"
    assert 0 < len(vi) <= 35, f"{sid} {hw} len={len(vi)}: {vi}"
    assert "/" not in vi, f"{sid} {hw} slash in vi"
    assert ipa.count("/") == 2 and not ipa.startswith("/ ") and not ipa.endswith(" /"), f"{sid} {hw} bad ipa"
    orig["pos"] = pos
    orig["ipa"] = ipa
    orig["vi"] = vi
    orig["status"] = "reviewed"
    out.append(orig)

assert len(out) == 100
with open("scratch/b37_r04_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r04_p5 saved OK")
