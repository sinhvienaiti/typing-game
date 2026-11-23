import json

items = [
    ("070003", "semiprofessionals", "noun", "/ˌsɛmiprəˈfɛʃənəlz/", "người làm nghề bán chuyên nghiệp"),
    ("070004", "semipros", "noun", "/ˈsɛmiˌproʊz/", "người chơi bán chuyên nghiệp"),
    ("070005", "serapes", "noun", "/səˈrɑːpeɪz/", "khăn choàng serape kiểu Mexico"),
    ("070006", "serratias", "noun", "/səˈreɪʃəz/", "vi khuẩn thuộc chi Serratia"),
    ("070007", "sesothos", "noun", "/səˈsuːtuːz/", "tiếng Sesotho; người dân Sotho"),
    ("070008", "shutterbugs", "noun", "/ˈʃʌtərˌbʌɡz/", "người đam mê chụp ảnh (khẩu ngữ)"),
    ("070009", "sightseers", "noun", "/ˈsaɪtˌsiːərz/", "khách tham quan ngắm cảnh"),
    ("070010", "siqueiroses", "noun", "/sɪˈkeɪroʊsɪz/", "họa sĩ tranh tường Siqueiros"),
    ("070011", "skags", "noun", "/skæɡz/", "ma túy heroin (tiếng lóng)"),
    ("070012", "skeats", "noun", "/skiːts/", "nhà ngữ văn Walter W. Skeat"),
    ("070013", "solarizations", "noun", "/ˌsoʊləraɪˈzeɪʃənz/", "hiện tượng đảo sắc; sự phơi nắng"),
    ("070014", "spivs", "noun", "/spɪvz/", "kẻ buôn lậu chui; tay mánh khóe"),
    ("070015", "steeplechasers", "noun", "/ˈstiːpəlˌtʃeɪsərz/", "ngựa đua vượt rào; VĐV chạy vượt"),
    ("070016", "subdeacons", "noun", "/ˌsʌbˈdiːkənz/", "phó trợ tế trong giáo hội"),
    ("070017", "tetrodes", "noun", "/ˈtɛtroʊdz/", "đèn điện tử bốn cực"),
    ("070018", "theobromas", "noun", "/ˌθiːəˈbroʊməz/", "cây ca cao thuộc chi Theobroma"),
    ("070019", "threnodies", "noun", "/ˈθrɛnədiz/", "bài ai điếu; khúc ca tang thương"),
    ("070020", "toyshops", "noun", "/ˈtɔɪˌʃɒps/", "cửa hàng bán đồ chơi"),
    ("070021", "twelvemonths", "noun", "/ˈtwɛlvˌmʌnθs/", "khoảng thời gian một năm"),
    ("070022", "umbos", "noun", "/ˈʌmboʊz/", "đỉnh nhô giữa khiên; rốn màng nhĩ"),
    ("070023", "unimportances", "noun", "/ˌʌnɪmˈpɔːrtənsɪz/", "sự không quan trọng; tính tầm phào"),
    ("070024", "windsocks", "noun", "/ˈwɪndˌsɒks/", "ống vải chỉ hướng và sức gió"),
    ("070025", "workaholisms", "noun", "/ˌwɜːrkəˈhɒlɪzəmz/", "chứng nghiện làm việc quá mức"),
    ("070026", "wtvs", "noun", "/ˌdʌbəljuː tiː ˈviːz/", "vi-rút u vết thương thực vật"),
    ("070027", "yellowhammers", "noun", "/ˈjɛloʊˌhæmərz/", "chim sẻ đồng vàng; gõ kiến vàng Mỹ"),
    ("070028", "yeniseis", "noun", "/ˌjɛnɪˈseɪz/", "sông Yenisei ở vùng Siberia"),
    ("070029", "zinssers", "noun", "/ˈzɪnsərz/", "nhà vi trùng học Hans Zinsser"),
    ("070030", "accreted", "verb", "/əˈkriːtɪd/", "đã bồi tụ thêm; đã mọc dính liền"),
    ("070031", "accretes", "verb", "/əˈkriːts/", "bồi tụ dần; kết hợp dính liền"),
    ("070032", "accreting", "verb", "/əˈkriːtɪŋ/", "đang bồi tụ dần; đang dính liền"),
    ("070033", "akabas", "noun", "/ˈɑːkəbəz/", "thành phố cảng Aqaba ở Jordan"),
    ("070034", "amnions", "noun", "/ˈæmniənz/", "màng ối bao bọc phôi thai"),
    ("070035", "apers", "noun", "/ˈeɪpərz/", "kẻ bắt chước nhại lại"),
    ("070036", "araneaes", "noun", "/əˈreɪniiːz/", "bộ Nhện trong lớp Hình nhện"),
    ("070037", "arhats", "noun", "/ˈɑːrhɑːts/", "bậc A-la-hán trong Phật giáo"),
    ("070038", "armholes", "noun", "/ˈɑːrmˌhoʊlz/", "lỗ tay áo; vòng nách áo"),
    ("070039", "audiometries", "noun", "/ˌɔːdiˈɒmɪtriz/", "phép đo thính lực kiểm tra tai"),
    ("070040", "bakeshops", "noun", "/ˈbeɪkˌʃɒps/", "tiệm làm và bán bánh ngọt"),
    ("070041", "baptistries", "noun", "/ˈbæptɪstriz/", "nhà rửa tội; bồn làm lễ rửa tội"),
    ("070042", "bassoonists", "noun", "/bəˈsuːnɪsts/", "nhạc công chơi kèn bassoon"),
    ("070043", "batises", "noun", "/ˈbeɪtɪsɪz/", "cây muối biển Batis; chim batis"),
    ("070044", "beignets", "noun", "/beɪnˈjeɪz/", "bánh rán bột chiên phồng kiểu Pháp"),
    ("070045", "bloodroots", "noun", "/ˈblʌdˌruːts/", "cây huyết căn mọc hoa trắng"),
    ("070046", "brahmanisms", "noun", "/ˈbrɑːməˌnɪzəmz/", "đạo Bà-la-môn cổ đại Ấn Độ"),
    ("070047", "cagers", "noun", "/ˈkeɪdʒərz/", "cầu thủ môn bóng rổ (lóng Mỹ)"),
    ("070048", "caloosahatchees", "noun", "/kəˌluːsəˈhætʃiz/", "sông Caloosahatchee ở Florida"),
    ("070049", "caramelised", "verb", "/ˈkærəməˌlaɪzd/", "đã thắng thành caramen (Anh)"),
    ("070050", "caramelises", "verb", "/ˈkærəməˌlaɪzɪz/", "thắng đường thành caramen (Anh)"),
    ("070051", "caramelising", "verb", "/ˈkærəməˌlaɪzɪŋ/", "đang thắng thành caramen (Anh)"),
    ("070052", "carreres", "noun", "/kəˈrɛərz/", "kiến trúc sư John M. Carrère"),
    ("070053", "cecropias", "noun", "/sɪˈkroʊpiəz/", "cây kèn rừng thuộc chi Cecropia"),
    ("070054", "chromatograms", "noun", "/kroʊˈmætəˌɡræmz/", "sắc ký đồ kết quả phân tích"),
    ("070055", "claystones", "noun", "/ˈkleɪˌstoʊnz/", "đá sét kết hạt mịn trầm tích"),
    ("070056", "clumbers", "noun", "/ˈklʌmbərz/", "giống chó săn Clumber Spaniel"),
    ("070057", "collembolas", "noun", "/kəˈlɛmbələz/", "bộ Bọ nhảy nhỏ sống trong đất"),
    ("070058", "compositaes", "noun", "/kəmˈpɒzɪtiːz/", "họ Cúc thực vật (tên cũ Aster)"),
    ("070059", "corrugations", "noun", "/ˌkɔːrəˈɡeɪʃənz/", "nếp gấp gợn sóng; rãnh sóng tôn"),
    ("070060", "cupressuses", "noun", "/kjʊˈprɛsəsɪz/", "cây hoàng đàn thuộc chi Bách"),
    ("070061", "curatorships", "noun", "/kjʊˈreɪtərʃɪps/", "chức vụ giám tuyển bảo tàng"),
    ("070062", "cycads", "noun", "/ˈsaɪkædz/", "cây thiên tuế cổ đại hạt trần"),
    ("070063", "depilatories", "noun", "/dɪˈpɪləˌtɔːriz/", "thuốc hoặc kem tẩy lông"),
    ("070064", "depravations", "noun", "/ˌdɛprəˈveɪʃənz/", "sự đồi bại suy đồi đạo đức"),
    ("070065", "diatomites", "noun", "/daɪˈætəˌmaɪts/", "đất tảo cát điatômit lọc thấm"),
    ("070066", "dioscoreas", "noun", "/ˌdaɪəˈskɔːriəz/", "cây họ Củ nâu thuộc chi Củ mài"),
    ("070067", "eiderdowns", "noun", "/ˈaɪdərˌdaʊnz/", "chăn lông vịt biển mềm nhẹ"),
    ("070068", "erythropoieses", "noun", "/ɪˌrɪθroʊpɔɪˈiːsiːz/", "quá trình tạo hồng cầu ở tủy"),
    ("070069", "eupatoriums", "noun", "/ˌjuːpəˈtɔːriəmz/", "cây cỏ lào thuộc chi Eupatorium"),
    ("070070", "eversions", "noun", "/ɪˈvɜːrʒənz/", "sự lộn ngược mặt trong ra ngoài"),
    ("070071", "factualities", "noun", "/ˌfæktʃuˈælɪtiz/", "tính chân thực; sự việc có thật"),
    ("070072", "finnans", "noun", "/ˈfɪnənz/", "cá tuyết hun khói kiểu Scotland"),
    ("070073", "flukier", "adj", "/ˈfluːkiər/", "ăn may nhiều hơn; bất thường hơn"),
    ("070074", "flukiest", "adj", "/ˈfluːkiɪst/", "ăn may nhất; thất thường nhất"),
    ("070075", "formalisations", "noun", "/ˌfɔːrməlaɪˈzeɪʃənz/", "sự hình thức hóa (cách viết Anh)"),
    ("070076", "fragarias", "noun", "/frəˈɡɛəriəz/", "cây dâu tây thuộc chi Fragaria"),
    ("070077", "gainsaying", "verb", "/ˈɡeɪnˌseɪɪŋ/", "đang phủ nhận; đang bác bỏ"),
    ("070078", "gainsays", "verb", "/ɡeɪnˈseɪz/", "phủ nhận; lên tiếng bác bỏ"),
    ("070079", "glassblowers", "noun", "/ˈɡlæsˌbloʊərz/", "thợ thổi tạo hình thủy tinh"),
    ("070080", "groundfishes", "noun", "/ˈɡraʊndˌfɪʃɪz/", "cá sống ở tầng đáy biển"),
    ("070081", "gypsophilas", "noun", "/dʒɪpˈsɒfɪləz/", "hoa bi bi; cây thạch trúc"),
    ("070082", "hadeans", "noun", "/ˈheɪdiənz/", "liên đại Hỏa thành Trái Đất"),
    ("070083", "hindguts", "noun", "/ˈhaɪndˌɡʌts/", "ruột sau của phôi hay động vật"),
    ("070084", "homogenisations", "noun", "/həˌmɒdʒɪnaɪˈzeɪʃənz/", "sự đồng hóa hỗn hợp (Anh)"),
    ("070085", "hoofers", "noun", "/ˈhʊfərz/", "vũ công chuyên nghiệp (lóng Mỹ)"),
    ("070086", "housetops", "noun", "/ˈhaʊsˌtɒps/", "nóc nhà; mái phía trên ngôi nhà"),
    ("070087", "hypovolemias", "noun", "/ˌhaɪpoʊvɒˈliːmiəz/", "chứng giảm thể tích máu tuần hoàn"),
    ("070088", "isosorbides", "noun", "/ˌaɪsoʊˈsɔːrbaɪdz/", "thuốc giãn mạch tim isosorbide"),
    ("070089", "kepis", "noun", "/ˈkeɪpiz/", "mũ kê-pi đỉnh phẳng có lưỡi trai"),
    ("070090", "lacewings", "noun", "/ˈleɪsˌwɪŋz/", "bọ cánh gân ăn rệp (cánh màng)"),
    ("070091", "lagniappes", "noun", "/ˈlænjæps/", "món quà nhỏ chủ tiệm tặng thêm"),
    ("070092", "laminators", "noun", "/ˈlæmɪˌneɪtərz/", "máy cán màng nhựa; thợ ép màng"),
    ("070093", "legatees", "noun", "/ˌlɛɡəˈtiːz/", "người được thừa hưởng di sản"),
    ("070094", "loquats", "noun", "/ˈloʊkwɒts/", "quả hoặc cây nhót tây (tỳ bà)"),
    ("070095", "luciferins", "noun", "/luːˈsɪfərɪnz/", "hợp chất phát quang sinh học"),
    ("070096", "lyssaviruses", "noun", "/ˌlɪsəˈvaɪrəsɪz/", "chi vi-rút gây bệnh dại"),
    ("070097", "maravillas", "noun", "/ˌmærəˈvɪləz/", "hoa phấn bốn giờ (mirabilis)"),
    ("070098", "matzohs", "noun", "/ˈmɑːtsəz/", "bánh mì không men matzo Do Thái"),
    ("070099", "meningoencephalitides", "noun", "/məˌnɪŋɡoʊɛnˌsɛfəˈlaɪtɪdiːz/", "bệnh viêm màng não và não"),
    ("070100", "moaners", "noun", "/ˈmoʊnərz/", "người hay rên rỉ than vãn"),
    ("070101", "monophysites", "noun", "/məˈnɒfɪˌsaɪts/", "tín đồ thuyết Nhất Tính Ki-tô"),
    ("070102", "mortmains", "noun", "/ˈmɔːrtmeɪnz/", "quyền sở hữu tài sản vĩnh viễn"),
]

with open("scratch/b35_r01_raw_p1.json") as f:
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

with open("scratch/b35_r01_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r01_p1.json OK")
