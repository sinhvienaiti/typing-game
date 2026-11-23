import json

# Part 1: records 3500 - 3599 (IDs 083502 - 083601)
p1_data = [
    {"id": "lex.en.100k.083502", "hw": "harangues", "pos": "verb", "ipa": "/həˈræŋz/", "vi": "lên giọng thuyết giáo; diễn thuyết", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083503", "hw": "haranguing", "pos": "verb", "ipa": "/həˈræŋɪŋ/", "vi": "lớn tiếng thuyết giáo; mắng mỏ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083504", "hw": "haras", "pos": "noun", "ipa": "/ˈhærəs/", "vi": "trại nhân giống ngựa; trại ngựa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083505", "hw": "harasses", "pos": "verb", "ipa": "/həˈræsɪz/", "vi": "quấy rối; làm phiền; sách nhiễu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083506", "hw": "harassing", "pos": "verb", "ipa": "/həˈræsɪŋ/", "vi": "quấy rối; làm phiền; sách nhiễu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083507", "hw": "harbourage", "pos": "noun", "ipa": "/ˈhɑːrbərɪdʒ/", "vi": "nơi trú ẩn; chỗ neo đậu tàu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083508", "hw": "harboured", "pos": "verb", "ipa": "/ˈhɑːrbərd/", "vi": "đã ấp ủ; đã chứa chấp; che giấu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083509", "hw": "harbouring", "pos": "verb", "ipa": "/ˈhɑːrbərɪŋ/", "vi": "ấp ủ; chứa chấp; che giấu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083510", "hw": "harbours", "pos": "noun", "ipa": "/ˈhɑːrbərz/", "vi": "các bến cảng; nơi neo đậu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083511", "hw": "hardbacked", "pos": "adj", "ipa": "/ˈhɑːrdbækt/", "vi": "có bìa cứng; bìa cứng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083512", "hw": "hardbacks", "pos": "noun", "ipa": "/ˈhɑːrdbæks/", "vi": "những cuốn sách bìa cứng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083513", "hw": "hardbake", "pos": "noun", "ipa": "/ˈhɑːrdbeɪk/", "vi": "kẹo giòn mật mía hạnh nhân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083514", "hw": "hardbitten", "pos": "adj", "ipa": "/ˌhɑːrdˈbɪtən/", "vi": "dày dạn kinh nghiệm; cứng rắn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083515", "hw": "hardboot", "pos": "noun", "ipa": "/ˈhɑːrdbuːt/", "vi": "đôi ủng cứng; người bảo thủ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083516", "hw": "harddrive", "pos": "noun", "ipa": "/ˈhɑːrddraɪv/", "vi": "ổ đĩa cứng máy tính", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083517", "hw": "harddrives", "pos": "noun", "ipa": "/ˈhɑːrddraɪvz/", "vi": "các ổ đĩa cứng máy tính", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083518", "hw": "hardenbergia", "pos": "noun", "ipa": "/ˌhɑːrdənˈbɜːrdʒiə/", "vi": "chi dây leo Hardenbergia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083519", "hw": "hardener", "pos": "noun", "ipa": "/ˈhɑːrdnər/", "vi": "chất làm cứng; chất tôi cứng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083520", "hw": "hardens", "pos": "verb", "ipa": "/ˈhɑːrdənz/", "vi": "làm cứng; trở nên cứng rắn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083521", "hw": "hardest", "pos": "adj", "ipa": "/ˈhɑːrdɪst/", "vi": "khó nhất; cứng nhất; chăm nhất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083522", "hw": "hardfisted", "pos": "adj", "ipa": "/ˌhɑːrdˈfɪstɪd/", "vi": "keo kiệt bủn xỉn; sắt đá", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083523", "hw": "hardhead", "pos": "noun", "ipa": "/ˈhɑːrdhed/", "vi": "kẻ cứng đầu bướng bỉnh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083524", "hw": "hardheartedness", "pos": "noun", "ipa": "/ˌhɑːrdˈhɑːrtɪdnəs/", "vi": "sự nhẫn tâm; tính sắt đá tàn nhẫn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083525", "hw": "hardily", "pos": "adv", "ipa": "/ˈhɑːrdɪli/", "vi": "một cách táo bạo; gan góc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083526", "hw": "hardiment", "pos": "noun", "ipa": "/ˈhɑːrdɪmənt/", "vi": "lòng dũng cảm; sự táo bạo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083527", "hw": "hardinggrass", "pos": "noun", "ipa": "/ˈhɑːrdɪŋɡræs/", "vi": "cỏ Harding; cỏ bồ hoàng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083528", "hw": "hardmouthed", "pos": "adj", "ipa": "/ˌhɑːrdˈmaʊðd/", "vi": "bướng bỉnh lì lợm; khó ghìm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083529", "hw": "hardnesses", "pos": "noun", "ipa": "/ˈhɑːrdnəsɪz/", "vi": "các độ cứng; mức độ cứng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083530", "hw": "hardpoint", "pos": "noun", "ipa": "/ˈhɑːrdpɔɪnt/", "vi": "giá treo vũ khí máy bay", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083531", "hw": "hardshell", "pos": "adj", "ipa": "/ˈhɑːrdʃel/", "vi": "vỏ cứng; bảo thủ cứng rắn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083532", "hw": "hardships", "pos": "noun", "ipa": "/ˈhɑːrdʃɪps/", "vi": "những gian nan khốn khó; cơ cực", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083533", "hw": "hardstanding", "pos": "noun", "ipa": "/ˈhɑːrdˌstændɪŋ/", "vi": "bãi đỗ nền bê tông cứng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083534", "hw": "hardwareman", "pos": "noun", "ipa": "/ˈhɑːrdwermən/", "vi": "người bán đồ kim khí", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083535", "hw": "hardwoods", "pos": "noun", "ipa": "/ˈhɑːrdwʊdz/", "vi": "các loại gỗ cứng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083536", "hw": "harefoot", "pos": "noun", "ipa": "/ˈherfʊt/", "vi": "cây cỏ ba lá chân thỏ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083537", "hw": "harelipped", "pos": "adj", "ipa": "/ˈherlɪpt/", "vi": "bị tật sứt môi; hở hàm ếch", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083538", "hw": "harful", "pos": "noun", "ipa": "/ˈhɑːrfəl/", "vi": "mũ trùm; lượng đầy nắm tay", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083539", "hw": "harikari", "pos": "noun", "ipa": "/ˌhɑːrɪˈkɑːri/", "vi": "mổ bụng tự sát hara-kiri", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083540", "hw": "harked", "pos": "verb", "ipa": "/hɑːrkt/", "vi": "đã lắng nghe; nhắc lại chuyện cũ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083541", "hw": "harking", "pos": "verb", "ipa": "/ˈhɑːrkɪŋ/", "vi": "đang lắng nghe; quay lại vấn đề", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083542", "hw": "harks", "pos": "verb", "ipa": "/hɑːrks/", "vi": "lắng nghe; quay lại chuyện cũ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083543", "hw": "harl", "pos": "noun", "ipa": "/hɑːrl/", "vi": "sợi lông tơ làm mồi câu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083544", "hw": "harle", "pos": "noun", "ipa": "/hɑːrl/", "vi": "vịt mào merganser; sợi xơ gai", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083545", "hw": "harmed", "pos": "verb", "ipa": "/hɑːrmd/", "vi": "đã gây hại; đã làm tổn thương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083546", "hw": "harming", "pos": "verb", "ipa": "/ˈhɑːrmɪŋ/", "vi": "gây tổn hại; làm tổn thương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083547", "hw": "harmlessness", "pos": "noun", "ipa": "/ˈhɑːrmləsnəs/", "vi": "tính vô hại; sự lành tính", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083548", "hw": "harmonical", "pos": "adj", "ipa": "/hɑːrˈmɑːnɪkəl/", "vi": "thuộc hòa âm; hài hòa cân đối", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083549", "hw": "harmonies", "pos": "noun", "ipa": "/ˈhɑːrməniz/", "vi": "những giai điệu hòa âm; hòa hợp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083550", "hw": "harmoniousness", "pos": "noun", "ipa": "/hɑːrˈmoʊniəsnəs/", "vi": "tính hòa hợp; sự du dương êm tai", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083551", "hw": "harmoniser", "pos": "noun", "ipa": "/ˈhɑːrmənaɪzər/", "vi": "người hòa giải; người phối âm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083552", "hw": "harmonises", "pos": "verb", "ipa": "/ˈhɑːrmənaɪzɪz/", "vi": "hòa hợp; làm cho ăn khớp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083553", "hw": "harmonising", "pos": "verb", "ipa": "/ˈhɑːrmənaɪzɪŋ/", "vi": "hòa hợp; làm cho hòa hợp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083554", "hw": "harmonist", "pos": "noun", "ipa": "/ˈhɑːrmənɪst/", "vi": "chuyên gia hòa âm; người phối âm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083555", "hw": "harmonizable", "pos": "adj", "ipa": "/ˈhɑːrmənaɪzəbəl/", "vi": "có thể hòa hợp; có thể ăn khớp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083556", "hw": "harmonizes", "pos": "verb", "ipa": "/ˈhɑːrmənaɪzɪz/", "vi": "hòa hợp; làm cho hài hòa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083557", "hw": "harmonizing", "pos": "verb", "ipa": "/ˈhɑːrmənaɪzɪŋ/", "vi": "làm cho hài hòa; hòa điệu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083558", "hw": "harmotome", "pos": "noun", "ipa": "/ˈhɑːrmətoʊm/", "vi": "khoáng vật harmotome", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083559", "hw": "harms", "pos": "verb", "ipa": "/hɑːrmz/", "vi": "làm hại; gây tổn thương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083560", "hw": "harnesses", "pos": "verb", "ipa": "/ˈhɑːrnəsɪz/", "vi": "khai thác; đóng yên cương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083561", "hw": "harnessing", "pos": "verb", "ipa": "/ˈhɑːrnəsɪŋ/", "vi": "khai thác nguồn lực; thắng cương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083562", "hw": "harpan", "pos": "noun", "ipa": "/ˈhɑːrpən/", "vi": "tầng đất chai cứng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083563", "hw": "harped", "pos": "verb", "ipa": "/hɑːrpt/", "vi": "chơi đàn hạc; nói đi nói lại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083564", "hw": "harpery", "pos": "noun", "ipa": "/ˈhɑːrpəri/", "vi": "tiếng gảy đàn hạc; đàn hạc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083565", "hw": "harpia", "pos": "noun", "ipa": "/hɑːrˈpaɪə/", "vi": "chi đại bàng Harpia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083566", "hw": "harping", "pos": "verb", "ipa": "/ˈhɑːrpɪŋ/", "vi": "chơi đàn hạc; lải nhải nhắc lại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083567", "hw": "harpooned", "pos": "verb", "ipa": "/hɑːrˈpuːnd/", "vi": "đã phóng lao móc cá", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083568", "hw": "harpooneer", "pos": "noun", "ipa": "/ˌhɑːrpuːˈnɪr/", "vi": "người phóng lao móc cá voi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083569", "hw": "harpooning", "pos": "verb", "ipa": "/hɑːrˈpuːnɪŋ/", "vi": "phóng lao móc bắt cá", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083570", "hw": "harpoons", "pos": "noun", "ipa": "/hɑːrˈpuːnz/", "vi": "những chiếc lao móc săn cá", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083571", "hw": "harps", "pos": "noun", "ipa": "/hɑːrps/", "vi": "những cây đàn hạc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083572", "hw": "harpulla", "pos": "noun", "ipa": "/hɑːrˈpʊlə/", "vi": "cây bồ hòn Harpullia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083573", "hw": "harpullia", "pos": "noun", "ipa": "/hɑːrˈpʊliə/", "vi": "chi bồ hòn Harpullia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083574", "hw": "harquebus", "pos": "noun", "ipa": "/ˈhɑːrkəbəs/", "vi": "khẩu súng hỏa mai cổ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083575", "hw": "harquebusier", "pos": "noun", "ipa": "/ˌhɑːrkəbəˈsɪr/", "vi": "lính bắn súng hỏa mai", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083576", "hw": "harries", "pos": "verb", "ipa": "/ˈhæriz/", "vi": "quấy nhiễu; cướp phá phiền toái", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083577", "hw": "harrisia", "pos": "noun", "ipa": "/həˈrɪsiə/", "vi": "chi xương rồng táo Harrisia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083578", "hw": "harrowed", "pos": "verb", "ipa": "/ˈhæroʊd/", "vi": "đã bừa đất; làm đau đớn khổ sở", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083579", "hw": "harrows", "pos": "noun", "ipa": "/ˈhæroʊz/", "vi": "những chiếc bừa đất ruộng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083580", "hw": "harrumph", "pos": "verb", "ipa": "/həˈrʌmf/", "vi": "hắng giọng tỏ vẻ bất bình", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083581", "hw": "harrumphed", "pos": "verb", "ipa": "/həˈrʌmft/", "vi": "đã hắng giọng cằn nhằn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083582", "hw": "harrumphing", "pos": "verb", "ipa": "/həˈrʌmfɪŋ/", "vi": "đang hắng giọng càu nhàu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083583", "hw": "harrumphs", "pos": "verb", "ipa": "/həˈrʌmfs/", "vi": "hắng giọng khó chịu; càu nhàu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083584", "hw": "harrying", "pos": "verb", "ipa": "/ˈhæriɪŋ/", "vi": "quấy rối liên tục; quấy phá", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083585", "hw": "harshen", "pos": "verb", "ipa": "/ˈhɑːrʃən/", "vi": "làm khắc nghiệt hơn; gay gắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083586", "hw": "harslet", "pos": "noun", "ipa": "/ˈhæslɪt/", "vi": "món lòng nội tạng lợn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083587", "hw": "hartal", "pos": "noun", "ipa": "/hɑːrˈtɑːl/", "vi": "cuộc tổng đình công phản đối", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083588", "hw": "hartshorn", "pos": "noun", "ipa": "/ˈhɑːrtsˌhɔːrn/", "vi": "bột gạc hươu; muối amoniac", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083589", "hw": "haruspex", "pos": "noun", "ipa": "/həˈrʌspeks/", "vi": "thầy bói xem nội tạng súc vật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083590", "hw": "haruspication", "pos": "noun", "ipa": "/həˌrʌspɪˈkeɪʃən/", "vi": "thuật bói xem nội tạng tế lễ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083591", "hw": "harversack", "pos": "noun", "ipa": "/ˈhævərsæk/", "vi": "túi dết đeo chéo; ba lô vải", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083592", "hw": "harvestfish", "pos": "noun", "ipa": "/ˈhɑːrvɪstfɪʃ/", "vi": "cá bơ biển Bắc Mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083593", "hw": "harvestmen", "pos": "noun", "ipa": "/ˈhɑːrvɪstmən/", "vi": "loài nhện chân dài harvestmen", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083594", "hw": "has", "pos": "verb", "ipa": "/hæz/", "vi": "có; sở hữu; trải qua", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083595", "hw": "haschisch", "pos": "noun", "ipa": "/ˈhæʃiːʃ/", "vi": "nhựa cần sa; thuốc phiện hasit", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083596", "hw": "hashed", "pos": "verb", "ipa": "/hæʃt/", "vi": "đã băm nhỏ; đã băm dữ liệu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083597", "hw": "hasher", "pos": "noun", "ipa": "/ˈhæʃər/", "vi": "dao băm thịt; nhân viên quán ăn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083598", "hw": "hashes", "pos": "noun", "ipa": "/ˈhæʃɪz/", "vi": "món thịt băm; chuỗi mã băm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083599", "hw": "hashing", "pos": "verb", "ipa": "/ˈhæʃɪŋ/", "vi": "băm nhỏ; tính toán hàm băm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083600", "hw": "hashmark", "pos": "noun", "ipa": "/ˈhæʃmɑːrk/", "vi": "vạch chuẩn sân cỏ; vạch cấp hiệu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.100k.083601", "hw": "hasley", "pos": "noun", "ipa": "/ˈhæzli/", "vi": "tên riêng Hasley", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
]

# Quick sanity check
assert len(p1_data) == 100, f"Expected 100 items, got {len(p1_data)}"
with open("scratch/b17_r08_raw_p1.json") as f:
    raw = json.load(f)

raw_map = {x["id"]: x for x in raw}
for x in p1_data:
    assert x["id"] in raw_map, f"Missing {x['id']}"
    assert x["hw"] == raw_map[x["id"]]["hw"], f"HW mismatch {x['hw']} vs {raw_map[x['id']]['hw']}"
    assert len(x["vi"]) <= 35, f"VI too long ({len(x['vi'])}): {x['vi']} for {x['hw']}"
    assert x["ipa"].startswith("/") and x["ipa"].endswith("/") and x["ipa"].count("/") == 2, f"IPA format error: {x['ipa']} for {x['hw']}"
    assert x["status"] == "reviewed"
    assert x["pos"] in ["noun", "verb", "adj", "adv", "intj", "prep", "pron", "conj", "det", "num"]
    # Check cefr/tier/notes match raw
    assert x["cefr"] == raw_map[x["id"]]["cefr"], f"CEFR mismatch for {x['hw']}"
    assert x["tier"] == raw_map[x["id"]]["tier"], f"TIER mismatch for {x['hw']}"
    assert x["notes"] == raw_map[x["id"]]["notes"], f"NOTES mismatch for {x['hw']}"

print("All 100 records in Part 1 verified successfully!")
