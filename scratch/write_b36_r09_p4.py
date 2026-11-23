import json

records = [
    ("079303", "procrastinating", "verb", "/prəˈkræstəˌneɪtɪŋ/", "trì hoãn, lần lữa, chần chừ"),
    ("079304", "procrastinations", "noun", "/prəˌkræstəˈneɪʃənz/", "sự trì hoãn, thói lần lữa"),
    ("079305", "procrastinative", "adj", "/prəˈkræstəˌneɪtɪv/", "hay trì hoãn, chần chừ, lần lữa"),
    ("079306", "procrastinatory", "adj", "/prəˈkræstənəˌtɔːri/", "nhằm trì hoãn, mang tính câu giờ"),
    ("079307", "procreant", "adj", "/ˈproʊkriənt/", "có khả năng sinh sản, sinh sôi"),
    ("079308", "procreated", "verb", "/ˈproʊkriˌeɪtɪd/", "đã sinh sản, đã sinh sôi nảy nở"),
    ("079309", "procreates", "verb", "/ˈproʊkriˌeɪts/", "sinh sản, truyền giống, sinh sôi"),
    ("079310", "procreating", "verb", "/ˈproʊkriˌeɪtɪŋ/", "sinh sản, truyền giống, sinh sôi"),
    ("079311", "procreativeness", "noun", "/ˈproʊkriˌeɪtɪvnəs/", "khả năng sinh sản, sức sinh sôi"),
    ("079312", "procreator", "noun", "/ˈproʊkriˌeɪtər/", "người sinh thành, đấng tạo hóa"),
    ("079313", "procrypsis", "noun", "/proʊˈkrɪpsɪs/", "khả năng ngụy trang (sinh vật)"),
    ("079314", "procryptic", "adj", "/proʊˈkrɪptɪk/", "có màu sắc ngụy trang (sinh vật)"),
    ("079315", "proctal", "adj", "/ˈprɑːktəl/", "thuộc hậu môn, vùng trực tràng"),
    ("079316", "proctalgia", "noun", "/prɑːkˈtældʒə/", "chứng đau trực tràng (y học)"),
    ("079317", "proctocele", "noun", "/ˈprɑːktəˌsiːl/", "chứng sa trực tràng (y học)"),
    ("079318", "proctodeae", "noun", "/ˌprɑːktəˈdiːiː/", "các ống hậu môn phôi thai"),
    ("079319", "proctodeum", "noun", "/ˌprɑːktəˈdiːəm/", "ống hậu môn phôi thai (phôi học)"),
    ("079320", "proctologic", "adj", "/ˌprɑːktəˈlɑːdʒɪk/", "thuộc hậu môn trực tràng học"),
    ("079321", "proctological", "adj", "/ˌprɑːktəˈlɑːdʒɪkəl/", "thuộc hậu môn trực tràng học"),
    ("079322", "proctoplasty", "noun", "/ˈprɑːktəˌplæsti/", "phẫu thuật tạo hình hậu môn"),
    ("079323", "proctored", "verb", "/ˈprɑːktərd/", "đã coi thi, đã giám sát phòng thi"),
    ("079324", "proctorial", "adj", "/prɑːkˈtɔːriəl/", "thuộc giám thị đại học"),
    ("079325", "proctoring", "verb", "/ˈprɑːktərɪŋ/", "coi thi, giám sát phòng thi"),
    ("079326", "proctorize", "verb", "/ˈprɑːktəˌraɪz/", "áp dụng kỷ luật giám thị (đại học)"),
    ("079327", "proctors", "verb", "/ˈprɑːktərz/", "coi thi, giám sát kỳ thi"),
    ("079328", "proctorship", "noun", "/ˈprɑːktərʃɪp/", "chức vụ giám thị đại học"),
    ("079329", "proctoscope", "noun", "/ˈprɑːktəˌskoʊp/", "ống soi trực tràng (y học)"),
    ("079330", "proctoscopic", "adj", "/ˌprɑːktəˈskɑːpɪk/", "thuộc nội soi trực tràng"),
    ("079331", "proctoscopy", "noun", "/prɑːkˈtɑːskəpi/", "thủ thuật soi trực tràng (y học)"),
    ("079332", "procural", "noun", "/prəˈkjʊrəl/", "sự kiếm được, sự thu xếp được"),
    ("079333", "procurance", "noun", "/prəˈkjʊrəns/", "sự thu mua, sự kiếm được"),
    ("079334", "procurancy", "noun", "/prəˈkjʊrənsi/", "sự thay mặt, chức vụ đại diện"),
    ("079335", "procuration", "noun", "/ˌprɑːkjəˈreɪʃən/", "giấy ủy quyền; sự thu mua"),
    ("079336", "procuratorial", "adj", "/ˌprɑːkjərəˈtɔːriəl/", "thuộc công tố viên, ủy quyền"),
    ("079337", "procuratory", "noun", "/prəˈkjʊrəˌtɔːri/", "giấy ủy quyền, giấy ủy nhiệm"),
    ("079338", "procured", "verb", "/prəˈkjʊrd/", "đã kiếm được, đã mua sắm được"),
    ("079339", "procures", "verb", "/prəˈkjʊrz/", "kiếm được, mua sắm, thu xếp được"),
    ("079340", "procuring", "verb", "/prəˈkjʊrɪŋ/", "kiếm được, mua sắm, thu xếp"),
    ("079341", "procurvation", "noun", "/ˌproʊkɜːrˈveɪʃən/", "sự uốn cong về phía trước"),
    ("079342", "procyclidine", "noun", "/proʊˈsaɪklɪdiːn/", "thuốc trị Parkinson procyclidine"),
    ("079343", "procyonid", "noun", "/proʊˈsaɪənɪd/", "loài thú họ Gấu mèo"),
    ("079344", "procyonidae", "noun", "/ˌproʊsaɪˈɑːnɪˌdiː/", "họ Gấu mèo (động vật học)"),
    ("079345", "prodded", "verb", "/ˈprɑːdɪd/", "đã chọc, đã thúc giục"),
    ("079346", "prodder", "noun", "/ˈprɑːdər/", "người thúc giục; dụng cụ chọc"),
    ("079347", "prodelision", "noun", "/ˌproʊdɪˈlɪʒən/", "sự tỉnh lược nguyên âm đầu (ngữ âm)"),
    ("079348", "prodigalise", "verb", "/ˈprɑːdɪɡəˌlaɪz/", "tiêu xài hoang phí, phung phí"),
    ("079349", "prodigalize", "verb", "/ˈprɑːdɪɡəˌlaɪz/", "tiêu xài hoang phí, phung phí"),
    ("079350", "prodigiousness", "noun", "/prəˈdɪdʒəsnəs/", "sự phi thường, kích thước khổng lồ"),
    ("079351", "proding", "noun", "/ˈprɑːdɪŋ/", "sự chọc, sự thúc giục (biến thể)"),
    ("079352", "prodition", "noun", "/prəˈdɪʃən/", "sự phản bội, tội phản nghịch (cổ)"),
    ("079353", "proditor", "noun", "/ˈprɑːdɪtər/", "kẻ phản bội, tên phản nghịch (cổ)"),
    ("079354", "prodome", "noun", "/ˈproʊdoʊm/", "sách dẫn nhập; tiền triệu (y học)"),
    ("079355", "prodroma", "noun", "/prəˈdroʊmə/", "tiền triệu, triệu chứng báo trước"),
    ("079356", "prodromic", "adj", "/proʊˈdrɑːmɪk/", "thuộc tiền triệu, báo trước bệnh"),
    ("079357", "prods", "verb", "/prɑːdz/", "chọc, thúc mạnh; thúc giục"),
    ("079358", "produceable", "adj", "/prəˈduːsəbəl/", "có thể sản xuất được, chế tạo được"),
    ("079359", "produced", "verb", "/prəˈduːst/", "đã sản xuất, tạo ra; đã xuất trình"),
    ("079360", "producers", "noun", "/prəˈduːsərz/", "nhà sản xuất, hãng sản xuất"),
    ("079361", "produces", "verb", "/prəˈduːsɪz/", "sản xuất, tạo ra; xuất trình"),
    ("079362", "producibility", "noun", "/prəˌduːsəˈbɪləti/", "khả năng sản xuất được"),
    ("079363", "producible", "adj", "/prəˈduːsəbəl/", "có thể sản xuất, chế tạo được"),
    ("079364", "producing", "verb", "/prəˈduːsɪŋ/", "sản xuất, tạo ra; xuất trình"),
    ("079365", "productible", "adj", "/prəˈdʌktəbəl/", "có thể sản xuất được (cổ)"),
    ("079366", "productile", "adj", "/prəˈdʌktəl/", "có thể kéo dài, uốn dài được"),
    ("079367", "productional", "adj", "/prəˈdʌkʃənəl/", "thuộc sản xuất, mang tính sản xuất"),
    ("079368", "productionist", "noun", "/prəˈdʌkʃənɪst/", "người theo chủ trương tăng sản xuất"),
    ("079369", "productions", "noun", "/prəˈdʌkʃənz/", "sự sản xuất; các tác phẩm, vở diễn"),
    ("079370", "proem", "noun", "/ˈproʊɛm/", "lời tựa, lời mở đầu tác phẩm"),
    ("079371", "proembryo", "noun", "/proʊˈɛmbrioʊ/", "tiền phôi, phôi sơ khai"),
    ("079372", "proemial", "adj", "/proʊˈiːmiəl/", "mở đầu, dẫn nhập (tác phẩm)"),
    ("079373", "proenzyme", "noun", "/proʊˈɛnzaɪm/", "tiền enzym, chất tiền men"),
    ("079374", "proepimeron", "noun", "/ˌproʊɛˈpɪmərɑːn/", "mảnh bên ngực trước (côn trùng)"),
    ("079375", "proepimerum", "noun", "/ˌproʊɛˈpɪmərəm/", "mảnh bên ngực trước (côn trùng)"),
    ("079376", "proestrum", "noun", "/proʊˈɛstrəm/", "giai đoạn trước động dục"),
    ("079377", "profanations", "noun", "/ˌprɑːfəˈneɪʃənz/", "những hành vi báng bổ, xúc phạm"),
    ("079378", "profanatory", "adj", "/prəˈfænəˌtɔːri/", "báng bổ, xúc phạm thần thánh"),
    ("079379", "profaneness", "noun", "/prəˈfeɪnnəs/", "thái độ báng bổ, lời nói tục tĩu"),
    ("079380", "profaner", "noun", "/prəˈfeɪnər/", "kẻ báng bổ, người làm ô uế"),
    ("079381", "profanes", "verb", "/prəˈfeɪnz/", "báng bổ, xúc phạm, làm ô uế"),
    ("079382", "profaning", "verb", "/prəˈfeɪnɪŋ/", "báng bổ, xúc phạm, làm ô uế"),
    ("079383", "professes", "verb", "/prəˈfɛsɪz/", "tuyên bố, thừa nhận; hành nghề"),
    ("079384", "professionalized", "verb", "/prəˈfɛʃənəˌlaɪzd/", "đã chuyên nghiệp hóa"),
    ("079385", "professionalizes", "verb", "/prəˈfɛʃənəˌlaɪzɪz/", "chuyên nghiệp hóa"),
    ("079386", "professionalizing", "verb", "/prəˈfɛʃənəˌlaɪzɪŋ/", "chuyên nghiệp hóa"),
    ("079387", "professions", "noun", "/prəˈfɛʃənz/", "các nghề nghiệp; lời tuyên xưng"),
    ("079388", "professorate", "noun", "/prəˈfɛsərət/", "đội ngũ giáo sư; chức giáo sư"),
    ("079389", "professorially", "adv", "/ˌprɑːfəˈsɔːriəli/", "theo kiểu giáo sư, ra vẻ thầy giáo"),
    ("079390", "professoriate", "noun", "/ˌprɑːfəˈsɔːriət/", "giới giáo sư, hội đồng giáo sư"),
    ("079391", "professors", "noun", "/prəˈfɛsərz/", "các giáo sư đại học"),
    ("079392", "proffered", "verb", "/ˈprɑːfərd/", "đã đề nghị, đã ngỏ lời trao tặng"),
    ("079393", "profferer", "noun", "/ˈprɑːfərər/", "người đề nghị, người trao tặng"),
    ("079394", "proffering", "verb", "/ˈprɑːfərɪŋ/", "đề nghị, ngỏ lời, trao tặng"),
    ("079395", "proffers", "verb", "/ˈprɑːfərz/", "đề nghị, ngỏ lời, trao tặng"),
    ("079396", "proficience", "noun", "/prəˈfɪʃəns/", "sự thành thạo, trình độ tinh thông"),
    ("079397", "proficients", "noun", "/prəˈfɪʃənts/", "những người thành thạo, bậc thầy"),
    ("079398", "profiled", "verb", "/ˈproʊfaɪld/", "đã phác họa; đã lập hồ sơ"),
    ("079399", "profiles", "verb", "/ˈproʊfaɪlz/", "phác họa mặt nghiêng; lập hồ sơ"),
    ("079400", "profilist", "noun", "/ˈproʊfaɪlɪst/", "họa sĩ vẽ chân dung nhìn nghiêng"),
    ("079401", "profilograph", "noun", "/proʊˈfaɪləˌɡræf/", "máy ghi biên dạng bề mặt"),
    ("079402", "profilometer", "noun", "/ˌproʊfəˈlɑːmɪtər/", "máy đo độ nhám bề mặt"),
]

raw = json.load(open("scratch/b36_r09_raw_p4.json"))
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
with open("scratch/b36_r09_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b36_r09_p4 saved OK")
