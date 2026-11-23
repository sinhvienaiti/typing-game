import json

RECORDS = [
    ("083803", "rights", "verb", "/raɪts/", "dựng thẳng lại; sửa chữa sai lầm"),
    ("083804", "rightwards", "adv", "/ˈraɪtwərdz/", "hướng về phía bên phải"),
    ("083805", "rigidification", "noun", "/rɪˌdʒɪdɪfɪˈkeɪʃən/", "sự làm cứng lại; sự cứng nhắc hóa"),
    ("083806", "rigidify", "verb", "/rɪˈdʒɪdɪˌfaɪ/", "làm cứng lại; trở nên cứng nhắc"),
    ("083807", "rigidifying", "noun", "/rɪˈdʒɪdɪˌfaɪɪŋ/", "sự làm cứng lại"),
    ("083808", "rigidities", "noun", "/rɪˈdʒɪdɪtiz/", "độ cứng; tính cứng nhắc"),
    ("083809", "rigil", "noun", "/ˈraɪdʒəl/", "sao Rigil Kentaurus"),
    ("083810", "rigorism", "noun", "/ˈrɪɡəˌrɪzəm/", "chủ nghĩa nghiêm khắc khắt khe"),
    ("083811", "rigourousness", "noun", "/ˈrɪɡərəsnəs/", "tính nghiêm ngặt; sự khắc nghiệt"),
    ("083812", "rigout", "noun", "/ˈrɪɡˌaʊt/", "bộ quần áo diện kỳ quặc"),
    ("083813", "rigs", "verb", "/rɪɡz/", "lắp đặt; gian lận kết quả"),
    ("083814", "rijstafel", "noun", "/ˈraɪstɑːfəl/", "món cơm bàn kiểu Indonesia Hà Lan"),
    ("083815", "rijstaffel", "noun", "/ˈraɪstɑːfəl/", "món cơm bàn kiểu Indonesia Hà Lan"),
    ("083816", "rijsttaffel", "noun", "/ˈraɪstɑːfəl/", "món cơm bàn kiểu Indonesia Hà Lan"),
    ("083817", "riker", "noun", "/ˈraɪkər/", "hộp trưng bày mẫu vật Riker"),
    ("083818", "riksmaal", "noun", "/ˈrɪksmɔːl/", "tiếng Na Uy chuẩn Riksmål"),
    ("083819", "riksmal", "noun", "/ˈrɪksmɔːl/", "tiếng Na Uy chuẩn Riksmål"),
    ("083820", "riles", "verb", "/raɪlz/", "làm bực mình; khuấy đục"),
    ("083821", "riling", "verb", "/ˈraɪlɪŋ/", "đang làm bực mình; đang khuấy đục"),
    ("083822", "rilled", "verb", "/rɪld/", "đã tạo rãnh xói; chảy thành suối"),
    ("083823", "rillet", "noun", "/ˈrɪlɪt/", "dòng suối nhỏ"),
    ("083824", "rilling", "verb", "/ˈrɪlɪŋ/", "đang chảy thành rãnh nhỏ"),
    ("083825", "rills", "verb", "/rɪlz/", "chảy thành dòng suối nhỏ"),
    ("083826", "rimactane", "noun", "/rɪˈmækteɪn/", "thuốc kháng lao Rimactane"),
    ("083827", "rimeless", "adj", "/ˈraɪmləs/", "không vần; không có vần điệu"),
    ("083828", "rimer", "noun", "/ˈraɪmər/", "mũi doa lỗ; người làm thơ tồi"),
    ("083829", "rimers", "noun", "/ˈraɪmərz/", "mũi doa lỗ; người làm thơ tồi"),
    ("083830", "rimes", "verb", "/raɪmz/", "gieo vần; phủ sương muối"),
    ("083831", "riming", "adj", "/ˈraɪmɪŋ/", "có vần điệu; hợp vần"),
    ("083832", "rimmer", "noun", "/ˈrɪmər/", "thép sôi; dụng cụ cắt mép bánh"),
    ("083833", "rimming", "verb", "/ˈrɪmɪŋ/", "đang viền mép; đang tạo vành"),
    ("083834", "rimose", "adj", "/ˈraɪmoʊs/", "nứt nẻ; có nhiều kẽ nứt"),
    ("083835", "rimous", "adj", "/ˈraɪməs/", "đầy vết nứt nẻ"),
    ("083836", "rims", "verb", "/rɪmz/", "viền mép; tạo vành quanh"),
    ("083837", "rimy", "adj", "/ˈraɪmi/", "phủ đầy sương muối"),
    ("083838", "rincon", "noun", "/rɪŋˈkoʊn/", "góc hẻm núi; khoảnh đất lõm"),
    ("083839", "rinded", "adj", "/ˈraɪndɪd/", "có vỏ ngoài; có cùi"),
    ("083840", "rinding", "verb", "/ˈraɪndɪŋ/", "đang bóc vỏ"),
    ("083841", "rinds", "verb", "/raɪndz/", "bóc vỏ; lột vỏ"),
    ("083842", "ringdove", "noun", "/ˈrɪŋˌdʌv/", "chim bồ câu gỗ cổ vòng"),
    ("083843", "ringent", "adj", "/ˈrɪndʒənt/", "há rộng hai môi (tràng hoa)"),
    ("083844", "ringers", "noun", "/ˈrɪŋərz/", "người rung chuông; ngựa tráo tên"),
    ("083845", "ringhals", "noun", "/ˈrɪŋhæls/", "rắn hổ mang phun nọc Nam Phi"),
    ("083846", "ringleted", "adj", "/ˈrɪŋlɪtɪd/", "uốn lọn xoăn tít (tóc)"),
    ("083847", "ringlety", "adj", "/ˈrɪŋlɪti/", "xoăn thành từng lọn"),
    ("083848", "ringlike", "adj", "/ˈrɪŋˌlaɪk/", "hình nhẫn; dạng vòng tròn"),
    ("083849", "ringoid", "adj", "/ˈrɪŋɡɔɪd/", "dạng vòng; giống chiếc nhẫn"),
    ("083850", "ringspot", "noun", "/ˈrɪŋˌspɑːt/", "bệnh đốm vòng ở thực vật"),
    ("083851", "ringstone", "noun", "/ˈrɪŋˌstoʊn/", "đá xây vòm cung"),
    ("083852", "ringtone", "noun", "/ˈrɪŋˌtoʊn/", "nhạc chuông điện thoại"),
    ("083853", "ringtones", "noun", "/ˈrɪŋˌtoʊnz/", "nhạc chuông điện thoại"),
    ("083854", "rinked", "verb", "/rɪŋkt/", "đã trượt băng trên sân"),
    ("083855", "rinkhals", "noun", "/ˈrɪŋkhæls/", "rắn hổ mang phun nọc Nam Phi"),
    ("083856", "rinking", "verb", "/ˈrɪŋkɪŋ/", "đang trượt băng trên sân"),
    ("083857", "rinks", "verb", "/rɪŋks/", "trượt băng trên sân"),
    ("083858", "rinsed", "verb", "/rɪnst/", "đã súc; đã tráng nước"),
    ("083859", "rinser", "noun", "/ˈrɪnsər/", "máy tráng rửa; vòi tráng"),
    ("083860", "rinses", "verb", "/ˈrɪnsɪz/", "súc; tráng nước"),
    ("083861", "rioted", "verb", "/ˈraɪətɪd/", "đã gây bạo loạn"),
    ("083862", "riotousness", "noun", "/ˈraɪətəsnəs/", "sự náo loạn; tính phóng túng"),
    ("083863", "riots", "verb", "/ˈraɪəts/", "gây bạo loạn"),
    ("083864", "riped", "verb", "/raɪpt/", "đã chín (hoa quả)"),
    ("083865", "ripens", "verb", "/ˈraɪpənz/", "làm chín; chín muồi"),
    ("083866", "ripes", "verb", "/raɪps/", "chín (quả)"),
    ("083867", "ripicolous", "adj", "/raɪˈpɪkələs/", "sống ở ven bờ sông"),
    ("083868", "riping", "verb", "/ˈraɪpɪŋ/", "đang chín dần"),
    ("083869", "riposted", "verb", "/rɪˈpoʊstɪd/", "đã đáp trả sắc bén"),
    ("083870", "ripostes", "verb", "/rɪˈpoʊsts/", "đáp trả sắc bén"),
    ("083871", "riposting", "verb", "/rɪˈpoʊstɪŋ/", "đang đáp trả sắc bén"),
    ("083872", "rippers", "noun", "/ˈrɪpərz/", "dụng cụ xé; lưỡi cày xới sâu"),
    ("083873", "ripples", "verb", "/ˈrɪpəlz/", "gợn sóng lăn tăn"),
    ("083874", "ripply", "adj", "/ˈrɪpli/", "gợn sóng lăn tăn"),
    ("083875", "riprap", "noun", "/ˈrɪpˌræp/", "đá hộc lát kè bờ"),
    ("083876", "risibility", "noun", "/ˌrɪzəˈbɪlɪti/", "tính hay cười; khiếu hài hước"),
    ("083877", "risked", "verb", "/rɪskt/", "đã liều lĩnh; đã mạo hiểm"),
    ("083878", "riskily", "adv", "/ˈrɪskɪli/", "một cách mạo hiểm; liều lĩnh"),
    ("083879", "risking", "verb", "/ˈrɪskɪŋ/", "đang liều lĩnh; đang mạo hiểm"),
    ("083880", "riskish", "adj", "/ˈrɪskɪʃ/", "hơi mạo hiểm; hơi rủi ro"),
    ("083881", "risklessness", "noun", "/ˈrɪskləsnəs/", "sự không có rủi ro; sự an toàn"),
    ("083882", "risks", "verb", "/rɪsks/", "liều lĩnh; đánh cược"),
    ("083883", "risorgimento", "noun", "/rɪˌsɔːrdʒɪˈmɛntoʊ/", "phong trào thống nhất nước Ý"),
    ("083884", "risottos", "noun", "/rɪˈzɑːtoʊz/", "món cơm Ý risotto"),
    ("083885", "rissole", "noun", "/ˈrɪsoʊl/", "chả viên chiên giòn bọc bột"),
    ("083886", "ritard", "noun", "/rɪˈtɑːrd/", "nhịp chậm dần (âm nhạc)"),
    ("083887", "ritenuto", "adj", "/ˌrɪtəˈnuːtoʊ/", "chậm đột ngột (âm nhạc)"),
    ("083888", "ritornallo", "noun", "/ˌrɪtɔːrˈnɛloʊ/", "đoạn nhạc dạo lặp lại"),
    ("083889", "ritualise", "verb", "/ˈrɪtʃuəˌlaɪz/", "nghi thức hóa"),
    ("083890", "ritualize", "verb", "/ˈrɪtʃuəˌlaɪz/", "nghi thức hóa"),
    ("083891", "rituals", "noun", "/ˈrɪtʃuəlz/", "nghi lễ; thói quen cố định"),
    ("083892", "rivage", "noun", "/ˈrɪvɪdʒ/", "bờ sông; bờ biển"),
    ("083893", "rivalled", "verb", "/ˈraɪvəld/", "đã cạnh tranh; đã sánh ngang"),
    ("083894", "rivalling", "verb", "/ˈraɪvəlɪŋ/", "đang cạnh tranh; đang sánh ngang"),
    ("083895", "rivals", "verb", "/ˈraɪvəlz/", "cạnh tranh; sánh ngang"),
    ("083896", "rivalship", "noun", "/ˈraɪvəlˌʃɪp/", "sự kình địch; sự cạnh tranh"),
    ("083897", "rived", "verb", "/raɪvd/", "đã xé toạc; đã chẻ ra"),
    ("083898", "riven", "verb", "/ˈrɪvən/", "bị xé toạc; bị chia rẽ sâu sắc"),
    ("083899", "rivenbark", "noun", "/ˈrɪvənbɑːrk/", "tên họ Rivenbark"),
    ("083900", "rivenbarks", "noun", "/ˈrɪvənbɑːrks/", "gia đình họ Rivenbark"),
    ("083901", "riverain", "adj", "/ˈrɪvəreɪn/", "ven sông; ở bên bờ sông"),
    ("083902", "rivered", "adj", "/ˈrɪvərd/", "có nhiều sông ngòi"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r08_raw_p4.json"))
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

json.dump(out, open("scratch/b37_r08_reviewed_p4.json", "w"), ensure_ascii=False, indent=2)
print("b37_r08_p4 saved OK")
