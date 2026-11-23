import json
import re

items = [
    {"id": "lex.en.200k.041902", "hw": "cysts", "pos": "noun", "ipa": "/sɪsts/", "vi": "các nang; những u nang", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041903", "hw": "dahs", "pos": "noun", "ipa": "/dɑːz/", "vi": "tiếng gạch ngang mã Morse", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041904", "hw": "delinquents", "pos": "noun", "ipa": "/dɪˈlɪŋkwənts/", "vi": "những kẻ phạm pháp vị thành niên", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041905", "hw": "deodorants", "pos": "noun", "ipa": "/diˈoʊdərənts/", "vi": "các chất khử mùi cơ thể", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041906", "hw": "dobsons", "pos": "noun", "ipa": "/ˈdɑːbsənz/", "vi": "ấu trùng bọ cánh rộng làm mồi", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041907", "hw": "erasmuses", "pos": "noun", "ipa": "/ɪˈræzməsɪz/", "vi": "các học giả Erasmus", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041908", "hw": "felines", "pos": "noun", "ipa": "/ˈfiːlaɪnz/", "vi": "các loài động vật họ mèo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041909", "hw": "fickler", "pos": "adj", "ipa": "/ˈfɪklər/", "vi": "thất thường hơn; dễ đổi thay hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041910", "hw": "ficklest", "pos": "adj", "ipa": "/ˈfɪklɪst/", "vi": "thất thường nhất; dễ đổi thay nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041911", "hw": "galilees", "pos": "noun", "ipa": "/ˈɡælɪliːz/", "vi": "các tiền sảnh nhà thờ cổ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041912", "hw": "gallups", "pos": "noun", "ipa": "/ˈɡæləps/", "vi": "các cuộc thăm dò dư luận Gallup", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041913", "hw": "hangouts", "pos": "noun", "ipa": "/ˈhæŋaʊts/", "vi": "các nơi chốn tụ tập quen thuộc", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041914", "hw": "hensons", "pos": "noun", "ipa": "/ˈhɛnsənz/", "vi": "những người họ Henson", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041915", "hw": "hubbles", "pos": "noun", "ipa": "/ˈhʌbəlz/", "vi": "các kính thiên văn Hubble", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041916", "hw": "inhalations", "pos": "noun", "ipa": "/ˌɪnhəˈleɪʃənz/", "vi": "các hơi hít vào; lần xông thuốc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041917", "hw": "jaggeder", "pos": "adj", "ipa": "/ˈdʒæɡɪdər/", "vi": "lởm chởm hơn; răng cưa hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041918", "hw": "jaggedest", "pos": "adj", "ipa": "/ˈdʒæɡɪdɪst/", "vi": "lởm chởm nhất; gồ ghề nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041919", "hw": "joachims", "pos": "noun", "ipa": "/ˈjoʊɑːkɪmz/", "vi": "những người tên Joachim", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041920", "hw": "jvs", "pos": "noun", "ipa": "/ˌdʒeɪˈviːz/", "vi": "các công ty liên doanh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041921", "hw": "kants", "pos": "noun", "ipa": "/kɑːnts/", "vi": "những triết gia kiểu Kant", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041922", "hw": "lasagnas", "pos": "noun", "ipa": "/ləˈzɑːnjəz/", "vi": "các đĩa bánh lasagna nướng", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041923", "hw": "leaflets", "pos": "noun", "ipa": "/ˈliːflɪts/", "vi": "các tờ rơi; lá chét nhỏ", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041924", "hw": "mcintoshes", "pos": "noun", "ipa": "/ˈmækɪntɑːʃɪz/", "vi": "các quả táo McIntosh; áo mưa Mac", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041925", "hw": "murkier", "pos": "adj", "ipa": "/ˈmɜːrkiər/", "vi": "tối tăm hơn; âm u u ám hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041926", "hw": "murkiest", "pos": "adj", "ipa": "/ˈmɜːrkiɪst/", "vi": "tối tăm nhất; âm u u ám nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041927", "hw": "nickelodeons", "pos": "noun", "ipa": "/ˌnɪkəˈloʊdiənz/", "vi": "các rạp chiếu phim 5 xu cổ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041928", "hw": "omens", "pos": "noun", "ipa": "/ˈoʊmənz/", "vi": "các điềm báo trước", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041929", "hw": "pallets", "pos": "noun", "ipa": "/ˈpæləts/", "vi": "các tấm nâng hàng; pallet gỗ", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041930", "hw": "patriarchies", "pos": "noun", "ipa": "/ˈpeɪtriɑːrkiz/", "vi": "các chế độ gia trưởng phụ hệ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041931", "hw": "patsies", "pos": "noun", "ipa": "/ˈpætsiz/", "vi": "những kẻ ngây thơ bị giật dây", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041932", "hw": "perming", "pos": "verb", "ipa": "/ˈpɜːrmɪŋ/", "vi": "đang uốn tóc quăn gợn sóng", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041933", "hw": "perms", "pos": "noun", "ipa": "/ˈpɜːrmz/", "vi": "các kiểu tóc uốn lọn quăn", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041934", "hw": "philanthropists", "pos": "noun", "ipa": "/fɪˈlænθrəpɪsts/", "vi": "các nhà từ thiện nhân đức", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041935", "hw": "piedmonts", "pos": "noun", "ipa": "/ˈpiːdmɑːnts/", "vi": "các vùng đồi dưới chân núi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041936", "hw": "pintos", "pos": "noun", "ipa": "/ˈpɪntoʊz/", "vi": "những con ngựa khoang đốm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041937", "hw": "pontiacs", "pos": "noun", "ipa": "/ˈpɑːntiæks/", "vi": "các xe hơi Pontiac; tù trưởng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041938", "hw": "prcs", "pos": "noun", "ipa": "/ˌpiːɑːrˈsiːz/", "vi": "các đại diện nước CHND Trung Hoa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041939", "hw": "predictors", "pos": "noun", "ipa": "/prɪˈdɪktərz/", "vi": "các yếu tố dự báo; người dự đoán", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041940", "hw": "qings", "pos": "noun", "ipa": "/tʃɪŋz/", "vi": "các hoàng đế triều đại nhà Thanh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041941", "hw": "retainers", "pos": "noun", "ipa": "/rɪˈteɪnərz/", "vi": "phí duy trì dịch vụ; gia nhân", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041942", "hw": "salients", "pos": "noun", "ipa": "/ˈseɪliənts/", "vi": "các điểm nhô ra chiến tuyến", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041943", "hw": "schematics", "pos": "noun", "ipa": "/skɪˈmætɪks/", "vi": "các sơ đồ nguyên lý mạch điện", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041944", "hw": "separatists", "pos": "noun", "ipa": "/ˈsɛprətɪsts/", "vi": "những người theo phái ly khai", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041945", "hw": "serbs", "pos": "noun", "ipa": "/sɜːrbz/", "vi": "những người dân Serbia", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041946", "hw": "snippets", "pos": "noun", "ipa": "/ˈsnɪpɪts/", "vi": "các đoạn trích ngắn; mẩu tin", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041947", "hw": "spielbergs", "pos": "noun", "ipa": "/ˈspiːlbɜːrɡz/", "vi": "những đạo diễn kiểu Spielberg", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041948", "hw": "spokeswomen", "pos": "noun", "ipa": "/ˈspoʊkswɪmɪn/", "vi": "các nữ phát ngôn viên", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041949", "hw": "stinkier", "pos": "adj", "ipa": "/ˈstɪŋkiər/", "vi": "hôi hám hơn; nặng mùi hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041950", "hw": "stinkiest", "pos": "adj", "ipa": "/ˈstɪŋkiɪst/", "vi": "hôi hám nhất; nặng mùi nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041951", "hw": "tcps", "pos": "noun", "ipa": "/ˌtiːsiːˈpiːz/", "vi": "các giao thức truyền tải TCP", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041952", "hw": "untimelier", "pos": "adj", "ipa": "/ʌnˈtaɪmliər/", "vi": "không đúng lúc hơn; quá sớm hơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041953", "hw": "untimeliest", "pos": "adj", "ipa": "/ʌnˈtaɪmliɪst/", "vi": "không đúng lúc nhất; non yểu nhất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041954", "hw": "woofs", "pos": "noun", "ipa": "/wʊfs/", "vi": "tiếng chó sủa gâu gâu; sợi ngang", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041955", "hw": "yakked", "pos": "verb", "ipa": "/jækt/", "vi": "đã ba hoa tán gẫu liên hồi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041956", "hw": "yakking", "pos": "verb", "ipa": "/ˈjækɪŋ/", "vi": "đang ba hoa tán gẫu liên hồi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041957", "hw": "agave family", "pos": "phrase", "ipa": "", "vi": "họ cây thùa dứa sợi", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041958", "hw": "alan stewart paton", "pos": "phrase", "ipa": "", "vi": "nhà văn Alan Paton", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041959", "hw": "alveolar artery", "pos": "phrase", "ipa": "", "vi": "động mạch huyệt răng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041960", "hw": "american agave", "pos": "phrase", "ipa": "", "vi": "cây thùa Mỹ; cây agao Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041961", "hw": "amphetamine sulfate", "pos": "phrase", "ipa": "", "vi": "thuốc amphetamine sulfate", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041962", "hw": "andaman sea", "pos": "phrase", "ipa": "", "vi": "vùng biển Andaman", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041963", "hw": "annular eclipse", "pos": "phrase", "ipa": "", "vi": "nhật thực hình khuyên tròn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041964", "hw": "argus pheasant", "pos": "phrase", "ipa": "", "vi": "chim trĩ sao Argus", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041965", "hw": "authoring language", "pos": "phrase", "ipa": "", "vi": "ngôn ngữ lập trình tác giả", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041966", "hw": "azerbaijani republic", "pos": "phrase", "ipa": "", "vi": "Cộng hòa Azerbaijan", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041967", "hw": "bacon rind", "pos": "phrase", "ipa": "", "vi": "bì thịt xông khói; da ba rọi", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041968", "hw": "batten down", "pos": "phrase", "ipa": "", "vi": "chèn chặt cửa nẹp chống bão", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041969", "hw": "becket bend", "pos": "phrase", "ipa": "", "vi": "mối thắt nối dây Becket", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041970", "hw": "beef loin", "pos": "phrase", "ipa": "", "vi": "thịt thăn lưng bò tơ", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041971", "hw": "benedictine order", "pos": "phrase", "ipa": "", "vi": "Dòng tu Biển Đức Công giáo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041972", "hw": "billiard parlor", "pos": "phrase", "ipa": "", "vi": "phòng chơi bi-a; quán bida", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041973", "hw": "black huckleberry", "pos": "phrase", "ipa": "", "vi": "cây việt quất đen Gaylussacia", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041974", "hw": "blaise pascal", "pos": "phrase", "ipa": "", "vi": "nhà bác học Blaise Pascal", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041975", "hw": "box huckleberry", "pos": "phrase", "ipa": "", "vi": "cây việt quất bụi hộp", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041976", "hw": "bristle brush", "pos": "phrase", "ipa": "", "vi": "bàn chải sợi lông cứng", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041977", "hw": "bristle grass", "pos": "phrase", "ipa": "", "vi": "cỏ lông cứng; cỏ đuôi chồn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041978", "hw": "brittany spaniel", "pos": "phrase", "ipa": "", "vi": "giống chó săn chỉ điểm Brittany", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041979", "hw": "bur grass", "pos": "phrase", "ipa": "", "vi": "cỏ cát quả gai dính", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041980", "hw": "canola oil", "pos": "phrase", "ipa": "", "vi": "dầu hạt cải canola tinh luyện", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041981", "hw": "cape marigold", "pos": "phrase", "ipa": "", "vi": "hoa cúc vạn thọ Cape Nam Phi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041982", "hw": "capillary tubing", "pos": "phrase", "ipa": "", "vi": "ống dẫn mao quản thủy tinh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041983", "hw": "cavity resonator", "pos": "phrase", "ipa": "", "vi": "khoang cộng hưởng vi sóng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041984", "hw": "charles sanders peirce", "pos": "phrase", "ipa": "", "vi": "nhà triết học Charles S. Peirce", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041985", "hw": "chinook jargon", "pos": "phrase", "ipa": "", "vi": "tiếng bồi thương mại Chinook", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041986", "hw": "clary sage", "pos": "phrase", "ipa": "", "vi": "cây xô thơm hoa tím clary", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041987", "hw": "climbing salamander", "pos": "phrase", "ipa": "", "vi": "kỳ giông trèo cây Bắc Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041988", "hw": "cochin china", "pos": "phrase", "ipa": "", "vi": "giống gà lông xù Cochin", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041989", "hw": "common iguana", "pos": "phrase", "ipa": "", "vi": "rồng đất xanh; cự đà Nam Mỹ", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041990", "hw": "congenital abnormality", "pos": "phrase", "ipa": "", "vi": "dị tật bất thường bẩm sinh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041991", "hw": "crepe myrtle", "pos": "phrase", "ipa": "", "vi": "cây hoa tường vi; bằng lăng sẻ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041992", "hw": "dangling modifier", "pos": "phrase", "ipa": "", "vi": "bổ ngữ treo lơ lửng sai ngữ pháp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041993", "hw": "domingo de guzman", "pos": "phrase", "ipa": "", "vi": "Thánh Đa Minh Guzman", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041994", "hw": "drop scone", "pos": "phrase", "ipa": "", "vi": "bánh scone rán chảo nhỏ", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041995", "hw": "eastern chipmunk", "pos": "phrase", "ipa": "", "vi": "sóc chuột sọc miền đông", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041996", "hw": "epidemic encephalitis", "pos": "phrase", "ipa": "", "vi": "viêm não truyền nhiễm dịch tễ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041997", "hw": "epsilon toxin", "pos": "phrase", "ipa": "", "vi": "ngoại độc tố epsilon vi khuẩn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041998", "hw": "excitable area", "pos": "phrase", "ipa": "", "vi": "vùng vỏ não kích thích vận động", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041999", "hw": "finger cymbals", "pos": "phrase", "ipa": "", "vi": "chũm chọe xỏ ngón tay múa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042000", "hw": "fourth ventricle", "pos": "phrase", "ipa": "", "vi": "não thất bốn của não bộ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042001", "hw": "franz joseph haydn", "pos": "phrase", "ipa": "", "vi": "nhạc sĩ Franz Joseph Haydn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

with open('scratch/b29_r04_raw_p5.json') as f:
    raw = json.load(f)

assert len(items) == 100, f"Expected 100 items, got {len(items)}"
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}

for idx, (it, r) in enumerate(zip(items, raw)):
    assert it['id'] == r['id'], f"ID mismatch: {it['id']} vs {r['id']}"
    assert it['hw'] == r['hw'], f"HW mismatch: {it['hw']} vs {r['hw']}"
    assert it['pos'] in allowed_pos, f"Invalid POS {it['pos']} for {it['id']}"
    assert len(it['vi']) > 0, f"Empty VI for {it['id']}"
    assert len(it['vi']) <= 35, f"Invalid VI length ({len(it['vi'])}) for {it['id']}: {it['vi']}"
    if it['pos'] != 'phrase' and ' ' not in it['hw']:
        assert it['ipa'].startswith('/') and it['ipa'].endswith('/') and it['ipa'].count('/') == 2, f"Invalid IPA for {it['id']}: {it['ipa']}"

with open('scratch/b29_r04_p5.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"Batch 29 Round 4 Part 5 validated and written successfully. Total items: {len(items)}")
