# -*- coding: utf-8 -*-
import json

part5_data = [
  {"id": "lex.en.200k.054402", "hw": "hypertrophic cardiomyopathy", "pos": "phrase", "ipa": "/ˌhaɪpərˈtroʊfɪk ˌkɑːrdioʊmaɪˈɑːpəθi/", "vi": "bệnh lý phì đại cơ tim", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054403", "hw": "imitative electronic deception", "pos": "phrase", "ipa": "/ˈɪmɪtətɪv ɪˌlɛkˈtrɑːnɪk dɪˈsɛpʃən/", "vi": "nghi binh điện tử mô phỏng giả lập", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054404", "hw": "increasing monotonic", "pos": "phrase", "ipa": "/ɪnˈkriːsɪŋ ˌmɑːnəˈtɑːnɪk/", "vi": "hàm số đơn điệu tăng dần", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054405", "hw": "inferior mesenteric artery", "pos": "phrase", "ipa": "/ɪnˈfɪəriər ˌmɛzənˈtɛrɪk ˈɑːrtəri/", "vi": "động mạch mạc treo tràng dưới ruột", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054406", "hw": "inspector maigret", "pos": "phrase", "ipa": "/ɪnˈspɛktər mɛˈɡreɪ/", "vi": "thanh tra hình sự Maigret", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054407", "hw": "intercostal artery", "pos": "phrase", "ipa": "/ˌɪntərˈkɑːstəl ˈɑːrtəri/", "vi": "động mạch liên sườn cấp máu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054408", "hw": "inverted pleat", "pos": "phrase", "ipa": "/ɪnˈvɜːrtɪd pliːt/", "vi": "nếp xếp li lộn ngược mặt trong", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054409", "hw": "karl von clausewitz", "pos": "phrase", "ipa": "/kɑːrl fɔːn ˈklaʊzəvɪts/", "vi": "nhà lý luận quân sự Clausewitz", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054410", "hw": "locative role", "pos": "phrase", "ipa": "/ˈlɑːkətɪv roʊl/", "vi": "vai trò định vị nơi chốn ngữ nghĩa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054411", "hw": "loggerhead turtle", "pos": "phrase", "ipa": "/ˈlɑːɡərˌhɛd ˈtɜːrtəl/", "vi": "rùa biển quản đồng đầu to", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054412", "hw": "mallee fowl", "pos": "phrase", "ipa": "/ˈmæli faʊl/", "vi": "chim ấp trứng gò đất mallee Úc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054413", "hw": "mary douglas leakey", "pos": "phrase", "ipa": "/ˈmɛri ˈdʌɡləs ˈliːki/", "vi": "nhà khảo cổ học Mary Leakey", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054414", "hw": "maxfield parrish", "pos": "phrase", "ipa": "/ˈmæksfiːld ˈpærɪʃ/", "vi": "họa sĩ minh họa Maxfield Parrish", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054415", "hw": "meadow fescue", "pos": "phrase", "ipa": "/ˈmɛdoʊ ˈfɛskjuː/", "vi": "cỏ đuôi trâu đồng cỏ chăn nuôi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054416", "hw": "membranous labyrinth", "pos": "phrase", "ipa": "/ˈmɛmbrənəs ˈlæbərɪnθ/", "vi": "mê đạo màng trong ốc tai trong", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054417", "hw": "milch cow", "pos": "phrase", "ipa": "/mɪltʃ kaʊ/", "vi": "bò sữa; nguồn lợi bị bòn rút", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054418", "hw": "monocular vision", "pos": "phrase", "ipa": "/məˈnɑːkjələr ˈvɪʒən/", "vi": "thị giác một mắt đơn độc", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054419", "hw": "mortise joint", "pos": "phrase", "ipa": "/ˈmɔːrtɪs dʒɔɪnt/", "vi": "mối ghép mộng mòi thợ mộc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054420", "hw": "otitis media", "pos": "phrase", "ipa": "/oʊˈtaɪtɪs ˈmiːdiə/", "vi": "bệnh viêm tai giữa cấp tính", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054421", "hw": "pale chrysanthemum aphid", "pos": "phrase", "ipa": "/peɪl krɪˈsænθəməm ˈeɪfɪd/", "vi": "rệp muội hoa cúc màu nhạt hại cây", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054422", "hw": "pan troglodytes", "pos": "phrase", "ipa": "/pæn ˈtrɑːɡlədaɪtiːz/", "vi": "loài tinh tinh thông minh châu Phi", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054423", "hw": "papillary tumor", "pos": "phrase", "ipa": "/ˈpæpɪlɛri ˈtuːmər/", "vi": "khối u nhú nhú gai lành tính", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054424", "hw": "pars intermedia", "pos": "phrase", "ipa": "/pɑːrz ˌɪntərˈmiːdiə/", "vi": "phần trung gian của tuyến yên não", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054425", "hw": "peyton rous", "pos": "phrase", "ipa": "/ˈpeɪtən raʊs/", "vi": "nhà virus học Nobel Peyton Rous", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054426", "hw": "phrygian deity", "pos": "phrase", "ipa": "/ˈfrɪdʒiən ˈdeɪɪti/", "vi": "thần linh xứ Phrygia cổ đại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054427", "hw": "pincushion flower", "pos": "phrase", "ipa": "/ˈpɪnkʊʃən ˈflaʊər/", "vi": "hoa gối cắm kim cúc hoa tím", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054428", "hw": "pis aller", "pos": "phrase", "ipa": "/ˌpiːz æˈleɪ/", "vi": "giải pháp cuối cùng bất đắc dĩ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054429", "hw": "prudhoe bay", "pos": "phrase", "ipa": "/ˈpruːdoʊ beɪ/", "vi": "vịnh mỏ dầu Prudhoe ở Alaska", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054430", "hw": "ragnar frisch", "pos": "phrase", "ipa": "/ˈræɡnɑːr frɪʃ/", "vi": "nhà kinh tế học Nobel Ragnar Frisch", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054431", "hw": "rameses ii", "pos": "phrase", "ipa": "/ˈræməsiːz ðə ˈsɛkənd/", "vi": "vua Pharaon Ramesses II Ai Cập", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054432", "hw": "rameses the great", "pos": "phrase", "ipa": "/ˈræməsiːz ðə ɡreɪt/", "vi": "đại đế Ramesses vĩ đại Ai Cập", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054433", "hw": "shiitake mushroom", "pos": "phrase", "ipa": "/ʃɪˈtɑːki ˈmʌʃruːm/", "vi": "nấm hương thơm; nấm đông cô giòn", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054434", "hw": "sinus rectus", "pos": "phrase", "ipa": "/ˈsaɪnəs ˈrɛktəs/", "vi": "xoang tĩnh mạch thẳng màng cứng não", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054435", "hw": "sisal hemp", "pos": "phrase", "ipa": "/ˈsaɪsəl hɛmp/", "vi": "sợi thùa gai sisal bện dây thừng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054436", "hw": "sodium hypochlorite", "pos": "phrase", "ipa": "/ˈsoʊdiəm ˌhaɪpoʊˈklɔːraɪt/", "vi": "nước tẩy javen natri hypoclorit", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054437", "hw": "solway firth", "pos": "phrase", "ipa": "/ˈsɑːlweɪ fɜːrθ/", "vi": "vịnh biển Solway Firth ở Anh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054438", "hw": "sonoran lyre snake", "pos": "phrase", "ipa": "/səˈnɔːrən ˈlaɪər sneɪk/", "vi": "loài rắn đàn lia Sonoran sa mạc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054439", "hw": "splenic artery", "pos": "phrase", "ipa": "/ˈsplɛnɪk ˈɑːrtəri/", "vi": "động mạch lách cấp máu cho lách", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054440", "hw": "splenic vein", "pos": "phrase", "ipa": "/ˈsplɛnɪk veɪn/", "vi": "tĩnh mạch lách dẫn máu về gan", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054441", "hw": "stinking bean trefoil", "pos": "phrase", "ipa": "/ˈstɪŋkɪŋ biːn ˈtrɛfɔɪl/", "vi": "cây thảo dã hương mùi hăng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054442", "hw": "strait of hormuz", "pos": "phrase", "ipa": "/streɪt əv hɔːrˈmuːz/", "vi": "eo biển chiến lược Hormuz", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054443", "hw": "tallulah bankhead", "pos": "phrase", "ipa": "/təˈluːlə ˈbæŋkhɛd/", "vi": "nữ minh tinh Tallulah Bankhead", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054444", "hw": "tansy mustard", "pos": "phrase", "ipa": "/ˈtænzi ˈmʌstərd/", "vi": "cây cải dại tansy hoa vàng dại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054445", "hw": "theater prompter", "pos": "phrase", "ipa": "/ˈθiːətər ˈprɑːmptər/", "vi": "người nhắc tuồng kịch sân khấu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054446", "hw": "usama bin laden", "pos": "phrase", "ipa": "/uːˈsɑːmə bɪn ˈlɑːdən/", "vi": "trùm khủng bố Usama bin Laden", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054447", "hw": "van wyck brooks", "pos": "phrase", "ipa": "/væn wɪk brʊks/", "vi": "nhà phê bình Van Wyck Brooks", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054448", "hw": "vertical stabiliser", "pos": "phrase", "ipa": "/ˈvɜːrtɪkəl ˈsteɪbəlaɪzər/", "vi": "cánh đuôi đứng ổn định máy bay", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054449", "hw": "vox populi", "pos": "phrase", "ipa": "/vɑːks ˈpɑːpjʊlaɪ/", "vi": "tiếng nói của nhân dân; dư luận", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054450", "hw": "warren gamaliel harding", "pos": "phrase", "ipa": "/ˈwɔːrən ɡəˈmeɪliəl ˈhɑːrdɪŋ/", "vi": "Tổng thống Mỹ Warren G. Harding", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054451", "hw": "weddell sea", "pos": "phrase", "ipa": "/ˈwɛdəl siː/", "vi": "vùng biển Weddell ở Nam Cực", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054452", "hw": "akans", "pos": "noun", "ipa": "/əˈkɑːnz/", "vi": "người dân tộc và tiếng Akan ở Ghana", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054453", "hw": "aldehydes", "pos": "noun", "ipa": "/ˈældɪhaɪdz/", "vi": "các hợp chất an-đê-hít hóa học", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054454", "hw": "allises", "pos": "noun", "ipa": "/ˈælɪsɪz/", "vi": "loài cá mòi allis shad châu Âu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054455", "hw": "arthritics", "pos": "noun", "ipa": "/ɑːrˈθrɪtɪks/", "vi": "những bệnh nhân bị viêm khớp xương", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054456", "hw": "astigmatisms", "pos": "noun", "ipa": "/əˈstɪɡmətɪzəmz/", "vi": "các tật khúc xạ loạn thị của mắt", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054457", "hw": "barbarities", "pos": "noun", "ipa": "/bɑːrˈbærətiz/", "vi": "hành vi man rợ tàn bạo dã man", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054458", "hw": "berliozes", "pos": "noun", "ipa": "/ˈbɛərlioʊzɪz/", "vi": "nhà soạn nhạc Pháp Hector Berlioz", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054459", "hw": "birdcages", "pos": "noun", "ipa": "/ˈbɜːrdkeɪdʒɪz/", "vi": "lồng nuôi chim bằng nan sắt tre", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054460", "hw": "birthmarks", "pos": "noun", "ipa": "/ˈbɜːrθmɑːrks/", "vi": "vết chàm; vết bớt bẩm sinh trên da", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054461", "hw": "blackfeet", "pos": "noun", "ipa": "/ˈblækfiːt/", "vi": "bộ tộc thổ dân Da Đỏ Blackfoot Mỹ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054462", "hw": "blackfoots", "pos": "noun", "ipa": "/ˈblækfʊts/", "vi": "người thuộc bộ tộc Blackfoot", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054463", "hw": "bloemfonteins", "pos": "noun", "ipa": "/ˈbluːmfɑːnteɪnz/", "vi": "thành phố Bloemfontein Nam Phi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054464", "hw": "bolshevisms", "pos": "noun", "ipa": "/ˈboʊlʃəvɪzəmz/", "vi": "chủ nghĩa Bôn-sê-vích Nga", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054465", "hw": "cagneys", "pos": "noun", "ipa": "/ˈkæɡniz/", "vi": "nam diễn viên Mỹ James Cagney", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054466", "hw": "calyxes", "pos": "noun", "ipa": "/ˈkeɪlɪksɪz/", "vi": "đài hoa nâng đỡ cánh hoa", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054467", "hw": "candelabras", "pos": "noun", "ipa": "/ˌkændəˈlɑːbrəz/", "vi": "giá cắm nhiều nhánh nến trang trí", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054468", "hw": "cannulas", "pos": "noun", "ipa": "/ˈkænjʊləz/", "vi": "ống thông kim luồn đưa thuốc y tế", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054469", "hw": "carrefours", "pos": "noun", "ipa": "/ˈkærəfʊərz/", "vi": "ngã tư đường; quảng trường giao lộ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054470", "hw": "cartwheeled", "pos": "verb", "ipa": "/ˈkɑːrtwiːld/", "vi": "đã nhào lộn bánh xe nghiêng người", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054471", "hw": "cartwheeling", "pos": "verb", "ipa": "/ˈkɑːrtwiːlɪŋ/", "vi": "đang nhào lộn bánh xe một tay", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054472", "hw": "cartwheels", "pos": "noun", "ipa": "/ˈkɑːrtwiːlz/", "vi": "động tác nhào lộn bánh xe thể dục", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054473", "hw": "caxtons", "pos": "noun", "ipa": "/ˈkækstənz/", "vi": "nhà in ấn đầu tiên William Caxton", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054474", "hw": "charlottetowns", "pos": "noun", "ipa": "/ˈʃɑːrləttaʊnz/", "vi": "thành phố cảng Charlottetown Canada", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054475", "hw": "citrons", "pos": "noun", "ipa": "/ˈsɪtrənz/", "vi": "quả thanh yên thuộc chi cam chanh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054476", "hw": "clotheslines", "pos": "noun", "ipa": "/ˈkloʊðzlaɪnz/", "vi": "dây căng phơi quần áo ngoài trời", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054477", "hw": "codifications", "pos": "noun", "ipa": "/ˌkɑːdɪfɪˈkeɪʃənz/", "vi": "sự pháp điển hóa hệ thống luật", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054478", "hw": "codons", "pos": "noun", "ipa": "/ˈkoʊdɑːnz/", "vi": "bộ ba mã hóa di truyền trên mARN", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054479", "hw": "contusions", "pos": "noun", "ipa": "/kənˈtuːʒənz/", "vi": "vết đụng dập bầm tím dưới da", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054480", "hw": "cortinae", "pos": "noun", "ipa": "/kɔːrˈtaɪniː/", "vi": "màng mạng nhện che phiến nấm mốc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054481", "hw": "cortinas", "pos": "noun", "ipa": "/kɔːrˈtiːnəz/", "vi": "lớp màng tơ mỏng bao quanh nấm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054482", "hw": "crannies", "pos": "noun", "ipa": "/ˈkræniz/", "vi": "khe nứt nhỏ; kẽ hở hốc tường", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054483", "hw": "cretins", "pos": "noun", "ipa": "/ˈkriːtɪnz/", "vi": "người bệnh đần độn do suy giáp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054484", "hw": "dayans", "pos": "noun", "ipa": "/daɪˈjɑːnz/", "vi": "tướng lĩnh Moshe Dayan của Israel", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054485", "hw": "delacroixes", "pos": "noun", "ipa": "/ˌdɛləˈkrwɑːzɪz/", "vi": "danh họa lãng mạn Eugène Delacroix", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054486", "hw": "elmwoods", "pos": "noun", "ipa": "/ˈɛlmwʊdz/", "vi": "gỗ cây du dùng đóng đồ nội thất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054487", "hw": "endocrinologists", "pos": "noun", "ipa": "/ˌɛndoʊkrɪˈnɑːlədʒɪsts/", "vi": "các bác sĩ chuyên khoa nội tiết", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054488", "hw": "fellinis", "pos": "noun", "ipa": "/fɛˈliːniz/", "vi": "đạo diễn điện ảnh Federico Fellini", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054489", "hw": "filers", "pos": "noun", "ipa": "/ˈfaɪlərz/", "vi": "người nộp tờ khai hồ sơ thuế", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054490", "hw": "finickier", "pos": "adj", "ipa": "/ˈfɪnɪkiər/", "vi": "kén chọn cẩn thận tỉ mỉ hơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054491", "hw": "finickiest", "pos": "adj", "ipa": "/ˈfɪnɪkiɪst/", "vi": "kén chọn cẩn thận cầu kỳ nhất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054492", "hw": "firenzes", "pos": "noun", "ipa": "/fɪˈrɛntseɪz/", "vi": "thành phố Florence Firenze của Ý", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054493", "hw": "gauris", "pos": "noun", "ipa": "/ˈɡaʊriz/", "vi": "nữ thần Gauri mẹ vàng Ấn Độ giáo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054494", "hw": "gazillions", "pos": "noun", "ipa": "/ɡəˈzɪljənz/", "vi": "hằng hà sa số; số lượng cực lớn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054495", "hw": "ghbs", "pos": "noun", "ipa": "/ˌdʒiː.eɪtʃˈbiːz/", "vi": "chất ức chế thần kinh GHB", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054496", "hw": "gluttons", "pos": "noun", "ipa": "/ˈɡlʌtənz/", "vi": "những kẻ phàm ăn tục uống háu đói", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054497", "hw": "goldstones", "pos": "noun", "ipa": "/ˈɡoʊldstoʊnz/", "vi": "thủy tinh lấp lánh ánh kim sa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054498", "hw": "goners", "pos": "noun", "ipa": "/ˈɡɔːnərz/", "vi": "người hết hy vọng; người sắp chết", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054499", "hw": "gorkies", "pos": "noun", "ipa": "/ˈɡɔːrkiz/", "vi": "đại văn hào Nga Maxim Gorky", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054500", "hw": "grantees", "pos": "noun", "ipa": "/ɡrænˈtiːz/", "vi": "người được nhận tài trợ học bổng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054501", "hw": "guardrails", "pos": "noun", "ipa": "/ˈɡɑːrdreɪlz/", "vi": "lan can chắn an toàn mép đường", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Validation
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

assert len(part5_data) == 100, f"Length is {len(part5_data)}"

with open('scratch/b31_r09_raw_p5.json') as f:
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

with open('scratch/b31_r09_p5.json', 'w', encoding='utf-8') as f:
    json.dump(part5_data, f, ensure_ascii=False, indent=2)

print("Validated and saved 100 items for Part 5")
