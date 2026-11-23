import json

data = [
  {"id": "lex.en.200k.033502", "hw": "poppies", "pos": "noun", "ipa": "/ˈpɑpiz/", "vi": "hoa anh túc; cây thuốc phiện", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033503", "hw": "raleighs", "pos": "noun", "ipa": "/ˈrɑːliz/", "vi": "thành phố Raleigh; xe đạp Raleigh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033504", "hw": "roths", "pos": "noun", "ipa": "/rɑːθs/", "vi": "quỹ Roth; gia tộc Roth", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033505", "hw": "slenderer", "pos": "adj", "ipa": "/ˈslɛndərər/", "vi": "mảnh mai hơn; thon thả hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033506", "hw": "slenderest", "pos": "adj", "ipa": "/ˈslɛndərəst/", "vi": "mảnh mai nhất; thon thả nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033507", "hw": "sloppier", "pos": "adj", "ipa": "/ˈslɑpiər/", "vi": "luộm thuộm hơn; cẩu thả hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033508", "hw": "sloppiest", "pos": "adj", "ipa": "/ˈslɑpiəst/", "vi": "luộm thuộm nhất; cẩu thả nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033509", "hw": "steeles", "pos": "noun", "ipa": "/stiːlz/", "vi": "người mang họ Steele", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033510", "hw": "tiffanies", "pos": "noun", "ipa": "/ˈtɪfəniz/", "vi": "đồ trang sức Tiffany; vải tiffany", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033511", "hw": "transmitters", "pos": "noun", "ipa": "/trænzˈmɪtərz/", "vi": "máy phát tín hiệu; chất truyền dẫn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033512", "hw": "typhoons", "pos": "noun", "ipa": "/taɪˈfunz/", "vi": "những cơn bão nhiệt đới", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033513", "hw": "vibrations", "pos": "noun", "ipa": "/vaɪˈbreɪʃənz/", "vi": "sự rung chuyển; cảm rung động", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033514", "hw": "wickets", "pos": "noun", "ipa": "/ˈwɪkɪts/", "vi": "khung thành crikê; cửa cổng nhỏ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033515", "hw": "winnipegs", "pos": "noun", "ipa": "/ˈwɪnɪpɛɡz/", "vi": "thành phố Winnipeg; hồ Winnipeg", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033516", "hw": "worcesters", "pos": "noun", "ipa": "/ˈwʊstərz/", "vi": "thành phố Worcester", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033517", "hw": "zuriches", "pos": "noun", "ipa": "/ˈzʊərɪks/", "vi": "thành phố Zurich", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033518", "hw": "adolescents", "pos": "noun", "ipa": "/ˌædəˈlɛsənts/", "vi": "thanh thiếu niên; tuổi mới lớn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033519", "hw": "airings", "pos": "noun", "ipa": "/ˈɛrɪŋz/", "vi": "sự phơi gió; buổi phát sóng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033520", "hw": "announcers", "pos": "noun", "ipa": "/əˈnaʊnsərz/", "vi": "phát thanh viên; người giới thiệu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033521", "hw": "babas", "pos": "noun", "ipa": "/ˈbɑːbɑːz/", "vi": "bánh baba ngâm rượu rum", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033522", "hw": "backdrops", "pos": "noun", "ipa": "/ˈbækdrɑps/", "vi": "phông nền sân khấu; bối cảnh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033523", "hw": "beaus", "pos": "noun", "ipa": "/boʊz/", "vi": "người tình; bạn trai quý phái", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033524", "hw": "blackouts", "pos": "noun", "ipa": "/ˈblækˌaʊts/", "vi": "sự mất điện; sự thoáng ngất đi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033525", "hw": "bluffest", "pos": "adj", "ipa": "/ˈblʌfɪst/", "vi": "thẳng thắn nhất; dốc đứng nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033526", "hw": "bollywoods", "pos": "noun", "ipa": "/ˈbɑːliwʊdz/", "vi": "nền điện ảnh Bollywood Ấn Độ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033527", "hw": "cartels", "pos": "noun", "ipa": "/kɑːrˈtɛlz/", "vi": "các ten buôn bán; nhóm độc quyền", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033528", "hw": "caucused", "pos": "verb", "ipa": "/ˈkɔkəst/", "vi": "đã họp nhóm kín chính trị", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033529", "hw": "caucusing", "pos": "verb", "ipa": "/ˈkɔkəsɪŋ/", "vi": "đang họp nhóm kín chính trị", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033530", "hw": "cheesier", "pos": "adj", "ipa": "/ˈtʃiziər/", "vi": "sến súa hơn; rẻ tiền hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033531", "hw": "cheesiest", "pos": "adj", "ipa": "/ˈtʃiziɪst/", "vi": "sến súa nhất; rẻ tiền nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033532", "hw": "citruses", "pos": "noun", "ipa": "/ˈsɪtrəsɪz/", "vi": "cây họ cam quýt; quả có múi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033533", "hw": "columnists", "pos": "noun", "ipa": "/ˈkɑləmnɪsts/", "vi": "nhà bình luận; người viết mục báo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033534", "hw": "constituents", "pos": "noun", "ipa": "/kənˈstɪtʃuənts/", "vi": "cử tri khu vực; thành phần hợp tạo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033535", "hw": "courtrooms", "pos": "noun", "ipa": "/ˈkɔrtruːmz/", "vi": "phòng xử án; phiên toà", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033536", "hw": "diazes", "pos": "noun", "ipa": "/ˈdiːæzɪz/", "vi": "người mang họ Diaz", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033537", "hw": "dorises", "pos": "noun", "ipa": "/ˈdɔrɪsɪz/", "vi": "những người tên Doris", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033538", "hw": "ducts", "pos": "noun", "ipa": "/dʌkts/", "vi": "ống dẫn chất lỏng; ống thông khí", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033539", "hw": "ews", "pos": "noun", "ipa": "/iːˌdʌbəlˈjuːz/", "vi": "hệ thống tác chiến điện tử", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033540", "hw": "flyers", "pos": "noun", "ipa": "/ˈflaɪərz/", "vi": "tờ bướm quảng cáo; hành khách bay", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033541", "hw": "glaciers", "pos": "noun", "ipa": "/ˈɡleɪʃərz/", "vi": "sông băng; khối băng trôi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033542", "hw": "influxes", "pos": "noun", "ipa": "/ˈɪnflʌksɪz/", "vi": "sự tràn vào; luồng đổ xô tới", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033543", "hw": "installments", "pos": "noun", "ipa": "/ɪnˈstɔlmənts/", "vi": "tiền trả góp; phần kỳ phát hành", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033544", "hw": "judaisms", "pos": "noun", "ipa": "/ˈdʒuːdeɪˌɪzəmz/", "vi": "các nhánh Do Thái giáo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033545", "hw": "kellers", "pos": "noun", "ipa": "/ˈkɛlərz/", "vi": "người mang họ Keller", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033546", "hw": "kernelled", "pos": "adj", "ipa": "/ˈkɜrnəld/", "vi": "có hạt nhân; có hạt cùi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033547", "hw": "kernelling", "pos": "noun", "ipa": "/ˈkɜrnəlɪŋ/", "vi": "sự tạo thành nhân hạt", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033548", "hw": "kernels", "pos": "noun", "ipa": "/ˈkɜrnəlz/", "vi": "hạt nhân; lõi cốt lõi vấn đề", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033549", "hw": "lexingtons", "pos": "noun", "ipa": "/ˈlɛksɪŋtənz/", "vi": "thành phố Lexington", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033550", "hw": "liaisons", "pos": "noun", "ipa": "/liˈeɪzɑnz/", "vi": "sự liên lạc; mối quan hệ tình cảm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033551", "hw": "limas", "pos": "noun", "ipa": "/ˈliːməz/", "vi": "đậu lima; thủ đô Lima Peru", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033552", "hw": "miners", "pos": "noun", "ipa": "/ˈmaɪnərz/", "vi": "thợ khai mỏ; người đào hầm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033553", "hw": "mosaics", "pos": "noun", "ipa": "/moʊˈzeɪɪks/", "vi": "tranh ghép mảnh; nghệ thuật khảm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033554", "hw": "mustangs", "pos": "noun", "ipa": "/ˈmʌstæŋz/", "vi": "ngựa hoang dã Bắc Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033555", "hw": "needier", "pos": "adj", "ipa": "/ˈnidiər/", "vi": "túng thiếu hơn; nghèo khó hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033556", "hw": "neediest", "pos": "adj", "ipa": "/ˈnidiɪst/", "vi": "túng thiếu nhất; nghèo khó nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033557", "hw": "patties", "pos": "noun", "ipa": "/ˈpætiz/", "vi": "miếng thịt băm kẹp bánh mì; chả", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033558", "hw": "romanians", "pos": "noun", "ipa": "/roʊˈmeɪniənz/", "vi": "người dân Romania", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033559", "hw": "saxons", "pos": "noun", "ipa": "/ˈsæksənz/", "vi": "người Xắc-xông; dân tộc Saxon", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033560", "hw": "seasides", "pos": "noun", "ipa": "/ˈsiːsaɪdz/", "vi": "bờ biển; vùng nghỉ mát ven biển", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033561", "hw": "semitics", "pos": "noun", "ipa": "/səˈmɪtɪks/", "vi": "ngành nghiên cứu ngữ hệ Xê-mít", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033562", "hw": "shampooed", "pos": "verb", "ipa": "/ʃæmˈpuːd/", "vi": "đã gội đầu; đã giặt thảm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033563", "hw": "shampooing", "pos": "verb", "ipa": "/ʃæmˈpuːɪŋ/", "vi": "đang gội đầu; sự gội sạch đầu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033564", "hw": "shampoos", "pos": "noun", "ipa": "/ʃæmˈpuːz/", "vi": "các loại dầu gội đầu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033565", "hw": "tangs", "pos": "noun", "ipa": "/tæŋz/", "vi": "mùi thơm gắt; chuôi dao rựa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033566", "hw": "telecoms", "pos": "noun", "ipa": "/ˈtɛləkɑmz/", "vi": "ngành viễn thông; mạng truyền thông", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033567", "hw": "toxicities", "pos": "noun", "ipa": "/tɑːkˈsɪsətiz/", "vi": "mức độ độc tính; nồng độ độc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033568", "hw": "wrappings", "pos": "noun", "ipa": "/ˈræpɪŋz/", "vi": "giấy gói bọc; vật liệu bao bì", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033569", "hw": "alan alexander milne", "pos": "phrase", "ipa": "", "vi": "nhà văn A. A. Milne (Anh)", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033570", "hw": "alligator lizard", "pos": "phrase", "ipa": "", "vi": "thằn lằn cá sấu Bắc Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033571", "hw": "american cranberry bush", "pos": "phrase", "ipa": "", "vi": "cây kim ngân hoa quả đỏ Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033572", "hw": "american mink", "pos": "phrase", "ipa": "", "vi": "chồn nâu châu Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033573", "hw": "andromeda galaxy", "pos": "phrase", "ipa": "", "vi": "thiên hà Tiên Nữ M31", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033574", "hw": "arc tangent", "pos": "phrase", "ipa": "", "vi": "hàm ac-tang; góc lượng giác tang", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033575", "hw": "ascending artery", "pos": "phrase", "ipa": "", "vi": "động mạch hướng lên", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033576", "hw": "australian cockroach", "pos": "phrase", "ipa": "", "vi": "loài gián Úc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033577", "hw": "bald cypress", "pos": "phrase", "ipa": "", "vi": "cây bụt mọc; cây bách hói", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033578", "hw": "benign tumour", "pos": "phrase", "ipa": "", "vi": "khối u lành tính", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033579", "hw": "black mulberry", "pos": "phrase", "ipa": "", "vi": "cây dâu tằm đen", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033580", "hw": "bluegrass region", "pos": "phrase", "ipa": "", "vi": "vùng cỏ xanh bang Kentucky", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033581", "hw": "bottling plant", "pos": "phrase", "ipa": "", "vi": "nhà máy đóng chai nước", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033582", "hw": "calcium nitrate", "pos": "phrase", "ipa": "", "vi": "hóa chất canxi nitrat", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033583", "hw": "cape tulip", "pos": "phrase", "ipa": "", "vi": "hoa tulip mũi Hảo Vọng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033584", "hw": "carbon monoxide poisoning", "pos": "phrase", "ipa": "", "vi": "ngộ độc khí cacbon monoxit", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033585", "hw": "cascade everlasting", "pos": "phrase", "ipa": "", "vi": "hoa cúc bất tử vùng Cascade", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033586", "hw": "cavalier hat", "pos": "phrase", "ipa": "", "vi": "mũ hiệp sĩ rộng vành có lông", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033587", "hw": "cayman islands dollar", "pos": "phrase", "ipa": "", "vi": "đồng đô la Quần đảo Cayman", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033588", "hw": "cellular slime mold", "pos": "phrase", "ipa": "", "vi": "nấm nhầy dạng tế bào", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033589", "hw": "charles edward ives", "pos": "phrase", "ipa": "", "vi": "nhạc sĩ Charles Ives người Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033590", "hw": "church slavic", "pos": "phrase", "ipa": "", "vi": "tiếng Slav Giáo hội cổ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033591", "hw": "clockwise rotation", "pos": "phrase", "ipa": "", "vi": "chuyển động quay theo kim đồng hồ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033592", "hw": "common juniper", "pos": "phrase", "ipa": "", "vi": "cây bách xù phổ thông", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033593", "hw": "complement fixation", "pos": "phrase", "ipa": "", "vi": "hiện tượng gắn kết bổ thể sinh học", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033594", "hw": "complement fixation test", "pos": "phrase", "ipa": "", "vi": "xét nghiệm gắn bổ thể chẩn đoán", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033595", "hw": "corrugated board", "pos": "phrase", "ipa": "", "vi": "bìa carton dạng lượn sóng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033596", "hw": "cotton flannel", "pos": "phrase", "ipa": "", "vi": "vải dạ nỉ làm từ sợi bông", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033597", "hw": "cow manure", "pos": "phrase", "ipa": "", "vi": "phân bò bón đất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033598", "hw": "cranberry bush", "pos": "phrase", "ipa": "", "vi": "bụi cây nam việt quất rừng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033599", "hw": "cultural anthropologist", "pos": "phrase", "ipa": "", "vi": "nhà nhân loại học văn hóa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033600", "hw": "custard apple tree", "pos": "phrase", "ipa": "", "vi": "cây na ta; cây mãng cầu ta", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.033601", "hw": "dinner napkin", "pos": "phrase", "ipa": "", "vi": "khăn ăn trải bàn trong bữa tối", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
]

ALLOWED_POS = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}

assert len(data) == 100
for i, item in enumerate(data):
    expected_id = f"lex.en.200k.{33502 + i:06d}"
    assert item["id"] == expected_id, f"ID error: {item['id']} != {expected_id}"
    assert item["pos"] in ALLOWED_POS, f"POS error: {item['pos']}"
    assert item["status"] == "reviewed"
    assert len(item["vi"]) <= 35, f"VI length error {len(item['vi'])} > 35 for {item['id']}: {item['vi']}"
    hw = item["hw"]
    ipa = item["ipa"]
    if " " not in hw:
        assert ipa.startswith("/") and ipa.endswith("/") and len(ipa) > 2, f"IPA error for {hw}: {ipa}"
        assert not ipa.startswith("/ ") and not ipa.endswith(" /"), f"IPA spacing error for {hw}: {ipa}"

with open("scratch/b27_r08_p1.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully validated and wrote 100 items to scratch/b27_r08_p1.json")
