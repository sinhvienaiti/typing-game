import json

# Manual word-by-word cognitive review for Batch 21 Round 3 Part 5 (records 1400-1499, IDs 200k.001402 to 200k.001501)
reviewed_entries = [
    # 1400: party girl
    {"ipa": "/ˈpɑːrti ɡɜːrl/", "vi": "cô gái thích tiệc tùng ăn chơi", "pos": "phrase"},
    # 1401: phone number
    {"ipa": "/foʊn ˈnʌmbər/", "vi": "số điện thoại liên lạc", "pos": "phrase"},
    # 1402: point woman
    {"ipa": "/pɔɪnt ˈwʊmən/", "vi": "nữ lãnh đạo tiên phong dẫn dắt", "pos": "phrase"},
    # 1403: power series
    {"ipa": "/ˈpaʊər ˈsɪriːz/", "vi": "chuỗi lũy thừa trong toán học", "pos": "phrase"},
    # 1404: press out
    {"ipa": "/prɛs aʊt/", "vi": "ép chiết lấy nước; dập tắt lửa", "pos": "phrase"},
    # 1405: rest home
    {"ipa": "/rɛst hoʊm/", "vi": "viện dưỡng lão; nhà an dưỡng tuổi", "pos": "phrase"},
    # 1406: run along
    {"ipa": "/rʌn əˈlɔːŋ/", "vi": "chạy dọc theo bờ; đi chỗ khác chơi", "pos": "phrase"},
    # 1407: stand by
    {"ipa": "/stænd baɪ/", "vi": "sẵn sàng hỗ trợ; đứng ngoài nhìn", "pos": "phrase"},
    # 1408: stand for
    {"ipa": "/stænd fɔːr/", "vi": "viết tắt của; đại diện biểu trưng", "pos": "phrase"},
    # 1409: step in
    {"ipa": "/stɛp ɪn/", "vi": "can thiệp giải quyết; thế chỗ ai", "pos": "phrase"},
    # 1410: take account
    {"ipa": "/teɪk əˈkaʊnt/", "vi": "lưu tâm xem xét; tính đến yếu tố", "pos": "phrase"},
    # 1411: very important person
    {"ipa": "/ˈvɛri ɪmˈpɔːrtənt ˈpɜːrsən/", "vi": "nhân vật rất quan trọng; khách VIP", "pos": "phrase"},
    # 1412: watch case
    {"ipa": "/wɑːtʃ keɪs/", "vi": "vỏ bọc đồng hồ đeo tay", "pos": "phrase"},
    # 1413: word game
    {"ipa": "/wɜːrd ɡeɪm/", "vi": "trò chơi đố chữ; trò chơi ngôn từ", "pos": "phrase"},
    # 1414: world record
    {"ipa": "/wɜːrld ˈrɛkərd/", "vi": "kỷ lục thế giới được xác lập", "pos": "phrase"},
    # 1415: manning
    {"ipa": "/ˈmænɪŋ/", "vi": "bố trí nhân lực; đang điều khiển", "pos": "verb"},
    # 1416: mans
    {"ipa": "/mænz/", "vi": "bố trí người vận hành; đảm nhiệm", "pos": "verb"},
    # 1417: board game
    {"ipa": "/bɔːrd ɡeɪm/", "vi": "trò chơi cờ bàn giải trí", "pos": "phrase"},
    # 1418: break even
    {"ipa": "/breɪk ˈiːvən/", "vi": "hòa vốn kinh doanh không lãi lỗ", "pos": "phrase"},
    # 1419: business deal
    {"ipa": "/ˈbɪznəs diːl/", "vi": "thương vụ mua bán; giao dịch", "pos": "phrase"},
    # 1420: close order
    {"ipa": "/kloʊs ˈɔːrdər/", "vi": "đội hình hành quân sát hàng", "pos": "phrase"},
    # 1421: day return
    {"ipa": "/deɪ rɪˈtɜːrn/", "vi": "vé tàu xe khứ hồi trong ngày", "pos": "phrase"},
    # 1422: department of state
    {"ipa": "/dɪˈpɑːrtmənt ʌv steɪt/", "vi": "Bộ Ngoại giao Hoa Kỳ", "pos": "phrase"},
    # 1423: eat at
    {"ipa": "/iːt æt/", "vi": "dày vò tâm can; ăn mòn dần", "pos": "phrase"},
    # 1424: eat on
    {"ipa": "/iːt ɑːn/", "vi": "gặm nhấm tinh thần; giày vò tâm can", "pos": "phrase"},
    # 1425: energy state
    {"ipa": "/ˈɛnərdʒi steɪt/", "vi": "trạng thái mức năng lượng vật lý", "pos": "phrase"},
    # 1426: fall for
    {"ipa": "/fɔːl fɔːr/", "vi": "phải lòng say đắm; sập bẫy lừa", "pos": "phrase"},
    # 1427: field game
    {"ipa": "/fiːld ɡeɪm/", "vi": "môn thể thao vận động ngoài trời", "pos": "phrase"},
    # 1428: fire company
    {"ipa": "/ˈfaɪər ˈkʌmpəni/", "vi": "đội lính cứu hỏa địa phương", "pos": "phrase"},
    # 1429: follow out
    {"ipa": "/ˈfɑːloʊ aʊt/", "vi": "thực hiện chỉ đạo đến nơi đến chốn", "pos": "phrase"},
    # 1430: follow up
    {"ipa": "/ˈfɑːloʊ ʌp/", "vi": "bám sát diễn biến; theo dõi thêm", "pos": "phrase"},
    # 1431: form of government
    {"ipa": "/fɔːrm ʌv ˈɡʌvərmənt/", "vi": "hình thức chính thể nhà nước", "pos": "phrase"},
    # 1432: free list
    {"ipa": "/friː lɪst/", "vi": "danh mục hàng hóa miễn thuế quan", "pos": "phrase"},
    # 1433: ground out
    {"ipa": "/ɡraʊnd aʊt/", "vi": "bị loại do bóng lăn chạm đất", "pos": "phrase"},
    # 1434: health food
    {"ipa": "/hɛlθ fuːd/", "vi": "thực phẩm bổ dưỡng cho sức khỏe", "pos": "phrase"},
    # 1435: health problem
    {"ipa": "/hɛlθ ˈprɑːbləm/", "vi": "vấn đề trục trặc về sức khỏe", "pos": "phrase"},
    # 1436: hold off
    {"ipa": "/hoʊld ɔːf/", "vi": "trì hoãn; cản bước bước tiến", "pos": "phrase"},
    # 1437: human head
    {"ipa": "/ˈhjuːmən hɛd/", "vi": "đầu người; phần đầu con người", "pos": "phrase"},
    # 1438: in any event
    {"ipa": "/ɪn ˈɛni ɪˈvɛnt/", "vi": "dù trong bất cứ tình huống nào", "pos": "phrase"},
    # 1439: long shot
    {"ipa": "/lɔːŋ ʃɑːt/", "vi": "canh bạc ít hy vọng; cú cược liều", "pos": "phrase"},
    # 1440: open air
    {"ipa": "/ˈoʊpən ɛr/", "vi": "ngoài trời thoáng mát; lộ thiên", "pos": "phrase"},
    # 1441: phone company
    {"ipa": "/foʊn ˈkʌmpəni/", "vi": "hãng cung cấp mạng viễn thông", "pos": "phrase"},
    # 1442: power saw
    {"ipa": "/ˈpaʊər sɔː/", "vi": "máy cưa xẻ chạy bằng điện", "pos": "phrase"},
    # 1443: range in
    {"ipa": "/reɪndʒ ɪn/", "vi": "ngắm bắn điều chỉnh cự ly đạn", "pos": "phrase"},
    # 1444: ready money
    {"ipa": "/ˈrɛdi ˈmʌni/", "vi": "tiền mặt có sẵn chi tiêu ngay", "pos": "phrase"},
    # 1445: road game
    {"ipa": "/roʊd ɡeɪm/", "vi": "trận đấu trên sân khách đối phương", "pos": "phrase"},
    # 1446: round out
    {"ipa": "/raʊnd aʊt/", "vi": "hoàn thiện trọn vẹn; làm tròn nét", "pos": "phrase"},
    # 1447: round up
    {"ipa": "/raʊnd ʌp/", "vi": "vây bắt tội phạm; dồn gia súc", "pos": "phrase"},
    # 1448: save up
    {"ipa": "/seɪv ʌp/", "vi": "tích lũy dành dụm tiền bạc", "pos": "phrase"},
    # 1449: size of it
    {"ipa": "/saɪz ʌv ɪt/", "vi": "thực trạng sự việc; sự thật là vậy", "pos": "phrase"},
    # 1450: sound out
    {"ipa": "/saʊnd aʊt/", "vi": "thăm dò ý kiến người khác", "pos": "phrase"},
    # 1451: stand out
    {"ipa": "/stænd aʊt/", "vi": "nổi bật xuất chúng; đập vào mắt", "pos": "phrase"},
    # 1452: stand up
    {"ipa": "/stænd ʌp/", "vi": "đứng dậy vươn lên; cho leo cây", "pos": "phrase"},
    # 1453: state department
    {"ipa": "/steɪt dɪˈpɑːrtmənt/", "vi": "Bộ Ngoại giao Hoa Kỳ", "pos": "phrase"},
    # 1454: step on
    {"ipa": "/stɛp ɑːn/", "vi": "giẫm chân lên; chà đạp áp bức", "pos": "phrase"},
    # 1455: step on it
    {"ipa": "/stɛp ɑːn ɪt/", "vi": "nhấn ga nhanh lên; khẩn trương lên", "pos": "phrase"},
    # 1456: stop watch
    {"ipa": "/stɑːp wɑːtʃ/", "vi": "đồng hồ bấm giây thể thao", "pos": "phrase"},
    # 1457: take hold
    {"ipa": "/teɪk hoʊld/", "vi": "nắm chặt lấy; phát huy tác dụng", "pos": "phrase"},
    # 1458: third person
    {"ipa": "/θɜːrd ˈpɜːrsən/", "vi": "ngôi thứ ba trong ngữ pháp", "pos": "phrase"},
    # 1459: time bill
    {"ipa": "/taɪm bɪl/", "vi": "hối phiếu thanh toán có kỳ hạn", "pos": "phrase"},
    # 1460: time value
    {"ipa": "/taɪm ˈvæljuː/", "vi": "trường độ nốt nhạc; độ ngân nốt", "pos": "phrase"},
    # 1461: trade in
    {"ipa": "/treɪd ɪn/", "vi": "đổi đồ cũ lấy đồ mới có bù tiền", "pos": "phrase"},
    # 1462: type family
    {"ipa": "/taɪp ˈfæməli/", "vi": "họ kiểu chữ phông chữ", "pos": "phrase"},
    # 1463: war room
    {"ipa": "/wɔːr ruːm/", "vi": "phòng chỉ huy tác chiến khẩn cấp", "pos": "phrase"},
    # 1464: white woman
    {"ipa": "/waɪt ˈwʊmən/", "vi": "người phụ nữ da trắng", "pos": "phrase"},
    # 1465: wish well
    {"ipa": "/wɪʃ wɛl/", "vi": "chúc điều may mắn tốt lành", "pos": "phrase"},
    # 1466: longed
    {"ipa": "/lɔːŋd/", "vi": "đã mong mỏi; khát khao da diết", "pos": "verb"},
    # 1467: longs
    {"ipa": "/lɔːŋz/", "vi": "mong mỏi thiết tha; khát khao", "pos": "verb"},
    # 1468: act of god
    {"ipa": "/ækt ʌv ɡɑːd/", "vi": "thiên tai bất khả kháng theo luật", "pos": "phrase"},
    # 1469: any longer
    {"ipa": "/ˈɛni ˈlɔːŋɡər/", "vi": "thêm chút nào nữa; không còn nữa", "pos": "phrase"},
    # 1470: break of day
    {"ipa": "/breɪk ʌv deɪ/", "vi": "lúc rạng đông; ánh bình minh rạng", "pos": "phrase"},
    # 1471: break off
    {"ipa": "/breɪk ɔːf/", "vi": "cắt đứt đàm phán; bẻ gãy rời ra", "pos": "phrase"},
    # 1472: change form
    {"ipa": "/tʃeɪndʒ fɔːrm/", "vi": "biến hình đổi dạng; chuyển thể", "pos": "phrase"},
    # 1473: child care
    {"ipa": "/tʃaɪld kɛr/", "vi": "dịch vụ chăm sóc trông giữ trẻ", "pos": "phrase"},
    # 1474: class war
    {"ipa": "/klæs wɔːr/", "vi": "cuộc chiến đấu tranh giai cấp", "pos": "phrase"},
    # 1475: close together
    {"ipa": "/kloʊs təˈɡɛðər/", "vi": "sát cạnh nhau; khăng khít", "pos": "phrase"},
    # 1476: common man
    {"ipa": "/ˈkɑːmən mæn/", "vi": "người dân bình thường; thường dân", "pos": "phrase"},
    # 1477: community service
    {"ipa": "/kəˈmjuːnəti ˈsɜːrvɪs/", "vi": "lao động công ích phục vụ xã hội", "pos": "phrase"},
    # 1478: drive out
    {"ipa": "/draɪv aʊt/", "vi": "xua đuổi ra ngoài; tống cổ", "pos": "phrase"},
    # 1479: drive up
    {"ipa": "/draɪv ʌp/", "vi": "lái xe đỗ lại; đẩy giá tăng vọt", "pos": "phrase"},
    # 1480: eat out
    {"ipa": "/iːt aʊt/", "vi": "đi ăn ngoài tiệm; đi ăn nhà hàng", "pos": "phrase"},
    # 1481: eat up
    {"ipa": "/iːt ʌp/", "vi": "ăn sạch nhẵn đĩa; ngốn hết ngân quỹ", "pos": "phrase"},
    # 1482: fall out
    {"ipa": "/fɔːl aʊt/", "vi": "bất hòa cãi cọ; bụi phóng xạ rơi", "pos": "phrase"},
    # 1483: fast one
    {"ipa": "/fæst wʌn/", "vi": "đòn lừa bịp xỏ lá; mưu mẹo gian xảo", "pos": "phrase"},
    # 1484: felt up
    {"ipa": "/fɛlt ʌp/", "vi": "sờ mó khiêu dâm; dính kết nỉ", "pos": "phrase"},
    # 1485: field house
    {"ipa": "/fiːld haʊs/", "vi": "nhà thi đấu thể thao phức hợp", "pos": "phrase"},
    # 1486: follow up on
    {"ipa": "/ˈfɑːloʊ ʌp ɑːn/", "vi": "tiếp tục theo sát theo đuổi", "pos": "phrase"},
    # 1487: government building
    {"ipa": "/ˈɡʌvərmənt ˈbɪldɪŋ/", "vi": "tòa nhà trụ sở cơ quan chính phủ", "pos": "phrase"},
    # 1488: hand in hand
    {"ipa": "/hænd ɪn hænd/", "vi": "tay trong tay; luôn song hành cùng", "pos": "phrase"},
    # 1489: hand to hand
    {"ipa": "/hænd tuː hænd/", "vi": "giáp lá cà cự ly gần; đánh tay đôi", "pos": "phrase"},
    # 1490: hold down
    {"ipa": "/hoʊld daʊn/", "vi": "đè nén áp chế; giữ vững vị trí việc", "pos": "phrase"},
    # 1491: hold still for
    {"ipa": "/hoʊld stɪl fɔːr/", "vi": "chịu đựng dung thứ; khoanh tay chịu", "pos": "phrase"},
    # 1492: in due season
    {"ipa": "/ɪn djuː ˈsiːzən/", "vi": "đúng thời vụ mùa màng; đúng dịp", "pos": "phrase"},
    # 1493: in style
    {"ipa": "/ɪn staɪl/", "vi": "hợp mốt thời thượng; sang trọng", "pos": "phrase"},
    # 1494: international law
    {"ipa": "/ˌɪntərˈnæʃənəl lɔː/", "vi": "công pháp quốc tế; luật quốc tế", "pos": "phrase"},
    # 1495: low water
    {"ipa": "/loʊ ˈwɔːtər/", "vi": "mực nước triều rút; con nước ròng", "pos": "phrase"},
    # 1496: matter of course
    {"ipa": "/ˈmætər ʌv kɔːrs/", "vi": "điều hiển nhiên; chuyện tất yếu", "pos": "phrase"},
    # 1497: matter of law
    {"ipa": "/ˈmætər ʌv lɔː/", "vi": "vấn đề thuộc phạm trù luật pháp", "pos": "phrase"},
    # 1498: military man
    {"ipa": "/ˈmɪlətɛri mæn/", "vi": "quân nhân binh nghiệp; người lính", "pos": "phrase"},
    # 1499: north american
    {"ipa": "/nɔːrθ əˈmɛrɪkən/", "vi": "người Bắc Mỹ; thuộc vùng Bắc Mỹ", "pos": "phrase"},
]

with open('scratch/b21_r03_raw_p5.json') as f:
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

with open('scratch/b21_r03_p5.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r03_p5.json created successfully and validated!")
