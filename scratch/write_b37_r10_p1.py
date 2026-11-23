import json

RECORDS = [
    ("084503", "saddest", "adj", "/ˈsædɪst/", "buồn nhất; thảm thương nhất"),
    ("084504", "saddhu", "noun", "/ˈsɑːduː/", "đạo sĩ khổ hạnh Ấn Độ"),
    ("084505", "saddlebacked", "adj", "/ˈsædəlˌbækt/", "lưng võng yên ngựa; sống trâu"),
    ("084506", "saddlebacks", "noun", "/ˈsædəlˌbæks/", "đồi sống trâu; chim lưng yên"),
    ("084507", "saddlebill", "noun", "/ˈsædəlˌbɪl/", "cò mỏ yên châu Phi"),
    ("084508", "saddlebow", "noun", "/ˈsædəlˌboʊ/", "vành cong trước yên ngựa"),
    ("084509", "saddlecloth", "noun", "/ˈsædəlˌklɔːθ/", "khăn lót yên ngựa"),
    ("084510", "saddlefast", "adj", "/ˈsædəlˌfæst/", "ngồi vững chắc trên yên ngựa"),
    ("084511", "saddleries", "noun", "/ˈsædləriz/", "nghề làm yên ngựa; đồ yên cương"),
    ("084512", "saddlers", "noun", "/ˈsædlərz/", "thợ làm yên ngựa"),
    ("084513", "saddles", "verb", "/ˈsædəlz/", "thắng yên ngựa; bắt gánh vác"),
    ("084514", "saddling", "verb", "/ˈsædlɪŋ/", "đang thắng yên; đang chất gánh"),
    ("084515", "sadducean", "adj", "/ˌsædʒəˈsiːən/", "thuộc giáo phái Sa-đốc cổ"),
    ("084516", "sadhe", "noun", "/ˈtsɑːdeɪ/", "chữ cái Do Thái Tsade"),
    ("084517", "sadiron", "noun", "/ˈsædˌaɪərn/", "bàn là gang nung nóng cổ"),
    ("084518", "sadirons", "noun", "/ˈsædˌaɪərnz/", "bàn là gang nung nóng cổ"),
    ("084519", "sadistically", "adv", "/səˈdɪstɪkli/", "tàn bạo; thích hành hạ dã man"),
    ("084520", "sadleria", "noun", "/sædˈlɪriə/", "chi dương xỉ Sadleria Hawaii"),
    ("084521", "sadnesses", "noun", "/ˈsædnəsɪz/", "nỗi buồn; sự u sầu"),
    ("084522", "sadomasochisms", "noun", "/ˌseɪdoʊˈmæsəˌkɪzəmz/", "xu hướng bạo dâm và khổ dâm"),
    ("084523", "sae", "noun", "/ˌɛsˌeɪˈiː/", "phong bì dán tem sẵn địa chỉ"),
    ("084524", "saek", "noun", "/sɛk/", "tiếng Saek (ngữ hệ Kra-Dai)"),
    ("084525", "safaqis", "noun", "/sfæks/", "thành phố cảng Sfax (Tunisia)"),
    ("084526", "safebreaker", "noun", "/ˈseɪfˌbreɪkər/", "kẻ chuyên phá két sắt"),
    ("084527", "safeguarded", "verb", "/ˈseɪfˌɡɑːrdɪd/", "đã bảo vệ; đã giữ gìn an toàn"),
    ("084528", "safeguarding", "verb", "/ˈseɪfˌɡɑːrdɪŋ/", "đang bảo vệ; đang giữ an toàn"),
    ("084529", "safeguards", "verb", "/ˈseɪfˌɡɑːrdz/", "bảo vệ; giữ gìn an toàn"),
    ("084530", "safelamp", "noun", "/ˈseɪfˌlæmp/", "đèn an toàn buồng tối"),
    ("084531", "safelight", "noun", "/ˈseɪfˌlaɪt/", "đèn phòng tối tráng ảnh"),
    ("084532", "saffian", "noun", "/ˈsæfiən/", "da dê thuộc nhuộm màu sáng"),
    ("084533", "saffians", "noun", "/ˈsæfiənz/", "da dê thuộc nhuộm màu sáng"),
    ("084534", "safflowers", "noun", "/ˈsæfˌlaʊərz/", "cây hồng hoa; hoa rum"),
    ("084535", "saffranin", "noun", "/ˈsæfrənɪn/", "thuốc nhuộm đỏ safranin"),
    ("084536", "saffranine", "noun", "/ˈsæfrəˌniːn/", "thuốc nhuộm đỏ safranin"),
    ("084537", "safi", "noun", "/ˈsɑːfi/", "thành phố cảng Safi (Maroc)"),
    ("084538", "safranin", "noun", "/ˈsæfrənɪn/", "thuốc nhuộm đỏ safranin"),
    ("084539", "safranine", "noun", "/ˈsæfrəˌniːn/", "thuốc nhuộm đỏ safranin"),
    ("084540", "sagaciously", "adv", "/səˈɡeɪʃəsli/", "khôn ngoan; sắc sảo"),
    ("084541", "sagaciousness", "noun", "/səˈɡeɪʃəsnəs/", "sự sắc sảo; trí minh mẫn"),
    ("084542", "sagacities", "noun", "/səˈɡæsɪtiz/", "sự minh mẫn; sự sáng suốt"),
    ("084543", "sagamores", "noun", "/ˈsæɡəˌmɔːrz/", "tù trưởng bộ lạc Bắc Mỹ"),
    ("084544", "sageness", "noun", "/ˈseɪdʒnəs/", "sự khôn ngoan; tính từng trải"),
    ("084545", "saggar", "noun", "/ˈsæɡər/", "bao nung đồ gốm chịu nhiệt"),
    ("084546", "sagged", "verb", "/sæɡd/", "đã võng xuống; đã chùng xuống"),
    ("084547", "sagger", "noun", "/ˈsæɡər/", "bao nung đồ gốm chịu nhiệt"),
    ("084548", "saggy", "adj", "/ˈsæɡi/", "bị võng xuống; chảy xệ"),
    ("084549", "sagina", "noun", "/səˈdʒaɪnə/", "chi cỏ trân châu Sagina"),
    ("084550", "sagittariidae", "noun", "/ˌsædʒɪˈtɛriˌdiː/", "họ Chim thư ký (Sagittariidae)"),
    ("084551", "sagittary", "adj", "/ˈsædʒɪˌtɛri/", "hình mũi tên"),
    ("084552", "sagittate", "adj", "/ˈsædʒɪteɪt/", "hình đầu mũi tên (lá)"),
    ("084553", "sagittated", "adj", "/ˈsædʒɪˌteɪtɪd/", "có dạng đầu mũi tên"),
    ("084554", "sagittiform", "adj", "/səˈdʒɪtɪˌfɔːrm/", "có hình mũi tên"),
    ("084555", "sags", "verb", "/sæɡz/", "võng xuống; chùng xuống; sụt giảm"),
    ("084556", "sahaptin", "noun", "/səˈhɑːptɪn/", "người Sahaptin; tiếng Sahaptin"),
    ("084557", "sahaptino", "noun", "/ˌsɑːhɑːpˈtiːnoʊ/", "người bản địa Sahaptin"),
    ("084558", "saigonese", "adj", "/ˌsaɪɡɑːˈniːz/", "thuộc Sài Gòn; người Sài Gòn"),
    ("084559", "sailable", "adj", "/ˈseɪləbəl/", "có thể đi thuyền buồm qua"),
    ("084560", "sailboater", "noun", "/ˈseɪlˌboʊtər/", "người chơi thuyền buồm"),
    ("084561", "sailed", "verb", "/seɪld/", "đã đi thuyền buồm; đã vượt biển"),
    ("084562", "sailer", "noun", "/ˈseɪlər/", "tàu thuyền chạy buồm"),
    ("084563", "sailess", "adj", "/ˈseɪlləs/", "không có cánh buồm"),
    ("084564", "sailorly", "adj", "/ˈseɪlərli/", "ra dáng thủy thủ; thạo nghề biển"),
    ("084565", "sailplaning", "noun", "/ˈseɪlˌpleɪnɪŋ/", "môn bay tàu lượn không động cơ"),
    ("084566", "sails", "verb", "/seɪlz/", "lái thuyền buồm; ra khơi"),
    ("084567", "sain", "verb", "/seɪn/", "ban phép lành; làm dấu thánh giá"),
    ("084568", "saintess", "noun", "/ˈseɪntɪs/", "nữ thánh"),
    ("084569", "saintlike", "adj", "/ˈseɪntˌlaɪk/", "thánh thiện; hiền từ như thánh"),
    ("084570", "saintness", "noun", "/ˈseɪntnəs/", "đức hạnh thánh thiện"),
    ("084571", "saintpaulia", "noun", "/ˌseɪntˈpɔːliə/", "cây hoa tử linh lan châu Phi"),
    ("084572", "saintship", "noun", "/ˈseɪntˌʃɪp/", "phẩm vị thánh nhân"),
    ("084573", "saith", "verb", "/ˈsɛθ/", "nói (ngôi 3 số ít dạng cổ)"),
    ("084574", "saiva", "noun", "/ˈʃaɪvə/", "tín đồ thờ thần Shiva"),
    ("084575", "saivism", "noun", "/ˈʃaɪˌvɪzəm/", "tín ngưỡng thờ thần Shiva"),
    ("084576", "sajama", "noun", "/səˈhɑːmə/", "núi lửa Sajama (Bolivia)"),
    ("084577", "sakartvelo", "noun", "/sɑːˌkɑːrtˈvɛloʊ/", "nước Gruzia (tên bản địa)"),
    ("084578", "saker", "noun", "/ˈseɪkər/", "chim cắt Saker; đại bác nhỏ xưa"),
    ("084579", "sakra", "noun", "/ˈʃʌkrə/", "thần Đế Thích (Phật giáo)"),
    ("084580", "saktism", "noun", "/ˈʃɑːkˌtɪzəm/", "giáo phái thờ nữ thần Shakti"),
    ("084581", "sakurako", "noun", "/sɑːˈkʊrəˌkoʊ/", "tên riêng nữ Nhật Sakurako"),
    ("084582", "sakyamuni", "noun", "/ˌʃɑːkjəˈmuːni/", "Đức Phật Thích Ca Mâu Ni"),
    ("084583", "sal", "noun", "/sæl/", "cây dầu săng Ấn Độ; muối"),
    ("084584", "salaamed", "verb", "/səˈlɑːmd/", "đã cúi đầu chào kiểu Hồi giáo"),
    ("084585", "salaaming", "verb", "/səˈlɑːmɪŋ/", "đang cúi chào kiểu Hồi giáo"),
    ("084586", "salaams", "verb", "/səˈlɑːmz/", "cúi đầu chào kiểu Hồi giáo"),
    ("084587", "salableness", "noun", "/ˈseɪləbəlnəs/", "tính dễ bán; khả năng tiêu thụ"),
    ("084588", "salaciously", "adv", "/səˈleɪʃəsli/", "dâm đãng; khiêu dâm thô tục"),
    ("084589", "salaciousness", "noun", "/səˈleɪʃəsnəs/", "tính dâm đãng; sự tục tĩu"),
    ("084590", "salacity", "noun", "/səˈlæsɪti/", "tính dâm đãng; thói hiếu sắc"),
    ("084591", "salamanders", "noun", "/ˈsæləˌmændərz/", "kỳ giông; rồng lửa thần thoại"),
    ("084592", "salamandridae", "noun", "/ˌsæləˈmændrɪˌdiː/", "họ Kỳ giông (Salamandridae)"),
    ("084593", "salamandriform", "adj", "/ˌsæləˈmændrɪˌfɔːrm/", "có hình dạng giống kỳ giông"),
    ("084594", "salamandrine", "adj", "/ˌsæləˈmændrɪn/", "thuộc kỳ giông; chịu được lửa"),
    ("084595", "salangane", "noun", "/ˈsælənˌɡeɪn/", "chim yến làm tổ (yến sào)"),
    ("084596", "salariat", "noun", "/səˈlɛriət/", "tầng lớp người làm công ăn lương"),
    ("084597", "salaries", "verb", "/ˈsæləriz/", "trả lương định kỳ cho"),
    ("084598", "salarying", "verb", "/ˈsæləriɪŋ/", "đang trả lương định kỳ"),
    ("084599", "saleability", "noun", "/ˌseɪləˈbɪlɪti/", "tính dễ bán; giá trị thương mại"),
    ("084600", "salep", "noun", "/ˈsælɛp/", "bột củ lan salep làm đồ uống"),
    ("084601", "saleratus", "noun", "/ˌsælɪˈreɪtəs/", "muối nở natri bicacbonat"),
    ("084602", "salesgirls", "noun", "/ˈseɪlzˌɡɜːrlz/", "nữ nhân viên bán hàng"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r10_raw_p1.json"))
by_id = {r["id"].split(".")[-1]: r for r in raw}
out = []
for sid, hw, pos, ipa, vi in RECORDS:
    rec = dict(by_id[sid])
    assert rec["hw"] == hw, (sid, hw, rec["hw"])
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

json.dump(out, open("scratch/b37_r10_reviewed_p1.json", "w"), ensure_ascii=False, indent=2)
print("b37_r10_p1 saved OK")
