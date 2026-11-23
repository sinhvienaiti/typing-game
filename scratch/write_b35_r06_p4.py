import json

items = [
    ("072803", "sothises", "noun", "/ˈsoʊθɪsɪz/", "sao Thiên Lang (tên Ai Cập cổ)"),
    ("072804", "soundboxes", "noun", "/ˈsaʊndˌbɒksɪz/", "hộp cộng hưởng âm thanh đàn"),
    ("072805", "squamatas", "noun", "/skwəˈmeɪtəz/", "bộ Có vảy (thằn lằn, rắn)"),
    ("072806", "stalinizations", "noun", "/ˌstɑːlɪnaɪˈzeɪʃənz/", "quá trình Stalin hóa chế độ"),
    ("072807", "sucrases", "noun", "/ˈsuːkreɪsɪz/", "enzym phân giải đường sucrase"),
    ("072808", "suers", "noun", "/ˈsuːərz/", "người khởi kiện ra tòa án"),
    ("072809", "sunlamps", "noun", "/ˈsʌnˌlæmps/", "đèn chiếu tia cực tím làm rám da"),
    ("072810", "teleosteis", "noun", "/ˌtɛliˈɒstiˌaɪ/", "nhóm Cá xương thật sự (Teleostei)"),
    ("072811", "tornillos", "noun", "/tɔːrˈniːjoʊz/", "cây đậu xoắn ốc Prosopis vùng khô"),
    ("072812", "tortuosities", "noun", "/ˌtɔːrtʃuˈɒsɪtiz/", "độ ngoằn ngoèo uốn khúc quanh co"),
    ("072813", "troches", "noun", "/ˈtroʊkiz/", "viên ngậm tan chậm trong miệng"),
    ("072814", "vengefulnesses", "noun", "/ˈvɛndʒfʊlnəsɪz/", "lòng thù hận dai dẳng; tính trả thù"),
    ("072815", "verdins", "noun", "/ˈvɜːrdɪnz/", "chim bạc má đầu vàng Bắc Mỹ"),
    ("072816", "viroids", "noun", "/ˈvaɪrɔɪdz/", "viroid (phân tử ARN gây bệnh cây)"),
    ("072817", "visualisers", "noun", "/ˈvɪʒuəˌlaɪzərz/", "phần mềm đồ họa; người trực quan"),
    ("072818", "votaries", "noun", "/ˈvoʊtəriz/", "tín đồ trung thành; người tôn sùng"),
    ("072819", "wahabisms", "noun", "/wəˈhɑːˌbɪzəmz/", "chủ nghĩa Hồi giáo Wahhabi"),
    ("072820", "wolframites", "noun", "/ˈwʊlfrəˌmaɪts/", "quặng vonfram sắt mangan wolframit"),
    ("072821", "wurtzites", "noun", "/ˈwɜːrtsaɪts/", "khoáng vật kẽm sunfua wurtzit"),
    ("072822", "yellowbirds", "noun", "/ˈjɛloʊˌbɜːrdz/", "chim chích vàng hoặc sẻ vàng"),
    ("072823", "abstractionists", "noun", "/æbˈstrækʃənɪsts/", "họa sĩ theo trường phái trừu tượng"),
    ("072824", "acrosomes", "noun", "/ˈækrəˌsoʊmz/", "thể đỉnh chóp đầu tinh trùng"),
    ("072825", "actinolites", "noun", "/ækˈtɪnəˌlaɪts/", "khoáng vật silicat xanh actinolit"),
    ("072826", "agraphias", "noun", "/eɪˈɡræfiəz/", "chứng mất khả năng viết (thần kinh)"),
    ("072827", "altocumuli", "noun", "/ˌæltoʊˈkjuːmjʊˌlaɪ/", "mây trung tích tầng cao vừa"),
    ("072828", "angelologies", "noun", "/ˌeɪndʒəˈlɒlədʒiz/", "thần học nghiên cứu về thiên thần"),
    ("072829", "anhingas", "noun", "/ænˈhɪŋɡəz/", "chim cổ rắn bơi lặn săn cá"),
    ("072830", "annalists", "noun", "/ˈænəlɪsts/", "nhà biên niên sử ghi chép lịch sử"),
    ("072831", "anomalas", "noun", "/əˈnɒmələz/", "chi Bọ cánh cứng hại lá Anomala"),
    ("072832", "antitussives", "noun", "/ˌæntɪˈtʌsɪvz/", "thuốc ức chế phản xạ giảm ho"),
    ("072833", "apiums", "noun", "/ˈeɪpiəmz/", "chi Cần tây thực vật (Apium)"),
    ("072834", "arboviruses", "noun", "/ˈɑːrboʊˌvaɪrəsɪz/", "vi-rút lây truyền qua muỗi ve"),
    ("072835", "audiocassettes", "noun", "/ˌɔːdioʊkəˈsɛts/", "băng từ cassette thu âm thanh"),
    ("072836", "bearberries", "noun", "/ˈbɛərˌbɛriz/", "cây quả mọng gấu (thảo dược)"),
    ("072837", "bellbirds", "noun", "/ˈbɛlˌbɜːrdz/", "chim chuông kêu vang như chuông"),
    ("072838", "billhooks", "noun", "/ˈbɪlˌhʊks/", "dao quắm lưỡi cong phát quang cây"),
    ("072839", "blackflies", "noun", "/ˈblækˌflaɪz/", "ruồi đen nhỏ hút máu; rệp đen đậu"),
    ("072840", "blacksnakes", "noun", "/ˈblækˌsneɪks/", "rắn đen (rắn chuột đen, rắn độc Úc)"),
    ("072841", "bluffers", "noun", "/ˈblʌfərz/", "kẻ hay hù dọa ra vẻ đánh lừa"),
    ("072842", "brantas", "noun", "/ˈbræntəz/", "chi Ngỗng trời biển (Branta)"),
    ("072843", "bronchoscopes", "noun", "/ˈbrɒŋkəˌskoʊps/", "ống nội soi khí quản phế quản"),
    ("072844", "cactaceaes", "noun", "/kækˈteɪʃiˌiːz/", "họ Xương rồng mọng nước có gai"),
    ("072845", "calamagrostises", "noun", "/ˌkæləməˈɡrɒstɪsɪz/", "chi Cỏ lau sậy sườn Calamagrostis"),
    ("072846", "carbonadoes", "noun", "/ˌkɑːrbəˈneɪdoʊz/", "kim cương đen; thịt khía nướng vỉ"),
    ("072847", "carbonados", "noun", "/ˌkɑːrbəˈneɪdoʊz/", "kim cương đen; thịt khía nướng vỉ"),
    ("072848", "cerumens", "noun", "/sɪˈruːmənz/", "ráy tai tiết ra trong ống tai"),
    ("072849", "chapatties", "noun", "/tʃəˈpɑːtiz/", "bánh mì dẹt Ấn Độ chapati"),
    ("072850", "chapattis", "noun", "/tʃəˈpɑːtiz/", "bánh mì dẹt Ấn Độ chapati"),
    ("072851", "chlorophytas", "noun", "/ˌklɔːrəˈfaɪtəz/", "ngành Tảo lục (Chlorophyta)"),
    ("072852", "chordates", "noun", "/ˈkɔːrdeɪts/", "động vật thuộc ngành Dây sống"),
    ("072853", "coastlands", "noun", "/ˈkoʊstˌlændz/", "vùng đất duyên hải ven biển"),
    ("072854", "cockups", "noun", "/ˈkɒkˌʌps/", "sự cố hỏng bét sai sót (lóng Anh)"),
    ("072855", "compartmentalises", "verb", "/kəmˌpɑːrtˈmɛntəlaɪzɪz/", "phân chia rạch ròi thành ngăn (Anh)"),
    ("072856", "compartmentalising", "verb", "/kəmˌpɑːrtˈmɛntəlaɪzɪŋ/", "đang phân chia rạch ròi thành ngăn"),
    ("072857", "copulatives", "noun", "/ˈkɒpjʊlətɪvz/", "từ nối (ngôn ngữ); động từ liên kết"),
    ("072858", "couvades", "noun", "/kuːˈvɑːdz/", "tục người chồng nằm ổ giả sinh con"),
    ("072859", "cukes", "noun", "/kjuːks/", "quả dưa chuột (cách gọi tắt Mỹ)"),
    ("072860", "cyclicities", "noun", "/ˌsɪkˈlɪsɪtiz/", "tính tuần hoàn lặp lại theo chu kỳ"),
    ("072861", "dtics", "noun", "/ˈdiːtɪks/", "Trung tâm Thông tin Kỹ thuật DTIC"),
    ("072862", "dunnocks", "noun", "/ˈdʌnəks/", "chim sẻ bờ rào dunnock châu Âu"),
    ("072863", "ephemeropteras", "noun", "/ɪˌfɛməˈrɒptərəz/", "bộ Phù du sống ngắn ngày"),
    ("072864", "eridanuses", "noun", "/ɪˈrɪdənəsɪz/", "chòm sao Ba Giang phương Nam"),
    ("072865", "eryngiums", "noun", "/ɪˈrɪndʒiəmz/", "chi Cây ngò gai biển Eryngium"),
    ("072866", "espadrilles", "noun", "/ˌɛspəˈdrɪlz/", "giày đế cói đay vải bạt nhẹ"),
    ("072867", "exabytes", "noun", "/ˈɛksəˌbaɪts/", "đơn vị dữ liệu exabyte (10^18 byte)"),
    ("072868", "fenestellae", "noun", "/ˌfɛnɪˈstɛliː/", "hốc tường thờ; cửa sổ nhỏ nhà thờ"),
    ("072869", "fenestellas", "noun", "/ˌfɛnɪˈstɛləz/", "hốc tường nhỏ; cửa sổ nhỏ nhà thờ"),
    ("072870", "fibrocartilages", "noun", "/ˌfaɪbroʊˈkɑːrtɪlɪdʒɪz/", "mô sụn xơ bền chắc (đĩa đệm)"),
    ("072871", "freebees", "noun", "/ˈfriːbiz/", "món quà hoặc vé miễn phí (biến thể)"),
    ("072872", "gloxinias", "noun", "/ɡlɒkˈsɪniəz/", "cây hoa chuông tử la lan Gloxinia"),
    ("072873", "goniometers", "noun", "/ˌɡoʊniˈɒmɪtərz/", "giác kế đo góc tinh thể hoặc khớp"),
    ("072874", "gooneys", "noun", "/ˈɡuːniz/", "chim hải âu lớn; kẻ ngốc khờ dại"),
    ("072875", "gunflints", "noun", "/ˈɡʌnˌflɪnts/", "viên đá lửa đánh lửa súng kíp xưa"),
    ("072876", "hatemongers", "noun", "/ˈheɪtˌmʌŋɡərz/", "kẻ kích động gieo rắc hận thù"),
    ("072877", "heliopauses", "noun", "/ˈhiːlioʊˌpɔːzɪz/", "nhật dừng (ranh giới nhật quyển)"),
    ("072878", "illinoisans", "noun", "/ˌɪlɪˈnɔɪənz/", "người dân bang Illinois của Mỹ"),
    ("072879", "impartations", "noun", "/ˌɪmpɑːrˈteɪʃənz/", "sự truyền đạt chia sẻ tri thức"),
    ("072880", "incrustations", "noun", "/ˌɪnkrʌˈsteɪʃənz/", "lớp vỏ cặn cứng bám; sự khảm đá"),
    ("072881", "indinavirs", "noun", "/ɪnˈdɪnəvɪərz/", "thuốc kháng HIV indinavir"),
    ("072882", "indurations", "noun", "/ˌɪndjʊˈreɪʃənz/", "sự xơ cứng mô; nốt sần cứng (y học)"),
    ("072883", "jugoslavs", "noun", "/ˈjuːɡoʊˌslɑːvz/", "người dân Nam Tư (biến thể cũ)"),
    ("072884", "kenafs", "noun", "/kɛˈnɑːfs/", "cây đay gai kenaf lấy sợi"),
    ("072885", "kirtles", "noun", "/ˈkɜːrtəlz/", "áo dài hoặc váy lót thời Trung cổ"),
    ("072886", "lipoids", "noun", "/ˈlɪpɔɪdz/", "chất giống chất béo (lipoid)"),
    ("072887", "locustas", "noun", "/loʊˈkʌstəz/", "chi Châu chấu di cư (Locusta)"),
    ("072888", "lovesicknesses", "noun", "/ˈlʌvˌsɪknəsɪz/", "nỗi tương tư sầu muộn vì yêu"),
    ("072889", "lummoxes", "noun", "/ˈlʌməksɪz/", "gã to xác vụng về thô kệch"),
    ("072890", "lyguses", "noun", "/ˈlaɪɡəsɪz/", "bọ xít hại cây chi Lygus"),
    ("072891", "mandolas", "noun", "/mænˈdoʊləz/", "đàn dây măng-đô-la cỡ lớn"),
    ("072892", "markhors", "noun", "/ˈmɑːrkɔːrz/", "dê rừng sừng xoắn markhor châu Á"),
    ("072893", "mbeyas", "noun", "/əmˈbeɪəz/", "thành phố Mbeya ở Tanzania"),
    ("072894", "mercaptopurines", "noun", "/ˌmɜːrkæptoʊˈpjʊəriːnz/", "thuốc ức chế miễn dịch 6-MP"),
    ("072895", "mercurochromes", "noun", "/mɜːrˈkjʊərəˌkroʊmz/", "thuốc sát trùng đỏ mercurochrome"),
    ("072896", "milksops", "noun", "/ˈmɪlkˌsɒps/", "kẻ yếu đuối nhát gan thiếu bản lĩnh"),
    ("072897", "moharrams", "noun", "/moʊˈhærəmz/", "tháng Muharram đầu năm Hồi giáo"),
    ("072898", "moonlighters", "noun", "/ˈmuːnˌlaɪtərz/", "người làm thêm nghề phụ ban đêm"),
    ("072899", "mosquitofishes", "noun", "/məˈskiːtoʊˌfɪʃɪz/", "cá ăn bọ gậy muỗi Gambusia"),
    ("072900", "nalchiks", "noun", "/ˈnɑːltʃɪks/", "thành phố Nalchik ở vùng Caucasus"),
    ("072901", "nucleoplasms", "noun", "/ˈnjuːklioʊˌplæzəmz/", "chất nhân tế bào (nhân tương)"),
    ("072902", "ontogeneses", "noun", "/ˌɒntəˈdʒɛnɪsiːz/", "quá trình phát sinh cá thể sinh vật"),
]

with open("scratch/b35_r06_raw_p4.json") as f:
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

with open("scratch/b35_r06_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r06_p4.json OK")
