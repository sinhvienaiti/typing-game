import json

items = [
    ("068203", "shakoes", "noun", "/ˈʃeɪkoʊz/", "mũ quân đội hình trụ gắn lông"),
    ("068204", "shakos", "noun", "/ˈʃeɪkoʊz/", "mũ lính cao chóp đứng thời xưa"),
    ("068205", "shamisens", "noun", "/ˈʃæmɪˌsɛnz/", "đàn tam ba dây truyền thống Nhật"),
    ("068206", "sightsaw", "verb", "/ˈsaɪtˌsɔː/", "đã đi tham quan thắng cảnh"),
    ("068207", "sightseed", "verb", "/ˈsaɪtˌsiːd/", "đã đi tham quan du lịch (cũ)"),
    ("068208", "sightseen", "verb", "/ˈsaɪtˌsiːn/", "đã đi tham quan (quá khứ phân từ)"),
    ("068209", "sightsees", "verb", "/ˈsaɪtˌsiːz/", "đi tham quan thắng cảnh du lịch"),
    ("068210", "siwans", "noun", "/siˈwɑːnz/", "tháng thứ ba Sivan lịch Do Thái"),
    ("068211", "solanaceaes", "noun", "/ˌsɒləˈneɪʃiz/", "họ Cà gồm cà chua khoai tây ớt"),
    ("068212", "spacefarings", "noun", "/ˈspeɪsˌfɛərɪŋz/", "chuyến du hành thám hiểm vũ trụ"),
    ("068213", "spartinas", "noun", "/spɑːrˈtaɪnəz/", "cỏ lách đầm lầy mặn Spartina"),
    ("068214", "spindrifts", "noun", "/ˈspɪnˌdrɪfts/", "bọt nước biển bị gió thổi tung"),
    ("068215", "spoonbills", "noun", "/ˈspuːnˌbɪlz/", "chim cò thìa mỏ dẹt đầu tròn"),
    ("068216", "strophes", "noun", "/ˈstroʊfiz/", "khổ thơ hát đối đáp Hy Lạp cổ"),
    ("068217", "succinylcholines", "noun", "/ˌsʌksɪnəlˈkoʊliːnz/", "thuốc giãn cơ gây mê nhanh"),
    ("068218", "sulfonylureas", "noun", "/ˌsʌlfəˈnɪljʊəriəz/", "nhóm thuốc uống trị tiểu đường"),
    ("068219", "supremacisms", "noun", "/suːˈprɛməˌsɪzəmz/", "chủ nghĩa thượng đẳng chủng tộc"),
    ("068220", "syzygies", "noun", "/ˈsɪzɪdʒiz/", "thẳng hàng ba thiên thể; cặp đối"),
    ("068221", "tammuzes", "noun", "/ˈtæməzɪz/", "tháng thứ mười Tammuz lịch Do Thái"),
    ("068222", "temazepams", "noun", "/təˈmæzəˌpæmz/", "thuốc ngủ an thần temazepam"),
    ("068223", "thyroidectomies", "noun", "/ˌθaɪrɔɪˈdɛktəmiz/", "ca phẫu thuật cắt bỏ tuyến giáp"),
    ("068224", "tilias", "noun", "/ˈtɪliəz/", "cây đoạn gỗ nhẹ thuộc chi Tilia"),
    ("068225", "tranquillisers", "noun", "/ˈtræŋkwɪˌlaɪzərz/", "thuốc an thần làm dịu thần kinh"),
    ("068226", "translocated", "verb", "/ˌtrænzloʊˈkeɪtɪd/", "đã chuyển đoạn gen; đã di dời chỗ"),
    ("068227", "translocates", "verb", "/ˈtrænzloʊˌkeɪts/", "chuyển đoạn nhiễm sắc thể; di dời"),
    ("068228", "translocating", "verb", "/ˌtrænzloʊˈkeɪtɪŋ/", "đang chuyển đoạn gen; đang di dời"),
    ("068229", "tropopauses", "noun", "/ˈtrɒpəˌpɔːzɪz/", "khoảng lặng đối lưu khí quyển"),
    ("068230", "vicariates", "noun", "/vaɪˈkɛəriəts/", "giáo phận đại diện tông tòa"),
    ("068231", "vioxxes", "noun", "/ˈvaɪɒksɪz/", "thuốc giảm đau chống viêm Vioxx"),
    ("068232", "voiceprints", "noun", "/ˈvɔɪsˌprɪnts/", "dấu vân giọng nói nhận dạng âm"),
    ("068233", "winckelmanns", "noun", "/ˈvɪŋkəlmɑːnz/", "nhà khảo cổ nghệ thuật Winckelmann"),
    ("068234", "zukermans", "noun", "/ˈzʊkərmənz/", "nghệ sĩ vĩ cầm Pinchas Zukerman"),
    ("068235", "achondroplasias", "noun", "/ˌeɪkɒndrəˈpleɪʒəz/", "bệnh lùn loạn sản sụn bẩm sinh"),
    ("068236", "aconita", "noun", "/əˈkɒnɪtə/", "cây ô đầu phụ tử độc chi Aconitum"),
    ("068237", "agapanthuses", "noun", "/ˌæɡəˈpænθəsɪz/", "hoa thanh anh huệ sông Nile"),
    ("068238", "aluminates", "noun", "/əˈluːmɪˌneɪts/", "muối hóa học aluminat"),
    ("068239", "americanized", "verb", "/əˈmɛrɪkəˌnaɪzd/", "đã Mỹ hóa theo văn hóa Mỹ"),
    ("068240", "americanizes", "verb", "/əˈmɛrɪkəˌnaɪzɪz/", "Mỹ hóa theo lối sống văn hóa Mỹ"),
    ("068241", "americanizing", "verb", "/əˈmɛrɪkəˌnaɪzɪŋ/", "đang Mỹ hóa theo phong cách Mỹ"),
    ("068242", "anosmias", "noun", "/ænˈɒzmiəz/", "chứng mất hoàn toàn khứu giác"),
    ("068243", "aspirators", "noun", "/ˈæspəˌreɪtərz/", "máy hút dịch y tế; ống hút chân"),
    ("068244", "balases", "noun", "/ˈbæləsɪz/", "đá quý spinel màu hồng đỏ balas"),
    ("068245", "boutonnieres", "noun", "/ˌbuːtənˈjɛərz/", "bông hoa nhỏ cài ve áo vest nam"),
    ("068246", "bvds", "noun", "/ˌbiː viː ˈdiːz/", "quần áo lót nam thương hiệu BVD"),
    ("068247", "carnaubas", "noun", "/kɑːrˈnɔːbəz/", "cây cọ hoặc sáp tự nhiên carnauba"),
    ("068248", "cashboxes", "noun", "/ˈkæʃˌbɒksɪz/", "hộp sắt khóa đựng tiền mặt quầy"),
    ("068249", "castrati", "noun", "/kæˈstrɑːti/", "nam ca sĩ hát giọng cao thời xưa"),
    ("068250", "castratos", "noun", "/kæˈstrɑːtoʊz/", "nam ca sĩ giọng nữ cao thời xưa"),
    ("068251", "chadors", "noun", "/ˈtʃɑːdərz/", "áo choàng trùm kín đầu nữ Iran"),
    ("068252", "changans", "noun", "/tʃɑːŋˈɑːnz/", "kinh đô Trường An Trung Quốc cổ"),
    ("068253", "chiasms", "noun", "/ˈkaɪæzəmz/", "giao thoa chéo; cấu trúc đối xứng"),
    ("068254", "conjurors", "noun", "/ˈkɒndʒərərz/", "nhà ảo thuật; thầy phù thủy"),
    ("068255", "corridas", "noun", "/kəˈriːdəz/", "trận đấu bò tót Tây Ban Nha"),
    ("068256", "cryptograms", "noun", "/ˈkrɪptəˌɡræmz/", "bản mật mã viết bằng ký hiệu ẩn"),
    ("068257", "cynosures", "noun", "/ˈsɪnəˌʃʊərz/", "tâm điểm chú ý; chòm sao Bắc Đẩu"),
    ("068258", "czestochowas", "noun", "/tʃɛstəˈxoʊvəz/", "thành phố Częstochowa của Ba Lan"),
    ("068259", "dapsones", "noun", "/ˈdæpˌsoʊnz/", "thuốc kháng sinh điều trị phong"),
    ("068260", "dermabrasions", "noun", "/ˌdɜːrməˈbreɪʒənz/", "kỹ thuật mài mòn tái tạo bề mặt da"),
    ("068261", "digitalisations", "noun", "/ˌdɪdʒɪtəlaɪˈzeɪʃənz/", "quá trình số hóa; liệu pháp tim"),
    ("068262", "diverticula", "noun", "/ˌdaɪvərˈtɪkjələ/", "túi thừa phình ra ở thành ruột"),
    ("068263", "diverticulums", "noun", "/ˌdaɪvərˈtɪkjələmz/", "túi thừa nhỏ trên thành ống tiêu"),
    ("068264", "dorsiflexions", "noun", "/ˌdɔːrsɪˈflɛkʃənz/", "động tác gập cổ chân lên cẳng"),
    ("068265", "doubloons", "noun", "/dʌˈbluːnz/", "đồng tiền vàng cổ Tây Ban Nha"),
    ("068266", "doyennes", "noun", "/dwɑːˈjɛnz/", "nữ trưởng lão uy tín trong ngành"),
    ("068267", "eaglets", "noun", "/ˈiːɡlɪts/", "chim đại bàng non mới nở"),
    ("068268", "eumeneses", "noun", "/ˈjuːməniːzɪz/", "tướng Eumenes; chi ong bắp cày"),
    ("068269", "frisias", "noun", "/ˈfrɪʒəz/", "vùng đất lịch sử Frisia ven biển"),
    ("068270", "fulas", "noun", "/ˈfuːləz/", "người và ngôn ngữ Fulani Tây Phi"),
    ("068271", "geomancies", "noun", "/ˈdʒiːəˌmænsiz/", "thuật xem phong thủy địa lý cổ"),
    ("068272", "gluier", "adj", "/ˈɡluːiər/", "dính bết nhớp nháp như keo hơn"),
    ("068273", "gluiest", "adj", "/ˈɡluːiɪst/", "dính bết nhớp nháp như keo nhất"),
    ("068274", "hamsuns", "noun", "/ˈhɑːmsənz/", "nhà văn Na Uy Knut Hamsun"),
    ("068275", "hylas", "noun", "/ˈhaɪləz/", "chi nhái bén leo cây xanh Hyla"),
    ("068276", "ironworkers", "noun", "/ˈaɪərnˌwɜːrkərz/", "thợ lắp dựng kết cấu thép; thợ rèn"),
    ("068277", "jabirus", "noun", "/ˌdʒæbəˈruːz/", "chim cò khổng lồ cổ đỏ jabiru"),
    ("068278", "jooks", "noun", "/dʒʊks/", "cháo trắng kiểu Á; quán rượu (lóng)"),
    ("068279", "kaches", "noun", "/ˈkɑːtʃɪz/", "vùng Kutch ở bang Gujarat Ấn Độ"),
    ("068280", "kittiwakes", "noun", "/ˈkɪtiˌweɪks/", "mòng biển kittiwake làm tổ vách đá"),
    ("068281", "larixes", "noun", "/ˈlɛərɪksɪz/", "cây thông rụng lá thuộc chi Larix"),
    ("068282", "lesvoses", "noun", "/ˈlɛzvɒsɪz/", "đảo Lesbos của Hy Lạp trên biển"),
    ("068283", "librations", "noun", "/laɪˈbreɪʃənz/", "sự bình động lắc của Mặt Trăng"),
    ("068284", "megaliths", "noun", "/ˈmɛɡəˌlɪθs/", "công trình cự thạch thời tiền sử"),
    ("068285", "metazoans", "noun", "/ˌmɛtəˈzoʊənz/", "động vật đa bào cơ thể phân hóa"),
    ("068286", "mikvahs", "noun", "/ˈmɪkvəz/", "bể tắm tẩy uế nghi lễ Do Thái"),
    ("068287", "mmpis", "noun", "/ˌɛm ɛm piː ˈaɪz/", "trắc nghiệm nhân cách đa pha MMPI"),
    ("068288", "moongs", "noun", "/muːŋz/", "hạt đậu xanh nhỏ nấu ăn Ấn Độ"),
    ("068289", "mountebanks", "noun", "/ˈmaʊntɪˌbæŋks/", "kẻ lang băm rao thuốc giả lừa bịp"),
    ("068290", "mussorgskies", "noun", "/mʊˈsɔːrɡskiz/", "nhà soạn nhạc Nga Mussorgsky"),
    ("068291", "mustelas", "noun", "/ˈmʌstɪləz/", "chi chồn nhỏ ăn thịt Mustela"),
    ("068292", "myoclonuses", "noun", "/ˌmaɪəˈkloʊnəsɪz/", "chứng giật cơ đột ngột từng cơn"),
    ("068293", "namers", "noun", "/ˈneɪmərz/", "người đặt tên; người chỉ điểm"),
    ("068294", "nibelungen", "noun", "/ˈniːbəˌlʊŋən/", "tộc người lùn sử thi Nibelungen"),
    ("068295", "nibelungs", "noun", "/ˈniːbəˌlʊŋz/", "nhân vật sử thi Nibelung của Đức"),
    ("068296", "notated", "verb", "/noʊˈteɪtɪd/", "đã ký âm nhạc; đã ghi ký hiệu"),
    ("068297", "notates", "verb", "/noʊˈteɪts/", "ký âm bản nhạc; ghi bằng ký hiệu"),
    ("068298", "notating", "verb", "/noʊˈteɪtɪŋ/", "đang ký âm nhạc; ghi ký hiệu toán"),
    ("068299", "paraboloids", "noun", "/pəˈræbəˌlɔɪdz/", "mặt cong paraboloid không gian"),
    ("068300", "parkier", "adj", "/ˈpɑːrkiər/", "lạnh buốt se lạnh hơn (khẩu ngữ)"),
    ("068301", "parkiest", "adj", "/ˈpɑːrkiɪst/", "lạnh buốt se lạnh nhất (khẩu ngữ)"),
    ("068302", "phenylketonurias", "noun", "/ˌfɛnɪlˌkiːtoʊˈnjʊəriəz/", "bệnh rối loạn chuyển hóa PKU"),
]

with open("scratch/b34_r07_raw_p3.json") as f:
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

with open("scratch/b34_r07_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r07_p3.json OK")
