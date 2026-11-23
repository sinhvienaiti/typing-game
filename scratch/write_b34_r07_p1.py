import json

items = [
    ("068003", "diltiazems", "noun", "/dɪlˈtaɪəzəmz/", "thuốc chẹn canxi trị cao huyết áp"),
    ("068004", "draggers", "noun", "/ˈdræɡərz/", "người lôi kéo; máy rà quét đáy biển"),
    ("068005", "dramatised", "verb", "/ˈdræməˌtaɪzd/", "đã chuyển thể thành kịch; kịch tính"),
    ("068006", "dramatises", "verb", "/ˈdræməˌtaɪzɪz/", "chuyển thể kịch; làm kịch tính hóa"),
    ("068007", "dramatising", "verb", "/ˈdræməˌtaɪzɪŋ/", "đang dựng kịch; phóng đại kịch tính"),
    ("068008", "dreadnaughts", "noun", "/ˈdrɛdˌnɔːts/", "thiết giáp hạm cỡ lớn đầu thế kỷ 20"),
    ("068009", "embezzlers", "noun", "/ɪmˈbɛzlərz/", "kẻ tham ô biển thủ công quỹ"),
    ("068010", "equipages", "noun", "/ˈɛkwɪpɪdʒɪz/", "xe ngựa sang trọng kèm người hầu"),
    ("068011", "farads", "noun", "/ˈfærədz/", "đơn vị điện dung fara (SI)"),
    ("068012", "finitenesses", "noun", "/ˈfaɪnaɪtnəsɪz/", "tính hữu hạn có giới hạn xác định"),
    ("068013", "fireclays", "noun", "/ˈfaɪərˌkleɪz/", "đất sét chịu nhiệt làm gạch lò nung"),
    ("068014", "galangals", "noun", "/ˈɡælənɡəlz/", "củ cây riềng nếp gia vị Đông Nam Á"),
    ("068015", "gamins", "noun", "/ˈɡæmɪnz/", "trẻ bụi đời lang thang đường phố"),
    ("068016", "gastrins", "noun", "/ˈɡæstrɪnz/", "hoóc-môn gastrin kích thích axit vị"),
    ("068017", "genua", "noun", "/ˈdʒɛnjuːə/", "khớp đầu gối; phần gập cấu trúc não"),
    ("068018", "hargeisas", "noun", "/hɑːrˈɡeɪsəz/", "thành phố Hargeisa ở Somalia"),
    ("068019", "hassams", "noun", "/ˈhæsəmz/", "họa sĩ ấn tượng Mỹ Childe Hassam"),
    ("068020", "haycocks", "noun", "/ˈheɪˌkɒks/", "đống cỏ khô vun hình nón trên đồng"),
    ("068021", "hemings", "noun", "/ˈhɛmɪŋz/", "diễn viên Anh John Heminges"),
    ("068022", "hesperideses", "noun", "/hɛˈspɛrɪdiːzɪz/", "tiên nữ vườn táo vàng Hesperides"),
    ("068023", "hindoos", "noun", "/ˈhɪnduːz/", "tín đồ Ấn Độ giáo (cách viết cũ)"),
    ("068024", "holloed", "verb", "/ˈhɒloʊd/", "đã hô vang gọi to; đã reo hò lớn"),
    ("068025", "holloing", "verb", "/ˈhɒloʊɪŋ/", "đang hô vang gọi to réo ầm ĩ"),
    ("068026", "hollos", "noun", "/ˈhɒloʊz/", "tiếng hô vang lớn gọi nhau"),
    ("068027", "hornswoggled", "verb", "/ˈhɔːrnˌswɒɡəld/", "đã lừa bịp qua mặt khéo léo (Mỹ)"),
    ("068028", "hornswoggles", "verb", "/ˈhɔːrnˌswɒɡəlz/", "lừa bịp phỉnh phờ khéo léo (lóng)"),
    ("068029", "hornswoggling", "verb", "/ˈhɔːrnˌswɒɡlɪŋ/", "đang lừa gạt qua mặt người khác"),
    ("068030", "hududs", "noun", "/hʊˈduːdz/", "hệ thống hình phạt luật Hồi giáo"),
    ("068031", "hussites", "noun", "/ˈhʌsaɪts/", "tín đồ phong trào cải cách Hussite"),
    ("068032", "ichors", "noun", "/ˈaɪkɔːrz/", "máu thần Hy Lạp; dịch vết loét"),
    ("068033", "inosines", "noun", "/ˈɪnəˌsiːnz/", "hợp chất nucleoside inosin sinh học"),
    ("068034", "karaiteses", "noun", "/ˈkærəˌaɪtsɪz/", "giáo phái Do Thái Karaite"),
    ("068035", "khoisans", "noun", "/ˈkɔɪsɑːnz/", "dân tộc và ngữ hệ Khoisan Nam Phi"),
    ("068036", "killdeers", "noun", "/ˈkɪlˌdɪərz/", "chim choi choi cổ khoang killdeer"),
    ("068037", "koinonias", "noun", "/ˌkɔɪnoʊˈniːəz/", "tình hiệp thông cộng đồng Cơ đốc"),
    ("068038", "lifehacked", "verb", "/ˈlaɪfˌhækt/", "đã dùng mẹo vặt tối ưu đời sống"),
    ("068039", "lifehacking", "verb", "/ˈlaɪfˌhækɪŋ/", "đang áp dụng mẹo vặt tiện ích"),
    ("068040", "lifehacks", "verb", "/ˈlaɪfˌhæks/", "áp dụng mẹo vặt xử lý nhanh việc"),
    ("068041", "macromolecules", "noun", "/ˌmækroʊˈmɒlɪˌkjuːlz/", "đại phân tử sinh học như protein"),
    ("068042", "mandrills", "noun", "/ˈmændrɪlz/", "khỉ đầu chó mặt vằn sặc sỡ mandrill"),
    ("068043", "melanocytes", "noun", "/məˈlænəˌsaɪts/", "tế bào hắc tố sản sinh melanin da"),
    ("068044", "narrowboats", "noun", "/ˈnæroʊˌboʊts/", "thuyền thân hẹp đi kênh đào Anh"),
    ("068045", "nazes", "noun", "/neɪzɪz/", "mũi đất nhô ra biển nhọn Naze"),
    ("068046", "niceties", "noun", "/ˈnaɪsɪtiz/", "chi tiết tinh tế; phép lịch sự nhỏ"),
    ("068047", "oarsmen", "noun", "/ˈɔːrzmən/", "người chèo thuyền bằng mái chèo"),
    ("068048", "oasts", "noun", "/oʊsts/", "lò sấy hoa bia khô làm bia"),
    ("068049", "oleoresins", "noun", "/ˌoʊlioʊˈrɛzɪnz/", "nhựa dầu chiết xuất từ gia vị"),
    ("068050", "orchiectomies", "noun", "/ˌɔːrkiˈɛktəmiz/", "ca phẫu thuật cắt bỏ tinh hoàn"),
    ("068051", "padrones", "noun", "/pəˈdroʊniz/", "chủ thầu môi giới lao động; ông chủ"),
    ("068052", "pasches", "noun", "/ˈpæsks/", "lễ Phục Sinh hoặc lễ Vượt Qua"),
    ("068053", "pemphiguses", "noun", "/ˈpɛmfɪɡəsɪz/", "bệnh bóng nước tự miễn pemphigus"),
    ("068054", "phanerozoics", "noun", "/ˌfænərəˈzoʊɪks/", "liên đại Hiển Sinh trong địa chất"),
    ("068055", "photocells", "noun", "/ˈfoʊtoʊˌsɛlz/", "tế bào quang điện cảm biến sáng"),
    ("068056", "pictographs", "noun", "/ˈpɪktəˌɡræfs/", "chữ tượng hình vẽ trên đá cổ"),
    ("068057", "pommies", "noun", "/ˈpɒmiz/", "người Anh (tiếng lóng ở Úc)"),
    ("068058", "positioners", "noun", "/pəˈzɪʃənərz/", "bộ định vị van; thiết bị căn chỉnh"),
    ("068059", "railroaders", "noun", "/ˈreɪlˌroʊdərz/", "công nhân nhân viên ngành đường sắt"),
    ("068060", "recusants", "noun", "/ˈrɛkjʊzənts/", "người chống đối không tuân thủ lễ"),
    ("068061", "redshanks", "noun", "/ˈrɛdˌʃæŋks/", "chim choi choi chân đỏ vùng đầm lầy"),
    ("068062", "rostands", "noun", "/rɒˈstɒnz/", "nhà soạn kịch Pháp Edmond Rostand"),
    ("068063", "rotenones", "noun", "/ˈroʊtəˌnoʊnz/", "chất độc thảo mộc diệt cá rotenon"),
    ("068064", "sabatons", "noun", "/ˈsæbəˌtɒnz/", "giày sắt bọc bàn chân áo giáp hiệp"),
    ("068065", "schonbergs", "noun", "/ˈʃɜːrnbɜːrɡz/", "nhà soạn nhạc Áo Arnold Schoenberg"),
    ("068066", "sexpots", "noun", "/ˈsɛksˌpɒts/", "người ăn mặc gợi cảm quyến rũ"),
    ("068067", "shovelers", "noun", "/ˈʃʌvələrz/", "vịt mỏ thìa; người xúc xẻng"),
    ("068068", "silenuses", "noun", "/saɪˈliːnəsɪz/", "thần rừng say rượu Silenus Hy Lạp"),
    ("068069", "skandas", "noun", "/ˈskʌndəz/", "thần chiến tranh Skanda; ngũ uẩn"),
    ("068070", "sourpusses", "noun", "/ˈsaʊərˌpʊsɪz/", "người mặt cau có hay càu nhàu"),
    ("068071", "spallations", "noun", "/spɔːˈleɪʃənz/", "phản ứng vỡ hạt nhân; sự bong vảy"),
    ("068072", "sporulations", "noun", "/ˌspɒrjəˈleɪʃənz/", "quá trình hình thành bào tử"),
    ("068073", "suburbanites", "noun", "/səˈbɜːrbəˌnaɪts/", "cư dân sinh sống ở vùng ngoại ô"),
    ("068074", "sweatbands", "noun", "/ˈswɛtˌbændz/", "băng vải thấm mồ hôi trán cổ tay"),
    ("068075", "tamarindos", "noun", "/ˌtæməˈrɪndoʊz/", "cây me ăn quả chua ngọt nhiệt đới"),
    ("068076", "taxuses", "noun", "/ˈtæksəsɪz/", "cây thủy tùng thông đỏ chi Taxus"),
    ("068077", "threescores", "noun", "/ˈθriːˌskɔːrz/", "số lượng sáu mươi (văn cổ)"),
    ("068078", "tikes", "noun", "/taɪks/", "đứa trẻ nhỏ; chó lai (khẩu ngữ)"),
    ("068079", "triskelia", "noun", "/traɪˈskɛliə/", "biểu tượng ba chân xoáy triskelion"),
    ("068080", "triskelions", "noun", "/traɪˈskɛliɒnz/", "họa tiết tam xoáy ba nhánh đối xứng"),
    ("068081", "ubiquinones", "noun", "/juːˈbɪkwɪˌnoʊnz/", "coenzym Q10 vận chuyển điện tử"),
    ("068082", "unios", "noun", "/ˈjuːnioʊz/", "trai sông nước ngọt thuộc chi Unio"),
    ("068083", "usurers", "noun", "/ˈjuːʒərərz/", "kẻ cho vay nặng lãi cắt cổ"),
    ("068084", "walloonses", "noun", "/wɒˈluːnzɪz/", "người vùng Wallonia nói tiếng Pháp"),
    ("068085", "washtubs", "noun", "/ˈwɒʃˌtʌbz/", "chậu hoặc thùng lớn giặt quần áo"),
    ("068086", "widgeons", "noun", "/ˈwɪdʒənz/", "vịt trời đầu vàng widgeon"),
    ("068087", "wimples", "noun", "/ˈwɪmpəlz/", "khăn trùm kín đầu cổ nữ tu thời xưa"),
    ("068088", "yakuts", "noun", "/jɑːˈkʊts/", "người dân tộc Yakut ở vùng Siberia"),
    ("068089", "abadans", "noun", "/ˌɑːbɑːˈdɑːnz/", "thành phố dầu mỏ Abadan ở Iran"),
    ("068090", "abrading", "verb", "/əˈbreɪdɪŋ/", "đang mài mòn làm trầy xước bề mặt"),
    ("068091", "acroleins", "noun", "/əˈkroʊliɪnz/", "hợp chất anđehit không no acrolein"),
    ("068092", "aerialists", "noun", "/ˈɛəriəlɪsts/", "nghệ sĩ nhào lộn đu dây trên không"),
    ("068093", "airbursts", "noun", "/ˈɛərˌbɜːrsts/", "vụ nổ bom phát nổ trên không trung"),
    ("068094", "alnicos", "noun", "/ˈælnɪˌkoʊz/", "hợp kim nam châm vĩnh cửu Alnico"),
    ("068095", "anthropometries", "noun", "/ˌænθrəˈpɒmɪtriz/", "ngành nhân trắc học đo kích thước"),
    ("068096", "anticyclones", "noun", "/ˌæntiˈsaɪkloʊnz/", "vùng xoáy nghịch áp suất khí cao"),
    ("068097", "aquitanias", "noun", "/ˌækwɪˈteɪniəz/", "vùng lịch sử Aquitaine tây nam Pháp"),
    ("068098", "armigers", "noun", "/ˈɑːrmɪdʒərz/", "người mang khiên hiệp sĩ; gia huy"),
    ("068099", "assayers", "noun", "/əˈseɪərz/", "chuyên viên thử nghiệm quặng kim"),
    ("068100", "bagfuls", "noun", "/ˈbæɡˌfʊlz/", "lượng đồ chứa đầy một túi"),
    ("068101", "blacklegged", "verb", "/ˈblækˌlɛɡd/", "đã phá đám đình công; đã lừa đảo"),
    ("068102", "blacklegging", "verb", "/ˈblækˌlɛɡɪŋ/", "đang phá đám đình công làm thay"),
]

with open("scratch/b34_r07_raw_p1.json") as f:
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

with open("scratch/b34_r07_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r07_p1.json OK")
