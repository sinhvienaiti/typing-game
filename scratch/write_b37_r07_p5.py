import json

RECORDS = [
    ("083403", "retroflected", "adj", "/ˌrɛtrəˈflɛktɪd/", "gập ngả ra phía sau"),
    ("083404", "retroflection", "noun", "/ˌrɛtrəˈflɛkʃən/", "sự ngả ra sau; sự gập ra sau"),
    ("083405", "retroflexed", "adj", "/ˌrɛtrəˈflɛkst/", "cong ngược ra sau; ngả ra sau"),
    ("083406", "retroflexion", "noun", "/ˌrɛtrəˈflɛkʃən/", "sự ngả ra sau; sự uốn lưỡi"),
    ("083407", "retrogradation", "noun", "/ˌrɛtrəɡrəˈdeɪʃən/", "sự đi ngược; sự nghịch hành"),
    ("083408", "retrograded", "verb", "/ˈrɛtrəˌɡreɪdɪd/", "đã thoái hóa; đã đi lùi"),
    ("083409", "retrogrades", "verb", "/ˈrɛtrəˌɡreɪdz/", "thoái hóa; đi lùi"),
    ("083410", "retrograding", "verb", "/ˈrɛtrəˌɡreɪdɪŋ/", "đang thoái hóa; đang đi lùi"),
    ("083411", "retrogress", "verb", "/ˌrɛtrəˈɡrɛs/", "thoái hóa; suy giảm"),
    ("083412", "retrogressed", "verb", "/ˌrɛtrəˈɡrɛst/", "đã thoái hóa; đã suy giảm"),
    ("083413", "retrogresses", "verb", "/ˌrɛtrəˈɡrɛsɪz/", "thoái hóa; suy giảm"),
    ("083414", "retrogressing", "verb", "/ˌrɛtrəˈɡrɛsɪŋ/", "đang thoái hóa; đang suy giảm"),
    ("083415", "retrogressively", "adv", "/ˌrɛtrəˈɡrɛsɪvli/", "theo chiều thụt lùi; thoái hóa"),
    ("083416", "retrogressives", "noun", "/ˌrɛtrəˈɡrɛsɪvz/", "người bảo thủ; xu hướng thụt lùi"),
    ("083417", "retroinsular", "adj", "/ˌrɛtroʊˈɪnsjələr/", "ở sau thùy đảo"),
    ("083418", "retroiridian", "adj", "/ˌrɛtroʊaɪˈrɪdiən/", "ở sau mống mắt"),
    ("083419", "retroject", "verb", "/ˌrɛtrəˈdʒɛkt/", "ném về phía sau; phóng ngược"),
    ("083420", "retrolingual", "adj", "/ˌrɛtroʊˈlɪŋɡwəl/", "ở sau lưỡi"),
    ("083421", "retromandibular", "adj", "/ˌrɛtroʊmænˈdɪbjələr/", "ở sau xương hàm dưới"),
    ("083422", "retromorphosis", "noun", "/ˌrɛtroʊmɔːrˈfoʊsɪs/", "sự thoái biến"),
    ("083423", "retronasal", "adj", "/ˌrɛtroʊˈneɪzəl/", "ở sau mũi; sau khoang mũi"),
    ("083424", "retronym", "noun", "/ˈrɛtrəˌnɪm/", "từ đặt lại để phân biệt nghĩa cũ"),
    ("083425", "retroocular", "adj", "/ˌrɛtroʊˈɑːkjələr/", "ở sau mắt"),
    ("083426", "retrooperative", "adj", "/ˌrɛtroʊˈɑːpərətɪv/", "có hiệu lực hồi tố"),
    ("083427", "retropack", "noun", "/ˈrɛtroʊˌpæk/", "cụm tên lửa hãm tàu vũ trụ"),
    ("083428", "retroperitoneal", "adj", "/ˌrɛtroʊˌpɛrɪtəˈniːəl/", "sau phúc mạc; sau màng bụng"),
    ("083429", "retropharingeal", "adj", "/ˌrɛtroʊfəˈrɪndʒiəl/", "ở sau hầu"),
    ("083430", "retrophyllum", "noun", "/ˌrɛtroʊˈfɪləm/", "chi cây lá kim Retrophyllum"),
    ("083431", "retroposition", "noun", "/ˌrɛtroʊpəˈzɪʃən/", "sự dịch chuyển ra sau"),
    ("083432", "retropubic", "adj", "/ˌrɛtroʊˈpjuːbɪk/", "ở sau xương mu"),
    ("083433", "retrorocket", "noun", "/ˈrɛtroʊˌrɑːkɪt/", "tên lửa hãm; động cơ đẩy ngược"),
    ("083434", "retrorse", "adj", "/rɪˈtrɔːrs/", "quặt ngược ra sau; cong ngược"),
    ("083435", "retros", "noun", "/ˈrɛtroʊz/", "phong cách hoài cổ"),
    ("083436", "retrosection", "noun", "/ˌrɛtroʊˈsɛkʃən/", "phép cắt từ phía sau"),
    ("083437", "retrousse", "adj", "/ˌrɛtruːˈseɪ/", "hếch lên (mũi)"),
    ("083438", "retrovert", "verb", "/ˌrɛtrəˈvɜːrt/", "quay ngược lại; ngả ra sau"),
    ("083439", "retroverted", "adj", "/ˌrɛtrəˈvɜːrtɪd/", "ngả ra sau"),
    ("083440", "retrovision", "noun", "/ˌrɛtroʊˈvɪʒən/", "sự hồi tưởng quá khứ"),
    ("083441", "retrying", "verb", "/ˌriːˈtraɪɪŋ/", "đang xử lại; đang thử lại"),
    ("083442", "rettery", "noun", "/ˈrɛtəri/", "bể ngâm giầm đay gai"),
    ("083443", "retting", "noun", "/ˈrɛtɪŋ/", "sự ngâm giầm đay gai"),
    ("083444", "retubing", "noun", "/ˌriːˈtuːbɪŋ/", "sự thay ống"),
    ("083445", "returned", "verb", "/rɪˈtɜːrnd/", "đã trở lại; đã trả lại"),
    ("083446", "returnee", "noun", "/rɪˌtɜːrˈniː/", "người trở về; người hồi hương"),
    ("083447", "returner", "noun", "/rɪˈtɜːrnər/", "người trở về; người trả lại"),
    ("083448", "returns", "verb", "/rɪˈtɜːrnz/", "trở về; trả lại"),
    ("083449", "retuse", "adj", "/rɪˈtuːs/", "có đầu tù hơi lõm (lá)"),
    ("083450", "retyre", "verb", "/ˌriːˈtaɪər/", "thay lốp xe"),
    ("083451", "reunified", "verb", "/ˌriːˈjuːnəˌfaɪd/", "đã thống nhất lại"),
    ("083452", "reunifies", "verb", "/ˌriːˈjuːnəˌfaɪz/", "thống nhất lại"),
    ("083453", "reunifying", "verb", "/ˌriːˈjuːnəˌfaɪɪŋ/", "đang thống nhất lại"),
    ("083454", "reunionist", "noun", "/ˌriːˈjuːnjənɪst/", "người chủ trương hợp nhất"),
    ("083455", "reunionistic", "adj", "/ˌriːˌjuːnjəˈnɪstɪk/", "chủ trương hợp nhất"),
    ("083456", "reunited", "verb", "/ˌriːjuːˈnaɪtɪd/", "đã đoàn tụ; đã tái hợp"),
    ("083457", "reunites", "verb", "/ˌriːjuːˈnaɪts/", "đoàn tụ; tái hợp"),
    ("083458", "reuniting", "verb", "/ˌriːjuːˈnaɪtɪŋ/", "đang đoàn tụ; đang tái hợp"),
    ("083459", "reusing", "verb", "/ˌriːˈjuːzɪŋ/", "đang tái sử dụng"),
    ("083460", "revaccinate", "verb", "/ˌriːˈvæksəˌneɪt/", "tiêm chủng lại"),
    ("083461", "revaccination", "noun", "/ˌriːˌvæksəˈneɪʃən/", "sự tiêm chủng lại"),
    ("083462", "revalidate", "verb", "/ˌriːˈvælɪˌdeɪt/", "gia hạn hiệu lực; xác nhận lại"),
    ("083463", "revalorization", "noun", "/ˌriːˌvælərəˈzeɪʃən/", "sự khôi phục giá trị tiền tệ"),
    ("083464", "revalorize", "verb", "/ˌriːˈvæləˌraɪz/", "khôi phục giá trị tiền tệ"),
    ("083465", "revaluate", "verb", "/ˌriːˈvæljuˌeɪt/", "đánh giá lại; nâng giá trị"),
    ("083466", "revamped", "verb", "/ˌriːˈvæmpt/", "đã sửa sang lại; đã cải tổ"),
    ("083467", "revamping", "verb", "/ˌriːˈvæmpɪŋ/", "đang sửa sang lại; đang cải tổ"),
    ("083468", "revamps", "verb", "/ˌriːˈvæmps/", "sửa sang lại; cải tổ"),
    ("083469", "revanch", "noun", "/rəˈvɑːnʃ/", "sự trả thù; sự phục thù"),
    ("083470", "revanchism", "noun", "/rəˈvɑːnʃɪzəm/", "chủ nghĩa phục thù"),
    ("083471", "revanchist", "adj", "/rəˈvɑːnʃɪst/", "thuộc chủ nghĩa phục thù"),
    ("083472", "revealable", "adj", "/rɪˈviːləbəl/", "có thể tiết lộ; có thể bộc lộ"),
    ("083473", "revealed", "verb", "/rɪˈviːld/", "đã tiết lộ; đã bộc lộ"),
    ("083474", "reveals", "verb", "/rɪˈviːlz/", "tiết lộ; bộc lộ"),
    ("083475", "revegetate", "verb", "/ˌriːˈvɛdʒɪˌteɪt/", "trồng phủ xanh lại thảm thực vật"),
    ("083476", "revelationist", "noun", "/ˌrɛvəˈleɪʃənɪst/", "người tin vào sự mặc khải"),
    ("083477", "revelator", "noun", "/ˈrɛvəˌleɪtər/", "người tiết lộ; người mặc khải"),
    ("083478", "revelled", "verb", "/ˈrɛvəld/", "đã vui chơi tưng bừng; chè chén"),
    ("083479", "revelling", "verb", "/ˈrɛvəlɪŋ/", "đang vui chơi tưng bừng"),
    ("083480", "revels", "verb", "/ˈrɛvəlz/", "vui chơi tưng bừng; chè chén"),
    ("083481", "revendication", "noun", "/rɪˌvɛndɪˈkeɪʃən/", "sự đòi lại; yêu sách đòi lại"),
    ("083482", "revenged", "verb", "/rɪˈvɛndʒd/", "đã trả thù"),
    ("083483", "revengefully", "adv", "/rɪˈvɛndʒfəli/", "đầy thù hận; hằn học trả thù"),
    ("083484", "revengefulness", "noun", "/rɪˈvɛndʒfəlnəs/", "óc trả thù; tính thù dai"),
    ("083485", "revengeless", "adj", "/rɪˈvɛndʒləs/", "không trả thù; không báo thù"),
    ("083486", "revenger", "noun", "/rɪˈvɛndʒər/", "người trả thù"),
    ("083487", "revenges", "verb", "/rɪˈvɛndʒɪz/", "trả thù"),
    ("083488", "revenging", "verb", "/rɪˈvɛndʒɪŋ/", "đang trả thù"),
    ("083489", "revenuer", "noun", "/ˈrɛvəˌnuːər/", "nhân viên thuế vụ"),
    ("083490", "reverb", "noun", "/ˈriːvɜːrb/", "hiệu ứng vang âm; độ dội âm"),
    ("083491", "reverberance", "noun", "/rɪˈvɜːrbərəns/", "sự vang dội; độ vang"),
    ("083492", "reverberated", "verb", "/rɪˈvɜːrbəˌreɪtɪd/", "đã vang dội; đã dội lại"),
    ("083493", "reverberates", "verb", "/rɪˈvɜːrbəˌreɪts/", "vang dội; dội lại"),
    ("083494", "reverberative", "adj", "/rɪˈvɜːrbəˌreɪtɪv/", "vang dội; dội lại"),
    ("083495", "reverberator", "noun", "/rɪˈvɜːrbəˌreɪtər/", "lò phản xạ; gương phản xạ"),
    ("083496", "reverberators", "noun", "/rɪˈvɜːrbəˌreɪtərz/", "lò phản xạ; gương phản xạ"),
    ("083497", "reverberatory", "adj", "/rɪˈvɜːrbərəˌtɔːri/", "vang dội; phản xạ nhiệt"),
    ("083498", "reverenced", "verb", "/ˈrɛvərənst/", "đã tôn kính; đã sùng kính"),
    ("083499", "reverences", "verb", "/ˈrɛvərənsɪz/", "tôn kính; sùng kính"),
    ("083500", "reverencing", "verb", "/ˈrɛvərənsɪŋ/", "đang tôn kính; đang sùng kính"),
    ("083501", "reveres", "verb", "/rɪˈvɪrz/", "tôn kính; kính trọng sâu sắc"),
    ("083502", "revering", "verb", "/rɪˈvɪrɪŋ/", "đang tôn kính"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r07_raw_p5.json"))
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

json.dump(out, open("scratch/b37_r07_reviewed_p5.json", "w"), ensure_ascii=False, indent=2)
print("b37_r07_p5 saved OK")
