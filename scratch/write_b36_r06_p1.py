import json

rows = [
    ("077503", "pneumograph", "noun", "/ˈnjuːməɡræf/", "máy ghi nhịp thở lồng ngực"),
    ("077504", "pneumographic", "adj", "/ˌnjuːməˈɡræfɪk/", "thuộc máy ghi nhịp thở"),
    ("077505", "pneumohydraulic", "adj", "/ˌnjuːmoʊhaɪˈdrɔːlɪk/", "thuộc khí nén thủy lực"),
    ("077506", "pneumolith", "noun", "/ˈnjuːməlɪθ/", "sỏi phổi (y học)"),
    ("077507", "pneumonoconiosis", "noun", "/njuːˌmɒnoʊkoʊniˈoʊsɪs/", "bệnh bụi phổi (y học)"),
    ("077508", "pneumorhagia", "noun", "/ˌnjuːməˈreɪdʒə/", "chứng xuất huyết phổi (y học)"),
    ("077509", "pneumorrhagia", "noun", "/ˌnjuːməˈreɪdʒə/", "chứng xuất huyết phổi (y học)"),
    ("077510", "pneumoscope", "noun", "/ˈnjuːməskoʊp/", "dụng cụ đo hô hấp phổi"),
    ("077511", "pneumostome", "noun", "/ˈnjuːməstoʊm/", "lỗ thở phổi (ốc sên, nhện)"),
    ("077512", "pneumotaxis", "noun", "/ˌnjuːməˈtæksɪs/", "tính hướng khí (sinh vật học)"),
    ("077513", "pneumovax", "noun", "/ˈnjuːməvæks/", "vắc-xin phế cầu Pneumovax"),
    ("077514", "pneutronic", "adj", "/njuːˈtrɒnɪk/", "thuộc hệ thống khí nén điện tử"),
    ("077515", "poachable", "adj", "/ˈpoʊtʃəbəl/", "có thể săn trộm; dễ chần (trứng)"),
    ("077516", "poachard", "noun", "/ˈpoʊtʃərd/", "vịt đầu nâu (Aythya ferina)"),
    ("077517", "poachers", "noun", "/ˈpoʊtʃərz/", "kẻ săn trộm; nồi chần trứng"),
    ("077518", "poaches", "verb", "/ˈpoʊtʃɪz/", "săn bắn trộm; chần nước sôi; lấn"),
    ("077519", "pochette", "noun", "/poʊˈʃɛt/", "ví cầm tay nhỏ; vĩ cầm bỏ túi"),
    ("077520", "pochettes", "noun", "/poʊˈʃɛts/", "ví cầm tay nhỏ; vĩ cầm bỏ túi"),
    ("077521", "pocketcomb", "noun", "/ˈpɑːkɪtˌkoʊm/", "lược nhỏ bỏ túi"),
    ("077522", "pocketed", "verb", "/ˈpɑːkɪtɪd/", "đã bỏ túi; đánh bi-a vào lỗ; giấu"),
    ("077523", "pocketing", "verb", "/ˈpɑːkɪtɪŋ/", "bỏ túi; đánh bi-a vào lỗ; chiếm"),
    ("077524", "pocketless", "adj", "/ˈpɑːkɪtləs/", "không có túi áo quần"),
    ("077525", "pocketpussy", "noun", "/ˈpɑːkɪtˌpʊsi/", "dụng cụ tình dục nam (bỏ túi)"),
    ("077526", "pockets", "verb", "/ˈpɑːkɪts/", "bỏ túi; đánh bi-a vào lỗ; chiếm"),
    ("077527", "pockety", "adj", "/ˈpɑːkɪti/", "có nhiều túi quặng; không đều"),
    ("077528", "pockiness", "noun", "/ˈpɑːkinəs/", "tình trạng rỗ mặt, có nốt rỗ"),
    ("077529", "pocky", "adj", "/ˈpɑːki/", "bị rỗ hoa; có nhiều nốt đậu mùa"),
    ("077530", "poco", "adv", "/ˈpoʊkoʊ/", "một chút, hơi (thuật ngữ âm nhạc)"),
    ("077531", "pococurante", "adj", "/ˌpoʊkoʊkjʊˈrænti/", "thản nhiên, thờ ơ, lãnh đạm"),
    ("077532", "pococuranteism", "noun", "/ˌpoʊkoʊkjʊˈræntɪɪzəm/", "thái độ thờ ơ, lãnh đạm thản nhiên"),
    ("077533", "pococurantism", "noun", "/ˌpoʊkoʊkjʊˈræntɪzəm/", "thái độ thờ ơ, lãnh đạm thản nhiên"),
    ("077534", "poculiform", "adj", "/ˈpɒkjʊlɪfɔːrm/", "có hình chiếc cốc, hình chén"),
    ("077535", "podagra", "noun", "/pəˈdæɡrə/", "bệnh gút ở ngón chân cái (y học)"),
    ("077536", "podagral", "adj", "/pəˈdæɡrəl/", "thuộc hoặc mắc bệnh gút chân"),
    ("077537", "podagric", "adj", "/pəˈdæɡrɪk/", "thuộc hoặc mắc bệnh gút chân"),
    ("077538", "podagrous", "adj", "/pəˈdæɡrəs/", "thuộc hoặc mắc bệnh gút chân"),
    ("077539", "podal", "adj", "/ˈpoʊdəl/", "thuộc bàn chân (y học)"),
    ("077540", "podalgia", "noun", "/poʊˈdældʒə/", "chứng đau bàn chân (y học)"),
    ("077541", "podalyria", "noun", "/ˌpɒdəˈlɪriə/", "chi cây đậu cảnh Podalyria"),
    ("077542", "podargidae", "noun", "/pɒˈdɑːrdʒɪdiː/", "họ Chim mỏ ếch (Podargidae)"),
    ("077543", "podargus", "noun", "/pəˈdɑːrɡəs/", "chi chim mỏ ếch (Podargus)"),
    ("077544", "podaxaceae", "noun", "/ˌpoʊdækˈseɪsiː/", "họ Nấm bụng Podaxaceae"),
    ("077545", "podded", "verb", "/ˈpɑːdɪd/", "đã bóc vỏ đậu; kết quả dạng đậu"),
    ("077546", "podding", "verb", "/ˈpɑːdɪŋ/", "bóc vỏ đậu; kết quả dạng đậu"),
    ("077547", "poddy", "noun", "/ˈpɑːdi/", "bê non mồ côi bú bình; mập lùn (Úc)"),
    ("077548", "podeal", "adj", "/ˈpoʊdiəl/", "thuộc cuống bụng (côn trùng)"),
    ("077549", "podeon", "noun", "/ˈpoʊdiɒn/", "cuống bụng thon (ong, kiến)"),
    ("077550", "podetium", "noun", "/poʊˈdiːʃəm/", "cuống sinh bào tử (địa y)"),
    ("077551", "podex", "noun", "/ˈpoʊdɛks/", "vùng hậu môn, đốt cuối (côn trùng)"),
    ("077552", "podge", "noun", "/pɑːdʒ/", "người béo lùn mập mạp"),
    ("077553", "podginess", "noun", "/ˈpɑːdʒinəs/", "dáng vẻ béo lùn, mũm mĩm"),
    ("077554", "podia", "noun", "/ˈpoʊdiə/", "bục phát biểu; dãy ghế đấu trường"),
    ("077555", "podiatric", "adj", "/ˌpɒdiˈætrɪk/", "thuộc chuyên khoa bàn chân"),
    ("077556", "podicipedidae", "noun", "/ˌpɒdɪsɪˈpɛdɪdiː/", "họ Chim lặn le hôi (Podicipedidae)"),
    ("077557", "podicipediformes", "noun", "/ˌpɒdɪˌsɪpɪdɪˈfɔːrmiːz/", "bộ Chim lặn le hôi"),
    ("077558", "podicipitiformes", "noun", "/ˌpɒdɪˌsɪpɪtɪˈfɔːrmiːz/", "bộ Chim lặn le hôi"),
    ("077559", "podilymbus", "noun", "/ˌpɒdɪˈlɪmbəs/", "chi chim lặn mỏ khoằm Podilymbus"),
    ("077560", "podiums", "noun", "/ˈpoʊdiəmz/", "bục giảng, bục trao giải; bệ đỡ"),
    ("077561", "podlike", "adj", "/ˈpɑːdlaɪk/", "giống vỏ quả đậu"),
    ("077562", "podobranchiae", "noun", "/ˌpɒdoʊˈbræŋkiːiː/", "mang gắn gốc chân (giáp xác)"),
    ("077563", "podocarp", "noun", "/ˈpɒdəkɑːrp/", "cây thông tre; cây kim giao (tùng)"),
    ("077564", "podocarpaceae", "noun", "/ˌpɒdoʊkɑːrˈpeɪsiː/", "họ Thông tre, họ Kim giao"),
    ("077565", "podocephalous", "adj", "/ˌpɒdoʊˈsɛfələs/", "có cụm hoa đầu trên cuống dài"),
    ("077566", "podoconus", "noun", "/ˌpɒdəˈkoʊnəs/", "trục nón trung tâm (trùng phóng xạ)"),
    ("077567", "podocyst", "noun", "/ˈpɒdəsɪst/", "túi bám mầm (sứa biển)"),
    ("077568", "pododerm", "noun", "/ˈpɒdədɜːrm/", "lớp bì móng guốc (thú y)"),
    ("077569", "podogram", "noun", "/ˈpɒdəɡræm/", "dấu in bàn chân (phân tích dáng đi)"),
    ("077570", "podogynium", "noun", "/ˌpɒdəˈdʒɪniəm/", "cuống nhụy hoa (thực vật học)"),
    ("077571", "podomere", "noun", "/ˈpɒdəmɪr/", "đốt chân (động vật chân khớp)"),
    ("077572", "podophyllous", "adj", "/ˌpɒdəˈfɪləs/", "có chân dạng lá (động vật)"),
    ("077573", "podophyllum", "noun", "/ˌpɒdəˈfɪləm/", "chi cây táo ma (Podophyllum)"),
    ("077574", "pods", "verb", "/pɑːdz/", "bóc vỏ đậu; kết quả dạng đậu"),
    ("077575", "podsol", "noun", "/ˈpɒdzɒl/", "đất pốt-dôn (đất xám bạc màu)"),
    ("077576", "podzolic", "adj", "/pɒdˈzɒlɪk/", "thuộc loại đất pốt-dôn"),
    ("077577", "poeciliid", "noun", "/piːˈsɪliɪd/", "cá khổng tước, cá bảy màu"),
    ("077578", "poeciliidae", "noun", "/ˌpiːsɪˈlaɪɪdiː/", "họ Cá khổng tước, cá bảy màu"),
    ("077579", "poecilocapsus", "noun", "/ˌpiːsɪloʊˈkæpsəs/", "chi bọ xít cây (Poecilocapsus)"),
    ("077580", "poecilogale", "noun", "/ˌpiːsɪˈlɒɡəli/", "chi chồn sọc trắng châu Phi"),
    ("077581", "poenology", "noun", "/piːˈnɒlədʒi/", "hình phạt học (chế độ nhà tù)"),
    ("077582", "poephila", "noun", "/poʊˈɛfɪlə/", "chi chim sẻ cỏ Úc (Poephila)"),
    ("077583", "poetaster", "noun", "/ˈpoʊɪˌtæstər/", "nhà thơ xoàng, kẻ làm thơ tồi"),
    ("077584", "poetasters", "noun", "/ˈpoʊɪˌtæstərz/", "nhà thơ xoàng, kẻ làm thơ tồi"),
    ("077585", "poeticality", "noun", "/ˌpoʊɪtɪˈkælɪti/", "chất thơ, tính thi ca"),
    ("077586", "poeticalness", "noun", "/poʊˈɛtɪkəlnəs/", "chất thơ, tính thi ca"),
    ("077587", "poeticise", "verb", "/ˈpoʊɪtɪsaɪz/", "thi vị hóa, làm cho giàu chất thơ"),
    ("077588", "poeticism", "noun", "/ˈpoʊɪtɪsɪzəm/", "từ ngữ thi ca; phong cách chất thơ"),
    ("077589", "poeticize", "verb", "/ˈpoʊɪtɪsaɪz/", "thi vị hóa, làm cho giàu chất thơ"),
    ("077590", "poetise", "verb", "/ˈpoʊɪtaɪz/", "làm thơ, diễn đạt bằng thơ"),
    ("077591", "poetiser", "noun", "/ˈpoʊɪtaɪzər/", "người làm thơ; nhà thơ xoàng"),
    ("077592", "poetize", "verb", "/ˈpoʊɪtaɪz/", "làm thơ, diễn đạt bằng thơ"),
    ("077593", "poetizer", "noun", "/ˈpoʊɪtaɪzər/", "người làm thơ; nhà thơ xoàng"),
    ("077594", "poets", "noun", "/ˈpoʊəts/", "nhà thơ, thi sĩ"),
    ("077595", "pofaced", "adj", "/ˈpoʊˌfeɪst/", "mặt lạnh tanh, giả vờ nghiêm nghị"),
    ("077596", "poge", "noun", "/poʊɡ/", "cà kheo; túi tiền (biến thể cũ)"),
    ("077597", "pogey", "noun", "/ˈpoʊɡi/", "tiền trợ cấp thất nghiệp (Canada)"),
    ("077598", "pogonia", "noun", "/pəˈɡoʊniə/", "chi lan đầm lầy hồng (Pogonia)"),
    ("077599", "pogonion", "noun", "/poʊˈɡoʊniɒn/", "điểm nhô nhất xương cằm (sọ học)"),
    ("077600", "pogonip", "noun", "/ˈpɒɡənɪp/", "sương mù băng giá dày đặc (Tây Mỹ)"),
    ("077601", "pogonology", "noun", "/ˌpoʊɡəˈnɒlədʒi/", "khoa học nghiên cứu về râu"),
    ("077602", "pogonophora", "noun", "/ˌpɒɡəˈnɒfərə/", "ngành Giun râu biển (Pogonophora)"),
]

with open("scratch/b36_r06_raw_p1.json", "r", encoding="utf-8") as f:
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

with open("scratch/b36_r06_p1.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("b36_r06_p1 saved OK")
