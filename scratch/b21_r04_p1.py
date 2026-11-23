import json

# Manual word-by-word cognitive review for Batch 21 Round 4 Part 1 (records 1500-1599, IDs 200k.001502 to 200k.001601)
reviewed_entries = [
    # 1500: north side
    {"ipa": "/nɔːrθ saɪd/", "vi": "phía bắc; mặt phía bắc tòa nhà", "pos": "phrase"},
    # 1501: phone system
    {"ipa": "/foʊn ˈsɪstəm/", "vi": "hệ thống tổng đài điện thoại", "pos": "phrase"},
    # 1502: play list
    {"ipa": "/pleɪ lɪst/", "vi": "danh sách bài hát phát; playlist", "pos": "phrase"},
    # 1503: playing area
    {"ipa": "/ˈpleɪɪŋ ˈɛriə/", "vi": "sân chơi bãi tập; khu vực thi đấu", "pos": "phrase"},
    # 1504: post office
    {"ipa": "/poʊst ˈɔːfɪs/", "vi": "bưu điện; bưu cục chuyển phát", "pos": "phrase"},
    # 1505: public works
    {"ipa": "/ˈpʌblɪk wɜːrks/", "vi": "các công trình phúc lợi công cộng", "pos": "phrase"},
    # 1506: put across
    {"ipa": "/pʊt əˈkrɔːs/", "vi": "truyền tải thông điệp hiệu quả", "pos": "phrase"},
    # 1507: red water
    {"ipa": "/rɛd ˈwɔːtər/", "vi": "bệnh đái ra máu ở gia súc", "pos": "phrase"},
    # 1508: rest house
    {"ipa": "/rɛst haʊs/", "vi": "nhà trạm nghỉ chân; quán trọ", "pos": "phrase"},
    # 1509: running game
    {"ipa": "/ˈrʌnɪŋ ɡeɪm/", "vi": "lối chơi chạy bóng tấn công", "pos": "phrase"},
    # 1510: school board
    {"ipa": "/skuːl bɔːrd/", "vi": "hội đồng quản trị trường học", "pos": "phrase"},
    # 1511: school term
    {"ipa": "/skuːl tɜːrm/", "vi": "học kỳ niên khóa nhà trường", "pos": "phrase"},
    # 1512: send in
    {"ipa": "/sɛnd ɪn/", "vi": "gửi đơn qua bưu điện; phái quân vào", "pos": "phrase"},
    # 1513: set on fire
    {"ipa": "/sɛt ɑːn ˈfaɪər/", "vi": "châm ngòi đốt cháy; thiêu rụi", "pos": "phrase"},
    # 1514: size up
    {"ipa": "/saɪz ʌp/", "vi": "quan sát đánh giá; nhìn thấu", "pos": "phrase"},
    # 1515: social control
    {"ipa": "/ˈsoʊʃəl kənˈtroʊl/", "vi": "sự kiểm soát kiểm tỏa xã hội", "pos": "phrase"},
    # 1516: soon enough
    {"ipa": "/suːn ɪˈnʌf/", "vi": "chẳng bao lâu nữa; chẳng mấy chốc", "pos": "phrase"},
    # 1517: step out
    {"ipa": "/stɛp aʊt/", "vi": "bước ra ngoài chốc lát; dạo phố", "pos": "phrase"},
    # 1518: step up
    {"ipa": "/stɛp ʌp/", "vi": "tăng cường đẩy mạnh; bước lên trước", "pos": "phrase"},
    # 1519: street name
    {"ipa": "/striːt neɪm/", "vi": "tên đường phố; tiếng lóng giang hồ", "pos": "phrase"},
    # 1520: summer house
    {"ipa": "/ˈsʌmər haʊs/", "vi": "nhà nghỉ mát mùa hè biệt lập", "pos": "phrase"},
    # 1521: summer school
    {"ipa": "/ˈsʌmər skuːl/", "vi": "khóa học hè; lớp bồi dưỡng hè", "pos": "phrase"},
    # 1522: take hold of
    {"ipa": "/teɪk hoʊld ʌv/", "vi": "nắm chặt lấy; xâm chiếm tâm trí", "pos": "phrase"},
    # 1523: third power
    {"ipa": "/θɜːrd ˈpaʊər/", "vi": "lũy thừa bậc ba; lập phương", "pos": "phrase"},
    # 1524: town house
    {"ipa": "/taʊn haʊs/", "vi": "nhà phố liền kề; biệt thự phố", "pos": "phrase"},
    # 1525: vote in
    {"ipa": "/voʊt ɪn/", "vi": "bầu cử trúng cử vào chức vụ", "pos": "phrase"},
    # 1526: working girl
    {"ipa": "/ˈwɜːrkɪŋ ɡɜːrl/", "vi": "cô gái đi làm; gái bán hoa", "pos": "phrase"},
    # 1527: world view
    {"ipa": "/wɜːrld vjuː/", "vi": "thế giới quan triết học", "pos": "phrase"},
    # 1528: sames
    {"ipa": "/ˈsɑːmiz/", "vi": "người Sami; những vật giống nhau", "pos": "noun"},
    # 1529: bad check
    {"ipa": "/bæd tʃɛk/", "vi": "séc giả; tấm séc không đủ tiền", "pos": "phrase"},
    # 1530: big board
    {"ipa": "/bɪɡ bɔːrd/", "vi": "Sở giao dịch chứng khoán New York", "pos": "phrase"},
    # 1531: break down
    {"ipa": "/breɪk daʊn/", "vi": "hỏng hóc máy móc; suy sụp tinh thần", "pos": "phrase"},
    # 1532: break through
    {"ipa": "/breɪk θruː/", "vi": "đột phá phòng tuyến; hé rạng mây", "pos": "phrase"},
    # 1533: child support
    {"ipa": "/tʃaɪld səˈpɔːrt/", "vi": "tiền cấp dưỡng nuôi con định kỳ", "pos": "phrase"},
    # 1534: church year
    {"ipa": "/tʃɜːrtʃ jɪr/", "vi": "năm phụng vụ giáo hội Kitô", "pos": "phrase"},
    # 1535: city father
    {"ipa": "/ˈsɪti ˈfɑːðər/", "vi": "quan chức lãnh đạo kỳ cựu đô thị", "pos": "phrase"},
    # 1536: city of london
    {"ipa": "/ˈsɪti ʌv ˈlʌndən/", "vi": "Khu tài chính Thành phố Luân Đôn", "pos": "phrase"},
    # 1537: clear away
    {"ipa": "/klɪr əˈweɪ/", "vi": "dọn dẹp sạch sẽ; tan biến đi", "pos": "phrase"},
    # 1538: first reading
    {"ipa": "/fɜːrst ˈriːdɪŋ/", "vi": "phiên đọc dự luật lần thứ nhất", "pos": "phrase"},
    # 1539: food court
    {"ipa": "/fuːd kɔːrt/", "vi": "khu ẩm thực tập trung trung tâm", "pos": "phrase"},
    # 1540: get the picture
    {"ipa": "/ɡɛt ðə ˈpɪktʃər/", "vi": "hiểu rõ tình hình; nắm bắt được ý", "pos": "phrase"},
    # 1541: human face
    {"ipa": "/ˈhjuːmən feɪs/", "vi": "khuôn mặt người; diện mạo nhân đạo", "pos": "phrase"},
    # 1542: in short order
    {"ipa": "/ɪn ʃɔːrt ˈɔːrdər/", "vi": "nhanh chóng mau lẹ; ngay tức khắc", "pos": "phrase"},
    # 1543: key out
    {"ipa": "/kiː aʊt/", "vi": "nhận diện phân loại sinh vật", "pos": "phrase"},
    # 1544: list system
    {"ipa": "/lɪst ˈsɪstəm/", "vi": "hệ thống bầu cử danh sách đảng", "pos": "phrase"},
    # 1545: major power
    {"ipa": "/ˈmeɪdʒər ˈpaʊər/", "vi": "cường quốc có tầm ảnh hưởng lớn", "pos": "phrase"},
    # 1546: old north state
    {"ipa": "/oʊld nɔːrθ steɪt/", "vi": "biệt danh bang Bắc Carolina", "pos": "phrase"},
    # 1547: political system
    {"ipa": "/pəˈlɪtɪkəl ˈsɪstəm/", "vi": "hệ thống thể chế chính trị", "pos": "phrase"},
    # 1548: question of law
    {"ipa": "/ˈkwɛstʃən ʌv lɔː/", "vi": "vấn đề giải thích pháp luật áp dụng", "pos": "phrase"},
    # 1549: red line
    {"ipa": "/rɛd laɪn/", "vi": "vạch ranh giới đỏ không thể vượt", "pos": "phrase"},
    # 1550: related to
    {"ipa": "/rɪˈleɪtɪd tuː/", "vi": "có liên quan mật thiết tới; có họ", "pos": "phrase"},
    # 1551: right bank
    {"ipa": "/raɪt bæŋk/", "vi": "Hữu ngạn sông Seine; bờ sông phải", "pos": "phrase"},
    # 1552: road show
    {"ipa": "/roʊd ʃoʊ/", "vi": "chương trình quảng bá lưu động", "pos": "phrase"},
    # 1553: run low
    {"ipa": "/rʌn loʊ/", "vi": "dần cạn kiệt; gần hết nguồn cung", "pos": "phrase"},
    # 1554: run short
    {"ipa": "/rʌn ʃɔːrt/", "vi": "bị thiếu hụt; không còn đủ dùng", "pos": "phrase"},
    # 1555: send for
    {"ipa": "/sɛnd fɔːr/", "vi": "cho mời đến; nhắn gọi người đến", "pos": "phrase"},
    # 1556: send on
    {"ipa": "/sɛnd ɑːn/", "vi": "chuyển tiếp thư từ; gửi đi trước", "pos": "phrase"},
    # 1557: short line
    {"ipa": "/ʃɔːrt laɪn/", "vi": "tuyến đường sắt nhánh địa phương", "pos": "phrase"},
    # 1558: short order
    {"ipa": "/ʃɔːrt ˈɔːrdər/", "vi": "món ăn chế biến nhanh phục vụ ngay", "pos": "phrase"},
    # 1559: six times
    {"ipa": "/sɪks taɪmz/", "vi": "sáu lần; gấp sáu lần", "pos": "phrase"},
    # 1560: talking point
    {"ipa": "/ˈtɔːkɪŋ pɔɪnt/", "vi": "chủ đề nóng bàn luận; luận điểm", "pos": "phrase"},
    # 1561: the least bit
    {"ipa": "/ðə liːst bɪt/", "vi": "một chút nào; một tí tẹo nào", "pos": "phrase"},
    # 1562: third party
    {"ipa": "/θɜːrd ˈpɑːrti/", "vi": "bên thứ ba ngoài cuộc tranh chấp", "pos": "phrase"},
    # 1563: water development
    {"ipa": "/ˈwɔːtər dɪˈvɛləpmənt/", "vi": "phát triển tài nguyên nước thủy lợi", "pos": "phrase"},
    # 1564: west point
    {"ipa": "/wɛst pɔɪnt/", "vi": "Học viện Quân sự West Point Mỹ", "pos": "phrase"},
    # 1565: word play
    {"ipa": "/wɜːrd pleɪ/", "vi": "nghệ thuật chơi chữ; lối nói lái", "pos": "phrase"},
    # 1566: working class
    {"ipa": "/ˈwɜːrkɪŋ klæs/", "vi": "giai cấp công nhân lao động", "pos": "phrase"},
    # 1567: young girl
    {"ipa": "/jʌŋ ɡɜːrl/", "vi": "thiếu nữ trẻ tuổi; bé gái nhỏ", "pos": "phrase"},
    # 1568: add to
    {"ipa": "/æd tuː/", "vi": "gia tăng thêm; bổ sung vào", "pos": "phrase"},
    # 1569: big shot
    {"ipa": "/bɪɡ ʃɑːt/", "vi": "nhân vật tai to mặt lớn; ông trùm", "pos": "phrase"},
    # 1570: business college
    {"ipa": "/ˈbɪznəs ˈkɑːlɪdʒ/", "vi": "trường cao đẳng đào tạo kinh doanh", "pos": "phrase"},
    # 1571: call fire
    {"ipa": "/kɔːl ˈfaɪər/", "vi": "hỏa lực bắn chi viện theo yêu cầu", "pos": "phrase"},
    # 1572: central time
    {"ipa": "/ˈsɛntrəl taɪm/", "vi": "múi giờ miền Trung nước Mỹ", "pos": "phrase"},
    # 1573: control room
    {"ipa": "/kənˈtroʊl ruːm/", "vi": "phòng điều khiển trung tâm", "pos": "phrase"},
    # 1574: cut away
    {"ipa": "/kʌt əˈweɪ/", "vi": "cắt bỏ phần thừa; chuyển cảnh máy", "pos": "phrase"},
    # 1575: eat into
    {"ipa": "/iːt ˈɪntuː/", "vi": "ăn lạm vào tài khoản; gặm mòn", "pos": "phrase"},
    # 1576: fall into
    {"ipa": "/fɔːl ˈɪntuː/", "vi": "rơi vào trạng thái; thuộc diện", "pos": "phrase"},
    # 1577: first step
    {"ipa": "/fɜːrst stɛp/", "vi": "bước đi đầu tiên; bước khởi đầu", "pos": "phrase"},
    # 1578: great white hope
    {"ipa": "/ɡreɪt waɪt hoʊp/", "vi": "niềm hy vọng lớn giải cứu khó khăn", "pos": "phrase"},
    # 1579: heart line
    {"ipa": "/hɑːrt laɪn/", "vi": "đường tâm đạo trong lòng bàn tay", "pos": "phrase"},
    # 1580: in due course
    {"ipa": "/ɪn djuː kɔːrs/", "vi": "đúng lúc; theo trình tự tự nhiên", "pos": "phrase"},
    # 1581: left field
    {"ipa": "/lɛft fiːld/", "vi": "vị trí sân ngoài bên trái; kỳ quặc", "pos": "phrase"},
    # 1582: line of heart
    {"ipa": "/laɪn ʌv hɑːrt/", "vi": "đường tâm đạo; đường tình duyên", "pos": "phrase"},
    # 1583: man hour
    {"ipa": "/mæn ˈaʊər/", "vi": "giờ công làm việc của một người", "pos": "phrase"},
    # 1584: matter of fact
    {"ipa": "/ˈmætər ʌv fækt/", "vi": "sự thật hiển nhiên; vấn đề thực tế", "pos": "phrase"},
    # 1585: new england
    {"ipa": "/nuː ˈɪŋɡlənd/", "vi": "vùng New England Đông Bắc Mỹ", "pos": "phrase"},
    # 1586: order form
    {"ipa": "/ˈɔːrdər fɔːrm/", "vi": "phiếu đặt mua hàng hóa", "pos": "phrase"},
    # 1587: perfect game
    {"ipa": "/ˈpɜːrfɪkt ɡeɪm/", "vi": "trận đấu ném bóng hoàn hảo", "pos": "phrase"},
    # 1588: phone call
    {"ipa": "/foʊn kɔːl/", "vi": "cuộc điện thoại trao đổi", "pos": "phrase"},
    # 1589: police car
    {"ipa": "/pəˈliːs kɑːr/", "vi": "xe tuần tra của cảnh sát", "pos": "phrase"},
    # 1590: put one across
    {"ipa": "/pʊt wʌn əˈkrɔːs/", "vi": "đánh lừa thành công; xỏ mũi", "pos": "phrase"},
    # 1591: second moment
    {"ipa": "/ˈsɛkənd ˈmoʊmənt/", "vi": "mô-men bậc hai; phương sai", "pos": "phrase"},
    # 1592: send out
    {"ipa": "/sɛnd aʊt/", "vi": "phát tán tín hiệu; gửi phát đi", "pos": "phrase"},
    # 1593: short story
    {"ipa": "/ʃɔːrt ˈstɔːri/", "vi": "tác phẩm truyện ngắn văn xuôi", "pos": "phrase"},
    # 1594: shot put
    {"ipa": "/ʃɑːt pʊt/", "vi": "môn thể thao đẩy tạ điền kinh", "pos": "phrase"},
    # 1595: social class
    {"ipa": "/ˈsoʊʃəl klæs/", "vi": "giai cấp tầng lớp trong xã hội", "pos": "phrase"},
    # 1596: stand back
    {"ipa": "/stænd bæk/", "vi": "lùi lại phía sau giữ khoảng cách", "pos": "phrase"},
    # 1597: stay together
    {"ipa": "/steɪ təˈɡɛðər/", "vi": "ở bên nhau sát cánh; gắn bó keo sơn", "pos": "phrase"},
    # 1598: street person
    {"ipa": "/striːt ˈpɜːrsən/", "vi": "người vô gia cư sống đầu đường", "pos": "phrase"},
    # 1599: system program
    {"ipa": "/ˈsɪstəm ˈproʊɡræm/", "vi": "chương trình phần mềm hệ thống", "pos": "phrase"},
]

with open('scratch/b21_r04_raw_p1.json') as f:
    raw_data = json.load(f)

assert len(raw_data) == 100
assert len(reviewed_entries) == 100

output = []
for i, item in enumerate(raw_data):
    rev = reviewed_entries[i]
    assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/") and rev["ipa"].count("/") == 2
    assert len(rev["vi"]) <= 35, f"vi too long: {rev['vi']} ({len(rev['vi'])} chars)"
    assert rev["pos"] in ["noun", "verb", "adj", "adv", "phrase", "intj", "prep", "conj", "pron", "det", "num"]
    
    new_item = {
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
    output.append(new_item)

with open('scratch/b21_r04_p1.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r04_p1.json created successfully and validated!")
