import json

items = [
    ("067103", "highchairs", "noun", "/ˈhaɪˌtʃɛərz/", "ghế cao ăn dặm cho trẻ nhỏ"),
    ("067104", "hightailed", "verb", "/ˈhaɪˌteɪld/", "đã co giò bỏ chạy thục mạng"),
    ("067105", "hightailing", "verb", "/ˈhaɪˌteɪlɪŋ/", "đang vắt chân lên cổ bỏ chạy"),
    ("067106", "hightails", "verb", "/ˈhaɪˌteɪlz/", "vắt chân lên cổ bỏ chạy thật nhanh"),
    ("067107", "hipparchuses", "noun", "/hɪˈpɑːrkəsɪz/", "nhà thiên văn cổ đại Hipparchus"),
    ("067108", "hoary alyssum", "phrase", "/ˈhɔːri əˈlɪsəm/", "cây cải hoa trắng Bắc Mỹ"),
    ("067109", "ilex decidua", "phrase", "/ˈaɪlɛks dɪˈsɪdʒuə/", "cây nhựa ruồi rụng lá quả đỏ"),
    ("067110", "inclosures", "noun", "/ɪnˈkloʊʒərz/", "tài liệu đính kèm; khu đất rào kín"),
    ("067111", "inessentials", "noun", "/ˌɪnɪˈsɛnʃəlz/", "những thứ phụ không thiết yếu"),
    ("067112", "ipomoea purpurea", "phrase", "/ˌɪpəˈmiːə pɜːrˈpjʊriə/", "cây hoa bìm bìm tím leo hàng rào"),
    ("067113", "ischiums", "noun", "/ˈɪskiəmz/", "xương ngồi ở phần dưới khung chậu"),
    ("067114", "ixodeses", "noun", "/ɪkˈsoʊdiːzɪz/", "chi ve cứng hút máu Ixodes"),
    ("067115", "jawless vertebrate", "phrase", "/ˈdʒɔːləs ˈvɜːrtɪbrət/", "động vật có xương sống không hàm"),
    ("067116", "kalugas", "noun", "/kəˈluːɡəz/", "cá tầm kaluga; thành phố Kaluga"),
    ("067117", "kaons", "noun", "/ˈkeɪɒnz/", "hạt hạ nguyên tử meson K (kaon)"),
    ("067118", "kauri copal", "phrase", "/ˈkaʊri ˈkoʊpəl/", "nhựa thông cổ kauri hóa thạch"),
    ("067119", "keratosis nigricans", "phrase", "/ˌkɛrəˈtoʊsɪs ˈnaɪɡrɪkænz/", "bệnh dày sừng gai đen trên da"),
    ("067120", "lacewing fly", "phrase", "/ˈleɪsˌwɪŋ flaɪ/", "côn trùng cánh màng mắt lưới"),
    ("067121", "laiuses", "noun", "/ˈleɪəsɪz/", "Vua Laius thành Thebes thần thoại"),
    ("067122", "lawbreakers", "noun", "/ˈlɔːˌbreɪkərz/", "kẻ vi phạm pháp luật; tội phạm"),
    ("067123", "leatherwoods", "noun", "/ˈlɛðərˌwʊdz/", "cây bụi vỏ dai dẻo như da thuộc"),
    ("067124", "lime disease spirochete", "phrase", "/laɪm dɪˈziːz ˈspaɪrəˌkiːt/", "xoắn khuẩn gây bệnh Lyme do ve"),
    ("067125", "loquat tree", "phrase", "/ˈloʊkwɒt triː/", "cây nhót tây; cây tỳ bà quả vàng"),
    ("067126", "lubumbashis", "noun", "/ˌluːbʊmˈbɑːʃiz/", "thành phố Lubumbashi ở Congo"),
    ("067127", "mahouts", "noun", "/məˈhaʊts/", "người quản tượng chăm và cưỡi voi"),
    ("067128", "mahrattas", "noun", "/məˈrɑːtəz/", "người dân tộc Maratha ở Ấn Độ"),
    ("067129", "maidenhair berry", "phrase", "/ˈmeɪdənˌhɛər ˈbɛri/", "cây tuyết quả bò hương bạc hà"),
    ("067130", "maidenhair tree", "phrase", "/ˈmeɪdənˌhɛər triː/", "cây bạch quả cổ đại lá hình quạt"),
    ("067131", "manglers", "noun", "/ˈmæŋɡlərz/", "người làm hỏng bóp méo; máy cán"),
    ("067132", "manicheans", "noun", "/ˌmænɪˈkiːənz/", "tín đồ đạo Mani nhị nguyên cổ đại"),
    ("067133", "marteses", "noun", "/ˈmɑːrtiːzɪz/", "chồn thông thuộc chi Martes"),
    ("067134", "maskers", "noun", "/ˈmæskərz/", "người đeo mặt nạ dự tiệc hóa trang"),
    ("067135", "matzoh ball", "phrase", "/ˈmɑːtsə bɔːl/", "viên bánh bột không men thả súp"),
    ("067136", "matzoh meal", "phrase", "/ˈmɑːtsə miːl/", "bột bánh mì không men nghiền mịn"),
    ("067137", "mcguffins", "noun", "/məˈɡʌfɪnz/", "chi tiết dẫn dắt cốt truyện phim"),
    ("067138", "melpomenes", "noun", "/mɛlˈpɒməniːz/", "nữ thần bi kịch Melpomene Hy Lạp"),
    ("067139", "micelles", "noun", "/maɪˈsɛlz/", "hạt mixen keo phân tử chất hoạt"),
    ("067140", "microtuses", "noun", "/maɪˈkroʊtəsɪz/", "chuột đồng thuộc chi Microtus"),
    ("067141", "mottles", "noun", "/ˈmɒtəlz/", "vết lốm đốm loang lổ trên bề mặt"),
    ("067142", "multiflora rose", "phrase", "/ˌmʌltiˈflɔːrə roʊz/", "cây tầm xuân nhiều hoa bụi leo"),
    ("067143", "mwanzas", "noun", "/əmˈwɑːnzəz/", "thành phố cảng Mwanza ở Tanzania"),
    ("067144", "nattas", "noun", "/ˈnɑːtəz/", "nhà hóa học Nobel Giulio Natta"),
    ("067145", "neuroleptics", "noun", "/ˌnjʊərəˈlɛptɪks/", "thuốc an thần kinh trị loạn thần"),
    ("067146", "ninons", "noun", "/ˈniːnɒnz/", "vải lụa mỏng xuyên thấu ninon"),
    ("067147", "nolle pros", "phrase", "/ˌnɒli ˈprɒs/", "lệnh đình chỉ rút cáo trạng (Mỹ)"),
    ("067148", "noncombatants", "noun", "/nɒnˈkɒmbətənts/", "người không trực tiếp chiến đấu"),
    ("067149", "northmans", "noun", "/ˈnɔːrθmənz/", "người Viking vùng Bắc Âu cổ đại"),
    ("067150", "ojibways", "noun", "/oʊˈdʒɪbweɪz/", "bộ tộc bản địa Ojibway Bắc Mỹ"),
    ("067151", "order araneae", "phrase", "/ˈɔːrdər əˈreɪniː/", "bộ Nhện tám chân trong lớp Hình"),
    ("067152", "order collembola", "phrase", "/ˈɔːrdər kɒˈlɛmbələ/", "bộ Bọ nhảy đuôi bật sống trong đất"),
    ("067153", "overlordships", "noun", "/ˈoʊvərˌlɔːrdʃɪps/", "quyền bá chủ của lãnh chúa tối cao"),
    ("067154", "pantheists", "noun", "/ˈpænθiɪsts/", "người theo thuyết phiếm thần"),
    ("067155", "parainfluenza virus", "phrase", "/ˌpærəɪnfluˈɛnzə ˈvaɪrəs/", "vi rút á cúm gây viêm đường hô hấp"),
    ("067156", "paresthesias", "noun", "/ˌpærɪsˈθiːʒəz/", "cảm giác tê rần châm chích ngoài da"),
    ("067157", "paroxysms", "noun", "/ˈpærəkˌsɪzəmz/", "cơn bùng phát dữ dội bất ngờ"),
    ("067158", "patricides", "noun", "/ˈpætrɪˌsaɪdz/", "tội giết cha; kẻ sát hại cha ruột"),
    ("067159", "pelages", "noun", "/ˈpɛlɪdʒɪz/", "bộ lông bao phủ cơ thể thú"),
    ("067160", "pellicles", "noun", "/ˈpɛlɪkəlz/", "lớp màng mỏng sinh học bảo vệ"),
    ("067161", "periosteums", "noun", "/ˌpɛriˈɒstiəmz/", "màng xương bao bọc bên ngoài xương"),
    ("067162", "peromyscuses", "noun", "/ˌpɛrəˈmɪskəsɪz/", "chuột hươu rừng Bắc Mỹ Peromyscus"),
    ("067163", "phthalic acid", "phrase", "/ˈθælɪk ˈæsɪd/", "axit phtalic nguyên liệu nhựa sơn"),
    ("067164", "pinchbecks", "noun", "/ˈpɪntʃˌbɛks/", "hợp kim giả vàng; đồ trang sức giả"),
    ("067165", "piriform lobe", "phrase", "/ˈpɪrɪfɔːrm loʊb/", "thùy não khứu giác hình quả lê"),
    ("067166", "polycythemias", "noun", "/ˌpɒlɪsaɪˈθiːmiəz/", "bệnh tăng sinh đa hồng cầu máu"),
    ("067167", "procaine hydrochloride", "phrase", "/ˈproʊkeɪn ˌhaɪdrəˈklɔːraɪd/", "thuốc gây tê cục bộ procain"),
    ("067168", "pufferies", "noun", "/ˈpʌfəriz/", "lời quảng cáo thổi phồng quá mức"),
    ("067169", "purple osier", "phrase", "/ˈpɜːrpəl ˈoʊʒər/", "cây liễu tía thân mảnh đan giỏ"),
    ("067170", "pyx chest", "phrase", "/pɪks tʃɛst/", "hòm chứa tiền xu kiểm định Hoàng"),
    ("067171", "quercus texana", "phrase", "/ˈkwɜːrkəs tɛkˈseɪnə/", "cây sồi đỏ Nuttall vùng Texas"),
    ("067172", "recantations", "noun", "/ˌriːkænˈteɪʃənz/", "sự rút lại tuyên bố niềm tin cũ"),
    ("067173", "reccos", "noun", "/ˈrɛkoʊz/", "lính trinh sát quân sự (tiếng lóng)"),
    ("067174", "red osier", "phrase", "/rɛd ˈoʊʒər/", "cây giác mộc cành đỏ Bắc Mỹ"),
    ("067175", "redstarts", "noun", "/ˈrɛdˌstɑːrts/", "chim đuôi đỏ họ Đớp ruồi"),
    ("067176", "rhinoviruses", "noun", "/ˌraɪnoʊˈvaɪrəsɪz/", "vi rút rhino gây cảm lạnh thường"),
    ("067177", "rosa multiflora", "phrase", "/ˈroʊzə ˌmʌltiˈflɔːrə/", "cây hoa hồng dại tầm xuân nhiều hoa"),
    ("067178", "sabals", "noun", "/ˈseɪbəlz/", "cây cọ lá quạt thuộc chi Sabal"),
    ("067179", "saccades", "noun", "/səˈkɑːdz/", "chuyển động đảo mắt nhanh liên tiếp"),
    ("067180", "saccharums", "noun", "/ˈsækərəmz/", "cây mía thuộc chi Saccharum"),
    ("067181", "salian frank", "phrase", "/ˈseɪliən fræŋk/", "người bộ tộc Frank Salia cổ đại"),
    ("067182", "sambucus canadensis", "phrase", "/sæmˈbjuːkəs ˌkænəˈdɛnsɪs/", "cây cơm cháy quả đen Bắc Mỹ"),
    ("067183", "schistosomas", "noun", "/ˌʃɪstəˈsoʊməz/", "sán máng ký sinh trong mạch máu"),
    ("067184", "schoolbags", "noun", "/ˈskuːlˌbæɡz/", "cặp sách học sinh; ba lô đi học"),
    ("067185", "scuts", "noun", "/skʌts/", "đuôi ngắn thỏ hươu; kẻ tầm thường"),
    ("067186", "serialisations", "noun", "/ˌsɪriəlaɪˈzeɪʃənz/", "sự tuần tự hóa; đăng báo nhiều kỳ"),
    ("067187", "shammy leather", "phrase", "/ˈʃæmi ˈlɛðər/", "da thuộc sơn dương mềm lau chùi"),
    ("067188", "silvicultures", "noun", "/ˈsɪlvɪˌkʌltʃərz/", "kỹ thuật trồng và chăm sóc rừng"),
    ("067189", "siraches", "noun", "/ˈsaɪræks/", "sách Huấn Ca trong Kinh Thánh"),
    ("067190", "southern maidenhair", "phrase", "/ˈsʌðərn ˈmeɪdənˌhɛər/", "dương xỉ tóc thần nữ phương nam"),
    ("067191", "stepparents", "noun", "/ˈstɛpˌpɛərənts/", "cha dượng; mẹ kế"),
    ("067192", "stickball game", "phrase", "/ˈstɪkˌbɔːl ɡeɪm/", "trò bóng chày đường phố dùng gậy"),
    ("067193", "stonecutters", "noun", "/ˈstoʊnˌkʌtərz/", "thợ đẽo đá; thợ chạm khắc đá"),
    ("067194", "strakes", "noun", "/streɪks/", "dải ván ghép dọc thân tàu thủy"),
    ("067195", "strumas", "noun", "/ˈstruːməz/", "bệnh bướu cổ sưng tuyến giáp"),
    ("067196", "styloid process", "phrase", "/ˈstaɪlɔɪd ˈprɒsɛs/", "mỏm trâm nhọn trên xương thái dương"),
    ("067197", "sudafeds", "noun", "/ˈsuːdəˌfɛdz/", "thuốc giảm nghẹt mũi Sudafed"),
    ("067198", "synaesthesias", "noun", "/ˌsɪnɪsˈθiːʒəz/", "hiện tượng giao thoa đa giác quan"),
    ("067199", "synchronisings", "noun", "/ˈsɪŋkrəˌnaɪzɪŋz/", "sự đồng bộ hóa thời gian nhịp điệu"),
    ("067200", "szilards", "noun", "/ˈzɪlɑːrdz/", "nhà vật lý hạt nhân Leo Szilard"),
    ("067201", "tallapoosas", "noun", "/ˌtæləˈpuːsəz/", "sông Tallapoosa ở miền nam Mỹ"),
    ("067202", "tambours", "noun", "/ˈtæmbʊərz/", "khung thêu tròn; trống mặt tròn"),
]

with open("scratch/b34_r05_raw_p2.json") as f:
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

with open("scratch/b34_r05_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r05_p2.json OK")
