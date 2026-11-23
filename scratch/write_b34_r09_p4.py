import json

items = [
    ("069303", "hyniums", "noun", "/ˈhɪniəmz/", "tầng sinh bào tử nấm (biến thể)"),
    ("069304", "icepicks", "noun", "/ˈaɪsˌpɪks/", "dùi nhọn đục tách nước đá"),
    ("069305", "ileuses", "noun", "/ˈɪliəsɪz/", "chứng tắc liệt ruột ngừng nhu động"),
    ("069306", "inlas", "noun", "/ˈɪnləz/", "Quân đội Giải phóng INLA Ireland"),
    ("069307", "irishwomans", "noun", "/ˈaɪrɪʃˌwʊmənz/", "phụ nữ người Ireland (biến thể)"),
    ("069308", "isometries", "noun", "/aɪˈsɒmɪtriz/", "phép biến hình đẳng cự giữ khoảng"),
    ("069309", "isothiocyanates", "noun", "/ˌaɪsoʊˌθaɪoʊˈsaɪəneɪts/", "hợp chất lưu huỳnh isothiocyanat"),
    ("069310", "kabalas", "noun", "/kəˈbɑːləz/", "truyền thống huyền bí Do Thái"),
    ("069311", "kludges", "noun", "/ˈklʌdʒɪz/", "giải pháp chắp vá tạm bợ vụng về"),
    ("069312", "latonas", "noun", "/ləˈtoʊnəz/", "nữ thần Latona mẹ của Apollo"),
    ("069313", "laurentiuses", "noun", "/lɔːˈrɛnʃəsɪz/", "Thánh tử đạo Lawrence thành Rome"),
    ("069314", "lauruses", "noun", "/ˈlɔːrəsɪz/", "cây nguyệt quế thuộc chi Laurus"),
    ("069315", "leadbellies", "noun", "/ˈlɛdˌbɛliz/", "nhạc sĩ nhạc blues Mỹ Lead Belly"),
    ("069316", "leptospiras", "noun", "/ˌlɛptəˈspaɪrəz/", "xoắn khuẩn gây bệnh vàng da chuột"),
    ("069317", "lugandas", "noun", "/luːˈɡændəz/", "tiếng Luganda phổ biến ở Uganda"),
    ("069318", "malvasias", "noun", "/mɑːlˈvɑːziəz/", "giống nho và rượu vang ngọt Ý"),
    ("069319", "marabouts", "noun", "/ˈmærəˌbuːz/", "cò già đầu trọc châu Phi; ẩn sĩ"),
    ("069320", "mesenteries", "noun", "/ˈmɛzənˌtɛriz/", "mạc treo ruột giữ ruột vào thành"),
    ("069321", "millilitres", "noun", "/ˈmɪlɪˌliːtərz/", "đơn vị thể tích mililít (Anh)"),
    ("069322", "miltiadeses", "noun", "/mɪlˈtaɪədiːzɪz/", "danh tướng Athens cổ Miltiades"),
    ("069323", "miwoks", "noun", "/ˈmiːwɒks/", "người bản địa Miwok California"),
    ("069324", "monkshoods", "noun", "/ˈmʌŋksˌhʊdz/", "cây ô đầu hoa tím mũ thầy tu độc"),
    ("069325", "muscadines", "noun", "/ˈmʌskəˌdaɪnz/", "nho vỏ dày bản địa đông nam Mỹ"),
    ("069326", "noncitizens", "noun", "/ˌnɒnˈsɪtɪzənz/", "người chưa có quyền công dân"),
    ("069327", "nymphaeas", "noun", "/nɪmˈfiːəz/", "hoa súng nước thuộc chi Nymphaea"),
    ("069328", "octoberfests", "noun", "/ɒkˈtoʊbərˌfɛsts/", "lễ hội bia Oktoberfest của Đức"),
    ("069329", "otorhinolaryngologies", "noun", "/ˌoʊtoʊˌraɪnoʊˌlærɪŋˈɡɒlədʒiz/", "chuyên khoa tai mũi họng"),
    ("069330", "palmier", "adj", "/ˈpɑːlmiər/", "thịnh vượng phát đạt rực rỡ hơn"),
    ("069331", "palmiest", "adj", "/ˈpɑːlmiɪst/", "thịnh vượng phát đạt rực rỡ nhất"),
    ("069332", "particularisms", "noun", "/pərˈtɪkjələrˌɪzəmz/", "chủ nghĩa đặc thù biệt phái cục bộ"),
    ("069333", "passkeys", "noun", "/ˈpæsˌkiːz/", "chìa khóa vạn năng mở nhiều cửa"),
    ("069334", "pelagianisms", "noun", "/pəˈleɪdʒiənˌɪzəmz/", "học thuyết thần học Pelagius cổ"),
    ("069335", "perishers", "noun", "/ˈpɛrɪʃərz/", "gã đáng ghét; kẻ phiền toái (Anh)"),
    ("069336", "possets", "noun", "/ˈpɒsɪts/", "đồ uống sữa nóng pha rượu gia vị"),
    ("069337", "pothoses", "noun", "/ˈpoʊθɒsɪz/", "cây trầu bà leo thuộc chi Pothos"),
    ("069338", "pseudotsugas", "noun", "/ˌsuːdoʊˈtsuːɡəz/", "cây linh sam Douglas Pseudotsuga"),
    ("069339", "reseeded", "verb", "/riːˈsiːdɪd/", "đã gieo hạt trồng lại; sắp hạt lại"),
    ("069340", "reseeding", "verb", "/riːˈsiːdɪŋ/", "đang gieo hạt trồng dặm lại cỏ"),
    ("069341", "reseeds", "verb", "/riːˈsiːdz/", "gieo hạt giống lại; xếp hạt đấu"),
    ("069342", "sambuci", "noun", "/sæmˈbjuːsaɪ/", "cây cơm cháy thuộc chi Sambucus"),
    ("069343", "sanderlings", "noun", "/ˈsændərlɪŋz/", "chim choắt cát nhỏ chạy ven sóng"),
    ("069344", "sardonyxes", "noun", "/sɑːrˈdɒnɪksɪz/", "đá mã não vân dải nâu trắng"),
    ("069345", "scatterbrains", "noun", "/ˈskætərˌbreɪnz/", "người đãng trí hay quên lơ đãng"),
    ("069346", "schwarzwalds", "noun", "/ˈʃvɑːrtsvɑːldz/", "vùng Rừng Đen Schwarzwald của Đức"),
    ("069347", "sciuruses", "noun", "/saɪˈjʊərəsɪz/", "sóc cây đuôi xù thuộc chi Sciurus"),
    ("069348", "scried", "verb", "/skraɪd/", "đã nhìn cầu pha lê tiên tri bói"),
    ("069349", "scries", "verb", "/skraɪz/", "soi cầu pha lê mặt nước đoán vận"),
    ("069350", "scrying", "verb", "/ˈskraɪɪŋ/", "đang nhìn cầu pha lê xem bói"),
    ("069351", "shaytans", "noun", "/ʃeɪˈtɑːnz/", "ác quỷ sa tăng (trong tiếng Ả Rập)"),
    ("069352", "shebeens", "noun", "/ʃɪˈbiːnz/", "quán rượu chui không phép (Ireland)"),
    ("069353", "shoshonis", "noun", "/ʃoʊˈʃoʊniz/", "người bản địa Shoshone miền Tây"),
    ("069354", "silicides", "noun", "/ˈsɪlɪˌsaɪdz/", "hợp chất silicua kim loại bán dẫn"),
    ("069355", "sirises", "noun", "/ˈsɪrɪsɪz/", "cây bồ kết tây; cây hợp hoan gỗ"),
    ("069356", "sorbuses", "noun", "/ˈsɔːrbəsɪz/", "cây thanh lương trà chi Sorbus"),
    ("069357", "spawners", "noun", "/ˈspɔːnərz/", "cá đang đẻ trứng; bộ sinh sản vật"),
    ("069358", "spodopteras", "noun", "/spoʊˈdɒptərəz/", "ngài sâu keo hại mùa Spodoptera"),
    ("069359", "syndicators", "noun", "/ˈsɪndɪˌkeɪtərz/", "nhà phân phối tin tức; người hùn"),
    ("069360", "toreros", "noun", "/tɔːˈrɛəroʊz/", "đấu sĩ đấu bò tót Tây Ban Nha"),
    ("069361", "tramcars", "noun", "/ˈtræmˌkɑːrz/", "toa xe điện chạy ray trên phố"),
    ("069362", "traumatologies", "noun", "/ˌtrɔːməˈtɒlədʒiz/", "ngành chấn thương chỉnh hình y học"),
    ("069363", "trematodes", "noun", "/ˈtrɛməˌtoʊdz/", "sán lá ký sinh gây bệnh ở người"),
    ("069364", "varans", "noun", "/ˈvɛərənz/", "kỳ đà lớn thuộc chi Varanus"),
    ("069365", "whins", "noun", "/wɪnz/", "cây kim tước gai hoa vàng; đá cứng"),
    ("069366", "whitecaps", "noun", "/ˈwaɪtˌkæps/", "đầu ngọn sóng bạc bọt trắng xóa"),
    ("069367", "zeppos", "noun", "/ˈzɛpoʊz/", "diễn viên hài Mỹ Zeppo Marx"),
    ("069368", "albuminurias", "noun", "/ælˌbjuːmɪˈnjʊəriəz/", "chứng đạm niệu xuất hiện albumin"),
    ("069369", "alcyones", "noun", "/ælˈsaɪəniːz/", "sao Alcyone; nữ thần Alcyone"),
    ("069370", "animalities", "noun", "/ˌænɪˈmælɪtiz/", "bản năng thú tính tự nhiên động vật"),
    ("069371", "annuitants", "noun", "/əˈnjuːɪtənts/", "người hưởng trợ cấp hưu trí niên"),
    ("069372", "ashcans", "noun", "/ˈæʃˌkænz/", "thùng sắt đựng tro rác; bom chìm"),
    ("069373", "ataraxias", "noun", "/ˌætəˈræksiəz/", "tâm thái tĩnh tại thanh thản triết"),
    ("069374", "augmentins", "noun", "/ɔːɡˈmɛntɪnz/", "thuốc kháng sinh phổ rộng Augmentin"),
    ("069375", "autocues", "noun", "/ˈɔːtoʊˌkjuːz/", "máy nhắc chữ truyền hình autocue"),
    ("069376", "bacitracins", "noun", "/ˌbæsɪˈtreɪsɪnz/", "thuốc mỡ kháng sinh bacitracin"),
    ("069377", "basseterres", "noun", "/bæsˈtɛərz/", "thủ đô Basseterre Saint Kitts"),
    ("069378", "bluestockings", "noun", "/ˈbluːˌstɒkɪŋz/", "nữ trí thức học giả thời xưa"),
    ("069379", "braincases", "noun", "/ˈbreɪnˌkeɪsɪz/", "hộp sọ bảo vệ bộ não bộ"),
    ("069380", "bunchier", "adj", "/ˈbʌntʃiər/", "mọc tụm thành chùm xum xuê hơn"),
    ("069381", "bunchiest", "adj", "/ˈbʌntʃiɪst/", "mọc tụm thành chùm xum xuê nhất"),
    ("069382", "busbars", "noun", "/ˈbʌsˌbɑːrz/", "thanh cái dẫn điện đồng tủ điện"),
    ("069383", "buspars", "noun", "/ˈbjuːspɑːrz/", "thuốc an thần giảm lo âu BuSpar"),
    ("069384", "calpes", "noun", "/ˈkælpiːz/", "núi đá Gibraltar Calpe cổ đại"),
    ("069385", "capitula", "noun", "/kəˈpɪtjʊlə/", "chỏm cầu đầu xương; cụm hoa đầu"),
    ("069386", "capitulums", "noun", "/kəˈpɪtjʊləmz/", "cụm hoa đầu họ Cúc; chỏm xương"),
    ("069387", "carboys", "noun", "/ˈkɑːrˌbɔɪz/", "bình thủy tinh lớn bọc giỏ đựng"),
    ("069388", "catkins", "noun", "/ˈkætˌkɪnz/", "cụm hoa đuôi sóc rủ xuống"),
    ("069389", "caucasias", "noun", "/kɔːˈkeɪʒəz/", "vùng Kavkaz giữa Biển Đen và Caspi"),
    ("069390", "cephalexins", "noun", "/ˌsɛfəˈlɛksɪnz/", "thuốc kháng sinh cefalexin"),
    ("069391", "chilubas", "noun", "/tʃɪˈluːbəz/", "tiếng Chiluba ở CHDC Congo"),
    ("069392", "cirios", "noun", "/ˈsɪrioʊz/", "cây sa mạc cao thon cirio Mexico"),
    ("069393", "cistuses", "noun", "/ˈsɪstəsɪz/", "cây hoa hồng đá thuộc chi Cistus"),
    ("069394", "construals", "noun", "/kənˈstruːəlz/", "cách diễn giải hiểu nghĩa câu chữ"),
    ("069395", "customhouses", "noun", "/ˈkʌstəmˌhaʊzɪz/", "cơ quan trụ sở làm thủ tục hải quan"),
    ("069396", "cymae", "noun", "/ˈsaɪmiː/", "đường gờ phào chỉ uốn lượn chữ S"),
    ("069397", "cymas", "noun", "/ˈsaɪməz/", "phào chỉ kiến trúc lượn sóng chữ S"),
    ("069398", "cynodons", "noun", "/ˈsɪnədɒnz/", "cỏ gà mọc thảm thuộc chi Cynodon"),
    ("069399", "cyprinuses", "noun", "/sɪˈpraɪnəsɪz/", "cá chép thuộc chi Cyprinus"),
    ("069400", "daylilies", "noun", "/ˈdeɪˌlɪliz/", "hoa hiên hoa kim châm nở một ngày"),
    ("069401", "deaminations", "noun", "/ˌdiːæmɪˈneɪʃənz/", "phản ứng tách loại nhóm amin hóa"),
    ("069402", "demineralizations", "noun", "/diːˌmɪnərəlaɪˈzeɪʃənz/", "sự khử khoáng mất canxi răng xương"),
]

with open("scratch/b34_r09_raw_p4.json") as f:
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

with open("scratch/b34_r09_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r09_p4.json OK")
