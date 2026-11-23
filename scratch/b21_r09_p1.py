import json

# Manual word-by-word cognitive review for Batch 21 Round 9 Part 1 (records 4000-4099, IDs 200k.004002 to 200k.004101)
reviewed_entries = [
    # 4000: ohs
    {"ipa": "/oʊz/", "vi": "tiếng thốt than ôi; những chữ Oh", "pos": "noun"},
    # 4001: ts
    {"ipa": "/tiːz/", "vi": "những chữ cái T; áo phông chữ T", "pos": "noun"},
    # 4002: videos
    {"ipa": "/ˈvɪdioʊz/", "vi": "các đoạn video; băng hình video", "pos": "noun"},
    # 4003: youngest
    {"ipa": "/ˈjʌŋɡɪst/", "vi": "trẻ tuổi nhất; nhỏ tuổi nhất", "pos": "adj"},
    # 4004: account statement
    {"ipa": "/əˈkaʊnt ˈsteɪtmənt/", "vi": "sao kê tài khoản; bản kê giao dịch", "pos": "phrase"},
    # 4005: air plant
    {"ipa": "/ɛr plænt/", "vi": "cây không khí; thực vật biểu sinh", "pos": "phrase"},
    # 4006: asking price
    {"ipa": "/ˈæskɪŋ praɪs/", "vi": "giá chào bán; giá người bán đưa ra", "pos": "phrase"},
    # 4007: bed cover
    {"ipa": "/bɛd ˈkʌvər/", "vi": "khăn phủ giường; tấm trải giường", "pos": "phrase"},
    # 4008: black economy
    {"ipa": "/blæk ɪˈkɑːnəmi/", "vi": "kinh tế ngầm; thị trường chợ đen", "pos": "phrase"},
    # 4009: built in bed
    {"ipa": "/ˌbɪlt ɪn bɛd/", "vi": "giường đóng liền tường; giường âm", "pos": "phrase"},
    # 4010: civil list
    {"ipa": "/ˈsɪvl lɪst/", "vi": "ngân sách chi tiêu hoàng gia Anh", "pos": "phrase"},
    # 4011: commercial art
    {"ipa": "/kəˈmɜːrʃl ɑːrt/", "vi": "mỹ thuật thương mại; vẽ quảng cáo", "pos": "phrase"},
    # 4012: committee meeting
    {"ipa": "/kəˈmɪti ˈmiːtɪŋ/", "vi": "cuộc họp ủy ban; phiên họp hội đồng", "pos": "phrase"},
    # 4013: cover version
    {"ipa": "/ˈkʌvər ˈvɜːrʒən/", "vi": "bản thu âm lại; bài hát cover", "pos": "phrase"},
    # 4014: decision table
    {"ipa": "/dɪˈsɪʒən ˈteɪbl/", "vi": "bảng quyết định logic điều kiện", "pos": "phrase"},
    # 4015: defense program
    {"ipa": "/dɪˈfɛns ˈproʊɡræm/", "vi": "chương trình quốc phòng quân sự", "pos": "phrase"},
    # 4016: degree program
    {"ipa": "/dɪˈɡriː ˈproʊɡræm/", "vi": "chương trình đào tạo cấp văn bằng", "pos": "phrase"},
    # 4017: drop press
    {"ipa": "/drɑːp prɛs/", "vi": "máy dập rơi; búa dập tự do rơi", "pos": "phrase"},
    # 4018: drug war
    {"ipa": "/drʌɡ wɔːr/", "vi": "cuộc chiến chống tội phạm ma túy", "pos": "phrase"},
    # 4019: eastern time
    {"ipa": "/ˈiːstərn taɪm/", "vi": "giờ miền Đông Bắc Mỹ; múi giờ EST", "pos": "phrase"},
    # 4020: energy secretary
    {"ipa": "/ˈɛnərdʒi ˈsɛkrətɛri/", "vi": "Bộ trưởng Năng lượng Hoa Kỳ", "pos": "phrase"},
    # 4021: energy unit
    {"ipa": "/ˈɛnərdʒi ˈjuːnɪt/", "vi": "đơn vị đo lường năng lượng", "pos": "phrase"},
    # 4022: fast track
    {"ipa": "/fæst træk/", "vi": "tiến trình nhanh; lộ trình rút ngắn", "pos": "phrase"},
    # 4023: fat person
    {"ipa": "/fæt ˈpɜːrsn/", "vi": "người béo phì; người mập mạp tròn", "pos": "phrase"},
    # 4024: federal security service
    {"ipa": "/ˈfɛdərəl sɪˈkjʊrəti ˈsɜːrvɪs/", "vi": "Cơ quan An ninh Liên bang Nga", "pos": "phrase"},
    # 4025: field judge
    {"ipa": "/fiːld dʒʌdʒ/", "vi": "trọng tài sân thi đấu điền kinh", "pos": "phrase"},
    # 4026: financial loss
    {"ipa": "/faɪˈnænʃl lɔːs/", "vi": "thua lỗ tài chính; thiệt hại tiền", "pos": "phrase"},
    # 4027: flight line
    {"ipa": "/flaɪt laɪn/", "vi": "sân đỗ máy bay trước nhà chứa xưởng", "pos": "phrase"},
    # 4028: food shop
    {"ipa": "/fuːd ʃɑːp/", "vi": "cửa hàng bán đồ ăn thực phẩm", "pos": "phrase"},
    # 4029: force unit
    {"ipa": "/fɔːrs ˈjuːnɪt/", "vi": "đơn vị đo lực vật lý; đơn vị lực", "pos": "phrase"},
    # 4030: free throw
    {"ipa": "/friː θroʊ/", "vi": "cú ném phạt trong bóng rổ", "pos": "phrase"},
    # 4031: freedom party
    {"ipa": "/ˈfriːdəm ˈpɑːrti/", "vi": "Đảng Tự do; đảng phái tự do chính", "pos": "phrase"},
    # 4032: gay woman
    {"ipa": "/ɡeɪ ˈwʊmən/", "vi": "người phụ nữ đồng tính; phái nữ gay", "pos": "phrase"},
    # 4033: god tree
    {"ipa": "/ɡɑːd triː/", "vi": "cây bông gạo linh thiêng; cây thần", "pos": "phrase"},
    # 4034: good spirit
    {"ipa": "/ɡʊd ˈspɪrɪt/", "vi": "tinh thần lạc quan; thần lành phước", "pos": "phrase"},
    # 4035: gun rest
    {"ipa": "/ɡʌn rɛst/", "vi": "giá tì nòng súng; điểm tựa bắn súng", "pos": "phrase"},
    # 4036: high fashion
    {"ipa": "/haɪ ˈfæʃən/", "vi": "thời trang cao cấp; mốt thời thượng", "pos": "phrase"},
    # 4037: high profile
    {"ipa": "/haɪ ˈproʊfaɪl/", "vi": "vị thế nổi bật thu hút công chúng", "pos": "phrase"},
    # 4038: hospital bed
    {"ipa": "/ˈhɑːspɪtl bɛd/", "vi": "giường bệnh viện cho bệnh nhân nằm", "pos": "phrase"},
    # 4039: indian red
    {"ipa": "/ˈɪndiən rɛd/", "vi": "sắc đỏ Ấn Độ; màu đỏ oxit sắt", "pos": "phrase"},
    # 4040: information theory
    {"ipa": "/ˌɪnfərˈmeɪʃən ˈθiːəri/", "vi": "lý thuyết thông tin trong tin học", "pos": "phrase"},
    # 4041: investment company
    {"ipa": "/ɪnˈvɛstmənt ˈkʌmpəni/", "vi": "công ty đầu tư vốn; quỹ đầu tư", "pos": "phrase"},
    # 4042: james river
    {"ipa": "/dʒeɪmz ˈrɪvər/", "vi": "sông James tại bang Virginia Mỹ", "pos": "phrase"},
    # 4043: job application
    {"ipa": "/dʒɑːb ˌæplɪˈkeɪʃən/", "vi": "đơn xin việc làm; hồ sơ ứng tuyển", "pos": "phrase"},
    # 4044: job interview
    {"ipa": "/dʒɑːb ˈɪntərvjuː/", "vi": "buổi phỏng vấn xin việc tuyển dụng", "pos": "phrase"},
    # 4045: john smith
    {"ipa": "/dʒɑːn smɪθ/", "vi": "thuyền trưởng John Smith Jamestown", "pos": "phrase"},
    # 4046: learned person
    {"ipa": "/ˈlɜːrnɪd ˈpɜːrsn/", "vi": "bậc học giả; nhà trí thức uyên bác", "pos": "phrase"},
    # 4047: light touch
    {"ipa": "/laɪt tʌtʃ/", "vi": "cú chạm nhẹ; cách ứng xử khéo léo", "pos": "phrase"},
    # 4048: limited review
    {"ipa": "/ˈlɪmɪtɪd rɪˈvjuː/", "vi": "soát xét có giới hạn; kiểm toán nhẹ", "pos": "phrase"},
    # 4049: line of flight
    {"ipa": "/laɪn ʌv flaɪt/", "vi": "quỹ đạo bay; đường bay trên trời", "pos": "phrase"},
    # 4050: looking glass
    {"ipa": "/ˈlʊkɪŋ ɡlæs/", "vi": "gương soi mặt; tấm gương phản chiếu", "pos": "phrase"},
    # 4051: male body
    {"ipa": "/meɪl ˈbɑːdi/", "vi": "thân thể nam giới; vóc dáng đàn ông", "pos": "phrase"},
    # 4052: master of education
    {"ipa": "/ˈmæstər ʌv ˌɛdʒuˈkeɪʃən/", "vi": "thạc sĩ giáo dục học bằng cấp", "pos": "phrase"},
    # 4053: master plan
    {"ipa": "/ˈmæstər plæn/", "vi": "kế hoạch tổng thể quy hoạch dài hạn", "pos": "phrase"},
    # 4054: mean distance
    {"ipa": "/miːn ˈdɪstəns/", "vi": "khoảng cách trung bình giữa hai vật", "pos": "phrase"},
    # 4055: moving picture
    {"ipa": "/ˈmuːvɪŋ ˈpɪktʃər/", "vi": "phim điện ảnh; hình ảnh chuyển động", "pos": "phrase"},
    # 4056: news agency
    {"ipa": "/nuːz ˈeɪdʒənsi/", "vi": "hãng thông tấn tin tức; cơ quan tin", "pos": "phrase"},
    # 4057: office block
    {"ipa": "/ˈɔːfɪs blɑːk/", "vi": "tòa nhà văn phòng làm việc lớn", "pos": "phrase"},
    # 4058: old rose
    {"ipa": "/oʊld roʊz/", "vi": "màu hồng cổ điển; sắc hồng xám tím", "pos": "phrase"},
    # 4059: opportunity cost
    {"ipa": "/ˌɑːpərˈtuːnəti kɔːst/", "vi": "chi phí cơ hội trong kinh tế học", "pos": "phrase"},
    # 4060: paper loss
    {"ipa": "/ˈpeɪpər lɔːs/", "vi": "khoản lỗ trên sổ sách kế toán", "pos": "phrase"},
    # 4061: patient of
    {"ipa": "/ˈpeɪʃnt ʌv/", "vi": "kiên nhẫn chịu đựng; chịu đựng được", "pos": "phrase"},
    # 4062: personal computer
    {"ipa": "/ˈpɜːrsənl kəmˈpjuːtər/", "vi": "máy vi tính cá nhân; thiết bị PC", "pos": "phrase"},
    # 4063: personal income
    {"ipa": "/ˈpɜːrsənl ˈɪnkʌm/", "vi": "thu nhập cá nhân kiếm được", "pos": "phrase"},
    # 4064: physical process
    {"ipa": "/ˈfɪzɪkl ˈprɑːsɛs/", "vi": "tiến trình vật lý tự nhiên", "pos": "phrase"},
    # 4065: plant food
    {"ipa": "/plænt fuːd/", "vi": "dinh dưỡng cho cây trồng; phân bón", "pos": "phrase"},
    # 4066: power walking
    {"ipa": "/ˈpaʊər ˈwɔːkɪŋ/", "vi": "đi bộ nhanh thể dục tốc độ cao", "pos": "phrase"},
    # 4067: prime of life
    {"ipa": "/praɪm ʌv laɪf/", "vi": "thời kỳ sung sức nhất đời người", "pos": "phrase"},
    # 4068: public square
    {"ipa": "/ˈpʌblɪk skwɛr/", "vi": "quảng trường công cộng giữa phố", "pos": "phrase"},
    # 4069: push around
    {"ipa": "/pʊʃ əˈraʊnd/", "vi": "bắt nạt ức hiếp; xỏ mũi chỉ huy", "pos": "phrase"},
    # 4070: radio source
    {"ipa": "/ˈreɪdioʊ sɔːrs/", "vi": "nguồn phát sóng vô tuyến thiên văn", "pos": "phrase"},
    # 4071: religious music
    {"ipa": "/rɪˈlɪdʒəs ˈmjuːzɪk/", "vi": "thánh ca tôn giáo; âm nhạc phụng vụ", "pos": "phrase"},
    # 4072: religious person
    {"ipa": "/rɪˈlɪdʒəs ˈpɜːrsn/", "vi": "người sùng đạo; tín đồ ngoan đạo", "pos": "phrase"},
    # 4073: sales tax
    {"ipa": "/seɪlz tæks/", "vi": "thuế bán hàng; thuế tiêu thụ bán lẻ", "pos": "phrase"},
    # 4074: second wind
    {"ipa": "/ˈsɛkənd wɪnd/", "vi": "sức bền phục hồi; năng lượng mới có", "pos": "phrase"},
    # 4075: secret plan
    {"ipa": "/ˈsiːkrət plæn/", "vi": "kế hoạch bí mật; mưu đồ ngầm kín", "pos": "phrase"},
    # 4076: secretary of energy
    {"ipa": "/ˈsɛkrətɛri ʌv ˈɛnərdʒi/", "vi": "Bộ trưởng Năng lượng Mỹ", "pos": "phrase"},
    # 4077: set square
    {"ipa": "/sɛt skwɛr/", "vi": "thước ê-ke tam giác góc vuông", "pos": "phrase"},
    # 4078: ship building
    {"ipa": "/ʃɪp ˈbɪldɪŋ/", "vi": "ngành đóng tàu thủy; đóng tàu bè", "pos": "phrase"},
    # 4079: shop talk
    {"ipa": "/ʃɑːp tɔːk/", "vi": "chuyện công việc nhà nghề; bàn việc", "pos": "phrase"},
    # 4080: short and sweet
    {"ipa": "/ʃɔːrt ænd swiːt/", "vi": "ngắn gọn súc tích dễ hiểu; vắn tắt", "pos": "phrase"},
    # 4081: shut out
    {"ipa": "/ʃʌt aʊt/", "vi": "chặn cửa ra vào; loại trừ khỏi trận", "pos": "phrase"},
    # 4082: shut up
    {"ipa": "/ʃʌt ʌp/", "vi": "im miệng lại; giam nhốt kín lại", "pos": "phrase"},
    # 4083: sick pay
    {"ipa": "/sɪk peɪ/", "vi": "tiền trợ cấp nghỉ ốm của nhân viên", "pos": "phrase"},
    # 4084: silver state
    {"ipa": "/ˈsɪlvər steɪt/", "vi": "bang Bạc; biệt danh bang Nevada", "pos": "phrase"},
    # 4085: smart money
    {"ipa": "/smɑːrt ˈmʌni/", "vi": "dòng tiền thông minh từ chuyên gia", "pos": "phrase"},
    # 4086: society of jesus
    {"ipa": "/səˈsaɪəti ʌv ˈdʒiːzəs/", "vi": "Dòng Tên trong Công giáo La Mã", "pos": "phrase"},
    # 4087: sound pressure
    {"ipa": "/saʊnd ˈprɛʃər/", "vi": "áp suất âm thanh trong không khí", "pos": "phrase"},
    # 4088: square away
    {"ipa": "/skwɛr əˈweɪ/", "vi": "sắp xếp gọn gàng; thu xếp xong xuôi", "pos": "phrase"},
    # 4089: standing order
    {"ipa": "/ˈstændɪŋ ˈɔːrdər/", "vi": "quy tắc thường trực; lệnh định kỳ", "pos": "phrase"},
    # 4090: stock list
    {"ipa": "/stɑːk lɪst/", "vi": "danh mục cổ phiếu niêm yết; bản kê", "pos": "phrase"},
    # 4091: stock market
    {"ipa": "/stɑːk ˈmɑːrkɪt/", "vi": "thị trường chứng khoán; sàn cổ phần", "pos": "phrase"},
    # 4092: talk shop
    {"ipa": "/tɔːk ʃɑːp/", "vi": "nói chuyện chuyên môn nghề nghiệp", "pos": "phrase"},
    # 4093: theory of games
    {"ipa": "/ˈθiːəri ʌv ɡeɪmz/", "vi": "lý thuyết trò chơi trong toán học", "pos": "phrase"},
    # 4094: under arms
    {"ipa": "/ˈʌndər ɑːrmz/", "vi": "được trang bị vũ khí chiến đấu", "pos": "phrase"},
    # 4095: union army
    {"ipa": "/ˈjuːnjən ˈɑːrmi/", "vi": "quân đội Liên bang miền Bắc Mỹ", "pos": "phrase"},
    # 4096: unit cost
    {"ipa": "/ˈjuːnɪt kɔːst/", "vi": "giá thành trên từng đơn vị sản phẩm", "pos": "phrase"},
    # 4097: university of texas
    {"ipa": "/ˌjuːnɪˈvɜːrsəti ʌv ˈtɛksəs/", "vi": "Viện Đại học Texas tại Hoa Kỳ", "pos": "phrase"},
    # 4098: video equipment
    {"ipa": "/ˈvɪdioʊ ɪˈkwɪpmənt/", "vi": "trang thiết bị quay phát video", "pos": "phrase"},
    # 4099: wanted notice
    {"ipa": "/ˈwɑːntɪd ˈnoʊtɪs/", "vi": "lệnh truy nã; thông báo truy bắt", "pos": "phrase"}
]

with open("scratch/b21_r09_raw_p1.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

assert len(raw_data) == 100
assert len(reviewed_entries) == 100

output = []
for i, item in enumerate(raw_data):
    rev = reviewed_entries[i]
    assert len(rev["vi"]) <= 35, f"Too long: {item['hw']} -> {rev['vi']} ({len(rev['vi'])} chars)"
    assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/"), f"Bad IPA: {item['hw']} -> {rev['ipa']}"
    assert rev["ipa"].count("/") == 2, f"Bad slash count: {item['hw']} -> {rev['ipa']}"
    assert rev["pos"] in ["noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"]

    entry = {
        "id": item["id"],
        "hw": item["hw"],
        "pos": rev["pos"],
        "ipa": rev["ipa"],
        "vi": rev["vi"],
        "cefr": item["cefr"],
        "tier": item["tier"],
        "status": "reviewed",
        "notes": item["notes"]
    }
    output.append(entry)

with open("scratch/b21_r09_p1.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(output)} entries for Round 9 Part 1.")
