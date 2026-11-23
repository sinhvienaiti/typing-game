import json

RECORDS = [
    ("087103", "simplist", "noun", "/ˈsɪmplɪst/", "người đơn giản hóa; thầy thuốc cây"),
    ("087104", "simulacra", "noun", "/ˌsɪmjəˈleɪkrə/", "hình ảnh mô phỏng; ảo ảnh giả tạo"),
    ("087105", "simulant", "adj", "/ˈsɪmjələnt/", "giả vờ; bắt chước tương tự"),
    ("087106", "simulates", "verb", "/ˈsɪmjəˌleɪts/", "mô phỏng; giả vờ"),
    ("087107", "simulating", "verb", "/ˈsɪmjəˌleɪtɪŋ/", "đang mô phỏng; đang giả vờ"),
    ("087108", "simulative", "adj", "/ˈsɪmjəˌleɪtɪv/", "có tính mô phỏng; giả tạo"),
    ("087109", "simulcasted", "verb", "/ˈsaɪməlˌkæstɪd/", "đã phát sóng đồng thời đa kênh"),
    ("087110", "simulcasting", "verb", "/ˈsaɪməlˌkæstɪŋ/", "đang phát sóng đồng thời đa kênh"),
    ("087111", "simulcasts", "verb", "/ˈsaɪməlˌkæsts/", "phát sóng đồng thời đa kênh"),
    ("087112", "simuliidae", "noun", "/ˌsɪmjʊˈlaɪɪˌdiː/", "họ Ruồi đen hút máu (Simuliidae)"),
    ("087113", "simultaneousness", "noun", "/ˌsaɪməlˈteɪniəsnəs/", "tính đồng thời; sự xảy ra cùng lúc"[:35]),
    ("087114", "simurg", "noun", "/ˈsiːmʊrɡ/", "chim thần khổng lồ Simurgh (Ba Tư)"[:35]),
    ("087115", "sinanthropus", "noun", "/ˌsaɪnˈænθrəpəs/", "chi Người vượn Bắc Kinh"),
    ("087116", "sinapinates", "noun", "/sɪˈnæpəˌneɪts/", "muối hay este của axit sinapic"),
    ("087117", "sinapism", "noun", "/ˈsɪnəˌpɪzəm/", "cao dán hạt mù tạt giảm đau"),
    ("087118", "since", "adv", "/sɪns/", "từ đó đến nay; trước đây"),
    ("087119", "sincipital", "adj", "/sɪnˈsɪpɪtəl/", "thuộc vùng trán thóp đỉnh đầu"),
    ("087120", "sinciput", "noun", "/ˈsɪnsɪˌpʌt/", "vùng đỉnh trước hộp sọ"),
    ("087121", "sinecurism", "noun", "/ˈsaɪnəˌkjʊrɪzəm/", "tệ trạng hưởng bổng lộc ngồi mát"),
    ("087122", "sinecurist", "noun", "/ˈsaɪnəˌkjʊrɪst/", "người hưởng lương nhàn hạ vô tích"[:35]),
    ("087123", "sinewiness", "noun", "/ˈsɪnjuːinəs/", "vẻ gân guốc rắn rỏi"),
    ("087124", "sinewless", "adj", "/ˈsɪnjuːləs/", "yếu ớt; nhu nhược thiếu sức sống"),
    ("087125", "sinfonia", "noun", "/ˌsɪnfəˈniːə/", "khúc mở đầu; bản giao hưởng nhỏ"),
    ("087126", "sinfonietta", "noun", "/ˌsɪnfəniˈɛtə/", "bản giao hưởng ngắn; dàn nhạc nhỏ"),
    ("087127", "sinfully", "adv", "/ˈsɪnfəli/", "tội lỗi; sai trái đáng trách"),
    ("087128", "singan", "noun", "/siːˈɑːn/", "thành phố Tây An (Trung Quốc)"),
    ("087129", "singed", "verb", "/sɪndʒd/", "đã làm cháy xém; đã thui lông"),
    ("087130", "singeress", "noun", "/ˈsɪŋərəs/", "nữ ca sĩ"),
    ("087131", "singes", "verb", "/ˈsɪndʒɪz/", "làm cháy xém; thui nhẹ lông"),
    ("087132", "singlemindedness", "noun", "/ˌsɪŋɡəlˈmaɪndɪdnəs/", "sự chuyên tâm nhất quán"),
    ("087133", "singlenesses", "noun", "/ˈsɪŋɡəlnəsɪz/", "tình trạng độc thân; lòng chân nhất"[:35]),
    ("087134", "singlestick", "noun", "/ˈsɪŋɡəlˌstɪk/", "môn đấu gậy gỗ bảo hộ tay"),
    ("087135", "singlesticker", "noun", "/ˈsɪŋɡəlˌstɪkər/", "thuyền buồm một cột buồm"),
    ("087136", "sings", "verb", "/sɪŋz/", "ca hát; hót líu lo; reo vang"),
    ("087137", "singularise", "verb", "/ˈsɪŋɡjələˌraɪz/", "chuyển sang số ít; làm nổi bật"),
    ("087138", "singularism", "noun", "/ˈsɪŋɡjələˌrɪzəm/", "thuyết đơn nguyên (triết học)"),
    ("087139", "singularities", "noun", "/ˌsɪŋɡjəˈlærɪtiz/", "điểm kỳ dị; nét kỳ lạ độc đáo"),
    ("087140", "singularize", "verb", "/ˈsɪŋɡjələˌraɪz/", "chuyển sang số ít; làm nổi bật"),
    ("087141", "singultus", "noun", "/sɪŋˈɡʌltəs/", "chứng nấc cụt"),
    ("087142", "sinh", "noun", "/saɪnʃ/", "hàm sin hypebol (toán học)"),
    ("087143", "sinic", "adj", "/ˈsaɪnɪk/", "thuộc Trung Hoa; gốc Hán"),
    ("087144", "sinistrality", "noun", "/ˌsɪnɪˈstrælɪti/", "tính thuận tay trái"),
    ("087145", "sinistrocerebral", "adj", "/ˌsɪnɪstroʊˈsɛrəbrəl/", "thuộc bán cầu đại não trái"),
    ("087146", "sinistrorsal", "adj", "/ˌsɪnɪˈstrɔːrsəl/", "xoắn từ phải sang trái (thực vật)"),
    ("087147", "sinistrorse", "adj", "/ˈsɪnɪˌstrɔːrs/", "xoắn sang trái (dây leo, vỏ ốc)"),
    ("087148", "sinkable", "adj", "/ˈsɪŋkəbəl/", "có thể bị chìm; đánh chìm được"),
    ("087149", "sinkhead", "noun", "/ˈsɪŋkˌhɛd/", "đầu rót bù co (đúc kim loại)"),
    ("087150", "sinned", "verb", "/sɪnd/", "đã phạm tội; đã làm điều tội lỗi"),
    ("087151", "sinnet", "noun", "/ˈsɪnɪt/", "dây thừng bện dẹt; sợi rơm tết"),
    ("087152", "sinningia", "noun", "/sɪˈnɪndʒiə/", "chi hoa tử la lan chuông Sinningia"[:35]),
    ("087153", "sinologue", "noun", "/ˈsaɪnəˌlɔːɡ/", "nhà Hán học"),
    ("087154", "sinoper", "noun", "/ˈsɪnəpər/", "thạch anh đỏ; đất son đỏ"),
    ("087155", "sinophile", "adj", "/ˈsaɪnəˌfaɪl/", "thân Trung Quốc; yêu văn hóa Hoa"),
    ("087156", "sinophilism", "noun", "/saɪˈnɑːfəˌlɪzəm/", "tâm lý thân Trung Quốc"),
    ("087157", "sinopia", "noun", "/sɪˈnoʊpiə/", "bản phác thảo phấn đỏ dưới tranh"),
    ("087158", "sinopis", "noun", "/sɪˈnoʊpɪs/", "đất son đỏ vẽ tranh tường"),
    ("087159", "sinornis", "noun", "/saɪˈnɔːrnɪs/", "chim hóa thạch Trung Hoa Sinornis"),
    ("087160", "sins", "verb", "/sɪnz/", "phạm tội; vi phạm luân lý"),
    ("087161", "sinsyne", "adv", "/ˈsɪnsaɪn/", "kể từ lúc đó (tiếng Scotland)"),
    ("087162", "sinti", "noun", "/ˈsɪnti/", "người Sinti (nhánh người Di-gan)"),
    ("087163", "sinuation", "noun", "/ˌsɪnjuˈeɪʃən/", "chỗ uốn khúc quanh co"),
    ("087164", "sinuatrial", "adj", "/ˌsaɪnjuˈeɪtriəl/", "thuộc nút xoang nhĩ (tim)"),
    ("087165", "sinuousness", "noun", "/ˈsɪnjuəsnəs/", "sự uốn lượn quanh co"),
    ("087166", "siphonage", "noun", "/ˈsaɪfənɪdʒ/", "sự hút chất lỏng bằng ống xi-phông"[:35]),
    ("087167", "siphonal", "adj", "/ˈsaɪfənəl/", "thuộc ống xi-phông"),
    ("087168", "siphoned", "verb", "/ˈsaɪfənd/", "đã rút bằng ống hút; đã bòn rút"),
    ("087169", "siphonic", "adj", "/saɪˈfɑːnɪk/", "thuộc nguyên lý ống xi-phông"),
    ("087170", "siphoning", "verb", "/ˈsaɪfənɪŋ/", "đang rút bằng ống hút; đang bòn rút"[:35]),
    ("087171", "siphonophora", "noun", "/ˌsaɪfəˈnɑːfərə/", "bộ Sứa ống (Siphonophorae)"),
    ("087172", "siphons", "noun", "/ˈsaɪfənz/", "ống xi-phông; vòi hút nhuyễn thể"),
    ("087173", "siphuncle", "noun", "/ˈsaɪfʌŋkəl/", "ống thông buồng vỏ ốc anh vũ"),
    ("087174", "siphunculi", "noun", "/saɪˈfʌŋkjəˌlaɪ/", "ống tiết dịch lưng con rệp cây"),
    ("087175", "sipped", "verb", "/sɪpt/", "đã nhấp từng ngụm nhỏ"),
    ("087176", "sippet", "noun", "/ˈsɪpɪt/", "miếng bánh mì chiên giòn ăn súp"),
    ("087177", "sipping", "verb", "/ˈsɪpɪŋ/", "đang nhấp từng ngụm nhỏ"),
    ("087178", "sips", "verb", "/sɪps/", "nhấp từng ngụm nhỏ"),
    ("087179", "sipuncula", "noun", "/sɪˈpʌŋkjələ/", "ngành Sá sùng (Sipuncula)"),
    ("087180", "sipunculid", "noun", "/sɪˈpʌŋkjəlɪd/", "con sá sùng; giun biển"),
    ("087181", "sircar", "noun", "/ˈsɜːrkɑːr/", "chính quyền Ấn Độ xưa; thư ký"),
    ("087182", "sired", "verb", "/ˈsaɪərd/", "đã sinh ra (thú đực); đã sáng lập"),
    ("087183", "siree", "noun", "/səˈriː/", "thưa ngài (dùng để nhấn mạnh)"),
    ("087184", "sirenian", "noun", "/saɪˈriːniən/", "thú biển bộ Bò biển (cá cúi)"),
    ("087185", "sirenidae", "noun", "/saɪˈrɛnɪˌdiː/", "họ Kỳ giông lươn (Sirenidae)"),
    ("087186", "sires", "verb", "/ˈsaɪərz/", "làm giống đực sinh con; đẻ ra"),
    ("087187", "sirgang", "noun", "/ˈsɜːrˌɡæŋ/", "chim chèo bẻo xanh (Ấn Độ)"),
    ("087188", "siriasis", "noun", "/sɪˈraɪəsɪs/", "chứng say nắng; cảm nắng nặng"),
    ("087189", "siring", "verb", "/ˈsaɪərɪŋ/", "đang phối giống đực; đang tạo ra"),
    ("087190", "sirkar", "noun", "/ˈsɜːrkɑːr/", "chính quyền Ấn Độ xưa; quản lý"),
    ("087191", "sirloins", "noun", "/ˈsɜːrˌlɔɪnz/", "thăn ngoại bò"),
    ("087192", "sirred", "verb", "/sɜːrd/", "đã gọi là ngài; đã xưng thưa ông"),
    ("087193", "sirree", "noun", "/səˈriː/", "thưa ngài (dùng để nhấn mạnh)"),
    ("087194", "sirring", "verb", "/ˈsɜːrɪŋ/", "đang gọi là ngài; xưng thưa ông"),
    ("087195", "sirs", "verb", "/sɜːrz/", "gọi là ngài; xưng hô thưa ông"),
    ("087196", "sirupy", "adj", "/ˈsɪrəpi/", "sánh ngọt như xi-rô; ngọt sến"),
    ("087197", "sisham", "noun", "/ˈʃiːʃəm/", "cây trắc Ấn Độ lấy gỗ quý"),
    ("087198", "sissiness", "noun", "/ˈsɪsinəs/", "tính yếu đuối ẻo lả (hàm ý chê)"),
    ("087199", "sissoo", "noun", "/ˈsɪsuː/", "cây trắc Ấn Độ Dalbergia sissoo"),
    ("087200", "sissu", "noun", "/ˈsɪsuː/", "cây trắc Ấn Độ lấy gỗ quý"),
    ("087201", "sissyish", "adj", "/ˈsɪsiɪʃ/", "nhút nhát yếu đuối; ủy mị"),
    ("087202", "sisterless", "adj", "/ˈsɪstərləs/", "không có chị em gái"),
]

# Remove slices cleanly <= 35 chars
RECORDS[10] = ("087113", "simultaneousness", "noun", "/ˌsaɪməlˈteɪniəsnəs/", "tính đồng thời; việc xảy cùng lúc")
RECORDS[11] = ("087114", "simurg", "noun", "/ˈsiːmʊrɡ/", "chim thần khổng lồ Ba Tư Simurgh")
RECORDS[19] = ("087122", "sinecurist", "noun", "/ˈsaɪnəˌkjʊrɪst/", "người hưởng lương nhàn hạ ăn không")
RECORDS[30] = ("087133", "singlenesses", "noun", "/ˈsɪŋɡəlnəsɪz/", "tình trạng độc thân; lòng son sắt")
RECORDS[49] = ("087152", "sinningia", "noun", "/sɪˈnɪndʒiə/", "chi hoa tử la lan chuông")
RECORDS[63] = ("087166", "siphonage", "noun", "/ˈsaɪfənɪdʒ/", "sự hút chất lỏng bằng xi-phông")
RECORDS[67] = ("087170", "siphoning", "verb", "/ˈsaɪfənɪŋ/", "đang hút bằng ống; đang bòn rút")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r05_raw_p2.json"))
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

json.dump(out, open("scratch/b38_r05_reviewed_p2.json", "w"), ensure_ascii=False, indent=2)
print("b38_r05_p2 saved OK")
