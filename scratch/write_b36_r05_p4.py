import json

rows = [
    ("077303", "plexor", "noun", "/ˈplɛksər/", "búa gõ khám phản xạ (y học)"),
    ("077304", "pliabilities", "noun", "/ˌplaɪəˈbɪlɪtiz/", "tính mềm dẻo, dễ uốn nắn"),
    ("077305", "pliableness", "noun", "/ˈplaɪəbəlnəs/", "tính mềm dẻo, dễ uốn, dễ bảo"),
    ("077306", "pliably", "adv", "/ˈplaɪəbli/", "một cách mềm dẻo, linh hoạt"),
    ("077307", "pliantly", "adv", "/ˈplaɪəntli/", "một cách mềm dẻo, dễ uốn nắn"),
    ("077308", "pliantness", "noun", "/ˈplaɪəntnəs/", "tính mềm dẻo, dễ uốn, dễ bảo"),
    ("077309", "plicae", "noun", "/ˈplaɪsiː/", "nếp gấp (giải phẫu); tóc bết rối"),
    ("077310", "plical", "adj", "/ˈplaɪkəl/", "thuộc nếp gấp, uốn nếp"),
    ("077311", "plicated", "adj", "/ˈplaɪkeɪtɪd/", "có nếp gấp, xếp nếp"),
    ("077312", "plicately", "adv", "/ˈplaɪkətli/", "theo dạng xếp nếp"),
    ("077313", "plicateness", "noun", "/ˈplaɪkətnəs/", "tính xếp nếp, có nếp gấp"),
    ("077314", "plicatoperipatus", "noun", "/plaɪˌkeɪtoʊpəˈrɪpətəs/", "chi giun nhung Plicatoperipatus"),
    ("077315", "plied", "verb", "/plaɪd/", "đã chăm chú làm; chạy tuyến; chập"),
    ("077316", "plies", "verb", "/plaɪz/", "chăm chú làm; chạy tuyến; chập sợi"),
    ("077317", "plighted", "verb", "/ˈplaɪtɪd/", "đã thề hứa, đã đính ước (cổ)"),
    ("077318", "plighter", "noun", "/ˈplaɪtər/", "người thề hứa, người cam kết"),
    ("077319", "plighting", "verb", "/ˈplaɪtɪŋ/", "thề hứa, đính ước (từ cổ)"),
    ("077320", "plights", "verb", "/plaɪts/", "thề hứa, đính ước (từ cổ)"),
    ("077321", "plim", "verb", "/plɪm/", "phình to ra, trương lên (cổ)"),
    ("077322", "plimsolls", "noun", "/ˈplɪmsəlz/", "giày vải đế cao su (Anh)"),
    ("077323", "plink", "verb", "/plɪŋk/", "búng kêu lanh canh; bắn tập bia"),
    ("077324", "plinthite", "noun", "/ˈplɪnθaɪt/", "đất sét đỏ giàu sắt plinthit"),
    ("077325", "plinths", "noun", "/plɪnθs/", "bệ cột, chân đế tượng"),
    ("077326", "pliocence", "noun", "/ˈplaɪəsiːn/", "thế Pliocen (địa chất)"),
    ("077327", "pliosaurus", "noun", "/ˌplaɪəˈsɔːrəs/", "bò sát biển cổ Pliosaurus"),
    ("077328", "plk", "noun", "/ˌpiːɛlˈkeɪ/", "viết tắt tấm ván plank (plk)"),
    ("077329", "ploce", "noun", "/ˈploʊsiː/", "phép điệp từ nhấn mạnh (tu từ học)"),
    ("077330", "ploceidae", "noun", "/ploʊˈsiːɪdiː/", "họ Chim rồng rộc (Ploceidae)"),
    ("077331", "ploceus", "noun", "/ˈploʊsiəs/", "chi chim rồng rộc (Ploceus)"),
    ("077332", "plodded", "verb", "/ˈplɑːdɪd/", "đã lê bước nặng nề; làm cặm cụi"),
    ("077333", "ploddingly", "adv", "/ˈplɑːdɪŋli/", "một cách ì ạch, chậm chạp cần cù"),
    ("077334", "plods", "verb", "/plɑːdz/", "lê bước nặng nề; làm việc cặm cụi"),
    ("077335", "plonked", "verb", "/plɒŋkt/", "đã đặt mạnh phịch; gảy đàn lộp bộp"),
    ("077336", "plonkie", "noun", "/ˈplɒŋki/", "người nghiện rượu vang rẻ tiền (Úc)"),
    ("077337", "plonking", "verb", "/ˈplɒŋkɪŋ/", "đặt mạnh phịch xuống; búng gảy dây"),
    ("077338", "plonks", "verb", "/plɒŋks/", "đặt mạnh phịch xuống; búng gảy dây"),
    ("077339", "plopped", "verb", "/plɑːpt/", "đã rơi tõm, rơi phịch xuống"),
    ("077340", "plopping", "verb", "/ˈplɑːpɪŋ/", "rơi tõm, rơi phịch xuống"),
    ("077341", "plops", "verb", "/plɑːps/", "rơi tõm, rơi phịch xuống"),
    ("077342", "plotless", "adj", "/ˈplɑːtləs/", "không có cốt truyện rõ ràng"),
    ("077343", "plotlessness", "noun", "/ˈplɑːtləsnəs/", "tình trạng thiếu cốt truyện"),
    ("077344", "plots", "verb", "/plɑːts/", "vạch âm mưu; vẽ đồ thị; lập sơ đồ"),
    ("077345", "plotting", "verb", "/ˈplɑːtɪŋ/", "vạch âm mưu; vẽ đồ thị; lập sơ đồ"),
    ("077346", "ploughable", "adj", "/ˈplaʊəbəl/", "có thể cày bừa trồng trọt được"),
    ("077347", "ploughland", "noun", "/ˈplaʊˌlænd/", "đất canh tác, ruộng cày"),
    ("077348", "ploughpoint", "noun", "/ˈplaʊˌpɔɪnt/", "mũi lưỡi cày"),
    ("077349", "ploughs", "verb", "/plaʊz/", "cày đất, cày ruộng; xẻ sóng"),
    ("077350", "ploughwise", "adv", "/ˈplaʊwaɪz/", "theo hướng luống cày"),
    ("077351", "ploughwright", "noun", "/ˈplaʊˌraɪt/", "thợ làm và sửa máy cày, lưỡi cày"),
    ("077352", "ploughwrights", "noun", "/ˈplaʊˌraɪts/", "thợ làm và sửa máy cày, lưỡi cày"),
    ("077353", "plouter", "verb", "/ˈplaʊtər/", "lội bì bõm; làm việc lúng túng"),
    ("077354", "plowable", "adj", "/ˈplaʊəbəl/", "có thể cày bừa trồng trọt được"),
    ("077355", "plower", "noun", "/ˈplaʊər/", "người cày ruộng; máy cày"),
    ("077356", "plowland", "noun", "/ˈplaʊˌlænd/", "đất canh tác, ruộng cày"),
    ("077357", "plows", "verb", "/plaʊz/", "cày đất, cày ruộng; xẻ sóng"),
    ("077358", "plowwright", "noun", "/ˈplaʊˌraɪt/", "thợ làm và sửa máy cày, lưỡi cày"),
    ("077359", "pls", "adv", "/pliːz/", "làm ơn, xin vui lòng (viết tắt)"),
    ("077360", "pluckiness", "noun", "/ˈplʌkinəs/", "lòng gan dạ, tinh thần quả cảm"),
    ("077361", "plucking", "verb", "/ˈplʌkɪŋ/", "nhổ, giật, vặt lông; gảy dây đàn"),
    ("077362", "pluckless", "adj", "/ˈplʌkləs/", "nhút nhát, thiếu gan dạ"),
    ("077363", "plucks", "verb", "/plʌks/", "nhổ, giật, vặt lông; gảy dây đàn"),
    ("077364", "plugging", "verb", "/ˈplʌɡɪŋ/", "cắm phích; bịt kín lỗ; quảng bá"),
    ("077365", "plugs", "verb", "/plʌɡz/", "cắm phích; bịt kín lỗ; quảng bá"),
    ("077366", "plumassier", "noun", "/pluːˈmæsjɛr/", "người buôn bán lông vũ trang trí"),
    ("077367", "plumate", "adj", "/ˈpluːmeɪt/", "có lông vũ; có chùm lông mịn"),
    ("077368", "plumbable", "adj", "/ˈplʌməbəl/", "có thể đo dò độ sâu được"),
    ("077369", "plumbaginaceae", "noun", "/plʌmˌbædʒɪˈneɪsiː/", "họ Đuôi công (Plumbaginaceae)"),
    ("077370", "plumbaginaceous", "adj", "/plʌmˌbædʒɪˈneɪʃəs/", "thuộc họ Đuôi công"),
    ("077371", "plumbaginales", "noun", "/plʌmˌbædʒɪˈneɪliːz/", "bộ Đuôi công (Plumbaginales)"),
    ("077372", "plumbaginous", "adj", "/plʌmˈbædʒɪnəs/", "giống hoặc chứa than chì (graphit)"),
    ("077373", "plumbean", "adj", "/ˈplʌmbiən/", "thuộc chì; nặng nề đần độn như chì"),
    ("077374", "plumbed", "verb", "/plʌmd/", "đã dò độ sâu; lắp ống nước; thăm dò"),
    ("077375", "plumbeous", "adj", "/ˈplʌmbiəs/", "có màu xám chì; nặng như chì"),
    ("077376", "plumbery", "noun", "/ˈplʌməri/", "nghề thợ ống nước; xưởng chì"),
    ("077377", "plumbic", "adj", "/ˈplʌmbɪk/", "thuộc chì hóa trị bốn"),
    ("077378", "plumbiferous", "adj", "/plʌmˈbɪfərəs/", "có chứa quặng chì"),
    ("077379", "plumbism", "noun", "/ˈplʌmbɪzəm/", "bệnh nhiễm độc chì (y học)"),
    ("077380", "plumbless", "adj", "/ˈplʌmləs/", "sâu thẳm không đo dò tới đáy"),
    ("077381", "plumbous", "adj", "/ˈplʌmbəs/", "thuộc chì hóa trị hai"),
    ("077382", "plumbs", "verb", "/plʌmz/", "dò độ sâu; lắp ống nước; thăm dò"),
    ("077383", "plumcot", "noun", "/ˈplʌmkɒt/", "quả lai giữa mận và mơ (plumcot)"),
    ("077384", "plumelet", "noun", "/ˈpluːmlɪt/", "chiếc lông vũ nhỏ; lá mầm nhỏ"),
    ("077385", "plumelets", "noun", "/ˈpluːmlɪts/", "chiếc lông vũ nhỏ; lá mầm nhỏ"),
    ("077386", "plumelike", "adj", "/ˈpluːmlaɪk/", "giống lông vũ; mềm mịn như lông"),
    ("077387", "plumes", "verb", "/pluːmz/", "rỉa lông; bốc lên cột; tự đắc"),
    ("077388", "plumiera", "noun", "/pluːˈmɪrə/", "chi cây hoa đại, hoa sứ (Plumeria)"),
    ("077389", "pluming", "verb", "/ˈpluːmɪŋ/", "rỉa lông; bốc lên cột; tự đắc"),
    ("077390", "plumiped", "adj", "/ˈpluːmɪpɛd/", "có lông phủ tới tận bàn chân (chim)"),
    ("077391", "plumlike", "adj", "/ˈplʌmlaɪk/", "giống như quả mận"),
    ("077392", "plummeted", "verb", "/ˈplʌmɪtɪd/", "đã lao thẳng xuống, giảm mạnh"),
    ("077393", "plummeting", "verb", "/ˈplʌmɪtɪŋ/", "lao thẳng xuống, giảm mạnh"),
    ("077394", "plummets", "verb", "/ˈplʌmɪts/", "lao thẳng xuống, giảm mạnh"),
    ("077395", "plumosely", "adv", "/ˈpluːmoʊsli/", "theo dạng chùm lông vũ"),
    ("077396", "plumosity", "noun", "/pluːˈmɒsɪti/", "trạng thái có nhiều lông vũ"),
    ("077397", "plumped", "verb", "/plʌmpt/", "đã rơi phịch; làm căng phồng; dồn"),
    ("077398", "plumper", "noun", "/ˈplʌmpər/", "miếng độn má; người mũm mĩm hơn"),
    ("077399", "plumply", "adv", "/ˈplʌmpli/", "một cách thẳng thắn; tròn trịa"),
    ("077400", "plumps", "verb", "/plʌmps/", "rơi phịch xuống; làm căng phồng"),
    ("077401", "plumpy", "adj", "/ˈplʌmpi/", "hơi tròn trịa, mũm mĩm dễ thương"),
    ("077402", "plumula", "noun", "/ˈpluːmjʊlə/", "lông tơ mịn; vảy cánh; chồi mầm"),
]

with open("scratch/b36_r05_raw_p4.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r05_p4.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r05_p4 saved OK")
