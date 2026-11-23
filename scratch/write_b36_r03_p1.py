import json

rows = [
    ("076003", "phasianidae", "noun", "/ˌfeɪziˈænɪdiː/", "họ Trĩ (gà lôi, chim công)"),
    ("076004", "phasianus", "noun", "/feɪziˈeɪnəs/", "chi chim trĩ đỏ (Phasianus)"),
    ("076005", "phasic", "adj", "/ˈfeɪzɪk/", "thuộc giai đoạn; theo pha"),
    ("076006", "phasing", "verb", "/ˈfeɪzɪŋ/", "thực hiện từng bước; đồng bộ pha"),
    ("076007", "phasma", "noun", "/ˈfæzmə/", "bọ que; bọ lá (chi Phasma)"),
    ("076008", "phasmatidae", "noun", "/fæzˈmætɪdiː/", "họ Bọ que (Phasmatidae)"),
    ("076009", "phasmatodea", "noun", "/ˌfæzməˈtoʊdiə/", "bộ Bọ que, bộ Bọ lá"),
    ("076010", "phasmida", "noun", "/ˈfæzmɪdə/", "bộ Bọ que, bộ Bọ lá"),
    ("076011", "phasmidae", "noun", "/ˈfæzmɪdiː/", "họ Bọ que (Phasmidae)"),
    ("076012", "phasmidia", "noun", "/fæzˈmɪdiə/", "phân lớp Giun tròn Phasmidia"),
    ("076013", "phatties", "noun", "/ˈfætiz/", "điếu thuốc cuốn to (tiếng lóng)"),
    ("076014", "phegopteris", "noun", "/fɪˈɡɒptərɪs/", "chi dương xỉ sồi (Phegopteris)"),
    ("076015", "pheidias", "noun", "/ˈfaɪdiəs/", "nhà điêu khắc Phidias (Hy Lạp cổ)"),
    ("076016", "phellem", "noun", "/ˈfɛlɛm/", "mô bần (lớp vỏ bần thực vật)"),
    ("076017", "phellodendron", "noun", "/ˌfɛləˈdɛndrɒn/", "chi cây hoàng bá (Phellodendron)"),
    ("076018", "phelloderm", "noun", "/ˈfɛlədɜːrm/", "lục bì (mô thực vật học)"),
    ("076019", "phellodermal", "adj", "/ˌfɛləˈdɜːrməl/", "thuộc lục bì (thực vật học)"),
    ("076020", "phellogen", "noun", "/ˈfɛlədʒɛn/", "tầng sinh bần (thực vật học)"),
    ("076021", "phellogenetic", "adj", "/ˌfɛlədʒəˈnɛtɪk/", "thuộc tầng sinh bần (thực vật học)"),
    ("076022", "phelloid", "noun", "/ˈfɛlɔɪd/", "tầng không hóa bần (thực vật)"),
    ("076023", "phellum", "noun", "/ˈfɛləm/", "mô bần (biến thể của phellem)"),
    ("076024", "phenacain", "noun", "/ˈfɛnəkeɪn/", "thuốc gây tê tại chỗ phenacain"),
    ("076025", "phenacomys", "noun", "/fɪˈnækəmɪs/", "chi chuột đồng cây Bắc Mỹ"),
    ("076026", "phenaphen", "noun", "/ˈfɛnəfɛn/", "thuốc giảm đau hạ sốt Phenaphen"),
    ("076027", "phene", "noun", "/fiːn/", "tính trạng biểu hình (di truyền)"),
    ("076028", "phenetic", "adj", "/fɪˈnɛtɪk/", "thuộc phân loại theo ngoại hình"),
    ("076029", "phenicia", "noun", "/fɪˈniːʃə/", "xứ Phoenicia (Địa Trung Hải cổ)"),
    ("076030", "pheniramine", "noun", "/fəˈnɪrəmiːn/", "thuốc kháng histamin pheniramin"),
    ("076031", "phenocline", "noun", "/ˈfiːnəklaɪn/", "biến thiên ngoại hình theo vùng"),
    ("076032", "phenocontour", "noun", "/ˌfiːnoʊˈkɒntʊr/", "đường đẳng vật hậu (đồng thời nở)"),
    ("076033", "phenocopy", "noun", "/ˈfiːnəˌkɒpi/", "kiểu hình mô phỏng (di truyền học)"),
    ("076034", "phenocryst", "noun", "/ˈfiːnəkrɪst/", "ban tinh lớn trong đá mácma"),
    ("076035", "phenocrystic", "adj", "/ˌfiːnəˈkrɪstɪk/", "thuộc ban tinh trong đá mácma"),
    ("076036", "phenodeme", "noun", "/ˈfiːnədiːm/", "quần thể ngoại hình (sinh thái)"),
    ("076037", "phenodeviant", "noun", "/ˌfiːnoʊˈdiːviənt/", "cá thể biến dị ngoại hình"),
    ("076038", "phenogam", "noun", "/ˈfiːnəɡæm/", "thực vật có hoa, có hạt"),
    ("076039", "phenogenetics", "noun", "/ˌfiːnoʊdʒəˈnɛtɪks/", "di truyền học hình thái phát triển"),
    ("076040", "phenological", "adj", "/ˌfiːnəˈlɒdʒɪkəl/", "thuộc vật hậu học (theo mùa)"),
    ("076041", "phenologically", "adv", "/ˌfiːnəˈlɒdʒɪkli/", "về mặt vật hậu học"),
    ("076042", "phenologist", "noun", "/fɪˈnɒlədʒɪst/", "nhà vật hậu học"),
    ("076043", "phenology", "noun", "/fɪˈnɒlədʒi/", "vật hậu học (chu kỳ sinh học mùa)"),
    ("076044", "phenomena", "noun", "/fəˈnɒmɪnə/", "các hiện tượng (số nhiều)"),
    ("076045", "phenomenalism", "noun", "/fɪˈnɒmɪnəlɪzəm/", "chủ nghĩa hiện tượng (triết học)"),
    ("076046", "phenomenalist", "noun", "/fɪˈnɒmɪnəlɪst/", "người theo thuyết hiện tượng"),
    ("076047", "phenomenalistic", "adj", "/fɪˌnɒmɪnəˈlɪstɪk/", "thuộc thuyết hiện tượng"),
    ("076048", "phenomenalistically", "adv", "/fɪˌnɒmɪnəˈlɪstɪkli/", "theo quan điểm thuyết hiện tượng"),
    ("076049", "phenomenalize", "verb", "/fɪˈnɒmɪnəlaɪz/", "biểu hiện thành hiện tượng"),
    ("076050", "phenomenism", "noun", "/fɪˈnɒmɪnɪzəm/", "thuyết hiện tượng (triết học)"),
    ("076051", "phenomenist", "noun", "/fɪˈnɒmɪnɪst/", "người theo thuyết hiện tượng"),
    ("076052", "phenomenistic", "adj", "/fɪˌnɒmɪˈnɪstɪk/", "thuộc thuyết hiện tượng"),
    ("076053", "phenomenological", "adj", "/fɪˌnɒmɪnəˈlɒdʒɪkəl/", "thuộc hiện tượng học"),
    ("076054", "phenomenologically", "adv", "/fɪˌnɒmɪnəˈlɒdʒɪkli/", "theo phương pháp hiện tượng học"),
    ("076055", "phenomenologist", "noun", "/fɪˌnɒmɪˈnɒlədʒɪst/", "nhà hiện tượng học"),
    ("076056", "phenoplast", "noun", "/ˈfiːnəplæst/", "nhựa nhiệt rắn phenol-fomandehit"),
    ("076057", "phensuximide", "noun", "/fɛnˈsʌksɪmaɪd/", "thuốc chống động kinh phensuximid"),
    ("076058", "phenylacetamide", "noun", "/ˌfɛnɪlæsɪˈtæmaɪd/", "hợp chất hóa học phenylacetamit"),
    ("076059", "phenylamine", "noun", "/ˌfɛnɪləˈmiːn/", "hợp chất phenylamin (anilin)"),
    ("076060", "phenylethylene", "noun", "/ˌfɛnɪlˈɛθɪliːn/", "chất styren (nhựa polystyren)"),
    ("076061", "phenylpropanes", "noun", "/ˌfɛnɪlˈproʊpeɪnz/", "hợp chất phenylpropan"),
    ("076062", "phenyltoloxamine", "noun", "/ˌfɛnɪltoʊˈlɒksəmiːn/", "thuốc kháng dị ứng phenyltoloxamin"),
    ("076063", "pheresis", "noun", "/fəˈriːsɪs/", "kỹ thuật lọc tách thành phần máu"),
    ("076064", "phew", "intj", "/fjuː/", "phù (thở phào nhẹ nhõm); ối"),
    ("076065", "phialophore", "noun", "/faɪˈæləfɔːr/", "cuống thể bình (nấm học)"),
    ("076066", "philadelphaceae", "noun", "/ˌfɪlədɛlˈfeɪsiː/", "họ Mai giả (Philadelphaceae)"),
    ("076067", "philaenus", "noun", "/fɪˈliːnəs/", "chi ve sầu nhảy bọt (Philaenus)"),
    ("076068", "philandered", "verb", "/fɪˈlændərd/", "đã tán tỉnh trăng hoa, lăng nhăng"),
    ("076069", "philandering", "verb", "/fɪˈlændərɪŋ/", "tán tỉnh trăng hoa, lăng nhăng"),
    ("076070", "philanders", "verb", "/fɪˈlændərz/", "tán tỉnh trăng hoa, lăng nhăng"),
    ("076071", "philanthrope", "noun", "/ˈfɪlənθroʊp/", "nhà từ thiện; người bác ái"),
    ("076072", "philanthropism", "noun", "/fɪˈlænθrəpɪzəm/", "chủ nghĩa nhân đạo, lòng bác ái"),
    ("076073", "philanthropize", "verb", "/fɪˈlænθrəpaɪz/", "làm việc từ thiện; rao giảng bác ái"),
    ("076074", "philatelical", "adj", "/ˌfɪləˈtɛlɪkəl/", "thuộc ngành sưu tầm tem thư"),
    ("076075", "philatelically", "adv", "/ˌfɪləˈtɛlɪkli/", "về mặt sưu tầm tem thư"),
    ("076076", "philatelists", "noun", "/fɪˈlætəlɪsts/", "người sưu tầm tem thư"),
    ("076077", "philhellene", "adj", "/ˌfɪlˈhɛliːn/", "người yêu mến văn hóa Hy Lạp"),
    ("076078", "philhellenic", "adj", "/ˌfɪlhɛˈliːnɪk/", "thân Hy Lạp; yêu văn hóa Hy Lạp"),
    ("076079", "philhellenism", "noun", "/ˌfɪlˈhɛlɪnɪzəm/", "tình cảm yêu mến và ủng hộ Hy Lạp"),
    ("076080", "philhellenist", "noun", "/ˌfɪlˈhɛlɪnɪst/", "người yêu mến và ủng hộ Hy Lạp"),
    ("076081", "phillidae", "noun", "/ˈfɪlɪdiː/", "họ Bọ lá (cách viết biến thể)"),
    ("076082", "phillipsite", "noun", "/ˈfɪlɪpsaɪt/", "khoáng vật zeolit phillipsit"),
    ("076083", "phillumenist", "noun", "/fɪˈluːmənɪst/", "người sưu tầm nhãn bao diêm"),
    ("076084", "phillyrea", "noun", "/fɪˈlɪriə/", "chi cây ô liu giả (Phillyrea)"),
    ("076085", "philobiblic", "adj", "/ˌfɪloʊˈbɪblɪk/", "yêu thích sách vở, mê sách"),
    ("076086", "philobilic", "adj", "/ˌfɪloʊˈbɪlɪk/", "yêu thích sách vở (biến thể)"),
    ("076087", "philogynist", "noun", "/fɪˈlɒdʒɪnɪst/", "người yêu quý và tôn trọng phụ nữ"),
    ("076088", "philogyny", "noun", "/fɪˈlɒdʒəni/", "lòng yêu mến và trân trọng phụ nữ"),
    ("076089", "philohela", "noun", "/ˌfɪləˈhiːlə/", "chi chim dẽ giun gỗ Mỹ (Philohela)"),
    ("076090", "philologer", "noun", "/fɪˈlɒlədʒər/", "nhà ngữ văn học"),
    ("076091", "philologian", "noun", "/ˌfɪləˈloʊdʒiən/", "nhà ngữ văn học"),
    ("076092", "philologic", "adj", "/ˌfɪləˈlɒdʒɪk/", "thuộc ngữ văn học"),
    ("076093", "philologically", "adv", "/ˌfɪləˈlɒdʒɪkli/", "về mặt ngữ văn học"),
    ("076094", "philologies", "noun", "/fɪˈlɒlədʒiz/", "ngành ngữ văn học cổ điển"),
    ("076095", "philologize", "verb", "/fɪˈlɒlədʒaɪz/", "nghiên cứu hoặc bàn luận ngữ văn"),
    ("076096", "philologue", "noun", "/ˈfɪləlɒɡ/", "nhà ngữ văn học; nhà nhân văn học"),
    ("076097", "philomachus", "noun", "/fɪˈlɒməkəs/", "chi chim choắt (Philomachus)"),
    ("076098", "philomathy", "noun", "/fɪˈlɒməθi/", "lòng ham học hỏi, yêu tri thức"),
    ("076099", "philomel", "noun", "/ˈfɪləmɛl/", "chim họa mi (trong thơ ca)"),
    ("076100", "philomela", "noun", "/ˌfɪləˈmiːlə/", "chim họa mi (thơ ca); tiên nữ cổ"),
    ("076101", "philomusical", "adj", "/ˌfɪloʊˈmjuːzɪkəl/", "yêu thích âm nhạc"),
    ("076102", "philophylla", "noun", "/ˌfɪloʊˈfɪlə/", "chi ruồi đục lá (Philophylla)"),
]

with open("scratch/b36_r03_raw_p1.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r03_p1.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r03_p1 saved OK")
