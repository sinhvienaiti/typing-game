import json

raw_items = json.load(open("scratch/b22_r02_raw_p3.json"))

reviews = [
    # 00: government officials
    {"pos": "phrase", "ipa": "/ˈɡʌvərnmənt əˈfɪʃlz/", "vi": "các quan chức chính phủ"},
    # 01: guide word
    {"pos": "phrase", "ipa": "/ɡaɪd wɜːrd/", "vi": "từ chỉ dẫn đầu trang từ điển"},
    # 02: hearing loss
    {"pos": "phrase", "ipa": "/ˈhɪrɪŋ lɔːs/", "vi": "suy giảm thính lực; khiếm thính"},
    # 03: high holiday
    {"pos": "phrase", "ipa": "/haɪ ˈhɑːlədeɪ/", "vi": "đại lễ Do Thái giáo"},
    # 04: hold dear
    {"pos": "phrase", "ipa": "/hoʊld dɪr/", "vi": "trân trọng; yêu quý hết lòng"},
    # 05: housing industry
    {"pos": "phrase", "ipa": "/ˈhaʊzɪŋ ˈɪndəstri/", "vi": "ngành xây dựng nhà ở"},
    # 06: ice mass
    {"pos": "phrase", "ipa": "/aɪs mæs/", "vi": "khối băng lớn; khối băng trôi"},
    # 07: in passing
    {"pos": "phrase", "ipa": "/ɪn ˈpæsɪŋ/", "vi": "nhân tiện; tiện thể nhắc qua"},
    # 08: intelligence information
    {"pos": "phrase", "ipa": "/ɪnˈtɛlɪdʒəns ˌɪnfərˈmeɪʃn/", "vi": "thông tin tình báo mật"},
    # 09: intelligence service
    {"pos": "phrase", "ipa": "/ɪnˈtɛlɪdʒəns ˈsɜːrvɪs/", "vi": "cơ quan tình báo; ngành tình báo"},
    # 10: labour party
    {"pos": "phrase", "ipa": "/ˈleɪbər ˈpɑːrti/", "vi": "Đảng Lao động Anh"},
    # 11: lake bed
    {"pos": "phrase", "ipa": "/leɪk bɛd/", "vi": "đáy hồ; lòng hồ thủy điện"},
    # 12: last laugh
    {"pos": "phrase", "ipa": "/læst læf/", "vi": "thắng lợi cuối cùng; nụ cười sau"},
    # 13: lay into
    {"pos": "phrase", "ipa": "/leɪ ˈɪntuː/", "vi": "chỉ trích gay gắt; đánh tới tấp"},
    # 14: lay out
    {"pos": "phrase", "ipa": "/leɪ aʊt/", "vi": "bố trí trình bày; chi tiêu tiền"},
    # 15: lay up
    {"pos": "phrase", "ipa": "/leɪ ʌp/", "vi": "nằm liệt giường; lưu kho bảo dưỡng"},
    # 16: league of nations
    {"pos": "phrase", "ipa": "/liːɡ əv ˈneɪʃnz/", "vi": "Hội Quốc Liên tiền thân LHQ"},
    # 17: learned response
    {"pos": "phrase", "ipa": "/ˈlɜːrnɪd rɪˈspɑːns/", "vi": "phản xạ có điều kiện do học tập"},
    # 18: light arm
    {"pos": "phrase", "ipa": "/laɪt ɑːrm/", "vi": "vũ khí bộ binh hạng nhẹ"},
    # 19: light reaction
    {"pos": "phrase", "ipa": "/laɪt riˈækʃn/", "vi": "pha sáng quang hợp"},
    # 20: machine gun
    {"pos": "phrase", "ipa": "/məˈʃiːn ɡʌn/", "vi": "súng máy liên thanh"},
    # 21: main file
    {"pos": "phrase", "ipa": "/meɪn faɪl/", "vi": "tệp chính; tập tin dữ liệu chính"},
    # 22: majority operation
    {"pos": "phrase", "ipa": "/məˈdʒɔːrəti ˌɑːpəˈreɪʃn/", "vi": "phép toán đa số logic ngưỡng"},
    # 23: man of letters
    {"pos": "phrase", "ipa": "/mæn əv ˈlɛtərz/", "vi": "nhà văn học; học giả uyên bác"},
    # 24: mental hospital
    {"pos": "phrase", "ipa": "/ˈmɛntl ˈhɑːspɪtl/", "vi": "bệnh viện tâm thần"},
    # 25: middle eastern
    {"pos": "phrase", "ipa": "/ˌmɪdl ˈiːstərn/", "vi": "thuộc vùng Trung Đông"},
    # 26: military vehicle
    {"pos": "phrase", "ipa": "/ˈmɪlətɛri ˈviːəkl/", "vi": "xe quân sự; phương tiện chiến đấu"},
    # 27: mobile river
    {"pos": "phrase", "ipa": "/moʊˈbiːl ˈrɪvər/", "vi": "sông Mobile ở Alabama"},
    # 28: murder charge
    {"pos": "phrase", "ipa": "/ˈmɜːrdər tʃɑːrdʒ/", "vi": "cáo buộc tội danh giết người"},
    # 29: national debt
    {"pos": "phrase", "ipa": "/ˈnæʃnəl dɛt/", "vi": "nợ công quốc gia; nợ chính phủ"},
    # 30: native american
    {"pos": "phrase", "ipa": "/ˈneɪtɪv əˈmɛrɪkən/", "vi": "người Mỹ bản địa; thổ dân da đỏ"},
    # 31: new york bay
    {"pos": "phrase", "ipa": "/njuː jɔːrk beɪ/", "vi": "vịnh New York"},
    # 32: northern europe
    {"pos": "phrase", "ipa": "/ˈnɔːrðərn ˈjʊərəp/", "vi": "vùng Bắc Âu; các nước Bắc Âu"},
    # 33: old italian
    {"pos": "phrase", "ipa": "/oʊld ɪˈtæljən/", "vi": "tiếng Ý cổ xưa"},
    # 34: one hundred five
    {"pos": "phrase", "ipa": "/wʌn ˈhʌndrəd faɪv/", "vi": "một trăm lẻ năm"},
    # 35: one thousand
    {"pos": "phrase", "ipa": "/wʌn ˈθaʊznd/", "vi": "một nghìn; một ngàn"},
    # 36: operating cost
    {"pos": "phrase", "ipa": "/ˈɑːpəreɪtɪŋ kɔːst/", "vi": "chi phí vận hành hoạt động"},
    # 37: phase out
    {"pos": "phrase", "ipa": "/feɪz aʊt/", "vi": "loại bỏ dần dần; xóa sổ từng bước"},
    # 38: picture window
    {"pos": "phrase", "ipa": "/ˈpɪktʃər ˈwɪndoʊ/", "vi": "cửa sổ kính lớn nhìn toàn cảnh"},
    # 39: point of honor
    {"pos": "phrase", "ipa": "/pɔɪnt əv ˈɑːnər/", "vi": "vấn đề danh dự; điều tự trọng"},
    # 40: power of attorney
    {"pos": "phrase", "ipa": "/ˈpaʊər əv əˈtɜːrni/", "vi": "giấy ủy quyền pháp lý"},
    # 41: power user
    {"pos": "phrase", "ipa": "/ˈpaʊər ˈjuːzər/", "vi": "người dùng thành thạo nâng cao"},
    # 42: public transport
    {"pos": "phrase", "ipa": "/ˈpʌblɪk ˈtrænspɔːrt/", "vi": "phương tiện giao thông công cộng"},
    # 43: quiet down
    {"pos": "phrase", "ipa": "/ˈkwaɪət daʊn/", "vi": "trở nên trật tự; yên ắng lại"},
    # 44: red bay
    {"pos": "phrase", "ipa": "/rɛd beɪ/", "vi": "cây bời lời đỏ Persea borbonia"},
    # 45: red guard
    {"pos": "phrase", "ipa": "/rɛd ɡɑːrd/", "vi": "Hồng vệ binh Cách mạng văn hóa"},
    # 46: republican party
    {"pos": "phrase", "ipa": "/rɪˈpʌblɪkən ˈpɑːrti/", "vi": "Đảng Cộng hòa Hoa Kỳ"},
    # 47: rose bed
    {"pos": "phrase", "ipa": "/roʊz bɛd/", "vi": "luống hoa hồng; bồn hoa hồng"},
    # 48: russian agency
    {"pos": "phrase", "ipa": "/ˈrʌʃn ˈeɪdʒənsi/", "vi": "cơ quan thông tấn Nga; cơ quan Nga"},
    # 49: sales division
    {"pos": "phrase", "ipa": "/seɪlz dɪˈvɪʒn/", "vi": "bộ phận kinh doanh; phòng bán hàng"},
    # 50: score paper
    {"pos": "phrase", "ipa": "/skɔːr ˈpeɪpər/", "vi": "giấy kẻ khuông nhạc soạn tổng phổ"},
    # 51: sexual union
    {"pos": "phrase", "ipa": "/ˈsɛkʃuəl ˈjuːnjən/", "vi": "sự giao hợp tính dục; phối ngẫu"},
    # 52: side chair
    {"pos": "phrase", "ipa": "/saɪd tʃɛr/", "vi": "ghế tựa không có tay vịn"},
    # 53: sir thomas more
    {"pos": "phrase", "ipa": "/sɜːr ˈtɑːməs mɔːr/", "vi": "học giả Thomas More"},
    # 54: soft money
    {"pos": "phrase", "ipa": "/sɔːft ˈmʌni/", "vi": "tiền quyên góp ngoài luật tranh cử"},
    # 55: soul brother
    {"pos": "phrase", "ipa": "/soʊl ˈbrʌðər/", "vi": "người anh em da đen; tri kỷ"},
    # 56: source materials
    {"pos": "phrase", "ipa": "/sɔːrs məˈtɪriəlz/", "vi": "tư liệu gốc; tài liệu nguồn"},
    # 57: space vehicle
    {"pos": "phrase", "ipa": "/speɪs ˈviːəkl/", "vi": "tàu du hành vũ trụ; tàu không gian"},
    # 58: special session
    {"pos": "phrase", "ipa": "/ˈspɛʃl ˈsɛʃn/", "vi": "kỳ họp bất thường; phiên họp riêng"},
    # 59: split down
    {"pos": "phrase", "ipa": "/splɪt daʊn/", "vi": "gộp cổ phiếu giảm số lượng"},
    # 60: sports fan
    {"pos": "phrase", "ipa": "/spɔːrts fæn/", "vi": "người hâm mộ thể thao; fan thể thao"},
    # 61: stand firm
    {"pos": "phrase", "ipa": "/stænd fɜːrm/", "vi": "đứng vững; giữ vững lập trường"},
    # 62: standing committee
    {"pos": "phrase", "ipa": "/ˈstændɪŋ kəˈmɪti/", "vi": "ủy ban thường trực; ban thường vụ"},
    # 63: stock image
    {"pos": "phrase", "ipa": "/stɑːk ˈɪmɪdʒ/", "vi": "hình ảnh tư liệu có sẵn; ảnh stock"},
    # 64: strike down
    {"pos": "phrase", "ipa": "/straɪk daʊn/", "vi": "bác bỏ đạo luật; đốn ngã hạ gục"},
    # 65: strike home
    {"pos": "phrase", "ipa": "/straɪk hoʊm/", "vi": "đánh trúng tâm lý; thấm thía"},
    # 66: sun plant
    {"pos": "phrase", "ipa": "/sʌn plænt/", "vi": "hoa mười giờ; cây ưa nắng"},
    # 67: take to task
    {"pos": "phrase", "ipa": "/teɪk tuː tæsk/", "vi": "khiển trách quở phạt; truy cứu lỗi"},
    # 68: teachers college
    {"pos": "phrase", "ipa": "/ˈtiːtʃərz ˈkɑːlɪdʒ/", "vi": "trường cao đẳng sư phạm"},
    # 69: test copy
    {"pos": "phrase", "ipa": "/tɛst ˈkɑːpi/", "vi": "bản in thử kiểm tra chất lượng"},
    # 70: trade edition
    {"pos": "phrase", "ipa": "/treɪd ɪˈdɪʃn/", "vi": "ấn bản sách thương mại phổ thông"},
    # 71: travel agency
    {"pos": "phrase", "ipa": "/ˈtrævl ˈeɪdʒənsi/", "vi": "đại lý du lịch; công ty lữ hành"},
    # 72: union jack
    {"pos": "phrase", "ipa": "/ˈjuːnjən dʒæk/", "vi": "quốc kỳ Liên hiệp Anh Union Jack"},
    # 73: upper class
    {"pos": "phrase", "ipa": "/ˈʌpər klæs/", "vi": "tầng lớp thượng lưu; quý tộc"},
    # 74: valley girl
    {"pos": "phrase", "ipa": "/ˈvæli ɡɜːrl/", "vi": "cô gái điệu đà sành điệu ngoại ô Mỹ"},
    # 75: watch guard
    {"pos": "phrase", "ipa": "/wɑːtʃ ɡɑːrd/", "vi": "dây móc xích đồng hồ quả quýt"},
    # 76: water jump
    {"pos": "phrase", "ipa": "/ˈwɔːtər dʒʌmp/", "vi": "rào chắn hào nước vượt chướng ngại"},
    # 77: weak part
    {"pos": "phrase", "ipa": "/wiːk pɑːrt/", "vi": "điểm yếu kém; phần khuyết điểm"},
    # 78: weather station
    {"pos": "phrase", "ipa": "/ˈwɛðər ˈsteɪʃn/", "vi": "trạm khí tượng; trạm quan trắc"},
    # 79: zero in
    {"pos": "phrase", "ipa": "/ˈzɪroʊ ɪn/", "vi": "nhắm chuẩn mục tiêu; tập trung vào"},
    # 80: babied
    {"pos": "verb", "ipa": "/ˈbeɪbid/", "vi": "đã cưng chiều; đã nâng niu như bé"},
    # 81: babying
    {"pos": "verb", "ipa": "/ˈbeɪbiɪŋ/", "vi": "nuông chiều quá mức; cưng nựng"},
    # 82: fathered
    {"pos": "verb", "ipa": "/ˈfɑːðərd/", "vi": "đã sinh ra con; đã làm cha"},
    # 83: fathering
    {"pos": "noun", "ipa": "/ˈfɑːðərɪŋ/", "vi": "thiên chức làm cha; sự dưỡng dục"},
    # 84: songs
    {"pos": "noun", "ipa": "/sɔːŋz/", "vi": "các bài hát; những khúc ca"},
    # 85: air crew
    {"pos": "phrase", "ipa": "/ɛr kruː/", "vi": "phi hành đoàn; tổ lái máy bay"},
    # 86: as usual
    {"pos": "phrase", "ipa": "/æz ˈjuːʒuəl/", "vi": "như thường lệ; như mọi khi"},
    # 87: asian country
    {"pos": "phrase", "ipa": "/ˈeɪʒn ˈkʌntri/", "vi": "quốc gia châu Á; đất nước châu Á"},
    # 88: attorney general
    {"pos": "phrase", "ipa": "/əˈtɜːrni ˈdʒɛnrəl/", "vi": "Bộ trưởng Tư pháp; Viện trưởng KS"},
    # 89: authority figure
    {"pos": "phrase", "ipa": "/əˈθɔːrəti ˈfɪɡjər/", "vi": "nhân vật có thẩm quyền lãnh đạo"},
    # 90: base metal
    {"pos": "phrase", "ipa": "/beɪs ˈmɛtl/", "vi": "kim loại cơ bản thường không quý"},
    # 91: battle damage
    {"pos": "phrase", "ipa": "/ˈbætl ˈdæmɪdʒ/", "vi": "thiệt hại do giao tranh chiến trận"},
    # 92: birth rate
    {"pos": "phrase", "ipa": "/bɜːrθ reɪt/", "vi": "tỷ lệ sinh đẻ; tỷ suất sinh"},
    # 93: birthday present
    {"pos": "phrase", "ipa": "/ˈbɜːrθdeɪ ˈprɛznt/", "vi": "quà tặng sinh nhật; quà sinh nhật"},
    # 94: blue cat
    {"pos": "phrase", "ipa": "/bluː kæt/", "vi": "cá trê xanh lam Bắc Mỹ"},
    # 95: bob about
    {"pos": "phrase", "ipa": "/bɑːb əˈbaʊt/", "vi": "nhấp nhô bồng bềnh trên mặt nước"},
    # 96: bob up
    {"pos": "phrase", "ipa": "/bɑːb ʌp/", "vi": "bất ngờ nổi lên; đột ngột xuất hiện"},
    # 97: body suit
    {"pos": "phrase", "ipa": "/ˈbɑːdi suːt/", "vi": "bộ đồ áo liền quần bó sát cơ thể"},
    # 98: brain damage
    {"pos": "phrase", "ipa": "/breɪn ˈdæmɪdʒ/", "vi": "tổn thương não bộ; tổn thương não"},
    # 99: brain disease
    {"pos": "phrase", "ipa": "/breɪn dɪˈziːz/", "vi": "bệnh lý não bộ; bệnh về não"}
]

for r in reviews:
    r["ipa"] = r["ipa"].strip()

assert len(reviews) == 100
assert len(raw_items) == 100

out_items = []
for i in range(100):
    item = dict(raw_items[i])
    rev = reviews[i]
    item["pos"] = rev["pos"]
    item["ipa"] = rev["ipa"]
    item["vi"] = rev["vi"]
    item["status"] = "reviewed"
    
    assert len(item["vi"]) <= 35, f"vi too long at {i}: {item['vi']}"
    assert len(item["vi"]) > 0
    assert item["ipa"].startswith("/") and item["ipa"].endswith("/") and item["ipa"].count("/") == 2
    out_items.append(item)

json.dump(out_items, open("scratch/b22_r02_p3.json", "w"), ensure_ascii=False, indent=2)
print("Round 2 Part 3 reviewed successfully: 100 items saved to scratch/b22_r02_p3.json")
