import json

records = [
    ("080903", "quadriplane", "noun", "/ˈkwɑːdrəˌpleɪn/", "máy bay thử nghiệm bốn tầng cánh"),
    ("080904", "quadripolar", "adj", "/ˌkwɑːdrəˈpoʊlər/", "có bốn cực (từ trường, phân bào)"),
    ("080905", "quadripole", "noun", "/ˈkwɑːdrəˌpoʊl/", "mạng điện bốn cực, tứ cực"),
    ("080906", "quadrisonic", "adj", "/ˌkwɑːdrəˈsɑːnɪk/", "thuộc hệ thống âm thanh bốn kênh"),
    ("080907", "quadrisyllabic", "adj", "/ˌkwɑːdrəsəˈlæbɪk/", "gồm bốn âm tiết (từ vựng học)"),
    ("080908", "quadrisyllable", "noun", "/ˈkwɑːdrəˌsɪləbəl/", "từ có bốn âm tiết"),
    ("080909", "quadrivalence", "noun", "/ˌkwɑːdrəˈveɪləns/", "hóa trị bốn (hóa học)"),
    ("080910", "quadrivalency", "noun", "/ˌkwɑːdrəˈveɪlənsi/", "tính hóa trị bốn (hóa học)"),
    ("080911", "quadrivalent", "adj", "/ˌkwɑːdrəˈveɪlənt/", "có hóa trị bốn (hóa học)"),
    ("080912", "quadrivia", "noun", "/kwɑːˈdrɪviə/", "bốn môn toán học Trung cổ"),
    ("080913", "quadrivial", "adj", "/kwɑːˈdrɪviəl/", "có bốn đường giao nhau; tứ khoa"),
    ("080914", "quadrivoltine", "adj", "/ˌkwɑːdrəˈvɑːltiːn/", "sinh sản bốn lứa một năm"),
    ("080915", "quadrophonic", "adj", "/ˌkwɑːdrəˈfɑːnɪk/", "thuộc âm thanh vòm bốn kênh"),
    ("080916", "quadrophony", "noun", "/kwɑːˈdrɑːfəni/", "kỹ thuật ghi phát âm thanh bốn kênh"),
    ("080917", "quadrumane", "noun", "/ˈkwɑːdrəˌmeɪn/", "động vật bộ Bốn tay (linh trưởng)"),
    ("080918", "quadrumanous", "adj", "/kwɑːˈdruːmənəs/", "có bốn chân cầm nắm như tay"),
    ("080919", "quadrumvirate", "noun", "/kwɑːˈdrʌmvərɪt/", "tứ đầu chế, nhóm bốn người"),
    ("080920", "quadrupled", "verb", "/kwɑːˈdruːpəld/", "đã tăng gấp bốn lần, nhân bốn"),
    ("080921", "quadrupler", "noun", "/kwɑːˈdruːplər/", "bộ nhân tần số gấp bốn (điện tử)"),
    ("080922", "quadruples", "verb", "/kwɑːˈdruːpəlz/", "tăng gấp bốn lần, nhân bốn"),
    ("080923", "quadruplicated", "verb", "/kwɑːˈdruːpləˌkeɪtɪd/", "đã sao thành bốn bản; nhân gấp bốn"),
    ("080924", "quadruplicates", "verb", "/kwɑːˈdruːpləˌkeɪts/", "sao làm bốn bản; nhân lên gấp bốn"),
    ("080925", "quadruplicating", "verb", "/kwɑːˈdruːpləˌkeɪtɪŋ/", "sao làm bốn bản; nhân lên gấp bốn"),
    ("080926", "quadruplication", "noun", "/kwɑːˌdruːpləˈkeɪʃən/", "sự nhân gấp bốn; việc lập bốn bản"),
    ("080927", "quadruplicity", "noun", "/ˌkwɑːdrʊˈplɪsəti/", "tính chất gồm bốn phần, bộ bốn"),
    ("080928", "quadruply", "adv", "/ˈkwɑːdrʊpli/", "gấp bốn lần, theo bộ bốn"),
    ("080929", "quadrupole", "noun", "/ˈkwɑːdrəˌpoʊl/", "trường tứ cực, mạch điện bốn cực"),
    ("080930", "quads", "noun", "/kwɑːdz/", "bộ bốn; sân vuông đại học; cơ đùi"),
    ("080931", "quaestorial", "adj", "/kwiːˈstɔːriəl/", "thuộc quan coi quốc khố La Mã"),
    ("080932", "quaffed", "verb", "/kwɑːft/", "đã nốc cạn, đã uống một hơi lớn"),
    ("080933", "quaffer", "noun", "/ˈkwɑːfər/", "người uống rượu từng hớp lớn"),
    ("080934", "quaffing", "verb", "/ˈkwɑːfɪŋ/", "nốc cạn, uống ừng ực một hơi"),
    ("080935", "quaffs", "verb", "/kwɑːfs/", "nốc cạn, uống một hơi sảng khoái"),
    ("080936", "quaggy", "adj", "/ˈkwɑːɡi/", "lầy lội, sũng nước, lún nhún bùn"),
    ("080937", "quagog", "noun", "/ˈkweɪhɔːɡ/", "ngào vỏ cứng Bắc Mỹ (biến thể cổ)"),
    ("080938", "quahaug", "noun", "/ˈkwɔːhɔːɡ/", "nghêu vỏ cứng Bắc Mỹ (Mercenaria)"),
    ("080939", "quailed", "verb", "/kweɪld/", "đã chùn bước, đã run sợ khiếp đảm"),
    ("080940", "quailing", "verb", "/ˈkweɪlɪŋ/", "chùn bước, run sợ, khiếp đảm"),
    ("080941", "quails", "verb", "/kweɪlz/", "chùn bước, nao núng, khiếp sợ"),
    ("080942", "quaked", "verb", "/kweɪkt/", "đã rung chuyển; đã run rẩy khiếp sợ"),
    ("080943", "quakeress", "noun", "/ˈkweɪkərəs/", "nữ tín đồ giáo phái Quaker"),
    ("080944", "quakerish", "adj", "/ˈkweɪkərɪʃ/", "giản dị, nghiêm trang kiểu Quaker"),
    ("080945", "quakes", "verb", "/kweɪks/", "rung chuyển, động đất; run rẩy"),
    ("080946", "quaking", "verb", "/ˈkweɪkɪŋ/", "rung chuyển, run lên bần bật"),
    ("080947", "quaky", "adj", "/ˈkweɪki/", "hay run rẩy, rung lắc yếu ớt"),
    ("080948", "quale", "noun", "/ˈkweɪli/", "cảm thụ chủ quan (triết học)"),
    ("080949", "qualia", "noun", "/ˈkwɑːliə/", "những phẩm tính cảm thụ chủ quan"),
    ("080950", "qualifiable", "adj", "/ˈkwɑːləˌfaɪəbəl/", "có thể hạn định; có thể đủ chuẩn"),
    ("080951", "qualifications", "noun", "/ˌkwɑːləfəˈkeɪʃənz/", "bằng cấp, trình độ; điều kiện"),
    ("080952", "qualificative", "adj", "/ˈkwɑːləfəˌkeɪtɪv/", "hạn định, bổ nghĩa phẩm chất"),
    ("080953", "qualifiers", "noun", "/ˈkwɑːləˌfaɪərz/", "từ bổ nghĩa; vòng đấu loại thể thao"),
    ("080954", "qualifies", "verb", "/ˈkwɑːləˌfaɪz/", "đủ tiêu chuẩn; lọt vào vòng trong"),
    ("080955", "qualities", "noun", "/ˈkwɑːlətiz/", "chất lượng; phẩm chất, đặc tính"),
    ("080956", "qualmish", "adj", "/ˈkwɑːlmɪʃ/", "buồn nôn, nôn nao; hay băn khoăn"),
    ("080957", "qualmishness", "noun", "/ˈkwɑːlmɪʃnəs/", "cảm giác buồn nôn; sự áy náy"),
    ("080958", "qualms", "noun", "/kwɑːmz/", "sự áy náy lương tâm; cơn buồn nôn"),
    ("080959", "qualmy", "adj", "/ˈkwɑːlmi/", "nôn nao khó chịu; hay áy náy"),
    ("080960", "qualyficatory", "adj", "/ˈkwɑːləfəˌkeɪtəri/", "nhằm xét chuẩn (biến thể sai chữ)"),
    ("080961", "qualyfied", "adj", "/ˈkwɑːləˌfaɪd/", "đủ tư cách, đủ trình độ (lỗi chữ)"),
    ("080962", "qualyfier", "noun", "/ˈkwɑːləˌfaɪər/", "vòng loại; từ bổ nghĩa (lỗi chữ)"),
    ("080963", "quamash", "noun", "/ˈkwɑːmæʃ/", "cây hành dại camassia Bắc Mỹ"),
    ("080964", "quamassia", "noun", "/kwəˈmɑːʃə/", "chi cây hành hoa Camassia"),
    ("080965", "quandang", "noun", "/ˈkwɑːndɑːŋ/", "cây đào sa mạc Úc (quandong)"),
    ("080966", "quandaries", "noun", "/ˈkwɑːndəriz/", "những tình thế tiến thoái lưỡng nan"),
    ("080967", "quandong", "noun", "/ˈkwɑːndɑːŋ/", "cây quả đào sa mạc Úc"),
    ("080968", "quangos", "noun", "/ˈkwæŋɡoʊz/", "các cơ quan bán công (Anh)"),
    ("080969", "quant", "noun", "/kwɑːnt/", "sào bịt đầu chống thuyền (Anh)"),
    ("080970", "quanta", "noun", "/ˈkwɑːntə/", "các lượng tử năng lượng (vật lý)"),
    ("080971", "quanternary", "noun", "/kwɑːˈtɜːrnəri/", "kỷ Đệ Tứ; hệ tứ phân (biến thể)"),
    ("080972", "quantifiability", "noun", "/ˌkwɑːntəfaɪəˈbɪləti/", "tính có thể định lượng đo đếm được"),
    ("080973", "quantise", "verb", "/ˈkwɑːntaɪz/", "lượng tử hóa, rời rạc hóa (Anh)"),
    ("080974", "quantities", "noun", "/ˈkwɑːntətiz/", "số lượng, khối lượng; đại lượng"),
    ("080975", "quantizer", "noun", "/ˈkwɑːnˌtaɪzər/", "bộ lượng tử hóa tín hiệu (điện tử)"),
    ("080976", "quantometer", "noun", "/kwɑːnˈtɑːmɪtər/", "máy quang phổ đo thành phần hợp kim"),
    ("080977", "quantong", "noun", "/ˈkwɑːntɑːŋ/", "quả đào sa mạc Úc (biến thể)"),
    ("080978", "quaoar", "noun", "/ˈkwɑːwɑːr/", "hành tinh lùn Quaoar (vũ trụ)"),
    ("080979", "quaquaversal", "adj", "/ˌkwɑːkwəˈvɜːrsəl/", "dốc tỏa mọi phía từ tâm (địa chất)"),
    ("080980", "quarantinable", "adj", "/ˈkwɔːrənˌtiːnəbəl/", "phải cách ly kiểm dịch (bệnh, hàng)"),
    ("080981", "quarantines", "verb", "/ˈkwɔːrənˌtiːnz/", "cách ly, kiểm dịch phòng bệnh"),
    ("080982", "quarantining", "verb", "/ˈkwɔːrənˌtiːnɪŋ/", "cách ly, kiểm dịch ngăn lây lan"),
    ("080983", "quarenden", "noun", "/ˈkwɑːrəndən/", "giống táo đỏ chín sớm vùng Devon"),
    ("080984", "quarender", "noun", "/ˈkwɑːrəndər/", "giống táo đỏ chín sớm (biến thể)"),
    ("080985", "quarkonia", "noun", "/kwɔːrˈkoʊniə/", "các trạng thái liên kết quark-phản"),
    ("080986", "quarkonium", "noun", "/kwɔːrˈkoʊniəm/", "meson gồm quark và phản quark"),
    ("080987", "quarreler", "noun", "/ˈkwɔːrələr/", "người hay cãi cọ, kẻ thích gây sự"),
    ("080988", "quarrelers", "noun", "/ˈkwɔːrələrz/", "những kẻ hay cãi cọ, gây gổ"),
    ("080989", "quarreling", "adj", "/ˈkwɔːrəlɪŋ/", "hay cãi cọ, thích sinh sự gây gổ"),
    ("080990", "quarrelled", "verb", "/ˈkwɔːrəld/", "đã cãi cọ, đã bất hòa xích mích"),
    ("080991", "quarreller", "noun", "/ˈkwɔːrələr/", "người hay cãi cọ, gây gổ (Anh)"),
    ("080992", "quarrellers", "noun", "/ˈkwɔːrələrz/", "những kẻ hay cãi cọ, gây gổ (Anh)"),
    ("080993", "quarrelling", "verb", "/ˈkwɔːrəlɪŋ/", "cãi cọ, cãi vã, bất hòa (Anh)"),
    ("080994", "quarrels", "verb", "/ˈkwɔːrəlz/", "cãi cọ, cãi vã; bất hòa, chê bai"),
    ("080995", "quarrelsomeness", "noun", "/ˈkwɔːrəlsəmnəs/", "tính hay cãi vã, thói hiếu chiến"),
    ("080996", "quarried", "verb", "/ˈkwɔːrid/", "đã khai thác từ mỏ đá; đã truy tìm"),
    ("080997", "quarriers", "noun", "/ˈkwɔːriərz/", "những công nhân khai thác mỏ đá"),
    ("080998", "quarries", "verb", "/ˈkwɔːriz/", "khai thác đá từ mỏ; truy tìm"),
    ("080999", "quarryings", "noun", "/ˈkwɔːriɪŋz/", "các hoạt động khai thác mỏ đá"),
    ("081000", "quarrymen", "noun", "/ˈkwɔːrimən/", "những người thợ khai thác mỏ đá"),
    ("081001", "quars", "noun", "/kwɑːrz/", "các tảng đá, khối thạch anh (hiếm)"),
    ("081002", "quartans", "noun", "/ˈkwɔːrtənz/", "cơn sốt rét cách bốn ngày (y học)"),
]

raw = json.load(open("scratch/b37_r02_raw_p5.json"))
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
with open("scratch/b37_r02_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r02_p5 saved OK")
