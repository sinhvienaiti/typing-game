import json

items = [
    ("069603", "prejudgments", "noun", "/ˌpriːˈdʒʌdʒmənts/", "sự phán xét vội vã thiếu chứng cứ"),
    ("069604", "primatologies", "noun", "/ˌpraɪməˈtɒlədʒiz/", "ngành linh trưởng học nghiên cứu"),
    ("069605", "quirts", "noun", "/kwɜːrts/", "roi da ngắn tết cán cho người cưỡi"),
    ("069606", "quizmasters", "noun", "/ˈkwɪzˌmɑːstərz/", "người dẫn đặt câu hỏi trò đố vui"),
    ("069607", "rhizobiums", "noun", "/raɪˈzoʊbiəmz/", "vi khuẩn cố định đạm nốt sần rễ"),
    ("069608", "rudbeckias", "noun", "/rʌdˈbɛkiəz/", "hoa cúc nón vàng đen Rudbeckia"),
    ("069609", "sailplanes", "noun", "/ˈseɪlˌpleɪnz/", "tàu lượn không động cơ bay nhờ gió"),
    ("069610", "settlors", "noun", "/ˈsɛtlərz/", "người lập quỹ tín thác tài sản"),
    ("069611", "shadowboxed", "verb", "/ˈʃædoʊˌbɒkst/", "đã tập đấm gió luyện quyền anh"),
    ("069612", "shadowboxes", "verb", "/ˈʃædoʊˌbɒksɪz/", "tập đấm gió đối kháng tưởng tượng"),
    ("069613", "shahns", "noun", "/ʃɑːnz/", "họa sĩ hiện thực Mỹ Ben Shahn"),
    ("069614", "spiraeas", "noun", "/spaɪˈriːəz/", "cây bụi hoa mơ trắng chi Spiraea"),
    ("069615", "sporangiums", "noun", "/spəˈrændʒiəmz/", "túi bào tử sinh bào tử ở thực vật"),
    ("069616", "stabroeks", "noun", "/ˈstɑːbrʊks/", "thành phố Stabroek (tên cũ Guyana)"),
    ("069617", "staffas", "noun", "/ˈstæfəz/", "đảo đá bazan Staffa ở Scotland"),
    ("069618", "streetwalkers", "noun", "/ˈstriːtˌwɔːkərz/", "gái bán dâm đứng đường (từ cũ)"),
    ("069619", "tannenbergs", "noun", "/ˈtænənˌbɜːrɡz/", "trận đánh Tannenberg lịch sử"),
    ("069620", "tantalites", "noun", "/ˈtæntəˌlaɪts/", "quặng khoáng vật chứa tantan"),
    ("069621", "tarsiers", "noun", "/ˈtɑːrsiərz/", "vượn lùn mắt to khổng lồ Đông Nam Á"),
    ("069622", "terases", "noun", "/ˈtɛrəsɪz/", "thai dị dạng bẩm sinh nghiêm trọng"),
    ("069623", "terata", "noun", "/ˈtɛrətə/", "dị thai biến dạng bẩm sinh (y học)"),
    ("069624", "tightwads", "noun", "/ˈtaɪtˌwɒdz/", "người keo kiệt bủn xỉn từng đồng"),
    ("069625", "tilefishes", "noun", "/ˈtaɪlˌfɪʃɪz/", "cá đầu vuông biển sâu tilefish"),
    ("069626", "tmvs", "noun", "/ˌtiː ɛm ˈviːz/", "vi rút khảm lá thuốc lá TMV"),
    ("069627", "tricorns", "noun", "/ˈtraɪˌkɔːrnz/", "mũ vành gập ba góc thế kỷ 18"),
    ("069628", "tuataras", "noun", "/ˌtuːəˈtɑːrəz/", "bò sát cổ đại tuatara New Zealand"),
    ("069629", "tulus", "noun", "/ˈtuːluːz/", "người và tiếng Tulu miền nam Ấn"),
    ("069630", "urokinases", "noun", "/ˌjʊəroʊˈkaɪneɪsɪz/", "enzym làm tan cục máu đông"),
    ("069631", "vaquitas", "noun", "/vəˈkiːtəz/", "cá heo vaquita Mexico rất hiếm"),
    ("069632", "winepresses", "noun", "/ˈwaɪnˌprɛsɪz/", "máy ép nước nho tươi làm rượu vang"),
    ("069633", "advertizings", "noun", "/ˈædvərˌtaɪzɪŋz/", "hoạt động quảng cáo (biến thể Mỹ)"),
    ("069634", "antinomianisms", "noun", "/ˌæntɪˈnoʊmiənˌɪzəmz/", "thuyết bài luật đạo đức thần học"),
    ("069635", "armamentaria", "noun", "/ˌɑːrməmɛnˈtɛəriə/", "kho thuốc và trang thiết bị y tế"),
    ("069636", "armamentariums", "noun", "/ˌɑːrməmɛnˈtɛəriəmz/", "toàn bộ trang thiết bị thuốc y khoa"),
    ("069637", "asthenias", "noun", "/æsˈθiːniəz/", "chứng suy nhược mất sức cơ thể"),
    ("069638", "atopies", "noun", "/ˈætəpiz/", "cơ địa dị ứng di truyền (y học)"),
    ("069639", "audiograms", "noun", "/ˈɔːdioʊˌɡræmz/", "biểu đồ thính lực đo độ nghe"),
    ("069640", "babinskis", "noun", "/bəˈbɪnskiz/", "nhà thần kinh học Joseph Babinski"),
    ("069641", "balkiest", "adj", "/ˈbɔːlkiɪst/", "bướng bỉnh khó bảo cứng đầu nhất"),
    ("069642", "bargellos", "noun", "/bɑːrˈdʒɛloʊz/", "kiểu thêu mũi chữ thập dích dắc"),
    ("069643", "bayats", "noun", "/baɪˈɑːts/", "lời thề trung thành bay'ah Hồi giáo"),
    ("069644", "bennes", "noun", "/ˈbɛniz/", "cây mè vừng trồng lấy hạt ép dầu"),
    ("069645", "birdwatched", "verb", "/ˈbɜːrdˌwɒtʃt/", "đã đi quan sát chim hoang dã"),
    ("069646", "birdwatches", "verb", "/ˈbɜːrdˌwɒtʃɪz/", "quan sát theo dõi chim tự nhiên"),
    ("069647", "birdwatching", "verb", "/ˈbɜːrdˌwɒtʃɪŋ/", "đang quan sát ngắm chim tự nhiên"),
    ("069648", "bises", "noun", "/biːz/", "gió bắc lạnh khô bise dãy Alps"),
    ("069649", "bunuels", "noun", "/buːnˈjwɛlz/", "đạo diễn siêu thực Luis Buñuel"),
    ("069650", "bydgoszczes", "noun", "/bɪdˈɡɒʃtʃɪz/", "thành phố Bydgoszcz ở Ba Lan"),
    ("069651", "cavies", "noun", "/ˈkeɪviz/", "chuột lang nuôi cảnh Nam Mỹ"),
    ("069652", "chandleries", "noun", "/ˈtʃɑːndləriz/", "cửa hàng vật tư tàu; xưởng nến"),
    ("069653", "cheeseboards", "noun", "/ˈtʃiːzˌbɔːrdz/", "thớt gỗ hoặc khay dọn phô mai"),
    ("069654", "chitlinses", "noun", "/ˈtʃɪtlɪnzɪz/", "món lòng non lợn chiên hầm Mỹ"),
    ("069655", "choughs", "noun", "/tʃʌfs/", "chim quạ núi mỏ đỏ chân đỏ"),
    ("069656", "chromatids", "noun", "/ˈkroʊmətɪdz/", "nhiễm sắc tử tách đôi nguyên phân"),
    ("069657", "chromospheres", "noun", "/ˈkroʊməˌsfɪərz/", "lớp sắc cầu khí quyển Mặt Trời"),
    ("069658", "clostridias", "noun", "/klɒˈstrɪdiəz/", "vi khuẩn kỵ khí chi Clostridium"),
    ("069659", "colorized", "verb", "/ˈkʌləˌraɪzd/", "đã lên màu cho phim ảnh trắng đen"),
    ("069660", "colorizes", "verb", "/ˈkʌləˌraɪzɪz/", "tô màu kỹ thuật số phim trắng đen"),
    ("069661", "colorizing", "verb", "/ˈkʌləˌraɪzɪŋ/", "đang lên màu cho ảnh phim cũ"),
    ("069662", "coneflowers", "noun", "/ˈkoʊnˌflaʊərz/", "hoa cúc nón đồng cỏ Rudbeckia"),
    ("069663", "croakier", "adj", "/ˈkroʊkiər/", "khàn đặc ồm ồm hơn"),
    ("069664", "croakiest", "adj", "/ˈkroʊkiɪst/", "khàn đặc ồm ồm nhất"),
    ("069665", "curculionidaes", "noun", "/kɜːrˌkjuːliˈɒnɪdiːz/", "họ bọ cánh cứng vòi voi; họ mọt"),
    ("069666", "cypripediums", "noun", "/ˌsɪprɪˈpiːdiəmz/", "hoa lan hài thuộc chi Cypripedium"),
    ("069667", "drabas", "noun", "/ˈdrɑːbəz/", "cây cỏ cải nhỏ thuộc chi Draba"),
    ("069668", "dumpsites", "noun", "/ˈdʌmpˌsaɪts/", "bãi đổ chôn lấp rác thải phế liệu"),
    ("069669", "egocentrisms", "noun", "/ˌiːɡoʊˈsɛntrɪzəmz/", "tính vị kỷ lấy mình làm trung tâm"),
    ("069670", "epiphyses", "noun", "/ɪˈpɪfɪsiːz/", "đầu xương dài; tuyến tùng não bộ"),
    ("069671", "eponyms", "noun", "/ˈɛpəˌnɪmz/", "tên riêng dùng đặt cho vật hay nơi"),
    ("069672", "eradicators", "noun", "/ɪˈrædɪˌkeɪtərz/", "người hoặc chất tẩy trừ tận gốc"),
    ("069673", "erewhons", "noun", "/ˈɛrɪwɒnz/", "tiểu thuyết trào phúng Erewhon"),
    ("069674", "esfahans", "noun", "/ˌɛsfəˈhɑːnz/", "thành phố cổ Esfahan của Iran"),
    ("069675", "excoriations", "noun", "/ɛkˌskɔːriˈeɪʃənz/", "vết trầy sây sát da; chỉ trích gắt"),
    ("069676", "ezos", "noun", "/ˈɛzoʊz/", "tên cổ của đảo Hokkaido Nhật Bản"),
    ("069677", "fanlights", "noun", "/ˈfænˌlaɪts/", "ô cửa kính hình bán nguyệt trên cửa"),
    ("069678", "forenames", "noun", "/ˈfɔːrˌneɪmz/", "tên riêng đứng trước họ (Anh)"),
    ("069679", "fornicators", "noun", "/ˈfɔːrnɪˌkeɪtərz/", "người quan hệ ngoài hôn nhân (cũ)"),
    ("069680", "fripperies", "noun", "/ˈfrɪpəriz/", "đồ trang sức hào nhoáng rườm rà"),
    ("069681", "fucuses", "noun", "/ˈfjuːkəsɪz/", "tảo bẹ nâu ven biển chi Fucus"),
    ("069682", "gastrostomies", "noun", "/ɡæˈstrɒstəmiz/", "phẫu thuật mở thông dạ dày nuôi ăn"),
    ("069683", "gellies", "noun", "/ˈdʒɛliz/", "thuốc nổ dẻo gelignit (tiếng lóng)"),
    ("069684", "guarneris", "noun", "/ɡwɑːrˈnɛriz/", "nghệ nhân làm đàn vĩ cầm Guarneri"),
    ("069685", "gunites", "noun", "/ˈɡʌnaɪts/", "vữa bê tông phun áp lực gia cố"),
    ("069686", "haems", "noun", "/hiːmz/", "nhóm nhân sắt heme trong hemoglobin"),
    ("069687", "hardpans", "noun", "/ˈhɑːrdˌpænz/", "tầng đất cứng chặt không thấm nước"),
    ("069688", "hawkshaws", "noun", "/ˈhɔːkˌʃɔːz/", "thám tử điều tra tài ba (lóng Mỹ)"),
    ("069689", "hemophiliacs", "noun", "/ˌhiːməˈfɪliæks/", "người mắc bệnh máu khó đông"),
    ("069690", "histiocytoses", "noun", "/ˌhɪstioʊsaɪˈtoʊsiːz/", "bệnh tăng sinh bất thường mô bào"),
    ("069691", "inhumations", "noun", "/ˌɪnhjʊˈmeɪʃənz/", "nghi thức chôn cất mai táng người"),
    ("069692", "interrogatories", "noun", "/ˌɪntəˈrɒɡətəriz/", "bảng câu hỏi thẩm vấn văn bản luật"),
    ("069693", "ioways", "noun", "/ˈaɪəweɪz/", "bộ tộc bản địa Iowa trung tây Mỹ"),
    ("069694", "irruptions", "noun", "/ɪˈrʌpʃənz/", "cuộc xâm nhập ồ ạt bất ngờ"),
    ("069695", "jansenists", "noun", "/ˈdʒænsənɪsts/", "tín đồ giáo phái Jansen thế kỷ 17"),
    ("069696", "kanangas", "noun", "/kəˈnɑːŋɡəz/", "thành phố Kananga ở CHDC Congo"),
    ("069697", "klaviers", "noun", "/klɑːˈvɪərz/", "nhạc cụ bàn phím cổ điển Đức"),
    ("069698", "kwangtungs", "noun", "/kwɑːŋˈtʊŋz/", "tỉnh Quảng Đông ở Trung Quốc"),
    ("069699", "leatherworks", "noun", "/ˈlɛðərˌwɜːrks/", "xưởng đồ da; sản phẩm làm từ da"),
    ("069700", "loosestrifes", "noun", "/ˈluːsˌstraɪfs/", "cây trân châu vàng; thiên khuê thảo"),
    ("069701", "lovastatins", "noun", "/ˌloʊvəˈstætɪnz/", "thuốc hạ mỡ máu cholesterol"),
    ("069702", "lundas", "noun", "/ˈlʌndəz/", "chim hải âu cổ rụt chi Lunda"),
]

with open("scratch/b34_r10_raw_p2.json") as f:
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

with open("scratch/b34_r10_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r10_p2.json OK")
