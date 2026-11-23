import json

records = [
    ("079703", "prosauropoda", "noun", "/ˌproʊsɔːˈrɑːpədə/", "nhóm khủng long tiền chân thằn lằn"),
    ("079704", "proscapsula", "noun", "/proʊˈskæpsjələ/", "túi thích ty nguyên thủy (sinh học)"),
    ("079705", "proscenia", "noun", "/proʊˈsiːniə/", "phần tiền sân khấu trước rèm"),
    ("079706", "proscolex", "noun", "/proʊˈskoʊlɛks/", "đầu sán non (sinh học ký sinh)"),
    ("079707", "proscolices", "noun", "/proʊˈskɑːlɪˌsiːz/", "các đầu sán non (ký sinh trùng)"),
    ("079708", "proscriber", "noun", "/proʊˈskraɪbər/", "người ra lệnh cấm, kẻ trục xuất"),
    ("079709", "proscribes", "verb", "/proʊˈskraɪbz/", "nghiêm cấm, đặt ra ngoài vòng luật"),
    ("079710", "proscribing", "verb", "/proʊˈskraɪbɪŋ/", "nghiêm cấm, đặt ra ngoài vòng luật"),
    ("079711", "proscrible", "verb", "/proʊˈskraɪb/", "cấm đoán, trục xuất (lỗi viết)"),
    ("079712", "proscriptive", "adj", "/proʊˈskrɪptɪv/", "nghiêm cấm, trục xuất, đàn áp"),
    ("079713", "proscriptively", "adv", "/proʊˈskrɪptɪvli/", "theo lối ngăn cấm, trục xuất"),
    ("079714", "prosect", "verb", "/proʊˈsɛkt/", "mổ xác chuẩn bị cho bài giảng y"),
    ("079715", "prosector", "noun", "/proʊˈsɛktər/", "trợ lý mổ xác phục vụ giảng dạy"),
    ("079716", "prosecutable", "adj", "/ˈprɑːsɪˌkjuːtəbəl/", "có thể bị truy tố, có thể khởi kiện"),
    ("079717", "prosecuted", "verb", "/ˈprɑːsɪˌkjuːtɪd/", "đã truy tố, khởi tố; theo đuổi"),
    ("079718", "prosecutes", "verb", "/ˈprɑːsɪˌkjuːts/", "truy tố, khởi tố; tiến hành tiếp"),
    ("079719", "prosecuting", "verb", "/ˈprɑːsɪˌkjuːtɪŋ/", "truy tố, buộc tội; theo đuổi"),
    ("079720", "prosecutrix", "noun", "/ˌprɑːsɪˈkjuːtrɪks/", "nữ công tố viên; nữ nguyên đơn"),
    ("079721", "proselyted", "verb", "/ˈprɑːsəˌlaɪtɪd/", "đã cải đạo, đã chiêu mộ tín đồ"),
    ("079722", "proselyter", "noun", "/ˈprɑːsəˌlaɪtər/", "người truyền đạo, người chiêu mộ"),
    ("079723", "proselytes", "verb", "/ˈprɑːsəˌlaɪts/", "cải đạo, chiêu mộ vào phe nhóm"),
    ("079724", "proselytical", "adj", "/ˌprɑːsəˈlɪtɪkəl/", "nhằm cải đạo, mang tính truyền giáo"),
    ("079725", "proselyting", "verb", "/ˈprɑːsəˌlaɪtɪŋ/", "cải đạo, chiêu mộ tín đồ mới"),
    ("079726", "proselytised", "verb", "/ˈprɑːsələˌtaɪzd/", "đã cải đạo, đã truyền bá (Anh)"),
    ("079727", "proselytises", "verb", "/ˈprɑːsələˌtaɪzɪz/", "cải đạo, truyền bá đức tin (Anh)"),
    ("079728", "proselytising", "verb", "/ˈprɑːsələˌtaɪzɪŋ/", "cải đạo, truyền bá đức tin (Anh)"),
    ("079729", "proselytization", "noun", "/ˌprɑːsələtəˈzeɪʃən/", "sự cải đạo, hoạt động truyền giáo"),
    ("079730", "proselytized", "verb", "/ˈprɑːsələˌtaɪzd/", "đã cải đạo, đã truyền bá đức tin"),
    ("079731", "proselytizer", "noun", "/ˈprɑːsələˌtaɪzər/", "người truyền giáo, người chiêu dụ"),
    ("079732", "proselytizes", "verb", "/ˈprɑːsələˌtaɪzɪz/", "cải đạo, chiêu dụ theo tôn giáo"),
    ("079733", "proselytizing", "verb", "/ˈprɑːsələˌtaɪzɪŋ/", "cải đạo, truyền đạo, chiêu dụ"),
    ("079734", "prosencephalic", "adj", "/ˌprɑːzɛnsəˈfælɪk/", "thuộc não trước (giải phẫu)"),
    ("079735", "prosencephalon", "noun", "/ˌprɑːzɛnˈsɛfəlɑːn/", "não trước (giải phẫu phôi thai)"),
    ("079736", "prosenchyma", "noun", "/prəˈzɛŋkɪmə/", "mô sợi dài (thực vật học)"),
    ("079737", "prosenchymatous", "adj", "/ˌprɑːzɛŋˈkɪmətəs/", "thuộc mô sợi dài (thực vật)"),
    ("079738", "proser", "noun", "/ˈproʊzər/", "người viết văn xuôi; người nói dai"),
    ("079739", "prosify", "verb", "/ˈproʊzəˌfaɪ/", "chuyển sang văn xuôi; làm tẻ nhạt"),
    ("079740", "prosily", "adv", "/ˈproʊzəli/", "một cách tẻ nhạt, khô khan"),
    ("079741", "prosimian", "noun", "/proʊˈsɪmiən/", "loài bán hầu, linh trưởng bậc thấp"),
    ("079742", "prosimii", "noun", "/proʊˈsɪmiˌaɪ/", "phân bộ Bán hầu (vượn cáo, cu li)"),
    ("079743", "prosiness", "noun", "/ˈproʊzinəs/", "tính chất khô khan, tẻ nhạt"),
    ("079744", "prosing", "noun", "/ˈproʊzɪŋ/", "lời nói dông dài nhàm chán"),
    ("079745", "prosiphon", "noun", "/proʊˈsaɪfən/", "ống hút nguyên thủy (chân đầu)"),
    ("079746", "prosit", "intj", "/ˈproʊzɪt/", "cạn ly, chúc sức khỏe! (tiếng Đức)"),
    ("079747", "proslavery", "adj", "/proʊˈsleɪvəri/", "ủng hộ chế độ chiếm hữu nô lệ"),
    ("079748", "prosobranch", "noun", "/ˈprɑːsəˌbræŋk/", "ốc phân lớp mang trước (sinh học)"),
    ("079749", "prosodiacal", "adj", "/ˌprɑːsəˈdaɪəkəl/", "thuộc vận luật, thi pháp học"),
    ("079750", "prosodial", "adj", "/prəˈsoʊdiəl/", "thuộc vận luật, ngữ điệu thơ ca"),
    ("079751", "prosodian", "noun", "/prəˈsoʊdiən/", "nhà nghiên cứu vận luật học"),
    ("079752", "prosodically", "adv", "/prəˈsɑːdɪkli/", "về mặt vận luật, theo ngữ điệu"),
    ("079753", "prosodion", "noun", "/prəˈsoʊdiˌɑːn/", "khúc thánh ca hành lễ Hy Lạp cổ"),
    ("079754", "prosodist", "noun", "/ˈprɑːsədɪst/", "chuyên gia về vận luật và thi pháp"),
    ("079755", "prosom", "noun", "/ˈproʊsɑːm/", "thuốc ngủ estazolam (biệt dược)"),
    ("079756", "prosopium", "noun", "/prəˈsoʊpiəm/", "chi cá hồi trắng (Prosopium)"),
    ("079757", "prosopoplegia", "noun", "/ˌprɑːsəpoʊˈpliːdʒə/", "chứng liệt cơ mặt (y học)"),
    ("079758", "prosopopoeia", "noun", "/prəˌsɑːpəˈpiːə/", "biện pháp nhân hóa (tu từ học)"),
    ("079759", "prospected", "verb", "/ˈprɑːspɛktɪd/", "đã thăm dò (mỏ), đã tìm kiếm"),
    ("079760", "prospecting", "verb", "/ˈprɑːspɛktɪŋ/", "thăm dò khoáng sản; tìm kiếm"),
    ("079761", "prospectively", "adv", "/prəˈspɛktɪvli/", "trong tương lai, đầy triển vọng"),
    ("079762", "prospects", "verb", "/ˈprɑːspɛkts/", "thăm dò khoáng sản; tìm kiếm cơ hội"),
    ("079763", "prospered", "verb", "/ˈprɑːspərd/", "đã phát đạt, đã thịnh vượng"),
    ("079764", "prosperities", "noun", "/prɑːˈspɛrətiz/", "sự phồn vinh, thời kỳ thịnh vượng"),
    ("079765", "prosperousness", "noun", "/ˈprɑːspərəsnəs/", "sự phát đạt, sự phồn thịnh"),
    ("079766", "prospers", "verb", "/ˈprɑːspərz/", "phát đạt, thịnh vượng, thành công"),
    ("079767", "prospicience", "noun", "/prəˈspɪʃəns/", "tầm nhìn xa, sự tiên liệu trước"),
    ("079768", "prospicient", "adj", "/prəˈspɪʃənt/", "biết lo xa, có tầm nhìn tương lai"),
    ("079769", "prosternal", "adj", "/proʊˈstɜːrnəl/", "thuộc tấm ngực trước (côn trùng)"),
    ("079770", "prosternum", "noun", "/proʊˈstɜːrnəm/", "tấm ngực trước (côn trùng học)"),
    ("079771", "prostheca", "noun", "/prɑːsˈθiːkə/", "mảnh phụ hàm dưới (côn trùng)"),
    ("079772", "prostheon", "noun", "/ˈprɑːsθiˌɑːn/", "điểm nhân trắc xương ổ răng trên"),
    ("079773", "prostheses", "noun", "/prɑːsˈθiːsiːz/", "các bộ phận giả (răng, chân tay)"),
    ("079774", "prosthetically", "adv", "/prɑːsˈθɛtɪkli/", "bằng bộ phận giả, theo chỉnh hình"),
    ("079775", "prosthion", "noun", "/ˈprɑːsθiˌɑːn/", "điểm xương ổ răng hàm trên"),
    ("079776", "prosthodontia", "noun", "/ˌprɑːsθəˈdɑːnʃə/", "chuyên khoa phục hình răng giả"),
    ("079777", "prostigmin", "noun", "/proʊˈstɪɡmɪn/", "thuốc trị nhược cơ neostigmine"),
    ("079778", "prostituted", "verb", "/ˈprɑːstəˌtuːtɪd/", "đã bán dâm; đã bán rẻ danh dự"),
    ("079779", "prostitutes", "verb", "/ˈprɑːstəˌtuːts/", "bán dâm; bán rẻ tài năng danh dự"),
    ("079780", "prostituting", "verb", "/ˈprɑːstəˌtuːtɪŋ/", "bán dâm; bán rẻ tài năng danh dự"),
    ("079781", "prostitutor", "noun", "/ˈprɑːstəˌtuːtər/", "kẻ ép bán dâm; kẻ bán rẻ lương tâm"),
    ("079782", "prostomia", "noun", "/proʊˈstoʊmiə/", "các thùy trước miệng (giun đốt)"),
    ("079783", "prostomial", "adj", "/proʊˈstoʊmiəl/", "thuộc thùy trước miệng (giun đốt)"),
    ("079784", "prostomium", "noun", "/proʊˈstoʊmiəm/", "thùy trước miệng (động vật đốt)"),
    ("079785", "prostrated", "verb", "/ˈprɑːstreɪtɪd/", "đã phủ phục; đã làm suy kiệt"),
    ("079786", "prostrates", "verb", "/ˈprɑːstreɪts/", "phủ phục, nằm sấp; làm suy sụp"),
    ("079787", "prostrating", "verb", "/ˈprɑːstreɪtɪŋ/", "phủ phục, nằm sấp; làm kiệt sức"),
    ("079788", "prostrator", "noun", "/ˈprɑːstreɪtər/", "người lật đổ; người nằm sụp lạy"),
    ("079789", "prot", "noun", "/prɑːt/", "người theo đạo Tin Lành (viết tắt)"),
    ("079790", "protagonism", "noun", "/prəˈtæɡəˌnɪzəm/", "vai trò nhân vật chính; sự ủng hộ"),
    ("079791", "protandric", "adj", "/proʊˈtændrɪk/", "nhị chín trước, đực trước"),
    ("079792", "protandrism", "noun", "/proʊˈtændrɪzəm/", "hiện tượng nhị chín trước nhụy"),
    ("079793", "protandrous", "adj", "/proʊˈtændrəs/", "có nhị chín trước, đực trước"),
    ("079794", "protandry", "noun", "/proʊˈtændri/", "tính nhị chín trước, đực trước"),
    ("079795", "protanopia", "noun", "/ˌproʊtəˈnoʊpiə/", "chứng mù màu đỏ (nhãn khoa)"),
    ("079796", "protanopic", "adj", "/ˌproʊtəˈnɑːpɪk/", "mắc chứng mù màu đỏ (nhãn khoa)"),
    ("079797", "protases", "noun", "/ˈprɑːtəˌsiːz/", "các mệnh đề điều kiện; phần mở kịch"),
    ("079798", "protasis", "noun", "/ˈprɑːtəsɪs/", "mệnh đề điều kiện; phần mở đầu kịch"),
    ("079799", "protatic", "adj", "/proʊˈtætɪk/", "mở đầu kịch; thuộc mệnh đề giả định"),
    ("079800", "proteales", "noun", "/ˌproʊtiˈeɪliːz/", "bộ Quắn hoa (thực vật học)"),
    ("079801", "protectant", "noun", "/prəˈtɛktənt/", "chất bảo vệ, vật che chở"),
    ("079802", "protectants", "noun", "/prəˈtɛktənts/", "các chất bảo vệ, thuốc bảo vệ"),
]

raw = json.load(open("scratch/b36_r10_raw_p3.json"))
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
with open("scratch/b36_r10_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b36_r10_p3 saved OK")
