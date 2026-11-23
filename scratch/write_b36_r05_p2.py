import json

rows = [
    ("077103", "platiniferous", "adj", "/ˌplætɪˈnɪfərəs/", "có chứa quặng bạch kim (platin)"),
    ("077104", "platinisation", "noun", "/ˌplætɪnɪˈzeɪʃən/", "sự mạ bạch kim (platin)"),
    ("077105", "platinise", "verb", "/ˈplætɪnaɪz/", "mạ bạch kim; tráng bạch kim"),
    ("077106", "platinite", "noun", "/ˈplætɪnaɪt/", "hợp kim thép niken platinit"),
    ("077107", "platinization", "noun", "/ˌplætɪnɪˈzeɪʃən/", "sự mạ bạch kim (platin)"),
    ("077108", "platinize", "verb", "/ˈplætɪnaɪz/", "mạ bạch kim; tráng bạch kim"),
    ("077109", "platinoid", "noun", "/ˈplætɪnɔɪd/", "hợp kim giả bạch kim platinoid"),
    ("077110", "platinous", "adj", "/ˈplætɪnəs/", "thuộc bạch kim hóa trị hai"),
    ("077111", "platitudinal", "adj", "/ˌplætɪˈtjuːdɪnəl/", "sáo rỗng, nhàm chán"),
    ("077112", "platitudinarian", "noun", "/ˌplætɪˌtjuːdɪˈnɛriən/", "người hay nói điều sáo rỗng"),
    ("077113", "platitudinize", "verb", "/ˌplætɪˈtjuːdɪnaɪz/", "nói toàn lời sáo rỗng nhàm chán"),
    ("077114", "platitudinously", "adv", "/ˌplætɪˈtjuːdɪnəsli/", "một cách sáo rỗng, nhàm chán"),
    ("077115", "platly", "adv", "/ˈplætli/", "một cách thẳng thừng, minh bạch"),
    ("077116", "platonics", "noun", "/pləˈtɒnɪks/", "tình yêu thuần khiết không dục vọng"),
    ("077117", "platonise", "verb", "/ˈpleɪtənaɪz/", "lý tưởng hóa theo triết học Platon"),
    ("077118", "platonistic", "adj", "/ˌpleɪtəˈnɪstɪk/", "thuộc triết học Platon"),
    ("077119", "platonize", "verb", "/ˈpleɪtənaɪz/", "lý tưởng hóa theo triết học Platon"),
    ("077120", "platonum", "noun", "/ˈplætənəm/", "bạch kim (cách viết cũ platinum)"),
    ("077121", "platotude", "noun", "/ˈplætɪtjuːd/", "lời nói sáo rỗng, tẻ nhạt (cổ)"),
    ("077122", "plats", "verb", "/plæts/", "vẽ bản đồ quy hoạch; bện, tết"),
    ("077123", "plattdeutsch", "noun", "/ˈplɑːtˌdɔɪtʃ/", "tiếng Hạ Đức (phương ngữ Đức)"),
    ("077124", "platted", "verb", "/ˈplætɪd/", "đã vẽ bản đồ đất; đã bện, tết"),
    ("077125", "platten", "verb", "/ˈplætən/", "dát phẳng; mặt bàn ép (máy in)"),
    ("077126", "plattensee", "noun", "/ˈplɑːtənzeɪ/", "hồ Balaton (Hungary, tiếng Đức)"),
    ("077127", "platting", "verb", "/ˈplætɪŋ/", "vẽ bản đồ quy hoạch; bện, tết"),
    ("077128", "platycephalic", "adj", "/ˌplætɪsɪˈfælɪk/", "có đầu dẹt, hộp sọ phẳng"),
    ("077129", "platycephalidae", "noun", "/ˌplætɪsɪˈfælɪdiː/", "họ Cá chai (Platycephalidae)"),
    ("077130", "platycerium", "noun", "/ˌplætɪˈsɪriəm/", "chi dương xỉ ổ rồng (Platycerium)"),
    ("077131", "platyctenea", "noun", "/ˌplætɪkˈtiːniə/", "bộ Sứa lược dẹt bò đáy"),
    ("077132", "platyctenean", "noun", "/ˌplætɪkˈtiːniən/", "sứa lược dẹt bò đáy"),
    ("077133", "platydactyl", "adj", "/ˌplætɪˈdæktɪl/", "có ngón chân bẹt (thằn lằn)"),
    ("077134", "platyhelminth", "noun", "/ˌplætɪˈhɛlmɪnθ/", "giun dẹp (ngành Giun dẹp)"),
    ("077135", "platykurtic", "adj", "/ˌplætɪˈkɜːrtɪk/", "có đỉnh phân phối tù (thống kê)"),
    ("077136", "platylobium", "noun", "/ˌplætɪˈloʊbiəm/", "chi cây bụi hoa dẹp Platylobium"),
    ("077137", "platymiscium", "noun", "/ˌplætɪˈmɪʃəm/", "chi gỗ quý Nam Mỹ Platymiscium"),
    ("077138", "platypoecilus", "noun", "/ˌplætɪˈpiːsɪləs/", "chi cá cảnh Xiphophorus (cũ)"),
    ("077139", "platyrhine", "adj", "/ˈplætɪˌraɪn/", "mũi rộng, sống mũi tẹt"),
    ("077140", "platyrhinian", "adj", "/ˌplætɪˈrɪniən/", "mũi rộng; thuộc khỉ Tân Thế giới"),
    ("077141", "platyrrhine", "adj", "/ˈplætɪˌraɪn/", "mũi rộng; thuộc khỉ Tân Thế giới"),
    ("077142", "platyrrhini", "noun", "/ˌplætɪˈraɪnaɪ/", "nhóm Khỉ mũi rộng Tân Thế giới"),
    ("077143", "platyrrhinian", "adj", "/ˌplætɪˈrɪniən/", "mũi rộng; thuộc khỉ Tân Thế giới"),
    ("077144", "platyrrhinic", "adj", "/ˌplætɪˈrɪnɪk/", "có mũi rộng, sống mũi bẹt"),
    ("077145", "platystemon", "noun", "/ˌplætɪˈstiːmən/", "chi hoa anh túc kem (Platystemon)"),
    ("077146", "plauditory", "adj", "/ˈplɔːdɪtɔːri/", "tán dương, ca ngợi, hoan nghênh"),
    ("077147", "plausibleness", "noun", "/ˈplɔːzəbəlnəs/", "tính hợp lý, vẻ có lý đáng tin"),
    ("077148", "plausive", "adj", "/ˈplɔːzɪv/", "tán thưởng; có vẻ hợp lý dễ tin"),
    ("077149", "playability", "noun", "/ˌpleɪəˈbɪlɪti/", "khả năng chơi được (trò chơi)"),
    ("077150", "playact", "verb", "/ˈpleɪækt/", "diễn kịch giả vờ, làm bộ làm tịch"),
    ("077151", "playactor", "noun", "/ˈpleɪˌæktər/", "diễn viên kịch (hay làm bộ)"),
    ("077152", "playbooks", "noun", "/ˈpleɪbʊks/", "sổ chiến thuật; cẩm nang kịch bản"),
    ("077153", "playfellow", "noun", "/ˈpleɪˌfɛloʊ/", "bạn chơi thuở nhỏ (từ cũ)"),
    ("077154", "playgame", "noun", "/ˈpleɪɡeɪm/", "trò chơi trẻ con; trò đùa nghịch"),
    ("077155", "playgoer", "noun", "/ˈpleɪˌɡoʊər/", "người hay đi xem kịch sân khấu"),
    ("077156", "playgoing", "adj", "/ˈpleɪˌɡoʊɪŋ/", "thường xuyên đi xem kịch"),
    ("077157", "playgroup", "noun", "/ˈpleɪɡruːp/", "nhóm trẻ mẫu giáo vui chơi chung"),
    ("077158", "playhouses", "noun", "/ˈpleɪˌhaʊsɪz/", "nhà hát kịch; nhà đồ chơi trẻ em"),
    ("077159", "playmates", "noun", "/ˈpleɪˌmeɪts/", "bạn cùng chơi, bạn thuở thơ ấu"),
    ("077160", "plays", "noun", "/pleɪz/", "vở kịch; lượt chơi; sự vui chơi"),
    ("077161", "playscript", "noun", "/ˈpleɪskrɪpt/", "kịch bản sân khấu"),
    ("077162", "playtester", "noun", "/ˈpleɪˌtɛstər/", "người chơi thử nghiệm trò chơi"),
    ("077163", "playtesters", "noun", "/ˈpleɪˌtɛstərz/", "người chơi thử nghiệm trò chơi"),
    ("077164", "playtherapy", "noun", "/ˈpleɪˌθɛrəpi/", "trị liệu tâm lý qua trò chơi"),
    ("077165", "playwrights", "noun", "/ˈpleɪˌraɪts/", "nhà viết kịch, soạn giả kịch"),
    ("077166", "plc", "noun", "/ˌpiːɛlˈsiː/", "công ty trách nhiệm hữu hạn (PLC)"),
    ("077167", "pleach", "verb", "/pliːtʃ/", "đan tết cành cây làm hàng rào"),
    ("077168", "pleadable", "adj", "/ˈpliːdəbəl/", "có thể viện dẫn để bào chữa"),
    ("077169", "pleaded", "verb", "/ˈpliːdɪd/", "đã bào chữa; đã khẩn khoản van nài"),
    ("077170", "pleadings", "noun", "/ˈpliːdɪŋz/", "hồ sơ tranh tụng; lời khẩn cầu"),
    ("077171", "pleads", "verb", "/pliːdz/", "bào chữa; khẩn khoản van nài"),
    ("077172", "pleasantnesses", "noun", "/ˈplɛzəntnəsɪz/", "vẻ dễ chịu, sự hòa nhã vui vẻ"),
    ("077173", "pleases", "verb", "/ˈpliːzɪz/", "làm hài lòng, làm vui lòng"),
    ("077174", "pleasingness", "noun", "/ˈpliːzɪŋnəs/", "tính dễ ưa, vẻ dễ chịu đẹp lòng"),
    ("077175", "pleasurability", "noun", "/ˌplɛʒərəˈbɪlɪti/", "tính chất mang lại niềm vui thích"),
    ("077176", "pleasurableness", "noun", "/ˈplɛʒərəbəlnəs/", "tính chất thú vị, dễ chịu"),
    ("077177", "pleasured", "verb", "/ˈplɛʒərd/", "đã làm hài lòng, tạo niềm vui"),
    ("077178", "pleasureless", "adj", "/ˈplɛʒərləs/", "buồn tẻ, không có chút niềm vui"),
    ("077179", "pleasures", "verb", "/ˈplɛʒərz/", "làm hài lòng, tạo niềm vui thích"),
    ("077180", "pleasuring", "verb", "/ˈplɛʒərɪŋ/", "làm hài lòng, tạo niềm vui thích"),
    ("077181", "pleated", "verb", "/ˈpliːtɪd/", "đã xếp nếp ly (quần áo, vải)"),
    ("077182", "pleater", "noun", "/ˈpliːtər/", "người hoặc dụng cụ xếp nếp vải"),
    ("077183", "pleats", "verb", "/pliːts/", "xếp nếp ly (quần áo, vải)"),
    ("077184", "plebeianise", "verb", "/plɪˈbiːənaɪz/", "làm cho thành bình dân, thô tục"),
    ("077185", "plebeianism", "noun", "/plɪˈbiːənɪzəm/", "tính chất bình dân, thô thiển"),
    ("077186", "plebeianize", "verb", "/plɪˈbiːənaɪz/", "làm cho thành bình dân, thô tục"),
    ("077187", "plebeianly", "adv", "/plɪˈbiːənli/", "một cách bình dân, tầm thường"),
    ("077188", "plebiscitary", "adj", "/plɪˈbɪsɪtəri/", "thuộc cuộc trưng cầu dân ý"),
    ("077189", "plebs", "noun", "/plɛbz/", "tầng lớp bình dân (La Mã cổ)"),
    ("077190", "plecopteran", "noun", "/plɪˈkɒptərən/", "bọ cánh úp đá (bộ Plecoptera)"),
    ("077191", "plecotus", "noun", "/plɪˈkoʊtəs/", "chi dơi tai dài (Plecotus)"),
    ("077192", "plectania", "noun", "/plɛkˈteɪniə/", "chi nấm cốc đen (Plectania)"),
    ("077193", "plectognath", "noun", "/ˈplɛktəɡnæθ/", "cá bộ Cá nóc (cá nóc, cá bò)"),
    ("077194", "plectognathi", "noun", "/plɛkˈtɒɡnəθaɪ/", "bộ Cá nóc cũ (Tetraodontiformes)"),
    ("077195", "plectomycetes", "noun", "/ˌplɛktoʊmaɪˈsiːtiːz/", "lớp nấm túi kín Plectomycetes"),
    ("077196", "plectophera", "noun", "/plɛkˈtɒfərə/", "bộ Phù du (cách gọi cũ)"),
    ("077197", "plectorrhiza", "noun", "/ˌplɛktəˈraɪzə/", "chi phong lan rễ bện Plectorrhiza"),
    ("077198", "plectra", "noun", "/ˈplɛktrə/", "miếng gảy đàn (phím gảy)"),
    ("077199", "plectron", "noun", "/ˈplɛktrɒn/", "miếng gảy đàn (plectrum)"),
    ("077200", "plectrophenax", "noun", "/ˌplɛktroʊˈfiːnæks/", "chi chim sẻ tuyết (Plectrophenax)"),
    ("077201", "pled", "verb", "/plɛd/", "đã bào chữa; đã khẩn nài (quá khứ)"),
    ("077202", "pledges", "verb", "/ˈplɛdʒɪz/", "cam kết, thề hứa; thế chấp, cầm cố"),
]

with open("scratch/b36_r05_raw_p2.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r05_p2.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r05_p2 saved OK")
