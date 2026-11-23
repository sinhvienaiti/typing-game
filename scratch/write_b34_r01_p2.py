import json

items = [
  {"id": "lex.en.200k.065103", "hw": "buboes", "pos": "noun", "ipa": "/ˈbjuːboʊz/", "vi": "hạch bạch huyết sưng to gây đau"},
  {"id": "lex.en.200k.065104", "hw": "bucurestis", "pos": "noun", "ipa": "/ˌbuːkʊˈrɛʃtiz/", "vi": "thủ đô Bucharest của Romania"},
  {"id": "lex.en.200k.065105", "hw": "bujumburas", "pos": "noun", "ipa": "/ˌbuːdʒʊmˈbʊrəz/", "vi": "thành phố Bujumbura của Burundi"},
  {"id": "lex.en.200k.065106", "hw": "burins", "pos": "noun", "ipa": "/ˈbjʊrɪnz/", "vi": "mũi đục chạm khắc kim loại đồng gỗ"},
  {"id": "lex.en.200k.065107", "hw": "caecums", "pos": "noun", "ipa": "/ˈsiːkəmz/", "vi": "manh tràng ruột tịt đầu ruột già"},
  {"id": "lex.en.200k.065108", "hw": "caffs", "pos": "noun", "ipa": "/kæfs/", "vi": "quán cà phê bình dân (lóng Anh)"},
  {"id": "lex.en.200k.065109", "hw": "candlemases", "pos": "noun", "ipa": "/ˈkændəlˌmæsɪz/", "vi": "lễ Dâng Chúa Giêsu trong Đền Thờ"},
  {"id": "lex.en.200k.065110", "hw": "carpels", "pos": "noun", "ipa": "/ˈkɑːrpəlz/", "vi": "lá noãn cấu tạo nhụy cái của hoa"},
  {"id": "lex.en.200k.065111", "hw": "catsups", "pos": "noun", "ipa": "/ˈkætʃəps/", "vi": "nước sốt cà chua sánh ketchup"},
  {"id": "lex.en.200k.065112", "hw": "chromates", "pos": "noun", "ipa": "/ˈkroʊmeɪts/", "vi": "muối hóa học cromat màu vàng cam"},
  {"id": "lex.en.200k.065113", "hw": "cinchonas", "pos": "noun", "ipa": "/sɪŋˈkoʊnəz/", "vi": "cây canh-ki-na lấy vỏ trị sốt rét"},
  {"id": "lex.en.200k.065114", "hw": "commiserations", "pos": "noun", "ipa": "/kəˌmɪzəˈreɪʃənz/", "vi": "lòng thương cảm lời chia buồn sâu"},
  {"id": "lex.en.200k.065115", "hw": "cumulonimbi", "pos": "noun", "ipa": "/ˌkjuːmjəloʊˈnɪmbaɪ/", "vi": "đám mây vũ tích dông tố cao vút"},
  {"id": "lex.en.200k.065116", "hw": "demerols", "pos": "noun", "ipa": "/ˈdɛməˌrɔːlz/", "vi": "thuốc giảm đau mạnh meperidine"},
  {"id": "lex.en.200k.065117", "hw": "dumdums", "pos": "noun", "ipa": "/ˈdʌmdʌmz/", "vi": "đạn đầu mềm nở rộng gây sát thương"},
  {"id": "lex.en.200k.065118", "hw": "dyscalculias", "pos": "noun", "ipa": "/ˌdɪskælˈkjuːliəz/", "vi": "chứng rối loạn khó học làm toán"},
  {"id": "lex.en.200k.065119", "hw": "enlils", "pos": "noun", "ipa": "/ˈɛnlɪlz/", "vi": "thần gió bão tối cao Sumer Enlil"},
  {"id": "lex.en.200k.065120", "hw": "eosins", "pos": "noun", "ipa": "/ˈiːəsɪnz/", "vi": "thuốc nhuộm mô tế bào màu hồng"},
  {"id": "lex.en.200k.065121", "hw": "epitaxies", "pos": "noun", "ipa": "/ˈɛpɪˌtæksiz/", "vi": "kỹ thuật cấy lớp tinh thể đơn bán"},
  {"id": "lex.en.200k.065122", "hw": "equerries", "pos": "noun", "ipa": "/ˈɛkwəriz/", "vi": "sĩ quan hầu cận hoàng gia Anh"},
  {"id": "lex.en.200k.065123", "hw": "exarches", "pos": "noun", "ipa": "/ˈɛksɑːrks/", "vi": "tổng trấn Byzantine; tổng giám mục"},
  {"id": "lex.en.200k.065124", "hw": "factotums", "pos": "noun", "ipa": "/fækˈtoʊtəmz/", "vi": "người làm đủ mọi công việc tạp vụ"},
  {"id": "lex.en.200k.065125", "hw": "fascicles", "pos": "noun", "ipa": "/ˈfæsɪkəlz/", "vi": "bó sợi cơ thần kinh; tập sách lẻ"},
  {"id": "lex.en.200k.065126", "hw": "fechners", "pos": "noun", "ipa": "/ˈfɛxnərz/", "vi": "nhà tâm vật lý học Đức Fechner"},
  {"id": "lex.en.200k.065127", "hw": "fetishized", "pos": "verb", "ipa": "/ˈfɛtɪˌʃaɪzd/", "vi": "đã sùng bái quá mức; đã thần tượng"},
  {"id": "lex.en.200k.065128", "hw": "fetishizes", "pos": "verb", "ipa": "/ˈfɛtɪˌʃaɪzɪz/", "vi": "sùng bái tôn thờ quá mức vật gì"},
  {"id": "lex.en.200k.065129", "hw": "fetishizing", "pos": "verb", "ipa": "/ˈfɛtɪˌʃaɪzɪŋ/", "vi": "đang sùng bái tôn thờ thái quá"},
  {"id": "lex.en.200k.065130", "hw": "flashbulbs", "pos": "noun", "ipa": "/ˈflæʃbʌlbz/", "vi": "bóng đèn nháy sáng chụp ảnh cổ"},
  {"id": "lex.en.200k.065131", "hw": "flypasts", "pos": "noun", "ipa": "/ˈflaɪpæsts/", "vi": "màn bay trình diễn máy bay nghi lễ"},
  {"id": "lex.en.200k.065132", "hw": "freethinkers", "pos": "noun", "ipa": "/ˈfriːˌθɪŋkərz/", "vi": "người theo tư tưởng tự do lý trí"},
  {"id": "lex.en.200k.065133", "hw": "gaeas", "pos": "noun", "ipa": "/ˈdʒiːəz/", "vi": "nữ thần Đất mẹ Hy Lạp cổ đại Gaia"},
  {"id": "lex.en.200k.065134", "hw": "gallstones", "pos": "noun", "ipa": "/ˈɡɔːlstoʊnz/", "vi": "viên sỏi kết tụ trong túi mật"},
  {"id": "lex.en.200k.065135", "hw": "globins", "pos": "noun", "ipa": "/ˈɡloʊbɪnz/", "vi": "protein hình cầu globin trong máu"},
  {"id": "lex.en.200k.065136", "hw": "goatskins", "pos": "noun", "ipa": "/ˈɡoʊtskɪnz/", "vi": "tấm da dê thuộc làm túi giày găng"},
  {"id": "lex.en.200k.065137", "hw": "guanosines", "pos": "noun", "ipa": "/ˈɡwɑːnəsiːnz/", "vi": "nucleoside guanosine cấu tạo ARN"},
  {"id": "lex.en.200k.065138", "hw": "haggadahs", "pos": "noun", "ipa": "/həˈɡɑːdəz/", "vi": "sách kinh lễ Vượt Qua Do Thái"},
  {"id": "lex.en.200k.065139", "hw": "handholds", "pos": "noun", "ipa": "/ˈhændhoʊldz/", "vi": "chỗ bám tay khi leo trèo vách đá"},
  {"id": "lex.en.200k.065140", "hw": "hundredweights", "pos": "noun", "ipa": "/ˈhʌndrədweɪts/", "vi": "đơn vị khối lượng tạ (Anh, Mỹ)"},
  {"id": "lex.en.200k.065141", "hw": "hyperkalemias", "pos": "noun", "ipa": "/ˌhaɪpərkəˈliːmiəz/", "vi": "chứng tăng nồng độ kali trong máu"},
  {"id": "lex.en.200k.065142", "hw": "icosahedra", "pos": "noun", "ipa": "/ˌaɪkɑːsəˈhiːdrə/", "vi": "khối đa diện đều hai mươi mặt"},
  {"id": "lex.en.200k.065143", "hw": "icosahedrons", "pos": "noun", "ipa": "/ˌaɪkɑːsəˈhiːdrənz/", "vi": "khối hình học hai mươi mặt đều"},
  {"id": "lex.en.200k.065144", "hw": "iguazus", "pos": "noun", "ipa": "/ˌiːɡwɑːˈsuːz/", "vi": "thác nước hùng vĩ Iguazu Nam Mỹ"},
  {"id": "lex.en.200k.065145", "hw": "internes", "pos": "noun", "ipa": "/ˈɪntɜːrnz/", "vi": "bác sĩ thực tập nội trú bệnh viện"},
  {"id": "lex.en.200k.065146", "hw": "jevonses", "pos": "noun", "ipa": "/ˈdʒɛvənzɪz/", "vi": "nhà kinh tế học Anh Stanley Jevons"},
  {"id": "lex.en.200k.065147", "hw": "keynesianisms", "pos": "noun", "ipa": "/ˈkeɪnziəˌnɪzəmz/", "vi": "học thuyết kinh tế vĩ mô Keynes"},
  {"id": "lex.en.200k.065148", "hw": "kibs", "pos": "noun", "ipa": "/ˈkɪbəˌbaɪts/", "vi": "đơn vị dữ liệu kibibyte (1024 B)"},
  {"id": "lex.en.200k.065149", "hw": "kumquats", "pos": "noun", "ipa": "/ˈkʌmkwɑːts/", "vi": "cây và quả quất tắc nhỏ vỏ ngọt"},
  {"id": "lex.en.200k.065150", "hw": "kwajaleins", "pos": "noun", "ipa": "/ˈkwɑːdʒələnz/", "vi": "đảo san hô vòng Kwajalein"},
  {"id": "lex.en.200k.065151", "hw": "laminitides", "pos": "noun", "ipa": "/ˌlæməˈnaɪtɪdiːz/", "vi": "bệnh viêm mô móng guốc ở ngựa bò"},
  {"id": "lex.en.200k.065152", "hw": "laputas", "pos": "noun", "ipa": "/ləˈpjuːtəz/", "vi": "hòn đảo bay hư cấu Laputa (Swift)"},
  {"id": "lex.en.200k.065153", "hw": "larboards", "pos": "noun", "ipa": "/ˈlɑːrbərdz/", "vi": "mạn bên trái của tàu thủy (từ cổ)"},
  {"id": "lex.en.200k.065154", "hw": "latecomers", "pos": "noun", "ipa": "/ˈleɪtˌkʌmərz/", "vi": "người đến muộn; người tham gia trễ"},
  {"id": "lex.en.200k.065155", "hw": "lumbermen", "pos": "noun", "ipa": "/ˈlʌmbərmən/", "vi": "thợ đốn cây rừng gỗ; chủ buôn gỗ"},
  {"id": "lex.en.200k.065156", "hw": "lysozymes", "pos": "noun", "ipa": "/ˈlaɪsəˌzaɪmz/", "vi": "enzym diệt khuẩn trong nước mắt"},
  {"id": "lex.en.200k.065157", "hw": "mainmasts", "pos": "noun", "ipa": "/ˈmeɪnmæsts/", "vi": "cột buồm chính cao nhất trên tàu"},
  {"id": "lex.en.200k.065158", "hw": "menarches", "pos": "noun", "ipa": "/mɛˈnɑːrkiz/", "vi": "kỳ hành kinh đầu tiên tuổi dậy thì"},
  {"id": "lex.en.200k.065159", "hw": "mezzotints", "pos": "noun", "ipa": "/ˈmɛtsoʊˌtɪnts/", "vi": "tranh khắc bản đồng sắc độ mịn"},
  {"id": "lex.en.200k.065160", "hw": "mishnas", "pos": "noun", "ipa": "/ˈmɪʃnəz/", "vi": "bộ luật truyền khẩu Do Thái Mishnah"},
  {"id": "lex.en.200k.065161", "hw": "mishnayoth", "pos": "noun", "ipa": "/ˌmɪʃnəˈjoʊθ/", "vi": "tập kinh luật truyền khẩu Mishnah"},
  {"id": "lex.en.200k.065162", "hw": "moghuls", "pos": "noun", "ipa": "/ˈmoʊɡəlz/", "vi": "đế chế và hoàng đế Mogul Ấn Độ"},
  {"id": "lex.en.200k.065163", "hw": "monazites", "pos": "noun", "ipa": "/ˈmɑːnəˌzaɪts/", "vi": "khoáng vật photphat giàu đất hiếm"},
  {"id": "lex.en.200k.065164", "hw": "moviemakings", "pos": "noun", "ipa": "/ˈmuːviˌmeɪkɪŋz/", "vi": "nghề sản xuất làm phim điện ảnh"},
  {"id": "lex.en.200k.065165", "hw": "mussets", "pos": "noun", "ipa": "/mjuːˈseɪz/", "vi": "nhà thơ lãng mạn Pháp de Musset"},
  {"id": "lex.en.200k.065166", "hw": "nannings", "pos": "noun", "ipa": "/ˈnænɪŋz/", "vi": "thành phố Nam Ninh tỉnh Quảng Tây"},
  {"id": "lex.en.200k.065167", "hw": "ovides", "pos": "noun", "ipa": "/ˈoʊvɪdz/", "vi": "chi động vật loài cừu núi Ovis"},
  {"id": "lex.en.200k.065168", "hw": "partitas", "pos": "noun", "ipa": "/pɑːrˈtiːtəz/", "vi": "tổ khúc biến tấu nhạc cổ điển Bach"},
  {"id": "lex.en.200k.065169", "hw": "pekingeses", "pos": "noun", "ipa": "/ˌpiːkɪˈniːzɪz/", "vi": "giống chó cảnh lông xù Bắc Kinh"},
  {"id": "lex.en.200k.065170", "hw": "philias", "pos": "noun", "ipa": "/ˈfɪliəz/", "vi": "lòng yêu thích say mê mãnh liệt"},
  {"id": "lex.en.200k.065171", "hw": "pintails", "pos": "noun", "ipa": "/ˈpɪnteɪlz/", "vi": "loài vịt trời đuôi nhọn dài di cư"},
  {"id": "lex.en.200k.065172", "hw": "polacks", "pos": "noun", "ipa": "/ˈpoʊlæks/", "vi": "từ miệt thị người gốc Ba Lan (lóng)"},
  {"id": "lex.en.200k.065173", "hw": "poolers", "pos": "noun", "ipa": "/ˈpuːlərz/", "vi": "người góp quỹ chung; đi chung xe"},
  {"id": "lex.en.200k.065174", "hw": "ptoses", "pos": "noun", "ipa": "/ˈtoʊsiːz/", "vi": "chứng sụp mí mắt hoặc sa nội tạng"},
  {"id": "lex.en.200k.065175", "hw": "ptosises", "pos": "noun", "ipa": "/ˈtoʊsɪsɪz/", "vi": "chứng sụp mí mắt trên (nhãn khoa)"},
  {"id": "lex.en.200k.065176", "hw": "pukas", "pos": "noun", "ipa": "/ˈpuːkəz/", "vi": "cây lá rộng puka vùng New Zealand"},
  {"id": "lex.en.200k.065177", "hw": "qats", "pos": "noun", "ipa": "/kɑːts/", "vi": "lá cây khát gây kích thích nhai"},
  {"id": "lex.en.200k.065178", "hw": "rachmaninovs", "pos": "noun", "ipa": "/rɑːxˈmɑːnɪˌnɔːfs/", "vi": "nhà soạn nhạc Nga Rachmaninoff"},
  {"id": "lex.en.200k.065179", "hw": "ragouts", "pos": "noun", "ipa": "/ræˈɡuːz/", "vi": "món thịt hầm rau củ kiểu Pháp ragu"},
  {"id": "lex.en.200k.065180", "hw": "remoras", "pos": "noun", "ipa": "/ˈrɛmərəz/", "vi": "cá ép có đĩa hút bám vào cá mập"},
  {"id": "lex.en.200k.065181", "hw": "salvadorians", "pos": "noun", "ipa": "/ˌsælvəˈdɔːriənz/", "vi": "người dân quốc gia El Salvador"},
  {"id": "lex.en.200k.065182", "hw": "schliemanns", "pos": "noun", "ipa": "/ˈʃliːmənz/", "vi": "nhà khảo cổ khai quật thành Troy"},
  {"id": "lex.en.200k.065183", "hw": "schwas", "pos": "noun", "ipa": "/ʃwɑːz/", "vi": "nguyên âm giữa ngắn không nhấn /ə/"},
  {"id": "lex.en.200k.065184", "hw": "scorias", "pos": "noun", "ipa": "/ˈskɔːriəz/", "vi": "xỉ núi lửa rỗ khí; xỉ luyện kim"},
  {"id": "lex.en.200k.065185", "hw": "secants", "pos": "noun", "ipa": "/ˈsiːkənts/", "vi": "đường cát tuyến cắt; hàm số sec"},
  {"id": "lex.en.200k.065186", "hw": "senecios", "pos": "noun", "ipa": "/sɪˈniːʃioʊz/", "vi": "chi cây hoa cúc bạc đầu Senecio"},
  {"id": "lex.en.200k.065187", "hw": "shysters", "pos": "noun", "ipa": "/ˈʃaɪstərz/", "vi": "kẻ làm ăn gian dối; luật sư xảo"},
  {"id": "lex.en.200k.065188", "hw": "slaveholders", "pos": "noun", "ipa": "/ˈsleɪvˌhoʊldərz/", "vi": "chủ sở hữu giam giữ nô lệ thời xưa"},
  {"id": "lex.en.200k.065189", "hw": "smetanas", "pos": "noun", "ipa": "/ˈsmɛtənəz/", "vi": "nhà soạn nhạc Séc Bedřich Smetana"},
  {"id": "lex.en.200k.065190", "hw": "snakeheads", "pos": "noun", "ipa": "/ˈsneɪkhɛdz/", "vi": "cá lóc cá quả nước ngọt ăn thịt"},
  {"id": "lex.en.200k.065191", "hw": "snellens", "pos": "noun", "ipa": "/ˈsnɛlənz/", "vi": "bác sĩ lập bảng đo thị lực Snellen"},
  {"id": "lex.en.200k.065192", "hw": "sodomites", "pos": "noun", "ipa": "/ˈsɑːdəmaɪts/", "vi": "cư dân thành Sodom cổ (Kinh Thánh)"},
  {"id": "lex.en.200k.065193", "hw": "solvations", "pos": "noun", "ipa": "/sɑːlˈveɪʃənz/", "vi": "quá trình dung môi hóa phân tử chất"},
  {"id": "lex.en.200k.065194", "hw": "spritzers", "pos": "noun", "ipa": "/ˈsprɪtsərz/", "vi": "đồ uống rượu vang pha nước có ga"},
  {"id": "lex.en.200k.065195", "hw": "stylizations", "pos": "noun", "ipa": "/ˌstaɪləˈzeɪʃənz/", "vi": "sự cách điệu hóa nét nghệ thuật"},
  {"id": "lex.en.200k.065196", "hw": "teetotalers", "pos": "noun", "ipa": "/ˈtiːˌtoʊtələrz/", "vi": "người kiêng tuyệt đối rượu bia cồn"},
  {"id": "lex.en.200k.065197", "hw": "tempters", "pos": "noun", "ipa": "/ˈtɛmptərz/", "vi": "kẻ cám dỗ dụ dỗ người làm điều sai"},
  {"id": "lex.en.200k.065198", "hw": "tenges", "pos": "noun", "ipa": "/tɛŋˈɡeɪz/", "vi": "đơn vị tiền tệ tenge Kazakhstan"},
  {"id": "lex.en.200k.065199", "hw": "tunnies", "pos": "noun", "ipa": "/ˈtʌniz/", "vi": "cá ngừ đại dương lớn thịt đỏ (Anh)"},
  {"id": "lex.en.200k.065200", "hw": "tureens", "pos": "noun", "ipa": "/təˈriːnz/", "vi": "bát tô sứ sâu lòng có nắp đậy súp"},
  {"id": "lex.en.200k.065201", "hw": "turtledoves", "pos": "noun", "ipa": "/ˈtɜːrtəlˌdʌvz/", "vi": "chim cu gáy hiền hòa biểu tượng yêu"},
  {"id": "lex.en.200k.065202", "hw": "uranyls", "pos": "noun", "ipa": "/ˈjʊrənəlz/", "vi": "nhóm ion hóa học chứa urani dioxit"}
]

with open('scratch/b34_r01_raw_p2.json') as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"Mismatch id at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"Mismatch hw at {i}: {item['hw']} vs {r['hw']}"
    assert len(item['vi']) <= 35, f"vi length > 35 at {i} ({item['hw']}): {len(item['vi'])}"
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {item['pos']}"
    assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Invalid ipa at {i}: {item['ipa']}"
    assert not item['ipa'][1:-1].startswith(' ') and not item['ipa'][1:-1].endswith(' '), f"Space in ipa at {i}: {item['ipa']}"
    r['pos'] = item['pos']
    r['ipa'] = item['ipa']
    r['vi'] = item['vi']
    r['status'] = 'reviewed'

with open('scratch/b34_r01_p2.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r01_p2.json OK")
