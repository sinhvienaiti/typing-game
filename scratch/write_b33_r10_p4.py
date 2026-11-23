import json

items = [
  {"id": "lex.en.200k.064803", "hw": "okens", "pos": "noun", "ipa": "/ˈoʊkənz/", "vi": "nhà tự nhiên học Đức Lorenz Oken"},
  {"id": "lex.en.200k.064804", "hw": "overspills", "pos": "noun", "ipa": "/ˈoʊvərˌspɪlz/", "vi": "lượng nước tràn; dân số giãn tràn"},
  {"id": "lex.en.200k.064805", "hw": "overspilt", "pos": "verb", "ipa": "/ˌoʊvərˈspɪlt/", "vi": "đã tràn qua bờ; đã di dời dư thừa"},
  {"id": "lex.en.200k.064806", "hw": "overtoped", "pos": "verb", "ipa": "/ˌoʊvərˈtɑːpt/", "vi": "đã vượt cao hơn đỉnh; đã che khuất"},
  {"id": "lex.en.200k.064807", "hw": "overtoping", "pos": "verb", "ipa": "/ˌoʊvərˈtɑːpɪŋ/", "vi": "đang vươn cao hơn hẳn (cách cũ)"},
  {"id": "lex.en.200k.064808", "hw": "overtopped", "pos": "verb", "ipa": "/ˌoʊvərˈtɑːpt/", "vi": "đã cao vượt trội hơn; che lấp"},
  {"id": "lex.en.200k.064809", "hw": "overtopping", "pos": "verb", "ipa": "/ˌoʊvərˈtɑːpɪŋ/", "vi": "đang vươn cao vượt hẳn lên trên"},
  {"id": "lex.en.200k.064810", "hw": "overtops", "pos": "verb", "ipa": "/ˌoʊvərˈtɑːps/", "vi": "vượt cao hơn hẳn; nổi trội hơn"},
  {"id": "lex.en.200k.064811", "hw": "panicles", "pos": "noun", "ipa": "/ˈpænəkəlz/", "vi": "cụm hoa hình chùy phân nhánh chùm"},
  {"id": "lex.en.200k.064812", "hw": "panofskies", "pos": "noun", "ipa": "/pɑːˈnɑːfskiz/", "vi": "nhà sử học nghệ thuật Panofsky"},
  {"id": "lex.en.200k.064813", "hw": "paramaribos", "pos": "noun", "ipa": "/ˌpærəˈmærəˌboʊz/", "vi": "thủ đô Paramaribo của Suriname"},
  {"id": "lex.en.200k.064814", "hw": "peepers", "pos": "noun", "ipa": "/ˈpiːpərz/", "vi": "kẻ rình trộm; mắt (lóng); ếch nhỏ"},
  {"id": "lex.en.200k.064815", "hw": "peristalses", "pos": "noun", "ipa": "/ˌpɛrəˈstɔːlsiːz/", "vi": "nhu động co bóp đẩy thức ăn ruột"},
  {"id": "lex.en.200k.064816", "hw": "pilchards", "pos": "noun", "ipa": "/ˈpɪltʃərdz/", "vi": "cá trích cơm mòi lớn đóng hộp"},
  {"id": "lex.en.200k.064817", "hw": "pinons", "pos": "noun", "ipa": "/ˈpɪnjənz/", "vi": "cây thông ăn hạt tây nam Mỹ piñon"},
  {"id": "lex.en.200k.064818", "hw": "plebes", "pos": "noun", "ipa": "/pliːbz/", "vi": "học viên năm nhất học viện quân sự"},
  {"id": "lex.en.200k.064819", "hw": "plfs", "pos": "noun", "ipa": "/ˌpiːˌɛlˈɛfs/", "vi": "Mặt trận Giải phóng Palestine PLF"},
  {"id": "lex.en.200k.064820", "hw": "potentiated", "pos": "verb", "ipa": "/pəˈtɛnʃiˌeɪtɪd/", "vi": "đã tăng cường hiệu lực tác dụng"},
  {"id": "lex.en.200k.064821", "hw": "potentiates", "pos": "verb", "ipa": "/pəˈtɛnʃiˌeɪts/", "vi": "làm tăng mạnh hiệu quả tác dụng"},
  {"id": "lex.en.200k.064822", "hw": "potentiating", "pos": "verb", "ipa": "/pəˈtɛnʃiˌeɪtɪŋ/", "vi": "đang khuếch đại tăng cường tác dụng"},
  {"id": "lex.en.200k.064823", "hw": "poufs", "pos": "noun", "ipa": "/puːfs/", "vi": "ghế đôn bọc nệm; búi tóc phồng"},
  {"id": "lex.en.200k.064824", "hw": "prothrombins", "pos": "noun", "ipa": "/proʊˈθrɑːmbɪnz/", "vi": "tiền chất đông máu prothrombin gan"},
  {"id": "lex.en.200k.064825", "hw": "quaggas", "pos": "noun", "ipa": "/ˈkwɑːɡəz/", "vi": "ngựa vằn nửa thân Nam Phi Quagga"},
  {"id": "lex.en.200k.064826", "hw": "quakerisms", "pos": "noun", "ipa": "/ˈkweɪkəˌrɪzəmz/", "vi": "tôn giáo hòa bình Quaker (Hội Bạn)"},
  {"id": "lex.en.200k.064827", "hw": "recapitulated", "pos": "verb", "ipa": "/ˌriːkəˈpɪtʃəˌleɪtɪd/", "vi": "đã tóm tắt điểm lại ý chính"},
  {"id": "lex.en.200k.064828", "hw": "recapitulates", "pos": "verb", "ipa": "/ˌriːkəˈpɪtʃəˌleɪts/", "vi": "tóm tắt lại; lặp lại quá trình"},
  {"id": "lex.en.200k.064829", "hw": "recapitulating", "pos": "verb", "ipa": "/ˌriːkəˈpɪtʃəˌleɪtɪŋ/", "vi": "đang tóm tắt điểm lại điểm chính"},
  {"id": "lex.en.200k.064830", "hw": "recodings", "pos": "noun", "ipa": "/ˌriːˈkoʊdɪŋz/", "vi": "sự mã hóa chuyển đổi lại dữ liệu"},
  {"id": "lex.en.200k.064831", "hw": "roentgens", "pos": "noun", "ipa": "/ˈrɛntɡənz/", "vi": "đơn vị đo tia X phóng xạ rơnghen"},
  {"id": "lex.en.200k.064832", "hw": "sabertooths", "pos": "noun", "ipa": "/ˈseɪbərˌtuːθs/", "vi": "hổ răng kiếm tiền sử tuyệt chủng"},
  {"id": "lex.en.200k.064833", "hw": "sacristans", "pos": "noun", "ipa": "/ˈsækrəstənz/", "vi": "người coi giữ đồ lễ trong nhà thờ"},
  {"id": "lex.en.200k.064834", "hw": "samovars", "pos": "noun", "ipa": "/ˈsæməvɑːrz/", "vi": "ấm đun nước pha trà Nga samovar"},
  {"id": "lex.en.200k.064835", "hw": "samoyeds", "pos": "noun", "ipa": "/ˌsæməˈjɛdz/", "vi": "chó kéo xe lông trắng; dân Samoyed"},
  {"id": "lex.en.200k.064836", "hw": "servitors", "pos": "noun", "ipa": "/ˈsɜːrvətərz/", "vi": "người hầu cận; trợ lý hầu việc"},
  {"id": "lex.en.200k.064837", "hw": "shaitans", "pos": "noun", "ipa": "/ʃaɪˈtɑːnz/", "vi": "ác quỷ trong truyền thuyết Hồi giáo"},
  {"id": "lex.en.200k.064838", "hw": "sials", "pos": "noun", "ipa": "/ˈsaɪəlz/", "vi": "lớp vỏ lục địa giàu silic nhôm"},
  {"id": "lex.en.200k.064839", "hw": "sinecures", "pos": "noun", "ipa": "/ˈsaɪnəˌkjʊərz/", "vi": "chức vị nhàn hạ hưởng lương cao"},
  {"id": "lex.en.200k.064840", "hw": "slaveholdings", "pos": "noun", "ipa": "/ˈsleɪvˌhoʊldɪŋz/", "vi": "chế độ sở hữu giữ nô lệ thời xưa"},
  {"id": "lex.en.200k.064841", "hw": "soudans", "pos": "noun", "ipa": "/suːˈdænz/", "vi": "quốc gia Sudan (cách viết Pháp cũ)"},
  {"id": "lex.en.200k.064842", "hw": "squeezers", "pos": "noun", "ipa": "/ˈskwiːzərz/", "vi": "dụng cụ ép vắt chanh; kẻ vòi vĩnh"},
  {"id": "lex.en.200k.064843", "hw": "suffragans", "pos": "noun", "ipa": "/ˈsʌfrəɡənz/", "vi": "giám mục phụ tá dưới tổng giám mục"},
  {"id": "lex.en.200k.064844", "hw": "thumbtacks", "pos": "noun", "ipa": "/ˈθʌmtæks/", "vi": "đinh ghim bấm đầu dẹt gắn bảng"},
  {"id": "lex.en.200k.064845", "hw": "toreadors", "pos": "noun", "ipa": "/ˈtɔːriəˌdɔːrz/", "vi": "võ sĩ đấu bò tót chuyên nghiệp"},
  {"id": "lex.en.200k.064846", "hw": "ulmuses", "pos": "noun", "ipa": "/ˈʌlməsɪz/", "vi": "chi cây du thân gỗ ôn đới Ulmus"},
  {"id": "lex.en.200k.064847", "hw": "vayus", "pos": "noun", "ipa": "/ˈvɑːjuːz/", "vi": "thần gió Vayu trong Ấn Độ giáo"},
  {"id": "lex.en.200k.064848", "hw": "virchows", "pos": "noun", "ipa": "/ˈfɪrxoʊz/", "vi": "bác sĩ bệnh lý học Đức Virchow"},
  {"id": "lex.en.200k.064849", "hw": "vizslas", "pos": "noun", "ipa": "/ˈviːʒləz/", "vi": "chó săn lông vàng Hungary Vizsla"},
  {"id": "lex.en.200k.064850", "hw": "vocatives", "pos": "noun", "ipa": "/ˈvɑːkətɪvz/", "vi": "cách hô ngữ gọi tên trong ngữ pháp"},
  {"id": "lex.en.200k.064851", "hw": "wisters", "pos": "noun", "ipa": "/ˈwɪstərz/", "vi": "nhà văn tiểu thuyết cao bồi Wister"},
  {"id": "lex.en.200k.064852", "hw": "wycherleys", "pos": "noun", "ipa": "/ˈwɪtʃərliz/", "vi": "nhà soạn hài kịch Anh Wycherley"},
  {"id": "lex.en.200k.064853", "hw": "battle of plataea", "pos": "phrase", "ipa": "/ˈbætəl əv pləˈtiːə/", "vi": "trận Plataea năm 479 TCN Hy-Ba Tư"},
  {"id": "lex.en.200k.064854", "hw": "bezoar goat", "pos": "phrase", "ipa": "/ˈbiːzɔːr ɡoʊt/", "vi": "dê rừng sừng dài Trung Đông Ba Tư"},
  {"id": "lex.en.200k.064855", "hw": "bufo boreas", "pos": "phrase", "ipa": "/ˈbjuːfoʊ ˈbɔːriəs/", "vi": "cóc phương Tây vằn lưng trắng Mỹ"},
  {"id": "lex.en.200k.064856", "hw": "burgeon forth", "pos": "phrase", "ipa": "/ˈbɜːrdʒən fɔːrθ/", "vi": "đâm chồi nảy lộc phát triển nhanh"},
  {"id": "lex.en.200k.064857", "hw": "canopic vase", "pos": "phrase", "ipa": "/kəˈnoʊpɪk veɪs/", "vi": "bình gốm Ai Cập đựng tạng ướp xác"},
  {"id": "lex.en.200k.064858", "hw": "cinnabar chanterelle", "pos": "phrase", "ipa": "/ˈsɪnəbɑːr ˌʃæntəˈrɛl/", "vi": "nấm chanterelle màu đỏ cam ăn được"},
  {"id": "lex.en.200k.064859", "hw": "cochon de lait", "pos": "phrase", "ipa": "/koʊˈʃɔːn də ˈlɛ/", "vi": "món thịt heo sữa quay nguyên con"},
  {"id": "lex.en.200k.064860", "hw": "condole with", "pos": "phrase", "ipa": "/kənˈdoʊl wɪð/", "vi": "chia buồn sâu sắc đồng cảm cùng ai"},
  {"id": "lex.en.200k.064861", "hw": "congress gaiter", "pos": "phrase", "ipa": "/ˈkɑːŋɡrəs ˈɡeɪtər/", "vi": "giày bốt cổ cao chun đàn hồi hông"},
  {"id": "lex.en.200k.064862", "hw": "cristoforo colombo", "pos": "phrase", "ipa": "/krɪˈstɔːfəroʊ kəˈlɔːmboʊ/", "vi": "nhà thám hiểm Christopher Columbus"},
  {"id": "lex.en.200k.064863", "hw": "cyperus papyrus", "pos": "phrase", "ipa": "/saɪˈpɪrəs pəˈpaɪrəs/", "vi": "cây cói giấy làm giấy cổ Ai Cập"},
  {"id": "lex.en.200k.064864", "hw": "falco peregrinus", "pos": "phrase", "ipa": "/ˈfælkoʊ ˌpɛrəˈɡraɪnəs/", "vi": "loài chim cắt lớn tốc độ cực nhanh"},
  {"id": "lex.en.200k.064865", "hw": "flexible sigmoidoscopy", "pos": "phrase", "ipa": "/ˈflɛksəbəl ˌsɪɡmɔɪˈdɑːskəpi/", "vi": "nội soi ống mềm đại tràng sigma"},
  {"id": "lex.en.200k.064866", "hw": "genus asclepias", "pos": "phrase", "ipa": "/ˈdʒiːnəs əˈskliːpiəs/", "vi": "chi cây bông tai nuôi bướm chúa"},
  {"id": "lex.en.200k.064867", "hw": "genus azolla", "pos": "phrase", "ipa": "/ˈdʒiːnəs əˈzoʊlə/", "vi": "chi bèo hoa dâu cố định đạm ruộng"},
  {"id": "lex.en.200k.064868", "hw": "genus bauhinia", "pos": "phrase", "ipa": "/ˈdʒiːnəs boʊˈhɪniə/", "vi": "chi cây hoa ban móng bò Bauhinia"},
  {"id": "lex.en.200k.064869", "hw": "genus chloris", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈklɔːrɪs/", "vi": "chi cỏ lông bông ngón tay Chloris"},
  {"id": "lex.en.200k.064870", "hw": "genus dracaena", "pos": "phrase", "ipa": "/ˈdʒiːnəs drəˈsiːnə/", "vi": "chi cây huyết dụ phát tài Dracaena"},
  {"id": "lex.en.200k.064871", "hw": "genus equisetum", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌɛkwəˈsiːtəm/", "vi": "chi thực vật cỏ tháp bút Equisetum"},
  {"id": "lex.en.200k.064872", "hw": "genus lepas", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈliːpəs/", "vi": "chi hà biển có cuống bám tàu Lepas"},
  {"id": "lex.en.200k.064873", "hw": "genus phaethon", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈfeɪəθɑːn/", "vi": "chi chim biển đuôi dài Phaethon"},
  {"id": "lex.en.200k.064874", "hw": "genus sciara", "pos": "phrase", "ipa": "/ˈdʒiːnəs saɪˈɛrə/", "vi": "chi ruồi nấm nhỏ cánh đen Sciara"},
  {"id": "lex.en.200k.064875", "hw": "genus syringa", "pos": "phrase", "ipa": "/ˈdʒiːnəs səˈrɪŋɡə/", "vi": "chi hoa tử đinh hương thơm Syringa"},
  {"id": "lex.en.200k.064876", "hw": "guibert of ravenna", "pos": "phrase", "ipa": "/ˈɡiːbɛər əv rəˈvɛnə/", "vi": "Giáo hoàng đối lập Clement III"},
  {"id": "lex.en.200k.064877", "hw": "james butler hickock", "pos": "phrase", "ipa": "/dʒeɪmz ˈbʌtlər ˈhɪkɑːk/", "vi": "xạ thủ miền Tây Wild Bill Hickok"},
  {"id": "lex.en.200k.064878", "hw": "jean honore fragonard", "pos": "phrase", "ipa": "/ʒɑːn ɔːnɔːˈreɪ frɑːɡɔːˈnɑːr/", "vi": "danh họa Rococo Pháp Fragonard"},
  {"id": "lex.en.200k.064879", "hw": "john van vleck", "pos": "phrase", "ipa": "/dʒɑːn væn vlɛk/", "vi": "nhà vật lý từ học Nobel Van Vleck"},
  {"id": "lex.en.200k.064880", "hw": "jugal bone", "pos": "phrase", "ipa": "/ˈdʒuːɡəl boʊn/", "vi": "xương gò má dưới mắt (giải phẫu)"},
  {"id": "lex.en.200k.064881", "hw": "jugal point", "pos": "phrase", "ipa": "/ˈdʒuːɡəl pɔɪnt/", "vi": "điểm gò má trong đo sọ nhân trắc"},
  {"id": "lex.en.200k.064882", "hw": "metabolic alkalosis", "pos": "phrase", "ipa": "/ˌmɛtəˈbɑːlɪk ˌælkəˈloʊsɪs/", "vi": "tình trạng nhiễm kiềm chuyển hóa"},
  {"id": "lex.en.200k.064883", "hw": "mola lanceolata", "pos": "phrase", "ipa": "/ˈmoʊlə ˌlænsiəˈleɪtə/", "vi": "cá mặt trăng đuôi nhọn biển sâu"},
  {"id": "lex.en.200k.064884", "hw": "mount orizaba", "pos": "phrase", "ipa": "/maʊnt ˌɔːrɪˈzɑːbə/", "vi": "núi lửa cao nhất Mexico Orizaba"},
  {"id": "lex.en.200k.064885", "hw": "mt orizaba", "pos": "phrase", "ipa": "/maʊnt ˌɔːrɪˈzɑːbə/", "vi": "đỉnh núi lửa Pico de Orizaba Mexico"},
  {"id": "lex.en.200k.064886", "hw": "musculus teres major", "pos": "phrase", "ipa": "/ˈmʌskjʊləs ˈtɪriːz ˈmeɪdʒər/", "vi": "cơ tròn lớn xoay khép khớp vai"},
  {"id": "lex.en.200k.064887", "hw": "musculus teres minor", "pos": "phrase", "ipa": "/ˈmʌskjʊləs ˈtɪriːz ˈmaɪnər/", "vi": "cơ tròn bé giữ ổn định khớp vai"},
  {"id": "lex.en.200k.064888", "hw": "negeri sembilan", "pos": "phrase", "ipa": "/nəˈɡɛri sɛmˈbiːlən/", "vi": "bang Negeri Sembilan ở Malaysia"},
  {"id": "lex.en.200k.064889", "hw": "obiter dictum", "pos": "phrase", "ipa": "/ˈɑːbɪtər ˈdɪktəm/", "vi": "nhận xét bên lề không ràng buộc án"},
  {"id": "lex.en.200k.064890", "hw": "order cetacea", "pos": "phrase", "ipa": "/ˈɔːrdər sɪˈteɪʃə/", "vi": "bộ động vật biển Cá voi và Cá heo"},
  {"id": "lex.en.200k.064891", "hw": "phanerozoic aeon", "pos": "phrase", "ipa": "/ˌfænərəˈzoʊɪk ˈiːɑːn/", "vi": "liên đại Hiển sinh địa chất (Anh)"},
  {"id": "lex.en.200k.064892", "hw": "plosive consonant", "pos": "phrase", "ipa": "/ˈploʊsɪv ˈkɑːnsənənt/", "vi": "phụ âm bật hơi tắc thanh quản"},
  {"id": "lex.en.200k.064893", "hw": "porphyritic rock", "pos": "phrase", "ipa": "/ˌpɔːrfəˈrɪtɪk rɑːk/", "vi": "đá mácma có tinh thể lớn ban tinh"},
  {"id": "lex.en.200k.064894", "hw": "princeton wordnet", "pos": "phrase", "ipa": "/ˈprɪnstən ˈwɜːrdnɛt/", "vi": "cơ sở dữ liệu từ vựng WordNet"},
  {"id": "lex.en.200k.064895", "hw": "quadric surface", "pos": "phrase", "ipa": "/ˈkwɑːdrɪk ˈsɜːrfɪs/", "vi": "mặt bậc hai hình học giải tích"},
  {"id": "lex.en.200k.064896", "hw": "quantum chromodynamics", "pos": "phrase", "ipa": "/ˈkwɑːntəm ˌkroʊmoʊdaɪˈnæmɪks/", "vi": "sắc động lực học lượng tử QCD"},
  {"id": "lex.en.200k.064897", "hw": "red underwing", "pos": "phrase", "ipa": "/rɛd ˈʌndərˌwɪŋ/", "vi": "bướm đêm cánh sau màu đỏ rực"},
  {"id": "lex.en.200k.064898", "hw": "respiratory alkalosis", "pos": "phrase", "ipa": "/ˈrɛspərəˌtɔːri ˌælkəˈloʊsɪs/", "vi": "nhiễm kiềm hô hấp do thở quá nhanh"},
  {"id": "lex.en.200k.064899", "hw": "royal poinciana", "pos": "phrase", "ipa": "/ˈrɔɪəl ˌpɔɪnsiˈænə/", "vi": "cây phượng vĩ hoa đỏ rực mùa hè"},
  {"id": "lex.en.200k.064900", "hw": "sapele mahogany", "pos": "phrase", "ipa": "/səˈpiːli məˈhɑːɡəni/", "vi": "gỗ dái ngựa đỏ sapele châu Phi"},
  {"id": "lex.en.200k.064901", "hw": "solidago canadensis", "pos": "phrase", "ipa": "/ˌsɑːlɪˈdeɪɡoʊ ˌkænəˈdɛnsɪs/", "vi": "cây cúc hoàng anh hoa vàng Canada"},
  {"id": "lex.en.200k.064902", "hw": "tarahumara frog", "pos": "phrase", "ipa": "/ˌtɑːrəhuːˈmɑːrə frɔːɡ/", "vi": "loài ếch suối vùng núi Tarahumara"}
]

with open('scratch/b33_r10_raw_p4.json') as f:
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

with open('scratch/b33_r10_p4.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r10_p4.json OK")
