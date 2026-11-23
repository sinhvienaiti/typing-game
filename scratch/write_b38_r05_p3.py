import json

RECORDS = [
    ("087203", "sisterlike", "adj", "/ˈsɪstərˌlaɪk/", "như chị em gái; thân thiết như chị"[:35]),
    ("087204", "sisterliness", "noun", "/ˈsɪstərlinəs/", "tình chị em gắn bó thân thiết"),
    ("087205", "sisters", "noun", "/ˈsɪstərz/", "chị em gái; nữ tu sĩ"),
    ("087206", "sistrurus", "noun", "/sɪˈstrʊrəs/", "chi rắn chuông lùn Bắc Mỹ"),
    ("087207", "sisyridae", "noun", "/sɪˈsɪrɪˌdiː/", "họ Bọ cánh gân ăn bọt biển"),
    ("087208", "sisyrinchium", "noun", "/ˌsɪsəˈrɪŋkiəm/", "chi cỏ mắt xanh Sisyrinchium"),
    ("087209", "sited", "verb", "/ˈsaɪtɪd/", "đã đặt vị trí; đã chọn địa điểm"),
    ("087210", "sites", "verb", "/saɪts/", "đặt vị trí; chọn địa điểm xây dựng"[:35]),
    ("087211", "sitfast", "noun", "/ˈsɪtˌfæst/", "vết chai loét lưng ngựa do yên cọ"),
    ("087212", "sith", "conj", "/sɪθ/", "kể từ khi; bởi vì (từ cổ)"),
    ("087213", "siting", "verb", "/ˈsaɪtɪŋ/", "đang đặt vị trí; đang chọn địa điểm"[:35]),
    ("087214", "sitiology", "noun", "/ˌsɪtiˈɑːlədʒi/", "dinh dưỡng học; khoa học thực phẩm"[:35]),
    ("087215", "sitology", "noun", "/saɪˈtɑːlədʒi/", "dinh dưỡng học; khoa học ăn uống"),
    ("087216", "sitophylus", "noun", "/saɪˈtɑːfɪləs/", "chi mọt gạo hại ngũ cốc"),
    ("087217", "sitotroga", "noun", "/ˌsɪtəˈtroʊɡə/", "chi ngài mạch hại hạt ngũ cốc"),
    ("087218", "sits", "verb", "/sɪts/", "ngồi; tọa lạc; họp bàn; ấp trứng"),
    ("087219", "sitsang", "noun", "/ˈsiːˌtsɑːŋ/", "vùng Tây Tạng"),
    ("087220", "sittidae", "noun", "/ˈsɪtɪˌdiː/", "họ Chim trèo cây (Sittidae)"),
    ("087221", "situates", "verb", "/ˈsɪtʃuˌeɪts/", "đặt vào vị trí; xác định vị trí"),
    ("087222", "situating", "verb", "/ˈsɪtʃuˌeɪtɪŋ/", "đang đặt vào vị trí; xác định chỗ"[:35]),
    ("087223", "situations", "noun", "/ˌsɪtʃuˈeɪʃənz/", "tình huống; hoàn cảnh; vị trí"),
    ("087224", "situs", "noun", "/ˈsaɪtəs/", "vị trí giải phẫu; vị thế pháp lý"),
    ("087225", "sivaism", "noun", "/ˈʃɪvəˌɪzəm/", "Ấn Độ giáo tôn thờ thần Shiva"),
    ("087226", "sivaistic", "adj", "/ˌʃɪvəˈɪstɪk/", "thuộc tín ngưỡng thờ thần Shiva"),
    ("087227", "sivaite", "noun", "/ˈʃɪvəˌaɪt/", "tín đồ thờ thần Shiva"),
    ("087228", "sivapithecus", "noun", "/ˌʃɪvəpɪˈθiːkəs/", "vượn nhân hình hóa thạch cổ"),
    ("087229", "sixain", "noun", "/ˈsɪkseɪn/", "bài thơ sáu câu; khổ thơ sáu dòng"),
    ("087230", "sixsome", "noun", "/ˈsɪksəm/", "nhóm sáu người; trận đấu sáu người"[:35]),
    ("087231", "sixte", "noun", "/siːkst/", "thế thủ thứ sáu trong đấu kiếm"),
    ("087232", "sixteenmo", "noun", "/ˌsɪksˈtiːnˌmoʊ/", "sách in khổ mười sáu"),
    ("087233", "sizar", "noun", "/ˈsaɪzər/", "sinh viên được miễn giảm phí xưa"),
    ("087234", "sizarship", "noun", "/ˈsaɪzərˌʃɪp/", "suất học bổng miễn phí đại học xưa"[:35]),
    ("087235", "sizeableness", "noun", "/ˈsaɪzəbəlnəs/", "kích cỡ khá lớn; tầm vóc đồ sộ"),
    ("087236", "sizer", "noun", "/ˈsaɪzər/", "máy phân loại cỡ; người định cỡ"),
    ("087237", "sizes", "verb", "/ˈsaɪzɪz/", "phân loại kích cỡ; hồ vải; đánh giá"[:35]),
    ("087238", "sizings", "noun", "/ˈsaɪzɪŋz/", "keo hồ vải giấy; việc phân cỡ"),
    ("087239", "sizy", "adj", "/ˈsaɪzi/", "sánh dính như keo hồ"),
    ("087240", "sizzled", "verb", "/ˈsɪzəld/", "đã kêu xèo xèo; nóng bỏng rát"),
    ("087241", "sizzler", "noun", "/ˈsɪzlər/", "ngày nắng như thiêu; đĩa bít tết"),
    ("087242", "sizzles", "verb", "/ˈsɪzəlz/", "kêu xèo xèo (chiên rán); nóng rực"),
    ("087243", "sjaelland", "noun", "/ˈʃɛlˌɑːn/", "đảo Zealand (Đan Mạch)"),
    ("087244", "sjambok", "noun", "/ˈʃæmˌbɑːk/", "roi da hà mã hay tê giác Nam Phi"),
    ("087245", "ska", "noun", "/skɑː/", "nhạc ska (tiền thân reggae Jamaica)"),
    ("087246", "skagerak", "noun", "/ˈskæɡəˌræk/", "eo biển Skagerrak (Bắc Âu)"),
    ("087247", "skald", "noun", "/skɔːld/", "thi sĩ ngâm thơ sử thi Bắc Âu cổ"),
    ("087248", "skat", "noun", "/skɑːt/", "trò chơi bài ba người Đức skat"),
    ("087249", "skated", "verb", "/ˈskeɪtɪd/", "đã trượt băng; đã trượt pa-tanh"),
    ("087250", "skates", "verb", "/skeɪts/", "trượt băng; trượt pa-tanh; lướt nhẹ"[:35]),
    ("087251", "skaw", "noun", "/skɔː/", "mũi đất Grenen (cực bắc Đan Mạch)"),
    ("087252", "skean", "noun", "/skiːn/", "dao găm cổ Scotland và Ireland"),
    ("087253", "skedaddled", "verb", "/skɪˈdædəld/", "đã ba chân bốn cẳng chạy trốn"),
    ("087254", "skedaddles", "verb", "/skɪˈdædəlz/", "vội vã tháo chạy; chuồn thẳng"),
    ("087255", "skedaddling", "verb", "/skɪˈdædlɪŋ/", "đang vội vã tháo chạy"),
    ("087256", "skee", "noun", "/skiː/", "ván trượt tuyết"),
    ("087257", "skeletonise", "verb", "/ˈskɛlətəˌnaɪz/", "làm trơ khung xương; rút gọn sườn"),
    ("087258", "skeletonize", "verb", "/ˈskɛlətəˌnaɪz/", "làm trơ khung xương; phác khung"),
    ("087259", "skellum", "noun", "/ˈskɛləm/", "kẻ vô lại lừa đảo (phương ngữ)"),
    ("087260", "skelp", "noun", "/skɛlp/", "cái tát mạnh; cú đánh (Scotland)"),
    ("087261", "skepful", "noun", "/ˈskɛpˌfʊl/", "một giỏ đan đầy"),
    ("087262", "skepsis", "noun", "/ˈskɛpsɪs/", "thuyết hoài nghi; thái độ nghi ngờ"),
    ("087263", "skepticize", "verb", "/ˈskɛptɪˌsaɪz/", "hoài nghi; tỏ ra nghi ngờ"),
    ("087264", "skerry", "noun", "/ˈskɛri/", "đảo đá ngầm nhỏ ngoài khơi"),
    ("087265", "sketched", "verb", "/skɛtʃt/", "đã phác thảo; đã vẽ sơ lược"),
    ("087266", "sketches", "verb", "/ˈskɛtʃɪz/", "phác thảo; vẽ phác họa nhanh"),
    ("087267", "sketching", "verb", "/ˈskɛtʃɪŋ/", "đang phác thảo; đang vẽ phác họa"),
    ("087268", "skewbald", "adj", "/ˈskjuːˌbɔːld/", "lang trắng nâu (lông ngựa)"),
    ("087269", "skewing", "verb", "/ˈskjuːɪŋ/", "đang làm lệch xiên; đang bóp méo"),
    ("087270", "skews", "verb", "/skjuːz/", "làm lệch xiên; bóp méo số liệu"),
    ("087271", "skiagram", "noun", "/ˈskaɪəˌɡræm/", "phim chụp X-quang"),
    ("087272", "skiagraph", "noun", "/ˈskaɪəˌɡræf/", "ảnh chụp tia X; hình chiếu bóng"),
    ("087273", "skiagraphy", "noun", "/skaɪˈɑːɡrəfi/", "kỹ thuật chụp ảnh X-quang"),
    ("087274", "skiascopy", "noun", "/skaɪˈɑːskəpi/", "phép soi bóng đồng tử đo khúc xạ"),
    ("087275", "skibidi", "adj", "/ˈskɪbɪdi/", "tốt hay tệ tùy ngữ cảnh (lóng)"),
    ("087276", "skibob", "noun", "/ˈskaɪˌbɑːb/", "xe trượt tuyết có tay lái ngồi"),
    ("087277", "skidded", "verb", "/ˈskɪdɪd/", "đã trượt bánh; đã trượt ngang"),
    ("087278", "skidding", "verb", "/ˈskɪdɪŋ/", "đang trượt bánh; đang trượt dài"),
    ("087279", "skiddoo", "verb", "/skɪˈduː/", "chuồn đi nhanh; biến mất (lóng)"),
    ("087280", "skidpan", "noun", "/ˈskɪdˌpæn/", "sân trơn tập xử lý xe trượt bánh"),
    ("087281", "skids", "verb", "/skɪdz/", "trượt bánh xe; trượt ngang"),
    ("087282", "skied", "verb", "/skiːd/", "đã trượt tuyết; đã đánh bóng bổng"),
    ("087283", "skies", "noun", "/skaɪz/", "bầu trời; vùng khí hậu"),
    ("087284", "skiffling", "noun", "/ˈskɪflɪŋ/", "kỹ thuật đẽo thô đá xây tường"),
    ("087285", "skijoring", "noun", "/ˈskiːˌdʒɔːrɪŋ/", "môn trượt tuyết có ngựa hoặc chó kéo"[:35]),
    ("087286", "skilless", "adj", "/ˈskɪlləs/", "vụng về; thiếu kỹ năng kinh nghiệm"[:35]),
    ("087287", "skilletfish", "noun", "/ˈskɪlɪtˌfɪʃ/", "cá chảo bám đá nhỏ Gobiesox"),
    ("087288", "skillion", "noun", "/ˈskɪljən/", "mái hiên dốc một mái; nhà phụ"),
    ("087289", "skilly", "noun", "/ˈskɪli/", "cháo yến mạch loãng (nhà tù xưa)"),
    ("087290", "skimboards", "noun", "/ˈskɪmˌbɔːrdz/", "ván lướt sóng nước nông bãi cát"),
    ("087291", "skimcoat", "verb", "/ˈskɪmˌkoʊt/", "trát lớp vữa mỏng làm phẳng tường"),
    ("087292", "skimped", "verb", "/skɪmpt/", "đã tằn tiện keo kiệt; cắt xén"),
    ("087293", "skimpiness", "noun", "/ˈskɪmpinəs/", "sự ít ỏi túng thiếu; tính keo kiệt"),
    ("087294", "skimping", "verb", "/ˈskɪmpɪŋ/", "đang tằn tiện keo kiệt; cắt bớt"),
    ("087295", "skimpingly", "adv", "/ˈskɪmpɪŋli/", "bủn xỉn; keo kiệt thiếu thốn"),
    ("087296", "skimps", "verb", "/skɪmps/", "tằn tiện keo kiệt; làm qua loa"),
    ("087297", "skims", "verb", "/skɪmz/", "hớt váng; đọc lướt; lướt sát mặt"),
    ("087298", "skinners", "noun", "/ˈskɪnərz/", "thợ lột da thú; kẻ buôn da"),
    ("087299", "skinning", "verb", "/ˈskɪnɪŋ/", "đang lột da; đang trầy da"),
    ("087300", "skins", "verb", "/skɪnz/", "lột da; gọt vỏ; làm trầy da"),
    ("087301", "skipants", "noun", "/ˈskiːˌpænts/", "quần chuyên dụng trượt tuyết"),
    ("087302", "skipped", "verb", "/skɪpt/", "đã bỏ qua; đã nhảy chân sáo"),
]

# Remove slices cleanly <= 35 chars
RECORDS[0] = ("087203", "sisterlike", "adj", "/ˈsɪstərˌlaɪk/", "thân thiết như chị em gái")
RECORDS[7] = ("087210", "sites", "verb", "/saɪts/", "đặt vị trí; chọn địa điểm xây")
RECORDS[10] = ("087213", "siting", "verb", "/ˈsaɪtɪŋ/", "đang đặt vị trí; đang chọn chỗ")
RECORDS[11] = ("087214", "sitiology", "noun", "/ˌsɪtiˈɑːlədʒi/", "dinh dưỡng học; khoa thực phẩm")
RECORDS[19] = ("087222", "situating", "verb", "/ˈsɪtʃuˌeɪtɪŋ/", "đang đặt vị trí; xác định chỗ")
RECORDS[27] = ("087230", "sixsome", "noun", "/ˈsɪksəm/", "nhóm sáu người; trận sáu người")
RECORDS[31] = ("087234", "sizarship", "noun", "/ˈsaɪzərˌʃɪp/", "học bổng miễn giảm học phí xưa")
RECORDS[34] = ("087237", "sizes", "verb", "/ˈsaɪzɪz/", "phân loại kích cỡ; hồ vải")
RECORDS[47] = ("087250", "skates", "verb", "/skeɪts/", "trượt băng; trượt pa-tanh")
RECORDS[82] = ("087285", "skijoring", "noun", "/ˈskiːˌdʒɔːrɪŋ/", "trượt tuyết có ngựa hay chó kéo")
RECORDS[83] = ("087286", "skilless", "adj", "/ˈskɪlləs/", "vụng về; thiếu kỹ năng")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r05_raw_p3.json"))
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

json.dump(out, open("scratch/b38_r05_reviewed_p3.json", "w"), ensure_ascii=False, indent=2)
print("b38_r05_p3 saved OK")
