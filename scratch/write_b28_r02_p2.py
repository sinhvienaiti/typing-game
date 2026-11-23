import json

with open("scratch/b28_r02_raw_p2.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

edits = {
    "lex.en.200k.035610": {"vi": "khoáng vật barit; spar nặng"},
    "lex.en.200k.035613": {"vi": "chưa thanh toán; còn nợ đọng"},
    "lex.en.200k.035638": {"vi": "lối qua đường có nút bấm đèn"},
    "lex.en.200k.035653": {"vi": "xe hơi cũ; ô tô đã qua sử dụng"},
    "lex.en.200k.035666": {"vi": "thuốc kích thích; chất kích thích"},
    "lex.en.200k.035675": {"vi": "hạt quark đỉnh; quark trên"},
    "lex.en.200k.035679": {"vi": "quyền sở hữu không tách rời"},
    "lex.en.200k.035680": {"vi": "quyền lợi không phân chia"},
    "lex.en.200k.035688": {"vi": "chấn thương đốt sống cổ va đập"},
    "lex.en.200k.035696": {"ipa": "/ˈeɪliəsɪz/", "vi": "các bí danh; biệt hiệu"},
    "lex.en.200k.035697": {"ipa": "/ˈænəhaɪmz/", "vi": "các giống ớt Anaheim"},
    "lex.en.200k.035698": {"ipa": "/əˈnɔɪz/", "vi": "làm phiền; gây bực mình"},
    "lex.en.200k.035699": {"ipa": "/ˈæntɪbɑːdiz/", "vi": "các kháng thể miễn dịch"},
    "lex.en.200k.035700": {"ipa": "/əˈpɑːsəlz/", "vi": "các vị tông đồ; sứ đồ"},
    "lex.en.200k.035701": {"ipa": "/ˈbɛləruːsɪz/", "vi": "các vùng đất Belarus"}
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

with open("scratch/b28_r02_p2.json", "w", encoding="utf-8") as f:
    json.dump(reviewed, f, ensure_ascii=False, indent=2)

print("Batch 28 Round 2 Part 2 reviewed successfully:", len(reviewed))
