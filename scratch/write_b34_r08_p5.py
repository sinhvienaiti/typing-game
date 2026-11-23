import json

items = [
    ("068903", "ghanians", "noun", "/ɡɑːˈniːənz/", "người dân nước Ghana (biến thể)"),
    ("068904", "globules", "noun", "/ˈɡlɒbjuːlz/", "giọt cầu nhỏ; viên hoàn nhỏ (y)"),
    ("068905", "glommed", "verb", "/ɡlɒmd/", "đã chộp lấy; bám chặt; lấy trộm"),
    ("068906", "glomming", "verb", "/ˈɡlɒmɪŋ/", "đang chộp lấy; bám chặt vào"),
    ("068907", "gloms", "verb", "/ɡlɒmz/", "chộp vồ lấy; bám dính vào (lóng)"),
    ("068908", "grandnephews", "noun", "/ˌɡrændˈnɛfjuːz/", "cháu trai gọi bằng ông bà cô chú"),
    ("068909", "hatboxes", "noun", "/ˈhætˌbɒksɪz/", "hộp tròn có nắp bảo quản mũ nón"),
    ("068910", "hatchways", "noun", "/ˈhætʃˌweɪz/", "cửa sập lối lên xuống khoang tàu"),
    ("068911", "henbanes", "noun", "/ˈhɛnˌbeɪnz/", "cây kỳ nham độc dược henbane"),
    ("068912", "heteropteras", "noun", "/ˌhɛtəˈrɒptərəz/", "phân bộ Bọ xít cánh nửa khác nhau"),
    ("068913", "hizbollahs", "noun", "/ˌhɪzbəˈlɑːz/", "tổ chức vũ trang Hezbollah Liban"),
    ("068914", "honkers", "noun", "/ˈhɒŋkərz/", "người bấm còi xe inh ỏi; ngỗng kêu"),
    ("068915", "hymnodies", "noun", "/ˈhɪmnədiz/", "tuyển tập thánh ca; việc hát thánh"),
    ("068916", "hyperopias", "noun", "/ˌhaɪpəˈroʊpiəz/", "tật khúc xạ viễn thị nhìn xa rõ"),
    ("068917", "hypospadiases", "noun", "/ˌhaɪpoʊˈspeɪdiəsɪz/", "dị tật bẩm sinh lỗ tiểu đóng thấp"),
    ("068918", "idealities", "noun", "/ˌaɪdiˈælɪtiz/", "tính chất lý tưởng hoàn mỹ"),
    ("068919", "immobilisations", "noun", "/ɪˌmoʊbɪlaɪˈzeɪʃənz/", "sự cố định khớp gãy; sự phong tỏa"),
    ("068920", "inebriates", "noun", "/ɪˈniːbriəts/", "người say rượu; kẻ nghiện rượu"),
    ("068921", "inebriating", "verb", "/ɪˈniːbriˌeɪtɪŋ/", "đang làm say sưa choáng ngợp ngây"),
    ("068922", "inroads", "noun", "/ˈɪnˌroʊdz/", "bước tiến thâm nhập; cuộc đột kích"),
    ("068923", "jambons", "noun", "/ˈdʒæmbɒnz/", "đùi lợn muối giăm bông (tiếng Pháp)"),
    ("068924", "klinefelters", "noun", "/ˈklaɪnˌfɛltərz/", "bác sĩ Mỹ Harry Klinefelter"),
    ("068925", "knackers", "noun", "/ˈnækərz/", "lò mổ ngựa già; thợ phá dỡ đồ cũ"),
    ("068926", "knishes", "noun", "/kəˈnɪʃɪz/", "bánh nướng nhân khoai thịt Do Thái"),
    ("068927", "langoustines", "noun", "/ˌlæŋɡəˈstiːnz/", "tôm hùm càng mảnh Na Uy"),
    ("068928", "leisters", "noun", "/ˈliːstərz/", "đinh ba chĩa nhọn đâm bắt cá sông"),
    ("068929", "letches", "noun", "/ˈlɛtʃɪz/", "kẻ háo sắc dâm ô biến thái"),
    ("068930", "leukopenias", "noun", "/ˌluːkəˈpiːniəz/", "tình trạng giảm bạch cầu trong máu"),
    ("068931", "livonians", "noun", "/lɪˈvoʊniənz/", "người bản địa vùng Livonia Baltic"),
    ("068932", "lutas", "noun", "/ˈluːtəz/", "đảo Rota thuộc Quần đảo Mariana"),
    ("068933", "lutefisks", "noun", "/ˈluːtəˌfɪsks/", "món cá tuyết khô ngâm kiềm Bắc Âu"),
    ("068934", "machiavellianisms", "noun", "/ˌmækiəˈvɛliənˌɪzəmz/", "thủ đoạn chính trị Machiavelli"),
    ("068935", "manducas", "noun", "/mænˈdjuːkəz/", "chi bướm đêm sâu sừng Manduca"),
    ("068936", "megillahs", "noun", "/məˈɡɪləz/", "cuộn kinh Megillah; chuyện dài dòng"),
    ("068937", "megilloth", "noun", "/məˈɡɪlɒθ/", "năm cuộn kinh Do Thái Megillot"),
    ("068938", "mezuzahs", "noun", "/məˈzʊzəz/", "hộp kinh treo khung cửa Do Thái"),
    ("068939", "mezuzoth", "noun", "/məˈzʊzoʊθ/", "cuộn kinh gắn khung cửa Do Thái"),
    ("068940", "middies", "noun", "/ˈmɪdiz/", "áo thủy thủ cổ rộng; học viên hải"),
    ("068941", "milkers", "noun", "/ˈmɪlkərz/", "bò vắt sữa; máy vắt sữa tự động"),
    ("068942", "monotheists", "noun", "/ˈmɒnoʊˌθiːɪsts/", "tín đồ theo tôn giáo độc thần"),
    ("068943", "nudas", "noun", "/ˈnjuːdəz/", "lớp sứa lược biển không xúc tu"),
    ("068944", "obbligatos", "noun", "/ˌɒblɪˈɡɑːtoʊz/", "bè nhạc đệm bắt buộc không thể bỏ"),
    ("068945", "odoacers", "noun", "/ˌoʊdoʊˈeɪsərz/", "vua Đức Odoacer lật đổ Tây La Mã"),
    ("068946", "osteoclasts", "noun", "/ˈɒstioʊˌklæsts/", "tế bào hủy xương tái hấp thu mô"),
    ("068947", "packmans", "noun", "/ˈpækmənz/", "người bán hàng rong mang gánh (cổ)"),
    ("068948", "parmelias", "noun", "/pɑːrˈmiːliəz/", "địa y tán lá bám đá chi Parmelia"),
    ("068949", "passifloras", "noun", "/ˌpæsɪˈflɔːrəz/", "cây chanh dây lạc tiên Passiflora"),
    ("068950", "pasters", "noun", "/ˈpeɪstərz/", "thợ dán giấy tường; dải băng dán"),
    ("068951", "patases", "noun", "/ˈpɑːtəsɪz/", "khỉ patas chạy nhanh ở châu Phi"),
    ("068952", "penlights", "noun", "/ˈpɛnˌlaɪts/", "đèn pin nhỏ hình cây bút khám bệnh"),
    ("068953", "pentoxides", "noun", "/pɛnˈtɒksaɪdz/", "hợp chất hóa học năm nguyên tử oxy"),
    ("068954", "perillas", "noun", "/pəˈrɪləz/", "cây tía tô; cây é tía chi Perilla"),
    ("068955", "planchettes", "noun", "/plɑːnˈʃɛts/", "tấm gỗ trái tim di chuyển cầu cơ"),
    ("068956", "polytheists", "noun", "/ˈpɒliˌθiːɪsts/", "người theo tín ngưỡng đa thần"),
    ("068957", "popularisations", "noun", "/ˌpɒpjələraɪˈzeɪʃənz/", "sự phổ biến đại chúng hóa kiến thức"),
    ("068958", "potboilers", "noun", "/ˈpɒtˌbɔɪlərz/", "tác phẩm viết vội chỉ để kiếm tiền"),
    ("068959", "quaestors", "noun", "/ˈkwiːstərz/", "quan coi kho bạc tài chính La Mã"),
    ("068960", "rastases", "noun", "/ˈrɑːstəz/", "tín đồ phong trào Rastafari Jamaica"),
    ("068961", "sandblasted", "verb", "/ˈsændˌblæstɪd/", "đã phun cát áp lực làm sạch bề mặt"),
    ("068962", "sandblasting", "verb", "/ˈsændˌblæstɪŋ/", "đang phun cát tẩy gỉ bề mặt kim"),
    ("068963", "sandblasts", "noun", "/ˈsændˌblæsts/", "cơn bão cát thổi mạnh; vòi phun cát"),
    ("068964", "sensoriums", "noun", "/sɛnˈsɔːriəmz/", "trung khu tiếp nhận cảm giác não"),
    ("068965", "sketchers", "noun", "/ˈskɛtʃərz/", "người vẽ phác thảo ký họa nhanh"),
    ("068966", "spectroscopes", "noun", "/ˈspɛktrəˌskoʊps/", "kính quang phổ phân tích ánh sáng"),
    ("068967", "stylets", "noun", "/ˈstaɪlɪts/", "que thăm phẫu thuật mảnh; vòi chích"),
    ("068968", "tamals", "noun", "/təˈmɑːlz/", "bánh bột ngô hấp lá chuối tamal"),
    ("068969", "telemanns", "noun", "/ˈtɛləmɑːnz/", "nhà soạn nhạc Đức G. P. Telemann"),
    ("068970", "thrombectomies", "noun", "/ˌθrɒmˈbɛktəmiz/", "phẫu thuật lấy bỏ cục huyết khối"),
    ("068971", "toroids", "noun", "/ˈtɔːrɔɪdz/", "hình vòng xuyến; lõi cuộn xuyến"),
    ("068972", "towlines", "noun", "/ˈtoʊˌlaɪnz/", "dây cáp kéo tàu xe trượt nước"),
    ("068973", "trichopteras", "noun", "/trɪˈkɒptərəz/", "bộ Cánh lông bướm nước Trichoptera"),
    ("068974", "trillionths", "noun", "/ˈtrɪljənθs/", "phân số một phần nghìn tỷ"),
    ("068975", "tropisms", "noun", "/ˈtroʊpɪzəmz/", "tính hướng động quay về kích thích"),
    ("068976", "turgots", "noun", "/tʊərˈɡoʊz/", "nhà kinh tế học Pháp Turgot"),
    ("068977", "tweezed", "verb", "/twiːzd/", "đã nhổ tỉa lông bằng cái nhíp"),
    ("068978", "tweezes", "verb", "/ˈtwiːzɪz/", "nhổ kẹp gắp vật nhỏ bằng nhíp"),
    ("068979", "tweezing", "verb", "/ˈtwiːzɪŋ/", "đang nhổ tỉa bằng nhíp nhỏ"),
    ("068980", "unclipping", "verb", "/ʌnˈklɪpɪŋ/", "đang tháo mở kẹp ghim hoặc móc"),
    ("068981", "unclips", "verb", "/ʌnˈklɪps/", "tháo bật mở kẹp giữ hoặc khóa cài"),
    ("068982", "visayans", "noun", "/vɪˈsaɪənz/", "người và tiếng Visaya Philippines"),
    ("068983", "welchers", "noun", "/ˈwɛltʃərz/", "kẻ quỵt nợ cá cược lật lọng (lóng)"),
    ("068984", "xerostomias", "noun", "/ˌzɪərəˈstoʊmiəz/", "chứng khô miệng do thiếu nước bọt"),
    ("068985", "yastrzemskis", "noun", "/jəˈstrɛmskiz/", "cầu thủ bóng chày C. Yastrzemski"),
    ("068986", "yquems", "noun", "/iːˈkɛmz/", "rượu vang trắng ngọt Château Yquem"),
    ("068987", "afterworlds", "noun", "/ˈæftərˌwɜːrldz/", "thế giới bên kia sau khi chết"),
    ("068988", "alyssums", "noun", "/əˈlɪsəmz/", "hoa thảm nhỏ thơm ngọt chi Alyssum"),
    ("068989", "argives", "noun", "/ˈɑːrɡaɪvz/", "người thành Argos; quân Hy Lạp cổ"),
    ("068990", "arthralgias", "noun", "/ɑːrˈθrældʒəz/", "chứng đau nhức khớp xương"),
    ("068991", "arthropodas", "noun", "/ɑːrˈθrɒpədəz/", "ngành Chân khớp gồm côn trùng nhện"),
    ("068992", "asafoetidas", "noun", "/ˌæsəˈfɛtɪdəz/", "nhựa gia vị mùi hăng a ngụy"),
    ("068993", "asthenospheres", "noun", "/æsˈθiːnəˌsfɪərz/", "quyển mềm nằm dưới thạch quyển"),
    ("068994", "autografts", "noun", "/ˈɔːtəˌɡræfts/", "mô ghép tự thân của chính bệnh nhân"),
    ("068995", "avestans", "noun", "/əˈvɛstənz/", "ngôn ngữ cổ Avesta kinh Hỏa giáo"),
    ("068996", "bankias", "noun", "/ˈbæŋkiəz/", "con hà biển khổng lồ đục gỗ tàu"),
    ("068997", "basothos", "noun", "/bəˈsuːtuːz/", "người dân tộc Sotho ở Lesotho"),
    ("068998", "blepharitides", "noun", "/ˌblɛfərɪˈtaɪdiːz/", "bệnh viêm bờ mi mắt sưng đỏ"),
    ("068999", "bosies", "noun", "/ˈboʊziz/", "bóng xoáy ngược trong môn cricket"),
    ("069000", "braceros", "noun", "/brəˈsɛəroʊz/", "công nhân thời vụ Mexico sang Mỹ"),
    ("069001", "cagoules", "noun", "/kəˈɡuːlz/", "áo khoác gió đi mưa nhẹ có mũ trùm"),
    ("069002", "calked", "verb", "/kɔːkt/", "đã xảm kín khe tàu; đóng đinh móng"),
]

with open("scratch/b34_r08_raw_p5.json") as f:
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

with open("scratch/b34_r08_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r08_p5.json OK")
