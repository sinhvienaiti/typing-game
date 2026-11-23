import json

records = [
    ("080503", "pupilise", "verb", "/ˈpjuːpəˌlaɪz/", "nhận làm học trò; dạy kèm (Anh)"),
    ("080504", "pupilize", "verb", "/ˈpjuːpəˌlaɪz/", "nhận làm học trò; dạy kèm"),
    ("080505", "pupillage", "noun", "/ˈpjuːpəlɪdʒ/", "thời kỳ tập sự; tuổi vị thành niên"),
    ("080506", "pupillarity", "noun", "/ˌpjuːpəˈlærəti/", "tuổi vị thành niên (luật Scotland)"),
    ("080507", "pupillise", "verb", "/ˈpjuːpəˌlaɪz/", "nhận làm học trò; dạy kèm (Anh)"),
    ("080508", "pupilometer", "noun", "/ˌpjuːpəˈlɑːmɪtər/", "dụng cụ đo đường kính đồng tử"),
    ("080509", "pupils", "noun", "/ˈpjuːpəlz/", "học sinh, học trò; con ngươi mắt"),
    ("080510", "pupilship", "noun", "/ˈpjuːpəlʃɪp/", "thân phận học trò, thời làm đệ tử"),
    ("080511", "pupiparous", "adj", "/pjʊˈpɪpərəs/", "đẻ ấu trùng sắp hóa nhộng (ruồi)"),
    ("080512", "pupivorous", "adj", "/pjʊˈpɪvərəs/", "ăn nhộng, ký sinh trên nhộng"),
    ("080513", "pupoid", "adj", "/ˈpjuːpɔɪd/", "có hình dạng giống con nhộng"),
    ("080514", "pupped", "verb", "/pʌpt/", "đã đẻ con (chó, cáo, hải cẩu)"),
    ("080515", "puppetoon", "noun", "/ˌpʌpəˈtuːn/", "phim hoạt hình rối tĩnh vật"),
    ("080516", "puppets", "noun", "/ˈpʌpɪts/", "những con rối; kẻ bù nhìn"),
    ("080517", "pupping", "verb", "/ˈpʌpɪŋ/", "đẻ con (chó, cáo, hải cẩu)"),
    ("080518", "puppyboys", "noun", "/ˈpʌpiˌbɔɪz/", "những chàng trai trẻ nông nổi"),
    ("080519", "puppygirls", "noun", "/ˈpʌpiˌɡɜːrlz/", "những cô gái trẻ tinh nghịch"),
    ("080520", "puppyish", "adj", "/ˈpʌpiɪʃ/", "như cún con; trẻ con, tự phụ"),
    ("080521", "puppyism", "noun", "/ˈpʌpiˌɪzəm/", "thói hợm hĩnh rỗng tuếch (cổ)"),
    ("080522", "puppylike", "adj", "/ˈpʌpiˌlaɪk/", "như cún con, tinh nghịch bám người"),
    ("080523", "pups", "verb", "/pʌps/", "đẻ con (chó, cáo, hải cẩu)"),
    ("080524", "purace", "noun", "/pʊˈrɑːseɪ/", "núi lửa Puracé (Colombia)"),
    ("080525", "purau", "noun", "/ˈpuːraʊ/", "cây tra biển, bụp biển (Polynesia)"),
    ("080526", "purblindly", "adv", "/ˈpɜːrˌblaɪndli/", "lờ mờ, cận nặng; thiển cận"),
    ("080527", "purblindness", "noun", "/ˈpɜːrˌblaɪndnəs/", "tình trạng mắt kém; sự thiển cận"),
    ("080528", "purchasability", "noun", "/ˌpɜːrtʃəsəˈbɪləti/", "tính mua được; tính dễ bị mua chuộc"),
    ("080529", "purchased", "verb", "/ˈpɜːrtʃəst/", "đã mua, đã tậu được"),
    ("080530", "purchases", "verb", "/ˈpɜːrtʃəsɪz/", "mua, mua sắm; đạt được bằng nỗ lực"),
    ("080531", "pureblooded", "adj", "/ˈpjʊrˌblʌdɪd/", "thuần chủng, dòng dõi thuần nhất"),
    ("080532", "pureed", "verb", "/pjʊˈreɪd/", "đã xay nhuyễn, đã nghiền nhừ"),
    ("080533", "pureeing", "verb", "/pjʊˈreɪɪŋ/", "xay nhuyễn, nghiền nhừ (thức ăn)"),
    ("080534", "purees", "verb", "/pjʊˈreɪz/", "xay nhuyễn, nghiền nhừ (thực phẩm)"),
    ("080535", "purfle", "noun", "/ˈpɜːrfəl/", "đường viền trang trí (đàn violin)"),
    ("080536", "purgas", "noun", "/ˈpɜːrɡəz/", "các loại thuốc tẩy xổ mạnh (cũ)"),
    ("080537", "purged", "verb", "/pɜːrdʒd/", "đã thanh lọc, tẩy sạch, thanh trừng"),
    ("080538", "purger", "noun", "/ˈpɜːrdʒər/", "người thanh trừng; thuốc tẩy xổ"),
    ("080539", "purges", "verb", "/ˈpɜːrdʒɪz/", "thanh lọc, tẩy sạch; thanh trừng"),
    ("080540", "purifications", "noun", "/ˌpjʊrəfəˈkeɪʃənz/", "sự tinh chế, sự làm sạch, tẩy uế"),
    ("080541", "purificatory", "adj", "/pjʊˈrɪfəkəˌtɔːri/", "để làm sạch, nhằm tẩy uế thanh lọc"),
    ("080542", "purified", "verb", "/ˈpjʊrəˌfaɪd/", "đã tinh chế, đã lọc sạch, tẩy uế"),
    ("080543", "purifies", "verb", "/ˈpjʊrəˌfaɪz/", "tinh chế, lọc sạch, thanh tẩy"),
    ("080544", "purinethol", "noun", "/pjʊˈriːnəˌθɔːl/", "thuốc trị bạch cầu mercaptopurine"),
    ("080545", "puristic", "adj", "/pjʊˈrɪstɪk/", "thuần túy chủ nghĩa, câu nệ chữ"),
    ("080546", "puristical", "adj", "/pjʊˈrɪstɪkəl/", "mang tính thuần túy chủ nghĩa"),
    ("080547", "puristically", "adv", "/pjʊˈrɪstɪkli/", "theo lối thuần túy chủ nghĩa"),
    ("080548", "puritanic", "adj", "/ˌpjʊrəˈtænɪk/", "khắc khổ, câu nệ đạo đức Thanh giáo"),
    ("080549", "puritanically", "adv", "/ˌpjʊrəˈtænɪkli/", "một cách khắc khổ, khắt khe đạo đức"),
    ("080550", "puritanicalness", "noun", "/ˌpjʊrəˈtænɪkəlnəs/", "tính khắc khổ, sự khắt khe đạo đức"),
    ("080551", "purled", "verb", "/pɜːrld/", "đã đan mũi xuống; đã chảy róc rách"),
    ("080552", "purler", "noun", "/ˈpɜːrlər/", "cú ngã nhào chúi đầu (khẩu ngữ)"),
    ("080553", "purlin", "noun", "/ˈpɜːrlɪn/", "thanh xà gồ mái nhà (xây dựng)"),
    ("080554", "purling", "verb", "/ˈpɜːrlɪŋ/", "đan mũi xuống; chảy róc rách êm ái"),
    ("080555", "purloined", "verb", "/pɜːrˈlɔɪnd/", "đã ăn cắp, đã cuỗm mất"),
    ("080556", "purloiner", "noun", "/pɜːrˈlɔɪnər/", "kẻ trộm cắp, kẻ cuỗm đồ"),
    ("080557", "purloining", "verb", "/pɜːrˈlɔɪnɪŋ/", "ăn cắp, lấy trộm, cuỗm đi"),
    ("080558", "purloins", "verb", "/pɜːrˈlɔɪnz/", "ăn cắp, lấy trộm, cuỗm đi"),
    ("080559", "purloo", "noun", "/pɜːrˈluː/", "cơm hầm thịt kiểu miền Nam Mỹ"),
    ("080560", "purls", "verb", "/pɜːrlz/", "đan mũi xuống; chảy róc rách; xoáy"),
    ("080561", "purparty", "noun", "/ˈpɜːrˌpɑːrti/", "phần tài sản được chia (luật cổ)"),
    ("080562", "purpleness", "noun", "/ˈpɜːrpəlnəs/", "sắc tím, màu đỏ tía"),
    ("080563", "purply", "adj", "/ˈpɜːrpli/", "hơi tím, tim tím, có sắc tía"),
    ("080564", "purpoint", "noun", "/ˈpɜːrpɔɪnt/", "áo giáp chần bông thời Trung cổ"),
    ("080565", "purported", "adj", "/pərˈpɔːrtɪd/", "được cho là, được đồn đại là"),
    ("080566", "purposelessly", "adv", "/ˈpɜːrpəsləsli/", "một cách vô định, không mục đích"),
    ("080567", "purposively", "adv", "/ˈpɜːrpəsɪvli/", "có chủ đích, có mục đích rõ ràng"),
    ("080568", "purposiveness", "noun", "/ˈpɜːrpəsɪvnəs/", "tính có chủ đích, hướng mục tiêu"),
    ("080569", "purpresture", "noun", "/pɜːrˈprɛstʃər/", "tội lấn chiếm đất công (luật cổ)"),
    ("080570", "purpuraceous", "adj", "/ˌpɜːrpjʊˈreɪʃəs/", "có màu đỏ tía, sắc tím thẫm"),
    ("080571", "purpurate", "verb", "/ˈpɜːrpjəˌreɪt/", "nhuộm màu đỏ tía; chuyển sang tía"),
    ("080572", "purpureal", "adj", "/pɜːrˈpjʊriəl/", "đỏ tía thẫm; thuộc ban xuất huyết"),
    ("080573", "purpuric", "adj", "/pɜːrˈpjʊrɪk/", "thuộc bệnh ban xuất huyết (y học)"),
    ("080574", "purred", "verb", "/pɜːrd/", "đã kêu gừ gừ (mèo); đã chạy êm ru"),
    ("080575", "purree", "noun", "/pʊˈriː/", "bột màu vàng Ấn Độ (purree)"),
    ("080576", "purring", "verb", "/ˈpɜːrɪŋ/", "kêu gừ gừ (mèo); nổ máy êm ru"),
    ("080577", "purrs", "verb", "/pɜːrz/", "kêu gừ gừ (mèo); chạy êm (động cơ)"),
    ("080578", "pursang", "adv", "/pʊrˈsɑːŋ/", "thuần chủng, dòng máu thuần (Pháp)"),
    ("080579", "pursed", "verb", "/pɜːrst/", "đã mím (môi), đã chu môi; nhăn lại"),
    ("080580", "purses", "verb", "/ˈpɜːrsɪz/", "mím (môi), chu môi; thắt túm lại"),
    ("080581", "pursiness", "noun", "/ˈpɜːrsinəs/", "chứng thở dốc; dáng béo phệ bệu"),
    ("080582", "pursing", "verb", "/ˈpɜːrsɪŋ/", "mím (môi), chu môi, thắt túm lại"),
    ("080583", "pursuable", "adj", "/pərˈsuːəbəl/", "có thể truy đuổi, có thể theo đuổi"),
    ("080584", "pursual", "noun", "/pərˈsuːəl/", "sự truy đuổi, sự theo đuổi mục tiêu"),
    ("080585", "pursuers", "noun", "/pərˈsuːərz/", "những kẻ truy đuổi, người đuổi theo"),
    ("080586", "pursues", "verb", "/pərˈsuːz/", "truy đuổi; theo đuổi, tiến hành"),
    ("080587", "pursuivant", "noun", "/ˈpɜːrswɪvənt/", "quan truyền lệnh cấp dưới; tùy tùng"),
    ("080588", "pursy", "adj", "/ˈpɜːrsi/", "thở hổn hển khò khè; béo phệ"),
    ("080589", "purtenance", "noun", "/ˈpɜːrtənəns/", "bộ lòng thú (tim, gan, phổi - cổ)"),
    ("080590", "purulence", "noun", "/ˈpjʊrələns/", "tình trạng mưng mủ, chất mủ"),
    ("080591", "purulency", "noun", "/ˈpjʊrələnsi/", "tình trạng mưng mủ, chứng sinh mủ"),
    ("080592", "purulently", "adv", "/ˈpjʊrələntli/", "trong tình trạng mưng mủ, đầy mủ"),
    ("080593", "purveyors", "noun", "/pərˈveɪərz/", "nhà cung cấp thực phẩm, hàng hóa"),
    ("080594", "puseyism", "noun", "/ˈpjuːziˌɪzəm/", "phong trào cải cách Anh giáo Pusey"),
    ("080595", "pushan", "noun", "/ˈpuːʃən/", "thần mặt trời Pushan (Ấn Độ giáo)"),
    ("080596", "pushball", "noun", "/ˈpʊʃˌbɔːl/", "môn thể thao đẩy bóng khổng lồ"),
    ("080597", "pushed", "verb", "/pʊʃt/", "đã đẩy, đã xô; đã thúc đẩy, ép buộc"),
    ("080598", "pushes", "verb", "/ˈpʊʃɪz/", "đẩy, xô; thúc đẩy, nài ép"),
    ("080599", "pushful", "adj", "/ˈpʊʃfəl/", "năng nổ, xông xáo; thích áp đặt"),
    ("080600", "pushily", "adv", "/ˈpʊʃɪli/", "một cách xông xáo, sỗ sàng áp đặt"),
    ("080601", "pushingly", "adv", "/ˈpʊʃɪŋli/", "theo kiểu thúc ép, sỗ sàng xông xáo"),
    ("080602", "pushkinology", "noun", "/ˌpʊʃkɪˈnɑːlədʒi/", "ngành nghiên cứu nhà thơ Pushkin"),
]

raw = json.load(open("scratch/b37_r02_raw_p1.json"))
by_id = {f"lex.en.200k.{r[0]}": r for r in records}
out = []
for orig in raw:
    sid, hw, pos, ipa, vi = by_id[orig["id"]]
    assert orig["hw"] == hw, f"{orig['id']}: {orig['hw']} vs {hw}"
    assert 0 < len(vi) <= 35, f"{sid} {hw} len={len(vi)}: {vi}"
    assert "/" not in vi, f"{sid} {hw} slash in vi"
    assert ipa.count("/") == 2 and not ipa.startswith("/ ") and not ipa.endswith(" /"), f"{sid} {hw} bad ipa"
    orig["pos"] = pos
    orig["ipa"] = ipa
    orig["vi"] = vi
    orig["status"] = "reviewed"
    out.append(orig)

assert len(out) == 100
with open("scratch/b37_r02_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r02_p1 saved OK")
