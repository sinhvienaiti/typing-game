import json

items = [
    ("068703", "poincianas", "noun", "/ˌpɔɪnsiˈænəz/", "cây phượng vĩ; cây điệp hoa đỏ"),
    ("068704", "purgations", "noun", "/pɜːrˈɡeɪʃənz/", "sự thanh tẩy tội lỗi; sự tẩy ruột"),
    ("068705", "quadrics", "noun", "/ˈkwɒdrɪks/", "mặt bậc hai trong không gian"),
    ("068706", "rales", "noun", "/rɑːlz/", "tiếng ran bất thường khi nghe phổi"),
    ("068707", "ramekins", "noun", "/ˈræmɪkɪnz/", "chén sứ nhỏ chịu nhiệt nướng bánh"),
    ("068708", "redactors", "noun", "/rɪˈdæktərz/", "người biên tập hiệu đính văn bản"),
    ("068709", "refractometers", "noun", "/ˌriːfrækˈtɒmɪtərz/", "khúc xạ kế đo chiết suất dung dịch"),
    ("068710", "revalued", "verb", "/riːˈvæljuːd/", "đã định giá lại; đã nâng giá đồng"),
    ("068711", "revalues", "verb", "/riːˈvæljuːz/", "định giá lại tài sản; nâng tỷ giá"),
    ("068712", "revaluing", "verb", "/riːˈvæljuːɪŋ/", "đang định giá lại; nâng giá tiền tệ"),
    ("068713", "salyuts", "noun", "/sælˈjuːts/", "trạm không gian Liên Xô Salyut"),
    ("068714", "savarins", "noun", "/ˈsævərɪnz/", "bánh ngọt hình nhẫn tẩm rượu rum"),
    ("068715", "sciaras", "noun", "/saɪˈɛərəz/", "chi ruồi nhỏ ăn nấm Sciara"),
    ("068716", "shingons", "noun", "/ˈʃɪŋɡɒnz/", "Mật tông Chân Ngôn của Nhật Bản"),
    ("068717", "sigmoidoscopies", "noun", "/ˌsɪɡmɔɪˈdɒskəpiz/", "nội soi đại tràng sigma bằng ống"),
    ("068718", "sippers", "noun", "/ˈsɪpərz/", "người nhấp từng ngụm; ống hút nhỏ"),
    ("068719", "sodomized", "verb", "/ˈsɒdəˌmaɪzd/", "đã giao hợp hậu môn hoặc với thú"),
    ("068720", "sodomizes", "verb", "/ˈsɒdəˌmaɪzɪz/", "giao hợp hậu môn hoặc với động vật"),
    ("068721", "sodomizing", "verb", "/ˈsɒdəˌmaɪzɪŋ/", "đang giao hợp hậu môn hoặc với thú"),
    ("068722", "somnambulists", "noun", "/sɒmˈnæmbjəlɪsts/", "người mắc chứng mộng du đi trong mơ"),
    ("068723", "stigmatisations", "noun", "/ˌstɪɡmətaɪˈzeɪʃənz/", "sự kỳ thị bêu riếu gắn mác xấu"),
    ("068724", "superabundances", "noun", "/ˌsuːpərəˈbʌndənsɪz/", "sự dư thừa quá mức dồi dào tràn"),
    ("068725", "syringas", "noun", "/sɪˈrɪŋɡəz/", "hoa tử đinh hương; hoa mai giả"),
    ("068726", "tarahumaras", "noun", "/ˌtɑːrəhuːˈmɑːrəz/", "người bản địa Tarahumara Mexico"),
    ("068727", "tercels", "noun", "/ˈtɜːrsəlz/", "chim ưng trống dùng trong săn mồi"),
    ("068728", "tideways", "noun", "/ˈtaɪdˌweɪz/", "luồng lạch có dòng thủy triều chảy"),
    ("068729", "tragedians", "noun", "/trəˈdʒiːdiənz/", "nhà viết bi kịch; diễn viên bi kịch"),
    ("068730", "transferors", "noun", "/trænsˈfɜːrərz/", "bên chuyển nhượng tài sản quyền"),
    ("068731", "underclassmen", "noun", "/ˌʌndərˈklæsmən/", "sinh viên năm nhất hoặc năm hai"),
    ("068732", "undershooting", "verb", "/ˌʌndərˈʃuːtɪŋ/", "đang bắn hụt đích; hạ cánh non"),
    ("068733", "undershoots", "verb", "/ˌʌndərˈʃuːts/", "hụt mục tiêu; không đạt mức dự báo"),
    ("068734", "vaudoises", "noun", "/voʊˈdwɑːzɪz/", "giáo phái Kháng Cách Waldensian"),
    ("068735", "vermonters", "noun", "/vərˈmɒntərz/", "người dân bang Vermont của Mỹ"),
    ("068736", "vervets", "noun", "/ˈvɜːrvɪts/", "khỉ vervet mặt đen ở châu Phi"),
    ("068737", "viborgs", "noun", "/ˈviːbɔːrɡz/", "thành phố Viborg ở Đan Mạch"),
    ("068738", "weltanschauungs", "noun", "/ˈvɛltɑːnˌʃaʊʊŋz/", "thế giới quan nhân sinh quan triết"),
    ("068739", "wheatears", "noun", "/ˈwiːtˌɪərz/", "chim đớp ruồi wheatear đít trắng"),
    ("068740", "woodcarvers", "noun", "/ˈwʊdˌkɑːrvərz/", "nghệ nhân chạm khắc đồ gỗ mỹ nghệ"),
    ("068741", "wordnets", "noun", "/ˈwɜːrdˌnɛts/", "mạng ngữ nghĩa từ vựng WordNet"),
    ("068742", "zoophilias", "noun", "/ˌzoʊəˈfɪliəz/", "tình trạng ái thú lệch lạc (y học)"),
    ("068743", "abiogeneses", "noun", "/ˌeɪbaɪoʊˈdʒɛnəsiːz/", "thuyết phát sinh tự nhiên sự sống"),
    ("068744", "achenes", "noun", "/əˈkiːnz/", "quả bế khô một hạt không tự mở"),
    ("068745", "alphabetizes", "verb", "/ˈælfəbəˌtaɪzɪz/", "sắp xếp theo thứ tự bảng chữ cái"),
    ("068746", "alphabetizing", "verb", "/ˈælfəbəˌtaɪzɪŋ/", "đang xếp theo thứ tự bảng chữ cái"),
    ("068747", "amberjacks", "noun", "/ˈæmbərˌdʒæks/", "cá cam biển lớn săn mồi"),
    ("068748", "antiemetics", "noun", "/ˌæntiɪˈmɛtɪks/", "thuốc chống buồn nôn và nôn mửa"),
    ("068749", "antiphonals", "noun", "/ænˈtɪfənəlz/", "sách thánh ca hát đối đáp hợp xướng"),
    ("068750", "aphereses", "noun", "/əˈfɛrəsiːz/", "tách lọc thành phần máu; rụng âm"),
    ("068751", "aristotelianisms", "noun", "/ˌærɪstəˈtiːliənˌɪzəmz/", "triết học chủ nghĩa Aristotle"),
    ("068752", "beguines", "noun", "/bɛˈɡiːnz/", "nữ tu dòng Beguine thời trung cổ"),
    ("068753", "benefactresses", "noun", "/ˌbɛnɪˈfæktrɪsɪz/", "nữ ân nhân mạnh thường quân tài trợ"),
    ("068754", "brachycephalics", "noun", "/ˌbrækɪsəˈfælɪks/", "người hoặc giống có hộp sọ đầu ngắn"),
    ("068755", "bronchodilators", "noun", "/ˌbrɒŋkoʊdaɪˈleɪtərz/", "thuốc làm giãn nở đường phế quản"),
    ("068756", "burnups", "noun", "/ˈbɜːrnˌʌps/", "độ cháy kiệt nhiên liệu hạt nhân"),
    ("068757", "buspirones", "noun", "/bjuːˈspaɪəroʊnz/", "thuốc điều trị lo âu buspiron"),
    ("068758", "caliches", "noun", "/kəˈliːtʃiz/", "tầng đất cứng giàu canxi cacbonat"),
    ("068759", "carabidaes", "noun", "/kəˈræbɪdiːz/", "họ bọ cánh cứng chân chạy Carabidae"),
    ("068760", "caravanserais", "noun", "/ˌkærəˈvænsəˌraɪz/", "lữ quán có sân cho đoàn lữ hành"),
    ("068761", "cauteries", "noun", "/ˈkɔːtəriz/", "dụng cụ đốt cầm máu; chất ăn mòn"),
    ("068762", "charier", "adj", "/ˈtʃɛəriər/", "thận trọng dè dặt cảnh giác hơn"),
    ("068763", "chariest", "adj", "/ˈtʃɛəriɪst/", "thận trọng dè dặt cảnh giác nhất"),
    ("068764", "cobias", "noun", "/ˈkoʊbiəz/", "cá giò; cá bớp biển thân dài"),
    ("068765", "conferments", "noun", "/kənˈfɜːrmənts/", "sự trao tặng bằng cấp; huân chương"),
    ("068766", "connived", "verb", "/kəˈnaɪvd/", "đã dung túng thông đồng âm mưu"),
    ("068767", "connives", "verb", "/kəˈnaɪvz/", "nhắm mắt làm ngơ; thông đồng lén"),
    ("068768", "convertors", "noun", "/kənˈvɜːrtərz/", "bộ chuyển đổi dòng điện; lò luyện"),
    ("068769", "coonhounds", "noun", "/ˈkuːnˌhaʊndz/", "giống chó săn chuyên lùng gấu mèo"),
    ("068770", "cornstalks", "noun", "/ˈkɔːrnˌstɔːks/", "thân cây ngô sau khi thu hoạch"),
    ("068771", "corynebacteria", "noun", "/kəˌraɪnibækˈtɪriə/", "trực khuẩn hình chùy gây bạch hầu"),
    ("068772", "deciliters", "noun", "/ˈdɛsɪˌliːtərz/", "đơn vị thể tích đề-xi-lít (0,1 lít)"),
    ("068773", "derains", "noun", "/dəˈrænz/", "họa sĩ Pháp André Derain"),
    ("068774", "djakartas", "noun", "/dʒəˈkɑːrtəz/", "thủ đô Jakarta (cách viết cũ)"),
    ("068775", "dogteeth", "noun", "/ˈdɒɡˌtiːθ/", "răng nanh; họa tiết răng sói"),
    ("068776", "dogtooths", "noun", "/ˈdɒɡˌtuːθs/", "răng nanh nhọn; họa tiết dệt carô"),
    ("068777", "eimerias", "noun", "/aɪˈmɪriəz/", "ký sinh trùng cầu trùng Eimeria"),
    ("068778", "elluls", "noun", "/ɛˈluːlz/", "tháng thứ mười hai Elul Do Thái"),
    ("068779", "excoriated", "verb", "/ɛkˈskɔːriˌeɪtɪd/", "đã chỉ trích gay gắt; làm trầy da"),
    ("068780", "excoriates", "verb", "/ɛkˈskɔːriˌeɪts/", "chỉ trích kịch liệt; làm trầy xước"),
    ("068781", "excoriating", "verb", "/ɛkˈskɔːriˌeɪtɪŋ/", "đang chỉ trích nặng nề; làm sây sát"),
    ("068782", "fallots", "noun", "/fæˈloʊz/", "bác sĩ tim mạch Pháp É. Fallot"),
    ("068783", "formalwears", "noun", "/ˈfɔːrməlˌwɛərz/", "trang phục dạ hội trang trọng"),
    ("068784", "fortunetellers", "noun", "/ˈfɔːrtʃənˌtɛlərz/", "thầy bói xem quẻ đoán tương lai"),
    ("068785", "froebels", "noun", "/ˈfrɜːrbəlz/", "nhà giáo dục Đức Friedrich Fröbel"),
    ("068786", "frustums", "noun", "/ˈfrʌstəmz/", "khối chóp cụt hoặc nón cụt hình học"),
    ("068787", "gasconaded", "verb", "/ˌɡæskəˈneɪdɪd/", "đã khoác lác ba hoa tự phụ (cũ)"),
    ("068788", "gasconades", "noun", "/ˌɡæskəˈneɪdz/", "lời nói khoác lác huênh hoang"),
    ("068789", "gasconading", "verb", "/ˌɡæskəˈneɪdɪŋ/", "đang ba hoa khoác lác phô trương"),
    ("068790", "grammes", "noun", "/ɡræmz/", "đơn vị khối lượng gam (Anh Anh)"),
    ("068791", "guessers", "noun", "/ˈɡɛsərz/", "người phỏng đoán không chắc chắn"),
    ("068792", "gunsights", "noun", "/ˈɡʌnˌsaɪts/", "kính ngắm hoặc đầu ruồi ngắm súng"),
    ("068793", "hakeas", "noun", "/ˈheɪkiəz/", "cây bụi có quả gỗ Úc chi Hakea"),
    ("068794", "handsaws", "noun", "/ˈhændˌsɔːz/", "cưa cầm tay dùng xẻ gỗ thủ công"),
    ("068795", "heliothises", "noun", "/ˌhiːliˈoʊθɪsɪz/", "ngài sâu xanh đục quả Heliothis"),
    ("068796", "hermaphroditisms", "noun", "/hɜːrˈmæfrəˌdaɪtɪzəmz/", "hiện tượng lưỡng tính sinh học"),
    ("068797", "hobnailing", "verb", "/ˈhɒbˌneɪlɪŋ/", "đang đóng đinh mũ vào đế giày"),
    ("068798", "hobnails", "noun", "/ˈhɒbˌneɪlz/", "đinh mũ đóng chống trượt đế giày"),
    ("068799", "horseflies", "noun", "/ˈhɔːrsˌflaɪz/", "ruồi trâu lớn hút máu gia súc"),
    ("068800", "hybridomas", "noun", "/ˌhaɪbrɪˈdoʊməz/", "tế bào lai tạo kháng thể đơn dòng"),
    ("068801", "ichneumons", "noun", "/ɪkˈnjuːmənz/", "cầy mangut Ai Cập; ong cự ký sinh"),
    ("068802", "iguanodons", "noun", "/ɪˈɡwɑːnəˌdɒnz/", "khủng long ăn cỏ Iguanodon cổ đại"),
]

with open("scratch/b34_r08_raw_p3.json") as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100
allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}

out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, items):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} != {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} != {hw}"
    assert pos in allowed_pos, f"Bad POS {pos} for {hw}"
    assert len(vi) <= 35, f"VI too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA: {hw} -> {ipa}"
    inner = ipa[1:-1]
    assert inner and not inner.startswith(" ") and not inner.endswith(" "), f"Empty/space IPA: {hw} -> {ipa}"
    rec = dict(r)
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

with open("scratch/b34_r08_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r08_p3.json OK")
