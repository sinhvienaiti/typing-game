import json

rows = [
    ("078703", "pregnability", "noun", "/ˌprɛɡnəˈbɪlɪti/", "tính dễ bị đánh chiếm, công phá"),
    ("078704", "pregnable", "adj", "/ˈprɛɡnəbəl/", "có thể bị đánh chiếm, công phá"),
    ("078705", "pregnanediol", "noun", "/prɛɡˌneɪnˈdaɪɒl/", "chất chuyển hóa pregnanediol"),
    ("078706", "pregnantly", "adv", "/ˈprɛɡnəntli/", "hàm súc, đầy ẩn ý sâu sắc"),
    ("078707", "pregravidic", "adj", "/ˌpriːɡrəˈvɪdɪk/", "trước giai đoạn mang thai (y học)"),
    ("078708", "preguidance", "noun", "/ˌpriːˈɡaɪdəns/", "sự hướng dẫn sơ bộ ban đầu"),
    ("078709", "pregustations", "noun", "/ˌpriːɡʌsˈteɪʃənz/", "sự nếm trước, sự thưởng thức trước"),
    ("078710", "prehallux", "noun", "/ˌpriːˈhæləks/", "xương tiền ngón cái (lưỡng cư)"),
    ("078711", "preheater", "noun", "/ˌpriːˈhiːtər/", "bộ gia nhiệt sơ bộ, máy hâm trước"),
    ("078712", "preheating", "noun", "/ˌpriːˈhiːtɪŋ/", "sự gia nhiệt trước, nung sơ bộ"),
    ("078713", "prehensible", "adj", "/prɪˈhɛnsɪbəl/", "có thể cầm nắm, bám giữ được"),
    ("078714", "prehensility", "noun", "/ˌpriːhɛnˈsɪlɪti/", "khả năng cầm nắm, bám cuốn (đuôi)"),
    ("078715", "prehensor", "noun", "/prɪˈhɛnsər/", "chi trước dùng để bắt mồi (sâu bọ)"),
    ("078716", "prehepatic", "adj", "/ˌpriːhɪˈpætɪk/", "ở phía trước gan (giải phẫu)"),
    ("078717", "prehistorian", "noun", "/ˌpriːhɪˈstɔːriən/", "nhà nghiên cứu thời tiền sử"),
    ("078718", "prehistorically", "adv", "/ˌpriːhɪˈstɒrɪkli/", "thuộc thời tiền sử; từ thuở tiền sử"),
    ("078719", "prehistories", "noun", "/ˌpriːˈhɪstəriz/", "thời tiền sử; giai đoạn trước đó"),
    ("078720", "prehuman", "adj", "/ˌpriːˈhjuːmən/", "tiền nhân loại (trước khi có người)"),
    ("078721", "preignition", "noun", "/ˌpriːɪɡˈnɪʃən/", "sự kích nổ sớm (động cơ đốt trong)"),
    ("078722", "preindication", "noun", "/ˌpriːɪndɪˈkeɪʃən/", "dấu hiệu báo trước, điềm báo trước"),
    ("078723", "preindustrial", "adj", "/ˌpriːɪnˈdʌstriəl/", "thuộc thời kỳ tiền công nghiệp"),
    ("078724", "preinstruct", "verb", "/ˌpriːɪnˈstrʌkt/", "chỉ dẫn trước, huấn luyện trước"),
    ("078725", "preisolate", "verb", "/ˌpriːˈaɪsəleɪt/", "cách ly trước, phân lập từ trước"),
    ("078726", "prejudged", "verb", "/ˌpriːˈdʒʌdʒd/", "đã phán xét vội, định kiến trước"),
    ("078727", "prejudgement", "noun", "/ˌpriːˈdʒʌdʒmənt/", "sự phán xét vội vàng; định kiến"),
    ("078728", "prejudger", "noun", "/ˌpriːˈdʒʌdʒər/", "người phán xét vội vã thiếu xét"),
    ("078729", "prejudges", "verb", "/ˌpriːˈdʒʌdʒɪz/", "phán xét vội vã, định kiến trước"),
    ("078730", "prejudging", "verb", "/ˌpriːˈdʒʌdʒɪŋ/", "phán xét vội vã, định kiến trước"),
    ("078731", "prejudicate", "verb", "/prɪˈdʒuːdɪkeɪt/", "phán quyết vội khi chưa tra xét"),
    ("078732", "prejudices", "verb", "/ˈprɛdʒədɪsɪz/", "gây thành kiến; làm phương hại"),
    ("078733", "prejudicially", "adv", "/ˌprɛdʒəˈdɪʃəli/", "gây phương hại, bất lợi; định kiến"),
    ("078734", "prejudicialness", "noun", "/ˌprɛdʒəˈdɪʃəlnəs/", "tính gây phương hại, thiên vị"),
    ("078735", "prejudicing", "verb", "/ˈprɛdʒədɪsɪŋ/", "gây thành kiến; làm phương hại"),
    ("078736", "prejudicious", "adj", "/ˌprɛdʒəˈdɪʃəs/", "có thành kiến, thiên vị, bất lợi"),
    ("078737", "prelacies", "noun", "/ˈprɛləsiz/", "chức giám mục; hàng giáo phẩm cao"),
    ("078738", "prelatess", "noun", "/ˈprɛlətɪs/", "nữ giáo trưởng; vợ giám mục (cổ)"),
    ("078739", "prelatic", "adj", "/prɪˈlætɪk/", "thuộc chức giám mục, hàng giáo phẩm"),
    ("078740", "prelatical", "adj", "/prɪˈlætɪkəl/", "thuộc chức giám mục, hàng giáo phẩm"),
    ("078741", "prelatise", "verb", "/ˈprɛlətaɪz/", "đưa vào hàng giáo phẩm giám mục"),
    ("078742", "prelatism", "noun", "/ˈprɛlətɪzəm/", "chế độ cai trị bằng giám mục"),
    ("078743", "prelatist", "noun", "/ˈprɛlətɪst/", "người ủng hộ chế độ giám mục"),
    ("078744", "prelatize", "verb", "/ˈprɛlətaɪz/", "đưa vào hàng giáo phẩm giám mục"),
    ("078745", "prelaunch", "adj", "/ˌpriːˈlɔːntʃ/", "trước khi phóng tên lửa, ra mắt"),
    ("078746", "prelect", "verb", "/prɪˈlɛkt/", "giảng bài công khai ở đại học (cổ)"),
    ("078747", "prelection", "noun", "/prɪˈlɛkʃən/", "bài thuyết giảng đại học (cổ)"),
    ("078748", "prelector", "noun", "/prɪˈlɛktər/", "giảng viên thuyết trình đại học"),
    ("078749", "prelibation", "noun", "/ˌpriːlaɪˈbeɪʃən/", "sự nếm trước, thưởng thức trước"),
    ("078750", "preliminarily", "adv", "/prɪˈlɪmɪˌnɛrəli/", "một cách sơ bộ, bước đầu mở màn"),
    ("078751", "preload", "noun", "/ˈpriːloʊd/", "tải trọng đặt trước (kỹ thuật)"),
    ("078752", "prelone", "noun", "/ˈpriːloʊn/", "thuốc kháng viêm Prelone"),
    ("078753", "preluder", "noun", "/ˈprɛljuːdər/", "nhạc công chơi khúc dạo đầu"),
    ("078754", "preludial", "adj", "/prɪˈluːdiəl/", "mang tính khúc dạo đầu, mở màn"),
    ("078755", "preludize", "verb", "/ˈprɛljʊdaɪz/", "chơi khúc dạo đầu; mở màn trước"),
    ("078756", "prelusion", "noun", "/prɪˈluːʒən/", "phần mở đầu, khúc mào đầu"),
    ("078757", "prelusive", "adj", "/prɪˈluːsɪv/", "mang tính mở đầu, dạo đầu"),
    ("078758", "prelusively", "adv", "/prɪˈluːsɪvli/", "như phần mở đầu, dạo đầu"),
    ("078759", "premandibular", "adj", "/ˌpriːmænˈdɪbjələr/", "ở phía trước xương hàm dưới"),
    ("078760", "premaritally", "adv", "/ˌpriːˈmærɪtəli/", "trước hôn nhân, trước khi kết hôn"),
    ("078761", "prematuration", "noun", "/ˌpriːmætʃʊˈreɪʃən/", "sự chín sớm, phát triển sớm"),
    ("078762", "prematureness", "noun", "/ˌpriːməˈtʃʊrnəs/", "tính non nớt; sự xảy ra quá sớm"),
    ("078763", "premaxilla", "noun", "/ˌpriːmækˈsɪlə/", "xương tiền hàm trên (giải phẫu)"),
    ("078764", "premaxillae", "noun", "/ˌpriːmækˈsɪliː/", "xương tiền hàm trên (giải phẫu)"),
    ("078765", "premaxillary", "adj", "/ˌpriːˈmæksəˌlɛri/", "thuộc xương tiền hàm trên"),
    ("078766", "premed", "noun", "/ˈpriːmɛd/", "sinh viên dự bị ngành y (Mỹ)"),
    ("078767", "premedication", "noun", "/ˌpriːmɛdɪˈkeɪʃən/", "thuốc tiền mê (uống trước gây mê)"),
    ("078768", "premedications", "noun", "/ˌpriːmɛdɪˈkeɪʃənz/", "thuốc tiền mê (uống trước gây mê)"),
    ("078769", "premeditatedly", "adv", "/ˌpriːˈmɛdɪteɪtɪdli/", "một cách cố ý, có tính toán trước"),
    ("078770", "premeditates", "verb", "/ˌpriːˈmɛdɪteɪts/", "trù tính trước, dự mưu trước"),
    ("078771", "premeditating", "verb", "/ˌpriːˈmɛdɪteɪtɪŋ/", "trù tính trước, dự mưu trước"),
    ("078772", "premeditative", "adj", "/ˌpriːˈmɛdɪteɪtɪv/", "có tính trù tính trước, dự mưu"),
    ("078773", "premeditator", "noun", "/ˌpriːˈmɛdɪteɪtər/", "kẻ chủ mưu tính toán từ trước"),
    ("078774", "premenstrua", "noun", "/ˌpriːˈmɛnstruə/", "thời kỳ tiền kinh nguyệt"),
    ("078775", "premillennial", "adj", "/ˌpriːmɪˈlɛniəl/", "thuộc thuyết tiền thiên niên kỷ"),
    ("078776", "premillennialism", "noun", "/ˌpriːmɪˈlɛniəlɪzəm/", "thuyết tiền thiên niên kỷ (Kitô)"),
    ("078777", "premillennialist", "noun", "/ˌpriːmɪˈlɛniəlɪst/", "người theo thuyết tiền thiên niên"),
    ("078778", "premised", "verb", "/ˈprɛmɪst/", "đã đặt làm tiền đề, giả định trước"),
    ("078779", "premising", "verb", "/ˈprɛmɪsɪŋ/", "đặt làm tiền đề, giả định trước"),
    ("078780", "premixed", "verb", "/ˌpriːˈmɪkst/", "đã trộn sẵn trước, pha chế sẵn"),
    ("078781", "premixes", "verb", "/ˌpriːˈmɪksɪz/", "trộn sẵn trước, pha chế sẵn"),
    ("078782", "premixing", "verb", "/ˌpriːˈmɪksɪŋ/", "trộn sẵn trước, pha chế sẵn"),
    ("078783", "premonish", "verb", "/prɪˈmɒnɪʃ/", "cảnh báo trước, báo hiệu trước"),
    ("078784", "premonitor", "noun", "/prɪˈmɒnɪtər/", "người hoặc vật cảnh báo trước"),
    ("078785", "premonitorily", "adv", "/prɪˈmɒnɪtərɪli/", "như điềm báo trước, cảnh báo"),
    ("078786", "premorse", "adj", "/prɪˈmɔːrs/", "có đầu cụt lởm chởm (thực vật)"),
    ("078787", "premotion", "noun", "/ˌpriːˈmoʊʃən/", "sự thúc đẩy ban đầu (thần học)"),
    ("078788", "premoulding", "noun", "/ˌpriːˈmoʊldɪŋ/", "sự ép tạo hình sơ bộ (công nghiệp)"),
    ("078789", "premundane", "adj", "/ˌpriːˈmʌndeɪn/", "trước khi có thế giới (khởi thủy)"),
    ("078790", "premunition", "noun", "/ˌpriːmjʊˈnɪʃən/", "sự phòng bị trước; miễn dịch nhiễm"),
    ("078791", "prename", "noun", "/ˈpriːneɪm/", "tên riêng (tên gọi đứng trước họ)"),
    ("078792", "prenanthes", "noun", "/prɪˈnænθiːz/", "chi rau diếp rừng (Prenanthes)"),
    ("078793", "prenatally", "adv", "/ˌpriːˈneɪtəli/", "ở giai đoạn trước khi sinh"),
    ("078794", "prenominate", "verb", "/ˌpriːˈnɒmɪneɪt/", "đã nêu tên trước đây (từ cổ)"),
    ("078795", "prenotion", "noun", "/ˌpriːˈnoʊʃən/", "quan niệm tiên thiên; sự linh cảm"),
    ("078796", "prenticeship", "noun", "/ˈprɛntɪsʃɪp/", "thời gian học việc, học nghề"),
    ("078797", "preoccipital", "adj", "/ˌpriːɒkˈsɪpɪtəl/", "ở phía trước thùy chẩm (não)"),
    ("078798", "preoccupancy", "noun", "/priˈɒkjʊpənsi/", "quyền chiếm giữ trước (tài sản)"),
    ("078799", "preoccupies", "verb", "/priˈɑːkjʊˌpaɪz/", "làm bận tâm, choán hết tâm trí"),
    ("078800", "preoccupying", "verb", "/priˈɑːkjʊˌpaɪɪŋ/", "làm bận tâm, choán hết tâm trí"),
    ("078801", "preocular", "adj", "/ˌpriːˈɒkjələr/", "ở phía trước mắt (sinh học)"),
    ("078802", "preoiler", "noun", "/ˌpriːˈɔɪlər/", "dụng cụ bôi trơn sơ bộ"),
]

with open("scratch/b36_r08_raw_p3.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r08_p3.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r08_p3 saved OK")
