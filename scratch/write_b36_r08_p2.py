import json

rows = [
    ("078603", "predestines", "verb", "/priˈdɛstɪnz/", "định sẵn số phận, tiền định an bài"),
    ("078604", "predestining", "verb", "/priˈdɛstɪnɪŋ/", "định sẵn số phận, tiền định an bài"),
    ("078605", "predeterminate", "verb", "/ˌpriːdɪˈtɜːrmɪnɪt/", "định đoạt trước, tiền định trước"),
    ("078606", "predeterminer", "noun", "/ˌpriːdɪˈtɜːrmɪnər/", "từ hạn định trước (ngữ pháp)"),
    ("078607", "predetermines", "verb", "/ˌpriːdɪˈtɜːrmɪnz/", "định đoạt trước, quyết định trước"),
    ("078608", "predetermining", "verb", "/ˌpriːdɪˈtɜːrmɪnɪŋ/", "định đoạt trước, quyết định trước"),
    ("078609", "prediabetes", "noun", "/ˌpriːdaɪəˈbiːtiːz/", "tình trạng tiền tiểu đường (y học)"),
    ("078610", "prediabetic", "adj", "/ˌpriːdaɪəˈbɛtɪk/", "thuộc giai đoạn tiền tiểu đường"),
    ("078611", "predial", "adj", "/ˈpriːdiəl/", "thuộc ruộng đất, đất đai nông thôn"),
    ("078612", "predicability", "noun", "/ˌprɛdɪkəˈbɪlɪti/", "tính có thể khẳng định (logic)"),
    ("078613", "predicable", "adj", "/ˈprɛdɪkəbəl/", "có thể khẳng định được (logic)"),
    ("078614", "predicableness", "noun", "/ˈprɛdɪkəbəlnəs/", "tính có thể khẳng định được"),
    ("078615", "predicamental", "adj", "/ˌprɛdɪkəˈmɛntəl/", "thuộc tình thế khó xử; phạm trù"),
    ("078616", "predicamentally", "adv", "/ˌprɛdɪkəˈmɛntəli/", "trong tình thế khó xử, ngặt nghèo"),
    ("078617", "predicant", "adj", "/ˈprɛdɪkənt/", "mang tính rao giảng, thuyết giáo"),
    ("078618", "predicated", "verb", "/ˈprɛdɪˌkeɪtɪd/", "đã đặt cơ sở trên; đã khẳng định"),
    ("078619", "predicates", "verb", "/ˈprɛdɪˌkeɪts/", "đặt cơ sở trên; khẳng định"),
    ("078620", "predicating", "verb", "/ˈprɛdɪˌkeɪtɪŋ/", "đặt cơ sở trên; khẳng định"),
    ("078621", "predicational", "adj", "/ˌprɛdɪˈkeɪʃənəl/", "thuộc vị ngữ, thuộc sự khẳng định"),
    ("078622", "predicator", "noun", "/ˈprɛdɪˌkeɪtər/", "vị ngữ (ngôn ngữ học); từ vị từ"),
    ("078623", "predicatory", "adj", "/ˈprɛdɪkətɔːri/", "mang tính thuyết giáo, rao giảng"),
    ("078624", "predictabilities", "noun", "/prɪˌdɪktəˈbɪlɪtiz/", "tính chất có thể dự đoán trước"),
    ("078625", "predicted", "verb", "/prɪˈdɪktɪd/", "đã dự đoán, đã dự báo trước"),
    ("078626", "predicting", "verb", "/prɪˈdɪktɪŋ/", "dự đoán, dự báo trước"),
    ("078627", "predictively", "adv", "/prɪˈdɪktɪvli/", "mang tính chất dự báo, tiên đoán"),
    ("078628", "predictiveness", "noun", "/prɪˈdɪktɪvnəs/", "khả năng dự báo, độ tin cậy dự đoán"),
    ("078629", "predicts", "verb", "/prɪˈdɪkts/", "dự đoán, dự báo trước"),
    ("078630", "predigest", "verb", "/ˌpriːdaɪˈdʒɛst/", "tiêu hóa sơ bộ trước (thức ăn)"),
    ("078631", "predigesting", "verb", "/ˌpriːdaɪˈdʒɛstɪŋ/", "tiêu hóa sơ bộ trước (thức ăn)"),
    ("078632", "predigestion", "noun", "/ˌpriːdaɪˈdʒɛstʃən/", "sự tiêu hóa sơ bộ; xử lý trước"),
    ("078633", "predigests", "verb", "/ˌpriːdaɪˈdʒɛsts/", "tiêu hóa sơ bộ trước (thức ăn)"),
    ("078634", "predikant", "noun", "/ˈpreɪdɪkɑːnt/", "mục sư Cải cách Hà Lan (Nam Phi)"),
    ("078635", "predisposes", "verb", "/ˌpriːdɪˈspoʊzɪz/", "làm dễ mắc bệnh; tạo khuynh hướng"),
    ("078636", "predisposing", "verb", "/ˌpriːdɪˈspoʊzɪŋ/", "làm dễ mắc bệnh; tạo khuynh hướng"),
    ("078637", "predominated", "verb", "/prɪˈdɑːmɪˌneɪtɪd/", "đã chiếm ưu thế, trội hơn hẳn"),
    ("078638", "predominately", "adv", "/prɪˈdɑːmɪnəntli/", "chủ yếu là, chiếm phần lớn ưu thế"),
    ("078639", "predominates", "verb", "/prɪˈdɑːmɪˌneɪts/", "chiếm ưu thế, vượt trội hơn hẳn"),
    ("078640", "predominating", "verb", "/prɪˈdɑːmɪˌneɪtɪŋ/", "chiếm ưu thế, vượt trội hơn hẳn"),
    ("078641", "predominatingly", "adv", "/prɪˈdɑːmɪneɪtɪŋli/", "chiếm ưu thế áp đảo, chủ yếu"),
    ("078642", "predomination", "noun", "/prɪˌdɑːmɪˈneɪʃən/", "sự chiếm ưu thế, sự vượt trội"),
    ("078643", "predominator", "noun", "/prɪˈdɑːmɪˌneɪtər/", "nhân tố hoặc người chiếm ưu thế"),
    ("078644", "preemptor", "noun", "/priːˈɛmptər/", "người ưu tiên mua trước (luật)"),
    ("078645", "preener", "noun", "/ˈpriːnər/", "người hay chải chuốt, làm dáng"),
    ("078646", "preexist", "verb", "/ˌpriːɪɡˈzɪst/", "tồn tại từ trước, có sẵn từ trước"),
    ("078647", "preexisted", "verb", "/ˌpriːɪɡˈzɪstɪd/", "đã tồn tại từ trước, có sẵn trước"),
    ("078648", "preexistent", "adj", "/ˌpriːɪɡˈzɪstənt/", "tồn tại từ trước, có sẵn trước"),
    ("078649", "preexists", "verb", "/ˌpriːɪɡˈzɪsts/", "tồn tại từ trước, có sẵn từ trước"),
    ("078650", "prefabricate", "verb", "/ˌpriːˈfæbrɪˌkeɪt/", "sản xuất sẵn, đúc sẵn (cấu kiện)"),
    ("078651", "prefabricated", "verb", "/ˌpriːˈfæbrɪˌkeɪtɪd/", "đã đúc sẵn, lắp ghép sẵn"),
    ("078652", "prefabricates", "verb", "/ˌpriːˈfæbrɪˌkeɪts/", "đúc sẵn, chế tạo lắp ghép sẵn"),
    ("078653", "prefabricating", "verb", "/ˌpriːˈfæbrɪˌkeɪtɪŋ/", "đúc sẵn, chế tạo lắp ghép sẵn"),
    ("078654", "prefabricator", "noun", "/ˌpriːˈfæbrɪˌkeɪtər/", "nhà sản xuất cấu kiện đúc sẵn"),
    ("078655", "prefaced", "verb", "/ˈprɛfəst/", "đã mở đầu bằng, viết lời tựa cho"),
    ("078656", "prefacer", "noun", "/ˈprɛfəsər/", "người viết lời tựa, lời nói đầu"),
    ("078657", "prefaces", "verb", "/ˈprɛfəsɪz/", "mở đầu bằng, viết lời tựa cho"),
    ("078658", "prefacing", "verb", "/ˈprɛfəsɪŋ/", "mở đầu bằng, viết lời tựa cho"),
    ("078659", "prefactor", "noun", "/ˈpriːˌfæktər/", "thừa số đứng trước (toán, vật lý)"),
    ("078660", "prefaded", "adj", "/ˌpriːˈfeɪdɪd/", "được xử lý làm bạc màu sẵn (vải)"),
    ("078661", "prefatorial", "adj", "/ˌprɛfəˈtɔːriəl/", "thuộc lời nói đầu, mang tính mở đầu"),
    ("078662", "prefatorily", "adv", "/ˌprɛfəˈtɔːrɪli/", "với tư cách lời mở đầu, tựa dẫn"),
    ("078663", "prefectoral", "adj", "/prɪˈfɛktərəl/", "thuộc tỉnh trưởng, người giám thị"),
    ("078664", "prefectorial", "adj", "/ˌpriːfɛkˈtɔːriəl/", "thuộc tỉnh trưởng, người giám thị"),
    ("078665", "prefectures", "noun", "/ˈpriːfɛktʃərz/", "tỉnh, quận hành chính (Pháp, Nhật)"),
    ("078666", "preferability", "noun", "/ˌprɛfərəˈbɪlɪti/", "tính đáng ưa chuộng hơn, ưu thế hơn"),
    ("078667", "preferableness", "noun", "/ˈprɛfərəbəlnəs/", "tính đáng thích hơn, ưu tiên hơn"),
    ("078668", "preferendum", "noun", "/ˌprɛfəˈrɛndəm/", "ngưỡng môi trường ưa thích nhất"),
    ("078669", "preferent", "adj", "/ˈprɛfərənt/", "được ưu tiên hơn, được ưa thích"),
    ("078670", "preferentialism", "noun", "/ˌprɛfəˈrɛnʃəlɪzəm/", "chính sách ưu đãi thuế quan"),
    ("078671", "preferentialist", "noun", "/ˌprɛfəˈrɛnʃəlɪst/", "người ủng hộ chính sách ưu đãi"),
    ("078672", "preferrer", "noun", "/prɪˈfɜːrər/", "người thích hơn; người đệ đơn kiện"),
    ("078673", "preferring", "verb", "/prɪˈfɜːrɪŋ/", "thích hơn, ưa hơn; đệ trình"),
    ("078674", "prefers", "verb", "/prɪˈfɜːrz/", "thích hơn, ưa hơn; đệ trình"),
    ("078675", "prefet", "noun", "/preɪˈfeɪ/", "tỉnh trưởng, quận trưởng (Pháp)"),
    ("078676", "prefiguratively", "adv", "/prɪˈfɪɡjərətɪvli/", "mang tính điềm báo hình tượng"),
    ("078677", "prefigurativeness", "noun", "/prɪˈfɪɡjərətɪvnəs/", "tính chất báo hiệu trước"),
    ("078678", "prefigured", "verb", "/ˌpriːˈfɪɡjərd/", "đã hình dung trước, báo hiệu trước"),
    ("078679", "prefigurement", "noun", "/ˌpriːˈfɪɡjərmənt/", "dấu hiệu báo trước, hình bóng trước"),
    ("078680", "prefigures", "verb", "/ˌpriːˈfɪɡjərz/", "hình dung trước, báo hiệu trước"),
    ("078681", "prefiguring", "verb", "/ˌpriːˈfɪɡjərɪŋ/", "hình dung trước, báo hiệu trước"),
    ("078682", "prefixal", "adj", "/ˈpriːfɪksəl/", "thuộc tiền tố (ngôn ngữ học)"),
    ("078683", "prefixally", "adv", "/ˈpriːfɪksəli/", "dưới dạng tiền tố ở đầu từ"),
    ("078684", "prefixation", "noun", "/ˌpriːfɪkˈseɪʃən/", "sự gắn thêm tiền tố (ngôn ngữ học)"),
    ("078685", "prefixed", "verb", "/ˈpriːfɪkst/", "đã gắn tiền tố vào; đặt phía trước"),
    ("078686", "prefixes", "verb", "/ˈpriːfɪksɪz/", "gắn tiền tố vào; đặt ở phía trước"),
    ("078687", "prefixing", "verb", "/ˈpriːfɪksɪŋ/", "gắn tiền tố vào; đặt ở phía trước"),
    ("078688", "prefixs", "verb", "/ˈpriːfɪksɪz/", "gắn tiền tố vào; đặt ở phía trước"),
    ("078689", "preflight", "adj", "/ˌpriːˈflaɪt/", "chuẩn bị trước chuyến bay"),
    ("078690", "prefoliation", "noun", "/ˌpriːfoʊliˈeɪʃən/", "cách xếp lá non trong chồi búp"),
    ("078691", "preformation", "noun", "/ˌpriːfɔːrˈmeɪʃən/", "sự tiền định hình (phôi học)"),
    ("078692", "preformative", "adj", "/prɪˈfɔːrmətɪv/", "tiền tố cấu tạo; hình thành trước"),
    ("078693", "preformed", "verb", "/ˌpriːˈfɔːrmd/", "đã định hình sẵn từ trước"),
    ("078694", "preforming", "verb", "/ˌpriːˈfɔːrmɪŋ/", "định hình sơ bộ từ trước"),
    ("078695", "preformism", "noun", "/ˌpriːˈfɔːrmɪzəm/", "thuyết tiền thành (sinh học cổ)"),
    ("078696", "preforms", "verb", "/ˌpriːˈfɔːrmz/", "định hình sơ bộ từ trước"),
    ("078697", "prefreezing", "noun", "/ˌpriːˈfriːzɪŋ/", "sự cấp đông sơ bộ trước"),
    ("078698", "prefusion", "noun", "/ˌpriːˈfjuːʒən/", "giai đoạn tiền nóng chảy"),
    ("078699", "preganglionic", "adj", "/ˌpriːˌɡæŋɡliˈɒnɪk/", "trước hạch thần kinh (giải phẫu)"),
    ("078700", "pregenital", "adj", "/ˌpriːˈdʒɛnɪtəl/", "tiền sinh dục (tâm phân học)"),
    ("078701", "preggers", "adj", "/ˈprɛɡərz/", "đang mang thai, có bầu (khẩu ngữ)"),
    ("078702", "preglacial", "adj", "/ˌpriːˈɡleɪʃəl/", "trước thời kỳ băng hà (địa chất)"),
]

with open("scratch/b36_r08_raw_p2.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r08_p2.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r08_p2 saved OK")
