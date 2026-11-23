import json

RECORDS = [
    ("086303", "serpopard", "noun", "/ˈsɜːrpəˌpɑːrd/", "linh thú đầu rắn mình báo cổ đại"),
    ("086304", "serpopards", "noun", "/ˈsɜːrpəˌpɑːrdz/", "linh thú đầu rắn mình báo cổ đại"),
    ("086305", "serranid", "noun", "/ˈsɛrənɪd/", "cá mú; cá song"),
    ("086306", "serranidae", "noun", "/səˈrænɪˌdiː/", "họ Cá mú (Serranidae)"),
    ("086307", "serrasalmus", "noun", "/ˌsɛrəˈsælməs/", "chi cá piranha răng cưa"),
    ("086308", "serratiform", "adj", "/səˈrætɪˌfɔːrm/", "có hình dạng răng cưa"),
    ("086309", "serratula", "noun", "/səˈrætʃələ/", "chi cây cúc lá răng cưa"),
    ("086310", "serratulate", "adj", "/səˈrætʃəˌleɪt/", "có mép răng cưa nhỏ mịn"),
    ("086311", "serratulation", "noun", "/səˌrætʃəˈleɪʃən/", "hàng răng cưa nhỏ li ti"),
    ("086312", "serrefile", "noun", "/ˈsɛrˌfaɪl/", "sĩ quan đi khóa hậu hàng quân"),
    ("086313", "serrekunda", "noun", "/ˌsɛrəˈkʊndə/", "thành phố Serrekunda (Gambia)"),
    ("086314", "serricorn", "adj", "/ˈsɛrɪˌkɔːrn/", "có râu hình răng cưa (bọ cánh cứng)"[:35]),
    ("086315", "serriostrade", "adj", "/ˌsɛrioʊˈrɑːstreɪt/", "có mỏ khía răng cưa"),
    ("086316", "serrula", "noun", "/ˈsɛrjələ/", "cơ quan khía răng cưa nhỏ"),
    ("086317", "serrulate", "adj", "/ˈsɛrjəˌleɪt/", "có mép răng cưa nhỏ"),
    ("086318", "serrulated", "adj", "/ˈsɛrjəˌleɪtɪd/", "có mép khía răng cưa nhỏ"),
    ("086319", "serrulation", "noun", "/ˌsɛrjəˈleɪʃən/", "đường viền khía răng cưa mịn"),
    ("086320", "sertularia", "noun", "/ˌsɜːrtʃəˈlɛriə/", "chi thủy tức lông chim Sertularia"),
    ("086321", "sertularian", "noun", "/ˌsɜːrtʃəˈlɛriən/", "thủy tức lông chim biển"),
    ("086322", "serums", "noun", "/ˈsɪrəmz/", "huyết thanh"),
    ("086323", "served", "verb", "/sɜːrvd/", "đã phục vụ; đã giao bóng"),
    ("086324", "serveries", "noun", "/ˈsɜːrvəriz/", "quầy soạn đồ ăn; phòng chia món"),
    ("086325", "servery", "noun", "/ˈsɜːrvəri/", "quầy soạn đồ ăn; phòng chia món"),
    ("086326", "serves", "verb", "/sɜːrvz/", "phục vụ; dọn món; giao bóng"),
    ("086327", "serviceableness", "noun", "/ˈsɜːrvɪsəbəlnəs/", "tính hữu dụng; sự bền tiện lợi"),
    ("086328", "serviced", "verb", "/ˈsɜːrvɪst/", "đã bảo dưỡng; đã phục vụ"),
    ("086329", "servicewoman", "noun", "/ˈsɜːrvɪsˌwʊmən/", "nữ quân nhân"),
    ("086330", "serviettes", "noun", "/ˌsɜːrviˈɛts/", "khăn ăn bàn tiệc"),
    ("086331", "serviles", "noun", "/ˈsɜːrvaɪlz/", "chữ phụ đọc kéo dài (ngữ âm Semit)"[:35]),
    ("086332", "servoamplifier", "noun", "/ˌsɜːrvoʊˈæmpləˌfaɪər/", "bộ khuếch đại trợ lực servo"),
    ("086333", "servobrake", "noun", "/ˈsɜːrvoʊˌbreɪk/", "phanh trợ lực servo"),
    ("086334", "servoclutch", "noun", "/ˈsɜːrvoʊˌklʌtʃ/", "ly hợp trợ lực servo"),
    ("086335", "servocoil", "noun", "/ˈsɜːrvoʊˌkɔɪl/", "cuộn dây điều khiển servo"),
    ("086336", "servocontrol", "noun", "/ˈsɜːrvoʊkənˌtroʊl/", "hệ điều khiển trợ lực servo"),
    ("086337", "servocylinder", "noun", "/ˈsɜːrvoʊˌsɪlɪndər/", "xi-lanh trợ lực servo"),
    ("086338", "servodrive", "noun", "/ˈsɜːrvoʊˌdraɪv/", "bộ truyền động servo"),
    ("086339", "servoengine", "noun", "/ˈsɜːrvoʊˌɛndʒɪn/", "động cơ trợ lực servo"),
    ("086340", "servogear", "noun", "/ˈsɜːrvoʊˌɡɪr/", "cơ cấu bánh răng trợ lực"),
    ("086341", "servomechanical", "adj", "/ˌsɜːrvoʊmɪˈkænɪkəl/", "thuộc cơ học trợ lực servo"),
    ("086342", "servomotor", "noun", "/ˈsɜːrvoʊˌmoʊtər/", "động cơ servo"),
    ("086343", "servopiston", "noun", "/ˈsɜːrvoʊˌpɪstən/", "pít-tông trợ lực servo"),
    ("086344", "servosystem", "noun", "/ˈsɜːrvoʊˌsɪstəm/", "hệ thống điều khiển servo"),
    ("086345", "servotab", "noun", "/ˈsɜːrvoʊˌtæb/", "cánh lái phụ thăng bằng máy bay"),
    ("086346", "serzone", "noun", "/ˈsɜːrˌzoʊn/", "thuốc chống trầm cảm Serzone"),
    ("086347", "sesamoidal", "adj", "/ˌsɛsəˈmɔɪdəl/", "thuộc xương vừng; dạng hạt vừng"),
    ("086348", "seseli", "noun", "/ˈsɛsəli/", "chi cây cần núi Seseli"),
    ("086349", "sesquialteral", "adj", "/ˌsɛskwiˈɔːltərəl/", "theo tỷ lệ ba trên hai; gấp rưỡi"),
    ("086350", "sesquioxide", "noun", "/ˌsɛskwiˈɑːksaɪd/", "oxit có tỷ lệ 2 nguyên tử trên 3 oxi"[:35]),
    ("086351", "sesquipedalia", "noun", "/ˌsɛskwɪpɪˈdeɪliə/", "từ ngữ dài ngoằng nhiều âm tiết"),
    ("086352", "sesquipedality", "noun", "/ˌsɛskwɪpɪˈdælɪti/", "thói dùng từ ngữ dài dòng cầu kỳ"),
    ("086353", "sesquitertial", "adj", "/ˌsɛskwɪˈtɜːrʃəl/", "theo tỷ lệ bốn trên ba"),
    ("086354", "sessional", "adj", "/ˈsɛʃənəl/", "thuộc phiên họp; theo khóa học kỳ"),
    ("086355", "sesterce", "noun", "/ˈsɛstərs/", "đồng xu bạc sestertius La Mã cổ"),
    ("086356", "sestertii", "noun", "/sɛˈstɜːrʃiˌaɪ/", "đồng xu sestertius La Mã cổ"),
    ("086357", "sestertius", "noun", "/sɛˈstɜːrʃəs/", "đồng xu sestertius La Mã cổ"),
    ("086358", "sestina", "noun", "/sɛˈstiːnə/", "thể thơ sáu khổ sáu dòng sestina"),
    ("086359", "setaceous", "adj", "/sɪˈteɪʃəs/", "có lông cứng; tua cứng như tơ lợn"[:35]),
    ("086360", "setae", "noun", "/ˈsiːtiː/", "lông cứng; tơ cứng (sinh học)"),
    ("086361", "setiferous", "adj", "/sɪˈtɪfərəs/", "mang lông cứng; có gai tơ"),
    ("086362", "setigerous", "adj", "/sɪˈtɪdʒərəs/", "có lông cứng; mọc tơ cứng"),
    ("086363", "setline", "noun", "/ˈsɛtˌlaɪn/", "dây câu giăng nhiều lưỡi cố định"),
    ("086364", "setophaga", "noun", "/sɪˈtɑːfəɡə/", "chi chim chích rừng Mỹ Setophaga"),
    ("086365", "sets", "noun", "/sɛts/", "bộ đồ vật; tập hợp; bối cảnh quay"),
    ("086366", "setterwort", "noun", "/ˈsɛtərˌwɜːrt/", "cây cỏ chân chim trị bệnh gia súc"[:35]),
    ("086367", "settles", "verb", "/ˈsɛtəlz/", "định cư; lắng đọng; giải quyết êm"),
    ("086368", "settlings", "noun", "/ˈsɛtlɪŋz/", "chất cặn lắng dưới đáy"),
    ("086369", "setula", "noun", "/ˈsɛtʃələ/", "lông cứng nhỏ; tơ mịn"),
    ("086370", "setuliform", "adj", "/sɪˈtʃʊlɪˌfɔːrm/", "có dạng lông tơ nhỏ"),
    ("086371", "sevener", "noun", "/ˈsɛvənər/", "quân bài bảy; vật mang số bảy"),
    ("086372", "sevensome", "noun", "/ˈsɛvənsəm/", "nhóm bảy người"),
    ("086373", "seventhly", "adv", "/ˈsɛvənθli/", "thứ bảy là"),
    ("086374", "seventyfold", "adj", "/ˈsɛvəntiˌfoʊld/", "gấp bảy mươi lần"),
    ("086375", "severalise", "verb", "/ˈsɛvrəˌlaɪz/", "tách riêng ra từng phần; phân biệt"),
    ("086376", "severalize", "verb", "/ˈsɛvrəˌlaɪz/", "tách riêng ra từng phần; phân biệt"),
    ("086377", "severalty", "noun", "/ˈsɛvrəlti/", "quyền sở hữu riêng biệt độc lập"),
    ("086378", "severances", "noun", "/ˈsɛvərənsɪz/", "tiền trợ cấp thôi việc; sự cắt đứt"),
    ("086379", "severeness", "noun", "/sɪˈvɪrnəs/", "sự nghiêm khắc; mức độ khắc nghiệt"),
    ("086380", "severities", "noun", "/sɪˈvɛrɪtiz/", "tính khắc nghiệt; biện pháp nghiêm"),
    ("086381", "severs", "verb", "/ˈsɛvərz/", "cắt đứt; chặt lìa; đoạn tuyệt"),
    ("086382", "severse", "adj", "/sɪˈvɪr/", "nghiêm khắc; khắc nghiệt"),
    ("086383", "severy", "noun", "/ˈsɛvəri/", "ô trần vòm kiến trúc Gothic"),
    ("086384", "sewellel", "noun", "/səˈwɛləl/", "loài gặm nhấm hải ly núi Bắc Mỹ"),
    ("086385", "sews", "verb", "/soʊz/", "khâu vá; may đồ"),
    ("086386", "sexagenary", "adj", "/sɛkˈsædʒəˌnɛri/", "ở tuổi sáu mươi; hệ cơ số 60"),
    ("086387", "sexangle", "noun", "/ˈsɛksˌæŋɡəl/", "hình lục giác"),
    ("086388", "sexangular", "adj", "/sɛksˈæŋɡjələr/", "có sáu góc; hình lục giác"),
    ("086389", "sexcentenary", "adj", "/ˌsɛksˈsɛntəˌnɛri/", "kỷ niệm 600 năm"),
    ("086390", "sexdecimal", "adj", "/ˌsɛksˈdɛsɪməl/", "có mười sáu mặt (tinh thể)"),
    ("086391", "sexdigitate", "adj", "/ˌsɛksˈdɪdʒɪteɪt/", "có sáu ngón tay hoặc ngón chân"),
    ("086392", "sexennial", "adj", "/sɛkˈsɛniəl/", "sáu năm một lần; kéo dài sáu năm"),
    ("086393", "sexes", "noun", "/ˈsɛksɪz/", "giới tính nam và nữ"),
    ("086394", "sexifid", "adj", "/ˈsɛksəˌfɪd/", "chẻ thành sáu thùy (hoa)"),
    ("086395", "sexillion", "num", "/sɛkˈsɪljən/", "một nghìn tỷ tỷ (mười mũ 21)"),
    ("086396", "sexily", "adv", "/ˈsɛksɪli/", "gợi cảm; quyến rũ"),
    ("086397", "sexing", "verb", "/ˈsɛksɪŋ/", "đang phân biệt giới tính (vật nuôi)"[:35]),
    ("086398", "sexisyllable", "noun", "/ˌsɛksɪˈsɪləbəl/", "từ có sáu âm tiết"),
    ("086399", "sexivalent", "adj", "/ˌsɛksəˈveɪlənt/", "có hóa trị sáu"),
    ("086400", "sexlimited", "adj", "/ˈsɛksˌlɪmɪtɪd/", "hạn chế theo giới tính (di truyền)"),
    ("086401", "sexlinkage", "noun", "/ˈsɛksˌlɪŋkɪdʒ/", "tính liên kết giới tính"),
    ("086402", "sexlinked", "adj", "/ˈsɛksˌlɪŋkt/", "liên kết với nhiễm sắc thể giới tính"[:35]),
]

# Clean 086314, 086331, 086350, 086359, 086366, 086397, 086402 without slices <= 35
RECORDS[11] = ("086314", "serricorn", "adj", "/ˈsɛrɪˌkɔːrn/", "có râu hình răng cưa (bọ)")
RECORDS[28] = ("086331", "serviles", "noun", "/ˈsɜːrvaɪlz/", "chữ cái phụ (ngữ âm học)")
RECORDS[47] = ("086350", "sesquioxide", "noun", "/ˌsɛskwiˈɑːksaɪd/", "oxit tỷ lệ hai ba (sesquioxit)")
RECORDS[56] = ("086359", "setaceous", "adj", "/sɪˈteɪʃəs/", "có lông cứng; dạng lông tơ cứng")
RECORDS[63] = ("086366", "setterwort", "noun", "/ˈsɛtərˌwɜːrt/", "cây cỏ chân chim chữa bệnh bò")
RECORDS[94] = ("086397", "sexing", "verb", "/ˈsɛksɪŋ/", "đang phân biệt giới tính con non")
RECORDS[99] = ("086402", "sexlinked", "adj", "/ˈsɛksˌlɪŋkt/", "liên kết nhiễm sắc thể giới tính")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r03_raw_p4.json"))
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

json.dump(out, open("scratch/b38_r03_reviewed_p4.json", "w"), ensure_ascii=False, indent=2)
print("b38_r03_p4 saved OK")
