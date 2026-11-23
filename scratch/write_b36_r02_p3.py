import json

rows = [
    ("075703", "persecutional", "adj", "/ˌpɜːrsɪˈkjuːʃənəl/", "thuộc sự ngược đãi, bức hại"),
    ("075704", "persecutive", "adj", "/ˈpɜːrsɪˌkjuːtɪv/", "có tính bức hại, ngược đãi"),
    ("075705", "persecutory", "adj", "/ˈpɜːrsɪkjətɔːri/", "có tính bức hại, trù dập"),
    ("075706", "persecutrix", "noun", "/ˈpɜːrsɪˌkjuːtrɪks/", "nữ kẻ bức hại, ngược đãi"),
    ("075707", "perseverant", "adj", "/ˌpɜːrsəˈvɪrənt/", "kiên trì, bền bỉ, nhẫn nại"),
    ("075708", "perseverate", "verb", "/pərˈsɛvəreɪt/", "lặp đi lặp lại lời nói (y học)"),
    ("075709", "persevered", "verb", "/ˌpɜːrsəˈvɪrd/", "đã kiên trì, bền bỉ theo đuổi"),
    ("075710", "perseveres", "verb", "/ˌpɜːrsəˈvɪrz/", "kiên trì, bền bỉ theo đuổi"),
    ("075711", "persic", "noun", "/ˈpɜːrsɪk/", "người Ba Tư; tiếng Ba Tư cổ"),
    ("075712", "persiennes", "noun", "/pərˈsiːɛnz/", "cửa chớp lá sách; vải hoa Ba Tư"),
    ("075713", "persism", "noun", "/ˈpɜːrsɪzəm/", "từ mượn tiếng Ba Tư; Hỏa giáo"),
    ("075714", "persisted", "verb", "/pərˈsɪstɪd/", "đã kiên trì; đã tiếp tục tồn tại"),
    ("075715", "persistences", "noun", "/pərˈsɪstənsɪz/", "sự kiên trì; tính bền vững"),
    ("075716", "persister", "noun", "/pərˈsɪstər/", "người kiên trì; tế bào dai dẳng"),
    ("075717", "persists", "verb", "/pərˈsɪsts/", "kiên trì; tiếp tục tồn tại"),
    ("075718", "personableness", "noun", "/ˈpɜːrsənəbəlnəs/", "vẻ duyên dáng, ưa nhìn, lịch thiệp"),
    ("075719", "personably", "adv", "/ˈpɜːrsənəbli/", "một cách duyên dáng, lịch thiệp"),
    ("075720", "personae", "noun", "/pərˈsoʊniː/", "nhân vật; hình tượng công chúng"),
    ("075721", "personalises", "verb", "/ˈpɜːrsənəlaɪzɪz/", "cá nhân hóa; ám chỉ cá nhân"),
    ("075722", "personalising", "verb", "/ˈpɜːrsənəlaɪzɪŋ/", "cá nhân hóa; ám chỉ cá nhân"),
    ("075723", "personalism", "noun", "/ˈpɜːrsənəlɪzəm/", "chủ nghĩa nhân vị (triết học)"),
    ("075724", "personalist", "noun", "/ˈpɜːrsənəlɪst/", "người theo thuyết nhân vị"),
    ("075725", "personalization", "noun", "/ˌpɜːrsənəlɪˈzeɪʃən/", "sự cá nhân hóa (theo sở thích)"),
    ("075726", "personalizes", "verb", "/ˈpɜːrsənəˌlaɪzɪz/", "cá nhân hóa; ám chỉ cá nhân"),
    ("075727", "personalizing", "verb", "/ˈpɜːrsənəˌlaɪzɪŋ/", "cá nhân hóa; ám chỉ cá nhân"),
    ("075728", "personalties", "noun", "/ˈpɜːrsənəltiz/", "động sản cá nhân (luật Anh-Mỹ)"),
    ("075729", "personas", "noun", "/pərˈsoʊnəz/", "nhân vật; hình tượng công chúng"),
    ("075730", "personate", "verb", "/ˈpɜːrsəneɪt/", "đóng vai; mạo danh, giả dạng"),
    ("075731", "personative", "adj", "/ˈpɜːrsəneɪtɪv/", "để đóng vai; mang tính giả dạng"),
    ("075732", "personator", "noun", "/ˈpɜːrsəˌneɪtər/", "diễn viên đóng vai; kẻ mạo danh"),
    ("075733", "personennamens", "noun", "/pɛrˈzoʊnənˌnɑːmənz/", "tên riêng cá nhân (tiếng Đức)"),
    ("075734", "personified", "verb", "/pərˈsɒnɪˌfaɪd/", "đã nhân cách hóa; là hiện thân của"),
    ("075735", "personifier", "noun", "/pərˈsɒnɪˌfaɪər/", "người nhân cách hóa; vật hiện thân"),
    ("075736", "personifies", "verb", "/pərˈsɒnɪˌfaɪz/", "nhân cách hóa; là hiện thân của"),
    ("075737", "personifying", "verb", "/pərˈsɒnɪˌfaɪɪŋ/", "nhân cách hóa; là hiện thân của"),
    ("075738", "persoonia", "noun", "/pərˈsuːniə/", "chi cây bụi geebung (Úc)"),
    ("075739", "perspectival", "adj", "/pərˈspɛktaɪvəl/", "thuộc phép phối cảnh, góc nhìn"),
    ("075740", "perspectively", "adv", "/pərˈspɛktɪvli/", "theo góc độ phối cảnh"),
    ("075741", "perspectivity", "noun", "/ˌpɜːrspɛkˈtɪvɪti/", "tính chất phép chiếu phối cảnh"),
    ("075742", "perspicaciously", "adv", "/ˌpɜːrspɪˈkeɪʃəsli/", "một cách sáng suốt, tinh tường"),
    ("075743", "perspicaciousness", "noun", "/ˌpɜːrspɪˈkeɪʃəsnəs/", "sự sáng suốt, tinh tường nhạy bén"),
    ("075744", "perspicuousness", "noun", "/pərˈspɪkjuəsnəs/", "sự rõ ràng, khúc chiết dễ hiểu"),
    ("075745", "perspirable", "adj", "/pərˈspaɪrəbəl/", "có thể toát mồ hôi; bay hơi qua"),
    ("075746", "perspirations", "noun", "/ˌpɜːrspəˈreɪʃənz/", "sự đổ mồ hôi; mồ hôi"),
    ("075747", "perspirative", "adj", "/pərˈspaɪrətɪv/", "làm toát mồ hôi, bài tiết mồ hôi"),
    ("075748", "perspiratory", "adj", "/pərˈspaɪrətɔːri/", "thuộc tuyến mồ hôi; gây đổ mồ hôi"),
    ("075749", "perspired", "verb", "/pərˈspaɪərd/", "đã đổ mồ hôi, toát mồ hôi"),
    ("075750", "perspirer", "noun", "/pərˈspaɪrər/", "người ra nhiều mồ hôi"),
    ("075751", "perspires", "verb", "/pərˈspaɪrz/", "đổ mồ hôi, toát mồ hôi"),
    ("075752", "perspiring", "verb", "/pərˈspaɪrɪŋ/", "đổ mồ hôi, toát mồ hôi"),
    ("075753", "persuaded", "verb", "/pərˈsweɪdɪd/", "đã thuyết phục, làm tin theo"),
    ("075754", "persuades", "verb", "/pərˈsweɪdz/", "thuyết phục, làm tin theo"),
    ("075755", "persuading", "verb", "/pərˈsweɪdɪŋ/", "thuyết phục, làm tin theo"),
    ("075756", "persuasibility", "noun", "/pərˌsweɪzəˈbɪlɪti/", "tính dễ bị thuyết phục"),
    ("075757", "persuasible", "adj", "/pərˈsweɪzəbəl/", "có thể thuyết phục được"),
    ("075758", "persuasibleness", "noun", "/pərˈsweɪzəbəlnəs/", "tính có thể thuyết phục được"),
    ("075759", "pertaincious", "adj", "/pərˈteɪnʃəs/", "ngoan cố, cố chấp (biến thể cũ)"),
    ("075760", "pertainciousness", "noun", "/pərˈteɪnʃəsnəs/", "tính ngoan cố, cố chấp (cổ)"),
    ("075761", "pertained", "verb", "/pərˈteɪnd/", "đã liên quan đến; thuộc về"),
    ("075762", "pertaining", "verb", "/pərˈteɪnɪŋ/", "liên quan đến; thuộc về"),
    ("075763", "pertains", "verb", "/pərˈteɪnz/", "liên quan đến; thuộc về"),
    ("075764", "pertainym", "noun", "/pərˈteɪnɪm/", "tính từ quan hệ (ngôn ngữ học)"),
    ("075765", "pertinaciously", "adv", "/ˌpɜːrtɪˈneɪʃəsli/", "một cách ngoan cố, bền bỉ bám sát"),
    ("075766", "pertinaciousness", "noun", "/ˌpɜːrtɪˈneɪʃəsnəs/", "tính ngoan cố, bền bỉ bám trụ"),
    ("075767", "pertinences", "noun", "/ˈpɜːrtɪnənsɪz/", "sự thích đáng, tính liên quan"),
    ("075768", "pertinency", "noun", "/ˈpɜːrtɪnənsi/", "tính thích đáng, sự xác đáng"),
    ("075769", "pertness", "noun", "/ˈpɜːrtnəs/", "vẻ xấc xược, hỗn láo, lanh chanh"),
    ("075770", "pertubative", "adj", "/pərˈtɜːrbətɪv/", "gây nhiễu loạn (biến thể cũ)"),
    ("075771", "perturbable", "adj", "/pərˈtɜːrbəbəl/", "dễ bị làm nhiễu loạn, xáo trộn"),
    ("075772", "perturbational", "adj", "/ˌpɜːrtərˈbeɪʃənəl/", "thuộc sự nhiễu loạn, xáo trộn"),
    ("075773", "perturbative", "adj", "/pərˈtɜːrbətɪv/", "gây nhiễu loạn, làm xáo trộn"),
    ("075774", "perturbs", "verb", "/pərˈtɜːrbz/", "làm xáo trộn, gây bối rối lo âu"),
    ("075775", "pertusaria", "noun", "/ˌpɜːrtəˈsɛriə/", "chi địa y Pertusaria"),
    ("075776", "pertusariaceae", "noun", "/ˌpɜːrtəsɛriˈeɪsiː/", "họ Địa y Pertusariaceae"),
    ("075777", "pertused", "adj", "/pərˈtjuːzd/", "bị đục lỗ thủng (sinh học)"),
    ("075778", "peruke", "noun", "/pəˈruːk/", "tóc giả nam giới (thế kỷ 17-18)"),
    ("075779", "peruked", "adj", "/pəˈruːkt/", "đội tóc giả cổ điển"),
    ("075780", "perusable", "adj", "/pəˈruːzəbəl/", "có thể đọc kỹ, xem xét được"),
    ("075781", "perused", "verb", "/pəˈruːzd/", "đã đọc kỹ, xem xét tỉ mỉ"),
    ("075782", "peruser", "noun", "/pəˈruːzər/", "người đọc kỹ, người xem xét"),
    ("075783", "peruses", "verb", "/pəˈruːzɪz/", "đọc kỹ, xem xét tỉ mỉ"),
    ("075784", "pervaded", "verb", "/pərˈveɪdɪd/", "đã lan tỏa khắp, thấm đẫm"),
    ("075785", "pervader", "noun", "/pərˈveɪdər/", "vật lan tỏa khắp, người thấm đẫm"),
    ("075786", "pervades", "verb", "/pərˈveɪdz/", "lan tỏa khắp, thấm đẫm"),
    ("075787", "pervading", "verb", "/pərˈveɪdɪŋ/", "lan tỏa khắp, thấm đẫm"),
    ("075788", "pervaporate", "verb", "/pərˈveɪpəreɪt/", "bay hơi thẩm thấu qua màng"),
    ("075789", "pervaporation", "noun", "/pərˌveɪpəˈreɪʃən/", "sự thẩm thấu bay hơi qua màng"),
    ("075790", "pervasion", "noun", "/pərˈveɪʒən/", "sự thấm đẫm, lan tỏa khắp nơi"),
    ("075791", "perve", "noun", "/pɜːrv/", "kẻ biến thái (từ lóng viết tắt)"),
    ("075792", "perversive", "adj", "/pərˈvɜːrsɪv/", "có xu hướng làm hư hỏng, bóp méo"),
    ("075793", "perverter", "noun", "/pərˈvɜːrtər/", "kẻ làm hư hỏng, kẻ xuyên tạc"),
    ("075794", "pervertible", "adj", "/pərˈvɜːrtəbəl/", "có thể bị bóp méo, làm hư hỏng"),
    ("075795", "perverting", "verb", "/pərˈvɜːrtɪŋ/", "làm hư hỏng; xuyên tạc, bóp méo"),
    ("075796", "perverts", "verb", "/pərˈvɜːrts/", "làm hư hỏng; xuyên tạc, bóp méo"),
    ("075797", "perviously", "adv", "/ˈpɜːrviəsli/", "có thể thấm qua được"),
    ("075798", "perviousness", "noun", "/ˈpɜːrviəsnəs/", "tính dễ thấm qua; tính cởi mở"),
    ("075799", "pesah", "noun", "/ˈpɛsɑːx/", "lễ Vượt Qua (Do Thái giáo)"),
    ("075800", "pesante", "adv", "/pəˈzɑːnteɪ/", "chơi nặng nề, trang trọng (nhạc)"),
    ("075801", "pesantran", "noun", "/pəˈsɑːntrɛn/", "trường nội trú Hồi giáo Indonesia"),
    ("075802", "pesewa", "noun", "/pəˈseɪwə/", "đồng xu pesewa (tiền Ghana)"),
]

with open("scratch/b36_r02_raw_p3.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r02_p3.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r02_p3 saved OK")
