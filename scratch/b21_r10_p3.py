import json

# Manual word-by-word cognitive review for Batch 21 Round 10 Part 3 (records 4700-4799, IDs 200k.004702 to 200k.004801)
reviewed_entries = [
    # 4700: television system
    {"ipa": "/ˈtɛləvɪʒən ˈsɪstəm/", "vi": "hệ thống truyền hình vô tuyến", "pos": "phrase"},
    # 4701: town hall
    {"ipa": "/taʊn hɔːl/", "vi": "tòa thị chính; trụ sở thị trấn", "pos": "phrase"},
    # 4702: train oil
    {"ipa": "/treɪn ɔɪl/", "vi": "dầu cá voi đun thắp sáng xưa", "pos": "phrase"},
    # 4703: two iron
    {"ipa": "/tuː ˈaɪərn/", "vi": "gậy sắt số 2 trong bộ gậy golf", "pos": "phrase"},
    # 4704: unit character
    {"ipa": "/ˈjuːnɪt ˈkærəktər/", "vi": "tính trạng đơn vị di truyền Mendel", "pos": "phrase"},
    # 4705: united nations
    {"ipa": "/juːˈnaɪtɪd ˈneɪʃənz/", "vi": "Liên Hợp Quốc; tổ chức LHQ", "pos": "phrase"},
    # 4706: united states congress
    {"ipa": "/juːˈnaɪtɪd steɪts ˈkɑːŋɡrəs/", "vi": "Quốc hội Hợp chúng quốc Hoa Kỳ", "pos": "phrase"},
    # 4707: university of chicago
    {"ipa": "/ˌjuːnɪˈvɜːrsəti ʌv ʃɪˈkɑːɡoʊ/", "vi": "Viện Đại học Chicago danh tiếng", "pos": "phrase"},
    # 4708: university of paris
    {"ipa": "/ˌjuːnɪˈvɜːrsəti ʌv ˈpærɪs/", "vi": "Viện Đại học Paris Sorbonne Pháp", "pos": "phrase"},
    # 4709: water spirit
    {"ipa": "/ˈwɔːtər ˈspɪrɪt/", "vi": "thần nước; tinh linh dưới nước", "pos": "phrase"},
    # 4710: wear round
    {"ipa": "/wɛr raʊnd/", "vi": "lái thuyền quay mũi xuôi chiều gió", "pos": "phrase"},
    # 4711: western culture
    {"ipa": "/ˈwɛstərn ˈkʌltʃər/", "vi": "nền văn hóa phương Tây Âu Mỹ", "pos": "phrase"},
    # 4712: word meaning
    {"ipa": "/wɜːrd ˈmiːnɪŋ/", "vi": "ngữ nghĩa của từ vựng; nghĩa từ", "pos": "phrase"},
    # 4713: working memory
    {"ipa": "/ˈwɜːrkɪŋ ˈmɛməri/", "vi": "trí nhớ ngắn hạn; trí nhớ làm việc", "pos": "phrase"},
    # 4714: classed
    {"ipa": "/klæst/", "vi": "đã xếp loại; đã phân hạng đẳng cấp", "pos": "verb"},
    # 4715: classes
    {"ipa": "/ˈklæsɪz/", "vi": "các lớp học; các tầng lớp xã hội", "pos": "noun"},
    # 4716: classing
    {"ipa": "/ˈklæsɪŋ/", "vi": "đang xếp loại; đang phân hạng lớp", "pos": "verb"},
    # 4717: ideas
    {"ipa": "/aɪˈdiːəz/", "vi": "các ý tưởng sáng tạo; những ý niệm", "pos": "noun"},
    # 4718: pasts
    {"ipa": "/pæsts/", "vi": "những chuỗi quá khứ dĩ vãng đã qua", "pos": "noun"},
    # 4719: possibles
    {"ipa": "/ˈpɑːsəblz/", "vi": "những khả năng tiềm năng có thể", "pos": "noun"},
    # 4720: account executive
    {"ipa": "/əˈkaʊnt ɪɡˈzɛkjətɪv/", "vi": "chuyên viên quản lý khách hàng AE", "pos": "phrase"},
    # 4721: air force officer
    {"ipa": "/ɛr fɔːrs ˈɔːfɪsər/", "vi": "sĩ quan lực lượng không quân", "pos": "phrase"},
    # 4722: american sign language
    {"ipa": "/əˈmɛrɪkən saɪn ˈlæŋɡwɪdʒ/", "vi": "ngôn ngữ ký hiệu Mỹ chuẩn ASL", "pos": "phrase"},
    # 4723: baby sitting
    {"ipa": "/ˈbeɪbi ˈsɪtɪŋ/", "vi": "việc giữ trẻ; trông nom trẻ em", "pos": "phrase"},
    # 4724: basic english
    {"ipa": "/ˈbeɪsɪk ˈɪŋɡlɪʃ/", "vi": "tiếng Anh cơ bản giản lược 850 từ", "pos": "phrase"},
    # 4725: basic training
    {"ipa": "/ˈbeɪsɪk ˈtreɪnɪŋ/", "vi": "khóa huấn luyện tân binh quân sự", "pos": "phrase"},
    # 4726: bear on
    {"ipa": "/bɛr ɑːn/", "vi": "ảnh hưởng tới; tác động liên quan", "pos": "phrase"},
    # 4727: big stick
    {"ipa": "/bɪɡ stɪk/", "vi": "chính sách cây gậy lớn đe dọa", "pos": "phrase"},
    # 4728: body and soul
    {"ipa": "/ˈbɑːdi ænd soʊl/", "vi": "cả thể xác lẫn tâm hồn; hết lòng", "pos": "phrase"},
    # 4729: body waste
    {"ipa": "/ˈbɑːdi weɪst/", "vi": "chất thải bài tiết từ cơ thể", "pos": "phrase"},
    # 4730: breaking off
    {"ipa": "/ˈbreɪkɪŋ ɔːf/", "vi": "sự bẻ gãy; việc chấm dứt quan hệ", "pos": "phrase"},
    # 4731: car window
    {"ipa": "/kɑːr ˈwɪndoʊ/", "vi": "cửa kính xe ô tô; cửa sổ xe hơi", "pos": "phrase"},
    # 4732: central africa
    {"ipa": "/ˈsɛntrəl ˈæfrɪkə/", "vi": "khu vực Trung Phi; xứ Trung Phi", "pos": "phrase"},
    # 4733: christmas green
    {"ipa": "/ˈkrɪsməs ɡriːn/", "vi": "cành lá xanh trang trí Giáng sinh", "pos": "phrase"},
    # 4734: complex body part
    {"ipa": "/ˈkɑːmplɛks ˈbɑːdi pɑːrt/", "vi": "bộ phận cơ thể cấu tạo phức tạp", "pos": "phrase"},
    # 4735: corner man
    {"ipa": "/ˈkɔːrnər mæn/", "vi": "trợ lý góc võ đài quyền anh", "pos": "phrase"},
    # 4736: cover letter
    {"ipa": "/ˈkʌvər ˈlɛtər/", "vi": "thư ứng tuyển xin việc làm gửi kèm", "pos": "phrase"},
    # 4737: digital watch
    {"ipa": "/ˈdɪdʒɪtl wɑːtʃ/", "vi": "đồng hồ đeo tay hiển thị điện tử", "pos": "phrase"},
    # 4738: direct evidence
    {"ipa": "/dəˈrɛkt ˈɛvɪdəns/", "vi": "chứng cứ trực tiếp trong phiên tòa", "pos": "phrase"},
    # 4739: direct tax
    {"ipa": "/dəˈrɛkt tæks/", "vi": "thuế trực thu đánh vào thu nhập", "pos": "phrase"},
    # 4740: direct trust
    {"ipa": "/dəˈrɛkt trʌst/", "vi": "sự ủy thác rõ ràng minh bạch", "pos": "phrase"},
    # 4741: drop the ball
    {"ipa": "/drɑːp ðə bɔːl/", "vi": "mắc sai lầm tai hại; làm hỏng việc", "pos": "phrase"},
    # 4742: east germany
    {"ipa": "/iːst ˈdʒɜːrməni/", "vi": "nước Cộng hòa Dân chủ Đức Đông Đức", "pos": "phrase"},
    # 4743: english teacher
    {"ipa": "/ˈɪŋɡlɪʃ ˈtiːtʃər/", "vi": "giáo viên dạy môn tiếng Anh", "pos": "phrase"},
    # 4744: established church
    {"ipa": "/ɪˈstæblɪʃt tʃɜːrtʃ/", "vi": "quốc giáo chính thức của nhà nước", "pos": "phrase"},
    # 4745: executive department
    {"ipa": "/ɪɡˈzɛkjətɪv dɪˈpɑːrtmənt/", "vi": "bộ ngành hành pháp chính phủ Mỹ", "pos": "phrase"},
    # 4746: fair ball
    {"ipa": "/fɛr bɔːl/", "vi": "bóng hợp lệ trong môn bóng chày", "pos": "phrase"},
    # 4747: fat chance
    {"ipa": "/fæt tʃæns/", "vi": "không có cửa đâu; cơ hội mong manh", "pos": "phrase"},
    # 4748: final solution
    {"ipa": "/ˈfaɪnl səˈluːʃən/", "vi": "kế hoạch diệt chủng người Do Thái", "pos": "phrase"},
    # 4749: fire engine
    {"ipa": "/ˈfaɪər ˈɛndʒɪn/", "vi": "xe chữa cháy cứu hỏa chuyên dụng", "pos": "phrase"},
    # 4750: five nations
    {"ipa": "/faɪv ˈneɪʃənz/", "vi": "Liên minh Năm bộ tộc Iroquois", "pos": "phrase"},
    # 4751: flat out
    {"ipa": "/flæt aʊt/", "vi": "hết tốc lực; thẳng thừng dứt khoát", "pos": "phrase"},
    # 4752: fly high
    {"ipa": "/flaɪ haɪ/", "vi": "thành công rực rỡ; bay cao bổng", "pos": "phrase"},
    # 4753: food waste
    {"ipa": "/fuːd weɪst/", "vi": "thức ăn thừa lãng phí; rác hữu cơ", "pos": "phrase"},
    # 4754: function call
    {"ipa": "/ˈfʌŋkʃən kɔːl/", "vi": "lệnh gọi hàm trong lập trình mã", "pos": "phrase"},
    # 4755: gas pressure
    {"ipa": "/ɡæs ˈprɛʃər/", "vi": "áp suất chất khí nén trong bình", "pos": "phrase"},
    # 4756: gas station
    {"ipa": "/ɡæs ˈsteɪʃən/", "vi": "cây xăng dầu; trạm tiếp nhiên liệu", "pos": "phrase"},
    # 4757: heat energy
    {"ipa": "/hiːt ˈɛnərdʒi/", "vi": "nhiệt năng nhiệt lượng vật lý", "pos": "phrase"},
    # 4758: henry the great
    {"ipa": "/ˈhɛnri ðə ɡreɪt/", "vi": "vua Henri IV Đại đế nước Pháp", "pos": "phrase"},
    # 4759: high blood pressure
    {"ipa": "/haɪ blʌd ˈprɛʃər/", "vi": "chứng bệnh tăng huyết áp tim mạch", "pos": "phrase"},
    # 4760: hospital train
    {"ipa": "/ˈhɑːspɪtl treɪn/", "vi": "đoàn tàu hỏa quân y cứu thương", "pos": "phrase"},
    # 4761: house fly
    {"ipa": "/haʊs flaɪ/", "vi": "con ruồi nhà phổ biến truyền bệnh", "pos": "phrase"},
    # 4762: house of cards
    {"ipa": "/haʊs ʌv kɑːrdz/", "vi": "lâu đài xây trên cát; cơ đồ dễ sụp", "pos": "phrase"},
    # 4763: housing start
    {"ipa": "/ˈhaʊzɪŋ stɑːrt/", "vi": "số lượng nhà ở mới khởi công xây", "pos": "phrase"},
    # 4764: ill will
    {"ipa": "/ɪl wɪl/", "vi": "ác ý thù ghét; mối ác cảm sâu sắc", "pos": "phrase"},
    # 4765: in good taste
    {"ipa": "/ɪn ɡʊd teɪst/", "vi": "tao nhã có gu; trang nhã tinh tế", "pos": "phrase"},
    # 4766: iron man
    {"ipa": "/ˈaɪərn mæn/", "vi": "người thép có sức bền phi thường", "pos": "phrase"},
    # 4767: kick about
    {"ipa": "/kɪk əˈbaʊt/", "vi": "bàn bạc thảo luận; lang thang la cà", "pos": "phrase"},
    # 4768: kick out
    {"ipa": "/kɪk aʊt/", "vi": "tống cổ đuổi ra; đuổi học sa thải", "pos": "phrase"},
    # 4769: kick up
    {"ipa": "/kɪk ʌp/", "vi": "quậy phá ầm ĩ; làm dấy lên bụi gió", "pos": "phrase"},
    # 4770: land mass
    {"ipa": "/lænd mæs/", "vi": "khối đất liền rộng lớn; lục địa", "pos": "phrase"},
    # 4771: law firm
    {"ipa": "/lɔː fɜːrm/", "vi": "công ty luật; văn phòng luật sư", "pos": "phrase"},
    # 4772: law of nations
    {"ipa": "/lɔː ʌv ˈneɪʃənz/", "vi": "công pháp quốc tế; luật quốc tế", "pos": "phrase"},
    # 4773: letter paper
    {"ipa": "/ˈlɛtər ˈpeɪpər/", "vi": "giấy viết thư tay; giấy gửi thư từ", "pos": "phrase"},
    # 4774: library fine
    {"ipa": "/ˈlaɪbrɛri faɪn/", "vi": "tiền phạt nộp muộn sách thư viện", "pos": "phrase"},
    # 4775: local option
    {"ipa": "/ˈloʊkl ˈɑːpʃən/", "vi": "quyền biểu quyết tại địa phương", "pos": "phrase"},
    # 4776: long fly
    {"ipa": "/lɔːŋ flaɪ/", "vi": "cú đánh bóng bổng xa ra ngoài sân", "pos": "phrase"},
    # 4777: loss leader
    {"ipa": "/lɔːs ˈliːdər/", "vi": "mặt hàng bán lỗ câu khách mua sắm", "pos": "phrase"},
    # 4778: mail out
    {"ipa": "/meɪl aʊt/", "vi": "gửi bưu phẩm đi qua bưu điện", "pos": "phrase"},
    # 4779: market square
    {"ipa": "/ˈmɑːrkɪt skwɛr/", "vi": "quảng trường họp chợ trung tâm phố", "pos": "phrase"},
    # 4780: mass energy
    {"ipa": "/mæs ˈɛnərdʒi/", "vi": "năng lượng tương đương khối lượng", "pos": "phrase"},
    # 4781: master key
    {"ipa": "/ˈmæstər kiː/", "vi": "chìa khóa vạn năng mở mọi ổ khóa", "pos": "phrase"},
    # 4782: master of science
    {"ipa": "/ˈmæstər ʌv ˈsaɪəns/", "vi": "thạc sĩ khoa học tự nhiên bằng cấp", "pos": "phrase"},
    # 4783: mental age
    {"ipa": "/ˈmɛntl eɪdʒ/", "vi": "tuổi trí tuệ đo theo chỉ số IQ", "pos": "phrase"},
    # 4784: metal saw
    {"ipa": "/ˈmɛtl sɔː/", "vi": "cưa sắt cầm tay; máy cưa kim loại", "pos": "phrase"},
    # 4785: middle high german
    {"ipa": "/ˈmɪdl haɪ ˈdʒɜːrmən/", "vi": "tiếng Đức thời kỳ Trung thế kỷ", "pos": "phrase"},
    # 4786: mix in
    {"ipa": "/mɪks ɪn/", "vi": "trộn lẫn vào; hòa nhập vào đám đông", "pos": "phrase"},
    # 4787: new britain
    {"ipa": "/nuː ˈbrɪtn/", "vi": "đảo New Britain xứ Papua New Guinea", "pos": "phrase"},
    # 4788: north african
    {"ipa": "/nɔːrθ ˈæfrɪkən/", "vi": "người Bắc Phi; thuộc về xứ Bắc Phi", "pos": "phrase"},
    # 4789: number one wood
    {"ipa": "/ˈnʌmbər wʌn wʊd/", "vi": "gậy gỗ driver số 1 trong môn golf", "pos": "phrase"},
    # 4790: party spirit
    {"ipa": "/ˈpɑːrti ˈspɪrɪt/", "vi": "tinh thần vì đảng phái; tính đảng", "pos": "phrase"},
    # 4791: personal credit line
    {"ipa": "/ˈpɜːrsənl ˈkrɛdɪt laɪn/", "vi": "hạn mức tín dụng cá nhân ngân hàng", "pos": "phrase"},
    # 4792: plus sign
    {"ipa": "/plʌs saɪn/", "vi": "dấu cộng trong phép tính toán học", "pos": "phrase"},
    # 4793: potential difference
    {"ipa": "/pəˈtɛnʃl ˈdɪfrəns/", "vi": "hiệu điện thế giữa hai điểm mạch", "pos": "phrase"},
    # 4794: primary health care
    {"ipa": "/ˈpraɪmɛri hɛlθ kɛr/", "vi": "chăm sóc y tế ban đầu tại cơ sở", "pos": "phrase"},
    # 4795: property master
    {"ipa": "/ˈprɑːpərti ˈmæstər/", "vi": "người quản lý đạo cụ sân khấu phim", "pos": "phrase"},
    # 4796: public housing
    {"ipa": "/ˈpʌblɪk ˈhaʊzɪŋ/", "vi": "khu nhà ở xã hội công cộng cho dân", "pos": "phrase"},
    # 4797: pull along
    {"ipa": "/pʊl əˈlɔːŋ/", "vi": "kéo lê đi theo; lôi kéo theo cùng", "pos": "phrase"},
    # 4798: queen mother
    {"ipa": "/kwiːn ˈmʌðər/", "vi": "hoàng thái hậu mẹ vua đương triều", "pos": "phrase"},
    # 4799: radio station
    {"ipa": "/ˈreɪdioʊ ˈsteɪʃən/", "vi": "trạm phát sóng phát thanh radio", "pos": "phrase"}
]

with open("scratch/b21_r10_raw_p3.json", "r", encoding="utf-8") as f:
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

with open("scratch/b21_r10_p3.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(output)} entries for Round 10 Part 3.")
