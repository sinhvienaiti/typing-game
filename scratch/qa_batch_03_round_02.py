import json

OVERRIDES_B03_R02 = {
    # 501-550
    "lex.en.100k.010501": {"vi": "bản lề cửa; điểm mấu chốt"},  # hinge
    "lex.en.100k.010504": {"vi": "vô đạo đức; trái luân thường"},  # immoral
    "lex.en.100k.010506": {"vi": "bệnh cúm mùa (influenza)"},  # influenza
    "lex.en.100k.010507": {"vi": "thông dịch viên; trình thông dịch"},  # interpreter
    "lex.en.100k.010517": {"vi": "vụ sạt lở đất; thắng áp đảo"},  # landslide
    "lex.en.100k.010521": {"vi": "dịu ngọt; êm dịu; đằm thắm"},  # mellow
    "lex.en.100k.010527": {"pos": "verb", "vi": "nhân lên; sinh sôi; làm phép nhân"},  # multiply
    "lex.en.100k.010528": {"vi": "rau cải thảo; thung lũng Napa"},  # napa
    "lex.en.100k.010530": {"vi": "tầng lớp quý tộc; phẩm giá cao"},  # nobility
    "lex.en.100k.010531": {"vi": "sự lãng quên; cõi hư vô"},  # oblivion
    "lex.en.100k.010532": {"vi": "khí ô-zôn; tầng ô-zôn"},  # ozone
    "lex.en.100k.010534": {"vi": "chứng bại liệt; sự tê liệt"},  # paralysis
    "lex.en.100k.010538": {"vi": "sự kiên trì bền bỉ; tính dai dẳng"},  # persistence
    "lex.en.100k.010540": {"vi": "vua Pha-ra-ông Ai Cập"},  # pharaoh
    "lex.en.100k.010541": {"vi": "hạt photon; quang tử ánh sáng"},  # photon
    "lex.en.100k.010545": {"vi": "trì hoãn; hoãn lại"},  # postpone
    "lex.en.100k.010550": {"vi": "tiên lượng bệnh; dự báo tương lai"},  # prognosis

    # 551-600
    "lex.en.100k.010555": {"vi": "đồng một bảng Anh (lóng quid)"},  # quid
    "lex.en.100k.010556": {"vi": "báo giá thương mại; câu trích"},  # quotation
    "lex.en.100k.010557": {"vi": "được cải tạo; được tái sinh"},  # reclaimed
    "lex.en.100k.010561": {"vi": "sự trấn áp chính trị; kìm nén"},  # repression
    "lex.en.100k.010562": {"vi": "việc truy xuất dữ liệu; tìm lại"},  # retrieval
    "lex.en.100k.010564": {"vi": "cây thanh hương trà (rowan)"},  # rowan
    "lex.en.100k.010572": {"vi": "mẩu vụn; mảnh cắt nhỏ"},  # shred
    "lex.en.100k.010574": {"vi": "người trượt ván; người trượt băng"},  # skater
    "lex.en.100k.010575": {"vi": "tiếng hít mũi; sự khịt mũi"},  # sniff
    "lex.en.100k.010577": {"vi": "khả năng trả nợ; dung môi"},  # solvent
    "lex.en.100k.010578": {"vi": "chim sẻ; chim sẻ nhà"},  # sparrow (fixed single character 'sẻ')
    "lex.en.100k.010581": {"vi": "mùi hôi thối; sự tồi tệ"},  # stink
    "lex.en.100k.010584": {"vi": "công nghị giáo hội; hội nghị"},  # synod
    "lex.en.100k.010587": {"vi": "nhóm ba người; quan hệ tay ba"},  # threesome
    "lex.en.100k.010591": {"vi": "không thể chịu nổi; quá sức"},  # unbearable
    "lex.en.100k.010599": {"vi": "không thể ngăn cản; dũng mãnh"},  # unstoppable
    "lex.en.100k.010600": {"vi": "chưa từng kể; vô số; khôn xiết"},  # untold

    # 601-650
    "lex.en.100k.010603": {"vi": "hành vi phá hoại của công"},  # vandalism
    "lex.en.100k.010606": {"vi": "đơn vị điện thế vôn (V)"},  # volt
    "lex.en.100k.010613": {"vi": "họ Jackson; tên riêng Jackson"},  # jackson
    "lex.en.100k.010614": {"vi": "tên riêng Adam; tổ phụ Adam"},  # adam
    "lex.en.100k.010615": {"vi": "tên riêng Andrew; Sứ đồ Andrew"},  # andrew
    "lex.en.100k.010616": {"vi": "họ Clinton; cựu tổng thống"},  # clinton
    "lex.en.100k.010617": {"vi": "được yêu thích nhất; sở thích"},  # favourite
    "lex.en.100k.010621": {"vi": "khí a-mô-ni-ắc (NH3)"},  # ammonia
    "lex.en.100k.010628": {"vi": "cô; dì; bác gái"},  # auntie
    "lex.en.100k.010631": {"vi": "màu be; màu nâu vàng nhạt"},  # beige (fixed single character 'be')
    "lex.en.100k.010633": {"vi": "gối ôm; sự củng cố; tăng cường"},  # bolster
    "lex.en.100k.010635": {"vi": "cám gạo; cám ngũ cốc"},  # bran
    "lex.en.100k.010640": {"vi": "máy bay trực thăng; dao chặt thịt"},  # chopper
    "lex.en.100k.010644": {"vi": "lính đặc nhiệm; lính biệt kích"},  # commando
    "lex.en.100k.010647": {"vi": "tính toán dữ liệu; xử lý số liệu"},  # compute

    # 651-700
    "lex.en.100k.010654": {"vi": "vành nhật hoa; vi-rút corona"},  # corona
    "lex.en.100k.010656": {"vi": "lừa dối; lừa gạt; đánh lừa"},  # deceive
    "lex.en.100k.010657": {"vi": "khoản khấu trừ thuế; phép diễn dịch"},  # deduction
    "lex.en.100k.010658": {"vi": "cho rằng; coi là; phán đoán"},  # deem
    "lex.en.100k.010662": {"vi": "tính khí; tính tình; sự sắp đặt"},  # disposition
    "lex.en.100k.010664": {"vi": "sự cập bến tàu; kết nối dock sạc"},  # docking
    "lex.en.100k.010672": {"vi": "ăn sâu bám rễ; cố thủ vững chắc"},  # entrenched
    "lex.en.100k.010680": {"vi": "ánh chói lóa; cái nhìn trừng trừng"},  # glare
    "lex.en.100k.010681": {"vi": "rõ rành rành; chói chang gay gắt"},  # glaring
    "lex.en.100k.010684": {"vi": "hẻm núi sâu; vực thẳm"},  # gorge
    "lex.en.100k.010685": {"vi": "quân du kích; lối đánh du kích"},  # guerrilla
    "lex.en.100k.010687": {"vi": "chuột hamster; chuột kiểng"},  # hamster
    "lex.en.100k.010691": {"vi": "người giúp việc; người hỗ trợ"},  # helper (purged awkward 'phó thủ')
    "lex.en.100k.010692": {"vi": "hệ thập lục phân (hex); bùa chú"},  # hex
    "lex.en.100k.010697": {"vi": "thủy tức; quái vật nhiều đầu"},  # hydra
    "lex.en.100k.010700": {"vi": "màu xanh chàm (indigo)"},  # indigo

    # 701-750
    "lex.en.100k.010705": {"vi": "cơn ngứa; sự ngứa ngáy; khao khát"},  # itch
    "lex.en.100k.010707": {"vi": "hát karaoke"},  # karaoke
    "lex.en.100k.010709": {"vi": "khớp ngón tay; cú đấm tay gấu"},  # knuckles
    "lex.en.100k.010710": {"vi": "nhựa cánh kiến (lac); một vạn"},  # lac
    "lex.en.100k.010718": {"vi": "mõm thú; rọ mõm; họng súng"},  # muzzle
    "lex.en.100k.010720": {"vi": "vỏ hạt cứng; tóm gọn ngắn gọn"},  # nutshell
    "lex.en.100k.010721": {"vi": "cáo phó; điếu văn tưởng niệm"},  # obituary
    "lex.en.100k.010731": {"vi": "dưa muối; đồ chua ngâm giấm"},  # pickle
    "lex.en.100k.010734": {"vi": "sùng đạo; ngoan đạo; sùng kính"},  # pious
    "lex.en.100k.010747": {"vi": "di tích; di vật lịch sử; cổ vật"},  # relic
    "lex.en.100k.010750": {"vi": "tiết mục biểu diễn; vốn bài bản"},  # repertoire
    "lex.en.100k.010753": {"vi": "làm chậm lại; kìm hãm tiến độ"},  # retard

    # 751-800
    "lex.en.100k.010761": {"vi": "liền mạch; trơn tru không ngắt"},  # seamless
    "lex.en.100k.010765": {"vi": "con sên trần; đường dẫn slug (IT)"},  # slug
    "lex.en.100k.010766": {"pos": "verb", "vi": "tăng vọt vút cao; bay lượn"},  # soar
    "lex.en.100k.010768": {"vi": "trì trệ; tù đọng; không phát triển"},  # stagnant
    "lex.en.100k.010776": {"vi": "đinh ghim mũ; hướng giải quyết"},  # tack
    "lex.en.100k.010778": {"vi": "gân cơ (y học)"},  # tendon
    "lex.en.100k.010779": {"vi": "nhà tư tưởng; người suy nghĩ sâu"},  # thinker
    "lex.en.100k.010781": {"vi": "đi ngang qua; duyệt qua (IT)"},  # traverse
    "lex.en.100k.010785": {"pos": "adj", "vi": "nâng cao tinh thần; phấn chấn"},  # uplifting
    "lex.en.100k.010789": {"vi": "biến mất; tan biến; biến mất tăm"},  # vanish
    "lex.en.100k.010791": {"vi": "loài rắn lục độc (viper)"},  # viper
    "lex.en.100k.010795": {"vi": "loài ong bắp cày"},  # wasp
    "lex.en.100k.010798": {"vi": "một cách sai lầm; oan uổng"},  # wrongly
    "lex.en.100k.010799": {"vi": "con ngựa vằn"},  # zebra

    # 801-850
    "lex.en.100k.010803": {"vi": "công tố viên quận (DA)"},  # da
    "lex.en.100k.010809": {"vi": "họ Wilson; tên riêng Wilson"},  # wilson
    "lex.en.100k.010813": {"vi": "nghịch cảnh; hoàn cảnh khó khăn"},  # adversity
    "lex.en.100k.010822": {"vi": "mỏ chim; mũi khoằm"},  # beak
    "lex.en.100k.010828": {"vi": "chớp nháy; chết tiệt (lóng)"},  # blinking
    "lex.en.100k.010829": {"vi": "nở hoa rực rỡ; chết tiệt (lóng)"},  # blooming
    "lex.en.100k.010830": {"vi": "quả việt quất"},  # blueberry
    "lex.en.100k.010832": {"vi": "cuốn tài liệu quảng cáo (brochure)"},  # brochure
    "lex.en.100k.010837": {"vi": "đàn trung cầm (cello)"},  # cello
    "lex.en.100k.010842": {"vi": "cô gái trẻ (tiếng Ireland)"},  # colleen
    "lex.en.100k.010845": {"vi": "biến chứng y khoa; sự phức tạp"},  # complication
    "lex.en.100k.010848": {"vi": "mâu thuẫn với; cãi lại; phủ nhận"},  # contradict
    "lex.en.100k.010850": {"vi": "viên đá tảng; nền móng cơ sở"},  # cornerstone

    # 851-900
    "lex.en.100k.010856": {"vi": "trang trí; trang hoàng nhà cửa"},  # decorate
    "lex.en.100k.010859": {"pos": "noun", "vi": "hậu duệ; con cháu đời sau"},  # descendant
    "lex.en.100k.010863": {"vi": "tên riêng Edward"},  # edward
    "lex.en.100k.010867": {"vi": "đá nhám mài kim loại"},  # emery
    "lex.en.100k.010871": {"vi": "ở bên ngoài; từ bên ngoài"},  # externally
    "lex.en.100k.010874": {"vi": "lông mày; chân mày"},  # eyebrow
    "lex.en.100k.010875": {"vi": "tiên nữ; yêu tinh tí hon"},  # fay
    "lex.en.100k.010876": {"vi": "thất bại thảm hại; mớ bòng bong"},  # fiasco
    "lex.en.100k.010878": {"vi": "quá trình lọc; sự thẩm thấu"},  # filtration
    "lex.en.100k.010880": {"vi": "việc định dạng văn bản (IT)"},  # formatting
    "lex.en.100k.010882": {"vi": "đơn vị đo foot (ft); hợp tác"},  # ft
    "lex.en.100k.010883": {"vi": "thuộc về dạ dày (y học)"},  # gastric
    "lex.en.100k.010885": {"vi": "đau buồn; thương tiếc; đau xót"},  # grieve
    "lex.en.100k.010888": {"vi": "điện ảnh Hollywood"},  # hollywood
    "lex.en.100k.010890": {"vi": "giọng khàn; vạm vỡ; chó tuyết"},  # husky
    "lex.en.100k.010894": {"vi": "không đúng cách; không phù hợp"},  # improperly
    "lex.en.100k.010897": {"vi": "địa ngục; biển lửa ngút trời"},  # inferno
    "lex.en.100k.010899": {"vi": "cuộc nổi dậy vũ trang; nổi loạn"},  # insurgency
    "lex.en.100k.010900": {"vi": "đe dọa; hăm dọa; uy hiếp"},  # intimidate (purged dialect 'trộ')

    # 901-950
    "lex.en.100k.010903": {"vi": "gọi hàm (IT invoke); viện dẫn"},  # invoke
    "lex.en.100k.010905": {"vi": "tên riêng Joseph"},  # joseph
    "lex.en.100k.010911": {"vi": "thùy não; dái tai (y học)"},  # lobe
    "lex.en.100k.010912": {"vi": "nhà vệ sinh (tiếng lóng Anh)"},  # loo
    "lex.en.100k.010913": {"vi": "tệ hại; dở tệ; bẩn thỉu"},  # lousy
    "lex.en.100k.010917": {"vi": "điều không may; tai ương; bất hạnh"},  # misfortune (fixed single character 'nạn')
    "lex.en.100k.010919": {"vi": "hoa phong lan"},  # orchid
    "lex.en.100k.010924": {"vi": "hòa bình; sự bình an (Pax)"},  # pax
    "lex.en.100k.010931": {"vi": "dược sĩ; người bán thuốc"},  # pharmacist
    "lex.en.100k.010933": {"vi": "hệ thống cọc móng; cọc đóng móng"},  # piling
    "lex.en.100k.010938": {"vi": "thuộc thời tiền sử"},  # prehistoric
    "lex.en.100k.010941": {"vi": "ưu tiên; đặt quyền ưu tiên trước"},  # prioritize
    "lex.en.100k.010945": {"vi": "tiếng lạch cạch; lục lạc đồ chơi"},  # rattle
    "lex.en.100k.010949": {"vi": "tàn dư; mảnh vải vụn còn sót"},  # remnant

    # 951-1000
    "lex.en.100k.010955": {"vi": "có hương thơm; ngát hương"},  # scented
    "lex.en.100k.010963": {"vi": "cái nhún vai"},  # shrug
    "lex.en.100k.010965": {"vi": "sự chân thành; tính thành thật"},  # sincerity
    "lex.en.100k.010967": {"vi": "giọng nữ cao (soprano)"},  # soprano
    "lex.en.100k.010982": {"vi": "lỗi chính tả; lỗi gõ phím"},  # typo (purged 'của thợ in')
    "lex.en.100k.010983": {"vi": "kẻ bạo chúa; kẻ độc tài bạo ngược"},  # tyrant
    "lex.en.100k.010987": {"vi": "sự đoàn kết; sự hợp nhất"},  # uniting
    "lex.en.100k.010990": {"vi": "người tự ý hành pháp trị tội"},  # vigilante
    "lex.en.100k.010992": {"vi": "trực quan hóa dữ liệu; hình dung"},  # visualization
    "lex.en.100k.010996": {"vi": "khóa kéo; dây kéo áo quần"},  # zipper
    "lex.en.100k.010997": {"vi": "sự phòng thủ; quốc phòng"},  # defence
    "lex.en.100k.010999": {"vi": "nước Jordan; dòng sông Jordan"},  # jordan
}

# Verify lengths <= 35
for k, v in OVERRIDES_B03_R02.items():
    if "vi" in v:
        assert len(v["vi"]) <= 35, f"Length > 35 for {k}: {v['vi']} ({len(v['vi'])})"

with open('content/english/qa-batches/batch-03.json', 'r', encoding='utf-8') as f:
    batch_data = json.load(f)

records = batch_data['records']
target_records = records[500:1000]

applied_count = 0
for r in target_records:
    rid = r['id']
    if rid in OVERRIDES_B03_R02:
        for k, v in OVERRIDES_B03_R02[rid].items():
            r[k] = v
        applied_count += 1
    assert len(r['vi']) <= 35, f"Target record length > 35: {rid} {r['vi']}"

# Update reviewedCount for Batch 03 to 1000 (Round 2 completed)
batch_data['reviewedCount'] = 1000

with open('content/english/qa-batches/batch-03.json', 'w', encoding='utf-8') as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully applied Batch 03 Round 2 ({applied_count} overrides). Reviewed: 1000/5000.")
