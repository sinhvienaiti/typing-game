# -*- coding: utf-8 -*-
import json

part5_data = [
  {"id": "lex.en.200k.054902", "hw": "rends", "pos": "verb", "ipa": "/rɛndz/", "vi": "xé rách toạc; làm tan nát cõi lòng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054903", "hw": "rightists", "pos": "noun", "ipa": "/ˈraɪtɪsts/", "vi": "những người thuộc phe cánh hữu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054904", "hw": "searchers", "pos": "noun", "ipa": "/ˈsɜːrtʃərz/", "vi": "những người tìm kiếm tìm tòi", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054905", "hw": "shakeups", "pos": "noun", "ipa": "/ˈʃeɪkʌps/", "vi": "các đợt cải tổ nhân sự lớn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054906", "hw": "singeing", "pos": "verb", "ipa": "/ˈsɪndʒɪŋ/", "vi": "đang đốt xém mép; đang sém lửa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054907", "hw": "skateboarders", "pos": "noun", "ipa": "/ˈskeɪtbɔːrdərz/", "vi": "những người trượt ván đường phố", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054908", "hw": "smokehouses", "pos": "noun", "ipa": "/ˈsmoʊkhaʊzɪz/", "vi": "nhà hun khói thịt cá xúc xích", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054909", "hw": "soundproofed", "pos": "verb", "ipa": "/ˈsaʊndpruːft/", "vi": "đã bọc cách âm; đã chống ồn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054910", "hw": "soundproofing", "pos": "verb", "ipa": "/ˈsaʊndpruːfɪŋ/", "vi": "đang cách âm; biện pháp cách âm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054911", "hw": "soundproofs", "pos": "verb", "ipa": "/ˈsaʊndpruːfs/", "vi": "cách âm; chống ồn cho căn phòng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054912", "hw": "spacewalked", "pos": "verb", "ipa": "/ˈspeɪswɔːkt/", "vi": "đã bước ra ngoài vũ trụ đi bộ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054913", "hw": "spacewalks", "pos": "verb", "ipa": "/ˈspeɪswɔːks/", "vi": "đi bộ ngoài khoảng không vũ trụ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054914", "hw": "spays", "pos": "verb", "ipa": "/speɪz/", "vi": "cắt buồng trứng; triệt sản chó mèo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054915", "hw": "sprigging", "pos": "noun", "ipa": "/ˈsprɪɡɪŋ/", "vi": "phương pháp giâm cành nhánh cỏ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054916", "hw": "sprigs", "pos": "noun", "ipa": "/sprɪɡz/", "vi": "những nhánh con; cành hoa nhỏ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054917", "hw": "steubens", "pos": "noun", "ipa": "/ˈstjuːbənz/", "vi": "tướng quân Baron von Steuben", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054918", "hw": "supremos", "pos": "noun", "ipa": "/suːˈpriːmoʊz/", "vi": "những thủ lĩnh quyền lực tối cao", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054919", "hw": "tarrier", "pos": "adj", "ipa": "/ˈtɑːriər/", "vi": "dính bết hắc ín hơn; đen nhẻm hơn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054920", "hw": "tarriest", "pos": "adj", "ipa": "/ˈtɑːriɪst/", "vi": "dính bết hắc ín nhất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054921", "hw": "tartaruses", "pos": "noun", "ipa": "/ˈtɑːrtərəsɪz/", "vi": "vực thẳm Tartarus dưới âm phủ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054922", "hw": "transgendereds", "pos": "noun", "ipa": "/trænzˈdʒɛndərdz/", "vi": "những người chuyển giới tính", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054923", "hw": "transliterations", "pos": "noun", "ipa": "/trænzˌlɪtəˈreɪʃənz/", "vi": "sự chuyển tự từ bảng chữ cái này", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054924", "hw": "trilaterals", "pos": "noun", "ipa": "/traɪˈlætərəlz/", "vi": "các hình tam giác có ba cạnh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054925", "hw": "tyndales", "pos": "noun", "ipa": "/ˈtɪndeɪlz/", "vi": "học giả William Tyndale nước Anh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054926", "hw": "undertows", "pos": "noun", "ipa": "/ˈʌndərtoʊz/", "vi": "các luồng sóng ngầm cuốn ra xa", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054927", "hw": "weaklings", "pos": "noun", "ipa": "/ˈwiːklɪŋz/", "vi": "những kẻ yếu đuối ươn hèn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054928", "hw": "windpipes", "pos": "noun", "ipa": "/ˈwɪndpaɪps/", "vi": "các ống khí quản dẫn khí", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054929", "hw": "yarders", "pos": "noun", "ipa": "/ˈjɑːrdərz/", "vi": "máy tời cáp gom gỗ rừng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054930", "hw": "yurts", "pos": "noun", "ipa": "/jɜːrts/", "vi": "lều tròn yurt của dân du mục", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054931", "hw": "zweigs", "pos": "noun", "ipa": "/zwaɪɡz/", "vi": "văn hào Áo Stefan Zweig", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054932", "hw": "alfred stieglitz", "pos": "phrase", "ipa": "/ˈælfrɪd ˈstiːɡlɪts/", "vi": "nhiếp ảnh gia Mỹ Alfred Stieglitz", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054933", "hw": "antigenic determinant", "pos": "phrase", "ipa": "/ˌæntɪˈdʒɛnɪk dɪˈtɜːrmɪnənt/", "vi": "quyết định kháng nguyên; epitope", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054934", "hw": "arnica bud", "pos": "phrase", "ipa": "/ˈɑːrnɪkə bʌd/", "vi": "búp hoa cúc arnica làm thuốc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054935", "hw": "arnica montana", "pos": "phrase", "ipa": "/ˈɑːrnɪkə mɑːnˈtænə/", "vi": "cây cúc arnica montana trị bầm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054936", "hw": "artur schnabel", "pos": "phrase", "ipa": "/ˈɑːrtər ˈʃnɑːbəl/", "vi": "nghệ sĩ dương cầm Artur Schnabel", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054937", "hw": "begonia family", "pos": "phrase", "ipa": "/bɪˈɡoʊniə ˈfæmɪli/", "vi": "họ thực vật hoa Thu hải đường", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054938", "hw": "bela lugosi", "pos": "phrase", "ipa": "/ˈbeɪlə lʊˈɡoʊsi/", "vi": "diễn viên huyền thoại Bela Lugosi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054939", "hw": "black elderberry", "pos": "phrase", "ipa": "/blæk ˈɛldərbɛri/", "vi": "cây cơm cháy đen; quả cơm cháy đen", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054940", "hw": "blue elderberry", "pos": "phrase", "ipa": "/bluː ˈɛldərbɛri/", "vi": "cây cơm cháy quả lam Bắc Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054941", "hw": "book of zephaniah", "pos": "phrase", "ipa": "/bʊk əv ˌzɛfəˈnaɪə/", "vi": "sách Tiên tri Xô-phô-ni-a", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054942", "hw": "bristly locust", "pos": "phrase", "ipa": "/ˈbrɪstli ˈloʊkəst/", "vi": "cây dương hòe thân nhiều gai cứng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054943", "hw": "cactus euphorbia", "pos": "phrase", "ipa": "/ˈkæktəs juːˈfɔːrbiə/", "vi": "cây xương rồng đại kích châu Phi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054944", "hw": "cell organelle", "pos": "phrase", "ipa": "/sɛl ˌɔːrɡəˈnɛl/", "vi": "các bào quan bên trong tế bào", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054945", "hw": "christmas begonia", "pos": "phrase", "ipa": "/ˈkrɪsməs bɪˈɡoʊniə/", "vi": "cây thu hải đường hoa Giáng sinh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054946", "hw": "circumflex femoral vein", "pos": "phrase", "ipa": "/ˈsɜːrkəmflɛks ˈfɛmərəl veɪn/", "vi": "tĩnh mạch mũ đùi giải phẫu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054947", "hw": "clostridium botulinum", "pos": "phrase", "ipa": "/klɒˈstrɪdiəm ˌbɒtjʊˈlaɪnəm/", "vi": "vi khuẩn sinh độc tố botulinum", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054948", "hw": "cloven hoof", "pos": "phrase", "ipa": "/ˈkloʊvən huːf/", "vi": "móng chẻ đôi; móng guốc của quỷ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054949", "hw": "common burdock", "pos": "phrase", "ipa": "/ˈkɑːmən ˈbɜːrdɑːk/", "vi": "cây ngưu bàng thường mọc dại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054950", "hw": "cracker bonbon", "pos": "phrase", "ipa": "/ˈkrækər ˈbɑːnbɑːn/", "vi": "ống pháo giấy quà tặng Giáng sinh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054951", "hw": "deltoid leaf", "pos": "phrase", "ipa": "/ˈdɛltɔɪd liːf/", "vi": "phiến lá có hình tam giác", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054952", "hw": "deltoid muscle", "pos": "phrase", "ipa": "/ˈdɛltɔɪd ˈmʌsəl/", "vi": "cơ tam giác deltoid ở vùng vai", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054953", "hw": "edward pusey", "pos": "phrase", "ipa": "/ˈɛdwərd ˈpjuːzi/", "vi": "nhà thần học Anh Edward Pusey", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054954", "hw": "elderberry bush", "pos": "phrase", "ipa": "/ˈɛldərbɛri bʊʃ/", "vi": "bụi cây cơm cháy sinh quả mọng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054955", "hw": "field brome", "pos": "phrase", "ipa": "/fiːld broʊm/", "vi": "cỏ đồng ruộng chi cỏ đuôi sẻ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054956", "hw": "gastric lavage", "pos": "phrase", "ipa": "/ˈɡæstrɪk ləˈvɑːʒ/", "vi": "thủ thuật rửa dạ dày cấp cứu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054957", "hw": "gentian violet", "pos": "phrase", "ipa": "/ˈdʒɛnʃən ˈvaɪələt/", "vi": "thuốc sát trùng cồn tím gentian", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054958", "hw": "genus amaryllis", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌæməˈrɪlɪs/", "vi": "chi hoa Thủy tiên Nam Phi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054959", "hw": "genus apus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈeɪpəs/", "vi": "chi chim yến bay nhanh họ Yến", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054960", "hw": "genus arnica", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈɑːrnɪkə/", "vi": "chi cúc thảo dược Arnica", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054961", "hw": "genus echinacea", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌɛkɪˈneɪʃə/", "vi": "chi cúc tím cúc dại Echinacea", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054962", "hw": "genus giardia", "pos": "phrase", "ipa": "/ˈdʒiːnəs dʒiːˈɑːrdiə/", "vi": "chi trùng roi ký sinh đường ruột", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054963", "hw": "genus mirabilis", "pos": "phrase", "ipa": "/ˈdʒiːnəs mɪˈræbəlɪs/", "vi": "chi hoa phấn; chi cây bốn giờ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054964", "hw": "genus mycoplasma", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌmaɪkoʊˈplæzmə/", "vi": "chi vi khuẩn không vách Mycoplasma", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054965", "hw": "genus proconsul", "pos": "phrase", "ipa": "/ˈdʒiːnəs proʊˈkɑːnsəl/", "vi": "chi vượn người linh trưởng cổ đại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054966", "hw": "granulation tissue", "pos": "phrase", "ipa": "/ˌɡrænjʊˈleɪʃən ˈtɪʃuː/", "vi": "mô hạt đang lên sẹo vết thương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054967", "hw": "great burdock", "pos": "phrase", "ipa": "/ɡreɪt ˈbɜːrdɑːk/", "vi": "cây ngưu bàng lớn làm thảo dược", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054968", "hw": "great crested grebe", "pos": "phrase", "ipa": "/ɡreɪt ˈkrɛstɪd ɡriːb/", "vi": "loài chim lặn mào lớn bơi lặn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054969", "hw": "greater burdock", "pos": "phrase", "ipa": "/ˈɡreɪtər ˈbɜːrdɑːk/", "vi": "cây ngưu bàng lớn có rễ bổ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054970", "hw": "greater kudu", "pos": "phrase", "ipa": "/ˈɡreɪtər ˈkuːduː/", "vi": "loài linh dương Kudu sừng xoắn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054971", "hw": "guy de maupassant", "pos": "phrase", "ipa": "/ɡiː də ˌmoʊpəˈsɑ̃ː/", "vi": "văn hào Guy de Maupassant Pháp", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054972", "hw": "hebridean islands", "pos": "phrase", "ipa": "/hɛˈbrɪdiən ˈaɪləndz/", "vi": "quần đảo Hebrides ở Scotland", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054973", "hw": "henry villard", "pos": "phrase", "ipa": "/ˈhɛnri vɪˈlɑːrd/", "vi": "nhà báo tài phiệt Henry Villard", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054974", "hw": "highball glass", "pos": "phrase", "ipa": "/ˈhaɪbɔːl ɡlæs/", "vi": "cốc pha cocktail dáng cao Highball", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054975", "hw": "hop marjoram", "pos": "phrase", "ipa": "/hɑːp ˈmɑːrdʒərəm/", "vi": "cây kinh giới hoa bia thảo mộc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054976", "hw": "horsehair wig", "pos": "phrase", "ipa": "/ˈhɔːrsheər wɪɡ/", "vi": "bộ tóc giả bện từ lông đuôi ngựa", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054977", "hw": "hussar monkey", "pos": "phrase", "ipa": "/hʊˈzɑːr ˈmʌŋki/", "vi": "khỉ patas; khỉ quân kỵ hussar", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054978", "hw": "japanese brome", "pos": "phrase", "ipa": "/ˌdʒæpəˈniːz broʊm/", "vi": "loài cỏ đuôi sẻ cỏ brome Nhật Bản", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054979", "hw": "john lackland", "pos": "phrase", "ipa": "/dʒɑːn ˈlæklænd/", "vi": "Vua John nước Anh mất đất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054980", "hw": "king begonia", "pos": "phrase", "ipa": "/kɪŋ bɪˈɡoʊniə/", "vi": "thu hải đường vua lá vằn đẹp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054981", "hw": "lacrimal bone", "pos": "phrase", "ipa": "/ˈlækrɪməl boʊn/", "vi": "xương lệ nhỏ ở hốc mắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054982", "hw": "lath and plaster", "pos": "phrase", "ipa": "/læθ ænd ˈplæstər/", "vi": "vách nan gỗ trát vữa thạch cao", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054983", "hw": "lesser burdock", "pos": "phrase", "ipa": "/ˈlɛsər ˈbɜːrdɑːk/", "vi": "cây ngưu bàng nhỏ rễ làm thuốc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054984", "hw": "lesser kudu", "pos": "phrase", "ipa": "/ˈlɛsər ˈkuːduː/", "vi": "loài linh dương Kudu cỡ nhỏ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054985", "hw": "lotus americanus", "pos": "phrase", "ipa": "/ˈloʊtəs əˌmɛrɪˈkɑːnəs/", "vi": "cỏ cánh chim sen đất châu Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054986", "hw": "maksim gorky", "pos": "phrase", "ipa": "/mækˈsiːm ˈɡɔːrki/", "vi": "đại văn hào Nga Maksim Gorky", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054987", "hw": "marsh gentian", "pos": "phrase", "ipa": "/mɑːrʃ ˈdʒɛnʃən/", "vi": "cây hoa long đởm vùng đầm lầy", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054988", "hw": "menominee whitefish", "pos": "phrase", "ipa": "/məˈnɑːmɪniː ˈwaɪtfɪʃ/", "vi": "loài cá hồi trắng Menominee", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054989", "hw": "metacarpal artery", "pos": "phrase", "ipa": "/ˌmɛtəˈkɑːrpəl ˈɑːrtəri/", "vi": "động mạch gian đốt bàn tay", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054990", "hw": "metacarpal vein", "pos": "phrase", "ipa": "/ˌmɛtəˈkɑːrpəl veɪn/", "vi": "tĩnh mạch gian đốt bàn tay", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054991", "hw": "mohammed reza pahlavi", "pos": "phrase", "ipa": "/moʊˈhæməd ˈreɪzə pæhˈlɑːvi/", "vi": "vua Shah Reza Pahlavi của Iran", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054992", "hw": "monounsaturated fatty acid", "pos": "phrase", "ipa": "/ˌmɑːnoʊʌnˈsætʃəreɪtɪd ˈfæti ˈæsɪd/", "vi": "axit béo không no đơn nối đôi", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054993", "hw": "mountain paca", "pos": "phrase", "ipa": "/ˈmaʊntɪn ˈpɑːkə/", "vi": "loài gặm nhấm paca sống trên núi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054994", "hw": "north carolinian", "pos": "phrase", "ipa": "/nɔːrθ ˌkærəˈlɪniən/", "vi": "người bang Bắc Carolina nước Mỹ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054995", "hw": "octal number system", "pos": "phrase", "ipa": "/ˈɑːktəl ˈnʌmbər ˈsɪstəm/", "vi": "hệ thống số đếm bát phân cơ số 8", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054996", "hw": "oral poliovirus vaccine", "pos": "phrase", "ipa": "/ˈɔːrəl ˌpoʊlioʊˈvaɪrəs vækˈsiːn/", "vi": "vắc-xin ngừa bại liệt dạng uống", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054997", "hw": "oxtail soup", "pos": "phrase", "ipa": "/ˈɑːksteɪl suːp/", "vi": "món canh súp đuôi bò hầm ngọt", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054998", "hw": "paleocene epoch", "pos": "phrase", "ipa": "/ˈpeɪlioʊsiːn ˈɛpək/", "vi": "thế Cổ Tân trong đại Tân Sinh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054999", "hw": "pericardial cavity", "pos": "phrase", "ipa": "/ˌpɛrɪˈkɑːrdiəl ˈkævɪti/", "vi": "khoang màng ngoài tim dịch tim", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055000", "hw": "pericardial sac", "pos": "phrase", "ipa": "/ˌpɛrɪˈkɑːrdiəl sæk/", "vi": "túi màng bao bọc bên ngoài tim", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.055001", "hw": "pericardial vein", "pos": "phrase", "ipa": "/ˌpɛrɪˈkɑːrdiəl veɪn/", "vi": "tĩnh mạch màng ngoài tim giải phẫu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Validation
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

assert len(part5_data) == 100, f"Length is {len(part5_data)}"

with open('scratch/b31_r10_raw_p5.json') as f:
    raw = json.load(f)

for i, (item, raw_item) in enumerate(zip(part5_data, raw)):
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

with open('scratch/b31_r10_p5.json', 'w', encoding='utf-8') as f:
    json.dump(part5_data, f, ensure_ascii=False, indent=2)

print("Validated and saved 100 items for Part 5")
