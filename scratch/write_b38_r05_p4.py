import json

RECORDS = [
    ("087303", "skippet", "noun", "/ˈskɪpɪt/", "hộp tròn bằng gỗ đựng ấn triện"),
    ("087304", "skipping", "verb", "/ˈskɪpɪŋ/", "đang bỏ qua; đang nhảy dây"),
    ("087305", "skippingly", "adv", "/ˈskɪpɪŋli/", "nhảy nhót tung tăng; bỏ quãng"),
    ("087306", "skips", "verb", "/skɪps/", "bỏ qua; nhảy dây; ném thia lia"),
    ("087307", "skirmished", "verb", "/ˈskɜːrmɪʃt/", "đã đụng độ giao tranh nhỏ"),
    ("087308", "skirmishers", "noun", "/ˈskɜːrmɪʃərz/", "lính trinh sát giao tranh tiên phong"[:35]),
    ("087309", "skirmishes", "verb", "/ˈskɜːrmɪʃɪz/", "giao tranh lẻ tẻ; tranh cãi nhỏ"),
    ("087310", "skirmishing", "verb", "/ˈskɜːrmɪʃɪŋ/", "đang giao tranh lẻ tẻ; cãi vã nhẹ"),
    ("087311", "skirr", "verb", "/skɜːr/", "lướt nhanh; chạy rảo sục sạo"),
    ("087312", "skirret", "noun", "/ˈskɪrɪt/", "cây rau cần củ ngọt Sium sisarum"),
    ("087313", "skirted", "verb", "/ˈskɜːrtɪd/", "đã đi vòng ven; đã né tránh"),
    ("087314", "skirts", "verb", "/skɜːrts/", "đi dọc theo rìa; né tránh đề cập"),
    ("087315", "skis", "verb", "/skiːz/", "trượt tuyết; trượt nước"),
    ("087316", "skite", "noun", "/skaɪt/", "kẻ khoác lác (Úc); cú đánh xéo"),
    ("087317", "skittishly", "adv", "/ˈskɪtɪʃli/", "hay giật mình; nhát sợ; đồng bóng"),
    ("087318", "skived", "verb", "/skaɪvd/", "đã trốn việc; đã lạng mỏng da"),
    ("087319", "skiver", "noun", "/ˈskaɪvər/", "dao lạng da; da cừu xẻ mỏng"),
    ("087320", "skives", "verb", "/skaɪvz/", "trốn việc; lạng mỏng tấm da"),
    ("087321", "skiving", "verb", "/ˈskaɪvɪŋ/", "đang trốn việc; đang lạng mỏng da"),
    ("087322", "skoal", "intj", "/skoʊl/", "cạn ly; chúc sức khỏe (Bắc Âu)"),
    ("087323", "skoplje", "noun", "/ˈskɔːpjə/", "thủ đô Skopje (Bắc Macedonia)"),
    ("087324", "skorpions", "noun", "/ˈskɔːrpiənz/", "súng tiểu liên Skorpion"),
    ("087325", "skreak", "verb", "/skriːk/", "rít lên kẽo kẹt; kêu thé"),
    ("087326", "skreigh", "verb", "/skriːx/", "kêu thét lên; thét vang (Scotland)"),
    ("087327", "skulked", "verb", "/skʌlkt/", "đã lén lút ẩn nấp; trốn việc"),
    ("087328", "skulkingly", "adv", "/ˈskʌlkɪŋli/", "lén lút rình rập; lẩn trốn"),
    ("087329", "skulks", "verb", "/skʌlks/", "lén lút rình rập; lẩn trốn việc"),
    ("087330", "skunkbush", "noun", "/ˈskʌŋkˌbʊʃ/", "cây bụi thơm hôi Rhus trilobata"),
    ("087331", "skunked", "verb", "/skʌŋkt/", "đã thua trắng tay; xịt mùi hôi"),
    ("087332", "skunking", "verb", "/ˈskʌŋkɪŋ/", "đang thắng trắng áp đảo; xịt hôi"),
    ("087333", "skunks", "verb", "/skʌŋks/", "đánh bại trắng tay (thể thao)"),
    ("087334", "skunkweed", "noun", "/ˈskʌŋkˌwiːd/", "cây cỏ mùi chồn hôi Bắc Mỹ"),
    ("087335", "skupshtina", "noun", "/ˈskʊpʃtɪnə/", "Quốc hội Serbia hay Montenegro"),
    ("087336", "skuxx", "adj", "/skʌks/", "bảnh bao; ngầu; sành điệu (lóng)"),
    ("087337", "skyed", "adj", "/skaɪd/", "treo quá cao trên tường triển lãm"),
    ("087338", "skyer", "noun", "/ˈskaɪər/", "cú đánh bóng bay vọt lên cao"),
    ("087339", "skyey", "adj", "/ˈskaɪi/", "thuộc bầu trời; xanh ngắt như trời"),
    ("087340", "skying", "verb", "/ˈskaɪɪŋ/", "đang đá bóng bổng lên trời"),
    ("087341", "skyjack", "verb", "/ˈskaɪˌdʒæk/", "cướp máy bay; không tặc"),
    ("087342", "skylarked", "verb", "/ˈskaɪˌlɑːrkt/", "đã nô đùa nghịch ngợm ầm ĩ"),
    ("087343", "skylarking", "verb", "/ˈskaɪˌlɑːrkɪŋ/", "đang nô đùa nghịch ngợm ầm ĩ"),
    ("087344", "skylarks", "verb", "/ˈskaɪˌlɑːrks/", "nô đùa nghịch ngợm ồn ào"),
    ("087345", "skylights", "noun", "/ˈskaɪˌlaɪts/", "cửa sổ trời trên mái nhà"),
    ("087346", "skyman", "noun", "/ˈskaɪmən/", "phi công; nhà hàng không"),
    ("087347", "skysail", "noun", "/ˈskaɪˌseɪl/", "cánh buồm cao nhất trên cột buồm"),
    ("087348", "skyscape", "noun", "/ˈskaɪˌskeɪp/", "quang cảnh bầu trời; tranh bầu trời"[:35]),
    ("087349", "slabbed", "verb", "/slæbd/", "đã xẻ thành phiến dày; lát tấm"),
    ("087350", "slabbing", "noun", "/ˈslæbɪŋ/", "gỗ bìa xẻ; sự cán phôi tấm dày"),
    ("087351", "slabs", "verb", "/slæbz/", "xẻ thành tấm dày; lát phiến đá"),
    ("087352", "slacked", "verb", "/slækt/", "đã nới lỏng; đã tôi vôi; lười biếng"[:35]),
    ("087353", "slackened", "verb", "/ˈslækənd/", "đã chùng xuống; đã chậm lại"),
    ("087354", "slackens", "verb", "/ˈslækənz/", "nới lỏng; chùng xuống; chậm lại"),
    ("087355", "slacklime", "noun", "/ˈslækˌlaɪm/", "vôi tôi"),
    ("087356", "slackline", "noun", "/ˈslækˌlaɪn/", "dây chùng đi thăng bằng"),
    ("087357", "slackly", "adv", "/ˈslækli/", "lỏng lẻo; uể oải thiếu chặt chẽ"),
    ("087358", "slagged", "verb", "/slæɡd/", "đã chỉ trích thậm tệ; tạo xỉ"),
    ("087359", "slagging", "verb", "/ˈslæɡɪŋ/", "đang chửi rủa chê bai; đang đóng xỉ"[:35]),
    ("087360", "slaggy", "adj", "/ˈslæɡi/", "có xỉ; giống xỉ luyện kim"),
    ("087361", "slagheap", "noun", "/ˈslæɡˌhiːp/", "bãi thải xỉ than mỏ"),
    ("087362", "slags", "verb", "/slæɡz/", "chỉ trích thậm tệ; kết thành xỉ"),
    ("087363", "slakeless", "adj", "/ˈsleɪkləs/", "không thể giải tỏa; không dập được"[:35]),
    ("087364", "slakes", "verb", "/sleɪks/", "làm dịu cơn khát; tôi vôi sống"),
    ("087365", "slaking", "verb", "/ˈsleɪkɪŋ/", "đang giải khát; đang tôi vôi sống"),
    ("087366", "slammed", "verb", "/slæmd/", "đã đóng sầm cửa; đã chỉ trích mạnh"[:35]),
    ("087367", "slammers", "noun", "/ˈslæmərz/", "nhà tù (lóng); người đóng sầm cửa"),
    ("087368", "slamming", "verb", "/ˈslæmɪŋ/", "đang đóng sầm; đang chỉ trích mạnh"),
    ("087369", "slams", "verb", "/slæmz/", "đóng sầm; đập mạnh; chỉ trích gay"),
    ("087370", "slandered", "verb", "/ˈslændərd/", "đã vu khống; đã phỉ báng danh dự"),
    ("087371", "slandering", "verb", "/ˈslændərɪŋ/", "đang vu khống; đang phỉ báng"),
    ("087372", "slanderously", "adv", "/ˈslændərəsli/", "mang tính vu khống phỉ báng"),
    ("087373", "slanderousness", "noun", "/ˈslændərəsnəs/", "tính chất vu khống phỉ báng"),
    ("087374", "slanders", "verb", "/ˈslændərz/", "vu khống; phỉ báng; nói xấu"),
    ("087375", "slangily", "adv", "/ˈslæŋɪli/", "theo kiểu tiếng lóng"),
    ("087376", "slanginess", "noun", "/ˈslæŋinəs/", "tính chất dùng nhiều tiếng lóng"),
    ("087377", "slanguage", "noun", "/ˈslæŋɡwɪdʒ/", "ngôn ngữ đậm tiếng lóng"),
    ("087378", "slantingly", "adv", "/ˈslæntɪŋli/", "nghiêng xiên; chéo cạnh"),
    ("087379", "slantingness", "noun", "/ˈslæntɪŋnəs/", "độ nghiêng xiên; tính thiên lệch"),
    ("087380", "slants", "verb", "/slænts/", "nghiêng xiên; bóp méo thiên lệch"),
    ("087381", "slantways", "adv", "/ˈslæntˌweɪz/", "theo hướng xiên chéo"),
    ("087382", "slantwise", "adv", "/ˈslæntˌwaɪz/", "theo chiều nghiêng xiên chéo"),
    ("087383", "slaphappy", "adj", "/ˈslæpˌhæpi/", "lơ ngơ vui vẻ thiếu nghiêm túc"),
    ("087384", "slapjack", "noun", "/ˈslæpˌdʒæk/", "bánh kếp; trò chơi bài slapjack"),
    ("087385", "slapjacks", "noun", "/ˈslæpˌdʒæks/", "bánh kếp nóng áp chảo"),
    ("087386", "slapped", "verb", "/slæpt/", "đã tát; đã vỗ mạnh; đã áp đặt"),
    ("087387", "slapping", "verb", "/ˈslæpɪŋ/", "đang tát; đang vỗ mạnh; đang áp đặt"[:35]),
    ("087388", "slaps", "verb", "/slæps/", "tát; vỗ mạnh; áp đặt mức phạt"),
    ("087389", "slapt", "verb", "/slæpt/", "đã tát; đã vỗ mạnh (cổ)"),
    ("087390", "slashes", "verb", "/ˈslæʃɪz/", "chém mạnh; cắt giảm mạnh"),
    ("087391", "slated", "verb", "/ˈsleɪtɪd/", "đã lợp ngói đá; đã chỉ trích nặng"[:35]),
    ("087392", "slates", "verb", "/sleɪts/", "lợp đá phiến; dự kiến; chỉ trích"),
    ("087393", "slatey", "adj", "/ˈsleɪti/", "màu xám đá phiến; dễ tách phiến"),
    ("087394", "slathering", "verb", "/ˈslæðərɪŋ/", "đang phết dày; đang trét đẫm"),
    ("087395", "slathers", "verb", "/ˈslæðərz/", "phết dày đặc; trét đẫm lên"),
    ("087396", "slatiness", "noun", "/ˈsleɪtinəs/", "tính chất phân phiến như đá phiến"),
    ("087397", "slats", "verb", "/slæts/", "đóng thanh nan gỗ; đập lạch bạch"),
    ("087398", "slatted", "adj", "/ˈslætɪd/", "có gắn các thanh nan gỗ song song"),
    ("087399", "slatternliness", "noun", "/ˈslætərnlinəs/", "thói cẩu thả luộm thuộm lếch thếch"[:35]),
    ("087400", "slaughtered", "verb", "/ˈslɔːtərd/", "đã giết mổ; đã tàn sát dã man"),
    ("087401", "slaughterers", "noun", "/ˈslɔːtərərz/", "người giết mổ gia súc; kẻ đồ tể"),
    ("087402", "slaughtering", "verb", "/ˈslɔːtərɪŋ/", "đang giết mổ; đang tàn sát"),
]

# Remove all slices cleanly <= 35 chars
RECORDS[5] = ("087308", "skirmishers", "noun", "/ˈskɜːrmɪʃərz/", "lính trinh sát giao tranh đầu")
RECORDS[45] = ("087348", "skyscape", "noun", "/ˈskaɪˌskeɪp/", "cảnh bầu trời; tranh vẽ bầu trời")
RECORDS[49] = ("087352", "slacked", "verb", "/slækt/", "đã nới lỏng; đã tôi vôi")
RECORDS[56] = ("087359", "slagging", "verb", "/ˈslæɡɪŋ/", "đang chê bai thậm tệ; tạo xỉ")
RECORDS[60] = ("087363", "slakeless", "adj", "/ˈsleɪkləs/", "không thể nguôi ngoai; không dịu")
RECORDS[63] = ("087366", "slammed", "verb", "/slæmd/", "đã đóng sầm; đã chỉ trích mạnh")
RECORDS[84] = ("087387", "slapping", "verb", "/ˈslæpɪŋ/", "đang tát; đang vỗ mạnh; áp đặt")
RECORDS[88] = ("087391", "slated", "verb", "/ˈsleɪtɪd/", "đã lợp đá phiến; đã dự kiến")
RECORDS[96] = ("087399", "slatternliness", "noun", "/ˈslætərnlinəs/", "thói cẩu thả luộm thuộm bê bối")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r05_raw_p4.json"))
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

json.dump(out, open("scratch/b38_r05_reviewed_p4.json", "w"), ensure_ascii=False, indent=2)
print("b38_r05_p4 saved OK")
