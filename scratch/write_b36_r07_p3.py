import json

rows = [
    ("078203", "postdated", "verb", "/ˌpoʊstˈdeɪtɪd/", "đã ghi lùi ngày sau; xảy ra sau"),
    ("078204", "postdates", "verb", "/ˌpoʊstˈdeɪts/", "ghi lùi ngày sau; xảy ra sau"),
    ("078205", "postdating", "verb", "/ˌpoʊstˈdeɪtɪŋ/", "ghi lùi ngày sau; xảy ra sau"),
    ("078206", "postdiluvian", "adj", "/ˌpoʊstdɪˈluːviən/", "thuộc thời kỳ sau Đại hồng thủy"),
    ("078207", "posteriority", "noun", "/pɒˌstɪriˈɒrɪti/", "vị trí ở phía sau; tính xảy ra sau"),
    ("078208", "posteriorly", "adv", "/pɒˈstɪriərli/", "ở phía sau, về hướng đuôi"),
    ("078209", "posters", "noun", "/ˈpoʊstərz/", "áp phích quảng cáo; người đăng bài"),
    ("078210", "postexilic", "adj", "/ˌpoʊstɛɡˈzɪlɪk/", "thuộc thời hậu lưu đày (Do Thái)"),
    ("078211", "postfixal", "adj", "/ˈpoʊstˌfɪksəl/", "thuộc hậu tố (từ vựng)"),
    ("078212", "postfixial", "adj", "/ˈpoʊstˌfɪksiəl/", "thuộc hậu tố (biến thể)"),
    ("078213", "postgasm", "noun", "/ˈpoʊstˌɡæzəm/", "trạng thái sau đạt cực khoái"),
    ("078214", "posthitis", "noun", "/pɒsˈθaɪtɪs/", "bệnh viêm bao quy đầu (y học)"),
    ("078215", "posthouse", "noun", "/ˈpoʊstˌhaʊs/", "trạm dịch mã đổi ngựa xưa; quán trọ"),
    ("078216", "posthumousness", "noun", "/ˈpɒstjʊməsnəs/", "tính chất diễn ra sau khi qua đời"),
    ("078217", "postiche", "noun", "/pɒˈstiːʃ/", "tóc giả; phần thêm vào giả tạo"),
    ("078218", "postillion", "noun", "/pəˈstɪljən/", "người cưỡi ngựa dẫn cỗ xe ngựa"),
    ("078219", "postimpressionist", "noun", "/ˌpoʊstɪmˈprɛʃənɪst/", "họa sĩ trường phái Hậu Ấn tượng"),
    ("078220", "postmarked", "verb", "/ˈpoʊstˌmɑːrkt/", "đã đóng dấu bưu điện"),
    ("078221", "postmarking", "verb", "/ˈpoʊstˌmɑːrkɪŋ/", "đóng dấu bưu điện (lên phong bì)"),
    ("078222", "postmarks", "verb", "/ˈpoʊstˌmɑːrks/", "đóng dấu bưu điện (lên phong bì)"),
    ("078223", "postmastership", "noun", "/ˈpoʊstˌmɑːstərʃɪp/", "chức vụ trưởng bưu cục"),
    ("078224", "postmen", "noun", "/ˈpoʊstmən/", "người đưa thư (nhân viên bưu điện)"),
    ("078225", "postmenta", "noun", "/poʊstˈmɛntə/", "phần gốc môi dưới (côn trùng học)"),
    ("078226", "postmentum", "noun", "/poʊstˈmɛntəm/", "phần gốc môi dưới (côn trùng học)"),
    ("078227", "postmeridian", "adj", "/ˌpoʊstməˈrɪdiən/", "buổi chiều (sau 12 giờ trưa, PM)"),
    ("078228", "postmortal", "adj", "/ˌpoʊstˈmɔːrtəl/", "sau khi chết, hậu tử (y học)"),
    ("078229", "postnatally", "adv", "/ˌpoʊstˈneɪtəli/", "ở giai đoạn sau khi sinh"),
    ("078230", "postponable", "adj", "/poʊstˈpoʊnəbəl/", "có thể trì hoãn lại được"),
    ("078231", "postponed", "verb", "/poʊstˈpoʊnd/", "đã hoãn lại, dời sang lúc khác"),
    ("078232", "postponer", "noun", "/poʊstˈpoʊnər/", "người trì hoãn, hay lần lữa"),
    ("078233", "postpones", "verb", "/poʊstˈpoʊnz/", "hoãn lại, dời sang lúc khác"),
    ("078234", "postponing", "verb", "/poʊstˈpoʊnɪŋ/", "hoãn lại, dời sang lúc khác"),
    ("078235", "postpose", "verb", "/ˌpoʊstˈpoʊz/", "đặt ở vị trí phía sau (ngôn ngữ)"),
    ("078236", "postpositional", "adj", "/ˌpoʊstpəˈzɪʃənəl/", "đứng sau danh từ (giới từ hậu vị)"),
    ("078237", "postpositionally", "adv", "/ˌpoʊstpəˈzɪʃənəli/", "theo vị trí đứng sau (ngữ pháp)"),
    ("078238", "postpositively", "adv", "/ˌpoʊstˈpɒzɪtɪvli/", "ở vị trí đứng sau danh từ"),
    ("078239", "postprandially", "adv", "/ˌpoʊstˈprændiəli/", "vào lúc sau bữa ăn"),
    ("078240", "postrouting", "noun", "/ˌpoʊstˈruːtɪŋ/", "hậu định tuyến (mạng máy tính)"),
    ("078241", "posts", "verb", "/poʊsts/", "đăng bài; gửi thư; niêm yết; cử đi"),
    ("078242", "postscripts", "noun", "/ˈpoʊstˌskrɪpts/", "phần tái bút (P.S.); đoạn hậu ký"),
    ("078243", "postulancy", "noun", "/ˈpɒstjʊlənsi/", "giai đoạn thỉnh sinh (tu viện)"),
    ("078244", "postulantship", "noun", "/ˈpɒstjʊləntʃɪp/", "thời kỳ làm thỉnh sinh (tu viện)"),
    ("078245", "postulated", "verb", "/ˈpɑːstʃəˌleɪtɪd/", "đã đặt làm giả thuyết, tiên đề"),
    ("078246", "postulates", "verb", "/ˈpɑːstʃəˌleɪts/", "đặt làm giả thuyết, đưa ra tiên đề"),
    ("078247", "postulating", "verb", "/ˈpɑːstʃəˌleɪtɪŋ/", "đặt làm giả thuyết, đưa ra tiên đề"),
    ("078248", "postulational", "adj", "/ˌpɑːstʃəˈleɪʃənəl/", "thuộc giả thuyết hoặc tiên đề"),
    ("078249", "postulator", "noun", "/ˈpɑːstʃəleɪtər/", "người đề cử; người xin phong thánh"),
    ("078250", "postured", "verb", "/ˈpɑːstʃərd/", "đã làm bộ, ra vẻ; đứng giữ tư thế"),
    ("078251", "posturer", "noun", "/ˈpɑːstʃərər/", "kẻ làm bộ làm tịch; diễn viên uốn"),
    ("078252", "postures", "verb", "/ˈpɑːstʃərz/", "làm bộ, ra vẻ; đứng giữ tư thế"),
    ("078253", "posturist", "noun", "/ˈpɑːstʃərɪst/", "kẻ làm bộ; diễn viên uốn dẻo"),
    ("078254", "potability", "noun", "/ˌpoʊtəˈbɪlɪti/", "tính uống được an toàn (nước)"),
    ("078255", "potableness", "noun", "/ˈpoʊtəbəlnəs/", "tính uống được an toàn (nước)"),
    ("078256", "potables", "noun", "/ˈpoʊtəbəlz/", "đồ uống, thức uống (từ trang trọng)"),
    ("078257", "potamic", "adj", "/pəˈtæmɪk/", "thuộc về sông ngòi"),
    ("078258", "potamogale", "noun", "/ˌpɒtəˈmɒɡəli/", "chi rái cá chuột chũi châu Phi"),
    ("078259", "potamogalidae", "noun", "/ˌpɒtəmoʊˈɡælɪdiː/", "họ Chuột chũi rái cá châu Phi"),
    ("078260", "potamogetonaceae", "noun", "/ˌpɒtəmoʊdʒiːtəˈneɪsiː/", "họ Rong mái chèo (Potamogeton)"),
    ("078261", "potamology", "noun", "/ˌpɒtəˈmɒlədʒi/", "sông ngòi học (thủy văn sông)"),
    ("078262", "potamophis", "noun", "/pəˈtæməfɪs/", "chi rắn đất Bắc Mỹ (Potamophis)"),
    ("078263", "potass", "noun", "/ˈpɒtæs/", "bồ tạt, kali cacbonat (potash cổ)"),
    ("078264", "potassic", "adj", "/pəˈtæsɪk/", "có chứa kali"),
    ("078265", "potation", "noun", "/poʊˈteɪʃən/", "sự uống rượu; đồ uống (văn học)"),
    ("078266", "potatoes", "noun", "/pəˈteɪtoʊz/", "củ khoai tây"),
    ("078267", "potatory", "adj", "/ˈpoʊtətɔːri/", "thuộc việc uống rượu; để uống"),
    ("078268", "potbound", "adj", "/ˈpɑːtbaʊnd/", "bị bó rễ chật trong chậu (cây)"),
    ("078269", "potboy", "noun", "/ˈpɑːtbɔɪ/", "cậu phụ bàn quán rượu (Anh cũ)"),
    ("078270", "potd", "noun", "/ˌpiːoʊtiːˈdiː/", "bức ảnh của ngày (viết tắt POTD)"),
    ("078271", "potds", "noun", "/ˌpiːoʊtiːˈdiːz/", "bức ảnh của ngày (viết tắt POTD)"),
    ("078272", "potencies", "noun", "/ˈpoʊtənsiz/", "hiệu lực mạnh; tiềm năng; công hiệu"),
    ("078273", "potentialise", "verb", "/pəˈtɛnʃəlaɪz/", "tạo tiềm năng; tăng hiệu lực thuốc"),
    ("078274", "potentialities", "noun", "/pəˌtɛnʃiˈælɪtiz/", "tiềm năng, khả năng tiềm ẩn"),
    ("078275", "potentialize", "verb", "/pəˈtɛnʃəlaɪz/", "tạo tiềm năng; tăng hiệu lực thuốc"),
    ("078276", "potentiometers", "noun", "/pəˌtɛnʃiˈɒmɪtərz/", "chiết áp (biến trở); điện thế kế"),
    ("078277", "potentiometric", "adj", "/pəˌtɛnʃioʊˈmɛtrɪk/", "thuộc phép đo điện thế"),
    ("078278", "potentness", "noun", "/ˈpoʊtəntnəs/", "sức mạnh, hiệu lực hùng mạnh"),
    ("078279", "poterium", "noun", "/poʊˈtɪriəm/", "chi cây địa du gai (Sarcopoterium)"),
    ("078280", "potheen", "noun", "/pɒˈtʃiːn/", "rượu khoai tây nấu lậu (Ireland)"),
    ("078281", "potherb", "noun", "/ˈpɑːtˌɜːrb/", "cây rau nấu canh; rau thơm gia vị"),
    ("078282", "pothered", "verb", "/ˈpɑːðərd/", "đã làm bận tâm, quấy rầy lo âu"),
    ("078283", "pothering", "verb", "/ˈpɑːðərɪŋ/", "làm bận tâm, quấy rầy lo âu"),
    ("078284", "pothers", "verb", "/ˈpɑːðərz/", "làm bận tâm, quấy rầy lo âu"),
    ("078285", "potholer", "noun", "/ˈpɑːtˌhoʊlər/", "người thám hiểm hang động ngầm"),
    ("078286", "potholing", "noun", "/ˈpɑːtˌhoʊlɪŋ/", "môn thám hiểm hang động ngầm"),
    ("078287", "pothook", "noun", "/ˈpɑːthʊk/", "móc treo nồi trên bếp lửa; nét móc"),
    ("078288", "pothouse", "noun", "/ˈpɑːthaʊs/", "quán rượu bình dân, quán bia (cũ)"),
    ("078289", "pothunter", "noun", "/ˈpɑːtˌhʌntər/", "kẻ đào bới trộm cổ vật; săn giải"),
    ("078290", "potman", "noun", "/ˈpɑːtmən/", "người phục vụ quán rượu (Anh cũ)"),
    ("078291", "potomania", "noun", "/ˌpoʊtəˈmeɪniə/", "chứng nghiện rượu nặng (y học)"),
    ("078292", "potoroinae", "noun", "/ˌpɒtəˈroʊɪniː/", "phân họ Chuột túi đuôi chuột Úc"),
    ("078293", "potoroo", "noun", "/ˌpɒtəˈruː/", "chuột túi đuôi chuột Úc (potoroo)"),
    ("078294", "potorous", "noun", "/pəˈtɔːrəs/", "chi chuột túi đuôi chuột Potorous"),
    ("078295", "pots", "verb", "/pɑːts/", "trồng vào chậu; đánh bi vào lỗ"),
    ("078296", "pott", "noun", "/pɑːt/", "giấy khổ pott (khổ giấy cũ Anh)"),
    ("078297", "pottered", "verb", "/ˈpɑːtərd/", "đã làm lặt vặt chậm rãi, lề mề"),
    ("078298", "potterer", "noun", "/ˈpɑːtərər/", "người làm lặt vặt lề mề chậm chạp"),
    ("078299", "pottering", "verb", "/ˈpɑːtərɪŋ/", "làm lặt vặt chậm rãi, lề mề (Anh)"),
    ("078300", "potters", "verb", "/ˈpɑːtərz/", "làm lặt vặt chậm rãi, lề mề (Anh)"),
    ("078301", "potting", "verb", "/ˈpɑːtɪŋ/", "trồng vào chậu; đánh bi vào lỗ"),
    ("078302", "potyokin", "noun", "/pɒtˈjɒkɪn/", "tướng Nga Potemkin (biến thể)"),
]

with open("scratch/b36_r07_raw_p3.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r07_p3.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r07_p3 saved OK")
