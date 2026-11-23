import json

# Manual word-by-word cognitive review for Batch 21 Round 4 Part 3 (records 1700-1799, IDs 200k.001702 to 200k.001801)
reviewed_entries = [
    # 1700: black art
    {"ipa": "/blæk ɑːrt/", "vi": "ma thuật hắc ám; thuật phù thủy", "pos": "phrase"},
    # 1701: black market
    {"ipa": "/blæk ˈmɑːrkɪt/", "vi": "chợ đen; thị trường chợ đen", "pos": "phrase"},
    # 1702: business department
    {"ipa": "/ˈbɪznəs dɪˈpɑːrtmənt/", "vi": "phòng kinh doanh; khoa quản trị", "pos": "phrase"},
    # 1703: buy food
    {"ipa": "/baɪ fuːd/", "vi": "mua thức ăn sẵn; mua đồ ăn", "pos": "phrase"},
    # 1704: coming into court
    {"ipa": "/ˈkʌmɪŋ ˈɪntuː kɔːrt/", "vi": "sự trình diện trước tòa án", "pos": "phrase"},
    # 1705: cover up
    {"ipa": "/ˈkʌvər ʌp/", "vi": "che đậy bưng bít; áo choàng ngoài", "pos": "phrase"},
    # 1706: drive off
    {"ipa": "/draɪv ɔːf/", "vi": "xua đuổi đi; lái xe rời đi", "pos": "phrase"},
    # 1707: fall down
    {"ipa": "/fɔːl daʊn/", "vi": "ngã quỵ xuống đất; đổ sụp", "pos": "phrase"},
    # 1708: fall off
    {"ipa": "/fɔːl ɔːf/", "vi": "sụt giảm số lượng; rơi khỏi", "pos": "phrase"},
    # 1709: fall through
    {"ipa": "/fɔːl θruː/", "vi": "đổ vỡ thất bại kế hoạch", "pos": "phrase"},
    # 1710: first language
    {"ipa": "/fɜːrst ˈlæŋɡwɪdʒ/", "vi": "tiếng mẹ đẻ; ngôn ngữ thứ nhất", "pos": "phrase"},
    # 1711: follow through
    {"ipa": "/ˈfɑːloʊ θruː/", "vi": "làm đến nơi đến chốn; vung vợt tiếp", "pos": "phrase"},
    # 1712: french people
    {"ipa": "/frɛntʃ ˈpiːpəl/", "vi": "người dân nước Pháp", "pos": "phrase"},
    # 1713: full term
    {"ipa": "/fʊl tɜːrm/", "vi": "sinh đủ tháng; trọn nhiệm kỳ", "pos": "phrase"},
    # 1714: ground state
    {"ipa": "/ɡraʊnd steɪt/", "vi": "trạng thái cơ bản trong vật lý", "pos": "phrase"},
    # 1715: head word
    {"ipa": "/hɛd wɜːrd/", "vi": "từ trung tâm; từ mục từ từ điển", "pos": "phrase"},
    # 1716: high church
    {"ipa": "/haɪ tʃɜːrtʃ/", "vi": "phái Thượng Giáo hội Anh giáo", "pos": "phrase"},
    # 1717: highs
    {"ipa": "/haɪz/", "vi": "các mức đỉnh cao; thời kỳ hoàng kim", "pos": "noun"},
    # 1718: home ground
    {"ipa": "/hoʊm ɡraʊnd/", "vi": "sân nhà quen thuộc; môi trường sống", "pos": "phrase"},
    # 1719: home stand
    {"ipa": "/hoʊm stænd/", "vi": "loạt trận thi đấu trên sân nhà", "pos": "phrase"},
    # 1720: job action
    {"ipa": "/dʒɑːb ˈækʃən/", "vi": "đình công biểu tình đòi quyền lợi", "pos": "phrase"},
    # 1721: line of march
    {"ipa": "/laɪn ʌv mɑːrtʃ/", "vi": "lộ trình hành quân của đoàn quân", "pos": "phrase"},
    # 1722: listen in
    {"ipa": "/ˈlɪsən ɪn/", "vi": "nghe lén; theo dõi đường truyền", "pos": "phrase"},
    # 1723: littlest
    {"ipa": "/ˈlɪtəlɪst/", "vi": "nhỏ bé nhất; ít ỏi nhất", "pos": "adj"},
    # 1724: morning room
    {"ipa": "/ˈmɔːrnɪŋ ruːm/", "vi": "phòng khách nhỏ ngồi ban sáng", "pos": "phrase"},
    # 1725: news media
    {"ipa": "/nuːz ˈmiːdiə/", "vi": "báo chí truyền thông tin tức", "pos": "phrase"},
    # 1726: night club
    {"ipa": "/naɪt klʌb/", "vi": "hộp đêm; vũ trường giải trí", "pos": "phrase"},
    # 1727: on paper
    {"ipa": "/ɑːn ˈpeɪpər/", "vi": "trên lý thuyết; nằm trên giấy tờ", "pos": "phrase"},
    # 1728: period of play
    {"ipa": "/ˈpɪriəd ʌv pleɪ/", "vi": "thời gian diễn ra trận đấu", "pos": "phrase"},
    # 1729: phone book
    {"ipa": "/foʊn bʊk/", "vi": "cuốn danh bạ số điện thoại", "pos": "phrase"},
    # 1730: pick out
    {"ipa": "/pɪk aʊt/", "vi": "chọn lọc ra; nhận ra giữa đám đông", "pos": "phrase"},
    # 1731: pick up
    {"ipa": "/pɪk ʌp/", "vi": "nhặt lên; đón rước ai; hồi phục", "pos": "phrase"},
    # 1732: poor people
    {"ipa": "/pʊr ˈpiːpəl/", "vi": "người nghèo khó cơ hàn", "pos": "phrase"},
    # 1733: program line
    {"ipa": "/ˈproʊɡræm laɪn/", "vi": "dòng mã lệnh lập trình", "pos": "phrase"},
    # 1734: record company
    {"ipa": "/ˈrɛkərd ˈkʌmpəni/", "vi": "công ty hãng đĩa thu âm", "pos": "phrase"},
    # 1735: room light
    {"ipa": "/ruːm laɪt/", "vi": "ánh sáng đèn trong phòng", "pos": "phrase"},
    # 1736: running start
    {"ipa": "/ˈrʌnɪŋ stɑːrt/", "vi": "khởi đầu thuận lợi có đà sẵn", "pos": "phrase"},
    # 1737: send back
    {"ipa": "/sɛnd bæk/", "vi": "gửi trả lại; đuổi về nước", "pos": "phrase"},
    # 1738: service of process
    {"ipa": "/ˈsɜːrvɪs ʌv ˈprɑːsɛs/", "vi": "thủ tục tống đạt trát hầu tòa", "pos": "phrase"},
    # 1739: service program
    {"ipa": "/ˈsɜːrvɪs ˈproʊɡræm/", "vi": "chương trình phần mềm tiện ích", "pos": "phrase"},
    # 1740: set shot
    {"ipa": "/sɛt ʃɑːt/", "vi": "cú ném rổ đứng yên tại chỗ", "pos": "phrase"},
    # 1741: sign up
    {"ipa": "/saɪn ʌp/", "vi": "đăng ký tham gia khóa học", "pos": "phrase"},
    # 1742: step down
    {"ipa": "/stɛp daʊn/", "vi": "từ chức; hạ điện áp máy biến thế", "pos": "phrase"},
    # 1743: united front
    {"ipa": "/juːˈnaɪtɪd frʌnt/", "vi": "mặt trận thống nhất liên minh", "pos": "phrase"},
    # 1744: us post office
    {"ipa": "/juː ɛs poʊst ˈɔːfɪs/", "vi": "Bưu chính Hoa Kỳ; bưu điện Mỹ", "pos": "phrase"},
    # 1745: walk about
    {"ipa": "/wɔːk əˈbaʊt/", "vi": "đi dạo bát phố; vi hành gặp dân", "pos": "phrase"},
    # 1746: walk out
    {"ipa": "/wɔːk aʊt/", "vi": "bỏ ra ngoài đình công phản đối", "pos": "phrase"},
    # 1747: walk out of
    {"ipa": "/wɔːk aʊt ʌv/", "vi": "bước ra khỏi phòng họp biểu tình", "pos": "phrase"},
    # 1748: water main
    {"ipa": "/ˈwɔːtər meɪn/", "vi": "đường ống cấp nước chính đô thị", "pos": "phrase"},
    # 1749: whole works
    {"ipa": "/hoʊl wɜːrks/", "vi": "tất tần tật mọi thứ; trọn bộ đồ", "pos": "phrase"},
    # 1750: word order
    {"ipa": "/wɜːrd ˈɔːrdər/", "vi": "trật tự sắp xếp từ trong câu", "pos": "phrase"},
    # 1751: across the country
    {"ipa": "/əˈkrɔːs ðə ˈkʌntri/", "vi": "trên khắp cả nước; toàn quốc", "pos": "phrase"},
    # 1752: at sea
    {"ipa": "/æt siː/", "vi": "lênh đênh ngoài biển; bối rối", "pos": "phrase"},
    # 1753: break away
    {"ipa": "/breɪk əˈweɪ/", "vi": "thoát ly ly khai; bứt phá bứt tốc", "pos": "phrase"},
    # 1754: case shot
    {"ipa": "/keɪs ʃɑːt/", "vi": "loại đạn pháo chùm sát thương", "pos": "phrase"},
    # 1755: church school
    {"ipa": "/tʃɜːrtʃ skuːl/", "vi": "trường học giáo xứ dòng tu", "pos": "phrase"},
    # 1756: city center
    {"ipa": "/ˈsɪti ˈsɛntər/", "vi": "trung tâm thành phố sầm uất", "pos": "phrase"},
    # 1757: come round
    {"ipa": "/kʌm raʊnd/", "vi": "hồi tỉnh lại; ghé qua chơi; đổi ý", "pos": "phrase"},
    # 1758: dead set
    {"ipa": "/dɛd sɛt/", "vi": "kiên quyết phản đối; dốc toàn lực", "pos": "phrase"},
    # 1759: department head
    {"ipa": "/dɪˈpɑːrtmənt hɛd/", "vi": "trưởng phòng ban; chủ nhiệm khoa", "pos": "phrase"},
    # 1760: department of music
    {"ipa": "/dɪˈpɑːrtmənt ʌv ˈmjuːzɪk/", "vi": "khoa âm nhạc trường đại học", "pos": "phrase"},
    # 1761: die out
    {"ipa": "/daɪ aʊt/", "vi": "tuyệt chủng dần biến mất", "pos": "phrase"},
    # 1762: drive home
    {"ipa": "/draɪv hoʊm/", "vi": "làm cho thấu hiểu; nhấn mạnh rõ", "pos": "phrase"},
    # 1763: due north
    {"ipa": "/djuː nɔːrθ/", "vi": "hướng thẳng chính bắc", "pos": "phrase"},
    # 1764: fall in love
    {"ipa": "/fɔːl ɪn lʌv/", "vi": "phải lòng say đắm; yêu tha thiết", "pos": "phrase"},
    # 1765: fall of man
    {"ipa": "/fɔːl ʌv mæn/", "vi": "sự sa ngã của loài người nguyên tội", "pos": "phrase"},
    # 1766: field line
    {"ipa": "/fiːld laɪn/", "vi": "đường sức từ trong điện từ học", "pos": "phrase"},
    # 1767: figure out
    {"ipa": "/ˈfɪɡjər aʊt/", "vi": "tìm ra cách giải quyết; hiểu ra", "pos": "phrase"},
    # 1768: film company
    {"ipa": "/fɪlm ˈkʌmpəni/", "vi": "công ty sản xuất phim điện ảnh", "pos": "phrase"},
    # 1769: fire control
    {"ipa": "/ˈfaɪər kənˈtroʊl/", "vi": "hệ thống kiểm soát hỏa lực quân sự", "pos": "phrase"},
    # 1770: government security
    {"ipa": "/ˈɡʌvərmənt sɪˈkjʊrəti/", "vi": "chứng khoán công trái chính phủ", "pos": "phrase"},
    # 1771: high ground
    {"ipa": "/haɪ ɡraʊnd/", "vi": "vị thế đạo đức cao; địa lợi cao", "pos": "phrase"},
    # 1772: in truth
    {"ipa": "/ɪn truːθ/", "vi": "thực tế thật lòng mà nói", "pos": "phrase"},
    # 1773: life science
    {"ipa": "/laɪf ˈsaɪəns/", "vi": "khoa học đời sống sinh học", "pos": "phrase"},
    # 1774: light air
    {"ipa": "/laɪt ɛr/", "vi": "làn gió thoảng cấp một nhẹ", "pos": "phrase"},
    # 1775: like crazy
    {"ipa": "/laɪk ˈkreɪzi/", "vi": "như điên dại; dữ dội cuồng nhiệt", "pos": "phrase"},
    # 1776: living death
    {"ipa": "/ˈlɪvɪŋ dɛθ/", "vi": "sống khổ như chết; cuộc sống mòn", "pos": "phrase"},
    # 1777: local street
    {"ipa": "/ˈloʊkəl striːt/", "vi": "đường nội bộ dân sinh khu vực", "pos": "phrase"},
    # 1778: lord it over
    {"ipa": "/lɔːrd ɪt ˈoʊvər/", "vi": "lên mặt hách dịch trịch thượng với", "pos": "phrase"},
    # 1779: love match
    {"ipa": "/lʌv mætʃ/", "vi": "hôn nhân bắt nguồn từ tình yêu", "pos": "phrase"},
    # 1780: main line
    {"ipa": "/meɪn laɪn/", "vi": "tuyến đường sắt chính; chính thống", "pos": "phrase"},
    # 1781: medical school
    {"ipa": "/ˈmɛdɪkəl skuːl/", "vi": "trường đại học y khoa đào tạo", "pos": "phrase"},
    # 1782: meeting house
    {"ipa": "/ˈmiːtɪŋ haʊs/", "vi": "nhà hội thánh; nơi sinh hoạt chung", "pos": "phrase"},
    # 1783: meeting place
    {"ipa": "/ˈmiːtɪŋ pleɪs/", "vi": "địa điểm tụ họp hội ngộ chung", "pos": "phrase"},
    # 1784: military government
    {"ipa": "/ˈmɪlətɛri ˈɡʌvərmənt/", "vi": "chính quyền quân sự lâm thời", "pos": "phrase"},
    # 1785: military group
    {"ipa": "/ˈmɪlətɛri ɡruːp/", "vi": "đoàn thể lực lượng quân nhân", "pos": "phrase"},
    # 1786: movie house
    {"ipa": "/ˈmuːvi haʊs/", "vi": "rạp chiếu phim rạp chiếu bóng", "pos": "phrase"},
    # 1787: music department
    {"ipa": "/ˈmjuːzɪk dɪˈpɑːrtmənt/", "vi": "khoa đào tạo âm nhạc", "pos": "phrase"},
    # 1788: news program
    {"ipa": "/nuːz ˈproʊɡræm/", "vi": "chương trình tin tức truyền hình", "pos": "phrase"},
    # 1789: oil well
    {"ipa": "/ɔɪl wɛl/", "vi": "giếng khai thác dầu mỏ", "pos": "phrase"},
    # 1790: on earth
    {"ipa": "/ɑːn ɜːrθ/", "vi": "trên thế gian này; rốt cuộc là", "pos": "phrase"},
    # 1791: pass on
    {"ipa": "/pæs ɑːn/", "vi": "truyền lại đời sau; qua đời", "pos": "phrase"},
    # 1792: price support
    {"ipa": "/praɪs səˈpɔːrt/", "vi": "chính sách trợ giá nông sản", "pos": "phrase"},
    # 1793: property right
    {"ipa": "/ˈprɑːpərti raɪt/", "vi": "quyền sở hữu tài sản pháp định", "pos": "phrase"},
    # 1794: public security
    {"ipa": "/ˈpʌblɪk sɪˈkjʊrəti/", "vi": "an ninh trật tự công cộng", "pos": "phrase"},
    # 1795: rest stop
    {"ipa": "/rɛst stɑːp/", "vi": "trạm dừng chân cao tốc nghỉ ngơi", "pos": "phrase"},
    # 1796: right stage
    {"ipa": "/raɪt steɪdʒ/", "vi": "phía cánh phải của sân khấu kịch", "pos": "phrase"},
    # 1797: right to vote
    {"ipa": "/raɪt tuː voʊt/", "vi": "quyền bầu cử phổ thông công dân", "pos": "phrase"},
    # 1798: run across
    {"ipa": "/rʌn əˈkrɔːs/", "vi": "tình cờ bắt gặp; chạy băng qua", "pos": "phrase"},
    # 1799: running head
    {"ipa": "/ˈrʌnɪŋ hɛd/", "vi": "tiêu đề đầu trang sách", "pos": "phrase"},
]

with open('scratch/b21_r04_raw_p3.json') as f:
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

with open('scratch/b21_r04_p3.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r04_p3.json created successfully and validated!")
