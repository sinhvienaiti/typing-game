# -*- coding: utf-8 -*-
import json

part2_data = [
    {"id": "lex.en.200k.051602", "hw": "sinkers", "pos": "noun", "ipa": "/ˈsɪŋkərz/", "vi": "chì câu cá; cú ném bóng chìm", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051603", "hw": "sophocleses", "pos": "noun", "ipa": "/ˈsɑːfəkliːzɪz/", "vi": "nhà soạn bi kịch Sophocles", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051604", "hw": "sorties", "pos": "noun", "ipa": "/ˈsɔːrtiz/", "vi": "phi vụ bay; cuộc xuất kích đột phá", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051605", "hw": "standishes", "pos": "noun", "ipa": "/ˈstændɪʃɪz/", "vi": "khay để bút mực và nghiên mực", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051606", "hw": "statuettes", "pos": "noun", "ipa": "/ˌstætʃuˈɛts/", "vi": "các bức tượng nhỏ trang trí", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051607", "hw": "storerooms", "pos": "noun", "ipa": "/ˈstɔːrruːmz/", "vi": "các gian phòng kho chứa đồ đạc", "cefr": "b1", "tier": "general"},
    {"id": "lex.en.200k.051608", "hw": "tenners", "pos": "noun", "ipa": "/ˈtɛnərz/", "vi": "tờ tiền mười bảng; mười đô la", "cefr": "b1", "tier": "general"},
    {"id": "lex.en.200k.051609", "hw": "tricepses", "pos": "noun", "ipa": "/ˈtraɪsɛpsɪz/", "vi": "các cơ tam đầu bắp tay sau", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051610", "hw": "untidied", "pos": "adj", "ipa": "/ʌnˈtaɪdid/", "vi": "chưa được dọn dẹp; bừa bộn", "cefr": "b1", "tier": "general"},
    {"id": "lex.en.200k.051611", "hw": "untidier", "pos": "adj", "ipa": "/ʌnˈtaɪdiər/", "vi": "bừa bộn hơn; luộm thuộm hơn", "cefr": "b1", "tier": "general"},
    {"id": "lex.en.200k.051612", "hw": "untidiest", "pos": "adj", "ipa": "/ʌnˈtaɪdiɪst/", "vi": "bừa bộn nhất; luộm thuộm nhất", "cefr": "b1", "tier": "general"},
    {"id": "lex.en.200k.051613", "hw": "velodromes", "pos": "noun", "ipa": "/ˈviːlədroʊmz/", "vi": "các trường đua xe đạp lòng chảo", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051614", "hw": "washier", "pos": "adj", "ipa": "/ˈwɑːʃiər/", "vi": "loãng toẹt hơn; nhợt nhạt hơn", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051615", "hw": "washiest", "pos": "adj", "ipa": "/ˈwɑːʃiɪst/", "vi": "loãng toẹt nhất; nhợt nhạt nhất", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051616", "hw": "waveguides", "pos": "noun", "ipa": "/ˈweɪvɡaɪdz/", "vi": "ống dẫn sóng điện từ cao tần", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051617", "hw": "weills", "pos": "noun", "ipa": "/waɪlz/", "vi": "nhạc sĩ Kurt Weill của Đức", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051618", "hw": "winemakings", "pos": "noun", "ipa": "/ˈwaɪnmeɪkɪŋz/", "vi": "quy trình nghề nấu ủ rượu vang", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051619", "hw": "womanizers", "pos": "noun", "ipa": "/ˈwʊmənaɪzərz/", "vi": "những kẻ lăng nhăng tán tỉnh", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051620", "hw": "wreckers", "pos": "noun", "ipa": "/ˈrɛkərz/", "vi": "xe cứu hộ kéo xe; thợ phá dỡ tàu", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051621", "hw": "zealanders", "pos": "noun", "ipa": "/ˈziːləndərz/", "vi": "người dân vùng đảo Zealand Đan Mạch", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051622", "hw": "adlai ewing stevenson", "pos": "phrase", "ipa": "/ˈædlaɪ ˈjuːɪŋ ˈstiːvənsən/", "vi": "chính khách Adlai Ewing Stevenson", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051623", "hw": "afferent fiber", "pos": "phrase", "ipa": "/ˈæfərənt ˈfaɪbər/", "vi": "sợi thần kinh hướng tâm cảm giác", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051624", "hw": "afferent nerve", "pos": "phrase", "ipa": "/ˈæfərənt nɜːrv/", "vi": "dây thần kinh cảm giác hướng tâm", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051625", "hw": "al madinah", "pos": "phrase", "ipa": "/æl məˈdiːnə/", "vi": "thánh địa Medina ở Ả Rập Xê Út", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051626", "hw": "alfred lunt", "pos": "phrase", "ipa": "/ˈælfrɪd lʌnt/", "vi": "diễn viên kịch Alfred Lunt Mỹ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051627", "hw": "au gratin", "pos": "adj", "ipa": "/oʊ ˈɡrɑːtən/", "vi": "nướng phủ phô mai và vụn bánh mì", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051628", "hw": "beaked salmon", "pos": "phrase", "ipa": "/biːkt ˈsæmən/", "vi": "loài cá mõm nhọn gonorynchid", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051629", "hw": "beaked whale", "pos": "phrase", "ipa": "/biːkt weɪl/", "vi": "cá voi mõm khoằm đại dương", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051630", "hw": "bill of lading", "pos": "phrase", "ipa": "/bɪl əv ˈleɪdɪŋ/", "vi": "vận đơn đường biển bốc hàng", "cefr": "b2", "tier": "specialized"},
    {"id": "lex.en.200k.051631", "hw": "blab out", "pos": "verb", "ipa": "/blæb aʊt/", "vi": "buột miệng tiết lộ bí mật", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051632", "hw": "brachial artery", "pos": "phrase", "ipa": "/ˈbreɪkiəl ˈɑːrtəri/", "vi": "động mạch cánh tay giải phẫu", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051633", "hw": "brachial vein", "pos": "phrase", "ipa": "/ˈbreɪkiəl veɪn/", "vi": "tĩnh mạch cánh tay dẫn máu", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051634", "hw": "canis dingo", "pos": "phrase", "ipa": "/ˈkeɪnɪs ˈdɪŋɡoʊ/", "vi": "chó hoang dingo ở nước Úc", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051635", "hw": "cecil blount demille", "pos": "phrase", "ipa": "/ˈsɛsəl blaʊnt dəˈmɪl/", "vi": "đạo diễn Cecil B. DeMille điện ảnh", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051636", "hw": "charlotte russe", "pos": "phrase", "ipa": "/ˈʃɑːrlət ruːs/", "vi": "bánh tráng miệng Charlotte Russe", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051637", "hw": "circassian walnut", "pos": "phrase", "ipa": "/sərˈkæʃən ˈwɔːlnʌt/", "vi": "gỗ cây óc chó Circassia", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051638", "hw": "clustered poppy mallow", "pos": "phrase", "ipa": "/ˈklʌstərd ˈpɑːpi ˈmæloʊ/", "vi": "cây hoa cẩm quỳ chùm đỏ tía", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051639", "hw": "crepe gardenia", "pos": "phrase", "ipa": "/kreɪp ɡɑːrˈdiːniə/", "vi": "cây hoa lài tây; cây dành dành", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051640", "hw": "demerara sugar", "pos": "phrase", "ipa": "/ˌdɛməˈrɛərə ˈʃʊɡər/", "vi": "đường mía nâu hạt to Demerara", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051641", "hw": "desert sand verbena", "pos": "phrase", "ipa": "/ˈdɛzərt sænd vərˈbiːnə/", "vi": "cây hoa cát sa mạc màu hồng tím", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051642", "hw": "dmitri shostakovich", "pos": "phrase", "ipa": "/d(ə)ˈmiːtri ˌʃɑːstəˈkoʊvɪtʃ/", "vi": "nhạc sĩ Dmitri Shostakovich Liên Xô", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051643", "hw": "dungeness crab", "pos": "phrase", "ipa": "/ˈdʌndʒənɛs kræb/", "vi": "loài cua Dungeness bờ tây Mỹ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051644", "hw": "eamon de valera", "pos": "phrase", "ipa": "/ˈeɪmən də vàˈlɛərə/", "vi": "tổng thống Éamon de Valera Ireland", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051645", "hw": "ecclesiastical benefice", "pos": "phrase", "ipa": "/ɪˌkliːziˈæstɪkəl ˈbɛnəfɪs/", "vi": "bổng lộc chức vụ trong giáo hội", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051646", "hw": "electroshock therapy", "pos": "phrase", "ipa": "/ɪˌlɛktroʊˈʃɑːk ˈθɛrəpi/", "vi": "liệu pháp sốc điện tâm thần ECT", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051647", "hw": "erich mendelsohn", "pos": "phrase", "ipa": "/ˈɛrɪk ˈmɛndəlsən/", "vi": "kiến trúc sư Erich Mendelsohn", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051648", "hw": "false sago", "pos": "phrase", "ipa": "/fɔːls ˈseɪɡoʊ/", "vi": "cây tuế giả chi sago bột", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051649", "hw": "fava bean", "pos": "phrase", "ipa": "/ˈfɑːvə biːn/", "vi": "hạt đậu tằm dinh dưỡng fava", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051650", "hw": "ferric oxide", "pos": "phrase", "ipa": "/ˈfɛrɪk ˈɑːksaɪd/", "vi": "oxit sắt III hóa chất màu đỏ", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051651", "hw": "fragrant sumac", "pos": "phrase", "ipa": "/ˈfreɪɡrənt ˈsuːmæk/", "vi": "cây thù du thơm Bắc Mỹ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051652", "hw": "frisian islands", "pos": "phrase", "ipa": "/ˈfriːʒən ˈaɪləndz/", "vi": "quần đảo Frisia bờ biển Bắc", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051653", "hw": "galilean telescope", "pos": "phrase", "ipa": "/ˌɡælɪˈliːən ˈtɛləskoʊp/", "vi": "kính thiên văn khúc xạ Galileo", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051654", "hw": "gautama buddha", "pos": "phrase", "ipa": "/ˌɡaʊtəmə ˈbʊdə/", "vi": "Đức Phật Thích Ca Mâu Ni", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051655", "hw": "genus fusarium", "pos": "phrase", "ipa": "/ˈdʒiːnəs fjuːˈzɛəriəm/", "vi": "chi nấm mốc gây bệnh Fusarium", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051656", "hw": "groundnut oil", "pos": "phrase", "ipa": "/ˈɡraʊndnʌt ɔɪl/", "vi": "dầu phụng; dầu ép hạt lạc thơm", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051657", "hw": "gunny sack", "pos": "phrase", "ipa": "/ˈɡʌni sæk/", "vi": "bao tải gai sợi đay; bao bố thô", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051658", "hw": "hoary golden bush", "pos": "phrase", "ipa": "/ˈhɔːri ˈɡoʊldən bʊʃ/", "vi": "cây bụi hoa vàng phủ lông trắng", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051659", "hw": "in extremis", "pos": "adv", "ipa": "/ˌɪn ɪkˈstriːmɪs/", "vi": "trong cơn nguy kịch; lúc hấp hối", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051660", "hw": "indian tapir", "pos": "phrase", "ipa": "/ˈɪndiən ˈteɪpər/", "vi": "loài heo vòi Mã Lai sọc trắng", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051661", "hw": "intermediate wheatgrass", "pos": "phrase", "ipa": "/ˌɪntərˈmiːdiət ˈwiːtɡræs/", "vi": "cỏ lúa mì thảo nguyên trung gian", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051662", "hw": "john barrington wain", "pos": "phrase", "ipa": "/dʒɑːn ˈbærɪŋtən weɪn/", "vi": "nhà văn nhà thơ John Wain nước Anh", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051663", "hw": "josef albers", "pos": "phrase", "ipa": "/ˈdʒoʊzəf ˈælbərz/", "vi": "họa sĩ màu sắc Josef Albers", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051664", "hw": "kaw river", "pos": "phrase", "ipa": "/kɔː ˈrɪvər/", "vi": "dòng sông Kansas Kaw ở Mỹ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051665", "hw": "largemouth bass", "pos": "phrase", "ipa": "/ˈlɑːrdʒmaʊθ bæs/", "vi": "cá vược đen miệng rộng nước ngọt", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051666", "hw": "largemouth black bass", "pos": "phrase", "ipa": "/ˈlɑːrdʒmaʊθ blæk bæs/", "vi": "loài cá vược đen mõm rộng", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051667", "hw": "lee buck trevino", "pos": "phrase", "ipa": "/liː bʌk trəˈviːnoʊ/", "vi": "tay golf Lee Buck Trevino nước Mỹ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051668", "hw": "legless lizard", "pos": "phrase", "ipa": "/ˈlɛɡləs ˈlɪzərd/", "vi": "loài thằn lằn không chân bò sát", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051669", "hw": "lymphocytic leukemia", "pos": "phrase", "ipa": "/ˌlɪmfəˈsɪtɪk luːˈkiːmiə/", "vi": "bệnh bạch cầu dòng tế bào lympho", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051670", "hw": "mare nostrum", "pos": "phrase", "ipa": "/ˈmɑːreɪ ˈnɑːstrəm/", "vi": "biển của chúng ta; Địa Trung Hải", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051671", "hw": "michaelmas day", "pos": "phrase", "ipa": "/ˈmɪkəlməs deɪ/", "vi": "ngày lễ Thánh Thiên thần Michael", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051672", "hw": "mycenaean culture", "pos": "phrase", "ipa": "/ˌmaɪsəˈniːən ˈkʌltʃər/", "vi": "nền văn minh Mycenae Hy Lạp cổ đại", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051673", "hw": "new world tapir", "pos": "phrase", "ipa": "/nuː wɜːrld ˈteɪpər/", "vi": "loài động vật heo vòi châu Mỹ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051674", "hw": "northern bog lemming", "pos": "phrase", "ipa": "/ˈnɔːrðərn bɑːɡ ˈlɛmɪŋ/", "vi": "chuột lemming đầm lầy phương bắc", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051675", "hw": "old frisian", "pos": "phrase", "ipa": "/oʊld ˈfriːʒən/", "vi": "tiếng Frisia cổ xưa vùng bờ biển", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051676", "hw": "oswald spengler", "pos": "phrase", "ipa": "/ˈɑːzwɔːld ˈspɛŋɡlər/", "vi": "triết gia Oswald Spengler người Đức", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051677", "hw": "overstuffed chair", "pos": "phrase", "ipa": "/ˌoʊvərˈstʌft tʃɛər/", "vi": "ghế bành nhồi bông nệm dày êm ái", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051678", "hw": "parathyroid gland", "pos": "phrase", "ipa": "/ˌpærəˈθaɪrɔɪd ɡlænd/", "vi": "tuyến nội tiết cận giáp nhỏ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051679", "hw": "penny pincher", "pos": "phrase", "ipa": "/ˈpɛni ˈpɪntʃər/", "vi": "kẻ keo kiệt bủn xỉn từng xu", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051680", "hw": "peter behrens", "pos": "phrase", "ipa": "/ˈpeɪtər ˈbɛərəns/", "vi": "kiến trúc sư Peter Behrens Đức", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051681", "hw": "pink sand verbena", "pos": "phrase", "ipa": "/pɪŋk sænd vərˈbiːnə/", "vi": "cây hoa cát hồng Abronia bò", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051682", "hw": "pinwheel flower", "pos": "phrase", "ipa": "/ˈpɪnwiːl ˈflaʊər/", "vi": "hoa lài tây; hoa chong chóng", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051683", "hw": "pinwheel roll", "pos": "phrase", "ipa": "/ˈpɪnwiːl roʊl/", "vi": "bánh mì cuộn hình xoáy chong chóng", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051684", "hw": "quercus borealis", "pos": "phrase", "ipa": "/ˈkwɜːrkəs ˌbɔːriˈeɪlɪs/", "vi": "loài sồi đỏ phương bắc vỏ nứt", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051685", "hw": "rappahannock river", "pos": "phrase", "ipa": "/ˌræpəˈhænək ˈrɪvər/", "vi": "sông Rappahannock bang Virginia", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051686", "hw": "refectory table", "pos": "phrase", "ipa": "/rɪˈfɛktəri ˈteɪbəl/", "vi": "bàn ăn dài kiểu tu viện phòng ăn", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051687", "hw": "ringworm bush", "pos": "phrase", "ipa": "/ˈrɪŋwɜːrm bʊʃ/", "vi": "cây muồng trâu trị bệnh hắc lào", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051688", "hw": "russet scab", "pos": "phrase", "ipa": "/ˈrʌsɪt skæb/", "vi": "bệnh đốm ghẻ màu nâu trên khoai tây", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051689", "hw": "sago palm", "pos": "phrase", "ipa": "/ˈseɪɡoʊ pɑːm/", "vi": "cây cọ sago lấy tinh bột báng", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051690", "hw": "scrunch up", "pos": "verb", "ipa": "/skrʌntʃ ʌp/", "vi": "co rúm người lại; vò nhàu nát", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051691", "hw": "seif dune", "pos": "phrase", "ipa": "/seɪf duːn/", "vi": "cồn cát lưỡi kiếm sa mạc chạy dài", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051692", "hw": "showy milkweed", "pos": "phrase", "ipa": "/ˈʃoʊi ˈmɪlkwiːd/", "vi": "cây bông tai hoa sặc sỡ Bắc Mỹ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051693", "hw": "snowy egret", "pos": "phrase", "ipa": "/ˈsnoʊi ˈiːɡrət/", "vi": "cò tuyết trắng lông xù châu Mỹ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051694", "hw": "sockeye salmon", "pos": "phrase", "ipa": "/ˈsɑːkaɪ ˈsæmən/", "vi": "cá hồi đỏ sockeye Thái Bình Dương", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051695", "hw": "southern bog lemming", "pos": "phrase", "ipa": "/ˈsʌðərn bɑːɡ ˈlɛmɪŋ/", "vi": "chuột lemming đầm lầy phương nam", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051696", "hw": "speech intelligibility", "pos": "phrase", "ipa": "/spiːtʃ ɪnˌtɛlədʒəˈbɪləti/", "vi": "độ rõ ràng dễ hiểu của lời nói", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051697", "hw": "superior vena cava", "pos": "phrase", "ipa": "/suːˈpɪəriər ˈviːnə ˈkeɪvə/", "vi": "tĩnh mạch chủ trên đưa máu về tim", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051698", "hw": "talcum powder", "pos": "phrase", "ipa": "/ˈtælkəm ˈpaʊdər/", "vi": "phấn rôm em bé bột talc thơm", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051699", "hw": "tracheal vein", "pos": "phrase", "ipa": "/trəˈkiːəl veɪn/", "vi": "tĩnh mạch khí quản cổ họng", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051700", "hw": "tricolour television tube", "pos": "phrase", "ipa": "/ˈtraɪkʌlər ˈtɛləvɪʒən tuːb/", "vi": "ống đèn hình ti-vi ba màu điện tử", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051701", "hw": "trigeminal nerve", "pos": "phrase", "ipa": "/traɪˈdʒɛmənəl nɜːrv/", "vi": "dây thần kinh sinh ba số V sọ", "cefr": "c2", "tier": "specialized"}
]

# Validation
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
errors = []

for idx, item in enumerate(part2_data):
    # Length check
    if len(item['vi']) > 35:
        errors.append(f"Row {idx} {item['hw']} vi too long ({len(item['vi'])}): {item['vi']}")
    # Semicolon spacing
    if ';' in item['vi']:
        parts = item['vi'].split(';')
        for p in parts[1:]:
            if not p.startswith(' '):
                errors.append(f"Row {idx} {item['hw']} semicolon spacing error: {item['vi']}")
    # POS check
    if item['pos'] not in allowed_pos:
        errors.append(f"Row {idx} {item['hw']} invalid pos: {item['pos']}")
    # IPA check
    ipa = item['ipa']
    if ' ' not in item['hw']:
        if not (ipa.startswith('/') and ipa.endswith('/') and len(ipa) > 2):
            errors.append(f"Row {idx} {item['hw']} single word invalid ipa: {ipa}")
    else:
        if ipa != "" and not (ipa.startswith('/') and ipa.endswith('/')):
            errors.append(f"Row {idx} {item['hw']} phrase invalid ipa: {ipa}")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for e in errors:
        print("  -", e)
    exit(1)
else:
    # Set status and notes
    for item in part2_data:
        item['status'] = 'reviewed'
        item['notes'] = None
    
    with open('scratch/b31_r04_p2.json', 'w', encoding='utf-8') as f:
        json.dump(part2_data, f, ensure_ascii=False, indent=2)
    print("Validated and saved 100 items for Part 2")
