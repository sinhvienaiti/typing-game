import json

items = [
  {"id": "lex.en.200k.063603", "hw": "ductless gland", "pos": "phrase", "ipa": "/ˈdʌktləs ɡlænd/", "vi": "tuyến nội tiết không ống dẫn"},
  {"id": "lex.en.200k.063604", "hw": "emanuel svedberg", "pos": "phrase", "ipa": "/ɪˈmænjuəl ˈsveɪdbɛrɡ/", "vi": "nhà thần học Thụy Điển Swedenborg"},
  {"id": "lex.en.200k.063605", "hw": "entente cordiale", "pos": "phrase", "ipa": "/ɑːnˈtɑːnt kɔːrdiˈɑːl/", "vi": "hiệp ước thân thiện Anh-Pháp 1904"},
  {"id": "lex.en.200k.063606", "hw": "feodor dostoevsky", "pos": "phrase", "ipa": "/ˈfjɔːdər ˌdɔːstəˈjɛfski/", "vi": "đại văn hào Nga Dostoevsky"},
  {"id": "lex.en.200k.063607", "hw": "feodor dostoyevsky", "pos": "phrase", "ipa": "/ˈfjɔːdər ˌdɔːstɔɪˈjɛfski/", "vi": "nhà văn hiện thực Nga Dostoyevsky"},
  {"id": "lex.en.200k.063608", "hw": "fritz kreisler", "pos": "phrase", "ipa": "/frɪts ˈkraɪslər/", "vi": "nghệ sĩ vĩ cầm Áo Fritz Kreisler"},
  {"id": "lex.en.200k.063609", "hw": "genus bombus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈbɑːmbəs/", "vi": "chi ong nghệ lông xù Bombus"},
  {"id": "lex.en.200k.063610", "hw": "genus cervus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈsɜːrvəs/", "vi": "chi động vật hươu nai lớn Cervus"},
  {"id": "lex.en.200k.063611", "hw": "genus khaya", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈkaɪə/", "vi": "chi cây gỗ dái ngựa gụ châu Phi"},
  {"id": "lex.en.200k.063612", "hw": "genus malva", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈmælvə/", "vi": "chi cây cẩm quỳ hoa đẹp Malva"},
  {"id": "lex.en.200k.063613", "hw": "genus philadelphus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌfɪləˈdɛlfəs/", "vi": "chi bụi hoa thơm nhài dại giả cam"},
  {"id": "lex.en.200k.063614", "hw": "genus ulva", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈʌlvə/", "vi": "chi rong biển xanh rau diếp biển"},
  {"id": "lex.en.200k.063615", "hw": "george herbert hitchings", "pos": "phrase", "ipa": "/dʒɔːrdʒ ˈhɜːrbərt ˈhɪtʃɪŋz/", "vi": "nhà dược lý học Nobel Hitchings"},
  {"id": "lex.en.200k.063616", "hw": "giovanni battista tiepolo", "pos": "phrase", "ipa": "/dʒoʊˈvɑːni bɑːˈtiːstə ˈtjɛpəloʊ/", "vi": "họa sĩ Baroque Ý Giovanni Tiepolo"},
  {"id": "lex.en.200k.063617", "hw": "isaac bashevis singer", "pos": "phrase", "ipa": "/ˈaɪzək bəˈʃeɪvɪs ˈsɪŋər/", "vi": "nhà văn Nobel văn học Isaac Singer"},
  {"id": "lex.en.200k.063618", "hw": "jamaica bayberry", "pos": "phrase", "ipa": "/dʒəˈmeɪkə ˈbeɪˌbɛri/", "vi": "cây lá thơm làm tinh dầu Jamaica"},
  {"id": "lex.en.200k.063619", "hw": "juniperus communis", "pos": "phrase", "ipa": "/dʒuːˈnɪpərəs kəˈmjuːnɪs/", "vi": "cây bách xù thông quả làm rượu gin"},
  {"id": "lex.en.200k.063620", "hw": "kingdom animalia", "pos": "phrase", "ipa": "/ˈkɪŋdəm ˌænɪˈmeɪliə/", "vi": "giới Động vật trong sinh học"},
  {"id": "lex.en.200k.063621", "hw": "kuroshio current", "pos": "phrase", "ipa": "/ˌkʊrəˈʃiːoʊ ˈkɜːrənt/", "vi": "hải lưu ấm Kuroshio vùng Nhật Bản"},
  {"id": "lex.en.200k.063622", "hw": "madame de maintenon", "pos": "phrase", "ipa": "/məˈdæm də ˌmæntəˈnɔːn/", "vi": "phu nhân quý tộc Pháp Maintenon"},
  {"id": "lex.en.200k.063623", "hw": "mercuric chloride", "pos": "phrase", "ipa": "/mərˈkjʊrɪk ˈklɔːraɪd/", "vi": "hợp chất độc thủy ngân (II) clorua"},
  {"id": "lex.en.200k.063624", "hw": "mikhail glinka", "pos": "phrase", "ipa": "/mɪˈxaɪl ˈɡlɪŋkə/", "vi": "nhà soạn nhạc cổ điển Nga Glinka"},
  {"id": "lex.en.200k.063625", "hw": "mikhail sergeyevich gorbachev", "pos": "phrase", "ipa": "/mɪˈxaɪl sərˈɡeɪəvɪtʃ ˈɡɔːrbətʃɔːf/", "vi": "nhà lãnh đạo Liên Xô Gorbachev"},
  {"id": "lex.en.200k.063626", "hw": "mirabilis californica", "pos": "phrase", "ipa": "/mɪˈræbəlɪs ˌkælɪˈfɔːrnɪkə/", "vi": "cây hoa bốn giờ hồng California"},
  {"id": "lex.en.200k.063627", "hw": "negative reinforcer", "pos": "phrase", "ipa": "/ˈnɛɡətɪv ˌriːɪnˈfɔːrsər/", "vi": "tác nhân củng cố hành vi tiêu cực"},
  {"id": "lex.en.200k.063628", "hw": "numeration system", "pos": "phrase", "ipa": "/ˌnuːməˈreɪʃən ˈsɪstəm/", "vi": "hệ thống đếm và ký hiệu ghi số"},
  {"id": "lex.en.200k.063629", "hw": "orange pekoe", "pos": "phrase", "ipa": "/ˈɔːrɪndʒ ˈpiːkoʊ/", "vi": "loại trà đen búp lá nguyên phẩm"},
  {"id": "lex.en.200k.063630", "hw": "panchen lama", "pos": "phrase", "ipa": "/ˈpɑːntʃɛn ˈlɑːmə/", "vi": "Đức Ban-thiền Lạt-ma Tây Tạng"},
  {"id": "lex.en.200k.063631", "hw": "paranasal sinus", "pos": "phrase", "ipa": "/ˌpærəˈneɪzəl ˈsaɪnəs/", "vi": "xoang cạnh mũi chứa khí vùng mặt"},
  {"id": "lex.en.200k.063632", "hw": "phaseolus vulgaris", "pos": "phrase", "ipa": "/fəˈsiːələs vʌlˈɡɛrɪs/", "vi": "cây đậu cô ve hạt xanh phổ biến"},
  {"id": "lex.en.200k.063633", "hw": "photostat machine", "pos": "phrase", "ipa": "/ˈfoʊtəstæt məˈʃiːn/", "vi": "máy sao chụp tài liệu quang học cũ"},
  {"id": "lex.en.200k.063634", "hw": "phrenic nerve", "pos": "phrase", "ipa": "/ˈfrɛnɪk nɜːrv/", "vi": "dây thần kinh hoành điều khiển thở"},
  {"id": "lex.en.200k.063635", "hw": "phrenic vein", "pos": "phrase", "ipa": "/ˈfrɛnɪk veɪn/", "vi": "tĩnh mạch hoành dẫn máu cơ hoành"},
  {"id": "lex.en.200k.063636", "hw": "pieter brueghel", "pos": "phrase", "ipa": "/ˈpiːtər ˈbrɔɪɡəl/", "vi": "danh họa Phục Hưng Hà Lan Bruegel"},
  {"id": "lex.en.200k.063637", "hw": "positive reinforcer", "pos": "phrase", "ipa": "/ˈpɑːzətɪv ˌriːɪnˈfɔːrsər/", "vi": "tác nhân thưởng củng cố tích cực"},
  {"id": "lex.en.200k.063638", "hw": "puka inti", "pos": "phrase", "ipa": "/ˈpuːkə ˈɪnti/", "vi": "nhóm nổi dậy Mặt Trời Đỏ ở Peru"},
  {"id": "lex.en.200k.063639", "hw": "queen regnant", "pos": "phrase", "ipa": "/kwiːn ˈrɛɡnənt/", "vi": "nữ vương trực tiếp nắm quyền trị vì"},
  {"id": "lex.en.200k.063640", "hw": "rashtriya swayamsevak sangh", "pos": "phrase", "ipa": "/rɑːʃˈtriːjə swəˌjʌmˈseɪvək ˈsʌŋɡ/", "vi": "tổ chức dân tộc Hindu giáo Ấn Độ"},
  {"id": "lex.en.200k.063641", "hw": "richard brinsley sheridan", "pos": "phrase", "ipa": "/ˈrɪtʃərd ˈbrɪnzli ˈʃɛrədən/", "vi": "nhà viết kịch chính khách Sheridan"},
  {"id": "lex.en.200k.063642", "hw": "roble beech", "pos": "phrase", "ipa": "/ˈroʊbleɪ biːtʃ/", "vi": "cây sồi phương nam cao lớn Nam Mỹ"},
  {"id": "lex.en.200k.063643", "hw": "rusty grackle", "pos": "phrase", "ipa": "/ˈrʌsti ˈɡrækəl/", "vi": "chim sáo đen lông gỉ sắt Bắc Mỹ"},
  {"id": "lex.en.200k.063644", "hw": "sabal palmetto", "pos": "phrase", "ipa": "/ˈseɪbəl pælˈmɛtoʊ/", "vi": "cây cọ lùn lá quạt bang Florida"},
  {"id": "lex.en.200k.063645", "hw": "seborrheic eczema", "pos": "phrase", "ipa": "/ˌsɛbəˈriːɪk ˈɛkzəmə/", "vi": "bệnh chàm viêm da tiết bã nhờn"},
  {"id": "lex.en.200k.063646", "hw": "sylvian aqueduct", "pos": "phrase", "ipa": "/ˈsɪlviən ˈækwəˌdʌkt/", "vi": "cống não Sylvius thông não thất"},
  {"id": "lex.en.200k.063647", "hw": "sylvian fissure", "pos": "phrase", "ipa": "/ˈsɪlviən ˈfɪʃər/", "vi": "rãnh bên Sylvius trên vỏ đại não"},
  {"id": "lex.en.200k.063648", "hw": "system of numeration", "pos": "phrase", "ipa": "/ˈsɪstəm əv ˌnuːməˈreɪʃən/", "vi": "hệ thống biểu diễn ký tự chữ số"},
  {"id": "lex.en.200k.063649", "hw": "tactile agnosia", "pos": "phrase", "ipa": "/ˈtæktaɪl æɡˈnoʊʒə/", "vi": "chứng không nhận diện vật bằng sờ"},
  {"id": "lex.en.200k.063650", "hw": "te kanawa", "pos": "phrase", "ipa": "/teɪ ˈkɑːnəwə/", "vi": "nữ danh ca opera Kiri Te Kanawa"},
  {"id": "lex.en.200k.063651", "hw": "teleost fish", "pos": "phrase", "ipa": "/ˈtɛliɑːst fɪʃ/", "vi": "loài cá xương thật hiện đại"},
  {"id": "lex.en.200k.063652", "hw": "valentina tereshkova", "pos": "phrase", "ipa": "/ˌvælənˈtiːnə ˌtɛrəʃˈkoʊvə/", "vi": "nữ phi hành gia đầu tiên vũ trụ"},
  {"id": "lex.en.200k.063653", "hw": "willa sibert cather", "pos": "phrase", "ipa": "/ˈwɪlə ˈsaɪbərt ˈkæðər/", "vi": "nữ tiểu thuyết gia Mỹ Willa Cather"},
  {"id": "lex.en.200k.063654", "hw": "william lawrence shirer", "pos": "phrase", "ipa": "/ˈwɪliəm ˈlɔːrəns ˈʃaɪrər/", "vi": "nhà báo sử gia Mỹ William Shirer"},
  {"id": "lex.en.200k.063655", "hw": "william tindale", "pos": "phrase", "ipa": "/ˈwɪliəm ˈtɪndəl/", "vi": "nhà dịch Kinh Thánh Anh Tyndale"},
  {"id": "lex.en.200k.063656", "hw": "zona pellucida", "pos": "phrase", "ipa": "/ˈzoʊnə pəˈluːsɪdə/", "vi": "màng trong suốt bao quanh noãn cầu"},
  {"id": "lex.en.200k.063657", "hw": "advowsons", "pos": "noun", "ipa": "/ədˈvaʊzənz/", "vi": "quyền đề cử giáo sĩ quản xứ Anh"},
  {"id": "lex.en.200k.063658", "hw": "airguns", "pos": "noun", "ipa": "/ˈɛərɡʌnz/", "vi": "súng hơi bắn đạn chì bằng khí nén"},
  {"id": "lex.en.200k.063659", "hw": "akkos", "pos": "noun", "ipa": "/ˈɑːkoʊz/", "vi": "thành phố cảng cổ Akko ở Israel"},
  {"id": "lex.en.200k.063660", "hw": "aliquots", "pos": "noun", "ipa": "/ˈælɪkwɑːts/", "vi": "ước số nguyên; phần mẫu thí nghiệm"},
  {"id": "lex.en.200k.063661", "hw": "anaphases", "pos": "noun", "ipa": "/ˈænəˌfeɪzɪz/", "vi": "kỳ sau trong quá trình phân bào"},
  {"id": "lex.en.200k.063662", "hw": "anomies", "pos": "noun", "ipa": "/ˈænəmiz/", "vi": "tình trạng hỗn loạn vô chuẩn mực"},
  {"id": "lex.en.200k.063663", "hw": "apraxias", "pos": "noun", "ipa": "/əˈpræksiəz/", "vi": "chứng rối loạn thực hiện động tác"},
  {"id": "lex.en.200k.063664", "hw": "argots", "pos": "noun", "ipa": "/ˈɑːrɡoʊz/", "vi": "biệt ngữ tiếng lóng nội bộ riêng"},
  {"id": "lex.en.200k.063665", "hw": "arianisms", "pos": "noun", "ipa": "/ˈɛriəˌnɪzəmz/", "vi": "học thuyết Cơ Đốc cổ đại Arius"},
  {"id": "lex.en.200k.063666", "hw": "azurites", "pos": "noun", "ipa": "/ˈæʒəraɪts/", "vi": "khoáng vật đá xanh lam đồng azurit"},
  {"id": "lex.en.200k.063667", "hw": "bakehouses", "pos": "noun", "ipa": "/ˈbeɪkhaʊzɪz/", "vi": "lò nướng bánh mì; xưởng làm bánh"},
  {"id": "lex.en.200k.063668", "hw": "ballades", "pos": "noun", "ipa": "/bæˈlɑːdz/", "vi": "thơ ba-lát cổ điển; bản nhạc ba-lát"},
  {"id": "lex.en.200k.063669", "hw": "barishes", "pos": "noun", "ipa": "/ˈbærɪʃɪz/", "vi": "nhóm ngôn ngữ Tạng-Miến Barish"},
  {"id": "lex.en.200k.063670", "hw": "bedposts", "pos": "noun", "ipa": "/ˈbɛdpoʊsts/", "vi": "cột trụ bốn góc khung giường ngủ"},
  {"id": "lex.en.200k.063671", "hw": "binderies", "pos": "noun", "ipa": "/ˈbaɪndəriz/", "vi": "xưởng khâu gấp đóng bìa sách vở"},
  {"id": "lex.en.200k.063672", "hw": "blats", "pos": "verb", "ipa": "/blæts/", "vi": "kêu be be; khóc rống hoặc thổi ầm"},
  {"id": "lex.en.200k.063673", "hw": "blatted", "pos": "verb", "ipa": "/ˈblætɪd/", "vi": "đã kêu be be; đã thổi kèn chói tai"},
  {"id": "lex.en.200k.063674", "hw": "blatting", "pos": "verb", "ipa": "/ˈblætɪŋ/", "vi": "đang kêu be be; đang nói lải nhải"},
  {"id": "lex.en.200k.063675", "hw": "borrelias", "pos": "noun", "ipa": "/bəˈriːliəz/", "vi": "xoắn khuẩn Borrelia gây bệnh Lyme"},
  {"id": "lex.en.200k.063676", "hw": "bowsprits", "pos": "noun", "ipa": "/ˈboʊsprɪts/", "vi": "thanh gỗ nhô ở mũi tàu giương buồm"},
  {"id": "lex.en.200k.063677", "hw": "braggadocios", "pos": "noun", "ipa": "/ˌbræɡəˈdoʊʃioʊz/", "vi": "thói khoác lác ba hoa; kẻ hay nổ"},
  {"id": "lex.en.200k.063678", "hw": "bremerhavens", "pos": "noun", "ipa": "/ˈbreɪmərˌhɑːfənz/", "vi": "cảng biển Bremerhaven miền bắc Đức"},
  {"id": "lex.en.200k.063679", "hw": "caftans", "pos": "noun", "ipa": "/ˈkæftænz/", "vi": "áo choàng dài thướt tha caftan"},
  {"id": "lex.en.200k.063680", "hw": "camelias", "pos": "noun", "ipa": "/kəˈmiːliəz/", "vi": "cây hoa trà mi cánh dày (biến thể)"},
  {"id": "lex.en.200k.063681", "hw": "carrousels", "pos": "noun", "ipa": "/ˌkærəˈsɛlz/", "vi": "băng chuyền hành lý; vòng quay ngựa"},
  {"id": "lex.en.200k.063682", "hw": "chemotaxises", "pos": "noun", "ipa": "/ˌkiːmoʊˈtæksɪsɪz/", "vi": "hiện tượng hóa hướng động tế bào"},
  {"id": "lex.en.200k.063683", "hw": "chlorhexidines", "pos": "noun", "ipa": "/klɔːrˈhɛksədiːnz/", "vi": "dung dịch sát khuẩn chlorhexidine"},
  {"id": "lex.en.200k.063684", "hw": "chromophores", "pos": "noun", "ipa": "/ˈkroʊməfɔːrz/", "vi": "nhóm mang màu sắc trong phân tử"},
  {"id": "lex.en.200k.063685", "hw": "climes", "pos": "noun", "ipa": "/klaɪmz/", "vi": "vùng khí hậu; miền đất thời tiết"},
  {"id": "lex.en.200k.063686", "hw": "cocoanuts", "pos": "noun", "ipa": "/ˈkoʊkənʌts/", "vi": "quả dừa; cây dừa (cách viết cũ)"},
  {"id": "lex.en.200k.063687", "hw": "condyles", "pos": "noun", "ipa": "/ˈkɑːndaɪlz/", "vi": "lồi cầu đầu tròn khớp nối xương"},
  {"id": "lex.en.200k.063688", "hw": "crapshoots", "pos": "noun", "ipa": "/ˈkræpʃuːts/", "vi": "ván cược may rủi; trò chơi súc sắc"},
  {"id": "lex.en.200k.063689", "hw": "crosscuts", "pos": "noun", "ipa": "/ˈkrɔːskʌts/", "vi": "đường cắt ngang; đường hầm nối vỉa"},
  {"id": "lex.en.200k.063690", "hw": "crosscutting", "pos": "verb", "ipa": "/ˈkrɔːskʌtɪŋ/", "vi": "đang cắt ngang thớ gỗ; chuyển cảnh"},
  {"id": "lex.en.200k.063691", "hw": "croutons", "pos": "noun", "ipa": "/ˈkruːtɑːnz/", "vi": "mẫu bánh mì nướng giòn rắc súp"},
  {"id": "lex.en.200k.063692", "hw": "delphinia", "pos": "noun", "ipa": "/dɛlˈfɪniə/", "vi": "các cây hoa phi yến thảo mọc chùm"},
  {"id": "lex.en.200k.063693", "hw": "delphiniums", "pos": "noun", "ipa": "/dɛlˈfɪniəmz/", "vi": "cây hoa phi yến thảo chùm xanh tím"},
  {"id": "lex.en.200k.063694", "hw": "dewberries", "pos": "noun", "ipa": "/ˈduːˌbɛriz/", "vi": "quả mâm xôi dây bò dại vị ngọt"},
  {"id": "lex.en.200k.063695", "hw": "disorients", "pos": "verb", "ipa": "/dɪsˈɔːriənts/", "vi": "làm mất phương hướng; gây bối rối"},
  {"id": "lex.en.200k.063696", "hw": "distensions", "pos": "noun", "ipa": "/dɪˈstɛnʃənz/", "vi": "tình trạng căng phồng giãn trướng"},
  {"id": "lex.en.200k.063697", "hw": "dramatisations", "pos": "noun", "ipa": "/ˌdræmətaɪˈzeɪʃənz/", "vi": "sự chuyển thể kịch hóa tiểu thuyết"},
  {"id": "lex.en.200k.063698", "hw": "drumheads", "pos": "noun", "ipa": "/ˈdrʌmhɛdz/", "vi": "mặt trống da căng; phần đỉnh trống"},
  {"id": "lex.en.200k.063699", "hw": "duplicators", "pos": "noun", "ipa": "/ˈduːplɪˌkeɪtərz/", "vi": "máy in sao chép nhanh văn bản"},
  {"id": "lex.en.200k.063700", "hw": "egotists", "pos": "noun", "ipa": "/ˈiːɡətɪsts/", "vi": "kẻ ích kỷ tự cao chỉ biết bản thân"},
  {"id": "lex.en.200k.063701", "hw": "eightieths", "pos": "noun", "ipa": "/ˈeɪtiəθs/", "vi": "phần thứ tám mươi; vị trí thứ 80"},
  {"id": "lex.en.200k.063702", "hw": "electronegativities", "pos": "noun", "ipa": "/ɪˌlɛktroʊˌnɛɡəˈtɪvətiz/", "vi": "độ âm điện hút electron nguyên tử"}
]

with open('scratch/b33_r08_raw_p2.json') as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"Mismatch id at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"Mismatch hw at {i}: {item['hw']} vs {r['hw']}"
    assert len(item['vi']) <= 35, f"vi length > 35 at {i} ({item['hw']}): {len(item['vi'])}"
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {item['pos']}"
    assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Invalid ipa at {i}: {item['ipa']}"
    assert not item['ipa'][1:-1].startswith(' ') and not item['ipa'][1:-1].endswith(' '), f"Space in ipa at {i}: {item['ipa']}"
    r['pos'] = item['pos']
    r['ipa'] = item['ipa']
    r['vi'] = item['vi']
    r['status'] = 'reviewed'

with open('scratch/b33_r08_p2.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r08_p2.json OK")
