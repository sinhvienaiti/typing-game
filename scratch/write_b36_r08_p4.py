import json

rows = [
    ("078803", "preoiling", "noun", "/ˌpriːˈɔɪlɪŋ/", "sự bôi trơn sơ bộ (động cơ)"),
    ("078804", "preopinion", "noun", "/ˌpriːəˈpɪnjən/", "thành kiến, ý kiến định sẵn trước"),
    ("078805", "preorbital", "adj", "/ˌpriːˈɔːrbɪtəl/", "ở phía trước hốc mắt (giải phẫu)"),
    ("078806", "preordain", "verb", "/ˌpriːɔːrˈdeɪn/", "định đoạt trước, tiền định an bài"),
    ("078807", "preordained", "verb", "/ˌpriːɔːrˈdeɪnd/", "đã định đoạt trước, tiền định"),
    ("078808", "preordaining", "verb", "/ˌpriːɔːrˈdeɪnɪŋ/", "định đoạt trước, tiền định an bài"),
    ("078809", "preordainment", "noun", "/ˌpriːɔːrˈdeɪnmənt/", "sự tiền định, sự định đoạt trước"),
    ("078810", "preordains", "verb", "/ˌpriːɔːrˈdeɪnz/", "định đoạt trước, tiền định an bài"),
    ("078811", "preordination", "noun", "/ˌpriːˌɔːrdɪˈneɪʃən/", "sự tiền định, sự sắp đặt từ trước"),
    ("078812", "preovarian", "adj", "/ˌpriːoʊˈvɛriən/", "ở phía trước buồng trứng (y học)"),
    ("078813", "preovulatory", "adj", "/ˌpriːˈɒvjʊlətɔːri/", "giai đoạn trước khi rụng trứng"),
    ("078814", "prepacks", "noun", "/ˈpriːpæks/", "hàng hóa đóng gói sẵn"),
    ("078815", "preparable", "adj", "/prɪˈpɛrəbəl/", "có thể chuẩn bị, pha chế được"),
    ("078816", "preparations", "noun", "/ˌprɛpəˈreɪʃənz/", "sự chuẩn bị; chế phẩm pha chế"),
    ("078817", "preparatively", "adv", "/prɪˈpærətɪvli/", "để chuẩn bị, mang tính chuẩn bị"),
    ("078818", "preparator", "noun", "/ˈprɛpəˌreɪtər/", "kỹ thuật viên chuẩn bị mẫu vật"),
    ("078819", "preparatorily", "adv", "/prɪˈpærətərɪli/", "với mục đích chuẩn bị trước"),
    ("078820", "preparedly", "adv", "/prɪˈpɛrɪdli/", "một cách có chuẩn bị sẵn sàng"),
    ("078821", "preparer", "noun", "/prɪˈpɛrər/", "người chuẩn bị, người lập hồ sơ"),
    ("078822", "prepares", "verb", "/prɪˈpɛrz/", "chuẩn bị, sửa soạn, pha chế"),
    ("078823", "preparietal", "adj", "/ˌpriːpəˈraɪɪtəl/", "ở phía trước xương đỉnh (sọ)"),
    ("078824", "preparing", "verb", "/prɪˈpɛrɪŋ/", "chuẩn bị, sửa soạn, pha chế"),
    ("078825", "prepatellar", "adj", "/ˌpriːpəˈtɛlər/", "ở phía trước xương bánh chè"),
    ("078826", "prepayable", "adj", "/ˌpriːˈpeɪəbəl/", "có thể trả trước, thanh toán trước"),
    ("078827", "prepayments", "noun", "/ˌpriːˈpeɪmənts/", "khoản trả trước; sự trả trước"),
    ("078828", "prepend", "verb", "/prɪˈpɛnd/", "gắn thêm vào phía đầu (tin học)"),
    ("078829", "prepense", "adj", "/prɪˈpɛns/", "có chủ ý từ trước, cố tình (luật)"),
    ("078830", "prepensely", "adv", "/prɪˈpɛnsli/", "một cách cố ý, tính toán từ trước"),
    ("078831", "preponderated", "verb", "/prɪˈpɒndəˌreɪtɪd/", "đã nặng hơn, chiếm ưu thế hơn"),
    ("078832", "preponderately", "adv", "/prɪˈpɒndərɪtli/", "chiếm phần lớn, trội hơn hẳn"),
    ("078833", "preponderates", "verb", "/prɪˈpɒndəˌreɪts/", "nặng hơn, chiếm ưu thế hơn hẳn"),
    ("078834", "preponderating", "adj", "/prɪˈpɒndəˌreɪtɪŋ/", "vượt trội hơn, có ảnh hưởng lớn hơn"),
    ("078835", "preponderation", "noun", "/prɪˌpɒndəˈreɪʃən/", "sự vượt trội hơn, ưu thế áp đảo"),
    ("078836", "prepose", "verb", "/ˌpriːˈpoʊz/", "đặt ở vị trí phía trước (từ)"),
    ("078837", "prepositionally", "adv", "/ˌprɛpəˈzɪʃənəli/", "với chức năng như một giới từ"),
    ("078838", "prepositions", "noun", "/ˌprɛpəˈzɪʃənz/", "giới từ (ngữ pháp)"),
    ("078839", "prepositive", "adj", "/prɪˈpɒzɪtɪv/", "đứng trước (tiếp đầu tố, giới từ)"),
    ("078840", "prepositively", "adv", "/prɪˈpɒzɪtɪvli/", "ở vị trí đứng trước"),
    ("078841", "prepossess", "verb", "/ˌpriːpəˈzɛs/", "tạo ấn tượng tốt sẵn; chiếm giữ"),
    ("078842", "prepossessed", "verb", "/ˌpriːpəˈzɛst/", "đã có ấn tượng sẵn; bị định kiến"),
    ("078843", "prepossesses", "verb", "/ˌpriːpəˈzɛsɪz/", "tạo ấn tượng tốt sẵn; chiếm giữ"),
    ("078844", "prepossessingly", "adv", "/ˌpriːpəˈzɛsɪŋli/", "một cách duyên dáng dễ gây cảm tình"),
    ("078845", "prepossessingness", "noun", "/ˌpriːpəˈzɛsɪŋnəs/", "vẻ duyên dáng, sức thu hút cảm tình"),
    ("078846", "prepossession", "noun", "/ˌpriːpəˈzɛʃən/", "định kiến có sẵn; sự chiếm trước"),
    ("078847", "preposterousness", "noun", "/prɪˈpɒstərəsnəs/", "sự phi lý nực cười, vô lý hết sức"),
    ("078848", "prepotence", "noun", "/prɪˈpoʊtəns/", "sự trội hẳn, quyền lực áp đảo"),
    ("078849", "prepotency", "noun", "/prɪˈpoʊtənsi/", "tính trội di truyền; sức mạnh trội"),
    ("078850", "prepotent", "adj", "/prɪˈpoʊtənt/", "hùng mạnh vượt trội; tính trội gen"),
    ("078851", "prepotently", "adv", "/prɪˈpoʊtəntli/", "với sức mạnh vượt trội áp đảo"),
    ("078852", "preppy", "adj", "/ˈprɛpi/", "chỉnh chu kiểu sinh viên trường tư"),
    ("078853", "preprandial", "adj", "/ˌpriːˈprændiəl/", "trước bữa ăn (như khai vị)"),
    ("078854", "preprint", "noun", "/ˈpriːprɪnt/", "bản thảo tiền ấn bản (khoa học)"),
    ("078855", "preprocess", "noun", "/ˈpriːˌprɑːsɛs/", "tiền xử lý (dữ liệu, vật liệu)"),
    ("078856", "preprocessing", "noun", "/ˌpriːˈprɑːsɛsɪŋ/", "quá trình tiền xử lý (dữ liệu)"),
    ("078857", "preprocessor", "noun", "/ˌpriːˈprɑːsɛsər/", "bộ tiền xử lý (trình biên dịch)"),
    ("078858", "preprofessional", "adj", "/ˌpriːprəˈfɛʃənəl/", "tiền chuyên nghiệp (dự bị nghề)"),
    ("078859", "preprogrammed", "adj", "/ˌpriːˈproʊɡræmd/", "được lập trình sẵn từ trước"),
    ("078860", "preprophase", "noun", "/ˌpriːˈproʊfeɪz/", "giai đoạn tiền kỳ đầu (phân bào)"),
    ("078861", "prepuberal", "adj", "/ˌpriːˈpjuːbərəl/", "trước tuổi dậy thì; trước xương mu"),
    ("078862", "prepuberty", "noun", "/ˌpriːˈpjuːbərti/", "giai đoạn tiền dậy thì"),
    ("078863", "prepubic", "adj", "/ˌpriːˈpjuːbɪk/", "ở phía trước xương mu (giải phẫu)"),
    ("078864", "prepublication", "adj", "/ˌpriːˌpʌblɪˈkeɪʃən/", "trước khi xuất bản (bản thảo)"),
    ("078865", "prepulsing", "noun", "/ˌpriːˈpʌlsɪŋ/", "sự phát xung kích trước"),
    ("078866", "prepupa", "noun", "/ˌpriːˈpjuːpə/", "giai đoạn tiền nhộng (côn trùng)"),
    ("078867", "prepupal", "adj", "/ˌpriːˈpjuːpəl/", "thuộc giai đoạn tiền nhộng"),
    ("078868", "preputial", "adj", "/prɪˈpjuːʃəl/", "thuộc bao quy đầu (giải phẫu)"),
    ("078869", "preputium", "noun", "/prɪˈpjuːʃəm/", "bao quy đầu (giải phẫu)"),
    ("078870", "prequel", "noun", "/ˈpriːkwəl/", "phần tiền truyện (phim, sách)"),
    ("078871", "prerecording", "verb", "/ˌpriːrɪˈkɔːrdɪŋ/", "thu âm trước, ghi hình sẵn"),
    ("078872", "prerecords", "verb", "/ˌpriːrɪˈkɔːrdz/", "thu âm trước, ghi hình sẵn"),
    ("078873", "preregister", "verb", "/ˌpriːˈrɛdʒɪstər/", "đăng ký trước (học phần, sự kiện)"),
    ("078874", "preregistered", "verb", "/ˌpriːˈrɛdʒɪstərd/", "đã đăng ký trước từ đầu"),
    ("078875", "preregistering", "verb", "/ˌpriːˈrɛdʒɪstərɪŋ/", "đăng ký trước từ đầu"),
    ("078876", "preregisters", "verb", "/ˌpriːˈrɛdʒɪstərz/", "đăng ký trước từ đầu"),
    ("078877", "preroast", "noun", "/ˈpriːroʊst/", "sự rang hoặc thiêu quặng sơ bộ"),
    ("078878", "prerogatived", "adj", "/prɪˈrɒɡətɪvd/", "được ban đặc quyền, đặc ân"),
    ("078879", "prerouting", "verb", "/ˌpriːˈruːtɪŋ/", "định tuyến sơ bộ (PREROUTING)"),
    ("078880", "pres", "noun", "/prɛz/", "tổng thống, chủ tịch (viết tắt)"),
    ("078881", "presacious", "adj", "/prɪˈseɪʃəs/", "ăn thịt sống, săn mồi (biến thể)"),
    ("078882", "presaged", "verb", "/ˈprɛsɪdʒd/", "đã báo hiệu trước, dự báo điềm"),
    ("078883", "presageful", "adj", "/ˈprɛsɪdʒfəl/", "đầy điềm báo trước, dự cảm"),
    ("078884", "presager", "noun", "/ˈprɛsɪdʒər/", "người tiên đoán, vật báo điềm trước"),
    ("078885", "presages", "verb", "/ˈprɛsɪdʒɪz/", "báo hiệu trước, dự báo điềm"),
    ("078886", "presaging", "verb", "/ˈprɛsɪdʒɪŋ/", "báo hiệu trước, dự báo điềm"),
    ("078887", "presanctified", "adj", "/ˌpriːˈsæŋktɪfaɪd/", "đã được thánh hiến trước (lễ nghi)"),
    ("078888", "presbyope", "noun", "/ˈprɛzbioʊp/", "người mắc tật lão thị (nhãn khoa)"),
    ("078889", "presbyopic", "adj", "/ˌprɛzbiˈɒpɪk/", "bị lão thị (viễn thị tuổi già)"),
    ("078890", "presbyteral", "adj", "/prɛzˈbɪtərəl/", "thuộc trưởng lão giáo hội, linh mục"),
    ("078891", "presbyterial", "adj", "/ˌprɛzbɪˈtɪriəl/", "thuộc trưởng lão giáo hội, linh mục"),
    ("078892", "presbyterially", "adv", "/ˌprɛzbɪˈtɪriəli/", "theo chế độ trưởng lão (giáo hội)"),
    ("078893", "presbyters", "noun", "/ˈprɛzbɪtərz/", "trưởng lão giáo hội; linh mục"),
    ("078894", "presbytes", "noun", "/prɛzˈbaɪtiːz/", "chi khỉ voọc (Presbytis)"),
    ("078895", "prescientific", "adj", "/ˌpriːsaɪənˈtɪfɪk/", "tiền khoa học (trước khoa học)"),
    ("078896", "prescind", "verb", "/prɪˈsɪnd/", "gạt ra ngoài, không xét tới"),
    ("078897", "prescriber", "noun", "/prɪˈskraɪbər/", "bác sĩ kê đơn thuốc; người quy định"),
    ("078898", "prescribes", "verb", "/prɪˈskraɪbz/", "kê đơn thuốc; quy định bắt buộc"),
    ("078899", "prescribing", "verb", "/prɪˈskraɪbɪŋ/", "kê đơn thuốc; quy định bắt buộc"),
    ("078900", "prescriptions", "noun", "/prɪˈskrɪpʃənz/", "đơn thuốc; quy định bắt buộc"),
    ("078901", "prescriptively", "adv", "/prɪˈskrɪptɪvli/", "theo quy tắc, mang tính quy phạm"),
    ("078902", "prescriptiveness", "noun", "/prɪˈskrɪptɪvnəs/", "tính quy phạm, tính áp đặt chuẩn"),
]

with open("scratch/b36_r08_raw_p4.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r08_p4.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r08_p4 saved OK")
