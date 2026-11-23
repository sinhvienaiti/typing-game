import json

items = [
  {"id": "lex.en.200k.052902", "hw": "frank winfield woolworth", "pos": "phrase", "ipa": "/fræŋk ˈwɪnfiːld ˈwʊlwərθ/", "vi": "Frank Woolworth; ông trùm bán lẻ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052903", "hw": "freshwater limpet", "pos": "phrase", "ipa": "/ˈfrɛʃwɔːtər ˈlɪmpɪt/", "vi": "ốc nón nước ngọt ancylidae", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052904", "hw": "funicular railway", "pos": "phrase", "ipa": "/fjuːˈnɪkjələr ˈreɪlweɪ/", "vi": "tuyến đường sắt leo núi cáp kéo", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052905", "hw": "fyodor dostoevsky", "pos": "phrase", "ipa": "/ˈfjɔːdər ˌdɒstəˈjɛfski/", "vi": "đại văn hào Fyodor Dostoevsky", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052906", "hw": "genus brassica", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈbræsɪkə/", "vi": "chi cải bắp brassica", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052907", "hw": "genus uca", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈjuːkə/", "vi": "chi còng gió; chi cua cáy kéo đàn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052908", "hw": "grantor trust", "pos": "phrase", "ipa": "/ˈɡræntər trʌst/", "vi": "quỹ ủy thác của người lập quỹ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052909", "hw": "graven image", "pos": "phrase", "ipa": "/ˈɡreɪvən ˈɪmɪdʒ/", "vi": "tượng chạm khắc thờ cúng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052910", "hw": "gray goldenrod", "pos": "phrase", "ipa": "/ɡreɪ ˈɡoʊldənrɑːd/", "vi": "cây hoàng kim xám hoa vàng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052911", "hw": "grey goldenrod", "pos": "phrase", "ipa": "/ɡreɪ ˈɡoʊldənrɑːd/", "vi": "cây hoa cúc hoàng anh xám", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052912", "hw": "gustave flaubert", "pos": "phrase", "ipa": "/ɡysˈtav floʊˈbɛr/", "vi": "Gustave Flaubert; văn hào Pháp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052913", "hw": "henry bolingbroke", "pos": "phrase", "ipa": "/ˈhɛnri ˈbɑːlɪŋbrʊk/", "vi": "Henry Bolingbroke; vua Henry IV", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052914", "hw": "hepatocellular carcinoma", "pos": "phrase", "ipa": "/ˌhɛpətoʊˈsɛljələr ˌkɑːrsəˈnoʊmə/", "vi": "ung thư biểu mô tế bào gan", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052915", "hw": "heterocyclic compound", "pos": "phrase", "ipa": "/ˌhɛtərəˈsaɪklɪk ˈkɑːmpaʊnd/", "vi": "hợp chất hóa học dị vòng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052916", "hw": "heterocyclic ring", "pos": "phrase", "ipa": "/ˌhɛtərəˈsaɪklɪk rɪŋ/", "vi": "vòng dị nguyên tử hóa học", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052917", "hw": "hypoglycemic agent", "pos": "phrase", "ipa": "/ˌhaɪpoʊɡlaɪˈsiːmɪk ˈeɪdʒənt/", "vi": "thuốc làm hạ đường huyết", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052918", "hw": "insect repellant", "pos": "phrase", "ipa": "/ˈɪnsɛkt rɪˈpɛlənt/", "vi": "thuốc xịt đuổi côn trùng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052919", "hw": "isadora duncan", "pos": "phrase", "ipa": "/ˌɪzəˈdɔːrə ˈdʌŋkən/", "vi": "vũ công múa Isadora Duncan", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052920", "hw": "johan august strindberg", "pos": "phrase", "ipa": "/ˈjuːhɑːn ˈaʊɡʊst ˈstrɪndbərɡ/", "vi": "August Strindberg; kịch tác gia", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052921", "hw": "john addington symonds", "pos": "phrase", "ipa": "/dʒɑːn ˈædɪŋtən ˈsɪməndz/", "vi": "nhà văn John Addington Symonds", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052922", "hw": "john birks gillespie", "pos": "phrase", "ipa": "/dʒɑːn bɜːrks ɡɪˈlɛspi/", "vi": "Dizzy Gillespie; nghệ sĩ jazz", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052923", "hw": "judas iscariot", "pos": "phrase", "ipa": "/ˈdʒuːdəs ɪsˈkæriət/", "vi": "Giu-đa Ít-ca-ri-ốt kẻ phản bội", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052924", "hw": "kaffir pox", "pos": "phrase", "ipa": "/ˈkæfər pɑːks/", "vi": "bệnh đậu mùa nhẹ alastrim", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052925", "hw": "kitchen midden", "pos": "phrase", "ipa": "/ˈkɪtʃɪn ˈmɪdən/", "vi": "đống rác vỏ sò thời tiền sử", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052926", "hw": "lamprey eel", "pos": "phrase", "ipa": "/ˈlæmpri iːl/", "vi": "cá mút đá không hàm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052927", "hw": "lochaber ax", "pos": "phrase", "ipa": "/lɑːkˈhɑːbər æks/", "vi": "vũ khí rìu cán dài Lochaber", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052928", "hw": "luciano pavarotti", "pos": "phrase", "ipa": "/luːˈtʃɑːnoʊ ˌpævəˈrɑːti/", "vi": "Luciano Pavarotti; danh ca opera", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052929", "hw": "marcel marceau", "pos": "phrase", "ipa": "/mɑːrˈsɛl mɑːrˈsoʊ/", "vi": "Marcel Marceau; bậc thầy kịch câm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052930", "hw": "mauna kea", "pos": "phrase", "ipa": "/ˈmaʊnə ˈkeɪə/", "vi": "núi lửa Mauna Kea ở Hawaii", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052931", "hw": "missouri goldenrod", "pos": "phrase", "ipa": "/mɪˈzʊri ˈɡoʊldənrɑːd/", "vi": "cúc hoàng anh Missouri", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052932", "hw": "moon trefoil", "pos": "phrase", "ipa": "/muːn ˈtrɛfɔɪl/", "vi": "cỏ ba lá ánh trăng medicago", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052933", "hw": "munchausen syndrome", "pos": "phrase", "ipa": "/ˈmʊntʃˌhaʊzən ˈsɪndroʊm/", "vi": "hội chứng tâm thần Munchausen", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052934", "hw": "nada daiquiri", "pos": "phrase", "ipa": "/ˈnɑːdə ˈdaɪkəri/", "vi": "cocktail daiquiri không cồn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052935", "hw": "narrow goldenrod", "pos": "phrase", "ipa": "/ˈnæroʊ ˈɡoʊldənrɑːd/", "vi": "cúc hoàng anh lá hẹp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052936", "hw": "nez perce", "pos": "phrase", "ipa": "/ˌnɛz ˈpɜːrs/", "vi": "bộ tộc thổ dân da đỏ Nez Perce", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052937", "hw": "ohio goldenrod", "pos": "phrase", "ipa": "/oʊˈhaɪoʊ ˈɡoʊldənrɑːd/", "vi": "cúc hoàng anh bang Ohio", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052938", "hw": "omnidirectional radio range", "pos": "phrase", "ipa": "/ˌɑːmnidəˈrɛkʃənl ˈreɪdioʊ reɪndʒ/", "vi": "đài vô tuyến đa hướng VOR", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052939", "hw": "omnidirectional range", "pos": "phrase", "ipa": "/ˌɑːmnidəˈrɛkʃənl reɪndʒ/", "vi": "đài vô tuyến điều hướng đa hướng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052940", "hw": "parti pris", "pos": "phrase", "ipa": "/ˌpɑːrtiː ˈpriː/", "vi": "thành kiến có sẵn; định kiến", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052941", "hw": "pentatonic scale", "pos": "phrase", "ipa": "/ˌpɛntəˈtɑːnɪk skeɪl/", "vi": "âm giai ngũ cung năm nốt", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052942", "hw": "perching bird", "pos": "phrase", "ipa": "/ˈpɜːrtʃɪŋ bɜːrd/", "vi": "loài chim biết đậu cành cây", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052943", "hw": "petrus stuyvesant", "pos": "phrase", "ipa": "/ˈpiːtrəs ˈstaɪvəsənt/", "vi": "toàn quyền Petrus Stuyvesant", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052944", "hw": "pneumococcal pneumonia", "pos": "phrase", "ipa": "/ˌnuːməˈkɑːkl nuːˈmoʊnjə/", "vi": "viêm phổi do phế cầu khuẩn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052945", "hw": "pneumococcal vaccine", "pos": "phrase", "ipa": "/ˌnuːməˈkɑːkl vækˈsiːn/", "vi": "vắc-xin ngừa khuẩn phế cầu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052946", "hw": "quilted bedspread", "pos": "phrase", "ipa": "/ˈkwɪltɪd ˈbɛdsprɛd/", "vi": "ga phủ giường chần bông", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052947", "hw": "red rockfish", "pos": "phrase", "ipa": "/rɛd ˈrɑːkfɪʃ/", "vi": "loài cá đá đỏ sebastes", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052948", "hw": "robert southey", "pos": "phrase", "ipa": "/ˈrɑːbərt ˈsaʊði/", "vi": "nhà thơ Robert Southey nước Anh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052949", "hw": "royal national eisteddfod", "pos": "phrase", "ipa": "/ˈrɔɪəl ˈnæʃnəl aɪsˈtɛðvɑːd/", "vi": "đại hội văn hóa xứ Wales", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052950", "hw": "saint irenaeus", "pos": "phrase", "ipa": "/seɪnt ˌaɪrəˈniːəs/", "vi": "thánh Irenaeus thành Lyon", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052951", "hw": "saint vitus dance", "pos": "phrase", "ipa": "/seɪnt ˈvaɪtəs dæns/", "vi": "chứng múa giật Sydenham", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052952", "hw": "scalded milk", "pos": "phrase", "ipa": "/ˈskɔːldɪd mɪlk/", "vi": "sữa đun gần sôi tiệt trùng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052953", "hw": "scarlet bugler", "pos": "phrase", "ipa": "/ˈskɑːrlət ˈbjuːɡlər/", "vi": "hoa mõm sói chuông đỏ penstemon", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052954", "hw": "scintillation counter", "pos": "phrase", "ipa": "/ˌsɪntəˈleɪʃən ˈkaʊntər/", "vi": "máy đếm nhấp nháy bức xạ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052955", "hw": "sea of marmara", "pos": "phrase", "ipa": "/siː əv ˈmɑːrmərə/", "vi": "biển nội địa Marmara ở Thổ Nhĩ Kỳ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052956", "hw": "short shrift", "pos": "phrase", "ipa": "/ʃɔːrt ʃrɪft/", "vi": "giải quyết qua loa; bác bỏ thẳng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052957", "hw": "sir john gielgud", "pos": "phrase", "ipa": "/sɜːr dʒɑːn ˈɡiːlɡʊd/", "vi": "ngài John Gielgud; diễn viên", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052958", "hw": "sixtus iv", "pos": "phrase", "ipa": "/ˈsɪkstəs ðə fɔːrθ/", "vi": "giáo hoàng Sixtô IV La Mã", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052959", "hw": "solvay process", "pos": "phrase", "ipa": "/ˈsɑːlveɪ ˈprɑːsɛs/", "vi": "quy trình Solvay sản xuất sô-đa", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052960", "hw": "spendthrift trust", "pos": "phrase", "ipa": "/ˈspɛndθrɪft trʌst/", "vi": "quỹ ủy thác ngừa tiêu xài hoang", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052961", "hw": "spreading bellflower", "pos": "phrase", "ipa": "/ˈsprɛdɪŋ ˈbɛlflaʊər/", "vi": "cây hoa chuông xòe cánh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052962", "hw": "sublingual vein", "pos": "phrase", "ipa": "/sʌbˈlɪŋɡwəl veɪn/", "vi": "tĩnh mạch dưới lưỡi", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052963", "hw": "swaddling bands", "pos": "phrase", "ipa": "/ˈswɑːdlɪŋ bændz/", "vi": "dải băng quấn tã em bé", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052964", "hw": "swaddling clothes", "pos": "phrase", "ipa": "/ˈswɑːdlɪŋ kloʊðz/", "vi": "tã vải quấn trẻ sơ sinh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052965", "hw": "sweet goldenrod", "pos": "phrase", "ipa": "/swiːt ˈɡoʊldənrɑːd/", "vi": "cúc hoàng anh lá thơm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052966", "hw": "tall bellflower", "pos": "phrase", "ipa": "/tɔːl ˈbɛlflaʊər/", "vi": "cây hoa chuông thân cao", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052967", "hw": "tall goldenrod", "pos": "phrase", "ipa": "/tɔːl ˈɡoʊldənrɑːd/", "vi": "cây cúc hoàng anh thân cao", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052968", "hw": "thalassemia major", "pos": "phrase", "ipa": "/ˌθæləˈsiːmiə ˈmeɪdʒər/", "vi": "bệnh tan máu bẩm sinh thể nặng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052969", "hw": "thelonious sphere monk", "pos": "phrase", "ipa": "/θəˈloʊniəs sfɪr mʌŋk/", "vi": "nghệ sĩ piano Thelonious Monk", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052970", "hw": "transdermal patch", "pos": "phrase", "ipa": "/trænzˈdɜːrməl pætʃ/", "vi": "miếng dán thuốc ngấm qua da", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052971", "hw": "tubal ligation", "pos": "phrase", "ipa": "/ˈtjuːbəl laɪˈɡeɪʃən/", "vi": "thủ thuật thắt ống dẫn trứng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052972", "hw": "ventricular septal defect", "pos": "phrase", "ipa": "/vɛnˈtrɪkjələr ˈsɛptl ˈdiːfɛkt/", "vi": "khuyết tật thông liên thất tim", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052973", "hw": "walter lippmann", "pos": "phrase", "ipa": "/ˈwɔːltər ˈlɪpmən/", "vi": "nhà báo Walter Lippmann", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052974", "hw": "wats line", "pos": "phrase", "ipa": "/wɑːts laɪn/", "vi": "đường dây viễn thông WATS", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052975", "hw": "whirling dervish", "pos": "phrase", "ipa": "/ˈwɜːrlɪŋ ˈdɜːrvɪʃ/", "vi": "tu sĩ múa xoay vòng Sufi giáo", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052976", "hw": "white mallee", "pos": "phrase", "ipa": "/waɪt ˈmæli/", "vi": "cây bạch đàn mallee trắng Úc", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052977", "hw": "yellow trefoil", "pos": "phrase", "ipa": "/ˈjɛloʊ ˈtrɛfɔɪl/", "vi": "cỏ ba lá hoa vàng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052978", "hw": "yugoslavian monetary unit", "pos": "phrase", "ipa": "/ˌjuːɡoʊˈslɑːviən ˈmɑːnəteri ˈjuːnɪt/", "vi": "tiền tệ nước Nam Tư", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052979", "hw": "aesops", "pos": "noun", "ipa": "/ˈiːsɑːps/", "vi": "các tập truyện ngụ ngôn Aesop", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052980", "hw": "agglomerations", "pos": "noun", "ipa": "/əˌɡlɑːməˈreɪʃənz/", "vi": "sự kết tụ; vùng đô thị quy tụ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052981", "hw": "alarics", "pos": "noun", "ipa": "/ˈæləˌrɪks/", "vi": "vua Alaric người Tây Goth", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052982", "hw": "alternations", "pos": "noun", "ipa": "/ˌɔːltərˈneɪʃənz/", "vi": "sự luân phiên; hiện tượng hoán vị", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052983", "hw": "anachronisms", "pos": "noun", "ipa": "/əˈnækrəˌnɪzəmz/", "vi": "điều lỗi thời; sự sai niên đại", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052984", "hw": "annapurnas", "pos": "noun", "ipa": "/ˌænəˈpʊrnəz/", "vi": "dãy núi Annapurna dãy Himalaya", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052985", "hw": "ardas", "pos": "noun", "ipa": "/ɑːrˈdɑːs/", "vi": "lời kinh cầu nguyện Ardas đạo Sikh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052986", "hw": "babylonias", "pos": "noun", "ipa": "/ˌbæbəˈloʊniəz/", "vi": "ốc xoắn babylonia; vùng Babylon", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052987", "hw": "berras", "pos": "noun", "ipa": "/ˈbɛrəz/", "vi": "huyền thoại bóng chày Yogi Berra", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052988", "hw": "bethunes", "pos": "noun", "ipa": "/bəˈθjuːnz/", "vi": "nhà giáo dục Mary McLeod Bethune", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052989", "hw": "bhaktis", "pos": "noun", "ipa": "/ˈbɑːktiz/", "vi": "lòng sùng kính bhakti Ấn Độ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052990", "hw": "blubbered", "pos": "verb", "ipa": "/ˈblʌbərd/", "vi": "đã khóc bù lu bù loa", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052991", "hw": "blubbering", "pos": "verb", "ipa": "/ˈblʌbərɪŋ/", "vi": "khóc sướt mướt; bù lu bù loa", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052992", "hw": "blubbers", "pos": "noun", "ipa": "/ˈblʌbərz/", "vi": "lớp mỡ cá voi; người hay khóc nhè", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052993", "hw": "bluebells", "pos": "noun", "ipa": "/ˈbluːbɛlz/", "vi": "những bông hoa chuông xanh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052994", "hw": "borers", "pos": "noun", "ipa": "/ˈbɔːrərz/", "vi": "con sâu đục thân; mũi khoan đục", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052995", "hw": "cantaloupes", "pos": "noun", "ipa": "/ˈkæntəloʊps/", "vi": "các quả dưa lưới cantaloupe", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052996", "hw": "coffeehouses", "pos": "noun", "ipa": "/ˈkɔːfihaʊsɪz/", "vi": "các quán cà phê; phòng trà đàm đạo", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052997", "hw": "colonists", "pos": "noun", "ipa": "/ˈkɑːlənɪsts/", "vi": "những người đi khai hoang thực dân", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052998", "hw": "cornfields", "pos": "noun", "ipa": "/ˈkɔːrnfiːldz/", "vi": "các cánh đồng bắp đồng ngô", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.052999", "hw": "counterinsurgencies", "pos": "noun", "ipa": "/ˌkaʊntərɪnˈsɜːrdʒənsiz/", "vi": "chiến dịch chống quân nổi dậy", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053000", "hw": "criminalizations", "pos": "noun", "ipa": "/ˌkrɪmɪnəlaɪˈzeɪʃənz/", "vi": "sự hình sự hóa hành vi phạm tội", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.053001", "hw": "croppers", "pos": "noun", "ipa": "/ˈkrɑːpərz/", "vi": "tá điền canh tác; cú ngã đau", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
]

assert len(items) == 100, f"Expected 100, got {len(items)}"
raw = json.load(open('scratch/b31_r06_raw_p5.json'))
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

with open('scratch/b31_r06_p5.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Validated and saved 100 items for Part 5")
