import json

items = [
    ("068403", "incuses", "noun", "/ˈɪŋkjʊsɪz/", "xương đe nhỏ nằm trong tai giữa"),
    ("068404", "insurrectionists", "noun", "/ˌɪnsəˈrɛkʃənɪsts/", "kẻ nổi loạn khởi nghĩa chống đối"),
    ("068405", "interrelates", "verb", "/ˌɪntərɪˈleɪts/", "liên hệ tương hỗ qua lại với nhau"),
    ("068406", "interrelating", "verb", "/ˌɪntərɪˈleɪtɪŋ/", "đang liên kết tương tác lẫn nhau"),
    ("068407", "intussusceptions", "noun", "/ˌɪntəsəˈsɛpʃənz/", "bệnh lồng ruột tắc nghẽn ở trẻ"),
    ("068408", "iroquoians", "noun", "/ˌɪrəˈkwɔɪənz/", "ngữ hệ và dân tộc Iroquois Bắc Mỹ"),
    ("068409", "jubilated", "verb", "/ˈdʒuːbɪˌleɪtɪd/", "đã reo hò vui sướng hân hoan"),
    ("068410", "jubilates", "verb", "/ˈdʒuːbɪˌleɪts/", "vui mừng hân hoan nhảy múa reo hò"),
    ("068411", "jubilating", "verb", "/ˈdʒuːbɪˌleɪtɪŋ/", "đang vui sướng hân hoan rạng rỡ"),
    ("068412", "kelts", "noun", "/kɛlts/", "người Celt cổ đại vùng Tây Âu"),
    ("068413", "kovnos", "noun", "/ˈkɒvnoʊz/", "thành phố Kaunas Litva (tên cũ)"),
    ("068414", "lascars", "noun", "/ˈlæskərz/", "thủy thủ Ấn Độ trên tàu châu Âu"),
    ("068415", "levitras", "noun", "/ləˈviːtrəz/", "thuốc trị rối loạn cương Levitra"),
    ("068416", "lisinoprils", "noun", "/laɪˈsɪnəˌprɪlz/", "thuốc hạ huyết áp ức chế lisinopril"),
    ("068417", "loniceras", "noun", "/ləˈnɪsərəz/", "cây hoa kim ngân thuộc chi Lonicera"),
    ("068418", "lupinuses", "noun", "/luːˈpaɪnəsɪz/", "hoa lupin đậu cánh chim chi Lupinus"),
    ("068419", "mandaras", "noun", "/mɑːnˈdɑːrəz/", "tiếng Mandara ở Cameroon Nigeria"),
    ("068420", "medocs", "noun", "/meɪˈdɒks/", "rượu vang đỏ vùng Médoc nước Pháp"),
    ("068421", "mujahidins", "noun", "/ˌmuːdʒəˈhiːdiːnz/", "chiến binh thánh chiến Hồi giáo"),
    ("068422", "multiversities", "noun", "/ˌmʌltiˈvɜːrsɪtiz/", "hệ thống đại học lớn đa phân hiệu"),
    ("068423", "musettes", "noun", "/mjuːˈzɛts/", "kèn túi nhỏ Pháp; túi đeo vai quân"),
    ("068424", "nasopharynges", "noun", "/ˌneɪzoʊfəˈrɪndʒiːz/", "vùng vòm họng mũi sau khoang mũi"),
    ("068425", "nasopharynxes", "noun", "/ˌneɪzoʊˈfærɪŋksɪz/", "vòm họng mũi thông giữa mũi họng"),
    ("068426", "nominalisms", "noun", "/ˈnɒmɪnəˌlɪzəmz/", "thuyết duy danh trong triết học"),
    ("068427", "nopals", "noun", "/ˈnoʊpəlz/", "cây xương rồng lê gai ăn nopal"),
    ("068428", "novocains", "noun", "/ˈnoʊvəˌkeɪnz/", "thuốc gây tê nha khoa novocain"),
    ("068429", "occipita", "noun", "/ɒkˈsɪpɪtə/", "vùng xương chẩm phía sau hộp sọ"),
    ("068430", "occiputs", "noun", "/ˈɒksɪˌpʊts/", "phần gáy chẩm phía sau đầu"),
    ("068431", "optatives", "noun", "/ˈɒptətɪvz/", "thức cầu khẩn trong ngữ pháp cổ"),
    ("068432", "osteoblasts", "noun", "/ˈɒstioʊˌblæsts/", "tế bào tạo xương nguyên bào xương"),
    ("068433", "oxaloacetates", "noun", "/ɒkˌsæloʊˈæsɪˌteɪts/", "muối oxaloaxetat chu trình Krebs"),
    ("068434", "pageboys", "noun", "/ˈpeɪdʒˌbɔɪz/", "kiểu tóc ngang vai úp; tiểu đồng"),
    ("068435", "panfishes", "noun", "/ˈpænˌfɪʃɪz/", "cá nhỏ vừa cỡ rán cả con trên chảo"),
    ("068436", "pegmatites", "noun", "/ˈpɛɡməˌtaɪts/", "đá macma hạt thô lớn pegmatit"),
    ("068437", "petrified", "verb", "/ˈpɛtrɪˌfaɪd/", "đã hóa đá; đã làm chết điếng vì sợ"),
    ("068438", "petrifies", "verb", "/ˈpɛtrɪˌfaɪz/", "hóa đá cổ vật; làm kinh hãi sững sờ"),
    ("068439", "photoemissions", "noun", "/ˌfoʊtoʊɪˈmɪʃənz/", "hiện tượng phát xạ quang điện tử"),
    ("068440", "plosives", "noun", "/ˈploʊsɪvz/", "phụ âm bật hơi tắc hoàn toàn"),
    ("068441", "polyploids", "noun", "/ˈpɒlɪˌplɔɪdz/", "sinh vật có bộ nhiễm sắc thể đa bội"),
    ("068442", "prayerbooks", "noun", "/ˈprɛərˌbʊks/", "sách kinh cầu nguyện nghi lễ"),
    ("068443", "puruses", "noun", "/pʊˈruːzɪz/", "sông Purús chảy qua Peru Brazil"),
    ("068444", "rashers", "noun", "/ˈræʃərz/", "lát thịt xông khói rán; cá mú đỏ"),
    ("068445", "reimposed", "verb", "/ˌriːɪmˈpoʊzd/", "đã tái áp đặt lại thuế hoặc luật"),
    ("068446", "reimposes", "verb", "/ˌriːɪmˈpoʊzɪz/", "áp đặt trở lại quy định cấm đoán"),
    ("068447", "reimposing", "verb", "/ˌriːɪmˈpoʊzɪŋ/", "đang áp đặt trở lại thuế hay lệnh"),
    ("068448", "ringtails", "noun", "/ˈrɪŋˌteɪlz/", "gấu mèo đuôi khoang; thú có túi Úc"),
    ("068449", "ritualists", "noun", "/ˈrɪtʃʊəlɪsts/", "người coi trọng nghi thức tôn giáo"),
    ("068450", "romanticists", "noun", "/roʊˈmæntɪsɪsts/", "người theo trường phái Lãng mạn"),
    ("068451", "rumexes", "noun", "/ˈruːmɛksɪz/", "cây chút chít thuộc chi Rumex"),
    ("068452", "sclerotinias", "noun", "/ˌsklɪərəˈtɪniəz/", "nấm thối trắng cây Sclerotinia"),
    ("068453", "selvages", "noun", "/ˈsɛlvɪdʒɪz/", "biên vải dệt chắc không tưa sợi"),
    ("068454", "sheepfolds", "noun", "/ˈʃiːpˌfoʊldz/", "chuồng trại quây rào nhốt đàn cừu"),
    ("068455", "shfs", "noun", "/ˌɛs eɪtʃ ˈɛfs/", "sóng vô tuyến siêu cao tần SHF"),
    ("068456", "shorteners", "noun", "/ˈʃɔːrtənərz/", "tác nhân rút ngắn; công cụ gọn link"),
    ("068457", "shufflers", "noun", "/ˈʃʌflərz/", "máy hoặc người xáo trộn bài; kẻ lê"),
    ("068458", "sodalites", "noun", "/ˈsoʊdəˌlaɪts/", "đá khoáng vật màu xanh lam sodalit"),
    ("068459", "soleuses", "noun", "/ˈsoʊliəsɪz/", "cơ dép sâu ở bắp chân người"),
    ("068460", "splenomegalies", "noun", "/ˌspliːnoʊˈmɛɡəliz/", "chứng sưng phình to lá lách (y học)"),
    ("068461", "spondylolistheses", "noun", "/ˌspɒndɪloʊlɪsˈθiːsiːz/", "chứng trượt đốt sống thắt lưng"),
    ("068462", "steerers", "noun", "/ˈstɪərərz/", "người cầm lái bẻ lái tàu xe"),
    ("068463", "sudsier", "adj", "/ˈsʌdziər/", "nhiều bọt xà phòng sủi tăm hơn"),
    ("068464", "sudsiest", "adj", "/ˈsʌdziɪst/", "nhiều bọt xà phòng sủi tăm nhất"),
    ("068465", "syndics", "noun", "/ˈsɪndɪks/", "ủy viên đại diện pháp lý hội đồng"),
    ("068466", "tejus", "noun", "/ˈteɪdʒuːz/", "thằn lằn lớn tegu Nam Mỹ"),
    ("068467", "termeses", "noun", "/ˈtɜːrmiːzɪz/", "chi mối đất nhiệt đới Termes"),
    ("068468", "theogonies", "noun", "/θiˈɒɡəniz/", "thần phả học nguồn gốc chư thần"),
    ("068469", "thomisms", "noun", "/ˈtoʊˌmɪzəmz/", "triết học thần học Thánh Tôma Aquin"),
    ("068470", "todies", "noun", "/ˈtoʊdiz/", "chim xanh nhỏ mỏ dẹt vùng Caribe"),
    ("068471", "triremes", "noun", "/ˈtraɪˌriːmz/", "chiến thuyền ba tầng chèo cổ đại"),
    ("068472", "waxwings", "noun", "/ˈwæksˌwɪŋz/", "chim sáp cánh đốm đỏ ăn quả mọng"),
    ("068473", "windjammers", "noun", "/ˈwɪndˌdʒæmərz/", "thuyền buồm thương mại cỡ lớn"),
    ("068474", "yhvhs", "noun", "/ˈjɑːweɪz/", "tên Chúa Giê-hô-va Do Thái YHWH"),
    ("068475", "abkhazians", "noun", "/æbˈkɑːziənz/", "người và ngôn ngữ vùng Abkhazia"),
    ("068476", "aestheticians", "noun", "/ˌɛsθəˈtɪʃənz/", "chuyên viên chăm sóc thẩm mỹ da"),
    ("068477", "amphibolites", "noun", "/æmˈfɪbəˌlaɪts/", "đá biến chất chứa khoáng amphibol"),
    ("068478", "analectas", "noun", "/ˌænəˈlɛktəz/", "tuyển tập danh ngôn trích lục cổ"),
    ("068479", "arameans", "noun", "/ˌærəˈmiːənz/", "người dân tộc Aram cổ đại Syria"),
    ("068480", "bacteroideses", "noun", "/ˌbæktəˈrɔɪdiːzɪz/", "vi khuẩn kỵ khí đường ruột"),
    ("068481", "barbets", "noun", "/ˈbɑːrbɪts/", "chim cu rốc đầu màu nhiệt đới"),
    ("068482", "barongs", "noun", "/bəˈrɒŋz/", "dao bản rộng barong Philippines"),
    ("068483", "benefactions", "noun", "/ˌbɛnɪˈfækʃənz/", "việc từ thiện quyên góp tiền của"),
    ("068484", "bigeyes", "noun", "/ˈbɪɡˌaɪz/", "cá mắt to đỏ sống vùng rạn biển"),
    ("068485", "bolshevists", "noun", "/ˈboʊlʃəvɪsts/", "đảng viên Bolshevik cách mạng Nga"),
    ("068486", "borzois", "noun", "/ˈbɔːrzɔɪz/", "giống chó săn sói cao lớn của Nga"),
    ("068487", "byelorussias", "noun", "/ˌbjɛləˈrʌʃəz/", "nước Belarus (tên thời Xô viết)"),
    ("068488", "celecoxibs", "noun", "/ˌsɛləˈkɒksɪbz/", "thuốc kháng viêm giảm đau celecoxib"),
    ("068489", "celestas", "noun", "/səˈlɛstəz/", "đàn chuông bàn phím âm thanh thanh"),
    ("068490", "changjiangs", "noun", "/tʃɑːŋˈdʒjɑːŋz/", "sông Trường Giang của Trung Quốc"),
    ("068491", "cobalamins", "noun", "/koʊˈbæləmɪnz/", "vitamin B12 thiết yếu tạo máu"),
    ("068492", "colchicums", "noun", "/ˈkɒltʃɪkəmz/", "cây nghệ tây đồng cỏ mùa thu độc"),
    ("068493", "collectivisations", "noun", "/kəˌlɛktɪvaɪˈzeɪʃənz/", "chính sách tập thể hóa nông nghiệp"),
    ("068494", "companionways", "noun", "/kəmˈpænjənˌweɪz/", "cầu thang nối các tầng boong tàu"),
    ("068495", "conniptions", "noun", "/kəˈnɪpʃənz/", "cơn giận dữ bộc phát mất bình tĩnh"),
    ("068496", "coppersmiths", "noun", "/ˈkɒpərˌsmɪθs/", "thợ gò hàn chế tác đồ bằng đồng"),
    ("068497", "coreopses", "noun", "/ˌkɔːriˈɒpsiːz/", "hoa cúc cánh bướm vàng Coreopsis"),
    ("068498", "cosinesses", "noun", "/ˈkoʊzinəsɪz/", "cảm giác ấm cúng thoải mái dễ chịu"),
    ("068499", "covilles", "noun", "/ˈkoʊvɪlz/", "nhà thực vật học Mỹ F. Coville"),
    ("068500", "cowtowns", "noun", "/ˈkaʊˌtaʊnz/", "thị trấn chăn nuôi bò miền Tây Mỹ"),
    ("068501", "dhaulagiris", "noun", "/ˌdaʊləˈɡɪriz/", "đỉnh núi cao Dhaulagiri ở Nepal"),
    ("068502", "diminuendos", "noun", "/dɪˌmɪnjʊˈɛndoʊz/", "đoạn nhạc nhỏ dần âm lượng"),
]

with open("scratch/b34_r07_raw_p5.json") as f:
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

with open("scratch/b34_r07_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r07_p5.json OK")
