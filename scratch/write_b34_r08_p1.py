import json

items = [
    ("068503", "diovans", "noun", "/ˈdaɪəˌvænz/", "thuốc hạ huyết áp Diovan"),
    ("068504", "dunkerses", "noun", "/ˈdʌŋkərzɪz/", "giáo phái Rửa tội Ngụp nước Đức"),
    ("068505", "egerias", "noun", "/ɪˈdʒɪriəz/", "cây rong thủy sinh chi Egeria"),
    ("068506", "endemisms", "noun", "/ˈɛndəˌmɪzəmz/", "tính đặc hữu chỉ có tại một vùng"),
    ("068507", "entrained", "verb", "/ɪnˈtreɪnd/", "đã lên tàu hỏa; đã cuốn kéo theo"),
    ("068508", "entraining", "verb", "/ɪnˈtreɪnɪŋ/", "đang lên tàu; cuốn kéo dòng chảy"),
    ("068509", "entrains", "verb", "/ɪnˈtreɪnz/", "lên tàu hỏa; cuốn trôi kéo theo"),
    ("068510", "exegetes", "noun", "/ˌɛksɪˈdʒiːts/", "học giả chú giải Kinh Thánh cổ văn"),
    ("068511", "externalizations", "noun", "/ɪkˌstɜːrnəlaɪˈzeɪʃənz/", "sự ngoại hiện hóa quy cho bên ngoài"),
    ("068512", "fabaceaes", "noun", "/fəˈbeɪʃiz/", "họ Đậu thực vật quả giáp Fabaceae"),
    ("068513", "facers", "noun", "/ˈfeɪsərz/", "tình huống bất ngờ khó khăn (lóng)"),
    ("068514", "finnics", "noun", "/ˈfɪnɪks/", "nhóm ngôn ngữ Finnic Phần Lan"),
    ("068515", "firebreaks", "noun", "/ˈfaɪərˌbreɪks/", "đường băng trắng cản cháy rừng"),
    ("068516", "fogeys", "noun", "/ˈfoʊɡiz/", "ông lão cổ hủ bảo thủ lỗi thời"),
    ("068517", "fustier", "adj", "/ˈfʌstiər/", "ẩm mốc hôi hám hơn; cổ hủ hơn"),
    ("068518", "fustiest", "adj", "/ˈfʌstiɪst/", "ẩm mốc hôi hám nhất; cổ hủ nhất"),
    ("068519", "gasometers", "noun", "/ɡæˈsɒmɪtərz/", "bình chứa khí ga lớn; đồng hồ ga"),
    ("068520", "goitres", "noun", "/ˈɡɔɪtərz/", "bệnh bướu cổ phì đại tuyến giáp"),
    ("068521", "grainings", "noun", "/ˈɡreɪnɪŋz/", "kỹ thuật sơn vẽ tạo vân gỗ giả"),
    ("068522", "guardrooms", "noun", "/ˈɡɑːrdˌruːmz/", "phòng trực gác; phòng giam lính"),
    ("068523", "hemodynamicses", "noun", "/ˌhiːmoʊdaɪˈnæmɪksɪz/", "huyết động lực học tuần hoàn máu"),
    ("068524", "heptanes", "noun", "/ˈhɛpˌteɪnz/", "hyđrocacbon lỏng bảy cacbon heptan"),
    ("068525", "highroads", "noun", "/ˈhaɪˌroʊdz/", "đường cái lớn trục giao thông"),
    ("068526", "hilums", "noun", "/ˈhaɪləmz/", "rốn cơ quan nơi mạch máu đi vào"),
    ("068527", "homileticses", "noun", "/ˌhɒmɪˈlɛtɪksɪz/", "nghệ thuật thuyết giáo giảng đạo"),
    ("068528", "horseheads", "noun", "/ˈhɔːrsˌhɛdz/", "cá mặt trăng Atlantic; đầu ngựa"),
    ("068529", "hysteroscopies", "noun", "/ˌhɪstəˈrɒskəpiz/", "thủ thuật nội soi buồng tử cung"),
    ("068530", "imponderables", "noun", "/ɪmˈpɒndərəbəlz/", "yếu tố khó lường không thể đo đếm"),
    ("068531", "inderals", "noun", "/ˈɪndərɔːlz/", "thuốc chẹn beta trị tim Inderal"),
    ("068532", "inspirers", "noun", "/ɪnˈspaɪərərz/", "người truyền cảm hứng sáng tạo"),
    ("068533", "internalisations", "noun", "/ɪnˌtɜːrnəlaɪˈzeɪʃənz/", "quá trình nội tâm hóa tiếp thu"),
    ("068534", "iseres", "noun", "/iːˈzɛərz/", "sông Isère chảy ở đông nam Pháp"),
    ("068535", "jinn", "noun", "/dʒɪn/", "thần linh siêu nhiên Jinn Ả Rập"),
    ("068536", "kirpans", "noun", "/kɪərˈpɑːnz/", "dao găm nghi lễ truyền thống Sikh"),
    ("068537", "koopmanses", "noun", "/ˈkoʊpmɑːnsɪz/", "nhà kinh tế học Nobel T. Koopmans"),
    ("068538", "lacquerwares", "noun", "/ˈlækərˌwɛərz/", "đồ thủ công mỹ nghệ sơn mài"),
    ("068539", "lambastes", "verb", "/læmˈbeɪsts/", "chỉ trích gay gắt; đánh đập mạnh"),
    ("068540", "lambchops", "noun", "/ˈlæmˌtʃɒps/", "miếng sườn cốt lết thịt cừu non"),
    ("068541", "laminarias", "noun", "/ˌlæmɪˈnɛəriəz/", "tảo bẹ biển nâu thuộc chi Laminaria"),
    ("068542", "lignums", "noun", "/ˈlɪɡnəmz/", "mô gỗ cứng; gỗ cây linh sam cứng"),
    ("068543", "linalools", "noun", "/lɪˈnælɔːlz/", "hương liệu thơm tự nhiên linalol"),
    ("068544", "lineaments", "noun", "/ˈlɪniəmənts/", "nét mặt đặc trưng đường nét dáng"),
    ("068545", "linums", "noun", "/ˈlaɪnəmz/", "cây lanh lấy sợi thuộc chi Linum"),
    ("068546", "lividities", "noun", "/lɪˈvɪdɪtiz/", "vết bầm tím tái; cơn giận tím mặt"),
    ("068547", "lobectomies", "noun", "/loʊˈbɛktəmiz/", "ca phẫu thuật cắt bỏ một thùy tạng"),
    ("068548", "mavins", "noun", "/ˈmeɪvənz/", "chuyên gia bậc thầy sành sỏi (Mỹ)"),
    ("068549", "maximisations", "noun", "/ˌmæksɪmaɪˈzeɪʃənz/", "sự tối đa hóa tăng lên cực đại"),
    ("068550", "mayennes", "noun", "/maɪˈɛnz/", "sông hoặc tỉnh Mayenne của Pháp"),
    ("068551", "momoses", "noun", "/ˈmoʊməsɪz/", "thần châm biếm Momus Hy Lạp cổ"),
    ("068552", "moonflowers", "noun", "/ˈmuːnˌflaʊərz/", "hoa bìm bìm đêm nở hoa trắng thơm"),
    ("068553", "mosaicisms", "noun", "/moʊˈzeɪɪˌsɪzəmz/", "hiện tượng thể khảm di truyền"),
    ("068554", "mynas", "noun", "/ˈmaɪnəz/", "chim sáo đen biết nhại tiếng người"),
    ("068555", "mytiluses", "noun", "/ˈmɪtɪləsɪz/", "con vẹm biển thuộc chi Mytilus"),
    ("068556", "nenetses", "noun", "/ˈnɛnɪtsɪz/", "người và tiếng Nenets vùng Bắc Cực"),
    ("068557", "nigeriens", "noun", "/niːˈʒɛriənz/", "người dân nước Cộng hòa Niger"),
    ("068558", "nonsuches", "noun", "/ˈnʌnˌsʌtʃɪz/", "người hoặc vật xuất chúng vô song"),
    ("068559", "nudibranches", "noun", "/ˈnjuːdɪˌbræŋks/", "sên biển trần màu sắc rực rỡ"),
    ("068560", "ortolans", "noun", "/ˈɔːrtələnz/", "chim sẻ đồng ortolan ăn thịt (Pháp)"),
    ("068561", "oximes", "noun", "/ˈɒksiːmz/", "hợp chất hữu cơ hóa học oxim"),
    ("068562", "oystercatchers", "noun", "/ˈɔɪstərˌkætʃərz/", "chim mò sò mỏ đỏ dài ven biển"),
    ("068563", "papains", "noun", "/pəˈpeɪɪnz/", "enzym phân giải đạm papain đu đủ"),
    ("068564", "paunchier", "adj", "/ˈpɔːntʃiər/", "bụng phệ to béo hơn"),
    ("068565", "paunchiest", "adj", "/ˈpɔːntʃiɪst/", "bụng phệ to béo nhất"),
    ("068566", "plavixes", "noun", "/ˈplævɪksɪz/", "thuốc chống đông máu Plavix"),
    ("068567", "polyelectrolytes", "noun", "/ˌpɒliɪˈlɛktrəˌlaɪts/", "polyme điện ly đa điện tích"),
    ("068568", "potshots", "noun", "/ˈpɒtˌʃɒts/", "phát bắn bừa; lời công kích dễ dãi"),
    ("068569", "priapuses", "noun", "/praɪˈeɪpəsɪz/", "thần sinh sôi Priapus Hy Lạp"),
    ("068570", "probenecids", "noun", "/proʊˈbɛnəsɪdz/", "thuốc trị bệnh gút probenecid"),
    ("068571", "prosopises", "noun", "/prɒˈsoʊpɪsɪz/", "cây mesquite sa mạc chi Prosopis"),
    ("068572", "psalmodies", "noun", "/ˈsɑːlmədiz/", "nghệ thuật hát thánh vịnh nhà thờ"),
    ("068573", "pythiums", "noun", "/ˈpɪθiəmz/", "nấm thủy sinh gây thối rễ Pythium"),
    ("068574", "radiobiologies", "noun", "/ˌreɪdioʊbaɪˈɒlədʒiz/", "ngành sinh học phóng xạ"),
    ("068575", "rinderpests", "noun", "/ˈrɪndərˌpɛsts/", "bệnh dịch tả trâu bò đã thanh toán"),
    ("068576", "rodentias", "noun", "/roʊˈdɛnʃəz/", "bộ Gặm nhấm gồm chuột sóc hải ly"),
    ("068577", "ruandas", "noun", "/ruːˈɑːndəz/", "nước Cộng hòa Rwanda (tên cũ)"),
    ("068578", "safecrackers", "noun", "/ˈseɪfˌkrækərz/", "tên trộm chuyên phá mở két sắt"),
    ("068579", "saliencies", "noun", "/ˈseɪliənsiz/", "đặc điểm nổi bật gây chú ý nhất"),
    ("068580", "sangays", "noun", "/sɑːŋˈɡaɪz/", "núi lửa Sangay ở Ecuador"),
    ("068581", "shaabans", "noun", "/ʃɑːˈbɑːnz/", "tháng thứ tám Sha'ban lịch Hồi"),
    ("068582", "shiisms", "noun", "/ˈʃiːɪzəmz/", "nhánh Hồi giáo Shia (tư tưởng)"),
    ("068583", "shintoisms", "noun", "/ˈʃɪntoʊˌɪzəmz/", "Thần đạo bản địa của Nhật Bản"),
    ("068584", "siskins", "noun", "/ˈsɪskɪnz/", "chim sẻ thông nhỏ màu vàng lục"),
    ("068585", "snowfields", "noun", "/ˈsnoʊˌfiːldz/", "cánh đồng tuyết phủ quanh năm"),
    ("068586", "spiritednesses", "noun", "/ˈspɪrɪtɪdnəsɪz/", "tinh thần sôi nổi nhiệt huyết hăng"),
    ("068587", "squealers", "noun", "/ˈskwiːlərz/", "kẻ chỉ điểm mật báo; lợn kêu éc éc"),
    ("068588", "stickled", "verb", "/ˈstɪkəld/", "đã khăng khăng bắt bẻ chi tiết nhỏ"),
    ("068589", "stickles", "verb", "/ˈstɪkəlz/", "khăng khăng đòi đúng tiểu tiết"),
    ("068590", "stickling", "verb", "/ˈstɪklɪŋ/", "đang khăng khăng bắt bẻ quy tắc"),
    ("068591", "streamliners", "noun", "/ˈstriːmˌlaɪnərz/", "tàu hỏa hoặc xe thiết kế khí động"),
    ("068592", "thessalians", "noun", "/θɛˈseɪliənz/", "người dân vùng Thessaly Hy Lạp"),
    ("068593", "tomatillos", "noun", "/ˌtɒməˈtiːoʊz/", "cà chua lồng đèn xanh Mexico"),
    ("068594", "toradols", "noun", "/ˈtɔːrəˌdɒlz/", "thuốc giảm đau mạnh Toradol"),
    ("068595", "transcaucasias", "noun", "/ˌtrænzkɔːˈkeɪʒəz/", "khu vực Ngoại Kavkaz Nam Kavkaz"),
    ("068596", "tzaras", "noun", "/ˈtsɑːrəz/", "nhà thơ Dada Tristan Tzara"),
    ("068597", "underbidding", "verb", "/ˌʌndərˈbɪdɪŋ/", "đang bỏ giá thấp hơn đối thủ"),
    ("068598", "underbids", "verb", "/ˌʌndərˈbɪdz/", "trả giá hoặc bỏ thầu thấp hơn"),
    ("068599", "unitards", "noun", "/ˈjuːnɪˌtɑːrdz/", "đồ tập bó sát toàn thân liền mảnh"),
    ("068600", "valedictions", "noun", "/ˌvælɪˈdɪkʃənz/", "diễn văn hoặc lời chào từ biệt"),
    ("068601", "weepers", "noun", "/ˈwiːpərz/", "người khóc thương; người khóc thuê"),
    ("068602", "wurzburgs", "noun", "/ˈvʊrtsˌbɜːrɡz/", "thành phố Würzburg ở Đức"),
]

with open("scratch/b34_r08_raw_p1.json") as f:
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

with open("scratch/b34_r08_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r08_p1.json OK")
