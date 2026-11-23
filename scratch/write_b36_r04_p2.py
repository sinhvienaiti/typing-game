import json

rows = [
    ("076603", "pierrette", "noun", "/ˌpjɛrˈɛt/", "nữ diễn viên kịch câm Pierrette"),
    ("076604", "pies", "noun", "/paɪz/", "bánh nướng nhân (pie)"),
    ("076605", "pietist", "noun", "/ˈpaɪɪtɪst/", "tín đồ kính tín; người quá sùng đạo"),
    ("076606", "pietistical", "adj", "/ˌpaɪɪˈtɪstɪkəl/", "thuộc thuyết kính tín; sùng đạo giả"),
    ("076607", "pietistically", "adv", "/ˌpaɪɪˈtɪstɪkli/", "một cách quá sùng đạo, đạo đức giả"),
    ("076608", "piezochemistry", "noun", "/piˌeɪzoʊˈkɛmɪstri/", "áp hóa học (hóa học áp suất cao)"),
    ("076609", "piezoelectrical", "adj", "/piˌeɪzoʊɪˈlɛktrɪkəl/", "thuộc hiệu ứng áp điện"),
    ("076610", "piezoelectrically", "adv", "/piˌeɪzoʊɪˈlɛktrɪkli/", "bằng hiệu ứng áp điện"),
    ("076611", "piezometer", "noun", "/ˌpaɪɪˈzɒmɪtər/", "áp kế; máy đo độ nén chất lỏng"),
    ("076612", "piezometric", "adj", "/ˌpaɪɪzəˈmɛtrɪk/", "thuộc áp kế, đo áp suất"),
    ("076613", "pif", "noun", "/pɪf/", "tệp thông tin chương trình PIF"),
    ("076614", "piffler", "noun", "/ˈpɪflər/", "người hay nói nhảm nhí vớ vẩn"),
    ("076615", "pigboat", "noun", "/ˈpɪɡboʊt/", "tàu ngầm (tiếng lóng hải quân)"),
    ("076616", "pigeoned", "verb", "/ˈpɪdʒənd/", "đã lừa bịp (khẩu ngữ)"),
    ("076617", "pigeongram", "noun", "/ˈpɪdʒənˌɡræm/", "thư tín do bồ câu đưa tin"),
    ("076618", "pigeonholes", "noun", "/ˈpɪdʒənˌhoʊlz/", "ô xếp thư; ngăn phân loại"),
    ("076619", "pigeoning", "verb", "/ˈpɪdʒənɪŋ/", "lừa bịp (khẩu ngữ)"),
    ("076620", "pigeonniers", "noun", "/ˌpiːʒɔːˈnjeɪz/", "chuồng chim bồ câu (Pháp)"),
    ("076621", "pigeonries", "noun", "/ˈpɪdʒənriz/", "chuồng nuôi chim bồ câu"),
    ("076622", "pigeonry", "noun", "/ˈpɪdʒənri/", "chuồng nuôi chim bồ câu"),
    ("076623", "pigeons", "verb", "/ˈpɪdʒənz/", "lừa bịp (khẩu ngữ)"),
    ("076624", "pigfish", "noun", "/ˈpɪɡfɪʃ/", "cá heo mõm lợn (cá vây pigfish)"),
    ("076625", "pigged", "verb", "/pɪɡd/", "đã ăn ngấu nghiến; đẻ lợn con"),
    ("076626", "piggeries", "noun", "/ˈpɪɡəriz/", "chuồng lợn; trại nuôi lợn; nơi bẩn"),
    ("076627", "pigging", "verb", "/ˈpɪɡɪŋ/", "ăn ngấu nghiến; đẻ lợn con"),
    ("076628", "piggishly", "adv", "/ˈpɪɡɪʃli/", "tham ăn tục uống, bẩn thỉu"),
    ("076629", "piggishness", "noun", "/ˈpɪɡɪʃnəs/", "tính tham ăn tục uống; sự bẩn thỉu"),
    ("076630", "piggybank", "noun", "/ˈpɪɡiˌbæŋk/", "ống heo tiết kiệm (heo đất)"),
    ("076631", "pigheadedly", "adv", "/ˌpɪɡˈhɛdɪdli/", "một cách bướng bỉnh, ngoan cố"),
    ("076632", "pigheadedness", "noun", "/ˌpɪɡˈhɛdɪdnəs/", "tính bướng bỉnh, cứng đầu cứng cổ"),
    ("076633", "pigling", "noun", "/ˈpɪɡlɪŋ/", "lợn con"),
    ("076634", "pigmental", "adj", "/pɪɡˈmɛntəl/", "thuộc sắc tố, chất tạo màu"),
    ("076635", "pigmentary", "adj", "/ˈpɪɡməntəri/", "thuộc sắc tố, chất tạo màu"),
    ("076636", "pignolia", "noun", "/pɪnˈjoʊliə/", "hạt thông ăn được (pignolia)"),
    ("076637", "pigpens", "noun", "/ˈpɪɡpɛnz/", "chuồng lợn; nơi ở bẩn thỉu bừa bộn"),
    ("076638", "pigs", "verb", "/pɪɡz/", "ăn ngấu nghiến như lợn; sống bừa"),
    ("076639", "pigskins", "noun", "/ˈpɪɡˌskɪnz/", "da lợn; bóng bầu dục (tiếng lóng)"),
    ("076640", "pigsticker", "noun", "/ˈpɪɡˌstɪkər/", "người săn lợn rừng; dao bầu"),
    ("076641", "pigsticking", "noun", "/ˈpɪɡˌstɪkɪŋ/", "môn săn lợn rừng bằng giáo (cổ)"),
    ("076642", "pigsties", "noun", "/ˈpɪɡstaɪz/", "chuồng lợn; nơi bẩn thỉu bừa bộn"),
    ("076643", "pigswill", "noun", "/ˈpɪɡswɪl/", "cám lợn; đồ ăn thức uống dở tệ"),
    ("076644", "pigtails", "noun", "/ˈpɪɡteɪlz/", "tóc bím đuôi sam"),
    ("076645", "pigwash", "noun", "/ˈpɪɡwɒʃ/", "cám lợn; văn chương nhảm nhí"),
    ("076646", "pijama", "noun", "/pəˈdʒɑːmə/", "đồ ngủ bộ pijama"),
    ("076647", "pikeblenny", "noun", "/ˈpaɪkˌblɛni/", "cá mào gà pikeblenny (biển)"),
    ("076648", "piked", "verb", "/paɪkt/", "đã đâm bằng giáo; nhảy gập người"),
    ("076649", "pikelet", "noun", "/ˈpaɪklɪt/", "bánh nướng chảo nhỏ (pikelet)"),
    ("076650", "pikeman", "noun", "/ˈpaɪkmən/", "lính giáo cổ; thợ mỏ dùng cuốc chim"),
    ("076651", "piker", "noun", "/ˈpaɪkər/", "kẻ keo kiệt nhỏ nhen; tay bạc nhút"),
    ("076652", "pikes", "verb", "/paɪks/", "đâm bằng giáo; nhảy gập người"),
    ("076653", "piking", "verb", "/ˈpaɪkɪŋ/", "đâm bằng giáo; nhảy gập người"),
    ("076654", "pilaff", "noun", "/pɪˈlɑːf/", "cơm nấu thập cẩm pilaf"),
    ("076655", "pilary", "adj", "/ˈpɪləri/", "thuộc lông, tóc (sinh học)"),
    ("076656", "pilaw", "noun", "/pɪˈlɔː/", "cơm nấu thập cẩm pilaf"),
    ("076657", "pilch", "noun", "/pɪltʃ/", "quần nỉ lót tã trẻ em (cổ)"),
    ("076658", "pilcrow", "noun", "/ˈpɪlkroʊ/", "ký hiệu xuống đoạn văn (¶)"),
    ("076659", "pilcrows", "noun", "/ˈpɪlkroʊz/", "ký hiệu xuống đoạn văn (¶)"),
    ("076660", "piled", "verb", "/paɪld/", "đã chất đống; đóng cọc"),
    ("076661", "pilewort", "noun", "/ˈpaɪlwɜːrt/", "cây mao lương chữa trĩ (Ficaria)"),
    ("076662", "pilfered", "verb", "/ˈpɪlfərd/", "đã ăn cắp vặt, trộm vặt"),
    ("076663", "pilfering", "verb", "/ˈpɪlfərɪŋ/", "ăn cắp vặt, trộm vặt"),
    ("076664", "pilfers", "verb", "/ˈpɪlfərz/", "ăn cắp vặt, trộm vặt"),
    ("076665", "piliferous", "adj", "/paɪˈlɪfərəs/", "có mang lông, râu (sinh học)"),
    ("076666", "pillages", "verb", "/ˈpɪlɪdʒɪz/", "cướp phá, cướp bóc (chiến tranh)"),
    ("076667", "pillboxes", "noun", "/ˈpɪlˌbɒksɪz/", "hộp đựng thuốc; lô cốt phòng thủ"),
    ("076668", "pilliwinks", "noun", "/ˈpɪliwɪŋks/", "dụng cụ kẹp tra tấn ngón tay (cổ)"),
    ("076669", "pilloried", "verb", "/ˈpɪlərid/", "đã đóng gông; bêu riếu công khai"),
    ("076670", "pillories", "verb", "/ˈpɪləriz/", "đóng gông; bêu riếu công khai"),
    ("076671", "pillorying", "verb", "/ˈpɪləriɪŋ/", "đóng gông; bêu riếu công khai"),
    ("076672", "pillowed", "verb", "/ˈpɪloʊd/", "đã gối đầu lên; tựa lên êm ái"),
    ("076673", "pillowing", "verb", "/ˈpɪloʊɪŋ/", "gối đầu lên; nâng đỡ tựa gối"),
    ("076674", "pillows", "verb", "/ˈpɪloʊz/", "gối đầu lên; nâng đỡ tựa gối"),
    ("076675", "pillowslip", "noun", "/ˈpɪloʊslɪp/", "vỏ gối, áo gối (Anh)"),
    ("076676", "pillowy", "adj", "/ˈpɪloʊi/", "mềm êm như gối, bồng bềnh"),
    ("076677", "pillule", "noun", "/ˈpɪljuːl/", "viên thuốc tròn nhỏ (viên hoàn)"),
    ("076678", "pillwort", "noun", "/ˈpɪlwɜːrt/", "cây dương xỉ thủy sinh Pilularia"),
    ("076679", "pilosebaceous", "adj", "/ˌpaɪloʊsɪˈbeɪʃəs/", "thuộc nang lông và tuyến bã nhờn"),
    ("076680", "pilosity", "noun", "/paɪˈlɒsɪti/", "tình trạng có nhiều lông, tóc"),
    ("076681", "piloted", "verb", "/ˈpaɪlətɪd/", "đã lái (máy bay, tàu); thử nghiệm"),
    ("076682", "pilotfish", "noun", "/ˈpaɪlətfɪʃ/", "cá dẫn đường (cá sọc hoa tiêu)"),
    ("076683", "pilots", "verb", "/ˈpaɪləts/", "lái (máy bay, tàu); chạy thử nghiệm"),
    ("076684", "pilous", "adj", "/ˈpaɪləs/", "có lông tơ; phủ lông mịn"),
    ("076685", "pilular", "adj", "/ˈpɪljələr/", "có dạng viên tròn nhỏ"),
    ("076686", "pilularia", "noun", "/ˌpɪljʊˈlɛriə/", "chi dương xỉ thủy sinh Pilularia"),
    ("076687", "pilule", "noun", "/ˈpɪljuːl/", "viên thuốc tròn nhỏ (viên hoàn)"),
    ("076688", "pilulous", "adj", "/ˈpɪljələs/", "có dạng viên tròn nhỏ"),
    ("076689", "pily", "adj", "/ˈpaɪli/", "có lông tơ; có tuyết mịn (vải)"),
    ("076690", "pimelode", "noun", "/ˈpɪmɪloʊd/", "cá nheo Nam Mỹ (họ Pimelodidae)"),
    ("076691", "piments", "noun", "/pɪˈmɛnts/", "ớt ngọt đỏ; hạt tiêu Jamaica"),
    ("076692", "pimped", "verb", "/pɪmpt/", "đã làm ma cô; độ trang trí đẹp"),
    ("076693", "pimpinella", "noun", "/ˌpɪmpɪˈnɛlə/", "chi cây hồi hương (Pimpinella)"),
    ("076694", "pimping", "adj", "/ˈpɪmpɪŋ/", "nhỏ nhen, tầm thường; ốm yếu"),
    ("076695", "pimps", "verb", "/pɪmps/", "làm môi giới ma cô; độ hào nhoáng"),
    ("076696", "pinaster", "noun", "/paɪˈnæstər/", "cây thông biển Địa Trung Hải"),
    ("076697", "pincers", "noun", "/ˈpɪnsərz/", "cái kìm, kẹp; càng cua bọ cạp"),
    ("076698", "pincette", "noun", "/pɪnˈsɛt/", "cái nhíp nhỏ, kẹp nhỏ (y tế)"),
    ("076699", "pinchers", "noun", "/ˈpɪntʃərz/", "cái kìm, kẹp; càng cua bọ cạp"),
    ("076700", "pinches", "verb", "/ˈpɪntʃɪz/", "véo, cấu; kẹp chặt; chôm chỉa"),
    ("076701", "pinchgut", "noun", "/ˈpɪntʃɡʌt/", "kẻ keo kiệt hà tiện bủn xỉn"),
    ("076702", "pinching", "verb", "/ˈpɪntʃɪŋ/", "véo, cấu; kẹp chặt; thắt ngặt"),
]

with open("scratch/b36_r04_raw_p2.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r04_p2.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r04_p2 saved OK")
