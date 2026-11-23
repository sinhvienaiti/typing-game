import json

# Manual word-by-word cognitive review for Batch 21 Round 6 Part 1 (records 2500-2599, IDs 200k.002502 to 200k.002601)
reviewed_entries = [
    # 2500: fast food
    {"ipa": "/fæst fuːd/", "vi": "đồ ăn nhanh; thức ăn chế biến sẵn", "pos": "phrase"},
    # 2501: federal office
    {"ipa": "/ˈfɛdərəl ˈɔːfɪs/", "vi": "cơ quan liên bang; công sở nhà nước", "pos": "phrase"},
    # 2502: final period
    {"ipa": "/ˈfaɪnəl ˈpɪriəd/", "vi": "hiệp đấu cuối cùng; giai đoạn chót", "pos": "phrase"},
    # 2503: foreign service
    {"ipa": "/ˈfɔːrən ˈsɜːrvɪs/", "vi": "ngành ngoại giao; cơ quan ngoại vụ", "pos": "phrase"},
    # 2504: funny house
    {"ipa": "/ˈfʌni haʊs/", "vi": "bệnh viện tâm thần; nhà ma giải trí", "pos": "phrase"},
    # 2505: give the eye
    {"ipa": "/ɡɪv ðə aɪ/", "vi": "liếc mắt đưa tình; nhìn ngó dò xét", "pos": "phrase"},
    # 2506: group practice
    {"ipa": "/ɡruːp ˈpræktɪs/", "vi": "phòng khám bác sĩ liên danh đa khoa", "pos": "phrase"},
    # 2507: half page
    {"ipa": "/hæf peɪdʒ/", "vi": "nửa trang sách; diện tích nửa trang", "pos": "phrase"},
    # 2508: head of hair
    {"ipa": "/hɛd ʌv hɛr/", "vi": "mái tóc dày mượt; chỏm tóc trên đầu", "pos": "phrase"},
    # 2509: head voice
    {"ipa": "/hɛd vɔɪs/", "vi": "giọng óc âm cao; giọng giả thanh", "pos": "phrase"},
    # 2510: hit the books
    {"ipa": "/hɪt ðə bʊks/", "vi": "dùi mài kinh sử; tập trung học bài", "pos": "phrase"},
    # 2511: human relationship
    {"ipa": "/ˈhjuːmən rɪˈleɪʃənʃɪp/", "vi": "mối quan hệ giữa người với người", "pos": "phrase"},
    # 2512: language area
    {"ipa": "/ˈlæŋɡwɪdʒ ˈɛriə/", "vi": "vùng ngôn ngữ trong vỏ não", "pos": "phrase"},
    # 2513: leading man
    {"ipa": "/ˈliːdɪŋ mæn/", "vi": "nam diễn viên chính; tài tử chính", "pos": "phrase"},
    # 2514: leave alone
    {"ipa": "/liːv əˈloʊn/", "vi": "để yên một mình; không làm phiền", "pos": "phrase"},
    # 2515: living dead
    {"ipa": "/ˈlɪvɪŋ dɛd/", "vi": "xác sống thây ma; sống không hồn", "pos": "phrase"},
    # 2516: local post office
    {"ipa": "/ˈloʊkəl poʊst ˈɔːfɪs/", "vi": "bưu điện địa phương cấp cơ sở", "pos": "phrase"},
    # 2517: main road
    {"ipa": "/meɪn roʊd/", "vi": "đường trục chính; tuyến đường lớn", "pos": "phrase"},
    # 2518: make clean
    {"ipa": "/meɪk kliːn/", "vi": "lau chùi sạch sẽ; làm trong sạch", "pos": "phrase"},
    # 2519: management control
    {"ipa": "/ˈmænɪdʒmənt kənˈtroʊl/", "vi": "kiểm soát quản trị điều hành", "pos": "phrase"},
    # 2520: medical community
    {"ipa": "/ˈmɛdɪkəl kəˈmjuːnəti/", "vi": "giới y khoa; cộng đồng ngành y tế", "pos": "phrase"},
    # 2521: middle age
    {"ipa": "/ˈmɪdəl eɪdʒ/", "vi": "tuổi trung niên; độ tuổi chín muồi", "pos": "phrase"},
    # 2522: money box
    {"ipa": "/ˈmʌni bɑːks/", "vi": "hộp tiền tiết kiệm; hòm bỏ ống heo", "pos": "phrase"},
    # 2523: month by month
    {"ipa": "/mʌnθ baɪ mʌnθ/", "vi": "hàng tháng liên tục; từng tháng một", "pos": "phrase"},
    # 2524: mother board
    {"ipa": "/ˈmʌðər bɔːrd/", "vi": "bo mạch chủ máy vi tính điện tử", "pos": "phrase"},
    # 2525: music paper
    {"ipa": "/ˈmjuːzɪk ˈpeɪpər/", "vi": "giấy kẻ khuông nhạc chép nốt", "pos": "phrase"},
    # 2526: order code
    {"ipa": "/ˈɔːrdər koʊd/", "vi": "mã lệnh lập trình; mã đơn đặt hàng", "pos": "phrase"},
    # 2527: paper white
    {"ipa": "/ˈpeɪpər waɪt/", "vi": "hoa thủy tiên trắng; màu trắng tinh", "pos": "phrase"},
    # 2528: picture taking
    {"ipa": "/ˈpɪktʃər ˈteɪkɪŋ/", "vi": "việc chụp ảnh; nghệ thuật nhiếp ảnh", "pos": "phrase"},
    # 2529: poor law
    {"ipa": "/pʊr lɔː/", "vi": "luật trợ cấp tế bần cho người nghèo", "pos": "phrase"},
    # 2530: popular music
    {"ipa": "/ˈpɑːpjələr ˈmjuːzɪk/", "vi": "nhạc đại chúng; dòng nhạc pop thịnh", "pos": "phrase"},
    # 2531: rule in
    {"ipa": "/ruːl ɪn/", "vi": "đưa vào danh sách; chấp thuận tính", "pos": "phrase"},
    # 2532: sea change
    {"ipa": "/siː tʃeɪndʒ/", "vi": "chuyển biến sâu sắc; thay đổi lớn", "pos": "phrase"},
    # 2533: sea god
    {"ipa": "/siː ɡɑːd/", "vi": "thần biển cả; hải thần đại dương", "pos": "phrase"},
    # 2534: section man
    {"ipa": "/ˈsɛkʃən mæn/", "vi": "trợ giảng đại học; phụ tá thảo luận", "pos": "phrase"},
    # 2535: service door
    {"ipa": "/ˈsɜːrvɪs dɔːr/", "vi": "cửa phụ nội bộ; lối đi nhân viên", "pos": "phrase"},
    # 2536: service staff
    {"ipa": "/ˈsɜːrvɪs stæf/", "vi": "đội ngũ nhân viên dịch vụ phục vụ", "pos": "phrase"},
    # 2537: side door
    {"ipa": "/saɪd dɔːr/", "vi": "cửa bên hông nhà; lối đi ngách ngầm", "pos": "phrase"},
    # 2538: small voice
    {"ipa": "/smɔːl vɔɪs/", "vi": "tiếng thì thầm; tiếng nói lương tâm", "pos": "phrase"},
    # 2539: social science
    {"ipa": "/ˈsoʊʃəl ˈsaɪəns/", "vi": "ngành khoa học xã hội nhân văn", "pos": "phrase"},
    # 2540: staff line
    {"ipa": "/stæf laɪn/", "vi": "dòng kẻ khuông nhạc ghi nốt", "pos": "phrase"},
    # 2541: starting point
    {"ipa": "/ˈstɑːrtɪŋ pɔɪnt/", "vi": "điểm xuất phát xuất hành; mốc đầu", "pos": "phrase"},
    # 2542: state capital
    {"ipa": "/steɪt ˈkæpɪtl/", "vi": "thủ phủ của tiểu bang hành chính", "pos": "phrase"},
    # 2543: system of rules
    {"ipa": "/ˈsɪstəm ʌv ruːlz/", "vi": "hệ thống quy tắc kỷ luật chung", "pos": "phrase"},
    # 2544: to that degree
    {"ipa": "/tuː ðæt dɪˈɡriː/", "vi": "đến mức độ sâu sắc như thế ấy", "pos": "phrase"},
    # 2545: water bed
    {"ipa": "/ˈwɔːtər bɛd/", "vi": "đệm nước êm ái; giường đệm nước", "pos": "phrase"},
    # 2546: white paper
    {"ipa": "/waɪt ˈpeɪpər/", "vi": "sách trắng báo cáo chính sách", "pos": "phrase"},
    # 2547: whole blood
    {"ipa": "/hoʊl blʌd/", "vi": "máu toàn phần chưa tách tế bào", "pos": "phrase"},
    # 2548: working dog
    {"ipa": "/ˈwɜːrkɪŋ dɔːɡ/", "vi": "chó nghiệp vụ; chó lao động", "pos": "phrase"},
    # 2549: lotted
    {"ipa": "/ˈlɑːtɪd/", "vi": "đã phân thành từng lô đất đấu giá", "pos": "verb"},
    # 2550: lotting
    {"ipa": "/ˈlɑːtɪŋ/", "vi": "đang phân chia thành từng lô đất", "pos": "verb"},
    # 2551: area code
    {"ipa": "/ˈɛriə koʊd/", "vi": "mã vùng điện thoại viễn thông", "pos": "phrase"},
    # 2552: ask round
    {"ipa": "/æsk raʊnd/", "vi": "mời bạn bè đến chơi nhà ăn cơm", "pos": "phrase"},
    # 2553: bank check
    {"ipa": "/bæŋk tʃɛk/", "vi": "séc ngân hàng; chi phiếu rút tiền", "pos": "phrase"},
    # 2554: blue air
    {"ipa": "/bluː ɛr/", "vi": "bầu không khí trong xanh trên trời", "pos": "phrase"},
    # 2555: business card
    {"ipa": "/ˈbɪznəs kɑːrd/", "vi": "tấm danh thiếp; thiếp giao dịch", "pos": "phrase"},
    # 2556: business district
    {"ipa": "/ˈbɪznəs ˈdɪstrɪkt/", "vi": "khu phố buôn bán tài chính sầm uất", "pos": "phrase"},
    # 2557: call waiting
    {"ipa": "/kɔːl ˈweɪtɪŋ/", "vi": "dịch vụ cuộc gọi chờ viễn thông", "pos": "phrase"},
    # 2558: car door
    {"ipa": "/kɑːr dɔːr/", "vi": "cánh cửa ô tô xe hơi chống va đập", "pos": "phrase"},
    # 2559: car race
    {"ipa": "/kɑːr reɪs/", "vi": "cuộc đua xe ô tô; giải đua xe hơi", "pos": "phrase"},
    # 2560: class feeling
    {"ipa": "/klæs ˈfiːlɪŋ/", "vi": "ý thức tình cảm giai cấp sâu sắc", "pos": "phrase"},
    # 2561: conference house
    {"ipa": "/ˈkɑːnfərəns haʊs/", "vi": "nhà hội nghị; trung tâm hội nghị", "pos": "phrase"},
    # 2562: control character
    {"ipa": "/kənˈtroʊl ˈkærəktər/", "vi": "ký tự điều khiển luồng dữ liệu", "pos": "phrase"},
    # 2563: cut price
    {"ipa": "/kʌt praɪs/", "vi": "giá bán đại hạ giá; giá chiết khấu", "pos": "phrase"},
    # 2564: data rate
    {"ipa": "/ˈdeɪtə reɪt/", "vi": "tốc độ truyền dẫn luồng dữ liệu số", "pos": "phrase"},
    # 2565: death cup
    {"ipa": "/dɛθ kʌp/", "vi": "nấm độc tử thần cực độc nguy hiểm", "pos": "phrase"},
    # 2566: department of energy
    {"ipa": "/dɪˈpɑːrtmənt ʌv ˈɛnərdʒi/", "vi": "Bộ Năng lượng quốc gia chính phủ", "pos": "phrase"},
    # 2567: east by north
    {"ipa": "/iːst baɪ nɔːrθ/", "vi": "hướng đông hơi chếch bắc 11 độ", "pos": "phrase"},
    # 2568: energy department
    {"ipa": "/ˈɛnərdʒi dɪˈpɑːrtmənt/", "vi": "sở quản lý năng lượng cơ quan", "pos": "phrase"},
    # 2569: european country
    {"ipa": "/ˌjʊrəˈpiːən ˈkʌntri/", "vi": "quốc gia nằm ở châu lục châu Âu", "pos": "phrase"},
    # 2570: fair use
    {"ipa": "/fɛr juːs/", "vi": "nguyên tắc sử dụng hợp lý bản quyền", "pos": "phrase"},
    # 2571: field of force
    {"ipa": "/fiːld ʌv fɔːrs/", "vi": "trường lực tương tác trong vật lý", "pos": "phrase"},
    # 2572: final result
    {"ipa": "/ˈfaɪnəl rɪˈzʌlt/", "vi": "kết quả chung cuộc sau cùng", "pos": "phrase"},
    # 2573: fire control system
    {"ipa": "/ˈfaɪər kənˈtroʊl ˈsɪstəm/", "vi": "hệ thống ngắm bắn hỏa lực vũ khí", "pos": "phrase"},
    # 2574: fit out
    {"ipa": "/fɪt aʊt/", "vi": "trang bị đồ đạc; sắm sửa phụ tùng", "pos": "phrase"},
    # 2575: force field
    {"ipa": "/fɔːrs fiːld/", "vi": "trường lực bảo vệ; từ trường lực", "pos": "phrase"},
    # 2576: foreign country
    {"ipa": "/ˈfɔːrən ˈkʌntri/", "vi": "nước ngoài; quốc gia ngoại quốc", "pos": "phrase"},
    # 2577: general election
    {"ipa": "/ˈdʒɛnərəl ɪˈlɛkʃən/", "vi": "cuộc tổng tuyển cử trên toàn quốc", "pos": "phrase"},
    # 2578: general staff
    {"ipa": "/ˈdʒɛnərəl stæf/", "vi": "bộ tổng tham mưu quân sự chiến lược", "pos": "phrase"},
    # 2579: god knows how
    {"ipa": "/ɡɑːd noʊz haʊ/", "vi": "trời mới biết thế nào; không ai rõ", "pos": "phrase"},
    # 2580: good friday
    {"ipa": "/ɡʊd ˈfraɪdeɪ/", "vi": "Thứ Sáu Tuần Thánh trong Kitô giáo", "pos": "phrase"},
    # 2581: government minister
    {"ipa": "/ˈɡʌvərnmənt ˈmɪnɪstər/", "vi": "bộ trưởng trong nội các chính phủ", "pos": "phrase"},
    # 2582: government note
    {"ipa": "/ˈɡʌvərnmənt noʊt/", "vi": "giấy bạc do chính phủ phát hành", "pos": "phrase"},
    # 2583: half blood
    {"ipa": "/hæf blʌd/", "vi": "người lai; anh em cùng cha khác mẹ", "pos": "phrase"},
    # 2584: half brother
    {"ipa": "/hæf ˈbrʌðər/", "vi": "anh em trai cùng cha khác mẹ", "pos": "phrase"},
    # 2585: half title
    {"ipa": "/hæf ˈtaɪtl/", "vi": "trang lót đề tựa cuốn sách", "pos": "phrase"},
    # 2586: head sea
    {"ipa": "/hɛd siː/", "vi": "sóng đầu đập ngược mũi tàu thuyền", "pos": "phrase"},
    # 2587: higher education
    {"ipa": "/ˈhaɪər ˌɛdʒəˈkeɪʃən/", "vi": "bậc giáo dục đại học và sau đại học", "pos": "phrase"},
    # 2588: in stock
    {"ipa": "/ɪn stɑːk/", "vi": "còn hàng trong kho trữ; có sẵn ngay", "pos": "phrase"},
    # 2589: information technology
    {"ipa": "/ˌɪnfərˈmeɪʃən tɛkˈnɑːlədʒi/", "vi": "ngành công nghệ thông tin máy tính", "pos": "phrase"},
    # 2590: keep track
    {"ipa": "/kiːp træk/", "vi": "theo dõi sát sao; nắm bắt diễn biến", "pos": "phrase"},
    # 2591: last minute
    {"ipa": "/læst ˈmɪnɪt/", "vi": "giây phút chót; thời khắc sau cùng", "pos": "phrase"},
    # 2592: light source
    {"ipa": "/laɪt sɔːrs/", "vi": "nguồn phát sáng; thiết bị đèn chiếu", "pos": "phrase"},
    # 2593: living room set
    {"ipa": "/ˈlɪvɪŋ ruːm sɛt/", "vi": "bộ bàn ghế sofa phòng khách đầy đủ", "pos": "phrase"},
    # 2594: lower court
    {"ipa": "/ˈloʊər kɔːrt/", "vi": "tòa án xét xử sơ thẩm cấp dưới", "pos": "phrase"},
    # 2595: medical report
    {"ipa": "/ˈmɛdɪkəl rɪˈpɔːrt/", "vi": "báo cáo bệnh án; hồ sơ giám định y", "pos": "phrase"},
    # 2596: middle west
    {"ipa": "/ˈmɪdəl wɛst/", "vi": "vùng Trung Tây nước Mỹ trù phú", "pos": "phrase"},
    # 2597: military march
    {"ipa": "/ˈmɪlətɛri mɑːrtʃ/", "vi": "khúc quân hành; bài nhạc duyệt binh", "pos": "phrase"},
    # 2598: natural history
    {"ipa": "/ˈnætʃərəl ˈhɪstəri/", "vi": "khoa học lịch sử tự nhiên vạn vật", "pos": "phrase"},
    # 2599: news article
    {"ipa": "/nuːz ˈɑːrtɪkəl/", "vi": "bài viết thời sự báo chí; tin tức", "pos": "phrase"},
]

with open('scratch/b21_r06_raw_p1.json') as f:
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

with open('scratch/b21_r06_p1.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r06_p1.json created successfully and validated!")
