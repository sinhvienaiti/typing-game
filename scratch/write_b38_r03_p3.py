import json

RECORDS = [
    ("086203", "sequestrated", "verb", "/ˈsiːkwɪˌstreɪtɪd/", "đã cô lập; đã kê biên tài sản"),
    ("086204", "sequestrates", "verb", "/ˈsiːkwɪˌstreɪts/", "cô lập; kê biên tài sản"),
    ("086205", "sequestrating", "verb", "/ˈsiːkwɪˌstreɪtɪŋ/", "đang cô lập; đang kê biên tài sản"),
    ("086206", "sequestrator", "noun", "/ˈsiːkwɪˌstreɪtər/", "người giữ tài sản bị kê biên"),
    ("086207", "sequestrectomy", "noun", "/ˌsiːkwɪˈstrɛktəmi/", "phẫu thuật lấy mảnh xương chết"),
    ("086208", "sequestrotomy", "noun", "/ˌsiːkwɪˈstrɑːtəmi/", "phẫu thuật mở lấy mảnh xương chết"),
    ("086209", "sequestrum", "noun", "/sɪˈkwɛstrəm/", "mảnh xương chết tách khỏi xương lành"),
    ("086210", "sequoiadendron", "noun", "/sɪˌkwɔɪəˈdɛndrən/", "chi Cù tùng khổng lồ"),
    ("086211", "sequoya", "noun", "/sɪˈkwɔɪə/", "cây tùng bách khổng lồ; Sequoyah"),
    ("086212", "ser", "noun", "/sɪr/", "đơn vị cân cổ Ấn Độ ser; loạt"),
    ("086213", "sera", "noun", "/ˈsɪrə/", "huyết thanh; thanh dịch"),
    ("086214", "serai", "noun", "/səˈraɪ/", "quán trọ đoàn lữ hành vùng Trung Á"),
    ("086215", "seral", "adj", "/ˈsɪrəl/", "thuộc chuỗi diễn thế sinh thái"),
    ("086216", "serang", "noun", "/səˈræŋ/", "đốc công thủy thủ tàu châu Á"),
    ("086217", "seraphical", "adj", "/səˈræfɪkəl/", "thanh cao như thiên thần Seraph"),
    ("086218", "seraphim", "noun", "/ˈsɛrəfɪm/", "lục dực thiên thần Seraph"),
    ("086219", "seraphine", "noun", "/ˈsɛrəˌfiːn/", "đàn phím hơi cổ seraphine"),
    ("086220", "seraskier", "noun", "/səˈræskɪr/", "tổng tư lệnh quân đội Ottoman xưa"),
    ("086221", "serax", "noun", "/ˈsɛræks/", "thuốc an thần Serax (oxazepam)"),
    ("086222", "serdica", "noun", "/ˈsɜːrdɪkə/", "tên cổ đại của thủ đô Sofia"),
    ("086223", "serein", "noun", "/səˈreɪn/", "cơn mưa bụi lúc trời quang mây"),
    ("086224", "serekunda", "noun", "/ˌsɛrəˈkʊndə/", "thành phố Serrekunda (Gambia)"),
    ("086225", "serenaded", "verb", "/ˌsɛrəˈneɪdɪd/", "đã hát tình ca dưới cửa sổ"),
    ("086226", "serenader", "noun", "/ˌsɛrəˈneɪdər/", "người hát tình ca ban đêm"),
    ("086227", "serenades", "verb", "/ˌsɛrəˈneɪdz/", "hát tình ca tặng dưới cửa sổ"),
    ("086228", "serenading", "verb", "/ˌsɛrəˈneɪdɪŋ/", "đang hát tình ca tặng ban đêm"),
    ("086229", "serenata", "noun", "/ˌsɛrəˈnɑːtə/", "khúc dạ nhạc thanh nhạc Ý"),
    ("086230", "serened", "verb", "/səˈriːnd/", "đã làm thanh bình; đã lắng dịu"),
    ("086231", "serenes", "verb", "/səˈriːnz/", "làm thanh bình; lắng dịu lại"),
    ("086232", "sereness", "noun", "/ˈsɪrnəs/", "sự khô héo; tình trạng héo úa"),
    ("086233", "serenify", "verb", "/səˈrɛnəˌfaɪ/", "làm cho thanh bình yên ả"),
    ("086234", "serening", "verb", "/səˈriːnɪŋ/", "đang làm thanh bình; lắng dịu"),
    ("086235", "serenoa", "noun", "/ˌsɛrəˈnoʊə/", "chi cây cọ lùn Serenoa"),
    ("086236", "serfage", "noun", "/ˈsɜːrfɪdʒ/", "chế độ nông nô; thân phận nông nô"),
    ("086237", "serfhood", "noun", "/ˈsɜːrfˌhʊd/", "thân phận nông nô"),
    ("086238", "serflike", "adj", "/ˈsɜːrfˌlaɪk/", "khúm núm phục dịch như nông nô"),
    ("086239", "sergeancy", "noun", "/ˈsɑːrdʒənsi/", "chức trung sĩ; cấp bậc trung sĩ"),
    ("086240", "sergeantship", "noun", "/ˈsɑːrdʒəntˌʃɪp/", "chức vụ trung sĩ"),
    ("086241", "sergette", "noun", "/sɜːrˈdʒɛt/", "vải len chéo mỏng"),
    ("086242", "sergt", "noun", "/ˈsɑːrdʒənt/", "trung sĩ (viết tắt)"),
    ("086243", "serialise", "verb", "/ˈsɪriəˌlaɪz/", "sắp xếp nối tiếp; đăng nhiều kỳ"),
    ("086244", "serialist", "noun", "/ˈsɪriəlɪst/", "tác giả viết truyện đăng nhiều kỳ"),
    ("086245", "serialists", "noun", "/ˈsɪriəlɪsts/", "tác giả viết truyện nhiều kỳ"),
    ("086246", "serialized", "verb", "/ˈsɪriəˌlaɪzd/", "đã đăng nhiều kỳ; đã tuần tự hóa"),
    ("086247", "serializes", "verb", "/ˈsɪriəˌlaɪzɪz/", "đăng nhiều kỳ; tuần tự hóa dữ liệu"),
    ("086248", "serializing", "verb", "/ˈsɪriəˌlaɪzɪŋ/", "đang đăng nhiều kỳ; tuần tự hóa"),
    ("086249", "seriate", "adj", "/ˈsɪriˌeɪt/", "xếp thành dãy liên tiếp"),
    ("086250", "seriated", "adj", "/ˈsɪriˌeɪtɪd/", "được xếp theo hàng nối tiếp"),
    ("086251", "seriation", "noun", "/ˌsɪriˈeɪʃən/", "sự sắp xếp theo chuỗi thứ tự"),
    ("086252", "seric", "adj", "/ˈsɪrɪk/", "thuộc Trung Hoa cổ; bằng tơ lụa"),
    ("086253", "sericeous", "adj", "/sɪˈrɪʃəs/", "mịn như lụa; có lông tơ mịn"),
    ("086254", "sericicultural", "adj", "/ˌsɛrɪsɪˈkʌltʃərəl/", "thuộc nghề trồng dâu nuôi tằm"),
    ("086255", "sericiculture", "noun", "/ˌsɛrɪsɪˈkʌltʃər/", "nghề trồng dâu nuôi tằm"),
    ("086256", "sericiculturist", "noun", "/ˌsɛrɪsɪˈkʌltʃərɪst/", "người nuôi tằm lấy tơ"),
    ("086257", "sericious", "adj", "/sɪˈrɪʃəs/", "mềm mượt như tơ lụa"),
    ("086258", "sericocarpus", "noun", "/ˌsɛrɪkoʊˈkɑːrpəs/", "chi cúc trắng Sericocarpus"),
    ("086259", "sericterium", "noun", "/ˌsɛrɪkˈtɪriəm/", "tuyến tơ (sâu tằm, nhện)"),
    ("086260", "serictery", "noun", "/sɪˈrɪktəri/", "tuyến tiết tơ của sâu tằm"),
    ("086261", "sericultural", "adj", "/ˌsɛrɪˈkʌltʃərəl/", "thuộc nghề nuôi tằm"),
    ("086262", "sericulturist", "noun", "/ˌsɛrɪˈkʌltʃərɪst/", "người làm nghề nuôi tằm"),
    ("086263", "seriema", "noun", "/ˌsɛriˈeɪmə/", "chim chân dài seriema Nam Mỹ"),
    ("086264", "serific", "adj", "/sɪˈrɪfɪk/", "nhả tơ; sinh ra sợi tơ"),
    ("086265", "seringa", "noun", "/səˈrɪŋɡə/", "cây cao su vùng Amazon; hoa nhài giả"),
    ("086266", "serinus", "noun", "/səˈraɪnəs/", "chi chim yến hót Serinus"),
    ("086267", "seriocomedy", "noun", "/ˌsɪrioʊˈkɑːmədi/", "bi hài kịch; hài kịch pha chính kịch"),
    ("086268", "seriocomical", "adj", "/ˌsɪrioʊˈkɑːmɪkəl/", "nửa đùa nửa thật; bi hài"),
    ("086269", "seriola", "noun", "/səˈraɪələ/", "chi cá cam biển Seriola"),
    ("086270", "serioso", "adv", "/ˌsɛriˈoʊsoʊ/", "trang nghiêm đứng đắn (âm nhạc)"),
    ("086271", "seriousnesses", "noun", "/ˈsɪriəsnəsɪz/", "mức độ nghiêm trọng; sự đứng đắn"),
    ("086272", "seriph", "noun", "/ˈsɛrɪf/", "nét chân chữ (phông chữ serif)"),
    ("086273", "seriphidium", "noun", "/ˌsɛrɪˈfɪdiəm/", "chi ngải bạc Seriphidium"),
    ("086274", "seriphus", "noun", "/səˈraɪfəs/", "chi cá đù nữ hoàng Seriphus"),
    ("086275", "sermoned", "verb", "/ˈsɜːrmənd/", "đã thuyết giáo; đã lên lớp dạy đời"),
    ("086276", "sermonette", "noun", "/ˌsɜːrməˈnɛt/", "bài thuyết giáo ngắn"),
    ("086277", "sermoning", "verb", "/ˈsɜːrmənɪŋ/", "đang thuyết giáo; đang dạy đời"),
    ("086278", "sermonise", "verb", "/ˈsɜːrməˌnaɪz/", "thuyết giáo; lên mặt dạy đời"),
    ("086279", "sermoniser", "noun", "/ˈsɜːrməˌnaɪzər/", "người hay giảng đạo lý"),
    ("086280", "sermonize", "verb", "/ˈsɜːrməˌnaɪz/", "thuyết giáo; lên mặt dạy đời"),
    ("086281", "sermonized", "verb", "/ˈsɜːrməˌnaɪzd/", "đã thuyết giáo; đã lên lớp dạy đời"),
    ("086282", "sermonizer", "noun", "/ˈsɜːrməˌnaɪzər/", "người hay giảng đạo lý"),
    ("086283", "sermonizes", "verb", "/ˈsɜːrməˌnaɪzɪz/", "thuyết giáo; lên mặt dạy đời"),
    ("086284", "sermonizing", "verb", "/ˈsɜːrməˌnaɪzɪŋ/", "đang thuyết giáo; đang dạy đời"),
    ("086285", "sermons", "verb", "/ˈsɜːrmənz/", "thuyết giáo; giảng đạo"),
    ("086286", "serologist", "noun", "/sɪˈrɑːlədʒɪst/", "nhà huyết thanh học"),
    ("086287", "seropurulent", "adj", "/ˌsɪroʊˈpjʊrələnt/", "lẫn huyết thanh và dịch mủ"),
    ("086288", "seroreaction", "noun", "/ˌsɪroʊriˈækʃən/", "phản ứng huyết thanh chẩn đoán"),
    ("086289", "serosal", "adj", "/sɪˈroʊsəl/", "thuộc thanh mạc"),
    ("086290", "serosity", "noun", "/sɪˈrɑːsɪti/", "thanh dịch; tính loãng như huyết thanh"),
    ("086291", "serotherapy", "noun", "/ˌsɪroʊˈθɛrəpi/", "liệu pháp tiêm huyết thanh"),
    ("086292", "serotinal", "adj", "/sɪˈrɑːtənəl/", "nở muộn cuối mùa hạ"),
    ("086293", "serotine", "noun", "/ˈsɛrəˌtaɪn/", "dơi nâu châu Âu Eptesicus"),
    ("086294", "serotinous", "adj", "/sɪˈrɑːtənəs/", "nở muộn; mở quả muộn sau cháy"),
    ("086295", "serotype", "noun", "/ˈsɪrəˌtaɪp/", "kiểu huyết thanh (vi sinh vật)"),
    ("086296", "serovaccination", "noun", "/ˌsɪroʊˌvæksəˈneɪʃən/", "tiêm phối hợp huyết thanh vắc-xin"),
    ("086297", "serpasil", "noun", "/ˈsɜːrpəsɪl/", "thuốc hạ huyết áp Serpasil"),
    ("086298", "serpentiform", "adj", "/sɜːrˈpɛntɪˌfɔːrm/", "có hình dạng ngoằn ngoèo như rắn"),
    ("086299", "serpentines", "noun", "/ˈsɜːrpənˌtiːnz/", "đường uốn khúc; đá xà vân"),
    ("086300", "serpentlike", "adj", "/ˈsɜːrpəntˌlaɪk/", "ngoằn ngoèo như rắn; xảo quyệt"),
    ("086301", "serpiginous", "adj", "/sɜːrˈpɪdʒənəs/", "lan ngoằn ngoèo trên da (vết loét)"),
    ("086302", "serpigo", "noun", "/sɜːrˈpaɪɡoʊ/", "bệnh hắc lào lan bò trên da"),
]

# Shorten any entries > 35 chars cleanly
RECORDS[6] = ("086209", "sequestrum", "noun", "/sɪˈkwɛstrəm/", "mảnh xương chết tách rời")
RECORDS[44] = ("086247", "serializes", "verb", "/ˈsɪriəˌlaɪzɪz/", "đăng nhiều kỳ; tuần tự hóa")
RECORDS[62] = ("086265", "seringa", "noun", "/səˈrɪŋɡə/", "cây cao su Amazon; hoa nhài tây")
RECORDS[64] = ("086267", "seriocomedy", "noun", "/ˌsɪrioʊˈkɑːmədi/", "bi hài kịch")
RECORDS[87] = ("086290", "serosity", "noun", "/sɪˈrɑːsɪti/", "thanh dịch; dịch huyết thanh")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r03_raw_p3.json"))
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

json.dump(out, open("scratch/b38_r03_reviewed_p3.json", "w"), ensure_ascii=False, indent=2)
print("b38_r03_p3 saved OK")
