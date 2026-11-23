import json

RECORDS = [
    ("087503", "sliter", "noun", "/ˈslaɪtər/", "người xẻ rãnh; dao rạch cắt"),
    ("087504", "slithered", "verb", "/ˈslɪðərd/", "đã trườn lướt; đã trượt êm"),
    ("087505", "slithers", "verb", "/ˈslɪðərz/", "trườn lướt; trượt ngoằn ngoèo"),
    ("087506", "slits", "verb", "/slɪts/", "rạch dài; xẻ khe hẹp; cắt xẻ"),
    ("087507", "slitted", "verb", "/ˈslɪtɪd/", "đã rạch khe; đã xẻ rãnh hẹp"),
    ("087508", "slitter", "noun", "/ˈslɪtər/", "máy cắt xẻ cuộn; dao rạch"),
    ("087509", "slitting", "verb", "/ˈslɪtɪŋ/", "đang rạch dài; đang xẻ khe"),
    ("087510", "slivered", "verb", "/ˈslɪvərd/", "đã tước mảnh nhỏ; đã chẻ dăm"),
    ("087511", "sliverer", "noun", "/ˈslɪvərər/", "người chẻ mảnh; máy tước sợi"),
    ("087512", "slivering", "verb", "/ˈslɪvərɪŋ/", "đang tước mảnh nhỏ; đang chẻ dăm"),
    ("087513", "slivers", "verb", "/ˈslɪvərz/", "tước thành mảnh nhỏ; chẻ dăm"),
    ("087514", "slivery", "adj", "/ˈslɪvəri/", "lởm chởm dăm nhọn; mảnh dẻ"),
    ("087515", "sloam", "noun", "/sloʊm/", "lớp đất sét mềm giữa vỉa than"),
    ("087516", "sloan", "noun", "/sloʊn/", "tên họ Sloan"),
    ("087517", "sloane", "noun", "/sloʊn/", "tiểu thư thượng lưu sành điệu Anh"),
    ("087518", "sloanea", "noun", "/sloʊˈniːə/", "chi cây gỗ cứng Sloanea"),
    ("087519", "slobbered", "verb", "/ˈslɑːbərd/", "đã chảy nước dãi; nói sướt mướt"),
    ("087520", "slobberer", "noun", "/ˈslɑːbərər/", "người hay chảy dãi; kẻ sướt mướt"),
    ("087521", "slobberiness", "noun", "/ˈslɑːbərinəs/", "tình trạng chảy dãi nhớp nháp"),
    ("087522", "slobbering", "verb", "/ˈslɑːbərɪŋ/", "đang chảy nước dãi; đang nức nở"),
    ("087523", "slobbers", "verb", "/ˈslɑːbərz/", "chảy nước dãi; biểu lộ sướt mướt"),
    ("087524", "slobbery", "adj", "/ˈslɑːbəri/", "đầy nước dãi; sướt mướt giả tạo"),
    ("087525", "sloganeer", "noun", "/ˌsloʊɡəˈnɪr/", "người chuyên nghĩ khẩu hiệu"),
    ("087526", "sloganise", "verb", "/ˈsloʊɡəˌnaɪz/", "đặt khẩu hiệu; tuyên truyền bằng câu"),
    ("087527", "sloganize", "verb", "/ˈsloʊɡəˌnaɪz/", "đặt khẩu hiệu; biến thành khẩu hiệu"),
    ("087528", "sloganizer", "noun", "/ˈsloʊɡəˌnaɪzər/", "người chuyên đặt khẩu hiệu"),
    ("087529", "sloid", "noun", "/slɔɪd/", "phương pháp giáo dục thủ công gỗ"),
    ("087530", "slojd", "noun", "/slɔɪd/", "phương pháp giáo dục thủ công gỗ"),
    ("087531", "sloot", "noun", "/sluːt/", "mương thoát nước; khe rãnh xói"),
    ("087532", "slopes", "verb", "/sloʊps/", "dốc nghiêng; chuồn đi lén lút"),
    ("087533", "slopewise", "adv", "/ˈsloʊpˌwaɪz/", "theo hướng nghiêng dốc"),
    ("087534", "slopingly", "adv", "/ˈsloʊpɪŋli/", "dốc nghiêng thoai thoải"),
    ("087535", "slopping", "verb", "/ˈslɑːpɪŋ/", "đang làm sánh đổ nước; lội bùn"),
    ("087536", "slopseller", "noun", "/ˈslɑːpˌsɛlər/", "người bán quần áo may sẵn rẻ tiền"),
    ("087537", "slopshing", "noun", "/ˈslɑːʃɪŋ/", "tiếng sóng vỗ dập dềnh"),
    ("087538", "slopshop", "noun", "/ˈslɑːpˌʃɑːp/", "cửa hàng bán đồ may sẵn rẻ tiền"),
    ("087539", "slopwork", "noun", "/ˈslɑːpˌwɜːrk/", "nghề may quần áo rẻ tiền; việc ẩu"),
    ("087540", "sloshes", "verb", "/ˈslɑːʃɪz/", "té nước ào ào; lội bì bõm"),
    ("087541", "sloshing", "verb", "/ˈslɑːʃɪŋ/", "đang té nước; đang sánh qua lại"),
    ("087542", "slothfully", "adv", "/ˈslɔːθfəli/", "lười biếng; uể oải chậm chạp"),
    ("087543", "slots", "verb", "/slɑːts/", "nhét vào khe; xếp vừa vào chỗ"),
    ("087544", "slotted", "verb", "/ˈslɑːtɪd/", "đã nhét vào khe; đã xếp đúng chỗ"),
    ("087545", "slotter", "noun", "/ˈslɑːtər/", "máy xọc rãnh then"),
    ("087546", "slotting", "verb", "/ˈslɑːtɪŋ/", "đang nhét vào khe; đang xọc rãnh"),
    ("087547", "slouched", "verb", "/slaʊtʃt/", "đã ngồi thõng vai; đi khom lưng"),
    ("087548", "sloucher", "noun", "/ˈslaʊtʃər/", "người đi khom lưng uể oải"),
    ("087549", "slouches", "verb", "/ˈslaʊtʃɪz/", "ngồi thõng vai; đi khom lưng"),
    ("087550", "slouchily", "adv", "/ˈslaʊtʃɪli/", "khom lưng rũ rượi; uể oải"),
    ("087551", "slouchiness", "noun", "/ˈslaʊtʃinəs/", "dáng điệu thõng vai uể oải"),
    ("087552", "slouching", "verb", "/ˈslaʊtʃɪŋ/", "đang ngồi thõng vai; đi khom lưng"),
    ("087553", "slouchingly", "adv", "/ˈslaʊtʃɪŋli/", "với dáng đi khom lưng uể oải"),
    ("087554", "sloughed", "verb", "/slʌft/", "đã lột xác; đã bong tróc vảy"),
    ("087555", "sloughs", "verb", "/slʌfs/", "lột xác; bong tróc lớp da chết"),
    ("087556", "sloughy", "adj", "/ˈslaʊi/", "lầy lội sình lầy; có mô hoại tử"),
    ("087557", "slovenija", "noun", "/sloʊˈviːnjə/", "nước Slovenia (tên bản địa)"),
    ("087558", "slowback", "noun", "/ˈsloʊˌbæk/", "người chậm chạp lười biếng"),
    ("087559", "slowcoach", "noun", "/ˈsloʊˌkoʊtʃ/", "người chậm chạp lề mề (lóng Anh)"),
    ("087560", "slowgoing", "adj", "/ˈsloʊˌɡoʊɪŋ/", "chậm chạp; thủng thẳng không vội"),
    ("087561", "slowworm", "noun", "/ˈsloʊˌwɜːrm/", "thằn lằn rắn không chân châu Âu"),
    ("087562", "sloyd", "noun", "/slɔɪd/", "phương pháp giáo dục thủ công gỗ"),
    ("087563", "slr", "noun", "/ˌɛsˌɛlˈɑːr/", "máy ảnh phản xạ ống kính đơn SLR"),
    ("087564", "slubbed", "adj", "/slʌbd/", "có nút sợi sần (vải dệt)"),
    ("087565", "slubber", "verb", "/ˈslʌbər/", "làm nhòe bẩn; kéo sợi thô"),
    ("087566", "slubberingly", "adv", "/ˈslʌbərɪŋli/", "cẩu thả qua loa; nhem nhuốc"),
    ("087567", "slubbing", "noun", "/ˈslʌbɪŋ/", "sợi thô se nhẹ trước khi kéo nhỏ"),
    ("087568", "sludger", "noun", "/ˈslʌdʒər/", "máy bơm hút bùn sệt; gầu nạo bùn"),
    ("087569", "sludgy", "adj", "/ˈslʌdʒi/", "đầy bùn sệt; lầy lội nhớp nháp"),
    ("087570", "slued", "verb", "/sluːd/", "đã xoay ngoắt sang một bên"),
    ("087571", "slues", "verb", "/sluːz/", "xoay ngoắt sang bên; trượt ngang"),
    ("087572", "sluff", "noun", "/slʌf/", "vùng lầy bùn; lớp da rắn lột"),
    ("087573", "slugabed", "noun", "/ˈslʌɡəˌbɛd/", "người lười hay nằm nướng buổi sáng"),
    ("087574", "sluggardly", "adv", "/ˈslʌɡərdli/", "lười biếng chậm chạp"),
    ("087575", "sluggards", "noun", "/ˈslʌɡərdz/", "người lười nhác chậm chạp"),
    ("087576", "slugged", "verb", "/slʌɡd/", "đã đấm mạnh; đã đánh bóng cực mạnh"),
    ("087577", "slugging", "verb", "/ˈslʌɡɪŋ/", "đang đấm mạnh; đang đánh cực mạnh"),
    ("087578", "slugs", "verb", "/slʌɡz/", "đấm mạnh; nốc cạn ly; đánh bóng"),
    ("087579", "sluiced", "verb", "/sluːst/", "đã xả nước rửa trôi; mở cửa cống"),
    ("087580", "sluicegate", "noun", "/ˈsluːsˌɡeɪt/", "cửa cống xả nước; van đập"),
    ("087581", "sluices", "verb", "/ˈsluːsɪz/", "xả nước xối mạnh; đãi vàng"),
    ("087582", "sluiceway", "noun", "/ˈsluːsˌweɪ/", "kênh dẫn nước qua cửa cống"),
    ("087583", "sluing", "verb", "/ˈsluːɪŋ/", "đang xoay ngoắt; đang trượt ngang"),
    ("087584", "sluit", "noun", "/sluːt/", "mương xói mòn; kênh cạn (Nam Phi)"),
    ("087585", "slumbered", "verb", "/ˈslʌmbərd/", "đã ngủ thiếp đi; đã ngủ yên"),
    ("087586", "slumberer", "noun", "/ˈslʌmbərər/", "người đang ngủ say"),
    ("087587", "slumbering", "verb", "/ˈslʌmbərɪŋ/", "đang ngủ yên; đang ngủ say"),
    ("087588", "slumberingly", "adv", "/ˈslʌmbərɪŋli/", "êm đềm như đang say ngủ"),
    ("087589", "slumberous", "adj", "/ˈslʌmbərəs/", "yên ả; êm đềm buồn ngủ"),
    ("087590", "slumbers", "verb", "/ˈslʌmbərz/", "ngủ say; ngủ yên tĩnh lặng"),
    ("087591", "slumbery", "adj", "/ˈslʌmbəri/", "buồn ngủ; uể oải thiu thiu"),
    ("087592", "slumbrous", "adj", "/ˈslʌmbrəs/", "yên ả tĩnh mịch; gây buồn ngủ"),
    ("087593", "slumdom", "noun", "/ˈslʌmdəm/", "khu nhà ổ chuột; cảnh sống nghèo"),
    ("087594", "slumgullion", "noun", "/slʌmˈɡʌljən/", "món thịt hầm thập cẩm loãng"),
    ("087595", "slumlord", "noun", "/ˈslʌmˌlɔːrd/", "chủ cho thuê nhà ổ chuột tồi tàn"),
    ("087596", "slumlords", "noun", "/ˈslʌmˌlɔːrdz/", "chủ cho thuê nhà ổ chuột tồi tàn"),
    ("087597", "slummed", "verb", "/slʌmd/", "đã trải nghiệm cảnh sống nghèo"),
    ("087598", "slummer", "noun", "/ˈslʌmər/", "người thích đi thăm khu ổ chuột"),
    ("087599", "slumming", "verb", "/ˈslʌmɪŋ/", "đang trải nghiệm cuộc sống bình dân"),
    ("087600", "slummock", "verb", "/ˈslʌmək/", "ăn ngấu nghiến; đi lệt xệt cẩu thả"),
    ("087601", "slumped", "verb", "/slʌmpt/", "đã sụt giảm mạnh; đã ngồi sụp"),
    ("087602", "slumping", "verb", "/ˈslʌmpɪŋ/", "đang sụt giảm mạnh; đang ngồi sụp"),
]

# Shorten 087526 and 087599 cleanly <= 35
RECORDS[23] = ("087526", "sloganise", "verb", "/ˈsloʊɡəˌnaɪz/", "đặt khẩu hiệu; nêu khẩu hiệu")
RECORDS[96] = ("087599", "slumming", "verb", "/ˈslʌmɪŋ/", "đang trải nghiệm đời bình dân")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r06_raw_p1.json"))
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

json.dump(out, open("scratch/b38_r06_reviewed_p1.json", "w"), ensure_ascii=False, indent=2)
print("b38_r06_p1 saved OK")
