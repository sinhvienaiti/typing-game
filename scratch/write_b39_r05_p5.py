import json

items = [
    ("092403", "tenancies", "noun", "/ˈtɛnənsiz/", "quyền thuê nhà đất (số nhiều)"),
    ("092404", "tenantable", "adj", "/ˈtɛnəntəbəl/", "có thể cho thuê ở được"),
    ("092405", "tenanting", "verb", "/ˈtɛnəntɪŋ/", "đang thuê ở; đang cư ngụ"),
    ("092406", "tenantless", "adj", "/ˈtɛnəntləs/", "bỏ trống không có người thuê"),
    ("092407", "tenantries", "noun", "/ˈtɛnəntriz/", "tá điền; nhóm người thuê (số nhiều)"),
    ("092408", "tenants", "verb", "/ˈtɛnənts/", "thuê ở; cư ngụ làm người thuê"),
    ("092409", "tendance", "noun", "/ˈtɛndəns/", "sự chăm sóc trông nom (cổ)"),
    ("092410", "tended", "verb", "/ˈtɛndɪd/", "đã chăm sóc; đã có xu hướng"),
    ("092411", "tendencies", "noun", "/ˈtɛndənsiz/", "xu hướng; khuynh hướng (số nhiều)"),
    ("092412", "tendencious", "adj", "/tɛnˈdɛnʃəs/", "thiên vị; mang ý đồ định hướng"),
    ("092413", "tendential", "adj", "/tɛnˈdɛnʃəl/", "có khuynh hướng; mang tính xu hướng"),
    ("092414", "tendentiousness", "noun", "/tɛnˈdɛnʃəsnəs/", "tính thiên lệch đầy dụng ý"),
    ("092415", "tendered", "verb", "/ˈtɛndɚd/", "đã đệ trình; đã đấu thầu"),
    ("092416", "tenderer", "noun", "/ˈtɛndɚɚ/", "nhà thầu; người nộp đơn dự thầu"),
    ("092417", "tenderfeet", "noun", "/ˈtɛndɚˌfit/", "lính mới; người mới vào nghề"),
    ("092418", "tendergreen", "noun", "/ˈtɛndɚˌɡrin/", "cải bẹ xanh Nhật; cải ngọt"),
    ("092419", "tenderheartedness", "noun", "/ˌtɛndɚˈhɑrtɪdnəs/", "lòng nhân hậu; tấm lòng trắc ẩn"),
    ("092420", "tendering", "verb", "/ˈtɛndɚɪŋ/", "đang đệ trình; đang bỏ thầu"),
    ("092421", "tenderisation", "noun", "/ˌtɛndɚaɪˈzeɪʃən/", "sự làm mềm thịt; công đoạn dần thịt"),
    ("092422", "tenderised", "adj", "/ˈtɛndɚˌaɪzd/", "đã được làm mềm (thịt)"),
    ("092423", "tenderiser", "noun", "/ˈtɛndɚˌaɪzɚ/", "chất làm mềm thịt; búa dần thịt"),
    ("092424", "tenderises", "verb", "/ˈtɛndɚˌaɪzɪz/", "làm mềm thịt; làm mềm lòng"),
    ("092425", "tenderising", "verb", "/ˈtɛndɚˌaɪzɪŋ/", "đang làm mềm thịt; đang làm dịu"),
    ("092426", "tenderization", "noun", "/ˌtɛndɚəˈzeɪʃən/", "sự làm mềm thịt; công đoạn dần thịt"),
    ("092427", "tenderizes", "verb", "/ˈtɛndɚˌaɪzɪz/", "làm mềm thịt; dần thịt cho mềm"),
    ("092428", "tenderizing", "verb", "/ˈtɛndɚˌaɪzɪŋ/", "đang làm mềm thịt; đang dần thịt"),
    ("092429", "tenders", "verb", "/ˈtɛndɚz/", "đệ trình; đấu thầu; trao tặng"),
    ("092430", "tendosynovitis", "noun", "/ˌtɛndoʊˌsaɪnəˈvaɪtɪs/", "viêm bao hoạt dịch gân"),
    ("092431", "tendrac", "noun", "/ˈtɛndræk/", "thú nhỏ tenrec Madagascar"),
    ("092432", "tendresse", "noun", "/tɑnˈdrɛs/", "tình cảm dịu dàng êm ái"),
    ("092433", "tends", "verb", "/ˈtɛndz/", "có xu hướng; chăm sóc trông nom"),
    ("092434", "tenebrific", "adj", "/ˌtɛnəˈbrɪfɪk/", "gây u tối ảm đạm"),
    ("092435", "tenebrionid", "noun", "/ˌtɛnəˈbriənɪd/", "bọ cánh cứng đen họ Tenebrionidae"),
    ("092436", "tenebrious", "adj", "/təˈnibriəs/", "tối tăm u ám; khó hiểu"),
    ("092437", "tenements", "noun", "/ˈtɛnəmənts/", "nhà tập thể cũ chật hẹp (số nhiều)"),
    ("092438", "tenets", "noun", "/ˈtɛnɪts/", "nguyên lý; giáo lý nền tảng"),
    ("092439", "tennises", "noun", "/ˈtɛnɪsɪz/", "môn quần vợt (số nhiều hiếm)"),
    ("092440", "tenonitis", "noun", "/ˌtɛnəˈnaɪtɪs/", "viêm gân; viêm bao gân mắt"),
    ("092441", "tenoretic", "noun", "/ˌtɛnəˈrɛtɪk/", "thuốc trị tăng huyết áp Tenoretic"),
    ("092442", "tenorist", "noun", "/ˈtɛnɚɪst/", "ca sĩ giọng nam cao; người thổi kèn"),
    ("092443", "tenoroon", "noun", "/ˌtɛnəˈrun/", "kèn bassoon giọng nam cao"),
    ("092444", "tenotomy", "noun", "/tɛˈnɑtəmi/", "phẫu thuật cắt gân chỉnh tật"),
    ("092445", "tenpence", "noun", "/ˈtɛnpəns/", "tiền xu mười xu (Anh)"),
    ("092446", "tenpins", "noun", "/ˈtɛnˌpɪnz/", "trò chơi bowling mười ky"),
    ("092447", "tenpounder", "noun", "/ˈtɛnˌpaʊndɚ/", "cá cháo biển mười cân"),
    ("092448", "tenrec", "noun", "/ˈtɛnrɛk/", "thú nhỏ ăn sâu bọ tenrec"),
    ("092449", "tenrecidae", "noun", "/tɛnˈrɛsɪˌdi/", "họ Thú tenrec Madagascar"),
    ("092450", "tenser", "adj", "/ˈtɛnsɚ/", "căng thẳng hơn (so sánh hơn)"),
    ("092451", "tensibility", "noun", "/ˌtɛnsəˈbɪlɪti/", "tính có thể kéo căng giãn"),
    ("092452", "tensible", "adj", "/ˈtɛnsəbəl/", "có thể kéo căng giãn được"),
    ("092453", "tensility", "noun", "/tɛnˈsɪlɪti/", "tính đàn hồi kéo căng được"),
    ("092454", "tensimeter", "noun", "/tɛnˈsɪmɪtɚ/", "áp kế hơi; máy đo sức căng"),
    ("092455", "tensiometer", "noun", "/ˌtɛnsiˈɑmɪtɚ/", "máy đo sức căng; máy đo ẩm đất"),
    ("092456", "tensiometers", "noun", "/ˌtɛnsiˈɑmɪtɚz/", "máy đo sức căng (số nhiều)"),
    ("092457", "tensionless", "adj", "/ˈtɛnʃənləs/", "thư thái không căng thẳng"),
    ("092458", "tensity", "noun", "/ˈtɛnsɪti/", "trạng thái căng thẳng cao độ"),
    ("092459", "tentacles", "noun", "/ˈtɛntəkəlz/", "xúc tu; tua vòi (số nhiều)"),
    ("092460", "tentaculata", "noun", "/tɛnˌtækjəˈleɪtə/", "lớp Sứa lược có xúc tu"),
    ("092461", "tentaculate", "adj", "/tɛnˈtækjəˌleɪt/", "có xúc tu; mang tua vòi"),
    ("092462", "tentaculum", "noun", "/tɛnˈtækjələm/", "xúc tu; tua cảm giác"),
    ("092463", "tentation", "noun", "/tɛnˈteɪʃən/", "sự thử nghiệm; sự cám dỗ (cổ)"),
    ("092464", "tentations", "noun", "/tɛnˈteɪʃənz/", "sự cám dỗ; phép thử (số nhiều)"),
    ("092465", "tented", "verb", "/ˈtɛntɪd/", "đã cắm trại; đã dựng lều"),
    ("092466", "tenterhook", "noun", "/ˈtɛntɚˌhʊk/", "móc sắt khung căng vải"),
    ("092467", "tenterhooks", "noun", "/ˈtɛntɚˌhʊks/", "tâm trạng hồi hộp đứng ngồi không yên"),
    ("092468", "tenthly", "adv", "/ˈtɛnθli/", "thứ mười là"),
    ("092469", "tenthredinidae", "noun", "/ˌtɛnθrəˈdɪnɪˌdi/", "họ Ong cưa ăn lá"),
    ("092470", "tents", "verb", "/ˈtɛnts/", "cắm trại bằng lều; phủ lều bạt"),
    ("092471", "tenuity", "noun", "/tɛˈnuəti/", "độ mỏng manh; tính thưa loãng"),
    ("092472", "tenuousness", "noun", "/ˈtɛnjuəsnəs/", "sự mỏng manh; tính yếu ớt mong manh"),
    ("092473", "tepal", "noun", "/ˈtɛpəl/", "cánh bao hoa (đài cánh giống nhau)"),
    ("092474", "tepefy", "verb", "/ˈtɛpəˌfaɪ/", "hâm hơi ấm; làm âm ấm"),
    ("092475", "tephrite", "noun", "/ˈtɛfˌraɪt/", "đá núi lửa tephrit"),
    ("092476", "tepidity", "noun", "/təˈpɪdɪti/", "độ ấm nhẹ; thái độ hờ hững"),
    ("092477", "tepidness", "noun", "/ˈtɛpɪdnəs/", "sự âm ấm; sự thờ ơ lãnh đạm"),
    ("092478", "teqball", "noun", "/ˈtɛkˌbɔl/", "môn bóng bàn đá chân teqball"),
    ("092479", "terabytes", "noun", "/ˈtɛrəˌbaɪts/", "đơn vị dữ liệu terabyte (số nhiều)"),
    ("092480", "teraflop", "noun", "/ˈtɛrəˌflɑp/", "nghìn tỷ phép tính dấu phẩy mỗi giây"),
    ("092481", "teratogenesis", "noun", "/ˌtɛrətoʊˈdʒɛnəsɪs/", "sự hình thành dị tật quái thai"),
    ("092482", "tercelet", "noun", "/ˈtɜːrsəlɪt/", "chim ưng đực (tiếng cổ)"),
    ("092483", "tercentennial", "noun", "/ˌtɜːrsɛnˈtɛniəl/", "lễ kỷ niệm 300 năm"),
    ("092484", "terebella", "noun", "/ˌtɛrəˈbɛlə/", "chi giun biển nhiều tơ Terebella"),
    ("092485", "terebellidae", "noun", "/ˌtɛrəˈbɛlɪˌdi/", "họ Giun biển nhiều tơ Terebellidae"),
    ("092486", "terebenthena", "noun", "/ˌtɛrəbɛnˈθinə/", "tinh dầu thông terebene"),
    ("092487", "terebinthine", "adj", "/ˌtɛrəˈbɪnθɪn/", "thuộc nhựa thông; có mùi dầu thông"),
    ("092488", "terebra", "noun", "/tɛˈribrə/", "ống đẻ trứng (côn trùng); ốc mũi khoan"),
    ("092489", "terebrate", "verb", "/ˈtɛrəˌbreɪt/", "khoan thủng; đục lỗ xoắn ốc"),
    ("092490", "terebration", "noun", "/ˌtɛrəˈbreɪʃən/", "hành động khoan đục xoắn ốc"),
    ("092491", "teredinid", "noun", "/tɛˈrɛdənɪd/", "con hà đục gỗ tàu biển"),
    ("092492", "teredinidae", "noun", "/ˌtɛrəˈdɪnɪˌdi/", "họ Hà đục gỗ tàu biển"),
    ("092493", "terefah", "adj", "/trəˈfɑ/", "không hợp chuẩn ăn sạch Do Thái"),
    ("092494", "tergal", "adj", "/ˈtɜːrɡəl/", "thuộc mặt lưng (động vật chân khớp)"),
    ("092495", "tergiversate", "verb", "/ˈtɜːrdʒəvɚˌseɪt/", "nói nước đôi lấp lửng; trở cờ"),
    ("092496", "tergiversation", "noun", "/ˌtɜːrdʒəvɚˈseɪʃən/", "lời thoái thác lấp lửng; sự trở cờ"),
    ("092497", "tergiversator", "noun", "/ˈtɜːrdʒəvɚˌseɪtɚ/", "kẻ lấp lửng thoái thác; kẻ trở cờ"),
    ("092498", "tergum", "noun", "/ˈtɜːrɡəm/", "tấm giáp lưng (chân khớp)"),
    ("092499", "termagancy", "noun", "/ˈtɜːrməɡənsi/", "tính đanh đá chua ngoa lắm lời"),
    ("092500", "termed", "verb", "/ˈtɜːrmd/", "đã gọi tên là; đã đặt thuật ngữ là"),
    ("092501", "terminates", "verb", "/ˈtɜːrməˌneɪts/", "chấm dứt; kết thúc; hủy bỏ"),
    ("092502", "terminating", "verb", "/ˈtɜːrməˌneɪtɪŋ/", "đang chấm dứt; đang kết thúc"),
]

# Trim <=35:
# 092418 "cải bẹ xanh Nhật; cải ngọt" = 27
# 092421/26 "sự làm mềm thịt; công đoạn dần thịt" = 37 -> "sự làm mềm thịt; cách dần thịt" = 32
items[18] = ("092421", "tenderisation", "noun", "/ˌtɛndɚaɪˈzeɪʃən/", "sự làm mềm thịt; cách dần thịt")
items[23] = ("092426", "tenderization", "noun", "/ˌtɛndɚəˈzeɪʃən/", "sự làm mềm thịt; cách dần thịt")
# 092435 "bọ cánh cứng đen họ Tenebrionidae" = 35 -> OK! Wait: let's count: 2+1+4+1+4+1+3+1+2+1+13 = 33
# 092437 "nhà tập thể cũ chật hẹp (số nhiều)" = 35
# 092439 "môn quần vợt (số nhiều hiếm)" = 29
# 092440 "viêm gân; viêm bao gân mắt" = 27
# 092442 "ca sĩ giọng nam cao; người thổi kèn" = 36 -> "ca sĩ giọng nam cao" = 19
items[39] = ("092442", "tenorist", "noun", "/ˈtɛnɚɪst/", "ca sĩ giọng nam cao; người thổi")
# Or better: "ca sĩ nam cao; người thổi sax tenor" (37) -> "ca sĩ nam cao; nghệ sĩ tenor" = 30!
items[39] = ("092442", "tenorist", "noun", "/ˈtɛnɚɪst/", "ca sĩ giọng nam cao; nghệ sĩ sax")
# 092467 "tâm trạng hồi hộp đứng ngồi không yên" = 37 -> "trạng thái đứng ngồi không yên" = 31
items[64] = ("092467", "tenterhooks", "noun", "/ˈtɛntɚˌhʊks/", "trạng thái đứng ngồi không yên")
# 092472 "sự mỏng manh; tính yếu ớt mong manh" = 36 -> "sự mỏng manh; tính yếu ớt" = 25
items[69] = ("092472", "tenuousness", "noun", "/ˈtɛnjuəsnəs/", "sự mỏng manh; tính yếu ớt")
# 092479 "đơn vị dữ liệu terabyte (số nhiều)" = 36 -> "terabyte (số nhiều)" = 19
items[76] = ("092479", "terabytes", "noun", "/ˈtɛrəˌbaɪts/", "terabyte (số nhiều)")
# 092480 "nghìn tỷ phép tính dấu phẩy mỗi giây" = 38 -> "nghìn tỷ phép tính mỗi giây" = 28
items[77] = ("092480", "teraflop", "noun", "/ˈtɛrəˌflɑp/", "nghìn tỷ phép tính mỗi giây")
# 092485 "họ Giun biển nhiều tơ Terebellidae" = 35
# 092487 "thuộc nhựa thông; có mùi dầu thông" = 36 -> "thuộc nhựa thông; mùi dầu thông" = 32
items[84] = ("092487", "terebinthine", "adj", "/ˌtɛrəˈbɪnθɪn/", "thuộc nhựa thông; mùi dầu thông")
# 092488 "ống đẻ trứng (côn trùng); ốc mũi khoan" = 39 -> "ống đẻ trứng côn trùng; ốc khoan" = 33
items[85] = ("092488", "terebra", "noun", "/tɛˈribrə/", "ống đẻ trứng côn trùng; ốc khoan")
# 092494 "thuộc mặt lưng (động vật chân khớp)" = 37 -> "thuộc mặt lưng (chân khớp)" = 27
items[91] = ("092494", "tergal", "adj", "/ˈtɜːrɡəl/", "thuộc mặt lưng (chân khớp)")
# 092496 "lời thoái thác lấp lửng; sự trở cờ" = 36 -> "sự thoái thác lấp lửng; sự trở cờ" = 35
items[93] = ("092496", "tergiversation", "noun", "/ˌtɜːrdʒəvɚˈseɪʃən/", "sự thoái thác lấp lửng; trở cờ")
# 092500 "đã gọi tên là; đã đặt thuật ngữ là" = 36 -> "đã gọi tên là; đã đặt tên là" = 29
items[97] = ("092500", "termed", "verb", "/ˈtɜːrmd/", "đã gọi tên là; đã đặt tên là")

with open("scratch/b39_r05_p5.json", "w") as f:
    json.dump(items, f, ensure_ascii=False, indent=2)
print("Wrote p5:", len(items))
