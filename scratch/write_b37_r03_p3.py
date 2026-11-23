import json

records = [
    ("081203", "quixotism", "noun", "/ˈkwɪksəˌtɪzəm/", "chủ nghĩa lãng mạn viển vông"),
    ("081204", "quixotry", "noun", "/ˈkwɪksətri/", "hành động hào hiệp phi thực tế"),
    ("081205", "quizzability", "noun", "/ˌkwɪzəˈbɪləti/", "tính chất đáng để trêu đùa"),
    ("081206", "quizzable", "adj", "/ˈkwɪzəbəl/", "đáng trêu đùa, có thể kiểm tra đố"),
    ("081207", "quizzed", "verb", "/kwɪzd/", "đã thẩm vấn; đã đố vui; soi mói"),
    ("081208", "quizzee", "noun", "/kwɪˈziː/", "người được hỏi, thí sinh vấn đáp"),
    ("081209", "quizzeer", "noun", "/ˈkwɪzər/", "người ra câu đố, người hỏi vặn"),
    ("081210", "quizzes", "noun", "/ˈkwɪzɪz/", "bài kiểm tra ngắn, cuộc đố vui"),
    ("081211", "quizzicality", "noun", "/ˌkwɪzɪˈkæləti/", "vẻ dò hỏi ngạc nhiên pha châm chọc"),
    ("081212", "quizzing", "verb", "/ˈkwɪzɪŋ/", "tra hỏi, thẩm vấn, kiểm tra đố vui"),
    ("081213", "quod", "noun", "/kwɑːd/", "nhà tù, nhà giam (tiếng lóng cũ)"),
    ("081214", "quoited", "verb", "/ˈkwɔɪtɪd/", "đã ném vòng sắt vào cọc (trò chơi)"),
    ("081215", "quoiting", "verb", "/ˈkwɔɪtɪŋ/", "ném vòng sắt vào cọc (trò chơi)"),
    ("081216", "quorate", "adj", "/ˈkwɔːrət/", "đủ số đại biểu hợp lệ để biểu quyết"),
    ("081217", "quoratean", "noun", "/kwɔːˈriːtən/", "ngữ hệ Quoratean (California)"),
    ("081218", "quotability", "noun", "/ˌkwoʊtəˈbɪləti/", "giá trị hay đáng được trích dẫn"),
    ("081219", "quotas", "noun", "/ˈkwoʊtəz/", "các hạn ngạch, định mức, chỉ tiêu"),
    ("081220", "quotations", "noun", "/kwoʊˈteɪʃənz/", "các câu trích dẫn; bảng báo giá"),
    ("081221", "quotative", "adj", "/ˈkwoʊtətɪv/", "dùng trích dẫn trực tiếp (ngữ pháp)"),
    ("081222", "quoteable", "adj", "/ˈkwoʊtəbəl/", "đáng trích dẫn (biến thể chính tả)"),
    ("081223", "quoted", "verb", "/ˈkwoʊtɪd/", "đã trích dẫn; đã báo giá niêm yết"),
    ("081224", "quotes", "verb", "/kwoʊts/", "trích dẫn; nêu bằng chứng; báo giá"),
    ("081225", "quoth", "verb", "/kwoʊθ/", "nói rằng, thưa rằng (từ cổ văn học)"),
    ("081226", "quotients", "noun", "/ˈkwoʊʃənts/", "thương số (phép chia); chỉ số"),
    ("081227", "quoting", "verb", "/ˈkwoʊtɪŋ/", "trích dẫn, dẫn chứng; báo giá"),
    ("081228", "quotum", "noun", "/ˈkwoʊtəm/", "hạn mức, định mức, phần phân bổ"),
    ("081229", "qurush", "noun", "/kʊˈruːʃ/", "đồng tiền xu qurush (Ả Rập Xê Út)"),
    ("081230", "qutb", "noun", "/ˈkʊtəb/", "bậc thánh trụ cột tâm linh"),
    ("081231", "qv", "noun", "/ˌkjuːˈviː/", "xem mục đó (viết tắt Latin)"),
    ("081232", "qwerty", "adj", "/ˈkwɜːrti/", "theo bố cục bàn phím chuẩn QWERTY"),
    ("081233", "qwertyuiop", "adj", "/ˌkwɜːrtiˈjuːiɑːp/", "thuộc hàng phím trên cùng QWERTY"),
    ("081234", "rabato", "noun", "/rəˈbɑːtoʊ/", "cổ áo ren dựng cao thế kỷ 17"),
    ("081235", "rabban", "noun", "/rəˈbɑːn/", "bậc tôn sư, thầy giảng luật Do Thái"),
    ("081236", "rabbeted", "verb", "/ˈræbətɪd/", "đã bào hèm, đã ghép mộng rãnh gỗ"),
    ("081237", "rabbeting", "verb", "/ˈræbətɪŋ/", "bào hèm, xẻ rãnh ghép mộng gỗ"),
    ("081238", "rabbets", "verb", "/ˈræbəts/", "bào hèm rãnh, ghép khớp mộng gỗ"),
    ("081239", "rabbin", "noun", "/ˈræbɪn/", "giáo sĩ Do Thái (cách viết cổ)"),
    ("081240", "rabbinicall", "adj", "/rəˈbɪnɪkəl/", "thuộc giáo sĩ Do Thái (biến thể)"),
    ("081241", "rabbinism", "noun", "/ˈræbəˌnɪzəm/", "học thuyết và truyền thống Do Thái"),
    ("081242", "rabbinist", "noun", "/ˈræbənɪst/", "người theo luật kinh Talmud Do Thái"),
    ("081243", "rabbited", "verb", "/ˈræbətɪd/", "đã săn thỏ; đã tán gẫu (lóng Anh)"),
    ("081244", "rabbiteye", "noun", "/ˈræbətˌaɪ/", "cây việt quất mắt thỏ Bắc Mỹ"),
    ("081245", "rabbitfish", "noun", "/ˈræbətˌfɪʃ/", "cá dìa, cá thỏ biển (Siganus)"),
    ("081246", "rabbiting", "verb", "/ˈræbətɪŋ/", "đi săn thỏ; nói huyên thuyên (lóng)"),
    ("081247", "rabbitries", "noun", "/ˈræbətriz/", "những trại nuôi thỏ, chuồng thỏ"),
    ("081248", "rabbitry", "noun", "/ˈræbətri/", "chuồng nuôi thỏ, trại chăn nuôi thỏ"),
    ("081249", "rabbits", "verb", "/ˈræbɪts/", "săn thỏ; nói huyên thuyên không dứt"),
    ("081250", "rabbitweed", "noun", "/ˈræbətˌwiːd/", "cây cỏ thỏ ăn (thực vật Bắc Mỹ)"),
    ("081251", "rabbitwood", "noun", "/ˈræbətˌwʊd/", "cây bụi gạc hươu, cây gỗ thỏ"),
    ("081252", "rabbity", "adj", "/ˈræbəti/", "giống thỏ, nhút nhát; có mùi thỏ"),
    ("081253", "rabblement", "noun", "/ˈræbəlmənt/", "đám đông ồn ào hỗn loạn (từ cổ)"),
    ("081254", "rabbler", "noun", "/ˈræblər/", "cây cào xỉ lò luyện kim; kẻ la ó"),
    ("081255", "rabidity", "noun", "/rəˈbɪdəti/", "sự điên cuồng, thái độ quá khích"),
    ("081256", "rabidness", "noun", "/ˈræbɪdnəs/", "sự cuồng tín, tính chất hung dữ"),
    ("081257", "rabon", "noun", "/rəˈbɑːn/", "tên họ Rabon (tiếng Anh)"),
    ("081258", "rabons", "noun", "/rəˈbɑːnz/", "gia đình họ Rabon"),
    ("081259", "raborn", "noun", "/ˈreɪbɔːrn/", "tên họ Raborn (tiếng Anh)"),
    ("081260", "raborns", "noun", "/ˈreɪbɔːrnz/", "gia đình họ Raborn"),
    ("081261", "rac", "noun", "/ˌɑːreɪˈsiː/", "Câu lạc bộ Ô tô Hoàng gia Anh"),
    ("081262", "raceabout", "noun", "/ˈreɪsəˌbaʊt/", "thuyền buồm đua nhỏ; xe thể thao cổ"),
    ("081263", "raced", "verb", "/reɪst/", "đã chạy đua, phóng nhanh; đập gấp"),
    ("081264", "racemiferous", "adj", "/ˌræsəˈmɪfərəs/", "mang hoa mọc thành chùm (thực vật)"),
    ("081265", "racemule", "noun", "/ˈræsəmjuːl/", "chùm hoa nhỏ, cụm hoa con"),
    ("081266", "racemulose", "adj", "/ˌræsəmˈjʊloʊs/", "mọc thành chùm hoa nhỏ (thực vật)"),
    ("081267", "raceplay", "noun", "/ˈreɪsˌpleɪ/", "nhập vai tình huống sắc tộc"),
    ("081268", "racerunner", "noun", "/ˈreɪsˌrʌnər/", "thằn lằn chạy nhanh Bắc Mỹ"),
    ("081269", "races", "verb", "/ˈreɪsɪz/", "chạy đua, thi đấu; phóng nhanh"),
    ("081270", "racetracks", "noun", "/ˈreɪsˌtræks/", "những trường đua (ngựa, ô tô)"),
    ("081271", "rachial", "adj", "/ˈreɪkiəl/", "thuộc cột sống, sống lưng"),
    ("081272", "rachidial", "adj", "/rəˈkɪdiəl/", "thuộc trục cột sống hoặc trục lá"),
    ("081273", "rachidian", "adj", "/rəˈkɪdiən/", "thuộc cột sống; dọc theo trục giữa"),
    ("081274", "rachiform", "adj", "/ˈreɪkəˌfɔːrm/", "có dạng giống trục cột sống"),
    ("081275", "rachilla", "noun", "/rəˈkɪlə/", "trục nhánh hoa nhỏ (cỏ, lúa)"),
    ("081276", "rachiodont", "adj", "/ˈreɪkiəˌdɑːnt/", "có răng sống lưng nuốt trứng (rắn)"),
    ("081277", "rachischisis", "noun", "/rəˈkɪskəsɪs/", "dị tật chẻ đôi cột sống bẩm sinh"),
    ("081278", "rachitic", "adj", "/rəˈkɪtɪk/", "mắc bệnh còi xương, yếu ớt"),
    ("081279", "rachitis", "noun", "/rəˈkaɪtɪs/", "bệnh còi xương; viêm cột sống"),
    ("081280", "rachmanism", "noun", "/ˈrɑːkməˌnɪzəm/", "thủ đoạn bóc lột người thuê nhà trọ"),
    ("081281", "rachycentridae", "noun", "/ˌrækəˈsɛntrɪˌdiː/", "họ Cá bớp biển (Rachycentridae)"),
    ("081282", "rachycentron", "noun", "/ˌrækəˈsɛntrɑːn/", "chi cá bớp biển (Rachycentron)"),
    ("081283", "racily", "adv", "/ˈreɪsəli/", "sống động hấp dẫn; hơi suồng sã"),
    ("081284", "raciness", "noun", "/ˈreɪsinəs/", "nét dí dỏm táo bạo; hương vị đậm đà"),
    ("081285", "racists", "noun", "/ˈreɪsɪsts/", "những kẻ phân biệt chủng tộc"),
    ("081286", "racked", "verb", "/rækt/", "đã tra tấn; đã hành hạ; đã xếp giá"),
    ("081287", "racker", "noun", "/ˈrækər/", "người xếp bi; ngựa chạy nước kiệu"),
    ("081288", "racketed", "verb", "/ˈrækətɪd/", "đã gây ồn ào; đã tống tiền"),
    ("081289", "racketiness", "noun", "/ˈrækətinəs/", "sự ồn ào náo nhiệt; thói ăn chơi"),
    ("081290", "racketing", "verb", "/ˈrækətɪŋ/", "làm ầm ĩ ồn ào; ăn chơi trác táng"),
    ("081291", "rackets", "verb", "/ˈrækəts/", "gây ồn ào náo nhiệt; tống tiền"),
    ("081292", "racks", "verb", "/ræks/", "hành hạ dữ dội; xếp lên giá"),
    ("081293", "rada", "noun", "/ˈrɑːdə/", "Học viện Kịch nghệ Hoàng gia Anh"),
    ("081294", "radhomanthine", "adj", "/ˌrædəˈmænθaɪn/", "nghiêm khắc công minh (thẩm phán)"),
    ("081295", "radiable", "adj", "/ˈreɪdiəbəl/", "cho tia bức xạ xuyên qua được"),
    ("081296", "radiacmeter", "noun", "/ˈreɪdiækˌmiːtər/", "máy đo cường độ phóng xạ quân sự"),
    ("081297", "radiale", "noun", "/ˌreɪdiˈeɪli/", "xương cổ tay phía xương quay"),
    ("081298", "radialia", "noun", "/ˌreɪdiˈeɪliə/", "các xương tia đỡ vây cá (giải phẫu)"),
    ("081299", "radiancy", "noun", "/ˈreɪdiənsi/", "sự rực rỡ chói lọi; vẻ hân hoan"),
    ("081300", "radiated", "verb", "/ˈreɪdiˌeɪtɪd/", "đã bức xạ, đã phát ra; đã tỏa sáng"),
    ("081301", "radiates", "verb", "/ˈreɪdiˌeɪts/", "bức xạ, phát xạ; tỏa ra từ tâm"),
    ("081302", "radiatiform", "adj", "/ˌreɪdiˈeɪtəˌfɔːrm/", "có cấu trúc tỏa tia hình sao"),
]

raw = json.load(open("scratch/b37_r03_raw_p3.json"))
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
with open("scratch/b37_r03_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r03_p3 saved OK")
