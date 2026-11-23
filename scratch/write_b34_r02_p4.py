import json

items = [
    ("065803", "hematologists", "noun", "/ˌhiːməˈtɒlədʒɪsts/", "bác sĩ chuyên khoa huyết học"),
    ("065804", "hierarches", "noun", "/ˈhaɪəˌrɑːrks/", "giáo chủ; người đứng đầu phẩm trật"),
    ("065805", "hirelings", "noun", "/ˈhaɪərlɪŋz/", "kẻ làm thuê vì tiền; lính đánh thuê"),
    ("065806", "hyaluronidases", "noun", "/ˌhaɪəljʊˈrɒnɪˌdeɪsɪz/", "enzym phân giải axit hyaluronic"),
    ("065807", "hyphenations", "noun", "/ˌhaɪfəˈneɪʃənz/", "cách ngắt dòng bằng dấu gạch nối"),
    ("065808", "ileostomies", "noun", "/ˌɪliˈɒstəmiz/", "phẫu thuật mở thông hồi tràng"),
    ("065809", "illogics", "noun", "/ɪˈlɒdʒɪks/", "sự phi lý; lập luận thiếu logic"),
    ("065810", "ingrains", "verb", "/ɪnˈɡreɪnz/", "khắc sâu; ăn sâu vào tâm trí"),
    ("065811", "isomerases", "noun", "/aɪˈsɒməˌreɪsɪz/", "enzym xúc tác đồng phân hóa"),
    ("065812", "justiciaries", "noun", "/dʒʌˈstɪʃiˌɛriz/", "thẩm phán tối cao thời phong kiến"),
    ("065813", "ladogas", "noun", "/ˈlɑːdəɡəz/", "hồ nước ngọt Ladoga ở Nga"),
    ("065814", "lathis", "noun", "/ˈlɑːtiz/", "gậy tre bọc sắt của cảnh sát Ấn"),
    ("065815", "leibnitzes", "noun", "/ˈlaɪbnɪtsɪz/", "nhà toán học triết học Leibniz"),
    ("065816", "lockmans", "noun", "/ˈlɒkmənz/", "người gác cửa âu thuyền"),
    ("065817", "magnetons", "noun", "/ˈmæɡnɪˌtɒnz/", "đơn vị mô-men từ lượng tử magneton"),
    ("065818", "markoffs", "noun", "/ˈmɑːrkɒfs/", "nhà toán học Nga Andrey Markov"),
    ("065819", "minuits", "noun", "/mɪnˈwiːz/", "thống đốc Hà Lan Peter Minuit"),
    ("065820", "miscues", "noun", "/mɪsˈkjuːz/", "cú thọc bi trượt; sai sót nhỏ"),
    ("065821", "mutineers", "noun", "/ˌmjuːtəˈnɪərz/", "kẻ nổi loạn chống chỉ huy trên tàu"),
    ("065822", "myrdals", "noun", "/ˈmɪərdɑːlz/", "nhà kinh tế học Thụy Điển Myrdal"),
    ("065823", "neoplatonisms", "noun", "/ˌniːoʊˈpleɪtəˌnɪzəmz/", "triết học Tân Platon cổ đại"),
    ("065824", "netminders", "noun", "/ˈnɛtˌmaɪndərz/", "thủ môn khúc côn cầu trên băng"),
    ("065825", "nonmembers", "noun", "/nɒnˈmɛmbərz/", "người không phải thành viên hội"),
    ("065826", "nucleoli", "noun", "/nuːˈkliːəˌlaɪ/", "hạch nhân bên trong nhân tế bào"),
    ("065827", "nurserymen", "noun", "/ˈnɜːrsərimən/", "người trồng và bán cây giống"),
    ("065828", "palatabilities", "noun", "/ˌpælətəˈbɪlɪtiz/", "vị ngon miệng của thức ăn"),
    ("065829", "pallidums", "noun", "/ˈpælɪdəmz/", "cầu nhạt trong hạch nền não bộ"),
    ("065830", "palpitations", "noun", "/ˌpælpɪˈteɪʃənz/", "triệu chứng tim đập nhanh mạnh"),
    ("065831", "perfectas", "noun", "/pərˈfɛktəz/", "vé cược đoán đúng hai ngựa về đầu"),
    ("065832", "pheochromocytomas", "noun", "/ˌfiːoʊˌkroʊmoʊsaɪˈtoʊməz/", "khối u tủy tuyến thượng thận"),
    ("065833", "photiuses", "noun", "/ˈfoʊʃəsɪz/", "Thượng phụ Photios I xứ Byzantium"),
    ("065834", "pietisms", "noun", "/ˈpaɪɪˌtɪzəmz/", "phong trào Sùng đạo Tin Lành Đức"),
    ("065835", "pluperfects", "noun", "/ˌpluːˈpɜːrfɪkts/", "thì quá khứ hoàn thành (ngữ pháp)"),
    ("065836", "polygonums", "noun", "/pəˈlɪɡənəmz/", "cây rau răm; cây nghể chi Polygonum"),
    ("065837", "qadis", "noun", "/ˈkɑːdiz/", "thẩm phán tòa án luật Hồi giáo"),
    ("065838", "repoted", "verb", "/riːˈpɒtɪd/", "đã sang chậu cây (biến thể)"),
    ("065839", "repoting", "verb", "/riːˈpɒtɪŋ/", "đang sang chậu cây (biến thể)"),
    ("065840", "repots", "verb", "/riːˈpɒts/", "chuyển cây sang chậu trồng mới"),
    ("065841", "repotted", "verb", "/riːˈpɒtɪd/", "đã chuyển cây sang chậu mới"),
    ("065842", "repotting", "verb", "/riːˈpɒtɪŋ/", "đang chuyển cây sang chậu mới"),
    ("065843", "reshes", "noun", "/ˈrɛʃɪz/", "chữ cái Do Thái và Phênixi resh"),
    ("065844", "rictuses", "noun", "/ˈrɪktəsɪz/", "miệng há ngoác; nụ cười nhăn mặt"),
    ("065845", "rollerbladed", "verb", "/ˈroʊlərˌbleɪdɪd/", "đã trượt giày patin một hàng bánh"),
    ("065846", "rollerblades", "noun", "/ˈroʊlərˌbleɪdz/", "giày trượt patin một hàng bánh"),
    ("065847", "scagged", "verb", "/skæɡd/", "đã làm rách xước; làm hỏng"),
    ("065848", "scagging", "verb", "/ˈskæɡɪŋ/", "đang làm rách xước; làm hỏng"),
    ("065849", "scags", "noun", "/skæɡz/", "vết rách xước; chất cấm hêrôin"),
    ("065850", "scheeles", "noun", "/ˈʃeɪləz/", "nhà hóa học Thụy Điển Scheele"),
    ("065851", "scholias", "noun", "/ˈskoʊliəz/", "lời chú giải cổ văn bên lề sách"),
    ("065852", "seamier", "adj", "/ˈsiːmiər/", "bẩn thỉu hơn; tệ nạn nhơ nhớp hơn"),
    ("065853", "seamiest", "adj", "/ˈsiːmiɪst/", "bẩn thỉu nhất; tệ nạn nhơ nhớp nhất"),
    ("065854", "seeders", "noun", "/ˈsiːdərz/", "máy gieo hạt; người gieo hạt"),
    ("065855", "sheikhas", "noun", "/ˈʃeɪkəz/", "vợ hoặc nữ quý tộc tù trưởng Ả Rập"),
    ("065856", "shoemakings", "noun", "/ˈʃuːˌmeɪkɪŋz/", "nghề đóng giày dép thủ công"),
    ("065857", "spermicides", "noun", "/ˈspɜːrmɪˌsaɪdz/", "chất diệt tinh trùng tránh thai"),
    ("065858", "spitballs", "noun", "/ˈspɪtˌbɔːlz/", "viên giấy nhai ướt bắn trêu đùa"),
    ("065859", "stragglier", "adj", "/ˈstræɡliər/", "mọc lan lộn xộn hơn; xộc xệch hơn"),
    ("065860", "straggliest", "adj", "/ˈstræɡliɪst/", "mọc lan lộn xộn nhất; xộc xệch nhất"),
    ("065861", "suspensories", "noun", "/səˈspɛnsəriz/", "băng treo nâng đỡ dùng trong y tế"),
    ("065862", "tallgrasses", "noun", "/ˈtɔːlˌɡræsɪz/", "cỏ cao mọc ở thảo nguyên"),
    ("065863", "tapenades", "noun", "/ˌtæpəˈnɑːdz/", "xốt ô liu nghiền tapenade Pháp"),
    ("065864", "teaspoonfuls", "noun", "/ˈtiːspuːnˌfʊlz/", "lượng đong đầy một thìa cà phê"),
    ("065865", "teratomas", "noun", "/ˌtɛrəˈtoʊməz/", "u quái chứa nhiều loại mô cơ thể"),
    ("065866", "tetchier", "adj", "/ˈtɛtʃiər/", "dễ cáu kỉnh hơn; hay hờn dỗi hơn"),
    ("065867", "tetchiest", "adj", "/ˈtɛtʃiɪst/", "dễ cáu kỉnh nhất; hay hờn dỗi nhất"),
    ("065868", "tetragrammatons", "noun", "/ˌtɛtrəˈɡræməˌtɒnz/", "tên Chúa bốn chữ YHWH Do Thái"),
    ("065869", "thorazines", "noun", "/ˈθɔːrəˌziːnz/", "thuốc an thần trị loạn thần"),
    ("065870", "tiepolos", "noun", "/tiˈɛpəloʊz/", "họa sĩ Rococo Ý Giovanni Tiepolo"),
    ("065871", "tocantinses", "noun", "/ˌtoʊkənˈtiːnzɪz/", "sông Tocantins chảy ở Brazil"),
    ("065872", "tombolas", "noun", "/ˈtɒmbələz/", "trò chơi quay số trúng thưởng"),
    ("065873", "tribologies", "noun", "/traɪˈbɒlədʒiz/", "khoa học ma sát và mài mòn học"),
    ("065874", "twofers", "noun", "/ˈtuːfərz/", "ưu đãi mua hai món giá bằng một"),
    ("065875", "unreasons", "noun", "/ʌnˈriːzənz/", "sự phi lý; hành động thiếu lý trí"),
    ("065876", "washerwomen", "noun", "/ˈwɒʃərˌwɪmən/", "người phụ nữ làm nghề giặt thuê"),
    ("065877", "wayfarings", "noun", "/ˈweɪˌfɛərɪŋz/", "chuyến đi bộ hành trình đường xa"),
    ("065878", "wedeled", "verb", "/ˈveɪdəld/", "đã trượt tuyết lượn vòng ngắn"),
    ("065879", "wedeling", "verb", "/ˈveɪdəlɪŋ/", "đang trượt tuyết lượn vòng ngắn"),
    ("065880", "wedels", "verb", "/ˈveɪdəlz/", "trượt tuyết lượn vòng ngắn đều"),
    ("065881", "whackos", "noun", "/ˈwækoʊz/", "kẻ lập dị kỳ quặc (khẩu ngữ)"),
    ("065882", "acid anhydrides", "phrase", "/ˈæsɪd ænˈhaɪdraɪdz/", "hợp chất anhiđrit axit"),
    ("065883", "acute pyelonephritis", "phrase", "/əˈkjuːt ˌpaɪəloʊnəˈfraɪtɪs/", "bệnh viêm thận bể thận cấp tính"),
    ("065884", "anemone cylindrica", "phrase", "/əˈnɛməni sɪˈlɪndrɪkə/", "cây cỏ chân ngỗng nến Bắc Mỹ"),
    ("065885", "antifouling paint", "phrase", "/ˌæntiˈfaʊlɪŋ peɪnt/", "sơn chống hà bám thân tàu biển"),
    ("065886", "athanasian creed", "phrase", "/ˌæθəˈneɪʒən kriːd/", "Kinh Tin Kính Athanasius"),
    ("065887", "bastardy proceeding", "phrase", "/ˈbæstərdi prəˈsiːdɪŋ/", "vụ kiện xác nhận cha cho con"),
    ("065888", "bombyx mori", "phrase", "/ˈbɒmbɪks ˈmɔːri/", "con tằm ăn lá dâu nhả tơ"),
    ("065889", "carl von linne", "phrase", "/kɑːrl fɒn lɪˈneɪ/", "nhà phân loại học Carl von Linné"),
    ("065890", "cassia alata", "phrase", "/ˈkæsiə əˈleɪtə/", "cây muồng trâu chữa bệnh ngoài da"),
    ("065891", "childe hassam", "phrase", "/tʃaɪld ˈhæsəm/", "họa sĩ ấn tượng Mỹ Childe Hassam"),
    ("065892", "chronic pyelonephritis", "phrase", "/ˈkrɒnɪk ˌpaɪəloʊnəˈfraɪtɪs/", "bệnh viêm thận bể thận mạn tính"),
    ("065893", "corticospinal tract", "phrase", "/ˌkɔːrtɪkoʊˈspaɪnəl trækt/", "bó vỏ-tủy sống; bó tháp thần kinh"),
    ("065894", "crocodilian reptile", "phrase", "/ˌkrɒkəˈdɪliən ˈrɛptaɪl/", "bò sát thuộc bộ Cá sấu"),
    ("065895", "cuneate leaf", "phrase", "/ˈkjuːnieɪt liːf/", "lá cây có gốc hình nêm thuôn"),
    ("065896", "eccrine gland", "phrase", "/ˈɛkraɪn ɡlænd/", "tuyến mồ hôi ngoại tiết eccrine"),
    ("065897", "el misti", "phrase", "/ɛl ˈmɪsti/", "núi lửa El Misti ở Peru"),
    ("065898", "euphorbia medusae", "phrase", "/juːˈfɔːrbiə mɪˈdjuːsiː/", "cây xương rồng đầu rắn Medusa"),
    ("065899", "fall armyworm", "phrase", "/fɔːl ˈɑːrmiˌwɜːrm/", "sâu keo mùa thu hại ngô lúa"),
    ("065900", "family canidae", "phrase", "/ˈfæməli ˈkænɪdiː/", "họ Chó gồm chó sói và cáo"),
    ("065901", "flagellated protozoan", "phrase", "/ˈflædʒəˌleɪtɪd ˌproʊtəˈzoʊən/", "động vật nguyên sinh có roi bơi"),
    ("065902", "fly agaric", "phrase", "/flaɪ ˈæɡərɪk/", "nấm độc tán đỏ chấm trắng"),
]

with open("scratch/b34_r02_raw_p4.json") as f:
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

with open("scratch/b34_r02_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r02_p4.json OK")
