import json

part1_data = [
  {"id": "lex.en.100k.096502", "hw": "obtund", "pos": "verb", "ipa": "/ɑːbˈtʌnd/", "vi": "làm dịu cơn đau; làm cùn bớt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096503", "hw": "obtundent", "pos": "noun", "ipa": "/ɑːbˈtʌndənt/", "vi": "chất làm dịu đau; thuốc gây tê", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096504", "hw": "obturate", "pos": "verb", "ipa": "/ˈɑːbtjʊreɪt/", "vi": "bịt kín buồng đạn; làm tắc kín", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096505", "hw": "obturation", "pos": "noun", "ipa": "/ˌɑːbtjʊˈreɪʃən/", "vi": "sự bịt kín hơi; sự trám kín", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096506", "hw": "obversion", "pos": "noun", "ipa": "/əbˈvɜːrʒən/", "vi": "phép đảo đổi mệnh đề logic", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096507", "hw": "obvert", "pos": "verb", "ipa": "/əbˈvɜːrt/", "vi": "đảo đổi mệnh đề; quay mặt trước", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096508", "hw": "obviated", "pos": "verb", "ipa": "/ˈɑːbvieɪtɪd/", "vi": "đã loại bỏ; đã hóa giải trở ngại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096509", "hw": "obviates", "pos": "verb", "ipa": "/ˈɑːbvieɪts/", "vi": "loại bỏ; hóa giải; ngăn ngừa sớm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096510", "hw": "obviation", "pos": "noun", "ipa": "/ˌɑːbviˈeɪʃən/", "vi": "sự loại bỏ; sự hóa giải ngăn ngừa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096511", "hw": "obvolute", "pos": "adj", "ipa": "/ˈɑːbvəluːt/", "vi": "cuốn gập xen kẽ nửa nọ nửa kia", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096512", "hw": "obvoluted", "pos": "adj", "ipa": "/ˈɑːbvəluːtɪd/", "vi": "có cánh hoa cuộn xếp xen kẽ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096513", "hw": "obvolution", "pos": "noun", "ipa": "/ˌɑːbvəˈluːʃən/", "vi": "cách sắp xếp cuộn xen kẽ nhau", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096514", "hw": "oc", "pos": "noun", "ipa": "/ˌoʊˈsiː/", "vi": "sĩ quan chỉ huy đơn vị OC", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096515", "hw": "occasionalism", "pos": "noun", "ipa": "/əˈkeɪʒənəlɪzəm/", "vi": "thuyết nhân duyên ngẫu phối", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096516", "hw": "occasionalist", "pos": "noun", "ipa": "/əˈkeɪʒənəlɪst/", "vi": "người theo thuyết ngẫu phối duyên", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096517", "hw": "occasionality", "pos": "noun", "ipa": "/əˌkeɪʒəˈnæləti/", "vi": "tính thỉnh thoảng; tính ngẫu nhiên", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096518", "hw": "occasioned", "pos": "verb", "ipa": "/əˈkeɪʒənd/", "vi": "đã gây ra; dấy lên sự kiện", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096519", "hw": "occasioning", "pos": "verb", "ipa": "/əˈkeɪʒənɪŋ/", "vi": "gây nên; làm dấy lên sự kiện", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096520", "hw": "occidentalise", "pos": "verb", "ipa": "/ˌɑːksɪˈdɛntəlaɪz/", "vi": "tây phương hóa; âu hóa lối sống", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096521", "hw": "occidentalist", "pos": "noun", "ipa": "/ˌɑːksɪˈdɛntəlɪst/", "vi": "nhà tây phương học; người âu hóa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096522", "hw": "occidentality", "pos": "noun", "ipa": "/ˌɑːksɪdɛnˈtæləti/", "vi": "đặc tính phương tây; bản sắc âu mỹ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096523", "hw": "occidentalization", "pos": "noun", "ipa": "/ˌɑːksɪˌdɛntəlaɪˈzeɪʃən/", "vi": "sự tây phương hóa; sự âu hóa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096524", "hw": "occidentalize", "pos": "verb", "ipa": "/ˌɑːksɪˈdɛntəlaɪz/", "vi": "tây phương hóa; theo lối sống tây", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096525", "hw": "occludent", "pos": "adj", "ipa": "/əˈkluːdənt/", "vi": "bịt kín; khép kín lối lại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096526", "hw": "occludes", "pos": "verb", "ipa": "/əˈkluːdz/", "vi": "bịt kín; làm nghẽn tắc mạch", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096527", "hw": "occluding", "pos": "verb", "ipa": "/əˈkluːdɪŋ/", "vi": "gây tắc nghẽn; bịt kín mạch máu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096528", "hw": "occlusor", "pos": "noun", "ipa": "/əˈkluːzɚ/", "vi": "cơ khép; cơ đóng nắp vỏ sò", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096529", "hw": "occultistic", "pos": "adj", "ipa": "/ˌɑːkʌlˈtɪstɪk/", "vi": "thuộc thuyết thần bí; ma thuật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096530", "hw": "occultly", "pos": "adv", "ipa": "/əˈkʌltli/", "vi": "một cách huyền bí; đầy bí hiểm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096531", "hw": "occultness", "pos": "noun", "ipa": "/əˈkʌltnəs/", "vi": "tính huyền bí; sự thâm sâu kỳ bí", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096532", "hw": "occulty", "pos": "noun", "ipa": "/əˈkʌlti/", "vi": "giới huyền thuật; giới thần bí", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096533", "hw": "occupancies", "pos": "noun", "ipa": "/ˈɑːkjəpənsiz/", "vi": "tỷ lệ lấp đầy; sự chiếm dụng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096534", "hw": "occupants", "pos": "noun", "ipa": "/ˈɑːkjəpənts/", "vi": "những người cư ngụ; hành khách ngồi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096535", "hw": "occupations", "pos": "noun", "ipa": "/ˌɑːkjəˈpeɪʃənz/", "vi": "các nghề nghiệp; cuộc chiếm đóng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096536", "hw": "occupies", "pos": "verb", "ipa": "/ˈɑːkjəpaɪz/", "vi": "chiếm lĩnh; chiếm đóng; cư ngụ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096537", "hw": "occurence", "pos": "noun", "ipa": "/əˈkɜːrəns/", "vi": "sự xảy ra; biến cố phát sinh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096538", "hw": "occurred", "pos": "verb", "ipa": "/əˈkɜːrd/", "vi": "đã diễn ra; đã xảy đến bất ngờ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096539", "hw": "occurrences", "pos": "noun", "ipa": "/əˈkɜːrənsɪz/", "vi": "các sự cố; những lần xảy ra", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096540", "hw": "occurring", "pos": "verb", "ipa": "/əˈkɜːrɪŋ/", "vi": "đang diễn ra; đang xảy đến", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096541", "hw": "occurs", "pos": "verb", "ipa": "/əˈkɜːrz/", "vi": "xảy ra; xuất hiện; tồn tại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096542", "hw": "oceanaria", "pos": "noun", "ipa": "/ˌoʊʃəˈnɛriə/", "vi": "các thủy cung biển nhân tạo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096543", "hw": "oceanarium", "pos": "noun", "ipa": "/ˌoʊʃəˈnɛriəm/", "vi": "thủy cung đại dương; hồ nuôi thú", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096544", "hw": "oceanaut", "pos": "noun", "ipa": "/ˈoʊʃənɔːt/", "vi": "nhà thám hiểm đại dương sâu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096545", "hw": "oceanian", "pos": "adj", "ipa": "/ˌoʊʃiˈænɪən/", "vi": "thuộc về châu Đại Dương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096546", "hw": "oceanid", "pos": "noun", "ipa": "/oʊˈsiːənɪd/", "vi": "nàng tiên biển Oceanid Hy Lạp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096547", "hw": "oceanites", "pos": "noun", "ipa": "/ˌoʊʃiəˈnaɪtiːz/", "vi": "chi chim hải âu bão Oceanites", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096548", "hw": "oceanographers", "pos": "noun", "ipa": "/ˌoʊʃəˈnɑːɡrəfɚz/", "vi": "các nhà hải dương học", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096549", "hw": "oceanographic", "pos": "adj", "ipa": "/ˌoʊʃənəˈɡræfɪk/", "vi": "thuộc về ngành hải dương học", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096550", "hw": "oceanographical", "pos": "adj", "ipa": "/ˌoʊʃənəˈɡræfɪkəl/", "vi": "thuộc hải dương học; biển cả", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096551", "hw": "oceanographically", "pos": "adv", "ipa": "/ˌoʊʃənəˈɡræfɪkli/", "vi": "về phương diện hải dương học", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096552", "hw": "oceanophilous", "pos": "adj", "ipa": "/ˌoʊʃəˈnɑːfɪləs/", "vi": "ưa sống vùng biển mở đại dương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096553", "hw": "oceanward", "pos": "adv", "ipa": "/ˈoʊʃənwɚd/", "vi": "hướng ra đại dương; về phía biển", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096554", "hw": "oceanwards", "pos": "adv", "ipa": "/ˈoʊʃənwɚdz/", "vi": "về phía biển khơi; hướng ra biển", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096555", "hw": "ocellar", "pos": "adj", "ipa": "/oʊˈsɛlɚ/", "vi": "thuộc mắt đơn ở sâu bọ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096556", "hw": "ocellate", "pos": "adj", "ipa": "/ˈɑːsəleɪt/", "vi": "có đốm hình mắt; có mắt đơn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096557", "hw": "ocellation", "pos": "noun", "ipa": "/ˌɑːsəˈleɪʃən/", "vi": "đốm tròn hình mắt trên cánh", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096558", "hw": "ocelli", "pos": "noun", "ipa": "/oʊˈsɛlaɪ/", "vi": "các mắt đơn côn trùng; đốm mắt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096559", "hw": "ocelliferous", "pos": "adj", "ipa": "/ˌɑːsəˈlɪfərəs/", "vi": "mang đốm hình mắt; có mắt đơn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096560", "hw": "ocelligerous", "pos": "adj", "ipa": "/ˌɑːsəˈlɪdʒərəs/", "vi": "có đốm mắt trên cánh bướm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096561", "hw": "och", "pos": "intj", "ipa": "/ɔːx/", "vi": "ôi chao; trời ơi thốt lên", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096562", "hw": "oche", "pos": "noun", "ipa": "/ˈɑːki/", "vi": "vạch ném phi tiêu oche", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096563", "hw": "ocherous", "pos": "adj", "ipa": "/ˈoʊkərəs/", "vi": "có màu đất son; chứa thổ hoàng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096564", "hw": "ochery", "pos": "adj", "ipa": "/ˈoʊkəri/", "vi": "nhuốm màu đất son; như thổ hoàng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096565", "hw": "ochlesis", "pos": "noun", "ipa": "/ɑːkˈliːsɪs/", "vi": "bệnh do chen chúc đông người", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096566", "hw": "ochlocracy", "pos": "noun", "ipa": "/ɑːkˈlɑːkrəsi/", "vi": "chính thể bạo dân chuyên chế", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096567", "hw": "ochlocrat", "pos": "noun", "ipa": "/ˈɑːkləkræt/", "vi": "kẻ mị dân kích động bạo dân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096568", "hw": "ochlocratic", "pos": "adj", "ipa": "/ˌɑːkləˈkrætɪk/", "vi": "thuộc nền thống trị bạo dân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096569", "hw": "ochlocratical", "pos": "adj", "ipa": "/ˌɑːkləˈkrætɪkəl/", "vi": "mang tính bạo dân chuyên chế", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096570", "hw": "ochna", "pos": "noun", "ipa": "/ˈɑːknə/", "vi": "chi hoa mai vàng Ochna", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096571", "hw": "ochnaceae", "pos": "noun", "ipa": "/ɑːkˈneɪsiːiː/", "vi": "họ mai vàng Ochnaceae", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096572", "hw": "ochotona", "pos": "noun", "ipa": "/ˌoʊkəˈtoʊnə/", "vi": "chi thỏ cộc Pika Ochotona", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096573", "hw": "ochotonidae", "pos": "noun", "ipa": "/ˌoʊkətəˈnɪdiː/", "vi": "họ thỏ cộc Ochotonidae", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096574", "hw": "ochraceous", "pos": "adj", "ipa": "/oʊˈkreɪʃəs/", "vi": "có màu vàng đất son; thổ hoàng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096575", "hw": "ochrea", "pos": "noun", "ipa": "/ˈoʊkriə/", "vi": "bẹ chìa ở gốc cuống lá", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096576", "hw": "ochreate", "pos": "adj", "ipa": "/ˈoʊkrieɪt/", "vi": "có bẹ chìa bao quanh thân cành", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096577", "hw": "ochreish", "pos": "adj", "ipa": "/ˈoʊkrɪʃ/", "vi": "hơi có sắc vàng đất son", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096578", "hw": "ochreous", "pos": "adj", "ipa": "/ˈoʊkriəs/", "vi": "chứa quặng đất son; sắc thổ hoàng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096579", "hw": "ochroid", "pos": "adj", "ipa": "/ˈoʊkrɔɪd/", "vi": "có màu tựa đất son vàng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096580", "hw": "ochroma", "pos": "noun", "ipa": "/oʊˈkroʊmə/", "vi": "chi cây gỗ nhẹ balsa Ochroma", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096581", "hw": "ochronosis", "pos": "noun", "ipa": "/ˌoʊkrəˈnoʊsɪs/", "vi": "bệnh sẫm màu mô xương ochronosis", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096582", "hw": "ochrous", "pos": "adj", "ipa": "/ˈoʊkrəs/", "vi": "mang sắc vàng thổ hoàng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096583", "hw": "ochry", "pos": "adj", "ipa": "/ˈoʊkri/", "vi": "nhuốm màu đất son rực rỡ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096584", "hw": "ocrea", "pos": "noun", "ipa": "/ˈoʊkriə/", "vi": "bẹ chìa thực vật học", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096585", "hw": "ocreaceous", "pos": "adj", "ipa": "/ˌoʊkriˈeɪʃəs/", "vi": "có cấu tạo giống bẹ chìa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096586", "hw": "ocreae", "pos": "noun", "ipa": "/ˈoʊkriiː/", "vi": "những bẹ chìa bảo vệ chồi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096587", "hw": "ocreate", "pos": "adj", "ipa": "/ˈoʊkrieɪt/", "vi": "được bao bọc bởi bẹ chìa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096588", "hw": "octachord", "pos": "noun", "ipa": "/ˈɑːktəkɔːrd/", "vi": "nhạc cụ tám dây; điệu tám âm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096589", "hw": "octachordal", "pos": "adj", "ipa": "/ˌɑːktəˈkɔːrdəl/", "vi": "thuộc thang âm hệ tám nốt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096590", "hw": "octactinal", "pos": "adj", "ipa": "/ˌɑːktækˈtaɪnəl/", "vi": "có gai tám tia tỏa tròn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096591", "hw": "octad", "pos": "noun", "ipa": "/ˈɑːktæd/", "vi": "bộ tám đơn vị; nhóm tám nguyên tố", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096592", "hw": "octagonally", "pos": "adv", "ipa": "/ɑːkˈtæɡənəli/", "vi": "theo hình dáng bát giác", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096593", "hw": "octagynous", "pos": "adj", "ipa": "/ɑːkˈtædʒɪnəs/", "vi": "có hoa mang tám nhụy cái", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096594", "hw": "octahedral", "pos": "adj", "ipa": "/ˌɑːktəˈhiːdrəl/", "vi": "có hình bát diện tám mặt đều", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096595", "hw": "octamerous", "pos": "adj", "ipa": "/ɑːkˈtæmərəs/", "vi": "có cấu tạo gồm tám phần", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096596", "hw": "octameter", "pos": "noun", "ipa": "/ɑːkˈtæmɪtɚ/", "vi": "thể thơ tám nhịp phách mỗi dòng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096597", "hw": "octandrous", "pos": "adj", "ipa": "/ɑːkˈtændrəs/", "vi": "có hoa mang tám nhị đực", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096598", "hw": "octangle", "pos": "noun", "ipa": "/ˈɑːktæŋɡəl/", "vi": "hình bát giác; hình tám góc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096599", "hw": "octangular", "pos": "adj", "ipa": "/ɑːkˈtæŋɡjəlɚ/", "vi": "có tám góc; thuộc hình bát giác", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096600", "hw": "octans", "pos": "noun", "ipa": "/ˈɑːktænz/", "vi": "chòm sao Nam Cực Bát Phân Nghi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096601", "hw": "octants", "pos": "noun", "ipa": "/ˈɑːktənts/", "vi": "những góc phần tám; kính bát phân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
]

assert len(part1_data) == 100, f"Expected 100 items, got {len(part1_data)}"

valid_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}

with open("scratch/b20_r04_raw_p1.json") as f:
    raw_p1 = json.load(f)

for i, (item, raw) in enumerate(zip(part1_data, raw_p1)):
    assert item["id"] == raw["id"], f"ID mismatch at {i}: {item['id']} vs {raw['id']}"
    assert item["hw"] == raw["hw"], f"HW mismatch at {i}: {item['hw']} vs {raw['hw']}"
    assert item["pos"] in valid_pos, f"Invalid POS at {i}: {item['pos']}"
    assert item["ipa"].startswith("/") and item["ipa"].endswith("/"), f"Invalid IPA slashes at {i}: {item['ipa']}"
    assert item["ipa"].count("/") == 2, f"IPA does not have exactly 2 slashes at {i}: {item['ipa']}"
    assert not item["ipa"].startswith("/ ") and not item["ipa"].endswith(" /"), f"IPA boundary spaces at {i}: {item['ipa']}"
    assert len(item["vi"]) <= 35, f"vi too long at {i} ({item['hw']}): {item['vi']} (len={len(item['vi'])})"
    assert len(item["vi"]) > 0, f"Empty vi at {i}"
    assert not any(art in item["vi"] for art in ["Số nhiều", "Xem ", "Dạng ", "Viết tắt", "Động từ chia", "%%"]), f"Crawler artifact in vi at {i}: {item['vi']}"
    assert item["status"] == "reviewed", f"Status not reviewed at {i}"

with open("scratch/b20_r04_p1.json", "w") as f:
    json.dump(part1_data, f, ensure_ascii=False, indent=2)

print("Batch 20 Round 4 Part 1 validated and saved successfully!")
