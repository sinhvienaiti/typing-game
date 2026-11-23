import json

items = [
    ("069003", "calking", "verb", "/ˈkɔːkɪŋ/", "đang xảm kín khe; đóng đinh móng"),
    ("069004", "calks", "noun", "/kɔːks/", "đinh chống trượt dưới móng ngựa"),
    ("069005", "chagas", "noun", "/ˈtʃɑːɡəz/", "tiếng Chaga ở Tanzania; bệnh Chagas"),
    ("069006", "chrysotiles", "noun", "/ˈkrɪsəˌtaɪlz/", "amiăng trắng khoáng vật chrysotile"),
    ("069007", "corticotropins", "noun", "/ˌkɔːrtɪkoʊˈtroʊpɪnz/", "hoóc-môn hướng vỏ thượng thận ACTH"),
    ("069008", "counterproposals", "noun", "/ˌkaʊntərprəˈpoʊzəlz/", "đề xuất phản hồi đưa ra đối lại"),
    ("069009", "crassulas", "noun", "/ˈkræsjʊləz/", "cây sen đá ngọc bích chi Crassula"),
    ("069010", "cubbyholes", "noun", "/ˈkʌbiˌhoʊlz/", "ngăn tủ nhỏ; căn phòng chật hẹp"),
    ("069011", "cusks", "noun", "/kʌsks/", "cá tuyết cusk vùng biển Bắc Đại Tây"),
    ("069012", "cutworms", "noun", "/ˈkʌtˌwɜːrmz/", "sâu xám cắn ngang gốc cây non"),
    ("069013", "deadnesses", "noun", "/ˈdɛdnəsɪz/", "trạng thái lặng ngắt vô hồn chết"),
    ("069014", "defilers", "noun", "/dɪˈfaɪlərz/", "kẻ làm ô uế vấy bẩn nơi linh thiêng"),
    ("069015", "delfs", "noun", "/dɛlfs/", "hố khai thác đá lộ thiên; gốm men"),
    ("069016", "demoralises", "verb", "/dɪˈmɒrəˌlaɪzɪz/", "làm mất tinh thần nhụt chí suy sụp"),
    ("069017", "depressors", "noun", "/dɪˈprɛsərz/", "cơ hạ; que đè lưỡi khám họng"),
    ("069018", "diaphoretics", "noun", "/ˌdaɪəfəˈrɛtɪks/", "thuốc làm vã mồ hôi giải cảm sốt"),
    ("069019", "diathses", "noun", "/daɪˈæθɪsiːz/", "cơ địa dễ mắc bệnh bẩm sinh"),
    ("069020", "dubonnets", "noun", "/ˌduːbəˈneɪz/", "rượu khai vị ngọt thảo mộc Dubonnet"),
    ("069021", "dysarthrias", "noun", "/dɪsˈɑːrθriəz/", "chứng nói khó do liệt cơ phát âm"),
    ("069022", "elderships", "noun", "/ˈɛldərʃɪps/", "chức vị trưởng lão trong giáo hội"),
    ("069023", "embrasures", "noun", "/ɪmˈbreɪʒərz/", "lỗ châu mai trên tường thành; hốc"),
    ("069024", "enucleations", "noun", "/ɪˌnjuːkliˈeɪʃənz/", "phẫu thuật khoét bỏ nhân mắt hoặc u"),
    ("069025", "erlenmeyers", "noun", "/ˈɜːrlənˌmaɪərz/", "nhà hóa học Đức Emil Erlenmeyer"),
    ("069026", "espagnoles", "noun", "/ˌɛspænˈjoʊlz/", "xốt nâu cơ bản ẩm thực Pháp"),
    ("069027", "evildoers", "noun", "/ˈiːvəlˌduːərz/", "kẻ làm điều gian ác phạm tội lỗi"),
    ("069028", "fetlocks", "noun", "/ˈfɛtˌlɒks/", "khớp cổ chân phía trên móng ngựa"),
    ("069029", "feudatories", "noun", "/ˈfjuːdətəriz/", "chư hầu nhận thái ấp thời phong"),
    ("069030", "flypapers", "noun", "/ˈflaɪˌpeɪpərz/", "giấy keo dính bẫy ruồi muỗi"),
    ("069031", "fukiens", "noun", "/fuːˈkjɛnz/", "tỉnh và tiếng Phúc Kiến Trung Quốc"),
    ("069032", "gimcracks", "noun", "/ˈdʒɪmˌkræks/", "đồ trang trí hào nhoáng rẻ tiền"),
    ("069033", "haemodialyses", "noun", "/ˌhiːmoʊdaɪˈælɪsiːz/", "liệu pháp chạy thận lọc máu"),
    ("069034", "halms", "noun", "/hɑːmz/", "thân rơm rạ cây họ đậu ngũ cốc"),
    ("069035", "handwashed", "verb", "/ˈhændˌwɒʃt/", "đã giặt giũ rửa sạch bằng tay"),
    ("069036", "handwashes", "verb", "/ˈhændˌwɒʃɪz/", "giặt nhẹ nhàng bằng tay không máy"),
    ("069037", "handwashing", "verb", "/ˈhændˌwɒʃɪŋ/", "đang rửa tay; đang giặt bằng tay"),
    ("069038", "hcfcs", "noun", "/ˌeɪtʃ siː ɛf ˈsiːz/", "khí làm lạnh phá tầng ôzôn HCFC"),
    ("069039", "headwaiters", "noun", "/ˌhɛdˈweɪtərz/", "trưởng phục vụ bàn tại nhà hàng"),
    ("069040", "homeoboxes", "noun", "/ˈhoʊmioʊˌbɒksɪz/", "đoạn gen hộp điều khiển phát triển"),
    ("069041", "hotchpotches", "noun", "/ˈhɒtʃˌpɒtʃɪz/", "mớ hỗn độn lộn xộn pha tạp nhiều"),
    ("069042", "hyaenas", "noun", "/haɪˈiːnəz/", "linh cẩu ăn xác vùng thảo nguyên"),
    ("069043", "ideograms", "noun", "/ˈɪdiəˌɡræmz/", "ký tự chữ biểu ý (ngôn ngữ học)"),
    ("069044", "idolaters", "noun", "/aɪˈdɒlətərz/", "người sùng bái tôn thờ ngẫu tượng"),
    ("069045", "insufflations", "noun", "/ˌɪnsəˈfleɪʃənz/", "kỹ thuật bơm thổi khí vào khoang"),
    ("069046", "isobars", "noun", "/ˈaɪsəˌbɑːrz/", "đường đẳng áp trên bản đồ thời tiết"),
    ("069047", "jotters", "noun", "/ˈdʒɒtərz/", "quyển sổ tay nhỏ ghi chép nhanh"),
    ("069048", "kishinevs", "noun", "/ˌkɪʃɪˈnɛvz/", "thủ đô Chișinău của Moldova"),
    ("069049", "kvasses", "noun", "/kvɑːsɪz/", "thức uống lúa mạch lên men Nga"),
    ("069050", "lateralizations", "noun", "/ˌlætərəlaɪˈzeɪʃənz/", "sự chuyên biệt hóa bán cầu não"),
    ("069051", "loanwords", "noun", "/ˈloʊnˌwɜːrdz/", "từ vay mượn từ ngôn ngữ khác"),
    ("069052", "maltis", "noun", "/ˈmɔːltiz/", "tiếng Malta hoặc người đảo Malta"),
    ("069053", "metalworkers", "noun", "/ˈmɛtəlˌwɜːrkərz/", "thợ gia công rèn đúc kim loại"),
    ("069054", "montespans", "noun", "/ˌmɒntəˈspɒnz/", "Nữ hầu tước Pháp de Montespan"),
    ("069055", "navarinos", "noun", "/ˌnævəˈriːnoʊz/", "trận hải chiến Navarino Hy Lạp"),
    ("069056", "noethers", "noun", "/ˈnɜːtərz/", "nhà toán học Đức Emmy Noether"),
    ("069057", "nomenklaturas", "noun", "/noʊˈmɛŋkləˌtjʊərəz/", "tầng lớp cán bộ đặc quyền Xô viết"),
    ("069058", "numberplates", "noun", "/ˈnʌmbərˌpleɪts/", "biển số đăng ký xe cơ giới (Anh)"),
    ("069059", "ogives", "noun", "/ˈoʊdʒaɪvz/", "vòm nhọn Gothic; mũi hình nón đạn"),
    ("069060", "overdrawing", "verb", "/ˌoʊvərˈdrɔːɪŋ/", "đang chi vượt số dư; phóng đại"),
    ("069061", "overdraws", "verb", "/ˌoʊvərˈdrɔːz/", "rút quá số dư tài khoản; nói quá"),
    ("069062", "pasterns", "noun", "/ˈpæstərnz/", "đốt cổ chân dưới nối móng ngựa"),
    ("069063", "peccaries", "noun", "/ˈpɛkəriz/", "lợn lòi peccary bản địa châu Mỹ"),
    ("069064", "pekes", "noun", "/piːks/", "chó cảnh lông xù Bắc Kinh (tắt)"),
    ("069065", "petrarcas", "noun", "/pɛˈtrɑːrkəz/", "nhà thơ Phục Hưng Ý Petrarca"),
    ("069066", "physostigmines", "noun", "/ˌfaɪsoʊˈstɪɡmiːnz/", "thuốc nhỏ mắt physostigmine"),
    ("069067", "picardies", "noun", "/ˈpɪkərdiz/", "vùng lịch sử Picardy miền bắc Pháp"),
    ("069068", "picuses", "noun", "/ˈpaɪkəsɪz/", "chi chim gõ kiến xanh Picus"),
    ("069069", "pingers", "noun", "/ˈpɪŋərz/", "máy phát xung âm thanh định vị"),
    ("069070", "pinnaces", "noun", "/ˈpɪnɪsɪz/", "xuồng máy nhỏ hoặc thuyền hai buồm"),
    ("069071", "pseudepigraphas", "noun", "/ˌsjuːdɪˈpɪɡrəfəz/", "ngụy thư mang danh tác giả cổ xưa"),
    ("069072", "pulques", "noun", "/ˈpʊlkeɪz/", "rượu lên men nhựa cây thùa Mexico"),
    ("069073", "railyards", "noun", "/ˈreɪlˌjɑːrdz/", "bãi ga tập kết lập tàu đường sắt"),
    ("069074", "raunches", "noun", "/rɔːntʃɪz/", "tính thô tục gợi dục dơ dáy (lóng)"),
    ("069075", "razorblades", "noun", "/ˈreɪzərˌbleɪdz/", "lưỡi dao lam sắc bén cạo râu"),
    ("069076", "reappraised", "verb", "/ˌriːəˈpreɪzd/", "đã đánh giá lại giá trị tình hình"),
    ("069077", "reappraises", "verb", "/ˌriːəˈpreɪzɪz/", "thẩm định đánh giá lại từ đầu"),
    ("069078", "reappraising", "verb", "/ˌriːəˈpreɪzɪŋ/", "đang xem xét đánh giá lại"),
    ("069079", "redondas", "noun", "/rɪˈdɒndəz/", "đảo Redonda thuộc Antigua Barbuda"),
    ("069080", "salvelinuses", "noun", "/ˌsælvəˈlaɪnəsɪz/", "cá hồi suối thuộc chi Salvelinus"),
    ("069081", "secretases", "noun", "/ˈsɛkrɪˌteɪsɪz/", "enzym cắt protein màng secretase"),
    ("069082", "serins", "noun", "/ˈsɛrɪnz/", "chim sẻ hót hay châu Âu Serinus"),
    ("069083", "serrations", "noun", "/sɛˈreɪʃənz/", "đường khía răng cưa dọc mép cạnh"),
    ("069084", "shiploads", "noun", "/ˈʃɪpˌloʊdz/", "chuyến hàng hóa chất đầy một tàu"),
    ("069085", "signallers", "noun", "/ˈsɪɡnələrz/", "lính thông tin tín hiệu phát cờ"),
    ("069086", "siloxanes", "noun", "/saɪˈlɒkseɪnz/", "hợp chất mạch silic-oxy siloxan"),
    ("069087", "slubs", "noun", "/slʌbz/", "đoạn sợi dệt xe xoắn phồng dày"),
    ("069088", "snarfed", "verb", "/snɑːrft/", "đã ăn ngấu nghiến; đã chôm lấy"),
    ("069089", "snarfing", "verb", "/ˈsnɑːrfɪŋ/", "đang ăn ngấu nghiến; lấy nhanh"),
    ("069090", "snarfs", "verb", "/snɑːrfs/", "ăn ngấu nghiến; lấy chôm nhanh"),
    ("069091", "sousaphones", "noun", "/ˈsuːzəˌfoʊnz/", "kèn bass đồng quấn vai diễu hành"),
    ("069092", "spathes", "noun", "/speɪðz/", "lá bắc mo bọc cụm hoa họ Ráy cau"),
    ("069093", "spinets", "noun", "/ˈspɪnɪts/", "đàn phím cổ nhỏ spinet; piano nhỏ"),
    ("069094", "sporrans", "noun", "/ˈspɒrənz/", "túi da lông đeo trước váy Scotland"),
    ("069095", "sportfishings", "noun", "/ˈspɔːrtˌfɪʃɪŋz/", "môn câu cá giải trí thể thao"),
    ("069096", "stiffeners", "noun", "/ˈstɪfənərz/", "thanh gia cường; chất làm cứng vải"),
    ("069097", "teakwoods", "noun", "/ˈtiːkˌwʊdz/", "gỗ tếch cứng bền chịu nước tốt"),
    ("069098", "thiazides", "noun", "/ˈθaɪəˌzaɪdz/", "nhóm thuốc lợi tiểu hạ áp thiazid"),
    ("069099", "thighbones", "noun", "/ˈθaɪˌboʊnz/", "xương đùi dài nhất trong cơ thể"),
    ("069100", "toklases", "noun", "/ˈtɒkləsɪz/", "nhà văn Mỹ Alice B. Toklas"),
    ("069101", "toxoids", "noun", "/ˈtɒksɔɪdz/", "giải độc tố dùng điều chế vắc-xin"),
    ("069102", "tribuli", "noun", "/ˈtrɪbjʊlaɪ/", "cây tật lê gai thuộc chi Tribulus"),
]

with open("scratch/b34_r09_raw_p1.json") as f:
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

with open("scratch/b34_r09_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r09_p1.json OK")
