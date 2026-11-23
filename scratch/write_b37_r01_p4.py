import json

records = [
    ("080303", "publiciser", "noun", "/ˈpʌblɪˌsaɪzər/", "người quảng bá, tuyên truyền (Anh)"),
    ("080304", "publicists", "noun", "/ˈpʌblɪsɪsts/", "những nhà quảng bá truyền thông"),
    ("080305", "publicities", "noun", "/pəˈblɪsətiz/", "sự công khai; hoạt động quảng bá"),
    ("080306", "publicizer", "noun", "/ˈpʌblɪˌsaɪzər/", "người quảng bá, người công bố"),
    ("080307", "publicizes", "verb", "/ˈpʌblɪˌsaɪzɪz/", "quảng bá rộng rãi, công khai"),
    ("080308", "publicness", "noun", "/ˈpʌblɪknəs/", "tính công khai, tính công cộng"),
    ("080309", "publishes", "verb", "/ˈpʌblɪʃɪz/", "xuất bản; công bố, đăng tải"),
    ("080310", "pucciniaceae", "noun", "/ˌpʌksɪniˈeɪsiː/", "họ Nấm gỉ sắt (Pucciniaceae)"),
    ("080311", "puccoon", "noun", "/pəˈkuːn/", "cây puccoon (lấy thuốc nhuộm đỏ)"),
    ("080312", "pucka", "adj", "/ˈpʌkə/", "thượng hạng, đích thực (Anh-Ấn)"),
    ("080313", "puckerbush", "noun", "/ˈpʌkərˌbʌʃ/", "bụi cây rậm vùng hoang dã Bắc Mỹ"),
    ("080314", "puckered", "verb", "/ˈpʌkərd/", "đã nhăn lại, đã nhíu mày, chúm lại"),
    ("080315", "puckering", "verb", "/ˈpʌkərɪŋ/", "nhăn lại, chau lại, chúm môi lại"),
    ("080316", "puckers", "verb", "/ˈpʌkərz/", "nhăn lại, chau mày, chúm môi lại"),
    ("080317", "puckery", "adj", "/ˈpʌkəri/", "chát làm săn miệng; có nếp nhăn"),
    ("080318", "puckishly", "adv", "/ˈpʌkɪʃli/", "một cách tinh nghịch, láu lỉnh"),
    ("080319", "puckishness", "noun", "/ˈpʌkɪʃnəs/", "tính tinh nghịch, vẻ láu lỉnh"),
    ("080320", "puddening", "noun", "/ˈpʊdnɪŋ/", "miếng đệm dây thừng chống va chạm"),
    ("080321", "pudder", "verb", "/ˈpʌdər/", "làm náo loạn; vấy bẩn bùn lầy (cổ)"),
    ("080322", "puddingheaded", "adj", "/ˈpʊdɪŋˌhɛdɪd/", "đần độn, đầu óc chậm chạp"),
    ("080323", "puddingwife", "noun", "/ˈpʊdɪŋˌwaɪf/", "cá bàng chài đầu xanh Caribe"),
    ("080324", "puddingy", "adj", "/ˈpʊdɪŋi/", "nhũn như bánh pudding; mập ục ịch"),
    ("080325", "puddled", "verb", "/ˈpʌdəld/", "đã lội vũng nước; đã luyện gang"),
    ("080326", "puddler", "noun", "/ˈpʌdlər/", "thợ luyện gang thành sắt rèn"),
    ("080327", "puddles", "verb", "/ˈpʌdəlz/", "nghịch vũng bùn; luyện gang"),
    ("080328", "puddling", "verb", "/ˈpʌdlɪŋ/", "trát đất sét kín nước; luyện gang"),
    ("080329", "puddly", "adj", "/ˈpʌdli/", "có nhiều vũng nước đọng, lầy lội"),
    ("080330", "pudency", "noun", "/ˈpjuːdənsi/", "tính e thẹn, sự bẽn lẽn rụt rè"),
    ("080331", "pudenda", "noun", "/pjuːˈdɛndə/", "bộ phận sinh dục ngoài nữ (y học)"),
    ("080332", "pudendum", "noun", "/pjuːˈdɛndəm/", "cơ quan sinh dục ngoài (giải phẫu)"),
    ("080333", "pudginess", "noun", "/ˈpʌdʒinəs/", "vẻ mũm mĩm, dáng người tròn lẳn"),
    ("080334", "pudicity", "noun", "/pjuːˈdɪsəti/", "tính đoan trang, đức hạnh e ấp"),
    ("080335", "pudsy", "adj", "/ˈpʌdzi/", "mũm mĩm, tròn trĩnh, béo lùn"),
    ("080336", "puerilely", "adv", "/ˈpjʊərəli/", "một cách ấu trĩ, trẻ con"),
    ("080337", "puerilism", "noun", "/ˈpjʊərəˌlɪzəm/", "hành vi thoái lui trẻ con (y học)"),
    ("080338", "puerpera", "noun", "/pjuːˈɜːrpərə/", "sản phụ vừa sinh con (y học)"),
    ("080339", "puffbird", "noun", "/ˈpʌfˌbɜːrd/", "chim đầu to vùng nhiệt đới Mỹ"),
    ("080340", "puffily", "adv", "/ˈpʌfəli/", "phồng lên, sưng húp; thở hổn hển"),
    ("080341", "puffins", "noun", "/ˈpʌfɪnz/", "những con chim hải âu cổ rụt"),
    ("080342", "puffs", "verb", "/pʌfs/", "thở hổn hển; nhả khói; thổi phồng"),
    ("080343", "puggaree", "noun", "/ˈpʌɡəri/", "khăn quấn mũ chống nắng (Ấn Độ)"),
    ("080344", "pugging", "noun", "/ˈpʌɡɪŋ/", "hỗn hợp đất sét nhào; lớp cách âm"),
    ("080345", "puggree", "noun", "/ˈpʌɡri/", "khăn quấn mũ chống nắng (Ấn Độ)"),
    ("080346", "pugnaciously", "adv", "/pʌɡˈneɪʃəsli/", "một cách hiếu chiến, hay gây sự"),
    ("080347", "pugnaciousness", "noun", "/pʌɡˈneɪʃəsnəs/", "tính hiếu chiến, máu gây gổ"),
    ("080348", "puisne", "adj", "/ˈpjuːni/", "cấp dưới, hậu bối (luật pháp Anh)"),
    ("080349", "puissances", "noun", "/ˈpwɪsənsɪz/", "sức mạnh; bài nhảy cao vượt tường"),
    ("080350", "pujunan", "noun", "/ˈpuːdʒənən/", "ngữ hệ Maiduan (thổ dân California)"),
    ("080351", "puked", "verb", "/pjuːkt/", "đã nôn mửa, đã ói mửa (khẩu ngữ)"),
    ("080352", "pukes", "verb", "/pjuːks/", "nôn mửa, ói mửa (khẩu ngữ)"),
    ("080353", "pukkah", "adj", "/ˈpʌkə/", "chính hiệu, đích thực, đáng tin"),
    ("080354", "pulasan", "noun", "/pəˈlɑːsən/", "cây chôm chôm rừng, quả pulasan"),
    ("080355", "pulassan", "noun", "/pəˈlɑːsən/", "cây chôm chôm rừng, quả pulasan"),
    ("080356", "puled", "verb", "/pjuːld/", "đã rên rỉ, đã khóc thút thít"),
    ("080357", "puler", "noun", "/ˈpjuːlər/", "kẻ hay rên rỉ, người khóc nhè"),
    ("080358", "pules", "verb", "/pjuːlz/", "rên rỉ, khóc thút thít, kêu chiếp"),
    ("080359", "pulicaria", "noun", "/ˌpjʊləˈkɛriə/", "chi cúc bọ chét (Pulicaria)"),
    ("080360", "pulicidae", "noun", "/pjuːˈlɪsɪˌdiː/", "họ Bọ chét thường (Pulicidae)"),
    ("080361", "pulicide", "noun", "/ˈpjuːləˌsaɪd/", "thuốc diệt bọ chét"),
    ("080362", "puling", "verb", "/ˈpjuːlɪŋ/", "rên rỉ, khóc thút thít, than vãn"),
    ("080363", "pulingly", "adv", "/ˈpjuːlɪŋli/", "với giọng rên rỉ, khóc nhai nhải"),
    ("080364", "pulled", "verb", "/pʊld/", "đã kéo, đã giật; đã đạt được"),
    ("080365", "pullers", "noun", "/ˈpʊlərz/", "người kéo; dụng cụ tháo vòng bi"),
    ("080366", "pulleys", "noun", "/ˈpʊliz/", "những cái ròng rọc, puly"),
    ("080367", "pulls", "verb", "/pʊlz/", "kéo, lôi, giật; thu hút, đạt được"),
    ("080368", "pullulate", "verb", "/ˈpʌljəˌleɪt/", "nảy mầm; sinh sôi nảy nở, lúc nhúc"),
    ("080369", "pullulation", "noun", "/ˌpʌljəˈleɪʃən/", "sự nảy chồi; sự sinh sôi nhanh"),
    ("080370", "pullulative", "adj", "/ˈpʌljəˌleɪtɪv/", "sinh sôi nảy nở nhanh, nảy chồi"),
    ("080371", "pulman", "noun", "/ˈpʊlmən/", "toa xe lửa giường nằm Pullman"),
    ("080372", "pulmobranchia", "noun", "/ˌpʌlmoʊˈbræŋkiə/", "phổi sách (cơ quan hô hấp nhện)"),
    ("080373", "pulmogastric", "adj", "/ˌpʌlmoʊˈɡæstrɪk/", "thuộc phổi và dạ dày (giải phẫu)"),
    ("080374", "pulmolith", "noun", "/ˈpʌlməˌlɪθ/", "sỏi phổi, sỏi phế quản (y học)"),
    ("080375", "pulmonate", "adj", "/ˈpʌlməˌneɪt/", "có phổi, hô hấp bằng phổi (ốc)"),
    ("080376", "pulmonology", "noun", "/ˌpʊlməˈnɑːlədʒi/", "khoa hô hấp, chuyên khoa phổi"),
    ("080377", "pulmotor", "noun", "/ˈpʊlˌmoʊtər/", "máy trợ thở hồi sức cấp cứu (cũ)"),
    ("080378", "pulpar", "adj", "/ˈpʌlpər/", "thuộc tủy răng, thuộc mô mềm"),
    ("080379", "pulped", "verb", "/pʌlpt/", "đã nghiền thành bột; đã hủy giấy"),
    ("080380", "pulper", "noun", "/ˈpʌlpər/", "máy nghiền bột giấy; máy xát vỏ"),
    ("080381", "pulpify", "verb", "/ˈpʌlpəˌfaɪ/", "nghiền thành bột nhão, bột giấy"),
    ("080382", "pulpiness", "noun", "/ˈpʌlpinəs/", "tình trạng mềm nhão, nhiều cùi thịt"),
    ("080383", "pulping", "verb", "/ˈpʌlpɪŋ/", "nghiền thành bột giấy, nghiền nhão"),
    ("080384", "pulpiteer", "noun", "/ˌpʌlpɪˈtɪr/", "người thuyết giáo kém (châm biếm)"),
    ("080385", "pulpous", "adj", "/ˈpʌlpəs/", "mềm nhão, nhiều cùi thịt (quả)"),
    ("080386", "pulps", "verb", "/pʌlps/", "nghiền thành bột nhão; xát vỏ hạt"),
    ("080387", "pulsatance", "noun", "/ˈpʌlsətəns/", "tần số góc (vật lý, kỹ thuật điện)"),
    ("080388", "pulsated", "verb", "/ˈpʌlseɪtɪd/", "đã đập nhịp nhàng; đã rung động"),
    ("080389", "pulsates", "verb", "/ˈpʌlseɪts/", "đập nhịp nhàng, rung động đều đặn"),
    ("080390", "pulsatile", "adj", "/ˈpʌlsətəl/", "đập theo nhịp, có xung nhịp"),
    ("080391", "pulsating", "verb", "/ˈpʌlseɪtɪŋ/", "đập nhịp nhàng, phập phồng"),
    ("080392", "pulsative", "adj", "/ˈpʌlsətɪv/", "đập theo nhịp, mang tính xung nhịp"),
    ("080393", "pulsator", "noun", "/ˈpʌlseɪtər/", "bộ tạo xung; máy đãi kim cương"),
    ("080394", "pulsatory", "adj", "/ˈpʌlsəˌtɔːri/", "đập theo nhịp, có nhịp đập"),
    ("080395", "pulsed", "verb", "/pʌlst/", "đã đập mạch; đã phát xung"),
    ("080396", "pulser", "noun", "/ˈpʌlsər/", "máy phát xung điện (kỹ thuật)"),
    ("080397", "pulses", "verb", "/ˈpʌlsɪz/", "đập theo mạch; phát xung; nhấp nháy"),
    ("080398", "pulsimeter", "noun", "/pʌlˈsɪmɪtər/", "máy đo nhịp mạch đập (y học)"),
    ("080399", "pultaceous", "adj", "/pʌlˈteɪʃəs/", "mềm nhão như cháo bột (y học)"),
    ("080400", "pultation", "noun", "/pʌlˈteɪʃən/", "sự nghiền thành bột nhão"),
    ("080401", "pulverable", "adj", "/ˈpʌlvərəbəl/", "có thể tán nhỏ thành bột mịn"),
    ("080402", "pulverate", "verb", "/ˈpʌlvəˌreɪt/", "tán nhỏ, nghiền vụn thành bột mịn"),
]

raw = json.load(open("scratch/b37_r01_raw_p4.json"))
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
with open("scratch/b37_r01_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r01_p4 saved OK")
