import json
import re

# Batch 20 Round 4 Part 4 (096802 to 096901, 100 records)
# Fully manual cognitive translation & QA review

raw_file = "scratch/b20_r04_raw_p4.json"
out_file = "scratch/b20_r04_p4.json"

with open(raw_file, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

assert len(raw_data) == 100, f"Expected 100 records, got {len(raw_data)}"

reviewed = {
    "lex.en.100k.096802": ("oilrig", "noun", "/ˈɔɪl.rɪɡ/", "giàn khoan dầu mỏ"),
    "lex.en.100k.096803": ("oils", "verb", "/ɔɪlz/", "tra dầu mỡ; bôi trơn"),
    "lex.en.100k.096804": ("oilstone", "noun", "/ˈɔɪlˌstoʊn/", "đá mài dầu; đá mài ướt"),
    "lex.en.100k.096805": ("oilstove", "noun", "/ˈɔɪlˌstoʊv/", "bếp dầu; lò sưởi đốt dầu"),
    "lex.en.100k.096806": ("oinks", "noun", "/ɔɪŋks/", "tiếng lợn ụt ịt; tiếng eng éc"),
    "lex.en.100k.096807": ("okapia", "noun", "/oʊˈkɑː.pi.ə/", "chi hươu đùi vằn Okapia"),
    "lex.en.100k.096808": ("okapis", "noun", "/oʊˈkɑː.piːz/", "loài hươu đùi vằn Okapi"),
    "lex.en.100k.096809": ("okayama", "noun", "/ˌoʊ.kɑːˈjɑː.mə/", "tỉnh Okayama của Nhật Bản"),
    "lex.en.100k.096810": ("okazaki", "noun", "/ˌoʊ.kəˈzɑː.ki/", "đoạn Okazaki (trong sinh học)"),
    "lex.en.100k.096811": ("okenfuss", "noun", "/ˈoʊ.kən.fʊs/", "họ Okenfuss; tên người"),
    "lex.en.100k.096812": ("oldened", "verb", "/ˈoʊl.dənd/", "đã làm già đi; đã già đi"),
    "lex.en.100k.096813": ("oldening", "verb", "/ˈoʊl.dən.ɪŋ/", "làm cho già đi; đang già đi"),
    "lex.en.100k.096814": ("oldens", "verb", "/ˈoʊl.dəndz/", "trở nên già đi; làm già đi"),
    "lex.en.100k.096815": ("oldest", "adj", "/ˈoʊl.dɪst/", "già nhất; cổ nhất; lâu đời nhất"),
    "lex.en.100k.096816": ("oldishness", "noun", "/ˈoʊl.dɪʃ.nəs/", "vẻ hơi già; nét già dặn"),
    "lex.en.100k.096817": ("oldline", "adj", "/ˈoʊldˌlaɪn/", "truyền thống; bảo thủ lâu đời"),
    "lex.en.100k.096818": ("oldsquaw", "noun", "/ˈoʊldˌskwɑː/", "vịt đuôi dài Bắc Cực"),
    "lex.en.100k.096819": ("oldsters", "noun", "/ˈoʊld.stɚz/", "những người cao tuổi; người già"),
    "lex.en.100k.096820": ("oldwench", "noun", "/ˈoʊldˌwentʃ/", "loài cá nóc gai nhiệt đới"),
    "lex.en.100k.096821": ("oldwife", "noun", "/ˈoʊldˌwaɪf/", "loài vịt đuôi dài; cá nóc gai"),
    "lex.en.100k.096822": ("ole", "noun", "/ˌoʊ.elˈiː/", "liên kết và nhúng đối tượng OLE"),
    "lex.en.100k.096823": ("oleacae", "noun", "/ˌoʊ.liˈeɪ.siː/", "họ thực vật Ô-liu (cũ)"),
    "lex.en.100k.096824": ("oleaceae", "noun", "/ˌoʊ.liˈeɪ.siː/", "họ thực vật Ô-liu Oleaceae"),
    "lex.en.100k.096825": ("oleaceous", "adj", "/ˌoʊ.liˈeɪ.ʃəs/", "thuộc họ cây Ô-liu"),
    "lex.en.100k.096826": ("oleaginously", "adv", "/ˌoʊ.liˈædʒ.ə.nəs.li/", "một cách nhầy nhụa; xu nịnh"),
    "lex.en.100k.096827": ("oleaginousness", "noun", "/ˌoʊ.liˈædʒ.ə.nəs.nəs/", "tính nhẫy dầu; thói xu nịnh"),
    "lex.en.100k.096828": ("oleales", "noun", "/ˌoʊ.liˈeɪ.liːz/", "bộ Ô-liu (thực vật học)"),
    "lex.en.100k.096829": ("oleandra", "noun", "/ˌoʊ.liˈæn.drə/", "chi dương xỉ leo Oleandra"),
    "lex.en.100k.096830": ("oleandraceae", "noun", "/ˌoʊ.li.ænˈdreɪ.siː/", "họ dương xỉ Oleandraceae"),
    "lex.en.100k.096831": ("oleaster", "noun", "/ˌoʊ.liˈæs.tɚ/", "cây nhót dại; ô-liu dại"),
    "lex.en.100k.096832": ("oleate", "noun", "/ˈoʊ.li.eɪt/", "muối hoặc este axit oleic"),
    "lex.en.100k.096833": ("olecranal", "adj", "/oʊˈlek.rə.nəl/", "thuộc mỏm khuỷu tay"),
    "lex.en.100k.096834": ("olefiant", "adj", "/oʊˈlef.i.ənt/", "sinh dầu (khí etylen)"),
    "lex.en.100k.096835": ("olefine", "noun", "/ˈoʊ.lə.fɪn/", "hiđrocacbon olefin; anken"),
    "lex.en.100k.096836": ("oleic", "adj", "/oʊˈleɪ.ɪk/", "thuộc axit oleic; có từ dầu"),
    "lex.en.100k.096837": ("oleiferous", "adj", "/ˌoʊ.liˈɪf.ɚ.əs/", "chứa dầu; sinh dầu thực vật"),
    "lex.en.100k.096838": ("oleograph", "noun", "/ˈoʊ.li.əˌɡræf/", "tranh in màu giả tranh sơn dầu"),
    "lex.en.100k.096839": ("oleographic", "adj", "/ˌoʊ.li.əˈɡræf.ɪk/", "thuộc kỹ thuật in giả sơn dầu"),
    "lex.en.100k.096840": ("oleography", "noun", "/ˌoʊ.liˈɑː.ɡrə.fi/", "kỹ thuật in màu giả tranh sơn dầu"),
    "lex.en.100k.096841": ("oleometer", "noun", "/ˌoʊ.liˈɑː.mə.t̬ɚ/", "dụng cụ đo tỷ trọng dầu"),
    "lex.en.100k.096842": ("oleophilic", "adj", "/ˌoʊ.li.oʊˈfɪl.ɪk/", "ưa dầu; dễ hòa tan trong dầu"),
    "lex.en.100k.096843": ("oleoresinous", "adj", "/ˌoʊ.li.oʊˈrez.ɪn.əs/", "chứa nhựa dầu thực vật"),
    "lex.en.100k.096844": ("oleosaccharum", "noun", "/ˌoʊ.li.oʊˈsæk.ɚ.əm/", "hỗn hợp đường tinh dầu hoa quả"),
    "lex.en.100k.096845": ("oleous", "adj", "/ˈoʊ.li.əs/", "có dầu; giống như dầu nhờn"),
    "lex.en.100k.096846": ("oleum", "noun", "/ˈoʊ.li.əm/", "oleum; axit sunfuric bốc khói"),
    "lex.en.100k.096847": ("olevel", "noun", "/ˈoʊˌlev.əl/", "chứng chỉ O-level của Anh"),
    "lex.en.100k.096848": ("olfactive", "adj", "/ɑːlˈfæk.tɪv/", "thuộc về khứu giác"),
    "lex.en.100k.096849": ("olfactometer", "noun", "/ˌɑːl.fækˈtɑː.mə.t̬ɚ/", "máy đo độ nhạy khứu giác"),
    "lex.en.100k.096850": ("olfersia", "noun", "/ɑːlˈfɝː.si.ə/", "chi dương xỉ Olfersia"),
    "lex.en.100k.096851": ("olibanum", "noun", "/oʊˈlɪb.ə.nəm/", "nhựa hương trầm; nhũ hương"),
    "lex.en.100k.096852": ("olid", "adj", "/ˈoʊ.lɪd/", "có mùi hôi thối; thum thủm"),
    "lex.en.100k.096853": ("oligacanthous", "adj", "/ˌɑːl.ɪ.ɡəˈkæn.θəs/", "có ít gai; gai thưa thớt"),
    "lex.en.100k.096854": ("oligandrous", "adj", "/ˌɑːl.ɪˈɡæn.drəs/", "có ít nhị hoa"),
    "lex.en.100k.096855": ("oligarchist", "noun", "/ˈɑː.lɪ.ɡɑːr.kɪst/", "người theo phe đầu sỏ"),
    "lex.en.100k.096856": ("oligocardia", "noun", "/ˌɑːl.ɪ.ɡoʊˈkɑːr.di.ə/", "chứng tim đập chậm bất thường"),
    "lex.en.100k.096857": ("oligocarpous", "adj", "/ˌɑːl.ɪ.ɡoʊˈkɑːr.pəs/", "có ít quả; sinh ít trái"),
    "lex.en.100k.096858": ("oligochaetous", "adj", "/ˌɑːl.ɪ.ɡoʊˈkiː.t̬əs/", "thuộc lớp giun ít tơ"),
    "lex.en.100k.096859": ("oligoclase", "noun", "/ˈɑː.lɪ.ɡoʊˌkleɪs/", "khoáng vật fenspat oligoclase"),
    "lex.en.100k.096860": ("oligodactyly", "noun", "/ˌɑː.lɪ.ɡoʊˈdæk.tɪ.li/", "tật thiếu ngón bẩm sinh"),
    "lex.en.100k.096861": ("oligodendria", "noun", "/ˌɑː.lɪ.ɡoʊˈden.dri.ə/", "tế bào thần kinh đệm ít nhánh"),
    "lex.en.100k.096862": ("oligodendroglia", "noun", "/ˌɑː.lɪ.ɡoʊˌdenˈdrɑː.ɡli.ə/", "tế bào thần kinh đệm ít nhánh"),
    "lex.en.100k.096863": ("oligodontia", "noun", "/ˌɑː.lɪ.ɡoʊˈdɑːn.ʃə/", "tật bẩm sinh thiếu nhiều răng"),
    "lex.en.100k.096864": ("oligodynamic", "adj", "/ˌɑː.lɪ.ɡoʊ.daɪˈnæm.ɪk/", "kháng khuẩn bằng ion kim loại"),
    "lex.en.100k.096865": ("oligogalactia", "noun", "/ˌɑː.lɪ.ɡoʊ.ɡəˈlæk.ʃə/", "chứng thiếu sữa mẹ sau sinh"),
    "lex.en.100k.096866": ("oligogene", "noun", "/ˈɑː.lɪ.ɡoʊˌdʒiːn/", "gen đơn hiệu quả lớn"),
    "lex.en.100k.096867": ("oligogenic", "adj", "/ˌɑː.lɪ.ɡoʊˈdʒen.ɪk/", "do ít gen chi phối"),
    "lex.en.100k.096868": ("oligoglia", "noun", "/ˌɑː.lɪˈɡɑː.ɡli.ə/", "tế bào thần kinh đệm ít nhánh"),
    "lex.en.100k.096869": ("oligolectic", "adj", "/ˌɑː.lɪ.ɡoʊˈlek.tɪk/", "chỉ thu phấn từ vài loài hoa"),
    "lex.en.100k.096870": ("oligomenorrhea", "noun", "/ˌɑː.lɪ.ɡoʊˌmen.əˈriː.ə/", "chứng thiểu kinh; kinh nguyệt thưa"),
    "lex.en.100k.096871": ("oligomer", "noun", "/əˈlɪɡ.ə.mɚ/", "chất polime mạch ngắn oligomer"),
    "lex.en.100k.096872": ("oligomeric", "adj", "/ˌɑː.lɪ.ɡoʊˈmer.ɪk/", "thuộc cấu trúc oligomer"),
    "lex.en.100k.096873": ("oligomerous", "adj", "/ˌɑː.lɪˈɡɑː.mɚ.əs/", "có ít bộ phận; cấu trúc giảm"),
    "lex.en.100k.096874": ("oligomonorrhea", "noun", "/ˌɑː.lɪ.ɡoʊˌmɑː.nəˈriː.ə/", "chứng kinh nguyệt thưa thớt"),
    "lex.en.100k.096875": ("oligonervous", "adj", "/ˌɑː.lɪ.ɡoʊˈnɝː.vəs/", "có ít gân lá; gân thưa"),
    "lex.en.100k.096876": ("oligophagous", "adj", "/ˌɑː.lɪˈɡɑː.fə.ɡəs/", "chỉ ăn một số ít loại thức ăn"),
    "lex.en.100k.096877": ("oligophagy", "noun", "/ˌɑː.lɪˈɡɑː.fə.dʒi/", "tính chỉ ăn số ít loại thức ăn"),
    "lex.en.100k.096878": ("oligophiletic", "adj", "/ˌɑː.lɪ.ɡoʊ.fɪˈlet̬.ɪk/", "bắt nguồn từ vài dạng tổ tiên"),
    "lex.en.100k.096879": ("oligophyllous", "adj", "/ˌɑː.lɪ.ɡoʊˈfɪl.əs/", "có ít lá; thưa thớt lá"),
    "lex.en.100k.096880": ("oligoplites", "noun", "/ˌɑː.lɪ.ɡoʊˈplaɪ.tiːz/", "chi cá thu da da Oligoplites"),
    "lex.en.100k.096881": ("oligopod", "adj", "/ˈɑː.lɪ.ɡoʊ.pɑːd/", "có ít chân (ở ấu trùng)"),
    "lex.en.100k.096882": ("oligopolistic", "adj", "/ˌɑː.lɪ.ɡə.pəˈlɪs.tɪk/", "thuộc thế độc quyền nhóm bán"),
    "lex.en.100k.096883": ("oligoporus", "noun", "/ˌɑː.lɪˈɡɑː.pɚ.əs/", "chi nấm lỗ Oligoporus"),
    "lex.en.100k.096884": ("oligopsony", "noun", "/ˌɑː.lɪˈɡɑːp.sə.ni/", "thị trường độc quyền nhóm mua"),
    "lex.en.100k.096885": ("oligopyrene", "adj", "/ˌɑː.lɪ.ɡoʊˈpaɪ.riːn/", "có ít hạch con; ít nhân"),
    "lex.en.100k.096886": ("oligosomal", "adj", "/ˌɑː.lɪ.ɡoʊˈsoʊ.məl/", "có ít nhiễm sắc thể"),
    "lex.en.100k.096887": ("oligospermatism", "noun", "/ˌɑː.lɪ.ɡoʊˈspɝː.mə.tɪ.zəm/", "chứng ít tinh trùng ở nam giới"),
    "lex.en.100k.096888": ("oligospermous", "adj", "/ˌɑː.lɪ.ɡoʊˈspɝː.məs/", "có ít hạt; ít tinh trùng"),
    "lex.en.100k.096889": ("oligosporous", "adj", "/ˌɑː.lɪˈɡɑː.spɚ.əs/", "có ít bào tử; thưa bào tử"),
    "lex.en.100k.096890": ("oligothermic", "adj", "/ˌɑː.lɪ.ɡoʊˈθɝː.mɪk/", "chịu được nhiệt độ thấp"),
    "lex.en.100k.096891": ("oligotrophic", "adj", "/ˌɑː.lɪ.ɡoʊˈtroʊ.fɪk/", "nghèo dinh dưỡng (hồ nước, đất)"),
    "lex.en.100k.096892": ("oliguresis", "noun", "/ˌɑː.lɪ.ɡjʊˈriː.sɪs/", "chứng thiểu niệu; ít nước tiểu"),
    "lex.en.100k.096893": ("olimbos", "noun", "/ˈoʊ.lɪm.bəs/", "núi Olympus tại Hy Lạp"),
    "lex.en.100k.096894": ("olio", "noun", "/ˈoʊ.li.oʊ/", "món thịt thập cẩm; mớ hỗn độn"),
    "lex.en.100k.096895": ("oliva", "noun", "/oʊˈlaɪ.və/", "thể trám hành não; chi ốc trám"),
    "lex.en.100k.096896": ("olivaceous", "adj", "/ˌɑː.lɪˈveɪ.ʃəs/", "có màu xanh ô-liu; lục xám"),
    "lex.en.100k.096897": ("olivacious", "adj", "/ˌɑː.lɪˈveɪ.ʃəs/", "có màu xanh ô-liu"),
    "lex.en.100k.096898": ("olivary", "adj", "/ˈɑː.lɪ.ver.i/", "có hình quả ô-liu; thuộc thể trám"),
    "lex.en.100k.096899": ("olivelike", "adj", "/ˈɑː.lɪv.laɪk/", "có hình dạng như quả ô-liu"),
    "lex.en.100k.096900": ("olivenit", "noun", "/ˈɑː.lɪ.və.naɪt/", "khoáng vật olivenit arsenat"),
    "lex.en.100k.096901": ("olivenite", "noun", "/ˈɑː.lɪ.və.naɪt/", "khoáng vật olivenit màu ô-liu"),
}

VALID_POS = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}

processed = []
for item in raw_data:
    item_id = item["id"]
    assert item_id in reviewed, f"Missing id: {item_id}"
    hw, pos, ipa, vi = reviewed[item_id]
    
    assert hw == item["hw"], f"HW mismatch: {hw} vs {item['hw']}"
    assert pos in VALID_POS, f"Invalid POS: {pos}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Invalid IPA: {ipa}"
    assert len(vi) <= 35, f"Vietnamese text too long ({len(vi)} chars): '{vi}'"
    assert not re.search(r"(Số nhiều của|Xem|Dạng|Viết tắt|Động từ chia|%%)", vi), f"Crawler artifact in vi: '{vi}'"

    new_item = {
        "id": item["id"],
        "hw": item["hw"],
        "pos": pos,
        "ipa": ipa,
        "vi": vi,
        "cefr": item["cefr"],
        "tier": item["tier"],
        "status": "reviewed",
        "notes": item["notes"],
    }
    processed.append(new_item)

with open(out_file, "w", encoding="utf-8") as f:
    json.dump(processed, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(processed)} items to {out_file}")
