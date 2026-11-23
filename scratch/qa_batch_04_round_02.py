import json

# Cognitive manual QA overrides for Batch 04 Round 02 (records 500 to 1000, STT 501 to 1000)
OVERRIDES_B04_R02 = {
    # 501 - 600
    "lex.en.100k.015501": {"vi": "rùng rợn ma quái; gợi nhớ cái chết"},  # macabre
    "lex.en.100k.015502": {"vi": "dạ hội hóa trang; màn kịch giả tạo"},  # masquerade
    "lex.en.100k.015503": {"vi": "vở kịch ướt át; tình tiết giật gân"},  # melodrama
    "lex.en.100k.015504": {"vi": "loài chim hét đen; màu lông loang"},  # merle
    "lex.en.100k.015505": {"vi": "mắt lưới; sự ăn khớp nhịp nhàng"},  # mesh
    "lex.en.100k.015507": {"vi": "bị ngược đãi bất công; bị bạo hành"},  # mistreated
    "lex.en.100k.015508": {"vi": "nghẹt lại âm thanh; nghe trầm đục"},  # muffled
    "lex.en.100k.015509": {"vi": "chứng ái kỷ tự luyến; thói tự cao"},  # narcissism
    "lex.en.100k.015510": {"vi": "có rãnh khía chữ V; khía răng cưa"},  # notched
    "lex.en.100k.015511": {"vi": "quả nhục đậu khấu; xỏ háng đối thủ"},  # nutmeg
    "lex.en.100k.015512": {"vi": "tinh ý tinh tường; tuân thủ lễ nghi"},  # observant
    "lex.en.100k.015513": {"vi": "góc tù hình học; đần độn chậm hiểu"},  # obtuse
    "lex.en.100k.015514": {"vi": "con chim đà điểu châu Phi khổng lồ"},  # ostrich (purged single-word 'đà điểu')
    "lex.en.100k.015515": {"vi": "trời u ám mây mù bao phủ; râm mát"},  # overcast
    "lex.en.100k.015516": {"vi": "người đốc công giám sát; cai quản"},  # overseer
    "lex.en.100k.015517": {"vi": "tấm gương mẫu mực; hình mẫu chuẩn"},  # paragon
    "lex.en.100k.015519": {"vi": "một cách kiên trì bền bỉ; dai dẳng"},  # persistently
    "lex.en.100k.015520": {"vi": "cánh hoa tươi mềm mại"},  # petal
    "lex.en.100k.015521": {"vi": "hành động vuốt ve mơn trớn; âu yếm"},  # petting
    "lex.en.100k.015522": {"vi": "kiểu hình hiển hiện (di truyền học)"},  # phenotype (purged single-word 'kiểu hình')
    "lex.en.100k.015523": {"vi": "sinh vật phù du trôi dạt trong nước"},  # plankton
    "lex.en.100k.015524": {"vi": "mang nặng định kiến; có thành kiến"},  # prejudiced
    "lex.en.100k.015525": {"vi": "ngăn cấm; giá cả đắt đỏ cắt cổ"},  # prohibitive
    "lex.en.100k.015526": {"vi": "việc cắt tỉa cành cây; cắt giảm"},  # pruning
    "lex.en.100k.015527": {"vi": "người đặt cược đánh bạc; khách hàng"},  # punter
    "lex.en.100k.015528": {"vi": "thuộc gen lặn; tính trạng lặn"},  # recessive (purged single-word 'lặn')
    "lex.en.100k.015529": {"vi": "hoàn trả chi phí; bồi hoàn tiền túi"},  # reimburse
    "lex.en.100k.015530": {"vi": "cải tạo nâng cấp; tu sửa làm mới"},  # renovate (purged single-word 'tu sửa')
    "lex.en.100k.015531": {"vi": "sự hồi hương; chuyển tiền về nước"},  # repatriation (purged single-word 'hồi hương')
    "lex.en.100k.015532": {"vi": "giúp hồi phục sức khỏe; bổ dưỡng"},  # restorative
    "lex.en.100k.015533": {"vi": "thụt vào trong; rút lại lời nói"},  # retracted
    "lex.en.100k.015534": {"vi": "đồng tiền rupi (Ấn Độ và Pakistan)"},  # rupee
    "lex.en.100k.015535": {"vi": "một cách châm chọc mỉa mai sâu cay"},  # sarcastically
    "lex.en.100k.015536": {"vi": "cuộn giấy da cổ; cuộn màn hình xem"},  # scroll
    "lex.en.100k.015537": {"vi": "đồ cũ đã qua sử dụng; tin nghe lại"},  # secondhand
    "lex.en.100k.015538": {"vi": "chất lượng kém ẩu tả; đồ làm dối"},  # shoddy
    "lex.en.100k.015539": {"vi": "nhơ nhớp bẩn thỉu; đồi bại đê tiện"},  # sleazy
    "lex.en.100k.015540": {"vi": "nụ cười khẩy đắc ý; cười nhếch mép"},  # smirk
    "lex.en.100k.015541": {"vi": "chim dẽ giun; bắn tỉa từ xa"},  # snipe
    "lex.en.100k.015542": {"vi": "trầm mặc ảm đạm u tối; buồn thảm"},  # somber
    "lex.en.100k.015543": {"vi": "sự huy hoàng tráng lệ; vẻ lộng lẫy"},  # splendor
    "lex.en.100k.015544": {"vi": "tiết trời mùa xuân; thời tuổi trẻ"},  # springtime
    "lex.en.100k.015545": {"vi": "vòi tưới cỏ tự động; vòi chữa cháy"},  # sprinkler
    "lex.en.100k.015546": {"vi": "nan ván thùng rượu; khuông nhạc kẻ"},  # stave
    "lex.en.100k.015547": {"vi": "tiểu đơn vị thành phần; phân bộ nhỏ"},  # subunit
    "lex.en.100k.015548": {"vi": "ngột ngạt ngột thở; bóp nghẹt tự do"},  # suffocating
    "lex.en.100k.015549": {"vi": "chi Lợn sinh học; đáng ngờ (sus)"},  # sus
    "lex.en.100k.015551": {"vi": "trò chơi quay số trúng thưởng lớn"},  # sweepstakes
    "lex.en.100k.015552": {"vi": "sự tổng hợp hóa chất; sự kết hợp"},  # synthesis (purged single-word 'tổng hợp')
    "lex.en.100k.015553": {"vi": "nghề may đo trang phục; may mặc"},  # tailoring
    "lex.en.100k.015554": {"vi": "tương đương với; chẳng khác gì là"},  # tantamount
    "lex.en.100k.015555": {"vi": "căng dây đàn; cơ bắp săn chắc căng"},  # taut
    "lex.en.100k.015556": {"vi": "lộ tẩy để lộ dấu vết; kẻ mách lẻo"},  # telltale
    "lex.en.100k.015557": {"vi": "thuộc vùng ngực khoang lồng ngực"},  # thoracic (purged single-word 'ngực')
    "lex.en.100k.015558": {"vi": "có thể chuyển nhượng sang tên được"},  # transferable
    "lex.en.100k.015559": {"vi": "cơn lốc xoáy kinh hoàng; vòi rồng"},  # twister
    "lex.en.100k.015560": {"vi": "đột xuất không báo trước; bất ngờ"},  # unannounced
    "lex.en.100k.015561": {"vi": "sự vạch trần bộc lộ; khám phá ra"},  # uncovering
    "lex.en.100k.015563": {"vi": "yên bình không có biến cố xáo trộn"},  # uneventful
    "lex.en.100k.015566": {"vi": "luật bất thành văn; truyền miệng"},  # unwritten
    "lex.en.100k.015567": {"vi": "thuộc về xe cộ giao thông đường bộ"},  # vehicular (purged single-word 'xe cộ')
    "lex.en.100k.015569": {"vi": "một cách tàn bạo hung ác dã man"},  # viciously
    "lex.en.100k.015570": {"vi": "hành động lội nước bì bõm; lội bùn"},  # wading
    "lex.en.100k.015571": {"vi": "trăng khuyết; suy giảm dần tàn lụi"},  # waning
    "lex.en.100k.015572": {"vi": "hoàn toàn toàn bộ 100%; trọn vẹn"},  # wholly
    "lex.en.100k.015573": {"vi": "nghị lực kiên cường; ý chí sắt đá"},  # willpower
    "lex.en.100k.015574": {"vi": "nghề mộc thợ gỗ; chế tác đồ mộc"},  # woodworking
    "lex.en.100k.015575": {"vi": "phủ lông cừu xù xì; mập mờ mơ hồ"},  # woolly
    "lex.en.100k.015576": {"vi": "củ khoai mỡ tím; củ từ củ khoai"},  # yam
    "lex.en.100k.015577": {"vi": "lòng đỏ quả trứng gà vịt giàu đạm"},  # yolk (purged single-word 'lòng đỏ')
    "lex.en.100k.015578": {"vi": "đường ngoặt góc nhọn gấp khúc (zig)"},  # zig
    "lex.en.100k.015579": {"ipa": "/ˌeɪ siː ˈsiː/", "vi": "giải đấu ACC; Bộ Tư lệnh Tác chiến"},  # acc
    "lex.en.100k.015580": {"vi": "tàu điện ngầm BART; tước hiệu Bart"},  # bart
    "lex.en.100k.015581": {"vi": "thủ đô Copenhagen (Đan Mạch)"},  # copenhagen
    "lex.en.100k.015582": {"ipa": "/ˌdiː ˈɛl/", "vi": "đề-xi-lít (dl); bằng lái xe DL"},  # dl
    "lex.en.100k.015583": {"vi": "sợi xơ dệt vải; chất xơ dinh dưỡng"},  # fibre (purged single-word 'sợi')
    "lex.en.100k.015584": {"vi": "thuộc về Phần Lan; tiếng Phần Lan"},  # finnish
    "lex.en.100k.015585": {"vi": "đáng kính trọng; mang lại danh dự"},  # honourable
    "lex.en.100k.015586": {"vi": "thủ đô Jakarta (nước Indonesia)"},  # jakarta
    "lex.en.100k.015587": {"vi": "thành phố Johannesburg (Nam Phi)"},  # johannesburg
    "lex.en.100k.015588": {"vi": "nàng Judith dũng cảm (Kinh Thánh)"},  # judith
    "lex.en.100k.015589": {"vi": "George Meredith; tên riêng Meredith"},  # meredith
    "lex.en.100k.015590": {"vi": "thuộc về Giáo phái Mặc Môn (Mormon)"},  # mormon
    "lex.en.100k.015591": {"vi": "quốc gia Somalia (Đông Phi)"},  # somalia
    "lex.en.100k.015592": {"vi": "chiếc cốc gốm hình ông già Toby jug"},  # toby
    "lex.en.100k.015593": {"vi": "xin lỗi; tạ lỗi chân thành"},  # apologise (purged crawler error 'biện hộ; bào chữa')
    "lex.en.100k.015594": {"vi": "xinh đẹp duyên dáng; cô nàng Bonnie"},  # bonnie
    "lex.en.100k.015595": {"vi": "tài tử Dustin Hoffman; họ Hoffman"},  # hoffman
    "lex.en.100k.015596": {"vi": "Thánh Jerome dịch Kinh Thánh"},  # jerome
    "lex.en.100k.015597": {"vi": "nhà nước Kuwait; thủ đô Kuwait"},  # kuwait
    "lex.en.100k.015598": {"vi": "thi sĩ Percy Shelley; họ Percy"},  # percy
    "lex.en.100k.015599": {"vi": "thủ đô Santiago hoa lệ (Chile)"},  # santiago
    "lex.en.100k.015600": {"vi": "trang trại Tara; đồi Tara (Ireland)"},  # tara

    # 601 - 700
    "lex.en.100k.015601": {"vi": "thủ đô Warsaw (thủ đô Ba Lan)"},  # warsaw
    "lex.en.100k.015602": {"vi": "tiếng Di (ngôn ngữ dân tộc Di)"},  # yi
    "lex.en.100k.015603": {"vi": "thành phố Bombay cổ (nay là Mumbai)"},  # bombay
    "lex.en.100k.015604": {"vi": "quận Bronx (thành phố New York)"},  # bronx
    "lex.en.100k.015605": {"vi": "tên riêng Cynthia; nữ thần Artemis"},  # cynthia
    "lex.en.100k.015606": {"vi": "thuộc Dominica; tu sĩ dòng Đa Minh"},  # dominican
    "lex.en.100k.015608": {"ipa": "/ˌiː ˈviː/", "vi": "xe điện (EV); đơn vị electron-vôn"},  # ev
    "lex.en.100k.015609": {"ipa": "/ˌɛf ˈoʊ/", "vi": "sĩ quan bay FO; bộ ngoại giao FO"},  # fo
    "lex.en.100k.015610": {"vi": "nhà vật lý nhiệt động J. W. Gibbs"},  # gibbs
    "lex.en.100k.015611": {"ipa": "/ˌdʒiː ɛm ˈtiː/", "vi": "giờ chuẩn quốc tế GMT (Greenwich)"},  # gmt
    "lex.en.100k.015612": {"vi": "vùng nghỉ dưỡng The Hamptons (Mỹ)"},  # hampton
    "lex.en.100k.015613": {"vi": "nhà văn Herman Melville; họ Herman"},  # herman
    "lex.en.100k.015614": {"ipa": "/ˈɑnɚz/", "vi": "bằng đại học danh dự; sự vinh danh"},  # honours
    "lex.en.100k.015615": {"vi": "ngôn ngữ đánh dấu siêu văn bản HTML"},  # html
    "lex.en.100k.015616": {"vi": "thành phố cảng Kobe; thịt bò Kobe"},  # kobe
    "lex.en.100k.015617": {"vi": "thuộc về Hội thánh Tin lành Giám Lý"},  # methodist
    "lex.en.100k.015618": {"vi": "công quốc Monaco giàu có (châu Âu)"},  # monaco
    "lex.en.100k.015619": {"vi": "siêu mẫu Naomi Campbell; tên Naomi"},  # naomi
    "lex.en.100k.015620": {"vi": "thủ đô Praha cổ kính (Cộng hòa Séc)"},  # prague
    "lex.en.100k.015621": {"vi": "tổ chức khủng bố quốc tế Al-Qaeda"},  # qaeda
    "lex.en.100k.015622": {"vi": "vua Saul đầu tiên của Israel cổ đại"},  # saul
    "lex.en.100k.015623": {"vi": "đảo Trinidad (Trinidad và Tobago)"},  # trinidad
    "lex.en.100k.015624": {"ipa": "/vɑːr/", "vi": "công nghệ trợ lý trọng tài VAR"},  # var
    "lex.en.100k.015625": {"vi": "liệu pháp châm cứu huyệt đạo đông y"},  # acupuncture (purged single-word 'châm cứu')
    "lex.en.100k.015626": {"vi": "bình xịt sol khí hạt sương áp suất"},  # aerosol (purged single-word 'sol khí')
    "lex.en.100k.015627": {"vi": "bột thạch rau câu agar tự nhiên"},  # agar
    "lex.en.100k.015628": {"vi": "được tổng hợp gộp chung lại số liệu"},  # aggregated
    "lex.en.100k.015630": {"vi": "ion amoni hóa học (gốc NH4+)"},  # ammonium
    "lex.en.100k.015631": {"vi": "mối tình vụng trộm đắm say lén lút"},  # amour
    "lex.en.100k.015632": {"vi": "sự ưng thuận phê chuẩn chính thức"},  # assent
    "lex.en.100k.015633": {"vi": "hành vi tàn bạo dã man; tội ác lớn"},  # atrocity
    "lex.en.100k.015634": {"vi": "cửa sau; cửa ngầm bảo mật backdoor"},  # backdoor
    "lex.en.100k.015635": {"vi": "thủ đô Baghdad lịch sử (Iraq)"},  # baghdad
    "lex.en.100k.015636": {"vi": "nụ cười rạng rỡ hớn hở; tỏa sáng"},  # beaming
    "lex.en.100k.015637": {"vi": "môn thể thao bi-a lỗ và carom"},  # billiards
    "lex.en.100k.015638": {"vi": "đã được tẩy trắng; bị bạc màu nắng"},  # bleached
    "lex.en.100k.015639": {"vi": "vết mực nhòe ố; vết nhơ thanh danh"},  # blot
    "lex.en.100k.015640": {"vi": "báo trước điềm; dự báo trước"},  # bode
    "lex.en.100k.015641": {"vi": "người gốc Hà Lan Boer tại Nam Phi"},  # boer
    "lex.en.100k.015642": {"vi": "giai cấp tư sản sở hữu tư bản"},  # bourgeoisie
    "lex.en.100k.015643": {"vi": "ở tư thế chuẩn bị sẵn sàng va chạm"},  # braced
    "lex.en.100k.015644": {"vi": "phồng to căng tròn nhô lồi ra ngoài"},  # bulging
    "lex.en.100k.015645": {"vi": "sản phẩm phụ sản xuất; hệ quả phụ"},  # byproduct
    "lex.en.100k.015647": {"vi": "thủ đô Canberra (nước Úc)"},  # canberra
    "lex.en.100k.015648": {"vi": "cực âm catot (vật lý điện tử)"},  # cathode (purged single-word 'âm cực')
    "lex.en.100k.015649": {"vi": "quần vải kaki thô dệt chéo chino"},  # chino
    "lex.en.100k.015650": {"vi": "phép lịch sự hòa nhã; tính văn minh"},  # civility
    "lex.en.100k.015651": {"vi": "ở đỉnh điểm cao trào kịch tính"},  # climactic
    "lex.en.100k.015652": {"vi": "hiện tượng gom cụm nhóm dữ liệu"},  # clustering
    "lex.en.100k.015653": {"vi": "sự đồng lõa tiếp tay; sự thông đồng"},  # complicity
    "lex.en.100k.015654": {"vi": "pháo hoa giấy tung bay tiệc tùng"},  # confetti
    "lex.en.100k.015655": {"vi": "cấu hình thông số; thiết lập máy"},  # configure
    "lex.en.100k.015656": {"vi": "người sành sỏi nghệ thuật món ăn"},  # connoisseur
    "lex.en.100k.015657": {"vi": "kho ngữ liệu văn bản; tập tác phẩm"},  # corpus (purged single-word 'ngữ liệu')
    "lex.en.100k.015658": {"vi": "mối tương quan; sự liên hệ gắn bó"},  # correlation
    "lex.en.100k.015659": {"vi": "áo nịt ngực thắt eo corset phụ nữ"},  # corset
    "lex.en.100k.015660": {"vi": "hoóc-môn căng thẳng stress Cortisol"},  # cortisol
    "lex.en.100k.015661": {"vi": "hũ sành đất nung; chuyện xàm nhảm"},  # crock
    "lex.en.100k.015662": {"vi": "lúc rạng đông bình minh hé sáng"},  # daybreak
    "lex.en.100k.015663": {"vi": "ngành khoa học nhân khẩu học"},  # demography
    "lex.en.100k.015664": {"vi": "sự xuất xứ bắt nguồn; từ phái sinh"},  # derivation
    "lex.en.100k.015665": {"vi": "tội đào ngũ; sự ruồng bỏ nghĩa vụ"},  # desertion
    "lex.en.100k.015666": {"vi": "gian xảo quanh co; lươn lẹo quỷ kế"},  # devious
    "lex.en.100k.015667": {"vi": "toàn bộ danh mục đĩa nhạc của ca sĩ"},  # discography
    "lex.en.100k.015669": {"vi": "bị sai khớp trật khớp xương đau đớn"},  # dislocated
    "lex.en.100k.015670": {"vi": "máy phân phối nhả hàng; bình xịt"},  # dispenser
    "lex.en.100k.015671": {"vi": "phân kỳ rẽ nhánh; bất đồng ý kiến"},  # diverge
    "lex.en.100k.015672": {"vi": "chòm sao Kiếm Ngư; loài cá heo dạt"},  # dorado
    "lex.en.100k.015673": {"vi": "thuyền độc mộc; hầm trú ẩn chìm"},  # dugout
    "lex.en.100k.015674": {"vi": "quốc gia Cộng hòa Ecuador (Nam Mỹ)"},  # ecuador
    "lex.en.100k.015675": {"vi": "thành phố Edmonton (Alberta Canada)"},  # edmonton
    "lex.en.100k.015677": {"vi": "đã bốc hơi cạn; sữa đặc cô đặc"},  # evaporated
    "lex.en.100k.015678": {"vi": "khơi gợi cảm xúc; gợi nhớ quá khứ"},  # evocative
    "lex.en.100k.015679": {"vi": "dập tắt ngọn lửa; dập tắt hy vọng"},  # extinguish
    "lex.en.100k.015680": {"vi": "sự thúc đẩy hỗ trợ; tạo điều kiện"},  # facilitation
    "lex.en.100k.015681": {"vi": "thoang thoảng lờ mờ; yếu ớt mờ ảo"},  # faintly
    "lex.en.100k.015683": {"vi": "sự thụ tinh thụ phấn; việc bón phân"},  # fertilization
    "lex.en.100k.015684": {"vi": "số lượng ít ỏi nhất; hiếm hoi nhất"},  # fewest
    "lex.en.100k.015685": {"vi": "vật liệu sợi thủy tinh cách nhiệt"},  # fiberglass
    "lex.en.100k.015686": {"vi": "kỹ thuật bấm ngón đàn; sự sờ mó"},  # fingering
    "lex.en.100k.015687": {"vi": "nhà văn Scott Fitzgerald (Gatsby)"},  # fitzgerald
    "lex.en.100k.015688": {"vi": "có rừng rậm bao phủ; rợp bóng cây"},  # forested
    "lex.en.100k.015689": {"vi": "phủ đầy sương giá; kính mờ nhám"},  # frosted
    "lex.en.100k.015690": {"vi": "sự tràn đầy viên mãn; độ đẫy đà"},  # fullness
    "lex.en.100k.015691": {"vi": "cơn gió giông lốc bão tố thổi mạnh"},  # gale
    "lex.en.100k.015692": {"pos": "verb", "vi": "bước phi nước đại; phi nước kiệu"},  # gallop
    "lex.en.100k.015693": {"vi": "thuộc về dòng dõi gia phả tổ tiên"},  # genealogical
    "lex.en.100k.015694": {"vi": "người ngoài Do Thái giáo; dân ngoại"},  # gentile
    "lex.en.100k.015695": {"vi": "một cách nhã nhặn; rộng lượng từ ái"},  # graciously
    "lex.en.100k.015696": {"vi": "thảo nguyên đồng cỏ xanh ngút ngàn"},  # grassland
    "lex.en.100k.015697": {"vi": "thiêng liêng cao quý; tôn sùng"},  # hallowed
    "lex.en.100k.015698": {"vi": "ngập ngừng ngắc ngứ; khập khiễng"},  # halting
    "lex.en.100k.015699": {"vi": "thủ phủ Hartford (bang Connecticut)"},  # hartford
    "lex.en.100k.015700": {"vi": "John Hawkins; thị trấn Hawkins"},  # hawkins

    # 701 - 800
    "lex.en.100k.015701": {"vi": "làm tăng cao độ; làm sâu sắc thêm"},  # heighten
    "lex.en.100k.015702": {"vi": "bánh lái tàu thuyền; vị trí chỉ huy"},  # helm
    "lex.en.100k.015703": {"vi": "cung cấp nước cho cơ thể; hydrat"},  # hydrate
    "lex.en.100k.015704": {"ipa": "/ˌaɪ siː ˈsiː/", "vi": "Tòa án Hình sự Quốc tế ICC"},  # icc
    "lex.en.100k.015705": {"vi": "không thấm qua; trơ trước tác động"},  # impervious
    "lex.en.100k.015706": {"vi": "ám chỉ liên can dính líu vào vụ án"},  # implicate
    "lex.en.100k.015707": {"vi": "việc nhập khẩu hàng hóa; du nhập"},  # importation
    "lex.en.100k.015708": {"vi": "liên miên không ngớt; dồn dập"},  # incessant
    "lex.en.100k.015709": {"vi": "đang tại chức đương nhiệm; bổn phận"},  # incumbent
    "lex.en.100k.015710": {"vi": "được cá nhân hóa; may đo riêng"},  # individualized
    "lex.en.100k.015711": {"vi": "tham lam vô đáy; không thể thỏa mãn"},  # insatiable
    "lex.en.100k.015713": {"vi": "dũng cảm gan dạ; không biết sợ hãi"},  # intrepid
    "lex.en.100k.015714": {"vi": "bị ngập lụt nước; tràn ngập tới tấp"},  # inundated
    "lex.en.100k.015716": {"vi": "món thịt nướng xiên que Kebab Thổ"},  # kebab
    "lex.en.100k.015717": {"vi": "bác sĩ Robert Koch; tập đoàn Koch"},  # koch
    "lex.en.100k.015718": {"vi": "thành phố cảng Lagos (Nigeria)"},  # lagos
    "lex.en.100k.015719": {"vi": "hệ thống mạng nội bộ LAN máy tính"},  # lan
    "lex.en.100k.015720": {"vi": "phòng rửa tay vệ sinh; buồng xí"},  # lavatory
    "lex.en.100k.015721": {"vi": "bên được cấp phép sử dụng quyền"},  # licensee
    "lex.en.100k.015722": {"vi": "bụng tụt trước sinh; sự nhẹ nhõm"},  # lightening
    "lex.en.100k.015723": {"vi": "theo đường tuyến tính; tỉ lệ thuận"},  # linearly
    "lex.en.100k.015725": {"vi": "thiết bị định vị; người khoanh vùng"},  # locator
    "lex.en.100k.015726": {"vi": "kẻ trung kiên; người trung thành"},  # loyalist
    "lex.en.100k.015727": {"ipa": "/ˌɛl ˈjuː/", "vi": "nguyên tố hóa học luteti (Lu)"},  # lu
    "lex.en.100k.015728": {"vi": "thuộc về phạm trù kinh tế vĩ mô"},  # macroeconomic
    "lex.en.100k.015729": {"vi": "ác tâm hiểm độc; chứa mã độc hại"},  # malicious
    "lex.en.100k.015730": {"vi": "cuộc truy lùng tội phạm ráo riết"},  # manhunt
    "lex.en.100k.015731": {"vi": "điệu đà kiểu cách; làm bộ giả tạo"},  # mannered
    "lex.en.100k.015732": {"vi": "tàn nhẫn không chút xót thương"},  # merciless
    "lex.en.100k.015733": {"vi": "phương pháp luận; hệ phương pháp"},  # methodology
    "lex.en.100k.015734": {"vi": "món sữa lắc kem hoa quả tươi ngon"},  # milkshake (purged crawler typo 'kem sưa')
    "lex.en.100k.015735": {"vi": "chỉ có một màu đơn sắc; đen trắng"},  # monochrome
    "lex.en.100k.015736": {"vi": "Jelly Roll Morton; muối Morton"},  # morton
    "lex.en.100k.015737": {"vi": "nhà xác bảo quản; thuộc tang lễ"},  # mortuary
    "lex.en.100k.015738": {"vi": "dân tộc chủ nghĩa cực đoan mù quáng"},  # nationalistic
    "lex.en.100k.015739": {"vi": "bác sĩ chuyên khoa thần kinh y học"},  # neurologist
    "lex.en.100k.015740": {"vi": "dòng sông Nin huyền thoại (Ai Cập)"},  # nile
    "lex.en.100k.015741": {"vi": "ngành sản phụ khoa sinh đẻ (y học)"},  # obstetrics
    "lex.en.100k.015742": {"vi": "tối quan trọng; tối cao hàng đầu"},  # paramount
    "lex.en.100k.015743": {"vi": "dạng hạt bụi mịn li ti lơ lửng"},  # particulate
    "lex.en.100k.015744": {"vi": "con chim trĩ gà lôi đuôi dài rực rỡ"},  # pheasant
    "lex.en.100k.015745": {"vi": "cây sáo nhỏ bổng piccolo (dàn nhạc)"},  # piccolo
    "lex.en.100k.015746": {"pos": "verb", "vi": "lao dốc thẳng đứng; sụt giảm mạnh"},  # plummet
    "lex.en.100k.015747": {"vi": "hình đa giác nhiều cạnh khép kín"},  # polygon
    "lex.en.100k.015748": {"vi": "loại trừ triệt tiêu khả năng xảy ra"},  # preclude
    "lex.en.100k.015749": {"vi": "đầy gai nhọn hoắt; khó tính dễ cáu"},  # prickly
    "lex.en.100k.015750": {"vi": "tu viện nhỏ tu viện trưởng cai quản"},  # priory
    "lex.en.100k.015752": {"vi": "lời đề xuất hợp tác; mệnh đề logic"},  # proposition
    "lex.en.100k.015753": {"vi": "mèo con dễ thương; con mèo nhỏ"},  # puss (purged vulgar crawler definition)
    "lex.en.100k.015754": {"vi": "sĩ quan quản lý quân nhu hậu cần"},  # quartermaster
    "lex.en.100k.015755": {"vi": "vẻ rạng rỡ sáng ngời; hào quang"},  # radiance
    "lex.en.100k.015756": {"ipa": "/ˌɑːr eɪ ˈɛf/", "vi": "Không quân Hoàng gia Anh (RAF)"},  # raf
    "lex.en.100k.015757": {"vi": "chủ nông trang nuôi gia súc bò ngựa"},  # rancher
    "lex.en.100k.015758": {"vi": "sự tương hỗ lẫn nhau; có đi có lại"},  # reciprocity
    "lex.en.100k.015759": {"vi": "bổ sung làm đầy lại; nạp thêm vào"},  # replenish (purged single-word 'bổ sung')
    "lex.en.100k.015761": {"vi": "rút lại lời nói; thụt móng vuốt lại"},  # retract
    "lex.en.100k.015762": {"vi": "thuộc bệnh viêm khớp dạng thấp"},  # rheumatoid
    "lex.en.100k.015763": {"vi": "khe nứt nẻ; sự rạn nứt bất hòa"},  # rift
    "lex.en.100k.015764": {"vi": "nước mặn biển khơi; sinh sống biển"},  # saltwater
    "lex.en.100k.015765": {"vi": "giàn giáo thi công; đoạn đầu đài"},  # scaffold
    "lex.en.100k.015767": {"vi": "hậu duệ danh giá; cành chồi ghép"},  # scion
    "lex.en.100k.015768": {"vi": "trò chơi ghép chữ Scrabble; cào bới"},  # scrabble
    "lex.en.100k.015769": {"vi": "trận tập luyện nội bộ; xô xát ẩu đả"},  # scrimmage
    "lex.en.100k.015770": {"vi": "dải duyên hải bờ biển ven đại dương"},  # seaboard
    "lex.en.100k.015772": {"vi": "vị trí tiền vệ chặn ngắn bóng chày"},  # shortstop
    "lex.en.100k.015773": {"vi": "ốm yếu quặt quẹo èo uột; nhợt nhạt"},  # sickly (purged single-word 'èo uột')
    "lex.en.100k.015774": {"vi": "môn thể thao bi-a snooker 21 bi màu"},  # snooker (purged single-word 'bi da')
    "lex.en.100k.015775": {"vi": "ôm ấp nép mình; rúc đầu vào lòng"},  # snuggle
    "lex.en.100k.015776": {"vi": "chuyên gia nghiên cứu xã hội học"},  # sociologist
    "lex.en.100k.015777": {"vi": "một cách trang nghiêm; thành kính"},  # solemnly
    "lex.en.100k.015778": {"vi": "cô độc lẻ loi; phòng giam biệt giam"},  # solitary
    "lex.en.100k.015779": {"vi": "thuộc về không gian ba chiều vị trí"},  # spatial (purged single-word 'không gian')
    "lex.en.100k.015781": {"vi": "mềm nhũn ươn ướt dễ bóp nén dẹt"},  # squishy
    "lex.en.100k.015782": {"vi": "thế cờ bế tắc; tình trạng ngõ cụt"},  # stalemate
    "lex.en.100k.015783": {"vi": "bốc mùi thối inh ỏi; tồi tệ tệ hại"},  # stinking
    "lex.en.100k.015784": {"vi": "cao to vạm vỡ; khỏe khoắn vạm vỡ"},  # strapping
    "lex.en.100k.015785": {"vi": "người livestream phát sóng; dải cờ"},  # streamer
    "lex.en.100k.015786": {"vi": "toa xe điện chạy trên đường ray phố"},  # streetcar (purged single-word 'xe điện')
    "lex.en.100k.015787": {"vi": "phóng viên tự do; xà dầm cầu dọc"},  # stringer
    "lex.en.100k.015788": {"vi": "một cách hời hợt; qua loa bên ngoài"},  # superficially
    "lex.en.100k.015790": {"vi": "vô cùng tột bậc; hết sức tối cao"},  # supremely (purged single-word 'cực kì')
    "lex.en.100k.015791": {"vi": "bị sưng phồng to; tự cao tự phụ"},  # swelled
    "lex.en.100k.015793": {"vi": "chiến thuật; mưu kế sách lược"},  # tactic
    "lex.en.100k.015794": {"vi": "đường băng sân bay; mặt đường nhựa"},  # tarmac
    "lex.en.100k.015795": {"vi": "đại lượng tenxơ (toán); cơ kéo căng"},  # tensor
    "lex.en.100k.015796": {"vi": "mã chứng khoán; máy điện báo giá"},  # ticker
    "lex.en.100k.015799": {"vi": "tiếng còi xe bim bim; hồi còi ngắn"},  # toot
    "lex.en.100k.015800": {"vi": "có hàm răng; mép viền khía răng cưa"},  # toothed

    # 801 - 900
    "lex.en.100k.015802": {"vi": "cành cây non nhỏ; chợt ngộ hiểu ra"},  # twig
    "lex.en.100k.015803": {"vi": "vết viêm loét dạ dày niêm mạc mô"},  # ulcer (purged single-word 'loét')
    "lex.en.100k.015804": {"vi": "một cách vô thức; trong tiềm thức"},  # unconsciously
    "lex.en.100k.015805": {"vi": "không ghi ngày tháng năm ban hành"},  # undated
    "lex.en.100k.015806": {"vi": "chưa được định nghĩa rõ ràng; mơ hồ"},  # undefined
    "lex.en.100k.015807": {"vi": "tận dụng tối đa hiệu quả; sử dụng"},  # utilize
    "lex.en.100k.015808": {"vi": "lòng tôn sùng thành kính; tôn kính"},  # veneration
    "lex.en.100k.015809": {"vi": "nguồn sinh lực dồi dào; nhiệt huyết"},  # verve
    "lex.en.100k.015810": {"vi": "bị biến thành nạn nhân; bị hãm hại"},  # victimized
    "lex.en.100k.015811": {"vi": "sinh lực dồi dào; sức mạnh bền bỉ"},  # vigor
    "lex.en.100k.015812": {"vi": "cái vẫy đuôi; người thích pha trò"},  # wag
    "lex.en.100k.015813": {"vi": "thợ đóng xe ngựa chở hàng thô sơ"},  # wainwright
    "lex.en.100k.015814": {"vi": "môn thể thao nâng cử tạ Olympic"},  # weightlifting
    "lex.en.100k.015815": {"vi": "hướng về phía tây; đi về hướng tây"},  # westbound
    "lex.en.100k.015817": {"vi": "máy tời dây cáp kéo vật nặng"},  # winch (purged single-word 'tời')
    "lex.en.100k.015819": {"vi": "mỉa mai chua chát; gượng gạo cười"},  # wry
    "lex.en.100k.015820": {"vi": "mở toang hoác sâu thẳm; há hốc mồm"},  # yawning
    "lex.en.100k.015821": {"vi": "cây thông đỏ độc yew; gỗ thủy tùng"},  # yew
    "lex.en.100k.015822": {"vi": "bò thịt Black Angus; thần Aengus"},  # angus
    "lex.en.100k.015823": {"ipa": "/ˌeɪ ˈviː/", "vi": "tháng Av Do Thái; nghe nhìn (A/V)"},  # av
    "lex.en.100k.015824": {"vi": "Phật giáo từ bi; đạo Phật giác ngộ"},  # buddhism
    "lex.en.100k.015825": {"vi": "nhà văn lừng danh Joseph Conrad"},  # conrad
    "lex.en.100k.015826": {"vi": "triết gia Ralph Waldo Emerson"},  # emerson
    "lex.en.100k.015827": {"vi": "người đi bẫy chim; từ điển Fowler"},  # fowler
    "lex.en.100k.015828": {"pos": "intj", "vi": "tiếng cảm thán Gee!; chữ cái G"},  # gee
    "lex.en.100k.015829": {"vi": "phong trào Hồi giáo Hamas"},  # hamas
    "lex.en.100k.015830": {"vi": "thủ phủ Helena; hoàng hậu Helena"},  # helena
    "lex.en.100k.015831": {"ipa": "/ˌaɪ ˈdʒiː/", "vi": "mạng Instagram (IG); kháng thể Ig"},  # ig
    "lex.en.100k.015832": {"vi": "thành phố cảng Naples cổ kính (Ý)"},  # naples
    "lex.en.100k.015833": {"vi": "vận động viên điền kinh Jesse Owens"},  # owens
    "lex.en.100k.015834": {"vi": "trên quy mô toàn tiểu bang rộng lớn"},  # statewide
    "lex.en.100k.015835": {"vi": "thành phố Sunderland (nước Anh)"},  # sunderland
    "lex.en.100k.015836": {"vi": "võ sĩ quyền anh thép Mike Tyson"},  # tyson
    "lex.en.100k.015837": {"ipa": "/ˌjuː ˈviː/", "vi": "bức xạ tia cực tím tử ngoại (UV)"},  # uv
    "lex.en.100k.015838": {"vi": "rượu mạnh mạch nha whisky hảo hạng"},  # whisky
    "lex.en.100k.015839": {"vi": "quốc gia Algérie rộng lớn (Bắc Phi)"},  # algeria
    "lex.en.100k.015840": {"vi": "tướng Robert Clive; họ Clive"},  # clive
    "lex.en.100k.015841": {"vi": "vi-rút xuất huyết Ebola nguy hiểm"},  # ebola
    "lex.en.100k.015842": {"vi": "hoàng hậu Esther (Kinh Thánh)"},  # esther
    "lex.en.100k.015843": {"vi": "trung tâm tài chính Frankfurt (Đức)"},  # frankfurt
    "lex.en.100k.015844": {"vi": "vua kèn clarinet jazz Benny Goodman"},  # goodman
    "lex.en.100k.015845": {"vi": "đất nước Guatemala (Trung Mỹ)"},  # guatemala
    "lex.en.100k.015846": {"vi": "thành phố cảng Hamburg (nước Đức)"},  # hamburg
    "lex.en.100k.015847": {"vi": "được dán tem nhãn; bị gắn mác"},  # labelled
    "lex.en.100k.015848": {"vi": "dòng sông Lena (vùng Siberia Nga)"},  # lena
    "lex.en.100k.015849": {"vi": "nữ thần mặt trăng Luna La Mã"},  # luna
    "lex.en.100k.015850": {"vi": "vua chúa Hồi giáo Malik; họ Malik"},  # malik
    "lex.en.100k.015851": {"ipa": "/ˌɛm ˈɛf/", "vi": "dải tần sóng trung MF vô tuyến"},  # mf
    "lex.en.100k.015852": {"ipa": "/ˈmɪdfiːld/", "vi": "khu vực trung tuyến giữa sân bóng"},  # midfield
    "lex.en.100k.015853": {"vi": "Đại Tiên tri Hồi giáo Mohammad"},  # mohammad
    "lex.en.100k.015854": {"ipa": "/ˌɑːr ˈoʊ/", "vi": "công nghệ lọc nước RO; tiếng Ro"},  # ro
    "lex.en.100k.015855": {"vi": "đồng cỏ xavan nhiệt đới hoang dã"},  # savannah
    "lex.en.100k.015856": {"ipa": "/ˌɛs ɛn ˈpiː/", "vi": "đa hình đơn nucleotide (SNP gen)"},  # snp
    "lex.en.100k.015857": {"ipa": "/ˈswɑnzi/", "vi": "thành phố cảng Swansea (xứ Wales)"},  # swansea
    "lex.en.100k.015858": {"vi": "thành phố Syracuse (bang New York)"},  # syracuse
    "lex.en.100k.015859": {"vi": "thủ đô Tehran sầm uất (nước Iran)"},  # tehran
    "lex.en.100k.015860": {"ipa": "/ˌtiː ˈɛm/", "vi": "nhãn hiệu đã đăng ký TM; thuli"},  # tm
    "lex.en.100k.015861": {"vi": "thành phố duyên hải Valencia (TBN)"},  # valencia
    "lex.en.100k.015862": {"ipa": "/ˈɔːθəraɪzd/", "vi": "được cơ quan cấp quyền chính thức"},  # authorised
    "lex.en.100k.015863": {"vi": "bang New Brunswick; thành Brunswick"},  # brunswick
    "lex.en.100k.015864": {"vi": "ông trùm thép Andrew Carnegie"},  # carnegie
    "lex.en.100k.015865": {"pos": "noun", "ipa": "/ˌsiː ˈviː/", "vi": "hồ sơ sơ yếu lý lịch xin việc (CV)"},  # cv
    "lex.en.100k.015866": {"vi": "đại thi hào nước Ý Dante Alighieri"},  # dante
    "lex.en.100k.015867": {"vi": "Thánh Dominic sáng lập dòng Đa Minh"},  # dominic
    "lex.en.100k.015868": {"vi": "quốc đảo Fiji (Thái Bình Dương)"},  # fiji
    "lex.en.100k.015869": {"vi": "thành phố Jacksonville (Florida)"},  # jacksonville
    "lex.en.100k.015870": {"vi": "thành phố Omaha; bộ tộc Omaha"},  # omaha
    "lex.en.100k.015871": {"vi": "hướng về phía trước; từ đó trở đi"},  # onwards
    "lex.en.100k.015872": {"vi": "thủ phủ Regina (Canada); nữ hoàng"},  # regina
    "lex.en.100k.015873": {"vi": "tỷ phú truyền thông Rupert Murdoch"},  # rupert
    "lex.en.100k.015874": {"ipa": "/ˌɛs ˈɛl/", "vi": "quốc gia Sierra Leone; cắt lỗ SL"},  # sl
    "lex.en.100k.015875": {"vi": "tầng nhà lầu; số tầng của tòa nhà"},  # storey (purged single-word 'tầng')
    "lex.en.100k.015876": {"vi": "dòng xe ô tô đa dụng gầm cao SUV"},  # suv
    "lex.en.100k.015877": {"ipa": "/ˌtiː ˈtiː/", "vi": "giải đua môtô TT; điện chuyển tiền"},  # tt
    "lex.en.100k.015878": {"vi": "giải quần vợt trên sân cỏ Wimbledon"},  # wimbledon
    "lex.en.100k.015879": {"vi": "cây keo lá tràm; chi thực vật keo"},  # acacia
    "lex.en.100k.015880": {"vi": "dính chặt vào bề mặt; tuân thủ luật"},  # adhere
    "lex.en.100k.015881": {"vi": "theo phái bất khả tri; hoài nghi"},  # agnostic
    "lex.en.100k.015882": {"vi": "căn chỉnh hàng ngũ; sự điều chỉnh"},  # aligning
    "lex.en.100k.015883": {"vi": "đầy sức quyến rũ mê hoặc; cám dỗ"},  # alluring
    "lex.en.100k.015884": {"vi": "phẫu thuật cắt bỏ đoạn chi cơ thể"},  # amputation
    "lex.en.100k.015885": {"vi": "môn thể thao câu cá bằng lưỡi câu"},  # angling (purged single-word 'câu cá')
    "lex.en.100k.015886": {"vi": "góc cạnh xương xẩu; tạo thành góc"},  # angular
    "lex.en.100k.015887": {"vi": "nhà phụ mở rộng; sáp nhập biên giới"},  # annex
    "lex.en.100k.015888": {"vi": "thù địch đối kháng; chống đối nhau"},  # antagonistic
    "lex.en.100k.015889": {"vi": "thuộc về Armenia; tiếng Armenia cổ"},  # armenian
    "lex.en.100k.015891": {"vi": "xúc xích chiên; ca khúc hit cực bốc"},  # banger
    "lex.en.100k.015892": {"vi": "đá núi lửa bazan đen sẫm cứng cáp"},  # basalt
    "lex.en.100k.015893": {"vi": "muộn màng trễ nải; lời chúc muộn"},  # belated
    "lex.en.100k.015894": {"ipa": "/bɛnˈɡɑːzi/", "vi": "thành phố cảng Benghazi (Libya)"},  # benghazi
    "lex.en.100k.015895": {"vi": "nổi cơn điên loạn; mất sạch tự chủ"},  # berserk
    "lex.en.100k.015896": {"vi": "sự cải thiện nâng cấp; sự tiến bộ"},  # betterment
    "lex.en.100k.015897": {"vi": "quyền bẩm sinh tự nhiên; thừa kế"},  # birthright
    "lex.en.100k.015898": {"vi": "đòn tấn công chớp nhoáng; oanh kích"},  # blitz
    "lex.en.100k.015899": {"vi": "thuộc họ bò tót; ngô nghê đờ đẫn"},  # bovine
    "lex.en.100k.015900": {"vi": "chữ nổi Braille cho người khiếm thị"},  # braille (purged single-word 'chữ nổi')

    # 901 - 1000
    "lex.en.100k.015901": {"vi": "khoảng nghỉ ngơi xả hơi chốc lát"},  # breather
    "lex.en.100k.015902": {"vi": "bờ vực thẳm; ranh giới hiểm nguy"},  # brink
    "lex.en.100k.015904": {"vi": "vùng lưu vực hứng nước sông ngòi"},  # catchment
    "lex.en.100k.015905": {"vi": "một cách dứt khoát; rành rẽ rõ ràng"},  # categorically
    "lex.en.100k.015906": {"vi": "cổ tử cung phụ nữ (giải phẫu học)"},  # cervix
    "lex.en.100k.015907": {"vi": "vui vẻ hoạt bát tươi cười hớn hở"},  # cheery
    "lex.en.100k.015908": {"vi": "phiếu ghi nợ nhỏ; cô nàng ranh mãnh"},  # chit
    "lex.en.100k.015909": {"vi": "mắc chứng sợ không gian hẹp tù túng"},  # claustrophobic
    "lex.en.100k.015910": {"vi": "răng cưa bánh răng; mắt xích nhỏ bé"},  # cog
    "lex.en.100k.015911": {"vi": "không có màu sắc; tẻ nhạt vô vị"},  # colorless
    "lex.en.100k.015912": {"vi": "sự đốt cháy nhiên liệu; bốc hỏa"},  # combustion
    "lex.en.100k.015913": {"vi": "có hình mặt cong lõm vào trong"},  # concave (purged single-word 'lõm')
    "lex.en.100k.015914": {"vi": "là hệ quả tất yếu kéo theo"},  # consequent
    "lex.en.100k.015915": {"vi": "hệ trọng có hậu quả lớn; vẻ tự đắc"},  # consequential
    "lex.en.100k.015916": {"vi": "thánh giá có tượng Chúa chịu nạn"},  # crucifix
    "lex.en.100k.015917": {"vi": "hạt gia vị thì là Ba Tư Ai Cập"},  # cumin
    "lex.en.100k.015918": {"vi": "giám tuyển nghệ thuật bảo tàng"},  # curator
    "lex.en.100k.015919": {"vi": "giải mã thông điệp ẩn giấu; dịch mã"},  # decode
    "lex.en.100k.015920": {"vi": "công việc chẩn đoán bệnh tật y khoa"},  # diagnosing
    "lex.en.100k.015921": {"vi": "người theo chế độ ăn kiêng giảm cân"},  # dieter
    "lex.en.100k.015922": {"vi": "tinh tường sáng suốt; có gu tinh tế"},  # discerning
    "lex.en.100k.015923": {"vi": "sự bất hòa mâu thuẫn; âm nghịch tai"},  # dissonance
    "lex.en.100k.015925": {"vi": "sự ép buộc bức bách; đe dọa vũ lực"},  # duress
    "lex.en.100k.015926": {"vi": "hội chứng khó đọc chữ (y học não)"},  # dyslexia
    "lex.en.100k.015927": {"vi": "mộc mạc bình dị chân quê; thô tục"},  # earthy
    "lex.en.100k.015928": {"vi": "lỗi lạc kiệt xuất; có địa vị cao"},  # eminent
    "lex.en.100k.015929": {"vi": "có hiệu lực bắt buộc thi hành luật"},  # enforceable
    "lex.en.100k.015930": {"vi": "mối thù hận sâu sắc; lòng thù địch"},  # enmity
    "lex.en.100k.015931": {"vi": "trạng thái cân bằng ổn định tâm lý"},  # equilibrium (purged single-word 'cân bằng')
    "lex.en.100k.015932": {"vi": "thời điểm xuân phân và thu phân"},  # equinox
    "lex.en.100k.015933": {"vi": "ấn phẩm nghệ thuật gợi dục lãng mạn"},  # erotica
    "lex.en.100k.015934": {"vi": "bài điếu văn ca ngợi người quá cố"},  # eulogy
    "lex.en.100k.015935": {"vi": "mặt trăng Europa; công chúa Europa"},  # europa
    "lex.en.100k.015936": {"vi": "đầy ắp sự kiện ly kỳ; nhiều biến cố"},  # eventful
    "lex.en.100k.015937": {"vi": "cuồng tín mù quáng; mê đắm cực đoan"},  # fanatical
    "lex.en.100k.015938": {"vi": "thành phố Fargo; bộ phim Fargo"},  # fargo
    "lex.en.100k.015939": {"vi": "được buộc cài chặt chẽ; đóng kín"},  # fastened
    "lex.en.100k.015940": {"vi": "con nai tơ non nớt; khúm núm bợ đỡ"},  # fawn
    "lex.en.100k.015941": {"vi": "thuộc về chất cặn bã phân (y học)"},  # fecal
    "lex.en.100k.015942": {"vi": "những mảnh vỡ vụn nát; dãy Flinders"},  # flinders
    "lex.en.100k.015943": {"vi": "tân sinh viên đại học năm thứ nhất"},  # fresher
    "lex.en.100k.015944": {"vi": "đường hoa quả tự nhiên Fructose"},  # fructose
    "lex.en.100k.015945": {"vi": "đồ đạc nội thất bài trí phòng ốc"},  # furnishing
    "lex.en.100k.015946": {"vi": "sự chỉnh trang nâng cấp đô thị cũ"},  # gentrification
    "lex.en.100k.015947": {"vi": "món bánh quy gừng nướng hình người"},  # gingerbread
    "lex.en.100k.015948": {"vi": "con cào cào nhảy; con châu chấu"},  # grasshopper
    "lex.en.100k.015949": {"vi": "thả rông gặm cỏ; vết trầy xước da"},  # graze
    "lex.en.100k.015950": {"vi": "người gieo trồng; nhà nông làm vườn"},  # grower
    "lex.en.100k.015951": {"vi": "dòng nhạc Grunge; bụi bặm bẩn thỉu"},  # grunge
    "lex.en.100k.015952": {"vi": "dũng sĩ Hercules sức mạnh vô song"},  # hercules
    "lex.en.100k.015953": {"vi": "một cách cực kỳ buồn cười nực cười"},  # hilariously
    "lex.en.100k.015954": {"vi": "quốc gia Honduras (vùng Trung Mỹ)"},  # honduras
    "lex.en.100k.015955": {"vi": "co cụm chen chúc co ro vì lạnh buốt"},  # huddled
    "lex.en.100k.015956": {"vi": "điệu múa lắc hông Hula của Hawaii"},  # hula
    "lex.en.100k.015957": {"vi": "hợp chất hữu cơ hiđrocacbon dầu mỏ"},  # hydrocarbon
    "lex.en.100k.015958": {"vi": "mang tính giả thiết; đặt giả định"},  # hypothetical
    "lex.en.100k.015959": {"vi": "hành vi mạo danh; sự giả dạng"},  # impersonation
    "lex.en.100k.015960": {"vi": "tùy cơ ứng biến; ngẫu hứng sáng tác"},  # improvise
    "lex.en.100k.015961": {"vi": "chứa chứng cứ buộc tội; tố cáo tội"},  # incriminating
    "lex.en.100k.015962": {"vi": "xui khiến kích động; gây chuyển dạ"},  # induce
    "lex.en.100k.015963": {"vi": "khoa học tin học; thông tin học số"},  # informatics (purged single-word 'tin học')
    "lex.en.100k.015964": {"vi": "nhiều vô số kể; nhiều không đếm xuể"},  # innumerable
    "lex.en.100k.015965": {"vi": "không thể vượt qua; nan giải"},  # insurmountable
    "lex.en.100k.015966": {"vi": "tính bất biến; không hề đổi thay"},  # invariant
    "lex.en.100k.015968": {"vi": "nhà tiên tri Isaiah (Kinh Thánh)"},  # isaiah
    "lex.en.100k.015969": {"vi": "vụ trốn ngục; bẻ khóa phần mềm iOS"},  # jailbreak
    "lex.en.100k.015970": {"vi": "cú lắc nảy mạnh; cú sốc bàng hoàng"},  # jolt
    "lex.en.100k.015971": {"vi": "trò tung hứng xảo thuật; sự xoay xở"},  # juggle
    "lex.en.100k.015972": {"vi": "máy phát nhạc tự động nhét tiền xu"},  # jukebox
    "lex.en.100k.015973": {"vi": "bộ trang phục áo liền quần jumpsuit"},  # jumpsuit
    "lex.en.100k.015975": {"vi": "nhà hóa học Kendall; Kendall Jenner"},  # kendall
    "lex.en.100k.015976": {"vi": "hạt Lancashire (Tây Bắc nước Anh)"},  # lancashire
    "lex.en.100k.015977": {"vi": "việc dùng đòn bẩy; tận dụng lợi thế"},  # leveraging
    "lex.en.100k.015978": {"vi": "màu đỏ cánh sen rực rỡ (magenta)"},  # magenta
    "lex.en.100k.015979": {"vi": "nhà lãnh đạo Mao Trạch Đông"},  # mao
    "lex.en.100k.015980": {"vi": "theo chủ nghĩa Mác; người Mác-xít"},  # marxist
    "lex.en.100k.015981": {"vi": "mối đe dọa nguy hiểm; kẻ quấy rối"},  # menace
    "lex.en.100k.015982": {"vi": "sự biến thái hình thể; sự lột xác"},  # metamorphosis
    "lex.en.100k.015983": {"vi": "hạng cân trung bình (võ đài boxing)"},  # middleweight (purged single-word 'hạng trung')
    "lex.en.100k.015984": {"vi": "thịt băm xay nhuyễn; nói năng ỡm ờ"},  # mince
    "lex.en.100k.015985": {"vi": "hiện đại hóa quy trình; đổi mới"},  # modernize
    "lex.en.100k.015986": {"vi": "chữ lồng nghệ thuật; ký hiệu lồng"},  # monogram
    "lex.en.100k.015987": {"vi": "loài cá chình biển Moray hung dữ"},  # moray
    "lex.en.100k.015988": {"vi": "nói được nhiều thứ tiếng; đa ngữ"},  # multilingual
    "lex.en.100k.015989": {"vi": "mang tính thần thoại; huyền bí"},  # mythic
    "lex.en.100k.015990": {"vi": "bánh ngô chiên giòn Nachos (Mexico)"},  # nacho
    "lex.en.100k.015991": {"vi": "ngủ quên mất cảnh giác; chợp mắt"},  # napping
    "lex.en.100k.015992": {"vi": "võ sĩ Chuck Norris; họ Norris"},  # norris
    "lex.en.100k.015993": {"vi": "nỗi nhớ nhung da diết; sự hoài niệm"},  # nostalgia
    "lex.en.100k.015994": {"vi": "thuộc về khứu giác; cảm giác ngửi"},  # olfactory
    "lex.en.100k.015996": {"vi": "John Osborne; máy tính Osborne"},  # osborne
    "lex.en.100k.015998": {"vi": "lãnh chúa tối cao; chúa tể áp bức"},  # overlord
    "lex.en.100k.015999": {"vi": "sự lạm dụng quá đà; sử dụng quá tải"},  # overuse
    "lex.en.100k.016000": {"vi": "trò chơi bắn súng sơn; viên đạn sơn"},  # paintball
}

# Verify lengths <= 35
for k, v in OVERRIDES_B04_R02.items():
    if "vi" in v:
        assert len(v["vi"]) <= 35, f"Length > 35 for {k}: {v['vi']} ({len(v['vi'])})"

with open('content/english/qa-batches/batch-04.json', 'r', encoding='utf-8') as f:
    batch_data = json.load(f)

# Apply overrides to records in range 500 to 1000
count = 0
for idx in range(500, 1000):
    rec = batch_data['records'][idx]
    rid = rec['id']
    if rid in OVERRIDES_B04_R02:
        count += 1
        for field, val in OVERRIDES_B04_R02[rid].items():
            rec[field] = val
        rec['status'] = 'reviewed'

batch_data['reviewedCount'] = 1000

with open('content/english/qa-batches/batch-04.json', 'w', encoding='utf-8') as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully applied Batch 04 Round 2 ({count} overrides). Reviewed: {batch_data['reviewedCount']}/5000.")
