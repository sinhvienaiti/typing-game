import json

records = [
    ("079203", "privateersman", "noun", "/ˌpraɪvəˈtɪrzmən/", "thủy thủ trên tàu lùng tư nhân"),
    ("079204", "privateness", "noun", "/ˈpraɪvɪtnəs/", "sự riêng tư, tính kín đáo"),
    ("079205", "privatised", "verb", "/ˈpraɪvəˌtaɪzd/", "đã tư nhân hóa, đã cổ phần hóa"),
    ("079206", "privatises", "verb", "/ˈpraɪvəˌtaɪzɪz/", "tư nhân hóa, chuyển sang tư nhân"),
    ("079207", "privatising", "verb", "/ˈpraɪvəˌtaɪzɪŋ/", "tư nhân hóa, chuyển sang tư nhân"),
    ("079208", "privative", "adj", "/ˈprɪvətɪv/", "thiếu vắng, tước đoạt; phủ định"),
    ("079209", "privatively", "adv", "/ˈprɪvətɪvli/", "theo nghĩa phủ định, tước đoạt"),
    ("079210", "privatized", "verb", "/ˈpraɪvəˌtaɪzd/", "đã tư nhân hóa, đã cổ phần hóa"),
    ("079211", "privatizes", "verb", "/ˈpraɪvəˌtaɪzɪz/", "tư nhân hóa, chuyển sang tư nhân"),
    ("079212", "privatizing", "verb", "/ˈpraɪvəˌtaɪzɪŋ/", "tư nhân hóa, chuyển sang tư nhân"),
    ("079213", "privileges", "verb", "/ˈprɪvəlɪdʒɪz/", "ban đặc quyền, ưu đãi, miễn trừ"),
    ("079214", "privileging", "verb", "/ˈprɪvəlɪdʒɪŋ/", "ban đặc quyền, ưu đãi, miễn trừ"),
    ("079215", "privine", "noun", "/ˈpraɪviːn/", "thuốc nhỏ mũi co mạch naphazoline"),
    ("079216", "privity", "noun", "/ˈprɪvəti/", "quan hệ trực tiếp (luật); đồng lõa"),
    ("079217", "prix", "noun", "/priː/", "giải thưởng (Pháp); giá cả"),
    ("079218", "prizable", "adj", "/ˈpraɪzəbəl/", "đáng quý trọng, có giá trị cao"),
    ("079219", "prized", "verb", "/praɪzd/", "đã trân trọng; đã cạy bẩy"),
    ("079220", "prizefighting", "noun", "/ˈpraɪzˌfaɪtɪŋ/", "quyền Anh thi đấu chuyên nghiệp"),
    ("079221", "prizeman", "noun", "/ˈpraɪzmən/", "người đoạt giải thưởng"),
    ("079222", "prizes", "verb", "/ˈpraɪzɪz/", "trân trọng, coi trọng; cạy bẩy"),
    ("079223", "prizing", "verb", "/ˈpraɪzɪŋ/", "trân trọng, coi trọng; cạy bẩy"),
    ("079224", "proa", "noun", "/ˈproʊə/", "thuyền buồm một buồm (Đông Nam Á)"),
    ("079225", "proaccelerin", "noun", "/ˌproʊækˈsɛlərɪn/", "yếu tố đông máu V (proaccelerin)"),
    ("079226", "proala", "noun", "/proʊˈeɪlə/", "mầm cánh trước (côn trùng)"),
    ("079227", "proalar", "adj", "/proʊˈeɪlər/", "thuộc mầm cánh trước (côn trùng)"),
    ("079228", "proam", "noun", "/ˈproʊˌæm/", "giải đấu chuyên nghiệp và nghiệp dư"),
    ("079229", "proangiosperme", "noun", "/ˌproʊændʒiəˈspɜːrmi/", "thực vật tiền hạt kín hóa thạch"),
    ("079230", "probabilist", "noun", "/ˈprɑːbəbəlɪst/", "người theo thuyết xác suất"),
    ("079231", "probabilities", "noun", "/ˌprɑːbəˈbɪlətiz/", "xác suất, khả năng xảy ra"),
    ("079232", "proband", "noun", "/ˈproʊbænd/", "ca chỉ điểm (nghiên cứu di truyền)"),
    ("079233", "probang", "noun", "/ˈproʊbæŋ/", "que thông thực quản (y học)"),
    ("079234", "probangs", "noun", "/ˈproʊbæŋz/", "những que thông thực quản"),
    ("079235", "probational", "adj", "/proʊˈbeɪʃənəl/", "thử việc, thử thách, án treo"),
    ("079236", "probationally", "adv", "/proʊˈbeɪʃənəli/", "theo chế độ thử thách, thử việc"),
    ("079237", "probationers", "noun", "/proʊˈbeɪʃənərz/", "người thử việc; người hưởng án treo"),
    ("079238", "probator", "noun", "/proʊˈbeɪtər/", "người kiểm định; người tố giác (cổ)"),
    ("079239", "probatory", "adj", "/ˈproʊbəˌtɔːri/", "mang tính chứng minh; để thử thách"),
    ("079240", "probed", "verb", "/proʊbd/", "đã thăm dò, đã dò xét kỹ"),
    ("079241", "probes", "verb", "/proʊbz/", "thăm dò, dò xét, điều tra kỹ"),
    ("079242", "probingly", "adv", "/ˈproʊbɪŋli/", "một cách thăm dò, dò xét sâu sắc"),
    ("079243", "problematicalist", "noun", "/ˌprɑːbləmˈætɪkəlɪst/", "người soạn thế cờ (cờ vua)"),
    ("079244", "problematicist", "noun", "/ˌprɑːbləˈmætəsɪst/", "người sáng tác thế cờ (cờ vua)"),
    ("079245", "problematist", "noun", "/ˈprɑːbləmətɪst/", "người sáng tác thế cờ"),
    ("079246", "problemist", "noun", "/ˈprɑːbləmɪst/", "người sáng tác và giải thế cờ"),
    ("079247", "proboscidean", "noun", "/ˌproʊbəˈsɪdiən/", "động vật bộ Vòi (như voi)"),
    ("079248", "proboscidian", "noun", "/ˌproʊbəˈsɪdiən/", "động vật có vòi (bộ Vòi)"),
    ("079249", "proboscidiferous", "adj", "/prəˌbɑːsɪˈdɪfərəs/", "có vòi (động vật học)"),
    ("079250", "proboscidiform", "adj", "/ˌproʊbəˈsɪdɪfɔːrm/", "có dạng hình vòi"),
    ("079251", "probud", "noun", "/ˈproʊbʌd/", "chồi non, nụ sơ khai (thực vật)"),
    ("079252", "procambial", "adj", "/proʊˈkæmbiəl/", "thuộc tiền tầng sinh gỗ (thực vật)"),
    ("079253", "procambium", "noun", "/proʊˈkæmbiəm/", "tiền tầng sinh gỗ (thực vật học)"),
    ("079254", "procarbazine", "noun", "/proʊˈkɑːrbəziːn/", "thuốc trị ung thư procarbazine"),
    ("079255", "procarp", "noun", "/ˈproʊkɑːrp/", "cơ quan sinh sản cái (tảo đỏ)"),
    ("079256", "procartilage", "noun", "/proʊˈkɑːrtəlɪdʒ/", "tiền sụn, mô sụn sơ khai"),
    ("079257", "procaryote", "noun", "/proʊˈkærioʊt/", "sinh vật nhân sơ (chưa có nhân)"),
    ("079258", "procaryotic", "adj", "/ˌproʊkæriˈɑːtɪk/", "thuộc sinh vật nhân sơ"),
    ("079259", "procathedral", "noun", "/ˌproʊkəˈθiːdrəl/", "nhà thờ tạm thay nhà thờ chính tòa"),
    ("079260", "procavia", "noun", "/proʊˈkeɪviə/", "chi đa man đá (Procavia)"),
    ("079261", "procaviidae", "noun", "/ˌproʊkəˈvaɪɪˌdiː/", "họ đa man (Procaviidae)"),
    ("079262", "procedurally", "adv", "/prəˈsiːdʒərəli/", "về mặt thủ tục, theo quy trình"),
    ("079263", "proceeded", "verb", "/prəˈsiːdɪd/", "đã tiến hành, đã đi tiếp"),
    ("079264", "procellaria", "noun", "/ˌprɑːsəˈlɛriə/", "chi hải âu (Procellaria)"),
    ("079265", "procellarian", "adj", "/ˌprɑːsəˈlɛriən/", "thuộc họ chim hải âu"),
    ("079266", "procellariidae", "noun", "/ˌprɑːsəˌlɛriˈaɪɪˌdiː/", "họ chim hải âu lớn"),
    ("079267", "procellariiformes", "noun", "/ˌprɑːsəˌlɛriɪˈfɔːrmiːz/", "bộ Hải âu (chim biển)"),
    ("079268", "procephalic", "adj", "/ˌproʊsəˈfælɪk/", "trước đầu, thuộc phần trước đầu"),
    ("079269", "procercoid", "noun", "/proʊˈsɜːrkɔɪd/", "ấu trùng đuôi móc (sán dây)"),
    ("079270", "procerebrum", "noun", "/ˌproʊsəˈriːbrəm/", "não trước (của động vật chân đốt)"),
    ("079271", "processability", "noun", "/ˌprɑːsɛsəˈbɪləti/", "tính khả gia công, khả năng xử lý"),
    ("079272", "processable", "adj", "/ˈprɑːsɛsəbəl/", "có thể xử lý, gia công được"),
    ("079273", "processer", "noun", "/ˈprɑːsɛsər/", "người chế biến; bộ xử lý"),
    ("079274", "processes", "verb", "/ˈprɑːsɛsɪz/", "xử lý, chế biến, gia công"),
    ("079275", "processibility", "noun", "/ˌprɑːsɛsəˈbɪləti/", "tính khả gia công, khả năng xử lý"),
    ("079276", "processible", "adj", "/ˈprɑːsɛsəbəl/", "có thể xử lý, có thể chế biến"),
    ("079277", "processionally", "adv", "/prəˈsɛʃənəli/", "theo hàng rước, như đám rước"),
    ("079278", "processionary", "adj", "/prəˈsɛʃəˌnɛri/", "đi thành đoàn nối đuôi (sâu bướm)"),
    ("079279", "processioned", "verb", "/prəˈsɛʃənd/", "đã đi rước, đã diễu hành"),
    ("079280", "processioning", "verb", "/prəˈsɛʃənɪŋ/", "diễu hành, đi theo đám rước"),
    ("079281", "processionist", "noun", "/prəˈsɛʃənɪst/", "người tham gia đám rước"),
    ("079282", "processionize", "verb", "/prəˈsɛʃəˌnaɪz/", "tham gia đám rước, diễu hành"),
    ("079283", "processions", "verb", "/prəˈsɛʃənz/", "đi thành đám rước, diễu hành"),
    ("079284", "prochondral", "adj", "/proʊˈkɑːndrəl/", "thuộc tiền sụn, sụn sơ khai"),
    ("079285", "prochromosome", "noun", "/proʊˈkroʊməˌsoʊm/", "tiền nhiễm sắc thể (tế bào học)"),
    ("079286", "prochronism", "noun", "/ˈproʊkrəˌnɪzəm/", "lỗi sai niên đại đặt sớm hơn"),
    ("079287", "procidence", "noun", "/ˈprɑːsɪdəns/", "chứng sa tạng (y học)"),
    ("079288", "prociphilus", "noun", "/proʊˈsɪfələs/", "chi rệp sáp hại cây (Prociphilus)"),
    ("079289", "proclaimation", "noun", "/ˌproʊkləˈmeɪʃən/", "lời tuyên bố, bản công bố (ít dùng)"),
    ("079290", "proclaimer", "noun", "/proʊˈkleɪmər/", "người tuyên bố, người công bố"),
    ("079291", "proclaiming", "verb", "/proʊˈkleɪmɪŋ/", "tuyên bố, công bố, ban bố"),
    ("079292", "proclaims", "verb", "/proʊˈkleɪmz/", "tuyên bố, công bố, ban bố"),
    ("079293", "proclamations", "noun", "/ˌprɑːkləˈmeɪʃənz/", "những bản tuyên cáo, lệnh công bố"),
    ("079294", "proclamatory", "adj", "/proʊˈklæməˌtɔːri/", "mang tính tuyên bố, công bố"),
    ("079295", "proclitic", "adj", "/proʊˈklɪtɪk/", "gắn trước âm tiết sau (ngôn ngữ)"),
    ("079296", "procnias", "noun", "/ˈprɑːkniəs/", "chi chim chuông (Procnias)"),
    ("079297", "procoelous", "adj", "/proʊˈsiːləs/", "lõm trước (đốt sống bò sát)"),
    ("079298", "proconsulate", "noun", "/proʊˈkɑːnsjələt/", "chức tổng đốc La Mã; nhiệm kỳ"),
    ("079299", "proconsulship", "noun", "/proʊˈkɑːnsəlʃɪp/", "chức vụ tổng đốc La Mã"),
    ("079300", "proconvertin", "noun", "/ˌproʊkənˈvɜːrtɪn/", "yếu tố đông máu VII (proconvertin)"),
    ("079301", "procrastinated", "verb", "/prəˈkræstəˌneɪtɪd/", "đã trì hoãn, đã lần lữa"),
    ("079302", "procrastinates", "verb", "/prəˈkræstəˌneɪts/", "trì hoãn, lần lữa, chần chừ"),
]

raw = json.load(open("scratch/b36_r09_raw_p3.json"))
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
with open("scratch/b36_r09_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b36_r09_p3 saved OK")
