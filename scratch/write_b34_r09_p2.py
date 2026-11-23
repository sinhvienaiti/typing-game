import json

items = [
    ("069103", "trickers", "noun", "/ˈtrɪkərz/", "kẻ lừa gạt hay chơi khăm người khác"),
    ("069104", "trophoblasts", "noun", "/ˈtrɒfəˌblæsts/", "lá nuôi phôi bám làm tổ tử cung"),
    ("069105", "typhas", "noun", "/ˈtaɪfəz/", "cây hương bồ nến nước chi Typha"),
    ("069106", "underframes", "noun", "/ˈʌndərˌfreɪmz/", "khung sườn gầm đỡ dưới toa xe"),
    ("069107", "vanquishers", "noun", "/ˈvæŋkwɪʃərz/", "người chiến thắng chinh phục kẻ thù"),
    ("069108", "xanthomonases", "noun", "/ˌzænθəˈmoʊnəsɪz/", "vi khuẩn gây bệnh đốm lá cây"),
    ("069109", "zidovudines", "noun", "/zɪˈdɒvjʊˌdiːnz/", "thuốc kháng vi rút HIV zidovudin"),
    ("069110", "aalsts", "noun", "/ɑːlsts/", "thành phố Aalst ở nước Bỉ"),
    ("069111", "acromia", "noun", "/əˈkroʊmiə/", "mỏm cùng vai ở đầu xương bả vai"),
    ("069112", "acromions", "noun", "/əˈkroʊmiɒnz/", "mỏm xương cùng vai nối xương đòn"),
    ("069113", "actualisations", "noun", "/ˌæktʃuəlaɪˈzeɪʃənz/", "sự hiện thực hóa biến thành thực tế"),
    ("069114", "alkynes", "noun", "/ˈælkaɪnz/", "hyđrocacbon không no nối ba ankin"),
    ("069115", "ampules", "noun", "/ˈæmpjuːlz/", "ống thủy tinh hàn kín đựng thuốc"),
    ("069116", "anglerfishes", "noun", "/ˈæŋɡlərˌfɪʃɪz/", "cá cần câu biển sâu có mồi sáng"),
    ("069117", "anverses", "noun", "/ɒnˈvɛərz/", "thành phố cảng Antwerp của Bỉ"),
    ("069118", "appetisers", "noun", "/ˈæpɪˌtaɪzərz/", "món ăn nhẹ khai vị đầu bữa"),
    ("069119", "archimandrites", "noun", "/ˌɑːrkɪˈmændraɪts/", "bề trên tu viện Chính Thống giáo"),
    ("069120", "armlets", "noun", "/ˈɑːrmlɪts/", "vòng đeo trang trí bắp tay trên"),
    ("069121", "assurednesses", "noun", "/əˈʃʊərɪdnəsɪz/", "sự tự tin chắc chắn vững vàng"),
    ("069122", "auchinclosses", "noun", "/ˈɔːkɪnˌklɒsɪz/", "nhà văn Mỹ Louis Auchincloss"),
    ("069123", "barbus", "noun", "/ˈbɑːrbəs/", "cá đòng đong; cá chép suối Barbus"),
    ("069124", "barleycorns", "noun", "/ˈbɑːrliˌkɔːrnz/", "hạt lúa mạch; đơn vị đo cổ một phần"),
    ("069125", "bedazzled", "verb", "/bɪˈdæzəld/", "đã làm lóa mắt mê hoặc choáng ngợp"),
    ("069126", "bedazzles", "verb", "/bɪˈdæzəlz/", "làm lóa mắt mê hoặc ngây ngất"),
    ("069127", "bedazzling", "verb", "/bɪˈdæzəlɪŋ/", "đang làm chói lòa mê hoặc lòng"),
    ("069128", "bilabials", "noun", "/baɪˈleɪbiəlz/", "âm đôi môi phát bằng hai môi"),
    ("069129", "bombyxes", "noun", "/ˈbɒmbɪksɪz/", "chi ngài tằm nhả tơ Bombyx"),
    ("069130", "borsches", "noun", "/ˈbɔːrʃɪz/", "súp củ dền đỏ truyền thống Đông Âu"),
    ("069131", "calans", "noun", "/ˈkeɪlənz/", "thuốc tim mạch hạ áp Calan"),
    ("069132", "cannisters", "noun", "/ˈkænɪstərz/", "hộp thiếc nắp kín đựng trà cà phê"),
    ("069133", "carettas", "noun", "/kəˈrɛtəz/", "rùa biển quản đồng chi Caretta"),
    ("069134", "carfuls", "noun", "/ˈkɑːrˌfʊlz/", "lượng người hoặc đồ chở đầy một xe"),
    ("069135", "catholicoses", "noun", "/kəˈθɒlɪkoʊsɪz/", "giáo chủ thượng phụ Giáo hội Đông"),
    ("069136", "centerboards", "noun", "/ˈsɛntərˌbɔːrdz/", "ván giữ thăng bằng dưới đáy thuyền"),
    ("069137", "cepheuses", "noun", "/ˈsiːfiəsɪz/", "vua Cepheus; chòm sao Tiên Vương"),
    ("069138", "chimborazos", "noun", "/ˌtʃɪmbəˈrɑːzoʊz/", "núi lửa cao Chimborazo Ecuador"),
    ("069139", "cisternae", "noun", "/sɪˈstɜːrniː/", "túi màng dẹt Golgi; bể chứa dịch"),
    ("069140", "cisternas", "noun", "/sɪˈstɜːrnəz/", "khoang bể chứa dịch trong giải"),
    ("069141", "coiners", "noun", "/ˈkɔɪnərz/", "người sáng tạo từ mới; thợ đúc tiền"),
    ("069142", "concretions", "noun", "/kənˈkriːʃənz/", "kết hạch đá; sỏi kết tụ trong tạng"),
    ("069143", "contos", "noun", "/ˈkɒntoʊz/", "đơn vị tiền cổ Bồ Đào Nha conto"),
    ("069144", "corrigendums", "noun", "/ˌkɒrɪˈdʒɛndəmz/", "bảng đính chính lỗi in trong sách"),
    ("069145", "crocodilians", "noun", "/ˌkrɒkəˈdɪliənz/", "loài bò sát lớn thuộc bộ Cá sấu"),
    ("069146", "deictics", "noun", "/ˈdaɪktɪks/", "từ chỉ xuất phụ thuộc ngữ cảnh"),
    ("069147", "dormitions", "noun", "/dɔːrˈmɪʃənz/", "lễ Đức Mẹ yên giấc về trời"),
    ("069148", "dysphonias", "noun", "/dɪsˈfoʊniəz/", "chứng rối loạn phát âm khàn tiếng"),
    ("069149", "evaporites", "noun", "/ɪˈvæpəˌraɪts/", "đá trầm tích muối khoáng bay hơi"),
    ("069150", "fornices", "noun", "/ˈfɔːrnɪsiːz/", "vòm não bộ; vòm túi giải phẫu"),
    ("069151", "fornixes", "noun", "/ˈfɔːrnɪksɪz/", "vòm uốn cong giải phẫu (thần kinh)"),
    ("069152", "fulmars", "noun", "/ˈfʊlmərz/", "chim hải âu lớn fulmar biển lạnh"),
    ("069153", "gamier", "adj", "/ˈɡeɪmiər/", "nặng mùi thú rừng hơn; táo bạo hơn"),
    ("069154", "gamiest", "adj", "/ˈɡeɪmiɪst/", "nặng mùi thú rừng nhất; táo bạo"),
    ("069155", "garfishes", "noun", "/ˈɡɑːrˌfɪʃɪz/", "cá nhái biển; cá sấu mõm dài"),
    ("069156", "glomeruli", "noun", "/ɡloʊˈmɛrjəˌlaɪ/", "cầu thận búi mao mạch lọc máu"),
    ("069157", "glyceryls", "noun", "/ˈɡlɪsərɪlz/", "gốc hóa học glixerol trong chất béo"),
    ("069158", "gougers", "noun", "/ˈɡaʊdʒərz/", "đục máng; kẻ chặt chém giá quá cao"),
    ("069159", "greatcoats", "noun", "/ˈɡreɪtˌkoʊts/", "áo khoác dạ quân đội dài dày dặn"),
    ("069160", "hallooing", "verb", "/həˈluːɪŋ/", "đang hô vang reo hò thúc chó săn"),
    ("069161", "halloos", "noun", "/həˈluːz/", "tiếng la hô vang gọi lớn ngoài đồng"),
    ("069162", "handgrips", "noun", "/ˈhændˌɡrɪps/", "tay cầm chống trượt trên dụng cụ"),
    ("069163", "harijans", "noun", "/ˈhʌrɪdʒənz/", "tầng lớp Dalit tiện dân Ấn Độ (cũ)"),
    ("069164", "havasupais", "noun", "/ˌhɑːvəˈsuːpaɪz/", "bộ tộc bản địa Havasupai Grand"),
    ("069165", "hemoptyses", "noun", "/hɪˈmɒptɪsiːz/", "triệu chứng ho khạc ra máu"),
    ("069166", "hemothoraxes", "noun", "/ˌhiːmoʊˈθɔːræksɪz/", "tràn máu khoang màng phổi"),
    ("069167", "hummocks", "noun", "/ˈhʌməks/", "gò đất nhấp nhô hoặc đồi băng nhỏ"),
    ("069168", "ideologists", "noun", "/ˌaɪdiˈɒlədʒɪsts/", "nhà tư tưởng xây dựng hệ ý thức"),
    ("069169", "ijtihads", "noun", "/ˌɪdʒtɪˈhɑːdz/", "phép suy luận luật học Hồi giáo"),
    ("069170", "interlanguages", "noun", "/ˌɪntərˈlæŋɡwɪdʒɪz/", "ngôn ngữ trung gian người học ngoại"),
    ("069171", "invigilators", "noun", "/ɪnˈvɪdʒɪˌleɪtərz/", "giám thị coi thi nghiêm ngặt (Anh)"),
    ("069172", "kanamycins", "noun", "/ˌkænəˈmaɪsɪnz/", "thuốc kháng sinh nhóm kanamycin"),
    ("069173", "khanties", "noun", "/ˈkɑːntiz/", "người bản địa Khanty vùng Siberia"),
    ("069174", "knapped", "verb", "/næpt/", "đã ghè đẽo đá lửa thành lưỡi sắc"),
    ("069175", "knapping", "verb", "/ˈnæpɪŋ/", "đang ghè đẽo đá lửa chế tác công"),
    ("069176", "knaps", "verb", "/næps/", "ghè đẽo đập tách mảnh đá lửa"),
    ("069177", "krakataus", "noun", "/ˌkrækəˈtaʊz/", "núi lửa Krakatoa ở Indonesia"),
    ("069178", "kuruses", "noun", "/ˈkʊrʊʃɪz/", "tiền xu kurus của Thổ Nhĩ Kỳ"),
    ("069179", "larreas", "noun", "/ˈlɑːriəz/", "cây bụi nhựa sa mạc chi Larrea"),
    ("069180", "lithopses", "noun", "/ˈlɪθɒpsɪz/", "cây mọng nước đá sống Lithops"),
    ("069181", "longans", "noun", "/ˈlɒŋɡənz/", "cây nhãn và quả nhãn ngọt mọng nước"),
    ("069182", "lucanias", "noun", "/luːˈkeɪniəz/", "vùng lịch sử Lucania miền nam Ý"),
    ("069183", "malebranches", "noun", "/ˌmɑːlˈbrɒ̃ʃɪz/", "triết gia Nicolas de Malebranche"),
    ("069184", "masseters", "noun", "/məˈsiːtərz/", "cơ cắn khỏe nâng hàm dưới khi nhai"),
    ("069185", "matchlocks", "noun", "/ˈmætʃˌlɒks/", "súng hỏa mai châm ngòi dây cổ đại"),
    ("069186", "mechanists", "noun", "/ˈmɛkənɪsts/", "nhà triết học theo thuyết cơ giới"),
    ("069187", "medroxyprogesterones", "noun", "/məˌdrɒksiproʊˈdʒɛstəroʊnz/", "hoóc-môn tổng hợp progestin"),
    ("069188", "memorializations", "noun", "/məˌmɔːriəlaɪˈzeɪʃənz/", "sự tưởng niệm xây đài ghi công"),
    ("069189", "millponds", "noun", "/ˈmɪlˌpɒndz/", "ao chứa nước dẫn dòng quay cối xay"),
    ("069190", "moppets", "noun", "/ˈmɒpɪts/", "em bé nhỏ dễ thương (thân mật)"),
    ("069191", "myms", "noun", "/ˈmaɪəm/", "đơn vị chiều dài 10 km (vạn mét)"),
    ("069192", "navvies", "noun", "/ˈnæviz/", "công nhân đào đường kênh (Anh)"),
    ("069193", "ngunis", "noun", "/əŋˈɡuːniz/", "nhóm dân tộc ngôn ngữ Nguni Nam Phi"),
    ("069194", "nuthouses", "noun", "/ˈnʌtˌhaʊzɪz/", "bệnh viện tâm thần (từ lóng cũ)"),
    ("069195", "odalisques", "noun", "/ˈoʊdəˌlɪsks/", "nữ tỳ hậu cung triều Ottoman xưa"),
    ("069196", "oilcloths", "noun", "/ˈɔɪlˌklɒθs/", "vải dầu không thấm nước trải bàn"),
    ("069197", "osmanthuses", "noun", "/ɒzˈmænθəsɪz/", "cây hoa mộc hương chi Osmanthus"),
    ("069198", "paintboxes", "noun", "/ˈpeɪntˌbɒksɪz/", "hộp đựng màu vẽ và cọ của họa sĩ"),
    ("069199", "paleobiologies", "noun", "/ˌpeɪlioʊbaɪˈɒlədʒiz/", "ngành cổ sinh vật học lịch sử"),
    ("069200", "papios", "noun", "/ˈpeɪpioʊz/", "khỉ đầu chó châu Phi chi Papio"),
    ("069201", "paspalums", "noun", "/ˈpæspələmz/", "cỏ san hô làm bãi cỏ chi Paspalum"),
    ("069202", "petabytes", "noun", "/ˈpɛtəˌbaɪts/", "đơn vị dữ liệu một triệu gigabyte"),
]

with open("scratch/b34_r09_raw_p2.json") as f:
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

with open("scratch/b34_r09_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r09_p2.json OK")
