import json

RECORDS = [
    ("084403", "ruttish", "adj", "/ˈrʌtɪʃ/", "đang động dục; hừng hực nhục dục"),
    ("084404", "rux", "noun", "/rʌks/", "cơn giận dữ; sự cáu giận"),
    ("084405", "rvb", "noun", "/ˌɑːrˌviːˈbiː/", "liên kết hóa trị cộng hưởng (RVB)"),
    ("084406", "rvn", "noun", "/ˌɑːrˌviːˈɛn/", "Việt Nam Cộng hòa (viết tắt)"),
    ("084407", "rwd", "noun", "/ˌɑːrˌdʌbəljuːˈdiː/", "hệ dẫn động cầu sau (RWD)"),
    ("084408", "rybbly", "adj", "/ˈrʌbli/", "nhiều gạch đá vụn; lởm chởm đá"),
    ("084409", "rynchopidae", "noun", "/rɪŋˈkɑːpɪˌdiː/", "họ Chim xẻng (Rynchopidae)"),
    ("084410", "rynchops", "noun", "/ˈrɪŋkɑːps/", "chi Chim xẻng (Rynchops)"),
    ("084411", "ryot", "noun", "/ˈraɪət/", "nông dân tá điền Ấn Độ"),
    ("084412", "rypticus", "noun", "/ˈrɪptɪkəs/", "chi cá xà phòng Rypticus"),
    ("084413", "saame", "noun", "/ˈsɑːmi/", "người Sami; tiếng Sami"),
    ("084414", "sabadilla", "noun", "/ˌsæbəˈdɪlə/", "cây cỏ loa kèn sabadilla"),
    ("084415", "sabaean", "adj", "/səˈbiːən/", "thuộc vương quốc Saba (Yemen cổ)"),
    ("084416", "sabaism", "noun", "/ˈseɪbiˌɪzəm/", "tục thờ tinh tú sao trời"),
    ("084417", "sabbatia", "noun", "/səˈbeɪtiə/", "chi hoa hồng sao Sabatia"),
    ("084418", "sabbatic", "adj", "/səˈbætɪk/", "thuộc ngày Sa-bát"),
    ("084419", "sabbatise", "verb", "/ˈsæbəˌtaɪz/", "giữ lệ nghỉ ngày Sa-bát"),
    ("084420", "sabbatize", "verb", "/ˈsæbəˌtaɪz/", "giữ lệ nghỉ ngày Sa-bát"),
    ("084421", "sabbatum", "noun", "/ˈsæbətəm/", "ngày lễ Sa-bát"),
    ("084422", "sabean", "adj", "/səˈbiːən/", "thuộc vương quốc Saba (Yemen cổ)"),
    ("084423", "sabertoothed", "adj", "/ˈseɪbərˌtuːθt/", "có răng nanh hình kiếm"),
    ("084424", "sabicu", "noun", "/ˌsɑːbɪˈkuː/", "cây gỗ cứng sabicu Cuba"),
    ("084425", "sabinea", "noun", "/səˈbɪniə/", "chi cây họ Đậu Sabinea"),
    ("084426", "sablefish", "noun", "/ˈseɪbəlˌfɪʃ/", "cá than đen Thái Bình Dương"),
    ("084427", "sabotaged", "verb", "/ˈsæbəˌtɑːʒd/", "đã phá hoại ngầm"),
    ("084428", "sabotages", "verb", "/ˈsæbəˌtɑːʒɪz/", "phá hoại ngầm"),
    ("084429", "sabotaging", "verb", "/ˈsæbəˌtɑːʒɪŋ/", "đang phá hoại ngầm"),
    ("084430", "sabretache", "noun", "/ˈseɪbərˌtæʃ/", "túi da đeo cạnh kiếm kỵ binh"),
    ("084431", "sabreur", "noun", "/sɑːˈbrɜːr/", "kỵ binh đấu kiếm; kiếm sĩ"),
    ("084432", "sabulosity", "noun", "/ˌsæbjəˈlɑːsɪti/", "tính nhiều cát; chất sạn"),
    ("084433", "sabulous", "adj", "/ˈsæbjələs/", "nhiều cát; có sỏi sạn"),
    ("084434", "saccate", "adj", "/ˈsækeɪt/", "hình túi; phồng thành túi"),
    ("084435", "saccharase", "noun", "/ˈsækəˌreɪs/", "enzim phân giải đường saccaraza"),
    ("084436", "saccharate", "noun", "/ˈsækəˌreɪt/", "muối sacarat"),
    ("084437", "saccharic", "adj", "/səˈkærɪk/", "thuộc axit saccaric"),
    ("084438", "sacchariferous", "adj", "/ˌsækəˈrɪfərəs/", "chứa đường; sinh đường"),
    ("084439", "saccharification", "noun", "/səˌkærɪfəˈkeɪʃən/", "quá trình đường hóa tinh bột"),
    ("084440", "saccharify", "verb", "/səˈkærəˌfaɪ/", "đường hóa; chuyển thành đường"),
    ("084441", "saccharimeter", "noun", "/ˌsækəˈrɪmɪtər/", "đường kế phân cực"),
    ("084442", "saccharimeters", "noun", "/ˌsækəˈrɪmɪtərz/", "đường kế phân cực"),
    ("084443", "saccharimetry", "noun", "/ˌsækəˈrɪmətri/", "phép đo nồng độ đường"),
    ("084444", "saccharinity", "noun", "/ˌsækəˈrɪnɪti/", "vị ngọt lịm quá mức"),
    ("084445", "saccharization", "noun", "/ˌsækərəˈzeɪʃən/", "sự đường hóa"),
    ("084446", "saccharize", "verb", "/ˈsækəˌraɪz/", "đường hóa; chuyển thành đường"),
    ("084447", "saccharogenic", "adj", "/ˌsækərəˈdʒɛnɪk/", "sinh đường; tạo thành đường"),
    ("084448", "saccharoid", "adj", "/ˈsækəˌrɔɪd/", "có cấu trúc hạt mịn như đường"),
    ("084449", "saccharometer", "noun", "/ˌsækəˈrɑːmɪtər/", "tỷ trọng kế đo nồng độ đường"),
    ("084450", "saccharometers", "noun", "/ˌsækəˈrɑːmɪtərz/", "tỷ trọng kế đo nồng độ đường"),
    ("084451", "saccharomycetaceae", "noun", "/ˌsækəroʊˌmaɪsɪˈteɪsiːˌiː/", "họ Nấm men bia"),
    ("084452", "saccharose", "noun", "/ˈsækəˌroʊs/", "đường mía saccarozơ"),
    ("084453", "sacciform", "adj", "/ˈsæksɪˌfɔːrm/", "có hình túi"),
    ("084454", "saccular", "adj", "/ˈsækjələr/", "dạng túi nhỏ; thuộc cầu nang tai"),
    ("084455", "sacculate", "adj", "/ˈsækjəlɪt/", "chia thành từng túi nhỏ"),
    ("084456", "sacculated", "adj", "/ˈsækjəˌleɪtɪd/", "chia thành từng túi nhỏ"),
    ("084457", "saccules", "noun", "/ˈsækjuːlz/", "túi nhỏ; cầu nang tai trong"),
    ("084458", "saccus", "noun", "/ˈsækəs/", "túi; khoang túi (giải phẫu)"),
    ("084459", "sacellum", "noun", "/səˈsɛləm/", "miếu nhỏ; điện thờ nhỏ (La Mã)"),
    ("084460", "sacerdocy", "noun", "/ˈsæsərdoʊsi/", "chức tư tế; giới tăng lữ"),
    ("084461", "sacerdotage", "noun", "/ˌsæsərˈdoʊtɪdʒ/", "chế độ thần quyền tăng lữ"),
    ("084462", "sacerdotalism", "noun", "/ˌsæsərˈdoʊtəˌlɪzəm/", "chủ nghĩa tăng lữ quyền"),
    ("084463", "sachems", "noun", "/ˈseɪtʃəmz/", "tù trưởng bộ lạc Bắc Mỹ"),
    ("084464", "sacker", "noun", "/ˈsækər/", "kẻ cướp phá; máy đóng bao"),
    ("084465", "sackings", "noun", "/ˈsækɪŋz/", "vụ sa thải; vụ cướp phá"),
    ("084466", "sackless", "adj", "/ˈsækləs/", "ngây thơ; vô tội; khờ khạo"),
    ("084467", "sacks", "verb", "/sæks/", "sa thải; cướp phá; đóng bao"),
    ("084468", "saclant", "noun", "/ˈsækˌlænt/", "Bộ Tư lệnh Đồng minh Đại Tây Dương"[:35]),
    ("084469", "saclike", "adj", "/ˈsækˌlaɪk/", "có hình dạng túi"),
    ("084470", "sacque", "noun", "/sæk/", "áo khoác dáng suông rộng"),
    ("084471", "sacra", "noun", "/ˈseɪkrə/", "xương cùng; vật thánh hiến"),
    ("084472", "sacramentalism", "noun", "/ˌsækrəˈmɛntəˌlɪzəm/", "thuyết hiệu lực bí tích"),
    ("084473", "sacramentalist", "noun", "/ˌsækrəˈmɛntəlɪst/", "người đề cao bí tích"),
    ("084474", "sacramentarian", "noun", "/ˌsækrəmənˈtɛriən/", "người theo thuyết biểu tượng bí tích"[:35]),
    ("084475", "sacramentarianism", "noun", "/ˌsækrəmənˈtɛriəˌnɪzəm/", "thuyết biểu tượng bí tích"),
    ("084476", "sacramentaries", "noun", "/ˌsækrəˈmɛntəriz/", "sách nghi thức bí tích xưa"),
    ("084477", "sacramentary", "adj", "/ˌsækrəˈmɛntəri/", "thuộc nghi lễ bí tích"),
    ("084478", "sacramented", "verb", "/ˈsækrəˌmɛntɪd/", "đã ban bí tích; đã thề thiêng liêng"[:35]),
    ("084479", "sacramenting", "verb", "/ˈsækrəˌmɛntɪŋ/", "đang ban bí tích"),
    ("084480", "sacraments", "verb", "/ˈsækrəmənts/", "ban bí tích; thề nguyền thiêng liêng"[:35]),
    ("084481", "sacraria", "noun", "/səˈkrɛriə/", "bể xả nước thánh; nội điện"),
    ("084482", "sacrarium", "noun", "/səˈkrɛriəm/", "bể xả nước thánh trong nhà thờ"),
    ("084483", "sacrificeable", "adj", "/ˈsækrəˌfaɪsəbəl/", "có thể hiến tế; có thể hy sinh"),
    ("084484", "sacrificed", "verb", "/ˈsækrəˌfaɪst/", "đã hy sinh; đã hiến tế"),
    ("084485", "sacrificers", "noun", "/ˈsækrəˌfaɪsərz/", "người hy sinh; thầy tế lễ"),
    ("084486", "sacrifices", "verb", "/ˈsækrəˌfaɪsɪz/", "hy sinh; hiến tế"),
    ("084487", "sacrificially", "adv", "/ˌsækrəˈfɪʃəli/", "mang tính hy sinh; như vật hiến tế"[:35]),
    ("084488", "sacrificing", "verb", "/ˈsækrəˌfaɪsɪŋ/", "đang hy sinh; đang hiến tế"),
    ("084489", "sacrileges", "noun", "/ˈsækrəlɪdʒɪz/", "hành vi báng bổ; tội phạm thánh"),
    ("084490", "sacrilegiously", "adv", "/ˌsækrəˈlɪdʒəsli/", "báng bổ; xúc phạm chốn thiêng"),
    ("084491", "sacrilegiousness", "noun", "/ˌsækrəˈlɪdʒəsnəs/", "tính báng bổ; sự phạm thánh"),
    ("084492", "sacrilegist", "noun", "/ˈsækrəlɪdʒɪst/", "kẻ phạm thánh; kẻ báng bổ"),
    ("084493", "sacring", "noun", "/ˈseɪkrɪŋ/", "nghi thức dâng bánh thánh; lễ phong"[:35]),
    ("084494", "sacrist", "noun", "/ˈseɪkrɪst/", "người giữ đồ thánh nhà thờ"),
    ("084495", "sacrocaudal", "adj", "/ˌseɪkroʊˈkɔːdəl/", "thuộc xương cùng và xương đuôi"),
    ("084496", "sacrococcygeal", "adj", "/ˌseɪkroʊkɑːkˈsɪdʒiəl/", "thuộc xương cùng cụt"),
    ("084497", "sacrolumbar", "adj", "/ˌseɪkroʊˈlʌmbər/", "thuộc xương cùng thắt lưng"),
    ("084498", "sacrosciatic", "adj", "/ˌseɪkroʊsaɪˈætɪk/", "thuộc xương cùng và xương ngồi"),
    ("084499", "sacrospinal", "adj", "/ˌseɪkroʊˈspaɪnəl/", "thuộc xương cùng và cột sống"),
    ("084500", "sacrovertebral", "adj", "/ˌseɪkroʊˈvɜːrtəbrəl/", "thuộc xương cùng và đốt sống"),
    ("084501", "sacs", "noun", "/sæks/", "túi sinh học; bao nhỏ"),
    ("084502", "sadder", "adj", "/ˈsædər/", "buồn hơn; thảm hơn"),
]

# Shorten those cleanly instead of slices
RECORDS[65] = ("084468", "saclant", "noun", "/ˈsækˌlænt/", "Tư lệnh Đồng minh Đại Tây Dương")
RECORDS[71] = ("084474", "sacramentarian", "noun", "/ˌsækrəmənˈtɛriən/", "người theo thuyết biểu tượng")
RECORDS[75] = ("084478", "sacramented", "verb", "/ˈsækrəˌmɛntɪd/", "đã ban bí tích; đã thề nguyện")
RECORDS[77] = ("084480", "sacraments", "verb", "/ˈsækrəmənts/", "ban bí tích; thề nguyện")
RECORDS[84] = ("084487", "sacrificially", "adv", "/ˌsækrəˈfɪʃəli/", "mang tính hy sinh; để hiến tế")
RECORDS[90] = ("084493", "sacring", "noun", "/ˈseɪkrɪŋ/", "lễ dâng bánh thánh; lễ đăng quang")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r09_raw_p5.json"))
by_id = {r["id"].split(".")[-1]: r for r in raw}
out = []
for sid, hw, pos, ipa, vi in RECORDS:
    rec = dict(by_id[sid])
    assert rec["hw"] == hw, (sid, hw, rec["hw"])
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

json.dump(out, open("scratch/b37_r09_reviewed_p5.json", "w"), ensure_ascii=False, indent=2)
print("b37_r09_p5 saved OK")
