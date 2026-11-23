import json

# Manual word-by-word cognitive review for Batch 21 Round 8 Part 4 (records 3800-3899, IDs 200k.003802 to 200k.003901)
reviewed_entries = [
    # 3800: complex number
    {"ipa": "/ˈkɑːmplɛks ˈnʌmbər/", "vi": "số phức trong toán học", "pos": "phrase"},
    # 3801: computer program
    {"ipa": "/kəmˈpjuːtər ˈproʊɡræm/", "vi": "chương trình máy tính; phần mềm", "pos": "phrase"},
    # 3802: conference center
    {"ipa": "/ˈkɑːnfərəns ˈsɛntər/", "vi": "trung tâm hội nghị; hội thảo", "pos": "phrase"},
    # 3803: count down
    {"ipa": "/kaʊnt daʊn/", "vi": "đếm ngược thời gian", "pos": "phrase"},
    # 3804: credit account
    {"ipa": "/ˈkrɛdɪt əˈkaʊnt/", "vi": "tài khoản tín dụng mua chịu", "pos": "phrase"},
    # 3805: dead ahead
    {"ipa": "/dɛd əˈhɛd/", "vi": "ngay phía trước; thẳng phía trước", "pos": "phrase"},
    # 3806: double star
    {"ipa": "/ˈdʌbl stɑːr/", "vi": "ngôi sao đôi trong thiên văn", "pos": "phrase"},
    # 3807: draw back
    {"ipa": "/drɔː bæk/", "vi": "lùi lại; rút lui; nhược điểm", "pos": "phrase"},
    # 3808: drop shot
    {"ipa": "/drɑːp ʃɑːt/", "vi": "cú bỏ nhỏ ngắn qua lưới vợt", "pos": "phrase"},
    # 3809: earth science
    {"ipa": "/ɜːrθ ˈsaɪəns/", "vi": "khoa học Trái Đất; địa chất học", "pos": "phrase"},
    # 3810: east river
    {"ipa": "/iːst ˈrɪvər/", "vi": "sông East River ở New York", "pos": "phrase"},
    # 3811: eating house
    {"ipa": "/ˈiːtɪŋ haʊs/", "vi": "quán ăn bình dân; tiệm cơm", "pos": "phrase"},
    # 3812: eating place
    {"ipa": "/ˈiːtɪŋ pleɪs/", "vi": "địa điểm ăn uống; quán ăn", "pos": "phrase"},
    # 3813: fair sex
    {"ipa": "/fɛr sɛks/", "vi": "phái đẹp; nữ giới; giới phụ nữ", "pos": "phrase"},
    # 3814: family tree
    {"ipa": "/ˈfæməli triː/", "vi": "cây gia phả; phả hệ gia tộc", "pos": "phrase"},
    # 3815: food color
    {"ipa": "/fuːd ˈkʌlər/", "vi": "phẩm màu thực phẩm an toàn", "pos": "phrase"},
    # 3816: form letter
    {"ipa": "/fɔːrm ˈlɛtər/", "vi": "thư mẫu; thư gửi hàng loạt", "pos": "phrase"},
    # 3817: gold standard
    {"ipa": "/ɡoʊld ˈstændərd/", "vi": "bản vị vàng; chuẩn mực vàng", "pos": "phrase"},
    # 3818: good authority
    {"ipa": "/ɡʊd əˈθɔːrəti/", "vi": "nguồn tin cậy; căn cứ đích xác", "pos": "phrase"},
    # 3819: government agency
    {"ipa": "/ˈɡʌvərnmənt ˈeɪdʒənsi/", "vi": "cơ quan chính phủ; cơ quan nhà nước", "pos": "phrase"},
    # 3820: ground ball
    {"ipa": "/ɡraʊnd bɔːl/", "vi": "bóng lăn trên mặt đất bóng chày", "pos": "phrase"},
    # 3821: hair oil
    {"ipa": "/hɛr ɔɪl/", "vi": "dầu dưỡng tóc; dầu bóng bôi tóc", "pos": "phrase"},
    # 3822: hair style
    {"ipa": "/hɛr staɪl/", "vi": "kiểu tóc; mẫu tóc tạo kiểu", "pos": "phrase"},
    # 3823: head shop
    {"ipa": "/hɛd ʃɑːp/", "vi": "cửa hàng bán phụ kiện cần sa", "pos": "phrase"},
    # 3824: head teacher
    {"ipa": "/hɛd ˈtiːtʃər/", "vi": "hiệu trưởng nhà trường", "pos": "phrase"},
    # 3825: high holy day
    {"ipa": "/haɪ ˈhoʊli deɪ/", "vi": "đại lễ Do Thái giáo; ngày lễ thánh", "pos": "phrase"},
    # 3826: high wind
    {"ipa": "/haɪ wɪnd/", "vi": "cơn gió mạnh; gió giật cấp cao", "pos": "phrase"},
    # 3827: holy water
    {"ipa": "/ˈhoʊli ˈwɔːtər/", "vi": "nước thánh ban phước trong nhà thờ", "pos": "phrase"},
    # 3828: hotel plan
    {"ipa": "/hoʊˈtɛl plæn/", "vi": "chế độ bao ăn uống của khách sạn", "pos": "phrase"},
    # 3829: international organization
    {"ipa": "/ˌɪntərˈnæʃnəl ˌɔːrɡənəˈzeɪʃən/", "vi": "tổ chức liên chính phủ quốc tế", "pos": "phrase"},
    # 3830: jack off
    {"ipa": "/dʒæk ɔːf/", "vi": "tự thỏa mãn sinh lý; thủ dâm", "pos": "phrase"},
    # 3831: john cash
    {"ipa": "/dʒɑːn kæʃ/", "vi": "Johnny Cash; danh ca đồng quê Mỹ", "pos": "phrase"},
    # 3832: last mentioned
    {"ipa": "/læst ˈmɛnʃənd/", "vi": "người vừa nhắc tới; điều sau cùng", "pos": "phrase"},
    # 3833: lie around
    {"ipa": "/laɪ əˈraʊnd/", "vi": "nằm dài lười biếng; nằm vương vãi", "pos": "phrase"},
    # 3834: long tom
    {"ipa": "/lɔːŋ tɑːm/", "vi": "súng thần công nòng dài trên tàu", "pos": "phrase"},
    # 3835: market letter
    {"ipa": "/ˈmɑːrkɪt ˈlɛtər/", "vi": "bản tin phân tích thị trường vốn", "pos": "phrase"},
    # 3836: master class
    {"ipa": "/ˈmæstər klæs/", "vi": "lớp bồi dưỡng bậc thầy; lớp cao cấp", "pos": "phrase"},
    # 3837: medical officer
    {"ipa": "/ˈmɛdɪkl ˈɔːfɪsər/", "vi": "sĩ quan y tế; bác sĩ quân y", "pos": "phrase"},
    # 3838: mental home
    {"ipa": "/ˈmɛntl hoʊm/", "vi": "bệnh viện tâm thần; trại dưỡng thần", "pos": "phrase"},
    # 3839: military campaign
    {"ipa": "/ˈmɪlətɛri kæmˈpeɪn/", "vi": "chiến dịch hành quân quân sự", "pos": "phrase"},
    # 3840: music teacher
    {"ipa": "/ˈmjuːzɪk ˈtiːtʃər/", "vi": "giáo viên dạy nhạc; thầy giáo nhạc", "pos": "phrase"},
    # 3841: nine times
    {"ipa": "/naɪn taɪmz/", "vi": "chín lần; gấp chín lần số lượng", "pos": "phrase"},
    # 3842: note value
    {"ipa": "/noʊt ˈvæljuː/", "vi": "trường độ nốt nhạc; giá trị nốt", "pos": "phrase"},
    # 3843: paper cup
    {"ipa": "/ˈpeɪpər kʌp/", "vi": "cốc giấy dùng một lần; ly giấy", "pos": "phrase"},
    # 3844: past master
    {"ipa": "/pæst ˈmæstər/", "vi": "bậc thầy lão luyện; người sành sỏi", "pos": "phrase"},
    # 3845: perfect gas
    {"ipa": "/ˈpɜːrfɪkt ɡæs/", "vi": "chất khí lý tưởng trong nhiệt động", "pos": "phrase"},
    # 3846: piece of ground
    {"ipa": "/piːs ʌv ɡraʊnd/", "vi": "mảnh đất thửa đất nhỏ; khu đất", "pos": "phrase"},
    # 3847: plant order
    {"ipa": "/plænt ˈɔːrdər/", "vi": "bộ thực vật trong sinh học", "pos": "phrase"},
    # 3848: political leader
    {"ipa": "/pəˈlɪtɪkl ˈliːdər/", "vi": "lãnh tụ chính trị; nhà chính trị", "pos": "phrase"},
    # 3849: political unit
    {"ipa": "/pəˈlɪtɪkl ˈjuːnɪt/", "vi": "đơn vị hành chính chính trị", "pos": "phrase"},
    # 3850: pop group
    {"ipa": "/pɑːp ɡruːp/", "vi": "nhóm nhạc pop; ban nhạc đại chúng", "pos": "phrase"},
    # 3851: practice range
    {"ipa": "/ˈpræktɪs reɪndʒ/", "vi": "sân tập đánh golf; bãi tập bắn đạn", "pos": "phrase"},
    # 3852: product development
    {"ipa": "/ˈprɑːdʌkt dɪˈvɛləpmənt/", "vi": "nghiên cứu phát triển sản phẩm mới", "pos": "phrase"},
    # 3853: pull back
    {"ipa": "/pʊl bæk/", "vi": "rút quân về tuyến sau; thoái lui", "pos": "phrase"},
    # 3854: pull off
    {"ipa": "/pʊl ɔːf/", "vi": "giật phăng ra; làm nên việc lớn", "pos": "phrase"},
    # 3855: push back
    {"ipa": "/pʊʃ bæk/", "vi": "đẩy lùi lại; hoãn lịch; phản kháng", "pos": "phrase"},
    # 3856: queen city
    {"ipa": "/kwiːn ˈsɪti/", "vi": "thành phố lớn của bang; Queen City", "pos": "phrase"},
    # 3857: question master
    {"ipa": "/ˈkwɛstʃən ˈmæstər/", "vi": "người dẫn chương trình đố vui; MC", "pos": "phrase"},
    # 3858: religious school
    {"ipa": "/rɪˈlɪdʒəs skuːl/", "vi": "trường học tôn giáo; trường dòng xứ", "pos": "phrase"},
    # 3859: remain down
    {"ipa": "/rɪˈmeɪn daʊn/", "vi": "tiếp tục nằm yên; đo sàn sau đòn", "pos": "phrase"},
    # 3860: round table
    {"ipa": "/raʊnd ˈteɪbl/", "vi": "bàn đàm phán; hội nghị bàn tròn", "pos": "phrase"},
    # 3861: royal family
    {"ipa": "/ˈrɔɪəl ˈfæməli/", "vi": "hoàng gia vương thất; gia đình vua", "pos": "phrase"},
    # 3862: royal house
    {"ipa": "/ˈrɔɪəl haʊs/", "vi": "hoàng tộc vương triều; hoàng thất", "pos": "phrase"},
    # 3863: sales event
    {"ipa": "/seɪlz ɪˈvɛnt/", "vi": "sự kiện khuyến mãi; đợt hạ giá bán", "pos": "phrase"},
    # 3864: scale down
    {"ipa": "/skeɪl daʊn/", "vi": "giảm bớt quy mô; thu nhỏ kích cỡ", "pos": "phrase"},
    # 3865: scene of action
    {"ipa": "/siːn ʌv ˈækʃən/", "vi": "hiện trường xảy ra việc; nơi đọ sức", "pos": "phrase"},
    # 3866: sea green
    {"ipa": "/siː ɡriːn/", "vi": "màu xanh biển; sắc xanh lục biển", "pos": "phrase"},
    # 3867: senior class
    {"ipa": "/ˈsiːnjər klæs/", "vi": "khóa học cuối cấp; lớp năm cuối", "pos": "phrase"},
    # 3868: sick call
    {"ipa": "/sɪk kɔːl/", "vi": "giờ khám bệnh quân đội; lệnh báo ốm", "pos": "phrase"},
    # 3869: sign language
    {"ipa": "/saɪn ˈlæŋɡwɪdʒ/", "vi": "ngôn ngữ ký hiệu cho người điếc", "pos": "phrase"},
    # 3870: social disease
    {"ipa": "/ˈsoʊʃl dɪˈziːz/", "vi": "bệnh xã hội lây qua đường tình dục", "pos": "phrase"},
    # 3871: special contract
    {"ipa": "/ˈspɛʃl ˈkɑːntrækt/", "vi": "hợp đồng có đóng dấu niêm phong", "pos": "phrase"},
    # 3872: specific performance
    {"ipa": "/spəˈsɪfɪk pərˈfɔːrməns/", "vi": "buộc thực thi đúng theo hợp đồng", "pos": "phrase"},
    # 3873: spread over
    {"ipa": "/sprɛd ˈoʊvər/", "vi": "rải đều ra; phân bổ qua thời gian", "pos": "phrase"},
    # 3874: stage door
    {"ipa": "/steɪdʒ dɔːr/", "vi": "cửa sau nhà hát dành cho nghệ sĩ", "pos": "phrase"},
    # 3875: sweet talk
    {"ipa": "/swiːt tɔːk/", "vi": "lời dỗ ngọt; lời đường mật xu nịnh", "pos": "phrase"},
    # 3876: take arms
    {"ipa": "/teɪk ɑːrmz/", "vi": "cầm vũ khí chiến đấu; nổi dậy đánh", "pos": "phrase"},
    # 3877: tax base
    {"ipa": "/tæks beɪs/", "vi": "cơ sở tính thuế; giá trị chịu thuế", "pos": "phrase"},
    # 3878: third degree
    {"ipa": "/θɜːrd dɪˈɡriː/", "vi": "biện pháp tra khảo bức cung dã man", "pos": "phrase"},
    # 3879: top executive
    {"ipa": "/tɑːp ɪɡˈzɛkjətɪv/", "vi": "giám đốc điều hành cấp cao nhất", "pos": "phrase"},
    # 3880: track event
    {"ipa": "/træk ɪˈvɛnt/", "vi": "nội dung chạy trên đường đua", "pos": "phrase"},
    # 3881: tree house
    {"ipa": "/triː haʊs/", "vi": "ngôi nhà dựng trên cành cây cao", "pos": "phrase"},
    # 3882: tv station
    {"ipa": "/ˌtiːˈviː ˈsteɪʃən/", "vi": "đài phát sóng truyền hình; đài TV", "pos": "phrase"},
    # 3883: us secret service
    {"ipa": "/juː ɛs ˈsiːkrət ˈsɜːrvɪs/", "vi": "Sở Mật vụ Hoa Kỳ bảo vệ tổng thống", "pos": "phrase"},
    # 3884: war crime
    {"ipa": "/wɔːr kraɪm/", "vi": "tội ác chiến tranh chống loài người", "pos": "phrase"},
    # 3885: war machine
    {"ipa": "/wɔːr məˈʃiːn/", "vi": "cỗ máy chiến tranh của quân đội", "pos": "phrase"},
    # 3886: waste of time
    {"ipa": "/weɪst ʌv taɪm/", "vi": "sự lãng phí thời gian vô bổ", "pos": "phrase"},
    # 3887: western united states
    {"ipa": "/ˈwɛstərn juːˈnaɪtɪd steɪts/", "vi": "miền Tây nước Mỹ; miền Tây Hoa Kỳ", "pos": "phrase"},
    # 3888: whole life insurance
    {"ipa": "/hoʊl laɪf ɪnˈʃʊrəns/", "vi": "bảo hiểm nhân thọ trọn đời", "pos": "phrase"},
    # 3889: william tell
    {"ipa": "/ˈwɪljəm tɛl/", "vi": "danh thủ bắn nỏ William Tell", "pos": "phrase"},
    # 3890: wonder woman
    {"ipa": "/ˈwʌndər ˈwʊmən/", "vi": "nữ anh hùng; người phụ nữ tài ba", "pos": "phrase"},
    # 3891: writing style
    {"ipa": "/ˈraɪtɪŋ staɪl/", "vi": "phong cách hành văn; lối viết chữ", "pos": "phrase"},
    # 3892: written language
    {"ipa": "/ˈrɪtn ˈlæŋɡwɪdʒ/", "vi": "ngôn ngữ viết; chữ viết thể hiện", "pos": "phrase"},
    # 3893: you bet
    {"ipa": "/juː bɛt/", "vi": "chắc chắn rồi; hiển nhiên là vậy", "pos": "phrase"},
    # 3894: young fish
    {"ipa": "/jʌŋ fɪʃ/", "vi": "cá con; cá giống mới nở từ trứng", "pos": "phrase"},
    # 3895: against the wind
    {"ipa": "/əˈɡɛnst ðə wɪnd/", "vi": "ngược chiều gió thổi; nghịch gió", "pos": "phrase"},
    # 3896: american indian day
    {"ipa": "/əˈmɛrɪkən ˈɪndiən deɪ/", "vi": "ngày kỷ niệm Người Mỹ bản địa Da đỏ", "pos": "phrase"},
    # 3897: bad weather
    {"ipa": "/bæd ˈwɛðər/", "vi": "thời tiết xấu giông bão; trời xấu", "pos": "phrase"},
    # 3898: band saw
    {"ipa": "/bænd sɔː/", "vi": "máy cưa vòng dây kim loại cắt gỗ", "pos": "phrase"},
    # 3899: battle plan
    {"ipa": "/ˈbætl plæn/", "vi": "kế hoạch tác chiến; phương án đánh", "pos": "phrase"}
]

with open("scratch/b21_r08_raw_p4.json", "r", encoding="utf-8") as f:
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

with open("scratch/b21_r08_p4.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(output)} entries for Part 4.")
