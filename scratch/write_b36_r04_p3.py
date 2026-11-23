import json

rows = [
    ("076703", "pinckneya", "noun", "/pɪŋkˈniːə/", "chi cây bụi hoa bắc Pinckneya"),
    ("076704", "pindolol", "noun", "/ˈpɪndəlɒl/", "thuốc tim mạch pindolol"),
    ("076705", "pinealoma", "noun", "/ˌpɪniəˈloʊmə/", "u tuyến tùng (u não hiếm gặp)"),
    ("076706", "pineapples", "noun", "/ˈpaɪnˌæpəlz/", "quả dứa, quả thơm"),
    ("076707", "pined", "verb", "/paɪnd/", "đã nhớ nhung mòn mỏi, héo hon"),
    ("076708", "pinery", "noun", "/ˈpaɪnəri/", "vườn trồng dứa; rừng cây thông"),
    ("076709", "pines", "verb", "/paɪnz/", "nhớ nhung mòn mỏi, héo hon"),
    ("076710", "pinesap", "noun", "/ˈpaɪnsæp/", "cây ký sinh rễ thông (Monotropa)"),
    ("076711", "pineus", "noun", "/ˈpaɪniəs/", "chi rệp sáp hại thông (Pineus)"),
    ("076712", "pineweed", "noun", "/ˈpaɪnwiːd/", "cỏ ban lá thông (Hypericum)"),
    ("076713", "pinfish", "noun", "/ˈpɪnfɪʃ/", "cá tráp gai vây pinfish"),
    ("076714", "pinged", "verb", "/pɪŋd/", "đã gửi tín hiệu ping; kêu boong"),
    ("076715", "pinging", "verb", "/ˈpɪŋɪŋ/", "gửi tín hiệu ping; kêu boong"),
    ("076716", "pings", "verb", "/pɪŋz/", "gửi tín hiệu ping; kêu boong"),
    ("076717", "pinguecula", "noun", "/pɪŋˈɡwɛkjələ/", "mộng mỡ kết mạc mắt (nhãn khoa)"),
    ("076718", "pinguid", "adj", "/ˈpɪŋɡwɪd/", "béo ngậy, nhiều mỡ, nhờn (văn)"),
    ("076719", "pinguin", "noun", "/ˈpɪŋɡwɪn/", "cây dứa gai pinguin (Bromelia)"),
    ("076720", "pinguinus", "noun", "/pɪŋˈɡwaɪnəs/", "chim anca lớn tuyệt chủng"),
    ("076721", "pinicola", "noun", "/pɪˈnɪkələ/", "chi chim sẻ thông (Pinicola)"),
    ("076722", "pinioning", "verb", "/ˈpɪnjənɪŋ/", "trói khuỷu tay; cắt lông cánh chim"),
    ("076723", "pinions", "verb", "/ˈpɪnjənz/", "trói khuỷu tay; cắt lông cánh chim"),
    ("076724", "pinite", "noun", "/ˈpɪnaɪt/", "khoáng vật mica biến tính pinit"),
    ("076725", "pinked", "verb", "/pɪŋkt/", "đã cắt mép răng cưa; đâm nhẹ kiếm"),
    ("076726", "pinkies", "noun", "/ˈpɪŋkiz/", "ngón tay út (khẩu ngữ)"),
    ("076727", "pinkify", "verb", "/ˈpɪŋkɪfaɪ/", "nhuộm màu hồng, làm hồng lên"),
    ("076728", "pinking", "verb", "/ˈpɪŋkɪŋ/", "cắt mép răng cưa; tiếng gõ động cơ"),
    ("076729", "pinkishness", "noun", "/ˈpɪŋkɪʃnəs/", "sắc hơi hồng, màu hồng nhạt"),
    ("076730", "pinkroot", "noun", "/ˈpɪŋkruːt/", "cây rễ hồng trị giun (Spigelia)"),
    ("076731", "pinks", "verb", "/pɪŋks/", "cắt mép răng cưa; tiếng gõ động cơ"),
    ("076732", "pinnae", "noun", "/ˈpɪniː/", "vành tai ngoài; lá chét; vây cá"),
    ("076733", "pinnal", "adj", "/ˈpɪnəl/", "thuộc vành tai ngoài; dạng lông"),
    ("076734", "pinnated", "adj", "/ˈpɪneɪtɪd/", "có lá chét mọc đối hình lông chim"),
    ("076735", "pinnatiped", "noun", "/pɪˈnætɪpɛd/", "chim chân ngón có màng bơi"),
    ("076736", "pinnatisect", "adj", "/pɪˈnætɪsɛkt/", "xẻ thùy sâu dạng lông chim (lá)"),
    ("076737", "pinned", "verb", "/pɪnd/", "đã ghim chặt, kẹp giữ, gắn đinh"),
    ("076738", "pinnipedia", "noun", "/ˌpɪnɪˈpiːdiə/", "phân bộ Chân màng (hải cẩu, sư tử)"),
    ("076739", "pinnothere", "noun", "/ˈpɪnoʊθɪr/", "cua đậu cộng sinh trong vỏ trai"),
    ("076740", "pinnotheres", "noun", "/ˌpɪnoʊˈθɪriːz/", "chi cua đậu (Pinnotheres)"),
    ("076741", "pinnotheridae", "noun", "/ˌpɪnoʊˈθɛrɪdiː/", "họ Cua đậu (Pinnotheridae)"),
    ("076742", "pinnules", "noun", "/ˈpɪnjuːlz/", "lá chét nhỏ cấp hai (dương xỉ)"),
    ("076743", "pinocle", "noun", "/ˈpiːnʌkəl/", "trò chơi bài pinochle"),
    ("076744", "pinocytotic", "adj", "/ˌpaɪnoʊsaɪˈtɒtɪk/", "thuộc hiện tượng ẩm bào (tế bào)"),
    ("076745", "pinophytina", "noun", "/ˌpaɪnoʊfaɪˈtaɪnə/", "phân ngành Thông (Pinophytina)"),
    ("076746", "pinopsida", "noun", "/paɪˈnɒpsɪdə/", "lớp Thông (Pinopsida)"),
    ("076747", "pinpointed", "verb", "/ˈpɪnˌpɔɪntɪd/", "đã định vị chính xác, chỉ rõ"),
    ("076748", "pinpointing", "verb", "/ˈpɪnˌpɔɪntɪŋ/", "định vị chính xác, chỉ rõ chi tiết"),
    ("076749", "pinpoints", "verb", "/ˈpɪnˌpɔɪnts/", "định vị chính xác, chỉ rõ chi tiết"),
    ("076750", "pins", "verb", "/pɪnz/", "ghim chặt, kẹp giữ, cài nút"),
    ("076751", "piny", "adj", "/ˈpaɪni/", "nhiều cây thông; có mùi nhựa thông"),
    ("076752", "pioneered", "verb", "/ˌpaɪəˈnɪrd/", "đã tiên phong, mở đường, đi đầu"),
    ("076753", "pioneering", "verb", "/ˌpaɪəˈnɪrɪŋ/", "tiên phong, mở đường, đi đầu"),
    ("076754", "pioneers", "verb", "/ˌpaɪəˈnɪrz/", "tiên phong, mở đường, đi đầu"),
    ("076755", "pipage", "noun", "/ˈpaɪpɪdʒ/", "việc dẫn bằng đường ống; cước ống"),
    ("076756", "piped", "verb", "/paɪpt/", "đã dẫn ống; thổi sáo; hót véo von"),
    ("076757", "pipefiter", "noun", "/ˈpaɪpˌfɪtər/", "thợ lắp đặt đường ống nước, hơi"),
    ("076758", "pipeful", "noun", "/ˈpaɪpfʊl/", "lượng thuốc nhồi đầy một tẩu"),
    ("076759", "piperaceae", "noun", "/ˌpɪpəˈreɪsiː/", "họ Hồ tiêu (Piperaceae)"),
    ("076760", "piperaceous", "adj", "/ˌpɪpəˈreɪʃəs/", "thuộc họ Hồ tiêu"),
    ("076761", "piperales", "noun", "/ˌpɪpəˈreɪliːz/", "bộ Hồ tiêu (Piperales)"),
    ("076762", "piperazin", "noun", "/paɪˈpɛrəzɪn/", "thuốc tẩy giun piperazin"),
    ("076763", "piperic", "adj", "/paɪˈpɛrɪk/", "thuộc axit piperic (từ hồ tiêu)"),
    ("076764", "piperin", "noun", "/ˈpaɪpərɪn/", "chất cay piperin (trong hạt tiêu)"),
    ("076765", "piperocaine", "noun", "/ˌpɪpəroʊˈkeɪn/", "thuốc gây tê tại chỗ piperocain"),
    ("076766", "pipes", "verb", "/paɪps/", "dẫn ống; thổi sáo; hót véo von"),
    ("076767", "pipewort", "noun", "/ˈpaɪpwɜːrt/", "cây cỏ dùi trống (Eriocaulaceae)"),
    ("076768", "pipidae", "noun", "/ˈpɪpɪdiː/", "họ Ếch không lưỡi (Pipidae)"),
    ("076769", "pipile", "noun", "/pɪˈpiːleɪ/", "chi gà tây rừng Nam Mỹ (Pipile)"),
    ("076770", "pipilo", "noun", "/ˈpɪpɪloʊ/", "chi chim sẻ bụi towhee (Pipilo)"),
    ("076771", "pipistrel", "noun", "/ˈpɪpɪstrɛl/", "dơi muỗi pipistrel"),
    ("076772", "pipkin", "noun", "/ˈpɪpkɪn/", "nồi đất nung nhỏ có tay cầm"),
    ("076773", "pipkins", "noun", "/ˈpɪpkɪnz/", "nồi đất nung nhỏ có tay cầm"),
    ("076774", "pipped", "verb", "/pɪpt/", "đã thắng sít sao; mổ vỏ trứng ra"),
    ("076775", "pipping", "verb", "/ˈpɪpɪŋ/", "thắng sít sao; mổ vỏ trứng chui ra"),
    ("076776", "pipra", "noun", "/ˈpɪprə/", "chi chim manakin (Pipra)"),
    ("076777", "pipracil", "noun", "/ˈpɪprəsɪl/", "kháng sinh piperacillin (Pipracil)"),
    ("076778", "pipridae", "noun", "/ˈpɪprɪdiː/", "họ Chim manakin (Pipridae)"),
    ("076779", "pips", "verb", "/pɪps/", "thắng sít sao; kêu bíp; mổ vỏ trứng"),
    ("076780", "pipsissewa", "noun", "/pɪpˈsɪsəwə/", "cây thảo dược mùa đông pipsissewa"),
    ("076781", "pipsqueak", "noun", "/ˈpɪpˌskwiːk/", "người nhỏ thó tầm thường"),
    ("076782", "piptadenia", "noun", "/ˌpɪptəˈdiːniə/", "chi cây gỗ họ Đậu (Piptadenia)"),
    ("076783", "pipturus", "noun", "/pɪpˈtjʊrəs/", "chi cây gai sợi Thái Bình Dương"),
    ("076784", "pipul", "noun", "/ˈpiːpəl/", "cây bồ đề (Ficus religiosa)"),
    ("076785", "pipy", "adj", "/ˈpaɪpi/", "giống ống rỗng; giọng lanh lảnh"),
    ("076786", "piquance", "noun", "/ˈpiːkəns/", "vị cay nồng; nét hóm hỉnh sắc sảo"),
    ("076787", "piquantly", "adv", "/ˈpiːkəntli/", "với vị cay nồng; sắc sảo hóm hỉnh"),
    ("076788", "piquantness", "noun", "/ˈpiːkəntnəs/", "vị cay nồng hấp dẫn; nét dí dỏm"),
    ("076789", "piqued", "verb", "/piːkt/", "đã làm phật lòng; khơi gợi tò mò"),
    ("076790", "piqueria", "noun", "/pɪˈkwɛriə/", "chi cây thảo nhiệt đới Piqueria"),
    ("076791", "piques", "verb", "/piːks/", "làm phật lòng; khơi gợi tò mò"),
    ("076792", "piquing", "verb", "/ˈpiːkɪŋ/", "làm phật lòng; khơi gợi tò mò"),
    ("076793", "piragua", "noun", "/pɪˈrɑːɡwə/", "thuyền độc mộc; thuyền hai buồm"),
    ("076794", "pirana", "noun", "/pɪˈrɑːnjə/", "cá răng cưa ăn thịt piranha"),
    ("076795", "piranga", "noun", "/pɪˈræŋɡə/", "chi chim sẻ đỏ tanager (Piranga)"),
    ("076796", "pirated", "verb", "/ˈpaɪrətɪd/", "đã sao chép lậu; cướp trên biển"),
    ("076797", "pirates", "verb", "/ˈpaɪrəts/", "sao chép lậu; cướp trên biển"),
    ("076798", "piratic", "adj", "/paɪˈrætɪk/", "mang tính cướp biển; ăn cướp lậu"),
    ("076799", "piratically", "adv", "/paɪˈrætɪkli/", "theo kiểu cướp biển; sao chép lậu"),
    ("076800", "pirating", "verb", "/ˈpaɪrətɪŋ/", "sao chép lậu; cướp trên biển"),
    ("076801", "pirogi", "noun", "/pɪˈroʊɡi/", "bánh nhân hấp luộc pierogi (Ba Lan)"),
    ("076802", "piroplasm", "noun", "/ˈpaɪrəplæzəm/", "ký sinh trùng hồng cầu piroplasm"),
]

with open("scratch/b36_r04_raw_p3.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r04_p3.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r04_p3 saved OK")
