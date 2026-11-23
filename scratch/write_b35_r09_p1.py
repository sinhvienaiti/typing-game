import json

items = [
    ("074003", "artiodactylas", "noun", "/ˌɑːrtioʊˈdæktɪləz/", "bộ Guốc chẵn (bò, lợn, hươu)"),
    ("074004", "autogyros", "noun", "/ˈɔːtoʊˌdʒaɪroʊz/", "máy bay cánh quay tự động autogyro"),
    ("074005", "autosomes", "noun", "/ˈɔːtəˌsoʊmz/", "nhiễm sắc thể thường (không giới)"),
    ("074006", "baryes", "noun", "/ˈbæriːz/", "đơn vị áp suất barye (CGS)"),
    ("074007", "broomcorns", "noun", "/ˈbruːmˌkɔːrnz/", "cây lúa miến làm chổi quét nhà"),
    ("074008", "bunchgrasses", "noun", "/ˈbʌntʃˌɡræsɪz/", "cỏ mọc thành từng khóm bụi dày"),
    ("074009", "byssi", "noun", "/ˈbɪsaɪ/", "tơ chân bám đá (trai vẹm); vải gai"),
    ("074010", "byssuses", "noun", "/ˈbɪsəsɪz/", "tơ chân bám đá (trai vẹm); vải mịn"),
    ("074011", "caladiums", "noun", "/kəˈleɪdiəmz/", "cây môn cảnh lá đốm chi Caladium"),
    ("074012", "calvarias", "noun", "/kælˈvɛəriəz/", "vòm sọ (phần trên hộp sọ)"),
    ("074013", "canebrakes", "noun", "/ˈkeɪnˌbreɪks/", "bụi rậm sậy trúc gai vùng đầm lầy"),
    ("074014", "capreoluses", "noun", "/kəˈpriːələsɪz/", "chi Hươu hoẵng châu Âu Capreolus"),
    ("074015", "carafates", "noun", "/ˈkærəˌfeɪts/", "thuốc tráng dạ dày Carafate"),
    ("074016", "cardamines", "noun", "/ˌkɑːrdəˈmaɪniːz/", "cây cải đắng đồng chi Cardamine"),
    ("074017", "cardinalates", "noun", "/ˈkɑːrdɪnəlɪts/", "chức hồng y; hồng y đoàn Công giáo"),
    ("074018", "cerussites", "noun", "/sɪˈrʌsaɪts/", "quặng chì cacbonat cerussit"),
    ("074019", "cervidaes", "noun", "/ˈsɜːrvɪˌdiːz/", "họ Hươu nai (bộ Guốc chẵn)"),
    ("074020", "chancres", "noun", "/ˈʃæŋkərz/", "vết loét săng giang mai không đau"),
    ("074021", "clangoured", "verb", "/ˈklæŋɡərd/", "đã vang tiếng kim loại rền (Anh)"),
    ("074022", "clangouring", "verb", "/ˈklæŋɡərɪŋ/", "đang vang tiếng kim loại rền (Anh)"),
    ("074023", "clangours", "noun", "/ˈklæŋɡərz/", "tiếng vang kim loại chói tai (Anh)"),
    ("074024", "clotheshorses", "noun", "/ˈkloʊðzˌhɔːrsɪz/", "giá phơi quần áo; người ham chưng"),
    ("074025", "connecters", "noun", "/kəˈnɛktərz/", "đầu nối; người kết nối (biến thể)"),
    ("074026", "crambes", "noun", "/ˈkræmbiz/", "chi Cây cải bắp biển Crambe"),
    ("074027", "cumanas", "noun", "/ˌkuːməˈnɑːz/", "thành phố cảng Cumaná ở Venezuela"),
    ("074028", "curacoas", "noun", "/ˌkjʊərəˈsoʊz/", "rượu mùi vỏ cam đắng Curaçao"),
    ("074029", "damozels", "noun", "/ˈdæməzɛlz/", "thiếu nữ khuê các (từ cổ thi ca)"),
    ("074030", "dastards", "noun", "/ˈdæstərdz/", "kẻ hèn nhát đê tiện đánh lén"),
    ("074031", "devisers", "noun", "/dɪˈvaɪzərz/", "người nghĩ ra kế hoạch phát minh"),
    ("074032", "dmuses", "noun", "/ˌdiː ˈmjuːzɪz/", "bằng Tiến sĩ Âm nhạc (D.Mus.)"),
    ("074033", "dolichoses", "noun", "/ˈdɒlɪˌkɒsɪz/", "chi Đậu ván cúc (Dolichos)"),
    ("074034", "effervesced", "verb", "/ˌɛfərˈvɛst/", "đã sủi bọt khí; đã sôi nổi nhiệt"),
    ("074035", "effervesces", "verb", "/ˌɛfərˈvɛsɪz/", "sủi bọt khí; sôi nổi hứng khởi"),
    ("074036", "epidendrums", "noun", "/ˌɛpɪˈdɛndrəmz/", "chi Hoa lan biểu sinh Epidendrum"),
    ("074037", "epiphenomenons", "noun", "/ˌɛpɪfɪˈnɒmɪnɒnz/", "hiện tượng phụ đi kèm (triết, y)"),
    ("074038", "epiphoras", "noun", "/ɪˈpɪfərəz/", "phép điệp cuối; chứng tràn nước mắt"),
    ("074039", "fila", "noun", "/ˈfaɪlə/", "sợi mảnh; cấu trúc dạng sợi"),
    ("074040", "filums", "noun", "/ˈfaɪləmz/", "cấu trúc sợi mảnh (sinh học)"),
    ("074041", "flunkeys", "noun", "/ˈflʌŋkiz/", "người hầu mặc chế phục; kẻ nịnh bợ"),
    ("074042", "fractionates", "verb", "/ˈfrækʃəˌneɪts/", "phân đoạn tách hỗn hợp (hóa)"),
    ("074043", "gazellas", "noun", "/ɡəˈzɛləz/", "chi Linh dương gazelle (Gazella)"),
    ("074044", "glossinas", "noun", "/ɡlɒˈsaɪnəz/", "ruồi xê-xê truyền bệnh ngủ"),
    ("074045", "harebells", "noun", "/ˈhɛərˌbɛlz/", "hoa chuông lam đồng cỏ châu Âu"),
    ("074046", "helvetians", "noun", "/hɛlˈviːʃənz/", "người bộ tộc Helvetii (Thụy Sĩ cổ)"),
    ("074047", "hemosiderins", "noun", "/ˌhiːmoʊˈsɪdərɪnz/", "phức hợp dự trữ sắt hemosiderin"),
    ("074048", "heterocycles", "noun", "/ˌhɛtəroʊˈsaɪkəlz/", "hợp chất hữu cơ dị vòng (hóa học)"),
    ("074049", "hevesies", "noun", "/ˈhɛvəʃiz/", "nhà hóa học Nobel George de Hevesy"),
    ("074050", "hoydens", "noun", "/ˈhɔɪdənz/", "cô gái nghịch ngợm hiếu động"),
    ("074051", "internationalities", "noun", "/ˌɪntərnæʃəˈnælɪtiz/", "tính chất quốc tế toàn cầu"),
    ("074052", "invertases", "noun", "/ɪnˈvɜːrteɪsɪz/", "enzym phân giải đường sucrase"),
    ("074053", "jacobinisms", "noun", "/ˈdʒækəbɪˌnɪzəmz/", "chủ nghĩa cấp tiến Jacobin Pháp"),
    ("074054", "jewfishes", "noun", "/ˈdʒuːˌfɪʃɪz/", "cá mú đen khổng lồ biển nhiệt đới"),
    ("074055", "jnds", "noun", "/ˌdʒeɪ ɛn ˈdiːz/", "ngưỡng sai biệt vừa đủ nhận (JND)"),
    ("074056", "knucklers", "noun", "/ˈnʌklərz/", "cú ném bóng knuckleball (bóng chày)"),
    ("074057", "lacrimations", "noun", "/ˌlækrɪˈmeɪʃənz/", "sự tiết chảy nhiều nước mắt (y học)"),
    ("074058", "lamiums", "noun", "/ˈleɪmiəmz/", "cây tầm ma chết hoa đẹp chi Lamium"),
    ("074059", "leuctras", "noun", "/ˈluːktrəz/", "trận Leuctra năm 371 TCN Hy Lạp"),
    ("074060", "luminesced", "verb", "/ˌluːmɪˈnɛst/", "đã phát quang lạnh không tỏa nhiệt"),
    ("074061", "luminesces", "verb", "/ˌluːmɪˈnɛsɪz/", "phát quang lạnh (huỳnh, lân quang)"),
    ("074062", "luminescing", "verb", "/ˌluːmɪˈnɛsɪŋ/", "đang phát quang lạnh dịu nhẹ"),
    ("074063", "lyrebirds", "noun", "/ˈlaɪərˌbɜːrdz/", "chim thiên cầm đuôi đàn lia Úc"),
    ("074064", "maculates", "verb", "/ˈmækjʊˌleɪts/", "làm lấm tấm đốm; làm hoen ố"),
    ("074065", "maculating", "verb", "/ˈmækjʊˌleɪtɪŋ/", "đang làm lấm tấm đốm; làm hoen ố"),
    ("074066", "majuscules", "noun", "/ˈmædʒəˌskjuːlz/", "chữ in hoa lớn (cổ tự học)"),
    ("074067", "managerships", "noun", "/ˈmænɪdʒərʃɪps/", "chức vụ người quản lý giám đốc"),
    ("074068", "manannans", "noun", "/ˈmænənənz/", "thần biển Manannán thần thoại Celt"),
    ("074069", "messmates", "noun", "/ˈmɛsˌmeɪts/", "bạn cùng bàn ăn; đồng đội ăn chung"),
    ("074070", "microcopied", "verb", "/ˈmaɪkroʊˌkɒpid/", "đã chụp sao lưu lên vi phim"),
    ("074071", "microcopies", "verb", "/ˈmaɪkroʊˌkɒpiz/", "sao chụp thu nhỏ lên vi phim"),
    ("074072", "microcopying", "verb", "/ˈmaɪkroʊˌkɒpiɪŋ/", "đang sao chụp thu nhỏ lên vi phim"),
    ("074073", "microsporums", "noun", "/ˌmaɪkrəˈspɔːrəmz/", "nấm gây hắc lào Microsporum"),
    ("074074", "millerites", "noun", "/ˈmɪləˌraɪts/", "quặng niken sunfua; tín đồ Miller"),
    ("074075", "milliamperes", "noun", "/ˌmɪliˈæmpɪərz/", "đơn vị cường độ dòng miliampe (mA)"),
    ("074076", "mizzenmasts", "noun", "/ˈmɪzənˌmæsts/", "cột buồm sau cùng phía lái tàu"),
    ("074077", "mizzled", "verb", "/ˈmɪzəld/", "đã mưa bụi lâm thâm; làm rối (Anh)"),
    ("074078", "mizzles", "noun", "/ˈmɪzəlz/", "mưa bụi lâm thâm; làm hoang mang"),
    ("074079", "mizzling", "verb", "/ˈmɪzlɪŋ/", "đang mưa bụi lâm thâm (phương ngữ)"),
    ("074080", "modistes", "noun", "/moʊˈdiːsts/", "thợ thiết kế thời trang nữ và mũ"),
    ("074081", "monomaniacs", "noun", "/ˌmɒnoʊˈmeɪniæks/", "người mắc chứng cuồng ám ảnh đơn lẻ"),
    ("074082", "mucopolysaccharidoses", "noun", "/ˌmjuːkoʊpɒlɪsækərɪˈdoʊsiːz/", "bệnh tích tụ mucopolysaccharid"),
    ("074083", "mudcats", "noun", "/ˈmʌdˌkæts/", "cá trê đầu dẹt Bắc Mỹ mudcat"),
    ("074084", "nebulisers", "noun", "/ˈnɛbjʊˌlaɪzərz/", "máy xông khí dung phun sương (Anh)"),
    ("074085", "nefazodones", "noun", "/nɛˈfæzəˌdoʊnz/", "thuốc chống trầm cảm nefazodone"),
    ("074086", "oligochaetas", "noun", "/ˌɒlɪɡoʊˈkiːtəz/", "lớp Ít tơ (giun đất, giun chỉ)"),
    ("074087", "omphaloceles", "noun", "/ɒmˈfæləˌsiːlz/", "dị tật thoát vị rốn bẩm sinh"),
    ("074088", "palaeogeographies", "noun", "/ˌpælioʊdʒiˈɒɡrəfiz/", "ngành cổ địa lý học (cách viết Anh)"),
    ("074089", "pelters", "noun", "/ˈpɛltərz/", "cơn mưa đá trút nước xối xả; kẻ ném"),
    ("074090", "phytolaccas", "noun", "/ˌfaɪtəˈlækəz/", "cây thương lục chi Phytolacca"),
    ("074091", "pinaceaes", "noun", "/paɪˈneɪʃiˌiːz/", "họ Thông (thông, vân sam, lãnh sam)"),
    ("074092", "pirozhkis", "noun", "/pɪˈrɒʃkiz/", "bánh nướng nhân thịt rau pirozhki"),
    ("074093", "plesiosauruses", "noun", "/ˌpliːsiəˈsɔːrəsɪz/", "bò sát biển cổ dài Plesiosaurus"),
    ("074094", "pneumonectomies", "noun", "/ˌnjuːməˈnɛktəmiz/", "phẫu thuật cắt bỏ toàn bộ một phổi"),
    ("074095", "pockmarking", "verb", "/ˈpɒkˌmɑːrkɪŋ/", "đang làm rỗ mặt hoặc lốm đốm vết"),
    ("074096", "pockmarks", "noun", "/ˈpɒkˌmɑːrks/", "vết sẹo rỗ đậu mùa; vết rỗ bề mặt"),
    ("074097", "pointednesses", "noun", "/ˈpɔɪntɪdnəsɪz/", "độ nhọn hoắt; tính sắc bén sâu cay"),
    ("074098", "polychaetas", "noun", "/ˌpɒlɪˈkiːtəz/", "lớp Giun nhiều tơ (rươi, giun biển)"),
    ("074099", "polynyas", "noun", "/pəˈlɪnjəz/", "vùng biển hở giữa băng dày vùng cực"),
    ("074100", "postums", "noun", "/ˈpoʊstəmz/", "đồ uống ngũ cốc rang Postum (Mỹ)"),
    ("074101", "raptuses", "noun", "/ˈræptəsɪz/", "cơn xuất thần; cơn kịch phát"),
    ("074102", "recognisances", "noun", "/rɪˈkɒɡnɪzənsɪz/", "giấy cam kết tại ngoại trước tòa"),
]

with open("scratch/b35_r09_raw_p1.json") as f:
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

with open("scratch/b35_r09_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r09_p1.json OK")
