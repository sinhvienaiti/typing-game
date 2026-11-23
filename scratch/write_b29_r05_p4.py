import json
import re

items = [
    {"id": "lex.en.200k.042302", "hw": "epoxies", "pos": "noun", "ipa": "/ɪˈpɑːksiz/", "vi": "các loại keo dán epoxy", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042303", "hw": "epoxying", "pos": "verb", "ipa": "/ɪˈpɑːksiɪŋ/", "vi": "đang dán bằng keo epoxy", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042304", "hw": "estonians", "pos": "noun", "ipa": "/ɛˈstoʊniənz/", "vi": "những người dân Estonia", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042305", "hw": "evangelists", "pos": "noun", "ipa": "/ɪˈvændʒəlɪsts/", "vi": "các nhà truyền bá Phúc Âm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042306", "hw": "eyeballed", "pos": "verb", "ipa": "/ˈaɪbɔːld/", "vi": "đã nhìn chằm chằm; ước lượng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042307", "hw": "eyeballing", "pos": "verb", "ipa": "/ˈaɪbɔːlɪŋ/", "vi": "đang nhìn chằm chằm; ước chừng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042308", "hw": "eyeballs", "pos": "noun", "ipa": "/ˈaɪbɔːlz/", "vi": "những nhãn cầu mắt; quả mắt", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042309", "hw": "fiends", "pos": "noun", "ipa": "/fiːndz/", "vi": "những kẻ ác độc; kẻ mê mẩn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042310", "hw": "fledglings", "pos": "noun", "ipa": "/ˈflɛdʒlɪŋz/", "vi": "chim non mới ra ràng; tân binh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042311", "hw": "flimsier", "pos": "adj", "ipa": "/ˈflɪmziər/", "vi": "mỏng manh hơn; yếu ớt hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042312", "hw": "flimsiest", "pos": "adj", "ipa": "/ˈflɪmziɪst/", "vi": "mỏng manh nhất; yếu ớt nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042313", "hw": "footers", "pos": "noun", "ipa": "/ˈfʊtərz/", "vi": "phần chân trang văn bản", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042314", "hw": "gambits", "pos": "noun", "ipa": "/ˈɡæmbɪts/", "vi": "nước cờ thí quân; đòn mở đầu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042315", "hw": "gleamings", "pos": "noun", "ipa": "/ˈɡliːmɪŋz/", "vi": "những ánh sáng le lói lấp lánh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042316", "hw": "grilles", "pos": "noun", "ipa": "/ɡrɪlz/", "vi": "các tấm lưới kim loại bảo vệ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042317", "hw": "heathens", "pos": "noun", "ipa": "/ˈhiːðənz/", "vi": "những kẻ ngoại đạo man di", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042318", "hw": "hemorrhaged", "pos": "verb", "ipa": "/ˈhɛmərɪdʒd/", "vi": "đã bị xuất huyết ồ ạt", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042319", "hw": "hemorrhages", "pos": "noun", "ipa": "/ˈhɛmərɪdʒɪz/", "vi": "các cơn xuất huyết mạch máu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042320", "hw": "hemorrhaging", "pos": "verb", "ipa": "/ˈhɛmərɪdʒɪŋ/", "vi": "đang xuất huyết; đang mất máu", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042321", "hw": "hereafters", "pos": "noun", "ipa": "/ˌhɪrˈæftərz/", "vi": "thế giới kiếp sau; cõi âm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042322", "hw": "hijackings", "pos": "noun", "ipa": "/ˈhaɪdʒækɪŋz/", "vi": "các vụ cướp máy bay tàu bè", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042323", "hw": "hoardings", "pos": "noun", "ipa": "/ˈhɔːrdɪŋz/", "vi": "các biển pa-nô quảng cáo lớn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042324", "hw": "horoscopes", "pos": "noun", "ipa": "/ˈhɔːrəskoʊps/", "vi": "các lá số tử vi chiêm tinh", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042325", "hw": "humanoids", "pos": "noun", "ipa": "/ˈhjuːmənɔɪdz/", "vi": "các người máy dạng người", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042326", "hw": "improvisations", "pos": "noun", "ipa": "/ˌɪmprəvaɪˈzeɪʃənz/", "vi": "những màn biểu diễn ngẫu hứng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042327", "hw": "jaggers", "pos": "noun", "ipa": "/ˈdʒæɡərz/", "vi": "những người họ Jagger", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042328", "hw": "jerkier", "pos": "adj", "ipa": "/ˈdʒɜːrkiər/", "vi": "giật cục hơn; rung lắc hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042329", "hw": "jerkiest", "pos": "adj", "ipa": "/ˈdʒɜːrkiɪst/", "vi": "giật cục nhất; rung lắc nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042330", "hw": "kathmandus", "pos": "noun", "ipa": "/ˌkætmænˈduːz/", "vi": "thành phố Kathmandu Nepal", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042331", "hw": "khzes", "pos": "noun", "ipa": "/ˈkɪləhɜːrtsɪz/", "vi": "các kilohertz; đơn vị kHz", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042332", "hw": "lexicons", "pos": "noun", "ipa": "/ˈlɛksɪkɑːnz/", "vi": "các bộ từ điển chuyên ngành", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042333", "hw": "livingstones", "pos": "noun", "ipa": "/ˈlɪvɪŋstənz/", "vi": "những người họ Livingstone", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042334", "hw": "lobbyists", "pos": "noun", "ipa": "/ˈlɑːbiɪsts/", "vi": "những kẻ vận động hành lang", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042335", "hw": "lucknows", "pos": "noun", "ipa": "/ˈlʌknaʊz/", "vi": "thành phố Lucknow Ấn Độ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042336", "hw": "lurked", "pos": "verb", "ipa": "/lɜːrkt/", "vi": "đã rình rập; đã ẩn nấp", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042337", "hw": "lurks", "pos": "verb", "ipa": "/lɜːrks/", "vi": "rình rập; ẩn nấp phục kích", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042338", "hw": "marguerites", "pos": "noun", "ipa": "/ˌmɑːrɡəˈriːts/", "vi": "hoa cúc trắng marguerite", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042339", "hw": "mcphersons", "pos": "noun", "ipa": "/məkˈfɜːrsənz/", "vi": "những người họ McPherson", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042340", "hw": "medallions", "pos": "noun", "ipa": "/məˈdæljənz/", "vi": "những chiếc huy chương tròn lớn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042341", "hw": "monastics", "pos": "noun", "ipa": "/məˈnæstɪks/", "vi": "những người tu sĩ tu viện", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042342", "hw": "mormonses", "pos": "noun", "ipa": "/ˈmɔːrmənzɪz/", "vi": "các tín đồ Giáo hội Mormon", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042343", "hw": "mots", "pos": "noun", "ipa": "/moʊz/", "vi": "những câu nói hóm hỉnh ngắn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042344", "hw": "mowers", "pos": "noun", "ipa": "/ˈmoʊərz/", "vi": "các máy cắt cỏ; thợ cắt cỏ", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042345", "hw": "namesakes", "pos": "noun", "ipa": "/ˈneɪmseɪks/", "vi": "những người cùng tên họ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042346", "hw": "nazareths", "pos": "noun", "ipa": "/ˈnæzərəθs/", "vi": "thị trấn Nazareth thiêng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042347", "hw": "nazisms", "pos": "noun", "ipa": "/ˈnɑːtsɪzəmz/", "vi": "chủ nghĩa phát xít Đức Quốc xã", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042348", "hw": "ogres", "pos": "noun", "ipa": "/ˈoʊɡərz/", "vi": "loài chằn tinh khổng lồ ăn thịt", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042349", "hw": "palermos", "pos": "noun", "ipa": "/pəˈlɛərmoʊz/", "vi": "thành phố Palermo xứ Sicily", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042350", "hw": "palliatives", "pos": "noun", "ipa": "/ˈpæliətɪvz/", "vi": "các biện pháp xoa dịu tạm thời", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042351", "hw": "parables", "pos": "noun", "ipa": "/ˈpærəbəlz/", "vi": "những câu chuyện ngụ ngôn đạo lý", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042352", "hw": "pastimes", "pos": "noun", "ipa": "/ˈpæstaɪmz/", "vi": "những trò tiêu khiển thư giãn", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042353", "hw": "patchworks", "pos": "noun", "ipa": "/ˈpætʃwɜːrks/", "vi": "tranh vải chắp vá; sự chắp vá", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042354", "hw": "peshawars", "pos": "noun", "ipa": "/pəˈʃɑːwərz/", "vi": "thành phố Peshawar Pakistan", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042355", "hw": "peskier", "pos": "adj", "ipa": "/ˈpɛskiər/", "vi": "phiền phức hơn; quấy rầy hơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042356", "hw": "peskiest", "pos": "adj", "ipa": "/ˈpɛskiɪst/", "vi": "phiền phức nhất; quấy rầy nhất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042357", "hw": "phobias", "pos": "noun", "ipa": "/ˈfoʊbiəz/", "vi": "các hội chứng ám ảnh sợ hãi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042358", "hw": "poseidons", "pos": "noun", "ipa": "/pəˈsaɪdənz/", "vi": "hình tượng thần biển Poseidon", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042359", "hw": "privatisations", "pos": "noun", "ipa": "/ˌpraɪvətaɪˈzeɪʃənz/", "vi": "các đợt cổ phần hóa tư nhân", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042360", "hw": "pullmans", "pos": "noun", "ipa": "/ˈpʊlmənz/", "vi": "các toa xe lửa tiện nghi Pullman", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042361", "hw": "purgatories", "pos": "noun", "ipa": "/ˈpɜːrɡətɔːriz/", "vi": "chốn luyện ngục thanh tẩy", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042362", "hw": "rebuttals", "pos": "noun", "ipa": "/rɪˈbʌtəlz/", "vi": "những lời bác bỏ tranh luận", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042363", "hw": "relievers", "pos": "noun", "ipa": "/rɪˈliːvərz/", "vi": "người cứu trợ; thuốc giảm đau", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042364", "hw": "riyadhs", "pos": "noun", "ipa": "/rɪˈjɑːdz/", "vi": "thủ đô Riyadh Ả Rập Xê Út", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042365", "hw": "samplers", "pos": "noun", "ipa": "/ˈsæmplərz/", "vi": "mẫu thêu thử; thiết bị lấy mẫu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042366", "hw": "sarajevos", "pos": "noun", "ipa": "/ˌsærəˈjeɪvoʊz/", "vi": "thành phố Sarajevo lịch sử", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042367", "hw": "scanter", "pos": "adj", "ipa": "/ˈskæntər/", "vi": "ít ỏi hơn; thiếu thốn hơn", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042368", "hw": "scantest", "pos": "adj", "ipa": "/ˈskæntɪst/", "vi": "ít ỏi nhất; thiếu thốn nhất", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042369", "hw": "schoolgirls", "pos": "noun", "ipa": "/ˈskuːlɡɜːrlz/", "vi": "các nữ sinh nữ sinh viên", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042370", "hw": "semblances", "pos": "noun", "ipa": "/ˈsɛmblənsɪz/", "vi": "những vẻ bề ngoài giả tạo", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042371", "hw": "sheiks", "pos": "noun", "ipa": "/ʃeɪks/", "vi": "các tù trưởng Ả Rập; thủ lĩnh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042372", "hw": "sines", "pos": "noun", "ipa": "/saɪnz/", "vi": "các giá trị hàm sin toán học", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042373", "hw": "sloths", "pos": "noun", "ipa": "/sloʊθs/", "vi": "những con lười biếng; con lười", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042374", "hw": "slowdowns", "pos": "noun", "ipa": "/ˈsloʊdaʊnz/", "vi": "các đợt suy thoái chậm lại", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042375", "hw": "snitched", "pos": "verb", "ipa": "/snɪtʃt/", "vi": "đã mách lẻo; đã chỉ điểm trộm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042376", "hw": "snitches", "pos": "noun", "ipa": "/ˈsnɪtʃɪz/", "vi": "những kẻ điểm chỉ mách lẻo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042377", "hw": "snitching", "pos": "verb", "ipa": "/ˈsnɪtʃɪŋ/", "vi": "đang mách lẻo; hành vi mách lẻo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042378", "hw": "snugger", "pos": "adj", "ipa": "/ˈsnʌɡər/", "vi": "ấm áp hơn; vừa vặn khít hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042379", "hw": "snuggest", "pos": "adj", "ipa": "/ˈsnʌɡɪst/", "vi": "ấm áp nhất; vừa vặn khít nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042380", "hw": "solstices", "pos": "noun", "ipa": "/ˈsɑːlstɪsɪz/", "vi": "ngày hạ chí và ngày đông chí", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042381", "hw": "sportier", "pos": "adj", "ipa": "/ˈspɔːrtiər/", "vi": "thể thao hơn; năng động hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042382", "hw": "sportiest", "pos": "adj", "ipa": "/ˈspɔːrtiɪst/", "vi": "thể thao nhất; năng động nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042383", "hw": "staffers", "pos": "noun", "ipa": "/ˈstæfərz/", "vi": "các nhân viên trong cơ quan", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042384", "hw": "sterilizations", "pos": "noun", "ipa": "/ˌstɛrələˈzeɪʃənz/", "vi": "các ca triệt sản; khử trùng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042385", "hw": "supermodels", "pos": "noun", "ipa": "/ˈsuːpərmɑːdəlz/", "vi": "các siêu mẫu thời trang quốc tế", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042386", "hw": "susceptibilities", "pos": "noun", "ipa": "/səˌsɛptəˈbɪlətiz/", "vi": "độ nhạy cảm; tính dễ nhiễm bệnh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042387", "hw": "tabletops", "pos": "noun", "ipa": "/ˈteɪbəltɑːps/", "vi": "các mặt bàn phẳng", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042388", "hw": "thermostats", "pos": "noun", "ipa": "/ˈθɜːrməstæts/", "vi": "các bộ điều chỉnh nhiệt tự động", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042389", "hw": "tinglings", "pos": "noun", "ipa": "/ˈtɪŋɡlɪŋz/", "vi": "cảm giác râm ran như kiến bò", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042390", "hw": "tongas", "pos": "noun", "ipa": "/ˈtɑːŋɡəz/", "vi": "xe ngựa hai bánh tonga Ấn Độ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042391", "hw": "topekas", "pos": "noun", "ipa": "/təˈpiːkəz/", "vi": "thành phố Topeka thủ phủ Kansas", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042392", "hw": "torts", "pos": "noun", "ipa": "/tɔːrts/", "vi": "các hành vi vi phạm dân sự", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042393", "hw": "touchscreens", "pos": "noun", "ipa": "/ˈtʌtʃskriːnz/", "vi": "các màn hình cảm ứng điện tử", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042394", "hw": "tropes", "pos": "noun", "ipa": "/troʊps/", "vi": "các biện pháp tu từ ẩn dụ quen", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042395", "hw": "undercuts", "pos": "noun", "ipa": "/ˈʌndərkʌts/", "vi": "kiểu tóc cạo viền undercut", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042396", "hw": "undercutting", "pos": "verb", "ipa": "/ˌʌndərˈkʌtɪŋ/", "vi": "đang bán phá giá cạnh tranh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042397", "hw": "unfriendlier", "pos": "adj", "ipa": "/ʌnˈfrɛndliər/", "vi": "kém thân thiện hơn; xa cách hơn", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042398", "hw": "unfriendliest", "pos": "adj", "ipa": "/ʌnˈfrɛndliɪst/", "vi": "kém thân thiện nhất; xa cách nhất", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042399", "hw": "vials", "pos": "noun", "ipa": "/ˈvaɪəlz/", "vi": "những lọ thủy tinh nhỏ đựng thuốc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042400", "hw": "warlords", "pos": "noun", "ipa": "/ˈwɔːrlɔːrdz/", "vi": "các lãnh chúa quân phiệt", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.042401", "hw": "zionisms", "pos": "noun", "ipa": "/ˈzaɪənɪzəmz/", "vi": "các hệ phái chủ nghĩa Zion", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""}
]

with open('scratch/b29_r05_raw_p4.json') as f:
    raw = json.load(f)

assert len(items) == 100, f"Expected 100 items, got {len(items)}"
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}

for idx, (it, r) in enumerate(zip(items, raw)):
    assert it['id'] == r['id'], f"ID mismatch: {it['id']} vs {r['id']}"
    assert it['hw'] == r['hw'], f"HW mismatch: {it['hw']} vs {r['hw']}"
    assert it['pos'] in allowed_pos, f"Invalid POS {it['pos']} for {it['id']}"
    assert len(it['vi']) > 0, f"Empty VI for {it['id']}"
    assert len(it['vi']) <= 35, f"Invalid VI length ({len(it['vi'])}) for {it['id']}: {it['vi']}"
    if it['pos'] != 'phrase' and ' ' not in it['hw']:
        assert it['ipa'].startswith('/') and it['ipa'].endswith('/') and it['ipa'].count('/') == 2, f"Invalid IPA for {it['id']}: {it['ipa']}"

with open('scratch/b29_r05_p4.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"Batch 29 Round 5 Part 4 validated and written successfully. Total items: {len(items)}")
