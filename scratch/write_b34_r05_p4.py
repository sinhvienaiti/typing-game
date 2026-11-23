import json

items = [
    ("067303", "scraggier", "adj", "/ˈskræɡiər/", "gầy nhom hơn; mọc lởm chởm thưa hơn"),
    ("067304", "scraggiest", "adj", "/ˈskræɡiɪst/", "gầy nhom nhất; lởm chởm thưa nhất"),
    ("067305", "seedbeds", "noun", "/ˈsiːdˌbɛdz/", "luống đất ươm gieo hạt giống"),
    ("067306", "sentes", "noun", "/ˈsɛnteɪz/", "đồng tiền xu nhỏ sente của Lesotho"),
    ("067307", "signiors", "noun", "/ˈsiːnjɔːrz/", "quý ông; ngài (cách gọi cổ Ý)"),
    ("067308", "signorinas", "noun", "/ˌsiːnjəˈriːnəz/", "cô thiếu nữ chưa chồng người Ý"),
    ("067309", "signorine", "noun", "/ˌsiːnjəˈriːneɪ/", "những cô gái trẻ chưa chồng ở Ý"),
    ("067310", "soaves", "noun", "/swɑːˈveɪz/", "rượu vang trắng Soave của Ý"),
    ("067311", "soteriologies", "noun", "/səˌtɪriˈɒlədʒiz/", "thần học nghiên cứu về sự cứu rỗi"),
    ("067312", "sphalerites", "noun", "/ˈsfæləˌraɪts/", "khoáng vật quặng kẽm sunfua chính"),
    ("067313", "spirometries", "noun", "/spaɪˈrɒmɪtriz/", "phép đo phế dung chức năng hô hấp"),
    ("067314", "stationers", "noun", "/ˈsteɪʃənərz/", "cửa hàng hoặc người bán văn phòng"),
    ("067315", "subjectivisms", "noun", "/səbˈdʒɛktɪˌvɪzəmz/", "thuyết chủ quan luận triết học"),
    ("067316", "syllabaries", "noun", "/ˈsɪləˌbɛriz/", "hệ chữ viết ký hiệu theo âm tiết"),
    ("067317", "szechwans", "noun", "/ˈsɛʃwɒnz/", "tỉnh Tứ Xuyên ở tây nam Trung Quốc"),
    ("067318", "tamarins", "noun", "/ˈtæmərɪnz/", "khỉ nhỏ bờm sư tử tamarin Nam Mỹ"),
    ("067319", "tanges", "noun", "/ˈtɑːŋɡeɪz/", "kiến trúc sư Nhật Kenzo Tange"),
    ("067320", "tartaries", "noun", "/ˈtɑːrtəriz/", "vùng lịch sử Tartary ở Trung Á"),
    ("067321", "teetotallers", "noun", "/ˈtiːˌtoʊtələrz/", "người kiêng rượu bia tuyệt đối"),
    ("067322", "theosophists", "noun", "/θiˈɒsəfɪsts/", "tín đồ theo thuyết thông thiên học"),
    ("067323", "thiries", "noun", "/ˈθɪriz/", "nhà thơ Bỉ Marcel Thiry"),
    ("067324", "thujas", "noun", "/ˈθjuːdʒəz/", "cây trắc bách diệp thuộc chi Thuja"),
    ("067325", "tombigbees", "noun", "/tɒmˈbɪɡbiz/", "sông Tombigbee ở miền nam Mỹ"),
    ("067326", "touchers", "noun", "/ˈtʌtʃərz/", "người chạm vào; quả bóng sát đích"),
    ("067327", "touchwoods", "noun", "/ˈtʌtʃˌwʊdz/", "gỗ mục bùi nhùi dễ bắt lửa"),
    ("067328", "trainloads", "noun", "/ˈtreɪnˌloʊdz/", "chuyến hàng hoặc khách đầy tàu hỏa"),
    ("067329", "trollers", "noun", "/ˈtroʊlərz/", "kẻ khiêu khích mạng; người câu rê"),
    ("067330", "whickered", "verb", "/ˈwɪkərd/", "đã hí khẽ (ngựa); kêu khẽ rụt rè"),
    ("067331", "whickering", "verb", "/ˈwɪkərɪŋ/", "đang hí khẽ (ngựa)"),
    ("067332", "whickers", "noun", "/ˈwɪkərz/", "tiếng ngựa hí khẽ nhẹ nhàng"),
    ("067333", "whippoorwills", "noun", "/ˈwɪpərˌwɪlz/", "chim ăn đêm whippoorwill Bắc Mỹ"),
    ("067334", "workingmen", "noun", "/ˈwɜːrkɪŋˌmɛn/", "công nhân nam lao động chân tay"),
    ("067335", "wyrds", "noun", "/wɪərdz/", "định mệnh số phận (từ cổ Anh)"),
    ("067336", "alexander woollcott", "phrase", "/ˌælɪɡˈzændər ˈwʊlkɒt/", "nhà phê bình văn học Mỹ Woollcott"),
    ("067337", "amedeo avogadro", "phrase", "/ˌɑːməˈdeɪoʊ ˌɑːvəˈɡɑːdroʊ/", "nhà vật lý hóa học Ý Avogadro"),
    ("067338", "american maidenhair fern", "phrase", "/əˈmɛrɪkən ˈmeɪdənˌhɛər fɜːrn/", "cây dương xỉ tóc thần Mỹ"),
    ("067339", "annular scotoma", "phrase", "/ˈænjələr skəˈtoʊmə/", "ám điểm mù hình nhẫn thị trường"),
    ("067340", "asa dulcis", "phrase", "/ˈæsə ˈdʌlsɪs/", "nhựa thơm cánh kiến trắng benzoin"),
    ("067341", "bermuda maidenhair fern", "phrase", "/bərˈmjuːdə ˈmeɪdənˌhɛər fɜːrn/", "dương xỉ tóc thần nữ Bermuda"),
    ("067342", "blacktip shark", "phrase", "/ˈblækˌtɪp ʃɑːrk/", "cá mập vây đen sống vùng rạn san hô"),
    ("067343", "borrelia burgdorferi", "phrase", "/bəˈriːliə bɜːrɡˈdɔːrfəri/", "xoắn khuẩn gây bệnh Lyme truyền ve"),
    ("067344", "brittle maidenhair", "phrase", "/ˈbrɪtəl ˈmeɪdənˌhɛər/", "cây dương xỉ tóc tiên cọng giòn"),
    ("067345", "cascade penstemon", "phrase", "/kæˈskeɪd ˈpɛnstəmən/", "hoa mõm rồng núi Cascade Bắc Mỹ"),
    ("067346", "charles edouard jeanneret", "phrase", "/ʃɑːrlz eɪˈdwɑːr ʒɑːnˈreɪ/", "tên thật kiến trúc sư Le Corbusier"),
    ("067347", "chenopodium rubrum", "phrase", "/ˌkiːnəˈpoʊdiəm ˈruːbrəm/", "cây rau muối đỏ Bắc bán cầu"),
    ("067348", "citrus mealybug", "phrase", "/ˈsɪtrəs ˈmiːlibʌɡ/", "rệp sáp trắng hại cây cam quýt"),
    ("067349", "class ciliata", "phrase", "/klæs ˌsɪliˈeɪtə/", "lớp Trùng lông bơi đơn bào tiêm mao"),
    ("067350", "cliff penstemon", "phrase", "/klɪf ˈpɛnstəmən/", "hoa mõm rồng mọc vách đá"),
    ("067351", "climbing maidenhair fern", "phrase", "/ˈklaɪmɪŋ ˈmeɪdənˌhɛər fɜːrn/", "cây dương xỉ dây leo Bắc Mỹ"),
    ("067352", "draba verna", "phrase", "/ˈdrɑːbə ˈvɜːrnə/", "cây cỏ cải hoa trắng mùa xuân"),
    ("067353", "falco subbuteo", "phrase", "/ˈfælkoʊ səˈbjuːtioʊ/", "chim cắt hobi săn chuồn chuồn Á Âu"),
    ("067354", "family ericaceae", "phrase", "/ˈfæməli ˌɛrɪˈkeɪʃiː/", "họ Thạch nam gồm đỗ quyên việt quất"),
    ("067355", "family liliaceae", "phrase", "/ˈfæməli ˌlɪliˈeɪʃiː/", "họ Loa kèn thực vật một lá mầm"),
    ("067356", "farley maidenhair", "phrase", "/ˈfɑːrli ˈmeɪdənˌhɛər/", "dương xỉ tóc thần giống Farley"),
    ("067357", "franz lehar", "phrase", "/frɑːnts ˈleɪhɑːr/", "nhà soạn nhạc Áo-Hung Franz Lehár"),
    ("067358", "gene sarazen", "phrase", "/dʒiːn ˈsærəzən/", "vận động viên gôn Mỹ Gene Sarazen"),
    ("067359", "genus apatosaurus", "phrase", "/ˈdʒiːnəs əˌpætəˈsɔːrəs/", "chi khủng long cổ dài Apatosaurus"),
    ("067360", "genus asplenium", "phrase", "/ˈdʒiːnəs əˈspliːniəm/", "chi dương xỉ tổ điểu Asplenium"),
    ("067361", "genus cucumis", "phrase", "/ˈdʒiːnəs ˈkjuːkjʊmɪs/", "chi dưa chuột và dưa lưới Cucumis"),
    ("067362", "genus danaus", "phrase", "/ˈdʒiːnəs dəˈneɪəs/", "chi bướm chúa di cư Danaus"),
    ("067363", "genus elephas", "phrase", "/ˈdʒiːnəs ˈɛlɪfəs/", "chi voi châu Á Elephas"),
    ("067364", "genus grus", "phrase", "/ˈdʒiːnəs ɡrʌs/", "chi chim sếu lớn cổ dài Grus"),
    ("067365", "genus lolium", "phrase", "/ˈdʒiːnəs ˈloʊliəm/", "chi cỏ hắc mạch Lolium"),
    ("067366", "genus mammut", "phrase", "/ˈdʒiːnəs ˈmæmət/", "chi voi răng vú tiền sử Mammut"),
    ("067367", "genus penstemon", "phrase", "/ˈdʒiːnəs ˈpɛnstəmən/", "chi hoa mõm rồng Penstemon"),
    ("067368", "genus tradescantia", "phrase", "/ˈdʒiːnəs ˌtrædɪˈskænʃə/", "chi cây thài lài cảnh Tradescantia"),
    ("067369", "genus turdus", "phrase", "/ˈdʒiːnəs ˈtɜːrdəs/", "chi chim hoét hót hay Turdus"),
    ("067370", "hypoglycaemic agent", "phrase", "/ˌhaɪpoʊɡlaɪˈsiːmɪk ˈeɪdʒənt/", "thuốc hạ đường huyết trị tiểu đường"),
    ("067371", "john anthony ciardi", "phrase", "/dʒɒn ˈænθəni tʃɪˈɑːrdi/", "nhà thơ và dịch giả Mỹ John Ciardi"),
    ("067372", "john ciardi", "phrase", "/dʒɒn tʃɪˈɑːrdi/", "nhà thơ Mỹ John Ciardi"),
    ("067373", "katabatic wind", "phrase", "/ˌkætəˈbætɪk wɪnd/", "gió lạnh đổ xuống từ sườn núi cao"),
    ("067374", "klemens metternich", "phrase", "/ˈklɛmɛns ˈmɛtərnɪk/", "tể tướng Áo Klemens von Metternich"),
    ("067375", "lhasa apso", "phrase", "/ˈlɑːsə ˈæpsoʊ/", "giống chó lông dài Lhasa Apso Tây"),
    ("067376", "louis the wideawake", "phrase", "/ˈluːi ðə ˈwaɪdəˌweɪk/", "Vua Pháp Louis VI Người béo"),
    ("067377", "maidenhair fern", "phrase", "/ˈmeɪdənˌhɛər fɜːrn/", "cây dương xỉ tóc thần nữ"),
    ("067378", "meno mosso", "phrase", "/ˌmeɪnoʊ ˈmɒsoʊ/", "nhịp điệu chậm lại bớt (âm nhạc)"),
    ("067379", "miliary fever", "phrase", "/ˈmɪliəri ˈfiːvər/", "bệnh sốt phát ban nốt nhỏ (y học)"),
    ("067380", "miliary tuberculosis", "phrase", "/ˈmɪliəri tjuːˌbɜːrkjʊˈloʊsɪs/", "bệnh lao kê lan tỏa toàn thân"),
    ("067381", "mimosa pudica", "phrase", "/mɪˈmoʊsə ˈpjuːdɪkə/", "cây xấu hổ; cây trinh nữ khép lá"),
    ("067382", "mohandas karamchand gandhi", "phrase", "/moʊˈhɑːndəs kɑːˈrɑːmtʃɑːnd ˈɡɑːndi/", "lãnh tụ Ấn Độ Mahatma Gandhi"),
    ("067383", "monic polynomial", "phrase", "/ˈmɒnɪk ˌpɒlɪˈnoʊmiəl/", "đa thức đơn khởi hệ số đầu bằng 1"),
    ("067384", "mordecai richler", "phrase", "/ˌmɔːrdəˈkaɪ ˈrɪtʃlər/", "nhà văn Canada Mordecai Richler"),
    ("067385", "nagari script", "phrase", "/ˈnɑːɡəri skrɪpt/", "hệ chữ viết cổ Nagari của Ấn Độ"),
    ("067386", "nasal canthus", "phrase", "/ˈneɪzəl ˈkænθəs/", "khóe mắt trong phía sống mũi"),
    ("067387", "perchloric acid", "phrase", "/pərˈklɔːrɪk ˈæsɪd/", "axit vô cơ cực mạnh pecloric"),
    ("067388", "pincushion hakea", "phrase", "/ˈpɪnˌkʊʃən həˈkiːə/", "cây hakea hoa cầu gai Úc"),
    ("067389", "plantago psyllium", "phrase", "/plænˈteɪɡoʊ ˈsɪliəm/", "cây mã đề lấy vỏ hạt chất xơ"),
    ("067390", "point of periapsis", "phrase", "/pɔɪnt əv ˌpɛriˈæpsɪs/", "điểm cận tâm gần thiên thể nhất"),
    ("067391", "populus nigra italica", "phrase", "/ˈpɒpjʊləs ˈnaɪɡrə ɪˈtælɪkə/", "cây dương đen dáng thẳng Lombardy"),
    ("067392", "praying mantid", "phrase", "/ˈpreɪɪŋ ˈmæntɪd/", "bọ ngựa giơ hai chân trước bắt mồi"),
    ("067393", "radclyffe hall", "phrase", "/ˈrædklɪf hɔːl/", "nữ nhà văn Anh Radclyffe Hall"),
    ("067394", "raja batis", "phrase", "/ˈrɑːdʒə ˈbeɪtɪs/", "cá đuối gai xanh lớn châu Âu"),
    ("067395", "ringneck snake", "phrase", "/ˈrɪŋˌnɛk sneɪk/", "rắn khoang cổ màu vàng Bắc Mỹ"),
    ("067396", "rock penstemon", "phrase", "/rɒk ˈpɛnstəmən/", "hoa mõm rồng mọc trên vách đá"),
    ("067397", "seminiferous tubule", "phrase", "/ˌsɛmɪˈnɪfərəs ˈtjuːbjuːl/", "ống sinh tinh sản xuất tinh trùng"),
    ("067398", "snuffbox fern", "phrase", "/ˈsnʌfˌbɒks fɜːrn/", "cây dương xỉ túi hạt snuffbox"),
    ("067399", "tabes dorsalis", "phrase", "/ˈteɪbiːz dɔːrˈseɪlɪs/", "bệnh liệt tủy sống do giang mai"),
    ("067400", "temporal canthus", "phrase", "/ˈtɛmpərəl ˈkænθəs/", "khóe mắt ngoài phía thái dương"),
    ("067401", "temporalis muscle", "phrase", "/ˌtɛmpəˈrɑːlɪs ˈmʌsəl/", "cơ thái dương nâng hàm khi nhai"),
    ("067402", "theobroma cacao", "phrase", "/ˌθiːəˈbroʊmə kəˈkaʊ/", "cây ca cao lấy hạt làm sô cô la"),
]

with open("scratch/b34_r05_raw_p4.json") as f:
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

with open("scratch/b34_r05_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r05_p4.json OK")
