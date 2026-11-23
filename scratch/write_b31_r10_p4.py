# -*- coding: utf-8 -*-
import json

part4_data = [
  {"id": "lex.en.200k.054802", "hw": "agees", "pos": "noun", "ipa": "/ˈeɪdʒiːz/", "vi": "nhà văn James Agee", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054803", "hw": "alexandrians", "pos": "noun", "ipa": "/ˌælɪɡˈzændriənz/", "vi": "cư dân thành phố Alexandria", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054804", "hw": "aughts", "pos": "noun", "ipa": "/ɔːts/", "vi": "số không; những năm đầu thế kỷ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054805", "hw": "bataans", "pos": "noun", "ipa": "/bəˈtɑːnz/", "vi": "bán đảo Bataan ở Philippines", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054806", "hw": "belayed", "pos": "verb", "ipa": "/bɪˈleɪd/", "vi": "đã neo dây; đã buộc dây an toàn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054807", "hw": "belaying", "pos": "verb", "ipa": "/bɪˈleɪɪŋ/", "vi": "đang giữ dây leo núi an toàn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054808", "hw": "belays", "pos": "noun", "ipa": "/bɪˈleɪz/", "vi": "điểm neo dây bảo hiểm leo núi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054809", "hw": "benzodiazepines", "pos": "noun", "ipa": "/ˌbɛnzoʊdaɪˈæzɪpiːnz/", "vi": "nhóm thuốc an thần gây ngủ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054810", "hw": "bonked", "pos": "verb", "ipa": "/bɑːŋkt/", "vi": "đã gõ đầu; đã kiệt sức khi chạy", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054811", "hw": "bonking", "pos": "verb", "ipa": "/ˈbɑːŋkɪŋ/", "vi": "đang gõ đầu; đang kiệt sức", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054812", "hw": "bonks", "pos": "verb", "ipa": "/bɑːŋks/", "vi": "gõ vào đầu; kiệt sức thể thao", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054813", "hw": "botticellis", "pos": "noun", "ipa": "/ˌbɒtɪˈtʃɛliz/", "vi": "danh họa Sandro Botticelli", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054814", "hw": "braes", "pos": "noun", "ipa": "/breɪz/", "vi": "các sườn đồi thoai thoải dốc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054815", "hw": "brawlers", "pos": "noun", "ipa": "/ˈbrɔːlərz/", "vi": "những kẻ hay gây lộn đánh nhau", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054816", "hw": "bunsens", "pos": "noun", "ipa": "/ˈbʌnsənz/", "vi": "đèn khí Bunsen phòng thí nghiệm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054817", "hw": "burls", "pos": "noun", "ipa": "/bɜːrlz/", "vi": "các bướu sần sùi trên thân cây", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054818", "hw": "canards", "pos": "noun", "ipa": "/kəˈnɑːrdz/", "vi": "những tin vịt; tin đồn thất thiệt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054819", "hw": "caraways", "pos": "noun", "ipa": "/ˈkærəweɪz/", "vi": "hạt thì là Ba Tư thơm caraway", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054820", "hw": "cenozoics", "pos": "noun", "ipa": "/ˌsiːnəˈzoʊɪks/", "vi": "đại Tân Sinh trong địa chất học", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054821", "hw": "cgses", "pos": "noun", "ipa": "/siː-dʒiː-ɛsɪz/", "vi": "hệ đo lường CGS xentimét-gam-giây", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054822", "hw": "chons", "pos": "noun", "ipa": "/tʃɒnz/", "vi": "đồng xu chon của Triều Tiên", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054823", "hw": "clamourings", "pos": "noun", "ipa": "/ˈklæmərɪŋz/", "vi": "tiếng la hét đòi hỏi ầm ĩ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054824", "hw": "commutations", "pos": "noun", "ipa": "/ˌkɑːmjuːˈteɪʃənz/", "vi": "sự giảm án; việc đi làm hàng ngày", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054825", "hw": "creosoted", "pos": "verb", "ipa": "/ˈkriːəsoʊtɪd/", "vi": "đã quét dầu creosote bảo quản", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054826", "hw": "creosotes", "pos": "noun", "ipa": "/ˈkriːəsoʊts/", "vi": "dầu creosote chống mục gỗ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054827", "hw": "creosoting", "pos": "verb", "ipa": "/ˈkriːəsoʊtɪŋ/", "vi": "đang quét dầu creosote bảo quản", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054828", "hw": "crumblier", "pos": "adj", "ipa": "/ˈkrʌmbliər/", "vi": "dễ vỡ vụn hơn; bở hơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054829", "hw": "crumbliest", "pos": "adj", "ipa": "/ˈkrʌmbliɪst/", "vi": "dễ vỡ vụn nhất; bở nhất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054830", "hw": "curios", "pos": "noun", "ipa": "/ˈkjʊrioʊz/", "vi": "những món đồ cổ độc lạ quý hiếm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054831", "hw": "cuzcos", "pos": "noun", "ipa": "/ˈkuːzkoʊz/", "vi": "thành phố cổ Cusco của người Inca", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054832", "hw": "datives", "pos": "noun", "ipa": "/ˈdeɪtɪvz/", "vi": "các tặng cách trong ngữ pháp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054833", "hw": "decentralisations", "pos": "noun", "ipa": "/diːˌsɛntrəlaɪˈzeɪʃənz/", "vi": "tiến trình phân quyền cơ quan", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054834", "hw": "deliverables", "pos": "noun", "ipa": "/dɪˈlɪvərəbəlz/", "vi": "các sản phẩm kết quả bàn giao", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054835", "hw": "disclaimed", "pos": "verb", "ipa": "/dɪsˈkleɪmd/", "vi": "đã từ chối; đã chối bỏ trách nhiệm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054836", "hw": "dramatizations", "pos": "noun", "ipa": "/ˌdræmətəˈzeɪʃənz/", "vi": "sự kịch hóa tác phẩm văn học", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054837", "hw": "dressier", "pos": "adj", "ipa": "/ˈdrɛsiər/", "vi": "ăn mặc sang trọng hơn; chỉn chu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054838", "hw": "dressiest", "pos": "adj", "ipa": "/ˈdrɛsiɪst/", "vi": "ăn mặc sang trọng lịch sự nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054839", "hw": "eardrums", "pos": "noun", "ipa": "/ˈɪərdrʌmz/", "vi": "những màng nhĩ trong tai", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054840", "hw": "emoticons", "pos": "noun", "ipa": "/ɪˈmoʊtɪkɑːnz/", "vi": "biểu tượng cảm xúc bằng ký tự", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054841", "hw": "empathised", "pos": "verb", "ipa": "/ˈɛmpəθaɪzd/", "vi": "đã đồng cảm; đã thấu hiểu tâm can", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054842", "hw": "empathises", "pos": "verb", "ipa": "/ˈɛmpəθaɪzɪz/", "vi": "đồng cảm; thấu cảm nỗi đau", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054843", "hw": "empathising", "pos": "verb", "ipa": "/ˈɛmpəθaɪzɪŋ/", "vi": "đang đồng cảm; đang thấu hiểu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054844", "hw": "encyclicals", "pos": "noun", "ipa": "/ɛnˈsɪklɪkəlz/", "vi": "những thông điệp của Giáo hoàng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054845", "hw": "folksier", "pos": "adj", "ipa": "/ˈfoʊksiər/", "vi": "dân dã hơn; mộc mạc gần gũi hơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054846", "hw": "folksiest", "pos": "adj", "ipa": "/ˈfoʊksiɪst/", "vi": "dân dã nhất; mộc mạc nhất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054847", "hw": "foramens", "pos": "noun", "ipa": "/fəˈreɪmənz/", "vi": "các lỗ nhỏ tự nhiên trong xương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054848", "hw": "forecasters", "pos": "noun", "ipa": "/ˈfɔːrkæstərz/", "vi": "những chuyên gia dự báo thời tiết", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054849", "hw": "formicas", "pos": "noun", "ipa": "/fɔːrˈmaɪkəz/", "vi": "chất liệu nhựa ép Formica phủ bàn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054850", "hw": "fosses", "pos": "noun", "ipa": "/ˈfɒsɪz/", "vi": "hào sâu bao quanh pháo đài lũy", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054851", "hw": "freemasons", "pos": "noun", "ipa": "/ˈfriːmeɪsənz/", "vi": "những thành viên Hội Tam Điểm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054852", "hw": "fundraised", "pos": "verb", "ipa": "/ˈfʌndreɪzd/", "vi": "đã gây quỹ từ thiện quyên tiền", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054853", "hw": "fundraises", "pos": "verb", "ipa": "/ˈfʌndreɪzɪz/", "vi": "gây quỹ; quyên góp tiền ủng hộ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054854", "hw": "fundraising", "pos": "verb", "ipa": "/ˈfʌndreɪzɪŋ/", "vi": "đang gây quỹ quyên góp tiền", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054855", "hw": "gardenias", "pos": "noun", "ipa": "/ɡɑːrˈdiːniəz/", "vi": "những bông hoa dành dành trắng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054856", "hw": "gazetteers", "pos": "noun", "ipa": "/ˌɡæzəˈtɪərz/", "vi": "từ điển địa danh; bảng tra địa lý", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054857", "hw": "glasshouses", "pos": "noun", "ipa": "/ˈɡlæshaʊzɪz/", "vi": "những nhà kính trồng rau cây hoa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054858", "hw": "glucks", "pos": "noun", "ipa": "/ɡlʊks/", "vi": "nhà soạn nhạc Christoph Gluck", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054859", "hw": "goggled", "pos": "verb", "ipa": "/ˈɡɑːɡəld/", "vi": "đã trố mắt nhìn ngạc nhiên", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054860", "hw": "goggling", "pos": "verb", "ipa": "/ˈɡɑːɡəlɪŋ/", "vi": "đang trố mắt ngạc nhiên nhìn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054861", "hw": "goldfinches", "pos": "noun", "ipa": "/ˈɡoʊldfɪntʃɪz/", "vi": "loài chim sẻ kim oanh lông vàng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054862", "hw": "hazlitts", "pos": "noun", "ipa": "/ˈhæzlɪts/", "vi": "nhà tiểu luận Anh William Hazlitt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054863", "hw": "hemodialyses", "pos": "noun", "ipa": "/ˌhiːmoʊdaɪˈæləsiːz/", "vi": "các đợt chạy thận nhân tạo lọc máu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054864", "hw": "holdups", "pos": "noun", "ipa": "/ˈhoʊldʌps/", "vi": "vụ cướp có vũ trang; sự tắc nghẽn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054865", "hw": "hunkered", "pos": "verb", "ipa": "/ˈhʌŋkərd/", "vi": "đã ngồi thụp xuống; đã cố thủ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054866", "hw": "hunkering", "pos": "verb", "ipa": "/ˈhʌŋkərɪŋ/", "vi": "đang ngồi xổm thụp; đang cố thủ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054867", "hw": "icicles", "pos": "noun", "ipa": "/ˈaɪsɪkəlz/", "vi": "những cột băng nhọn rủ xuống", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054868", "hw": "japonicas", "pos": "noun", "ipa": "/dʒəˈpɒnɪkəz/", "vi": "cây hoa trà mi Nhật Bản japonica", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054869", "hw": "jungians", "pos": "noun", "ipa": "/ˈjʊŋiənz/", "vi": "môn đồ tâm lý học Carl Jung", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054870", "hw": "kavas", "pos": "noun", "ipa": "/ˈkɑːvəz/", "vi": "thức uống kava Nam Thái Bình Dương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054871", "hw": "kronen", "pos": "noun", "ipa": "/ˈkroʊnən/", "vi": "đồng curon đơn vị tiền tệ Bắc Âu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054872", "hw": "kroner", "pos": "noun", "ipa": "/ˈkroʊnər/", "vi": "đồng tiền krone Na Uy và Đan Mạch", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054873", "hw": "kuis", "pos": "noun", "ipa": "/ˈkuːiz/", "vi": "người dân tộc Kui ở Đông Nam Á", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054874", "hw": "kwas", "pos": "noun", "ipa": "/kwɑːz/", "vi": "nhóm ngôn ngữ Kwa ở Tây Phi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054875", "hw": "litigated", "pos": "verb", "ipa": "/ˈlɪtɪɡeɪtɪd/", "vi": "đã khởi kiện ra tòa tranh tụng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054876", "hw": "lyses", "pos": "noun", "ipa": "/ˈlaɪsiːz/", "vi": "sự tan rã tế bào; sự giảm sốt dần", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054877", "hw": "maare", "pos": "noun", "ipa": "/ˈmɑːrə/", "vi": "hồ miệng núi lửa maar nông rộng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054878", "hw": "maars", "pos": "noun", "ipa": "/mɑːrz/", "vi": "những miệng núi lửa maar chứa nước", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054879", "hw": "macaques", "pos": "noun", "ipa": "/məˈkæk/", "vi": "loài khỉ đuôi dài; khỉ macaque", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054880", "hw": "madcaps", "pos": "noun", "ipa": "/ˈmædkæps/", "vi": "những kẻ bốc đồng liều lĩnh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054881", "hw": "malformations", "pos": "noun", "ipa": "/ˌmælfɔːrˈmeɪʃənz/", "vi": "các dị tật dị dạng bẩm sinh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054882", "hw": "maquises", "pos": "noun", "ipa": "/məˈkiːz/", "vi": "du kích kháng chiến Maquis Pháp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054883", "hw": "maritimeses", "pos": "noun", "ipa": "/ˈmærɪtaɪmzɪz/", "vi": "vùng các tỉnh Duyên hải Canada", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054884", "hw": "matrics", "pos": "noun", "ipa": "/ˈmætrɪks/", "vi": "kỳ thi tốt nghiệp ở Nam Phi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054885", "hw": "medans", "pos": "noun", "ipa": "/meɪˈdɑːnz/", "vi": "thành phố Medan trên đảo Sumatra", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054886", "hw": "minders", "pos": "noun", "ipa": "/ˈmaɪndərz/", "vi": "người chăm sóc; cận vệ bảo vệ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054887", "hw": "mouldier", "pos": "adj", "ipa": "/ˈmoʊldiər/", "vi": "mốc meo nhiều hơn; cũ kỹ hơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054888", "hw": "mouldiest", "pos": "adj", "ipa": "/ˈmoʊldiɪst/", "vi": "mốc meo nhiều nhất; cũ rích nhất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054889", "hw": "muskier", "pos": "adj", "ipa": "/ˈmʌskiər/", "vi": "đậm mùi xạ hương nồng hơn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054890", "hw": "muskiest", "pos": "adj", "ipa": "/ˈmʌskiɪst/", "vi": "đậm mùi xạ hương nồng nhất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054891", "hw": "nabluses", "pos": "noun", "ipa": "/ˈnæbləsɪz/", "vi": "thành phố cổ Nablus ở Bờ Tây", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054892", "hw": "neems", "pos": "noun", "ipa": "/niːmz/", "vi": "loài cây neem sầu đâu trị bệnh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054893", "hw": "ocas", "pos": "noun", "ipa": "/ˈoʊkəz/", "vi": "cây chua me đất lấy củ oca Andes", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054894", "hw": "otos", "pos": "noun", "ipa": "/ˈoʊtoʊz/", "vi": "người bộ tộc Otoe da đỏ Bắc Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054895", "hw": "overwrites", "pos": "verb", "ipa": "/ˌoʊvərˈraɪts/", "vi": "ghi đè dữ liệu; viết hoa mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054896", "hw": "overwriting", "pos": "verb", "ipa": "/ˌoʊvərˈraɪtɪŋ/", "vi": "đang ghi đè lên dữ liệu cũ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054897", "hw": "pericleses", "pos": "noun", "ipa": "/ˈpɛrɪkliːzɪz/", "vi": "nhà lãnh đạo Athens cổ Pericles", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054898", "hw": "psalters", "pos": "noun", "ipa": "/ˈsɔːltərz/", "vi": "những cuốn sách Thánh vịnh dùng lễ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054899", "hw": "pwrs", "pos": "noun", "ipa": "/ˌpiː.dʌbəl.juːˈɑːrz/", "vi": "lò phản ứng hạt nhân nước áp lực", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054900", "hw": "qeds", "pos": "noun", "ipa": "/ˌkjuː.iːˈdiːz/", "vi": "thuyết điện động lực học lượng tử", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.200k.054901", "hw": "rainmakers", "pos": "noun", "ipa": "/ˈreɪnmeɪkərz/", "vi": "người mang về hợp đồng béo bở", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""}
]

# Validation
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}
expected_keys = ['id', 'hw', 'pos', 'ipa', 'vi', 'cefr', 'tier', 'status', 'notes']

assert len(part4_data) == 100, f"Length is {len(part4_data)}"

with open('scratch/b31_r10_raw_p4.json') as f:
    raw = json.load(f)

for i, (item, raw_item) in enumerate(zip(part4_data, raw)):
    assert item['id'] == raw_item['id'], f"ID mismatch at {i}: {item['id']} vs {raw_item['id']}"
    assert item['hw'] == raw_item['hw'], f"HW mismatch at {i}: {item['hw']} vs {raw_item['hw']}"
    assert list(item.keys()) == expected_keys, f"Keys mismatch at {i}: {list(item.keys())}"
    assert item['pos'] in allowed_pos, f"pos invalid at {i}: {item['pos']}"
    assert len(item['vi']) <= 35, f"vi too long ({len(item['vi'])} chars) at {i}: {item['vi']}"
    assert item['status'] == 'reviewed'
    if ' ' not in item['hw']:
        assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and len(item['ipa']) > 2, f"invalid ipa at {i}: {item['ipa']}"
    if ';' in item['vi']:
        for seg in item['vi'].split(';')[1:]:
            assert seg.startswith(' '), f"missing space after semicolon at {i}: {item['vi']}"

with open('scratch/b31_r10_p4.json', 'w', encoding='utf-8') as f:
    json.dump(part4_data, f, ensure_ascii=False, indent=2)

print("Validated and saved 100 items for Part 4")
