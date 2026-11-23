import json

records = [
    ("079603", "propelled", "verb", "/prəˈpɛld/", "đã đẩy đi, đã thúc đẩy tiến tới"),
    ("079604", "propels", "verb", "/prəˈpɛlz/", "đẩy đi, thúc đẩy tiến về phía trước"),
    ("079605", "propenal", "noun", "/ˈproʊpəˌnæl/", "hợp chất hữu cơ acrolein (hóa học)"),
    ("079606", "propenoate", "noun", "/proʊˈpɛnoʊˌeɪt/", "muối hoặc este propenoate"),
    ("079607", "propenonitrile", "noun", "/proʊˌpɛnoʊˈnaɪtrəl/", "hợp chất acrylonitrile (hóa học)"),
    ("079608", "propension", "noun", "/prəˈpɛnʃən/", "khuynh hướng tự nhiên, thiên hướng"),
    ("079609", "properness", "noun", "/ˈprɑːpərnəs/", "tính đúng đắn, sự thích hợp"),
    ("079610", "properties", "noun", "/ˈprɑːpərtiz/", "tài sản, bất động sản; tính chất"),
    ("079611", "propertyless", "adj", "/ˈprɑːpərtiləs/", "không có tài sản, vô sản"),
    ("079612", "prophage", "noun", "/ˈproʊfeɪdʒ/", "tiền thể thực khuẩn (sinh học)"),
    ("079613", "prophasic", "adj", "/proʊˈfeɪzɪk/", "thuộc kỳ đầu phân bào (sinh học)"),
    ("079614", "prophesied", "verb", "/ˈprɑːfəˌsaɪd/", "đã tiên tri, đã dự đoán tương lai"),
    ("079615", "prophesier", "noun", "/ˈprɑːfəˌsaɪər/", "nhà tiên tri, người đoán trước"),
    ("079616", "prophesies", "verb", "/ˈprɑːfəˌsaɪz/", "tiên tri, tiên đoán tương lai"),
    ("079617", "prophesying", "verb", "/ˈprɑːfəˌsaɪɪŋ/", "tiên tri, tiên đoán tương lai"),
    ("079618", "prophethood", "noun", "/ˈprɑːfɪtˌhʊd/", "sứ mệnh nhà tiên tri, chức tiên tri"),
    ("079619", "propheticalness", "noun", "/prəˈfɛtɪkəlnəs/", "tính chất tiên tri, sự tiên đoán"),
    ("079620", "prophloem", "noun", "/proʊˈfloʊəm/", "mạch rây nguyên sinh (thực vật)"),
    ("079621", "prophototropic", "adj", "/ˌproʊfoʊˈtrɑːpɪk/", "hướng sáng thuận, mọc về phía sáng"),
    ("079622", "prophylactically", "adv", "/ˌproʊfəˈlæktɪkli/", "nhằm phòng bệnh, để dự phòng"),
    ("079623", "prophylaxes", "noun", "/ˌproʊfəˈlæksiːz/", "các biện pháp phòng ngừa bệnh tật"),
    ("079624", "prophyll", "noun", "/ˈproʊfɪl/", "lá bắc con, lá gốc (thực vật học)"),
    ("079625", "prophyllum", "noun", "/proʊˈfɪləm/", "lá bắc con, lá sơ khởi (thực vật)"),
    ("079626", "propinquities", "noun", "/prəˈpɪŋkwətiz/", "sự gần gũi không gian, huyết thống"),
    ("079627", "propionaldehyde", "noun", "/ˌproʊpiəˈnældəˌhaɪd/", "chất hữu cơ propionaldehyde"),
    ("079628", "propitiable", "adj", "/prəˈpɪʃiəbəl/", "có thể xoa dịu, làm nguôi giận"),
    ("079629", "propitiated", "verb", "/prəˈpɪʃiˌeɪtɪd/", "đã xoa dịu, đã làm nguôi cơn giận"),
    ("079630", "propitiates", "verb", "/prəˈpɪʃiˌeɪts/", "xoa dịu, làm lành, làm nguôi giận"),
    ("079631", "propitiating", "verb", "/prəˈpɪʃiˌeɪtɪŋ/", "xoa dịu, làm nguôi giận, cầu hòa"),
    ("079632", "propitiatingly", "adv", "/prəˈpɪʃiˌeɪtɪŋli/", "với vẻ xoa dịu, cầu hòa"),
    ("079633", "propitiative", "adj", "/prəˈpɪʃiətɪv/", "nhằm xoa dịu, có ý làm lành"),
    ("079634", "propitiator", "noun", "/prəˈpɪʃiˌeɪtər/", "người xoa dịu, người hòa giải"),
    ("079635", "propitiatorily", "adv", "/prəˈpɪʃiəˌtɔːrəli/", "nhằm xoa dịu, với thái độ cầu hòa"),
    ("079636", "propitiously", "adv", "/prəˈpɪʃəsli/", "một cách thuận lợi, tốt lành"),
    ("079637", "propitiousness", "noun", "/prəˈpɪʃəsnəs/", "sự thuận lợi, điềm tốt lành"),
    ("079638", "propjet", "noun", "/ˈprɑːpˌdʒɛt/", "máy bay tuabin cánh quạt"),
    ("079639", "proplasm", "noun", "/ˈproʊplæzəm/", "khuôn mẫu, hình mẫu (điêu khắc)"),
    ("079640", "proplastid", "noun", "/proʊˈplæstɪd/", "tiền lạp thể (sinh học thực vật)"),
    ("079641", "propleura", "noun", "/proʊˈplʊrə/", "các mảnh bên ngực trước (côn trùng)"),
    ("079642", "propleuron", "noun", "/proʊˈplʊrɑːn/", "mảnh bên đốt ngực trước (côn trùng)"),
    ("079643", "propman", "noun", "/ˈprɑːpmæn/", "nhân viên phụ trách đạo cụ sân khấu"),
    ("079644", "propodial", "adj", "/proʊˈpoʊdiəl/", "thuộc đốt chi gần (cánh tay, đùi)"),
    ("079645", "propolar", "adj", "/proʊˈpoʊlər/", "trước cực, gần cực (sinh học)"),
    ("079646", "propolis", "noun", "/ˈprɑːpəlɪs/", "keo ong (chất nhựa ong mật tạo ra)"),
    ("079647", "propone", "verb", "/prəˈpoʊn/", "đề xuất, nêu ra, đề nghị (luật cổ)"),
    ("079648", "proportionable", "adj", "/prəˈpɔːrʃənəbəl/", "tương xứng, cân đối theo tỷ lệ"),
    ("079649", "proportionalist", "noun", "/prəˈpɔːrʃənəlɪst/", "người ủng hộ bầu cử tỷ lệ"),
    ("079650", "proportionateness", "noun", "/prəˈpɔːrʃənətnəs/", "sự tương xứng, tính cân đối"),
    ("079651", "proportioned", "verb", "/prəˈpɔːrʃənd/", "đã cân đối, đã chia theo tỷ lệ"),
    ("079652", "proportioner", "noun", "/prəˈpɔːrʃənər/", "người chia phần; bộ định tỷ lệ"),
    ("079653", "proportioning", "verb", "/prəˈpɔːrʃənɪŋ/", "cân đối, chia đều theo tỷ lệ"),
    ("079654", "proportionless", "adj", "/prəˈpɔːrʃənləs/", "thiếu cân đối, không tương xứng"),
    ("079655", "proportionment", "noun", "/prəˈpɔːrʃənmənt/", "sự phân chia cân đối theo tỷ lệ"),
    ("079656", "proportions", "verb", "/prəˈpɔːrʃənz/", "cân đối, chia đều theo tỷ lệ"),
    ("079657", "proposals", "noun", "/prəˈpoʊzəlz/", "các đề xuất, kiến nghị; lời cầu hôn"),
    ("079658", "proposed", "verb", "/prəˈpoʊzd/", "đã đề xuất, dự định; đã cầu hôn"),
    ("079659", "proposes", "verb", "/prəˈpoʊzɪz/", "đề xuất, dự định; cầu hôn"),
    ("079660", "proposing", "verb", "/prəˈpoʊzɪŋ/", "đề xuất, kiến nghị; cầu hôn"),
    ("079661", "propositional", "adj", "/ˌprɑːpəˈzɪʃənəl/", "thuộc mệnh đề (logic học, ngôn ngữ)"),
    ("079662", "propositionally", "adv", "/ˌprɑːpəˈzɪʃənəli/", "dưới dạng mệnh đề, về mặt mệnh đề"),
    ("079663", "propositions", "noun", "/ˌprɑːpəˈzɪʃənz/", "đề xuất; mệnh đề (toán, logic học)"),
    ("079664", "propositus", "noun", "/prəˈpɑːzətəs/", "người khởi điểm cây phả hệ"),
    ("079665", "propounded", "verb", "/prəˈpaʊndɪd/", "đã đề xuất, đã nêu lên thuyết phục"),
    ("079666", "propounder", "noun", "/prəˈpaʊndər/", "người đề xuất (lý thuyết, ý kiến)"),
    ("079667", "propounding", "verb", "/prəˈpaʊndɪŋ/", "đề xuất, nêu ra để xem xét"),
    ("079668", "propounds", "verb", "/prəˈpaʊndz/", "đề xuất, nêu ra để xem xét"),
    ("079669", "propped", "verb", "/prɑːpt/", "đã chống đỡ, đã kê đỡ lên"),
    ("079670", "propping", "verb", "/ˈprɑːpɪŋ/", "chống đỡ, kê đỡ, nâng đỡ"),
    ("079671", "propraetor", "noun", "/proʊˈpriːtər/", "cựu pháp quan làm thống đốc La Mã"),
    ("079672", "propretor", "noun", "/proʊˈpriːtər/", "cựu pháp quan làm thống đốc La Mã"),
    ("079673", "proprietarily", "adv", "/prəˈpraɪəˌtɛrəli/", "thuộc quyền sở hữu độc quyền"),
    ("079674", "proprieties", "noun", "/prəˈpraɪətiz/", "phép lịch sự, chuẩn mực đúng đắn"),
    ("079675", "proprietorial", "adj", "/prəˌpraɪəˈtɔːriəl/", "như chủ sở hữu, mang tính chiếm hữu"),
    ("079676", "proprietorially", "adv", "/prəˌpraɪəˈtɔːriəli/", "với vẻ làm chủ, mang tính chiếm hữu"),
    ("079677", "proprietors", "noun", "/prəˈpraɪətərz/", "chủ sở hữu, chủ doanh nghiệp"),
    ("079678", "proprietorships", "noun", "/prəˈpraɪətərˌʃɪps/", "doanh nghiệp tư nhân; quyền sở hữu"),
    ("079679", "proprioceptor", "noun", "/ˌproʊpriəˈsɛptər/", "thụ thể bản thể (cảm nhận tư thế)"),
    ("079680", "propriogenic", "adj", "/ˌproʊpriəˈdʒɛnɪk/", "tự phát sinh, nội sinh"),
    ("079681", "proprionamide", "noun", "/ˌproʊpriˈɑːnəmaɪd/", "hợp chất proprionamide (hóa học)"),
    ("079682", "propterygia", "noun", "/ˌprɑːptəˈrɪdʒiə/", "các xương sụn gốc vây trước (cá)"),
    ("079683", "propterygium", "noun", "/ˌprɑːptəˈrɪdʒiəm/", "xương sụn gốc vây trước (cá sụn)"),
    ("079684", "proptosis", "noun", "/prɑːpˈtoʊsɪs/", "chứng lồi nhãn cầu (y học)"),
    ("079685", "propulsatory", "adj", "/prəˈpʌlsəˌtɔːri/", "có tác dụng đẩy tới, dồn tới"),
    ("079686", "propulsor", "noun", "/prəˈpʌlsər/", "bộ phận đẩy, động cơ đẩy tàu"),
    ("079687", "propulsory", "adj", "/prəˈpʌlsəri/", "có lực đẩy, dùng để đẩy tới"),
    ("079688", "propupa", "noun", "/proʊˈpjuːpə/", "giai đoạn tiền nhộng (côn trùng)"),
    ("079689", "propygidium", "noun", "/ˌproʊpɪˈdʒɪdiəm/", "đốt bụng áp chót (bọ cánh cứng)"),
    ("079690", "propylaea", "noun", "/ˌprɑːpəˈliːə/", "tiền sảnh cổng đền Hy Lạp cổ đại"),
    ("079691", "propylaeum", "noun", "/ˌprɑːpəˈliːəm/", "cổng lớn dẫn vào điện thờ cổ đại"),
    ("079692", "propylite", "noun", "/ˈprɑːpəˌlaɪt/", "đá propylit (địa chất)"),
    ("079693", "propylon", "noun", "/ˈprɑːpəˌlɑːn/", "cổng dẫn vào đền thờ Ai Cập cổ"),
    ("079694", "propylona", "noun", "/ˌprɑːpəˈloʊnə/", "những cổng dẫn vào đền thờ cổ"),
    ("079695", "prorata", "adv", "/ˌproʊˈrɑːtə/", "theo tỷ lệ tương ứng"),
    ("079696", "prorogations", "noun", "/ˌproʊrəˈɡeɪʃənz/", "những lần tạm hoãn kỳ họp quốc hội"),
    ("079697", "prorogued", "verb", "/proʊˈroʊɡd/", "đã tạm hoãn, đã bế mạc (kỳ họp)"),
    ("079698", "prorogues", "verb", "/proʊˈroʊɡz/", "tạm hoãn, đình kỳ họp (quốc hội)"),
    ("079699", "proroguing", "verb", "/proʊˈroʊɡɪŋ/", "tạm hoãn, đình kỳ họp (quốc hội)"),
    ("079700", "prosaicness", "noun", "/proʊˈzeɪɪknəs/", "sự tẻ nhạt, tính chất khô khan"),
    ("079701", "prosaism", "noun", "/ˈproʊzeɪˌɪzəm/", "lối diễn đạt tầm thường, khô khan"),
    ("079702", "prosaist", "noun", "/ˈproʊzeɪɪst/", "nhà văn xuôi; người khô khan"),
]

raw = json.load(open("scratch/b36_r10_raw_p2.json"))
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
with open("scratch/b36_r10_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b36_r10_p2 saved OK")
