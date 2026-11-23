import json

RECORDS = [
    ("083203", "restively", "adv", "/ˈrɛstɪvli/", "bồn chồn; không yên"),
    ("083204", "restocked", "verb", "/ˌriːˈstɑːkt/", "đã nhập thêm hàng"),
    ("083205", "restocking", "verb", "/ˌriːˈstɑːkɪŋ/", "đang nhập thêm hàng"),
    ("083206", "restocks", "verb", "/ˌriːˈstɑːks/", "nhập thêm hàng"),
    ("083207", "restorable", "adj", "/rɪˈstɔːrəbəl/", "có thể khôi phục lại"),
    ("083208", "restorationism", "noun", "/ˌrɛstəˈreɪʃəˌnɪzəm/", "thuyết cứu rỗi phổ quát"),
    ("083209", "restorationist", "noun", "/ˌrɛstəˈreɪʃənɪst/", "người theo thuyết phục hồi"),
    ("083210", "restorations", "noun", "/ˌrɛstəˈreɪʃənz/", "sự phục hồi; sự trùng tu"),
    ("083211", "restored", "verb", "/rɪˈstɔːrd/", "đã khôi phục; đã phục hồi"),
    ("083212", "restores", "verb", "/rɪˈstɔːrz/", "khôi phục; phục hồi"),
    ("083213", "restoril", "noun", "/ˈrɛstərɪl/", "thuốc ngủ Restoril"),
    ("083214", "restoring", "verb", "/rɪˈstɔːrɪŋ/", "đang khôi phục; đang phục hồi"),
    ("083215", "restraining", "verb", "/rɪˈstreɪnɪŋ/", "đang kiềm chế; đang kìm hãm"),
    ("083216", "restrains", "verb", "/rɪˈstreɪnz/", "kiềm chế; kìm hãm"),
    ("083217", "restraints", "noun", "/rɪˈstreɪnts/", "sự kiềm chế; sự ràng buộc"),
    ("083218", "restrengthen", "verb", "/ˌriːˈstrɛŋθən/", "làm mạnh lại; củng cố lại"),
    ("083219", "restrictionism", "noun", "/rɪˈstrɪkʃəˌnɪzəm/", "chính sách hạn chế"),
    ("083220", "restrictionist", "adj", "/rɪˈstrɪkʃənɪst/", "theo chính sách hạn chế"),
    ("083221", "restrictions", "noun", "/rɪˈstrɪkʃənz/", "sự hạn chế; quy định giới hạn"),
    ("083222", "restricts", "verb", "/rɪˈstrɪkts/", "hạn chế; giới hạn"),
    ("083223", "restrike", "noun", "/ˈriːˌstraɪk/", "tiền xu đúc lại từ khuôn cũ"),
    ("083224", "restructured", "verb", "/ˌriːˈstrʌktʃərd/", "đã tái cấu trúc"),
    ("083225", "restructures", "verb", "/ˌriːˈstrʌktʃərz/", "tái cấu trúc"),
    ("083226", "restructuring", "verb", "/ˌriːˈstrʌktʃərɪŋ/", "đang tái cấu trúc"),
    ("083227", "restructurings", "noun", "/ˌriːˈstrʌktʃərɪŋz/", "sự tái cấu trúc"),
    ("083228", "rests", "verb", "/rɛsts/", "nghỉ ngơi; đặt lên"),
    ("083229", "resublime", "verb", "/ˌriːsəˈblaɪm/", "thăng hoa lại"),
    ("083230", "resubmits", "verb", "/ˌriːsəbˈmɪts/", "nộp lại; gửi lại"),
    ("083231", "resubmitted", "verb", "/ˌriːsəbˈmɪtɪd/", "đã nộp lại; đã gửi lại"),
    ("083232", "resubmitting", "verb", "/ˌriːsəbˈmɪtɪŋ/", "đang nộp lại; đang gửi lại"),
    ("083233", "resulted", "verb", "/rɪˈzʌltɪd/", "đã dẫn đến; đã kết quả là"),
    ("083234", "resultful", "adj", "/rɪˈzʌltfəl/", "có kết quả; có hiệu quả"),
    ("083235", "resulting", "adj", "/rɪˈzʌltɪŋ/", "nảy sinh từ đó; kết quả là"),
    ("083236", "results", "verb", "/rɪˈzʌlts/", "dẫn đến; phát sinh từ"),
    ("083237", "resumed", "verb", "/rɪˈzuːmd/", "đã tiếp tục lại"),
    ("083238", "resumes", "verb", "/rɪˈzuːmz/", "tiếp tục lại"),
    ("083239", "resuming", "verb", "/rɪˈzuːmɪŋ/", "đang tiếp tục lại"),
    ("083240", "resummons", "noun", "/ˌriːˈsʌmənz/", "lệnh triệu tập lại"),
    ("083241", "resupinate", "adj", "/rɪˈsuːpɪnət/", "lộn ngược; quay ngược"),
    ("083242", "resupine", "adj", "/ˌrɛsjʊˈpaɪn/", "nằm ngửa; ngửa mặt lên"),
    ("083243", "resupplied", "verb", "/ˌriːsəˈplaɪd/", "đã tiếp tế lại; đã cung cấp lại"),
    ("083244", "resupplies", "verb", "/ˌriːsəˈplaɪz/", "tiếp tế lại; cung cấp lại"),
    ("083245", "resupply", "verb", "/ˌriːsəˈplaɪ/", "tiếp tế lại; cung cấp lại"),
    ("083246", "resupplying", "verb", "/ˌriːsəˈplaɪɪŋ/", "đang tiếp tế lại; đang cung cấp"),
    ("083247", "resurfaced", "verb", "/ˌriːˈsɜːrfɪst/", "đã nổi lên lại; đã trải mặt lại"),
    ("083248", "resurfaces", "verb", "/ˌriːˈsɜːrfɪsɪz/", "nổi lên lại; trải mặt lại"),
    ("083249", "resurfacing", "verb", "/ˌriːˈsɜːrfɪsɪŋ/", "đang nổi lên lại"),
    ("083250", "resurrected", "verb", "/ˌrɛzəˈrɛktɪd/", "đã hồi sinh; đã phục sinh"),
    ("083251", "resurrecting", "verb", "/ˌrɛzəˈrɛktɪŋ/", "đang hồi sinh; đang phục sinh"),
    ("083252", "resurrectionary", "adj", "/ˌrɛzəˈrɛkʃəˌnɛri/", "thuộc sự phục sinh; đào trộm mộ"),
    ("083253", "resurrectionist", "noun", "/ˌrɛzəˈrɛkʃənɪst/", "kẻ đào trộm xác chết"),
    ("083254", "resurrects", "verb", "/ˌrɛzəˈrɛkts/", "làm sống lại; phục sinh"),
    ("083255", "resuscitates", "verb", "/rɪˈsʌsɪˌteɪts/", "hồi sức; làm sống lại"),
    ("083256", "resuscitating", "verb", "/rɪˈsʌsɪˌteɪtɪŋ/", "đang hồi sức; đang làm sống lại"),
    ("083257", "resuscitative", "adj", "/rɪˈsʌsɪˌteɪtɪv/", "có tác dụng hồi sức; phục hồi"),
    ("083258", "resuspend", "verb", "/ˌriːsəˈspɛnd/", "đưa lại dạng huyền phù"),
    ("083259", "reswitching", "noun", "/ˌriːˈswɪtʃɪŋ/", "sự chuyển mạch lại"),
    ("083260", "resynthesis", "noun", "/ˌriːˈsɪnθəsɪs/", "sự tổng hợp lại"),
    ("083261", "retable", "noun", "/rɪˈteɪbəl/", "vách trang trí sau bàn thờ"),
    ("083262", "retailed", "verb", "/ˈriːteɪld/", "đã bán lẻ"),
    ("083263", "retailers", "noun", "/ˈriːˌteɪlərz/", "nhà bán lẻ"),
    ("083264", "retails", "verb", "/ˈriːteɪlz/", "bán lẻ"),
    ("083265", "retaining", "verb", "/rɪˈteɪnɪŋ/", "đang giữ lại"),
    ("083266", "retains", "verb", "/rɪˈteɪnz/", "giữ lại; duy trì"),
    ("083267", "retaken", "verb", "/ˌriːˈteɪkən/", "đã chiếm lại; đã chụp lại"),
    ("083268", "retaliated", "verb", "/rɪˈtæliˌeɪtɪd/", "đã trả đũa; đã trả thù"),
    ("083269", "retaliates", "verb", "/rɪˈtæliˌeɪts/", "trả đũa; trả thù"),
    ("083270", "retaliating", "verb", "/rɪˈtæliˌeɪtɪŋ/", "đang trả đũa; đang trả thù"),
    ("083271", "retaliative", "adj", "/rɪˈtæliˌeɪtɪv/", "có tính trả đũa; báo thù"),
    ("083272", "retaliator", "noun", "/rɪˈtæliˌeɪtər/", "người trả đũa; kẻ báo thù"),
    ("083273", "retannage", "noun", "/ˌriːˈtænɪdʒ/", "sự thuộc da lại"),
    ("083274", "retantion", "noun", "/rɪˈtɛnʃən/", "sự giữ lại"),
    ("083275", "retapering", "noun", "/ˌriːˈteɪpərɪŋ/", "sự vót thuôn lại"),
    ("083276", "retardate", "noun", "/rɪˈtɑːrdeɪt/", "người chậm phát triển trí tuệ"),
    ("083277", "retardative", "adj", "/rɪˈtɑːrdətɪv/", "làm chậm trễ; hãm lại"),
    ("083278", "retardatory", "adj", "/rɪˈtɑːrdəˌtɔːri/", "làm chậm lại; kìm hãm"),
    ("083279", "retardent", "noun", "/rɪˈtɑːrdənt/", "chất làm chậm; chất ức chế"),
    ("083280", "retarder", "noun", "/rɪˈtɑːrdər/", "chất làm chậm; bộ hãm"),
    ("083281", "retarding", "verb", "/rɪˈtɑːrdɪŋ/", "đang làm chậm lại; cản trở"),
    ("083282", "retardment", "noun", "/rɪˈtɑːrdmənt/", "sự chậm trễ; sự trì hoãn"),
    ("083283", "retards", "verb", "/rɪˈtɑːrdz/", "làm chậm lại; kìm hãm"),
    ("083284", "retched", "verb", "/rɛtʃt/", "đã nôn khan; đã ọe"),
    ("083285", "retches", "verb", "/ˈrɛtʃɪz/", "nôn khan; ọe"),
    ("083286", "retching", "verb", "/ˈrɛtʃɪŋ/", "đang nôn khan; đang ọe"),
    ("083287", "retd", "adj", "/rɪˈtaɪərd/", "đã nghỉ hưu (viết tắt)"),
    ("083288", "retecious", "adj", "/rɪˈtiːʃəs/", "dạng mạng lưới"),
    ("083289", "retelling", "noun", "/ˌriːˈtɛlɪŋ/", "bản kể lại mới; sự thuật lại"),
    ("083290", "retem", "noun", "/ˈrɛtəm/", "cây bụi sa mạc Retama"),
    ("083291", "retemper", "verb", "/ˌriːˈtɛmpər/", "tôi lại thép; trộn lại"),
    ("083292", "retentions", "noun", "/rɪˈtɛnʃənz/", "sự giữ lại; khoản tiền giữ lại"),
    ("083293", "retentively", "adv", "/rɪˈtɛntɪvli/", "nhớ lâu; giữ chặt"),
    ("083294", "retentiveness", "noun", "/rɪˈtɛntɪvnəs/", "khả năng ghi nhớ tốt; độ bền"),
    ("083295", "retentivity", "noun", "/ˌriːtɛnˈtɪvɪti/", "độ từ dư; khả năng ghi nhớ"),
    ("083296", "retenue", "noun", "/rəˈtɛnjuː/", "sự tự kiềm chế; sự dè dặt"),
    ("083297", "rethought", "verb", "/ˌriːˈθɔːt/", "đã suy nghĩ lại"),
    ("083298", "rethrash", "verb", "/ˌriːˈθræʃ/", "đập lúa lại; bàn lại vấn đề cũ"),
    ("083299", "rethread", "verb", "/ˌriːˈθrɛd/", "xâu chỉ lại; tiện lại ren"),
    ("083300", "retia", "noun", "/ˈriːʃə/", "mạng lưới; đám rối mạch"),
    ("083301", "retiari", "noun", "/rɪˈtiːəriː/", "đấu sĩ quăng lưới (La Mã)"),
    ("083302", "retiarius", "noun", "/ˌrɛʃiˈɛriəs/", "đấu sĩ quăng lưới (La Mã)"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r07_raw_p3.json"))
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

json.dump(out, open("scratch/b37_r07_reviewed_p3.json", "w"), ensure_ascii=False, indent=2)
print("b37_r07_p3 saved OK")
