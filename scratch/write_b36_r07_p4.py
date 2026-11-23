import json

rows = [
    ("078303", "pouches", "verb", "/ˈpaʊtʃɪz/", "nhét vào túi; làm phồng như túi"),
    ("078304", "pouching", "verb", "/ˈpaʊtʃɪŋ/", "nhét vào túi; làm phồng như túi"),
    ("078305", "pouchlike", "adj", "/ˈpaʊtʃlaɪk/", "có hình dạng giống chiếc túi"),
    ("078306", "pouchy", "adj", "/ˈpaʊtʃi/", "có túi; phồng xệ xuống như túi"),
    ("078307", "poudrette", "noun", "/puːˈdrɛt/", "phân bón khô chế biến từ phân bắc"),
    ("078308", "poudrin", "noun", "/ˈpuːdrɪn/", "bụi băng kim li ti (tinh thể băng)"),
    ("078309", "poulette", "noun", "/puːˈlɛt/", "nước sốt kem nấm poulette (Pháp)"),
    ("078310", "poulp", "noun", "/puːlp/", "con bạch tuộc (từ cổ)"),
    ("078311", "poulpe", "noun", "/puːlp/", "con bạch tuộc (từ cổ)"),
    ("078312", "poult", "noun", "/poʊlt/", "gà giò, vịt giò, gà tây non"),
    ("078313", "poulterer", "noun", "/ˈpoʊltərər/", "người buôn bán gia cầm"),
    ("078314", "poulterers", "noun", "/ˈpoʊltərərz/", "người buôn bán gia cầm"),
    ("078315", "poulticed", "verb", "/ˈpoʊltɪst/", "đã đắp thuốc cao lên vết thương"),
    ("078316", "poultices", "verb", "/ˈpoʊltɪsɪz/", "đắp thuốc cao lên vết thương"),
    ("078317", "poulticing", "verb", "/ˈpoʊltɪsɪŋ/", "đắp thuốc cao lên vết thương"),
    ("078318", "poultries", "noun", "/ˈpoʊltriz/", "gia cầm; thịt gia cầm"),
    ("078319", "poultryman", "noun", "/ˈpoʊltrimən/", "người chăn nuôi hoặc bán gia cầm"),
    ("078320", "poults", "noun", "/poʊlts/", "gà giò, gà tây non"),
    ("078321", "pounced", "verb", "/paʊnst/", "đã vồ lấy, chộp lấy bất ngờ"),
    ("078322", "pouncer", "noun", "/ˈpaʊnsər/", "kẻ vồ chụp; túi rắc bột phấn"),
    ("078323", "pounces", "verb", "/ˈpaʊnsɪz/", "vồ lấy, chộp lấy bất ngờ"),
    ("078324", "pouncing", "verb", "/ˈpaʊnsɪŋ/", "vồ lấy, chộp lấy bất ngờ"),
    ("078325", "poundal", "noun", "/ˈpaʊndəl/", "đơn vị lực poundal (hệ Anh-Mỹ)"),
    ("078326", "pounded", "verb", "/ˈpaʊndɪd/", "đã giã nát; nện thình thịch; đập"),
    ("078327", "pounds", "verb", "/paʊndz/", "giã nát; nện thình thịch; đập mạnh"),
    ("078328", "pourboire", "noun", "/pʊrˈbwɑːr/", "tiền boa, tiền thưởng thêm (Pháp)"),
    ("078329", "poured", "verb", "/pɔːrd/", "đã rót, đổ, trút xuống"),
    ("078330", "pourparler", "noun", "/pʊrˈpɑːrleɪ/", "cuộc đàm phán thăm dò sơ bộ"),
    ("078331", "pourpoint", "noun", "/ˈpʊrpɔɪnt/", "áo chẽn mặc giáp (Trung Cổ)"),
    ("078332", "pours", "verb", "/pɔːrz/", "rót, đổ, trút xuống"),
    ("078333", "poussette", "noun", "/puːˈsɛt/", "điệu xoay tròn đổi chỗ (múa cổ)"),
    ("078334", "pouted", "verb", "/ˈpaʊtɪd/", "đã bĩu môi, phụng phịu hờn dỗi"),
    ("078335", "pouteria", "noun", "/paʊˈtɪriə/", "chi cây trứng gà (Pouteria)"),
    ("078336", "pouting", "verb", "/ˈpaʊtɪŋ/", "bĩu môi, phụng phịu hờn dỗi"),
    ("078337", "poutingly", "adv", "/ˈpaʊtɪŋli/", "với vẻ bĩu môi hờn dỗi"),
    ("078338", "pouts", "verb", "/paʊts/", "bĩu môi, phụng phịu hờn dỗi"),
    ("078339", "pouyi", "noun", "/ˈpuːji/", "Hoàng đế Phổ Nghi (Puyi, nhà Thanh)"),
    ("078340", "powderer", "noun", "/ˈpaʊdərər/", "người hoặc dụng cụ rắc phấn bột"),
    ("078341", "powderiness", "noun", "/ˈpaʊdərinəs/", "độ mịn như bột, tính chất dạng bột"),
    ("078342", "powdering", "verb", "/ˈpaʊdərɪŋ/", "tán thành bột; rắc phấn, phủ bột"),
    ("078343", "powderise", "verb", "/ˈpaʊdəraɪz/", "tán nhuyễn thành bột; rắc bột"),
    ("078344", "powderize", "verb", "/ˈpaʊdəraɪz/", "tán nhuyễn thành bột; rắc bột"),
    ("078345", "powders", "verb", "/ˈpaʊdərz/", "tán thành bột; rắc phấn, phủ bột"),
    ("078346", "powering", "verb", "/ˈpaʊərɪŋ/", "cấp nguồn điện; truyền động lực"),
    ("078347", "powerlessly", "adv", "/ˈpaʊərləsli/", "một cách bất lực, yếu đuối"),
    ("078348", "powerplant", "noun", "/ˈpaʊərˌplænt/", "nhà máy điện; tổ máy phát động lực"),
    ("078349", "powers", "verb", "/ˈpaʊərz/", "cấp nguồn điện; truyền động lực"),
    ("078350", "powerstation", "noun", "/ˈpaʊərˌsteɪʃən/", "nhà máy phát điện, trạm điện"),
    ("078351", "powerwash", "verb", "/ˈpaʊərwɒʃ/", "phun rửa áp lực cao"),
    ("078352", "powwowed", "verb", "/ˈpaʊwaʊd/", "đã họp bàn thảo luận nhanh"),
    ("078353", "powwowing", "verb", "/ˈpaʊwaʊɪŋ/", "họp bàn thảo luận nhanh"),
    ("078354", "powwows", "verb", "/ˈpaʊˌwaʊz/", "họp bàn thảo luận nhanh"),
    ("078355", "poxy", "adj", "/ˈpɒksi/", "nhiễm bệnh giang mai; tồi tệ (lóng)"),
    ("078356", "poyou", "noun", "/ˈpoʊjuː/", "con ta-tu sáu đai Nam Mỹ (poyou)"),
    ("078357", "pozsony", "noun", "/ˈpɒʒɒni/", "thành phố Bratislava (tên Hungary)"),
    ("078358", "pozzy", "noun", "/ˈpɒzi/", "mứt ăn bánh (tiếng lóng quân đội)"),
    ("078359", "pp", "noun", "/ˌpiːˈpiː/", "trang (số nhiều pages, viết tắt)"),
    ("078360", "ppd", "noun", "/ˌpiːˌpiːˈdiː/", "đã trả trước cước phí (viết tắt)"),
    ("078361", "ppe", "noun", "/ˌpiːˌpiːˈiː/", "đồ bảo hộ cá nhân PPE; ngành PPE"),
    ("078362", "pplo", "noun", "/ˌpiːˌpiːɛlˈoʊ/", "vi khuẩn Mycoplasma (PPLO)"),
    ("078363", "pps", "noun", "/ˌpiːˌpiːˈɛs/", "tái bút lần hai (P.P.S.)"),
    ("078364", "praam", "noun", "/prɑːm/", "xà lan đáy bằng; pháo hạm đáy bằng"),
    ("078365", "practicableness", "noun", "/ˈpræktɪkəbəlnəs/", "tính khả thi, tính thực tế"),
    ("078366", "practicalness", "noun", "/ˈpræktɪkəlnəs/", "tính thực tế, tính thực tiễn"),
    ("078367", "practicer", "noun", "/ˈpræktɪsər/", "người thực hành, người hành nghề"),
    ("078368", "practices", "verb", "/ˈpræktɪsɪz/", "luyện tập, thực hành, hành nghề"),
    ("078369", "practician", "noun", "/prækˈtɪʃən/", "người hành nghề có kinh nghiệm"),
    ("078370", "practicing", "verb", "/ˈpræktɪsɪŋ/", "luyện tập, thực hành, hành nghề"),
    ("078371", "practiser", "noun", "/ˈpræktɪsər/", "người thực hành, người hành nghề"),
    ("078372", "practises", "verb", "/ˈpræktɪsɪz/", "luyện tập, thực hành, hành nghề"),
    ("078373", "practising", "verb", "/ˈpræktɪsɪŋ/", "luyện tập, thực hành, hành nghề"),
    ("078374", "praeabdomen", "noun", "/ˌpriːæbˈdoʊmən/", "phần trước bụng (côn trùng)"),
    ("078375", "praeaxial", "adj", "/ˌpriːˈæksiəl/", "ở phía trước trục chi (giải phẫu)"),
    ("078376", "praecentrum", "noun", "/ˌpriːˈsɛntrəm/", "mấu trước thân đốt sống (sinh học)"),
    ("078377", "praecoces", "noun", "/prɪˈkoʊsiːz/", "chim non sớm tự lập (rời tổ sớm)"),
    ("078378", "praecocial", "adj", "/prɪˈkoʊʃəl/", "sớm tự lập sau khi nở (chim non)"),
    ("078379", "praecostal", "adj", "/ˌpriːˈkɒstəl/", "trước gân sườn cánh (côn trùng)"),
    ("078380", "praecoxal", "adj", "/ˌpriːˈkɒksəl/", "trước đốt háng (động vật chân khớp)"),
    ("078381", "praecrural", "adj", "/ˌpriːˈkrʊrəl/", "thuộc mặt trước cẳng chân"),
    ("078382", "praedial", "adj", "/ˈpriːdiəl/", "thuộc ruộng đất, đất đai nông thôn"),
    ("078383", "praemunire", "noun", "/ˌpriːmjʊˈnaɪri/", "tội xúc phạm vương quyền Anh (cổ)"),
    ("078384", "praeoccipital", "adj", "/ˌpriːɒkˈsɪpɪtəl/", "ở phía trước thùy chẩm (não bộ)"),
    ("078385", "praeoral", "adj", "/ˌpriːˈɔːrəl/", "ở phía trước miệng (sinh học)"),
    ("078386", "praepostor", "noun", "/prɪˈpɒstər/", "trưởng lớp, học sinh giám thị (Anh)"),
    ("078387", "praetorial", "adj", "/priːˈtɔːriəl/", "thuộc pháp quan La Mã cổ đại"),
    ("078388", "pragmatise", "verb", "/ˈpræɡmətaɪz/", "thực tế hóa, coi như chuyện có thực"),
    ("078389", "pragmatistic", "adj", "/ˌpræɡməˈtɪstɪk/", "thuộc chủ nghĩa thực dụng"),
    ("078390", "pragmatize", "verb", "/ˈpræɡmətaɪz/", "thực tế hóa, coi như chuyện có thực"),
    ("078391", "praisable", "adj", "/ˈpreɪzəbəl/", "đáng khen ngợi, đáng tán dương"),
    ("078392", "praised", "verb", "/preɪzd/", "đã khen ngợi, ca ngợi, tán dương"),
    ("078393", "praiseful", "adj", "/ˈpreɪzfəl/", "đầy lời khen ngợi, tán dương"),
    ("078394", "praiser", "noun", "/ˈpreɪzər/", "người khen ngợi, người ca tụng"),
    ("078395", "praises", "verb", "/ˈpreɪzɪz/", "khen ngợi, ca ngợi, tán dương"),
    ("078396", "praiseworthily", "adv", "/ˈpreɪzˌwɜːrðɪli/", "một cách đáng khen ngợi"),
    ("078397", "praiseworthiness", "noun", "/ˈpreɪzˌwɜːrðinəs/", "tính đáng khen, đức tính đáng ngợi"),
    ("078398", "praisworthiness", "noun", "/ˈpreɪzˌwɜːrðinəs/", "phẩm chất đáng khen (biến thể)"),
    ("078399", "prajna", "noun", "/ˈprʌdʒnə/", "trí tuệ Bát-nhã (triết Phật giáo)"),
    ("078400", "prakritic", "adj", "/prəˈkrɪtɪk/", "thuộc nhóm ngôn ngữ Prakrit (Ấn)"),
    ("078401", "pranced", "verb", "/prænst/", "đã nhảy tung tăng; đi nghênh ngang"),
    ("078402", "prances", "verb", "/ˈprænsɪz/", "nhảy tung tăng; đi nghênh ngang"),
]

with open("scratch/b36_r07_raw_p4.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

assert len(raw) == len(rows) == 100
out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, rows):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} vs {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} vs {hw}"
    assert len(vi) <= 35, f"vi too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.count("/") == 2 and not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"bad ipa: {hw} -> {ipa}"
    r["pos"] = pos
    r["ipa"] = ipa
    r["vi"] = vi
    r["status"] = "reviewed"
    out.append(r)

with open("scratch/b36_r07_p4.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r07_p4 saved OK")
