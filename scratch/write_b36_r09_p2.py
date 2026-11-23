import json

records = [
    ("079103", "primage", "noun", "/ˈpraɪmɪdʒ/", "phụ phí bốc dỡ trả thêm cho thuyền"),
    ("079104", "primariness", "noun", "/ˈpraɪˌmɛrinəs/", "tính chất chính yếu, hàng đầu"),
    ("079105", "primateship", "noun", "/ˈpraɪmɪtʃɪp/", "chức tổng giám mục giáo chủ"),
    ("079106", "primatial", "adj", "/praɪˈmeɪʃəl/", "thuộc tổng giám mục giáo chủ"),
    ("079107", "primatical", "adj", "/praɪˈmætɪkəl/", "thuộc tổng giám mục giáo chủ"),
    ("079108", "primatological", "adj", "/ˌpraɪmətəˈlɑːdʒɪkəl/", "thuộc linh trưởng học"),
    ("079109", "primatologist", "noun", "/ˌpraɪməˈtɑːlədʒɪst/", "nhà linh trưởng học"),
    ("079110", "primaxin", "noun", "/praɪˈmæksɪn/", "thuốc kháng sinh imipenem"),
    ("079111", "primely", "adv", "/ˈpraɪmli/", "tuyệt hảo, xuất sắc, hàng đầu"),
    ("079112", "primeness", "noun", "/ˈpraɪmnəs/", "chất lượng hàng đầu; tính nguyên tố"),
    ("079113", "primero", "noun", "/prɪˈmɛroʊ/", "trò đánh bài cổ thế kỷ 16 ở Âu"),
    ("079114", "primers", "noun", "/ˈpraɪmərz/", "sách vỡ lòng; lớp sơn lót; hạt nổ"),
    ("079115", "primerval", "adj", "/praɪˈmɜːrvəl/", "nguyên thủy, thái cổ, ban sơ"),
    ("079116", "primes", "verb", "/praɪmz/", "mồi, khởi động; sơn lót; chuẩn bị"),
    ("079117", "primetide", "noun", "/ˈpraɪmˌtaɪd/", "buổi sáng sớm; tuổi thanh xuân"),
    ("079118", "primeur", "noun", "/priːˈmɜːr/", "nông sản đầu mùa; rượu vang mới"),
    ("079119", "primevally", "adv", "/praɪˈmiːvəli/", "từ thuở nguyên thủy, ban sơ"),
    ("079120", "primigenial", "adj", "/ˌpraɪmɪˈdʒiːniəl/", "đầu tiên, nguyên sinh, ban sơ"),
    ("079121", "primigenious", "adj", "/ˌpraɪmɪˈdʒiːniəs/", "đầu tiên, nguyên thủy, ban sơ"),
    ("079122", "primigenous", "adj", "/praɪˈmɪdʒənəs/", "nguyên thủy, đầu tiên, sơ khai"),
    ("079123", "primigravida", "noun", "/ˌpraɪmɪˈɡrævɪdə/", "sản phụ mang thai con so"),
    ("079124", "primine", "noun", "/ˈpraɪmaɪn/", "vỏ noãn ngoài (thực vật học)"),
    ("079125", "primipara", "noun", "/praɪˈmɪpərə/", "sản phụ đẻ con so lần đầu"),
    ("079126", "primiparae", "noun", "/praɪˈmɪpəˌriː/", "những sản phụ đẻ con so"),
    ("079127", "primiparity", "noun", "/ˌpraɪmɪˈpærəti/", "tình trạng sinh con so (lần đầu)"),
    ("079128", "primiparous", "adj", "/praɪˈmɪpərəs/", "đẻ con so, sinh con lần đầu"),
    ("079129", "primitiae", "noun", "/prɪˈmɪʃiˌiː/", "hoa quả đầu mùa; thu nhập đầu tiên"),
    ("079130", "primitivist", "noun", "/ˈprɪmɪtɪvɪst/", "người theo chủ nghĩa nguyên thủy"),
    ("079131", "primitivity", "noun", "/ˌprɪmɪˈtɪvəti/", "tính nguyên thủy, nét sơ khai"),
    ("079132", "primness", "noun", "/ˈprɪmnəs/", "vẻ câu nệ, tính nghiêm trang quá"),
    ("079133", "primogenial", "adj", "/ˌpraɪməˈdʒiːniəl/", "nguyên thủy, sơ khai; con trưởng"),
    ("079134", "primogenital", "adj", "/ˌpraɪməˈdʒɛnɪtəl/", "thuộc con trưởng, quyền con trưởng"),
    ("079135", "primogenitary", "adj", "/ˌpraɪməˈdʒɛnəˌtɛri/", "thuộc quyền trưởng nam kế tự"),
    ("079136", "primogenitor", "noun", "/ˌpraɪməˈdʒɛnətər/", "tổ tiên trực hệ, thủy tổ"),
    ("079137", "primordia", "noun", "/praɪˈmɔːrdiə/", "các mầm cơ quan sơ khai (sinh học)"),
    ("079138", "primordiality", "noun", "/praɪˌmɔːrdiˈæləti/", "tính nguyên sơ, trạng thái ban đầu"),
    ("079139", "primordializm", "noun", "/praɪˈmɔːrdiəˌlɪzəm/", "chủ nghĩa nguyên thủy (chính trị)"),
    ("079140", "primordially", "adv", "/praɪˈmɔːrdiəli/", "về nguyên thủy, ngay từ ban đầu"),
    ("079141", "primped", "verb", "/prɪmpt/", "đã chải chuốt, đã làm dáng"),
    ("079142", "primps", "verb", "/prɪmps/", "chải chuốt, làm dáng kỹ lưỡng"),
    ("079143", "primrosy", "adj", "/ˈprɪmˌroʊzi/", "đầy hoa anh thảo; vàng nhạt tươi"),
    ("079144", "primulaceae", "noun", "/ˌprɪmjəˈleɪsiː/", "họ Anh thảo (thực vật học)"),
    ("079145", "primulales", "noun", "/ˌprɪmjəˈleɪliːz/", "bộ Anh thảo (thực vật học)"),
    ("079146", "princelet", "noun", "/ˈprɪnslɪt/", "tiểu vương, ông hoàng nhỏ (mỉa mai)"),
    ("079147", "princelets", "noun", "/ˈprɪnslɪts/", "các tiểu vương, ông hoàng nhỏ"),
    ("079148", "princelike", "adj", "/ˈprɪnsˌlaɪk/", "oai vệ như hoàng tử, hào phóng"),
    ("079149", "princeliness", "noun", "/ˈprɪnslinəs/", "vẻ vương giả, sự hào phóng"),
    ("079150", "princelings", "noun", "/ˈprɪnslɪŋz/", "các tiểu vương; thái tử đảng"),
    ("079151", "princeps", "noun", "/ˈprɪnsɛps/", "nguyên thủ La Mã; ấn bản đầu tiên"),
    ("079152", "princeship", "noun", "/ˈprɪnsʃɪp/", "địa vị vương công, tước vị hoàng tử"),
    ("079153", "princesses", "noun", "/ˈprɪnsɛsɪz/", "các nàng công chúa, vương nữ"),
    ("079154", "princewood", "noun", "/ˈprɪnsˌwʊd/", "cây gỗ hoàng tử (vùng Caribe)"),
    ("079155", "principals", "noun", "/ˈprɪnsəpəlz/", "hiệu trưởng; tiền gốc; bên ủy thác"),
    ("079156", "principen", "noun", "/ˈprɪnsəpən/", "thuốc kháng sinh ampicillin"),
    ("079157", "principia", "noun", "/prɪnˈsɪpiə/", "các nguyên lý cơ bản, nguyên tắc"),
    ("079158", "principium", "noun", "/prɪnˈsɪpiəm/", "nguyên lý, khởi nguyên (triết học)"),
    ("079159", "principles", "noun", "/ˈprɪnsəpəlz/", "các nguyên lý, nguyên tắc, đạo lý"),
    ("079160", "prinia", "noun", "/ˈprɪniə/", "chi chim chiền chiện sâu (Prinia)"),
    ("079161", "prinival", "noun", "/ˈprɪnəvəl/", "thuốc hạ huyết áp lisinopril"),
    ("079162", "prinker", "noun", "/ˈprɪŋkər/", "người hay chải chuốt, ăn diện"),
    ("079163", "printability", "noun", "/ˌprɪntəˈbɪləti/", "tính in được, chất lượng khả in"),
    ("079164", "printed", "adj", "/ˈprɪntɪd/", "được in ấn, dạng bản in"),
    ("079165", "printery", "noun", "/ˈprɪntəri/", "nhà in; xưởng in vải hoa"),
    ("079166", "printings", "noun", "/ˈprɪntɪŋz/", "những đợt in, các bản in"),
    ("079167", "printless", "adj", "/ˈprɪntləs/", "không dấu vết; không chữ in"),
    ("079168", "prints", "noun", "/prɪnts/", "bản in; dấu vân; vải hoa in"),
    ("079169", "priodontes", "noun", "/ˌpraɪəˈdɑːntiːz/", "chi tatu khổng lồ (Priodontes)"),
    ("079170", "prionace", "noun", "/praɪˈɑːnəsi/", "chi cá mập xanh (Prionace)"),
    ("079171", "prionotus", "noun", "/ˌpraɪəˈnoʊtəs/", "chi cá chào mào biển (Prionotus)"),
    ("079172", "priorate", "noun", "/ˈpraɪərət/", "chức tu viện phó; tu viện nhỏ"),
    ("079173", "priorities", "noun", "/praɪˈɔːrətiz/", "những ưu tiên, thứ tự ưu tiên"),
    ("079174", "priorly", "adv", "/ˈpraɪərli/", "trước đó, trước kia"),
    ("079175", "priorship", "noun", "/ˈpraɪərʃɪp/", "chức vụ trưởng tu viện phó"),
    ("079176", "priscoan", "noun", "/ˈprɪskoʊən/", "liên đại Hỏa Thành (địa chất)"),
    ("079177", "prised", "verb", "/praɪzd/", "đã cạy ra, đã bẩy lên"),
    ("079178", "prisere", "noun", "/ˈpraɪsɪr/", "diễn thế sinh thái nguyên sinh"),
    ("079179", "prises", "verb", "/ˈpraɪzɪz/", "cạy, bẩy lên (bằng đòn bẩy)"),
    ("079180", "prising", "verb", "/ˈpraɪzɪŋ/", "cạy, bẩy lên (bằng đòn bẩy)"),
    ("079181", "prismatically", "adv", "/prɪzˈmætɪkli/", "theo dạng lăng kính; rực rỡ màu"),
    ("079182", "prismatoid", "noun", "/prɪzˈmætɔɪd/", "hình lăng trụ cụt (hình học)"),
    ("079183", "prismatoidal", "adj", "/ˌprɪzməˈtɔɪdəl/", "có dạng hình lăng trụ cụt"),
    ("079184", "prismoid", "noun", "/ˈprɪzmɔɪd/", "hình lăng trụ cụt đều (hình học)"),
    ("079185", "prismoidal", "adj", "/prɪzˈmɔɪdəl/", "có dạng lăng trụ cụt đều"),
    ("079186", "prismy", "adj", "/ˈprɪzmi/", "như lăng kính; lấp lánh nhiều màu"),
    ("079187", "prisonbreak", "noun", "/ˈprɪzənˌbreɪk/", "cuộc vượt ngục, sự trốn tù"),
    ("079188", "prisoned", "verb", "/ˈprɪzənd/", "đã giam cầm, đã bỏ tù"),
    ("079189", "prisoning", "verb", "/ˈprɪzənɪŋ/", "giam cầm, bỏ tù, giam giữ"),
    ("079190", "prisonlike", "adj", "/ˈprɪzənˌlaɪk/", "như nhà tù, ngột ngạt giam hãm"),
    ("079191", "prisons", "verb", "/ˈprɪzənz/", "giam cầm, bỏ tù, giam giữ"),
    ("079192", "prissily", "adv", "/ˈprɪsɪli/", "một cách kiểu cách, câu nệ"),
    ("079193", "prissiness", "noun", "/ˈprɪsinəs/", "tính kiểu cách, sự quá câu nệ"),
    ("079194", "pristidae", "noun", "/ˈprɪstɪˌdiː/", "họ cá đao (Pristidae)"),
    ("079195", "pristinely", "adv", "/ˈprɪstiːnli/", "vẹn nguyên, tinh khôi ban sơ"),
    ("079196", "pristis", "noun", "/ˈprɪstɪs/", "chi cá đao (Pristis)"),
    ("079197", "prisy", "adj", "/ˈprɪsi/", "kiểu cách, câu nệ, khó tính"),
    ("079198", "prithee", "intj", "/ˈprɪði/", "làm ơn, xin hãy (văn cổ)"),
    ("079199", "pritzelago", "noun", "/ˌprɪtsəˈleɪɡoʊ/", "chi cải núi (Pritzelago)"),
    ("079200", "privacies", "noun", "/ˈpraɪvəsiz/", "sự riêng tư, chốn riêng tư"),
    ("079201", "privat", "noun", "/prɪˈvɑːt/", "lính trơn; đồ vật cá nhân (cổ)"),
    ("079202", "privateering", "noun", "/ˌpraɪvəˈtɪrɪŋ/", "hoạt động tàu lùng tư nhân"),
]

raw = json.load(open("scratch/b36_r09_raw_p2.json"))
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
with open("scratch/b36_r09_p2.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b36_r09_p2 saved OK")
