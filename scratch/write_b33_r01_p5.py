import json

items = [
  {"id": "lex.en.200k.060403", "hw": "stonemasons", "pos": "noun", "ipa": "/ˈstoʊnmeɪsənz/", "vi": "thợ xây đá; thợ đẽo chạm khắc đá"},
  {"id": "lex.en.200k.060404", "hw": "tangierses", "pos": "noun", "ipa": "/tænˈdʒɪərzɪz/", "vi": "thành phố cảng Tangier Ma-rốc"},
  {"id": "lex.en.200k.060405", "hw": "tarkovskies", "pos": "noun", "ipa": "/tɑːrˈkɔːfskiz/", "vi": "đạo diễn điện ảnh Andrei Tarkovsky"},
  {"id": "lex.en.200k.060406", "hw": "tendonitides", "pos": "noun", "ipa": "/ˌtɛndəˈnaɪtɪdiːz/", "vi": "các chứng bệnh viêm gân khớp"},
  {"id": "lex.en.200k.060407", "hw": "testators", "pos": "noun", "ipa": "/ˈtɛsteɪtərz/", "vi": "người lập bản di chúc thừa kế"},
  {"id": "lex.en.200k.060408", "hw": "tricyclics", "pos": "noun", "ipa": "/traɪˈsaɪklɪks/", "vi": "thuốc chống trầm cảm ba vòng"},
  {"id": "lex.en.200k.060409", "hw": "vergers", "pos": "noun", "ipa": "/ˈvɜːrdʒərz/", "vi": "người trông coi giữ lễ nhà thờ"},
  {"id": "lex.en.200k.060410", "hw": "wagnerians", "pos": "noun", "ipa": "/vɑːɡˈnɪəriənz/", "vi": "người hâm mộ nhạc kịch Wagner"},
  {"id": "lex.en.200k.060411", "hw": "welties", "pos": "noun", "ipa": "/ˈwɛltiz/", "vi": "nữ nhà văn Mỹ Eudora Welty"},
  {"id": "lex.en.200k.060412", "hw": "wheals", "pos": "noun", "ipa": "/wiːlz/", "vi": "vết sưng đỏ nổi mề đay; vết lằn roi"},
  {"id": "lex.en.200k.060413", "hw": "wheatstones", "pos": "noun", "ipa": "/ˈwiːtstoʊnz/", "vi": "nhà vật lý Anh Charles Wheatstone"},
  {"id": "lex.en.200k.060414", "hw": "whippers", "pos": "noun", "ipa": "/ˈwɪpərz/", "vi": "người đánh roi; dụng cụ đánh kem"},
  {"id": "lex.en.200k.060415", "hw": "whitetails", "pos": "noun", "ipa": "/ˈwaɪtteɪlz/", "vi": "loài hươu đuôi trắng Bắc Mỹ"},
  {"id": "lex.en.200k.060416", "hw": "winterier", "pos": "adj", "ipa": "/ˈwɪntəriər/", "vi": "giá rét mùa đông hơn; lạnh lẽo hơn"},
  {"id": "lex.en.200k.060417", "hw": "winteriest", "pos": "adj", "ipa": "/ˈwɪntəriɪst/", "vi": "giá rét mùa đông nhất; lạnh buốt"},
  {"id": "lex.en.200k.060418", "hw": "woodcutters", "pos": "noun", "ipa": "/ˈwʊdkʌtərz/", "vi": "người tiều phu đốn củi rừng"},
  {"id": "lex.en.200k.060419", "hw": "zamas", "pos": "noun", "ipa": "/ˈzɑːməz/", "vi": "trận quyết chiến Zama cổ đại"},
  {"id": "lex.en.200k.060420", "hw": "alfred de musset", "pos": "phrase", "ipa": "/ˌælfrɛd də mjuːˈseɪ/", "vi": "nhà thơ Pháp Alfred de Musset"},
  {"id": "lex.en.200k.060421", "hw": "allegro con spirito", "pos": "phrase", "ipa": "/əˈlɛɡroʊ kɑːn ˈspɪrɪtoʊ/", "vi": "nhịp nhanh đầy hứng khởi âm nhạc"},
  {"id": "lex.en.200k.060422", "hw": "alopecia areata", "pos": "phrase", "ipa": "/ˌæləˈpiːʃə ˌɛriˈeɪtə/", "vi": "chứng rụng tóc từng mảng tròn"},
  {"id": "lex.en.200k.060423", "hw": "anemone virginiana", "pos": "phrase", "ipa": "/əˈnɛməni vərˌdʒɪniˈeɪnə/", "vi": "cây hoa hải quỳ Virginia Bắc Mỹ"},
  {"id": "lex.en.200k.060424", "hw": "anterior serratus muscle", "pos": "phrase", "ipa": "/ænˈtɪəriər səˈreɪtəs ˈmʌsl/", "vi": "cơ răng cưa trước lồng ngực"},
  {"id": "lex.en.200k.060425", "hw": "antineoplastic drug", "pos": "phrase", "ipa": "/ˌæntiˌniːoʊˈplæstɪk drʌɡ/", "vi": "thuốc hóa trị chống khối u ung thư"},
  {"id": "lex.en.200k.060426", "hw": "anton pavlovich chekhov", "pos": "phrase", "ipa": "/ˈɑːntɑːn ˈpɑːvləvɪtʃ ˈtʃɛkɔːf/", "vi": "đại văn hào Nga Anton Chekhov"},
  {"id": "lex.en.200k.060427", "hw": "arc secant", "pos": "phrase", "ipa": "/ɑːrk ˈsiːkənt/", "vi": "hàm lượng giác ngược cung sec"},
  {"id": "lex.en.200k.060428", "hw": "articulatory system", "pos": "phrase", "ipa": "/ɑːrˈtɪkjʊlətɔːri ˈsɪstəm/", "vi": "hệ thống cơ quan phát âm ngôn ngữ"},
  {"id": "lex.en.200k.060429", "hw": "australian turtledove", "pos": "phrase", "ipa": "/ɔːˈstreɪljən ˈtɜːrtldʌv/", "vi": "chim cu gáy vằn nước Úc"},
  {"id": "lex.en.200k.060430", "hw": "bog bilberry", "pos": "phrase", "ipa": "/bɑːɡ ˈbɪlbɛri/", "vi": "cây việt quất đầm lầy quả xanh"},
  {"id": "lex.en.200k.060431", "hw": "candlemas day", "pos": "phrase", "ipa": "/ˈkændlməs deɪ/", "vi": "lễ Dâng Chúa trong đền thờ"},
  {"id": "lex.en.200k.060432", "hw": "catsup bottle", "pos": "phrase", "ipa": "/ˈkɛtʃəp ˈbɑːtl/", "vi": "chai đựng nước tương cà chua"},
  {"id": "lex.en.200k.060433", "hw": "cinchona bark", "pos": "phrase", "ipa": "/sɪŋˈkoʊnə bɑːrk/", "vi": "vỏ cây canh-ki-na chữa sốt rét"},
  {"id": "lex.en.200k.060434", "hw": "cinchona tree", "pos": "phrase", "ipa": "/sɪŋˈkoʊnə triː/", "vi": "cây canh-ki-na nguồn chất quinin"},
  {"id": "lex.en.200k.060435", "hw": "citrus reticulata", "pos": "phrase", "ipa": "/ˈsɪtrəs rɪˌtɪkjʊˈleɪtə/", "vi": "cây quýt ngọt thuộc chi cam chanh"},
  {"id": "lex.en.200k.060436", "hw": "cornus mas", "pos": "phrase", "ipa": "/ˈkɔːrnəs mæs/", "vi": "cây sơn thù du hoa vàng châu Âu"},
  {"id": "lex.en.200k.060437", "hw": "cumulonimbus cloud", "pos": "phrase", "ipa": "/ˌkjuːmjʊloʊˈnɪmbəs klaʊd/", "vi": "đám mây vũ tích gây mưa giông"},
  {"id": "lex.en.200k.060438", "hw": "dumdum bullet", "pos": "phrase", "ipa": "/ˈdʌmdʌm ˈbʊlɪt/", "vi": "đạn đầu mềm nổ phá đum-đum"},
  {"id": "lex.en.200k.060439", "hw": "dumdum fever", "pos": "phrase", "ipa": "/ˈdʌmdʌm ˈfiːvər/", "vi": "bệnh sốt đen nội tạng ký sinh"},
  {"id": "lex.en.200k.060440", "hw": "dwarf bilberry", "pos": "phrase", "ipa": "/dwɔːrf ˈbɪlbɛri/", "vi": "cây việt quất bụi lùn vùng núi"},
  {"id": "lex.en.200k.060441", "hw": "edmond de goncourt", "pos": "phrase", "ipa": "/ˈɛdmɑːnd də ɡɔ̃ˈkuːr/", "vi": "nhà văn Pháp Edmond de Goncourt"},
  {"id": "lex.en.200k.060442", "hw": "gaius valerius catullus", "pos": "phrase", "ipa": "/ˈɡaɪəs vəˈlɪriəs kəˈtʌləs/", "vi": "nhà thơ trữ tình La Mã Catullus"},
  {"id": "lex.en.200k.060443", "hw": "genus cornus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈkɔːrnəs/", "vi": "chi thực vật cây sơn thù du"},
  {"id": "lex.en.200k.060444", "hw": "genus juniperus", "pos": "phrase", "ipa": "/ˈdʒiːnəs dʒuːˈnɪpərəs/", "vi": "chi thực vật cây bách xù"},
  {"id": "lex.en.200k.060445", "hw": "genus otus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈoʊtəs/", "vi": "chi chim cú mèo nhỏ tai dài Otus"},
  {"id": "lex.en.200k.060446", "hw": "genus pandanus", "pos": "phrase", "ipa": "/ˈdʒiːnəs pænˈdeɪnəs/", "vi": "chi thực vật cây dứa dại dứa thơm"},
  {"id": "lex.en.200k.060447", "hw": "genus phalaenopsis", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌfælɪˈnɑːpsɪs/", "vi": "chi hoa phong lan hồ điệp"},
  {"id": "lex.en.200k.060448", "hw": "genus tyrannus", "pos": "phrase", "ipa": "/ˈdʒiːnəs taɪˈrænəs/", "vi": "chi chim đớp ruồi bạo chúa Mỹ"},
  {"id": "lex.en.200k.060449", "hw": "george boole", "pos": "phrase", "ipa": "/dʒɔːrdʒ buːl/", "vi": "nhà toán học logic George Boole"},
  {"id": "lex.en.200k.060450", "hw": "gulf of tehuantepec", "pos": "phrase", "ipa": "/ɡʌlf əv təˈwɑːntəpɛk/", "vi": "vịnh biển Tehuantepec ở Mexico"},
  {"id": "lex.en.200k.060451", "hw": "hendrik verwoerd", "pos": "phrase", "ipa": "/ˈhɛndrɪk fərˈvʊərt/", "vi": "cựu Thủ tướng Nam Phi Verwoerd"},
  {"id": "lex.en.200k.060452", "hw": "hideki yukawa", "pos": "phrase", "ipa": "/hɪˈdɛki juːˈkɑːwə/", "vi": "nhà vật lý Nobel Hideki Yukawa"},
  {"id": "lex.en.200k.060453", "hw": "hilaire belloc", "pos": "phrase", "ipa": "/hɪˈlɛər ˈbɛlɑːk/", "vi": "nhà văn sử gia Anh Hilaire Belloc"},
  {"id": "lex.en.200k.060454", "hw": "hybrid tuberous begonia", "pos": "phrase", "ipa": "/ˈhaɪbrɪd ˈtuːbərəs bɪˈɡoʊniə/", "vi": "cây hoa thu hải đường củ lai"},
  {"id": "lex.en.200k.060455", "hw": "iguazu falls", "pos": "phrase", "ipa": "/ˌiːɡwəˈsuː fɔːlz/", "vi": "quần thể thác nước hùng vĩ Iguazu"},
  {"id": "lex.en.200k.060456", "hw": "iris pallida", "pos": "phrase", "ipa": "/ˈaɪrɪs ˈpælɪdə/", "vi": "hoa diên vĩ Dalmatic thơm rễ"},
  {"id": "lex.en.200k.060457", "hw": "isamu noguchi", "pos": "phrase", "ipa": "/iːˈsɑːmuː noʊˈɡuːtʃi/", "vi": "nhà điêu khắc Mỹ-Nhật Noguchi"},
  {"id": "lex.en.200k.060458", "hw": "jacobus arminius", "pos": "phrase", "ipa": "/dʒəˈkoʊbəs ɑːrˈmɪniəs/", "vi": "nhà thần học Hà Lan Arminius"},
  {"id": "lex.en.200k.060459", "hw": "kumquat tree", "pos": "phrase", "ipa": "/ˈkʌmkwɑːt triː/", "vi": "cây quất cảnh; cây tắc quả vàng"},
  {"id": "lex.en.200k.060460", "hw": "lead chromate", "pos": "phrase", "ipa": "/lɛd ˈkroʊmeɪt/", "vi": "hợp chất màu vàng chì cromat"},
  {"id": "lex.en.200k.060461", "hw": "long hundredweight", "pos": "phrase", "ipa": "/lɔːŋ ˈhʌndrədweɪt/", "vi": "đơn vị tạ Anh bằng 112 pound"},
  {"id": "lex.en.200k.060462", "hw": "meadow pipit", "pos": "phrase", "ipa": "/ˈmɛdoʊ ˈpɪpɪt/", "vi": "loài chim manh đồng cỏ châu Âu"},
  {"id": "lex.en.200k.060463", "hw": "meles meles", "pos": "phrase", "ipa": "/ˈmiːliːz ˈmiːliːz/", "vi": "loài lửng mật vằn mặt châu Âu"},
  {"id": "lex.en.200k.060464", "hw": "metric hundredweight", "pos": "phrase", "ipa": "/ˈmɛtrɪk ˈhʌndrədweɪt/", "vi": "đơn vị khối lượng tạ hệ mét 50kg"},
  {"id": "lex.en.200k.060465", "hw": "monophonic music", "pos": "phrase", "ipa": "/ˌmɑːnəˈfɑːnɪk ˈmjuːzɪk/", "vi": "nhạc đơn âm chỉ một giai điệu"},
  {"id": "lex.en.200k.060466", "hw": "northern snakehead", "pos": "phrase", "ipa": "/ˈnɔːrðərn ˈsneɪkhɛd/", "vi": "cá quả phương bắc; cá lóc hoa"},
  {"id": "lex.en.200k.060467", "hw": "noughts and crosses", "pos": "phrase", "ipa": "/nɔːts ænd ˈkrɔːsɪz/", "vi": "trò chơi cờ ca-rô X-O ba ô"},
  {"id": "lex.en.200k.060468", "hw": "nucleolar organiser", "pos": "phrase", "ipa": "/nuːˈkliːələr ˈɔːrɡənaɪzər/", "vi": "vùng tổ chức hạch nhân NST"},
  {"id": "lex.en.200k.060469", "hw": "osseous labyrinth", "pos": "phrase", "ipa": "/ˈɑːsiəs ˈlæbərɪnθ/", "vi": "mê đạo xương tai trong giải phẫu"},
  {"id": "lex.en.200k.060470", "hw": "oval kumquat", "pos": "phrase", "ipa": "/ˈoʊvəl ˈkʌmkwɑːt/", "vi": "cây quất trái bầu dục Nagami"},
  {"id": "lex.en.200k.060471", "hw": "pan troglodytes troglodytes", "pos": "phrase", "ipa": "/pæn ˌtrɑːɡləˈdaɪtiːz ˌtrɑːɡləˈdaɪtiːz/", "vi": "tinh tinh mặt đen vùng Trung Phi"},
  {"id": "lex.en.200k.060472", "hw": "parietal pleura", "pos": "phrase", "ipa": "/pəˈraɪətl ˈplʊərə/", "vi": "lá thành màng phổi bọc lồng ngực"},
  {"id": "lex.en.200k.060473", "hw": "political incorrectness", "pos": "phrase", "ipa": "/pəˈlɪtɪkl ˌɪnkəˈrɛktnəs/", "vi": "sự phát ngôn kém nhạy cảm xã hội"},
  {"id": "lex.en.200k.060474", "hw": "posterior serratus muscle", "pos": "phrase", "ipa": "/pɑːˈstɪəriər səˈreɪtəs ˈmʌsl/", "vi": "cơ răng cưa sau vùng lưng"},
  {"id": "lex.en.200k.060475", "hw": "primary amenorrhea", "pos": "phrase", "ipa": "/ˈpraɪmɛri eɪˌmɛnəˈriːə/", "vi": "chứng vô kinh nguyên phát ở nữ"},
  {"id": "lex.en.200k.060476", "hw": "redback vole", "pos": "phrase", "ipa": "/ˈrɛdbæk voʊl/", "vi": "loài chuột đồng lưng nâu đỏ"},
  {"id": "lex.en.200k.060477", "hw": "regular icosahedron", "pos": "phrase", "ipa": "/ˈrɛɡjələr aɪˌkɑːsəˈhiːdrən/", "vi": "khối hai mươi mặt tam giác đều"},
  {"id": "lex.en.200k.060478", "hw": "round kumquat", "pos": "phrase", "ipa": "/raʊnd ˈkʌmkwɑːt/", "vi": "cây quất quả tròn Marumi"},
  {"id": "lex.en.200k.060479", "hw": "salix lucida", "pos": "phrase", "ipa": "/ˈseɪlɪks ˈluːsɪdə/", "vi": "loài cây liễu lá bóng Bắc Mỹ"},
  {"id": "lex.en.200k.060480", "hw": "salix repens", "pos": "phrase", "ipa": "/ˈseɪlɪks ˈriːpɛnz/", "vi": "loài cây liễu bụi thấp thân bò"},
  {"id": "lex.en.200k.060481", "hw": "secondary amenorrhea", "pos": "phrase", "ipa": "/ˈsɛkəndɛri eɪˌmɛnəˈriːə/", "vi": "chứng vô kinh thứ phát mất kinh"},
  {"id": "lex.en.200k.060482", "hw": "sensorineural hearing loss", "pos": "phrase", "ipa": "/ˌsɛnsəriˈnjʊərəl ˈhɪərɪŋ lɔːs/", "vi": "điếc tiếp nhận thần kinh thính giác"},
  {"id": "lex.en.200k.060483", "hw": "serratus anterior", "pos": "phrase", "ipa": "/səˈreɪtəs ænˈtɪəriər/", "vi": "cơ răng cưa trước bên sườn ngực"},
  {"id": "lex.en.200k.060484", "hw": "serratus magnus", "pos": "phrase", "ipa": "/səˈreɪtəs ˈmæɡnəs/", "vi": "bó cơ răng cưa lớn kéo xương vai"},
  {"id": "lex.en.200k.060485", "hw": "serratus posterior", "pos": "phrase", "ipa": "/səˈreɪtəs pɑːˈstɪəriər/", "vi": "cơ răng cưa sau hỗ trợ hô hấp"},
  {"id": "lex.en.200k.060486", "hw": "serratus posterior superior", "pos": "phrase", "ipa": "/səˈreɪtəs pɑːˈstɪəriər suːˈpɪriər/", "vi": "cơ răng cưa sau trên nâng sườn"},
  {"id": "lex.en.200k.060487", "hw": "severable contract", "pos": "phrase", "ipa": "/ˈsɛvərəbl ˈkɑːntrækt/", "vi": "hợp đồng chia tách điều khoản được"},
  {"id": "lex.en.200k.060488", "hw": "short hundredweight", "pos": "phrase", "ipa": "/ʃɔːrt ˈhʌndrədweɪt/", "vi": "đơn vị tạ Mỹ bằng 100 pound"},
  {"id": "lex.en.200k.060489", "hw": "snellen chart", "pos": "phrase", "ipa": "/ˈsnɛlən tʃɑːrt/", "vi": "bảng chữ cái đo thị lực Snellen"},
  {"id": "lex.en.200k.060490", "hw": "snellen test", "pos": "phrase", "ipa": "/ˈsnɛlən tɛst/", "vi": "bài kiểm tra đo thị lực Snellen"},
  {"id": "lex.en.200k.060491", "hw": "the tempter", "pos": "phrase", "ipa": "/ðə ˈtɛmptər/", "vi": "quỷ Satan kẻ cám dỗ nhân loại"},
  {"id": "lex.en.200k.060492", "hw": "troglodytes troglodytes", "pos": "phrase", "ipa": "/ˌtrɑːɡləˈdaɪtiːz ˌtrɑːɡləˈdaɪtiːz/", "vi": "chim hồng tước nhỏ Bắc bán cầu"},
  {"id": "lex.en.200k.060493", "hw": "tuberous begonia", "pos": "phrase", "ipa": "/ˈtuːbərəs bɪˈɡoʊniə/", "vi": "cây hoa thu hải đường thân củ"},
  {"id": "lex.en.200k.060494", "hw": "tyrrhenian sea", "pos": "phrase", "ipa": "/tɪˈriːniən siː/", "vi": "biển Tyrrhenus ngoài khơi nước Ý"},
  {"id": "lex.en.200k.060495", "hw": "ulmus americana", "pos": "phrase", "ipa": "/ˈʌlməs əˌmɛrɪˈkeɪnə/", "vi": "cây du trắng cổ thụ Bắc Mỹ"},
  {"id": "lex.en.200k.060496", "hw": "uranyl group", "pos": "phrase", "ipa": "/ˈjʊərənɪl ɡruːp/", "vi": "nhóm hóa học ion uranyl UO2"},
  {"id": "lex.en.200k.060497", "hw": "uranyl radical", "pos": "phrase", "ipa": "/ˈjʊərənɪl ˈrædɪkl/", "vi": "gốc hóa học uranyl mang điện dương"},
  {"id": "lex.en.200k.060498", "hw": "vanguards of conquest", "pos": "phrase", "ipa": "/ˈvænɡɑːrdz əv ˈkɑːŋkwɛst/", "vi": "đội quân tiên phong chinh phạt"},
  {"id": "lex.en.200k.060499", "hw": "vena tibialis", "pos": "phrase", "ipa": "/ˈviːnə ˌtɪbiˈeɪlɪs/", "vi": "tĩnh mạch chày dẫn máu cẳng chân"},
  {"id": "lex.en.200k.060500", "hw": "william stanley jevons", "pos": "phrase", "ipa": "/ˈwɪljəm ˈstænli ˈdʒɛvənz/", "vi": "nhà kinh tế học William Jevons"},
  {"id": "lex.en.200k.060501", "hw": "ablutions", "pos": "noun", "ipa": "/əˈbluːʃənz/", "vi": "nghi thức tắm rửa tẩy uế tôn giáo"},
  {"id": "lex.en.200k.060502", "hw": "alcaldes", "pos": "noun", "ipa": "/ælˈkɑːldeɪz/", "vi": "chức thị trưởng vùng Tây Ban Nha"}
]

with open('scratch/b33_r01_raw_p5.json') as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"Mismatch id at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"Mismatch hw at {i}: {item['hw']} vs {r['hw']}"
    assert len(item['vi']) <= 35, f"vi length > 35 at {i} ({item['hw']}): {len(item['vi'])}"
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {item['pos']}"
    if ' ' not in item['hw']:
        assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Invalid ipa at {i}: {item['ipa']}"
    r['pos'] = item['pos']
    r['ipa'] = item['ipa']
    r['vi'] = item['vi']
    r['status'] = 'reviewed'

with open('scratch/b33_r01_p5.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 1 Part 5 validated and written successfully.")
