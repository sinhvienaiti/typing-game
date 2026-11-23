import json

# Manual cognitive QA review for Batch 29 Round 2 Part 3 (IDs 040702 to 040801)
reviewed_items = [
    {"id": "lex.en.200k.040702", "hw": "unraveled", "pos": "verb", "ipa": "/ʌnˈrævəld/", "vi": "đã tháo gỡ mối chỉ; đã làm sáng tỏ", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040703", "hw": "unraveling", "pos": "verb", "ipa": "/ʌnˈrævəlɪŋ/", "vi": "đang tháo sợi; đang làm sáng tỏ", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040704", "hw": "veterinarians", "pos": "noun", "ipa": "/ˌvɛtərəˈnɛriənz/", "vi": "bác sĩ thú y chữa bệnh thú nuôi", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040705", "hw": "vidals", "pos": "noun", "ipa": "/ˈviːdɑːlz/", "vi": "nhà văn Gore Vidal; người Vidal", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040706", "hw": "wastelands", "pos": "noun", "ipa": "/ˈweɪstlændz/", "vi": "vùng đất hoang vu cằn cỗi", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040707", "hw": "watchdogs", "pos": "noun", "ipa": "/ˈwɑːtʃdɔːɡz/", "vi": "chó canh gác; cơ quan giám sát", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040708", "hw": "waterier", "pos": "adj", "ipa": "/ˈwɔːtəriər/", "vi": "nhiều nước hơn; lỏng nhạt hơn", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040709", "hw": "wateriest", "pos": "adj", "ipa": "/ˈwɔːtəriɪst/", "vi": "loãng nhiều nước nhất; nhạt nhất", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040710", "hw": "weasels", "pos": "noun", "ipa": "/ˈwiːzəlz/", "vi": "con chồn nâu; kẻ tráo trở lươn lẹo", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040711", "hw": "yukons", "pos": "noun", "ipa": "/ˈjuːkɑːnz/", "vi": "vùng lãnh thổ Yukon Canada", "cefr": "B2", "tier": "geography", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040712", "hw": "zests", "pos": "noun", "ipa": "/zɛsts/", "vi": "vỏ chanh bào; sự hào hứng say mê", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040713", "hw": "zulus", "pos": "noun", "ipa": "/ˈzuːluːz/", "vi": "người Zulu; tiếng Zulu Nam Phi", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040714", "hw": "absorbent cotton", "pos": "phrase", "ipa": "", "vi": "bông gòn y tế thấm hút nước", "cefr": "B2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040715", "hw": "aegean civilisation", "pos": "phrase", "ipa": "", "vi": "văn minh biển Aegea thời cổ", "cefr": "C1", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040716", "hw": "alkyl radical", "pos": "phrase", "ipa": "", "vi": "gốc tự do ankyl hữu cơ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040717", "hw": "alveolar bed", "pos": "phrase", "ipa": "", "vi": "mạng lưới mao mạch phế nang", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040718", "hw": "alveolar point", "pos": "phrase", "ipa": "", "vi": "điểm huyệt phế nang hàm trên", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040719", "hw": "alveolar process", "pos": "phrase", "ipa": "", "vi": "mỏm phế nang xương hàm", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040720", "hw": "amyloid protein plaque", "pos": "phrase", "ipa": "", "vi": "mảng protein xơ amyloid não", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040721", "hw": "babylonian weeping willow", "pos": "phrase", "ipa": "", "vi": "cây liễu rủ cành Babylon", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040722", "hw": "blister blight", "pos": "phrase", "ipa": "", "vi": "bệnh phồng rộp lá chè", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040723", "hw": "brown hyena", "pos": "phrase", "ipa": "", "vi": "loài linh cẩu nâu châu Phi", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040724", "hw": "buffalo gourd", "pos": "phrase", "ipa": "", "vi": "dây bầu hoang trâu sa mạc", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040725", "hw": "buttermilk pancake", "pos": "phrase", "ipa": "", "vi": "bánh kếp nướng bơ sữa xốp", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040726", "hw": "carbon tet", "pos": "phrase", "ipa": "", "vi": "dung môi cacbon tetraclorua", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040727", "hw": "cesar franck", "pos": "phrase", "ipa": "", "vi": "nhạc sĩ César Franck", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040728", "hw": "classifying adjective", "pos": "phrase", "ipa": "", "vi": "tính từ mang tính phân loại", "cefr": "C1", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040729", "hw": "cleft palate", "pos": "phrase", "ipa": "", "vi": "chứng hở hàm ếch bẩm sinh", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040730", "hw": "communicable disease", "pos": "phrase", "ipa": "", "vi": "bệnh truyền nhiễm lây lan", "cefr": "B2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040731", "hw": "computational linguist", "pos": "phrase", "ipa": "", "vi": "chuyên gia ngôn ngữ học tính toán", "cefr": "C2", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040732", "hw": "computerized tomography", "pos": "phrase", "ipa": "", "vi": "chụp cắt lớp vi tính CT", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040733", "hw": "condenser microphone", "pos": "phrase", "ipa": "", "vi": "mi-crô dạng tụ điện condenser", "cefr": "B2", "tier": "technology", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040734", "hw": "contraceptive diaphragm", "pos": "phrase", "ipa": "", "vi": "màng ngăn âm đạo ngừa thai", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040735", "hw": "convergent thinking", "pos": "phrase", "ipa": "", "vi": "lối tư duy logic hội tụ", "cefr": "C1", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040736", "hw": "crepe jasmine", "pos": "phrase", "ipa": "", "vi": "cây ngọc bút; hoa lài tây", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040737", "hw": "de mille", "pos": "phrase", "ipa": "", "vi": "nhà biên đạo Agnes de Mille", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040738", "hw": "electric dipole", "pos": "phrase", "ipa": "", "vi": "lưỡng cực điện tích", "cefr": "C2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040739", "hw": "electric dipole moment", "pos": "phrase", "ipa": "", "vi": "mô-men lưỡng cực điện trường", "cefr": "C2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040740", "hw": "english toy spaniel", "pos": "phrase", "ipa": "", "vi": "chó cảnh spaniel đồ chơi Anh", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040741", "hw": "epistle of jeremiah", "pos": "phrase", "ipa": "", "vi": "Thư thư ký Jeremiah Kinh Thánh", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040742", "hw": "epistle of jude", "pos": "phrase", "ipa": "", "vi": "Thư của sứ đồ Giu-đe", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040743", "hw": "esprit de corps", "pos": "phrase", "ipa": "", "vi": "tinh thần đoàn kết tập thể", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040744", "hw": "ethyl chloride", "pos": "phrase", "ipa": "", "vi": "etyl clorua gây tê lạnh", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040745", "hw": "ethyl ether", "pos": "phrase", "ipa": "", "vi": "dung môi ete etylic bay hơi", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040746", "hw": "false mistletoe", "pos": "phrase", "ipa": "", "vi": "cây tầm gửi giả Bắc Mỹ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040747", "hw": "fire tongs", "pos": "phrase", "ipa": "", "vi": "cái kẹp than lò sưởi; kẹp lửa", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040748", "hw": "firmness of purpose", "pos": "phrase", "ipa": "", "vi": "sự kiên định mục đích đã định", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040749", "hw": "fish filet", "pos": "phrase", "ipa": "", "vi": "miếng phi lê nạc cá tươi", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040750", "hw": "genus calypso", "pos": "phrase", "ipa": "", "vi": "chi phong lan tiên Calypso", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040751", "hw": "genus candida", "pos": "phrase", "ipa": "", "vi": "chi nấm men gây bệnh Candida", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040752", "hw": "genus dahlia", "pos": "phrase", "ipa": "", "vi": "chi hoa thược dược nhiều cánh", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040753", "hw": "genus rhinoceros", "pos": "phrase", "ipa": "", "vi": "chi động vật tê giác một sừng", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040754", "hw": "golden aster", "pos": "phrase", "ipa": "", "vi": "hoa cúc cánh vàng sao rực rỡ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040755", "hw": "hair follicle", "pos": "phrase", "ipa": "", "vi": "nang lông chân tóc da đầu", "cefr": "B2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040756", "hw": "hemorrhagic stroke", "pos": "phrase", "ipa": "", "vi": "tai biến đột quỵ xuất huyết não", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040757", "hw": "horace walpole", "pos": "phrase", "ipa": "", "vi": "tiểu thuyết gia Horace Walpole", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040758", "hw": "husk tomato", "pos": "phrase", "ipa": "", "vi": "quả thù lù vỏ bọc; tầm bóp", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040759", "hw": "hyena dog", "pos": "phrase", "ipa": "", "vi": "chó hoang châu Phi đốm vằn", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040760", "hw": "ice tongs", "pos": "phrase", "ipa": "", "vi": "kẹp gắp đá lạnh uống nước", "cefr": "A2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040761", "hw": "implosion therapy", "pos": "phrase", "ipa": "", "vi": "liệu pháp tâm lý tràn ngập sợ", "cefr": "C2", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040762", "hw": "indelible ink", "pos": "phrase", "ipa": "", "vi": "loại mực vĩnh cửu không phai nhòe", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040763", "hw": "karl gauss", "pos": "phrase", "ipa": "", "vi": "nhà toán học thiên tài Carl Gauss", "cefr": "C1", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040764", "hw": "kilowatt hour", "pos": "phrase", "ipa": "", "vi": "ki-lô-oát giờ; số điện kWh", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040765", "hw": "krebs cycle", "pos": "phrase", "ipa": "", "vi": "chu trình axit xitric Krebs", "cefr": "C1", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040766", "hw": "kyrgyz republic", "pos": "phrase", "ipa": "", "vi": "Cộng hòa Kyrgyzstan Trung Á", "cefr": "B2", "tier": "geography", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040767", "hw": "late purple aster", "pos": "phrase", "ipa": "", "vi": "hoa cúc tây tím nở muộn thu", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040768", "hw": "lazar house", "pos": "phrase", "ipa": "", "vi": "trại cách ly bệnh phong hủi", "cefr": "C2", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040769", "hw": "lister plough", "pos": "phrase", "ipa": "", "vi": "máy cày xới tạo luống đôi", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040770", "hw": "louis pasteur", "pos": "phrase", "ipa": "", "vi": "nhà vi sinh học Louis Pasteur", "cefr": "B2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040771", "hw": "lymphatic vessel", "pos": "phrase", "ipa": "", "vi": "mạch dẫn dịch bạch huyết", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040772", "hw": "lyndon baines johnson", "pos": "phrase", "ipa": "", "vi": "tổng thống Mỹ Lyndon B. Johnson", "cefr": "B2", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040773", "hw": "marmalade plum", "pos": "phrase", "ipa": "", "vi": "quả sapoche mận mứt ngọt", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040774", "hw": "martin heidegger", "pos": "phrase", "ipa": "", "vi": "triết gia Đức Martin Heidegger", "cefr": "C2", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040775", "hw": "meadow leek", "pos": "phrase", "ipa": "", "vi": "hành đồng cỏ dại Bắc Mỹ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040776", "hw": "mennonite church", "pos": "phrase", "ipa": "", "vi": "Giáo hội Cơ đốc Mennonite", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040777", "hw": "missouri gourd", "pos": "phrase", "ipa": "", "vi": "cây bầu hoang dại Missouri", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040778", "hw": "nasal septum", "pos": "phrase", "ipa": "", "vi": "vách ngăn sống mũi giữa hai lỗ", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040779", "hw": "ooze out", "pos": "phrase", "ipa": "", "vi": "rỉ nước dịch ra; chảy từ từ ra", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040780", "hw": "ooze through", "pos": "phrase", "ipa": "", "vi": "thấm thấu qua màng; rỉ qua kẽ", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040781", "hw": "oral fissure", "pos": "phrase", "ipa": "", "vi": "khe nứt khóe mép miệng", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040782", "hw": "orange liqueur", "pos": "phrase", "ipa": "", "vi": "rượu mùi thơm vỏ cam ngọt", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040783", "hw": "percival lowell", "pos": "phrase", "ipa": "", "vi": "nhà thiên văn Percival Lowell", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040784", "hw": "pliny the elder", "pos": "phrase", "ipa": "", "vi": "học giả Pliny Già cổ La Mã", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040785", "hw": "preemptive right", "pos": "phrase", "ipa": "", "vi": "quyền ưu tiên mua cổ phần trước", "cefr": "C1", "tier": "business", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040786", "hw": "radiocarbon dating", "pos": "phrase", "ipa": "", "vi": "định tuổi bằng cacbon phóng xạ", "cefr": "B2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040787", "hw": "reciprocal ohm", "pos": "phrase", "ipa": "", "vi": "đơn vị đo độ dẫn điện siemens", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040788", "hw": "rhea americana", "pos": "phrase", "ipa": "", "vi": "loài đà điểu châu Mỹ lớn", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040789", "hw": "rush aster", "pos": "phrase", "ipa": "", "vi": "hoa cúc tây thân cỏ sậy nhỏ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040790", "hw": "sabre rattling", "pos": "phrase", "ipa": "", "vi": "sự giương oai đe dọa vũ lực", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040791", "hw": "senile psychosis", "pos": "phrase", "ipa": "", "vi": "chứng loạn thần do tuổi già lú lẫn", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040792", "hw": "shasta daisy", "pos": "phrase", "ipa": "", "vi": "hoa cúc trắng Shasta thân thảo", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040793", "hw": "shoot craps", "pos": "phrase", "ipa": "", "vi": "chơi trò lắc xí ngầu craps", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040794", "hw": "shoulder girdle", "pos": "phrase", "ipa": "", "vi": "đai xương bả vai nâng tay", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040795", "hw": "sierra madre oriental", "pos": "phrase", "ipa": "", "vi": "dãy núi Đông Sierra Madre Mexico", "cefr": "B2", "tier": "geography", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040796", "hw": "simon bolivar", "pos": "phrase", "ipa": "", "vi": "nhà giải phóng Simón Bolívar", "cefr": "B2", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040797", "hw": "sloop of war", "pos": "phrase", "ipa": "", "vi": "thuyền buồm chiến hạm pháo nhỏ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040798", "hw": "smoked haddock", "pos": "phrase", "ipa": "", "vi": "cá tuyết haddock xông khói mặn", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040799", "hw": "smooth aster", "pos": "phrase", "ipa": "", "vi": "hoa cúc sao thân nhẵn xanh", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040800", "hw": "somatic delusion", "pos": "phrase", "ipa": "", "vi": "chứng hoang tưởng cơ thể bệnh", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040801", "hw": "southeastern pocket gopher", "pos": "phrase", "ipa": "", "vi": "chuột nang má túi Đông Nam", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""}
]

# Validation
ALLOWED_POS = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}
with open('scratch/b29_r02_raw_p3.json', 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

assert len(reviewed_items) == 100, f"Expected 100 items, got {len(reviewed_items)}"
for r, rev in zip(raw_items, reviewed_items):
    assert r["id"] == rev["id"], f"ID mismatch: {r['id']} vs {rev['id']}"
    assert r["hw"] == rev["hw"], f"HW mismatch: {r['hw']} vs {rev['hw']}"
    assert rev["pos"] in ALLOWED_POS, f"Invalid POS for {rev['id']}: {rev['pos']}"
    assert 0 < len(rev["vi"]) <= 35, f"Invalid VI length ({len(rev['vi'])}) for {rev['id']}: {rev['vi']}"
    assert rev["status"] == "reviewed", f"Status must be reviewed: {rev['id']}"
    if " " not in rev["hw"]:
        assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/") and rev["ipa"].count("/") == 2, f"Invalid single-word IPA: {rev['id']}: {rev['ipa']}"

with open('scratch/b29_r02_p3.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 2 Part 3 validated and written successfully. Total items:", len(reviewed_items))
