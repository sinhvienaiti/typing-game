import json

with open("scratch/b28_r02_raw_p3.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

edits = {
    "lex.en.200k.035702": {"ipa": "/brʌntʃt/", "vi": "đã ăn bữa sáng kết hợp trưa"},
    "lex.en.200k.035703": {"ipa": "/ˈbrʌntʃɪz/", "vi": "các bữa sáng kết hợp trưa"},
    "lex.en.200k.035704": {"ipa": "/ˈbrʌntʃɪŋ/", "vi": "ăn bữa sáng kết hợp trưa"},
    "lex.en.200k.035705": {"ipa": "/ˈbɜːrɡəndiz/", "vi": "các loại rượu vang Burgundy"},
    "lex.en.200k.035706": {"ipa": "/ˈtʃeɪndʒərz/", "vi": "người thay đổi; máy đổi tiền"},
    "lex.en.200k.035707": {"ipa": "/ˈtʃɛsnʌts/", "vi": "các hạt dẻ; câu chuyện cũ rích"},
    "lex.en.200k.035708": {"ipa": "/ˈkliːnʌps/", "vi": "các đợt dọn sạch; vụ kiếm đậm"},
    "lex.en.200k.035709": {"ipa": "/kənˈsaɪsər/", "vi": "ngắn gọn hơn; súc tích hơn"},
    "lex.en.200k.035710": {"ipa": "/kənˈsaɪsɪst/", "vi": "ngắn gọn nhất; súc tích nhất"},
    "lex.en.200k.035711": {"ipa": "/kənˈfaɪnmənts/", "vi": "sự giam giữ; thời kỳ ở cữ"},
    "lex.en.200k.035712": {"ipa": "/kənˈtrækʃənz/", "vi": "các cơn co thắt; dạng rút gọn"},
    "lex.en.200k.035713": {"ipa": "/kənˈvɜːrdʒənsɪz/", "vi": "các điểm hội tụ; sự giao nhau"},
    "lex.en.200k.035714": {"ipa": "/ˈkʌmɪŋzɪz/", "vi": "những người họ Cummings"},
    "lex.en.200k.035715": {"ipa": "/dɪˈdʌkʃənz/", "vi": "các khoản khấu trừ; phép diễn dịch"},
    "lex.en.200k.035716": {"ipa": "/daɪˈdʒɛstɪvz/", "vi": "bánh quy tiêu hóa; thuốc tiêu hóa"},
    "lex.en.200k.035717": {"ipa": "/dɪsˈkleɪmərz/", "vi": "các lời từ chối trách nhiệm"},
    "lex.en.200k.035718": {"ipa": "/ˌɛstɪˈmeɪʃənz/", "vi": "sự ước lượng; sự đánh giá"},
    "lex.en.200k.035719": {"ipa": "/ˌɛkskəˈveɪʃənz/", "vi": "các công trình khai quật khảo cổ"},
    "lex.en.200k.035720": {"ipa": "/ɪkˈstriːmɪsts/", "vi": "những kẻ cực đoan quá khích"},
    "lex.en.200k.035721": {"ipa": "/ˈfiːdɚz/", "vi": "máng ăn gia súc; tuyến nhánh"},
    "lex.en.200k.035722": {"ipa": "/ˈflæʃlaɪts/", "vi": "các chiếc đèn pin cầm tay"},
    "lex.en.200k.035723": {"ipa": "/ˈɡeɪoʊz/", "vi": "văn phòng kiểm toán chính phủ Mỹ"},
    "lex.en.200k.035724": {"ipa": "/ˈɡraʊndbreɪkɪŋz/", "vi": "các buổi lễ khởi công động thổ"},
    "lex.en.200k.035725": {"ipa": "/ˈɡruːpɪŋz/", "vi": "các nhóm phân loại; tập hợp"},
    "lex.en.200k.035726": {"ipa": "/ˈhɑːrdɪŋz/", "vi": "những người họ Harding"},
    "lex.en.200k.035727": {"ipa": "/ˈaɪdəz/", "vi": "Hiệp hội Phát triển Quốc tế (IDA)"},
    "lex.en.200k.035728": {"ipa": "/ˈɪləstreɪtərz/", "vi": "các họa sĩ vẽ minh họa"},
    "lex.en.200k.035729": {"ipa": "/ɪmˈbælənsɪz/", "vi": "tình trạng mất cân bằng"},
    "lex.en.200k.035730": {"ipa": "/ˈkæpəz/", "vi": "các chữ cái Hy Lạp kappa"},
    "lex.en.200k.035731": {"ipa": "/ˈlɪniɪdʒɪz/", "vi": "dòng dõi huyết thống; gia tộc"},
    "lex.en.200k.035732": {"ipa": "/ˈliːtərz/", "vi": "các lít; những lít"},
    "lex.en.200k.035733": {"ipa": "/ləˈreɪnz/", "vi": "các vùng đất Lorraine"},
    "lex.en.200k.035734": {"ipa": "/ˈlaɪənzɪz/", "vi": "những người họ Lyons"},
    "lex.en.200k.035735": {"ipa": "/ˈmɑːrliz/", "vi": "những người họ Marley"},
    "lex.en.200k.035736": {"ipa": "/ˈmoʊtərweɪz/", "vi": "các tuyến đường cao tốc"},
    "lex.en.200k.035737": {"ipa": "/əbˈsiːnər/", "vi": "tục tĩu hơn; đồi bại hơn"},
    "lex.en.200k.035738": {"ipa": "/əbˈsiːnɪst/", "vi": "tục tĩu nhất; đồi bại nhất"},
    "lex.en.200k.035739": {"ipa": "/ˈɑːktəpaɪ/", "vi": "những con bạch tuộc"},
    "lex.en.200k.035740": {"ipa": "/ˈɑːktəpʊsɪz/", "vi": "những con bạch tuộc"},
    "lex.en.200k.035741": {"ipa": "/pɪˈkæsoʊz/", "vi": "các tranh của danh họa Picasso"},
    "lex.en.200k.035742": {"ipa": "/ˈprɪviər/", "vi": "kín đáo hơn; được biết riêng hơn"},
    "lex.en.200k.035743": {"ipa": "/ˈprɪviz/", "vi": "nhà tiêu ngoài trời; nhà xí"},
    "lex.en.200k.035744": {"ipa": "/ˈprɪviɪst/", "vi": "kín đáo nhất; được biết nhiều nhất"},
    "lex.en.200k.035745": {"ipa": "/ˈsɜːrpənts/", "vi": "những con mãng xà; rắn độc"},
    "lex.en.200k.035746": {"ipa": "/ˈsɛsəmiz/", "vi": "các cây mè; hạt vừng"},
    "lex.en.200k.035747": {"ipa": "/ˈʃɛpərdz/", "vi": "những người họ Shepard"},
    "lex.en.200k.035748": {"ipa": "/ˈsɪsɪliz/", "vi": "vùng đảo Sicily"},
    "lex.en.200k.035749": {"ipa": "/ˈsaɪrənz/", "vi": "tiếng còi hú báo động; tiên cá"},
    "lex.en.200k.035750": {"ipa": "/ˈsleɪtɚz/", "vi": "thợ lợp ngói đá phiến; bọ ẩm"},
    "lex.en.200k.035751": {"ipa": "/ˈsliːpɚz/", "vi": "người đang ngủ; toa giường nằm"},
    "lex.en.200k.035752": {"ipa": "/ˈsnoʊiər/", "vi": "nhiều tuyết phủ hơn"},
    "lex.en.200k.035753": {"ipa": "/ˈsnoʊiɪst/", "vi": "nhiều tuyết phủ nhất"},
    "lex.en.200k.035754": {"ipa": "/stɪŋks/", "vi": "mùi hôi thối nồng nặc"},
    "lex.en.200k.035755": {"ipa": "/ˈstɔːrmiər/", "vi": "nhiều bão tố hơn; dữ dội hơn"},
    "lex.en.200k.035756": {"ipa": "/ˈstɔːrmiɪst/", "vi": "nhiều bão tố nhất"},
    "lex.en.200k.035757": {"ipa": "/ˌsʌbkəˈmɪtiz/", "vi": "các tiểu ban công tác"},
    "lex.en.200k.035758": {"ipa": "/ˈswɑːtɪd/", "vi": "đã đập mạnh; đã quật ngã"},
    "lex.en.200k.035759": {"ipa": "/swaɪnz/", "vi": "loài lợn; những kẻ bẩn thỉu"},
    "lex.en.200k.035760": {"ipa": "/ˈʌndərwʊdz/", "vi": "tầng cây bụi dưới tán rừng"},
    "lex.en.200k.035761": {"ipa": "/ˈʌndərwɜːrldz/", "vi": "các thế giới ngầm tội phạm"},
    "lex.en.200k.035762": {"ipa": "/ˌviːˈtiːz/", "vi": "tiểu bang Vermont (VT)"},
    "lex.en.200k.035763": {"ipa": "/weɪz/", "vi": "những người họ Wei"},
    "lex.en.200k.035764": {"ipa": "/ˈzaɪənz/", "vi": "núi Sion; đất thánh Zion"},
    "lex.en.200k.035772": {"vi": "bác sĩ Joseph Lister"},
    "lex.en.200k.035774": {"vi": "hạt quark đáy; quark đẹp"},
    "lex.en.200k.035780": {"vi": "hạt quark đáy; quark dưới"},
    "lex.en.200k.035781": {"vi": "cây lô hội Mũi Hảo Vọng"},
    "lex.en.200k.035788": {"vi": "đào bới lại chuyện cũ; nạo vét"},
    "lex.en.200k.035789": {"vi": "thèm thuồng nhỏ dãi; mê mẩn"},
    "lex.en.200k.035791": {"vi": "rút đi dần; suy thoái dần"},
    "lex.en.200k.035792": {"vi": "rút xuống thấp; lắng dịu bớt"},
    "lex.en.200k.035793": {"vi": "rút ra xa bờ; thoái trào"},
    "lex.en.200k.035794": {"vi": "thủy triều rút; tàn lụi dần"}
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

with open("scratch/b28_r02_p3.json", "w", encoding="utf-8") as f:
    json.dump(reviewed, f, ensure_ascii=False, indent=2)

print("Batch 28 Round 2 Part 3 reviewed successfully:", len(reviewed))
