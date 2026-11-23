import json

items = [
    ("067403", "tobacco hornworm", "phrase", "/təˈbækoʊ ˈhɔːrnˌwɜːrm/", "sâu sừng xanh hại cây thuốc lá"),
    ("067404", "tomato hornworm", "phrase", "/təˈmeɪtoʊ ˈhɔːrnˌwɜːrm/", "sâu sừng xanh ăn lá cà chua"),
    ("067405", "tyto alba", "phrase", "/ˈtaɪtoʊ ˈælbə/", "chim cú lợn lưng xám mặt trắng"),
    ("067406", "vannevar bush", "phrase", "/væˈniːvər bʊʃ/", "kỹ sư tiên phong máy tính V. Bush"),
    ("067407", "abenakis", "noun", "/ˌæbəˈnɑːkiz/", "người bản địa Abenaki Bắc Mỹ"),
    ("067408", "agnosias", "noun", "/æɡˈnoʊʒəz/", "chứng mất khả năng nhận biết giác"),
    ("067409", "areopaguses", "noun", "/ˌæriˈɒpəɡəsɪz/", "đồi và hội đồng tối cao Athens cổ"),
    ("067410", "arrivedercis", "noun", "/əˌriːvəˈdɛərtʃiz/", "lời chào tạm biệt bằng tiếng Ý"),
    ("067411", "astrocytes", "noun", "/ˈæstrəˌsaɪts/", "tế bào thần kinh đệm hình sao"),
    ("067412", "avifaunas", "noun", "/ˌeɪvɪˈfɔːnəz/", "khu hệ chim sinh sống tại một vùng"),
    ("067413", "babblers", "noun", "/ˈbæblərz/", "người nói nhảm; chim họa mi khứu"),
    ("067414", "bandmasters", "noun", "/ˈbændˌmæstərz/", "nhạc trưởng chỉ huy ban nhạc kèn"),
    ("067415", "belshazzars", "noun", "/bɛlˈʃæzərz/", "vua Babylon cổ đại Belshazzar"),
    ("067416", "billfishes", "noun", "/ˈbɪlˌfɪʃɪz/", "cá mỏ kiếm gồm cá cờ và cá kiếm"),
    ("067417", "blabbermouths", "noun", "/ˈblæbərˌmaʊðz/", "kẻ lẻo mép hay buôn chuyện tiết lộ"),
    ("067418", "bluetongues", "noun", "/ˈbluːˌtʌŋz/", "bệnh lưỡi xanh ở cừu; thằn lằn Úc"),
    ("067419", "bowdlers", "noun", "/ˈbaʊdlərz/", "bác sĩ biên tập kiểm duyệt Bowdler"),
    ("067420", "boysenberries", "noun", "/ˈbɔɪzənˌbɛriz/", "quả mâm xôi lai đen đỏ boysenberry"),
    ("067421", "cabdrivers", "noun", "/ˈkæbˌdraɪvərz/", "tài xế lái xe taxi chở khách"),
    ("067422", "canoeists", "noun", "/kəˈnuːɪsts/", "vận động viên hoặc người chèo ca nô"),
    ("067423", "capets", "noun", "/kæˈpeɪz/", "vua triều đại Capet của nước Pháp"),
    ("067424", "ccrcs", "noun", "/ˌsiː siː ɑːr ˈsiːz/", "khu hưu trí chăm sóc liên tục CCRC"),
    ("067425", "centrosomes", "noun", "/ˈsɛntrəˌsoʊmz/", "trung thể tổ chức thoi phân bào"),
    ("067426", "chemiluminescences", "noun", "/ˌkɛmiˌluːmɪˈnɛsənsɪz/", "hiện tượng phát quang hóa học"),
    ("067427", "cherubinis", "noun", "/ˌkɛrʊˈbiːniz/", "nhà soạn nhạc Ý Luigi Cherubini"),
    ("067428", "chieftaincies", "noun", "/ˈtʃiːftənsiz/", "chức vị hoặc lãnh địa tù trưởng"),
    ("067429", "clangers", "noun", "/ˈklæŋərz/", "sai lầm ngớ ngẩn tai hại (lóng Anh)"),
    ("067430", "conodonts", "noun", "/ˈkɒnəˌdɒnts/", "sinh vật răng nón cổ sinh hóa thạch"),
    ("067431", "coracles", "noun", "/ˈkɒrəkəlz/", "thuyền thúng nan tròn bọc da cổ"),
    ("067432", "cowpeas", "noun", "/ˈkaʊˌpiːz/", "cây đậu đũa; đậu trắng mắt đen"),
    ("067433", "crinoids", "noun", "/ˈkraɪnɔɪdz/", "động vật huệ biển nhánh lông vũ"),
    ("067434", "crofters", "noun", "/ˈkrɒftərz/", "nông dân thuê tiểu điền ở Scotland"),
    ("067435", "deflators", "noun", "/dɪˈfleɪtərz/", "chỉ số giảm phát điều chỉnh giá"),
    ("067436", "deponents", "noun", "/dɪˈpoʊnənts/", "người làm chứng tuyên thệ khai báo"),
    ("067437", "dexedrines", "noun", "/ˈdɛksɪˌdriːnz/", "thuốc kích thần kinh Dexedrine"),
    ("067438", "dinesens", "noun", "/ˈdɪnəsənz/", "nữ nhà văn Đan Mạch Isak Dinesen"),
    ("067439", "dinoflagellates", "noun", "/ˌdaɪnoʊˈflædʒəˌleɪts/", "tảo giáp hai roi gây thủy triều đỏ"),
    ("067440", "dodomas", "noun", "/dəˈdoʊməz/", "thủ đô Dodoma của Tanzania"),
    ("067441", "dogsleds", "noun", "/ˈdɒɡˌslɛdz/", "xe trượt tuyết do đàn chó kéo"),
    ("067442", "doodlebugs", "noun", "/ˈduːdəlˌbʌɡz/", "ấu trùng kiến sư tử; bom bay V-1"),
    ("067443", "dysthymias", "noun", "/dɪsˈθaɪmiəz/", "rối loạn trầm cảm kéo dài nhẹ mạn"),
    ("067444", "eskers", "noun", "/ˈɛskərz/", "gờ cát sỏi ngoằn ngoèo do băng tan"),
    ("067445", "ethnoses", "noun", "/ˈɛθnoʊsɪz/", "tộc người chung văn hóa lịch sử"),
    ("067446", "fasceses", "noun", "/ˈfæsiːzɪz/", "bó gậy kèm rìu quyền lực La Mã cổ"),
    ("067447", "featherbedded", "verb", "/ˈfɛðərˌbɛdɪd/", "đã nuông chiều quá; giữ nhân sự dư"),
    ("067448", "featherbeded", "verb", "/ˈfɛðərˌbɛdɪd/", "đã nuông chiều quá mức (biến thể)"),
    ("067449", "featherbeding", "verb", "/ˈfɛðərˌbɛdɪŋ/", "đang nuông chiều quá mức (biến thể)"),
    ("067450", "featherbeds", "noun", "/ˈfɛðərˌbɛdz/", "nệm lông vũ êm ái; việc nhàn rỗi"),
    ("067451", "femorises", "noun", "/ˈfɛmərɪsɪz/", "xương đùi (biến thể số nhiều)"),
    ("067452", "footboards", "noun", "/ˈfʊtˌbɔːrdz/", "ván chân giường; bậc để chân xe"),
    ("067453", "footraces", "noun", "/ˈfʊtˌreɪsɪz/", "cuộc thi chạy bộ đua tốc độ"),
    ("067454", "fraxinuses", "noun", "/ˈfræksɪnəsɪz/", "cây tần bì thuộc chi Fraxinus"),
    ("067455", "gallinas", "noun", "/ɡəˈliːnəz/", "gà rừng lông đỏ thuộc chi Gallus"),
    ("067456", "goldmarks", "noun", "/ˈɡoʊldˌmɑːrks/", "nhà phát minh; nhạc sĩ Goldmark"),
    ("067457", "gorgets", "noun", "/ˈɡɔːrdʒɪts/", "tấm giáp bảo vệ cổ; vòng cổ áo"),
    ("067458", "hematopoieses", "noun", "/hɪˌmætoʊpɔɪˈiːsiːz/", "quá trình sinh tạo các tế bào máu"),
    ("067459", "heterosexisms", "noun", "/ˌhɛtəroʊˈsɛksɪzəmz/", "định kiến đề cao dị tính luyến ái"),
    ("067460", "highwaters", "noun", "/ˈhaɪˌwɔːtərz/", "mực nước triều cường cao nhất"),
    ("067461", "hoaxers", "noun", "/ˈhoʊksərz/", "kẻ bày trò lừa bịp tung tin giả"),
    ("067462", "homeopaths", "noun", "/ˈhoʊmiəˌpæθs/", "thầy thuốc vi lượng đồng căn"),
    ("067463", "hoopoes", "noun", "/ˈhuːpuːz/", "chim đầu rìu mào lông xòe đẹp"),
    ("067464", "hornpipes", "noun", "/ˈhɔːrnˌpaɪps/", "điệu nhảy hornpipe; kèn sừng"),
    ("067465", "hypervelocities", "noun", "/ˌhaɪpərvəˈlɒsɪtiz/", "siêu vận tốc cực cao ngoài vũ trụ"),
    ("067466", "internodes", "noun", "/ˈɪntərˌnoʊdz/", "đoạn lóng thân cây giữa hai đốt"),
    ("067467", "kambas", "noun", "/ˈkɑːmbəz/", "dân tộc và ngôn ngữ Kamba ở Kenya"),
    ("067468", "landsides", "noun", "/ˈlændˌsaɪdz/", "má trượt kim loại ở lưỡi cày"),
    ("067469", "lechers", "noun", "/ˈlɛtʃərz/", "kẻ háo sắc dâm ô trác táng"),
    ("067470", "lepuses", "noun", "/ˈliːpəsɪz/", "chòm sao Thiên Thố; chi thỏ rừng"),
    ("067471", "lgvs", "noun", "/ˌɛl dʒiː ˈviːz/", "bệnh hột xoài u hạt bạch huyết bẹn"),
    ("067472", "liberalised", "verb", "/ˈlɪbərəˌlaɪzd/", "đã tự do hóa nới lỏng quy định"),
    ("067473", "liberalises", "verb", "/ˈlɪbərəˌlaɪzɪz/", "tự do hóa kinh tế hoặc chính trị"),
    ("067474", "liberalising", "verb", "/ˈlɪbərəˌlaɪzɪŋ/", "đang tự do hóa nới lỏng kiểm soát"),
    ("067475", "lunettes", "noun", "/luːˈnɛts/", "công sự bán nguyệt; cửa sổ vòm"),
    ("067476", "lycians", "noun", "/ˈlɪʃənz/", "người và tiếng Lycia cổ Tiểu Á"),
    ("067477", "magueys", "noun", "/məˈɡeɪz/", "cây thùa Mexico lấy sợi và rượu"),
    ("067478", "majorettes", "noun", "/ˌmeɪdʒəˈrɛts/", "nữ cổ động viên xoay gậy diễu hành"),
    ("067479", "mammalogies", "noun", "/məˈmɒlədʒiz/", "ngành thú học nghiên cứu động vật"),
    ("067480", "mandragoras", "noun", "/mænˈdræɡərəz/", "cây nhân sâm ma cà độc dược cổ đại"),
    ("067481", "mantillas", "noun", "/mænˈtɪləz/", "khăn voan ren trùm đầu Tây Ban Nha"),
    ("067482", "meitners", "noun", "/ˈmaɪtnərz/", "nhà vật lý hạt nhân Lise Meitner"),
    ("067483", "melenas", "noun", "/məˈliːnəz/", "tình trạng đi ngoài phân đen do máu"),
    ("067484", "mignonettes", "noun", "/ˌmɪnjəˈnɛts/", "hoa mộc tê thơm reseda"),
    ("067485", "milages", "noun", "/ˈmaɪlɪdʒɪz/", "tổng quãng đường tính bằng dặm"),
    ("067486", "moldered", "verb", "/ˈmoʊldərd/", "đã mục nát phân rã dần theo năm"),
    ("067487", "moldering", "verb", "/ˈmoʊldərɪŋ/", "đang mục rữa phân hủy thành bụi"),
    ("067488", "molders", "verb", "/ˈmoʊldərz/", "mục nát dần; rã thành cát bụi"),
    ("067489", "morganites", "noun", "/ˈmɔːrɡəˌnaɪts/", "đá quý beryl màu hồng morganit"),
    ("067490", "moruses", "noun", "/ˈmɔːrəsɪz/", "cây dâu tằm thuộc chi Morus"),
    ("067491", "nandrolones", "noun", "/ˈnændrəˌloʊnz/", "hoóc-môn tăng cơ steroid nandrolon"),
    ("067492", "nightspots", "noun", "/ˈnaɪtˌspɒts/", "hộp đêm quán bar giải trí ban đêm"),
    ("067493", "omiyas", "noun", "/oʊˈmiːəz/", "thành phố Omiya ở Saitama Nhật Bản"),
    ("067494", "orisons", "noun", "/ˈɒrɪzənz/", "lời cầu nguyện khấn vái (văn cổ)"),
    ("067495", "panhandlers", "noun", "/ˈpænˌhændlərz/", "người ăn xin ngoài phố (Mỹ)"),
    ("067496", "papaws", "noun", "/pəˈpɔːz/", "cây quả đu đủ Bắc Mỹ; cây đu đủ"),
    ("067497", "pasangs", "noun", "/pəˈsɑːŋz/", "dê núi hoang dã Ba Tư pasang"),
    ("067498", "patencies", "noun", "/ˈpeɪtənsiz/", "tính thông thoáng không tắc nghẽn"),
    ("067499", "pinoles", "noun", "/pɪˈnoʊleɪz/", "bột ngô rang ngọt truyền thống"),
    ("067500", "pleaders", "noun", "/ˈpliːdərz/", "luật sư biện hộ trước tòa án"),
    ("067501", "plumerias", "noun", "/pluːˈmɪriəz/", "cây hoa đại sứ thơm chi Plumeria"),
    ("067502", "polymerisations", "noun", "/ˌpɒlɪməraɪˈzeɪʃənz/", "phản ứng trùng hợp tạo polyme"),
]

with open("scratch/b34_r05_raw_p5.json") as f:
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

with open("scratch/b34_r05_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r05_p5.json OK")
