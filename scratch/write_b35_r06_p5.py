import json

items = [
    ("072903", "outports", "noun", "/ˈaʊtˌpɔːrts/", "cảng phụ tiền tiêu ngoài cửa biển"),
    ("072904", "panjandrums", "noun", "/pænˈdʒændrəmz/", "người tự cao có thế lực chức sắc"),
    ("072905", "pediculuses", "noun", "/pɪˈdɪkjʊləsɪz/", "chi Chấy rận ký sinh (Pediculus)"),
    ("072906", "phantasmas", "noun", "/fænˈtæzməz/", "bóng ma ảo ảnh trong tâm trí"),
    ("072907", "phenylbutazones", "noun", "/ˌfɛnəlˈbjuːtəˌzoʊnz/", "thuốc kháng viêm phenylbutazone"),
    ("072908", "pickaninnies", "noun", "/ˈpɪkəˌnɪniz/", "từ miệt thị cũ chỉ trẻ da đen (cổ)"),
    ("072909", "pickelhaubes", "noun", "/ˈpɪkəlˌhaʊbəz/", "mũ sắt chóp nhọn quân đội Phổ-Đức"),
    ("072910", "pistacias", "noun", "/pɪˈsteɪʃəz/", "chi Cây hồ trăn (hạt dẻ cười)"),
    ("072911", "polyporuses", "noun", "/pɒˈlɪpərəsɪz/", "chi Nấm lỗ mọc trên gỗ Polyporus"),
    ("072912", "powerbrokers", "noun", "/ˈpaʊərˌbroʊkərz/", "nhân vật giật dây nắm quyền lực"),
    ("072913", "preceptorships", "noun", "/prɪˈsɛptərʃɪps/", "chức vụ người hướng dẫn thực tập"),
    ("072914", "pukus", "noun", "/ˈpuːkuːz/", "linh dương châu Phi sừng vòng puku"),
    ("072915", "rangifers", "noun", "/ˈrændʒɪfərz/", "chi Tuần lộc Bắc Cực (Rangifer)"),
    ("072916", "ratches", "noun", "/ˈrætʃɪz/", "cơ cấu bánh cóc hãm một chiều"),
    ("072917", "ringways", "noun", "/ˈrɪŋˌweɪz/", "đường vành đai bao quanh đô thị"),
    ("072918", "rubberstamped", "verb", "/ˌrʌbərˈstæmpt/", "đã đóng dấu cao su; duyệt cho qua"),
    ("072919", "rubberstamping", "verb", "/ˌrʌbərˈstæmpɪŋ/", "đang đóng dấu; duyệt máy móc"),
    ("072920", "rubberstamps", "verb", "/ˌrʌbərˈstæmps/", "đóng dấu cao su; duyệt thông qua"),
    ("072921", "salvinias", "noun", "/sælˈvɪniəz/", "chi Bèo ong (bèo vảy ốc) Salvinia"),
    ("072922", "schmears", "noun", "/ʃmɪərz/", "lớp phết kem; tiền hối lộ; trọn gói"),
    ("072923", "singhaleses", "noun", "/ˌsɪŋəˈliːz/", "người dân tộc Sinhala Sri Lanka"),
    ("072924", "skirled", "verb", "/skɜːrld/", "đã rít vang tiếng kèn túi Scotland"),
    ("072925", "skirling", "verb", "/ˈskɜːrlɪŋ/", "đang rít vang tiếng kèn túi"),
    ("072926", "skirls", "noun", "/skɜːrlz/", "tiếng rít chói tai của kèn túi"),
    ("072927", "squinching", "verb", "/ˈskwɪntʃɪŋ/", "đang nheo mắt lại; đang co rúm lại"),
    ("072928", "staphylinidaes", "noun", "/ˌstæfɪˈlɪnɪˌdiːz/", "họ Bọ cánh cộc (bọ cánh cứng ngắn)"),
    ("072929", "statices", "noun", "/ˈstætɪsɪz/", "cây hoa bất tử thạch thảo biển"),
    ("072930", "tamarixes", "noun", "/ˈtæmərɪksɪz/", "cây thánh liễu (liễu muối Tamarix)"),
    ("072931", "telophases", "noun", "/ˈtɛləˌfeɪzɪz/", "kỳ cuối quá trình phân bào"),
    ("072932", "testates", "noun", "/ˈtɛsteɪts/", "người để lại di chúc hợp pháp"),
    ("072933", "tetrachloroethylenes", "noun", "/ˌtɛtrəklɔːroʊˈɛθɪliːnz/", "dung môi tẩy khô tetracloetylen"),
    ("072934", "thamnophides", "noun", "/θæmˈnɒfɪˌdiːz/", "chi Rắn sọc vườn Bắc Mỹ Thamnophis"),
    ("072935", "thermopiles", "noun", "/ˈθɜːrməˌpaɪlz/", "cảm biến nhiệt điện (thermopile)"),
    ("072936", "thumbholes", "noun", "/ˈθʌmˌhoʊlz/", "lỗ xỏ ngón tay cái (tay áo, bảng)"),
    ("072937", "timbermans", "noun", "/ˈtɪmbərmənz/", "thợ đốn gỗ; thợ chống lò hầm mỏ"),
    ("072938", "tonicities", "noun", "/toʊˈnɪsɪtiz/", "trương lực cơ; áp suất thẩm thấu"),
    ("072939", "trapas", "noun", "/ˈtræpəz/", "chi Cây củ ấu nước (Trapa)"),
    ("072940", "trichotomies", "noun", "/traɪˈkɒtəmiz/", "phép chia làm ba nhánh hoặc phần"),
    ("072941", "tringas", "noun", "/ˈtrɪŋɡəz/", "chi Chim choắt chân mảnh (Tringa)"),
    ("072942", "tudungs", "noun", "/ˈtuːdʊŋz/", "khăn trùm đầu tudung phụ nữ Mã Lai"),
    ("072943", "ultracentrifuged", "verb", "/ˌʌltrəˈsɛntrɪfjuːdʒd/", "đã tách chiết bằng siêu ly tâm"),
    ("072944", "ultracentrifuges", "noun", "/ˌʌltrəˈsɛntrɪˌfjuːdʒɪz/", "máy siêu ly tâm tốc độ cực cao"),
    ("072945", "ultracentrifuging", "verb", "/ˌʌltrəˈsɛntrɪfjuːdʒɪŋ/", "đang quay tách bằng siêu ly tâm"),
    ("072946", "ultranationalisms", "noun", "/ˌʌltrəˈnæʃənəˌlɪzəmz/", "chủ nghĩa dân tộc cực đoan"),
    ("072947", "understandabilities", "noun", "/ˌʌndərstændəˈbɪlɪtiz/", "tính dễ hiểu rõ ràng minh bạch"),
    ("072948", "unorthodoxies", "noun", "/ʌnˈɔːrθəˌdɒksiz/", "tính chất phi chính thống dị biệt"),
    ("072949", "untrustworthinesses", "noun", "/ʌnˈtrʌstwɜːrðinəsɪz/", "sự thiếu đáng tin cậy bất tín"),
    ("072950", "utrillos", "noun", "/juːˈtrɪloʊz/", "họa sĩ Pháp Maurice Utrillo"),
    ("072951", "vanadates", "noun", "/ˈvænəˌdeɪts/", "muối hóa học vanadat của vanadi"),
    ("072952", "versts", "noun", "/vɜːrsts/", "đơn vị dặm Nga cổ verst (~1,07 km)"),
    ("072953", "vitalists", "noun", "/ˈvaɪtəlɪsts/", "người theo thuyết sinh lực luận"),
    ("072954", "waterscapes", "noun", "/ˈwɔːtərˌskeɪps/", "tranh phong cảnh mặt nước sông biển"),
    ("072955", "whitsuntides", "noun", "/ˈwɪtsənˌtaɪdz/", "tuần lễ Chúa Thánh Thần Hiện Xuống"),
    ("072956", "zooids", "noun", "/ˈzoʊɔɪdz/", "cá thể đơn trong tập đoàn động vật"),
    ("072957", "abducenses", "noun", "/æbˈdjuːsənzɪz/", "dây thần kinh vận nhãn ngoài (VI)"),
    ("072958", "acedias", "noun", "/əˈsiːdiəz/", "sự lười biếng thờ ơ tâm linh"),
    ("072959", "advertized", "verb", "/ˈædvərˌtaɪzd/", "đã quảng cáo (biến thể chính tả)"),
    ("072960", "advertizes", "verb", "/ˈædvərˌtaɪzɪz/", "quảng cáo rao bán (biến thể)"),
    ("072961", "affricates", "noun", "/ˈæfrɪkəts/", "phụ âm tắc xát (ngôn ngữ học)"),
    ("072962", "alarums", "noun", "/əˈlɑːrəmz/", "tiếng chuông báo động hỗn loạn (cổ)"),
    ("072963", "albizias", "noun", "/ælˈbɪziəz/", "cây hợp hoan (cây keo lá me)"),
    ("072964", "albugineas", "noun", "/ˌælbjʊˈdʒɪniəz/", "lớp màng trắng bao tinh hoàn mắt"),
    ("072965", "apomixes", "noun", "/ˌæpəˈmɪksiːz/", "sinh sản vô phối không thụ tinh"),
    ("072966", "apomixises", "noun", "/ˌæpəˈmɪksɪsɪz/", "sinh sản vô phối không thụ tinh"),
    ("072967", "aquanauts", "noun", "/ˈækwəˌnɔːts/", "thợ lặn sống dưới đáy biển sâu"),
    ("072968", "archaebacterias", "noun", "/ˌɑːrkibækˈtɪəriəz/", "nhóm Vi khuẩn cổ sống khắc nghiệt"),
    ("072969", "autoregulations", "noun", "/ˌɔːtoʊrɛɡjʊˈleɪʃənz/", "cơ chế tự điều hòa lưu lượng máu"),
    ("072970", "begetters", "noun", "/bɪˈɡɛtərz/", "người sinh thành; người khởi nguồn"),
    ("072971", "beingnesses", "noun", "/ˈbiːɪŋnəsɪz/", "bản chất tồn tại; sự hiện hữu"),
    ("072972", "boneshakers", "noun", "/ˈboʊnˌʃeɪkərz/", "xe đạp bánh cứng xóc nảy thời xưa"),
    ("072973", "briards", "noun", "/ˈbriːɑːrdz/", "giống chó chăn cừu lông dài Briard"),
    ("072974", "bushbucks", "noun", "/ˈbʊʃˌbʌks/", "linh dương rừng sọc trắng châu Phi"),
    ("072975", "capfuls", "noun", "/ˈkæpˌfʊlz/", "lượng chất lỏng đầy một nắp chai"),
    ("072976", "carbamides", "noun", "/ˈkɑːrbəˌmaɪdz/", "hợp chất hữu cơ urê (carbamid)"),
    ("072977", "cardoons", "noun", "/kɑːrˈduːnz/", "cây actisô dại ăn cuống lá cardoon"),
    ("072978", "centrioles", "noun", "/ˈsɛntriˌoʊlz/", "trung tử trong tế bào động vật"),
    ("072979", "chaffered", "verb", "/ˈtʃæfərd/", "đã mặc cả trả giá kỳ kèo (cổ)"),
    ("072980", "chaffering", "verb", "/ˈtʃæfərɪŋ/", "đang mặc cả trả giá kỳ kèo (cổ)"),
    ("072981", "chaffers", "verb", "/ˈtʃæfərz/", "mặc cả trả giá; tán gẫu vu vơ (cổ)"),
    ("072982", "chiloes", "noun", "/tʃɪˈloʊˌeɪz/", "đảo Chiloé ở miền nam Chile"),
    ("072983", "chrysoprases", "noun", "/ˈkrɪsəˌpreɪzɪz/", "đá quý ngọc lục thạch anh táo"),
    ("072984", "cockleshells", "noun", "/ˈkɒkəlˌʃɛlz/", "vỏ sò tim; thuyền nhỏ mong manh"),
    ("072985", "constantinas", "noun", "/ˌkɒnstənˈtiːnəz/", "hoàng hậu Constantina La Mã"),
    ("072986", "conventicles", "noun", "/kənˈvɛntɪkəlz/", "nhóm họp đạo bí mật trái phép (cổ)"),
    ("072987", "countermoves", "noun", "/ˈkaʊntərˌmuːvz/", "nước cờ đối phó; đòn phản kích"),
    ("072988", "curanderos", "noun", "/ˌkʊərənˈdɛəroʊz/", "thầy lang dân gian châu Mỹ Latinh"),
    ("072989", "dairens", "noun", "/ˈdaɪrənz/", "thành phố cảng Đại Liên (tên cũ)"),
    ("072990", "deerhounds", "noun", "/ˈdɪərˌhaʊndz/", "chó săn hươu cao lớn Scotland"),
    ("072991", "defensibilities", "noun", "/dɪˌfɛnsəˈbɪlɪtiz/", "tính có thể biện hộ bảo vệ được"),
    ("072992", "digitigrades", "noun", "/ˈdɪdʒɪtɪˌɡreɪdz/", "động vật đi bằng đầu ngón chân"),
    ("072993", "dipsomaniacs", "noun", "/ˌdɪpsoʊˈmeɪniæks/", "người mắc chứng cuồng uống rượu"),
    ("072994", "ectasias", "noun", "/ɛkˈteɪʒəz/", "tình trạng giãn nở ống hay mạch"),
    ("072995", "ectomorphs", "noun", "/ˈɛktəˌmɔːrfs/", "người có tạng người gầy mảnh khảnh"),
    ("072996", "endocardia", "noun", "/ˌɛndoʊˈkɑːrdiə/", "màng nội tâm mạc lót buồng tim"),
    ("072997", "erses", "noun", "/ˈɜːrsɪz/", "tiếng Gael Scotland hoặc Ireland"),
    ("072998", "europeanisations", "noun", "/ˌjʊərəpiənaɪˈzeɪʃənz/", "quá trình Âu hóa (cách viết Anh)"),
    ("072999", "excursi", "noun", "/ɛkˈskɜːrsaɪ/", "đoạn bình luận lạc đề; chuyến dạo"),
    ("073000", "flamens", "noun", "/ˈfleɪmɛnz/", "tư tế thờ thần linh La Mã cổ đại"),
    ("073001", "flamines", "noun", "/ˈflæmɪˌniːz/", "tư tế thờ thần linh La Mã cổ đại"),
    ("073002", "fraternisations", "noun", "/ˌfrætərnaɪˈzeɪʃənz/", "sự kết thân thân mật quá mức (Anh)"),
]

with open("scratch/b35_r06_raw_p5.json") as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100
allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}
out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, items):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} != {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} != {hw}"
    assert pos in allowed_pos, f"Bad POS: {pos}"
    assert len(vi) <= 35, f"VI too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA: {hw} -> {ipa}"
    assert not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"Space in IPA: {hw} -> {ipa}"
    out.append({**r, "pos": pos, "ipa": ipa, "vi": vi, "status": "reviewed"})

with open("scratch/b35_r06_p5.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r06_p5.json OK")
