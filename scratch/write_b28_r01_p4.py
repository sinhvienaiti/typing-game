import json

with open("scratch/b28_r01_raw_p4.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

edits = {
    "lex.en.200k.035302": {"ipa": "/kəˈmɛnsmənts/", "vi": "các lễ tốt nghiệp; lễ trao bằng"},
    "lex.en.200k.035307": {"ipa": "/ˈdaɪnərz/", "vi": "thực khách; các quán ăn bình dân"},
    "lex.en.200k.035308": {"ipa": "/ˈdɪznilændz/", "vi": "các khu giải trí Disneyland"},
    "lex.en.200k.035309": {"ipa": "/ˌdɪspəˈzɪʃənz/", "vi": "tính khí; sự bố trí sắp xếp"},
    "lex.en.200k.035310": {"ipa": "/ˈɛkstəsiz/", "vi": "trạng thái ngây ngất; mê ly"},
    "lex.en.200k.035311": {"ipa": "/ˌeɪtˈtiːnθs/", "vi": "các phần mười tám (1/18)"},
    "lex.en.200k.035312": {"ipa": "/ɪˈlɛvənθs/", "vi": "các phần mười một (1/11)"},
    "lex.en.200k.035313": {"ipa": "/ˈɛnvɔɪz/", "vi": "các đặc sứ; phái viên ngoại giao"},
    "lex.en.200k.035314": {"ipa": "/ɛˈstoʊniəz/", "vi": "các vùng đất Estonia"},
    "lex.en.200k.035315": {"ipa": "/ˌfæsɪˈneɪʃənz/", "vi": "sự mê hoặc quyến rũ; say mê"},
    "lex.en.200k.035316": {"ipa": "/fɜːrz/", "vi": "cây linh sam; rừng linh sam"},
    "lex.en.200k.035317": {"ipa": "/ˈfɔːrənərz/", "vi": "những người nước ngoài"},
    "lex.en.200k.035318": {"ipa": "/ˈɡoʊliz/", "vi": "các thủ môn"},
    "lex.en.200k.035319": {"ipa": "/ˈɡreɪdiənts/", "vi": "độ dốc; biến thiên gradien"},
    "lex.en.200k.035320": {"ipa": "/ˈɡreɪviz/", "vi": "các loại nước sốt thịt"},
    "lex.en.200k.035321": {"ipa": "/ˈheɪliz/", "vi": "những người họ Haley"},
    "lex.en.200k.035322": {"ipa": "/ˈhɛrɪŋz/", "vi": "các con cá trích"},
    "lex.en.200k.035323": {"ipa": "/ɪnˈdʒʌŋkʃənz/", "vi": "các lệnh cấm của tòa án"},
    "lex.en.200k.035324": {"ipa": "/ˌdʒɛrɪˈmaɪəz/", "vi": "những người bi quan hay than phiền"},
    "lex.en.200k.035325": {"ipa": "/dʒuːdz/", "vi": "những người tên Jude"},
    "lex.en.200k.035326": {"ipa": "/ˈkiːnoʊtɪd/", "vi": "đã đọc bài diễn văn khai mạc"},
    "lex.en.200k.035327": {"ipa": "/ˈkiːnoʊts/", "vi": "các bài diễn văn khai mạc"},
    "lex.en.200k.035328": {"ipa": "/ˈkiːnoʊtɪŋ/", "vi": "đọc bài diễn văn khai mạc"},
    "lex.en.200k.035329": {"ipa": "/ˈkiːɛvz/", "vi": "các món gà cuộn Kiev"},
    "lex.en.200k.035330": {"ipa": "/ˈkrɪʃnəz/", "vi": "những tín đồ đạo Krishna"},
    "lex.en.200k.035331": {"ipa": "/ˈlɑːməz/", "vi": "các vị lạt-ma Tây Tạng"},
    "lex.en.200k.035332": {"ipa": "/pləˈsiːboʊz/", "vi": "các viên giả dược"},
    "lex.en.200k.035333": {"ipa": "/pləˈsiːboʊz/", "vi": "các viên giả dược"},
    "lex.en.200k.035334": {"ipa": "/ˌpiːɛsˈeɪz/", "vi": "thông điệp cộng đồng; chỉ số PSA"},
    "lex.en.200k.035335": {"ipa": "/ˌrɛtrəˈspɛktɪvz/", "vi": "các cuộc triển lãm hồi tưởng"},
    "lex.en.200k.035336": {"ipa": "/ˈrɑːbɪnzɪz/", "vi": "những người họ Robbins"},
    "lex.en.200k.035337": {"ipa": "/ˈʃiːəz/", "vi": "các tín đồ Hồi giáo dòng Shia"},
    "lex.en.200k.035338": {"ipa": "/ˈspæroʊz/", "vi": "các con chim sẻ"},
    "lex.en.200k.035340": {"ipa": "/ˈskwɑːtɪst/", "vi": "lùn tịt nhất; bè bè nhất"},
    "lex.en.200k.035341": {"ipa": "/ˈstraʊsɪz/", "vi": "những người họ Strauss"},
    "lex.en.200k.035342": {"ipa": "/səˈblaɪmər/", "vi": "hùng vĩ hơn; cao cả hơn"},
    "lex.en.200k.035343": {"ipa": "/səˈblaɪmɪst/", "vi": "hùng vĩ nhất; cao cả nhất"},
    "lex.en.200k.035344": {"ipa": "/ˈsʊniz/", "vi": "các tín đồ Hồi giáo dòng Sunni"},
    "lex.en.200k.035345": {"ipa": "/təˈkiːləz/", "vi": "các loại rượu tequila"},
    "lex.en.200k.035346": {"ipa": "/θʌɡz/", "vi": "những tên côn đồ hung hãn"},
    "lex.en.200k.035347": {"ipa": "/tɪts/", "vi": "loài chim bạc má; bầu ngực"},
    "lex.en.200k.035348": {"ipa": "/ˈtʌlsəz/", "vi": "các thành phố Tulsa"},
    "lex.en.200k.035349": {"ipa": "/ˈjuːɛfoʊz/", "vi": "các vật thể bay không xác định"},
    "lex.en.200k.035351": {"vi": "người sành uống bia ale"},
    "lex.en.200k.035354": {"vi": "cây thùa Mỹ; dứa sợi Mỹ"},
    "lex.en.200k.035377": {"vi": "món gà hầm nồi đất"},
    "lex.en.200k.035384": {"vi": "gấu trúc lớn; đại miêu hùng"},
    "lex.en.200k.035385": {"vi": "mèo lông dài Maine Coon"},
    "lex.en.200k.035389": {"vi": "ván ngồi ngang trên thuyền"},
    "lex.en.200k.035390": {"vi": "hoa chuông chén đĩa"},
    "lex.en.200k.035397": {"vi": "món trứng chiên phù dung"}
}

reviewed = []
for item in raw:
    item_id = item["id"]
    if item_id in edits:
        for k, v in edits[item_id].items():
            item[k] = v
    item["status"] = "reviewed"
    assert len(item["vi"]) <= 35, f"Length > 35 at {item_id}: {item['vi']}"
    if item["pos"] != "phrase":
        assert item["ipa"].startswith("/") and item["ipa"].endswith("/") and item["ipa"].count("/") == 2, f"Bad IPA at {item['hw']}: {item['ipa']}"
    reviewed.append(item)

with open("scratch/b28_r01_p4.json", "w", encoding="utf-8") as f:
    json.dump(reviewed, f, ensure_ascii=False, indent=2)

print("Part 4 reviewed successfully:", len(reviewed))
