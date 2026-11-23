import json

RECORDS = [
    ("087603", "slumps", "verb", "/slʌmps/", "sụt giảm mạnh; ngã sụp xuống"),
    ("087604", "slums", "verb", "/slʌmz/", "sống ở khu ổ chuột; làm việc tồi"),
    ("087605", "slung", "noun", "/slʌŋ/", "rượu mạnh pha đường nước nóng"),
    ("087606", "slurring", "verb", "/ˈslɜːrɪŋ/", "đang nói líu nhíu; đang bôi nhọ"),
    ("087607", "slurs", "verb", "/slɜːrz/", "nói líu nhíu; bôi nhọ danh dự"),
    ("087608", "slusher", "noun", "/ˈslʌʃər/", "gầu cạp xúc quặng đá hầm lò"),
    ("087609", "slushing", "noun", "/ˈslʌʃɪŋ/", "việc bơm chèn vữa xi măng lỏng"),
    ("087610", "sluttery", "noun", "/ˈslʌtəri/", "sự cẩu thả bẩn thỉu; lối sống buông"),
    ("087611", "sluttishly", "adv", "/ˈslʌtɪʃli/", "luộm thuộm nhếch nhác; lẳng lơ"),
    ("087612", "sluttishness", "noun", "/ˈslʌtɪʃnəs/", "tính luộm thuộm lôi thôi; lẳng lơ"),
    ("087613", "slutty", "adj", "/ˈslʌti/", "lẳng lơ phóng túng; cẩu thả"),
    ("087614", "slyboots", "noun", "/ˈslaɪˌbuːts/", "kẻ ranh mãnh kín đáo"),
    ("087615", "slype", "noun", "/slaɪp/", "hành lang có mái vòm nhà thờ cổ"),
    ("087616", "smacked", "verb", "/smækt/", "đã tát; đã vỗ mạnh; có thoang thoảng"),
    ("087617", "smacks", "verb", "/smæks/", "tát; vỗ cái bốp; phảng phất vị"),
    ("087618", "smacksman", "noun", "/ˈsmæksmən/", "thủy thủ trên thuyền buồm đánh cá"),
    ("087619", "smallage", "noun", "/ˈsmɔːlɪdʒ/", "cây cần tây dại"),
    ("087620", "smallest", "adj", "/ˈsmɔːlɪst/", "nhỏ nhất; bé nhất"),
    ("087621", "smallfolk", "noun", "/ˈsmɔːlˌfoʊk/", "người bình dân; các tiên nhỏ bé"),
    ("087622", "smalt", "noun", "/smɔːlt/", "bột thủy tinh xanh coban làm màu"),
    ("087623", "smaltite", "noun", "/ˈsmɔːlˌtaɪt/", "quặng coban smaltit"),
    ("087624", "smalto", "noun", "/ˈsmɑːltoʊ/", "viên thủy tinh màu ghép khảm tranh"),
    ("087625", "smaragd", "noun", "/ˈsmærəɡd/", "ngọc lục bảo"),
    ("087626", "smaragdite", "noun", "/sməˈræɡˌdaɪt/", "khoáng vật amphibol xanh smaragdit"),
    ("087627", "smarmily", "adv", "/ˈsmɑːrmɪli/", "nịnh bợ trơn tru giả tạo"),
    ("087628", "smarminess", "noun", "/ˈsmɑːrminəs/", "thái độ nịnh bợ ngọt xớt giả tạo"),
    ("087629", "smarted", "verb", "/ˈsmɑːrtɪd/", "đã đau nhói rát; đã chịu hậu quả"),
    ("087630", "smarten", "verb", "/ˈsmɑːrtən/", "chỉnh trang cho gọn gàng bảnh bao"),
    ("087631", "smartened", "verb", "/ˈsmɑːrtənd/", "đã chỉnh trang bảnh bao gọn gàng"),
    ("087632", "smartening", "verb", "/ˈsmɑːrtənɪŋ/", "đang chỉnh trang cho bảnh bao"),
    ("087633", "smartens", "verb", "/ˈsmɑːrtənz/", "chỉnh trang cho bảnh bao gọn gàng"),
    ("087634", "smartish", "adj", "/ˈsmɑːrtɪʃ/", "khá nhanh nhẹn; hơi rát; bảnh bao"),
    ("087635", "smartphone", "noun", "/ˈsmɑːrtˌfoʊn/", "điện thoại thông minh"),
    ("087636", "smarts", "verb", "/smɑːrts/", "đau rát nhói; chịu tổn thất đau đớn"),
    ("087637", "smashes", "verb", "/ˈsmæʃɪz/", "đập tan tành; đánh bại áp đảo"),
    ("087638", "smatterer", "noun", "/ˈsmætərər/", "người hiểu biết hời hợt nông cạn"),
    ("087639", "smatteringly", "adv", "/ˈsmætərɪŋli/", "một cách hời hợt nông cạn"),
    ("087640", "smaze", "noun", "/smeɪz/", "khói mù lẫn sương hóa học"),
    ("087641", "smeared", "verb", "/smɪrd/", "đã trét nhòe; đã bôi nhọ danh dự"),
    ("087642", "smeariness", "noun", "/ˈsmɪrinəs/", "tính nhờn nhòe lem luốc"),
    ("087643", "smearing", "verb", "/ˈsmɪrɪŋ/", "đang trét nhòe; đang bôi nhọ"),
    ("087644", "smears", "verb", "/smɪrz/", "trét nhòe; bôi nhọ danh dự"),
    ("087645", "smeary", "adj", "/ˈsmɪri/", "lem luốc nhòe nhoẹt; nhờn bẩn"),
    ("087646", "smectite", "noun", "/ˈsmɛktaɪt/", "nhóm khoáng sét trương nở smectit"),
    ("087647", "smeech", "noun", "/smiːtʃ/", "khói khét; mùi cháy khét"),
    ("087648", "smegmatic", "adj", "/smɛɡˈmætɪk/", "thuộc bựa sinh dục"),
    ("087649", "smelled", "verb", "/smɛld/", "đã ngửi thấy; đã bốc mùi"),
    ("087650", "smeller", "noun", "/ˈsmɛlər/", "người đánh hơi; cái mũi (từ lóng)"),
    ("087651", "smellless", "adj", "/ˈsmɛlləs/", "không mùi; vô mùi"),
    ("087652", "smells", "verb", "/smɛlz/", "ngửi; có mùi; nghi ngờ có mờ ám"),
    ("087653", "smidgin", "noun", "/ˈsmɪdʒɪn/", "một chút xíu; một nhúm nhỏ"),
    ("087654", "smilacaceae", "noun", "/ˌsmaɪləˈkeɪsiːˌiː/", "họ Khúc khắc; họ Kim cang"),
    ("087655", "smiled", "verb", "/smaɪld/", "đã mỉm cười"),
    ("087656", "smiledon", "noun", "/ˈsmaɪləˌdɑːn/", "hổ răng kiếm tiền sử Smilodon"),
    ("087657", "smileless", "adj", "/ˈsmaɪlləs/", "không nở nụ cười; lạnh lùng nghiêm"),
    ("087658", "smiles", "verb", "/smaɪlz/", "mỉm cười"),
    ("087659", "smilo", "noun", "/ˈsmaɪloʊ/", "cỏ gạo núi Oloptum miliaceum"),
    ("087660", "smirched", "verb", "/smɜːrtʃt/", "đã vấy bẩn; đã bôi nhọ thanh danh"),
    ("087661", "smirches", "verb", "/ˈsmɜːrtʃɪz/", "vấy bẩn; bôi nhọ thanh danh"),
    ("087662", "smirching", "verb", "/ˈsmɜːrtʃɪŋ/", "đang vấy bẩn; đang bôi nhọ"),
    ("087663", "smirked", "verb", "/smɜːrkt/", "đã cười khẩy tự mãn; cười nhếch mép"),
    ("087664", "smirker", "noun", "/ˈsmɜːrkər/", "người hay cười khẩy tự mãn"),
    ("087665", "smirking", "verb", "/ˈsmɜːrkɪŋ/", "đang cười khẩy; cười nhếch mép"),
    ("087666", "smirkingly", "adv", "/ˈsmɜːrkɪŋli/", "với điệu cười khẩy tự mãn"),
    ("087667", "smirks", "verb", "/smɜːrks/", "cười khẩy; cười nhếch mép tự mãn"),
    ("087668", "smitane", "noun", "/smiˈtæn/", "nước xốt kem chua hành kiểu Pháp"),
    ("087669", "smiter", "noun", "/ˈsmaɪtər/", "người giáng đòn trừng phạt"),
    ("087670", "smithers", "noun", "/ˈsmɪðərz/", "mảnh vỡ vụn; từng mảnh nhỏ"),
    ("087671", "smithery", "noun", "/ˈsmɪθəri/", "lò rèn; nghề thợ rèn"),
    ("087672", "smithfield", "noun", "/ˈsmɪθˌfiːld/", "chợ đầu mối thịt Smithfield (Anh)"),
    ("087673", "smithsonite", "noun", "/ˈsmɪθsəˌnaɪt/", "quặng kẽm cacbonat smithsonit"),
    ("087674", "smocked", "verb", "/smɑːkt/", "đã may chun tổ ong trên ngực áo"),
    ("087675", "smocks", "verb", "/smɑːks/", "may xếp nếp tổ ong trang trí"),
    ("087676", "smogginess", "noun", "/ˈsmɑːɡinəs/", "tình trạng đầy khói mù ô nhiễm"),
    ("087677", "smokable", "adj", "/ˈsmoʊkəbəl/", "có thể hút được (thuốc lá)"),
    ("087678", "smokelessness", "noun", "/ˈsmoʊkləsnəs/", "trạng thái không khói"),
    ("087679", "smokes", "verb", "/smoʊks/", "hút thuốc; bốc khói; hun khói"),
    ("087680", "smokey", "adj", "/ˈsmoʊki/", "đầy khói; có mùi vị khói; xám khói"),
    ("087681", "smokily", "adv", "/ˈsmoʊkɪli/", "mờ mịt khói; thoảng mùi khói"),
    ("087682", "smokiness", "noun", "/ˈsmoʊkinəs/", "sự mù khói; mùi vị hun khói"),
    ("087683", "smokingly", "adv", "/ˈsmoʊkɪŋli/", "ngùn ngụt như khói bốc"),
    ("087684", "smoko", "noun", "/ˈsmoʊkoʊ/", "giờ giải lao ngắn (tiếng lóng Úc)"),
    ("087685", "smoldered", "verb", "/ˈsmoʊldərd/", "đã cháy âm ỉ; âm ỉ bực tức"),
    ("087686", "smolderingly", "adv", "/ˈsmoʊldərɪŋli/", "âm ỉ cháy; chất chứa giận dữ"),
    ("087687", "smolders", "verb", "/ˈsmoʊldərz/", "cháy âm ỉ không ngọn lửa; âm ỉ giận"),
    ("087688", "smolt", "noun", "/smoʊlt/", "cá hồi non chuẩn bị ra biển"),
    ("087689", "smooched", "verb", "/smuːtʃt/", "đã hôn hít âu yếm nồng nhiệt"),
    ("087690", "smooches", "verb", "/ˈsmuːtʃɪz/", "hôn hít âu yếm nồng nhiệt"),
    ("087691", "smoothbark", "noun", "/ˈsmuːðˌbɑːrk/", "cây bạch đàn vỏ trơn Úc"),
    ("087692", "smoothering", "noun", "/ˈsmuːðərɪŋ/", "công đoạn làm nhẵn mịn bề mặt"),
    ("087693", "smoothfaced", "adj", "/ˈsmuːðˌfeɪst/", "mặt nhẵn nhụi không râu; giả tạo"),
    ("087694", "smoothhound", "noun", "/ˈsmuːðˌhaʊnd/", "cá nhám chó da trơn"),
    ("087695", "smoothies", "noun", "/ˈsmuːðiz/", "sinh tố trái cây xay; kẻ khéo miệng"),
    ("087696", "smoothing", "verb", "/ˈsmuːðɪŋ/", "đang vuốt phẳng; đang làm mịn"),
    ("087697", "smooths", "verb", "/smuːðz/", "vuốt phẳng; làm trơn mịn; xoa dịu"),
    ("087698", "smoothspoken", "adj", "/ˈsmuːðˌspoʊkən/", "ăn nói ngọt ngào khéo léo"),
    ("087699", "smorrebrod", "noun", "/ˈsmɜːrəˌbrɔːd/", "bánh mì kẹp hở kiểu Đan Mạch"),
    ("087700", "smorzando", "adj", "/smɔːrˈtsɑːndoʊ/", "nhẹ dần rồi tắt hẳn (âm nhạc)"),
    ("087701", "smote", "verb", "/smoʊt/", "đã giáng đòn mạnh; đã đánh bại"),
    ("087702", "smotherer", "noun", "/ˈsmʌðərər/", "kẻ làm ngạt thở; người kìm hãm"),
]

# Trim those longer than 35 chars cleanly
RECORDS[13] = ("087616", "smacked", "verb", "/smækt/", "đã tát; đã vỗ cái bốp; thoảng vị")
RECORDS[60] = ("087663", "smirked", "verb", "/smɜːrkt/", "đã cười khẩy tự mãn")
RECORDS[84] = ("087687", "smolders", "verb", "/ˈsmoʊldərz/", "cháy âm ỉ không lửa; âm ỉ giận")
RECORDS[92] = ("087695", "smoothies", "noun", "/ˈsmuːðiz/", "sinh tố hoa quả; kẻ dẻo miệng")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r06_raw_p2.json"))
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

json.dump(out, open("scratch/b38_r06_reviewed_p2.json", "w"), ensure_ascii=False, indent=2)
print("b38_r06_p2 saved OK")
