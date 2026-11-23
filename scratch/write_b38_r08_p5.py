import json

RECORDS = [
    ("088903", "spooled", "verb", "/spuːld/", "đã cuộn vào ống chỉ; đã đệm in"),
    ("088904", "spooler", "noun", "/ˈspuːlər/", "bộ đệm điều phối hàng đợi in ấn"),
    ("088905", "spooling", "verb", "/ˈspuːlɪŋ/", "đang cuộn ống chỉ; đang xếp hàng in"[:35]),
    ("088906", "spools", "verb", "/spuːlz/", "cuộn vào ống; xếp hàng đợi xử lý"),
    ("088907", "spoonbeak", "noun", "/ˈspuːnˌbiːk/", "chim cò mỏ thìa"),
    ("088908", "spoondrift", "noun", "/ˈspuːnˌdrɪft/", "bụi nước biển cuốn bay khi bão lớn"),
    ("088909", "spooned", "verb", "/spuːnd/", "đã múc bằng thìa; đã ôm ấp áp lưng"[:35]),
    ("088910", "spooner", "noun", "/ˈspuːnər/", "người hay nói nhầm lẫn âm đầu"),
    ("088911", "spooney", "adj", "/ˈspuːni/", "si tình ngớ ngẩn; yếu đuối sến sẩm"),
    ("088912", "spoonfeed", "verb", "/ˈspuːnˌfiːd/", "đút từng thìa; nhồi nhét sẵn hết"),
    ("088913", "spoonfeeding", "noun", "/ˈspuːnˌfiːdɪŋ/", "cách dạy nhồi nhét làm sẵn hết"),
    ("088914", "spoonily", "adv", "/ˈspuːnɪli/", "một cách si tình ngớ ngẩn"),
    ("088915", "spooniness", "noun", "/ˈspuːninəs/", "sự si tình ngốc nghếch sến sẩm"),
    ("088916", "spooning", "verb", "/ˈspuːnɪŋ/", "đang múc thìa; đang ôm áp lưng nhau"[:35]),
    ("088917", "spoons", "verb", "/spuːnz/", "múc bằng thìa; ôm ấp áp lưng nhau"),
    ("088918", "spoony", "adj", "/ˈspuːni/", "si tình ngốc nghếch; khờ dại"),
    ("088919", "spoored", "verb", "/spʊrd/", "đã lần theo dấu vết chân thú rừng"),
    ("088920", "spooring", "verb", "/ˈspʊrɪŋ/", "đang lần theo dấu vết chân thú"),
    ("088921", "spoors", "verb", "/spʊrz/", "lần theo dấu chân thú rừng"),
    ("088922", "sporadical", "adj", "/spəˈrædɪkəl/", "lác đác rời rạc; thỉnh thoảng xảy"[:35]),
    ("088923", "sporadicalness", "noun", "/spəˈrædɪkəlnəs/", "tính chất lác đác thưa thớt rời rạc"[:35]),
    ("088924", "sporangia", "noun", "/spəˈrændʒiə/", "túi bào tử (thực vật bậc thấp)"),
    ("088925", "sporangial", "adj", "/spəˈrændʒiəl/", "thuộc túi bào tử"),
    ("088926", "sporangiophore", "noun", "/spəˈrændʒiəˌfɔːr/", "cuống mang túi bào tử"),
    ("088927", "sporeling", "noun", "/ˈspɔːrlɪŋ/", "cây non mọc lên từ bào tử"),
    ("088928", "sporicide", "noun", "/ˈspɔːrəˌsaɪd/", "chất hóa học diệt bào tử vi khuẩn"),
    ("088929", "sporiferous", "adj", "/spɔːˈrɪfərəs/", "mang bào tử; sinh sản bào tử"),
    ("088930", "sporification", "noun", "/ˌspɔːrɪfɪˈkeɪʃən/", "quá trình hình thành bào tử"),
    ("088931", "sporocarp", "noun", "/ˈspɔːrəˌkɑːrp/", "quả bào tử; thể quả nấm"),
    ("088932", "sporogenesis", "noun", "/ˌspɔːroʊˈdʒɛnəsɪs/", "quá trình phát sinh bào tử"),
    ("088933", "sporogenous", "adj", "/spɔːˈrɑːdʒənəs/", "sinh ra bào tử; tạo bào tử"),
    ("088934", "sporophore", "noun", "/ˈspɔːrəˌfɔːr/", "thể mang bào tử (nấm)"),
    ("088935", "sporophyl", "noun", "/ˈspɔːrəˌfɪl/", "lá mang túi bào tử"),
    ("088936", "sporophyll", "noun", "/ˈspɔːrəˌfɪl/", "lá bào tử (mang túi bào tử)"),
    ("088937", "sporozoa", "noun", "/ˌspɔːrəˈzoʊə/", "nhóm Trùng bào tử ký sinh"),
    ("088938", "sporozoan", "noun", "/ˌspɔːrəˈzoʊən/", "sinh vật trùng bào tử ký sinh"),
    ("088939", "sporozoite", "noun", "/ˌspɔːrəˈzoʊˌaɪt/", "thể thoa trùng (ký sinh trùng sốt)"),
    ("088940", "sportful", "adj", "/ˈspɔːrtfəl/", "vui nhộn; tinh nghịch hay đùa"),
    ("088941", "sportily", "adv", "/ˈspɔːrtɪli/", "khỏe khoắn thể thao; bảnh bao"),
    ("088942", "sportiness", "noun", "/ˈspɔːrtinəs/", "vẻ năng động thể thao; hào phóng"),
    ("088943", "sportively", "adv", "/ˈspɔːrtɪvli/", "vui đùa tinh nghịch"),
    ("088944", "sportiveness", "noun", "/ˈspɔːrtɪvnəs/", "tính vui đùa tinh nghịch"),
    ("088945", "sports", "noun", "/spɔːrts/", "môn thể thao; người chơi đẹp"),
    ("088946", "sporule", "noun", "/ˈspɔːrjuːl/", "bào tử nhỏ"),
    ("088947", "spotcast", "noun", "/ˈspɑːtˌkæst/", "bản tin phát thanh truyền hình nhanh"[:35]),
    ("088948", "spotcaster", "noun", "/ˈspɑːtˌkæstər/", "phát thanh viên đưa tin tại hiện场"[:35]),
    ("088949", "spotlessness", "noun", "/ˈspɑːtləsnəs/", "sự sạch sẽ tinh tươm không tì vết"),
    ("088950", "spotlighting", "noun", "/ˈspɑːtˌlaɪtɪŋ/", "việc rọi đèn pha làm nổi bật"),
    ("088951", "spottily", "adv", "/ˈspɑːtɪli/", "chỗ có chỗ không; không đồng đều"),
    ("088952", "spottiness", "noun", "/ˈspɑːtinəs/", "tình trạng lốm đốm; thiếu đều đặn"),
    ("088953", "spotweld", "verb", "/ˈspɑːtˌwɛld/", "hàn điểm điện trở"),
    ("088954", "spousals", "noun", "/ˈspaʊzəlz/", "hôn lễ; lễ đính hôn cưới hỏi"),
    ("088955", "spouted", "verb", "/ˈspaʊtɪd/", "đã phun vọt thành tia; nói tràng"),
    ("088956", "spouter", "noun", "/ˈspaʊtər/", "cá voi phun nước; kẻ ba hoa dài"),
    ("088957", "spoutless", "adj", "/ˈspaʊtləs/", "không có vòi rót"),
    ("088958", "spouts", "verb", "/spaʊts/", "phun trào thành vòi; nói liên hồi"),
    ("088959", "sprachbund", "noun", "/ˈʃprɑːxˌbʊnt/", "liên minh ngôn ngữ vùng địa lý"),
    ("088960", "sprachbunds", "noun", "/ˈʃprɑːxˌbʊndz/", "liên minh ngôn ngữ vùng địa lý"),
    ("088961", "sprachgefuhl", "noun", "/ˈʃprɑːxɡəˌfuːl/", "cảm thức ngôn ngữ tự nhiên"),
    ("088962", "spraddle", "verb", "/ˈsprædəl/", "dang rộng hai chân; bò lê lết"),
    ("088963", "spraguea", "noun", "/ˈspreɪɡiə/", "chi hoa chân mèo núi Spraguea"),
    ("088964", "sprained", "verb", "/spreɪnd/", "đã làm bong gân; bị bong gân"),
    ("088965", "spraining", "verb", "/ˈspreɪnɪŋ/", "đang làm bong gân"),
    ("088966", "sprains", "verb", "/spreɪnz/", "làm bong gân; bị trẹo khớp gân"),
    ("088967", "sprainting", "noun", "/ˈspreɪntɪŋ/", "dấu phân rái cá; việc thải phân"),
    ("088968", "spraints", "noun", "/spreɪnts/", "phân rái cá"),
    ("088969", "sprang", "verb", "/spræŋ/", "đã nhảy bật lên; đã bất ngờ xuất"),
    ("088970", "spratter", "noun", "/ˈsprætər/", "ngư dân đánh bắt cá trích nhỏ"),
    ("088971", "sprawled", "verb", "/sprɔːld/", "đã nằm dang tay chân; lan tràn"),
    ("088972", "sprawler", "noun", "/ˈsprɔːlər/", "người nằm xoạc chân; cây mọc lan"),
    ("088973", "sprawls", "verb", "/sprɔːlz/", "nằm xoạc tay chân; lan rộng bừa"),
    ("088974", "sprawly", "adj", "/ˈsprɔːli/", "bừa bộn lan man; mọc bò lan rộng"),
    ("088975", "sprayboard", "noun", "/ˈspreɪˌbɔːrd/", "tấm chắn bọt sóng mũi xuồng"),
    ("088976", "sprayey", "adj", "/ˈspreɪi/", "có nhiều cành lá nhỏ xòe; bụi sương"[:35]),
    ("088977", "spreadeagle", "verb", "/ˌsprɛdˈiːɡəl/", "trói giang tay chân; thắng áp đảo"),
    ("088978", "spreaders", "noun", "/ˈsprɛdərz/", "máy rải phân; dao phết bơ"),
    ("088979", "spreadhead", "noun", "/ˈsprɛdˌhɛd/", "tiêu đề lớn chạy ngang nhiều cột"),
    ("088980", "sprechgesang", "noun", "/ˈʃprɛçɡəˌzɑːŋ/", "kỹ thuật hát nói biểu cảm Đức"),
    ("088981", "sprechstimme", "noun", "/ˈʃprɛçˌʃtɪmə/", "lối hát nói biểu cảm (nhạc kịch)"),
    ("088982", "spreed", "verb", "/spriːd/", "đã ăn chơi chè chén thả ga"),
    ("088983", "spreeing", "verb", "/ˈspriːɪŋ/", "đang ăn chơi vung tiền thả ga"),
    ("088984", "sprees", "verb", "/spriːz/", "ăn chơi tiêu xài thả ga"),
    ("088985", "sprigged", "adj", "/sprɪɡd/", "in thêu hoa văn cành lá nhỏ"),
    ("088986", "sprigger", "noun", "/ˈsprɪɡər/", "người thêu cành hoa nhỏ; thợ đóng"),
    ("088987", "spriggy", "adj", "/ˈsprɪɡi/", "nhiều cành nhánh con; trang trí hoa"[:35]),
    ("088988", "spright", "noun", "/spraɪt/", "tiên nhỏ; yêu tinh; tinh linh"),
    ("088989", "sprightful", "adj", "/ˈspraɪtfəl/", "tinh nghịch hoạt bát; vui vẻ"),
    ("088990", "sprigtail", "noun", "/ˈsprɪɡˌteɪl/", "chim gà gô đuôi nhọn; vịt đuôi kim"),
    ("088991", "springal", "noun", "/ˈsprɪŋəl/", "gã thanh niên trẻ (văn cổ)"),
    ("088992", "springald", "noun", "/ˈsprɪŋəld/", "chàng trai trẻ; máy bắn đá cổ"),
    ("088993", "springbuck", "noun", "/ˈsprɪŋˌbʌk/", "linh dương nhảy Nam Phi"),
    ("088994", "springe", "noun", "/sprɪndʒ/", "bẫy thòng lọng bật bắt chim thú"),
    ("088995", "springers", "noun", "/ˈsprɪŋərz/", "chó săn Springer; đá chân vòm"),
    ("088996", "springhead", "noun", "/ˈsprɪŋˌhɛd/", "nguồn suối đầu; cội nguồn gốc rễ"),
    ("088997", "springheels", "noun", "/ˈsprɪŋˌhiːlz/", "giày gót lò xo bật nhảy"),
    ("088998", "springily", "adv", "/ˈsprɪŋɪli/", "nhún nhảy đàn hồi nhẹ nhàng"),
    ("088999", "springing", "noun", "/ˈsprɪŋɪŋ/", "điểm chân vòm; độ nảy đàn hồi"),
    ("089000", "springless", "adj", "/ˈsprɪŋləs/", "không có lò xo; thiếu mùa xuân"),
    ("089001", "springlet", "noun", "/ˈsprɪŋlət/", "dòng suối nhỏ"),
    ("089002", "springline", "noun", "/ˈsprɪŋˌlaɪn/", "đường chân vòm (kiến trúc)"),
]

# Cleanly replace slices and fix 088948 typo (no CJK `场`!) and 088969 truncated phrase
RECORDS[2] = ("088905", "spooling", "verb", "/ˈspuːlɪŋ/", "đang cuộn ống; đang đệm hàng in")
RECORDS[6] = ("088909", "spooned", "verb", "/spuːnd/", "đã múc bằng thìa; đã ôm áp lưng")
RECORDS[13] = ("088916", "spooning", "verb", "/ˈspuːnɪŋ/", "đang múc thìa; đang ôm áp lưng")
RECORDS[19] = ("088922", "sporadical", "adj", "/spəˈrædɪkəl/", "lác đác rời rạc; thỉnh thoảng")
RECORDS[20] = ("088923", "sporadicalness", "noun", "/spəˈrædɪkəlnəs/", "tính lác đác thưa thớt rời rạc")
RECORDS[44] = ("088947", "spotcast", "noun", "/ˈspɑːtˌkæst/", "bản tin phát thanh trực tiếp ngắn")
RECORDS[45] = ("088948", "spotcaster", "noun", "/ˈspɑːtˌkæstər/", "phóng viên phát thanh tại chỗ")
RECORDS[66] = ("088969", "sprang", "verb", "/spræŋ/", "đã nhảy bật lên; đã nảy sinh")
RECORDS[73] = ("088976", "sprayey", "adj", "/ˈspreɪi/", "có nhiều cành nhánh nhỏ; sương bụi"[:35])
RECORDS[73] = ("088976", "sprayey", "adj", "/ˈspreɪi/", "nhiều cành nhánh nhỏ; bụi sương")
RECORDS[84] = ("088987", "spriggy", "adj", "/ˈsprɪɡi/", "có nhiều cành nhánh con")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r08_raw_p5.json"))
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

json.dump(out, open("scratch/b38_r08_reviewed_p5.json", "w"), ensure_ascii=False, indent=2)
print("b38_r08_p5 saved OK")
