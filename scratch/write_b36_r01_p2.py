import json

rows = [
    ("075103", "pedogenesis", "noun", "/ˌpiːdoʊˈdʒɛnɪsɪs/", "hiện tượng ấu sinh; hình thành đất"),
    ("075104", "pedogenic", "adj", "/ˌpiːdəˈdʒɛnɪk/", "thuộc quá trình hình thành đất"),
    ("075105", "pedogeny", "noun", "/pɪˈdɒdʒəni/", "sự hình thành đất (thổ nhưỡng)"),
    ("075106", "pedologic", "adj", "/ˌpiːdəˈlɒdʒɪk/", "thuộc thổ nhưỡng học (khoa học đất)"),
    ("075107", "pedologically", "adv", "/ˌpiːdəˈlɒdʒɪkli/", "về mặt thổ nhưỡng học"),
    ("075108", "pedologist", "noun", "/pɪˈdɒlədʒɪst/", "nhà thổ nhưỡng học; nhà nhi khoa"),
    ("075109", "pedometers", "noun", "/pɪˈdɒmɪtərz/", "máy đếm bước chân"),
    ("075110", "peds", "noun", "/piːdz/", "khoa nhi (y học); khối đất kết tụ"),
    ("075111", "peduncular", "adj", "/pɪˈdʌŋkjələr/", "có cuống; thuộc cuống (sinh học)"),
    ("075112", "pedwood", "noun", "/ˈpɛdwʊd/", "cây gỗ cứng pedwood (bụi gỗ chó)"),
    ("075113", "peed", "verb", "/piːd/", "đã đi tiểu (khẩu ngữ)"),
    ("075114", "peeked", "verb", "/piːkt/", "đã nhìn trộm; đã hé nhìn"),
    ("075115", "peeking", "verb", "/ˈpiːkɪŋ/", "nhìn trộm; hé nhìn"),
    ("075116", "peeks", "verb", "/piːks/", "nhìn trộm; hé nhìn"),
    ("075117", "peelings", "noun", "/ˈpiːlɪŋz/", "vỏ gọt ra; mảnh da bong tróc"),
    ("075118", "peels", "verb", "/piːlz/", "gọt vỏ; bóc vỏ; bong tróc"),
    ("075119", "peening", "noun", "/ˈpiːnɪŋ/", "sự tán đầu búa (gia công kim loại)"),
    ("075120", "peepbo", "noun", "/ˈpiːpˌboʊ/", "trò chơi ú òa (với trẻ nhỏ)"),
    ("075121", "peeped", "verb", "/piːpt/", "đã nhìn hé; đã kêu chiêm chiếp"),
    ("075122", "peeping", "verb", "/ˈpiːpɪŋ/", "nhìn hé; kêu chiêm chiếp"),
    ("075123", "peeps", "verb", "/piːps/", "nhìn hé; kêu chiêm chiếp"),
    ("075124", "peerages", "noun", "/ˈpɪrɪdʒɪz/", "hàng quý tộc; tước vị quý tộc Anh"),
    ("075125", "peered", "verb", "/pɪrd/", "đã nhìn chăm chú; đã hé ra"),
    ("075126", "peering", "verb", "/ˈpɪrɪŋ/", "nhìn chăm chú; hé ra"),
    ("075127", "peerlessly", "adv", "/ˈpɪrləsli/", "vô song, không gì sánh bằng"),
    ("075128", "peerlessness", "noun", "/ˈpɪrləsnəs/", "tính vô song, không gì sánh kịp"),
    ("075129", "peers", "verb", "/pɪrz/", "nhìn chăm chú; hé ra"),
    ("075130", "pees", "verb", "/piːz/", "đi tiểu (khẩu ngữ)"),
    ("075131", "peeths", "noun", "/piːθs/", "chợ phiên nông sản Ấn Độ (peeth)"),
    ("075132", "peewit", "noun", "/ˈpiːwɪt/", "chim te te mào (vanellus)"),
    ("075133", "pegamoid", "noun", "/ˈpɛɡəmɔɪd/", "vải giả da pegamoid (bọc sách)"),
    ("075134", "pegged", "verb", "/pɛɡd/", "đã đóng chốt; đã neo giữ tỷ giá"),
    ("075135", "pegging", "verb", "/ˈpɛɡɪŋ/", "đóng chốt; neo giữ tỷ giá"),
    ("075136", "pegmatitic", "adj", "/ˌpɛɡməˈtɪtɪk/", "thuộc đá pegmatit (địa chất)"),
    ("075137", "pegs", "verb", "/pɛɡz/", "đóng chốt; neo giữ tỷ giá"),
    ("075138", "pehlevi", "noun", "/ˈpɑːləvi/", "tiếng Pahlavi (Ba Tư trung đại)"),
    ("075139", "peices", "noun", "/ˈpiːsɪz/", "dạng viết nhầm của pieces (mảnh)"),
    ("075140", "pein", "noun", "/piːn/", "đầu tròn búa nguội; phần mỏm búa"),
    ("075141", "peireskia", "noun", "/pəˈrɛskiə/", "chi xương rồng có lá (Pereskia)"),
    ("075142", "pejoration", "noun", "/ˌpɛdʒəˈreɪʃən/", "sự làm giảm giá trị; sự thoái nghĩa"),
    ("075143", "pekin", "noun", "/ˈpiːkɪn/", "lụa Bắc Kinh; vải sọc pekin"),
    ("075144", "pekingman", "noun", "/ˌpiːkɪŋˈmæn/", "người vượn Bắc Kinh (hóa thạch)"),
    ("075145", "pelada", "noun", "/pəˈlɑːdə/", "chứng rụng tóc từng mảng (y học)"),
    ("075146", "pelagian", "adj", "/pɪˈleɪdʒiən/", "thuộc biển khơi; thuyết Pelagius"),
    ("075147", "pelasgic", "adj", "/pəˈlæzdʒɪk/", "thuộc dân tộc Pelasgi (Hy Lạp cổ)"),
    ("075148", "pele", "noun", "/ˈpɛleɪ/", "nữ thần lửa Pele; tháp phòng thủ"),
    ("075149", "pelecanidae", "noun", "/ˌpɛlɪˈkænɪdiː/", "họ Bồ nông (Pelecanidae)"),
    ("075150", "pelecaniformes", "noun", "/ˌpɛlɪˌkænɪˈfɔːrmiːz/", "bộ Bồ nông (Pelecaniformes)"),
    ("075151", "pelecanoididae", "noun", "/ˌpɛlɪkəˈnɔɪdɪdiː/", "họ Chim lặn phương Nam"),
    ("075152", "pelecypod", "adj", "/pəˈlɛsɪpɒd/", "thuộc lớp hai mảnh vỏ (nhuyễn thể)"),
    ("075153", "pelecypodous", "adj", "/ˌpɛlɪˈsɪpədəs/", "thuộc lớp hai mảnh vỏ (nhuyễn thể)"),
    ("075154", "pelerine", "noun", "/ˈpɛləriːn/", "áo choàng vai ngắn của phụ nữ"),
    ("075155", "pelew", "noun", "/pəˈluː/", "quần đảo Palau (tên cũ Pelew)"),
    ("075156", "pelicans", "noun", "/ˈpɛlɪkənz/", "chim bồ nông"),
    ("075157", "peliosis", "noun", "/ˌpɛliˈoʊsɪs/", "bệnh u mạch xuất huyết dưới da"),
    ("075158", "pellaea", "noun", "/pəˈliːə/", "chi dương xỉ vách đá (Pellaea)"),
    ("075159", "pellagrous", "adj", "/pəˈleɪɡrəs/", "mắc bệnh nứt da pellagra (y học)"),
    ("075160", "pelleted", "verb", "/ˈpɛlɪtɪd/", "đã nén thành viên; ném liên tiếp"),
    ("075161", "pelleting", "verb", "/ˈpɛlɪtɪŋ/", "nén thành viên; ném liên tiếp"),
    ("075162", "pellets", "verb", "/ˈpɛlɪts/", "nén thành viên; ném liên tiếp"),
    ("075163", "pellicular", "adj", "/pəˈlɪkjələr/", "thuộc màng mỏng, lớp vỏ bọc"),
    ("075164", "pellicularia", "noun", "/pəˌlɪkjəˈlɛriə/", "chi nấm sợi Pellicularia"),
    ("075165", "pellitory", "noun", "/ˈpɛlɪtəri/", "cây cỏ mọc khe tường; cúc thơm"),
    ("075166", "pellucidity", "noun", "/ˌpɛljuˈsɪdɪti/", "tính trong suốt; sự rõ ràng"),
    ("075167", "pellucidly", "adv", "/pəˈluːsɪdli/", "trong suốt; một cách rõ ràng"),
    ("075168", "pellucidness", "noun", "/pəˈluːsɪdnəs/", "tính trong suốt; sự rõ ràng"),
    ("075169", "pelma", "noun", "/ˈpɛlmə/", "lòng bàn chân (giải phẫu)"),
    ("075170", "pelmanism", "noun", "/ˈpɛlmənɪzəm/", "phương pháp luyện trí nhớ Pelman"),
    ("075171", "pelobatidae", "noun", "/ˌpɛloʊˈbætɪdiː/", "họ Cóc đào hang (Pelobatidae)"),
    ("075172", "peloria", "noun", "/pəˈlɔːriə/", "tính cân xứng tỏa tròn bất thường"),
    ("075173", "peloric", "adj", "/pəˈlɔːrɪk/", "có hoa biến dạng đối xứng đều"),
    ("075174", "pelory", "noun", "/ˈpɛləri/", "hiện tượng hoa biến dạng đối xứng"),
    ("075175", "pelotons", "noun", "/ˈpɛlətɒnz/", "đoàn đua xe đạp (peloton)"),
    ("075176", "pelta", "noun", "/ˈpɛltə/", "chiếc khiên nhẹ hình trăng khuyết"),
    ("075177", "peltae", "noun", "/ˈpɛltiː/", "chiếc khiên nhẹ hình trăng khuyết"),
    ("075178", "peltandra", "noun", "/pɛlˈtændrə/", "chi cây ráy mũi tên Peltandra"),
    ("075179", "peltast", "noun", "/ˈpɛltæst/", "lính nhẹ cầm khiên cổ Hy Lạp"),
    ("075180", "peltasts", "noun", "/ˈpɛltæsts/", "lính nhẹ cầm khiên cổ Hy Lạp"),
    ("075181", "peltately", "adv", "/ˈpɛlteɪtli/", "theo dạng hình khiên tròn"),
    ("075182", "pelted", "verb", "/ˈpɛltɪd/", "đã ném tới tấp; trút xuống (mưa)"),
    ("075183", "peltinervate", "adj", "/ˌpɛltɪˈnɜːrveɪt/", "có gân lá tỏa dạng hình khiên"),
    ("075184", "peltiphyllum", "noun", "/ˌpɛltɪˈfɪləm/", "chi cây lá khiên (Peltiphyllum)"),
    ("075185", "peltmonger", "noun", "/ˈpɛltˌmʌŋɡər/", "người buôn da lông thú sống"),
    ("075186", "peltmongers", "noun", "/ˈpɛltˌmʌŋɡərz/", "người buôn da lông thú sống"),
    ("075187", "peltries", "noun", "/ˈpɛltriz/", "da thú còn lông (chưa thuộc)"),
    ("075188", "peltry", "noun", "/ˈpɛltri/", "da thú còn lông (chưa thuộc)"),
    ("075189", "pelts", "verb", "/pɛlts/", "ném tới tấp; trút xuống (mưa)"),
    ("075190", "peludo", "noun", "/peɪˈluːdoʊ/", "ta-tu lông rậm Nam Mỹ (peludo)"),
    ("075191", "pelves", "noun", "/ˈpɛlviːz/", "khung chậu; bể thận (giải phẫu)"),
    ("075192", "pelvimeter", "noun", "/pɛlˈvɪmɪtər/", "thước đo khung chậu (sản khoa)"),
    ("075193", "pelvimetry", "noun", "/pɛlˈvɪmɪtri/", "phép đo kích thước khung chậu"),
    ("075194", "pelvisacral", "adj", "/ˌpɛlvɪˈseɪkrəl/", "thuộc xương chậu và xương cùng"),
    ("075195", "pelvises", "noun", "/ˈpɛlvɪsɪz/", "khung chậu; bể thận (giải phẫu)"),
    ("075196", "pelvisternum", "noun", "/ˌpɛlvɪˈstɜːrnəm/", "sụn trước xương mu (giải phẫu)"),
    ("075197", "pelycosaur", "noun", "/ˈpɛlɪkəˌsɔːr/", "bò sát cổ có vây lưng Pelycosaur"),
    ("075198", "pelycosauria", "noun", "/ˌpɛlɪkəˈsɔːriə/", "bộ Bò sát cổ Pelycosauria"),
    ("075199", "pemican", "noun", "/ˈpɛmɪkən/", "thịt khô nghiền trộn mỡ pemican"),
    ("075200", "pemoline", "noun", "/ˈpɛməliːn/", "chất kích thích thần kinh pemolin"),
    ("075201", "pempheridae", "noun", "/ˌpɛmfəˈraɪdiː/", "họ Cá tráp hang (Pempheridae)"),
    ("075202", "pemphigous", "adj", "/ˈpɛmfɪɡəs/", "thuộc bệnh bóng nước pemphigus"),
]

with open("scratch/b36_r01_raw_p2.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r01_p2.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r01_p2 saved OK")
