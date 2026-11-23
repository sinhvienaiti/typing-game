import json

with open("scratch/b28_r03_raw_p1.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

edits = {
    "lex.en.200k.036002": {"vi": "đảo Borneo phần Indonesia"},
    "lex.en.200k.036018": {"vi": "thập tự chữ thập Malta"},
    "lex.en.200k.036021": {"vi": "tôm tít; tôm tích; bề bề"},
    "lex.en.200k.036023": {"vi": "dao chặt thịt; dao phay bản to"},
    "lex.en.200k.036027": {"vi": "tình tiết giảm nhẹ hình phạt"},
    "lex.en.200k.036038": {"vi": "viên thuốc tránh thai uống"},
    "lex.en.200k.036082": {"vi": "câu nói líu lưỡi; câu xoắn lưỡi"},
    "lex.en.200k.036087": {"vi": "cây dẻ gai cành rủ"},
    "lex.en.200k.036089": {"vi": "củ mài hoang; củ khoai mài"},
    "lex.en.200k.036096": {"ipa": "/ˈeɪdʒɪŋz/", "vi": "quá trình lão hóa; sự ủ chín"},
    "lex.en.200k.036097": {"ipa": "/ˈbɑːrɪŋz/", "vi": "sự loại trừ; các thanh chắn rào"},
    "lex.en.200k.036098": {"ipa": "/ˈbɜːrɡləriz/", "vi": "các vụ đột nhập trộm cắp"},
    "lex.en.200k.036099": {"ipa": "/ˌkæfəˈtɪriəz/", "vi": "các quán ăn tự phục vụ"},
    "lex.en.200k.036100": {"ipa": "/kɔːˈkeɪʒənz/", "vi": "người da trắng chủng Cáp-ca"},
    "lex.en.200k.036101": {"ipa": "/ˈtʃɪliənz/", "vi": "người dân nước Chile"}
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

with open("scratch/b28_r03_p1.json", "w", encoding="utf-8") as f:
    json.dump(reviewed, f, ensure_ascii=False, indent=2)

print("Batch 28 Round 3 Part 1 reviewed successfully:", len(reviewed))
