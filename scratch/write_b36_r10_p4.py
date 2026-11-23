import json

records = [
    ("079803", "protectest", "verb", "/prəˈtɛktəst/", "bảo vệ, che chở (ngôi 2 cổ)"),
    ("079804", "protecteth", "verb", "/prəˈtɛktəθ/", "bảo vệ, che chở (ngôi 3 cổ)"),
    ("079805", "protectingly", "adv", "/prəˈtɛktɪŋli/", "với vẻ bảo vệ, che chở"),
    ("079806", "protectional", "adj", "/prəˈtɛkʃənəl/", "thuộc sự bảo vệ, mang tính bảo hộ"),
    ("079807", "protectionisms", "noun", "/prəˈtɛkʃəˌnɪzəmz/", "các chính sách bảo hộ mậu dịch"),
    ("079808", "protectionists", "noun", "/prəˈtɛkʃənɪsts/", "những người theo chủ nghĩa bảo hộ"),
    ("079809", "protections", "noun", "/prəˈtɛkʃənz/", "sự bảo vệ, biện pháp bảo hộ"),
    ("079810", "protectoral", "adj", "/prəˈtɛktərəl/", "thuộc quan bảo hộ, chế độ bảo hộ"),
    ("079811", "protectorates", "noun", "/prəˈtɛktərɪts/", "các nước bảo hộ, xứ bảo hộ"),
    ("079812", "protectories", "noun", "/prəˈtɛktəriz/", "các trại bảo trợ trẻ mồ côi"),
    ("079813", "protectors", "noun", "/prəˈtɛktərz/", "người bảo vệ; thiết bị bảo hộ"),
    ("079814", "protectorship", "noun", "/prəˈtɛktərʃɪp/", "chức vị quan bảo quốc (lịch sử Anh)"),
    ("079815", "protectorships", "noun", "/prəˈtɛktərʃɪps/", "các chức vị bảo hộ, nhiếp chính"),
    ("079816", "protectory", "noun", "/prəˈtɛktəri/", "trại bảo trợ trẻ em cơ nhỡ"),
    ("079817", "protectress", "noun", "/prəˈtɛktrəs/", "nữ bảo vệ, nữ ân nhân che chở"),
    ("079818", "protectresses", "noun", "/prəˈtɛktrəsɪz/", "những nữ ân nhân bảo vệ"),
    ("079819", "proteid", "noun", "/ˈproʊtiˌɪd/", "protein phức hợp (thuật ngữ cũ)"),
    ("079820", "proteidae", "noun", "/ˈproʊtiɪˌdiː/", "họ kỳ giông bùn (Proteidae)"),
    ("079821", "proteiform", "adj", "/ˈproʊtiəˌfɔːrm/", "biến hình đa dạng, hay biến đổi"),
    ("079822", "proteinic", "adj", "/proʊˈtiːnɪk/", "thuộc chất đạm, có protein"),
    ("079823", "proteinous", "adj", "/proʊˈtiːnəs/", "giàu chất đạm, mang tính protein"),
    ("079824", "proteles", "noun", "/ˈprɑːtəˌliːz/", "chi chó sói đất (Proteles)"),
    ("079825", "protempore", "adj", "/ˌproʊˈtɛmpəri/", "tạm thời, lâm thời (tiếng Latin)"),
    ("079826", "protend", "verb", "/proʊˈtɛnd/", "duỗi ra, kéo dài ra (văn học cổ)"),
    ("079827", "protensive", "adj", "/proʊˈtɛnsɪv/", "kéo dài theo thời gian, không gian"),
    ("079828", "proteoclastic", "adj", "/ˌproʊtiəˈklæstɪk/", "phân giải protein, tiêu đạm"),
    ("079829", "proteolitic", "adj", "/ˌproʊtiəˈlɪtɪk/", "phân giải protein (biến thể)"),
    ("079830", "proteose", "noun", "/ˈproʊtiˌoʊs/", "chất proteose (thủy phân protein)"),
    ("079831", "proteosome", "noun", "/ˈproʊtiəˌsoʊm/", "hạt phức hợp protein (vắc-xin mũi)"),
    ("079832", "proterandric", "adj", "/ˌproʊtərˈændrɪk/", "nhị chín trước, đực trước"),
    ("079833", "proterandrous", "adj", "/ˌproʊtərˈændrəs/", "có nhị chín trước (thực vật học)"),
    ("079834", "proterandry", "noun", "/ˌproʊtərˈændri/", "tính nhị chín trước nhụy (thực vật)"),
    ("079835", "proteranthous", "adj", "/ˌproʊtərˈænθəs/", "nở hoa trước khi ra lá (cây)"),
    ("079836", "proteranthy", "noun", "/ˌproʊtərˈænθi/", "hiện tượng hoa nở trước khi ra lá"),
    ("079837", "proterochampsa", "noun", "/ˌproʊtəroʊˈkæmpsə/", "thằn lằn tiền sử Proterochampsa"),
    ("079838", "proterogynic", "adj", "/ˌproʊtərəˈdʒɪnɪk/", "nhụy chín trước, cái trước"),
    ("079839", "proterogynous", "adj", "/ˌproʊtəˈrɑːdʒənəs/", "có nhụy chín trước (thực vật học)"),
    ("079840", "proterogyny", "noun", "/ˌproʊtəˈrɑːdʒəni/", "tính nhụy chín trước nhị"),
    ("079841", "protestantize", "verb", "/ˈprɑːtəstənˌtaɪz/", "cải đạo theo đạo Tin Lành"),
    ("079842", "protestator", "noun", "/ˌprɑːtəˈsteɪtər/", "người phản đối, người kháng nghị"),
    ("079843", "protested", "verb", "/prəˈtɛstɪd/", "đã phản đối, đã kháng nghị"),
    ("079844", "protesters", "noun", "/ˈproʊtɛstərz/", "những người biểu tình, phản đối"),
    ("079845", "protesting", "verb", "/prəˈtɛstɪŋ/", "phản đối, biểu tình; khẳng định"),
    ("079846", "protestingly", "adv", "/prəˈtɛstɪŋli/", "với giọng phản đối, phản kháng"),
    ("079847", "protestor", "noun", "/ˈproʊtɛstər/", "người biểu tình, người phản đối"),
    ("079848", "protestors", "noun", "/ˈproʊtɛstərz/", "những người biểu tình, phản đối"),
    ("079849", "protests", "verb", "/prəˈtɛsts/", "phản đối, biểu tình; khẳng định"),
    ("079850", "prothalamion", "noun", "/ˌproʊθəˈleɪmiən/", "bài thơ chúc mừng hôn lễ"),
    ("079851", "prothalamium", "noun", "/ˌproʊθəˈleɪmiəm/", "bài ca chúc mừng trước lễ cưới"),
    ("079852", "prothallial", "adj", "/proʊˈθæliəl/", "thuộc nguyên tản (dương xỉ)"),
    ("079853", "prothallium", "noun", "/proʊˈθæliəm/", "nguyên tản, thể giao tử (dương xỉ)"),
    ("079854", "prothalloid", "adj", "/proʊˈθælɔɪd/", "có dạng nguyên tản (thực vật)"),
    ("079855", "prothesis", "noun", "/ˈprɑːθəsɪs/", "bàn dâng lễ; sự thêm âm đầu từ"),
    ("079856", "prothetic", "adj", "/proʊˈθɛtɪk/", "thuộc âm chêm đầu từ (ngôn ngữ)"),
    ("079857", "prothetically", "adv", "/proʊˈθɛtɪkli/", "theo lối thêm âm đầu từ"),
    ("079858", "prothonotaries", "noun", "/ˌproʊθəˈnoʊtəriz/", "các chánh lục sự tòa án"),
    ("079859", "prothonotary", "noun", "/ˌproʊθəˈnoʊtəri/", "chánh lục sự tòa án; chưởng ấn"),
    ("079860", "prothoracic", "adj", "/ˌproʊθɔːˈræsɪk/", "thuộc đốt ngực trước (côn trùng)"),
    ("079861", "prothrombinase", "noun", "/proʊˈθrɑːmbəˌneɪs/", "enzym prothrombinase (đông máu)"),
    ("079862", "protirelin", "noun", "/proʊˈtaɪrəlɪn/", "hormone giải phóng thyrotropin"),
    ("079863", "protistan", "noun", "/proʊˈtɪstən/", "sinh vật nguyên sinh đơn bào"),
    ("079864", "protoactinium", "noun", "/ˌproʊtoʊækˈtɪniəm/", "nguyên tố hóa học protactini"),
    ("079865", "protoaecidium", "noun", "/ˌproʊtoʊiˈsɪdiəm/", "tiền túi bào tử gỉ (nấm học)"),
    ("079866", "protoanthropology", "noun", "/ˌproʊtoʊˌænθrəˈpɑːlədʒi/", "nhân học sơ khai thời tiền sử"),
    ("079867", "protoarchaeology", "noun", "/ˌproʊtoʊˌɑːrkiˈɑːlədʒi/", "khảo cổ học giai đoạn sơ sử"),
    ("079868", "protoarcheology", "noun", "/ˌproʊtoʊˌɑːrkiˈɑːlədʒi/", "khảo cổ học giai đoạn sơ sử"),
    ("079869", "protoavis", "noun", "/ˌproʊtoʊˈeɪvɪs/", "hóa thạch Protoavis (cổ sinh)"),
    ("079870", "protobasidium", "noun", "/ˌproʊtoʊbəˈsɪdiəm/", "tiền đảm (sinh học nấm)"),
    ("079871", "protobios", "noun", "/ˌproʊtoʊˈbaɪɑːs/", "dạng sống sơ khai, vi sinh vật"),
    ("079872", "protoblast", "noun", "/ˈproʊtəˌblæst/", "tế bào phôi trần, tế bào mầm"),
    ("079873", "protocerebral", "adj", "/ˌproʊtəsəˈriːbrəl/", "thuộc não trước (côn trùng)"),
    ("079874", "protocerebron", "noun", "/ˌproʊtəsəˈriːbrɑːn/", "não trước (chân khớp, côn trùng)"),
    ("079875", "protocerebrum", "noun", "/ˌproʊtəsəˈriːbrəm/", "não trước (chân khớp, côn trùng)"),
    ("079876", "protochlorophyll", "noun", "/ˌproʊtəˈklɔːrəfɪl/", "tiền diệp lục tố (thực vật)"),
    ("079877", "protocols", "noun", "/ˈproʊtəˌkɔːlz/", "các giao thức; nghi thức ngoại giao"),
    ("079878", "protoconch", "noun", "/ˈproʊtəˌkɑːŋk/", "vỏ ấu trùng ban đầu (ốc, động vật)"),
    ("079879", "protocone", "noun", "/ˈproʊtəˌkoʊn/", "mấu chính răng hàm trên (giải phẫu)"),
    ("079880", "protoconid", "noun", "/ˌproʊtəˈkɑːnɪd/", "mấu chính răng hàm dưới (giải phẫu)"),
    ("079881", "protocorm", "noun", "/ˈproʊtəˌkɔːrm/", "mầm thân rễ non (lan, thực vật)"),
    ("079882", "protocosta", "noun", "/ˌproʊtəˈkɑːstə/", "gân mép trước cánh (côn trùng)"),
    ("079883", "protocranium", "noun", "/ˌproʊtəˈkreɪniəm/", "vùng chẩm sọ (côn trùng học)"),
    ("079884", "protoctist", "noun", "/prəˈtɑːktɪst/", "sinh vật nguyên sinh (tảo, đơn bào)"),
    ("079885", "protoctista", "noun", "/ˌproʊtɑːkˈtɪstə/", "giới Nguyên sinh (sinh học)"),
    ("079886", "protogen", "noun", "/ˈproʊtəˌdʒɛn/", "gen nguyên thủy; axit lipoic"),
    ("079887", "protogenesis", "noun", "/ˌproʊtəˈdʒɛnəsɪs/", "quá trình phát sinh sự sống đầu"),
    ("079888", "protogenic", "adj", "/ˌproʊtəˈdʒɛnɪk/", "khởi sinh sớm (địa chất, sinh học)"),
    ("079889", "protogeometric", "adj", "/ˌproʊtoʊdʒiəˈmɛtrɪk/", "thuộc thời kỳ tiền hình học"),
    ("079890", "protoheme", "noun", "/ˈproʊtoʊˌhiːm/", "nhóm heme b, hồng cầu tố (sinh hóa)"),
    ("079891", "protohemin", "noun", "/ˌproʊtoʊˈhiːmɪn/", "hợp chất protohemin (hóa sinh)"),
    ("079892", "protohippus", "noun", "/ˌproʊtəˈhɪpəs/", "chi ngựa tiền sử Protohippus"),
    ("079893", "protohistory", "noun", "/ˌproʊtoʊˈhɪstəri/", "giai đoạn sơ sử, tiền sử học"),
    ("079894", "protohuman", "adj", "/ˌproʊtoʊˈhjuːmən/", "thuộc người vượn cổ, tiền nhân"),
    ("079895", "protolanguage", "noun", "/ˈproʊtoʊˌlæŋɡwɪdʒ/", "ngôn ngữ tổ tiên (ngôn ngữ học)"),
    ("079896", "protoleucocyte", "noun", "/ˌproʊtəˈluːkəˌsaɪt/", "tiền bạch cầu, bạch cầu non"),
    ("079897", "protolithic", "adj", "/ˌproʊtəˈlɪθɪk/", "thuộc thời kỳ đồ đá sơ khai"),
    ("079898", "protologisms", "noun", "/prəˈtɑːləˌdʒɪzəmz/", "các từ mới đặt chưa phổ biến"),
    ("079899", "protology", "noun", "/prəˈtɑːlədʒi/", "thuyết nguyên thủy, nghiên cứu gốc"),
    ("079900", "protomammal", "noun", "/ˌproʊtəˈmæməl/", "động vật tiền thú (hóa thạch)"),
    ("079901", "protomartyr", "noun", "/ˈproʊtəˌmɑːrtər/", "người tử vì đạo đầu tiên"),
    ("079902", "protomerite", "noun", "/ˌproʊtəˈmɛraɪt/", "phần trước tế bào trùng hai ngăn"),
]

raw = json.load(open("scratch/b36_r10_raw_p4.json"))
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
with open("scratch/b36_r10_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b36_r10_p4 saved OK")
