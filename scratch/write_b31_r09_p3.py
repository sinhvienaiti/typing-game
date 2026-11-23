# -*- coding: utf-8 -*-
import json

part3_data = [
  {"id": "lex.en.200k.054202", "hw": "john speke", "pos": "phrase", "ipa": "/dʒɑːn spiːk/", "vi": "nhà thám hiểm Anh John Speke", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054203", "hw": "karl adolph verner", "pos": "phrase", "ipa": "/kɑːrl ˈeɪdɒlf ˈvɜːrnər/", "vi": "nhà ngôn ngữ học Karl Verner", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054204", "hw": "karl jaspers", "pos": "phrase", "ipa": "/kɑːrl ˈjæspərz/", "vi": "triết gia hiện sinh Karl Jaspers", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054205", "hw": "karl waldemar ziegler", "pos": "phrase", "ipa": "/kɑːrl ˈvɑːldəmɑːr ˈtsiːɡlər/", "vi": "nhà hóa học Nobel Karl Ziegler", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054206", "hw": "kidney vetch", "pos": "phrase", "ipa": "/ˈkɪdni vɛtʃ/", "vi": "cây cỏ thận hoa vàng dược liệu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054207", "hw": "konrad adenauer", "pos": "phrase", "ipa": "/ˈkɑːnræd ˈædənˌaʊər/", "vi": "Thủ tướng Đức Konrad Adenauer", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054208", "hw": "konrad zacharias lorenz", "pos": "phrase", "ipa": "/ˈkɑːnræd ˌzækəˈraɪəs ˈlɔːrɛnts/", "vi": "nhà tập tính học Konrad Lorenz", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054209", "hw": "little lord fauntleroy", "pos": "phrase", "ipa": "/ˈlɪtl lɔːrd ˈfɔːntləroɪ/", "vi": "cậu bé lễ phép công tử bột", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054210", "hw": "lord of misrule", "pos": "phrase", "ipa": "/lɔːrd əv mɪsˈruːl/", "vi": "chúa quậy phá trong lễ Giáng sinh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054211", "hw": "louis leakey", "pos": "phrase", "ipa": "/ˈluːi ˈliːki/", "vi": "nhà cổ nhân học Louis Leakey", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054212", "hw": "mary leakey", "pos": "phrase", "ipa": "/ˈmɛri ˈliːki/", "vi": "nhà khảo cổ học nữ Mary Leakey", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054213", "hw": "monoamine oxidase", "pos": "phrase", "ipa": "/ˌmɑːnoʊˈæmiːn ˈɑːksɪdeɪs/", "vi": "enzym oxy hóa monoamine oxidase", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054214", "hw": "nigella sativa", "pos": "phrase", "ipa": "/naɪˈdʒɛlə səˈtiːvə/", "vi": "cây thì là đen nigella hạt đen thơm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054215", "hw": "operant conditioning", "pos": "phrase", "ipa": "/ˈɑːpərənt kənˈdɪʃənɪŋ/", "vi": "điều kiện hóa thao tác tâm lý học", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054216", "hw": "oxbow lake", "pos": "phrase", "ipa": "/ˈɑːksboʊ leɪk/", "vi": "hồ móng ngựa từ khúc sông uốn cong", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054217", "hw": "paolo veronese", "pos": "phrase", "ipa": "/ˈpaʊloʊ ˌvɛroʊˈneɪzeɪ/", "vi": "danh họa Ý Paolo Veronese", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054218", "hw": "papillary muscle", "pos": "phrase", "ipa": "/ˈpæpɪlɛri ˈmʌsəl/", "vi": "cơ nhú trong tâm thất của tim", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054219", "hw": "petronius arbiter", "pos": "phrase", "ipa": "/pɪˈtroʊniəs ˈɑːrbɪtər/", "vi": "nhà văn La Mã Petronius Arbiter", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054220", "hw": "pinnate leaf", "pos": "phrase", "ipa": "/ˈpɪneɪt liːf/", "vi": "lá kép hình lông chim thực vật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054221", "hw": "prepositional object", "pos": "phrase", "ipa": "/ˌprɛpəˈzɪʃənəl ˈɑːbdʒɪkt/", "vi": "tân ngữ đi theo sau giới từ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054222", "hw": "prepositional phrase", "pos": "phrase", "ipa": "/ˌprɛpəˈzɪʃənəl freɪz/", "vi": "cụm giới từ trong ngữ pháp", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054223", "hw": "prostatic adenocarcinoma", "pos": "phrase", "ipa": "/prɑːˈstætɪk ˌædɪnoʊˌkɑːrsɪˈnoʊmə/", "vi": "ung thư biểu mô tuyến tiền liệt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054224", "hw": "richard burbage", "pos": "phrase", "ipa": "/ˈrɪtʃərd ˈbɜːrbɪdʒ/", "vi": "nam diễn viên kịch Richard Burbage", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054225", "hw": "richard leakey", "pos": "phrase", "ipa": "/ˈrɪtʃərd ˈliːki/", "vi": "nhà cổ sinh học Richard Leakey", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054226", "hw": "rosh hashanah", "pos": "phrase", "ipa": "/ˌrɔːʃ həˈʃɑːnə/", "vi": "Tết năm mới Rosh Hashanah Do Thái", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054227", "hw": "sagittal suture", "pos": "phrase", "ipa": "/ˈsædʒɪtəl ˈsuːtʃər/", "vi": "đường khớp dọc đỉnh hộp sọ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054228", "hw": "scaly anteater", "pos": "phrase", "ipa": "/ˈskeɪli ˈæntiːtər/", "vi": "loài tê tê có vảy ăn kiến", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054229", "hw": "sclerotic coat", "pos": "phrase", "ipa": "/skləˈrɑːtɪk koʊt/", "vi": "màng củng mạc bảo vệ nhãn cầu mắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054230", "hw": "sheep fescue", "pos": "phrase", "ipa": "/ʃiːp ˈfɛskjuː/", "vi": "cỏ đuôi trâu cừu làm bãi chăn thả", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054231", "hw": "slobber over", "pos": "phrase", "ipa": "/ˈslɑːbər ˈoʊvər/", "vi": "chảy dãi thèm thuồng; xuýt xoa", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054232", "hw": "smart aleck", "pos": "phrase", "ipa": "/smɑːrt ˈælɪk/", "vi": "kẻ tinh tướng; kẻ làm ra vẻ ta đây", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054233", "hw": "soda jerker", "pos": "phrase", "ipa": "/ˈsoʊdə ˈdʒɜːrkər/", "vi": "nhân viên pha chế soda quầy nước", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054234", "hw": "sotto voce", "pos": "phrase", "ipa": "/ˌsɑːtoʊ ˈvoʊtʃeɪ/", "vi": "nói nhỏ giọng; thì thầm khe khẽ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054235", "hw": "splenic fever", "pos": "phrase", "ipa": "/ˈsplɛnɪk ˈfiːvər/", "vi": "bệnh than lây từ động vật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054236", "hw": "stapling machine", "pos": "phrase", "ipa": "/ˈsteɪplɪŋ məˈʃiːn/", "vi": "máy dập ghim giấy; súng bắn ghim", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054237", "hw": "superior mesenteric artery", "pos": "phrase", "ipa": "/suːˈpɪəriər ˌmɛzənˈtɛrɪk ˈɑːrtəri/", "vi": "động mạch mạc treo tràng trên ruột", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054238", "hw": "superoxide anion", "pos": "phrase", "ipa": "/ˌsuːpərˈɑːksaɪd ˈænaɪən/", "vi": "anion superoxide gốc tự do oxy", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054239", "hw": "suspender belt", "pos": "phrase", "ipa": "/səˈspɛndər bɛlt/", "vi": "đai nịt giữ vớ dài phụ nữ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054240", "hw": "systemic lupus erythematosus", "pos": "phrase", "ipa": "/sɪˈstɛmɪk ˈluːpəs ˌɛrɪˌθiːməˈtoʊsəs/", "vi": "bệnh lupus ban đỏ hệ thống", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054241", "hw": "tannic acid", "pos": "phrase", "ipa": "/ˈtænɪk ˈæsɪd/", "vi": "axit tannic trong vỏ cây trà", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054242", "hw": "terminus ad quem", "pos": "phrase", "ipa": "/ˈtɜːrmɪnəs æd kwɛm/", "vi": "thời hạn cuối cùng; điểm kết thúc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054243", "hw": "valedictory address", "pos": "phrase", "ipa": "/ˌvælɪˈdɪktəri əˈdrɛs/", "vi": "bài diễn văn chia tay tốt nghiệp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054244", "hw": "valedictory speaker", "pos": "phrase", "ipa": "/ˌvælɪˈdɪktəri ˈspiːkər/", "vi": "học sinh đọc diễn văn tốt nghiệp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054245", "hw": "yellow jacaranda", "pos": "phrase", "ipa": "/ˈjɛloʊ ˌdʒækəˈrændə/", "vi": "cây hoa điệp vàng rực rỡ nhiệt đới", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054246", "hw": "adjudicators", "pos": "noun", "ipa": "/əˈdʒuːdɪkeɪtərz/", "vi": "những người phân xử; trọng tài", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054247", "hw": "albees", "pos": "noun", "ipa": "/ˈɔːlbiz/", "vi": "nhà biên kịch Edward Albee", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054248", "hw": "appalachianses", "pos": "noun", "ipa": "/ˌæpəˈleɪtʃənzɪz/", "vi": "các dãy núi Appalachian đông Mỹ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054249", "hw": "ardses", "pos": "noun", "ipa": "/ˈɑːrdzɪz/", "vi": "hội chứng suy hô hấp cấp ARDS", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054250", "hw": "arleses", "pos": "noun", "ipa": "/ˈɑːrlzɪz/", "vi": "tiền đặt cọc giữ chỗ giao kèo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054251", "hw": "athanasiuses", "pos": "noun", "ipa": "/ˌæθəˈneɪʒəsɪz/", "vi": "Thánh Athanasius xứ Alexandria", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054252", "hw": "bahasas", "pos": "noun", "ipa": "/bəˈhɑːsəz/", "vi": "tiếng Bahasa của Malaysia Indonesia", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054253", "hw": "bambini", "pos": "noun", "ipa": "/bæmˈbiːni/", "vi": "những đứa trẻ sơ sinh bé bỏng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054254", "hw": "bambinos", "pos": "noun", "ipa": "/bæmˈbiːnoʊz/", "vi": "các em bé sơ sinh bụ bẫm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054255", "hw": "beanstalks", "pos": "noun", "ipa": "/ˈbiːnstɔːks/", "vi": "thân cây đậu leo cao vút cổ tích", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054256", "hw": "biers", "pos": "noun", "ipa": "/bɪərz/", "vi": "cáng đặt áo quan; cáng quan tài", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054257", "hw": "biplanes", "pos": "noun", "ipa": "/ˈbaɪpleɪnz/", "vi": "máy bay cổ hai tầng cánh song song", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054258", "hw": "bogies", "pos": "noun", "ipa": "/ˈboʊɡiz/", "vi": "bóng ma; xe trượt toa xe lửa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054259", "hw": "callower", "pos": "adj", "ipa": "/ˈkæloʊər/", "vi": "non nớt thiếu kinh nghiệm hơn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054260", "hw": "callowest", "pos": "adj", "ipa": "/ˈkæloʊɪst/", "vi": "non nớt thiếu kinh nghiệm nhất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054261", "hw": "candours", "pos": "noun", "ipa": "/ˈkændərz/", "vi": "tính ngay thẳng thật thà bộc trực", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054262", "hw": "caravaggios", "pos": "noun", "ipa": "/ˌkærəˈvɑːdʒioʊz/", "vi": "danh họa Ý Caravaggio tài ba", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054263", "hw": "certioraris", "pos": "noun", "ipa": "/ˌsɜːrʃiəˈrɛəraɪz/", "vi": "lệnh xem xét lại bản án tòa trên", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054264", "hw": "checkerboards", "pos": "noun", "ipa": "/ˈtʃɛkərbɔːrdz/", "vi": "bàn cờ đam caro ca-rô ô vuông", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054265", "hw": "chinamans", "pos": "noun", "ipa": "/ˈtʃaɪnəmənz/", "vi": "từ miệt thị người Trung Quốc cổ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054266", "hw": "cholines", "pos": "noun", "ipa": "/ˈkoʊliːnz/", "vi": "dưỡng chất choline cho não bộ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054267", "hw": "coleopteras", "pos": "noun", "ipa": "/ˌkoʊliˈɑːptərəz/", "vi": "các loài côn trùng bộ cánh cứng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054268", "hw": "collectivists", "pos": "noun", "ipa": "/kəˈlɛktɪvɪsts/", "vi": "những người theo chủ nghĩa tập thể", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054269", "hw": "connexions", "pos": "noun", "ipa": "/kəˈnɛkʃənz/", "vi": "mối liên kết; sự kết nối quan hệ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054270", "hw": "constructivists", "pos": "noun", "ipa": "/kənˈstrʌktɪvɪsts/", "vi": "người theo chủ nghĩa kiến tạo", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054271", "hw": "cousteaus", "pos": "noun", "ipa": "/kuːˈstoʊz/", "vi": "nhà hải dương học Jacques Cousteau", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054272", "hw": "cowbells", "pos": "noun", "ipa": "/ˈkaʊbɛlz/", "vi": "chuông đeo cổ bò; chuông đồng bò", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054273", "hw": "crabbier", "pos": "adj", "ipa": "/ˈkræbiər/", "vi": "càu nhàu gắt gỏng khó chịu hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054274", "hw": "crabbiest", "pos": "adj", "ipa": "/ˈkræbiɪst/", "vi": "càu nhàu gắt gỏng khó chịu nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054275", "hw": "cracows", "pos": "noun", "ipa": "/ˈkrækaʊz/", "vi": "thành phố cổ Krakow của Ba Lan", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054276", "hw": "cretans", "pos": "noun", "ipa": "/ˈkriːtənz/", "vi": "người dân bản địa đảo Crete Hy Lạp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054277", "hw": "crocuses", "pos": "noun", "ipa": "/ˈkroʊkəsɪz/", "vi": "cây hoa nghệ tây hoa tím vàng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054278", "hw": "dagons", "pos": "noun", "ipa": "/ˈdeɪɡɒnz/", "vi": "vị thần biển cả Dagon cổ đại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054279", "hw": "diploids", "pos": "noun", "ipa": "/ˈdɪplɔɪdz/", "vi": "tế bào sinh vật lưỡng bội 2n", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054280", "hw": "disfigurements", "pos": "noun", "ipa": "/dɪsˈfɪɡjərmənts/", "vi": "những vết biến dạng làm mất thẩm mỹ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054281", "hw": "dostoyevskies", "pos": "noun", "ipa": "/ˌdɒstəˈjɛfskiz/", "vi": "đại văn hào Nga Fyodor Dostoevsky", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054282", "hw": "dressmakers", "pos": "noun", "ipa": "/ˈdrɛsmeɪkərz/", "vi": "những người thợ may váy đầm nữ", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054283", "hw": "ebses", "pos": "noun", "ipa": "/ˌiː.biːˈɛsɪz/", "vi": "hội chứng ly thượng bì bọng nước", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054284", "hw": "ecfs", "pos": "noun", "ipa": "/ˌiː.siːˈɛfs/ ", "vi": "dịch ngoại bào bao quanh tế bào", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054285", "hw": "ejectors", "pos": "noun", "ipa": "/ɪˈdʒɛktərz/", "vi": "bộ phận tống vỏ đạn; người đẩy ra", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054286", "hw": "emoted", "pos": "verb", "ipa": "/ɪˈmoʊtɪd/", "vi": "đã bộc lộ cảm xúc cường điệu kịch", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054287", "hw": "emotes", "pos": "verb", "ipa": "/ɪˈmoʊts/", "vi": "bộc lộ cảm xúc kịch; biểu cảm kịch", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054288", "hw": "emoting", "pos": "verb", "ipa": "/ɪˈmoʊtɪŋ/", "vi": "đang biểu lộ cảm xúc cường điệu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054289", "hw": "episcopalians", "pos": "noun", "ipa": "/ɪˌpɪskəˈpeɪliənz/", "vi": "tín đồ Giáo hội Giám mục Episcopal", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054290", "hw": "ermines", "pos": "noun", "ipa": "/ˈɜːrmɪnz/", "vi": "bộ lông chồn ecmin trắng quý giá", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054291", "hw": "fishnets", "pos": "noun", "ipa": "/ˈfɪʃnɛts/", "vi": "lưới đánh bắt cá; vớ lưới mắt cáo", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054292", "hw": "gallaudets", "pos": "noun", "ipa": "/ˌɡæləˈdɛts/", "vi": "nhà giáo dục Thomas H. Gallaudet", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054293", "hw": "gaskells", "pos": "noun", "ipa": "/ˈɡæskəlz/", "vi": "nữ nhà văn Elizabeth Gaskell", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054294", "hw": "gdansks", "pos": "noun", "ipa": "/ɡəˈdænsks/", "vi": "thành phố cảng Gdansk của Ba Lan", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054295", "hw": "gnats", "pos": "noun", "ipa": "/næts/", "vi": "những con muỗi mắt ruồi nhuế nhỏ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054296", "hw": "golgis", "pos": "noun", "ipa": "/ˈɡɔːldʒiz/", "vi": "bác sĩ Camillo Golgi giải Nobel", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054297", "hw": "grecians", "pos": "noun", "ipa": "/ˈɡriːʃənz/", "vi": "người Hy Lạp cổ; học giả Hy Lạp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054298", "hw": "gunboats", "pos": "noun", "ipa": "/ˈɡʌnboʊts/", "vi": "pháo hạm chiến hạm tuần tra cỡ nhỏ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054299", "hw": "headlocks", "pos": "noun", "ipa": "/ˈhɛdlɑːks/", "vi": "đòn siết chặt đầu kẹp cổ đô vật", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054300", "hw": "headpieces", "pos": "noun", "ipa": "/ˈhɛdpiːsɪz/", "vi": "mũ sắt bảo hộ; trang sức đội đầu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054301", "hw": "hookes", "pos": "noun", "ipa": "/hʊks/", "vi": "nhà khoa học phát minh Robert Hooke", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

for it in part3_data:
    it['ipa'] = it['ipa'].strip()

# Validation
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

assert len(part3_data) == 100, f"Length is {len(part3_data)}"

with open('scratch/b31_r09_raw_p3.json') as f:
    raw = json.load(f)

for i, (item, raw_item) in enumerate(zip(part3_data, raw)):
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

with open('scratch/b31_r09_p3.json', 'w', encoding='utf-8') as f:
    json.dump(part3_data, f, ensure_ascii=False, indent=2)

print("Validated and saved 100 items for Part 3")
