import json

rows = [
    ("075903", "pettishly", "adv", "/ˈpɛtɪʃli/", "một cách cáu kỉnh, hay dỗi"),
    ("075904", "pettishness", "noun", "/ˈpɛtɪʃnəs/", "tính cáu kỉnh, hay dỗi"),
    ("075905", "pettitoes", "noun", "/ˈpɛtɪtoʊz/", "chân giò lợn (nấu ăn)"),
    ("075906", "petulancy", "noun", "/ˈpɛtjʊlənsi/", "tính hờn dỗi, cáu kỉnh vô cớ"),
    ("075907", "petuntse", "noun", "/pəˈtʊntsə/", "đá bạch đôn tử (làm gốm sứ)"),
    ("075908", "pewage", "noun", "/ˈpjuːɪdʒ/", "tiền thuê ghế ngồi trong nhà thờ"),
    ("075909", "pewit", "noun", "/ˈpiːwɪt/", "chim te te; mòng biển đầu đen"),
    ("075910", "pezizaceae", "noun", "/pɛzɪˈzeɪsiː/", "họ Nấm cốc (Pezizaceae)"),
    ("075911", "pezizales", "noun", "/pɛzɪˈzeɪliːz/", "bộ Nấm cốc (Pezizales)"),
    ("075912", "pezophaps", "noun", "/ˈpɛzəfæps/", "chi chim solitaire tuyệt chủng"),
    ("075913", "pfannkuchen", "noun", "/ˈpfænˌkuːxən/", "bánh rán nhân mứt Đức Pfannkuchen"),
    ("075914", "pfenning", "noun", "/ˈfɛnɪŋ/", "đồng xu pfennig (tiền Đức cũ)"),
    ("075915", "pfizer", "noun", "/ˈfaɪzər/", "tập đoàn dược phẩm Pfizer (Mỹ)"),
    ("075916", "pg", "noun", "/ˌpiːˈdʒiː/", "khuyến cáo phụ huynh (nhãn phim PG)"),
    ("075917", "phacella", "noun", "/fəˈsɛlə/", "sợi túi vị (sứa); tuyến phacella"),
    ("075918", "phacochoerus", "noun", "/ˌfækoʊˈkɪrəs/", "chi lợn bướu châu Phi"),
    ("075919", "phaenogam", "noun", "/ˈfiːnəɡæm/", "thực vật có hoa, thực vật có hạt"),
    ("075920", "phaenogamic", "adj", "/ˌfiːnəˈɡæmɪk/", "thuộc thực vật có hoa, có hạt"),
    ("075921", "phaeochromocytoma", "noun", "/ˌfiːoʊˌkroʊmoʊsaɪˈtoʊmə/", "u tủy thượng thận (y học)"),
    ("075922", "phaeophyceae", "noun", "/ˌfiːəˈfaɪsiː/", "lớp Tảo nâu (Phaeophyceae)"),
    ("075923", "phaeophyta", "noun", "/fiˈɒfɪtə/", "ngành Tảo nâu (Phaeophyta)"),
    ("075924", "phaethontidae", "noun", "/ˌfeɪɪˈθɒntɪdiː/", "họ Chim nhiệt đới (Phaethontidae)"),
    ("075925", "phagedaane", "noun", "/ˌfædʒɪˈdiːn/", "vết loét hoại tử lan rộng (y học)"),
    ("075926", "phagedane", "noun", "/ˈfædʒɪdeɪn/", "vết loét hoại tử lan rộng (y học)"),
    ("075927", "phagocytise", "verb", "/ˈfæɡəsaɪtaɪz/", "thực bào (tế bào nuốt vật lạ)"),
    ("075928", "phagocytize", "verb", "/ˈfæɡəsaɪtaɪz/", "thực bào (tế bào nuốt vật lạ)"),
    ("075929", "phagocytose", "verb", "/ˌfæɡəˈsaɪtoʊs/", "thực bào (tế bào nuốt vật lạ)"),
    ("075930", "phagosome", "noun", "/ˈfæɡəsoʊm/", "thể thực bào (túi trong tế bào)"),
    ("075931", "phagun", "noun", "/ˈfɑːɡʊn/", "tháng thứ 12 lịch Ấn Độ (Phalguna)"),
    ("075932", "phaius", "noun", "/ˈfeɪəs/", "chi hoa lan hạc đính (Phaius)"),
    ("075933", "phalacrocoracidae", "noun", "/fəˌlækrəkəˈræsɪdiː/", "họ Chim cốc (Phalacrocoracidae)"),
    ("075934", "phalacrosis", "noun", "/ˌfæləˈkroʊsɪs/", "chứng rụng tóc, hói đầu (y học)"),
    ("075935", "phalaenoptilus", "noun", "/fəˌliːnɒpˈtɪləs/", "chi cú muỗi nghèo (Phalaenoptilus)"),
    ("075936", "phalange", "noun", "/fəˈlændʒ/", "đốt ngón tay chân; đội hình falăng"),
    ("075937", "phalanger", "noun", "/fəˈlændʒər/", "thú có túi leo cây Úc (phalanger)"),
    ("075938", "phalangeridae", "noun", "/ˌfæləndʒəˈraɪdiː/", "họ Thú có túi phalanger"),
    ("075939", "phalanges", "noun", "/fəˈlændʒiːz/", "đốt ngón tay chân; đội hình falăng"),
    ("075940", "phalangida", "noun", "/fəˈlændʒɪdə/", "bộ Nhện chân dài (Opiliones)"),
    ("075941", "phalangiidae", "noun", "/ˌfælənˈdʒaɪɪdiː/", "họ Nhện chân dài (Phalangiidae)"),
    ("075942", "phalangitis", "noun", "/ˌfælənˈdʒaɪtɪs/", "viêm đốt ngón tay hoặc chân"),
    ("075943", "phalangium", "noun", "/fəˈlændʒiəm/", "chi nhện chân dài Phalangium"),
    ("075944", "phalanstere", "noun", "/ˌfælənˈstɛr/", "cộng đồng phalanster (Fourier)"),
    ("075945", "phalansterian", "adj", "/ˌfælənˈstɪriən/", "thuộc cộng đồng phalanster"),
    ("075946", "phalansterianism", "noun", "/ˌfælənˈstɪriənɪzəm/", "học thuyết cộng đồng phalanster"),
    ("075947", "phalanstery", "noun", "/ˈfælənstɛri/", "cộng đồng phalanster (Fourier)"),
    ("075948", "phalanxes", "noun", "/ˈfeɪlæŋksɪz/", "đội hình phalăng; đốt ngón tay"),
    ("075949", "phalaropidae", "noun", "/ˌfælˈærəpɪdiː/", "họ Chim lội màng chân Phalaropidae"),
    ("075950", "phalaropus", "noun", "/ˌfælˈærəpəs/", "chi chim lội màng chân Phalaropus"),
    ("075951", "phalguna", "noun", "/ˈfɑːlɡʊnə/", "tháng thứ 12 lịch Ấn Độ (Phalguna)"),
    ("075952", "phallaceae", "noun", "/fæˈleɪsiː/", "họ Nấm mùi thối (Phallaceae)"),
    ("075953", "phallales", "noun", "/fæˈleɪliːz/", "bộ Nấm mùi thối (Phallales)"),
    ("075954", "phalli", "noun", "/ˈfælaɪ/", "dương vật; biểu tượng sinh thực khí"),
    ("075955", "phallically", "adv", "/ˈfælɪkli/", "liên quan đến dương vật"),
    ("075956", "phallicism", "noun", "/ˈfælɪsɪzəm/", "tín ngưỡng sùng bái sinh thực khí"),
    ("075957", "phallodynia", "noun", "/ˌfæloʊˈdɪniə/", "chứng đau dương vật (y học)"),
    ("075958", "phallosome", "noun", "/ˈfæləsoʊm/", "cơ quan giao cấu côn trùng"),
    ("075959", "phalluses", "noun", "/ˈfæləsɪz/", "dương vật; biểu tượng sinh thực khí"),
    ("075960", "phalsa", "noun", "/ˈfɑːlsə/", "cây cò ke quả mọng Ấn Độ (phalsa)"),
    ("075961", "phanerogam", "noun", "/ˈfænərəˌɡæm/", "thực vật có hạt, có hoa"),
    ("075962", "phanerogamae", "noun", "/ˌfænərəˈɡæmiː/", "ngành Thực vật có hạt"),
    ("075963", "phanerogamic", "adj", "/ˌfænərəˈɡæmɪk/", "thuộc thực vật có hoa, có hạt"),
    ("075964", "phanerogamous", "adj", "/ˌfænəˈrɒɡəməs/", "thuộc thực vật có hoa, có hạt"),
    ("075965", "phaneromania", "noun", "/ˌfænərəˈmeɪniə/", "thói quen cắn móng, nặn da bệnh lý"),
    ("075966", "phanerophyte", "noun", "/ˈfænərəˌfaɪt/", "cây thân gỗ chồi lộ (sinh thái)"),
    ("075967", "phanstasmal", "adj", "/fænˈtæzməl/", "mang tính ảo ảnh, ma quái (cổ)"),
    ("075968", "phantasies", "noun", "/ˈfæntəsiz/", "trí tưởng tượng; ảo mộng"),
    ("075969", "phantasmagorically", "adv", "/fænˌtæzməˈɡɒrɪkli/", "như cảnh biến ảo kỳ dị (ảo ảnh)"),
    ("075970", "phantasmata", "noun", "/fænˈtæzmətə/", "bóng ma; ảo ảnh, huyễn ảnh"),
    ("075971", "phantasmic", "adj", "/fænˈtæzmɪk/", "có tính chất ảo ảnh, huyễn hoặc"),
    ("075972", "phantast", "noun", "/ˈfæntæst/", "người mơ mộng hão huyền"),
    ("075973", "phantastic", "adj", "/fænˈtæstɪk/", "tuyệt vời; kỳ quái (cách viết cổ)"),
    ("075974", "phantoms", "noun", "/ˈfæntəmz/", "bóng ma; ảo ảnh"),
    ("075975", "pharisaically", "adv", "/ˌfærɪˈseɪɪkli/", "một cách đạo đức giả, câu nệ"),
    ("075976", "pharisaicalness", "noun", "/ˌfærɪˈseɪɪkəlnəs/", "thói đạo đức giả, câu nệ"),
    ("075977", "pharisaism", "noun", "/ˈfærɪseɪˌɪzəm/", "thói đạo đức giả; phái Pharisi"),
    ("075978", "pharmaceutic", "adj", "/ˌfɑːrməˈsuːtɪk/", "thuộc dược phẩm, dược học"),
    ("075979", "pharmaceutically", "adv", "/ˌfɑːrməˈsuːtɪkli/", "về mặt dược học, bào chế thuốc"),
    ("075980", "pharmaceutist", "noun", "/ˌfɑːrməˈsuːtɪst/", "dược sĩ; nhà bào chế thuốc"),
    ("075981", "pharmacies", "noun", "/ˈfɑːrməsiz/", "hiệu thuốc; ngành dược"),
    ("075982", "pharmacodynamic", "adj", "/ˌfɑːrməkoʊdaɪˈnæmɪk/", "thuộc dược lực học"),
    ("075983", "pharmacodynamics", "noun", "/ˌfɑːrməkoʊdaɪˈnæmɪks/", "dược lực học (tác dụng của thuốc)"),
    ("075984", "pharmacognostic", "adj", "/ˌfɑːrməkɒɡˈnɒstɪk/", "thuộc dược liệu học"),
    ("075985", "pharmacognostical", "adj", "/ˌfɑːrməkɒɡˈnɒstɪkəl/", "thuộc dược liệu học"),
    ("075986", "pharmacognosy", "noun", "/ˌfɑːrməˈkɒɡnəsi/", "dược liệu học (thuốc từ tự nhiên)"),
    ("075987", "pharmacokinetic", "adj", "/ˌfɑːrməkoʊkɪˈnɛtɪk/", "thuộc dược động học"),
    ("075988", "pharmacopoeial", "adj", "/ˌfɑːrməkəˈpiːəl/", "thuộc dược điển"),
    ("075989", "pharmacopoeist", "noun", "/ˌfɑːrməkəˈpiːɪst/", "người biên soạn dược điển"),
    ("075990", "pharomacrus", "noun", "/ˌfærəˈmækrəs/", "chi chim quetzal (Pharomachrus)"),
    ("075991", "pharyngal", "adj", "/fəˈrɪŋɡəl/", "thuộc hầu, yết hầu"),
    ("075992", "pharynges", "noun", "/fəˈrɪndʒiːz/", "hầu, họng (giải phẫu)"),
    ("075993", "pharyngology", "noun", "/ˌfɛrɪŋˈɡɒlədʒi/", "khoa học nghiên cứu hầu họng"),
    ("075994", "pharyngoscope", "noun", "/fəˈrɪŋɡəskoʊp/", "dụng cụ soi hầu họng (y học)"),
    ("075995", "pharyngotomy", "noun", "/ˌfɛrɪŋˈɡɒtəmi/", "phẫu thuật mở hầu họng (y học)"),
    ("075996", "pharynxes", "noun", "/ˈfɛrɪŋksɪz/", "hầu, họng (giải phẫu)"),
    ("075997", "phascogale", "noun", "/fæsˈkɒɡəli/", "chi thú túi chuột phascogale (Úc)"),
    ("075998", "phascolarctos", "noun", "/ˌfæskoʊˈlɑːrktɒs/", "chi gấu túi koala (Phascolarctos)"),
    ("075999", "phased", "verb", "/feɪzd/", "đã thực hiện từng giai đoạn"),
    ("076000", "phasemeter", "noun", "/ˈfeɪzˌmiːtər/", "pha kế (máy đo góc lệch pha)"),
    ("076001", "phases", "verb", "/ˈfeɪzɪz/", "thực hiện theo từng giai đoạn"),
    ("076002", "phasianid", "noun", "/feɪˈziːənɪd/", "chim họ Trĩ (gà lôi, công)"),
]

with open("scratch/b36_r02_raw_p5.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r02_p5.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r02_p5 saved OK")
