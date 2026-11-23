import json

records = [
    ("080603", "pusillanimously", "adv", "/ˌpjuːsəˈlænəməsli/", "một cách hèn nhát, nhu nhược"),
    ("080604", "pusillanimousness", "noun", "/ˌpjuːsəˈlænəməsnəs/", "tính hèn nhát, sự nhu nhược yếu hèn"),
    ("080605", "pussley", "noun", "/ˈpʌsli/", "cây rau sam (biến thể khẩu ngữ)"),
    ("080606", "pussly", "noun", "/ˈpʌsli/", "cây rau sam (biến thể khẩu ngữ)"),
    ("080607", "pussyfooted", "verb", "/ˈpʊsiˌfʊtɪd/", "đã đi rón rén; đã lảng tránh vấn đề"),
    ("080608", "pussyfooter", "noun", "/ˈpʊsiˌfʊtər/", "người hay né tránh lập trường"),
    ("080609", "pussyfooting", "verb", "/ˈpʊsiˌfʊtɪŋ/", "rón rén; lảng tránh nêu quan điểm"),
    ("080610", "pussyfoots", "verb", "/ˈpʊsiˌfʊts/", "đi rón rén; né tránh lập trường"),
    ("080611", "pussytoes", "noun", "/ˈpʊsiˌtoʊz/", "cây cúc chân mèo (Antennaria)"),
    ("080612", "pustalate", "verb", "/ˈpʌstʃəˌleɪt/", "nổi mụn mủ, mưng thành mụn mủ"),
    ("080613", "pustulant", "noun", "/ˈpʌstʃələnt/", "chất gây nổi mụn mủ ngoài da"),
    ("080614", "pustular", "adj", "/ˈpʌstʃələr/", "có mụn mủ, dạng mụn mủ (da liễu)"),
    ("080615", "pustulate", "adj", "/ˈpʌstʃəlɪt/", "nổi mụn mủ, có nốt sần giống mụn"),
    ("080616", "pustulation", "noun", "/ˌpʌstʃəˈleɪʃən/", "quá trình nổi mụn mủ trên da"),
    ("080617", "pustulous", "adj", "/ˈpʌstʃələs/", "đầy mụn mủ, nổi nhiều mụn mủ"),
    ("080618", "putage", "noun", "/ˈpjuːtɪdʒ/", "tội thông dâm của phụ nữ (luật cổ)"),
    ("080619", "putamina", "noun", "/pjʊˈteɪmənə/", "các hạch quả cứng, hột quả hạch"),
    ("080620", "putaminous", "adj", "/pjʊˈtæmənəs/", "thuộc hột cứng quả hạch (thực vật)"),
    ("080621", "putatively", "adv", "/ˈpjuːtətɪvli/", "theo như suy đoán, được cho là"),
    ("080622", "putdownable", "adj", "/ˌpʊtˈdaʊnəbəl/", "dễ chán, dễ đặt sách xuống bỏ dở"),
    ("080623", "putinism", "noun", "/ˈpuːtəˌnɪzəm/", "chủ nghĩa Putin (chính trị Nga)"),
    ("080624", "putlog", "noun", "/ˈpʊtˌlɔːɡ/", "thanh gióng ngang giàn giáo"),
    ("080625", "putoff", "noun", "/ˈpʊtˌɔːf/", "lời thoái thác, lý do trì hoãn"),
    ("080626", "putredinous", "adj", "/pjʊˈtrɛdənəs/", "thối rữa, hôi thối, hư hỏng"),
    ("080627", "putrefacient", "adj", "/ˌpjuːtrəˈfeɪʃənt/", "gây thối rữa, làm phân hủy hữu cơ"),
    ("080628", "putrefactive", "adj", "/ˌpjuːtrəˈfæktɪv/", "thuộc sự thối rữa, gây thối rữa"),
    ("080629", "putrefiable", "adj", "/ˌpjuːtrəˈfaɪəbəl/", "dễ bị thối rữa, dễ phân hủy"),
    ("080630", "putrefied", "verb", "/ˈpjuːtrəˌfaɪd/", "đã bị thối rữa, đã phân hủy"),
    ("080631", "putrefies", "verb", "/ˈpjuːtrəˌfaɪz/", "thối rữa, phân hủy; làm hủ bại"),
    ("080632", "putrefying", "verb", "/ˈpjuːtrəˌfaɪɪŋ/", "thối rữa, phân hủy, bốc mùi hôi"),
    ("080633", "putrescible", "adj", "/pjʊˈtrɛsəbəl/", "dễ thối rữa, dễ ôi thiu phân hủy"),
    ("080634", "putridity", "noun", "/pjʊˈtrɪdəti/", "tình trạng thối rữa, mùi hôi thối"),
    ("080635", "putridly", "adv", "/ˈpjuːtrɪdli/", "hôi thối nồng nặc, tồi tệ vô cùng"),
    ("080636", "putridness", "noun", "/ˈpjuːtrɪdnəs/", "sự thối rữa, tính mục nát"),
    ("080637", "putrification", "noun", "/ˌpjuːtrəfəˈkeɪʃən/", "quá trình thối rữa (biến thể)"),
    ("080638", "putrify", "verb", "/ˈpjuːtrəˌfaɪ/", "làm thối rữa, mục nát (biến thể)"),
    ("080639", "puts", "verb", "/pʊts/", "đặt, để; đưa ra; viết ra, diễn đạt"),
    ("080640", "putschist", "noun", "/ˈpʊtʃɪst/", "kẻ tham gia đảo chính bạo loạn"),
    ("080641", "putted", "verb", "/ˈpʌtɪd/", "đã gạt nhẹ bóng vào lỗ (golf)"),
    ("080642", "puttee", "noun", "/ˈpʌti/", "băng xà cạp quấn bắp chân (quân sự)"),
    ("080643", "puttered", "verb", "/ˈpʌtərd/", "đã làm việc lặt vặt, lúi húi"),
    ("080644", "putterer", "noun", "/ˈpʌtərər/", "người làm việc vặt, hay lúi húi"),
    ("080645", "putterers", "noun", "/ˈpʌtərərz/", "những người hay lúi húi làm vặt"),
    ("080646", "puttering", "verb", "/ˈpʌtərɪŋ/", "làm việc lặt vặt, lúi húi thong thả"),
    ("080647", "putters", "verb", "/ˈpʌtərz/", "làm lặt vặt lúi húi; đánh gôn nhẹ"),
    ("080648", "puttie", "noun", "/ˈpʌti/", "xà cạp quấn chân (biến thể cổ)"),
    ("080649", "puttied", "verb", "/ˈpʌtid/", "đã trét mát-tít, đã trám bột trét"),
    ("080650", "putties", "verb", "/ˈpʌtiz/", "trét mát-tít, trám bột trét"),
    ("080651", "puttying", "verb", "/ˈpʌtiɪŋ/", "trét mát-tít, trám kín khe hở"),
    ("080652", "puttyroot", "noun", "/ˈpʌtiˌruːt/", "cây lan củ dính Bắc Mỹ (Aplectrum)"),
    ("080653", "putunghua", "noun", "/ˌpuːtʊŋˈhwɑː/", "tiếng Trung Phổ thông (Putonghua)"),
    ("080654", "puy", "noun", "/pwiː/", "chỏm nón núi lửa tắt ở Pháp"),
    ("080655", "puzzledom", "noun", "/ˈpʌzəldəm/", "tình trạng bối rối, mớ bòng bong"),
    ("080656", "puzzles", "verb", "/ˈpʌzəlz/", "làm bối rối, gây khó hiểu; vắt óc"),
    ("080657", "puzzolan", "noun", "/ˈpʊtsəˌlæn/", "tro núi lửa pozzolan làm xi măng"),
    ("080658", "pvt", "noun", "/ˈpraɪvɪt/", "binh nhì, lính trơn (viết tắt)"),
    ("080659", "pw", "noun", "/ˌpiːˈdʌbəljuː/", "mật khẩu (viết tắt trên mạng)"),
    ("080660", "pyaemia", "noun", "/paɪˈiːmiə/", "nhiễm khuẩn huyết sinh mủ (Anh)"),
    ("080661", "pyaemic", "adj", "/paɪˈiːmɪk/", "thuộc nhiễm khuẩn huyết sinh mủ"),
    ("080662", "pycnanthemum", "noun", "/ˌpɪknænˈθiːməm/", "chi cây bạc hà núi Bắc Mỹ"),
    ("080663", "pycnial", "adj", "/ˈpɪkniəl/", "thuộc túi bào tử phấn gỉ (nấm)"),
    ("080664", "pycnic", "adj", "/ˈpɪknɪk/", "có tạng người thấp đậm, cổ to"),
    ("080665", "pycnid", "noun", "/ˈpɪknɪd/", "thể bình chứa bào tử (nấm học)"),
    ("080666", "pycnidia", "noun", "/pɪkˈnɪdiə/", "các thể bình chứa bào tử (nấm)"),
    ("080667", "pycnidial", "adj", "/pɪkˈnɪdiəl/", "thuộc thể bình bào tử (nấm)"),
    ("080668", "pycnidium", "noun", "/pɪkˈnɪdiəm/", "thể bình sinh bào tử đính (nấm)"),
    ("080669", "pycnodysostosis", "noun", "/ˌpɪknoʊˌdɪsɑːsˈtoʊsɪs/", "bệnh xương hóa đặc di truyền"),
    ("080670", "pycnogonid", "noun", "/pɪkˈnɑːɡənɪd/", "con nhện biển (lớp Pycnogonida)"),
    ("080671", "pycnogonida", "noun", "/ˌpɪknəˈɡɑːnɪdə/", "lớp Nhện biển (chân khớp biển)"),
    ("080672", "pycnomater", "noun", "/pɪkˈnɑːmɪtər/", "bình đo tỷ trọng (biến thể sai chữ)"),
    ("080673", "pycnosis", "noun", "/pɪkˈnoʊsɪs/", "hiện tượng cô đặc nhân tế bào"),
    ("080674", "pycnostyle", "noun", "/ˈpɪknəˌstaɪl/", "hàng cột xếp sát nhau (kiến trúc)"),
    ("080675", "pycnotic", "adj", "/pɪkˈnɑːtɪk/", "thuộc sự cô đặc nhân tế bào"),
    ("080676", "pycnoxylic", "adj", "/ˌpɪknəˈzaɪlɪk/", "có gỗ cứng đặc (thực vật hạt trần)"),
    ("080677", "pyebald", "adj", "/ˈpaɪˌbɔːld/", "lang trắng đen, loang lổ (ngựa)"),
    ("080678", "pyedog", "noun", "/ˈpaɪˌdɔːɡ/", "chó hoang bản địa châu Á (cũ)"),
    ("080679", "pyelitis", "noun", "/ˌpaɪəˈlaɪtɪs/", "bệnh viêm bể thận (y học)"),
    ("080680", "pyelogram", "noun", "/ˈpaɪələˌɡræm/", "phim chụp X-quang bể thận niệu quản"),
    ("080681", "pyelographic", "adj", "/ˌpaɪələˈɡræfɪk/", "thuộc chụp X-quang bể thận"),
    ("080682", "pyelography", "noun", "/ˌpaɪəˈlɑːɡrəfi/", "kỹ thuật chụp X-quang bể thận"),
    ("080683", "pyemia", "noun", "/paɪˈiːmiə/", "bệnh nhiễm khuẩn huyết sinh mủ"),
    ("080684", "pyemic", "adj", "/paɪˈiːmɪk/", "thuộc nhiễm khuẩn huyết sinh mủ"),
    ("080685", "pygal", "adj", "/ˈpaɪɡəl/", "thuộc vùng mông, hậu môn (bò sát)"),
    ("080686", "pygidium", "noun", "/pɪˈdʒɪdiəm/", "mảnh đốt cuối bụng (côn trùng)"),
    ("080687", "pygmaean", "adj", "/pɪɡˈmiːən/", "nhỏ bé như người lùn Pygmy"),
    ("080688", "pygmean", "adj", "/pɪɡˈmiːən/", "bé nhỏ, lùn tịt như người Pygmy"),
    ("080689", "pygmyism", "noun", "/ˈpɪɡmiˌɪzəm/", "chứng còi lùn, tầm vóc nhỏ bé"),
    ("080690", "pygophore", "noun", "/ˈpɪɡəˌfɔːr/", "đốt sinh dục đực (bọ cánh nửa)"),
    ("080691", "pygopodidae", "noun", "/ˌpaɪɡəˈpɑːdɪˌdiː/", "họ Thằn lằn không chân Úc"),
    ("080692", "pygopus", "noun", "/pɪˈɡoʊpəs/", "chi thằn lằn rắn Úc (Pygopus)"),
    ("080693", "pygoscelis", "noun", "/ˌpaɪɡəˈsiːlɪs/", "chi chim cánh cụt Nam Cực"),
    ("080694", "pygostyle", "noun", "/ˈpaɪɡəˌstaɪl/", "xương phao câu (đốt đuôi chim)"),
    ("080695", "pyinma", "noun", "/pɪˈɪnmə/", "cây gỗ bằng lăng nước Myanmar"),
    ("080696", "pyjamas", "noun", "/pəˈdʒɑːməz/", "bộ đồ ngủ pijama (Anh)"),
    ("080697", "pyknic", "adj", "/ˈpɪknɪk/", "có tạng người thấp mập, lưng dày"),
    ("080698", "pyknosis", "noun", "/pɪkˈnoʊsɪs/", "hiện tượng cô đặc nhân tế bào"),
    ("080699", "pyknotic", "adj", "/pɪkˈnɑːtɪk/", "có nhân tế bào bị cô đặc lại"),
    ("080700", "pylodictus", "noun", "/ˌpaɪloʊˈdɪktɪs/", "chi cá trê đầu bẹt Bắc Mỹ"),
    ("080701", "pylorectomy", "noun", "/ˌpaɪləˈrɛktəmi/", "phẫu thuật cắt môn vị dạ dày"),
    ("080702", "pylorrhea", "noun", "/ˌpaɪəˈriːə/", "viêm nha chu chảy mủ (biến thể)"),
]

raw = json.load(open("scratch/b37_r02_raw_p2.json"))
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
with open("scratch/b37_r02_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r02_p2 saved OK")
