import json

data = [
  {"id": "lex.en.200k.034102", "hw": "lushes", "pos": "noun", "ipa": "/ˈlʌʃɪz/", "vi": "những kẻ nghiện rượu say xỉn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034103", "hw": "lushest", "pos": "adj", "ipa": "/ˈlʌʃɪst/", "vi": "xanh tươi tốt nhất; um tùm nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034104", "hw": "mbas", "pos": "noun", "ipa": "/ˌɛmbiːˈeɪz/", "vi": "bằng thạc sĩ quản trị kinh doanh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034105", "hw": "megs", "pos": "noun", "ipa": "/mɛɡz/", "vi": "đơn vị mê-ga-bai; triệu byte", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034106", "hw": "meltdowns", "pos": "noun", "ipa": "/ˈmɛltˌdaʊnz/", "vi": "sự tan chảy hạt nhân; khủng hoảng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034107", "hw": "messiahs", "pos": "noun", "ipa": "/məˈsaɪəz/", "vi": "đấng cứu thế; đấng Mê-si-a", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034108", "hw": "meteors", "pos": "noun", "ipa": "/ˈmitiərz/", "vi": "những vệt sao băng rơi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034109", "hw": "nus", "pos": "noun", "ipa": "/nuːz/", "vi": "chữ cái Hy Lạp nu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034110", "hw": "obstructions", "pos": "noun", "ipa": "/əbˈstrʌkʃənz/", "vi": "vật cản trở; sự gây ách tắc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034111", "hw": "odysseys", "pos": "noun", "ipa": "/ˈɑdɪsiz/", "vi": "những chuyến phiêu lưu gian truân", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034112", "hw": "outsiders", "pos": "noun", "ipa": "/ˌaʊtˈsaɪdərz/", "vi": "người ngoài cuộc; kẻ lạc lõng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034113", "hw": "phis", "pos": "noun", "ipa": "/faɪz/", "vi": "chữ cái Hy Lạp phi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034114", "hw": "plums", "pos": "noun", "ipa": "/plʌmz/", "vi": "những quả mận ngọt mọng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034115", "hw": "plurals", "pos": "noun", "ipa": "/ˈplʊrəlz/", "vi": "các dạng số nhiều ngữ pháp", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034116", "hw": "poes", "pos": "noun", "ipa": "/poʊz/", "vi": "nhà văn Edgar Allan Poe", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034117", "hw": "portrayals", "pos": "noun", "ipa": "/pɔrˈtreɪəlz/", "vi": "sự khắc họa; chân dung miêu tả", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034118", "hw": "rajs", "pos": "noun", "ipa": "/rɑːdʒz/", "vi": "thời kỳ đô hộ của Anh tại Ấn Độ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034119", "hw": "replicated", "pos": "verb", "ipa": "/ˈrɛplɪkeɪtɪd/", "vi": "đã nhân bản; đã tái tạo lại", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034120", "hw": "replicates", "pos": "verb", "ipa": "/ˈrɛplɪkeɪts/", "vi": "nhân bản; sao chép tái tạo lại", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034121", "hw": "replicating", "pos": "verb", "ipa": "/ˈrɛplɪkeɪtɪŋ/", "vi": "đang nhân bản; quá trình tái tạo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034122", "hw": "retaliations", "pos": "noun", "ipa": "/rɪˌtæliˈeɪʃənz/", "vi": "những đòn đáp trả trả đũa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034123", "hw": "rfs", "pos": "noun", "ipa": "/ˌɑːrˈɛfs/", "vi": "tần số sóng vô tuyến điện RF", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034124", "hw": "rooftops", "pos": "noun", "ipa": "/ˈruːftɑps/", "vi": "những tầng mái nhà ngắm cảnh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034125", "hw": "rvs", "pos": "noun", "ipa": "/ˌɑːrˈviːz/", "vi": "xe nhà lưu động du lịch RV", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034126", "hw": "sedans", "pos": "noun", "ipa": "/sɪˈdænz/", "vi": "dòng xe ô tô 4 chỗ sedan", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034127", "hw": "sitcoms", "pos": "noun", "ipa": "/ˈsɪtkɑmz/", "vi": "phim hài kịch tình huống sitcom", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034128", "hw": "spoilers", "pos": "noun", "ipa": "/ˈspɔɪlərz/", "vi": "tiết lộ nội dung phim; cánh gió", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034129", "hw": "telegrams", "pos": "noun", "ipa": "/ˈtɛləɡræmz/", "vi": "những bức điện tín gửi đi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034130", "hw": "ulsters", "pos": "noun", "ipa": "/ˈʌlstərz/", "vi": "áo choàng dài mùa đông Ulster", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034131", "hw": "unescos", "pos": "noun", "ipa": "/juːˈnɛskoʊz/", "vi": "tổ chức UNESCO Liên Hợp Quốc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034132", "hw": "wordings", "pos": "noun", "ipa": "/ˈwɜrdɪŋz/", "vi": "cách dùng từ ngữ văn phong", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034133", "hw": "absentee ballot", "pos": "phrase", "ipa": "", "vi": "phiếu bầu cử gửi từ xa vắng mặt", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034134", "hw": "adjutant general", "pos": "phrase", "ipa": "", "vi": "viên tướng tổng trợ lý hành chính", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034135", "hw": "arterial blood gases", "pos": "phrase", "ipa": "", "vi": "khí máu động mạch phân tích", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034136", "hw": "bamboo fern", "pos": "phrase", "ipa": "", "vi": "dương xỉ thân đốt như tre", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034137", "hw": "bavarian blue", "pos": "phrase", "ipa": "", "vi": "phô mai vân mốc xanh Bavaria", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034138", "hw": "black hickory", "pos": "phrase", "ipa": "", "vi": "cây mại châu đen Bắc Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034139", "hw": "blackjack oak", "pos": "phrase", "ipa": "", "vi": "cây sồi đen lá rộng mọc cằn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034140", "hw": "blood kinship", "pos": "phrase", "ipa": "", "vi": "quan hệ huyết thống ruột thịt", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034141", "hw": "blood transfusion", "pos": "phrase", "ipa": "", "vi": "thủ thuật y tế truyền máu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034142", "hw": "brandy sling", "pos": "phrase", "ipa": "", "vi": "thức uống rượu brandy pha chanh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034143", "hw": "bridal wreath", "pos": "phrase", "ipa": "", "vi": "cây hoa mẫu đơn trắng kết chùm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034144", "hw": "brook thistle", "pos": "phrase", "ipa": "", "vi": "cây kế gai tím mọc ven suối", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034145", "hw": "brownish yellow", "pos": "phrase", "ipa": "", "vi": "gam màu vàng ánh nâu hổ phách", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034146", "hw": "calcium carbonate", "pos": "phrase", "ipa": "", "vi": "muối đá vôi canxi cacbonat", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034147", "hw": "california quail", "pos": "phrase", "ipa": "", "vi": "chim cút mào bang California", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034148", "hw": "cane blight", "pos": "phrase", "ipa": "", "vi": "bệnh cháy khô thân cây mía", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034149", "hw": "carbohydrate loading", "pos": "phrase", "ipa": "", "vi": "chế độ nạp tinh bột dự trữ carbo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034150", "hw": "cascade transformer", "pos": "phrase", "ipa": "", "vi": "máy biến áp cao thế ghép tầng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034151", "hw": "castor bean", "pos": "phrase", "ipa": "", "vi": "hạt thầu dầu ép lấy dầu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034152", "hw": "celery cabbage", "pos": "phrase", "ipa": "", "vi": "rau cải thảo cuộn búp dài", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034153", "hw": "centre of flotation", "pos": "phrase", "ipa": "", "vi": "tâm nổi diện tích mớn nước", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034154", "hw": "cervical glands", "pos": "phrase", "ipa": "", "vi": "tuyến tiết nhầy cổ tử cung", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034155", "hw": "contextual definition", "pos": "phrase", "ipa": "", "vi": "định nghĩa từ theo ngữ cảnh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034156", "hw": "cookery book", "pos": "phrase", "ipa": "", "vi": "sách hướng dẫn nấu ăn gia đình", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034157", "hw": "cottage tulip", "pos": "phrase", "ipa": "", "vi": "hoa tulip vườn muộn châu Âu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034158", "hw": "crab nebula", "pos": "phrase", "ipa": "", "vi": "tinh vân Con Cua M1 vũ trụ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034159", "hw": "cuckoo bread", "pos": "phrase", "ipa": "", "vi": "cây chua me đất hoa trắng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034160", "hw": "cuckoo clock", "pos": "phrase", "ipa": "", "vi": "chiếc đồng hồ chim cu gáy", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034161", "hw": "cuckoo flower", "pos": "phrase", "ipa": "", "vi": "cây rau sương hoa đồng nội", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034162", "hw": "cyril burt", "pos": "phrase", "ipa": "", "vi": "nhà tâm lý học Cyril Burt (Anh)", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034163", "hw": "davy lamp", "pos": "phrase", "ipa": "", "vi": "đèn an toàn thợ mỏ Davy", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034164", "hw": "delusions of persecution", "pos": "phrase", "ipa": "", "vi": "chứng hoang tưởng bị hại truy sát", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034165", "hw": "digestive gland", "pos": "phrase", "ipa": "", "vi": "tuyến tiết dịch tiêu hóa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034166", "hw": "doppler effect", "pos": "phrase", "ipa": "", "vi": "hiệu ứng biến đổi tần số Doppler", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034167", "hw": "dormitory room", "pos": "phrase", "ipa": "", "vi": "phòng ngủ tập thể ký túc xá", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034168", "hw": "duplex apartment", "pos": "phrase", "ipa": "", "vi": "căn hộ thông hai tầng hiện đại", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034169", "hw": "exchange transfusion", "pos": "phrase", "ipa": "", "vi": "thay máu toàn phần điều trị", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034170", "hw": "flotation device", "pos": "phrase", "ipa": "", "vi": "thiết bị nổi cứu sinh trên biển", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034171", "hw": "grub out", "pos": "phrase", "ipa": "", "vi": "đào bới tận gốc cây phế thải", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034172", "hw": "grub street", "pos": "phrase", "ipa": "", "vi": "giới văn sĩ viết thuê kiếm sống", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034173", "hw": "grub up", "pos": "phrase", "ipa": "", "vi": "đào xới nhổ bật rễ cây", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034174", "hw": "halo blight", "pos": "phrase", "ipa": "", "vi": "bệnh đốm quầng vi khuẩn hại lá", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034175", "hw": "hang gliding", "pos": "phrase", "ipa": "", "vi": "môn thể thao dù lượn diều bay", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034176", "hw": "hartford fern", "pos": "phrase", "ipa": "", "vi": "dương xỉ leo Hartford Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034177", "hw": "hasty pudding", "pos": "phrase", "ipa": "", "vi": "cháo ngô nấu bột ăn nóng vội", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034178", "hw": "honduras mahogany", "pos": "phrase", "ipa": "", "vi": "gỗ đào hoa tâm Honduras", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034179", "hw": "hubble law", "pos": "phrase", "ipa": "", "vi": "định luật giãn nở vũ trụ Hubble", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034180", "hw": "human reproductive cloning", "pos": "phrase", "ipa": "", "vi": "nhân bản vô tính sinh sản người", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034181", "hw": "hydrated oxide", "pos": "phrase", "ipa": "", "vi": "hợp chất ôxít ngậm nước", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034182", "hw": "incline bench press", "pos": "phrase", "ipa": "", "vi": "bài tập đẩy tạ đòn ghế dốc lên", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034183", "hw": "internal auditory vein", "pos": "phrase", "ipa": "", "vi": "tĩnh mạch thính giác trong sọ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034184", "hw": "intestinal obstruction", "pos": "phrase", "ipa": "", "vi": "hội chứng tắc ruột cơ học", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034185", "hw": "jewel casket", "pos": "phrase", "ipa": "", "vi": "tráp đựng trang sức châu báu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034186", "hw": "johann strauss", "pos": "phrase", "ipa": "", "vi": "nhạc sĩ vĩ đại Johann Strauss (Áo)", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034187", "hw": "lake eyre", "pos": "phrase", "ipa": "", "vi": "hồ nước mặn Eyre ở nước Úc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034188", "hw": "laurence olivier", "pos": "phrase", "ipa": "", "vi": "diễn viên kịch Laurence Olivier", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034189", "hw": "leading astray", "pos": "phrase", "ipa": "", "vi": "dụ dỗ làm lầm đường lạc lối", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034190", "hw": "left atrium", "pos": "phrase", "ipa": "", "vi": "buồng tâm nhĩ trái của tim", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034191", "hw": "leland stanford", "pos": "phrase", "ipa": "", "vi": "nhà sáng lập Leland Stanford", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034192", "hw": "leonardo da vinci", "pos": "phrase", "ipa": "", "vi": "danh họa thiên tài Da Vinci (Ý)", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034193", "hw": "leroy robert paige", "pos": "phrase", "ipa": "", "vi": "cầu thủ ném bóng Satchel Paige", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034194", "hw": "lymph node", "pos": "phrase", "ipa": "", "vi": "hạch bạch huyết bảo vệ cơ thể", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034195", "hw": "market capitalization", "pos": "phrase", "ipa": "", "vi": "giá trị vốn hóa toàn thị trường", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034196", "hw": "masking paper", "pos": "phrase", "ipa": "", "vi": "giấy dán che chắn khi sơn xịt", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034197", "hw": "masking piece", "pos": "phrase", "ipa": "", "vi": "tấm vách phông che hậu trường", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034198", "hw": "mercury barometer", "pos": "phrase", "ipa": "", "vi": "khí áp kế cột thủy ngân chuẩn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034199", "hw": "midwestern united states", "pos": "phrase", "ipa": "", "vi": "khu vực Trung Tây nước Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034200", "hw": "mink coat", "pos": "phrase", "ipa": "", "vi": "chiếc áo khoác lông chồn quý", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.034201", "hw": "mountain quail", "pos": "phrase", "ipa": "", "vi": "loài chim cút mào núi Bắc Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
]

ALLOWED_POS = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}

assert len(data) == 100
for i, item in enumerate(data):
    expected_id = f"lex.en.200k.{34102 + i:06d}"
    assert item["id"] == expected_id, f"ID error: {item['id']} != {expected_id}"
    assert item["pos"] in ALLOWED_POS, f"POS error: {item['pos']}"
    assert item["status"] == "reviewed"
    assert len(item["vi"]) <= 35, f"VI length error {len(item['vi'])} > 35 for {item['id']}: {item['vi']}"
    hw = item["hw"]
    ipa = item["ipa"]
    if " " not in hw:
        assert ipa.startswith("/") and ipa.endswith("/") and len(ipa) > 2, f"IPA error for {hw}: {ipa}"
        assert not ipa.startswith("/ ") and not ipa.endswith(" /"), f"IPA spacing error for {hw}: {ipa}"

with open("scratch/b27_r09_p2.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully validated and wrote 100 items to scratch/b27_r09_p2.json")
