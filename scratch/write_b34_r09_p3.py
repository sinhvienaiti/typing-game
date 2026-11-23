import json

items = [
    ("069203", "phalarises", "noun", "/ˈfælərɪsɪz/", "cỏ hoàng yến thuộc chi Phalaris"),
    ("069204", "photogravures", "noun", "/ˌfoʊtoʊɡrəˈvjʊərz/", "kỹ thuật in ảnh khắc lõm bản đồng"),
    ("069205", "pilocarpines", "noun", "/ˌpaɪloʊˈkɑːrpiːnz/", "thuốc nhỏ mắt trị tăng nhãn áp"),
    ("069206", "pinnies", "noun", "/ˈpɪniz/", "tạp dề; váy yếm trẻ em (khẩu ngữ)"),
    ("069207", "pomes", "noun", "/poʊmz/", "quả táo giả thịt mọng như lê táo"),
    ("069208", "potamogetons", "noun", "/ˌpɒtəmoʊˈdʒiːtɒnz/", "cây thủy sinh chi Potamogeton"),
    ("069209", "presentiments", "noun", "/prɪˈzɛntɪmənts/", "linh cảm dự báo điều sắp xảy đến"),
    ("069210", "proserpinas", "noun", "/prəˈsɜːrpɪnəz/", "nữ thần âm phủ Proserpina La Mã"),
    ("069211", "pruners", "noun", "/ˈpruːnərz/", "kéo cắt cành cây; người tỉa cành"),
    ("069212", "pseuds", "noun", "/sjuːdz/", "kẻ trí thức rởm ra vẻ thông thái"),
    ("069213", "purveyed", "verb", "/pərˈveɪd/", "đã cung cấp lương thực thực phẩm"),
    ("069214", "purveying", "verb", "/pərˈveɪɪŋ/", "đang cung ứng thực phẩm dịch vụ"),
    ("069215", "purveys", "verb", "/pərˈveɪz/", "cung cấp thực phẩm hoặc thông tin"),
    ("069216", "ranters", "noun", "/ˈræntərz/", "người gào thét hùng hổ giảng đạo"),
    ("069217", "rapscallions", "noun", "/ræpˈskæliənz/", "kẻ lưu manh ranh ma nghịch ngợm"),
    ("069218", "rased", "verb", "/reɪzd/", "đã san bằng phá sập hoàn toàn (Anh)"),
    ("069219", "rasing", "verb", "/ˈreɪzɪŋ/", "đang san phẳng triệt hạ công trình"),
    ("069220", "reenactors", "noun", "/ˌriːɪˈnæktərz/", "người diễn tái hiện sự kiện lịch sử"),
    ("069221", "repps", "noun", "/rɛps/", "vải dệt gân sọc nổi repp bọc ghế"),
    ("069222", "ringlets", "noun", "/ˈrɪŋlɪts/", "lọn tóc xoăn; bướm mắt vòng"),
    ("069223", "roquettes", "noun", "/rɒˈkɛts/", "rau cải xà lách rocket vị cay nồng"),
    ("069224", "rugas", "noun", "/ˈruːɡəz/", "nếp gấp niêm mạc bên trong dạ dày"),
    ("069225", "salesrooms", "noun", "/ˈseɪlzˌruːmz/", "phòng trưng bày giới thiệu bán hàng"),
    ("069226", "salvors", "noun", "/ˈsælvərz/", "tàu hoặc người cứu hộ tàu hàng đắm"),
    ("069227", "shuas", "noun", "/ˈʃuːəz/", "người Ả Rập Shuwa; tên Shua"),
    ("069228", "sirdars", "noun", "/ˈsɪərdɑːrz/", "tổng chỉ huy quân đội; thủ lĩnh Ấn"),
    ("069229", "sisons", "noun", "/ˈsaɪsɒnz/", "cây cỏ mùi tây hoang chi Sison"),
    ("069230", "sorbates", "noun", "/ˈsɔːrbeɪts/", "muối axit sorbic chất bảo quản"),
    ("069231", "spankers", "noun", "/ˈspæŋkərz/", "buồm phụ sau lái tàu; người đánh"),
    ("069232", "sundews", "noun", "/ˈsʌnˌduːz/", "cây gọng vó bắt côn trùng"),
    ("069233", "tadalafils", "noun", "/təˈdæləˌfɪlz/", "thuốc giãn mạch tadalafil (Cialis)"),
    ("069234", "tailplanes", "noun", "/ˈteɪlˌpleɪnz/", "cánh đuôi ổn định ngang máy bay"),
    ("069235", "tapises", "noun", "/ˈtæpɪzɪz/", "thảm dệt trang trí treo tường"),
    ("069236", "toilers", "noun", "/ˈtɔɪlərz/", "người lao động cật lực vất vả"),
    ("069237", "vardenafils", "noun", "/vɑːrˈdɛnəˌfɪlz/", "hoạt chất trị rối loạn cương"),
    ("069238", "vestured", "verb", "/ˈvɛstʃərd/", "đã khoác áo choàng lễ phục cho"),
    ("069239", "vestures", "noun", "/ˈvɛstʃərz/", "lễ phục áo choàng; y phục che phủ"),
    ("069240", "vesturing", "verb", "/ˈvɛstʃərɪŋ/", "đang mặc áo choàng phủ kín"),
    ("069241", "whoopers", "noun", "/ˈhuːpərz/", "sếu Mỹ; thiên nga kêu vang; ho gà"),
    ("069242", "zithromaxes", "noun", "/zɪˈθroʊˌmæksɪz/", "thuốc kháng sinh Zithromax"),
    ("069243", "zocors", "noun", "/ˈzoʊkɔːrz/", "thuốc hạ mỡ máu simvastatin Zocor"),
    ("069244", "acceptations", "noun", "/ˌæksɛpˈteɪʃənz/", "nghĩa thông dụng được thừa nhận"),
    ("069245", "achilleas", "noun", "/ˌækɪˈliːəz/", "cây cúc vạn diệp thuộc chi Achillea"),
    ("069246", "ackees", "noun", "/ˈækiz/", "quả ackee đặc sản vùng Caribe"),
    ("069247", "acylations", "noun", "/ˌæsəˈleɪʃənz/", "phản ứng hóa học gắn nhóm acyl"),
    ("069248", "agarics", "noun", "/əˈɡærɪks/", "nấm mũ mang lá thuộc họ Agaricaceae"),
    ("069249", "agrostises", "noun", "/əˈɡrɒstɪsɪz/", "cỏ mật thảm sân gôn chi Agrostis"),
    ("069250", "ampullas", "noun", "/æmˈpʊləz/", "bóng phình ống dẫn; lọ thủy tinh"),
    ("069251", "antiparticles", "noun", "/ˌæntiˈpɑːrtɪkəlz/", "phản hạt vật chất mang điện ngược"),
    ("069252", "araneas", "noun", "/əˈreɪniəz/", "nhện vườn dệt lưới thuộc chi Aranea"),
    ("069253", "armyworms", "noun", "/ˈɑːrmiˌwɜːrmz/", "sâu keo cắn phá hàng loạt mùa màng"),
    ("069254", "artemias", "noun", "/ɑːrˈtiːmiəz/", "tôm nước mặn làm mồi cá Artemia"),
    ("069255", "assignors", "noun", "/əˈsaɪnərz/", "bên chuyển nhượng quyền lợi tài sản"),
    ("069256", "atriplexes", "noun", "/ˈætrɪplɛksɪz/", "cây rau muối thuộc chi Atriplex"),
    ("069257", "ayins", "noun", "/ˈaɪɪnz/", "chữ cái Do Thái và Phênixi ayin"),
    ("069258", "bermudases", "noun", "/bərˈmjuːdəzɪz/", "quần đảo Bermuda Đại Tây Dương"),
    ("069259", "bodged", "verb", "/bɒdʒd/", "đã làm ẩu sửa chắp vá tạm bợ (Anh)"),
    ("069260", "bodges", "verb", "/ˈbɒdʒɪz/", "làm hỏng bét; vá víu cẩu thả (Anh)"),
    ("069261", "bodging", "verb", "/ˈbɒdʒɪŋ/", "đang sửa ẩu vá víu tạm bợ (Anh)"),
    ("069262", "boehmes", "noun", "/ˈbɜːməz/", "nhà thần bí học Đức Jakob Boehme"),
    ("069263", "brasiers", "noun", "/ˈbreɪʒərz/", "lò than đồng hở; thợ gò đồ đồng"),
    ("069264", "breathalysers", "noun", "/ˈbrɛθəˌlaɪzərz/", "máy đo nồng độ cồn qua hơi thở"),
    ("069265", "bryozoans", "noun", "/ˌbraɪəˈzoʊənz/", "động vật hình rêu sống tập đoàn"),
    ("069266", "butterbeans", "noun", "/ˈbʌtərˌbiːnz/", "hạt đậu ngự dẹt lớn béo ngậy"),
    ("069267", "canidaes", "noun", "/ˈkænɪdiːz/", "họ Chó gồm chó sói cáo và chó rừng"),
    ("069268", "carlinas", "noun", "/kɑːrˈliːnəz/", "cúc gai Địa Trung Hải chi Carlina"),
    ("069269", "chartisms", "noun", "/ˈtʃɑːrtɪzəmz/", "phong trào Hiến chương Anh"),
    ("069270", "chorions", "noun", "/ˈkɔːriɒnz/", "màng đệm ngoài cùng bao bọc phôi"),
    ("069271", "cingula", "noun", "/ˈsɪŋɡjʊlə/", "vòng đai giải phẫu; hồi đai não"),
    ("069272", "cingulums", "noun", "/ˈsɪŋɡjʊləmz/", "gờ cổ răng; dải sợi liên kết não"),
    ("069273", "congregants", "noun", "/ˈkɒŋɡrɪɡənts/", "tín đồ tham dự buổi lễ nhà thờ"),
    ("069274", "cowhands", "noun", "/ˈkaʊˌhændz/", "người làm công chăn bò trang trại"),
    ("069275", "crawdads", "noun", "/ˈkrɔːˌdædz/", "tôm hùm đất sống nước ngọt (Mỹ)"),
    ("069276", "crotaluses", "noun", "/ˈkrɒtələsɪz/", "rắn đuôi chuông độc chi Crotalus"),
    ("069277", "cryostats", "noun", "/ˈkraɪoʊˌstæts/", "thiết bị ổn nhiệt cực thấp"),
    ("069278", "cucurbitas", "noun", "/kjuːˈkɜːrbɪtəz/", "cây bầu bí thuộc chi Cucurbita"),
    ("069279", "denebs", "noun", "/ˈdɛnɛbz/", "ngôi sao sáng Deneb chòm Thiên Nga"),
    ("069280", "deuterons", "noun", "/ˈdjuːtəˌrɒnz/", "hạt nhân nguyên tử đơteri (1p+1n)"),
    ("069281", "eclogues", "noun", "/ˈɛklɒɡz/", "bài thơ mục đồng đối thoại đồng quê"),
    ("069282", "enologies", "noun", "/iːˈnɒlədʒiz/", "khoa học kỹ thuật sản xuất rượu"),
    ("069283", "enthraled", "verb", "/ɪnˈθrɔːld/", "đã mê hoặc cuốn hút say đắm (cũ)"),
    ("069284", "enthraling", "verb", "/ɪnˈθrɔːlɪŋ/", "đang mê hoặc quyến rũ (biến thể)"),
    ("069285", "epicondyles", "noun", "/ˌɛpɪˈkɒndaɪlz/", "mỏm trên lồi cầu ở đầu xương dài"),
    ("069286", "epistaxises", "noun", "/ˌɛpɪˈstæksɪsɪz/", "tình trạng chảy máu cam ở mũi"),
    ("069287", "euryales", "noun", "/jʊˈraɪəliz/", "cây khiếm thực Euryale; sao biển"),
    ("069288", "gawped", "verb", "/ɡɔːpt/", "đã há hốc mồm nhìn trân trân (Anh)"),
    ("069289", "gawping", "verb", "/ˈɡɔːpɪŋ/", "đang đứng ngây người nhìn chằm chằm"),
    ("069290", "gawps", "verb", "/ɡɔːps/", "nhìn chằm chằm ngơ ngác lộ liễu"),
    ("069291", "geryons", "noun", "/ˈdʒɪriɒnz/", "quái vật ba thân Geryon Hy Lạp"),
    ("069292", "guanacos", "noun", "/ɡwɑːˈnɑːkoʊz/", "lạc đà không bướu hoang dã Nam Mỹ"),
    ("069293", "handbells", "noun", "/ˈhændˌbɛlz/", "chuông đồng nhỏ cầm tay hợp tấu"),
    ("069294", "hannukahs", "noun", "/ˈhɑːnəkəz/", "lễ hội ánh sáng Hanukkah Do Thái"),
    ("069295", "hasdrubals", "noun", "/hæzˈdruːbəlz/", "tướng Carthage Hasdrubal Barca"),
    ("069296", "hawsers", "noun", "/ˈhɔːzərz/", "dây thừng cáp bện to neo kéo tàu"),
    ("069297", "haytis", "noun", "/ˈheɪtiz/", "đảo quốc Haiti ở vùng biển Caribe"),
    ("069298", "hepatomas", "noun", "/ˌhɛpəˈtoʊməz/", "khối u ác tính tế bào biểu mô gan"),
    ("069299", "hidatsas", "noun", "/hɪˈdɑːtsəz/", "bộ tộc bản địa Hidatsa Bắc Mỹ"),
    ("069300", "hogweeds", "noun", "/ˈhɒɡˌwiːdz/", "cây độc cần khổng lồ gây bỏng da"),
    ("069301", "hymeniums", "noun", "/haɪˈmiːniəmz/", "tầng sinh bào tử nấm (nấm học)"),
    ("069302", "hynia", "noun", "/ˈhɪniə/", "tầng sinh bào tử nấm (biến thể)"),
]

with open("scratch/b34_r09_raw_p3.json") as f:
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

with open("scratch/b34_r09_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r09_p3.json OK")
