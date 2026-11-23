import json

with open("scratch/b28_r02_raw_p1.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

edits = {
    "lex.en.200k.035504": {"ipa": "/ˈfæniz/", "vi": "vùng mông; túi đeo hông"},
    "lex.en.200k.035506": {"ipa": "/ˈfrɔɪdz/", "vi": "những người họ Freud"},
    "lex.en.200k.035507": {"ipa": "/ˈfriːdmənz/", "vi": "những người họ Friedman"},
    "lex.en.200k.035508": {"vi": "đã rót qua phễu; đã dồn lại"},
    "lex.en.200k.035509": {"ipa": "/ˈfʌnəlɪŋ/", "vi": "rót qua phễu; việc dồn lại"},
    "lex.en.200k.035510": {"ipa": "/ˈfʌnəlɪŋ/", "vi": "rót qua phễu; việc dồn lại"},
    "lex.en.200k.035512": {"ipa": "/ˈɡrʌmpiɪst/", "vi": "cáu kỉnh nhất; gắt gỏng nhất"},
    "lex.en.200k.035515": {"ipa": "/ɪˈmɜːrʒənz/", "vi": "sự ngâm mình; việc chìm đắm"},
    "lex.en.200k.035516": {"ipa": "/ˌkeɪˈbiːz/", "vi": "các kilobyte (KB)"},
    "lex.en.200k.035518": {"ipa": "/ˌɛlsiːˈdiːz/", "vi": "các màn hình tinh thể lỏng LCD"},
    "lex.en.200k.035520": {"ipa": "/ˈmeɪtərz/", "vi": "mẹ; các màng não"},
    "lex.en.200k.035522": {"ipa": "/ˈmɜːrsərz/", "vi": "những người buôn vải vóc"},
    "lex.en.200k.035528": {"ipa": "/ˌɑːrbiːˈaɪz/", "vi": "điểm đánh bóng ghi điểm (RBI)"},
    "lex.en.200k.035530": {"ipa": "/ˈriːθɪŋks/", "vi": "những sự suy nghĩ lại"},
    "lex.en.200k.035533": {"ipa": "/ˈsæzɪz/", "vi": "đặc nhiệm không quân SAS"},
    "lex.en.200k.035534": {"ipa": "/ˈʃɛrɪdənz/", "vi": "những người họ Sheridan"},
    "lex.en.200k.035535": {"ipa": "/ˈʃɜːrwʊdz/", "vi": "các khu rừng Sherwood"},
    "lex.en.200k.035537": {"ipa": "/ˈstʌfɪŋz/", "vi": "nhân nhồi thịt gà vịt; đệm nhồi"},
    "lex.en.200k.035538": {"ipa": "/ˈsʌðərləndz/", "vi": "những người họ Sutherland"},
    "lex.en.200k.035539": {"ipa": "/ˈtiːzərz/", "vi": "người hay trêu; đoạn giới thiệu"},
    "lex.en.200k.035543": {"ipa": "/ˈvɔːrtɛksɪz/", "vi": "các cơn lốc xoáy; xoáy nước"},
    "lex.en.200k.035545": {"ipa": "/wɑːndz/", "vi": "các cây đũa thần; gậy phép"},
    "lex.en.200k.035555": {"vi": "đem đổi chác; bán tháo đi"},
    "lex.en.200k.035575": {"vi": "Giáo hội Cơ Đốc Tự Trị"},
    "lex.en.200k.035579": {"vi": "hệ thống phân loại Dewey"},
    "lex.en.200k.035581": {"vi": "hạt quark dưới; quark xuống"},
    "lex.en.200k.035586": {"vi": "món trứng chiên phù dung"},
    "lex.en.200k.035589": {"vi": "cậu bé chạy việc vặt"},
    "lex.en.200k.035594": {"vi": "tuổi thai theo thụ tinh"},
    "lex.en.200k.035598": {"vi": "động tác đập chân bơi lội"},
    "lex.en.200k.035601": {"vi": "quá trình phân đoạn"}
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

with open("scratch/b28_r02_p1.json", "w", encoding="utf-8") as f:
    json.dump(reviewed, f, ensure_ascii=False, indent=2)

print("Batch 28 Round 2 Part 1 reviewed successfully:", len(reviewed))
