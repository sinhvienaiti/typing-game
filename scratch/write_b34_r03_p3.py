import json

items = [
    ("066203", "nasebies", "noun", "/ˈneɪzbiz/", "trận đánh Naseby Nội chiến Anh"),
    ("066204", "oligos", "noun", "/ˈɒlɪˌɡoʊz/", "chuỗi ngắn axit nucleic hoặc đường"),
    ("066205", "pamphleteers", "noun", "/ˌpæmfləˈtɪərz/", "người viết sách mỏng tuyên truyền"),
    ("066206", "peptidases", "noun", "/ˈpɛptɪˌdeɪsɪz/", "enzym thủy phân liên kết peptit"),
    ("066207", "percherons", "noun", "/ˈpɜːrtʃəˌrɒnz/", "giống ngựa kéo to khỏe Percheron"),
    ("066208", "perquisites", "noun", "/ˈpɜːrkwəzɪts/", "bổng lộc phụ cấp ngoài lương"),
    ("066209", "petroglyphs", "noun", "/ˈpɛtrəˌɡlɪfs/", "hình chạm khắc đá thời tiền sử"),
    ("066210", "phonations", "noun", "/foʊˈneɪʃənz/", "sự phát âm rung dây thanh quản"),
    ("066211", "pintles", "noun", "/ˈpɪntəlz/", "chốt bản lề xoay bánh lái tàu"),
    ("066212", "planchets", "noun", "/ˈplæntʃɪts/", "phôi kim loại tròn để dập tiền xu"),
    ("066213", "playsuits", "noun", "/ˈpleɪˌsuːts/", "bộ quần áo liền dạo chơi"),
    ("066214", "prags", "noun", "/prɑːɡz/", "thành phố Praha (cách viết Prag)"),
    ("066215", "pressurised", "verb", "/ˈprɛʃəˌraɪzd/", "đã điều áp; đã tạo áp suất cao"),
    ("066216", "pyridoxines", "noun", "/ˌpɪrɪˈdɒksiːnz/", "vitamin B6 dạng pyridoxin"),
    ("066217", "quartics", "noun", "/ˈkwɔːrtɪks/", "phương trình hoặc đường bậc bốn"),
    ("066218", "recessionals", "noun", "/rɪˈsɛʃənəlz/", "bài thánh ca kết thúc buổi lễ"),
    ("066219", "reckoners", "noun", "/ˈrɛkənərz/", "người tính toán; bảng tính nhanh"),
    ("066220", "reconditioned", "verb", "/ˌriːkənˈdɪʃənd/", "đã tân trang phục hồi như mới"),
    ("066221", "reconditioning", "verb", "/ˌriːkənˈdɪʃənɪŋ/", "đang tân trang sửa chữa phục hồi"),
    ("066222", "reconditions", "verb", "/ˌriːkənˈdɪʃənz/", "tân trang phục hồi máy móc cũ"),
    ("066223", "repechages", "noun", "/ˌrɛpəˈʃɑːʒɪz/", "vòng đấu vớt tranh huy chương"),
    ("066224", "ricers", "noun", "/ˈraɪsərz/", "dụng cụ ép nghiền nhuyễn khoai tây"),
    ("066225", "rickovers", "noun", "/ˈrɪkˌoʊvərz/", "đô đốc Mỹ Hyman G. Rickover"),
    ("066226", "sargassums", "noun", "/sɑːrˈɡæsəmz/", "rong mơ trôi nổi vùng biển ấm"),
    ("066227", "sauterneses", "noun", "/soʊˈtɜːrnɪz/", "rượu vang ngọt trắng Sauternes"),
    ("066228", "scatterguns", "noun", "/ˈskætərˌɡʌnz/", "súng săn bắn đạn chùm"),
    ("066229", "schmoes", "noun", "/ʃmoʊz/", "anh chàng khờ khạo (khẩu ngữ)"),
    ("066230", "shinas", "noun", "/ˈʃiːnəz/", "ngôn ngữ Shina ở bắc Pakistan"),
    ("066231", "shopfronts", "noun", "/ˈʃɒpˌfrʌnts/", "mặt tiền cửa hàng trưng bày"),
    ("066232", "silkwoods", "noun", "/ˈsɪlkˌwʊdz/", "cây gỗ lá mượt silkwood Úc"),
    ("066233", "snoods", "noun", "/snuːdz/", "lưới trùm tóc; khăn ống quàng cổ"),
    ("066234", "sticklebacks", "noun", "/ˈstɪkəlˌbæks/", "cá gai nhỏ sống nước ngọt mặn"),
    ("066235", "stockfishes", "noun", "/ˈstɒkˌfɪʃɪz/", "cá tuyết phơi khô không ướp muối"),
    ("066236", "stockists", "noun", "/ˈstɒkɪsts/", "đại lý phân phối giữ hàng tồn kho"),
    ("066237", "strongboxes", "noun", "/ˈstrɒŋˌbɒksɪz/", "két sắt nhỏ; rương khóa đựng tiền"),
    ("066238", "subdirectories", "noun", "/ˌsʌbdəˈrɛktəriz/", "thư mục con trong hệ thống tệp"),
    ("066239", "superstrings", "noun", "/ˈsuːpərˌstrɪŋz/", "siêu dây lý thuyết vật lý cơ bản"),
    ("066240", "sutlers", "noun", "/ˈsʌtlərz/", "người bán hàng đi theo quân đội"),
    ("066241", "tarantellas", "noun", "/ˌtærənˈtɛləz/", "điệu nhảy tarantella miền Nam Ý"),
    ("066242", "thermospheres", "noun", "/ˈθɜːrməˌsfɪərz/", "tầng nhiệt trong khí quyển Trái Đất"),
    ("066243", "toughies", "noun", "/ˈtʌfiz/", "tên côn đồ hung hãn; bài toán khó"),
    ("066244", "traves", "noun", "/treɪvz/", "xà ngang; khung giữ ngựa đóng móng"),
    ("066245", "trotskyisms", "noun", "/ˈtrɒtskiˌɪzəmz/", "học thuyết chính trị Trotskyism"),
    ("066246", "ultraconservatives", "noun", "/ˌʌltrəkənˈsɜːrvətɪvz/", "người theo quan điểm cực kỳ bảo thủ"),
    ("066247", "urates", "noun", "/ˈjʊəreɪts/", "muối urat của axit uric"),
    ("066248", "ureys", "noun", "/ˈjʊəriz/", "nhà hóa học Nobel Harold Urey"),
    ("066249", "venturers", "noun", "/ˈvɛntʃərərz/", "người mạo hiểm khởi nghiệp đầu tư"),
    ("066250", "whippersnappers", "noun", "/ˈwɪpərˌsnæpərz/", "nhóc con ngạo mạn; kẻ trẻ người non"),
    ("066251", "zimbalists", "noun", "/ˈzɪmbəlɪsts/", "nghệ sĩ vĩ cầm Efrem Zimbalist"),
    ("066252", "alben barkley", "phrase", "/ˈælbən ˈbɑːrkli/", "Phó Tổng thống Mỹ Alben Barkley"),
    ("066253", "alben william barkley", "phrase", "/ˈælbən ˈwɪljəm ˈbɑːrkli/", "chính khách Mỹ Alben W. Barkley"),
    ("066254", "alizarin crimson", "phrase", "/əˈlɪzərɪn ˈkrɪmzən/", "chất màu đỏ thắm alizarin"),
    ("066255", "alizarin red", "phrase", "/əˈlɪzərɪn rɛd/", "thuốc nhuộm đỏ tươi alizarin"),
    ("066256", "alizarin yellow", "phrase", "/əˈlɪzərɪn ˈjɛloʊ/", "chất chỉ thị màu vàng alizarin"),
    ("066257", "alnus maritima", "phrase", "/ˈælnəs məˈrɪtɪmə/", "cây tống quán sủ ven biển Bắc Mỹ"),
    ("066258", "annelid worm", "phrase", "/ˈænəlɪd wɜːrm/", "giun đốt thân phân nhiều đốt"),
    ("066259", "arthur honegger", "phrase", "/ˈɑːrθər ˈhɒnɪɡər/", "nhà soạn nhạc Thụy Sĩ Honegger"),
    ("066260", "battle of tannenberg", "phrase", "/ˈbætəl əv ˈtænənˌbɜːrɡ/", "trận chiến lịch sử Tannenberg"),
    ("066261", "beet armyworm", "phrase", "/biːt ˈɑːrmiˌwɜːrm/", "sâu xanh da láng hại củ cải"),
    ("066262", "ben shahn", "phrase", "/bɛn ʃɑːn/", "họa sĩ hiện thực Mỹ Ben Shahn"),
    ("066263", "benjamin shahn", "phrase", "/ˈbɛndʒəmɪn ʃɑːn/", "họa sĩ Mỹ Benjamin Shahn"),
    ("066264", "cascara sagrada", "phrase", "/kæˈskɛərə səˈɡrɑːdə/", "vỏ cây cascara dùng làm thuốc xổ"),
    ("066265", "cladistic analysis", "phrase", "/kləˈdɪstɪk əˈnælɪsɪs/", "phân tích phát sinh chủng loại"),
    ("066266", "clifford odets", "phrase", "/ˈklɪfərd oʊˈdɛts/", "nhà viết kịch Mỹ Clifford Odets"),
    ("066267", "coonskin cap", "phrase", "/ˈkuːnskɪn kæp/", "mũ lông gấu mèo có đuôi rủ"),
    ("066268", "crataegus mollis", "phrase", "/krəˈtiːɡəs ˈmɒlɪs/", "cây táo gai lông mịn Bắc Mỹ"),
    ("066269", "cucurbita maxima", "phrase", "/kjuːˈkɜːrbɪtə ˈmæksɪmə/", "cây bí đỏ bí ngô lớn"),
    ("066270", "deltoid tuberosity", "phrase", "/ˈdɛltɔɪd ˌtuːbəˈrɒsɪti/", "lồi củ cơ delta trên xương cánh tay"),
    ("066271", "dianthus chinensis", "phrase", "/daɪˈænθəs tʃaɪˈnɛnsɪs/", "cây cẩm chướng Trung Quốc"),
    ("066272", "flannel mullein", "phrase", "/ˈflænəl ˈmʌlɪn/", "cây nhung thảo lá dày như vải nỉ"),
    ("066273", "frederick james furnivall", "phrase", "/ˈfrɛdrɪk dʒeɪmz ˈfɜːrnɪˌvɔːl/", "học giả ngữ văn Anh Furnivall"),
    ("066274", "genus anomia", "phrase", "/ˈdʒiːnəs əˈnoʊmiə/", "chi sò vỏ mỏng Anomia"),
    ("066275", "genus euterpe", "phrase", "/ˈdʒiːnəs juːˈtɜːrpi/", "chi cây cọ açaí Euterpe"),
    ("066276", "genus kalmia", "phrase", "/ˈdʒiːnəs ˈkælmiə/", "chi cây nguyệt quế núi Kalmia"),
    ("066277", "genus lactuca", "phrase", "/ˈdʒiːnəs ˈlæktjʊkə/", "chi rau diếp xà lách Lactuca"),
    ("066278", "genus maranta", "phrase", "/ˈdʒiːnəs məˈræntə/", "chi cây dong riềng cảnh Maranta"),
    ("066279", "genus morone", "phrase", "/ˈdʒiːnəs məˈroʊni/", "chi cá vược ôn đới Morone"),
    ("066280", "genus neurospora", "phrase", "/ˈdʒiːnəs njʊəˈrɒspərə/", "chi nấm mốc bánh mì Neurospora"),
    ("066281", "genus ostrea", "phrase", "/ˈdʒiːnəs ˈɒstriə/", "chi hàu biển dẹt Ostrea"),
    ("066282", "genus pecten", "phrase", "/ˈdʒiːnəs ˈpɛktɛn/", "chi điệp biển vỏ quạt Pecten"),
    ("066283", "genus pisum", "phrase", "/ˈdʒiːnəs ˈpaɪsəm/", "chi đậu Hà Lan Pisum"),
    ("066284", "genus rhizobium", "phrase", "/ˈdʒiːnəs raɪˈzoʊbiəm/", "chi vi khuẩn cố định đạm Rhizobium"),
    ("066285", "genus rudbeckia", "phrase", "/ˈdʒiːnəs rʌdˈbɛkiə/", "chi hoa cúc nón vàng Rudbeckia"),
    ("066286", "genus spiraea", "phrase", "/ˈdʒiːnəs spaɪˈriːə/", "chi cây bụi hoa mơ Spiraea"),
    ("066287", "haemolytic anaemia", "phrase", "/ˌhiːməˈlɪtɪk əˈniːmiə/", "bệnh thiếu máu tan huyết"),
    ("066288", "ipse dixit", "phrase", "/ˈɪpsi ˈdɪksɪt/", "lời khẳng định võ đoán thiếu chứng"),
    ("066289", "isobutyl nitrite", "phrase", "/ˌaɪsoʊˈbjuːtəl ˈnaɪtraɪt/", "hợp chất hữu cơ isobutyl nitrit"),
    ("066290", "jakob boehme", "phrase", "/ˈjɑːkɒp ˈbɜːmə/", "nhà thần bí học Đức Jakob Boehme"),
    ("066291", "japanese medlar", "phrase", "/ˌdʒæpəˈniːz ˈmɛdlər/", "cây tỳ bà Nhật; quả nhót tây Nhật"),
    ("066292", "lathyrus niger", "phrase", "/ˈlæθɪrəs ˈnaɪdʒər/", "cây đậu leo đen châu Âu"),
    ("066293", "medlar tree", "phrase", "/ˈmɛdlər triː/", "cây nhót tây Âu; cây sơn tra Âu"),
    ("066294", "moth mullein", "phrase", "/mɒθ ˈmʌlɪn/", "cây nhung thảo hoa bướm"),
    ("066295", "myotonic dystrophy", "phrase", "/ˌmaɪəˈtɒnɪk ˈdɪstrəfi/", "bệnh loạn dưỡng tăng trương lực cơ"),
    ("066296", "myotonic muscular dystrophy", "phrase", "/ˌmaɪəˈtɒnɪk ˈmʌskjələr ˈdɪstrəfi/", "loạn dưỡng cơ cứng cơ di truyền"),
    ("066297", "neap tide", "phrase", "/niːp taɪd/", "thủy triều kém; con nước ròng yếu"),
    ("066298", "northern phalarope", "phrase", "/ˈnɔːrðərn ˈfæləˌroʊp/", "chim phalarope cổ đỏ phương Bắc"),
    ("066299", "novaya zemlya", "phrase", "/noʊˈvaɪə zɛmˈljɑː/", "quần đảo Novaya Zemlya Bắc Cực"),
    ("066300", "nyssa sylvatica", "phrase", "/ˈnɪsə sɪlˈvætɪkə/", "cây gỗ gôm đen Bắc Mỹ"),
    ("066301", "phaseolus caracalla", "phrase", "/fəˈsiːələs ˌkærəˈkælə/", "cây hoa đậu dây xoắn hình ốc sên"),
    ("066302", "phragmites communis", "phrase", "/fræɡˈmaɪtiːz ˈkɒmjʊnɪs/", "cây lau sậy mọc đầm lầy"),
]

with open("scratch/b34_r03_raw_p3.json") as f:
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

with open("scratch/b34_r03_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r03_p3.json OK")
