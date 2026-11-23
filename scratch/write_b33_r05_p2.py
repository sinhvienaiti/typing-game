import json

items = [
  {"id": "lex.en.200k.062103", "hw": "quatrains", "pos": "noun", "ipa": "/ˈkwɑːtreɪnz/", "vi": "khổ thơ tứ tuyệt bốn câu thơ"},
  {"id": "lex.en.200k.062104", "hw": "radiotelephones", "pos": "noun", "ipa": "/ˌreɪdioʊˈtɛləfoʊnz/", "vi": "máy điện thoại vô tuyến liên lạc"},
  {"id": "lex.en.200k.062105", "hw": "reexaminations", "pos": "noun", "ipa": "/ˌriːɪɡˌzæməˈneɪʃənz/", "vi": "cuộc kiểm tra lại; thẩm vấn lại"},
  {"id": "lex.en.200k.062106", "hw": "ribavirins", "pos": "noun", "ipa": "/ˌraɪbəˈvaɪrɪnz/", "vi": "thuốc kháng vi-rút ribavirin"},
  {"id": "lex.en.200k.062107", "hw": "sabbats", "pos": "noun", "ipa": "/ˈsæbəts/", "vi": "hội nghị phù thủy; ngày nghỉ Sabat"},
  {"id": "lex.en.200k.062108", "hw": "salicylates", "pos": "noun", "ipa": "/səˈlɪsəleɪts/", "vi": "hợp chất muối giảm đau salicylat"},
  {"id": "lex.en.200k.062109", "hw": "salmos", "pos": "noun", "ipa": "/ˈsælmoʊz/", "vi": "chi cá hồi Đại Tây Dương Salmo"},
  {"id": "lex.en.200k.062110", "hw": "samphires", "pos": "noun", "ipa": "/ˈsæmfaɪərz/", "vi": "cây rau mặn ven biển samphire"},
  {"id": "lex.en.200k.062111", "hw": "sandpits", "pos": "noun", "ipa": "/ˈsændpɪts/", "vi": "hố cát sân chơi; hố nhảy xa"},
  {"id": "lex.en.200k.062112", "hw": "sednas", "pos": "noun", "ipa": "/ˈsɛdnəz/", "vi": "nữ thần biển Sedna; hành tinh lùn"},
  {"id": "lex.en.200k.062113", "hw": "sheetrocks", "pos": "noun", "ipa": "/ˈʃiːtrɑːks/", "vi": "tấm vách thạch cao ốp trần tường"},
  {"id": "lex.en.200k.062114", "hw": "shemas", "pos": "noun", "ipa": "/ʃəˈmɑːz/", "vi": "bài kinh cầu nguyện Shema Do Thái"},
  {"id": "lex.en.200k.062115", "hw": "shoeshines", "pos": "noun", "ipa": "/ˈʃuːʃaɪnz/", "vi": "dịch vụ đánh xi làm bóng đôi giày"},
  {"id": "lex.en.200k.062116", "hw": "showerheads", "pos": "noun", "ipa": "/ˈʃaʊərhɛdz/", "vi": "đầu bát vòi hoa sen phòng tắm"},
  {"id": "lex.en.200k.062117", "hw": "silvans", "pos": "noun", "ipa": "/ˈsɪlvənz/", "vi": "vị thần rừng cây cối cổ điển"},
  {"id": "lex.en.200k.062118", "hw": "skittered", "pos": "verb", "ipa": "/ˈskɪtərd/", "vi": "đã chạy lướt nhanh thoăn thoắt"},
  {"id": "lex.en.200k.062119", "hw": "skittering", "pos": "verb", "ipa": "/ˈskɪtərɪŋ/", "vi": "đang lướt chạy nhanh thoăn thoắt"},
  {"id": "lex.en.200k.062120", "hw": "skitters", "pos": "verb", "ipa": "/ˈskɪtərz/", "vi": "chạy lướt nhanh nhẹn thoăn thoắt"},
  {"id": "lex.en.200k.062121", "hw": "sprits", "pos": "noun", "ipa": "/sprɪts/", "vi": "thanh sào căng chéo buồm thuyền"},
  {"id": "lex.en.200k.062122", "hw": "stovepipes", "pos": "noun", "ipa": "/ˈstoʊvpaɪps/", "vi": "ống dẫn khói lò sưởi; mũ chóp cao"},
  {"id": "lex.en.200k.062123", "hw": "swallowtails", "pos": "noun", "ipa": "/ˈswɑːloʊteɪlz/", "vi": "bướm phượng đuôi én; áo đuôi tôm"},
  {"id": "lex.en.200k.062124", "hw": "tendrils", "pos": "noun", "ipa": "/ˈtɛndrəlz/", "vi": "tua cuốn dây leo; lọn tóc xoăn nhỏ"},
  {"id": "lex.en.200k.062125", "hw": "tepees", "pos": "noun", "ipa": "/ˈtiːpiz/", "vi": "lều chóp nón bằng da thổ dân Mỹ"},
  {"id": "lex.en.200k.062126", "hw": "theodicies", "pos": "noun", "ipa": "/θiˈɑːdəsiz/", "vi": "thần chính luận lý giải cái ác"},
  {"id": "lex.en.200k.062127", "hw": "theoreticians", "pos": "noun", "ipa": "/ˌθiːərəˈtɪʃənz/", "vi": "nhà lý thuyết học chuyên lý luận"},
  {"id": "lex.en.200k.062128", "hw": "tinderboxes", "pos": "noun", "ipa": "/ˈtɪndərbɑːksɪz/", "vi": "hộp bùi nhùi đánh lửa; ngòi nổ căng"},
  {"id": "lex.en.200k.062129", "hw": "tobacconists", "pos": "noun", "ipa": "/təˈbækənɪsts/", "vi": "chủ tiệm bán thuốc lá và tẩu thuốc"},
  {"id": "lex.en.200k.062130", "hw": "toxicologists", "pos": "noun", "ipa": "/ˌtɑːksɪˈkɑːlədʒɪsts/", "vi": "chuyên gia độc chất học chất độc"},
  {"id": "lex.en.200k.062131", "hw": "tussocks", "pos": "noun", "ipa": "/ˈtʌsəks/", "vi": "khóm cỏ mọc dày; búi lông hoặc tóc"},
  {"id": "lex.en.200k.062132", "hw": "undines", "pos": "noun", "ipa": "/ʌnˈdiːnz/", "vi": "nữ thủy thần nước trong thần thoại"},
  {"id": "lex.en.200k.062133", "hw": "uygurs", "pos": "noun", "ipa": "/ˈwiːɡərz/", "vi": "người Duy Ngô Nhĩ ở vùng Tân Cương"},
  {"id": "lex.en.200k.062134", "hw": "vignas", "pos": "noun", "ipa": "/ˈvɪɡnəz/", "vi": "chi cây họ đậu nhiệt đới Vigna"},
  {"id": "lex.en.200k.062135", "hw": "vintners", "pos": "noun", "ipa": "/ˈvɪntnərz/", "vi": "người nấu ủ và buôn bán rượu vang"},
  {"id": "lex.en.200k.062136", "hw": "wormier", "pos": "adj", "ipa": "/ˈwɜːrmiər/", "vi": "nhiều sâu bọ đục khoét hư hại hơn"},
  {"id": "lex.en.200k.062137", "hw": "wormiest", "pos": "adj", "ipa": "/ˈwɜːrmiɪst/", "vi": "bị sâu bọ giòi đục ăn nhiều nhất"},
  {"id": "lex.en.200k.062138", "hw": "wurlitzers", "pos": "noun", "ipa": "/ˈwɜːrlɪtsərz/", "vi": "đàn organ rạp chiếu bóng Wurlitzer"},
  {"id": "lex.en.200k.062139", "hw": "xtcs", "pos": "noun", "ipa": "/ɛks tiː siz/", "vi": "thuốc lắc ma túy tổng hợp ecstasy"},
  {"id": "lex.en.200k.062140", "hw": "aleksandr scriabin", "pos": "phrase", "ipa": "/ˌælɪɡˈzɑːndər skriˈɑːbɪn/", "vi": "nhà soạn nhạc Nga Scriabin"},
  {"id": "lex.en.200k.062141", "hw": "allemande sauce", "pos": "phrase", "ipa": "/ˌæləˈmænd sɔːs/", "vi": "sốt trắng kem trứng chanh kiểu Pháp"},
  {"id": "lex.en.200k.062142", "hw": "araucaria family", "pos": "phrase", "ipa": "/ˌærəˈkɛəriə ˈfæməli/", "vi": "họ thực vật cây bách tán Araucaria"},
  {"id": "lex.en.200k.062143", "hw": "artemisia campestris", "pos": "phrase", "ipa": "/ˌɑːrtɪˈmiːʒə kæmˈpɛstrɪs/", "vi": "cây ngải đồng thân thảo vùng ôn đới"},
  {"id": "lex.en.200k.062144", "hw": "auf wiedersehen", "pos": "phrase", "ipa": "/aʊf ˈviːdərzeɪən/", "vi": "lời chào tạm biệt hẹn gặp (Đức)"},
  {"id": "lex.en.200k.062145", "hw": "august von wassermann", "pos": "phrase", "ipa": "/ˈaʊɡʊst fɔːn ˈvɑːsərmɑːn/", "vi": "bác sĩ vi khuẩn học Đức Wassermann"},
  {"id": "lex.en.200k.062146", "hw": "blinking chickweed", "pos": "phrase", "ipa": "/ˈblɪŋkɪŋ ˈtʃɪkwiːd/", "vi": "cây cỏ suối mọc ẩm ướt bờ khe"},
  {"id": "lex.en.200k.062147", "hw": "bryan donkin", "pos": "phrase", "ipa": "/ˈbraɪən ˈdɑːŋkɪn/", "vi": "kỹ sư chế tạo Anh Bryan Donkin"},
  {"id": "lex.en.200k.062148", "hw": "bulgur pilaf", "pos": "phrase", "ipa": "/ˈbʊlɡər pɪˈlɑːf/", "vi": "món cơm lúa mì nghiền bulgur pilaf"},
  {"id": "lex.en.200k.062149", "hw": "california redbud", "pos": "phrase", "ipa": "/ˌkælɪˈfɔːrnjə ˈrɛdbʌd/", "vi": "cây ban hoa đỏ hồng rực California"},
  {"id": "lex.en.200k.062150", "hw": "carl orff", "pos": "phrase", "ipa": "/kɑːrl ɔːrf/", "vi": "nhà soạn nhạc Đức Carl Orff"},
  {"id": "lex.en.200k.062151", "hw": "cidade de praia", "pos": "phrase", "ipa": "/siˈdɑːdʒi də ˈpraɪə/", "vi": "thủ đô Praia cộng hòa Cabo Verde"},
  {"id": "lex.en.200k.062152", "hw": "common mugwort", "pos": "phrase", "ipa": "/ˈkɑːmən ˈmʌɡwɜːrt/", "vi": "cây ngải cứu thường lá thơm vị đắng"},
  {"id": "lex.en.200k.062153", "hw": "count maurice maeterlinck", "pos": "phrase", "ipa": "/kaʊnt mɔːˈriːs ˈmeɪtərlɪŋk/", "vi": "bá tước văn hào Bỉ Maeterlinck"},
  {"id": "lex.en.200k.062154", "hw": "cyclopean masonry", "pos": "phrase", "ipa": "/ˌsaɪkləˈpiːən ˈmeɪsənri/", "vi": "tường xây ghép đá tảng lớn cổ đại"},
  {"id": "lex.en.200k.062155", "hw": "dies irae", "pos": "phrase", "ipa": "/ˈdiːeɪz ˈɪreɪ/", "vi": "thánh ca cầu hồn Ngày Phán Xét"},
  {"id": "lex.en.200k.062156", "hw": "dithered color", "pos": "phrase", "ipa": "/ˈdɪðərd ˈkʌlər/", "vi": "màu pha trộn bằng điểm ảnh xen kẽ"},
  {"id": "lex.en.200k.062157", "hw": "dithered colour", "pos": "phrase", "ipa": "/ˈdɪðərd ˈkʌlər/", "vi": "màu sắc mô phỏng bằng hạt điểm ảnh"},
  {"id": "lex.en.200k.062158", "hw": "ephedra sinica", "pos": "phrase", "ipa": "/ɪˈfɛdrə ˈsɪnɪkə/", "vi": "cây thảo ma hoàng làm thuốc Đông y"},
  {"id": "lex.en.200k.062159", "hw": "genus amaranthus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌæməˈrænθəs/", "vi": "chi thực vật rau dền họ Dền"},
  {"id": "lex.en.200k.062160", "hw": "genus anser", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈænsər/", "vi": "chi chim ngỗng xám cổ dài Anser"},
  {"id": "lex.en.200k.062161", "hw": "genus araucaria", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌærəˈkɛəriə/", "vi": "chi cây bách tán tùng cổ Araucaria"},
  {"id": "lex.en.200k.062162", "hw": "genus chimaera", "pos": "phrase", "ipa": "/ˈdʒiːnəs kaɪˈmɪərə/", "vi": "chi cá mập ma biển sâu Chimaera"},
  {"id": "lex.en.200k.062163", "hw": "genus nepeta", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈnɛpɪtə/", "vi": "chi cây bạc hà mèo họ Hoa môi"},
  {"id": "lex.en.200k.062164", "hw": "genus paramecium", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌpærəˈmiːʃiəm/", "vi": "chi trùng đế giày đơn bào nước ngọt"},
  {"id": "lex.en.200k.062165", "hw": "genus pelargonium", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌpɛlɑːrˈɡoʊniəm/", "vi": "chi hoa phong lữ thảo lá thơm"},
  {"id": "lex.en.200k.062166", "hw": "george szell", "pos": "phrase", "ipa": "/dʒɔːrdʒ sɛl/", "vi": "nhạc trưởng chỉ huy George Szell"},
  {"id": "lex.en.200k.062167", "hw": "glottis vera", "pos": "phrase", "ipa": "/ˈɡlɑːtɪs ˈvɪərə/", "vi": "thanh môn thật tạo âm giọng nói"},
  {"id": "lex.en.200k.062168", "hw": "gustav theodor fechner", "pos": "phrase", "ipa": "/ˈɡʊstɑːf ˈteɪədɔːr ˈfɛknər/", "vi": "nhà tâm lý học Đức Gustav Fechner"},
  {"id": "lex.en.200k.062169", "hw": "hawksbill turtle", "pos": "phrase", "ipa": "/ˈhɔːksbɪl ˈtɜːrtl/", "vi": "loài rùa biển đồi mồi quý hiếm"},
  {"id": "lex.en.200k.062170", "hw": "honoris causa", "pos": "phrase", "ipa": "/əˈnɔːrɪs ˈkɔːzə/", "vi": "học vị tiến sĩ danh dự trao tặng"},
  {"id": "lex.en.200k.062171", "hw": "horsetail milkweed", "pos": "phrase", "ipa": "/ˈhɔːrsteɪl ˈmɪlkwiːd/", "vi": "cây bông tai lá kim giống đuôi ngựa"},
  {"id": "lex.en.200k.062172", "hw": "in apposition", "pos": "phrase", "ipa": "/ɪn ˌæpəˈzɪʃən/", "vi": "nằm ở chức năng đồng vị ngữ câu"},
  {"id": "lex.en.200k.062173", "hw": "jus sanguinis", "pos": "phrase", "ipa": "/dʒʌs ˈsæŋɡwɪnɪs/", "vi": "luật quốc tịch dựa theo huyết thống"},
  {"id": "lex.en.200k.062174", "hw": "konstantin stanislavsky", "pos": "phrase", "ipa": "/ˈkɑːnstəntiːn ˌstænəˈslɑːfski/", "vi": "đạo diễn diễn xuất Nga Stanislavsky"},
  {"id": "lex.en.200k.062175", "hw": "lammas day", "pos": "phrase", "ipa": "/ˈlæməs deɪ/", "vi": "lễ tạ ơn mùa lúa mì đầu tháng Tám"},
  {"id": "lex.en.200k.062176", "hw": "lanius borealis", "pos": "phrase", "ipa": "/ˈleɪniəs ˌbɔːriˈeɪlɪs/", "vi": "chim bách thanh phương bắc ăn thịt"},
  {"id": "lex.en.200k.062177", "hw": "lichen planus", "pos": "phrase", "ipa": "/ˈlaɪkən ˈpleɪnəs/", "vi": "bệnh da liễu viêm sẩn liken phẳng"},
  {"id": "lex.en.200k.062178", "hw": "liposomal delivery vector", "pos": "phrase", "ipa": "/ˌlɪpəˈsoʊml dɪˈlɪvəri ˈvɛktər/", "vi": "chất mang thuốc bọc màng liposome"},
  {"id": "lex.en.200k.062179", "hw": "murrumbidgee river", "pos": "phrase", "ipa": "/ˌmʌrəmˈbɪdʒi ˈrɪvər/", "vi": "dòng sông lớn Murrumbidgee nước Úc"},
  {"id": "lex.en.200k.062180", "hw": "musculus sartorius", "pos": "phrase", "ipa": "/ˈmʌskjʊləs sɑːrˈtɔːriəs/", "vi": "cơ may cơ dài nhất dọc đùi người"},
  {"id": "lex.en.200k.062181", "hw": "nelson algren", "pos": "phrase", "ipa": "/ˈnɛlsən ˈɔːlɡrən/", "vi": "nhà văn hiện thực Mỹ Nelson Algren"},
  {"id": "lex.en.200k.062182", "hw": "oryza sativa", "pos": "phrase", "ipa": "/əˈraɪzə səˈtaɪvə/", "vi": "cây lúa nước trồng trọt châu Á"},
  {"id": "lex.en.200k.062183", "hw": "palatine raphe", "pos": "phrase", "ipa": "/ˈpælətaɪn ˈreɪfi/", "vi": "đường gờ giữa vòm khẩu cái miệng"},
  {"id": "lex.en.200k.062184", "hw": "passer domesticus", "pos": "phrase", "ipa": "/ˈpæsər dəˈmɛstɪkəs/", "vi": "loài chim sẻ nhà phổ biến thành thị"},
  {"id": "lex.en.200k.062185", "hw": "piddle away", "pos": "phrase", "ipa": "/ˈpɪdl əˈweɪ/", "vi": "tiêu phí thời gian tiền bạc vô bổ"},
  {"id": "lex.en.200k.062186", "hw": "pigeon guillemot", "pos": "phrase", "ipa": "/ˈpɪdʒən ˈɡɪlɪmɑːt/", "vi": "chim biển guillemot đen chân đỏ son"},
  {"id": "lex.en.200k.062187", "hw": "polynesian tattler", "pos": "phrase", "ipa": "/ˌpɑːlɪˈniːʒən ˈtætlər/", "vi": "chim choắt xám di cư Polynesia"},
  {"id": "lex.en.200k.062188", "hw": "polysyllabic word", "pos": "phrase", "ipa": "/ˌpɑːlisɪˈlæbɪk wɜːrd/", "vi": "từ đa âm tiết có nhiều âm tiết"},
  {"id": "lex.en.200k.062189", "hw": "pyloric valve", "pos": "phrase", "ipa": "/paɪˈlɔːrɪk vælv/", "vi": "cơ thắt van môn vị đáy dạ dày"},
  {"id": "lex.en.200k.062190", "hw": "pyloric vein", "pos": "phrase", "ipa": "/paɪˈlɔːrɪk veɪn/", "vi": "tĩnh mạch môn vị dẫn máu dạ dày"},
  {"id": "lex.en.200k.062191", "hw": "quartic polynomial", "pos": "phrase", "ipa": "/ˈkwɔːrtɪk ˌpɑːlɪˈnoʊmiəl/", "vi": "biểu thức đa thức đại số bậc bốn"},
  {"id": "lex.en.200k.062192", "hw": "rein orchis", "pos": "phrase", "ipa": "/reɪn ˈɔːrkɪs/", "vi": "cây hoa phong lan môi hình quả thận"},
  {"id": "lex.en.200k.062193", "hw": "rhodesian ridgeback", "pos": "phrase", "ipa": "/roʊˈdiːʒən ˈrɪdʒbæk/", "vi": "chó săn sư tử bờm lưng Nam Phi"},
  {"id": "lex.en.200k.062194", "hw": "road mender", "pos": "phrase", "ipa": "/roʊd ˈmɛndər/", "vi": "công nhân sửa chữa vá đường sá"},
  {"id": "lex.en.200k.062195", "hw": "robert ranke graves", "pos": "phrase", "ipa": "/ˈrɑːbərt ˈræŋkə ɡreɪvz/", "vi": "thi sĩ nhà văn Anh Robert Graves"},
  {"id": "lex.en.200k.062196", "hw": "rubus occidentalis", "pos": "phrase", "ipa": "/ˈruːbəs ˌɑːksɪdɛnˈteɪlɪs/", "vi": "cây mâm xôi quả đen mọng Bắc Mỹ"},
  {"id": "lex.en.200k.062197", "hw": "sadi carnot", "pos": "phrase", "ipa": "/səˈdi kɑːrˈnoʊ/", "vi": "nhà vật lý nhiệt học Sadi Carnot"},
  {"id": "lex.en.200k.062198", "hw": "salix arctica", "pos": "phrase", "ipa": "/ˈseɪlɪks ˈɑːrktɪkə/", "vi": "cây liễu lùn bò sát vùng Bắc Cực"},
  {"id": "lex.en.200k.062199", "hw": "slaked lime", "pos": "phrase", "ipa": "/sleɪkt laɪm/", "vi": "vôi tôi canxi hydroxit xây dựng"},
  {"id": "lex.en.200k.062200", "hw": "sodium thiosulfate", "pos": "phrase", "ipa": "/ˈsoʊdiəm ˌθaɪoʊˈsʌlfeɪt/", "vi": "hóa chất giải độc natri thiosunfat"},
  {"id": "lex.en.200k.062201", "hw": "strawberry hemangioma", "pos": "phrase", "ipa": "/ˈstrɔːbɛri hɪˌmændʒiˈoʊmə/", "vi": "u máu đỏ hình quả dâu tây ở trẻ em"},
  {"id": "lex.en.200k.062202", "hw": "terre adelie", "pos": "phrase", "ipa": "/tɛər ˈɑːdəli/", "vi": "vùng đất Adélie thuộc châu Nam Cực"}
]

with open('scratch/b33_r05_raw_p2.json') as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"Mismatch id at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"Mismatch hw at {i}: {item['hw']} vs {r['hw']}"
    assert len(item['vi']) <= 35, f"vi length > 35 at {i} ({item['hw']}): {len(item['vi'])}"
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {item['pos']}"
    if ' ' not in item['hw']:
        assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Invalid ipa at {i}: {item['ipa']}"
    r['pos'] = item['pos']
    r['ipa'] = item['ipa']
    r['vi'] = item['vi']
    r['status'] = 'reviewed'

with open('scratch/b33_r05_p2.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 5 Part 2 validated and written successfully.")
