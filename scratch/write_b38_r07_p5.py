import json

RECORDS = [
    ("088403", "spartein", "noun", "/ˈspɑːrtiˌɪn/", "ankaloit spartein từ cây kim tước"),
    ("088404", "spartium", "noun", "/ˈspɑːrʃəm/", "chi cây kim tước Tây Ban Nha"),
    ("088405", "spasmodical", "adj", "/spæzˈmɑːdɪkəl/", "co thắt; thất thường từng cơn"),
    ("088406", "spasmology", "noun", "/spæzˈmɑːlədʒi/", "khoa nghiên cứu chứng co thắt"),
    ("088407", "spasmolysis", "noun", "/spæzˈmɑːləsɪs/", "sự làm giãn co thắt cơ"),
    ("088408", "spasmolytic", "noun", "/ˌspæzməˈlɪtɪk/", "thuốc chống co thắt; thuốc giãn cơ"),
    ("088409", "spatangoida", "noun", "/ˌspætənˈɡɔɪdə/", "bộ Nhím biển hình trái tim"),
    ("088410", "spathaceous", "adj", "/spəˈθeɪʃəs/", "có mo bao hoa (họ Ráy, Cau)"),
    ("088411", "spathed", "adj", "/speɪðd/", "có mo hoa bao bọc"),
    ("088412", "spathic", "adj", "/ˈspæθɪk/", "tách lớp phẳng như fenspat"),
    ("088413", "spathiform", "adj", "/ˈspæθɪˌfɔːrm/", "có dạng khoáng chất tách phẳng"),
    ("088414", "spathiphyllum", "noun", "/ˌspæθəˈfɪləm/", "cây lan ý (huệ hòa bình)"),
    ("088415", "spathose", "adj", "/ˈspeɪθoʊs/", "có mo hoa lớn; tách lớp phẳng"),
    ("088416", "spathulate", "adj", "/ˈspætʃələt/", "có hình chiếc bay hay thìa dẹt"),
    ("088417", "spattee", "noun", "/spæˈtiː/", "ghệt che mắt cá chân"),
    ("088418", "spatterdashes", "noun", "/ˈspætərˌdæʃɪz/", "xà cạp che bùn cẳng chân"),
    ("088419", "spatterdock", "noun", "/ˈspætərˌdɑːk/", "cây súng vàng mọc đầm lầy"),
    ("088420", "spatters", "verb", "/ˈspætərz/", "bắn tung tóe; rơi lộp độp"),
    ("088421", "spatular", "adj", "/ˈspætʃələr/", "có hình chiếc bay; hình thìa dẹt"),
    ("088422", "spatule", "noun", "/ˈspætʃuːl/", "bộ phận có đầu dẹt hình thìa"),
    ("088423", "spatuliform", "adj", "/ˈspætʃələˌfɔːrm/", "có dạng hình thìa dẹt"),
    ("088424", "spaven", "noun", "/ˈspævən/", "chứng sưng khớp cổ chân ngựa"),
    ("088425", "spavin", "noun", "/ˈspævɪn/", "chứng sưng khớp khuỷu chân sau ngựa"[:35]),
    ("088426", "spavined", "adj", "/ˈspævɪnd/", "bị sưng khớp chân sau; khập khiễng"[:35]),
    ("088427", "spawl", "noun", "/spɔːl/", "mảnh đá vỡ mẻ; mảnh gỗ dăm"),
    ("088428", "spawned", "verb", "/spɔːnd/", "đã đẻ trứng (cá, ếch); sinh ra"),
    ("088429", "spawning", "verb", "/ˈspɔːnɪŋ/", "đang đẻ trứng (cá); đang sinh sôi"),
    ("088430", "spawns", "verb", "/spɔːnz/", "đẻ trứng (cá, ếch); sản sinh hàng"),
    ("088431", "spd", "noun", "/ˌɛsˌpiːˈdiː/", "Đảng Dân chủ Xã hội Đức (SPD)"),
    ("088432", "speakable", "adj", "/ˈspiːkəbəl/", "có thể nói thành lời được"),
    ("088433", "speakers", "noun", "/ˈspiːkərz/", "diễn giả; loa phát âm; chủ tịch"),
    ("088434", "speared", "verb", "/spɪrd/", "đã đâm bằng ngọn giáo; vươn thẳng"),
    ("088435", "speargun", "noun", "/ˈspɪrˌɡʌn/", "súng bắn lao săn cá dưới nước"),
    ("088436", "spearheaded", "verb", "/ˈspɪrˌhɛdɪd/", "đã dẫn đầu tiên phong chiến dịch"),
    ("088437", "spearheading", "verb", "/ˈspɪrˌhɛdɪŋ/", "đang dẫn đầu tiên phong phong trào"),
    ("088438", "spearheads", "verb", "/ˈspɪrˌhɛdz/", "dẫn đầu tiên phong; mở mũi nhọn"),
    ("088439", "spearing", "verb", "/ˈspɪrɪŋ/", "đang đâm bằng giáo; vươn mầm thẳng"[:35]),
    ("088440", "spearman", "noun", "/ˈspɪrmən/", "lính cầm giáo; lính đánh lao"),
    ("088441", "spears", "noun", "/spɪrz/", "ngọn giáo mác; ngọn mầm măng tây"),
    ("088442", "speary", "adj", "/ˈspɪri/", "nhọn thẳng như ngọn giáo"),
    ("088443", "specialiser", "noun", "/ˈspɛʃəˌlaɪzər/", "chuyên gia; người chuyên môn hóa"),
    ("088444", "specialises", "verb", "/ˈspɛʃəˌlaɪzɪz/", "chuyên môn hóa; chuyên về lĩnh vực"[:35]),
    ("088445", "specialising", "verb", "/ˈspɛʃəˌlaɪzɪŋ/", "đang chuyên môn hóa; chuyên sâu"),
    ("088446", "specialistic", "adj", "/ˌspɛʃəˈlɪstɪk/", "thuộc chuyên môn sâu; chuyên biệt"),
    ("088447", "specialists", "noun", "/ˈspɛʃəlɪsts/", "chuyên gia; bác sĩ chuyên khoa"),
    ("088448", "specializer", "noun", "/ˈspɛʃəˌlaɪzər/", "chuyên gia; người chuyên môn hóa"),
    ("088449", "specializes", "verb", "/ˈspɛʃəˌlaɪzɪz/", "chuyên môn hóa; chuyên về"),
    ("088450", "specializing", "verb", "/ˈspɛʃəˌlaɪzɪŋ/", "đang chuyên môn hóa; chuyên về"),
    ("088451", "speciate", "verb", "/ˈspiːʃiˌeɪt/", "phân hóa hình thành loài mới"),
    ("088452", "speciational", "adj", "/ˌspiːʃiˈeɪʃənəl/", "thuộc sự hình thành loài mới"),
    ("088453", "specifications", "noun", "/ˌspɛsəfɪˈkeɪʃənz/", "thông số kỹ thuật; bản quy cách"),
    ("088454", "specificness", "noun", "/spəˈsɪfɪknəs/", "tính đặc trưng; nét cụ thể rõ ràng"),
    ("088455", "specifies", "verb", "/ˈspɛsəˌfaɪz/", "chỉ rõ; quy định cụ thể"),
    ("088456", "specifity", "noun", "/ˌspɛsɪˈfɪsɪti/", "tính đặc hiệu; nét riêng biệt"),
    ("088457", "specifying", "verb", "/ˈspɛsəˌfaɪɪŋ/", "đang chỉ rõ; đang quy định cụ thể"),
    ("088458", "specilative", "adj", "/ˈspɛkjəˌleɪtɪv/", "suy đoán; mang tính đầu cơ"),
    ("088459", "speciogenesis", "noun", "/ˌspiːʃioʊˈdʒɛnəsɪs/", "quá trình phát sinh loài mới"),
    ("088460", "speciological", "adj", "/ˌspiːʃiəˈlɑːdʒɪkəl/", "thuộc khoa học nghiên cứu về loài"),
    ("088461", "speciology", "noun", "/ˌspiːʃiˈɑːlədʒi/", "khoa học nghiên cứu về loài"),
    ("088462", "speciosity", "noun", "/ˌspiːʃiˈɑːsɪti/", "vẻ hào nhoáng ngụy biện bề ngoài"),
    ("088463", "speciousness", "noun", "/ˈspiːʃəsnəs/", "tính ngụy biện giả dối bề ngoài"),
    ("088464", "specking", "verb", "/ˈspɛkɪŋ/", "đang lấm tấm đốm nhỏ; đốm màu"),
    ("088465", "speckles", "verb", "/ˈspɛkəlz/", "làm lấm tấm đốm; rắc đốm nhỏ"),
    ("088466", "speckless", "adj", "/ˈspɛkləs/", "sạch bong không một vết bụi"),
    ("088467", "speckling", "verb", "/ˈspɛklɪŋ/", "đang rắc đốm lấm tấm"),
    ("088468", "specks", "verb", "/spɛks/", "điểm những hạt nhỏ; tạo đốm nhỏ"),
    ("088469", "spectated", "verb", "/ˈspɛkteɪtɪd/", "đã dự xem; đã làm khán giả xem"),
    ("088470", "spectates", "verb", "/ˈspɛkteɪts/", "dự xem; theo dõi như khán giả"),
    ("088471", "spectating", "verb", "/ˈspɛkteɪtɪŋ/", "đang dự xem như khán giả"),
    ("088472", "spectatress", "noun", "/spɛkˈteɪtrəs/", "nữ khán giả"),
    ("088473", "spectinomycin", "noun", "/ˌspɛktɪnoʊˈmaɪsɪn/", "thuốc kháng sinh spectinomycin"),
    ("088474", "spectra", "noun", "/ˈspɛktrə/", "quang phổ; dải phổ"),
    ("088475", "spectrality", "noun", "/spɛkˈtrælɪti/", "vẻ ma quái; tính chất quang phổ"),
    ("088476", "spectrally", "adv", "/ˈspɛktrəli/", "ma quái như bóng ma; theo quang phổ"[:35]),
    ("088477", "spectrographically", "adv", "/ˌspɛktrəˈɡræfɪkli/", "bằng phương pháp quang phổ ký"),
    ("088478", "spectrography", "noun", "/spɛkˈtrɑːɡrəfi/", "kỹ thuật chụp ảnh quang phổ"),
    ("088479", "spectroheliogram", "noun", "/ˌspɛktroʊˈhiːliəˌɡræm/", "ảnh chụp đơn sắc quang phổ Mặt Trời"[:35]),
    ("088480", "spectroheliograph", "noun", "/ˌspɛktroʊˈhiːliəˌɡræf/", "máy chụp quang phổ Mặt Trời"),
    ("088481", "spectroheliography", "noun", "/ˌspɛktroʊˌhiːliˈɑːɡrəfi/", "phép chụp quang phổ Mặt Trời"),
    ("088482", "spectrohelioscope", "noun", "/ˌspɛktroʊˈhiːliəˌskoʊp/", "kính quan sát quang phổ Mặt Trời"),
    ("088483", "spectrology", "noun", "/spɛkˈtrɑːlədʒi/", "quang phổ học; khoa nghiên cứu ma"),
    ("088484", "spectrophotography", "noun", "/ˌspɛktroʊfəˈtɑːɡrəfi/", "phép chụp ảnh quang phổ"),
    ("088485", "spectrophotometers", "noun", "/ˌspɛktroʊfoʊˈtɑːmɪtərz/", "máy quang phổ kế"),
    ("088486", "spectrophotometric", "adj", "/ˌspɛktroʊˌfoʊtəˈmɛtrɪk/", "thuộc phép đo quang phổ"),
    ("088487", "spectrophotometry", "noun", "/ˌspɛktroʊfoʊˈtɑːmətri/", "phép đo quang phổ hấp thụ"),
    ("088488", "spectroscopical", "adj", "/ˌspɛktrəˈskɑːpɪkəl/", "thuộc quang phổ học"),
    ("088489", "specula", "noun", "/ˈspɛkjələ/", "mỏ vịt khám y khoa; gương phản xạ"),
    ("088490", "speculated", "verb", "/ˈspɛkjəˌleɪtɪd/", "đã suy đoán; đã đầu cơ"),
    ("088491", "speculating", "verb", "/ˈspɛkjəˌleɪtɪŋ/", "đang suy đoán; đang đầu cơ"),
    ("088492", "speculations", "noun", "/ˌspɛkjəˈleɪʃənz/", "sự suy đoán; hoạt động đầu cơ"),
    ("088493", "speculativeness", "noun", "/ˈspɛkjəˌleɪtɪvnəs/", "tính chất suy đoán phỏng chừng"),
    ("088494", "speculatory", "adj", "/ˈspɛkjələˌtɔːri/", "mang tính suy đoán; có tính đầu cơ"),
    ("088495", "sped", "verb", "/spɛd/", "đã phóng nhanh; đã chạy vội"),
    ("088496", "speechification", "noun", "/ˌspiːtʃəfɪˈkeɪʃən/", "lời diễn thuyết dài dòng nhàm chán"),
    ("088497", "speechified", "verb", "/ˈspiːtʃəˌfaɪd/", "đã diễn thuyết dài dòng"),
    ("088498", "speechifier", "noun", "/ˈspiːtʃəˌfaɪər/", "người hay diễn thuyết dài dòng"),
    ("088499", "speechifies", "verb", "/ˈspiːtʃəˌfaɪz/", "diễn thuyết dài dòng văn tự"),
    ("088500", "speechify", "verb", "/ˈspiːtʃəˌfaɪ/", "diễn thuyết dông dài"),
    ("088501", "speechifying", "verb", "/ˈspiːtʃəˌfaɪɪŋ/", "đang diễn thuyết dông dài"),
    ("088502", "speechlessly", "adv", "/ˈspiːtʃləsli/", "lặng người không nói nên lời"),
]

# Replace slices cleanly <= 35 chars
RECORDS[22] = ("088425", "spavin", "noun", "/ˈspævɪn/", "sưng khớp khuỷu chân sau ngựa")
RECORDS[23] = ("088426", "spavined", "adj", "/ˈspævɪnd/", "sưng khớp chân sau; đi khập khiễng")
RECORDS[36] = ("088439", "spearing", "verb", "/ˈspɪrɪŋ/", "đang đâm bằng giáo; vươn mầm thẳng")
RECORDS[41] = ("088444", "specialises", "verb", "/ˈspɛʃəˌlaɪzɪz/", "chuyên môn hóa; chuyên về")
RECORDS[73] = ("088476", "spectrally", "adv", "/ˈspɛktrəli/", "như bóng ma; theo quang phổ")
RECORDS[76] = ("088479", "spectroheliogram", "noun", "/ˌspɛktroʊˈhiːliəˌɡræm/", "ảnh chụp quang phổ Mặt Trời")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r07_raw_p5.json"))
by_id = {r["id"].split(".")[-1]: r for r in raw}
out = []
for sid, hw, pos, ipa, vi in RECORDS:
    rec = dict(by_id[sid])
    assert rec["hw"] == hw, (sid, hw, rec["hw"])
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

json.dump(out, open("scratch/b38_r07_reviewed_p5.json", "w"), ensure_ascii=False, indent=2)
print("b38_r07_p5 saved OK")
