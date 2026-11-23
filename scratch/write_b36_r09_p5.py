import json

records = [
    ("079403", "profited", "verb", "/ˈprɑːfɪtɪd/", "đã thu lợi, hưởng lợi; có ích"),
    ("079404", "profiteered", "verb", "/ˌprɑːfɪˈtɪrd/", "đã đầu cơ trục lợi, bán cắt cổ"),
    ("079405", "profiteering", "verb", "/ˌprɑːfɪˈtɪrɪŋ/", "đầu cơ trục lợi, thu lời bất chính"),
    ("079406", "profiteers", "noun", "/ˌprɑːfɪˈtɪrz/", "những kẻ đầu cơ trục lợi"),
    ("079407", "profiting", "verb", "/ˈprɑːfɪtɪŋ/", "thu lợi, hưởng lợi; sinh lời"),
    ("079408", "profitlessly", "adv", "/ˈprɑːfɪtləsli/", "không sinh lời, vô ích, công cốc"),
    ("079409", "profligately", "adv", "/ˈprɑːflɪɡətli/", "phóng đãng, trác táng, hoang phí"),
    ("079410", "profoundity", "noun", "/prəˈfaʊndəti/", "sự sâu sắc, chiều sâu (ít dùng)"),
    ("079411", "profuseness", "noun", "/prəˈfjuːsnəs/", "sự dồi dào, tính hào phóng"),
    ("079412", "profusions", "noun", "/prəˈfjuːʒənz/", "sự dồi dào, lượng phong phú"),
    ("079413", "prog", "noun", "/prɑːɡ/", "thức ăn, lương thực; giám thị"),
    ("079414", "progamete", "noun", "/proʊˈɡæmiːt/", "tiền giao tử (sinh vật học)"),
    ("079415", "progamic", "adj", "/proʊˈɡæmɪk/", "trước thụ tinh, tiền giao phối"),
    ("079416", "progenesis", "noun", "/proʊˈdʒɛnəsɪs/", "hiện tượng thành thục sinh dục sớm"),
    ("079417", "progenetic", "adj", "/ˌproʊdʒəˈnɛtɪk/", "thành thục sinh dục sớm (sinh học)"),
    ("079418", "progenitive", "adj", "/proʊˈdʒɛnətɪv/", "có khả năng sinh con cái"),
    ("079419", "progenitorial", "adj", "/prəˌdʒɛnəˈtɔːriəl/", "thuộc tổ tiên, thuộc ông cha"),
    ("079420", "progenitress", "noun", "/proʊˈdʒɛnətrəs/", "bà tổ, nữ thủy tổ"),
    ("079421", "progenitrix", "noun", "/proʊˈdʒɛnətrɪks/", "bà tổ, nữ thủy tổ"),
    ("079422", "progeniture", "noun", "/proʊˈdʒɛnətʃər/", "con cháu, dòng dõi; sự sinh sản"),
    ("079423", "progeotropism", "noun", "/ˌproʊdʒiˈɑːtrəˌpɪzəm/", "tính hướng đất thuận (thực vật)"),
    ("079424", "progestational", "adj", "/ˌproʊdʒɛˈsteɪʃənəl/", "thuộc hormone trợ thai progesterone"),
    ("079425", "proggins", "noun", "/ˈprɑːɡɪnz/", "giám thị đại học (lóng cổ)"),
    ("079426", "proglottis", "noun", "/proʊˈɡlɑːtɪs/", "đốt sán dây (sinh học)"),
    ("079427", "prognathic", "adj", "/prɑːɡˈnæθɪk/", "vẩu, có hàm dưới nhô ra trước"),
    ("079428", "prognathous", "adj", "/ˈprɑːɡnəθəs/", "vẩu, có hàm dưới nhô ra trước"),
    ("079429", "progne", "noun", "/ˈprɑːɡni/", "chi chim nhạn lớn (Progne)"),
    ("079430", "prognoses", "noun", "/prɑːɡˈnoʊsiːz/", "những tiên lượng (bệnh tật)"),
    ("079431", "prognosticable", "adj", "/prɑːɡˈnɑːstɪkəbəl/", "có thể tiên đoán, dự báo được"),
    ("079432", "prognosticated", "verb", "/prɑːɡˈnɑːstəˌkeɪtɪd/", "đã dự đoán, đã tiên đoán"),
    ("079433", "prognosticates", "verb", "/prɑːɡˈnɑːstəˌkeɪts/", "dự đoán, tiên đoán, báo trước"),
    ("079434", "prognosticating", "verb", "/prɑːɡˈnɑːstəˌkeɪtɪŋ/", "dự đoán, tiên đoán, báo trước"),
    ("079435", "prognosticative", "adj", "/prɑːɡˈnɑːstəˌkeɪtɪv/", "có tính tiên đoán, dự báo"),
    ("079436", "prognosticatory", "adj", "/prɑːɡˈnɑːstəkəˌtɔːri/", "báo trước, mang tính tiên tri"),
    ("079437", "prograde", "adj", "/ˈproʊɡreɪd/", "chuyển động thuận (thiên văn học)"),
    ("079438", "programed", "adj", "/ˈproʊɡræmd/", "đã được lập trình, đã lên lịch"),
    ("079439", "programer", "noun", "/ˈproʊɡræmər/", "lập trình viên (biến thể chính tả)"),
    ("079440", "programmability", "noun", "/ˌproʊɡræməˈbɪləti/", "khả năng lập trình được"),
    ("079441", "programmable", "adj", "/ˈproʊɡræməbəl/", "có thể lập trình được"),
    ("079442", "programmed", "verb", "/ˈproʊɡræmd/", "đã lập trình; đã lên chương trình"),
    ("079443", "programmes", "verb", "/ˈproʊɡræmz/", "lập trình; lên lịch trình (Anh)"),
    ("079444", "programmings", "noun", "/ˈproʊɡræmɪŋz/", "chương trình phát sóng; lập trình"),
    ("079445", "programs", "verb", "/ˈproʊɡræmz/", "lập trình; lên chương trình"),
    ("079446", "progressed", "verb", "/prəˈɡrɛst/", "đã tiến bộ, đã tiến triển"),
    ("079447", "progresses", "verb", "/prəˈɡrɛsɪz/", "tiến bộ, tiến triển, phát triển"),
    ("079448", "progressing", "verb", "/prəˈɡrɛsɪŋ/", "tiến bộ, tiến triển, tiến tới"),
    ("079449", "progressional", "adj", "/prəˈɡrɛʃənəl/", "thuộc sự tiến triển, theo cấp tiến"),
    ("079450", "progressionist", "noun", "/prəˈɡrɛʃənɪst/", "người tin vào thuyết tiến hóa"),
    ("079451", "progressions", "noun", "/prəˈɡrɛʃənz/", "sự tiến triển; dãy cấp số (toán)"),
    ("079452", "progressist", "noun", "/prəˈɡrɛsɪst/", "người cấp tiến, người theo tiến bộ"),
    ("079453", "progressivist", "noun", "/prəˈɡrɛsɪvɪst/", "người theo chủ nghĩa cấp tiến"),
    ("079454", "progressivistic", "adj", "/prəˌɡrɛsəˈvɪstɪk/", "thuộc chủ nghĩa cấp tiến"),
    ("079455", "progymnosperm", "noun", "/ˌproʊdʒɪmˈnɑːspɜːrm/", "thực vật tiền hạt trần"),
    ("079456", "prohibiter", "noun", "/proʊˈhɪbɪtər/", "người ngăn cấm, người cấm đoán"),
    ("079457", "prohibiting", "verb", "/proʊˈhɪbɪtɪŋ/", "ngăn cấm, nghiêm cấm, cản trở"),
    ("079458", "prohibitionism", "noun", "/ˌproʊhɪˈbɪʃənˌɪzəm/", "chủ trương cấm rượu (lịch sử Mỹ)"),
    ("079459", "prohibitiveness", "noun", "/proʊˈhɪbɪtɪvnəs/", "tính ngăn cấm; mức giá quá đắt"),
    ("079460", "prohibitor", "noun", "/proʊˈhɪbɪtər/", "người ngăn cấm, cơ quan cấm đoán"),
    ("079461", "prohibits", "verb", "/proʊˈhɪbɪts/", "ngăn cấm, nghiêm cấm, cản trở"),
    ("079462", "projectable", "adj", "/prəˈdʒɛktəbəl/", "có thể phóng chiếu; có thể dự báo"),
    ("079463", "projectiles", "noun", "/prəˈdʒɛktəlz/", "đầu đạn, tên lửa, vật phóng"),
    ("079464", "projectional", "adj", "/prəˈdʒɛkʃənəl/", "thuộc phép chiếu, phóng chiếu"),
    ("079465", "projections", "noun", "/prəˈdʒɛkʃənz/", "sự dự báo; hình chiếu; phần nhô ra"),
    ("079466", "projective", "adj", "/prəˈdʒɛktɪv/", "thuộc phép chiếu, xạ ảnh (toán học)"),
    ("079467", "projectively", "adv", "/prəˈdʒɛktɪvli/", "theo phép chiếu, bằng phép chiếu"),
    ("079468", "projectivity", "noun", "/ˌprɑːdʒɛkˈtɪvəti/", "phép biến đổi xạ ảnh (toán học)"),
    ("079469", "projects", "verb", "/prəˈdʒɛkts/", "dự kiến, ước tính; phóng, chiếu"),
    ("079470", "prokayotae", "noun", "/ˌproʊkæriˈoʊtiː/", "giới sinh vật nhân sơ (biến thể)"),
    ("079471", "prolamine", "noun", "/proʊˈlæmiːn/", "prolamin (protein thực vật hạt)"),
    ("079472", "prolan", "noun", "/ˈproʊlæn/", "hormone hướng sinh dục prolan"),
    ("079473", "prolape", "verb", "/proʊˈlæps/", "sa xuống, tụt xuống (y học)"),
    ("079474", "prolapsed", "verb", "/proʊˈlæpst/", "đã bị sa, đã tụt xuống (tạng)"),
    ("079475", "prolapses", "verb", "/proʊˈlæpsɪz/", "sa xuống, tụt xuống (cơ quan)"),
    ("079476", "prolapsing", "verb", "/proʊˈlæpsɪŋ/", "sa xuống, tụt xuống (y học)"),
    ("079477", "prolapsus", "noun", "/proʊˈlæpsəs/", "chứng sa tạng (y học)"),
    ("079478", "prolately", "adv", "/ˈproʊleɪtli/", "theo dạng thuôn dài (hình cầu dài)"),
    ("079479", "prolateness", "noun", "/ˈproʊleɪtnəs/", "hình dáng thuôn dài ở hai cực"),
    ("079480", "prolates", "verb", "/ˈproʊleɪts/", "kéo dài ra; phát âm, thốt ra (cổ)"),
    ("079481", "prolative", "adj", "/ˈproʊlətɪv/", "bổ nghĩa nguyên mẫu (ngữ pháp)"),
    ("079482", "prolegomena", "noun", "/ˌprɑːlɪˈɡɑːmənə/", "lời dẫn nhập, phần mở đầu sách"),
    ("079483", "prolegomenon", "noun", "/ˌprɑːlɪˈɡɑːməˌnɑːn/", "lời mở đầu, bài luận dẫn nhập"),
    ("079484", "prolegomenous", "adj", "/ˌprɑːlɪˈɡɑːmənəs/", "có tính chất mở đầu, dẫn nhập"),
    ("079485", "prolegs", "noun", "/ˈproʊlɛɡz/", "các chân giả ở bụng (sâu bướm)"),
    ("079486", "proleptic", "adj", "/proʊˈlɛptɪk/", "nói trước tương lai, đón trước"),
    ("079487", "proletarianise", "verb", "/ˌproʊlɪˈtɛriəˌnaɪz/", "vô sản hóa (Anh)"),
    ("079488", "proletarianism", "noun", "/ˌproʊlɪˈtɛriəˌnɪzəm/", "tình trạng vô sản; ý thức vô sản"),
    ("079489", "proletarianize", "verb", "/ˌproʊlɪˈtɛriəˌnaɪz/", "vô sản hóa (biến thành vô sản)"),
    ("079490", "proletariate", "noun", "/ˌproʊlɪˈtɛriət/", "giai cấp vô sản (biến thể cổ)"),
    ("079491", "proletary", "adj", "/ˈproʊləˌtɛri/", "thuộc tầng lớp lao động vô sản (cổ)"),
    ("079492", "prolicidal", "adj", "/ˌproʊlɪˈsaɪdəl/", "liên quan đến hành vi giết con"),
    ("079493", "prolicide", "noun", "/ˈproʊlɪˌsaɪd/", "tội giết con đẻ (hay thai nhi)"),
    ("079494", "proliferated", "verb", "/prəˈlɪfəˌreɪtɪd/", "đã sinh sôi nảy nở nhanh, tăng vọt"),
    ("079495", "proliferates", "verb", "/prəˈlɪfəˌreɪts/", "sinh sôi nảy nở, tăng sinh nhanh"),
    ("079496", "proliferating", "verb", "/prəˈlɪfəˌreɪtɪŋ/", "sinh sôi nảy nở, tăng sinh nhanh"),
    ("079497", "proliferative", "adj", "/prəˈlɪfəˌreɪtɪv/", "tăng sinh nhanh, sinh sôi mạnh"),
    ("079498", "proliferator", "noun", "/prəˈlɪfəˌreɪtər/", "tác nhân gây tăng sinh (sinh học)"),
    ("079499", "proliferous", "adj", "/prəˈlɪfərəs/", "nảy mầm chồi mới, sinh sôi mạnh"),
    ("079500", "proliferously", "adv", "/prəˈlɪfərəsli/", "nảy nở nhiều, sinh sôi dồi dào"),
    ("079501", "prolifically", "adv", "/prəˈlɪfɪkli/", "sinh sản nhiều, sáng tác dồi dào"),
    ("079502", "prolificity", "noun", "/ˌproʊlɪˈfɪsəti/", "sức sinh sản dồi dào, tính sai quả"),
]

raw = json.load(open("scratch/b36_r09_raw_p5.json"))
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
with open("scratch/b36_r09_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b36_r09_p5 saved OK")
