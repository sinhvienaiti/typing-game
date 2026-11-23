import json

# Manual word-by-word cognitive review for Batch 21 Round 9 Part 3 (records 4200-4299, IDs 200k.004202 to 200k.004301)
reviewed_entries = [
    # 4200: state prison
    {"ipa": "/steɪt ˈprɪzn/", "vi": "nhà tù tiểu bang; trại giam bang", "pos": "phrase"},
    # 4201: stick in
    {"ipa": "/stɪk ɪn/", "vi": "cắm vào; đút vào; khắc sâu tâm trí", "pos": "phrase"},
    # 4202: stick on
    {"ipa": "/stɪk ɑːn/", "vi": "dán chặt vào; gắn dính lên trên", "pos": "phrase"},
    # 4203: stick to
    {"ipa": "/stɪk tuː/", "vi": "bám chặt vào; kiên trì tuân thủ", "pos": "phrase"},
    # 4204: stick with
    {"ipa": "/stɪk wɪð/", "vi": "gắn bó trung thành; tiếp tục theo", "pos": "phrase"},
    # 4205: street address
    {"ipa": "/striːt əˈdrɛs/", "vi": "địa chỉ nhà; số nhà tên đường phố", "pos": "phrase"},
    # 4206: sun king
    {"ipa": "/sʌn kɪŋ/", "vi": "Vua Mặt Trời Louis XIV nước Pháp", "pos": "phrase"},
    # 4207: tax credit
    {"ipa": "/tæks ˈkrɛdɪt/", "vi": "khoản tín dụng thuế; khấu trừ thuế", "pos": "phrase"},
    # 4208: term insurance
    {"ipa": "/tɜːrm ɪnˈʃʊrəns/", "vi": "bảo hiểm nhân thọ có thời hạn", "pos": "phrase"},
    # 4209: throw away
    {"ipa": "/θroʊ əˈweɪ/", "vi": "vứt bỏ đi; lãng phí cơ hội tốt", "pos": "phrase"},
    # 4210: times square
    {"ipa": "/taɪmz skwɛr/", "vi": "Quảng trường Thời đại New York", "pos": "phrase"},
    # 4211: title of respect
    {"ipa": "/ˈtaɪtl ʌv rɪˈspɛkt/", "vi": "tước hiệu kính cẩn; kính xưng", "pos": "phrase"},
    # 4212: tree line
    {"ipa": "/triː laɪn/", "vi": "đường giới hạn cây gỗ mọc", "pos": "phrase"},
    # 4213: trial court
    {"ipa": "/ˈtraɪəl kɔːrt/", "vi": "tòa án sơ thẩm xét xử vụ án", "pos": "phrase"},
    # 4214: union card
    {"ipa": "/ˈjuːnjən kɑːrd/", "vi": "thẻ đoàn viên công đoàn lao động", "pos": "phrase"},
    # 4215: wedding night
    {"ipa": "/ˈwɛdɪŋ naɪt/", "vi": "đêm tân hôn của đôi vợ chồng trẻ", "pos": "phrase"},
    # 4216: west indian
    {"ipa": "/wɛst ˈɪndiən/", "vi": "người dân vùng biển Tây Ấn Caribe", "pos": "phrase"},
    # 4217: white lie
    {"ipa": "/waɪt laɪ/", "vi": "lời nói dối vô hại; thiện ý", "pos": "phrase"},
    # 4218: wild man
    {"ipa": "/waɪld mæn/", "vi": "người hoang dã; kẻ hung bạo dã man", "pos": "phrase"},
    # 4219: wind power
    {"ipa": "/wɪnd ˈpaʊər/", "vi": "năng lượng gió; điện sức gió", "pos": "phrase"},
    # 4220: work camp
    {"ipa": "/wɜːrk kæmp/", "vi": "trại lao động; trại cải tạo", "pos": "phrase"},
    # 4221: writing table
    {"ipa": "/ˈraɪtɪŋ ˈteɪbl/", "vi": "bàn viết thư; bàn viết làm việc", "pos": "phrase"},
    # 4222: becomes
    {"ipa": "/bɪˈkʌmz/", "vi": "trở nên; hóa thành; hợp với ai", "pos": "verb"},
    # 4223: comings
    {"ipa": "/ˈkʌmɪŋz/", "vi": "những lần ghé đến; sự đi đến", "pos": "noun"},
    # 4224: deaths
    {"ipa": "/dɛθs/", "vi": "những cái chết; các ca tử vong", "pos": "noun"},
    # 4225: foods
    {"ipa": "/fuːdz/", "vi": "các loại đồ ăn thức uống thực phẩm", "pos": "noun"},
    # 4226: guyed
    {"ipa": "/ɡaɪd/", "vi": "đã chế giễu giễu cợt; đã chằng dây", "pos": "verb"},
    # 4227: guying
    {"ipa": "/ˈɡaɪɪŋ/", "vi": "đang chế giễu giễu cợt; chằng néo", "pos": "verb"},
    # 4228: guys
    {"ipa": "/ɡaɪz/", "vi": "các anh chàng; các bạn; dây chằng", "pos": "noun"},
    # 4229: payed
    {"ipa": "/peɪd/", "vi": "đã xả dây neo tàu; đã trét hắc ín", "pos": "verb"},
    # 4230: pays
    {"ipa": "/peɪz/", "vi": "các khoản lương; những khoản lương", "pos": "noun"},
    # 4231: problems
    {"ipa": "/ˈprɑːbləmz/", "vi": "các vấn đề rắc rối; những khó khăn", "pos": "noun"},
    # 4232: truer
    {"ipa": "/ˈtruːər/", "vi": "chân thật hơn; trung thành hơn", "pos": "adj"},
    # 4233: truest
    {"ipa": "/ˈtruːɪst/", "vi": "chân thực nhất; trung thành nhất", "pos": "adj"},
    # 4234: active site
    {"ipa": "/ˈæktɪv saɪt/", "vi": "trung tâm hoạt động phân tử enzym", "pos": "phrase"},
    # 4235: air cell
    {"ipa": "/ɛr sɛl/", "vi": "buồng khí quả trứng; phế nang phổi", "pos": "phrase"},
    # 4236: air mass
    {"ipa": "/ɛr mæs/", "vi": "khối không khí lớn trong khí quyển", "pos": "phrase"},
    # 4237: approach shot
    {"ipa": "/əˈproʊtʃ ʃɑːt/", "vi": "cú đánh bóng tiếp cận lỗ golf", "pos": "phrase"},
    # 4238: army base
    {"ipa": "/ˈɑːrmi beɪs/", "vi": "căn cứ lục quân; đồn trại quân sự", "pos": "phrase"},
    # 4239: baby grand
    {"ipa": "/ˈbeɪbi ɡrænd/", "vi": "đàn đại dương cầm loại nhỏ baby", "pos": "phrase"},
    # 4240: bank manager
    {"ipa": "/bæŋk ˈmænɪdʒər/", "vi": "giám đốc chi nhánh ngân hàng", "pos": "phrase"},
    # 4241: bank statement
    {"ipa": "/bæŋk ˈsteɪtmənt/", "vi": "bản sao kê tài khoản ngân hàng", "pos": "phrase"},
    # 4242: best and greatest
    {"ipa": "/bɛst ænd ˈɡreɪtɪst/", "vi": "tốt nhất và vĩ đại nhất trần gian", "pos": "phrase"},
    # 4243: blood pressure
    {"ipa": "/blʌd ˈprɛʃər/", "vi": "chỉ số huyết áp; áp lực dòng máu", "pos": "phrase"},
    # 4244: bottom line
    {"ipa": "/ˈbɑːtəm laɪn/", "vi": "lợi nhuận ròng; điều cốt lõi nhất", "pos": "phrase"},
    # 4245: brain dead
    {"ipa": "/breɪn dɛd/", "vi": "chết não không hồi phục; ngu ngốc", "pos": "phrase"},
    # 4246: bridge over
    {"ipa": "/brɪdʒ ˈoʊvər/", "vi": "bắc cầu vượt qua; giải quyết tạm", "pos": "phrase"},
    # 4247: bus stop
    {"ipa": "/bʌs stɑːp/", "vi": "điểm dừng đón trả khách xe buýt", "pos": "phrase"},
    # 4248: car traffic
    {"ipa": "/kɑːr ˈtræfɪk/", "vi": "dòng xe cộ lưu thông; xe ô tô chạy", "pos": "phrase"},
    # 4249: cash price
    {"ipa": "/kæʃ praɪs/", "vi": "giá thanh toán ngay bằng tiền mặt", "pos": "phrase"},
    # 4250: cast around
    {"ipa": "/kæst əˈraʊnd/", "vi": "ráo riết tìm kiếm cách giải quyết", "pos": "phrase"},
    # 4251: change surface
    {"ipa": "/tʃeɪndʒ ˈsɜːrfɪs/", "vi": "thay đổi mặt sân; biến đổi bề mặt", "pos": "phrase"},
    # 4252: control condition
    {"ipa": "/kənˈtroʊl kənˈdɪʃən/", "vi": "điều kiện đối chứng khi thí nghiệm", "pos": "phrase"},
    # 4253: cover charge
    {"ipa": "/ˈkʌvər tʃɑːrdʒ/", "vi": "phí vào cửa quán bar; phụ thu chỗ", "pos": "phrase"},
    # 4254: critical point
    {"ipa": "/ˈkrɪtɪkl pɔɪnt/", "vi": "điểm tới hạn; thời điểm quyết định", "pos": "phrase"},
    # 4255: dead centre
    {"ipa": "/dɛd ˈsɛntər/", "vi": "điểm chết máy móc; chính giữa tâm", "pos": "phrase"},
    # 4256: dead letter
    {"ipa": "/dɛd ˈlɛtər/", "vi": "thư không người nhận; luật vô hiệu", "pos": "phrase"},
    # 4257: defense department
    {"ipa": "/dɪˈfɛns dɪˈpɑːrtmənt/", "vi": "bộ quốc phòng phụ trách quân đội", "pos": "phrase"},
    # 4258: defense force
    {"ipa": "/dɪˈfɛns fɔːrs/", "vi": "lực lượng quốc phòng phòng vệ", "pos": "phrase"},
    # 4259: department of defense
    {"ipa": "/dɪˈpɑːrtmənt ʌv dɪˈfɛns/", "vi": "Bộ Quốc phòng Hoa Kỳ Lầu Năm Góc", "pos": "phrase"},
    # 4260: direct action
    {"ipa": "/dəˈrɛkt ˈækʃən/", "vi": "hành động trực tiếp gây áp lực", "pos": "phrase"},
    # 4261: direct current
    {"ipa": "/dəˈrɛkt ˈkɜːrənt/", "vi": "dòng điện một chiều ký hiệu DC", "pos": "phrase"},
    # 4262: doctor of education
    {"ipa": "/ˈdɑːktər ʌv ˌɛdʒuˈkeɪʃən/", "vi": "tiến sĩ giáo dục học bằng cấp", "pos": "phrase"},
    # 4263: draw away
    {"ipa": "/drɔː əˈweɪ/", "vi": "bứt phá vượt lên; kéo lùi xa ra", "pos": "phrase"},
    # 4264: draw play
    {"ipa": "/drɔː pleɪ/", "vi": "chiêu giả chuyền chạy bóng bầu dục", "pos": "phrase"},
    # 4265: dress out
    {"ipa": "/drɛs aʊt/", "vi": "mổ thịt làm sạch thú; mặc đồ diện", "pos": "phrase"},
    # 4266: dress up
    {"ipa": "/drɛs ʌp/", "vi": "ăn diện lộng lẫy; mặc đồ hóa trang", "pos": "phrase"},
    # 4267: economy class
    {"ipa": "/ɪˈkɑːnəmi klæs/", "vi": "khoang ghế hạng phổ thông máy bay", "pos": "phrase"},
    # 4268: engineering school
    {"ipa": "/ˌɛndʒɪˈnɪrɪŋ skuːl/", "vi": "trường đào tạo kỹ sư công nghệ", "pos": "phrase"},
    # 4269: fair trade
    {"ipa": "/fɛr treɪd/", "vi": "thương mại công bằng bình đẳng", "pos": "phrase"},
    # 4270: fashion business
    {"ipa": "/ˈfæʃən ˈbɪznəs/", "vi": "kinh doanh thời trang; ngành mốt", "pos": "phrase"},
    # 4271: father christmas
    {"ipa": "/ˈfɑːðər ˈkrɪsməs/", "vi": "Ông già Noel phát quà Giáng sinh", "pos": "phrase"},
    # 4272: field of operation
    {"ipa": "/fiːld ʌv ˌɑːpəˈreɪʃən/", "vi": "địa bàn hoạt động; phạm vi thao tác", "pos": "phrase"},
    # 4273: file in
    {"ipa": "/faɪl ɪn/", "vi": "nối đuôi nhau bước vào hàng một", "pos": "phrase"},
    # 4274: financial officer
    {"ipa": "/faɪˈnænʃl ˈɔːfɪsər/", "vi": "giám đốc tài chính; cán bộ tài vụ", "pos": "phrase"},
    # 4275: finding of law
    {"ipa": "/ˈfaɪndɪŋ ʌv lɔː/", "vi": "kết luận áp dụng điều luật tòa án", "pos": "phrase"},
    # 4276: flight control
    {"ipa": "/flaɪt kənˈtroʊl/", "vi": "kiểm soát không lưu chuyến bay", "pos": "phrase"},
    # 4277: fly by
    {"ipa": "/flaɪ baɪ/", "vi": "bay lướt ngang qua; vụt bay qua", "pos": "phrase"},
    # 4278: fly on
    {"ipa": "/flaɪ ɑːn/", "vi": "tiếp tục bay xa; hạ cánh xuống tàu", "pos": "phrase"},
    # 4279: fourth power
    {"ipa": "/fɔːrθ ˈpaʊər/", "vi": "lũy thừa bậc bốn trong đại số", "pos": "phrase"},
    # 4280: free agent
    {"ipa": "/friː ˈeɪdʒənt/", "vi": "vận động viên tự do; người tự chủ", "pos": "phrase"},
    # 4281: french capital
    {"ipa": "/frɛntʃ ˈkæpɪtl/", "vi": "thủ đô Paris hoa lệ của nước Pháp", "pos": "phrase"},
    # 4282: fresh water
    {"ipa": "/frɛʃ ˈwɔːtər/", "vi": "nguồn nước ngọt; nước không mặn", "pos": "phrase"},
    # 4283: gas oil
    {"ipa": "/ɡæs ɔɪl/", "vi": "dầu đi-ê-zen sưởi ấm đốt lò", "pos": "phrase"},
    # 4284: grade school
    {"ipa": "/ɡreɪd skuːl/", "vi": "trường tiểu học dành cho trẻ em", "pos": "phrase"},
    # 4285: greater london
    {"ipa": "/ˈɡreɪtər ˈlʌndən/", "vi": "vùng đô thị Đại Luân Đôn nước Anh", "pos": "phrase"},
    # 4286: guide on
    {"ipa": "/ɡaɪd ɑːn/", "vi": "lấy làm chuẩn mực; căn cứ theo mốc", "pos": "phrase"},
    # 4287: hard surface
    {"ipa": "/hɑːrd ˈsɜːrfɪs/", "vi": "rải nhựa lát cứng bề mặt đường đi", "pos": "phrase"},
    # 4288: head count
    {"ipa": "/hɛd kaʊnt/", "vi": "việc đếm đầu người; kiểm kê sĩ số", "pos": "phrase"},
    # 4289: human foot
    {"ipa": "/ˈhjuːmən fʊt/", "vi": "bàn chân người cấu tạo giải phẫu", "pos": "phrase"},
    # 4290: income tax
    {"ipa": "/ˈɪnkʌm tæks/", "vi": "thuế thu nhập cá nhân doanh nghiệp", "pos": "phrase"},
    # 4291: india paper
    {"ipa": "/ˈɪndiə ˈpeɪpər/", "vi": "giấy in kinh thánh siêu mỏng dai", "pos": "phrase"},
    # 4292: lose track
    {"ipa": "/luːz træk/", "vi": "mất dấu vết; không theo dõi kịp", "pos": "phrase"},
    # 4293: love handle
    {"ipa": "/lʌv ˈhændl/", "vi": "ngấn mỡ thừa hai bên hông eo", "pos": "phrase"},
    # 4294: lower california
    {"ipa": "/ˈloʊər ˌkælɪˈfɔːrnjə/", "vi": "bán đảo Baja California tại Mexico", "pos": "phrase"},
    # 4295: male child
    {"ipa": "/meɪl tʃaɪld/", "vi": "bé trai nhỏ; bé trai sơ sinh", "pos": "phrase"},
    # 4296: map out
    {"ipa": "/mæp aʊt/", "vi": "vạch ra kế hoạch chiến lược tỉ mỉ", "pos": "phrase"},
    # 4297: mental case
    {"ipa": "/ˈmɛntl keɪs/", "vi": "người bệnh tâm thần; kẻ gàn dở", "pos": "phrase"},
    # 4298: money supply
    {"ipa": "/ˈmʌni səˈplaɪ/", "vi": "mức cung tiền trong nền kinh tế", "pos": "phrase"},
    # 4299: national security council
    {"ipa": "/ˈnæʃnəl sɪˈkjʊrəti ˈkaʊnsl/", "vi": "Hội đồng An ninh Quốc gia Hoa Kỳ", "pos": "phrase"}
]

with open("scratch/b21_r09_raw_p3.json", "r", encoding="utf-8") as f:
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

with open("scratch/b21_r09_p3.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(output)} entries for Round 9 Part 3.")
