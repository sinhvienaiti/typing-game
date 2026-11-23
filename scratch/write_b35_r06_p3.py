import json

items = [
    ("072703", "acetamides", "noun", "/əˈsɛtəˌmaɪdz/", "hợp chất hóa học axetamit"),
    ("072704", "adelgids", "noun", "/əˈdɛldʒɪdz/", "rệp sáp hại cây thông chi Adelges"),
    ("072705", "agathises", "noun", "/ˈæɡəθɪsɪz/", "cây thông kauri chi Agathis"),
    ("072706", "aglets", "noun", "/ˈæɡlɪts/", "đầu bịt cứng ở hai đầu dây giày"),
    ("072707", "allhallowses", "noun", "/ɔːlˈhæloʊzɪz/", "Lễ Các Thánh (ngày 1 tháng 11)"),
    ("072708", "anglophobias", "noun", "/ˌæŋɡloʊˈfoʊbiəz/", "tâm lý bài hoặc sợ nước Anh"),
    ("072709", "anorgasmias", "noun", "/ˌænɔːrˈɡæzmiəz/", "chứng rối loạn không đạt cực khoái"),
    ("072710", "aphididaes", "noun", "/əˈfɪdɪˌdiːz/", "họ Rệp vừng hút nhựa cây"),
    ("072711", "arterias", "noun", "/ɑːrˈtɪəriəz/", "động mạch (tên giải phẫu Latinh)"),
    ("072712", "arthroscopes", "noun", "/ˈɑːrθrəˌskoʊps/", "kính nội soi thăm dò khớp xương"),
    ("072713", "arytenoids", "noun", "/ˌærɪˈtiːnɔɪdz/", "sụn phễu thanh quản (giải phẫu)"),
    ("072714", "asalas", "noun", "/ˈæsələz/", "tổ chức vũ trang ASALA Armenia"),
    ("072715", "asynchronies", "noun", "/eɪˈsɪŋkrəniz/", "tình trạng bất đồng bộ lệch nhịp"),
    ("072716", "avenses", "noun", "/ˈævɛnsɪz/", "cây địa du cánh bướm (chi Geum)"),
    ("072717", "barrelhouses", "noun", "/ˈbærəlˌhaʊzɪz/", "quán rượu bình dân; phong cách jazz"),
    ("072718", "beigels", "noun", "/ˈbeɪɡəlz/", "bánh mì vòng tròn Do Thái (Anh)"),
    ("072719", "bluepoints", "noun", "/ˈbluːˌpɔɪnts/", "hàu Bluepoint vịnh Long Island Mỹ"),
    ("072720", "calanthes", "noun", "/kəˈlænθiz/", "cây hoa lan bầu rượu chi Calanthe"),
    ("072721", "cameluses", "noun", "/kəˈmiːləsɪz/", "chi Lạc đà (lạc đà một, hai bướu)"),
    ("072722", "caudatas", "noun", "/kɔːˈdeɪtəz/", "bộ Có đuôi (kỳ giông, sa giông)"),
    ("072723", "ceftazidimes", "noun", "/sɛfˈtæzɪˌdiːmz/", "thuốc kháng sinh tiêm ceftazidime"),
    ("072724", "cercopithecuses", "noun", "/ˌsɜːrkoʊpɪˈθiːkəsɪz/", "chi Khỉ đuôi dài Cercopithecus"),
    ("072725", "chatterers", "noun", "/ˈtʃætərərz/", "kẻ nói liến thoắng; chim sáo bồ"),
    ("072726", "claustrums", "noun", "/ˈklɔːstrəmz/", "tường chất xám mỏng trong não"),
    ("072727", "coccidioidomycoses", "noun", "/kɒkˌsɪdiɔɪdoʊmaɪˈkoʊsiːz/", "bệnh nhiễm nấm thung lũng phổi"),
    ("072728", "cookstoves", "noun", "/ˈkʊkˌstoʊvz/", "bếp lò nấu ăn bằng củi hoặc gas"),
    ("072729", "copouts", "noun", "/ˈkɒpˌaʊts/", "cách thoái thác đùn đẩy (khẩu ngữ)"),
    ("072730", "culicidaes", "noun", "/kjʊˈlɪsɪˌdiːz/", "họ Muỗi trong bộ Hai cánh"),
    ("072731", "cuniculuses", "noun", "/kjʊˈnɪkjʊləsɪz/", "chi Chuột paca Nam Mỹ (Cuniculus)"),
    ("072732", "cyproheptadines", "noun", "/ˌsɪproʊˈhɛptədiːnz/", "thuốc kháng histamin cyproheptadin"),
    ("072733", "dishrags", "noun", "/ˈdɪʃˌræɡz/", "giẻ lau rửa chén bát (Mỹ)"),
    ("072734", "djiboutians", "noun", "/dʒɪˈbuːtiənz/", "người dân nước Djibouti Đông Phi"),
    ("072735", "dooryards", "noun", "/ˈdɔːrˌjɑːrdz/", "sân nhỏ ngay trước cửa nhà"),
    ("072736", "dunkards", "noun", "/ˈdʌŋkərdz/", "tín đồ giáo phái Rửa tội Dunkard"),
    ("072737", "egises", "noun", "/ˈiːdʒɪsɪz/", "chiếc khiên che chở của thần Zeus"),
    ("072738", "empennages", "noun", "/ˌɒmpəˈnɑːʒɪz/", "bộ cánh đuôi ổn định máy bay"),
    ("072739", "enses", "noun", "/ˈɛnsɪz/", "chi Trai móng tay vỏ dài (Ensis)"),
    ("072740", "fetoproteins", "noun", "/ˌfiːtoʊˈproʊtiːnz/", "protein huyết thanh bào thai"),
    ("072741", "frypans", "noun", "/ˈfraɪˌpænz/", "chảo rán chiên thực phẩm"),
    ("072742", "gaduses", "noun", "/ˈɡeɪdəsɪz/", "chi Cá tuyết Đại Tây Dương Gadus"),
    ("072743", "gametogeneses", "noun", "/ɡəˌmiːtoʊˈdʒɛnɪsiːz/", "quá trình tạo giao tử sinh dục"),
    ("072744", "gantlets", "noun", "/ˈɡɔːntlɪts/", "hàng roi phạt chạy qua; găng giáp"),
    ("072745", "grapnels", "noun", "/ˈɡræpnəlz/", "móc neo nhiều chấu kéo móc đồ"),
    ("072746", "gravimeters", "noun", "/ɡræˈvɪmɪtərz/", "trọng lực kế đo trường hấp dẫn"),
    ("072747", "grillworks", "noun", "/ˈɡrɪlˌwɜːrks/", "khung song sắt hoa văn trang trí"),
    ("072748", "grotesqueries", "noun", "/ɡroʊˈtɛskəriz/", "nét quái dị kỳ quặc lố bịch"),
    ("072749", "hamartomas", "noun", "/ˌhæmɑːrˈtoʊməz/", "u mô thừa lành tính hamartoma"),
    ("072750", "headsails", "noun", "/ˈhɛdˌseɪlz/", "cánh buồm giương ở mũi tàu thuyền"),
    ("072751", "hegiras", "noun", "/hɪˈdʒaɪrəz/", "cuộc thiên di Hijrah năm 622 (Hồi)"),
    ("072752", "homophiles", "noun", "/ˈhoʊməˌfaɪlz/", "người đồng tính; tổ chức đồng tính"),
    ("072753", "hydruses", "noun", "/ˈhaɪdrəsɪz/", "chòm sao Thủy Xà phương Nam"),
    ("072754", "incoordinations", "noun", "/ɪnˌkoʊɔːrdɪˈneɪʃənz/", "sự mất phối hợp vận động cơ bắp"),
    ("072755", "interestingnesses", "noun", "/ˈɪntrɪstɪŋnəsɪz/", "tính thú vị hấp dẫn thu hút"),
    ("072756", "jabots", "noun", "/ʒæˈboʊz/", "dải ren xếp nếp trước ngực áo xưa"),
    ("072757", "jackanapeses", "noun", "/ˈdʒækəˌneɪpsɪz/", "kẻ xấc xược ngỗ ngược láo xược"),
    ("072758", "kansus", "noun", "/ˈkænsuːz/", "tỉnh Cam Túc ở tây bắc Trung Quốc"),
    ("072759", "kerosines", "noun", "/ˈkɛrəˌsiːnz/", "dầu hỏa nhiên liệu (cách viết Anh)"),
    ("072760", "khachaturians", "noun", "/ˌkɑːtʃəˈtʊəriənz/", "nhà soạn nhạc Aram Khachaturian"),
    ("072761", "knuckleboneses", "noun", "/ˈnʌkəlˌboʊnzɪz/", "trò thảy đá bắt xương (cổ điển)"),
    ("072762", "konquerors", "noun", "/ˈkɒŋkərərz/", "trình duyệt web Konqueror (KDE)"),
    ("072763", "laggers", "noun", "/ˈlæɡərz/", "người đi sau; thợ bọc cách nhiệt"),
    ("072764", "lanoxins", "noun", "/ləˈnɒksɪnz/", "thuốc trợ tim digoxin (Lanoxin)"),
    ("072765", "liepajas", "noun", "/ˈliːəpɑːjəz/", "thành phố cảng Liepāja ở Latvia"),
    ("072766", "limuli", "noun", "/ˈlɪmjʊˌlaɪ/", "chi Sam biển cổ đại (Limulus)"),
    ("072767", "manumits", "verb", "/ˌmænjʊˈmɪts/", "trả tự do giải phóng cho nô lệ"),
    ("072768", "manumitted", "verb", "/ˌmænjʊˈmɪtɪd/", "đã trả tự do giải phóng nô lệ"),
    ("072769", "manumitting", "verb", "/ˌmænjʊˈmɪtɪŋ/", "đang trả tự do giải phóng nô lệ"),
    ("072770", "marranos", "noun", "/məˈrɑːnoʊz/", "người Do Thái Tây Ban Nha cải đạo"),
    ("072771", "mastabas", "noun", "/ˈmæstəbəz/", "lăng mộ tường nghiêng Ai Cập cổ"),
    ("072772", "melanisms", "noun", "/ˈmɛləˌnɪzəmz/", "hiện tượng hắc tố biến màu đen"),
    ("072773", "molybdenites", "noun", "/məˈlɪbdɪˌnaɪts/", "quặng molypdenit (MoS2)"),
    ("072774", "mrtas", "noun", "/ˌɛm ɑːr tiː ˈeɪz/", "nhóm nổi dậy MRTA ở Peru"),
    ("072775", "murres", "noun", "/mɜːrz/", "chim biển anca mỏ nhọn Bắc Cực"),
    ("072776", "nadolols", "noun", "/ˈneɪdəˌlɒlz/", "thuốc chẹn beta tim mạch nadolol"),
    ("072777", "nares", "noun", "/ˈnɛəriːz/", "hai lỗ mũi (giải phẫu học)"),
    ("072778", "narises", "noun", "/ˈnɛərɪsɪz/", "lỗ mũi ngoài hoặc trong (y học)"),
    ("072779", "natterjacks", "noun", "/ˈnætərˌdʒæks/", "cóc chạy nhanh sọc vàng châu Âu"),
    ("072780", "nownesses", "noun", "/ˈnaʊnəsɪz/", "tính hiện hữu ngay trong hiện tại"),
    ("072781", "osteopetroses", "noun", "/ˌɒstioʊpɪˈtroʊsiːz/", "bệnh xương đặc hóa đá di truyền"),
    ("072782", "pancytopenias", "noun", "/ˌpænsaɪtəˈpiːniəz/", "hội chứng giảm ba dòng tế bào máu"),
    ("072783", "perdixes", "noun", "/ˈpɜːrdɪksɪz/", "chi Gà gô xám châu Âu (Perdix)"),
    ("072784", "phizes", "noun", "/fɪzɪz/", "họa sĩ minh họa Dickens (Phiz)"),
    ("072785", "piperines", "noun", "/ˈpɪpəˌriːnz/", "hợp chất tạo vị cay hạt tiêu đen"),
    ("072786", "plantsmans", "noun", "/ˈplæntsmənz/", "nhà trồng cây chuyên sưu tầm giống"),
    ("072787", "proviruses", "noun", "/proʊˈvaɪrəsɪz/", "tiền vi-rút tích hợp vào ADN chủ"),
    ("072788", "pteropuses", "noun", "/ˈtɛrəpəsɪz/", "chi Dơi quạ ăn quả khổng lồ"),
    ("072789", "puerarias", "noun", "/pjʊˈɛəriəz/", "cây sắn dây thuộc chi Pueraria"),
    ("072790", "pyromancers", "noun", "/ˈpaɪroʊˌmænsərz/", "thầy bói xem quẻ bằng ngọn lửa"),
    ("072791", "quarrymans", "noun", "/ˈkwɒrɪmənz/", "công nhân khai thác đá tại mỏ đá"),
    ("072792", "quiddities", "noun", "/ˈkwɪdɪtiz/", "bản chất cốt lõi; lý lẽ bắt bẻ vụn"),
    ("072793", "resurveys", "noun", "/riːˈsɜːrveɪz/", "cuộc khảo sát đo đạc điều tra lại"),
    ("072794", "sadomasochists", "noun", "/ˌsædoʊˈmæsəkɪsts/", "người thực hành BDSM bạo-khổ dâm"),
    ("072795", "scheffleras", "noun", "/ʃɛˈflɛərəz/", "cây ngũ gia bì thuộc chi Schefflera"),
    ("072796", "secretaires", "noun", "/ˌsɛkrɪˈtɛərz/", "tủ bàn viết có nắp gập kéo ra"),
    ("072797", "shipways", "noun", "/ˈʃɪpˌweɪz/", "triền đà đóng và hạ thủy tàu biển"),
    ("072798", "silphiums", "noun", "/ˈsɪlfiəmz/", "cây thảo dược cổ đại Silphium"),
    ("072799", "silverworks", "noun", "/ˈsɪlvərˌwɜːrks/", "đồ chế tác bằng bạc; xưởng làm bạc"),
    ("072800", "soleas", "noun", "/ˈsoʊliəz/", "chi Cá bơn lưỡi trâu châu Âu Solea"),
    ("072801", "solenopses", "noun", "/ˌsɒlɪˈnɒpsiːz/", "chi Kiến lửa đốt đau (Solenopsis)"),
    ("072802", "sopors", "noun", "/ˈsoʊpɔːrz/", "trạng thái ngủ li bì sâu (y học)"),
]

with open("scratch/b35_r06_raw_p3.json") as f:
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

with open("scratch/b35_r06_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r06_p3.json OK")
