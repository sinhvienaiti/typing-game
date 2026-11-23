import json

# Cognitive manual QA overrides for Batch 03 Round 10 (records 4500 to 5000, STT 4501 to 5000)
OVERRIDES_B03_R10 = {
    # 4501 - 4600
    "lex.en.100k.014501": {"vi": "bụi bẩn cáu ghét; vết nhơ bẩn"},  # grime
    "lex.en.100k.014502": {"vi": "con chim diệc; cò diệc mò cá"},  # heron (purged single-word 'diệc')
    "lex.en.100k.014504": {"vi": "nạn cướp máy bay; không tặc"},  # hijacking
    "lex.en.100k.014506": {"vi": "phi logic; vô lý; thiếu hợp lý"},  # illogical
    "lex.en.100k.014508": {"vi": "cản trở; gây trở ngại; ngăn bước"},  # impede
    "lex.en.100k.014510": {"vi": "cá tính riêng biệt; tính độc đáo"},  # individuality
    "lex.en.100k.014513": {"vi": "quân đội IRA; tài khoản hưu IRA"},  # ira
    "lex.en.100k.014515": {"vi": "lịch trình chuyến đi; lộ trình"},  # itinerary
    "lex.en.100k.014516": {"vi": "gây nguy hại; đe dọa liều lĩnh"},  # jeopardize
    "lex.en.100k.014517": {"vi": "họa sĩ Jasper Johns; họ Johns"},  # johns
    "lex.en.100k.014518": {"vi": "nhang hương trầm; tượng thần linh"},  # joss
    "lex.en.100k.014519": {"vi": "thủy quái Leviathan; vật khổng lồ"},  # leviathan
    "lex.en.100k.014520": {"vi": "cô đơn buồn bã; hẻo lánh vắng vẻ"},  # lonesome
    "lex.en.100k.014521": {"vi": "thành phố Louisville (Kentucky)"},  # louisville
    "lex.en.100k.014522": {"vi": "quai xách; mấu lồi; kéo lê nặng"},  # lug
    "lex.en.100k.014523": {"vi": "nước hơi ấm; thờ ơ nguội lạnh"},  # lukewarm
    "lex.en.100k.014524": {"vi": "quang thông lumen; lòng ống mạch"},  # lumen
    "lex.en.100k.014525": {"vi": "thuộc Malaysia; người Malaysia"},  # malaysian
    "lex.en.100k.014526": {"vi": "hoa cúc hoàng kim marguerite"},  # marguerite
    "lex.en.100k.014527": {"vi": "mức tăng giá bán lẻ; tiền lãi tăng"},  # markup
    "lex.en.100k.014528": {"vi": "bị làm hỏng; bị sứt mẻ thanh danh"},  # marred
    "lex.en.100k.014529": {"vi": "tên riêng Melissa; chi tía tô đất"},  # melissa
    "lex.en.100k.014530": {"vi": "mang tính ẩn dụ; nghĩa bóng ẩn dụ"},  # metaphorical
    "lex.en.100k.014531": {"vi": "đại thi hào thi sĩ John Milton"},  # milton
    "lex.en.100k.014532": {"ipa": "/ˌɛm ˈɛl/", "vi": "mi-li-lít (ml); đơn vị thể tích"},  # ml
    "lex.en.100k.014533": {"vi": "phô mai sợi mềm Mozzarella Ý"},  # mozzarella
    "lex.en.100k.014534": {"vi": "đa phương; nhiều bên tham gia"},  # multilateral
    "lex.en.100k.014535": {"vi": "người trùng tên; vật cùng tên"},  # namesake
    "lex.en.100k.014536": {"vi": "nhà thơ Ogden Nash; họ Nash"},  # nash
    "lex.en.100k.014537": {"vi": "trứng chấy; lỗi vặt chi li"},  # nit
    "lex.en.100k.014538": {"vi": "Alfred Nobel; giải thưởng Nobel"},  # nobel
    "lex.en.100k.014539": {"vi": "thành phố Norfolk; hạt Norfolk"},  # norfolk
    "lex.en.100k.014540": {"vi": "mang tính chuẩn mực; quy phạm"},  # normative
    "lex.en.100k.014541": {"vi": "sắc thái tinh tế; sự khác biệt nhỏ"},  # nuance
    "lex.en.100k.014542": {"vi": "tính khách quan; tính công tâm"},  # objectivity
    "lex.en.100k.014543": {"vi": "gây tắc nghẽn; chắn ngang cản trở"},  # obstruct (purged single-word 'chắn')
    "lex.en.100k.014544": {"vi": "kẻ bị ruồng bỏ; bị xua đuổi"},  # outcast
    "lex.en.100k.014545": {"vi": "tình trạng quá nhiệt; nóng máy"},  # overheating
    "lex.en.100k.014546": {"vi": "làm dịu triệu chứng; giảm nhẹ đau"},  # palliative
    "lex.en.100k.014547": {"vi": "tấm kính cửa sổ; ô kính khung cửa"},  # pane
    "lex.en.100k.014548": {"vi": "có tầm nhìn toàn cảnh; bao quát"},  # panoramic
    "lex.en.100k.014549": {"vi": "đồ ghép vải; mớ chắp vá lộn xộn"},  # patchwork
    "lex.en.100k.014550": {"vi": "chứng ấu dâm; bệnh ấu dâm lệch lạc"},  # pedophilia
    "lex.en.100k.014551": {"vi": "duy trì lâu dài; kéo dài mãi mãi"},  # perpetuate (purged single-word 'nối')
    "lex.en.100k.014552": {"vi": "nhau thai (sản khoa y học)"},  # placenta
    "lex.en.100k.014553": {"vi": "mang tính tiên tri; báo trước"},  # prophetic
    "lex.en.100k.014554": {"vi": "bút danh nghệ danh; tên giả bí mật"},  # pseudonym
    "lex.en.100k.014555": {"vi": "nơi luyện ngục; nỗi khổ tạm thời"},  # purgatory
    "lex.en.100k.014557": {"vi": "mối quan hệ hòa hợp; sự gắn kết"},  # rapport
    "lex.en.100k.014558": {"vi": "tính hợp lý lý tính; sự sáng suốt"},  # rationality
    "lex.en.100k.014559": {"vi": "sự bác bỏ luận điểm; lời phản biện"},  # rebuttal
    "lex.en.100k.014561": {"vi": "được làm lạnh bảo quản; ướp đá"},  # refrigerated
    "lex.en.100k.014562": {"vi": "người giải tỏa; thuốc làm dịu đau"},  # reliever
    "lex.en.100k.014563": {"vi": "vang vọng cộng hưởng; tạo đồng cảm"},  # resonate
    "lex.en.100k.014564": {"vi": "khoảng nghỉ ngơi tạm thời; hoãn nợ"},  # respite
    "lex.en.100k.014566": {"vi": "sự đại bại thảm hại; đánh tan tác"},  # rout
    "lex.en.100k.014567": {"vi": "thô sơ sơ đẳng; cơ bản ban đầu"},  # rudimentary
    "lex.en.100k.014568": {"vi": "bộ mẫu dùng thử; máy lấy mẫu nhạc"},  # sampler
    "lex.en.100k.014569": {"vi": "vùng đất Savoy; bắp cải xoăn Savoy"},  # savoy
    "lex.en.100k.014570": {"vi": "giàn giáo xây dựng; khung nâng đỡ"},  # scaffolding (purged single-word 'giàn')
    "lex.en.100k.014572": {"vi": "thuộc về trầm tích (địa chất)"},  # sedimentary
    "lex.en.100k.014573": {"vi": "diễn viên hài kịch Peter Sellers"},  # sellers
    "lex.en.100k.014575": {"vi": "một cách kinh ngạc; gây sốc tột độ"},  # shockingly
    "lex.en.100k.014576": {"vi": "sự chậm lại; sự suy giảm nhịp độ"},  # slowdown
    "lex.en.100k.014577": {"vi": "ngày chí (hạ chí hoặc đông chí)"},  # solstice
    "lex.en.100k.014578": {"vi": "một cách thưa thớt; rải rác ít ỏi"},  # sparsely
    "lex.en.100k.014579": {"vi": "trục quay se sợi; con suốt dệt"},  # spindle
    "lex.en.100k.014580": {"vi": "mang phong cách thể thao; năng động"},  # sporty
    "lex.en.100k.014581": {"vi": "nhân viên cơ quan; thành viên ban"},  # staffer
    "lex.en.100k.014582": {"vi": "cương vị ngôi sao nổi tiếng"},  # stardom
    "lex.en.100k.014583": {"vi": "uy nghi đường bệ; tráng lệ nguy nga"},  # stately
    "lex.en.100k.014584": {"vi": "bốc hơi mịt mù; nóng bỏng gợi cảm"},  # steamy
    "lex.en.100k.014585": {"vi": "nút chai đậy kín; vật chặn nút đậy"},  # stopper
    "lex.en.100k.014586": {"vi": "về mặt cấu trúc; theo kết cấu"},  # structurally
    "lex.en.100k.014589": {"vi": "siêu mẫu thời trang quốc tế"},  # supermodel
    "lex.en.100k.014592": {"vi": "bệnh giang mai (y khoa)"},  # syphilis
    "lex.en.100k.014593": {"vi": "mặt trên của bàn; trò chơi cờ bàn"},  # tabletop
    "lex.en.100k.014594": {"vi": "cơn ăn vạ hờn dỗi; cơn cáu gắt"},  # tantrum
    "lex.en.100k.014595": {"vi": "bộ điều nhiệt nhiệt độ tự động"},  # thermostat
    "lex.en.100k.014596": {"vi": "xếp theo bậc thang; phân nhiều cấp"},  # tiered
    "lex.en.100k.014600": {"vi": "vật tổ tô-tem; biểu tượng tâm linh"},  # totem

    # 4601 - 4700
    "lex.en.100k.014602": {"vi": "thanh bình yên tĩnh; tĩnh lặng"},  # tranquil
    "lex.en.100k.014603": {"vi": "thuộc bờ bên kia Đại Tây Dương"},  # transatlantic
    "lex.en.100k.014604": {"vi": "vượt qua mọi giới hạn; vượt trội"},  # transcend
    "lex.en.100k.014606": {"vi": "bán phá giá cạnh tranh; thịt thăn"},  # undercut
    "lex.en.100k.014607": {"vi": "không có giấy phép; hoạt động chui"},  # unlicensed
    "lex.en.100k.014609": {"vi": "thư giãn thả lỏng; cuộn tháo ra"},  # unwind
    "lex.en.100k.014610": {"vi": "biến động chấn động; xáo trộn lớn"},  # upheaval
    "lex.en.100k.014611": {"vi": "tiểu bang Vermont (Hoa Kỳ)"},  # vermont
    "lex.en.100k.014612": {"pos": "num", "ipa": "/ˌviː aɪ ˈaɪ/", "vi": "số 7 (số La Mã VII); thứ bảy"},  # vii
    "lex.en.100k.014613": {"vi": "nghệ sĩ kéo đàn vĩ cầm (violin)"},  # violinist
    "lex.en.100k.014614": {"vi": "lãnh chúa quân phiệt thống trị"},  # warlord
    "lex.en.100k.014615": {"vi": "cảnh giác đề phòng; canh chừng"},  # watchful
    "lex.en.100k.014617": {"vi": "đau nhói lòng; đau đớn xé ruột"},  # wrenching
    "lex.en.100k.014618": {"vi": "cái ách kìm kẹp; ách áp bức nô dịch"},  # yoke (purged single-word 'ách')
    "lex.en.100k.014619": {"vi": "quốc vương Khalip; bang California"},  # calif
    "lex.en.100k.014620": {"ipa": "/ˌsiː ˈiː/", "vi": "sau Công nguyên (viết tắt CE)"},  # ce
    "lex.en.100k.014621": {"vi": "thủ tướng Anh Winston Churchill"},  # churchill
    "lex.en.100k.014622": {"vi": "Đại đế Cyrus (Ba Tư cổ đại)"},  # cyrus
    "lex.en.100k.014623": {"vi": "Mahatma Gandhi; Indira Gandhi"},  # gandhi
    "lex.en.100k.014624": {"ipa": "/ˌdʒiː ˈiː/", "vi": "nguyên tố gecmani (Ge); tập đoàn GE"},  # ge
    "lex.en.100k.014625": {"vi": "khiếu hài hước; sự dí dỏm vui vẻ"},  # humour
    "lex.en.100k.014626": {"vi": "linh hồn Ka (Ai Cập cổ đại)"},  # ka
    "lex.en.100k.014627": {"vi": "đồ chơi lắp ráp xếp hình Lego"},  # lego
    "lex.en.100k.014628": {"vi": "quốc gia Nepal (dãy Himalaya)"},  # nepal
    "lex.en.100k.014629": {"vi": "tài tử điện ảnh Paul Newman"},  # newman
    "lex.en.100k.014630": {"vi": "thuộc về Ba Tư; tiếng Ba Tư"},  # persian
    "lex.en.100k.014631": {"vi": "thuộc nước Bỉ; người vương quốc Bỉ"},  # belgian
    "lex.en.100k.014632": {"vi": "nhà cải cách tôn giáo John Calvin"},  # calvin
    "lex.en.100k.014633": {"vi": "tên riêng Dana; họ Dana"},  # dana
    "lex.en.100k.014634": {"vi": "vườn địa đàng Eden; chốn bồng lai"},  # eden
    "lex.en.100k.014635": {"vi": "tiếng Hindi (Ấn Độ); người Ấn"},  # hindi
    "lex.en.100k.014636": {"ipa": "/ˌeɪtʃ ˈɛm/", "vi": "héc-tô-mét (hm); tiếng hắng giọng"},  # hm
    "lex.en.100k.014637": {"vi": "thành phố Indianapolis (Indiana)"},  # indianapolis
    "lex.en.100k.014638": {"vi": "quốc gia Libya (Bắc Phi)"},  # libya
    "lex.en.100k.014639": {"ipa": "/ˌɛn ˈɛm/", "vi": "nanomet (nm); một phần tỷ mét"},  # nm
    "lex.en.100k.014640": {"vi": "tên người Tracy; Spencer Tracy"},  # tracy
    "lex.en.100k.014641": {"vi": "thành phố cảng Aberdeen (Scotland)"},  # aberdeen
    "lex.en.100k.014642": {"vi": "thủ phủ Albany (bang New York)"},  # albany
    "lex.en.100k.014644": {"vi": "nhà triết học Giordano Bruno"},  # bruno
    "lex.en.100k.014645": {"vi": "thuộc về Bulgaria; tiếng Bulgaria"},  # bulgarian
    "lex.en.100k.014646": {"vi": "thành phố cổ Chester (nước Anh)"},  # chester
    "lex.en.100k.014647": {"ipa": "/ˌiː ˈeɪ/", "vi": "thần Ea (Lưỡng Hà); hãng game EA"},  # ea
    "lex.en.100k.014648": {"pos": "num", "vi": "số 18; mười tám"},  # eighteen
    "lex.en.100k.014649": {"vi": "tên riêng Lindsay; Lindsay Lohan"},  # lindsay
    "lex.en.100k.014650": {"vi": "đất nước Myanmar; nước Miến Điện"},  # myanmar
    "lex.en.100k.014651": {"ipa": "/ˌɛn ɛs ˈdʌbəl.juː/", "vi": "bang New South Wales (Úc)"},  # nsw
    "lex.en.100k.014652": {"vi": "thành phố Rochester (New York)"},  # rochester
    "lex.en.100k.014654": {"vi": "biên đạo Ted Shawn; ca sĩ Shawn"},  # shawn
    "lex.en.100k.014655": {"vi": "vị vua khôn ngoan Solomon (Do Thái)"},  # solomon
    "lex.en.100k.014656": {"vi": "sao Kim (Kim tinh); nữ thần Vệ Nữ"},  # venus
    "lex.en.100k.014657": {"vi": "tiếng Ngô (phương ngôn Trung Hoa)"},  # wu
    "lex.en.100k.014658": {"vi": "kiêng khem; bỏ phiếu trắng"},  # abstain
    "lex.en.100k.014659": {"vi": "âm học môi trường; đặc tính âm vang"},  # acoustics
    "lex.en.100k.014660": {"vi": "Liên đoàn Bóng bầu dục Úc (AFL)"},  # afl
    "lex.en.100k.014661": {"vi": "luồng không khí lưu thông; dòng khí"},  # airflow
    "lex.en.100k.014663": {"vi": "con linh dương thảo nguyên hoang dã"},  # antelope
    "lex.en.100k.014664": {"vi": "nhà nghiên cứu nhân chủng học"},  # anthropologist
    "lex.en.100k.014665": {"vi": "thuộc về động mạch chủ quả tim"},  # aortic
    "lex.en.100k.014666": {"vi": "sự âu lo e ngại sợ hãi; sự bắt giữ"},  # apprehension
    "lex.en.100k.014667": {"vi": "tổng giáo phận Công giáo La Mã"},  # archdiocese
    "lex.en.100k.014668": {"vi": "thuộc về nước Áo; người nước Áo"},  # austrian
    "lex.en.100k.014670": {"vi": "ống bễ thổi lửa lò rèn kim loại"},  # bellows (purged single-word 'bễ')
    "lex.en.100k.014671": {"vi": "thợ nổ mìn phá đá; súng bắn tia"},  # blaster
    "lex.en.100k.014673": {"vi": "một cách thẳng thừng; không vòng vo"},  # bluntly
    "lex.en.100k.014674": {"vi": "đỏ mặt e thẹn; ngượng ngùng đỏ má"},  # blushing
    "lex.en.100k.014675": {"vi": "được tết bím tóc; bện xoắn dây"},  # braided
    "lex.en.100k.014676": {"vi": "nữ phù dâu trong đám cưới"},  # bridesmaid
    "lex.en.100k.014677": {"vi": "nước muối ngâm dưa; nước biển mặn"},  # brine
    "lex.en.100k.014678": {"vi": "có vòng một đẫy đà; ngực nở nang"},  # busty
    "lex.en.100k.014679": {"vi": "hoàng đế Julius Caesar La Mã"},  # caesar
    "lex.en.100k.014680": {"vi": "tác giả Lewis Carroll; họ Carroll"},  # carroll
    "lex.en.100k.014681": {"vi": "hang động ngầm lớn trong lòng đất"},  # cavern
    "lex.en.100k.014683": {"vi": "người soát vé; quân cờ đam kẻ ô"},  # checker
    "lex.en.100k.014684": {"vi": "tinh thần nghĩa hiệp trượng nghĩa"},  # chivalry
    "lex.en.100k.014685": {"vi": "thùng đánh bơ; khuấy đảo dữ dội"},  # churn
    "lex.en.100k.014686": {"vi": "cộng tác viên dự án; người hợp tác"},  # collaborator
    "lex.en.100k.014687": {"vi": "sự ép buộc cưỡng bách; sự thôi thúc"},  # compulsion
    "lex.en.100k.014688": {"vi": "làm phép hiện ra; gợi lại ký ức"},  # conjure
    "lex.en.100k.014689": {"vi": "thuộc về ngữ cảnh; theo bối cảnh"},  # contextual
    "lex.en.100k.014690": {"vi": "con gấu mèo hoang dã; người lập dị"},  # coon
    "lex.en.100k.014691": {"vi": "hậu vệ góc phòng ngự biên"},  # cornerback
    "lex.en.100k.014692": {"vi": "lòng tin; sự tín nhiệm công nhận"},  # credence
    "lex.en.100k.014693": {"vi": "làn đạn hỏa lực chéo cánh; đôi co"},  # crossfire
    "lex.en.100k.014695": {"vi": "thái độ hoài nghi cay độc; yếm thế"},  # cynicism
    "lex.en.100k.014696": {"vi": "có nang dạng túi; thuộc bàng quang"},  # cystic (purged single-word 'nang')
    "lex.en.100k.014697": {"vi": "chủ nghĩa Dada; tiếng gọi bố"},  # dada
    "lex.en.100k.014698": {"vi": "nhỏ nhắn thanh tú; trang nhã"},  # dainty
    "lex.en.100k.014699": {"vi": "bên vay nợ; người mang công nợ"},  # debtor
    "lex.en.100k.014700": {"vi": "trật đường ray tàu; chệch hướng"},  # derail

    # 4701 - 4800
    "lex.en.100k.014701": {"vi": "nhân viên điều phối xe/chuyến bay"},  # dispatcher
    "lex.en.100k.014703": {"vi": "bốc thuốc cấp phát; phân phối đồ"},  # dispense
    "lex.en.100k.014704": {"vi": "bị bỏ qua xem nhẹ; bị ngó lơ"},  # disregarded
    "lex.en.100k.014705": {"vi": "sự hòa tan hóa chất; biến mất dần"},  # dissolving
    "lex.en.100k.014707": {"vi": "giải khuây vui tính; làm đổi hướng"},  # diverting
    "lex.en.100k.014708": {"vi": "luồng gió lùa se lạnh; vại bia tươi"},  # draught
    "lex.en.100k.014710": {"vi": "bệnh chàm da mãn tính (eczema)"},  # eczema
    "lex.en.100k.014712": {"vi": "việc trút hết ra; làm trống rỗng"},  # emptying
    "lex.en.100k.014714": {"vi": "một cách sai sót; do lầm tưởng"},  # erroneously
    "lex.en.100k.014716": {"vi": "thành phố Eugene (tiểu bang Oregon)"},  # eugene
    "lex.en.100k.014717": {"vi": "tiếng kêu thốt lên; câu cảm thán"},  # exclamation
    "lex.en.100k.014718": {"vi": "người đao phủ thi hành án tử hình"},  # executioner
    "lex.en.100k.014720": {"vi": "tuyến đường cao tốc giao thông"},  # expressway
    "lex.en.100k.014721": {"vi": "vòi nước bồn rửa; van khóa vòi nước"},  # faucet
    "lex.en.100k.014722": {"vi": "gan góc gan lì; hiếu chiến đanh đá"},  # feisty
    "lex.en.100k.014723": {"vi": "có hình ngón tay; phân nhánh ngón"},  # fingered
    "lex.en.100k.014724": {"vi": "kẻ chỉ điểm phản bội; tên tay sai"},  # fink
    "lex.en.100k.014725": {"vi": "nhà soạn kịch John Fletcher"},  # fletcher
    "lex.en.100k.014727": {"vi": "được nêu ở phần trên; vừa kể trước"},  # foregoing
    "lex.en.100k.014728": {"vi": "bị làm vấy bẩn; bị phạm lỗi cản trở"},  # fouled
    "lex.en.100k.014729": {"vi": "đầu hồi mái nhà; tường tam giác mái"},  # gable
    "lex.en.100k.014730": {"vi": "giàn giá treo cổ tử tù"},  # gallows
    "lex.en.100k.014731": {"vi": "đảo Guernsey; giống bò Guernsey"},  # guernsey
    "lex.en.100k.014732": {"vi": "thể thơ Haiku truyền thống Nhật Bản"},  # haiku
    "lex.en.100k.014734": {"vi": "kể từ giờ trở đi; từ nay về sau"},  # henceforth
    "lex.en.100k.014735": {"vi": "đỉnh đồi dốc thoai thoải"},  # hilltop
    "lex.en.100k.014736": {"vi": "kẻ lang thang; người phiêu bạt"},  # hobo
    "lex.en.100k.014738": {"vi": "lời chào hỏi thân ái kiểu cao bồi"},  # howdy
    "lex.en.100k.014739": {"vi": "thuyền buồm nhỏ ven biển đáy bằng"},  # hoy
    "lex.en.100k.014740": {"vi": "linh cảm mách bảo; dáng lưng khom"},  # hunch
    "lex.en.100k.014741": {"ipa": "/ˌaɪ ˈiː/", "vi": "tức là; cụ thể là (id est - i.e.)"},  # ie
    "lex.en.100k.014743": {"vi": "bị tước khả năng; mất năng lực"},  # incapacitated
    "lex.en.100k.014744": {"vi": "vết rạch phẫu thuật mổ; đường rạch"},  # incision
    "lex.en.100k.014746": {"vi": "không thể giải thích nổi; bí hiểm"},  # inexplicable
    "lex.en.100k.014747": {"vi": "ăn sâu bám rễ; thâm căn cố đế"},  # ingrained
    "lex.en.100k.014748": {"vi": "đổi mới tư duy; cải tiến sáng tạo"},  # innovate
    "lex.en.100k.014750": {"vi": "điệu nhảy jive; nói chuyện phét lác"},  # jive
    "lex.en.100k.014752": {"vi": "thùng bom bia kim loại (keg 50 lít)"},  # keg
    "lex.en.100k.014753": {"vi": "cô gái trẻ thiếu nữ; nàng thôn nữ"},  # lass
    "lex.en.100k.014754": {"vi": "vết thương tổn nội tạng mô (y học)"},  # lesion
    "lex.en.100k.014755": {"vi": "nữ kiến trúc sư Maya Lin; họ Lâm"},  # lin
    "lex.en.100k.014756": {"vi": "khoảng lặng tạm thời; ru ngủ êm dịu"},  # lull
    "lex.en.100k.014757": {"vi": "bài hát ru con êm đềm ngủ ngon"},  # lullaby
    "lex.en.100k.014758": {"vi": "thuộc vùng thắt lưng; đốt sống lưng"},  # lumbar
    "lex.en.100k.014759": {"vi": "thành phố cổ Lyon (nước Pháp)"},  # lyon
    "lex.en.100k.014760": {"vi": "con cá thu biển tươi sống"},  # mackerel
    "lex.en.100k.014761": {"vi": "bơ thực vật margarin nhân tạo"},  # marge
    "lex.en.100k.014762": {"vi": "ngành triết học siêu hình học"},  # metaphysics
    "lex.en.100k.014763": {"vi": "vùng Trung Tây nước Mỹ (Midwest)"},  # midwest
    "lex.en.100k.014764": {"vi": "sự quản lý yếu kém; sự quản lý sai"},  # mismanagement
    "lex.en.100k.014765": {"vi": "con mạt bụi nhà; con ve bét nhỏ"},  # mite
    "lex.en.100k.014766": {"vi": "nhà xác bệnh viện; nơi lưu thi hài"},  # morgue
    "lex.en.100k.014767": {"vi": "tạp nhạp lộn xộn; sặc sỡ đa sắc"},  # motley
    "lex.en.100k.014768": {"vi": "món hầm thịt rau; lượt đánh lại gôn"},  # mulligan
    "lex.en.100k.014769": {"vi": "nhai ngấu nghiến tóp tép; gặm nhấm"},  # munch
    "lex.en.100k.014770": {"vi": "có cấu trúc mắt lưới; dạng mắt cáo"},  # netted
    "lex.en.100k.014771": {"vi": "mắc chứng suy nhược thần kinh lo âu"},  # neurotic
    "lex.en.100k.014773": {"vi": "bắt buộc phải làm; giúp đỡ làm ơn"},  # oblige
    "lex.en.100k.014774": {"vi": "người cư ngụ; người ngồi trong xe"},  # occupant
    "lex.en.100k.014775": {"vi": "chỉ số nhiên liệu octan xăng"},  # octane
    "lex.en.100k.014776": {"vi": "quãng tám âm nhạc; chu kỳ tám ngày"},  # octave
    "lex.en.100k.014777": {"vi": "thường hay xảy ra; nhiều bận dịp"},  # oftentimes
    "lex.en.100k.014778": {"vi": "hoạt động tác chiến quân sự (ops)"},  # ops
    "lex.en.100k.014780": {"vi": "quan trọng hàng đầu; có tính lấn át"},  # overriding
    "lex.en.100k.014781": {"vi": "ở vị trí áp chót; cận kề cuối cùng"},  # penultimate
    "lex.en.100k.014782": {"vi": "cây bạc hà cay thơm mát; kẹo bạc hà"},  # peppermint
    "lex.en.100k.014783": {"vi": "điểm bách phân vị (thống kê)"},  # percentile
    "lex.en.100k.014785": {"vi": "phong thái đĩnh đạc; sự điềm tĩnh"},  # poise
    "lex.en.100k.014787": {"vi": "nhân giống cây; truyền bá tư tưởng"},  # propagate
    "lex.en.100k.014789": {"vi": "cạy bằng xà beng; tò mò tọc mạch"},  # pry
    "lex.en.100k.014791": {"vi": "phục hồi chức vụ; khôi phục lại"},  # reinstate
    "lex.en.100k.014792": {"vi": "từ bỏ quyền hạn; nhượng quyền lại"},  # relinquish
    "lex.en.100k.014793": {"vi": "mang tính khắc phục; giúp hồi phục"},  # remedial
    "lex.en.100k.014794": {"vi": "danh tiếng lừng lẫy; sự nổi tiếng"},  # renown
    "lex.en.100k.014795": {"vi": "người trả lời khảo sát; bị đơn tòa"},  # respondent
    "lex.en.100k.014796": {"vi": "sự nối lại hoạt động; tiếp tục lại"},  # resumption
    "lex.en.100k.014797": {"vi": "ngành bán lẻ; hoạt động bán lẻ hàng"},  # retailing
    "lex.en.100k.014798": {"vi": "thoái lui thụt lùi; nghịch hành lùi"},  # retrograde
    "lex.en.100k.014799": {"pos": "verb", "vi": "tôn kính sùng bái; tôn sùng hết mực"},  # revere

    # 4801 - 4900
    "lex.en.100k.014801": {"vi": "chi hoa hồng Rosa; tên riêng Rosa"},  # rosa
    "lex.en.100k.014802": {"vi": "khuẩn ngộ độc ruột Salmonella"},  # salmonella
    "lex.en.100k.014803": {"vi": "bù nhìn rơm đuổi quạ đồng ruộng"},  # scarecrow
    "lex.en.100k.014804": {"vi": "nóng như thiêu đốt đổ lửa gay gắt"},  # scorching
    "lex.en.100k.014805": {"vi": "nhà biên kịch kịch bản phim ảnh"},  # screenwriter
    "lex.en.100k.014806": {"vi": "thầy ký chép sách; người chép thuê"},  # scribe
    "lex.en.100k.014807": {"vi": "sự chà rửa cọ sạch; lau chùi kỳ cọ"},  # scrubbing
    "lex.en.100k.014808": {"vi": "ngồi nhiều thụ động; ít vận động"},  # sedentary
    "lex.en.100k.014809": {"vi": "người lính gác cổng; lính canh gác"},  # sentry
    "lex.en.100k.014810": {"vi": "người coi sóc nhà thờ kiêm đào mộ"},  # sexton
    "lex.en.100k.014811": {"vi": "cảnh bừa bãi tan hoang; sự hỗn loạn"},  # shambles
    "lex.en.100k.014812": {"vi": "được bóc vỏ; có lớp vỏ cứng bảo vệ"},  # shelled
    "lex.en.100k.014813": {"vi": "bệnh zona thần kinh (giời leo ngứa)"},  # shingles
    "lex.en.100k.014814": {"vi": "chảo rán có tay cầm; chảo gang đúc"},  # skillet
    "lex.en.100k.014815": {"vi": "nhơn nhớt trơn trợt; nhầy nhụa"},  # slimy
    "lex.en.100k.014816": {"vi": "dép lê đi trong nhà; dép xỏ ngón"},  # slipper
    "lex.en.100k.014817": {"vi": "thoai thoải dốc; nằm nghiêng dốc"},  # sloping
    "lex.en.100k.014818": {"vi": "mõm thú nhô ra dài ngoằng; mũi mõm"},  # snout (purged single-word 'mõm')
    "lex.en.100k.014819": {"vi": "làm mềm mượt; sự mềm dịu đi"},  # softening
    "lex.en.100k.014820": {"vi": "đòn phạt đánh mông; cái tát mông"},  # spank
    "lex.en.100k.014821": {"vi": "bóng ma rùng rợn; mối lo rình rập"},  # specter
    "lex.en.100k.014822": {"vi": "sự văng bắn tung tóe nước; tạt nước"},  # splashing
    "lex.en.100k.014823": {"vi": "mầm cây mới nhú; rau mầm tươi xanh"},  # sprout
    "lex.en.100k.014824": {"pos": "noun", "vi": "vị thế uy tín xã hội; chỗ đứng"},  # standing
    "lex.en.100k.014825": {"vi": "sự khử trùng diệt khuẩn; triệt sản"},  # sterilization
    "lex.en.100k.014826": {"vi": "xe đẩy em bé nhỏ; người đi dạo phố"},  # stroller
    "lex.en.100k.014827": {"vi": "cuống vé máy bay; mẩu thuốc lá tàn"},  # stub
    "lex.en.100k.014828": {"vi": "ở phần trên văn bản luật (La-tinh)"},  # supra
    "lex.en.100k.014829": {"vi": "tính tế nhị nhạy cảm; sự khéo xử"},  # tact
    "lex.en.100k.014830": {"vi": "mớ dây bòng bong rối; mớ rắc rối"},  # tangle
    "lex.en.100k.014832": {"vi": "tia sét chớp nhoáng; tin sét đánh"},  # thunderbolt
    "lex.en.100k.014833": {"vi": "bạt nhún lò xo tập thể thao lò xo"},  # trampoline
    "lex.en.100k.014834": {"vi": "dòng sông Trent (miền trung Anh)"},  # trent
    "lex.en.100k.014836": {"vi": "áo chẽn kiểu tunic thời La Mã dài"},  # tunic
    "lex.en.100k.014837": {"vi": "có sóng siêu âm; thuộc về siêu âm"},  # ultrasonic
    "lex.en.100k.014838": {"vi": "sự hủy hoại bại vong; tháo mở ra"},  # undoing
    "lex.en.100k.014839": {"vi": "một cách bất hợp pháp; trái phép"},  # unlawfully
    "lex.en.100k.014840": {"vi": "bất kham khó bảo; ngỗ nghịch bướng"},  # unruly
    "lex.en.100k.014841": {"vi": "Liên bang Xô Viết (Liên Xô - USSR)"},  # ussr
    "lex.en.100k.014842": {"vi": "có mái vòm uốn cong; xây kiểu vòm"},  # vaulted
    "lex.en.100k.014843": {"vi": "món thịt bê sữa thơm mềm tơ"},  # veal
    "lex.en.100k.014844": {"vi": "kiểm tra đối soát xác minh dữ liệu"},  # verifying
    "lex.en.100k.014846": {"vi": "được tráng sáp bóng; phủ lớp sáp"},  # waxed
    "lex.en.100k.014847": {"vi": "người mặc đồ; người mang trang sức"},  # wearer
    "lex.en.100k.014848": {"vi": "loài cá vược trắng Whiting biển sâu"},  # whiting
    "lex.en.100k.014849": {"vi": "chủ tâm cố ý phạm luật; bướng bỉnh"},  # willful
    "lex.en.100k.014850": {"vi": "tay nghề điêu luyện; kỹ thuật khéo"},  # workmanship
    "lex.en.100k.014851": {"vi": "chim tiêu liêu nhỏ; chim hồng tước"},  # wren
    "lex.en.100k.014852": {"vi": "chữ cái Hy Lạp Zeta (ký hiệu Z, ζ)"},  # zeta
    "lex.en.100k.014853": {"vi": "nhà văn James Baldwin; họ Baldwin"},  # baldwin
    "lex.en.100k.014854": {"vi": "Đức Phật Thích Ca; bậc Giác ngộ"},  # buddha
    "lex.en.100k.014855": {"vi": "vua Edgar nước Anh; Edgar Allan Poe"},  # edgar
    "lex.en.100k.014856": {"vi": "thuộc về Hungary; tiếng Hungary"},  # hungarian
    "lex.en.100k.014857": {"vi": "quốc đảo băng giá Iceland (Bắc Âu)"},  # iceland
    "lex.en.100k.014858": {"vi": "tướng Joseph Johnston; họ Johnston"},  # johnston
    "lex.en.100k.014859": {"ipa": "/ˌɛm ɛl ˈɛs/", "vi": "giải bóng đá nhà nghề Mỹ MLS"},  # mls
    "lex.en.100k.014860": {"vi": "sự việc; vật quyền pháp lý La-tinh"},  # res
    "lex.en.100k.014861": {"vi": "thành phố Springfield (Illinois)"},  # springfield
    "lex.en.100k.014862": {"vi": "Tòa thánh Quốc gia Thành Vatican"},  # vatican
    "lex.en.100k.014863": {"vi": "nhà thơ Isaac Watts; đơn vị oát"},  # watts
    "lex.en.100k.014864": {"ipa": "/jɪɹ/", "vi": "năm (viết tắt tiếng Anh year)"},  # yr
    "lex.en.100k.014865": {"vi": "thành phố Calgary (Alberta Canada)"},  # calgary
    "lex.en.100k.014866": {"vi": "thành phố và đại học Durham (Anh)"},  # durham
    "lex.en.100k.014867": {"vi": "ông hoàng nhạc rock Elvis Presley"},  # elvis
    "lex.en.100k.014868": {"vi": "người gốc Phần Lan; cậu bé Finn"},  # finn
    "lex.en.100k.014869": {"vi": "nhà phân tâm học lỗi lạc Carl Jung"},  # jung
    "lex.en.100k.014870": {"vi": "vương triều Lancaster; thành phố"},  # lancaster
    "lex.en.100k.014871": {"ipa": "/ˌɛm ˈbiː/", "vi": "megabyte (MB); megabit dung lượng"},  # mb
    "lex.en.100k.014872": {"vi": "thành phố cảng Newport (Mỹ & Anh)"},  # newport
    "lex.en.100k.014873": {"vi": "thủ tướng William Pitt; Brad Pitt"},  # pitt
    "lex.en.100k.014874": {"vi": "nhà nước Qatar giàu có (Trung Đông)"},  # qatar
    "lex.en.100k.014875": {"vi": "quốc gia Romania (Đông Nam Âu)"},  # romania
    "lex.en.100k.014876": {"pos": "num", "vi": "số 70; bảy mươi"},  # seventy
    "lex.en.100k.014877": {"vi": "nhà vật lý J. Thomson; họ Thomson"},  # thomson
    "lex.en.100k.014878": {"vi": "quốc gia Cộng hòa Uganda (Đông Phi)"},  # uganda
    "lex.en.100k.014879": {"vi": "tiểu bang Wyoming rộng lớn (Hoa Kỳ)"},  # wyoming
    "lex.en.100k.014880": {"ipa": "/ˌtrɪpəl ˈeɪ/", "vi": "xếp hạng tín dụng AAA; hiệp hội AAA"},  # aaa
    "lex.en.100k.014881": {"vi": "thành phố cổ Alexandria (Ai Cập)"},  # alexandria
    "lex.en.100k.014882": {"vi": "Buffalo Bill Cody; tên riêng Cody"},  # cody
    "lex.en.100k.014883": {"vi": "bán đảo Cornwall (Tây Nam nước Anh)"},  # cornwall
    "lex.en.100k.014884": {"ipa": "/ˌdiː ˈbiː/", "vi": "đề-xi-ben (dB); cơ sở dữ liệu DB"},  # db
    "lex.en.100k.014885": {"ipa": "/ˌkeɪ ˈwaɪ/", "vi": "viết tắt bang Kentucky Hoa Kỳ (KY)"},  # ky
    "lex.en.100k.014886": {"vi": "họ Sanchez; cầu thủ bóng đá Sanchez"},  # sanchez
    "lex.en.100k.014887": {"vi": "kính viễn vọng James Webb; họ Webb"},  # webb
    "lex.en.100k.014888": {"vi": "trôi dạt bềnh bồng; mất định hướng"},  # adrift
    "lex.en.100k.014889": {"vi": "dưới sự bảo trợ che chở; sự bảo hộ"},  # aegis
    "lex.en.100k.014891": {"vi": "nhà giả kim thuật thời trung cổ"},  # alchemist
    "lex.en.100k.014892": {"vi": "khiến người khác xa lánh; cô lập"},  # alienate
    "lex.en.100k.014893": {"vi": "cuốn niên giám niên lịch hàng năm"},  # almanac
    "lex.en.100k.014894": {"vi": "cây nha đam mọng nước; cây lô hội"},  # aloe
    "lex.en.100k.014895": {"vi": "sự hợp nhất doanh nghiệp; pha trộn"},  # amalgamation
    "lex.en.100k.014896": {"vi": "thuộc loài lưỡng cư; đổ bộ thủy bộ"},  # amphibious
    "lex.en.100k.014897": {"vi": "sự khuếch đại tín hiệu; làm rõ thêm"},  # amplification
    "lex.en.100k.014898": {"vi": "cũ kỹ lỗi thời; lạc hậu cổ lỗ sĩ"},  # antiquated (purged single-word 'cũ')

    # 4901 - 5000
    "lex.en.100k.014901": {"vi": "bãi chiến trường; bang tranh chấp"},  # battleground
    "lex.en.100k.014902": {"vi": "đính hạt cườm; đọng giọt tấm tấm"},  # beaded
    "lex.en.100k.014903": {"vi": "cơ bắp tay trước; bắp tay nhị đầu"},  # biceps
    "lex.en.100k.014904": {"vi": "vết phồng rộp da; vết rộp bóng nước"},  # blister
    "lex.en.100k.014905": {"vi": "lậu không bản quyền; nấu rượu lậu"},  # bootleg
    "lex.en.100k.014906": {"vi": "trận so găng đấu quyền; đợt ốm sốt"},  # bout
    "lex.en.100k.014907": {"vi": "loài cá bơn dẹt brill biển sâu"},  # brill
    "lex.en.100k.014908": {"vi": "nhà thơ Rupert Brooke; dòng suối"},  # brooke
    "lex.en.100k.014909": {"vi": "chuyên khoa tim mạch (y học)"},  # cardiology
    "lex.en.100k.014910": {"vi": "họa sĩ vẽ truyện tranh biếm họa"},  # cartoonist
    "lex.en.100k.014911": {"vi": "nồi đất nung hầm; món hầm đút lò"},  # casserole
    "lex.en.100k.014912": {"vi": "chiếc vạc lớn nấu ăn; vạc phù thủy"},  # cauldron
    "lex.en.100k.014913": {"vi": "chất xơ xen-lu-lô-zơ (sinh học)"},  # cellulose
    "lex.en.100k.014914": {"vi": "ngôi nhà gỗ trên núi kiểu Thụy Sĩ"},  # chalet
    "lex.en.100k.014915": {"vi": "hiếm muộn không con cái; vô sinh"},  # childless
    "lex.en.100k.014916": {"vi": "sạch sẽ ngăn nắp; dứt khoát gãy gọn"},  # cleanly
    "lex.en.100k.014917": {"vi": "sữa rửa mặt làm sạch da; chất tẩy ố"},  # cleanser
    "lex.en.100k.014918": {"vi": "tàu buồm vượt sóng; tông đơ kéo tỉa"},  # clipper
    "lex.en.100k.014919": {"vi": "phủ đầy mây mù; u sầu u ám mờ đục"},  # clouded
    "lex.en.100k.014920": {"vi": "bức tượng khổng lồ; người khổng lồ"},  # colossus
    "lex.en.100k.014921": {"vi": "rất đáng biểu dương; đáng ca ngợi"},  # commendable
    "lex.en.100k.014922": {"vi": "với mức giá cạnh tranh; ganh đua"},  # competitively
    "lex.en.100k.014923": {"vi": "tổng kiểm toán; kiểm soát tài chính"},  # comptroller
    "lex.en.100k.014924": {"vi": "con thỏ rừng hoang dã; thỏ coney"},  # coney
    "lex.en.100k.014925": {"vi": "theo lệ thông thường; theo quy ước"},  # conventionally
    "lex.en.100k.014926": {"vi": "quanh co uốn khúc; rối rắm phức tạp"},  # convoluted
    "lex.en.100k.014927": {"vi": "khu rào quây nhốt đàn ngựa gia súc"},  # corral
    "lex.en.100k.014928": {"vi": "luật sư bào chữa; lời khuyên can"},  # counsel
    "lex.en.100k.014929": {"vi": "tiếng bồi Creole; người lai Creole"},  # creole
    "lex.en.100k.014930": {"vi": "ô buồng làm việc văn phòng; góc nhỏ"},  # cubicle
    "lex.en.100k.014931": {"vi": "uốn cong cong mềm mại; uốn khúc"},  # curving (purged single-word 'cong')
    "lex.en.100k.014932": {"vi": "nhà bác học Charles Darwin tiến hóa"},  # darwin
    "lex.en.100k.014933": {"vi": "thị trấn Dawson (Canada); họ Dawson"},  # dawson
    "lex.en.100k.014934": {"vi": "sự giải cứu khỏi hiểm nguy; cứu rỗi"},  # deliverance
    "lex.en.100k.014935": {"vi": "bần hàn cùng quẫn; trắng tay nghèo"},  # destitute
    "lex.en.100k.014936": {"vi": "đi chệch đường lối; lệch chuẩn mực"},  # deviate
    "lex.en.100k.014937": {"vi": "sự khéo léo nhanh nhạy đôi bàn tay"},  # dexterity
    "lex.en.100k.014938": {"vi": "sự pha loãng nồng độ; loãng vốn"},  # dilution
    "lex.en.100k.014939": {"vi": "linh kiện đi-ốt bán dẫn (điện tử)"},  # diode
    "lex.en.100k.014940": {"vi": "sống phóng túng trác táng; hao tán"},  # dissipated
    "lex.en.100k.014941": {"vi": "chơi nhạc êm dịu ngọt ngào (dolce)"},  # dolce
    "lex.en.100k.014942": {"vi": "thuốc an thần làm dịu; sự chán ngắt"},  # downer
    "lex.en.100k.014943": {"ipa": "/ˌdiː ˈɛs/", "vi": "nguyên tố hóa học Ds; máy game DS"},  # ds
    "lex.en.100k.014944": {"vi": "một cách linh hoạt; đầy năng động"},  # dynamically
    "lex.en.100k.014945": {"ipa": "/ˌiː diː ˈɛs/", "vi": "hội chứng gen Ehlers-Danlos (y học)"},  # eds
    "lex.en.100k.014946": {"vi": "sự bắn phóng ra; tống khứ đuổi ra"},  # ejection
    "lex.en.100k.014948": {"vi": "thuộc về loài ngựa; giống như ngựa"},  # equine
    "lex.en.100k.014949": {"vi": "hợp chất hữu cơ este thơm (hóa học)"},  # ester
    "lex.en.100k.014950": {"vi": "sự bốc hơi nước; quá trình bay hơi"},  # evaporation
    "lex.en.100k.014951": {"vi": "thúc đẩy tiến độ; xúc tiến nhanh"},  # expedite
    "lex.en.100k.014952": {"vi": "mang tính định mệnh; hệ trọng"},  # fateful
    "lex.en.100k.014953": {"vi": "mũ phớt vành mềm fedora quý ông"},  # fedora
    "lex.en.100k.014954": {"vi": "pháo phòng không; búa rìu dư luận"},  # flak
    "lex.en.100k.014956": {"vi": "bàn đạp tiến công; vị trí đứng chân"},  # foothold
    "lex.en.100k.014957": {"vi": "đáng sợ gớm ghiếc hiểm trở; cấm chỉ"},  # forbidding
    "lex.en.100k.014958": {"vi": "bị tước mất quyền lợi; bị tịch thu"},  # forfeited
    "lex.en.100k.014959": {"vi": "tình cảm anh em ruột thịt; huynh đệ"},  # fraternal
    "lex.en.100k.014960": {"vi": "lớp lông tơ mịn màng; cảnh sát cớm"},  # fuzz
    "lex.en.100k.014961": {"vi": "Isabella Gardner; Martin Gardner"},  # gardner
    "lex.en.100k.014962": {"vi": "ghê rợn tái mét mặt mày; kinh hoàng"},  # ghastly
    "lex.en.100k.014963": {"vi": "đem lại sự thỏa mãn; vừa lòng hả hê"},  # gratifying
    "lex.en.100k.014964": {"vi": "nhà văn lừng danh Graham Greene"},  # greene
    "lex.en.100k.014965": {"vi": "sự nhiệt tình hào hứng; sự say sưa"},  # gusto
    "lex.en.100k.014967": {"vi": "đường chân tóc; vết rạn nứt sợi tóc"},  # hairline
    "lex.en.100k.014968": {"vi": "tai nghe điện thoại; máy cầm tay"},  # handset
    "lex.en.100k.014969": {"vi": "vô cùng đau đớn xót xa; kinh hãi"},  # harrowing
    "lex.en.100k.014970": {"vi": "nữ thừa kế gia sản kếch xù"},  # heiress
    "lex.en.100k.014971": {"vi": "thuộc về lá gan cơ thể; rêu lá gan"},  # hepatic
    "lex.en.100k.014972": {"vi": "đơn vị tần số Hertz (ký hiệu Hz)"},  # hertz
    "lex.en.100k.014973": {"vi": "hỗn hợp dị thể; không thuần nhất"},  # heterogeneous
    "lex.en.100k.014974": {"vi": "bao da đựng súng lục gắn thắt lưng"},  # holster
    "lex.en.100k.014975": {"vi": "móng vuốt guốc ngựa bò; bước đi bộ"},  # hoof
    "lex.en.100k.014976": {"vi": "kỵ sĩ cưỡi ngựa; người nài ngựa"},  # horseman
    "lex.en.100k.014977": {"vi": "đại văn hào nước Pháp Victor Hugo"},  # hugo
    "lex.en.100k.014978": {"vi": "thân vỏ tàu thuyền; vỏ hạt bắp ngô"},  # hull
    "lex.en.100k.014979": {"vi": "chướng ngại vật cản trở; tật ngọng"},  # impediment
    "lex.en.100k.014980": {"vi": "không thể đâm thủng; kiên cố bí ẩn"},  # impenetrable
    "lex.en.100k.014981": {"vi": "không thể tưởng tượng nổi; khó tin"},  # inconceivable
    "lex.en.100k.014982": {"vi": "sự phẫn nộ trước điều bất công"},  # indignation
    "lex.en.100k.014983": {"vi": "theo bản năng tự nhiên; vô thức"},  # instinctive
    "lex.en.100k.014985": {"vi": "các hệ tư tưởng chủ nghĩa; trào lưu"},  # ism
    "lex.en.100k.014986": {"vi": "tổ chức phát hành chứng khoán thẻ"},  # issuer
    "lex.en.100k.014987": {"vi": "lời nói đùa cợt trêu ghẹo; trò cười"},  # jest
    "lex.en.100k.014988": {"vi": "dao mổ nhỏ; tạp chí y khoa Lancet"},  # lancet
    "lex.en.100k.014989": {"vi": "bão đổ bộ vào đất liền; cập bờ"},  # landfall
    "lex.en.100k.014990": {"vi": "bị nứt rò rỉ nước; hay để lộ bí mật"},  # leaky
    "lex.en.100k.014991": {"vi": "thể thơ hài hước 5 câu Limerick"},  # limerick
    "lex.en.100k.014992": {"vi": "người thích sống một mình cô độc"},  # loner
    "lex.en.100k.014993": {"vi": "từ tính hút; sức lôi cuốn mãnh liệt"},  # magnetism
    "lex.en.100k.014994": {"vi": "rất bài bản có phương pháp; trật tự"},  # methodical
    "lex.en.100k.014995": {"vi": "nghệ sĩ diễn kịch câm hình thể"},  # mime
    "lex.en.100k.014996": {"vi": "ở mức độ tối thiểu nhất; rất ít ỏi"},  # minimally
    "lex.en.100k.014997": {"vi": "sự tạm ngưng trả nợ; lệnh tạm hoãn"},  # moratorium
    "lex.en.100k.014998": {"vi": "chuyển hóa dần dần; biến hình dạng"},  # morph
    "lex.en.100k.014999": {"vi": "chủ nghĩa đa dạng văn hóa sắc tộc"},  # multiculturalism
}

# Verify lengths <= 35
for k, v in OVERRIDES_B03_R10.items():
    if "vi" in v:
        assert len(v["vi"]) <= 35, f"Length > 35 for {k}: {v['vi']} ({len(v['vi'])})"

with open('content/english/qa-batches/batch-03.json', 'r', encoding='utf-8') as f:
    batch_data = json.load(f)

# Apply overrides to records in range 4500 to 5000
count = 0
for idx in range(4500, 5000):
    rec = batch_data['records'][idx]
    rid = rec['id']
    if rid in OVERRIDES_B03_R10:
        count += 1
        for field, val in OVERRIDES_B03_R10[rid].items():
            rec[field] = val
        rec['status'] = 'reviewed'

batch_data['reviewedCount'] = 5000
batch_data['status'] = 'completed'

with open('content/english/qa-batches/batch-03.json', 'w', encoding='utf-8') as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully applied Batch 03 Round 10 ({count} overrides). Reviewed: {batch_data['reviewedCount']}/5000. Status: {batch_data['status']}")
