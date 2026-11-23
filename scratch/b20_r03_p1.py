import json

part1_data = [
  {"id": "lex.en.100k.096002", "hw": "nonreflective", "pos": "adj", "ipa": "/ˌnɑnrɪˈflɛktɪv/", "vi": "không phản chiếu; phi phản xạ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096003", "hw": "nonrelativistic", "pos": "adj", "ipa": "/ˌnɑnˌrɛlətɪˈvɪstɪk/", "vi": "phi tương đối tính; phi tương đối", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096004", "hw": "nonreligious", "pos": "adj", "ipa": "/ˌnɑnrɪˈlɪdʒəs/", "vi": "không theo tôn giáo; phi tôn giáo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096005", "hw": "nonremittal", "pos": "noun", "ipa": "/ˌnɑnrɪˈmɪtəl/", "vi": "sự không chuyển tiền; sự vỡ nợ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096006", "hw": "nonrepetitive", "pos": "adj", "ipa": "/ˌnɑnrɪˈpɛtətɪv/", "vi": "không lặp lại; không trùng lặp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096007", "hw": "nonrepresentational", "pos": "adj", "ipa": "/ˌnɑnˌrɛprɪzɛnˈteɪʃənəl/", "vi": "trừu tượng; phi tả thực", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096008", "hw": "nonrepresentative", "pos": "adj", "ipa": "/ˌnɑnˌrɛprɪˈzɛntətɪv/", "vi": "không đại diện; không tiêu biểu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096009", "hw": "nonresilient", "pos": "adj", "ipa": "/ˌnɑnrɪˈzɪliənt/", "vi": "không đàn hồi; kém kiên cường", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096010", "hw": "nonresinous", "pos": "adj", "ipa": "/ˌnɑnˈrɛzənəs/", "vi": "không chứa nhựa cây; phi nhựa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096011", "hw": "nonresiny", "pos": "adj", "ipa": "/ˌnɑnˈrɛzɪni/", "vi": "không dính nhựa; phi nhựa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096012", "hw": "nonresistant", "pos": "adj", "ipa": "/ˌnɑnrɪˈzɪstənt/", "vi": "không kháng cự; dễ tổn thương", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096013", "hw": "nonresonant", "pos": "adj", "ipa": "/ˌnɑnˈrɛzənənt/", "vi": "không vang vọng; không cộng hưởng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096014", "hw": "nonreticulate", "pos": "adj", "ipa": "/ˌnɑnrɪˈtɪkjələt/", "vi": "không có dạng lưới; phi lưới", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096015", "hw": "nonretractable", "pos": "adj", "ipa": "/ˌnɑnrɪˈtræktəbəl/", "vi": "không thu vào được; cố định", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096016", "hw": "nonretractile", "pos": "adj", "ipa": "/ˌnɑnrɪˈtræktəl/", "vi": "không thể thụt vào; không co rụt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096017", "hw": "nonreversible", "pos": "adj", "ipa": "/ˌnɑnrɪˈvɜːrsəbəl/", "vi": "bất thuận nghịch; không đảo ngược", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096018", "hw": "nonrhythmic", "pos": "adj", "ipa": "/ˌnɑnˈrɪðmɪk/", "vi": "không có nhịp điệu; phi nhịp", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096019", "hw": "nonrigid", "pos": "adj", "ipa": "/ˌnɑnˈrɪdʒɪd/", "vi": "không cứng; linh hoạt; mềm dẻo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096020", "hw": "nonruminant", "pos": "adj", "ipa": "/ˌnɑnˈruːmɪnənt/", "vi": "không nhai lại; phi nhai lại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096021", "hw": "nonsegmental", "pos": "adj", "ipa": "/ˌnɑnsɛɡˈmɛntəl/", "vi": "không phân đoạn; không chia đốt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096022", "hw": "nonsegregated", "pos": "adj", "ipa": "/ˌnɑnˈsɛɡrɪɡeɪtɪd/", "vi": "không phân biệt chủng tộc; hòa nhập", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096023", "hw": "nonsensicality", "pos": "noun", "ipa": "/ˌnɑnsɛnˈsɪkələti/", "vi": "điều vô nghĩa; tính chất vô lý", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096024", "hw": "nonsensically", "pos": "adv", "ipa": "/ˌnɑnˈsɛnsɪkli/", "vi": "một cách vô lý; ngớ ngẩn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096025", "hw": "nonsensicalness", "pos": "noun", "ipa": "/ˌnɑnˈsɛnsɪkəlnəs/", "vi": "tính chất vô lý; sự vô nghĩa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096026", "hw": "nonsensitive", "pos": "adj", "ipa": "/ˌnɑnˈsɛnsətɪv/", "vi": "không nhạy cảm; không tuyệt mật", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096027", "hw": "nonsesuch", "pos": "noun", "ipa": "/ˈnʌnˌsʌtʃ/", "vi": "vật độc nhất vô nhị; kiệt xuất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096028", "hw": "nonsingular", "pos": "adj", "ipa": "/ˌnɑnˈsɪŋɡjəlɚ/", "vi": "khả nghịch; không suy biến", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096029", "hw": "nonslippery", "pos": "adj", "ipa": "/ˌnɑnˈslɪpəri/", "vi": "không trơn trượt; có độ bám", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096030", "hw": "nonsocial", "pos": "adj", "ipa": "/ˌnɑnˈsoʊʃəl/", "vi": "phi xã hội; không có tính bầy đàn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096031", "hw": "nonsovereign", "pos": "adj", "ipa": "/ˌnɑnˈsɑːvrən/", "vi": "không có chủ quyền; phi chủ quyền", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096032", "hw": "nonspatial", "pos": "adj", "ipa": "/ˌnɑnˈspeɪʃəl/", "vi": "phi không gian; ngoài không gian", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096033", "hw": "nonspeaking", "pos": "adj", "ipa": "/ˌnɑnˈspiːkɪŋ/", "vi": "không nói; vai phụ không lời thoại", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096034", "hw": "nonspecifically", "pos": "adv", "ipa": "/ˌnɑnspəˈsɪfɪkli/", "vi": "một cách chung chung; không cụ thể", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096035", "hw": "nonspherical", "pos": "adj", "ipa": "/ˌnɑnˈsfɛrɪkəl/", "vi": "không có dạng hình cầu; phi cầu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096036", "hw": "nonsteroid", "pos": "noun", "ipa": "/ˌnɑnˈstɪrɔɪd/", "vi": "chất phi steroid; thuốc kháng viêm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096037", "hw": "nonsubjective", "pos": "adj", "ipa": "/ˌnɑnsəbˈdʒɛktɪv/", "vi": "khách quan; không thiên vị cá nhân", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096038", "hw": "nonsubmergible", "pos": "adj", "ipa": "/ˌnɑnsəbˈmɜːrdʒəbəl/", "vi": "không thể chìm; không lặn được", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096039", "hw": "nonsubmersible", "pos": "adj", "ipa": "/ˌnɑnsəbˈmɜːrsəbəl/", "vi": "không thể chìm; không lặn ngầm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096040", "hw": "nonsuit", "pos": "noun", "ipa": "/ˈnɑːnsuːt/", "vi": "sự đình chỉ vụ kiện; xử hủy kiện", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096041", "hw": "nonsuppurative", "pos": "adj", "ipa": "/ˌnɑnˈsʌpjərətɪv/", "vi": "không mưng mủ; phi tạo mủ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096042", "hw": "nonsweet", "pos": "adj", "ipa": "/ˌnɑnˈswiːt/", "vi": "không ngọt; lạt; không có vị ngọt", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096043", "hw": "nonsyllabic", "pos": "adj", "ipa": "/ˌnɑnsɪˈlæbɪk/", "vi": "không tạo âm tiết; phi âm tiết", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096044", "hw": "nonsymbiotic", "pos": "adj", "ipa": "/ˌnɑnˌsɪmbaɪˈɑːtɪk/", "vi": "không cộng sinh; sống độc lập", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096045", "hw": "nonsynchronous", "pos": "adj", "ipa": "/ˌnɑnˈsɪŋkrənəs/", "vi": "không đồng bộ; không cùng pha", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096046", "hw": "nonsynthetic", "pos": "adj", "ipa": "/ˌnɑnsɪnˈθɛtɪk/", "vi": "tự nhiên; không phải nhân tạo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096047", "hw": "nonteachers", "pos": "noun", "ipa": "/ˌnɑnˈtiːtʃɚz/", "vi": "nhân sự không trực tiếp dạy học", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096048", "hw": "nontelescopic", "pos": "adj", "ipa": "/ˌnɑnˌtɛləˈskɑːpɪk/", "vi": "không thu rút được; phi kính viễn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096049", "hw": "nontelescoping", "pos": "adj", "ipa": "/ˌnɑnˈtɛləskoʊpɪŋ/", "vi": "không co rút lồng vào nhau", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096050", "hw": "nonterritorial", "pos": "adj", "ipa": "/ˌnɑnˌtɛrəˈtɔːriəl/", "vi": "phi lãnh thổ; không chiếm cứ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096051", "hw": "nontranslational", "pos": "adj", "ipa": "/ˌnɑntrænzˈleɪʃənəl/", "vi": "không tịnh tiến; phi tịnh tiến", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096052", "hw": "nontransmissible", "pos": "adj", "ipa": "/ˌnɑntrænzˈmɪsəbəl/", "vi": "không truyền nhiễm; không lây lan", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096053", "hw": "nontransparent", "pos": "adj", "ipa": "/ˌnɑntrænsˈpɛrənt/", "vi": "không trong suốt; thiếu minh bạch", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096054", "hw": "nontricyclic", "pos": "adj", "ipa": "/ˌnɑntraɪˈsɪklɪk/", "vi": "phi ba vòng; ngoài nhóm ba vòng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096055", "hw": "nonturbulent", "pos": "adj", "ipa": "/ˌnɑnˈtɜːrbjələnt/", "vi": "không nhiễu loạn; êm đềm", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096056", "hw": "nonuniformity", "pos": "noun", "ipa": "/ˌnɑnˌjuːnəˈfɔːrməti/", "vi": "tính không đồng đều; sự dị chất", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096057", "hw": "nonunionised", "pos": "adj", "ipa": "/ˌnɑnˈjuːnjənaɪzd/", "vi": "không tham gia công đoàn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096058", "hw": "nonunionized", "pos": "adj", "ipa": "/ˌnɑnˈjuːnjənaɪzd/", "vi": "không thuộc tổ chức công đoàn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096059", "hw": "nonuple", "pos": "adj", "ipa": "/ˈnɑːnjəpəl/", "vi": "gấp chín lần; gồm chín phần", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096060", "hw": "nonviscid", "pos": "adj", "ipa": "/ˌnɑnˈvɪsɪd/", "vi": "không nhớt; không bết dính", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096061", "hw": "nonvisual", "pos": "adj", "ipa": "/ˌnɑnˈvɪʒuəl/", "vi": "phi thị giác; ngoài tầm nhìn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096062", "hw": "nonvolatilisable", "pos": "adj", "ipa": "/ˌnɑnˌvɑːlətəlaɪzəbəl/", "vi": "không thể bay hơi; khó thăng hoa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096063", "hw": "nonvolatilizable", "pos": "adj", "ipa": "/ˌnɑnˌvɑːlətəlaɪzəbəl/", "vi": "không thể bay hơi; cố định", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096064", "hw": "nonvoluntary", "pos": "adj", "ipa": "/ˌnɑnˈvɑːlənˌtɛri/", "vi": "không chủ ý; ngoài ý muốn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096065", "hw": "nonvoter", "pos": "noun", "ipa": "/ˌnɑnˈvoʊtɚ/", "vi": "người không đi bầu cử; cử tri vắng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096066", "hw": "nonwashable", "pos": "adj", "ipa": "/ˌnɑnˈwɑːʃəbəl/", "vi": "không giặt được bằng nước", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096067", "hw": "nonwoody", "pos": "adj", "ipa": "/ˌnɑnˈwʊdi/", "vi": "không thân gỗ; thân thảo", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096068", "hw": "nonworker", "pos": "noun", "ipa": "/ˌnɑnˈwɜːrkɚ/", "vi": "người không lao động", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096069", "hw": "noob", "pos": "noun", "ipa": "/nuːb/", "vi": "tay mơ; người mới; gà mờ", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096070", "hw": "noobie", "pos": "noun", "ipa": "/ˈnuːbi/", "vi": "tân thủ; lính mới; người mới chơi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096071", "hw": "noobs", "pos": "noun", "ipa": "/nuːbz/", "vi": "những tay mơ; những người mới chơi", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096072", "hw": "noodles", "pos": "noun", "ipa": "/ˈnuːdəlz/", "vi": "mì sợi; các món mì; bún phở", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096073", "hw": "nooning", "pos": "noun", "ipa": "/ˈnuːnɪŋ/", "vi": "giờ nghỉ trưa; bữa ăn trưa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096074", "hw": "noontime", "pos": "noun", "ipa": "/ˈnuːntaɪm/", "vi": "buổi trưa; đúng giữa trưa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096075", "hw": "nopalea", "pos": "noun", "ipa": "/noʊˈpeɪliə/", "vi": "chi xương rồng Nopalea", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096076", "hw": "nope", "pos": "intj", "ipa": "/noʊp/", "vi": "không; hổng có đâu", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096077", "hw": "nor", "pos": "conj", "ipa": "/nɔːr/", "vi": "cũng không; mà cũng chẳng", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096078", "hw": "noreaster", "pos": "noun", "ipa": "/nɔːrˈiːstɚ/", "vi": "bão đông bắc dữ dội ven biển", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096079", "hw": "noreg", "pos": "noun", "ipa": "/ˈnuːrɛɡ/", "vi": "nước Na Uy tiếng Nynorsk", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096080", "hw": "norethandrolone", "pos": "noun", "ipa": "/ˌnɔːrɛθˈændroʊloʊn/", "vi": "thuốc đồng hóa norethandrolone", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096081", "hw": "norethynodrel", "pos": "noun", "ipa": "/ˌnɔːrɛθˈaɪnədrɛl/", "vi": "hoạt chất progestin norethynodrel", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096082", "hw": "norflex", "pos": "noun", "ipa": "/ˈnɔːrflɛks/", "vi": "thuốc giãn cơ Norflex", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096083", "hw": "norinyl", "pos": "noun", "ipa": "/ˈnɔːrɪnɪl/", "vi": "thuốc ngừa thai kết hợp Norinyl", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096084", "hw": "norland", "pos": "noun", "ipa": "/ˈnɔːrlənd/", "vi": "xứ sở phương bắc; miền bắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096085", "hw": "norlander", "pos": "noun", "ipa": "/ˈnɔːrləndɚ/", "vi": "người phương bắc; dân xứ bắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096086", "hw": "norlestrin", "pos": "noun", "ipa": "/nɔːrˈlɛstrɪn/", "vi": "thuốc tránh thai Norlestrin", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096087", "hw": "norlutin", "pos": "noun", "ipa": "/nɔːrˈluːtɪn/", "vi": "thuốc nội tiết Norlutin", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096088", "hw": "normalised", "pos": "verb", "ipa": "/ˈnɔːrməlaɪzd/", "vi": "đã bình thường hóa; đã chuẩn hóa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096089", "hw": "normaliser", "pos": "noun", "ipa": "/ˈnɔːrməlaɪzɚ/", "vi": "người chuẩn hóa; bộ điều chuẩn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096090", "hw": "normalises", "pos": "verb", "ipa": "/ˈnɔːrməlaɪzɪz/", "vi": "bình thường hóa; quy chuẩn hóa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096091", "hw": "normalising", "pos": "verb", "ipa": "/ˈnɔːrməlaɪzɪŋ/", "vi": "bình thường hóa; đang chuẩn hóa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096092", "hw": "normalized", "pos": "verb", "ipa": "/ˈnɔːrməlaɪzd/", "vi": "đã bình thường hóa; đã chuẩn hóa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096093", "hw": "normalizes", "pos": "verb", "ipa": "/ˈnɔːrməlaɪzɪz/", "vi": "bình thường hóa; quy chuẩn hóa", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096094", "hw": "normalizing", "pos": "verb", "ipa": "/ˈnɔːrməlaɪzɪŋ/", "vi": "bình thường hóa; điều chuẩn", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096095", "hw": "normodyne", "pos": "noun", "ipa": "/ˈnɔːrmədaɪn/", "vi": "thuốc hạ huyết áp Normodyne", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096096", "hw": "normothermia", "pos": "noun", "ipa": "/ˌnɔːrmoʊˈθɜːrmiə/", "vi": "thân nhiệt bình thường", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096097", "hw": "norocean", "pos": "noun", "ipa": "/məˈrɑːkən/", "vi": "người Ma Rốc; tiếng Ma Rốc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096098", "hw": "norsk", "pos": "adj", "ipa": "/nɔːrsk/", "vi": "thuộc Na Uy; tiếng Na Uy", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096099", "hw": "northeastwardly", "pos": "adv", "ipa": "/ˌnɔːrθˈiːstwɚdli/", "vi": "về hướng đông bắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096100", "hw": "northernermost", "pos": "adj", "ipa": "/ˈnɔːrðɚnɚˌmoʊst/", "vi": "xa nhất về phía bắc; cực bắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
  {"id": "lex.en.100k.096101", "hw": "northernness", "pos": "noun", "ipa": "/ˈnɔːrðɚnnəs/", "vi": "đặc trưng phương bắc", "cefr": "C2", "tier": "expanded", "status": "reviewed", "notes": ""},
]

assert len(part1_data) == 100, f"Expected 100 items, got {len(part1_data)}"

valid_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det"}

with open("scratch/b20_r03_raw_p1.json") as f:
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

with open("scratch/b20_r03_p1.json", "w") as f:
    json.dump(part1_data, f, ensure_ascii=False, indent=2)

print("Batch 20 Round 3 Part 1 validated and saved successfully!")
