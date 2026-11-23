import json

records = [
    ("081403", "raetam", "noun", "/ˈriːtəm/", "cây bụi sa mạc raetam (Retama)"),
    ("081404", "rafale", "noun", "/rɑːˈfɑːl/", "tràng đạn liên thanh; cơn gió giật"),
    ("081405", "raff", "noun", "/ræf/", "đồ phế thải; bọn hạ lưu (lóng)"),
    ("081406", "raffinate", "noun", "/ˈræfəˌneɪt/", "phần dung dịch tinh lọc còn lại"),
    ("081407", "raffinates", "noun", "/ˈræfəˌneɪts/", "các phần dung dịch tinh lọc còn lại"),
    ("081408", "raffishly", "adv", "/ˈræfɪʃli/", "một cách phóng túng, phong trần"),
    ("081409", "raffishness", "noun", "/ˈræfɪʃnəs/", "vẻ hào hoa phóng túng, phong trần"),
    ("081410", "rafflesiaceae", "noun", "/rəˌfliːziˈeɪsiː/", "họ Hoa xác thối khổng lồ"),
    ("081411", "raffling", "verb", "/ˈræflɪŋ/", "bán vé số, mở xổ số rút thăm trúng"),
    ("081412", "rafted", "verb", "/ˈræftɪd/", "đã đi bè, đã kết bè gỗ vượt thác"),
    ("081413", "raftered", "adj", "/ˈræftərd/", "có xà kèo gỗ mái nhà lộ thiên"),
    ("081414", "rafting", "verb", "/ˈræftɪŋ/", "đi bè gỗ; chèo xuồng vượt thác"),
    ("081415", "raftman", "noun", "/ˈræftmən/", "người lái bè gỗ, thợ chèo bè"),
    ("081416", "raftsman", "noun", "/ˈræftsmən/", "người lái bè gỗ trên sông"),
    ("081417", "raga", "noun", "/ˈrɑːɡə/", "điệu nhạc cổ điển Ấn Độ (raga)"),
    ("081418", "ragebait", "noun", "/ˈreɪdʒˌbeɪt/", "nội dung câu tương tác gây phẫn nộ"),
    ("081419", "raged", "verb", "/reɪdʒd/", "đã nổi cơn thịnh nộ; đã hoành hành"),
    ("081420", "ragee", "noun", "/ˈrɑːɡi/", "cây kê ngón tay Ấn Độ (ragi)"),
    ("081421", "rages", "verb", "/ˈreɪdʒɪz/", "nổi cơn thịnh nộ; hoành hành dữ dội"),
    ("081422", "ragfair", "noun", "/ˈræɡˌfɛr/", "chợ trời bán quần áo cũ và đồ phế"),
    ("081423", "raggedness", "noun", "/ˈræɡɪdnəs/", "sự rách rưới; vẻ lởm chởm xù xì"),
    ("081424", "ragging", "verb", "/ˈræɡɪŋ/", "trêu chọc, bắt nạt tân sinh viên"),
    ("081425", "raglet", "noun", "/ˈræɡlɪt/", "rãnh xây tường lắp máng xối chì"),
    ("081426", "ragman", "noun", "/ˈræɡmən/", "người thu mua giẻ rách đồng nát"),
    ("081427", "ragmen", "noun", "/ˈræɡmən/", "những người thu mua giẻ rách cũ"),
    ("081428", "rags", "verb", "/ræɡz/", "mắng nhiếc; trêu chọc, bắt nạt"),
    ("081429", "ragshop", "noun", "/ˈræɡˌʃɑːp/", "tiệm mua bán giẻ rách và quần áo cũ"),
    ("081430", "ragsorter", "noun", "/ˈræɡˌsɔːrtər/", "công nhân phân loại vải vụn"),
    ("081431", "ragstone", "noun", "/ˈræɡˌstoʊn/", "đá tảng thô cứng dùng xây tường"),
    ("081432", "raided", "verb", "/ˈreɪdɪd/", "đã đột kích, càn quét; lục soát"),
    ("081433", "raids", "verb", "/reɪdz/", "đột kích, cướp phá; truy quét"),
    ("081434", "railage", "noun", "/ˈreɪlɪdʒ/", "vận chuyển đường sắt; cước tàu"),
    ("081435", "railbird", "noun", "/ˈreɪlˌbɜːrd/", "người tựa rào xem đua ngựa (Mỹ)"),
    ("081436", "railed", "verb", "/reɪld/", "đã rào lan can; đã mắng gay gắt"),
    ("081437", "railer", "noun", "/ˈreɪlər/", "người hay chửi rủa, kẻ công kích"),
    ("081438", "railroaded", "verb", "/ˈreɪlˌroʊdɪd/", "đã ép thông qua vội; vu oan"),
    ("081439", "railroads", "noun", "/ˈreɪlˌroʊdz/", "các tuyến đường sắt, hãng đường sắt"),
    ("081440", "railways", "noun", "/ˈreɪlˌweɪz/", "các tuyến đường sắt (Anh)"),
    ("081441", "raimentless", "adj", "/ˈreɪməntləs/", "không quần áo che thân, trần truồng"),
    ("081442", "rainbird", "noun", "/ˈreɪnˌbɜːrd/", "chim báo mưa nhiệt đới (cuckoo)"),
    ("081443", "rainbows", "noun", "/ˈreɪnˌboʊz/", "những chiếc cầu vồng bảy sắc"),
    ("081444", "raincloud", "noun", "/ˈreɪnˌklaʊd/", "đám mây đen mang mưa, mây vũ tầng"),
    ("081445", "rained", "verb", "/reɪnd/", "đã đổ mưa, đã rơi xuống như mưa"),
    ("081446", "rainfly", "noun", "/ˈreɪnˌflaɪ/", "tấm bạt phủ chống mưa trên nóc lều"),
    ("081447", "raininess", "noun", "/ˈreɪninəs/", "tình trạng mưa dầm dề, nhiều mưa"),
    ("081448", "rains", "verb", "/reɪnz/", "đổ mưa, rơi mưa; trút xuống dồn dập"),
    ("081449", "raintight", "adj", "/ˈreɪnˌtaɪt/", "kín nước mưa, chống thấm mưa tốt"),
    ("081450", "rainwear", "noun", "/ˈreɪnˌwɛr/", "quần áo đi mưa, đồ chống mưa"),
    ("081451", "raisable", "adj", "/ˈreɪzəbəl/", "có thể nâng lên, giơ lên, gây quỹ"),
    ("081452", "raiseable", "adj", "/ˈreɪzəbəl/", "có thể nâng lên, giơ lên (biến thể)"),
    ("081453", "raisers", "noun", "/ˈreɪzərz/", "người chăn nuôi; người quyên góp"),
    ("081454", "raises", "verb", "/ˈreɪzɪz/", "nâng lên, giơ lên; nuôi; gây quỹ"),
    ("081455", "rait", "verb", "/reɪt/", "ngâm nước làm mục vỏ thân lanh (cổ)"),
    ("081456", "raiu", "noun", "/ˌɑːreɪaɪˈjuː/", "xét nghiệm hấp thu iốt phóng xạ"),
    ("081457", "rajanya", "noun", "/ˈrɑːdʒənjə/", "đẳng cấp vương công chiến binh Ấn"),
    ("081458", "rajidae", "noun", "/ˈreɪdʒɪˌdiː/", "họ Cá đuối bướm gai (Rajidae)"),
    ("081459", "rajiformes", "noun", "/ˌreɪdʒəˈfɔːrmiːz/", "bộ Cá đuối (Rajiformes)"),
    ("081460", "rakaposhi", "noun", "/ˌrɑːkəˈpoʊʃi/", "đỉnh núi tuyết Rakaposhi (Pakistan)"),
    ("081461", "raked", "verb", "/reɪkt/", "đã cào gom lá; đã bắn quét dọc"),
    ("081462", "rakehell", "noun", "/ˈreɪkˌhɛl/", "tay chơi trác táng, kẻ buông thả"),
    ("081463", "rakehelly", "adj", "/ˈreɪkˌhɛli/", "ăn chơi trác táng, phóng đãng"),
    ("081464", "raker", "noun", "/ˈreɪkər/", "người cào; thanh chống; răng cào"),
    ("081465", "rakes", "verb", "/reɪks/", "cào gom lá; rà soát; bắn dọc"),
    ("081466", "rakety", "adj", "/ˈrækəti/", "ồn ào náo nhiệt, phóng đãng ăn chơi"),
    ("081467", "raking", "verb", "/ˈreɪkɪŋ/", "cào gom; rà soát kỹ; bắn quét dọc"),
    ("081468", "rakishness", "noun", "/ˈreɪkɪʃnəs/", "vẻ phong trần; thói trác táng"),
    ("081469", "rakshas", "noun", "/ˈrɑːkʃəs/", "ác quỷ La Sát (thần thoại Ấn Độ)"),
    ("081470", "rallentandi", "noun", "/ˌrɑːlənˈtɑːndi/", "những đoạn nhạc đánh chậm dần lại"),
    ("081471", "rallentando", "adj", "/ˌrɑːlənˈtɑːndoʊ/", "chậm dần đều (chỉ dẫn âm nhạc)"),
    ("081472", "rallidae", "noun", "/ˈrælɪˌdiː/", "họ Gà nước, trích cồ (Rallidae)"),
    ("081473", "rallied", "verb", "/ˈrælɪd/", "đã tập hợp lại; đã hồi phục giá trị"),
    ("081474", "rallies", "verb", "/ˈrælɪz/", "tập hợp lại; hồi phục; trêu đùa"),
    ("081475", "ralline", "adj", "/ˈrælaɪn/", "thuộc họ chim gà nước (Rallidae)"),
    ("081476", "rallycross", "noun", "/ˈræliˌkrɔːs/", "môn đua ô tô đường hỗn hợp ngắn"),
    ("081477", "rallyingly", "adv", "/ˈræliɪŋli/", "với giọng trêu đùa châm chọc"),
    ("081478", "ramal", "adj", "/ˈreɪməl/", "thuộc cành cây, mọc trên nhánh"),
    ("081479", "ramalina", "noun", "/ˌræməˈlaɪnə/", "chi địa y dạng bụi Ramalina"),
    ("081480", "ramanavami", "noun", "/ˌrɑːməˈnɑːvəmi/", "lễ hội mừng ngày sinh thần Rama"),
    ("081481", "ramate", "adj", "/ˈreɪmeɪt/", "có cành nhánh, phân nhánh"),
    ("081482", "rambled", "verb", "/ˈræmbəld/", "đã đi dạo vẩn vơ; đã nói lan man"),
    ("081483", "rambles", "verb", "/ˈræmbəlz/", "đi dạo vẩn vơ; nói viết lan man"),
    ("081484", "ramblingly", "adv", "/ˈræmblɪŋli/", "một cách lan man, rời rạc"),
    ("081485", "rambotan", "noun", "/ræmˈbuːtən/", "cây chôm chôm, quả chôm chôm (lỗi)"),
    ("081486", "rambutans", "noun", "/ræmˈbuːtənz/", "những quả chôm chôm"),
    ("081487", "ramdrive", "noun", "/ˈræmˌdraɪv/", "ổ đĩa ảo trên bộ nhớ RAM (tin học)"),
    ("081488", "rameal", "adj", "/ˈreɪmiəl/", "thuộc cành cây, ở nhánh (thực vật)"),
    ("081489", "ramellose", "adj", "/rəˈmɛloʊs/", "có nhiều cành nhánh nhỏ (thực vật)"),
    ("081490", "rament", "noun", "/ˈreɪmənt/", "vảy lông nhỏ phủ lá non (dương xỉ)"),
    ("081491", "ramequin", "noun", "/ˈræməkɪn/", "bánh phô mai nướng; chén sứ nướng"),
    ("081492", "ramiferous", "adj", "/rəˈmɪfərəs/", "mang cành nhánh, phân nhánh nhiều"),
    ("081493", "ramified", "verb", "/ˈræməˌfaɪd/", "đã phân nhánh, tỏa nhánh chằng chịt"),
    ("081494", "ramifies", "verb", "/ˈræməˌfaɪz/", "phân nhánh, tỏa nhánh chằng chịt"),
    ("081495", "ramiflorous", "adj", "/ˌræməˈflɔːrəs/", "nở hoa trực tiếp trên cành cây lớn"),
    ("081496", "ramiform", "adj", "/ˈreɪməˌfɔːrm/", "có dạng giống cành cây phân nhánh"),
    ("081497", "ramifying", "verb", "/ˈræməˌfaɪɪŋ/", "phân nhánh, tỏa ra nhiều hệ quả"),
    ("081498", "ramigenous", "adj", "/rəˈmɪdʒənəs/", "mọc nhánh, mọc ra từ cành"),
    ("081499", "ramigerous", "adj", "/rəˈmɪdʒərəs/", "có nhánh, mang cành (sinh học)"),
    ("081500", "rammaged", "adj", "/ˈræmɪdʒd/", "say rượu khướt (tiếng lóng cổ Anh)"),
    ("081501", "ramman", "noun", "/ˈræmən/", "thần bão tố Ramman (Lưỡng Hà cổ)"),
    ("081502", "rammed", "verb", "/ræmd/", "đã đâm sầm vào, đã nện chặt xuống"),
]

raw = json.load(open("scratch/b37_r03_raw_p5.json"))
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
with open("scratch/b37_r03_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r03_p5 saved OK")
