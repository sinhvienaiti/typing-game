import json

items = [
    ("071703", "prevacids", "noun", "/ˈprɛvəsɪdz/", "thuốc trị trào ngược Prevacid"),
    ("071704", "psychodynamicses", "noun", "/ˌsaɪkoʊdaɪˈnæmɪksɪz/", "tâm động lực học (tâm lý)"),
    ("071705", "putrescines", "noun", "/pjuːˈtrɛsiːnz/", "hợp chất sinh học thối putrescine"),
    ("071706", "respighis", "noun", "/rɛˈspiːɡiz/", "nhà soạn nhạc Ý Ottorino Respighi"),
    ("071707", "romanticizations", "noun", "/roʊˌmæntɪsaɪˈzeɪʃənz/", "sự lãng mạn hóa lý tưởng hóa"),
    ("071708", "rossbaches", "noun", "/ˈrɒsbɑːks/", "trận Rossbach năm 1757 ở Đức"),
    ("071709", "ruddled", "verb", "/ˈrʌdəld/", "đã đánh dấu đất son đỏ; làm đục"),
    ("071710", "ruddling", "verb", "/ˈrʌdlɪŋ/", "đang đánh dấu son đỏ; làm đục"),
    ("071711", "secobarbitals", "noun", "/ˌsiːkoʊˈbɑːrbɪˌtɑːlz/", "thuốc ngủ barbiturat secobarbital"),
    ("071712", "shinglers", "noun", "/ˈʃɪŋɡlərz/", "thợ lợp mái ván lợp; máy ép xỉ"),
    ("071713", "sinkiangs", "noun", "/ˌsɪnkiˈæŋz/", "khu tự trị Tân Cương (tên cũ)"),
    ("071714", "sises", "noun", "/ˈsaɪzɪz/", "mặt sáu xúc xắc; kích cỡ (từ cũ)"),
    ("071715", "speechmakings", "noun", "/ˈspiːtʃˌmeɪkɪŋz/", "việc đọc diễn văn diễn thuyết"),
    ("071716", "sphericities", "noun", "/sfɪˈrɪsɪtiz/", "độ cầu (mức độ giống hình cầu)"),
    ("071717", "spiracles", "noun", "/ˈspaɪrəkəlz/", "lỗ thở côn trùng; lỗ phun nước"),
    ("071718", "stambouls", "noun", "/stæmˈbuːlz/", "thành phố Istanbul (tên cũ)"),
    ("071719", "staymans", "noun", "/ˈsteɪmənz/", "giống táo chua giòn Stayman"),
    ("071720", "telefaxed", "verb", "/ˈtɛlɪˌfækst/", "đã gửi văn bản qua máy fax"),
    ("071721", "telefaxes", "verb", "/ˈtɛlɪˌfæksɪz/", "gửi văn bản qua máy fax"),
    ("071722", "telefaxing", "verb", "/ˈtɛlɪˌfæksɪŋ/", "đang gửi văn bản qua máy fax"),
    ("071723", "terabits", "noun", "/ˈtɛrəˌbɪts/", "đơn vị dữ liệu terabit (10^12 bit)"),
    ("071724", "thyrotoxicoses", "noun", "/ˌθaɪroʊtɒksɪˈkoʊsiːz/", "hội chứng nhiễm độc giáp cường giáp"),
    ("071725", "toadfishes", "noun", "/ˈtoʊdˌfɪʃɪz/", "cá cóc biển đầu to miệng rộng"),
    ("071726", "tofranils", "noun", "/ˈtɒfrənɪlz/", "thuốc chống trầm cảm Tofranil"),
    ("071727", "towages", "noun", "/ˈtoʊɪdʒɪz/", "dịch vụ lai dắt tàu xe; phí kéo"),
    ("071728", "trinitarianisms", "noun", "/ˌtrɪnɪˈtɛəriəˌnɪzəmz/", "học thuyết Chúa Ba Ngôi Ki-tô"),
    ("071729", "uuts", "noun", "/ˌjuː juː ˈtiːz/", "nguyên tố hóa học ununtri (Nh)"),
    ("071730", "vdus", "noun", "/ˌviː diː ˈjuːz/", "màn hình hiển thị máy tính (VDU)"),
    ("071731", "versants", "noun", "/ˈvɜːrsənts/", "sườn dốc chung một phía dãy núi"),
    ("071732", "allopathies", "noun", "/əˈlɒpəθiz/", "y học Tây y đối chứng (allopathy)"),
    ("071733", "ambulated", "verb", "/ˈæmbjʊˌleɪtɪd/", "đã đi lại tản bộ; di chuyển được"),
    ("071734", "ambulates", "verb", "/ˈæmbjʊˌleɪts/", "đi lại bước đi (y học, trang trọng)"),
    ("071735", "ambulating", "verb", "/ˈæmbjʊˌleɪtɪŋ/", "đang đi lại di chuyển (y học)"),
    ("071736", "anthologists", "noun", "/ænˈθɒlədʒɪsts/", "người biên soạn tuyển tập văn thơ"),
    ("071737", "aquilegias", "noun", "/ˌækwɪˈliːdʒəz/", "hoa bồ câu columbine chi Aquilegia"),
    ("071738", "augites", "noun", "/ˈɔːdʒaɪts/", "khoáng vật silicat sẫm màu augit"),
    ("071739", "australopithecines", "noun", "/ɒˌstræloʊˈpɪθɪˌsiːnz/", "vượn người cổ Australopithecus"),
    ("071740", "balbriggans", "noun", "/bælˈbrɪɡənz/", "vải dệt kim cotton Balbriggan"),
    ("071741", "baronetages", "noun", "/ˈbærənɪtɪdʒɪz/", "tầng lớp nam tước thế tập Anh"),
    ("071742", "batnas", "noun", "/ˈbætnəz/", "thành phố Batna ở đông bắc Algeria"),
    ("071743", "beachballs", "noun", "/ˈbiːtʃˌbɔːlz/", "bóng hơi chơi trên bãi biển"),
    ("071744", "bellyfuls", "noun", "/ˈbɛliˌfʊlz/", "lượng ăn no căng bụng; quá đủ ngấy"),
    ("071745", "bertillons", "noun", "/ˌbɛərtiˈjɒnz/", "hệ thống nhân trắc học Bertillon"),
    ("071746", "bialies", "noun", "/biˈɑːliz/", "bánh mì tròn nướng nhân hành bialy"),
    ("071747", "bolshies", "noun", "/ˈboʊlʃiz/", "người Bolshevik; kẻ chống đối (Anh)"),
    ("071748", "booteses", "noun", "/boʊˈoʊtiːzɪz/", "chòm sao Mục Phu (Boötes)"),
    ("071749", "bordelaises", "noun", "/ˌbɔːrdəˈleɪzɪz/", "xốt rượu vang đỏ tủy xương Pháp"),
    ("071750", "caudexes", "noun", "/ˈkɔːdɛksɪz/", "gốc thân phình; gốc rễ cây cau dừa"),
    ("071751", "caudices", "noun", "/ˈkɔːdɪsiːz/", "gốc thân phình; gốc thân cau dừa"),
    ("071752", "cefuroximes", "noun", "/ˌsɛfjʊˈrɒksiːmz/", "thuốc kháng sinh cefuroxime"),
    ("071753", "charivaris", "noun", "/ˌʃɑːrɪˈvɑːriz/", "màn khua chiêng gõ nồi trêu chọc"),
    ("071754", "chlordiazepoxides", "noun", "/ˌklɔːrdaɪæzɪˈpɒksaɪdz/", "thuốc an thần chlordiazepoxide"),
    ("071755", "chyles", "noun", "/kaɪlz/", "dưỡng trấp (dịch bạch huyết béo)"),
    ("071756", "cigarets", "noun", "/ˌsɪɡəˈrɛts/", "điếu thuốc lá (cách viết rút gọn)"),
    ("071757", "cladonias", "noun", "/kləˈdoʊniəz/", "địa y tuần lộc thuộc chi Cladonia"),
    ("071758", "cocyti", "noun", "/koʊˈsaɪtaɪ/", "sông than khóc Cocytus âm phủ"),
    ("071759", "contextualisms", "noun", "/kənˈtɛkstʃuəˌlɪzəmz/", "chủ nghĩa ngữ cảnh bối cảnh"),
    ("071760", "copyholds", "noun", "/ˈkɒpiˌhoʊldz/", "chế độ thuê đất phong kiến Anh cổ"),
    ("071761", "cryptomerias", "noun", "/ˌkrɪptəˈmɪəriəz/", "cây tuyết tùng Nhật Bản (sugi)"),
    ("071762", "cuscutas", "noun", "/kʌsˈkjuːtəz/", "cây dây tơ hồng ký sinh (Cuscuta)"),
    ("071763", "cycases", "noun", "/ˈsaɪkəsɪz/", "cây tuế vạn tuế thuộc chi Cycas"),
    ("071764", "darnels", "noun", "/ˈdɑːrnəlz/", "cỏ độc mọc lẫn lúa mạch (Lolium)"),
    ("071765", "demarches", "noun", "/deɪˈmɑːrʃɪz/", "động thái ngoại giao; công hàm"),
    ("071766", "dematerialized", "verb", "/ˌdiːməˈtɪəriəˌlaɪzd/", "đã phi vật chất hóa; đã tan biến"),
    ("071767", "dematerializes", "verb", "/ˌdiːməˈtɪəriəˌlaɪzɪz/", "phi vật chất hóa; làm tan biến mất"),
    ("071768", "dematerializing", "verb", "/ˌdiːməˈtɪəriəˌlaɪzɪŋ/", "đang phi vật chất hóa; tan biến"),
    ("071769", "depigmentations", "noun", "/diːˌpɪɡmɛnˈteɪʃənz/", "sự mất sắc tố trên da hoặc tóc"),
    ("071770", "edmontosauruses", "noun", "/ɛdˌmɒntəˈsɔːrəsɪz/", "khủng long mỏ vịt Edmontosaurus"),
    ("071771", "effused", "verb", "/ɪˈfjuːzd/", "đã tràn ra, tỏa ra, tràn dịch"),
    ("071772", "effuses", "verb", "/ɪˈfjuːzɪz/", "tràn ra, tỏa ra, rò dịch (y học)"),
    ("071773", "effusing", "verb", "/ɪˈfjuːzɪŋ/", "đang tràn ra, đang tỏa ra"),
    ("071774", "electrocauteries", "noun", "/ɪˌlɛktroʊˈkɔːtəriz/", "kỹ thuật đốt điện cầm máu cắt mô"),
    ("071775", "electroplated", "verb", "/ɪˈlɛktroʊˌpleɪtɪd/", "đã mạ điện kim loại lên bề mặt"),
    ("071776", "electroplates", "noun", "/ɪˈlɛktroʊˌpleɪts/", "vật dụng mạ điện; mạ điện phủ lớp"),
    ("071777", "eragrostises", "noun", "/ˌɛrəˈɡrɒstɪsɪz/", "cỏ tình yêu thuộc chi Eragrostis"),
    ("071778", "ergotamines", "noun", "/ɜːrˈɡɒtəmiːnz/", "thuốc trị đau nửa đầu ergotamine"),
    ("071779", "faqirs", "noun", "/fəˈkɪərz/", "tu sĩ khổ hạnh Hồi giáo hoặc Ấn"),
    ("071780", "firetraps", "noun", "/ˈfaɪərˌtræps/", "nhà dễ cháy thiếu lối thoát hiểm"),
    ("071781", "footgears", "noun", "/ˈfʊtˌɡɪərz/", "giày dép và ủng đi chân nói chung"),
    ("071782", "forestays", "noun", "/ˈfɔːrˌsteɪz/", "dây néo trước giữ cột buồm tàu"),
    ("071783", "fritillarias", "noun", "/ˌfrɪtɪˈlɛəriəz/", "hoa bối mẫu (bách hợp đốm ô vuông)"),
    ("071784", "frogfishes", "noun", "/ˈfrɒɡˌfɪʃɪz/", "cá cần câu vây tay có mồi nhử"),
    ("071785", "gameboards", "noun", "/ˈɡeɪmˌbɔːrdz/", "bàn cờ dùng cho trò chơi board game"),
    ("071786", "gigos", "noun", "/ˈɡaɪˌɡoʊz/", "quy luật rác vào rác ra (GIGO)"),
    ("071787", "glassfuls", "noun", "/ˈɡlæsˌfʊlz/", "lượng chất lỏng rót đầy một ly"),
    ("071788", "hatpins", "noun", "/ˈhætˌpɪnz/", "kim cài dài giữ chặt mũ vào tóc"),
    ("071789", "highjacked", "verb", "/ˈhaɪˌdʒækt/", "đã cướp máy bay hoặc xe chở hàng"),
    ("071790", "highjacks", "noun", "/ˈhaɪˌdʒæks/", "vụ cướp xe hàng hoặc máy bay"),
    ("071791", "illumed", "verb", "/ɪˈluːmd/", "đã chiếu sáng tỏa sáng (thi ca)"),
    ("071792", "illumes", "verb", "/ɪˈluːmz/", "chiếu sáng tỏa rạng (thi ca)"),
    ("071793", "illuming", "verb", "/ɪˈluːmɪŋ/", "đang chiếu sáng tỏa rạng (thi ca)"),
    ("071794", "islamized", "verb", "/ˈɪzləˌmaɪzd/", "đã Hồi giáo hóa theo đạo Hồi"),
    ("071795", "islamizes", "verb", "/ˈɪzləˌmaɪzɪz/", "Hồi giáo hóa theo đạo Hồi"),
    ("071796", "islamizing", "verb", "/ˈɪzləˌmaɪzɪŋ/", "đang Hồi giáo hóa theo đạo Hồi"),
    ("071797", "laffites", "noun", "/ləˈfiːts/", "hải tặc Pháp-Mỹ Jean Lafitte"),
    ("071798", "lappets", "noun", "/ˈlæpɪts/", "dải rủ trang trí mũ; dái thịt gà"),
    ("071799", "manakins", "noun", "/ˈmænəkɪnz/", "chim manakin rừng nhiệt đới Nam Mỹ"),
    ("071800", "marums", "noun", "/ˈmɛərəmz/", "cây cỏ xạ hương mèo Teucrium marum"),
    ("071801", "melkites", "noun", "/ˈmɛlkaɪts/", "tín đồ Giáo hội Công giáo Melkite"),
    ("071802", "memsahibs", "noun", "/ˈmɛmsɑːhɪbz/", "bà chủ người Âu ở Ấn Độ thuộc địa"),
]

with open("scratch/b35_r04_raw_p3.json") as f:
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

with open("scratch/b35_r04_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r04_p3.json OK")
