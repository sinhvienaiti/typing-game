import json

# Cognitive manual QA overrides for Batch 03 Round 09 (records 4000 to 4500, STT 4001 to 4500)
OVERRIDES_B03_R09 = {
    # 4001 - 4100
    "lex.en.100k.014002": {"vi": "món đậu dahl Ấn Độ; đậu lăng dahl"},  # dahl
    "lex.en.100k.014003": {"vi": "chim quạ gáy xám; chim quạ nhỏ"},  # daw
    "lex.en.100k.014007": {"vi": "phạm pháp; chậm thanh toán nợ"},  # delinquent
    "lex.en.100k.014009": {"vi": "chất khử mùi; lăn khử mùi cơ thể"},  # deodorant (purged 'bay mùi')
    "lex.en.100k.014010": {"vi": "rau thì là; cây thì là gia vị"},  # dill (purged single-word 'thì là')
    "lex.en.100k.014011": {"vi": "ngừng sản xuất; đình chỉ; ngưng"},  # discontinue (purged slang 'khai tử')
    "lex.en.100k.014015": {"vi": "sự thất vọng; sự bàng hoàng"},  # dismay
    "lex.en.100k.014016": {"vi": "chứng chóng mặt; sự hoa mắt"},  # dizziness (purged single-word 'chóng mặt')
    "lex.en.100k.014019": {"vi": "quý ông; tước hiệu kính cẩn (Esq.)"},  # esquire
    "lex.en.100k.014020": {"vi": "hạt Essex (nước Anh)"},  # essex
    "lex.en.100k.014026": {"vi": "một cách dữ dội; mãnh liệt"},  # fiercely
    "lex.en.100k.014027": {"vi": "sự phân hạch; phân chia tế bào"},  # fission
    "lex.en.100k.014029": {"vi": "tâng bốc; nịnh nọt; khen ngợi"},  # flatter
    "lex.en.100k.014030": {"vi": "cơn gió tuyết; sự náo động bất ngờ"},  # flurry
    "lex.en.100k.014033": {"vi": "bị tước bỏ; bị tịch thu; mất quyền"},  # forfeit
    "lex.en.100k.014034": {"vi": "đồng phrăng; đồng franc Pháp"},  # franc
    "lex.en.100k.014037": {"vi": "thiên thần Gabriel (Kinh Thánh)"},  # gabriel
    "lex.en.100k.014039": {"vi": "Dải Gaza; vùng lãnh thổ Gaza"},  # gaza
    "lex.en.100k.014042": {"vi": "kẻ ngốc nghếch; tên tay sai côn đồ"},  # goon
    "lex.en.100k.014043": {"vi": "người sành ăn uống; món ăn cao cấp"},  # gourmet
    "lex.en.100k.014047": {"vi": "nơi lui tới quen thuộc; chốn tụ tập"},  # hangout
    "lex.en.100k.014049": {"vi": "héc-ta (đơn vị đo diện tích)"},  # hectare
    "lex.en.100k.014050": {"vi": "dấu hôn cổ (hickey); vết cắn yêu"},  # hickey
    "lex.en.100k.014051": {"vi": "mã định danh; phần tử nhận diện"},  # identifier
    "lex.en.100k.014052": {"vi": "nghèo khó bần cùng; kiệt quệ"},  # impoverished
    "lex.en.100k.014053": {"vi": "đã công nghiệp hóa; phát triển"},  # industrialized
    "lex.en.100k.014054": {"vi": "một cách thân mật; không nghi thức"},  # informally
    "lex.en.100k.014057": {"vi": "thành thể chế; đưa vào trại/viện"},  # institutionalized
    "lex.en.100k.014058": {"vi": "sự say sưa; tình trạng say chất cồn"},  # intoxication
    "lex.en.100k.014059": {"vi": "hóa đơn thanh toán; bản kê chi phí"},  # invoice
    "lex.en.100k.014060": {"vi": "nước Jamaica (vùng biển Caribe)"},  # jamaica
    "lex.en.100k.014061": {"vi": "nhân vật Joshua (Kinh Thánh)"},  # joshua
    "lex.en.100k.014062": {"vi": "lò nung gốm sứ; lò sấy gạch"},  # kiln (purged single-word 'lò')
    "lex.en.100k.014063": {"vi": "tiềm ẩn; tiềm tàng; âm ỉ ngầm"},  # latent
    "lex.en.100k.014064": {"vi": "thành phố León (Tây Ban Nha)"},  # leon
    "lex.en.100k.014065": {"pos": "noun", "vi": "cây hoa tử đinh hương; màu hoa cà"},  # lilac
    "lex.en.100k.014066": {"vi": "Joseph Lister; máy cày luống"},  # lister
    "lex.en.100k.014067": {"vi": "cực kỳ căm ghét; ghê tởm sâu sắc"},  # loathe
    "lex.en.100k.014071": {"vi": "nữ hộ sinh; bà đỡ đẻ chuyên môn"},  # midwife
    "lex.en.100k.014072": {"vi": "vô cùng quan trọng; trọng đại"},  # momentous
    "lex.en.100k.014073": {"vi": "thành phố Montgomery; họ Montgomery"},  # montgomery
    "lex.en.100k.014075": {"vi": "người phát ngôn; cơ quan ngôn luận"},  # mouthpiece
    "lex.en.100k.014076": {"vi": "cẩu thả thiếu trách nhiệm; bất cẩn"},  # negligent
    "lex.en.100k.014077": {"vi": "thuộc về trẻ sơ sinh; sơ sinh"},  # neonatal
    "lex.en.100k.014078": {"vi": "thuộc nơ-ron; thuộc hệ thần kinh"},  # neuronal
    "lex.en.100k.014079": {"vi": "vô hiệu hóa; trung hòa; triệt tiêu"},  # neutralize
    "lex.en.100k.014080": {"vi": "rạp chiếu phim mini giá rẻ xưa"},  # nickelodeon
    "lex.en.100k.014081": {"vi": "công chứng viên; người công chứng"},  # notary
    "lex.en.100k.014082": {"vi": "thành phố Oakland (California)"},  # oakland
    "lex.en.100k.014083": {"vi": "dùng để trang trí; làm cảnh đẹp"},  # ornamental
    "lex.en.100k.014085": {"vi": "quá đắt đỏ; định giá quá cao"},  # overpriced
    "lex.en.100k.014086": {"vi": "bãi quây ngựa; bãi tập ngựa đua"},  # paddock
    "lex.en.100k.014087": {"vi": "tuyên úy quân đội; linh mục (cha)"},  # padre
    "lex.en.100k.014090": {"vi": "khoa sư phạm; phương pháp giáo dục"},  # pedagogy
    "lex.en.100k.014091": {"vi": "thích hợp; liên quan trực tiếp"},  # pertinent
    "lex.en.100k.014092": {"vi": "vóc dáng; thể chất; thể hình cơ thể"},  # physique
    "lex.en.100k.014094": {"vi": "chạy bằng khí nén; chứa khí nén"},  # pneumatic
    "lex.en.100k.014095": {"vi": "thuộc chương trình sau tiến sĩ"},  # postdoctoral
    "lex.en.100k.014096": {"vi": "tự xưng; công khai thừa nhận"},  # professed
    "lex.en.100k.014097": {"vi": "tính chuyên nghiệp; sự thành thạo"},  # professionalism
    "lex.en.100k.014098": {"vi": "chó sục mặt xệ Pug; giống chó Pug"},  # pug
    "lex.en.100k.014100": {"vi": "bộ tản nhiệt làm mát; lò sưởi ấm"},  # radiator

    # 4101 - 4200
    "lex.en.100k.014101": {"vi": "dễ đọc; văn phong rõ ràng mạch lạc"},  # readable
    "lex.en.100k.014102": {"vi": "lượng độc giả; tập hợp bạn đọc"},  # readership
    "lex.en.100k.014103": {"vi": "trấn an; cam đoan; làm an lòng"},  # reassure
    "lex.en.100k.014104": {"vi": "công nhận; nhận ra; ghi nhận"},  # recognise
    "lex.en.100k.014107": {"vi": "phí duy trì dịch vụ; người hầu cận"},  # retainer
    "lex.en.100k.014108": {"vi": "cuộc vui chơi say sưa; hội hè hả hê"},  # revel
    "lex.en.100k.014109": {"vi": "người La Mã; Thư gửi tín hữu Rôma"},  # romans
    "lex.en.100k.014110": {"vi": "cuộc vây bắt; bài tổng hợp tin tức"},  # roundup
    "lex.en.100k.014112": {"vi": "vết lằn bánh xe; thói quen lối mòn"},  # rut
    "lex.en.100k.014113": {"vi": "lời chào hòa bình sa-lam (Ả Rập)"},  # salaam
    "lex.en.100k.014114": {"vi": "nổi bật nhất; quan trọng trọng tâm"},  # salient
    "lex.en.100k.014115": {"vi": "phòng xông hơi khô; nhà tắm sauna"},  # sauna
    "lex.en.100k.014116": {"vi": "thuộc về sơ đồ; giản đồ kỹ thuật"},  # schematic
    "lex.en.100k.014117": {"vi": "mắc bệnh tâm thần phân liệt"},  # schizophrenic
    "lex.en.100k.014119": {"vi": "ly khai; mang tính chất ly khai"},  # separatist
    "lex.en.100k.014122": {"vi": "hình bóng đen; bóng hình ngược sáng"},  # silhouette (purged single-word 'bóng')
    "lex.en.100k.014123": {"vi": "môn trượt tuyết lượn qua cọc tiêu"},  # slalom
    "lex.en.100k.014124": {"vi": "tự mãn; tự đắc; vênh váo"},  # smug
    "lex.en.100k.014125": {"vi": "buôn lậu; vận chuyển trái phép"},  # smuggle
    "lex.en.100k.014126": {"vi": "chất hàn; vảy hàn; thiếc hàn chì"},  # solder
    "lex.en.100k.014127": {"vi": "một cách tự phát; tự ý tự nhiên"},  # spontaneously
    "lex.en.100k.014128": {"vi": "sạch không tì vết; tinh tươm sạch"},  # spotless
    "lex.en.100k.014129": {"vi": "vòi rót nước; vòi phun nước"},  # spout
    "lex.en.100k.014130": {"vi": "có tính ổn định; mang tính giữ vững"},  # stabilizing
    "lex.en.100k.014132": {"vi": "hôi thối; bốc mùi nồng nặc"},  # stinky
    "lex.en.100k.014133": {"vi": "đường may mũi chỉ; vết khâu may"},  # stitching
    "lex.en.100k.014134": {"vi": "rất vất vả; đòi hỏi nhiều sức lực"},  # strenuous
    "lex.en.100k.014135": {"vi": "một cách nổi bật; rất ấn tượng"},  # strikingly
    "lex.en.100k.014137": {"vi": "làm hoen ố danh dự; bôi bẩn ô nhục"},  # sully
    "lex.en.100k.014138": {"vi": "khoản phụ phí; tiền thu thêm"},  # surcharge
    "lex.en.100k.014139": {"vi": "thành phố Tampa (bang Florida)"},  # tampa
    "lex.en.100k.014140": {"vi": "bộ bài tarot (bói toán)"},  # tarot
    "lex.en.100k.014141": {"vi": "tính khí; khí chất tự nhiên"},  # temperament
    "lex.en.100k.014143": {"vi": "rụt rè; nhút nhát thiếu tự tin"},  # timid
    "lex.en.100k.014144": {"vi": "thợ hàn vá dạo; người táy máy sửa"},  # tinker
    "lex.en.100k.014145": {"vi": "người đứng đầu; mũ chóp cao nam"},  # topper
    "lex.en.100k.014147": {"vi": "độ bền dẻo dai; sức chịu đựng cao"},  # toughness
    "lex.en.100k.014148": {"vi": "độc chất học; môn học về chất độc"},  # toxicology
    "lex.en.100k.014149": {"vi": "được trân quý; quý báu nâng niu"},  # treasured
    "lex.en.100k.014150": {"vi": "kim loại vonfam (tungsten)"},  # tungsten
    "lex.en.100k.014153": {"vi": "sự đồng thanh; sự hòa hợp đồng điệu"},  # unison
    "lex.en.100k.014154": {"vi": "không người lái; vận hành tự động"},  # unmanned
    "lex.en.100k.014156": {"vi": "không đúng lúc; quá sớm yểu mệnh"},  # untimely
    "lex.en.100k.014157": {"vi": "cây phới đánh trứng; cái đánh trứng"},  # whisk
    "lex.en.100k.014158": {"vi": "mơ tưởng viển vông; khao khát"},  # wishful
    "lex.en.100k.014160": {"vi": "cờ lê vặn ốc; cú giật vặn mạnh"},  # wrench
    "lex.en.100k.014161": {"vi": "nếp nhăn da; nếp gấp vải quần áo"},  # wrinkle
    "lex.en.100k.014162": {"vi": "Rachel Carson; họ Carson"},  # carson
    "lex.en.100k.014163": {"vi": "danh mục sản phẩm; mục lục tài liệu"},  # catalogue
    "lex.en.100k.014164": {"ipa": "/ˌdʒiː ˈbiː/", "vi": "chất độc thần kinh sarin; gigabyte"},  # gb
    "lex.en.100k.014165": {"vi": "tiếng Hê-brơ; người Hê-brơ Do Thái"},  # hebrew
    "lex.en.100k.014166": {"vi": "nước Hungary; Cộng hòa Hungary"},  # hungary
    "lex.en.100k.014167": {"vi": "bang Idaho (Hoa Kỳ)"},  # idaho
    "lex.en.100k.014168": {"vi": "tổng thống Mỹ Richard Nixon"},  # nixon
    "lex.en.100k.014169": {"vi": "nhà phê bình I. A. Richards"},  # richards
    "lex.en.100k.014170": {"vi": "thành phố Sheffield (nước Anh)"},  # sheffield
    "lex.en.100k.014171": {"vi": "thành phố cổ Ur (Lưỡng Hà)"},  # ur
    "lex.en.100k.014172": {"vi": "phi hành gia Neil Armstrong"},  # armstrong
    "lex.en.100k.014173": {"vi": "nước Bungari; nước Bulgaria"},  # bulgaria
    "lex.en.100k.014174": {"ipa": "/ˌsiː ˈɛs/", "vi": "nguyên tố xê-si (Cs); hơi cay CS"},  # cs
    "lex.en.100k.014175": {"vi": "bang Delaware; dòng sông Delaware"},  # delaware
    "lex.en.100k.014177": {"ipa": "/ˌɛf ˈiː/", "vi": "nguyên tố sắt (Fe); ký hiệu sắt"},  # fe
    "lex.en.100k.014178": {"vi": "nước Ghana (Tây Phi)"},  # ghana
    "lex.en.100k.014179": {"vi": "đàn guitar Gibson; Charles Gibson"},  # gibson
    "lex.en.100k.014180": {"ipa": "/ˌɛn ˈdʒiː/", "vi": "nanogam (ng); đơn vị đo khối lượng"},  # ng
    "lex.en.100k.014181": {"vi": "William Penn; Đại học Penn"},  # penn
    "lex.en.100k.014182": {"ipa": "/ˌɑːr ˈeɪ/", "vi": "nguyên tố phóng xạ rađi (Ra)"},  # ra
    "lex.en.100k.014183": {"vi": "nhà thơ James Whitcomb Riley"},  # riley
    "lex.en.100k.014184": {"vi": "nước Cộng hòa Sudan (Châu Phi)"},  # sudan
    "lex.en.100k.014185": {"vi": "đảng viên Đảng Bảo thủ (Anh)"},  # tory
    "lex.en.100k.014186": {"vi": "Thượng đế Allah (Hồi giáo)"},  # allah
    "lex.en.100k.014187": {"ipa": "/ˌbiː ˈɑːr/", "vi": "nguyên tố brôm (Br); thẻ ngắt dòng"},  # br
    "lex.en.100k.014188": {"vi": "Đại học Johns Hopkins; họ Hopkins"},  # hopkins
    "lex.en.100k.014189": {"vi": "thuộc về Indonesia; tiếng Indonesia"},  # indonesian
    "lex.en.100k.014191": {"vi": "tổ chức khủng bố Jemaah Islamiyah"},  # ji
    "lex.en.100k.014192": {"vi": "thành phố Memphis (Tennessee)"},  # memphis
    "lex.en.100k.014193": {"vi": "minh tinh Marilyn Monroe"},  # monroe
    "lex.en.100k.014194": {"ipa": "/ˌɛm viː ˈpiː/", "vi": "cầu thủ xuất sắc nhất; sản phẩm MVP"},  # mvp
    "lex.en.100k.014195": {"vi": "nước Cộng hòa Peru (Nam Mỹ)"},  # peru
    "lex.en.100k.014196": {"vi": "tướng Colin Powell; họ Powell"},  # powell
    "lex.en.100k.014197": {"vi": "vua; quốc vương (tiếng La-tinh)"},  # rex
    "lex.en.100k.014198": {"vi": "Tổng thống Franklin D. Roosevelt"},  # roosevelt
    "lex.en.100k.014199": {"ipa": "/ˌɛs ˈdiː/", "vi": "bang Nam Dakota; thẻ nhớ SD chuẩn"},  # sd
    "lex.en.100k.014200": {"pos": "num", "vi": "số 13; mười ba"},  # thirteen

    # 4201 - 4300
    "lex.en.100k.014202": {"vi": "nghề kế toán; ngành kế toán"},  # accountancy
    "lex.en.100k.014203": {"vi": "sự công nhận; lời cảm ơn cảm tạ"},  # acknowledgment
    "lex.en.100k.014204": {"vi": "thực tế hiện hữu; tính chân thực"},  # actuality
    "lex.en.100k.014205": {"vi": "sự ngưỡng mộ; sự sùng kính tôn thờ"},  # adoration
    "lex.en.100k.014206": {"vi": "đối thủ; địch thủ; kẻ đối địch"},  # adversary
    "lex.en.100k.014207": {"vi": "ngành hàng không; khí động lực học"},  # aeronautics
    "lex.en.100k.014208": {"vi": "bằng chứng ngoại phạm (luật)"},  # alibi
    "lex.en.100k.014209": {"vi": "lời chào hỏi thân ái (tiếng Hawaii)"},  # aloha
    "lex.en.100k.014210": {"vi": "nữ diễn viên múa ba lê"},  # ballerina
    "lex.en.100k.014211": {"vi": "ban nhạc huyền thoại The Beatles"},  # beatles
    "lex.en.100k.014212": {"vi": "thành phố Belfast (Bắc Ireland)"},  # belfast
    "lex.en.100k.014213": {"vi": "hoang mang bối rối; ngơ ngác"},  # bewildered
    "lex.en.100k.014214": {"vi": "ống nhòm hai mắt cầm tay"},  # binoculars (purged absurd 'con mắt xa')
    "lex.en.100k.014215": {"vi": "điên rồ; mất trí; khùng khùng"},  # bonkers
    "lex.en.100k.014216": {"vi": "trơ trẽn trơ tráo; vô liêm sỉ"},  # brazen
    "lex.en.100k.014217": {"vi": "sủi bọt tăm; vui vẻ sôi nổi"},  # bubbly
    "lex.en.100k.014218": {"vi": "hài kịch châm biếm; diễn tạp kỹ"},  # burlesque
    "lex.en.100k.014219": {"vi": "hang hốc của thú; đào bới hang"},  # burrow
    "lex.en.100k.014221": {"vi": "lửa trại bập bùng; đóng trại"},  # campfire
    "lex.en.100k.014223": {"vi": "mối quan hệ nhân quả; sự gây ra"},  # causation
    "lex.en.100k.014224": {"vi": "vật trung tâm trang trí; tâm điểm"},  # centerpiece
    "lex.en.100k.014225": {"vi": "sự đình chỉ; sự chấm dứt hoàn toàn"},  # cessation
    "lex.en.100k.014226": {"vi": "con tắc kè hoa; người dễ đổi thay"},  # chameleon
    "lex.en.100k.014227": {"vi": "trò chơi cờ đam (checkers)"},  # checkers
    "lex.en.100k.014228": {"vi": "ghế sofa bọc da Chesterfield"},  # chesterfield
    "lex.en.100k.014229": {"vi": "sự bừa bộn; đồ đạc lộn xộn"},  # clutter
    "lex.en.100k.014231": {"vi": "mang tính che giấu; giấu giếm"},  # concealing
    "lex.en.100k.014232": {"vi": "bản hòa tấu công-xéc-tô (âm nhạc)"},  # concerto
    "lex.en.100k.014233": {"vi": "căn hộ chung cư cao cấp (condo)"},  # condominium
    "lex.en.100k.014234": {"vi": "có hình nón; hình chóp nón"},  # conical
    "lex.en.100k.014235": {"vi": "nhạc viện; nhà kính trồng cây"},  # conservatory
    "lex.en.100k.014236": {"vi": "sự hạn chế ràng buộc; sự gò bó"},  # constraint
    "lex.en.100k.014237": {"vi": "có tác dụng tránh thai; ngừa thai"},  # contraceptive
    "lex.en.100k.014238": {"vi": "tính đàm thoại; khẩu ngữ đối thoại"},  # conversational
    "lex.en.100k.014239": {"vi": "dồi dào phong phú; thừa thãi"},  # copious
    "lex.en.100k.014240": {"vi": "thân ái chân thành; nồng hậu"},  # cordial
    "lex.en.100k.014241": {"vi": "thủ pháp đối âm; tính tương phản"},  # counterpoint
    "lex.en.100k.014243": {"vi": "chủ nợ; bên cho vay (tài chính)"},  # creditor
    "lex.en.100k.014244": {"vi": "vỡ vụn từng mảnh; sụp đổ tiêu tan"},  # crumble
    "lex.en.100k.014245": {"vi": "hầm mộ dưới thánh đường; hầm mộ"},  # crypt
    "lex.en.100k.014246": {"vi": "thuộc quyền giám hộ; lau dọn bảo vệ"},  # custodial
    "lex.en.100k.014247": {"vi": "sự lừa dối; mánh khóe gian trá"},  # deceit
    "lex.en.100k.014248": {"vi": "được ban hành sắc lệnh; quy định"},  # decreed
    "lex.en.100k.014249": {"vi": "sự thiệt hại tổn hao; bất lợi"},  # detriment
    "lex.en.100k.014250": {"vi": "bất mãn bực dọc; cáu kỉnh"},  # disgruntled
    "lex.en.100k.014252": {"ipa": "/ˌdiː ˈɛm/", "vi": "tin nhắn trực tiếp (DM); đề-xi-mét"},  # dm
    "lex.en.100k.014253": {"vi": "trong nước; về mặt nội địa"},  # domestically
    "lex.en.100k.014255": {"vi": "sắc lệnh ban bố; chỉ dụ hoàng gia"},  # edict
    "lex.en.100k.014256": {"vi": "cực kỳ tồi tệ; trắng trợn thái quá"},  # egregious
    "lex.en.100k.014257": {"vi": "gợi ra thông tin; khơi gợi phản ứng"},  # elicit
    "lex.en.100k.014258": {"vi": "nhà truyền bá Phúc âm; người cổ vũ"},  # evangelist
    "lex.en.100k.014259": {"vi": "mang tính giải thích; thuyết minh"},  # explanatory
    "lex.en.100k.014260": {"vi": "tội tống tiền; hành vi cưỡng đoạt"},  # extortion
    "lex.en.100k.014261": {"vi": "nhãn cầu; quả cầu mắt"},  # eyeball
    "lex.en.100k.014262": {"vi": "cuồng tín cực đoan; say mê quá mức"},  # fanatic
    "lex.en.100k.014263": {"vi": "tường lửa mạng (an ninh mạng)"},  # firewall
    "lex.en.100k.014264": {"vi": "bình giữ nhiệt; bình thót cổ"},  # flask
    "lex.en.100k.014265": {"vi": "non nớt mới nổi; mới vào nghề"},  # fledgling
    "lex.en.100k.014266": {"vi": "mỏng mảnh manh manh; ọp ẹp tạm bợ"},  # flimsy
    "lex.en.100k.014267": {"vi": "chìa khóa thông minh (fob); mặt dây"},  # fob
    "lex.en.100k.014268": {"vi": "chân trang văn bản; người đi bộ"},  # footer
    "lex.en.100k.014269": {"pos": "num", "vi": "số 14; mười bốn"},  # fourteen
    "lex.en.100k.014270": {"vi": "lạnh buốt giá; phủ sương tuyết"},  # frosty
    "lex.en.100k.014271": {"vi": "sáng loáng lấp lánh; lóng lánh"},  # gleaming
    "lex.en.100k.014272": {"ipa": "/ˌdʒiː ˈpiː/", "vi": "bác sĩ đa khoa gia đình (GP)"},  # gp
    "lex.en.100k.014274": {"vi": "kinh hoàng rùng rợn; ghê rợn"},  # gruesome
    "lex.en.100k.014275": {"vi": "nhẹ dạ cả tin; dễ bị lừa gạt"},  # gullible
    "lex.en.100k.014276": {"vi": "cơn gió giật mạnh; đợt bộc phát"},  # gust
    "lex.en.100k.014277": {"vi": "quả táo gai; tiếng ngập ngừng 'hơ'"},  # haw
    "lex.en.100k.014278": {"vi": "nền lò sưởi; không gian bếp ấm cúng"},  # hearth
    "lex.en.100k.014279": {"vi": "ngoại đạo; man di mọi rợ"},  # heathen
    "lex.en.100k.014280": {"vi": "con nhím gai (hedgehog)"},  # hedgehog
    "lex.en.100k.014281": {"vi": "sự xuất huyết; chảy máu ồ ạt"},  # hemorrhage
    "lex.en.100k.014283": {"vi": "tích trữ quá mức; biển quảng cáo"},  # hoarding
    "lex.en.100k.014284": {"vi": "ảnh nổi ba chiều; hình ảnh toàn ký"},  # hologram
    "lex.en.100k.014285": {"vi": "loài người; toàn thể nhân loại"},  # humankind
    "lex.en.100k.014286": {"vi": "người máy có hình người; dạng người"},  # humanoid
    "lex.en.100k.014287": {"vi": "thuộc về thủy điện; dùng sức nước"},  # hydroelectric
    "lex.en.100k.014289": {"vi": "chủ nghĩa lý tưởng; thuyết duy tâm"},  # idealism
    "lex.en.100k.014290": {"vi": "ngành miễn dịch học (y học)"},  # immunology
    "lex.en.100k.014291": {"vi": "tiểu quỷ; đứa trẻ tinh nghịch"},  # imp
    "lex.en.100k.014292": {"vi": "luận tội quan chức; truất phế"},  # impeach
    "lex.en.100k.014293": {"vi": "sự nuông chiều; sự thỏa mãn đam mê"},  # indulging
    "lex.en.100k.014294": {"vi": "bị ức chế tâm lý; rụt rè e dè"},  # inhibited
    "lex.en.100k.014297": {"vi": "bờ hồ; ven hồ nước"},  # lakeside
    "lex.en.100k.014298": {"vi": "chủ sở hữu đất đai; địa chủ"},  # landowner
    "lex.en.100k.014300": {"vi": "vốn từ vựng; bộ thuật ngữ từ điển"},  # lexicon

    # 4301 - 4400
    "lex.en.100k.014301": {"vi": "tâm điểm chú ý; ánh đèn sân khấu"},  # limelight
    "lex.en.100k.014302": {"vi": "vô hạn; vô biên; không giới hạn"},  # limitless (purged single-word 'vô bờ')
    "lex.en.100k.014304": {"pos": "noun", "vi": "đồng phục hầu cận; màu sơn xe hãng"},  # livery
    "lex.en.100k.014305": {"vi": "máy xúc lật; người bốc vác hàng"},  # loader
    "lex.en.100k.014306": {"vi": "người vận động hành lang chính sách"},  # lobbyist
    "lex.en.100k.014308": {"vi": "nhà cải cách Martin Luther"},  # luther
    "lex.en.100k.014309": {"vi": "mì ống cong Macaroni"},  # macaroni
    "lex.en.100k.014310": {"vi": "sự cố kỹ thuật; trục trặc hư hỏng"},  # malfunction
    "lex.en.100k.014311": {"vi": "kim loại mangan (hóa học)"},  # manganese
    "lex.en.100k.014314": {"vi": "quái vật Medusa; con sứa biển"},  # medusa
    "lex.en.100k.014315": {"vi": "ngày hạ chí; giữa mùa hè"},  # midsummer
    "lex.en.100k.014316": {"vi": "giao lưu hòa nhập; trộn lẫn"},  # mingle
    "lex.en.100k.014317": {"vi": "sự không tương xứng; cọc cạch"},  # mismatch
    "lex.en.100k.014318": {"pos": "verb", "vi": "cắt cỏ; xén cỏ bằng máy"},  # mow
    "lex.en.100k.014319": {"vi": "máy cắt cỏ; người xén cỏ"},  # mower
    "lex.en.100k.014320": {"vi": "lúc chạng vạng; hoàng hôn sập tối"},  # nightfall
    "lex.en.100k.014321": {"vi": "thương hiệu Nike; nữ thần Nike"},  # nike
    "lex.en.100k.014322": {"vi": "hoạt động về đêm; thuộc ban đêm"},  # nocturnal
    "lex.en.100k.014323": {"vi": "trên danh nghĩa; chỉ là hình thức"},  # nominally
    "lex.en.100k.014324": {"vi": "có thể quan sát thấy; dễ nhận biết"},  # observable
    "lex.en.100k.014325": {"vi": "yêu tinh ăn thịt người; kẻ tàn ác"},  # ogre
    "lex.en.100k.014326": {"vi": "được tra dầu nhờn; say bí tỉ"},  # oiled
    "lex.en.100k.014327": {"vi": "thông thường; như lệ thường"},  # ordinarily
    "lex.en.100k.014328": {"vi": "khu vực sân ngoài (bóng chày)"},  # outfield
    "lex.en.100k.014329": {"vi": "mang tính tham gia của cộng đồng"},  # participatory
    "lex.en.100k.014330": {"vi": "thú tiêu khiển; hoạt động giải trí"},  # pastime
    "lex.en.100k.014331": {"vi": "thuộc về người cha; phía bên nội"},  # paternal
    "lex.en.100k.014332": {"vi": "viên nén nhỏ; hạt thức ăn viên"},  # pellet
    "lex.en.100k.014333": {"vi": "con lắc đồng hồ; quả lắc dao động"},  # pendulum
    "lex.en.100k.014334": {"vi": "phiền phức khó chịu; hay quấy rầy"},  # pesky
    "lex.en.100k.014335": {"vi": "nỗi ám ảnh sợ hãi; chứng sợ hãi"},  # phobia
    "lex.en.100k.014336": {"vi": "trò chơi bắn bóng bàn pinball"},  # pinball
    "lex.en.100k.014338": {"vi": "toàn thể; toàn quyền quyết định"},  # plenary
    "lex.en.100k.014339": {"vi": "mưu mẹo mánh khóe; đòn thủ đoạn"},  # ploy
    "lex.en.100k.014340": {"vi": "chiến lợi phẩm; của cướp bóc"},  # plunder
    "lex.en.100k.014341": {"vi": "sợi nhân tạo polyester; vải sợi"},  # polyester
    "lex.en.100k.014342": {"pos": "noun", "vi": "thuộc đa thức; biểu thức đa thức"},  # polynomial
    "lex.en.100k.014343": {"vi": "cháo yến mạch; món cháo đặc"},  # porridge
    "lex.en.100k.014344": {"vi": "người biểu tình phản đối"},  # protester
    "lex.en.100k.014345": {"vi": "người theo chủ nghĩa thực tế"},  # realist
    "lex.en.100k.014346": {"vi": "chồm hai chân trước; việc nuôi nấng"},  # rearing
    "lex.en.100k.014347": {"vi": "sự trấn an tâm lý; lời cam đoan"},  # reassurance
    "lex.en.100k.014350": {"vi": "dân mê nhạc rock; thanh bập bênh"},  # rockers
    "lex.en.100k.014351": {"vi": "quân xe cờ vua; chim quạ gáy xám"},  # rook
    "lex.en.100k.014353": {"vi": "đánh thức dậy; khơi gợi nhiệt huyết"},  # rouse
    "lex.en.100k.014354": {"vi": "rất ít ỏi; khan hiếm không đáng kể"},  # scant
    "lex.en.100k.014355": {"vi": "kẻ gánh tội thay; bia đỡ đạn"},  # scapegoat
    "lex.en.100k.014356": {"vi": "tiếng rít chói tai; tiếng phanh két"},  # screeching
    "lex.en.100k.014357": {"vi": "sự tiết chất; chất dịch tiết ra"},  # secretion
    "lex.en.100k.014358": {"vi": "tù trưởng Ả Rập; thủ lĩnh bộ tộc"},  # sheik
    "lex.en.100k.014359": {"vi": "hàm sin (lượng giác học)"},  # sine
    "lex.en.100k.014360": {"vi": "con chồn hôi; kẻ đáng khinh bỉ"},  # skunk
    "lex.en.100k.014361": {"vi": "con lười Nam Mỹ; tính lười biếng"},  # sloth
    "lex.en.100k.014362": {"vi": "kẻ điểm chỉ; người mách lẻo"},  # snitch
    "lex.en.100k.014363": {"vi": "vừa vặn ấm cúng; gọn gàng kín gió"},  # snug
    "lex.en.100k.014364": {"vi": "đấu tập đối kháng; cuộc cãi vặt"},  # sparring
    "lex.en.100k.014365": {"vi": "kính đeo mắt; cặp kính cận"},  # spectacles
    "lex.en.100k.014366": {"vi": "trò hài nhại giễu cợt; trò lừa bịp"},  # spoof
    "lex.en.100k.014368": {"vi": "nằm sâu dưới lòng đất; ngầm bí mật"},  # subterranean
    "lex.en.100k.014369": {"vi": "siêu phàm vượt bậc; phi thường"},  # superhuman
    "lex.en.100k.014370": {"vi": "bộ đồ nỉ thể thao; áo nỉ tập luyện"},  # sweats
    "lex.en.100k.014371": {"vi": "có thể chấp nhận được; tạm ổn"},  # tolerable
    "lex.en.100k.014372": {"vi": "quốc đảo Tonga; ngôn ngữ Tonga"},  # tonga
    "lex.en.100k.014373": {"vi": "hành vi sai phạm dân sự (luật tort)"},  # tort
    "lex.en.100k.014374": {"vi": "sự xâm nhập trái phép; xâm phạm"},  # trespass
    "lex.en.100k.014375": {"vi": "bộ âu phục dạ tiệc Tuxedo; áo vét"},  # tuxedo
    "lex.en.100k.014376": {"vi": "tinh tế khiêm nhường; trang nhã"},  # understated
    "lex.en.100k.014378": {"vi": "một cách đơn phương; độc đoán"},  # unilaterally
    "lex.en.100k.014379": {"vi": "vô tình; không cố ý; ngoài ý muốn"},  # unintentional (purged opposite 'cố ý')
    "lex.en.100k.014380": {"vi": "một cách vô tình; không hay biết"},  # unknowingly
    "lex.en.100k.014381": {"vi": "bất khả xâm phạm; không ai đụng tới"},  # untouchable
    "lex.en.100k.014384": {"vi": "tính đa dụng linh hoạt; sự tháo vát"},  # versatility
    "lex.en.100k.014385": {"vi": "lọ thủy tinh nhỏ; ống thuốc tiêm"},  # vial
    "lex.en.100k.014386": {"vi": "máy rung cơ học; dụng cụ tạo rung"},  # vibrator
    "lex.en.100k.014387": {"vi": "than khóc thảm thiết; rên rỉ inh ỏi"},  # wailing
    "lex.en.100k.014388": {"vi": "từ đâu mà ra; từ nơi nào đến"},  # whence
    "lex.en.100k.014389": {"vi": "Đại học Yale (Mỹ); khóa Yale"},  # yale
    "lex.en.100k.014390": {"vi": "nước Cộng hòa Yemen (Trung Đông)"},  # yemen
    "lex.en.100k.014392": {"vi": "Robert Graves; những ngôi mộ"},  # graves
    "lex.en.100k.014393": {"vi": "Giáo hoàng Gregory; Thánh Gregory"},  # gregory
    "lex.en.100k.014394": {"vi": "Tổng thống Rutherford B. Hayes"},  # hayes
    "lex.en.100k.014395": {"vi": "thành phố Minneapolis (Minnesota)"},  # minneapolis
    "lex.en.100k.014396": {"vi": "nhà văn Toni Morrison; Jim Morrison"},  # morrison
    "lex.en.100k.014397": {"vi": "nhà tiên tri Muhammad (Hồi giáo)"},  # muhammad
    "lex.en.100k.014398": {"vi": "họ Robertson; tên người Robertson"},  # robertson
    "lex.en.100k.014399": {"pos": "num", "vi": "số 17; mười bảy"},  # seventeen
    "lex.en.100k.014400": {"vi": "tỉnh bang Alberta (Canada)"},  # alberta

    # 4401 - 4500
    "lex.en.100k.014401": {"vi": "đại văn hào James Joyce (Ireland)"},  # joyce
    "lex.en.100k.014402": {"vi": "sự phán quyết; khả năng phán đoán"},  # judgement
    "lex.en.100k.014403": {"vi": "chuột Mickey (Disney); họ Mickey"},  # mickey (purged crawler error 'Micken')
    "lex.en.100k.014404": {"vi": "thứ Hai (viết tắt); từ xưng hô"},  # mon
    "lex.en.100k.014405": {"ipa": "/ˌɛn ɛs ˈeɪ/", "vi": "Cơ quan An ninh Quốc gia Mỹ (NSA)"},  # nsa
    "lex.en.100k.014406": {"vi": "thủ phủ Sacramento (California)"},  # sacramento
    "lex.en.100k.014407": {"vi": "địa chỉ URL; đường dẫn trang web"},  # url
    "lex.en.100k.014408": {"ipa": "/ˌeɪ tiː ˈɛm/", "vi": "máy rút tiền tự động ATM"},  # atm
    "lex.en.100k.014409": {"vi": "thành phố biển Brighton (nước Anh)"},  # brighton
    "lex.en.100k.014410": {"vi": "thuộc Phật giáo; tín đồ Phật giáo"},  # buddhist
    "lex.en.100k.014411": {"ipa": "/ˌsiː ˈɛf/", "vi": "đối chiếu; so sánh (từ viết tắt cf)"},  # cf
    "lex.en.100k.014412": {"pos": "num", "ipa": "/ˌsiː ˈɛl/", "vi": "số 150 (số La Mã CL); centilit"},  # cl
    "lex.en.100k.014413": {"vi": "tên riêng Herbert; George Herbert"},  # herbert
    "lex.en.100k.014414": {"ipa": "/ˌɛl ˈpiː/", "vi": "đĩa than album dài LP (âm nhạc)"},  # lp
    "lex.en.100k.014415": {"vi": "tên riêng nữ Nina; Nina Simone"},  # nina
    "lex.en.100k.014416": {"vi": "Viện Đại học Princeton (Hoa Kỳ)"},  # princeton
    "lex.en.100k.014418": {"vi": "tướng William Sherman; xe Sherman"},  # sherman
    "lex.en.100k.014419": {"vi": "thuộc về Việt Nam; tiếng Việt"},  # vietnamese
    "lex.en.100k.014420": {"vi": "đàn phong cầm accordion; đàn xếp"},  # accordion
    "lex.en.100k.014421": {"vi": "quả sồi; hạt cây sồi non"},  # acorn
    "lex.en.100k.014423": {"vi": "thuộc ngành hàng không vũ trụ"},  # aeronautical
    "lex.en.100k.014424": {"vi": "về mặt thẩm mỹ; đầy tính nghệ thuật"},  # aesthetically
    "lex.en.100k.014426": {"vi": "ốm yếu bệnh tật; suy thoái đình trệ"},  # ailing
    "lex.en.100k.014428": {"vi": "cáo buộc không căn cứ; quả quyết"},  # allege
    "lex.en.100k.014430": {"vi": "cây thuốc bạch chỉ (thảo mộc)"},  # angelica
    "lex.en.100k.014431": {"vi": "kẻ tấn công hung hãn; hung thủ"},  # assailant
    "lex.en.100k.014432": {"vi": "lạc lối; lầm đường lạc lối"},  # astray
    "lex.en.100k.014434": {"vi": "mang điềm tốt lành; thuận lợi"},  # auspicious
    "lex.en.100k.014435": {"vi": "người báo thù; kẻ rửa hận"},  # avenger
    "lex.en.100k.014436": {"vi": "thủ đô Băng Cốc (Thái Lan)"},  # bangkok
    "lex.en.100k.014438": {"vi": "hoàn toàn vô căn cứ; thiếu cơ sở"},  # baseless
    "lex.en.100k.014439": {"ipa": "/ˌbiː ˈbiː/", "vi": "đạn chì BB (súng hơi); viên bi nhỏ"},  # bb
    "lex.en.100k.014441": {"vi": "nhà hảo tâm tài trợ; vị ân nhân"},  # benefactor
    "lex.en.100k.014442": {"vi": "bủa vây bám riết; giày vò phiền hà"},  # beset
    "lex.en.100k.014443": {"vi": "người viết tiểu sử cuộc đời"},  # biographer
    "lex.en.100k.014444": {"vi": "chua ngoa đanh đá; hay nói xấu"},  # bitchy
    "lex.en.100k.014446": {"vi": "tiếng bíp điện tử; tiếng ngắt sóng"},  # bleep
    "lex.en.100k.014447": {"pos": "noun", "vi": "chuyện nhảm nhí; lời nói vô lý"},  # bollocks
    "lex.en.100k.014448": {"vi": "đường ruột nội tạng; đáy lòng sâu"},  # bowels
    "lex.en.100k.014450": {"vi": "phô mai mềm Brie của Pháp"},  # brie
    "lex.en.100k.014451": {"vi": "cặp đựng tài liệu công tác; cặp táp"},  # briefcase
    "lex.en.100k.014452": {"vi": "bị cài thiết bị nghe lén; bực mình"},  # bugged
    "lex.en.100k.014453": {"vi": "thủ đô Cairo (Ai Cập)"},  # cairo
    "lex.en.100k.014457": {"vi": "sự gần gũi mật thiết; độ kín gió"},  # closeness
    "lex.en.100k.014459": {"vi": "nguyên đơn khởi kiện; người tố giác"},  # complainant
    "lex.en.100k.014460": {"vi": "sự pha chế trộn lẫn; tính lãi kép"},  # compounding
    "lex.en.100k.014462": {"vi": "trịch thượng bề trên; khinh người"},  # condescending
    "lex.en.100k.014463": {"vi": "tuân thủ chuẩn mực; tương thích"},  # conforming
    "lex.en.100k.014464": {"vi": "sự tuân thủ khuôn phép; đồng thuận"},  # conformity
    "lex.en.100k.014465": {"vi": "tận tâm chu đáo; có trách nhiệm cao"},  # conscientious
    "lex.en.100k.014467": {"vi": "một cách đầy sức thuyết phục"},  # convincingly
    "lex.en.100k.014468": {"vi": "tay nghề thủ công tinh xảo"},  # craftsmanship
    "lex.en.100k.014469": {"vi": "họ Crawford; diễn viên Crawford"},  # crawford
    "lex.en.100k.014470": {"vi": "tột bậc vinh quang; đỉnh cao nhất"},  # crowning
    "lex.en.100k.014471": {"vi": "khấu trừ chi phí; trừ bớt đi"},  # deduct (purged single-word 'trừ')
    "lex.en.100k.014472": {"vi": "hạt Devon (Tây Nam nước Anh)"},  # devon
    "lex.en.100k.014473": {"vi": "cơ hoành ngăn ngực bụng; màng chắn"},  # diaphragm
    "lex.en.100k.014474": {"vi": "sự phân đôi đối lập; sự chia đôi"},  # dichotomy
    "lex.en.100k.014475": {"vi": "nhỏ nhắn bé xíu; có tính giảm nhỏ"},  # diminutive
    "lex.en.100k.014477": {"vi": "sự phân kỳ; sự khác biệt rẽ lối"},  # divergence
    "lex.en.100k.014478": {"vi": "chắc chắn; không một chút nghi ngờ"},  # doubtless
    "lex.en.100k.014479": {"vi": "nhược điểm trở ngại; điều bất lợi"},  # drawback
    "lex.en.100k.014480": {"vi": "đang suy giảm dần; ngày một hao hụt"},  # dwindling
    "lex.en.100k.014481": {"vi": "dễ dàng không tốn sức; thanh thoát"},  # effortless
    "lex.en.100k.014482": {"vi": "nhấn mạnh dứt khoát; rành rẽ"},  # emphatic
    "lex.en.100k.014484": {"vi": "ca tử vong; thiệt mạng vì tai nạn"},  # fatality
    "lex.en.100k.014485": {"vi": "hung dữ hung tợn; vô cùng dữ dội"},  # ferocious
    "lex.en.100k.014487": {"vi": "dây tóc bóng đèn; sợi tơ mảnh nhỏ"},  # filament
    "lex.en.100k.014489": {"vi": "soạn thảo hoạch định; phát biểu rõ"},  # formulate
    "lex.en.100k.014490": {"vi": "sảnh đón khách; hành lang phòng đợi"},  # foyer
    "lex.en.100k.014492": {"vi": "tranh bích họa trên vách tường vôi"},  # fresco
    "lex.en.100k.014493": {"vi": "thân máy bay (hàng không)"},  # fuselage (purged single-word 'thân')
    "lex.en.100k.014494": {"vi": "dáng điệu bước đi; nhịp bước chân"},  # gait
    "lex.en.100k.014496": {"vi": "ma quái rùng rợn; mờ ảo chập chờn"},  # ghostly
    "lex.en.100k.014497": {"vi": "được mạ vàng óng; thếp vàng óng ánh"},  # gilt
    "lex.en.100k.014498": {"vi": "tàu lượn không động cơ; phi cơ lượn"},  # glider
    "lex.en.100k.014499": {"vi": "quả bưởi chùm Mỹ; bưởi bồng đắng"},  # grapefruit
    "lex.en.100k.014500": {"vi": "một cách nghiêm trọng; trang nghiêm"},  # gravely
}

# Verify lengths <= 35
for k, v in OVERRIDES_B03_R09.items():
    if "vi" in v:
        assert len(v["vi"]) <= 35, f"Length > 35 for {k}: {v['vi']} ({len(v['vi'])})"

with open('content/english/qa-batches/batch-03.json', 'r', encoding='utf-8') as f:
    batch_data = json.load(f)

# Apply overrides to records in range 4000 to 4500
count = 0
for idx in range(4000, 4500):
    rec = batch_data['records'][idx]
    rid = rec['id']
    if rid in OVERRIDES_B03_R09:
        count += 1
        for field, val in OVERRIDES_B03_R09[rid].items():
            rec[field] = val
        rec['status'] = 'reviewed'

batch_data['reviewedCount'] = 4500

with open('content/english/qa-batches/batch-03.json', 'w', encoding='utf-8') as f:
    json.dump(batch_data, f, ensure_ascii=False, indent=2)

print(f"Successfully applied Batch 03 Round 9 ({count} overrides). Reviewed: {batch_data['reviewedCount']}/5000.")
