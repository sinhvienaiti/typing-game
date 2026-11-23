import json

items = [
    ("071503", "carminatives", "noun", "/kɑːrˈmɪnətɪvz/", "thuốc tiêu hơi chống đầy bụng"),
    ("071504", "catechumens", "noun", "/ˌkætɪˈkjuːmənz/", "người dự tòng học giáo lý"),
    ("071505", "cheroots", "noun", "/ʃəˈruːts/", "xì gà cắt phẳng hai đầu cheroot"),
    ("071506", "chinquapins", "noun", "/ˈtʃɪŋkəˌpɪnz/", "cây hoặc hạt dẻ bụi chinquapin"),
    ("071507", "coeloms", "noun", "/ˈsiːləmz/", "khoang cơ thể chính (thể xoang)"),
    ("071508", "coitions", "noun", "/koʊˈɪʃənz/", "hành vi giao hợp tình dục (y học)"),
    ("071509", "coloradans", "noun", "/ˌkɒləˈrɑːdənz/", "người dân bang Colorado của Mỹ"),
    ("071510", "cryogens", "noun", "/ˈkraɪədʒənz/", "chất làm lạnh sâu âm độ"),
    ("071511", "cuppers", "noun", "/ˈkʌpərz/", "người nếm thử trà cà phê; giác hơi"),
    ("071512", "cutpurses", "noun", "/ˈkʌtˌpɜːrsɪz/", "tên móc túi cắt hầu bao (cổ)"),
    ("071513", "declawed", "verb", "/diːˈklɔːd/", "đã cắt bỏ móng vuốt (mèo)"),
    ("071514", "declawing", "verb", "/diːˈklɔːɪŋ/", "đang cắt bỏ móng vuốt"),
    ("071515", "declaws", "verb", "/diːˈklɔːz/", "cắt bỏ móng vuốt động vật"),
    ("071516", "diazoniums", "noun", "/ˌdaɪəˈzoʊniəmz/", "muối hoặc ion diazoni hữu cơ"),
    ("071517", "dipterocarps", "noun", "/dɪpˈtɛrəˌkɑːrps/", "cây họ Dầu nhiệt đới gỗ quý"),
    ("071518", "dominicuses", "noun", "/ˈdɒmɪnɪkəsɪz/", "ngày Chủ nhật; người tên Dominicus"),
    ("071519", "doorposts", "noun", "/ˈdɔːrˌpoʊsts/", "thanh đứng khung cửa ra vào"),
    ("071520", "ethenes", "noun", "/ˈɛθiːnz/", "khí etylen / eten (C2H4)"),
    ("071521", "exarchates", "noun", "/ˈɛksɑːrˌkeɪts/", "khu tổng trấn Byzantine; tòa tổng"),
    ("071522", "flaviviruses", "noun", "/ˈfleɪvɪˌvaɪrəsɪz/", "họ vi-rút Flavivirus (sốt vàng)"),
    ("071523", "fontannes", "noun", "/fɒnˈtænz/", "nữ diễn viên Mỹ Lynn Fontanne"),
    ("071524", "fornaxes", "noun", "/ˈfɔːrnæksɪz/", "chòm sao Thiên Lô (Lò Rèn)"),
    ("071525", "fossilizes", "verb", "/ˈfɒsəˌlaɪzɪz/", "hóa thạch; trở nên bảo thủ lạc hậu"),
    ("071526", "fossilizing", "verb", "/ˈfɒsəˌlaɪzɪŋ/", "đang hóa thạch; dần trở nên cổ hủ"),
    ("071527", "gadabouts", "noun", "/ˈɡædəˌbaʊts/", "người thích rong chơi đây đó"),
    ("071528", "gitanas", "noun", "/hɪˈtɑːnəz/", "cô gái người Digan Tây Ban Nha"),
    ("071529", "glycyrrhizas", "noun", "/ˌɡlɪsɪˈraɪzəz/", "chi Cây cam thảo (Glycyrrhiza)"),
    ("071530", "goonies", "noun", "/ˈɡuːniz/", "chim hải âu lớn; kẻ ngốc nghếch"),
    ("071531", "gorals", "noun", "/ˈɡɔːrəlz/", "sơn dương goral dãy Himalaya"),
    ("071532", "greenmarkets", "noun", "/ˈɡriːnˌmɑːrkɪts/", "chợ nông sản tươi xanh ngoài trời"),
    ("071533", "hallels", "noun", "/ˈhælɛlz/", "bài thánh vịnh ca ngợi Chúa Hallel"),
    ("071534", "hamitics", "noun", "/həˈmɪtɪks/", "nhóm ngôn ngữ Hamite Bắc Phi"),
    ("071535", "harlequinades", "noun", "/ˌhɑːrlɪkwɪˈneɪdz/", "trò diễn hề kịch câm kiểu Ý"),
    ("071536", "hebbels", "noun", "/ˈhɛbəlz/", "nhà soạn kịch Đức Friedrich Hebbel"),
    ("071537", "howdahs", "noun", "/ˈhaʊdəz/", "kiệu ngồi có mui đặt trên lưng voi"),
    ("071538", "hydralazines", "noun", "/haɪˈdræləziːnz/", "thuốc giãn mạch trị cao huyết áp"),
    ("071539", "hydrillas", "noun", "/haɪˈdrɪləz/", "rong đuôi chó thủy sinh hydrilla"),
    ("071540", "impaneled", "verb", "/ɪmˈpænəld/", "đã lập danh sách bồi thẩm đoàn"),
    ("071541", "impaneling", "verb", "/ɪmˈpænəlɪŋ/", "đang lập danh sách bồi thẩm đoàn"),
    ("071542", "inamoratas", "noun", "/ɪnˌæməˈrɑːtəz/", "người tình nữ; cô gái được yêu"),
    ("071543", "indited", "verb", "/ɪnˈdaɪtɪd/", "đã sáng tác, biên soạn (văn thơ)"),
    ("071544", "indites", "verb", "/ɪnˈdaɪts/", "sáng tác, viết nên (trang trọng)"),
    ("071545", "inditing", "verb", "/ɪnˈdaɪtɪŋ/", "đang sáng tác, viết nên văn thơ"),
    ("071546", "industrialises", "verb", "/ɪnˈdʌstriəˌlaɪzɪz/", "công nghiệp hóa nền kinh tế (Anh)"),
    ("071547", "industrialising", "verb", "/ɪnˈdʌstriəˌlaɪzɪŋ/", "đang công nghiệp hóa (Anh)"),
    ("071548", "keratoplasties", "noun", "/ˌkɛrətoʊˈplæstiz/", "phẫu thuật ghép giác mạc mắt"),
    ("071549", "kinglets", "noun", "/ˈkɪŋlɪts/", "chim tước mào vàng châu Mỹ"),
    ("071550", "kingsnakes", "noun", "/ˈkɪŋˌsneɪks/", "rắn vua không độc săn rắn khác"),
    ("071551", "korchnois", "noun", "/kɔːrtʃˈnɔɪz/", "kỳ thủ cờ vua Viktor Korchnoi"),
    ("071552", "liberalists", "noun", "/ˈlɪbərəlɪsts/", "người ủng hộ chủ nghĩa tự do"),
    ("071553", "limned", "verb", "/lɪmd/", "đã vẽ minh họa; đã phác họa (cổ)"),
    ("071554", "limns", "verb", "/lɪmz/", "vẽ minh họa; mô tả phác họa (cổ)"),
    ("071555", "luffas", "noun", "/ˈlʌfəz/", "cây mướp hương; xơ mướp khô"),
    ("071556", "lustrums", "noun", "/ˈlʌstrəmz/", "chu kỳ năm năm (La Mã cổ đại)"),
    ("071557", "lyallpurs", "noun", "/ˈlaɪəlˌpʊərz/", "thành phố Faisalabad (tên cũ)"),
    ("071558", "maaloxes", "noun", "/ˈmeɪlɒksɪz/", "thuốc kháng axit dạ dày Maalox"),
    ("071559", "mackles", "noun", "/ˈmækəlz/", "vết lem nhòe khi in (nghề in)"),
    ("071560", "manats", "noun", "/məˈnɑːts/", "đồng tiền manat vùng Caspi"),
    ("071561", "manicottis", "noun", "/ˌmænɪˈkɒtiz/", "mì ống lớn nhồi phô mai manicotti"),
    ("071562", "mealies", "noun", "/ˈmiːliz/", "bắp ngô (tiếng Anh Nam Phi)"),
    ("071563", "megacolons", "noun", "/ˌmɛɡəˈkoʊlənz/", "bệnh phình giãn đại tràng"),
    ("071564", "menhirs", "noun", "/ˈmɛnhɪərz/", "trụ đá cự thạch dựng đứng cổ đại"),
    ("071565", "menorrhagias", "noun", "/ˌmɛnəˈreɪdʒəz/", "chứng rong kinh kéo dài"),
    ("071566", "milfoils", "noun", "/ˈmɪlˌfɔɪlz/", "cây cỏ thi yarrow (lá xẻ mịn)"),
    ("071567", "myiases", "noun", "/maɪˈaɪəsiːz/", "bệnh giòi ruồi ký sinh ở mô"),
    ("071568", "naysayings", "noun", "/ˈneɪˌseɪɪŋz/", "sự phủ nhận bác bỏ phản đối"),
    ("071569", "nestorianisms", "noun", "/nɛˈstɔːriəˌnɪzəmz/", "giáo thuyết Cảnh giáo (Nestorius)"),
    ("071570", "normalizers", "noun", "/ˈnɔːrməˌlaɪzərz/", "nhân tố chuẩn hóa bình thường hóa"),
    ("071571", "nostocs", "noun", "/ˈnɒstɒks/", "vi khuẩn lam tảo đá chi Nostoc"),
    ("071572", "oilskins", "noun", "/ˈɔɪlˌskɪnz/", "áo mưa vải bạt tẩm dầu chống nước"),
    ("071573", "origanums", "noun", "/əˈrɪɡənəmz/", "cây kinh giới cay chi Origanum"),
    ("071574", "pekineses", "noun", "/ˌpiːkɪˈniːzɪz/", "chó Bắc Kinh lông dài mặt xệ"),
    ("071575", "peperomias", "noun", "/ˌpɛpəˈroʊmiəz/", "cây lá ngọc lan càng cua Peperomia"),
    ("071576", "phalangists", "noun", "/fəˈlændʒɪsts/", "đảng viên phái Falange Tây Ban Nha"),
    ("071577", "phosphoproteins", "noun", "/ˌfɒsfoʊˈproʊtiːnz/", "protein gắn nhóm photphat"),
    ("071578", "pityriases", "noun", "/ˌpɪtɪˈraɪəsiːz/", "bệnh vảy phấn da (vảy cám)"),
    ("071579", "platanuses", "noun", "/ˈplætənəsɪz/", "cây tiêu huyền lá phong Platanus"),
    ("071580", "playboxes", "noun", "/ˈpleɪˌbɒksɪz/", "hộp đựng đồ chơi trẻ em"),
    ("071581", "plevnas", "noun", "/ˈplɛvnəz/", "thành phố Pleven ở Bulgaria"),
    ("071582", "popguns", "noun", "/ˈpɒpˌɡʌnz/", "súng hơi nút bần đồ chơi trẻ em"),
    ("071583", "postludes", "noun", "/ˈpoʊstˌluːdz/", "đoạn nhạc kết thúc lễ hoặc tác phẩm"),
    ("071584", "primordiums", "noun", "/praɪˈmɔːrdiəmz/", "mầm phôi sơ khai cơ quan"),
    ("071585", "propanediols", "noun", "/ˌproʊpeɪnˈdaɪɒlz/", "hợp chất rượu propanediol"),
    ("071586", "proteaceaes", "noun", "/ˌproʊtiˈeɪʃiˌiːz/", "họ Quắn hoa (mắc ca, ngân hoa)"),
    ("071587", "quasiparticles", "noun", "/ˌkwɑːziˈpɑːrtɪkəlz/", "chuẩn hạt trong vật lý chất rắn"),
    ("071588", "ravelings", "noun", "/ˈrævəlɪŋz/", "sợi chỉ tơ bị xổ bung rời ra"),
    ("071589", "reoviruses", "noun", "/ˌriːoʊˈvaɪrəsɪz/", "họ vi-rút đường hô hấp tiêu hóa"),
    ("071590", "rhodochrosites", "noun", "/ˌroʊdəˈkroʊsaɪts/", "đá quý cacbonat mangan hồng"),
    ("071591", "salps", "noun", "/sælps/", "động vật sống biển thân trong suốt"),
    ("071592", "saones", "noun", "/soʊnz/", "sông Saône ở miền đông nước Pháp"),
    ("071593", "saturnias", "noun", "/səˈtɜːrniəz/", "chi Ngài hoàng đế lớn (Saturnia)"),
    ("071594", "scalier", "adj", "/ˈskeɪliər/", "nhiều vảy hơn; đóng cáu cặn hơn"),
    ("071595", "scaliest", "adj", "/ˈskeɪliɪst/", "nhiều vảy nhất; đóng cáu cặn nhất"),
    ("071596", "scutellarias", "noun", "/ˌskjuːtəˈlɛəriəz/", "chi Cây hoàng cầm (cây mũ đầu)"),
    ("071597", "sgraffiti", "noun", "/zɡrɑːˈfiːti/", "kỹ thuật cạo vữa vẽ tranh tường"),
    ("071598", "sgraffitos", "noun", "/zɡrɑːˈfiːtoʊz/", "tranh tường cạo lớp vữa sgraffito"),
    ("071599", "sheenier", "adj", "/ˈʃiːniər/", "bóng mượt óng ả hơn"),
    ("071600", "sheeniest", "adj", "/ˈʃiːniɪst/", "bóng mượt óng ả nhất"),
    ("071601", "shovelfuls", "noun", "/ˈʃʌvəlˌfʊlz/", "lượng xúc đầy một lưỡi xẻng"),
    ("071602", "sickrooms", "noun", "/ˈsɪkˌruːmz/", "phòng chăm sóc người bệnh tại nhà"),
]

with open("scratch/b35_r04_raw_p1.json") as f:
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

with open("scratch/b35_r04_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r04_p1.json OK")
