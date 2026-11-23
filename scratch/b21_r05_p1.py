import json

# Manual word-by-word cognitive review for Batch 21 Round 5 Part 1 (records 2000-2099, IDs 200k.002002 to 200k.002101)
reviewed_entries = [
    # 2000: as required
    {"ipa": "/æz rɪˈkwaɪərd/", "vi": "theo đúng yêu cầu; khi cần thiết", "pos": "phrase"},
    # 2001: at peace
    {"ipa": "/æt piːs/", "vi": "sống thanh thản; yên nghỉ ngàn thu", "pos": "phrase"},
    # 2002: beat in
    {"ipa": "/biːt ɪn/", "vi": "nhồi nhét kiến thức; đập lõm vào", "pos": "phrase"},
    # 2003: bed down
    {"ipa": "/bɛd daʊn/", "vi": "trải chỗ ngủ tạm; đi ngủ", "pos": "phrase"},
    # 2004: big science
    {"ipa": "/bɪɡ ˈsaɪəns/", "vi": "nền khoa học quy mô lớn", "pos": "phrase"},
    # 2005: black lead
    {"ipa": "/blæk lɛd/", "vi": "than chì làm ruột bút chì", "pos": "phrase"},
    # 2006: business relationship
    {"ipa": "/ˈbɪznəs rɪˈleɪʃənˌʃɪp/", "vi": "quan hệ làm ăn; quan hệ kinh doanh", "pos": "phrase"},
    # 2007: center line
    {"ipa": "/ˈsɛntər laɪn/", "vi": "vạch kẻ tim đường giao thông", "pos": "phrase"},
    # 2008: change hands
    {"ipa": "/tʃeɪndʒ hændz/", "vi": "đổi chủ sở hữu; chuyển nhượng", "pos": "phrase"},
    # 2009: common law
    {"ipa": "/ˈkɑːmən lɔː/", "vi": "thông luật; hệ thống luật án lệ", "pos": "phrase"},
    # 2010: control board
    {"ipa": "/kənˈtroʊl bɔːrd/", "vi": "bảng điều khiển; ban kiểm soát", "pos": "phrase"},
    # 2011: county line
    {"ipa": "/ˈkaʊnti laɪn/", "vi": "ranh giới địa giới hành chính hạt", "pos": "phrase"},
    # 2012: current of air
    {"ipa": "/ˈkɜːrənt ʌv ɛr/", "vi": "luồng gió thổi; dòng không khí", "pos": "phrase"},
    # 2013: die down
    {"ipa": "/daɪ daʊn/", "vi": "lắng dịu dần; tàn tạ bớt", "pos": "phrase"},
    # 2014: die off
    {"ipa": "/daɪ ɔːf/", "vi": "chết dần chết mòn hết; tuyệt chủng", "pos": "phrase"},
    # 2015: drive away
    {"ipa": "/draɪv əˈweɪ/", "vi": "xua đuổi đi chỗ khác; lái xe đi", "pos": "phrase"},
    # 2016: eat away
    {"ipa": "/iːt əˈweɪ/", "vi": "gặm mòn phá hủy; ăn mòn dần", "pos": "phrase"},
    # 2017: energy level
    {"ipa": "/ˈɛnərdʒi ˈlɛvəl/", "vi": "mức năng lượng lượng tử vật lý", "pos": "phrase"},
    # 2018: fall away
    {"ipa": "/fɔːl əˈweɪ/", "vi": "rơi rụng giảm dần; thoái lui", "pos": "phrase"},
    # 2019: final cause
    {"ipa": "/ˈfaɪnəl kɔːz/", "vi": "mục đích tối hậu của sự vật", "pos": "phrase"},
    # 2020: first base
    {"ipa": "/fɜːrst beɪs/", "vi": "chốt gôn một bóng chày; bước đầu", "pos": "phrase"},
    # 2021: football game
    {"ipa": "/ˈfʊtˌbɔːl ɡeɪm/", "vi": "trận thi đấu bóng đá; bóng bầu dục", "pos": "phrase"},
    # 2022: free fall
    {"ipa": "/friː fɔːl/", "vi": "sự rơi tự do; sụt giá tự do", "pos": "phrase"},
    # 2023: go deep
    {"ipa": "/ɡoʊ diːp/", "vi": "đi sâu vào bản chất; tiến sâu", "pos": "phrase"},
    # 2024: group meeting
    {"ipa": "/ɡruːp ˈmiːtɪŋ/", "vi": "buổi họp nhóm; cuộc họp tập thể", "pos": "phrase"},
    # 2025: half rest
    {"ipa": "/hæf rɛst/", "vi": "dấu lặng trắng trong bản nhạc", "pos": "phrase"},
    # 2026: hold open
    {"ipa": "/hoʊld ˈoʊpən/", "vi": "giữ ngỏ cơ hội; giữ cửa mở", "pos": "phrase"},
    # 2027: hold the line
    {"ipa": "/hoʊld ðə laɪn/", "vi": "giữ vững phòng tuyến; giữ giá", "pos": "phrase"},
    # 2028: leave behind
    {"ipa": "/liːv bɪˈhaɪnd/", "vi": "bỏ lại phía sau; để quên lại", "pos": "phrase"},
    # 2029: little dog
    {"ipa": "/ˈlɪtəl dɔːɡ/", "vi": "chòm sao Tiểu Khuyển trên trời", "pos": "phrase"},
    # 2030: main office
    {"ipa": "/meɪn ˈɔːfɪs/", "vi": "trụ sở chính; văn phòng trung tâm", "pos": "phrase"},
    # 2031: make pass
    {"ipa": "/meɪk pæs/", "vi": "chuyền bóng cho đồng đội; tán tỉnh", "pos": "phrase"},
    # 2032: medical care
    {"ipa": "/ˈmɛdɪkəl kɛr/", "vi": "dịch vụ chăm sóc chữa trị y tế", "pos": "phrase"},
    # 2033: military law
    {"ipa": "/ˈmɪlətɛri lɔː/", "vi": "quân luật; luật pháp quân đội", "pos": "phrase"},
    # 2034: modern world
    {"ipa": "/ˈmɑːdərn wɜːrld/", "vi": "thế giới văn minh đương đại", "pos": "phrase"},
    # 2035: movie making
    {"ipa": "/ˈmuːvi ˈmeɪkɪŋ/", "vi": "nghề làm phim; sản xuất điện ảnh", "pos": "phrase"},
    # 2036: one million million
    {"ipa": "/wʌn ˈmɪljən ˈmɪljən/", "vi": "một nghìn tỷ; một ngàn tỷ", "pos": "phrase"},
    # 2037: pass over
    {"ipa": "/pæs ˈoʊvər/", "vi": "băng qua; bỏ qua không thăng chức", "pos": "phrase"},
    # 2038: pay cut
    {"ipa": "/peɪ kʌt/", "vi": "sự cắt giảm tiền lương", "pos": "phrase"},
    # 2039: play reading
    {"ipa": "/pleɪ ˈriːdɪŋ/", "vi": "buổi tập đọc kịch bản phân vai", "pos": "phrase"},
    # 2040: price level
    {"ipa": "/praɪs ˈlɛvəl/", "vi": "mặt bằng giá cả chung", "pos": "phrase"},
    # 2041: private line
    {"ipa": "/ˈpraɪvət laɪn/", "vi": "đường dây điện thoại nội bộ riêng", "pos": "phrase"},
    # 2042: put forward
    {"ipa": "/pʊt ˈfɔːrwərd/", "vi": "đề xuất ý kiến; tiến cử người", "pos": "phrase"},
    # 2043: real stuff
    {"ipa": "/riːl stʌf/", "vi": "hàng chuẩn xịn; thứ đích thực", "pos": "phrase"},
    # 2044: red fire
    {"ipa": "/rɛd ˈfaɪər/", "vi": "ngọn lửa đỏ rực; pháo sáng đỏ", "pos": "phrase"},
    # 2045: response time
    {"ipa": "/rɪˈspɑːns taɪm/", "vi": "thời gian phản hồi tín hiệu", "pos": "phrase"},
    # 2046: running hand
    {"ipa": "/ˈrʌnɪŋ hænd/", "vi": "chữ viết tay thảo nét liền", "pos": "phrase"},
    # 2047: service break
    {"ipa": "/ˈsɜːrvɪs breɪk/", "vi": "pha bẻ bàn giao bóng quần vợt", "pos": "phrase"},
    # 2048: service industry
    {"ipa": "/ˈsɜːrvɪs ˈɪndəstri/", "vi": "ngành công nghiệp dịch vụ", "pos": "phrase"},
    # 2049: six day war
    {"ipa": "/sɪks deɪ wɔːr/", "vi": "Chiến tranh Sáu ngày năm 1967", "pos": "phrase"},
    # 2050: sleep over
    {"ipa": "/sliːp ˈoʊvər/", "vi": "ngủ lại qua đêm ở nhà bạn bè", "pos": "phrase"},
    # 2051: so to speak
    {"ipa": "/soʊ tuː spiːk/", "vi": "có thể nói là; ví như là", "pos": "phrase"},
    # 2052: sound system
    {"ipa": "/saʊnd ˈsɪstəm/", "vi": "hệ thống dàn thiết bị âm thanh", "pos": "phrase"},
    # 2053: speak out
    {"ipa": "/spiːk aʊt/", "vi": "thẳng thắn lên tiếng phản đối", "pos": "phrase"},
    # 2054: speak up
    {"ipa": "/spiːk ʌp/", "vi": "nói to hơn; dõng dạc nêu quan điểm", "pos": "phrase"},
    # 2055: special education
    {"ipa": "/ˈspɛʃəl ˌɛdʒəˈkeɪʃən/", "vi": "giáo dục chuyên biệt đặc thù", "pos": "phrase"},
    # 2056: standard time
    {"ipa": "/ˈstændərd taɪm/", "vi": "giờ tiêu chuẩn theo múi giờ", "pos": "phrase"},
    # 2057: to that effect
    {"ipa": "/tuː ðæt ɪˈfɛkt/", "vi": "đại ý mang nội dung tương tự", "pos": "phrase"},
    # 2058: walk through
    {"ipa": "/wɔːk θruː/", "vi": "tập dượt qua; chỉ dẫn từng bước", "pos": "phrase"},
    # 2059: water boy
    {"ipa": "/ˈwɔːtər bɔɪ/", "vi": "cậu bé tiếp nước cho vận động viên", "pos": "phrase"},
    # 2060: white gold
    {"ipa": "/waɪt ɡoʊld/", "vi": "vàng trắng trang sức quý", "pos": "phrase"},
    # 2061: write about
    {"ipa": "/raɪt əˈbaʊt/", "vi": "viết sách báo về chủ đề", "pos": "phrase"},
    # 2062: write out
    {"ipa": "/raɪt aʊt/", "vi": "viết ra đầy đủ chi tiết bằng chữ", "pos": "phrase"},
    # 2063: write up
    {"ipa": "/raɪt ʌp/", "vi": "bài báo nhận định; bài tường trình", "pos": "phrase"},
    # 2064: account book
    {"ipa": "/əˈkaʊnt bʊk/", "vi": "sổ sách kế toán thu chi", "pos": "phrase"},
    # 2065: allow for
    {"ipa": "/əˈlaʊ fɔːr/", "vi": "tính đến; dự trù khả năng xảy ra", "pos": "phrase"},
    # 2066: art form
    {"ipa": "/ɑːrt fɔːrm/", "vi": "loại hình nghệ thuật sáng tạo", "pos": "phrase"},
    # 2067: ball over
    {"ipa": "/bɔːl ˈoʊvər/", "vi": "làm cho kinh ngạc; khiến sững sờ", "pos": "phrase"},
    # 2068: big brother
    {"ipa": "/bɪɡ ˈbrʌðər/", "vi": "anh trai lớn; kẻ giám sát ngầm", "pos": "phrase"},
    # 2069: bit field
    {"ipa": "/bɪt fiːld/", "vi": "trường bit trong cấu trúc dữ liệu", "pos": "phrase"},
    # 2070: black english
    {"ipa": "/blæk ˈɪŋɡlɪʃ/", "vi": "tiếng Anh của người da đen Mỹ", "pos": "phrase"},
    # 2071: book of account
    {"ipa": "/bʊk ʌv əˈkaʊnt/", "vi": "sổ sách kế toán; sổ tài chính", "pos": "phrase"},
    # 2072: break open
    {"ipa": "/breɪk ˈoʊpən/", "vi": "phá khóa cạy tung mở cửa", "pos": "phrase"},
    # 2073: career man
    {"ipa": "/kəˈrɪr mæn/", "vi": "người đàn ông theo đuổi sự nghiệp", "pos": "phrase"},
    # 2074: central city
    {"ipa": "/ˈsɛntrəl ˈsɪti/", "vi": "thành phố hạt nhân trung tâm", "pos": "phrase"},
    # 2075: charge up
    {"ipa": "/tʃɑːrdʒ ʌp/", "vi": "sạc đầy pin; kích động cảm xúc", "pos": "phrase"},
    # 2076: church music
    {"ipa": "/tʃɜːrtʃ ˈmjuːzɪk/", "vi": "thánh ca; âm nhạc phụng vụ nhà thờ", "pos": "phrase"},
    # 2077: class action
    {"ipa": "/klæs ˈækʃən/", "vi": "vụ kiện tụng tập thể bảo vệ quyền", "pos": "phrase"},
    # 2078: clear the air
    {"ipa": "/klɪr ðə ɛr/", "vi": "xua tan bầu không khí căng thẳng", "pos": "phrase"},
    # 2079: club car
    {"ipa": "/klʌb kɑːr/", "vi": "toa hành khách câu lạc bộ tàu hỏa", "pos": "phrase"},
    # 2080: community college
    {"ipa": "/kəˈmjuːnəti ˈkɑːlɪdʒ/", "vi": "trường cao đẳng cộng đồng", "pos": "phrase"},
    # 2081: department of history
    {"ipa": "/dɪˈpɑːrtmənt ʌv ˈhɪstəri/", "vi": "khoa lịch sử trường đại học", "pos": "phrase"},
    # 2082: dog house
    {"ipa": "/dɔːɡ haʊs/", "vi": "chuồng chó nuôi; chỗ bị ruồng bỏ", "pos": "phrase"},
    # 2083: dog show
    {"ipa": "/dɔːɡ ʃoʊ/", "vi": "hội thi triển lãm các giống chó", "pos": "phrase"},
    # 2084: due process
    {"ipa": "/djuː ˈprɑːsɛs/", "vi": "thủ tục pháp lý công bằng", "pos": "phrase"},
    # 2085: east side
    {"ipa": "/iːst saɪd/", "vi": "khu vực bờ phía đông đô thị", "pos": "phrase"},
    # 2086: far east
    {"ipa": "/fɑːr iːst/", "vi": "vùng Viễn Đông châu Á", "pos": "phrase"},
    # 2087: federal government
    {"ipa": "/ˈfɛdərəl ˈɡʌvərmənt/", "vi": "chính phủ liên bang Hoa Kỳ", "pos": "phrase"},
    # 2088: football team
    {"ipa": "/ˈfʊtˌbɔːl tiːm/", "vi": "đội tuyển bóng đá; đội bóng bầu dục", "pos": "phrase"},
    # 2089: free trade
    {"ipa": "/friː treɪd/", "vi": "thương mại mậu dịch tự do", "pos": "phrase"},
    # 2090: get married
    {"ipa": "/ɡɛt ˈmærid/", "vi": "kết hôn thành thân; lập gia đình", "pos": "phrase"},
    # 2091: get moving
    {"ipa": "/ɡɛt ˈmuːvɪŋ/", "vi": "bắt đầu khởi hành; khẩn trương lên", "pos": "phrase"},
    # 2092: go to sleep
    {"ipa": "/ɡoʊ tuː sliːp/", "vi": "chìm vào giấc ngủ say; đi ngủ", "pos": "phrase"},
    # 2093: ground water
    {"ipa": "/ɡraʊnd ˈwɔːtər/", "vi": "mạch nước ngầm dưới lòng đất", "pos": "phrase"},
    # 2094: happy chance
    {"ipa": "/ˈhæpi tʃæns/", "vi": "dịp may ngẫu nhiên; sự may mắn", "pos": "phrase"},
    # 2095: health club
    {"ipa": "/hɛlθ klʌb/", "vi": "câu lạc bộ chăm sóc thể hình", "pos": "phrase"},
    # 2096: high sign
    {"ipa": "/haɪ saɪn/", "vi": "ám hiệu bí mật bằng tay", "pos": "phrase"},
    # 2097: high technology
    {"ipa": "/haɪ tɛkˈnɑːlədʒi/", "vi": "công nghệ cao tiên tiến", "pos": "phrase"},
    # 2098: higher law
    {"ipa": "/ˈhaɪər lɔː/", "vi": "luật đạo đức tự nhiên tối cao", "pos": "phrase"},
    # 2099: history department
    {"ipa": "/ˈhɪstəri dɪˈpɑːrtmənt/", "vi": "khoa lịch sử viện nghiên cứu", "pos": "phrase"},
]

with open('scratch/b21_r05_raw_p1.json') as f:
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

with open('scratch/b21_r05_p1.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r05_p1.json created successfully and validated!")
