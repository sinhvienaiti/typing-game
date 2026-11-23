# -*- coding: utf-8 -*-
import json

part4_data = [
    {"id": "lex.en.200k.051802", "hw": "sunnahs", "pos": "noun", "ipa": "/ˈsʊnəz/", "vi": "các truyền thống Sunnah Hồi giáo", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051803", "hw": "surfactants", "pos": "noun", "ipa": "/sərˈfæktənts/", "vi": "các chất hoạt động bề mặt tẩy rửa", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051804", "hw": "tarns", "pos": "noun", "ipa": "/tɑːrnz/", "vi": "các hồ nước băng hà trên núi cao", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051805", "hw": "taters", "pos": "noun", "ipa": "/ˈteɪtərz/", "vi": "củ khoai tây; quả bóng đập xa", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051806", "hw": "taxicabs", "pos": "noun", "ipa": "/ˈtæksikæbz/", "vi": "các chiếc xe tắc xi chở khách", "cefr": "a2", "tier": "general"},
    {"id": "lex.en.200k.051807", "hw": "tellurides", "pos": "noun", "ipa": "/ˈtɛljʊraɪdz/", "vi": "các hợp chất khoáng telu telurit", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051808", "hw": "thules", "pos": "noun", "ipa": "/ˈθuːliz/", "vi": "vùng cực bắc Thule thần thoại", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051809", "hw": "thunks", "pos": "noun", "ipa": "/θʌŋks/", "vi": "tiếng kêu bịch nặng nề", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051810", "hw": "tibers", "pos": "noun", "ipa": "/ˈtaɪbərz/", "vi": "dòng sông Tevere Tiber ở Roma Ý", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051811", "hw": "trevelyans", "pos": "noun", "ipa": "/trɪˈvɛljənz/", "vi": "sử gia George Macaulay Trevelyan", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051812", "hw": "tupelos", "pos": "noun", "ipa": "/ˈtuːpəloʊz/", "vi": "chi cây hoa tupelo vùng đầm lầy", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051813", "hw": "villainies", "pos": "noun", "ipa": "/ˈvɪləniz/", "vi": "hành vi đê tiện độc ác; tội ác", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051814", "hw": "viziers", "pos": "noun", "ipa": "/vɪˈzɪərz/", "vi": "các tể tướng đại thần Hồi giáo", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051815", "hw": "whimsier", "pos": "adj", "ipa": "/ˈwɪmziər/", "vi": "kỳ quái hơn; kỳ lạ hão huyền hơn", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051816", "hw": "whimsies", "pos": "noun", "ipa": "/ˈwɪmziz/", "vi": "ý tưởng kỳ quặc; tính thất thường", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051817", "hw": "whimsiest", "pos": "adj", "ipa": "/ˈwɪmziɪst/", "vi": "kỳ quái nhất; hão huyền nhất", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051818", "hw": "wiccas", "pos": "noun", "ipa": "/ˈwɪkəz/", "vi": "phù thủy tà thuật tôn giáo Wicca", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051819", "hw": "workpieces", "pos": "noun", "ipa": "/ˈwɜːrkpiːsɪz/", "vi": "các chi tiết gia công; phôi thô", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051820", "hw": "yucatans", "pos": "noun", "ipa": "/ˌjuːkəˈtænz/", "vi": "bán đảo Yucatán ở Mexico", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051821", "hw": "zircons", "pos": "noun", "ipa": "/ˈzɜːrkɑːnz/", "vi": "các tinh thể đá quý zircon silicat", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051822", "hw": "acute lymphocytic leukemia", "pos": "phrase", "ipa": "/əˈkjuːt ˌlɪmfəˈsɪtɪk luːˈkiːmiə/", "vi": "bệnh bạch cầu cấp dòng lympho", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051823", "hw": "aniline oil", "pos": "phrase", "ipa": "/ˈænəlɪn ɔɪl/", "vi": "dầu anilin dùng làm phẩm nhuộm", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051824", "hw": "atopic eczema", "pos": "phrase", "ipa": "/eɪˈtɑːpɪk ˈɛɡzəmə/", "vi": "bệnh chàm thể tạng; viêm da cơ địa", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051825", "hw": "bass viol", "pos": "phrase", "ipa": "/beɪs ˈvaɪəl/", "vi": "đàn vi-ô-lông trầm cổ điển viola", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051826", "hw": "battle of maldon", "pos": "phrase", "ipa": "/ˈbætəl əv ˈmɔːldən/", "vi": "trận chiến Maldon cổ nước Anh", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051827", "hw": "bay of biscay", "pos": "phrase", "ipa": "/beɪ əv ˈbɪskeɪ/", "vi": "vịnh Biscay Đại Tây Dương", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051828", "hw": "bicameral script", "pos": "phrase", "ipa": "/baɪˈkæmərəl skrɪpt/", "vi": "hệ chữ viết có hoa và thường", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051829", "hw": "black maire", "pos": "phrase", "ipa": "/blæk ˈmaɪreɪ/", "vi": "cây gỗ đen maire ở New Zealand", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051830", "hw": "bound morpheme", "pos": "phrase", "ipa": "/baʊnd ˈmɔːrfiːm/", "vi": "hình vị ràng buộc ngữ pháp", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051831", "hw": "buccal artery", "pos": "phrase", "ipa": "/ˈbʌkəl ˈɑːrtəri/", "vi": "động mạch má giải phẫu mặt", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051832", "hw": "buccal cavity", "pos": "phrase", "ipa": "/ˈbʌkəl ˈkævəti/", "vi": "khoang miệng; xoang má miệng", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051833", "hw": "caffe latte", "pos": "phrase", "ipa": "/ˌkæfeɪ ˈlɑːteɪ/", "vi": "cà phê sữa kiểu Ý latte", "cefr": "a2", "tier": "general"},
    {"id": "lex.en.200k.051834", "hw": "cassia tora", "pos": "phrase", "ipa": "/ˈkæsiə ˈtɔːrə/", "vi": "cây thảo quyết minh muồng ngủ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051835", "hw": "cheval glass", "pos": "phrase", "ipa": "/ʃəˈvæl ɡlæs/", "vi": "gương soi toàn thân có chân đứng", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051836", "hw": "chloe anthony wofford", "pos": "phrase", "ipa": "/ˈkloʊi ˈænθəni ˈwʊfərd/", "vi": "nhà văn Toni Morrison Nobel", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051837", "hw": "chop suey", "pos": "phrase", "ipa": "/ˌtʃɑːp ˈsuːi/", "vi": "món rau củ xào thịt thập cẩm", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051838", "hw": "chronic lymphocytic leukemia", "pos": "phrase", "ipa": "/ˈkrɑːnɪk ˌlɪmfəˈsɪtɪk luːˈkiːmiə/", "vi": "bạch cầu dòng lympho mạn tính CLL", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051839", "hw": "coattails effect", "pos": "phrase", "ipa": "/ˈkoʊtteɪlz ɪˈfɛkt/", "vi": "hiệu ứng vạt áo chính trị", "cefr": "c2", "tier": "general"},
    {"id": "lex.en.200k.051840", "hw": "connemara heath", "pos": "phrase", "ipa": "/ˌkɑːnəˈmɑːrə hiːθ/", "vi": "cây thạch nam Connemara Ireland", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051841", "hw": "contra danse", "pos": "phrase", "ipa": "/ˈkɑːntrə dæns/", "vi": "điệu nhảy dân vũ đối hàng contra", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051842", "hw": "coriolis effect", "pos": "phrase", "ipa": "/ˌkɔːriˈoʊlɪs ɪˈfɛkt/", "vi": "hiệu ứng xoay Coriolis Trái Đất", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051843", "hw": "coriolis force", "pos": "phrase", "ipa": "/ˌkɔːriˈoʊlɪs fɔːrs/", "vi": "lực quán tính Coriolis Trái Đất", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051844", "hw": "cristobal balenciaga", "pos": "phrase", "ipa": "/krɪsˈtoʊbəl bəˌlɛnsiˈɑːɡə/", "vi": "nhà thiết kế Cristóbal Balenciaga", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051845", "hw": "curvilinear correlation", "pos": "phrase", "ipa": "/ˌkɜːrvəˈlɪniər ˌkɔːrəˈleɪʃən/", "vi": "tương quan đường cong thống kê", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051846", "hw": "drosophila melanogaster", "pos": "phrase", "ipa": "/droʊˈsɑːfɪlə məˌlænoʊˈɡæstər/", "vi": "loài ruồi giấm thường thí nghiệm", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051847", "hw": "equine distemper", "pos": "phrase", "ipa": "/ˈiːkwaɪn dɪsˈtɛmpər/", "vi": "bệnh viêm hạch truyền nhiễm ở ngựa", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051848", "hw": "european curlew", "pos": "phrase", "ipa": "/ˌjʊrəˈpiːən ˈkɜːrljuː/", "vi": "chim choắt mỏ cong lớn châu Âu", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051849", "hw": "fernand leger", "pos": "phrase", "ipa": "/fɛrˈnɑːn leɪˈʒeɪ/", "vi": "họa sĩ lập thể Fernand Léger", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051850", "hw": "fertilized ovum", "pos": "phrase", "ipa": "/ˈfɜːrtəlaɪzd ˈoʊvəm/", "vi": "trứng đã thụ tinh; hợp tử", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051851", "hw": "free morpheme", "pos": "phrase", "ipa": "/friː ˈmɔːrfiːm/", "vi": "hình vị tự do trong ngôn ngữ học", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051852", "hw": "genus prunus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈpruːnəs/", "vi": "chi mận mơ đào Prunus", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051853", "hw": "genus regulus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈrɛɡjələs/", "vi": "chi chim tước mào vàng Regulus", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051854", "hw": "genus vanda", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈvændə/", "vi": "chi hoa phong lan Vanda rực rỡ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051855", "hw": "genus verbena", "pos": "phrase", "ipa": "/ˈdʒiːnəs vərˈbiːnə/", "vi": "chi thực vật cỏ roi ngựa Verbena", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051856", "hw": "giant anteater", "pos": "phrase", "ipa": "/ˈdʒaɪənt ˈæntiːtər/", "vi": "thú ăn kiến khổng lồ Nam Mỹ", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051857", "hw": "great anteater", "pos": "phrase", "ipa": "/ɡreɪt ˈæntiːtər/", "vi": "loài thú ăn kiến khổng lồ", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051858", "hw": "hoary alison", "pos": "phrase", "ipa": "/ˈhɔːri ˈælɪsən/", "vi": "cây hoa cải hoa trắng phủ lông", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051859", "hw": "inferior vena cava", "pos": "phrase", "ipa": "/ɪnˈfɪəriər ˈviːnə ˈkeɪvə/", "vi": "tĩnh mạch chủ dưới dẫn máu", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051860", "hw": "john hoyer updike", "pos": "phrase", "ipa": "/dʒɑːn ˈhɔɪər ˈʌpdaɪk/", "vi": "nhà văn John Updike người Mỹ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051861", "hw": "john huss", "pos": "phrase", "ipa": "/dʒɑːn hʊs/", "vi": "nhà cải cách tôn giáo Jan Hus", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051862", "hw": "karl von frisch", "pos": "phrase", "ipa": "/kɑːrl fɔn frɪʃ/", "vi": "nhà tập tính học Karl von Frisch", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051863", "hw": "laurentian highlands", "pos": "phrase", "ipa": "/lɔːˈrɛnʃən ˈhaɪləndz/", "vi": "vùng cao nguyên Laurentian Canada", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051864", "hw": "laurentian plateau", "pos": "phrase", "ipa": "/lɔːˈrɛnʃən plæˈtoʊ/", "vi": "khiên đá Laurentian ở Canada", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051865", "hw": "lip synchronisation", "pos": "phrase", "ipa": "/lɪp ˌsɪŋkrənəˈzeɪʃən/", "vi": "sự khớp khẩu hình; hát nhép", "cefr": "b2", "tier": "general"},
    {"id": "lex.en.200k.051866", "hw": "mauritanian monetary unit", "pos": "phrase", "ipa": "/ˌmɔːrɪˈteɪniən ˈmʌnɪtɛri ˈjuːnɪt/", "vi": "tiền tệ ouguiya của Mauritania", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051867", "hw": "michaelmas daisy", "pos": "phrase", "ipa": "/ˈmɪkəlməs ˈdeɪzi/", "vi": "hoa cúc sao Michaelmas nở thu", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051868", "hw": "mollusk family", "pos": "phrase", "ipa": "/ˈmɑːləsk ˌfæməli/", "vi": "họ ngành thân mềm nhuyễn thể", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051869", "hw": "mycenaean civilization", "pos": "phrase", "ipa": "/ˌmaɪsəˈniːən ˌsɪvəlɪˈzeɪʃən/", "vi": "nền văn minh Mycenae Hy Lạp cổ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051870", "hw": "new world anteater", "pos": "phrase", "ipa": "/nuː wɜːrld ˈæntiːtər/", "vi": "thú ăn kiến châu Mỹ nhiệt đới", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051871", "hw": "on the coattails", "pos": "phrase", "ipa": "/ɑːn ðə ˈkoʊtteɪlz/", "vi": "dựa hơi thơm lây; theo đuôi ăn theo", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051872", "hw": "painted terrapin", "pos": "phrase", "ipa": "/ˈpeɪntɪd ˈtɛrəpɪn/ ", "vi": "loài rùa nước ngọt đốm màu sặc sỡ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051873", "hw": "parasympathetic nervous system", "pos": "phrase", "ipa": "/ˌpærəˌsɪmpəˈθɛtɪk ˈnɜːrvəs ˈsɪstəm/", "vi": "hệ thần kinh đối giao cảm cơ thể", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051874", "hw": "pearl sago", "pos": "phrase", "ipa": "/pɜːrl ˈseɪɡoʊ/", "vi": "hạt trân châu bột báng sago", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051875", "hw": "photoelectric emission", "pos": "phrase", "ipa": "/ˌfoʊtoʊɪˈlɛktrɪk ɪˈmɪʃən/", "vi": "sự phát xạ electron quang điện", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051876", "hw": "pinwheel wind collector", "pos": "phrase", "ipa": "/ˈpɪnwiːl wɪnd kəˈlɛktər/", "vi": "chong chóng gió đo tốc độ gió", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051877", "hw": "port orford cedar", "pos": "phrase", "ipa": "/pɔːrt ˈɔːrfərd ˈsiːdər/", "vi": "gỗ trắc bách diệp Port Orford", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051878", "hw": "precocious dentition", "pos": "phrase", "ipa": "/prɪˈkoʊʃəs dɛnˈtɪʃən/", "vi": "hiện tượng mọc răng sớm ở trẻ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051879", "hw": "proteolytic enzyme", "pos": "phrase", "ipa": "/ˌproʊtiəˈlɪtɪk ˈɛnzaɪm/", "vi": "men protease phân giải protein", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051880", "hw": "sand stargazer", "pos": "phrase", "ipa": "/sænd ˈstɑːrɡeɪzər/", "vi": "cá sao ngắm cát vùi mình đáy biển", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051881", "hw": "sea lamprey", "pos": "phrase", "ipa": "/siː ˈlæmpri/", "vi": "loài cá mút đá biển ký sinh", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051882", "hw": "seashore mallow", "pos": "phrase", "ipa": "/ˈsiːʃɔːr ˈmæloʊ/", "vi": "cây hoa cẩm quỳ ven bờ biển", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051883", "hw": "serous membrane", "pos": "phrase", "ipa": "/ˈsɪərəs ˈmɛmbreɪn/", "vi": "màng thanh dịch cơ thể bọc nội tạng", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051884", "hw": "shel silverstein", "pos": "phrase", "ipa": "/ʃɛl ˈsɪlvərstiːn/", "vi": "nhà thơ họa sĩ Shel Silverstein", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051885", "hw": "slender wheatgrass", "pos": "phrase", "ipa": "/ˈslɛndər ˈwiːtɡræs/", "vi": "cây cỏ lúa mì thân mảnh đồng cỏ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051886", "hw": "spina bifida", "pos": "phrase", "ipa": "/ˈspaɪnə ˈbɪfɪdə/", "vi": "dị tật bẩm sinh nứt đốt sống gai", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051887", "hw": "steffi graf", "pos": "phrase", "ipa": "/ˈstɛfi ɡræf/", "vi": "huyền thoại quần vợt Steffi Graf", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051888", "hw": "stephen vincent benet", "pos": "phrase", "ipa": "/ˈstiːvən ˈvɪnsənt bɛˈneɪ/", "vi": "nhà văn Stephen Vincent Benét Mỹ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051889", "hw": "stone curlew", "pos": "phrase", "ipa": "/stoʊn ˈkɜːrljuː/", "vi": "loài chim dẽ cùi mắt lồi vạc đất", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051890", "hw": "truncation error", "pos": "phrase", "ipa": "/trʌŋˈkeɪʃən ˈɛrər/", "vi": "sai số do cắt cụt số học toán", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051891", "hw": "victimless crime", "pos": "phrase", "ipa": "/ˈvɪktəmləs kraɪm/", "vi": "tội phạm không có nạn nhân cụ thể", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051892", "hw": "white maire", "pos": "phrase", "ipa": "/waɪt ˈmaɪreɪ/", "vi": "cây gỗ maire trắng ở New Zealand", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051893", "hw": "advils", "pos": "noun", "ipa": "/ˈædvɪlz/", "vi": "thuốc giảm đau hạ sốt Advil", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051894", "hw": "agitators", "pos": "noun", "ipa": "/ˈædʒɪteɪtərz/", "vi": "kẻ kích động biểu tình; cánh khuấy", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051895", "hw": "albedos", "pos": "noun", "ipa": "/ælˈbiːdoʊz/", "vi": "suất phản chiếu ánh sáng bề mặt", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051896", "hw": "alcotts", "pos": "noun", "ipa": "/ˈɔːlkɑːts/", "vi": "nhà văn Louisa May Alcott nước Mỹ", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051897", "hw": "anaphylaxises", "pos": "noun", "ipa": "/ˌænəfəˈlæksɪsɪz/", "vi": "các cơn sốc phản vệ dị ứng cấp tính", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051898", "hw": "angeluses", "pos": "noun", "ipa": "/ˈændʒələsɪz/", "vi": "kinh Truyền Tin; chuông báo kinh", "cefr": "c2", "tier": "specialized"},
    {"id": "lex.en.200k.051899", "hw": "angoras", "pos": "noun", "ipa": "/æŋˈɡɔːrəz/", "vi": "thỏ lông xù Angora; len angora", "cefr": "c1", "tier": "general"},
    {"id": "lex.en.200k.051900", "hw": "applicators", "pos": "noun", "ipa": "/ˈæplɪkeɪtərz/", "vi": "dụng cụ bôi thuốc; que thoa thuốc", "cefr": "c1", "tier": "specialized"},
    {"id": "lex.en.200k.051901", "hw": "arsonists", "pos": "noun", "ipa": "/ˈɑːrsənɪsts/", "vi": "những kẻ cố ý phóng hỏa đốt nhà", "cefr": "c1", "tier": "general"}
]

# Validation
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
errors = []

for idx, item in enumerate(part4_data):
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
    ipa = item['ipa'].strip()
    item['ipa'] = ipa
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
    for item in part4_data:
        item['status'] = 'reviewed'
        item['notes'] = None
    
    with open('scratch/b31_r04_p4.json', 'w', encoding='utf-8') as f:
        json.dump(part4_data, f, ensure_ascii=False, indent=2)
    print("Validated and saved 100 items for Part 4")
