import json

# Manual word-by-word cognitive review for Batch 21 Round 7 Part 4 (records 3300-3399, IDs 200k.003302 to 200k.003401)
reviewed_entries = [
    # 3300: lie in
    {"ipa": "/laɪ ɪn/", "vi": "nằm ở cốt lõi; ngủ nướng sáng", "pos": "phrase"},
    # 3301: lie with
    {"ipa": "/laɪ wɪð/", "vi": "thuộc về trách nhiệm của; ăn nằm", "pos": "phrase"},
    # 3302: light brown
    {"ipa": "/laɪt braʊn/", "vi": "màu nâu nhạt; tông màu hạt dẻ nhạt", "pos": "phrase"},
    # 3303: line judge
    {"ipa": "/laɪn dʒʌdʒ/", "vi": "trọng tài biên trong quần vợt", "pos": "phrase"},
    # 3304: living rock
    {"ipa": "/ˈlɪvɪŋ rɑːk/", "vi": "đá gốc tự nhiên; cây xương rồng đá", "pos": "phrase"},
    # 3305: master in business
    {"ipa": "/ˈmæstər ɪn ˈbɪznəs/", "vi": "thạc sĩ ngành quản trị kinh doanh", "pos": "phrase"},
    # 3306: medical science
    {"ipa": "/ˈmɛdɪkəl ˈsaɪəns/", "vi": "ngành khoa học y học điều trị bệnh", "pos": "phrase"},
    # 3307: minute hand
    {"ipa": "/ˈmɪnɪt hænd/", "vi": "chiếc kim phút của mặt đồng hồ tròn", "pos": "phrase"},
    # 3308: national insurance
    {"ipa": "/ˈnæʃənəl ɪnˈʃʊrəns/", "vi": "hệ thống bảo hiểm quốc gia của Anh", "pos": "phrase"},
    # 3309: national leader
    {"ipa": "/ˈnæʃənəl ˈliːdər/", "vi": "vị lãnh tụ của quốc gia dân tộc", "pos": "phrase"},
    # 3310: natural event
    {"ipa": "/ˈnætʃərəl ɪˈvɛnt/", "vi": "hiện tượng biến cố của tự nhiên", "pos": "phrase"},
    # 3311: north island
    {"ipa": "/nɔːrθ ˈaɪlənd/", "vi": "Đảo Bắc của đất nước New Zealand", "pos": "phrase"},
    # 3312: oil industry
    {"ipa": "/ɔɪl ˈɪndəstri/", "vi": "ngành công nghiệp khai thác dầu khí", "pos": "phrase"},
    # 3313: old north french
    {"ipa": "/oʊld nɔːrθ frɛntʃ/", "vi": "tiếng Pháp miền Bắc thời Trung cổ", "pos": "phrase"},
    # 3314: open letter
    {"ipa": "/ˈoʊpən ˈlɛtər/", "vi": "bức thư ngỏ gửi đến công chúng rộng", "pos": "phrase"},
    # 3315: parts department
    {"ipa": "/pɑːrts dɪˈpɑːrtmənt/", "vi": "bộ phận phụ tùng linh kiện máy móc", "pos": "phrase"},
    # 3316: pass across
    {"ipa": "/pæs əˈkrɔːs/", "vi": "đi băng ngang qua; chuyền tay qua", "pos": "phrase"},
    # 3317: peter the great
    {"ipa": "/ˈpiːtər ðə ɡreɪt/", "vi": "Đại đế Pyotr Đệ Nhất của nước Nga", "pos": "phrase"},
    # 3318: physical change
    {"ipa": "/ˈfɪzɪkəl tʃeɪndʒ/", "vi": "hiện tượng biến đổi vật lý chất", "pos": "phrase"},
    # 3319: plant part
    {"ipa": "/plænt pɑːrt/", "vi": "bộ phận của cây cối thực vật", "pos": "phrase"},
    # 3320: police station
    {"ipa": "/pəˈliːs ˈsteɪʃən/", "vi": "đồn công an cảnh sát khu vực quận", "pos": "phrase"},
    # 3321: previous question
    {"ipa": "/ˈpriːviəs ˈkwɛstʃən/", "vi": "kiến nghị biểu quyết ngay phiên họp", "pos": "phrase"},
    # 3322: product line
    {"ipa": "/ˈprɑːdʌkt laɪn/", "vi": "dòng sản phẩm hàng hóa chuyên biệt", "pos": "phrase"},
    # 3323: record cover
    {"ipa": "/ˈrɛkərd ˈkʌvər/", "vi": "vỏ bọc bìa đĩa hát than âm nhạc", "pos": "phrase"},
    # 3324: ride out
    {"ipa": "/raɪd aʊt/", "vi": "vượt qua giông bão; bình yên vượt", "pos": "phrase"},
    # 3325: role model
    {"ipa": "/roʊl ˈmɑːdəl/", "vi": "tấm gương sáng; hình mẫu noi theo", "pos": "phrase"},
    # 3326: safe sex
    {"ipa": "/seɪf sɛks/", "vi": "tình dục an toàn có biện pháp ngừa", "pos": "phrase"},
    # 3327: screen out
    {"ipa": "/skriːn aʊt/", "vi": "sàng lọc kỹ lưỡng; loại bỏ phần xấu", "pos": "phrase"},
    # 3328: secretary general
    {"ipa": "/ˌsɛkrətɛri ˈdʒɛnərəl/", "vi": "Tổng thư ký của tổ chức quốc tế", "pos": "phrase"},
    # 3329: security council
    {"ipa": "/sɪˈkjʊrəti ˈkaʊnsəl/", "vi": "Hội đồng Bảo an Liên Hợp Quốc", "pos": "phrase"},
    # 3330: security staff
    {"ipa": "/sɪˈkjʊrəti stæf/", "vi": "đội ngũ nhân viên an ninh bảo vệ", "pos": "phrase"},
    # 3331: serve up
    {"ipa": "/sɜːrv ʌp/", "vi": "dọn thức ăn lên bàn; phục vụ món ăn", "pos": "phrase"},
    # 3332: side judge
    {"ipa": "/saɪd dʒʌdʒ/", "vi": "trọng tài biên môn bóng bầu dục", "pos": "phrase"},
    # 3333: slow up
    {"ipa": "/sloʊ ʌp/", "vi": "giảm tốc độ lại; làm chậm bước tiến", "pos": "phrase"},
    # 3334: small letter
    {"ipa": "/smɔːl ˈlɛtər/", "vi": "chữ cái viết thường trong văn bản", "pos": "phrase"},
    # 3335: social movement
    {"ipa": "/ˈsoʊʃəl ˈmuːvmənt/", "vi": "phong trào đấu tranh xã hội quy mô", "pos": "phrase"},
    # 3336: standard of living
    {"ipa": "/ˈstændərd ʌv ˈlɪvɪŋ/", "vi": "tiêu chuẩn mức sống của nhân dân", "pos": "phrase"},
    # 3337: stupid person
    {"ipa": "/ˈstuːpɪd ˈpɜːrsən/", "vi": "người ngu xuẩn; kẻ ngốc nghếch đần", "pos": "phrase"},
    # 3338: subject area
    {"ipa": "/ˈsʌbdʒɪkt ˈɛriə/", "vi": "phạm vi chuyên môn; lĩnh vực bộ môn", "pos": "phrase"},
    # 3339: tax bill
    {"ipa": "/tæks bɪl/", "vi": "hóa đơn thông báo thuế vụ nộp", "pos": "phrase"},
    # 3340: tax rate
    {"ipa": "/tæks reɪt/", "vi": "mức thuế suất quy định hiện hành", "pos": "phrase"},
    # 3341: term paper
    {"ipa": "/tɜːrm ˈpeɪpər/", "vi": "bài luận nghiên cứu cuối học kỳ", "pos": "phrase"},
    # 3342: third eye
    {"ipa": "/θɜːrd aɪ/", "vi": "con mắt thứ ba; trực giác tâm linh", "pos": "phrase"},
    # 3343: trade policy
    {"ipa": "/treɪd ˈpɑːləsi/", "vi": "chính sách ngoại thương thương mại", "pos": "phrase"},
    # 3344: via media
    {"ipa": "/ˌvaɪə ˈmiːdiə/", "vi": "con đường trung đạo dung hòa", "pos": "phrase"},
    # 3345: wall street
    {"ipa": "/wɔːl striːt/", "vi": "phố tài chính Wall Street của Mỹ", "pos": "phrase"},
    # 3346: wear away
    {"ipa": "/wɛr əˈweɪ/", "vi": "bào mòn nhẵn thín; xói mòn dần theo", "pos": "phrase"},
    # 3347: world war ii
    {"ipa": "/wɜːrld wɔːr tuː/", "vi": "Đại chiến Thế giới lần thứ hai", "pos": "phrase"},
    # 3348: americans
    {"ipa": "/əˈmɛrəkənz/", "vi": "những người Mỹ; người dân Hoa Kỳ", "pos": "noun"},
    # 3349: orders
    {"ipa": "/ˈɔːrdərz/", "vi": "các mệnh lệnh; những đơn đặt hàng", "pos": "noun"},
    # 3350: partied
    {"ipa": "/ˈpɑːrtid/", "vi": "đã dự tiệc tùng; đã vui chơi tiệc", "pos": "verb"},
    # 3351: parties
    {"ipa": "/ˈpɑːrtiz/", "vi": "các bữa tiệc tùng; các đảng phái", "pos": "noun"},
    # 3352: partying
    {"ipa": "/ˈpɑːrtiɪŋ/", "vi": "đang vui chơi tiệc tùng thâu đêm", "pos": "verb"},
    # 3353: ran
    {"ipa": "/ræn/", "vi": "đã chạy đua; đã vận hành quản lý", "pos": "verb"},
    # 3354: runs
    {"ipa": "/rʌnz/", "vi": "các điểm chạy gôn; những chuyến đi", "pos": "noun"},
    # 3355: access road
    {"ipa": "/ˈæksɛs roʊd/", "vi": "đường nhánh nối vào đường cao tốc", "pos": "phrase"},
    # 3356: action officer
    {"ipa": "/ˈækʃən ˈɔːfɪsər/", "vi": "sĩ quan trực tiếp xử lý hồ sơ vụ", "pos": "phrase"},
    # 3357: area unit
    {"ipa": "/ˈɛriə ˈjuːnɪt/", "vi": "đơn vị đo lường diện tích đất đai", "pos": "phrase"},
    # 3358: art student
    {"ipa": "/ɑːrt ˈstuːdənt/", "vi": "sinh viên theo học trường mỹ thuật", "pos": "phrase"},
    # 3359: at bottom
    {"ipa": "/æt ˈbɑːtəm/", "vi": "về bản chất cơ bản; suy cho cùng", "pos": "phrase"},
    # 3360: ball field
    {"ipa": "/bɔːl fiːld/", "vi": "sân chơi bóng chày; bãi cỏ đá bóng", "pos": "phrase"},
    # 3361: bar line
    {"ipa": "/bɑːr laɪn/", "vi": "vạch kẻ phân chia ô nhịp âm nhạc", "pos": "phrase"},
    # 3362: battle line
    {"ipa": "/ˈbætəl laɪn/", "vi": "chiến tuyến phòng thủ mặt trận đánh", "pos": "phrase"},
    # 3363: big fish
    {"ipa": "/bɪɡ fɪʃ/", "vi": "nhân vật quyền uy cộm cán; cá lớn", "pos": "phrase"},
    # 3364: bill of review
    {"ipa": "/bɪl ʌv rɪˈvjuː/", "vi": "đơn thỉnh cầu tái thẩm xét lại án", "pos": "phrase"},
    # 3365: black letter
    {"ipa": "/blæk ˈlɛtər/", "vi": "kiểu chữ gothic cổ; luật thành văn", "pos": "phrase"},
    # 3366: blood bank
    {"ipa": "/blʌd bæŋk/", "vi": "ngân hàng máu dự trữ cấp cứu viện", "pos": "phrase"},
    # 3367: blue green
    {"ipa": "/bluː ɡriːn/", "vi": "màu xanh lơ lục lam pha ngọc bích", "pos": "phrase"},
    # 3368: book of knowledge
    {"ipa": "/bʊk ʌv ˈnɑːlɪdʒ/", "vi": "cuốn từ điển bách khoa tri thức", "pos": "phrase"},
    # 3369: bottom out
    {"ipa": "/ˈbɑːtəm aʊt/", "vi": "chạm đáy suy thoái rồi phục hồi", "pos": "phrase"},
    # 3370: broken home
    {"ipa": "/ˈbroʊkən hoʊm/", "vi": "gia đình đổ vỡ cha mẹ ly hôn", "pos": "phrase"},
    # 3371: business organization
    {"ipa": "/ˈbɪznəs ˌɔːrɡənəˈzeɪʃən/", "vi": "doanh nghiệp thương mại làm ăn", "pos": "phrase"},
    # 3372: change of direction
    {"ipa": "/tʃeɪndʒ ʌv dəˈrɛkʃən/", "vi": "sự chuyển hướng đi; đổi phương châm", "pos": "phrase"},
    # 3373: church property
    {"ipa": "/tʃɜːrtʃ ˈprɑːpərti/", "vi": "bất động sản tài sản của giáo hội", "pos": "phrase"},
    # 3374: clean room
    {"ipa": "/kliːn ruːm/", "vi": "phòng sạch vô trùng thí nghiệm chip", "pos": "phrase"},
    # 3375: cold front
    {"ipa": "/koʊld frʌnt/", "vi": "khối không khí lạnh tràn về gió rét", "pos": "phrase"},
    # 3376: college student
    {"ipa": "/ˈkɑːlɪdʒ ˈstuːdənt/", "vi": "sinh viên đang học đại học cao đẳng", "pos": "phrase"},
    # 3377: contract law
    {"ipa": "/ˈkɑːntrækt lɔː/", "vi": "luật hợp đồng dân sự kinh doanh", "pos": "phrase"},
    # 3378: council member
    {"ipa": "/ˈkaʊnsəl ˈmɛmbər/", "vi": "thành viên hội đồng nghị sự dân sự", "pos": "phrase"},
    # 3379: count on
    {"ipa": "/kaʊnt ɑːn/", "vi": "trông cậy tin tưởng vào sự giúp đỡ", "pos": "phrase"},
    # 3380: county council
    {"ipa": "/ˈkaʊnti ˈkaʊnsəl/", "vi": "hội đồng chính quyền hạt địa phương", "pos": "phrase"},
    # 3381: court of justice
    {"ipa": "/kɔːrt ʌv ˈdʒʌstɪs/", "vi": "tòa án công lý xét xử tư pháp", "pos": "phrase"},
    # 3382: dance music
    {"ipa": "/dæns ˈmjuːzɪk/", "vi": "nhạc khiêu vũ sàn nhảy sôi động", "pos": "phrase"},
    # 3383: data link
    {"ipa": "/ˈdeɪtə lɪŋk/", "vi": "đường truyền liên kết dữ liệu số", "pos": "phrase"},
    # 3384: deep space
    {"ipa": "/diːp speɪs/", "vi": "không gian sâu thẳm ngoài vũ trụ", "pos": "phrase"},
    # 3385: double check
    {"ipa": "/ˈdʌbəl tʃɛk/", "vi": "kiểm tra kỹ lại lần hai cẩn thận", "pos": "phrase"},
    # 3386: economic policy
    {"ipa": "/ˌɛkəˈnɑːmɪk ˈpɑːləsi/", "vi": "đường lối chính sách kinh tế nước", "pos": "phrase"},
    # 3387: family doctor
    {"ipa": "/ˈfæməli ˈdɑːktər/", "vi": "bác sĩ gia đình chăm sóc sức khỏe", "pos": "phrase"},
    # 3388: family planning
    {"ipa": "/ˈfæməli ˈplænɪŋ/", "vi": "chương trình kế hoạch hóa gia đình", "pos": "phrase"},
    # 3389: federal official
    {"ipa": "/ˈfɛdərəl əˈfɪʃəl/", "vi": "viên chức chính phủ cấp liên bang", "pos": "phrase"},
    # 3390: financial center
    {"ipa": "/faɪˈnænʃəl ˈsɛntər/", "vi": "trung tâm tài chính tiền tệ quốc tế", "pos": "phrase"},
    # 3391: fire station
    {"ipa": "/ˈfaɪər ˈsteɪʃən/", "vi": "trạm phòng cháy cứu hỏa thường trực", "pos": "phrase"},
    # 3392: fish family
    {"ipa": "/fɪʃ ˈfæməli/", "vi": "họ các loài cá trong sinh vật học", "pos": "phrase"},
    # 3393: george town
    {"ipa": "/dʒɔːrdʒ taʊn/", "vi": "thị trấn George Town danh tiếng", "pos": "phrase"},
    # 3394: glass over
    {"ipa": "/ɡlæs ˈoʊvər/", "vi": "đôi mắt lờ đờ vô hồn; đóng lớp băng", "pos": "phrase"},
    # 3395: great hall
    {"ipa": "/ɡreɪt hɔːl/", "vi": "đại sảnh nguy nga trong lâu đài cổ", "pos": "phrase"},
    # 3396: growing season
    {"ipa": "/ˈɡroʊɪŋ ˈsiːzən/", "vi": "mùa sinh trưởng đâm chồi nở hoa", "pos": "phrase"},
    # 3397: gun control
    {"ipa": "/ɡʌn kənˈtroʊl/", "vi": "luật kiểm soát quyền sử dụng súng", "pos": "phrase"},
    # 3398: high spot
    {"ipa": "/haɪ spɑːt/", "vi": "điểm nhấn nổi bật; hồi cao trào", "pos": "phrase"},
    # 3399: holy man
    {"ipa": "/ˈhoʊli mæn/", "vi": "bậc thánh nhân tu hành đạo đức", "pos": "phrase"},
]

with open('scratch/b21_r07_raw_p4.json') as f:
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

with open('scratch/b21_r07_p4.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r07_p4.json created successfully and validated!")
