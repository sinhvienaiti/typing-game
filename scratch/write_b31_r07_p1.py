import json

items = [
  {"id": "lex.en.200k.053002", "hw": "cuddies", "pos": "noun", "ipa": "/ˈkʌdiz/", "vi": "con lừa nhỏ; căn buồng nhỏ trên tàu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053003", "hw": "cuttlefishes", "pos": "noun", "ipa": "/ˈkʌtlfɪʃɪz/", "vi": "các con mực nang biển", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053004", "hw": "decanters", "pos": "noun", "ipa": "/dɪˈkæntərz/", "vi": "các bình thủy tinh chiết rượu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053005", "hw": "deconstructed", "pos": "verb", "ipa": "/ˌdiːkənˈstrʌktɪd/", "vi": "đã giải cấu trúc; tháo dỡ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053006", "hw": "deconstructing", "pos": "verb", "ipa": "/ˌdiːkənˈstrʌktɪŋ/", "vi": "đang giải cấu trúc; phân tích", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053007", "hw": "deconstructs", "pos": "verb", "ipa": "/ˌdiːkənˈstrʌkts/", "vi": "giải cấu trúc văn bản", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053008", "hw": "dimaggios", "pos": "noun", "ipa": "/dɪˈmɑːdʒioʊz/", "vi": "huyền thoại bóng chày Joe DiMaggio", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053009", "hw": "discouragements", "pos": "noun", "ipa": "/dɪsˈkɜːrɪdʒmənts/", "vi": "sự nản lòng; điều làm nhụt chí", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053010", "hw": "divans", "pos": "noun", "ipa": "/daɪˈvænz/", "vi": "ghế đi-văng dài không lưng tựa", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053011", "hw": "dossed", "pos": "verb", "ipa": "/dɑːst/", "vi": "đã ngủ tạm bợ qua đêm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053012", "hw": "dosses", "pos": "verb", "ipa": "/ˈdɑːsɪz/", "vi": "ngủ tạm bợ qua đêm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053013", "hw": "dossing", "pos": "verb", "ipa": "/ˈdɑːsɪŋ/", "vi": "ngủ tạm bợ; sự ngủ lang bạt", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053014", "hw": "ecclesiasteses", "pos": "noun", "ipa": "/ɪˌkliːziˈæstiːziːz/", "vi": "sách Giảng Viên trong Kinh Thánh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053015", "hw": "elbes", "pos": "noun", "ipa": "/ˈɛlbəz/", "vi": "dòng sông Elbe ở Trung Âu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053016", "hw": "endicotts", "pos": "noun", "ipa": "/ˈɛndɪkəts/", "vi": "thống đốc John Endecott", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053017", "hw": "erises", "pos": "noun", "ipa": "/ˈɛrɪsɪz/", "vi": "hành tinh lùn Eris; nữ thần Eris", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053018", "hw": "esrs", "pos": "noun", "ipa": "/ˌiːˌɛsˈɑːrz/", "vi": "chỉ số tốc độ lắng hồng cầu ESR", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053019", "hw": "expressionists", "pos": "noun", "ipa": "/ɪkˈsprɛʃənɪsts/", "vi": "nghệ sĩ trường phái biểu hiện", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053020", "hw": "fibreglasses", "pos": "noun", "ipa": "/ˈfaɪbərɡlæsɪz/", "vi": "các loại sợi thủy tinh composite", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053021", "hw": "flexors", "pos": "noun", "ipa": "/ˈflɛksərz/", "vi": "các nhóm cơ gập; cơ gấp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053022", "hw": "garudas", "pos": "noun", "ipa": "/ɡəˈruːdəz/", "vi": "loài chim thần Garuda Ấn Độ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053023", "hw": "gaucher", "pos": "adj", "ipa": "/ɡoʊˈʃeɪər/", "vi": "vụng về hơn; ngượng nghịu hơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053024", "hw": "gauchest", "pos": "adj", "ipa": "/ɡoʊˈʃeɪɪst/", "vi": "vụng về nhất; ngượng nghịu nhất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053025", "hw": "gooseberries", "pos": "noun", "ipa": "/ˈɡuːzbɛriz/", "vi": "các quả lý gai gooseberry", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053026", "hw": "handlebars", "pos": "noun", "ipa": "/ˈhændəlbɑːrz/", "vi": "ghi-đông xe; tay lái xe đạp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053027", "hw": "handoffs", "pos": "noun", "ipa": "/ˈhændɔːfs/", "vi": "đường chuyền tay; sự bàn giao", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053028", "hw": "headlamps", "pos": "noun", "ipa": "/ˈhɛdlæmps/", "vi": "đèn pha trước xe; đèn đội đầu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053029", "hw": "heinleins", "pos": "noun", "ipa": "/ˈhaɪnlaɪnz/", "vi": "nhà văn Robert Heinlein", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053030", "hw": "iaas", "pos": "noun", "ipa": "/ˈaɪ.æz/", "vi": "hạ tầng như một dịch vụ IaaS", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053031", "hw": "inducements", "pos": "noun", "ipa": "/ɪnˈduːsmənts/", "vi": "động cơ khuyến khích; sự dẫn dụ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053032", "hw": "infomercials", "pos": "noun", "ipa": "/ˈɪnfoʊmɜːrʃəlz/", "vi": "chương trình quảng cáo thông tin", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053033", "hw": "iranis", "pos": "noun", "ipa": "/ɪˈrɑːniz/", "vi": "người dân Iran; người Ba Tư", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053034", "hw": "ishtars", "pos": "noun", "ipa": "/ˈɪʃtɑːrz/", "vi": "nữ thần Ishtar thành Babylon", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053035", "hw": "joyrides", "pos": "noun", "ipa": "/ˈdʒɔɪraɪdz/", "vi": "chuyến lái xe dạo phố mạo hiểm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053036", "hw": "joyriding", "pos": "verb", "ipa": "/ˈdʒɔɪraɪdɪŋ/", "vi": "lái xe trộm dạo phố phóng nhanh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053037", "hw": "kuomintangs", "pos": "noun", "ipa": "/ˌkwoʊmɪnˈtæŋz/", "vi": "Quốc Dân Đảng Trung Hoa", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053038", "hw": "larders", "pos": "noun", "ipa": "/ˈlɑːrdərz/", "vi": "tủ đựng thức ăn dự trữ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053039", "hw": "lasagnes", "pos": "noun", "ipa": "/ləˈzɑːnjəz/", "vi": "các món mì lát đút lò lasagna", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053040", "hw": "latrobes", "pos": "noun", "ipa": "/ləˈtroʊbz/", "vi": "kiến trúc sư Benjamin Latrobe", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053041", "hw": "lianas", "pos": "noun", "ipa": "/liˈɑːnəz/", "vi": "các loài dây leo thân gỗ nhiệt đới", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053042", "hw": "linzes", "pos": "noun", "ipa": "/ˈlɪntsɪz/", "vi": "thành phố Linz nước Áo", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053043", "hw": "loggers", "pos": "noun", "ipa": "/ˈlɔːɡərz/", "vi": "thợ đốn gỗ; chương trình ghi log", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053044", "hw": "lorcas", "pos": "noun", "ipa": "/ˈlɔːrkəz/", "vi": "nhà thơ Federico García Lorca", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053045", "hw": "macadamias", "pos": "noun", "ipa": "/ˌmækəˈdeɪmiəz/", "vi": "hạt mắc-ca; cây mắc-ca", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053046", "hw": "manets", "pos": "noun", "ipa": "/mæˈneɪz/", "vi": "danh họa Édouard Manet", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053047", "hw": "marmites", "pos": "noun", "ipa": "/ˈmɑːrmaɪts/", "vi": "chiết xuất men bia Marmite", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053048", "hw": "methionines", "pos": "noun", "ipa": "/mɪˈθaɪəniːnz/", "vi": "axit amin thiết yếu methionine", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053049", "hw": "muggier", "pos": "adj", "ipa": "/ˈmʌɡiər/", "vi": "oi ả ngột ngạt hơn; nóng ẩm hơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053050", "hw": "muggiest", "pos": "adj", "ipa": "/ˈmʌɡiɪst/", "vi": "oi ả ngột ngạt nhất; bức nhất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053051", "hw": "nighthawks", "pos": "noun", "ipa": "/ˈnaɪthɔːks/", "vi": "loài chim sơn ca đêm; kẻ cú đêm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053052", "hw": "nogaleses", "pos": "noun", "ipa": "/noʊˈɡɑːlɛsɪz/", "vi": "thành phố Nogales vùng biên giới", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053053", "hw": "objectors", "pos": "noun", "ipa": "/əbˈdʒɛktərz/", "vi": "người phản kháng; người chống đối", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053054", "hw": "oresteses", "pos": "noun", "ipa": "/ɒˈrɛstiːziːz/", "vi": "nhân vật Orestes trong thần thoại", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053055", "hw": "ozarkses", "pos": "noun", "ipa": "/ˈoʊzɑːrksɪz/", "vi": "dãy cao nguyên Ozarks ở Mỹ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053056", "hw": "paducahs", "pos": "noun", "ipa": "/pəˈduːkəz/", "vi": "thành phố Paducah bang Kentucky", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053057", "hw": "peppier", "pos": "adj", "ipa": "/ˈpɛpiər/", "vi": "tràn đầy năng lượng hơn; hoạt bát", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053058", "hw": "peppiest", "pos": "adj", "ipa": "/ˈpɛpiɪst/", "vi": "sôi nổi nhất; tràn đầy sinh lực", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053059", "hw": "pepyses", "pos": "noun", "ipa": "/ˈpiːpsɪz/", "vi": "tác giả nhật ký Samuel Pepys", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053060", "hw": "pitfalls", "pos": "noun", "ipa": "/ˈpɪtfɔːlz/", "vi": "những cạm bẫy khó lường", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053061", "hw": "polentas", "pos": "noun", "ipa": "/poʊˈlɛntəz/", "vi": "món cháo bột ngô nghiền Ý", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053062", "hw": "preteens", "pos": "noun", "ipa": "/ˌpriːˈtiːnz/", "vi": "lứa tuổi thiếu nhi trước dậy thì", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053063", "hw": "psychoanalysts", "pos": "noun", "ipa": "/ˌsaɪkoʊˈænəlɪsts/", "vi": "các chuyên gia phân tâm học", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053064", "hw": "rankines", "pos": "noun", "ipa": "/ˈræŋkɪnz/", "vi": "thang đo nhiệt độ Rankine", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053065", "hw": "rearguards", "pos": "noun", "ipa": "/ˈrɪrɡɑːrdz/", "vi": "đội quân hậu vệ bọc lót", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053066", "hw": "rebuses", "pos": "noun", "ipa": "/ˈriːbəsɪz/", "vi": "câu đố chữ hình vẽ minh họa", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053067", "hw": "reimses", "pos": "noun", "ipa": "/ˈræ̃sɪz/", "vi": "thành phố Reims nước Pháp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053068", "hw": "ritalins", "pos": "noun", "ipa": "/ˈrɪtəlɪnz/", "vi": "thuốc kích thần Ritalin", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053069", "hw": "robesons", "pos": "noun", "ipa": "/ˈroʊbsənz/", "vi": "nghệ sĩ ca sĩ Paul Robeson", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053070", "hw": "seaways", "pos": "noun", "ipa": "/ˈsiːweɪz/", "vi": "đường hàng hải; tuyến đường biển", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053071", "hw": "semiautomatics", "pos": "noun", "ipa": "/ˌsɛmiaʊtəˈmætɪks/", "vi": "súng ngắn trường bán tự động", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053072", "hw": "sigurds", "pos": "noun", "ipa": "/ˈsɪɡərdz/", "vi": "anh hùng dũng sĩ Sigurd Bắc Âu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053073", "hw": "simians", "pos": "noun", "ipa": "/ˈsɪmiənz/", "vi": "loài linh trưởng dạng khỉ vượn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053074", "hw": "spillers", "pos": "noun", "ipa": "/ˈspɪlərz/", "vi": "người làm đổ nước; kẻ làm tràn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053075", "hw": "staplers", "pos": "noun", "ipa": "/ˈsteɪplərz/", "vi": "những chiếc máy bấm kim dập ghim", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053076", "hw": "sternes", "pos": "noun", "ipa": "/stɜːrnz/", "vi": "nhà văn Laurence Sterne", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053077", "hw": "subroutines", "pos": "noun", "ipa": "/ˈsʌbruːtiːnz/", "vi": "các chương trình con lập trình", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053078", "hw": "tammanies", "pos": "noun", "ipa": "/ˈtæməniz/", "vi": "bộ máy chính trị Tammany Hall", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053079", "hw": "telephotos", "pos": "noun", "ipa": "/ˌtɛləˈfoʊtoʊz/", "vi": "ống kính chụp xa telephoto", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053080", "hw": "thimbles", "pos": "noun", "ipa": "/ˈθɪmbəlz/", "vi": "chiếc đê bảo vệ ngón tay khâu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053081", "hw": "timurs", "pos": "noun", "ipa": "/tɪˈmʊrz/", "vi": "hoàng đế chinh phục Timur Lame", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053082", "hw": "tokios", "pos": "noun", "ipa": "/ˈtoʊkioʊz/", "vi": "thủ đô Tokyo Nhật Bản", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053083", "hw": "triptychs", "pos": "noun", "ipa": "/ˈtrɪptɪks/", "vi": "bộ tranh tam liên họa ba bức", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053084", "hw": "trnas", "pos": "noun", "ipa": "/ˌtiːˌɑːrˌɛnˈeɪz/", "vi": "các phân tử tARN vận chuyển", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053085", "hw": "tuaregs", "pos": "noun", "ipa": "/ˈtwɑːrɛɡz/", "vi": "bộ tộc du mục Tuareg sa mạc", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053086", "hw": "tugboats", "pos": "noun", "ipa": "/ˈtʌɡboʊts/", "vi": "các tàu kéo tàu lai dắt cảng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053087", "hw": "uralses", "pos": "noun", "ipa": "/ˈjʊərəlzɪz/", "vi": "dãy núi Ural ranh giới Á-Âu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053088", "hw": "venezias", "pos": "noun", "ipa": "/vəˈnɛtsioʊz/", "vi": "thành phố kênh đào Venice Ý", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053089", "hw": "visualisations", "pos": "noun", "ipa": "/ˌvɪʒuəlaɪˈzeɪʃənz/", "vi": "sự trực quan hóa hình ảnh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053090", "hw": "welshmans", "pos": "noun", "ipa": "/ˈwɛlʃmənz/", "vi": "người đàn ông xứ Wales", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053091", "hw": "wrinklier", "pos": "adj", "ipa": "/ˈrɪŋkliər/", "vi": "nhăn nheo hơn; nhiều nếp nhăn hơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053092", "hw": "wrinkliest", "pos": "adj", "ipa": "/ˈrɪŋkliɪst/", "vi": "nhăn nheo nhất; nhiều nếp nhăn nhất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053093", "hw": "zamans", "pos": "noun", "ipa": "/zəˈmɑːnz/", "vi": "loài cây muồng tím me tây", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053094", "hw": "zirconias", "pos": "noun", "ipa": "/zɜːrˈkoʊniəz/", "vi": "đá quý khối nhân tạo zirconia", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053095", "hw": "zolofts", "pos": "noun", "ipa": "/ˈzoʊlɒfts/", "vi": "thuốc chống trầm cảm Zoloft", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053096", "hw": "ad nauseam", "pos": "phrase", "ipa": "/ˌæd ˈnɔːziəm/", "vi": "nói đi nói lại đến phát ngán", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053097", "hw": "amun ra", "pos": "phrase", "ipa": "/ˈɑːmuːn ˈrɑː/", "vi": "thần mặt trời Amun-Ra Ai Cập", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053098", "hw": "arcuate artery", "pos": "phrase", "ipa": "/ˈɑːrkjʊeɪt ˈɑːrtəri/", "vi": "động mạch hình cung thận và chân", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053099", "hw": "attar of roses", "pos": "phrase", "ipa": "/ˈætər əv ˈroʊzɪz/", "vi": "tinh dầu hoa hồng nguyên chất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.0530100" if False else "lex.en.200k.053100", "hw": "banded anteater", "pos": "phrase", "ipa": "/ˈbændɪd ˈæntiːtər/", "vi": "thú ăn kiến thú có túi numbat", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053101", "hw": "baron munchausen", "pos": "phrase", "ipa": "/ˈbærən ˈmʊntʃˌhaʊzən/", "vi": "nam tước ba hoa Munchausen", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
]

assert len(items) == 100, f"Expected 100, got {len(items)}"
raw = json.load(open('scratch/b31_r07_raw_p1.json'))
assert len(raw) == 100, f"Expected raw 100, got {len(raw)}"

valid_pos = {'noun', 'verb', 'adj', 'adv', 'phrase', 'intj', 'prep', 'conj', 'pron', 'det', 'num'}

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"ID mismatch at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"HW mismatch at {i}: {item['hw']} vs {r['hw']}"
    assert item['pos'] in valid_pos, f"Invalid POS {item['pos']} at {i}"
    assert len(item['vi']) <= 35, f"vi too long ({len(item['vi'])} chars) at {i}: {item['vi']}"
    assert len(item['vi']) > 0, f"empty vi at {i}"
    assert item['status'] == 'reviewed', f"status not reviewed at {i}"
    if ' ' not in item['hw']:
        assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and len(item['ipa']) > 2, f"Invalid IPA at {i}: {item['ipa']}"
        assert item['ipa'].count('/') == 2, f"IPA count slashes != 2 at {i}: {item['ipa']}"
    else:
        if item['ipa']:
            assert item['ipa'].startswith('/') and item['ipa'].endswith('/'), f"Invalid phrase IPA at {i}: {item['ipa']}"

with open('scratch/b31_r07_p1.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Validated and saved 100 items for Part 1")
