import json

RECORDS = [
    ("085803", "sectionalization", "noun", "/ˌsɛkʃənəlaɪˈzeɪʃən/", "sự phân chia khu vực; tính cục bộ"),
    ("085804", "sectionalize", "verb", "/ˈsɛkʃənəˌlaɪz/", "phân chia thành từng khu vực"),
    ("085805", "sectionally", "adv", "/ˈsɛkʃənəli/", "theo từng đoạn; theo từng khu vực"),
    ("085806", "sectioning", "verb", "/ˈsɛkʃənɪŋ/", "đang cắt lát; đang phân khu vực"),
    ("085807", "sections", "verb", "/ˈsɛkʃənz/", "cắt lát mỏng; chia thành từng phần"),
    ("085808", "sectoral", "adj", "/ˈsɛktərəl/", "thuộc ngành kinh tế; hình quạt"),
    ("085809", "sectral", "noun", "/ˈsɛktrəl/", "thuốc chẹn beta Sectral trị cao áp"),
    ("085810", "secularise", "verb", "/ˈsɛkjələˌraɪz/", "thế tục hóa; tách khỏi tôn giáo"),
    ("085811", "secularised", "verb", "/ˈsɛkjələˌraɪzd/", "đã thế tục hóa"),
    ("085812", "secularises", "verb", "/ˈsɛkjələˌraɪzɪz/", "thế tục hóa"),
    ("085813", "secularising", "verb", "/ˈsɛkjələˌraɪzɪŋ/", "đang thế tục hóa"),
    ("085814", "secularity", "noun", "/ˌsɛkjəˈlærɪti/", "tính thế tục; đời sống trần tục"),
    ("085815", "secularized", "verb", "/ˈsɛkjələˌraɪzd/", "đã thế tục hóa"),
    ("085816", "secularizes", "verb", "/ˈsɛkjələˌraɪzɪz/", "thế tục hóa"),
    ("085817", "secularizing", "verb", "/ˈsɛkjələˌraɪzɪŋ/", "đang thế tục hóa"),
    ("085818", "secularly", "adv", "/ˈsɛkjələrli/", "theo cách thế tục; hàng thế kỷ"),
    ("085819", "secund", "adj", "/ˈsiːkənd/", "mọc quay về một phía (thực vật)"),
    ("085820", "secundigravida", "noun", "/sɪˌkʌndɪˈɡrævɪdə/", "sản phụ mang thai lần thứ hai"),
    ("085821", "secundine", "noun", "/ˈsɛkənˌdaɪn/", "màng bọc trong noãn thực vật"),
    ("085822", "securable", "adj", "/sɪˈkjʊrəbəl/", "có thể bảo đảm; có thể đạt được"),
    ("085823", "secured", "verb", "/sɪˈkjʊrd/", "đã bảo đảm; đã cố định chắc"),
    ("085824", "secureness", "noun", "/sɪˈkjʊrnəs/", "sự an toàn; cảm giác yên tâm"),
    ("085825", "securer", "noun", "/sɪˈkjʊrər/", "người bảo vệ; người giành được"),
    ("085826", "secures", "verb", "/sɪˈkjʊrz/", "bảo đảm; cố định chắc; giành được"),
    ("085827", "securiform", "adj", "/sɪˈkjʊrɪˌfɔːrm/", "có hình lưỡi rìu"),
    ("085828", "securing", "verb", "/sɪˈkjʊrɪŋ/", "đang bảo đảm; đang cố định chắc"),
    ("085829", "securities", "noun", "/sɪˈkjʊrɪtiz/", "chứng khoán; cổ phiếu trái phiếu"),
    ("085830", "securitization", "noun", "/sɪˌkjʊrɪtəˈzeɪʃən/", "chứng khoán hóa tài sản nợ"),
    ("085831", "sedateness", "noun", "/sɪˈdeɪtnəs/", "vẻ điềm tĩnh; phong thái ung dung"),
    ("085832", "sedatives", "noun", "/ˈsɛdətɪvz/", "thuốc an thần; chất làm dịu"),
    ("085833", "sedecuple", "noun", "/sɪˈdɛkjʊpəl/", "lượng gấp mười sáu lần"),
    ("085834", "sedentarily", "adv", "/ˌsɛdənˈtɛrəli/", "tĩnh tại; ít vận động đi lại"),
    ("085835", "sedentariness", "noun", "/ˌsɛdənˈtɛrinəs/", "lối sống ít vận động; tính định cư"),
    ("085836", "sederunt", "noun", "/sɪˈdɛrənt/", "phiên họp kéo dài (Scotland)"),
    ("085837", "sedgelike", "adj", "/ˈsɛdʒˌlaɪk/", "giống cây cói; giống cây lác"),
    ("085838", "sedgy", "adj", "/ˈsɛdʒi/", "mọc đầy cói lác"),
    ("085839", "sedilia", "noun", "/sɪˈdɪliə/", "bộ ghế đá xây cho giáo sĩ ngồi"),
    ("085840", "sedimentologic", "adj", "/ˌsɛdəməntəˈlɑːdʒɪk/", "thuộc trầm tích học"),
    ("085841", "sedimentologicaly", "adv", "/ˌsɛdəˌmɛntəˈlɑːdʒɪkli/", "về mặt trầm tích học"),
    ("085842", "sedimentologist", "noun", "/ˌsɛdəmənˈtɑːlədʒɪst/", "nhà trầm tích học"),
    ("085843", "sedimentology", "noun", "/ˌsɛdəmənˈtɑːlədʒi/", "ngành trầm tích học"),
    ("085844", "sedimentometer", "noun", "/ˌsɛdəmənˈtɑːmɪtər/", "máy đo tốc độ lắng hạt"),
    ("085845", "seditionary", "adj", "/sɪˈdɪʃəˌnɛri/", "kích động nổi loạn lật đổ"),
    ("085846", "seditiously", "adv", "/sɪˈdɪʃəsli/", "mang tính xúi giục nổi loạn"),
    ("085847", "seditiousness", "noun", "/sɪˈdɪʃəsnəs/", "tính chất kích động nổi loạn"),
    ("085848", "seduced", "verb", "/sɪˈduːst/", "đã quyến rũ; đã dụ dỗ"),
    ("085849", "seducement", "noun", "/sɪˈduːsmənt/", "sự quyến rũ; sự cám dỗ"),
    ("085850", "seduces", "verb", "/sɪˈduːsɪz/", "quyến rũ; dụ dỗ; lôi cuốn"),
    ("085851", "seducible", "adj", "/sɪˈduːsəbəl/", "dễ bị quyến rũ; dễ xiêu lòng"),
    ("085852", "seducing", "verb", "/sɪˈduːsɪŋ/", "đang quyến rũ; đang dụ dỗ"),
    ("085853", "seductiveness", "noun", "/sɪˈdʌktɪvnəs/", "sự quyến rũ mê hoặc"),
    ("085854", "sedulity", "noun", "/sɪˈduːlɪti/", "tính cần mẫn; sự siêng năng"),
    ("085855", "sedulous", "adj", "/ˈsɛdʒələs/", "siêng năng; cần cù; kiên trì"),
    ("085856", "sedulousness", "noun", "/ˈsɛdʒələsnəs/", "sự siêng năng cần mẫn"),
    ("085857", "seedage", "noun", "/ˈsiːdɪdʒ/", "sự nhân giống bằng hạt"),
    ("085858", "seedcake", "noun", "/ˈsiːdˌkeɪk/", "bánh ngọt nướng tẩm hạt gia vị"),
    ("085859", "seedcase", "noun", "/ˈsiːdˌkeɪs/", "vỏ quả chứa hạt; bao hạt"),
    ("085860", "seedful", "adj", "/ˈsiːdfəl/", "nhiều hạt; sai hạt"),
    ("085861", "seedily", "adv", "/ˈsiːdɪli/", "nhếch nhác; tồi tàn; uể oải"),
    ("085862", "seeding", "verb", "/ˈsiːdɪŋ/", "đang gieo hạt; đang xếp hạt giống"),
    ("085863", "seedman", "noun", "/ˈsiːdmən/", "người buôn hạt giống cây trồng"),
    ("085864", "seeds", "verb", "/siːdz/", "gieo hạt; tách bỏ hạt; phân hạt"),
    ("085865", "seedstalk", "noun", "/ˈsiːdˌstɔːk/", "cuống hoa mang hạt"),
    ("085866", "seemed", "verb", "/siːmd/", "đã dường như; đã có vẻ như"),
    ("085867", "seemliness", "noun", "/ˈsiːmlinəs/", "sự đúng mực đoan trang"),
    ("085868", "seems", "verb", "/siːmz/", "dường như; có vẻ như"),
    ("085869", "seen", "verb", "/siːn/", "đã nhìn thấy; đã gặp; đã hiểu"),
    ("085870", "seeped", "verb", "/siːpt/", "đã rỉ ra; đã thấm qua"),
    ("085871", "seeps", "verb", "/siːps/", "rỉ ra; thấm chậm qua"),
    ("085872", "seeres", "noun", "/ˈsiːərɪs/", "nữ tiên tri; bà đồng bói toán"),
    ("085873", "sees", "verb", "/siːz/", "nhìn thấy; hiểu ra; gặp gỡ"),
    ("085874", "seesawed", "verb", "/ˈsiːˌsɔːd/", "đã chơi bập bênh; dao động qua lại"[:35]),
    ("085875", "seesawing", "verb", "/ˈsiːˌsɔːɪŋ/", "đang bập bênh; đang dao động"),
    ("085876", "seesaws", "verb", "/ˈsiːˌsɔːz/", "chơi bập bênh; dao động lên xuống"),
    ("085877", "seethed", "verb", "/siːðd/", "đã sôi sùng sục; đã sôi sục giận"),
    ("085878", "seethes", "verb", "/siːðz/", "sôi sùng sục; giận sôi lên"),
    ("085879", "segar", "noun", "/sɪˈɡɑːr/", "điếu xì gà (cách viết cổ)"),
    ("085880", "segmentary", "adj", "/ˈsɛɡmənˌtɛri/", "chia thành từng đốt hay đoạn"),
    ("085881", "segmenting", "verb", "/ˈsɛɡmɛntɪŋ/", "đang phân đoạn; đang tách khúc"),
    ("085882", "segments", "verb", "/ˈsɛɡmɛnts/", "phân đoạn; tách thành từng khúc"),
    ("085883", "segregates", "verb", "/ˈsɛɡrɪˌɡeɪts/", "tách riêng; phân biệt đối xử"),
    ("085884", "segregating", "verb", "/ˈsɛɡrɪˌɡeɪtɪŋ/", "đang tách riêng; đang phân biệt"),
    ("085885", "segregationism", "noun", "/ˌsɛɡrɪˈɡeɪʃəˌnɪzəm/", "chủ nghĩa phân biệt chủng tộc"),
    ("085886", "segregative", "adj", "/ˈsɛɡrɪˌɡeɪtɪv/", "có tính tách riêng hay phân ly"),
    ("085887", "segregator", "noun", "/ˈsɛɡrɪˌɡeɪtər/", "máy phân loại; người phân tách"),
    ("085888", "seicento", "noun", "/seɪˈtʃɛntoʊ/", "thế kỷ 17 trong nghệ thuật Ý"),
    ("085889", "seigneurial", "adj", "/seɪnˈjʊriəl/", "thuộc lãnh chúa phong kiến"),
    ("085890", "seigneury", "noun", "/ˈseɪnjəri/", "lãnh địa phong kiến"),
    ("085891", "seignior", "noun", "/ˈseɪnjər/", "lãnh chúa phong kiến; quý ngài"),
    ("085892", "seigniorial", "adj", "/seɪnˈjɔːriəl/", "thuộc lãnh chúa phong kiến"),
    ("085893", "seignorage", "noun", "/ˈseɪnjərɪdʒ/", "lợi nhuận đúc tiền; phí đúc tiền"),
    ("085894", "seined", "verb", "/seɪnd/", "đã đánh cá bằng lưới vây kéo"),
    ("085895", "seiner", "noun", "/ˈseɪnər/", "thuyền đánh cá lưới vây"),
    ("085896", "seines", "verb", "/seɪnz/", "đánh cá bằng lưới vây kéo"),
    ("085897", "seining", "verb", "/ˈseɪnɪŋ/", "đang đánh cá bằng lưới vây kéo"),
    ("085898", "seise", "verb", "/siːz/", "trao quyền sở hữu bất động sản"),
    ("085899", "seisin", "noun", "/ˈsiːzɪn/", "quyền chiếm hữu đất đai hợp pháp"),
    ("085900", "seism", "noun", "/ˈsaɪzəm/", "trận động đất; sự chấn động đất"),
    ("085901", "seismal", "adj", "/ˈsaɪzməl/", "thuộc địa chấn; gây động đất"),
    ("085902", "seismism", "noun", "/ˈsaɪzˌmɪzəm/", "hoạt động địa chấn"),
]

# Remove slice at 085874 cleanly <= 35
RECORDS[71] = ("085874", "seesawed", "verb", "/ˈsiːˌsɔːd/", "đã chơi bập bênh; dao động lại")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r02_raw_p4.json"))
by_id = {r["id"].split(".")[-1]: r for r in raw}
out = []
for sid, hw, pos, ipa, vi in RECORDS:
    rec = dict(by_id[sid])
    assert rec["hw"] == hw, (sid, hw, rec["hw"])
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

json.dump(out, open("scratch/b38_r02_reviewed_p4.json", "w"), ensure_ascii=False, indent=2)
print("b38_r02_p4 saved OK")
