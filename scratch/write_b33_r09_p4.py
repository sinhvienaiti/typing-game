import json

items = [
  {"id": "lex.en.200k.064303", "hw": "lunate bone", "pos": "phrase", "ipa": "/ˈluːneɪt boʊn/", "vi": "xương nguyệt hàng gần ở cổ tay"},
  {"id": "lex.en.200k.064304", "hw": "madame tussaud", "pos": "phrase", "ipa": "/məˈdæm tuːˈsoʊ/", "vi": "nghệ nhân tượng sáp Madame Tussaud"},
  {"id": "lex.en.200k.064305", "hw": "malignant pustule", "pos": "phrase", "ipa": "/məˈlɪɡnənt ˈpʌstʃuːl/", "vi": "mụn mủ ác tính bệnh than ngoài da"},
  {"id": "lex.en.200k.064306", "hw": "malus fusca", "pos": "phrase", "ipa": "/ˈmeɪləs ˈfʌskə/", "vi": "cây táo dại quả chua vùng Tây Mỹ"},
  {"id": "lex.en.200k.064307", "hw": "marie tussaud", "pos": "phrase", "ipa": "/məˈriː tuːˈsoʊ/", "vi": "bà chủ bảo tàng tượng sáp Tussaud"},
  {"id": "lex.en.200k.064308", "hw": "mcguffey eclectic readers", "pos": "phrase", "ipa": "/məˈɡʌfi ɪˈklɛktɪk ˈriːdərz/", "vi": "bộ sách giáo khoa tập đọc McGuffey"},
  {"id": "lex.en.200k.064309", "hw": "medial geniculate", "pos": "phrase", "ipa": "/ˈmiːdiəl dʒəˈnɪkjəlɪt/", "vi": "nhân thể gối trong xử lý thính giác"},
  {"id": "lex.en.200k.064310", "hw": "medial geniculate body", "pos": "phrase", "ipa": "/ˈmiːdiəl dʒəˈnɪkjəlɪt ˈbɑːdi/", "vi": "thể gối trong vùng đồi thị não"},
  {"id": "lex.en.200k.064311", "hw": "modest mussorgsky", "pos": "phrase", "ipa": "/ˈmɑːdɪst mʊˈsɔːrɡski/", "vi": "nhà soạn nhạc Nga Mussorgsky"},
  {"id": "lex.en.200k.064312", "hw": "musculus pectoralis", "pos": "phrase", "ipa": "/ˈmʌskjʊləs ˌpɛktəˈrælɪs/", "vi": "khối cơ ngực trước lồng ngực"},
  {"id": "lex.en.200k.064313", "hw": "musculus pectoralis major", "pos": "phrase", "ipa": "/ˈmʌskjʊləs ˌpɛktəˈrælɪs ˈmeɪdʒər/", "vi": "cơ ngực lớn vùng thành ngực trước"},
  {"id": "lex.en.200k.064314", "hw": "musculus pectoralis minor", "pos": "phrase", "ipa": "/ˈmʌskjʊləs ˌpɛktəˈrælɪs ˈmaɪnər/", "vi": "cơ ngực bé nằm dưới cơ ngực lớn"},
  {"id": "lex.en.200k.064315", "hw": "optic chiasm", "pos": "phrase", "ipa": "/ˈɑːptɪk ˈkaɪæzəm/", "vi": "giao thoa dây thần kinh thị giác"},
  {"id": "lex.en.200k.064316", "hw": "opuntia cholla", "pos": "phrase", "ipa": "/oʊˈpʌntiə ˈtʃɔɪə/", "vi": "xương rồng thân trụ có gai cholla"},
  {"id": "lex.en.200k.064317", "hw": "pieris japonica", "pos": "phrase", "ipa": "/ˈpaɪərɪs dʒəˈpɑːnɪkə/", "vi": "cây bụi hoa chuông Nhật Bản Pieris"},
  {"id": "lex.en.200k.064318", "hw": "piltdown man", "pos": "phrase", "ipa": "/ˈpɪltdaʊn mæn/", "vi": "hóa thạch giả người vượn Piltdown"},
  {"id": "lex.en.200k.064319", "hw": "pouched mole", "pos": "phrase", "ipa": "/paʊtʃt moʊl/", "vi": "chuột chũi có túi vàng sa mạc Úc"},
  {"id": "lex.en.200k.064320", "hw": "pouched mouse", "pos": "phrase", "ipa": "/paʊtʃt maʊs/", "vi": "chuột có túi nhỏ ăn côn trùng Úc"},
  {"id": "lex.en.200k.064321", "hw": "pouched rat", "pos": "phrase", "ipa": "/paʊtʃt ræt/", "vi": "chuột túi má lớn châu Phi và Mỹ"},
  {"id": "lex.en.200k.064322", "hw": "purulent pleurisy", "pos": "phrase", "ipa": "/ˈpjʊrələnt ˈplʊrəsi/", "vi": "viêm màng phổi có mủ tràn khoang"},
  {"id": "lex.en.200k.064323", "hw": "richard trevithick", "pos": "phrase", "ipa": "/ˈrɪtʃərd ˈtrɛvəθɪk/", "vi": "nhà phát minh đầu máy hơi nước Anh"},
  {"id": "lex.en.200k.064324", "hw": "rough bindweed", "pos": "phrase", "ipa": "/rʌf ˈbaɪndwiːd/", "vi": "dây leo gai kim cang Địa Trung Hải"},
  {"id": "lex.en.200k.064325", "hw": "saudi arabian riyal", "pos": "phrase", "ipa": "/ˈsaʊdi əˈreɪbiən riˈɑːl/", "vi": "đồng tiền riyal của Ả Rập Xê Út"},
  {"id": "lex.en.200k.064326", "hw": "sergei pavlovich diaghilev", "pos": "phrase", "ipa": "/ˈsɛrɡeɪ ˈpɑːvləvɪtʃ diˈɑːɡəlɛf/", "vi": "ông bầu đoàn múa Nga Diaghilev"},
  {"id": "lex.en.200k.064327", "hw": "sholem asch", "pos": "phrase", "ipa": "/ˈʃoʊləm æʃ/", "vi": "nhà văn tiếng Yiddish Sholem Asch"},
  {"id": "lex.en.200k.064328", "hw": "spoonbill catfish", "pos": "phrase", "ipa": "/ˈspuːnbɪl ˈkætfɪʃ/", "vi": "cá tầm mỏ mái chèo Bắc Mỹ"},
  {"id": "lex.en.200k.064329", "hw": "striped killifish", "pos": "phrase", "ipa": "/straɪpt ˈkɪliˌfɪʃ/", "vi": "cá tuế sọc ven biển Đại Tây Dương"},
  {"id": "lex.en.200k.064330", "hw": "submandibular gland", "pos": "phrase", "ipa": "/ˌsʌbmænˈdɪbjələr ɡlænd/", "vi": "tuyến nước bọt dưới hàm tiết dịch"},
  {"id": "lex.en.200k.064331", "hw": "teilhard de chardin", "pos": "phrase", "ipa": "/teɪˈjɑːr də ʃɑːrˈdæn/", "vi": "linh mục cổ sinh vật học Chardin"},
  {"id": "lex.en.200k.064332", "hw": "tilia americana", "pos": "phrase", "ipa": "/ˈtɪliə əˌmɛrɪˈkænə/", "vi": "cây đoạn gỗ nhẹ Bắc Mỹ hoa thơm"},
  {"id": "lex.en.200k.064333", "hw": "titus lucretius carus", "pos": "phrase", "ipa": "/ˈtaɪtəs luˈkriːʃəs ˈkɛrəs/", "vi": "nhà thơ triết gia La Mã Lucretius"},
  {"id": "lex.en.200k.064334", "hw": "tsuga canadensis", "pos": "phrase", "ipa": "/ˈtsuːɡə ˌkænəˈdɛnsɪs/", "vi": "cây thông thiết sam Canada Bắc Mỹ"},
  {"id": "lex.en.200k.064335", "hw": "vena hepatica", "pos": "phrase", "ipa": "/ˈviːnə hɪˈpætɪkə/", "vi": "tĩnh mạch gan đổ vào tĩnh mạch chủ"},
  {"id": "lex.en.200k.064336", "hw": "vinca rosea", "pos": "phrase", "ipa": "/ˈvɪŋkə ˈroʊziə/", "vi": "cây hoa dừa cạn hồng làm dược liệu"},
  {"id": "lex.en.200k.064337", "hw": "yellow salsify", "pos": "phrase", "ipa": "/ˈjɛloʊ ˈsælsəfi/", "vi": "cây rễ cúc hoa vàng quả lông bay"},
  {"id": "lex.en.200k.064338", "hw": "zinnia grandiflora", "pos": "phrase", "ipa": "/ˈzɪniə ˌɡrændɪˈflɔːrə/", "vi": "cây cúc lá nhám hoa vàng Bắc Mỹ"},
  {"id": "lex.en.200k.064339", "hw": "akens", "pos": "noun", "ipa": "/ˈɑːkənz/", "vi": "thành phố cổ Aachen miền tây Đức"},
  {"id": "lex.en.200k.064340", "hw": "amblyopias", "pos": "noun", "ipa": "/ˌæmbliˈoʊpiəz/", "vi": "chứng nhược thị giảm thị lực mắt"},
  {"id": "lex.en.200k.064341", "hw": "analectses", "pos": "noun", "ipa": "/ˈænəˌlɛktsɪz/", "vi": "tuyển tập trích đoạn văn triết học"},
  {"id": "lex.en.200k.064342", "hw": "anaphoras", "pos": "noun", "ipa": "/əˈnæfərəz/", "vi": "phép điệp ngữ đầu câu; hồi chỉ từ"},
  {"id": "lex.en.200k.064343", "hw": "angases", "pos": "noun", "ipa": "/æŋˈɡɑːsɪz/", "vi": "người và ngôn ngữ Angas ở Nigeria"},
  {"id": "lex.en.200k.064344", "hw": "annams", "pos": "noun", "ipa": "/ˈænæmz/", "vi": "tên lịch sử miền Trung An Nam xưa"},
  {"id": "lex.en.200k.064345", "hw": "arresters", "pos": "noun", "ipa": "/əˈrɛstərz/", "vi": "van chống sét; cáp hãm đà máy bay"},
  {"id": "lex.en.200k.064346", "hw": "auguries", "pos": "noun", "ipa": "/ˈɔːɡjəriz/", "vi": "điềm báo trước; thuật bói điềm chim"},
  {"id": "lex.en.200k.064347", "hw": "baluchis", "pos": "noun", "ipa": "/bəˈluːtʃiz/", "vi": "người dân và tiếng Balochi Pakistan"},
  {"id": "lex.en.200k.064348", "hw": "batholiths", "pos": "noun", "ipa": "/ˈbæθəlɪθs/", "vi": "khối đá xâm nhập sâu lớn batholith"},
  {"id": "lex.en.200k.064349", "hw": "beograds", "pos": "noun", "ipa": "/biˈɑːɡrɑːdz/", "vi": "thủ đô Belgrade của nước Serbia"},
  {"id": "lex.en.200k.064350", "hw": "birefringences", "pos": "noun", "ipa": "/ˌbaɪrɪˈfrɪndʒənsɪz/", "vi": "hiện tượng lưỡng chiết ánh sáng"},
  {"id": "lex.en.200k.064351", "hw": "blaxploitations", "pos": "noun", "ipa": "/ˌblæksplɔɪˈteɪʃənz/", "vi": "dòng phim hành động người da đen"},
  {"id": "lex.en.200k.064352", "hw": "bowheads", "pos": "noun", "ipa": "/ˈboʊhɛdz/", "vi": "cá voi đầu cong sống vùng Bắc Cực"},
  {"id": "lex.en.200k.064353", "hw": "brattled", "pos": "verb", "ipa": "/ˈbrætəld/", "vi": "đã kêu lách cách; đã nổ lốp bốp"},
  {"id": "lex.en.200k.064354", "hw": "brattles", "pos": "verb", "ipa": "/ˈbrætəlz/", "vi": "kêu lạch cạch ồn ào; chạy vội vã"},
  {"id": "lex.en.200k.064355", "hw": "brattling", "pos": "verb", "ipa": "/ˈbrætəlɪŋ/", "vi": "đang kêu lạch cạch ầm ĩ liên hồi"},
  {"id": "lex.en.200k.064356", "hw": "brunelleschis", "pos": "noun", "ipa": "/ˌbruːnəˈlɛskiz/", "vi": "kiến trúc sư Ý cổ Brunelleschi"},
  {"id": "lex.en.200k.064357", "hw": "calami", "pos": "noun", "ipa": "/ˈkæləmaɪ/", "vi": "cây song mây nhiệt đới; bút sậy cổ"},
  {"id": "lex.en.200k.064358", "hw": "calamuses", "pos": "noun", "ipa": "/ˈkæləməsɪz/", "vi": "cây thủy xương bồ; cây song mây"},
  {"id": "lex.en.200k.064359", "hw": "carotherses", "pos": "noun", "ipa": "/kəˈrʌðərzɪz/", "vi": "kỹ sư phát minh ni-lông Carothers"},
  {"id": "lex.en.200k.064360", "hw": "centerfields", "pos": "noun", "ipa": "/ˈsɛntərfiːldz/", "vi": "vùng giữa sân ngoài môn bóng chày"},
  {"id": "lex.en.200k.064361", "hw": "chelates", "pos": "noun", "ipa": "/ˈkiːleɪts/", "vi": "phức chất càng kim loại chelat"},
  {"id": "lex.en.200k.064362", "hw": "chelating", "pos": "verb", "ipa": "/ˈkiːleɪtɪŋ/", "vi": "đang tạo phức chelat gắp kim loại"},
  {"id": "lex.en.200k.064363", "hw": "chlorites", "pos": "noun", "ipa": "/ˈklɔːraɪts/", "vi": "muối clorit; khoáng sét xanh lục"},
  {"id": "lex.en.200k.064364", "hw": "choosers", "pos": "noun", "ipa": "/ˈtʃuːzərz/", "vi": "người đưa ra lựa chọn quyết định"},
  {"id": "lex.en.200k.064365", "hw": "cockatiels", "pos": "noun", "ipa": "/ˌkɑːkəˈtiːlz/", "vi": "vẹt mào má hồng Úc nuôi làm cảnh"},
  {"id": "lex.en.200k.064366", "hw": "copepods", "pos": "noun", "ipa": "/ˈkoʊpəˌpɑːdz/", "vi": "giáp xác chân chèo li ti phù du"},
  {"id": "lex.en.200k.064367", "hw": "cosmologists", "pos": "noun", "ipa": "/kɑːzˈmɑːlədʒɪsts/", "vi": "nhà khoa học nghiên cứu vũ trụ học"},
  {"id": "lex.en.200k.064368", "hw": "croupiers", "pos": "noun", "ipa": "/ˈkruːpiərz/", "vi": "người hồ lì chia bài tại sòng bạc"},
  {"id": "lex.en.200k.064369", "hw": "curacies", "pos": "noun", "ipa": "/ˈkjʊrəsɪz/", "vi": "chức vụ giáo sĩ phụ tá giáo xứ"},
  {"id": "lex.en.200k.064370", "hw": "cyberwars", "pos": "noun", "ipa": "/ˈsaɪbərwɔːrz/", "vi": "cuộc chiến tranh tấn công mạng"},
  {"id": "lex.en.200k.064371", "hw": "daubers", "pos": "noun", "ipa": "/ˈdɔːbərz/", "vi": "họa sĩ vẽ tồi; que bôi mực dấu"},
  {"id": "lex.en.200k.064372", "hw": "decarboxylations", "pos": "noun", "ipa": "/ˌdiːkɑːrˌbɑːksəˈleɪʃənz/", "vi": "phản ứng tách loại nhóm cacboxyl"},
  {"id": "lex.en.200k.064373", "hw": "denotations", "pos": "noun", "ipa": "/ˌdiːnoʊˈteɪʃənz/", "vi": "nghĩa đen trực tiếp; sự biểu thị rõ"},
  {"id": "lex.en.200k.064374", "hw": "densifications", "pos": "noun", "ipa": "/ˌdɛnsəfəˈkeɪʃənz/", "vi": "sự nén chặt làm tăng mật độ khối"},
  {"id": "lex.en.200k.064375", "hw": "dramamines", "pos": "noun", "ipa": "/ˈdræməˌmiːnz/", "vi": "thuốc chống say tàu xe Dramamine"},
  {"id": "lex.en.200k.064376", "hw": "drecks", "pos": "noun", "ipa": "/drɛks/", "vi": "đồ rác rưởi rẻ tiền vô giá trị"},
  {"id": "lex.en.200k.064377", "hw": "dualists", "pos": "noun", "ipa": "/ˈduːəlɪsts/", "vi": "người theo học thuyết nhị nguyên"},
  {"id": "lex.en.200k.064378", "hw": "edams", "pos": "noun", "ipa": "/ˈiːdəmz/", "vi": "phô mai tròn sáp đỏ Edam Hà Lan"},
  {"id": "lex.en.200k.064379", "hw": "episiotomies", "pos": "noun", "ipa": "/ɪˌpiːziˈɑːtəmiz/", "vi": "rạch tầng sinh môn hỗ trợ sinh nở"},
  {"id": "lex.en.200k.064380", "hw": "espoos", "pos": "noun", "ipa": "/ˈɛspoʊz/", "vi": "thành phố công nghệ Espoo Phần Lan"},
  {"id": "lex.en.200k.064381", "hw": "exercisers", "pos": "noun", "ipa": "/ˈɛksərˌsaɪzərz/", "vi": "máy tập thể dục; người tập luyện"},
  {"id": "lex.en.200k.064382", "hw": "exocrines", "pos": "noun", "ipa": "/ˈɛksəkrɪnz/", "vi": "tuyến ngoại tiết tiết qua ống dẫn"},
  {"id": "lex.en.200k.064383", "hw": "fabianas", "pos": "noun", "ipa": "/ˌfæbiˈɑːnəz/", "vi": "chi cây bụi hoa nhỏ Fabiana Nam Mỹ"},
  {"id": "lex.en.200k.064384", "hw": "falloffs", "pos": "noun", "ipa": "/ˈfɔːlɔːfs/", "vi": "sự suy giảm sụt thấp bất ngờ"},
  {"id": "lex.en.200k.064385", "hw": "fenlands", "pos": "noun", "ipa": "/ˈfɛnlændz/", "vi": "vùng đất trũng đầm lầy tháo nước"},
  {"id": "lex.en.200k.064386", "hw": "fixatives", "pos": "noun", "ipa": "/ˈfɪksətɪvz/", "vi": "chất giữ màu ảnh; chất định hương"},
  {"id": "lex.en.200k.064387", "hw": "flashovers", "pos": "noun", "ipa": "/ˈflæʃˌoʊvərz/", "vi": "phóng điện hồ quang; đám cháy bùng"},
  {"id": "lex.en.200k.064388", "hw": "fleered", "pos": "verb", "ipa": "/flɪərd/", "vi": "đã cười khẩy nhạo báng khinh bỉ"},
  {"id": "lex.en.200k.064389", "hw": "fleers", "pos": "noun", "ipa": "/flɪərz/", "vi": "người bỏ chạy trốn; lời cười khẩy"},
  {"id": "lex.en.200k.064390", "hw": "flowerbeds", "pos": "noun", "ipa": "/ˈflaʊərˌbɛdz/", "vi": "bồn hoa luống đất trồng hoa cảnh"},
  {"id": "lex.en.200k.064391", "hw": "fundaments", "pos": "noun", "ipa": "/ˈfʌndəmənts/", "vi": "nền tảng cơ bản; vùng hậu môn mông"},
  {"id": "lex.en.200k.064392", "hw": "galaxes", "pos": "noun", "ipa": "/ˈɡeɪlæksɪz/", "vi": "cây lá tim hoa trắng Bắc Mỹ galax"},
  {"id": "lex.en.200k.064393", "hw": "handsprings", "pos": "noun", "ipa": "/ˈhændsprɪŋz/", "vi": "động tác chống tay bật lộn người"},
  {"id": "lex.en.200k.064394", "hw": "haseks", "pos": "noun", "ipa": "/ˈhɑːʃɛks/", "vi": "nhà văn trào phúng Séc Hašek"},
  {"id": "lex.en.200k.064395", "hw": "hirers", "pos": "noun", "ipa": "/ˈhaɪərərz/", "vi": "nhà tuyển dụng nhân sự; người thuê"},
  {"id": "lex.en.200k.064396", "hw": "hollyhocks", "pos": "noun", "ipa": "/ˈhɑːliˌhɑːks/", "vi": "cây hoa thục quỳ thân cao rực rỡ"},
  {"id": "lex.en.200k.064397", "hw": "homoeopathies", "pos": "noun", "ipa": "/ˌhoʊmiˈɑːpəθiz/", "vi": "y học vi lượng đồng căn (viết Anh)"},
  {"id": "lex.en.200k.064398", "hw": "hydrologists", "pos": "noun", "ipa": "/haɪˈdrɑːlədʒɪsts/", "vi": "nhà khoa học thủy văn nguồn nước"},
  {"id": "lex.en.200k.064399", "hw": "ilmenites", "pos": "noun", "ipa": "/ˈɪlməˌnaɪts/", "vi": "quặng khoáng vật sắt titan ilmenit"},
  {"id": "lex.en.200k.064400", "hw": "indomethacins", "pos": "noun", "ipa": "/ˌɪndoʊˈmɛθəsɪnz/", "vi": "thuốc kháng viêm indomethacin"},
  {"id": "lex.en.200k.064401", "hw": "intercalations", "pos": "noun", "ipa": "/ɪnˌtɜːrkəˈleɪʃənz/", "vi": "sự chèn ngày nhuận; xen lớp phân tử"},
  {"id": "lex.en.200k.064402", "hw": "interweaves", "pos": "verb", "ipa": "/ˌɪntərˈwiːvz/", "vi": "đan xen bện chặt lồng ghép vào nhau"}
]

with open('scratch/b33_r09_raw_p4.json') as f:
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

with open('scratch/b33_r09_p4.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r09_p4.json OK")
