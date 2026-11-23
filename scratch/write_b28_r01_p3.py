import json

with open("scratch/b28_r01_raw_p3.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

edits = {
    "lex.en.200k.035213": {"vi": "bản hòa âm bí ẩn; câu đố canon"},
    "lex.en.200k.035215": {"vi": "sống phụ đáy tàu"},
    "lex.en.200k.035216": {"vi": "tam cá nguyệt đầu tiên; 3 tháng đầu"},
    "lex.en.200k.035225": {"vi": "cơn cắn rứt lương tâm; sự ân hận"},
    "lex.en.200k.035227": {"vi": "quả hồ đào; hạt cây hồ đào"},
    "lex.en.200k.035228": {"vi": "trại tập trung của dân lang thang"},
    "lex.en.200k.035229": {"vi": "cá sòng; cá sòng đại dương"},
    "lex.en.200k.035239": {"vi": "sự hát nhép; khớp khẩu hình"},
    "lex.en.200k.035248": {"vi": "ý định phạm tội; tâm thế phạm tội"},
    "lex.en.200k.035250": {"vi": "áo dòng tu sĩ; trang phục tu viện"},
    "lex.en.200k.035251": {"vi": "cây xạ hương rừng bò"},
    "lex.en.200k.035252": {"vi": "các xoang cạnh mũi; xoang mũi"},
    "lex.en.200k.035254": {"vi": "cỏ muhly thân mảnh"},
    "lex.en.200k.035256": {"vi": "trò chơi bài old sledge"},
    "lex.en.200k.035258": {"vi": "đêm tối như mực; bóng tối đen kịt"},
    "lex.en.200k.035266": {"vi": "cá măng bạc; cá đù bạc"},
    "lex.en.200k.035268": {"vi": "kẻ tán gái; kẻ hám sắc lăng nhăng"},
    "lex.en.200k.035269": {"vi": "cây hoa hài; cây cuống giày"},
    "lex.en.200k.035272": {"vi": "mì Ý sốt thịt viên"},
    "lex.en.200k.035274": {"vi": "bọ cánh cứng kẹp kìm; kẹp kìm"},
    "lex.en.200k.035289": {"ipa": "/ˈeɪbəlz/", "vi": "những người tên Abel"},
    "lex.en.200k.035290": {"ipa": "/ˈeɪdʒæksɪz/", "vi": "những người tên Ajax"},
    "lex.en.200k.035291": {"ipa": "/ˈeɪməsɪz/", "vi": "những người tên Amos"},
    "lex.en.200k.035292": {"ipa": "/ˌæzərbaɪˈdʒɑːnz/", "vi": "các khu vực Azerbaijan"},
    "lex.en.200k.035293": {"ipa": "/ˈbæntərd/", "vi": "đã nói đùa; đã trêu chọc"},
    "lex.en.200k.035294": {"ipa": "/ˈbæntərz/", "vi": "những lời nói đùa; lời trêu chọc"},
    "lex.en.200k.035295": {"ipa": "/ˈbɪdɚz/", "vi": "những người tham gia đấu thầu"},
    "lex.en.200k.035296": {"ipa": "/ˈblækbərnz/", "vi": "những người họ Blackburn"},
    "lex.en.200k.035297": {"ipa": "/ˈblɑːkbʌstərz/", "vi": "các tác phẩm bom tấn; phim ăn khách"},
    "lex.en.200k.035298": {"ipa": "/ˈboʊlɚz/", "vi": "vận động viên bowling; mũ quả dưa"},
    "lex.en.200k.035299": {"ipa": "/ˈkæmioʊz/", "vi": "vai diễn khách mời; ngọc chạm nổi"},
    "lex.en.200k.035300": {"ipa": "/ˈkærəmɛlz/", "vi": "kẹo caramen; đường thắng kẹo"},
    "lex.en.200k.035301": {"ipa": "/ˈkroʊməsˌoʊmz/", "vi": "các nhiễm sắc thể"}
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

with open("scratch/b28_r01_p3.json", "w", encoding="utf-8") as f:
    json.dump(reviewed, f, ensure_ascii=False, indent=2)

print("Part 3 reviewed successfully:", len(reviewed))
