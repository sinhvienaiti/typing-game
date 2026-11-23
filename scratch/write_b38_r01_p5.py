import json

RECORDS = [
    ("085403", "sclerodermatales", "noun", "/ˌsklɪroʊdɜːrməˈteɪliːz/", "bộ Nấm trứng đất"),
    ("085404", "sclerodermatous", "adj", "/ˌsklɪroʊˈdɜːrmətəs/", "có lớp da cứng; có vỏ cứng"),
    ("085405", "sclerogen", "noun", "/ˈsklɪrədʒən/", "chất hóa gỗ thành tế bào"),
    ("085406", "sclerogenic", "adj", "/ˌsklɪrəˈdʒɛnɪk/", "gây xơ cứng; tạo lignin"),
    ("085407", "scleroid", "adj", "/ˈsklɪrɔɪd/", "có cấu trúc xơ cứng như gỗ"),
    ("085408", "scleroma", "noun", "/skləˈroʊmə/", "u xơ cứng niêm mạc mũi họng"),
    ("085409", "sclerometer", "noun", "/skləˈrɑːmɪtər/", "máy đo độ cứng bề mặt vật liệu"),
    ("085410", "scleronomous", "adj", "/skləˈrɑːnəməs/", "không phụ thuộc thời gian (cơ học)"),
    ("085411", "scleropages", "noun", "/skləˈrɑːpədʒiːz/", "chi Cá rồng (Scleropages)"),
    ("085412", "scleroparei", "noun", "/ˌsklɪrəpəˈriːaɪ/", "nhóm cá mù làn má giáp xương"),
    ("085413", "scleroprotein", "noun", "/ˌsklɪroʊˈproʊtiːn/", "protein sợi không tan (sừng, keo)"),
    ("085414", "sclerose", "verb", "/ˈsklɪroʊs/", "làm xơ cứng; trở nên xơ cứng"),
    ("085415", "sclerosed", "adj", "/skləˈroʊzd/", "bị xơ cứng"),
    ("085416", "sclerotica", "noun", "/skləˈrɑːtɪkə/", "củng mạc mắt"),
    ("085417", "sclerotin", "noun", "/ˈsklɪrətɪn/", "protein cứng lớp vỏ côn trùng"),
    ("085418", "sclerotiniaceae", "noun", "/skləˌroʊtɪniˈeɪsiːˌiː/", "họ Nấm hạch Sclerotiniaceae"),
    ("085419", "sclerotitis", "noun", "/ˌsklɪrəˈtaɪtɪs/", "viêm củng mạc mắt"),
    ("085420", "sclerotization", "noun", "/skləˌrɑːtəˈzeɪʃən/", "quá trình hóa cứng vỏ côn trùng"),
    ("085421", "sclerotized", "adj", "/ˈsklɛrəˌtaɪzd/", "đã hóa cứng (lớp vỏ kitin)"),
    ("085422", "sclerotomy", "noun", "/skləˈrɑːtəmi/", "phẫu thuật mở củng mạc mắt"),
    ("085423", "sclerous", "adj", "/ˈsklɪrəs/", "xơ cứng; cứng chắc"),
    ("085424", "sclk", "noun", "/ˌɛsˌsiːˌɛlˈkeɪ/", "đồng hồ tàu vũ trụ (SCLK)"),
    ("085425", "scm", "noun", "/ˌɛsˌsiːˈɛm/", "nữ hộ sinh có chứng chỉ quốc gia"),
    ("085426", "scobicular", "adj", "/skoʊˈbɪkjələr/", "dạng hạt mạt cưa"),
    ("085427", "scobiform", "adj", "/ˈskoʊbɪˌfɔːrm/", "mịn như mạt cưa (hạt nhỏ)"),
    ("085428", "scobs", "noun", "/skɑːbz/", "mạt cưa; mạt giũa kim loại"),
    ("08529", "scoffed", "verb", "/skɔːft/", "đã chế nhạo; đã ăn ngấu nghiến"),
    ("085430", "scoffingly", "adv", "/ˈskɔːfɪŋli/", "một cách chế nhạo khinh miệt"),
    ("085431", "scoffs", "verb", "/skɔːfs/", "chế nhạo; ăn ngấu nghiến"),
    ("085432", "scoke", "noun", "/skoʊk/", "cây thương lục Mỹ"),
    ("085433", "scolded", "verb", "/ˈskoʊldɪd/", "đã la mắng; đã quở trách"),
    ("085434", "scolder", "noun", "/ˈskoʊldər/", "người hay cằn nhằn la mắng"),
    ("085435", "scolds", "verb", "/skoʊldz/", "la mắng; quở trách"),
    ("085436", "scoleces", "noun", "/skoʊˈliːsiːz/", "đầu sán dây"),
    ("085437", "scolex", "noun", "/ˈskoʊlɛks/", "đầu sán dây có giác bám"),
    ("085438", "scolion", "noun", "/ˈskoʊliən/", "bài ca tụng ngâm trong yến tiệc"),
    ("085439", "scoliotic", "adj", "/ˌskoʊliˈɑːtɪk/", "bị chứng vẹo cột sống"),
    ("085440", "scollop", "noun", "/ˈskɑːləp/", "con sò điệp; đường viền lượn sóng"),
    ("085441", "scolopaceous", "adj", "/ˌskɑːləˈpeɪʃəs/", "thuộc họ Chim dẽ"),
    ("085442", "scolopacidae", "noun", "/ˌskɑːləˈpæsɪˌdiː/", "họ Chim dẽ (Scolopacidae)"),
    ("085443", "scolopacine", "adj", "/skəˈlɑːpəˌsaɪn/", "thuộc chim dẽ giun"),
    ("085444", "scolopax", "noun", "/ˈskɑːləˌpæks/", "chi Chim dẽ gà (Scolopax)"),
    ("085445", "scolopendrid", "noun", "/ˌskɑːləˈpɛndrɪd/", "con rết họ Scolopendridae"),
    ("085446", "scolopendrine", "adj", "/ˌskɑːləˈpɛndrən/", "giống con rết; thuộc họ Rết"),
    ("085447", "scolopendrium", "noun", "/ˌskɑːləˈpɛndriəm/", "dương xỉ lưỡi hươu"),
    ("085448", "scolymus", "noun", "/ˈskɑːlɪməs/", "chi cây kế vàng Scolymus"),
    ("085449", "scolytidae", "noun", "/skəˈlɪtɪˌdiː/", "họ Bọ đục vỏ cây"),
    ("085450", "scomberesocidae", "noun", "/ˌskɑːmbɛrɪˈsɑːsɪˌdiː/", "họ Cá thu đao (Scomberesocidae)"),
    ("085451", "scomberesox", "noun", "/skɑːmˈbɛrɪˌsɑːks/", "chi Cá thu đao Đại Tây Dương"),
    ("085452", "scomberomorus", "noun", "/ˌskɑːmbərəˈmɔːrəs/", "chi Cá thu vạch (Scomberomorus)"),
    ("085453", "scombresocidae", "noun", "/ˌskɑːmbrɪˈsɑːsɪˌdiː/", "họ Cá thu đao"),
    ("085454", "scombresox", "noun", "/skɑːmˈbrɛsɑːks/", "chi Cá thu đao"),
    ("085455", "scombridae", "noun", "/ˈskɑːmbrɪˌdiː/", "họ Cá thu ngừ (Scombridae)"),
    ("085456", "scombroidea", "noun", "/skɑːmˈbrɔɪdiə/", "phân bộ Cá thu ngừ"),
    ("085457", "sconces", "noun", "/ˈskɑːnsɪz/", "giá đèn gắn tường; pháo đài nhỏ"),
    ("085458", "scooped", "verb", "/skuːpt/", "đã xúc; đã múc; đã săn tin độc"[:35]),
    ("085459", "scooper", "noun", "/ˈskuːpər/", "cái muôi xúc; người xúc"),
    ("085460", "scoopful", "noun", "/ˈskuːpˌfʊl/", "một muỗng đầy; một xẻng đầy"),
    ("085461", "scooping", "verb", "/ˈskuːpɪŋ/", "đang xúc; đang múc; đang khoét"),
    ("085462", "scoots", "verb", "/skuːts/", "lẻn đi nhanh; phóng vút đi"),
    ("085463", "scooted", "verb", "/ˈskuːtɪd/", "đã lẻn đi nhanh; đã phóng đi"),
    ("085464", "scooting", "verb", "/ˈskuːtɪŋ/", "đang phóng nhanh; đang trượt xe"),
    ("085465", "scoots", "verb", "/skuːts/", "lẻn đi nhanh; trượt xe đẩy"),
    ("085466", "scopa", "noun", "/ˈskoʊpə/", "chùm lông hút phấn hoa (ong)"),
    ("085467", "scopae", "noun", "/ˈskoʊpiː/", "chùm lông hút phấn hoa (ong)"),
    ("085468", "scopal", "adj", "/ˈskoʊpəl/", "thuộc phạm vi"),
    ("085469", "scopate", "adj", "/ˈskoʊpeɪt/", "có chùm lông rậm như bàn chải"),
    ("085470", "scophthalmus", "noun", "/skɑːfˈθælməs/", "chi cá bơn turbot Scophthalmus"),
    ("085471", "scopiform", "adj", "/ˈskoʊpɪˌfɔːrm/", "có hình chổi; dạng chùm lông"),
    ("085472", "scopolia", "noun", "/skoʊˈpoʊliə/", "chi cây cà độc dược Scopolia"),
    ("085473", "scopula", "noun", "/ˈskɑːpjələ/", "chùm lông bám ở chân nhện"),
    ("085474", "scopulate", "adj", "/ˈskɑːpjəˌleɪt/", "có chùm lông hình bàn chải"),
    ("085475", "scorbutic", "adj", "/skɔːrˈbjuːtɪk/", "mắc bệnh còi scorbut"),
    ("085476", "scorbutus", "noun", "/skɔːrˈbjuːtəs/", "bệnh scorbut (thiếu vitamin C)"),
    ("085477", "scorchers", "noun", "/ˈskɔːrtʃərz/", "ngày nắng cháy da; cú đánh cháy sân"[:35]),
    ("085478", "scorches", "verb", "/ˈskɔːrtʃɪz/", "làm cháy xém; thiêu đốt"),
    ("085479", "scorchy", "adj", "/ˈskɔːrtʃi/", "lưu hóa sém quá mức (cao su)"),
    ("085480", "scored", "verb", "/skɔːrd/", "đã ghi điểm; đã khía rãnh"),
    ("085481", "scoriaceous", "adj", "/ˌskɔːriˈeɪʃəs/", "xốp như xỉ núi lửa"),
    ("085482", "scoriae", "noun", "/ˈskɔːriˌiː/", "xỉ núi lửa; xỉ luyện kim"),
    ("085483", "scorification", "noun", "/ˌskɔːrɪfɪˈkeɪʃən/", "quá trình hóa xỉ tách kim loại"),
    ("085484", "scorify", "verb", "/ˈskɔːrəˌfaɪ/", "nấu chảy thành xỉ để tinh luyện"),
    ("085485", "scorning", "verb", "/ˈskɔːrnɪŋ/", "đang khinh bỉ; đang chê bai"),
    ("085486", "scorns", "verb", "/skɔːrnz/", "khinh bỉ; coi thường; chê bai"),
    ("085487", "scorpaena", "noun", "/skɔːrˈpiːnə/", "chi cá mù làn Scorpaena"),
    ("085488", "scorpaenid", "noun", "/skɔːrˈpiːnɪd/", "cá mù làn"),
    ("085489", "scorpaenidae", "noun", "/skɔːrˈpiːnɪˌdiː/", "họ Cá mù làn (Scorpaenidae)"),
    ("085490", "scorpaenoid", "noun", "/skɔːrˈpiːnɔɪd/", "cá thuộc phân bộ Cá mù làn"),
    ("085491", "scorpaenoidea", "noun", "/ˌskɔːrpɪˈnɔɪdiə/", "liên họ Cá mù làn"),
    ("085492", "scorper", "noun", "/ˈskɔːrpər/", "dao khắc gỗ mũi tròn"),
    ("085493", "scorpioid", "adj", "/ˈskɔːrpiˌɔɪd/", "cuộn xoắn như đuôi bọ cạp"),
    ("085494", "scorpionida", "noun", "/ˌskɔːrpiˈɑːnɪdə/", "bộ Bọ cạp (Scorpionida)"),
    ("085495", "scorpionweed", "noun", "/ˈskɔːrpiənˌwiːd/", "cây hoa xoắn chi Phacelia"),
    ("085496", "scorzonera", "noun", "/ˌskɔːrzəˈnɪrə/", "cây rau diếp đen Tây Ban Nha"),
    ("085497", "scotched", "verb", "/skɑːtʃt/", "đã dập tắt; đã chặn đứng; khía"),
    ("085498", "scotches", "verb", "/ˈskɑːtʃɪz/", "dập tắt; ngăn chặn; khía rãnh"),
    ("085499", "scotching", "verb", "/ˈskɑːtʃɪŋ/", "đang dập tắt; đang ngăn chặn"),
    ("085500", "scotchwoman", "noun", "/ˈskɑːtʃˌwʊmən/", "người phụ nữ Scotland"),
    ("085501", "scotia", "noun", "/ˈskoʊʃə/", "đường gờ lõm chân cột"),
    ("085502", "scotice", "adv", "/ˈskɑːtɪsi/", "theo cách nói tiếng Scotland"),
]

# Fix 08529 typo in id, 085462 wrong hw (`scoops`!), and remove slices cleanly
RECORDS[26] = ("085429", "scoffed", "verb", "/skɔːft/", "đã chế nhạo; đã ăn ngấu nghiến")
RECORDS[55] = ("085458", "scooped", "verb", "/skuːpt/", "đã xúc; đã múc; đã săn tin độc")
RECORDS[59] = ("085462", "scoops", "verb", "/skuːps/", "xúc; múc; khoét lỗ")
RECORDS[74] = ("085477", "scorchers", "noun", "/ˈskɔːrtʃərz/", "ngày nắng như thiêu; cú sút mạnh")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r01_raw_p5.json"))
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

json.dump(out, open("scratch/b38_r01_reviewed_p5.json", "w"), ensure_ascii=False, indent=2)
print("b38_r01_p5 saved OK")
