import json

items = [
  {"id": "lex.en.200k.061903", "hw": "retes", "pos": "noun", "ipa": "/ˈriːtiːz/", "vi": "mạng lưới mạch máu hoặc ống nhỏ"},
  {"id": "lex.en.200k.061904", "hw": "rouleaus", "pos": "noun", "ipa": "/ruːˈloʊz/", "vi": "cuộn tiền xu giấy; chuỗi hồng cầu"},
  {"id": "lex.en.200k.061905", "hw": "rumpelstiltskins", "pos": "noun", "ipa": "/ˌrʌmplˈstɪltskɪnz/", "vi": "yêu tinh cổ tích Rumpelstiltskin"},
  {"id": "lex.en.200k.061906", "hw": "saddened", "pos": "verb", "ipa": "/ˈsædnd/", "vi": "đã làm buồn lòng; đã khiến u sầu"},
  {"id": "lex.en.200k.061907", "hw": "saddening", "pos": "verb", "ipa": "/ˈsædnɪŋ/", "vi": "đang làm buồn lòng; khiến đau buồn"},
  {"id": "lex.en.200k.061908", "hw": "saddens", "pos": "verb", "ipa": "/ˈsædnz/", "vi": "làm buồn lòng; gây nỗi buồn thương"},
  {"id": "lex.en.200k.061909", "hw": "sambucas", "pos": "noun", "ipa": "/sæmˈbuːkəz/", "vi": "rượu mùi hồi ngọt Sambuca nước Ý"},
  {"id": "lex.en.200k.061910", "hw": "scleras", "pos": "noun", "ipa": "/ˈsklɪərəz/", "vi": "lớp củng mạc tròng trắng của mắt"},
  {"id": "lex.en.200k.061911", "hw": "scullions", "pos": "noun", "ipa": "/ˈskʌljənz/", "vi": "người hầu phụ bếp chuyên rửa bát"},
  {"id": "lex.en.200k.061912", "hw": "seemlier", "pos": "adj", "ipa": "/ˈsiːmliər/", "vi": "đúng mực trang nhã phải phép hơn"},
  {"id": "lex.en.200k.061913", "hw": "seemliest", "pos": "adj", "ipa": "/ˈsiːmliɪst/", "vi": "đúng mực trang nhã phải phép nhất"},
  {"id": "lex.en.200k.061914", "hw": "servals", "pos": "noun", "ipa": "/ˈsɜːrvəlz/", "vi": "loài mèo hoang tai to serval Phi"},
  {"id": "lex.en.200k.061915", "hw": "sheepsheads", "pos": "noun", "ipa": "/ˈʃiːpshɛdz/", "vi": "cá tráp răng cừu vằn sọc; kẻ ngốc"},
  {"id": "lex.en.200k.061916", "hw": "signboards", "pos": "noun", "ipa": "/ˈsaɪnbɔːrdz/", "vi": "tấm biển hiệu cửa hàng; biển báo"},
  {"id": "lex.en.200k.061917", "hw": "skipjacks", "pos": "noun", "ipa": "/ˈskɪpdʒæks/", "vi": "cá ngừ vằn đại dương; bọ bật nhảy"},
  {"id": "lex.en.200k.061918", "hw": "slatier", "pos": "adj", "ipa": "/ˈsleɪtiər/", "vi": "sắc xám đá phiến sẫm màu hơn"},
  {"id": "lex.en.200k.061919", "hw": "slatiest", "pos": "adj", "ipa": "/ˈsleɪtiɪst/", "vi": "màu xám đá phiến sẫm nhất"},
  {"id": "lex.en.200k.061920", "hw": "spasskies", "pos": "noun", "ipa": "/ˈspæskiz/", "vi": "vua cờ vua thế giới Boris Spassky"},
  {"id": "lex.en.200k.061921", "hw": "stoats", "pos": "noun", "ipa": "/stoʊts/", "vi": "chồn ecmin đuôi chóp đen mùa đông"},
  {"id": "lex.en.200k.061922", "hw": "strassburgs", "pos": "noun", "ipa": "/ˈstrɑːsbɜːrɡz/", "vi": "thành phố cổ Strasbourg nước Pháp"},
  {"id": "lex.en.200k.061923", "hw": "subpopulations", "pos": "noun", "ipa": "/ˌsʌbˌpɑːpjʊˈleɪʃənz/", "vi": "nhóm quần thể phụ thuộc cộng đồng"},
  {"id": "lex.en.200k.061924", "hw": "summarizations", "pos": "noun", "ipa": "/ˌsʌməraɪˈzeɪʃənz/", "vi": "sự tóm tắt nội dung ngắn gọn"},
  {"id": "lex.en.200k.061925", "hw": "sunrooms", "pos": "noun", "ipa": "/ˈsʌnruːmz/", "vi": "phòng kính đón nắng ấm trong nhà"},
  {"id": "lex.en.200k.061926", "hw": "taals", "pos": "noun", "ipa": "/tɑːlz/", "vi": "tiếng Hà Lan Nam Phi Afrikaans"},
  {"id": "lex.en.200k.061927", "hw": "thyroxines", "pos": "noun", "ipa": "/θaɪˈrɑːksiːnz/", "vi": "hoóc-môn tuyến giáp thyroxine T4"},
  {"id": "lex.en.200k.061928", "hw": "tlingits", "pos": "noun", "ipa": "/ˈtlɪŋɡɪts/", "vi": "bộ tộc thổ dân Tlingit Alaska"},
  {"id": "lex.en.200k.061929", "hw": "traineeships", "pos": "noun", "ipa": "/treɪˈniːʃɪps/", "vi": "chương trình thực tập sinh có lương"},
  {"id": "lex.en.200k.061930", "hw": "trilobites", "pos": "noun", "ipa": "/ˈtraɪləbaɪts/", "vi": "động vật hóa thạch bọ ba thùy cổ"},
  {"id": "lex.en.200k.061931", "hw": "trioxides", "pos": "noun", "ipa": "/traɪˈɑːksaɪdz/", "vi": "hợp chất hóa học oxit chứa 3 oxy"},
  {"id": "lex.en.200k.061932", "hw": "ulaanbaatars", "pos": "noun", "ipa": "/ˌuːlɑːnˈbɑːtərz/", "vi": "thủ đô Ulaanbaatar của Mông Cổ"},
  {"id": "lex.en.200k.061933", "hw": "umlauts", "pos": "noun", "ipa": "/ˈʊmlaʊts/", "vi": "dấu hai chấm đổi âm chữ cái Đức"},
  {"id": "lex.en.200k.061934", "hw": "undergarments", "pos": "noun", "ipa": "/ˈʌndərɡɑːrmənts/", "vi": "quần áo lót mặc bên trong người"},
  {"id": "lex.en.200k.061935", "hw": "vasodilations", "pos": "noun", "ipa": "/ˌveɪzoʊdaɪˈleɪʃənz/", "vi": "hiện tượng giãn nở lòng mạch máu"},
  {"id": "lex.en.200k.061936", "hw": "viburnums", "pos": "noun", "ipa": "/vaɪˈbɜːrnəmz/", "vi": "cây bụi hoa tú cầu dại viburnum"},
  {"id": "lex.en.200k.061937", "hw": "vidalias", "pos": "noun", "ipa": "/vaɪˈdeɪljəz/", "vi": "hành tây ngọt Vidalia; thị trấn Mỹ"},
  {"id": "lex.en.200k.061938", "hw": "windowpanes", "pos": "noun", "ipa": "/ˈwɪndoʊpeɪnz/", "vi": "tấm kính lắp trong khung cửa sổ"},
  {"id": "lex.en.200k.061939", "hw": "yawls", "pos": "noun", "ipa": "/jɔːlz/", "vi": "thuyền buồm hai cột buồm phụ sau"},
  {"id": "lex.en.200k.061940", "hw": "ymirs", "pos": "noun", "ipa": "/ˈiːmɪərz/", "vi": "người khổng lồ băng thủy tổ Ymir"},
  {"id": "lex.en.200k.061941", "hw": "ziggurats", "pos": "noun", "ipa": "/ˈzɪɡʊræts/", "vi": "đền tháp bậc thang Lưỡng Hà cổ"},
  {"id": "lex.en.200k.061942", "hw": "ague grass", "pos": "phrase", "ipa": "/ˈeɪɡjuː ɡræs/", "vi": "cây cỏ sao rễ vàng trị sốt rét"},
  {"id": "lex.en.200k.061943", "hw": "ague root", "pos": "phrase", "ipa": "/ˈeɪɡjuː ruːt/", "vi": "rễ cây thảo dược đắng trị sốt rét"},
  {"id": "lex.en.200k.061944", "hw": "ague weed", "pos": "phrase", "ipa": "/ˈeɪɡjuː wiːd/", "vi": "cây cỏ trạch lan đắng hạ sốt"},
  {"id": "lex.en.200k.061945", "hw": "albrecht durer", "pos": "phrase", "ipa": "/ˈɑːlbrɛkt ˈdjʊərər/", "vi": "danh họa Phục hưng Albrecht Dürer"},
  {"id": "lex.en.200k.061946", "hw": "alvar aalto", "pos": "phrase", "ipa": "/ˈɑːlvɑːr ˈɑːltoʊ/", "vi": "kiến trúc sư Phần Lan Alvar Aalto"},
  {"id": "lex.en.200k.061947", "hw": "american pennyroyal", "pos": "phrase", "ipa": "/əˈmɛrɪkən ˈpɛnirɔɪəl/", "vi": "cây bạc hà hăng đuổi muỗi Bắc Mỹ"},
  {"id": "lex.en.200k.061948", "hw": "andrei gromyko", "pos": "phrase", "ipa": "/ɑːnˈdreɪ ɡrəˈmiːkoʊ/", "vi": "nhà ngoại giao Xô Viết Gromyko"},
  {"id": "lex.en.200k.061949", "hw": "anoxic anoxia", "pos": "phrase", "ipa": "/ænˈɑːksɪk ænˈɑːksiə/", "vi": "chứng thiếu oxy do giảm khí thở"},
  {"id": "lex.en.200k.061950", "hw": "anterior fontanelle", "pos": "phrase", "ipa": "/ænˈtɪəriər ˌfɑːntəˈnɛl/", "vi": "thóp trước đỉnh đầu trẻ sơ sinh"},
  {"id": "lex.en.200k.061951", "hw": "artemisia californica", "pos": "phrase", "ipa": "/ˌɑːrtɪˈmiːʒə ˌkælɪˈfɔːrnɪkə/", "vi": "cây ngải thơm bụi xám California"},
  {"id": "lex.en.200k.061952", "hw": "bartolomeo vanzetti", "pos": "phrase", "ipa": "/ˌbɑːrtɑːləˈmeɪoʊ vænˈzɛti/", "vi": "người Ý bị xử oan vụ án Vanzetti"},
  {"id": "lex.en.200k.061953", "hw": "beau brummell", "pos": "phrase", "ipa": "/boʊ ˈbrʌml/", "vi": "người tiên phong mốt quý ông Anh"},
  {"id": "lex.en.200k.061954", "hw": "black guillemot", "pos": "phrase", "ipa": "/blæk ˈɡɪlɪmɑːt/", "vi": "chim biển guillemot đen chân đỏ"},
  {"id": "lex.en.200k.061955", "hw": "black lovage", "pos": "phrase", "ipa": "/blæk ˈlʌvɪdʒ/", "vi": "cây rau cần núi đen gia vị châu Âu"},
  {"id": "lex.en.200k.061956", "hw": "butterfly orchis", "pos": "phrase", "ipa": "/ˈbʌtərflaɪ ˈɔːrkɪs/", "vi": "cây hoa phong lan cánh bướm trắng"},
  {"id": "lex.en.200k.061957", "hw": "carissa grandiflora", "pos": "phrase", "ipa": "/kəˈrɪsə ˌɡrændɪˈflɔːrə/", "vi": "cây mận gai Nam Phi hoa trắng thơm"},
  {"id": "lex.en.200k.061958", "hw": "carlo goldoni", "pos": "phrase", "ipa": "/ˈkɑːrloʊ ɡoʊlˈdoʊni/", "vi": "nhà viết hài kịch Ý Carlo Goldoni"},
  {"id": "lex.en.200k.061959", "hw": "cattail millet", "pos": "phrase", "ipa": "/ˈkætteɪl ˈmɪlɪt/", "vi": "cây kê ngọc trai bông hình đuôi nến"},
  {"id": "lex.en.200k.061960", "hw": "common chickweed", "pos": "phrase", "ipa": "/ˈkɑːmən ˈtʃɪkwiːd/", "vi": "cỏ tinh thảo hoa sao trắng mọc dại"},
  {"id": "lex.en.200k.061961", "hw": "common duckweed", "pos": "phrase", "ipa": "/ˈkɑːmən ˈdʌkwiːd/", "vi": "cây bèo tấm xanh nổi trên mặt ao"},
  {"id": "lex.en.200k.061962", "hw": "crookes radiometer", "pos": "phrase", "ipa": "/krʊks ˌreɪdiˈɑːmɪtər/", "vi": "cối xay bức xạ ánh sáng Crookes"},
  {"id": "lex.en.200k.061963", "hw": "danse du ventre", "pos": "phrase", "ipa": "/dɑːns duː ˈvɑːntrə/", "vi": "điệu múa bụng quyến rũ Trung Đông"},
  {"id": "lex.en.200k.061964", "hw": "devanagari script", "pos": "phrase", "ipa": "/ˌdeɪvəˈnɑːɡəri skrɪpt/", "vi": "hệ chữ viết cổ Devanagari Ấn Độ"},
  {"id": "lex.en.200k.061965", "hw": "doggerel verse", "pos": "phrase", "ipa": "/ˈdɔːɡərəl vɜːrs/", "vi": "thơ con cóc vè vần điệu ngô nghê"},
  {"id": "lex.en.200k.061966", "hw": "draft evader", "pos": "phrase", "ipa": "/dræft ɪˈveɪdər/", "vi": "người trốn tránh nghĩa vụ quân sự"},
  {"id": "lex.en.200k.061967", "hw": "duckweed family", "pos": "phrase", "ipa": "/ˈdʌkwiːd ˈfæməli/", "vi": "phân họ thực vật Bèo tấm thủy sinh"},
  {"id": "lex.en.200k.061968", "hw": "epigastric artery", "pos": "phrase", "ipa": "/ˌɛpɪˈɡæstrɪk ˈɑːrtəri/", "vi": "động mạch thượng vị thành bụng"},
  {"id": "lex.en.200k.061969", "hw": "fagus americana", "pos": "phrase", "ipa": "/ˈfeɪɡəs əˌmɛrɪˈkeɪnə/", "vi": "cây dẻ gai vỏ xám nhẵn Bắc Mỹ"},
  {"id": "lex.en.200k.061970", "hw": "false glottis", "pos": "phrase", "ipa": "/fɔːls ˈɡlɑːtɪs/", "vi": "nếp tiền đình giả trên thanh môn"},
  {"id": "lex.en.200k.061971", "hw": "field chickweed", "pos": "phrase", "ipa": "/fiːld ˈtʃɪkwiːd/", "vi": "cỏ tinh thảo đồng hoa trắng nhỏ"},
  {"id": "lex.en.200k.061972", "hw": "flying gurnard", "pos": "phrase", "ipa": "/ˈflaɪɪŋ ˈɡɜːrnərd/", "vi": "cá chào mào biển vây xòe như cánh"},
  {"id": "lex.en.200k.061973", "hw": "genus cydonia", "pos": "phrase", "ipa": "/ˈdʒiːnəs sɪˈdoʊniə/", "vi": "chi cây mộc qua tây quả vàng thơm"},
  {"id": "lex.en.200k.061974", "hw": "genus jatropha", "pos": "phrase", "ipa": "/ˈdʒiːnəs dʒəˈtroʊfə/", "vi": "chi cây dầu mè cọc rào Jatropha"},
  {"id": "lex.en.200k.061975", "hw": "genus medicago", "pos": "phrase", "ipa": "/ˈdʒiːnəs mɛdɪˈkeɪɡoʊ/", "vi": "chi cỏ linh lăng giàu đạm Medicago"},
  {"id": "lex.en.200k.061976", "hw": "genus nerium", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈnɪriəm/", "vi": "chi cây hoa trúc đào nhựa độc"},
  {"id": "lex.en.200k.061977", "hw": "genus orchis", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈɔːrkɪs/", "vi": "chi địa lan củ đôi châu Âu Orchis"},
  {"id": "lex.en.200k.061978", "hw": "genus rheum", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈriːəm/", "vi": "chi thực vật cây đại hoàng Rheum"},
  {"id": "lex.en.200k.061979", "hw": "genus rissa", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈrɪsə/", "vi": "chi chim mòng biển chân đen Rissa"},
  {"id": "lex.en.200k.061980", "hw": "genus sterna", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈstɜːrnə/", "vi": "chi chim nhàn biển cánh dài Sterna"},
  {"id": "lex.en.200k.061981", "hw": "great duckweed", "pos": "phrase", "ipa": "/ɡreɪt ˈdʌkwiːd/", "vi": "bèo tấm lớn mặt dưới màu tía"},
  {"id": "lex.en.200k.061982", "hw": "harold clayton urey", "pos": "phrase", "ipa": "/ˈhɛrəld ˈkleɪtn ˈjʊəri/", "vi": "nhà hóa học tìm đơteri Harold Urey"},
  {"id": "lex.en.200k.061983", "hw": "henry engelhard steinway", "pos": "phrase", "ipa": "/ˈhɛnri ˈɛŋɡəlhɑːrd ˈstaɪnweɪ/", "vi": "nhà chế tạo đàn dương cầm Steinway"},
  {"id": "lex.en.200k.061984", "hw": "indian chickweed", "pos": "phrase", "ipa": "/ˈɪndiən ˈtʃɪkwiːd/", "vi": "cây rau đắng đất mọc bò sát mặt"},
  {"id": "lex.en.200k.061985", "hw": "inferior epigastric vein", "pos": "phrase", "ipa": "/ɪnˈfɪriər ˌɛpɪˈɡæstrɪk veɪn/", "vi": "tĩnh mạch thượng vị dưới ổ bụng"},
  {"id": "lex.en.200k.061986", "hw": "john dowland", "pos": "phrase", "ipa": "/dʒɑːn ˈdaʊlənd/", "vi": "nhạc sĩ đàn lute Anh John Dowland"},
  {"id": "lex.en.200k.061987", "hw": "joseph alois schumpeter", "pos": "phrase", "ipa": "/ˈdʒoʊzəf ˈɑːlɔɪs ˈʃʊmpɛtər/", "vi": "nhà kinh tế học Joseph Schumpeter"},
  {"id": "lex.en.200k.061988", "hw": "josip broz", "pos": "phrase", "ipa": "/ˈjoʊsɪp broʊz/", "vi": "lãnh tụ Nam Tư Josip Broz Tito"},
  {"id": "lex.en.200k.061989", "hw": "karl gunnar myrdal", "pos": "phrase", "ipa": "/kɑːrl ˈɡʊnɑːr ˈmɪərdɑːl/", "vi": "nhà kinh tế xã hội Gunnar Myrdal"},
  {"id": "lex.en.200k.061990", "hw": "kronecker delta", "pos": "phrase", "ipa": "/ˈkrɑːnɛkər ˈdɛltə/", "vi": "hàm số rời rạc Kronecker delta"},
  {"id": "lex.en.200k.061991", "hw": "lake nyasa", "pos": "phrase", "ipa": "/leɪk naɪˈæsə/", "vi": "hồ Malawi lớn ở Đông Nam Phi"},
  {"id": "lex.en.200k.061992", "hw": "lesser duckweed", "pos": "phrase", "ipa": "/ˈlɛsər ˈdʌkwiːd/", "vi": "cây bèo cám nhỏ nổi mặt nước ao"},
  {"id": "lex.en.200k.061993", "hw": "lickety cut", "pos": "phrase", "ipa": "/ˈlɪkəti kʌt/", "vi": "nhanh như cắt; vù một cái tức thì"},
  {"id": "lex.en.200k.061994", "hw": "lickety split", "pos": "phrase", "ipa": "/ˈlɪkəti splɪt/", "vi": "nhanh như chớp; vội vã tức khắc"},
  {"id": "lex.en.200k.061995", "hw": "macaca radiata", "pos": "phrase", "ipa": "/məˈkɑːkə ˌreɪdiˈeɪtə/", "vi": "loài khỉ mũ mào tóc xoáy Ấn Độ"},
  {"id": "lex.en.200k.061996", "hw": "male orchis", "pos": "phrase", "ipa": "/meɪl ˈɔːrkɪs/", "vi": "hoa địa lan tía sớm châu Âu"},
  {"id": "lex.en.200k.061997", "hw": "marabou stork", "pos": "phrase", "ipa": "/ˈmærəbuː stɔːrk/", "vi": "loài cò già marabou ăn xác thối"},
  {"id": "lex.en.200k.061998", "hw": "marcel lajos breuer", "pos": "phrase", "ipa": "/mɑːrˈsɛl ˈlɑːjoʊʃ ˈbrɔɪər/", "vi": "kiến trúc sư Bauhaus Marcel Breuer"},
  {"id": "lex.en.200k.061999", "hw": "mess of pottage", "pos": "phrase", "ipa": "/mɛs əv ˈpɑːtɪdʒ/", "vi": "món lợi nhỏ mọn rẻ mạt trước mắt"},
  {"id": "lex.en.200k.062000", "hw": "metallized dye", "pos": "phrase", "ipa": "/ˈmɛtlaɪzd daɪ/", "vi": "thuốc nhuộm phức hợp kim loại bền"},
  {"id": "lex.en.200k.062001", "hw": "nitrogen trichloride", "pos": "phrase", "ipa": "/ˈnaɪtrədʒən traɪˈklɔːraɪd/", "vi": "chất lỏng dễ nổ nitơ triclorua"},
  {"id": "lex.en.200k.062002", "hw": "old codger", "pos": "phrase", "ipa": "/oʊld ˈkɑːdʒər/", "vi": "ông lão kỳ quặc gàn dở (thân mật)"}
]

with open('scratch/b33_r04_raw_p5.json') as f:
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

with open('scratch/b33_r04_p5.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 4 Part 5 validated and written successfully.")
