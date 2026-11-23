import json

RECORDS = [
    ("085703", "scutiferous", "adj", "/skjuːˈtɪfərəs/", "mang khiên; có tấm vảy cứng"),
    ("085704", "scutiform", "adj", "/ˈskjuːtɪˌfɔːrm/", "có hình cái khiên"),
    ("085705", "scutigera", "noun", "/skjuːˈtɪdʒərə/", "chi Rết nhà chân dài (Scutigera)"),
    ("085706", "scutigerella", "noun", "/ˌskjuːtɪdʒəˈrɛlə/", "chi trùng khớp chân rết vườn"),
    ("085707", "scutigeridae", "noun", "/ˌskjuːtɪˈdʒɛrɪˌdiː/", "họ Rết nhà (Scutigeridae)"),
    ("085708", "scutiped", "adj", "/ˈskjuːtɪˌpɛd/", "có bàn chân phủ vảy sừng"),
    ("085709", "scutter", "noun", "/ˈskʌtər/", "tiếng chạy lon ton vội vã"),
    ("085710", "scuttled", "verb", "/ˈskʌtəld/", "đã đánh đắm tàu; đã chạy vội"),
    ("085711", "scuttles", "verb", "/ˈskʌtəlz/", "đánh đắm tàu; chạy lon ton vội vã"),
    ("085712", "scuttling", "verb", "/ˈskʌtlɪŋ/", "đang đánh đắm; đang chạy vội vã"),
    ("085713", "scutum", "noun", "/ˈskjuːtəm/", "khiên lớn La Mã; vảy sừng bò sát"),
    ("085714", "scyliorhinidae", "noun", "/ˌsɪliəˈrɪnɪˌdiː/", "họ Cá nhám mèo (Scyliorhinidae)"),
    ("085715", "scyphiferous", "adj", "/saɪˈfɪfərəs/", "mang chén bào tử (địa y)"),
    ("085716", "scyphiform", "adj", "/ˈsaɪfɪˌfɔːrm/", "có hình chén uống rượu"),
    ("085717", "scyphistoma", "noun", "/saɪˈfɪstəmə/", "thể polyp sứa dạng chén"),
    ("085718", "scyphoid", "adj", "/ˈsaɪfɔɪd/", "có hình chén"),
    ("085719", "scyphozoan", "noun", "/ˌsaɪfəˈzoʊən/", "sứa thật thuộc lớp Scyphozoa"),
    ("085720", "scyphus", "noun", "/ˈsaɪfəs/", "chén rượu hai quai Hy Lạp cổ"),
    ("085721", "scythed", "verb", "/saɪðd/", "đã cắt bằng lưỡi hái; đã hạ gục"),
    ("085722", "scythefish", "noun", "/ˈsaɪðˌfɪʃ/", "cá hố bạc thân dẹt dài"),
    ("085723", "scythes", "verb", "/saɪðz/", "cắt bằng lưỡi hái"),
    ("085724", "scything", "verb", "/ˈsaɪðɪŋ/", "đang cắt bằng lưỡi hái"),
    ("085725", "sdi", "noun", "/ˌɛsˌdiːˈaɪ/", "Sáng kiến Phòng thủ Chiến lược"),
    ("085726", "sdk", "noun", "/ˌɛsˌdiːˈkeɪ/", "bộ công cụ phát triển phần mềm"),
    ("085727", "sdks", "noun", "/ˌɛsˌdiːˈkeɪz/", "bộ công cụ phát triển phần mềm"),
    ("085728", "sdlp", "noun", "/ˌɛsˌdiːˌɛlˈpiː/", "Đảng Lao động Xã hội Dân chủ"),
    ("085729", "sdp", "noun", "/ˌɛsˌdiːˈpiː/", "Đảng Dân chủ Xã hội"),
    ("085730", "seabag", "noun", "/ˈsiːˌbæɡ/", "túi vải đựng đồ của thủy thủ"),
    ("085731", "seadrome", "noun", "/ˈsiːˌdroʊm/", "sân bay nổi trên mặt biển"),
    ("085732", "seafowl", "noun", "/ˈsiːˌfaʊl/", "chim biển"),
    ("085733", "seagirt", "adj", "/ˈsiːˌɡɜːrt/", "được biển cả bao bọc xung quanh"),
    ("085734", "seahorses", "noun", "/ˈsiːˌhɔːrsɪz/", "cá ngựa; hải mã"),
    ("085735", "sealers", "noun", "/ˈsiːlərz/", "thợ săn hải cẩu; máy hàn miệng túi"),
    ("085736", "sealery", "noun", "/ˈsiːləri/", "nghề săn hải cẩu; bãi hải cẩu"),
    ("085737", "seals", "verb", "/siːlz/", "niêm phong; đóng dấu; bịt kín"),
    ("085738", "sealyham", "noun", "/ˈsiːlihæm/", "giống chó sục Sealyham (xứ Wales)"),
    ("085739", "seamanlike", "adj", "/ˈsiːmənˌlaɪk/", "thạo nghề đi biển; đúng thủy thủ"),
    ("085740", "seamanly", "adj", "/ˈsiːmənli/", "giỏi nghề biển; ra dáng thủy thủ"),
    ("085741", "seamer", "noun", "/ˈsiːmər/", "máy viền mép; máy ghép mí lon"),
    ("085742", "seaming", "verb", "/ˈsiːmɪŋ/", "đang may đường nối; đang ghép mí"),
    ("085743", "seams", "verb", "/siːmz/", "may nối; ghép mí; làm nứt rạn"),
    ("085744", "sean", "noun", "/ʃɔːn/", "tên riêng nam Sean"),
    ("085745", "seaquake", "noun", "/ˈsiːˌkweɪk/", "động đất dưới đáy biển"),
    ("085746", "searched", "verb", "/sɜːrtʃt/", "đã tìm kiếm; đã khám xét"),
    ("085747", "searches", "verb", "/ˈsɜːrtʃɪz/", "tìm kiếm; khám xét"),
    ("085748", "searchless", "adj", "/ˈsɜːrtʃləs/", "không thể dò xét thấu; vô biên"),
    ("085749", "searobin", "noun", "/ˈsiːˌrɑːbɪn/", "cá chào mào biển (họ Triglidae)"),
    ("085750", "sears", "verb", "/sɪrz/", "áp chảo cháy cạnh; thiêu đốt"),
    ("085751", "seaslug", "noun", "/ˈsiːˌslʌɡ/", "sên biển (hải tiêu, hải sâm)"),
    ("085752", "seasnail", "noun", "/ˈsiːˌsneɪl/", "ốc biển; cá nòng nọc biển"),
    ("085753", "seasonableness", "noun", "/ˈsiːzənəbəlnəs/", "tính đúng mùa; sự hợp thời"),
    ("085754", "seasoner", "noun", "/ˈsiːzənər/", "người nêm gia vị; gia vị tẩm ướp"),
    ("085755", "seasons", "verb", "/ˈsiːzənz/", "nêm gia vị; phơi sấy gỗ; tôi luyện"),
    ("085756", "seato", "noun", "/ˈsiːtoʊ/", "Tổ chức Hiệp ước Đông Nam Á"),
    ("085757", "seaweedy", "adj", "/ˈsiːˌwiːdi/", "nhiều rong biển; giống rong biển"),
    ("085758", "sebastiana", "noun", "/sɪˌbæstiˈænə/", "chi cây hạt nhảy Sebastiana"),
    ("085759", "sebastodes", "noun", "/ˌsɛbəˈstoʊdiːz/", "chi cá đá Thái Bình Dương"),
    ("085760", "sebestan", "noun", "/sɪˈbɛstən/", "cây cùm rụm; quả cùm rụm"),
    ("085761", "sebiferous", "adj", "/sɪˈbɪfərəs/", "tiết chất nhờn; sinh sáp thực vật"),
    ("085762", "sebific", "adj", "/sɪˈbɪfɪk/", "tiết chất béo hay sáp"),
    ("085763", "sebiparous", "adj", "/sɪˈbɪpərəs/", "tiết bã nhờn"),
    ("085764", "secateur", "noun", "/ˈsɛkəˌtɜːr/", "kéo cắt tỉa cành cây"),
    ("085765", "seccotine", "noun", "/ˈsɛkəˌtiːn/", "keo dán lỏng gốc cá seccotine"),
    ("085766", "seceded", "verb", "/sɪˈsiːdɪd/", "đã ly khai; đã tách khỏi liên bang"),
    ("085767", "seceder", "noun", "/sɪˈsiːdər/", "người chủ trương ly khai"),
    ("085768", "secedes", "verb", "/sɪˈsiːdz/", "ly khai; rút khỏi tổ chức"),
    ("085769", "seceding", "verb", "/sɪˈsiːdɪŋ/", "đang ly khai; đang tách khỏi"),
    ("085770", "secern", "verb", "/sɪˈsɜːrn/", "phân biệt rạch ròi; bài tiết"),
    ("085771", "secernate", "verb", "/sɪˈsɜːrneɪt/", "tách biệt rõ; tiết dịch"),
    ("085772", "secernent", "adj", "/sɪˈsɜːrnənt/", "thuộc bài tiết; tiết dịch"),
    ("085773", "secernment", "noun", "/sɪˈsɜːrnmənt/", "sự bài tiết; sự phân tách"),
    ("085774", "sechuana", "noun", "/sɛtˈʃwɑːnə/", "tiếng Tswana (Nam Phi)"),
    ("085775", "secludes", "verb", "/sɪˈkluːdz/", "cách ly; tách biệt khỏi xã hội"),
    ("085776", "secluding", "verb", "/sɪˈkluːdɪŋ/", "đang cách ly; đang ẩn dật"),
    ("085777", "seclusionist", "noun", "/sɪˈkluːʒənɪst/", "người chủ trương biệt lập ẩn dật"),
    ("085778", "seclusions", "noun", "/sɪˈkluːʒənz/", "sự ẩn dật; nơi hẻo lánh tách biệt"),
    ("085779", "seclusive", "adj", "/sɪˈkluːsɪv/", "thích ẩn dật; tách biệt hẻo lánh"),
    ("085780", "seconde", "noun", "/sɛˈkɑːnd/", "thế đỡ gạt hạ trong đấu kiếm"),
    ("085781", "seconded", "verb", "/ˈsɛkəndɪd/", "đã biệt phái; đã tán thành đề nghị"),
    ("085782", "seconding", "verb", "/ˈsɛkəndɪŋ/", "đang biệt phái; đang tán thành"),
    ("085783", "seconds", "verb", "/ˈsɛkəndz/", "tán thành đề nghị; điều động tạm"),
    ("085784", "secotiaceae", "noun", "/sɪˌkoʊtiˈeɪsiːˌiː/", "họ Nấm Secotiaceae"),
    ("085785", "secotiales", "noun", "/sɪˌkoʊtiˈeɪliːz/", "bộ Nấm Secotiales"),
    ("085786", "secpar", "noun", "/ˈsɛkpɑːr/", "đơn vị khoảng cách parsec"),
    ("085787", "secreta", "noun", "/sɪˈkriːtə/", "chất tiết; sản phẩm bài tiết"),
    ("085788", "secretagogue", "noun", "/sɪˈkriːtəˌɡɑːɡ/", "chất kích thích bài tiết"),
    ("085789", "secretaria", "noun", "/ˌsɛkrəˈtɛriə/", "ban thư ký; văn phòng bí thư"),
    ("085790", "secretariate", "noun", "/ˌsɛkrəˈtɛriət/", "ban thư ký; nha thư ký"),
    ("085791", "secreted", "verb", "/sɪˈkriːtɪd/", "đã tiết ra; đã cất giấu kín"),
    ("085792", "secreter", "noun", "/sɪˈkriːtər/", "cơ quan bài tiết; người giấu"),
    ("085793", "secretes", "verb", "/sɪˈkriːts/", "tiết ra; cất giấu kín"),
    ("085794", "secreting", "verb", "/sɪˈkriːtɪŋ/", "đang tiết ra; đang cất giấu"),
    ("085795", "secrets", "noun", "/ˈsiːkrɪts/", "bí mật; điều thầm kín"),
    ("085796", "sectarianise", "verb", "/sɛkˈtɛriəˌnaɪz/", "chia rẽ thành phe phái giáo phái"),
    ("085797", "sectarianize", "verb", "/sɛkˈtɛriəˌnaɪz/", "chia rẽ thành phe phái giáo phái"),
    ("085798", "sectarist", "noun", "/ˈsɛktərɪst/", "người theo bè phái; người cuồng tín"),
    ("085799", "sectile", "adj", "/ˈsɛktəl/", "có thể cắt lát bằng dao (khoáng)"),
    ("085800", "sectility", "noun", "/sɛkˈtɪlɪti/", "tính cắt gọt được bằng dao"),
    ("085801", "sectionalisation", "noun", "/ˌsɛkʃənəlaɪˈzeɪʃən/", "sự phân chia khu vực; tính cục bộ"),
    ("085802", "sectionalise", "verb", "/ˈsɛkʃənəˌlaɪz/", "phân chia thành khu vực"),
]

# Shorten 085735, 085737, 085765 cleanly <= 35
RECORDS[32] = ("085735", "sealers", "noun", "/ˈsiːlərz/", "thợ săn hải cẩu; máy hàn túi")
RECORDS[95] = ("085798", "sectarist", "noun", "/ˈsɛktərɪst/", "người theo bè phái; tín đồ phái")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r02_raw_p3.json"))
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

json.dump(out, open("scratch/b38_r02_reviewed_p3.json", "w"), ensure_ascii=False, indent=2)
print("b38_r02_p3 saved OK")
