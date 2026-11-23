import json

rows = [
    ("075503", "pericranium", "noun", "/ˌpɛrɪˈkreɪniəm/", "màng ngoài xương sọ; hộp sọ"),
    ("075504", "pericycle", "noun", "/ˈpɛrɪˌsaɪkəl/", "tầng trụ bì (thực vật học)"),
    ("075505", "pericyclic", "adj", "/ˌpɛrɪˈsaɪklɪk/", "thuộc tầng trụ bì (thực vật học)"),
    ("075506", "periderm", "noun", "/ˈpɛrɪdɜːrm/", "chu bì (lớp vỏ bần thực vật)"),
    ("075507", "peridermal", "adj", "/ˌpɛrɪˈdɜːrməl/", "thuộc chu bì (thực vật học)"),
    ("075508", "peridermic", "adj", "/ˌpɛrɪˈdɜːrmɪk/", "thuộc chu bì (thực vật học)"),
    ("075509", "peridinian", "noun", "/ˌpɛrɪˈdɪniən/", "trùng hai roi Peridinium"),
    ("075510", "peridiniidae", "noun", "/ˌpɛrɪdɪˈnaɪɪdiː/", "họ Tảo hai roi (Peridiniidae)"),
    ("075511", "peridotic", "adj", "/ˌpɛrɪˈdɒtɪk/", "thuộc đá peridotit, ngọc peridot"),
    ("075512", "peridrome", "noun", "/ˈpɛrɪdroʊm/", "hành lang bao quanh đền Hy Lạp cổ"),
    ("075513", "perigeal", "adj", "/ˌpɛrɪˈdʒiːəl/", "thuộc điểm cận địa (thiên văn)"),
    ("075514", "perigean", "adj", "/ˌpɛrɪˈdʒiːən/", "thuộc điểm cận địa (thủy triều)"),
    ("075515", "perigon", "noun", "/ˈpɛrɪɡɒn/", "góc đầy 360 độ (hình học)"),
    ("075516", "perigonal", "adj", "/pəˈrɪɡənəl/", "thuộc bao hoa (thực vật học)"),
    ("075517", "perigone", "noun", "/ˈpɛrɪɡoʊn/", "bao hoa (thực vật học)"),
    ("075518", "perigonium", "noun", "/ˌpɛrɪˈɡoʊniəm/", "bao hoa; màng bao túi tinh rêu"),
    ("075519", "perigynia", "noun", "/ˌpɛrɪˈdʒɪniə/", "lá bắc bao quả (chi Cói Carex)"),
    ("075520", "perigynium", "noun", "/ˌpɛrɪˈdʒɪniəm/", "lá bắc bao quả (chi Cói Carex)"),
    ("075521", "perigynous", "adj", "/pəˈrɪdʒɪnəs/", "có hoa đính quanh bầu (thực vật)"),
    ("075522", "perigyny", "noun", "/pəˈrɪdʒɪni/", "tính trạng hoa đính quanh bầu"),
    ("075523", "perihelia", "noun", "/ˌpɛrɪˈhiːliə/", "điểm cận nhật (thiên văn học)"),
    ("075524", "perihelial", "adj", "/ˌpɛrɪˈhiːliəl/", "thuộc điểm cận nhật (thiên văn)"),
    ("075525", "perihepatic", "adj", "/ˌpɛrɪhɪˈpætɪk/", "quanh gan (giải phẫu, y học)"),
    ("075526", "perihysteric", "adj", "/ˌpɛrɪhɪˈstɛrɪk/", "quanh tử cung (giải phẫu)"),
    ("075527", "perijove", "noun", "/ˈpɛrɪˌdʒoʊv/", "điểm cận Mộc (gần sao Mộc nhất)"),
    ("075528", "perikarya", "noun", "/ˌpɛrɪˈkɛriə/", "thân tế bào thần kinh"),
    ("075529", "perikaryon", "noun", "/ˌpɛrɪˈkɛriɒn/", "thân tế bào thần kinh"),
    ("075530", "perilled", "verb", "/ˈpɛrəld/", "đã đặt vào nguy hiểm; mạo hiểm"),
    ("075531", "perilling", "verb", "/ˈpɛrəlɪŋ/", "đặt vào nguy hiểm; mạo hiểm"),
    ("075532", "perilousness", "noun", "/ˈpɛrələsnəs/", "tính chất nguy hiểm, hiểm nghèo"),
    ("075533", "perils", "verb", "/ˈpɛrəlz/", "làm nguy hại; đặt vào nguy hiểm"),
    ("075534", "perilune", "noun", "/ˈpɛrɪˌluːn/", "điểm cận Nguyệt (gần Mặt Trăng)"),
    ("075535", "perilunes", "noun", "/ˈpɛrɪˌluːnz/", "điểm cận Nguyệt (gần Mặt Trăng)"),
    ("075536", "perimetric", "adj", "/ˌpɛrɪˈmɛtrɪk/", "thuộc chu vi; quanh tử cung"),
    ("075537", "perimetrically", "adv", "/ˌpɛrɪˈmɛtrɪkli/", "theo chu vi; bằng thị trường kế"),
    ("075538", "perimorph", "noun", "/ˈpɛrɪmɔːrf/", "tinh thể bao vỏ giả hình (khoáng)"),
    ("075539", "perimysium", "noun", "/ˌpɛrɪˈmɪziəm/", "màng bao bó sợi cơ (giải phẫu)"),
    ("075540", "perinasal", "adj", "/ˌpɛrɪˈneɪzəl/", "quanh mũi; cạnh hốc mũi"),
    ("075541", "perinatologist", "noun", "/ˌpɛrɪneɪˈtɒlədʒɪst/", "bác sĩ chuyên khoa sản chu sinh"),
    ("075542", "perinea", "noun", "/ˌpɛrɪˈniːə/", "đáy chậu; tầng sinh môn (y học)"),
    ("075543", "perineotomy", "noun", "/ˌpɛrɪniˈɒtəmi/", "thủ thuật rạch tầng sinh môn"),
    ("075544", "perinephric", "adj", "/ˌpɛrɪˈnɛfrɪk/", "quanh thận; thuộc bao mỡ thận"),
    ("075545", "perinephrium", "noun", "/ˌpɛrɪˈnɛfriəm/", "bao mỡ quanh thận (giải phẫu)"),
    ("075546", "perineuritis", "noun", "/ˌpɛrɪnjʊˈraɪtɪs/", "viêm bao quanh dây thần kinh"),
    ("075547", "perineurium", "noun", "/ˌpɛrɪˈnjʊriəm/", "màng bao bó sợi thần kinh"),
    ("075548", "periodisation", "noun", "/ˌpɪriədaɪˈzeɪʃən/", "sự phân kỳ (lịch sử, huấn luyện)"),
    ("075549", "periodism", "noun", "/ˈpɪriədɪzəm/", "tính chu kỳ; hiện tượng định kỳ"),
    ("075550", "periodization", "noun", "/ˌpɪriədaɪˈzeɪʃən/", "sự phân kỳ (lịch sử, huấn luyện)"),
    ("075551", "periodogram", "noun", "/pɪˈriːədəɡræm/", "biểu đồ phổ chu kỳ (thống kê)"),
    ("075552", "periodontia", "noun", "/ˌpɛriəˈdɒnʃə/", "chuyên khoa nha chu (răng hàm mặt)"),
    ("075553", "periodontic", "adj", "/ˌpɛriəˈdɒntɪk/", "thuộc nha chu (răng hàm mặt)"),
    ("075554", "periophthalmus", "noun", "/ˌpɛriɒfˈθælməs/", "chi cá thòi lòi (Periophthalmus)"),
    ("075555", "periostea", "noun", "/ˌpɛriˈɒstiə/", "màng ngoài xương (cốt mạc)"),
    ("075556", "periosteal", "adj", "/ˌpɛriˈɒstiəl/", "thuộc màng ngoài xương (cốt mạc)"),
    ("075557", "periostitic", "adj", "/ˌpɛriɒsˈtɪtɪk/", "thuộc bệnh viêm màng xương"),
    ("075558", "periostitis", "noun", "/ˌpɛriɒsˈtaɪtɪs/", "bệnh viêm màng xương (y học)"),
    ("075559", "periostraca", "noun", "/ˌpɛriˈɒstrəkə/", "lớp vỏ sừng ngoài vỏ ốc trai"),
    ("075560", "periostracum", "noun", "/ˌpɛriˈɒstrəkəm/", "lớp vỏ sừng ngoài vỏ ốc trai"),
    ("075561", "periotic", "adj", "/ˌpɛriˈoʊtɪk/", "quanh tai trong; xương đá (tai)"),
    ("075562", "peripatetically", "adv", "/ˌpɛrɪpəˈtɛtɪkli/", "lưu động rày đây mai đó; dạo bước"),
    ("075563", "peripateticism", "noun", "/ˌpɛrɪpəˈtɛtɪsɪzəm/", "trường phái Tiêu dao (Aristotle)"),
    ("075564", "peripatidae", "noun", "/ˌpɛrɪˈpætɪdiː/", "họ Giun nhung (Peripatidae)"),
    ("075565", "peripatopsidae", "noun", "/ˌpɛrɪpəˈtɒpsɪdiː/", "họ Giun nhung phương Nam"),
    ("075566", "peripatopsis", "noun", "/ˌpɛrɪpəˈtɒpsɪs/", "chi giun nhung Peripatopsis"),
    ("075567", "peripatus", "noun", "/pəˈrɪpətəs/", "giun nhung; chi Peripatus"),
    ("075568", "peripetia", "noun", "/ˌpɛrɪpɪˈtiːə/", "bước ngoặt bất ngờ (kịch, văn học)"),
    ("075569", "peripety", "noun", "/ˈpɛrɪpəti/", "bước ngoặt bất ngờ (kịch, văn học)"),
    ("075570", "peripheric", "adj", "/ˌpɛrɪˈfɛrɪk/", "ở ngoại vi, bên rìa ngoài"),
    ("075571", "periphlebitis", "noun", "/ˌpɛrɪflɪˈbaɪtɪs/", "bệnh viêm quanh tĩnh mạch (y học)"),
    ("075572", "periphrases", "noun", "/pəˈrɪfrəsiːz/", "lối nói vòng vo, diễn đạt dài dòng"),
    ("075573", "periphrastically", "adv", "/ˌpɛrɪˈfræstɪkli/", "bằng cách nói vòng vo, giải thích"),
    ("075574", "periphyton", "noun", "/pəˈrɪfɪtɒn/", "sinh vật bám nền dưới nước"),
    ("075575", "periplasm", "noun", "/ˈpɛrɪplæzəm/", "ngoại chất tế bào (vi khuẩn)"),
    ("075576", "periplasmic", "adj", "/ˌpɛrɪˈplæzmɪk/", "thuộc vùng chu chất (vi khuẩn)"),
    ("075577", "periplast", "noun", "/ˈpɛrɪplæst/", "màng bao ngoại chất (nguyên sinh)"),
    ("075578", "periploca", "noun", "/pəˈrɪpləkə/", "chi dây leo tơ liễu (Periploca)"),
    ("075579", "peripneumony", "noun", "/ˌpɛrɪˈnjuːməni/", "bệnh viêm màng phổi và phổi (cổ)"),
    ("075580", "peripteral", "adj", "/pəˈrɪptərəl/", "có hàng cột bao quanh bốn phía"),
    ("075581", "peripterous", "adj", "/pəˈrɪptərəs/", "có hàng cột bao quanh bốn phía"),
    ("075582", "periptery", "noun", "/pəˈrɪptəri/", "đền đài có hàng cột bao quanh"),
    ("075583", "perique", "noun", "/pəˈriːk/", "thuốc lá sợi lên men perique"),
    ("075584", "perisarc", "noun", "/ˈpɛrɪsɑːrk/", "lớp vỏ kitin bao ngoài thủy tức"),
    ("075585", "periscopes", "noun", "/ˈpɛrɪˌskoʊps/", "kính tiềm vọng"),
    ("075586", "periscopic", "adj", "/ˌpɛrɪˈskɒpɪk/", "dạng kính tiềm vọng; trường rộng"),
    ("075587", "periselene", "noun", "/ˌpɛrɪsɪˈliːni/", "điểm cận nguyệt (gần Mặt Trăng)"),
    ("075588", "perishability", "noun", "/ˌpɛrɪʃəˈbɪlɪti/", "tính dễ hư hỏng, mau ôi thiu"),
    ("075589", "perishableness", "noun", "/ˈpɛrɪʃəbəlnəs/", "tính dễ hư hỏng, mau ôi thiu"),
    ("075590", "perishables", "noun", "/ˈpɛrɪʃəbəlz/", "thực phẩm tươi sống dễ hư hỏng"),
    ("075591", "perishably", "adv", "/ˈpɛrɪʃəbli/", "theo cách dễ hư hỏng, mau hỏng"),
    ("075592", "perished", "verb", "/ˈpɛrɪʃt/", "đã diệt vong; bỏ mạng; mục nát"),
    ("075593", "perishes", "verb", "/ˈpɛrɪʃɪz/", "diệt vong; bỏ mạng; mục nát"),
    ("075594", "perishing", "verb", "/ˈpɛrɪʃɪŋ/", "diệt vong; bỏ mạng; mục nát"),
    ("075595", "perishingly", "adv", "/ˈpɛrɪʃɪŋli/", "rét buốt thấu xương; cực kỳ"),
    ("075596", "perisoreus", "noun", "/ˌpɛrɪˈsɔːriəs/", "chi chim giẻ cùi xám (Perisoreus)"),
    ("075597", "perisperm", "noun", "/ˈpɛrɪspɜːrm/", "ngoại nhũ (trong hạt thực vật)"),
    ("075598", "perispheric", "adj", "/ˌpɛrɪˈsfɛrɪk/", "có dạng hình cầu, bao quanh"),
    ("075599", "perissodactyl", "noun", "/pəˌrɪsəˈdæktɪl/", "thú móng guốc lẻ (ngựa, tê giác)"),
    ("075600", "perissodactylate", "adj", "/pəˌrɪsəˈdæktɪlɪt/", "thuộc bộ Móng guốc lẻ"),
    ("075601", "peristalith", "noun", "/pəˈrɪstəlɪθ/", "vòng đá đứng bao quanh gò mộ cổ"),
    ("075602", "peristaltic", "adj", "/ˌpɛrɪˈstæltɪk/", "thuộc nhu động (ống tiêu hóa)"),
]

with open("scratch/b36_r02_raw_p1.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r02_p1.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r02_p1 saved OK")
