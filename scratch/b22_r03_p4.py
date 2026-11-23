import json

raw_items = json.load(open("scratch/b22_r03_raw_p4.json"))

reviews = [
    # 00: distribution law
    {"pos": "phrase", "ipa": "/ˌdɪstrɪˈbjuːʃn lɔː/", "vi": "định luật phân bố thống kê"},
    # 01: eastern standard time
    {"pos": "phrase", "ipa": "/ˈiːstərn ˈstændərd taɪm/", "vi": "giờ chuẩn miền Đông Bắc Mỹ EST"},
    # 02: electric bill
    {"pos": "phrase", "ipa": "/ɪˈlɛktrɪk bɪl/", "vi": "hóa đơn tiền điện hàng tháng"},
    # 03: extended order
    {"pos": "phrase", "ipa": "/ɪkˈstɛndɪd ˈɔːrdər/", "vi": "đội hình hàng mở rộng tác chiến"},
    # 04: fake book
    {"pos": "phrase", "ipa": "/feɪk bʊk/", "vi": "tập hợp âm bài hát bỏ túi"},
    # 05: fall flat
    {"pos": "phrase", "ipa": "/fɔːl flæt/", "vi": "thất bại hoàn toàn; không gây cười"},
    # 06: fault line
    {"pos": "phrase", "ipa": "/fɔːlt laɪn/", "vi": "đường đứt gãy địa chất"},
    # 07: field of honor
    {"pos": "phrase", "ipa": "/fiːld əv ˈɑːnər/", "vi": "chiến trường danh dự; bãi quyết đấu"},
    # 08: financial aid
    {"pos": "phrase", "ipa": "/faɪˈnænʃl eɪd/", "vi": "hỗ trợ tài chính; gói học bổng"},
    # 09: fixed star
    {"pos": "phrase", "ipa": "/fɪkst stɑːr/", "vi": "hằng tinh thiên văn học"},
    # 10: food chain
    {"pos": "phrase", "ipa": "/fuːd tʃeɪn/", "vi": "chuỗi thức ăn sinh thái"},
    # 11: foot doctor
    {"pos": "phrase", "ipa": "/fʊt ˈdɑːktər/", "vi": "bác sĩ chuyên khoa bàn chân"},
    # 12: foreign aid
    {"pos": "phrase", "ipa": "/ˈfɔːrən eɪd/", "vi": "viện trợ nước ngoài; ODA"},
    # 13: frame in
    {"pos": "phrase", "ipa": "/freɪm ɪn/", "vi": "đóng khung bao bọc xung quanh"},
    # 14: golden age
    {"pos": "phrase", "ipa": "/ˈɡoʊldən eɪdʒ/", "vi": "thời kỳ hoàng kim rực rỡ nhất"},
    # 15: green bay
    {"pos": "phrase", "ipa": "/ɡriːn beɪ/", "vi": "thành phố Green Bay bang Wisconsin"},
    # 16: green tea
    {"pos": "phrase", "ipa": "/ɡriːn tiː/", "vi": "trà xanh tươi; chè xanh"},
    # 17: guard dog
    {"pos": "phrase", "ipa": "/ɡɑːrd dɔːɡ/", "vi": "chó canh gác nhà; chó nghiệp vụ"},
    # 18: hang back
    {"pos": "phrase", "ipa": "/hæŋ bæk/", "vi": "do dự ngập ngừng; lùi lại phía sau"},
    # 19: heavy metal
    {"pos": "phrase", "ipa": "/ˈhɛvi ˈmɛtl/", "vi": "kim loại nặng; nhạc heavy metal"},
    # 20: historical record
    {"pos": "phrase", "ipa": "/hɪˈstɔːrɪkl ˈrɛkərd/", "vi": "tư liệu ghi chép lịch sử thành văn"},
    # 21: holding cell
    {"pos": "phrase", "ipa": "/ˈhoʊldɪŋ sɛl/", "vi": "buồng tạm giam giữ can phạm"},
    # 22: ice bag
    {"pos": "phrase", "ipa": "/aɪs bæɡ/", "vi": "túi chườm đá lạnh y tế"},
    # 23: industrial bank
    {"pos": "phrase", "ipa": "/ɪnˈdʌstriəl bæŋk/", "vi": "ngân hàng công nghiệp chuyên dụng"},
    # 24: industrial park
    {"pos": "phrase", "ipa": "/ɪnˈdʌstriəl pɑːrk/", "vi": "khu công nghiệp chế xuất"},
    # 25: information measure
    {"pos": "phrase", "ipa": "/ˌɪnfərˈmeɪʃn ˈmɛʒər/", "vi": "thước đo lượng thông tin bit"},
    # 26: intelligence test
    {"pos": "phrase", "ipa": "/ɪnˈtɛlɪdʒəns tɛst/", "vi": "bài kiểm tra trắc nghiệm trí tuệ IQ"},
    # 27: james bay
    {"pos": "phrase", "ipa": "/dʒeɪmz beɪ/", "vi": "vịnh James phía nam vịnh Hudson"},
    # 28: jesus christ
    {"pos": "phrase", "ipa": "/ˈdʒiːzəs kraɪst/", "vi": "Chúa Giê-su Ki-tô"},
    # 29: jewish new year
    {"pos": "phrase", "ipa": "/ˈdʒuːɪʃ njuː jɪr/", "vi": "Tết Năm Mới Do Thái Rosh Hashanah"},
    # 30: journal box
    {"pos": "phrase", "ipa": "/ˈdʒɜːrnl bɑːks/", "vi": "hộp đỡ ổ trục toa xe lửa"},
    # 31: jump cut
    {"pos": "phrase", "ipa": "/dʒʌmp kʌt/", "vi": "kỹ thuật cắt cảnh nhảy cóc phim"},
    # 32: jump shot
    {"pos": "phrase", "ipa": "/dʒʌmp ʃɑːt/", "vi": "cú ném bóng rổ khi bật nhảy"},
    # 33: labor pain
    {"pos": "phrase", "ipa": "/ˈleɪbər peɪn/", "vi": "cơn đau đẻ chuyển dạ dữ dội"},
    # 34: legal injury
    {"pos": "phrase", "ipa": "/ˈliːɡl ˈɪndʒəri/", "vi": "tổn hại pháp lý; thiệt hại quyền"},
    # 35: life cycle
    {"pos": "phrase", "ipa": "/laɪf ˈsaɪkl/", "vi": "vòng đời sinh trưởng; chu kỳ sống"},
    # 36: listening watch
    {"pos": "phrase", "ipa": "/ˈlɪsnɪŋ wɑːtʃ/", "vi": "ca trực nghe sóng vô tuyến liên tục"},
    # 37: louis the german
    {"pos": "phrase", "ipa": "/ˈluːi ðə ˈdʒɜːrmən/", "vi": "Vua Louis Người Đức Caroling"},
    # 38: magazine article
    {"pos": "phrase", "ipa": "/ˌmæɡəˈziːn ˈɑːrtɪkl/", "vi": "bài báo đăng trên tạp chí định kỳ"},
    # 39: mary ii
    {"pos": "phrase", "ipa": "/ˈmɛri ðə ˈsɛkənd/", "vi": "Nữ hoàng Mary Đệ Nhị nước Anh"},
    # 40: match plane
    {"pos": "phrase", "ipa": "/mætʃ pleɪn/", "vi": "cái bào soi rãnh mộng ghép gỗ"},
    # 41: mental image
    {"pos": "phrase", "ipa": "/ˈmɛntl ˈɪmɪdʒ/", "vi": "hình ảnh tưởng tượng trong tâm trí"},
    # 42: military intelligence
    {"pos": "phrase", "ipa": "/ˈmɪlətɛri ɪnˈtɛlɪdʒəns/", "vi": "tình báo quân sự; tin tình báo"},
    # 43: mountain range
    {"pos": "phrase", "ipa": "/ˈmaʊntn reɪndʒ/", "vi": "dãy núi trùng điệp non cao"},
    # 44: moving van
    {"pos": "phrase", "ipa": "/ˈmuːvɪŋ væn/", "vi": "xe tải chuyên dọn nhà chở đồ đạc"},
    # 45: national science foundation
    {"pos": "phrase", "ipa": "/ˈnæʃnəl ˈsaɪəns faʊnˈdeɪʃn/", "vi": "Quỹ Khoa học Quốc gia Hoa Kỳ NSF"},
    # 46: native land
    {"pos": "phrase", "ipa": "/ˈneɪtɪv lænd/", "vi": "quê cha đất tổ; xứ sở quê hương"},
    # 47: net ball
    {"pos": "phrase", "ipa": "/nɛt bɔːl/", "vi": "bóng chạm mép lưới rơi qua sân"},
    # 48: opposite number
    {"pos": "phrase", "ipa": "/ˈɑːpəzət ˈnʌmbər/", "vi": "người đồng cấp tương đương đối tác"},
    # 49: pacific time
    {"pos": "phrase", "ipa": "/pəˈsɪfɪk taɪm/", "vi": "múi giờ bờ Tây Thái Bình Dương PT"},
    # 50: pair production
    {"pos": "phrase", "ipa": "/pɛr prəˈdʌkʃn/", "vi": "hiện tượng sinh cặp hạt và phản hạt"},
    # 51: passing water
    {"pos": "phrase", "ipa": "/ˈpæsɪŋ ˈwɔːtər/", "vi": "việc tiểu tiện bài tiết nước tiểu"},
    # 52: picture plane
    {"pos": "phrase", "ipa": "/ˈpɪktʃər pleɪn/", "vi": "mặt phẳng tranh vẽ phối cảnh họa"},
    # 53: plant cell
    {"pos": "phrase", "ipa": "/plænt sɛl/", "vi": "tế bào thực vật có vách xenlulô"},
    # 54: police squad
    {"pos": "phrase", "ipa": "/pəˈliːs skwɑːd/", "vi": "tiểu đội cảnh sát đặc nhiệm cơ động"},
    # 55: political platform
    {"pos": "phrase", "ipa": "/pəˈlɪtɪkl ˈplætfɔːrm/", "vi": "cương lĩnh chính trị của đảng"},
    # 56: quarter round
    {"pos": "phrase", "ipa": "/ˈkwɔːrtər raʊnd/", "vi": "thanh phào chỉ tròn một phần tư"},
    # 57: race driver
    {"pos": "phrase", "ipa": "/reɪs ˈdraɪvər/", "vi": "tay đua xe ô tô; tay lái tốc độ"},
    # 58: red blood cell
    {"pos": "phrase", "ipa": "/rɛd blʌd sɛl/", "vi": "tế bào hồng cầu chuyên chở oxy"},
    # 59: rock garden
    {"pos": "phrase", "ipa": "/rɑːk ˈɡɑːrdn/", "vi": "vườn đá cảnh; hòn non bộ sân vườn"},
    # 60: round shape
    {"pos": "phrase", "ipa": "/raʊnd ʃeɪp/", "vi": "hình tròn xoe; dạng hình tròn cầu"},
    # 61: sea horse
    {"pos": "phrase", "ipa": "/siː hɔːrs/", "vi": "con cá ngựa dưới biển; hải mã"},
    # 62: security intelligence
    {"pos": "phrase", "ipa": "/sɪˈkjʊrəti ɪnˈtɛlɪdʒəns/", "vi": "tin tức tình báo an ninh quốc gia"},
    # 63: seeing eye dog
    {"pos": "phrase", "ipa": "/ˈsiːɪŋ aɪ dɔːɡ/", "vi": "chó dẫn đường trợ giúp người mù"},
    # 64: seven iron
    {"pos": "phrase", "ipa": "/ˈsɛvn ˈaɪərn/", "vi": "gậy sắt số 7 chơi đánh golf"},
    # 65: shopping list
    {"pos": "phrase", "ipa": "/ˈʃɑːpɪŋ lɪst/", "vi": "danh sách mua sắm; danh sách đi chợ"},
    # 66: small loan company
    {"pos": "phrase", "ipa": "/smɔːl loʊn ˈkʌmpəni/", "vi": "công ty tài chính vi mô cho vay nhỏ"},
    # 67: small stores
    {"pos": "phrase", "ipa": "/smɔːl stɔːrz/", "vi": "vật dụng thiết yếu cá nhân thủy thủ"},
    # 68: soft market
    {"pos": "phrase", "ipa": "/sɔːft ˈmɑːrkɪt/", "vi": "thị trường suy yếu thừa cung"},
    # 69: solo man
    {"pos": "phrase", "ipa": "/ˈsoʊloʊ mæn/", "vi": "người vượn cổ Solo Homo erectus"},
    # 70: south korea
    {"pos": "phrase", "ipa": "/saʊθ kəˈriːə/", "vi": "Đại Hàn Dân Quốc; nước Hàn Quốc"},
    # 71: space writer
    {"pos": "phrase", "ipa": "/speɪs ˈraɪtər/", "vi": "cộng tác viên báo trả theo dòng"},
    # 72: square dance
    {"pos": "phrase", "ipa": "/skwɛr dæns/", "vi": "điệu nhảy bốn đôi xếp hình vuông Mỹ"},
    # 73: surface ship
    {"pos": "phrase", "ipa": "/ˈsɜːrfɪs ʃɪp/", "vi": "tàu chiến mặt nước của hải quân"},
    # 74: switch off
    {"pos": "phrase", "ipa": "/swɪtʃ ɔːf/", "vi": "ngắt cầu dao; tắt nguồn điện"},
    # 75: taste property
    {"pos": "phrase", "ipa": "/teɪst ˈprɑːpərti/", "vi": "đặc tính vị giác; thuộc tính nếm"},
    # 76: teaching reading
    {"pos": "phrase", "ipa": "/ˈtiːtʃɪŋ ˈriːdɪŋ/", "vi": "phương pháp dạy tập đọc; dạy đọc"},
    # 77: test suit
    {"pos": "phrase", "ipa": "/tɛst suːt/", "vi": "vụ kiện án lệ thử nghiệm luật"},
    # 78: touch screen
    {"pos": "phrase", "ipa": "/tʌtʃ skriːn/", "vi": "màn hình cảm ứng đa điểm"},
    # 79: trade union movement
    {"pos": "phrase", "ipa": "/treɪd ˈjuːnjən ˈmuːvmənt/", "vi": "phong trào công đoàn lao động"},
    # 80: transfer tax
    {"pos": "phrase", "ipa": "/trænsˈfɜːr tæks/", "vi": "thuế chuyển quyền sở hữu tài sản"},
    # 81: water bird
    {"pos": "phrase", "ipa": "/ˈwɔːtər bɜːrd/", "vi": "chim sống dưới nước; loài thủy cầm"},
    # 82: wave number
    {"pos": "phrase", "ipa": "/weɪv ˈnʌmbər/", "vi": "số sóng trong quang phổ bước sóng"},
    # 83: white meat
    {"pos": "phrase", "ipa": "/waɪt miːt/", "vi": "thịt trắng như thịt lườn gà vịt"},
    # 84: write copy
    {"pos": "phrase", "ipa": "/raɪt ˈkɑːpi/", "vi": "viết lời quảng cáo copywriting"},
    # 85: zero point
    {"pos": "phrase", "ipa": "/ˈzɪroʊ pɔɪnt/", "vi": "điểm mốc số 0; gốc tọa độ chuẩn"},
    # 86: commonest
    {"pos": "adj", "ipa": "/ˈkɑːmənɪst/", "vi": "phổ biến nhất; thông thường nhất"},
    # 87: likelier
    {"pos": "adj", "ipa": "/ˈlaɪkliər/", "vi": "có nhiều khả năng hơn; dễ xảy ra"},
    # 88: likeliest
    {"pos": "adj", "ipa": "/ˈlaɪkliɪst/", "vi": "có khả năng nhất; triển vọng nhất"},
    # 89: perfectest
    {"pos": "adj", "ipa": "/ˈpɜːrfɪktɪst/", "vi": "hoàn hảo tột bậc; trọn vẹn nhất"},
    # 90: personals
    {"pos": "noun", "ipa": "/ˈpɜːrsnlz/", "vi": "mục nhắn tin riêng trên báo chí"},
    # 91: wonned
    {"pos": "verb", "ipa": "/wʌnd/", "vi": "đã trú ngụ; đã quen ở nơi chốn"},
    # 92: wonning
    {"pos": "noun", "ipa": "/ˈwʌnɪŋ/", "vi": "chốn cư ngụ; nơi trú ẩn xưa"},
    # 93: american falls
    {"pos": "phrase", "ipa": "/əˈmɛrɪkən fɔːlz/", "vi": "thác nước American Falls Niagara"},
    # 94: animal material
    {"pos": "phrase", "ipa": "/ˈænɪml məˈtɪriəl/", "vi": "vật liệu có nguồn gốc từ động vật"},
    # 95: animal product
    {"pos": "phrase", "ipa": "/ˈænɪml ˈprɑːdʌkt/", "vi": "thành phẩm chế biến từ động vật"},
    # 96: annual ring
    {"pos": "phrase", "ipa": "/ˈænjuəl rɪŋ/", "vi": "vòng gỗ tăng trưởng hàng năm cây"},
    # 97: appeal board
    {"pos": "phrase", "ipa": "/əˈpiːl bɔːrd/", "vi": "hội đồng xét xử phúc thẩm kháng cáo"},
    # 98: bear upon
    {"pos": "phrase", "ipa": "/bɛr əˈpɑːn/", "vi": "tác động trực tiếp đến; liên quan"},
    # 99: beauty sleep
    {"pos": "phrase", "ipa": "/ˈbjuːti sliːp/", "vi": "giấc ngủ sớm làm đẹp da buổi tối"}
]

for r in reviews:
    r["ipa"] = r["ipa"].strip()

assert len(reviews) == 100
assert len(raw_items) == 100

out_items = []
for i in range(100):
    item = dict(raw_items[i])
    rev = reviews[i]
    item["pos"] = rev["pos"]
    item["ipa"] = rev["ipa"]
    item["vi"] = rev["vi"]
    item["status"] = "reviewed"
    
    assert len(item["vi"]) <= 35, f"vi too long at {i}: {item['vi']}"
    assert len(item["vi"]) > 0
    assert item["ipa"].startswith("/") and item["ipa"].endswith("/") and item["ipa"].count("/") == 2
    out_items.append(item)

json.dump(out_items, open("scratch/b22_r03_p4.json", "w"), ensure_ascii=False, indent=2)
print("Round 3 Part 4 reviewed successfully: 100 items saved to scratch/b22_r03_p4.json")
