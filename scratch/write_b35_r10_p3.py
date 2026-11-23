import json

rows = [
    ("074703", "tremas", "noun", "/ˈtriːməz/", "chi cây hu đay (Trema)"),
    ("074704", "triopses", "noun", "/ˈtraɪɒpsɪz/", "giáp xác ba mắt triops"),
    ("074705", "trochees", "noun", "/ˈtroʊkiːz/", "bước nhịp trọng nhẹ (thơ ca)"),
    ("074706", "trophozoites", "noun", "/ˌtrɒfəˈzoʊaɪts/", "thể hoạt động dinh dưỡng (ký sinh)"),
    ("074707", "ulexes", "noun", "/ˈjuːlɛksɪz/", "chi cây kim tước gai (Ulex)"),
    ("074708", "vagaries", "noun", "/ˈveɪɡəriz/", "sự thay đổi thất thường"),
    ("074709", "abelias", "noun", "/əˈbiːliəz/", "chi cây lục đạo mộc (Abelia)"),
    ("074710", "acoruses", "noun", "/əˈkɔːrəsɪz/", "chi cây thủy xương bồ (Acorus)"),
    ("074711", "aeonia", "noun", "/iˈoʊniə/", "chi sen đá Aeonium"),
    ("074712", "amoebiases", "noun", "/ˌæmiˈbaɪəsɪz/", "bệnh kiết lỵ amíp"),
    ("074713", "annameses", "noun", "/ˌænəˈmiːzɪz/", "người An Nam (tên cũ Việt Nam)"),
    ("074714", "annunciated", "verb", "/əˈnʌnsieɪtɪd/", "đã loan báo; đã truyền tin"),
    ("074715", "annunciates", "verb", "/əˈnʌnsieɪts/", "loan báo; truyền tin"),
    ("074716", "annunciating", "verb", "/əˈnʌnsieɪtɪŋ/", "loan báo; truyền tin"),
    ("074717", "anodized", "verb", "/ˈænədaɪzd/", "đã ôxy hóa điện phân (anốt hóa)"),
    ("074718", "anodizes", "verb", "/ˈænədaɪzɪz/", "ôxy hóa điện phân (anốt hóa)"),
    ("074719", "anodizing", "verb", "/ˈænədaɪzɪŋ/", "ôxy hóa điện phân (anốt hóa)"),
    ("074720", "arcsins", "noun", "/ˈɑːrksɪnz/", "hàm lượng giác ngược arcsin"),
    ("074721", "asafetidas", "noun", "/ˌæsəˈfɛtɪdəz/", "nhựa cây a ngùy (asafoetida)"),
    ("074722", "autarchies", "noun", "/ˈɔːtɑːrkiz/", "chính sách kinh tế tự cung tự cấp"),
    ("074723", "averagenesses", "noun", "/ˈævərɪdʒnəsɪz/", "tính chất trung bình, bình thường"),
    ("074724", "baccharides", "noun", "/ˈbækərɪdz/", "chi cúc bạc (Baccharis)"),
    ("074725", "barndoors", "noun", "/ˈbɑːrnˌdɔːrz/", "cửa chuồng trại; cánh chắn đèn"),
    ("074726", "bedcovers", "noun", "/ˈbɛdˌkʌvərz/", "khăn phủ giường; ga trải giường"),
    ("074727", "bibliomanias", "noun", "/ˌbɪbliəˈmeɪniəz/", "chứng cuồng sách, nghiện sưu tầm"),
    ("074728", "bigrams", "noun", "/ˈbaɪɡræmz/", "cặp hai ký tự liên tiếp (bigram)"),
    ("074729", "bloviated", "verb", "/ˈbloʊvieɪtɪd/", "đã ba hoa khoác lác dài dòng"),
    ("074730", "bloviates", "verb", "/ˈbloʊvieɪts/", "ba hoa khoác lác dài dòng"),
    ("074731", "bloviating", "verb", "/ˈbloʊvieɪtɪŋ/", "ba hoa khoác lác dài dòng"),
    ("074732", "boletes", "noun", "/boʊˈliːts/", "nấm thông bolet (chi Boletus)"),
    ("074733", "bornites", "noun", "/ˈbɔːrnaɪts/", "quặng đồng bornit (đồng công)"),
    ("074734", "buckyballs", "noun", "/ˈbʌkiˌbɔːlz/", "phân tử cầu cacbon buckyball"),
    ("074735", "burettes", "noun", "/bjʊˈrɛts/", "ống chuẩn độ buret (hóa học)"),
    ("074736", "burgoos", "noun", "/ˈbɜːrɡuːz/", "súp thịt hầm burgoo; cháo thủy thủ"),
    ("074737", "buteas", "noun", "/ˈbjuːtiəz/", "chi cây giêng giêng (Butea)"),
    ("074738", "calliphoras", "noun", "/kəˈlɪfərəz/", "chi ruồi nhặng xanh (Calliphora)"),
    ("074739", "catechized", "verb", "/ˈkætɪkaɪzd/", "đã hỏi đáp giáo lý; chất vấn kỹ"),
    ("074740", "catechizes", "verb", "/ˈkætɪkaɪzɪz/", "hỏi đáp giáo lý; chất vấn kỹ"),
    ("074741", "catechizing", "verb", "/ˈkætɪkaɪzɪŋ/", "hỏi đáp giáo lý; chất vấn kỹ"),
    ("074742", "cervicitises", "noun", "/ˌsɜːrvɪˈsaɪtɪsɪz/", "bệnh viêm cổ tử cung (y học)"),
    ("074743", "chalcids", "noun", "/ˈkælsɪdz/", "ong ký sinh nhỏ (siêu họ Chalcid)"),
    ("074744", "chlorobenzenes", "noun", "/ˌklɔːroʊˈbɛnziːnz/", "hợp chất hữu cơ clobenzen"),
    ("074745", "chokies", "noun", "/ˈtʃoʊkiz/", "nhà giam; xà lim (từ lóng Anh-Ấn)"),
    ("074746", "clupeas", "noun", "/ˈkluːpiəz/", "chi cá trích (Clupea)"),
    ("074747", "coalmans", "noun", "/ˈkoʊlmənz/", "người bán hoặc giao than đá"),
    ("074748", "comints", "noun", "/ˈkɒmɪnts/", "tình báo thông tin liên lạc COMINT"),
    ("074749", "comploted", "verb", "/kəmˈplɒtɪd/", "đã cấu kết âm mưu"),
    ("074750", "comploting", "verb", "/kəmˈplɒtɪŋ/", "cấu kết âm mưu"),
    ("074751", "complots", "verb", "/kəmˈplɒts/", "cấu kết âm mưu"),
    ("074752", "complotted", "verb", "/kəmˈplɒtɪd/", "đã cấu kết âm mưu"),
    ("074753", "complotting", "verb", "/kəmˈplɒtɪŋ/", "cấu kết âm mưu"),
    ("074754", "corchoruses", "noun", "/kɔːrˈkɔːrəsɪz/", "chi cây đay (Corchorus)"),
    ("074755", "darvons", "noun", "/ˈdɑːrvɒnz/", "thuốc giảm đau Darvon"),
    ("074756", "derated", "verb", "/diːˈreɪtɪd/", "đã hạ công suất định mức"),
    ("074757", "derates", "verb", "/diːˈreɪts/", "hạ công suất định mức"),
    ("074758", "derating", "verb", "/diːˈreɪtɪŋ/", "hạ công suất định mức"),
    ("074759", "diaphyses", "noun", "/daɪˈæfɪsiːz/", "thân xương dài (giải phẫu)"),
    ("074760", "dieffenbachias", "noun", "/ˌdiːfənˈbɑːkiəz/", "cây vạn niên thanh (Dieffenbachia)"),
    ("074761", "dipodomyses", "noun", "/ˌdɪpəˈdɒmɪsɪz/", "chi chuột nhảy túi (Dipodomys)"),
    ("074762", "disfluencies", "noun", "/dɪsˈfluːənsiz/", "chứng nói lắp ngập ngừng (ngôn ngữ)"),
    ("074763", "dolours", "noun", "/ˈdoʊlərz/", "nỗi đau khổ sâu sắc (văn học)"),
    ("074764", "doyleys", "noun", "/ˈdɔɪliz/", "khăn ren nhỏ lót đĩa bánh"),
    ("074765", "enterobacterias", "noun", "/ˌɛntəroʊbækˈtɪriəz/", "vi khuẩn đường ruột Enterobacteria"),
    ("074766", "epimediums", "noun", "/ˌɛpɪˈmiːdiəmz/", "cây dâm dương hoắc (Epimedium)"),
    ("074767", "eulogises", "verb", "/ˈjuːlədʒaɪzɪz/", "ca ngợi; đọc điếu văn ca tụng"),
    ("074768", "felafels", "noun", "/fəˈlɑːfəlz/", "bánh đậu rán falafel (Trung Đông)"),
    ("074769", "fingerpaints", "noun", "/ˈfɪŋɡərpeɪnts/", "màu vẽ bằng ngón tay (trẻ em)"),
    ("074770", "finocchios", "noun", "/fɪˈnɒkioʊz/", "cây thì là củ Ý (finocchio)"),
    ("074771", "fluorochromes", "noun", "/ˈflʊərəkroʊmz/", "chất nhuộm huỳnh quang sinh học"),
    ("074772", "forepaws", "noun", "/ˈfɔːrpɔːz/", "bàn chân trước (động vật)"),
    ("074773", "glycosurias", "noun", "/ˌɡlaɪkoʊˈsjʊriəz/", "chứng đái ra đường (y học)"),
    ("074774", "goosefleshes", "noun", "/ˈɡuːsflɛʃɪz/", "tình trạng nổi da gà"),
    ("074775", "goosefoots", "noun", "/ˈɡuːsfʊts/", "cây rau muối (họ Dền)"),
    ("074776", "gyroplanes", "noun", "/ˈdʒaɪrəpleɪnz/", "máy bay cánh quay tự động"),
    ("074777", "headshakes", "noun", "/ˈhɛdʃeɪks/", "cái lắc đầu (tỏ ý không đồng tình)"),
    ("074778", "heracleums", "noun", "/ˌhɛrəˈkliːəmz/", "chi cây độc cần khổng lồ Heracleum"),
    ("074779", "humidified", "verb", "/hjuːˈmɪdɪfaɪd/", "đã làm ẩm; tạo độ ẩm"),
    ("074780", "humidifies", "verb", "/hjuːˈmɪdɪfaɪz/", "làm ẩm; tạo độ ẩm"),
    ("074781", "humidifying", "verb", "/hjuːˈmɪdɪfaɪɪŋ/", "làm ẩm; tạo độ ẩm"),
    ("074782", "hypervitaminoses", "noun", "/ˌhaɪpərvaɪtəmɪˈnoʊsiːz/", "chứng thừa vitamin (y học)"),
    ("074783", "hytrins", "noun", "/ˈhaɪtrɪnz/", "thuốc trị tăng huyết áp Hytrin"),
    ("074784", "isobutylenes", "noun", "/ˌaɪsoʊˈbjuːtəliːnz/", "khí hydrocacbon isobutylen"),
    ("074785", "isoeteses", "noun", "/aɪˈsoʊɪtiːz/", "chi thủy phỉ (thạch tùng nước)"),
    ("074786", "kassites", "noun", "/ˈkæsaɪts/", "người Kassite (Lưỡng Hà cổ đại)"),
    ("074787", "koppies", "noun", "/ˈkɒpiz/", "ngọn đồi đá nhỏ trên thảo nguyên"),
    ("074788", "labyrinthitises", "noun", "/ˌlæbərɪnˈθaɪtɪsɪz/", "bệnh viêm mê đạo tai trong (y học)"),
    ("074789", "loadstones", "noun", "/ˈloʊdstoʊnz/", "đá nam châm tự nhiên (magnetit)"),
    ("074790", "megestrols", "noun", "/mɪˈdʒɛstrəlz/", "thuốc nội tiết megestrol"),
    ("074791", "microbalances", "noun", "/ˈmaɪkroʊˌbælənsɪz/", "cân vi lượng độ nhạy cực cao"),
    ("074792", "microcircuits", "noun", "/ˈmaɪkroʊˌsɜːrkɪts/", "vi mạch; mạch tích hợp"),
    ("074793", "micrometeorites", "noun", "/ˌmaɪkroʊˈmiːtiəraɪts/", "vi thiên thạch (bụi vũ trụ)"),
    ("074794", "moraceaes", "noun", "/mɔːˈreɪsiːz/", "họ Dâu tằm (Moraceae)"),
    ("074795", "mugils", "noun", "/ˈmjuːdʒɪlz/", "chi cá đối (Mugil)"),
    ("074796", "munimentses", "noun", "/ˈmjuːnɪməntsɪz/", "văn tự chứng minh quyền sở hữu"),
    ("074797", "nailheads", "noun", "/ˈneɪlhɛdz/", "đầu đinh; mũ đinh tán"),
    ("074798", "nelumbos", "noun", "/nɪˈlʌmboʊz/", "chi Sen (Nelumbo)"),
    ("074799", "nephrocalcinoses", "noun", "/ˌnɛfroʊˌkælsɪˈnoʊsiːz/", "bệnh vôi hóa nhu mô thận (y học)"),
    ("074800", "nerodias", "noun", "/nɪˈroʊdiəz/", "chi rắn nước Bắc Mỹ (Nerodia)"),
    ("074801", "niprs", "noun", "/ˈnɪpərz/", "mạng quân sự NIPRNet; nhóm NIPR"),
    ("074802", "padders", "noun", "/ˈpædərz/", "kẻ cướp đường (từ cổ); máy đệm"),
]

with open("scratch/b35_r10_raw_p3.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

assert len(raw) == len(rows) == 100
out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, rows):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} vs {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} vs {hw}"
    assert len(vi) <= 35, f"vi too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.count("/") == 2 and not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"bad ipa: {hw} -> {ipa}"
    r["pos"] = pos
    r["ipa"] = ipa
    r["vi"] = vi
    r["status"] = "reviewed"
    out.append(r)

with open("scratch/b35_r10_p3.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b35_r10_p3 saved OK")
