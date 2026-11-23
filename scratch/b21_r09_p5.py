import json

# Manual word-by-word cognitive review for Batch 21 Round 9 Part 5 (records 4400-4499, IDs 200k.004402 to 200k.004501)
reviewed_entries = [
    # 4400: hand glass
    {"ipa": "/hænd ɡlæs/", "vi": "gương cầm tay; kính lúp cầm tay", "pos": "phrase"},
    # 4401: heart block
    {"ipa": "/hɑːrt blɑːk/", "vi": "nghẽn dẫn truyền xung điện tim", "pos": "phrase"},
    # 4402: hotel bill
    {"ipa": "/hoʊˈtɛl bɪl/", "vi": "hóa đơn thanh toán phòng khách sạn", "pos": "phrase"},
    # 4403: human activity
    {"ipa": "/ˈhjuːmən ækˈtɪvəti/", "vi": "hoạt động của con người; nhân sinh", "pos": "phrase"},
    # 4404: ice pick
    {"ipa": "/aɪs pɪk/", "vi": "dùi đập đá; cây nhọn chọc vỡ băng", "pos": "phrase"},
    # 4405: indian shot
    {"ipa": "/ˈɪndiən ʃɑːt/", "vi": "cây chuối hoa; cây dong riềng cảnh", "pos": "phrase"},
    # 4406: indian summer
    {"ipa": "/ˈɪndiən ˈsʌmər/", "vi": "tiết trời ấm áp mùa thu muộn", "pos": "phrase"},
    # 4407: insurance policy
    {"ipa": "/ɪnˈʃʊrəns ˈpɑːləsi/", "vi": "hợp đồng bảo hiểm; đơn bảo hiểm", "pos": "phrase"},
    # 4408: international flight
    {"ipa": "/ˌɪntərˈnæʃnəl flaɪt/", "vi": "chuyến bay quốc tế qua biên giới", "pos": "phrase"},
    # 4409: japan current
    {"ipa": "/dʒəˈpæn ˈkɜːrənt/", "vi": "hải lưu Kuroshio Nhật Bản", "pos": "phrase"},
    # 4410: king of france
    {"ipa": "/kɪŋ ʌv fræns/", "vi": "vua nước Pháp; hoàng đế nước Pháp", "pos": "phrase"},
    # 4411: labor day
    {"ipa": "/ˈleɪbər deɪ/", "vi": "Ngày Quốc tế Lao động; lễ Lao động", "pos": "phrase"},
    # 4412: land resources
    {"ipa": "/lænd rɪˈsɔːrsɪz/", "vi": "tài nguyên đất đai quốc gia", "pos": "phrase"},
    # 4413: line score
    {"ipa": "/laɪn skɔːr/", "vi": "bảng tổng hợp điểm số hiệp đấu", "pos": "phrase"},
    # 4414: little joe
    {"ipa": "/ˈlɪtl dʒoʊ/", "vi": "điểm bốn nút trong trò đổ xúc xắc", "pos": "phrase"},
    # 4415: louis the far
    {"ipa": "/ˈluːɪs ðə fɑːr/", "vi": "vua Louis Đệ ngũ nước Pháp", "pos": "phrase"},
    # 4416: low mass
    {"ipa": "/loʊ mæs/", "vi": "thánh lễ đọc không có hát ca đoàn", "pos": "phrase"},
    # 4417: low status
    {"ipa": "/loʊ ˈsteɪtəs/", "vi": "địa vị thấp kém trong xã hội", "pos": "phrase"},
    # 4418: military band
    {"ipa": "/ˈmɪlətɛri bænd/", "vi": "đoàn quân nhạc; ban nhạc quân đội", "pos": "phrase"},
    # 4419: military operation
    {"ipa": "/ˈmɪlətɛri ˌɑːpəˈreɪʃən/", "vi": "chiến dịch tác chiến quân sự", "pos": "phrase"},
    # 4420: network army
    {"ipa": "/ˈnɛtwɜːrk ˈɑːrmi/", "vi": "đội quân mạng lưới trực tuyến", "pos": "phrase"},
    # 4421: new mexico
    {"ipa": "/nuː ˈmɛksɪkoʊ/", "vi": "tiểu bang New Mexico của nước Mỹ", "pos": "phrase"},
    # 4422: notice board
    {"ipa": "/ˈnoʊtɪs bɔːrd/", "vi": "bảng thông báo tin tức cơ quan", "pos": "phrase"},
    # 4423: old boy network
    {"ipa": "/oʊld bɔɪ ˈnɛtwɜːrk/", "vi": "mạng lưới quan hệ thân hữu ô dù", "pos": "phrase"},
    # 4424: order arms
    {"ipa": "/ˈɔːrdər ɑːrmz/", "vi": "khẩu lệnh hạ súng; tư thế hạ súng", "pos": "phrase"},
    # 4425: place bet
    {"ipa": "/pleɪs bɛt/", "vi": "đặt tiền cá cược; cược về đích nhì", "pos": "phrase"},
    # 4426: planning board
    {"ipa": "/ˈplænɪŋ bɔːrd/", "vi": "ban hoạch định quy hoạch dự án", "pos": "phrase"},
    # 4427: plant process
    {"ipa": "/plænt ˈprɑːsɛs/", "vi": "chồi nhánh cây; quá trình quang hợp", "pos": "phrase"},
    # 4428: political theory
    {"ipa": "/pəˈlɪtɪkl ˈθiːəri/", "vi": "lý luận chính trị; thuyết chính trị", "pos": "phrase"},
    # 4429: price competition
    {"ipa": "/praɪs ˌkɑːmpəˈtɪʃən/", "vi": "cạnh tranh về giá cả hàng hóa", "pos": "phrase"},
    # 4430: put option
    {"ipa": "/pʊt ˈɑːpʃən/", "vi": "hợp đồng quyền chọn bán chứng khoán", "pos": "phrase"},
    # 4431: raise up
    {"ipa": "/reɪz ʌp/", "vi": "nâng cao lên; đề bạt cất nhắc ai", "pos": "phrase"},
    # 4432: roll out
    {"ipa": "/roʊl aʊt/", "vi": "ra mắt sản phẩm mới; trải thảm ra", "pos": "phrase"},
    # 4433: roll up
    {"ipa": "/roʊl ʌp/", "vi": "cuộn tròn lại; xắn tay áo; tụ tập", "pos": "phrase"},
    # 4434: rose water
    {"ipa": "/roʊz ˈwɔːtər/", "vi": "nước hoa hồng chưng cất dưỡng da", "pos": "phrase"},
    # 4435: royal court
    {"ipa": "/ˈrɔɪəl kɔːrt/", "vi": "triều đình hoàng gia; cung đình vua", "pos": "phrase"},
    # 4436: safety match
    {"ipa": "/ˈseɪfti mætʃ/", "vi": "que diêm an toàn; que quẹt diêm", "pos": "phrase"},
    # 4437: selling point
    {"ipa": "/ˈsɛlɪŋ pɔɪnt/", "vi": "điểm độc đáo hút khách; ưu điểm bán", "pos": "phrase"},
    # 4438: sense of direction
    {"ipa": "/sɛns ʌv dəˈrɛkʃən/", "vi": "khả năng định hướng phương hướng", "pos": "phrase"},
    # 4439: social structure
    {"ipa": "/ˈsoʊʃl ˈstrʌktʃər/", "vi": "cơ cấu cấu trúc tổ chức xã hội", "pos": "phrase"},
    # 4440: sound unit
    {"ipa": "/saʊnd ˈjuːnɪt/", "vi": "đơn vị đo âm thanh; âm vị ngôn ngữ", "pos": "phrase"},
    # 4441: spot market
    {"ipa": "/spɑːt ˈmɑːrkɪt/", "vi": "thị trường giao dịch ngay tức thì", "pos": "phrase"},
    # 4442: summer sweet
    {"ipa": "/ˈsʌmər swiːt/", "vi": "cây thược dược thơm hoa trắng", "pos": "phrase"},
    # 4443: surface area
    {"ipa": "/ˈsɜːrfɪs ˈɛriə/", "vi": "diện tích bề mặt bao phủ vật thể", "pos": "phrase"},
    # 4444: tax collection
    {"ipa": "/tæks kəˈlɛkʃən/", "vi": "công tác thu thuế ngân sách công", "pos": "phrase"},
    # 4445: team spirit
    {"ipa": "/tiːm ˈspɪrɪt/", "vi": "tinh thần đồng đội gắn kết tập thể", "pos": "phrase"},
    # 4446: television show
    {"ipa": "/ˈtɛləvɪʒən ʃoʊ/", "vi": "chương trình truyền hình phát sóng", "pos": "phrase"},
    # 4447: ten percent
    {"ipa": "/tɛn pərˈsɛnt/", "vi": "mười phần trăm; một phần mười số", "pos": "phrase"},
    # 4448: thomas young
    {"ipa": "/ˈtɑːməs jʌŋ/", "vi": "nhà bác học Thomas Young nước Anh", "pos": "phrase"},
    # 4449: throw together
    {"ipa": "/θroʊ təˈɡɛðər/", "vi": "lắp ghép vội vàng; gộp chung lại", "pos": "phrase"},
    # 4450: town planning
    {"ipa": "/taʊn ˈplænɪŋ/", "vi": "quy hoạch đô thị; xây dựng thị trấn", "pos": "phrase"},
    # 4451: traffic control
    {"ipa": "/ˈtræfɪk kənˈtroʊl/", "vi": "điều khiển giao thông luồng xe", "pos": "phrase"},
    # 4452: traffic court
    {"ipa": "/ˈtræfɪk kɔːrt/", "vi": "tòa án xử lý vi phạm giao thông", "pos": "phrase"},
    # 4453: training ship
    {"ipa": "/ˈtreɪnɪŋ ʃɪp/", "vi": "tàu huấn luyện thủy thủ hải quân", "pos": "phrase"},
    # 4454: walking on air
    {"ipa": "/ˈwɔːkɪŋ ɑːn ɛr/", "vi": "vui sướng ngất ngây; lâng lâng bay", "pos": "phrase"},
    # 4455: want ad
    {"ipa": "/wɑːnt æd/", "vi": "mục rao vặt tìm việc tìm người", "pos": "phrase"},
    # 4456: wedding party
    {"ipa": "/ˈwɛdɪŋ ˈpɑːrti/", "vi": "tiệc cưới; đoàn rước dâu đám cưới", "pos": "phrase"},
    # 4457: white metal
    {"ipa": "/waɪt ˈmɛtl/", "vi": "hợp kim thiếc trắng chống ma sát", "pos": "phrase"},
    # 4458: prettied
    {"ipa": "/ˈprɪtid/", "vi": "đã làm đẹp; đã tô điểm xinh xắn", "pos": "verb"},
    # 4459: prettier
    {"ipa": "/ˈprɪtiər/", "vi": "xinh đẹp hơn; duyên dáng hơn", "pos": "adj"},
    # 4460: prettiest
    {"ipa": "/ˈprɪtiɪst/", "vi": "xinh đẹp nhất; duyên dáng nhất", "pos": "adj"},
    # 4461: across the nation
    {"ipa": "/əˈkrɔːs ðə ˈneɪʃən/", "vi": "trên khắp đất nước; trên toàn quốc", "pos": "phrase"},
    # 4462: action plant
    {"ipa": "/ˈækʃən plænt/", "vi": "cây xấu hổ cụp lá; cây trinh nữ", "pos": "phrase"},
    # 4463: african country
    {"ipa": "/ˈæfrɪkən ˈkʌntri/", "vi": "quốc gia thuộc lục địa châu Phi", "pos": "phrase"},
    # 4464: american civil war
    {"ipa": "/əˈmɛrɪkən ˈsɪvl wɔːr/", "vi": "cuộc Nội chiến Hoa Kỳ nam bắc", "pos": "phrase"},
    # 4465: animal order
    {"ipa": "/ˈænɪml ˈɔːrdər/", "vi": "bộ động vật trong sinh học", "pos": "phrase"},
    # 4466: application form
    {"ipa": "/ˌæplɪˈkeɪʃən fɔːrm/", "vi": "mẫu đơn xin nhập học đăng ký nộp", "pos": "phrase"},
    # 4467: at bay
    {"ipa": "/æt beɪ/", "vi": "bị dồn vào chân tường; bị dồn bí", "pos": "phrase"},
    # 4468: big cat
    {"ipa": "/bɪɡ kæt/", "vi": "động vật họ mèo lớn; hổ báo sư tử", "pos": "phrase"},
    # 4469: black african
    {"ipa": "/blæk ˈæfrɪkən/", "vi": "người châu Phi da đen bản xứ", "pos": "phrase"},
    # 4470: black felt cup
    {"ipa": "/blæk fɛlt kʌp/", "vi": "nấm nỉ đen chén nhỏ hình cốc", "pos": "phrase"},
    # 4471: body count
    {"ipa": "/ˈbɑːdi kaʊnt/", "vi": "số lượng thi thể chết; tử trận", "pos": "phrase"},
    # 4472: body structure
    {"ipa": "/ˈbɑːdi ˈstrʌktʃər/", "vi": "cấu trúc thân xác; hình thể cơ thể", "pos": "phrase"},
    # 4473: boy wonder
    {"ipa": "/bɔɪ ˈwʌndər/", "vi": "cậu bé thần đồng; thiếu niên kỳ tài", "pos": "phrase"},
    # 4474: capital of australia
    {"ipa": "/ˈkæpɪtl ʌv ɔːˈstreɪljə/", "vi": "thủ đô Canberra của nước Úc", "pos": "phrase"},
    # 4475: car seat
    {"ipa": "/kɑːr siːt/", "vi": "ghế ngồi ô tô; ghế xe hơi an toàn", "pos": "phrase"},
    # 4476: carry to term
    {"ipa": "/ˈkæri tuː tɜːrm/", "vi": "mang thai đủ tháng đến kỳ sinh nở", "pos": "phrase"},
    # 4477: cast away
    {"ipa": "/kæst əˈweɪ/", "vi": "vứt bỏ đi; trôi dạt vào đảo hoang", "pos": "phrase"},
    # 4478: catch fire
    {"ipa": "/kætʃ faɪər/", "vi": "bắt lửa bốc cháy đùng đùng", "pos": "phrase"},
    # 4479: cell phone
    {"ipa": "/sɛl foʊn/", "vi": "điện thoại di động; máy di động", "pos": "phrase"},
    # 4480: charge card
    {"ipa": "/tʃɑːrdʒ kɑːrd/", "vi": "thẻ thanh toán trả sau định kỳ", "pos": "phrase"},
    # 4481: chief justice
    {"ipa": "/tʃiːf ˈdʒʌstɪs/", "vi": "chánh án Tòa án Tối cao Hoa Kỳ", "pos": "phrase"},
    # 4482: christmas star
    {"ipa": "/ˈkrɪsməs stɑːr/", "vi": "hoa trạng nguyên; sao Bê-lem", "pos": "phrase"},
    # 4483: class structure
    {"ipa": "/klæs ˈstrʌktʃər/", "vi": "cơ cấu các giai cấp trong xã hội", "pos": "phrase"},
    # 4484: click open
    {"ipa": "/klɪk ˈoʊpən/", "vi": "nhấp chuột mở tệp; bật lẫy mở ra", "pos": "phrase"},
    # 4485: color tv
    {"ipa": "/ˈkʌlər ˌtiːˈviː/", "vi": "máy thu hình màu; tivi màu sắc", "pos": "phrase"},
    # 4486: common touch
    {"ipa": "/ˈkɑːmən tʌtʃ/", "vi": "sự gần gũi bình dân với người dân", "pos": "phrase"},
    # 4487: computer language
    {"ipa": "/kəmˈpjuːtər ˈlæŋɡwɪdʒ/", "vi": "ngôn ngữ lập trình cho máy vi tính", "pos": "phrase"},
    # 4488: computer technology
    {"ipa": "/kəmˈpjuːtər tɛkˈnɑːlədʒi/", "vi": "công nghệ máy tính kỹ thuật số", "pos": "phrase"},
    # 4489: conference table
    {"ipa": "/ˈkɑːnfərəns ˈteɪbl/", "vi": "chiếc bàn dài dùng họp hội nghị", "pos": "phrase"},
    # 4490: control surface
    {"ipa": "/kənˈtroʊl ˈsɜːrfɪs/", "vi": "bề mặt điều khiển lái cánh máy bay", "pos": "phrase"},
    # 4491: deep brown
    {"ipa": "/diːp braʊn/", "vi": "màu nâu sẫm thẫm; sắc nâu đậm", "pos": "phrase"},
    # 4492: defense policy
    {"ipa": "/dɪˈfɛns ˈpɑːləsi/", "vi": "chính sách quốc phòng an ninh", "pos": "phrase"},
    # 4493: draw the line
    {"ipa": "/drɔː ðə laɪn/", "vi": "vạch ra giới hạn; từ chối vượt quá", "pos": "phrase"},
    # 4494: dress down
    {"ipa": "/drɛs daʊn/", "vi": "mặc đồ giản dị; khiển trách gay gắt", "pos": "phrase"},
    # 4495: driving force
    {"ipa": "/ˈdraɪvɪŋ fɔːrs/", "vi": "động lực chính thúc đẩy phát triển", "pos": "phrase"},
    # 4496: dry out
    {"ipa": "/draɪ aʊt/", "vi": "khô khốc hoàn toàn; cai nghiện rượu", "pos": "phrase"},
    # 4497: dry up
    {"ipa": "/draɪ ʌp/", "vi": "khô cạn hoàn toàn; im bặt nín lặng", "pos": "phrase"},
    # 4498: east india company
    {"ipa": "/iːst ˈɪndiə ˈkʌmpəni/", "vi": "Công ty Đông Ấn Anh thuộc địa", "pos": "phrase"},
    # 4499: edge up
    {"ipa": "/ɛdʒ ʌp/", "vi": "nhích từng chút lên cao; tăng nhẹ", "pos": "phrase"}
]

with open("scratch/b21_r09_raw_p5.json", "r", encoding="utf-8") as f:
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

with open("scratch/b21_r09_p5.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(output)} entries for Round 9 Part 5.")
