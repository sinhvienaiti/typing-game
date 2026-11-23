import json

rows = [
    ("075203", "penalisation", "noun", "/ˌpiːnəlaɪˈzeɪʃən/", "sự xử phạt; hình phạt"),
    ("075204", "penalised", "verb", "/ˈpiːnəlaɪzd/", "đã xử phạt, trừng phạt"),
    ("075205", "penalises", "verb", "/ˈpiːnəlaɪzɪz/", "xử phạt, trừng phạt"),
    ("075206", "penalising", "verb", "/ˈpiːnəlaɪzɪŋ/", "xử phạt, trừng phạt"),
    ("075207", "penalist", "noun", "/ˈpiːnəlɪst/", "chuyên gia hình phạt học; hình luật"),
    ("075208", "penanced", "verb", "/ˈpɛnənst/", "đã áp đặt hình phạt xá tội"),
    ("075209", "penances", "verb", "/ˈpɛnənsɪz/", "áp đặt hình phạt xá tội"),
    ("075210", "penancing", "verb", "/ˈpɛnənsɪŋ/", "áp đặt hình phạt xá tội"),
    ("075211", "penates", "noun", "/pɪˈneɪtiːz/", "gia thần bảo hộ (La Mã cổ đại)"),
    ("075212", "pence", "noun", "/pɛns/", "đồng xu pên-ni (số nhiều của penny)"),
    ("075213", "penciler", "noun", "/ˈpɛnsələr/", "người ghi sổ cá cược; người vẽ chì"),
    ("075214", "penciling", "noun", "/ˈpɛnsəlɪŋ/", "nét vẽ bút chì; nét tô kẻ"),
    ("075215", "penciller", "noun", "/ˈpɛnsələr/", "người ghi sổ cá cược; người vẽ chì"),
    ("075216", "pencilling", "verb", "/ˈpɛnsəlɪŋ/", "vẽ bằng bút chì; ghi sổ lại"),
    ("075217", "pencils", "verb", "/ˈpɛnsəlz/", "vẽ bằng bút chì; ghi chú"),
    ("075218", "pencraft", "noun", "/ˈpɛnkræft/", "nghệ thuật viết lách; bút pháp"),
    ("075219", "pend", "verb", "/pɛnd/", "treo lơ lửng; chờ quyết định"),
    ("075220", "pended", "verb", "/ˈpɛndɪd/", "đã chờ xử lý; đã treo lơ lửng"),
    ("075221", "pendency", "noun", "/ˈpɛndənsi/", "tình trạng đang chờ giải quyết"),
    ("075222", "pendentive", "noun", "/pɛnˈdɛntɪv/", "vòm tam giác chống mái vòm"),
    ("075223", "pendently", "adv", "/ˈpɛndəntli/", "treo lơ lửng; nhô nghiêng ra"),
    ("075224", "pendicle", "noun", "/ˈpɛndɪkəl/", "mảnh đất thuê nhỏ (Scotland)"),
    ("075225", "pends", "verb", "/pɛndz/", "chờ giải quyết; treo lơ lửng"),
    ("075226", "pendulant", "adj", "/ˈpɛndjələnt/", "đu đưa, đung đưa, lủng lẳng"),
    ("075227", "pendular", "adj", "/ˈpɛndjələr/", "thuộc con lắc; dao động qua lại"),
    ("075228", "pendulate", "verb", "/ˈpɛndjəleɪt/", "đu đưa lúc lắc; dao động"),
    ("075229", "pendulously", "adv", "/ˈpɛndjələsli/", "một cách rủ xuống, đu đưa"),
    ("075230", "pendulousness", "noun", "/ˈpɛndjələsnəs/", "tính rủ xuống, đu đưa"),
    ("075231", "pendulums", "noun", "/ˈpɛndjələmz/", "con lắc (đồng hồ, vật lý)"),
    ("075232", "peneal", "adj", "/ˈpaɪniəl/", "hình quả thông (biến thể pineal)"),
    ("075233", "peneapple", "noun", "/ˈpaɪnˌæpəl/", "quả dứa; lựu đạn (biến thể cũ)"),
    ("075234", "peneidae", "noun", "/pɪˈniːɪdiː/", "họ Tôm he (Penaeidae)"),
    ("075235", "peneplane", "noun", "/ˈpiːnəpleɪn/", "bán bình nguyên; đồng bằng san bằng"),
    ("075236", "penes", "noun", "/ˈpiːniːz/", "dương vật (giải phẫu)"),
    ("075237", "penetrability", "noun", "/ˌpɛnɪtrəˈbɪlɪti/", "tính xuyên thấu; tính thẩm thấu"),
    ("075238", "penetrably", "adv", "/ˈpɛnɪtrəbli/", "có thể xuyên thấu qua được"),
    ("075239", "penetralia", "noun", "/ˌpɛnɪˈtreɪliə/", "chốn thâm cung; nơi bí mật nhất"),
    ("075240", "penetralium", "noun", "/ˌpɛnɪˈtreɪliəm/", "chốn thâm cung; nơi bí mật nhất"),
    ("075241", "penetrant", "adj", "/ˈpɛnɪtrənt/", "có khả năng xuyên thấu, thấm qua"),
    ("075242", "penetrated", "verb", "/ˈpɛnɪˌtreɪtɪd/", "đã xuyên qua; đã thâm nhập"),
    ("075243", "penetrates", "verb", "/ˈpɛnɪˌtreɪts/", "xuyên qua; thâm nhập"),
    ("075244", "penetratively", "adv", "/ˈpɛnɪtreɪtɪvli/", "một cách sâu sắc, thấu đáo"),
    ("075245", "penetrometer", "noun", "/ˌpɛnɪˈtrɒmɪtər/", "thẩm kế; dụng cụ đo độ đâm xuyên"),
    ("075246", "pengou", "noun", "/ˈpɛŋɡoʊ/", "đồng pengo (tiền cũ Hungary)"),
    ("075247", "penguins", "noun", "/ˈpɛŋɡwɪnz/", "chim cánh cụt"),
    ("075248", "penholder", "noun", "/ˈpɛnˌhoʊldər/", "quản bút; ống cắm bút"),
    ("075249", "peniaphobia", "noun", "/ˌpiːniəˈfoʊbiə/", "chứng sợ cảnh nghèo túng (tâm lý)"),
    ("075250", "penicillase", "noun", "/ˈpɛnɪsɪleɪs/", "enzym phân hủy penicillin"),
    ("075251", "penicillate", "adj", "/ˌpɛnɪˈsɪlɪt/", "có chùm lông dạng bút vẽ"),
    ("075252", "penicilliform", "adj", "/ˌpɛnɪˈsɪlɪfɔːrm/", "có hình chùm dạng bút lông"),
    ("075253", "penicillinase", "noun", "/ˌpɛnɪˈsɪlɪneɪs/", "enzym penicillinase"),
    ("075254", "peninsulate", "verb", "/pɪˈnɪnsjəleɪt/", "biến thành bán đảo"),
    ("075255", "penitentially", "adv", "/ˌpɛnɪˈtɛnʃəli/", "một cách ăn năn, sám hối"),
    ("075256", "penitentiaries", "noun", "/ˌpɛnɪˈtɛnʃəriz/", "nhà tù liên bang; trại cải huấn"),
    ("075257", "penmen", "noun", "/ˈpɛnmən/", "người viết chữ đẹp; nhà văn"),
    ("075258", "penna", "noun", "/ˈpɛnə/", "lông vũ bao ngoài của chim"),
    ("075259", "pennae", "noun", "/ˈpɛniː/", "lông vũ bao ngoài của chim"),
    ("075260", "pennate", "adj", "/ˈpɛneɪt/", "có lông cánh; dạng lông chim"),
    ("075261", "pennatula", "noun", "/pəˈnætʃələ/", "chi san hô bút biển (Pennatula)"),
    ("075262", "pennatulidae", "noun", "/ˌpɛnəˈtjuːlɪdiː/", "họ San hô bút biển"),
    ("075263", "penned", "verb", "/pɛnd/", "đã viết, sáng tác; đã nhốt chuồng"),
    ("075264", "penner", "noun", "/ˈpɛnər/", "tác giả, người viết; hộp đựng bút"),
    ("075265", "pennies", "noun", "/ˈpɛniz/", "đồng xu pên-ni (Anh, Mỹ)"),
    ("075266", "penniferous", "adj", "/pɛˈnɪfərəs/", "có phủ lông vũ"),
    ("075267", "penniform", "adj", "/ˈpɛnɪfɔːrm/", "có hình dạng lông chim"),
    ("075268", "pennigerous", "adj", "/pɛˈnɪdʒərəs/", "có mang lông vũ"),
    ("075269", "pennilessly", "adv", "/ˈpɛnɪləsli/", "trong cảnh không một xu dính túi"),
    ("075270", "pennilessness", "noun", "/ˈpɛnɪləsnəs/", "cảnh túng quẫn không một xu"),
    ("075271", "pennoncel", "noun", "/ˈpɛnənsəl/", "cờ đuôi nheo nhỏ gắn giáo (cổ)"),
    ("075272", "pennoncelle", "noun", "/ˈpɛnənsəl/", "cờ đuôi nheo nhỏ gắn giáo (cổ)"),
    ("075273", "pennorth", "noun", "/ˈpɛnərθ/", "lượng hàng đáng giá một xu"),
    ("075274", "pennycress", "noun", "/ˈpɛniˌkrɛs/", "cây cải đồng (Thlaspi arvense)"),
    ("075275", "pennyings", "noun", "/ˈpɛniɪŋz/", "trò ném đồng xu; đồng bạc cổ Anh"),
    ("075276", "pennywhistle", "noun", "/ˈpɛniˌwɪsəl/", "sáo kim loại 6 lỗ (tin whistle)"),
    ("075277", "pennywise", "adj", "/ˈpɛniˌwaɪz/", "khôn vặt tiết kiệm xu lẻ"),
    ("075278", "pennywort", "noun", "/ˈpɛniˌwɜːrt/", "cây rau má thủy sinh (Hydrocotyle)"),
    ("075279", "pennyworts", "noun", "/ˈpɛniˌwɜːrts/", "cây rau má thủy sinh (Hydrocotyle)"),
    ("075280", "penoche", "noun", "/pəˈnoʊtʃi/", "kẹo đường nâu bơ sữa penuche"),
    ("075281", "penological", "adj", "/ˌpiːnəˈlɒdʒɪkəl/", "thuộc hình phạt học"),
    ("075282", "penologically", "adv", "/ˌpiːnəˈlɒdʒɪkli/", "về mặt hình phạt học"),
    ("075283", "penoncel", "noun", "/ˈpɛnənsəl/", "cờ đuôi nheo nhỏ gắn giáo (cổ)"),
    ("075284", "penpusher", "noun", "/ˈpɛnˌpʊʃər/", "nhân viên bàn giấy tẻ nhạt"),
    ("075285", "pens", "noun", "/pɛnz/", "cây bút viết; chuồng nhốt thú"),
    ("075286", "pensile", "adj", "/ˈpɛnsaɪl/", "treo lơ lửng; làm tổ treo (chim)"),
    ("075287", "pensioned", "verb", "/ˈpɛnʃənd/", "đã cấp lương hưu; cho nghỉ hưu"),
    ("075288", "pensioning", "verb", "/ˈpɛnʃənɪŋ/", "cấp lương hưu; cho nghỉ hưu"),
    ("075289", "pensions", "verb", "/ˈpɛnʃənz/", "cấp lương hưu; trả trợ cấp"),
    ("075290", "pensiveness", "noun", "/ˈpɛnsɪvnəs/", "sự trầm tư, nỗi suy tư sâu lắng"),
    ("075291", "penstocks", "noun", "/ˈpɛnstɒks/", "ống dẫn áp lực thủy điện; cửa cống"),
    ("075292", "penswan", "noun", "/ˈpɛnˌswɒn/", "thiên nga mái"),
    ("075293", "pentacapsular", "adj", "/ˌpɛntəˈkæpsjələr/", "có năm nang, năm ô (thực vật)"),
    ("075294", "pentacarpellary", "adj", "/ˌpɛntəˈkɑːrpəˌlɛri/", "có năm lá noãn (thực vật)"),
    ("075295", "pentachord", "noun", "/ˈpɛntəkɔːrd/", "đàn năm dây; chuỗi năm âm"),
    ("075296", "pentacoccous", "adj", "/ˌpɛntəˈkɒkəs/", "có năm mảnh vỏ hạt (thực vật)"),
    ("075297", "pentadactyl", "adj", "/ˌpɛntəˈdæktɪl/", "có năm ngón chi (động vật)"),
    ("075298", "pentadactyle", "noun", "/ˌpɛntəˈdæktɪl/", "động vật có năm ngón chi"),
    ("075299", "pentadactylism", "noun", "/ˌpɛntəˈdæktɪlɪzəm/", "đặc điểm có năm ngón chi"),
    ("075300", "pentadecagon", "noun", "/ˌpɛntəˈdɛkəɡɒn/", "hình thập ngũ giác (15 cạnh)"),
    ("075301", "pentagonally", "adv", "/pɛnˈtæɡənəli/", "theo hình ngũ giác"),
    ("075302", "pentagraf", "noun", "/ˈpɛntəɡræf/", "máy phóng họa đồ (pantograph)"),
]

with open("scratch/b36_r01_raw_p3.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

assert len(raw) == len(rows) == 100
out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, rows):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} vs {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} vs {hw}"
    assert len(vi) <= 35, f"vi too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.count("/") == 2 and not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"bad ipa: {hw} -> {ipa}"
    r["pos"] = pos
    r["ipa"] = ipa
    r["vi"] = vi
    r["status"] = "reviewed"
    out.append(r)

with open("scratch/b36_r01_p3.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r01_p3 saved OK")
