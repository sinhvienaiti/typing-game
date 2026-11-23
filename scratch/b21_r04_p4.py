import json

# Manual word-by-word cognitive review for Batch 21 Round 4 Part 4 (records 1800-1899, IDs 200k.001802 to 200k.001901)
reviewed_entries = [
    # 1800: send off
    {"ipa": "/sɛnd ɔːf/", "vi": "phái đi; tiễn đưa; đuổi khỏi sân", "pos": "phrase"},
    # 1801: service road
    {"ipa": "/ˈsɜːrvɪs roʊd/", "vi": "đường gom dân sinh dọc cao tốc", "pos": "phrase"},
    # 1802: sex change
    {"ipa": "/sɛks tʃeɪndʒ/", "vi": "phẫu thuật chuyển đổi giới tính", "pos": "phrase"},
    # 1803: side road
    {"ipa": "/saɪd roʊd/", "vi": "đường nhánh phụ rẽ", "pos": "phrase"},
    # 1804: sleep in
    {"ipa": "/sliːp ɪn/", "vi": "ngủ nướng; ngủ dậy muộn sáng", "pos": "phrase"},
    # 1805: small town
    {"ipa": "/smɔːl taʊn/", "vi": "thị trấn nhỏ nơi thôn quê", "pos": "phrase"},
    # 1806: stage right
    {"ipa": "/steɪdʒ raɪt/", "vi": "phía cánh phải sân khấu kịch", "pos": "phrase"},
    # 1807: starting time
    {"ipa": "/ˈstɑːrtɪŋ taɪm/", "vi": "thời điểm bắt đầu xuất phát", "pos": "phrase"},
    # 1808: strong point
    {"ipa": "/strɔːŋ pɔɪnt/", "vi": "điểm mạnh sở trường; thế mạnh lớn", "pos": "phrase"},
    # 1809: talking book
    {"ipa": "/ˈtɔːkɪŋ bʊk/", "vi": "sách nói thu âm cho người khiếm thị", "pos": "phrase"},
    # 1810: tv set
    {"ipa": "/ˌtiːˈviː sɛt/", "vi": "máy thu hình tivi gia đình", "pos": "phrase"},
    # 1811: war baby
    {"ipa": "/wɔːr ˈbeɪbi/", "vi": "đứa trẻ sinh ra giữa thời loạn lạc", "pos": "phrase"},
    # 1812: water project
    {"ipa": "/ˈwɔːtər ˈprɑːdʒɛkt/", "vi": "dự án công trình thủy lợi cấp nước", "pos": "phrase"},
    # 1813: age class
    {"ipa": "/eɪdʒ klæs/", "vi": "nhóm phân loại lứa tuổi", "pos": "phrase"},
    # 1814: art history
    {"ipa": "/ɑːrt ˈhɪstəri/", "vi": "lịch sử mỹ thuật hội họa", "pos": "phrase"},
    # 1815: box in
    {"ipa": "/bɑːks ɪn/", "vi": "dồn vào thế bí; bao vây nhốt chặt", "pos": "phrase"},
    # 1816: build in
    {"ipa": "/bɪld ɪn/", "vi": "tích hợp sẵn bên trong hệ thống", "pos": "phrase"},
    # 1817: check bit
    {"ipa": "/tʃɛk bɪt/", "vi": "bit kiểm tra tính chẵn lẻ dữ liệu", "pos": "phrase"},
    # 1818: check girl
    {"ipa": "/tʃɛk ɡɜːrl/", "vi": "nữ nhân viên nhận giữ áo khoác", "pos": "phrase"},
    # 1819: city boy
    {"ipa": "/ˈsɪti bɔɪ/", "vi": "chàng trai thị thành; công tử phố", "pos": "phrase"},
    # 1820: common person
    {"ipa": "/ˈkɑːmən ˈpɜːrsən/", "vi": "người dân thường; thứ dân bình dân", "pos": "phrase"},
    # 1821: course of study
    {"ipa": "/kɔːrs ʌv ˈstʌdi/", "vi": "chương trình giáo trình học tập", "pos": "phrase"},
    # 1822: drive around
    {"ipa": "/draɪv əˈraʊnd/", "vi": "lái xe chạy dạo quanh ngắm phố", "pos": "phrase"},
    # 1823: earth up
    {"ipa": "/ɜːrθ ʌp/", "vi": "vun đất đắp gốc cây trồng", "pos": "phrase"},
    # 1824: english system
    {"ipa": "/ˈɪŋɡlɪʃ ˈsɪstəm/", "vi": "hệ thống đo lường truyền thống Anh", "pos": "phrase"},
    # 1825: field general
    {"ipa": "/fiːld ˈdʒɛnərəl/", "vi": "tướng chỉ huy thực địa; thủ lĩnh", "pos": "phrase"},
    # 1826: film making
    {"ipa": "/fɪlm ˈmeɪkɪŋ/", "vi": "nghệ thuật sản xuất làm phim", "pos": "phrase"},
    # 1827: food market
    {"ipa": "/fuːd ˈmɑːrkɪt/", "vi": "chợ buôn bán thực phẩm đồ ăn", "pos": "phrase"},
    # 1828: home key
    {"ipa": "/hoʊm kiː/", "vi": "giọng chủ trong bản hòa âm", "pos": "phrase"},
    # 1829: home page
    {"ipa": "/hoʊm peɪdʒ/", "vi": "trang chủ trang web chính", "pos": "phrase"},
    # 1830: home range
    {"ipa": "/hoʊm reɪndʒ/", "vi": "địa bàn sinh sống quen thuộc", "pos": "phrase"},
    # 1831: john major
    {"ipa": "/dʒɑːn ˈmeɪdʒər/", "vi": "Thủ tướng Anh John Major", "pos": "phrase"},
    # 1832: life style
    {"ipa": "/laɪf staɪl/", "vi": "phong cách lối sống sinh hoạt", "pos": "phrase"},
    # 1833: line of force
    {"ipa": "/laɪn ʌv fɔːrs/", "vi": "đường sức từ trường điện trường", "pos": "phrase"},
    # 1834: little league
    {"ipa": "/ˈlɪtəl liːɡ/", "vi": "Giải bóng chày thiếu nhi Mỹ", "pos": "phrase"},
    # 1835: living room
    {"ipa": "/ˈlɪvɪŋ ruːm/", "vi": "phòng khách sinh hoạt gia đình", "pos": "phrase"},
    # 1836: look forward
    {"ipa": "/lʊk ˈfɔːrwərd/", "vi": "trông đợi; ngóng chờ háo hức", "pos": "phrase"},
    # 1837: look upon
    {"ipa": "/lʊk əˈpɑːn/", "vi": "coi như là; nhìn nhận đánh giá", "pos": "phrase"},
    # 1838: market research
    {"ipa": "/ˈmɑːrkɪt rɪˈsɜːrtʃ/", "vi": "nghiên cứu khảo sát thị trường", "pos": "phrase"},
    # 1839: middle name
    {"ipa": "/ˈmɪdəl neɪm/", "vi": "tên lót; tên đệm trong khai sinh", "pos": "phrase"},
    # 1840: mother country
    {"ipa": "/ˈmʌðər ˈkʌntri/", "vi": "đất mẹ quê hương; chính quốc", "pos": "phrase"},
    # 1841: office building
    {"ipa": "/ˈɔːfɪs ˈbɪldɪŋ/", "vi": "tòa nhà cao ốc văn phòng", "pos": "phrase"},
    # 1842: on the table
    {"ipa": "/ɑːn ðə ˈteɪbəl/", "vi": "được đem ra bàn thảo đàm phán", "pos": "phrase"},
    # 1843: out of practice
    {"ipa": "/aʊt ʌv ˈpræktɪs/", "vi": "lụt nghề do lâu ngày không tập", "pos": "phrase"},
    # 1844: pass by
    {"ipa": "/pæs baɪ/", "vi": "đi lướt qua; bỏ qua cơ hội", "pos": "phrase"},
    # 1845: personal business
    {"ipa": "/ˈpɜːrsənəl ˈbɪznəs/", "vi": "việc riêng tư; công việc cá nhân", "pos": "phrase"},
    # 1846: personal care
    {"ipa": "/ˈpɜːrsənəl kɛr/", "vi": "chăm sóc vệ sinh cá nhân hàng ngày", "pos": "phrase"},
    # 1847: pick over
    {"ipa": "/pɪk ˈoʊvər/", "vi": "chọn lọc kỹ càng; loại bỏ thứ xấu", "pos": "phrase"},
    # 1848: quality of life
    {"ipa": "/ˈkwɑːləti ʌv laɪf/", "vi": "chất lượng đời sống con người", "pos": "phrase"},
    # 1849: ready to hand
    {"ipa": "/ˈrɛdi tuː hænd/", "vi": "sẵn sàng trong tầm tay với lấy", "pos": "phrase"},
    # 1850: security system
    {"ipa": "/sɪˈkjʊrəti ˈsɪstəm/", "vi": "hệ thống an ninh camera chống trộm", "pos": "phrase"},
    # 1851: send down
    {"ipa": "/sɛnd daʊn/", "vi": "đình chỉ đuổi học tạm thời; bỏ tù", "pos": "phrase"},
    # 1852: service department
    {"ipa": "/ˈsɜːrvɪs dɪˈpɑːrtmənt/", "vi": "bộ phận chăm sóc khách hàng", "pos": "phrase"},
    # 1853: show bill
    {"ipa": "/ʃoʊ bɪl/", "vi": "tờ áp phích quảng cáo diễn kịch", "pos": "phrase"},
    # 1854: sign over
    {"ipa": "/saɪn ˈoʊvər/", "vi": "ký chuyển nhượng quyền sở hữu", "pos": "phrase"},
    # 1855: sleep with
    {"ipa": "/sliːp wɪð/", "vi": "ngủ với; quan hệ tình dục cùng", "pos": "phrase"},
    # 1856: take stage
    {"ipa": "/teɪk steɪdʒ/", "vi": "chiếm lĩnh sân khấu; thu hút chú ý", "pos": "phrase"},
    # 1857: take the stage
    {"ipa": "/teɪk ðə steɪdʒ/", "vi": "bước lên sân khấu tỏa sáng", "pos": "phrase"},
    # 1858: third class
    {"ipa": "/θɜːrd klæs/", "vi": "vé tàu hạng ba; loại tầm thường", "pos": "phrase"},
    # 1859: united states government
    {"ipa": "/juːˈnaɪtɪd steɪts ˈɡʌvərmənt/", "vi": "Chính phủ Hợp chúng quốc Hoa Kỳ", "pos": "phrase"},
    # 1860: vote down
    {"ipa": "/voʊt daʊn/", "vi": "bỏ phiếu bác bỏ dự luật", "pos": "phrase"},
    # 1861: walk over
    {"ipa": "/wɔːk ˈoʊvər/", "vi": "thắng dễ như bỡn; ức hiếp ai", "pos": "phrase"},
    # 1862: wall in
    {"ipa": "/wɔːl ɪn/", "vi": "xây tường bao kín vây chặt", "pos": "phrase"},
    # 1863: world cup
    {"ipa": "/wɜːrld kʌp/", "vi": "Cúp bóng đá thế giới World Cup", "pos": "phrase"},
    # 1864: gamer
    {"ipa": "/ˈɡeɪmər/", "vi": "can đảm hơn; gan góc chịu chơi hơn", "pos": "adj"},
    # 1865: gamest
    {"ipa": "/ˈɡeɪmɪst/", "vi": "can đảm nhất; gan dạ quả cảm nhất", "pos": "adj"},
    # 1866: access time
    {"ipa": "/ˈækˌsɛs taɪm/", "vi": "thời gian truy xuất bộ nhớ máy", "pos": "phrase"},
    # 1867: action at law
    {"ipa": "/ˈækʃən æt lɔː/", "vi": "vụ kiện tụng tố tụng pháp lý", "pos": "phrase"},
    # 1868: baby talk
    {"ipa": "/ˈbeɪbi tɔːk/", "vi": "tiếng bi bô của trẻ thơ", "pos": "phrase"},
    # 1869: back door
    {"ipa": "/bæk dɔːr/", "vi": "cửa sau nhà; đường luồn lách ngầm", "pos": "phrase"},
    # 1870: body process
    {"ipa": "/ˈbɑːdi ˈprɑːsɛs/", "vi": "quá trình sinh lý bên trong cơ thể", "pos": "phrase"},
    # 1871: body type
    {"ipa": "/ˈbɑːdi taɪp/", "vi": "tạng người; vóc dáng thể chất", "pos": "phrase"},
    # 1872: british system
    {"ipa": "/ˈbrɪtɪʃ ˈsɪstəm/", "vi": "hệ thống đo lường khối đế quốc Anh", "pos": "phrase"},
    # 1873: build on
    {"ipa": "/bɪld ɑːn/", "vi": "xây dựng dựa trên nền tảng sẵn", "pos": "phrase"},
    # 1874: by the piece
    {"ipa": "/baɪ ðə piːs/", "vi": "tính theo từng món; ăn lương khoán", "pos": "phrase"},
    # 1875: chief of state
    {"ipa": "/tʃiːf ʌv steɪt/", "vi": "nguyên thủ quốc gia đứng đầu nước", "pos": "phrase"},
    # 1876: class act
    {"ipa": "/klæs ækt/", "vi": "người tài hoa đẳng cấp lịch lãm", "pos": "phrase"},
    # 1877: club head
    {"ipa": "/klʌb hɛd/", "vi": "đầu gậy đánh gôn", "pos": "phrase"},
    # 1878: college level
    {"ipa": "/ˈkɑːlɪdʒ ˈlɛvəl/", "vi": "trình độ giáo dục bậc đại học", "pos": "phrase"},
    # 1879: come forward
    {"ipa": "/kʌm ˈfɔːrwərd/", "vi": "đứng ra xung phong; ra trình báo", "pos": "phrase"},
    # 1880: come upon
    {"ipa": "/kʌm əˈpɑːn/", "vi": "tình cờ bắt gặp; bất chợt ập đến", "pos": "phrase"},
    # 1881: course of action
    {"ipa": "/kɔːrs ʌv ˈækʃən/", "vi": "phương hướng hành động chiến lược", "pos": "phrase"},
    # 1882: date line
    {"ipa": "/deɪt laɪn/", "vi": "đường đổi ngày quốc tế", "pos": "phrase"},
    # 1883: dead person
    {"ipa": "/dɛd ˈpɜːrsən/", "vi": "người quá cố; thi hài người đã mất", "pos": "phrase"},
    # 1884: die back
    {"ipa": "/daɪ bæk/", "vi": "chết khô ngọn cây; tàn lụi từ ngọn", "pos": "phrase"},
    # 1885: election day
    {"ipa": "/ɪˈlɛkʃən deɪ/", "vi": "ngày hội cử tri toàn quốc đi bầu", "pos": "phrase"},
    # 1886: english person
    {"ipa": "/ˈɪŋɡlɪʃ ˈpɜːrsən/", "vi": "người mang quốc tịch Anh", "pos": "phrase"},
    # 1887: fall under
    {"ipa": "/fɔːl ˈʌndər/", "vi": "thuộc phạm vi diện; chịu ảnh hưởng", "pos": "phrase"},
    # 1888: family relationship
    {"ipa": "/ˈfæməli rɪˈleɪʃənˌʃɪp/", "vi": "mối quan hệ họ hàng ruột thịt", "pos": "phrase"},
    # 1889: financial year
    {"ipa": "/faɪˈnænʃəl jɪr/", "vi": "năm tài chính; niên độ kế toán", "pos": "phrase"},
    # 1890: form class
    {"ipa": "/fɔːrm klæs/", "vi": "từ loại trong ngữ pháp ngôn ngữ", "pos": "phrase"},
    # 1891: free press
    {"ipa": "/friː prɛs/", "vi": "báo chí truyền thông độc lập tự do", "pos": "phrase"},
    # 1892: front matter
    {"ipa": "/frʌnt ˈmætər/", "vi": "phần lời mở đầu tựa đầu sách", "pos": "phrase"},
    # 1893: front room
    {"ipa": "/frʌnt ruːm/", "vi": "phòng phía trước nhà; phòng khách", "pos": "phrase"},
    # 1894: good old boy
    {"ipa": "/ɡʊd oʊld bɔɪ/", "vi": "anh bạn chân quê miền Nam nước Mỹ", "pos": "phrase"},
    # 1895: great dog
    {"ipa": "/ɡreɪt dɔːɡ/", "vi": "chòm sao Đại Khuyển trên bầu trời", "pos": "phrase"},
    # 1896: hard lead
    {"ipa": "/hɑːrd lɛd/", "vi": "hợp kim chì cứng chứa antimon", "pos": "phrase"},
    # 1897: hold water
    {"ipa": "/hoʊld ˈwɔːtər/", "vi": "đứng vững lý lẽ; kín nước không rò", "pos": "phrase"},
    # 1898: interest group
    {"ipa": "/ˈɪntrəst ɡruːp/", "vi": "nhóm lợi ích chính trị vận động", "pos": "phrase"},
    # 1899: kill off
    {"ipa": "/kɪl ɔːf/", "vi": "tiêu diệt tận gốc; giết sạch", "pos": "phrase"},
]

with open('scratch/b21_r04_raw_p4.json') as f:
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

with open('scratch/b21_r04_p4.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r04_p4.json created successfully and validated!")
