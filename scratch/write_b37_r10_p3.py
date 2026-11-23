import json

RECORDS = [
    ("084703", "samlet", "noun", "/ˈsæmlət/", "cá hồi con"),
    ("084704", "sammy", "noun", "/ˈsæmi/", "lính Mỹ (biệt danh Thế chiến I)"),
    ("084705", "samolus", "noun", "/ˈsæmələs/", "chi rau má đầm lầy Samolus"),
    ("084706", "samoyede", "noun", "/səˈmɔɪˌɛd/", "chó tuyết Samoyed; người Samoyed"),
    ("084707", "samoyedic", "noun", "/ˌsæmɔɪˈɛdɪk/", "nhóm ngôn ngữ Samoyed"),
    ("084708", "sampled", "verb", "/ˈsæmpəld/", "đã lấy mẫu; đã nếm thử"),
    ("084709", "samples", "verb", "/ˈsæmpəlz/", "lấy mẫu; nếm thử"),
    ("084710", "sampson", "noun", "/ˈsæmpsən/", "Samson; người khỏe phi thường"),
    ("084711", "samriddhi", "noun", "/səmˈrɪdhi/", "tên riêng nữ Ấn Độ Samriddhi"),
    ("084712", "sanatarium", "noun", "/ˌsænəˈtɛriəm/", "viện điều dưỡng; trại an dưỡng"),
    ("084713", "sanative", "adj", "/ˈsænətɪv/", "chữa lành; có tác dụng trị bệnh"),
    ("084714", "sanatoria", "noun", "/ˌsænəˈtɔːriə/", "viện điều dưỡng; nhà an dưỡng"),
    ("084715", "sanctifier", "noun", "/ˈsæŋktɪˌfaɪər/", "đấng thánh hóa; Chúa Thánh Thần"),
    ("084716", "sanctifies", "verb", "/ˈsæŋktɪˌfaɪz/", "thánh hóa; ban phép lành"),
    ("084717", "sanctifying", "verb", "/ˈsæŋktɪˌfaɪɪŋ/", "đang thánh hóa; đang ban phép"),
    ("084718", "sanctionative", "adj", "/ˈsæŋkʃəˌneɪtɪv/", "phê chuẩn; cho phép"),
    ("084719", "sanctions", "verb", "/ˈsæŋkʃənz/", "phê chuẩn; trừng phạt kinh tế"),
    ("084720", "sanctitude", "noun", "/ˈsæŋktɪˌtuːd/", "sự thánh thiện; vẻ tôn nghiêm"),
    ("084721", "sandaled", "adj", "/ˈsændəld/", "mang dép xăng-đan"),
    ("084722", "sandalled", "adj", "/ˈsændəld/", "mang dép xăng-đan"),
    ("084723", "sandarac", "noun", "/ˈsændəˌræk/", "nhựa thơm sandarac dùng làm sơn"),
    ("084724", "sandarach", "noun", "/ˈsændəˌræk/", "nhựa thơm sandarac; thạch hùng"),
    ("084725", "sandbagged", "verb", "/ˈsændˌbæɡd/", "đã đắp bao cát; đã đánh lừa"),
    ("084726", "sandbagger", "noun", "/ˈsændˌbæɡər/", "kẻ giả vờ yếu để lừa đối thủ"),
    ("084727", "sandbagging", "verb", "/ˈsændˌbæɡɪŋ/", "đang đắp bao cát; đang giấu bài"),
    ("084728", "sandbags", "verb", "/ˈsændˌbæɡz/", "đắp bao cát; giấu tài đánh lừa"),
    ("084729", "sandberry", "noun", "/ˈsændˌbɛri/", "cây bụi quả mọng vùng cát"),
    ("084730", "sandboy", "noun", "/ˈsændˌbɔɪ/", "cậu bé bán cát rải sàn xưa"),
    ("084731", "sandbur", "noun", "/ˈsændˌbɜːr/", "cỏ gai mọc đất cát"),
    ("084732", "sandcastle", "noun", "/ˈsændˌkæsəl/", "lâu đài cát"),
    ("084733", "sandcastler", "noun", "/ˈsændˌkæslər/", "người xây lâu đài cát"),
    ("084734", "sandcastles", "noun", "/ˈsændˌkæsəlz/", "lâu đài cát"),
    ("084735", "sanded", "verb", "/ˈsændɪd/", "đã chà nhám; đã rải cát"),
    ("084736", "sanders", "noun", "/ˈsændərz/", "máy chà nhám; gỗ đàn hương đỏ"),
    ("084737", "sandfilling", "noun", "/ˈsændˌfɪlɪŋ/", "sự chèn lấp bằng cát"),
    ("084738", "sandfish", "noun", "/ˈsændˌfɪʃ/", "cá cát; thằn lằn cát"),
    ("084739", "sandhog", "noun", "/ˈsændˌhɔːɡ/", "công nhân đào đường hầm dưới nước"),
    ("084740", "sandhopper", "noun", "/ˈsændˌhɑːpər/", "con rận biển nhảy trên bãi cát"),
    ("084741", "sandhurst", "noun", "/ˈsændˌhɜːrst/", "Học viện Quân sự Hoàng gia Anh"),
    ("084742", "sandiness", "noun", "/ˈsændinəs/", "tính nhiều cát; màu vàng cát"),
    ("084743", "sanding", "verb", "/ˈsændɪŋ/", "đang chà nhám; đang rải cát"),
    ("084744", "sandiver", "noun", "/ˈsændɪvər/", "xỉ nổi trên mặt thủy tinh nóng chảy"[:35]),
    ("084745", "sandlike", "adj", "/ˈsændˌlaɪk/", "giống như cát; có hạt như cát"),
    ("084746", "sandnigger", "noun", "/ˈsændˌnɪɡər/", "từ miệt thị chủng tộc (không dùng)"),
    ("084747", "sandniggers", "noun", "/ˈsændˌnɪɡərz/", "từ miệt thị chủng tộc (không dùng)"),
    ("084748", "sandomierz", "noun", "/sænˈdɔːmjɛʃ/", "thị trấn Sandomierz (Ba Lan)"),
    ("084749", "sandpapered", "verb", "/ˈsændˌpeɪpərd/", "đã đánh giấy nhám"),
    ("084750", "sandpapering", "verb", "/ˈsændˌpeɪpərɪŋ/", "đang đánh giấy nhám"),
    ("084751", "sandpapers", "verb", "/ˈsændˌpeɪpərz/", "đánh giấy nhám"),
    ("084752", "sandpapery", "adj", "/ˈsændˌpeɪpəri/", "nhám như giấy ráp; khàn khàn"),
    ("084753", "sandpile", "noun", "/ˈsændˌpaɪl/", "đống cát; bài toán đống cát"),
    ("084754", "sandril", "noun", "/ˈsændrɪl/", "thuốc hạ huyết áp Sandril"),
    ("084755", "sandspur", "noun", "/ˈsændˌspɜːr/", "cỏ gai mọc đất cát"),
    ("084756", "sandstones", "noun", "/ˈsændˌstoʊnz/", "đá sa thạch"),
    ("084757", "sandstorms", "noun", "/ˈsændˌstɔːrmz/", "bão cát"),
    ("084758", "sandwiched", "verb", "/ˈsændwɪtʃt/", "đã kẹp vào giữa"),
    ("084759", "sandwiches", "verb", "/ˈsændwɪtʃɪz/", "kẹp vào giữa"),
    ("084760", "sandwiching", "verb", "/ˈsændwɪtʃɪŋ/", "đang kẹp vào giữa"),
    ("084761", "sandwichman", "noun", "/ˈsændwɪtʃˌmæn/", "người đeo biển quảng cáo hai mặt"),
    ("084762", "sandwort", "noun", "/ˈsændˌwɜːrt/", "cây cỏ mọc đất cát (chi Arenaria)"[:35]),
    ("084763", "saneness", "noun", "/ˈseɪnnəs/", "sự tỉnh táo; đầu óc minh mẫn"),
    ("084764", "sanfoin", "noun", "/ˈseɪnˌfɔɪn/", "cây đậu hồng sainfoin"),
    ("084765", "sanforize", "verb", "/ˈsænfəˌraɪz/", "xử lý vải chống co rút"),
    ("084766", "sanforized", "adj", "/ˈsænfəˌraɪzd/", "đã xử lý chống co rút (vải)"),
    ("084767", "sanga", "noun", "/ˈsæŋɡə/", "bò lai sanga châu Phi; công sự đá"),
    ("084768", "sangapenum", "noun", "/ˌsæŋɡəˈpiːnəm/", "nhựa cây thảo dược sagapenum"),
    ("084769", "sangar", "noun", "/ˈsæŋɡɑːr/", "công sự phòng thủ xếp bằng đá"),
    ("084770", "sangaree", "noun", "/ˌsæŋɡəˈriː/", "rượu vang pha cam chanh và đá"),
    ("084771", "sangfroid", "noun", "/ˌsɑːnˈfrwɑː/", "sự bình tĩnh; bản lĩnh điềm tĩnh"),
    ("084772", "sangha", "noun", "/ˈsʌŋɡə/", "Tăng đoàn Phật giáo"),
    ("084773", "sangos", "noun", "/ˈsæŋɡoʊz/", "tiếng Sango; người Sango"),
    ("084774", "sangraal", "noun", "/ˌsænˈɡreɪl/", "Chén Thánh"),
    ("084775", "sanguicolous", "adj", "/sæŋˈɡwɪkələs/", "ký sinh sống trong máu"),
    ("084776", "sanguiferous", "adj", "/sæŋˈɡwɪfərəs/", "dẫn máu; chứa máu"),
    ("084777", "sanguification", "noun", "/ˌsæŋɡwɪfɪˈkeɪʃən/", "quá trình tạo máu"),
    ("084778", "sanguinariness", "noun", "/ˈsæŋɡwɪˌnɛrinəs/", "tính khát máu; sự đẫm máu"),
    ("084779", "sanguined", "verb", "/ˈsæŋɡwɪnd/", "đã nhuộm màu đỏ máu"),
    ("084780", "sanguinely", "adv", "/ˈsæŋɡwɪnli/", "đầy lạc quan; tràn đầy hy vọng"),
    ("084781", "sanguineness", "noun", "/ˈsæŋɡwɪnnəs/", "tính lạc quan; niềm tin tươi sáng"),
    ("084782", "sanguineous", "adj", "/sæŋˈɡwɪniəs/", "thuộc máu; đỏ như máu; lạc quan"),
    ("084783", "sanguines", "verb", "/ˈsæŋɡwɪnz/", "nhuộm đỏ như máu"),
    ("084784", "sanguining", "verb", "/ˈsæŋɡwɪnɪŋ/", "đang nhuộm đỏ như máu"),
    ("084785", "sanguinity", "noun", "/sæŋˈɡwɪnɪti/", "tính lạc quan; vẻ hồng hào"),
    ("084786", "sanguinivorous", "adj", "/ˌsæŋɡwɪˈnɪvərəs/", "hút máu; sống bằng máu"),
    ("084787", "sanguinolent", "adj", "/sæŋˈɡwɪnələnt/", "có lẫn máu; nhuốm máu"),
    ("084788", "sanguis", "noun", "/ˈsæŋɡwɪs/", "máu (thuật ngữ Latinh)"),
    ("084789", "sanguivorous", "adj", "/sæŋˈɡwɪvərəs/", "ăn máu; hút máu (dơi, đỉa)"),
    ("084790", "sanhedrim", "noun", "/sænˈhiːdrəm/", "Tòa công luận Do Thái tối cao"),
    ("084791", "sanhedrins", "noun", "/sænˈhiːdrənz/", "Tòa công luận Do Thái tối cao"),
    ("084792", "sanicle", "noun", "/ˈsænɪkəl/", "cây hoa tán thuốc Sanicula"),
    ("084793", "sanicula", "noun", "/səˈnɪkjələ/", "chi cây sanicle (họ Hoa tán)"),
    ("084794", "sanies", "noun", "/ˈseɪniˌiːz/", "dịch mủ loãng lẫn máu"),
    ("084795", "sanify", "verb", "/ˈsænɪˌfaɪ/", "làm hợp vệ sinh; cải thiện vệ sinh"[:35]),
    ("084796", "sanious", "adj", "/ˈseɪniəs/", "có dịch mủ loãng lẫn máu"),
    ("084797", "sanitaria", "noun", "/ˌsænɪˈtɛriə/", "viện điều dưỡng"),
    ("084798", "sanitarian", "noun", "/ˌsænɪˈtɛriən/", "chuyên gia y tế vệ sinh"),
    ("084799", "sanitarians", "noun", "/ˌsænɪˈtɛriənz/", "chuyên gia y tế vệ sinh"),
    ("084800", "sanitariness", "noun", "/ˈsænɪˌtɛrinəs/", "tình trạng sạch sẽ hợp vệ sinh"),
    ("084801", "sanitate", "verb", "/ˈsænɪˌteɪt/", "lắp đặt hệ thống vệ sinh"),
    ("084802", "sanitises", "verb", "/ˈsænɪˌtaɪzɪz/", "khử trùng; sát khuẩn; làm sạch"),
]

# Clean 084744, 084762, 084795 cleanly without slices
RECORDS[41] = ("084744", "sandiver", "noun", "/ˈsændɪvər/", "bọt xỉ thủy tinh nóng chảy")
RECORDS[59] = ("084762", "sandwort", "noun", "/ˈsændˌwɜːrt/", "cây cỏ cát chi Arenaria")
RECORDS[92] = ("084795", "sanify", "verb", "/ˈsænɪˌfaɪ/", "cải thiện vệ sinh; làm sạch sẽ")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r10_raw_p3.json"))
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

json.dump(out, open("scratch/b37_r10_reviewed_p3.json", "w"), ensure_ascii=False, indent=2)
print("b37_r10_p3 saved OK")
