# -*- coding: utf-8 -*-
import json

part2_data = [
  {"id": "lex.en.200k.054602", "hw": "maxfield frederick parrish", "pos": "phrase", "ipa": "/ˈmæksfiːld ˈfrɛdərɪk ˈpærɪʃ/", "vi": "họa sĩ minh họa Maxfield Parrish", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054603", "hw": "medial rectus", "pos": "phrase", "ipa": "/ˈmiːdiəl ˈrɛktəs/", "vi": "cơ thẳng trong của nhãn cầu mắt", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054604", "hw": "medial rectus muscle", "pos": "phrase", "ipa": "/ˈmiːdiəl ˈrɛktəs ˈmʌsəl/", "vi": "cơ thẳng trong của mắt", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054605", "hw": "micrometer caliper", "pos": "phrase", "ipa": "/maɪˈkrɑːmɪtər ˈkælɪpər/", "vi": "thước panme đo độ dày chính xác", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054606", "hw": "mikhail bakunin", "pos": "phrase", "ipa": "/mɪˈkaɪl bəˈkuːnɪn/", "vi": "nhà tư tưởng vô chính phủ Bakunin", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054607", "hw": "monoamine oxidase inhibitor", "pos": "phrase", "ipa": "/ˌmɑːnoʊˈæmiːn ˈɑːksɪdeɪs ɪnˈhɪbɪtər/", "vi": "thuốc chống trầm cảm nhóm MAOI", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054608", "hw": "naproxen sodium", "pos": "phrase", "ipa": "/nəˈprɑːksən ˈsoʊdiəm/", "vi": "thuốc giảm đau hạ sốt naproxen", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054609", "hw": "oleander fern", "pos": "phrase", "ipa": "/ˌoʊliˈændər fɜːrn/", "vi": "dương xỉ lá trúc đào nhiệt đới", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054610", "hw": "pacific spiny dogfish", "pos": "phrase", "ipa": "/pəˈsɪfɪk ˈspaɪni ˈdɔːɡfɪʃ/", "vi": "cá nhám gai Thái Bình Dương", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054611", "hw": "papillary tumour", "pos": "phrase", "ipa": "/ˈpæpɪləri ˈtuːmər/", "vi": "khối u nhú; bướu dạng nhú", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054612", "hw": "parenthetical expression", "pos": "phrase", "ipa": "/ˌpærənˈθɛtɪkəl ɪkˈsprɛʃən/", "vi": "cụm từ chêm; từ trong ngoặc đơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054613", "hw": "paul vernier", "pos": "phrase", "ipa": "/pɔːl vɛərnˈjeɪ/", "vi": "nhà toán học Pierre Vernier", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054614", "hw": "pentobarbital sodium", "pos": "phrase", "ipa": "/ˌpɛntoʊˈbɑːrbɪtɑːl ˈsoʊdiəm/", "vi": "thuốc an thần pentobarbital natri", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054615", "hw": "plonk down", "pos": "phrase", "ipa": "/plɑːŋk daʊn/", "vi": "ngồi phịch xuống; đặt mạnh xuống", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054616", "hw": "quadrangular prism", "pos": "phrase", "ipa": "/kwəˈdræŋɡjələr ˈprɪzəm/", "vi": "hình lăng trụ tứ giác đáy", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054617", "hw": "rabindranath tagore", "pos": "phrase", "ipa": "/rəˈbiːndrənɑːt tæˈɡɔːr/", "vi": "đại thi hào Rabindranath Tagore", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054618", "hw": "ramesses ii", "pos": "phrase", "ipa": "/ˈræmɪsiːz ðə ˈsɛkənd/", "vi": "Pharaon vĩ đại Ramesses II Ai Cập", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054619", "hw": "ramesses the great", "pos": "phrase", "ipa": "/ˈræmɪsiːz ðə ɡreɪt/", "vi": "Ramesses Đại đế của Ai Cập cổ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054620", "hw": "ring lardner", "pos": "phrase", "ipa": "/rɪŋ ˈlɑːrdnər/", "vi": "nhà văn truyện ngắn Ring Lardner", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054621", "hw": "salafist group", "pos": "phrase", "ipa": "/ˈsæləfɪst ɡruːp/", "vi": "nhóm Hồi giáo chính thống Salafi", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054622", "hw": "shrove tuesday", "pos": "phrase", "ipa": "/ˌʃroʊv ˈtuːzdeɪ/", "vi": "thứ Ba Xưng tội trước Mùa Chay", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054623", "hw": "sir rabindranath tagore", "pos": "phrase", "ipa": "/sɜːr rəˈbiːndrənɑːt tæˈɡɔːr/", "vi": "thi hào Sir Rabindranath Tagore", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054624", "hw": "spiny dogfish", "pos": "phrase", "ipa": "/ˈspaɪni ˈdɔːɡfɪʃ/", "vi": "loài cá nhám gai có độc nhẹ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054625", "hw": "stilt plover", "pos": "phrase", "ipa": "/stɪlt ˈplʌvər/", "vi": "chim cà kheo chân dài mảnh khảnh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054626", "hw": "thermocouple junction", "pos": "phrase", "ipa": "/ˈθɜːrmoʊkʌpəl ˈdʒʌŋkʃən/", "vi": "mối nối điểm đo cặp nhiệt điện", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054627", "hw": "tibia vara", "pos": "phrase", "ipa": "/ˈtɪbiə ˈvɛərə/", "vi": "chứng cẳng chân cong vòng kiềng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054628", "hw": "tule tree", "pos": "phrase", "ipa": "/ˈtuːli triː/", "vi": "cây bách khổng lồ Tule ở Mexico", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054629", "hw": "unipolar depression", "pos": "phrase", "ipa": "/ˌjuːnɪˈpoʊlər dɪˈprɛʃən/", "vi": "rối loạn trầm cảm đơn cực nặng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054630", "hw": "vermillion flycatcher", "pos": "phrase", "ipa": "/vərˈmɪliən ˈflaɪkætʃər/", "vi": "chim đớp ruồi đỏ tươi châu Mỹ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054631", "hw": "vernier scale", "pos": "phrase", "ipa": "/ˈvɜːrniər skeɪl/", "vi": "thước phụ đo chính xác; du xích", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054632", "hw": "visceral leishmaniasis", "pos": "phrase", "ipa": "/ˈvɪsərəl ˌliːʃməˈnaɪəsɪs/", "vi": "bệnh sốt đen do ký sinh trùng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054633", "hw": "yellowtail snapper", "pos": "phrase", "ipa": "/ˈjɛloʊteɪl ˈsnæpər/", "vi": "cá hồng đuôi vàng biển nhiệt đới", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054634", "hw": "abbes", "pos": "noun", "ipa": "/æˈbeɪz/", "vi": "các viện phụ; tu viện trưởng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054635", "hw": "alkaloids", "pos": "noun", "ipa": "/ˈælkəlɔɪdz/", "vi": "các ancaloit; hợp chất ancaloit", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054636", "hw": "amides", "pos": "noun", "ipa": "/ˈæmaɪdz/", "vi": "các hợp chất amit hữu cơ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054637", "hw": "aqabas", "pos": "noun", "ipa": "/ˈɑːkəbəz/", "vi": "thành phố cảng Aqaba của Jordan", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054638", "hw": "arapahoes", "pos": "noun", "ipa": "/əˈræpəhoʊz/", "vi": "người da đỏ bộ tộc Arapaho Bắc Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054639", "hw": "bassi", "pos": "noun", "ipa": "/ˈbɑːsiː/", "vi": "những giọng nam trầm sâu lắng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054640", "hw": "bassos", "pos": "noun", "ipa": "/ˈbæsoʊz/", "vi": "các ca sĩ hát giọng nam trầm basso", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054641", "hw": "beneluxes", "pos": "noun", "ipa": "/ˈbɛnəlʌksɪz/", "vi": "khối liên minh ba nước Benelux", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054642", "hw": "bishkeks", "pos": "noun", "ipa": "/bɪʃˈkɛks/", "vi": "thủ đô Bishkek của Kyrgyzstan", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054643", "hw": "bloodlusts", "pos": "noun", "ipa": "/ˈblʌdlʌsts/", "vi": "cơn khát máu; dục vọng chém giết", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054644", "hw": "blotters", "pos": "noun", "ipa": "/ˈblɑːtərz/", "vi": "giấy thấm mực; sổ nhật ký tạm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054645", "hw": "brigids", "pos": "noun", "ipa": "/ˈbrɪdʒɪdz/", "vi": "nữ thánh Brigid bảo trợ Ireland", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054646", "hw": "broils", "pos": "noun", "ipa": "/brɔɪlz/", "vi": "cuộc cãi cọ ầm ĩ; món thịt nướng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054647", "hw": "cantatas", "pos": "noun", "ipa": "/kənˈtɑːtəz/", "vi": "các bản hợp xướng tôn giáo cantata", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054648", "hw": "cers", "pos": "noun", "ipa": "/siː-iː-ɑːrz/", "vi": "phản ứng cảm xúc có điều kiện CER", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054649", "hw": "charons", "pos": "noun", "ipa": "/ˈkɛərənz/", "vi": "người lái đò Charon dưới âm phủ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054650", "hw": "claroes", "pos": "noun", "ipa": "/ˈklɑːroʊz/", "vi": "các điếu xì gà có lá bọc màu nhạt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054651", "hw": "cocksuckers", "pos": "noun", "ipa": "/ˈkɑːksʌkərz/", "vi": "những kẻ đáng ghét; đồ khốn nạn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054652", "hw": "colonialists", "pos": "noun", "ipa": "/kəˈloʊniəlɪsts/", "vi": "những kẻ theo chủ nghĩa thực dân", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054653", "hw": "colters", "pos": "noun", "ipa": "/ˈkoʊltərz/", "vi": "lưỡi dao cắt của khung lưỡi cày", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054654", "hw": "combusted", "pos": "verb", "ipa": "/kəmˈbʌstɪd/", "vi": "đã bốc cháy; đã thiêu đốt dữ dội", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054655", "hw": "combusting", "pos": "verb", "ipa": "/kəmˈbʌstɪŋ/", "vi": "đang bốc cháy; đang phát hỏa cháy", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054656", "hw": "combusts", "pos": "verb", "ipa": "/kəmˈbʌsts/", "vi": "bốc cháy; phát hỏa; thiêu cháy", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054657", "hw": "demigods", "pos": "noun", "ipa": "/ˈdɛmiɡɑːdz/", "vi": "các bán thần; những vị á thần", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054658", "hw": "drays", "pos": "noun", "ipa": "/dreɪz/", "vi": "xe thồ chở hàng nặng không thành", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054659", "hw": "duomos", "pos": "noun", "ipa": "/ˈdwoʊmoʊz/", "vi": "các nhà thờ chính tòa lớn ở Ý", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054660", "hw": "epicentres", "pos": "noun", "ipa": "/ˈɛpɪsɛntərz/", "vi": "các tâm chấn động đất trên mặt đất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054661", "hw": "fops", "pos": "noun", "ipa": "/fɑːps/", "vi": "những kẻ ăn diện kệch cỡm đua đòi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054662", "hw": "galicians", "pos": "noun", "ipa": "/ɡəˈlɪʃənz/", "vi": "người dân vùng Galicia Tây Ban Nha", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054663", "hw": "gehrigs", "pos": "noun", "ipa": "/ˈɡɛrɪɡz/", "vi": "huyền thoại bóng chày Lou Gehrig", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054664", "hw": "gerbils", "pos": "noun", "ipa": "/ˈdʒɜːrbɪlz/", "vi": "những con chuột cát nhảy sa mạc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054665", "hw": "headcounts", "pos": "noun", "ipa": "/ˈhɛdkaʊnts/", "vi": "việc đếm đầu người; tổng nhân sự", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054666", "hw": "heartthrobs", "pos": "noun", "ipa": "/ˈhɑːrtθrɑːbz/", "vi": "thần tượng làm say đắm lòng người", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054667", "hw": "helveticas", "pos": "noun", "ipa": "/hɛlˈvɛtɪkəz/", "vi": "phông chữ không chân Helvetica", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054668", "hw": "holdouts", "pos": "noun", "ipa": "/ˈhoʊldaʊts/", "vi": "những người kiên quyết chống cự", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054669", "hw": "honorees", "pos": "noun", "ipa": "/ˌɑːnəˈriːz/", "vi": "những người được trao tặng vinh dự", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054670", "hw": "idylls", "pos": "noun", "ipa": "/ˈaɪdɪlz/", "vi": "bài thơ thôn dã; cảnh điền viên", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054671", "hw": "ikons", "pos": "noun", "ipa": "/ˈaɪkɑːnz/", "vi": "các bức tranh thánh; biểu tượng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054672", "hw": "illusionists", "pos": "noun", "ipa": "/ɪˈluːʒənɪsts/", "vi": "những nhà ảo thuật điêu luyện", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054673", "hw": "impellers", "pos": "noun", "ipa": "/ɪmˈpɛlərz/", "vi": "các cánh quạt đẩy; bánh công tác", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054674", "hw": "jibed", "pos": "verb", "ipa": "/dʒaɪbd/", "vi": "đã phù hợp; đã ăn khớp khớp với", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054675", "hw": "jibes", "pos": "noun", "ipa": "/dʒaɪbz/", "vi": "những lời chế giễu; sự châm chọc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054676", "hw": "jibing", "pos": "verb", "ipa": "/ˈdʒaɪbɪŋ/", "vi": "đang ăn khớp; đang châm chọc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054677", "hw": "joules", "pos": "noun", "ipa": "/dʒuːlz/", "vi": "đơn vị năng lượng jun trong vật lý", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054678", "hw": "kalashnikovs", "pos": "noun", "ipa": "/kəˈlæʃnɪkɑːvz/", "vi": "các khẩu súng trường tiểu liên AK", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054679", "hw": "leavers", "pos": "noun", "ipa": "/ˈliːvərz/", "vi": "học sinh tốt nghiệp; người rời đi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054680", "hw": "lecterns", "pos": "noun", "ipa": "/ˈlɛktərnz/", "vi": "những bục phát biểu thuyết trình", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054681", "hw": "loaches", "pos": "noun", "ipa": "/ˈloʊtʃɪz/", "vi": "loài cá chạch bùn nước ngọt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054682", "hw": "macrophages", "pos": "noun", "ipa": "/ˈmækrəfeɪdʒɪz/", "vi": "các đại thực bào miễn dịch cơ thể", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054683", "hw": "mahayanas", "pos": "noun", "ipa": "/ˌmɑːhəˈjɑːnəz/", "vi": "các nhánh Phật giáo Đại thừa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054684", "hw": "marionettes", "pos": "noun", "ipa": "/ˌmæriəˈnɛts/", "vi": "những con rối dây trên sân khấu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054685", "hw": "masochists", "pos": "noun", "ipa": "/ˈmæsəkɪsts/", "vi": "những người mang tính khổ dâm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054686", "hw": "mitterrands", "pos": "noun", "ipa": "/ˌmiːtɛˈrɑ̃ːdz/", "vi": "Tổng thống Pháp François Mitterrand", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054687", "hw": "nerudas", "pos": "noun", "ipa": "/nɛˈruːdəz/", "vi": "nhà thơ Nobel Chile Pablo Neruda", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054688", "hw": "orlies", "pos": "noun", "ipa": "/ˈɔːrliz/", "vi": "sân bay quốc tế Orly tại Paris", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054689", "hw": "paediatricses", "pos": "noun", "ipa": "/ˌpiːdiˈætrɪksɪz/", "vi": "khoa nhi; các ngành nhi khoa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054690", "hw": "pallier", "pos": "adj", "ipa": "/ˈpæliər/", "vi": "thân thiết hơn; gần gũi như bạn bè", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054691", "hw": "palliest", "pos": "adj", "ipa": "/ˈpæliɪst/", "vi": "thân thiết nhất; gắn bó nhất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054692", "hw": "pendragons", "pos": "noun", "ipa": "/pɛnˈdræɡənz/", "vi": "thủ lĩnh tối cao của người Briton", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054693", "hw": "phonemes", "pos": "noun", "ipa": "/ˈfoʊniːmz/", "vi": "các âm vị tối thiểu trong ngôn ngữ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054694", "hw": "plebeians", "pos": "noun", "ipa": "/plɪˈbiːənz/", "vi": "những thường dân thời La Mã cổ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054695", "hw": "precessions", "pos": "noun", "ipa": "/prɪˈsɛʃənz/", "vi": "hiện tượng tiến động của trục quay", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054696", "hw": "preempted", "pos": "verb", "ipa": "/priːˈɛmptɪd/", "vi": "đã đón đầu; đã giành quyền trước", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054697", "hw": "preempting", "pos": "verb", "ipa": "/priːˈɛmptɪŋ/", "vi": "đang đón đầu; đang ngăn chặn sớm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054698", "hw": "preempts", "pos": "noun", "ipa": "/priːˈɛmpts/", "vi": "chiến thuật đón đầu; giá thầu chặn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054699", "hw": "racquetballs", "pos": "noun", "ipa": "/ˈrækɪtbɔːlz/", "vi": "môn bóng quần trong nhà dùng vợt", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054700", "hw": "regrowing", "pos": "verb", "ipa": "/riːˈɡroʊɪŋ/", "vi": "đang tái sinh; đang mọc lại mầm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054701", "hw": "regrows", "pos": "verb", "ipa": "/riːˈɡroʊz/", "vi": "mọc lại mầm; tái sinh tế bào", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Validation
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

assert len(part2_data) == 100, f"Length is {len(part2_data)}"

with open('scratch/b31_r10_raw_p2.json') as f:
    raw = json.load(f)

for i, (item, raw_item) in enumerate(zip(part2_data, raw)):
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

with open('scratch/b31_r10_p2.json', 'w', encoding='utf-8') as f:
    json.dump(part2_data, f, ensure_ascii=False, indent=2)

print("Validated and saved 100 items for Part 2")
