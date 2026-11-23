import json

items = [
    ("070103", "multifloras", "noun", "/ˌmʌltɪˈflɔːrəz/", "hoa hồng tầm xuân đa hoa"),
    ("070104", "nystatins", "noun", "/naɪˈstætɪnz/", "thuốc kháng nấm nystatin"),
    ("070105", "orangemans", "noun", "/ˈɒrɪndʒmənz/", "hội viên Hội Orange Bắc Ireland"),
    ("070106", "osiers", "noun", "/ˈoʊʒərz/", "cây liễu giỏ; cành liễu đan rổ"),
    ("070107", "ostracods", "noun", "/ˈɒstrəˌkɒdz/", "động vật giáp xác vỏ hai mảnh"),
    ("070108", "otoes", "noun", "/ˈoʊtoʊz/", "người Otoe bản địa Bắc Mỹ"),
    ("070109", "oxcarts", "noun", "/ˈɒksˌkɑːrts/", "xe bò kéo bánh gỗ chở hàng"),
    ("070110", "pantaloons", "noun", "/ˌpæntəˈluːnz/", "quần ống túm cổ điển; vai hề"),
    ("070111", "phytochemistries", "noun", "/ˌfaɪtoʊˈkɛmɪstriz/", "ngành hóa thực vật học"),
    ("070112", "planthoppers", "noun", "/ˈplæntˌhɒpərz/", "rầy bọ nhảy chích hút nhựa cây"),
    ("070113", "popinjays", "noun", "/ˈpɒpɪnˌdʒeɪz/", "kẻ khoác lác chưng diện; chim vẹt"),
    ("070114", "pronked", "verb", "/prɒŋkt/", "đã nhảy bật cả bốn chân lên"),
    ("070115", "pronking", "verb", "/ˈprɒŋkɪŋ/", "đang nhảy bật cả bốn chân lên"),
    ("070116", "pronks", "verb", "/prɒŋks/", "nhảy bật cả bốn chân lên"),
    ("070117", "qums", "noun", "/kʊmz/", "thành phố thánh địa Qom ở Iran"),
    ("070118", "radiopharmaceuticals", "noun", "/ˌreɪdioʊfɑːrməˈsuːtɪkəlz/", "dược chất phóng xạ chẩn đoán"),
    ("070119", "ratters", "noun", "/ˈrætərz/", "chó săn chuột; kẻ phản bội"),
    ("070120", "rubbernecked", "verb", "/ˈrʌbərˌnɛkt/", "đã ngoái rướn cổ tò mò nhìn"),
    ("070121", "rubbernecking", "verb", "/ˈrʌbərˌnɛkɪŋ/", "đang ngoái rướn cổ tò mò nhìn"),
    ("070122", "rubbernecks", "noun", "/ˈrʌbərˌnɛks/", "người ngoái cổ tò mò nhìn ngó"),
    ("070123", "rubdowns", "noun", "/ˈrʌbˌdaʊnz/", "bài xoa bóp thư giãn cơ bắp"),
    ("070124", "sabayons", "noun", "/sæˈbaɪɒnz/", "xốt kem trứng rượu vang sabayon"),
    ("070125", "salais", "noun", "/səˈlaɪz/", "cây nhựa hương Ấn Độ salai"),
    ("070126", "salians", "noun", "/ˈseɪliənz/", "người Frank vùng sông Salian"),
    ("070127", "sensitizers", "noun", "/ˈsɛnsɪˌtaɪzərz/", "chất gây nhạy sáng hoặc dị ứng"),
    ("070128", "shudras", "noun", "/ˈʃuːdrəz/", "đẳng cấp lao động Shudra Ấn Độ"),
    ("070129", "snarlier", "adj", "/ˈsnɑːrliər/", "rối bù hơn; gầm gừ cáu kỉnh hơn"),
    ("070130", "snarliest", "adj", "/ˈsnɑːrliɪst/", "rối bù nhất; gầm gừ cáu kỉnh nhất"),
    ("070131", "snuffboxes", "noun", "/ˈsnʌfˌbɒksɪz/", "hộp nhỏ đựng thuốc lá hít"),
    ("070132", "solferinos", "noun", "/ˌsɒlfəˈriːnoʊz/", "màu đỏ tía; thuốc nhuộm hồng tía"),
    ("070133", "spirochetes", "noun", "/ˈspaɪrəˌkiːts/", "xoắn khuẩn hình lò xo di động"),
    ("070134", "stickballs", "noun", "/ˈstɪkˌbɔːlz/", "trò bóng chày đường phố dùng gậy"),
    ("070135", "sweatsuits", "noun", "/ˈswɛtˌsuːts/", "bộ quần áo nỉ thể thao mặc ấm"),
    ("070136", "teredines", "noun", "/təˈrɛdɪˌniːz/", "con hà đục gỗ tàu thuyền biển"),
    ("070137", "teredos", "noun", "/təˈriːdoʊz/", "con hà đục gỗ tàu thuyền biển"),
    ("070138", "thrombophlebitides", "noun", "/ˌθrɒmboʊfləˈbaɪtɪdiːz/", "bệnh viêm tĩnh mạch huyết khối"),
    ("070139", "tilths", "noun", "/tɪlθs/", "độ tơi xốp của đất canh tác"),
    ("070140", "titanosaurs", "noun", "/taɪˈtænəˌsɔːrz/", "khủng long cổ dài khổng lồ"),
    ("070141", "tugelas", "noun", "/tʊˈɡɛləz/", "thác nước Tugela ở Nam Phi"),
    ("070142", "tyches", "noun", "/ˈtaɪkiz/", "nữ thần vận mệnh Tyche Hy Lạp"),
    ("070143", "tytos", "noun", "/ˈtaɪtoʊz/", "cú lợn mặt tim thuộc chi Tyto"),
    ("070144", "valsartans", "noun", "/vælˈsɑːrtənz/", "thuốc hạ huyết áp valsartan"),
    ("070145", "virgas", "noun", "/ˈvɜːrɡəz/", "vệt mưa bốc hơi trước chạm đất"),
    ("070146", "vitrines", "noun", "/vɪˈtriːnz/", "tủ kính trưng bày đồ quý hiếm"),
    ("070147", "weensier", "adj", "/ˈwiːnsiər/", "bé tí xíu hơn (khẩu ngữ)"),
    ("070148", "weensiest", "adj", "/ˈwiːnsiɪst/", "bé tí xíu nhất (khẩu ngữ)"),
    ("070149", "worktables", "noun", "/ˈwɜːrkˌteɪbəlz/", "bàn làm việc thợ hoặc bếp"),
    ("070150", "zinzendorfs", "noun", "/ˈzɪnzənˌdɔːrfs/", "bá tước Nikolaus von Zinzendorf"),
    ("070151", "aggressed", "verb", "/əˈɡrɛst/", "đã chủ động gây hấn tấn công"),
    ("070152", "aggresses", "verb", "/əˈɡrɛsɪz/", "chủ động gây hấn tấn công"),
    ("070153", "aggressing", "verb", "/əˈɡrɛsɪŋ/", "đang chủ động gây hấn tấn công"),
    ("070154", "amygdalins", "noun", "/əˈmɪɡdəlɪnz/", "hợp chất amygdalin trong hạt hạnh"),
    ("070155", "anthropocentrisms", "noun", "/ˌænθrəpoʊˈsɛntrɪzəmz/", "chủ nghĩa lấy con người làm tâm"),
    ("070156", "antialiasings", "noun", "/ˌæntiˈeɪliəsɪŋz/", "kỹ thuật khử răng cưa đồ họa"),
    ("070157", "antivenins", "noun", "/ˌæntiˈvɛnɪnz/", "huyết thanh kháng nọc độc rắn"),
    ("070158", "apatosauruses", "noun", "/əˌpætəˈsɔːrəsɪz/", "khủng long cổ dài Apatosaurus"),
    ("070159", "apomorphines", "noun", "/ˌæpəˈmɔːrfiːnz/", "thuốc apomorphine trị Parkinson"),
    ("070160", "aspleniums", "noun", "/əˈspliːniəmz/", "cây tổ điểu thuộc chi Asplenium"),
    ("070161", "bastardizations", "noun", "/ˌbæstərdaɪˈzeɪʃənz/", "sự làm biến chất suy đồi"),
    ("070162", "blitts", "noun", "/biː ˈlɪts/", "bằng Cử nhân Văn chương (B.Litt.)"),
    ("070163", "bragis", "noun", "/ˈbrɑːɡiz/", "thần thi ca Bragi vùng Bắc Âu"),
    ("070164", "canthuses", "noun", "/ˈkænθəsɪz/", "khóe mắt nơi hai mí gặp nhau"),
    ("070165", "centimes", "noun", "/ˈsɑːnˌtiːmz/", "đồng xu xen-tim (1/100 franc)"),
    ("070166", "chondrosarcomas", "noun", "/ˌkɒndroʊsɑːrˈkoʊməz/", "u ác tính mô sụn (ung thư sụn)"),
    ("070167", "ciardis", "noun", "/tʃiˈɑːrdiz/", "nhà thơ Mỹ John Ciardi"),
    ("070168", "ciliatas", "noun", "/ˌsɪliˈeɪtəz/", "lớp Trùng lông bơi nguyên sinh"),
    ("070169", "clubheads", "noun", "/ˈklʌbˌhɛdz/", "đầu gậy đánh gôn hoặc chùy"),
    ("070170", "coquetries", "noun", "/ˈkoʊkɪtriz/", "sự đong đưa làm duyên tán tỉnh"),
    ("070171", "crossbills", "noun", "/ˈkrɒsˌbɪlz/", "chim mỏ chéo chuyên tách hạt thông"),
    ("070172", "cucumides", "noun", "/kjʊˈkjuːmɪˌdiːz/", "chi Dưa chuột và dưa lưới Cucumis"),
    ("070173", "cythereas", "noun", "/ˌsɪθəˈriːəz/", "thần tình yêu Aphrodite Cytherea"),
    ("070174", "cytidines", "noun", "/ˈsaɪtɪˌdiːnz/", "nucleoside cytidine cấu tạo RNA"),
    ("070175", "danauses", "noun", "/dəˈneɪəsɪz/", "chi Bướm vua Danaus"),
    ("070176", "daybooks", "noun", "/ˈdeɪˌbʊks/", "sổ nhật ký ghi giao dịch hằng ngày"),
    ("070177", "deflorations", "noun", "/ˌdɛfləˈreɪʃənz/", "sự hái hoa; sự phá trinh (sách cũ)"),
    ("070178", "deputised", "verb", "/ˈdɛpjʊˌtaɪzd/", "đã ủy quyền làm đại diện (Anh)"),
    ("070179", "deputises", "verb", "/ˈdɛpjʊˌtaɪzɪz/", "ủy quyền làm đại diện (Anh)"),
    ("070180", "deputising", "verb", "/ˈdɛpjʊˌtaɪzɪŋ/", "đang ủy quyền làm đại diện (Anh)"),
    ("070181", "dermatomyositises", "noun", "/ˌdɜːrmətoʊmaɪəˈsaɪtɪsɪz/", "bệnh viêm da cơ tự miễn"),
    ("070182", "diagonalizations", "noun", "/daɪˌæɡənəlaɪˈzeɪʃənz/", "phép chéo hóa ma trận (toán học)"),
    ("070183", "dockages", "noun", "/ˈdɒkɪdʒɪz/", "phí neo đậu tàu; khoản khấu trừ"),
    ("070184", "durazzos", "noun", "/dʊˈrɑːtsoʊz/", "thành phố cảng Durrës ở Albania"),
    ("070185", "elavils", "noun", "/ˈɛləvɪlz/", "thuốc chống trầm cảm Elavil"),
    ("070186", "elephases", "noun", "/ˈɛlɪˌfæsiːz/", "chi Voi châu Á (Elephas)"),
    ("070187", "ergometers", "noun", "/ɜːrˈɡɒmɪtərz/", "máy đo công cơ bắp; xe đạp lực kế"),
    ("070188", "ericaceaes", "noun", "/ˌɛrɪˈkeɪʃiˌiːz/", "họ Thạch nam đỗ quyên Ericaceae"),
    ("070189", "etanercepts", "noun", "/ɪˈtænərˌsɛpts/", "thuốc sinh học etanercept trị khớp"),
    ("070190", "exospheres", "noun", "/ˈɛksoʊˌsfɪərz/", "tầng ngoài cùng của khí quyển"),
    ("070191", "fibromas", "noun", "/faɪˈbroʊməz/", "u xơ lành tính ở mô liên kết"),
    ("070192", "foresails", "noun", "/ˈfɔːrˌseɪlz/", "cánh buồm chính ở cột buồm mũi"),
    ("070193", "gafsas", "noun", "/ˈɡæfsəz/", "thành phố ốc đảo Gafsa ở Tunisia"),
    ("070194", "goosebumps", "noun", "/ˈɡuːsˌbʌmps/", "nổi da gà do lạnh hoặc sợ hãi"),
    ("070195", "gruses", "noun", "/ˈɡrʌsɪz/", "chòm sao Thiên Hạc; chi Sếu Grus"),
    ("070196", "hepatomegalies", "noun", "/ˌhɛpətoʊˈmɛɡəliz/", "chứng gan to bất thường (y học)"),
    ("070197", "hupas", "noun", "/ˈhuːpəz/", "bộ tộc người bản địa Hupa ở Mỹ"),
    ("070198", "hyadeses", "noun", "/ˈhaɪədiːzɪz/", "cụm sao Hyades trong chòm Kim Ngưu"),
    ("070199", "hypocalcemias", "noun", "/ˌhaɪpoʊkælˈsiːmiəz/", "tình trạng hạ canxi trong máu"),
    ("070200", "hysons", "noun", "/ˈhaɪsənz/", "trà xanh Trung Quốc Hyson"),
    ("070201", "immunogens", "noun", "/ɪˈmjuːnədʒənz/", "chất kích thích tạo miễn dịch"),
    ("070202", "infantilisms", "noun", "/ɪnˈfæntəlˌɪzəmz/", "tính trẻ con; chứng nhi hóa"),
]

with open("scratch/b35_r01_raw_p2.json") as f:
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

with open("scratch/b35_r01_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r01_p2.json OK")
