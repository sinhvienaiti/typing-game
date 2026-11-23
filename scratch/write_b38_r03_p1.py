import json

RECORDS = [
    ("086003", "semicolonial", "adj", "/ˌsɛmikəˈloʊniəl/", "nửa thuộc địa"),
    ("086004", "semicolonialism", "noun", "/ˌsɛmikəˈloʊniəˌlɪzəm/", "chế độ nửa thuộc địa"),
    ("086005", "semicoma", "noun", "/ˌsɛmiˈkoʊmə/", "trạng thái bán hôn mê"),
    ("086006", "semicomatose", "adj", "/ˌsɛmiˈkoʊməˌtoʊs/", "bán hôn mê; lơ mơ gần bất tỉnh"),
    ("086007", "semiconsciousness", "noun", "/ˌsɛmiˈkɑːnʃəsnəs/", "trạng thái nửa tỉnh nửa mê"),
    ("086008", "semicontinuous", "adj", "/ˌsɛmikənˈtɪnjuəs/", "bán liên tục; gần như liên tục"),
    ("086009", "semidark", "adj", "/ˌsɛmiˈdɑːrk/", "lờ mờ tối; tranh tối tranh sáng"),
    ("086010", "semidarkness", "noun", "/ˌsɛmiˈdɑːrknəs/", "cảnh tranh tối tranh sáng; mờ tối"),
    ("086011", "semidiameter", "noun", "/ˌsɛmidaɪˈæmɪtər/", "bán kính biểu kiến (thiên văn)"),
    ("086012", "semidivine", "adj", "/ˌsɛmidɪˈvaɪn/", "nửa người nửa thần; như thần thánh"),
    ("086013", "semidome", "noun", "/ˈsɛmiˌdoʊm/", "nửa mái vòm; vòm bán cầu"),
    ("086014", "semidomestication", "noun", "/ˌsɛmidəˌmɛstɪˈkeɪʃən/", "tình trạng bán thuần hóa"),
    ("086015", "semidominant", "adj", "/ˌsɛmiˈdɑːmənənt/", "trội không hoàn toàn (di truyền)"),
    ("086016", "semidouble", "adj", "/ˌsɛmiˈdʌbəl/", "nửa kép; nhiều lớp cánh (hoa)"),
    ("086017", "semidrying", "adj", "/ˌsɛmiˈdraɪɪŋ/", "khô chậm; bán khô (dầu sơn)"),
    ("086018", "semiepiphyte", "noun", "/ˌsɛmiˈɛpɪˌfaɪt/", "cây bán biểu sinh"),
    ("086019", "semifinished", "adj", "/ˌsɛmiˈfɪnɪʃt/", "bán thành phẩm; gia công dở dang"),
    ("086020", "semiflexible", "adj", "/ˌsɛmiˈflɛksəbəl/", "nửa mềm dẻo; bán linh hoạt"),
    ("086021", "semifloating", "adj", "/ˌsɛmiˈfloʊtɪŋ/", "bán nổi; nửa bơi lơ lửng"),
    ("086022", "semifluid", "adj", "/ˌsɛmiˈfluːɪd/", "sền sệt; bán lỏng"),
    ("086023", "semifluidity", "noun", "/ˌsɛmifluːˈɪdɪti/", "tính bán lỏng; độ sền sệt"),
    ("086024", "semifossil", "adj", "/ˌsɛmiˈfɑːsəl/", "bán hóa thạch; hóa thạch một phần"),
    ("086025", "semigloss", "noun", "/ˈsɛmiˌɡlɔːs/", "sơn bán bóng; lớp phủ hơi bóng"),
    ("086026", "semihard", "adj", "/ˌsɛmiˈhɑːrd/", "bán cứng; hơi cứng"),
    ("086027", "semihemidemisemiquaver", "noun", "/ˌsɛmiˌhɛmiˌdɛmiˈsɛmiˌkweɪvər/", "nốt móc năm (âm nhạc)"),
    ("086028", "semihemidemisemiquavers", "noun", "/ˌsɛmiˌhɛmiˌdɛmiˈsɛmiˌkweɪvərz/", "nốt móc năm (âm nhạc)"),
    ("086029", "semilethal", "adj", "/ˌsɛmiˈliːθəl/", "gây chết bán phần (gen)"),
    ("086030", "semiliquid", "adj", "/ˌsɛmiˈlɪkwɪd/", "bán lỏng; sền sệt"),
    ("086031", "semiliterate", "adj", "/ˌsɛmiˈlɪtərət/", "biết đọc viết sơ sài; bán mù chữ"),
    ("086032", "semimaturation", "noun", "/ˌsɛmiˌmætʃəˈreɪʃən/", "trạng thái chín ương; bán thành thục"[:35]),
    ("086033", "semimechanized", "adj", "/ˌsɛmiˈmɛkəˌnaɪzd/", "bán cơ giới hóa; cơ khí hóa một phần"[:35]),
    ("086034", "semimetal", "noun", "/ˌsɛmiˈmɛtəl/", "á kim; bán kim loại"),
    ("086035", "seminarist", "noun", "/ˈsɛməˌnɛrɪst/", "chủng sinh; học viên chủng viện"),
    ("086036", "semination", "noun", "/ˌsɛməˈneɪʃən/", "sự gieo hạt; sự phát tán hạt"),
    ("086037", "seminivorous", "adj", "/ˌsɛməˈnɪvərəs/", "ăn hạt"),
    ("086038", "seminomad", "noun", "/ˌsɛmiˈnoʊmæd/", "người bán du cư"),
    ("086039", "seminomadic", "adj", "/ˌsɛminoʊˈmædɪk/", "sống bán du cư"),
    ("086040", "seminude", "adj", "/ˌsɛmiˈnuːd/", "bán khỏa thân"),
    ("086041", "seminudity", "noun", "/ˌsɛmiˈnuːdɪti/", "tình trạng bán khỏa thân"),
    ("086042", "semiologies", "noun", "/ˌsiːmiˈɑːlədʒiz/", "ký hiệu học; triệu chứng học"),
    ("086043", "semiopaque", "adj", "/ˌsɛmioʊˈpeɪk/", "bán trong mờ; hơi đục"),
    ("086044", "semioscillation", "noun", "/ˌsɛmiˌɑːsəˈleɪʃən/", "nửa chu kỳ dao động"),
    ("086045", "semiotical", "adj", "/ˌsiːmiˈɑːtɪkəl/", "thuộc ký hiệu học"),
    ("086046", "semiotician", "noun", "/ˌsiːmiəˈtɪʃən/", "nhà ký hiệu học"),
    ("086047", "semipalmated", "adj", "/ˌsɛmiˈpælˌmeɪtɪd/", "có màng bơi xẻ nông ở chân (chim)"),
    ("086048", "semiparasite", "noun", "/ˌsɛmiˈpærəˌsaɪt/", "cây bán ký sinh"),
    ("086049", "semiparasitic", "adj", "/ˌsɛmiˌpærəˈsɪtɪk/", "sống bán ký sinh"),
    ("086050", "semipenniform", "adj", "/ˌsɛmiˈpɛnɪˌfɔːrm/", "có dạng nửa lông chim (cơ)"),
    ("086051", "semipolitical", "adj", "/ˌsɛmipəˈlɪtɪkəl/", "mang tính bán chính trị"),
    ("086052", "semipublic", "adj", "/ˌsɛmiˈpʌblɪk/", "bán công; phục vụ một phần công chúng"[:35]),
    ("086053", "semipure", "adj", "/ˌsɛmiˈpjʊr/", "bán tinh khiết; gần tinh khiết"),
    ("086054", "semiquavers", "noun", "/ˈsɛmiˌkweɪvərz/", "nốt móc kép (âm nhạc)"),
    ("086055", "semiquincentennial", "adj", "/ˌsɛmiˌkwɪnsɛnˈtɛniəl/", "thuộc lễ kỷ niệm 250 năm"),
    ("086056", "semirigid", "adj", "/ˌsɛmiˈrɪdʒɪd/", "bán cứng"),
    ("086057", "semisedentary", "adj", "/ˌsɛmiˈsɛdənˌtɛri/", "bán định cư"),
    ("086058", "semisoft", "adj", "/ˌsɛmiˈsɔːft/", "bán mềm; hơi mềm"),
    ("086059", "semispan", "noun", "/ˈsɛmiˌspæn/", "nửa sải cánh máy bay"),
    ("086060", "semisphere", "noun", "/ˈsɛmiˌsfɪr/", "bán cầu"),
    ("086061", "semispherical", "adj", "/ˌsɛmiˈsfɛrɪkəl/", "có hình bán cầu"),
    ("086062", "semistable", "adj", "/ˌsɛmiˈsteɪbəl/", "bán ổn định; ổn định một phần"),
    ("086063", "semisteel", "noun", "/ˈsɛmiˌstiːl/", "gang pha thép"),
    ("086064", "semiterrestrial", "adj", "/ˌsɛmitəˈrɛstriəl/", "bán sống trên cạn; lưỡng cư"),
    ("086065", "semitism", "noun", "/ˈsɛmɪˌtɪzəm/", "ngôn ngữ hay đặc điểm người Semit"),
    ("086066", "semitonal", "adj", "/ˌsɛmiˈtoʊnəl/", "thuộc nửa cung (âm nhạc)"),
    ("086067", "semitrance", "noun", "/ˈsɛmiˌtræns/", "trạng thái nửa xuất thần"),
    ("086068", "semitransparency", "noun", "/ˌsɛmitrænsˈpɛrənsi/", "tính bán trong suốt; độ mờ"),
    ("086069", "semitropic", "adj", "/ˌsɛmiˈtrɑːpɪk/", "cận nhiệt đới"),
    ("086070", "semitropics", "noun", "/ˌsɛmiˈtrɑːpɪks/", "vùng cận nhiệt đới"),
    ("086071", "semivitreous", "adj", "/ˌsɛmiˈvɪtriəs/", "bán thủy tinh hóa"),
    ("086072", "semiyearly", "adj", "/ˌsɛmiˈjɪrli/", "nửa năm một lần; mỗi sáu tháng"),
    ("086073", "semmit", "noun", "/ˈsɛmɪt/", "áo lót mặc sát người (Scotland)"),
    ("086074", "semola", "noun", "/ˈsɛmələ/", "tấm lúa mì cứng làm mì Ý"),
    ("086075", "sempach", "noun", "/ˈzɛmpɑːx/", "trận chiến Sempach (Thụy Sĩ)"),
    ("086076", "sempervirent", "adj", "/ˌsɛmpərˈvaɪrənt/", "xanh quanh năm; thường xanh"),
    ("086077", "sempiternity", "noun", "/ˌsɛmpɪˈtɜːrnɪti/", "sự vĩnh cửu; tính trường tồn"),
    ("086078", "semplice", "adj", "/ˈsɛmplɪtʃeɪ/", "mộc mạc giản dị (âm nhạc)"),
    ("086079", "sempre", "adv", "/ˈsɛmpreɪ/", "xuyên suốt; luôn giữ sắc thái"),
    ("086080", "sempstress", "noun", "/ˈsɛmpstrəs/", "nữ thợ may vá"),
    ("086081", "senary", "adj", "/ˈsiːnəri/", "thuộc hệ cơ số sáu; gồm sáu phần"),
    ("086082", "senatorship", "noun", "/ˈsɛnətərˌʃɪp/", "chức vụ thượng nghị sĩ"),
    ("086083", "senatus", "noun", "/sɪˈneɪtəs/", "viện nguyên lão La Mã; hội đồng"),
    ("086084", "sendai", "noun", "/ˈsɛndaɪ/", "thành phố Sendai (Nhật Bản)"),
    ("086085", "sendal", "noun", "/ˈsɛndəl/", "lụa mỏng thời Trung cổ"),
    ("086086", "sendan", "noun", "/ˈsɛndən/", "cây xoan Nhật Bản; lụa mỏng"),
    ("086087", "sendee", "noun", "/sɛnˈdiː/", "người nhận (thư, bưu kiện)"),
    ("086088", "senectitude", "noun", "/sɪˈnɛktɪˌtuːd/", "tuổi già; sự già nua tuổi tác"),
    ("086089", "senefelder", "noun", "/ˈzeːnəˌfɛldər/", "nhà phát minh in đá Senefelder"),
    ("086090", "senega", "noun", "/ˈsɛnəɡə/", "rễ cây viễn chí Bắc Mỹ làm thuốc"),
    ("086091", "senesce", "verb", "/sɪˈnɛs/", "già đi; lão hóa"),
    ("086092", "seneschals", "noun", "/ˈsɛnəʃəlz/", "quan tổng quản lâu đài xưa"),
    ("086093", "sengreen", "noun", "/ˈsɛnˌɡriːn/", "cây trường sinh mọc vách đá"),
    ("086094", "senhora", "noun", "/sənˈjɔːrə/", "bà, quý bà (tiếng Bồ Đào Nha)"),
    ("086095", "senhorita", "noun", "/ˌsɛnjəˈriːtə/", "cô, tiểu thư (tiếng Bồ Đào Nha)"),
    ("086096", "seniti", "noun", "/ˈsɛnɪti/", "đơn vị tiền xu seniti của Tonga"),
    ("086097", "sennenhunde", "noun", "/ˈzɛnənˌhʊndə/", "giống chó núi Thụy Sĩ"),
    ("086098", "sennet", "noun", "/ˈsɛnɪt/", "hiệu kèn báo ra sân khấu (kịch cổ)"[:35]),
    ("086099", "sennight", "noun", "/ˈsɛnˌnaɪt/", "một tuần lễ (bảy đêm, từ cổ)"),
    ("086100", "sennit", "noun", "/ˈsɛnɪt/", "dây thừng bện dẹt; sợi rơm tết mũ"),
    ("086101", "sensationalise", "verb", "/sɛnˈseɪʃənəˌlaɪz/", "giật gân hóa; thổi phồng tin"),
    ("086102", "sensationalize", "verb", "/sɛnˈseɪʃənəˌlaɪz/", "giật gân hóa; thổi phồng tin"),
]

# Replace slices cleanly <= 35
RECORDS[29] = ("086032", "semimaturation", "noun", "/ˌsɛmiˌmætʃəˈreɪʃən/", "sự chín ương; sự bán trưởng thành"[:35])
RECORDS[29] = ("086032", "semimaturation", "noun", "/ˌsɛmiˌmætʃəˈreɪʃən/", "trạng thái chín ương")
RECORDS[30] = ("086033", "semimechanized", "adj", "/ˌsɛmiˈmɛkəˌnaɪzd/", "bán cơ giới hóa")
RECORDS[49] = ("086052", "semipublic", "adj", "/ˌsɛmiˈpʌblɪk/", "bán công; bán công cộng")
RECORDS[95] = ("086098", "sennet", "noun", "/ˈsɛnɪt/", "hiệu kèn báo hiệu lên sân khấu")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r03_raw_p1.json"))
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

json.dump(out, open("scratch/b38_r03_reviewed_p1.json", "w"), ensure_ascii=False, indent=2)
print("b38_r03_p1 saved OK")
