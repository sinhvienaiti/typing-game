import json

items = [
  {"id": "lex.en.200k.058502", "hw": "cruses", "pos": "noun", "ipa": "/krˈuzɪz/", "vi": "bình đựng dầu; bình đất nhỏ"},
  {"id": "lex.en.200k.058503", "hw": "ddcs", "pos": "noun", "ipa": "/dˌiːdiːsˈiːz/", "vi": "phân loại Dewey; bộ điều khiển số"},
  {"id": "lex.en.200k.058504", "hw": "destabilised", "pos": "verb", "ipa": "/dɪstˈeɪbəlaɪzd/", "vi": "làm mất ổn định; gây bất ổn"},
  {"id": "lex.en.200k.058505", "hw": "destabilises", "pos": "verb", "ipa": "/dɪstˈeɪbəlaɪzɪz/", "vi": "làm mất ổn định; gây mất cân bằng"},
  {"id": "lex.en.200k.058506", "hw": "destabilising", "pos": "verb", "ipa": "/dɪstˈeɪbəlaɪzɪŋ/", "vi": "làm mất ổn định; gây rối loạn"},
  {"id": "lex.en.200k.058507", "hw": "detentes", "pos": "noun", "ipa": "/deɪtˈɑːnts/", "vi": "sự hòa hoãn; giảm bớt căng thẳng"},
  {"id": "lex.en.200k.058508", "hw": "divvied", "pos": "verb", "ipa": "/dˈɪvid/", "vi": "đã chia phần; phân phát"},
  {"id": "lex.en.200k.058509", "hw": "divvies", "pos": "verb", "ipa": "/dˈɪviz/", "vi": "chia phần; phân chia"},
  {"id": "lex.en.200k.058510", "hw": "domitians", "pos": "noun", "ipa": "/doʊmˈɪʃənz/", "vi": "hoàng đế Domitian; bạo chúa"},
  {"id": "lex.en.200k.058511", "hw": "egomaniacs", "pos": "noun", "ipa": "/ˌiːɡoʊmˈeɪniæks/", "vi": "kẻ tự cao tự đại; người tự tôn"},
  {"id": "lex.en.200k.058512", "hw": "electrochemistries", "pos": "noun", "ipa": "/ɪlˌɛktroʊkˈɛmɪstriz/", "vi": "ngành điện hóa học"},
  {"id": "lex.en.200k.058513", "hw": "englishwomans", "pos": "noun", "ipa": "/ˈɪŋɡlɪʃwʊmənz/", "vi": "phụ nữ người Anh"},
  {"id": "lex.en.200k.058514", "hw": "extensors", "pos": "noun", "ipa": "/ɪkstˈɛnsɚz/", "vi": "cơ duỗi"},
  {"id": "lex.en.200k.058515", "hw": "feists", "pos": "noun", "ipa": "/fˈaɪsts/", "vi": "chó sục nhỏ; chó nhỏ lăng xăng"},
  {"id": "lex.en.200k.058516", "hw": "fishtailed", "pos": "verb", "ipa": "/fˈɪʃteɪld/", "vi": "lắc đuôi cá; xe lạng đuôi"},
  {"id": "lex.en.200k.058517", "hw": "fishtailing", "pos": "verb", "ipa": "/fˈɪʃteɪlɪŋ/", "vi": "lạng đuôi xe; lắc đuôi cá"},
  {"id": "lex.en.200k.058518", "hw": "fishtails", "pos": "verb", "ipa": "/fˈɪʃteɪlz/", "vi": "lạng đuôi xe; lắc lư"},
  {"id": "lex.en.200k.058519", "hw": "flagstones", "pos": "noun", "ipa": "/flˈæɡstˌoʊnz/", "vi": "phiến đá lát; đá phiến lát sân"},
  {"id": "lex.en.200k.058520", "hw": "flavins", "pos": "noun", "ipa": "/flˈeɪvɪnz/", "vi": "hợp chất flavin"},
  {"id": "lex.en.200k.058521", "hw": "foxholes", "pos": "noun", "ipa": "/fˈɑkshˌoʊlz/", "vi": "công sự cá nhân; hố cá nhân"},
  {"id": "lex.en.200k.058522", "hw": "freeholders", "pos": "noun", "ipa": "/frˈihˌoʊldɚz/", "vi": "chủ sở hữu đất đai vĩnh viễn"},
  {"id": "lex.en.200k.058523", "hw": "freons", "pos": "noun", "ipa": "/frˈiɑnz/", "vi": "khí freon; chất làm lạnh freon"},
  {"id": "lex.en.200k.058524", "hw": "frieslands", "pos": "noun", "ipa": "/frˈizləndz/", "vi": "tỉnh Friesland Hà Lan"},
  {"id": "lex.en.200k.058525", "hw": "frissons", "pos": "noun", "ipa": "/friːsˈɔːnz/", "vi": "cảm giác rùng mình; xúc động"},
  {"id": "lex.en.200k.058526", "hw": "frittatas", "pos": "noun", "ipa": "/frɪtˈɑːtəz/", "vi": "món trứng tráng kiểu Ý"},
  {"id": "lex.en.200k.058527", "hw": "gastroenterologists", "pos": "noun", "ipa": "/ɡˌæstroʊˌɛntərˈɑːlədʒɪsts/", "vi": "bác sĩ chuyên khoa tiêu hóa"},
  {"id": "lex.en.200k.058528", "hw": "gibrans", "pos": "noun", "ipa": "/dʒɪbrˈɑːnz/", "vi": "nhà thơ Gibran"},
  {"id": "lex.en.200k.058529", "hw": "girlhoods", "pos": "noun", "ipa": "/ɡˈɜːrlhʊdz/", "vi": "thời con gái; tuổi thiếu nữ"},
  {"id": "lex.en.200k.058530", "hw": "gorgonzolas", "pos": "noun", "ipa": "/ɡɔːrɡənzˈoʊləz/", "vi": "phô mai xanh gorgonzola"},
  {"id": "lex.en.200k.058531", "hw": "grappas", "pos": "noun", "ipa": "/ɡrˈæpəz/", "vi": "rượu nho grappa của Ý"},
  {"id": "lex.en.200k.058532", "hw": "hafts", "pos": "noun", "ipa": "/hˈæfts/", "vi": "cán dao; chuôi rìu"},
  {"id": "lex.en.200k.058533", "hw": "halses", "pos": "noun", "ipa": "/hˈɑːlsɪz/", "vi": "họa sĩ Hals; tác phẩm của Hals"},
  {"id": "lex.en.200k.058534", "hw": "hirohitos", "pos": "noun", "ipa": "/hˌɪroʊhˈiːtoʊz/", "vi": "Nhật hoàng Hirohito"},
  {"id": "lex.en.200k.058535", "hw": "hnds", "pos": "noun", "ipa": "/ˌeɪtʃɛndˈiːz/", "vi": "bằng cao đẳng quốc gia Anh"},
  {"id": "lex.en.200k.058536", "hw": "hospitalisations", "pos": "noun", "ipa": "/hˌɑːspɪtəlaɪzˈeɪʃənz/", "vi": "sự nhập viện; ca điều trị"},
  {"id": "lex.en.200k.058537", "hw": "immunofluorescences", "pos": "noun", "ipa": "/ɪmjˌuːnoʊflʊrˈɛsənsɪz/", "vi": "miễn dịch huỳnh quang"},
  {"id": "lex.en.200k.058538", "hw": "impaled", "pos": "verb", "ipa": "/ˌɪmpˈeɪld/", "vi": "đâm xuyên qua; cắm vào cọc"},
  {"id": "lex.en.200k.058539", "hw": "impales", "pos": "verb", "ipa": "/ˌɪmpˈeɪlz/", "vi": "đâm xuyên qua; xiên qua"},
  {"id": "lex.en.200k.058540", "hw": "impaling", "pos": "verb", "ipa": "/ˌɪmpˈeɪlɪŋ/", "vi": "đang đâm xuyên; hành vi xiên"},
  {"id": "lex.en.200k.058541", "hw": "impoundments", "pos": "noun", "ipa": "/ˌɪmpˈaʊndmənts/", "vi": "hồ chứa nước; sự tịch thu"},
  {"id": "lex.en.200k.058542", "hw": "incisors", "pos": "noun", "ipa": "/ˌɪnsˈaɪzɚz/", "vi": "răng cửa"},
  {"id": "lex.en.200k.058543", "hw": "ipvs", "pos": "noun", "ipa": "/ˌaɪpiːvˈiːz/", "vi": "vắc-xin bại liệt bất hoạt"},
  {"id": "lex.en.200k.058544", "hw": "kails", "pos": "noun", "ipa": "/kˈeɪlz/", "vi": "cải xoăn; món canh rau cải"},
  {"id": "lex.en.200k.058545", "hw": "kampucheas", "pos": "noun", "ipa": "/kˌæmpʊtʃˈiːəz/", "vi": "nước Campuchia"},
  {"id": "lex.en.200k.058546", "hw": "khats", "pos": "noun", "ipa": "/kˈæts/", "vi": "cây lá khát; lá ma túy khat"},
  {"id": "lex.en.200k.058547", "hw": "kingstowns", "pos": "noun", "ipa": "/kˈɪŋztaʊnz/", "vi": "thành phố Kingstown"},
  {"id": "lex.en.200k.058548", "hw": "kronur", "pos": "noun", "ipa": "/krˈoʊnʊər/", "vi": "đồng króna của Iceland"},
  {"id": "lex.en.200k.058549", "hw": "loamier", "pos": "adj", "ipa": "/lˈoʊmiɚ/", "vi": "nhiều đất thịt hơn; màu mỡ hơn"},
  {"id": "lex.en.200k.058550", "hw": "loamiest", "pos": "adj", "ipa": "/lˈoʊmiɪst/", "vi": "nhiều đất thịt nhất"},
  {"id": "lex.en.200k.058551", "hw": "longboats", "pos": "noun", "ipa": "/lˈɔːŋboʊts/", "vi": "thuyền cứu sinh tàu buồm"},
  {"id": "lex.en.200k.058552", "hw": "luminals", "pos": "noun", "ipa": "/lˈuːmɪnəlz/", "vi": "thuốc an thần Luminal"},
  {"id": "lex.en.200k.058553", "hw": "maginots", "pos": "noun", "ipa": "/mˈæʒɪnoʊz/", "vi": "phòng tuyến Maginot"},
  {"id": "lex.en.200k.058554", "hw": "mandrels", "pos": "noun", "ipa": "/mˈændrəlz/", "vi": "trục gá máy tiện; lõi uốn"},
  {"id": "lex.en.200k.058555", "hw": "marengos", "pos": "noun", "ipa": "/mərˈɛŋɡoʊz/", "vi": "trận Marengo; món gà Marengo"},
  {"id": "lex.en.200k.058556", "hw": "martingales", "pos": "noun", "ipa": "/mˈɑːrtɪŋɡeɪlz/", "vi": "dây ức ngựa; phép cược nhân đôi"},
  {"id": "lex.en.200k.058557", "hw": "mesoamericans", "pos": "noun", "ipa": "/mˌɛzoʊəmˈɛrɪkənz/", "vi": "người Trung Mỹ cổ đại"},
  {"id": "lex.en.200k.058558", "hw": "mesoamericas", "pos": "noun", "ipa": "/mˌɛzoʊəmˈɛrɪkəz/", "vi": "vùng Trung Mỹ cổ đại"},
  {"id": "lex.en.200k.058559", "hw": "methylphenidates", "pos": "noun", "ipa": "/mˌɛθəlfenˈɪdeɪts/", "vi": "thuốc methylphenidate"},
  {"id": "lex.en.200k.058560", "hw": "molles", "pos": "noun", "ipa": "/mˈɔːleɪz/", "vi": "cây tiêu giả Peru"},
  {"id": "lex.en.200k.058561", "hw": "moonbeams", "pos": "noun", "ipa": "/mˈunbˌimz/", "vi": "tia sáng trăng; ánh trăng"},
  {"id": "lex.en.200k.058562", "hw": "motorcars", "pos": "noun", "ipa": "/mˈoʊtɚkˌɑrz/", "vi": "xe hơi; ô tô"},
  {"id": "lex.en.200k.058563", "hw": "mullas", "pos": "noun", "ipa": "/mˈʌləz/", "vi": "giáo sĩ Hồi giáo mullah"},
  {"id": "lex.en.200k.058564", "hw": "nymphos", "pos": "noun", "ipa": "/nˈɪmfoʊz/", "vi": "người phụ nữ mắc chứng cuồng dâm"},
  {"id": "lex.en.200k.058565", "hw": "obstructionists", "pos": "noun", "ipa": "/əbstrˈʌkʃənəsts/", "vi": "kẻ cản trở tiến trình nghị trường"},
  {"id": "lex.en.200k.058566", "hw": "oligonucleotides", "pos": "noun", "ipa": "/ˌɑːlɪɡoʊnˌuːkliːətˈaɪdz/", "vi": "chuỗi ngắn oligonucleotide"},
  {"id": "lex.en.200k.058567", "hw": "outcroppings", "pos": "noun", "ipa": "/ˈaʊtkrɑːpɪŋz/", "vi": "mỏm đá lộ thiên; khối đá trồi"},
  {"id": "lex.en.200k.058568", "hw": "penicillia", "pos": "noun", "ipa": "/pˌɛnəsˈɪliə/", "vi": "chi nấm penicillium"},
  {"id": "lex.en.200k.058569", "hw": "penicilliums", "pos": "noun", "ipa": "/pˌɛnəsˈɪliəmz/", "vi": "nấm mốc penicillium"},
  {"id": "lex.en.200k.058570", "hw": "piafs", "pos": "noun", "ipa": "/piːˈɑːfs/", "vi": "danh ca Édith Piaf"},
  {"id": "lex.en.200k.058571", "hw": "polygamists", "pos": "noun", "ipa": "/pəlˈɪɡəmɪsts/", "vi": "người theo chế độ đa thê"},
  {"id": "lex.en.200k.058572", "hw": "prahas", "pos": "noun", "ipa": "/prˈɑːhəz/", "vi": "thành phố Praha"},
  {"id": "lex.en.200k.058573", "hw": "quires", "pos": "noun", "ipa": "/kwˈaɪɚz/", "vi": "tập 24 tờ giấy; ram giấy quire"},
  {"id": "lex.en.200k.058574", "hw": "recapitulations", "pos": "noun", "ipa": "/rˌikəpˌɪtʃəlˈeɪʃənz/", "vi": "sự tóm tắt lại; phần nhắc lại"},
  {"id": "lex.en.200k.058575", "hw": "recces", "pos": "noun", "ipa": "/rˈɛkiz/", "vi": "chuyến thám thính; trinh sát"},
  {"id": "lex.en.200k.058576", "hw": "retinitides", "pos": "noun", "ipa": "/rˌɛtənˈaɪtɪdiːz/", "vi": "bệnh viêm võng mạc"},
  {"id": "lex.en.200k.058577", "hw": "salats", "pos": "noun", "ipa": "/səˈlɑːts/", "vi": "lễ cầu nguyện salat Hồi giáo"},
  {"id": "lex.en.200k.058578", "hw": "shipowners", "pos": "noun", "ipa": "/ʃˈɪpˌoʊnɚz/", "vi": "chủ tàu thủy"},
  {"id": "lex.en.200k.058579", "hw": "snakebites", "pos": "noun", "ipa": "/snˈeɪkbˌaɪts/", "vi": "vết rắn cắn; nọc rắn cắn"},
  {"id": "lex.en.200k.058580", "hw": "sparklers", "pos": "noun", "ipa": "/spˈɑːrklɚz/", "vi": "que pháo bông; pháo sáng cầm tay"},
  {"id": "lex.en.200k.058581", "hw": "stirrers", "pos": "noun", "ipa": "/stˈɜːrɚz/", "vi": "que khuấy; kẻ khuấy động rắc rối"},
  {"id": "lex.en.200k.058582", "hw": "svelter", "pos": "adj", "ipa": "/svˈɛltɚ/", "vi": "mảnh mai hơn; thon thả hơn"},
  {"id": "lex.en.200k.058583", "hw": "sveltest", "pos": "adj", "ipa": "/svˈɛltɪst/", "vi": "mảnh mai nhất; thon thả nhất"},
  {"id": "lex.en.200k.058584", "hw": "tassos", "pos": "noun", "ipa": "/tˈɑːsoʊz/", "vi": "nhà thơ Tasso"},
  {"id": "lex.en.200k.058585", "hw": "teasdales", "pos": "noun", "ipa": "/tˈizdeɪlz/", "vi": "nhà thơ Teasdale"},
  {"id": "lex.en.200k.058586", "hw": "theravadas", "pos": "noun", "ipa": "/tˌɛrəvˈɑːdəz/", "vi": "Phật giáo Nam truyền Theravada"},
  {"id": "lex.en.200k.058587", "hw": "thuringias", "pos": "noun", "ipa": "/θjʊrˈɪndʒiəz/", "vi": "bang Thüringen của Đức"},
  {"id": "lex.en.200k.058588", "hw": "toupees", "pos": "noun", "ipa": "/tuːpˈeɪz/", "vi": "bộ tóc giả che hói đầu"},
  {"id": "lex.en.200k.058589", "hw": "tourers", "pos": "noun", "ipa": "/tˈʊrɚz/", "vi": "xe du lịch đường trường"},
  {"id": "lex.en.200k.058590", "hw": "trusteeships", "pos": "noun", "ipa": "/trʌstˈiːʃɪps/", "vi": "chế độ ủy thác; quyền giám hộ"},
  {"id": "lex.en.200k.058591", "hw": "untruths", "pos": "noun", "ipa": "/əntrˈuθs/", "vi": "lời nói dối; điều sai sự thật"},
  {"id": "lex.en.200k.058592", "hw": "upjohns", "pos": "noun", "ipa": "/ˈʌpdʒɑːnz/", "vi": "hãng dược Upjohn"},
  {"id": "lex.en.200k.058593", "hw": "vilnas", "pos": "noun", "ipa": "/vˈɪlnəz/", "vi": "thành phố Vilna"},
  {"id": "lex.en.200k.058594", "hw": "vistulas", "pos": "noun", "ipa": "/vˈɪstʃʊləz/", "vi": "sông Vistula ở Ba Lan"},
  {"id": "lex.en.200k.058595", "hw": "warhorses", "pos": "noun", "ipa": "/wˈɔːrhɔːrsɪz/", "vi": "ngựa chiến; lão tướng dày dạn"},
  {"id": "lex.en.200k.058596", "hw": "willets", "pos": "noun", "ipa": "/wˈɪlɪts/", "vi": "chim dẽ mỏ thẳng willet"},
  {"id": "lex.en.200k.058597", "hw": "windups", "pos": "noun", "ipa": "/wˈaɪndʌps/", "vi": "đoạn kết; tư thế ném bóng chày"},
  {"id": "lex.en.200k.058598", "hw": "wycliffes", "pos": "noun", "ipa": "/wˈɪklɪfs/", "vi": "nhà cải cách Wycliffe"},
  {"id": "lex.en.200k.058599", "hw": "yellowtails", "pos": "noun", "ipa": "/jˈɛloʊteɪlz/", "vi": "cá đuôi vàng; cá cam Nhật Bản"},
  {"id": "lex.en.200k.058600", "hw": "zambonis", "pos": "noun", "ipa": "/zæmbˈoʊniz/", "vi": "máy là phẳng mặt sân băng"},
  {"id": "lex.en.200k.058601", "hw": "ad valorem", "pos": "phrase", "ipa": "/æd vəˈlɔːrəm/", "vi": "tính theo giá trị hàng hóa"}
]

with open('scratch/b32_r08_raw_p1.json') as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"Mismatch id at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"Mismatch hw at {i}: {item['hw']} vs {r['hw']}"
    assert len(item['vi']) <= 35, f"vi length > 35 at {i} ({item['hw']}): {len(item['vi'])}"
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {item['pos']}"
    if ' ' not in item['hw']:
        assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Invalid ipa at {i}: {item['ipa']}"
    r['pos'] = item['pos']
    r['ipa'] = item['ipa']
    r['vi'] = item['vi']
    r['status'] = 'reviewed'

with open('scratch/b32_r08_p1.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Part 1 validated and written successfully.")
