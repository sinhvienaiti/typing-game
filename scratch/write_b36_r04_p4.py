import json

rows = [
    ("076803", "piroshki", "noun", "/pɪˈrɒʃki/", "bánh nhân piroshki (ẩm thực Nga)"),
    ("076804", "pirouetted", "verb", "/ˌpɪruˈɛtɪd/", "đã xoay tròn một chân (múa ba-lê)"),
    ("076805", "pirouettes", "verb", "/ˌpɪruˈɛts/", "xoay tròn một chân (múa ba-lê)"),
    ("076806", "pirouetting", "verb", "/ˌpɪruˈɛtɪŋ/", "xoay tròn một chân (múa ba-lê)"),
    ("076807", "pisanosaur", "noun", "/pɪˈsænəˌsɔːr/", "khủng long Pisanosaurus"),
    ("076808", "pisanosaurus", "noun", "/pɪˌsænəˈsɔːrəs/", "khủng long Pisanosaurus"),
    ("076809", "piscary", "noun", "/ˈpɪskəri/", "quyền đánh bắt cá trong vùng nước"),
    ("076810", "piscatorially", "adv", "/ˌpɪskəˈtɔːriəli/", "về mặt nghề cá, thú câu cá"),
    ("076811", "piscatory", "adj", "/ˈpɪskətɔːri/", "thuộc nghề cá, thú câu cá"),
    ("076812", "piscicultural", "adj", "/ˌpɪsɪˈkʌltʃərəl/", "thuộc nghề nuôi trồng thủy sản, cá"),
    ("076813", "pisciculture", "noun", "/ˈpɪsɪˌkʌltʃər/", "nghề nuôi cá, ngư nghiệp"),
    ("076814", "pisciculturist", "noun", "/ˌpɪsɪˈkʌltʃərɪst/", "người nuôi cá chuyên nghiệp"),
    ("076815", "piscidia", "noun", "/pɪˈsɪdiə/", "chi cây độc cá Jamaica (Piscidia)"),
    ("076816", "piscina", "noun", "/pɪˈsaɪnə/", "ao cá; bồn rửa lễ nhà thờ"),
    ("076817", "piscinae", "noun", "/pɪˈsaɪniː/", "ao cá; bồn rửa lễ nhà thờ"),
    ("076818", "piscinal", "adj", "/ˈpɪsɪnəl/", "thuộc ao cá hoặc bể rửa lễ"),
    ("076819", "pish", "intj", "/pɪʃ/", "xì, hừ (tỏ ý khinh thường)"),
    ("076820", "pishogue", "noun", "/pɪˈʃoʊɡ/", "ma thuật, phép phù thủy (Ireland)"),
    ("076821", "pismire", "noun", "/ˈpɪsmaɪər/", "con kiến (từ cổ)"),
    ("076822", "pisolite", "noun", "/ˈpaɪsəlaɪt/", "đá vôi trứng cá lớn (pisolit)"),
    ("076823", "pisolitic", "adj", "/ˌpaɪsəˈlɪtɪk/", "thuộc đá pisolit"),
    ("076824", "pisos", "noun", "/ˈpiːsoʊz/", "tầng nhà; căn hộ (Tây Ban Nha)"),
    ("076825", "pissabed", "noun", "/ˈpɪsəbɛd/", "cây bồ công anh (từ lóng cũ)"),
    ("076826", "pisses", "verb", "/ˈpɪsɪz/", "đi tiểu (thô tục); mưa xối xả"),
    ("076827", "pissis", "noun", "/ˈpɪsɪs/", "núi Monte Pissis (dãy Andes)"),
    ("076828", "pissoir", "noun", "/pɪsˈwɑːr/", "nhà tiểu công cộng (kiểu Pháp)"),
    ("076829", "pist", "noun", "/pɪst/", "tiếng suỵt gọi nhỏ; dấu vết (cổ)"),
    ("076830", "pistia", "noun", "/ˈpɪstiə/", "chi bèo cái (Pistia)"),
    ("076831", "pistillary", "adj", "/ˈpɪstəˌlɛri/", "thuộc nhụy hoa (thực vật học)"),
    ("076832", "pistillidium", "noun", "/ˌpɪstɪˈlɪdiəm/", "túi noãn, cơ quan cái (thực vật)"),
    ("076833", "pistilliferous", "adj", "/ˌpɪstɪˈlɪfərəs/", "có mang nhụy hoa (thực vật học)"),
    ("076834", "pistillode", "noun", "/ˈpɪstɪloʊd/", "nhụy lép, nhụy thoái hóa"),
    ("076835", "pistillody", "noun", "/ˈpɪstɪlədi/", "hiện tượng hóa nhụy bất thường"),
    ("076836", "pistolade", "noun", "/ˌpɪstəˈleɪd/", "phát súng ngắn; loạt súng lục"),
    ("076837", "pistole", "noun", "/pɪˈstoʊl/", "đồng tiền vàng pistole (châu Âu cổ)"),
    ("076838", "pistoleer", "noun", "/ˌpɪstəˈlɪr/", "tay súng lục; người mang súng ngắn"),
    ("076839", "pistolet", "noun", "/ˈpɪstəlɛt/", "súng ngắn bỏ túi cỡ nhỏ (cổ)"),
    ("076840", "pistolgraph", "noun", "/ˈpɪstəlɡræf/", "máy ảnh cầm tay kiểu súng cổ"),
    ("076841", "pitahayas", "noun", "/ˌpɪtəˈhaɪəz/", "quả thanh long (pitahaya)"),
    ("076842", "pitaya", "noun", "/pɪˈtaɪə/", "cây và quả thanh long"),
    ("076843", "pitayas", "noun", "/pɪˈtaɪəz/", "quả thanh long (pitaya)"),
    ("076844", "pitcherful", "noun", "/ˈpɪtʃərfʊl/", "lượng đầy một bình rót"),
    ("076845", "pitches", "verb", "/ˈpɪtʃɪz/", "ném bóng; dựng trại; lao chao đảo"),
    ("076846", "pitchforked", "verb", "/ˈpɪtʃfɔːrkt/", "đã hất bằng chĩa; đẩy vội vào ghế"),
    ("076847", "pitchforking", "verb", "/ˈpɪtʃfɔːrkɪŋ/", "hất bằng chĩa; đẩy vội vào ghế"),
    ("076848", "pitchforks", "verb", "/ˈpɪtʃˌfɔːrks/", "hất bằng chĩa; đẩy vội vào ghế"),
    ("076849", "pitchiness", "noun", "/ˈpɪtʃinəs/", "màu đen như hắc ín; chất nhựa thông"),
    ("076850", "pitchmen", "noun", "/ˈpɪtʃmən/", "người bán hàng rong miệng lưỡi"),
    ("076851", "pitchstone", "noun", "/ˈpɪtʃstoʊn/", "đá thủy tinh núi lửa hắc diện"),
    ("076852", "piteousness", "noun", "/ˈpɪtiəsnəs/", "tình trạng đáng thương, thảm thương"),
    ("076853", "pithecan", "noun", "/pɪˈθiːkən/", "người vượn hóa thạch"),
    ("076854", "pithecanthrope", "noun", "/ˌpɪθɪˈkænθroʊp/", "người vượn cổ đại (hóa thạch)"),
    ("076855", "pithecellobium", "noun", "/ˌpɪθɪsɪˈloʊbiəm/", "chi cây keo me tây Pithecellobium"),
    ("076856", "pithecia", "noun", "/pɪˈθiːʃə/", "chi khỉ saki Nam Mỹ (Pithecia)"),
    ("076857", "pithecoil", "adj", "/pɪˈθiːkɔɪl/", "giống loài khỉ vượn"),
    ("076858", "pithecolobium", "noun", "/ˌpɪθɪkəˈloʊbiəm/", "chi cây keo me tây Pithecellobium"),
    ("076859", "pithiness", "noun", "/ˈpɪθinəs/", "tính súc tích, cô đọng đầy ý nghĩa"),
    ("076860", "pithless", "adj", "/ˈpɪθləs/", "không có lõi; thiếu sức sống, nhạt"),
    ("076861", "pitiableness", "noun", "/ˈpɪtiəbəlnəs/", "tình cảnh đáng thương, thảm hại"),
    ("076862", "pitiably", "adv", "/ˈpɪtiəbli/", "một cách đáng thương, thảm hại"),
    ("076863", "pitied", "verb", "/ˈpɪtid/", "đã thương hại, xót thương"),
    ("076864", "pities", "verb", "/ˈpɪtiz/", "thương hại, xót thương"),
    ("076865", "pitifulness", "noun", "/ˈpɪtɪfəlnəs/", "tình cảnh thảm hại; lòng thương xót"),
    ("076866", "pitilessness", "noun", "/ˈpɪtɪləsnəs/", "sự tàn nhẫn, nhẫn tâm vô tình"),
    ("076867", "pitmen", "noun", "/ˈpɪtmən/", "thợ mỏ hầm lò; thanh truyền cơ khí"),
    ("076868", "pitpan", "noun", "/ˈpɪtpæn/", "thuyền độc mộc đáy bằng (Trung Mỹ)"),
    ("076869", "pitprop", "noun", "/ˈpɪtprɒp/", "cột gỗ chống nóc hầm lò"),
    ("076870", "pitressin", "noun", "/pɪˈtrɛsɪn/", "hoóc-môn chống lợi tiểu pitressin"),
    ("076871", "pits", "verb", "/pɪts/", "đào hố; tách hạt quả; cho đấu nhau"),
    ("076872", "pitsaw", "noun", "/ˈpɪtsɔː/", "cưa xẻ gỗ hai người (trên hố cưa)"),
    ("076873", "pittidae", "noun", "/ˈpɪtɪdiː/", "họ Chim đuôi cụt (Pittidae)"),
    ("076874", "pittile", "noun", "/ˈpɪtaɪl/", "khán giả ngồi ghế tầng trệt giá rẻ"),
    ("076875", "pittite", "noun", "/ˈpɪtaɪt/", "khán giả ngồi ghế tầng trệt giá rẻ"),
    ("076876", "pituitous", "adj", "/pɪˈtjuːɪtəs/", "đầy dịch nhầy, giống đờm dãi"),
    ("076877", "pituitrin", "noun", "/pɪˈtjuːɪtrɪn/", "hoóc-môn tuyến yên pituitrin"),
    ("076878", "pituiturism", "noun", "/pɪˈtjuːɪtərɪzəm/", "hiện tượng rối loạn tuyến yên"),
    ("076879", "pituophis", "noun", "/pɪˈtjuːəfɪs/", "chi rắn bò gopher (Pituophis)"),
    ("076880", "pityariasis", "noun", "/ˌpɪtɪˈraɪəsɪs/", "bệnh vảy phấn (da liễu)"),
    ("076881", "pitying", "verb", "/ˈpɪtiɪŋ/", "thương hại, xót thương"),
    ("076882", "pitymys", "noun", "/ˈpɪtɪmɪs/", "chi chuột đồng thông (Pitymys)"),
    ("076883", "pityrogramma", "noun", "/ˌpɪtɪroʊˈɡræmə/", "chi dương xỉ phấn Pityrogramma"),
    ("076884", "pivotable", "adj", "/ˈpɪvətəbəl/", "có thể xoay quanh trục"),
    ("076885", "pivotally", "adv", "/ˈpɪvətəli/", "ở vị trí then chốt, mấu chốt"),
    ("076886", "pivoted", "verb", "/ˈpɪvətɪd/", "đã xoay quanh trục; chuyển hướng"),
    ("076887", "pivoting", "verb", "/ˈpɪvətɪŋ/", "xoay quanh trục; chuyển hướng"),
    ("076888", "pivots", "verb", "/ˈpɪvəts/", "xoay quanh trục; chuyển hướng"),
    ("076889", "pivottable", "noun", "/ˈpɪvətˌteɪbəl/", "bảng tổng hợp dữ liệu (PivotTable)"),
    ("076890", "pixilation", "noun", "/ˌpɪksɪˈleɪʃən/", "sự ngơ ngẩn; hoạt họa từng khung"),
    ("076891", "pixyish", "adj", "/ˈpɪksiɪʃ/", "tinh nghịch như tiểu tiên"),
    ("076892", "pizzle", "noun", "/ˈpɪzəl/", "roi gân bò; dương vật thú"),
    ("076893", "pk", "noun", "/ˌpiːˈkeɪ/", "viết tắt công viên Park; phạt đền"),
    ("076894", "pkg", "noun", "/ˈpækɪdʒ/", "viết tắt gói hàng (package)"),
    ("076895", "pkt", "noun", "/ˈpækɪt/", "viết tắt gói nhỏ (packet)"),
    ("076896", "pl", "noun", "/ˌpiːˈɛl/", "viết tắt Place; Ba Lan; số nhiều"),
    ("076897", "pla", "noun", "/ˌpiːɛlˈeɪ/", "nhựa PLA; mảng logic PLA; quân PLA"),
    ("076898", "placability", "noun", "/ˌplækəˈbɪlɪti/", "tính dễ nguôi giận, dễ xoa dịu"),
    ("076899", "placable", "adj", "/ˈplækəbəl/", "dễ nguôi giận, dễ xoa dịu"),
    ("076900", "placably", "adv", "/ˈplækəbli/", "một cách ôn hòa, dễ nguôi giận"),
    ("076901", "placarded", "verb", "/ˈplækɑːrdɪd/", "đã dán áp phích, biển hiệu"),
    ("076902", "placarder", "noun", "/ˈplækɑːrdər/", "người đi dán áp phích, biển hiệu"),
]

with open("scratch/b36_r04_raw_p4.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r04_p4.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r04_p4 saved OK")
