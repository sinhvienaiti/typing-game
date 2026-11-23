import json

OVERRIDES_ROUND_10 = {
    # 4501-4550
    "lex.en.100k.009501": {"vi": "lời thú nhận; sự xưng tội"},  # confession
    "lex.en.100k.009504": {"vi": "sự chinh phục; sự xâm chiếm"},  # conquest
    "lex.en.100k.009508": {"pos": "noun", "vi": "phóng viên thường trú; tương ứng"},  # correspondent
    "lex.en.100k.009510": {"vi": "con cua"},  # crab
    "lex.en.100k.009518": {"vi": "ảo tưởng; sự hoang tưởng"},  # delusion
    "lex.en.100k.009519": {"vi": "đáng mơ ước; đáng khao khát"},  # desirable (purged 'đáng làm vợ/chồng')
    "lex.en.100k.009522": {"vi": "chứng chỉ; bằng tốt nghiệp"},  # diploma
    "lex.en.100k.009523": {"vi": "tủ có ngăn kéo; người phụ việc"},  # dresser
    "lex.en.100k.009530": {"vi": "sự hạnh phúc tuyệt vời; tinh tế"},  # felicity
    "lex.en.100k.009531": {"vi": "thuộc thời phong kiến"},  # feudal
    "lex.en.100k.009533": {"vi": "bị làm phẳng; bẹp gí; san phẳng"},  # flattened
    "lex.en.100k.009536": {"vi": "cỏ khô cho gia súc; tài liệu vụn"},  # fodder
    "lex.en.100k.009541": {"vi": "thuộc chính phủ; cơ quan nhà nước"},  # governmental
    "lex.en.100k.009543": {"vi": "dấu ấn đặc trưng; phẩm chất tiêu biểu"},  # hallmark (37 chars!) -> wait, check length
    "lex.en.100k.009545": {"vi": "hàng rào bụi cây; phòng vệ rủi ro"},  # hedge
    "lex.en.100k.009547": {"vi": "thảo mộc; cây cỏ làm thuốc"},  # herb
    "lex.en.100k.009550": {"vi": "hoa bia (nấu bia)"},  # hops

    # 4551-4600
    "lex.en.100k.009552": {"vi": "vệ sinh; giữ vệ sinh sạch sẽ"},  # hygiene
    "lex.en.100k.009555": {"vi": "ngớ ngẩn; ngu ngốc; điên rồ"},  # idiotic
    "lex.en.100k.009559": {"vi": "hoàn hảo; không tì vết; tinh tươm"},  # immaculate (purged single word 'phau')
    "lex.en.100k.009560": {"vi": "án phạt tù; sự giam giữ"},  # imprisonment
    "lex.en.100k.009569": {"vi": "dung nham núi lửa"},  # lava
    "lex.en.100k.009571": {"vi": "theo nghĩa đen; nguyên văn"},  # literal
    "lex.en.100k.009572": {"vi": "tội ngộ sát; vô ý làm chết người"},  # manslaughter
    "lex.en.100k.009578": {"vi": "vữa xây dựng; cối giã; súng cối"},  # mortar
    "lex.en.100k.009581": {"vi": "người kể chuyện; người thuyết minh"},  # narrator
    "lex.en.100k.009583": {"vi": "lạc quan; đầy hy vọng"},  # optimistic
    "lex.en.100k.009585": {"vi": "sự phẫn nộ tột cùng; bức xúc"},  # outrage
    "lex.en.100k.009587": {"pos": "adj", "vi": "mang tính bè phái; thiên vị"},  # partisan
    "lex.en.100k.009590": {"vi": "nội dung khiêu dâm (18+)"},  # porno
    "lex.en.100k.009595": {"vi": "thể loại văn xuôi"},  # prose
    "lex.en.100k.009598": {"vi": "suy thoái kinh tế; sự sa sút"},  # recession
    "lex.en.100k.009599": {"vi": "cho rằng; tính toán; ước tính"},  # reckon
    "lex.en.100k.009600": {"vi": "cán bộ hộ tịch; chuyên viên đăng ký"},  # registrar (36 chars!) -> wait, check length

    # 4601-4650
    "lex.en.100k.009601": {"vi": "sự từ chối; sự bác bỏ"},  # rejection
    "lex.en.100k.009603": {"vi": "miễn cưỡng; do dự; bất đắc dĩ"},  # reluctant
    "lex.en.100k.009609": {"vi": "tấm thảm trải sàn"},  # rug
    "lex.en.100k.009610": {"vi": "mặn mà; vị mặn; cáu kỉnh"},  # salty
    "lex.en.100k.009615": {"vi": "bác sĩ tâm lý; sự co rút lại"},  # shrink
    "lex.en.100k.009618": {"vi": "sự sụt giảm mạnh; suy thoái"},  # slump
    "lex.en.100k.009620": {"vi": "người nào đó; nhân vật quan trọng"},  # somebody
    "lex.en.100k.009621": {"vi": "thưa thớt; rải rác; ít ỏi"},  # sparse
    "lex.en.100k.009623": {"vi": "người phát ngôn; đại diện báo chí"},  # spokesman
    "lex.en.100k.009625": {"vi": "vết bẩn; vết ố; sự hoen ố"},  # stain
    "lex.en.100k.009626": {"vi": "đói lả; chết đói; rất đói"},  # starving
    "lex.en.100k.009627": {"pos": "verb", "vi": "lái xe; định hướng; dẫn dắt"},  # steer
    "lex.en.100k.009630": {"vi": "một cách đầy đủ; thỏa đáng"},  # sufficiently
    "lex.en.100k.009636": {"vi": "có đuôi; bị bám đuôi theo dõi"},  # tailed
    "lex.en.100k.009637": {"vi": "bắp đùi; phần đùi"},  # thigh
    "lex.en.100k.009640": {"vi": "tha thứ; chịu đựng; dung thứ"},  # tolerate
    "lex.en.100k.009641": {"vi": "để ngực trần; không mái che"},  # topless
    "lex.en.100k.009643": {"vi": "nhà giao dịch (trader); thương nhân"},  # trader
    "lex.en.100k.009647": {"vi": "không thể chấp nhận được"},  # unacceptable
    "lex.en.100k.009650": {"vi": "thói phù phiếm; lòng kiêu căng"},  # vanity

    # 4651-4700
    "lex.en.100k.009653": {"vi": "vi phạm; xâm phạm quyền lợi"},  # violate
    "lex.en.100k.009656": {"vi": "vô giá trị; không có giá trị"},  # worthless
    "lex.en.100k.009660": {"vi": "tên riêng Charles"},  # charles
    "lex.en.100k.009662": {"vi": "nhà nước Israel"},  # israel
    "lex.en.100k.009663": {"vi": "không bên nào; cả hai đều không"},  # neither
    "lex.en.100k.009666": {"vi": "tuổi vị thành niên; tuổi dậy thì"},  # adolescence
    "lex.en.100k.009671": {"vi": "sự so sánh tương tự; phép loại suy"},  # analogy
    "lex.en.100k.009675": {"vi": "kiêu ngạo; ngạo mạn; tự cao"},  # arrogant
    "lex.en.100k.009676": {"vi": "khẳng định; quả quyết"},  # asserting
    "lex.en.100k.009677": {"vi": "thuộc tính; đặc tính"},  # attribute (noun)
    "lex.en.100k.009678": {"vi": "chờ đợi; đón chờ"},  # await
    "lex.en.100k.009686": {"vi": "thanh cản xe ô tô; bội thu"},  # bumper
    "lex.en.100k.009692": {"vi": "cá da trơn; kẻ giả danh trên mạng"},  # catfish
    "lex.en.100k.009694": {"vi": "kẹo cao su nhai; miếng nhai"},  # chew (noun)

    # 4701-4750
    "lex.en.100k.009701": {"vi": "sự thụ thai; quan niệm; ý niệm"},  # conception
    "lex.en.100k.009703": {"vi": "hợp tác; cộng tác; chung sức"},  # cooperate
    "lex.en.100k.009704": {"vi": "dây thừng nhỏ; quần vải nhung kẻ"},  # cords
    "lex.en.100k.009708": {"vi": "cơn sốt nhất thời; trào lưu rộ"},  # craze
    "lex.en.100k.009713": {"vi": "tài liệu tóm tắt; bản tin vắn"},  # digest
    "lex.en.100k.009714": {"vi": "đồng xu mười cent (dime)"},  # dime
    "lex.en.100k.009717": {"vi": "gây xao nhãng; làm phân tâm"},  # distract
    "lex.en.100k.009718": {"vi": "sự xao nhãng; làm mất tập trung"},  # distraction
    "lex.en.100k.009719": {"vi": "chim bồ câu trắng; phái hòa bình"},  # dove
    "lex.en.100k.009721": {"vi": "cuộc đấu tay đôi; cuộc đọ sức"},  # duel
    "lex.en.100k.009726": {"vi": "men răng; lớp men tráng"},  # enamel
    "lex.en.100k.009730": {"vi": "sắp diễn ra; sắp tới; cởi mở"},  # forthcoming
    "lex.en.100k.009733": {"vi": "sự vĩ đại; tầm vóc vĩ đại"},  # greatness
    "lex.en.100k.009734": {"vi": "ảm đạm; u ám; nghiệt ngã"},  # grim
    "lex.en.100k.009735": {"vi": "thiết bị cầm tay; nhỏ gọn"},  # handheld
    "lex.en.100k.009741": {"vi": "bốc cháy; châm ngòi; kích hoạt"},  # ignite
    "lex.en.100k.009747": {"vi": "điều tra viên; nhà nghiên cứu"},  # investigator
    "lex.en.100k.009749": {"vi": "cú đấm thẳng; mũi tiêm vắc-xin"},  # jab
    "lex.en.100k.009750": {"vi": "nút thắt; mối dây; hải lý"},  # knot

    # 4751-4800
    "lex.en.100k.009752": {"vi": "tay chân; chi thể; cành cây lớn"},  # limb (PURGED 'but see chân tay')
    "lex.en.100k.009753": {"vi": "tiền vệ phòng ngự (bóng bầu dục)"},  # linebacker
    "lex.en.100k.009754": {"vi": "rác thải bừa bãi; lứa con sơ sinh"},  # litter
    "lex.en.100k.009758": {"vi": "kiệt tác nghệ thuật; tác phẩm lớn"},  # masterpiece
    "lex.en.100k.009760": {"vi": "phép ẩn dụ"},  # metaphor
    "lex.en.100k.009761": {"vi": "lò vi sóng; sóng viba"},  # microwave
    "lex.en.100k.009763": {"vi": "màn sương mù mỏng"},  # mist
    "lex.en.100k.009767": {"vi": "tỷ lệ lấp đầy phòng; sự cư trú"},  # occupancy
    "lex.en.100k.009771": {"vi": "sự tràn ngập; chi phí vượt dự toán"},  # overrun
    "lex.en.100k.009772": {"pos": "noun", "vi": "đại dịch toàn cầu; tính đại dịch"},  # pandemic
    "lex.en.100k.009777": {"vi": "trọng tải; gói dữ liệu (IT)"},  # payload
    "lex.en.100k.009778": {"pos": "noun", "vi": "bàn đạp chân (xe đạp/đàn)"},  # pedal
    "lex.en.100k.009782": {"vi": "đơn vị đo panh (pint)"},  # pint
    "lex.en.100k.009783": {"vi": "hạt hoa quả; điểm pip (Forex)"},  # pip
    "lex.en.100k.009787": {"vi": "có thể dự đoán trước; dễ đoán"},  # predictable
    "lex.en.100k.009789": {"vi": "uy tín; thanh thế danh giá"},  # prestige
    "lex.en.100k.009792": {"vi": "bên mua; người mua hàng"},  # purchaser
    "lex.en.100k.009795": {"vi": "bất động sản; địa ốc"},  # realty
    "lex.en.100k.009797": {"vi": "thuộc hệ hô hấp"},  # respiratory
    "lex.en.100k.009799": {"vi": "truy xuất dữ liệu (IT); tìm lại"},  # retrieve
    "lex.en.100k.009800": {"vi": "xem xét lại; thăm lại"},  # revisit

    # 4801-4850
    "lex.en.100k.009801": {"vi": "hồi sinh; phục hồi; làm sống lại"},  # revive
    "lex.en.100k.009807": {"vi": "dấu gạch chéo (/); vết chém"},  # slash
    "lex.en.100k.009809": {"vi": "ướt sũng; ngấm nước; say bí tỉ"},  # soaked
    "lex.en.100k.009811": {"vi": "đinh thúc ngựa; động lực thúc đẩy"},  # spur
    "lex.en.100k.009814": {"vi": "nỗ lực; phấn đấu; cố gắng"},  # strive
    "lex.en.100k.009816": {"vi": "môi trường xung quanh; vùng lân cận"},  # surroundings
    "lex.en.100k.009821": {"vi": "đồ rẻ tiền; hình xăm (tattoo)"},  # tat
    "lex.en.100k.009823": {"vi": "độ dày; bề dày"},  # thickness
    "lex.en.100k.009824": {"vi": "đặc điểm; nét tính cách"},  # trait
    "lex.en.100k.009825": {"vi": "kẻ phản bội; kẻ phản quốc"},  # traitor
    "lex.en.100k.009831": {"vi": "sinh viên đại học chưa tốt nghiệp"},  # undergraduate
    "lex.en.100k.009835": {"vi": "không an toàn; nguy hiểm"},  # unsafe
    "lex.en.100k.009837": {"vi": "ngày lễ tình nhân; thiệp Valentine"},  # valentine
    "lex.en.100k.009840": {"pos": "verb", "vi": "kết hôn; cưới gả"},  # wed
    "lex.en.100k.009841": {"pos": "noun", "vi": "trận đòn roi; sự đánh đập"},  # whipping
    "lex.en.100k.009843": {"vi": "vòng hoa tưởng niệm; vòng hoa"},  # wreath
    "lex.en.100k.009845": {"vi": "âm (trong âm dương ngũ hành)"},  # yin
    "lex.en.100k.009847": {"vi": "tên riêng Martin; chim nhạn Martin"},  # martin
    "lex.en.100k.009848": {"vi": "họ người Jones; cơn thèm thuốc"},  # jones

    # 4851-4900
    "lex.en.100k.009858": {"vi": "động mạch; tuyến huyết mạch"},  # artery
    "lex.en.100k.009862": {"vi": "cái rìu; sự sa thải nhân sự"},  # ax
    "lex.en.100k.009864": {"vi": "chỗ uốn cong; bệnh giảm áp (lặn)"},  # bends
    "lex.en.100k.009867": {"vi": "hoa nở rộ; hoa cây ăn quả"},  # blossom
    "lex.en.100k.009868": {"vi": "đầm lầy; bãi lầy than bùn"},  # bog
    "lex.en.100k.009870": {"vi": "sự chia tay; sự đổ vỡ quan hệ"},  # breakup
    "lex.en.100k.009872": {"vi": "nước Anh; Vương quốc Anh"},  # britain
    "lex.en.100k.009878": {"vi": "khối lớn; mẩu; đoạn dữ liệu (IT)"},  # chunk
    "lex.en.100k.009882": {"vi": "bắt buộc; có tính cưỡng chế"},  # compulsory
    "lex.en.100k.009885": {"vi": "xe ô tô 2 cửa mui kín (coupé)"},  # coupe
    "lex.en.100k.009888": {"vi": "uốn xoăn; cong lại"},  # curled
    "lex.en.100k.009890": {"vi": "ban ngày; thời gian ban ngày"},  # daytime
    "lex.en.100k.009894": {"vi": "mờ ảo; lờ mờ; u tối"},  # dim
    "lex.en.100k.009897": {"vi": "con lừa"},  # donkey
    "lex.en.100k.009898": {"pos": "noun", "vi": "nỗi khiếp sợ; sự kinh hoàng"},  # dread

    # 4901-4950
    "lex.en.100k.009914": {"vi": "vũ khí cầm tay; súng ống"},  # firearm (purged archaic 'hỏa khí')
    "lex.en.100k.009915": {"vi": "khiếm khuyết; tì vết; thiếu sót"},  # flaw
    "lex.en.100k.009920": {"vi": "phong cách funk; sôi động; mùi lạ"},  # funky (purged purely 'hôi thối')
    "lex.en.100k.009934": {"vi": "chứng viêm; tình trạng viêm sưng"},  # inflammation
    "lex.en.100k.009937": {"vi": "kiểm tra; thanh tra; giám định"},  # inspect
    "lex.en.100k.009940": {"vi": "họ tên riêng Johnson"},  # johnson
    "lex.en.100k.009944": {"vi": "giảng viên đại học"},  # lecturer
    "lex.en.100k.009949": {"vi": "sự cô đơn; nỗi cô đơn quạnh quẽ"},  # loneliness
    "lex.en.100k.009952": {"vi": "cây ngô; hạt ngô; bắp ngô"},  # maize

    # 4951-5000
    "lex.en.100k.009956": {"vi": "kẻ chủ mưu; bộ óc đầu não"},  # mastermind
    "lex.en.100k.009958": {"vi": "mi-crô; thiết bị thu âm giọng nói"},  # microphone
    "lex.en.100k.009961": {"vi": "sự sửa đổi; sự điều chỉnh"},  # modification
    "lex.en.100k.009964": {"vi": "nàng thơ; nguồn cảm hứng"},  # muse
    "lex.en.100k.009966": {"vi": "điều hướng; định vị dẫn đường"},  # navigate
    "lex.en.100k.009967": {"vi": "không cần thiết; không đáng có"},  # needless
    "lex.en.100k.009971": {"vi": "sự lạc quan; tinh thần tích cực"},  # optimism
    "lex.en.100k.009978": {"pos": "noun", "vi": "người đi bộ"},  # pedestrian
    "lex.en.100k.009980": {"vi": "đã gọt vỏ; đã bóc vỏ"},  # peeled (PURGED crawler 'trần truồng')
    "lex.en.100k.009981": {"vi": "xác định chính xác; điểm bấm"},  # pinpoint
    "lex.en.100k.009983": {"vi": "cú chích nhẹ; kẻ đáng ghét"},  # prick (PURGED SEVERE VULGAR OBSCENITY 'cặc; chim; đồ khốn')
    "lex.en.100k.009985": {"vi": "truy vấn dữ liệu (IT); thắc mắc"},  # query
    "lex.en.100k.009991": {"vi": "sự hạn chế; điều giới hạn"},  # restriction
    "lex.en.100k.009994": {"vi": "han gỉ; cùn; lâu không dùng"},  # rusty
    "lex.en.100k.009996": {"vi": "màu đỏ tươi; đỏ thắm"},  # scarlet
    "lex.en.100k.009997": {"vi": "người Scotland; tên riêng Scott"},  # scott
    "lex.en.100k.009998": {"vi": "hiếm khi; ít khi"},  # seldom
}

# Fix length for hallmark & registrar
OVERRIDES_ROUND_10["lex.en.100k.009543"] = {"vi": "dấu ấn đặc trưng; phẩm chất chuẩn"}
OVERRIDES_ROUND_10["lex.en.100k.009600"] = {"vi": "cán bộ hộ tịch; người đăng ký"}

# Verify length <= 35
for k, v in OVERRIDES_ROUND_10.items():
    if "vi" in v:
        assert len(v["vi"]) <= 35, f"Length > 35 for {k}: {v['vi']} ({len(v['vi'])})"

with open('content/english/qa-batches/batch-02.json', 'r', encoding='utf-8') as f:
    batch_data = json.load(f)

records = batch_data['records']
target_records = records[4500:5000]

applied_count = 0
for r in target_records:
    rid = r['id']
    if rid in OVERRIDES_ROUND_10:
        for k, v in OVERRIDES_ROUND_10[rid].items():
            r[k] = v
        applied_count += 1
    assert len(r['vi']) <= 35, f"Target record length > 35: {rid} {r['vi']}"

# Mark Batch 02 completed!
batch_data['reviewedCount'] = 5000
batch_data['status'] = 'completed'

with open('content/english/qa-batches/batch-02.json', 'w', encoding='utf-8') as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully applied Round 10 ({applied_count} overrides). Total reviewed: 5000/5000. Batch 02 COMPLETED!")
