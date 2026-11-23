import json

rows = [
    ("077003", "planography", "noun", "/pləˈnɒɡrəfi/", "kỹ thuật in phẳng (litho)"),
    ("077004", "planometrics", "noun", "/ˌplænəˈmɛtrɪks/", "kế hoạch lượng (kinh tế học)"),
    ("077005", "plans", "verb", "/plænz/", "lên kế hoạch, dự định, vẽ thiết kế"),
    ("077006", "planta", "noun", "/ˈplæntə/", "lòng bàn chân; đốt bàn chân"),
    ("077007", "plantable", "adj", "/ˈplæntəbəl/", "có thể trồng trọt được"),
    ("077008", "plantaginaceae", "noun", "/plænˌtædʒɪˈneɪsiː/", "họ Mã đề (Plantaginaceae)"),
    ("077009", "plantaginales", "noun", "/plænˌtædʒɪˈneɪliːz/", "bộ Mã đề (Plantaginales)"),
    ("077010", "plantal", "adj", "/ˈplæntəl/", "thuộc thực vật, cây cối"),
    ("077011", "planten", "noun", "/ˈplæntən/", "cây chuối lớn (cách viết cổ)"),
    ("077012", "planters", "noun", "/ˈplæntərz/", "chủ đồn điền; chậu trồng cây"),
    ("077013", "plantlet", "noun", "/ˈplæntlɪt/", "cây con nhỏ (mọc từ cây mẹ)"),
    ("077014", "plants", "noun", "/plænts/", "thực vật, cây cối; nhà máy"),
    ("077015", "plantula", "noun", "/ˈplæntjʊlə/", "đệm vuốt chân côn trùng"),
    ("077016", "planula", "noun", "/ˈplænjʊlə/", "ấu trùng bơi của ruột khoang"),
    ("077017", "planular", "adj", "/ˈplænjʊlər/", "thuộc ấu trùng planula"),
    ("077018", "planuloid", "adj", "/ˈplænjʊlɔɪd/", "có dạng như ấu trùng planula"),
    ("077019", "planum", "noun", "/ˈpleɪnəm/", "mặt phẳng giải phẫu (xương, não)"),
    ("077020", "plashed", "verb", "/plæʃt/", "đã tạt nước bắn tung tóe; đan cành"),
    ("077021", "plashes", "verb", "/ˈplæʃɪz/", "tạt nước bắn tung tóe; đan cành"),
    ("077022", "plashing", "verb", "/ˈplæʃɪŋ/", "tạt nước bắn tung tóe; đan cành"),
    ("077023", "plashy", "adj", "/ˈplæʃi/", "lầy lội đầy vũng nước; loang lổ"),
    ("077024", "plasmablast", "noun", "/ˈplæzməˌblæst/", "nguyên bào tương bào (miễn dịch)"),
    ("077025", "plasmacyte", "noun", "/ˈplæzməˌsaɪt/", "tương bào (tế bào miễn dịch)"),
    ("077026", "plasmacytes", "noun", "/ˈplæzməˌsaɪts/", "tương bào (tế bào miễn dịch)"),
    ("077027", "plasmagene", "noun", "/ˈplæzməˌdʒiːn/", "gen tế bào chất (ngoài nhân)"),
    ("077028", "plasmalemma", "noun", "/ˌplæzməˈlɛmə/", "màng sinh chất tế bào"),
    ("077029", "plasmatic", "adj", "/plæzˈmætɪk/", "thuộc huyết tương, sinh chất"),
    ("077030", "plasmatogamy", "noun", "/plæzməˈtɒɡəmi/", "sự hòa hợp tế bào chất (nấm)"),
    ("077031", "plasmatoparous", "adj", "/ˌplæzməˈtɒpərəs/", "tạo tế bào chất mầm (sinh học)"),
    ("077032", "plasmocyte", "noun", "/ˈplæzməˌsaɪt/", "tương bào; tế bào huyết tương"),
    ("077033", "plasmodesm", "noun", "/ˈplæzməˌdɛzm/", "cầu sinh chất liên bào (thực vật)"),
    ("077034", "plasmodesmid", "noun", "/ˌplæzməˈdɛzmɪd/", "sợi cầu sinh chất liên bào"),
    ("077035", "plasmodial", "adj", "/plæzˈmoʊdiəl/", "thuộc thể hợp bào nhầy (plasmodium)"),
    ("077036", "plasmodiidae", "noun", "/ˌplæzməˈdaɪɪdiː/", "họ Ký sinh trùng sốt rét"),
    ("077037", "plasmodiophora", "noun", "/plæzˌmoʊdiˈɒfərə/", "chi nấm nhầy rễ cải Plasmodiophora"),
    ("077038", "plasmodiophoraceae", "noun", "/plæzˌmoʊdiɒfəˈreɪsiː/", "họ Nấm nhầy rễ cải"),
    ("077039", "plasmogamy", "noun", "/plæzˈmɒɡəmi/", "sự hòa hợp tế bào chất (nấm)"),
    ("077040", "plasmogen", "noun", "/ˈplæzmədʒən/", "chất nguyên sinh tạo sự sống (cổ)"),
    ("077041", "plasmolyse", "verb", "/ˈplæzməlaɪz/", "gây co nguyên sinh (tế bào)"),
    ("077042", "plasmolysis", "noun", "/plæzˈmɒlɪsɪs/", "sự co nguyên sinh (tế bào)"),
    ("077043", "plasmolytic", "adj", "/ˌplæzməˈlɪtɪk/", "thuộc sự co nguyên sinh"),
    ("077044", "plasmolytically", "adv", "/ˌplæzməˈlɪtɪkli/", "theo cơ chế co nguyên sinh"),
    ("077045", "plasmometric", "adj", "/ˌplæzməˈmɛtrɪk/", "thuộc phép đo độ co nguyên sinh"),
    ("077046", "plasmon", "noun", "/ˈplæzmɒn/", "hệ gen ngoài nhân (tế bào chất)"),
    ("077047", "plasmosome", "noun", "/ˈplæzməˌsoʊm/", "hạch nhân thực (sinh học tế bào)"),
    ("077048", "plasmotomy", "noun", "/plæzˈmɒtəmi/", "sự phân cắt hợp bào đa nhân"),
    ("077049", "plasmotype", "noun", "/ˈplæzməˌtaɪp/", "kiểu di truyền tế bào chất"),
    ("077050", "plassom", "noun", "/ˈplæsəm/", "nguyên chất không nhân (biến thể)"),
    ("077051", "plasterers", "noun", "/ˈplæstərərz/", "thợ trát vữa, thợ thạch cao"),
    ("077052", "plasters", "verb", "/ˈplæstərz/", "trát vữa; dán băng gạc; làm quá tải"),
    ("077053", "plasticise", "verb", "/ˈplæstɪsaɪz/", "hóa dẻo, làm tăng độ dẻo"),
    ("077054", "plasticiser", "noun", "/ˈplæstɪˌsaɪzər/", "chất hóa dẻo (phụ gia nhựa)"),
    ("077055", "plasticization", "noun", "/ˌplæstɪsaɪˈzeɪʃən/", "quá trình hóa dẻo vật liệu"),
    ("077056", "plasticize", "verb", "/ˈplæstɪsaɪz/", "hóa dẻo, làm tăng độ dẻo"),
    ("077057", "plasticized", "verb", "/ˈplæstɪsaɪzd/", "đã được hóa dẻo (nhựa, vật liệu)"),
    ("077058", "plasticizes", "verb", "/ˈplæstɪsaɪzɪz/", "hóa dẻo, làm tăng độ dẻo"),
    ("077059", "plasticizing", "verb", "/ˈplæstɪsaɪzɪŋ/", "hóa dẻo, làm tăng độ dẻo"),
    ("077060", "plastidal", "adj", "/ˈplæstɪdəl/", "thuộc lạp thể (lục lạp thực vật)"),
    ("077061", "plastidome", "noun", "/ˈplæstɪˌdoʊm/", "toàn bộ hệ lạp thể trong tế bào"),
    ("077062", "plastidotype", "noun", "/ˈplæstɪdəˌtaɪp/", "kiểu gen hệ lạp thể thực vật"),
    ("077063", "plastidule", "noun", "/ˈplæstɪdjuːl/", "tiểu thể sinh chất giả thuyết (cổ)"),
    ("077064", "plastin", "noun", "/ˈplæstɪn/", "protein gắn kết actin plastin"),
    ("077065", "plastinate", "verb", "/ˈplæstɪneɪt/", "nhựa hóa bảo quản mẫu giải phẫu"),
    ("077066", "plastochondria", "noun", "/ˌplæstəˈkɒndriə/", "ti thể dạng sợi (sinh học cổ)"),
    ("077067", "plastocont", "noun", "/ˈplæstəkɒnt/", "ti thể dạng que (sinh học cổ)"),
    ("077068", "plastocyte", "noun", "/ˈplæstəˌsaɪt/", "tiểu cầu máu; tế bào mang lạp thể"),
    ("077069", "plastodeme", "noun", "/ˈplæstəˌdiːm/", "quần thể biến dị kiểu hình"),
    ("077070", "plastodesma", "noun", "/ˌplæstəˈdɛzmə/", "cầu nối sinh chất (biến thể)"),
    ("077071", "plastogamy", "noun", "/plæˈstɒɡəmi/", "sự hòa hợp tế bào chất"),
    ("077072", "plastogen", "noun", "/ˈplæstədʒən/", "nhân tố di truyền lạp thể"),
    ("077073", "plastokont", "noun", "/ˈplæstəkɒnt/", "ti thể dạng que (sinh học cổ)"),
    ("077074", "plastolysis", "noun", "/plæˈstɒlɪsɪs/", "sự tan rã lạp thể thực vật"),
    ("077075", "plastomere", "noun", "/ˈplæstəmɪr/", "đoạn giữa tinh trùng; mảnh lạp thể"),
    ("077076", "plastorhexis", "noun", "/ˌplæstəˈrɛksɪs/", "sự đứt vỡ lạp thể trong tế bào"),
    ("077077", "plastosome", "noun", "/ˈplæstəˌsoʊm/", "ti thể (cách gọi cũ trong sinh học)"),
    ("077078", "plastral", "adj", "/ˈplæstrəl/", "thuộc yếm bụng rùa; giáp ngực"),
    ("077079", "platalea", "noun", "/pləˈteɪliə/", "chi cò thìa (Platalea)"),
    ("077080", "plataleidae", "noun", "/ˌplætəˈliːɪdiː/", "họ Cò thìa (nhóm cò quăm)"),
    ("077081", "platan", "noun", "/ˈplætən/", "cây chò nước tiêu huyền (Platanus)"),
    ("077082", "platanaceae", "noun", "/ˌplætəˈneɪsiː/", "họ Chò nước (Platanaceae)"),
    ("077083", "platanistidae", "noun", "/ˌplætəˈnɪstɪdiː/", "họ Cá heo sông Ấn (Platanistidae)"),
    ("077084", "platanthera", "noun", "/pləˈtænθərə/", "chi phong lan bướm (Platanthera)"),
    ("077085", "plateaux", "noun", "/plæˈtoʊz/", "cao nguyên; trạng thái chững lại"),
    ("077086", "plated", "verb", "/ˈpleɪtɪd/", "đã mạ kim loại; bọc giáp; bày đĩa"),
    ("077087", "platelayer", "noun", "/ˈpleɪtˌleɪər/", "công nhân lắp đặt bảo trì ray tàu"),
    ("077088", "platelaying", "noun", "/ˈpleɪtˌleɪɪŋ/", "nghề lắp đặt đường ray tàu hỏa"),
    ("077089", "plateletphereses", "noun", "/ˌpleɪtlətˈfɛrɪsiːz/", "kỹ thuật gạn tách tiểu cầu (y học)"),
    ("077090", "plateletpheresis", "noun", "/ˌpleɪtlətˈfɛrɪsɪs/", "kỹ thuật gạn tách tiểu cầu (y học)"),
    ("077091", "platelike", "adj", "/ˈpleɪtˌlaɪk/", "có dạng bản dẹt, dạng tấm mỏng"),
    ("077092", "plateros", "noun", "/plɑːˈtɛroʊs/", "thợ chế tác bạc (Tây Ban Nha)"),
    ("077093", "plates", "verb", "/pleɪts/", "mạ kim loại; bọc giáp; bày lên đĩa"),
    ("077094", "platformed", "verb", "/ˈplætfɔːrmd/", "đã tạo bệ đỡ; đưa lên nền tảng số"),
    ("077095", "platforming", "verb", "/ˈplætfɔːrmɪŋ/", "tạo bệ đỡ; đưa lên nền tảng số"),
    ("077096", "platformist", "noun", "/ˈplætfɔːrmɪst/", "người theo chủ nghĩa cương lĩnh"),
    ("077097", "platformists", "noun", "/ˈplætfɔːrmɪsts/", "người theo chủ nghĩa cương lĩnh"),
    ("077098", "platforms", "verb", "/ˈplætfɔːrmz/", "tạo bệ đỡ; đưa lên nền tảng số"),
    ("077099", "plathelmintha", "noun", "/ˌplætθɛlˈmɪnθə/", "ngành Giun dẹp (Platyhelminthes)"),
    ("077100", "platichthys", "noun", "/pləˈtɪkθɪs/", "chi cá bơn sông (Platichthys)"),
    ("077101", "platiculture", "noun", "/ˈplætɪˌkʌltʃər/", "kỹ thuật nuôi cấy trên đĩa thạch"),
    ("077102", "platinic", "adj", "/pləˈtɪnɪk/", "thuộc bạch kim hóa trị bốn"),
]

with open("scratch/b36_r05_raw_p1.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r05_p1.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r05_p1 saved OK")
