import json

# Manual word-by-word cognitive review for Batch 21 Round 10 Part 1 (records 4500-4599, IDs 200k.004502 to 200k.004601)
reviewed_entries = [
    # 4500: eight ball
    {"ipa": "/eɪt bɔːl/", "vi": "bi số 8 bida; tình thế hiểm nghèo", "pos": "phrase"},
    # 4501: engine room
    {"ipa": "/ˈɛndʒɪn ruːm/", "vi": "buồng máy tàu; đầu tàu phát triển", "pos": "phrase"},
    # 4502: estate car
    {"ipa": "/ɪˈsteɪt kɑːr/", "vi": "xe ô tô cốp dài gia đình du lịch", "pos": "phrase"},
    # 4503: fire walking
    {"ipa": "/ˈfaɪər ˈwɔːkɪŋ/", "vi": "nghi thức đi trên than lửa hồng rực", "pos": "phrase"},
    # 4504: first aid
    {"ipa": "/fɜːrst eɪd/", "vi": "sơ cứu ban đầu; cấp cứu khẩn cấp", "pos": "phrase"},
    # 4505: football coach
    {"ipa": "/ˈfʊtbɔːl koʊtʃ/", "vi": "huấn luyện viên môn bóng đá", "pos": "phrase"},
    # 4506: form division
    {"ipa": "/fɔːrm dɪˈvɪʒən/", "vi": "ngành hình thái học sinh vật", "pos": "phrase"},
    # 4507: free spirit
    {"ipa": "/friː ˈspɪrɪt/", "vi": "tâm hồn tự do phóng khoáng tự tại", "pos": "phrase"},
    # 4508: fresh food
    {"ipa": "/frɛʃ fuːd/", "vi": "thực phẩm tươi mới; đồ ăn tươi ngon", "pos": "phrase"},
    # 4509: garden state
    {"ipa": "/ˈɡɑːrdn steɪt/", "vi": "bang Vườn; biệt hiệu New Jersey Mỹ", "pos": "phrase"},
    # 4510: george ii
    {"ipa": "/dʒɔːrdʒ ðə ˈsɛkənd/", "vi": "vua George Đệ nhị nước Anh", "pos": "phrase"},
    # 4511: grade point
    {"ipa": "/ɡreɪd pɔɪnt/", "vi": "điểm số học tập; điểm tích lũy GPA", "pos": "phrase"},
    # 4512: grand total
    {"ipa": "/ɡrænd ˈtoʊtl/", "vi": "tổng số toàn bộ; tổng cộng chung", "pos": "phrase"},
    # 4513: ground floor
    {"ipa": "/ɡraʊnd flɔːr/", "vi": "tầng trệt tòa nhà; tầng một mặt đất", "pos": "phrase"},
    # 4514: ground rule
    {"ipa": "/ɡraʊnd ruːl/", "vi": "quy tắc cơ bản; luật chơi trên sân", "pos": "phrase"},
    # 4515: hand to mouth
    {"ipa": "/hænd tuː maʊθ/", "vi": "sống qua ngày; được chăng hay chớ", "pos": "phrase"},
    # 4516: holy father
    {"ipa": "/ˈhoʊli ˈfɑːðər/", "vi": "Đức Thánh Cha; Giáo hoàng La Mã", "pos": "phrase"},
    # 4517: hot stock
    {"ipa": "/hɑːt stɑːk/", "vi": "cổ phiếu sốt giá hút dòng tiền sàn", "pos": "phrase"},
    # 4518: house cat
    {"ipa": "/haʊs kæt/", "vi": "mèo nhà nuôi; mèo nuôi trong nhà", "pos": "phrase"},
    # 4519: indian club
    {"ipa": "/ˈɪndiən klʌb/", "vi": "quả chùy tập thể dục dưỡng sinh", "pos": "phrase"},
    # 4520: iron out
    {"ipa": "/ˈaɪərn aʊt/", "vi": "tháo gỡ bất đồng; giải quyết êm đẹp", "pos": "phrase"},
    # 4521: keep apart
    {"ipa": "/kiːp əˈpɑːrt/", "vi": "giữ tách xa nhau; ngăn cách riêng", "pos": "phrase"},
    # 4522: labor of love
    {"ipa": "/ˈleɪbər ʌv lʌv/", "vi": "việc làm vì đam mê không vụ lợi", "pos": "phrase"},
    # 4523: like mad
    {"ipa": "/laɪk mæd/", "vi": "như điên cuồng; vô cùng dữ dội", "pos": "phrase"},
    # 4524: long island sound
    {"ipa": "/lɔːŋ ˈaɪlənd saʊnd/", "vi": "eo biển Long Island tại nước Mỹ", "pos": "phrase"},
    # 4525: market economy
    {"ipa": "/ˈmɑːrkɪt ɪˈkɑːnəmi/", "vi": "nền kinh tế thị trường cạnh tranh", "pos": "phrase"},
    # 4526: may apple
    {"ipa": "/meɪ ˈæpl/", "vi": "cây táo tháng năm; cây độc mayapple", "pos": "phrase"},
    # 4527: mental health
    {"ipa": "/ˈmɛntl hɛlθ/", "vi": "sức khỏe tâm thần; tâm lý lành mạnh", "pos": "phrase"},
    # 4528: military commission
    {"ipa": "/ˈmɪlətɛri kəˈmɪʃən/", "vi": "tòa án quân sự; sắc lệnh thụ phong", "pos": "phrase"},
    # 4529: multiple star
    {"ipa": "/ˈmʌltɪpl stɑːr/", "vi": "hệ đa sao trong vũ trụ thiên văn", "pos": "phrase"},
    # 4530: natural ability
    {"ipa": "/ˈnætʃrəl əˈbɪləti/", "vi": "tài năng bẩm sinh; thiên phú sẵn có", "pos": "phrase"},
    # 4531: north channel
    {"ipa": "/nɔːrθ ˈtʃænl/", "vi": "eo biển Bắc ngăn cách xứ Ireland", "pos": "phrase"},
    # 4532: on guard
    {"ipa": "/ɑːn ɡɑːrd/", "vi": "luôn cảnh giác đề phòng; canh gác", "pos": "phrase"},
    # 4533: one iron
    {"ipa": "/wʌn ˈaɪərn/", "vi": "gậy sắt số 1 môn thể thao đánh golf", "pos": "phrase"},
    # 4534: paying back
    {"ipa": "/ˈpeɪɪŋ bæk/", "vi": "hoàn trả nợ nần; trả đũa báo thù", "pos": "phrase"},
    # 4535: physical value
    {"ipa": "/ˈfɪzɪkl ˈvæljuː/", "vi": "giá trị hữu hình; giá trị vật chất", "pos": "phrase"},
    # 4536: piece of eight
    {"ipa": "/piːs ʌv eɪt/", "vi": "đồng bạc tám hào cổ Tây Ban Nha", "pos": "phrase"},
    # 4537: plant department
    {"ipa": "/plænt dɪˈpɑːrtmənt/", "vi": "phòng quản lý máy móc nhà xưởng", "pos": "phrase"},
    # 4538: political economy
    {"ipa": "/pəˈlɪtɪkl ɪˈkɑːnəmi/", "vi": "kinh tế chính trị học chuyên ngành", "pos": "phrase"},
    # 4539: pop art
    {"ipa": "/pɑːp ɑːrt/", "vi": "nghệ thuật đại chúng Pop Art", "pos": "phrase"},
    # 4540: private security force
    {"ipa": "/ˈpraɪvət sɪˈkjʊrəti fɔːrs/", "vi": "lực lượng vệ sĩ an ninh tư nhân", "pos": "phrase"},
    # 4541: professional association
    {"ipa": "/prəˈfɛʃənl əˌsoʊsiˈeɪʃən/", "vi": "hiệp hội nghề nghiệp chuyên gia", "pos": "phrase"},
    # 4542: pull together
    {"ipa": "/pʊl təˈɡɛðər/", "vi": "chung sức đồng lòng; trấn tĩnh lại", "pos": "phrase"},
    # 4543: read method
    {"ipa": "/rɛd ˈmɛθəd/", "vi": "phương pháp sinh con tự nhiên Read", "pos": "phrase"},
    # 4544: reading material
    {"ipa": "/ˈriːdɪŋ məˈtɪriəl/", "vi": "tài liệu dùng để đọc; sách báo đọc", "pos": "phrase"},
    # 4545: red heat
    {"ipa": "/rɛd hiːt/", "vi": "nhiệt độ đỏ lửa; cơn giận dữ tột độ", "pos": "phrase"},
    # 4546: return address
    {"ipa": "/rɪˈtɜːrn əˈdrɛs/", "vi": "địa chỉ người gửi trả lại thư", "pos": "phrase"},
    # 4547: rise to power
    {"ipa": "/raɪz tuː ˈpaʊər/", "vi": "vươn lên nắm quyền lực tối cao", "pos": "phrase"},
    # 4548: risk capital
    {"ipa": "/rɪsk ˈkæpɪtl/", "vi": "vốn đầu tư mạo hiểm rủi ro cao", "pos": "phrase"},
    # 4549: roll over
    {"ipa": "/roʊl ˈoʊvər/", "vi": "lăn lộn mình; gia hạn khoản vay", "pos": "phrase"},
    # 4550: rule of evidence
    {"ipa": "/ruːl ʌv ˈɛvɪdəns/", "vi": "quy tắc chấp nhận chứng cứ tòa án", "pos": "phrase"},
    # 4551: secret society
    {"ipa": "/ˈsiːkrət səˈsaɪəti/", "vi": "hội kín ngầm; giáo phái bí mật", "pos": "phrase"},
    # 4552: sense of touch
    {"ipa": "/sɛns ʌv tʌtʃ/", "vi": "xúc giác; cảm nhận qua va chạm da", "pos": "phrase"},
    # 4553: set in stone
    {"ipa": "/sɛt ɪn stoʊn/", "vi": "bất di bất dịch; khắc cốt ghi tâm", "pos": "phrase"},
    # 4554: shoot for
    {"ipa": "/ʃuːt fɔːr/", "vi": "hướng tới mục tiêu; phấn đấu đạt", "pos": "phrase"},
    # 4555: short division
    {"ipa": "/ʃɔːrt dɪˈvɪʒən/", "vi": "phép chia nhẩm rút gọn số học", "pos": "phrase"},
    # 4556: sick list
    {"ipa": "/sɪk lɪst/", "vi": "danh sách người ốm nghỉ làm việc", "pos": "phrase"},
    # 4557: skin test
    {"ipa": "/skɪn tɛst/", "vi": "xét nghiệm dị ứng phản ứng qua da", "pos": "phrase"},
    # 4558: south wind
    {"ipa": "/saʊθ wɪnd/", "vi": "ngọn gió thổi từ phương nam tới", "pos": "phrase"},
    # 4559: speech community
    {"ipa": "/spiːtʃ kəˈmjuːnəti/", "vi": "cộng đồng ngôn ngữ cùng tiếng nói", "pos": "phrase"},
    # 4560: spirit away
    {"ipa": "/ˈspɪrɪt əˈweɪ/", "vi": "bí mật bắt cóc đem đi mất tích", "pos": "phrase"},
    # 4561: sports meeting
    {"ipa": "/spɔːrts ˈmiːtɪŋ/", "vi": "đại hội thể thao; hội thao thi đấu", "pos": "phrase"},
    # 4562: spot price
    {"ipa": "/spɑːt praɪs/", "vi": "giá giao dịch ngay tại chỗ sàn", "pos": "phrase"},
    # 4563: spread head
    {"ipa": "/sprɛd hɛd/", "vi": "tiêu đề bài báo dàn rộng nhiều cột", "pos": "phrase"},
    # 4564: spring break
    {"ipa": "/sprɪŋ breɪk/", "vi": "kỳ nghỉ mùa xuân của sinh viên Mỹ", "pos": "phrase"},
    # 4565: spring training
    {"ipa": "/sprɪŋ ˈtreɪnɪŋ/", "vi": "đợt tập huấn mùa xuân bóng chày", "pos": "phrase"},
    # 4566: stage manager
    {"ipa": "/steɪdʒ ˈmænɪdʒər/", "vi": "người quản lý chỉ huy sân khấu kịch", "pos": "phrase"},
    # 4567: state of israel
    {"ipa": "/steɪt ʌv ˈɪzriəl/", "vi": "Nhà nước Israel tại vùng Trung Đông", "pos": "phrase"},
    # 4568: street drug
    {"ipa": "/striːt drʌɡ/", "vi": "ma túy buôn bán bất hợp pháp vỉa hè", "pos": "phrase"},
    # 4569: strong drink
    {"ipa": "/strɔːŋ drɪŋk/", "vi": "rượu nặng độ cồn cao; rượu mạnh", "pos": "phrase"},
    # 4570: supply line
    {"ipa": "/səˈplaɪ laɪn/", "vi": "tuyến đường tiếp tế hậu cần quân sự", "pos": "phrase"},
    # 4571: take turns
    {"ipa": "/teɪk tɜːrnz/", "vi": "lần lượt thay phiên nhau làm việc", "pos": "phrase"},
    # 4572: target area
    {"ipa": "/ˈtɑːrɡɪt ˈɛriə/", "vi": "khu vực mục tiêu nhắm bắn tác chiến", "pos": "phrase"},
    # 4573: television set
    {"ipa": "/ˈtɛləvɪʒən sɛt/", "vi": "máy thu hình vô tuyến; chiếc tivi", "pos": "phrase"},
    # 4574: the likes of
    {"ipa": "/ðə laɪks ʌv/", "vi": "những đối tượng như; hạng người như", "pos": "phrase"},
    # 4575: traffic light
    {"ipa": "/ˈtræfɪk laɪt/", "vi": "hệ thống đèn tín hiệu giao thông", "pos": "phrase"},
    # 4576: unit trust
    {"ipa": "/ˈjuːnɪt trʌst/", "vi": "quỹ ủy thác đầu tư tương hỗ", "pos": "phrase"},
    # 4577: wall rock
    {"ipa": "/wɔːl rɑːk/", "vi": "đá vách ngăn kề cận mạch khoáng sản", "pos": "phrase"},
    # 4578: watch glass
    {"ipa": "/wɑːtʃ ɡlæs/", "vi": "mặt kính đồng hồ; đĩa mặt kính", "pos": "phrase"},
    # 4579: water supply
    {"ipa": "/ˈwɔːtər səˈplaɪ/", "vi": "nguồn cấp nước sạch đô thị dân sinh", "pos": "phrase"},
    # 4580: week from monday
    {"ipa": "/wiːk frʌm ˈmʌndeɪ/", "vi": "thứ Hai của tuần tới nữa", "pos": "phrase"},
    # 4581: west coast
    {"ipa": "/wɛst koʊst/", "vi": "vùng Bờ Tây Thái Bình Dương nước Mỹ", "pos": "phrase"},
    # 4582: western australia
    {"ipa": "/ˈwɛstərn ɔːˈstreɪljə/", "vi": "tiểu bang Tây Úc rộng lớn", "pos": "phrase"},
    # 4583: wonder boy
    {"ipa": "/ˈwʌndər bɔɪ/", "vi": "chàng trai thần đồng kỳ tài", "pos": "phrase"},
    # 4584: word of advice
    {"ipa": "/wɜːrd ʌv ədˈvaɪs/", "vi": "lời khuyên chân thành bảo ban", "pos": "phrase"},
    # 4585: bitted
    {"ipa": "/ˈbɪtɪd/", "vi": "đã tra hàm thiếc cương cho ngựa", "pos": "verb"},
    # 4586: bitting
    {"ipa": "/ˈbɪtɪŋ/", "vi": "tra hàm thiếc ngựa; cắt rãnh chìa", "pos": "verb"},
    # 4587: hits
    {"ipa": "/hɪts/", "vi": "các cú đánh trúng; bài hát ăn khách", "pos": "noun"},
    # 4588: nicer
    {"ipa": "/ˈnaɪsər/", "vi": "tốt đẹp hơn; tử tế hơn; xinh hơn", "pos": "adj"},
    # 4589: nicest
    {"ipa": "/ˈnaɪsɪst/", "vi": "tốt đẹp nhất; tử tế nhất; xinh nhất", "pos": "adj"},
    # 4590: sayings
    {"ipa": "/ˈseɪɪŋz/", "vi": "các câu châm ngôn; lời tục ngữ xưa", "pos": "noun"},
    # 4591: understands
    {"ipa": "/ˌʌndərˈstændz/", "vi": "hiểu rõ; thấu cảm; nắm được ý", "pos": "verb"},
    # 4592: yorks
    {"ipa": "/jɔːrks/", "vi": "những thành viên nhà York nước Anh", "pos": "noun"},
    # 4593: active trust
    {"ipa": "/ˈæktɪv trʌst/", "vi": "sự ủy thác tích cực có điều hành", "pos": "phrase"},
    # 4594: animal black
    {"ipa": "/ˈænɪml blæk/", "vi": "chất đen than xương động vật", "pos": "phrase"},
    # 4595: application program
    {"ipa": "/ˌæplɪˈkeɪʃən ˈproʊɡræm/", "vi": "phần mềm ứng dụng máy tính cá nhân", "pos": "phrase"},
    # 4596: arms control
    {"ipa": "/ɑːrmz kənˈtroʊl/", "vi": "kiểm soát cắt giảm vũ khí trang bị", "pos": "phrase"},
    # 4597: board foot
    {"ipa": "/bɔːrd fʊt/", "vi": "đơn vị đo thể tích gỗ xẻ ván", "pos": "phrase"},
    # 4598: book agent
    {"ipa": "/bʊk ˈeɪdʒənt/", "vi": "đại lý phát hành sách xuất bản", "pos": "phrase"},
    # 4599: boss around
    {"ipa": "/bɔːs əˈraʊnd/", "vi": "hách dịch sai bảo; chỉ tay năm ngón", "pos": "phrase"}
]

with open("scratch/b21_r10_raw_p1.json", "r", encoding="utf-8") as f:
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

with open("scratch/b21_r10_p1.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(output)} entries for Round 10 Part 1.")
