import json

items = [
    ("067603", "alimentations", "noun", "/ˌælɪmɛnˈteɪʃənz/", "sự nuôi dưỡng; nguồn thực phẩm"),
    ("067604", "ammeters", "noun", "/ˈæmˌmiːtərz/", "đồng hồ ampe kế đo cường độ dòng"),
    ("067605", "amphipods", "noun", "/ˈæmfɪˌpɒdz/", "giáp xác chân khác như bọ cát biển"),
    ("067606", "ananases", "noun", "/əˈnænəsɪz/", "cây dứa thơm thuộc chi Ananas"),
    ("067607", "apeldoorns", "noun", "/ˈɑːpəldɔːrnz/", "thành phố Apeldoorn ở Hà Lan"),
    ("067608", "arenarias", "noun", "/ˌærəˈnɛəriəz/", "cây cỏ cát thuộc chi Arenaria"),
    ("067609", "armourers", "noun", "/ˈɑːrmərərz/", "thợ rèn áo giáp và vũ khí cổ"),
    ("067610", "bagpipers", "noun", "/ˈbæɡˌpaɪpərz/", "nghệ sĩ thổi kèn túi Scotland"),
    ("067611", "berzeliuses", "noun", "/bərˈziːliəsɪz/", "nhà hóa học Thụy Điển Berzelius"),
    ("067612", "bifurcates", "verb", "/ˈbaɪfərˌkeɪts/", "phân đôi tách thành hai nhánh"),
    ("067613", "bifurcating", "verb", "/ˈbaɪfərˌkeɪtɪŋ/", "đang rẽ đôi phân thành hai nhánh"),
    ("067614", "blixens", "noun", "/ˈblɪksənz/", "nữ nhà văn Đan Mạch Karen Blixen"),
    ("067615", "bontempses", "noun", "/ˈbɒntɑːmzɪz/", "nhà văn Mỹ Arna Bontemps"),
    ("067616", "bounders", "noun", "/ˈbaʊndərz/", "gã thô lỗ vô lại; kẻ hèn (Anh)"),
    ("067617", "carduccis", "noun", "/kɑːrˈduːtʃiz/", "nhà thơ Nobel Ý Giosuè Carducci"),
    ("067618", "catechins", "noun", "/ˈkætɪtʃɪnz/", "chất chống oxy hóa catechin trà"),
    ("067619", "ciscs", "noun", "/sɪsks/", "vi xử lý CISC; Tình báo Hình sự"),
    ("067620", "cockatrices", "noun", "/ˈkɒkəˌtraɪsɪz/", "quái vật đầu gà thân rắn thần thoại"),
    ("067621", "conjunctures", "noun", "/kənˈdʒʌŋktʃərz/", "thời điểm bước ngoặt giao hội thế"),
    ("067622", "convolvuli", "noun", "/kənˈvɒlvjʊlaɪ/", "cây bìm bìm hoa loa kèn leo"),
    ("067623", "convolvuluses", "noun", "/kənˈvɒlvjʊləsɪz/", "hoa bìm bìm chi Convolvulus"),
    ("067624", "cummerbunds", "noun", "/ˈkʌmərˌbʌndz/", "đai lưng vải rộng thắt áo lễ tuxedo"),
    ("067625", "cymbidiums", "noun", "/sɪmˈbɪdiəmz/", "hoa địa lan kiếm chi Cymbidium"),
    ("067626", "daysprings", "noun", "/ˈdeɪˌsprɪŋz/", "lúc rạng đông bình minh (thơ văn)"),
    ("067627", "demoiselles", "noun", "/ˌdɛmwɑːˈzɛlz/", "cô gái trẻ (Pháp); cá thia biển"),
    ("067628", "dependances", "noun", "/dɪˈpɛndənsɪz/", "sự phụ thuộc lệ thuộc (biến thể)"),
    ("067629", "dichloromethanes", "noun", "/daɪˌklɔːroʊˈmɛθeɪnz/", "dung môi hữu cơ điclometan"),
    ("067630", "didacticses", "noun", "/daɪˈdæktɪksɪz/", "khoa học phương pháp giảng dạy"),
    ("067631", "dirndls", "noun", "/ˈdɜːrndəlz/", "váy truyền thống vùng Bavaria Áo"),
    ("067632", "dodecaneses", "noun", "/ˌdoʊdɪkəˈniːzɪz/", "quần đảo Dodecanese của Hy Lạp"),
    ("067633", "doohickeys", "noun", "/ˈduːˌhɪkiz/", "cái món đồ lặt vặt quên tên (lóng)"),
    ("067634", "doorjambs", "noun", "/ˈdɔːrˌdʒæmz/", "thanh đố đứng hai bên khung cửa"),
    ("067635", "dubliners", "noun", "/ˈdʌblɪnərz/", "người dân thủ đô Dublin Ireland"),
    ("067636", "educationalists", "noun", "/ˌɛdʒʊˈkeɪʃənəlɪsts/", "chuyên gia lý luận giáo dục học"),
    ("067637", "elamites", "noun", "/ˈiːləmaɪts/", "cư dân vương quốc cổ Elam Ba Tư"),
    ("067638", "eponas", "noun", "/ɛˈpoʊnəz/", "nữ thần ngựa Epona thần thoại"),
    ("067639", "etds", "noun", "/ˌiː tiː ˈdiːz/", "giờ khởi hành ETD; máy dò chất nổ"),
    ("067640", "evolutionisms", "noun", "/ˌɛvəˈluːʃəˌnɪzəmz/", "học thuyết tiến hóa sinh học"),
    ("067641", "fatihas", "noun", "/ˈfɑːtɪhəz/", "chương mở đầu Al-Fatiha kinh Quran"),
    ("067642", "firebricks", "noun", "/ˈfaɪərˌbrɪks/", "gạch chịu nhiệt cao lát lò nung"),
    ("067643", "flowages", "noun", "/ˈfloʊɪdʒɪz/", "lưu lượng dòng chảy; vùng ngập nước"),
    ("067644", "foldouts", "noun", "/ˈfoʊldˌaʊts/", "trang sách hoặc bản đồ gấp mở rộng"),
    ("067645", "freyrs", "noun", "/freɪərz/", "thần phồn thực Freyr Bắc Âu"),
    ("067646", "friggas", "noun", "/ˈfrɪɡəz/", "nữ thần tối cao Frigg Bắc Âu"),
    ("067647", "frumps", "noun", "/frʌmps/", "người ăn mặc lôi thôi lỗi mốt"),
    ("067648", "gastropodas", "noun", "/ɡæˈstrɒpədəz/", "lớp Chân bụng gồm ốc sên và ốc biển"),
    ("067649", "geminated", "verb", "/ˈdʒɛmɪneɪtɪd/", "đã nhân đôi phụ âm; ghép đôi cặp"),
    ("067650", "geminates", "noun", "/ˈdʒɛmɪnəts/", "phụ âm kép phát âm kéo dài"),
    ("067651", "geminating", "verb", "/ˈdʒɛmɪneɪtɪŋ/", "đang nhân đôi âm; ghép thành cặp"),
    ("067652", "gesners", "noun", "/ˈɡɛsnərz/", "nhà tự nhiên học Conrad Gessner"),
    ("067653", "glinkas", "noun", "/ˈɡlɪŋkəz/", "nhà soạn nhạc Nga Mikhail Glinka"),
    ("067654", "grackles", "noun", "/ˈɡrækəlz/", "chim sáo đen mỏ nhọn châu Mỹ"),
    ("067655", "grindles", "noun", "/ˈɡrɪndəlz/", "cá vây cung Amia calva Bắc Mỹ"),
    ("067656", "hailstones", "noun", "/ˈheɪlˌstoʊnz/", "hạt cục mưa đá rơi trong giông"),
    ("067657", "hasidisms", "noun", "/ˈhæsɪˌdɪzəmz/", "giáo phái Do Thái giáo Hasidism"),
    ("067658", "hayseeds", "noun", "/ˈheɪˌsiːdz/", "người nhà quê chất phác (khẩu ngữ)"),
    ("067659", "hryvnias", "noun", "/ˈrɪvniəz/", "đơn vị tiền tệ hryvnia của Ukraine"),
    ("067660", "hydroxyzines", "noun", "/haɪˈdrɒksɪˌziːnz/", "thuốc kháng histamin hydroxyzine"),
    ("067661", "jaywalked", "verb", "/ˈdʒeɪˌwɔːkt/", "đã đi bộ sang đường ẩu sai luật"),
    ("067662", "jennets", "noun", "/ˈdʒɛnɪts/", "lừa cái; giống ngựa nhỏ Tây Ban Nha"),
    ("067663", "kolams", "noun", "/ˈkoʊləmz/", "người Kolam Ấn; tranh bột gạo sàn"),
    ("067664", "kreislers", "noun", "/ˈkraɪzlərz/", "nghệ sĩ vĩ cầm Fritz Kreisler"),
    ("067665", "kuznetses", "noun", "/ˈkʊznɛtsɪz/", "nhà kinh tế học Simon Kuznets"),
    ("067666", "laryngoscopes", "noun", "/ləˈrɪŋɡəˌskoʊps/", "dụng cụ đèn soi thanh quản y khoa"),
    ("067667", "levators", "noun", "/lɪˈveɪtərz/", "cơ nâng bộ phận trong giải phẫu"),
    ("067668", "limonites", "noun", "/ˈlaɪməˌnaɪts/", "quặng sắt oxit ngậm nước limonit"),
    ("067669", "linocuts", "noun", "/ˈlaɪnoʊˌkʌts/", "tranh khắc bản cao su linoleum"),
    ("067670", "lombardias", "noun", "/ˌlɒmbɑːrˈdiːəz/", "vùng Lombardy ở miền bắc nước Ý"),
    ("067671", "madrasahs", "noun", "/məˈdrɑːsəz/", "trường tôn giáo khoa học Hồi giáo"),
    ("067672", "matchers", "noun", "/ˈmætʃərz/", "người ghép đôi; công cụ so khớp"),
    ("067673", "mesenchymes", "noun", "/ˈmɛzəŋˌkaɪmz/", "mô trung mô phôi thai tạo liên kết"),
    ("067674", "metonymies", "noun", "/mɪˈtɒnɪmiz/", "biện pháp tu từ hoán dụ"),
    ("067675", "mujahedeens", "noun", "/ˌmuːdʒəˈhiːdiːnz/", "chiến binh thánh chiến Hồi giáo"),
    ("067676", "navahoes", "noun", "/ˈnævəˌhoʊz/", "bộ tộc bản địa Navajo Tây Nam Mỹ"),
    ("067677", "navahos", "noun", "/ˈnævəˌhoʊz/", "người Navajo (cách viết biến thể)"),
    ("067678", "naysayers", "noun", "/ˈneɪˌseɪərz/", "người hay bác bỏ bi quan chỉ trích"),
    ("067679", "nbes", "noun", "/ˌɛn biː ˈiːz/", "hướng bắc chếch đông NBE (la bàn)"),
    ("067680", "nernsts", "noun", "/nɜːrnsts/", "nhà hóa học Nobel Walther Nernst"),
    ("067681", "occams", "noun", "/ˈɒkəmz/", "triết gia Anh William of Ockham"),
    ("067682", "outsoles", "noun", "/ˈaʊtˌsoʊlz/", "lớp đế ngoài tiếp đất của giày"),
    ("067683", "overexploitations", "noun", "/ˌoʊvərˌɛksplɔɪˈteɪʃənz/", "sự khai thác cạn kiệt quá mức"),
    ("067684", "passerines", "noun", "/ˈpæsəraɪnz/", "chim hót đậu cành thuộc bộ Sẻ"),
    ("067685", "pectuses", "noun", "/ˈpɛktəsɪz/", "phần ngực lồng ngực (giải phẫu)"),
    ("067686", "pigmies", "noun", "/ˈpɪɡmiz/", "người lùn Pygmy; vật bé nhỏ"),
    ("067687", "plaints", "noun", "/pleɪnts/", "lời than thở ai oán; đơn khiếu kiện"),
    ("067688", "prepuces", "noun", "/ˈpriːpjuːsɪz/", "lớp da bao quy đầu ở cơ quan sinh"),
    ("067689", "proctologists", "noun", "/prɒkˈtɒlədʒɪsts/", "bác sĩ khoa hậu môn trực tràng"),
    ("067690", "propanols", "noun", "/ˈproʊpəˌnɒlz/", "rượu cồn ba cacbon propanol"),
    ("067691", "propellors", "noun", "/prəˈpɛlərz/", "chân vịt tàu; cánh quạt máy bay"),
    ("067692", "prophases", "noun", "/ˈproʊˌfeɪzɪz/", "kỳ đầu của quá trình phân chia tế"),
    ("067693", "radiograms", "noun", "/ˈreɪdioʊˌɡræmz/", "bức điện vô tuyến; ảnh chụp X-quang"),
    ("067694", "robles", "noun", "/ˈroʊbleɪz/", "cây gỗ sồi roble Tây Ban Nha"),
    ("067695", "roulades", "noun", "/ruːˈlɑːdz/", "thịt cuộn nhân; đoạn luyến thanh"),
    ("067696", "rubias", "noun", "/ˈruːbiəz/", "cây thiên thảo nhuộm đỏ chi Rubia"),
    ("067697", "sacajaweas", "noun", "/ˌsækədʒəˈwiːəz/", "nữ dẫn đường bản địa Sacagawea"),
    ("067698", "salvadoreans", "noun", "/ˌsælvəˈdɔːriənz/", "người dân nước El Salvador"),
    ("067699", "salvers", "noun", "/ˈsælvərz/", "khay bạc phẳng bưng thức ăn đồ uống"),
    ("067700", "schoolmistresses", "noun", "/ˈskuːlˌmɪstrɪsɪz/", "nữ giáo viên hoặc cô hiệu trưởng"),
    ("067701", "semitrailers", "noun", "/ˈsɛmiˌtreɪlərz/", "rơ-moóc thùng chở hàng nối đầu kéo"),
    ("067702", "setswanas", "noun", "/sɛtˈswɑːnəz/", "ngôn ngữ Setswana ở Botswana"),
]

with open("scratch/b34_r06_raw_p2.json") as f:
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

with open("scratch/b34_r06_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r06_p2.json OK")
