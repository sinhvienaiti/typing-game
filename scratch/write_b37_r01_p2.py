import json

records = [
    ("080103", "pseudolarix", "noun", "/ˌsuːdoʊˈlɛrɪks/", "chi thông rụng lá vàng Trung Quốc"),
    ("080104", "pseudologer", "noun", "/suːˈdɑːlədʒər/", "người mắc chứng nói dối bệnh lý"),
    ("080105", "pseudomembrane", "noun", "/ˌsuːdoʊˈmɛmbreɪn/", "giả mạc (màng viêm trên niêm mạc)"),
    ("080106", "pseudomitosis", "noun", "/ˌsuːdoʊmaɪˈtoʊsɪs/", "sự gián phân giả (tế bào học)"),
    ("080107", "pseudomixis", "noun", "/ˌsuːdoʊˈmɪksɪs/", "sự phối hợp tế bào sinh dưỡng (nấm)"),
    ("080108", "pseudomonad", "noun", "/ˌsuːdoʊˈmoʊnæd/", "vi khuẩn thuộc chi Pseudomonas"),
    ("080109", "pseudomonadales", "noun", "/ˌsuːdoʊmoʊnəˈdeɪliːz/", "bộ vi khuẩn trực khuẩn mủ xanh"),
    ("080110", "pseudomonodaceae", "noun", "/ˌsuːdoʊmoʊnəˈdeɪsiː/", "họ vi khuẩn trực khuẩn gram âm"),
    ("080111", "pseudomorph", "noun", "/ˈsuːdoʊˌmɔːrf/", "tinh thể giả hình (khoáng vật học)"),
    ("080112", "pseudomorphism", "noun", "/ˌsuːdoʊˈmɔːrfɪzəm/", "hiện tượng giả hình (khoáng vật)"),
    ("080113", "pseudomorphous", "adj", "/ˌsuːdoʊˈmɔːrfəs/", "có dạng giả hình (khoáng vật)"),
    ("080114", "pseudonymity", "noun", "/ˌsuːdəˈnɪməti/", "tình trạng dùng bút danh, ẩn danh"),
    ("080115", "pseudonymously", "adv", "/suːˈdɑːnəməsli/", "dưới bút danh, lấy tên giả"),
    ("080116", "pseudonymousness", "noun", "/suːˈdɑːnəməsnəs/", "tính chất nặc danh, dùng bút danh"),
    ("080117", "pseudonyms", "noun", "/ˈsuːdəˌnɪmz/", "các bút danh, biệt hiệu, tên giả"),
    ("080118", "pseudoparticle", "noun", "/ˌsuːdoʊˈpɑːrtɪkəl/", "giả hạt, chuẩn hạt (vật lý)"),
    ("080119", "pseudoperiodic", "adj", "/ˌsuːdoʊˌpɪriˈɑːdɪk/", "giả tuần hoàn (toán học)"),
    ("080120", "pseudoperipteral", "adj", "/ˌsuːdoʊpəˈrɪptərəl/", "có hàng cột giả gắn vào tường (đền)"),
    ("080121", "pseudophloem", "noun", "/ˌsuːdoʊˈfloʊəm/", "mô mạch rây giả (thực vật học)"),
    ("080122", "pseudopleuronectes", "noun", "/ˌsuːdoʊˌplʊrəˈnɛktiːz/", "chi cá bơn mùa đông (cá bơn Mỹ)"),
    ("080123", "pseudopodium", "noun", "/ˌsuːdoʊˈpoʊdiəm/", "chân giả (trùng biến hình)"),
    ("080124", "pseudopregnancy", "noun", "/ˌsuːdoʊˈprɛɡnənsi/", "tình trạng mang thai giả (y học)"),
    ("080125", "pseudoprostyle", "adj", "/ˌsuːdoʊˈproʊstaɪl/", "chỉ có hàng cột giả mặt tiền"),
    ("080126", "pseudorandom", "adj", "/ˌsuːdoʊˈrændəm/", "giả ngẫu nhiên (toán, tin học)"),
    ("080127", "pseudorubella", "noun", "/ˌsuːdoʊruːˈbɛlə/", "bệnh sốt phát ban đào ở trẻ nhỏ"),
    ("080128", "pseudorumination", "noun", "/ˌsuːdoʊˌruːməˈneɪʃən/", "hiện tượng ăn lại phân (ở thỏ)"),
    ("080129", "pseudoryx", "noun", "/ˈsuːdɔːrɪks/", "loài sao la, kỳ lân châu Á"),
    ("080130", "pseudoscorpion", "noun", "/ˌsuːdoʊˈskɔːrpiən/", "con bọ cạp giả (họ Hình nhện)"),
    ("080131", "pseudoscorpiones", "noun", "/ˌsuːdoʊˌskɔːrpiˈoʊniːz/", "bộ Bọ cạp giả (Pseudoscorpiones)"),
    ("080132", "pseudoscorpionida", "noun", "/ˌsuːdoʊˌskɔːrpiˈɑːnɪdə/", "bộ Bọ cạp giả (Pseudoscorpionida)"),
    ("080133", "pseudosmallpox", "noun", "/ˌsuːdoʊˈsmɔːlpɑːks/", "bệnh đậu mùa nhẹ, đậu mùa giả"),
    ("080134", "pseudosperm", "noun", "/ˈsuːdoʊˌspɜːrm/", "hạt giả, quả một hạt giống hạt"),
    ("080135", "pseudosphere", "noun", "/ˈsuːdoʊˌsfɪr/", "giả mặt cầu (hình học phi Euclid)"),
    ("080136", "pseudospherical", "adj", "/ˌsuːdoʊˈsfɪrɪkəl/", "thuộc giả mặt cầu (hình học)"),
    ("080137", "pseudotaxus", "noun", "/ˌsuːdoʊˈtæksəs/", "chi thông đỏ trắng (Pseudotaxus)"),
    ("080138", "pseudovaluation", "noun", "/ˌsuːdoʊˌvæljuˈeɪʃən/", "giả định giá (đại số học)"),
    ("080139", "pseudovariola", "noun", "/ˌsuːdoʊvəˈraɪələ/", "bệnh đậu mùa nhẹ (y học)"),
    ("080140", "pseudovector", "noun", "/ˌsuːdoʊˈvɛktər/", "giả vectơ, vectơ trục (toán, lý)"),
    ("080141", "pseudowintera", "noun", "/ˌsuːdoʊˈwɪntərə/", "chi cây hồ tiêu New Zealand"),
    ("080142", "pshaw", "intj", "/ʃɔː/", "xì, hừ (tiếng kêu tỏ ý coi thường)"),
    ("080143", "psilanthropism", "noun", "/ˌsaɪˈlænθrəˌpɪzəm/", "thuyết coi Giê-su là người phàm"),
    ("080144", "psilanthropist", "noun", "/ˌsaɪˈlænθrəpɪst/", "người coi Chúa Giê-su là người phàm"),
    ("080145", "psilanthropy", "noun", "/saɪˈlænθrəpi/", "thuyết coi Giê-su là người phàm"),
    ("080146", "psilomelane", "noun", "/ˌsaɪləˈmɛleɪn/", "quặng mangan đen psilomelan"),
    ("080147", "psilophytaceae", "noun", "/ˌsaɪloʊfaɪˈteɪsiː/", "họ thực vật cổ đại Psilophytaceae"),
    ("080148", "psilophytales", "noun", "/ˌsaɪloʊfaɪˈteɪliːz/", "bộ thực vật cổ Psilophytales"),
    ("080149", "psilophyte", "noun", "/ˈsaɪləˌfaɪt/", "thực vật hóa thạch cổ Psilophyta"),
    ("080150", "psilophyton", "noun", "/ˌsaɪləˈfaɪtɑːn/", "chi thực vật cổ Psilophyton"),
    ("080151", "psilopsida", "noun", "/saɪˈlɑːpsɪdə/", "lớp Thực vật khỏa quyết"),
    ("080152", "psilosis", "noun", "/saɪˈloʊsɪs/", "bệnh tiêu chảy mỡ; chứng rụng lông"),
    ("080153", "psilotaceae", "noun", "/ˌsaɪləˈteɪsiː/", "họ Lã khỏa quyết (Psilotaceae)"),
    ("080154", "psilotales", "noun", "/ˌsaɪləˈteɪliːz/", "bộ Lã khỏa quyết (Psilotales)"),
    ("080155", "psilotatae", "noun", "/ˌsaɪləˈteɪtiː/", "lớp Lã khỏa quyết (thực vật)"),
    ("080156", "psilotum", "noun", "/saɪˈloʊtəm/", "chi cây lá thông đá (Psilotum)"),
    ("080157", "psithyrus", "noun", "/ˈsɪθərəs/", "phân chi ong vò vẽ ký sinh tổ"),
    ("080158", "psittacidae", "noun", "/sɪˈtæsɪˌdiː/", "họ Vẹt thật (Psittacidae)"),
    ("080159", "psittaciformes", "noun", "/ˌsɪtəsɪˈfɔːrmiːz/", "bộ Vẹt (Psittaciformes)"),
    ("080160", "psittacine", "adj", "/ˈsɪtəˌsaɪn/", "thuộc họ vẹt, giống chim vẹt"),
    ("080161", "psittacosaur", "noun", "/ˈsɪtəkəˌsɔːr/", "khủng long mỏ vẹt Psittacosaurus"),
    ("080162", "psittacosaurus", "noun", "/ˌsɪtəkəˈsɔːrəs/", "khủng long mỏ vẹt Psittacosaurus"),
    ("080163", "psittacotic", "adj", "/ˌsɪtəˈkɑːtɪk/", "thuộc bệnh sốt vẹt (y học)"),
    ("080164", "psittacula", "noun", "/sɪˈtækjələ/", "chi vẹt má vàng, vẹt cổ hồng"),
    ("080165", "psittacus", "noun", "/ˈsɪtəkəs/", "chi vẹt xám châu Phi (Psittacus)"),
    ("080166", "psocid", "noun", "/ˈsɑːsɪd/", "con rệp sách (bộ Psocoptera)"),
    ("080167", "psocidae", "noun", "/ˈsɑːsɪˌdiː/", "họ Rệp vỏ cây (Psocidae)"),
    ("080168", "psocoptera", "noun", "/ˌsɑːˈkɑːptərə/", "bộ Rệp sách, bọ ăn giấy"),
    ("080169", "psophia", "noun", "/ˈsɑːfiə/", "chi chim kèn đồng Nam Mỹ (Psophia)"),
    ("080170", "psophiidae", "noun", "/səˈfaɪɪˌdiː/", "họ Chim kèn đồng (Psophiidae)"),
    ("080171", "psophocarpus", "noun", "/ˌsɑːfəˈkɑːrpəs/", "chi Đậu rồng (Psophocarpus)"),
    ("080172", "psora", "noun", "/ˈsɔːrə/", "bệnh ngứa da mãn tính; bệnh vảy nến"),
    ("080173", "psoralea", "noun", "/səˈreɪliə/", "chi cây Phá cố chỉ (họ Đậu)"),
    ("080174", "psoriatic", "adj", "/ˌsɔːriˈætɪk/", "thuộc bệnh vảy nến (da liễu)"),
    ("080175", "psoric", "adj", "/ˈsɔːrɪk/", "thuộc bệnh ghẻ ngứa, vảy nến"),
    ("080176", "psst", "intj", "/psst/", "suỵt, suỵt! (tiếng gọi khẽ)"),
    ("080177", "psv", "noun", "/ˌpiːɛsˈviː/", "xe chở khách công cộng (viết tắt)"),
    ("080178", "psych", "verb", "/saɪk/", "lên dây cót tinh thần; đoán tâm lý"),
    ("080179", "psychaesthenia", "noun", "/ˌsaɪkɪsˈθiːniə/", "chứng suy nhược tâm thần (ám ảnh)"),
    ("080180", "psychaesthenic", "adj", "/ˌsaɪkɪsˈθɛnɪk/", "mắc chứng suy nhược tâm thần"),
    ("080181", "psychanalysis", "noun", "/ˌsaɪkəˈnæləsɪs/", "phân tâm học (biến thể ít dùng)"),
    ("080182", "psyched", "verb", "/saɪkt/", "đã khích lệ tinh thần; đã làm hốt"),
    ("080183", "psychedelias", "noun", "/ˌsaɪkəˈdiːljəz/", "văn hóa ảo giác, nghệ thuật sặc sỡ"),
    ("080184", "psychedelically", "adv", "/ˌsaɪkəˈdɛlɪkli/", "theo kiểu ảo giác, sặc sỡ kỳ ảo"),
    ("080185", "psyches", "verb", "/saɪks/", "khích lệ tinh thần; đọc vị đối thủ"),
    ("080186", "psychiatrical", "adj", "/ˌsaɪkiˈætrɪkəl/", "thuộc ngành tâm thần học"),
    ("080187", "psychiatrically", "adv", "/ˌsaɪkiˈætrɪkli/", "về mặt tâm thần học"),
    ("080188", "psychiatries", "noun", "/səˈkaɪətriz/", "các chuyên ngành tâm thần học"),
    ("080189", "psychiatrists", "noun", "/səˈkaɪətrɪsts/", "các bác sĩ chuyên khoa tâm thần"),
    ("080190", "psychicism", "noun", "/ˈsaɪkəˌsɪzəm/", "thuyết tâm linh, tính siêu linh"),
    ("080191", "psychics", "noun", "/ˈsaɪkɪks/", "những nhà ngoại cảm; tâm linh học"),
    ("080192", "psyching", "verb", "/ˈsaɪkɪŋ/", "lên dây cót; dò xét tâm lý"),
    ("080193", "psychoanalysed", "verb", "/ˌsaɪkoʊˈænəˌlaɪzd/", "đã phân tâm trị liệu (Anh)"),
    ("080194", "psychoanalyses", "verb", "/ˌsaɪkoʊˈænəˌlaɪzɪz/", "phân tâm trị liệu (Anh)"),
    ("080195", "psychoanalysing", "verb", "/ˌsaɪkoʊˈænəˌlaɪzɪŋ/", "phân tâm trị liệu (Anh)"),
    ("080196", "psychoanalytically", "adv", "/ˌsaɪkoʊænəˈlɪtɪkli/", "theo phương pháp phân tâm học"),
    ("080197", "psychoanalyzed", "verb", "/ˌsaɪkoʊˈænəˌlaɪzd/", "đã phân tâm trị liệu"),
    ("080198", "psychoanalyzes", "verb", "/ˌsaɪkoʊˈænəˌlaɪzɪz/", "phân tâm trị liệu"),
    ("080199", "psychoanalyzing", "verb", "/ˌsaɪkoʊˈænəˌlaɪzɪŋ/", "phân tâm trị liệu"),
    ("080200", "psychodid", "noun", "/saɪˈkɑːdɪd/", "con muỗi mắt cánh bướm (Psychodid)"),
    ("080201", "psychodidae", "noun", "/saɪˈkɑːdɪˌdiː/", "họ Muỗi mắt, bướm nhỏ cánh lông"),
    ("080202", "psychogenesis", "noun", "/ˌsaɪkoʊˈdʒɛnəsɪs/", "sự phát sinh tâm lý; bệnh tâm căn"),
]

raw = json.load(open("scratch/b37_r01_raw_p2.json"))
by_id = {f"lex.en.200k.{r[0]}": r for r in records}
out = []
for orig in raw:
    sid, hw, pos, ipa, vi = by_id[orig["id"]]
    assert orig["hw"] == hw, f"{orig['id']}: {orig['hw']} vs {hw}"
    assert 0 < len(vi) <= 35, f"{sid} {hw} len={len(vi)}: {vi}"
    assert "/" not in vi, f"{sid} {hw} slash in vi"
    assert ipa.count("/") == 2 and not ipa.startswith("/ ") and not ipa.endswith(" /"), f"{sid} {hw} bad ipa"
    orig["pos"] = pos
    orig["ipa"] = ipa
    orig["vi"] = vi
    orig["status"] = "reviewed"
    out.append(orig)

assert len(out) == 100
with open("scratch/b37_r01_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r01_p2 saved OK")
