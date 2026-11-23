import json

items = [
    ("074103", "reenforced", "verb", "/ˌriːɪnˈfɔːrst/", "đã gia cố tăng cường củng cố"),
    ("074104", "reenforces", "verb", "/ˌriːɪnˈfɔːrsɪz/", "gia cố tăng cường củng cố (Mỹ cũ)"),
    ("074105", "reenforcing", "verb", "/ˌriːɪnˈfɔːrsɪŋ/", "đang gia cố tăng cường củng cố"),
    ("074106", "resiled", "verb", "/rɪˈzaɪld/", "đã rút khỏi cam kết (luật, cổ)"),
    ("074107", "resiles", "verb", "/rɪˈzaɪlz/", "rút khỏi cam kết; bật nảy lại (cổ)"),
    ("074108", "resiling", "verb", "/rɪˈzaɪlɪŋ/", "đang rút khỏi cam kết thỏa thuận"),
    ("074109", "salesclerks", "noun", "/ˈseɪlzˌklɜːrks/", "nhân viên bán hàng tại quầy (Mỹ)"),
    ("074110", "salubrities", "noun", "/səˈluːbrɪtiz/", "tính chất lành mạnh tốt sức khỏe"),
    ("074111", "samites", "noun", "/ˈsæmaɪts/", "vải lụa gấm dày dệt sợi vàng xưa"),
    ("074112", "sarcolemmata", "noun", "/ˌsɑːrkəˈlɛmətə/", "màng sợi cơ vân (giải phẫu)"),
    ("074113", "secales", "noun", "/sɪˈkeɪliːz/", "chi Lúa mạch đen (Secale)"),
    ("074114", "sesquipedalians", "noun", "/ˌsɛskwɪpɪˈdeɪliənz/", "từ ngữ rất dài; người dùng từ dài"),
    ("074115", "seychelloides", "noun", "/ˌseɪʃɛˈlwɑːz/", "người dân đảo quốc Seychelles"),
    ("074116", "sinequans", "noun", "/ˈsɪnɪˌkwɒnz/", "thuốc chống trầm cảm Sinequan"),
    ("074117", "spiles", "noun", "/spaɪlz/", "cọc gỗ đóng móng; chốt vòi thùng"),
    ("074118", "spongers", "noun", "/ˈspʌndʒərz/", "kẻ ăn bám chực; thợ lặn bọt biển"),
    ("074119", "stochasticities", "noun", "/ˌstoʊkæˈstɪsɪtiz/", "tính ngẫu nhiên bất định (xác suất)"),
    ("074120", "stoeps", "noun", "/stʊps/", "bậc thềm hiên trước nhà (Nam Phi)"),
    ("074121", "stridulations", "noun", "/ˌstrɪdʒʊˈleɪʃənz/", "tiếng cọ cánh kêu rít của côn trùng"),
    ("074122", "strophanthuses", "noun", "/stroʊˈfænθəsɪz/", "cây sừng dê độc chi Strophanthus"),
    ("074123", "subphyla", "noun", "/sʌbˈfaɪlə/", "phân ngành (bậc phân loại sinh học)"),
    ("074124", "subphylums", "noun", "/ˈsʌbˌfaɪləmz/", "phân ngành (bậc phân loại sinh học)"),
    ("074125", "sunchokes", "noun", "/ˈsʌnˌtʃoʊks/", "củ cúc vu (Jerusalem artichoke)"),
    ("074126", "suspiciousnesses", "noun", "/səˈspɪʃəsnəsɪz/", "tính đa nghi hay ngờ vực"),
    ("074127", "switchmans", "noun", "/ˈswɪtʃmənz/", "nhân viên bẻ ghi đường sắt"),
    ("074128", "tapdanced", "verb", "/ˈtæpˌdænst/", "đã nhảy thiết hài gõ nhịp giày"),
    ("074129", "tapdances", "verb", "/ˈtæpˌdænsɪz/", "nhảy thiết hài gõ gót mũi giày"),
    ("074130", "tapdancing", "verb", "/ˈtæpˌdænsɪŋ/", "đang nhảy thiết hài gõ nhịp giày"),
    ("074131", "tectonas", "noun", "/tɛkˈtoʊnəz/", "chi Cây gỗ tếch (Tectona)"),
    ("074132", "tenormins", "noun", "/ˈtɛnɔːrmɪnz/", "thuốc chẹn beta hạ áp Tenormin"),
    ("074133", "tilters", "noun", "/ˈtɪltərz/", "hiệp sĩ đấu thương; máy nghiêng đổ"),
    ("074134", "tremolites", "noun", "/ˈtrɛməˌlaɪts/", "khoáng vật silicat tremolit"),
    ("074135", "uscbs", "noun", "/ˌjuː ɛs siː ˈbiːz/", "Cục Hải quan Hoa Kỳ (USCB)"),
    ("074136", "washermans", "noun", "/ˈwɒʃərmənz/", "người đàn ông làm nghề giặt là"),
    ("074137", "whimseys", "noun", "/ˈwɪmziz/", "ý thích bất chợt kỳ quặc (biến thể)"),
    ("074138", "yeniseys", "noun", "/ˌjɛnɪˈseɪz/", "sông Yenisei ở vùng Siberia (Nga)"),
    ("074139", "abstractnesses", "noun", "/ˈæbstræktnəsɪz/", "tính trừu tượng khái quát"),
    ("074140", "acousticians", "noun", "/ˌækuːˈstɪʃənz/", "chuyên gia hoặc nhà âm học"),
    ("074141", "advisees", "noun", "/ədˌvaɪˈziːz/", "người được cố vấn hướng dẫn"),
    ("074142", "alhazens", "noun", "/ælˈhɑːzɛnz/", "nhà quang học Ả Rập Alhazen"),
    ("074143", "allometries", "noun", "/əˈlɒmɪtriz/", "quy luật tăng trưởng tương đối"),
    ("074144", "allotropes", "noun", "/ˈæləˌtroʊps/", "dạng thù hình của nguyên tố"),
    ("074145", "almandines", "noun", "/ˈælmənˌdiːnz/", "đá quý ngọc hồng lựu almandin"),
    ("074146", "analyticities", "noun", "/ˌænəlɪˈtɪsɪtiz/", "tính giải tích của hàm số (toán)"),
    ("074147", "androsterones", "noun", "/ænˈdrɒstəˌroʊnz/", "hoóc-môn sinh dục nam androsteron"),
    ("074148", "aroids", "noun", "/ˈɛərɔɪdz/", "cây thuộc họ Ráy (Araceae)"),
    ("074149", "arteriographies", "noun", "/ɑːrˌtɪəriˈɒɡrəfiz/", "kỹ thuật chụp X-quang động mạch"),
    ("074150", "balkanized", "verb", "/ˈbɔːlkəˌnaɪzd/", "đã chia rẽ thành các phe nhỏ"),
    ("074151", "balkanizes", "verb", "/ˈbɔːlkəˌnaɪzɪz/", "chia cắt thành các quốc gia nhỏ"),
    ("074152", "balkanizing", "verb", "/ˈbɔːlkəˌnaɪzɪŋ/", "đang chia cắt thành các phe nhỏ"),
    ("074153", "brisses", "noun", "/ˈbrɪsɪz/", "lễ cắt bao quy đầu Do Thái (Bris)"),
    ("074154", "bynames", "noun", "/ˈbaɪˌneɪmz/", "biệt danh; tên gọi phụ gắn kèm"),
    ("074155", "chungas", "noun", "/ˈtʃʊŋɡəz/", "chim chạy bộ mào seriema nhỏ Chunga"),
    ("074156", "concretized", "verb", "/ˈkɒŋkrɪˌtaɪzd/", "đã cụ thể hóa thành hình thái rõ"),
    ("074157", "concretizes", "verb", "/ˈkɒŋkrɪˌtaɪzɪz/", "cụ thể hóa ý tưởng trừu tượng"),
    ("074158", "concretizing", "verb", "/ˈkɒŋkrɪˌtaɪzɪŋ/", "đang cụ thể hóa ý tưởng"),
    ("074159", "counterblasts", "noun", "/ˈkaʊntərˌblæsts/", "lời phản bác gay gắt kịch liệt"),
    ("074160", "cupronickels", "noun", "/ˌkjuːproʊˈnɪkəlz/", "hợp kim đồng-niken đúc tiền xu"),
    ("074161", "cyclothymias", "noun", "/ˌsaɪkloʊˈθaɪmiəz/", "rối loạn khí sắc chu kỳ lưỡng cực"),
    ("074162", "decimeters", "noun", "/ˈdɛsɪˌmiːtərz/", "đơn vị độ dài đề-xi-mét (0,1 m)"),
    ("074163", "densitometers", "noun", "/ˌdɛnsɪˈtɒmɪtərz/", "máy đo mật độ quang hoặc xương"),
    ("074164", "dislodgements", "noun", "/dɪsˈlɒdʒmənts/", "sự đánh bật đẩy ra khỏi vị trí"),
    ("074165", "dittanies", "noun", "/ˈdɪtəniz/", "cây bạch tiên thơm (dittany)"),
    ("074166", "egalites", "noun", "/ˌeɪɡɑːlɪˈteɪz/", "tinh thần bình đẳng (tiếng Pháp)"),
    ("074167", "equids", "noun", "/ˈiːkwɪdz/", "động vật họ Ngựa (ngựa, lừa)"),
    ("074168", "etuis", "noun", "/eɪˈtwiːz/", "hộp hoặc bao nhỏ đựng kim khâu đồ"),
    ("074169", "eurythmies", "noun", "/jʊˈrɪðmiz/", "nghệ thuật múa nhịp eurythmy"),
    ("074170", "feldenes", "noun", "/ˈfɛldiːnz/", "thuốc kháng viêm giảm đau Feldene"),
    ("074171", "fivesomes", "noun", "/ˈfaɪvsəmz/", "nhóm năm người; trận đấu năm người"),
    ("074172", "gizehs", "noun", "/ˈɡiːzəz/", "thành phố Giza (kim tự tháp Ai Cập)"),
    ("074173", "glucophages", "noun", "/ˈɡluːkoʊˌfeɪdʒɪz/", "thuốc trị tiểu đường Glucophage"),
    ("074174", "guomindangs", "noun", "/ˌɡwoʊmɪnˈdɑːŋz/", "Quốc dân Đảng Trung Hoa"),
    ("074175", "hairsprings", "noun", "/ˈhɛərˌsprɪŋz/", "dây tóc lò xo cân bằng đồng hồ"),
    ("074176", "hassocks", "noun", "/ˈhæsəks/", "đệm quỳ lót chân dày; bụi cỏ dày"),
    ("074177", "heyses", "noun", "/ˈhaɪzəz/", "văn sĩ Đức Nobel Paul Heyse"),
    ("074178", "hoatzins", "noun", "/hoʊˈætsɪnz/", "chim hoatzin có vuốt cánh Nam Mỹ"),
    ("074179", "homonymies", "noun", "/həˈmɒnɪmiz/", "hiện tượng đồng âm khác nghĩa"),
    ("074180", "hoppled", "verb", "/ˈhɒpəld/", "đã buộc dây khống chế chân ngựa"),
    ("074181", "hopples", "verb", "/ˈhɒpəlz/", "buộc dây chân ngựa không chạy xa"),
    ("074182", "hoppling", "verb", "/ˈhɒplɪŋ/", "đang buộc dây chân giữ ngựa"),
    ("074183", "houris", "noun", "/ˈhʊəriz/", "tiên nữ xinh đẹp thiên đường Hồi"),
    ("074184", "housebreaks", "verb", "/ˈhaʊsˌbreɪks/", "huấn luyện thú cưng đi vệ sinh đúng"),
    ("074185", "hypersecretions", "noun", "/ˌhaɪpərsɪˈkriːʃənz/", "tình trạng tăng tiết dịch quá mức"),
    ("074186", "inchoatives", "noun", "/ɪnˈkoʊətɪvz/", "động từ biểu thị sự bắt đầu (ngữ)"),
    ("074187", "indorsed", "verb", "/ɪnˈdɔːrst/", "đã ký hậu chuyển nhượng; đã ủng hộ"),
    ("074188", "indorses", "verb", "/ɪnˈdɔːrsɪz/", "ký hậu séc; chứng thực ủng hộ"),
    ("074189", "indorsing", "verb", "/ɪnˈdɔːrsɪŋ/", "đang ký hậu séc; đang ủng hộ"),
    ("074190", "infusorias", "noun", "/ˌɪnfjʊˈzɔːriəz/", "động vật nguyên sinh truyền dịch"),
    ("074191", "intactnesses", "noun", "/ɪnˈtæktnəsɪz/", "tình trạng nguyên vẹn không sứt mẻ"),
    ("074192", "intromissions", "noun", "/ˌɪntrəˈmɪʃənz/", "sự đưa vào; sự lồng ghép vào trong"),
    ("074193", "iritides", "noun", "/aɪˈrɪtɪˌdiːz/", "bệnh viêm mống mắt (nhãn khoa)"),
    ("074194", "kerygmas", "noun", "/kɛˈrɪɡməz/", "lời rao giảng cốt lõi Tin Mừng"),
    ("074195", "latrias", "noun", "/ləˈtraɪəz/", "sự tôn thờ tối cao chỉ dành Chúa"),
    ("074196", "lineations", "noun", "/ˌlɪniˈeɪʃənz/", "hệ thống đường nét kẻ vạch"),
    ("074197", "litterbugs", "noun", "/ˈlɪtərˌbʌɡz/", "kẻ vứt xả rác bừa bãi nơi công cộng"),
    ("074198", "lollygags", "verb", "/ˈlɒliˌɡæɡz/", "la cà lêu lổng phí thời gian"),
    ("074199", "lysimachias", "noun", "/ˌlɪsɪˈmeɪkiəz/", "cây trân châu chi Lysimachia"),
    ("074200", "mannikins", "noun", "/ˈmænɪkɪnz/", "hình nộm mẫu; người lùn tí hon"),
    ("074201", "martinmases", "noun", "/ˈmɑːrtɪnməsɪz/", "lễ Thánh Martin (11 tháng 11)"),
    ("074202", "masqueraders", "noun", "/ˌmæskəˈreɪdərz/", "người đeo mặt nạ dự hội hóa trang"),
]

with open("scratch/b35_r09_raw_p2.json") as f:
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

with open("scratch/b35_r09_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r09_p2.json OK")
