import json

# Manual QA review for Batch 20 Round 10 Part 1 (099502 to 099601)
part1_data = [
  {"id": "lex.en.100k.099502", "hw": "parleyvoo", "pos": "noun", "ipa": "/ˌpɑːrliˈvuː/", "vi": "tiếng Pháp bồi; người Pháp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099503", "hw": "parliamentarism", "pos": "noun", "ipa": "/ˌpɑːrləˈmɛntərɪzəm/", "vi": "chế độ đại nghị; phái nghị viện", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099504", "hw": "parlormaid", "pos": "noun", "ipa": "/ˈpɑːrlərˌmeɪd/", "vi": "người hầu phòng khách", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099505", "hw": "parlourmaid", "pos": "noun", "ipa": "/ˈpɑːrlərˌmeɪd/", "vi": "người hầu phòng khách", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099506", "hw": "parlously", "pos": "adv", "ipa": "/ˈpɑːrləsli/", "vi": "nguy hiểm; hiểm nghèo; bấp bênh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099507", "hw": "parly", "pos": "noun", "ipa": "/ˈpɑːrli/", "vi": "tàu hỏa vé rẻ; nghị viện", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099508", "hw": "parmassus", "pos": "noun", "ipa": "/pɑːrˈnæsəs/", "vi": "núi Parnassus; thi đàn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099509", "hw": "parmeliaceae", "pos": "noun", "ipa": "/pɑːrˌmiliˈeɪsiːˌaɪ/", "vi": "họ địa y Parmeliaceae", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099510", "hw": "parnahiba", "pos": "noun", "ipa": "/pɑːrnəˈiːbə/", "vi": "sông Parnaíba (Brazil)", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099511", "hw": "parnaiba", "pos": "noun", "ipa": "/pɑːrnəˈiːbə/", "vi": "sông Parnaíba (Brazil)", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099512", "hw": "parnassia", "pos": "noun", "ipa": "/pɑːrˈnæsiə/", "vi": "chi cỏ quạ; chi Parnassia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099513", "hw": "parnassian", "pos": "adj", "ipa": "/pɑːrˈnæsiən/", "vi": "thuộc núi Parnassus; thuộc thi phú", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099514", "hw": "parnassianism", "pos": "noun", "ipa": "/pɑːrˈnæsiənɪzəm/", "vi": "trường phái thi sơn Parnasse", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099515", "hw": "parnassism", "pos": "noun", "ipa": "/pɑːrˈnæsɪzəm/", "vi": "chủ nghĩa thi ca phái Parnasse", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099516", "hw": "paroccipital", "pos": "adj", "ipa": "/ˌpærɒkˈsɪpɪtl/", "vi": "thuộc mấu cạnh chẩm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099517", "hw": "paroccipitut", "pos": "noun", "ipa": "/ˌpærɒkˈsɪpɪtət/", "vi": "mấu cạnh chẩm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099518", "hw": "parochetus", "pos": "noun", "ipa": "/pəˈrɒkɪtəs/", "vi": "chi đậu hoa lam Parochetus", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099519", "hw": "parochialise", "pos": "verb", "ipa": "/pəˈroʊkiəlaɪz/", "vi": "giới hạn cục bộ; địa phương hóa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099520", "hw": "parochialist", "pos": "noun", "ipa": "/pəˈroʊkiəlɪst/", "vi": "người có tư tưởng cục bộ hẹp hòi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099521", "hw": "parochiality", "pos": "noun", "ipa": "/pəˌroʊkiˈæləti/", "vi": "tính cục bộ; tính hạn hẹp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099522", "hw": "parochialize", "pos": "verb", "ipa": "/pəˈroʊkiəlaɪz/", "vi": "giới hạn cục bộ; địa phương hóa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099523", "hw": "parodic", "pos": "adj", "ipa": "/pəˈrɑːdɪk/", "vi": "thuộc thể loại nhại; có tính nhại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099524", "hw": "parodical", "pos": "adj", "ipa": "/pəˈrɑːdɪkəl/", "vi": "có tính chất nhại; khôi hài", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099525", "hw": "parodied", "pos": "verb", "ipa": "/ˈpærədid/", "vi": "đã nhại lại; đã châm biếm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099526", "hw": "parodies", "pos": "noun", "ipa": "/ˈpærədiz/", "vi": "các tác phẩm nhại; các bài nhại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099527", "hw": "parodistic", "pos": "adj", "ipa": "/ˌpærəˈdɪstɪk/", "vi": "có phong cách nhại; châm biếm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099528", "hw": "parodying", "pos": "verb", "ipa": "/ˈpærədiɪŋ/", "vi": "đang nhại lại; đang châm biếm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099529", "hw": "paroecious", "pos": "adj", "ipa": "/pəˈriːʃəs/", "vi": "lưỡng tính đồng gốc (rêu)", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099530", "hw": "paroemia", "pos": "noun", "ipa": "/pəˈriːmiə/", "vi": "cách ngôn; tục ngữ; ngạn ngữ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099531", "hw": "paroicous", "pos": "adj", "ipa": "/pəˈriːkəs/", "vi": "lưỡng tính đực cái kề nhau", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099532", "hw": "parol", "pos": "noun", "ipa": "/pəˈroʊl/", "vi": "lời nói miệng; cam kết miệng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099533", "hw": "paronomasia", "pos": "noun", "ipa": "/ˌpærənəˈmeɪʒə/", "vi": "lối chơi chữ đồng âm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099534", "hw": "paronomastic", "pos": "adj", "ipa": "/ˌpærənəˈmæstɪk/", "vi": "có tính chất chơi chữ đồng âm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099535", "hw": "paronomastically", "pos": "adv", "ipa": "/ˌpærənəˈmæstɪkli/", "vi": "bằng cách chơi chữ đồng âm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099536", "hw": "paronym", "pos": "noun", "ipa": "/ˈpærənɪm/", "vi": "từ cùng gốc; từ phái sinh gần âm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099537", "hw": "paronymic", "pos": "adj", "ipa": "/ˌpærəˈnɪmɪk/", "vi": "thuộc từ phái sinh cùng gốc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099538", "hw": "parophrys", "pos": "noun", "ipa": "/pəˈrɒfrɪs/", "vi": "chi cá bơn mắt phải Parophrys", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099539", "hw": "paroquet", "pos": "noun", "ipa": "/ˈpærəkɪt/", "vi": "vẹt đuôi dài nhỏ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099540", "hw": "parorchidium", "pos": "noun", "ipa": "/ˌpærɔːrˈkɪdiəm/", "vi": "chứng tinh hoàn lạc chỗ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099541", "hw": "parosamia", "pos": "noun", "ipa": "/ˌpærɒˈseɪmiə/", "vi": "chứng rối loạn khứu giác", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099542", "hw": "parotic", "pos": "adj", "ipa": "/pəˈroʊtɪk/", "vi": "thuộc vùng gần tai", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099543", "hw": "parotitic", "pos": "adj", "ipa": "/ˌpærəˈtɪtɪk/", "vi": "thuộc chứng quai bị", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099544", "hw": "parous", "pos": "adj", "ipa": "/ˈpeɪrəs/", "vi": "đã từng sinh con", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099545", "hw": "paroxetime", "pos": "noun", "ipa": "/pəˈrɒksətiːm/", "vi": "thuốc paroxetine", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099546", "hw": "paroxysmally", "pos": "adv", "ipa": "/ˌpærəkˈsɪzməli/", "vi": "kịch phát; từng cơn dữ dội", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099547", "hw": "paroxytone", "pos": "noun", "ipa": "/pəˈrɑːksətoʊn/", "vi": "từ có trọng âm ở âm tiết áp chót", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099548", "hw": "parpen", "pos": "noun", "ipa": "/ˈpɑːrpən/", "vi": "viên đá giằng tường", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099549", "hw": "parqueted", "pos": "verb", "ipa": "/ˈpɑːrkeɪd/", "vi": "đã lát sàn gỗ hoa văn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099550", "hw": "parqueterie", "pos": "noun", "ipa": "/ˈpɑːrkətri/", "vi": "nghệ thuật ghép sàn gỗ mỹ nghệ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099551", "hw": "parqueting", "pos": "verb", "ipa": "/ˈpɑːrkeɪɪŋ/", "vi": "đang lát sàn gỗ hoa văn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099552", "hw": "parquets", "pos": "noun", "ipa": "/ˈpɑːrkeɪz/", "vi": "các sàn gỗ ghép hoa văn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099553", "hw": "parrakeet", "pos": "noun", "ipa": "/ˈpærəkiːt/", "vi": "vẹt đuôi dài nhỏ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099554", "hw": "parricidal", "pos": "adj", "ipa": "/ˌpærɪˈsaɪdl/", "vi": "thuộc tội sát hại cha mẹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099555", "hw": "parricidally", "pos": "adv", "ipa": "/ˌpærɪˈsaɪdəli/", "vi": "một cách sát hại đấng sinh thành", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099556", "hw": "parried", "pos": "verb", "ipa": "/ˈpærid/", "vi": "đã gạt đỡ; đã né tránh đòn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099557", "hw": "parries", "pos": "noun", "ipa": "/ˈpæriz/", "vi": "các thế gạt đỡ; đòn hóa giải", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099558", "hw": "parroket", "pos": "noun", "ipa": "/ˈpærəkɪt/", "vi": "vẹt đuôi dài nhỏ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099559", "hw": "parroquet", "pos": "noun", "ipa": "/ˈpærəkɪt/", "vi": "vẹt đuôi dài nhỏ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099560", "hw": "parroted", "pos": "verb", "ipa": "/ˈpærətid/", "vi": "đã lặp lại như vẹt; đã nói leo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099561", "hw": "parroter", "pos": "noun", "ipa": "/ˈpærətər/", "vi": "người nhắc lại như vẹt; kẻ nói leo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099562", "hw": "parrotia", "pos": "noun", "ipa": "/pəˈroʊʃiə/", "vi": "chi cây thiết mộc Parrotia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099563", "hw": "parroting", "pos": "verb", "ipa": "/ˈpærətɪŋ/", "vi": "đang lặp lại như vẹt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099564", "hw": "parrotiopsis", "pos": "noun", "ipa": "/ˌpærətiˈɒpsɪs/", "vi": "chi cây bụi Parrotiopsis", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099565", "hw": "parrotlike", "pos": "adj", "ipa": "/ˈpærətˌlaɪk/", "vi": "như vẹt; máy móc không hiểu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099566", "hw": "parrotry", "pos": "noun", "ipa": "/ˈpærətri/", "vi": "thói lặp lại như vẹt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099567", "hw": "parrots", "pos": "noun", "ipa": "/ˈpærəts/", "vi": "các con vẹt", "cefr": "A1", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099568", "hw": "parrquetry", "pos": "noun", "ipa": "/ˈpɑːrkətri/", "vi": "nghệ thuật ghép gỗ; sàn gỗ hoa văn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099569", "hw": "parrying", "pos": "verb", "ipa": "/ˈpæriɪŋ/", "vi": "đang gạt đỡ; đang né tránh đòn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099570", "hw": "parsecs", "pos": "noun", "ipa": "/ˈpɑːrsɛks/", "vi": "các đơn vị parsec (thiên văn)", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099571", "hw": "parsed", "pos": "verb", "ipa": "/pɑːrst/", "vi": "đã phân tích cú pháp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099572", "hw": "parseeism", "pos": "noun", "ipa": "/pɑːrˈsiːɪzəm/", "vi": "đạo Hỏa giáo Ba Tư", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099573", "hw": "parses", "pos": "verb", "ipa": "/ˈpɑːrsɪz/", "vi": "phân tích cú pháp; mổ xẻ ngữ pháp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099574", "hw": "parsiism", "pos": "noun", "ipa": "/pɑːrˈsiːɪzəm/", "vi": "đạo Hỏa giáo Ba Tư", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099575", "hw": "parsimoniously", "pos": "adv", "ipa": "/ˌpɑːrsɪˈmoʊniəsli/", "vi": "một cách bủn xỉn; quá tiết kiệm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099576", "hw": "parsimoniousness", "pos": "noun", "ipa": "/ˌpɑːrsɪˈmoʊniəsnəs/", "vi": "tính bủn xỉn; thói keo kiệt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099577", "hw": "parsing", "pos": "noun", "ipa": "/ˈpɑːrsɪŋ/", "vi": "việc phân tích cú pháp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099578", "hw": "parsonic", "pos": "adj", "ipa": "/pɑːrˈsɑːnɪk/", "vi": "thuộc mục sư; kiểu giáo sĩ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099579", "hw": "partaken", "pos": "verb", "ipa": "/pɑːrˈteɪkən/", "vi": "đã dự phần; đã cùng chia sẻ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099580", "hw": "partakers", "pos": "noun", "ipa": "/pɑːrˈteɪkərz/", "vi": "những người cùng dự phần", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099581", "hw": "partan", "pos": "noun", "ipa": "/ˈpɑːrtən/", "vi": "cua biển ăn được (từ Scotland)", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099582", "hw": "parthenocarpic", "pos": "adj", "ipa": "/ˌpɑːrθɪnoʊˈkɑːrpɪk/", "vi": "thuộc tạo quả không hạt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099583", "hw": "parthenocarpy", "pos": "noun", "ipa": "/ˌpɑːrθɪnoʊˈkɑːrpi/", "vi": "hiện tượng sinh quả không hạt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099584", "hw": "parthenocissus", "pos": "noun", "ipa": "/ˌpɑːrθɪnoʊˈsɪsəs/", "vi": "chi nho dại leo Parthenocissus", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099585", "hw": "parthenogamy", "pos": "noun", "ipa": "/ˌpɑːrθɪˈnɑːɡəmi/", "vi": "sự tiếp hợp nhân đơn tính", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099586", "hw": "parthenogenetically", "pos": "adv", "ipa": "/ˌpɑːrθɪnoʊdʒəˈnɛtɪkli/", "vi": "bằng hình thức trinh sinh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099587", "hw": "parthenogeny", "pos": "noun", "ipa": "/ˌpɑːrθɪˈnɑːdʒəni/", "vi": "sự trinh sản; sinh sản đơn tính", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099588", "hw": "parthenote", "pos": "noun", "ipa": "/ˈpɑːrθənoʊt/", "vi": "hợp tử trinh sản", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099589", "hw": "parti", "pos": "noun", "ipa": "/pɑːrˈtiː/", "vi": "ý niệm kiến trúc chủ đạo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099590", "hw": "partiable", "pos": "adj", "ipa": "/ˈpɑːrtiəbəl/", "vi": "có thể phân chia được", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099591", "hw": "partialism", "pos": "noun", "ipa": "/ˈpɑːrʃəlɪzəm/", "vi": "thái độ thiên vị; tính phiến diện", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099592", "hw": "partialness", "pos": "noun", "ipa": "/ˈpɑːrʃəlnəs/", "vi": "tính cục bộ; tính không hoàn chỉnh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099593", "hw": "partibility", "pos": "noun", "ipa": "/ˌpɑːrtəˈbɪləti/", "vi": "khả năng phân chia tài sản", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099594", "hw": "participance", "pos": "noun", "ipa": "/pɑːrˈtɪsɪpəns/", "vi": "sự tham gia; sự dự phần", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099595", "hw": "participants", "pos": "noun", "ipa": "/pɑːrˈtɪsɪpənts/", "vi": "các người tham gia; các thành viên", "cefr": "B1", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099596", "hw": "participated", "pos": "verb", "ipa": "/pɑːrˈtɪsɪpeɪtɪd/", "vi": "đã tham gia; đã dự vào", "cefr": "B1", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099597", "hw": "participates", "pos": "verb", "ipa": "/pɑːrˈtɪsɪpeɪts/", "vi": "tham gia; dự vào", "cefr": "B1", "tier": "core", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099598", "hw": "participational", "pos": "adj", "ipa": "/pɑːrˌtɪsɪˈpeɪʃənl/", "vi": "thuộc hình thức tham gia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099599", "hw": "participative", "pos": "adj", "ipa": "/pɑːrˈtɪsɪpeɪtɪv/", "vi": "có tính đồng tham gia", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099600", "hw": "participator", "pos": "noun", "ipa": "/pɑːrˈtɪsɪpeɪtər/", "vi": "người tham gia; người dự phần", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.099601", "hw": "participators", "pos": "noun", "ipa": "/pɑːrˈtɪsɪpeɪtərz/", "vi": "những người tham gia; người dự phần", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Validation
raw_items = json.load(open('scratch/b20_r10_raw_p1.json', 'r', encoding='utf-8'))
assert len(part1_data) == 100
assert len(raw_items) == 100

for i, item in enumerate(part1_data):
    raw = raw_items[i]
    assert item["id"] == raw["id"], f"ID mismatch at {i}: {item['id']} vs {raw['id']}"
    assert item["hw"] == raw["hw"], f"HW mismatch at {i}: {item['hw']} vs {raw['hw']}"
    assert len(item["vi"]) <= 35, f"vi too long at {i} ({item['hw']}): {item['vi']} ({len(item['vi'])} chars)"
    assert item["pos"] in ["noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num"], f"Invalid pos at {i}: {item['pos']}"
    assert item["ipa"].startswith("/") and item["ipa"].endswith("/") and item["ipa"].count("/") == 2, f"Invalid ipa at {i}: {item['ipa']}"
    assert item["status"] == "reviewed"
    item["cefr"] = raw.get("cefr", "C2")
    item["tier"] = raw.get("tier", "expanded")
    item["notes"] = raw.get("notes", "")

with open('scratch/b20_r10_p1.json', 'w', encoding='utf-8') as f:
    json.dump(part1_data, f, ensure_ascii=False, indent=2)

print("b20_r10_p1.json created successfully and validated!")
