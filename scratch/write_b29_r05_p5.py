import json
import re

items = [
    {"id": "lex.en.200k.042402", "hw": "acadia national park", "pos": "phrase", "ipa": "", "vi": "vườn quốc gia Acadia nước Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042403", "hw": "acetyl group", "pos": "phrase", "ipa": "", "vi": "nhóm chức acetyl hóa học", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042404", "hw": "addis ababa", "pos": "phrase", "ipa": "", "vi": "thủ đô Addis Ababa Ethiopia", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042405", "hw": "amphibian family", "pos": "phrase", "ipa": "", "vi": "họ động vật lưỡng cư", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042406", "hw": "autonomic nervous system", "pos": "phrase", "ipa": "", "vi": "hệ thần kinh tự chủ thực vật", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042407", "hw": "baffle board", "pos": "phrase", "ipa": "", "vi": "tấm cản âm; tấm hướng dòng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042408", "hw": "balm of gilead", "pos": "phrase", "ipa": "", "vi": "dầu thơm Gilead; cây balsam", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042409", "hw": "bas mitzvah", "pos": "phrase", "ipa": "", "vi": "lễ trưởng thành nữ Bat Mitzvah", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042410", "hw": "bel esprit", "pos": "phrase", "ipa": "", "vi": "người tài hoa thông thái", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042411", "hw": "ben gurion", "pos": "phrase", "ipa": "", "vi": "thủ tướng David Ben-Gurion", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042412", "hw": "bermuda buttercup", "pos": "phrase", "ipa": "", "vi": "hoa me chua đất hoa vàng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042413", "hw": "biting midge", "pos": "phrase", "ipa": "", "vi": "con bọ mát cắn; dãn cát", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042414", "hw": "cairn terrier", "pos": "phrase", "ipa": "", "vi": "chó sục Cairn Scotland", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042415", "hw": "cantilever bridge", "pos": "phrase", "ipa": "", "vi": "cầu công xôn; cầu đòn hẫng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042416", "hw": "cape hyacinth", "pos": "phrase", "ipa": "", "vi": "cây hoa dạ lan hương Mũi Hảo Vọng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042417", "hw": "captain bligh", "pos": "phrase", "ipa": "", "vi": "thuyền trưởng William Bligh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042418", "hw": "cobble together", "pos": "phrase", "ipa": "", "vi": "chắp vá vội vàng; ghép lại", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042419", "hw": "cobble up", "pos": "phrase", "ipa": "", "vi": "chắp vá tạm thời; làm ẩu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042420", "hw": "coco de macao", "pos": "phrase", "ipa": "", "vi": "cây cọ dừa Macao", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042421", "hw": "common scurvy grass", "pos": "phrase", "ipa": "", "vi": "rau thìa trị bệnh scorbut", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042422", "hw": "cordon bleu", "pos": "phrase", "ipa": "", "vi": "đầu bếp danh tiếng bậc thầy", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042423", "hw": "corneal graft", "pos": "phrase", "ipa": "", "vi": "phẫu thuật ghép mảnh giác mạc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042424", "hw": "creeping buttercup", "pos": "phrase", "ipa": "", "vi": "cây mao lương bò lan", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042425", "hw": "crepe fern", "pos": "phrase", "ipa": "", "vi": "loài dương xỉ lá crepe", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042426", "hw": "donald glaser", "pos": "phrase", "ipa": "", "vi": "nhà vật lý Donald A. Glaser", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042427", "hw": "dormer window", "pos": "phrase", "ipa": "", "vi": "cửa sổ mái nhà nhô ra", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042428", "hw": "duffel coat", "pos": "phrase", "ipa": "", "vi": "áo khoác dạ duffel cài khuy gỗ", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042429", "hw": "edmund kean", "pos": "phrase", "ipa": "", "vi": "diễn viên kịch Edmund Kean", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042430", "hw": "emile zola", "pos": "phrase", "ipa": "", "vi": "đại văn hào Émile Zola", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042431", "hw": "estradiol patch", "pos": "phrase", "ipa": "", "vi": "miếng dán hormone estradiol", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042432", "hw": "false pretence", "pos": "phrase", "ipa": "", "vi": "hành vi giả mạo lừa đảo", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042433", "hw": "fleshed out", "pos": "phrase", "ipa": "", "vi": "được phát triển đầy đủ chi tiết", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042434", "hw": "genus hibiscus", "pos": "phrase", "ipa": "", "vi": "chi râm bụt; chi dâm bụt", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042435", "hw": "glandular disorder", "pos": "phrase", "ipa": "", "vi": "chứng rối loạn tuyến nội tiết", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042436", "hw": "glandular fever", "pos": "phrase", "ipa": "", "vi": "bệnh sốt tăng bạch cầu đơn nhân", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042437", "hw": "globe artichoke", "pos": "phrase", "ipa": "", "vi": "cây hoa atisô búp tròn", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042438", "hw": "gopher tortoise", "pos": "phrase", "ipa": "", "vi": "loài rùa đào hang gopher", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042439", "hw": "henry of navarre", "pos": "phrase", "ipa": "", "vi": "Vua Henri IV của Pháp", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042440", "hw": "heuristic program", "pos": "phrase", "ipa": "", "vi": "chương trình thuật toán heuristic", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042441", "hw": "heuristic rule", "pos": "phrase", "ipa": "", "vi": "quy tắc kinh nghiệm heuristic", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042442", "hw": "honey mesquite", "pos": "phrase", "ipa": "", "vi": "cây gai mật mesquite", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042443", "hw": "huckleberry oak", "pos": "phrase", "ipa": "", "vi": "loài cây sồi lùn huckleberry", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042444", "hw": "hydroxy acid", "pos": "phrase", "ipa": "", "vi": "axit hydroxy hữu cơ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042445", "hw": "indira nehru gandhi", "pos": "phrase", "ipa": "", "vi": "nữ thủ tướng Indira Gandhi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042446", "hw": "invert soap", "pos": "phrase", "ipa": "", "vi": "xà phòng cation nghịch đảo", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042447", "hw": "jerusalem artichoke", "pos": "phrase", "ipa": "", "vi": "củ cúc vu; atisô Jerusalem", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042448", "hw": "johannes brahms", "pos": "phrase", "ipa": "", "vi": "nhà soạn nhạc Johannes Brahms", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042449", "hw": "john trumbull", "pos": "phrase", "ipa": "", "vi": "họa sĩ John Trumbull", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042450", "hw": "leaf scorch", "pos": "phrase", "ipa": "", "vi": "bệnh cháy rìa lá cây", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042451", "hw": "legal ouster", "pos": "phrase", "ipa": "", "vi": "sự trục xuất hợp pháp đất đai", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042452", "hw": "limestone salamander", "pos": "phrase", "ipa": "", "vi": "kỳ giông sống trên núi đá vôi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042453", "hw": "marsh marigold", "pos": "phrase", "ipa": "", "vi": "hoa cúc đầm lầy vàng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042454", "hw": "meadow clary", "pos": "phrase", "ipa": "", "vi": "cây xô thơm đồng cỏ dại", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042455", "hw": "moveable feast", "pos": "phrase", "ipa": "", "vi": "ngày lễ tôn giáo di động", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042456", "hw": "mucous membrane", "pos": "phrase", "ipa": "", "vi": "lớp màng niêm mạc; màng nhầy", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042457", "hw": "nuttall oak", "pos": "phrase", "ipa": "", "vi": "cây sồi đỏ Nuttall", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042458", "hw": "of unsound mind", "pos": "phrase", "ipa": "", "vi": "mất trí; tâm thần không ổn định", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042459", "hw": "ozark mountains", "pos": "phrase", "ipa": "", "vi": "dãy núi Ozark miền nam nước Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042460", "hw": "palmetto state", "pos": "phrase", "ipa": "", "vi": "tiểu bang Nam Carolina", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042461", "hw": "panamanian monetary unit", "pos": "phrase", "ipa": "", "vi": "đơn vị tiền tệ Panama", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042462", "hw": "parasitic jaeger", "pos": "phrase", "ipa": "", "vi": "chim cướp biển ký sinh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042463", "hw": "parietal cortex", "pos": "phrase", "ipa": "", "vi": "vùng vỏ não đỉnh não bộ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042464", "hw": "phonograph needle", "pos": "phrase", "ipa": "", "vi": "đầu kim máy hát đĩa than", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042465", "hw": "phonological system", "pos": "phrase", "ipa": "", "vi": "hệ thống ngữ âm học", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042466", "hw": "polyurethane foam", "pos": "phrase", "ipa": "", "vi": "mút xốp bọt polyurethane", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042467", "hw": "pontoon bridge", "pos": "phrase", "ipa": "", "vi": "cây cầu phao dã chiến nổi", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042468", "hw": "pontoon plane", "pos": "phrase", "ipa": "", "vi": "thủy phi cơ hạ cánh phao nổi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042469", "hw": "port vila", "pos": "phrase", "ipa": "", "vi": "thủ đô Port Vila Vanuatu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042470", "hw": "prairie gourd vine", "pos": "phrase", "ipa": "", "vi": "dây leo cây bầu dại đồng cỏ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042471", "hw": "pretrial conference", "pos": "phrase", "ipa": "", "vi": "phiên họp hòa giải trước xử án", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042472", "hw": "pulmonary stenosis", "pos": "phrase", "ipa": "", "vi": "chứng hẹp van động mạch phổi", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042473", "hw": "pyramidal tent", "pos": "phrase", "ipa": "", "vi": "lều cắm trại hình chóp tháp", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042474", "hw": "rattlesnake fern", "pos": "phrase", "ipa": "", "vi": "dương xỉ chùm hoa đuôi rắn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042475", "hw": "red campion", "pos": "phrase", "ipa": "", "vi": "hoa cẩm chướng rừng đỏ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042476", "hw": "revolutionary proletarian nucleus", "pos": "phrase", "ipa": "", "vi": "nhóm hạt nhân vô sản cách mạng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042477", "hw": "rice weevil", "pos": "phrase", "ipa": "", "vi": "con mọt gạo cắn hạt thóc", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042478", "hw": "richard lovelace", "pos": "phrase", "ipa": "", "vi": "nhà thơ Richard Lovelace", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042479", "hw": "robert herrick", "pos": "phrase", "ipa": "", "vi": "nhà thơ Robert Herrick", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042480", "hw": "roman hyacinth", "pos": "phrase", "ipa": "", "vi": "hoa dạ lan hương trắng La Mã", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042481", "hw": "rose campion", "pos": "phrase", "ipa": "", "vi": "hoa nhung gai cẩm chướng hồng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042482", "hw": "saw palmetto", "pos": "phrase", "ipa": "", "vi": "cây cọ lùn răng cưa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042483", "hw": "scurvy grass", "pos": "phrase", "ipa": "", "vi": "cây cỏ muỗng thìa Bắc Cực", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042484", "hw": "secretarial assistant", "pos": "phrase", "ipa": "", "vi": "trợ lý hành chính thư ký", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042485", "hw": "secretarial school", "pos": "phrase", "ipa": "", "vi": "trường đào tạo nghiệp vụ thư ký", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042486", "hw": "seed weevil", "pos": "phrase", "ipa": "", "vi": "loài bọ cánh cứng đục hạt mầm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042487", "hw": "sinn fein", "pos": "phrase", "ipa": "", "vi": "đảng phái chính trị Sinn Féin", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042488", "hw": "soya bean", "pos": "phrase", "ipa": "", "vi": "hạt đậu nành; hạt đỗ tương", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042489", "hw": "starved aster", "pos": "phrase", "ipa": "", "vi": "hoa cúc thạch thảo cánh nhỏ còi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042490", "hw": "stillborn infant", "pos": "phrase", "ipa": "", "vi": "thai nhi bị chết lưu lúc sinh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042491", "hw": "stock buyback", "pos": "phrase", "ipa": "", "vi": "hoạt động mua lại cổ phiếu quỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042492", "hw": "stratified sampling", "pos": "phrase", "ipa": "", "vi": "phương pháp chọn mẫu phân tầng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042493", "hw": "strep throat", "pos": "phrase", "ipa": "", "vi": "bệnh viêm họng do liên cầu khuẩn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042494", "hw": "systolic pressure", "pos": "phrase", "ipa": "", "vi": "chỉ số huyết áp tâm thu tối đa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042495", "hw": "the great unwashed", "pos": "phrase", "ipa": "", "vi": "tầng lớp bình dân cùng khổ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042496", "hw": "tightrope walking", "pos": "phrase", "ipa": "", "vi": "môn xiếc đi thăng bằng trên dây", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042497", "hw": "trade unionism", "pos": "phrase", "ipa": "", "vi": "phong trào công đoàn lao động", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042498", "hw": "transitive verb", "pos": "phrase", "ipa": "", "vi": "ngoại động từ trong ngữ pháp", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042499", "hw": "venn diagram", "pos": "phrase", "ipa": "", "vi": "biểu đồ tập hợp Venn", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042500", "hw": "volumetric analysis", "pos": "phrase", "ipa": "", "vi": "phương pháp chuẩn độ thể tích", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042501", "hw": "west nile encephalitis", "pos": "phrase", "ipa": "", "vi": "bệnh viêm não virus West Nile", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""}
]

with open('scratch/b29_r05_raw_p5.json') as f:
    raw = json.load(f)

assert len(items) == 100, f"Expected 100 items, got {len(items)}"
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}

for idx, (it, r) in enumerate(zip(items, raw)):
    assert it['id'] == r['id'], f"ID mismatch: {it['id']} vs {r['id']}"
    assert it['hw'] == r['hw'], f"HW mismatch: {it['hw']} vs {r['hw']}"
    assert it['pos'] in allowed_pos, f"Invalid POS {it['pos']} for {it['id']}"
    assert len(it['vi']) > 0, f"Empty VI for {it['id']}"
    assert len(it['vi']) <= 35, f"Invalid VI length ({len(it['vi'])}) for {it['id']}: {it['vi']}"
    if it['pos'] != 'phrase' and ' ' not in it['hw']:
        assert it['ipa'].startswith('/') and it['ipa'].endswith('/') and it['ipa'].count('/') == 2, f"Invalid IPA for {it['id']}: {it['ipa']}"

with open('scratch/b29_r05_p5.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"Batch 29 Round 5 Part 5 validated and written successfully. Total items: {len(items)}")
