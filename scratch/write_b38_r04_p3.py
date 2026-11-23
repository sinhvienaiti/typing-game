import json

RECORDS = [
    ("086703", "shiptainer", "noun", "/ˈʃɪpˌteɪnər/", "cần trục giàn bốc xếp container"),
    ("086704", "shipworm", "noun", "/ˈʃɪpˌwɜːrm/", "con hà đục gỗ tàu biển"),
    ("086705", "shir", "noun", "/ʃɜːr/", "dải thun; sợi chun co giãn"),
    ("086706", "shiraoi", "noun", "/ʃɪˈraʊi/", "thị trấn Shiraoi (Hokkaido, Nhật)"),
    ("086707", "shirked", "verb", "/ʃɜːrkt/", "đã trốn tránh nghĩa vụ"),
    ("086708", "shirks", "verb", "/ʃɜːrks/", "trốn tránh trách nhiệm"),
    ("086709", "shirr", "verb", "/ʃɜːr/", "may rút nhún chỉ chun; nướng trứng"),
    ("086710", "shirred", "verb", "/ʃɜːrd/", "đã may rút nhún; đã nướng khuôn"),
    ("086711", "shirrs", "verb", "/ʃɜːrz/", "may rút nhún chun; nướng khuôn"),
    ("086712", "shirtily", "adv", "/ˈʃɜːrtɪli/", "cáu kỉnh; bực dọc khó chịu"),
    ("086713", "shirtiness", "noun", "/ˈʃɜːrtinəs/", "tính hay cáu kỉnh; sự bực dọc"),
    ("086714", "shirtless", "adj", "/ˈʃɜːrtləs/", "ở trần; không mặc áo"),
    ("086715", "shirts", "noun", "/ʃɜːrts/", "áo sơ mi"),
    ("086716", "shirtwaister", "noun", "/ˈʃɜːrtˌweɪstər/", "váy liền sơ mi thắt eo"),
    ("086717", "shishkabob", "noun", "/ˈʃɪʃkəˌbɑːb/", "thịt xiên nướng kiểu Trung Đông"),
    ("086718", "shitbowl", "noun", "/ˈʃɪtˌboʊl/", "chậu bẩn; tình cảnh tệ (thô tục)"),
    ("086719", "shitlips", "noun", "/ˈʃɪtˌlɪps/", "kẻ ăn nói thô lỗ (tiếng lóng)"),
    ("086720", "shits", "verb", "/ʃɪts/", "đại tiện; phóng uế (thô tục)"),
    ("086721", "shittah", "noun", "/ˈʃɪtə/", "cây gỗ keo vùng Kinh Thánh"),
    ("086722", "shitted", "verb", "/ˈʃɪtɪd/", "đã đại tiện (thô tục)"),
    ("086723", "shittimwood", "noun", "/ˈʃɪtəmˌwʊd/", "gỗ cây keo đóng Hòm Giao Ước"),
    ("086724", "shitwork", "noun", "/ˈʃɪtˌwɜːrk/", "việc vặt nhàm chán nặng nhọc (lóng)"[:35]),
    ("086725", "shivaism", "noun", "/ˈʃɪvəˌɪzəm/", "Ấn Độ giáo tôn thờ thần Shiva"),
    ("086726", "shivaist", "noun", "/ˈʃɪvəɪst/", "tín đồ thờ thần Shiva"),
    ("086727", "shivered", "verb", "/ˈʃɪvərd/", "đã run rẩy; đã vỡ tan từng mảnh"),
    ("086728", "shivers", "verb", "/ˈʃɪvərz/", "run rẩy vì lạnh sợ; vỡ vụn ra"),
    ("086729", "shivoo", "noun", "/ʃɪˈvuː/", "buổi tiệc tùng náo nhiệt (Úc)"),
    ("086730", "shlemiel", "noun", "/ʃləˈmiːl/", "người hậu đậu vụng về hay gặp xui"),
    ("086731", "shlep", "noun", "/ʃlɛp/", "chuyến đi vất vả; người vụng về"),
    ("086732", "shlepper", "noun", "/ˈʃlɛpər/", "người khuân vác; kẻ vụng về"),
    ("086733", "shlimazel", "noun", "/ʃlɪˈmɑːzəl/", "kẻ xui xẻo kinh niên"),
    ("086734", "shlockmeister", "noun", "/ˈʃlɑːkˌmaɪstər/", "kẻ buôn bán đồ dỏm rẻ tiền"),
    ("086735", "shmaltz", "noun", "/ʃmɑːlts/", "sự sướt mướt ủy mị; mỡ gà"),
    ("086736", "shmear", "noun", "/ʃmɪr/", "lớp phết kem; tiền đút lót"),
    ("086737", "shmegegge", "noun", "/ʃməˈɡɛɡi/", "chuyện nhảm nhí; kẻ khờ khạo"),
    ("086738", "shmo", "noun", "/ʃmoʊ/", "kẻ khờ khạo ngốc nghếch (lóng)"),
    ("086739", "shmoose", "verb", "/ʃmuːz/", "tán gẫu thân mật tạo quan hệ"),
    ("086740", "shmooze", "noun", "/ʃmuːz/", "cuộc trò chuyện xã giao thân mật"),
    ("086741", "shnook", "noun", "/ʃnʊk/", "người ngây thơ dễ bị lợi dụng"),
    ("086742", "shnorr", "verb", "/ʃnɔːr/", "xin xỏ ăn chực; năn nỉ vay mượn"),
    ("086743", "shnorrer", "noun", "/ˈʃnɔːrər/", "kẻ ăn bám chuyên xin xỏ"),
    ("086744", "shoaled", "verb", "/ʃoʊld/", "đã cạn dần; đã tụ thành đàn cá"),
    ("086745", "shoaling", "verb", "/ˈʃoʊlɪŋ/", "đang cạn dần; đang tụ đàn cá"),
    ("086746", "shoals", "verb", "/ʃoʊlz/", "trở nên nông cạn; tụ thành đàn"),
    ("086747", "shoaly", "adj", "/ˈʃoʊli/", "nhiều bãi cát cạn; nhiều đá ngầm"),
    ("086748", "shockingness", "noun", "/ˈʃɑːkɪŋnəs/", "tính chất gây sốc; sự kinh hoàng"),
    ("086749", "shocks", "verb", "/ʃɑːks/", "gây sốc; làm chấn động; giật điện"),
    ("086750", "shodden", "adj", "/ˈʃɑːdən/", "được đóng móng; có mang giày"),
    ("086751", "shoebills", "noun", "/ˈʃuːˌbɪlz/", "cò mỏ giày châu Phi"),
    ("086752", "shoebird", "noun", "/ˈʃuːˌbɜːrd/", "chim mỏ giày (cò mỏ giày)"),
    ("086753", "shoeblack", "noun", "/ˈʃuːˌblæk/", "thợ đánh giày dạo"),
    ("086754", "shoeblacks", "noun", "/ˈʃuːˌblæks/", "thợ đánh giày dạo"),
    ("086755", "shoeful", "noun", "/ˈʃuːˌfʊl/", "lượng chứa đầy một chiếc giày"),
    ("086756", "shoemakers", "noun", "/ˈʃuːˌmeɪkərz/", "thợ đóng giày; thợ sửa giày"),
    ("086757", "shoen", "noun", "/ʃuːn/", "đôi giày (dạng cổ)"),
    ("086758", "shoetree", "noun", "/ˈʃuːˌtriː/", "cốt giữ phom giày"),
    ("086759", "shogunal", "adj", "/ˈʃoʊɡənəl/", "thuộc chế độ Mạc phủ Nhật Bản"),
    ("086760", "shone", "verb", "/ʃoʊn/", "đã chiếu sáng; đã tỏa sáng"),
    ("086761", "shooed", "verb", "/ʃuːd/", "đã xua đuổi đi"),
    ("086762", "shooing", "verb", "/ˈʃuːɪŋ/", "đang xua đuổi đi"),
    ("086763", "shoos", "verb", "/ʃuːz/", "xua đuổi đi (bằng tiếng suỵt)"),
    ("086764", "shooters", "noun", "/ˈʃuːtərz/", "xạ thủ; tay súng; ly rượu nhỏ"),
    ("086765", "shophar", "noun", "/ˈʃoʊfɑːr/", "kèn tù và sừng cừu Do Thái"),
    ("086766", "shopman", "noun", "/ˈʃɑːpmən/", "chủ tiệm; nhân viên bán hàng"),
    ("086767", "shopmen", "noun", "/ˈʃɑːpmən/", "chủ tiệm; nhân viên bán hàng"),
    ("086768", "shopped", "verb", "/ʃɑːpt/", "đã đi mua sắm; đã tố giác"),
    ("086769", "shoppy", "adj", "/ˈʃɑːpi/", "đậm mùi nghề nghiệp; nhiều cửa hiệu"[:35]),
    ("086770", "shops", "verb", "/ʃɑːps/", "đi mua sắm; tố giác ai cho công an"[:35]),
    ("086771", "shopsoiled", "adj", "/ˈʃɑːpˌsɔɪld/", "hơi cũ sờn do trưng bày ở tiệm"),
    ("086772", "shopwalker", "noun", "/ˈʃɑːpˌwɔːkər/", "quản lý tầng cửa hàng bách hóa"),
    ("086773", "shopwindow", "noun", "/ˌʃɑːpˈwɪndoʊ/", "tủ kính trưng bày cửa hàng"),
    ("086774", "shortages", "noun", "/ˈʃɔːrtɪdʒɪz/", "sự thiếu hụt; tình trạng khan hiếm"[:35]),
    ("086775", "shortcomings", "noun", "/ˈʃɔːrtˌkʌmɪŋz/", "thiếu sót; khuyết điểm; nhược điểm"[:35]),
    ("086776", "shorted", "verb", "/ˈʃɔːrtɪd/", "đã đoản mạch; đã bán khống"),
    ("086777", "shortens", "verb", "/ˈʃɔːrtənz/", "rút ngắn; làm ngắn lại"),
    ("086778", "shorter", "adj", "/ˈʃɔːrtər/", "ngắn hơn; thấp hơn"),
    ("086779", "shortest", "adj", "/ˈʃɔːrtɪst/", "ngắn nhất; thấp nhất"),
    ("086780", "shortia", "noun", "/ˈʃɔːrtiə/", "chi hoa chuông núi Shortia"),
    ("086781", "shorting", "verb", "/ˈʃɔːrtɪŋ/", "đang đoản mạch; đang bán khống"),
    ("086782", "shortlived", "adj", "/ˌʃɔːrtˈlɪvd/", "ngắn ngủi; chết yểu"),
    ("086783", "shorty", "noun", "/ˈʃɔːrti/", "người thấp bé; phim ngắn"),
    ("086784", "shoshonean", "noun", "/ʃəˈʃoʊniən/", "ngữ tộc Shoshone (Bắc Mỹ)"),
    ("086785", "shoshonian", "noun", "/ʃəˈʃoʊniən/", "người Shoshone; ngữ tộc Shoshone"),
    ("086786", "shotcrust", "noun", "/ˈʃɔːrtˌkrʌst/", "vỏ bánh nướng giòn bở"),
    ("086787", "shotdrilling", "noun", "/ˈʃɑːtˌdrɪlɪŋ/", "phương pháp khoan đá bằng bi thép"),
    ("086788", "shote", "noun", "/ʃoʊt/", "heo con vừa cai sữa"),
    ("086789", "shotted", "adj", "/ˈʃɑːtɪd/", "đã nạp đạn bi; nặng chì"),
    ("086790", "shotten", "adj", "/ˈʃɑːtən/", "đã đẻ hết trứng (cá trích)"),
    ("086791", "shotting", "noun", "/ˈʃɑːtɪŋ/", "quá trình tạo hạt bi kim loại"),
    ("086792", "shotty", "adj", "/ˈʃɑːti/", "cứng tròn như viên đạn bi"),
    ("086793", "shouldering", "verb", "/ˈʃoʊldərɪŋ/", "đang vác lên vai; đang gánh vác"),
    ("086794", "shoulders", "verb", "/ˈʃoʊldərz/", "vác trên vai; gánh vác trách nhiệm"[:35]),
    ("086795", "shouts", "verb", "/ʃaʊts/", "hét lớn; la to; khao chầu rượu"),
    ("086796", "shoved", "verb", "/ʃʌvd/", "đã xô đẩy mạnh; đã nhét vào"),
    ("086797", "shovelbill", "noun", "/ˈʃʌvəlˌbɪl/", "vịt mỏ thìa"),
    ("086798", "shovelboard", "noun", "/ˈʃʌvəlˌbɔːrd/", "trò chơi đẩy đĩa gỗ trên bàn"),
    ("086799", "shovelled", "verb", "/ˈʃʌvəld/", "đã xúc bằng xẻng; đã hốt"),
    ("086800", "shovelling", "verb", "/ˈʃʌvəlɪŋ/", "đang xúc bằng xẻng; đang hốt"),
    ("086801", "shovelman", "noun", "/ˈʃʌvəlmən/", "công nhân xúc đất bằng xẻng"),
    ("086802", "shovelmen", "noun", "/ˈʃʌvəlmən/", "công nhân xúc đất bằng xẻng"),
]

# Remove slices cleanly <= 35 chars
RECORDS[21] = ("086724", "shitwork", "noun", "/ˈʃɪtˌwɜːrk/", "việc vặt nhàm chán nặng nhọc")
RECORDS[66] = ("086769", "shoppy", "adj", "/ˈʃɑːpi/", "đậm chuyện nghề; nhiều cửa tiệm")
RECORDS[67] = ("086770", "shops", "verb", "/ʃɑːps/", "đi mua sắm; đi tố giác ai")
RECORDS[71] = ("086774", "shortages", "noun", "/ˈʃɔːrtɪdʒɪz/", "sự thiếu hụt; sự khan hiếm")
RECORDS[72] = ("086775", "shortcomings", "noun", "/ˈʃɔːrtˌkʌmɪŋz/", "thiếu sót; khuyết điểm")
RECORDS[91] = ("086794", "shoulders", "verb", "/ˈʃoʊldərz/", "vác lên vai; gánh vác gánh nặng")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r04_raw_p3.json"))
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

json.dump(out, open("scratch/b38_r04_reviewed_p3.json", "w"), ensure_ascii=False, indent=2)
print("b38_r04_p3 saved OK")
