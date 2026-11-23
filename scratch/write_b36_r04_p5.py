import json

rows = [
    ("076903", "placarding", "verb", "/ˈplækɑːrdɪŋ/", "dán áp phích, niêm yết thông báo"),
    ("076904", "placards", "verb", "/ˈplækɑːrdz/", "dán áp phích, niêm yết thông báo"),
    ("076905", "placated", "verb", "/ˈpleɪkeɪtɪd/", "đã xoa dịu, làm nguôi giận"),
    ("076906", "placater", "noun", "/ˈpleɪkeɪtər/", "người xoa dịu, người hòa giải"),
    ("076907", "placates", "verb", "/ˈpleɪkeɪts/", "xoa dịu, làm nguôi giận"),
    ("076908", "placatingly", "adv", "/ˈpleɪkeɪtɪŋli/", "với giọng xoa dịu, dỗ dành"),
    ("076909", "placative", "adj", "/ˈpleɪkeɪtɪv/", "có tính xoa dịu, làm dịu"),
    ("076910", "placeability", "noun", "/ˌpleɪsəˈbɪlɪti/", "độ dễ đổ (bê tông); khả năng bán"),
    ("076911", "placeholders", "noun", "/ˈpleɪsˌhoʊldərz/", "phần giữ chỗ (placeholder)"),
    ("076912", "placeman", "noun", "/ˈpleɪsmən/", "kẻ cầu chức được bổ nhiệm ăn lộc"),
    ("076913", "placentae", "noun", "/pləˈsɛntiː/", "nhau thai (y học); giá noãn"),
    ("076914", "placentalia", "noun", "/ˌplæsənˈteɪliə/", "phân lớp Thú có nhau thai"),
    ("076915", "placentate", "adj", "/ˈplæsənteɪt/", "có nhau thai; có giá noãn"),
    ("076916", "placentiferous", "adj", "/ˌplæsənˈtɪfərəs/", "có mang nhau thai; mang giá noãn"),
    ("076917", "placentigerous", "adj", "/ˌplæsənˈtɪdʒərəs/", "có mang nhau thai; mang giá noãn"),
    ("076918", "placentitis", "noun", "/ˌplæsənˈtaɪtɪs/", "chứng viêm nhau thai (y học)"),
    ("076919", "placering", "noun", "/ˈplæsərɪŋ/", "việc đãi vàng, khai thác sa khoáng"),
    ("076920", "places", "verb", "/ˈpleɪsɪz/", "đặt, để; xếp vị trí, sắp xếp"),
    ("076921", "placeseeker", "noun", "/ˈpleɪsˌsiːkər/", "người chạy chức, cầu quan"),
    ("076922", "placet", "noun", "/ˈpleɪsɛt/", "phiếu thuận, biểu quyết đồng ý"),
    ("076923", "placidness", "noun", "/ˈplæsɪdnəs/", "vẻ bình lặng, êm đềm, điềm tĩnh"),
    ("076924", "placidyl", "noun", "/ˈplæsɪdɪl/", "thuốc an thần gây ngủ Placidyl"),
    ("076925", "placing", "verb", "/ˈpleɪsɪŋ/", "đặt, để; xếp vị trí, sắp xếp"),
    ("076926", "placoderm", "noun", "/ˈplækədɜːrm/", "cá da phiến cổ đại (hóa thạch)"),
    ("076927", "placodermi", "noun", "/ˌplækəˈdɜːrmiː/", "lớp Cá da phiến (Placodermi)"),
    ("076928", "placuna", "noun", "/pləˈkjuːnə/", "chi sò cửa sổ mỏng (Placuna)"),
    ("076929", "plafond", "noun", "/plæˈfɒnd/", "trần nhà trang trí; hạn mức trần"),
    ("076930", "plagal", "adj", "/ˈpleɪɡəl/", "thuộc nhịp kết phụ (âm nhạc)"),
    ("076931", "plagianthus", "noun", "/ˌpleɪdʒiˈænθəs/", "chi cây gỗ dải Plagianthus"),
    ("076932", "plagiarisation", "noun", "/ˌpleɪdʒəraɪˈzeɪʃən/", "sự đạo văn, sao chép ý tưởng"),
    ("076933", "plagiariser", "noun", "/ˈpleɪdʒəraɪzər/", "kẻ đạo văn, ăn cắp ý tưởng"),
    ("076934", "plagiarises", "verb", "/ˈpleɪdʒəraɪzɪz/", "đạo văn, ăn cắp ý tưởng"),
    ("076935", "plagiarising", "verb", "/ˈpleɪdʒəraɪzɪŋ/", "đạo văn, ăn cắp ý tưởng"),
    ("076936", "plagiaristic", "adj", "/ˌpleɪdʒəˈrɪstɪk/", "mang tính đạo văn, sao chép"),
    ("076937", "plagiarization", "noun", "/ˌpleɪdʒəraɪˈzeɪʃən/", "sự đạo văn, sao chép ý tưởng"),
    ("076938", "plagiarizer", "noun", "/ˈpleɪdʒəraɪzər/", "kẻ đạo văn, ăn cắp ý tưởng"),
    ("076939", "plagiarizes", "verb", "/ˈpleɪdʒəraɪzɪz/", "đạo văn, ăn cắp ý tưởng"),
    ("076940", "plagiarizing", "verb", "/ˈpleɪdʒəraɪzɪŋ/", "đạo văn, ăn cắp ý tưởng"),
    ("076941", "plagiary", "noun", "/ˈpleɪdʒəri/", "hành vi đạo văn; kẻ đạo văn"),
    ("076942", "plagioclastic", "adj", "/ˌpleɪdʒioʊˈklæstɪk/", "thuộc khoáng vật fenspat plagiocla"),
    ("076943", "plagioclimax", "noun", "/ˌpleɪdʒioʊˈklaɪmæks/", "cao đỉnh sinh thái do con người"),
    ("076944", "plagiosere", "noun", "/ˈpleɪdʒioʊsɪr/", "diễn thế sinh thái bị xáo trộn"),
    ("076945", "plagiotropic", "adj", "/ˌpleɪdʒiəˈtrɒpɪk/", "hướng nghiêng (thực vật học)"),
    ("076946", "plagiotropism", "noun", "/ˌpleɪdʒiˈɒtrəpɪzəm/", "tính hướng nghiêng (thực vật)"),
    ("076947", "plagiotropous", "adj", "/ˌpleɪdʒiˈɒtrəpəs/", "mọc hướng nghiêng (thực vật)"),
    ("076948", "plagued", "verb", "/pleɪɡd/", "đã gây tai họa; quấy rầy triền miên"),
    ("076949", "plagues", "verb", "/pleɪɡz/", "gây tai họa; quấy rầy triền miên"),
    ("076950", "plaguesome", "adj", "/ˈpleɪɡsəm/", "phiền toái, rầy rà, khó chịu"),
    ("076951", "plaguey", "adj", "/ˈpleɪɡi/", "phiền phức, khó chịu; gây dịch"),
    ("076952", "plaguily", "adv", "/ˈpleɪɡɪli/", "một cách rất khó chịu, phiền toái"),
    ("076953", "plaguing", "verb", "/ˈpleɪɡɪŋ/", "gây tai họa; quấy rầy triền miên"),
    ("076954", "plainclothesman", "noun", "/ˈpleɪnˌkloʊðzmən/", "cảnh sát mặc thường phục"),
    ("076955", "plains", "adj", "/pleɪnz/", "thuộc vùng đồng bằng, thảo nguyên"),
    ("076956", "plainsmen", "noun", "/ˈpleɪnzmən/", "người sống ở vùng đồng bằng"),
    ("076957", "plaintext", "noun", "/ˈpleɪntɛkst/", "văn bản gốc chưa mã hóa (bản rõ)"),
    ("076958", "plaintiffs", "noun", "/ˈpleɪntɪfs/", "nguyên đơn (trong vụ kiện dân sự)"),
    ("076959", "plaintiveness", "noun", "/ˈpleɪntɪvnəs/", "vẻ buồn bã, ai oán, thê lương"),
    ("076960", "plaited", "verb", "/ˈpleɪtɪd/", "đã bện, tết tóc; đã xếp nếp"),
    ("076961", "plaiter", "noun", "/ˈpleɪtər/", "người tết tóc, bện dây, xếp nếp"),
    ("076962", "plaiting", "verb", "/ˈpleɪtɪŋ/", "bện, tết tóc; xếp nếp"),
    ("076963", "plaits", "verb", "/pleɪts/", "bện, tết tóc; xếp nếp"),
    ("076964", "planate", "adj", "/ˈpleɪneɪt/", "phẳng, bẹt (cơ học, sinh học)"),
    ("076965", "planch", "noun", "/plæntʃ/", "phiến đá hoặc tấm kim loại mỏng"),
    ("076966", "planed", "verb", "/pleɪnd/", "đã bào nhẵn gỗ; đã lướt trên nước"),
    ("076967", "planeform", "noun", "/ˈpleɪnfɔːrm/", "hình chiếu bằng cánh máy bay"),
    ("076968", "planeness", "noun", "/ˈpleɪnnəs/", "tính phẳng, độ phẳng bề mặt"),
    ("076969", "planera", "noun", "/pləˈnɪrə/", "chi cây gỗ sồi nước (Planera)"),
    ("076970", "planes", "verb", "/pleɪnz/", "bào nhẵn (gỗ); lướt trên mặt nước"),
    ("076971", "planetal", "adj", "/ˈplænɪtəl/", "thuộc về hành tinh"),
    ("076972", "planetaria", "noun", "/ˌplænɪˈtɛriə/", "nhà chiếu mô hình vũ trụ"),
    ("076973", "planetism", "noun", "/ˈplænɪtɪzəm/", "hiện tượng chuyển động hành tinh"),
    ("076974", "planetoidal", "adj", "/ˌplænɪˈtɔɪdəl/", "thuộc tiểu hành tinh"),
    ("076975", "plangency", "noun", "/ˈplændʒənsi/", "âm vang dội, tiếng ngân trầm buồn"),
    ("076976", "plangently", "adv", "/ˈplændʒəntli/", "một cách ngân vang, trầm hùng"),
    ("076977", "planiform", "adj", "/ˈpleɪnɪfɔːrm/", "dạng dẹt phẳng (mặt khớp xương)"),
    ("076978", "planigraphy", "noun", "/pləˈnɪɡrəfi/", "phép chụp cắt lớp mặt phẳng"),
    ("076979", "planimeter", "noun", "/pləˈnɪmɪtər/", "dụng cụ đo diện tích mặt phẳng"),
    ("076980", "planimetric", "adj", "/ˌplænɪˈmɛtrɪk/", "thuộc phép đo diện tích mặt phẳng"),
    ("076981", "planimetrical", "adj", "/ˌplænɪˈmɛtrɪkəl/", "thuộc phép đo diện tích mặt phẳng"),
    ("076982", "planimetrically", "adv", "/ˌplænɪˈmɛtrɪkli/", "bằng phép đo diện tích mặt phẳng"),
    ("076983", "planimetries", "noun", "/pləˈnɪmɪtriz/", "phép đo diện tích; hình học phẳng"),
    ("076984", "planimetry", "noun", "/pləˈnɪmɪtri/", "phép đo diện tích; hình học phẳng"),
    ("076985", "planing", "verb", "/ˈpleɪnɪŋ/", "bào nhẵn (gỗ); lướt trên mặt nước"),
    ("076986", "planipetalous", "adj", "/ˌplænɪˈpɛtələs/", "có cánh hoa phẳng dẹt"),
    ("076987", "planish", "verb", "/ˈplænɪʃ/", "dát phẳng; đánh bóng kim loại"),
    ("076988", "planisher", "noun", "/ˈplænɪʃər/", "thợ hoặc búa dát phẳng kim loại"),
    ("076989", "planisphere", "noun", "/ˈplænɪsfɪr/", "bình đồ sao; bản đồ cầu dẹt"),
    ("076990", "planispheric", "adj", "/ˌplænɪˈsfɛrɪk/", "thuộc bình đồ sao, bản đồ cầu dẹt"),
    ("076991", "planispiral", "adj", "/ˌpleɪnɪˈspaɪrəl/", "xoắn ốc trên một mặt phẳng"),
    ("076992", "planissimo", "adv", "/plɑːˈnɪsɪmoʊ/", "cực nhẹ, thật khẽ (âm nhạc)"),
    ("076993", "planked", "verb", "/plæŋkt/", "đã lát ván gỗ; đặt mạnh xuống"),
    ("076994", "planks", "verb", "/plæŋks/", "lát ván gỗ; đặt mạnh xuống"),
    ("076995", "planktont", "noun", "/ˈplæŋktɒnt/", "sinh vật phù du (biến thể)"),
    ("076996", "planktonts", "noun", "/ˈplæŋktɒnts/", "sinh vật phù du (biến thể)"),
    ("076997", "planless", "adj", "/ˈplænləs/", "không có kế hoạch, vô định"),
    ("076998", "planococcus", "noun", "/ˌplænoʊˈkɒkəs/", "chi rệp sáp cam (Planococcus)"),
    ("076999", "planoconcave", "adj", "/ˌpleɪnoʊˈkɒnkeɪv/", "phẳng lõm (thấu kính)"),
    ("077000", "planoconidium", "noun", "/ˌpleɪnoʊkoʊˈnɪdiəm/", "bào tử đính di động"),
    ("077001", "planoconvex", "adj", "/ˌpleɪnoʊˈkɒnvɛks/", "phẳng lồi (thấu kính)"),
    ("077002", "planographic", "adj", "/ˌplænəˈɡræfɪk/", "thuộc kỹ thuật in phẳng (litho)"),
]

with open("scratch/b36_r04_raw_p5.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r04_p5.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r04_p5 saved OK")
