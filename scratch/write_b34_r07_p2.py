import json

items = [
    ("068103", "blacklegs", "noun", "/ˈblækˌlɛɡz/", "kẻ phá đám đình công; kẻ lừa đảo"),
    ("068104", "bookclubs", "noun", "/ˈbʊkˌklʌbz/", "câu lạc bộ đọc sách theo kỳ"),
    ("068105", "brumaires", "noun", "/bruːˈmɛərz/", "tháng Sương mù lịch Cộng hòa Pháp"),
    ("068106", "canapes", "noun", "/ˈkænəpeɪz/", "bánh quy khai vị phết nhân mặn"),
    ("068107", "carides", "noun", "/ˈkærɪdiːz/", "cột tượng nữ chống mái (biến thể)"),
    ("068108", "caryatids", "noun", "/ˌkæriˈætɪdz/", "cột trụ tạc hình thiếu nữ chống mái"),
    ("068109", "centrexes", "noun", "/ˈsɛntrɛksɪz/", "dịch vụ tổng đài nội bộ trung tâm"),
    ("068110", "chicots", "noun", "/ˈtʃɪkəts/", "cây cà phê Kentucky; gốc cây khô"),
    ("068111", "clavered", "verb", "/ˈkleɪvərd/", "đã tán gẫu buôn chuyện (Scotland)"),
    ("068112", "clavering", "verb", "/ˈkleɪvərɪŋ/", "đang tán gẫu phiếm chuyện"),
    ("068113", "clavers", "verb", "/ˈkleɪvərz/", "tán gẫu buôn chuyện phiếm"),
    ("068114", "clomipramines", "noun", "/kloʊˈmɪprəˌmiːnz/", "thuốc chống trầm cảm clomipramin"),
    ("068115", "clubrooms", "noun", "/ˈklʌbˌruːmz/", "phòng sinh hoạt chung câu lạc bộ"),
    ("068116", "collagenases", "noun", "/kəˈlædʒəˌneɪsɪz/", "enzym phân hủy sợi collagen mô"),
    ("068117", "countercurrents", "noun", "/ˈkaʊntərˌkɜːrənts/", "dòng hải lưu hoặc xu hướng ngược"),
    ("068118", "cowbirds", "noun", "/ˈkaʊˌbɜːrdz/", "chim sáo bò đẻ nhờ tổ chim khác"),
    ("068119", "cowslips", "noun", "/ˈkaʊˌslɪps/", "hoa báo xuân vàng dại đồng cỏ"),
    ("068120", "cufflinks", "noun", "/ˈkʌfˌlɪŋks/", "khuy cài măng sét cổ tay áo sơ mi"),
    ("068121", "deciduae", "noun", "/dɪˈsɪdʒuːiː/", "lớp màng rụng niêm mạc tử cung"),
    ("068122", "deciduas", "noun", "/dɪˈsɪdʒuːəz/", "màng rụng bong ra sau khi sinh nở"),
    ("068123", "defrosters", "noun", "/dɪˈfrɒstərz/", "thiết bị sưởi rã đông kính xe tủ"),
    ("068124", "devilries", "noun", "/ˈdɛvəlriz/", "trò ma quái hiểm ác; ma thuật đen"),
    ("068125", "disorganisations", "noun", "/dɪsˌɔːrɡənaɪˈzeɪʃənz/", "tình trạng hỗn loạn thiếu tổ chức"),
    ("068126", "droseras", "noun", "/ˈdrɒsərəz/", "cây gọng vó ăn thịt chi Drosera"),
    ("068127", "drupes", "noun", "/druːps/", "quả hạch một hạt cứng như đào mận"),
    ("068128", "duckbills", "noun", "/ˈdʌkˌbɪlz/", "thú mỏ vịt; cá tầm thìa Bắc Mỹ"),
    ("068129", "ebonites", "noun", "/ˈɛbəˌnaɪts/", "cao su lưu hóa cứng đen ebonit"),
    ("068130", "endogamies", "noun", "/ɛnˈdɒɡəmiz/", "tục kết hôn nội tộc trong nhóm"),
    ("068131", "epilators", "noun", "/ˈɛpɪˌleɪtərz/", "máy nhổ lông bằng điện tử"),
    ("068132", "eschatons", "noun", "/ˈɛskəˌtɒnz/", "thời khắc tận thế chung cuộc"),
    ("068133", "finitudes", "noun", "/ˈfɪnɪˌtjuːdz/", "tính chất hữu hạn có giới hạn"),
    ("068134", "floatplanes", "noun", "/ˈfloʊtˌpleɪnz/", "thủy phi cơ lắp phao hạ cánh nước"),
    ("068135", "footplates", "noun", "/ˈfʊtˌpleɪts/", "sàn đứng lái đầu máy xe lửa"),
    ("068136", "fringillas", "noun", "/frɪnˈdʒɪləz/", "chim sẻ đồng thuộc chi Fringilla"),
    ("068137", "gamows", "noun", "/ˈɡæmɒvz/", "nhà vật lý vũ trụ George Gamow"),
    ("068138", "gatecrashers", "noun", "/ˈɡeɪtˌkræʃərz/", "kẻ đột nhập tiệc không có giấy mời"),
    ("068139", "gerontologists", "noun", "/ˌdʒɛrənˈtɒlədʒɪsts/", "nhà nghiên cứu lão khoa tuổi già"),
    ("068140", "gofers", "noun", "/ˈɡoʊfərz/", "người chạy việc vặt sai vặt (lóng)"),
    ("068141", "greenrooms", "noun", "/ˈɡriːnˌruːmz/", "phòng chờ hậu trường của nghệ sĩ"),
    ("068142", "halothanes", "noun", "/ˈhæləˌθeɪnz/", "thuốc gây mê bay hơi halothan"),
    ("068143", "harakiris", "noun", "/ˌhærəˈkɪriz/", "nghi thức tự mổ bụng Nhật Bản"),
    ("068144", "harridans", "noun", "/ˈhærɪdənz/", "mụ già hung dữ hay la mắng chửi bới"),
    ("068145", "hindlimbs", "noun", "/ˈhaɪndˌlɪmz/", "chi sau của động vật bốn chân"),
    ("068146", "homoeroticisms", "noun", "/ˌhoʊmoʊɪˈrɒtɪsɪzəmz/", "xu hướng gợi dục đồng giới"),
    ("068147", "introits", "noun", "/ˈɪntrɔɪts/", "bài thánh ca nhập lễ mở đầu lễ"),
    ("068148", "ipomoeas", "noun", "/ˌaɪpəˈmiːəz/", "cây rau muống; bìm bìm chi Ipomoea"),
    ("068149", "irredentists", "noun", "/ˌɪrɪˈdɛntɪsts/", "người đòi thu hồi lãnh thổ lịch sử"),
    ("068150", "irreversibilities", "noun", "/ˌɪrɪˌvɜːrsəˈbɪlɪtiz/", "tính bất khả nghịch không thể quay"),
    ("068151", "ivries", "noun", "/iːvˈriz/", "trận đánh Ivry-la-Bataille Pháp"),
    ("068152", "jotuns", "noun", "/ˈjɒtənz/", "người khổng lồ Jotunn Bắc Âu"),
    ("068153", "juncuses", "noun", "/ˈdʒʌŋkəsɪz/", "cây cói bấc làm tim đèn chi Juncus"),
    ("068154", "khalifahs", "noun", "/kəˈliːfəz/", "vua hồi giáo tối cao khalip"),
    ("068155", "lamarckians", "noun", "/ləˈmɑːrkiənz/", "người theo thuyết tiến hóa Lamarck"),
    ("068156", "layabouts", "noun", "/ˈleɪəˌbaʊts/", "kẻ lười biếng ăn không ngồi rồi"),
    ("068157", "limbi", "noun", "/ˈlɪmbaɪ/", "vùng rìa mép giải phẫu; quầng Limbo"),
    ("068158", "limburgers", "noun", "/ˈlɪmbɜːrɡərz/", "phô mai mềm mùi nồng Limburger"),
    ("068159", "limbuses", "noun", "/ˈlɪmbəsɪz/", "đường viền mép giác mạc hoặc mô"),
    ("068160", "liposomes", "noun", "/ˈlɪpəˌsoʊmz/", "túi vi cầu lipid dẫn thuốc y học"),
    ("068161", "lordosises", "noun", "/lɔːrˈdoʊsɪsɪz/", "chứng ưỡn cong cột sống thắt lưng"),
    ("068162", "madronas", "noun", "/məˈdroʊnəz/", "cây gỗ thường xanh vỏ đỏ madrone"),
    ("068163", "masculinizations", "noun", "/ˌmæskjʊlɪnaɪˈzeɪʃənz/", "sự nam tính hóa đặc điểm sinh lý"),
    ("068164", "mcguffeys", "noun", "/məˈɡʌfiz/", "nhà giáo dục Mỹ W. McGuffey"),
    ("068165", "meerschaums", "noun", "/ˈmɪərˌʃɔːmz/", "khoáng đá bọt biển làm tẩu thuốc"),
    ("068166", "menottis", "noun", "/məˈnɒtiz/", "nhà soạn nhạc kịch Ý Menotti"),
    ("068167", "mensheviks", "noun", "/ˈmɛnʃəˌvɪks/", "phe thiểu số Menshevik Nga 1903"),
    ("068168", "mkos", "noun", "/ˌɛm keɪ ˈoʊz/", "tổ chức Mujahedin-e Khalq Iran"),
    ("068169", "nephrons", "noun", "/ˈnɛfrɒnz/", "đơn vị lọc máu cơ bản của thận"),
    ("068170", "neutralisations", "noun", "/ˌnjuːtrəlaɪˈzeɪʃənz/", "quá trình trung hòa hóa học vô hiệu"),
    ("068171", "ngbs", "noun", "/ˌɛn dʒiː ˈbiːz/", "Cục Vệ binh Quốc gia Mỹ NGB"),
    ("068172", "nilotics", "noun", "/naɪˈlɒtɪks/", "nhóm ngôn ngữ sông Nile Đông Phi"),
    ("068173", "numidians", "noun", "/njuːˈmɪdiənz/", "cư dân vương quốc Numidia cổ đại"),
    ("068174", "ohioans", "noun", "/oʊˈhaɪoʊənz/", "người dân bang Ohio của Mỹ"),
    ("068175", "otolaryngologists", "noun", "/ˌoʊtoʊˌlærɪŋˈɡɒlədʒɪsts/", "bác sĩ chuyên khoa tai mũi họng"),
    ("068176", "oxalises", "noun", "/ˈɒksəlɪsɪz/", "cây chua me đất thuộc chi Oxalis"),
    ("068177", "papavers", "noun", "/pəˈpeɪvərz/", "cây anh túc thuốc phiện chi Papaver"),
    ("068178", "patrollers", "noun", "/pəˈtroʊlərz/", "người đi tuần tra bảo vệ an ninh"),
    ("068179", "pentoses", "noun", "/ˈpɛnˌtoʊsɪz/", "đường đơn năm cacbon pentoza"),
    ("068180", "phragmiteses", "noun", "/fræɡˈmaɪtiːzɪz/", "cây lau sậy mọc ven đầm lầy"),
    ("068181", "phyllos", "noun", "/ˈfaɪloʊz/", "lá bột cán siêu mỏng làm bánh Âu"),
    ("068182", "pilothouses", "noun", "/ˈpaɪlətˌhaʊzɪz/", "buồng lái điều khiển trên boong tàu"),
    ("068183", "polychaetes", "noun", "/ˈpɒlɪˌkiːts/", "giun đốt biển có nhiều tơ"),
    ("068184", "prancers", "noun", "/ˈprɑːnsərz/", "ngựa nhảy chồm; tuần lộc Prancer"),
    ("068185", "prosthodonticses", "noun", "/ˌprɒsθəˈdɒntɪksɪz/", "chuyên khoa phục hình răng giả"),
    ("068186", "protegees", "noun", "/ˌproʊtɪˈʒeɪz/", "nữ học trò được người lớn bảo trợ"),
    ("068187", "pustules", "noun", "/ˈpʌstjuːlz/", "mụn mủ nhỏ nổi trên bề mặt da"),
    ("068188", "quats", "noun", "/kwɒts/", "hợp chất amoni bậc bốn khử khuẩn"),
    ("068189", "quattrocentos", "noun", "/ˌkwɑːtroʊˈtʃɛntoʊz/", "thời kỳ nghệ thuật Ý thế kỷ 15"),
    ("068190", "queenlier", "adj", "/ˈkwiːnliər/", "uy nghi lộng lẫy như nữ hoàng hơn"),
    ("068191", "queenliest", "adj", "/ˈkwiːnliɪst/", "uy nghi lộng lẫy như nữ hoàng nhất"),
    ("068192", "refloated", "verb", "/riːˈfloʊtɪd/", "đã cứu hộ nổi lại tàu mắc cạn"),
    ("068193", "refloating", "verb", "/riːˈfloʊtɪŋ/", "đang kéo nổi tàu bị mắc cạn"),
    ("068194", "refloats", "verb", "/riːˈfloʊts/", "làm nổi lại tàu đắm; tái thả nổi"),
    ("068195", "rehears", "verb", "/riːˈhɪərz/", "xét xử phúc thẩm lại; nghe lại vụ"),
    ("068196", "riyals", "noun", "/riˈjɑːlz/", "đơn vị tiền tệ riyal Trung Đông"),
    ("068197", "rosaceaes", "noun", "/roʊˈzeɪʃiz/", "họ Hoa hồng gồm táo lê đào mận"),
    ("068198", "sangomas", "noun", "/sɑːŋˈɡoʊməz/", "thầy lang trị bệnh tâm linh Zulu"),
    ("068199", "sardas", "noun", "/ˈsɑːrdəz/", "cá ngừ sọc Atlantic thuộc chi Sarda"),
    ("068200", "schoolchildren", "noun", "/ˈskuːlˌtʃɪldrən/", "học sinh lứa tuổi đi học phổ thông"),
    ("068201", "scillas", "noun", "/ˈsɪləz/", "cây lan chuông xanh chi Scilla"),
    ("068202", "sesamoids", "noun", "/ˈsɛsəˌmɔɪdz/", "xương vừng nhỏ nằm trong gân khớp"),
]

with open("scratch/b34_r07_raw_p2.json") as f:
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

with open("scratch/b34_r07_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r07_p2.json OK")
