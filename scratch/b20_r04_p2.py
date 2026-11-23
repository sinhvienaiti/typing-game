import json
import re

# Batch 20 Round 4 Part 2 (096602 to 096701, 100 records)
# Fully manual cognitive translation & QA review

raw_file = "scratch/b20_r04_raw_p2.json"
out_file = "scratch/b20_r04_p2.json"

with open(raw_file, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

assert len(raw_data) == 100, f"Expected 100 records, got {len(raw_data)}"

# Manual review dictionary
reviewed = {
    "lex.en.100k.096602": ("octaploid", "adj", "/ˈɑːk.tə.plɔɪd/", "bát bội; có tám bộ nhiễm sắc thể"),
    "lex.en.100k.096603": ("octarch", "adj", "/ˈɑːk.tɑːrk/", "có tám bó mạch"),
    "lex.en.100k.096604": ("octarchy", "noun", "/ˈɑːk.tɑːr.ki/", "chính thể tám người; bát đầu chế"),
    "lex.en.100k.096605": ("octaroon", "noun", "/ˌɑːk.təˈruːn/", "người có một phần tám máu da đen"),
    "lex.en.100k.096606": ("octastyle", "adj", "/ˈɑːk.təˌstaɪl/", "có tám cột mặt tiền"),
    "lex.en.100k.096607": ("octateuch", "noun", "/ˈɑːk.tə.tuːk/", "tám cuốn đầu Kinh Cựu ước"),
    "lex.en.100k.096608": ("octavalent", "adj", "/ˌɑːk.təˈveɪ.lənt/", "có hóa trị tám"),
    "lex.en.100k.096609": ("octennial", "adj", "/ɑːkˈten.i.əl/", "kéo dài tám năm; tám năm một lần"),
    "lex.en.100k.096610": ("octennially", "adv", "/ɑːkˈten.i.ə.li/", "mỗi tám năm một lần"),
    "lex.en.100k.096611": ("octette", "noun", "/ɑːkˈtet/", "bộ tám; bản nhạc cho tám người"),
    "lex.en.100k.096612": ("octillion", "noun", "/ɑːkˈtɪl.jən/", "nghìn triệu triệu triệu triệu"),
    "lex.en.100k.096613": ("octingentenary", "noun", "/ˌɑːk.tɪn.dʒenˈten.ər.i/", "lễ kỷ niệm tám trăm năm"),
    "lex.en.100k.096614": ("octobrist", "noun", "/ɑːkˈtoʊ.brɪst/", "thành viên đảng Tháng Mười"),
    "lex.en.100k.096615": ("octocentenary", "noun", "/ˌɑːk.toʊ.senˈten.ər.i/", "lễ kỷ niệm tám trăm năm"),
    "lex.en.100k.096616": ("octocentennial", "noun", "/ˌɑːk.toʊ.senˈten.i.əl/", "lễ kỷ niệm tám trăm năm"),
    "lex.en.100k.096617": ("octode", "noun", "/ˈɑːk.toʊd/", "đèn điện tử tám cực"),
    "lex.en.100k.096618": ("octodecimo", "noun", "/ˌɑːk.toʊˈdes.ɪ.moʊ/", "khổ sách gấp mười tám"),
    "lex.en.100k.096619": ("octogynous", "adj", "/ɑːkˈtɑː.dʒə.nəs/", "có tám vòi nhụy; tám nhụy"),
    "lex.en.100k.096620": ("octolateral", "adj", "/ˌɑːk.toʊˈlæt̬.ɚ.əl/", "có tám cạnh; tám mặt"),
    "lex.en.100k.096621": ("octonal", "adj", "/ˈɑːk.tə.nəl/", "thuộc cơ số tám; hệ bát phân"),
    "lex.en.100k.096622": ("octonarian", "adj", "/ˌɑːk.təˈner.i.ən/", "có tám âm tiết; thuộc câu tám âm"),
    "lex.en.100k.096623": ("octonary", "noun", "/ˈɑːk.təˌner.i/", "nhóm tám; thể thơ tám âm tiết"),
    "lex.en.100k.096624": ("octonocular", "adj", "/ˌɑːk.təˈnɑː.kjə.lɚ/", "có tám con mắt"),
    "lex.en.100k.096625": ("octopetalous", "adj", "/ˌɑːk.toʊˈpet̬.əl.əs/", "có tám cánh hoa"),
    "lex.en.100k.096626": ("octopoda", "noun", "/ɑːkˈtɑː.pə.də/", "bộ Bạch tuộc"),
    "lex.en.100k.096627": ("octopodidae", "noun", "/ˌɑːk.təˈpɑː.dɪ.diː/", "họ Bạch tuộc Octopodidae"),
    "lex.en.100k.096628": ("octopodous", "adj", "/ɑːkˈtɑː.pə.dəs/", "có tám chân; thuộc bộ bạch tuộc"),
    "lex.en.100k.096629": ("octoradiate", "adj", "/ˌɑːk.toʊˈreɪ.di.ət/", "có tám tia; tỏa tám nhánh"),
    "lex.en.100k.096630": ("octosepalous", "adj", "/ˌɑːk.toʊˈsep.əl.əs/", "có tám lá đài"),
    "lex.en.100k.096631": ("octosporous", "adj", "/ɑːkˈtɑː.spɚ.əs/", "có tám bào tử"),
    "lex.en.100k.096632": ("octostyle", "noun", "/ˈɑːk.təˌstaɪl/", "hàng hiên tám cột; dãy tám cột"),
    "lex.en.100k.096633": ("octosyllable", "noun", "/ˌɑːk.toʊˈsɪl.ə.bəl/", "từ tám âm tiết; câu thơ tám âm"),
    "lex.en.100k.096634": ("ocularist", "noun", "/ˈɑː.kjə.lɚ.ɪst/", "chuyên viên làm mắt giả"),
    "lex.en.100k.096635": ("ocularly", "adv", "/ˈɑː.kjə.lɚ.li/", "bằng mắt; bằng thị giác"),
    "lex.en.100k.096636": ("oculat", "adj", "/ˈɑː.kjə.lət/", "có mắt đơn; có đốm mắt"),
    "lex.en.100k.096637": ("oculated", "adj", "/ˈɑː.kjə.leɪ.t̬ɪd/", "có mắt đơn; có đốm hình mắt"),
    "lex.en.100k.096638": ("oculi", "noun", "/ˈɑː.kjə.laɪ/", "các lỗ tròn; các cửa sổ tròn"),
    "lex.en.100k.096639": ("oculiferous", "adj", "/ˌɑː.kjəˈlɪf.ɚ.əs/", "có mang mắt; có cơ quan thị giác"),
    "lex.en.100k.096640": ("oculiform", "adj", "/ˈɑː.kjə.ləˌfɔːrm/", "có hình mắt; dạng mắt"),
    "lex.en.100k.096641": ("oculism", "noun", "/ˈɑː.kjə.lɪ.zəm/", "khoa mắt; ngành nhãn khoa cổ"),
    "lex.en.100k.096642": ("oculistic", "adj", "/ˌɑː.kjəˈlɪs.tɪk/", "thuộc nhãn khoa; thuộc khoa mắt"),
    "lex.en.100k.096643": ("oculists", "noun", "/ˈɑː.kjə.lɪsts/", "các bác sĩ chuyên khoa mắt"),
    "lex.en.100k.096644": ("ocyurus", "noun", "/ˌɒs.iˈjʊər.əs/", "chi cá hồng đuôi vàng Ocyurus"),
    "lex.en.100k.096645": ("oddfellow", "noun", "/ˈɑːdˌfel.oʊ/", "hội viên hội tương tế Odd Fellows"),
    "lex.en.100k.096646": ("oddment", "noun", "/ˈɑːd.mənt/", "mảnh vụn thừa; đồ lặt vặt"),
    "lex.en.100k.096647": ("odea", "noun", "/oʊˈdiː.ə/", "các nhà hát cổ Hy Lạp; phòng nhạc"),
    "lex.en.100k.096648": ("odeum", "noun", "/oʊˈdiː.əm/", "nhà hát Hy Lạp cổ; phòng hòa nhạc"),
    "lex.en.100k.096649": ("odevity", "noun", "/ˈoʊ.də.vɪ.ti/", "tính chẵn lẻ"),
    "lex.en.100k.096650": ("odic", "adj", "/ˈoʊ.dɪk/", "thuộc bài ca tụng; tụng thi"),
    "lex.en.100k.096651": ("odiousness", "noun", "/ˈoʊ.di.əs.nəs/", "sự đáng ghét; tính đáng ghê tởm"),
    "lex.en.100k.096652": ("odist", "noun", "/ˈoʊ.dɪst/", "nhà thơ sáng tác bài tụng ca"),
    "lex.en.100k.096653": ("odobenidae", "noun", "/ˌoʊ.dəˈben.ɪ.diː/", "họ Hải mã Odobenidae"),
    "lex.en.100k.096654": ("odobenus", "noun", "/ˌoʊ.dəˈbiː.nəs/", "chi Hải mã Odobenus"),
    "lex.en.100k.096655": ("odograph", "noun", "/ˈoʊ.də.ɡræf/", "máy ghi hành trình; máy ghi đường"),
    "lex.en.100k.096656": ("odometers", "noun", "/oʊˈdɑː.mə.t̬ɚz/", "các đồng hồ đo quãng đường"),
    "lex.en.100k.096657": ("odonate", "noun", "/ˈoʊ.də.neɪt/", "loài chuồn chuồn bộ Odonata"),
    "lex.en.100k.096658": ("odontalgia", "noun", "/ˌoʊ.dɑːnˈtæl.dʒə/", "chứng đau răng; cơn đau răng"),
    "lex.en.100k.096659": ("odontalgic", "adj", "/ˌoʊ.dɑːnˈtæl.dʒɪk/", "thuộc chứng đau răng; trị đau răng"),
    "lex.en.100k.096660": ("odontaspididae", "noun", "/ˌoʊ.dɑːn.tæˈspɪd.ɪ.diː/", "họ cá mập cát Odontaspididae"),
    "lex.en.100k.096661": ("odontaspis", "noun", "/ˌoʊ.dɑːnˈtæ.spɪs/", "chi cá mập cát Odontaspis"),
    "lex.en.100k.096662": ("odontiasis", "noun", "/ˌoʊ.dɑːnˈtaɪ.ə.sɪs/", "quá trình mọc răng sữa"),
    "lex.en.100k.096663": ("odontic", "adj", "/oʊˈdɑːn.tɪk/", "thuộc về răng; thuộc nha khoa"),
    "lex.en.100k.096664": ("odontist", "noun", "/oʊˈdɑːn.tɪst/", "nha sĩ; thầy thuốc chữa răng"),
    "lex.en.100k.096665": ("odontoblast", "noun", "/oʊˈdɑːn.tə.blæst/", "nguyên bào tạo ngà răng"),
    "lex.en.100k.096666": ("odontoblastic", "adj", "/ˌoʊ.dɑːn.təˈblæs.tɪk/", "thuộc nguyên bào tạo ngà"),
    "lex.en.100k.096667": ("odontobothrion", "noun", "/ˌoʊ.dɑːn.toʊˈbɑː.θri.ɑːn/", "huyệt răng; lỗ chân răng"),
    "lex.en.100k.096668": ("odontoceti", "noun", "/ˌoʊ.dɑːn.toʊˈseɪ.ti/", "phân bộ Cá voi có răng"),
    "lex.en.100k.096669": ("odontoclast", "noun", "/oʊˈdɑːn.tə.klæst/", "hủy cốt bào ngà răng"),
    "lex.en.100k.096670": ("odontogeny", "noun", "/ˌoʊ.dɑːnˈtɑː.dʒə.ni/", "quá trình phát triển răng"),
    "lex.en.100k.096671": ("odontoid", "adj", "/oʊˈdɑːn.tɔɪd/", "có dạng răng; hình răng"),
    "lex.en.100k.096672": ("odontolith", "noun", "/oʊˈdɑːn.tə.lɪθ/", "cao răng; vôi răng"),
    "lex.en.100k.096673": ("odontological", "adj", "/ˌoʊ.dɑːn.təˈlɑː.dʒɪk.əl/", "thuộc nha khoa học"),
    "lex.en.100k.096674": ("odontologist", "noun", "/ˌoʊ.dɑːnˈtɑː.lə.dʒɪst/", "bác sĩ nha khoa; chuyên gia răng"),
    "lex.en.100k.096675": ("odontophore", "noun", "/oʊˈdɑːn.tə.fɔːr/", "khối nâng lưỡi gai thân mềm"),
    "lex.en.100k.096676": ("odontophorus", "noun", "/ˌoʊ.dɑːnˈtɑː.fɚ.əs/", "chi chim cút Tân Thế giới"),
    "lex.en.100k.096677": ("odontoplast", "noun", "/oʊˈdɑːn.tə.plæst/", "nguyên bào tạo ngà răng"),
    "lex.en.100k.096678": ("odontorrhagia", "noun", "/ˌoʊ.dɑːn.toʊˈreɪ.dʒə/", "chảy máu chân răng nặng"),
    "lex.en.100k.096679": ("odontoscope", "noun", "/oʊˈdɑːn.tə.skoʊp/", "gương khám răng; kính soi răng"),
    "lex.en.100k.096680": ("odorant", "noun", "/ˈoʊ.dɚ.ənt/", "chất tạo mùi; hương liệu"),
    "lex.en.100k.096681": ("odoriferously", "adv", "/ˌoʊ.dəˈrɪf.ɚ.əs.li/", "một cách ngát hương thơm"),
    "lex.en.100k.096682": ("odoriferousness", "noun", "/ˌoʊ.dəˈrɪf.ɚ.əs.nəs/", "sự ngát hương; tính thơm tho"),
    "lex.en.100k.096683": ("odorise", "verb", "/ˈoʊ.də.raɪz/", "thêm mùi; tạo mùi thơm"),
    "lex.en.100k.096684": ("odorize", "verb", "/ˈoʊ.də.raɪz/", "tạo mùi hương; làm cho có mùi"),
    "lex.en.100k.096685": ("odorously", "adv", "/ˈoʊ.dɚ.əs.li/", "một cách thơm ngát; đượm hương"),
    "lex.en.100k.096686": ("odorousness", "noun", "/ˈoʊ.dɚ.əs.nəs/", "hương thơm ngát; mùi thơm"),
    "lex.en.100k.096687": ("odourise", "verb", "/ˈoʊ.dɚ.aɪz/", "thêm chất tạo mùi; làm có mùi"),
    "lex.en.100k.096688": ("odovacar", "noun", "/ˌoʊ.doʊˈveɪ.kɚ/", "thủ lĩnh Odoacer của Ý"),
    "lex.en.100k.096689": ("odovakar", "noun", "/ˌoʊ.doʊˈvæ.kɚ/", "thủ lĩnh Odoacer"),
    "lex.en.100k.096690": ("odynophagia", "noun", "/ˌoʊ.dɪ.noʊˈfeɪ.dʒə/", "chứng nuốt đau"),
    "lex.en.100k.096691": ("oecanthus", "noun", "/iːˈkæn.θəs/", "chi dế cây Oecanthus"),
    "lex.en.100k.096692": ("oecisis", "noun", "/iːˈsɪs.ɪs/", "sự định cư quần lạc sinh vật"),
    "lex.en.100k.096693": ("oecist", "noun", "/ˈiː.sɪst/", "người lập thuộc địa Hy Lạp cổ"),
    "lex.en.100k.096694": ("oecium", "noun", "/ˈiː.si.əm/", "túi ấp rêu biển bọt"),
    "lex.en.100k.096695": ("oecoid", "noun", "/ˈiː.kɔɪd/", "khung nâng đỡ hồng cầu"),
    "lex.en.100k.096696": ("oecological", "adj", "/ˌiː.kəˈlɑː.dʒɪk.əl/", "thuộc về sinh thái học"),
    "lex.en.100k.096697": ("oecology", "noun", "/iːˈkɑː.lə.dʒi/", "sinh thái học"),
    "lex.en.100k.096698": ("oecumenic", "adj", "/ˌek.jʊˈmen.ɪk/", "thuộc đại kết tôn giáo; phổ quát"),
    "lex.en.100k.096699": ("oecumenicity", "noun", "/ˌek.jʊ.məˈnɪs.ɪ.ti/", "tính đại kết; tính phổ quát chung"),
    "lex.en.100k.096700": ("oecumenism", "noun", "/ˌek.jʊˈmen.ɪ.zəm/", "phong trào đại kết Ki-tô giáo"),
    "lex.en.100k.096701": ("oecusse", "noun", "/oʊ.eɪˈkuː.seɪ/", "đặc khu Oecusse của Đông Timor"),
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
