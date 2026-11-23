import json

with open('scratch/b32_r04_raw_p5.json') as f:
    raw_items = json.load(f)

reviewed_data = {
    "lex.en.200k.056902": {"pos": "phrase", "ipa": "", "vi": "tài tử điện ảnh Humphrey Bogart"},
    "lex.en.200k.056903": {"pos": "phrase", "ipa": "", "vi": "loài thông cổ Huon ở Tasmania"},
    "lex.en.200k.056904": {"pos": "phrase", "ipa": "", "vi": "chứng đỏ mặt phì đại; mũi sư tử"},
    "lex.en.200k.056905": {"pos": "phrase", "ipa": "", "vi": "nhà báo điều tra Ida Tarbell"},
    "lex.en.200k.056906": {"pos": "phrase", "ipa": "", "vi": "hình thái học biến cách từ ngữ"},
    "lex.en.200k.056907": {"pos": "phrase", "ipa": "", "vi": "eo đất Kra ở miền nam Thái Lan"},
    "lex.en.200k.056908": {"pos": "phrase", "ipa": "", "vi": "nhà văn Pháp La Rochefoucauld"},
    "lex.en.200k.056909": {"pos": "phrase", "ipa": "", "vi": "hồ Albert Nyanza ở Đông Phi"},
    "lex.en.200k.056910": {"pos": "phrase", "ipa": "", "vi": "nữ họa sĩ trừu tượng Lee Krasner"},
    "lex.en.200k.056911": {"pos": "phrase", "ipa": "", "vi": "tập hợp phân thể fractal Mandelbrot"},
    "lex.en.200k.056912": {"pos": "phrase", "ipa": "", "vi": "nhà hóa học Nobel Manfred Eigen"},
    "lex.en.200k.056913": {"pos": "phrase", "ipa": "", "vi": "vũ công ba-lê Mikhail Baryshnikov"},
    "lex.en.200k.056914": {"pos": "phrase", "ipa": "", "vi": "buồm thấp nhất trên cột buồm lái"},
    "lex.en.200k.056915": {"pos": "phrase", "ipa": "", "vi": "tĩnh mạch tuyến mang tai mặt"},
    "lex.en.200k.056916": {"pos": "phrase", "ipa": "", "vi": "hóa chất diêm sinh kali clorat"},
    "lex.en.200k.056917": {"pos": "phrase", "ipa": "", "vi": "nguyên đại Nguyên sinh Proterozoic"},
    "lex.en.200k.056918": {"pos": "phrase", "ipa": "", "vi": "bệnh động kinh tâm thần vận động"},
    "lex.en.200k.056919": {"pos": "phrase", "ipa": "", "vi": "cổ phiếu quỹ mua lại của công ty"},
    "lex.en.200k.056920": {"pos": "phrase", "ipa": "", "vi": "chứng rung giật nhãn cầu dạng xoay"},
    "lex.en.200k.056921": {"pos": "phrase", "ipa": "", "vi": "Thánh Beda Đáng kính nước Anh"},
    "lex.en.200k.056922": {"pos": "phrase", "ipa": "", "vi": "dây thần kinh tạng nội tạng"},
    "lex.en.200k.056923": {"pos": "phrase", "ipa": "", "vi": "nếp gấp xếp ly hình nan quạt"},
    "lex.en.200k.056924": {"pos": "phrase", "ipa": "", "vi": "thanh đầm đất; que nén thuốc nổ"},
    "lex.en.200k.056925": {"pos": "phrase", "ipa": "", "vi": "globulin miễn dịch kháng uốn ván"},
    "lex.en.200k.056926": {"pos": "phrase", "ipa": "", "vi": "hồ Victoria lớn nhất châu Phi"},
    "lex.en.200k.056927": {"pos": "phrase", "ipa": "", "vi": "thống chế Phổ von Blücher"},
    "lex.en.200k.056928": {"pos": "phrase", "ipa": "", "vi": "bột màu đất son vàng tự nhiên"},
    "lex.en.200k.056929": {"pos": "noun", "ipa": "/ˈæblətɪvz/", "vi": "danh từ cách công cụ trong ngữ pháp"},
    "lex.en.200k.056930": {"pos": "noun", "ipa": "/aɪˈoʊliz/", "vi": "sốt tỏi dầu ô liu aioli kiểu Pháp"},
    "lex.en.200k.056931": {"pos": "noun", "ipa": "/ˈɛərhɛdz/", "vi": "kẻ rỗng tuếch; người ngớ ngẩn"},
    "lex.en.200k.056932": {"pos": "noun", "ipa": "/ælˈseɪʃənz/", "vi": "dân xứ Alsace; giống chó béc-giê"},
    "lex.en.200k.056933": {"pos": "noun", "ipa": "/ˌæntəˈnaɪnəsɪz/", "vi": "Hoàng đế La Mã Antoninus Pius"},
    "lex.en.200k.056934": {"pos": "noun", "ipa": "/ˌæpənˈdɛktəmiz/", "vi": "phẫu thuật mổ cắt bỏ ruột thừa"},
    "lex.en.200k.056935": {"pos": "noun", "ipa": "/ˈæplɪts/", "vi": "tiểu ứng dụng phần mềm applet"},
    "lex.en.200k.056936": {"pos": "noun", "ipa": "/əˈræknɪdz/", "vi": "lớp động vật hình nhện tám chân"},
    "lex.en.200k.056937": {"pos": "noun", "ipa": "/əˈrɪstəz/", "vi": "râu hạt lúa cỏ; lông râu côn trùng"},
    "lex.en.200k.056938": {"pos": "noun", "ipa": "/ˈætɪvænz/", "vi": "thuốc an thần giảm lo âu Ativan"},
    "lex.en.200k.056939": {"pos": "noun", "ipa": "/ˈbiːnoʊz/", "vi": "bữa tiệc liên hoan; trò chơi lô tô"},
    "lex.en.200k.056940": {"pos": "noun", "ipa": "/biːˈɛlzɪbʌbz/", "vi": "chúa quỷ ruồi Beelzebub địa ngục"},
    "lex.en.200k.056941": {"pos": "noun", "ipa": "/ˈbɜːrɡəmɑːts/", "vi": "quả cam hương bergamot nước Ý"},
    "lex.en.200k.056942": {"pos": "noun", "ipa": "/ˈbɪljənθs/", "vi": "phần một phần tỉ; thứ một tỉ"},
    "lex.en.200k.056943": {"pos": "noun", "ipa": "/ˌbaɪoʊˈmɛdɪsɪnz/", "vi": "ngành y sinh học hiện đại"},
    "lex.en.200k.056944": {"pos": "noun", "ipa": "/bleɪnz/", "vi": "mụn nhọt sưng mủ; vết lở loét da"},
    "lex.en.200k.056945": {"pos": "noun", "ipa": "/ˈbʊlhɔːrnz/", "vi": "chiếc loa phóng thanh cầm tay"},
    "lex.en.200k.056946": {"pos": "noun", "ipa": "/kəˈlɪstoʊz/", "vi": "mặt trăng Callisto của sao Mộc"},
    "lex.en.200k.056947": {"pos": "noun", "ipa": "/ˈkændɪdətʃərz/", "vi": "tư cách ứng cử viên; sự tranh cử"},
    "lex.en.200k.056948": {"pos": "noun", "ipa": "/ˌkæpəˈdoʊʃiəz/", "vi": "vùng thung lũng đá Cappadocia"},
    "lex.en.200k.056949": {"pos": "noun", "ipa": "/ˌkɑːrdɪˈnælətiz/", "vi": "bản số tập hợp; lực lượng tập hợp"},
    "lex.en.200k.056950": {"pos": "noun", "ipa": "/kɑːrˈnoʊz/", "vi": "nhà vật lý nhiệt học Sadi Carnot"},
    "lex.en.200k.056951": {"pos": "noun", "ipa": "/ˌsɛljuˈloʊsɪks/", "vi": "vật liệu chất dẻo xenluloza"},
    "lex.en.200k.056952": {"pos": "noun", "ipa": "/kɛlts/", "vi": "người Celt cổ xưa; rìu đá tiền sử"},
    "lex.en.200k.056953": {"pos": "noun", "ipa": "/ˈtʃɛərlɪfts/", "vi": "hệ thống cáp treo ghế trượt tuyết"},
    "lex.en.200k.056954": {"pos": "noun", "ipa": "/ˈklɔːrəplæsts/", "vi": "bào quan lục lạp quang hợp"},
    "lex.en.200k.056955": {"pos": "noun", "ipa": "/sərˈkæʃənz/", "vi": "người dân tộc Circassia ở Kavkaz"},
    "lex.en.200k.056956": {"pos": "noun", "ipa": "/ˈkaʊlɪŋz/", "vi": "vỏ bọc kim loại động cơ máy bay"},
    "lex.en.200k.056957": {"pos": "noun", "ipa": "/dɪˈklɛnʃənz/", "vi": "sự biến cách danh từ; sự suy thoái"},
    "lex.en.200k.056958": {"pos": "noun", "ipa": "/ˌdiːhjuːˈmɪdəfaɪərz/", "vi": "máy hút ẩm không khí gia đình"},
    "lex.en.200k.056959": {"pos": "noun", "ipa": "/ˈdɪʃwɑːʃɪŋz/", "vi": "công việc rửa chén bát đĩa ăn"},
    "lex.en.200k.056960": {"pos": "noun", "ipa": "/ˈdrɔːhɪdəz/", "vi": "thị trấn cổ Drogheda ở Ireland"},
    "lex.en.200k.056961": {"pos": "noun", "ipa": "/ˌiːˌbiːˈviːz/", "vi": "vi-rút gây u lympho Epstein-Barr"},
    "lex.en.200k.056962": {"pos": "noun", "ipa": "/ˈɛlɪsɪz/", "vi": "đảo Ellis ở New York; thần già nua"},
    "lex.en.200k.056963": {"pos": "noun", "ipa": "/ˈfæriərz/", "vi": "thợ rèn đóng móng sắt cho ngựa"},
    "lex.en.200k.056964": {"pos": "noun", "ipa": "/ˈfɛraɪts/", "vi": "vật liệu từ tính ferit; pha ferit"},
    "lex.en.200k.056965": {"pos": "verb", "ipa": "/fɪkˈseɪts/", "vi": "bị ám ảnh; dán chặt mắt chăm chú"},
    "lex.en.200k.056966": {"pos": "verb", "ipa": "/fɪkˈseɪtɪŋ/", "vi": "đang bị ám ảnh; dán mắt nhìn"},
    "lex.en.200k.056967": {"pos": "noun", "ipa": "/ˈflæʃərz/", "vi": "kẻ phô dâm bệnh hoạn; đèn chớp nháy"},
    "lex.en.200k.056968": {"pos": "verb", "ipa": "/fɔːrˈtɛlz/", "vi": "tiên đoán trước; báo trước điềm"},
    "lex.en.200k.056969": {"pos": "noun", "ipa": "/frɪlz/", "vi": "diềm đăng ten xếp nếp; chi tiết phụ"},
    "lex.en.200k.056970": {"pos": "noun", "ipa": "/ˈɡaʊtʃoʊz/", "vi": "chàng cao bồi thảo nguyên Nam Mỹ"},
    "lex.en.200k.056971": {"pos": "noun", "ipa": "/ˈdʒɛnəvəz/", "vi": "thành phố cảng Genova nước Ý"},
    "lex.en.200k.056972": {"pos": "noun", "ipa": "/ˈheɪlstɔːrmz/", "vi": "trận mưa đá dồn dập tàn phá"},
    "lex.en.200k.056973": {"pos": "noun", "ipa": "/ˈhændmeɪdənz/", "vi": "nữ tỳ hầu cận; công cụ phục vụ"},
    "lex.en.200k.056974": {"pos": "noun", "ipa": "/ˈhɑːbɡɑːblɪnz/", "vi": "yêu tinh lùn tinh quái; nỗi sợ hão"},
    "lex.en.200k.056975": {"pos": "noun", "ipa": "/ˈhoʊlbaɪnz/", "vi": "danh họa Phục hưng Hans Holbein"},
    "lex.en.200k.056976": {"pos": "verb", "ipa": "/ˈhʌvəld/", "vi": "đã sống chen chúc trong lều nát"},
    "lex.en.200k.056977": {"pos": "verb", "ipa": "/ˈhʌvəlɪŋ/", "vi": "sống chui rúc trong túp lều nát"},
    "lex.en.200k.056978": {"pos": "noun", "ipa": "/ˈhʌvəlz/", "vi": "những túp lều lụp xụp tồi tàn"},
    "lex.en.200k.056979": {"pos": "noun", "ipa": "/ˈhaɪɡənzɪz/", "vi": "nhà vật lý Christiaan Huygens"},
    "lex.en.200k.056980": {"pos": "noun", "ipa": "/ˈaɪsbɑːksɪz/", "vi": "thùng chứa đá ướp lạnh; tủ đá cổ"},
    "lex.en.200k.056981": {"pos": "verb", "ipa": "/ɪmˈpɪndʒd/", "vi": "đã xâm phạm lấn át; tác động mạnh"},
    "lex.en.200k.056982": {"pos": "verb", "ipa": "/ɪmˈpɪndʒɪz/", "vi": "xâm phạm tác động xấu; đè nặng lên"},
    "lex.en.200k.056983": {"pos": "noun", "ipa": "/ˈɪntərloʊpərz/", "vi": "kẻ xâm nhập xen vào; kẻ chen ngang"},
    "lex.en.200k.056984": {"pos": "verb", "ipa": "/ˈaɪtəmaɪzɪz/", "vi": "liệt kê từng khoản mục chi tiết"},
    "lex.en.200k.056985": {"pos": "verb", "ipa": "/ˈaɪtəmaɪzɪŋ/", "vi": "liệt kê chi tiết từng danh mục"},
    "lex.en.200k.056986": {"pos": "noun", "ipa": "/ˈkæfərz/", "vi": "từ ngữ miệt thị chủng tộc ở Nam Phi"},
    "lex.en.200k.056987": {"pos": "noun", "ipa": "/ˈkɪŋmeɪkərz/", "vi": "người giật dây dựng ngôi quyền lực"},
    "lex.en.200k.056988": {"pos": "noun", "ipa": "/lɑːrˈdʒɛsɪz/", "vi": "sự hào phóng ban phát; bổng lộc"},
    "lex.en.200k.056989": {"pos": "noun", "ipa": "/ˌɛlˌsiːˈɛmz/", "vi": "bội chung nhỏ nhất; tàu đổ bộ LCM"},
    "lex.en.200k.056990": {"pos": "noun", "ipa": "/ˈlɑːzɪndʒɪz/", "vi": "kẹo ngậm ho; hình quả trám"},
    "lex.en.200k.056991": {"pos": "noun", "ipa": "/məˈrɑːtəz/", "vi": "chiến binh đế quốc Maratha Ấn Độ"},
    "lex.en.200k.056992": {"pos": "noun", "ipa": "/ˈɛmˌbɪts/", "vi": "đơn vị triệu bit dữ liệu megabit"},
    "lex.en.200k.056993": {"pos": "noun", "ipa": "/ˈmiːltaɪmz/", "vi": "các bữa ăn hàng ngày; giờ ăn cơm"},
    "lex.en.200k.056994": {"pos": "noun", "ipa": "/ˈmɛdlaɪnz/", "vi": "cơ sở dữ liệu y sinh học MEDLINE"},
    "lex.en.200k.056995": {"pos": "noun", "ipa": "/məˈnɑːməniz/", "vi": "bộ tộc thổ dân da đỏ Menominee"},
    "lex.en.200k.056996": {"pos": "noun", "ipa": "/miːnz/", "vi": "phong thái đĩnh đạc; nét mặt cử chỉ"},
    "lex.en.200k.056997": {"pos": "noun", "ipa": "/moʊˌdiːliˈɑːniz/", "vi": "danh họa Amedeo Modigliani nước Ý"},
    "lex.en.200k.056998": {"pos": "noun", "ipa": "/ˈmɑːnoʊtaɪps/", "vi": "tranh in độc bản; máy xếp chữ rời"},
    "lex.en.200k.056999": {"pos": "noun", "ipa": "/ˈnaɪnərz/", "vi": "số chín; cầu thủ bóng đá bầu dục"},
    "lex.en.200k.057000": {"pos": "noun", "ipa": "/ˈnɑːdʒuːlz/", "vi": "nốt sần nốt hạch nhỏ dưới da"},
    "lex.en.200k.057001": {"pos": "noun", "ipa": "/ˌnɔːrməlaɪˈzeɪʃənz/", "vi": "sự bình thường hóa; sự chuẩn hóa"}
}

output_items = []
errors = []

for item in raw_items:
    item_id = item['id']
    if item_id not in reviewed_data:
        errors.append(f"Missing reviewed data for {item_id}")
        continue
    
    rev = reviewed_data[item_id]
    vi = rev['vi']
    pos = rev['pos']
    ipa = rev['ipa']
    
    # Validation
    if len(vi) > 35:
        errors.append(f"Length violation (>35) for {item_id} ({item['hw']}): '{vi}' ({len(vi)} chars)")
    if pos not in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase']:
        errors.append(f"Invalid POS '{pos}' for {item_id}")
    if ipa != "":
        if not (ipa.startswith('/') and ipa.endswith('/') and ipa.count('/') == 2):
            errors.append(f"Invalid IPA format '{ipa}' for {item_id}")
    elif ' ' not in item['hw']:
        errors.append(f"Single word missing IPA for {item_id} ({item['hw']})")
        
    new_item = {
        "id": item["id"],
        "hw": item["hw"],
        "pos": pos,
        "ipa": ipa,
        "vi": vi,
        "cefr": item.get("cefr", "C2"),
        "tier": item.get("tier", 5),
        "status": "reviewed",
        "notes": item.get("notes", "")
    }
    output_items.append(new_item)

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for e in errors:
        print(" - " + e)
    exit(1)

with open('scratch/b32_r04_p5.json', 'w', encoding='utf-8') as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)

print(f"Successfully authored and validated Part 5: {len(output_items)} items saved to scratch/b32_r04_p5.json")
