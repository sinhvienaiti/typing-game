import json

rows = [
    ("077803", "polyergus", "noun", "/ˌpɒliˈɜːrɡəs/", "chi kiến nô lệ Amazon (Polyergus)"),
    ("077804", "polyesterification", "noun", "/pɒliˌɛstərɪfɪˈkeɪʃən/", "phản ứng tạo nhựa polyester"),
    ("077805", "polyestrous", "adj", "/ˌpɒliˈɛstrəs/", "động dục nhiều lần trong năm"),
    ("077806", "polyfactor", "noun", "/ˌpɒliˈfæktər/", "đa nhân tố (tương tác nhiều yếu tố)"),
    ("077807", "polyfactorial", "adj", "/ˌpɒlifækˈtɔːriəl/", "do nhiều yếu tố, đa nhân tố"),
    ("077808", "polyfunctional", "adj", "/ˌpɒliˈfʌŋkʃənəl/", "đa chức năng, nhiều công dụng"),
    ("077809", "polygalaceae", "noun", "/ˌpɒlɪɡəˈleɪsiː/", "họ Viễn chí (Polygalaceae)"),
    ("077810", "polygalactia", "noun", "/ˌpɒlɪɡəˈlækʃə/", "chứng tiết sữa quá nhiều (y học)"),
    ("077811", "polygamic", "adj", "/ˌpɒlɪˈɡæmɪk/", "thuộc chế độ đa thê hoặc đa phu"),
    ("077812", "polygamously", "adv", "/pəˈlɪɡəməsli/", "theo chế độ đa thê, đa phu"),
    ("077813", "polygastric", "adj", "/ˌpɒlɪˈɡæstrɪk/", "có nhiều ngăn dạ dày (nhai lại)"),
    ("077814", "polygene", "noun", "/ˈpɒlɪdʒiːn/", "đa gen (nhiều gen cùng quy định)"),
    ("077815", "polygenesis", "noun", "/ˌpɒlɪˈdʒɛnɪsɪs/", "thuyết đa nguồn gốc (tiến hóa)"),
    ("077816", "polygenesist", "noun", "/ˌpɒlɪˈdʒɛnɪsɪst/", "người theo thuyết đa nguồn gốc"),
    ("077817", "polygenetic", "adj", "/ˌpɒlɪdʒəˈnɛtɪk/", "thuộc đa nguồn gốc; do nhiều gen"),
    ("077818", "polygeny", "noun", "/pəˈlɪdʒəni/", "tính di truyền đa gen (số lượng)"),
    ("077819", "polyglandular", "adj", "/ˌpɒlɪˈɡlændjələr/", "thuộc nhiều tuyến nội tiết"),
    ("077820", "polyglotism", "noun", "/ˈpɒlɪˌɡlɒtɪzəm/", "khả năng biết nhiều ngoại ngữ"),
    ("077821", "polyglottal", "adj", "/ˌpɒlɪˈɡlɒtəl/", "đa ngữ, biết nhiều thứ tiếng"),
    ("077822", "polyglottic", "adj", "/ˌpɒlɪˈɡlɒtɪk/", "đa ngữ, viết bằng nhiều thứ tiếng"),
    ("077823", "polyglottism", "noun", "/ˈpɒlɪˌɡlɒtɪzəm/", "khả năng sử dụng nhiều thứ tiếng"),
    ("077824", "polyglottist", "noun", "/ˈpɒlɪˌɡlɒtɪst/", "người thông thạo nhiều thứ tiếng"),
    ("077825", "polyglottous", "adj", "/ˌpɒlɪˈɡlɒtəs/", "đa ngữ, biết nhiều thứ tiếng"),
    ("077826", "polygonales", "noun", "/ˌpɒlɪɡəˈneɪliːz/", "bộ Rau răm (Polygonales)"),
    ("077827", "polygonally", "adv", "/pəˈlɪɡənəli/", "theo hình đa giác"),
    ("077828", "polygonatum", "noun", "/ˌpɒlɪɡəˈneɪtəm/", "chi cây hoàng tinh (Polygonatum)"),
    ("077829", "polygonia", "noun", "/ˌpɒlɪˈɡoʊniə/", "chi bướm dấu phẩy (Polygonia)"),
    ("077830", "polygonometry", "noun", "/ˌpɒlɪɡəˈnɒmətri/", "phép đo đa giác (toán học)"),
    ("077831", "polygonous", "adj", "/pəˈlɪɡənəs/", "có hình đa giác, nhiều góc"),
    ("077832", "polygottal", "adj", "/ˌpɒlɪˈɡɒtəl/", "đa ngữ, nói được nhiều thứ tiếng"),
    ("077833", "polygottic", "adj", "/ˌpɒlɪˈɡɒtɪk/", "đa ngữ, viết nhiều thứ tiếng"),
    ("077834", "polygraphy", "noun", "/pəˈlɪɡrəfi/", "máy ghi đa thông số; viết mật mã"),
    ("077835", "polygynist", "noun", "/pəˈlɪdʒɪnɪst/", "người đàn ông theo chế độ đa thê"),
    ("077836", "polyhaploid", "adj", "/ˌpɒlɪˈhæplɔɪd/", "đa đơn bội (di truyền học)"),
    ("077837", "polyharmonic", "adj", "/ˌpɒlɪhɑːrˈmɒnɪk/", "đa điều hòa (toán giải tích)"),
    ("077838", "polyhedra", "noun", "/ˌpɒlɪˈhiːdrə/", "khối đa diện (nhiều mặt phẳng)"),
    ("077839", "polyhedric", "adj", "/ˌpɒlɪˈhiːdrɪk/", "có nhiều mặt, dạng khối đa diện"),
    ("077840", "polyhedrosis", "noun", "/ˌpɒlɪhɪˈdroʊsɪs/", "bệnh virus thể đa diện (sâu tằm)"),
    ("077841", "polyhidrosis", "noun", "/ˌpɒlɪhaɪˈdroʊsɪs/", "chứng tăng tiết mồ hôi nhiều"),
    ("077842", "polyhistor", "noun", "/ˌpɒlɪˈhɪstɔːr/", "nhà bác học uyên bác đa ngành"),
    ("077843", "polyhistoric", "adj", "/ˌpɒlɪhɪˈstɒrɪk/", "uyên bác, am hiểu nhiều lĩnh vực"),
    ("077844", "polyhybrid", "noun", "/ˌpɒlɪˈhaɪbrɪd/", "cơ thể lai nhiều cặp tính trạng"),
    ("077845", "polyisomere", "noun", "/ˌpɒlɪˈaɪsəmɪr/", "cơ thể có nhiều khúc giống nhau"),
    ("077846", "polykaric", "adj", "/ˌpɒlɪˈkærɪk/", "đa nhân (tế bào nhiều nhân)"),
    ("077847", "polymastigina", "noun", "/ˌpɒlɪmæstɪˈdʒaɪnə/", "bộ Trùng đa roi ký sinh"),
    ("077848", "polymastigote", "noun", "/ˌpɒlɪˈmæstɪɡoʊt/", "trùng roi có nhiều roi bơi"),
    ("077849", "polymathic", "adj", "/ˌpɒlɪˈmæθɪk/", "uyên bác, thông thạo nhiều ngành"),
    ("077850", "polymathy", "noun", "/ˈpɒlɪˌmæθi/", "sự uyên bác, kiến thức sâu rộng"),
    ("077851", "polymelus", "noun", "/pəˈlɪmələs/", "dị tật thừa chân tay (quái thai)"),
    ("077852", "polymenia", "noun", "/ˌpɒlɪˈmiːniə/", "chứng kinh nguyệt nhiều bất thường"),
    ("077853", "polymerically", "adv", "/ˌpɒlɪˈmɛrɪkli/", "theo cấu trúc polyme"),
    ("077854", "polymerise", "verb", "/ˈpɒlɪməraɪz/", "trùng hợp (tạo chuỗi polyme)"),
    ("077855", "polymerised", "verb", "/ˈpɒlɪməraɪzd/", "đã trùng hợp (tạo chuỗi polyme)"),
    ("077856", "polymerises", "verb", "/ˈpɒlɪməraɪzɪz/", "trùng hợp (tạo chuỗi polyme)"),
    ("077857", "polymerising", "verb", "/ˈpɒlɪməraɪzɪŋ/", "trùng hợp (tạo chuỗi polyme)"),
    ("077858", "polymerism", "noun", "/ˈpɒlɪmərɪzəm/", "hiện tượng trùng hợp (hóa học)"),
    ("077859", "polymerized", "verb", "/pəˈlɪməˌraɪzd/", "đã trùng hợp (tạo chuỗi polyme)"),
    ("077860", "polymerizes", "verb", "/pəˈlɪməˌraɪzɪz/", "trùng hợp (tạo chuỗi polyme)"),
    ("077861", "polymerizing", "verb", "/pəˈlɪməˌraɪzɪŋ/", "trùng hợp (tạo chuỗi polyme)"),
    ("077862", "polymerous", "adj", "/pəˈlɪmərəs/", "gồm nhiều phần; có nhiều monome"),
    ("077863", "polymery", "noun", "/ˈpɒlɪməri/", "hiện tượng trùng hợp; nhiều cặp gen"),
    ("077864", "polymetallic", "adj", "/ˌpɒlɪmɪˈtælɪk/", "đa kim loại (chứa nhiều kim loại)"),
    ("077865", "polymitosis", "noun", "/ˌpɒlɪmaɪˈtoʊsɪs/", "sự nguyên phân liên tiếp nhiều lần"),
    ("077866", "polymolecular", "adj", "/ˌpɒlɪməˈlɛkjələr/", "đa phân tử (gồm nhiều phân tử)"),
    ("077867", "polymorphemic", "adj", "/ˌpɒlɪmɔːrˈfiːmɪk/", "gồm nhiều hình vị (ngôn ngữ học)"),
    ("077868", "polymorphocellular", "adj", "/ˌpɒlɪˌmɔːrfoʊˈsɛljələr/", "đa dạng tế bào (mô học)"),
    ("077869", "polymorphonuclear", "adj", "/ˌpɒlɪˌmɔːrfoʊˈnjuːkliər/", "đa hình thái nhân (bạch cầu)"),
    ("077870", "polymorphously", "adv", "/ˌpɒlɪˈmɔːrfəsli/", "theo nhiều dạng hình thái"),
    ("077871", "polymox", "noun", "/ˈpɒlɪmɒks/", "kháng sinh amoxicillin (Polymox)"),
    ("077872", "polynemidae", "noun", "/ˌpɒlɪˈnɛmɪdiː/", "họ Cá nhụ, cá chét (Polynemidae)"),
    ("077873", "polyneuritis", "noun", "/ˌpɒlɪnjʊˈraɪtɪs/", "viêm đa dây thần kinh ngoại biên"),
    ("077874", "polynia", "noun", "/pəˈlɪnjə/", "vùng nước hở giữa băng (polynya)"),
    ("077875", "polynomials", "noun", "/ˌpɑːlɪˈnoʊmiəlz/", "đa thức (toán học)"),
    ("077876", "polynuclear", "adj", "/ˌpɒlɪˈnjuːkliər/", "đa nhân; có nhiều vòng thơm"),
    ("077877", "polyodon", "noun", "/ˌpɒlɪˈoʊdɒn/", "chi cá tầm thìa (Polyodon)"),
    ("077878", "polyodontidae", "noun", "/ˌpɒlɪoʊˈdɒntɪdiː/", "họ Cá tầm thìa (Polyodontidae)"),
    ("077879", "polyoestrous", "adj", "/ˌpɒlɪˈiːstrəs/", "động dục nhiều lần trong năm"),
    ("077880", "polyoicous", "adj", "/ˌpɒlɪˈɔɪkəs/", "đa tính trên cùng một cây (rêu)"),
    ("077881", "polyoma", "noun", "/ˌpɒlɪˈoʊmə/", "virus đa u (polyomavirus)"),
    ("077882", "polyonychia", "noun", "/ˌpɒlɪoʊˈnɪkiə/", "dị tật thừa móng tay chân"),
    ("077883", "polyonymous", "adj", "/ˌpɒlɪˈɒnɪməs/", "được gọi bằng nhiều tên khác nhau"),
    ("077884", "polyonymy", "noun", "/pəˈlɪɒnəmi/", "tình trạng có nhiều tên gọi"),
    ("077885", "polyopia", "noun", "/ˌpɒlɪˈoʊpiə/", "tật nhìn một hóa nhiều hình (y học)"),
    ("077886", "polyorchism", "noun", "/ˌpɒlɪˈɔːrkɪzəm/", "dị tật có thừa tinh hoàn (y học)"),
    ("077887", "polyose", "noun", "/ˈpɒlɪoʊs/", "đường đa polysaccarit (hóa sinh)"),
    ("077888", "polyparasitism", "noun", "/ˌpɒlɪˈpærəsaɪtɪzəm/", "hiện tượng nhiễm nhiều ký sinh"),
    ("077889", "polypary", "noun", "/ˈpɒlɪpəri/", "tập đoàn san hô dạng polyp"),
    ("077890", "polype", "noun", "/ˈpɒlɪp/", "thủy tức; u lành niêm mạc (polyp)"),
    ("077891", "polypedates", "noun", "/ˌpɒlɪˈpɛdətiːz/", "chi nhái cây bay (Polypedates)"),
    ("077892", "polypedatidae", "noun", "/ˌpɒlɪpɪˈdætɪdiː/", "họ Nhái cây Rhacophoridae (cũ)"),
    ("077893", "polypetalous", "adj", "/ˌpɒlɪˈpɛtələs/", "có nhiều cánh hoa rời (thực vật)"),
    ("077894", "polyphagia", "noun", "/ˌpɒlɪˈfeɪdʒə/", "chứng ăn uống vô độ; tính ăn tạp"),
    ("077895", "polyphagian", "adj", "/ˌpɒlɪˈfeɪdʒən/", "ăn tạp nhiều loại thức ăn"),
    ("077896", "polyphagous", "adj", "/pəˈlɪfəɡəs/", "ăn tạp; ăn nhiều loài sinh vật"),
    ("077897", "polyphasic", "adj", "/ˌpɒlɪˈfeɪzɪk/", "đa pha, chia thành nhiều giai đoạn"),
    ("077898", "polyphasy", "noun", "/ˈpɒlɪfeɪzi/", "tính đa pha, trạng thái nhiều pha"),
    ("077899", "polyphone", "noun", "/ˈpɒlɪfoʊn/", "chữ cái ghi nhiều âm (ngôn ngữ)"),
    ("077900", "polyphonically", "adv", "/ˌpɒlɪˈfɒnɪkli/", "theo lối phức điệu đa âm (nhạc)"),
    ("077901", "polyphonies", "noun", "/pəˈlɪfəniz/", "âm nhạc phức điệu; hiện tượng đa âm"),
    ("077902", "polyphonous", "adj", "/pəˈlɪfənəs/", "đa âm; theo lối phức điệu (âm nhạc)"),
]

with open("scratch/b36_r06_raw_p4.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r06_p4.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r06_p4 saved OK")
