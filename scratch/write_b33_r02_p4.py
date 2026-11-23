import json

items = [
  {"id": "lex.en.200k.060803", "hw": "tawneys", "pos": "noun", "ipa": "/ˈtɔːniz/", "vi": "nhà sử học kinh tế Richard Tawney"},
  {"id": "lex.en.200k.060804", "hw": "thms", "pos": "noun", "ipa": "/tiː eɪtʃ ɛmz/", "vi": "bằng Thạc sĩ Thần học ThM"},
  {"id": "lex.en.200k.060805", "hw": "ticinos", "pos": "noun", "ipa": "/tiːˈtʃiːnoʊz/", "vi": "bang Ticino nói tiếng Ý Thụy Sĩ"},
  {"id": "lex.en.200k.060806", "hw": "trotskyists", "pos": "noun", "ipa": "/ˈtrɑːtskiɪsts/", "vi": "người theo học thuyết Trotsky"},
  {"id": "lex.en.200k.060807", "hw": "truncheons", "pos": "noun", "ipa": "/ˈtrʌntʃənz/", "vi": "chiếc dùi cui cảnh sát"},
  {"id": "lex.en.200k.060808", "hw": "verlaines", "pos": "noun", "ipa": "/vɛərˈlɛnz/", "vi": "nhà thơ tượng trưng Paul Verlaine"},
  {"id": "lex.en.200k.060809", "hw": "wainscotings", "pos": "noun", "ipa": "/ˈweɪnskətɪŋz/", "vi": "tấm gỗ ốp chân tường trang trí"},
  {"id": "lex.en.200k.060810", "hw": "wavells", "pos": "noun", "ipa": "/ˈweɪvəlz/", "vi": "thống chế Anh Archibald Wavell"},
  {"id": "lex.en.200k.060811", "hw": "acidophilus milk", "pos": "phrase", "ipa": "/ˌæsɪˈdɑːfɪləs mɪlk/", "vi": "sữa lên men lợi khuẩn acidophilus"},
  {"id": "lex.en.200k.060812", "hw": "actinic dermatitis", "pos": "phrase", "ipa": "/ækˈtɪnɪk ˌdɜːrməˈtaɪtɪs/", "vi": "viêm da dị ứng ánh nắng mặt trời"},
  {"id": "lex.en.200k.060813", "hw": "alkane series", "pos": "phrase", "ipa": "/ˈælkeɪn ˈsɪriːz/", "vi": "dãy đồng đẳng hydrocacbon ankan"},
  {"id": "lex.en.200k.060814", "hw": "allen stewart konigsberg", "pos": "phrase", "ipa": "/ˈælən ˈstjuːərt ˈkɑːnɪɡzbɜːrɡ/", "vi": "đạo diễn điện ảnh Woody Allen"},
  {"id": "lex.en.200k.060815", "hw": "alpha crucis", "pos": "phrase", "ipa": "/ˈælfə ˈkruːsɪs/", "vi": "ngôi sao sáng nhất chòm Nam Thập"},
  {"id": "lex.en.200k.060816", "hw": "american foxhound", "pos": "phrase", "ipa": "/əˈmɛrɪkən ˈfɑːkshaʊnd/", "vi": "giống chó săn cáo chạy nhanh Mỹ"},
  {"id": "lex.en.200k.060817", "hw": "anechoic chamber", "pos": "phrase", "ipa": "/ˌænɪˈkoʊɪk ˈtʃeɪmbər/", "vi": "buồng triệt tiêu dội âm không tiếng"},
  {"id": "lex.en.200k.060818", "hw": "apus apus", "pos": "phrase", "ipa": "/ˈeɪpəs ˈeɪpəs/", "vi": "loài chim yến lượn bụng trắng đen"},
  {"id": "lex.en.200k.060819", "hw": "aquila degli abruzzi", "pos": "phrase", "ipa": "/ˈɑːkwilə ˈdɛlji əˈbruːtsi/", "vi": "thành phố miền núi L'Aquila ở Ý"},
  {"id": "lex.en.200k.060820", "hw": "arctic skua", "pos": "phrase", "ipa": "/ˈɑːrktɪk ˈskjuːə/", "vi": "chim cướp biển Bắc Cực săn mồi"},
  {"id": "lex.en.200k.060821", "hw": "baader meinhof gang", "pos": "phrase", "ipa": "/ˈbɑːdər ˈmaɪnhɔːf ɡæŋ/", "vi": "nhóm vũ trang Baader-Meinhof Đức"},
  {"id": "lex.en.200k.060822", "hw": "benvenuto cellini", "pos": "phrase", "ipa": "/ˌbɛnvəˈnuːtoʊ tʃəˈliːni/", "vi": "thợ kim hoàn điêu khắc Ý Cellini"},
  {"id": "lex.en.200k.060823", "hw": "beta crucis", "pos": "phrase", "ipa": "/ˈbeɪtə ˈkruːsɪs/", "vi": "ngôi sao Mimosa chòm Nam Thập Tự"},
  {"id": "lex.en.200k.060824", "hw": "bicuspid valve", "pos": "phrase", "ipa": "/baɪˈkʌspɪd vælv/", "vi": "van hai lá tim trái; van nhĩ thất"},
  {"id": "lex.en.200k.060825", "hw": "bowline knot", "pos": "phrase", "ipa": "/ˈboʊlɪn nɑːt/", "vi": "nút thắt dây thòng lọng hàng hải"},
  {"id": "lex.en.200k.060826", "hw": "bush nasturtium", "pos": "phrase", "ipa": "/bʊʃ nəˈstɜːrʃəm/", "vi": "cây hoa sen cạn dạng bụi thấp"},
  {"id": "lex.en.200k.060827", "hw": "calla palustris", "pos": "phrase", "ipa": "/ˈkælə pəˈlʌstrɪs/", "vi": "cây ráy nước hoa mo trắng đầm lầy"},
  {"id": "lex.en.200k.060828", "hw": "diapason stop", "pos": "phrase", "ipa": "/ˌdaɪəˈpeɪzən stɑːp/", "vi": "cần kéo thanh âm chính đàn organ"},
  {"id": "lex.en.200k.060829", "hw": "dwarf spurge", "pos": "phrase", "ipa": "/dwɔːrf spɜːrdʒ/", "vi": "cây cỏ sữa lùn thân thấp mảnh"},
  {"id": "lex.en.200k.060830", "hw": "ejaculatory duct", "pos": "phrase", "ipa": "/ɪˈdʒækjʊlətɔːri dʌkt/", "vi": "ống phóng tinh giải phẫu sinh dục"},
  {"id": "lex.en.200k.060831", "hw": "eminence grise", "pos": "phrase", "ipa": "/ˌɛmɪnɑːns ˈɡriːz/", "vi": "nhân vật quyền lực giật dây ngầm"},
  {"id": "lex.en.200k.060832", "hw": "english foxhound", "pos": "phrase", "ipa": "/ˈɪŋɡlɪʃ ˈfɑːkshaʊnd/", "vi": "giống chó săn cáo truyền thống Anh"},
  {"id": "lex.en.200k.060833", "hw": "flowering spurge", "pos": "phrase", "ipa": "/ˈflaʊərɪŋ spɜːrdʒ/", "vi": "cây cỏ sữa nở chùm hoa trắng nhỏ"},
  {"id": "lex.en.200k.060834", "hw": "garden nasturtium", "pos": "phrase", "ipa": "/ˈɡɑːrdn nəˈstɜːrʃəm/", "vi": "cây hoa sen cạn cảnh trồng vườn"},
  {"id": "lex.en.200k.060835", "hw": "genus allosaurus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌæləˈsɔːrəs/", "vi": "chi khủng long ăn thịt Allosaurus"},
  {"id": "lex.en.200k.060836", "hw": "genus myotis", "pos": "phrase", "ipa": "/ˈdʒiːnəs maɪˈoʊtɪs/", "vi": "chi dơi nhỏ tai chuột Myotis"},
  {"id": "lex.en.200k.060837", "hw": "gideon algernon mantell", "pos": "phrase", "ipa": "/ˈɡɪdiən ˈældʒərnɑːn ˈmæntl/", "vi": "nhà cổ sinh vật học Gideon Mantell"},
  {"id": "lex.en.200k.060838", "hw": "great skua", "pos": "phrase", "ipa": "/ɡreɪt ˈskjuːə/", "vi": "loài chim cướp biển cỡ lớn Bắc Âu"},
  {"id": "lex.en.200k.060839", "hw": "gum benzoin", "pos": "phrase", "ipa": "/ɡʌm ˈbɛnzoʊɪn/", "vi": "nhựa thơm cánh kiến trắng benzoin"},
  {"id": "lex.en.200k.060840", "hw": "harry lillis crosby", "pos": "phrase", "ipa": "/ˈhæri ˈlɪlɪs ˈkrɔːzbi/", "vi": "danh ca tài tử Mỹ Bing Crosby"},
  {"id": "lex.en.200k.060841", "hw": "heinrich schliemann", "pos": "phrase", "ipa": "/ˈhaɪnrɪk ˈʃliːmɑːn/", "vi": "nhà khảo cổ Heinrich Schliemann"},
  {"id": "lex.en.200k.060842", "hw": "hermann snellen", "pos": "phrase", "ipa": "/ˈhɛərmɑːn ˈsnɛlən/", "vi": "bác sĩ nhãn khoa Hermann Snellen"},
  {"id": "lex.en.200k.060843", "hw": "heterodyne oscillator", "pos": "phrase", "ipa": "/ˈhɛtərədaɪn ˈɑːsɪleɪtər/", "vi": "mạch dao động tạo phách dị tần"},
  {"id": "lex.en.200k.060844", "hw": "horsetail lichen", "pos": "phrase", "ipa": "/ˈhɔːrsteɪl ˈlaɪkən/", "vi": "loài địa y sợi dài đuôi ngựa"},
  {"id": "lex.en.200k.060845", "hw": "hugh dowding", "pos": "phrase", "ipa": "/hjuː ˈdaʊdɪŋ/", "vi": "tư lệnh Không quân Anh Hugh Dowding"},
  {"id": "lex.en.200k.060846", "hw": "isaac merrit singer", "pos": "phrase", "ipa": "/ˈaɪzək ˈmɛrɪt ˈsɪŋər/", "vi": "nhà phát minh máy khâu Isaac Singer"},
  {"id": "lex.en.200k.060847", "hw": "jan evangelista purkinje", "pos": "phrase", "ipa": "/jɑːn iːˌvændʒəˈliːstə ˈpɜːrkɪndʒi/", "vi": "nhà sinh lý học Séc Jan Purkyně"},
  {"id": "lex.en.200k.060848", "hw": "jointer plane", "pos": "phrase", "ipa": "/ˈdʒɔɪntər pleɪn/", "vi": "cây bào dài làm phẳng mối ghép gỗ"},
  {"id": "lex.en.200k.060849", "hw": "karelian isthmus", "pos": "phrase", "ipa": "/kəˈriːljən ˈɪsməs/", "vi": "eo đất chiến lược Karelia nước Nga"},
  {"id": "lex.en.200k.060850", "hw": "karl augustus menninger", "pos": "phrase", "ipa": "/kɑːrl ɔːˈɡʌstəs ˈmɛnɪŋɡər/", "vi": "bác sĩ tâm thần học Karl Menninger"},
  {"id": "lex.en.200k.060851", "hw": "kubla khan", "pos": "phrase", "ipa": "/ˈkuːblə kɑːn/", "vi": "Đại hãn Mông Cổ Hốt Tất Liệt"},
  {"id": "lex.en.200k.060852", "hw": "latchkey child", "pos": "phrase", "ipa": "/ˈlætʃkiː tʃaɪld/", "vi": "trẻ tự ở nhà một mình sau giờ học"},
  {"id": "lex.en.200k.060853", "hw": "lead arsenate", "pos": "phrase", "ipa": "/lɛd ˈɑːrsəneɪt/", "vi": "chất trừ sâu độc hại chì asenat"},
  {"id": "lex.en.200k.060854", "hw": "leafy spurge", "pos": "phrase", "ipa": "/ˈliːfi spɜːrdʒ/", "vi": "cỏ sữa lá xâm hại đồng cỏ Bắc Mỹ"},
  {"id": "lex.en.200k.060855", "hw": "litchi nut", "pos": "phrase", "ipa": "/ˈlaɪtʃi nʌt/", "vi": "quả vải thiều ngọt mọng nước"},
  {"id": "lex.en.200k.060856", "hw": "litchi tree", "pos": "phrase", "ipa": "/ˈlaɪtʃi triː/", "vi": "cây vải thiều trồng ăn quả"},
  {"id": "lex.en.200k.060857", "hw": "louvered window", "pos": "phrase", "ipa": "/ˈluːvərd ˈwɪndoʊ/", "vi": "cửa sổ chớp lật lá sách thông gió"},
  {"id": "lex.en.200k.060858", "hw": "loya jirga", "pos": "phrase", "ipa": "/ˈlɔɪə ˈdʒɪərɡə/", "vi": "đại hội đồng bô lão Afghanistan"},
  {"id": "lex.en.200k.060859", "hw": "mandibular condyle", "pos": "phrase", "ipa": "/mænˈdɪbjələr ˈkɑːndaɪl/", "vi": "lồi cầu khớp nối xương hàm dưới"},
  {"id": "lex.en.200k.060860", "hw": "mangosteen tree", "pos": "phrase", "ipa": "/ˈmæŋɡəstiːn triː/", "vi": "cây măng cụt nhiệt đới quả tím"},
  {"id": "lex.en.200k.060861", "hw": "mansard roof", "pos": "phrase", "ipa": "/ˈmænsɑːrd ruːf/", "vi": "kiểu mái vát hai độ dốc Mansard"},
  {"id": "lex.en.200k.060862", "hw": "meiji tenno", "pos": "phrase", "ipa": "/ˈmeɪdʒi ˈtɛnoʊ/", "vi": "Thiên hoàng Minh Trị Nhật Bản"},
  {"id": "lex.en.200k.060863", "hw": "mikhail kalinin", "pos": "phrase", "ipa": "/mɪˈkaɪl kəˈliːnɪn/", "vi": "chủ tịch Xô Viết Mikhail Kalinin"},
  {"id": "lex.en.200k.060864", "hw": "musculus sphincter ani", "pos": "phrase", "ipa": "/ˈmʌskjʊləs ˈsfɪŋktər ˈeɪnaɪ/", "vi": "cơ vòng thắt điều khiển hậu môn"},
  {"id": "lex.en.200k.060865", "hw": "myrtle spurge", "pos": "phrase", "ipa": "/ˈmɜːrtl spɜːrdʒ/", "vi": "cây cỏ sữa lá sim mọng nước bò lan"},
  {"id": "lex.en.200k.060866", "hw": "nasturtium family", "pos": "phrase", "ipa": "/nəˈstɜːrʃəm ˈfæməli/", "vi": "họ thực vật cây hoa sen cạn"},
  {"id": "lex.en.200k.060867", "hw": "naut mi", "pos": "phrase", "ipa": "/ˈnɔːtɪkl maɪl/", "vi": "đơn vị đo đường biển hải lý"},
  {"id": "lex.en.200k.060868", "hw": "oculomotor nerve", "pos": "phrase", "ipa": "/ˌɑːkjʊloʊˈmoʊtər nɜːrv/", "vi": "dây thần kinh sọ số III vận nhãn"},
  {"id": "lex.en.200k.060869", "hw": "olduvai gorge", "pos": "phrase", "ipa": "/ˈoʊldʊvaɪ ɡɔːrdʒ/", "vi": "hẻm núi khảo cổ người cổ Olduvai"},
  {"id": "lex.en.200k.060870", "hw": "ovis aries", "pos": "phrase", "ipa": "/ˈoʊvɪs ˈɛəriːz/", "vi": "loài cừu nhà nuôi lấy lông thịt"},
  {"id": "lex.en.200k.060871", "hw": "parceled out", "pos": "phrase", "ipa": "/ˈpɑːrsəld aʊt/", "vi": "đã phân chia nhỏ ra từng phần"},
  {"id": "lex.en.200k.060872", "hw": "piper nigrum", "pos": "phrase", "ipa": "/ˈpaɪpər ˈnaɪɡrəm/", "vi": "dây hồ tiêu gia vị cay nồng"},
  {"id": "lex.en.200k.060873", "hw": "popliteal artery", "pos": "phrase", "ipa": "/ˌpɑːplɪˈtiːəl ˈɑːrtəri/", "vi": "động mạch vùng khoeo sau đầu gối"},
  {"id": "lex.en.200k.060874", "hw": "postfix notation", "pos": "phrase", "ipa": "/ˈpoʊstfɪks noʊˈteɪʃən/", "vi": "ký pháp Ba Lan ngược hậu tố toán"},
  {"id": "lex.en.200k.060875", "hw": "primula sinensis", "pos": "phrase", "ipa": "/ˈprɪmjʊlə saɪˈnɛnsɪs/", "vi": "hoa anh thảo cảnh gốc Trung Quốc"},
  {"id": "lex.en.200k.060876", "hw": "pterygoid muscle", "pos": "phrase", "ipa": "/ˈtɛrɪɡɔɪd ˈmʌsl/", "vi": "cơ chân bướm hỗ trợ nhai hàm"},
  {"id": "lex.en.200k.060877", "hw": "pterygoid process", "pos": "phrase", "ipa": "/ˈtɛrɪɡɔɪd ˈprɑːsɛs/", "vi": "mỏm chân bướm xương bướm hộp sọ"},
  {"id": "lex.en.200k.060878", "hw": "sea of azoff", "pos": "phrase", "ipa": "/siː əv ˈɑːzɔːf/", "vi": "vùng biển nội địa Azov Biển Đen"},
  {"id": "lex.en.200k.060879", "hw": "sholom asch", "pos": "phrase", "ipa": "/ˈʃɑːloʊm ɑːʃ/", "vi": "nhà văn gốc Ba Lan Sholom Asch"},
  {"id": "lex.en.200k.060880", "hw": "spurge laurel", "pos": "phrase", "ipa": "/spɜːrdʒ ˈlɔːrəl/", "vi": "cây bụi thường xanh nguyệt quế gai"},
  {"id": "lex.en.200k.060881", "hw": "stinking hellebore", "pos": "phrase", "ipa": "/ˈstɪŋkɪŋ ˈhɛlɪbɔːr/", "vi": "cây lê lô mùi hôi hoa xanh lục"},
  {"id": "lex.en.200k.060882", "hw": "sub judice", "pos": "phrase", "ipa": "/sʌb ˈdʒuːdɪsi/", "vi": "vụ việc đang chờ tòa án xét xử"},
  {"id": "lex.en.200k.060883", "hw": "transuranic element", "pos": "phrase", "ipa": "/ˌtrænzjʊˈrænɪk ˈɛləmənt/", "vi": "nguyên tố hóa học nặng sau urani"},
  {"id": "lex.en.200k.060884", "hw": "trazodone hydrochloride", "pos": "phrase", "ipa": "/ˈtræzədoʊn ˌhaɪdrəˈklɔːraɪd/", "vi": "thuốc điều trị trầm cảm trazodone"},
  {"id": "lex.en.200k.060885", "hw": "tycho brahe", "pos": "phrase", "ipa": "/ˈtaɪkoʊ ˈbrɑːhi/", "vi": "nhà thiên văn Đan Mạch Tycho Brahe"},
  {"id": "lex.en.200k.060886", "hw": "uranyl nitrate", "pos": "phrase", "ipa": "/ˈjʊərənɪl ˈnaɪtreɪt/", "vi": "muối tinh thể vàng uranyl nitrat"},
  {"id": "lex.en.200k.060887", "hw": "vigna sinensis", "pos": "phrase", "ipa": "/ˈvɪɡnə saɪˈnɛnsɪs/", "vi": "cây đậu đũa; đậu trắng mắt đen"},
  {"id": "lex.en.200k.060888", "hw": "viola pubescens", "pos": "phrase", "ipa": "/vaɪˈoʊlə pjuːˈbɛsənz/", "vi": "loài hoa violet vàng lá lông mềm"},
  {"id": "lex.en.200k.060889", "hw": "vladimir vladimirovich nabokov", "pos": "phrase", "ipa": "/vlæˈdɪmɪr vlæˈdɪmɪrəvɪtʃ nəˈbɔːkɔːf/", "vi": "tiểu thuyết gia Nga-Mỹ Nabokov"},
  {"id": "lex.en.200k.060890", "hw": "walker foxhound", "pos": "phrase", "ipa": "/ˈwɔːkər ˈfɑːkshaʊnd/", "vi": "giống chó săn cáo Treeing Walker"},
  {"id": "lex.en.200k.060891", "hw": "activewears", "pos": "noun", "ipa": "/ˈæktɪvwɛərz/", "vi": "trang phục tập luyện thể thao"},
  {"id": "lex.en.200k.060892", "hw": "adits", "pos": "noun", "ipa": "/ˈædɪts/", "vi": "đường hầm ngang dẫn vào trong mỏ"},
  {"id": "lex.en.200k.060893", "hw": "allyls", "pos": "noun", "ipa": "/ˈælɪlz/", "vi": "nhóm gốc hữu cơ allyl hóa học"},
  {"id": "lex.en.200k.060894", "hw": "antananarivos", "pos": "noun", "ipa": "/ˌɑːntəˌnɑːnəˈriːvoʊz/", "vi": "thủ đô Antananarivo Madagascar"},
  {"id": "lex.en.200k.060895", "hw": "asciteses", "pos": "noun", "ipa": "/əˈsaɪtiːzɪz/", "vi": "bệnh cổ trướng tích dịch ổ bụng"},
  {"id": "lex.en.200k.060896", "hw": "aspics", "pos": "noun", "ipa": "/ˈæspɪks/", "vi": "món thạch thịt nấu đông trong suốt"},
  {"id": "lex.en.200k.060897", "hw": "avicennas", "pos": "noun", "ipa": "/ˌævɪˈsɛnəz/", "vi": "danh y triết gia Ba Tư Ibn Sina"},
  {"id": "lex.en.200k.060898", "hw": "barrettes", "pos": "noun", "ipa": "/bəˈrɛts/", "vi": "chiếc kẹp tóc cài trang trí nữ"},
  {"id": "lex.en.200k.060899", "hw": "bellocs", "pos": "noun", "ipa": "/ˈbɛlɑːks/", "vi": "nhà văn nhà sử học Hilaire Belloc"},
  {"id": "lex.en.200k.060900", "hw": "bitterns", "pos": "noun", "ipa": "/ˈbɪtərnz/", "vi": "chim vạc đầm lầy cổ ngắn kêu to"},
  {"id": "lex.en.200k.060901", "hw": "blackheads", "pos": "noun", "ipa": "/ˈblækhɛdz/", "vi": "mụn đầu đen trên da mặt; đầu đinh"},
  {"id": "lex.en.200k.060902", "hw": "bleeders", "pos": "noun", "ipa": "/ˈbliːdərz/", "vi": "người mắc bệnh máu khó đông"}
]

with open('scratch/b33_r02_raw_p4.json') as f:
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

with open('scratch/b33_r02_p4.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 2 Part 4 validated and written successfully.")
