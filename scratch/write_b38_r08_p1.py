import json

RECORDS = [
    ("088503", "speedo", "noun", "/ˈspiːdoʊ/", "đồng hồ tốc độ; quần bơi bó"),
    ("088504", "speedomiter", "noun", "/spiːˈdɑːmɪtər/", "đồng hồ đo tốc độ; công-tơ-mét"),
    ("088505", "speedster", "noun", "/ˈspiːdstər/", "tay đua tốc độ; xe hơi thể thao"),
    ("088506", "speiss", "noun", "/spaɪs/", "xỉ luyện quặng asenua kim loại"),
    ("088507", "spelaean", "adj", "/spɪˈliːən/", "thuộc hang động; sống trong hang"),
    ("088508", "spelaelogical", "adj", "/ˌspiːliəˈlɑːdʒɪkəl/", "thuộc hang động học"),
    ("088509", "spelaelogy", "noun", "/ˌspiːliˈɑːlədʒi/", "ngành hang động học"),
    ("088510", "spelaeologist", "noun", "/ˌspiːliˈɑːlədʒɪst/", "nhà nghiên cứu hang động"),
    ("088511", "spelaeology", "noun", "/ˌspiːliˈɑːlədʒi/", "hang động học"),
    ("088512", "speleological", "adj", "/ˌspiːliəˈlɑːdʒɪkəl/", "thuộc hang động học"),
    ("088513", "speleologist", "noun", "/ˌspiːliˈɑːlədʒɪst/", "nhà thám hiểm nghiên cứu hang động"),
    ("088514", "spelicans", "noun", "/ˈspɛlɪkənz/", "trò chơi rút que; que chơi"),
    ("088515", "spellbind", "verb", "/ˈspɛlˌbaɪnd/", "mê hoặc; làm say đắm lòng người"),
    ("088516", "spelldown", "noun", "/ˈspɛlˌdaʊn/", "cuộc thi đánh vần loại trực tiếp"),
    ("088517", "spelled", "verb", "/spɛld/", "đã đánh vần; đã báo hiệu; đổi ca"),
    ("088518", "spellers", "noun", "/ˈspɛlərz/", "người đánh vần; sách dạy đánh vần"),
    ("088519", "spellings", "noun", "/ˈspɛlɪŋz/", "chính tả; cách đánh vần từ"),
    ("088520", "spells", "verb", "/spɛlz/", "đánh vần; có nghĩa là; thay phiên"),
    ("088521", "spelunk", "verb", "/spɪˈlʌŋk/", "thám hiểm hang động"),
    ("088522", "spelunking", "noun", "/spɪˈlʌŋkɪŋ/", "hoạt động thám hiểm hang động"),
    ("088523", "spencerian", "adj", "/spɛnˈsɪriən/", "thuộc triết lý Herbert Spencer"),
    ("088524", "spencerianism", "noun", "/spɛnˈsɪriəˌnɪzəm/", "học thuyết tiến hóa xã hội Spencer"),
    ("088525", "spencerism", "noun", "/ˈspɛnsəˌrɪzəm/", "triết lý của Herbert Spencer"),
    ("088526", "spergula", "noun", "/ˈspɜːrɡjələ/", "chi cỏ Spergula (họ Cẩm chướng)"),
    ("088527", "spergularia", "noun", "/ˌspɜːrɡjəˈlɛriə/", "chi cỏ muối biển Spergularia"),
    ("088528", "spermagonium", "noun", "/ˌspɜːrməˈɡoʊniəm/", "túi chứa tinh tử (nấm rỉ)"),
    ("088529", "spermaphore", "noun", "/ˈspɜːrməˌfɔːr/", "giá noãn (thực vật học)"),
    ("088530", "spermaphyte", "noun", "/ˈspɜːrməˌfaɪt/", "thực vật có hạt"),
    ("088531", "spermary", "noun", "/ˈspɜːrməri/", "tinh hoàn; tuyến sinh tinh"),
    ("088532", "spermatheca", "noun", "/ˌspɜːrməˈθiːkə/", "túi chứa tinh trùng (côn trùng)"),
    ("088533", "spermatid", "noun", "/ˈspɜːrmətɪd/", "tiền tinh trùng; tinh tử"),
    ("088534", "spermatium", "noun", "/spɜːrˈmeɪʃəm/", "tinh tử; giao tử đực bất động"),
    ("088535", "spermatocele", "noun", "/spɜːrˈmætəˌsiːl/", "u nang mào tinh hoàn"),
    ("088536", "spermatocide", "noun", "/spɜːrˈmætəˌsaɪd/", "chất diệt tinh trùng"),
    ("088537", "spermatocyte", "noun", "/spɜːrˈmætəˌsaɪt/", "tinh bào"),
    ("088538", "spermatogenetic", "adj", "/spɜːrˌmætoʊdʒəˈnɛtɪk/", "sinh tinh trùng; tạo tinh trùng"),
    ("088539", "spermatogenous", "adj", "/ˌspɜːrməˈtɑːdʒənəs/", "sản sinh tinh trùng"),
    ("088540", "spermatogonium", "noun", "/spɜːrˌmætəˈɡoʊniəm/", "tinh nguyên bào"),
    ("088541", "spermatological", "adj", "/ˌspɜːrmətəˈlɑːdʒɪkəl/", "thuộc tinh trùng học"),
    ("088542", "spermatologist", "noun", "/ˌspɜːrməˈtɑːlədʒɪst/", "nhà nghiên cứu tinh trùng học"),
    ("088543", "spermatology", "noun", "/ˌspɜːrməˈtɑːlədʒi/", "tinh trùng học"),
    ("088544", "spermatophore", "noun", "/spɜːrˈmætəˌfɔːr/", "túi tinh trùng (mực, giáp xác)"),
    ("088545", "spermatophyta", "noun", "/ˌspɜːrməˈtɑːfɪtə/", "ngành Thực vật có hạt"),
    ("088546", "spermatophyte", "noun", "/spɜːrˈmætəˌfaɪt/", "thực vật có hạt"),
    ("088547", "spermatophytes", "noun", "/spɜːrˈmætəˌfaɪts/", "thực vật có hạt"),
    ("088548", "spermatorrhea", "noun", "/spɜːrˌmætəˈriːə/", "chứng di tinh"),
    ("088549", "spermatorrhoea", "noun", "/spɜːrˌmætəˈriːə/", "chứng di tinh"),
    ("088550", "spermatozoa", "noun", "/ˌspɜːrmətəˈzoʊə/", "tinh trùng"),
    ("088551", "spermatozoal", "adj", "/ˌspɜːrmətəˈzoʊəl/", "thuộc tinh trùng"),
    ("088552", "spermatozoan", "noun", "/ˌspɜːrmətəˈzoʊən/", "tế bào tinh trùng"),
    ("088553", "spermatozoid", "noun", "/spɜːrˈmætəˌzɔɪd/", "tinh trùng; giao tử đực di động"),
    ("088554", "spermic", "adj", "/ˈspɜːrmɪk/", "thuộc tinh dịch; thuộc tinh trùng"),
    ("088555", "spermicidol", "adj", "/ˈspɜːrməˌsaɪdəl/", "diệt tinh trùng"),
    ("088556", "spermid", "noun", "/ˈspɜːrmɪd/", "tinh tử; tiền tinh trùng"),
    ("088557", "spermiducal", "adj", "/ˌspɜːrmɪˈduːkəl/", "thuộc ống dẫn tinh"),
    ("088558", "spermiduct", "noun", "/ˈspɜːrmɪˌdʌkt/", "ống dẫn tinh"),
    ("088559", "spermin", "noun", "/ˈspɜːrmɪn/", "hợp chất hữu cơ spermin"),
    ("088560", "spermine", "noun", "/ˈspɜːrˌmiːn/", "chất sinh học spermin"),
    ("088561", "spermiogenesis", "noun", "/ˌspɜːrmioʊˈdʒɛnəsɪs/", "quá trình biệt hóa thành tinh trùng"),
    ("088562", "spermogonial", "adj", "/ˌspɜːrməˈɡoʊniəl/", "thuộc túi tinh tử của nấm"),
    ("088563", "spermogonium", "noun", "/ˌspɜːrməˈɡoʊniəm/", "túi bào tử đực (nấm, địa y)"),
    ("088564", "spermological", "adj", "/ˌspɜːrməˈlɑːdʒɪkəl/", "thuộc tinh trùng học; hạt giống"),
    ("088565", "spermologist", "noun", "/spɜːrˈmɑːlədʒɪst/", "nhà nghiên cứu hạt hay tinh trùng"),
    ("088566", "spermology", "noun", "/spɜːrˈmɑːlədʒi/", "hạt học; tinh trùng học"),
    ("088567", "spermophile", "noun", "/ˈspɜːrməˌfaɪl/", "sóc đất ăn hạt"),
    ("088568", "spermophyte", "noun", "/ˈspɜːrməˌfaɪt/", "thực vật có hạt"),
    ("088569", "spermous", "adj", "/ˈspɜːrməs/", "thuộc tinh trùng; giống tinh dịch"),
    ("088570", "sperrylife", "noun", "/ˈspɛrɪˌlaɪt/", "khoáng vật bạch kim sperrylit"),
    ("088571", "spessartine", "noun", "/ˈspɛsərˌtiːn/", "đá ngọc hồng lựu spessartin"),
    ("088572", "spessartite", "noun", "/ˈspɛsərˌtaɪt/", "đá ngọc hồng lựu spessartit"),
    ("088573", "spewed", "verb", "/spjuːd/", "đã phun ra; đã nôn mửa; tuôn trào"),
    ("088574", "spewer", "noun", "/ˈspjuːər/", "người phun ra; người nôn mửa"),
    ("088575", "spewing", "verb", "/ˈspjuːɪŋ/", "đang phun trào; đang nôn mửa"),
    ("088576", "spews", "verb", "/spjuːz/", "phun trào; nôn mửa; tuôn ra"),
    ("088577", "sphacelate", "verb", "/ˈsfæsəˌleɪt/", "bị hoại tử; làm thối hoại mô"),
    ("088578", "sphacelation", "noun", "/ˌsfæsəˈleɪʃən/", "sự hoại tử mô"),
    ("088579", "sphacele", "noun", "/ˈsfæsəliː/", "chi cây họ Hoa môi Sphacele"),
    ("088580", "sphacelotheca", "noun", "/ˌsfæsəloʊˈθiːkə/", "chi nấm than hại ngũ cốc"),
    ("088581", "sphacelus", "noun", "/ˈsfæsələs/", "mảng mô hoại tử; chứng hoại thư"),
    ("088582", "sphaeralcea", "noun", "/sfɪˈrælsiə/", "chi cẩm quỳ sa mạc Sphaeralcea"),
    ("088583", "sphaeriaceae", "noun", "/ˌsfɪriˈeɪsiːˌiː/", "họ Nấm túi cầu Sphaeriaceae"),
    ("088584", "sphaeriales", "noun", "/ˌsfɪriˈeɪliːz/", "bộ Nấm túi cầu Sphaeriales"),
    ("088585", "sphaerobolaceae", "noun", "/ˌsfɪroʊboʊˈleɪsiːˌiː/", "họ Nấm bắn bào tử như đạn pháo"),
    ("088586", "sphaerocarpaceae", "noun", "/ˌsfɪroʊkɑːrˈpeɪsiːˌiː/", "họ Rêu tản cầu Sphaerocarpaceae"),
    ("088587", "sphaerocarpales", "noun", "/ˌsfɪroʊkɑːrˈpeɪliːz/", "bộ Rêu tản cầu Sphaerocarpales"),
    ("088588", "sphaerocarpos", "noun", "/ˌsfɪroʊˈkɑːrpəs/", "chi Rêu tản chai Sphaerocarpos"),
    ("088589", "sphaerocarpus", "noun", "/ˌsfɪroʊˈkɑːrpəs/", "chi Rêu tản chai Sphaerocarpus"),
    ("088590", "sphagna", "noun", "/ˈsfæɡnə/", "rêu nước; rêu than bùn"),
    ("088591", "sphagnales", "noun", "/sfæɡˈneɪliːz/", "bộ Rêu than bùn (Sphagnales)"),
    ("088592", "sphecidae", "noun", "/ˈsfɛsɪˌdiː/", "họ Ong tò vò đào hang (Sphecidae)"),
    ("088593", "sphecius", "noun", "/ˈsfiːʃəs/", "chi ong bắp cày săn ve sầu"),
    ("088594", "sphecoid", "noun", "/ˈsfiːkɔɪd/", "ong bắp cày đơn độc họ Sphecidae"),
    ("088595", "sphecoidea", "noun", "/sfɪˈkɔɪdiə/", "liên họ Ong tò vò Sphecoidea"),
    ("088596", "sphecotheres", "noun", "/ˌsfɛkəˈθɪriːz/", "chi chim vàng anh ăn sung Úc"),
    ("088597", "sphene", "noun", "/sfiːn/", "khoáng vật titanit (sphene)"),
    ("088598", "sphenic", "adj", "/ˈsfiːnɪk/", "có hình cái nêm"),
    ("088599", "sphenion", "noun", "/ˈsfiːniɑːn/", "điểm đỉnh góc trước xương đỉnh"),
    ("088600", "spheniscidae", "noun", "/sfɪˈnɪsɪˌdiː/", "họ Chim cánh cụt (Spheniscidae)"),
    ("088601", "sphenisciformes", "noun", "/sfɪˌnɪsɪˈfɔːrmiːz/", "bộ Chim cánh cụt"),
    ("088602", "spheniscus", "noun", "/sfɪˈnɪskəs/", "chi Chim cánh cụt đới ôn hòa"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r08_raw_p1.json"))
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

json.dump(out, open("scratch/b38_r08_reviewed_p1.json", "w"), ensure_ascii=False, indent=2)
print("b38_r08_p1 saved OK")
