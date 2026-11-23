import json

RECORDS = [
    ("083303", "retiary", "adj", "/ˈriːtiˌɛri/", "hình lưới; thuộc lưới"),
    ("083304", "reticently", "adv", "/ˈrɛtɪsəntli/", "một cách dè dặt; ít nói"),
    ("083305", "retick", "verb", "/ˌriːˈtɪk/", "bọc lại áo đệm; đánh dấu lại"),
    ("083306", "reticula", "noun", "/rɪˈtɪkjələ/", "màng lưới; dạ tổ ong"),
    ("083307", "reticulated", "adj", "/rɪˈtɪkjəˌleɪtɪd/", "có hình mắt lưới"),
    ("083308", "reticulin", "noun", "/rɪˈtɪkjəlɪn/", "chất lưới reticulin"),
    ("083309", "reticulitermes", "noun", "/rɪˌtɪkjəlɪˈtɜːrmiːz/", "chi mối Reticulitermes"),
    ("083310", "reticulopodia", "noun", "/rɪˌtɪkjəloʊˈpoʊdiə/", "chân giả hình lưới"),
    ("083311", "retiform", "adj", "/ˈrɛtɪˌfɔːrm/", "hình mạng lưới"),
    ("083312", "retiling", "noun", "/ˌriːˈtaɪlɪŋ/", "sự lợp ngói lại; sự lát gạch lại"),
    ("083313", "retimber", "verb", "/ˌriːˈtɪmbər/", "chống gỗ lại hầm lò; trồng rừng"),
    ("083314", "retime", "verb", "/ˌriːˈtaɪm/", "chỉnh lại thời điểm; định giờ lại"),
    ("083315", "retinacula", "noun", "/ˌrɛtɪˈnækjələ/", "hãm gân; móc giữ cánh"),
    ("083316", "retinaculum", "noun", "/ˌrɛtɪˈnækjələm/", "hãm gân; móc cánh côn trùng"),
    ("083317", "retinae", "noun", "/ˈrɛtɪˌniː/", "võng mạc; màng lưới mắt"),
    ("083318", "retinalla", "noun", "/ˌrɛtɪˈnɛlə/", "lưới tơ thần kinh"),
    ("083319", "retinene", "noun", "/ˈrɛtɪˌniːn/", "chất sắc tố võng mạc retinen"),
    ("083320", "retinerved", "adj", "/ˈrɛtɪˌnɜːrvd/", "có gân lá dạng mạng lưới"),
    ("083321", "retinoid", "noun", "/ˈrɛtɪˌnɔɪd/", "dẫn xuất vitamin A retinoid"),
    ("083322", "retinophore", "noun", "/rɪˈtɪnəˌfɔːr/", "tế bào võng mạc côn trùng"),
    ("083323", "retinoscope", "noun", "/ˈrɛtɪnəˌskoʊp/", "kính soi bóng đồng tử"),
    ("083324", "retinoscopy", "noun", "/ˌrɛtɪˈnɑːskəpi/", "phép soi bóng đồng tử"),
    ("083325", "retinosis", "noun", "/ˌrɛtɪˈnoʊsɪs/", "bệnh thoái hóa võng mạc"),
    ("083326", "retirements", "noun", "/rɪˈtaɪərmənts/", "sự nghỉ hưu; tiền lương hưu"),
    ("083327", "retires", "verb", "/rɪˈtaɪərz/", "nghỉ hưu; rút lui"),
    ("083328", "retisolution", "noun", "/ˌrɛtɪsəˈluːʃən/", "sự hòa tan thể Golgi"),
    ("083329", "retispersion", "noun", "/ˌrɛtɪˈspɜːrʒən/", "sự phân tán thể Golgi"),
    ("083330", "retold", "verb", "/ˌriːˈtoʊld/", "đã kể lại; đã thuật lại"),
    ("083331", "retook", "verb", "/ˌriːˈtʊk/", "đã chiếm lại; đã chụp lại"),
    ("083332", "retooled", "verb", "/ˌriːˈtuːld/", "đã cải tiến thiết bị; tái tổ chức"),
    ("083333", "retooling", "verb", "/ˌriːˈtuːlɪŋ/", "đang cải tiến; đang tái tổ chức"),
    ("083334", "retools", "verb", "/ˌriːˈtuːlz/", "cải tiến máy móc; tái tổ chức"),
    ("083335", "retorted", "verb", "/rɪˈtɔːrtɪd/", "đã đáp trả; đã vặn lại"),
    ("083336", "retorting", "verb", "/rɪˈtɔːrtɪŋ/", "đang đáp trả; đang vặn lại"),
    ("083337", "retortion", "noun", "/rɪˈtɔːrʃən/", "sự bẻ ngược lại; sự trả đũa"),
    ("083338", "retorts", "verb", "/rɪˈtɔːrts/", "đáp trả; vặn lại"),
    ("083339", "retoucher", "noun", "/ˌriːˈtʌtʃər/", "người chỉnh sửa ảnh"),
    ("083340", "retraced", "verb", "/rɪˈtreɪst/", "đã lần ngược lại; đã vẽ lại"),
    ("083341", "retraces", "verb", "/rɪˈtreɪsɪz/", "lần ngược lại; vẽ lại"),
    ("083342", "retracing", "verb", "/rɪˈtreɪsɪŋ/", "đang lần ngược lại; đang vẽ lại"),
    ("083343", "retractation", "noun", "/ˌriːtrækˈteɪʃən/", "sự rút lại lời; sự hủy bỏ"),
    ("083344", "retractations", "noun", "/ˌriːtrækˈteɪʃənz/", "lời rút lại; sự hủy bỏ"),
    ("083345", "retractility", "noun", "/rɪˌtræktɪˈlɪti/", "tính co rút được"),
    ("083346", "retracting", "verb", "/rɪˈtræktɪŋ/", "đang rút lại; đang thu vào"),
    ("083347", "retractors", "noun", "/rɪˈtræktərz/", "banh phẫu thuật; cơ kéo lùi"),
    ("083348", "retracts", "verb", "/rɪˈtrækts/", "rút lại; thu vào"),
    ("083349", "retral", "adj", "/ˈriːtrəl/", "hướng về phía sau; ở phía sau"),
    ("083350", "retransfer", "verb", "/ˌriːtrænsˈfɜːr/", "chuyển lại; dời lại"),
    ("083351", "retransform", "verb", "/ˌriːtrænsˈfɔːrm/", "biến đổi lại"),
    ("083352", "retranslation", "noun", "/ˌriːtrænsˈleɪʃən/", "sự dịch lại; bản dịch lại"),
    ("083353", "retranslocation", "noun", "/ˌriːtrænsloʊˈkeɪʃən/", "sự chuyển vị lại"),
    ("083354", "retransmission", "noun", "/ˌriːtrænsˈmɪʃən/", "sự truyền lại; sự phát lại"),
    ("083355", "retransmiter", "noun", "/ˌriːtrænsˈmɪtər/", "máy tiếp phát; máy phát lại"),
    ("083356", "retransmits", "verb", "/ˌriːtrænsˈmɪts/", "truyền lại; phát lại"),
    ("083357", "retransmitted", "verb", "/ˌriːtrænsˈmɪtɪd/", "đã truyền lại; đã phát lại"),
    ("083358", "retransmitting", "verb", "/ˌriːtrænsˈmɪtɪŋ/", "đang truyền lại; đang phát lại"),
    ("083359", "retreaded", "verb", "/ˌriːˈtrɛdɪd/", "đã đắp lại lốp xe"),
    ("083360", "retreader", "noun", "/ˌriːˈtrɛdər/", "khuôn đắp lại lốp xe"),
    ("083361", "retreading", "verb", "/ˌriːˈtrɛdɪŋ/", "đang đắp lại lốp xe"),
    ("083362", "retreads", "verb", "/ˌriːˈtrɛdz/", "đắp lại lốp xe"),
    ("083363", "retreatant", "noun", "/rɪˈtriːtənt/", "người tham gia tĩnh tâm"),
    ("083364", "retreating", "verb", "/rɪˈtriːtɪŋ/", "đang rút lui; đang thoái lui"),
    ("083365", "retreats", "verb", "/rɪˈtriːts/", "rút lui; thoái lui"),
    ("083366", "retree", "noun", "/ˈriːtriː/", "giấy thứ phẩm; giấy lỗi nhẹ"),
    ("083367", "retrenched", "verb", "/rɪˈtrɛntʃt/", "đã cắt giảm chi tiêu"),
    ("083368", "retrenches", "verb", "/rɪˈtrɛntʃɪz/", "cắt giảm chi tiêu"),
    ("083369", "retrenching", "verb", "/rɪˈtrɛntʃɪŋ/", "đang cắt giảm chi tiêu"),
    ("083370", "retributory", "adj", "/rɪˈtrɪbjəˌtɔːri/", "mang tính trừng phạt; báo ứng"),
    ("083371", "retried", "verb", "/ˌriːˈtraɪd/", "đã xử lại; đã thử lại"),
    ("083372", "retrieved", "verb", "/rɪˈtriːvd/", "đã lấy lại; đã truy xuất"),
    ("083373", "retrieves", "verb", "/rɪˈtriːvz/", "lấy lại; truy xuất"),
    ("083374", "retrieving", "verb", "/rɪˈtriːvɪŋ/", "đang lấy lại; đang truy xuất"),
    ("083375", "retrimming", "verb", "/ˌriːˈtrɪmɪŋ/", "đang cắt tỉa lại; đang chỉnh lại"),
    ("083376", "retroact", "verb", "/ˌrɛtroʊˈækt/", "tác động ngược; có hiệu lực hồi tố"),
    ("083377", "retroacted", "verb", "/ˌrɛtroʊˈæktɪd/", "đã tác động ngược; đã hồi tố"),
    ("083378", "retroacting", "verb", "/ˌrɛtroʊˈæktɪŋ/", "đang tác động ngược"),
    ("083379", "retroaction", "noun", "/ˌrɛtroʊˈækʃən/", "tác động ngược; phản tác dụng"),
    ("083380", "retroactivity", "noun", "/ˌrɛtroʊækˈtɪvɪti/", "tính hồi tố"),
    ("083381", "retroacts", "verb", "/ˌrɛtroʊˈækts/", "tác động ngược; có hiệu lực hồi tố"),
    ("083382", "retrobuccal", "adj", "/ˌrɛtroʊˈbʌkəl/", "ở sau khoang miệng"),
    ("083383", "retrobulbar", "adj", "/ˌrɛtroʊˈbʌlbər/", "ở sau nhãn cầu"),
    ("083384", "retrocaecal", "adj", "/ˌrɛtroʊˈsiːkəl/", "ở sau manh tràng"),
    ("083385", "retrocede", "verb", "/ˌrɛtrəˈsiːd/", "lùi lại; nhượng trả lại"),
    ("083386", "retrocedence", "noun", "/ˌrɛtrəˈsiːdəns/", "sự lùi lại; sự nhượng trả lại"),
    ("083387", "retrocedent", "adj", "/ˌrɛtrəˈsiːdənt/", "lùi lại; lặn vào trong"),
    ("083388", "retrocerebral", "adj", "/ˌrɛtroʊˈsɛrəbrəl/", "ở sau não"),
    ("083389", "retrocervical", "adj", "/ˌrɛtroʊˈsɜːrvɪkəl/", "ở sau cổ tử cung"),
    ("083390", "retrocession", "noun", "/ˌrɛtrəˈsɛʃən/", "sự thoái lui; sự nhượng trả lại"),
    ("083391", "retrocessive", "adj", "/ˌrɛtrəˈsɛsɪv/", "lùi lại; thụt lùi"),
    ("083392", "retrochoir", "noun", "/ˈrɛtroʊˌkwaɪər/", "gian sau hậu cung nhà thờ"),
    ("083393", "retrocollic", "adj", "/ˌrɛtroʊˈkɑːlɪk/", "ở sau cổ; gáy"),
    ("083394", "retrocurved", "adj", "/ˌrɛtroʊˈkɜːrvd/", "cong ngược ra sau"),
    ("083395", "retrod", "verb", "/ˌriːˈtrɑːd/", "đã giẫm lại; đã đi lại"),
    ("083396", "retrodden", "verb", "/ˌriːˈtrɑːdən/", "đã giẫm lại; đã đi lại"),
    ("083397", "retrodeviation", "noun", "/ˌrɛtroʊˌdiːviˈeɪʃən/", "sự lệch ngả ra sau"),
    ("083398", "retroes", "noun", "/ˈrɛtroʊz/", "phong cách hoài cổ"),
    ("083399", "retrofits", "verb", "/ˈrɛtroʊˌfɪts/", "trang bị thêm; cải tạo"),
    ("083400", "retrofitted", "verb", "/ˈrɛtroʊˌfɪtɪd/", "đã trang bị thêm; đã cải tạo"),
    ("083401", "retrofitting", "verb", "/ˈrɛtroʊˌfɪtɪŋ/", "đang trang bị thêm; đang cải tạo"),
    ("083402", "retrofixation", "noun", "/ˌrɛtroʊfɪkˈseɪʃən/", "sự cố định ngả sau"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r07_raw_p4.json"))
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

json.dump(out, open("scratch/b37_r07_reviewed_p4.json", "w"), ensure_ascii=False, indent=2)
print("b37_r07_p4 saved OK")
