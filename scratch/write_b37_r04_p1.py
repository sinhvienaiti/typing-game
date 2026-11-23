import json

records = [
    ("081503", "ramming", "verb", "/ˈræmɪŋ/", "đâm sầm vào, nện chặt, thúc mạnh"),
    ("081504", "rammish", "adj", "/ˈræmɪʃ/", "hôi mùi dê đực, hăng nồng khó chịu"),
    ("081505", "ramoconidium", "noun", "/ˌreɪmoʊkəˈnɪdiəm/", "bào tử đính nhánh (nấm học)"),
    ("081506", "ramontchi", "noun", "/ˌræməntˈtʃiː/", "cây mận gai Madagascar, quả bồ quân"),
    ("081507", "ramontchis", "noun", "/ˌræməntˈtʃiːz/", "những cây mận gai Madagascar"),
    ("081508", "ramous", "adj", "/ˈreɪməs/", "có nhiều cành nhánh, phân nhánh"),
    ("081509", "rampaged", "verb", "/ˈræmpeɪdʒd/", "đã nổi cơn hung hãn, càn quét"),
    ("081510", "rampageous", "adj", "/ræmˈpeɪdʒəs/", "hung hãn, bạo lực, nổi loạn dữ dội"),
    ("081511", "rampageously", "adv", "/ræmˈpeɪdʒəsli/", "một cách hung hãn, điên cuồng"),
    ("081512", "rampageousness", "noun", "/ræmˈpeɪdʒəsnəs/", "tính hung hãn, cơn nổi giận dữ dội"),
    ("081513", "rampages", "verb", "/ˈræmpeɪdʒɪz/", "nổi cơn hung hãn, càn quét dữ dội"),
    ("081514", "rampaging", "verb", "/ˈræmpeɪdʒɪŋ/", "nổi cơn hung hãn, lao đi điên cuồng"),
    ("081515", "rampancy", "noun", "/ˈræmpənsi/", "tình trạng tràn lan, sự hoành hành"),
    ("081516", "ramparts", "noun", "/ˈræmpɑːrts/", "những lũy thành bảo vệ (pháo đài)"),
    ("081517", "ramphastidae", "noun", "/ræmˈfæstɪˌdiː/", "họ Chim tu-căng mỏ lớn"),
    ("081518", "ramphomicron", "noun", "/ˌræmfəˈmaɪkrɑːn/", "chi chim ruồi mỏ gai (Nam Mỹ)"),
    ("081519", "ramrods", "noun", "/ˈræmˌrɑːdz/", "que thông nòng súng; kẻ cứng nhắc"),
    ("081520", "rams", "verb", "/ræmz/", "đâm sầm vào, húc mạnh, nện chặt"),
    ("081521", "ramule", "noun", "/ˈræmjuːl/", "cành con, nhánh nhỏ (thực vật học)"),
    ("081522", "ranales", "noun", "/rəˈneɪliːz/", "bộ Mao lương (phân loại thực vật)"),
    ("081523", "ranatra", "noun", "/ˈrænətrə/", "chi bọ cạp nước thân que dài"),
    ("081524", "rance", "noun", "/ræns/", "đá hoa cương vân đỏ Bỉ; thanh giằng"),
    ("081525", "ranched", "verb", "/ræntʃt/", "đã làm chủ trang trại chăn nuôi"),
    ("081526", "ranches", "verb", "/ˈræntʃɪz/", "quản lý trang trại chăn nuôi"),
    ("081527", "ranchman", "noun", "/ˈræntʃmən/", "chủ trang trại hoặc thợ chăn nuôi"),
    ("081528", "rancho", "noun", "/ˈræntʃoʊ/", "chòi thợ chăn nuôi; trang trại"),
    ("081529", "rancidness", "noun", "/ˈrænsɪdnəs/", "mùi ôi thiu, vị gắt hỏng (dầu mỡ)"),
    ("081530", "rancorously", "adv", "/ˈræŋkərəsli/", "với lòng thù hận sâu sắc, cay độc"),
    ("081531", "randan", "noun", "/ˈrændən/", "thuyền ba chèo; cuộc ăn chơi ầm"),
    ("081532", "randem", "noun", "/ˈrændəm/", "cỗ xe ba ngựa kéo nối đuôi nhau"),
    ("081533", "randers", "noun", "/ˈrɑːndərz/", "thành phố cảng Randers (Đan Mạch)"),
    ("081534", "randily", "adv", "/ˈrændəli/", "dâm đãng; ồn ào thô lỗ (khẩu ngữ)"),
    ("081535", "randiness", "noun", "/ˈrændinəs/", "sự thèm muốn xác thịt, dâm đãng"),
    ("081536", "randomizes", "verb", "/ˈrændəˌmaɪzɪz/", "chọn ngẫu nhiên, phân bố ngẫu nhiên"),
    ("081537", "randomizing", "verb", "/ˈrændəˌmaɪzɪŋ/", "ngẫu nhiên hóa, sắp xếp ngẫu nhiên"),
    ("081538", "randoms", "noun", "/ˈrændəmz/", "những biến cố hoặc mẫu ngẫu nhiên"),
    ("081539", "ranged", "verb", "/reɪndʒd/", "đã dao động; đã xếp hàng; rảo bước"),
    ("081540", "ranges", "verb", "/ˈreɪndʒɪz/", "dao động, trải dài; xếp thành hàng"),
    ("081541", "rangiferoid", "adj", "/rænˈdʒɪfəˌrɔɪd/", "có nhánh sừng giống tuần lộc"),
    ("081542", "ranid", "noun", "/ˈrænɪd/", "con ếch đồng thuộc họ Ranidae"),
    ("081543", "ranidae", "noun", "/ˈrænɪˌdiː/", "họ Ếch đồng thực thụ (Ranidae)"),
    ("081544", "ranidaphobia", "noun", "/ˌrænɪdəˈfoʊbiə/", "chứng sợ ếch nhái (tâm lý học)"),
    ("081545", "raniform", "adj", "/ˈrænəˌfɔːrm/", "có hình dạng giống loài ếch"),
    ("081546", "ranine", "adj", "/ˈreɪnaɪn/", "thuộc loài ếch; vùng dưới lưỡi"),
    ("081547", "ranivorous", "adj", "/rəˈnɪvərəs/", "ăn thịt ếch nhái (động vật học)"),
    ("081548", "rankled", "verb", "/ˈræŋkəld/", "đã gây cay cú, âm ỉ bực tức mãi"),
    ("081549", "rankles", "verb", "/ˈræŋkəlz/", "gây cay cú, âm ỉ khó chịu lâu dài"),
    ("081550", "rankling", "verb", "/ˈræŋklɪŋ/", "âm ỉ bực bội, gây nhức nhối mãi"),
    ("081551", "rankly", "adv", "/ˈræŋkli/", "nồng nặc, hôi hám; trắng trợn"),
    ("081552", "rankness", "noun", "/ˈræŋknəs/", "mùi hôi nồng nặc; vẻ mọc um tùm"),
    ("081553", "ranks", "verb", "/ræŋks/", "xếp hạng, đánh giá; xếp thành hàng"),
    ("081554", "ransomer", "noun", "/ˈrænsəmər/", "người trả tiền chuộc; đấng cứu"),
    ("081555", "ransoming", "verb", "/ˈrænsəmɪŋ/", "trả tiền chuộc, chuộc tự do cho ai"),
    ("081556", "ransomless", "adj", "/ˈrænsəmləs/", "không tiền chuộc; không thể chuộc"),
    ("081557", "ransoms", "verb", "/ˈrænsəmz/", "đòi tiền chuộc; chuộc người về"),
    ("081558", "rantan", "noun", "/ˈrænˌtæn/", "tiếng đập cửa rầm; cuộc ăn chơi ầm"),
    ("081559", "ranted", "verb", "/ˈræntɪd/", "đã gào thét hung hăng, than vãn dài"),
    ("081560", "rants", "verb", "/rænts/", "gào thét dữ dội, ba hoa chê bai"),
    ("081561", "ranula", "noun", "/ˈrænjələ/", "u nang tuyến nước bọt dưới lưỡi"),
    ("081562", "ranunculales", "noun", "/rəˌnʌŋkjʊˈleɪliːz/", "bộ Mao lương (thực vật học)"),
    ("081563", "ranunculi", "noun", "/rəˈnʌŋkjəˌlaɪ/", "những cây hoa mao lương"),
    ("081564", "ranunculuses", "noun", "/rəˈnʌŋkjələsɪz/", "các loài cây hoa mao lương"),
    ("081565", "raoti", "noun", "/ˈraʊti/", "lều vải nhỏ một mái (Anh-Ấn cổ)"),
    ("081566", "raoulia", "noun", "/rɑːˈuːliə/", "chi thực vật đệm núi (Raoulia)"),
    ("081567", "rapaciously", "adv", "/rəˈpeɪʃəsli/", "một cách tham lam, hung hãn vơ vét"),
    ("081568", "rapateaceae", "noun", "/ˌræpətiˈeɪsiː/", "họ thực vật Nam Mỹ Rapateaceae"),
    ("081569", "rapeful", "adj", "/ˈreɪpfəl/", "có xu hướng cưỡng bức, bạo lực"),
    ("081570", "rapes", "noun", "/reɪps/", "những vụ cưỡng hiếp; cây cải dầu"),
    ("081571", "raphicerus", "noun", "/ˌræfəˈsɪrəs/", "chi linh dương nhỏ châu Phi"),
    ("081572", "raphidae", "noun", "/ˈræfɪˌdiː/", "họ chim cưu Dodo tuyệt chủng"),
    ("081573", "raphide", "noun", "/ˈræfaɪd/", "tinh thể hình kim oxalat (cây)"),
    ("081574", "raphidiidae", "noun", "/ˌræfɪˈdaɪɪˌdiː/", "họ Ruồi cổ dài (côn trùng học)"),
    ("081575", "raphus", "noun", "/ˈreɪfəs/", "chi chim Dodo tuyệt chủng (Raphus)"),
    ("081576", "rapidness", "noun", "/ˈræpɪdnəs/", "sự nhanh chóng, tốc độ cao"),
    ("081577", "raping", "verb", "/ˈreɪpɪŋ/", "cưỡng hiếp, xâm hại tình dục"),
    ("081578", "rapparee", "noun", "/ˌræpəˈriː/", "du kích quân cướp Ireland thế kỷ 17"),
    ("081579", "rapped", "verb", "/ræpt/", "đã gõ mạnh, đập khẽ; đã hát rap"),
    ("081580", "rappee", "noun", "/ræˈpiː/", "thuốc lá hít mũi loại đậm đặc"),
    ("081581", "rappeller", "noun", "/rəˈpɛlər/", "người leo núi đu dây xuống dốc"),
    ("081582", "rapping", "verb", "/ˈræpɪŋ/", "gõ mạnh, đập cốc cốc; hát nhạc rap"),
    ("081583", "raps", "verb", "/ræps/", "gõ mạnh; quở trách; hát nhạc rap"),
    ("081584", "raptatory", "adj", "/ˈræptəˌtɔːri/", "săn mồi bằng vuốt; hung dữ cướp bóc"),
    ("081585", "raptly", "adv", "/ˈræptli/", "say mê, chăm chú hết sức"),
    ("081586", "raptores", "noun", "/ræpˈtɔːriːz/", "nhóm chim săn mồi có móng vuốt"),
    ("081587", "raptured", "adj", "/ˈræptʃərd/", "ngây ngất, sung sướng mê ly"),
    ("081588", "raput", "noun", "/ˈrɑːdʒpʊt/", "thành viên đẳng cấp chiến binh Ấn"),
    ("081589", "rarefies", "verb", "/ˈrɛrəˌfaɪz/", "làm loãng (khí), giảm mật độ"),
    ("081590", "rarefy", "verb", "/ˈrɛrəˌfaɪ/", "làm loãng (khí), thanh lọc tinh tế"),
    ("081591", "rarefying", "verb", "/ˈrɛrəˌfaɪɪŋ/", "làm loãng (khí), giảm mật độ"),
    ("081592", "rareripe", "adj", "/ˈrɛrˌraɪp/", "chín sớm trước mùa (trái cây)"),
    ("081593", "rarify", "verb", "/ˈrɛrəˌfaɪ/", "làm loãng; làm tinh vi khó hiểu hơn"),
    ("081594", "rariora", "noun", "/ˌrɛriˈɔːrə/", "những cổ vật sách quý hiếm"),
    ("081595", "rascalion", "noun", "/rəˈskæljən/", "kẻ lưu manh, tên côn đồ vô lại"),
    ("081596", "rasorial", "adj", "/rəˈsɔːriəl/", "ưa bới đất tìm mồi (loài gà, chim)"),
    ("081597", "raspatory", "noun", "/ˈræspəˌtɔːri/", "dao nạo xương (dụng cụ phẫu thuật)"),
    ("081598", "raspberries", "noun", "/ˈræzˌbɛriz/", "những quả mâm xôi; tiếng bĩu môi"),
    ("081599", "rasped", "verb", "/ræspt/", "đã giũa; đã phát ra giọng khàn rè"),
    ("081600", "rasper", "noun", "/ˈræspər/", "cái giũa thô; người nói giọng khàn"),
    ("081601", "raspingly", "adv", "/ˈræspɪŋli/", "với âm thanh khàn rè, chói tai"),
    ("081602", "rasps", "verb", "/ræsps/", "giũa bằng giũa thô; nói khàn rè"),
]

raw = json.load(open("scratch/b37_r04_raw_p1.json"))
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
with open("scratch/b37_r04_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("b37_r04_p1 saved OK")
