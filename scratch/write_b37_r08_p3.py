import json

RECORDS = [
    ("083703", "rhynia", "noun", "/ˈraɪniə/", "chi thực vật hóa thạch Rhynia"),
    ("083704", "rhyniaceae", "noun", "/ˌraɪniˈeɪsiːˌiː/", "họ Rhyniaceae (hóa thạch)"),
    ("083705", "rhythmics", "noun", "/ˈrɪðmɪks/", "tiết tấu học; nhịp điệu học"),
    ("083706", "rhythmings", "noun", "/ˈrɪðmɪŋz/", "sự tạo nhịp điệu"),
    ("083707", "rhythmise", "verb", "/ˈrɪðˌmaɪz/", "tạo nhịp điệu"),
    ("083708", "rhythmist", "noun", "/ˈrɪðmɪst/", "người am hiểu tiết tấu"),
    ("083709", "rhythmize", "verb", "/ˈrɪðˌmaɪz/", "tạo nhịp điệu"),
    ("083710", "rhytidectomy", "noun", "/ˌrɪtɪˈdɛktəmi/", "phẫu thuật căng da mặt"),
    ("083711", "rhytidoplasty", "noun", "/rɪˈtɪdəˌplæsti/", "phẫu thuật căng da mặt"),
    ("083712", "ria", "noun", "/ˈriːə/", "vịnh hẹp ngập triều (ria)"),
    ("083713", "rials", "noun", "/riˈɑːlz/", "đồng rial (Iran, Oman)"),
    ("083714", "rialto", "noun", "/riˈæltoʊ/", "khu chợ buôn bán; khu nhà hát"),
    ("083715", "riat", "noun", "/ˈraɪət/", "nông dân tá điền Ấn Độ"),
    ("083716", "ribboned", "adj", "/ˈrɪbənd/", "được trang trí bằng ruy băng"),
    ("083717", "ribbonfish", "noun", "/ˈrɪbənˌfɪʃ/", "cá hố; cá ruy băng"),
    ("083718", "ribbonlike", "adj", "/ˈrɪbənˌlaɪk/", "dài mảnh như dải ruy băng"),
    ("083719", "ribbonwood", "noun", "/ˈrɪbənˌwʊd/", "cây gỗ ruy băng New Zealand"),
    ("083720", "ribbony", "adj", "/ˈrɪbəni/", "như dải ruy băng"),
    ("083721", "ribgrass", "noun", "/ˈrɪbˌɡræs/", "cây mã đề lá hẹp"),
    ("083722", "ribhus", "noun", "/ˈrɪbuːz/", "các thần thợ thủ công Vệ Đà"),
    ("083723", "ribier", "noun", "/rɪˈbjɛr/", "giống nho đen Ribier"),
    ("083724", "ribless", "adj", "/ˈrɪbləs/", "không có xương sườn; không gân"),
    ("083725", "riblike", "adj", "/ˈrɪbˌlaɪk/", "giống xương sườn; dạng gân"),
    ("083726", "ribonucleases", "noun", "/ˌraɪboʊˈnjuːkliˌeɪsɪz/", "enzim ribonuclease"),
    ("083727", "ribonucleinase", "noun", "/ˌraɪboʊˈnjuːkliɪˌneɪs/", "enzim phân giải ARN"),
    ("083728", "ribs", "verb", "/rɪbz/", "trêu chọc; làm gân sườn"),
    ("083729", "ribwort", "noun", "/ˈrɪbwɜːrt/", "cây mã đề lá hẹp"),
    ("083730", "ricebird", "noun", "/ˈraɪsˌbɜːrd/", "chim sẻ đồng; chim bạc má Java"),
    ("083731", "ricefield", "noun", "/ˈraɪsˌfiːld/", "cánh đồng lúa; ruộng lúa"),
    ("083732", "ricegrass", "noun", "/ˈraɪsˌɡræs/", "cỏ gạo (họ Hòa thảo)"),
    ("083733", "richea", "noun", "/ˈrɪtʃiə/", "chi cây bụi Richea Úc"),
    ("083734", "richer", "adj", "/ˈrɪtʃər/", "giàu hơn; đậm đà hơn"),
    ("083735", "richest", "adj", "/ˈrɪtʃəst/", "giàu nhất; đậm đà nhất"),
    ("083736", "richmondena", "noun", "/ˌrɪtʃmənˈdiːnə/", "chim hồng y giáo chủ"),
    ("083737", "richter", "noun", "/ˈrɪktər/", "thang đo động đất Richter"),
    ("083738", "richweed", "noun", "/ˈrɪtʃˌwiːd/", "cây richweed (họ Tầm ma)"),
    ("083739", "ricked", "verb", "/rɪkt/", "đã đánh đống rơm; đã trật khớp"),
    ("083740", "ricker", "noun", "/ˈrɪkər/", "sào gỗ làm giàn giáo; trụ chống"),
    ("083741", "ricketiness", "noun", "/ˈrɪkɪtinəs/", "tình trạng ọp ẹp; lung lay"),
    ("083742", "rickettsiaceae", "noun", "/rɪˌkɛtsiˈeɪsiːˌiː/", "họ vi khuẩn Rickettsiaceae"),
    ("083743", "rickettsiae", "noun", "/rɪˈkɛtsiˌiː/", "vi khuẩn Rickettsia"),
    ("083744", "rickettsiales", "noun", "/rɪˌkɛtsiˈeɪliːz/", "bộ vi khuẩn Rickettsiales"),
    ("083745", "rickettsialpox", "noun", "/rɪˈkɛtsiəlˌpɑːks/", "bệnh sốt phát ban dạng đậu"),
    ("083746", "rickettsiosis", "noun", "/rɪˌkɛtsiˈoʊsɪs/", "bệnh nhiễm vi khuẩn Rickettsia"),
    ("083747", "ricking", "verb", "/ˈrɪkɪŋ/", "đang đánh đống rơm; đang trẹo khớp"),
    ("083748", "rickrack", "noun", "/ˈrɪkˌræk/", "dây viền áo răng cưa"),
    ("083749", "rickroll", "verb", "/ˈrɪkˌroʊl/", "lừa bấm vào video nhạc Rick Astley"),
    ("083750", "rickrolled", "verb", "/ˈrɪkˌroʊld/", "đã lừa bấm vào link nhạc trêu"),
    ("083751", "rickrolling", "verb", "/ˈrɪkˌroʊlɪŋ/", "đang lừa bấm vào link nhạc trêu"),
    ("083752", "rickrolls", "verb", "/ˈrɪkˌroʊlz/", "lừa bấm vào link nhạc trêu"),
    ("083753", "ricks", "verb", "/rɪks/", "đánh đống rơm; làm trẹo khớp"),
    ("083754", "ricksha", "noun", "/ˈrɪkʃɔː/", "xe kéo tay; xích lô"),
    ("083755", "ricocheted", "verb", "/ˈrɪkəˌʃeɪd/", "đã nảy bật ra (đạn, đá)"),
    ("083756", "ricocheting", "verb", "/ˈrɪkəˌʃeɪɪŋ/", "đang nảy bật ra"),
    ("083757", "ricochets", "verb", "/ˈrɪkəˌʃeɪz/", "nảy bật ra"),
    ("083758", "ricrac", "noun", "/ˈrɪkˌræk/", "dây viền răng cưa"),
    ("083759", "rictal", "adj", "/ˈrɪktəl/", "thuộc khóe miệng; há rộng miệng"),
    ("083760", "ridable", "adj", "/ˈraɪdəbəl/", "có thể cưỡi được; đi qua được"),
    ("083761", "riddel", "noun", "/ˈrɪdəl/", "màn che bên bàn thờ"),
    ("083762", "ridden", "verb", "/ˈrɪdən/", "đã cưỡi; đã đi xe"),
    ("083763", "riddles", "verb", "/ˈrɪdəlz/", "đục lỗ chỗ; giải câu đố"),
    ("083764", "riddling", "noun", "/ˈrɪdlɪŋ/", "sự sàng sảy; việc ra câu đố"),
    ("083765", "ridel", "noun", "/ˈraɪdəl/", "màn che bên bàn thờ"),
    ("083766", "riderless", "adj", "/ˈraɪdərləs/", "không có người cưỡi"),
    ("083767", "ridgel", "noun", "/ˈrɪdʒəl/", "gia súc thiến sót một tinh hoàn"),
    ("083768", "ridgeling", "noun", "/ˈrɪdʒlɪŋ/", "ngựa non chưa xuống hết tinh hoàn"),
    ("083769", "ridger", "noun", "/ˈrɪdʒər/", "máy cày lên luống; người đánh luống"),
    ("083770", "ridges", "verb", "/ˈrɪdʒɪz/", "tạo luống; nổi gờ sống"),
    ("083771", "ridgeway", "noun", "/ˈrɪdʒˌweɪ/", "đường mòn chạy dọc đỉnh đồi"),
    ("083772", "ridgil", "noun", "/ˈrɪdʒɪl/", "gia súc ẩn một bên tinh hoàn"),
    ("083773", "ridging", "verb", "/ˈrɪdʒɪŋ/", "đang lên luống; đang tạo gờ"),
    ("083774", "ridgling", "noun", "/ˈrɪdʒlɪŋ/", "ngựa non ẩn một tinh hoàn"),
    ("083775", "ridgy", "adj", "/ˈrɪdʒi/", "có nhiều gờ; nhiều sống núi"),
    ("083776", "ridiculed", "verb", "/ˈrɪdɪˌkjuːld/", "đã chế nhạo; đã nhạo báng"),
    ("083777", "ridiculer", "noun", "/ˈrɪdɪˌkjuːlər/", "người hay chế nhạo"),
    ("083778", "ridicules", "verb", "/ˈrɪdɪˌkjuːlz/", "chế nhạo; nhạo báng"),
    ("083779", "ridiculing", "verb", "/ˈrɪdɪˌkjuːlɪŋ/", "đang chế nhạo; đang nhạo báng"),
    ("083780", "ridotto", "noun", "/rɪˈdɑːtoʊ/", "buổi dạ hội ca múa đeo mặt nạ"),
    ("083781", "rifadin", "noun", "/ˈrɪfədɪn/", "thuốc kháng lao Rifadin"),
    ("083782", "rifeness", "noun", "/ˈraɪfnəs/", "tình trạng lan tràn phổ biến"),
    ("083783", "riffian", "noun", "/ˈrɪfiən/", "người Berber vùng Rif (Maroc)"),
    ("083784", "riflebird", "noun", "/ˈraɪfəlˌbɜːrd/", "chim thiên đường đen Úc"),
    ("083785", "riflegreen", "adj", "/ˈraɪfəlˌɡriːn/", "màu xanh lục sẫm"),
    ("083786", "riflemen", "noun", "/ˈraɪfəlmən/", "lính súng trường"),
    ("083787", "riflery", "noun", "/ˈraɪfəlri/", "môn bắn súng trường"),
    ("083788", "rifles", "verb", "/ˈraɪfəlz/", "lục soát; cướp sạch"),
    ("083789", "riflescope", "noun", "/ˈraɪfəlˌskoʊp/", "ống ngắm súng trường"),
    ("083790", "rifted", "verb", "/ˈrɪftɪd/", "đã nứt toác; đã rạn nứt"),
    ("083791", "rifting", "verb", "/ˈrɪftɪŋ/", "đang tách giãn; đang rạn nứt"),
    ("083792", "rifts", "verb", "/rɪfts/", "nứt ra; tách ra"),
    ("083793", "riftzone", "noun", "/ˈrɪftˌzoʊn/", "đới tách giãn kiến tạo"),
    ("083794", "rigescent", "adj", "/rɪˈdʒɛsənt/", "trở nên cứng đờ"),
    ("083795", "righlet", "noun", "/ˈrɪŋlɪt/", "lọn tóc xoăn dài"),
    ("083796", "righted", "verb", "/ˈraɪtɪd/", "đã chỉnh thẳng; đã sửa sai"),
    ("083797", "rightest", "adj", "/ˈraɪtɪst/", "đúng nhất; tận cùng bên phải"),
    ("083798", "rightfield", "noun", "/ˈraɪtˌfiːld/", "khu vực cánh phải sân bóng chày"),
    ("083799", "righting", "verb", "/ˈraɪtɪŋ/", "đang dựng thẳng lại; đang sửa sai"),
    ("083800", "rightish", "adj", "/ˈraɪtɪʃ/", "hơi ngả về cánh hữu"),
    ("083801", "rightism", "noun", "/ˈraɪtˌɪzəm/", "chủ nghĩa cánh hữu"),
    ("083802", "righto", "intj", "/ˈraɪtoʊ/", "đồng ý; rõ rồi"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r08_raw_p3.json"))
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

json.dump(out, open("scratch/b37_r08_reviewed_p3.json", "w"), ensure_ascii=False, indent=2)
print("b37_r08_p3 saved OK")
