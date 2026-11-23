import json

items = [
    ("066603", "plushier", "adj", "/ˈplʌʃiər/", "mềm mượt dày như nhung hơn"),
    ("066604", "plushiest", "adj", "/ˈplʌʃiɪst/", "mềm mượt dày như nhung nhất"),
    ("066605", "postulations", "noun", "/ˌpɒstjəˈleɪʃənz/", "giả định tiên đề đưa ra chứng minh"),
    ("066606", "proprietresses", "noun", "/prəˈpraɪətrɪsɪz/", "nữ chủ nhân cơ sở kinh doanh"),
    ("066607", "ranitidines", "noun", "/rəˈnɪtɪˌdiːnz/", "thuốc giảm tiết axit ranitidin"),
    ("066608", "redbuds", "noun", "/ˈrɛdˌbʌdz/", "cây hoa tử kinh nở hoa mùa xuân"),
    ("066609", "respired", "verb", "/rɪˈspaɪərd/", "đã hít thở; đã hô hấp trao đổi khí"),
    ("066610", "respires", "verb", "/rɪˈspaɪərz/", "hít thở; hô hấp trao đổi khí"),
    ("066611", "respiring", "verb", "/rɪˈspaɪərɪŋ/", "đang hít thở; hô hấp trao đổi khí"),
    ("066612", "rhabdomyosarcomas", "noun", "/ˌræbdoʊˌmaɪoʊsɑːrˈkoʊməz/", "khối u ác tính mô cơ vân"),
    ("066613", "roamers", "noun", "/ˈroʊmərz/", "người lang thang phiêu bạt đây đó"),
    ("066614", "roundheads", "noun", "/ˈraʊndˌhɛdz/", "phe Nghị viện trong Nội chiến Anh"),
    ("066615", "saqqaras", "noun", "/səˈkɑːrəz/", "nghĩa trang kim tự tháp Saqqara"),
    ("066616", "sawans", "noun", "/ˈsɑːwənz/", "tháng Sawan mùa mưa theo lịch Ấn"),
    ("066617", "sawflies", "noun", "/ˈsɔːˌflaɪz/", "ong cắn lá bọ cưa hại cây"),
    ("066618", "scouters", "noun", "/ˈskaʊtərz/", "huynh trưởng hướng đạo sinh"),
    ("066619", "septets", "noun", "/sɛpˈtɛts/", "nhóm bảy nhạc công; bộ bảy"),
    ("066620", "smegmas", "noun", "/ˈsmɛɡməz/", "chất bựa sinh dục tích tụ tự nhiên"),
    ("066621", "smoggier", "adj", "/ˈsmɒɡiər/", "mù mịt khói bụi ô nhiễm hơn"),
    ("066622", "smoggiest", "adj", "/ˈsmɒɡiɪst/", "mù mịt khói bụi ô nhiễm nhất"),
    ("066623", "squattier", "adj", "/ˈskwɒtiər/", "lùn béo chắc nịch hơn"),
    ("066624", "squattiest", "adj", "/ˈskwɒtiɪst/", "lùn béo chắc nịch nhất"),
    ("066625", "szells", "noun", "/sɛlz/", "nhạc trưởng Hungary George Szell"),
    ("066626", "taifs", "noun", "/taɪfs/", "thành phố Taif ở Ả Rập Xê Út"),
    ("066627", "tutankhamens", "noun", "/ˌtuːtənˈkɑːmənz/", "Pharaon Ai Cập Tutankhamun"),
    ("066628", "usufructs", "noun", "/ˈjuːzjʊˌfrʌkts/", "quyền hưởng dụng tài sản người khác"),
    ("066629", "wassermanns", "noun", "/ˈwɑːsərmənz/", "xét nghiệm huyết thanh giang mai"),
    ("066630", "xanthines", "noun", "/ˈzænθiːnz/", "hợp chất hữu cơ kích thích xanthin"),
    ("066631", "zebus", "noun", "/ˈziːbjuːz/", "bò u lưng gù vùng nhiệt đới Ấn Độ"),
    ("066632", "alizarin carmine", "phrase", "/əˈlɪzərɪn ˈkɑːrmaɪn/", "phẩm nhuộm đỏ thắm alizarin"),
    ("066633", "anaphoric relation", "phrase", "/ˌænəˈfɔːrɪk rɪˈleɪʃən/", "quan hệ hồi chỉ trong ngôn ngữ"),
    ("066634", "babinski reflex", "phrase", "/bəˈbɪnski ˈriːflɛks/", "phản xạ bệnh lý ngón chân Babinski"),
    ("066635", "black cohosh", "phrase", "/blæk ˈkoʊhɒʃ/", "cây thiên ma đen Bắc Mỹ thảo dược"),
    ("066636", "blue cohosh", "phrase", "/bluː ˈkoʊhɒʃ/", "cây thiên ma xanh Bắc Mỹ"),
    ("066637", "canvasback duck", "phrase", "/ˈkænvəsˌbæk dʌk/", "vịt lưng trắng đầu hung Bắc Mỹ"),
    ("066638", "carlina vulgaris", "phrase", "/kɑːrˈlaɪnə vʌlˈɡɛərɪs/", "cây cúc gai thường châu Âu"),
    ("066639", "cervus sika", "phrase", "/ˈsɜːrvəs ˈsaɪkə/", "loài hươu sao đốm trắng Đông Á"),
    ("066640", "chalcis fly", "phrase", "/ˈkælsɪs flaɪ/", "ong ký sinh nhỏ thuộc chi Chalcis"),
    ("066641", "cubital joint", "phrase", "/ˈkjuːbɪtəl dʒɔɪnt/", "khớp khuỷu nối cánh và cẳng tay"),
    ("066642", "cubital nerve", "phrase", "/ˈkjuːbɪtəl nɜːrv/", "dây thần kinh trụ dọc khuỷu tay"),
    ("066643", "deodar cedar", "phrase", "/ˈdiːədɑːr ˈsiːdər/", "cây tuyết tùng Himalaya deodar"),
    ("066644", "discoid lupus erythematosus", "phrase", "/ˈdɪskɔɪd ˈluːpəs ˌɛrɪˌθɛməˈtoʊsəs/", "bệnh lupus ban đỏ dạng đĩa"),
    ("066645", "edouard vuillard", "phrase", "/eɪˈdwɑːr ˈvwiːjɑːr/", "họa sĩ Pháp Édouard Vuillard"),
    ("066646", "eucalyptus rostrata", "phrase", "/ˌjuːkəˈlɪptəs rɒˈstreɪtə/", "cây bạch đàn đỏ ven sông Úc"),
    ("066647", "family chironomidae", "phrase", "/ˈfæməli ˌkaɪrəˈnɒmɪdiː/", "họ muỗi lắc không đốt Chironomidae"),
    ("066648", "felis concolor", "phrase", "/ˈfiːlɪs ˈkɒŋkələr/", "báo sư tử puma châu Mỹ"),
    ("066649", "fowling piece", "phrase", "/ˈfaʊlɪŋ piːs/", "súng săn nòng trơn bắn chim"),
    ("066650", "genus annona", "phrase", "/ˈdʒiːnəs əˈnoʊnə/", "chi cây mãng cầu na Annona"),
    ("066651", "genus ascaris", "phrase", "/ˈdʒiːnəs ˈæskərɪs/", "chi giun đũa ký sinh ruột Ascaris"),
    ("066652", "genus boletus", "phrase", "/ˈdʒiːnəs boʊˈliːtəs/", "chi nấm thông lỗ xốp Boletus"),
    ("066653", "genus carica", "phrase", "/ˈdʒiːnəs ˈkærɪkə/", "chi cây đu đủ Carica"),
    ("066654", "genus centaurea", "phrase", "/ˈdʒiːnəs sɛnˈtɔːriə/", "chi hoa thanh cúc Centaurea"),
    ("066655", "genus chalcis", "phrase", "/ˈdʒiːnəs ˈkælsɪs/", "chi ong ký sinh nhỏ Chalcis"),
    ("066656", "genus chlamydomonas", "phrase", "/ˈdʒiːnəs ˌklæmɪdəˈmoʊnəs/", "chi tảo lục đơn bào Chlamydomonas"),
    ("066657", "genus euonymus", "phrase", "/ˈdʒiːnəs juːˈɒnɪməs/", "chi cây đỗ trọng cảnh Euonymus"),
    ("066658", "genus gentiana", "phrase", "/ˈdʒiːnəs ˌdʒɛnʃiˈeɪnə/", "chi hoa long đởm thảo Gentiana"),
    ("066659", "genus grevillea", "phrase", "/ˈdʒiːnəs ɡrəˈvɪliə/", "chi cây ngân hoa Grevillea Úc"),
    ("066660", "genus mazama", "phrase", "/ˈdʒiːnəs məˈzɑːmə/", "chi hươu lùn Nam Mỹ Mazama"),
    ("066661", "genus urtica", "phrase", "/ˈdʒiːnəs ˈɜːrtɪkə/", "chi cây tầm ma gây ngứa Urtica"),
    ("066662", "gutta balata", "phrase", "/ˈɡʌtə bəˈlɑːtə/", "nhựa cây cao su thiên nhiên balata"),
    ("066663", "hsuan chiao", "phrase", "/ʃwæn dʒaʊ/", "đạo Huyền giáo tức Đạo giáo"),
    ("066664", "inhere in", "phrase", "/ɪnˈhɪər ɪn/", "vốn thuộc về bản chất bên trong"),
    ("066665", "jakob liebmann beer", "phrase", "/ˈjɑːkɒp ˈliːbmɑːn bɛər/", "nhà soạn nhạc Đức Meyerbeer"),
    ("066666", "jawless fish", "phrase", "/ˈdʒɔːləs fɪʃ/", "cá không hàm như cá mút đá"),
    ("066667", "jean edouard vuillard", "phrase", "/ʒɑːn eɪˈdwɑːr ˈvwiːjɑːr/", "họa sĩ Pháp J. É. Vuillard"),
    ("066668", "josef michel montgolfier", "phrase", "/ʒoʊˈzɛf miːˈʃɛl mɒntˈɡɒlfiər/", "nhà phát minh khinh khí cầu Pháp"),
    ("066669", "karl landsteiner", "phrase", "/kɑːrl ˈlændˌstaɪnər/", "nhà sinh học phát hiện nhóm máu"),
    ("066670", "larix occidentalis", "phrase", "/ˈlɛərɪks ˌɒksɪdɛnˈteɪlɪs/", "cây thông rụng lá miền tây Bắc Mỹ"),
    ("066671", "madia sativa", "phrase", "/ˈmeɪdiə səˈtaɪvə/", "cây cúc dầu trồng lấy hạt madia"),
    ("066672", "magnolia macrophylla", "phrase", "/mæɡˈnoʊliə ˌmækroʊˈfɪlə/", "cây mộc lan lá to Bắc Mỹ"),
    ("066673", "melvil dewey", "phrase", "/ˈmɛlvɪl ˈduːi/", "người lập bảng phân loại thư viện"),
    ("066674", "mountain rimu", "phrase", "/ˈmaʊntən ˈriːmuː/", "cây tùng bách núi ở New Zealand"),
    ("066675", "musca domestica", "phrase", "/ˈmʌskə doʊˈmɛstɪkə/", "loài ruồi nhà phổ biến toàn cầu"),
    ("066676", "neandertal man", "phrase", "/niˈændərtɑːl mæn/", "người tiền sử Neanderthal cổ đại"),
    ("066677", "nicotinamide adenine dinucleotide", "phrase", "/ˌnɪkəˈtɪnəˌmaɪd ˈædəniːn daɪˈnuːkliəˌtaɪd/", "coenzym chuyển hóa tế bào NAD"),
    ("066678", "oboe da caccia", "phrase", "/ˈoʊboʊ dɑː ˈkɑːtʃə/", "kèn ô-boa trầm cong thời Baroque"),
    ("066679", "olecranon process", "phrase", "/oʊˈlɛkrəˌnɒn ˈprɒsɛs/", "mỏm khuỷu nhô ra ở xương trụ"),
    ("066680", "order anura", "phrase", "/ˈɔːrdər əˈnjʊərə/", "bộ Không đuôi gồm ếch nhái cóc"),
    ("066681", "otitis externa", "phrase", "/oʊˈtaɪtɪs ɛkˈstɜːrnə/", "bệnh viêm ống tai ngoài"),
    ("066682", "pastor roseus", "phrase", "/ˈpæstər ˈroʊziəs/", "chim sáo màu hồng di cư Á Âu"),
    ("066683", "poinciana regia", "phrase", "/ˌpɔɪnsiˈeɪnə ˈriːdʒiə/", "cây phượng vĩ nở hoa đỏ rực"),
    ("066684", "polygonum orientale", "phrase", "/pəˈlɪɡənəm ˌɔːriɛnˈteɪli/", "cây nghể bà; cỏ thủy hồng"),
    ("066685", "quercus suber", "phrase", "/ˈkwɜːrkəs ˈsuːbər/", "cây sồi vỏ bần làm nút chai vang"),
    ("066686", "raoul dufy", "phrase", "/rɑːˈuːl djuːˈfi/", "họa sĩ Pháp Raoul Dufy"),
    ("066687", "reentrant angle", "phrase", "/riːˈɛntrənt ˈæŋɡəl/", "góc lõm lớn hơn 180 độ"),
    ("066688", "renal corpuscle", "phrase", "/ˈriːnəl ˈkɔːrpʌsəl/", "tiểu thể thận lọc máu cầu thận"),
    ("066689", "res gestae", "phrase", "/ˈreɪz ˈdʒɛstiː/", "tình tiết gắn liền hành vi pháp lý"),
    ("066690", "rock hyrax", "phrase", "/rɒk ˈhaɪræks/", "thú nhỏ sống ở hốc đá châu Phi"),
    ("066691", "sciurus vulgaris", "phrase", "/saɪˈjʊərəs vʌlˈɡɛərɪs/", "loài sóc đỏ tai chùm châu Âu"),
    ("066692", "shirred egg", "phrase", "/ʃɜːrd ɛɡ/", "trứng nướng chén kiểu Pháp"),
    ("066693", "sixpenny nail", "phrase", "/ˈsɪkspɛni neɪl/", "đinh sắt đóng gỗ dài hai inch"),
    ("066694", "spiked loosestrife", "phrase", "/spaɪkt ˈluːsˌstraɪf/", "cây thiên khuê thảo bông tím"),
    ("066695", "subgenus poinciana", "phrase", "/sʌbˈdʒiːnəs ˌpɔɪnsiˈeɪnə/", "phân chi thực vật phượng Poinciana"),
    ("066696", "summer cohosh", "phrase", "/ˈsʌmər ˈkoʊhɒʃ/", "cây thiên ma hè nở hoa trắng"),
    ("066697", "superheterodyne receiver", "phrase", "/ˌsuːpərˈhɛtərəˌdaɪn rɪˈsiːvər/", "máy thu vô tuyến siêu ngoại sai"),
    ("066698", "the pamirs", "phrase", "/ðə pəˈmɪərz/", "dãy núi cao Pamir vùng Trung Á"),
    ("066699", "thermobaric bomb", "phrase", "/ˌθɜːrmoʊˈbærɪk bɒm/", "bom nhiệt áp hút oxy tạo sóng nổ"),
    ("066700", "thuja orientalis", "phrase", "/ˈθjuːdʒə ˌɔːriɛnˈteɪlɪs/", "cây trắc bách diệp phương Đông"),
    ("066701", "turbinate bone", "phrase", "/ˈtɜːrbɪnət boʊn/", "xương xoăn mũi làm ấm không khí"),
    ("066702", "walpurgis night", "phrase", "/vɑːlˈpʊərɡɪs naɪt/", "đêm hội truyền thống Walpurgis"),
]

with open("scratch/b34_r04_raw_p2.json") as f:
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

with open("scratch/b34_r04_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r04_p2.json OK")
