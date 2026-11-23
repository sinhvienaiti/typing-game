import json

# Manual word-by-word cognitive review for Batch 21 Round 9 Part 4 (records 4300-4399, IDs 200k.004302 to 200k.004401)
reviewed_entries = [
    # 4300: oil pressure
    {"ipa": "/ɔɪl ˈprɛʃər/", "vi": "áp suất dầu bôi trơn động cơ", "pos": "phrase"},
    # 4301: old bag
    {"ipa": "/oʊld bæɡ/", "vi": "mụ già cáu kỉnh; bà già khó tính", "pos": "phrase"},
    # 4302: on the fly
    {"ipa": "/ɑːn ðə flaɪ/", "vi": "khi đang di chuyển; làm tức thì", "pos": "phrase"},
    # 4303: outside marriage
    {"ipa": "/ˌaʊtˈsaɪd ˈmærɪdʒ/", "vi": "ngoài hôn nhân; con ngoài giá thú", "pos": "phrase"},
    # 4304: piece of paper
    {"ipa": "/piːs ʌv ˈpeɪpər/", "vi": "mảnh giấy; tờ giấy ghi chép", "pos": "phrase"},
    # 4305: piece of writing
    {"ipa": "/piːs ʌv ˈraɪtɪŋ/", "vi": "tác phẩm văn học; bài viết bút ký", "pos": "phrase"},
    # 4306: political machine
    {"ipa": "/pəˈlɪtɪkl məˈʃiːn/", "vi": "bộ máy chính trị đảng phái", "pos": "phrase"},
    # 4307: pop the question
    {"ipa": "/pɑːp ðə ˈkwɛstʃən/", "vi": "ngỏ lời cầu hôn; hỏi cưới bạn gái", "pos": "phrase"},
    # 4308: post exchange
    {"ipa": "/poʊst ɪksˈtʃeɪndʒ/", "vi": "cửa hàng bách hóa quân đội Mỹ", "pos": "phrase"},
    # 4309: prime number
    {"ipa": "/praɪm ˈnʌmbər/", "vi": "số nguyên tố trong toán học", "pos": "phrase"},
    # 4310: prison house
    {"ipa": "/ˈprɪzn haʊs/", "vi": "ngục thất giam giữ; cảnh tù đày", "pos": "phrase"},
    # 4311: public address system
    {"ipa": "/ˈpʌblɪk əˈdrɛs ˈsɪstəm/", "vi": "hệ thống loa phát thanh công cộng", "pos": "phrase"},
    # 4312: putting to death
    {"ipa": "/ˈpʊtɪŋ tuː dɛθ/", "vi": "việc xử tử hình; thi hành án tử", "pos": "phrase"},
    # 4313: real estate
    {"ipa": "/ˈriːəl ɪˈsteɪt/", "vi": "bất động sản; nhà đất địa ốc", "pos": "phrase"},
    # 4314: reality check
    {"ipa": "/riˈæləti tʃɛk/", "vi": "đối chiếu thực tế; hồi tỉnh thực tế", "pos": "phrase"},
    # 4315: roll in
    {"ipa": "/roʊl ɪn/", "vi": "đổ dồn về ào ạt; tiền cuồn cuộn vào", "pos": "phrase"},
    # 4316: sales staff
    {"ipa": "/seɪlz stæf/", "vi": "nhân viên phòng kinh doanh bán hàng", "pos": "phrase"},
    # 4317: senior moment
    {"ipa": "/ˈsiːnjər ˈmoʊmənt/", "vi": "khoảnh khắc đãng trí của tuổi già", "pos": "phrase"},
    # 4318: show window
    {"ipa": "/ʃoʊ ˈwɪndoʊ/", "vi": "tủ kính trưng bày hàng mẫu tiệm", "pos": "phrase"},
    # 4319: shut down
    {"ipa": "/ʃʌt daʊn/", "vi": "tắt máy; ngừng hoạt động nhà máy", "pos": "phrase"},
    # 4320: shut off
    {"ipa": "/ʃʌt ɔːf/", "vi": "khóa van ngắt nguồn; cắt nguồn cấp", "pos": "phrase"},
    # 4321: sick leave
    {"ipa": "/sɪk liːv/", "vi": "nghỉ phép ốm; thời gian nghỉ bệnh", "pos": "phrase"},
    # 4322: silver city
    {"ipa": "/ˈsɪlvər ˈsɪti/", "vi": "thành phố Silver City ở New Mexico", "pos": "phrase"},
    # 4323: simple eye
    {"ipa": "/ˈsɪmpl aɪ/", "vi": "mắt đơn ở loài côn trùng sâu bọ", "pos": "phrase"},
    # 4324: sitting room
    {"ipa": "/ˈsɪtɪŋ ruːm/", "vi": "phòng khách; phòng sinh hoạt chung", "pos": "phrase"},
    # 4325: small business administration
    {"ipa": "/smɔːl ˈbɪznəs ədˌmɪnɪˈstreɪʃən/", "vi": "Cơ quan Quản lý Doanh nghiệp nhỏ", "pos": "phrase"},
    # 4326: social activity
    {"ipa": "/ˈsoʊʃl ækˈtɪvəti/", "vi": "hoạt động giao lưu ngoài xã hội", "pos": "phrase"},
    # 4327: spot check
    {"ipa": "/spɑːt tʃɛk/", "vi": "kiểm tra đột xuất bất ngờ lấy mẫu", "pos": "phrase"},
    # 4328: staff officer
    {"ipa": "/stæf ˈɔːfɪsər/", "vi": "sĩ quan tham mưu cơ quan tác chiến", "pos": "phrase"},
    # 4329: standing room
    {"ipa": "/ˈstændɪŋ ruːm/", "vi": "chỗ đứng xem; khoảng trống đứng", "pos": "phrase"},
    # 4330: stick about
    {"ipa": "/stɪk əˈbaʊt/", "vi": "nán lại đợi; nấn ná luẩn quẩn gần", "pos": "phrase"},
    # 4331: stick by
    {"ipa": "/stɪk baɪ/", "vi": "trung thành kề vai; gắn bó sắt son", "pos": "phrase"},
    # 4332: stick out
    {"ipa": "/stɪk aʊt/", "vi": "nhô ra ngoài; lộ rõ nổi bật lên", "pos": "phrase"},
    # 4333: stick up
    {"ipa": "/stɪk ʌp/", "vi": "chĩa súng cướp của; dựng đứng lên", "pos": "phrase"},
    # 4334: stock issue
    {"ipa": "/stɑːk ˈɪʃuː/", "vi": "đợt phát hành cổ phiếu mới ra sàn", "pos": "phrase"},
    # 4335: stock of record
    {"ipa": "/stɑːk ʌv ˈrɛkərd/", "vi": "cổ phiếu được ghi nhận vào sổ sách", "pos": "phrase"},
    # 4336: student union
    {"ipa": "/ˈstuːdnt ˈjuːnjən/", "vi": "hội sinh viên; hội quán sinh viên", "pos": "phrase"},
    # 4337: summer stock
    {"ipa": "/ˈsʌmər stɑːk/", "vi": "các đoàn kịch lưu diễn mùa hè", "pos": "phrase"},
    # 4338: take advantage
    {"ipa": "/teɪk ədˈvæntɪdʒ/", "vi": "tận dụng cơ hội; lợi dụng lòng tốt", "pos": "phrase"},
    # 4339: take apart
    {"ipa": "/teɪk əˈpɑːrt/", "vi": "tháo dỡ rời ra; phê bình gay gắt", "pos": "phrase"},
    # 4340: take the fifth
    {"ipa": "/teɪk ðə fɪfθ/", "vi": "viện Tu chính án số năm giữ im lặng", "pos": "phrase"},
    # 4341: target company
    {"ipa": "/ˈtɑːrɡɪt ˈkʌmpəni/", "vi": "công ty mục tiêu bị thâu tóm", "pos": "phrase"},
    # 4342: tax income
    {"ipa": "/tæks ˈɪnkʌm/", "vi": "nguồn thu ngân sách từ thuế khóa", "pos": "phrase"},
    # 4343: try square
    {"ipa": "/traɪ skwɛr/", "vi": "thước vuông góc thợ mộc kiểm tra", "pos": "phrase"},
    # 4344: value statement
    {"ipa": "/ˈvæljuː ˈsteɪtmənt/", "vi": "bản tuyên bố giá trị cốt lõi", "pos": "phrase"},
    # 4345: voice box
    {"ipa": "/vɔɪs bɑːks/", "vi": "thanh quản cơ quan phát ra âm thanh", "pos": "phrase"},
    # 4346: wake up
    {"ipa": "/weɪk ʌp/", "vi": "thức dậy tỉnh giấc; làm tỉnh ngộ", "pos": "phrase"},
    # 4347: waste of money
    {"ipa": "/weɪst ʌv ˈmʌni/", "vi": "sự lãng phí tiền của vô ích", "pos": "phrase"},
    # 4348: west germany
    {"ipa": "/wɛst ˈdʒɜːrməni/", "vi": "nước Tây Đức Cộng hòa Liên bang Đức", "pos": "phrase"},
    # 4349: work in progress
    {"ipa": "/wɜːrk ɪn ˈprɑːɡrɛs/", "vi": "sản phẩm dở dang đang hoàn thiện", "pos": "phrase"},
    # 4350: write in code
    {"ipa": "/raɪt ɪn koʊd/", "vi": "viết bằng mật mã; viết mã bí mật", "pos": "phrase"},
    # 4351: written text
    {"ipa": "/ˈrɪtn tɛkst/", "vi": "văn bản viết ra; bản văn tự in ấn", "pos": "phrase"},
    # 4352: histories
    {"ipa": "/ˈhɪstəriz/", "vi": "các cuốn sử ký; những dòng lịch sử", "pos": "noun"},
    # 4353: larges
    {"ipa": "/ˈlɑːrdʒɪz/", "vi": "các cỡ áo lớn; kích thước cỡ bự", "pos": "noun"},
    # 4354: wronger
    {"ipa": "/ˈrɔːŋər/", "vi": "sai lầm hơn; không đúng đắn hơn", "pos": "adj"},
    # 4355: wrongest
    {"ipa": "/ˈrɔːŋɪst/", "vi": "sai lệch nhất; tồi tệ nhất", "pos": "adj"},
    # 4356: air division
    {"ipa": "/ɛr dɪˈvɪʒən/", "vi": "sư đoàn không quân chiến thuật", "pos": "phrase"},
    # 4357: air traffic
    {"ipa": "/ɛr ˈtræfɪk/", "vi": "lưu lượng máy bay trên không phận", "pos": "phrase"},
    # 4358: animal group
    {"ipa": "/ˈænɪml ɡruːp/", "vi": "nhóm động vật; bầy thú hoang dã", "pos": "phrase"},
    # 4359: army officer
    {"ipa": "/ˈɑːrmi ˈɔːfɪsər/", "vi": "sĩ quan lục quân; cán bộ quân đội", "pos": "phrase"},
    # 4360: art teacher
    {"ipa": "/ɑːrt ˈtiːtʃər/", "vi": "giáo viên mỹ thuật dạy vẽ tranh", "pos": "phrase"},
    # 4361: baby doctor
    {"ipa": "/ˈbeɪbi ˈdɑːktər/", "vi": "bác sĩ khoa nhi; thầy thuốc trẻ thơ", "pos": "phrase"},
    # 4362: break dance
    {"ipa": "/breɪk dæns/", "vi": "điệu nhảy bẻ người breakdance", "pos": "phrase"},
    # 4363: broken heart
    {"ipa": "/ˈbroʊkən hɑːrt/", "vi": "trái tim vỡ nát; cõi lòng tan nát", "pos": "phrase"},
    # 4364: building block
    {"ipa": "/ˈbɪldɪŋ blɑːk/", "vi": "viên gạch nền tảng; thành tố cơ bản", "pos": "phrase"},
    # 4365: bus line
    {"ipa": "/bʌs laɪn/", "vi": "tuyến xe buýt; lộ trình xe buýt", "pos": "phrase"},
    # 4366: bus service
    {"ipa": "/bʌs ˈsɜːrvɪs/", "vi": "dịch vụ vận tải xe buýt công cộng", "pos": "phrase"},
    # 4367: business agent
    {"ipa": "/ˈbɪznəs ˈeɪdʒənt/", "vi": "đại diện thương mại; đại diện thầu", "pos": "phrase"},
    # 4368: capital loss
    {"ipa": "/ˈkæpɪtl lɔːs/", "vi": "khoản lỗ vốn đầu tư; hao hụt vốn", "pos": "phrase"},
    # 4369: capital of washington
    {"ipa": "/ˈkæpɪtl ʌv ˈwɑːʃɪŋtən/", "vi": "thủ phủ Olympia của bang Washington", "pos": "phrase"},
    # 4370: card table
    {"ipa": "/kɑːrd ˈteɪbl/", "vi": "bàn chơi bài gấp gọn; bàn đánh bài", "pos": "phrase"},
    # 4371: cash account
    {"ipa": "/kæʃ əˈkaʊnt/", "vi": "tài khoản tiền mặt kế toán", "pos": "phrase"},
    # 4372: charles the great
    {"ipa": "/tʃɑːrlz ðə ɡreɪt/", "vi": "Đại đế Charlemagne nước Frank", "pos": "phrase"},
    # 4373: color force
    {"ipa": "/ˈkʌlər fɔːrs/", "vi": "lực tương tác mạnh giữa các quark", "pos": "phrase"},
    # 4374: come apart
    {"ipa": "/kʌm əˈpɑːrt/", "vi": "vỡ vụn ra; bung ra thành từng mảnh", "pos": "phrase"},
    # 4375: common multiple
    {"ipa": "/ˈkɑːmən ˈmʌltɪpl/", "vi": "bội số chung trong số học toán", "pos": "phrase"},
    # 4376: common stock
    {"ipa": "/ˈkɑːmən stɑːk/", "vi": "cổ phiếu phổ thông công ty cổ phần", "pos": "phrase"},
    # 4377: computer science
    {"ipa": "/kəmˈpjuːtər ˈsaɪəns/", "vi": "ngành khoa học máy tính thông tin", "pos": "phrase"},
    # 4378: cost analysis
    {"ipa": "/kɔːst əˈnæləsɪs/", "vi": "phân tích cơ cấu chi phí vận hành", "pos": "phrase"},
    # 4379: credit union
    {"ipa": "/ˈkrɛdɪt ˈjuːnjən/", "vi": "hợp tác xã tín dụng tài chính", "pos": "phrase"},
    # 4380: cross hair
    {"ipa": "/krɔːs hɛr/", "vi": "vạch chữ thập trong ống ngắm bắn", "pos": "phrase"},
    # 4381: daily double
    {"ipa": "/ˈdeɪli ˈdʌbl/", "vi": "kèo cá cược đúp hai cuộc đua ngựa", "pos": "phrase"},
    # 4382: double bed
    {"ipa": "/ˈdʌbl bɛd/", "vi": "giường ngủ đôi cho hai người nằm", "pos": "phrase"},
    # 4383: double door
    {"ipa": "/ˈdʌbl dɔːr/", "vi": "cửa đôi hai cánh mở rộng ra vào", "pos": "phrase"},
    # 4384: east german
    {"ipa": "/iːst ˈdʒɜːrmən/", "vi": "thuộc về Đông Đức; người Đông Đức", "pos": "phrase"},
    # 4385: edge in
    {"ipa": "/ɛdʒ ɪn/", "vi": "chen lấn len lỏi từng chút một vào", "pos": "phrase"},
    # 4386: expected value
    {"ipa": "/ɪkˈspɛktɪd ˈvæljuː/", "vi": "giá trị kỳ vọng trong thống kê toán", "pos": "phrase"},
    # 4387: farm out
    {"ipa": "/fɑːrm aʊt/", "vi": "khoán việc ra ngoài; giao thầu phụ", "pos": "phrase"},
    # 4388: feeling of movement
    {"ipa": "/ˈfiːlɪŋ ʌv ˈmuːvmənt/", "vi": "cảm giác vận động cơ thể vận động", "pos": "phrase"},
    # 4389: field trip
    {"ipa": "/fiːld trɪp/", "vi": "chuyến tham quan thực tế; dã ngoại", "pos": "phrase"},
    # 4390: fifth part
    {"ipa": "/fɪfθ pɑːrt/", "vi": "một phần năm; tỷ lệ một phần năm", "pos": "phrase"},
    # 4391: figure eight
    {"ipa": "/ˈfɪɡjər eɪt/", "vi": "hình số tám; đường trượt số tám", "pos": "phrase"},
    # 4392: figure of eight
    {"ipa": "/ˈfɪɡjər ʌv eɪt/", "vi": "nút thắt hình số tám; hình số tám", "pos": "phrase"},
    # 4393: file out
    {"ipa": "/faɪl aʊt/", "vi": "nối đuôi nhau bước ra hàng một", "pos": "phrase"},
    # 4394: finding of fact
    {"ipa": "/ˈfaɪndɪŋ ʌv fækt/", "vi": "kết luận về các tình tiết thực tế", "pos": "phrase"},
    # 4395: fit the bill
    {"ipa": "/fɪt ðə bɪl/", "vi": "đáp ứng đúng yêu cầu; vừa vặn hợp", "pos": "phrase"},
    # 4396: fix up
    {"ipa": "/fɪks ʌp/", "vi": "sửa chữa nâng cấp; dàn xếp việc", "pos": "phrase"},
    # 4397: for dear life
    {"ipa": "/fɔːr dɪr laɪf/", "vi": "chạy thục mạng cứu lấy mạng sống", "pos": "phrase"},
    # 4398: french region
    {"ipa": "/frɛntʃ ˈriːdʒən/", "vi": "vùng lãnh thổ hành chính nước Pháp", "pos": "phrase"},
    # 4399: government agent
    {"ipa": "/ˈɡʌvərnmənt ˈeɪdʒənt/", "vi": "đặc vụ chính phủ; thanh tra công vụ", "pos": "phrase"}
]

with open("scratch/b21_r09_raw_p4.json", "r", encoding="utf-8") as f:
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

with open("scratch/b21_r09_p4.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(output)} entries for Round 9 Part 4.")
