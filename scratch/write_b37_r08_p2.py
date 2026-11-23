import json

RECORDS = [
    ("083603", "rhapsodically", "adv", "/ræpˈsɑːdɪkəli/", "dạt dào cảm xúc; đầy say mê"),
    ("083604", "rhapsodise", "verb", "/ˈræpsəˌdaɪz/", "ca ngợi nồng nhiệt; ngâm sử thi"),
    ("083605", "rhapsodised", "verb", "/ˈræpsəˌdaɪzd/", "đã ca ngợi nồng nhiệt"),
    ("083606", "rhapsodises", "verb", "/ˈræpsəˌdaɪzɪz/", "ca ngợi nồng nhiệt"),
    ("083607", "rhapsodising", "verb", "/ˈræpsəˌdaɪzɪŋ/", "đang ca ngợi nồng nhiệt"),
    ("083608", "rhapsodist", "noun", "/ˈræpsədɪst/", "người ngâm sử thi; người ca tụng"),
    ("083609", "rhapsodized", "verb", "/ˈræpsəˌdaɪzd/", "đã nói với nhiệt tình dạt dào"),
    ("083610", "rhapsodizes", "verb", "/ˈræpsəˌdaɪzɪz/", "nói với nhiệt tình dạt dào"),
    ("083611", "rhapsodizing", "verb", "/ˈræpsəˌdaɪzɪŋ/", "đang nói với nhiệt tình dạt dào"),
    ("083612", "rheidae", "noun", "/ˈriːɪˌdiː/", "họ Đà điểu Nam Mỹ"),
    ("083613", "rheiformes", "noun", "/ˌriːɪˈfɔːrmiːz/", "bộ Đà điểu Nam Mỹ"),
    ("083614", "rhematic", "adj", "/rɪˈmætɪk/", "thuộc cấu tạo từ; thuộc vị từ"),
    ("083615", "rheme", "noun", "/riːm/", "thuyết ngữ; phần thuật"),
    ("083616", "rheobase", "noun", "/ˈriːəˌbeɪs/", "dòng điện ngưỡng kích thích"),
    ("083617", "rheobiotic", "adj", "/ˌriːoʊbaɪˈɑːtɪk/", "sống ở dòng nước chảy"),
    ("083618", "rheologic", "adj", "/ˌriːəˈlɑːdʒɪk/", "thuộc lưu biến học"),
    ("083619", "rheometers", "noun", "/riˈɑːmɪtərz/", "lưu biến kế; máy đo độ nhớt"),
    ("083620", "rheometry", "noun", "/riˈɑːmətri/", "phép đo lưu biến"),
    ("083621", "rheostats", "noun", "/ˈriːəˌstæts/", "biến trở"),
    ("083622", "rheotaxis", "noun", "/ˌriːoʊˈtæksɪs/", "tính hướng dòng chảy"),
    ("083623", "rheotropic", "adj", "/ˌriːoʊˈtrɑːpɪk/", "hướng dòng chảy"),
    ("083624", "rhetor", "noun", "/ˈriːtər/", "bậc thầy tu từ học; nhà hùng biện"),
    ("083625", "rhetoricians", "noun", "/ˌrɛtəˈrɪʃənz/", "nhà tu từ học; nhà hùng biện"),
    ("083626", "rheumaticky", "adj", "/ruːˈmætɪki/", "mắc bệnh thấp khớp"),
    ("083627", "rhexia", "noun", "/ˈrɛksiə/", "chi cỏ hoa Rhexia"),
    ("083628", "rhibhus", "noun", "/ˈrɪbuːz/", "các thần thợ thủ công Ấn Độ"),
    ("083629", "rhinal", "adj", "/ˈraɪnəl/", "thuộc mũi"),
    ("083630", "rhincodon", "noun", "/ˈrɪŋkəˌdɑːn/", "chi cá nhám voi"),
    ("083631", "rhincodontidae", "noun", "/ˌrɪŋkoʊˈdɑːntɪˌdiː/", "họ Cá nhám voi"),
    ("083632", "rhinecephalon", "noun", "/ˌraɪnəˈsɛfəˌlɑːn/", "não khứu giác"),
    ("083633", "rhinencephalon", "noun", "/ˌraɪnənˈsɛfəˌlɑːn/", "não khứu giác"),
    ("083634", "rhinion", "noun", "/ˈrɪniən/", "điểm mũi (nhân trắc học)"),
    ("083635", "rhinobatidae", "noun", "/ˌraɪnoʊˈbætɪˌdiː/", "họ Cá đuối đàn"),
    ("083636", "rhinocerotidae", "noun", "/ˌraɪnəsəˈrɑːtɪˌdiː/", "họ Tê giác"),
    ("083637", "rhinolaryngologist", "noun", "/ˌraɪnoʊˌlærɪŋˈɡɑːlədʒɪst/", "bác sĩ chuyên khoa mũi họng"),
    ("083638", "rhinolaryngology", "noun", "/ˌraɪnoʊˌlærɪŋˈɡɑːlədʒi/", "mũi họng học"),
    ("083639", "rhinology", "noun", "/raɪˈnɑːlədʒi/", "khoa bệnh mũi"),
    ("083640", "rhinolophidae", "noun", "/ˌraɪnoʊˈlɑːfɪˌdiː/", "họ Dơi lá mũi"),
    ("083641", "rhinonicteris", "noun", "/ˌraɪnoʊˈnɪktərɪs/", "chi Dơi mũi quả cam"),
    ("083642", "rhinopathy", "noun", "/raɪˈnɑːpəθi/", "bệnh ở mũi"),
    ("083643", "rhinopharyngeal", "adj", "/ˌraɪnoʊfəˈrɪndʒiəl/", "thuộc mũi hầu"),
    ("083644", "rhinopharyngitis", "noun", "/ˌraɪnoʊˌfærɪnˈdʒaɪtɪs/", "viêm mũi họng"),
    ("083645", "rhinopharyns", "noun", "/ˌraɪnoʊˈfærɪŋks/", "tỵ hầu; mũi hầu"),
    ("083646", "rhinophore", "noun", "/ˈraɪnəˌfɔːr/", "xúc tu khứu giác (sên biển)"),
    ("083647", "rhinophyma", "noun", "/ˌraɪnoʊˈfaɪmə/", "bệnh mũi sư tử; phì đại mũi"),
    ("083648", "rhinoptera", "noun", "/raɪˈnɑːptərə/", "chi Cá ó (Rhinoptera)"),
    ("083649", "rhinoreaction", "noun", "/ˌraɪnoʊriˈækʃən/", "phản ứng niêm mạc mũi"),
    ("083650", "rhinoscope", "noun", "/ˈraɪnəˌskoʊp/", "đèn soi mũi"),
    ("083651", "rhinoscopy", "noun", "/raɪˈnɑːskəpi/", "phép soi mũi"),
    ("083652", "rhinosporidiosis", "noun", "/ˌraɪnoʊspəˌrɪdiˈoʊsɪs/", "bệnh nấm mũi rhinosporidiosis"),
    ("083653", "rhinostenosis", "noun", "/ˌraɪnoʊstəˈnoʊsɪs/", "hẹp lỗ mũi; nghẹt mũi"),
    ("083654", "rhinotermitidae", "noun", "/ˌraɪnoʊtɜːrˈmɪtɪˌdiː/", "họ Mối đất (Rhinotermitidae)"),
    ("083655", "rhinotomy", "noun", "/raɪˈnɑːtəmi/", "thủ thuật rạch mũi"),
    ("083656", "rhinotracheitis", "noun", "/ˌraɪnoʊˌtreɪkiˈaɪtɪs/", "viêm mũi khí quản"),
    ("083657", "rhipsalis", "noun", "/rɪpˈseɪlɪs/", "chi Xương rồng rủ (Rhipsalis)"),
    ("083658", "rhiptoglossa", "noun", "/ˌrɪptəˈɡlɑːsə/", "phân bộ Tắc kè hoa"),
    ("083659", "rhizanthous", "adj", "/raɪˈzænθəs/", "có hoa mọc từ rễ"),
    ("083660", "rhizobia", "noun", "/raɪˈzoʊbiə/", "vi khuẩn nốt rễ cây họ đậu"),
    ("083661", "rhizobiaceae", "noun", "/raɪˌzoʊbiˈeɪsiːˌiː/", "họ vi khuẩn Rhizobiaceae"),
    ("083662", "rhizobial", "adj", "/raɪˈzoʊbiəl/", "thuộc vi khuẩn nốt rễ"),
    ("083663", "rhizocarp", "noun", "/ˈraɪzəˌkɑːrp/", "cây cỏ sống nhiều năm"),
    ("083664", "rhizocarpous", "adj", "/ˌraɪzəˈkɑːrpəs/", "có rễ sống nhiều năm"),
    ("083665", "rhizocephalan", "noun", "/ˌraɪzəˈsɛfələn/", "giáp xác ký sinh đầu rễ"),
    ("083666", "rhizoctinia", "noun", "/ˌraɪzɑːkˈtɪniə/", "chi nấm gây thối rễ"),
    ("083667", "rhizogenesis", "noun", "/ˌraɪzəˈdʒɛnəsɪs/", "sự hình thành rễ"),
    ("083668", "rhizoid", "noun", "/ˈraɪzɔɪd/", "rễ giả"),
    ("083669", "rhizoidal", "adj", "/ˌraɪˈzɔɪdəl/", "thuộc rễ giả"),
    ("083670", "rhizomorph", "noun", "/ˈraɪzəˌmɔːrf/", "sợi nấm dạng rễ"),
    ("083671", "rhizomorphous", "adj", "/ˌraɪzəˈmɔːrfəs/", "có dạng rễ"),
    ("083672", "rhizophoraceae", "noun", "/ˌraɪzəfəˈreɪsiːˌiː/", "họ Đước (Rhizophoraceae)"),
    ("083673", "rhizopod", "noun", "/ˈraɪzəˌpɑːd/", "động vật chân giả"),
    ("083674", "rhizopoda", "noun", "/raɪˈzɑːpədə/", "lớp Chân giả (Rhizopoda)"),
    ("083675", "rhizopodan", "noun", "/raɪˈzɑːpədən/", "động vật nguyên sinh chân giả"),
    ("083676", "rhizopodium", "noun", "/ˌraɪzəˈpoʊdiəm/", "chân giả; chân rễ"),
    ("083677", "rhizopogon", "noun", "/ˌraɪzəˈpoʊɡɑːn/", "chi nấm củ ngầm Rhizopogon"),
    ("083678", "rhizopogonaceae", "noun", "/ˌraɪzəˌpoʊɡəˈneɪsiːˌiː/", "họ nấm củ ngầm Rhizopogonaceae"),
    ("083679", "rhizosphere", "noun", "/ˈraɪzəˌsfɪr/", "vùng rễ; tầng đất quanh rễ"),
    ("083680", "rhizotaxis", "noun", "/ˌraɪzəˈtæksɪs/", "sự phân bố hệ rễ"),
    ("083681", "rhodamine", "noun", "/ˈroʊdəˌmiːn/", "chất nhuộm huỳnh quang rhodamin"),
    ("083682", "rhodanthe", "noun", "/roʊˈdænθi/", "hoa cúc bất tử Úc"),
    ("083683", "rhodolite", "noun", "/ˈroʊdəˌlaɪt/", "đá ngọc hồng lựu tím hồng"),
    ("083684", "rhodomontade", "noun", "/ˌrɑːdəmɑːnˈteɪd/", "lời nói khoác lác; ba hoa"),
    ("083685", "rhodophyceae", "noun", "/ˌroʊdoʊˈfaɪsiːˌiː/", "lớp Tảo đỏ"),
    ("083686", "rhodosphaera", "noun", "/ˌroʊdəˈsfɪrə/", "chi cây Rhodosphaera Úc"),
    ("083687", "rhodymenia", "noun", "/ˌroʊdɪˈmiːniə/", "chi rong đỏ Rhodymenia"),
    ("083688", "rhodymeniaceae", "noun", "/ˌroʊdɪˌmiːniˈeɪsiːˌiː/", "họ rong đỏ Rhodymeniaceae"),
    ("083689", "rhoeadales", "noun", "/ˌriːəˈdeɪliːz/", "bộ Thuốc phiện cũ (Rhoeadales)"),
    ("083690", "rhombi", "noun", "/ˈrɑːmbaɪ/", "hình thoi"),
    ("083691", "rhombohedron", "noun", "/ˌrɑːmbəˈhiːdrən/", "khối mặt thoi"),
    ("083692", "rhonchus", "noun", "/ˈrɑːŋkəs/", "tiếng ran ngáy (phổi)"),
    ("083693", "rhotacise", "verb", "/ˈroʊtəˌsaɪz/", "phát âm nặng âm r"),
    ("083694", "rhotacism", "noun", "/ˈroʊtəˌsɪzəm/", "sự phát âm rung quá âm r"),
    ("083695", "rhotacize", "verb", "/ˈroʊtəˌsaɪz/", "phát âm nặng âm r"),
    ("083696", "rhyacotriton", "noun", "/ˌraɪəkəˈtraɪtɑːn/", "chi kỳ giông suối Tây Bắc Mỹ"),
    ("083697", "rhymeless", "adj", "/ˈraɪmləs/", "không có vần"),
    ("083698", "rhymes", "verb", "/raɪmz/", "gieo vần; hợp vần với"),
    ("083699", "rhynchocephalia", "noun", "/ˌrɪŋkoʊsəˈfeɪliə/", "bộ Đầu mỏ (bò sát)"),
    ("083700", "rhynchoelaps", "noun", "/ˌrɪŋkoʊˈiːlæps/", "chi rắn san hô Úc"),
    ("083701", "rhynchophoran", "noun", "/rɪŋˈkɑːfərən/", "bọ vòi voi; bọ dừa"),
    ("083702", "rhyncostylis", "noun", "/ˌrɪŋkoʊˈstaɪlɪs/", "chi lan ngọc điểm (Rhynchostylis)"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b37_r08_raw_p2.json"))
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

json.dump(out, open("scratch/b37_r08_reviewed_p2.json", "w"), ensure_ascii=False, indent=2)
print("b37_r08_p2 saved OK")
