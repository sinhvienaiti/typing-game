import json

records = [
    ("081103", "quickshot", "noun", "/ˈkwɪkˌʃɑːt/", "người xuất tinh sớm (khẩu ngữ)"),
    ("081104", "quickshots", "noun", "/ˈkwɪkˌʃɑːts/", "người xuất tinh sớm (khẩu ngữ)"),
    ("081105", "quickthorn", "noun", "/ˈkwɪkˌθɔːrn/", "cây táo gai làm hàng rào (Anh)"),
    ("081106", "quickwitted", "adj", "/ˌkwɪkˈwɪtɪd/", "nhanh trí, ứng đối lanh lợi"),
    ("081107", "quictlaim", "noun", "/ˈkwɪtˌkleɪm/", "giấy từ bỏ quyền sở hữu (lỗi viết)"),
    ("081108", "quidam", "noun", "/ˈkwaɪdəm/", "một người vô danh nào đó (Latin)"),
    ("081109", "quidative", "adj", "/ˈkwɪdətɪv/", "thuộc bản chất cốt lõi (triết học)"),
    ("081110", "quidditch", "noun", "/ˈkwɪdɪtʃ/", "môn thể thao chổi bay Quidditch"),
    ("081111", "quiddle", "verb", "/ˈkwɪdəl/", "làm việc vặt vãnh tốn thì giờ"),
    ("081112", "quidnunc", "noun", "/ˈkwɪdˌnʌŋk/", "kẻ hay hóng chuyện, tọc mạch"),
    ("081113", "quiesce", "verb", "/kwaɪˈɛs/", "trở nên yên ắng, ngừng hoạt động"),
    ("081114", "quiescency", "noun", "/kwaɪˈɛsənsi/", "trạng thái tĩnh lặng, sự yên nghỉ"),
    ("081115", "quieted", "verb", "/ˈkwaɪətɪd/", "đã làm yên tĩnh, đã xoa dịu êm ả"),
    ("081116", "quietened", "verb", "/ˈkwaɪətənd/", "đã im ắng lại, đã làm dịu đi (Anh)"),
    ("081117", "quietening", "verb", "/ˈkwaɪətənɪŋ/", "trở nên yên ắng, làm dịu đi (Anh)"),
    ("081118", "quietens", "verb", "/ˈkwaɪətənz/", "làm yên ắng, dịu lại dần (Anh)"),
    ("081119", "quieting", "verb", "/ˈkwaɪətɪŋ/", "làm yên tĩnh, trấn an, vỗ về êm dịu"),
    ("081120", "quietive", "adj", "/ˈkwaɪətɪv/", "có tác dụng làm dịu, an thần"),
    ("081121", "quiets", "verb", "/ˈkwaɪəts/", "làm yên tĩnh, trấn tĩnh, xoa dịu"),
    ("081122", "quiller", "noun", "/ˈkwɪlər/", "máy đánh ống sợi ngang (ngành dệt)"),
    ("081123", "quillet", "noun", "/ˈkwɪlɪt/", "lý sự cùn, chi tiết bắt bẻ câu chữ"),
    ("081124", "quilling", "noun", "/ˈkwɪlɪŋ/", "nếp xếp tổ ong; thuật xoắn giấy"),
    ("081125", "quillons", "noun", "/ˈkwɪlənz/", "hai nhánh chắn tay chuôi kiếm"),
    ("081126", "quillwort", "noun", "/ˈkwɪlˌwɜːrt/", "cây thủy cửu (họ Thông đất nước)"),
    ("081127", "quilts", "verb", "/kwɪlts/", "chần bông (chăn mền), khâu ghép"),
    ("081128", "quim", "noun", "/kwɪm/", "bộ phận sinh dục nữ (tiếng lóng)"),
    ("081129", "quina", "noun", "/ˈkiːnə/", "vỏ cây canh-ki-na (chế ký ninh)"),
    ("081130", "quinary", "adj", "/ˈkwaɪnəri/", "gồm năm phần, theo hệ cơ số năm"),
    ("081131", "quinate", "adj", "/ˈkwaɪnət/", "có năm lá chét mọc cùng cuống"),
    ("081132", "quinceaneras", "noun", "/ˌkiːnseɪˈnjɛrəs/", "tiệc mừng tuổi 15 thiếu nữ Mỹ Latin"),
    ("081133", "quincenterany", "adj", "/kwɪnˈsɛntənəri/", "kỷ niệm năm trăm năm (biến thể)"),
    ("081134", "quincunces", "noun", "/ˈkwɪŋkʌnsɪz/", "các kiểu xếp năm điểm hình chữ ngũ"),
    ("081135", "quincuncial", "adj", "/kwɪnˈkʌnʃəl/", "xếp theo hình chữ ngũ (nanh sấu)"),
    ("081136", "quincunx", "noun", "/ˈkwɪŋkʌŋks/", "cách xếp năm điểm hình nanh sấu"),
    ("081137", "quincunxes", "noun", "/ˈkwɪŋkʌŋksɪz/", "các cách xếp năm điểm hình chữ ngũ"),
    ("081138", "quindecillion", "noun", "/ˌkwɪndɛˈsɪljən/", "số 10 lũy thừa 48 (quindecillion)"),
    ("081139", "quindecillions", "noun", "/ˌkwɪndɛˈsɪljənz/", "hàng quindecillion (10 mũ 48)"),
    ("081140", "quingagesima", "noun", "/ˌkwɪŋɡəˈdʒɛsəmə/", "Chủ nhật thứ 50 trước Lễ Phục sinh"),
    ("081141", "quingentenary", "adj", "/ˌkwɪndʒɛnˈtɛnəri/", "thuộc lễ kỷ niệm năm trăm năm"),
    ("081142", "quinia", "noun", "/ˈkwɪniə/", "chất ký ninh (thuốc trị sốt rét cổ)"),
    ("081143", "quinic", "adj", "/ˈkwɪnɪk/", "thuộc axit quinic (vỏ canh-ki-na)"),
    ("081144", "quinidex", "noun", "/ˈkwɪnəˌdɛks/", "thuốc chống loạn nhịp quinidine"),
    ("081145", "quinism", "noun", "/ˈkwaɪˌnɪzəm/", "chứng ngộ độc ký ninh (ù tai)"),
    ("081146", "quinize", "verb", "/ˈkwaɪˌnaɪz/", "điều trị bằng thuốc ký ninh"),
    ("081147", "quinoas", "noun", "/ˈkiːnwɑːz/", "các loại hạt diêm mạch quinoa"),
    ("081148", "quinora", "noun", "/kwɪˈnɔːrə/", "thuốc trị loạn nhịp tim quinidine"),
    ("081149", "quinquagenarian", "noun", "/ˌkwɪŋkwədʒəˈnɛriən/", "người ở độ tuổi 50 đến 59"),
    ("081150", "quinquagenary", "adj", "/kwɪŋˈkwædʒəˌnɛri/", "thuộc năm mươi năm, kỷ niệm 50 năm"),
    ("081151", "quinquagesima", "noun", "/ˌkwɪŋkwəˈdʒɛsəmə/", "Chủ nhật cuối trước Thứ tư Lễ Tro"),
    ("081152", "quinquagular", "adj", "/kwɪŋˈkwæŋɡjələr/", "có năm góc, hình ngũ giác (lỗi)"),
    ("081153", "quinquefarious", "adj", "/ˌkwɪŋkwəˈfɛriəs/", "xếp thành năm hàng dọc (thực vật)"),
    ("081154", "quinquefid", "adj", "/ˈkwɪŋkwəˌfɪd/", "xẻ thành năm thùy sâu (lá, đài hoa)"),
    ("081155", "quinquefoliate", "adj", "/ˌkwɪŋkwəˈfoʊliət/", "có năm lá chét (thực vật học)"),
    ("081156", "quinqueliteral", "adj", "/ˌkwɪŋkwəˈlɪtərəl/", "gồm năm chữ cái (ngôn ngữ học)"),
    ("081157", "quinquennia", "noun", "/kwɪŋˈkwɛniə/", "những khoảng thời gian năm năm"),
    ("081158", "quinquennial", "adj", "/kwɪŋˈkwɛniəl/", "kéo dài năm năm; năm năm một lần"),
    ("081159", "quinquennium", "noun", "/kwɪŋˈkwɛniəm/", "khoảng thời gian năm năm, ngũ niên"),
    ("081160", "quinquepartite", "adj", "/ˌkwɪŋkwəˈpɑːrtaɪt/", "chia làm năm phần, gồm năm nước"),
    ("081161", "quinquereme", "noun", "/ˈkwɪŋkwəˌriːm/", "chiến thuyền năm tầng chèo cổ đại"),
    ("081162", "quinquesect", "verb", "/ˈkwɪŋkwəˌsɛkt/", "chia thành năm phần bằng nhau"),
    ("081163", "quinquesyllable", "noun", "/ˌkwɪŋkwəˈsɪləbəl/", "từ gồm năm âm tiết"),
    ("081164", "quinquevalence", "noun", "/ˌkwɪŋkwəˈveɪləns/", "hóa trị năm (hóa học)"),
    ("081165", "quinquevalency", "noun", "/ˌkwɪŋkwəˈveɪlənsi/", "tính hóa trị năm (hóa học)"),
    ("081166", "quinquevalent", "adj", "/ˌkwɪŋkwəˈveɪlənt/", "có hóa trị năm (hóa học)"),
    ("081167", "quinquevalve", "adj", "/ˈkwɪŋkwəˌvælv/", "có năm van, năm mảnh vỏ (sinh học)"),
    ("081168", "quinquina", "noun", "/kɪŋˈkiːnə/", "cây canh-ki-na, vỏ canh-ki-na"),
    ("081169", "quinquivalence", "noun", "/kwɪŋˈkwɪvələns/", "hóa trị năm (hóa học)"),
    ("081170", "quinquivalency", "noun", "/kwɪŋˈkwɪvələnsi/", "tính hóa trị năm (hóa học)"),
    ("081171", "quinquivalent", "adj", "/kwɪŋˈkwɪvələnt/", "có hóa trị năm (hóa học)"),
    ("081172", "quins", "noun", "/kwɪnz/", "ca sinh năm (năm trẻ sinh cùng lúc)"),
    ("081173", "quintan", "adj", "/ˈkwɪntən/", "xảy ra cứ mỗi năm ngày (cơn sốt)"),
    ("081174", "quintessentially", "adv", "/ˌkwɪntɪˈsɛnʃəli/", "tinh túy nhất, điển hình nhất"),
    ("081175", "quintic", "adj", "/ˈkwɪntɪk/", "bậc năm (đa thức, phương trình)"),
    ("081176", "quintile", "noun", "/ˈkwɪntaɪl/", "ngũ phân vị, một phần năm"),
    ("081177", "quintillions", "noun", "/kwɪnˈtɪljənz/", "hàng tỷ tỷ (Mỹ, 10 mũ 18)"),
    ("081178", "quintillionth", "adj", "/kwɪnˈtɪljənθ/", "thứ một tỷ tỷ (10 mũ 18)"),
    ("081179", "quintipara", "noun", "/kwɪnˈtɪpərə/", "sản phụ sinh con lần thứ năm"),
    ("081180", "quints", "noun", "/kwɪnts/", "ca sinh năm (năm đứa trẻ sinh năm)"),
    ("081181", "quintupled", "verb", "/ˈkwɪntʊpəld/", "đã tăng gấp năm lần, nhân năm"),
    ("081182", "quintuples", "verb", "/ˈkwɪntʊpəlz/", "tăng gấp năm lần, nhân năm"),
    ("081183", "quintuplicate", "adj", "/kwɪnˈtuːpləkət/", "gồm năm bản giống nhau, gấp năm"),
    ("081184", "quintuply", "adv", "/ˈkwɪntʊpli/", "gấp năm lần, thành năm bản"),
    ("081185", "quira", "noun", "/ˈkiːrə/", "cây gỗ đỏ Panama (Platymiscium)"),
    ("081186", "quirinal", "noun", "/ˈkwɪrənəl/", "phủ tổng thống Ý; chính phủ Ý"),
    ("081187", "quisby", "adj", "/ˈkwɪzbi/", "đáng ngờ, mờ ám; không làm việc"),
    ("081188", "quiscalus", "noun", "/ˈkwɪskələs/", "chi chim sáo đen đuôi thuyền Bắc Mỹ"),
    ("081189", "quisle", "verb", "/ˈkwɪzəl/", "làm tay sai phản bội tổ quốc"),
    ("081190", "quislingism", "noun", "/ˈkwɪzlɪŋˌɪzəm/", "hành vi phản quốc theo giặc"),
    ("081191", "quitch", "noun", "/kwɪtʃ/", "cỏ gấu mì dại (loài cỏ dại dai sức)"),
    ("081192", "quiting", "verb", "/ˈkwɪtɪŋ/", "từ bỏ, nghỉ việc (biến thể sai chữ)"),
    ("081193", "quitrent", "noun", "/ˈkwɪtˌrɛnt/", "tô cố định miễn lao dịch"),
    ("081194", "quittance", "noun", "/ˈkwɪtəns/", "giấy miễn nợ, biên nhận thanh toán"),
    ("081195", "quitted", "verb", "/ˈkwɪtɪd/", "đã từ bỏ, đã nghỉ việc, đã rời đi"),
    ("081196", "quittor", "noun", "/ˈkwɪtər/", "bệnh rò mủ móng ngựa (thú y)"),
    ("081197", "quivered", "verb", "/ˈkwɪvərd/", "đã run rẩy, đã rung động khẽ"),
    ("081198", "quiverful", "noun", "/ˈkwɪvərˌfʊl/", "một ống đầy tên; gia đình đông con"),
    ("081199", "quivers", "verb", "/ˈkwɪvərz/", "run rẩy, rung nhẹ, rùng mình"),
    ("081200", "quivive", "noun", "/ˌkiːˈviːv/", "tư thế cảnh giác cao độ (khẩu ngữ)"),
    ("081201", "quixote", "noun", "/kiːˈhoʊti/", "người hảo tâm mơ mộng viển vông"),
    ("081202", "quixotics", "noun", "/kwɪkˈsɑːtɪks/", "tính hào hiệp mơ mộng phi thực tế"),
]

raw = json.load(open("scratch/b37_r03_raw_p2.json"))
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
with open("scratch/b37_r03_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r03_p2 saved OK")
