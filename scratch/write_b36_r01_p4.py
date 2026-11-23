import json

rows = [
    ("075303", "pentagynous", "adj", "/pɛnˈtædʒɪnəs/", "có năm nhụy (thực vật)"),
    ("075304", "pentahedral", "adj", "/ˌpɛntəˈhiːdrəl/", "có năm mặt (hình học)"),
    ("075305", "pentahedron", "noun", "/ˌpɛntəˈhiːdrən/", "hình khối năm mặt"),
    ("075306", "pentahydrate", "noun", "/ˌpɛntəˈhaɪdreɪt/", "muối ngậm năm phân tử nước"),
    ("075307", "pentahydrates", "noun", "/ˌpɛntəˈhaɪdreɪts/", "muối ngậm năm phân tử nước"),
    ("075308", "pentail", "noun", "/ˈpɛnteɪl/", "chuột chù cây đuôi lông"),
    ("075309", "pentamerism", "noun", "/pɛnˈtæmərɪzəm/", "cấu tạo theo bội số năm (sinh học)"),
    ("075310", "pentamethylenetetrazol", "noun", "/ˌpɛntəmɛθɪliːnˈtɛtrəzoʊl/", "thuốc trợ tim mạch pentetrazol"),
    ("075311", "pentandrous", "adj", "/pɛnˈtændrəs/", "có năm nhị hoa (thực vật)"),
    ("075312", "pentane", "noun", "/ˈpɛnteɪn/", "khí hydrocacbon pentan"),
    ("075313", "pentangular", "adj", "/pɛnˈtæŋɡjələr/", "có năm góc; hình ngũ giác"),
    ("075314", "pentapetalous", "adj", "/ˌpɛntəˈpɛtələs/", "có năm cánh hoa (thực vật)"),
    ("075315", "pentaphyllous", "adj", "/ˌpɛntəˈfɪləs/", "có năm lá (thực vật)"),
    ("075316", "pentaploid", "adj", "/ˈpɛntəplɔɪd/", "ngũ bội (năm bộ NST)"),
    ("075317", "pentaprism", "noun", "/ˈpɛntəˌprɪzəm/", "lăng kính năm mặt (máy ảnh)"),
    ("075318", "pentaspherical", "adj", "/ˌpɛntəˈsfɛrɪkəl/", "ngũ cầu (tọa độ hình học)"),
    ("075319", "pentastomid", "noun", "/pɛnˈtæstəmɪd/", "giáp xác ký sinh sán lưỡi"),
    ("075320", "pentastomida", "noun", "/ˌpɛntəˈstɒmɪdə/", "lớp Giáp xác sán lưỡi"),
    ("075321", "pentastyle", "noun", "/ˈpɛntəstaɪl/", "hàng hiên năm cột (kiến trúc cổ)"),
    ("075322", "pentasyllabic", "adj", "/ˌpɛntəsɪˈlæbɪk/", "có năm âm tiết (ngôn ngữ)"),
    ("075323", "pentasyllable", "noun", "/ˈpɛntəˌsɪləbəl/", "từ gồm năm âm tiết"),
    ("075324", "pentatomic", "adj", "/ˌpɛntəˈtɒmɪk/", "có năm nguyên tử (hóa học)"),
    ("075325", "pentatone", "noun", "/ˈpɛntətoʊn/", "quãng năm âm; thang âm ngũ cung"),
    ("075326", "pentavalence", "noun", "/ˌpɛntəˈveɪləns/", "hóa trị năm (hóa học)"),
    ("075327", "pentecostalist", "noun", "/ˌpɛntɪˈkɒstəlɪst/", "tín đồ Tin Lành Ngũ Tuần"),
    ("075328", "pentecostals", "noun", "/ˌpɛntɪˈkɒstəlz/", "tín đồ phái Ngũ Tuần"),
    ("075329", "penthouses", "noun", "/ˈpɛntˌhaʊsɪz/", "căn hộ áp mái; mái che dốc"),
    ("075330", "pentice", "noun", "/ˈpɛntɪs/", "mái che dốc gắn tường (kiến trúc)"),
    ("075331", "pentimenti", "noun", "/ˌpɛntɪˈmɛnti/", "vết vẽ cũ lộ dưới sơn (hội họa)"),
    ("075332", "pentomic", "adj", "/pɛnˈtɒmɪk/", "thuộc sư đoàn ngũ giác (quân sự Mỹ)"),
    ("075333", "pentstemon", "noun", "/ˈpɛntstɪmən/", "chi hoa chuông Penstemon (Mỹ)"),
    ("075334", "pentylenetetrazol", "noun", "/ˌpɛntɪliːnˈtɛtrəzoʊl/", "thuốc kích thích thần kinh PTZ"),
    ("075335", "penuche", "noun", "/pəˈnuːtʃi/", "kẹo đường nâu bơ sữa penuche"),
    ("075336", "penuchle", "noun", "/ˈpiːnʌkəl/", "trò chơi bài pinochle"),
    ("075337", "penultima", "noun", "/pɪˈnʌltɪmə/", "âm tiết áp chót"),
    ("075338", "penultimately", "adv", "/pɪˈnʌltɪmɪtli/", "ở vị trí áp chót"),
    ("075339", "penumbrae", "noun", "/pɪˈnʌmbriː/", "vùng nửa tối (thiên văn)"),
    ("075340", "penumbras", "noun", "/pɪˈnʌmbrəz/", "vùng nửa tối (thiên văn)"),
    ("075341", "penumbrous", "adj", "/pɪˈnʌmbrəs/", "thuộc vùng nửa tối, mờ ảo"),
    ("075342", "penuriously", "adv", "/pɪˈnjʊriəsli/", "keo kiệt bủn xỉn; túng thiếu"),
    ("075343", "penuriousness", "noun", "/pɪˈnjʊriəsnəs/", "tính bủn xỉn; cảnh túng quẫn"),
    ("075344", "penutian", "noun", "/pəˈnuːtiən/", "ngữ hệ bản địa Penutian (Bắc Mỹ)"),
    ("075345", "penvis", "noun", "/ˈpɛnvɪs/", "biến thể viết nhầm của pelvis"),
    ("075346", "penwiper", "noun", "/ˈpɛnˌwaɪpər/", "miếng giẻ lau ngòi bút mực"),
    ("075347", "peopler", "noun", "/ˈpiːpələr/", "người đưa dân tới định cư"),
    ("075348", "peopling", "verb", "/ˈpiːpəlɪŋ/", "đưa dân đến ở, lập cư"),
    ("075349", "peperino", "noun", "/ˌpɛpəˈriːnoʊ/", "đá tro núi lửa peperino (Ý)"),
    ("075350", "peplus", "noun", "/ˈpɛpləs/", "áo choàng Hy Lạp cổ; màng bào tử"),
    ("075351", "pepo", "noun", "/ˈpiːpoʊ/", "quả bầu nậm (dạng quả bí, dưa)"),
    ("075352", "pepped", "verb", "/pɛpt/", "đã tiếp thêm sinh lực; khuấy động"),
    ("075353", "pepperbox", "noun", "/ˈpɛpərˌbɒks/", "lọ rắc hạt tiêu; súng lục xoay nòng"),
    ("075354", "peppered", "verb", "/ˈpɛpərd/", "đã rắc tiêu; nã đạn liên tiếp"),
    ("075355", "pepperiness", "noun", "/ˈpɛpərinəs/", "vị cay nồng; tính nóng nảy"),
    ("075356", "peppering", "verb", "/ˈpɛpərɪŋ/", "rắc tiêu; nã đạn tới tấp"),
    ("075357", "peppers", "verb", "/ˈpɛpərz/", "rắc tiêu; bắn tỉa tới tấp"),
    ("075358", "pepperwort", "noun", "/ˈpɛpərˌwɜːrt/", "cây cải cay dại (Lepidium)"),
    ("075359", "peppily", "adv", "/ˈpɛpɪli/", "một cách hăng hái, sôi nổi"),
    ("075360", "peppiness", "noun", "/ˈpɛpinəs/", "sự hoạt bát, hăng hái, sôi nổi"),
    ("075361", "pepping", "verb", "/ˈpɛpɪŋ/", "tiếp thêm sinh lực; làm sôi nổi"),
    ("075362", "peps", "verb", "/pɛps/", "tiếp thêm sinh lực; làm sôi nổi"),
    ("075363", "peptics", "noun", "/ˈpɛptɪks/", "thuốc hỗ trợ tiêu hóa (y học)"),
    ("075364", "peptisation", "noun", "/ˌpɛptɪˈzeɪʃən/", "sự keo tán (phân tán keo)"),
    ("075365", "peptise", "verb", "/ˈpɛptaɪz/", "keo tán (phân tán keo)"),
    ("075366", "peptization", "noun", "/ˌpɛptɪˈzeɪʃən/", "sự keo tán (phân tán keo)"),
    ("075367", "peptize", "verb", "/ˈpɛptaɪz/", "keo tán (phân tán keo)"),
    ("075368", "peptogen", "noun", "/ˈpɛptədʒən/", "chất kích thích tạo pepsin"),
    ("075369", "peptonic", "adj", "/pɛpˈtɒnɪk/", "thuộc pepton (chất đạm thủy phân)"),
    ("075370", "peptonization", "noun", "/ˌpɛptənaɪˈzeɪʃən/", "sự thủy phân thành pepton"),
    ("075371", "peptonize", "verb", "/ˈpɛptənaɪz/", "thủy phân protein thành pepton"),
    ("075372", "per", "prep", "/pɜːr/", "mỗi; theo; bằng, qua (phương tiện)"),
    ("075373", "perambulated", "verb", "/pəˈræmbjəleɪtɪd/", "đã đi dạo; đi kiểm tra thực địa"),
    ("075374", "perambulates", "verb", "/pəˈræmbjəleɪts/", "đi dạo; đi kiểm tra thực địa"),
    ("075375", "perambulators", "noun", "/pəˈræmbjəleɪtərz/", "xe đẩy trẻ em; máy đo quãng đường"),
    ("075376", "perambulatory", "adj", "/pəˈræmbjələtɔːri/", "hay đi lại; đi kiểm tra thực địa"),
    ("075377", "peramelidae", "noun", "/ˌpɛrəˈmɛlɪdiː/", "họ Chuột túi bandicoot"),
    ("075378", "perborate", "noun", "/pərˈbɔːreɪt/", "muối peborat (chất tẩy trắng)"),
    ("075379", "perceivably", "adv", "/pərˈsiːvəbli/", "có thể nhận thấy rõ rệt"),
    ("075380", "perceives", "verb", "/pərˈsiːvz/", "nhận thấy, cảm nhận, nhận thức"),
    ("075381", "perceiving", "verb", "/pərˈsiːvɪŋ/", "nhận thấy, cảm nhận, nhận thức"),
    ("075382", "percentagewise", "adv", "/pərˈsɛntɪdʒwaɪz/", "tính theo tỷ lệ phần trăm"),
    ("075383", "perceptibility", "noun", "/pərˌsɛptəˈbɪlɪti/", "tính có thể nhận biết, tri giác"),
    ("075384", "perceptional", "adj", "/pərˈsɛpʃənəl/", "thuộc nhận thức, tri giác"),
    ("075385", "perceptionalism", "noun", "/pərˈsɛpʃənəlɪzəm/", "thuyết lấy tri giác làm nền tảng"),
    ("075386", "perceptivity", "noun", "/ˌpɜːrsɛpˈtɪvɪti/", "năng lực tri giác, thấu hiểu"),
    ("075387", "percetile", "noun", "/ˈpɜːrsətaɪl/", "lỗi viết của percentile (phân vị)"),
    ("075388", "perched", "verb", "/pɜːrtʃt/", "đã đậu trên cành; nằm cheo leo"),
    ("075389", "percher", "noun", "/ˈpɜːrtʃər/", "chim đậu cành; người ngồi chỗ cao"),
    ("075390", "perches", "verb", "/ˈpɜːrtʃɪz/", "đậu trên cành; đặt cheo leo"),
    ("075391", "perching", "verb", "/ˈpɜːrtʃɪŋ/", "đậu trên cành; đặt cheo leo"),
    ("075392", "perchloric", "adj", "/pərˈklɔːrɪk/", "thuộc axit pecloric"),
    ("075393", "perchloride", "noun", "/pərˈklɔːraɪd/", "hợp chất peclorua"),
    ("075394", "perchloromethane", "noun", "/pərˌklɔːroʊˈmɛθeɪn/", "chất cacbon tetraclorua (CCl4)"),
    ("075395", "percidae", "noun", "/ˈpɜːrsɪdiː/", "họ Cá vược nước ngọt (Percidae)"),
    ("075396", "perciformes", "noun", "/ˌpɜːrsɪˈfɔːrmiːz/", "bộ Cá vược (Perciformes)"),
    ("075397", "percina", "noun", "/pərˈsaɪnə/", "chi cá vược suối nhỏ (Percina)"),
    ("075398", "percipience", "noun", "/pərˈsɪpiəns/", "sự tinh tường, nhạy bén tri giác"),
    ("075399", "percipiency", "noun", "/pərˈsɪpiənsi/", "tính tinh tường, nhạy bén"),
    ("075400", "percoid", "noun", "/ˈpɜːrkɔɪd/", "cá dạng cá vược"),
    ("075401", "percoidea", "noun", "/ˌpɜːrˈkɔɪdiə/", "siêu họ Cá vược (Percoidea)"),
    ("075402", "percoidean", "noun", "/pərˈkɔɪdiən/", "thuộc cá vược; loài cá vược"),
]

with open("scratch/b36_r01_raw_p4.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r01_p4.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r01_p4 saved OK")
