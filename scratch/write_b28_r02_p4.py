import json

with open("scratch/b28_r02_raw_p4.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

edits = {
    "lex.en.200k.035806": {"vi": "bước lấn sân sang; đột phá vào"},
    "lex.en.200k.035823": {"vi": "ngả lưng ngủ; đi ngủ tạm"},
    "lex.en.200k.035825": {"vi": "vạch giao bóng (bóng bầu dục)"},
    "lex.en.200k.035828": {"vi": "tiến bộ; đạt được bước tiến"},
    "lex.en.200k.035841": {"vi": "thùng thuốc súng; mầm mống họa"},
    "lex.en.200k.035846": {"vi": "vạch giao bóng (bóng bầu dục)"},
    "lex.en.200k.035851": {"vi": "làm bẹp rúm; đập thủng vào"},
    "lex.en.200k.035852": {"vi": "ngăn chặn; đẩy lùi hiểm họa"},
    "lex.en.200k.035856": {"vi": "tính tự cao tự đại; kiêu ngạo"},
    "lex.en.200k.035871": {"ipa": "/ˈæmplɪfaɪərz/", "vi": "các bộ khuếch đại âm thanh"},
    "lex.en.200k.035872": {"ipa": "/ˈɔːdəbəlz/", "vi": "lệnh đổi chiến thuật miệng"},
    "lex.en.200k.035873": {"ipa": "/ˈeɪvənz/", "vi": "các dòng sông Avon"},
    "lex.en.200k.035874": {"ipa": "/biːpt/", "vi": "đã phát tiếng bíp; bấm còi"},
    "lex.en.200k.035875": {"ipa": "/ˈbiːpɪŋ/", "vi": "đang kêu bíp; tiếng còi bíp"},
    "lex.en.200k.035876": {"ipa": "/biːps/", "vi": "những tiếng kêu bíp"},
    "lex.en.200k.035877": {"ipa": "/ˈbɪskɪts/", "vi": "bánh quy; bánh nướng xốp"},
    "lex.en.200k.035878": {"ipa": "/bræts/", "vi": "những đứa trẻ hư; ranh con"},
    "lex.en.200k.035879": {"ipa": "/ˈtʃɛklɪsts/", "vi": "các danh sách kiểm tra việc"},
    "lex.en.200k.035880": {"ipa": "/ˈtʃɛrəkiːz/", "vi": "người da đỏ bộ tộc Cherokee"},
    "lex.en.200k.035881": {"ipa": "/ˌsɪndəˈrɛləz/", "vi": "những nàng Lọ Lem"},
    "lex.en.200k.035882": {"ipa": "/kənˌfɛdəˈreɪʃənz/", "vi": "các liên minh; liên bang"},
    "lex.en.200k.035884": {"ipa": "/ˌkɔːrəˈneɪʃənz/", "vi": "các lễ đăng quang vương quyền"},
    "lex.en.200k.035885": {"ipa": "/ˈkaʊnsəlɪŋz/", "vi": "các buổi tham vấn tâm lý"},
    "lex.en.200k.035886": {"ipa": "/kraɪˈmiːəz/", "vi": "vùng bán đảo Krym"},
    "lex.en.200k.035887": {"ipa": "/ˈkʌmbərləndz/", "vi": "các vùng đất Cumberland"},
    "lex.en.200k.035888": {"ipa": "/ˈkʌnɪŋər/", "vi": "ranh mãnh hơn; xảo quyệt hơn"},
    "lex.en.200k.035889": {"ipa": "/ˈkʌnɪŋɪst/", "vi": "ranh mãnh nhất; xảo quyệt nhất"},
    "lex.en.200k.035890": {"ipa": "/daɪˈæspərəz/", "vi": "cộng đồng người di cư hải ngoại"},
    "lex.en.200k.035891": {"ipa": "/ˌɛntərˈteɪnərz/", "vi": "các nghệ sĩ biểu diễn giải trí"},
    "lex.en.200k.035892": {"ipa": "/ˈfærəlz/", "vi": "những người họ Farrell"},
    "lex.en.200k.035893": {"ipa": "/ˈfaɪnəlɪsts/", "vi": "các đấu thủ vào chung kết"},
    "lex.en.200k.035894": {"ipa": "/ˈɡædʒɪts/", "vi": "các thiết bị công nghệ tiện ích"},
    "lex.en.200k.035895": {"ipa": "/ˈɡlɪtʃɪz/", "vi": "các lỗi kỹ thuật; sự cố nhỏ"},
    "lex.en.200k.035896": {"ipa": "/ˈɡriːsiər/", "vi": "nhiều dầu mỡ hơn; nhờn hơn"},
    "lex.en.200k.035897": {"ipa": "/ˈɡriːsiɪst/", "vi": "nhiều dầu mỡ nhất; nhờn nhất"},
    "lex.en.200k.035898": {"ipa": "/ˈhæmbɜːrɡərz/", "vi": "các chiếc bánh kẹp hăm-bơ-gơ"},
    "lex.en.200k.035899": {"ipa": "/ɪmˈpɜːrfɪkts/", "vi": "thì quá khứ chưa hoàn thành"},
    "lex.en.200k.035900": {"ipa": "/ˈɪnlɛts/", "vi": "các lạch nước; eo biển nhỏ"},
    "lex.en.200k.035901": {"ipa": "/ˈkiːstoʊnz/", "vi": "đá đỉnh vòm; yếu tố then chốt"}
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

with open("scratch/b28_r02_p4.json", "w", encoding="utf-8") as f:
    json.dump(reviewed, f, ensure_ascii=False, indent=2)

print("Batch 28 Round 2 Part 4 reviewed successfully:", len(reviewed))
