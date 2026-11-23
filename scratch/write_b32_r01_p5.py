# -*- coding: utf-8 -*-
import json

part5_data = [
  {"id": "lex.en.200k.055402", "hw": "oxbridges", "pos": "noun", "ipa": "/ˈɑːksbrɪdʒɪz/", "vi": "các trường Oxford và Cambridge", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055403", "hw": "pantos", "pos": "noun", "ipa": "/ˈpæntoʊz/", "vi": "những vở kịch câm Giáng sinh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055404", "hw": "paseos", "pos": "noun", "ipa": "/pəˈseɪoʊz/", "vi": "đại lộ dạo bộ; chuyến đi dạo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055405", "hw": "peewees", "pos": "noun", "ipa": "/ˈpiːwiːz/", "vi": "người tí hon; hạng thi đấu nhí", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055406", "hw": "penobscots", "pos": "noun", "ipa": "/pəˈnɑːbskɑːts/", "vi": "người da đỏ Penobscot ở Maine", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055407", "hw": "pleiadeses", "pos": "noun", "ipa": "/ˈpliːədiːzɪz/", "vi": "nhóm sao Thất Nữ; cụm sao Tua Rua", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055408", "hw": "plovdivs", "pos": "noun", "ipa": "/ˈplɒvdɪvz/", "vi": "thành phố cổ Plovdiv Bulgaria", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055409", "hw": "pogroms", "pos": "noun", "ipa": "/ˈpoʊɡrəmz/", "vi": "các cuộc tàn sát người Do Thái", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055410", "hw": "puli", "pos": "noun", "ipa": "/ˈpuːli/", "vi": "giống chó chăn cừu lông bện Puli", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055411", "hw": "puls", "pos": "noun", "ipa": "/pʊlz/", "vi": "đồng xu pul của Afghanistan", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055412", "hw": "reignited", "pos": "verb", "ipa": "/ˌriːɪɡˈnaɪtɪd/", "vi": "đã nhen nhóm lại; thắp sáng lại", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055413", "hw": "reignites", "pos": "verb", "ipa": "/ˌriːɪɡˈnaɪts/", "vi": "bùng cháy lại; nhen nhóm lại", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055414", "hw": "reigniting", "pos": "verb", "ipa": "/ˌriːɪɡˈnaɪtɪŋ/", "vi": "đang làm bùng cháy lại ngọn lửa", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055415", "hw": "reticles", "pos": "noun", "ipa": "/ˈrɛtɪkəlz/", "vi": "lưới dây ngắm trong kính ngắm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055416", "hw": "rhizomes", "pos": "noun", "ipa": "/ˈraɪzoʊmz/", "vi": "những thân rễ ngầm của cây", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055417", "hw": "ricins", "pos": "noun", "ipa": "/ˈraɪsɪnz/", "vi": "chất độc cực mạnh ricin thầu dầu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055418", "hw": "roadrunners", "pos": "noun", "ipa": "/ˈroʊdrʌnərz/", "vi": "loài chim chẹo đất chạy nhanh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055419", "hw": "saboteurs", "pos": "noun", "ipa": "/ˌsæbəˈtɜːrz/", "vi": "những kẻ hoạt động phá hoại ngầm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055420", "hw": "sapphos", "pos": "noun", "ipa": "/ˈsæfoʊz/", "vi": "nữ thi sĩ trữ tình Sappho Hy Lạp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055421", "hw": "seawalls", "pos": "noun", "ipa": "/ˈsiːwɔːlz/", "vi": "những bức tường đê chắn sóng biển", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055422", "hw": "showgirls", "pos": "noun", "ipa": "/ˈʃoʊɡɜːrlz/", "vi": "các nữ vũ công biểu diễn sân khấu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055423", "hw": "silkworms", "pos": "noun", "ipa": "/ˈsɪlkwɜːrmz/", "vi": "những con tằm ăn lá dâu nhả tơ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055424", "hw": "smolletts", "pos": "noun", "ipa": "/ˈsmɑːlɪts/", "vi": "nhà văn Tobias Smollett Scotland", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055425", "hw": "stampers", "pos": "noun", "ipa": "/ˈstæmpərz/", "vi": "máy dập khuôn; người đóng dấu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055426", "hw": "steinems", "pos": "noun", "ipa": "/ˈstaɪnəmz/", "vi": "nhà đấu tranh Gloria Steinem", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055427", "hw": "steppers", "pos": "noun", "ipa": "/ˈstɛpərz/", "vi": "vũ công điệu step; động cơ bước", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055428", "hw": "stopgaps", "pos": "noun", "ipa": "/ˈstɑːpɡæps/", "vi": "biện pháp tạm thời; đồ thay thế", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055429", "hw": "sunblocks", "pos": "noun", "ipa": "/ˈsʌnblɑːks/", "vi": "các loại kem chống nắng ngăn nắng", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055430", "hw": "timoreses", "pos": "noun", "ipa": "/ˌtiːmɔːˈriːzɪz/", "vi": "người dân đảo Timor Đông Nam Á", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055431", "hw": "triglycerides", "pos": "noun", "ipa": "/traɪˈɡlɪsəraɪdz/", "vi": "chất béo trung tính triglyceride", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055432", "hw": "trinitarians", "pos": "noun", "ipa": "/ˌtrɪnɪˈtɛəriənz/", "vi": "người tin thuyết Chúa Ba Ngôi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055433", "hw": "tweedier", "pos": "adj", "ipa": "/ˈtwiːdiər/", "vi": "đậm chất vải tuýt thô mộc hơn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055434", "hw": "tweediest", "pos": "adj", "ipa": "/ˈtwiːdiɪst/", "vi": "đậm chất vải tuýt len nhất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055435", "hw": "wains", "pos": "noun", "ipa": "/weɪnz/", "vi": "cỗ xe ngựa chở hàng lớn ở quê", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055436", "hw": "waws", "pos": "noun", "ipa": "/wɔːz/", "vi": "chữ cái waw bảng chữ Ả Rập", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055437", "hw": "wedgies", "pos": "noun", "ipa": "/ˈwɛdʒiz/", "vi": "đôi giày đế xuồng; trò kéo quần", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055438", "hw": "weekenders", "pos": "noun", "ipa": "/ˈwiːkɛndərz/", "vi": "người đi nghỉ mát cuối tuần", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055439", "hw": "woozier", "pos": "adj", "ipa": "/ˈwuːziər/", "vi": "chóng mặt hơn; lảo đảo hơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055440", "hw": "wooziest", "pos": "adj", "ipa": "/ˈwuːziɪst/", "vi": "chóng mặt nhất; choáng váng nhất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055441", "hw": "yuppies", "pos": "noun", "ipa": "/ˈjʌpiz/", "vi": "giới trẻ thành đạt thích hưởng thụ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055442", "hw": "zingers", "pos": "noun", "ipa": "/ˈzɪŋərz/", "vi": "lời châm chọc sắc sảo bất ngờ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055443", "hw": "zits", "pos": "noun", "ipa": "/zɪts/", "vi": "những đốm mụn trứng cá trên mặt", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055444", "hw": "acetic anhydride", "pos": "phrase", "ipa": "/əˈsiːtɪk ænˈhaɪdraɪd/", "vi": "anhiđrit axetic trong hóa học", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055445", "hw": "adenosine triphosphate", "pos": "phrase", "ipa": "/əˈdɛnəsiːn traɪˈfɑːsfeɪt/", "vi": "hợp chất năng lượng ATP tế bào", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055446", "hw": "adi granth", "pos": "phrase", "ipa": "/ˈɑːdi ɡrʌnθ/", "vi": "kinh thánh Adi Granth của đạo Sikh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055447", "hw": "al jolson", "pos": "phrase", "ipa": "/æl ˈdʒoʊlsən/", "vi": "danh ca diễn viên Al Jolson Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055448", "hw": "alfred binet", "pos": "phrase", "ipa": "/ˈælfrɪd bɪˈneɪ/", "vi": "nhà tâm lý Alfred Binet người Pháp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055449", "hw": "alpha globulin", "pos": "phrase", "ipa": "/ˈælfə ˈɡlɑːbjʊlɪn/", "vi": "protein alpha globulin huyết tương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055450", "hw": "antonio gaudi", "pos": "phrase", "ipa": "/ænˈtoʊnioʊ ˈɡaʊdi/", "vi": "kiến trúc sư Antoni Gaudí", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055451", "hw": "australian aborigine", "pos": "phrase", "ipa": "/ɔːˈstreɪliən ˌæbəˈrɪdʒɪni/", "vi": "người bản địa thổ dân Úc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055452", "hw": "barbara tuchman", "pos": "phrase", "ipa": "/ˈbɑːrbərə ˈtʌkmən/", "vi": "nữ sử gia Mỹ Barbara Tuchman", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055453", "hw": "bay of campeche", "pos": "phrase", "ipa": "/beɪ əv kæmˈpiːtʃi/", "vi": "vịnh Campeche ở miền nam Mexico", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055454", "hw": "beta globulin", "pos": "phrase", "ipa": "/ˈbeɪtə ˈɡlɑːbjʊlɪn/", "vi": "nhóm đạm beta globulin huyết tương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055455", "hw": "cardinal bellarmine", "pos": "phrase", "ipa": "/ˈkɑːrdɪnəl ˈbɛlərmiːn/", "vi": "Hồng y Robert Bellarmine của Ý", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055456", "hw": "carob bar", "pos": "phrase", "ipa": "/ˈkærəb bɑːr/", "vi": "thanh kẹo đậu carob thay socola", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055457", "hw": "carob powder", "pos": "phrase", "ipa": "/ˈkærəb ˈpaʊdər/", "vi": "bột quả đậu carob thay bột ca cao", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055458", "hw": "carob tree", "pos": "phrase", "ipa": "/ˈkærəb triː/", "vi": "cây minh đậu carob Địa Trung Hải", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055459", "hw": "cephalic vein", "pos": "phrase", "ipa": "/sɪˈfælɪk veɪn/", "vi": "tĩnh mạch đầu ở cánh tay", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055460", "hw": "chukchi language", "pos": "phrase", "ipa": "/ˈtʃʊktʃi ˈlæŋɡwɪdʒ/", "vi": "tiếng Chukchi của thổ dân Siberia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055461", "hw": "chukchi sea", "pos": "phrase", "ipa": "/ˈtʃʊktʃi siː/", "vi": "biển Chukchi ở Bắc Băng Dương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055462", "hw": "cingulate gyrus", "pos": "phrase", "ipa": "/ˈsɪŋɡjələt ˈdʒaɪrəs/", "vi": "hồi đai của đại não bộ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055463", "hw": "civet bean", "pos": "phrase", "ipa": "/ˈsɪvɪt biːn/", "vi": "hạt đậu ngự dẹt; đậu Lima", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055464", "hw": "comity of nations", "pos": "phrase", "ipa": "/ˈkɑːməti əv ˈneɪʃənz/", "vi": "tình hòa hiếu giữa các quốc gia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055465", "hw": "common foxglove", "pos": "phrase", "ipa": "/ˈkɑːmən ˈfɑːksɡlʌv/", "vi": "cây hoa mao địa hoàng tím trị tim", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055466", "hw": "comte de mirabeau", "pos": "phrase", "ipa": "/kɔ̃ːt də ˌmɪrəˈboʊ/", "vi": "Bá tước Mirabeau Cách mạng Pháp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055467", "hw": "creme brulee", "pos": "phrase", "ipa": "/krɛm bruːˈleɪ/", "vi": "món tráng miệng kem trứng cháy", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055468", "hw": "edward goldenberg robinson", "pos": "phrase", "ipa": "/ˈɛdwərd ˈɡoʊldənbɜːrɡ ˈrɑːbɪnsən/", "vi": "diễn viên Edward G. Robinson", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055469", "hw": "eider duck", "pos": "phrase", "ipa": "/ˈaɪdər dʌk/", "vi": "loài vịt biển eider lấy lông vũ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055470", "hw": "false foxglove", "pos": "phrase", "ipa": "/fɔːls ˈfɑːksɡlʌv/", "vi": "cây mao địa hoàng hoa vàng giả", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055471", "hw": "false sarsaparilla", "pos": "phrase", "ipa": "/fɔːls ˌsɑːrspəˈrɪlə/", "vi": "cây sâm hoang dại Bắc Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055472", "hw": "feast of tabernacles", "pos": "phrase", "ipa": "/fiːst əv ˈtæbərnækəlz/", "vi": "ngày lễ Lều Tạm của người Do Thái", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055473", "hw": "foxglove family", "pos": "phrase", "ipa": "/ˈfɑːksɡlʌv ˈfæmɪli/", "vi": "họ thực vật hoa Mõm sói Huyền sâm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055474", "hw": "frans hals", "pos": "phrase", "ipa": "/frɑːns hɑːls/", "vi": "danh họa Hà Lan Frans Hals", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055475", "hw": "genus jynx", "pos": "phrase", "ipa": "/ˈdʒiːnəs dʒɪŋks/", "vi": "chi chim cổ vẹo gõ kiến", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055476", "hw": "genus rattus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈrætəs/", "vi": "chi chuột cống chuột nhà", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055477", "hw": "genus stegosaurus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌstɛɡəˈsɔːrəs/", "vi": "chi khủng long bọc giáp gai lưng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055478", "hw": "geosynchronous orbit", "pos": "phrase", "ipa": "/ˌdʒiːoʊˈsɪŋkrənəs ˈɔːrbɪt/", "vi": "quỹ đạo địa đồng bộ vệ tinh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055479", "hw": "gerard depardieu", "pos": "phrase", "ipa": "/ʒeɪˈrɑːr deɪpɑːrˈdjuː/", "vi": "nam tài tử Gérard Depardieu Pháp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055480", "hw": "grassy death camas", "pos": "phrase", "ipa": "/ˈɡræsi dɛθ ˈkæməs/", "vi": "cây hoa tử huệ lá cỏ có độc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055481", "hw": "gulf of campeche", "pos": "phrase", "ipa": "/ɡʌlf əv kæmˈpiːtʃi/", "vi": "vịnh Campeche ở miền nam Mexico", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055482", "hw": "haberdashery store", "pos": "phrase", "ipa": "/ˌhæbərˈdæʃəri stɔːr/", "vi": "tiệm bán phụ liệu may mặc kim chỉ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055483", "hw": "hebridean isles", "pos": "phrase", "ipa": "/hɛˈbrɪdiən aɪlz/", "vi": "quần đảo Hebrides ở Scotland", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055484", "hw": "henry rowe schoolcraft", "pos": "phrase", "ipa": "/ˈhɛnri roʊ ˈskuːlkræft/", "vi": "nhà địa lý Henry Rowe Schoolcraft", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055485", "hw": "humoral immune response", "pos": "phrase", "ipa": "/ˈhjuːmərəl ɪˈmjuːn rɪˈspɑːns/", "vi": "đáp ứng miễn dịch dịch thể", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055486", "hw": "immune globulin", "pos": "phrase", "ipa": "/ɪˈmjuːn ˈɡlɑːbjʊlɪn/", "vi": "kháng thể globulin miễn dịch", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055487", "hw": "jacksonian epilepsy", "pos": "phrase", "ipa": "/dʒækˈsoʊniən ˈɛpɪlɛpsi/", "vi": "chứng động kinh cục bộ Jackson", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055488", "hw": "julia evelina smith", "pos": "phrase", "ipa": "/ˈdʒuːliə ˌɛvəˈlaɪnə smɪθ/", "vi": "nhà vận động Julia Evelina Smith", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055489", "hw": "lacrimal duct", "pos": "phrase", "ipa": "/ˈlækrɪməl dʌkt/", "vi": "ống dẫn nước mắt; tuyến dẫn lệ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055490", "hw": "lacrimal gland", "pos": "phrase", "ipa": "/ˈlækrɪməl ɡlænd/", "vi": "tuyến lệ tiết ra nước mắt", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055491", "hw": "lancastrian line", "pos": "phrase", "ipa": "/lænˈkæstriən laɪn/", "vi": "vương triều hoàng gia Lancaster", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055492", "hw": "law of parsimony", "pos": "phrase", "ipa": "/lɔː əv pɑːrˈsɪməni/", "vi": "nguyên lý giản ước dao cạo Occam", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055493", "hw": "louis isadore kahn", "pos": "phrase", "ipa": "/ˈluːɪs ˈɪzədɔːr kɑːn/", "vi": "kiến trúc sư Louis Kahn nước Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055494", "hw": "octal notation", "pos": "phrase", "ipa": "/ˈɑːktəl noʊˈteɪʃən/", "vi": "hệ thống ký hiệu số bát phân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055495", "hw": "optical maser", "pos": "phrase", "ipa": "/ˈɑːptɪkəl ˈmeɪzər/", "vi": "thiết bị phát tia la-de quang học", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055496", "hw": "order foraminifera", "pos": "phrase", "ipa": "/ˈɔːrdər fəˌræmɪˈnɪfərə/", "vi": "bộ Trùng có lỗ có vỏ đá vôi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055497", "hw": "os breve", "pos": "phrase", "ipa": "/ɑːs ˈbreɪvi/", "vi": "xương ngắn nhỏ trong cơ thể", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055498", "hw": "patrilineal kin", "pos": "phrase", "ipa": "/ˌpætrɪˈlɪniəl kɪn/", "vi": "họ hàng thân thích theo dòng cha", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055499", "hw": "paul john flory", "pos": "phrase", "ipa": "/pɔːl dʒɑːn ˈflɔːri/", "vi": "nhà hóa học Nobel Paul Flory", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055500", "hw": "pierre de fermat", "pos": "phrase", "ipa": "/pjɛər də fɛərˈmɑː/", "vi": "nhà toán học Pierre de Fermat", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055501", "hw": "plunk down", "pos": "phrase", "ipa": "/plʌŋk daʊn/", "vi": "đặt phịch xuống; trả tiền mặt ra", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Validation
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

assert len(part5_data) == 100, f"Length is {len(part5_data)}"

with open('scratch/b32_r01_raw_p5.json') as f:
    raw = json.load(f)

for i, (item, raw_item) in enumerate(zip(part5_data, raw)):
    assert item['id'] == raw_item['id'], f"ID mismatch at {i}: {item['id']} vs {raw_item['id']}"
    assert item['hw'] == raw_item['hw'], f"HW mismatch at {i}: {item['hw']} vs {raw_item['hw']}"
    assert list(item.keys()) == expected_keys, f"Keys mismatch at {i}: {list(item.keys())}"
    assert item['pos'] in allowed_pos, f"pos invalid at {i}: {item['pos']}"
    assert len(item['vi']) <= 35, f"vi too long ({len(item['vi'])} chars) at {i}: {item['vi']}"
    assert item['status'] == 'reviewed'
    if ' ' not in item['hw']:
        assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and len(item['ipa']) > 2, f"invalid ipa at {i}: {item['ipa']}"
    if ';' in item['vi']:
        for seg in item['vi'].split(';')[1:]:
            assert seg.startswith(' '), f"missing space after semicolon at {i}: {item['vi']}"

with open('scratch/b32_r01_p5.json', 'w', encoding='utf-8') as f:
    json.dump(part5_data, f, ensure_ascii=False, indent=2)

print("Validated and saved 100 items for Part 5")
