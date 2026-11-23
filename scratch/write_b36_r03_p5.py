import json

rows = [
    ("076403", "phrased", "verb", "/freɪzd/", "đã diễn đạt bằng lời, đặt câu"),
    ("076404", "phraseogram", "noun", "/ˈfreɪziəˌɡræm/", "ký hiệu tốc ký ghi cả cụm từ"),
    ("076405", "phraseograph", "noun", "/ˈfreɪziəˌɡræf/", "cụm từ viết bằng ký hiệu tốc ký"),
    ("076406", "phraseographic", "adj", "/ˌfreɪziəˈɡræfɪk/", "thuộc cách ghi tốc ký cả cụm từ"),
    ("076407", "phraseological", "adj", "/ˌfreɪziəˈlɒdʒɪkəl/", "thuộc ngữ cú, cụm từ cố định"),
    ("076408", "phraseologist", "noun", "/ˌfreɪziˈɒlədʒɪst/", "nhà nghiên cứu thành ngữ, ngữ cú"),
    ("076409", "phrases", "verb", "/ˈfreɪzɪz/", "diễn đạt bằng lời, đặt câu"),
    ("076410", "phreaking", "noun", "/ˈfriːkɪŋ/", "xâm nhập phá hệ thống điện thoại"),
    ("076411", "phrenalgia", "noun", "/frɪˈnældʒə/", "chứng đau dây thần kinh; u sầu"),
    ("076412", "phrenetic", "adj", "/frɪˈnɛtɪk/", "cuồng nhiệt, điên cuồng"),
    ("076413", "phrenitic", "adj", "/frɪˈnɪtɪk/", "bị viêm não; điên loạn"),
    ("076414", "phrenitis", "noun", "/frɪˈnaɪtɪs/", "bệnh viêm não, mê sảng (y học cổ)"),
    ("076415", "phrenologic", "adj", "/ˌfrɛnəˈlɒdʒɪk/", "thuộc khoa xem sọ (não tướng học)"),
    ("076416", "phretium", "noun", "/ˈfriːtiəm/", "quần xã sinh vật hồ chứa nhân tạo"),
    ("076417", "phrontistery", "noun", "/ˈfrɒntɪstəri/", "trường học, nơi học tập nghiên cứu"),
    ("076418", "phrynosoma", "noun", "/ˌfraɪnəˈsoʊmə/", "chi thằn lằn có sừng (Phrynosoma)"),
    ("076419", "phthiriasis", "noun", "/ˌθaɪˈraɪəsɪs/", "bệnh rận ký sinh, chấy rận"),
    ("076420", "phthiriidae", "noun", "/θaɪˈraɪɪdiː/", "họ Rận mu (Phthiriidae)"),
    ("076421", "phthirius", "noun", "/ˈθaɪriəs/", "chi rận mu (Pthirus)"),
    ("076422", "phthirus", "noun", "/ˈθaɪrəs/", "chi rận mu (Pthirus)"),
    ("076423", "phthisical", "adj", "/ˈtaɪzɪkəl/", "mắc bệnh lao phổi; gầy mòn"),
    ("076424", "phthorimaea", "noun", "/ˌθɒrɪˈmiːə/", "chi bướm sâu đục củ khoai tây"),
    ("076425", "phusis", "noun", "/ˈfjuːsɪs/", "tự nhiên, bản tính (triết Hy Lạp)"),
    ("076426", "phut", "noun", "/fʌt/", "tiếng xì xịt; hỏng bét tiêu tan"),
    ("076427", "phyad", "noun", "/ˈfaɪæd/", "dạng di truyền sinh thái"),
    ("076428", "phycobilin", "noun", "/ˌfaɪkoʊˈbaɪlɪn/", "sắc tố tảo lam phycobilin"),
    ("076429", "phycological", "adj", "/ˌfaɪkəˈlɒdʒɪkəl/", "thuộc tảo học (nghiên cứu tảo)"),
    ("076430", "phycomycete", "noun", "/ˌfaɪkoʊˈmaɪsiːt/", "nấm tảo (lớp nấm bậc thấp)"),
    ("076431", "phycomycetes", "noun", "/ˌfaɪkoʊmaɪˈsiːtiːz/", "nấm tảo (nhóm nấm bậc thấp)"),
    ("076432", "phycomycosis", "noun", "/ˌfaɪkoʊmaɪˈkoʊsɪs/", "bệnh nhiễm nấm mốc (y học)"),
    ("076433", "phyla", "noun", "/ˈfaɪlə/", "ngành (phân loại sinh học)"),
    ("076434", "phylactic", "adj", "/faɪˈlæktɪk/", "có tác dụng phòng bệnh, miễn dịch"),
    ("076435", "phylaxis", "noun", "/faɪˈlæksɪs/", "sự phòng vệ miễn dịch tự nhiên"),
    ("076436", "phyle", "noun", "/ˈfaɪliː/", "bộ lạc thị tộc (Hy Lạp cổ)"),
    ("076437", "phyletically", "adv", "/faɪˈlɛtɪkli/", "theo dòng tiến hóa chủng loại"),
    ("076438", "phyllidae", "noun", "/ˈfɪlɪdiː/", "họ Bọ lá (Phylliidae)"),
    ("076439", "phylliform", "adj", "/ˈfɪlɪfɔːrm/", "có hình dạng chiếc lá"),
    ("076440", "phyllitis", "noun", "/fɪˈlaɪtɪs/", "chi dương xỉ lưỡi hươu Phyllitis"),
    ("076441", "phyllium", "noun", "/ˈfɪliəm/", "chi bọ lá (Phyllium)"),
    ("076442", "phylloclad", "noun", "/ˈfɪləklæd/", "cành dạng lá (cành dẹt quang hợp)"),
    ("076443", "phyllocladaceae", "noun", "/ˌfɪləkləˈdeɪsiː/", "họ Thông lá dẹt Phyllocladaceae"),
    ("076444", "phylloclade", "noun", "/ˈfɪləkleɪd/", "cành dạng lá (cành dẹt quang hợp)"),
    ("076445", "phyllocladus", "noun", "/ˌfɪləˈkleɪdəs/", "chi thông cần tây (Phyllocladus)"),
    ("076446", "phyllode", "noun", "/ˈfɪloʊd/", "cuống lá biến dạng dẹt như lá"),
    ("076447", "phyllodial", "adj", "/fɪˈloʊdiəl/", "thuộc cuống lá dẹt (thực vật)"),
    ("076448", "phyllodoce", "noun", "/fɪˈlɒdəsi/", "chi đỗ quyên núi cao Phyllodoce"),
    ("076449", "phyllome", "noun", "/ˈfɪloʊm/", "cơ quan tương đồng lá (thực vật)"),
    ("076450", "phyllophagan", "noun", "/fɪˈlɒfəɡən/", "động vật ăn lá cây"),
    ("076451", "phyllophagous", "adj", "/fɪˈlɒfəɡəs/", "ăn lá cây (côn trùng, động vật)"),
    ("076452", "phyllophorus", "adj", "/fɪˈlɒfərəs/", "mang lá, có cơ quan dạng lá"),
    ("076453", "phyllopod", "adj", "/ˈfɪləpɒd/", "thuộc phân lớp Chân lá (giáp xác)"),
    ("076454", "phylloporus", "noun", "/fɪˈlɒpərəs/", "chi nấm lỗ lá (Phylloporus)"),
    ("076455", "phylloquinone", "noun", "/ˌfɪloʊˈkwɪnoʊn/", "vitamin K1 (phylloquinon)"),
    ("076456", "phyllorhynchus", "noun", "/ˌfɪləˈrɪŋkəs/", "chi rắn mũi lá (Phyllorhynchus)"),
    ("076457", "phylloscopus", "noun", "/fɪˈlɒskəpəs/", "chi chim chích lá (Phylloscopus)"),
    ("076458", "phyllostomatidae", "noun", "/ˌfɪləstoʊˈmætɪdiː/", "họ Dơi mũi lá Tân Thế giới"),
    ("076459", "phyllostome", "noun", "/ˈfɪləstoʊm/", "dơi mũi lá (Tân Thế giới)"),
    ("076460", "phyllostomidae", "noun", "/ˌfɪləˈstɒmɪdiː/", "họ Dơi mũi lá Tân Thế giới"),
    ("076461", "phyllostomus", "noun", "/fɪˈlɒstəməs/", "chi dơi mũi lá (Phyllostomus)"),
    ("076462", "phyllotaxis", "noun", "/ˌfɪləˈtæksɪs/", "cách sắp xếp lá trên cành"),
    ("076463", "phylloxeridae", "noun", "/ˌfɪlɒkˈsɛrɪdiː/", "họ Rệp hại nho (Phylloxeridae)"),
    ("076464", "phylobiology", "noun", "/ˌfaɪloʊbaɪˈɒlədʒi/", "sinh học hành vi chủng loài"),
    ("076465", "phylogenesis", "noun", "/ˌfaɪloʊˈdʒɛnɪsɪs/", "phát sinh chủng loại (tiến hóa)"),
    ("076466", "phylogenic", "adj", "/ˌfaɪloʊˈdʒɛnɪk/", "thuộc phát sinh chủng loại"),
    ("076467", "physalia", "noun", "/faɪˈseɪliə/", "sứa lửa chiến hạm (Physalia)"),
    ("076468", "physaria", "noun", "/faɪˈsɛriə/", "chi cây bàng quang quả Physaria"),
    ("076469", "physeteridae", "noun", "/ˌfaɪsɪˈtɛrɪdiː/", "họ Cá nhà táng (Physeteridae)"),
    ("076470", "physiatrics", "noun", "/ˌfɪziˈætrɪks/", "y học phục hồi, vật lý trị liệu"),
    ("076471", "physicalness", "noun", "/ˈfɪzɪkəlnəs/", "tính vật chất, tính hữu hình"),
    ("076472", "physicism", "noun", "/ˈfɪzɪsɪzəm/", "chủ nghĩa duy vật (triết học)"),
    ("076473", "physicists", "noun", "/ˈfɪzɪsɪsts/", "nhà vật lý học"),
    ("076474", "physicky", "adj", "/ˈfɪzɪki/", "ốm yếu xanh xao; có vị như thuốc"),
    ("076475", "physidae", "noun", "/ˈfɪsɪdiː/", "họ Ốc sên nước ngọt Physidae"),
    ("076476", "physiocrat", "noun", "/ˈfɪziəkræt/", "người theo trường phái trọng nông"),
    ("076477", "physiocrats", "noun", "/ˈfɪziəkræts/", "người theo trường phái trọng nông"),
    ("076478", "physiogeny", "noun", "/ˌfɪziˈɒdʒəni/", "sự phát sinh chức năng cơ thể"),
    ("076479", "physiognomic", "adj", "/ˌfɪziəɡˈnɒmɪk/", "thuộc nhân tướng học; nét mặt"),
    ("076480", "physiognomical", "adj", "/ˌfɪziəɡˈnɒmɪkəl/", "thuộc nhân tướng học; nét mặt"),
    ("076481", "physiognomically", "adv", "/ˌfɪziəɡˈnɒmɪkli/", "về mặt nhân tướng, diện mạo"),
    ("076482", "physiognomist", "noun", "/ˌfɪziˈɒɡnəmɪst/", "thầy xem tướng; nhà nhân tướng học"),
    ("076483", "physiographer", "noun", "/ˌfɪziˈɒɡrəfər/", "nhà địa lý tự nhiên (địa văn học)"),
    ("076484", "physiographic", "adj", "/ˌfɪziəˈɡræfɪk/", "thuộc địa lý tự nhiên (địa văn)"),
    ("076485", "physiographical", "adj", "/ˌfɪziəˈɡræfɪkəl/", "thuộc địa lý tự nhiên (địa văn)"),
    ("076486", "physiographically", "adv", "/ˌfɪziəˈɡræfɪkli/", "về mặt địa lý tự nhiên"),
    ("076487", "physiologies", "noun", "/ˌfɪziˈɒlədʒiz/", "sinh lý học; cơ chế sinh lý"),
    ("076488", "physiologise", "verb", "/ˌfɪziˈɒlədʒaɪz/", "nghiên cứu hoặc giảng giải sinh lý"),
    ("076489", "physiologised", "verb", "/ˌfɪziˈɒlədʒaɪzd/", "đã nghiên cứu, giải thích sinh lý"),
    ("076490", "physiologises", "verb", "/ˌfɪziˈɒlədʒaɪzɪz/", "nghiên cứu hoặc giảng giải sinh lý"),
    ("076491", "physiologising", "verb", "/ˌfɪziˈɒlədʒaɪzɪŋ/", "nghiên cứu hoặc giảng giải sinh lý"),
    ("076492", "physiotherapeutic", "adj", "/ˌfɪzioʊˌθɛrəˈpjuːtɪk/", "thuộc vật lý trị liệu"),
    ("076493", "physostegia", "noun", "/ˌfaɪzoʊˈstiːdʒə/", "chi hoa ngoan ngoãn Physostegia"),
    ("076494", "physostigma", "noun", "/ˌfaɪzoʊˈstɪɡmə/", "chi đậu độc Calabar Physostigma"),
    ("076495", "phytelephas", "noun", "/ˌfaɪtɪˈlɛfəs/", "chi cọ ngà voi (Phytelephas)"),
    ("076496", "phytochemist", "noun", "/ˌfaɪtoʊˈkɛmɪst/", "nhà hóa sinh thực vật"),
    ("076497", "phytocoenoses", "noun", "/ˌfaɪtoʊsɪˈnoʊsiːz/", "quần xã thực vật (sinh thái học)"),
    ("076498", "phytocoenosis", "noun", "/ˌfaɪtoʊsɪˈnoʊsɪs/", "quần xã thực vật (sinh thái học)"),
    ("076499", "phytogenesis", "noun", "/ˌfaɪtoʊˈdʒɛnɪsɪs/", "sự phát sinh thực vật"),
    ("076500", "phytogenetic", "adj", "/ˌfaɪtoʊdʒəˈnɛtɪk/", "thuộc sự phát sinh thực vật"),
    ("076501", "phytogenetically", "adv", "/ˌfaɪtoʊdʒəˈnɛtɪkli/", "theo lịch sử phát sinh thực vật"),
    ("076502", "phytogeny", "noun", "/faɪˈtɒdʒəni/", "sự phát sinh và tiến hóa thực vật"),
]

with open("scratch/b36_r03_raw_p5.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r03_p5.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r03_p5 saved OK")
