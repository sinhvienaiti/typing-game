import json

RECORDS = [
    ("085603", "scrinium", "noun", "/ˈskrɪniəm/", "hộp đựng cuộn sách thời La Mã"),
    ("085604", "scription", "noun", "/ˈskrɪpʃən/", "lối chữ viết tay; phong cách viết"),
    ("085605", "scriptoria", "noun", "/skrɪpˈtɔːriə/", "phòng chép kinh sách tu viện"),
    ("085606", "scripturalism", "noun", "/ˈskrɪptʃərəˌlɪzəm/", "chủ nghĩa tuân thủ Kinh Thánh"),
    ("085607", "scripturalist", "noun", "/ˈskrɪptʃərəlɪst/", "người tuân thủ chặt Kinh Thánh"),
    ("085608", "scripturist", "noun", "/ˈskrɪptʃərɪst/", "học giả am hiểu Kinh Thánh"),
    ("085609", "scrirrhous", "adj", "/ˈskɪrəs/", "xơ cứng (khối u ung thư)"),
    ("085610", "scrive", "verb", "/skraɪv/", "khắc vạch dấu lên gỗ kim loại"),
    ("085611", "scrivened", "adj", "/ˈskrɪvənd/", "được sao chép tay tỉ mỉ"),
    ("085612", "scrobicula", "noun", "/skrəˈbɪkjələ/", "hốc nhỏ; vết lõm nhỏ"),
    ("085613", "scrobiculat", "adj", "/skrəˈbɪkjəlɪt/", "có nhiều hốc nhỏ; rỗ nhỏ"),
    ("085614", "scrobiculated", "adj", "/skrəˈbɪkjəˌleɪtɪd/", "có nhiều vết lõm nhỏ"),
    ("085615", "scrobicule", "noun", "/ˈskrɑːbɪˌkjuːl/", "hốc nhỏ; vết lõm nhỏ"),
    ("085616", "scrolled", "verb", "/skroʊld/", "đã cuộn trang; đã chạm hoa văn"),
    ("085617", "scrolling", "verb", "/ˈskroʊlɪŋ/", "đang cuộn màn hình; chạm xoắn"),
    ("085618", "scrolls", "verb", "/skroʊlz/", "cuộn trang; cuộn màn hình"),
    ("085619", "scroop", "noun", "/skruːp/", "tiếng sột soạt giòn của vải lụa"),
    ("085620", "scrophularia", "noun", "/ˌskrɑːfjəˈlɛriə/", "chi cây Huyền sâm (Scrophularia)"),
    ("085621", "scrophulariales", "noun", "/ˌskrɑːfjəˌlɛriˈeɪliːz/", "bộ Hoa mõm sói"),
    ("085622", "scrota", "noun", "/ˈskroʊtə/", "bìu dái (giải phẫu)"),
    ("085623", "scrotitis", "noun", "/skroʊˈtaɪtɪs/", "viêm bìu"),
    ("085624", "scrounged", "verb", "/skraʊndʒd/", "đã đi xin xỏ; đã bới tìm đồ"),
    ("085625", "scrounges", "verb", "/ˈskraʊndʒɪz/", "xin xỏ ăn chực; lục tìm đồ"),
    ("085626", "scrounging", "verb", "/ˈskraʊndʒɪŋ/", "đang xin xỏ; đang bới tìm đồ"),
    ("085627", "scrubbiness", "noun", "/ˈskrʌbinəs/", "tình trạng còi cọc; vẻ lôi thôi"),
    ("085628", "scrubbird", "noun", "/ˈskrʌbˌbɜːrd/", "chim bụi rậm Úc"),
    ("085629", "scrubwoman", "noun", "/ˈskrʌbˌwʊmən/", "nữ lao công lau dọn"),
    ("085630", "scrudge", "noun", "/skrʌdʒ/", "cái móc nhỏ giữ ngói lợp mái"),
    ("085631", "scruffily", "adv", "/ˈskrʌfɪli/", "luộm thuộm; nhếch nhác bẩn thỉu"),
    ("085632", "scruffiness", "noun", "/ˈskrʌfinəs/", "vẻ lôi thôi nhếch nhác"),
    ("085633", "scrummed", "verb", "/skrʌmd/", "đã đấu cụm tranh bóng bầu dục"),
    ("085634", "scrumming", "verb", "/ˈskrʌmɪŋ/", "đang đấu cụm tranh bóng bầu dục"),
    ("085635", "scrumptiously", "adv", "/ˈskrʌmpʃəsli/", "ngon tuyệt; tuyệt hảo"),
    ("085636", "scrums", "verb", "/skrʌmz/", "đấu cụm tranh bóng bầu dục"),
    ("085637", "scrupled", "verb", "/ˈskruːpəld/", "đã do dự băn khoăn lương tâm"),
    ("085638", "scrupling", "verb", "/ˈskruːplɪŋ/", "đang do dự băn khoăn lương tâm"),
    ("085639", "scrupulosity", "noun", "/ˌskruːpjəˈlɑːsɪti/", "tính quá cẩn trọng; nỗi áy náy"),
    ("085640", "scrutator", "noun", "/skruːˈteɪtər/", "người giám sát kiểm phiếu"),
    ("085641", "scrutinised", "verb", "/ˈskruːtəˌnaɪzd/", "đã xem xét kỹ lưỡng; soi xét"),
    ("085642", "scrutiniser", "noun", "/ˈskruːtəˌnaɪzər/", "người kiểm tra soi xét kỹ lưỡng"),
    ("085643", "scrutinises", "verb", "/ˈskruːtəˌnaɪzɪz/", "xem xét kỹ lưỡng; soi xét"),
    ("085644", "scrutinising", "verb", "/ˈskruːtəˌnaɪzɪŋ/", "đang xem xét kỹ lưỡng; soi xét"),
    ("085645", "scrutinized", "verb", "/ˈskruːtəˌnaɪzd/", "đã xem xét kỹ lưỡng; soi xét"),
    ("085646", "scrutinizer", "noun", "/ˈskruːtəˌnaɪzər/", "người kiểm tra soi xét kỹ lưỡng"),
    ("085647", "scrutinizes", "verb", "/ˈskruːtəˌnaɪzɪz/", "xem xét kỹ lưỡng; soi xét"),
    ("085648", "scrutinizing", "verb", "/ˈskruːtəˌnaɪzɪŋ/", "đang xem xét kỹ lưỡng; soi xét"),
    ("085649", "scrutinizingly", "adv", "/ˈskruːtəˌnaɪzɪŋli/", "dò xét kỹ lưỡng; soi mói tỉ mỉ"),
    ("085650", "scudded", "verb", "/ˈskʌdɪd/", "đã lướt nhanh; đã bay vút qua"),
    ("085651", "scuds", "verb", "/skʌdz/", "lướt nhanh trên mặt nước hay trời"),
    ("085652", "scuffed", "verb", "/skʌft/", "đã làm trầy xước; lê bước chân"),
    ("085653", "scuffer", "noun", "/ˈskʌfər/", "giày dép xăng-đan đi dạo"),
    ("085654", "scuffing", "verb", "/ˈskʌfɪŋ/", "đang làm trầy xước; đang lê gót"),
    ("085655", "scuffled", "verb", "/ˈskʌfəld/", "đã ẩu đả xô xát nhẹ"),
    ("085656", "scuffles", "noun", "/ˈskʌfəlz/", "cuộc ẩu đả ngắn; vụ xô xát"),
    ("085657", "scuffling", "verb", "/ˈskʌflɪŋ/", "đang ẩu đả xô xát nhẹ"),
    ("085658", "scuffs", "verb", "/skʌfs/", "làm trầy xước; kéo lê bàn chân"),
    ("085659", "scug", "noun", "/skʌɡ/", "kẻ hèn hạ bẩn thỉu; người bị trêu"),
    ("085660", "sculduggery", "noun", "/skʌlˈdʌɡəri/", "trò gian lận; thủ đoạn xảo trá"),
    ("085661", "sculled", "verb", "/skʌld/", "đã chèo thuyền bằng mái chèo đôi"),
    ("085662", "sculls", "verb", "/skʌlz/", "chèo thuyền bằng mái chèo đôi"),
    ("085663", "sculp", "verb", "/skʌlp/", "điêu khắc; chạm trổ"),
    ("085664", "sculpting", "verb", "/ˈskʌlptɪŋ/", "đang điêu khắc; đang tạc tượng"),
    ("085665", "sculptors", "noun", "/ˈskʌlptərz/", "nhà điêu khắc"),
    ("085666", "sculpts", "verb", "/skʌlpts/", "điêu khắc; tạc tượng"),
    ("085667", "sculpturer", "noun", "/ˈskʌlptʃərər/", "nhà điêu khắc"),
    ("085668", "sculptures", "verb", "/ˈskʌlptʃərz/", "điêu khắc; tạc thành tượng"),
    ("085669", "sculpturesque", "adj", "/ˌskʌlptʃəˈrɛsk/", "đẹp cân đối như tượng tạc"),
    ("085670", "sculpturing", "verb", "/ˈskʌlptʃərɪŋ/", "đang điêu khắc; đang tạc tượng"),
    ("085671", "scumble", "noun", "/ˈskʌmbəl/", "lớp màu phủ mờ (hội họa)"),
    ("085672", "scummed", "verb", "/skʌmd/", "đã hớt bọt cặn; nổi váng bọt"),
    ("085673", "scumming", "verb", "/ˈskʌmɪŋ/", "đang hớt bọt cặn; nổi váng bọt"),
    ("085674", "scums", "verb", "/skʌmz/", "hớt bọt cặn; nổi lớp váng bọt"),
    ("085675", "scungy", "adj", "/ˈskʌndʒi/", "dơ dáy; bừa bộn nhếch nhác"),
    ("085676", "scunnered", "adj", "/ˈskʌnərd/", "chán ngấy; ghê tởm (Scotland)"),
    ("085677", "scuppered", "verb", "/ˈskʌpərd/", "đã đánh đắm; đã phá hỏng kế hoạch"),
    ("085678", "scuppering", "verb", "/ˈskʌpərɪŋ/", "đang đánh đắm; đang phá hỏng"),
    ("085679", "scuppers", "verb", "/ˈskʌpərz/", "đánh đắm tàu; làm phá sản dự định"),
    ("085680", "scurfiness", "noun", "/ˈskɜːrfinəs/", "tình trạng nhiều gàu vảy da"),
    ("085681", "scurfing", "noun", "/ˈskɜːrfɪŋ/", "sự bong tróc vảy; việc cạo gàu"),
    ("085682", "scurried", "verb", "/ˈskɜːrid/", "đã chạy vội vã lon ton"),
    ("085683", "scurries", "verb", "/ˈskɜːriz/", "chạy vội vã bước ngắn"),
    ("085684", "scurrile", "adj", "/ˈskɜːrəl/", "thô tục; phỉ báng cay nghiệt"),
    ("085685", "scurrility", "noun", "/skɜːˈrɪlɪti/", "lời lẽ thô tục xúc phạm"),
    ("085686", "scurrilously", "adv", "/ˈskɜːrələsli/", "thô tục; chửi rủa phỉ báng"),
    ("085687", "scurrilousness", "noun", "/ˈskɜːrələsnəs/", "tính chất thô bỉ; lời lẽ xúc phạm"),
    ("085688", "scurvied", "adj", "/ˈskɜːrvid/", "bị bệnh scorbut"),
    ("085689", "scurvily", "adv", "/ˈskɜːrvɪli/", "hèn hạ; đê tiện; bần tiện"),
    ("085690", "scurviness", "noun", "/ˈskɜːrvinəs/", "tính hèn hạ; sự bần tiện"),
    ("085691", "scuta", "noun", "/ˈskjuːtə/", "tấm vảy sừng cứng; tấm khiên"),
    ("085692", "scutage", "noun", "/ˈskjuːtɪdʒ/", "thuế miễn nghĩa vụ quân dịch xưa"),
    ("085693", "scutal", "adj", "/ˈskjuːtəl/", "thuộc tấm vảy sừng; hình khiên"),
    ("085694", "scutate", "adj", "/ˈskjuːteɪt/", "có vảy sừng lớn; hình khiên"),
    ("085695", "scutch", "noun", "/skʌtʃ/", "dao đập tách sợi lanh"),
    ("085696", "scutcheon", "noun", "/ˈskʌtʃən/", "tấm che ổ khóa; gia huy"),
    ("085697", "scutcher", "noun", "/ˈskʌtʃər/", "máy đập xé bông sợi lanh"),
    ("085698", "scutel", "noun", "/ˈskjuːtəl/", "vảy nhỏ hình khiên"),
    ("085699", "scutellate", "adj", "/ˈskjuːtəˌleɪt/", "có vảy nhỏ; hình đĩa cạn"),
    ("085700", "scutellation", "noun", "/ˌskjuːtəˈleɪʃən/", "sự sắp xếp vảy sừng chân chim"),
    ("085701", "scutelliform", "adj", "/skjuːˈtɛlɪˌfɔːrm/", "có hình đĩa tròn hay khiên nhỏ"),
    ("085702", "scutellum", "noun", "/skjuːˈtɛləm/", "lá mầm ngô; vảy hình khiên"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r02_raw_p2.json"))
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

json.dump(out, open("scratch/b38_r02_reviewed_p2.json", "w"), ensure_ascii=False, indent=2)
print("b38_r02_p2 saved OK")
