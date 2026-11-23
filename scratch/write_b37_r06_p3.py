import json

records = [
    ("082703", "remarried", "verb", "/ˌriːˈmɛrid/", "đã tái hôn, đã kết hôn lần nữa"),
    ("082704", "remarries", "verb", "/ˌriːˈmɛriz/", "tái hôn, đi bước nữa sau ly hôn"),
    ("082705", "remarrying", "verb", "/ˌriːˈmɛriɪŋ/", "tái hôn, kết hôn lại lần nữa"),
    ("082706", "remble", "verb", "/ˈrɛmbəl/", "dọn dẹp gọn gàng; cuỗm lấy (cổ)"),
    ("082707", "rembrandtesque", "adj", "/ˌrɛmbrænˈtɛsk/", "theo phong cách họa sĩ Rembrandt"),
    ("082708", "remedied", "verb", "/ˈrɛmədid/", "đã khắc phục, đã cứu chữa sai sót"),
    ("082709", "remedies", "verb", "/ˈrɛmədiz/", "khắc phục, sửa chữa, chữa trị bệnh"),
    ("082710", "remediless", "adj", "/ˈrɛmədɪləs/", "vô phương cứu chữa, không thể sửa"),
    ("082711", "remedying", "verb", "/ˈrɛmədiɪŋ/", "khắc phục, sửa chữa, điều trị bệnh"),
    ("082712", "remelting", "noun", "/ˌriːˈmɛltɪŋ/", "quá trình nấu chảy lại kim loại"),
    ("082713", "rememberable", "adj", "/rɪˈmɛmbərəbəl/", "đáng ghi nhớ, dễ nhớ lâu"),
    ("082714", "remembered", "verb", "/rɪˈmɛmbərd/", "đã nhớ lại, đã ghi nhớ"),
    ("082715", "remembers", "verb", "/rɪˈmɛmbərz/", "nhớ lại, ghi nhớ trong tâm trí"),
    ("082716", "remembrancer", "noun", "/rɪˈmɛmbrənsər/", "vật kỷ niệm nhắc nhớ; quan thu nợ"),
    ("082717", "remetal", "verb", "/ˌriːˈmɛtəl/", "rải đá lại mặt đường; tráng kim lại"),
    ("082718", "remex", "noun", "/ˈriːmɛks/", "lông bay chính trên cánh chim"),
    ("082719", "remiges", "noun", "/ˈrɛməˌdʒiːz/", "các lông bay ở cánh chim (động vật)"),
    ("082720", "remigial", "adj", "/rɪˈmɪdʒiəl/", "thuộc lông bay cánh chim"),
    ("082721", "remigrate", "verb", "/ˌriːˈmaɪɡreɪt/", "di cư trở lại, hồi cư về quê cũ"),
    ("082722", "remigrated", "verb", "/ˌriːˈmaɪɡreɪtɪd/", "đã di cư trở lại quê hương cũ"),
    ("082723", "remigrates", "verb", "/ˌriːˈmaɪɡreɪts/", "di cư trở lại, hồi cư về vùng cũ"),
    ("082724", "remigrating", "verb", "/ˌriːˈmaɪɡreɪtɪŋ/", "di cư trở về nơi xuất phát ban đầu"),
    ("082725", "remilegia", "noun", "/ˌrɛməˈliːdʒə/", "chi cá ép bám cá voi (Remilegia)"),
    ("082726", "remilitarisation", "noun", "/riˌmɪlɪtəraɪˈzeɪʃən/", "sự tái quân sự hóa (Anh)"),
    ("082727", "remilitarise", "verb", "/riˈmɪlɪtəˌraɪz/", "tái quân sự hóa khu vực (Anh)"),
    ("082728", "remilitarize", "verb", "/riˈmɪlɪtəˌraɪz/", "tái quân sự hóa, vũ trang trở lại"),
    ("082729", "reminded", "verb", "/rɪˈmaɪndɪd/", "đã nhắc nhở, đã gợi nhớ lại"),
    ("082730", "remindful", "adj", "/rɪˈmaɪndfəl/", "hay gợi nhớ, nhắc nhở lại kỷ niệm"),
    ("082731", "reminding", "verb", "/rɪˈmaɪndɪŋ/", "nhắc nhở; làm gợi nhớ đến"),
    ("082732", "reminds", "verb", "/rɪˈmaɪndz/", "nhắc nhở; gợi nhớ lại điều gì"),
    ("082733", "reminisced", "verb", "/ˌrɛməˈnɪst/", "đã hồi tưởng, ôn lại chuyện xưa"),
    ("082734", "reminiscently", "adv", "/ˌrɛməˈnɪsəntli/", "với vẻ hồi tưởng bâng khuâng"),
    ("082735", "reminisces", "verb", "/ˌrɛməˈnɪsɪz/", "hồi tưởng, kể lại kỷ niệm xưa"),
    ("082736", "reminiscing", "verb", "/ˌrɛməˈnɪsɪŋ/", "hồi tưởng, ôn lại kỷ niệm cũ"),
    ("082737", "remint", "verb", "/ˌriːˈmɪnt/", "đúc lại tiền xu mới từ tiền cũ"),
    ("082738", "remissible", "adj", "/rɪˈmɪsəbəl/", "có thể tha thứ, được miễn giảm"),
    ("082739", "remissiness", "noun", "/rɪˈmɪsinəs/", "sự cẩu thả, tính tắc trách lơ là"),
    ("082740", "remissive", "adj", "/rɪˈmɪsɪv/", "làm dịu đi, giảm bớt (cơn đau, sốt)"),
    ("082741", "remissly", "adv", "/rɪˈmɪsli/", "một cách cẩu thả, lơ là thiếu trách"),
    ("082742", "remissness", "noun", "/rɪˈmɪsnəs/", "sự cẩu thả, tính chểnh mảng lơ là"),
    ("082743", "remitment", "noun", "/rɪˈmɪtmənt/", "khoản tiền chuyển gửi; sự miễn giảm"),
    ("082744", "remits", "verb", "/rɪˈmɪts/", "chuyển tiền; miễn giảm; chuyển lên"),
    ("082745", "remittal", "noun", "/rɪˈmɪtəl/", "sự chuyển tiền; sự tha miễn tội"),
    ("082746", "remitted", "verb", "/rɪˈmɪtɪd/", "đã chuyển tiền; đã tha miễn giảm"),
    ("082747", "remittee", "noun", "/ˌriːmɪˈtiː/", "người nhận tiền chuyển khoản đến"),
    ("082748", "remitter", "noun", "/rɪˈmɪtər/", "người chuyển tiền, người gửi tiền"),
    ("082749", "remitting", "verb", "/rɪˈmɪtɪŋ/", "chuyển tiền; miễn giảm; dịu đi"),
    ("082750", "remnants", "noun", "/ˈrɛmnənts/", "tàn dư, phần thừa còn sót lại"),
    ("082751", "remodelled", "verb", "/ˌriːˈmɑːdəld/", "đã tu sửa cải tạo nhà (Anh)"),
    ("082752", "remodelling", "verb", "/ˌriːˈmɑːdəlɪŋ/", "tu sửa cải tạo lại kiến trúc (Anh)"),
    ("082753", "remodels", "verb", "/ˌriːˈmɑːdəlz/", "tu sửa, cải tạo lại kiến trúc"),
    ("082754", "remolded", "verb", "/ˌriːˈmoʊldɪd/", "đã đúc lại khuôn, uốn nắn lại"),
    ("082755", "remolding", "verb", "/ˌriːˈmoʊldɪŋ/", "đúc lại khuôn mới, định hình lại"),
    ("082756", "remolds", "verb", "/ˌriːˈmoʊldz/", "đúc lại khuôn, cải tạo nắn lại"),
    ("082757", "remonetise", "verb", "/riˈmɑːnəˌtaɪz/", "khôi phục làm tiền tệ hợp pháp"),
    ("082758", "remonetization", "noun", "/riˌmɑːnətəˈzeɪʃən/", "sự khôi phục vai trò tiền tệ"),
    ("082759", "remonetize", "verb", "/riˈmɑːnəˌtaɪz/", "khôi phục lại làm tiền tệ hợp pháp"),
    ("082760", "remonstrant", "adj", "/rɪˈmɑːnstrənt/", "mang tính can gián, phản kháng nhẹ"),
    ("082761", "remonstrated", "verb", "/rɪˈmɑːnstreɪtɪd/", "đã phản đối, đã khuyên can gay gắt"),
    ("082762", "remonstrates", "verb", "/rɪˈmɑːnstreɪts/", "phản đối kịch liệt, lên tiếng can"),
    ("082763", "remonstrating", "verb", "/rɪˈmɑːnstreɪtɪŋ/", "phản đối gay gắt, khuyên can ngăn"),
    ("082764", "remonstration", "noun", "/ˌrɛmənˈstreɪʃən/", "lời phản đối gay gắt, sự can gián"),
    ("082765", "remonstrative", "adj", "/rɪˈmɑːnstrətɪv/", "có tính chất phản đối, quở trách"),
    ("082766", "remonstrator", "noun", "/ˈrɛmənˌstreɪtər/", "người lên tiếng phản đối, can gián"),
    ("082767", "remontant", "adj", "/rɪˈmɑːntənt/", "nở hoa nhiều lần trong năm (cây)"),
    ("082768", "remontoir", "noun", "/ˌrɛmənˈtwɑːr/", "cơ cấu truyền lực đều cho đồng hồ"),
    ("082769", "remorsefulness", "noun", "/rɪˈmɔːrsfəlnəs/", "sự ân hận, nỗi day dứt lương tâm"),
    ("082770", "remotion", "noun", "/rɪˈmoʊʃən/", "sự dời chỗ, sự loại bỏ (từ cổ)"),
    ("082771", "remotor", "noun", "/rɪˈmoʊtər/", "cơ kéo giật lùi (ở giáp xác)"),
    ("082772", "remotorings", "noun", "/riˈmoʊtərɪŋz/", "các lần thay động cơ mới cho tàu"),
    ("082773", "remoulded", "verb", "/ˌriːˈmoʊldɪd/", "đã đúc lại khuôn, uốn nắn lại (Anh)"),
    ("082774", "remoulding", "verb", "/ˌriːˈmoʊldɪŋ/", "đúc lại khuôn mới, nắn lại (Anh)"),
    ("082775", "remoulds", "verb", "/ˌriːˈmoʊldz/", "đúc lại khuôn, uốn nắn lại (Anh)"),
    ("082776", "remounted", "verb", "/ˌriːˈmaʊntɪd/", "đã lên ngựa lại; đã lắp lại khung"),
    ("082777", "remounting", "verb", "/ˌriːˈmaʊntɪŋ/", "trèo lên lại; lắp ráp lại khung giá"),
    ("082778", "remounts", "verb", "/ˌriːˈmaʊnts/", "lên ngựa lại; lắp lại khung giá mới"),
    ("082779", "remous", "noun", "/rəˈmuː/", "xoáy nước; dòng khí xoáy ngược"),
    ("082780", "removability", "noun", "/rɪˌmuːvəˈbɪləti/", "tính tháo lắp được; thể cách chức"),
    ("082781", "removes", "verb", "/rɪˈmuːvz/", "dời đi, tháo bỏ, loại bỏ, xóa bỏ"),
    ("082782", "removing", "verb", "/rɪˈmuːvɪŋ/", "loại bỏ, gỡ bỏ, dọn dẹp chuyển đi"),
    ("082783", "remunerates", "verb", "/rɪˈmjuːnəˌreɪts/", "trả thù lao, đền bù công sức"),
    ("082784", "remunerating", "verb", "/rɪˈmjuːnəˌreɪtɪŋ/", "trả thù lao, đền bù công sức"),
    ("082785", "remunerator", "noun", "/rɪˈmjuːnəˌreɪtər/", "người trả thù lao, người đền đáp"),
    ("082786", "ren", "noun", "/rɛn/", "quả thận (giải phẫu Latin)"),
    ("082787", "renaissances", "noun", "/ˌrɛnəˈsɑːnsɪz/", "những thời kỳ phục hưng văn hóa"),
    ("082788", "renaissant", "adj", "/rɪˈneɪsənt/", "hồi sinh trở lại, kiểu Phục hưng"),
    ("082789", "renamed", "verb", "/ˌriːˈneɪmd/", "đã đổi tên, đã đặt tên mới cho"),
    ("082790", "renames", "verb", "/ˌriːˈneɪmz/", "đổi tên, đặt tên gọi mới khác"),
    ("082791", "renaming", "verb", "/ˌriːˈneɪmɪŋ/", "đổi tên gọi, đặt tên mới cho vật"),
    ("082792", "renature", "verb", "/riˈneɪtʃər/", "phục hồi cấu trúc tự nhiên (sinh)"),
    ("082793", "rencontre", "noun", "/rɑːnˈkɑːntrə/", "cuộc gặp gỡ bất ngờ; cuộc đụng độ"),
    ("082794", "rencounter", "noun", "/rɛnˈkaʊntər/", "cuộc chạm trán, cuộc gặp gỡ bất ngờ"),
    ("082795", "rendered", "verb", "/ˈrɛndərd/", "đã làm cho; đã trao; kết xuất"),
    ("082796", "renders", "verb", "/ˈrɛndərz/", "làm cho; diễn tả; trao; kết xuất"),
    ("082797", "rendezvoused", "verb", "/ˈrɑːndeɪˌvuːd/", "đã hẹn gặp; đã tập kết điểm hẹn"),
    ("082798", "rendezvouses", "verb", "/ˈrɑːndeɪˌvuːz/", "hẹn gặp mặt; tập kết tại điểm hẹn"),
    ("082799", "rendezvousing", "verb", "/ˈrɑːndeɪˌvuːɪŋ/", "hẹn gặp nhau; tập kết tàu vũ trụ"),
    ("082800", "rendrynge", "noun", "/ˈrɛndrɪŋ/", "sự trình bày, sự diễn giải (cổ)"),
    ("082801", "renegaded", "verb", "/ˈrɛnəˌɡeɪdɪd/", "đã phản bội, đã bỏ đạo, đào ngũ"),
    ("082802", "renegades", "verb", "/ˈrɛnəˌɡeɪdz/", "phản bội phe phái, bỏ hàng ngũ"),
]

raw = json.load(open("scratch/b37_r06_raw_p3.json"))
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
with open("scratch/b37_r06_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r06_p3 saved OK")
