import json

rows = [
    ("078003", "pomologist", "noun", "/pəˈmɒlədʒɪst/", "chuyên gia quả học (cây ăn quả)"),
    ("078004", "pomona", "noun", "/pəˈmoʊnə/", "nữ thần hoa quả Pomona (La Mã)"),
    ("078005", "pomoxis", "noun", "/pəˈmɒksɪs/", "chi cá vược crappie (Pomoxis)"),
    ("078006", "pompability", "noun", "/ˌpʌmpəˈbɪlɪti/", "khả năng bơm, năng suất bơm"),
    ("078007", "pompetta", "noun", "/pɒmˈpɛtə/", "bóng bóp mực in; ống hút nhỏ giọt"),
    ("078008", "pompier", "noun", "/pɒmˈpjɛr/", "lính cứu hỏa (Pháp); thang móc"),
    ("078009", "pompom", "noun", "/ˈpɑːmpɑːm/", "ngù len tròn; pháo bắn nhanh"),
    ("078010", "pomposo", "adv", "/pɒmˈpoʊsoʊ/", "trang nghiêm, oai vệ (âm nhạc)"),
    ("078011", "ponceau", "noun", "/pɒnˈsoʊ/", "màu đỏ thẫm hoa anh túc (ponceau)"),
    ("078012", "poncirus", "noun", "/pɒnˈsaɪrəs/", "chi cây cam ba lá (chỉ thực)"),
    ("078013", "pondage", "noun", "/ˈpɒndɪdʒ/", "lượng nước trữ ao hồ; sự tích nước"),
    ("078014", "ponderability", "noun", "/ˌpɒndərəˈbɪlɪti/", "tính cân đo được, có trọng lượng"),
    ("078015", "ponderation", "noun", "/ˌpɒndəˈreɪʃən/", "sự cân nhắc kỹ lưỡng; phép cân"),
    ("078016", "pondered", "verb", "/ˈpɑːndərd/", "đã suy ngẫm, nghiền ngẫm, cân nhắc"),
    ("078017", "ponderer", "noun", "/ˈpɑːndərər/", "người hay suy tư, trầm ngâm"),
    ("078018", "ponderingly", "adv", "/ˈpɑːndərɪŋli/", "một cách trầm ngâm, suy tư kỹ"),
    ("078019", "ponderosity", "noun", "/ˌpɒndəˈrɒsɪti/", "sự nặng nề; vẻ trang trọng quá mức"),
    ("078020", "ponderousness", "noun", "/ˈpɒndərəsnəs/", "sự nặng nề chậm chạp, rườm rà"),
    ("078021", "ponders", "verb", "/ˈpɑːndərz/", "suy ngẫm, nghiền ngẫm, cân nhắc"),
    ("078022", "pondfish", "noun", "/ˈpɒndfɪʃ/", "cá nuôi trong ao hồ"),
    ("078023", "ponding", "noun", "/ˈpɒndɪŋ/", "sự ứ đọng nước thành vũng, ao"),
    ("078024", "pondlet", "noun", "/ˈpɒndlɪt/", "vũng ao nhỏ"),
    ("078025", "pongamia", "noun", "/pɒŋˈɡeɪmiə/", "chi cây mấu dầu, bánh dày Pongamia"),
    ("078026", "ponged", "verb", "/pɒŋd/", "đã bốc mùi hôi thối (khẩu ngữ Anh)"),
    ("078027", "pongid", "noun", "/ˈpɒndʒɪd/", "loài vượn lớn (họ Đười ươi)"),
    ("078028", "pongidae", "noun", "/ˈpɒndʒɪdiː/", "họ Đười ươi, vượn lớn (Pongidae)"),
    ("078029", "ponging", "verb", "/ˈpɒŋɪŋ/", "bốc mùi hôi thối (khẩu ngữ Anh)"),
    ("078030", "pongs", "verb", "/pɒŋz/", "bốc mùi hôi thối (khẩu ngữ Anh)"),
    ("078031", "pongy", "adj", "/ˈpɒŋi/", "có mùi hôi thối, kham khẳm (Anh)"),
    ("078032", "ponies", "noun", "/ˈpoʊniz/", "ngựa giống nhỏ (pony); tiền đặt cọc"),
    ("078033", "ponka", "noun", "/ˈpɒŋkə/", "người bản địa Ponca (Bắc Mỹ)"),
    ("078034", "ponselle", "noun", "/pɒnˈsɛl/", "nữ danh ca opera Rosa Ponselle"),
    ("078035", "ponstel", "noun", "/ˈpɒnstɛl/", "thuốc giảm đau chống viêm Ponstel"),
    ("078036", "pontage", "noun", "/ˈpɒntɪdʒ/", "phí qua cầu (thuế cầu cổ)"),
    ("078037", "pontal", "adj", "/ˈpɒntəl/", "thuộc về cây cầu"),
    ("078038", "pontederia", "noun", "/ˌpɒntɪˈdɪriə/", "chi cây lục bình Mỹ (Pontederia)"),
    ("078039", "pontederiaceae", "noun", "/ˌpɒntɪˌdɪriˈeɪsiː/", "họ Lục bình (Pontederiaceae)"),
    ("078040", "pontic", "adj", "/ˈpɒntɪk/", "thuộc Biển Đen (Hắc Hải) hoặc cầu"),
    ("078041", "pontificalia", "noun", "/pɒnˌtɪfɪˈkeɪliə/", "phẩm phục và huy hiệu giám mục"),
    ("078042", "pontifically", "adv", "/pɒnˈtɪfɪkli/", "với giọng điệu lên mặt dạy đời"),
    ("078043", "pontificated", "verb", "/pɑːnˈtɪfɪˌkeɪtɪd/", "đã lên mặt dạy đời trịnh trọng"),
    ("078044", "pontificates", "verb", "/pɑːnˈtɪfɪˌkeɪts/", "lên mặt dạy đời trịnh trọng"),
    ("078045", "pontificating", "verb", "/pɑːnˈtɪfɪˌkeɪtɪŋ/", "lên mặt dạy đời trịnh trọng"),
    ("078046", "pontification", "noun", "/pɑːnˌtɪfɪˈkeɪʃən/", "lối nói lên mặt dạy đời; lễ phong"),
    ("078047", "pontificator", "noun", "/pɑːnˈtɪfɪˌkeɪtər/", "người hay nói giọng dạy đời"),
    ("078048", "pontify", "verb", "/ˈpɒntɪfaɪ/", "lên mặt phán xét (như giáo hoàng)"),
    ("078049", "pontil", "noun", "/ˈpɒntɪl/", "thanh sắt giữ phôi thổi thủy tinh"),
    ("078050", "ponto", "noun", "/ˈpɑːntoʊ/", "đơn vị đo chiều dài cổ Bồ Đào Nha"),
    ("078051", "ponton", "noun", "/ˈpɑːntən/", "cầu phao; xà lan phao"),
    ("078052", "pontoneer", "noun", "/ˌpɒntəˈnɪr/", "công binh bắc cầu phao"),
    ("078053", "pontonier", "noun", "/ˌpɒntəˈnɪr/", "công binh bắc cầu phao"),
    ("078054", "pontooned", "verb", "/pɑːnˈtuːnd/", "đã bắc cầu phao vượt qua"),
    ("078055", "pontooning", "verb", "/pɑːnˈtuːnɪŋ/", "bắc cầu phao vượt qua"),
    ("078056", "pontoons", "verb", "/pɑːnˈtuːnz/", "bắc cầu phao vượt qua"),
    ("078057", "ponycart", "noun", "/ˈpoʊniˌkɑːrt/", "xe ngựa nhỏ hai bánh (chở trẻ em)"),
    ("078058", "pooecetes", "noun", "/ˌpoʊɪˈsiːtiːz/", "chi chim sẻ đồng cỏ Pooecetes"),
    ("078059", "poofter", "noun", "/ˈpuːftər/", "từ miệt thị người đồng tính nam"),
    ("078060", "pooh", "intj", "/puː/", "xì, chà (tỏ ý khinh hoặc coi nhẹ)"),
    ("078061", "pooka", "noun", "/ˈpuːkə/", "yêu tinh biến hình (dân gian)"),
    ("078062", "pookoo", "noun", "/ˈpuːkuː/", "linh dương đồng cỏ puku (châu Phi)"),
    ("078063", "pooled", "verb", "/puːld/", "đã góp chung lại, tập trung nguồn"),
    ("078064", "pooling", "verb", "/ˈpuːlɪŋ/", "góp chung lại, tập trung nguồn lực"),
    ("078065", "pools", "verb", "/puːlz/", "góp chung lại, tập trung nguồn lực"),
    ("078066", "pooped", "verb", "/puːpt/", "đã đi nặng (khẩu ngữ); kiệt sức lử"),
    ("078067", "pooping", "verb", "/ˈpuːpɪŋ/", "đi nặng (khẩu ngữ); làm kiệt sức"),
    ("078068", "poops", "verb", "/puːps/", "đi nặng (khẩu ngữ); làm kiệt sức"),
    ("078069", "poorer", "adj", "/ˈpʊrər/", "nghèo hơn, kém hơn (so sánh hơn)"),
    ("078070", "poorest", "adj", "/ˈpʊrɪst/", "nghèo nhất, kém nhất (so sánh nhất)"),
    ("078071", "poorwill", "noun", "/ˈpʊrwɪl/", "chim cú muỗi nghèo Bắc Mỹ"),
    ("078072", "poove", "noun", "/puːv/", "từ miệt thị người đồng tính nam"),
    ("078073", "pooves", "noun", "/puːvz/", "từ miệt thị người đồng tính nam"),
    ("078074", "popedom", "noun", "/ˈpoʊpdəm/", "chức vị hoặc quyền lực Giáo hoàng"),
    ("078075", "popeyed", "adj", "/ˈpɑːpaɪd/", "mắt trố lồi ra, trừng mắt kinh ngạc"),
    ("078076", "popillia", "noun", "/pəˈpɪliə/", "chi bọ hung Nhật Bản (Popillia)"),
    ("078077", "popishly", "adv", "/ˈpoʊpɪʃli/", "mang tính giáo hoàng thái quá (cổ)"),
    ("078078", "popishness", "noun", "/ˈpoʊpɪʃnəs/", "sự sùng bái Giáo hoàng (từ cổ)"),
    ("078079", "poplitei", "noun", "/pɒpˈlɪtiaɪ/", "cơ kheo (mặt sau đầu gối)"),
    ("078080", "popliteus", "noun", "/pɒpˈlɪtiəs/", "cơ kheo (mặt sau đầu gối)"),
    ("078081", "poppa", "noun", "/ˈpɑːpə/", "bố, ba (cách gọi thân mật)"),
    ("078082", "poppadam", "noun", "/ˈpɒpədəm/", "bánh đa giòn đậu lăng Ấn Độ"),
    ("078083", "poppas", "noun", "/ˈpɑːpəz/", "bố, ba (cách gọi thân mật)"),
    ("078084", "popped", "verb", "/pɑːpt/", "đã nổ bốp; bật ra bất ngờ; ghé qua"),
    ("078085", "poppied", "adj", "/ˈpɑːpid/", "có nhiều hoa anh túc; buồn ngủ"),
    ("078086", "popple", "noun", "/ˈpɑːpəl/", "sóng vỗ nhấp nhô cuồn cuộn"),
    ("078087", "popply", "adj", "/ˈpɑːpli/", "nhấp nhô cuồn cuộn (mặt nước)"),
    ("078088", "pops", "verb", "/pɑːps/", "nổ bốp; bật ra bất ngờ; ghé qua"),
    ("078089", "popshop", "noun", "/ˈpɑːpʃɒp/", "hiệu cầm đồ (tiếng lóng Anh cũ)"),
    ("078090", "popsy", "noun", "/ˈpɑːpsi/", "cô gái trẻ (tiếng lóng Anh cũ)"),
    ("078091", "populariser", "noun", "/ˈpɒpjələraɪzər/", "người phổ biến, đại chúng hóa"),
    ("078092", "popularism", "noun", "/ˈpɒpjələrɪzəm/", "chủ nghĩa bình dân, đại chúng"),
    ("078093", "populates", "verb", "/ˈpɑːpjəleɪts/", "cư trú ở; điền dữ liệu tự động"),
    ("078094", "populating", "verb", "/ˈpɑːpjəˌleɪtɪŋ/", "cư trú ở; điền dữ liệu tự động"),
    ("078095", "populations", "noun", "/ˌpɑːpjəˈleɪʃənz/", "dân số; quần thể sinh vật"),
    ("078096", "populi", "noun", "/ˈpɒpjʊli/", "nhân dân, công chúng (tiếng Latinh)"),
    ("078097", "populists", "noun", "/ˈpɑːpjəlɪsts/", "người theo chủ nghĩa dân túy"),
    ("078098", "populously", "adv", "/ˈpɒpjələsli/", "đông đúc dân cư"),
    ("078099", "populousness", "noun", "/ˈpɒpjələsnəs/", "tình trạng đông dân cư"),
    ("078100", "popup", "noun", "/ˈpɑːpʌp/", "cửa sổ bật lên (web); sách nổi"),
    ("078101", "porcelainise", "verb", "/ˈpɔːrsəlɪnaɪz/", "tráng men sứ; hóa sứ"),
    ("078102", "porcelainize", "verb", "/ˈpɔːrsəlɪnaɪz/", "tráng men sứ; hóa sứ"),
]

with open("scratch/b36_r07_raw_p1.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r07_p1.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r07_p1 saved OK")
