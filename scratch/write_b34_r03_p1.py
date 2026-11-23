import json

items = [
    ("066003", "hypercalcemias", "noun", "/ˌhaɪpərkælˈsiːmiəz/", "tình trạng tăng canxi trong máu"),
    ("066004", "hypotonias", "noun", "/ˌhaɪpəˈtoʊniəz/", "tình trạng giảm trương lực cơ"),
    ("066005", "ichthyoses", "noun", "/ˌɪkθiˈoʊsiːz/", "bệnh da vảy cá bẩm sinh"),
    ("066006", "intimas", "noun", "/ˈɪntɪməz/", "lớp áo trong của thành mạch máu"),
    ("066007", "ionescos", "noun", "/ˌiːəˈnɛskoʊz/", "nhà soạn kịch phi lý Ionesco"),
    ("066008", "issachars", "noun", "/ˈɪsəkɑːrz/", "nhân vật Kinh Thánh Y-sa-ca"),
    ("066009", "jakobsons", "noun", "/ˈjɑːkəbsənz/", "nhà ngôn ngữ học Roman Jakobson"),
    ("066010", "kwanzas", "noun", "/ˈkwɑːnzəz/", "đồng tiền kwanza của Angola"),
    ("066011", "laburnums", "noun", "/ləˈbɜːrnəmz/", "cây kim tước hoa vàng rủ"),
    ("066012", "landgraves", "noun", "/ˈlændˌɡreɪvz/", "bá tước lãnh chúa vùng Đức cổ"),
    ("066013", "laruses", "noun", "/ˈlɛərəsɪz/", "chi chim mòng biển Larus"),
    ("066014", "leaseholders", "noun", "/ˈliːsˌhoʊldərz/", "người thuê đất hoặc nhà dài hạn"),
    ("066015", "listerioses", "noun", "/lɪˌstɪəriˈoʊsiːz/", "bệnh nhiễm khuẩn listeriosis"),
    ("066016", "longlegses", "noun", "/ˈlɒŋˌlɛɡzɪz/", "chim cà kheo; nhện chân dài"),
    ("066017", "manichaeans", "noun", "/ˌmænɪˈkiːənz/", "tín đồ Mani giáo nhị nguyên cổ đại"),
    ("066018", "meningiomas", "noun", "/məˌnɪndʒiˈoʊməz/", "khối u lành tính ở màng não"),
    ("066019", "militarisations", "noun", "/ˌmɪlɪtəraɪˈzeɪʃənz/", "sự quân sự hóa khu vực"),
    ("066020", "moonier", "adj", "/ˈmuːniər/", "mơ màng hơn; nhiều ánh trăng hơn"),
    ("066021", "mooniest", "adj", "/ˈmuːniɪst/", "mơ màng nhất; nhiều ánh trăng nhất"),
    ("066022", "neckars", "noun", "/ˈnɛkɑːrz/", "sông Neckar ở miền nam nước Đức"),
    ("066023", "neoconservatisms", "noun", "/ˌniːoʊkənˈsɜːrvəˌtɪzəmz/", "chủ nghĩa tân bảo thủ chính trị"),
    ("066024", "niduses", "noun", "/ˈnaɪdəsɪz/", "ổ vi khuẩn; nơi sinh sản phát tán"),
    ("066025", "obeahs", "noun", "/ˈoʊbiəz/", "tín ngưỡng ma thuật Obeah Caribe"),
    ("066026", "oleas", "noun", "/ˈoʊliəz/", "cây ô liu thuộc chi Olea"),
    ("066027", "overindulged", "verb", "/ˌoʊvərɪnˈdʌldʒd/", "đã chiều chuộng hoặc ăn uống quá độ"),
    ("066028", "overindulges", "verb", "/ˌoʊvərɪnˈdʌldʒɪz/", "chiều chuộng hoặc ăn uống quá độ"),
    ("066029", "overindulging", "verb", "/ˌoʊvərɪnˈdʌldʒɪŋ/", "đang ăn uống hoặc nuông chiều quá"),
    ("066030", "paderewskis", "noun", "/ˌpædəˈrɛfskiz/", "nghệ sĩ dương cầm Paderewski"),
    ("066031", "paraprofessionals", "noun", "/ˌpærəprəˈfɛʃənəlz/", "trợ lý hỗ trợ chuyên môn y tế giáo"),
    ("066032", "pesetas", "noun", "/pəˈseɪtəz/", "đồng tiền peseta cũ của Tây Ban Nha"),
    ("066033", "pilasters", "noun", "/pɪˈlæstərz/", "cột trụ giả đắp nổi sát tường"),
    ("066034", "prakrits", "noun", "/ˈprɑːkrɪts/", "nhóm ngôn ngữ Prakrit Ấn Độ cổ"),
    ("066035", "procurers", "noun", "/prəˈkjʊərərz/", "kẻ môi giới mại dâm; người thu mua"),
    ("066036", "pyruses", "noun", "/ˈpaɪrəsɪz/", "cây lê thuộc chi Pyrus"),
    ("066037", "redbreasts", "noun", "/ˈrɛdˌbrɛsts/", "chim cổ đỏ oanh châu Âu"),
    ("066038", "rededications", "noun", "/riːˌdɛdɪˈkeɪʃənz/", "lễ tái khánh thành; sự tái hiến"),
    ("066039", "remonstrances", "noun", "/rɪˈmɒnstrənsɪz/", "lời phản đối; lời can gián gay gắt"),
    ("066040", "reredoses", "noun", "/ˈrɪərˌdoʊsɪz/", "bình phong chạm khắc sau bàn thờ"),
    ("066041", "rescripts", "noun", "/ˈriːˌskrɪpts/", "sắc lệnh phán quyết chính thức"),
    ("066042", "saales", "noun", "/ˈzɑːləz/", "sông Saale chảy qua miền đông Đức"),
    ("066043", "samizdats", "noun", "/ˌsæmɪzˈdɑːts/", "tài liệu xuất bản lén lút thời Xô"),
    ("066044", "sentimentalists", "noun", "/ˌsɛntɪˈmɛntəlɪsts/", "người dễ xúc động ủy mị đa cảm"),
    ("066045", "sepals", "noun", "/ˈsiːpəlz/", "lá đài bảo vệ nụ hoa"),
    ("066046", "shavuots", "noun", "/ʃɑːˈvuːoʊts/", "lễ Ngũ Tuần Shavuot của Do Thái"),
    ("066047", "shinbones", "noun", "/ˈʃɪnˌboʊnz/", "xương ống quyển; xương chày chân"),
    ("066048", "silenes", "noun", "/saɪˈliːniz/", "cây hoa bắt ruồi chi Silene"),
    ("066049", "skullduggeries", "noun", "/skʌlˈdʌɡəriz/", "thủ đoạn gian trá lừa đảo ngầm"),
    ("066050", "skyhooks", "noun", "/ˈskaɪˌhʊks/", "móc treo tưởng tượng; cần cẩu bay"),
    ("066051", "sniffier", "adj", "/ˈsnɪfiər/", "hách dịch khinh khỉnh hơn"),
    ("066052", "sniffiest", "adj", "/ˈsnɪfiɪst/", "hách dịch khinh khỉnh nhất"),
    ("066053", "sphenoids", "noun", "/ˈsfiːnɔɪdz/", "xương bướm ở nền hộp sọ"),
    ("066054", "stalactites", "noun", "/stəˈlæktaɪts/", "nhũ đá rủ xuống từ trần hang động"),
    ("066055", "straightjackets", "noun", "/ˈstreɪtˌdʒækɪts/", "áo bó khống chế; sự trói buộc"),
    ("066056", "tattlers", "noun", "/ˈtætlərz/", "kẻ mách lẻo; chim choắt đồi núi"),
    ("066057", "thylacines", "noun", "/ˈθaɪləˌsiːnz/", "chó sói túi Tasmania đã tuyệt chủng"),
    ("066058", "ugaritics", "noun", "/ˌuːɡəˈrɪtɪks/", "tiếng Ugarit cổ đại ở Syria"),
    ("066059", "uuhs", "noun", "/ˈuːz/", "nguyên tố phóng xạ livermorium Uuh"),
    ("066060", "vaccinias", "noun", "/vækˈsɪniəz/", "vi rút vắc-xin gây bệnh đậu bò"),
    ("066061", "vicias", "noun", "/ˈvɪsiəz/", "cây đậu tằm thuộc chi Vicia"),
    ("066062", "vincristines", "noun", "/vɪnˈkrɪstiːnz/", "thuốc hóa trị ung thư vincristin"),
    ("066063", "waybills", "noun", "/ˈweɪˌbɪlz/", "vận đơn ghi chi tiết hàng hóa"),
    ("066064", "wetbacks", "noun", "/ˈwɛtˌbæks/", "người nhập cư Mexico (từ miệt thị)"),
    ("066065", "withies", "noun", "/ˈwɪðiz/", "cành liễu dẻo dùng đan rổ rá"),
    ("066066", "wykehams", "noun", "/ˈwɪkəmz/", "giám mục Anh William of Wykeham"),
    ("066067", "abies concolor", "phrase", "/ˈeɪbiːz ˈkɒŋkələr/", "cây linh sam trắng Bắc Mỹ"),
    ("066068", "adenomatous polyp", "phrase", "/ˌædəˈnoʊmətəs ˈpɒlɪp/", "polip u tuyến ở niêm mạc ruột"),
    ("066069", "aedes albopictus", "phrase", "/eɪˈiːdiːz ˌælboʊˈpɪktəs/", "muỗi vằn châu Á truyền bệnh"),
    ("066070", "agrostis alba", "phrase", "/əˈɡrɒstɪs ˈælbə/", "cỏ lông trắng; cỏ mật Agrostis"),
    ("066071", "ashcan school", "phrase", "/ˈæʃkæn skuːl/", "trường phái hội họa Mỹ Ashcan"),
    ("066072", "baton twirler", "phrase", "/bəˈtɒn ˈtwɜːrlər/", "người biểu diễn xoay gậy diễu hành"),
    ("066073", "carex arenaria", "phrase", "/ˈkɛərɛks ˌærəˈnɛəriə/", "cây cói cát châu Âu mọc ven biển"),
    ("066074", "coffea robusta", "phrase", "/ˈkɒfiə roʊˈbʌstə/", "cây cà phê vối Robusta"),
    ("066075", "collared peccary", "phrase", "/ˈkɒlərd ˈpɛkəri/", "lợn lòi cổ khoang trắng châu Mỹ"),
    ("066076", "common gum cistus", "phrase", "/ˈkɒmən ɡʌm ˈsɪstəs/", "cây hoa hồng đá tiết nhựa thơm"),
    ("066077", "common madia", "phrase", "/ˈkɒmən ˈmeɪdiə/", "cây cúc dầu California"),
    ("066078", "common mullein", "phrase", "/ˈkɒmən ˈmʌlɪn/", "cây hoa mao địa hoàng nhung vàng"),
    ("066079", "connotative of", "phrase", "/ˈkɒnəˌteɪtɪv əv/", "mang hàm ý; gợi liên tưởng tới"),
    ("066080", "corpus delicti", "phrase", "/ˈkɔːrpəs dɪˈlɪktaɪ/", "vật chứng cấu thành tội phạm"),
    ("066081", "crocus sativus", "phrase", "/ˈkroʊkəs səˈtaɪvəs/", "cây nghệ tây cho nhụy hoa saffron"),
    ("066082", "ecuadoran monetary unit", "phrase", "/ˌɛkwəˈdɔːrən ˈmɒnɪtəri ˈjuːnɪt/", "đơn vị tiền tệ của Ecuador"),
    ("066083", "eleonora duse", "phrase", "/ˌɛleɪəˈnɔːrə ˈduːzeɪ/", "nữ diễn viên kịch Ý Eleonora Duse"),
    ("066084", "euphorbia marginata", "phrase", "/juːˈfɔːrbiə ˌmɑːrdʒɪˈneɪtə/", "cây cỏ sữa lá viền trắng tuyết"),
    ("066085", "eva le gallienne", "phrase", "/ˈiːvə lə ˌɡæliˈɛn/", "nữ diễn viên Mỹ Eva Le Gallienne"),
    ("066086", "family leguminosae", "phrase", "/ˈfæməli ləˌɡjuːmɪˈnoʊsiː/", "họ Đậu thực vật cho hạt giáp"),
    ("066087", "family noctuidae", "phrase", "/ˈfæməli nɒkˈtjuːɪdiː/", "họ Ngài đêm bướm hoạt động tối"),
    ("066088", "fuchsia coccinea", "phrase", "/ˈfjuːʃə kɒkˈsɪniə/", "cây hoa lồng đèn đỏ thẫm"),
    ("066089", "genus cistus", "phrase", "/ˈdʒiːnəs ˈsɪstəs/", "chi thực vật hoa hồng đá Cistus"),
    ("066090", "genus cynodon", "phrase", "/ˈdʒiːnəs ˈsɪnədɒn/", "chi cỏ gà Cynodon"),
    ("066091", "genus cyprinus", "phrase", "/ˈdʒiːnəs sɪˈpraɪnəs/", "chi cá chép Cyprinus"),
    ("066092", "genus dimetrodon", "phrase", "/ˈdʒiːnəs daɪˈmɛtrədɒn/", "chi bò sát tiền sử Dimetrodon"),
    ("066093", "genus hordeum", "phrase", "/ˈdʒiːnəs ˈhɔːrdiəm/", "chi lúa mạch Hordeum"),
    ("066094", "genus lagopus", "phrase", "/ˈdʒiːnəs ˈlæɡəpəs/", "chi chim gà gô tuyết Lagopus"),
    ("066095", "genus lathyrus", "phrase", "/ˈdʒiːnəs ˈlæθɪrəs/", "chi đậu hương Lathyrus"),
    ("066096", "genus madia", "phrase", "/ˈdʒiːnəs ˈmeɪdiə/", "chi cây cúc nhựa thơm Madia"),
    ("066097", "genus oestrus", "phrase", "/ˈdʒiːnəs ˈiːstrəs/", "chi ruồi trâu ký sinh Oestrus"),
    ("066098", "genus ricinus", "phrase", "/ˈdʒiːnəs ˈrɪsɪnəs/", "chi cây thầu dầu Ricinus"),
    ("066099", "genus tillandsia", "phrase", "/ˈdʒiːnəs tɪˈlændziə/", "chi cây không khí dứa Tillandsia"),
    ("066100", "georg philipp telemann", "phrase", "/ˈɡeɪɔːrɡ ˈfɪlɪp ˈtɛləmɑːn/", "nhà soạn nhạc Đức Telemann"),
    ("066101", "glyceryl ester", "phrase", "/ˈɡlɪsərɪl ˈɛstər/", "hợp chất este của glixerol"),
    ("066102", "gnaeus julius agricola", "phrase", "/ˈnaɪəs ˈdʒuːliəs əˈɡrɪkələ/", "tướng La Mã Julius Agricola"),
]

with open("scratch/b34_r03_raw_p1.json") as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100
allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}

out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, items):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} != {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} != {hw}"
    assert pos in allowed_pos, f"Bad POS {pos} for {hw}"
    assert len(vi) <= 35, f"VI too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA: {hw} -> {ipa}"
    inner = ipa[1:-1]
    assert inner and not inner.startswith(" ") and not inner.endswith(" "), f"Empty/space IPA: {hw} -> {ipa}"
    rec = dict(r)
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

with open("scratch/b34_r03_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r03_p1.json OK")
