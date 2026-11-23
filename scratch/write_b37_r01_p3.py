import json

records = [
    ("080203", "psychogenetic", "adj", "/ˌsaɪkoʊdʒəˈnɛtɪk/", "có nguồn gốc tâm lý, tâm căn"),
    ("080204", "psycholinguist", "noun", "/ˌsaɪkoʊˈlɪŋɡwɪst/", "nhà tâm lý ngôn ngữ học"),
    ("080205", "psychologies", "noun", "/saɪˈkɑːlədʒiz/", "các trường phái tâm lý học"),
    ("080206", "psychologise", "verb", "/saɪˈkɑːləˌdʒaɪz/", "phân tích dưới góc độ tâm lý (Anh)"),
    ("080207", "psychologism", "noun", "/saɪˈkɑːləˌdʒɪzəm/", "chủ nghĩa tâm lý (triết học)"),
    ("080208", "psychologists", "noun", "/saɪˈkɑːlədʒɪsts/", "các nhà tâm lý học"),
    ("080209", "psychologize", "verb", "/saɪˈkɑːləˌdʒaɪz/", "suy diễn tâm lý, phân tích tâm lý"),
    ("080210", "psychomancy", "noun", "/ˈsaɪkəˌmænsi/", "thuật gọi hồn bói toán (huyền bí)"),
    ("080211", "psychometrical", "adj", "/ˌsaɪkəˈmɛtrɪkəl/", "thuộc trắc nghiệm tâm lý"),
    ("080212", "psychometrika", "noun", "/ˌsaɪkoʊˈmɛtrɪkə/", "tạp chí tâm lý đo lường học"),
    ("080213", "psychoneuroses", "noun", "/ˌsaɪkoʊnʊˈroʊsiːz/", "các chứng rối loạn tâm căn"),
    ("080214", "psychoneurosis", "noun", "/ˌsaɪkoʊnʊˈroʊsɪs/", "chứng rối loạn tâm căn (y học)"),
    ("080215", "psychonomics", "noun", "/ˌsaɪkəˈnɑːmɪks/", "tâm lý học thực nghiệm nhận thức"),
    ("080216", "psychopathically", "adv", "/ˌsaɪkəˈpæθɪkli/", "theo kiểu rối loạn nhân cách"),
    ("080217", "psychopathologic", "adj", "/ˌsaɪkoʊˌpæθəˈlɑːdʒɪk/", "thuộc bệnh lý tâm thần"),
    ("080218", "psychopathologist", "noun", "/ˌsaɪkoʊpəˈθɑːlədʒɪst/", "nhà nghiên cứu bệnh lý tâm thần"),
    ("080219", "psychophysicist", "noun", "/ˌsaɪkoʊˈfɪzəsɪst/", "nhà tâm vật lý học"),
    ("080220", "psychophysiologist", "noun", "/ˌsaɪkoʊˌfɪziˈɑːlədʒɪst/", "nhà tâm sinh lý học"),
    ("080221", "psychopsis", "noun", "/saɪˈkɑːpsɪs/", "chi hoa lan bướm (Psychopsis)"),
    ("080222", "psychoses", "noun", "/saɪˈkoʊsiːz/", "các chứng loạn thần (tâm thần học)"),
    ("080223", "psychosexuality", "noun", "/ˌsaɪkoʊˌsɛkʃuˈæləti/", "tính dục tâm lý (phân tâm học)"),
    ("080224", "psychosocial", "adj", "/ˌsaɪkoʊˈsoʊʃəl/", "thuộc tâm lý xã hội"),
    ("080225", "psychosomatically", "adv", "/ˌsaɪkoʊsəˈmætɪkli/", "do tác động tâm lý lên thể chất"),
    ("080226", "psychosurgeries", "noun", "/ˌsaɪkoʊˈsɜːrdʒəriz/", "các ca phẫu thuật tâm thần"),
    ("080227", "psychotherapeutically", "adv", "/ˌsaɪkoʊˌθɛrəˈpjuːtɪkli/", "bằng liệu pháp tâm lý trị liệu"),
    ("080228", "psychotherapeutics", "noun", "/ˌsaɪkoʊˌθɛrəˈpjuːtɪks/", "ngành tâm lý trị liệu học"),
    ("080229", "psychotically", "adv", "/saɪˈkɑːtɪkli/", "như người loạn thần, điên cuồng"),
    ("080230", "psychotogen", "noun", "/saɪˈkɑːtədʒən/", "chất gây ảo giác loạn thần"),
    ("080231", "psychotomimetic", "adj", "/ˌsaɪkɑːtoʊmaɪˈmɛtɪk/", "gây ảo giác giống chứng loạn thần"),
    ("080232", "psychphysiologist", "noun", "/ˌsaɪkˌfɪziˈɑːlədʒɪst/", "nhà tâm sinh lý học (lỗi viết)"),
    ("080233", "psychrometer", "noun", "/saɪˈkrɑːmɪtər/", "ẩm kế khô ướt (đo độ ẩm khí)"),
    ("080234", "psychrometers", "noun", "/saɪˈkrɑːmɪtərz/", "các ẩm kế đo độ ẩm không khí"),
    ("080235", "psychrometre", "noun", "/saɪˈkrɑːmɪtər/", "ẩm kế đo độ ẩm (biến thể Anh)"),
    ("080236", "psychrometres", "noun", "/saɪˈkrɑːmɪtərz/", "các ẩm kế đo độ ẩm (Anh)"),
    ("080237", "psychrophilic", "adj", "/ˌsaɪkrəˈfɪlɪk/", "ưa lạnh (vi sinh vật ưa dưới 20 độ)"),
    ("080238", "psycophysiologist", "noun", "/ˌsaɪkoʊˌfɪziˈɑːlədʒɪst/", "nhà tâm sinh lý học (lỗi viết)"),
    ("080239", "psycophysiology", "noun", "/ˌsaɪkoʊˌfɪziˈɑːlədʒi/", "tâm sinh lý học (lỗi viết)"),
    ("080240", "psyllidae", "noun", "/ˈsɪlɪˌdiː/", "họ Rầy nhảy hại cây (Psyllidae)"),
    ("080241", "pta", "noun", "/ˌpiːtiːˈeɪ/", "hội phụ huynh và giáo viên (PTA)"),
    ("080242", "ptboat", "noun", "/ˌpiːtiːˈboʊt/", "tàu tuần tra phóng ngư lôi"),
    ("080243", "pte", "noun", "/ˈpraɪvɪt/", "binh nhì, lính trơn (viết tắt)"),
    ("080244", "pteretis", "noun", "/təˈriːtɪs/", "chi dương xỉ đà điểu (Pteretis)"),
    ("080245", "pteridaceae", "noun", "/ˌtɛrɪˈdeɪsiː/", "họ Ráng chân xỉ (Pteridaceae)"),
    ("080246", "pteridological", "adj", "/ˌtɛrɪdəˈlɑːdʒɪkəl/", "thuộc ngành dương xỉ học"),
    ("080247", "pteridologist", "noun", "/ˌtɛrɪˈdɑːlədʒɪst/", "nhà nghiên cứu dương xỉ học"),
    ("080248", "pteridology", "noun", "/ˌtɛrɪˈdɑːlədʒi/", "ngành dương xỉ học (thực vật)"),
    ("080249", "pteridophyte", "noun", "/təˈrɪdəˌfaɪt/", "thực vật ngành Dương xỉ (có mạch)"),
    ("080250", "pteridosperm", "noun", "/təˈrɪdəˌspɜːrm/", "thực vật dương xỉ có hạt hóa thạch"),
    ("080251", "pteridospermae", "noun", "/təˌrɪdoʊˈspɜːrmiː/", "nhóm dương xỉ có hạt hóa thạch"),
    ("080252", "pteridospermaphyta", "noun", "/təˌrɪdoʊspɜːrmˈæfɪtə/", "ngành dương xỉ có hạt hóa thạch"),
    ("080253", "pteridospermopsida", "noun", "/təˌrɪdoʊspɜːrˈmɑːpsɪdə/", "lớp dương xỉ có hạt hóa thạch"),
    ("080254", "pteriidae", "noun", "/təˈraɪɪˌdiː/", "họ Trai ngọc biển (Pteriidae)"),
    ("080255", "pterins", "noun", "/ˈtɛrɪnz/", "sắc tố cánh bướm (hóa sinh học)"),
    ("080256", "pterion", "noun", "/ˈtɪriɑːn/", "điểm khớp thóp bên sọ (giải phẫu)"),
    ("080257", "pternohyla", "noun", "/ˌtɜːrnəˈhaɪlə/", "chi ếch cây đào hang Mexico"),
    ("080258", "pterocarp", "noun", "/ˈtɛrəˌkɑːrp/", "quả có cánh phát tán (thực vật)"),
    ("080259", "pterocarya", "noun", "/ˌtɛrəˈkɛriə/", "chi cây Phong dương (Pterocarya)"),
    ("080260", "pterocles", "noun", "/ˈtɛrəˌkliːz/", "chi chim gà gô cát (Pterocles)"),
    ("080261", "pteroclididae", "noun", "/ˌtɛrəˈklɪdɪˌdiː/", "họ Chim gà gô cát (Pteroclididae)"),
    ("080262", "pterocnemia", "noun", "/ˌtɛrəkˈniːmiə/", "chi đà điểu nhỏ Nam Mỹ"),
    ("080263", "pterodactylidae", "noun", "/ˌtɛrəˈdæktəlɪˌdiː/", "họ Thằn lằn bay cổ ngắn"),
    ("080264", "pterodactyloid", "adj", "/ˌtɛrəˈdæktəlɔɪd/", "giống thằn lằn bay, bộ Dực long"),
    ("080265", "pterodactylous", "adj", "/ˌtɛrəˈdæktələs/", "thuộc thằn lằn bay tiền sử"),
    ("080266", "pterodactylus", "noun", "/ˌtɛrəˈdæktələs/", "chi Thằn lằn bay cánh da"),
    ("080267", "pteroid", "adj", "/ˈtɪrɔɪd/", "có dạng cánh (xương cổ tay)"),
    ("080268", "pterois", "noun", "/ˈtɛrɔɪs/", "chi cá mao tiên có gai độc"),
    ("080269", "pteropod", "noun", "/ˈtɛrəˌpɑːd/", "ốc biển chân cánh (bướm biển)"),
    ("080270", "pteropogon", "noun", "/təˈrɑːpəɡɑːn/", "chi cây cúc lông vũ Úc"),
    ("080271", "pteropsida", "noun", "/təˈrɑːpsɪdə/", "lớp Thực vật lá lớn, dương xỉ"),
    ("080272", "pterosauria", "noun", "/ˌtɛrəˈsɔːriə/", "bộ Thằn lằn bay (Dực long)"),
    ("080273", "pterospermum", "noun", "/ˌtɛrəˈspɜːrməm/", "chi cây Lòng mang (họ Cẩm quỳ)"),
    ("080274", "pterostigna", "noun", "/ˌtɛrəˈstɪɡmə/", "vết sắc tố trên cánh (lỗi chữ)"),
    ("080275", "pterostylis", "noun", "/ˌtɛrəˈstaɪlɪs/", "chi lan lưỡi mác (Úc)"),
    ("080276", "pterygia", "noun", "/təˈrɪdʒiə/", "các mộng thịt ở mắt; cánh màng"),
    ("080277", "pterygial", "adj", "/təˈrɪdʒiəl/", "thuộc vây cá hoặc phần cánh"),
    ("080278", "pterygiod", "noun", "/ˈtɛrɪɡɔɪd/", "xương bướm cánh (biến thể sai chữ)"),
    ("080279", "pterygiodus", "adj", "/ˌtɛrɪˈɡɔɪdəs/", "thuộc xương cánh, có dạng cánh"),
    ("080280", "pterygote", "noun", "/ˈtɛrɪˌɡoʊt/", "côn trùng thuộc phân lớp Có cánh"),
    ("080281", "pterygotous", "adj", "/ˌtɛrɪˈɡoʊtəs/", "thuộc côn trùng có cánh"),
    ("080282", "pteryla", "noun", "/ˈtɛrələ/", "vùng da mọc lông vũ ở chim"),
    ("080283", "pterylae", "noun", "/ˈtɛrəˌliː/", "các vùng da mọc lông vũ ở chim"),
    ("080284", "ptilocercus", "noun", "/ˌtaɪloʊˈsɜːrkəs/", "chi đồi đuôi bút lông (Ptilocercus)"),
    ("080285", "ptilocrinus", "noun", "/ˌtaɪləˈkraɪnəs/", "chi huệ biển sâu (Ptilocrinus)"),
    ("080286", "ptilonorhynchidae", "noun", "/ˌtaɪlənɔːˈrɪŋkɪˌdiː/", "họ Chim tạo cảnh Úc và New Guinea"),
    ("080287", "ptilonorhynchus", "noun", "/ˌtaɪlənɔːˈrɪŋkəs/", "chi chim tạo cảnh màu tím satin"),
    ("080288", "ptisan", "noun", "/ˈtɪzən/", "nước cháo lúa mạch; trà thảo mộc"),
    ("080289", "ptloris", "noun", "/ˈtɪlərɪs/", "chi chim thiên đường mỏ kiếm"),
    ("080290", "ptochocracy", "noun", "/toʊˈkɑːkrəsi/", "chế độ cai trị bởi giới nghèo"),
    ("080291", "ptomain", "noun", "/ˈtoʊmeɪn/", "độc tố ptomaine trong thịt phân hủy"),
    ("080292", "ptotic", "adj", "/ˈtoʊtɪk/", "mắc chứng sụp mí, sa tạng (y học)"),
    ("080293", "ptyalin", "noun", "/ˈtaɪəlɪn/", "men tiêu hóa tinh bột (nước bọt)"),
    ("080294", "ptyalise", "verb", "/ˈtaɪəˌlaɪz/", "tiết nhiều nước bọt quá mức (Anh)"),
    ("080295", "ptyalism", "noun", "/ˈtaɪəˌlɪzəm/", "chứng tăng tiết nước bọt (y học)"),
    ("080296", "ptyalith", "noun", "/ˈtaɪəˌlɪθ/", "sỏi tuyến nước bọt (y học)"),
    ("080297", "ptyalize", "verb", "/ˈtaɪəˌlaɪz/", "tiết nhiều nước bọt quá mức"),
    ("080298", "ptyas", "noun", "/ˈtaɪəs/", "chi rắn ráo chuột châu Á (Ptyas)"),
    ("080299", "ptychozoon", "noun", "/ˌtaɪkəˈzoʊɑːn/", "chi thằn lằn bay Đông Nam Á"),
    ("080300", "pubby", "adj", "/ˈpʌbi/", "mang không khí quán rượu (lóng Anh)"),
    ("080301", "puberal", "adj", "/ˈpjuːbərəl/", "thuộc tuổi dậy thì (giải phẫu)"),
    ("080302", "publications", "noun", "/ˌpʌblɪˈkeɪʃənz/", "các ấn phẩm; việc xuất bản công bố"),
]

raw = json.load(open("scratch/b37_r01_raw_p3.json"))
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
with open("scratch/b37_r01_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r01_p3 saved OK")
