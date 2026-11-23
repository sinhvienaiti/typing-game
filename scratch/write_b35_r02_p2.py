import json

items = [
    ("070603", "thermochemistries", "noun", "/ˌθɜːrmoʊˈkɛmɪstriz/", "ngành nhiệt hóa học"),
    ("070604", "towelings", "noun", "/ˈtaʊəlɪŋz/", "vải thô dệt làm khăn tắm lau"),
    ("070605", "trigrams", "noun", "/ˈtraɪˌɡræmz/", "quẻ ba hào Kinh Dịch; nhóm ba chữ"),
    ("070606", "underlayments", "noun", "/ˈʌndərˌleɪmənts/", "lớp lót dưới sàn nhà hoặc mái"),
    ("070607", "undersurfaces", "noun", "/ˈʌndərˌsɜːrfɪsɪz/", "bề mặt phía dưới đáy"),
    ("070608", "unguents", "noun", "/ˈʌŋɡwənts/", "thuốc mỡ bôi da; dầu thơm xức"),
    ("070609", "urias", "noun", "/jʊˈraɪəz/", "chim biển mỏ nhọn họ Anka"),
    ("070610", "varixes", "noun", "/ˈvɛərɪksɪz/", "búi giãn tĩnh mạch ngoằn ngoèo"),
    ("070611", "volutions", "noun", "/vəˈluːʃənz/", "vòng xoắn ốc; chuyển động cuộn xoay"),
    ("070612", "vulgarians", "noun", "/vʌlˈɡɛəriənz/", "người thô tục thiếu văn hóa"),
    ("070613", "watchbands", "noun", "/ˈwɒtʃˌbændz/", "dây đeo đồng hồ đeo tay"),
    ("070614", "weeders", "noun", "/ˈwiːdərz/", "dụng cụ nhổ cỏ; người làm cỏ"),
    ("070615", "whaleboats", "noun", "/ˈweɪlˌboʊts/", "thuyền chèo mũi nhọn săn cá voi"),
    ("070616", "whitethroats", "noun", "/ˈwaɪtˌθroʊts/", "chim chích họng trắng châu Âu"),
    ("070617", "whoredoms", "noun", "/ˈhɔːrdəmz/", "tệ nạn mại dâm; sự sa đọa (cổ)"),
    ("070618", "acroporas", "noun", "/əˈkrɒpərəz/", "san hô cành thuộc chi Acropora"),
    ("070619", "amauroses", "noun", "/ˌæmɔːˈroʊsiːz/", "chứng mù không tổn thương nhãn cầu"),
    ("070620", "aneled", "verb", "/əˈniːld/", "đã xức dầu thánh (cổ)"),
    ("070621", "aneles", "verb", "/əˈniːlz/", "xức dầu thánh cầu nguyện (cổ)"),
    ("070622", "aneling", "verb", "/əˈniːlɪŋ/", "đang xức dầu thánh (cổ)"),
    ("070623", "anouilhs", "noun", "/ɑːˈnuːiz/", "nhà soạn kịch Pháp Jean Anouilh"),
    ("070624", "answerers", "noun", "/ˈænsərərz/", "người trả lời; máy tự động trả lời"),
    ("070625", "appanages", "noun", "/ˈæpənɪdʒɪz/", "thái ấp ban cấp; đặc quyền đi kèm"),
    ("070626", "apsus", "noun", "/ˈæpsuːs/", "vị thần nước ngọt Apsu (Lưỡng Hà)"),
    ("070627", "arachises", "noun", "/əˈreɪkɪsɪz/", "chi Đậu phộng (lạc) Arachis"),
    ("070628", "archilochi", "noun", "/ˌɑːrkɪˈloʊkaɪ/", "chi Chim ruồi Archilochus"),
    ("070629", "arquebuses", "noun", "/ˈɑːrkwɪˌbʌsɪz/", "súng hỏa mai cổ có giá đỡ"),
    ("070630", "batswanas", "noun", "/bɑːtˈswɑːnəz/", "người dân nước Botswana"),
    ("070631", "breastworks", "noun", "/ˈbrɛstˌwɜːrks/", "công sự lũy đất đắp che ngực"),
    ("070632", "britishers", "noun", "/ˈbrɪtɪʃərz/", "người Anh (khẩu ngữ)"),
    ("070633", "brythonics", "noun", "/brɪˈθɒnɪks/", "nhóm ngôn ngữ Celt Briton"),
    ("070634", "butylenes", "noun", "/ˈbjuːtɪˌliːnz/", "khí butylen thuộc dãy anken"),
    ("070635", "captoprils", "noun", "/ˈkæptəˌprɪlz/", "thuốc hạ huyết áp captopril"),
    ("070636", "chelonias", "noun", "/kɪˈloʊniəz/", "chi Rùa biển xanh Chelonia"),
    ("070637", "chichewas", "noun", "/tʃɪˈtʃeɪwəz/", "dân tộc và tiếng Chichewa (Malawi)"),
    ("070638", "cholecalciferols", "noun", "/ˌkoʊlɪkælˈsɪfəˌrɒlz/", "vitamin D3 (cholecalciferol)"),
    ("070639", "cholecystokinins", "noun", "/ˌkoʊlɪˌsɪstoʊˈkaɪnɪnz/", "hoóc-môn tiêu hóa cholecystokinin"),
    ("070640", "chunnels", "noun", "/ˈtʃʌnəlz/", "đường hầm eo biển Manche (Anh-Pháp)"),
    ("070641", "chuvashes", "noun", "/tʃuːˈvɑːʃɪz/", "người dân tộc và tiếng Chuvash"),
    ("070642", "coxas", "noun", "/ˈkɒksəz/", "xương hông; đốt háng chân côn trùng"),
    ("070643", "crystalizes", "verb", "/ˈkrɪstəˌlaɪzɪz/", "kết tinh thành tinh thể; rõ nét"),
    ("070644", "crystalizing", "verb", "/ˈkrɪstəˌlaɪzɪŋ/", "đang kết tinh; đang làm rõ nét"),
    ("070645", "decussated", "verb", "/ˈdɛkəˌseɪtɪd/", "đã giao chéo hình chữ thập (X)"),
    ("070646", "decussates", "verb", "/ˈdɛkəˌseɪts/", "bắt chéo hình chữ thập (X)"),
    ("070647", "decussating", "verb", "/ˈdɛkəˌseɪtɪŋ/", "đang bắt chéo hình chữ thập (X)"),
    ("070648", "deflagrations", "noun", "/ˌdɛfləˈɡreɪʃənz/", "sự cháy nổ tỏa nhiệt cận âm"),
    ("070649", "degustations", "noun", "/ˌdiːɡʌˈsteɪʃənz/", "buổi nếm thử rượu vang và món ăn"),
    ("070650", "delphinuses", "noun", "/dɛlˈfaɪnəsɪz/", "chòm sao Hải Đồn (Cá Heo)"),
    ("070651", "demoralisations", "noun", "/dɪˌmɒrəlaɪˈzeɪʃənz/", "sự làm suy sụp tinh thần nản lòng"),
    ("070652", "demurrages", "noun", "/dɪˈmɜːrɪdʒɪz/", "phí lưu tàu quá hạn bốc dỡ"),
    ("070653", "diastemas", "noun", "/ˌdaɪəˈstiːməz/", "khe hở giữa hai răng liền kề"),
    ("070654", "diastemata", "noun", "/ˌdaɪəˈstɛmətə/", "khe hở giữa hai răng cửa"),
    ("070655", "dikas", "noun", "/ˈdiːkəz/", "cây xoài hoang Tây Phi dika"),
    ("070656", "doornails", "noun", "/ˈdɔːrˌneɪlz/", "đinh mũ lớn đóng chốt cánh cửa gỗ"),
    ("070657", "dysgraphias", "noun", "/dɪsˈɡræfiəz/", "chứng rối loạn khả năng viết chữ"),
    ("070658", "echinococci", "noun", "/ɪˌkaɪnoʊˈkɒkaɪ/", "sán dải chó ký sinh Echinococcus"),
    ("070659", "erigerons", "noun", "/ɪˈrɪdʒərənz/", "cây cúc đầu nhỏ thuộc chi Erigeron"),
    ("070660", "escheats", "noun", "/ɪsˈtʃiːts/", "tài sản vô chủ xung công"),
    ("070661", "farthingales", "noun", "/ˈfɑːrðɪŋˌɡeɪlz/", "khung tùng váy phồng thời Phục Hưng"),
    ("070662", "frontbenchers", "noun", "/ˌfrʌntˈbɛntʃərz/", "nghị sĩ chủ chốt ngồi hàng ghế đầu"),
    ("070663", "gloriosas", "noun", "/ɡlɔːˈriːoʊzəz/", "cây huệ diệu leo rực rỡ Gloriosa"),
    ("070664", "guairas", "noun", "/ˈɡwaɪrəz/", "thác Guaira trên sông Paraná"),
    ("070665", "haiks", "noun", "/haɪks/", "áo choàng trùm haik vùng Bắc Phi"),
    ("070666", "hammarskjolds", "noun", "/ˈhæmərˌʃʊldz/", "tổng thư ký LHQ Dag Hammarskjöld"),
    ("070667", "heveas", "noun", "/ˈhiːviəz/", "cây cao su tự nhiên chi Hevea"),
    ("070668", "hirundos", "noun", "/hɪˈrʌndoʊz/", "chim nhạn én thuộc chi Hirundo"),
    ("070669", "hydropses", "noun", "/ˈhaɪdrɒpsɪz/", "chứng phù ứ dịch trong mô cơ thể"),
    ("070670", "initialised", "verb", "/ɪˈnɪʃəˌlaɪzd/", "đã khởi tạo giá trị ban đầu (Anh)"),
    ("070671", "initialises", "verb", "/ɪˈnɪʃəˌlaɪzɪz/", "khởi tạo giá trị ban đầu (Anh)"),
    ("070672", "initialising", "verb", "/ɪˈnɪʃəˌlaɪzɪŋ/", "đang khởi tạo giá trị ban đầu"),
    ("070673", "ixias", "noun", "/ˈɪksiəz/", "hoa diên vĩ ngô đồng châu Phi Ixia"),
    ("070674", "kabbalists", "noun", "/ˈkæbəlɪsts/", "nhà nghiên cứu mật giáo Kabbalah"),
    ("070675", "knapweeds", "noun", "/ˈnæpˌwiːdz/", "cây cỏ cúc gai đầu tròn Centaurea"),
    ("070676", "laryngectomies", "noun", "/ˌlærɪnˈdʒɛktəmiz/", "phẫu thuật cắt bỏ thanh quản"),
    ("070677", "letterers", "noun", "/ˈlɛtərərz/", "thợ vẽ chữ biển hiệu thủ công"),
    ("070678", "letups", "noun", "/ˈlɛtˌʌps/", "sự tạm lắng dịu bớt; sự ngừng nghỉ"),
    ("070679", "lobitos", "noun", "/loʊˈbiːtoʊz/", "thành phố cảng Lobito ở Angola"),
    ("070680", "logwoods", "noun", "/ˈlɒɡˌwʊdz/", "cây gỗ vang nhuộm màu tím đỏ"),
    ("070681", "lylies", "noun", "/ˈlɪliz/", "nhà văn Anh John Lyly"),
    ("070682", "marylanders", "noun", "/ˈmɛrɪləndərz/", "người dân bang Maryland của Mỹ"),
    ("070683", "massawas", "noun", "/məˈsɑːwəz/", "thành phố cảng Massawa ở Eritrea"),
    ("070684", "microdots", "noun", "/ˈmaɪkroʊˌdɒts/", "vi ảnh gián điệp thu nhỏ cỡ chấm"),
    ("070685", "mimeoed", "verb", "/ˈmɪmiˌoʊd/", "đã in quay rônêô bằng giấy sáp"),
    ("070686", "mimeoing", "verb", "/ˈmɪmiˌoʊɪŋ/", "đang in quay rônêô bằng giấy sáp"),
    ("070687", "mimeos", "noun", "/ˈmɪmiˌoʊz/", "máy in rônêô; bản in bằng giấy sáp"),
    ("070688", "mimirs", "noun", "/ˈmiːmɪərz/", "thần trí tuệ Mímir Bắc Âu"),
    ("070689", "minified", "verb", "/ˈmɪnɪˌfaɪd/", "đã thu gọn kích thước (mã nguồn)"),
    ("070690", "minifies", "verb", "/ˈmɪnɪˌfaɪz/", "thu gọn kích thước; làm nhỏ lại"),
    ("070691", "minifying", "verb", "/ˈmɪnɪˌfaɪɪŋ/", "đang thu gọn kích thước; làm nhỏ"),
    ("070692", "naphthols", "noun", "/ˈnæfθɒlz/", "hợp chất hữu cơ naphthol"),
    ("070693", "nemeas", "noun", "/ˈniːmiəz/", "thung lũng cổ đại Nemea Hy Lạp"),
    ("070694", "overstressed", "verb", "/ˌoʊvərˈstrɛst/", "đã nhấn mạnh thái quá; quá căng"),
    ("070695", "overstresses", "verb", "/ˌoʊvərˈstrɛsɪz/", "nhấn mạnh thái quá; làm quá tải"),
    ("070696", "overstressing", "verb", "/ˌoʊvərˈstrɛsɪŋ/", "đang nhấn mạnh quá mức; quá tải"),
    ("070697", "paddlefishes", "noun", "/ˈpædəlˌfɪʃɪz/", "cá tầm thìa mỏ dẹt Bắc Mỹ"),
    ("070698", "pansas", "noun", "/ˈpɑːnsəz/", "tháng lịch cổ Pansa; tên họ La Mã"),
    ("070699", "pasiphaes", "noun", "/pəˈsɪfəˌiːz/", "hoàng hậu Pasiphaë đảo Crete cổ"),
    ("070700", "perseas", "noun", "/pɜːrˈsiːəz/", "chi Cây bơ thực vật (Persea)"),
    ("070701", "phagocytes", "noun", "/ˈfæɡəˌsaɪts/", "tế bào thực bào ăn vi khuẩn"),
    ("070702", "pipistrelles", "noun", "/ˈpɪpɪˌstrɛlz/", "dơi muỗi nhỏ châu Âu pipistrelle"),
]

with open("scratch/b35_r02_raw_p2.json") as f:
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

with open("scratch/b35_r02_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r02_p2.json OK")
