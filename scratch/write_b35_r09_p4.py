import json

items = [
    ("074303", "haleru", "noun", "/hɑːˈlɛruː/", "đơn vị tiền xu haléř (Séc-Slovakia)"),
    ("074304", "hopeis", "noun", "/hoʊˈpeɪz/", "tỉnh Hà Bắc (Trung Quốc)"),
    ("074305", "hyaloids", "noun", "/ˈhaɪəˌlɔɪdz/", "màng pha lê trong suốt ở mắt"),
    ("074306", "hypanthia", "noun", "/haɪˈpænθiə/", "đế hoa hình chén (thực vật học)"),
    ("074307", "hypanthiums", "noun", "/haɪˈpænθiəmz/", "đế hoa hình chén (thực vật học)"),
    ("074308", "iberts", "noun", "/iːˈbɛərz/", "nhà soạn nhạc Pháp Jacques Ibert"),
    ("074309", "indocins", "noun", "/ˈɪndəsɪnz/", "thuốc kháng viêm giảm đau Indocin"),
    ("074310", "isopteras", "noun", "/aɪˈsɒptərəz/", "bộ Cánh đều (loài mối)"),
    ("074311", "kahoolawes", "noun", "/kəˌhoʊəˈlɑːweɪz/", "đảo Kahoolawe ở bang Hawaii (Mỹ)"),
    ("074312", "keratinizations", "noun", "/ˌkɛrətɪnaɪˈzeɪʃənz/", "quá trình sừng hóa tế bào biểu bì"),
    ("074313", "kibes", "noun", "/kaɪbz/", "vết loét nứt nẻ do cóng ở gót chân"),
    ("074314", "latinists", "noun", "/ˈlætɪnɪsts/", "học giả chuyên gia tiếng Latinh"),
    ("074315", "latitudinarians", "noun", "/ˌlætɪtjuːdɪˈnɛəriənz/", "người có tư tưởng tôn giáo cởi mở"),
    ("074316", "loppers", "noun", "/ˈlɒpərz/", "kéo cắt tỉa cành cây cán dài"),
    ("074317", "makeweights", "noun", "/ˈmeɪkˌweɪts/", "vật bù trọng lượng; người thế chỗ"),
    ("074318", "mameys", "noun", "/məˈmeɪz/", "quả vú sữa mamey nhiệt đới Mỹ"),
    ("074319", "matoakas", "noun", "/ˌmætoʊˈɑːkəz/", "công chúa Pocahontas (Matoaka)"),
    ("074320", "megaeras", "noun", "/mɪˈdʒɪərəz/", "nữ thần báo thù Megaera Hy Lạp"),
    ("074321", "merioneses", "noun", "/mɪˈraɪəniːzɪz/", "chi Chuột nhảy sa mạc Meriones"),
    ("074322", "minelayings", "noun", "/ˈmaɪnˌleɪɪŋz/", "hoạt động rải thủy lôi hoặc gài mìn"),
    ("074323", "misperceived", "verb", "/ˌmɪspərˈsiːvd/", "đã nhận thức sai lệch hiểu nhầm"),
    ("074324", "misperceives", "verb", "/ˌmɪspərˈsiːvz/", "nhận thức sai lệch, hiểu nhầm"),
    ("074325", "misperceiving", "verb", "/ˌmɪspərˈsiːvɪŋ/", "đang nhận thức sai lệch, hiểu nhầm"),
    ("074326", "momordicas", "noun", "/məˈmɔːrdɪkəz/", "chi Mướp đắng khổ qua (Momordica)"),
    ("074327", "nankeens", "noun", "/nænˈkiːnz/", "vải bông vàng nâu; quần vải nankin"),
    ("074328", "norgestrels", "noun", "/nɔːrˈdʒɛstrəlz/", "hoóc-môn tránh thai norgestrel"),
    ("074329", "orangewoods", "noun", "/ˈɒrɪndʒˌwʊdz/", "gỗ thân cây cam hương (cây cam)"),
    ("074330", "phocoenas", "noun", "/foʊˈsiːnəz/", "chi Cá heo chuột (Phocoena)"),
    ("074331", "photocoagulations", "noun", "/ˌfoʊtoʊkoʊæɡjʊˈleɪʃənz/", "kỹ thuật quang đông võng mạc laser"),
    ("074332", "potences", "noun", "/ˈpoʊtənsɪz/", "vũ khí hoặc cây thánh giá hình T"),
    ("074333", "quodlibets", "noun", "/ˈkwɒdlɪˌbɛts/", "đề tài tranh luận; liên khúc nhạc"),
    ("074334", "racecards", "noun", "/ˈreɪsˌkɑːrdz/", "tờ chương trình danh sách đua ngựa"),
    ("074335", "saltshakers", "noun", "/ˈsɔːltˌʃeɪkərz/", "lọ nhỏ đục lỗ rắc muối ăn"),
    ("074336", "scups", "noun", "/skʌps/", "cá tráp biển bạc Đại Tây Dương"),
    ("074337", "semideserts", "noun", "/ˌsɛmiˈdɛzərts/", "vùng bán hoang mạc khô cằn thưa cây"),
    ("074338", "serows", "noun", "/ˈsɛroʊz/", "sơn dương rừng châu Á (tỳ linh)"),
    ("074339", "spiritualized", "verb", "/ˈspɪrɪtʃuəˌlaɪzd/", "đã tâm linh hóa nâng lên tinh thần"),
    ("074340", "spiritualizes", "verb", "/ˈspɪrɪtʃuəˌlaɪzɪz/", "tâm linh hóa hướng về tinh thần"),
    ("074341", "spiritualizing", "verb", "/ˈspɪrɪtʃuəˌlaɪzɪŋ/", "đang tâm linh hóa nâng tinh thần"),
    ("074342", "strappadoes", "noun", "/strəˈpɑːdoʊz/", "hình phạt tra tấn treo ngược trói"),
    ("074343", "strappados", "noun", "/strəˈpɑːdoʊz/", "hình phạt tra tấn treo ngược trói"),
    ("074344", "strombuses", "noun", "/ˈstrɒmbəsɪz/", "chi Ốc tù và biển (Strombus)"),
    ("074345", "sulfanilamides", "noun", "/ˌsʌlfəˈnɪləˌmaɪdz/", "thuốc kháng khuẩn sulfanilamide"),
    ("074346", "sulindacs", "noun", "/sʊˈlɪndæks/", "thuốc kháng viêm giảm đau sulindac"),
    ("074347", "teratogens", "noun", "/ˈtɛrətədʒənz/", "tác nhân gây dị tật thai nhi"),
    ("074348", "thanatologies", "noun", "/ˌθænəˈtɒlədʒiz/", "tử vong học nghiên cứu cái chết"),
    ("074349", "theologists", "noun", "/θiˈɒlədʒɪsts/", "nhà thần học nghiên cứu tôn giáo"),
    ("074350", "triskaidekaphobias", "noun", "/ˌtrɪskaɪdɛkəˈfoʊbiəz/", "hội chứng ám ảnh sợ số mười ba"),
    ("074351", "upthrusts", "noun", "/ˈʌpˌθrʌsts/", "đứt gãy trồi nâng lên (địa chất)"),
    ("074352", "welwitschias", "noun", "/wɛlˈwɪtʃiəz/", "cây sa mạc trường thọ Welwitschia"),
    ("074353", "whinstones", "noun", "/ˈwɪnˌstoʊnz/", "đá bazan đen cứng (đá whin Anh)"),
    ("074354", "yellowwoods", "noun", "/ˈjɛloʊˌwʊdz/", "cây gỗ vàng yellowwood (Podocarpus)"),
    ("074355", "yersins", "noun", "/jɛərˈsænz/", "bác sĩ vi khuẩn học A. Yersin"),
    ("074356", "abetters", "noun", "/əˈbɛtərz/", "kẻ tiếp tay đồng lõa xúi giục"),
    ("074357", "abstainers", "noun", "/æbˈsteɪnərz/", "người kiêng rượu; người phiếu trắng"),
    ("074358", "afroasiatics", "noun", "/ˌæfroʊeɪʒiˈætɪks/", "ngữ hệ Phi-Á (Semit, Ai Cập...)"),
    ("074359", "alienages", "noun", "/ˈeɪliənɪdʒɪz/", "tình trạng người ngoại kiều (luật)"),
    ("074360", "angiomas", "noun", "/ˌændʒiˈoʊməz/", "u mạch máu hoặc mạch bạch huyết"),
    ("074361", "angiomata", "noun", "/ˌændʒiˈoʊmətə/", "u mạch máu hoặc mạch bạch huyết"),
    ("074362", "anoas", "noun", "/əˈnoʊəz/", "trâu rừng lùn anoa đảo Sulawesi"),
    ("074363", "antitypes", "noun", "/ˈæntɪˌtaɪps/", "hình mẫu tương ứng hoặc đối lập"),
    ("074364", "anurans", "noun", "/əˈnjʊərənz/", "động vật lưỡng cư không đuôi (ếch)"),
    ("074365", "apoapses", "noun", "/ˌæpoʊˈæpsiːz/", "điểm viễn tâm trên quỹ đạo elip"),
    ("074366", "apodemuses", "noun", "/ˌæpəˈdiːməsɪz/", "chi Chuột đồng rừng Cựu Thế giới"),
    ("074367", "appurtenances", "noun", "/əˈpɜːrtənənsɪz/", "phụ kiện đi kèm; quyền phụ thuộc"),
    ("074368", "arccoses", "noun", "/ˈɑːrkˌkoʊsɪz/", "hàm lượng giác ngược arccos"),
    ("074369", "assyriologies", "noun", "/əˌsɪriˈɒlədʒiz/", "ngành Assyria học Lưỡng Hà cổ đại"),
    ("074370", "athetoses", "noun", "/ˌæθɪˈtoʊsiːz/", "chứng múa vờn uốn éo tay chân"),
    ("074371", "azotes", "noun", "/əˈzoʊts/", "khí nitơ (tên gọi hóa học cũ)"),
    ("074372", "backcrossed", "verb", "/ˈbækˌkrɒst/", "đã lai hồi giao với thế hệ bố mẹ"),
    ("074373", "backcrosses", "verb", "/ˈbækˌkrɒsɪz/", "lai hồi giao (di truyền học)"),
    ("074374", "backcrossing", "verb", "/ˈbækˌkrɒsɪŋ/", "đang lai hồi giao với bố mẹ"),
    ("074375", "bedstraws", "noun", "/ˈbɛdˌstrɔːz/", "cây cỏ sữa đông Galium (thảo mộc)"),
    ("074376", "bichromates", "noun", "/baɪˈkroʊmeɪts/", "muối dicromat (bicromat) hóa học"),
    ("074377", "bladderworts", "noun", "/ˈblædərˌwɜːrts/", "cây bèo đất ăn bọ dưới nước"),
    ("074378", "bovids", "noun", "/ˈboʊvɪdz/", "động vật họ Trâu bò (bò, dê, cừu)"),
    ("074379", "carinates", "noun", "/ˈkærɪnɪts/", "chim biết bay có xương lưỡi hái"),
    ("074380", "chemoreceptors", "noun", "/ˌkiːmoʊrɪˈsɛptərz/", "thụ thể hóa học cảm nhận hóa chất"),
    ("074381", "chrysoberyls", "noun", "/ˈkrɪsəˌbɛrəlz/", "đá quý chrysoberyl (mắt mèo)"),
    ("074382", "collotypes", "noun", "/ˈkɒləˌtaɪps/", "kỹ thuật in bản keo gelatin"),
    ("074383", "condonations", "noun", "/ˌkɒndəˈneɪʃənz/", "sự tha thứ bỏ qua lỗi lầm (luật)"),
    ("074384", "costumiers", "noun", "/kɒˈstjʊmjərz/", "người thiết kế cho thuê trang phục"),
    ("074385", "countryfolks", "noun", "/ˈkʌntriˌfoʊks/", "người dân sống ở vùng nông thôn"),
    ("074386", "crosspieces", "noun", "/ˈkrɒsˌpiːsɪz/", "thanh giằng ngang bắc ngang qua"),
    ("074387", "cuirassiers", "noun", "/ˌkwɪrəˈsɪərz/", "kỵ binh nặng mặc áo giáp ngực xưa"),
    ("074388", "cuscuses", "noun", "/ˈkʌskəsɪz/", "thú có túi leo cây cuscus châu Úc"),
    ("074389", "demijohns", "noun", "/ˈdɛmiˌdʒɒnz/", "bình thủy tinh cổ hẹp bọc giỏ mây"),
    ("074390", "dicentras", "noun", "/daɪˈsɛntrəz/", "cây hoa trái tim rỉ máu"),
    ("074391", "disinvested", "verb", "/ˌdɪsɪnˈvɛstɪd/", "đã thoái vốn rút vốn đầu tư"),
    ("074392", "disinvesting", "verb", "/ˌdɪsɪnˈvɛstɪŋ/", "đang thoái vốn rút vốn đầu tư"),
    ("074393", "disinvests", "verb", "/ˌdɪsɪnˈvɛsts/", "thoái vốn, rút vốn đầu tư ra khỏi"),
    ("074394", "doorsills", "noun", "/ˈdɔːrˌsɪlz/", "bệ ngưỡng cửa ra vào sát sàn"),
    ("074395", "dossers", "noun", "/ˈdɒsərz/", "người vô gia cư ngủ trọ rẻ (Anh)"),
    ("074396", "drachms", "noun", "/dræmz/", "đơn vị đơ-ram; đồng bạc Hy Lạp cổ"),
    ("074397", "duologues", "noun", "/ˈdjuːəˌlɒɡz/", "màn đối thoại tay đôi hai nhân vật"),
    ("074398", "duratives", "noun", "/ˈdjʊərətɪvz/", "thể kéo dài liên tục (ngôn ngữ)"),
    ("074399", "enlistees", "noun", "/ˌɛnlɪˈstiːz/", "tân binh nhập ngũ quân đội"),
    ("074400", "eriophorums", "noun", "/ˌɛriˈɒfərəmz/", "cây cỏ bông tuyết Bắc Cực"),
    ("074401", "exophthalmoses", "noun", "/ˌɛksɒfˈθælmoʊsɪz/", "chứng lồi nhãn cầu (Basedow)"),
    ("074402", "fairleads", "noun", "/ˈfɛərˌliːdz/", "khoen hoặc ròng rọc dẫn hướng dây"),
]

with open("scratch/b35_r09_raw_p4.json") as f:
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

with open("scratch/b35_r09_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r09_p4.json OK")
