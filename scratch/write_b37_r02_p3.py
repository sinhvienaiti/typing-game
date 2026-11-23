import json

records = [
    ("080703", "pylorrhoea", "noun", "/ˌpaɪəˈriːə/", "bệnh viêm nha chu chảy mủ (Anh)"),
    ("080704", "pyocyanase", "noun", "/ˌpaɪoʊˈsaɪəˌneɪs/", "chất kháng sinh pyocyanase (cũ)"),
    ("080705", "pyocyanin", "noun", "/ˌpaɪoʊˈsaɪənɪn/", "sắc tố độc xanh lam pyocyanin"),
    ("080706", "pyoderma", "noun", "/ˌpaɪəˈdɜːrmə/", "bệnh viêm da sinh mủ (da liễu)"),
    ("080707", "pyodermic", "adj", "/ˌpaɪəˈdɜːrmɪk/", "thuộc bệnh viêm da sinh mủ"),
    ("080708", "pyogenesis", "noun", "/ˌpaɪəˈdʒɛnəsɪs/", "quá trình tạo mủ, sự sinh mủ"),
    ("080709", "pyoid", "adj", "/ˈpaɪɔɪd/", "giống mủ, có dạng chất mủ"),
    ("080710", "pyometra", "noun", "/ˌpaɪəˈmiːtrə/", "bệnh viêm mủ tử cung (thú y, y học)"),
    ("080711", "pyonephritis", "noun", "/ˌpaɪoʊnəˈfraɪtɪs/", "bệnh viêm thận sinh mủ (y học)"),
    ("080712", "pyorrhea", "noun", "/ˌpaɪəˈriːə/", "viêm nha chu chảy mủ; sự chảy mủ"),
    ("080713", "pyorrhoea", "noun", "/ˌpaɪəˈriːə/", "viêm nha chu chảy mủ (Anh)"),
    ("080714", "pyosis", "noun", "/paɪˈoʊsɪs/", "sự hóa mủ, sự sinh mủ (y học)"),
    ("080715", "pyracanth", "noun", "/ˈpaɪrəˌkænθ/", "cây táo gai lửa (Pyracantha)"),
    ("080716", "pyralid", "noun", "/ˈpɪrəlɪd/", "ngài bướm đêm họ Pyralidae"),
    ("080717", "pyralididae", "noun", "/ˌpɪrəˈlɪdɪˌdiː/", "họ Ngài bướm đêm (Pyralididae)"),
    ("080718", "pyralis", "noun", "/ˈpɪrəlɪs/", "chi ngài sâu bột (Pyralis)"),
    ("080719", "pyramidalism", "noun", "/pɪˈræmɪdəˌlɪzəm/", "thuyết thần bí về kim tự tháp"),
    ("080720", "pyramidally", "adv", "/pɪˈræmɪdəli/", "theo dạng hình chóp, kim tự tháp"),
    ("080721", "pyramidia", "noun", "/ˌpɪrəˈmɪdiə/", "các chỏm đá đỉnh kim tự tháp"),
    ("080722", "pyramidic", "adj", "/ˌpɪrəˈmɪdɪk/", "có hình kim tự tháp, dạng hình chóp"),
    ("080723", "pyramidical", "adj", "/ˌpɪrəˈmɪdɪkəl/", "có dạng hình kim tự tháp, hình chóp"),
    ("080724", "pyramidically", "adv", "/ˌpɪrəˈmɪdɪkli/", "theo dạng hình kim tự tháp"),
    ("080725", "pyramidion", "noun", "/ˌpɪrəˈmɪdiˌɑːn/", "chỏm đá đỉnh kim tự tháp, đài tưởng"),
    ("080726", "pyramidise", "verb", "/ˈpɪrəməˌdaɪz/", "tạo thành hình chóp, tháp (Anh)"),
    ("080727", "pyramidist", "noun", "/ˈpɪrəmɪdɪst/", "nhà nghiên cứu kim tự tháp"),
    ("080728", "pyranometer", "noun", "/ˌpaɪrəˈnɑːmɪtər/", "nhật xạ kế (đo bức xạ mặt trời)"),
    ("080729", "pyrausta", "noun", "/paɪˈrɔːstə/", "chi bướm đêm sâu đục thân Pyrausta"),
    ("080730", "pyrectic", "adj", "/paɪˈrɛktɪk/", "gây sốt; có tác dụng hạ sốt"),
    ("080731", "pyrenocarp", "noun", "/paɪˈriːnəˌkɑːrp/", "quả hạch, quả nạc có nhân cứng"),
    ("080732", "pyrenoid", "noun", "/ˈpaɪrəˌnɔɪd/", "hạt tạo tinh bột trong lục lạp tảo"),
    ("080733", "pyrenomycetes", "noun", "/paɪˌriːnoʊmaɪˈsiːtiːz/", "lớp nấm túi bào tử kín"),
    ("080734", "pyrenophore", "noun", "/paɪˈrɛnəˌfɔːr/", "phần tế bào chất chứa nhân"),
    ("080735", "pyrethrin", "noun", "/paɪˈriːθrɪn/", "hoạt chất trừ sâu pyrethrin"),
    ("080736", "pyrethrins", "noun", "/paɪˈriːθrɪnz/", "nhóm hoạt chất trừ sâu từ hoa cúc"),
    ("080737", "pyrexial", "adj", "/paɪˈrɛksiəl/", "bị sốt, thuộc cơn sốt (y học)"),
    ("080738", "pyrexic", "adj", "/paɪˈrɛksɪk/", "liên quan đến cơn sốt, gây sốt"),
    ("080739", "pyrgeometer", "noun", "/ˌpɜːrdʒiˈɑːmɪtər/", "dụng cụ đo bức xạ hồng ngoại"),
    ("080740", "pyrheliometer", "noun", "/ˌpɜːrˌhiːliˈɑːmɪtər/", "trực xạ kế đo năng lượng mặt trời"),
    ("080741", "pyridoxamine", "noun", "/ˌpɪrɪˈdɑːksəmiːn/", "dẫn xuất vitamin B6 pyridoxamine"),
    ("080742", "pyriform", "adj", "/ˈpɪrəˌfɔːrm/", "có hình quả lê (sinh học)"),
    ("080743", "pyrilamine", "noun", "/paɪˈrɪləmiːn/", "thuốc kháng histamin pyrilamine"),
    ("080744", "pyritic", "adj", "/paɪˈrɪtɪk/", "thuộc quặng pyrit, chứa pyrit sắt"),
    ("080745", "pyritical", "adj", "/paɪˈrɪtɪkəl/", "thuộc quặng pyrit, giống pyrit"),
    ("080746", "pyritiferous", "adj", "/ˌpaɪrəˈtɪfərəs/", "chứa quặng pyrit sắt (địa chất)"),
    ("080747", "pyrocellulose", "noun", "/ˌpaɪroʊˈsɛljəˌloʊs/", "chất nổ nitrocellulose (quân sự)"),
    ("080748", "pyrocephalus", "noun", "/ˌpaɪroʊˈsɛfələs/", "chi chim đớp ruồi đầu đỏ son"),
    ("080749", "pyrochemical", "adj", "/ˌpaɪroʊˈkɛmɪkəl/", "thuộc hóa học nhiệt độ cao"),
    ("080750", "pyrochemically", "adv", "/ˌpaɪroʊˈkɛmɪkli/", "bằng quy trình nhiệt hóa học"),
    ("080751", "pyrochemistry", "noun", "/ˌpaɪroʊˈkɛmɪstri/", "hóa học phản ứng ở nhiệt độ cao"),
    ("080752", "pyroclastic", "adj", "/ˌpaɪroʊˈklæstɪk/", "tạo thành từ mảnh vụn núi lửa"),
    ("080753", "pyroconductivity", "noun", "/ˌpaɪroʊkəndʌkˈtɪvəti/", "tính dẫn điện khi bị nung nóng"),
    ("080754", "pyroelectrical", "adj", "/ˌpaɪroʊɪˈlɛktrɪkəl/", "có tính nhiệt điện (vật lý)"),
    ("080755", "pyroelectricity", "noun", "/ˌpaɪroʊɪlɛkˈtrɪsəti/", "hiện tượng nhiệt điện (tinh thể)"),
    ("080756", "pyrogallic", "adj", "/ˌpaɪrəˈɡælɪk/", "thuộc axit pyrogallol (hóa học)"),
    ("080757", "pyrogenetic", "adj", "/ˌpaɪrədʒəˈnɛtɪk/", "gây sốt; sinh ra nhiệt lượng"),
    ("080758", "pyrogenicity", "noun", "/ˌpaɪrədʒəˈnɪsəti/", "tính chất gây sốt (dược phẩm)"),
    ("080759", "pyrogenous", "adj", "/paɪˈrɑːdʒənəs/", "gây sốt; sinh ra bởi lửa hay nhiệt"),
    ("080760", "pyrograph", "noun", "/ˈpaɪrəˌɡræf/", "bức tranh khắc bằng bút lửa"),
    ("080761", "pyrographer", "noun", "/paɪˈrɑːɡrəfər/", "nghệ nhân vẽ tranh bút lửa"),
    ("080762", "pyrographic", "adj", "/ˌpaɪrəˈɡræfɪk/", "thuộc nghệ thuật vẽ bút lửa"),
    ("080763", "pyrogravure", "noun", "/ˌpaɪrəɡrəˈvjʊr/", "nghệ thuật khắc gỗ da bằng lửa"),
    ("080764", "pyrolaceae", "noun", "/ˌpɪrəˈleɪsiː/", "họ Lộc đề thảo (Pyrolaceae)"),
    ("080765", "pyrolator", "noun", "/paɪˈrɑːlətər/", "tín đồ thờ phụng thần lửa"),
    ("080766", "pyrolatry", "noun", "/paɪˈrɑːlətri/", "tín ngưỡng thờ lửa, bái hỏa"),
    ("080767", "pyroleter", "noun", "/paɪˈrɑːlətər/", "thiết bị dập lửa trên tàu biển"),
    ("080768", "pyroligneous", "adj", "/ˌpaɪrəˈlɪɡniəs/", "thu được từ chưng cất khan gỗ"),
    ("080769", "pyrolignic", "adj", "/ˌpaɪrəˈlɪɡnɪk/", "thuộc axit chưng cất từ gỗ"),
    ("080770", "pyrology", "noun", "/paɪˈrɑːlədʒi/", "khoa học về nhiệt và lửa"),
    ("080771", "pyrolusite", "noun", "/ˌpaɪrəˈluːsaɪt/", "quặng mangan điôxit pyrolusit"),
    ("080772", "pyrolytically", "adv", "/ˌpaɪrəˈlɪtɪkli/", "bằng phương pháp nhiệt phân"),
    ("080773", "pyromagnetic", "adj", "/ˌpaɪroʊmæɡˈnɛtɪk/", "thuộc hiệu ứng nhiệt từ (vật lý)"),
    ("080774", "pyromagnetism", "noun", "/ˌpaɪroʊˈmæɡnəˌtɪzəm/", "hiện tượng từ tính phụ thuộc nhiệt"),
    ("080775", "pyromancy", "noun", "/ˈpaɪroʊˌmænsi/", "thuật xem bói bằng ngọn lửa"),
    ("080776", "pyromaniacal", "adj", "/ˌpaɪroʊməˈnaɪəkəl/", "mắc chứng cuồng phóng hỏa đốt phá"),
    ("080777", "pyrometallurgical", "adj", "/ˌpaɪroʊˌmɛtəˈlɜːrdʒɪkəl/", "thuộc hỏa luyện kim (luyện nhiệt)"),
    ("080778", "pyrometers", "noun", "/paɪˈrɑːmɪtərz/", "những hỏa kế đo nhiệt độ cực cao"),
    ("080779", "pyrometric", "adj", "/ˌpaɪrəˈmɛtrɪk/", "thuộc phép đo nhiệt độ cao"),
    ("080780", "pyrometrical", "adj", "/ˌpaɪrəˈmɛtrɪkəl/", "thuộc phép đo bằng hỏa kế"),
    ("080781", "pyrometrically", "adv", "/ˌpaɪrəˈmɛtrɪkli/", "bằng phương pháp đo nhiệt độ cao"),
    ("080782", "pyrometry", "noun", "/paɪˈrɑːmətri/", "phép đo nhiệt độ cao bằng hỏa kế"),
    ("080783", "pyromorphite", "noun", "/ˌpaɪrəˈmɔːrfaɪt/", "khoáng vật chì pyromorphit"),
    ("080784", "pyromotor", "noun", "/ˈpaɪrəˌmoʊtər/", "động cơ nhiệt dùng khí nóng"),
    ("080785", "pyrophobia", "noun", "/ˌpaɪrəˈfoʊbiə/", "hội chứng ám ảnh sợ lửa"),
    ("080786", "pyrophoric", "adj", "/ˌpaɪrəˈfɔːrɪk/", "tự bốc cháy trong không khí (hóa)"),
    ("080787", "pyrophorus", "noun", "/paɪˈrɑːfərəs/", "bọ bổ củi phát quang vùng nhiệt đới"),
    ("080788", "pyrophosphoric", "adj", "/ˌpaɪroʊfɑːsˈfɔːrɪk/", "thuộc axit pyrophosphoric (hóa học)"),
    ("080789", "pyroscope", "noun", "/ˈpaɪrəˌskoʊp/", "hỏa kế quang học đo bức xạ nhiệt"),
    ("080790", "pyrosis", "noun", "/paɪˈroʊsɪs/", "chứng ợ nóng, trào ngược axit (y)"),
    ("080791", "pyrosphere", "noun", "/ˈpaɪrəˌsfɪr/", "hỏa quyển (lớp magma nóng Trái Đất)"),
    ("080792", "pyrostat", "noun", "/ˈpaɪrəˌstæt/", "bộ điều nhiệt cho lò nhiệt độ cao"),
    ("080793", "pyrotechnically", "adv", "/ˌpaɪrəˈtɛknɪkli/", "về mặt pháo hoa; đầy tài hoa rực rỡ"),
    ("080794", "pyrotechnist", "noun", "/ˌpaɪrəˈtɛknɪst/", "kỹ thuật viên chế tạo pháo hoa"),
    ("080795", "pyrotechnists", "noun", "/ˌpaɪrəˈtɛknɪsts/", "những nghệ nhân làm pháo hoa"),
    ("080796", "pyrotechny", "noun", "/ˈpaɪrəˌtɛkni/", "nghệ thuật làm và đốt pháo hoa"),
    ("080797", "pyroxenic", "adj", "/ˌpaɪrəˈziːnɪk/", "chứa khoáng vật pyroxen (địa chất)"),
    ("080798", "pyroxilin", "noun", "/paɪˈrɑːksəlɪn/", "thuốc nổ bông pyroxylin (biến thể)"),
    ("080799", "pyroxylin", "noun", "/paɪˈrɑːksəlɪn/", "nitrocellulose hòa tan làm sơn, nổ"),
    ("080800", "pyroxyline", "noun", "/paɪˈrɑːksəˌliːn/", "chất pyroxylin (biến thể chính tả)"),
    ("080801", "pyrrhocoridae", "noun", "/ˌpɪrəˈkɔːrɪˌdiː/", "họ Bọ xít lửa đỏ (Pyrrhocoridae)"),
    ("080802", "pyrrhonism", "noun", "/ˈpɪrəˌnɪzəm/", "chủ nghĩa hoài nghi Pyrrho"),
]

raw = json.load(open("scratch/b37_r02_raw_p3.json"))
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
with open("scratch/b37_r02_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r02_p3 saved OK")
