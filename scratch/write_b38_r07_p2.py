import json

RECORDS = [
    ("088103", "somatology", "noun", "/ˌsoʊməˈtɑːlədʒi/", "nhân chủng học hình thể cơ thể"),
    ("088104", "somatome", "noun", "/ˈsoʊməˌtoʊm/", "đốt phôi; khúc thân phôi thai"),
    ("088105", "somatoplasm", "noun", "/soʊˈmætəˌplæzəm/", "chất sinh dưỡng tế bào thân"),
    ("088106", "somatopleure", "noun", "/soʊˈmætəˌplʊr/", "lá thành phôi thai"),
    ("088107", "somatosense", "noun", "/ˌsoʊmətoʊˈsɛns/", "cảm giác bản thể thân thể"),
    ("088108", "somatotrophin", "noun", "/ˌsoʊmətoʊˈtroʊfɪn/", "hormone tăng trưởng somatotropin"),
    ("088109", "somatotropic", "adj", "/ˌsoʊmətoʊˈtrɑːpɪk/", "kích thích tăng trưởng cơ thể"),
    ("088110", "somatotype", "noun", "/soʊˈmætəˌtaɪp/", "tạng người; kiểu thể hình cơ thể"),
    ("088111", "sombreness", "noun", "/ˈsɑːmbərnəs/", "vẻ u ám ảm đạm; sự u sầu"),
    ("088112", "sombrous", "adj", "/ˈsɑːmbrəs/", "u ám; ảm đạm; trầm buồn"),
    ("088113", "somersaulted", "verb", "/ˈsʌmərˌsɔːltɪd/", "đã nhào lộn vòng trên không"),
    ("088114", "somersaults", "verb", "/ˈsʌmərˌsɔːlts/", "nhào lộn vòng trên không"),
    ("088115", "somersets", "verb", "/ˈsʌmərsɛts/", "nhào lộn nhào vòng"),
    ("088116", "somersetted", "verb", "/ˈsʌmərsɛtɪd/", "đã nhào lộn nhào vòng"),
    ("088117", "somersetting", "verb", "/ˈsʌmərsɛtɪŋ/", "đang nhào lộn nhào vòng"),
    ("088118", "somesthesia", "noun", "/ˌsɑːmɪsˈθiːʒə/", "cảm giác thân thể xúc giác bản thể"),
    ("088119", "somesthesis", "noun", "/ˌsɑːmɪsˈθiːsɪs/", "hệ cảm giác thân thể"),
    ("088120", "something", "pron", "/ˈsʌmθɪŋ/", "điều gì đó; việc gì đó; thứ gì đó"[:35]),
    ("088121", "somewhither", "adv", "/ˈsʌmˌwɪðər/", "đến một nơi nào đó (từ cổ)"),
    ("088122", "somewise", "adv", "/ˈsʌmˌwaɪz/", "bằng một cách nào đó"),
    ("088123", "somital", "adj", "/ˈsoʊmɪtəl/", "thuộc đốt phôi; thuộc khúc thân"),
    ("088124", "somitic", "adj", "/soʊˈmɪtɪk/", "thuộc đốt phôi (phôi học)"),
    ("088125", "sommers", "noun", "/ˈsɑːmərz/", "tên họ Sommer; dòng họ Sommer"),
    ("088126", "somnambulant", "adj", "/sɑːmˈnæmbjələnt/", "mộng du; đi lại trong lúc ngủ"),
    ("088127", "somnambulate", "verb", "/sɑːmˈnæmbjəˌleɪt/", "bị mộng du; bước đi khi đang ngủ"),
    ("088128", "somnambulation", "noun", "/sɑːmˌnæmbjəˈleɪʃən/", "chứng mộng du; trạng thái miên hành"[:35]),
    ("088129", "somnambules", "noun", "/sɑːmˈnæmbjuːlz/", "người mắc chứng mộng du"),
    ("088130", "somnambulistic", "adj", "/sɑːmˌnæmbjəˈlɪstɪk/", "thuộc chứng mộng du; như mộng du"),
    ("088131", "somniferous", "adj", "/sɑːmˈnɪfərəs/", "gây buồn ngủ; có tác dụng gây ngủ"),
    ("088132", "somnific", "adj", "/sɑːmˈnɪfɪk/", "gây buồn ngủ; dễ ru ngủ"),
    ("088133", "somniloquence", "noun", "/sɑːmˈnɪləkwəns/", "tật nói mớ trong khi ngủ"),
    ("088134", "somniloquens", "noun", "/sɑːmˈnɪləkwəns/", "chứng nói mớ khi đang ngủ"),
    ("088135", "somniloquism", "noun", "/sɑːmˈnɪləˌkwɪzəm/", "tật nói mớ; nói mơ khi ngủ"),
    ("088136", "somniloquist", "noun", "/sɑːmˈnɪləkwɪst/", "người hay nói mớ khi ngủ"),
    ("088137", "somniloquous", "adj", "/sɑːmˈnɪləkwəs/", "hay nói mớ trong khi ngủ"),
    ("088138", "somniloquy", "noun", "/sɑːmˈnɪləkwi/", "chứng nói mớ khi ngủ"),
    ("088139", "somnolency", "noun", "/ˈsɑːmnələnsi/", "cơn buồn ngủ; trạng thái lơ mơ"),
    ("088140", "somnolently", "adv", "/ˈsɑːmnələntli/", "ngái ngủ; lờ đờ buồn ngủ"),
    ("088141", "somnolism", "noun", "/ˈsɑːmnəˌlɪzəm/", "trạng thái ngủ thôi miên"),
    ("088142", "somnophilia", "noun", "/ˌsɑːmnoʊˈfɪliə/", "chứng lệch lạc ham muốn người ngủ"),
    ("088143", "somrai", "noun", "/sɔːmˈraɪ/", "tiếng Somrai (Cộng hòa Tchad)"),
    ("088144", "sonance", "noun", "/ˈsoʊnəns/", "sự phát ra âm thanh; âm sắc vang"),
    ("088145", "sonancy", "noun", "/ˈsoʊnənsi/", "tính chất hữu thanh (ngữ âm học)"),
    ("088146", "sonant", "adj", "/ˈsoʊnənt/", "hữu thanh; vang tiếng"),
    ("088147", "sonde", "noun", "/sɑːnd/", "máy dò khí tượng phóng tầng cao"),
    ("088148", "songful", "adj", "/ˈsɔːŋfəl/", "du dương; tràn ngập tiếng ca"),
    ("088149", "songfulness", "noun", "/ˈsɔːŋfəlnəs/", "tính du dương giàu nhạc điệu"),
    ("088150", "songless", "adj", "/ˈsɔːŋləs/", "không cất tiếng hót; không bài hát"[:35]),
    ("088151", "songlike", "adj", "/ˈsɔːŋˌlaɪk/", "du dương như một bài hát"),
    ("088152", "songsmith", "noun", "/ˈsɔːŋˌsmɪθ/", "nhạc sĩ sáng tác ca khúc"),
    ("088153", "songsters", "noun", "/ˈsɔːŋstərz/", "ca sĩ; loài chim biết hót"),
    ("088154", "songstresses", "noun", "/ˈsɔːŋstrəsɪz/", "nữ ca sĩ"),
    ("088155", "sonically", "adv", "/ˈsɑːnɪkli/", "về mặt âm thanh"),
    ("088156", "soniferous", "adj", "/soʊˈnɪfərəs/", "truyền âm thanh; phát ra tiếng"),
    ("088157", "sonless", "adj", "/ˈsʌnləs/", "không có con trai nối dõi"),
    ("088158", "sonly", "adj", "/ˈsʌnli/", "hiếu thảo; đúng đạo làm con trai"),
    ("088159", "sonneteer", "noun", "/ˌsɑːnəˈtɪr/", "nhà thơ sáng tác thơ sonnet"),
    ("088160", "sonnic", "adj", "/ˈsɑːnɪk/", "thuộc âm thanh; siêu thanh"),
    ("088161", "sonobuoy", "noun", "/ˈsɑːnoʊˌbuːi/", "phao thủy âm phát hiện tàu ngầm"),
    ("088162", "sonograph", "noun", "/ˈsɑːnəˌɡræf/", "máy ghi quang phổ âm; máy siêu âm"),
    ("088163", "sonoluminescence", "noun", "/ˌsɑːnoʊˌluːməˈnɛsəns/", "hiện tượng phát quang do siêu âm"),
    ("088164", "sonometer", "noun", "/soʊˈnɑːmɪtər/", "âm kế; máy đo dây rung và thính lực"[:35]),
    ("088165", "sonomicrometry", "noun", "/ˌsɑːnoʊmaɪˈkrɑːmətri/", "phép đo khoảng cách vi mô bằng siêu âm"[:35]),
    ("088166", "sonorific", "adj", "/ˌsɑːnəˈrɪfɪk/", "phát ra âm thanh vang dội"),
    ("088167", "sonorousness", "noun", "/səˈnɔːrəsnəs/", "độ vang rền trầm ấm (giọng nói)"),
    ("088168", "sons", "noun", "/sʌnz/", "con trai"),
    ("088169", "sonship", "noun", "/ˈsʌnˌʃɪp/", "địa vị làm con trai; tư cách con"),
    ("088170", "sonsy", "adj", "/ˈsɑːnsi/", "khỏe mạnh đẫy đà phúc hậu"),
    ("088171", "soochong", "noun", "/ˈsuːˌtʃɔːŋ/", "trà đen Tiểu Chủng Phúc Kiến"),
    ("088172", "sool", "verb", "/suːl/", "suỵt chó tấn công; thúc giục (Úc)"),
    ("088173", "soony", "adj", "/ˈsuːni/", "mủi lòng ủy mị; dễ xúc động"),
    ("088174", "sooted", "adj", "/ˈsʊtɪd/", "ám đầy bồ hóng muội than"),
    ("088175", "sooterkin", "noun", "/ˈsuːtərkɪn/", "quái vật nhỏ hư cấu; ý tưởng yểu"),
    ("088176", "soothed", "verb", "/suːðd/", "đã xoa dịu; đã làm nguôi cơn đau"),
    ("088177", "soother", "noun", "/ˈsuːðər/", "núm vú giả; người an ủi xoa dịu"),
    ("088178", "soothes", "verb", "/suːðz/", "xoa dịu; làm dịu cơn đau hay giận"),
    ("088179", "soothfast", "adj", "/ˈsuːθˌfæst/", "trung thực; đáng tin; chung thủy"),
    ("088180", "soothfastly", "adv", "/ˈsuːθˌfæstli/", "một cách chân thực trung thành"),
    ("088181", "soothfastness", "noun", "/ˈsuːθˌfæstnəs/", "sự chân thực; lòng trung thành"),
    ("088182", "soothly", "adv", "/ˈsuːθli/", "thật vậy; chân thực (văn cổ)"),
    ("088183", "soothsay", "verb", "/ˈsuːθˌseɪ/", "tiên đoán tương lai; bói toán"),
    ("088184", "sootily", "adv", "/ˈsʊtɪli/", "đen nhẻm muội than bồ hóng"),
    ("088185", "sootiness", "noun", "/ˈsʊtinəs/", "tình trạng bám đầy bồ hóng"),
    ("088186", "sootless", "adj", "/ˈsʊtləs/", "không có bồ hóng muội than"),
    ("088187", "sophister", "noun", "/ˈsɑːfɪstər/", "sinh viên năm hai ba (Cambridge)"),
    ("088188", "sophistically", "adv", "/səˈfɪstɪkli/", "theo lối ngụy biện khéo léo"),
    ("088189", "sophisticatedly", "adv", "/səˈfɪstəˌkeɪtɪdli/", "tinh tế sành sỏi; phức tạp cao"),
    ("088190", "sophisticates", "verb", "/səˈfɪstəˌkeɪts/", "làm phức tạp tinh vi; làm mất chất"[:35]),
    ("088191", "sophisticating", "verb", "/səˈfɪstəˌkeɪtɪŋ/", "đang làm phức tạp; pha trộn giả"),
    ("088192", "sophists", "noun", "/ˈsɑːfɪsts/", "nhà ngụy biện; triết gia biện sĩ"),
    ("088193", "sophomoric", "adj", "/ˌsɑːfəˈmɔːrɪk/", "nông nổi tỏ ra hiểu biết; năm hai"),
    ("088194", "sophonias", "noun", "/ˌsɑːfəˈnaɪəs/", "tiên tri Xô-phô-ni (Kinh Thánh)"),
    ("088195", "sophy", "noun", "/ˈsoʊfi/", "quốc vương Ba Tư triều đại Safavid"[:35]),
    ("088196", "soporiferous", "adj", "/ˌsɑːpəˈrɪfərəs/", "gây buồn ngủ; buồn tẻ dễ ru ngủ"),
    ("088197", "soporifically", "adv", "/ˌsɑːpəˈrɪfɪkli/", "gây buồn ngủ rũ rượi"),
    ("088198", "sopped", "verb", "/sɑːpt/", "đã nhúng thấm đẫm; thấm hút nước"),
    ("088199", "soppily", "adv", "/ˈsɑːpɪli/", "ướt sũng; ủy mị sướt mướt quá đà"),
    ("088200", "soppiness", "noun", "/ˈsɑːpinəs/", "tính ướt sũng; sự ủy mị sướt mướt"),
    ("088201", "soprani", "noun", "/səˈprɑːni/", "ca sĩ giọng nữ cao"),
    ("088202", "sopranist", "noun", "/səˈprɑːnɪst/", "nam ca sĩ hát giọng nữ cao soprano"[:35]),
]

# Remove slices cleanly <= 35 chars
RECORDS[17] = ("088120", "something", "pron", "/ˈsʌmθɪŋ/", "điều gì đó; thứ gì đó; chút ít")
RECORDS[25] = ("088128", "somnambulation", "noun", "/sɑːmˌnæmbjəˈleɪʃən/", "chứng mộng du; tật miên hành")
RECORDS[47] = ("088150", "songless", "adj", "/ˈsɔːŋləs/", "không biết hót; thiếu tiếng hát")
RECORDS[61] = ("088164", "sonometer", "noun", "/soʊˈnɑːmɪtər/", "âm kế; máy đo dây rung thính lực")
RECORDS[62] = ("088165", "sonomicrometry", "noun", "/ˌsɑːnoʊmaɪˈkrɑːmətri/", "phép đo vi mô bằng sóng siêu âm")
RECORDS[87] = ("088190", "sophisticates", "verb", "/səˈfɪstəˌkeɪts/", "làm tinh vi phức tạp; pha tạp")
RECORDS[92] = ("088195", "sophy", "noun", "/ˈsoʊfi/", "quốc vương Ba Tư triều Safavid")
RECORDS[99] = ("088202", "sopranist", "noun", "/səˈprɑːnɪst/", "ca sĩ nam hát giọng nữ cao")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r07_raw_p2.json"))
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

json.dump(out, open("scratch/b38_r07_reviewed_p2.json", "w"), ensure_ascii=False, indent=2)
print("b38_r07_p2 saved OK")
