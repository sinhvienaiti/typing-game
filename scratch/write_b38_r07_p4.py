import json

RECORDS = [
    ("088303", "southwestwardly", "adv", "/ˌsaʊθˈwɛstwərdli/", "theo hướng tây nam"),
    ("088304", "souvlakia", "noun", "/suːˈvlɑːkjə/", "món thịt xiên nướng Hy Lạp"),
    ("088305", "souwester", "noun", "/ˌsaʊˈwɛstər/", "mũ đi biển chống mưa; gió tây nam"),
    ("088306", "sovereignly", "adv", "/ˈsɑːvrənli/", "tối cao; đầy uy quyền tuyệt đối"),
    ("088307", "sovereigns", "noun", "/ˈsɑːvrənz/", "quốc vương; đồng bảng vàng xưa"),
    ("088308", "sovietisation", "noun", "/ˌsoʊviətəˈzeɪʃən/", "sự Xô-viết hóa"),
    ("088309", "sovietise", "verb", "/ˈsoʊviəˌtaɪz/", "Xô-viết hóa"),
    ("088310", "sovietization", "noun", "/ˌsoʊviətəˈzeɪʃən/", "sự Xô-viết hóa"),
    ("088311", "sovietize", "verb", "/ˈsoʊviəˌtaɪz/", "Xô-viết hóa"),
    ("088312", "sovkhoz", "noun", "/sɔːvˈxɔːz/", "nông trường quốc doanh Liên Xô cũ"),
    ("088313", "sowback", "noun", "/ˈsaʊˌbæk/", "cồn cát dải thấp; khối sắt dư đúc"),
    ("088314", "sowbane", "noun", "/ˈsaʊˌbeɪn/", "cây rau muối dại độc cho lợn"),
    ("088315", "sowbelly", "noun", "/ˈsaʊˌbɛli/", "thịt ba chỉ lợn ướp muối"),
    ("088316", "sowbread", "noun", "/ˈsaʊˌbrɛd/", "cây anh thảo củ hoa hồng"),
    ("088317", "sowcar", "noun", "/saʊˈkɑːr/", "chủ ngân hàng Ấn Độ truyền thống"),
    ("088318", "sowdrunk", "adj", "/ˈsaʊˌdrʌŋk/", "say bí tỉ; say khướt không biết gì"[:35]),
    ("088319", "sowed", "verb", "/soʊd/", "đã gieo hạt; đã gieo rắc"),
    ("088320", "sowing", "verb", "/ˈsoʊɪŋ/", "đang gieo hạt; đang gieo rắc"),
    ("088321", "sowkar", "noun", "/saʊˈkɑːr/", "chủ ngân hàng Ấn Độ truyền thống"),
    ("088322", "sows", "verb", "/soʊz/", "gieo hạt; gieo rắc"),
    ("088323", "sox", "noun", "/sɑːks/", "đôi tất; vớ chân (cách viết ngắn)"),
    ("088324", "sp", "noun", "/ˌɛsˈpiː/", "chính tả; cách viết (viết tắt)"),
    ("088325", "spaceful", "adj", "/ˈspeɪsfəl/", "rộng rãi thoáng đãng"),
    ("088326", "spaceless", "adj", "/ˈspeɪsləs/", "không gian vô tận; không giới hạn"),
    ("088327", "spacemark", "noun", "/ˈspeɪsˌmɑːrk/", "ký hiệu dấu cách (in ấn)"),
    ("088328", "spacemedicine", "noun", "/ˈspeɪsˌmɛdɪsən/", "y học du hành vũ trụ"),
    ("088329", "spaceport", "noun", "/ˈspeɪsˌpɔːrt/", "sân bay phóng tàu vũ trụ"),
    ("088330", "spacer", "noun", "/ˈspeɪsər/", "miếng đệm căn khoảng cách"),
    ("088331", "spaces", "noun", "/ˈspeɪsɪz/", "khoảng trống; không gian; chỗ ngồi"),
    ("088332", "spaceships", "noun", "/ˈspeɪsˌʃɪps/", "tàu vũ trụ"),
    ("088333", "spacetime", "noun", "/ˈspeɪsˌtaɪm/", "không-thời gian (vật lý)"),
    ("088334", "spacewalking", "noun", "/ˈspeɪsˌwɔːkɪŋ/", "việc đi bộ ngoài không gian vũ trụ"),
    ("088335", "spaceward", "adv", "/ˈspeɪswərd/", "hướng ra ngoài không gian vũ trụ"),
    ("088336", "spacewards", "adv", "/ˈspeɪswərdz/", "hướng ra ngoài không gian vũ trụ"),
    ("088337", "spacewoman", "noun", "/ˈspeɪsˌwʊmən/", "nữ phi hành gia vũ trụ"),
    ("088338", "spacings", "noun", "/ˈspeɪsɪŋz/", "khoảng cách giữa các vật hay chữ"),
    ("088339", "spaciotemporal", "adj", "/ˌspeɪʃoʊˈtɛmpərəl/", "thuộc không-thời gian"),
    ("088340", "spaciously", "adv", "/ˈspeɪʃəsli/", "rộng rãi thoáng đãng"),
    ("088341", "spaded", "verb", "/ˈspeɪdɪd/", "đã đào xới bằng mai thuổng"),
    ("088342", "spadeful", "noun", "/ˈspeɪdˌfʊl/", "một xẻng đầy; một mai đất đầy"),
    ("088343", "spader", "noun", "/ˈspeɪdər/", "người đào xới đất bằng mai"),
    ("088344", "spades", "verb", "/speɪdz/", "đào xới bằng mai thuổng"),
    ("088345", "spadesman", "noun", "/ˈspeɪdzmən/", "người đào đất bằng mai thuổng"),
    ("088346", "spadger", "noun", "/ˈspædʒər/", "chim sẻ (tiếng lóng Anh)"),
    ("088347", "spadiceous", "adj", "/spəˈdɪʃəs/", "nâu hạt dẻ; có cụm hoa bông mo"),
    ("088348", "spadices", "noun", "/spəˈdaɪsiːz/", "cụm hoa bông mo (họ Ráy)"),
    ("088349", "spadicose", "adj", "/ˈspædɪˌkoʊs/", "có cụm hoa dạng bông mo"),
    ("088350", "spadille", "noun", "/spəˈdɪl/", "quân át bích (bài ombre)"),
    ("088351", "spading", "verb", "/ˈspeɪdɪŋ/", "đang đào xới đất bằng mai thuổng"),
    ("088352", "spado", "noun", "/ˈspeɪdoʊ/", "người bị thiến; động vật vô sinh"),
    ("088353", "spadones", "noun", "/spəˈdoʊniːz/", "người bị thiến; động vật vô sinh"),
    ("088354", "spae", "verb", "/speɪ/", "tiên đoán; bói toán (Scotland)"),
    ("088355", "spaewife", "noun", "/ˈspeɪˌwaɪf/", "bà thầy bói (Scotland)"),
    ("088356", "spahee", "noun", "/spɑːˈhiː/", "kỵ binh đế chế Ottoman xưa"),
    ("088357", "spahi", "noun", "/spɑːˈhiː/", "kỵ binh đế chế Ottoman xưa"),
    ("088358", "spake", "verb", "/speɪk/", "đã nói (quá khứ cổ của speak)"),
    ("088359", "spalacidae", "noun", "/spəˈlæsɪˌdiː/", "họ Chuột dũi mù (Spalacidae)"),
    ("088360", "spalder", "noun", "/ˈspɔːldər/", "công nhân đập nghiền quặng đá"),
    ("088361", "spallbale", "adj", "/ˈspɔːləbəl/", "có thể đập vỡ thành mảnh đá"),
    ("088362", "spalling", "noun", "/ˈspɔːlɪŋ/", "hiện tượng bong tróc nứt vỡ đá"),
    ("088363", "spalpeen", "noun", "/spælˈpiːn/", "gã vô lại; thằng nhóc tinh quái"),
    ("088364", "spandril", "noun", "/ˈspændrəl/", "mảng tường tam giác trên vòm cung"),
    ("088365", "spangles", "verb", "/ˈspæŋɡəlz/", "đính kim sa lấp lánh; điểm lấp lánh"[:35]),
    ("088366", "spangling", "verb", "/ˈspæŋɡlɪŋ/", "đang đính kim sa lấp lánh"),
    ("088367", "spanked", "verb", "/spæŋkt/", "đã đánh đòn vào mông; thắng dễ"),
    ("088368", "spanks", "verb", "/spæŋks/", "đánh đòn vào mông; phóng vút đi"),
    ("088369", "spanless", "adj", "/ˈspænləs/", "không thể đo sải hết; vô biên"),
    ("088370", "spanners", "noun", "/ˈspænərz/", "cờ lê vặn ốc"),
    ("088371", "spans", "noun", "/spænz/", "sải tay; nhịp cầu; khoảng thời gian"),
    ("088372", "sparable", "noun", "/ˈspɛrəbəl/", "đinh không mũ đóng gót giày xưa"),
    ("088373", "sparaxis", "noun", "/spəˈræksɪs/", "chi hoa loa kèn Nam Phi Sparaxis"),
    ("088374", "spared", "verb", "/spɛrd/", "đã tha cho; đã dành dụm tiết kiệm"),
    ("088375", "sparely", "adv", "/ˈspɛrli/", "thanh đạm sơ sài; dè sẻn ít ỏi"),
    ("088376", "sparerib", "noun", "/ˈspɛrˌrɪb/", "sườn non heo nướng"),
    ("088377", "spares", "verb", "/spɛrz/", "tha cho; dành ra; kiêng cữ"),
    ("088378", "sparganiaceae", "noun", "/ˌspɑːrɡəniˈeɪsiːˌiː/", "họ Thủy liễu (Sparganiaceae)"),
    ("088379", "sparganium", "noun", "/spɑːrˈɡeɪniəm/", "chi Thủy liễu (Sparganium)"),
    ("088380", "sparger", "noun", "/ˈspɑːrdʒər/", "vòi phun rưới nước nấu bia"),
    ("088381", "sparget", "noun", "/ˈspɑːrdʒɪt/", "ống rắc nước; vòi tưới phun"),
    ("088382", "sparid", "noun", "/ˈspærɪd/", "cá tráp biển họ Sparidae"),
    ("088383", "sparidae", "noun", "/ˈspærɪˌdiː/", "họ Cá tráp (Sparidae)"),
    ("088384", "sparingness", "noun", "/ˈspɛrɪŋnəs/", "tính tiết kiệm dè sẻn; vẻ thanh đạm"[:35]),
    ("088385", "sparked", "verb", "/spɑːrkt/", "đã tóe tia lửa; đã khơi nguồn"),
    ("088386", "sparking", "verb", "/ˈspɑːrkɪŋ/", "đang tóe tia lửa; đang khơi mào"),
    ("088387", "sparkish", "adj", "/ˈspɑːrkɪʃ/", "bảnh bao ăn diện; sôi nổi phóng tú"[:35]),
    ("088388", "sparkleberry", "noun", "/ˈspɑːrkəlˌbɛri/", "cây việt quất bụi cao Bắc Mỹ"),
    ("088389", "sparkled", "verb", "/ˈspɑːrkəld/", "đã lấp lánh ánh sáng; sủi tăm"),
    ("088390", "sparkles", "verb", "/ˈspɑːrkəlz/", "lấp lánh rực rỡ; sủi bọt tăm"),
    ("088391", "sparkless", "adj", "/ˈspɑːrkləs/", "không có tia lửa; tẻ nhạt"),
    ("088392", "sparklet", "noun", "/ˈspɑːrklɪt/", "tia sáng nhỏ lấp lánh; tia lửa nhỏ"),
    ("088393", "sparks", "verb", "/spɑːrks/", "tóe tia lửa điện; khơi nguồn hứng"),
    ("088394", "sparkwear", "noun", "/ˈspɑːrkˌwɛr/", "sự mài mòn điện cực do phóng điện"[:35]),
    ("088395", "sparky", "adj", "/ˈspɑːrki/", "sôi nổi hoạt bát; dí dỏm"),
    ("088396", "sparmannia", "noun", "/spɑːrˈmæniə/", "chi cây vông gai châu Phi Sparmannia"[:35]),
    ("088397", "sparoid", "noun", "/ˈspɛrɔɪd/", "cá giống cá tráp; cá tráp biển"),
    ("088398", "sparred", "verb", "/spɑːrd/", "đã đấu tập quyền anh; tranh luận"),
    ("088399", "sparry", "adj", "/ˈspɑːri/", "có tinh thể tách phẳng ánh thủy tinh"[:35]),
    ("088400", "spars", "verb", "/spɑːrz/", "đấu tập quyền anh; đấu khẩu nhẹ"),
    ("088401", "spartacan", "adj", "/ˈspɑːrtəkən/", "thuộc phong trào Spartacus (Đức)"),
    ("088402", "spartacism", "noun", "/ˈspɑːrtəˌsɪzəm/", "chủ trương cách mạng Spartacus"),
]

# Cleanly replace slices / long lines <= 35 chars
RECORDS[15] = ("088318", "sowdrunk", "adj", "/ˈsaʊˌdrʌŋk/", "say bí tỉ; say khướt")
RECORDS[62] = ("088365", "spangles", "verb", "/ˈspæŋɡəlz/", "đính kim sa lấp lánh; điểm sáng")
RECORDS[81] = ("088384", "sparingness", "noun", "/ˈspɛrɪŋnəs/", "tính tiết kiệm; sự thanh đạm")
RECORDS[84] = ("088387", "sparkish", "adj", "/ˈspɑːrkɪʃ/", "bảnh bao ăn diện; sôi nổi")
RECORDS[91] = ("088394", "sparkwear", "noun", "/ˈspɑːrkˌwɛr/", "mài mòn điện cực do tia lửa điện")
RECORDS[93] = ("088396", "sparmannia", "noun", "/spɑːrˈmæniə/", "chi cây bụi hoa trắng Sparmannia")
RECORDS[96] = ("088399", "sparry", "adj", "/ˈspɑːri/", "dạng tinh thể ánh thủy tinh")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r07_raw_p4.json"))
by_id = {r["id"].split(".")[-1]: r for r in raw}
out = []
for sid, hw, pos, ipa, vi in RECORDS:
    rec = dict(by_id[sid])
    assert rec["hw"] == hw, (sid, hw, rec["hw"])
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

json.dump(out, open("scratch/b38_r07_reviewed_p4.json", "w"), ensure_ascii=False, indent=2)
print("b38_r07_p4 saved OK")
