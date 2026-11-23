import json

items = [
  {"id": "lex.en.200k.063203", "hw": "upanishads", "pos": "noun", "ipa": "/uˈpænɪʃædz/", "vi": "kinh triết học Ấn Độ Upanishad"},
  {"id": "lex.en.200k.063204", "hw": "verdigrises", "pos": "noun", "ipa": "/ˈvɜːrdɪɡriːsɪz/", "vi": "lớp gỉ xanh trên bề mặt đồng"},
  {"id": "lex.en.200k.063205", "hw": "verdigrising", "pos": "verb", "ipa": "/ˈvɜːrdɪɡriːsɪŋ/", "vi": "đang phủ lên lớp gỉ đồng xanh"},
  {"id": "lex.en.200k.063206", "hw": "walkaways", "pos": "noun", "ipa": "/ˈwɔːkəweɪz/", "vi": "trận thắng áp đảo dễ dàng; bỏ cuộc"},
  {"id": "lex.en.200k.063207", "hw": "wiffles", "pos": "noun", "ipa": "/ˈwɪfəlz/", "vi": "cú thổi nhẹ; bóng nhựa đục lỗ"},
  {"id": "lex.en.200k.063208", "hw": "winfreds", "pos": "noun", "ipa": "/ˈwɪnfrɪdz/", "vi": "Thánh truyền giáo Anh Winfrid"},
  {"id": "lex.en.200k.063209", "hw": "acer saccharum", "pos": "phrase", "ipa": "/ˈeɪsər ˈsækərəm/", "vi": "cây phong đường lấy mật Bắc Mỹ"},
  {"id": "lex.en.200k.063210", "hw": "apocrine gland", "pos": "phrase", "ipa": "/ˈæpəkrɪn ɡlænd/", "vi": "tuyến mồ hôi đầu tiết vùng nách bẹn"},
  {"id": "lex.en.200k.063211", "hw": "aristarchus of samos", "pos": "phrase", "ipa": "/ˌærɪˈstɑːrkəs əv ˈseɪmɑːs/", "vi": "nhà thiên văn cổ đại Aristarchus"},
  {"id": "lex.en.200k.063212", "hw": "boysenberry bush", "pos": "phrase", "ipa": "/ˈbɔɪzənˌbɛri bʊʃ/", "vi": "cây bụi mâm xôi lai boysenberry"},
  {"id": "lex.en.200k.063213", "hw": "branchial cleft", "pos": "phrase", "ipa": "/ˈbræŋkiəl klɛft/", "vi": "khe mang ở phôi thai và cá"},
  {"id": "lex.en.200k.063214", "hw": "calamus penna", "pos": "phrase", "ipa": "/ˈkæləməs ˈpɛnə/", "vi": "cá tráp porgy Đại Tây Dương"},
  {"id": "lex.en.200k.063215", "hw": "codling moth", "pos": "phrase", "ipa": "/ˈkɑːdlɪŋ mɔːθ/", "vi": "bướm đêm sâu đục quả táo lê"},
  {"id": "lex.en.200k.063216", "hw": "common staghorn fern", "pos": "phrase", "ipa": "/ˈkɑːmən ˈstæɡhɔːrn fɜːrn/", "vi": "cây dương xỉ ổ rồng sừng hươu"},
  {"id": "lex.en.200k.063217", "hw": "cowpea plant", "pos": "phrase", "ipa": "/ˈkaʊpiː plænt/", "vi": "cây đậu đũa; cây đậu mắt đen"},
  {"id": "lex.en.200k.063218", "hw": "creme de menthe", "pos": "phrase", "ipa": "/ˌkrɛm də ˈmɑːnθ/", "vi": "rượu mùi bạc hà ngọt xanh Pháp"},
  {"id": "lex.en.200k.063219", "hw": "cycladic civilisation", "pos": "phrase", "ipa": "/saɪˈklædɪk ˌsɪvələˈzeɪʃən/", "vi": "văn minh Cyclades cổ đại (Anh)"},
  {"id": "lex.en.200k.063220", "hw": "drum majorette", "pos": "phrase", "ipa": "/drʌm ˌmeɪdʒəˈrɛt/", "vi": "nữ tiếp viên múa gậy dẫn đội nhạc"},
  {"id": "lex.en.200k.063221", "hw": "eero saarinen", "pos": "phrase", "ipa": "/ˈɛəroʊ ˈsɑːrənən/", "vi": "kiến trúc sư Phần Lan Eero Saarinen"},
  {"id": "lex.en.200k.063222", "hw": "epigastric fossa", "pos": "phrase", "ipa": "/ˌɛpɪˈɡæstrɪk ˈfɑːsə/", "vi": "hõm thượng vị ngay dưới xương ức"},
  {"id": "lex.en.200k.063223", "hw": "fyodor mikhailovich dostoevsky", "pos": "phrase", "ipa": "/ˈfjɔːdər mɪˈxaɪləvɪtʃ ˌdɔːstəˈjɛfski/", "vi": "đại văn hào Nga Dostoevsky"},
  {"id": "lex.en.200k.063224", "hw": "genus fraxinus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈfræksɪnəs/", "vi": "chi cây tần bì gỗ dẻo Fraxinus"},
  {"id": "lex.en.200k.063225", "hw": "genus lepus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈliːpəs/", "vi": "chi thỏ rừng chạy nhanh Lepus"},
  {"id": "lex.en.200k.063226", "hw": "genus mandragora", "pos": "phrase", "ipa": "/ˈdʒiːnəs mænˈdræɡərə/", "vi": "chi cây ma cà rồng Mandragora"},
  {"id": "lex.en.200k.063227", "hw": "genus morus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈmɔːrəs/", "vi": "chi cây dâu tằm nuôi tằm Morus"},
  {"id": "lex.en.200k.063228", "hw": "genus plumeria", "pos": "phrase", "ipa": "/ˈdʒiːnəs pluːˈmɪriə/", "vi": "chi cây hoa sứ hoa đại Plumeria"},
  {"id": "lex.en.200k.063229", "hw": "genus rickettsia", "pos": "phrase", "ipa": "/ˈdʒiːnəs rɪˈkɛtsiə/", "vi": "chi vi khuẩn ký sinh Rickettsia"},
  {"id": "lex.en.200k.063230", "hw": "glenoid cavity", "pos": "phrase", "ipa": "/ˈɡliːnɔɪd ˈkævəti/", "vi": "ổ chảo xương bả vai khớp cánh tay"},
  {"id": "lex.en.200k.063231", "hw": "hageman factor", "pos": "phrase", "ipa": "/ˈhæɡəmən ˈfæktər/", "vi": "yếu tố XII đông máu Hageman"},
  {"id": "lex.en.200k.063232", "hw": "hugh capet", "pos": "phrase", "ipa": "/hjuː ˈkeɪpət/", "vi": "vua sáng lập triều Capet Pháp Hugh"},
  {"id": "lex.en.200k.063233", "hw": "jaroslav hasek", "pos": "phrase", "ipa": "/ˈjɑːrəslɑːf ˈhɑːʃɛk/", "vi": "nhà văn Séc Jaroslav Hašek"},
  {"id": "lex.en.200k.063234", "hw": "joe bloggs", "pos": "phrase", "ipa": "/dʒoʊ blɑːɡz/", "vi": "người dân bình thường nói chung"},
  {"id": "lex.en.200k.063235", "hw": "karol wojtyla", "pos": "phrase", "ipa": "/ˈkɑːrɔːl vɔɪˈtiːwə/", "vi": "Giáo hoàng Gioan Phaolô II Wojtyla"},
  {"id": "lex.en.200k.063236", "hw": "lactobacillus acidophilus", "pos": "phrase", "ipa": "/ˌlæktəbəˈsɪləs ˌæsɪˈdɑːfɪləs/", "vi": "lợi khuẩn đường ruột acidophilus"},
  {"id": "lex.en.200k.063237", "hw": "laparoscopic cholecystectomy", "pos": "phrase", "ipa": "/ˌlæpərəˈskɑːpɪk ˌkɑːlɪsɪsˈtɛktəmi/", "vi": "phẫu thuật nội soi cắt bỏ túi mật"},
  {"id": "lex.en.200k.063238", "hw": "manila maguey", "pos": "phrase", "ipa": "/məˈnɪlə ˈmæɡweɪ/", "vi": "sợi cây thùa Manila làm dây thừng"},
  {"id": "lex.en.200k.063239", "hw": "martes americana", "pos": "phrase", "ipa": "/ˈmɑːrtiːz əˌmɛrɪˈkænə/", "vi": "chồn thông vàng Bắc Mỹ Martes"},
  {"id": "lex.en.200k.063240", "hw": "mignonette family", "pos": "phrase", "ipa": "/ˌmɪnjəˈnɛt ˈfæməli/", "vi": "họ cây Mộc tê thảo Resedaceae"},
  {"id": "lex.en.200k.063241", "hw": "mikhail ivanovich kalinin", "pos": "phrase", "ipa": "/mɪˈxaɪl iˈvɑːnəvɪtʃ kəˈliːnɪn/", "vi": "chủ tịch Xô Viết Mikhail Kalinin"},
  {"id": "lex.en.200k.063242", "hw": "minato ohashi bridge", "pos": "phrase", "ipa": "/miˈnɑːtoʊ oʊˈhɑːʃi brɪdʒ/", "vi": "cầu giàn thép Minato Ohashi ở Osaka"},
  {"id": "lex.en.200k.063243", "hw": "myelinated nerve fiber", "pos": "phrase", "ipa": "/ˈmaɪəlɪˌneɪtɪd nɜːrv ˈfaɪbər/", "vi": "sợi thần kinh bọc bao myelin"},
  {"id": "lex.en.200k.063244", "hw": "papaw tree", "pos": "phrase", "ipa": "/ˈpɔːpɔː triː/", "vi": "cây na gai Bắc Mỹ; cây đu đủ"},
  {"id": "lex.en.200k.063245", "hw": "peter carl goldmark", "pos": "phrase", "ipa": "/ˈpiːtər kɑːrl ˈɡoʊldmɑːrk/", "vi": "kỹ sư đĩa hát LP Peter Goldmark"},
  {"id": "lex.en.200k.063246", "hw": "peter goldmark", "pos": "phrase", "ipa": "/ˈpiːtər ˈɡoʊldmɑːrk/", "vi": "nhà phát minh TV màu Peter Goldmark"},
  {"id": "lex.en.200k.063247", "hw": "prunus spinosa", "pos": "phrase", "ipa": "/ˈpruːnəs spɪˈnoʊsə/", "vi": "cây mận gai đen làm rượu sloe"},
  {"id": "lex.en.200k.063248", "hw": "pudendal artery", "pos": "phrase", "ipa": "/pjuːˈdɛndəl ˈɑːrtəri/", "vi": "động mạch thẹn cấp máu đáy chậu"},
  {"id": "lex.en.200k.063249", "hw": "pudendal block", "pos": "phrase", "ipa": "/pjuːˈdɛndəl blɑːk/", "vi": "gây tê thần kinh thẹn khi sinh đẻ"},
  {"id": "lex.en.200k.063250", "hw": "pudendal vein", "pos": "phrase", "ipa": "/pjuːˈdɛndəl veɪn/", "vi": "tĩnh mạch thẹn vùng đáy chậu"},
  {"id": "lex.en.200k.063251", "hw": "ranunculus repens", "pos": "phrase", "ipa": "/rəˈnʌŋkjʊləs ˈriːpɛnz/", "vi": "cây mao lương bò hoa vàng óng"},
  {"id": "lex.en.200k.063252", "hw": "saale glaciation", "pos": "phrase", "ipa": "/ˈzɑːlə ˌɡleɪsiˈeɪʃən/", "vi": "thời kỳ băng hà Saale ở châu Âu"},
  {"id": "lex.en.200k.063253", "hw": "santa gertrudis", "pos": "phrase", "ipa": "/ˈsæntə ɡərˈtruːdɪs/", "vi": "giống bò thịt đỏ Santa Gertrudis"},
  {"id": "lex.en.200k.063254", "hw": "silky tamarin", "pos": "phrase", "ipa": "/ˈsɪlki ˈtæmərɪn/", "vi": "khỉ sư tử vàng lông mượt Brazil"},
  {"id": "lex.en.200k.063255", "hw": "staghorn fern", "pos": "phrase", "ipa": "/ˈstæɡhɔːrn fɜːrn/", "vi": "cây dương xỉ sừng hươu bám thân gỗ"},
  {"id": "lex.en.200k.063256", "hw": "thomas bowdler", "pos": "phrase", "ipa": "/ˈtɑːməs ˈbaʊdlər/", "vi": "bác sĩ chuyên cắt xén sách Bowdler"},
  {"id": "lex.en.200k.063257", "hw": "visual agnosia", "pos": "phrase", "ipa": "/ˈvɪʒuəl æɡˈnoʊʒə/", "vi": "chứng mù nhận thức đồ vật thị giác"},
  {"id": "lex.en.200k.063258", "hw": "von willebrand", "pos": "phrase", "ipa": "/vɑːn ˈvɪləbrænd/", "vi": "bác sĩ Phần Lan von Willebrand"},
  {"id": "lex.en.200k.063259", "hw": "welsh rarebit", "pos": "phrase", "ipa": "/wɛlʃ ˈrɛərbɪt/", "vi": "bánh mì nướng phô mai sốt bia Wales"},
  {"id": "lex.en.200k.063260", "hw": "wood hoopoe", "pos": "phrase", "ipa": "/wʊd ˈhuːpuː/", "vi": "chim đầu rìu rừng đuôi dài châu Phi"},
  {"id": "lex.en.200k.063261", "hw": "yersinia pestis", "pos": "phrase", "ipa": "/jərˈsɪniə ˈpɛstɪs/", "vi": "trực khuẩn gây bệnh dịch hạch"},
  {"id": "lex.en.200k.063262", "hw": "zanzibar copal", "pos": "phrase", "ipa": "/ˈzænzɪˌbɑːr ˈkoʊpəl/", "vi": "nhựa thơm copal vùng Zanzibar"},
  {"id": "lex.en.200k.063263", "hw": "zonal pelargonium", "pos": "phrase", "ipa": "/ˈzoʊnəl ˌpɛlərˈɡoʊniəm/", "vi": "cây phong lữ thảo lá có vòng đai"},
  {"id": "lex.en.200k.063264", "hw": "aetiologies", "pos": "noun", "ipa": "/ˌiːtiˈɑːlədʒiz/", "vi": "nguyên nhân học gây bệnh tật (Anh)"},
  {"id": "lex.en.200k.063265", "hw": "alehouses", "pos": "noun", "ipa": "/ˈeɪlhaʊzɪz/", "vi": "quán rượu bia truyền thống thời xưa"},
  {"id": "lex.en.200k.063266", "hw": "aleuts", "pos": "noun", "ipa": "/əˈluːts/", "vi": "người bản địa quần đảo Aleut Alaska"},
  {"id": "lex.en.200k.063267", "hw": "amontillados", "pos": "noun", "ipa": "/əˌmɑːntɪˈjɑːdoʊz/", "vi": "rượu vang sherry Amontillado"},
  {"id": "lex.en.200k.063268", "hw": "anoxias", "pos": "noun", "ipa": "/æˈnɑːksiəz/", "vi": "tình trạng mô cơ thể thiếu hẳn oxy"},
  {"id": "lex.en.200k.063269", "hw": "arrheniuses", "pos": "noun", "ipa": "/əˈriːniəsɪz/", "vi": "nhà hóa học Thụy Điển Arrhenius"},
  {"id": "lex.en.200k.063270", "hw": "arterioscleroses", "pos": "noun", "ipa": "/ɑːrˌtɪrioʊskləˈroʊsiːz/", "vi": "chứng xơ cứng dày thành động mạch"},
  {"id": "lex.en.200k.063271", "hw": "averroeses", "pos": "noun", "ipa": "/əˈvɛroʊˌiːzɪz/", "vi": "triết gia Ả Rập trung cổ Averroes"},
  {"id": "lex.en.200k.063272", "hw": "bitterroots", "pos": "noun", "ipa": "/ˈbɪtərruːts/", "vi": "cây hoa đá rễ đắng vùng Bắc Mỹ"},
  {"id": "lex.en.200k.063273", "hw": "blubbed", "pos": "verb", "ipa": "/blʌbd/", "vi": "đã khóc nức nở sưng mắt (lóng Anh)"},
  {"id": "lex.en.200k.063274", "hw": "blubbing", "pos": "verb", "ipa": "/ˈblʌbɪŋ/", "vi": "đang khóc lóc rưng rức (lóng Anh)"},
  {"id": "lex.en.200k.063275", "hw": "blubs", "pos": "verb", "ipa": "/blʌbz/", "vi": "khóc thút thít sướt mướt (lóng Anh)"},
  {"id": "lex.en.200k.063276", "hw": "boethiuses", "pos": "noun", "ipa": "/boʊˈiːθiəsɪz/", "vi": "triết gia La Mã hậu kỳ Boethius"},
  {"id": "lex.en.200k.063277", "hw": "burundians", "pos": "noun", "ipa": "/bəˈrʌndiənz/", "vi": "công dân quốc gia Đông Phi Burundi"},
  {"id": "lex.en.200k.063278", "hw": "carpentarias", "pos": "noun", "ipa": "/ˌkɑːrpənˈtɛriəz/", "vi": "vịnh Carpentaria phía bắc nước Úc"},
  {"id": "lex.en.200k.063279", "hw": "casuarinas", "pos": "noun", "ipa": "/ˌkæʒuəˈriːnəz/", "vi": "cây phi lao chắn cát vùng ven biển"},
  {"id": "lex.en.200k.063280", "hw": "cathedras", "pos": "noun", "ipa": "/kəˈθiːdrəz/", "vi": "ngai tòa giám mục trong nhà thờ"},
  {"id": "lex.en.200k.063281", "hw": "cedis", "pos": "noun", "ipa": "/ˈsiːdiz/", "vi": "đơn vị tiền tệ cedi của nước Ghana"},
  {"id": "lex.en.200k.063282", "hw": "chequebooks", "pos": "noun", "ipa": "/ˈtʃɛkbʊks/", "vi": "cuốn sổ ngân phiếu séc (Anh)"},
  {"id": "lex.en.200k.063283", "hw": "coloraturas", "pos": "noun", "ipa": "/ˌkʌlərəˈtʊrəz/", "vi": "giọng nữ cao luyến láy điêu luyện"},
  {"id": "lex.en.200k.063284", "hw": "conjunctivae", "pos": "noun", "ipa": "/ˌkɑːndʒʌŋkˈtaɪviː/", "vi": "màng kết mạc bảo vệ mi và nhãn cầu"},
  {"id": "lex.en.200k.063285", "hw": "conjunctivas", "pos": "noun", "ipa": "/ˌkɑːndʒʌŋkˈtaɪvəz/", "vi": "các lớp màng kết mạc mỏng của mắt"},
  {"id": "lex.en.200k.063286", "hw": "counterarguments", "pos": "noun", "ipa": "/ˌkaʊntərˈɑːrɡjəmənts/", "vi": "lập luận phản bác ý kiến đối lập"},
  {"id": "lex.en.200k.063287", "hw": "crabapples", "pos": "noun", "ipa": "/ˈkræbˌæpəlz/", "vi": "cây và quả táo dại vị chua làm mứt"},
  {"id": "lex.en.200k.063288", "hw": "crakes", "pos": "noun", "ipa": "/kreɪks/", "vi": "chim gà nước nhỏ cánh ngắn crake"},
  {"id": "lex.en.200k.063289", "hw": "crustaceas", "pos": "noun", "ipa": "/krʌˈsteɪʃəz/", "vi": "ngành động vật giáp xác có vỏ cứng"},
  {"id": "lex.en.200k.063290", "hw": "culti", "pos": "noun", "ipa": "/ˈkʌltaɪ/", "vi": "giáo phái dị đoan; nghi lễ tôn sùng"},
  {"id": "lex.en.200k.063291", "hw": "cultuses", "pos": "noun", "ipa": "/ˈkʌltəsɪz/", "vi": "các hệ thống nghi lễ thờ phụng"},
  {"id": "lex.en.200k.063292", "hw": "curtseyed", "pos": "verb", "ipa": "/ˈkɜːrtsid/", "vi": "đã nhún gối cúi chào kiểu lễ nghi"},
  {"id": "lex.en.200k.063293", "hw": "curtseying", "pos": "verb", "ipa": "/ˈkɜːrtsiɪŋ/", "vi": "đang khẽ nhún đầu gối chào lịch sự"},
  {"id": "lex.en.200k.063294", "hw": "curtseys", "pos": "noun", "ipa": "/ˈkɜːrtsiz/", "vi": "cái nhún gối cúi chào của phụ nữ"},
  {"id": "lex.en.200k.063295", "hw": "cybeles", "pos": "noun", "ipa": "/ˈsɪbəliːz/", "vi": "nữ thần đất mẹ Phrygia cổ Cybele"},
  {"id": "lex.en.200k.063296", "hw": "dampeners", "pos": "noun", "ipa": "/ˈdæmpənərz/", "vi": "bộ giảm chấn; người làm mất hứng"},
  {"id": "lex.en.200k.063297", "hw": "daoisms", "pos": "noun", "ipa": "/ˈdaʊɪzəmz/", "vi": "triết lý và tôn giáo Đạo giáo"},
  {"id": "lex.en.200k.063298", "hw": "dilators", "pos": "noun", "ipa": "/daɪˈleɪtərz/", "vi": "dụng cụ nong rộng; cơ giãn đồng tử"},
  {"id": "lex.en.200k.063299", "hw": "diplomates", "pos": "noun", "ipa": "/ˈdɪpləmeɪts/", "vi": "bác sĩ chuyên khoa đạt chứng chỉ"},
  {"id": "lex.en.200k.063300", "hw": "disrobed", "pos": "verb", "ipa": "/dɪsˈroʊbd/", "vi": "đã cởi bỏ áo choàng; lột trang phục"},
  {"id": "lex.en.200k.063301", "hw": "disrobes", "pos": "verb", "ipa": "/dɪsˈroʊbz/", "vi": "cởi bỏ y phục lễ phục; tước áo chức"},
  {"id": "lex.en.200k.063302", "hw": "disrobing", "pos": "verb", "ipa": "/dɪsˈroʊbɪŋ/", "vi": "đang cởi bỏ lễ phục quần áo"}
]

with open('scratch/b33_r07_raw_p3.json') as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"Mismatch id at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"Mismatch hw at {i}: {item['hw']} vs {r['hw']}"
    assert len(item['vi']) <= 35, f"vi length > 35 at {i} ({item['hw']}): {len(item['vi'])}"
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {item['pos']}"
    assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Invalid ipa at {i}: {item['ipa']}"
    assert not item['ipa'][1:-1].startswith(' ') and not item['ipa'][1:-1].endswith(' '), f"Space in ipa at {i}: {item['ipa']}"
    r['pos'] = item['pos']
    r['ipa'] = item['ipa']
    r['vi'] = item['vi']
    r['status'] = 'reviewed'

with open('scratch/b33_r07_p3.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r07_p3.json OK")
