import json

items = [
    ("067803", "baboos", "noun", "/ˈbɑːbuːz/", "thầy ký Ấn Độ baboo (cách gọi cũ)"),
    ("067804", "basilicatas", "noun", "/bəˌzɪlɪˈkɑːtəz/", "vùng Basilicata ở miền nam Ý"),
    ("067805", "benthoses", "noun", "/ˈbɛnθoʊzɪz/", "hệ sinh vật vùng đáy biển sâu"),
    ("067806", "benzocaines", "noun", "/ˈbɛnzoʊˌkeɪnz/", "thuốc gây tê tại chỗ benzocain"),
    ("067807", "bobolinks", "noun", "/ˈbɒbəˌlɪŋks/", "chim sáo đồng cỏ bobolink Bắc Mỹ"),
    ("067808", "bombuses", "noun", "/ˈbɒmbəsɪz/", "ong vò vẽ bông thuộc chi Bombus"),
    ("067809", "brancusis", "noun", "/brɑːnˈkuːsiz/", "nhà điêu khắc Romania Brâncuși"),
    ("067810", "calcinations", "noun", "/ˌkælsɪˈneɪʃənz/", "quá trình nung vôi hóa ở nhiệt cao"),
    ("067811", "candlewicks", "noun", "/ˈkændəlˌwɪks/", "sợi bấc nến; vải thêu nổi hạt"),
    ("067812", "canettis", "noun", "/kəˈnɛtiz/", "nhà văn Nobel Elias Canetti"),
    ("067813", "capeks", "noun", "/ˈtʃɑːpɛks/", "nhà văn Séc Karel Čapek"),
    ("067814", "capitations", "noun", "/ˌkæpɪˈteɪʃənz/", "thuế đinh; thuế tính theo đầu người"),
    ("067815", "celebrexes", "noun", "/ˈsɛləˌbrɛksɪz/", "thuốc giảm đau chống viêm Celebrex"),
    ("067816", "cervuses", "noun", "/ˈsɜːrvəsɪz/", "hươu đỏ thuộc chi Cervus"),
    ("067817", "chignons", "noun", "/ˈʃiːnjɒnz/", "búi tóc cuộn gọn sau gáy phụ nữ"),
    ("067818", "christianized", "verb", "/ˈkrɪstʃəˌnaɪzd/", "đã truyền bá cải đạo Cơ đốc giáo"),
    ("067819", "christianizes", "verb", "/ˈkrɪstʃəˌnaɪzɪz/", "Cơ đốc hóa; cải sang Cơ đốc giáo"),
    ("067820", "christianizing", "verb", "/ˈkrɪstʃəˌnaɪzɪŋ/", "đang truyền đạo Cơ đốc hóa"),
    ("067821", "chuffing", "verb", "/ˈtʃʌfɪŋ/", "đang phì hơi như đầu máy tàu hỏa"),
    ("067822", "chuffs", "verb", "/tʃʌfs/", "phì hơi mạnh như động cơ hơi nước"),
    ("067823", "collimations", "noun", "/ˌkɒlɪˈmeɪʃənz/", "sự chuẩn trực căn chỉnh tia sáng"),
    ("067824", "countrywomen", "noun", "/ˈkʌntriˌwɪmɪn/", "phụ nữ nông thôn; nữ đồng hương"),
    ("067825", "couperins", "noun", "/ˌkuːpəˈrænz/", "nhà soạn nhạc Pháp F. Couperin"),
    ("067826", "crimpers", "noun", "/ˈkrɪmpərz/", "máy dập uốn tóc; kìm bấm đầu dây"),
    ("067827", "crosiers", "noun", "/ˈkroʊʒərz/", "gậy mục tử đầu cong của giám mục"),
    ("067828", "cruets", "noun", "/ˈkruːɪts/", "lọ nhỏ đựng giấm dầu ăn trên bàn"),
    ("067829", "cycloids", "noun", "/ˈsaɪklɔɪdz/", "đường cong xycloit bánh xe lăn"),
    ("067830", "dacoits", "noun", "/dəˈkɔɪts/", "kẻ cướp có vũ trang ở Ấn Độ"),
    ("067831", "diazoes", "noun", "/daɪˈeɪzoʊz/", "hợp chất hữu cơ chứa nhóm diazo"),
    ("067832", "dishcloths", "noun", "/ˈdɪʃˌklɒθs/", "khăn lau rửa chén bát nhà bếp"),
    ("067833", "duralumins", "noun", "/djʊˈræljʊmɪnz/", "hợp kim nhôm bền nhẹ duralumin"),
    ("067834", "duses", "noun", "/ˈduːzeɪz/", "nữ diễn viên kịch Ý Eleonora Duse"),
    ("067835", "dustmen", "noun", "/ˈdʌstmən/", "công nhân thu gom rác thải (Anh)"),
    ("067836", "dybbukkim", "noun", "/dɪˈbʊkiːm/", "linh hồn nhập xác dybbuk Do Thái"),
    ("067837", "dybbuks", "noun", "/ˈdɪbʊks/", "ma ám nhập thể trong truyện Do Thái"),
    ("067838", "eurocentrisms", "noun", "/ˌjʊəroʊˈsɛntrɪzəmz/", "tư tưởng lấy châu Âu làm trung tâm"),
    ("067839", "fedayeens", "noun", "/ˌfɛdaɪˈiːnz/", "chiến binh du kích cảm tử Ả Rập"),
    ("067840", "fellahs", "noun", "/ˈfɛləz/", "nông dân lao động vùng Ai Cập"),
    ("067841", "flatworms", "noun", "/ˈflætˌwɜːrmz/", "giun dẹp thân mảnh như sán dây"),
    ("067842", "fujiyamas", "noun", "/ˌfuːdʒiˈjɑːməz/", "núi lửa biểu tượng Phú Sĩ Nhật Bản"),
    ("067843", "gristmills", "noun", "/ˈɡrɪstˌmɪlz/", "nhà máy hoặc cối xay ngũ cốc bột"),
    ("067844", "groundcovers", "noun", "/ˈɡraʊndˌkʌvərz/", "cây thảm bò che phủ mặt đất"),
    ("067845", "hagfishes", "noun", "/ˈhæɡˌfɪʃɪz/", "cá mút đá myxin không hàm đáy biển"),
    ("067846", "hairnets", "noun", "/ˈhɛərˌnɛts/", "lưới mảnh trùm giữ gọn búi tóc"),
    ("067847", "hitchingses", "noun", "/ˈhɪtʃɪŋzɪz/", "nhà dược học Nobel G. Hitchings"),
    ("067848", "impostures", "noun", "/ɪmˈpɒstʃərz/", "hành vi mạo danh lừa đảo tinh vi"),
    ("067849", "insurgences", "noun", "/ɪnˈsɜːrdʒənsɪz/", "cuộc nổi dậy vũ trang chống đối"),
    ("067850", "intubated", "verb", "/ˈɪntjʊˌbeɪtɪd/", "đã đặt ống nội khí quản cấp cứu"),
    ("067851", "intubates", "verb", "/ˈɪntjʊˌbeɪts/", "đặt ống thông vào khí quản y khoa"),
    ("067852", "intubating", "verb", "/ˈɪntjʊˌbeɪtɪŋ/", "đang đặt ống thông khí quản"),
    ("067853", "justiciars", "noun", "/dʒʌˈstɪʃiərz/", "quan tòa tối cao Anh thời trung cổ"),
    ("067854", "khayas", "noun", "/ˈkaɪəz/", "cây gỗ gụ châu Phi thuộc chi Khaya"),
    ("067855", "kuroshios", "noun", "/ˌkʊroʊˈʃiːoʊz/", "dòng hải lưu nóng Kuroshio Nhật"),
    ("067856", "lamivudines", "noun", "/ləˈmɪvjʊˌdiːnz/", "thuốc kháng vi rút HIV lamivudin"),
    ("067857", "maintenons", "noun", "/mæntˈnɒnz/", "Phu nhân Maintenon triều Louis XIV"),
    ("067858", "malvas", "noun", "/ˈmælvəz/", "cây cẩm quỳ thuộc chi Malva"),
    ("067859", "marginalities", "noun", "/ˌmɑːrdʒɪˈnælɪtiz/", "tình trạng bị đẩy ra bên lề xã hội"),
    ("067860", "markovas", "noun", "/ˈmɑːrkəvəz/", "nữ nghệ sĩ múa ba lê A. Markova"),
    ("067861", "meshworks", "noun", "/ˈmɛʃˌwɜːrks/", "mạng lưới cấu trúc đan xen"),
    ("067862", "milhauds", "noun", "/miːˈjoʊz/", "nhà soạn nhạc Pháp Darius Milhaud"),
    ("067863", "ministrations", "noun", "/ˌmɪnɪˈstreɪʃənz/", "sự chăm sóc giúp đỡ tận tình"),
    ("067864", "mycotoxins", "noun", "/ˌmaɪkoʊˈtɒksɪnz/", "độc tố sinh học do nấm mốc tiết ra"),
    ("067865", "numerations", "noun", "/ˌnjuːməˈreɪʃənz/", "hệ thống ghi số; phép đếm đánh số"),
    ("067866", "numismatists", "noun", "/njuːˈmɪzmətɪsts/", "nhà nghiên cứu sưu tầm tiền xu cổ"),
    ("067867", "overextending", "verb", "/ˌoʊvərɪkˈstɛndɪŋ/", "đang mở rộng hoặc gắng quá sức"),
    ("067868", "overextends", "verb", "/ˌoʊvərɪkˈstɛndz/", "kéo căng quá mức; làm quá sức"),
    ("067869", "overmuches", "noun", "/ˌoʊvərˈmʌtʃɪz/", "số lượng dư thừa quá mức cho phép"),
    ("067870", "pastos", "noun", "/ˈpɑːstoʊz/", "thành phố Pasto tây nam Colombia"),
    ("067871", "pederasts", "noun", "/ˈpɛdəˌræsts/", "kẻ xâm hại trẻ vị thành niên (cổ)"),
    ("067872", "peleuses", "noun", "/ˈpiːliəsɪz/", "vua Peleus trong thần thoại Hy Lạp"),
    ("067873", "peridotites", "noun", "/pəˈrɪdəˌtaɪts/", "đá mắc ma siêu mafic peridotit"),
    ("067874", "philadelphuses", "noun", "/ˌfɪləˈdɛlfəsɪz/", "cây mai giả hoa thơm trắng"),
    ("067875", "phlogistons", "noun", "/flɒˈdʒɪstɒnz/", "chất cháy giả định trong hóa học cổ"),
    ("067876", "photostats", "noun", "/ˈfoʊtəˌstæts/", "máy hoặc bản sao chụp tài liệu xưa"),
    ("067877", "phytochemicals", "noun", "/ˌfaɪtoʊˈkɛmɪkəlz/", "hợp chất sinh học tự nhiên thực vật"),
    ("067878", "pigmans", "noun", "/ˈpɪɡmənz/", "người chăn nuôi đàn lợn"),
    ("067879", "platier", "adj", "/ˈpleɪtiər/", "dạng phiến dẹt hơn; bằng phẳng hơn"),
    ("067880", "platiest", "adj", "/ˈpleɪtiɪst/", "dạng phiến dẹt nhất; bằng phẳng"),
    ("067881", "plummier", "adj", "/ˈplʌmiər/", "ngon lành béo bở hấp dẫn hơn"),
    ("067882", "plummiest", "adj", "/ˈplʌmiɪst/", "ngon lành béo bở hấp dẫn nhất"),
    ("067883", "progestogens", "noun", "/proʊˈdʒɛstədʒənz/", "hoóc-môn nhóm progestogen thai kỳ"),
    ("067884", "putamens", "noun", "/pjuːˈteɪmənz/", "nhân bèo sẫm trong hạch nền não bộ"),
    ("067885", "reinforcers", "noun", "/ˌriːɪnˈfɔːrsərz/", "tác nhân củng cố hành vi tâm lý"),
    ("067886", "saltbushes", "noun", "/ˈsɔːltˌbʊʃɪz/", "cây bụi chịu mặn mọc vùng khô hạn"),
    ("067887", "screechier", "adj", "/ˈskriːtʃiər/", "chói tai rít lên the thé hơn"),
    ("067888", "screechiest", "adj", "/ˈskriːtʃiɪst/", "chói tai rít lên the thé nhất"),
    ("067889", "seraglios", "noun", "/sɪˈrɑːlioʊz/", "hậu cung cung điện hoàng gia Thổ"),
    ("067890", "shirers", "noun", "/ˈʃaɪrərz/", "nhà sử học báo chí William Shirer"),
    ("067891", "shirtwaists", "noun", "/ˈʃɜːrtˌweɪsts/", "áo sơ mi nữ chít eo kiểu cổ điển"),
    ("067892", "snifters", "noun", "/ˈsnɪftərz/", "ly bầu đáy rộng uống rượu mạnh"),
    ("067893", "soundmans", "noun", "/ˈsaʊndmənz/", "kỹ thuật viên âm thanh thu âm phim"),
    ("067894", "sporophytes", "noun", "/ˈspɔːrəˌfaɪts/", "thể bào tử sinh bào tử ở thực vật"),
    ("067895", "sprogs", "noun", "/sprɒɡz/", "tân binh lính mới; trẻ nhỏ (Anh)"),
    ("067896", "stereoscopes", "noun", "/ˈstɛriəˌskoʊps/", "kính xem ảnh lập thể ba chiều"),
    ("067897", "teleosts", "noun", "/ˈtɛliˌɒsts/", "nhóm cá xương thật chiếm đa số"),
    ("067898", "tetroxides", "noun", "/tɛˈtrɒksaɪdz/", "hợp chất hóa học bốn oxy tetroxit"),
    ("067899", "ticktocks", "noun", "/ˈtɪkˌtɒks/", "tiếng tích tắc đều đặn của đồng hồ"),
    ("067900", "tindales", "noun", "/ˈtɪndəlz/", "học giả dịch Kinh Thánh Tyndale"),
    ("067901", "toolmakers", "noun", "/ˈtuːlˌmeɪkərz/", "thợ chế tạo dụng cụ khuôn mẫu cơ"),
    ("067902", "torreons", "noun", "/ˌtɒriˈoʊnz/", "thành phố Torreón miền bắc Mexico"),
]

with open("scratch/b34_r06_raw_p4.json") as f:
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

with open("scratch/b34_r06_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r06_p4.json OK")
