import json

items = [
    ("070203", "invidias", "noun", "/ɪnˈvɪdiəz/", "sự ganh tỵ ác ý (tiếng Latinh)"),
    ("070204", "inwardnesses", "noun", "/ˈɪnwərdnəsɪz/", "bản chất nội tâm sâu kín"),
    ("070205", "jeremiads", "noun", "/ˌdʒɛrɪˈmaɪədz/", "bài than trách bi quan dài dòng"),
    ("070206", "jussieus", "noun", "/dʒuːˈsjɜːrz/", "nhà thực vật học Pháp Jussieu"),
    ("070207", "kitbags", "noun", "/ˈkɪtˌbæɡz/", "túi quân trang; túi đựng đồ nghề"),
    ("070208", "konoes", "noun", "/ˈkoʊnoʊˌeɪz/", "thủ tướng Nhật Fumimaro Konoe"),
    ("070209", "koussevitzkies", "noun", "/ˌkuːsəˈvɪtskiz/", "nhạc trưởng Sergei Koussevitzky"),
    ("070210", "lehars", "noun", "/leɪˈhɑːrz/", "nhà soạn nhạc Franz Lehár"),
    ("070211", "leukocytoses", "noun", "/ˌluːkoʊsaɪˈtoʊsiːz/", "tình trạng tăng bạch cầu trong máu"),
    ("070212", "liliaceaes", "noun", "/ˌlɪliˈeɪʃiˌiːz/", "họ Bách hợp (họ Loa kèn)"),
    ("070213", "loliums", "noun", "/ˈloʊliəmz/", "cỏ mạch đen thuộc chi Lolium"),
    ("070214", "loziers", "noun", "/ˈloʊʒərz/", "nữ bác sĩ Mỹ Clemence Lozier"),
    ("070215", "malarkies", "noun", "/məˈlɑːrkiz/", "chuyện vớ vẩn nhảm nhí (khẩu ngữ)"),
    ("070216", "mammuts", "noun", "/ˈmæməts/", "chi Voi răng mấu tiền sử Mammut"),
    ("070217", "mantids", "noun", "/ˈmæntɪdz/", "bọ ngựa thuộc họ Mantidae"),
    ("070218", "mashis", "noun", "/ˈmɑːʃiz/", "tiếng Mashi của dân tộc Bantu"),
    ("070219", "mealworms", "noun", "/ˈmiːlˌwɜːrmz/", "sâu gạo (ấu trùng bọ cánh cứng)"),
    ("070220", "mealybugs", "noun", "/ˈmiːliˌbʌɡz/", "rệp sáp trắng hại cây trồng"),
    ("070221", "minahs", "noun", "/ˈmaɪnəz/", "chim sáo sậu hay nói tiếng người"),
    ("070222", "mischances", "noun", "/mɪsˈtʃænsɪz/", "điều rủi ro; sự không may mắn"),
    ("070223", "muchnesses", "noun", "/ˈmʌtʃnəsɪz/", "mức độ nhiều; tính phong phú"),
    ("070224", "muenchens", "noun", "/ˈmjuːnɪks/", "thành phố München ở Đức"),
    ("070225", "nagaris", "noun", "/ˈnɑːɡəriz/", "chữ viết cổ Devanagari Ấn Độ"),
    ("070226", "overnighters", "noun", "/ˌoʊvərˈnaɪtərz/", "khách lưu trú qua đêm; túi du lịch"),
    ("070227", "palestrae", "noun", "/pəˈlɛstriː/", "trường đấu vật Hy Lạp La Mã cổ"),
    ("070228", "palestras", "noun", "/pəˈlɛstrəz/", "trường đấu vật Hy Lạp La Mã cổ"),
    ("070229", "penstemons", "noun", "/ˈpɛnstɪmənz/", "cây hoa chuông râu Penstemon"),
    ("070230", "periapses", "noun", "/ˌpɛriˈæpsiːz/", "điểm cận tâm trên quỹ đạo"),
    ("070231", "phthises", "noun", "/ˈθaɪsiːz/", "bệnh lao phổi; chứng suy mòn"),
    ("070232", "praxiteleses", "noun", "/prækˈsɪtəliːzɪz/", "nhà điêu khắc Hy Lạp Praxiteles"),
    ("070233", "prayas", "noun", "/ˈpreɪəz/", "sứa ống biển sâu thuộc chi Praya"),
    ("070234", "programmas", "noun", "/prəˈɡræməz/", "chương trình; sắc lệnh công bố"),
    ("070235", "quadroons", "noun", "/kwɒˈdruːnz/", "người lai một phần tư gốc Phi"),
    ("070236", "radiocommunications", "noun", "/ˌreɪdioʊkəˌmjuːnɪˈkeɪʃənz/", "liên lạc truyền tin bằng vô tuyến"),
    ("070237", "ramiprils", "noun", "/rəˈmɪprɪlz/", "thuốc hạ huyết áp ramipril"),
    ("070238", "remicades", "noun", "/ˈrɛmɪˌkeɪdz/", "thuốc sinh học Remicade trị viêm"),
    ("070239", "reseated", "verb", "/riːˈsiːtɪd/", "đã bố trí lại chỗ ngồi; đặt khít"),
    ("070240", "reseating", "verb", "/riːˈsiːtɪŋ/", "đang bố trí lại chỗ ngồi"),
    ("070241", "reseats", "verb", "/riːˈsiːts/", "bố trí lại chỗ ngồi; đặt khít lại"),
    ("070242", "rhodonites", "noun", "/ˈroʊdəˌnaɪts/", "khoáng vật đá hồng ngọc rhodonite"),
    ("070243", "sapsuckers", "noun", "/ˈsæpˌsʌkərz/", "chim gõ kiến hút nhựa cây Bắc Mỹ"),
    ("070244", "sarazens", "noun", "/ˈsærəzənz/", "tay gôn Gene Sarazen; người Ả Rập"),
    ("070245", "sfaxes", "noun", "/sfæksɪz/", "thành phố cảng Sfax ở Tunisia"),
    ("070246", "simnels", "noun", "/ˈsɪmnəlz/", "bánh hoa quả hạnh nhân Simnel"),
    ("070247", "simoleonses", "noun", "/sɪˈmoʊliənzɪz/", "đồng đô la Mỹ; tiền bạc (lóng Mỹ)"),
    ("070248", "smidgeons", "noun", "/ˈsmɪdʒənz/", "một chút xíu; một lượng rất nhỏ"),
    ("070249", "spermacetis", "noun", "/ˌspɜːrməˈsɛtiz/", "chất sáp cá nhà táng (mỹ phẩm)"),
    ("070250", "streusels", "noun", "/ˈstruːsəlz/", "vụn bơ đường rắc mặt bánh nướng"),
    ("070251", "stridors", "noun", "/ˈstraɪdərz/", "tiếng thở rít do hẹp đường thở"),
    ("070252", "taboras", "noun", "/təˈbɔːrəz/", "thành phố Tabora ở Tanzania"),
    ("070253", "tackers", "noun", "/ˈtækərz/", "máy bắn ghim; người khâu lược"),
    ("070254", "telefilms", "noun", "/ˈtɛlɪˌfɪlmz/", "phim sản xuất cho truyền hình"),
    ("070255", "temporalises", "verb", "/ˈtɛmpərəˌlaɪzɪz/", "thế tục hóa; làm tạm thời (Anh)"),
    ("070256", "threadier", "adj", "/ˈθrɛdiər/", "mảnh như sợi hơn; xơ xác sờn hơn"),
    ("070257", "threadiest", "adj", "/ˈθrɛdiɪst/", "mảnh như sợi nhất; xơ xác sờn nhất"),
    ("070258", "thymosins", "noun", "/ˈθaɪməsɪnz/", "hoóc-môn tuyến ức thymosin"),
    ("070259", "tradescantias", "noun", "/ˌtrædɪˈskænʃəz/", "cây thài lài tím chi Tradescantia"),
    ("070260", "transferrals", "noun", "/trænsˈfɜːrəlz/", "sự chuyển nhượng; sự bàn giao"),
    ("070261", "turduses", "noun", "/ˈtɜːrdəsɪz/", "chim hoét thuộc chi Turdus"),
    ("070262", "vineries", "noun", "/ˈvaɪnəriz/", "vườn trồng nho; nhà kính trồng nho"),
    ("070263", "vitrectomies", "noun", "/vɪˈtrɛktəmiz/", "phẫu thuật cắt dịch kính mắt"),
    ("070264", "washstands", "noun", "/ˈwɒʃˌstændz/", "bàn đặt chậu rửa mặt cổ điển"),
    ("070265", "woollcotts", "noun", "/ˈwʊlkəts/", "nhà phê bình Alexander Woollcott"),
    ("070266", "xenotransplantations", "noun", "/ˌzɛnoʊtrænzplænˈteɪʃənz/", "cấy ghép dị chủng khác loài"),
    ("070267", "anonyms", "noun", "/ˈænənɪmz/", "người ẩn danh; tác phẩm khuyết danh"),
    ("070268", "aplasias", "noun", "/əˈpleɪʒəz/", "chứng bất sản (cơ quan không tạo)"),
    ("070269", "arachnidas", "noun", "/əˈræknɪdəz/", "lớp Hình nhện (nhện, bọ cạp, ve)"),
    ("070270", "attenders", "noun", "/əˈtɛndərz/", "người tham dự; người chăm sóc"),
    ("070271", "autoloaders", "noun", "/ˈɔːtoʊˌloʊdərz/", "cơ cấu nạp đạn tự động"),
    ("070272", "axils", "noun", "/ˈæksəlz/", "nách lá nơi cuống gắn vào thân"),
    ("070273", "baldheads", "noun", "/ˈbɔːldˌhɛdz/", "người bị hói đầu hoặc cạo trọc"),
    ("070274", "barnstormers", "noun", "/ˈbɑːrnˌstɔːrmərz/", "đoàn lưu diễn; phi công biểu diễn"),
    ("070275", "benzoquinones", "noun", "/ˌbɛnzoʊkwɪˈnoʊnz/", "hợp chất hữu cơ vòng benzoquinone"),
    ("070276", "bethinking", "verb", "/bɪˈθɪŋkɪŋ/", "đang suy nghĩ lại; đang tự nhủ"),
    ("070277", "bethinks", "verb", "/bɪˈθɪŋks/", "suy nghĩ kỹ lại; chợt nhớ ra"),
    ("070278", "bleriots", "noun", "/ˈblɛrioʊz/", "kỹ sư hàng không Louis Blériot"),
    ("070279", "blinis", "noun", "/ˈbliːniz/", "bánh kếp blini truyền thống Nga"),
    ("070280", "bultmanns", "noun", "/ˈbʊltmənz/", "nhà thần học Đức Rudolf Bultmann"),
    ("070281", "cabotages", "noun", "/ˈkæbətɪdʒɪz/", "vận tải ven biển nội địa; cabotage"),
    ("070282", "camelinas", "noun", "/ˌkæməˈliːnəz/", "cây cải dầu lanh chi Camelina"),
    ("070283", "cannulations", "noun", "/ˌkænjʊˈleɪʃənz/", "kỹ thuật đặt ống thông y tế"),
    ("070284", "cercosporas", "noun", "/ˌsɜːrkəˈspɔːrəz/", "nấm gây bệnh đốm lá Cercospora"),
    ("070285", "chironomuses", "noun", "/ˌkaɪrəˈnoʊməsɪz/", "muỗi lắc không đốt chi Chironomus"),
    ("070286", "claudications", "noun", "/ˌklɔːdɪˈkeɪʃənz/", "chứng đau cách hồi khi đi lại"),
    ("070287", "clearways", "noun", "/ˈklɪərˌweɪz/", "tuyến đường cấm dừng đỗ xe"),
    ("070288", "cnidarias", "noun", "/naɪˈdɛəriəz/", "ngành Thích ty bào (sứa, san hô)"),
    ("070289", "colocasias", "noun", "/ˌkɒləˈkeɪʒəz/", "cây khoai môn thuộc chi Colocasia"),
    ("070290", "cotangents", "noun", "/koʊˈtændʒənts/", "hàm lượng giác côtang (cot)"),
    ("070291", "crohns", "noun", "/kroʊnz/", "bác sĩ tiêu hóa Burrill B. Crohn"),
    ("070292", "densitometries", "noun", "/ˌdɛnsɪˈtɒmɪtriz/", "phép đo mật độ quang hoặc xương"),
    ("070293", "deoxyriboses", "noun", "/diˌɒksiˈraɪboʊsɪz/", "đường năm cacbon cấu tạo ADN"),
    ("070294", "dhaks", "noun", "/dɑːks/", "cây rừng hoa đỏ dhak Ấn Độ"),
    ("070295", "disingenuousnesses", "noun", "/ˌdɪsɪnˈdʒɛnjʊəsnəsɪz/", "sự giả tạo thiếu thành thật"),
    ("070296", "drmses", "noun", "/ˌdiː ɑːr ɛm ˈɛsɪz/", "hệ quản lý tài nguyên DRM (Mỹ)"),
    ("070297", "dysgeneses", "noun", "/dɪsˈdʒɛnɪˌsiːz/", "chứng loạn sản cơ quan (y học)"),
    ("070298", "emersions", "noun", "/ɪˈmɜːrʒənz/", "sự ló ra lại sau khi bị che khuất"),
    ("070299", "euphorbiaceaes", "noun", "/juːˌfɔːrbiˈeɪʃiˌiːz/", "họ Thầu dầu thực vật (Euphorbia)"),
    ("070300", "exceedances", "noun", "/ɪkˈsiːdənsɪz/", "mức độ vượt ngưỡng cho phép"),
    ("070301", "flyswatters", "noun", "/ˈflaɪˌswɒtərz/", "cây vỉ đập ruồi muỗi"),
    ("070302", "frottages", "noun", "/frəˈtɑːʒɪz/", "kỹ thuật cà giấy lấy vân; sự cọ xát"),
]

with open("scratch/b35_r01_raw_p3.json") as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100
allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}
out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, items):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} != {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} != {hw}"
    assert pos in allowed_pos, f"Bad POS: {pos}"
    assert len(vi) <= 35, f"VI too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA: {hw} -> {ipa}"
    assert not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"Space in IPA: {hw} -> {ipa}"
    out.append({**r, "pos": pos, "ipa": ipa, "vi": vi, "status": "reviewed"})

with open("scratch/b35_r01_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r01_p3.json OK")
