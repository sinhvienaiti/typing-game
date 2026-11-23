import json

# Manual word-by-word cognitive review for Batch 21 Round 8 Part 2 (records 3600-3699, IDs 200k.003602 to 200k.003701)
reviewed_entries = [
    # 3600: content word
    {"ipa": "/ˈkɑːntɛnt wɜːrd/", "vi": "từ thực; từ mang nghĩa từ vựng", "pos": "phrase"},
    # 3601: cost of capital
    {"ipa": "/kɔːst ʌv ˈkæpɪtl/", "vi": "chi phí sử dụng vốn; chi phí vốn", "pos": "phrase"},
    # 3602: council tax
    {"ipa": "/ˈkaʊnsl tæks/", "vi": "thuế hội đồng địa phương ở Anh", "pos": "phrase"},
    # 3603: department store
    {"ipa": "/dɪˈpɑːrtmənt stɔːr/", "vi": "cửa hàng bách hóa; hiệu bách hóa", "pos": "phrase"},
    # 3604: doctor of music
    {"ipa": "/ˈdɑːktər ʌv ˈmjuːzɪk/", "vi": "tiến sĩ âm nhạc học; bằng tiến sĩ", "pos": "phrase"},
    # 3605: draw in
    {"ipa": "/drɔː ɪn/", "vi": "thu hút; kéo vào; trời sập tối", "pos": "phrase"},
    # 3606: drop behind
    {"ipa": "/drɑːp bɪˈhaɪnd/", "vi": "tụt lại phía sau; chậm chân hơn", "pos": "phrase"},
    # 3607: east sea
    {"ipa": "/iːst siː/", "vi": "Biển Đông; vùng biển phía đông", "pos": "phrase"},
    # 3608: economic science
    {"ipa": "/ˌekəˈnɑːmɪk ˈsaɪəns/", "vi": "khoa học kinh tế; kinh tế học", "pos": "phrase"},
    # 3609: father of radio
    {"ipa": "/ˈfɑːðər ʌv ˈreɪdioʊ/", "vi": "cha đẻ của vô tuyến truyền thanh", "pos": "phrase"},
    # 3610: finish line
    {"ipa": "/ˈfɪnɪʃ laɪn/", "vi": "vạch đích; vạch về đích", "pos": "phrase"},
    # 3611: foreign bill
    {"ipa": "/ˈfɔːrən bɪl/", "vi": "hối phiếu quốc tế; hối phiếu ngoài", "pos": "phrase"},
    # 3612: french blue
    {"ipa": "/frɛntʃ bluː/", "vi": "màu xanh lam Pháp; sắc xanh Pháp", "pos": "phrase"},
    # 3613: full professor
    {"ipa": "/fʊl prəˈfɛsər/", "vi": "giáo sư thực thụ; giáo sư chính", "pos": "phrase"},
    # 3614: gas main
    {"ipa": "/ɡæs meɪn/", "vi": "đường ống dẫn khí đốt chính", "pos": "phrase"},
    # 3615: grand national
    {"ipa": "/ɡrænd ˈnæʃənl/", "vi": "giải đua ngựa vượt rào danh tiếng", "pos": "phrase"},
    # 3616: ground cover
    {"ipa": "/ɡraʊnd ˈkʌvər/", "vi": "thảm thực vật phủ đất; cây bò phủ", "pos": "phrase"},
    # 3617: group captain
    {"ipa": "/ɡruːp ˈkæptɪn/", "vi": "đại tá không quân hoàng gia Anh", "pos": "phrase"},
    # 3618: hard drink
    {"ipa": "/hɑːrd drɪŋk/", "vi": "đồ uống có cồn nặng; rượu mạnh", "pos": "phrase"},
    # 3619: holding company
    {"ipa": "/ˈhoʊldɪŋ ˈkʌmpəni/", "vi": "công ty mẹ; công ty nắm giữ cổ phần", "pos": "phrase"},
    # 3620: holy city
    {"ipa": "/ˈhoʊli ˈsɪti/", "vi": "thánh địa; thành phố linh thiêng", "pos": "phrase"},
    # 3621: jack up
    {"ipa": "/dʒæk ʌp/", "vi": "kích nâng lên; tăng vọt giá cả", "pos": "phrase"},
    # 3622: know the score
    {"ipa": "/noʊ ðə skɔːr/", "vi": "hiểu rõ sự tình; nắm rõ ngọn ngành", "pos": "phrase"},
    # 3623: lady friend
    {"ipa": "/ˈleɪdi frɛnd/", "vi": "bạn gái thân thiết; người yêu nữ", "pos": "phrase"},
    # 3624: least effort
    {"ipa": "/liːst ˈɛfərt/", "vi": "ít nỗ lực nhất; công sức tối thiểu", "pos": "phrase"},
    # 3625: long division
    {"ipa": "/lɔːŋ dɪˈvɪʒən/", "vi": "phép chia đặt tính; phép chia dài", "pos": "phrase"},
    # 3626: love tree
    {"ipa": "/lʌv triː/", "vi": "cây tình nhân; cây gỗ sưa đỏ", "pos": "phrase"},
    # 3627: market forces
    {"ipa": "/ˈmɑːrkɪt ˈfɔːrsɪz/", "vi": "các lực lượng thị trường cung cầu", "pos": "phrase"},
    # 3628: medical practice
    {"ipa": "/ˈmɛdɪkl ˈpræktɪs/", "vi": "hoạt động hành nghề y; phòng khám", "pos": "phrase"},
    # 3629: military officer
    {"ipa": "/ˈmɪlətɛri ˈɔːfɪsər/", "vi": "sĩ quan quân đội; cán bộ quân đội", "pos": "phrase"},
    # 3630: natural science
    {"ipa": "/ˈnætʃrəl ˈsaɪəns/", "vi": "khoa học tự nhiên", "pos": "phrase"},
    # 3631: news organization
    {"ipa": "/nuːz ˌɔːrɡənəˈzeɪʃən/", "vi": "tổ chức tin tức; cơ quan báo chí", "pos": "phrase"},
    # 3632: number agreement
    {"ipa": "/ˈnʌmbər əˈɡriːmənt/", "vi": "sự hòa hợp về số trong ngữ pháp", "pos": "phrase"},
    # 3633: open marriage
    {"ipa": "/ˈoʊpən ˈmærɪdʒ/", "vi": "hôn nhân mở; hôn nhân cởi mở", "pos": "phrase"},
    # 3634: open secret
    {"ipa": "/ˈoʊpən ˈsiːkrət/", "vi": "bí mật mở; điều ai cũng biết rõ", "pos": "phrase"},
    # 3635: out of fashion
    {"ipa": "/aʊt ʌv ˈfæʃən/", "vi": "lỗi thời; lỗi mốt; không hợp thời", "pos": "phrase"},
    # 3636: partner off
    {"ipa": "/ˈpɑːrtnər ɔːf/", "vi": "bắt cặp với nhau; kết đôi lứa", "pos": "phrase"},
    # 3637: physical body
    {"ipa": "/ˈfɪzɪkl ˈbɑːdi/", "vi": "thân xác vật lý; cơ thể con người", "pos": "phrase"},
    # 3638: potential energy
    {"ipa": "/pəˈtɛnʃl ˈɛnərdʒi/", "vi": "thế năng; năng lượng tiềm tàng", "pos": "phrase"},
    # 3639: power trip
    {"ipa": "/ˈpaʊər trɪp/", "vi": "thói lạm quyền; thói hám quyền lực", "pos": "phrase"},
    # 3640: pull at
    {"ipa": "/pʊl æt/", "vi": "kéo nhẹ; giật nhẹ; níu kéo", "pos": "phrase"},
    # 3641: pull out
    {"ipa": "/pʊl aʊt/", "vi": "rút lui; lăn bánh ra; nhổ ra", "pos": "phrase"},
    # 3642: pull up
    {"ipa": "/pʊl ʌp/", "vi": "dừng xe tấp vào lề; kéo lên; trách", "pos": "phrase"},
    # 3643: push out
    {"ipa": "/pʊʃ aʊt/", "vi": "đẩy ra ngoài; sa thải; tống khứ", "pos": "phrase"},
    # 3644: push up
    {"ipa": "/pʊʃ ʌp/", "vi": "đẩy lên cao; bài tập chống đẩy", "pos": "phrase"},
    # 3645: race meeting
    {"ipa": "/reɪs ˈmiːtɪŋ/", "vi": "cuộc đua ngựa; hội đua ngựa", "pos": "phrase"},
    # 3646: red sun
    {"ipa": "/rɛd sʌn/", "vi": "mặt trời đỏ rực rỡ; mặt trời lặn", "pos": "phrase"},
    # 3647: safe and sound
    {"ipa": "/seɪf ænd saʊnd/", "vi": "bình an vô sự; nguyên vẹn an toàn", "pos": "phrase"},
    # 3648: sales department
    {"ipa": "/seɪlz dɪˈpɑːrtmənt/", "vi": "bộ phận kinh doanh; phòng bán hàng", "pos": "phrase"},
    # 3649: sales force
    {"ipa": "/seɪlz fɔːrs/", "vi": "đội ngũ bán hàng; nhóm kinh doanh", "pos": "phrase"},
    # 3650: sea king
    {"ipa": "/siː kɪŋ/", "vi": "thủ lĩnh hải tặc Viking; vua biển", "pos": "phrase"},
    # 3651: short subject
    {"ipa": "/ʃɔːrt ˈsʌbdʒɪkt/", "vi": "phim ngắn chiếu kèm; tác phẩm ngắn", "pos": "phrase"},
    # 3652: show trial
    {"ipa": "/ʃoʊ ˈtraɪəl/", "vi": "phiên tòa dàn dựng; xử án hình thức", "pos": "phrase"},
    # 3653: slow down
    {"ipa": "/sloʊ daʊn/", "vi": "chậm lại; giảm tốc độ; bớt vội vã", "pos": "phrase"},
    # 3654: sort program
    {"ipa": "/sɔːrt ˈproʊɡræm/", "vi": "chương trình sắp xếp dữ liệu", "pos": "phrase"},
    # 3655: source code
    {"ipa": "/sɔːrs koʊd/", "vi": "mã nguồn phần mềm máy tính", "pos": "phrase"},
    # 3656: space station
    {"ipa": "/speɪs ˈsteɪʃən/", "vi": "trạm không gian; trạm vũ trụ", "pos": "phrase"},
    # 3657: square off
    {"ipa": "/skwɛr ɔːf/", "vi": "thủ thế giao đấu; chuẩn bị đọ sức", "pos": "phrase"},
    # 3658: thus far
    {"ipa": "/ðʌs fɑːr/", "vi": "cho đến nay; cho đến lúc này", "pos": "phrase"},
    # 3659: time scale
    {"ipa": "/taɪm skeɪl/", "vi": "thang thời gian; quy mô thời gian", "pos": "phrase"},
    # 3660: title page
    {"ipa": "/ˈtaɪtl peɪdʒ/", "vi": "trang nhan đề; trang bìa cuốn sách", "pos": "phrase"},
    # 3661: town gas
    {"ipa": "/taʊn ɡæs/", "vi": "khí than đô thị; khí đốt sinh hoạt", "pos": "phrase"},
    # 3662: track and field
    {"ipa": "/træk ænd fiːld/", "vi": "môn điền kinh; thể thao điền kinh", "pos": "phrase"},
    # 3663: training table
    {"ipa": "/ˈtreɪnɪŋ ˈteɪbl/", "vi": "chế độ dinh dưỡng vận động viên", "pos": "phrase"},
    # 3664: under the weather
    {"ipa": "/ˈʌndər ðə ˈwɛðər/", "vi": "cảm thấy không khỏe; người hơi ốm", "pos": "phrase"},
    # 3665: water skin
    {"ipa": "/ˈwɔːtər skɪn/", "vi": "túi da đựng nước; bầu nước bằng da", "pos": "phrase"},
    # 3666: wind off
    {"ipa": "/waɪnd ɔːf/", "vi": "tháo cuộn; gỡ dây; tở cuộn ra", "pos": "phrase"},
    # 3667: world trade center
    {"ipa": "/wɜːrld treɪd ˈsɛntər/", "vi": "trung tâm thương mại thế giới", "pos": "phrase"},
    # 3668: blackest
    {"ipa": "/ˈblækɪst/", "vi": "đen nhất; tăm tối nhất; u ám nhất", "pos": "adj"},
    # 3669: followings
    {"ipa": "/ˈfɑːloʊɪŋz/", "vi": "nhóm người theo dõi; nhóm hâm mộ", "pos": "noun"},
    # 3670: air defense
    {"ipa": "/ɛr dɪˈfɛns/", "vi": "phòng không; hệ thống phòng không", "pos": "phrase"},
    # 3671: art movement
    {"ipa": "/ɑːrt ˈmuːvmənt/", "vi": "phong trào nghệ thuật; trào lưu mới", "pos": "phrase"},
    # 3672: ball boy
    {"ipa": "/bɔːl bɔɪ/", "vi": "cậu bé nhặt bóng trên sân thể thao", "pos": "phrase"},
    # 3673: bank card
    {"ipa": "/bæŋk kɑːrd/", "vi": "thẻ ngân hàng; thẻ rút tiền tự động", "pos": "phrase"},
    # 3674: bank note
    {"ipa": "/bæŋk noʊt/", "vi": "tờ tiền giấy; giấy bạc ngân hàng", "pos": "phrase"},
    # 3675: bar bit
    {"ipa": "/bɑːr bɪt/", "vi": "thanh ngậm hàm thiếc của ngựa", "pos": "phrase"},
    # 3676: blood brother
    {"ipa": "/blʌd ˈbrʌðər/", "vi": "anh em ruột thịt; anh em kết nghĩa", "pos": "phrase"},
    # 3677: blood cup
    {"ipa": "/blʌd kʌp/", "vi": "nấm chén đỏ tươi; nấm cốc đỏ", "pos": "phrase"},
    # 3678: by memory
    {"ipa": "/baɪ ˈmɛməri/", "vi": "bằng trí nhớ; học thuộc lòng", "pos": "phrase"},
    # 3679: cancer body
    {"ipa": "/ˈkænsər ˈbɑːdi/", "vi": "thể vùi ung thư; tế bào ung thư", "pos": "phrase"},
    # 3680: capital account
    {"ipa": "/ˈkæpɪtl əˈkaʊnt/", "vi": "tài khoản vốn cán cân thanh toán", "pos": "phrase"},
    # 3681: case agreement
    {"ipa": "/keɪs əˈɡriːmənt/", "vi": "sự hòa hợp về cách ngữ pháp", "pos": "phrase"},
    # 3682: cash in hand
    {"ipa": "/kæʃ ɪn hænd/", "vi": "tiền mặt hiện có; tiền trong tay", "pos": "phrase"},
    # 3683: charge account
    {"ipa": "/tʃɑːrdʒ əˈkaʊnt/", "vi": "tài khoản ghi nợ mua chịu", "pos": "phrase"},
    # 3684: chinese date
    {"ipa": "/ˌtʃaɪˈniːz deɪt/", "vi": "quả táo tàu; quả hồng táo khô", "pos": "phrase"},
    # 3685: city hall
    {"ipa": "/ˈsɪti hɔːl/", "vi": "tòa thị chính; ủy ban thị xã", "pos": "phrase"},
    # 3686: civil death
    {"ipa": "/ˈsɪvl dɛθ/", "vi": "tước bỏ toàn bộ quyền công dân", "pos": "phrase"},
    # 3687: civil wrong
    {"ipa": "/ˈsɪvl rɔːŋ/", "vi": "hành vi xâm hại dân sự; sai trái", "pos": "phrase"},
    # 3688: color of law
    {"ipa": "/ˈkʌlər ʌv lɔː/", "vi": "danh nghĩa công quyền; vẻ hợp pháp", "pos": "phrase"},
    # 3689: common cold
    {"ipa": "/ˈkɑːmən koʊld/", "vi": "bệnh cảm lạnh thông thường", "pos": "phrase"},
    # 3690: contact action
    {"ipa": "/ˈkɑːntækt ˈækʃən/", "vi": "tác dụng tiếp xúc; hành động chạm", "pos": "phrase"},
    # 3691: control operation
    {"ipa": "/kənˈtroʊl ˌɑːpəˈreɪʃən/", "vi": "thao tác điều khiển; lệnh điều hành", "pos": "phrase"},
    # 3692: control stock
    {"ipa": "/kənˈtroʊl stɑːk/", "vi": "cổ phiếu quyền chi phối công ty", "pos": "phrase"},
    # 3693: count off
    {"ipa": "/kaʊnt ɔːf/", "vi": "điểm danh theo số; đếm lần lượt", "pos": "phrase"},
    # 3694: country doctor
    {"ipa": "/ˈkʌntri ˈdɑːktər/", "vi": "bác sĩ nông thôn; thầy thuốc làng", "pos": "phrase"},
    # 3695: daily round
    {"ipa": "/ˈdeɪli raʊnd/", "vi": "công việc thường nhật; lệ hàng ngày", "pos": "phrase"},
    # 3696: dance of death
    {"ipa": "/dæns ʌv dɛθ/", "vi": "vũ điệu thần chết; khúc ca tử thần", "pos": "phrase"},
    # 3697: dead weight
    {"ipa": "/dɛd weɪt/", "vi": "gánh nặng vô ích; vật cản trở", "pos": "phrase"},
    # 3698: double date
    {"ipa": "/ˈdʌbl deɪt/", "vi": "buổi hẹn hò đôi của hai cặp bạn", "pos": "phrase"},
    # 3699: draw out
    {"ipa": "/drɔː aʊt/", "vi": "rút tiền ra; kéo dài thời gian", "pos": "phrase"}
]

with open("scratch/b21_r08_raw_p2.json", "r", encoding="utf-8") as f:
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

with open("scratch/b21_r08_p2.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(output)} entries for Part 2.")
