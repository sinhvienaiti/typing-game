import json

with open("scratch/b28_r01_raw_p5.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

edits = {
    "lex.en.200k.035409": {"vi": "tội cố ý gây thương tích nặng"},
    "lex.en.200k.035413": {"vi": "đi bộ; cuốc bộ"},
    "lex.en.200k.035415": {"vi": "con sam biển; cua móng ngựa"},
    "lex.en.200k.035436": {"vi": "anh hề sặc sỡ; gã hề triều đình"},
    "lex.en.200k.035445": {"vi": "đàn phong cầm phím piano"},
    "lex.en.200k.035450": {"vi": "lốp xe bơm hơi"},
    "lex.en.200k.035453": {"vi": "kali cacbonat; muối bồ tạt"},
    "lex.en.200k.035473": {"vi": "bong tróc ra; gạt bỏ đi"},
    "lex.en.200k.035476": {"vi": "pháo đuôi tàu chiến"},
    "lex.en.200k.035478": {"vi": "trốn đi lậu vé; lẻn lên tàu"},
    "lex.en.200k.035488": {"vi": "cây tulip vàng; cây dương vàng"},
    "lex.en.200k.035490": {"ipa": "/əˈkɪliːzɪz/", "vi": "những người hùng Achilles"},
    "lex.en.200k.035491": {"ipa": "/ˈæltoʊz/", "vi": "giọng nữ trầm; ca sĩ giọng trầm"},
    "lex.en.200k.035492": {"ipa": "/ˈæmbroʊzɪz/", "vi": "những người tên Ambrose"},
    "lex.en.200k.035493": {"ipa": "/əˈnɑːməliz/", "vi": "những sự bất thường; điểm dị thường"},
    "lex.en.200k.035494": {"ipa": "/ˈæpərtʃərz/", "vi": "các khẩu độ ống kính; khe hở"},
    "lex.en.200k.035495": {"ipa": "/əˈprɛntɪsʃɪps/", "vi": "các khóa học việc; sự học nghề"},
    "lex.en.200k.035496": {"ipa": "/brɛdθs/", "vi": "chiều rộng; bề rộng; phạm vi rộng"},
    "lex.en.200k.035497": {"ipa": "/ˈbʌstərz/", "vi": "người phá vỡ; kẻ khuất phục"},
    "lex.en.200k.035498": {"ipa": "/klɛnzd/", "vi": "đã tẩy uế; đã làm sạch tinh khiết"},
    "lex.en.200k.035499": {"ipa": "/ˈklɛnzɪz/", "vi": "tẩy uế; làm sạch sâu"},
    "lex.en.200k.035500": {"ipa": "/kəˈnɛktərz/", "vi": "các đầu cắm nối; giắc kết nối"},
    "lex.en.200k.035501": {"ipa": "/kənˈsɑːlɪdeɪts/", "vi": "củng cố; hợp nhất; sáp nhập"}
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

with open("scratch/b28_r01_p5.json", "w", encoding="utf-8") as f:
    json.dump(reviewed, f, ensure_ascii=False, indent=2)

print("Part 5 reviewed successfully:", len(reviewed))
