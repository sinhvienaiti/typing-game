import json

records = [
    ("082603", "rejigging", "verb", "/ˌriːˈdʒɪɡɪŋ/", "sắp xếp lại, cải tổ cơ cấu lại"),
    ("082604", "rejigs", "verb", "/ˌriːˈdʒɪɡz/", "sắp xếp lại, điều chỉnh lại máy"),
    ("082605", "rejoiced", "verb", "/rɪˈdʒɔɪst/", "đã vui mừng hân hoan, phấn khởi"),
    ("082606", "rejoices", "verb", "/rɪˈdʒɔɪsɪz/", "vui mừng hân hoan, hết sức mừng rỡ"),
    ("082607", "rejoined", "verb", "/ˌriːˈdʒɔɪnd/", "đã gia nhập lại; đã đối đáp lại"),
    ("082608", "rejoining", "verb", "/ˌriːˈdʒɔɪnɪŋ/", "gia nhập trở lại, tái hợp; đáp lời"),
    ("082609", "rejoins", "verb", "/ˌriːˈdʒɔɪnz/", "gia nhập lại, đoàn tụ; đối đáp lại"),
    ("082610", "rejuvenated", "verb", "/rɪˈdʒuːvəˌneɪtɪd/", "đã làm trẻ hóa, đã hồi sinh lại"),
    ("082611", "rejuvenates", "verb", "/rɪˈdʒuːvəˌneɪts/", "làm trẻ hóa, trẻ trung hồi xuân"),
    ("082612", "rejuvenating", "verb", "/rɪˈdʒuːvəˌneɪtɪŋ/", "làm trẻ hóa, tiếp thêm sức sống mới"),
    ("082613", "rejuvenations", "noun", "/rɪˌdʒuːvəˈneɪʃənz/", "những quá trình trẻ hóa, hồi xuân"),
    ("082614", "rejuvenesce", "verb", "/ˌriːdʒuːvəˈnɛs/", "trẻ lại, lấy lại tuổi thanh xuân"),
    ("082615", "rejuvenescence", "noun", "/ˌriːdʒuːvəˈnɛsəns/", "sự trẻ lại, quá trình trẻ hóa"),
    ("082616", "rejuvenescent", "adj", "/ˌriːdʒuːvəˈnɛsənt/", "làm trẻ lại, đang hồi xuân"),
    ("082617", "rekindled", "verb", "/ˌriːˈkɪndəld/", "đã nhóm lại lửa; đã khơi dậy lại"),
    ("082618", "rekindles", "verb", "/ˌriːˈkɪndəlz/", "nhóm lại lửa; khơi dậy lại tình cảm"),
    ("082619", "rekindling", "verb", "/ˌriːˈkɪndlɪŋ/", "nhóm lại lửa; nhen nhóm lại hy vọng"),
    ("082620", "relabel", "verb", "/ˌriːˈleɪbəl/", "dán nhãn lại, phân loại gắn mác lại"),
    ("082621", "relabelled", "verb", "/ˌriːˈleɪbəld/", "đã dán nhãn lại, gắn mác lại (Anh)"),
    ("082622", "relabelling", "verb", "/ˌriːˈleɪbəlɪŋ/", "dán nhãn lại, đặt tên mới (Anh)"),
    ("082623", "relabels", "verb", "/ˌriːˈleɪbəlz/", "dán nhãn lại, gắn lại nhãn mác mới"),
    ("082624", "relace", "verb", "/ˌriːˈleɪs/", "buộc lại dây (giày, áo nịt ngực)"),
    ("082625", "relafen", "noun", "/ˈrɛləfɛn/", "thuốc giảm đau chống viêm Relafen"),
    ("082626", "relapsed", "verb", "/rɪˈlæpst/", "đã tái phát (bệnh); đã tái nghiện"),
    ("082627", "relapses", "verb", "/rɪˈlæpsɪz/", "tái phát bệnh; tái nghiện, sa ngã"),
    ("082628", "relater", "noun", "/rɪˈleɪtər/", "người kể lại, người thuật chuyện"),
    ("082629", "relates", "verb", "/rɪˈleɪts/", "kể lại; liên hệ, có liên quan đến"),
    ("082630", "relating", "verb", "/rɪˈleɪtɪŋ/", "kể lại; liên hệ với, đồng cảm được"),
    ("082631", "relationships", "noun", "/rɪˈleɪʃənˌʃɪps/", "các mối quan hệ, sự gắn kết"),
    ("082632", "relationshopping", "noun", "/rɪˈleɪʃənˌʃɑːpɪŋ/", "kiểu hẹn hò kén chọn như đi mua sắm"),
    ("082633", "relativise", "verb", "/ˈrɛlətəˌvaɪz/", "tương đối hóa (cách viết Anh)"),
    ("082634", "relativist", "noun", "/ˈrɛlətəvɪst/", "người theo thuyết tương đối"),
    ("082635", "relativities", "noun", "/ˌrɛləˈtɪvətiz/", "sự tương quan tiền lương giữa nghề"),
    ("082636", "relator", "noun", "/rɪˈleɪtər/", "người đứng đơn kiện; người kể"),
    ("082637", "relatrix", "noun", "/rɪˈleɪtrɪks/", "nữ nguyên đơn thay mặt tố cáo"),
    ("082638", "relatum", "noun", "/rɪˈleɪtəm/", "đối tượng được quy chiếu (triết)"),
    ("082639", "relaxative", "adj", "/rɪˈlæksətɪv/", "làm giãn mềm, giúp thư giãn; nhuận"),
    ("082640", "relaxes", "verb", "/rɪˈlæksɪz/", "thư giãn, nghỉ ngơi; nới lỏng ra"),
    ("082641", "relaying", "noun", "/ˈriːleɪɪŋ/", "việc tiếp âm, truyền tiếp tín hiệu"),
    ("082642", "released", "verb", "/rɪˈliːst/", "đã thả ra, phóng thích; phát hành"),
    ("082643", "releasee", "noun", "/ˌrɪliːˈsiː/", "người được giải phóng nghĩa vụ"),
    ("082644", "releaser", "noun", "/rɪˈliːsər/", "cơ cấu nhả; tác nhân kích thích"),
    ("082645", "releases", "verb", "/rɪˈliːsɪz/", "thả ra, giải thoát; phát hành"),
    ("082646", "releasor", "noun", "/rɪˈliːsər/", "người từ bỏ quyền đòi hỏi (luật)"),
    ("082647", "relegated", "verb", "/ˈrɛləˌɡeɪtɪd/", "đã giáng hạng; đẩy xuống thứ yếu"),
    ("082648", "relegates", "verb", "/ˈrɛləˌɡeɪts/", "giáng hạng; xếp xuống vị trí thấp"),
    ("082649", "relented", "verb", "/rɪˈlɛntɪd/", "đã mủi lòng, đã nhượng bộ dịu lại"),
    ("082650", "relenting", "verb", "/rɪˈlɛntɪŋ/", "mủi lòng thương, dịu lại nhượng bộ"),
    ("082651", "relents", "verb", "/rɪˈlɛnts/", "mủi lòng, mềm lòng, chịu nhượng bộ"),
    ("082652", "relet", "verb", "/ˌriːˈlɛt/", "cho thuê lại (nhà đất) khi hết hạn"),
    ("082653", "reletting", "noun", "/ˌriːˈlɛtɪŋ/", "việc cho thuê lại tài sản (luật)"),
    ("082654", "reliableness", "noun", "/rɪˈlaɪəbəlnəs/", "độ tin cậy, tính chất đáng tin"),
    ("082655", "relied", "verb", "/rɪˈlaɪd/", "đã tin cậy, đã nương tựa, phụ thuộc"),
    ("082656", "relies", "verb", "/rɪˈlaɪz/", "tin cậy, dựa dẫm, phụ thuộc vào"),
    ("082657", "relieves", "verb", "/rɪˈliːvz/", "làm dịu (đau); giải tỏa; thay phiên"),
    ("082658", "relieving", "verb", "/rɪˈliːvɪŋ/", "làm dịu nhẹ, giải cứu; thay ca trực"),
    ("082659", "relievo", "noun", "/rɪˈliːvoʊ/", "tranh phù điêu chạm nổi"),
    ("082660", "religiology", "noun", "/rɪˌlɪdʒiˈɑːlədʒi/", "tôn giáo học (nghiên cứu tôn giáo)"),
    ("082661", "religioner", "noun", "/rɪˈlɪdʒənər/", "tu sĩ; tín đồ sùng đạo (từ cổ)"),
    ("082662", "religionise", "verb", "/rɪˈlɪdʒəˌnaɪz/", "tôn giáo hóa; sùng đạo (Anh)"),
    ("082663", "religionism", "noun", "/rɪˈlɪdʒəˌnɪzəm/", "lòng sùng đạo thái quá, cuồng tín"),
    ("082664", "religionize", "verb", "/rɪˈlɪdʒəˌnaɪz/", "tôn giáo hóa, truyền bá tôn giáo"),
    ("082665", "religions", "noun", "/rɪˈlɪdʒənz/", "các tôn giáo, tín ngưỡng"),
    ("082666", "religiose", "adj", "/rɪˈlɪdʒiˌoʊs/", "sùng đạo một cách thái quá, cuồng"),
    ("082667", "religiousism", "noun", "/rɪˈlɪdʒəsˌɪzəm/", "thói sùng đạo giả tạo, đạo đức giả"),
    ("082668", "relined", "verb", "/ˌriːˈlaɪnd/", "đã lót lớp mới (áo, phanh, răng)"),
    ("082669", "relines", "verb", "/ˌriːˈlaɪnz/", "lót lớp mới mặt trong (áo, phanh)"),
    ("082670", "relining", "verb", "/ˌriːˈlaɪnɪŋ/", "thay lớp lót bên trong (áo, lò)"),
    ("082671", "relinquishes", "verb", "/rɪˈlɪŋkwɪʃɪz/", "từ bỏ (quyền lợi), buông tay trao"),
    ("082672", "reliquae", "noun", "/ˈrɛlɪˌkwiː/", "di hài, di vật còn sót lại (cổ)"),
    ("082673", "relishable", "adj", "/ˈrɛlɪʃəbəl/", "thơm ngon hấp dẫn, đáng thưởng thức"),
    ("082674", "relished", "verb", "/ˈrɛlɪʃt/", "đã thưởng thức ngon lành, thích thú"),
    ("082675", "relishes", "verb", "/ˈrɛlɪʃɪz/", "thích thú, thưởng thức ngon lành"),
    ("082676", "reloaded", "verb", "/ˌriːˈloʊdɪd/", "đã nạp đạn lại; đã tải lại trang"),
    ("082677", "reloading", "verb", "/ˌriːˈloʊdɪŋ/", "nạp lại đạn; tải lại trang dữ liệu"),
    ("082678", "reloads", "verb", "/ˌriːˈloʊdz/", "nạp đạn lại; tải lại trang web"),
    ("082679", "relocatable", "adj", "/ˌriːˈloʊkətəbəl/", "có thể di dời, định vị lại được"),
    ("082680", "relocates", "verb", "/ˌriːˈloʊkeɪts/", "di dời, chuyển địa điểm đến nơi mới"),
    ("082681", "relocating", "verb", "/ˌriːˈloʊkeɪtɪŋ/", "di dời, chuyển chỗ ở hoặc trụ sở"),
    ("082682", "relucent", "adj", "/rɪˈluːsənt/", "sáng ngời, phản chiếu rực rỡ (thơ)"),
    ("082683", "reluct", "verb", "/rɪˈlʌkt/", "miễn cưỡng, chống đối lại (hiếm)"),
    ("082684", "reluctivity", "noun", "/ˌriːlʌkˈtɪvəti/", "từ trở suất của vật liệu (vật lý)"),
    ("082685", "relume", "verb", "/rɪˈluːm/", "thắp sáng lại, nhen lại ánh sáng"),
    ("082686", "relying", "verb", "/rɪˈlaɪɪŋ/", "tin cậy vào, dựa vào, phụ thuộc"),
    ("082687", "relyric", "verb", "/ˌriːˈlɪrɪk/", "viết lời ca mới cho giai điệu cũ"),
    ("082688", "remade", "verb", "/ˌriːˈmeɪd/", "đã làm lại, đã dựng lại phiên bản"),
    ("082689", "remained", "verb", "/rɪˈmeɪnd/", "đã ở lại, đã giữ nguyên, còn lại"),
    ("082690", "remakes", "noun", "/ˈriːmeɪks/", "những phiên bản phim, nhạc làm lại"),
    ("082691", "reman", "verb", "/ˌriːˈmæn/", "bố trí nhân sự mới, tuyển lại người"),
    ("082692", "remanded", "verb", "/rɪˈmændɪd/", "đã tạm giam; đã trả hồ sơ xử lại"),
    ("082693", "remanding", "verb", "/rɪˈmændɪŋ/", "tống tạm giam chờ xét xử; trả tòa"),
    ("082694", "remands", "verb", "/rɪˈmændz/", "tạm giam chờ xét xử; trả hồ sơ lại"),
    ("082695", "remanence", "noun", "/ˈrɛmənəns/", "từ dư, độ từ hóa còn dư (vật lý)"),
    ("082696", "remanent", "adj", "/ˈrɛmənənt/", "còn dư lại, còn sót lại sau cùng"),
    ("082697", "remanet", "noun", "/ˈrɛmənɪt/", "vụ án hoãn xử sang kỳ sau (luật)"),
    ("082698", "remarkableness", "noun", "/rɪˈmɑːrkəbəlnəs/", "tính chất đáng chú ý, sự phi thường"),
    ("082699", "remarked", "verb", "/rɪˈmɑːrkt/", "đã nhận xét, phát biểu; chú ý tới"),
    ("082700", "remarking", "verb", "/rɪˈmɑːrkɪŋ/", "nhận xét, bình luận; để ý nhận thấy"),
    ("082701", "remarks", "verb", "/rɪˈmɑːrks/", "nhận xét, phát biểu ý kiến; chú ý"),
    ("082702", "remarque", "noun", "/rəˈmɑːrk/", "dấu khắc nhỏ ngoài lề bản in thử"),
]

raw = json.load(open("scratch/b37_r06_raw_p2.json"))
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
with open("scratch/b37_r06_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r06_p2 saved OK")
