import json

RECORDS = [
    ("085203", "scattily", "adv", "/ˈskætɪli/", "đãng trí; thất thường; điên rồ"),
    ("085204", "scattiness", "noun", "/ˈskætinəs/", "tính đãng trí; sự khùng điên"),
    ("085205", "scatting", "verb", "/ˈskætɪŋ/", "đang hát ứng tác scat; chạy biến"),
    ("085206", "scauper", "noun", "/ˈskɔːpər/", "mũi đục lòng máng điêu khắc"),
    ("085207", "scaur", "noun", "/skɔːr/", "vách đá dốc lởm chởm"),
    ("085208", "scavenged", "verb", "/ˈskævɪndʒd/", "đã bới rác tìm đồ; ăn xác thối"),
    ("085209", "scavenges", "verb", "/ˈskævɪndʒɪz/", "bới tìm phế liệu; ăn xác thối"),
    ("085210", "scavenging", "verb", "/ˈskævɪndʒɪŋ/", "đang bới rác; đang ăn xác thối"),
    ("085211", "sce", "noun", "/ˌɛsˌsiːˈiː/", "Bằng giáo dục Scotland (SCE)"),
    ("085212", "sceliphron", "noun", "/ˈsɛlɪˌfrɑːn/", "chi ong tò vò xây tổ bùn"),
    ("085213", "sceloglaux", "noun", "/ˌsɛləˈɡlɔːks/", "chi cú mặt trắng New Zealand"),
    ("085214", "scena", "noun", "/ˈʃeɪnə/", "màn hát kịch tính (opera Ý)"),
    ("085215", "scend", "verb", "/sɛnd/", "nhô bổng lên (sóng biển, tàu)"),
    ("085216", "sceneshifter", "noun", "/ˈsiːnˌʃɪftər/", "nhân viên chuyển cảnh sân khấu"),
    ("085217", "scenical", "adj", "/ˈsiːnɪkəl/", "thuộc sân khấu; có cảnh đẹp"),
    ("085218", "scenograph", "noun", "/ˈsiːnəˌɡræf/", "bức vẽ phối cảnh công trình"),
    ("085219", "scenographer", "noun", "/sɪˈnɑːɡrəfər/", "họa sĩ thiết kế bối cảnh"),
    ("085220", "scenographic", "adj", "/ˌsiːnəˈɡræfɪk/", "thuộc phối cảnh; dàn dựng cảnh"),
    ("085221", "scenography", "noun", "/sɪˈnɑːɡrəfi/", "nghệ thuật thiết kế sân khấu"),
    ("085222", "scenting", "verb", "/ˈsɛntɪŋ/", "đang đánh hơi; đang ướp hương"),
    ("085223", "scents", "verb", "/sɛnts/", "đánh hơi thấy; tỏa hương thơm"),
    ("085224", "scepsis", "noun", "/ˈskɛpsɪs/", "thuyết hoài nghi triết học"),
    ("085225", "sceptered", "adj", "/ˈsɛptərd/", "cầm vương trượng; nắm vương quyền"),
    ("085226", "sceptreless", "adj", "/ˈsɛptərləs/", "không có vương trượng; mất ngôi"),
    ("085227", "scet", "noun", "/ˌɛsˌsiːˌiːˈtiː/", "giờ sự kiện tàu vũ trụ (SCET)"),
    ("085228", "sch", "noun", "/skuːl/", "trường học (viết tắt)"),
    ("085229", "schaffneria", "noun", "/ʃæfˈnɪriə/", "chi dương xỉ Schaffneria"),
    ("085230", "schappe", "noun", "/ʃæp/", "sợi tơ tằm kéo từ tơ phế"),
    ("085231", "schedules", "noun", "/ˈskɛdʒʊlz/", "lịch trình; thời gian biểu"),
    ("085232", "schemata", "noun", "/skiːˈmɑːtə/", "giản đồ; lược đồ nhận thức"),
    ("085233", "schematisation", "noun", "/ˌskiːmətaɪˈzeɪʃən/", "sự sơ đồ hóa; sự hệ thống hóa"),
    ("085234", "schematise", "verb", "/ˈskiːməˌtaɪz/", "sơ đồ hóa; hệ thống hóa"),
    ("085235", "schematised", "verb", "/ˈskiːməˌtaɪzd/", "đã sơ đồ hóa; đã hệ thống hóa"),
    ("085236", "schematises", "verb", "/ˈskiːməˌtaɪzɪz/", "sơ đồ hóa; hệ thống hóa"),
    ("085237", "schematising", "verb", "/ˈskiːməˌtaɪzɪŋ/", "đang sơ đồ hóa; hệ thống hóa"),
    ("085238", "schematism", "noun", "/ˈskiːməˌtɪzəm/", "hệ thống sơ đồ; phép khái lược"),
    ("085239", "schematize", "verb", "/ˈskiːməˌtaɪz/", "hệ thống hóa; lập sơ đồ"),
    ("085240", "schematized", "verb", "/ˈskiːməˌtaɪzd/", "đã hệ thống hóa; đã lập sơ đồ"),
    ("085241", "schematizes", "verb", "/ˈskiːməˌtaɪzɪz/", "hệ thống hóa; lập sơ đồ"),
    ("085242", "schematizing", "verb", "/ˈskiːməˌtaɪzɪŋ/", "đang hệ thống hóa; đang lập sơ đồ"),
    ("085243", "schemed", "verb", "/skiːmd/", "đã bày mưu; đã vạch kế hoạch"),
    ("085244", "schemes", "verb", "/skiːmz/", "bày mưu tính kế; lập âm mưu"),
    ("085245", "schemozzle", "noun", "/ʃəˈmɑːzəl/", "cảnh hỗn loạn; vụ ẩu đả ồn ào"),
    ("085246", "scheol", "noun", "/ˈʃiːoʊl/", "âm phủ; cõi chết (Do Thái giáo)"),
    ("085247", "scherzando", "adj", "/skɛrtˈsɑːndoʊ/", "vui tươi nghịch ngợm (âm nhạc)"),
    ("085248", "scheuchzeriaceae", "noun", "/ˌʃɔɪktzəriˈeɪsiːˌiː/", "họ thực vật đầm lầy"),
    ("085249", "schiedam", "noun", "/skiːˈdæm/", "rượu gin Hà Lan Schiedam"),
    ("085250", "schinus", "noun", "/ˈskaɪnəs/", "chi cây tiêu Brazil Schinus"),
    ("085251", "schipperke", "noun", "/ˈskɪpərki/", "giống chó đen Bỉ Schipperke"),
    ("085252", "schismatical", "adj", "/skɪzˈmætɪkəl/", "ly giáo; gây chia rẽ bè phái"),
    ("085253", "schismatically", "adv", "/skɪzˈmætɪkli/", "theo lối ly giáo; gây chia rẽ"),
    ("085254", "schismatise", "verb", "/ˈskɪzməˌtaɪz/", "chia rẽ thành bè phái ly giáo"),
    ("085255", "schismatize", "verb", "/ˈskɪzməˌtaɪz/", "chia rẽ thành bè phái ly giáo"),
    ("085256", "schistic", "adj", "/ˈʃɪstɪk/", "thuộc đá phiến sét"),
    ("085257", "schistorrhachis", "noun", "/ˌskɪstəˈreɪkɪs/", "tật nứt đốt sống bẩm sinh"),
    ("085258", "schistose", "adj", "/ˈʃɪstoʊs/", "có cấu trúc phân phiến (đá)"),
    ("085259", "schistosomatidae", "noun", "/ˌʃɪstəsoʊˈmætɪˌdiː/", "họ Sán máng (Schistosomatidae)"),
    ("085260", "schistosomiases", "noun", "/ˌʃɪstəsəˈmaɪəsiːz/", "bệnh sán máng"),
    ("085261", "schistous", "adj", "/ˈʃɪstəs/", "có dạng đá phiến"),
    ("085262", "schizachyrium", "noun", "/ˌskɪzəˈkaɪriəm/", "chi cỏ chổi Schizachyrium"),
    ("085263", "schizaea", "noun", "/skaɪˈziːə/", "chi dương xỉ tóc xoăn Schizaea"),
    ("085264", "schizaeaceae", "noun", "/ˌskaɪziˈeɪsiːˌiː/", "họ Dương xỉ Schizaeaceae"),
    ("085265", "schizanthus", "noun", "/skɪˈzænθəs/", "hoa bướm Schizanthus"),
    ("085266", "schizo", "noun", "/ˈskɪtsoʊ/", "người tâm thần phân liệt (lóng)"),
    ("085267", "schizocarp", "noun", "/ˈskɪzəˌkɑːrp/", "quả nẻ tách (thực vật học)"),
    ("085268", "schizogony", "noun", "/skaɪˈzɑːɡəni/", "sinh sản liệt phân"),
    ("085269", "schizolysis", "noun", "/skaɪˈzɑːləsɪs/", "sự phân tách tế bào"),
    ("085270", "schizomycete", "noun", "/ˌskɪzoʊˈmaɪsiːt/", "vi khuẩn phân liệt (thuật ngữ cũ)"),
    ("085271", "schizomycetes", "noun", "/ˌskɪzoʊmaɪˈsiːtiːz/", "lớp Vi khuẩn phân liệt"),
    ("085272", "schizont", "noun", "/ˈskɪzɑːnt/", "thể phân liệt (ký sinh trùng)"),
    ("085273", "schizopetalon", "noun", "/ˌskɪzoʊˈpɛtələn/", "chi hoa cánh xẻ Chile"),
    ("085274", "schizophragma", "noun", "/ˌskɪzoʊˈfræɡmə/", "chi cẩm tú cầu leo Nhật Bản"),
    ("085275", "schizophrene", "noun", "/ˈskɪtsəˌfriːn/", "bệnh nhân tâm thần phân liệt"),
    ("085276", "schizophrenically", "adv", "/ˌskɪtsəˈfrɛnɪkli/", "như tâm thần phân liệt; chia rẽ"),
    ("085277", "schizophyceae", "noun", "/ˌskɪzoʊˈfaɪsiːˌiː/", "lớp Tảo lam (vi khuẩn lam)"),
    ("085278", "schizophyta", "noun", "/skaɪˈzɑːfɪtə/", "ngành thực vật phân liệt cũ"),
    ("085279", "schizophyte", "noun", "/ˈskɪzəˌfaɪt/", "vi sinh vật sinh sản phân đôi"),
    ("085280", "schizopod", "adj", "/ˈskɪzəˌpɑːd/", "có chân chẻ hai nhánh (giáp xác)"),
    ("085281", "schizopoda", "noun", "/skaɪˈzɑːpədə/", "nhóm Giáp xác chân khe"),
    ("085282", "schizosaccharomycetaceae", "noun", "/ˌskɪzoʊˌsækəroʊˌmaɪsɪˈteɪsiːˌiː/", "họ Nấm men phân đôi"),
    ("085283", "schizothymia", "noun", "/ˌskɪzoʊˈθaɪmiə/", "tính khí khép kín lạnh lùng"),
    ("085284", "schlepp", "verb", "/ʃlɛp/", "khuân vác lê bước nặng nhọc"),
    ("085285", "schlepper", "noun", "/ˈʃlɛpər/", "người khuân vác; kẻ vụng về"),
    ("085286", "schleps", "verb", "/ʃlɛps/", "khuân vác nặng nhọc; lết đi"),
    ("085287", "schlesien", "noun", "/ˈʃleɪziən/", "vùng Silesia (tiếng Đức)"),
    ("085288", "schlimazel", "noun", "/ʃlɪˈmɑːzəl/", "người xui xẻo bẩm sinh"),
    ("085289", "schlockmeister", "noun", "/ˈʃlɑːkˌmaɪstər/", "kẻ buôn hàng dỏm rẻ tiền"),
    ("085290", "schlong", "noun", "/ʃlɔːŋ/", "dương vật (tiếng lóng)"),
    ("085291", "schlumbergera", "noun", "/ˌʃlʊmbərˈɡɛrə/", "chi xương rồng càng cua"),
    ("085292", "schmalze", "noun", "/ʃmɑːlts/", "sự ủy mị giả tạo; mỡ gà rán"),
    ("085293", "schmalzy", "adj", "/ˈʃmɑːltsi/", "ủy mị thái quá; sướt mướt"),
    ("085294", "schmeer", "noun", "/ʃmɪr/", "lớp phết mỏng; tiền hối lộ"),
    ("085295", "schmegegge", "noun", "/ʃməˈɡɛɡi/", "chuyện nhảm nhí; kẻ ngốc nghếch"),
    ("085296", "schmoose", "noun", "/ʃmuːz/", "cuộc trò chuyện thân mật xã giao"),
    ("085297", "schmoozer", "noun", "/ˈʃmuːzər/", "người giỏi bắt chuyện xã giao"),
    ("085298", "schmutz", "noun", "/ʃmʊts/", "chất bẩn; vết dơ; rác rưởi"),
    ("085299", "schnecken", "noun", "/ˈʃnɛkən/", "bánh ngọt cuộn ốc Đức"),
    ("085300", "schnittlaugh", "noun", "/ˈʃnɪtˌlaʊx/", "lá hẹ tây; hành tăm (tiếng Đức)"),
    ("085301", "schnorchel", "noun", "/ˈʃnɔːrkəl/", "ống thông hơi tàu ngầm; ống thở"),
    ("085302", "schnorkel", "noun", "/ˈʃnɔːrkəl/", "ống thông hơi tàu ngầm; ống thở"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r01_raw_p3.json"))
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

json.dump(out, open("scratch/b38_r01_reviewed_p3.json", "w"), ensure_ascii=False, indent=2)
print("b38_r01_p3 saved OK")
