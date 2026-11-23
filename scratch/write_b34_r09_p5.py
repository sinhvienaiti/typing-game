import json

items = [
    ("069403", "diethylstilbestrols", "noun", "/daɪˌɛθəlstɪlˈbɛstrɒlz/", "estrogen tổng hợp DES (dược phẩm)"),
    ("069404", "dimetrodons", "noun", "/daɪˈmɛtrəˌdɒnz/", "bò sát tiền sử vây lưng Dimetrodon"),
    ("069405", "divertimenti", "noun", "/dɪˌvɛərtɪˈmɛnti/", "tổ khúc nhạc nhẹ nhàng divertimento"),
    ("069406", "divertimentos", "noun", "/dɪˌvɛərtɪˈmɛntoʊz/", "bản nhạc giải trí nhẹ divertimento"),
    ("069407", "downstrokes", "noun", "/ˈdaʊnˌstroʊks/", "nét bút kéo từ trên xuống dưới"),
    ("069408", "earthmans", "noun", "/ˈɜːrθmənz/", "cư dân Trái Đất (khoa học viễn)"),
    ("069409", "ecclesiasticuses", "noun", "/ɪˌkliːziˈæstɪkəsɪz/", "sách Huấn Ca trong Cựu Ước"),
    ("069410", "ecuadorans", "noun", "/ˌɛkwəˈdɔːrənz/", "người dân nước Cộng hòa Ecuador"),
    ("069411", "embryologists", "noun", "/ˌɛmbriˈɒlədʒɪsts/", "nhà khoa học nghiên cứu phôi học"),
    ("069412", "enteropathies", "noun", "/ˌɛntəˈrɒpəθiz/", "bệnh lý tổn thương ở ruột non"),
    ("069413", "enumerators", "noun", "/ɪˈnjuːməˌreɪtərz/", "nhân viên điều tra thống kê dân số"),
    ("069414", "escolars", "noun", "/ɛˈskɒlərz/", "cá thu dầu biển sâu thịt béo"),
    ("069415", "essenes", "noun", "/ɛˈsiːnz/", "giáo phái khổ hạnh Do Thái Essene"),
    ("069416", "exonucleases", "noun", "/ˌɛksoʊˈnjuːkliˌeɪsɪz/", "enzym cắt tỉa đầu chuỗi ADN ARN"),
    ("069417", "fellies", "noun", "/ˈfɛliz/", "vành gỗ cong tạo niềng bánh xe ngựa"),
    ("069418", "frunzes", "noun", "/ˈfrʊnzɪz/", "thành phố Frunze (tên cũ Bishkek)"),
    ("069419", "gamines", "noun", "/ɡæˈmiːnz/", "cô bé tinh nghịch nhanh nhẹn"),
    ("069420", "handwrited", "verb", "/ˈhændˌraɪtɪd/", "đã viết bằng tay (biến thể hiếm)"),
    ("069421", "handwrites", "verb", "/ˈhændˌraɪts/", "viết tay trực tiếp lên giấy"),
    ("069422", "harmonizers", "noun", "/ˈhɑːrməˌnaɪzərz/", "người hòa âm nhạc; bộ hòa tiếng"),
    ("069423", "harpsichordists", "noun", "/ˈhɑːrpsɪˌkɔːrdɪsts/", "nghệ sĩ đàn phím cổ harpsichord"),
    ("069424", "hordeums", "noun", "/ˈhɔːrdiəmz/", "cây lúa mạch thuộc chi Hordeum"),
    ("069425", "hrvatskas", "noun", "/hərˈvɑːtskəz/", "đất nước Croatia (tên bản địa)"),
    ("069426", "hydronephroses", "noun", "/ˌhaɪdroʊnəˈfroʊsiːz/", "bệnh thận ứ nước giãn đài bể thận"),
    ("069427", "imbricates", "verb", "/ˈɪmbrɪˌkeɪts/", "xếp gối chồng lên nhau như ngói"),
    ("069428", "imbricating", "verb", "/ˈɪmbrɪˌkeɪtɪŋ/", "đang xếp chồng lên nhau như ngói"),
    ("069429", "intervenors", "noun", "/ˌɪntərˈviːnərz/", "bên thứ ba can thiệp tố tụng"),
    ("069430", "ischaemias", "noun", "/ɪˈskiːmiəz/", "tình trạng thiếu máu cục bộ mô"),
    ("069431", "janissaries", "noun", "/ˈdʒænɪˌsɛriz/", "cận vệ tinh nhuệ Janissary Thổ"),
    ("069432", "jehads", "noun", "/dʒɪˈhɑːdz/", "cuộc thánh chiến Hồi giáo"),
    ("069433", "jointures", "noun", "/ˈdʒɔɪntʃərz/", "tài sản bảo đảm cho vợ góa phụ"),
    ("069434", "kadais", "noun", "/kəˈdaɪz/", "nhóm ngôn ngữ Kra-Dai Đông Nam Á"),
    ("069435", "kanaras", "noun", "/ˈkænərəz/", "vùng ven biển Kanara ở Ấn Độ"),
    ("069436", "kinescopes", "noun", "/ˈkɪnɪˌskoʊps/", "ống đèn hình âm cực truyền hình cũ"),
    ("069437", "kwakiutls", "noun", "/kwɑːˈkjuːtəlz/", "bộ tộc bản địa Kwakwaka'wakw"),
    ("069438", "lagopuses", "noun", "/ˈlæɡəpəsɪz/", "chim gà gô tuyết chi Lagopus"),
    ("069439", "larned", "verb", "/lɑːrnd/", "đã học; đã dạy bảo (phương ngữ)"),
    ("069440", "larning", "verb", "/ˈlɑːrnɪŋ/", "đang học hỏi; dạy (phương ngữ)"),
    ("069441", "larns", "verb", "/lɑːrnz/", "học hành; dạy bảo (phương ngữ)"),
    ("069442", "lathyruses", "noun", "/ˈlæθɪrəsɪz/", "cây đậu hương thuộc chi Lathyrus"),
    ("069443", "laybies", "noun", "/ˈleɪˌbaɪz/", "chỗ đỗ xe ven đường; vũng tránh tàu"),
    ("069444", "leguminosaes", "noun", "/ləˌɡjuːmɪˈnoʊsiːz/", "họ Đậu thực vật quả đậu giáp"),
    ("069445", "lhotses", "noun", "/ˈloʊtseɪz/", "đỉnh núi Lhotse ở dãy Himalaya"),
    ("069446", "liposarcomas", "noun", "/ˌlɪpoʊsɑːrˈkoʊməz/", "khối u ác tính mô mỡ"),
    ("069447", "macroevolutions", "noun", "/ˌmækroʊˌɛvəˈluːʃənz/", "tiến hóa lớn hình thành loài mới"),
    ("069448", "madias", "noun", "/ˈmeɪdiəz/", "cây cúc nhựa thơm chi Madia"),
    ("069449", "mbabanes", "noun", "/ˌɛmbɑːˈbɑːneɪz/", "thủ đô Mbabane của Eswatini"),
    ("069450", "mechanizes", "verb", "/ˈmɛkəˌnaɪzɪz/", "cơ giới hóa đưa máy móc vào"),
    ("069451", "micropenises", "noun", "/ˌmaɪkroʊˈpiːnɪsɪz/", "chứng dương vật nhỏ bẩm sinh"),
    ("069452", "momi", "noun", "/ˈmoʊmaɪ/", "thần châm biếm Momus Hy Lạp cổ"),
    ("069453", "momuses", "noun", "/ˈmoʊməsɪz/", "vị thần chế giễu châm biếm Momus"),
    ("069454", "monstrances", "noun", "/ˈmɒnstrənsɪz/", "hộp kính chầu Thánh Thể Công giáo"),
    ("069455", "moorhens", "noun", "/ˈmʊərˌhɛnz/", "chim trích cồ gà nước mỏ đỏ"),
    ("069456", "mycoses", "noun", "/maɪˈkoʊsiːz/", "bệnh nhiễm nấm ở người và vật"),
    ("069457", "najds", "noun", "/nædʒdz/", "vùng cao nguyên Najd Ả Rập Xê Út"),
    ("069458", "nephelines", "noun", "/ˈnɛfəˌliːnz/", "khoáng vật silicat nefelin núi lửa"),
    ("069459", "neuromarketings", "noun", "/ˌnjʊəroʊˈmɑːrkɪtɪŋz/", "tiếp thị thần kinh đo phản ứng não"),
    ("069460", "neurontins", "noun", "/njʊəˈrɒntɪnz/", "thuốc chống co giật đau thần kinh"),
    ("069461", "noctuidaes", "noun", "/nɒkˈtjuːɪdiːz/", "họ Ngài đêm bướm ăn đêm Noctuidae"),
    ("069462", "oestruses", "noun", "/ˈiːstrəsɪz/", "kỳ động dục của thú; ruồi trâu"),
    ("069463", "omentums", "noun", "/oʊˈmɛntəmz/", "màng mạc nối che phủ ruột ổ bụng"),
    ("069464", "onchocerciases", "noun", "/ˌɒŋkoʊsərˈkaɪəsiːz/", "bệnh giun chỉ mù sông châu Phi"),
    ("069465", "outvoted", "verb", "/ˌaʊtˈvoʊtɪd/", "đã thắng áp đảo bằng số phiếu bầu"),
    ("069466", "outvotes", "verb", "/ˌaʊtˈvoʊts/", "vượt hơn về số phiếu bầu quyết"),
    ("069467", "outvoting", "verb", "/ˌaʊtˈvoʊtɪŋ/", "đang thắng thế bằng lá phiếu bầu"),
    ("069468", "pavanes", "noun", "/pəˈvænz/", "điệu nhảy chậm trang trọng pavane"),
    ("069469", "phonograms", "noun", "/ˈfoʊnəˌɡræmz/", "ký hiệu chữ biểu âm; bản ghi âm"),
    ("069470", "pijs", "noun", "/ˌpiː aɪ ˈdʒeɪz/", "tổ chức Thánh chiến Hồi giáo PIJ"),
    ("069471", "pilei", "noun", "/ˈpaɪliaɪ/", "mũ nấm; mũ phớt La Mã; mây mũ chóp"),
    ("069472", "pileuses", "noun", "/ˈpaɪliəsɪz/", "mũ nấm mang bào tử; mũ cổ La Mã"),
    ("069473", "pleasantries", "noun", "/ˈplɛzəntriz/", "lời xã giao lịch sự bông đùa nhẹ"),
    ("069474", "pottles", "noun", "/ˈpɒtəlz/", "bình đo hai lít xưa; giỏ dâu nhỏ"),
    ("069475", "principalships", "noun", "/ˈprɪnsəpəlʃɪps/", "chức vụ hiệu trưởng nhà trường"),
    ("069476", "quartettes", "noun", "/kwɔːrˈtɛts/", "nhóm hòa tấu bốn nhạc công; bộ bốn"),
    ("069477", "querns", "noun", "/kwɜːrnz/", "cối đá xay ngũ cốc bằng tay cổ xưa"),
    ("069478", "renovators", "noun", "/ˈrɛnəˌveɪtərz/", "thợ cải tạo sửa chữa phục chế nhà"),
    ("069479", "ricinuses", "noun", "/ˈrɪsɪnəsɪz/", "cây thầu dầu thuộc chi Ricinus"),
    ("069480", "salals", "noun", "/səˈlælz/", "cây bụi quả mọng salal Bắc Mỹ"),
    ("069481", "salmis", "noun", "/ˈsælmiz/", "món thịt chim hầm rượu vang Pháp"),
    ("069482", "sandhis", "noun", "/ˈsændiz/", "hiện tượng biến âm tiếp giáp sandhi"),
    ("069483", "sardegnas", "noun", "/sɑːrˈdɛnjəz/", "đảo Sardegna thuộc nước Ý"),
    ("069484", "sassenaches", "noun", "/ˈsæsənæks/", "người Anh (cách gọi ở Scotland)"),
    ("069485", "schnorred", "verb", "/ʃnɔːrd/", "đã xin xỏ vòi vĩnh ăn bám (lóng)"),
    ("069486", "schnorring", "verb", "/ˈʃnɔːrɪŋ/", "đang xin xỏ ăn bám vòi vĩnh (lóng)"),
    ("069487", "schnorrs", "verb", "/ʃnɔːrz/", "xin xỏ ăn bám vòi vĩnh (lóng)"),
    ("069488", "scutes", "noun", "/skjuːts/", "tấm vảy sừng mai rùa hoặc da cá sấu"),
    ("069489", "snowsuits", "noun", "/ˈsnoʊˌsuːts/", "bộ quần áo ấm chống thấm đi tuyết"),
    ("069490", "sonatinas", "noun", "/ˌsɒnəˈtiːnəz/", "bản xônát ngắn dễ chơi sonatina"),
    ("069491", "spellbinders", "noun", "/ˈspɛlˌbaɪndərz/", "diễn giả nói cuốn hút mê hoặc người"),
    ("069492", "squashier", "adj", "/ˈskwɒʃiər/", "mềm nhũn bở dễ bóp nát hơn"),
    ("069493", "squashiest", "adj", "/ˈskwɒʃiɪst/", "mềm nhũn bở dễ bóp nát nhất"),
    ("069494", "tailcoats", "noun", "/ˈteɪlˌkoʊts/", "áo khoác lễ đuôi tôm trang trọng"),
    ("069495", "temucos", "noun", "/tɛˈmuːkoʊz/", "thành phố Temuco ở miền nam Chile"),
    ("069496", "tenniels", "noun", "/ˈtɛniəlz/", "họa sĩ minh họa Anh John Tenniel"),
    ("069497", "tiddlers", "noun", "/ˈtɪdlərz/", "cá nhỏ; em bé nhỏ xíu (khẩu ngữ)"),
    ("069498", "tillandsias", "noun", "/tɪˈlændziəz/", "cây không khí dứa chi Tillandsia"),
    ("069499", "towboats", "noun", "/ˈtoʊˌboʊts/", "tàu kéo đẩy sà lan trên sông biển"),
    ("069500", "trichomoniases", "noun", "/ˌtrɪkoʊməˈnaɪəsiːz/", "bệnh nhiễm trùng roi trichomonas"),
    ("069501", "twirlers", "noun", "/ˈtwɜːrlərz/", "người xoay gậy diễu hành; cầu thủ"),
    ("069502", "unchaster", "adj", "/ʌnˈtʃeɪstər/", "không trong trắng tiết hạnh hơn"),
]

with open("scratch/b34_r09_raw_p5.json") as f:
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

with open("scratch/b34_r09_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r09_p5.json OK")
