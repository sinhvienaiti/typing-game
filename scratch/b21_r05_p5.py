import json

# Manual word-by-word cognitive review for Batch 21 Round 5 Part 5 (records 2400-2499, IDs 200k.002402 to 200k.002501)
reviewed_entries = [
    # 2400: sex act
    {"ipa": "/sɛks ækt/", "vi": "hành vi tình dục; việc quan hệ", "pos": "phrase"},
    # 2401: short account
    {"ipa": "/ʃɔːrt əˈkaʊnt/", "vi": "tài khoản bán khống chứng khoán", "pos": "phrase"},
    # 2402: track down
    {"ipa": "/træk daʊn/", "vi": "lùng bắt; truy tìm manh mối", "pos": "phrase"},
    # 2403: tried and true
    {"ipa": "/traɪd ænd truː/", "vi": "đã được kiểm chứng; đáng tin cậy", "pos": "phrase"},
    # 2404: true bill
    {"ipa": "/truː bɪl/", "vi": "bản cáo trạng được bồi thẩm phê", "pos": "phrase"},
    # 2405: us air force
    {"ipa": "/juː ɛs ˈɛr fɔːrs/", "vi": "Không quân Hoa Kỳ; không lực Mỹ", "pos": "phrase"},
    # 2406: water dog
    {"ipa": "/ˈwɔːtər dɔːɡ/", "vi": "chó săn vịt nước; người bơi giỏi", "pos": "phrase"},
    # 2407: weight down
    {"ipa": "/weɪt daʊn/", "vi": "đè nặng trĩu; dằn nặng xuống", "pos": "phrase"},
    # 2408: whole step
    {"ipa": "/hoʊl stɛp/", "vi": "nguyên cung trong âm nhạc", "pos": "phrase"},
    # 2409: word for word
    {"ipa": "/wɜːrd fɔːr wɜːrd/", "vi": "nguyên văn; chuẩn xác từng câu chữ", "pos": "phrase"},
    # 2410: freer
    {"ipa": "/ˈfriːər/", "vi": "tự do hơn; thông thoáng hơn", "pos": "adj"},
    # 2411: someones
    {"ipa": "/ˈsʌmwʌnz/", "vi": "nhân vật quan trọng; những ai đó", "pos": "noun"},
    # 2412: american language
    {"ipa": "/əˈmɛrɪkən ˈlæŋɡwɪdʒ/", "vi": "tiếng Anh Mỹ; ngôn ngữ kiểu Mỹ", "pos": "phrase"},
    # 2413: blood line
    {"ipa": "/blʌd laɪn/", "vi": "dòng máu; huyết thống gia tộc", "pos": "phrase"},
    # 2414: blue book
    {"ipa": "/bluː bʊk/", "vi": "sách xanh báo cáo; sổ bạ danh bạ", "pos": "phrase"},
    # 2415: book review
    {"ipa": "/bʊk rɪˈvjuː/", "vi": "bài điểm sách; bài phê bình sách", "pos": "phrase"},
    # 2416: box family
    {"ipa": "/bɑːks ˈfæməli/", "vi": "họ hoàng dương trong thực vật học", "pos": "phrase"},
    # 2417: break short
    {"ipa": "/breɪk ʃɔːrt/", "vi": "cắt ngang; kết thúc đột ngột", "pos": "phrase"},
    # 2418: building site
    {"ipa": "/ˈbɪldɪŋ saɪt/", "vi": "công trường thi công xây dựng", "pos": "phrase"},
    # 2419: clean out
    {"ipa": "/kliːn aʊt/", "vi": "dọn sạch sẽ; nạo vét sạch túi", "pos": "phrase"},
    # 2420: clean up
    {"ipa": "/kliːn ʌp/", "vi": "dọn dẹp ngăn nắp; kiếm bộn tiền", "pos": "phrase"},
    # 2421: cross off
    {"ipa": "/krɔːs ɔːf/", "vi": "gạch bỏ tên; xóa khỏi danh sách", "pos": "phrase"},
    # 2422: death rate
    {"ipa": "/dɛθ reɪt/", "vi": "tỷ lệ tử vong số ca qua đời", "pos": "phrase"},
    # 2423: death tax
    {"ipa": "/dɛθ tæks/", "vi": "thuế tài sản thừa kế di sản", "pos": "phrase"},
    # 2424: department of education
    {"ipa": "/dɪˈpɑːrtmənt ʌv ˌɛdʒəˈkeɪʃən/", "vi": "Bộ Giáo dục; sở giáo dục", "pos": "phrase"},
    # 2425: director of research
    {"ipa": "/dəˈrɛktər ʌv ˈriːsɜːrtʃ/", "vi": "giám đốc nghiên cứu phát triển", "pos": "phrase"},
    # 2426: do justice
    {"ipa": "/duː ˈdʒʌstɪs/", "vi": "lột tả trọn vẹn; đối xử công bằng", "pos": "phrase"},
    # 2427: drop back
    {"ipa": "/drɑːp bæk/", "vi": "tụt lại phía sau; lùi về tuyến sau", "pos": "phrase"},
    # 2428: east by south
    {"ipa": "/iːst baɪ saʊθ/", "vi": "hướng đông chếch nam 11 độ", "pos": "phrase"},
    # 2429: education department
    {"ipa": "/ˌɛdʒəˈkeɪʃən dɪˈpɑːrtmənt/", "vi": "khoa giáo dục; sở giáo dục", "pos": "phrase"},
    # 2430: federal court
    {"ipa": "/ˈfɛdərəl kɔːrt/", "vi": "tòa án liên bang tài phán", "pos": "phrase"},
    # 2431: field of study
    {"ipa": "/fiːld ʌv ˈstʌdi/", "vi": "lĩnh vực nghiên cứu; chuyên ngành", "pos": "phrase"},
    # 2432: financial support
    {"ipa": "/faɪˈnænʃəl səˈpɔːrt/", "vi": "hỗ trợ tài chính; tài trợ kinh phí", "pos": "phrase"},
    # 2433: fit in
    {"ipa": "/fɪt ɪn/", "vi": "hòa nhập cộng đồng; vừa khít", "pos": "phrase"},
    # 2434: good nature
    {"ipa": "/ɡʊd ˈneɪtʃər/", "vi": "bản tính lương thiện hiền từ", "pos": "phrase"},
    # 2435: half step
    {"ipa": "/hæf stɛp/", "vi": "nửa cung âm nhạc; bán cung", "pos": "phrase"},
    # 2436: hospital care
    {"ipa": "/ˈhɑːspɪtl kɛr/", "vi": "chăm sóc y tế bệnh viện nội trú", "pos": "phrase"},
    # 2437: hot air
    {"ipa": "/hɑːt ɛr/", "vi": "luồng khí nóng; lời nói khoác lác", "pos": "phrase"},
    # 2438: information science
    {"ipa": "/ˌɪnfərˈmeɪʃən ˈsaɪəns/", "vi": "ngành khoa học thông tin lưu trữ", "pos": "phrase"},
    # 2439: keep note
    {"ipa": "/kiːp noʊt/", "vi": "ghi chép lại; lưu tâm chú ý", "pos": "phrase"},
    # 2440: leading off
    {"ipa": "/ˈliːdɪŋ ɔːf/", "vi": "mở màn trận đấu; sự khởi đầu", "pos": "phrase"},
    # 2441: legal power
    {"ipa": "/ˈliːɡəl ˈpaʊər/", "vi": "thẩm quyền tư pháp; quyền hợp pháp", "pos": "phrase"},
    # 2442: light hour
    {"ipa": "/laɪt ˈaʊər/", "vi": "giờ ánh sáng trong thiên văn", "pos": "phrase"},
    # 2443: list price
    {"ipa": "/lɪst praɪs/", "vi": "giá bán niêm yết theo quy định", "pos": "phrase"},
    # 2444: little rock
    {"ipa": "/ˈlɪtəl rɑːk/", "vi": "thủ phủ Little Rock bang Arkansas", "pos": "phrase"},
    # 2445: long island
    {"ipa": "/lɔːŋ ˈaɪlənd/", "vi": "đảo Long Island tại bang New York", "pos": "phrase"},
    # 2446: middle watch
    {"ipa": "/ˈmɪdəl wɑːtʃ/", "vi": "phiên gác đêm từ nửa đêm đến sáng", "pos": "phrase"},
    # 2447: modern times
    {"ipa": "/ˈmɑːdərn taɪmz/", "vi": "thời kỳ hiện đại; phim Thời đại mới", "pos": "phrase"},
    # 2448: morning star
    {"ipa": "/ˈmɔːrnɪŋ stɑːr/", "vi": "sao Mai; sao Kim lúc bình minh", "pos": "phrase"},
    # 2449: natural law
    {"ipa": "/ˈnætʃərəl lɔː/", "vi": "luật tự nhiên; quy luật tự nhiên", "pos": "phrase"},
    # 2450: near miss
    {"ipa": "/nɪr mɪs/", "vi": "vụ suýt va chạm; tai nạn gang tấc", "pos": "phrase"},
    # 2451: north american country
    {"ipa": "/nɔːrθ əˈmɛrɪkən ˈkʌntri/", "vi": "quốc gia thuộc khu vực Bắc Mỹ", "pos": "phrase"},
    # 2452: old growth
    {"ipa": "/oʊld ɡroʊθ/", "vi": "rừng nguyên sinh; rừng già cổ thụ", "pos": "phrase"},
    # 2453: pass away
    {"ipa": "/pæs əˈweɪ/", "vi": "qua đời tạ thế; biến mất tiêu tan", "pos": "phrase"},
    # 2454: pay rate
    {"ipa": "/peɪ reɪt/", "vi": "mức thù lao; đơn giá tiền lương", "pos": "phrase"},
    # 2455: personal check
    {"ipa": "/ˈpɜːrsənəl tʃɛk/", "vi": "tấm séc cá nhân tài khoản", "pos": "phrase"},
    # 2456: picture book
    {"ipa": "/ˈpɪktʃər bʊk/", "vi": "sách tranh minh họa cho thiếu nhi", "pos": "phrase"},
    # 2457: price list
    {"ipa": "/praɪs lɪst/", "vi": "bảng báo giá hàng hóa dịch vụ", "pos": "phrase"},
    # 2458: public figure
    {"ipa": "/ˈpʌblɪk ˈfɪɡjər/", "vi": "nhân vật nổi tiếng của công chúng", "pos": "phrase"},
    # 2459: put to sleep
    {"ipa": "/pʊt tuː sliːp/", "vi": "ru cho ngủ; cho an tử động vật", "pos": "phrase"},
    # 2460: rate of pay
    {"ipa": "/reɪt ʌv peɪ/", "vi": "mức lương chi trả; định mức lương", "pos": "phrase"},
    # 2461: reading room
    {"ipa": "/ˈriːdɪŋ ruːm/", "vi": "phòng đọc sách báo thư viện", "pos": "phrase"},
    # 2462: red lead
    {"ipa": "/rɛd lɛd/", "vi": "chì đỏ; ô-xít chì sơn chống rỉ", "pos": "phrase"},
    # 2463: research director
    {"ipa": "/ˈriːsɜːrtʃ dəˈrɛktər/", "vi": "giám đốc nghiên cứu khoa học", "pos": "phrase"},
    # 2464: room rate
    {"ipa": "/ruːm reɪt/", "vi": "giá thuê phòng khách sạn một đêm", "pos": "phrase"},
    # 2465: round hand
    {"ipa": "/raʊnd hænd/", "vi": "kiểu chữ viết tay nét tròn nghiêng", "pos": "phrase"},
    # 2466: second base
    {"ipa": "/ˈsɛkənd beɪs/", "vi": "chốt gôn số hai trong bóng chày", "pos": "phrase"},
    # 2467: show card
    {"ipa": "/ʃoʊ kɑːrd/", "vi": "bìa quảng cáo; biển áp phích tiệm", "pos": "phrase"},
    # 2468: significant other
    {"ipa": "/sɪɡˈnɪfɪkənt ˈʌðər/", "vi": "người yêu gắn bó; nửa kia đời mình", "pos": "phrase"},
    # 2469: single tax
    {"ipa": "/ˈsɪŋɡəl tæks/", "vi": "học thuyết thuế giá trị đất đai", "pos": "phrase"},
    # 2470: south by east
    {"ipa": "/saʊθ baɪ iːst/", "vi": "hướng nam hơi chếch sang đông", "pos": "phrase"},
    # 2471: space program
    {"ipa": "/speɪs ˈproʊɡræm/", "vi": "chương trình nghiên cứu không gian", "pos": "phrase"},
    # 2472: special interest
    {"ipa": "/ˈspɛʃəl ˈɪntrəst/", "vi": "nhóm lợi ích đặc thù vận động", "pos": "phrase"},
    # 2473: to the letter
    {"ipa": "/tuː ðə ˈlɛtər/", "vi": "chính xác tuyệt đối từng câu chữ", "pos": "phrase"},
    # 2474: trade book
    {"ipa": "/treɪd bʊk/", "vi": "sách đại chúng phổ thông thị trường", "pos": "phrase"},
    # 2475: writing system
    {"ipa": "/ˈraɪtɪŋ ˈsɪstəm/", "vi": "hệ thống chữ viết ký tự văn tự", "pos": "phrase"},
    # 2476: lefter
    {"ipa": "/ˈlɛftər/", "vi": "về phía bên trái hơn; tả khuynh hơn", "pos": "adj"},
    # 2477: leftest
    {"ipa": "/ˈlɛftɪst/", "vi": "ở bên trái nhất; cực tả chính trị", "pos": "adj"},
    # 2478: lefts
    {"ipa": "/lɛfts/", "vi": "những cú đấm tay trái; phe cánh tả", "pos": "noun"},
    # 2479: across the board
    {"ipa": "/əˈkrɔːs ðə bɔːrd/", "vi": "toàn diện áp dụng cho mọi đối tượng", "pos": "phrase"},
    # 2480: add together
    {"ipa": "/æd təˈɡɛðər/", "vi": "cộng dồn lại; gộp chung tính tổng", "pos": "phrase"},
    # 2481: at all costs
    {"ipa": "/æt ɔːl kɔːsts/", "vi": "bằng mọi giá; bằng bất cứ giá nào", "pos": "phrase"},
    # 2482: back of beyond
    {"ipa": "/bæk ʌv bɪˈjɑːnd/", "vi": "nơi xa xôi hẻo lánh; chốn heo hút", "pos": "phrase"},
    # 2483: box number
    {"ipa": "/bɑːks ˈnʌmbər/", "vi": "mã số hộp thư bưu điện riêng", "pos": "phrase"},
    # 2484: central body
    {"ipa": "/ˈsɛntrəl ˈbɑːdi/", "vi": "trung thể sinh học tế bào; cơ quan", "pos": "phrase"},
    # 2485: central office
    {"ipa": "/ˈsɛntrəl ˈɔːfɪs/", "vi": "văn phòng tổng vụ; trụ sở chính", "pos": "phrase"},
    # 2486: city district
    {"ipa": "/ˈsɪti ˈdɪstrɪkt/", "vi": "quận nội thành; đơn vị hành chính", "pos": "phrase"},
    # 2487: coming upon
    {"ipa": "/ˈkʌmɪŋ əˈpɑːn/", "vi": "việc tình cờ bắt gặp; sự hội ngộ", "pos": "phrase"},
    # 2488: common front
    {"ipa": "/ˈkɑːmən frʌnt/", "vi": "mặt trận thống nhất; khối liên minh", "pos": "phrase"},
    # 2489: common market
    {"ipa": "/ˈkɑːmən ˈmɑːrkɪt/", "vi": "khối thị trường chung liên kết", "pos": "phrase"},
    # 2490: contract in
    {"ipa": "/ˈkɑːntrækt ɪn/", "vi": "cam kết tham gia công đoàn đóng quỹ", "pos": "phrase"},
    # 2491: control key
    {"ipa": "/kənˈtroʊl kiː/", "vi": "phím Ctrl điều khiển trên bàn phím", "pos": "phrase"},
    # 2492: current account
    {"ipa": "/ˈkɜːrənt əˈkaʊnt/", "vi": "tài khoản thanh toán vãng lai", "pos": "phrase"},
    # 2493: cut across
    {"ipa": "/kʌt əˈkrɔːs/", "vi": "đi đường tắt; vượt qua rào cản", "pos": "phrase"},
    # 2494: die hard
    {"ipa": "/daɪ hɑːrd/", "vi": "bảo thủ ngoan cố; khó lòng dứt bỏ", "pos": "phrase"},
    # 2495: drop down
    {"ipa": "/drɑːp daʊn/", "vi": "rơi tuột xuống; nằm rạp né đạn", "pos": "phrase"},
    # 2496: drop off
    {"ipa": "/drɑːp ɔːf/", "vi": "thả khách xuống xe; thiu thiu ngủ", "pos": "phrase"},
    # 2497: due east
    {"ipa": "/djuː iːst/", "vi": "hướng thẳng về chính đông la bàn", "pos": "phrase"},
    # 2498: earth god
    {"ipa": "/ɜːrθ ɡɑːd/", "vi": "thổ địa thần linh; thần đất đai", "pos": "phrase"},
    # 2499: fall guy
    {"ipa": "/fɔːl ɡaɪ/", "vi": "kẻ chịu tội thay; con dê tế thần", "pos": "phrase"},
]

with open('scratch/b21_r05_raw_p5.json') as f:
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

with open('scratch/b21_r05_p5.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r05_p5.json created successfully and validated!")
