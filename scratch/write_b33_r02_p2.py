import json

items = [
  {"id": "lex.en.200k.060603", "hw": "siltiest", "pos": "adj", "ipa": "/ˈsɪltiɪst/", "vi": "đầy phù sa bùn cát lắng nhất"},
  {"id": "lex.en.200k.060604", "hw": "sobriquets", "pos": "noun", "ipa": "/ˈsoʊbrɪkeɪz/", "vi": "biệt danh; tên hiệu thường gọi"},
  {"id": "lex.en.200k.060605", "hw": "southers", "pos": "noun", "ipa": "/ˈsaʊðərz/", "vi": "cơn gió thổi mạnh từ hướng nam"},
  {"id": "lex.en.200k.060606", "hw": "splashdowns", "pos": "noun", "ipa": "/ˈsplæʃdaʊnz/", "vi": "sự hạ cánh tàu vũ trụ xuống biển"},
  {"id": "lex.en.200k.060607", "hw": "stelas", "pos": "noun", "ipa": "/ˈstiːləz/", "vi": "bia đá khắc chữ kỷ niệm cổ đại"},
  {"id": "lex.en.200k.060608", "hw": "strabismuses", "pos": "noun", "ipa": "/strəˈbɪzməsɪz/", "vi": "chứng lác mắt; tật lé mắt bẩm sinh"},
  {"id": "lex.en.200k.060609", "hw": "surveiled", "pos": "verb", "ipa": "/sərˈveɪld/", "vi": "đã theo dõi giám sát bí mật"},
  {"id": "lex.en.200k.060610", "hw": "surveiling", "pos": "verb", "ipa": "/sərˈveɪlɪŋ/", "vi": "đang theo dõi giám sát an ninh"},
  {"id": "lex.en.200k.060611", "hw": "surveils", "pos": "verb", "ipa": "/sərˈveɪlz/", "vi": "theo dõi chặt chẽ; giám sát"},
  {"id": "lex.en.200k.060612", "hw": "taches", "pos": "noun", "ipa": "/tɑːʃɪz/", "vi": "vết bớt sắc tố trên da; đồng hồ đo"},
  {"id": "lex.en.200k.060613", "hw": "thessalonicas", "pos": "noun", "ipa": "/ˌθɛsələˈniːkəz/", "vi": "thành phố cảng Thessaloniki Hy Lạp"},
  {"id": "lex.en.200k.060614", "hw": "thrombi", "pos": "noun", "ipa": "/ˈθrɑːmbaɪ/", "vi": "cục máu đông huyết khối trong mạch"},
  {"id": "lex.en.200k.060615", "hw": "thrombins", "pos": "noun", "ipa": "/ˈθrɑːmbɪnz/", "vi": "men thrombin làm đông tụ máu"},
  {"id": "lex.en.200k.060616", "hw": "tollers", "pos": "noun", "ipa": "/ˈtoʊlərz/", "vi": "người kéo chuông; người thu phí"},
  {"id": "lex.en.200k.060617", "hw": "tortes", "pos": "noun", "ipa": "/ˈtɔːrts/", "vi": "bánh ngọt torte nhiều tầng kem hạt"},
  {"id": "lex.en.200k.060618", "hw": "tribesmen", "pos": "noun", "ipa": "/ˈtraɪbzmən/", "vi": "người dân thành viên trong bộ lạc"},
  {"id": "lex.en.200k.060619", "hw": "tuchmans", "pos": "noun", "ipa": "/ˈtʌkmənz/", "vi": "nữ sử gia Mỹ Barbara Tuchman"},
  {"id": "lex.en.200k.060620", "hw": "turbojets", "pos": "noun", "ipa": "/ˈtɜːrboʊdʒɛts/", "vi": "động cơ phản lực tuabin khí"},
  {"id": "lex.en.200k.060621", "hw": "turgenevs", "pos": "noun", "ipa": "/tʊərˈɡeɪnjəvz/", "vi": "đại văn hào Nga Ivan Turgenev"},
  {"id": "lex.en.200k.060622", "hw": "twerps", "pos": "noun", "ipa": "/twɜːrps/", "vi": "gã ngốc đáng ghét; kẻ nhát gan hèn"},
  {"id": "lex.en.200k.060623", "hw": "valencienneses", "pos": "noun", "ipa": "/ˌvælənˈsjɛnzɪz/", "vi": "thành phố Valenciennes Pháp"},
  {"id": "lex.en.200k.060624", "hw": "wiesenthals", "pos": "noun", "ipa": "/ˈviːzənθɑːlz/", "vi": "nhà săn tội phạm Simon Wiesenthal"},
  {"id": "lex.en.200k.060625", "hw": "withes", "pos": "noun", "ipa": "/wɪðz/", "vi": "nhành liễu dẻo bện dây buộc bó củi"},
  {"id": "lex.en.200k.060626", "hw": "yachtsmen", "pos": "noun", "ipa": "/ˈjɑːtsmən/", "vi": "người chơi lái du thuyền trên biển"},
  {"id": "lex.en.200k.060627", "hw": "yellers", "pos": "noun", "ipa": "/ˈjɛlərz/", "vi": "người hay la hét ầm ĩ quát tháo"},
  {"id": "lex.en.200k.060628", "hw": "aare river", "pos": "phrase", "ipa": "/ˈɑːrə ˈrɪvər/", "vi": "dòng sông Aare chảy qua Thụy Sĩ"},
  {"id": "lex.en.200k.060629", "hw": "acer rubrum", "pos": "phrase", "ipa": "/ˈeɪsər ˈruːbrəm/", "vi": "cây phong lá đỏ rực Bắc Mỹ"},
  {"id": "lex.en.200k.060630", "hw": "american barberry", "pos": "phrase", "ipa": "/əˈmɛrɪkən ˈbɑːrbɛri/", "vi": "cây hoàng liên gai mọc ở Bắc Mỹ"},
  {"id": "lex.en.200k.060631", "hw": "anemone sylvestris", "pos": "phrase", "ipa": "/əˈnɛməni sɪlˈvɛstrɪs/", "vi": "cây hoa hải quỳ tuyết trắng châu Âu"},
  {"id": "lex.en.200k.060632", "hw": "antineoplastic antibiotic", "pos": "phrase", "ipa": "/ˌæntiˌniːoʊˈplæstɪk ˌæntibaɪˈɑːtɪk/", "vi": "thuốc kháng sinh điều trị ung thư"},
  {"id": "lex.en.200k.060633", "hw": "arnold lucius gesell", "pos": "phrase", "ipa": "/ˈɑːrnəld ˈluːʃəs ɡəˈzɛl/", "vi": "bác sĩ tâm lý trẻ em Arnold Gesell"},
  {"id": "lex.en.200k.060634", "hw": "artium magister", "pos": "phrase", "ipa": "/ˈɑːrtiəm ˈmædʒɪstər/", "vi": "học vị thạc sĩ nghệ thuật nhân văn"},
  {"id": "lex.en.200k.060635", "hw": "atomistic theory", "pos": "phrase", "ipa": "/ˌætəˈmɪstɪk ˈθiːəri/", "vi": "học thuyết nguyên tử luận"},
  {"id": "lex.en.200k.060636", "hw": "barberry family", "pos": "phrase", "ipa": "/ˈbɑːrbɛri ˈfæməli/", "vi": "họ thực vật cây hoàng liên gai"},
  {"id": "lex.en.200k.060637", "hw": "bechamel sauce", "pos": "phrase", "ipa": "/ˌbeɪʃəˈmɛl sɔːs/", "vi": "nước sốt kem trắng kiểu Pháp"},
  {"id": "lex.en.200k.060638", "hw": "berna eli oldfield", "pos": "phrase", "ipa": "/ˈbɜːrnə ˈiːlaɪ ˈoʊldfiːld/", "vi": "tay đua xe huyền thoại Oldfield"},
  {"id": "lex.en.200k.060639", "hw": "bernardo bertolucci", "pos": "phrase", "ipa": "/bərˈnɑːrdoʊ ˌbɜːrtəˈluːtʃi/", "vi": "đạo diễn điện ảnh Ý Bertolucci"},
  {"id": "lex.en.200k.060640", "hw": "boris godunov", "pos": "phrase", "ipa": "/ˈbɔːrɪs ˌɡɑːdʊˈnɔːf/", "vi": "Sa hoàng Nga Boris Godunov"},
  {"id": "lex.en.200k.060641", "hw": "bristly sarsaparilla", "pos": "phrase", "ipa": "/ˈbrɪsli ˌsærsəpəˈrɪlə/", "vi": "cây nhân sâm gai lông Bắc Mỹ"},
  {"id": "lex.en.200k.060642", "hw": "brow ptosis", "pos": "phrase", "ipa": "/braʊ ˈtoʊsɪs/", "vi": "chứng sa sụp cung lông mày"},
  {"id": "lex.en.200k.060643", "hw": "butyric acid", "pos": "phrase", "ipa": "/bjuːˈtɪrɪk ˈæsɪd/", "vi": "axit béo butyric mùi bơ ôi thiu"},
  {"id": "lex.en.200k.060644", "hw": "calcium stearate", "pos": "phrase", "ipa": "/ˈkælsiəm ˈstɪəreɪt/", "vi": "chất phụ gia canxi stearat"},
  {"id": "lex.en.200k.060645", "hw": "cave myotis", "pos": "phrase", "ipa": "/keɪv maɪˈoʊtɪs/", "vi": "loài dơi tai chuột sống trong hang"},
  {"id": "lex.en.200k.060646", "hw": "chanson de geste", "pos": "phrase", "ipa": "/ʃɑ̃ːˈsɔ̃ː də ˈʒɛst/", "vi": "trường ca sử thi trung cổ Pháp"},
  {"id": "lex.en.200k.060647", "hw": "charles frederick menninger", "pos": "phrase", "ipa": "/tʃɑːrlz ˈfrɛdərɪk ˈmɛnɪŋɡər/", "vi": "bác sĩ tâm thần Charles Menninger"},
  {"id": "lex.en.200k.060648", "hw": "charles menninger", "pos": "phrase", "ipa": "/tʃɑːrlz ˈmɛnɪŋɡər/", "vi": "nhà tâm thần học Charles Menninger"},
  {"id": "lex.en.200k.060649", "hw": "chinese jujube", "pos": "phrase", "ipa": "/tʃaɪˈniːz ˈdʒuːdʒuːb/", "vi": "quả táo tàu đỏ sấy khô thuốc bắc"},
  {"id": "lex.en.200k.060650", "hw": "common barberry", "pos": "phrase", "ipa": "/ˈkɑːmən ˈbɑːrbɛri/", "vi": "cây bụi gai hoàng mộc quả đỏ chua"},
  {"id": "lex.en.200k.060651", "hw": "copperplate engraving", "pos": "phrase", "ipa": "/ˈkɑːpərpleɪt ɪnˈɡreɪvɪŋ/", "vi": "nghệ thuật in tranh khắc bản đồng"},
  {"id": "lex.en.200k.060652", "hw": "digitalis lutea", "pos": "phrase", "ipa": "/ˌdɪdʒɪˈteɪlɪs ˈluːtiə/", "vi": "cây mao địa hoàng hoa vàng rơm"},
  {"id": "lex.en.200k.060653", "hw": "digitalis purpurea", "pos": "phrase", "ipa": "/ˌdɪdʒɪˈteɪlɪs pɜːrˈpjʊəriə/", "vi": "cây mao địa hoàng hoa chuông tím"},
  {"id": "lex.en.200k.060654", "hw": "edward jean steichen", "pos": "phrase", "ipa": "/ˈɛdwərd dʒiːn ˈstaɪkən/", "vi": "nhiếp ảnh gia Mỹ Edward Steichen"},
  {"id": "lex.en.200k.060655", "hw": "erwin panofsky", "pos": "phrase", "ipa": "/ˈɜːrwɪn pəˈnɑːfski/", "vi": "sử gia nghệ thuật Erwin Panofsky"},
  {"id": "lex.en.200k.060656", "hw": "european barberry", "pos": "phrase", "ipa": "/ˌjʊərəˈpiːən ˈbɑːrbɛri/", "vi": "cây hoàng mộc gai châu Âu"},
  {"id": "lex.en.200k.060657", "hw": "fulminating mercury", "pos": "phrase", "ipa": "/ˈfʊlmɪneɪtɪŋ ˈmɜːrkjəri/", "vi": "thủy ngân fulminat làm kíp nổ"},
  {"id": "lex.en.200k.060658", "hw": "genus bubo", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈbjuːboʊ/", "vi": "chi chim cú lớn sừng tai Bubo"},
  {"id": "lex.en.200k.060659", "hw": "genus cinchona", "pos": "phrase", "ipa": "/ˈdʒiːnəs sɪŋˈkoʊnə/", "vi": "chi thực vật cây canh-ki-na"},
  {"id": "lex.en.200k.060660", "hw": "genus ovis", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈoʊvɪs/", "vi": "chi động vật họ cừu Ovis"},
  {"id": "lex.en.200k.060661", "hw": "genus senecio", "pos": "phrase", "ipa": "/ˈdʒiːnəs sɪˈniːʃioʊ/", "vi": "chi cây thảo dược cúc bạc Senecio"},
  {"id": "lex.en.200k.060662", "hw": "george washington goethals", "pos": "phrase", "ipa": "/dʒɔːrdʒ ˈwɑːʃɪŋtən ˈɡoʊθəlz/", "vi": "kỹ sư trưởng kênh Panama Goethals"},
  {"id": "lex.en.200k.060663", "hw": "ginkgo biloba", "pos": "phrase", "ipa": "/ˈɡɪŋkoʊ baɪˈloʊbə/", "vi": "cây bạch quả cổ đại lá hình quạt"},
  {"id": "lex.en.200k.060664", "hw": "giovanni francesco albani", "pos": "phrase", "ipa": "/dʒoʊˈvɑːni frænˈtʃɛskoʊ ælˈbɑːni/", "vi": "Giáo hoàng Công giáo Clement XI"},
  {"id": "lex.en.200k.060665", "hw": "hairy spurge", "pos": "phrase", "ipa": "/ˈhɛəri spɜːrdʒ/", "vi": "cây cỏ sữa có lông họ Thầu dầu"},
  {"id": "lex.en.200k.060666", "hw": "inverse secant", "pos": "phrase", "ipa": "/ɪnˈvɜːrs ˈsiːkənt/", "vi": "hàm lượng giác ngược cung arcsec"},
  {"id": "lex.en.200k.060667", "hw": "japanese barberry", "pos": "phrase", "ipa": "/ˌdʒæpəˈniːz ˈbɑːrbɛri/", "vi": "cây bụi cảnh hoàng liên gai Nhật"},
  {"id": "lex.en.200k.060668", "hw": "japanese spurge", "pos": "phrase", "ipa": "/ˌdʒæpəˈniːz spɜːrdʒ/", "vi": "cây phủ nền thường xanh Nhật Bản"},
  {"id": "lex.en.200k.060669", "hw": "jean chauvin", "pos": "phrase", "ipa": "/ʒɑ̃ː ʃoʊˈvæ̃ː/", "vi": "nhà cải cách tôn giáo Jean Calvin"},
  {"id": "lex.en.200k.060670", "hw": "jujube bush", "pos": "phrase", "ipa": "/ˈdʒuːdʒuːb bʊʃ/", "vi": "cây bụi táo tàu gai quả ngọt"},
  {"id": "lex.en.200k.060671", "hw": "karl menninger", "pos": "phrase", "ipa": "/kɑːrl ˈmɛnɪŋɡər/", "vi": "bác sĩ tâm thần Mỹ Karl Menninger"},
  {"id": "lex.en.200k.060672", "hw": "karl wernicke", "pos": "phrase", "ipa": "/kɑːrl ˈvɛərnɪkə/", "vi": "bác sĩ thần kinh học Karl Wernicke"},
  {"id": "lex.en.200k.060673", "hw": "lamaze method", "pos": "phrase", "ipa": "/ləˈmɑːz ˈmɛθəd/", "vi": "phương pháp thở sinh con tự nhiên"},
  {"id": "lex.en.200k.060674", "hw": "lente insulin", "pos": "phrase", "ipa": "/ˈlɛnteɪ ˈɪnsəlɪn/", "vi": "insulin tác dụng trung bình chậm"},
  {"id": "lex.en.200k.060675", "hw": "little brown myotis", "pos": "phrase", "ipa": "/ˈlɪtl braʊn maɪˈoʊtɪs/", "vi": "loài dơi nâu nhỏ ăn muỗi Bắc Mỹ"},
  {"id": "lex.en.200k.060676", "hw": "ogee arch", "pos": "phrase", "ipa": "/ˈoʊdʒiː ɑːrtʃ/", "vi": "vòm cong uốn lượn chữ S kiến trúc"},
  {"id": "lex.en.200k.060677", "hw": "osteogenic sarcoma", "pos": "phrase", "ipa": "/ˌɑːstiəˈdʒɛnɪk sɑːrˈkoʊmə/", "vi": "bệnh ung thư mô xương ác tính"},
  {"id": "lex.en.200k.060678", "hw": "petty spurge", "pos": "phrase", "ipa": "/ˈpɛti spɜːrdʒ/", "vi": "cây cỏ sữa nhỏ nhựa trắng độc"},
  {"id": "lex.en.200k.060679", "hw": "pinus glabra", "pos": "phrase", "ipa": "/ˈpaɪnəs ˈɡlæbrə/", "vi": "cây thông vỏ nhẵn vùng đông nam Mỹ"},
  {"id": "lex.en.200k.060680", "hw": "popliteal vein", "pos": "phrase", "ipa": "/ˌpɑːplɪˈtiːəl veɪn/", "vi": "tĩnh mạch khoeo chân sau đầu gối"},
  {"id": "lex.en.200k.060681", "hw": "prunella vulgaris", "pos": "phrase", "ipa": "/pruːˈnɛlə vʌlˈɡɛərɪs/", "vi": "cây hạ khô thảo hoa tím chữa bệnh"},
  {"id": "lex.en.200k.060682", "hw": "quercus virginiana", "pos": "phrase", "ipa": "/ˈkwɜːrkəs vərˌdʒɪniˈeɪnə/", "vi": "cây sồi tán rộng Virginia miền nam"},
  {"id": "lex.en.200k.060683", "hw": "rudolf karl virchow", "pos": "phrase", "ipa": "/ˈruːdɔːlf kɑːrl ˈvɪərkoʊ/", "vi": "cha đẻ bệnh lý học Rudolf Virchow"},
  {"id": "lex.en.200k.060684", "hw": "rudolf virchow", "pos": "phrase", "ipa": "/ˈruːdɔːlf ˈvɪərkoʊ/", "vi": "nhà bệnh học vĩ đại Rudolf Virchow"},
  {"id": "lex.en.200k.060685", "hw": "sergei rachmaninov", "pos": "phrase", "ipa": "/ˈsɛərɡeɪ rɑːkˈmɑːnɪnɔːf/", "vi": "nhạc sĩ dương cầm Nga Rachmaninov"},
  {"id": "lex.en.200k.060686", "hw": "serratus posterior inferior", "pos": "phrase", "ipa": "/səˈreɪtəs pɑːˈstɪəriər ɪnˈfɪriər/", "vi": "cơ răng cưa sau dưới kéo hạ sườn"},
  {"id": "lex.en.200k.060687", "hw": "skiffle group", "pos": "phrase", "ipa": "/ˈskɪfl ɡruːp/", "vi": "ban nhạc dân gian skiffle nước Anh"},
  {"id": "lex.en.200k.060688", "hw": "spiff up", "pos": "phrase", "ipa": "/spɪf ʌp/", "vi": "tút lại cho bảnh bao; dọn tươm tất"},
  {"id": "lex.en.200k.060689", "hw": "spurge family", "pos": "phrase", "ipa": "/spɜːrdʒ ˈfæməli/", "vi": "họ thực vật Thầu dầu Euphorbiaceae"},
  {"id": "lex.en.200k.060690", "hw": "sun spurge", "pos": "phrase", "ipa": "/sʌn spɜːrdʒ/", "vi": "cây cỏ sữa hướng dương nhựa độc"},
  {"id": "lex.en.200k.060691", "hw": "synchronic linguistics", "pos": "phrase", "ipa": "/sɪŋˈkrɑːnɪk lɪŋˈɡwɪstɪks/", "vi": "ngôn ngữ học đồng đại hiện thời"},
  {"id": "lex.en.200k.060692", "hw": "teff grass", "pos": "phrase", "ipa": "/tɛf ɡræs/", "vi": "cây ngũ cốc hạt nhỏ teff Ethiopia"},
  {"id": "lex.en.200k.060693", "hw": "tinea pedis", "pos": "phrase", "ipa": "/ˈtɪniə ˈpɛdɪs/", "vi": "bệnh nấm kẽ chân nước ăn chân"},
  {"id": "lex.en.200k.060694", "hw": "ulan bator", "pos": "phrase", "ipa": "/ˈuːlɑːn ˈbɑːtɔːr/", "vi": "thủ đô Ulaanbaatar của Mông Cổ"},
  {"id": "lex.en.200k.060695", "hw": "ursus americanus", "pos": "phrase", "ipa": "/ˈɜːrsəs əˌmɛrɪˈkeɪnəs/", "vi": "loài gấu đen rừng Bắc Mỹ"},
  {"id": "lex.en.200k.060696", "hw": "wild spurge", "pos": "phrase", "ipa": "/waɪld spɜːrdʒ/", "vi": "cây cỏ sữa dại mọc hoang ven đường"},
  {"id": "lex.en.200k.060697", "hw": "william claire menninger", "pos": "phrase", "ipa": "/ˈwɪljəm klɛər ˈmɛnɪŋɡər/", "vi": "bác sĩ tâm thần William Menninger"},
  {"id": "lex.en.200k.060698", "hw": "william menninger", "pos": "phrase", "ipa": "/ˈwɪljəm ˈmɛnɪŋɡər/", "vi": "bác sĩ tâm thần học Menninger"},
  {"id": "lex.en.200k.060699", "hw": "wood spurge", "pos": "phrase", "ipa": "/wʊd spɜːrdʒ/", "vi": "cây cỏ sữa rừng hoa xanh lục"},
  {"id": "lex.en.200k.060700", "hw": "yellowfin croaker", "pos": "phrase", "ipa": "/ˈjɛloʊfɪn ˈkroʊkər/", "vi": "loài cá đù vây vàng biển Thái Bình"},
  {"id": "lex.en.200k.060701", "hw": "acrostics", "pos": "noun", "ipa": "/əˈkrɔːstɪks/", "vi": "thơ khoáng thủ ghép vần đầu dòng"},
  {"id": "lex.en.200k.060702", "hw": "agrippinas", "pos": "noun", "ipa": "/ˌæɡrɪˈpaɪnəz/", "vi": "hoàng hậu La Mã cổ đại Agrippina"}
]

with open('scratch/b33_r02_raw_p2.json') as f:
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

with open('scratch/b33_r02_p2.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 2 Part 2 validated and written successfully.")
