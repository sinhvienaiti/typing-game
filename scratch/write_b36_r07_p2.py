import json

rows = [
    ("078103", "porcelainous", "adj", "/ˌpɔːrsəˈleɪnəs/", "bằng sứ; bóng láng như sứ"),
    ("078104", "porcelains", "noun", "/ˈpɔːrsəlɪnz/", "đồ gốm sứ; sứ cao cấp"),
    ("078105", "porcelaneous", "adj", "/ˌpɔːrsəˈleɪniəs/", "bằng sứ; bóng láng như sứ"),
    ("078106", "porcellaneous", "adj", "/ˌpɔːrsəˈleɪniəs/", "bằng sứ; bóng láng như sứ"),
    ("078107", "porcellanic", "adj", "/ˌpɔːrsəˈlænɪk/", "giống chất sứ; bằng sứ"),
    ("078108", "porcellanous", "adj", "/ˌpɔːrsəˈleɪnəs/", "bằng sứ; bóng láng như sứ"),
    ("078109", "porcellio", "noun", "/pɔːrˈsɛlioʊ/", "chi bọ gỗ ẩm (Porcellio)"),
    ("078110", "porcellionidae", "noun", "/pɔːrˌsɛliˈɒnɪdiː/", "họ Bọ gỗ ẩm (Porcellionidae)"),
    ("078111", "porcupinefish", "noun", "/ˈpɔːrkjʊpaɪnˌfɪʃ/", "cá nóc nhím (Diodon)"),
    ("078112", "porcupinish", "adj", "/ˈpɔːrkjʊpaɪnɪʃ/", "xù gai như nhím; hay cáu kỉnh"),
    ("078113", "pored", "verb", "/pɔːrd/", "đã đọc chăm chú, nghiền ngẫm"),
    ("078114", "pores", "verb", "/pɔːrz/", "đọc chăm chú, nghiền ngẫm"),
    ("078115", "porge", "verb", "/pɔːrdʒ/", "lọc sạch gân máu thịt (lễ Do Thái)"),
    ("078116", "poriferan", "noun", "/pəˈrɪfərən/", "động vật thân lỗ; bọt biển"),
    ("078117", "poriferous", "adj", "/pəˈrɪfərəs/", "có nhiều lỗ xốp nhỏ"),
    ("078118", "poring", "verb", "/ˈpɔːrɪŋ/", "đọc chăm chú, nghiền ngẫm"),
    ("078119", "porkfish", "noun", "/ˈpɔːrkfɪʃ/", "cá vây sọc vàng porkfish"),
    ("078120", "porkholt", "noun", "/ˈpɔːrkhoʊlt/", "thịt lợn hoặc thịt cừu hầm (từ cổ)"),
    ("078121", "porkling", "noun", "/ˈpɔːrklɪŋ/", "lợn con, lợn sữa"),
    ("078122", "porks", "noun", "/pɔːrks/", "thịt lợn; bổng lộc chính trị"),
    ("078123", "porky", "adj", "/ˈpɔːrki/", "mập mạp; giống thịt lợn; bốc phét"),
    ("078124", "pornographers", "noun", "/pɔːrˈnɑːɡrəfərz/", "người sản xuất nội dung khiêu dâm"),
    ("078125", "pornographically", "adv", "/ˌpɔːrnəˈɡræfɪkli/", "theo kiểu khiêu dâm, dâm ô"),
    ("078126", "poronotus", "noun", "/ˌpɔːrəˈnoʊtəs/", "chi cá chim bơ (Poronotus)"),
    ("078127", "poroplastic", "adj", "/ˌpɔːrəˈplæstɪk/", "xốp và dẻo (nỉ dùng bó bột)"),
    ("078128", "poroporo", "noun", "/ˌpɔːroʊˈpɔːroʊ/", "cây cà dại poroporo (New Zealand)"),
    ("078129", "porose", "adj", "/ˈpɔːroʊs/", "có lỗ nhỏ li ti, rỗ xốp"),
    ("078130", "porously", "adv", "/ˈpɔːrəsli/", "theo kiểu rỗ xốp, thấm qua"),
    ("078131", "porphyrio", "noun", "/pɔːrˈfɪrioʊ/", "chi chim sâm cầm tím (Porphyrio)"),
    ("078132", "porphyrula", "noun", "/pɔːrˈfɪrjʊlə/", "chi gà nước tía Mỹ (Porphyrula)"),
    ("078133", "porpoised", "verb", "/ˈpɔːrpəst/", "đã nhảy nhấp nhô mặt nước (tàu, cá)"),
    ("078134", "porpoises", "verb", "/ˈpɔːrpəsɪz/", "nhảy nhấp nhô trên mặt nước"),
    ("078135", "porpoising", "verb", "/ˈpɔːrpəsɪŋ/", "nhảy nhấp nhô trên mặt nước"),
    ("078136", "porraceous", "adj", "/pɒˈreɪʃəs/", "có màu xanh lá tỏi tây (y học)"),
    ("078137", "porriginous", "adj", "/pəˈrɪdʒɪnəs/", "bị bệnh chốc lở da đầu (y học)"),
    ("078138", "porrigo", "noun", "/pəˈraɪɡoʊ/", "bệnh chốc lở da đầu (y học cổ)"),
    ("078139", "portableness", "noun", "/ˈpɔːrtəbəlnəs/", "tính dễ mang theo, gọn nhẹ"),
    ("078140", "portably", "adv", "/ˈpɔːrtəbli/", "một cách gọn nhẹ dễ mang theo"),
    ("078141", "portaged", "verb", "/ˈpɔːrtɪdʒd/", "đã khiêng vác thuyền qua quãng cạn"),
    ("078142", "portages", "verb", "/ˈpɔːrtɪdʒɪz/", "khiêng vác thuyền qua quãng cạn"),
    ("078143", "portaging", "verb", "/ˈpɔːrtɪdʒɪŋ/", "khiêng vác thuyền qua quãng cạn"),
    ("078144", "portakabin", "noun", "/ˈpɔːrtəˌkæbɪn/", "nhà lắp ghép di động (Portakabin)"),
    ("078145", "portamento", "noun", "/ˌpɔːrtəˈmɛntoʊ/", "kỹ thuật trượt luyến âm (âm nhạc)"),
    ("078146", "portative", "adj", "/ˈpɔːrtətɪv/", "có thể xách tay mang đi (đàn organ)"),
    ("078147", "portcrayon", "noun", "/pɔːrtˈkreɪɒn/", "cán kẹp chì vẽ (hội họa)"),
    ("078148", "ported", "verb", "/ˈpɔːrtɪd/", "đã chuyển mã phần mềm; vác súng"),
    ("078149", "portelas", "noun", "/pɔːrˈtɛləz/", "địa danh Portela; tên họ Portela"),
    ("078150", "portentousness", "noun", "/pɔːrˈtɛntəsnəs/", "vẻ báo điềm dữ; tính khoa trương"),
    ("078151", "porters", "noun", "/ˈpɔːrtərz/", "nhân viên khuân vác; người gác cổng"),
    ("078152", "portfire", "noun", "/ˈpɔːrtfaɪər/", "ống ngòi châm thuốc súng pháo (cổ)"),
    ("078153", "porticoed", "adj", "/ˈpɔːrtɪkoʊd/", "có hàng hiên cột trước cửa"),
    ("078154", "porting", "verb", "/ˈpɔːrtɪŋ/", "chuyển mã phần mềm; bế súng"),
    ("078155", "portionable", "adj", "/ˈpɔːrʃənəbəl/", "có thể chia phần được"),
    ("078156", "portioned", "verb", "/ˈpɔːrʃənd/", "đã chia thành từng phần, phân chia"),
    ("078157", "portioner", "noun", "/ˈpɔːrʃənər/", "người chia phần ăn, chia khẩu phần"),
    ("078158", "portioning", "verb", "/ˈpɔːrʃənɪŋ/", "chia thành từng phần, phân chia"),
    ("078159", "portionless", "adj", "/ˈpɔːrʃənləs/", "không có phần; không của hồi môn"),
    ("078160", "portions", "verb", "/ˈpɔːrʃənz/", "chia thành từng phần, phân chia"),
    ("078161", "portliness", "noun", "/ˈpɔːrtlinəs/", "vẻ béo tốt bệ vệ, đẫy đà"),
    ("078162", "portmanteaus", "noun", "/pɔːrtˈmæntoʊz/", "va li da lớn; từ ghép âm nghĩa"),
    ("078163", "portmanteaux", "noun", "/pɔːrtˈmæntoʊz/", "va li da lớn; từ ghép âm nghĩa"),
    ("078164", "portolan", "noun", "/ˈpɔːrtələn/", "hải đồ cảng biển thời Trung Cổ"),
    ("078165", "portolans", "noun", "/ˈpɔːrtələnz/", "hải đồ cảng biển thời Trung Cổ"),
    ("078166", "portrayable", "adj", "/pɔːrˈtreɪəbəl/", "có thể khắc họa, miêu tả được"),
    ("078167", "portreeve", "noun", "/ˈpɔːrtriːv/", "trưởng quan cảng thị (lịch sử Anh)"),
    ("078168", "portress", "noun", "/ˈpɔːrtrɪs/", "nữ nhân viên gác cổng"),
    ("078169", "ports", "verb", "/pɔːrts/", "chuyển mã phần mềm; bế súng"),
    ("078170", "portugall", "noun", "/ˈpɔːrtʃəɡəl/", "nước Bồ Đào Nha (chính tả cổ)"),
    ("078171", "portugalls", "noun", "/ˈpɔːrtʃəɡəlz/", "người Bồ Đào Nha (cổ)"),
    ("078172", "portulacaceae", "noun", "/ˌpɔːrtjʊləˈkeɪsiː/", "họ Rau sam (Portulacaceae)"),
    ("078173", "portulan", "noun", "/ˈpɔːrtjʊlən/", "hải đồ cảng biển thời Trung Cổ"),
    ("078174", "portunidae", "noun", "/pɔːrˈtjuːnɪdiː/", "họ Cua bơi (ghẹ, cua biển)"),
    ("078175", "portunus", "noun", "/pɔːrˈtjuːnəs/", "chi cua ghẹ bơi (Portunus)"),
    ("078176", "portwatcher", "noun", "/ˈpɔːrtˌwɒtʃər/", "lính canh gác bến cảng"),
    ("078177", "porzana", "noun", "/pɔːrˈzænə/", "chi gà nước đốm (Porzana)"),
    ("078178", "posable", "adj", "/ˈpoʊzəbəl/", "có thể tạo dáng (búp bê, mô hình)"),
    ("078179", "poses", "verb", "/ˈpoʊzɪz/", "tạo dáng; đặt câu hỏi; giả vờ"),
    ("078180", "poseuse", "noun", "/poʊˈzɜːz/", "người phụ nữ làm dáng màu mè"),
    ("078181", "poshly", "adv", "/ˈpɒʃli/", "một cách sang trọng, quý phái"),
    ("078182", "poshness", "noun", "/ˈpɒʃnəs/", "vẻ sang trọng, lịch lãm quý phái"),
    ("078183", "posilogy", "noun", "/poʊˈsɒlədʒi/", "khoa liều lượng thuốc (biến thể)"),
    ("078184", "posited", "verb", "/ˈpɑːzɪtɪd/", "đã đặt làm tiền đề, giả định"),
    ("078185", "positing", "verb", "/ˈpɑːzɪtɪŋ/", "đặt làm tiền đề, đưa ra giả định"),
    ("078186", "positionally", "adv", "/pəˈzɪʃənəli/", "theo vị trí; xét về vị trí"),
    ("078187", "positioned", "verb", "/pəˈzɪʃənd/", "đã đặt vào vị trí, định vị"),
    ("078188", "positions", "verb", "/pəˈzɪʃənz/", "đặt vào vị trí, định vị"),
    ("078189", "posits", "verb", "/ˈpɑːzɪts/", "đặt làm tiền đề, đưa ra giả định"),
    ("078190", "posology", "noun", "/poʊˈsɒlədʒi/", "liều lượng học (dược học)"),
    ("078191", "posseman", "noun", "/ˈpɒsɪmən/", "thành viên đội truy bắt dân phòng"),
    ("078192", "possesses", "verb", "/pəˈzɛsɪz/", "sở hữu; chiếm hữu; ám ảnh"),
    ("078193", "possessing", "verb", "/pəˈzɛsɪŋ/", "sở hữu; chiếm hữu; ám ảnh"),
    ("078194", "possessional", "adj", "/pəˈzɛʃənəl/", "thuộc quyền sở hữu"),
    ("078195", "possessions", "noun", "/pəˈzɛʃənz/", "tài sản, vật sở hữu; sự chiếm hữu"),
    ("078196", "possessory", "adj", "/pəˈzɛsəri/", "thuộc quyền chiếm hữu (luật học)"),
    ("078197", "possibilities", "noun", "/ˌpɑːsəˈbɪlɪtiz/", "khả năng có thể xảy ra; triển vọng"),
    ("078198", "possibleness", "noun", "/ˈpɑːsəbəlnəs/", "khả năng có thể xảy ra"),
    ("078199", "possumwood", "noun", "/ˈpɒsəmˌwʊd/", "cây thị gỗ cứng (hoặc Quintinia)"),
    ("078200", "postally", "adv", "/ˈpoʊstəli/", "bằng đường bưu điện"),
    ("078201", "postbiblical", "adj", "/ˌpoʊstˈbɪblɪkəl/", "thuộc thời kỳ sau Kinh Thánh"),
    ("078202", "postcava", "noun", "/ˌpoʊstˈkeɪvə/", "tĩnh mạch chủ dưới (giải phẫu)"),
]

with open("scratch/b36_r07_raw_p2.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r07_p2.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r07_p2 saved OK")
