import json

items = [
    ("067503", "polyploidies", "noun", "/ˈpɒlɪˌplɔɪdiz/", "hiện tượng đa bội bộ nhiễm sắc thể"),
    ("067504", "precentors", "noun", "/prɪˈsɛntərz/", "người lĩnh xướng ca đoàn nhà thờ"),
    ("067505", "pyridoxals", "noun", "/ˌpɪrɪˈdɒksəlz/", "dạng vitamin B6 hoạt tính pyridoxal"),
    ("067506", "rarebits", "noun", "/ˈrɛərˌbɪts/", "bánh mì nướng phủ xốt phô mai nóng"),
    ("067507", "reciters", "noun", "/rɪˈsaɪtərz/", "người ngâm thơ; người đọc diễn cảm"),
    ("067508", "rickettsias", "noun", "/rɪˈkɛtsiəz/", "vi khuẩn ký sinh nội bào Rickettsia"),
    ("067509", "salukis", "noun", "/səˈluːkiz/", "chó săn đuổi giống cổ Saluki Trung"),
    ("067510", "sards", "noun", "/sɑːrdz/", "đá ngọc mã não nâu; dân Sardinia"),
    ("067511", "sartors", "noun", "/ˈsɑːrtərz/", "thợ may quần áo (từ cổ văn học)"),
    ("067512", "satchmos", "noun", "/ˈsætʃˌmoʊz/", "biệt danh nghệ sĩ Louis Armstrong"),
    ("067513", "scriptoriums", "noun", "/skrɪpˈtɔːriəmz/", "phòng chép sách bản thảo tu viện"),
    ("067514", "seaborgs", "noun", "/ˈsiːbɔːrɡz/", "nhà hóa học Nobel Glenn Seaborg"),
    ("067515", "seigniorages", "noun", "/ˈseɪnjərɪdʒɪz/", "lợi nhuận chênh lệch đúc phát hành"),
    ("067516", "shorebirds", "noun", "/ˈʃɔːrˌbɜːrdz/", "chim lội kiếm mồi ven bờ biển"),
    ("067517", "smoothbores", "noun", "/ˈsmuːðˌbɔːrz/", "súng nòng trơn không rãnh xoắn"),
    ("067518", "smouldered", "verb", "/ˈsmoʊldərd/", "đã cháy âm ỉ không ngọn lửa"),
    ("067519", "smoulders", "noun", "/ˈsmoʊldərz/", "lửa cháy âm ỉ; đốm than ngún khói"),
    ("067520", "sousses", "noun", "/ˈsuːsɪz/", "thành phố cảng Sousse ở Tunisia"),
    ("067521", "spectrograms", "noun", "/ˈspɛktrəˌɡræmz/", "biểu đồ ảnh phổ tần số âm thanh"),
    ("067522", "spoilsports", "noun", "/ˈspɔɪlˌspɔːrts/", "kẻ phá đám làm cụt hứng mọi người"),
    ("067523", "stobs", "noun", "/stɒbz/", "cọc gỗ ngắn đóng mốc; gốc cây cụt"),
    ("067524", "summersets", "noun", "/ˈsʌmərˌsɛts/", "cú lộn nhào vòng qua đầu (biến thể)"),
    ("067525", "tallboys", "noun", "/ˈtɔːlˌbɔɪz/", "tủ ngăn kéo cao; lon bia cao 16 oz"),
    ("067526", "tereshkovas", "noun", "/ˌtɛrəʃˈkoʊvəz/", "nữ phi hành gia đầu tiên Tereshkova"),
    ("067527", "thiocyanates", "noun", "/ˌθaɪoʊˈsaɪəneɪts/", "muối hoặc este axit thiocyanic"),
    ("067528", "tricots", "noun", "/ˈtriːkoʊz/", "vải dệt kim sợi dọc mịn đàn hồi"),
    ("067529", "trollops", "noun", "/ˈtrɒləps/", "người lôi thôi; người phóng đãng"),
    ("067530", "undulations", "noun", "/ˌʌndjəˈleɪʃənz/", "chuyển động nhấp nhô gợn sóng"),
    ("067531", "wekas", "noun", "/ˈwɛkəz/", "chim weka không bay ở New Zealand"),
    ("067532", "willebrands", "noun", "/ˈvɪləˌbrændz/", "bác sĩ Phần Lan Erik von Willebrand"),
    ("067533", "agaricus campestris", "phrase", "/ˈæɡərɪkəs kæmˈpɛstrɪs/", "nấm mỡ đồng cỏ ăn được"),
    ("067534", "algerian centime", "phrase", "/ælˈdʒɪriən ˈsɒntiːm/", "đơn vị tiền xu centime Algeria"),
    ("067535", "andre maurois", "phrase", "/ɑːnˈdreɪ moʊˈrwɑː/", "nhà văn Pháp André Maurois"),
    ("067536", "antianxiety agent", "phrase", "/ˌæntiæŋˈzaɪəti ˈeɪdʒənt/", "hoạt chất giải lo âu an thần nhẹ"),
    ("067537", "antianxiety drug", "phrase", "/ˌæntiæŋˈzaɪəti drʌɡ/", "thuốc điều trị chứng rối loạn lo âu"),
    ("067538", "arc cotangent", "phrase", "/ɑːrk koʊˈtændʒənt/", "hàm lượng giác ngược arccotang"),
    ("067539", "armillaria ponderosa", "phrase", "/ˌɑːrmɪˈlɛəriə ˌpɒndəˈroʊsə/", "nấm tùng nhung trắng Bắc Mỹ"),
    ("067540", "aum shinrikyo", "phrase", "/aʊm ʃɪnˈriːkjoʊ/", "giáo phái Nhật Aum Shinrikyo"),
    ("067541", "battle of plassey", "phrase", "/ˈbætəl əv ˈplæsi/", "trận Plassey năm 1757 ở Ấn Độ"),
    ("067542", "beurre noisette", "phrase", "/bɜːr nwɑːˈzɛt/", "bơ nấu chín nâu thơm mùi hạt dẻ"),
    ("067543", "bigeye scad", "phrase", "/ˈbɪɡaɪ skæd/", "cá nục tráo mắt to vùng biển ấm"),
    ("067544", "brittle maidenhair fern", "phrase", "/ˈbrɪtəl ˈmeɪdənˌhɛər fɜːrn/", "cây dương xỉ tóc tiên cọng giòn"),
    ("067545", "citta del vaticano", "phrase", "/tʃiːˈtɑː dɛl ˌvɑːtiˈkɑːnoʊ/", "Thành quốc Vatican (tên tiếng Ý)"),
    ("067546", "class arachnida", "phrase", "/klæs əˈræknɪdə/", "lớp Hình nhện gồm nhện và bọ cạp"),
    ("067547", "clumber spaniel", "phrase", "/ˈklʌmbər ˈspænjəl/", "giống chó săn lông dài Clumber Anh"),
    ("067548", "cucumis melo", "phrase", "/ˈkjuːkjʊmɪs ˈmiːloʊ/", "cây dưa lưới; cây dưa bở dưa vàng"),
    ("067549", "elephas maximus", "phrase", "/ˈɛlɪfəs ˈmæksɪməs/", "loài voi châu Á kích thước lớn"),
    ("067550", "family euphorbiaceae", "phrase", "/ˈfæməli juːˌfɔːrbiˈeɪʃiː/", "họ Thầu dầu có nhựa mủ trắng"),
    ("067551", "farley maidenhair fern", "phrase", "/ˈfɑːrli ˈmeɪdənˌhɛər fɜːrn/", "dương xỉ tóc thần giống Farley"),
    ("067552", "finnan haddock", "phrase", "/ˈfɪnən ˈhædək/", "cá tuyết chấm đen hun khói Scotland"),
    ("067553", "fissure of sylvius", "phrase", "/ˈfɪʃər əv ˈsɪlviəs/", "rãnh não bên Sylvius đại não"),
    ("067554", "frederic auguste bartholdi", "phrase", "/ˌfrɛdərɪk oʊˈɡuːst bɑːrˈtɒldi/", "nhà điêu khắc Tượng Nữ thần Tự do"),
    ("067555", "genus camelina", "phrase", "/ˈdʒiːnəs ˌkæməˈlaɪnə/", "chi cây cải dầu camelina"),
    ("067556", "genus cercospora", "phrase", "/ˈdʒiːnəs sɜːrˈkɒspərə/", "chi nấm đốm lá cây Cercospora"),
    ("067557", "genus chironomus", "phrase", "/ˈdʒiːnəs ˌkaɪrəˈnoʊməs/", "chi muỗi lắc không đốt Chironomus"),
    ("067558", "genus coccus", "phrase", "/ˈdʒiːnəs ˈkɒkəs/", "chi rệp sáp vỏ cứng Coccus"),
    ("067559", "genus colocasia", "phrase", "/ˈdʒiːnəs ˌkɒləˈkeɪʃə/", "chi cây khoai môn sọ Colocasia"),
    ("067560", "genus gossypium", "phrase", "/ˈdʒiːnəs ɡɒˈsɪpiəm/", "chi cây bông vải Gossypium"),
    ("067561", "grus americana", "phrase", "/ɡrʌs əˌmɛrɪˈkeɪnə/", "sếu Mỹ trắng quý hiếm có nguy cơ"),
    ("067562", "haitian centime", "phrase", "/ˈheɪʃən ˈsɒntiːm/", "đơn vị tiền xu centime của Haiti"),
    ("067563", "hamate bone", "phrase", "/ˈheɪmeɪt boʊn/", "xương móc trong hàng xương cổ tay"),
    ("067564", "hinayana buddhism", "phrase", "/ˌhiːnəˈjɑːnə ˈbʊdɪzəm/", "Phật giáo Tiểu thừa truyền thống"),
    ("067565", "iles marquises", "phrase", "/iːl mɑːrˈkiːz/", "quần đảo Marquesas vùng Polynesia"),
    ("067566", "jerboa kangaroo", "phrase", "/dʒɜːrˈboʊə ˌkæŋɡəˈruː/", "chuột túi nhảy nhỏ Úc đuôi chổi"),
    ("067567", "jerboa rat", "phrase", "/dʒɜːrˈboʊə ræt/", "chuột nhảy chân dài ở Úc"),
    ("067568", "juglans californica", "phrase", "/ˈdʒuːɡlənz ˌkælɪˈfɔːrnɪkə/", "cây óc chó đen bản địa California"),
    ("067569", "kangaroo jerboa", "phrase", "/ˌkæŋɡəˈruː dʒɜːrˈboʊə/", "chuột túi nhảy nhỏ Úc"),
    ("067570", "louis bleriot", "phrase", "/luːˈiː ˌblɛriˈoʊ/", "phi công tiên phong Louis Blériot"),
    ("067571", "lucius annaeus seneca", "phrase", "/ˈluːʃəs əˈniːəs ˈsɛnɪkə/", "triết gia Khắc kỷ La Mã Seneca"),
    ("067572", "marguerite radclyffe hall", "phrase", "/ˌmɑːrɡəˈriːt ˈrædklɪf hɔːl/", "nữ nhà văn Anh Radclyffe Hall"),
    ("067573", "mentha arvensis", "phrase", "/ˈmɛnθə ɑːrˈvɛnsɪs/", "cây bạc hà đồng ruộng lấy tinh dầu"),
    ("067574", "metacentric chromosome", "phrase", "/ˌmɛtəˈsɛntrɪk ˈkroʊməˌsoʊm/", "nhiễm sắc thể có tâm động ở giữa"),
    ("067575", "mirabilis jalapa", "phrase", "/mɪˈræbɪlɪs dʒəˈlæpə/", "cây hoa phấn nở vào buổi chiều"),
    ("067576", "monocot family", "phrase", "/ˈmɒnəˌkɒt ˈfæməli/", "họ thực vật một lá mầm"),
    ("067577", "monocot genus", "phrase", "/ˈmɒnəˌkɒt ˈdʒiːnəs/", "chi thực vật một lá mầm"),
    ("067578", "mons veneris", "phrase", "/mɒnz ˈvɛnərɪs/", "vùng gò mu phía trước xương mu nữ"),
    ("067579", "mount kanchenjunga", "phrase", "/maʊnt ˌkɑːntʃənˈdʒʊŋɡə/", "đỉnh núi cao thứ ba Kanchenjunga"),
    ("067580", "mousseline de sole", "phrase", "/ˌmuːsəˈliːn də swɑː/", "vải tơ lụa mỏng nhẹ mousseline"),
    ("067581", "muscular tonus", "phrase", "/ˈmʌskjələr ˈtoʊnəs/", "trương lực căng tự nhiên của cơ"),
    ("067582", "nicker nut", "phrase", "/ˈnɪkər nʌt/", "hạt mộc qua biển cứng làm chuỗi"),
    ("067583", "nicker seed", "phrase", "/ˈnɪkər siːd/", "hạt cây dây vút nicker biển"),
    ("067584", "openside plane", "phrase", "/ˈoʊpənˌsaɪd pleɪn/", "bào hở cạnh dùng soi rãnh mộng gỗ"),
    ("067585", "pinus mugo", "phrase", "/ˈpaɪnəs ˈmjuːɡoʊ/", "cây thông lùn núi mugo châu Âu"),
    ("067586", "redwood penstemon", "phrase", "/ˈrɛdwʊd ˈpɛnstəmən/", "hoa mõm rồng rừng gỗ đỏ California"),
    ("067587", "rosa canina", "phrase", "/ˈroʊzə kəˈnaɪnə/", "cây hoa hồng dại tầm xuân châu Âu"),
    ("067588", "salad nicoise", "phrase", "/ˈsæləd niːˈswɑːz/", "món xà lách cá ngừ kiểu Nice Pháp"),
    ("067589", "scented penstemon", "phrase", "/ˈsɛntɪd ˈpɛnstəmən/", "cây hoa mõm rồng tỏa hương thơm"),
    ("067590", "seborrheic keratosis", "phrase", "/ˌsɛbəˈriːɪk ˌkɛrəˈtoʊsɪs/", "tình trạng dày sừng tiết bã lành"),
    ("067591", "serge koussevitzky", "phrase", "/sɜːrdʒ ˌkuːsəˈvɪtski/", "nhạc trưởng Nga Mỹ Koussevitzky"),
    ("067592", "sir seretse khama", "phrase", "/sɜːr səˈrɛtseɪ ˈkɑːmə/", "Tổng thống đầu tiên của Botswana"),
    ("067593", "soursop tree", "phrase", "/ˈsaʊərsɒp triː/", "cây mãng cầu xiêm ăn quả chua ngọt"),
    ("067594", "topgallant mast", "phrase", "/təˈɡælənt mæst/", "đốt cột buồm thượng trên tàu buồm"),
    ("067595", "topgallant sail", "phrase", "/təˈɡælənt seɪl/", "cánh buồm thượng tầng ba trên tàu"),
    ("067596", "typical jerboa", "phrase", "/ˈtɪpɪkəl dʒɜːrˈboʊə/", "chuột nhảy sa mạc điển hình jerboa"),
    ("067597", "ulmus pumila", "phrase", "/ˈʌlməs ˈpjuːmɪlə/", "cây du lùn Siberia chịu hạn tốt"),
    ("067598", "veronica peregrina", "phrase", "/vəˈrɒnɪkə ˌpɛrɪˈɡriːnə/", "cỏ thủy tiên lá rau sam Bắc Mỹ"),
    ("067599", "viola canina", "phrase", "/vaɪˈoʊlə kəˈnaɪnə/", "cây hoa tím dại đồng cỏ châu Âu"),
    ("067600", "vulpes velox", "phrase", "/ˈvʌlpiːz ˈviːlɒks/", "cáo nhanh đồng cỏ Bắc Mỹ"),
    ("067601", "adzes", "noun", "/ˈædzɪz/", "rìu lưỡi ngang để đẽo gọt gỗ"),
    ("067602", "aeronauts", "noun", "/ˈɛərəˌnɔːts/", "phi công lái khinh khí cầu khí cụ"),
]

with open("scratch/b34_r06_raw_p1.json") as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100
allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}

out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, items):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} != {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} != {hw}"
    assert pos in allowed_pos, f"Bad POS {pos} for {hw}"
    assert len(vi) <= 35, f"VI too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA: {hw} -> {ipa}"
    inner = ipa[1:-1]
    assert inner and not inner.startswith(" ") and not inner.endswith(" "), f"Empty/space IPA: {hw} -> {ipa}"
    rec = dict(r)
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

with open("scratch/b34_r06_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r06_p1.json OK")
