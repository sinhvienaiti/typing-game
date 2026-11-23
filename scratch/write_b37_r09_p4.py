import json

RECORDS = [
    ("084303", "ruggelach", "noun", "/ˈrʊɡəˌlɑːx/", "bánh sừng bò nhân mứt Do Thái"),
    ("084304", "rugosity", "noun", "/ruːˈɡɑːsɪti/", "tình trạng nhăn nheo; độ gồ ghề"),
    ("084305", "rugous", "adj", "/ˈruːɡəs/", "nhăn nheo; gồ ghề"),
    ("084306", "rugulah", "noun", "/ˈrʊɡəˌlɑː/", "bánh ngọt cuộn nhân Do Thái"),
    ("084307", "rugulose", "adj", "/ˈruːɡjəˌloʊs/", "hơi nhăn nheo"),
    ("084308", "ruinate", "verb", "/ˈruːəˌneɪt/", "hủy hoại; tàn phá"),
    ("084309", "ruing", "verb", "/ˈruːɪŋ/", "đang hối tiếc; đang ân hận"),
    ("084310", "ruins", "verb", "/ˈruːɪnz/", "phá hủy hoàn toàn; làm hỏng"),
    ("084311", "rulable", "adj", "/ˈruːləbəl/", "có thể cai quản; có thể kẻ dòng"),
    ("084312", "ruleless", "adj", "/ˈruːlləs/", "vô nguyên tắc; không theo quy tắc"),
    ("084313", "rulers", "noun", "/ˈruːlərz/", "người cai trị; cây thước kẻ"),
    ("084314", "rulerships", "noun", "/ˈruːlərˌʃɪps/", "quyền cai trị; ngôi vị thống trị"),
    ("084315", "rules", "verb", "/ruːlz/", "cai trị; phán quyết; kẻ dòng"),
    ("084316", "rulley", "noun", "/ˈrʌli/", "xe bò kéo bốn bánh"),
    ("084317", "rumansh", "adj", "/ruːˈmɑːnʃ/", "thuộc tiếng Romansh (Thụy Sĩ)"),
    ("084318", "rumbled", "verb", "/ˈrʌmbəld/", "đã gầm ầm ầm; đã phát giác"),
    ("084319", "rumbler", "noun", "/ˈrʌmblər/", "thùng quay đánh bóng; người kêu ca"),
    ("084320", "rumbles", "verb", "/ˈrʌmbəlz/", "gầm vang ầm ầm; phát hiện ra"),
    ("084321", "ruminantia", "noun", "/ˌruːmɪˈnænʃə/", "phân bộ Động vật nhai lại"),
    ("084322", "ruminants", "noun", "/ˈruːmɪnənts/", "động vật nhai lại; người trầm tư"),
    ("084323", "ruminated", "verb", "/ˈruːməˌneɪtɪd/", "đã nhai lại; đã ngẫm nghĩ kỹ"),
    ("084324", "ruminates", "verb", "/ˈruːməˌneɪts/", "nhai lại; ngẫm nghĩ kỹ"),
    ("084325", "ruminating", "verb", "/ˈruːməˌneɪtɪŋ/", "đang nhai lại; đang ngẫm nghĩ"),
    ("084326", "ruminatively", "adv", "/ˈruːmɪnətɪvli/", "trầm ngâm suy tư"),
    ("084327", "ruminator", "noun", "/ˈruːməˌneɪtər/", "người trầm tư; người suy ngẫm"),
    ("084328", "rummaged", "verb", "/ˈrʌmɪdʒd/", "đã lục tung; đã lục soát"),
    ("084329", "rummages", "verb", "/ˈrʌmɪdʒɪz/", "lục tung; lục soát"),
    ("084330", "rummaging", "verb", "/ˈrʌmɪdʒɪŋ/", "đang lục tung; đang lục soát"),
    ("084331", "rumminess", "noun", "/ˈrʌminəs/", "tính kỳ quặc; vẻ lập dị"),
    ("084332", "rumness", "noun", "/ˈrʌmnəs/", "tính kỳ quặc; sự lập dị"),
    ("084333", "rumohra", "noun", "/ruːˈmɔːrə/", "chi dương xỉ lá da Rumohra"),
    ("084334", "rumored", "adj", "/ˈruːmərd/", "bị đồn đại; theo lời đồn"),
    ("084335", "rumormonger", "noun", "/ˈruːmərˌmʌŋɡər/", "kẻ chuyên phao tin đồn nhảm"),
    ("084336", "rumormongering", "noun", "/ˈruːmərˌmʌŋɡərɪŋ/", "hành vi phao tin đồn nhảm"),
    ("084337", "rumoured", "verb", "/ˈruːmərd/", "đã đồn đại; đã phao tin"),
    ("084338", "rumouring", "verb", "/ˈruːmərɪŋ/", "đang đồn đại; đang phao tin"),
    ("084339", "rumourmonger", "noun", "/ˈruːmərˌmʌŋɡər/", "kẻ chuyên phao tin đồn nhảm"),
    ("084340", "rumours", "verb", "/ˈruːmərz/", "đồn đại; phao tin"),
    ("084341", "rumples", "verb", "/ˈrʌmpəlz/", "làm nhăn; vò nhàu"),
    ("084342", "rumpling", "verb", "/ˈrʌmplɪŋ/", "đang làm nhăn; đang vò nhàu"),
    ("084343", "rumrunner", "noun", "/ˈrʌmˌrʌnər/", "kẻ buôn lậu rượu"),
    ("084344", "runagate", "noun", "/ˈrʌnəˌɡeɪt/", "kẻ trốn chạy; người sống lang thang"),
    ("084345", "runaround", "noun", "/ˈrʌnəˌraʊnd/", "sự thoái thác lòng vòng"),
    ("084346", "runch", "noun", "/rʌntʃ/", "cây củ cải dại"),
    ("084347", "runcinate", "adj", "/ˈrʌnsənət/", "xẻ thùy răng cưa ngược (lá)"),
    ("084348", "rundell", "noun", "/ˈrʌndəl/", "tên họ Rundell"),
    ("084349", "rundells", "noun", "/ˈrʌndəlz/", "gia đình họ Rundell"),
    ("084350", "rundlet", "noun", "/ˈrʌndlət/", "thùng gỗ đựng rượu nhỏ"),
    ("084351", "runlet", "noun", "/ˈrʌnlɪt/", "dòng suối nhỏ; thùng rượu nhỏ"),
    ("084352", "runniness", "noun", "/ˈrʌninəs/", "tính lỏng; độ loãng dễ chảy"),
    ("084353", "runproof", "adj", "/ˈrʌnˌpruːf/", "chống tuột sợi (vải dệt kim)"),
    ("084354", "runtiness", "noun", "/ˈrʌntinəs/", "sự còi cọc; vóc dáng nhỏ bé"),
    ("084355", "runways", "noun", "/ˈrʌnˌweɪz/", "đường băng sân bay; sàn diễn"),
    ("084356", "rupestral", "adj", "/ruːˈpɛstrəl/", "mọc trên đá; vẽ trên vách đá"),
    ("084357", "rupestrine", "adj", "/ruːˈpɛstrɪn/", "sống giữa vách đá; mọc trên đá"),
    ("084358", "rupicapra", "noun", "/ˌruːpɪˈkæprə/", "chi sơn dương núi Alps"),
    ("084359", "rupicola", "noun", "/ruːˈpɪkələ/", "chi chim mào đá Nam Mỹ"),
    ("084360", "rupicolous", "adj", "/ruːˈpɪkələs/", "sống hoặc mọc trên vách đá"),
    ("084361", "ruptiliocarpon", "noun", "/rʌpˌtɪliəˈkɑːrpɑːn/", "chi cây Ruptiliocarpon"),
    ("084362", "ruptured", "verb", "/ˈrʌptʃərd/", "đã vỡ; đã rách; đã đứt đoạn"),
    ("084363", "ruptures", "verb", "/ˈrʌptʃərz/", "làm vỡ; làm rách; cắt đứt"),
    ("084364", "rupturewort", "noun", "/ˈrʌptʃərˌwɜːrt/", "cây cỏ trị thoát vị Herniaria"),
    ("084365", "rupturing", "verb", "/ˈrʌptʃərɪŋ/", "đang làm vỡ; đang cắt đứt"),
    ("084366", "ruralism", "noun", "/ˈrʊrəˌlɪzəm/", "nếp sống thôn dã; từ địa phương"),
    ("084367", "ruralization", "noun", "/ˌrʊrələˈzeɪʃən/", "sự nông thôn hóa"),
    ("084368", "ruralize", "verb", "/ˈrʊrəˌlaɪz/", "nông thôn hóa; về sống ở quê"),
    ("084369", "rusa", "noun", "/ˈruːsə/", "chi hươu nai Rusa"),
    ("084370", "ruscaceae", "noun", "/rəˈskeɪsiːˌiː/", "họ thực vật Ruscaceae"),
    ("084371", "rushes", "verb", "/ˈrʌʃɪz/", "lao vội; hối hả"),
    ("084372", "rushlike", "adj", "/ˈrʌʃˌlaɪk/", "giống cây bấc; giống cây cói"),
    ("084373", "russ", "noun", "/rʊs/", "người Nga; dân tộc Rus cổ"),
    ("084374", "russianize", "verb", "/ˈrʌʃəˌnaɪz/", "Nga hóa"),
    ("084375", "russification", "noun", "/ˌrʌsəfəˈkeɪʃən/", "sự Nga hóa"),
    ("084376", "russify", "verb", "/ˈrʌsəˌfaɪ/", "Nga hóa"),
    ("084377", "russofile", "adj", "/ˈrʌsoʊˌfaɪl/", "thân Nga"),
    ("084378", "russophile", "adj", "/ˈrʌsəˌfaɪl/", "thân Nga; ngưỡng mộ nước Nga"),
    ("084379", "russophobe", "adj", "/ˈrʌsəˌfoʊb/", "bài Nga; ghét Nga"),
    ("084380", "russophobia", "noun", "/ˌrʌsəˈfoʊbiə/", "tâm lý bài Nga; sợ nước Nga"),
    ("084381", "russulaceae", "noun", "/ˌrʌsjəˈleɪsiːˌiː/", "họ nấm Russulaceae"),
    ("084382", "rustically", "adv", "/ˈrʌstɪkli/", "mộc mạc; chân chất quê mùa"),
    ("084383", "rusticated", "verb", "/ˈrʌstɪˌkeɪtɪd/", "đã đình chỉ học tạm thời; xây thô"),
    ("084384", "rusticates", "verb", "/ˈrʌstɪˌkeɪts/", "về quê sống; đình chỉ học tạm thời"),
    ("084385", "rusticating", "verb", "/ˈrʌstɪˌkeɪtɪŋ/", "đang về quê sống; đang đình chỉ"),
    ("084386", "rusticism", "noun", "/ˈrʌstɪˌsɪzəm/", "cách nói thôn dã; nét quê mùa"),
    ("084387", "rusticness", "noun", "/ˈrʌstɪknəs/", "vẻ mộc mạc; nét chân chất"),
    ("084388", "rustled", "verb", "/ˈrʌsəld/", "đã xào xạc; đã ăn trộm gia súc"),
    ("084389", "rustlers", "noun", "/ˈrʌslərz/", "kẻ trộm gia súc"),
    ("084390", "rustles", "verb", "/ˈrʌsəlz/", "xào xạc; ăn trộm gia súc"),
    ("084391", "rustless", "adj", "/ˈrʌstləs/", "không gỉ sét"),
    ("084392", "rustproofed", "adj", "/ˈrʌstˌpruːft/", "đã được xử lý chống gỉ"),
    ("084393", "rusts", "verb", "/rʌsts/", "bị gỉ sét; han gỉ"),
    ("084394", "rutaceous", "adj", "/ruːˈteɪʃəs/", "thuộc họ Cam chanh (Rutaceae)"),
    ("084395", "rutherfordium", "noun", "/ˌrʌðərˈfɔːrdiəm/", "nguyên tố hóa học rutherfordi"),
    ("084396", "ruthful", "adj", "/ˈruːθfəl/", "giàu lòng thương xót; hối hận"),
    ("084397", "ruthfulness", "noun", "/ˈruːθfəlnəs/", "lòng thương xót; nỗi ân hận"),
    ("084398", "ruthlessnesses", "noun", "/ˈruːθləsnəsɪz/", "sự tàn nhẫn; hành động nhẫn tâm"),
    ("084399", "ruths", "noun", "/ruːθs/", "lòng thương hại; sự hối tiếc"),
    ("084400", "rutilant", "adj", "/ˈruːtɪlənt/", "đỏ rực; sáng lấp lánh"),
    ("084401", "ruts", "verb", "/rʌts/", "tạo vết hằn bánh xe; vào mùa động dục"[:35]),
    ("084402", "rutting", "verb", "/ˈrʌtɪŋ/", "đang tạo vết bánh xe; đang động dục"[:35]),
]

# Shorten 084383, 084384, 084401, 084402 cleanly to <= 35
RECORDS[80] = ("084383", "rusticated", "verb", "/ˈrʌstɪˌkeɪtɪd/", "đã về quê sống; đã đình chỉ học")
RECORDS[81] = ("084384", "rusticates", "verb", "/ˈrʌstɪˌkeɪts/", "về quê sống; đình chỉ học")
RECORDS[98] = ("084401", "ruts", "verb", "/rʌts/", "cày thành rãnh; vào mùa động dục")
RECORDS[99] = ("084402", "rutting", "verb", "/ˈrʌtɪŋ/", "đang cày rãnh; đang động dục")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r09_raw_p4.json"))
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

json.dump(out, open("scratch/b37_r09_reviewed_p4.json", "w"), ensure_ascii=False, indent=2)
print("b37_r09_p4 saved OK")
