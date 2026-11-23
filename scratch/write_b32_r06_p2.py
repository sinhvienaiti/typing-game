import json

records = [
    {"id": "lex.en.200k.057602", "hw": "amenhotep iv", "pos": "phrase", "ipa": "", "vi": "pharaon Amenhotep IV Akhenaten"},
    {"id": "lex.en.200k.057603", "hw": "amyl nitrate", "pos": "phrase", "ipa": "", "vi": "hợp chất hữu cơ amyl nitrat"},
    {"id": "lex.en.200k.057604", "hw": "analysis situs", "pos": "phrase", "ipa": "", "vi": "ngành hình học tô pô cổ điển"},
    {"id": "lex.en.200k.057605", "hw": "anticholinergic drug", "pos": "phrase", "ipa": "", "vi": "thuốc kháng hệ cholinergic y học"},
    {"id": "lex.en.200k.057606", "hw": "arabidopsis thaliana", "pos": "phrase", "ipa": "", "vi": "cây cải mô hình Arabidopsis"},
    {"id": "lex.en.200k.057607", "hw": "austronesian language", "pos": "phrase", "ipa": "", "vi": "ngữ hệ Nam Đảo Austronesian"},
    {"id": "lex.en.200k.057608", "hw": "bertolt brecht", "pos": "phrase", "ipa": "", "vi": "kịch tác gia Đức Bertolt Brecht"},
    {"id": "lex.en.200k.057609", "hw": "blazon out", "pos": "phrase", "ipa": "", "vi": "công bố rộng rãi; loan báo rầm rộ"},
    {"id": "lex.en.200k.057610", "hw": "bulgur wheat", "pos": "phrase", "ipa": "", "vi": "lúa mì nứt bulgur hạt nguyên cám"},
    {"id": "lex.en.200k.057611", "hw": "caesarian delivery", "pos": "phrase", "ipa": "", "vi": "phương pháp sinh mổ bắt con"},
    {"id": "lex.en.200k.057612", "hw": "caesarian section", "pos": "phrase", "ipa": "", "vi": "phẫu thuật sinh mổ lấy thai"},
    {"id": "lex.en.200k.057613", "hw": "carbon tetrachloride", "pos": "phrase", "ipa": "", "vi": "dung môi cacbon tetraclorua CCl4"},
    {"id": "lex.en.200k.057614", "hw": "cassia occidentalis", "pos": "phrase", "ipa": "", "vi": "cây muồng tây muồng ngủ dại"},
    {"id": "lex.en.200k.057615", "hw": "charles digby harrod", "pos": "phrase", "ipa": "", "vi": "doanh nhân bán lẻ Charles Harrod"},
    {"id": "lex.en.200k.057616", "hw": "class amphibia", "pos": "phrase", "ipa": "", "vi": "lớp Động vật lưỡng cư sinh vật"},
    {"id": "lex.en.200k.057617", "hw": "damson plum", "pos": "phrase", "ipa": "", "vi": "cây mận damson quả tím thẫm"},
    {"id": "lex.en.200k.057618", "hw": "damson plum tree", "pos": "phrase", "ipa": "", "vi": "cây mận gai damson sai quả tím"},
    {"id": "lex.en.200k.057619", "hw": "dante alighieri", "pos": "phrase", "ipa": "", "vi": "đại thi hào Ý Dante Alighieri"},
    {"id": "lex.en.200k.057620", "hw": "discriminative stimulus", "pos": "phrase", "ipa": "", "vi": "kích thích phân biệt hành vi"},
    {"id": "lex.en.200k.057621", "hw": "downy brome", "pos": "phrase", "ipa": "", "vi": "cỏ lúa hoang brome lông tơ"},
    {"id": "lex.en.200k.057622", "hw": "drooping brome", "pos": "phrase", "ipa": "", "vi": "cỏ brome đuôi chồn rủ nhánh"},
    {"id": "lex.en.200k.057623", "hw": "ellice islands", "pos": "phrase", "ipa": "", "vi": "quần đảo Ellice nay là Tuvalu"},
    {"id": "lex.en.200k.057624", "hw": "european nuthatch", "pos": "phrase", "ipa": "", "vi": "chim trèo cây nuthatch châu Âu"},
    {"id": "lex.en.200k.057625", "hw": "ex libris", "pos": "phrase", "ipa": "", "vi": "con dấu nhãn sách cá nhân"},
    {"id": "lex.en.200k.057626", "hw": "garcinia cambogia", "pos": "phrase", "ipa": "", "vi": "cây bứa chua Garcinia cambogia"},
    {"id": "lex.en.200k.057627", "hw": "genus banksia", "pos": "phrase", "ipa": "", "vi": "chi cây hoa banksia nước Úc"},
    {"id": "lex.en.200k.057628", "hw": "genus calendula", "pos": "phrase", "ipa": "", "vi": "chi Cúc kim tiền hoa cúc vạn thọ"},
    {"id": "lex.en.200k.057629", "hw": "genus chlorella", "pos": "phrase", "ipa": "", "vi": "chi vi tảo lục đơn bào Chlorella"},
    {"id": "lex.en.200k.057630", "hw": "genus saiga", "pos": "phrase", "ipa": "", "vi": "chi linh dương mũi to saiga"},
    {"id": "lex.en.200k.057631", "hw": "guglielmo marconi", "pos": "phrase", "ipa": "", "vi": "nhà phát minh Guglielmo Marconi"},
    {"id": "lex.en.200k.057632", "hw": "ida minerva tarbell", "pos": "phrase", "ipa": "", "vi": "nhà báo điều tra Mỹ Ida Tarbell"},
    {"id": "lex.en.200k.057633", "hw": "intra vires", "pos": "phrase", "ipa": "", "vi": "trong phạm vi thẩm quyền luật định"},
    {"id": "lex.en.200k.057634", "hw": "john roebling", "pos": "phrase", "ipa": "", "vi": "kỹ sư xây cầu treo John Roebling"},
    {"id": "lex.en.200k.057635", "hw": "ken elton kesey", "pos": "phrase", "ipa": "", "vi": "văn hào người Mỹ Ken Elton Kesey"},
    {"id": "lex.en.200k.057636", "hw": "kurt waldheim", "pos": "phrase", "ipa": "", "vi": "Tổng thư ký LHQ Kurt Waldheim"},
    {"id": "lex.en.200k.057637", "hw": "lettre de cachet", "pos": "phrase", "ipa": "", "vi": "trát lệnh bắt giam của hoàng gia"},
    {"id": "lex.en.200k.057638", "hw": "libyan dirham", "pos": "phrase", "ipa": "", "vi": "đồng tiền xu dirham của Libya"},
    {"id": "lex.en.200k.057639", "hw": "loris gracilis", "pos": "phrase", "ipa": "", "vi": "loài vượn mắt to cu li mảnh khảnh"},
    {"id": "lex.en.200k.057640", "hw": "lower tunguska", "pos": "phrase", "ipa": "", "vi": "dòng sông Hạ Tunguska ở Siberia"},
    {"id": "lex.en.200k.057641", "hw": "methyl salicylate", "pos": "phrase", "ipa": "", "vi": "dầu nóng xoa bóp metyl salixylat"},
    {"id": "lex.en.200k.057642", "hw": "moroccan dirham", "pos": "phrase", "ipa": "", "vi": "đồng tiền tệ dirham Ma-rốc"},
    {"id": "lex.en.200k.057643", "hw": "myocardial infarct", "pos": "phrase", "ipa": "", "vi": "chứng nhồi máu cơ tim cấp tính"},
    {"id": "lex.en.200k.057644", "hw": "needle furze", "pos": "phrase", "ipa": "", "vi": "cây kim tước gai vàng nở rộ"},
    {"id": "lex.en.200k.057645", "hw": "obovate leaf", "pos": "phrase", "ipa": "", "vi": "lá hình trứng ngược cuống nhọn"},
    {"id": "lex.en.200k.057646", "hw": "peter alexander ustinov", "pos": "phrase", "ipa": "", "vi": "nam diễn viên tài tử Peter Ustinov"},
    {"id": "lex.en.200k.057647", "hw": "pieter bruegel", "pos": "phrase", "ipa": "", "vi": "danh họa Hà Lan Pieter Bruegel"},
    {"id": "lex.en.200k.057648", "hw": "plautus alle", "pos": "phrase", "ipa": "", "vi": "chim anca nhỏ bờ biển Bắc Cực"},
    {"id": "lex.en.200k.057649", "hw": "posse comitatus", "pos": "phrase", "ipa": "", "vi": "lực lượng dân phòng tạm thời"},
    {"id": "lex.en.200k.057650", "hw": "quercus bicolor", "pos": "phrase", "ipa": "", "vi": "loài sồi đầm lầy trắng hai màu lá"},
    {"id": "lex.en.200k.057651", "hw": "raymond bernard cattell", "pos": "phrase", "ipa": "", "vi": "nhà tâm lý học Raymond Cattell"},
    {"id": "lex.en.200k.057652", "hw": "regulus regulus", "pos": "phrase", "ipa": "", "vi": "chim tước mào vàng châu Âu"},
    {"id": "lex.en.200k.057653", "hw": "robert andrews millikan", "pos": "phrase", "ipa": "", "vi": "nhà vật lý Nobel Robert Millikan"},
    {"id": "lex.en.200k.057654", "hw": "rosa banksia", "pos": "phrase", "ipa": "", "vi": "loài hồng hoa vàng leo Banksia"},
    {"id": "lex.en.200k.057655", "hw": "sea of okhotsk", "pos": "phrase", "ipa": "", "vi": "vùng biển Okhotsk lạnh viễn đông"},
    {"id": "lex.en.200k.057656", "hw": "shish kebab", "pos": "phrase", "ipa": "", "vi": "món thịt xiên nướng shish kebab"},
    {"id": "lex.en.200k.057657", "hw": "sidle up", "pos": "phrase", "ipa": "", "vi": "lén lút tiến lại gần bên cạnh"},
    {"id": "lex.en.200k.057658", "hw": "sildenafil citrate", "pos": "phrase", "ipa": "", "vi": "hoạt chất cường dương sildenafil"},
    {"id": "lex.en.200k.057659", "hw": "sir peter ustinov", "pos": "phrase", "ipa": "", "vi": "nghệ sĩ sân khấu Sir Peter Ustinov"},
    {"id": "lex.en.200k.057660", "hw": "slacken off", "pos": "phrase", "ipa": "", "vi": "chùng xuống; giảm dần cường độ"},
    {"id": "lex.en.200k.057661", "hw": "smooth softshell", "pos": "phrase", "ipa": "", "vi": "loài rùa mai mềm mai nhẵn bóng"},
    {"id": "lex.en.200k.057662", "hw": "stephen butler leacock", "pos": "phrase", "ipa": "", "vi": "nhà văn trào phúng Stephen Leacock"},
    {"id": "lex.en.200k.057663", "hw": "stephen leacock", "pos": "phrase", "ipa": "", "vi": "nhà văn danh hài Stephen Leacock"},
    {"id": "lex.en.200k.057664", "hw": "streptococcal sore throat", "pos": "phrase", "ipa": "", "vi": "viêm họng mủ do liên cầu khuẩn"},
    {"id": "lex.en.200k.057665", "hw": "taconic mountains", "pos": "phrase", "ipa": "", "vi": "dãy núi Taconic miền đông nước Mỹ"},
    {"id": "lex.en.200k.057666", "hw": "tetanus antitoxin", "pos": "phrase", "ipa": "", "vi": "huyết thanh kháng độc tố uốn ván"},
    {"id": "lex.en.200k.057667", "hw": "trackless trolley", "pos": "phrase", "ipa": "", "vi": "xe buýt bánh hơi chạy bằng điện"},
    {"id": "lex.en.200k.057668", "hw": "tyrolean alps", "pos": "phrase", "ipa": "", "vi": "dãy núi An-pơ miền Tyrol"},
    {"id": "lex.en.200k.057669", "hw": "upper tunguska", "pos": "phrase", "ipa": "", "vi": "dòng sông Thượng Tunguska Siberia"},
    {"id": "lex.en.200k.057670", "hw": "vena cerebrum superior", "pos": "phrase", "ipa": "", "vi": "tĩnh mạch đại não trên màng não"},
    {"id": "lex.en.200k.057671", "hw": "voyageurs national park", "pos": "phrase", "ipa": "", "vi": "Vườn quốc gia sông nước Voyageurs"},
    {"id": "lex.en.200k.057672", "hw": "wattle and daub", "pos": "phrase", "ipa": "", "vi": "kỹ thuật trát vách phên bùn rơm"},
    {"id": "lex.en.200k.057673", "hw": "wild emmer", "pos": "phrase", "ipa": "", "vi": "loài lúa mì hoang sơ khai emmer"},
    {"id": "lex.en.200k.057674", "hw": "abrogations", "pos": "noun", "ipa": "/ˌæbrəˈɡeɪʃənz/", "vi": "các quyết định bãi bỏ hủy bỏ luật"},
    {"id": "lex.en.200k.057675", "hw": "adenauers", "pos": "noun", "ipa": "/ˈædənˌaʊɚz/", "vi": "thủ tướng Tây Đức Konrad Adenauer"},
    {"id": "lex.en.200k.057676", "hw": "amyloidoses", "pos": "noun", "ipa": "/ˌæmɪlɔɪˈdoʊsiːz/", "vi": "bệnh thoái hóa dạng tinh bột"},
    {"id": "lex.en.200k.057677", "hw": "antofagastas", "pos": "noun", "ipa": "/ˌæntoʊfəˈɡæstəz/", "vi": "thành phố cảng Antofagasta Chile"},
    {"id": "lex.en.200k.057678", "hw": "assameses", "pos": "noun", "ipa": "/ˌæsəˈmiːzɪz/", "vi": "người dân hoặc tiếng Assam Ấn Độ"},
    {"id": "lex.en.200k.057679", "hw": "auks", "pos": "noun", "ipa": "/ɔːks/", "vi": "loài chim lặn biển anca phương bắc"},
    {"id": "lex.en.200k.057680", "hw": "banguis", "pos": "noun", "ipa": "/bɑːŋˈɡiːz/", "vi": "thành phố thủ đô Bangui Trung Phi"},
    {"id": "lex.en.200k.057681", "hw": "bannockburns", "pos": "noun", "ipa": "/ˌbænəkˈbɜːrnz/", "vi": "chiến trường Bannockburn lịch sử"},
    {"id": "lex.en.200k.057682", "hw": "barbadians", "pos": "noun", "ipa": "/bɑːrˈbeɪdiənz/", "vi": "người dân đảo quốc Barbados Caribe"},
    {"id": "lex.en.200k.057683", "hw": "bassinets", "pos": "noun", "ipa": "/ˌbæsɪˈnɛts/", "vi": "chiếc nôi giỏ đan cho trẻ em"},
    {"id": "lex.en.200k.057684", "hw": "beechwoods", "pos": "noun", "ipa": "/ˈbiːtʃwʊdz/", "vi": "khu rừng dẻ gai; gỗ dẻ gai"},
    {"id": "lex.en.200k.057685", "hw": "behaviorists", "pos": "noun", "ipa": "/bɪˈheɪvjɚɪsts/", "vi": "các nhà tâm lý học hành vi"},
    {"id": "lex.en.200k.057686", "hw": "belched", "pos": "verb", "ipa": "/bɛltʃt/", "vi": "đã ợ hơi to; đã phun trào khói bụi"},
    {"id": "lex.en.200k.057687", "hw": "belches", "pos": "noun", "ipa": "/ˈbɛltʃɪz/", "vi": "tiếng ợ hơi; đợt phun khói bụi"},
    {"id": "lex.en.200k.057688", "hw": "bestiaries", "pos": "noun", "ipa": "/ˈbɛstɪˌɛriz/", "vi": "sách ngụ ngôn chép về loài thú"},
    {"id": "lex.en.200k.057689", "hw": "bravuras", "pos": "noun", "ipa": "/brəˈvjʊrəz/", "vi": "màn phô diễn kỹ xảo điêu luyện"},
    {"id": "lex.en.200k.057690", "hw": "buchenwalds", "pos": "noun", "ipa": "/ˈbuːxənvɑːldz/", "vi": "trại tập trung Buchenwald phát xít"},
    {"id": "lex.en.200k.057691", "hw": "carillonned", "pos": "verb", "ipa": "/ˈkærɪlɑːnd/", "vi": "đã gióng chuông chùm hòa âm"},
    {"id": "lex.en.200k.057692", "hw": "carillonning", "pos": "verb", "ipa": "/ˈkærɪlɑːnɪŋ/", "vi": "đang tấu chuông chùm tháp chuông"},
    {"id": "lex.en.200k.057693", "hw": "chattahoochees", "pos": "noun", "ipa": "/ˌtʃætəˈhuːtʃiz/", "vi": "sông Chattahoochee bang Georgia"},
    {"id": "lex.en.200k.057694", "hw": "cochleas", "pos": "noun", "ipa": "/ˈkɑːkliəz/", "vi": "các ốc tai tiếp nhận thính giác"},
    {"id": "lex.en.200k.057695", "hw": "concatenations", "pos": "noun", "ipa": "/kənˌkætəˈneɪʃənz/", "vi": "chuỗi biến cố liên kết liên hoàn"},
    {"id": "lex.en.200k.057696", "hw": "concertinaed", "pos": "verb", "ipa": "/ˌkɑːnsɚˈtiːnəd/", "vi": "đã gập lại như xếp quạt ruột mèo"},
    {"id": "lex.en.200k.057697", "hw": "concertinaing", "pos": "verb", "ipa": "/ˌkɑːnsɚˈtiːnəɪŋ/", "vi": "đang xếp gập dồn lại nén cong"},
    {"id": "lex.en.200k.057698", "hw": "concertinas", "pos": "noun", "ipa": "/ˌkɑːnsɚˈtiːnəz/", "vi": "cây đàn xếp nhỏ concertina"},
    {"id": "lex.en.200k.057699", "hw": "copulae", "pos": "noun", "ipa": "/ˈkɑːpjʊliː/", "vi": "các liên động từ nối ngữ pháp"},
    {"id": "lex.en.200k.057700", "hw": "dails", "pos": "noun", "ipa": "/dɔːlz/", "vi": "hạ viện Quốc hội nước Ireland"},
    {"id": "lex.en.200k.057701", "hw": "demostheneses", "pos": "noun", "ipa": "/dɪˈmɑːsθəniːzɪz/", "vi": "hùng biện gia vĩ đại Demosthenes"}
]

# Validation
with open('scratch/b32_r06_raw_p2.json') as f:
    raw = json.load(f)

assert len(records) == 100, f"Expected 100 records, got {len(records)}"
for i, (r, raw_r) in enumerate(zip(records, raw)):
    assert r['id'] == raw_r['id'], f"Mismatch id at {i}: {r['id']} vs {raw_r['id']}"
    assert r['hw'] == raw_r['hw'], f"Mismatch hw at {i}: {r['hw']} vs {raw_r['hw']}"
    assert len(r['vi']) <= 35, f"Length violation at {i} ({r['hw']}): len={len(r['vi'])}: {r['vi']}"
    assert r['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {r['pos']}"
    if ' ' not in r['hw']:
        assert r['ipa'].startswith('/') and r['ipa'].endswith('/') and r['ipa'].count('/') == 2, f"Invalid ipa at {i}: {r['ipa']}"

# Merge with raw
final_p2 = []
for r, raw_r in zip(records, raw):
    item = dict(raw_r)
    item['pos'] = r['pos']
    item['ipa'] = r['ipa']
    item['vi'] = r['vi']
    item['status'] = 'reviewed'
    final_p2.append(item)

with open('scratch/b32_r06_p2.json', 'w') as f:
    json.dump(final_p2, f, ensure_ascii=False, indent=2)
print("Part 2 validated and written successfully.")
