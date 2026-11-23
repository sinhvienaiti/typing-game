# -*- coding: utf-8 -*-
import json

part4_data = [
  {"id": "lex.en.200k.055302", "hw": "publius cornelius tacitus", "pos": "phrase", "ipa": "/ˈpʌbliəs kɔːrˈniːliəs ˈtæsɪtəs/", "vi": "sử gia La Mã Cornelius Tacitus", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055303", "hw": "radiologic technologist", "pos": "phrase", "ipa": "/ˌreɪdiəˈlɑːdʒɪk tɛkˈnɑːlədʒɪst/", "vi": "kỹ thuật viên chẩn đoán hình ảnh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055304", "hw": "rex begonia", "pos": "phrase", "ipa": "/rɛks bɪˈɡoʊniə/", "vi": "cây thu hải đường lá hoa văn Rex", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055305", "hw": "rocket larkspur", "pos": "phrase", "ipa": "/ˈrɑːkɪt ˈlɑːrkspɜːr/", "vi": "cây hoa phi yến tím; hoa chân chim", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055306", "hw": "safflower oil", "pos": "phrase", "ipa": "/ˈsæflaʊər ɔɪl/", "vi": "dầu ăn ép từ hạt hoa hồng rum", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055307", "hw": "safflower seed", "pos": "phrase", "ipa": "/ˈsæflaʊər siːd/", "vi": "hạt cây hoa hồng rum làm dầu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055308", "hw": "salix nigra", "pos": "phrase", "ipa": "/ˈseɪlɪks ˈnaɪɡrə/", "vi": "loài cây liễu đen Bắc Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055309", "hw": "sarah siddons", "pos": "phrase", "ipa": "/ˈsɛərə ˈsɪdənz/", "vi": "nữ diễn viên kịch Sarah Siddons", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055310", "hw": "sensorimotor area", "pos": "phrase", "ipa": "/ˌsɛnsəriˈmoʊtər ˈɛəriə/", "vi": "vùng cảm giác vận động vỏ não", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055311", "hw": "sensorimotor region", "pos": "phrase", "ipa": "/ˌsɛnsəriˈmoʊtər ˈriːdʒən/", "vi": "vùng cảm giác vận động của não", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055312", "hw": "sessile trillium", "pos": "phrase", "ipa": "/ˈsɛsaɪl ˈtrɪliəm/", "vi": "cây hoa trillium hoa không cuống", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055313", "hw": "sheep gadfly", "pos": "phrase", "ipa": "/ʃiːp ˈɡædflaɪ/", "vi": "ruồi trâu ký sinh mũi cừu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055314", "hw": "showy goldenrod", "pos": "phrase", "ipa": "/ˈʃoʊi ˈɡoʊldənrɑːd/", "vi": "cây hoa hoàng anh nở rộ rực rỡ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055315", "hw": "shrubby bittersweet", "pos": "phrase", "ipa": "/ˈʃrʌbi ˈbɪtərswiːt/", "vi": "dây leo mót bụi; cây dây leo mót", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055316", "hw": "sir charles wheatstone", "pos": "phrase", "ipa": "/sɜːr tʃɑːrlz ˈwiːtstoʊn/", "vi": "nhà vật lý Sir Charles Wheatstone", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055317", "hw": "small civet", "pos": "phrase", "ipa": "/smɔːl ˈsɪvɪt/", "vi": "loài cầy hương nhỏ châu Á", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055318", "hw": "spiny anteater", "pos": "phrase", "ipa": "/ˈspaɪni ˈæntiːtər/", "vi": "thú lông nhím đẻ trứng echidna", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055319", "hw": "striped gentian", "pos": "phrase", "ipa": "/straɪpt ˈdʒɛnʃən/", "vi": "cây hoa long đởm cánh có sọc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055320", "hw": "symbolic logician", "pos": "phrase", "ipa": "/sɪmˈbɑːlɪk loʊˈdʒɪʃən/", "vi": "nhà logic học ký hiệu toán học", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055321", "hw": "trillium sessile", "pos": "phrase", "ipa": "/ˈtrɪliəm ˈsɛsaɪl/", "vi": "loài hoa cỏ ba lá không cuống", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055322", "hw": "van de velde", "pos": "phrase", "ipa": "/væn də ˈvɛldə/", "vi": "kiến trúc sư Henry van de Velde", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055323", "hw": "wax begonia", "pos": "phrase", "ipa": "/wæks bɪˈɡoʊniə/", "vi": "cây hoa thu hải đường lá sáp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055324", "hw": "wheatstone bridge", "pos": "phrase", "ipa": "/ˈwiːtstoʊn brɪdʒ/", "vi": "mạch cầu đo điện trở Wheatstone", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055325", "hw": "whitetail deer", "pos": "phrase", "ipa": "/ˈwaɪtteɪl dɪər/", "vi": "loài hươu đuôi trắng Bắc Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055326", "hw": "absolutists", "pos": "noun", "ipa": "/ˈæbsəluːtɪsts/", "vi": "những người theo thuyết chuyên chế", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055327", "hw": "abyssinias", "pos": "noun", "ipa": "/ˌæbɪˈsɪniəz/", "vi": "đất nước Abyssinia nay là Ethiopia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055328", "hw": "aliyahs", "pos": "noun", "ipa": "/ˌɑːliˈjɑːz/", "vi": "làn sóng di cư Do Thái về Israel", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055329", "hw": "asios", "pos": "noun", "ipa": "/ˈeɪsioʊz/", "vi": "chi cú tai Asio lông mào dài", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055330", "hw": "atomizers", "pos": "noun", "ipa": "/ˈætəmaɪzərz/", "vi": "bình xịt phun sương; ống tán hạt", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055331", "hw": "avos", "pos": "noun", "ipa": "/ˈɑːvoʊz/", "vi": "đồng xu avo đơn vị tiền tệ Macao", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055332", "hw": "beachheads", "pos": "noun", "ipa": "/ˈbiːtʃhɛdz/", "vi": "các cứ điểm đổ bộ bờ biển", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055333", "hw": "belgiques", "pos": "noun", "ipa": "/bɛlˈʒiːks/", "vi": "vương quốc Bỉ tiếng Pháp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055334", "hw": "berms", "pos": "noun", "ipa": "/bɜːrmz/", "vi": "gờ đắp lề đường; bờ đất ngăn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055335", "hw": "biogeneses", "pos": "noun", "ipa": "/ˌbaɪoʊˈdʒɛnɪsiːz/", "vi": "thuyết sinh vật sinh ra sinh vật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055336", "hw": "blowtorches", "pos": "noun", "ipa": "/ˈbloʊtɔːrtʃɪz/", "vi": "các đèn xì thổi lửa hàn kim loại", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055337", "hw": "boles", "pos": "noun", "ipa": "/boʊlz/", "vi": "thân cây gỗ thẳng; đất sét đỏ bole", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055338", "hw": "bowties", "pos": "noun", "ipa": "/ˈboʊtaɪz/", "vi": "những chiếc nơ đeo cổ cánh bướm", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055339", "hw": "bucklers", "pos": "noun", "ipa": "/ˈbʌklərz/", "vi": "chiếc khiên tròn nhỏ thời trung cổ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055340", "hw": "caesareas", "pos": "noun", "ipa": "/ˌsɛzəˈriːəz/", "vi": "thành phố cảng cổ Caesarea Israel", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055341", "hw": "catskillses", "pos": "noun", "ipa": "/ˈkætskɪlzɪz/", "vi": "dãy núi Catskills ở New York", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055342", "hw": "chummier", "pos": "adj", "ipa": "/ˈtʃʌmiər/", "vi": "thân thiện hơn; gần gũi bạn bè hơn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055343", "hw": "chummiest", "pos": "adj", "ipa": "/ˈtʃʌmiɪst/", "vi": "thân thiện nhất; gắn bó thân nhất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055344", "hw": "colostomies", "pos": "noun", "ipa": "/kəˈlɑːstəmiz/", "vi": "phẫu thuật mở thông đại tràng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055345", "hw": "commercialisations", "pos": "noun", "ipa": "/kəˌmɜːrʃəlaɪˈzeɪʃənz/", "vi": "quá trình thương mại hóa sản phẩm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055346", "hw": "concepcions", "pos": "noun", "ipa": "/kənˌsɛpsiˈoʊnz/", "vi": "thành phố Concepción ở Chile", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055347", "hw": "conflated", "pos": "verb", "ipa": "/kənˈfleɪtɪd/", "vi": "đã gộp chung; đã đánh đồng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055348", "hw": "conflates", "pos": "verb", "ipa": "/kənˈfleɪts/", "vi": "gộp lẫn vào nhau; đánh đồng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055349", "hw": "conflating", "pos": "verb", "ipa": "/kənˈfleɪtɪŋ/", "vi": "đang gộp lẫn; đang đánh đồng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055350", "hw": "conservatoires", "pos": "noun", "ipa": "/kənˈsɜːrvətwɑːrz/", "vi": "các nhạc viện nghệ thuật âm nhạc", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055351", "hw": "contrases", "pos": "noun", "ipa": "/ˈkɑːntrəzɪz/", "vi": "phiến quân Contra ở Nicaragua", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055352", "hw": "cubists", "pos": "noun", "ipa": "/ˈkjuːbɪsts/", "vi": "họa sĩ thuộc trường phái lập thể", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055353", "hw": "cuds", "pos": "noun", "ipa": "/kʌdz/", "vi": "thức ăn nhai lại của động vật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055354", "hw": "debaters", "pos": "noun", "ipa": "/dɪˈbeɪtərz/", "vi": "những người tham gia tranh biện", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055355", "hw": "depositaries", "pos": "noun", "ipa": "/dɪˈpɑːzɪtɛriz/", "vi": "nơi lưu ký; người nhận ký gửi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055356", "hw": "deputations", "pos": "noun", "ipa": "/ˌdɛpjʊˈteɪʃənz/", "vi": "các phái đoàn đại biểu đại diện", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055357", "hw": "derided", "pos": "verb", "ipa": "/dɪˈraɪdɪd/", "vi": "đã chế nhạo; đã chế giễu bỉ báng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055358", "hw": "derides", "pos": "verb", "ipa": "/dɪˈraɪdz/", "vi": "chế nhạo; nhạo báng; giễu cợt", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055359", "hw": "deriding", "pos": "verb", "ipa": "/dɪˈraɪdɪŋ/", "vi": "đang chế nhạo; đang giễu cợt", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055360", "hw": "dervishes", "pos": "noun", "ipa": "/ˈdɜːrvɪʃɪz/", "vi": "các tu sĩ Hồi giáo múa dervish", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055361", "hw": "ditas", "pos": "noun", "ipa": "/ˈdiːtəz/", "vi": "loài cây hoa sữa nhiệt đới dita", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055362", "hw": "fibroblasts", "pos": "noun", "ipa": "/ˈfaɪbroʊblæsts/", "vi": "các nguyên bào sợi tạo mô liên kết", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055363", "hw": "fiefs", "pos": "noun", "ipa": "/fiːfs/", "vi": "các thái ấp lãnh địa phong kiến", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055364", "hw": "frizzed", "pos": "verb", "ipa": "/frɪzd/", "vi": "đã uốn tóc xoăn tít xù mì", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055365", "hw": "frizzes", "pos": "noun", "ipa": "/ˈfrɪzɪz/", "vi": "mái tóc xoăn tít xù; lọn tóc quăn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055366", "hw": "frizzing", "pos": "verb", "ipa": "/ˈfrɪzɪŋ/", "vi": "đang uốn xoăn tít; làm xoăn xù", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055367", "hw": "fungicides", "pos": "noun", "ipa": "/ˈfʌndʒɪsaɪdz/", "vi": "các loại thuốc diệt nấm mốc hại", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055368", "hw": "gendarmeries", "pos": "noun", "ipa": "/ʒɑːnˈdɑːrməriz/", "vi": "lực lượng cảnh binh sen đầm Pháp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055369", "hw": "genoeses", "pos": "noun", "ipa": "/ˌdʒɛnoʊˈiːzɪz/", "vi": "người dân thành Genova nước Ý", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055370", "hw": "geodesics", "pos": "noun", "ipa": "/ˌdʒiːəˈdɛsɪks/", "vi": "các đường trắc địa ngắn nhất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055371", "hw": "gnps", "pos": "noun", "ipa": "/ˌdʒiː.ɛnˈpiːz/", "vi": "tổng sản phẩm quốc dân GNP kinh tế", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055372", "hw": "guineveres", "pos": "noun", "ipa": "/ˈɡwɪnəvɪərz/", "vi": "Hoàng hậu Guinevere vua Arthur", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055373", "hw": "gynaecologists", "pos": "noun", "ipa": "/ˌɡaɪnɪˈkɑːlədʒɪsts/", "vi": "các bác sĩ chuyên khoa phụ sản", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055374", "hw": "holdovers", "pos": "noun", "ipa": "/ˈhoʊldoʊvərz/", "vi": "những tàn tích cũ; người lưu nhiệm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055375", "hw": "honeydews", "pos": "noun", "ipa": "/ˈhʌniduːz/", "vi": "trái dưa lưới ruột xanh ngọt ngào", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055376", "hw": "honeypots", "pos": "noun", "ipa": "/ˈhʌnipɑːts/", "vi": "hũ mật ngọt; mồi bẫy tin tặc mạng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055377", "hw": "housewarmings", "pos": "noun", "ipa": "/ˈhaʊswɔːrmɪŋz/", "vi": "những bữa tiệc mừng tân gia nhà", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055378", "hw": "incumbencies", "pos": "noun", "ipa": "/ɪnˈkʌmbənsiz/", "vi": "các thời gian nhiệm kỳ đương chức", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055379", "hw": "kharkovs", "pos": "noun", "ipa": "/ˈkɑːrkɔːvz/", "vi": "thành phố công nghiệp Kharkiv", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055380", "hw": "kikes", "pos": "noun", "ipa": "/kaɪks/", "vi": "từ ngữ miệt thị người Do Thái", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055381", "hw": "kiowas", "pos": "noun", "ipa": "/ˈkaɪoʊwəz/", "vi": "bộ tộc người da đỏ Kiowa Bắc Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055382", "hw": "labials", "pos": "noun", "ipa": "/ˈleɪbiəlz/", "vi": "các phụ âm môi trong ngữ âm học", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055383", "hw": "lazulis", "pos": "noun", "ipa": "/ləˈzuːliz/", "vi": "ngọc lưu ly lapis lazuli xanh biếc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055384", "hw": "ledbetters", "pos": "noun", "ipa": "/ˈlɛdbɛtərz/", "vi": "nhạc sĩ dòng nhạc blues Lead Belly", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055385", "hw": "lithospheres", "pos": "noun", "ipa": "/ˈlɪθəsfɪərz/", "vi": "các thạch quyển của vỏ Trái Đất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055386", "hw": "loafers", "pos": "noun", "ipa": "/ˈloʊfərz/", "vi": "đôi giày lười; kẻ lười biếng", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055387", "hw": "maiduguris", "pos": "noun", "ipa": "/maɪˈduːɡʊriz/", "vi": "thành phố Maiduguri ở Nigeria", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055388", "hw": "manamas", "pos": "noun", "ipa": "/məˈnæməz/", "vi": "thành phố Manama thủ đô Bahrain", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055389", "hw": "marcianos", "pos": "noun", "ipa": "/mɑːrsiˈɑːnoʊz/", "vi": "võ sĩ quyền anh Rocky Marciano", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055390", "hw": "marmots", "pos": "noun", "ipa": "/ˈmɑːrməts/", "vi": "loài sóc đất marmot vùng núi tuyết", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055391", "hw": "mealier", "pos": "adj", "ipa": "/ˈmiːliər/", "vi": "bở xốp hơn; chứa nhiều bột hơn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055392", "hw": "mealiest", "pos": "adj", "ipa": "/ˈmiːliɪst/", "vi": "bở bột nhất; xốp nhiều bột nhất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055393", "hw": "menorahs", "pos": "noun", "ipa": "/məˈnɔːrəz/", "vi": "chân đèn menorah bảy nhánh Do Thái", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055394", "hw": "minibars", "pos": "noun", "ipa": "/ˈmɪnibɑːrz/", "vi": "tủ lạnh nhỏ minibar ở khách sạn", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055395", "hw": "missals", "pos": "noun", "ipa": "/ˈmɪsəlz/", "vi": "cuốn sách kinh lễ của Công giáo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055396", "hw": "molas", "pos": "noun", "ipa": "/ˈmoʊləz/", "vi": "loài cá mặt trăng khổng lồ mola", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055397", "hw": "morgens", "pos": "noun", "ipa": "/ˈmɔːrɡənz/", "vi": "đơn vị đo diện tích đất cổ morgen", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055398", "hw": "nightcaps", "pos": "noun", "ipa": "/ˈnaɪtkæps/", "vi": "mũ ngủ; ly rượu uống trước khi ngủ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055399", "hw": "oceanfronts", "pos": "noun", "ipa": "/ˈoʊʃənfrʌnts/", "vi": "khu đất bờ biển nhìn thẳng ra biển", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055400", "hw": "oestrogens", "pos": "noun", "ipa": "/ˈiːstrədʒənz/", "vi": "nội tiết tố nữ estrogen", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055401", "hw": "olivines", "pos": "noun", "ipa": "/ˈɑːlɪviːnz/", "vi": "khoáng vật silicat olivin màu lục", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Validation
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

assert len(part4_data) == 100, f"Length is {len(part4_data)}"

with open('scratch/b32_r01_raw_p4.json') as f:
    raw = json.load(f)

for i, (item, raw_item) in enumerate(zip(part4_data, raw)):
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

with open('scratch/b32_r01_p4.json', 'w', encoding='utf-8') as f:
    json.dump(part4_data, f, ensure_ascii=False, indent=2)

print("Validated and saved 100 items for Part 4")
