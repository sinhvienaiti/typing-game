import json

items = [
  {"id": "lex.en.200k.061703", "hw": "ptarmigans", "pos": "noun", "ipa": "/ˈtɑːrmɪɡənz/", "vi": "loài gà gô tuyết vùng cực bắc"},
  {"id": "lex.en.200k.061704", "hw": "pugins", "pos": "noun", "ipa": "/ˈpjuːdʒɪnz/", "vi": "kiến trúc sư Gothic Augustus Pugin"},
  {"id": "lex.en.200k.061705", "hw": "quantifiers", "pos": "noun", "ipa": "/ˈkwɑːntɪfaɪərz/", "vi": "lượng từ ngữ pháp; ký hiệu lượng từ"},
  {"id": "lex.en.200k.061706", "hw": "reiterations", "pos": "noun", "ipa": "/riːˌɪtəˈreɪʃənz/", "vi": "sự lặp lại nhấn mạnh; lời nhắc lại"},
  {"id": "lex.en.200k.061707", "hw": "saturnalias", "pos": "noun", "ipa": "/ˌsætərˈneɪliəz/", "vi": "lễ hội phóng túng Saturnalia La Mã"},
  {"id": "lex.en.200k.061708", "hw": "scallions", "pos": "noun", "ipa": "/ˈskæljənz/", "vi": "cây hành lá; hành hoa tươi xanh"},
  {"id": "lex.en.200k.061709", "hw": "senes", "pos": "noun", "ipa": "/seɪnz/", "vi": "đồng xu lẻ sen Nhật Bản (1/100 yên)"},
  {"id": "lex.en.200k.061710", "hw": "sixers", "pos": "noun", "ipa": "/ˈsɪksərz/", "vi": "số sáu; cú đánh 6 điểm môn cricket"},
  {"id": "lex.en.200k.061711", "hw": "southwestwards", "pos": "noun", "ipa": "/ˌsaʊθˈwɛstwərdz/", "vi": "hướng tây nam; vùng phía tây nam"},
  {"id": "lex.en.200k.061712", "hw": "sprues", "pos": "noun", "ipa": "/spruːz/", "vi": "bệnh đường ruột sprue; cuống đúc"},
  {"id": "lex.en.200k.061713", "hw": "stakeouts", "pos": "noun", "ipa": "/ˈsteɪkaʊts/", "vi": "cuộc mai phục theo dõi mật thám"},
  {"id": "lex.en.200k.061714", "hw": "steffenses", "pos": "noun", "ipa": "/ˈstɛfənzɪz/", "vi": "nhà báo điều tra Lincoln Steffens"},
  {"id": "lex.en.200k.061715", "hw": "striplings", "pos": "noun", "ipa": "/ˈstrɪplɪŋz/", "vi": "chàng thiếu niên mới lớn"},
  {"id": "lex.en.200k.061716", "hw": "suborders", "pos": "noun", "ipa": "/ˈsʌbˌɔːrdərz/", "vi": "bậc phân loại sinh học phân bộ"},
  {"id": "lex.en.200k.061717", "hw": "svengalis", "pos": "noun", "ipa": "/svɛnˈɡɑːliz/", "vi": "kẻ thao túng kiểm soát tâm lý ngầm"},
  {"id": "lex.en.200k.061718", "hw": "talkier", "pos": "adj", "ipa": "/ˈtɔːkiər/", "vi": "lắm lời nói nhiều hơn; dài dòng hơn"},
  {"id": "lex.en.200k.061719", "hw": "talkiest", "pos": "adj", "ipa": "/ˈtɔːkiɪst/", "vi": "lắm lời ba hoa nhất; dài dòng nhất"},
  {"id": "lex.en.200k.061720", "hw": "thalli", "pos": "noun", "ipa": "/ˈθælaɪ/", "vi": "cơ thể dạng tản của tảo và địa y"},
  {"id": "lex.en.200k.061721", "hw": "thalluses", "pos": "noun", "ipa": "/ˈθæləsɪz/", "vi": "các tán tản của thực vật bậc thấp"},
  {"id": "lex.en.200k.061722", "hw": "thoracotomies", "pos": "noun", "ipa": "/ˌθɔːrəˈkɑːtəmiz/", "vi": "phẫu thuật mở khoang lồng ngực"},
  {"id": "lex.en.200k.061723", "hw": "transcribers", "pos": "noun", "ipa": "/trænˈskraɪbərz/", "vi": "người chép lời thoại; máy chép băng"},
  {"id": "lex.en.200k.061724", "hw": "trfs", "pos": "noun", "ipa": "/tiː ɑːr ɛfs/", "vi": "hoóc-môn giải phóng hướng giáp TRH"},
  {"id": "lex.en.200k.061725", "hw": "trivialities", "pos": "noun", "ipa": "/ˌtrɪviˈælətiz/", "vi": "chuyện vụn vặt; điều tầm phào vặt"},
  {"id": "lex.en.200k.061726", "hw": "upsilons", "pos": "noun", "ipa": "/ˈjuːpsɪlɑːnz/", "vi": "chữ cái Hy Lạp Upsilon thứ 20"},
  {"id": "lex.en.200k.061727", "hw": "valines", "pos": "noun", "ipa": "/ˈveɪliːnz/", "vi": "axit amin thiết yếu valin protein"},
  {"id": "lex.en.200k.061728", "hw": "wallensteins", "pos": "noun", "ipa": "/ˈwɑːlənstaɪnz/", "vi": "danh tướng Đức Wallenstein"},
  {"id": "lex.en.200k.061729", "hw": "wingbacks", "pos": "noun", "ipa": "/ˈwɪŋbæks/", "vi": "hậu vệ biên dâng cao; ghế tựa bành"},
  {"id": "lex.en.200k.061730", "hw": "yalus", "pos": "noun", "ipa": "/ˈjɑːluz/", "vi": "sông Áp Lục biên giới Trung-Triều"},
  {"id": "lex.en.200k.061731", "hw": "yukawas", "pos": "noun", "ipa": "/juːˈkɑːwəz/", "vi": "nhà vật lý Nhật Hideki Yukawa"},
  {"id": "lex.en.200k.061732", "hw": "zends", "pos": "noun", "ipa": "/zɛndz/", "vi": "ngôn ngữ cổ điển kinh Zend Avesta"},
  {"id": "lex.en.200k.061733", "hw": "zloties", "pos": "noun", "ipa": "/ˈzlɔːtiz/", "vi": "đồng tiền tệ zloty của Ba Lan"},
  {"id": "lex.en.200k.061734", "hw": "adelie coast", "pos": "phrase", "ipa": "/ˈɑːdəli koʊst/", "vi": "bờ biển Adélie thuộc châu Nam Cực"},
  {"id": "lex.en.200k.061735", "hw": "adelie land", "pos": "phrase", "ipa": "/ˈɑːdəli lænd/", "vi": "lãnh thổ vùng đất Adélie Nam Cực"},
  {"id": "lex.en.200k.061736", "hw": "adelie penguin", "pos": "phrase", "ipa": "/ˈɑːdəli ˈpɛŋɡwɪn/", "vi": "chim cánh cụt Adélie vòng mắt trắng"},
  {"id": "lex.en.200k.061737", "hw": "anatoli karpov", "pos": "phrase", "ipa": "/ˌænəˈtoʊli ˈkɑːrpɔːf/", "vi": "vua cờ vua thế giới Anatoly Karpov"},
  {"id": "lex.en.200k.061738", "hw": "barbara wertheim tuchman", "pos": "phrase", "ipa": "/ˈbɑːrbərə ˈwɜːrθaɪm ˈtʌkmən/", "vi": "nữ sử gia Pulitzer Barbara Tuchman"},
  {"id": "lex.en.200k.061739", "hw": "battle of issus", "pos": "phrase", "ipa": "/ˈbætl əv ˈɪsəs/", "vi": "trận chiến Issus thời Alexander"},
  {"id": "lex.en.200k.061740", "hw": "battle of naseby", "pos": "phrase", "ipa": "/ˈbætl əv ˈneɪzbi/", "vi": "trận chiến Naseby Nội chiến Anh"},
  {"id": "lex.en.200k.061741", "hw": "beefsteak begonia", "pos": "phrase", "ipa": "/ˈbiːfsteɪk bɪˈɡoʊniə/", "vi": "thu hải đường lá tròn mặt dưới đỏ"},
  {"id": "lex.en.200k.061742", "hw": "blackbody radiation", "pos": "phrase", "ipa": "/ˌblækˈbɑːdi ˌreɪdiˈeɪʃən/", "vi": "bức xạ điện từ vật đen tuyệt đối"},
  {"id": "lex.en.200k.061743", "hw": "calendula officinalis", "pos": "phrase", "ipa": "/kəˈlɛndjʊlə əˌfɪsɪˈneɪlɪs/", "vi": "cây hoa cúc xu xi dược liệu vàng"},
  {"id": "lex.en.200k.061744", "hw": "canine chorea", "pos": "phrase", "ipa": "/ˈkeɪnaɪn kɔːˈriːə/", "vi": "chứng co giật cơ bắp ở loài chó"},
  {"id": "lex.en.200k.061745", "hw": "chenopodium album", "pos": "phrase", "ipa": "/ˌkiːnoʊˈpoʊdiəm ˈælbəm/", "vi": "cây rau muối trắng chân ngỗng"},
  {"id": "lex.en.200k.061746", "hw": "chromic acid", "pos": "phrase", "ipa": "/ˈkroʊmɪk ˈæsɪd/", "vi": "axit cromic oxy hóa mạnh mạ điện"},
  {"id": "lex.en.200k.061747", "hw": "colobus monkey", "pos": "phrase", "ipa": "/ˈkɑːləbəs ˈmʌŋki/", "vi": "loài khỉ lông đen trắng colobus Phi"},
  {"id": "lex.en.200k.061748", "hw": "conjunctival veins", "pos": "phrase", "ipa": "/ˌkɑːndʒʌŋkˈtaɪvl veɪnz/", "vi": "tĩnh mạch màng kết mạc nhãn cầu mắt"},
  {"id": "lex.en.200k.061749", "hw": "doberman pinscher", "pos": "phrase", "ipa": "/ˈdoʊbərmən ˈpɪnʃər/", "vi": "giống chó nghiệp vụ Doberman Đức"},
  {"id": "lex.en.200k.061750", "hw": "electromotive drug administration", "pos": "phrase", "ipa": "/ɪˌlɛktroʊˈmoʊtɪv drʌɡ ədˌmɪnɪˈstreɪʃən/", "vi": "dẫn truyền thuốc bằng dòng điện di"},
  {"id": "lex.en.200k.061751", "hw": "electromotive force", "pos": "phrase", "ipa": "/ɪˌlɛktroʊˈmoʊtɪv fɔːrs/", "vi": "suất điện động nguồn điện vật lý"},
  {"id": "lex.en.200k.061752", "hw": "electromotive force series", "pos": "phrase", "ipa": "/ɪˌlɛktroʊˈmoʊtɪv fɔːrs ˈsɪriːz/", "vi": "dãy thế điện cực chuẩn kim loại"},
  {"id": "lex.en.200k.061753", "hw": "electromotive series", "pos": "phrase", "ipa": "/ɪˌlɛktroʊˈmoʊtɪv ˈsɪriːz/", "vi": "dãy điện hóa sắp xếp kim loại"},
  {"id": "lex.en.200k.061754", "hw": "epigastric vein", "pos": "phrase", "ipa": "/ˌɛpɪˈɡæstrɪk veɪn/", "vi": "tĩnh mạch thượng vị thành bụng"},
  {"id": "lex.en.200k.061755", "hw": "eucalyptus maculata", "pos": "phrase", "ipa": "/ˌjuːkəˈlɪptəs ˌmækjʊˈleɪtə/", "vi": "cây bạch đàn vỏ đốm vằn nước Úc"},
  {"id": "lex.en.200k.061756", "hw": "family asteraceae", "pos": "phrase", "ipa": "/ˈfæməli ˌæstəˈreɪsiː/", "vi": "họ thực vật hoa Cúc lớn nhất"},
  {"id": "lex.en.200k.061757", "hw": "genus alnus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈælnəs/", "vi": "chi thực vật cây tống quán sủ"},
  {"id": "lex.en.200k.061758", "hw": "genus avena", "pos": "phrase", "ipa": "/ˈdʒiːnəs əˈviːnə/", "vi": "chi thực vật ngũ cốc yến mạch Avena"},
  {"id": "lex.en.200k.061759", "hw": "genus chenopodium", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌkiːnoʊˈpoʊdiəm/", "vi": "chi cây rau muối dại chân ngỗng"},
  {"id": "lex.en.200k.061760", "hw": "genus colobus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈkɑːləbəs/", "vi": "chi khỉ không ngón cái Colobus Phi"},
  {"id": "lex.en.200k.061761", "hw": "genus dianthus", "pos": "phrase", "ipa": "/ˈdʒiːnəs daɪˈænθəs/", "vi": "chi thực vật hoa cẩm chướng thơm"},
  {"id": "lex.en.200k.061762", "hw": "genus fagus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈfeɪɡəs/", "vi": "chi cây gỗ dẻ gai ôn đới Fagus"},
  {"id": "lex.en.200k.061763", "hw": "genus laburnum", "pos": "phrase", "ipa": "/ˈdʒiːnəs ləˈbɜːrnəm/", "vi": "chi cây muồng hoa vàng rũ Laburnum"},
  {"id": "lex.en.200k.061764", "hw": "genus larus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈlɛərəs/", "vi": "chi chim mòng biển cỡ lớn Larus"},
  {"id": "lex.en.200k.061765", "hw": "genus olea", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈoʊliə/", "vi": "chi thực vật cây ô liu lấy dầu"},
  {"id": "lex.en.200k.061766", "hw": "genus pyrus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈpaɪrəs/", "vi": "chi thực vật cây lê ăn quả Pyrus"},
  {"id": "lex.en.200k.061767", "hw": "genus sargassum", "pos": "phrase", "ipa": "/ˈdʒiːnəs sɑːrˈɡæsəm/", "vi": "chi tảo nâu rong mơ biển Sargassum"},
  {"id": "lex.en.200k.061768", "hw": "genus silene", "pos": "phrase", "ipa": "/ˈdʒiːnəs saɪˈliːniː/", "vi": "chi cây hoa cẩm nhung Silene"},
  {"id": "lex.en.200k.061769", "hw": "genus vicia", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈvɪʃə/", "vi": "chi thực vật dây đậu tằm họ Đậu"},
  {"id": "lex.en.200k.061770", "hw": "george bryan brummell", "pos": "phrase", "ipa": "/dʒɔːrdʒ ˈbraɪən ˈbrʌml/", "vi": "quý ông thời trang Beau Brummell"},
  {"id": "lex.en.200k.061771", "hw": "gluteus minimus", "pos": "phrase", "ipa": "/ˈɡluːtiəs ˈmɪnəməs/", "vi": "cơ mông bé lớp sâu nhất vùng hông"},
  {"id": "lex.en.200k.061772", "hw": "gunnar myrdal", "pos": "phrase", "ipa": "/ˈɡʊnɑːr ˈmɪərdɑːl/", "vi": "nhà kinh tế Nobel Gunnar Myrdal"},
  {"id": "lex.en.200k.061773", "hw": "harold urey", "pos": "phrase", "ipa": "/ˈhɛrəld ˈjʊəri/", "vi": "nhà hóa học Nobel Harold Urey"},
  {"id": "lex.en.200k.061774", "hw": "human chorionic gonadotropin", "pos": "phrase", "ipa": "/ˈhjuːmən ˌkɔːriˈɑːnɪk ɡoʊˌnædəˈtroʊpɪn/", "vi": "hoóc-môn thai kỳ hCG thử thai"},
  {"id": "lex.en.200k.061775", "hw": "immunizing agent", "pos": "phrase", "ipa": "/ˈɪmjʊnaɪzɪŋ ˈeɪdʒənt/", "vi": "chế phẩm tạo miễn dịch; vắc-xin"},
  {"id": "lex.en.200k.061776", "hw": "jean francois champollion", "pos": "phrase", "ipa": "/ʒɑ̃ː frɑ̃ːˈswɑː ʃɑ̃ːpɔlˈjɔ̃ː/", "vi": "nhà giải mã chữ Ai Cập Champollion"},
  {"id": "lex.en.200k.061777", "hw": "karl wilhelm scheele", "pos": "phrase", "ipa": "/kɑːrl ˈvɪlhɛlm ˈʃeɪlə/", "vi": "nhà hóa học phát hiện oxy Scheele"},
  {"id": "lex.en.200k.061778", "hw": "lota lota", "pos": "phrase", "ipa": "/ˈloʊtə ˈloʊtə/", "vi": "loài cá tuyết nước ngọt châu Âu"},
  {"id": "lex.en.200k.061779", "hw": "mare liberum", "pos": "phrase", "ipa": "/ˈmɛəri ˈlɪbərəm/", "vi": "luận thuyết Biển Tự Do hàng hải"},
  {"id": "lex.en.200k.061780", "hw": "mimeograph machine", "pos": "phrase", "ipa": "/ˈmɪmioʊɡræf məˈʃiːn/", "vi": "máy in quay tay giấy nến rônêô"},
  {"id": "lex.en.200k.061781", "hw": "mutual exclusiveness", "pos": "phrase", "ipa": "/ˈmjuːtʃuəl ɪkˈskluːsɪvnəs/", "vi": "tính xung khắc loại trừ lẫn nhau"},
  {"id": "lex.en.200k.061782", "hw": "nemean games", "pos": "phrase", "ipa": "/nɪˈmiːən ɡeɪmz/", "vi": "Đại hội thể thao cổ đại Nemea"},
  {"id": "lex.en.200k.061783", "hw": "nemean lion", "pos": "phrase", "ipa": "/nɪˈmiːən ˈlaɪən/", "vi": "con sư tử da bất hoại vùng Nemea"},
  {"id": "lex.en.200k.061784", "hw": "neroli oil", "pos": "phrase", "ipa": "/ˈnɛrəli ɔɪl/", "vi": "tinh dầu hoa cam đắng thơm Neroli"},
  {"id": "lex.en.200k.061785", "hw": "nucleolus organiser", "pos": "phrase", "ipa": "/nuːˈkliːələs ˈɔːrɡənaɪzər/", "vi": "vùng tổ chức hạch nhân (tế bào)"},
  {"id": "lex.en.200k.061786", "hw": "os trapezium", "pos": "phrase", "ipa": "/ɑːs trəˈpiːziəm/", "vi": "xương thang cổ tay dưới ngón cái"},
  {"id": "lex.en.200k.061787", "hw": "pes planus", "pos": "phrase", "ipa": "/pɛs ˈpleɪnəs/", "vi": "tật bàn chân bẹt mất vòm cong"},
  {"id": "lex.en.200k.061788", "hw": "picea orientalis", "pos": "phrase", "ipa": "/ˈpaɪsiə ˌɔːriɛnˈteɪlɪs/", "vi": "cây vân sam phương Đông Kavkaz"},
  {"id": "lex.en.200k.061789", "hw": "plimsoll line", "pos": "phrase", "ipa": "/ˈplɪmsɑːl laɪn/", "vi": "vạch dấu mớn nước an toàn thân tàu"},
  {"id": "lex.en.200k.061790", "hw": "plimsoll mark", "pos": "phrase", "ipa": "/ˈplɪmsɑːl mɑːrk/", "vi": "vạch dấu tải trọng tối đa thân tàu"},
  {"id": "lex.en.200k.061791", "hw": "prunus maritima", "pos": "phrase", "ipa": "/ˈpruːnəs məˈrɪtɪmə/", "vi": "cây mận bãi biển cồn cát Đại Tây"},
  {"id": "lex.en.200k.061792", "hw": "prunus virginiana", "pos": "phrase", "ipa": "/ˈpruːnəs vərˌdʒɪniˈeɪnə/", "vi": "cây anh đào dại quả chát Virginia"},
  {"id": "lex.en.200k.061793", "hw": "puerperal fever", "pos": "phrase", "ipa": "/pjuːˈɜːrpərəl ˈfiːvər/", "vi": "bệnh sốt nhiễm trùng hậu sản"},
  {"id": "lex.en.200k.061794", "hw": "ready reckoner", "pos": "phrase", "ipa": "/ˈrɛdi ˈrɛkənər/", "vi": "sổ bảng tính sẵn hỗ trợ tính nhẩm"},
  {"id": "lex.en.200k.061795", "hw": "recessional march", "pos": "phrase", "ipa": "/rɪˈsɛʃənl mɑːrtʃ/", "vi": "khúc hành khúc rước lễ bế mạc"},
  {"id": "lex.en.200k.061796", "hw": "ringgold wilmer lardner", "pos": "phrase", "ipa": "/ˈrɪŋɡoʊld ˈwɪlmər ˈlɑːrdnər/", "vi": "nhà văn trào phúng Mỹ Ring Lardner"},
  {"id": "lex.en.200k.061797", "hw": "rochon prism", "pos": "phrase", "ipa": "/roʊˈʃɔ̃ː ˈprɪzəm/", "vi": "lăng kính phân cực kép Rochon"},
  {"id": "lex.en.200k.061798", "hw": "salic law", "pos": "phrase", "ipa": "/ˈsælɪk lɔː/", "vi": "đạo luật Salic cấm nữ kế vị ngai"},
  {"id": "lex.en.200k.061799", "hw": "sargassum fish", "pos": "phrase", "ipa": "/sɑːrˈɡæsəm fɪʃ/", "vi": "cá ngụy trang tảo mơ sargassum"},
  {"id": "lex.en.200k.061800", "hw": "scotch laburnum", "pos": "phrase", "ipa": "/skɑːtʃ ləˈbɜːrnəm/", "vi": "cây kim tước hoa vàng Scotland"},
  {"id": "lex.en.200k.061801", "hw": "sea of marmora", "pos": "phrase", "ipa": "/siː əv ˈmɑːrmərə/", "vi": "biển nội địa Marmara Thổ Nhĩ Kỳ"},
  {"id": "lex.en.200k.061802", "hw": "sunray pleat", "pos": "phrase", "ipa": "/ˈsʌnreɪ pliːt/", "vi": "đường xếp ly váy xòe hình nan quạt"}
]

with open('scratch/b33_r04_raw_p3.json') as f:
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

with open('scratch/b33_r04_p3.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 4 Part 3 validated and written successfully.")
