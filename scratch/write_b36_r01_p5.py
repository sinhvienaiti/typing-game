import json

rows = [
    ("075403", "percolates", "verb", "/ˈpɜːrkəleɪts/", "thấm qua, rỉ qua; pha cà phê phin"),
    ("075404", "percolating", "verb", "/ˈpɜːrkəˌleɪtɪŋ/", "thấm qua, rỉ qua; pha cà phê phin"),
    ("075405", "percomorphi", "noun", "/ˌpɜːrkəˈmɔːrfaɪ/", "bộ Cá vược (nhóm Percomorphi)"),
    ("075406", "percophidae", "noun", "/pərˈkɒfɪdiː/", "họ Cá bống đầu dẹt (Percophidae)"),
    ("075407", "percurrent", "adj", "/pərˈkɜːrənt/", "chạy suốt dọc thân (sinh học)"),
    ("075408", "percusion", "noun", "/pərˈkʌʃən/", "sự gõ; bộ gõ (viết nhầm percussion)"),
    ("075409", "percuss", "verb", "/pərˈkʌs/", "gõ khám (y học); vỗ đập"),
    ("075410", "percussed", "verb", "/pərˈkʌst/", "đã gõ khám (y học); đã đập mạnh"),
    ("075411", "percusses", "verb", "/pərˈkʌsɪz/", "gõ khám (y học); vỗ đập"),
    ("075412", "percussing", "verb", "/pərˈkʌsɪŋ/", "gõ khám (y học); vỗ đập"),
    ("075413", "percussively", "adv", "/pərˈkʌsɪvli/", "theo kiểu gõ đập mạnh"),
    ("075414", "percussiveness", "noun", "/pərˈkʌsɪvnəs/", "tính chất gõ đập vang"),
    ("075415", "percussor", "noun", "/pərˈkʌsər/", "búa gõ phản xạ (y học); kim hỏa"),
    ("075416", "percutaneously", "adv", "/ˌpɜːrkjuːˈteɪniəsli/", "xuyên qua da (tiêm, hấp thụ)"),
    ("075417", "perdicidae", "noun", "/pərˈdɪsɪdiː/", "họ Chim đa đa (Perdicidae)"),
    ("075418", "perdicinae", "noun", "/pərˈdɪsɪniː/", "phân họ Chim đa đa (Perdicinae)"),
    ("075419", "perdifoil", "noun", "/ˈpɜːrdɪfɔɪl/", "cây rụng lá theo mùa"),
    ("075420", "perdu", "adj", "/pərˈduː/", "ẩn nấp phục kích; ẩn dật"),
    ("075421", "perdue", "adj", "/pərˈduː/", "ẩn nấp phục kích; ẩn dật"),
    ("075422", "perdurability", "noun", "/pərˌdjʊrəˈbɪlɪti/", "tính bền vững lâu dài, vĩnh cửu"),
    ("075423", "perdurable", "adj", "/pərˈdjʊrəbəl/", "bền vững lâu dài, vĩnh cửu"),
    ("075424", "perdurably", "adv", "/pərˈdjʊrəbli/", "một cách bền lâu, vĩnh viễn"),
    ("075425", "perdure", "verb", "/pərˈdjʊr/", "tồn tại bền lâu, kéo dài mãi"),
    ("075426", "pere", "noun", "/pɛr/", "cha (tiếng Pháp); tu sĩ (xưng hô)"),
    ("075427", "peregrin", "adj", "/ˈpɛrɪɡrɪn/", "ngoại lai; chim cắt lớn (biến thể)"),
    ("075428", "peregrinate", "verb", "/ˈpɛrɪɡrɪˌneɪt/", "du hành xa; đi lang thang"),
    ("075429", "peregrinated", "verb", "/ˈpɛrɪɡrɪˌneɪtɪd/", "đã du hành xa; đã đi lang thang"),
    ("075430", "peregrinates", "verb", "/ˈpɛrɪɡrɪˌneɪts/", "du hành xa; đi lang thang"),
    ("075431", "peregrinating", "verb", "/ˈpɛrɪɡrɪˌneɪtɪŋ/", "du hành xa; đi lang thang"),
    ("075432", "peregrinator", "noun", "/ˈpɛrɪɡrɪˌneɪtər/", "người đi chu du, lang thang"),
    ("075433", "pereia", "noun", "/pəˈriːə/", "phần ngực giáp xác (có chân bò)"),
    ("075434", "pereion", "noun", "/pəˈriːɒn/", "phần ngực giáp xác (động vật)"),
    ("075435", "perejil", "noun", "/ˌpɛrɛˈhiːl/", "đảo Perejil (eo biển Gibraltar)"),
    ("075436", "peremptoriness", "noun", "/pəˈrɛmptərinəs/", "tính độc đoán, ra lệnh không cãi"),
    ("075437", "perennate", "verb", "/ˈpɛrəneɪt/", "tồn tại qua nhiều mùa (thực vật)"),
    ("075438", "perennation", "noun", "/ˌpɛrəˈneɪʃən/", "sự sống lưu niên qua nhiều năm"),
    ("075439", "perenniality", "noun", "/pəˌrɛniˈælɪti/", "tính lâu dài, tính lưu niên"),
    ("075440", "pereskia", "noun", "/pəˈrɛskiə/", "chi xương rồng lá (Pereskia)"),
    ("075441", "perfecting", "verb", "/pərˈfɛktɪŋ/", "hoàn thiện, trau chuốt hoàn hảo"),
    ("075442", "perfectionistic", "adj", "/pərˌfɛkʃəˈnɪstɪk/", "cầu toàn, đòi hỏi sự hoàn hảo"),
    ("075443", "perfectively", "adv", "/pərˈfɛktɪvli/", "thuộc thể hoàn thành (ngữ pháp)"),
    ("075444", "perfectiveness", "noun", "/pərˈfɛktɪvnəs/", "tính hoàn hảo; thể hoàn thành"),
    ("075445", "perfectivity", "noun", "/ˌpɜːrfɛkˈtɪvɪti/", "tính chất thể hoàn thành"),
    ("075446", "perfectness", "noun", "/ˈpɜːrfɪktnəs/", "sự hoàn hảo, sự toàn mỹ"),
    ("075447", "perfecto", "noun", "/pərˈfɛktoʊ/", "điếu xì gà perfecto (thon hai đầu)"),
    ("075448", "perfects", "verb", "/pərˈfɛkts/", "hoàn thiện, làm cho hoàn hảo"),
    ("075449", "perfervid", "adj", "/pərˈfɜːrvɪd/", "nồng nhiệt sôi nổi thái quá"),
    ("075450", "perfervidly", "adv", "/pərˈfɜːrvɪdli/", "một cách nồng nhiệt mãnh liệt"),
    ("075451", "perfervidness", "noun", "/pərˈfɜːrvɪdnəs/", "sự nồng nhiệt mãnh liệt"),
    ("075452", "perfidiousness", "noun", "/pərˈfɪdiəsnəs/", "sự bội bạc, sự phản trắc"),
    ("075453", "perfoliate", "adj", "/pərˈfoʊliɪt/", "có lá ôm xuyên thân (thực vật)"),
    ("075454", "perfoliation", "noun", "/pərˌfoʊliˈeɪʃən/", "tính trạng lá ôm xuyên thân"),
    ("075455", "perforable", "adj", "/ˈpɜːrfərəbəl/", "có thể đục thủng, khoan thủng"),
    ("075456", "perforates", "verb", "/ˈpɜːrfəˌreɪts/", "đục thủng, khoan lỗ xuyên qua"),
    ("075457", "perforating", "verb", "/ˈpɜːrfəˌreɪtɪŋ/", "đục thủng, khoan lỗ xuyên qua"),
    ("075458", "perforative", "adj", "/ˈpɜːrfərətɪv/", "có tác dụng đục thủng, xuyên qua"),
    ("075459", "perforator", "noun", "/ˈpɜːrfəreɪtər/", "máy đục lỗ; dụng cụ khoan xuyên"),
    ("075460", "performable", "adj", "/pərˈfɔːrməbəl/", "có thể thực hiện, biểu diễn được"),
    ("075461", "performances", "noun", "/pərˈfɔːrmənsɪz/", "buổi biểu diễn; hiệu suất làm việc"),
    ("075462", "performative", "noun", "/pərˈfɔːrmətɪv/", "lời nói hành động (ngữ dụng học)"),
    ("075463", "performed", "verb", "/pərˈfɔːrmd/", "đã thực hiện; đã biểu diễn"),
    ("075464", "performers", "noun", "/pərˈfɔːrmərz/", "người biểu diễn; diễn viên"),
    ("075465", "performs", "verb", "/pərˈfɔːrmz/", "thực hiện; biểu diễn"),
    ("075466", "perfumers", "noun", "/pərˈfjuːmərz/", "nhà điều chế nước hoa; người bán"),
    ("075467", "perfumes", "verb", "/pərˈfjuːmz/", "xức nước hoa; tỏa hương thơm"),
    ("075468", "perfumier", "noun", "/pərˈfjuːmiər/", "nhà điều chế nước hoa"),
    ("075469", "perfuming", "verb", "/pərˈfjuːmɪŋ/", "xức nước hoa; tỏa hương thơm"),
    ("075470", "perfunctoriness", "noun", "/pərˈfʌŋktərinəs/", "tính chiếu lệ, sự làm cho qua loa"),
    ("075471", "perfusions", "noun", "/pərˈfjuːʒənz/", "sự tưới máu; truyền dịch (y học)"),
    ("075472", "perfusive", "adj", "/pərˈfjuːsɪv/", "tràn ngập, rải khắp, thấm đẫm"),
    ("075473", "pergameneous", "adj", "/ˌpɜːrɡəˈmiːniəs/", "giống giấy da dê; dạng da mỏng"),
    ("075474", "periapical", "adj", "/ˌpɛriˈæpɪkəl/", "quanh chóp chân răng (nha khoa)"),
    ("075475", "periapt", "noun", "/ˈpɛriæpt/", "bùa đeo hộ mệnh (từ cổ)"),
    ("075476", "periarterial", "adj", "/ˌpɛriɑːrˈtɪriəl/", "quanh động mạch (giải phẫu)"),
    ("075477", "periarteritis", "noun", "/ˌpɛriˌɑːrtəˈraɪtɪs/", "bệnh viêm quanh động mạch (y học)"),
    ("075478", "periarthric", "adj", "/ˌpɛriˈɑːrθrɪk/", "quanh khớp xương (giải phẫu)"),
    ("075479", "periaxial", "adj", "/ˌpɛriˈæksiəl/", "quanh trục; bao quanh sợi trục"),
    ("075480", "periblast", "noun", "/ˈpɛrɪblæst/", "lớp tế bào quanh phôi (sinh học)"),
    ("075481", "periblastic", "adj", "/ˌpɛrɪˈblæstɪk/", "thuộc lớp quanh phôi (phôi học)"),
    ("075482", "periblem", "noun", "/ˈpɛrɪblɛm/", "tầng sinh vỏ sơ cấp (thực vật)"),
    ("075483", "peribranchial", "adj", "/ˌpɛrɪˈbræŋkiəl/", "quanh khe mang (giải phẫu)"),
    ("075484", "peribulbar", "adj", "/ˌpɛrɪˈbʌlbər/", "quanh nhãn cầu (y học)"),
    ("075485", "pericallis", "noun", "/ˌpɛrɪˈkælɪs/", "chi cúc bách hợp Pericallis"),
    ("075486", "pericambium", "noun", "/ˌpɛrɪˈkæmbiəm/", "tầng trụ bì, vòng sinh mạch"),
    ("075487", "pericapillary", "adj", "/ˌpɛrɪˈkæpɪˌlɛri/", "quanh mao mạch (y học)"),
    ("075488", "pericardia", "noun", "/ˌpɛrɪˈkɑːrdiə/", "màng ngoài tim (ngoại tâm mạc)"),
    ("075489", "pericardiac", "adj", "/ˌpɛrɪˈkɑːrdiæk/", "thuộc màng ngoài tim"),
    ("075490", "pericarpial", "adj", "/ˌpɛrɪˈkɑːrpiəl/", "thuộc vỏ quả (thực vật học)"),
    ("075491", "pericarps", "noun", "/ˈpɛrɪkɑːrps/", "vỏ quả (thực vật học)"),
    ("075492", "pericellular", "adj", "/ˌpɛrɪˈsɛljələr/", "quanh tế bào (sinh học)"),
    ("075493", "pericementoclasia", "noun", "/ˌpɛrɪsɪˌmɛntoʊˈkleɪʒə/", "viêm quanh chân răng có mủ"),
    ("075494", "pericentric", "adj", "/ˌpɛrɪˈsɛntrɪk/", "quanh tâm động (di truyền học)"),
    ("075495", "perichondral", "adj", "/ˌpɛrɪˈkɒndrəl/", "thuộc màng sụn (giải phẫu)"),
    ("075496", "perichondria", "noun", "/ˌpɛrɪˈkɒndriə/", "màng sụn (giải phẫu)"),
    ("075497", "perichondrium", "noun", "/ˌpɛrɪˈkɒndriəm/", "màng sụn (giải phẫu)"),
    ("075498", "periclase", "noun", "/ˈpɛrɪkleɪz/", "khoáng vật magie oxit periclas"),
    ("075499", "periclinal", "adj", "/ˌpɛrɪˈklaɪnəl/", "song song bề mặt; nghiêng quanh vòm"),
    ("075500", "pericope", "noun", "/pəˈrɪkəpi/", "đoạn trích Kinh Thánh (nghi lễ)"),
    ("075501", "pericrania", "noun", "/ˌpɛrɪˈkreɪniə/", "màng ngoài xương sọ; hộp sọ"),
    ("075502", "pericranial", "adj", "/ˌpɛrɪˈkreɪniəl/", "thuộc màng ngoài xương sọ"),
]

with open("scratch/b36_r01_raw_p5.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r01_p5.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r01_p5 saved OK")
