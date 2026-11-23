# -*- coding: utf-8 -*-
import json

part2_data = [
  {"id": "lex.en.200k.053602", "hw": "genus arius", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈɛəriəs/", "vi": "chi cá úc biển Arius", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053603", "hw": "genus bellis", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈbɛlɪs/", "vi": "chi hoa cúc dại Bellis", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053604", "hw": "genus caiman", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈkeɪmən/", "vi": "chi cá sấu Caiman Nam Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053605", "hw": "genus xenopus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈzɛnəpəs/", "vi": "chi ếch có móng Xenopus", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053606", "hw": "glaciations", "pos": "noun", "ipa": "/ˌɡleɪʃiˈeɪʃənz/", "vi": "các thời kỳ băng hà phủ kín", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053607", "hw": "glutamines", "pos": "noun", "ipa": "/ˈɡluːtəmiːnz/", "vi": "axit amin glutamine sinh học", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053608", "hw": "glycolic acid", "pos": "phrase", "ipa": "/ɡlaɪˈkɑːlɪk ˈæsɪd/", "vi": "axit glycolic dưỡng da tẩy tế bào", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053609", "hw": "gomorrahs", "pos": "noun", "ipa": "/ɡəˈmɔːrəz/", "vi": "thành bang sa đồi Gomorrah", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053610", "hw": "goofballs", "pos": "noun", "ipa": "/ˈɡuːfbɔːlz/", "vi": "kẻ ngớ ngẩn; viên thuốc an thần", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053611", "hw": "gordian knot", "pos": "phrase", "ipa": "/ˈɡɔːrdiən nɑːt/", "vi": "nút thắt Gordian nan giải", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053612", "hw": "great ragweed", "pos": "phrase", "ipa": "/ɡreɪt ˈræɡwiːd/", "vi": "cây cỏ phấn hương khổng lồ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053613", "hw": "hairstylists", "pos": "noun", "ipa": "/ˈhɛrstaɪlɪsts/", "vi": "chuyên viên tạo mẫu tóc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053614", "hw": "harpies", "pos": "noun", "ipa": "/ˈhɑːrpiz/", "vi": "quái điểu Harpy; mụ đàn bà dữ dằn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053615", "hw": "hatha yoga", "pos": "phrase", "ipa": "/ˈhɑːtə ˈjoʊɡə/", "vi": "trường phái yoga Hatha cổ điển", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053616", "hw": "havelocks", "pos": "noun", "ipa": "/ˈhævlɑːks/", "vi": "mũ trùm vải che gáy Havelock", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053617", "hw": "henri bergson", "pos": "phrase", "ipa": "/ɑːnˈriː ˈbɛərɡsən/", "vi": "triết gia Pháp Henri Bergson", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053618", "hw": "henri louis bergson", "pos": "phrase", "ipa": "/ɑːnˈriː ˈluːi ˈbɛərɡsən/", "vi": "triết gia Henri-Louis Bergson", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053619", "hw": "hernan cortes", "pos": "phrase", "ipa": "/ɛərˈnɑːn kɔːrˈtɛz/", "vi": "nhà chinh phục Hernán Cortés", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053620", "hw": "hieing", "pos": "verb", "ipa": "/ˈhaɪɪŋ/", "vi": "đang rảo bước; đang vội vã", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053621", "hw": "hipped roof", "pos": "phrase", "ipa": "/hɪpt ruːf/", "vi": "kiểu mái nhà dốc bốn phía", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053622", "hw": "hippocrateses", "pos": "noun", "ipa": "/hɪˈpɑːkrətiːzɪz/", "vi": "danh y Hippocrates Hy Lạp cổ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053623", "hw": "humeral veil", "pos": "phrase", "ipa": "/ˈhjuːmərəl veɪl/", "vi": "khăn phủ vai của linh mục", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053624", "hw": "hypnotists", "pos": "noun", "ipa": "/ˈhɪpnətɪsts/", "vi": "các nhà thôi miên trị liệu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053625", "hw": "isosceles triangle", "pos": "phrase", "ipa": "/aɪˌsɑːsəliːz ˈtraɪæŋɡəl/", "vi": "hình tam giác cân hình học", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053626", "hw": "jackfruit tree", "pos": "phrase", "ipa": "/ˈdʒækfruːt triː/", "vi": "cây mít nhiệt đới quả to", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053627", "hw": "jauntier", "pos": "adj", "ipa": "/ˈdʒɔːntiər/", "vi": "vui vẻ hơn; bảnh bao hơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053628", "hw": "jauntiest", "pos": "adj", "ipa": "/ˈdʒɔːntiɪst/", "vi": "vui vẻ nhất; bảnh bao tự tin nhất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053629", "hw": "john dos passos", "pos": "phrase", "ipa": "/dʒɑːn dəs ˈpæsəs/", "vi": "nhà văn Mỹ John Dos Passos", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053630", "hw": "jonesboros", "pos": "noun", "ipa": "/ˈdʒoʊnzbɜːroʊz/", "vi": "thành phố Jonesboro ở Arkansas", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053631", "hw": "jutlands", "pos": "noun", "ipa": "/ˈdʒʌtləndz/", "vi": "bán đảo Jutland của Đan Mạch", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053632", "hw": "kiribatis", "pos": "noun", "ipa": "/ˈkɪrɪbætiz/", "vi": "quốc đảo Kiribati Thái Bình Dương", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053633", "hw": "knaves", "pos": "noun", "ipa": "/neɪvz/", "vi": "quân bồi lá bài; kẻ gian giảo", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053634", "hw": "kneecapped", "pos": "verb", "ipa": "/ˈniːkæpt/", "vi": "đã bắn vào đầu gối trừng phạt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053635", "hw": "kneecaps", "pos": "noun", "ipa": "/ˈniːkæps/", "vi": "xương bánh chè ở đầu gối", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053636", "hw": "kurosawas", "pos": "noun", "ipa": "/ˌkʊroʊˈsɑːwəz/", "vi": "đạo diễn Nhật Akira Kurosawa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053637", "hw": "lakefronts", "pos": "noun", "ipa": "/ˈleɪkfrʌnts/", "vi": "khu đất ven hồ nhìn ra hồ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053638", "hw": "large magellanic cloud", "pos": "phrase", "ipa": "/lɑːrdʒ ˌmædʒəˈlænɪk klaʊd/", "vi": "Đám mây Magellan Lớn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053639", "hw": "ledas", "pos": "noun", "ipa": "/ˈliːdəz/", "vi": "hoàng hậu Leda trong thần thoại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053640", "hw": "legalisations", "pos": "noun", "ipa": "/ˌliːɡəlaɪˈzeɪʃənz/", "vi": "thủ tục hợp pháp hóa văn bản", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053641", "hw": "lemmons", "pos": "noun", "ipa": "/ˈlɛmənz/", "vi": "nam diễn viên Mỹ Jack Lemmon", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053642", "hw": "logbooks", "pos": "noun", "ipa": "/ˈlɔːɡbʊks/", "vi": "sổ nhật ký hàng hải hành trình", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053643", "hw": "logical positivist", "pos": "phrase", "ipa": "/ˈlɑːdʒɪkəl ˈpɑːzətɪvɪst/", "vi": "người theo thực chứng logic", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053644", "hw": "loopers", "pos": "noun", "ipa": "/ˈluːpərz/", "vi": "loài sâu đo; con lăn tạo vòng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053645", "hw": "magellanic cloud", "pos": "phrase", "ipa": "/ˌmædʒəˈlænɪk klaʊd/", "vi": "Đám mây Magellan thiên văn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053646", "hw": "malmos", "pos": "noun", "ipa": "/ˈmælməʊz/", "vi": "thành phố cảng Malmö ở Thụy Điển", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053647", "hw": "marie stopes", "pos": "phrase", "ipa": "/məˈriː stoʊps/", "vi": "nhà vận động Marie Stopes", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053648", "hw": "mariposas", "pos": "noun", "ipa": "/ˌmærɪˈpoʊsəz/", "vi": "hoa huệ mariposa xứ California", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053649", "hw": "matzo ball", "pos": "phrase", "ipa": "/ˈmɑːtsə bɔːl/", "vi": "viên bánh súp bột matzo Do Thái", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053650", "hw": "matzo meal", "pos": "phrase", "ipa": "/ˈmɑːtsə miːl/", "vi": "bột bánh mì không men matzo", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053651", "hw": "meriwether lewis", "pos": "phrase", "ipa": "/ˌmɛriwɛðər ˈluːɪs/", "vi": "nhà thám hiểm Meriwether Lewis", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053652", "hw": "merrimacks", "pos": "noun", "ipa": "/ˈmɛrɪmæks/", "vi": "dòng sông Merrimack ở Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053653", "hw": "methodisms", "pos": "noun", "ipa": "/ˈmɛθədɪzəmz/", "vi": "các phong trào Giám Lý Tin Lành", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053654", "hw": "metrologies", "pos": "noun", "ipa": "/mɛˈtrɑːlədʒiz/", "vi": "khoa học đo lường định lượng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053655", "hw": "mint julep", "pos": "phrase", "ipa": "/mɪnt ˈdʒuːlɪp/", "vi": "cocktail bourbon bạc hà đá bào", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053656", "hw": "mohs scale", "pos": "phrase", "ipa": "/moʊz skeɪl/", "vi": "thang đo độ cứng khoáng vật Mohs", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053657", "hw": "mons pubis", "pos": "phrase", "ipa": "/mɑːnz ˈpjuːbɪs/", "vi": "gò mu vùng xương mu cơ thể", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053658", "hw": "moravias", "pos": "noun", "ipa": "/məˈreɪviəz/", "vi": "vùng lịch sử Moravia xứ Séc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053659", "hw": "motorboats", "pos": "noun", "ipa": "/ˈmoʊtərbəʊts/", "vi": "thuyền máy chạy động cơ cao tốc", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053660", "hw": "nannas", "pos": "noun", "ipa": "/ˈnænəz/", "vi": "bà ngoại; bà nội thân thương", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053661", "hw": "nostradamuses", "pos": "noun", "ipa": "/ˌnɑːstrəˈdeɪməsɪz/", "vi": "nhà tiên tri Nostradamus", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053662", "hw": "nunneries", "pos": "noun", "ipa": "/ˈnʌnəriz/", "vi": "các tu viện dành cho nữ tu dòng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053663", "hw": "oregonians", "pos": "noun", "ipa": "/ˌɔːrɪˈɡoʊniənz/", "vi": "cư dân bang Oregon nước Mỹ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053664", "hw": "parana river", "pos": "phrase", "ipa": "/pærəˈnɑː ˈrɪvər/", "vi": "dòng sông Paraná ở Nam Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053665", "hw": "paretos", "pos": "noun", "ipa": "/pəˈreɪtoʊz/", "vi": "nhà kinh tế học Vilfredo Pareto", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053666", "hw": "peculiarities", "pos": "noun", "ipa": "/pɪˌkjuːliˈærətiz/", "vi": "nét đặc thù riêng biệt; tính kỳ lạ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053667", "hw": "peridots", "pos": "noun", "ipa": "/ˈpɛrɪdɑːts/", "vi": "ngọc peridot màu xanh ô liu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053668", "hw": "peter abelard", "pos": "phrase", "ipa": "/ˈpiːtər ˈæbəlɑːrd/", "vi": "triết gia Pháp Peter Abelard", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053669", "hw": "physicked", "pos": "verb", "ipa": "/ˈfɪzɪkt/", "vi": "đã cho uống thuốc tẩy xổ chữa trị", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053670", "hw": "physicking", "pos": "verb", "ipa": "/ˈfɪzɪkɪŋ/", "vi": "đang cho dùng thuốc xổ điều trị", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053671", "hw": "pica pica", "pos": "phrase", "ipa": "/ˈpaɪkə ˈpaɪkə/", "vi": "loài chim ác là Á-Âu đuôi dài", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053672", "hw": "pickpockets", "pos": "noun", "ipa": "/ˈpɪkpɑːkɪts/", "vi": "những kẻ chuyên móc túi cắp vặt", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053673", "hw": "piezo effect", "pos": "phrase", "ipa": "/piˈeɪzoʊ ɪˈfɛkt/", "vi": "hiệu ứng áp điện nén sinh điện", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053674", "hw": "pimento butter", "pos": "phrase", "ipa": "/pɪˈmɛntoʊ ˈbʌtər/", "vi": "bơ trộn ớt chuông ngọt phết bánh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053675", "hw": "pimento tree", "pos": "phrase", "ipa": "/pɪˈmɛntoʊ triː/", "vi": "cây tiêu hương Jamaica hạt thơm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053676", "hw": "pipa americana", "pos": "phrase", "ipa": "/ˈpiːpə əˌmɛrɪˈkɑːnə/", "vi": "loài cóc tổ ong Pipa Suriname", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053677", "hw": "proxima centauri", "pos": "phrase", "ipa": "/ˌprɑːksɪmə sɛnˈtɔːraɪ/", "vi": "sao Cận Tinh gần Hệ Mặt Trời", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053678", "hw": "puebla de zaragoza", "pos": "phrase", "ipa": "/ˈpwɛblə deɪ ˌzærəˈɡoʊzə/", "vi": "thành phố Puebla của Mexico", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053679", "hw": "quartos", "pos": "noun", "ipa": "/ˈkwɔːrtoʊz/", "vi": "các tập sách in khổ bốn trang", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053680", "hw": "questioners", "pos": "noun", "ipa": "/ˈkwɛstʃənərz/", "vi": "những người đặt câu hỏi chất vấn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053681", "hw": "randall jarrell", "pos": "phrase", "ipa": "/ˈrændəl dʒəˈrɛl/", "vi": "nhà thơ phê bình Randall Jarrell", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053682", "hw": "rasmus christian rask", "pos": "phrase", "ipa": "/ˈræsməs ˈkrɪstʃən ˈræsk/", "vi": "học giả ngôn ngữ Rasmus Rask", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053683", "hw": "red pimpernel", "pos": "phrase", "ipa": "/rɛd ˈpɪmpərnɛl/", "vi": "cây an lạc hoa đỏ thắm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053684", "hw": "refried beans", "pos": "phrase", "ipa": "/ˌriːfraɪd ˈbiːnz/", "vi": "món đậu nghiền xào kiểu Mexico", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053685", "hw": "remarriages", "pos": "noun", "ipa": "/riːˈmærɪdʒɪz/", "vi": "các cuộc tái hôn kết hôn lại", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053686", "hw": "revelries", "pos": "noun", "ipa": "/ˈrɛvəlriz/", "vi": "những cuộc liên hoan chè chén say", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053687", "hw": "robert peary", "pos": "phrase", "ipa": "/ˈrɑːbərt ˈpɪəri/", "vi": "nhà thám hiểm Bắc Cực Robert Peary", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053688", "hw": "rotisseries", "pos": "noun", "ipa": "/roʊˈtɪsəriz/", "vi": "lò nướng thịt quay trục xoay tròn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053689", "hw": "sceptics", "pos": "noun", "ipa": "/ˈskɛptɪks/", "vi": "những người có tư tưởng hoài nghi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053690", "hw": "scrims", "pos": "noun", "ipa": "/skrɪmz/", "vi": "màn the mỏng trong sân khấu kịch", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053691", "hw": "seedless raisin", "pos": "phrase", "ipa": "/ˈsiːdləs ˈreɪzən/", "vi": "nho khô không hạt ngọt dịu", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053692", "hw": "shalom asch", "pos": "phrase", "ipa": "/ʃəˈloʊm æʃ/ ", "vi": "nhà văn Do Thái Sholem Asch", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053693", "hw": "sherbets", "pos": "noun", "ipa": "/ˈʃɜːrbəts/", "vi": "kem tuyết sorbet trái cây tươi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053694", "hw": "siddharthas", "pos": "noun", "ipa": "/sɪˈdɑːrtəz/", "vi": "Đức Phật Thích Ca Tất Đạt Đa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053695", "hw": "simpletons", "pos": "noun", "ipa": "/ˈsɪmpəltənz/", "vi": "những kẻ khờ khạo dễ tin dạ đần", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053696", "hw": "small magellanic cloud", "pos": "phrase", "ipa": "/smɔːl ˌmædʒəˈlænɪk klaʊd/", "vi": "Đám mây Magellan Nhỏ thiên văn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053697", "hw": "smallmouth bass", "pos": "phrase", "ipa": "/ˈsmɔːlmaʊθ bæs/", "vi": "loài cá vược đen miệng nhỏ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053698", "hw": "smallmouth black bass", "pos": "phrase", "ipa": "/ˈsmɔːlmaʊθ blæk bæs/", "vi": "cá vược đen miệng nhỏ Bắc Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053699", "hw": "soapboxes", "pos": "noun", "ipa": "/ˈsoʊpbɑːksɪz/", "vi": "hòm gỗ diễn thuyết đường phố công", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053700", "hw": "standardisations", "pos": "noun", "ipa": "/ˌstændərdaɪˈzeɪʃənz/", "vi": "việc tiêu chuẩn hóa đồng bộ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053701", "hw": "striders", "pos": "noun", "ipa": "/ˈstraɪdərz/", "vi": "người sải bước dài; con bọ nước", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Clean ipa trailing space if any
for it in part2_data:
    it['ipa'] = it['ipa'].strip()

# Validation
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

assert len(part2_data) == 100, f"Length is {len(part2_data)}"

with open('scratch/b31_r08_raw_p2.json') as f:
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

with open('scratch/b31_r08_p2.json', 'w', encoding='utf-8') as f:
    json.dump(part2_data, f, ensure_ascii=False, indent=2)

print("Validated and saved 100 items for Part 2")
