import json

RECORDS = [
    ("085003", "saturniidae", "noun", "/ˌsætɜːrˈnaɪɪˌdiː/", "họ Bướm đêm hoàng đế"),
    ("085004", "saturnism", "noun", "/ˈsætərˌnɪzəm/", "chứng nhiễm độc chì"),
    ("085005", "satyriasis", "noun", "/ˌsætəˈraɪəsɪs/", "chứng cuồng dâm nam"),
    ("085006", "satyric", "adj", "/səˈtɪrɪk/", "thuộc thần rừng Satyr; dâm dật"),
    ("085007", "satyridae", "noun", "/səˈtɪrɪˌdiː/", "phân họ Bướm mắt nâu"),
    ("085008", "sauceboat", "noun", "/ˈsɔːsˌboʊt/", "bát rót nước xốt hình thuyền"),
    ("085009", "saucebox", "noun", "/ˈsɔːsˌbɑːks/", "đứa trẻ hỗn xược; người láo xược"),
    ("085010", "sauced", "verb", "/sɔːst/", "đã rưới nước xốt; đã nói hỗn"),
    ("085011", "saucepans", "noun", "/ˈsɔːsˌpænz/", "nồi nhỏ có tay cầm dài"),
    ("085012", "saucepot", "noun", "/ˈsɔːsˌpɑːt/", "nồi nấu xốt hai quai"),
    ("085013", "saucerkraut", "noun", "/ˈsaʊərˌkraʊt/", "dưa cải muối chua kiểu Đức"),
    ("085014", "sauces", "verb", "/ˈsɔːsɪz/", "rưới xốt; nói hỗn xược"),
    ("085015", "saucing", "verb", "/ˈsɔːsɪŋ/", "đang rưới xốt; đang nói hỗn"),
    ("085016", "saucisse", "noun", "/soʊˈsiːs/", "bó cành lấp hào; xúc xích"),
    ("085017", "sauks", "noun", "/sɔːks/", "bộ lạc Sauk (Bắc Mỹ)"),
    ("085018", "saumur", "noun", "/soʊˈmʊr/", "rượu vang Saumur (Pháp)"),
    ("085019", "sauntered", "verb", "/ˈsɔːntərd/", "đã tản bộ thong thả"),
    ("085020", "saunterer", "noun", "/ˈsɔːntərər/", "người đi tản bộ nhàn nhã"),
    ("085021", "sauntering", "verb", "/ˈsɔːntərɪŋ/", "đang tản bộ thong thả"),
    ("085022", "saunters", "verb", "/ˈsɔːntərz/", "tản bộ thong thả"),
    ("085023", "saurischia", "noun", "/sɔːˈrɪskiə/", "bộ Khủng long hông thằn lằn"),
    ("085024", "saurischian", "noun", "/sɔːˈrɪskiən/", "khủng long hông thằn lằn"),
    ("085025", "sauroid", "adj", "/ˈsɔːrɔɪd/", "giống thằn lằn; dạng bò sát"),
    ("085026", "sauromalus", "noun", "/sɔːˈrɑːmələs/", "chi kỳ nhông chuckwalla"),
    ("085027", "sauropoda", "noun", "/sɔːˈrɑːpədə/", "nhánh Khủng long chân thằn lằn"),
    ("085028", "sauropodomorpha", "noun", "/sɔːˌrɑːpədəˈmɔːrfə/", "phân bộ Khủng long cổ dài"),
    ("085029", "sauropterygia", "noun", "/ˌsɔːrɑːptəˈrɪdʒiə/", "siêu bộ Thằn lằn vây biển"),
    ("085030", "saurosuchus", "noun", "/ˌsɔːroʊˈsuːkəs/", "loài bò sát cổ đại Saurosuchus"),
    ("085031", "saururaceae", "noun", "/ˌsɔːrʊəˈreɪsiːˌiː/", "họ Lá giấp (Saururaceae)"),
    ("085032", "saururus", "noun", "/sɔːˈrʊərəs/", "chi cây Đuôi thằn lằn (Saururus)"),
    ("085033", "sausages", "noun", "/ˈsɔːsɪdʒɪz/", "xúc xích; lạp xưởng"),
    ("085034", "saussurea", "noun", "/sɔːˈsjʊəriə/", "chi cây mộc hương Saussurea"),
    ("085035", "savaged", "verb", "/ˈsævɪdʒd/", "đã cắn xé dã man; đã chỉ trích"),
    ("085036", "savages", "verb", "/ˈsævɪdʒɪz/", "cắn xé dã man; chỉ trích gay gắt"),
    ("085037", "savaging", "verb", "/ˈsævɪdʒɪŋ/", "đang cắn xé; đang đả kích"),
    ("085038", "savate", "noun", "/səˈvɑːt/", "môn quyền cước Savate Pháp"),
    ("085039", "saves", "noun", "/seɪvz/", "pha cứu thua (thể thao)"),
    ("085040", "savine", "noun", "/ˈsævɪn/", "cây bách xù độc savin"),
    ("085041", "savinjska", "noun", "/sɑːˈviːnskə/", "vùng Savinja ở Slovenia"),
    ("085042", "savoriness", "noun", "/ˈseɪvərinəs/", "hương vị thơm ngon đậm đà"),
    ("085043", "savorless", "adj", "/ˈseɪvərləs/", "nhạt nhẽo; vô vị"),
    ("085044", "savorlessness", "noun", "/ˈseɪvərləsnəs/", "sự nhạt nhẽo; tính vô vị"),
    ("085045", "savoured", "verb", "/ˈseɪvərd/", "đã thưởng thức; đã nếm kỹ"),
    ("085046", "savourless", "adj", "/ˈseɪvərləs/", "nhạt nhẽo; vô vị"),
    ("085047", "savourlessness", "noun", "/ˈseɪvərləsnəs/", "sự nhạt nhẽo; tính vô vị"),
    ("085048", "savours", "verb", "/ˈseɪvərz/", "thưởng thức; mang hơi hướng"),
    ("085049", "savvied", "verb", "/ˈsævid/", "đã hiểu rõ; đã nắm bắt"),
    ("085050", "savvier", "adj", "/ˈsæviər/", "thông thạo hơn; sành sỏi hơn"),
    ("085051", "savvies", "verb", "/ˈsæviz/", "hiểu rõ; nắm bắt nhanh"),
    ("085052", "savvying", "verb", "/ˈsæviɪŋ/", "đang hiểu rõ; đang nắm bắt"),
    ("085053", "sawbill", "noun", "/ˈsɔːˌbɪl/", "chim vịt mỏ cưa"),
    ("085054", "sawder", "noun", "/ˈsɔːdər/", "lời tâng bốc nịnh hót"),
    ("085055", "sawer", "noun", "/ˈsɔːər/", "thợ cưa gỗ"),
    ("085056", "sawney", "noun", "/ˈsɔːni/", "người khờ khạo; biệt danh Scotland"),
    ("085057", "sawpit", "noun", "/ˈsɔːˌpɪt/", "hố cưa gỗ xẻ cây"),
    ("085058", "sawwort", "noun", "/ˈsɔːˌwɜːrt/", "cây cúc lá răng cưa Serratula"),
    ("085059", "saxatile", "adj", "/ˈsæksəˌtaɪl/", "sống giữa đá; mọc trên đá"),
    ("085060", "saxegothea", "noun", "/ˌsæksəˈɡɑːθiə/", "cây thông Prince Albert (Chile)"),
    ("085061", "saxhorn", "noun", "/ˈsæksˌhɔːrn/", "kèn đồng saxhorn"),
    ("085062", "saxicavous", "adj", "/sækˈsɪkəvəs/", "đục khoét đá (nhuyễn thể)"),
    ("085063", "saxicola", "noun", "/sækˈsɪkələ/", "chi chim sẻ bụi Saxicola"),
    ("085064", "saxicoline", "adj", "/sækˈsɪkəˌlaɪn/", "sống trên đá; mọc trên vách đá"),
    ("085065", "saxicolous", "adj", "/sækˈsɪkələs/", "mọc trên đá; sống giữa đá"),
    ("085066", "saxifragaceae", "noun", "/ˌsæksɪfrəˈɡeɪsiːˌiː/", "họ Tai hùm (Saxifragaceae)"),
    ("085067", "saxist", "noun", "/ˈsæksɪst/", "nghệ sĩ chơi kèn saxophone"),
    ("085068", "saxtuba", "noun", "/ˈsæksˌtuːbə/", "kèn đồng trầm saxtuba"),
    ("085069", "sayanci", "noun", "/səˈjɑːntʃi/", "tiếng Sayanci (Nigeria)"),
    ("085070", "saye", "noun", "/ˌɛsˌeɪˌwaɪˈiː/", "quỹ tiết kiệm mua cổ phiếu (SAYE)"),
    ("085071", "sayeret", "noun", "/səˈjɛrɛt/", "đơn vị trinh sát đặc nhiệm Israel"),
    ("085072", "sayornis", "noun", "/seɪˈɔːrnɪs/", "chi chim đớp ruồi Sayornis"),
    ("085073", "sayyid", "noun", "/ˈsaɪɪd/", "hậu duệ nhà tiên tri; ngài"),
    ("085074", "scabbed", "verb", "/skæbd/", "đã đóng vảy; đã phá công"),
    ("085075", "scabbily", "adv", "/ˈskæbɪli/", "nhếch nhác; hèn hạ đê tiện"),
    ("085076", "scabbiness", "noun", "/ˈskæbinəs/", "tình trạng đóng vảy; sự ghẻ lở"),
    ("085077", "scabbing", "verb", "/ˈskæbɪŋ/", "đang đóng vảy; đang làm thay"),
    ("085078", "scabicide", "noun", "/ˈskeɪbəˌsaɪd/", "thuốc diệt cái ghẻ"),
    ("085079", "scabietic", "adj", "/ˌskeɪbiˈɛtɪk/", "mắc bệnh ghẻ; thuộc bệnh ghẻ"),
    ("085080", "scabrousness", "noun", "/ˈskeɪbrəsnəs/", "bề mặt thô ráp sần sùi"),
    ("085081", "scabs", "verb", "/skæbz/", "đóng vảy; đi làm phá đình công"),
    ("085082", "scaglia", "noun", "/ˈskɑːljə/", "tầng đá vôi đỏ Scaglia (Ý)"),
    ("085083", "scagliola", "noun", "/skælˈjoʊlə/", "vữa thạch cao giả cẩm thạch"),
    ("085084", "scala", "noun", "/ˈskeɪlə/", "thang; bậc; khoang ốc tai"),
    ("085085", "scalage", "noun", "/ˈskeɪlɪdʒ/", "tỷ lệ hao hụt; phép đo gỗ"),
    ("085086", "scalariform", "adj", "/skəˈlærɪˌfɔːrm/", "có dạng hình bậc thang"),
    ("085087", "scalary", "adj", "/ˈskeɪləri/", "có dạng bậc thang"),
    ("085088", "scalded", "verb", "/ˈskɔːldɪd/", "đã làm bỏng nước sôi; đã chần"),
    ("085089", "scalding", "verb", "/ˈskɔːldɪŋ/", "đang làm bỏng; đang chần nước sôi"),
    ("085090", "scalds", "verb", "/skɔːldz/", "làm bỏng nước sôi; chần qua"),
    ("085091", "scalelike", "adj", "/ˈskeɪlˌlaɪk/", "giống vảy cá; dạng vảy"),
    ("085092", "scalenus", "noun", "/skəˈliːnəs/", "cơ bậc thang (vùng cổ)"),
    ("085093", "scales", "verb", "/skeɪlz/", "trèo lên; cạo vảy; cân đo"),
    ("085094", "scaleshape", "adj", "/ˈskeɪlˌʃeɪp/", "hình vảy; dạng bậc thang"),
    ("085095", "scalic", "adj", "/ˈskeɪlɪk/", "thuộc thang âm; thuộc âm giai"),
    ("085096", "scaliform", "adj", "/ˈskeɪlɪˌfɔːrm/", "có dạng bậc thang; dạng vảy"),
    ("085097", "scaliness", "noun", "/ˈskeɪlinəs/", "tình trạng nhiều vảy; sự bong vảy"),
    ("085098", "scall", "noun", "/skɔːl/", "vảy đóng trên da đầu; bệnh chốc"),
    ("085099", "scallawag", "noun", "/ˈskæləˌwæɡ/", "kẻ du côn; đứa trẻ ranh mãnh"),
    ("085100", "scallopine", "noun", "/ˌskæləˈpiːni/", "món thịt lát mỏng áp chảo"),
    ("085101", "scalloping", "verb", "/ˈskɑːləpɪŋ/", "đang cắt viền vỏ sò; bắt điệp"),
    ("085102", "scallops", "verb", "/ˈskɑːləps/", "cắt viền lượn sóng; nướng điệp"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r01_raw_p1.json"))
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

json.dump(out, open("scratch/b38_r01_reviewed_p1.json", "w"), ensure_ascii=False, indent=2)
print("b38_r01_p1 saved OK")
