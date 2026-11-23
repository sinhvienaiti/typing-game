import json

records = [
    ("079003", "preternaturalism", "noun", "/ˌpriːtərˈnætʃərəˌlɪzəm/", "tính chất siêu nhiên, thuyết kỳ bí"),
    ("079004", "preternaturalness", "noun", "/ˌpriːtərˈnætʃərəlnəs/", "tính phi thường, vẻ siêu nhiên"),
    ("079005", "preterpluperfect", "noun", "/ˌpriːtərˌpluːˈpɜːrfɪkt/", "thì quá khứ hoàn thành (ngữ pháp)"),
    ("079006", "pretersensual", "adj", "/ˌpriːtərˈsɛnʃuəl/", "siêu cảm giác, vượt ngoài giác quan"),
    ("079007", "pretest", "noun", "/ˈpriːtɛst/", "bài kiểm tra trước, đợt sơ khảo"),
    ("079008", "pretested", "verb", "/ˌpriːˈtɛstɪd/", "đã kiểm tra trước, đã thử trước"),
    ("079009", "pretesticular", "adj", "/ˌpriːtɛˈstɪkjələr/", "trước tinh hoàn (giải phẫu)"),
    ("079010", "pretesting", "verb", "/ˌpriːˈtɛstɪŋ/", "kiểm tra trước, thử nghiệm trước"),
    ("079011", "pretests", "verb", "/ˌpriːˈtɛsts/", "kiểm tra trước, thử nghiệm trước"),
    ("079012", "pretexted", "verb", "/ˈpriːtɛkstɪd/", "đã lấy cớ, đã viện cớ"),
    ("079013", "pretexting", "verb", "/ˈpriːtɛkstɪŋ/", "lấy cớ, viện cớ (mạo danh dò tin)"),
    ("079014", "pretexts", "verb", "/ˈpriːtɛksts/", "lấy cớ, viện cớ"),
    ("079015", "pretibial", "adj", "/ˌpriːˈtɪbiəl/", "trước xương chày (giải phẫu)"),
    ("079016", "pretone", "noun", "/ˈpriːtoʊn/", "âm tiết ngay trước trọng âm"),
    ("079017", "pretonic", "adj", "/ˌpriːˈtɑːnɪk/", "trước trọng âm (ngữ âm học)"),
    ("079018", "pretorial", "adj", "/prɪˈtɔːriəl/", "thuộc pháp quan La Mã cổ đại"),
    ("079019", "pretorium", "noun", "/prɪˈtɔːriəm/", "dinh thống đốc; lều tướng La Mã"),
    ("079020", "prettification", "noun", "/ˌprɪtɪfɪˈkeɪʃən/", "sự tô điểm, sự làm đẹp thêm"),
    ("079021", "prettified", "verb", "/ˈprɪtɪˌfaɪd/", "đã tô điểm, đã làm đẹp thêm"),
    ("079022", "prettifier", "noun", "/ˈprɪtɪˌfaɪər/", "người tô điểm; công cụ định dạng"),
    ("079023", "prettifies", "verb", "/ˈprɪtɪˌfaɪz/", "tô điểm, làm đẹp thêm"),
    ("079024", "prettifying", "verb", "/ˈprɪtɪˌfaɪɪŋ/", "tô điểm, làm đẹp thêm"),
    ("079025", "prettyish", "adj", "/ˈprɪtiɪʃ/", "xinh xắn, hơi xinh, dễ thương"),
    ("079026", "pretuning", "noun", "/ˌpriːˈtuːnɪŋ/", "sự điều chỉnh trước, chỉnh sơ bộ"),
    ("079027", "pretzels", "noun", "/ˈprɛtsəlz/", "bánh quy xoắn giòn"),
    ("079028", "prevailed", "verb", "/prɪˈveɪld/", "đã thắng thế; đã thuyết phục"),
    ("079029", "prevailer", "noun", "/prɪˈveɪlər/", "người thắng thế, người chiếm ưu thế"),
    ("079030", "prevailingly", "adv", "/prɪˈveɪlɪŋli/", "phổ biến, thịnh hành, chủ yếu"),
    ("079031", "prevailingness", "noun", "/prɪˈveɪlɪŋnəs/", "tính phổ biến, sự thịnh hành"),
    ("079032", "prevails", "verb", "/prɪˈveɪlz/", "thắng thế, thịnh hành; thuyết phục"),
    ("079033", "prevalently", "adv", "/ˈprɛvələntli/", "một cách phổ biến, thịnh hành"),
    ("079034", "prevaricated", "verb", "/prəˈvɛrəˌkeɪtɪd/", "đã nói quanh co, đã lảng tránh"),
    ("079035", "prevaricates", "verb", "/prəˈvɛrəˌkeɪts/", "nói quanh co, lảng tránh sự thật"),
    ("079036", "prevaricating", "verb", "/prəˈvɛrəˌkeɪtɪŋ/", "nói quanh co, lảng tránh sự thật"),
    ("079037", "prevaricator", "noun", "/prəˈvɛrəˌkeɪtər/", "kẻ nói quanh co, kẻ lươn lẹo"),
    ("079038", "prevenance", "noun", "/ˈprɛvənəns/", "sự ân cần chu đáo, sự lo trước"),
    ("079039", "preveniently", "adv", "/prɪˈviːniəntli/", "đi trước, dự phòng trước"),
    ("079040", "preventability", "noun", "/prɪˌvɛntəˈbɪləti/", "tính có thể phòng ngừa được"),
    ("079041", "preventatives", "noun", "/prɪˈvɛntətɪvz/", "thuốc phòng bệnh; biện pháp ngừa"),
    ("079042", "prevented", "verb", "/prɪˈvɛntɪd/", "đã ngăn chặn, đã phòng ngừa"),
    ("079043", "preventer", "noun", "/prɪˈvɛntər/", "người ngăn cản; dây giằng phụ"),
    ("079044", "preventibility", "noun", "/prɪˌvɛntəˈbɪləti/", "tính có thể ngăn ngừa được"),
    ("079045", "preventible", "adj", "/prɪˈvɛntəbəl/", "có thể ngăn ngừa, có thể tránh"),
    ("079046", "preventing", "verb", "/prɪˈvɛntɪŋ/", "ngăn chặn, cản trở, phòng ngừa"),
    ("079047", "preventively", "adv", "/prɪˈvɛntɪvli/", "nhằm phòng ngừa, mang tính dự phòng"),
    ("079048", "preventiveness", "noun", "/prɪˈvɛntɪvnəs/", "tính chất phòng ngừa, sự dự phòng"),
    ("079049", "preventorium", "noun", "/ˌpriːvɛnˈtɔːriəm/", "viện điều dưỡng phòng lao (lịch sử)"),
    ("079050", "prevents", "verb", "/prɪˈvɛnts/", "ngăn chặn, cản trở, phòng ngừa"),
    ("079051", "prevenules", "noun", "/priːˈvɛnjuːlz/", "tiểu tĩnh mạch sơ cấp (giải phẫu)"),
    ("079052", "prevernal", "adj", "/ˌpriːˈvɜːrnəl/", "đầu mùa xuân, trước tiết xuân"),
    ("079053", "prevertebral", "adj", "/ˌpriːˈvɜːrtəbrəl/", "trước cột sống (giải phẫu)"),
    ("079054", "prevesical", "adj", "/ˌpriːˈvɛsɪkəl/", "trước bàng quang (giải phẫu)"),
    ("079055", "previewed", "verb", "/ˈpriːvjuːd/", "đã xem trước, đã duyệt trước"),
    ("079056", "previewing", "verb", "/ˈpriːvjuːɪŋ/", "xem trước, chiếu thử, duyệt trước"),
    ("079057", "previews", "verb", "/ˈpriːvjuːz/", "xem trước, chiếu thử, giới thiệu"),
    ("079058", "previousness", "noun", "/ˈpriːviəsnəs/", "sự trước đó; tính hấp tấp vội vàng"),
    ("079059", "previse", "verb", "/prɪˈvaɪz/", "thấy trước, báo trước, cảnh báo"),
    ("079060", "previsional", "adj", "/prɪˈvɪʒənəl/", "thuộc sự dự đoán, thấy trước"),
    ("079061", "previsionary", "adj", "/prɪˈvɪʒəˌnɛri/", "thuộc tiên tri, có tầm nhìn xa"),
    ("079062", "previtamin", "noun", "/ˌpriːˈvaɪtəmɪn/", "tiền vitamin, tiền sinh tố"),
    ("079063", "prevocalic", "adj", "/ˌpriːvoʊˈkælɪk/", "đứng trước nguyên âm (ngữ âm)"),
    ("079064", "prevocational", "adj", "/ˌpriːvoʊˈkeɪʃənəl/", "hướng nghiệp sơ bộ, tiền nghề"),
    ("079065", "prewarn", "verb", "/ˌpriːˈwɔːrn/", "cảnh báo trước, báo động trước"),
    ("079066", "prex", "noun", "/prɛks/", "hiệu trưởng đại học (lóng)"),
    ("079067", "prexie", "noun", "/ˈprɛksi/", "tem thư loạt Tổng thống Mỹ 1938"),
    ("079068", "prexies", "noun", "/ˈprɛksiz/", "các con tem loạt Tổng thống Mỹ"),
    ("079069", "preyer", "noun", "/ˈpreɪər/", "động vật săn mồi; kẻ săn bắt"),
    ("079070", "prezzie", "noun", "/ˈprɛzi/", "quà tặng (thân mật)"),
    ("079071", "priacanthidae", "noun", "/ˌpraɪəˈkænθɪˌdiː/", "họ cá trác, họ cá mắt to"),
    ("079072", "priacanthus", "noun", "/ˌpraɪəˈkænθəs/", "chi cá trác, chi cá mắt to"),
    ("079073", "priapean", "adj", "/ˌpraɪəˈpiːən/", "thuộc thần sinh thực; tục tĩu"),
    ("079074", "priappus", "noun", "/praɪˈeɪpəs/", "thần sinh thực nam (thần thoại)"),
    ("079075", "priceable", "adj", "/ˈpraɪsəbəl/", "có thể định giá được"),
    ("079076", "priced", "adj", "/praɪst/", "có định giá, có gắn nhãn giá"),
    ("079077", "pricelessly", "adv", "/ˈpraɪsləsli/", "hài hước khó tin; vô cùng quý giá"),
    ("079078", "pricelessness", "noun", "/ˈpraɪsləsnəs/", "sự vô giá; tính khôi hài hết sức"),
    ("079079", "priceyness", "noun", "/ˈpraɪsinəs/", "sự đắt đỏ, giá cả cao"),
    ("079080", "pricily", "adv", "/ˈpraɪsɪli/", "một cách đắt đỏ, với giá cao"),
    ("079081", "pricked", "verb", "/prɪkt/", "đã chích, đã đâm; đã dựng tai"),
    ("079082", "pricket", "noun", "/ˈprɪkɪt/", "chân cắm nến; hươu đực hai tuổi"),
    ("079083", "prickets", "noun", "/ˈprɪkɪts/", "những chân cắm nến; hươu hai tuổi"),
    ("079084", "prickleback", "noun", "/ˈprɪkəlˌbæk/", "cá gai biển (họ Stichaeidae)"),
    ("079085", "prickled", "verb", "/ˈprɪkəld/", "đã châm chích; đã nổi gai ốc"),
    ("079086", "prickles", "verb", "/ˈprɪkəlz/", "châm chích, ngứa ran, nổi gai"),
    ("079087", "prickliness", "noun", "/ˈprɪklinəs/", "tính đầy gai; tính hay cáu gắt"),
    ("079088", "pricks", "verb", "/prɪks/", "chích, đâm, châm; dựng (tai)"),
    ("079089", "prickteaser", "noun", "/ˈprɪkˌtiːzər/", "người tán tỉnh nhưng khước từ"),
    ("079090", "pridefully", "adv", "/ˈpraɪdfəli/", "một cách kiêu hãnh, tự hào"),
    ("079091", "pridefulness", "noun", "/ˈpraɪdfəlnəs/", "lòng kiêu hãnh, tính tự phụ"),
    ("079092", "pried", "verb", "/praɪd/", "đã cạy, đã bẩy; đã tọc mạch dò xét"),
    ("079093", "prier", "noun", "/ˈpraɪər/", "người tò mò, kẻ hay tọc mạch"),
    ("079094", "pries", "verb", "/praɪz/", "cạy, bẩy; tọc mạch, dò xét"),
    ("079095", "priestlike", "adj", "/ˈpriːstˌlaɪk/", "giống linh mục, vẻ đạo mạo"),
    ("079096", "priestliness", "noun", "/ˈpriːstlinəs/", "phong thái linh mục, vẻ đạo mạo"),
    ("079097", "priests", "noun", "/priːsts/", "các linh mục, thầy tu, tăng lữ"),
    ("079098", "priggery", "noun", "/ˈprɪɡəri/", "thói làm bộ đạo đức, vẻ tự mãn"),
    ("079099", "priggishly", "adv", "/ˈprɪɡɪʃli/", "một cách hợm hĩnh, câu nệ"),
    ("079100", "priggishness", "noun", "/ˈprɪɡɪʃnəs/", "tính hợm hĩnh, thói tự cao tự đại"),
    ("079101", "priggism", "noun", "/ˈprɪɡˌɪzəm/", "thói hợm hĩnh, lối sống câu nệ"),
    ("079102", "primaeval", "adj", "/praɪˈmiːvəl/", "nguyên thủy, thái cổ, ban sơ"),
]

raw = json.load(open("scratch/b36_r09_raw_p1.json"))
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
with open("scratch/b36_r09_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b36_r09_p1 saved OK")
