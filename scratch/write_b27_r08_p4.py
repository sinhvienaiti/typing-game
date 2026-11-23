import json

data = [
  {"id": "lex.en.200k.033802", "hw": "dust wrapper", "pos": "phrase", "ipa": "", "vi": "bìa bọc sách chống bụi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033803", "hw": "egyptian vulture", "pos": "phrase", "ipa": "", "vi": "kền kền Ai Cập mỏ vàng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033804", "hw": "emmett kelly", "pos": "phrase", "ipa": "", "vi": "nghệ sĩ hề Emmett Kelly", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033805", "hw": "evergreen thorn", "pos": "phrase", "ipa": "", "vi": "cây gai gai thường xanh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033806", "hw": "fern genus", "pos": "phrase", "ipa": "", "vi": "chi thực vật dương xỉ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033807", "hw": "flanders poppy", "pos": "phrase", "ipa": "", "vi": "hoa anh túc tưởng niệm đỏ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033808", "hw": "flannel leaf", "pos": "phrase", "ipa": "", "vi": "cây thảo lá nhung tơ mềm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033809", "hw": "fragrant water lily", "pos": "phrase", "ipa": "", "vi": "hoa súng trắng ngát hương", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033810", "hw": "frozen custard", "pos": "phrase", "ipa": "", "vi": "kem trứng sữa đông lạnh dẻo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033811", "hw": "gabriel daniel fahrenheit", "pos": "phrase", "ipa": "", "vi": "nhà vật lý Daniel Fahrenheit", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033812", "hw": "gastric artery", "pos": "phrase", "ipa": "", "vi": "động mạch cung cấp dạ dày", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033813", "hw": "generalized epilepsy", "pos": "phrase", "ipa": "", "vi": "động kinh toàn thể toàn thân", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033814", "hw": "george orwell", "pos": "phrase", "ipa": "", "vi": "nhà văn George Orwell (Anh)", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033815", "hw": "germ warfare", "pos": "phrase", "ipa": "", "vi": "chiến tranh vũ khí vi trùng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033816", "hw": "giant hornet", "pos": "phrase", "ipa": "", "vi": "ong bắp cày khổng lồ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033817", "hw": "gorilla gorilla gorilla", "pos": "phrase", "ipa": "", "vi": "khỉ đột đất thấp phía tây", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033818", "hw": "grade insignia", "pos": "phrase", "ipa": "", "vi": "phù hiệu quân hàm chữ V", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033819", "hw": "grapefruit juice", "pos": "phrase", "ipa": "", "vi": "nước ép bưởi chùm giải khát", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033820", "hw": "het up", "pos": "phrase", "ipa": "", "vi": "bị kích động; nóng giận bực bội", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033821", "hw": "high jinx", "pos": "phrase", "ipa": "", "vi": "trò quậy phá đùa nghịch ồn ào", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033822", "hw": "highland scot", "pos": "phrase", "ipa": "", "vi": "người vùng Cao nguyên xứ Scotland", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033823", "hw": "iceberg lettuce", "pos": "phrase", "ipa": "", "vi": "xà lách búp giòn Iceberg", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033824", "hw": "in spades", "pos": "phrase", "ipa": "", "vi": "rất nhiều; vô cùng dồi dào", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033825", "hw": "joseph paxton", "pos": "phrase", "ipa": "", "vi": "kiến trúc sư Joseph Paxton", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033826", "hw": "junction transistor", "pos": "phrase", "ipa": "", "vi": "bóng bán dẫn tiếp mặt ghép BJT", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033827", "hw": "kerry blue terrier", "pos": "phrase", "ipa": "", "vi": "giống chó sục Kerry xanh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033828", "hw": "lark about", "pos": "phrase", "ipa": "", "vi": "đùa giỡn nô đùa vui nhộn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033829", "hw": "laundry detergent", "pos": "phrase", "ipa": "", "vi": "bột giặt; nước giặt quần áo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033830", "hw": "left gastric artery", "pos": "phrase", "ipa": "", "vi": "động mạch vị trái nuôi dạ dày", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033831", "hw": "lemon zest", "pos": "phrase", "ipa": "", "vi": "vỏ chanh vàng bào mỏng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033832", "hw": "lennox robinson", "pos": "phrase", "ipa": "", "vi": "nhà viết kịch Lennox Robinson", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033833", "hw": "linkage group", "pos": "phrase", "ipa": "", "vi": "nhóm gen liên kết di truyền", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033834", "hw": "lithuanian monetary unit", "pos": "phrase", "ipa": "", "vi": "đơn vị tiền tệ Litva", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033835", "hw": "lollipop lady", "pos": "phrase", "ipa": "", "vi": "nữ hướng dẫn học sinh qua đường", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033836", "hw": "magnus hitch", "pos": "phrase", "ipa": "", "vi": "nút dây neo ma sát Magnus", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033837", "hw": "milo maize", "pos": "phrase", "ipa": "", "vi": "giống lúa miến Milo hạt kê", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033838", "hw": "mont blanc", "pos": "phrase", "ipa": "", "vi": "đỉnh núi tuyết Mont Blanc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033839", "hw": "morphological rule", "pos": "phrase", "ipa": "", "vi": "quy tắc hình thái học ngôn ngữ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033840", "hw": "motor neuron", "pos": "phrase", "ipa": "", "vi": "tế bào thần kinh vận động", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033841", "hw": "moving stairway", "pos": "phrase", "ipa": "", "vi": "cầu thang cuốn tự động", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033842", "hw": "mulberry tree", "pos": "phrase", "ipa": "", "vi": "cây dâu tằm ăn lá nuôi tằm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033843", "hw": "norfolk terrier", "pos": "phrase", "ipa": "", "vi": "chó sục cảnh Norfolk tai cụp", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033844", "hw": "oliver wendell holmes", "pos": "phrase", "ipa": "", "vi": "thẩm phán Oliver Wendell Holmes", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033845", "hw": "pancake batter", "pos": "phrase", "ipa": "", "vi": "bột lỏng pha làm bánh kếp", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033846", "hw": "pancreatic duct", "pos": "phrase", "ipa": "", "vi": "ống dẫn dịch tụy tuyến tụy", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033847", "hw": "parlour car", "pos": "phrase", "ipa": "", "vi": "toa xe lửa hạng sang êm ái", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033848", "hw": "parlour game", "pos": "phrase", "ipa": "", "vi": "trò chơi giải trí trong phòng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033849", "hw": "peacekeeping mission", "pos": "phrase", "ipa": "", "vi": "sứ mệnh giữ gìn hòa bình LHQ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033850", "hw": "peacekeeping operation", "pos": "phrase", "ipa": "", "vi": "chiến dịch gìn giữ hòa bình", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033851", "hw": "pepper shrub", "pos": "phrase", "ipa": "", "vi": "bụi cây hồ tiêu mọc thấp", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033852", "hw": "pike perch", "pos": "phrase", "ipa": "", "vi": "cá hồi chấm; cá vược răng nhọn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033853", "hw": "plum duff", "pos": "phrase", "ipa": "", "vi": "bánh pudding mận khô hấp", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033854", "hw": "polka dot", "pos": "phrase", "ipa": "", "vi": "họa tiết chấm bi tròn đều", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033855", "hw": "postmaster general", "pos": "phrase", "ipa": "", "vi": "tổng cục trưởng cục bưu điện", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033856", "hw": "principle of equivalence", "pos": "phrase", "ipa": "", "vi": "nguyên lý tương đương Einstein", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033857", "hw": "provost guard", "pos": "phrase", "ipa": "", "vi": "đội cảnh vệ quân cảnh kiểm soát", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033858", "hw": "quaker gun", "pos": "phrase", "ipa": "", "vi": "khẩu pháo gỗ nghi binh ngụy trang", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033859", "hw": "raving mad", "pos": "phrase", "ipa": "", "vi": "phát điên cuồng dại hoàn toàn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033860", "hw": "recurring decimal", "pos": "phrase", "ipa": "", "vi": "số thập phân tuần hoàn vô hạn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033861", "hw": "red grouse", "pos": "phrase", "ipa": "", "vi": "gà gô đỏ vùng đầm lầy Anh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033862", "hw": "regression coefficient", "pos": "phrase", "ipa": "", "vi": "hệ số hồi quy thống kê", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033863", "hw": "right gastric artery", "pos": "phrase", "ipa": "", "vi": "động mạch vị phải nuôi dạ dày", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033864", "hw": "rubber boa", "pos": "phrase", "ipa": "", "vi": "trăn cát cao su Bắc Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033865", "hw": "santa lucia fir", "pos": "phrase", "ipa": "", "vi": "cây linh sam nón gai Santa Lucia", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033866", "hw": "sex linkage", "pos": "phrase", "ipa": "", "vi": "hiện tượng di truyền liên kết giới", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033867", "hw": "sheath knife", "pos": "phrase", "ipa": "", "vi": "dao găm bỏ trong bao da", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033868", "hw": "short gastric artery", "pos": "phrase", "ipa": "", "vi": "các động mạch vị ngắn dạ dày", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033869", "hw": "sickle cell", "pos": "phrase", "ipa": "", "vi": "tế bào hồng cầu hình lưỡi liềm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033870", "hw": "sir joseph paxton", "pos": "phrase", "ipa": "", "vi": "ngài Joseph Paxton (kiến trúc)", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033871", "hw": "sir leonard hutton", "pos": "phrase", "ipa": "", "vi": "cầu thủ crikê Leonard Hutton", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033872", "hw": "small cell carcinoma", "pos": "phrase", "ipa": "", "vi": "ung thư biểu mô tế bào nhỏ ác", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033873", "hw": "snuff user", "pos": "phrase", "ipa": "", "vi": "người chuyên hít thuốc lá bột", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033874", "hw": "socket wrench", "pos": "phrase", "ipa": "", "vi": "cần siết đầu khẩu; cờ lê tuýp", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033875", "hw": "spanish bayonet", "pos": "phrase", "ipa": "", "vi": "cây ngọc giá mũi lê nhọn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033876", "hw": "spanish grunt", "pos": "phrase", "ipa": "", "vi": "loài cá sạo vùng biển Tây Ban Nha", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033877", "hw": "spinal puncture", "pos": "phrase", "ipa": "", "vi": "thủ thuật chọc dò tủy sống", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033878", "hw": "spiral nebula", "pos": "phrase", "ipa": "", "vi": "tinh vân xoắn ốc vũ trụ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033879", "hw": "stoop to", "pos": "phrase", "ipa": "", "vi": "hạ mình làm chuyện hèn kém", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033880", "hw": "sulphur bacteria", "pos": "phrase", "ipa": "", "vi": "vi khuẩn quang hợp lưu huỳnh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033881", "hw": "takeoff booster", "pos": "phrase", "ipa": "", "vi": "động cơ tên lửa đẩy lúc cất cánh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033882", "hw": "therapeutic cloning", "pos": "phrase", "ipa": "", "vi": "nhân bản trị liệu tạo tế bào gốc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033883", "hw": "tunisian monetary unit", "pos": "phrase", "ipa": "", "vi": "đơn vị tiền tệ Tunisia", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033884", "hw": "ugandan monetary unit", "pos": "phrase", "ipa": "", "vi": "đơn vị tiền tệ Uganda", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033885", "hw": "unwelcome person", "pos": "phrase", "ipa": "", "vi": "kẻ không được chào đón; khách lạ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033886", "hw": "urinary bladder", "pos": "phrase", "ipa": "", "vi": "bọng đái; bàng quang chứa nước", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033887", "hw": "urinary tract infection", "pos": "phrase", "ipa": "", "vi": "nhiễm trùng đường tiết niệu UTI", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033888", "hw": "virginia woolf", "pos": "phrase", "ipa": "", "vi": "nữ văn sĩ Virginia Woolf (Anh)", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033889", "hw": "walter hess", "pos": "phrase", "ipa": "", "vi": "nhà sinh lý Walter Hess (Thụy Sĩ)", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033890", "hw": "wheat germ", "pos": "phrase", "ipa": "", "vi": "phôi mầm hạt lúa mì dinh dưỡng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033891", "hw": "winged everlasting", "pos": "phrase", "ipa": "", "vi": "hoa cúc bất tử có cánh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033892", "hw": "woman hater", "pos": "phrase", "ipa": "", "vi": "người có ác cảm với phụ nữ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033893", "hw": "worldly belongings", "pos": "phrase", "ipa": "", "vi": "của cải vật chất phàm trần", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033894", "hw": "yellow hornet", "pos": "phrase", "ipa": "", "vi": "ong vò vẽ vàng khổng lồ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033895", "hw": "aleppos", "pos": "noun", "ipa": "/əˈlɛpoʊz/", "vi": "thành phố Aleppo ở Syria", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033896", "hw": "armenias", "pos": "noun", "ipa": "/ɑːrˈmiːniəz/", "vi": "đất nước Armenia", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033897", "hw": "batters", "pos": "noun", "ipa": "/ˈbætərz/", "vi": "cầu thủ đánh bóng; bột bánh lỏng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033898", "hw": "bedtimes", "pos": "noun", "ipa": "/ˈbɛdtaɪmz/", "vi": "giờ đi ngủ; thời gian lên giường", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033899", "hw": "captivities", "pos": "noun", "ipa": "/kæpˈtɪvətiz/", "vi": "tình cảnh bị giam cầm nuôi nhốt", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033900", "hw": "catastrophes", "pos": "noun", "ipa": "/kəˈtæstrəfiz/", "vi": "thảm họa thảm khốc; đại họa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033901", "hw": "concussions", "pos": "noun", "ipa": "/kənˈkʌʃənz/", "vi": "chấn động não do va đập", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
]

ALLOWED_POS = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}

assert len(data) == 100
for i, item in enumerate(data):
    expected_id = f"lex.en.200k.{33802 + i:06d}"
    assert item["id"] == expected_id, f"ID error: {item['id']} != {expected_id}"
    assert item["pos"] in ALLOWED_POS, f"POS error: {item['pos']}"
    assert item["status"] == "reviewed"
    assert len(item["vi"]) <= 35, f"VI length error {len(item['vi'])} > 35 for {item['id']}: {item['vi']}"
    hw = item["hw"]
    ipa = item["ipa"]
    if " " not in hw:
        assert ipa.startswith("/") and ipa.endswith("/") and len(ipa) > 2, f"IPA error for {hw}: {ipa}"
        assert not ipa.startswith("/ ") and not ipa.endswith(" /"), f"IPA spacing error for {hw}: {ipa}"

with open("scratch/b27_r08_p4.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully validated and wrote 100 items to scratch/b27_r08_p4.json")
