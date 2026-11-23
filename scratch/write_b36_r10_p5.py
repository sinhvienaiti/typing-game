import json

records = [
    ("079903", "protomorphic", "adj", "/ˌproʊtəˈmɔːrfɪk/", "có hình thái nguyên thủy, sơ khai"),
    ("079904", "protomorphous", "adj", "/ˌproʊtəˈmɔːrfəs/", "có dạng nguyên thủy, dạng gốc"),
    ("079905", "protonate", "verb", "/ˈproʊtəˌneɪt/", "gắn thêm proton (hóa học)"),
    ("079906", "protonema", "noun", "/ˌproʊtəˈniːmə/", "tản sợi non (giai đoạn đầu rêu)"),
    ("079907", "protonemata", "noun", "/ˌproʊtəˈniːmətə/", "các tản sợi non (của cây rêu)"),
    ("079908", "protonematoid", "adj", "/ˌproʊtəˈnɛməˌtɔɪd/", "có dạng tản sợi non (rêu)"),
    ("079909", "protonephridia", "noun", "/ˌproʊtoʊnəˈfrɪdiə/", "các nguyên đơn thận (giun dẹp)"),
    ("079910", "protonephridial", "adj", "/ˌproʊtoʊnəˈfrɪdiəl/", "thuộc nguyên đơn thận"),
    ("079911", "protonephridium", "noun", "/ˌproʊtoʊnəˈfrɪdiəm/", "nguyên đơn thận (cơ quan bài tiết)"),
    ("079912", "protoneurone", "noun", "/ˌproʊtoʊˈnʊroʊn/", "tế bào thần kinh đơn cực sơ khai"),
    ("079913", "protonic", "adj", "/proʊˈtɑːnɪk/", "thuộc hạt proton (vật lý)"),
    ("079914", "protonotary", "noun", "/ˌproʊtəˈnoʊtəri/", "chánh lục sự tòa án; chưởng ấn"),
    ("079915", "protons", "noun", "/ˈproʊtɑːnz/", "các hạt proton (vật lý hạt nhân)"),
    ("079916", "protopathic", "adj", "/ˌproʊtəˈpæθɪk/", "cảm giác thô sơ (đau, nóng lạnh)"),
    ("079917", "protopepsia", "noun", "/ˌproʊtəˈpɛpsiə/", "quá trình tiêu hóa đầu ở dạ dày"),
    ("079918", "protoperithecium", "noun", "/ˌproʊtoʊˌpɛrɪˈθiːʃəm/", "thể quả túi sơ khai (nấm)"),
    ("079919", "protophyte", "noun", "/ˈproʊtəˌfaɪt/", "thực vật đơn bào nguyên thủy"),
    ("079920", "protoplasmatic", "adj", "/ˌproʊtəplæzˈmætɪk/", "thuộc chất nguyên sinh tế bào"),
    ("079921", "protoplasmic", "adj", "/ˌproʊtəˈplæzmɪk/", "thuộc chất nguyên sinh tế bào"),
    ("079922", "protoplastic", "adj", "/ˌproʊtəˈplæstɪk/", "thuộc nguyên sinh chất; nguyên thủy"),
    ("079923", "protopod", "noun", "/ˈproʊtəˌpɑːd/", "đốt gốc phần phụ (giáp xác)"),
    ("079924", "protostar", "noun", "/ˈproʊtəˌstɑːr/", "tiền sao (giai đoạn hình thành sao)"),
    ("079925", "protostele", "noun", "/ˈproʊtəˌstiːl/", "trụ dẫn nguyên thủy (thực vật)"),
    ("079926", "prototheria", "noun", "/ˌproʊtəˈθɪriə/", "phân lớp Thú huyệt (thú đẻ trứng)"),
    ("079927", "prototherian", "noun", "/ˌproʊtəˈθɪriən/", "loài thú huyệt (như thú mỏ vịt)"),
    ("079928", "prototroph", "noun", "/ˈproʊtəˌtrɑːf/", "sinh vật tự dưỡng nguyên thủy"),
    ("079929", "prototypes", "noun", "/ˈproʊtəˌtaɪps/", "các nguyên mẫu, bản mẫu thử nghiệm"),
    ("079930", "protozoic", "adj", "/ˌproʊtəˈzoʊɪk/", "thuộc động vật nguyên sinh"),
    ("079931", "protozoological", "adj", "/ˌproʊtəˌzoʊəˈlɑːdʒɪkəl/", "thuộc động vật nguyên sinh học"),
    ("079932", "protozoologist", "noun", "/ˌproʊtəzoʊˈɑːlədʒɪst/", "nhà nghiên cứu động vật đơn bào"),
    ("079933", "protozoon", "noun", "/ˌproʊtəˈzoʊɑːn/", "động vật nguyên sinh đơn bào"),
    ("079934", "protractedly", "adv", "/prəˈtræktɪdli/", "kéo dài lê thê, dây dưa"),
    ("079935", "protractedness", "noun", "/prəˈtræktɪdnəs/", "sự kéo dài lê thê, sự dây dưa"),
    ("079936", "protractible", "adj", "/prəˈtræktəbəl/", "có thể thò ra, vươn dài ra được"),
    ("079937", "protractile", "adj", "/proʊˈtræktəl/", "có thể thò ra thụt vào (lưỡi, móng)"),
    ("079938", "protractility", "noun", "/ˌproʊtrækˈtɪləti/", "khả năng thò ra thụt vào được"),
    ("079939", "protracting", "verb", "/prəˈtræktɪŋ/", "kéo dài ra, làm dây dưa lâu"),
    ("079940", "protractions", "noun", "/prəˈtrækʃənz/", "sự kéo dài thời gian; sự đưa ra"),
    ("079941", "protractive", "adj", "/prəˈtræktɪv/", "kéo dài thời gian, gây chậm trễ"),
    ("079942", "protracts", "verb", "/prəˈtrækts/", "kéo dài thời gian, làm dây dưa"),
    ("079943", "protriptyline", "noun", "/proʊˈtrɪptəˌliːn/", "thuốc chống trầm cảm protriptyline"),
    ("079944", "protrophic", "adj", "/proʊˈtrɑːfɪk/", "tự dưỡng chất vô cơ (sinh học)"),
    ("079945", "protropin", "noun", "/ˈproʊtrəpɪn/", "hormone tăng trưởng somatrem"),
    ("079946", "protruded", "verb", "/prəˈtruːdɪd/", "đã nhô ra, đã lồi ra ngoài"),
    ("079947", "protrudes", "verb", "/prəˈtruːdz/", "nhô ra, lồi ra, thò ra ngoài"),
    ("079948", "protrusible", "adj", "/proʊˈtruːsəbəl/", "có thể thò ra, nhô ra được"),
    ("079949", "protrusile", "adj", "/proʊˈtruːsəl/", "có thể thò ra, nhô ra ngoài"),
    ("079950", "protrusility", "noun", "/prəˌtruːsəˈlɪti/", "khả năng thò ra ngoài được"),
    ("079951", "protrusively", "adv", "/prəˈtruːsɪvli/", "theo kiểu nhô ra, lộ rõ ra"),
    ("079952", "protrusiveness", "noun", "/prəˈtruːsɪvnəs/", "tính chất nhô ra, lồi ra ngoài"),
    ("079953", "protuberantly", "adv", "/prəˈtuːbərəntli/", "theo cách lồi ra, phình to ra"),
    ("079954", "protuberate", "verb", "/prəˈtuːbəˌreɪt/", "lồi ra, nhô ra, phồng lên"),
    ("079955", "protura", "noun", "/prəˈtjʊrə/", "bộ Nguyên vĩ (côn trùng không cánh)"),
    ("079956", "proturan", "noun", "/prəˈtjʊrən/", "loài sâu nguyên vĩ (không mắt cánh)"),
    ("079957", "proudling", "noun", "/ˈpraʊdlɪŋ/", "kẻ ngạo mạn, người kiêu căng"),
    ("079958", "proudness", "noun", "/ˈpraʊdnəs/", "niềm kiêu hãnh, sự tự hào"),
    ("079959", "prov", "noun", "/prɑːv/", "viết tắt của tỉnh, khu vực"),
    ("079960", "provableness", "noun", "/ˈpruːvəbəlnəs/", "tính có thể chứng minh được"),
    ("079961", "provenly", "adv", "/ˈpruːvənli/", "một cách đã được chứng minh"),
    ("079962", "proventriculusz", "noun", "/ˌproʊvɛnˈtrɪkjələs/", "dạ dày tuyến (chim); mề côn trùng"),
    ("079963", "prover", "noun", "/ˈpruːvər/", "người chứng minh; máy kiểm định"),
    ("079964", "proverbialism", "noun", "/prəˈvɜːrbiəˌlɪzəm/", "lối nói tục ngữ, thành ngữ cổ"),
    ("079965", "proverbialist", "noun", "/prəˈvɜːrbiəlɪst/", "người sưu tầm hoặc hay dùng tục ngữ"),
    ("079966", "proves", "verb", "/pruːvz/", "chứng minh; tỏ ra là, hóa ra là"),
    ("079967", "proviant", "noun", "/ˈproʊviənt/", "lương thực tiếp tế quân đội (cổ)"),
    ("079968", "provicative", "adj", "/prəˈvɑːkətɪv/", "khiêu khích, kích động (ít dùng)"),
    ("079969", "provided", "verb", "/prəˈvaɪdɪd/", "đã cung cấp, đã chu cấp, trang bị"),
    ("079970", "providently", "adv", "/ˈprɑːvɪdəntli/", "biết lo xa, có tính dự phòng"),
    ("079971", "provides", "verb", "/prəˈvaɪdz/", "cung cấp, chu cấp; quy định (luật)"),
    ("079972", "providing", "verb", "/prəˈvaɪdɪŋ/", "cung cấp, chu cấp; miễn là"),
    ("079973", "provinces", "noun", "/ˈprɑːvɪnsɪz/", "các tỉnh; vùng nông thôn; lĩnh vực"),
    ("079974", "provincialist", "noun", "/prəˈvɪnʃəlɪst/", "người có tư tưởng cục bộ địa phương"),
    ("079975", "provinciality", "noun", "/prəˌvɪnʃiˈæləti/", "tính chất tỉnh lẻ, tầm nhìn hạn hẹp"),
    ("079976", "provincialization", "noun", "/prəˌvɪnʃələˈzeɪʃən/", "sự địa phương hóa thành tỉnh lẻ"),
    ("079977", "provincialize", "verb", "/prəˈvɪnʃəˌlaɪz/", "làm mang tính địa phương, tỉnh lẻ"),
    ("079978", "provine", "verb", "/proʊˈvaɪn/", "chiết cành nho, giâm cành nho"),
    ("079979", "proving", "verb", "/ˈpruːvɪŋ/", "chứng minh, thử nghiệm; hóa ra là"),
    ("079980", "provisionality", "noun", "/prəˌvɪʒəˈnæləti/", "tính chất tạm thời, lâm thời"),
    ("079981", "provisionalness", "noun", "/prəˈvɪʒənəlnəs/", "tính chất tạm thời, chưa chính thức"),
    ("079982", "provisionary", "adj", "/prəˈvɪʒəˌnɛri/", "tạm thời, lâm thời, dự kiến"),
    ("079983", "provisioned", "verb", "/prəˈvɪʒənd/", "đã tiếp tế, đã cung cấp lương thực"),
    ("079984", "provisioning", "verb", "/prəˈvɪʒənɪŋ/", "tiếp tế, cung cấp lương thực phẩm"),
    ("079985", "provisionless", "adj", "/prəˈvɪʒənləs/", "không có lương thực dự trữ"),
    ("079986", "provisionment", "noun", "/prəˈvɪʒənmənt/", "việc tiếp tế lương thực phẩm"),
    ("079987", "provisor", "noun", "/prəˈvaɪzər/", "người quản lý lương thực; giám thị"),
    ("079988", "provocations", "noun", "/ˌprɑːvəˈkeɪʃənz/", "những hành vi khiêu khích, chọc tức"),
    ("079989", "provocativeness", "noun", "/prəˈvɑːkətɪvnəs/", "tính chất khiêu khích, sự khêu gợi"),
    ("079990", "provokes", "verb", "/prəˈvoʊks/", "khiêu khích, chọc tức; gây ra"),
    ("079991", "provokingly", "adv", "/prəˈvoʊkɪŋli/", "một cách khiêu khích, trêu ngươi"),
    ("079992", "provosts", "noun", "/ˈproʊvoʊsts/", "hiệu trưởng; chánh cảnh sát quân sự"),
    ("079993", "provostship", "noun", "/ˈproʊvoʊstʃɪp/", "chức hiệu trưởng; chức thị trưởng"),
    ("079994", "prowfish", "noun", "/ˈpraʊˌfɪʃ/", "cá mũi tàu (Zaprora silenus)"),
    ("079995", "prowled", "verb", "/praʊld/", "đã rình mò, đã đi lại lén lút"),
    ("079996", "prowling", "verb", "/ˈpraʊlɪŋ/", "rình mò, lảng vảng săn mồi"),
    ("079997", "prowls", "verb", "/praʊlz/", "rình mò, lảng vảng đi săn mồi"),
    ("079998", "proxies", "noun", "/ˈprɑːksiz/", "người ủy quyền; máy chủ trung gian"),
    ("079999", "proximad", "adv", "/ˈprɑːksɪˌmæd/", "hướng về phía gần tâm (giải phẫu)"),
    ("080000", "proximally", "adv", "/ˈprɑːksɪməli/", "ở phía gần gốc, gần tâm (giải phẫu)"),
    ("080001", "proximately", "adv", "/ˈprɑːksəmətli/", "ngay gần, xấp xỉ, trực tiếp"),
    ("080002", "proximateness", "noun", "/ˈprɑːksəmətnəs/", "sự gần gũi trực tiếp, tính cận kề"),
]

raw = json.load(open("scratch/b36_r10_raw_p5.json"))
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
with open("scratch/b36_r10_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b36_r10_p5 saved OK")
