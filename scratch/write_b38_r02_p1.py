import json

RECORDS = [
    ("085503", "scotodinia", "noun", "/ˌskɑːtəˈdɪniə/", "chóng mặt kèm tối sầm mắt"),
    ("085504", "scotomatous", "adj", "/skəˈtɑːmətəs/", "thuộc ám điểm (thị lực)"),
    ("085505", "scotophilous", "adj", "/skəˈtɑːfɪləs/", "ưa tối; sống hoạt động về đêm"),
    ("085506", "scotopia", "noun", "/skəˈtoʊpiə/", "thị giác nhìn trong bóng tối"),
    ("085507", "scotopic", "adj", "/skəˈtɑːpɪk/", "thích nghi nhìn trong tối"),
    ("085508", "scottice", "adv", "/ˈskɑːtɪsi/", "theo cách nói tiếng Scotland"),
    ("085509", "scotticise", "verb", "/ˈskɑːtɪˌsaɪz/", "Scotland hóa"),
    ("085510", "scotticism", "noun", "/ˈskɑːtɪˌsɪzəm/", "cách nói đặc trưng Scotland"),
    ("085511", "scotticize", "verb", "/ˈskɑːtɪˌsaɪz/", "Scotland hóa"),
    ("085512", "scoubidous", "noun", "/ˈskuːbɪduːz/", "dây nhựa đan móc khóa"),
    ("085513", "scoundrelism", "noun", "/ˈskaʊndrəˌlɪzəm/", "hành vi đê tiện vô lại"),
    ("085514", "scoundrelly", "adj", "/ˈskaʊndrəli/", "vô lại; đểu cáng; bất lương"),
    ("085515", "scoundrelom", "noun", "/ˈskaʊndrəldəm/", "giới vô lại; tính chất đê tiện"),
    ("085516", "scourage", "noun", "/ˈskaʊrɪdʒ/", "nước tẩy rửa; bọt nước cọ rửa"),
    ("085517", "scourged", "verb", "/skɜːrdʒd/", "đã đánh bằng roi; đã tàn phá"),
    ("085518", "scourger", "noun", "/ˈskɜːrdʒər/", "kẻ đánh roi; kẻ hành hạ"),
    ("085519", "scourges", "verb", "/ˈskɜːrdʒɪz/", "đánh bằng roi; tàn phá nặng nề"),
    ("085520", "scourging", "verb", "/ˈskɜːrdʒɪŋ/", "đang đánh bằng roi; đang tàn phá"),
    ("085521", "scourings", "noun", "/ˈskaʊrɪŋz/", "chất cặn tẩy rửa; bọt nước cọ"),
    ("085522", "scoutcraft", "noun", "/ˈskaʊtˌkræft/", "kỹ năng hướng đạo sinh"),
    ("085523", "scouted", "verb", "/ˈskaʊtɪd/", "đã trinh sát; đã bác bỏ thẳng"),
    ("085524", "scouts", "verb", "/skaʊts/", "trinh sát; dò xét; tìm kiếm"),
    ("085525", "scowled", "verb", "/skaʊld/", "đã cau mày giận dữ"),
    ("085526", "scowlingly", "adv", "/ˈskaʊlɪŋli/", "cau có giận dữ; quắc mắt"),
    ("085527", "scowls", "verb", "/skaʊlz/", "cau mày giận dữ; nhìn sưng sỉa"),
    ("085528", "scpo", "noun", "/ˌɛsˌsiːˌpiːˈoʊ/", "thượng sĩ hải quân (SCPO)"),
    ("085529", "scrabbly", "adj", "/ˈskræbli/", "cằn cỗi thưa thớt; nguệch ngoạc"),
    ("085530", "scragged", "adj", "/skræɡd/", "gầy guộc khẳng khiu; lởm chởm"),
    ("085531", "scragginess", "noun", "/ˈskræɡinəs/", "vẻ gầy guộc khẳng khiu"),
    ("085532", "scrambles", "verb", "/ˈskræmbəlz/", "trèo vội; tranh giành; đánh trứng"),
    ("085533", "scrambling", "verb", "/ˈskræmbəlɪŋ/", "đang trèo vội; đang tranh giành"),
    ("085534", "scramjet", "noun", "/ˈskræmˌdʒɛt/", "động cơ phản lực tĩnh siêu âm"),
    ("085535", "scran", "noun", "/skræn/", "đồ ăn; thức ăn thừa"),
    ("085536", "scranch", "verb", "/skræntʃ/", "nhai giòn rụm; kêu lạo xạo"),
    ("085537", "scrannel", "adj", "/ˈskrænəl/", "gầy còm; thé yếu (âm thanh)"),
    ("085538", "scranny", "adj", "/ˈskræni/", "gầy gò khẳng khiu; còm cõi"),
    ("085539", "scraped", "verb", "/skreɪpt/", "đã cạo; đã nạo; đã trầy xước"),
    ("085540", "scrapes", "verb", "/skreɪps/", "cạo; nạo; cọ xát gây trầy"),
    ("085541", "scrappage", "noun", "/ˈskræpɪdʒ/", "phế liệu; việc thanh lý xe cũ"),
    ("085542", "scrapped", "verb", "/skræpt/", "đã hủy bỏ; đã tháo làm phế liệu"),
    ("085543", "scrappily", "adv", "/ˈskræpɪli/", "chắp vá lộn xộn; đầy quyết liệt"),
    ("085544", "scrapping", "verb", "/ˈskræpɪŋ/", "đang hủy bỏ; đang ẩu đả"),
    ("085545", "scratched", "verb", "/skrætʃt/", "đã cào xước; đã gãi; đã gạch bỏ"),
    ("085546", "scratches", "verb", "/ˈskrætʃɪz/", "cào xước; gãi; gạch bỏ"),
    ("085547", "scratchily", "adv", "/ˈskrætʃɪli/", "nguệch ngoạc; cẩu thả; rè rít"),
    ("085548", "scratchiness", "noun", "/ˈskrætʃinəs/", "độ thô ráp; giọng khàn rít"),
    ("085549", "scraunch", "verb", "/skrɔːntʃ/", "nhai rôm rốp; kêu lạo xạo"),
    ("085550", "scrawled", "verb", "/skrɔːld/", "đã viết nguệch ngoạc"),
    ("085551", "scrawler", "noun", "/ˈskrɔːlər/", "người viết chữ nguệch ngoạc"),
    ("085552", "scrawling", "verb", "/ˈskrɔːlɪŋ/", "đang viết nguệch ngoạc"),
    ("085553", "scrawls", "verb", "/skrɔːlz/", "viết nguệch ngoạc"),
    ("085554", "scrawly", "adj", "/ˈskrɔːli/", "nguệch ngoạc; viết cẩu thả"),
    ("085555", "scrawniness", "noun", "/ˈskrɔːninəs/", "vẻ gầy nhom ốm yếu"),
    ("085556", "scray", "noun", "/skreɪ/", "chim nhạn biển"),
    ("085557", "scrayer", "noun", "/ˈskreɪər/", "chim nhạn biển"),
    ("085558", "screak", "verb", "/skriːk/", "kêu cót két; rít chói tai"),
    ("085559", "screakily", "adv", "/ˈskriːkɪli/", "kẽo kẹt; rít lên chói tai"),
    ("085560", "screaky", "adj", "/ˈskriːki/", "kêu cót két; kẽo kẹt"),
    ("085561", "screamed", "verb", "/skriːmd/", "đã hét lên; đã la thét"),
    ("085562", "screamers", "noun", "/ˈskriːmərz/", "kẻ hay hét; chim báo động"),
    ("085563", "screams", "verb", "/skriːmz/", "hét lên; la thét; kêu vang"),
    ("085564", "screeched", "verb", "/skriːtʃt/", "đã hét chói tai; đã rít kít"),
    ("085565", "screeches", "verb", "/ˈskriːtʃɪz/", "hét chói tai; rít lên kít kít"),
    ("085566", "screened", "verb", "/skriːnd/", "đã che chắn; đã sàng lọc; chiếu"),
    ("085567", "screenings", "noun", "/ˈskriːnɪŋz/", "buổi chiếu phim; việc sàng lọc"),
    ("085568", "screenland", "noun", "/ˈskriːnˌlænd/", "kinh đô điện ảnh; giới phim ảnh"),
    ("085569", "screens", "verb", "/skriːnz/", "che chắn; sàng lọc; trình chiếu"),
    ("085570", "screensaver", "noun", "/ˈskriːnˌseɪvər/", "trình bảo vệ màn hình"),
    ("085571", "screeve", "verb", "/skriːv/", "vẽ tranh phấn trên vỉa hè"),
    ("085572", "screever", "noun", "/ˈskriːvər/", "họa sĩ vẽ phấn vỉa hè"),
    ("085573", "screwballer", "noun", "/ˈskruːˌbɔːlər/", "người ném bóng xoáy ngược"),
    ("085574", "screwbean", "noun", "/ˈskruːˌbiːn/", "cây đậu quả xoắn Prosopis"),
    ("085575", "screwed", "verb", "/skruːd/", "đã vặn vít; đã làm hỏng bét"),
    ("085576", "screwiness", "noun", "/ˈskruːinəs/", "tính gàn dở; sự điên khùng"),
    ("085577", "screws", "verb", "/skruːz/", "vặn vít; siết chặt; ép buộc"),
    ("085578", "screwtop", "noun", "/ˈskruːˌtɑːp/", "nắp vặn (chai, lọ)"),
    ("085579", "scribacious", "adj", "/skraɪˈbeɪʃəs/", "say mê viết lách; thích cầm bút"),
    ("085580", "scribal", "adj", "/ˈskraɪbəl/", "thuộc người sao chép thư tịch"),
    ("085581", "scribbled", "verb", "/ˈskrɪbəld/", "đã viết nguệch ngoạc; viết vội"),
    ("085582", "scribblers", "noun", "/ˈskrɪblərz/", "người viết ẩu; nhà văn quèn"),
    ("085583", "scribbles", "verb", "/ˈskrɪbəlz/", "viết nguệch ngoạc; vẽ bậy"),
    ("085584", "scribbling", "verb", "/ˈskrɪblɪŋ/", "đang viết nguệch ngoạc; viết vội"),
    ("085585", "scribed", "verb", "/skraɪbd/", "đã vạch dấu bằng mũi vạch"),
    ("085586", "scribes", "verb", "/skraɪbz/", "sao chép; vạch dấu đường cắt"),
    ("085587", "scribing", "verb", "/ˈskraɪbɪŋ/", "đang sao chép; đang vạch dấu"),
    ("085588", "scrimmaged", "verb", "/ˈskrɪmɪdʒd/", "đã đấu tập; đã xô xát hỗn chiến"),
    ("085589", "scrimmager", "noun", "/ˈskrɪmɪdʒər/", "tiền đạo bóng bầu dục"),
    ("085590", "scrimmages", "verb", "/ˈskrɪmɪdʒɪz/", "đấu tập; xô xát tranh bóng"),
    ("085591", "scrimmaging", "verb", "/ˈskrɪmɪdʒɪŋ/", "đang đấu tập; đang xô xát"),
    ("085592", "scrimped", "verb", "/skrɪmpt/", "đã tằn tiện; đã cắt xén bủn xỉn"),
    ("085593", "scrimpiness", "noun", "/ˈskrɪmpinəs/", "tính bủn xỉn keo kiệt"),
    ("085594", "scrimping", "verb", "/ˈskrɪmpɪŋ/", "đang tiết kiệm tằn tiện"),
    ("085595", "scrimps", "verb", "/skrɪmps/", "tiết kiệm tằn tiện; cắt xén"),
    ("085596", "scrimpy", "adj", "/ˈskrɪmpi/", "ít ỏi; bủn xỉn; túng thiếu"),
    ("085597", "scrimshank", "verb", "/ˈskrɪmˌʃæŋk/", "trốn việc; lười biếng né tránh"),
    ("085598", "scrimshanker", "noun", "/ˈskrɪmˌʃæŋkər/", "kẻ trốn việc; kẻ làm biếng"),
    ("085599", "scrimshawed", "verb", "/ˈskrɪmˌʃɔːd/", "đã chạm khắc trên ngà voi xương"),
    ("085600", "scrimshawing", "verb", "/ˈskrɪmˌʃɔːɪŋ/", "đang chạm khắc ngà voi xương"),
    ("085601", "scrimshaws", "verb", "/ˈskrɪmˌʃɔːz/", "chạm khắc trên ngà voi xương"),
    ("085602", "scrimy", "adj", "/ˈskraɪmi/", "keo kiệt; bẩn thỉu nhếch nhác"),
]

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r02_raw_p1.json"))
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

json.dump(out, open("scratch/b38_r02_reviewed_p1.json", "w"), ensure_ascii=False, indent=2)
print("b38_r02_p1 saved OK")
