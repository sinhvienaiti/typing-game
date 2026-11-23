import json

items = [
  {"id": "lex.en.200k.064103", "hw": "lightheadednesses", "pos": "noun", "ipa": "/ˌlaɪtˈhɛdɪdnəsɪz/", "vi": "cảm giác choáng váng xây xẩm mặt"},
  {"id": "lex.en.200k.064104", "hw": "lilia", "pos": "noun", "ipa": "/ˈlɪliə/", "vi": "chi hoa bách hợp hoa loa kèn"},
  {"id": "lex.en.200k.064105", "hw": "lullies", "pos": "noun", "ipa": "/ˈlʊliz/", "vi": "nhà soạn nhạc cung đình Pháp Lully"},
  {"id": "lex.en.200k.064106", "hw": "luteins", "pos": "noun", "ipa": "/ˈluːtiːnz/", "vi": "sắc tố vàng bổ mắt lutein thực vật"},
  {"id": "lex.en.200k.064107", "hw": "malamutes", "pos": "noun", "ipa": "/ˈmæləˌmjuːts/", "vi": "giống chó kéo xe tuyết Alaska khỏe"},
  {"id": "lex.en.200k.064108", "hw": "masterships", "pos": "noun", "ipa": "/ˈmæstərʃɪps/", "vi": "trình độ bậc thầy; chức hiệu trưởng"},
  {"id": "lex.en.200k.064109", "hw": "merckxes", "pos": "noun", "ipa": "/ˈmɛrksɪz/", "vi": "cua-rơ huyền thoại Bỉ Eddy Merckx"},
  {"id": "lex.en.200k.064110", "hw": "mescals", "pos": "noun", "ipa": "/mɛˈskælz/", "vi": "cây thùa Mexico; rượu mạnh mezcal"},
  {"id": "lex.en.200k.064111", "hw": "metatheses", "pos": "noun", "ipa": "/məˈtæθəsiːz/", "vi": "hiện tượng đảo vị trí âm vị từ ngữ"},
  {"id": "lex.en.200k.064112", "hw": "minicomputers", "pos": "noun", "ipa": "/ˈmɪnikəmˌpjuːtərz/", "vi": "máy tính tầm trung đa người dùng"},
  {"id": "lex.en.200k.064113", "hw": "minnesotans", "pos": "noun", "ipa": "/ˌmɪnəˈsoʊtənz/", "vi": "người dân sinh sống bang Minnesota"},
  {"id": "lex.en.200k.064114", "hw": "missises", "pos": "noun", "ipa": "/ˈmɪsɪzɪz/", "vi": "bà xã; người vợ (khẩu ngữ thân mật)"},
  {"id": "lex.en.200k.064115", "hw": "mitochondria", "pos": "noun", "ipa": "/ˌmaɪtəˈkɑːndriə/", "vi": "ty thể bào quan sinh năng lượng"},
  {"id": "lex.en.200k.064116", "hw": "musculuses", "pos": "noun", "ipa": "/ˈmʌskjələsɪz/", "vi": "bắp cơ giải phẫu trong cơ thể"},
  {"id": "lex.en.200k.064117", "hw": "myositises", "pos": "noun", "ipa": "/ˌmaɪəˈsaɪtɪsɪz/", "vi": "chứng bệnh viêm đau mô cơ vân"},
  {"id": "lex.en.200k.064118", "hw": "newsier", "pos": "adj", "ipa": "/ˈnuːziər/", "vi": "nhiều tin tức mới hấp dẫn hơn"},
  {"id": "lex.en.200k.064119", "hw": "newsiest", "pos": "adj", "ipa": "/ˈnuːziɪst/", "vi": "nhiều tin tức nóng hổi mới nhất"},
  {"id": "lex.en.200k.064120", "hw": "noctuas", "pos": "noun", "ipa": "/ˈnɑːktʃuəz/", "vi": "chi ngài bướm đêm nâu xám Noctua"},
  {"id": "lex.en.200k.064121", "hw": "nowruzes", "pos": "noun", "ipa": "/noʊˈruːzɪz/", "vi": "lễ hội đón năm mới Ba Tư Nowruz"},
  {"id": "lex.en.200k.064122", "hw": "ornithines", "pos": "noun", "ipa": "/ˈɔːrnəθiːnz/", "vi": "axit amin chu trình urê ornithine"},
  {"id": "lex.en.200k.064123", "hw": "orthopteras", "pos": "noun", "ipa": "/ɔːrˈθɑːptərəz/", "vi": "bộ côn trùng Cánh thẳng châu chấu"},
  {"id": "lex.en.200k.064124", "hw": "papeetes", "pos": "noun", "ipa": "/ˌpɑːpeɪˈeɪteɪz/", "vi": "thủ phủ cảng Papeete đảo Tahiti"},
  {"id": "lex.en.200k.064125", "hw": "plasterworks", "pos": "noun", "ipa": "/ˈplæstərwɜːrks/", "vi": "công trình trát vữa thạch cao trần"},
  {"id": "lex.en.200k.064126", "hw": "plenitudes", "pos": "noun", "ipa": "/ˈplɛnətuːdz/", "vi": "sự sung mãn dồi dào tròn đầy trọn"},
  {"id": "lex.en.200k.064127", "hw": "plzens", "pos": "noun", "ipa": "/ˈpɪlzənz/", "vi": "thành phố bia Plzeň ở Cộng hòa Séc"},
  {"id": "lex.en.200k.064128", "hw": "porkchops", "pos": "noun", "ipa": "/ˈpɔːrktʃɑːps/", "vi": "miếng thịt sườn heo cốt lết nướng"},
  {"id": "lex.en.200k.064129", "hw": "prostatitises", "pos": "noun", "ipa": "/ˌprɑːstəˈtaɪtɪsɪz/", "vi": "chứng bệnh viêm tuyến tiền liệt"},
  {"id": "lex.en.200k.064130", "hw": "proteas", "pos": "noun", "ipa": "/ˈproʊtiəz/", "vi": "hoa cúc hoàng đế Nam Phi protea"},
  {"id": "lex.en.200k.064131", "hw": "purslanes", "pos": "noun", "ipa": "/ˈpɜːrsleɪnz/", "vi": "cây rau sam mọc bò thân mọng nước"},
  {"id": "lex.en.200k.064132", "hw": "pyroxenes", "pos": "noun", "ipa": "/paɪˈrɑːksiːnz/", "vi": "nhóm khoáng vật silicat đá núi lửa"},
  {"id": "lex.en.200k.064133", "hw": "qiblas", "pos": "noun", "ipa": "/ˈkɪbləz/", "vi": "hướng quay mặt cầu nguyện về Mecca"},
  {"id": "lex.en.200k.064134", "hw": "racialists", "pos": "noun", "ipa": "/ˈreɪʃəlɪsts/", "vi": "kẻ phân biệt kỳ thị chủng tộc"},
  {"id": "lex.en.200k.064135", "hw": "raitas", "pos": "noun", "ipa": "/ˈraɪtəz/", "vi": "món sốt sữa chua dưa chuột Ấn Độ"},
  {"id": "lex.en.200k.064136", "hw": "ramjets", "pos": "noun", "ipa": "/ˈræmdʒɛts/", "vi": "động cơ phản lực tĩnh nén khí dòng"},
  {"id": "lex.en.200k.064137", "hw": "saragossas", "pos": "noun", "ipa": "/ˌsærəˈɡɑːsəz/", "vi": "thành phố cổ Zaragoza Tây Ban Nha"},
  {"id": "lex.en.200k.064138", "hw": "seamounts", "pos": "noun", "ipa": "/ˈsiːmaʊnts/", "vi": "ngọn núi ngầm dưới đáy đại dương"},
  {"id": "lex.en.200k.064139", "hw": "sidelights", "pos": "noun", "ipa": "/ˈsaɪdlaɪts/", "vi": "đèn định vị mạn tàu; cửa kính bên"},
  {"id": "lex.en.200k.064140", "hw": "silvanuses", "pos": "noun", "ipa": "/sɪlˈveɪnəsɪz/", "vi": "thần rừng đồng ruộng La Mã Silvanus"},
  {"id": "lex.en.200k.064141", "hw": "sociobiologies", "pos": "noun", "ipa": "/ˌsoʊsioʊbaɪˈɑːlədʒiz/", "vi": "ngành xã hội sinh học tiến hóa"},
  {"id": "lex.en.200k.064142", "hw": "specifiers", "pos": "noun", "ipa": "/ˈspɛsəˌfaɪərz/", "vi": "người lập quy cách kỹ thuật; bổ tố"},
  {"id": "lex.en.200k.064143", "hw": "spicks", "pos": "noun", "ipa": "/spɪks/", "vi": "từ miệt thị người gốc Mỹ Latin"},
  {"id": "lex.en.200k.064144", "hw": "sterilizers", "pos": "noun", "ipa": "/ˈstɛrəˌlaɪzərz/", "vi": "thiết bị tiệt trùng dụng cụ y tế"},
  {"id": "lex.en.200k.064145", "hw": "stradivaris", "pos": "noun", "ipa": "/ˌstrɑːdəˈvɑːriz/", "vi": "nghệ nhân đàn vĩ cầm Ý Stradivari"},
  {"id": "lex.en.200k.064146", "hw": "subsequences", "pos": "noun", "ipa": "/ˈsʌbsəkwənsɪz/", "vi": "dãy con toán học; sự việc nối tiếp"},
  {"id": "lex.en.200k.064147", "hw": "tangshans", "pos": "noun", "ipa": "/tɑːŋˈʃɑːnz/", "vi": "thành phố công nghiệp Đường Sơn TQ"},
  {"id": "lex.en.200k.064148", "hw": "taproots", "pos": "noun", "ipa": "/ˈtæpruːts/", "vi": "rễ cọc chính cắm thẳng xuống đất"},
  {"id": "lex.en.200k.064149", "hw": "thermidors", "pos": "noun", "ipa": "/ˈθɜːrmɪdɔːrz/", "vi": "tháng Nhiệt lịch Pháp; món tôm hùm"},
  {"id": "lex.en.200k.064150", "hw": "tindals", "pos": "noun", "ipa": "/ˈtɪndəlz/", "vi": "nhà dịch Kinh Thánh Anh Tyndale"},
  {"id": "lex.en.200k.064151", "hw": "tragicomedies", "pos": "noun", "ipa": "/ˌtrædʒɪˈkɑːmədiz/", "vi": "tác phẩm bi hài kịch pha trộn"},
  {"id": "lex.en.200k.064152", "hw": "trazodones", "pos": "noun", "ipa": "/ˈtræzədoʊnz/", "vi": "thuốc chống trầm cảm ngủ trazodone"},
  {"id": "lex.en.200k.064153", "hw": "troupers", "pos": "noun", "ipa": "/ˈtruːpərz/", "vi": "diễn viên đoàn kịch; người tận tụy"},
  {"id": "lex.en.200k.064154", "hw": "tyrannosaurs", "pos": "noun", "ipa": "/tɪˈrænəˌsɔːrz/", "vi": "khủng long bạo chúa ăn thịt T-Rex"},
  {"id": "lex.en.200k.064155", "hw": "umbrians", "pos": "noun", "ipa": "/ˈʌmbriənz/", "vi": "người và ngôn ngữ cổ vùng Umbria Ý"},
  {"id": "lex.en.200k.064156", "hw": "villainesses", "pos": "noun", "ipa": "/ˈvɪlənəsɪz/", "vi": "nữ nhân vật phản diện độc ác"},
  {"id": "lex.en.200k.064157", "hw": "vincas", "pos": "noun", "ipa": "/ˈvɪŋkəz/", "vi": "cây hoa dừa cạn làm cảnh và thuốc"},
  {"id": "lex.en.200k.064158", "hw": "wristlets", "pos": "noun", "ipa": "/ˈrɪstlɪts/", "vi": "vòng đeo cổ tay; bao ấm cổ tay len"},
  {"id": "lex.en.200k.064159", "hw": "actinides", "pos": "noun", "ipa": "/ˈæktənaɪdz/", "vi": "nhóm nguyên tố phóng xạ họ actini"},
  {"id": "lex.en.200k.064160", "hw": "alkenes", "pos": "noun", "ipa": "/ˈælkiːnz/", "vi": "hiđrocacbon có liên kết đôi anken"},
  {"id": "lex.en.200k.064161", "hw": "antisera", "pos": "noun", "ipa": "/ˌæntiˈsɪrə/", "vi": "các mẫu huyết thanh giàu kháng thể"},
  {"id": "lex.en.200k.064162", "hw": "antiserums", "pos": "noun", "ipa": "/ˌæntiˈsɪrəmz/", "vi": "huyết thanh kháng thể miễn dịch"},
  {"id": "lex.en.200k.064163", "hw": "avocations", "pos": "noun", "ipa": "/ˌævəˈkeɪʃənz/", "vi": "sở thích tiêu khiển ngoài giờ làm"},
  {"id": "lex.en.200k.064164", "hw": "bedsits", "pos": "noun", "ipa": "/ˈbɛdsɪts/", "vi": "phòng trọ nhỏ kiêm phòng ngủ khách"},
  {"id": "lex.en.200k.064165", "hw": "bisected", "pos": "verb", "ipa": "/baɪˈsɛktɪd/", "vi": "đã cắt chia làm hai nửa bằng nhau"},
  {"id": "lex.en.200k.064166", "hw": "bisecting", "pos": "verb", "ipa": "/baɪˈsɛktɪŋ/", "vi": "đang cắt phân đôi thành hai nửa"},
  {"id": "lex.en.200k.064167", "hw": "bisects", "pos": "verb", "ipa": "/baɪˈsɛkts/", "vi": "cắt chia đôi làm hai phần đều nhau"},
  {"id": "lex.en.200k.064168", "hw": "bluebonnets", "pos": "noun", "ipa": "/ˈbluːˌbɑːnɪts/", "vi": "hoa lupin xanh; mũ tròn Scotland"},
  {"id": "lex.en.200k.064169", "hw": "boodles", "pos": "noun", "ipa": "/ˈbuːdəlz/", "vi": "đống tiền hối lộ phi pháp (lóng Mỹ)"},
  {"id": "lex.en.200k.064170", "hw": "bulbuls", "pos": "noun", "ipa": "/ˈbʊlbʊlz/", "vi": "chim chào mào hót hay vùng Á-Phi"},
  {"id": "lex.en.200k.064171", "hw": "bwrs", "pos": "noun", "ipa": "/ˌbiːˌdʌbəljuːˈɑːrz/", "vi": "lò phản ứng hạt nhân nước sôi BWR"},
  {"id": "lex.en.200k.064172", "hw": "cabers", "pos": "noun", "ipa": "/ˈkeɪbərz/", "vi": "thân gỗ nặng thi ném truyền thống"},
  {"id": "lex.en.200k.064173", "hw": "cambia", "pos": "noun", "ipa": "/ˈkæmbiə/", "vi": "tầng phát sinh vỏ gỗ ở thân cây"},
  {"id": "lex.en.200k.064174", "hw": "cambiums", "pos": "noun", "ipa": "/ˈkæmbiəmz/", "vi": "các lớp mô tượng tầng sinh gỗ cây"},
  {"id": "lex.en.200k.064175", "hw": "canaras", "pos": "noun", "ipa": "/ˈkænərəz/", "vi": "khu vực ven biển cổ Canara Ấn Độ"},
  {"id": "lex.en.200k.064176", "hw": "carets", "pos": "noun", "ipa": "/ˈkærəts/", "vi": "dấu mũ (^) chỉnh sửa chèn ký tự"},
  {"id": "lex.en.200k.064177", "hw": "chapaties", "pos": "noun", "ipa": "/tʃəˈpɑːtiz/", "vi": "bánh mì dẹt không men nướng Ấn Độ"},
  {"id": "lex.en.200k.064178", "hw": "chapatis", "pos": "noun", "ipa": "/tʃəˈpɑːtiz/", "vi": "bánh mì dẹt Ấn Độ làm từ bột mì"},
  {"id": "lex.en.200k.064179", "hw": "charrs", "pos": "noun", "ipa": "/tʃɑːrz/", "vi": "cá hồi suối nước lạnh vùng Bắc Cực"},
  {"id": "lex.en.200k.064180", "hw": "ciras", "pos": "noun", "ipa": "/ˌsiːˌaɪˌɑːrˈeɪz/", "vi": "nhóm Quân đội Cộng hòa Ireland CIRA"},
  {"id": "lex.en.200k.064181", "hw": "clockmakers", "pos": "noun", "ipa": "/ˈklɑːkˌmeɪkərz/", "vi": "nghệ nhân chế tác sửa chữa đồng hồ"},
  {"id": "lex.en.200k.064182", "hw": "colloquies", "pos": "noun", "ipa": "/ˈkɑːləkwiz/", "vi": "cuộc hội đàm đàm thoại trang trọng"},
  {"id": "lex.en.200k.064183", "hw": "correggios", "pos": "noun", "ipa": "/kəˈrɛdʒoʊz/", "vi": "danh họa Phục Hưng Ý Correggio"},
  {"id": "lex.en.200k.064184", "hw": "cotonous", "pos": "noun", "ipa": "/ˌkoʊtəˈnuːz/", "vi": "thành phố cảng lớn Cotonou ở Benin"},
  {"id": "lex.en.200k.064185", "hw": "credenzas", "pos": "noun", "ipa": "/krɪˈdɛnzəz/", "vi": "tủ thấp dài phòng ăn hay văn phòng"},
  {"id": "lex.en.200k.064186", "hw": "cyanoses", "pos": "noun", "ipa": "/ˌsaɪəˈnoʊsiːz/", "vi": "chứng da tím tái do thiếu oxy máu"},
  {"id": "lex.en.200k.064187", "hw": "cytogeneticses", "pos": "noun", "ipa": "/ˌsaɪtoʊdʒəˈnɛtɪksɪz/", "vi": "ngành di truyền học tế bào học"},
  {"id": "lex.en.200k.064188", "hw": "deciuses", "pos": "noun", "ipa": "/ˈdiːʃəsɪz/", "vi": "hoàng đế La Mã cổ đại Decius"},
  {"id": "lex.en.200k.064189", "hw": "edgers", "pos": "noun", "ipa": "/ˈɛdʒərz/", "vi": "máy xén viền mép cỏ; thợ viền mép"},
  {"id": "lex.en.200k.064190", "hw": "endoderms", "pos": "noun", "ipa": "/ˈɛndəˌdɜːrmz/", "vi": "lớp nội bì phôi thai tạo nội tạng"},
  {"id": "lex.en.200k.064191", "hw": "esops", "pos": "noun", "ipa": "/ˈiːsɑːps/", "vi": "chính sách cổ phiếu nhân viên ESOP"},
  {"id": "lex.en.200k.064192", "hw": "ethelreds", "pos": "noun", "ipa": "/ˈɛθəlrɛdz/", "vi": "vua Anglo-Saxon Anh Ethelred II"},
  {"id": "lex.en.200k.064193", "hw": "examens", "pos": "noun", "ipa": "/ɛɡˈzeɪmənz/", "vi": "nghi thức tự kiểm điểm lương tâm"},
  {"id": "lex.en.200k.064194", "hw": "forelegs", "pos": "noun", "ipa": "/ˈfɔːrlɛɡz/", "vi": "cặp chân trước của thú bốn chân"},
  {"id": "lex.en.200k.064195", "hw": "gawkier", "pos": "adj", "ipa": "/ˈɡɔːkiər/", "vi": "vụng về lóng ngóng thô kệch hơn"},
  {"id": "lex.en.200k.064196", "hw": "gawkiest", "pos": "adj", "ipa": "/ˈɡɔːkiɪst/", "vi": "vụng về lóng ngóng ngượng ngập nhất"},
  {"id": "lex.en.200k.064197", "hw": "glockenspiels", "pos": "noun", "ipa": "/ˈɡlɑːkənʃpiːlz/", "vi": "nhạc cụ gõ phím thanh kim loại"},
  {"id": "lex.en.200k.064198", "hw": "helvetias", "pos": "noun", "ipa": "/hɛlˈviːʃəz/", "vi": "tên cổ La Mã của đất nước Thụy Sĩ"},
  {"id": "lex.en.200k.064199", "hw": "hemlines", "pos": "noun", "ipa": "/ˈhɛmlaɪnz/", "vi": "đường gấu viền mép dưới chân váy áo"},
  {"id": "lex.en.200k.064200", "hw": "hewers", "pos": "noun", "ipa": "/ˈhjuːərz/", "vi": "thợ đẽo gỗ đá; thợ đào than mỏ"},
  {"id": "lex.en.200k.064201", "hw": "hypostases", "pos": "noun", "ipa": "/haɪˈpɑːstəsiːz/", "vi": "bản thể ngôi vị; sự ứ tụ huyết dịch"},
  {"id": "lex.en.200k.064202", "hw": "hypostasises", "pos": "noun", "ipa": "/haɪˈpɑːstəsɪsɪz/", "vi": "sự cụ thể hóa trừu tượng; bản thể"}
]

with open('scratch/b33_r09_raw_p2.json') as f:
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

with open('scratch/b33_r09_p2.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r09_p2.json OK")
