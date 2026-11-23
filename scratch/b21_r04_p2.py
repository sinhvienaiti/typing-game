import json

# Manual word-by-word cognitive review for Batch 21 Round 4 Part 2 (records 1600-1699, IDs 200k.001602 to 200k.001701)
reviewed_entries = [
    # 1600: take into account
    {"ipa": "/teɪk ˈɪntuː əˈkaʊnt/", "vi": "tính đến; cân nhắc xem xét đến", "pos": "phrase"},
    # 1601: talking head
    {"ipa": "/ˈtɔːkɪŋ hɛd/", "vi": "bình luận viên truyền hình", "pos": "phrase"},
    # 1602: thought process
    {"ipa": "/θɔːt ˈprɑːsɛs/", "vi": "tiến trình tư duy suy nghĩ", "pos": "phrase"},
    # 1603: vote out
    {"ipa": "/voʊt aʊt/", "vi": "bỏ phiếu bãi nhiệm chức vụ", "pos": "phrase"},
    # 1604: word of god
    {"ipa": "/wɜːrd ʌv ɡɑːd/", "vi": "Lời Chúa trong Kinh Thánh", "pos": "phrase"},
    # 1605: world bank
    {"ipa": "/wɜːrld bæŋk/", "vi": "Ngân hàng Thế giới", "pos": "phrase"},
    # 1606: young woman
    {"ipa": "/jʌŋ ˈwʊmən/", "vi": "cô gái trẻ; thiếu nữ thanh xuân", "pos": "phrase"},
    # 1607: came
    {"ipa": "/keɪm/", "vi": "đã đến; đã tới nơi", "pos": "verb"},
    # 1608: states
    {"ipa": "/steɪts/", "vi": "các quốc gia; những tiểu bang", "pos": "noun"},
    # 1609: stating
    {"ipa": "/ˈsteɪtɪŋ/", "vi": "đang tuyên bố; nêu rõ ràng", "pos": "verb"},
    # 1610: threes
    {"ipa": "/θriːz/", "vi": "các con số ba; nhóm bộ ba", "pos": "noun"},
    # 1611: add on
    {"ipa": "/æd ɑːn/", "vi": "bổ sung thêm; phụ kiện gắn thêm", "pos": "phrase"},
    # 1612: american plan
    {"ipa": "/əˈmɛrɪkən plæn/", "vi": "gói phòng khách sạn kèm ba bữa ăn", "pos": "phrase"},
    # 1613: at any rate
    {"ipa": "/æt ˈɛni reɪt/", "vi": "dù thế nào đi nữa; ít nhất là", "pos": "phrase"},
    # 1614: be born
    {"ipa": "/biː bɔːrn/", "vi": "được sinh ra chào đời; xuất hiện", "pos": "phrase"},
    # 1615: call into question
    {"ipa": "/kɔːl ˈɪntuː ˈkwɛstʃən/", "vi": "đặt dấu hỏi nghi vấn; chất vấn", "pos": "phrase"},
    # 1616: case study
    {"ipa": "/keɪs ˈstʌdi/", "vi": "nghiên cứu tình huống điển hình", "pos": "phrase"},
    # 1617: cool down
    {"ipa": "/kuːl daʊn/", "vi": "hạ nhiệt độ; bài tập thả lỏng cơ", "pos": "phrase"},
    # 1618: cool off
    {"ipa": "/kuːl ɔːf/", "vi": "nguôi giận; bình tĩnh tĩnh tâm lại", "pos": "phrase"},
    # 1619: cover for
    {"ipa": "/ˈkʌvər fɔːr/", "vi": "bao che cho; làm việc thay cho ai", "pos": "phrase"},
    # 1620: dog do
    {"ipa": "/dɔːɡ duː/", "vi": "phân chó trên bãi cỏ", "pos": "phrase"},
    # 1621: drive back
    {"ipa": "/draɪv bæk/", "vi": "đẩy lùi quân địch; lái xe về", "pos": "phrase"},
    # 1622: fall back
    {"ipa": "/fɔːl bæk/", "vi": "rút lui về sau; phải cầu viện đến", "pos": "phrase"},
    # 1623: fall over
    {"ipa": "/fɔːl ˈoʊvər/", "vi": "ngã nhào chúi xuống; sụp đổ", "pos": "phrase"},
    # 1624: far and near
    {"ipa": "/fɑːr ænd nɪr/", "vi": "khắp bốn phương; gần xa khắp chốn", "pos": "phrase"},
    # 1625: force play
    {"ipa": "/fɔːrs pleɪ/", "vi": "pha bắt buộc bóng chày", "pos": "phrase"},
    # 1626: free energy
    {"ipa": "/friː ˈɛnərdʒi/", "vi": "năng lượng tự do nhiệt động học", "pos": "phrase"},
    # 1627: fun run
    {"ipa": "/fʌn rʌn/", "vi": "cuộc chạy bộ gây quỹ cộng đồng", "pos": "phrase"},
    # 1628: group action
    {"ipa": "/ɡruːp ˈækʃən/", "vi": "hành động tập thể đồng lòng", "pos": "phrase"},
    # 1629: hands down
    {"ipa": "/hændz daʊn/", "vi": "dễ như trở bàn tay; hoàn toàn vượt", "pos": "phrase"},
    # 1630: light within
    {"ipa": "/laɪt wɪˈðɪn/", "vi": "ánh sáng nội tâm thiêng liêng", "pos": "phrase"},
    # 1631: like hell
    {"ipa": "/laɪk hɛl/", "vi": "rất dữ dội; không đời nào chịu", "pos": "phrase"},
    # 1632: line of fire
    {"ipa": "/laɪn ʌv ˈfaɪər/", "vi": "lằn ranh đường đạn bắn", "pos": "phrase"},
    # 1633: lose it
    {"ipa": "/luːz ɪt/", "vi": "mất kiểm soát bản thân; nổi điên", "pos": "phrase"},
    # 1634: market order
    {"ipa": "/ˈmɑːrkɪt ˈɔːrdər/", "vi": "lệnh thị trường chứng khoán", "pos": "phrase"},
    # 1635: medical man
    {"ipa": "/ˈmɛdɪkəl mæn/", "vi": "bác sĩ nam giới; thầy thuốc y khoa", "pos": "phrase"},
    # 1636: news report
    {"ipa": "/nuːz rɪˈpɔːrt/", "vi": "bản tin tường thuật sự việc", "pos": "phrase"},
    # 1637: old english
    {"ipa": "/oʊld ˈɪŋɡlɪʃ/", "vi": "tiếng Anh cổ thời Trung Cổ", "pos": "phrase"},
    # 1638: open fire
    {"ipa": "/ˈoʊpən ˈfaɪər/", "vi": "nổ súng khai hỏa; ngọn lửa trần", "pos": "phrase"},
    # 1639: phone line
    {"ipa": "/foʊn laɪn/", "vi": "đường dây thuê bao điện thoại", "pos": "phrase"},
    # 1640: phone service
    {"ipa": "/foʊn ˈsɜːrvɪs/", "vi": "dịch vụ mạng điện thoại", "pos": "phrase"},
    # 1641: political party
    {"ipa": "/pəˈlɪtɪkəl ˈpɑːrti/", "vi": "đảng phái chính trị hoạt động", "pos": "phrase"},
    # 1642: press down
    {"ipa": "/prɛs daʊn/", "vi": "ấn mạnh xuống; đè nén", "pos": "phrase"},
    # 1643: press down on
    {"ipa": "/prɛs daʊn ɑːn/", "vi": "tạo áp lực nặng nề lên", "pos": "phrase"},
    # 1644: private school
    {"ipa": "/ˈpraɪvət skuːl/", "vi": "trường tư thục dân lập", "pos": "phrase"},
    # 1645: program music
    {"ipa": "/ˈproʊɡræm ˈmjuːzɪk/", "vi": "nhạc có tiêu đề câu chuyện", "pos": "phrase"},
    # 1646: question of fact
    {"ipa": "/ˈkwɛstʃən ʌv fækt/", "vi": "vấn đề tình tiết thực tế vụ án", "pos": "phrase"},
    # 1647: round off
    {"ipa": "/raʊnd ɔːf/", "vi": "làm tròn chữ số; hoàn tất êm đẹp", "pos": "phrase"},
    # 1648: running away
    {"ipa": "/ˈrʌnɪŋ əˈweɪ/", "vi": "hành vi bỏ trốn trốn chạy", "pos": "phrase"},
    # 1649: running play
    {"ipa": "/ˈrʌnɪŋ pleɪ/", "vi": "chiến thuật chạy bóng bầu dục", "pos": "phrase"},
    # 1650: side street
    {"ipa": "/saɪd striːt/", "vi": "phố nhỏ nhánh phụ", "pos": "phrase"},
    # 1651: sign in
    {"ipa": "/saɪn ɪn/", "vi": "đăng nhập hệ thống; ký tên vào", "pos": "phrase"},
    # 1652: sound off
    {"ipa": "/saʊnd ɔːf/", "vi": "lên tiếng thẳng thắn; điểm danh to", "pos": "phrase"},
    # 1653: trade good
    {"ipa": "/treɪd ɡʊd/", "vi": "hàng hóa trao đổi mậu dịch", "pos": "phrase"},
    # 1654: turned on
    {"ipa": "/tɜːrnd ɑːn/", "vi": "hưng phấn kích thích; được bật lên", "pos": "phrase"},
    # 1655: tv show
    {"ipa": "/ˌtiːˈviː ʃoʊ/", "vi": "chương trình giải trí truyền hình", "pos": "phrase"},
    # 1656: very fast
    {"ipa": "/ˈvɛri fæst/", "vi": "rất nhanh chóng mau lẹ", "pos": "phrase"},
    # 1657: walk in
    {"ipa": "/wɔːk ɪn/", "vi": "bước vào phòng; không cần hẹn trước", "pos": "phrase"},
    # 1658: water program
    {"ipa": "/ˈwɔːtər ˈproʊɡræm/", "vi": "chương trình kiểm soát nguồn nước", "pos": "phrase"},
    # 1659: west side
    {"ipa": "/wɛst saɪd/", "vi": "khu vực bờ phía tây thành phố", "pos": "phrase"},
    # 1660: add up
    {"ipa": "/æd ʌp/", "vi": "cộng tổng số; hợp lý logic", "pos": "phrase"},
    # 1661: by choice
    {"ipa": "/baɪ tʃɔɪs/", "vi": "do tự nguyện lựa chọn", "pos": "phrase"},
    # 1662: cause of death
    {"ipa": "/kɔːz ʌv dɛθ/", "vi": "nguyên nhân dẫn đến tử vong", "pos": "phrase"},
    # 1663: close at hand
    {"ipa": "/kloʊs æt hænd/", "vi": "ngay trong tầm tay; cận kề sắp đến", "pos": "phrase"},
    # 1664: dead end
    {"ipa": "/dɛd ɛnd/", "vi": "ngõ cụt không lối thoát; bế tắc", "pos": "phrase"},
    # 1665: due south
    {"ipa": "/djuː saʊθ/", "vi": "hướng thẳng chính nam", "pos": "phrase"},
    # 1666: fall all over
    {"ipa": "/fɔːl ɔːl ˈoʊvər/", "vi": "vồ vập săn đón niềm nở thái quá", "pos": "phrase"},
    # 1667: fast day
    {"ipa": "/fæst deɪ/", "vi": "ngày ăn chay tôn giáo", "pos": "phrase"},
    # 1668: front line
    {"ipa": "/frʌnt laɪn/", "vi": "chiến tuyến tuyến đầu; tiên phong", "pos": "phrase"},
    # 1669: go forward
    {"ipa": "/ɡoʊ ˈfɔːrwərd/", "vi": "tiến bước lên phía trước; xúc tiến", "pos": "phrase"},
    # 1670: government department
    {"ipa": "/ˈɡʌvərmənt dɪˈpɑːrtmənt/", "vi": "cơ quan bộ ngành chính phủ", "pos": "phrase"},
    # 1671: government issue
    {"ipa": "/ˈɡʌvərmənt ˈɪʃuː/", "vi": "quân nhu chính phủ cấp; lính Mỹ", "pos": "phrase"},
    # 1672: hand saw
    {"ipa": "/hænd sɔː/", "vi": "cưa xẻ gỗ cầm tay", "pos": "phrase"},
    # 1673: health check
    {"ipa": "/hɛlθ tʃɛk/", "vi": "kiểm tra sức khỏe tổng quát", "pos": "phrase"},
    # 1674: high society
    {"ipa": "/haɪ səˈsaɪəti/", "vi": "giới thượng lưu quý tộc giàu sang", "pos": "phrase"},
    # 1675: home movie
    {"ipa": "/hoʊm ˈmuːvi/", "vi": "phim tư liệu gia đình tự quay", "pos": "phrase"},
    # 1676: human body
    {"ipa": "/ˈhjuːmən ˈbɑːdi/", "vi": "cơ thể sinh học của con người", "pos": "phrase"},
    # 1677: human death
    {"ipa": "/ˈhjuːmən dɛθ/", "vi": "thiệt hại nhân mạng; tử vong người", "pos": "phrase"},
    # 1678: in full action
    {"ipa": "/ɪn fʊl ˈækʃən/", "vi": "đang hoạt động hết công suất tối đa", "pos": "phrase"},
    # 1679: in writing
    {"ipa": "/ɪn ˈraɪtɪŋ/", "vi": "bằng văn bản giấy tờ chính thức", "pos": "phrase"},
    # 1680: information age
    {"ipa": "/ˌɪnfərˈmeɪʃən eɪdʒ/", "vi": "thời đại công nghệ thông tin", "pos": "phrase"},
    # 1681: leave office
    {"ipa": "/liːv ˈɔːfɪs/", "vi": "rời khỏi nhiệm sở; mãn nhiệm kỳ", "pos": "phrase"},
    # 1682: lost cause
    {"ipa": "/lɔːst kɔːz/", "vi": "mục tiêu vô vọng không cứu vãn", "pos": "phrase"},
    # 1683: middle school
    {"ipa": "/ˈmɪdəl skuːl/", "vi": "trường trung học cơ sở", "pos": "phrase"},
    # 1684: old boy
    {"ipa": "/oʊld bɔɪ/", "vi": "cựu học sinh nam của trường", "pos": "phrase"},
    # 1685: old gold
    {"ipa": "/oʊld ɡoʊld/", "vi": "màu vàng kim sẫm cổ kính", "pos": "phrase"},
    # 1686: pick at
    {"ipa": "/pɪk æt/", "vi": "bứt rứt cậy gỡ; ăn uống uể oải", "pos": "phrase"},
    # 1687: police court
    {"ipa": "/pəˈliːs kɔːrt/", "vi": "tòa án xử vi phạm pháp luật nhỏ", "pos": "phrase"},
    # 1688: press home
    {"ipa": "/prɛs hoʊm/", "vi": "nhấn mạnh lý lẽ; tận dụng ưu thế", "pos": "phrase"},
    # 1689: round down
    {"ipa": "/raʊnd daʊn/", "vi": "làm tròn số giảm xuống dưới", "pos": "phrase"},
    # 1690: second period
    {"ipa": "/ˈsɛkənd ˈpɪriəd/", "vi": "hiệp thi đấu thứ hai; tiết hai", "pos": "phrase"},
    # 1691: sign on
    {"ipa": "/saɪn ɑːn/", "vi": "ký hợp đồng làm việc; nhận trợ cấp", "pos": "phrase"},
    # 1692: stand still
    {"ipa": "/stænd stɪl/", "vi": "đứng yên bất động; đình đốn", "pos": "phrase"},
    # 1693: state bank
    {"ipa": "/steɪt bæŋk/", "vi": "ngân hàng cấp tiểu bang tại Mỹ", "pos": "phrase"},
    # 1694: take the stand
    {"ipa": "/teɪk ðə stænd/", "vi": "bước lên bục nhân chứng khai báo", "pos": "phrase"},
    # 1695: training school
    {"ipa": "/ˈtreɪnɪŋ skuːl/", "vi": "trường dạy nghề; trường huấn luyện", "pos": "phrase"},
    # 1696: turned out
    {"ipa": "/tɜːrnd aʊt/", "vi": "ăn vận chỉnh tề; hóa ra là", "pos": "phrase"},
    # 1697: west country
    {"ipa": "/wɛst ˈkʌntri/", "vi": "vùng tây nam nước Anh", "pos": "phrase"},
    # 1698: finds
    {"ipa": "/faɪndz/", "vi": "các phát hiện mới; di vật khảo cổ", "pos": "noun"},
    # 1699: bit by bit
    {"ipa": "/bɪt baɪ bɪt/", "vi": "từng chút một; dần dà từng tí", "pos": "phrase"},
]

with open('scratch/b21_r04_raw_p2.json') as f:
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

with open('scratch/b21_r04_p2.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r04_p2.json created successfully and validated!")
