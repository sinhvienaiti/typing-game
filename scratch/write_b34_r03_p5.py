import json

items = [
    ("066403", "neriums", "noun", "/ˈnɪriəmz/", "cây trúc đào thuộc chi Nerium"),
    ("066404", "nonsmokers", "noun", "/ˌnɒnˈsmoʊkərz/", "người không hút thuốc lá"),
    ("066405", "ofos", "noun", "/ˈoʊfoʊz/", "người và ngôn ngữ Ofo Bắc Mỹ"),
    ("066406", "orchises", "noun", "/ˈɔːrkɪsɪz/", "hoa lan đất thuộc chi Orchis"),
    ("066407", "pedicabs", "noun", "/ˈpɛdɪˌkæbz/", "xe xích lô đạp chở khách"),
    ("066408", "pennyroyals", "noun", "/ˌpɛniˈrɔɪəlz/", "cây bạc hà hăng đuổi muỗi"),
    ("066409", "persistencies", "noun", "/pərˈsɪstənsiz/", "tính kiên trì bền bỉ kéo dài"),
    ("066410", "pfennige", "noun", "/ˈpfɛnɪɡə/", "tiền xu nhỏ pfennig cũ của Đức"),
    ("066411", "pfennigs", "noun", "/ˈfɛnɪɡz/", "đồng xu pfennig cũ của Đức"),
    ("066412", "pharmacopeiae", "noun", "/ˌfɑːrməkəˈpiːiː/", "bộ sách dược điển quy chuẩn thuốc"),
    ("066413", "pharmacopeias", "noun", "/ˌfɑːrməkəˈpiːəz/", "dược điển chính thức về dược phẩm"),
    ("066414", "photomontages", "noun", "/ˌfoʊtoʊmɒnˈtɑːʒɪz/", "bức ảnh cắt ghép từ nhiều tấm ảnh"),
    ("066415", "plasmaphereses", "noun", "/ˌplæzməfəˈriːsiːz/", "liệu pháp lọc tách huyết tương máu"),
    ("066416", "plutocrats", "noun", "/ˈpluːtəˌkræts/", "nhà tài phiệt giàu nắm quyền lực"),
    ("066417", "pomelos", "noun", "/ˈpɒməloʊz/", "quả bưởi vỏ dày vị thanh"),
    ("066418", "posterns", "noun", "/ˈpɒstərnz/", "cửa hậu nhỏ bí mật trong thành lũy"),
    ("066419", "proles", "noun", "/proʊlz/", "tầng lớp lao động vô sản (lóng)"),
    ("066420", "psychophysicses", "noun", "/ˌsaɪkoʊˈfɪzɪksɪz/", "ngành tâm vật lý học thực nghiệm"),
    ("066421", "pungs", "noun", "/pʌŋz/", "xe trượt tuyết thùng thấp một ngựa"),
    ("066422", "rededicated", "verb", "/riːˈdɛdɪˌkeɪtɪd/", "đã tái khánh thành; tái cống hiến"),
    ("066423", "rededicates", "verb", "/riːˈdɛdɪˌkeɪts/", "tái khánh thành; tái hiến dâng"),
    ("066424", "rededicating", "verb", "/riːˈdɛdɪˌkeɪtɪŋ/", "đang tái khánh thành; tái hiến dâng"),
    ("066425", "rhymers", "noun", "/ˈraɪmərz/", "người làm thơ vần; thi sĩ xoàng"),
    ("066426", "rissas", "noun", "/ˈrɪsəz/", "chi chim mòng biển xám Rissa"),
    ("066427", "secularisations", "noun", "/ˌsɛkjələraɪˈzeɪʃənz/", "quá trình thế tục hóa xã hội"),
    ("066428", "sericultures", "noun", "/ˈsɛrɪˌkʌltʃərz/", "nghề trồng dâu nuôi tằm lấy tơ"),
    ("066429", "shorthorns", "noun", "/ˈʃɔːrtˌhɔːrnz/", "giống bò thịt sừng ngắn Shorthorn"),
    ("066430", "sickbays", "noun", "/ˈsɪkˌbeɪz/", "phòng y tế bệnh xá trên tàu thủy"),
    ("066431", "sightlier", "adj", "/ˈsaɪtliər/", "dễ nhìn đẹp mắt hơn; ưa nhìn hơn"),
    ("066432", "sightliest", "adj", "/ˈsaɪtliɪst/", "dễ nhìn đẹp mắt nhất"),
    ("066433", "smudgier", "adj", "/ˈsmʌdʒiər/", "nhòe nhoẹt vết bẩn hơn"),
    ("066434", "smudgiest", "adj", "/ˈsmʌdʒiɪst/", "nhòe nhoẹt vết bẩn nhất"),
    ("066435", "solingens", "noun", "/ˈzoʊlɪŋənz/", "thành phố dao kéo Solingen Đức"),
    ("066436", "sorbents", "noun", "/ˈsɔːrbənts/", "chất hấp phụ dùng thu gom chất lỏng"),
    ("066437", "spackles", "noun", "/ˈspækəlz/", "bột bả ma tít trét vá tường"),
    ("066438", "stalagmites", "noun", "/stəˈlæɡmaɪts/", "măng đá mọc lên từ nền hang động"),
    ("066439", "sternas", "noun", "/ˈstɜːrnəz/", "chi chim nhạn biển Sterna"),
    ("066440", "tandoors", "noun", "/tænˈdʊərz/", "lò nướng đất sét hình trụ Ấn Độ"),
    ("066441", "trichlorides", "noun", "/traɪˈklɔːraɪdz/", "hợp chất hóa học triclorua"),
    ("066442", "ventolins", "noun", "/ˈvɛntəlɪnz/", "thuốc xịt cắt cơn hen Ventolin"),
    ("066443", "vervains", "noun", "/ˈvɜːrveɪnz/", "cây cỏ roi ngựa dược liệu"),
    ("066444", "volutes", "noun", "/vəˈluːts/", "họa tiết cuộn xoắn ốc đầu cột"),
    ("066445", "wisecracked", "verb", "/ˈwaɪzˌkrækt/", "đã buông lời nói đùa châm biếm"),
    ("066446", "wisecracking", "verb", "/ˈwaɪzˌkrækɪŋ/", "đang nói đùa hóm hỉnh châm biếm"),
    ("066447", "wisecracks", "noun", "/ˈwaɪzˌkræks/", "câu nói đùa dí dỏm hay châm chọc"),
    ("066448", "allium sativum", "phrase", "/ˈæliəm səˈtaɪvəm/", "cây tỏi gia vị và dược liệu"),
    ("066449", "amanita mappa", "phrase", "/ˌæməˈnaɪtə ˈmæpə/", "nấm độc giả tán vàng Amanita"),
    ("066450", "amour propre", "phrase", "/ˌæmʊər ˈprɒprə/", "lòng tự trọng; tính tự ái kiêu ngạo"),
    ("066451", "andrea guarneri", "phrase", "/ɑːnˈdreɪə ɡwɑːrˈnɛri/", "nghệ nhân làm đàn vĩ cầm Guarneri"),
    ("066452", "ardea occidentalis", "phrase", "/ˈɑːrdiə ˌɒksɪdɛnˈteɪlɪs/", "diệc lớn trắng châu Mỹ"),
    ("066453", "artemia salina", "phrase", "/ɑːrˈtiːmiə səˈlaɪnə/", "tôm nước mặn nhỏ làm thức ăn cá"),
    ("066454", "babinski sign", "phrase", "/bəˈbɪnski saɪn/", "dấu hiệu phản xạ bệnh lý Babinski"),
    ("066455", "benjamin ricketson tucker", "phrase", "/ˈbɛndʒəmɪn ˈrɪkətsən ˈtʌkər/", "triết gia vô chính phủ B. Tucker"),
    ("066456", "betula lenta", "phrase", "/ˈbɛtjʊlə ˈlɛntə/", "cây bạch dương ngọt hương dầu gió"),
    ("066457", "bladder fucus", "phrase", "/ˈblædər ˈfjuːkəs/", "tảo bẹ túi khí màu nâu"),
    ("066458", "blood corpuscle", "phrase", "/blʌd ˈkɔːrpʌsəl/", "tế bào máu gồm hồng cầu bạch cầu"),
    ("066459", "bog kalmia", "phrase", "/bɒɡ ˈkælmiə/", "cây nguyệt quế đầm lầy Bắc Mỹ"),
    ("066460", "chihuahuan desert", "phrase", "/tʃɪˈwɑːwən ˈdɛzərt/", "sa mạc Chihuahua ở Bắc Mỹ"),
    ("066461", "clostridium perfringens", "phrase", "/klɒˈstrɪdiəm pərˈfrɪndʒɛnz/", "vi khuẩn gây hoại thư sinh hơi"),
    ("066462", "copper pyrites", "phrase", "/ˈkɒpər ˈpaɪraɪts/", "quặng đồng hoàng thiết pyrit"),
    ("066463", "crotalus tigris", "phrase", "/ˈkrɒtələs ˈtaɪɡrɪs/", "rắn đuôi chuông vằn hổ tây nam Mỹ"),
    ("066464", "cypripedium album", "phrase", "/ˌsɪprɪˈpiːdiəm ˈælbəm/", "hoa lan hài trắng Bắc Mỹ"),
    ("066465", "eucalypt ovata", "phrase", "/ˈjuːkəlɪpt oʊˈveɪtə/", "cây bạch đàn đầm lầy lá xoan"),
    ("066466", "family curculionidae", "phrase", "/ˈfæməli kɜːrˌkjuːliˈɒnɪdiː/", "họ bọ cánh cứng vòi voi; họ mọt"),
    ("066467", "formica rufa", "phrase", "/ˈfɔːrmɪkə ˈruːfə/", "loài kiến gỗ đỏ rừng châu Âu"),
    ("066468", "garden loosestrife", "phrase", "/ˈɡɑːrdən ˈluːsˌstraɪf/", "cây trân châu vàng trồng vườn"),
    ("066469", "genus cypripedium", "phrase", "/ˈdʒiːnəs ˌsɪprɪˈpiːdiəm/", "chi hoa lan hài Cypripedium"),
    ("066470", "genus draba", "phrase", "/ˈdʒiːnəs ˈdrɑːbə/", "chi cỏ cải nhỏ Draba"),
    ("066471", "genus fucus", "phrase", "/ˈdʒiːnəs ˈfjuːkəs/", "chi tảo nâu bẹ biển Fucus"),
    ("066472", "genus lunda", "phrase", "/ˈdʒiːnəs ˈlʌndə/", "chi chim hải âu cổ rụt Lunda"),
    ("066473", "genus physalis", "phrase", "/ˈdʒiːnəs ˈfaɪsəlɪs/", "chi tầm bóp thù lù Physalis"),
    ("066474", "genus squalus", "phrase", "/ˈdʒiːnəs ˈskweɪləs/", "chi cá nhám gai Squalus"),
    ("066475", "genus treponema", "phrase", "/ˈdʒiːnəs ˌtrɛpəˈniːmə/", "chi xoắn khuẩn giang mai Treponema"),
    ("066476", "hiatal hernia", "phrase", "/haɪˈeɪtəl ˈhɜːrniə/", "thoát vị hoành qua khe thực quản"),
    ("066477", "homo heidelbergensis", "phrase", "/ˈhoʊmoʊ ˌhaɪdəlbɜːrˈɡɛnsɪs/", "người cổ đại Heidelberg tiền sử"),
    ("066478", "husking bee", "phrase", "/ˈhʌskɪŋ biː/", "buổi họp cộng đồng bóc bẹ ngô"),
    ("066479", "in vacuo", "phrase", "/ɪn ˈvækjuoʊ/", "trong môi trường chân không"),
    ("066480", "integumentary system", "phrase", "/ɪnˌtɛɡjʊˈmɛntəri ˈsɪstəm/", "hệ da lông móng bao bọc cơ thể"),
    ("066481", "juglans cinerea", "phrase", "/ˈdʒuːɡlənz sɪˈnɪriə/", "cây óc chó trắng lấy gỗ và hạt"),
    ("066482", "lama peruana", "phrase", "/ˈlɑːmə ˌpɛruːˈɑːnə/", "lạc đà không bướu llama Nam Mỹ"),
    ("066483", "little rhody", "phrase", "/ˈlɪtəl ˈroʊdi/", "biệt danh bang Rhode Island Mỹ"),
    ("066484", "loosestrife family", "phrase", "/ˈluːsˌstraɪf ˈfæməli/", "họ Tử vi; họ Bằng lăng"),
    ("066485", "louis the stammerer", "phrase", "/ˈluːi ðə ˈstæmərər/", "Vua Pháp Louis II Người Nói Lắp"),
    ("066486", "luis bunuel", "phrase", "/luːˈiːs buːnˈjwɛl/", "đạo diễn siêu thực Luis Buñuel"),
    ("066487", "magnetic pyrites", "phrase", "/mæɡˈnɛtɪk ˈpaɪraɪts/", "quặng sắt từ pyrrhotit"),
    ("066488", "morone americana", "phrase", "/məˈroʊni əˌmɛrɪˈkeɪnə/", "cá vược trắng Bắc Mỹ Morone"),
    ("066489", "morus rubra", "phrase", "/ˈmɔːrəs ˈruːbrə/", "cây dâu tằm quả đỏ Bắc Mỹ"),
    ("066490", "nebular hypothesis", "phrase", "/ˈnɛbjələr haɪˈpɒθəsɪs/", "giả thuyết tinh vân hình thành sao"),
    ("066491", "octal numeration system", "phrase", "/ˈɒktəl ˌnuːməˈreɪʃən ˈsɪstəm/", "hệ thống đếm cơ số tám bát phân"),
    ("066492", "plagal cadence", "phrase", "/ˈpleɪɡəl ˈkeɪdəns/", "kết âm plagal trong hòa âm nhạc"),
    ("066493", "prairie coneflower", "phrase", "/ˈprɛəri ˈkoʊnˌflaʊər/", "hoa cúc nón đồng cỏ Bắc Mỹ"),
    ("066494", "purple loosestrife", "phrase", "/ˈpɜːrpəl ˈluːsˌstraɪf/", "cây thiên khuê thảo hoa tím"),
    ("066495", "quercus coccinea", "phrase", "/ˈkwɜːrkəs kɒkˈsɪniə/", "cây sồi lá đỏ thẫm Bắc Mỹ"),
    ("066496", "rhus ovata", "phrase", "/ˈruːs oʊˈveɪtə/", "cây sơn mật lá trứng Bắc Mỹ"),
    ("066497", "sambre river", "phrase", "/ˈsɑːmbrə ˈrɪvər/", "sông Sambre chảy qua Pháp và Bỉ"),
    ("066498", "samuel pierpoint langley", "phrase", "/ˈsæmjʊəl ˈpɪərpɔɪnt ˈlæŋli/", "nhà thiên văn hàng không Langley"),
    ("066499", "seanad eireann", "phrase", "/ˈʃænəd ˈɛərən/", "Thượng viện Cộng hòa Ireland"),
    ("066500", "siouan language", "phrase", "/ˈsuːən ˈlæŋɡwɪdʒ/", "ngữ hệ bản địa Sioux Bắc Mỹ"),
    ("066501", "skin perceptiveness", "phrase", "/skɪn pərˈsɛptɪvnəs/", "khả năng cảm nhận xúc giác qua da"),
    ("066502", "svante august arrhenius", "phrase", "/ˈsvɑːntə ˈɔːɡəst əˈriːniəs/", "nhà hóa học Nobel Svante Arrhenius"),
]

with open("scratch/b34_r03_raw_p5.json") as f:
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

with open("scratch/b34_r03_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r03_p5.json OK")
