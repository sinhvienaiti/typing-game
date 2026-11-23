import json

# Round 6 overrides (records 2500 to 3000, STT 2501 to 3000, IDs lex.en.100k.012501 to 013000)
OVERRIDES_B03_R06 = {
    # 2501-2550
    "lex.en.100k.012501": {"vi": "lịch sự; nhã nhặn; lịch thiệp"},  # courteous
    "lex.en.100k.012505": {"vi": "thái độ; phong thái; cách cư xử"},  # demeanor
    "lex.en.100k.012506": {"vi": "bản thử nghiệm; buổi diễn thử"},  # demo
    "lex.en.100k.012509": {"vi": "chất tẩy rửa; bột giặt; tẩy rửa"},  # detergent
    "lex.en.100k.012511": {"pos": "verb", "vi": "nghĩ ra; sáng chế; vạch kế hoạch"},  # devise (pos fixed)
    "lex.en.100k.012514": {"vi": "tính đa dạng; sự phong phú"},  # diversity
    "lex.en.100k.012516": {"vi": "thời gian chết; máy ngưng chạy"},  # downtime
    "lex.en.100k.012518": {"vi": "máy sấy khô; chất làm khô"},  # drier
    "lex.en.100k.012519": {"vi": "cái tôi cá nhân; lòng tự trọng"},  # ego
    "lex.en.100k.012520": {"vi": "vùng lãnh thổ trong nước khác"},  # enclave
    "lex.en.100k.012523": {"vi": "thời đại; kỷ nguyên lịch sử"},  # epoch
    "lex.en.100k.012524": {"vi": "thuộc môn cưỡi ngựa; kỵ sĩ"},  # equestrian
    "lex.en.100k.012526": {"vi": "thuộc đạo đức; đúng luân thường"},  # ethical
    "lex.en.100k.012533": {"vi": "cầu thủ bắt bóng (bóng chày)"},  # fielder
    "lex.en.100k.012534": {"vi": "lính cứu hỏa; thợ xúc than lò"},  # fireman
    "lex.en.100k.012536": {"vi": "cá sấu Nam Mỹ (alligator lóng)"},  # gator
    "lex.en.100k.012538": {"vi": "sự khái quát hóa; quy chụp chung"},  # generalization
    "lex.en.100k.012540": {"vi": "buổi biểu diễn nhạc; việc làm tạm"},  # gig
    "lex.en.100k.012541": {"vi": "chiêu trò câu khách; mẹo quảng cáo"},  # gimmick
    "lex.en.100k.012543": {"vi": "họng súng; bị dí súng uy hiếp"},  # gunpoint
    "lex.en.100k.012544": {"pos": "verb", "vi": "đốn; chém; xâm nhập máy tính"},  # hack
    "lex.en.100k.012545": {"vi": "thành phố Hays; cỏ khô khô ráo"},  # hays
    "lex.en.100k.012548": {"pos": "intj", "vi": "hoan hô!; tiếng reo mừng vui"},  # hooray
    "lex.en.100k.012551": {"vi": "tống giam; bỏ tù; giam giữ"},  # imprison (purged single-word 'bỏ tù')
    "lex.en.100k.012553": {"vi": "một cách ngây thơ; vô tội"},  # innocently
    "lex.en.100k.012556": {"vi": "nhân viên tạp vụ; người dọn dẹp"},  # janitor
    "lex.en.100k.012557": {"vi": "hay phán xét; định kiến khắt khe"},  # judgmental
    "lex.en.100k.012558": {"vi": "sống tàu thuyền; đáy lườn tàu"},  # keel (purged single-word 'sống')
    "lex.en.100k.012559": {"vi": "dâm ô; tục tĩu; khiêu dâm"},  # lewd
    "lex.en.100k.012560": {"vi": "xe sang limousine; xe sang dài"},  # limousine
    "lex.en.100k.012561": {"vi": "cây đoạn (bồ đề châu Âu)"},  # linden
    "lex.en.100k.012563": {"vi": "mắc-ma (núi lửa phun trào)"},  # magma
    "lex.en.100k.012564": {"vi": "có từ tính; có sức hút nam châm"},  # magnetic (purged single-word 'từ')
    "lex.en.100k.012565": {"vi": "phân chuồng; phân bón hữu cơ"},  # manure (purged single-word 'phân')
    "lex.en.100k.012566": {"pos": "noun", "vi": "kỳ quan; điều kỳ diệu; kinh ngạc"},  # marvel
    "lex.en.100k.012567": {"vi": "cơ chế vận hành; bộ máy máy móc"},  # mechanism
    "lex.en.100k.012570": {"vi": "chứng ghét phụ nữ; thói bài nữ"},  # misogyny
    "lex.en.100k.012571": {"vi": "thừa số nhân; hệ số nhân đôi"},  # multiplier
    "lex.en.100k.012573": {"vi": "hệ thống danh pháp khoa học"},  # nomenclature
    "lex.en.100k.012576": {"vi": "béo vị hạt dẻ; gàn dở lẩn thẩn"},  # nutty
    "lex.en.100k.012577": {"vi": "sự mờ mịt; tình trạng vô danh"},  # obscurity
    "lex.en.100k.012578": {"vi": "cuộc tấn công dữ dội; ồ ạt tới"},  # onslaught
    "lex.en.100k.012579": {"vi": "ngọc mắt mèo (đá opal)"},  # opal
    "lex.en.100k.012580": {"vi": "bệnh liệt; chứng bại liệt hay run"},  # palsy
    "lex.en.100k.012581": {"vi": "cây đu đủ; quả đu đủ chín"},  # papaya
    "lex.en.100k.012582": {"vi": "chim đa đa; chim gà gô"},  # partridge
    "lex.en.100k.012583": {"vi": "đặc quyền đãi ngộ; bổng lộc"},  # perk
    "lex.en.100k.012585": {"vi": "thuần khiết tinh thần (Platon)"},  # platonic
    "lex.en.100k.012587": {"vi": "điệu nhảy điệu nhạc polka"},  # polka
    "lex.en.100k.012588": {"vi": "tôm biển lớn; con tôm sú"},  # prawn (purged single-word 'tôm')
    "lex.en.100k.012590": {"vi": "được ưu đãi; dành đặc quyền"},  # preferential
    "lex.en.100k.012591": {"vi": "bộ linh trưởng (động vật học)"},  # primates
    "lex.en.100k.012594": {"vi": "tiếng lách cách; làm rung lắc"},  # rattling
    "lex.en.100k.012597": {"vi": "sự tinh chế; sự cải tiến tinh tế"},  # refinement
    "lex.en.100k.012599": {"vi": "không ngừng nghỉ; không nao núng"},  # relentlessly (purged crawler 'rầm rầm')
    "lex.en.100k.012600": {"vi": "cải tổ tân trang; sửa đổi nâng cấp"},  # revamp

    # 2601-2650
    "lex.en.100k.012601": {"vi": "con tê giác"},  # rhinoceros
    "lex.en.100k.012602": {"vi": "loài gặm nhấm (chuột...)"},  # rodent
    "lex.en.100k.012603": {"vi": "bánh lái tàu thủy/máy bay"},  # rudder
    "lex.en.100k.012604": {"vi": "bậc thang; nấc thang danh vọng"},  # rung (purged single-word 'bậc')
    "lex.en.100k.012605": {"pos": "noun", "vi": "sự hy sinh; vật hiến tế; tế lễ"},  # sacrifice
    "lex.en.100k.012606": {"vi": "kịch bản tình huống; viễn cảnh"},  # scenario
    "lex.en.100k.012608": {"vi": "thủy thủ hải quân; người đi biển"},  # seaman
    "lex.en.100k.012611": {"vi": "sự ngắn ngủi; tình trạng thiếu hụt"},  # shortness
    "lex.en.100k.012612": {"vi": "việc định cỡ; tráng hồ vải"},  # sizing (purged single-word 'hồ')
    "lex.en.100k.012614": {"vi": "xỉ kim loại; xỉ than xỉ quặng"},  # slag (purged single-word 'xỉ')
    "lex.en.100k.012615": {"vi": "giấc ngủ say; giấc ngủ êm đềm"},  # slumber
    "lex.en.100k.012616": {"vi": "tiền som (Kyrgyzstan/Uzbekistan)"},  # som
    "lex.en.100k.012617": {"vi": "trung thành kiên định; cầm máu"},  # staunch
    "lex.en.100k.012618": {"vi": "thay thế; chỗ đứng hữu ích"},  # stead
    "lex.en.100k.012620": {"vi": "thuộc về kết cấu; cấu trúc"},  # structural
    "lex.en.100k.012623": {"vi": "sự phù hợp; tính thích ứng"},  # suitability
    "lex.en.100k.012624": {"vi": "sự đình chỉ; hệ thống treo xe"},  # suspension
    "lex.en.100k.012627": {"vi": "đối xứng; cân đối hai bên"},  # symmetric
    "lex.en.100k.012628": {"vi": "ti vi (truyền hình lóng Anh)"},  # telly
    "lex.en.100k.012629": {"vi": "vô tâm; thiếu suy nghĩ chu đáo"},  # thoughtless
    "lex.en.100k.012630": {"vi": "ngành tô-pô học (toán học)"},  # topology
    "lex.en.100k.012632": {"vi": "sự quá cảnh; việc trung chuyển"},  # transit
    "lex.en.100k.012634": {"vi": "chấn thương; tổn thương tâm lý"},  # trauma
    "lex.en.100k.012639": {"vi": "tính độc đáo; tính độc nhất"},  # uniqueness
    "lex.en.100k.012640": {"vi": "vén màn khánh thành; hé lộ ra"},  # unveil
    "lex.en.100k.012642": {"vi": "đỉnh hình học; chóp nón"},  # vertex (purged single-word 'đỉnh')
    "lex.en.100k.012644": {"vi": "tiếng huýt sáo; tiếng gió rít"},  # whistling
    "lex.en.100k.012645": {"pos": "noun", "vi": "tiếng reo hò; tiếng hú hét"},  # whoop
    "lex.en.100k.012646": {"vi": "đồ gỗ gia dụng; nghề thợ mộc"},  # woodwork
    "lex.en.100k.012649": {"vi": "thành phố Glasgow (Scotland)"},  # glasgow
    "lex.en.100k.012650": {"vi": "tên riêng Helen"},  # helen
    "lex.en.100k.012652": {"vi": "tiểu bang/sông Mississippi"},  # mississippi
    "lex.en.100k.012653": {"vi": "quan hệ công chúng (PR)"},  # pr
    "lex.en.100k.012654": {"vi": "tên riêng Samuel; Sa-mu-ên"},  # samuel
    "lex.en.100k.012655": {"vi": "tên riêng/họ Stanley"},  # stanley
    "lex.en.100k.012656": {"vi": "tên họ Turner; thợ tiện gỗ"},  # turner
    "lex.en.100k.012659": {"ipa": "/ˌɛs ˈsiː/", "vi": "bang South Carolina; chất scandi"},  # sc
    "lex.en.100k.012661": {"vi": "tên họ Watson (bác sĩ Watson)"},  # watson
    "lex.en.100k.012662": {"vi": "vi-rút HIV; hội chứng HIV"},  # hiv
    "lex.en.100k.012663": {"vi": "hạt Kent (nước Anh)"},  # kent
    "lex.en.100k.012664": {"vi": "đại lộ Madison; tên riêng"},  # madison
    "lex.en.100k.012666": {"vi": "tên riêng/họ Tyler"},  # tyler
    "lex.en.100k.012667": {"vi": "tiểu bang Washington; Tây Úc"},  # wa
    "lex.en.100k.012671": {"vi": "mẫu Anh (đo diện tích đất)"},  # acre
    "lex.en.100k.012673": {"vi": "mang tính thẩm mỹ; tính mỹ cảm"},  # aesthetic
    "lex.en.100k.012676": {"vi": "bánh mì vòng (bagel)"},  # bagel
    "lex.en.100k.012678": {"vi": "kẻ cố chấp cuồng tín mù quáng"},  # bigot
    "lex.en.100k.012679": {"vi": "tên họ Blake"},  # blake
    "lex.en.100k.012680": {"vi": "khăn quàng lông; con trăn boa"},  # boa
    "lex.en.100k.012682": {"vi": "ly khai; tách nhóm độc lập"},  # breakaway
    "lex.en.100k.012684": {"vi": "vàng thỏi đúc; bạc thỏi"},  # bullion
    "lex.en.100k.012685": {"vi": "gập ghềnh; xóc nảy mấp mô"},  # bumpy
    "lex.en.100k.012687": {"vi": "cá chép; cằn nhằn bắt bẻ vặt"},  # carp
    "lex.en.100k.012688": {"vi": "dầu thầu dầu; sao Castor"},  # castor
    "lex.en.100k.012690": {"vi": "nhà hùng biện Cicero; cỡ chữ"},  # cicero
    "lex.en.100k.012691": {"vi": "thị tộc dòng họ; bè phái"},  # clan
    "lex.en.100k.012693": {"pos": "verb", "vi": "chộp lấy; côn xe (bộ ly hợp)"},  # clutch
    "lex.en.100k.012698": {"vi": "làm ô nhiễm độc hại; lây nhiễm"},  # contaminate
    "lex.en.100k.012699": {"vi": "nhà thầu xây dựng; hợp đồng"},  # contractor
    "lex.en.100k.012700": {"vi": "sự truyền tải; chuyển nhượng"},  # conveying

    # 2651-2700
    "lex.en.100k.012701": {"vi": "niềm tin vững chắc; án kết tội"},  # conviction
    "lex.en.100k.012707": {"vi": "thô ráp; dầu thô; chưa tinh chế"},  # crude (purged single-word 'thô')
    "lex.en.100k.012710": {"vi": "trục xuất khỏi quốc gia"},  # deport
    "lex.en.100k.012712": {"vi": "pha loãng; làm nhạt bớt"},  # dilute
    "lex.en.100k.012714": {"vi": "suy thoái kinh tế; đà suy giảm"},  # downturn
    "lex.en.100k.012721": {"vi": "đoàn tùy tùng; phái đoàn theo"},  # entourage
    "lex.en.100k.012722": {"vi": "đã bị dập tắt hoàn toàn"},  # extinguished
    "lex.en.100k.012723": {"vi": "khía cạnh vấn đề; mặt cắt đá quý"},  # facet
    "lex.en.100k.012724": {"vi": "sự mệt mỏi; mỏi mệt kiệt sức"},  # fatigue
    "lex.en.100k.012725": {"vi": "chứng xơ hóa mô (y học)"},  # fibrosis
    "lex.en.100k.012727": {"vi": "vịnh hẹp cửa sông (Scotland)"},  # firth
    "lex.en.100k.012729": {"vi": "chỉ nha khoa làm sạch răng"},  # floss
    "lex.en.100k.012731": {"pos": "noun", "vi": "hóa thạch; thuộc về hóa thạch"},  # fossil
    "lex.en.100k.012734": {"vi": "viên đá quý; ngọc quý"},  # gem
    "lex.en.100k.012735": {"vi": "thuộc ngữ tộc German; cổ Đức"},  # germanic
    "lex.en.100k.012736": {"vi": "mấu chốt; ý chính cốt lõi"},  # gist
    "lex.en.100k.012737": {"vi": "đấu sĩ La Mã cổ đại"},  # gladiator
    "lex.en.100k.012739": {"vi": "bảng thuật ngữ; tra cứu từ vựng"},  # glossary
    "lex.en.100k.012740": {"vi": "gam (đơn vị khối lượng); hãng GM"},  # gm
    "lex.en.100k.012741": {"vi": "con ngỗng; véo mông trêu chọc"},  # goose
    "lex.en.100k.012745": {"vi": "phòng tập thể dục; nhà thể thao"},  # gymnasium
    "lex.en.100k.012749": {"vi": "trùm phát xít Adolf Hitler"},  # hitler
    "lex.en.100k.012750": {"vi": "mối liên kết; cuộc tình một đêm"},  # hookup
    "lex.en.100k.012751": {"pos": "verb", "vi": "tiếng hú dài; hú hét vang"},  # howl
    "lex.en.100k.012752": {"vi": "thuộc trường phái ấn tượng"},  # impressionist
    "lex.en.100k.012755": {"vi": "thiết yếu toàn vẹn; tích phân"},  # integral
    "lex.en.100k.012757": {"vi": "nguyên tố hóa học i-ốt"},  # iodine
    "lex.en.100k.012760": {"vi": "ki-lô-mét (km)"},  # kilometer
    "lex.en.100k.012764": {"vi": "vị trí gen; quỹ tích toán học"},  # locus
    "lex.en.100k.012766": {"vi": "tiểu bang Maine (Mỹ)"},  # maine
    "lex.en.100k.012768": {"vi": "trò chơi bắn bi; sự tỉnh táo"},  # marbles
    "lex.en.100k.012769": {"vi": "rạp che lớn; bảng hiệu nhà hát"},  # marquee
    "lex.en.100k.012770": {"vi": "bệnh viêm màng não nguy hiểm"},  # meningitis
    "lex.en.100k.012773": {"ipa": "/ˌɛm ˈpiːz/", "vi": "các nghị sĩ; các cảnh sát quân sự"},  # mps
    "lex.en.100k.012774": {"pos": "verb", "vi": "cằn nhằn lải nhải; ngựa già yếu"},  # nag
    "lex.en.100k.012775": {"vi": "thị trường ngách; hốc tường"},  # niche
    "lex.en.100k.012778": {"vi": "ngóc ngách; góc nhỏ kín đáo"},  # nook (purged single-word 'xó')
    "lex.en.100k.012780": {"pos": "verb", "vi": "thở hổn hển; tiếng thở dốc"},  # pant
    "lex.en.100k.012782": {"vi": "được vá lại; chắp vá loang lổ"},  # patched
    "lex.en.100k.012783": {"vi": "bán đảo địa lý"},  # peninsula
    "lex.en.100k.012784": {"vi": "biến thái trụy lạc; đồi bại"},  # perverted
    "lex.en.100k.012785": {"vi": "đã bị nhổ lông; được gảy đàn"},  # plucked
    "lex.en.100k.012787": {"vi": "đội vũ trang tự quản; nhóm bạn"},  # posse
    "lex.en.100k.012789": {"pos": "verb", "vi": "vị ngữ; đặt cơ sở nền tảng trên"},  # predicate
    "lex.en.100k.012790": {"vi": "mặt bằng cơ sở; tiền đề lý lẽ"},  # premises
    "lex.en.100k.012792": {"vi": "nhà tiên tri; đấng tiên tri"},  # prophet
    "lex.en.100k.012794": {"vi": "ngành chụp ảnh X quang y tế"},  # radiology
    "lex.en.100k.012797": {"pos": "verb", "vi": "chiếm lại; tái chiếm đoạt"},  # recapture
    "lex.en.100k.012799": {"vi": "sự thuyên giảm bệnh; miễn giảm nợ"},  # remission
    "lex.en.100k.012800": {"vi": "từ bỏ quyền lợi; tuyên bố khước từ"},  # renounce

    # 2701-2750
    "lex.en.100k.012801": {"vi": "sự ăn năn hối hận; sự hối lỗi"},  # repentance (purged single-word 'ăn năn')
    "lex.en.100k.012802": {"vi": "sự phục hồi; trùng tu; phục chế"},  # restoration
    "lex.en.100k.012806": {"vi": "tên họ Roberts"},  # roberts
    "lex.en.100k.012809": {"vi": "bí tích tôn giáo; thánh lễ"},  # sacrament
    "lex.en.100k.012810": {"vi": "nhân viên bán hàng; người bán"},  # salesperson
    "lex.en.100k.012812": {"vi": "tai ương thảm họa; trừng phạt"},  # scourge
    "lex.en.100k.012816": {"vi": "được may khâu cẩn thận"},  # sewn
    "lex.en.100k.012818": {"vi": "cây bụi nhỏ; lùm cây bụi"},  # shrub
    "lex.en.100k.012819": {"vi": "hệ thống biển báo; bảng hiệu"},  # signage
    "lex.en.100k.012822": {"vi": "lời lăng mạ miệt thị; nói nhịu"},  # slur
    "lex.en.100k.012824": {"vi": "vô cùng; hết sức đau đớn"},  # sorely
    "lex.en.100k.012827": {"vi": "yêu tinh tí hon; tiên nữ nhỏ"},  # sprite
    "lex.en.100k.012828": {"vi": "muối sunfat; gốc sunfat"},  # sulfate
    "lex.en.100k.012829": {"pos": "verb", "vi": "đổi chác; hoán đổi vị trí"},  # swap
    "lex.en.100k.012832": {"vi": "dính nhớp; rẻ tiền lòe loẹt"},  # tacky
    "lex.en.100k.012833": {"vi": "hàm tang; đường tiếp tuyến"},  # tangent
    "lex.en.100k.012835": {"vi": "bản di chúc; minh chứng cho"},  # testament
    "lex.en.100k.012836": {"vi": "ngành điều trị học; liệu pháp"},  # therapeutics
    "lex.en.100k.012838": {"pos": "verb", "vi": "chào mời; tâng bốc; phe vé"},  # tout
    "lex.en.100k.012839": {"vi": "đạn vạch đường; chất đánh dấu"},  # tracer
    "lex.en.100k.012840": {"vi": "xe chở ô tô; tàu chuyên chở"},  # transporter
    "lex.en.100k.012844": {"vi": "vô tình; không cố ý; sơ ý"},  # unintentionally
    "lex.en.100k.012849": {"vi": "bản phán quyết của tòa án"},  # verdict
    "lex.en.100k.012850": {"vi": "nghề nghiệp; thiên hướng nghề"},  # vocation
    "lex.en.100k.012853": {"vi": "cơ quan giám sát; chó giữ nhà"},  # watchdog
    "lex.en.100k.012855": {"vi": "con chồn; kẻ trơn tráo giảo hoạt"},  # weasel
    "lex.en.100k.012857": {"vi": "tán tỉnh cưa cẩm; thuyết phục"},  # woo
    "lex.en.100k.012859": {"vi": "nước Bỉ (Belgium)"},  # belgium
    "lex.en.100k.012860": {"pos": "noun", "vi": "phân khối (cc); gửi kèm bản sao"},  # cc
    "lex.en.100k.012861": {"vi": "màu sắc; cờ hiệu quân đội"},  # colours
    "lex.en.100k.012862": {"vi": "tên riêng/họ Harvey"},  # harvey
    "lex.en.100k.012863": {"vi": "tên riêng/họ Morris"},  # morris
    "lex.en.100k.012864": {"vi": "nước Na Uy"},  # norway
    "lex.en.100k.012865": {"vi": "tên riêng Rachel"},  # rachel
    "lex.en.100k.012866": {"pos": "num", "vi": "mười lăm (15)"},  # fifteen (pos fixed)
    "lex.en.100k.012867": {"vi": "tiểu bang Georgia (Mỹ viết tắt)"},  # ga
    "lex.en.100k.012868": {"vi": "người Norman; vùng Normandy"},  # norman
    "lex.en.100k.012870": {"vi": "các chuyến tham quan; phố Tours"},  # tours
    "lex.en.100k.012871": {"vi": "bằng cử nhân (Bachelor of Arts)"},  # ba
    "lex.en.100k.012872": {"vi": "nước Cu-ba (Cuba)"},  # cuba
    "lex.en.100k.012874": {"vi": "mã lực (HP); hãng máy tính HP"},  # hp
    "lex.en.100k.012876": {"vi": "ngọn núi (Mount); bang Montana"},  # mt
    "lex.en.100k.012878": {"vi": "tổng thống Nga Vladimir Putin"},  # putin
    "lex.en.100k.012879": {"vi": "tên dòng họ Stuart"},  # stuart
    "lex.en.100k.012884": {"vi": "chứng thiếu máu (bệnh lý)"},  # anemia
    "lex.en.100k.012886": {"vi": "thích hợp; có khuynh hướng dễ"},  # apt
    "lex.en.100k.012889": {"vi": "tự miễn dịch (y học)"},  # autoimmune
    "lex.en.100k.012891": {"vi": "đá dằn đường ray; balát tàu thủy"},  # ballast
    "lex.en.100k.012892": {"vi": "người ăn xin; kẻ ăn mày"},  # beggar
    "lex.en.100k.012893": {"vi": "thủ đô Bắc Kinh (Trung Quốc)"},  # beijing
    "lex.en.100k.012896": {"vi": "bộ đệm dữ liệu; vùng đệm"},  # buffer
    "lex.en.100k.012897": {"pos": "noun", "vi": "đường tránh; phẫu thuật bắc cầu"},  # bypass
    "lex.en.100k.012899": {"vi": "tụ điện (linh kiện điện tử)"},  # capacitor
    "lex.en.100k.012900": {"vi": "vùng biển Caribe; người Caribe"},  # caribbean

    # 2751-2800
    "lex.en.100k.012901": {"vi": "thợ mộc gia dụng; thợ đóng gỗ"},  # carpenter
    "lex.en.100k.012902": {"vi": "thực đơn nhà hàng (à la carte)"},  # carte
    "lex.en.100k.012904": {"vi": "theo phái trung lập; trung dung"},  # centrist
    "lex.en.100k.012906": {"vi": "sự lưu thông máu; số bản phát hành"},  # circulation
    "lex.en.100k.012907": {"vi": "chu vi đường tròn; đường chu vi"},  # circumference
    "lex.en.100k.012908": {"vi": "trích dẫn khoa học; trát hầu tòa"},  # citation
    "lex.en.100k.012910": {"vi": "giáo sĩ; mục sư tôn giáo"},  # clergyman
    "lex.en.100k.012911": {"vi": "lối nói sáo rỗng; rập khuôn cũ"},  # cliche
    "lex.en.100k.012913": {"vi": "đấu trường La Mã; nhà thi đấu lớn"},  # coliseum
    "lex.en.100k.012916": {"vi": "sự tham vấn; buổi hội chẩn"},  # consultation
    "lex.en.100k.012919": {"vi": "ủy viên hội đồng thành phố"},  # councilman
    "lex.en.100k.012920": {"vi": "quả nam việt quất"},  # cranberry
    "lex.en.100k.012923": {"vi": "nông trại nhỏ thuê canh tác"},  # croft
    "lex.en.100k.012925": {"vi": "sốt sữa trứng kem custard"},  # custard
    "lex.en.100k.012928": {"vi": "hoang tàn tiêu điều; cô quạnh"},  # desolate
    "lex.en.100k.012930": {"vi": "máy xúc đất; công nhân đào mỏ"},  # digger
    "lex.en.100k.012932": {"vi": "bài diễn thuyết; luận bàn học thuật"},  # discourse
    "lex.en.100k.012936": {"vi": "bánh rán vòng ngọt (donut)"},  # doughnut
    "lex.en.100k.012938": {"vi": "độ cao so với biển; sự nâng cao"},  # elevation
    "lex.en.100k.012939": {"pos": "num", "vi": "mười một (11)"},  # eleven (pos fixed)
    "lex.en.100k.012942": {"vi": "bí truyền; thâm sâu khó hiểu"},  # esoteric
    "lex.en.100k.012944": {"pos": "noun", "vi": "ngoại thất; phần bên ngoài"},  # exterior
    "lex.en.100k.012945": {"vi": "truyện ngụ ngôn"},  # fable
    "lex.en.100k.012946": {"vi": "bè phái trong đảng; phe nhóm"},  # faction
    "lex.en.100k.012947": {"vi": "tội phạm hình sự; phạm trọng tội"},  # felon
    "lex.en.100k.012949": {"vi": "dễ bốc cháy; dễ bắt lửa"},  # flammable
    "lex.en.100k.012950": {"vi": "phân số (toán); tỷ lệ phần nhỏ"},  # fraction
    "lex.en.100k.012952": {"vi": "ngọc hồng lựu (đá garnet)"},  # garnet
    "lex.en.100k.012953": {"vi": "thuộc địa nhiệt (nhiệt đất)"},  # geothermal
    "lex.en.100k.012954": {"pos": "noun", "vi": "vỉ nướng; song sắt; nạo mài"},  # grate
    "lex.en.100k.012958": {"vi": "ngành trồng trọt làm vườn"},  # horticulture
    "lex.en.100k.012960": {"vi": "sự cấp nước; sự ngậm nước"},  # hydration
    "lex.en.100k.012962": {"vi": "sự thoát tội; không bị trừng phạt"},  # impunity
    "lex.en.100k.012964": {"vi": "việc đánh chỉ mục tra cứu"},  # indexing
    "lex.en.100k.012965": {"vi": "quán tính vật lý; sức ì trệ"},  # inertia
    "lex.en.100k.012966": {"vi": "chứng vô sinh; hiếm muộn"},  # infertility
    "lex.en.100k.012967": {"vi": "vốn có sẵn; cố hữu bên trong"},  # inherent
    "lex.en.100k.012970": {"vi": "sự trớ trêu; sự châm biếm mỉa mai"},  # irony (purged crawler mistranslation 'thép/gang')
    "lex.en.100k.012974": {"vi": "con đỉa hút máu; kẻ bòn rút"},  # leech
    "lex.en.100k.012975": {"vi": "vòng hoa đội đầu Hawaii"},  # lei
    "lex.en.100k.012976": {"vi": "khả năng xảy ra; xác suất"},  # likelihood
    "lex.en.100k.012977": {"vi": "dục vọng; lòng ham muốn khoái lạc"},  # lust
    "lex.en.100k.012979": {"vi": "tạm thời; dùng tạm thay thế"},  # makeshift
    "lex.en.100k.012980": {"vi": "thủ dâm; tự kích thích tình dục"},  # masturbate (sanitized)
    "lex.en.100k.012982": {"vi": "về mặt toán học; theo toán học"},  # mathematically
    "lex.en.100k.012983": {"vi": "ung thư hắc tố da (melanoma)"},  # melanoma
    "lex.en.100k.012985": {"vi": "ngây thơ khờ dại; chất phác"},  # naive
    "lex.en.100k.012986": {"vi": "sự giáng sinh; sự ra đời"},  # nativity
    "lex.en.100k.012987": {"vi": "khéo léo; tiện lợi tuyệt vời"},  # nifty
    "lex.en.100k.012988": {"vi": "mờ nhạt; ít ai biết; tối nghĩa"},  # obscure
    "lex.en.100k.012989": {"vi": "bị mồ côi cha mẹ"},  # orphaned
    "lex.en.100k.012990": {"vi": "chế độ tăng tốc; chạy quá tải"},  # overdrive
    "lex.en.100k.012991": {"vi": "lớp bông độn đệm; chèn đệm"},  # padding
    "lex.en.100k.012992": {"vi": "kim loại quý palađi (Pd)"},  # palladium
    "lex.en.100k.012994": {"vi": "mầm bệnh; vi sinh vật gây bệnh"},  # pathogen
    "lex.en.100k.012995": {"pos": "noun", "vi": "trại giam liên bang; nhà tù"},  # penitentiary
    "lex.en.100k.012997": {"vi": "dàn nhạc giao hưởng; yêu âm nhạc"},  # philharmonic
    "lex.en.100k.012998": {"vi": "quảng trường công cộng Ý"},  # piazza
    "lex.en.100k.013000": {"vi": "người tiên phong; khai phá mở đường"},  # pioneer (purged crawler 'namviet')
}

# Verify lengths <= 35
for k, v in OVERRIDES_B03_R06.items():
    if "vi" in v:
        assert len(v["vi"]) <= 35, f"Length > 35 for {k}: {v['vi']} ({len(v['vi'])})"

with open('content/english/qa-batches/batch-03.json', 'r', encoding='utf-8') as f:
    batch_data = json.load(f)

# Apply overrides to records in range 2500 to 3000
count = 0
for idx in range(2500, 3000):
    rec = batch_data['records'][idx]
    rid = rec['id']
    if rid in OVERRIDES_B03_R06:
        count += 1
        for field, val in OVERRIDES_B03_R06[rid].items():
            rec[field] = val
        rec['status'] = 'reviewed'

batch_data['reviewedCount'] = 3000

with open('content/english/qa-batches/batch-03.json', 'w', encoding='utf-8') as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully applied Batch 03 Round 6 ({count} overrides). Reviewed: {batch_data['reviewedCount']}/5000.")
