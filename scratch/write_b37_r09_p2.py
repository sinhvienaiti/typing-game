import json

RECORDS = [
    ("084103", "rosaceous", "adj", "/roʊˈzeɪʃəs/", "thuộc họ Hoa hồng"),
    ("084104", "rosarian", "noun", "/roʊˈzɛriən/", "người trồng và yêu hoa hồng"),
    ("084105", "rosaries", "noun", "/ˈroʊzəriz/", "chuỗi tràng hạt; kinh Mân Côi"),
    ("084106", "rosarium", "noun", "/roʊˈzɛriəm/", "vườn chuyên trồng hoa hồng"),
    ("084107", "rosefish", "noun", "/ˈroʊzˌfɪʃ/", "cá hồng biển Đại Tây Dương"),
    ("084108", "rosellinia", "noun", "/ˌroʊzəˈlɪniə/", "chi nấm mốc Rosellinia"),
    ("084109", "rosemaling", "noun", "/ˈroʊzˌmɑːlɪŋ/", "nghệ thuật vẽ hoa Na Uy"),
    ("084110", "roseolar", "adj", "/roʊˈziːələr/", "có nốt ban đào; thuộc ban đào"),
    ("084111", "rosidae", "noun", "/ˈroʊzɪˌdiː/", "phân lớp Hoa hồng (Rosidae)"),
    ("084112", "rosilla", "noun", "/roʊˈsɪlə/", "cây cỏ hắt hơi tây nam Mỹ"),
    ("084113", "rosily", "adv", "/ˈroʊzɪli/", "màu hồng tươi; đầy lạc quan"),
    ("084114", "rosined", "verb", "/ˈrɑːzənd/", "đã xoa nhựa thông (vĩ đàn)"),
    ("084115", "rosining", "verb", "/ˈrɑːzənɪŋ/", "đang xoa nhựa thông"),
    ("084116", "rosins", "verb", "/ˈrɑːzənz/", "xoa nhựa thông; tẩm nhựa thông"),
    ("084117", "rosinweed", "noun", "/ˈrɑːzənˌwiːd/", "cây cỏ nhựa thông"),
    ("084118", "rosiny", "adj", "/ˈrɑːzəni/", "có chất nhựa thông; như nhựa thông"),
    ("084119", "rostella", "noun", "/rɑːˈstɛlə/", "mỏ nhọn; cựa hoa lan"),
    ("084120", "rostellar", "adj", "/rɑːˈstɛlər/", "thuộc mỏ nhọn; thuộc vòi"),
    ("084121", "rostellate", "adj", "/ˈrɑːstəˌleɪt/", "có mỏ nhọn nhỏ; có vòi nhỏ"),
    ("084122", "rostellum", "noun", "/rɑːˈstɛləm/", "mỏ nhọn; cựa hoa lan; vòi sán"),
    ("084123", "rostra", "noun", "/ˈrɑːstrə/", "mũi tàu chiến; bục diễn thuyết"),
    ("084124", "rostral", "adj", "/ˈrɑːstrəl/", "thuộc mỏ; hướng về phía đầu"),
    ("084125", "rostrat", "adj", "/ˈrɑːstrət/", "có mỏ; hình mỏ chim"),
    ("084126", "rostrate", "adj", "/ˈrɑːstreɪt/", "có mỏ; dạng mỏ chim"),
    ("084127", "rostrated", "adj", "/ˈrɑːstreɪtɪd/", "có mỏ; có vòi nhọn"),
    ("084128", "rostriform", "adj", "/ˈrɑːstrɪˌfɔːrm/", "có dạng mỏ chim"),
    ("084129", "rosular", "adj", "/ˈrɑːsjələr/", "xếp hình hoa thị (lá cây)"),
    ("084130", "rotameter", "noun", "/roʊˈtæmɪtər/", "lưu lượng kế phao; thước đo bản đồ"),
    ("084131", "rotas", "noun", "/ˈroʊtəz/", "bảng phân công luân phiên"),
    ("084132", "rotates", "verb", "/ˈroʊteɪts/", "quay; xoay vòng; luân phiên"),
    ("084133", "rotating", "verb", "/ˈroʊteɪtɪŋ/", "đang quay; đang luân phiên"),
    ("084134", "rotative", "adj", "/ˈroʊtətɪv/", "quay vòng; luân phiên"),
    ("084135", "rotator", "noun", "/ˈroʊteɪtər/", "cơ xoay; bộ phận quay"),
    ("084136", "rotatoria", "noun", "/ˌroʊtəˈtɔːriə/", "lớp Luân trùng (Rotatoria)"),
    ("084137", "rotatorium", "noun", "/ˌroʊtəˈtɔːriəm/", "khớp xoay (giải phẫu)"),
    ("084138", "rotegut", "noun", "/ˈrɑːtˌɡʌt/", "rượu rẻ tiền hại dạ dày"),
    ("084139", "rotifera", "noun", "/roʊˈtɪfərə/", "ngành Luân trùng (Rotifera)"),
    ("084140", "rotiform", "adj", "/ˈroʊtɪˌfɔːrm/", "hình bánh xe; dạng vành tròn"),
    ("084141", "rotl", "noun", "/ˈrɑːtəl/", "đơn vị cân cổ vùng Trung Đông"),
    ("084142", "rotorcraft", "noun", "/ˈroʊtərˌkræft/", "máy bay cánh quay; trực thăng"),
    ("084143", "rotortiller", "noun", "/ˈroʊtərˌtɪlər/", "máy xới đất trục quay"),
    ("084144", "rottenly", "adv", "/ˈrɑːtənli/", "tồi tệ; thối nát"),
    ("084145", "rottenstone", "noun", "/ˈrɑːtənˌstoʊn/", "bột đá vôi đánh bóng kim loại"),
    ("084146", "rotula", "noun", "/ˈrɑːtjələ/", "xương bánh chè; bộ phận nhím biển"),
    ("084147", "rotular", "adj", "/ˈrɑːtjələr/", "thuộc xương bánh chè"),
    ("084148", "rotule", "noun", "/ˈrɑːtjuːl/", "xương bánh chè"),
    ("084149", "rotundate", "adj", "/roʊˈtʌndət/", "tròn trịa; bo tròn góc"),
    ("084150", "rotundifolious", "adj", "/roʊˌtʌndɪˈfoʊliəs/", "có lá tròn"),
    ("084151", "rotundly", "adv", "/roʊˈtʌndli/", "tròn trịa; vang dội oang oang"),
    ("084152", "rotundness", "noun", "/roʊˈtʌndnəs/", "vẻ tròn trịa; độ vang tròn tiếng"),
    ("084153", "roturier", "noun", "/roʊˌtʊriˈeɪ/", "người bình dân không có tước vị"),
    ("084154", "roucou", "noun", "/ruːˈkuː/", "cây điều nhuộm; chất màu annatto"),
    ("084155", "rougeberry", "noun", "/ˈruːʒˌbɛri/", "cây quả đỏ rougeberry"),
    ("084156", "rouges", "verb", "/ˈruːʒɪz/", "đánh má hồng; bôi phấn hồng"),
    ("084157", "roughdried", "adj", "/ˈrʌfˌdraɪd/", "đã phơi khô nhưng chưa ủi phẳng"),
    ("084158", "roughed", "verb", "/rʌft/", "đã phác thảo thô; đã chơi thô bạo"),
    ("084159", "roughening", "verb", "/ˈrʌfənɪŋ/", "đang làm thô nhám"),
    ("084160", "roughens", "verb", "/ˈrʌfənz/", "làm thô nhám; trở nên sần sùi"),
    ("084161", "roughhewn", "adj", "/ˌrʌfˈhjuːn/", "đẽo thô; chưa gọt giũa"),
    ("084162", "roughing", "verb", "/ˈrʌfɪŋ/", "đang gia công thô; đang chơi thô"),
    ("084163", "roughish", "adj", "/ˈrʌfɪʃ/", "hơi thô; hơi nhám"),
    ("084164", "roughleg", "noun", "/ˈrʌfˌlɛɡ/", "chim ó chân lông"),
    ("084165", "roughometer", "noun", "/rʌˈfɑːmɪtər/", "máy đo độ gồ ghề mặt đường"),
    ("084166", "roughs", "verb", "/rʌfs/", "phác thảo thô; chơi thô bạo"),
    ("084167", "rouging", "verb", "/ˈruːʒɪŋ/", "đang đánh má hồng"),
    ("084168", "rouleaux", "noun", "/ruːˈloʊ/", "cọc tiền xu cuộn giấy; chuỗi hồng cầu"),
    ("084169", "roundaboutness", "noun", "/ˈraʊndəˌbaʊtnəs/", "sự vòng vo quanh co"),
    ("084170", "roundabouts", "noun", "/ˈraʊndəˌbaʊts/", "bùng binh giao thông; vòng xoay"),
    ("084171", "roundheaded", "adj", "/ˌraʊndˈhɛdɪd/", "có đầu tròn; đầu ngắn"),
    ("084172", "rounds", "verb", "/raʊndz/", "đi tuần tra; làm tròn số"),
    ("084173", "roundsman", "noun", "/ˈraʊndzmən/", "nhân viên giao hàng định kỳ"),
    ("084174", "roup", "noun", "/ruːp/", "bệnh sổ mũi truyền nhiễm ở gà"),
    ("084175", "rouseabout", "noun", "/ˈraʊzəˌbaʊt/", "nhân công tạp vụ trại cừu"),
    ("084176", "roused", "verb", "/raʊzd/", "đã đánh thức; đã khơi dậy"),
    ("084177", "rouses", "verb", "/ˈraʊzɪz/", "đánh thức; khơi dậy"),
    ("084178", "rousseauan", "adj", "/ruːˈsoʊən/", "thuộc triết gia Jean-Jacques Rousseau"),
    ("084179", "roust", "verb", "/raʊst/", "xua đuổi; khuấy động mạnh"),
    ("084180", "rousted", "verb", "/ˈraʊstɪd/", "đã xua đuổi; đã lôi ra"),
    ("084181", "rousting", "verb", "/ˈraʊstɪŋ/", "đang xua đuổi; đang khuấy động"),
    ("084182", "rousts", "verb", "/raʊsts/", "xua đuổi; khuấy động"),
    ("084183", "routed", "verb", "/ˈruːtɪd/", "đã định tuyến; đã đánh tan tác"),
    ("084184", "routeman", "noun", "/ˈruːtmən/", "nhân viên giao hàng theo tuyến"),
    ("084185", "routemarch", "noun", "/ˈruːtˌmɑːrtʃ/", "cuộc hành quân đường dài"),
    ("084186", "routes", "verb", "/ruːts/", "định tuyến; chuyển hướng đi"),
    ("084187", "routing", "verb", "/ˈruːtɪŋ/", "đang định tuyến; đang dẫn đường"),
    ("084188", "routinise", "verb", "/ruːˈtiːˌnaɪz/", "biến thành thói quen thường nhật"),
    ("084189", "routinised", "verb", "/ruːˈtiːˌnaɪzd/", "đã biến thành lệ thường"),
    ("084190", "routinises", "verb", "/ruːˈtiːˌnaɪzɪz/", "biến thành lệ thường"),
    ("084191", "routinising", "verb", "/ruːˈtiːˌnaɪzɪŋ/", "đang biến thành lệ thường"),
    ("084192", "routinism", "noun", "/ruːˈtiːˌnɪzəm/", "thói quen rập khuôn bảo thủ"),
    ("084193", "routinize", "verb", "/ruːˈtiːˌnaɪz/", "biến thành thói quen thường nhật"),
    ("084194", "routinized", "verb", "/ruːˈtiːˌnaɪzd/", "đã biến thành lệ thường"),
    ("084195", "routinizes", "verb", "/ruːˈtiːˌnaɪzɪz/", "biến thành lệ thường"),
    ("084196", "routinizing", "verb", "/ruːˈtiːˌnaɪzɪŋ/", "đang biến thành lệ thường"),
    ("084197", "routs", "verb", "/raʊts/", "đánh tan tác; khoét rãnh gỗ"),
    ("084198", "rovers", "noun", "/ˈroʊvərz/", "người lãng du; xe tự hành"),
    ("084199", "rowanberry", "noun", "/ˈroʊənˌbɛri/", "quả thanh lương trà"),
    ("084200", "rowdily", "adv", "/ˈraʊdɪli/", "ồn ào hỗn loạn; ngỗ ngược"),
    ("084201", "rowdinesses", "noun", "/ˈraʊdinəsɪz/", "sự ồn ào gây rối"),
    ("084202", "rowed", "verb", "/roʊd/", "đã chèo thuyền; đã cãi vã"),
]

# Shorten 084118, 084168, 084178 to <= 35 cleanly
RECORDS[15] = ("084118", "rosiny", "adj", "/ˈrɑːzəni/", "có nhựa thông; như nhựa thông")
RECORDS[65] = ("084168", "rouleaux", "noun", "/ruːˈloʊ/", "cọc tiền xu cuộn; chuỗi hồng cầu")
RECORDS[75] = ("084178", "rousseauan", "adj", "/ruːˈsoʊən/", "theo triết lý của Rousseau")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r09_raw_p2.json"))
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

json.dump(out, open("scratch/b37_r09_reviewed_p2.json", "w"), ensure_ascii=False, indent=2)
print("b37_r09_p2 saved OK")
