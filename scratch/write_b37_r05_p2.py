import json

records = [
    ("082103", "recurred", "verb", "/rɪˈkɜːrd/", "đã tái diễn, đã lặp lại, tái phát"),
    ("082104", "recurs", "verb", "/rɪˈkɜːrz/", "tái diễn, lặp lại, tái phát lại"),
    ("082105", "recursively", "adv", "/rɪˈkɜːrsɪvli/", "theo cách đệ quy (toán, tin học)"),
    ("082106", "recursiveness", "noun", "/rɪˈkɜːrsɪvnəs/", "tính đệ quy, tính chất tự lặp lại"),
    ("082107", "recurvate", "adj", "/rɪˈkɜːrveɪt/", "uốn cong ngược ra sau (thực vật)"),
    ("082108", "recurvirostra", "noun", "/rɪˌkɜːrvɪˈrɑːstrə/", "chi chim cà kheo mỏ cong hếch"),
    ("082109", "recurvirostral", "adj", "/rɪˌkɜːrvɪˈrɑːstrəl/", "có mỏ cong hếch ngược lên (chim)"),
    ("082110", "recurvirostridae", "noun", "/rɪˌkɜːrvɪˈrɑːstrɪˌdiː/", "họ Chim cà kheo mỏ cong"),
    ("082111", "recusation", "noun", "/ˌrɛkjʊˈzeɪʃən/", "yêu cầu thay đổi thẩm phán (luật)"),
    ("082112", "recut", "verb", "/ˌriːˈkʌt/", "cắt lại, mài cắt lại (đá quý)"),
    ("082113", "recycled", "verb", "/ˌriːˈsaɪkəld/", "đã tái chế; đã sử dụng lại"),
    ("082114", "recycles", "verb", "/ˌriːˈsaɪkəlz/", "tái chế (rác thải); tái sử dụng"),
    ("082115", "redacting", "verb", "/rɪˈdæktɪŋ/", "biên tập sửa chữa; bôi đen che đi"),
    ("082116", "redacts", "verb", "/rɪˈdækts/", "biên tập chỉnh sửa; bôi đen mật"),
    ("082117", "redan", "noun", "/rɪˈdæn/", "công sự hình chữ V nhô ra (quân sự)"),
    ("082118", "redargue", "verb", "/rɪˈdɑːrɡjuː/", "bác bỏ lý lẽ, phản bác lại (cổ)"),
    ("082119", "redbait", "verb", "/ˈrɛdˌbeɪt/", "vu khống gán mác cộng sản đàn áp"),
    ("082120", "redbaiting", "noun", "/ˈrɛdˌbeɪtɪŋ/", "hành vi chụp mũ cộng sản để bôi nhọ"),
    ("082121", "redbelly", "noun", "/ˈrɛdˌbɛli/", "rắn độc bụng đỏ Úc; cá rô phi đỏ"),
    ("082122", "redberry", "noun", "/ˈrɛdˌbɛri/", "cây quả mọng đỏ (họ Táo gai)"),
    ("082123", "redbill", "noun", "/ˈrɛdˌbɪl/", "chim mòng biển mỏ đỏ; chim cà kheo"),
    ("082124", "redbrush", "noun", "/ˈrɛdˌbrʌʃ/", "cây bụi cành đỏ (Bắc Mỹ)"),
    ("082125", "redbug", "noun", "/ˈrɛdˌbʌɡ/", "bọ xít đỏ hại bông; con mò đỏ"),
    ("082126", "redcurrant", "noun", "/ˌrɛdˈkɜːrənt/", "quả lý chua đỏ (chùm mọng nhỏ)"),
    ("082127", "redd", "verb", "/rɛd/", "dọn dẹp gọn gàng; đẻ trứng (cá hồi)"),
    ("082128", "reddening", "verb", "/ˈrɛdənɪŋ/", "đỏ bừng mặt, ửng đỏ, nhuộm đỏ"),
    ("082129", "reddens", "verb", "/ˈrɛdənz/", "đỏ ửng lên, đỏ bừng mặt; nhuộm đỏ"),
    ("082130", "reddishness", "noun", "/ˈrɛdɪʃnəs/", "sắc hơi đỏ, vẻ ửng đỏ nhạt"),
    ("082131", "reddition", "noun", "/rɛˈdɪʃən/", "sự hoàn trả; lời giải thích (luật)"),
    ("082132", "reddle", "noun", "/ˈrɛdəl/", "đất son đỏ đánh dấu cừu"),
    ("082133", "reddy", "adj", "/ˈrɛdi/", "hơi đỏ, có ánh sắc đỏ nhạt"),
    ("082134", "redeems", "verb", "/rɪˈdiːmz/", "chuộc lại; bù đắp lỗi lầm; đổi lấy"),
    ("082135", "redefined", "verb", "/ˌriːdɪˈfaɪnd/", "đã định nghĩa lại, xác định lại"),
    ("082136", "redefines", "verb", "/ˌriːdɪˈfaɪnz/", "định nghĩa lại, thay đổi hoàn toàn"),
    ("082137", "redefining", "verb", "/ˌriːdɪˈfaɪnɪŋ/", "định nghĩa lại, làm thay đổi hẳn"),
    ("082138", "redeliver", "verb", "/ˌriːdɪˈlɪvər/", "giao hàng lại; hoàn trả; đọc lại"),
    ("082139", "redelivered", "verb", "/ˌriːdɪˈlɪvərd/", "đã giao lại; đã hoàn trả; đọc lại"),
    ("082140", "redelivering", "verb", "/ˌriːdɪˈlɪvərɪŋ/", "giao lại lần nữa; đọc lại bài"),
    ("082141", "redelivers", "verb", "/ˌriːdɪˈlɪvərz/", "giao lại lần nữa; hoàn trả lại"),
    ("082142", "redelivery", "noun", "/ˌriːdɪˈlɪvəri/", "sự giao hàng lại; sự hoàn trả lại"),
    ("082143", "redemand", "verb", "/ˌriːdɪˈmænd/", "đòi lại lần nữa, yêu cầu lại"),
    ("082144", "redemptional", "adj", "/rɪˈdɛmpʃənəl/", "thuộc sự cứu chuộc, chuộc lỗi"),
    ("082145", "redemptorist", "noun", "/rɪˈdɛmptərɪst/", "tu sĩ Dòng Chúa Cứu Thế"),
    ("082146", "redemptory", "adj", "/rɪˈdɛmptəri/", "để cứu chuộc, mang tính chuộc lại"),
    ("082147", "redeposition", "noun", "/ˌriːdɛpəˈzɪʃən/", "sự tái lắng đọng, tái bồi tụ"),
    ("082148", "redescend", "verb", "/ˌriːdɪˈsɛnd/", "đi xuống lại, giáng xuống lần nữa"),
    ("082149", "redescription", "noun", "/ˌriːdɪˈskrɪpʃən/", "sự mô tả lại (loài sinh vật mới)"),
    ("082150", "redesigning", "noun", "/ˌriːdɪˈzaɪnɪŋ/", "việc thiết kế lại, chỉnh sửa mẫu"),
    ("082151", "redetermine", "verb", "/ˌriːdɪˈtɜːrmɪn/", "xác định lại, định đoạt lại"),
    ("082152", "redeveloped", "verb", "/ˌriːdɪˈvɛləpt/", "đã quy hoạch tái phát triển lại"),
    ("082153", "redeveloping", "verb", "/ˌriːdɪˈvɛləpɪŋ/", "tái phát triển, cải tạo lại khu đất"),
    ("082154", "redevelops", "verb", "/ˌriːdɪˈvɛləps/", "tái phát triển, quy hoạch xây lại"),
    ("082155", "redheader", "noun", "/ˈrɛdˌhɛdər/", "người có mái tóc màu đỏ hung"),
    ("082156", "redial", "verb", "/ˌriːˈdaɪəl/", "gọi lại số vừa quay (điện thoại)"),
    ("082157", "redialed", "verb", "/ˌriːˈdaɪəld/", "đã bấm gọi lại số điện thoại cũ"),
    ("082158", "redialing", "verb", "/ˌriːˈdaɪəlɪŋ/", "bấm quay số gọi lại lần nữa"),
    ("082159", "redials", "verb", "/ˌriːˈdaɪəlz/", "bấm quay số gọi lại lần nữa"),
    ("082160", "redid", "verb", "/ˌriːˈdɪd/", "đã làm lại, sửa sang trang trí lại"),
    ("082161", "redingote", "noun", "/ˈrɛdɪŋˌɡoʊt/", "áo khoác dài chít eo dáng xòe"),
    ("082162", "redintegrate", "verb", "/rɪˈdɪntəˌɡreɪt/", "khôi phục toàn vẹn như ban đầu"),
    ("082163", "redintegration", "noun", "/rɪˌdɪntəˈɡreɪʃən/", "sự tái hợp hoàn chỉnh; hồi ức liên"),
    ("082164", "redirected", "verb", "/ˌriːdaɪˈrɛktɪd/", "đã chuyển hướng, đã điều hướng lại"),
    ("082165", "redirecting", "verb", "/ˌriːdaɪˈrɛktɪŋ/", "chuyển hướng, điều hướng sang lối"),
    ("082166", "redirects", "verb", "/ˌriːdaɪˈrɛkts/", "chuyển hướng, điều hướng sang mới"),
    ("082167", "rediscount", "verb", "/ˌriːdɪˈskaʊnt/", "tái chiết khấu thương phiếu (tài)"),
    ("082168", "rediscovered", "verb", "/ˌriːdɪˈskʌvərd/", "đã tái phát hiện, khám phá lại"),
    ("082169", "rediscovering", "verb", "/ˌriːdɪˈskʌvərɪŋ/", "khám phá lại, tìm thấy trở lại"),
    ("082170", "rediscovers", "verb", "/ˌriːdɪˈskʌvərz/", "tái khám phá, phát hiện lại"),
    ("082171", "redispose", "verb", "/ˌriːdɪˈspoʊz/", "bố trí sắp xếp lại từ đầu"),
    ("082172", "redisposition", "noun", "/ˌriːdɪspəˈzɪʃən/", "sự tái bố trí, điều động sắp xếp"),
    ("082173", "redistil", "verb", "/ˌriːdɪˈstɪl/", "chưng cất lại lần nữa (hóa học)"),
    ("082174", "redlining", "noun", "/ˈrɛdˌlaɪnɪŋ/", "phân biệt tín dụng theo khu dân cư"),
    ("082175", "redly", "adv", "/ˈrɛdli/", "với sắc đỏ thắm, ửng đỏ rực"),
    ("082176", "redmaids", "noun", "/ˈrɛdˌmeɪdz/", "cây hoa hồng mao California"),
    ("082177", "redman", "noun", "/ˈrɛdˌmæn/", "người bản địa châu Mỹ (từ cũ)"),
    ("082178", "rednecked", "adj", "/ˈrɛdˌnɛkt/", "có cổ màu đỏ (chim); quê mùa bảo"),
    ("082179", "rednecks", "noun", "/ˈrɛdˌnɛks/", "dân lao động da trắng nông thôn Mỹ"),
    ("082180", "redolence", "noun", "/ˈrɛdələns/", "hương thơm ngào ngạt, mùi gợi nhớ"),
    ("082181", "redone", "adj", "/ˌriːˈdʌn/", "đã được làm lại, sửa trang trí lại"),
    ("082182", "redounded", "verb", "/rɪˈdaʊndɪd/", "đã dội lại, đã góp phần mang lại"),
    ("082183", "redounding", "verb", "/rɪˈdaʊndɪŋ/", "dội lại, góp phần mang lại danh"),
    ("082184", "redounds", "verb", "/rɪˈdaʊndz/", "dội ngược lại, mang lại vinh dự"),
    ("082185", "redressed", "verb", "/rɪˈdrɛst/", "đã khắc phục, đền bù thiệt hại"),
    ("082186", "redresses", "verb", "/rɪˈdrɛsɪz/", "sửa chữa sai lầm, đền bù oan sai"),
    ("082187", "redressing", "verb", "/rɪˈdrɛsɪŋ/", "khắc phục bất công, đền bù lại"),
    ("082188", "redroot", "noun", "/ˈrɛdˌruːt/", "cây rễ đỏ Bắc Mỹ (Ceanothus)"),
    ("082189", "redskins", "noun", "/ˈrɛdˌskɪnz/", "người bản địa châu Mỹ (cách gọi cũ)"),
    ("082190", "reducers", "noun", "/rɪˈduːsərz/", "chất khử; khớp nối thu ống (cơ khí)"),
    ("082191", "reduces", "verb", "/rɪˈduːsɪz/", "làm giảm bớt, hạ xuống; thu gọn"),
    ("082192", "reductibility", "noun", "/rɪˌdʌktəˈbɪləti/", "tính khử được; tính rút gọn được"),
    ("082193", "reductional", "adj", "/rɪˈdʌkʃənəl/", "thuộc sự giảm phân, rút gọn"),
    ("082194", "reductionistic", "adj", "/rɪˌdʌkʃəˈnɪstɪk/", "thuộc chủ nghĩa giản lược quy giảm"),
    ("082195", "reductions", "noun", "/rɪˈdʌkʃənz/", "sự cắt giảm, mức giảm; phản ứng khử"),
    ("082196", "reductivism", "noun", "/rɪˈdʌktɪˌvɪzəm/", "chủ nghĩa quy giản (triết học)"),
    ("082197", "reductor", "noun", "/rɪˈdʌktər/", "chất khử; ống lọc khử (hóa học)"),
    ("082198", "reduibility", "noun", "/rɪˌduːsəˈbɪləti/", "tính khả quy, tính rút gọn được"),
    ("082199", "redundance", "noun", "/rɪˈdʌndəns/", "sự dư thừa, tình trạng thừa thãi"),
    ("082200", "redundancies", "noun", "/rɪˈdʌndənsiz/", "sự dư thừa; việc sa thải thừa nhân"),
    ("082201", "redundantly", "adv", "/rɪˈdʌndəntli/", "một cách dư thừa, thừa thãi"),
    ("082202", "reduplicated", "verb", "/rɪˈduːpləˌkeɪtɪd/", "đã lặp lại, đã láy âm; đã nhân đôi"),
]

raw = json.load(open("scratch/b37_r05_raw_p2.json"))
by_id = {f"lex.en.200k.{r[0]}": r for r in records}
out = []
for orig in raw:
    sid, hw, pos, ipa, vi = by_id[orig["id"]]
    assert orig["hw"] == hw, f"{orig['id']}: {orig['hw']} vs {hw}"
    assert 0 < len(vi) <= 35, f"{sid} {hw} len={len(vi)}: {vi}"
    assert "/" not in vi, f"{sid} {hw} slash in vi"
    assert ipa.count("/") == 2 and not ipa.startswith("/ ") and not ipa.endswith(" /"), f"{sid} {hw} bad ipa"
    orig["pos"] = pos
    orig["ipa"] = ipa
    orig["vi"] = vi
    orig["status"] = "reviewed"
    out.append(orig)

assert len(out) == 100
with open("scratch/b37_r05_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r05_p2 saved OK")
