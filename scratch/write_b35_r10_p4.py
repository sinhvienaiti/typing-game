import json

rows = [
    ("074803", "papaverines", "noun", "/pəˈpævəriːnz/", "thuốc chống co thắt papaverin"),
    ("074804", "paraesthesias", "noun", "/ˌpærɪsˈθiːʒəz/", "chứng dị cảm tê bì (y học)"),
    ("074805", "parotitises", "noun", "/ˌpærəˈtaɪtɪsɪz/", "bệnh viêm tuyến mang tai (quai bị)"),
    ("074806", "peregrinations", "noun", "/ˌpɛrɪɡrɪˈneɪʃənz/", "chuyến du hành dài ngày"),
    ("074807", "periwigs", "noun", "/ˈpɛrɪwɪɡz/", "tóc giả nam dài (thế kỷ 17-18)"),
    ("074808", "phycoerythrins", "noun", "/ˌfaɪkoʊɪˈrɪθrɪnz/", "sắc tố đỏ tảo phycoerythrin"),
    ("074809", "planetesimals", "noun", "/ˌplænɪˈtɛsəməlz/", "vi hành tinh (thiên văn học)"),
    ("074810", "poxviruses", "noun", "/ˈpɒksˌvaɪrəsɪz/", "họ virus đậu mùa (Poxvirus)"),
    ("074811", "probabilisms", "noun", "/ˈprɒbəblɪzəmz/", "thuyết xác suất; thuyết cái nhiên"),
    ("074812", "profiteroles", "noun", "/prəˈfɪtəroʊlz/", "bánh su kem phủ sô-cô-la"),
    ("074813", "psyllas", "noun", "/ˈsɪləz/", "bọ nhảy hại lá (chi Psylla)"),
    ("074814", "pterocarpuses", "noun", "/ˌtɛrəˈkɑːrpəsɪz/", "chi gỗ giáng hương (Pterocarpus)"),
    ("074815", "quintettes", "noun", "/kwɪnˈtɛts/", "nhóm ngũ tấu; bản nhạc ngũ tấu"),
    ("074816", "raphanuses", "noun", "/ˈræfənəsɪz/", "chi củ cải (Raphanus)"),
    ("074817", "remudas", "noun", "/rɪˈmuːdəz/", "đàn ngựa dự bị (chăn bò Mỹ)"),
    ("074818", "retamas", "noun", "/rəˈtɑːməz/", "chi cây bụi kim tước Retama"),
    ("074819", "rhodophytas", "noun", "/ˌroʊdəˈfaɪtəz/", "ngành tảo đỏ (Rhodophyta)"),
    ("074820", "romanized", "verb", "/ˈroʊmənaɪzd/", "đã Latinh hóa (chữ viết)"),
    ("074821", "romanizes", "verb", "/ˈroʊmənaɪzɪz/", "Latinh hóa (chữ viết)"),
    ("074822", "romanizing", "verb", "/ˈroʊmənaɪzɪŋ/", "Latinh hóa (chữ viết)"),
    ("074823", "roundednesses", "noun", "/ˈraʊndɪdnəsɪz/", "tính tròn trịa; sự hoàn chỉnh"),
    ("074824", "ruritanians", "noun", "/ˌrʊərɪˈteɪniənz/", "cư dân xứ tưởng tượng Ruritania"),
    ("074825", "sapodillas", "noun", "/ˌsæpəˈdɪləz/", "quả hồng xiêm (lồng mứt)"),
    ("074826", "schottisches", "noun", "/ˈʃɒtɪʃɪz/", "điệu nhảy dân gian schottische"),
    ("074827", "scolyti", "noun", "/ˈskɒlɪtaɪ/", "chi bọ đục vỏ cây (Scolytus)"),
    ("074828", "shortgrasses", "noun", "/ˈʃɔːrtˌɡræsɪz/", "cỏ thảo nguyên thấp (Bắc Mỹ)"),
    ("074829", "sovietisms", "noun", "/ˈsoʊviətɪzəmz/", "đặc trưng Xô viết; lối nói Liên Xô"),
    ("074830", "stableboys", "noun", "/ˈsteɪbəlˌbɔɪz/", "chú bé phụ việc chuồng ngựa"),
    ("074831", "sterculias", "noun", "/stɜːrˈkjuːliəz/", "chi cây trôm (Sterculia)"),
    ("074832", "stomachers", "noun", "/ˈstʌməkərz/", "yếm thêu che ngực váy áo cổ"),
    ("074833", "sylvilaguses", "noun", "/ˌsɪlvɪˈleɪɡəsɪz/", "chi thỏ đuôi bông (Sylvilagus)"),
    ("074834", "tankfuls", "noun", "/ˈtæŋkfʊlz/", "lượng đầy một bồn chứa"),
    ("074835", "thiobacilli", "noun", "/ˌθaɪoʊbəˈsɪlaɪ/", "vi khuẩn lưu huỳnh Thiobacillus"),
    ("074836", "thomomyses", "noun", "/θəˈmɒmɪsɪz/", "chi chuột túi má (Thomomys)"),
    ("074837", "thundershowers", "noun", "/ˈθʌndərˌʃaʊərz/", "mưa rào kèm sấm chớp"),
    ("074838", "timpanists", "noun", "/ˈtɪmpənɪsts/", "nhạc công chơi trống định âm"),
    ("074839", "tomographs", "noun", "/ˈtɒməɡræfs/", "máy chụp cắt lớp (y học)"),
    ("074840", "tramplers", "noun", "/ˈtræmplərz/", "kẻ giẫm đạp lên"),
    ("074841", "tridacnas", "noun", "/trɪˈdæknəz/", "chi trai tai tượng khổng lồ"),
    ("074842", "umbelliferaes", "noun", "/ʌmˌbɛlɪˈfɛriːz/", "họ Hoa tán (Apiaceae cổ)"),
    ("074843", "unicyclists", "noun", "/ˈjuːnɪˌsaɪklɪsts/", "người đi xe đạp một bánh"),
    ("074844", "vizors", "noun", "/ˈvaɪzərz/", "mặt nạ mũ giáp; lưỡi trai mũ"),
    ("074845", "warreners", "noun", "/ˈwɒrənərz/", "người trông coi khu nuôi thỏ săn"),
    ("074846", "wickiups", "noun", "/ˈwɪkiʌps/", "lều mái vòm lá cây wickiup (Mỹ)"),
    ("074847", "zabagliones", "noun", "/ˌzɑːbəlˈjoʊniz/", "món kem trứng rượu vang Ý"),
    ("074848", "zygomas", "noun", "/zaɪˈɡoʊməz/", "xương gò má; cung gò má"),
    ("074849", "ajugas", "noun", "/əˈdʒuːɡəz/", "chi cây cân cốt thảo (Ajuga)"),
    ("074850", "alabamans", "noun", "/ˌæləˈbæmənz/", "người dân bang Alabama (Mỹ)"),
    ("074851", "amenorrhoeas", "noun", "/eɪˌmɛnəˈriːəz/", "chứng vô kinh (y học)"),
    ("074852", "anglicizing", "verb", "/ˈæŋɡlɪsaɪzɪŋ/", "Anh hóa (ngôn ngữ, phong tục)"),
    ("074853", "anguises", "noun", "/ˈæŋɡwɪsɪz/", "chi thằn lằn giun (Anguis)"),
    ("074854", "armerias", "noun", "/ɑːrˈmɪriəz/", "chi hoa cúc biển thrift (Armeria)"),
    ("074855", "aztreonams", "noun", "/æzˈtriːənæmz/", "kháng sinh aztreonam"),
    ("074856", "balagans", "noun", "/ˈbæləɡænz/", "nhà kho sàn (Siberia); rạp hát hội"),
    ("074857", "beroes", "noun", "/ˈbɪroʊz/", "sứa lược không xúc tu Beroe"),
    ("074858", "berrettas", "noun", "/bəˈrɛtəz/", "mũ nồi mềm; mũ giáo sĩ biretta"),
    ("074859", "breechblocks", "noun", "/ˈbriːtʃˌblɒks/", "khối khóa nòng pháo; quy lát súng"),
    ("074860", "burets", "noun", "/bjʊˈrɛts/", "ống chuẩn độ buret (hóa học)"),
    ("074861", "burgraves", "noun", "/ˈbɜːrɡreɪvz/", "thủ lĩnh thành quách Đức thời xưa"),
    ("074862", "callinecteses", "noun", "/ˌkælɪˈnɛktiːz/", "chi cua xanh bơi (Callinectes)"),
    ("074863", "carcharhinuses", "noun", "/ˌkɑːrkəˈraɪnəsɪz/", "chi cá mập trắng mắt trắng"),
    ("074864", "carousals", "noun", "/kəˈraʊzəlz/", "cuộc chè chén say sưa; vòng xoay"),
    ("074865", "cenchruses", "noun", "/ˈsɛŋkrəsɪz/", "chi cỏ gai cát (Cenchrus)"),
    ("074866", "cicers", "noun", "/ˈsaɪsərz/", "chi cây đậu gà (Cicer)"),
    ("074867", "ciconias", "noun", "/sɪˈkoʊniəz/", "chi chim hạc, cò trắng (Ciconia)"),
    ("074868", "copaibas", "noun", "/koʊˈpaɪbəz/", "nhựa dầu thơm copaiba (Nam Mỹ)"),
    ("074869", "cuons", "noun", "/ˈkjuːɒnz/", "chi sói lửa châu Á (Cuon alpinus)"),
    ("074870", "cyclopias", "noun", "/saɪˈkloʊpiəz/", "dị tật một mắt bẩm sinh (y học)"),
    ("074871", "cypraeas", "noun", "/sɪˈpriːəz/", "chi ốc tiền xu, ốc sứ (Cypraea)"),
    ("074872", "delbrucks", "noun", "/ˈdɛlbrʊks/", "nhà sinh học Max Delbruck (Nobel)"),
    ("074873", "docetisms", "noun", "/doʊˈsiːtɪzəmz/", "thuyết Ảo ảnh Kitô học (Docetism)"),
    ("074874", "embonpoints", "noun", "/ˌɒ̃bɒ̃ˈpwæ̃/", "dáng người mập mạp đẫy đà"),
    ("074875", "erinaceuses", "noun", "/ˌɛrɪˈneɪʃəsɪz/", "chi nhím gai châu Âu (Erinaceus)"),
    ("074876", "fatihahs", "noun", "/ˈfɑːtɪhɑːz/", "chương mở đầu Kinh Qur'an (Fatihah)"),
    ("074877", "feathertops", "noun", "/ˈfɛðərˌtɒps/", "cỏ lông vũ (Pennisetum villosum)"),
    ("074878", "flocculated", "verb", "/ˈflɒkjəleɪtɪd/", "đã kết bông; keo tụ thành bông"),
    ("074879", "flocculates", "verb", "/ˈflɒkjəleɪts/", "kết bông; keo tụ thành bông"),
    ("074880", "flocculating", "verb", "/ˈflɒkjəleɪtɪŋ/", "kết bông; keo tụ thành bông"),
    ("074881", "flybridges", "noun", "/ˈflaɪˌbrɪdʒɪz/", "boong lái hở trên nóc du thuyền"),
    ("074882", "funiculuses", "noun", "/fjuːˈnɪkjələsɪz/", "cuống noãn; thừng rốn; thừng tinh"),
    ("074883", "fusspots", "noun", "/ˈfʌspɒts/", "người hay cằn nhằn cầu toàn vặt"),
    ("074884", "gallimaufries", "noun", "/ˌɡælɪˈmɔːfriz/", "mớ hổ lốn; tập hợp lộn xộn"),
    ("074885", "genserics", "noun", "/ˈɡɛnsərɪks/", "vua Genseric (bộ tộc Vandal)"),
    ("074886", "givennesses", "noun", "/ˈɡɪvənnəsɪz/", "tính hiển nhiên; điều mặc nhiên"),
    ("074887", "glauconites", "noun", "/ˈɡlɔːkənaɪts/", "khoáng vật lục glauconit"),
    ("074888", "gombrowiczes", "noun", "/ɡɒmˈbrɒvɪtʃɪz/", "nhà văn Witold Gombrowicz (Ba Lan)"),
    ("074889", "goosanders", "noun", "/ˈɡuːˌsændərz/", "vịt mỏ nhọn lớn (Mergus merganser)"),
    ("074890", "groundmasses", "noun", "/ˈɡraʊndˌmæsɪz/", "chất nền khoáng vật (địa chất)"),
    ("074891", "haemolyses", "noun", "/hɪˈmɒlɪsiːz/", "sự tan máu (dung huyết)"),
    ("074892", "hebraists", "noun", "/ˈhiːbreɪɪsts/", "học giả tiếng Do Thái (Hebrew)"),
    ("074893", "hedgefunds", "noun", "/ˈhɛdʒfʌndz/", "quỹ đầu cơ (tài chính)"),
    ("074894", "integralities", "noun", "/ˌɪntɪˈɡrælɪtiz/", "tính toàn vẹn; sự trọn vẹn"),
    ("074895", "intercommunions", "noun", "/ˌɪntərkəˈmjuːnjənz/", "sự hiệp thông giữa các giáo hội"),
    ("074896", "izars", "noun", "/ɪˈzɑːrz/", "trang phục vải quấn Hồi giáo izar"),
    ("074897", "lochias", "noun", "/ˈloʊkiəz/", "sản dịch sau sinh (y học)"),
    ("074898", "logograms", "noun", "/ˈlɒɡəɡræmz/", "ký tự ghi ý (như chữ Hán)"),
    ("074899", "maigres", "noun", "/ˈmeɪɡərz/", "cá lù đù biển maigre (châu Âu)"),
    ("074900", "mastoiditides", "noun", "/ˌmæstɔɪˈdaɪtɪdiːz/", "bệnh viêm xương chũm tai (y học)"),
    ("074901", "mellarils", "noun", "/ˈmɛlərɪlz/", "thuốc an thần Mellaril"),
    ("074902", "mercouris", "noun", "/mɛrˈkʊriz/", "nữ diễn viên Melina Mercouri"),
]

with open("scratch/b35_r10_raw_p4.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

assert len(raw) == len(rows) == 100
out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, rows):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} vs {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} vs {hw}"
    assert len(vi) <= 35, f"vi too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.count("/") == 2 and not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"bad ipa: {hw} -> {ipa}"
    r["pos"] = pos
    r["ipa"] = ipa
    r["vi"] = vi
    r["status"] = "reviewed"
    out.append(r)

with open("scratch/b35_r10_p4.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b35_r10_p4 saved OK")
