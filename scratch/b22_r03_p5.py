import json

raw_items = json.load(open("scratch/b22_r03_raw_p5.json"))

reviews = [
    # 00: blow off
    {"pos": "phrase", "ipa": "/bloʊ ɔːf/", "vi": "thổi bay đi; phớt lờ trốn tránh"},
    # 01: bob hope
    {"pos": "phrase", "ipa": "/bɑːb hoʊp/", "vi": "danh hài Bob Hope"},
    # 02: body temperature
    {"pos": "phrase", "ipa": "/ˈbɑːdi ˈtɛmprətʃər/", "vi": "nhiệt độ cơ thể; thân nhiệt người"},
    # 03: bottom fish
    {"pos": "phrase", "ipa": "/ˈbɑːtəm fɪʃ/", "vi": "loài cá tầng đáy đại dương"},
    # 04: branch out
    {"pos": "phrase", "ipa": "/bræntʃ aʊt/", "vi": "mở rộng kinh doanh sang ngành mới"},
    # 05: business editor
    {"pos": "phrase", "ipa": "/ˈbɪznəs ˈɛdɪtər/", "vi": "biên tập viên chuyên mục kinh tế"},
    # 06: capital of florida
    {"pos": "phrase", "ipa": "/ˈkæpɪtl əv ˈflɔːrədə/", "vi": "thủ phủ bang Florida; Tallahassee"},
    # 07: capital of israel
    {"pos": "phrase", "ipa": "/ˈkæpɪtl əv ˈɪzriəl/", "vi": "thủ đô nước Israel; Jerusalem"},
    # 08: cell theory
    {"pos": "phrase", "ipa": "/sɛl ˈθiːəri/", "vi": "thuyết tế bào học sinh học"},
    # 09: centre spread
    {"pos": "phrase", "ipa": "/ˈsɛntər sprɛd/", "vi": "trang đôi chính giữa tờ báo"},
    # 10: chain saw
    {"pos": "phrase", "ipa": "/tʃeɪn sɔː/", "vi": "máy cưa xích cầm tay đốn gỗ"},
    # 11: chicken run
    {"pos": "phrase", "ipa": "/ˈtʃɪkɪn rʌn/", "vi": "sân rào quây nuôi gà thả vườn"},
    # 12: chief assistant
    {"pos": "phrase", "ipa": "/tʃiːf əˈsɪstənt/", "vi": "trợ lý chính; trợ tá trưởng"},
    # 13: child abuse
    {"pos": "phrase", "ipa": "/tʃaɪld əˈbjuːs/", "vi": "tội ngược đãi bạo hành trẻ em"},
    # 14: claim agent
    {"pos": "phrase", "ipa": "/kleɪm ˈeɪdʒənt/", "vi": "chuyên viên giám định bồi thường"},
    # 15: coffee shop
    {"pos": "phrase", "ipa": "/ˈkɔːfi ʃɑːp/", "vi": "quán cà phê; tiệm bán cà phê"},
    # 16: conversation piece
    {"pos": "phrase", "ipa": "/ˌkɑːnvərˈseɪʃn piːs/", "vi": "vật gợi đề tài trò chuyện độc đáo"},
    # 17: critical analysis
    {"pos": "phrase", "ipa": "/ˈkrɪtɪkl əˈnæləsɪs/", "vi": "phân tích phản biện phê phán"},
    # 18: door guard
    {"pos": "phrase", "ipa": "/dɔːr ɡɑːrd/", "vi": "người gác cửa; chốt an toàn cửa"},
    # 19: early bird
    {"pos": "phrase", "ipa": "/ˈɜːrli bɜːrd/", "vi": "người dậy sớm; khách đăng ký sớm"},
    # 20: electric range
    {"pos": "phrase", "ipa": "/ɪˈlɛktrɪk reɪndʒ/", "vi": "bếp điện nấu ăn gia đình"},
    # 21: entry word
    {"pos": "phrase", "ipa": "/ˈɛntri wɜːrd/", "vi": "mục từ chính đầu mục từ điển"},
    # 22: executive agency
    {"pos": "phrase", "ipa": "/ɪɡˈzɛkjətɪv ˈeɪdʒənsi/", "vi": "cơ quan trực thuộc nhánh hành pháp"},
    # 23: false face
    {"pos": "phrase", "ipa": "/fɔːls feɪs/", "vi": "mặt nạ hóa trang; bộ mặt giả tạo"},
    # 24: film writer
    {"pos": "phrase", "ipa": "/fɪlm ˈraɪtər/", "vi": "nhà biên kịch phim điện ảnh"},
    # 25: final payment
    {"pos": "phrase", "ipa": "/ˈfaɪnl ˈpeɪmənt/", "vi": "đợt thanh toán tất toán cuối cùng"},
    # 26: fish species
    {"pos": "phrase", "ipa": "/fɪʃ ˈspiːʃiːz/", "vi": "các loài cá thủy sản"},
    # 27: fly ball
    {"pos": "phrase", "ipa": "/flaɪ bɔːl/", "vi": "quả bóng bay bổng lên cao bóng chày"},
    # 28: follow suit
    {"pos": "phrase", "ipa": "/ˈfɑːloʊ suːt/", "vi": "làm theo gương; đánh bài cùng chất"},
    # 29: frame up
    {"pos": "phrase", "ipa": "/freɪm ʌp/", "vi": "gài bẫy vu khống dựng chuyện"},
    # 30: fuel oil
    {"pos": "phrase", "ipa": "/ˈfjuːəl ɔɪl/", "vi": "dầu nhiên liệu đốt lò FO"},
    # 31: german silver
    {"pos": "phrase", "ipa": "/ˈdʒɜːrmən ˈsɪlvər/", "vi": "hợp kim bạc Đức đồng niken kẽm"},
    # 32: ground crew
    {"pos": "phrase", "ipa": "/ɡraʊnd kruː/", "vi": "đội ngũ nhân viên mặt đất sân bay"},
    # 33: guard hair
    {"pos": "phrase", "ipa": "/ɡɑːrd hɛr/", "vi": "lớp lông bảo vệ phủ ngoài của thú"},
    # 34: gun mike
    {"pos": "phrase", "ipa": "/ɡʌn maɪk/", "vi": "micro định hướng thu âm tầm xa"},
    # 35: hand truck
    {"pos": "phrase", "ipa": "/hænd trʌk/", "vi": "xe đẩy hàng hai bánh bằng tay"},
    # 36: hang around
    {"pos": "phrase", "ipa": "/hæŋ əˈraʊnd/", "vi": "lảng vảng la cà loanh quanh"},
    # 37: hate mail
    {"pos": "phrase", "ipa": "/heɪt meɪl/", "vi": "thư thù ghét nặc danh đe dọa"},
    # 38: historical present
    {"pos": "phrase", "ipa": "/hɪˈstɔːrɪkl ˈprɛznt/", "vi": "thì hiện tại kể chuyện lịch sử"},
    # 39: holy saturday
    {"pos": "phrase", "ipa": "/ˈhoʊli ˈsætərdeɪ/", "vi": "Thứ Bảy Tuần Thánh Phục Sinh"},
    # 40: home reserve
    {"pos": "phrase", "ipa": "/hoʊm rɪˈzɜːrv/", "vi": "lực lượng quân đội dự bị quốc nội"},
    # 41: home territory
    {"pos": "phrase", "ipa": "/hoʊm ˈtɛrətɔːri/", "vi": "địa bàn cư trú lãnh thổ quê nhà"},
    # 42: house painting
    {"pos": "phrase", "ipa": "/haʊs ˈpeɪntɪŋ/", "vi": "nghề sơn nhà; công việc sơn tường"},
    # 43: in detail
    {"pos": "phrase", "ipa": "/ɪn dɪˈteɪl/", "vi": "tỉ mỉ tường tận; cặn kẽ chi tiết"},
    # 44: industrial management
    {"pos": "phrase", "ipa": "/ɪnˈdʌstriəl ˈmænɪdʒmənt/", "vi": "ngành quản lý công nghiệp sản xuất"},
    # 45: insurance agent
    {"pos": "phrase", "ipa": "/ɪnˈʃʊrəns ˈeɪdʒənt/", "vi": "đại lý tư vấn bảo hiểm nhân thọ"},
    # 46: kill zone
    {"pos": "phrase", "ipa": "/kɪl zoʊn/", "vi": "khu vực tiêu diệt phục kích đạn"},
    # 47: kingdom of god
    {"pos": "phrase", "ipa": "/ˈkɪŋdəm əv ɡɑːd/", "vi": "Nước Thiên Đàng của Thiên Chúa"},
    # 48: kitchen police
    {"pos": "phrase", "ipa": "/ˈkɪtʃɪn pəˈliːs/", "vi": "lính phụ trách tạp dịch nhà bếp KP"},
    # 49: language teaching
    {"pos": "phrase", "ipa": "/ˈlæŋɡwɪdʒ ˈtiːtʃɪŋ/", "vi": "giảng dạy ngôn ngữ ngoại ngữ"},
    # 50: language zone
    {"pos": "phrase", "ipa": "/ˈlæŋɡwɪdʒ zoʊn/", "vi": "vùng ngữ vực phân bố ngôn ngữ"},
    # 51: last mile
    {"pos": "phrase", "ipa": "/læst maɪl/", "vi": "chặng đường giao hàng cuối cùng"},
    # 52: left wing
    {"pos": "phrase", "ipa": "/lɛft wɪŋ/", "vi": "phe cánh tả; tiền đạo cánh trái"},
    # 53: line of vision
    {"pos": "phrase", "ipa": "/laɪn əv ˈvɪʒn/", "vi": "đường ngắm thẳng; trục tầm nhìn"},
    # 54: listed security
    {"pos": "phrase", "ipa": "/ˈlɪstɪd sɪˈkjʊrəti/", "vi": "chứng khoán niêm yết sàn giao dịch"},
    # 55: load up
    {"pos": "phrase", "ipa": "/loʊd ʌp/", "vi": "chất đầy hàng hóa lên; nạp đầy"},
    # 56: magic eye
    {"pos": "phrase", "ipa": "/ˈmædʒɪk aɪ/", "vi": "mắt thần điện tử; đèn chỉ thị sóng"},
    # 57: memory image
    {"pos": "phrase", "ipa": "/ˈmɛməri ˈɪmɪdʒ/", "vi": "hình ảnh lưu giữ trong trí nhớ"},
    # 58: natural shape
    {"pos": "phrase", "ipa": "/ˈnætʃrəl ʃeɪp/", "vi": "hình thái dáng vẻ tự nhiên vốn có"},
    # 59: net sales
    {"pos": "phrase", "ipa": "/nɛt seɪlz/", "vi": "doanh thu bán hàng thuần"},
    # 60: north korea
    {"pos": "phrase", "ipa": "/nɔːrθ kəˈriːə/", "vi": "nước Triều Tiên; Bắc Triều Tiên"},
    # 61: old salt
    {"pos": "phrase", "ipa": "/oʊld sɔːlt/", "vi": "thủy thủ già dày dạn kinh nghiệm"},
    # 62: operating table
    {"pos": "phrase", "ipa": "/ˈɑːpəreɪtɪŋ ˈteɪbl/", "vi": "bàn phẫu thuật phòng mổ"},
    # 63: orange group
    {"pos": "phrase", "ipa": "/ˈɔːrɪndʒ ɡruːp/", "vi": "tổ chức tôn giáo phái Cam Orange"},
    # 64: personal loan
    {"pos": "phrase", "ipa": "/ˈpɜːrsənl loʊn/", "vi": "vay tín chấp tiêu dùng cá nhân"},
    # 65: primary cell
    {"pos": "phrase", "ipa": "/ˈpraɪmɛri sɛl/", "vi": "pin sơ cấp không thể sạc lại"},
    # 66: primary sex character
    {"pos": "phrase", "ipa": "/ˈpraɪmɛri sɛks ˈkærəktər/", "vi": "đặc tính sinh dục sơ cấp bẩm sinh"},
    # 67: public relations person
    {"pos": "phrase", "ipa": "/ˈpʌblɪk rɪˈleɪʃnz ˈpɜːrsn/", "vi": "nhân viên chuyên viên PR công chúng"},
    # 68: red fox
    {"pos": "phrase", "ipa": "/rɛd fɑːks/", "vi": "con cáo lông đỏ Vulpes vulpes"},
    # 69: rent out
    {"pos": "phrase", "ipa": "/rɛnt aʊt/", "vi": "cho người khác thuê kiếm tiền"},
    # 70: river horse
    {"pos": "phrase", "ipa": "/ˈrɪvər hɔːrs/", "vi": "con hà mã khổng lồ sông nước"},
    # 71: rock and roll
    {"pos": "phrase", "ipa": "/rɑːk ænd roʊl/", "vi": "dòng nhạc rock and roll kinh điển"},
    # 72: rock beauty
    {"pos": "phrase", "ipa": "/rɑːk ˈbjuːti/", "vi": "loài cá bướm đá nhiệt đới"},
    # 73: room temperature
    {"pos": "phrase", "ipa": "/ruːm ˈtɛmprətʃər/", "vi": "nhiệt độ phòng thông thường"},
    # 74: row house
    {"pos": "phrase", "ipa": "/roʊ haʊs/", "vi": "dãy nhà phố liền kề san sát"},
    # 75: school newspaper
    {"pos": "phrase", "ipa": "/skuːl ˈnuːzpeɪpər/", "vi": "tờ báo nội bộ trường học học sinh"},
    # 76: science museum
    {"pos": "phrase", "ipa": "/ˈsaɪəns mjuˈziːəm/", "vi": "bảo tàng khoa học kỹ thuật"},
    # 77: side of meat
    {"pos": "phrase", "ipa": "/saɪd əv miːt/", "vi": "nửa tảng thịt xẻ dọc súc vật"},
    # 78: six pack
    {"pos": "phrase", "ipa": "/sɪks pæk/", "vi": "lốc 6 lon bia; cơ bụng sáu múi"},
    # 79: solid figure
    {"pos": "phrase", "ipa": "/ˈsɑːlɪd ˈfɪɡjər/", "vi": "hình khối không gian ba chiều học"},
    # 80: spring scale
    {"pos": "phrase", "ipa": "/sprɪŋ skeɪl/", "vi": "cái cân lò xo đo lực"},
    # 81: steel blue
    {"pos": "phrase", "ipa": "/stiːl bluː/", "vi": "sắc xám xanh màu thép nguội"},
    # 82: steel production
    {"pos": "phrase", "ipa": "/stiːl prəˈdʌkʃn/", "vi": "sản lượng chế tạo luyện kim thép"},
    # 83: table wine
    {"pos": "phrase", "ipa": "/ˈteɪbl waɪn/", "vi": "rượu vang thông thường uống kèm bữa"},
    # 84: time frame
    {"pos": "phrase", "ipa": "/taɪm freɪm/", "vi": "khung thời gian thực hiện dự án"},
    # 85: trading post
    {"pos": "phrase", "ipa": "/ˈtreɪdɪŋ poʊst/", "vi": "trạm giao thương trao đổi hàng hóa"},
    # 86: video display
    {"pos": "phrase", "ipa": "/ˈvɪdioʊ dɪˈspleɪ/", "vi": "màn hình hiển thị hình ảnh video"},
    # 87: voting system
    {"pos": "phrase", "ipa": "/ˈvoʊtɪŋ ˈsɪstəm/", "vi": "hệ thống bầu cử thể thức bỏ phiếu"},
    # 88: wake island
    {"pos": "phrase", "ipa": "/weɪk ˈaɪlənd/", "vi": "đảo san hô Wake của Hoa Kỳ"},
    # 89: waste material
    {"pos": "phrase", "ipa": "/weɪst məˈtɪriəl/", "vi": "chất thải; vật liệu phế thải"},
    # 90: waste of material
    {"pos": "phrase", "ipa": "/weɪst əv məˈtɪriəl/", "vi": "sự lãng phí vật tư nguyên liệu thô"},
    # 91: waste product
    {"pos": "phrase", "ipa": "/weɪst ˈprɑːdʌkt/", "vi": "sản phẩm phụ phế phẩm bỏ đi"},
    # 92: watch chain
    {"pos": "phrase", "ipa": "/wɑːtʃ tʃeɪn/", "vi": "sợi dây đeo đồng hồ bỏ túi quý tộc"},
    # 93: wedding band
    {"pos": "phrase", "ipa": "/ˈwɛdɪŋ bænd/", "vi": "nhẫn cưới trơn trao ngày hôn lễ"},
    # 94: weird sister
    {"pos": "phrase", "ipa": "/wɪrd ˈsɪstər/", "vi": "nữ thần vận mệnh; mụ phù thủy kỳ bí"},
    # 95: white pages
    {"pos": "phrase", "ipa": "/waɪt ˈpeɪdʒɪz/", "vi": "danh bạ trang trắng cá nhân"},
    # 96: writing arm
    {"pos": "phrase", "ipa": "/ˈraɪtɪŋ ɑːrm/", "vi": "tay ghế gắn bàn viết học sinh"},
    # 97: young bird
    {"pos": "phrase", "ipa": "/jʌŋ bɜːrd/", "vi": "chim non mới nở chưa biết bay"},
    # 98: youth culture
    {"pos": "phrase", "ipa": "/juːθ ˈkʌltʃər/", "vi": "văn hóa lối sống của giới trẻ"},
    # 99: aprils
    {"pos": "noun", "ipa": "/ˈeɪprəlz/", "vi": "những tháng Tư mùa xuân tươi đẹp"}
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

json.dump(out_items, open("scratch/b22_r03_p5.json", "w"), ensure_ascii=False, indent=2)
print("Round 3 Part 5 reviewed successfully: 100 items saved to scratch/b22_r03_p5.json")
