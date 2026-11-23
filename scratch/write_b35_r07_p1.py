import json

items = [
    ("073003", "gaillardias", "noun", "/ɡeɪˈlɑːrdiəz/", "hoa cúc mâm xôi Gaillardia"),
    ("073004", "galagos", "noun", "/ɡəˈleɪɡoʊz/", "vượn cáo bụi đêm châu Phi galago"),
    ("073005", "gemfibrozils", "noun", "/dʒɛmˈfaɪbrəzɪlz/", "thuốc hạ mỡ máu gemfibrozil"),
    ("073006", "gravimetries", "noun", "/ɡræˈvɪmɪtriz/", "phép phân tích trọng lượng (hóa)"),
    ("073007", "greasewoods", "noun", "/ˈɡriːsˌwʊdz/", "cây bụi đất kiềm vùng khô Mỹ"),
    ("073008", "groundspeeds", "noun", "/ˈɡraʊndˌspiːdz/", "tốc độ máy bay so với mặt đất"),
    ("073009", "gspcs", "noun", "/ˌdʒiː ɛs piː ˈsiːz/", "tổ chức vũ trang Hồi giáo GSPC"),
    ("073010", "halabs", "noun", "/ˈhælæbz/", "thành phố Aleppo (Halab Syria)"),
    ("073011", "hamartias", "noun", "/ˌhɑːmɑːrˈtiːəz/", "khuyết điểm bi kịch nhân vật (văn)"),
    ("073012", "helminthics", "noun", "/hɛlˈmɪnθɪks/", "thuốc tẩy giun sán ký sinh"),
    ("073013", "helots", "noun", "/ˈhɛləts/", "nông nô nô lệ Sparta cổ đại"),
    ("073014", "honkytonks", "noun", "/ˈhɒŋkiˌtɒŋks/", "quán bar nhạc đồng quê bình dân"),
    ("073015", "hyoscyamines", "noun", "/ˌhaɪəˈsaɪəmiːnz/", "chất chống co thắt hyoscyamine"),
    ("073016", "hypernatremias", "noun", "/ˌhaɪpərnəˈtriːmiəz/", "tình trạng tăng natri trong máu"),
    ("073017", "innocencies", "noun", "/ˈɪnəsənsiz/", "sự ngây thơ trong sáng vô tội"),
    ("073018", "isopodas", "noun", "/aɪˈsɒpədəz/", "bộ Chân đều (con rận gỗ, rận biển)"),
    ("073019", "jiddahs", "noun", "/ˈdʒɪdəz/", "thành phố cảng Jeddah Ả Rập Xê Út"),
    ("073020", "khoikhois", "noun", "/ˈkɔɪˌkɔɪz/", "người và ngôn ngữ Khoikhoi Nam Phi"),
    ("073021", "lamisils", "noun", "/ˈlæmɪsɪlz/", "thuốc kháng nấm da Lamisil"),
    ("073022", "lepidolites", "noun", "/lɛˈpɪdəˌlaɪts/", "khoáng vật mica tím chứa liti"),
    ("073023", "liliuokalanis", "noun", "/lɪˌliːuːoʊkəˈlɑːniz/", "nữ hoàng Hawaii Liliuokalani"),
    ("073024", "lingcods", "noun", "/ˈlɪŋˌkɒdz/", "cá tuyết xanh Thái Bình Dương"),
    ("073025", "linnaeas", "noun", "/lɪˈniːəz/", "cây hoa chuông đôi phương bắc"),
    ("073026", "lunules", "noun", "/ˈluːnjuːlz/", "vùng trăng lưỡi liềm gốc móng tay"),
    ("073027", "mahdists", "noun", "/ˈmɑːdɪsts/", "tín đồ phong trào Mahdi ở Sudan"),
    ("073028", "mainsheets", "noun", "/ˈmeɪnˌʃiːts/", "dây lèo điều khiển buồm chính"),
    ("073029", "mashies", "noun", "/ˈmæʃiz/", "gậy đánh gôn sắt số 5 cổ điển"),
    ("073030", "mercenarias", "noun", "/ˌmɜːrsɪˈnɛəriəz/", "chi Ngao vỏ cứng Đại Tây Dương"),
    ("073031", "mounters", "noun", "/ˈmaʊntərz/", "thợ lắp ráp; người gắn khung ảnh"),
    ("073032", "myrtuses", "noun", "/ˈmɜːrtəsɪz/", "chi Cây sim hương đào Myrtus"),
    ("073033", "neurasthenics", "noun", "/ˌnjʊərəsˈθɛnɪks/", "người mắc chứng suy nhược thần kinh"),
    ("073034", "norethindrones", "noun", "/ˌnɔːrɛˈθɪndroʊnz/", "progestin tổng hợp norethindrone"),
    ("073035", "numeniuses", "noun", "/njʊˈmiːniəsɪz/", "chi Chim choắt mỏ cong (curlew)"),
    ("073036", "ophryses", "noun", "/ˈɒfrɪsɪz/", "chi Hoa lan ong châu Âu (Ophrys)"),
    ("073037", "oreads", "noun", "/ˈɔːriˌædz/", "nữ thần rừng núi Oread Hy Lạp"),
    ("073038", "outcastes", "noun", "/ˈaʊtˌkæsts/", "người ngoài đẳng cấp tiện dân Ấn"),
    ("073039", "panderers", "noun", "/ˈpændərərz/", "kẻ chiều chuộng nịnh bợ; môi giới"),
    ("073040", "paracenteses", "noun", "/ˌpærəsɛnˈtiːsiːz/", "thủ thuật chọc dò hút dịch ổ bụng"),
    ("073041", "pebas", "noun", "/ˈpiːbəz/", "con tatu chín đai ở châu Mỹ"),
    ("073042", "penicillamines", "noun", "/ˌpɛnɪˈsɪləmiːnz/", "thuốc thải đồng penicillamine"),
    ("073043", "percas", "noun", "/ˈpɜːrkəz/", "chi Cá rô sông Á-Âu (Perca)"),
    ("073044", "politicked", "verb", "/ˈpɒlɪˌtɪkt/", "đã vận động tranh cử làm chính trị"),
    ("073045", "politicks", "verb", "/ˈpɒlɪˌtɪks/", "vận động luồn lách chính trị"),
    ("073046", "pravastatins", "noun", "/ˌprævəˈstætɪnz/", "thuốc hạ mỡ máu pravastatin"),
    ("073047", "primidones", "noun", "/ˈprɪmɪˌdoʊnz/", "thuốc chống động kinh primidone"),
    ("073048", "propellents", "noun", "/prəˈpɛlənts/", "nhiên liệu đẩy tên lửa; khí đẩy"),
    ("073049", "propoxyphenes", "noun", "/proʊˈpɒksɪfiːnz/", "thuốc giảm đau opioid propoxyphene"),
    ("073050", "pulexes", "noun", "/ˈpjuːlɛksɪz/", "chi Bọ chét hút máu người (Pulex)"),
    ("073051", "pyas", "noun", "/ˈpjɑːz/", "đơn vị tiền xu pya của Myanmar"),
    ("073052", "pyralidaes", "noun", "/paɪˈrælɪˌdiːz/", "họ Ngài bướm sáp hại ngũ cốc"),
    ("073053", "quadruplets", "noun", "/kwɒˈdruːplɪts/", "ca sinh bốn; bộ bốn giống nhau"),
    ("073054", "radiotelephonies", "noun", "/ˌreɪdioʊtɪˈlɛfəniz/", "hệ thống điện thoại vô tuyến"),
    ("073055", "ryukyuans", "noun", "/riˈuːkjuːənz/", "người và ngôn ngữ quần đảo Ryukyu"),
    ("073056", "salmonidaes", "noun", "/sælˈmɒnɪˌdiːz/", "họ Cá hồi (cá hồi sông và biển)"),
    ("073057", "salvinorins", "noun", "/ˌsælvɪˈnɔːrɪnz/", "hoạt chất gây ảo giác salvinorin"),
    ("073058", "sclerites", "noun", "/ˈsklɛəraɪts/", "mảnh vỏ kitin cứng (chân khớp)"),
    ("073059", "scotswomans", "noun", "/ˈskɒtsˌwʊmənz/", "người phụ nữ xứ Scotland"),
    ("073060", "serviceberries", "noun", "/ˈsɜːrvɪsˌbɛriz/", "cây quả mọng shadbush Bắc Mỹ"),
    ("073061", "sinlessnesses", "noun", "/ˈsɪnləsnəsɪz/", "tính trong sạch không tội lỗi"),
    ("073062", "sirups", "noun", "/ˈsɪrəps/", "nước đường cô đặc xi-rô (biến thể)"),
    ("073063", "sorbians", "noun", "/ˈsɔːrbiənz/", "người dân tộc Sorb ở miền đông Đức"),
    ("073064", "spodumenes", "noun", "/ˈspɒdjʊˌmiːnz/", "khoáng vật quặng liti spodumene"),
    ("073065", "starers", "noun", "/ˈstɛərərz/", "người nhìn chằm chằm không chớp"),
    ("073066", "stellarias", "noun", "/stəˈlɛəriəz/", "cây phồn lâu (cỏ sao chickweed)"),
    ("073067", "stibnites", "noun", "/ˈstɪbnaɪts/", "quặng antimon sunfua stibnit"),
    ("073068", "stroboscopes", "noun", "/ˈstroʊbəˌskoʊps/", "đèn chớp nhấp nháy đo chuyển động"),
    ("073069", "superbias", "noun", "/suːˈpɜːrbiəz/", "tội ngạo mạn kiêu căng (bảy tội)"),
    ("073070", "testaceas", "noun", "/tɛˈsteɪʃəz/", "nhóm Trùng biến hình có vỏ Testacea"),
    ("073071", "thessalonians", "noun", "/ˌθɛsəˈloʊniənz/", "người Tê-sa-lô-ni-ca; thư Tân Ước"),
    ("073072", "tollmans", "noun", "/ˈtoʊlmənz/", "nhân viên thu phí cầu đường"),
    ("073073", "tonometries", "noun", "/toʊˈnɒmɪtriz/", "phép đo nhãn áp mắt hoặc áp lực"),
    ("073074", "trogons", "noun", "/ˈtroʊɡɒnz/", "chim nuốc lông sặc sỡ nhiệt đới"),
    ("073075", "uhlands", "noun", "/ˈuːlændz/", "thi sĩ Đức Ludwig Uhland"),
    ("073076", "underexposures", "noun", "/ˌʌndərɪkˈspoʊʒərz/", "tình trạng chụp ảnh thiếu sáng"),
    ("073077", "winier", "adj", "/ˈwaɪniər/", "đượm hương vị rượu vang hơn"),
    ("073078", "winiest", "adj", "/ˈwaɪniɪst/", "đượm hương vị rượu vang nhất"),
    ("073079", "wuerzburgs", "noun", "/ˈvɜːrtsbɜːrɡz/", "thành phố Würzburg ở bang Bavaria"),
    ("073080", "abortuses", "noun", "/əˈbɔːrtəsɪz/", "thai nhi sẩy hoặc nạo bỏ (y học)"),
    ("073081", "academicisms", "noun", "/ˌækəˈdɛmɪˌsɪzəmz/", "tính hàn lâm sách vở kinh viện"),
    ("073082", "actinomyceses", "noun", "/ˌæktɪnoʊˈmaɪsiːzɪz/", "chi Xạ khuẩn kỵ khí Actinomyces"),
    ("073083", "airted", "verb", "/ˈɛərtɪd/", "đã dẫn hướng chỉ đường (Scotland)"),
    ("073084", "airting", "verb", "/ˈɛərtɪŋ/", "đang dẫn hướng chỉ đường"),
    ("073085", "airts", "verb", "/ˈɛərts/", "dẫn hướng; hướng gió (Scotland)"),
    ("073086", "anastomosed", "verb", "/əˈnæstəˌmoʊzd/", "đã thông nối mạch máu hoặc nhánh"),
    ("073087", "anastomosing", "verb", "/əˈnæstəˌmoʊzɪŋ/", "đang thông nối mạch máu nhánh cây"),
    ("073088", "angiologies", "noun", "/ˌændʒiˈɒlədʒiz/", "chuyên khoa mạch máu học"),
    ("073089", "angulated", "verb", "/ˈæŋɡjʊˌleɪtɪd/", "đã tạo góc cạnh khúc khuỷu"),
    ("073090", "angulates", "verb", "/ˈæŋɡjʊˌleɪts/", "tạo góc cạnh gập khúc"),
    ("073091", "angulating", "verb", "/ˈæŋɡjʊˌleɪtɪŋ/", "đang tạo góc cạnh gập khúc"),
    ("073092", "antlions", "noun", "/ˈæntˌlaɪənz/", "côn trùng kiến sư tử đào hố bẫy"),
    ("073093", "archils", "noun", "/ˈɑːrkɪlz/", "thuốc nhuộm màu tím chiết từ địa y"),
    ("073094", "asurs", "noun", "/ˈɑːsʊərz/", "thần tối cao Assyria; thành Ashur"),
    ("073095", "basketmakers", "noun", "/ˈbæskɪtˌmeɪkərz/", "thợ đan rổ rá giỏ mây tre"),
    ("073096", "bastardisations", "noun", "/ˌbæstərdaɪˈzeɪʃənz/", "sự làm biến chất suy đồi (Anh)"),
    ("073097", "bigoses", "noun", "/ˈbiːɡoʊsɪz/", "món thịt hầm cải muối bigos Ba Lan"),
    ("073098", "brahminisms", "noun", "/ˈbrɑːmɪˌnɪzəmz/", "đạo Bà-la-môn cổ đại Ấn Độ"),
    ("073099", "brickbats", "noun", "/ˈbrɪkˌbæts/", "mảnh gạch vỡ ném; lời chỉ trích gay"),
    ("073100", "brunnhildes", "noun", "/bruːnˈhɪldəz/", "nữ chiến binh Brünnhilde Bắc Âu"),
    ("073101", "brusas", "noun", "/ˈbruːsəz/", "thành phố Bursa ở Thổ Nhĩ Kỳ"),
    ("073102", "buskins", "noun", "/ˈbʌskɪnz/", "ủng da cao cổ đế dày diễn kịch cổ"),
]

with open("scratch/b35_r07_raw_p1.json") as f:
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

with open("scratch/b35_r07_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r07_p1.json OK")
