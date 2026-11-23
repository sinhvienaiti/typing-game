import json

# Manual cognitive QA review for Batch 29 Round 1 Part 2 (IDs 040102 to 040201)
reviewed_items = [
    {"id": "lex.en.200k.040102", "hw": "davy crockett", "pos": "phrase", "ipa": "", "vi": "người hùng Davy Crockett", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040103", "hw": "de sade", "pos": "phrase", "ipa": "", "vi": "hầu tước De Sade", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040104", "hw": "dental amalgam", "pos": "phrase", "ipa": "", "vi": "hỗn hống nha khoa; amalgam", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040105", "hw": "dissociation constant", "pos": "phrase", "ipa": "", "vi": "hằng số điện ly; hằng số phân ly", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040106", "hw": "double dipper", "pos": "phrase", "ipa": "", "vi": "người ăn hai mang; nhận hai lương", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040107", "hw": "eared seal", "pos": "phrase", "ipa": "", "vi": "hải cẩu có vành tai", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040108", "hw": "eccles cake", "pos": "phrase", "ipa": "", "vi": "bánh ngọt Eccles", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040109", "hw": "elizabeth seton", "pos": "phrase", "ipa": "", "vi": "nữ thánh Elizabeth Seton", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040110", "hw": "erectile tissue", "pos": "phrase", "ipa": "", "vi": "mô cương cứng", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040111", "hw": "ernest bloch", "pos": "phrase", "ipa": "", "vi": "nhạc sĩ Ernest Bloch", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040112", "hw": "eurasian green toad", "pos": "phrase", "ipa": "", "vi": "cóc xanh lục Á-Âu", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040113", "hw": "european woolly thistle", "pos": "phrase", "ipa": "", "vi": "cây kế lông châu Âu", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040114", "hw": "fatah revolutionary council", "pos": "phrase", "ipa": "", "vi": "hội đồng cách mạng Fatah", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040115", "hw": "fixed intonation", "pos": "phrase", "ipa": "", "vi": "ngữ điệu cố định; cao độ chuẩn", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040116", "hw": "forlorn hope", "pos": "phrase", "ipa": "", "vi": "hy vọng mong manh; việc liều lĩnh", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040117", "hw": "fred sanger", "pos": "phrase", "ipa": "", "vi": "nhà hóa sinh Fred Sanger", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040118", "hw": "frederic william maitland", "pos": "phrase", "ipa": "", "vi": "sử gia Frederic Maitland", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040119", "hw": "gobble up", "pos": "phrase", "ipa": "", "vi": "ăn ngấu nghiến; thâu tóm nhanh", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040120", "hw": "gopher turtle", "pos": "phrase", "ipa": "", "vi": "rùa đất gopher", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040121", "hw": "great grandparent", "pos": "phrase", "ipa": "", "vi": "cụ cố; ông bà cố", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040122", "hw": "grenade thrower", "pos": "phrase", "ipa": "", "vi": "lính ném lựu đạn", "cefr": "C1", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040123", "hw": "habeas corpus", "pos": "phrase", "ipa": "", "vi": "lệnh đình quyền giam giữ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040124", "hw": "harpoon gun", "pos": "phrase", "ipa": "", "vi": "súng bắn lao móc; súng phóng lao", "cefr": "C1", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040125", "hw": "harpoon line", "pos": "phrase", "ipa": "", "vi": "dây nối lao móc săn cá", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040126", "hw": "honduran monetary unit", "pos": "phrase", "ipa": "", "vi": "đơn vị tiền tệ Honduras", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040127", "hw": "humphrey bogart", "pos": "phrase", "ipa": "", "vi": "diễn viên Humphrey Bogart", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040128", "hw": "indivisible by", "pos": "phrase", "ipa": "", "vi": "không chia hết cho", "cefr": "C1", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040129", "hw": "inhalation anthrax", "pos": "phrase", "ipa": "", "vi": "bệnh than thể hô hấp", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040130", "hw": "inner hebrides", "pos": "phrase", "ipa": "", "vi": "quần đảo Inner Hebrides", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040131", "hw": "intonation pattern", "pos": "phrase", "ipa": "", "vi": "mô hình ngữ điệu giọng", "cefr": "C1", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040132", "hw": "john copley", "pos": "phrase", "ipa": "", "vi": "họa sĩ John Copley", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040133", "hw": "josiah willard gibbs", "pos": "phrase", "ipa": "", "vi": "nhà vật lý Willard Gibbs", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040134", "hw": "kendal green", "pos": "phrase", "ipa": "", "vi": "vải len xanh Kendal", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040135", "hw": "keyhole saw", "pos": "phrase", "ipa": "", "vi": "cưa xoi; cưa lỗ khóa", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040136", "hw": "leon trotsky", "pos": "phrase", "ipa": "", "vi": "nhà cách mạng Leon Trotsky", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040137", "hw": "lesotho monetary unit", "pos": "phrase", "ipa": "", "vi": "đơn vị tiền tệ Lesotho", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040138", "hw": "leveraged buyout", "pos": "phrase", "ipa": "", "vi": "thâu tóm bằng vốn vay", "cefr": "C1", "tier": "business", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040139", "hw": "lexical ambiguity", "pos": "phrase", "ipa": "", "vi": "tính mơ hồ về từ vựng", "cefr": "C1", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040140", "hw": "lindy hop", "pos": "phrase", "ipa": "", "vi": "điệu nhảy swing Lindy Hop", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040141", "hw": "line of gab", "pos": "phrase", "ipa": "", "vi": "lời lẽ ba hoa; tài ăn nói", "cefr": "C2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040142", "hw": "little dipper", "pos": "phrase", "ipa": "", "vi": "chòm sao Tiểu Hùng", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040143", "hw": "madame curie", "pos": "phrase", "ipa": "", "vi": "bà Marie Curie", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040144", "hw": "margaret sanger", "pos": "phrase", "ipa": "", "vi": "nhà hoạt động Margaret Sanger", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040145", "hw": "martin cline", "pos": "phrase", "ipa": "", "vi": "nhà khoa học Martin Cline", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040146", "hw": "massed fire", "pos": "phrase", "ipa": "", "vi": "hỏa lực bắn tập trung", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040147", "hw": "mekong river", "pos": "phrase", "ipa": "", "vi": "sông Mê Kông", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040148", "hw": "mental quickness", "pos": "phrase", "ipa": "", "vi": "sự nhanh trí; trí óc nhạy bén", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040149", "hw": "mooring tower", "pos": "phrase", "ipa": "", "vi": "tháp neo tàu khí cầu", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040150", "hw": "mount godwin austen", "pos": "phrase", "ipa": "", "vi": "đỉnh K2; núi Godwin Austen", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040151", "hw": "narcotic antagonist", "pos": "phrase", "ipa": "", "vi": "thuốc kháng chất gây nghiện", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040152", "hw": "oedipus rex", "pos": "phrase", "ipa": "", "vi": "vở kịch Oedipus Rex", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040153", "hw": "onion smut", "pos": "phrase", "ipa": "", "vi": "bệnh than đen hại hành", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040154", "hw": "optical condenser", "pos": "phrase", "ipa": "", "vi": "bộ tụ quang kính hiển vi", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040155", "hw": "ord kangaroo rat", "pos": "phrase", "ipa": "", "vi": "chuột túi chuột Ord", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040156", "hw": "orville wright", "pos": "phrase", "ipa": "", "vi": "nhà chế tạo Orville Wright", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040157", "hw": "pin tumbler", "pos": "phrase", "ipa": "", "vi": "con chốt trụ khóa pin", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040158", "hw": "pisces the fishes", "pos": "phrase", "ipa": "", "vi": "chòm sao Song Ngư", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040159", "hw": "pocket billiards", "pos": "phrase", "ipa": "", "vi": "trò chơi bi-a lỗ", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040160", "hw": "poison hemlock", "pos": "phrase", "ipa": "", "vi": "cây độc cần dược liệu", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040161", "hw": "potassium hydroxide", "pos": "phrase", "ipa": "", "vi": "kali hiđroxit; kiềm ăn da", "cefr": "C1", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040162", "hw": "potsdam conference", "pos": "phrase", "ipa": "", "vi": "hội nghị Potsdam lịch sử", "cefr": "C1", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040163", "hw": "primrose jasmine", "pos": "phrase", "ipa": "", "vi": "hoa lài vàng; hoa lài mùa xuân", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040164", "hw": "psychoactive drug", "pos": "phrase", "ipa": "", "vi": "thuốc hướng thần; chất hướng tâm", "cefr": "C1", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040165", "hw": "quezon city", "pos": "phrase", "ipa": "", "vi": "thành phố Quezon", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040166", "hw": "raisin bran", "pos": "phrase", "ipa": "", "vi": "ngũ cốc nho khô cám mạch", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040167", "hw": "rectal artery", "pos": "phrase", "ipa": "", "vi": "động mạch trực tràng", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040168", "hw": "red sprites", "pos": "phrase", "ipa": "", "vi": "sét thượng tầng khí quyển", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040169", "hw": "ring thrush", "pos": "phrase", "ipa": "", "vi": "chim hoét khoang ngực", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040170", "hw": "run aground", "pos": "phrase", "ipa": "", "vi": "mắc cạn bờ; trôi dạt vào bờ", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040171", "hw": "rusty blackbird", "pos": "phrase", "ipa": "", "vi": "chim sáo lông gỉ sắt", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040172", "hw": "saucer magnolia", "pos": "phrase", "ipa": "", "vi": "hoa mộc lan tách trà", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040173", "hw": "sea of cortes", "pos": "phrase", "ipa": "", "vi": "vịnh California biển Cortez", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040174", "hw": "sei whale", "pos": "phrase", "ipa": "", "vi": "cá voi lưng xám Sei", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040175", "hw": "shiite muslim", "pos": "phrase", "ipa": "", "vi": "tín đồ Hồi giáo dòng Shia", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040176", "hw": "sir thomas raffles", "pos": "phrase", "ipa": "", "vi": "ngài Stamford Raffles", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040177", "hw": "soldier grainy club", "pos": "phrase", "ipa": "", "vi": "nấm đầu dù hạt sần sùi", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040178", "hw": "song thrush", "pos": "phrase", "ipa": "", "vi": "chim hoét hót hót ca", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040179", "hw": "subcutaneous test", "pos": "phrase", "ipa": "", "vi": "xét nghiệm tiêm dưới da", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040180", "hw": "sweet sorghum", "pos": "phrase", "ipa": "", "vi": "cây miến mía; cao lương ngọt", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040181", "hw": "toothed sword fern", "pos": "phrase", "ipa": "", "vi": "dương xỉ thanh kiếm có răng", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040182", "hw": "tropic of cancer", "pos": "phrase", "ipa": "", "vi": "đường chí tuyến Bắc", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040183", "hw": "trouser clip", "pos": "phrase", "ipa": "", "vi": "kẹp gấu quần đi xe đạp", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040184", "hw": "tuba root", "pos": "phrase", "ipa": "", "vi": "củ dây mật; rễ cây tuba", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040185", "hw": "water thrush", "pos": "phrase", "ipa": "", "vi": "chim hoét nước đầm lầy", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040186", "hw": "wheat flag smut", "pos": "phrase", "ipa": "", "vi": "bệnh than lá lúa mì", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040187", "hw": "whittle away", "pos": "phrase", "ipa": "", "vi": "gọt tỉa bớt; hao mòn dần", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040188", "hw": "whittle down", "pos": "phrase", "ipa": "", "vi": "cắt giảm dần; rút gọn danh sách", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040189", "hw": "william butterfield", "pos": "phrase", "ipa": "", "vi": "kiến trúc sư Butterfield", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040190", "hw": "winfield scott", "pos": "phrase", "ipa": "", "vi": "tướng quân Winfield Scott", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040191", "hw": "wood ibis", "pos": "phrase", "ipa": "", "vi": "cò lạo Mỹ; chim gỗ ibis", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040192", "hw": "wood thrush", "pos": "phrase", "ipa": "", "vi": "chim hoét rừng sồi", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040193", "hw": "woolly thistle", "pos": "phrase", "ipa": "", "vi": "cây kế lông tơ trắng", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040194", "hw": "yellow turnip", "pos": "phrase", "ipa": "", "vi": "củ cải thụy điển vàng", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040195", "hw": "zambian monetary unit", "pos": "phrase", "ipa": "", "vi": "đơn vị tiền tệ Zambia", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040196", "hw": "absurdities", "pos": "noun", "ipa": "/əbˈsɜːrdətiz/", "vi": "điều vô lý; chuyện phi lý", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040197", "hw": "americanas", "pos": "noun", "ipa": "/əˌmɛrəˈkɑːnəz/", "vi": "văn hóa phẩm đậm chất Mỹ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040198", "hw": "armchairs", "pos": "noun", "ipa": "/ˈɑːrmtʃɛrz/", "vi": "ghế bành tựa; ghế bành mềm", "cefr": "A2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040199", "hw": "aryans", "pos": "noun", "ipa": "/ˈɛriənz/", "vi": "người Aryan thượng đẳng", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040200", "hw": "babysitters", "pos": "noun", "ipa": "/ˈbeɪbiˌsɪtərz/", "vi": "người trông trẻ; người giữ trẻ", "cefr": "A2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040201", "hw": "backlogged", "pos": "verb", "ipa": "/ˈbækˌlɔːɡd/", "vi": "tồn đọng; tích lũy dồn việc", "cefr": "C1", "tier": "business", "status": "reviewed", "notes": ""}
]

# Validation
ALLOWED_POS = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}
with open('scratch/b29_r01_raw_p2.json', 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

assert len(reviewed_items) == 100, f"Expected 100 items, got {len(reviewed_items)}"
for r, rev in zip(raw_items, reviewed_items):
    assert r["id"] == rev["id"], f"ID mismatch: {r['id']} vs {rev['id']}"
    assert r["hw"] == rev["hw"], f"HW mismatch: {r['hw']} vs {rev['hw']}"
    assert rev["pos"] in ALLOWED_POS, f"Invalid POS for {rev['id']}: {rev['pos']}"
    assert 0 < len(rev["vi"]) <= 35, f"Invalid VI length ({len(rev['vi'])}) for {rev['id']}: {rev['vi']}"
    assert rev["status"] == "reviewed", f"Status must be reviewed: {rev['id']}"
    if " " not in rev["hw"]:
        assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/") and rev["ipa"].count("/") == 2, f"Invalid single-word IPA: {rev['id']}: {rev['ipa']}"

with open('scratch/b29_r01_p2.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 1 Part 2 validated and written successfully. Total items:", len(reviewed_items))
