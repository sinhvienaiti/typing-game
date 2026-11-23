import json

rows = [
    ("077603", "pogonophoran", "noun", "/ˌpoʊɡəˈnɒfərən/", "giun râu biển (ngành Pogonophora)"),
    ("077604", "pogostemon", "noun", "/ˌpoʊɡəˈstiːmən/", "chi cây hoắc hương (Pogostemon)"),
    ("077605", "pogromist", "noun", "/ˈpɒɡrəmɪst/", "kẻ tham gia cuộc thảm sát pogrom"),
    ("077606", "pogy", "noun", "/ˈpoʊɡi/", "tiền trợ cấp thất nghiệp (Canada)"),
    ("077607", "poikilocyte", "noun", "/ˈpɔɪkɪləˌsaɪt/", "hồng cầu biến dạng bất thường"),
    ("077608", "poikilotherm", "noun", "/pɔɪˈkɪləθɜːrm/", "động vật biến nhiệt (máu lạnh)"),
    ("077609", "poikilothermic", "adj", "/pɔɪˌkɪləˈθɜːrmɪk/", "biến nhiệt (thân nhiệt đổi theo)"),
    ("077610", "poikilothermism", "noun", "/pɔɪˈkɪləθɜːrmɪzəm/", "tính trạng biến nhiệt (máu lạnh)"),
    ("077611", "poikilothermous", "adj", "/pɔɪˌkɪləˈθɜːrməs/", "biến nhiệt (thân nhiệt đổi theo)"),
    ("077612", "poind", "verb", "/pɔɪnd/", "tịch biên tài sản xiết nợ (luật cổ)"),
    ("077613", "pointal", "noun", "/ˈpɔɪntəl/", "vòm nhọn kiến trúc; bút khắc nhọn"),
    ("077614", "pointel", "noun", "/ˈpɔɪntəl/", "dùi khắc nhọn; sàn lát ô vuông"),
    ("077615", "pointillistic", "adj", "/ˌpwæntɪˈlɪstɪk/", "thuộc trường phái điểm họa"),
    ("077616", "pointing", "noun", "/ˈpɔɪntɪŋ/", "sự trỏ; việc trít mạch vữa tường"),
    ("077617", "pointrel", "noun", "/ˈpɔɪntrəl/", "dụng cụ khắc nhọn trên sáp, gỗ"),
    ("077618", "points", "verb", "/pɔɪnts/", "chỉ trỏ; hướng mũi về; nhấn mạnh"),
    ("077619", "pointsman", "noun", "/ˈpɔɪntsmən/", "cảnh sát giao thông; người gác ghi"),
    ("077620", "pointwise", "adv", "/ˈpɔɪntwaɪz/", "theo từng điểm (toán học)"),
    ("077621", "poises", "verb", "/ˈpɔɪzɪz/", "giữ thăng bằng; sẵn sàng tư thế"),
    ("077622", "poising", "verb", "/ˈpɔɪzɪŋ/", "giữ thăng bằng; sẵn sàng tư thế"),
    ("077623", "poisonberry", "noun", "/ˈpɔɪzənˌbɛri/", "cây mọng độc (Solanum)"),
    ("077624", "poisoned", "verb", "/ˈpɔɪzənd/", "đã đầu độc; đã làm ô nhiễm, hư hỏng"),
    ("077625", "poisoners", "noun", "/ˈpɔɪzənərz/", "kẻ đầu độc"),
    ("077626", "poisonousness", "noun", "/ˈpɔɪzənəsnəs/", "tính chất độc hại, độc tính"),
    ("077627", "poisons", "verb", "/ˈpɔɪzənz/", "đầu độc; làm ô nhiễm, làm hư hỏng"),
    ("077628", "poivrade", "noun", "/pwɑːˈvrɑːd/", "nước sốt tiêu poivrade (Pháp)"),
    ("077629", "poked", "verb", "/poʊkt/", "đã chọc, thọc; lục lọi"),
    ("077630", "pokes", "verb", "/poʊks/", "chọc, thọc; lục lọi, thò ra"),
    ("077631", "pokeweeds", "noun", "/ˈpoʊkwiːdz/", "cây thương lục Mỹ (pokeweed)"),
    ("077632", "pokeys", "noun", "/ˈpoʊkiz/", "nhà tù, nhà giam (tiếng lóng)"),
    ("077633", "pokie", "noun", "/ˈpoʊki/", "máy đánh bạc xèng (Úc); nhà tù"),
    ("077634", "pokily", "adv", "/ˈpoʊkɪli/", "chật chội, lề mề chậm chạp"),
    ("077635", "pokiness", "noun", "/ˈpoʊkinəs/", "sự chật chội tù túng; tính chậm rì"),
    ("077636", "pokomo", "noun", "/pəˈkoʊmoʊ/", "người Pokomo; tiếng Pokomo (Kenya)"),
    ("077637", "polacca", "noun", "/pəˈlɑːkə/", "thuyền buôn ba buồm Địa Trung Hải"),
    ("077638", "polacre", "noun", "/pəˈlɑːkər/", "thuyền buôn ba buồm Địa Trung Hải"),
    ("077639", "polander", "noun", "/ˈpoʊləndər/", "người Ba Lan (từ cổ)"),
    ("077640", "polanisia", "noun", "/ˌpɒləˈnɪʒə/", "chi cây mần ri Bắc Mỹ (Polanisia)"),
    ("077641", "polarimeters", "noun", "/ˌpoʊləˈrɪmɪtərz/", "phân cực kế (máy đo góc quay cực)"),
    ("077642", "polarimetric", "adj", "/ˌpoʊlərɪˈmɛtrɪk/", "thuộc phép đo góc phân cực"),
    ("077643", "polarisable", "adj", "/ˈpoʊləraɪzəbəl/", "có thể phân cực được"),
    ("077644", "polariscope", "noun", "/poʊˈlɛrəˌskoʊp/", "kính kiểm tra ánh sáng phân cực"),
    ("077645", "polarised", "verb", "/ˈpoʊləraɪzd/", "đã phân cực hóa; gây chia rẽ sâu"),
    ("077646", "polariser", "noun", "/ˈpoʊləraɪzər/", "bộ lọc phân cực (quang học)"),
    ("077647", "polarises", "verb", "/ˈpoʊləraɪzɪz/", "làm phân cực; gây chia rẽ sâu sắc"),
    ("077648", "polarising", "verb", "/ˈpoʊləraɪzɪŋ/", "làm phân cực; gây chia rẽ sâu sắc"),
    ("077649", "polarizability", "noun", "/ˌpoʊləraɪzəˈbɪlɪti/", "độ phân cực hóa (vật lý, hóa học)"),
    ("077650", "polarizable", "adj", "/ˈpoʊləraɪzəbəl/", "có thể phân cực được"),
    ("077651", "polarized", "verb", "/ˈpoʊləˌraɪzd/", "đã phân cực hóa; gây chia rẽ sâu"),
    ("077652", "polarizer", "noun", "/ˈpoʊləˌraɪzər/", "bộ lọc phân cực (quang học)"),
    ("077653", "polarizes", "verb", "/ˈpoʊləˌraɪzɪz/", "làm phân cực; gây chia rẽ sâu sắc"),
    ("077654", "polarizing", "verb", "/ˈpoʊləˌraɪzɪŋ/", "làm phân cực; gây chia rẽ sâu sắc"),
    ("077655", "polarographic", "adj", "/ˌpoʊlərəˈɡræfɪk/", "thuộc phép phân tích cực phổ"),
    ("077656", "polarography", "noun", "/ˌpoʊləˈrɑːɡrəfi/", "phép phân tích cực phổ (điện hóa)"),
    ("077657", "polatouche", "noun", "/ˈpɒlətuːʃ/", "sóc bay châu Âu (Pteromys)"),
    ("077658", "poleax", "noun", "/ˈpoʊlæks/", "rìu chiến cán dài; rìu giết mổ"),
    ("077659", "poled", "verb", "/poʊld/", "đã chống sào đẩy thuyền; dựng cọc"),
    ("077660", "polemicise", "verb", "/pəˈlɛmɪsaɪz/", "tranh luận gay gắt, bút chiến"),
    ("077661", "polemicize", "verb", "/pəˈlɛmɪsaɪz/", "tranh luận gay gắt, bút chiến"),
    ("077662", "polemise", "verb", "/ˈpɒlɪmaɪz/", "tranh luận gay gắt, bút chiến"),
    ("077663", "polemist", "noun", "/ˈpɒlɪmɪst/", "nhà bút chiến, người tranh luận"),
    ("077664", "polemize", "verb", "/ˈpɒlɪmaɪz/", "tranh luận gay gắt, bút chiến"),
    ("077665", "polemoniaceae", "noun", "/ˌpɒlɪmoʊniˈeɪsiː/", "họ Hoa chuông (Polemoniaceae)"),
    ("077666", "polemoniacecous", "adj", "/ˌpɒlɪmoʊniˈeɪʃəs/", "thuộc họ Hoa chuông (biến thể)"),
    ("077667", "polemoniaceous", "adj", "/ˌpɒlɪmoʊniˈeɪʃəs/", "thuộc họ Hoa chuông Polemoniaceae"),
    ("077668", "polemoniales", "noun", "/ˌpɒlɪmoʊniˈeɪliːz/", "bộ Hoa chuông (Polemoniales)"),
    ("077669", "polemonium", "noun", "/ˌpɒlɪˈmoʊniəm/", "chi hoa thang Jacob (Polemonium)"),
    ("077670", "poler", "noun", "/ˈpoʊlər/", "người chống sào; ngựa gọng xe"),
    ("077671", "poles", "verb", "/poʊlz/", "chống sào đẩy thuyền; dựng cọc đỡ"),
    ("077672", "poleward", "adv", "/ˈpoʊlwərd/", "hướng về phía cực (Bắc hoặc Nam)"),
    ("077673", "polianthes", "noun", "/ˌpɒliˈænθiːz/", "chi hoa huệ trắng (Polianthes)"),
    ("077674", "polibureau", "noun", "/ˈpɒlɪˌbjʊroʊ/", "Bộ Chính trị (cách viết biến thể)"),
    ("077675", "poliburo", "noun", "/ˈpɒlɪˌbjʊroʊ/", "Bộ Chính trị (cách viết biến thể)"),
    ("077676", "policed", "verb", "/pəˈliːst/", "đã tuần tra, kiểm soát, giữ trật tự"),
    ("077677", "polices", "verb", "/pəˈliːsɪz/", "tuần tra, kiểm soát, giữ trật tự"),
    ("077678", "policewomen", "noun", "/pəˈliːsˌwɪmɪn/", "nữ cảnh sát"),
    ("077679", "policing", "verb", "/pəˈliːsɪŋ/", "tuần tra, kiểm soát, giữ trật tự"),
    ("077680", "policlinic", "noun", "/ˌpɒlɪˈklɪnɪk/", "phòng khám đa khoa ngoại trú"),
    ("077681", "policymaker", "noun", "/ˈpɑːləsiˌmeɪkər/", "nhà hoạch định chính sách"),
    ("077682", "policymaking", "noun", "/ˈpɑːləsiˌmeɪkɪŋ/", "việc hoạch định chính sách"),
    ("077683", "poling", "verb", "/ˈpoʊlɪŋ/", "chống sào đẩy thuyền; dựng cọc đỡ"),
    ("077684", "poliomyelitic", "adj", "/ˌpoʊlioʊmaɪəˈlɪtɪk/", "thuộc bệnh bại liệt (y học)"),
    ("077685", "polioptila", "noun", "/ˌpɒliɒpˈtɪlə/", "chi chim bắt muỗi (Polioptila)"),
    ("077686", "poliosis", "noun", "/ˌpɒliˈoʊsɪs/", "chứng bạc tóc từng đám (y học)"),
    ("077687", "poliplicate", "adj", "/ˌpɒlɪˈplɪkɪt/", "có nhiều nếp gấp dọc"),
    ("077688", "polis", "noun", "/ˈpɒlɪs/", "thành bang (Hy Lạp cổ đại)"),
    ("077689", "polishers", "noun", "/ˈpɑːlɪʃərz/", "thợ đánh bóng; máy đánh bóng"),
    ("077690", "polishes", "noun", "/ˈpɑːlɪʃɪz/", "xi đánh bóng; sự đánh bóng"),
    ("077691", "politesses", "noun", "/ˌpɒlɪˈtɛsɪz/", "sự lịch thiệp nhã nhặn"),
    ("077692", "politicalisms", "noun", "/pəˈlɪtɪkəlɪzəmz/", "chủ nghĩa chính trị hóa"),
    ("077693", "politicalization", "noun", "/pəˌlɪtɪkəlaɪˈzeɪʃən/", "sự chính trị hóa"),
    ("077694", "politicalize", "verb", "/pəˈlɪtɪkəlaɪz/", "chính trị hóa"),
    ("077695", "politicians", "noun", "/ˌpɑːlɪˈtɪʃənz/", "chính trị gia, chính khách"),
    ("077696", "politicised", "verb", "/pəˈlɪtɪsaɪzd/", "đã chính trị hóa"),
    ("077697", "politicises", "verb", "/pəˈlɪtɪsaɪzɪz/", "chính trị hóa"),
    ("077698", "politicising", "verb", "/pəˈlɪtɪsaɪzɪŋ/", "chính trị hóa"),
    ("077699", "politicization", "noun", "/pəˌlɪtɪsɪˈzeɪʃən/", "sự chính trị hóa"),
    ("077700", "politicized", "verb", "/pəˈlɪtɪˌsaɪzd/", "đã chính trị hóa"),
    ("077701", "politicizes", "verb", "/pəˈlɪtɪˌsaɪzɪz/", "chính trị hóa"),
    ("077702", "politicizing", "verb", "/pəˈlɪtɪˌsaɪzɪŋ/", "chính trị hóa"),
]

with open("scratch/b36_r06_raw_p2.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r06_p2.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r06_p2 saved OK")
