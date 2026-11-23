import json

RECORDS = [
    ("086603", "sheltering", "verb", "/ˈʃɛltərɪŋ/", "đang che chở; đang trú ẩn"),
    ("086604", "shelterless", "adj", "/ˈʃɛltərləs/", "không nơi nương tựa; không mái nhà"[:35]),
    ("086605", "shelters", "verb", "/ˈʃɛltərz/", "che chở; cho trú ẩn; bảo vệ"),
    ("086606", "shelty", "noun", "/ˈʃɛlti/", "ngựa lùn Shetland; chó chăn cừu"),
    ("086607", "shelved", "verb", "/ʃɛlvd/", "đã gác lại; đã xếp lên kệ"),
    ("086608", "shelver", "noun", "/ˈʃɛlvər/", "người xếp sách lên kệ thư viện"),
    ("086609", "shelves", "noun", "/ʃɛlvz/", "cái kệ; giá sách; thềm đá ngầm"),
    ("086610", "shelving", "verb", "/ˈʃɛlvɪŋ/", "đang gác lại; đang xếp lên kệ"),
    ("086611", "shelvy", "adj", "/ˈʃɛlvi/", "có nhiều bãi cạn ngầm; thoai thoải"[:35]),
    ("086612", "shemmas", "noun", "/ˈʃɛməz/", "khăn choàng cổ trắng Ethiopia"),
    ("086613", "shemozzle", "noun", "/ʃəˈmɑːzəl/", "cảnh hỗn loạn; mớ rắc rối"),
    ("086614", "shenanigans", "noun", "/ʃəˈnænɪɡənz/", "trò nghịch ngợm; thủ đoạn mờ ám"),
    ("086615", "sheol", "noun", "/ˈʃiːoʊl/", "âm phủ; cõi người chết (Do Thái)"),
    ("086616", "shepherded", "verb", "/ˈʃɛpərdɪd/", "đã chăn dắt; đã dẫn dắt cẩn thận"),
    ("086617", "shepherdesses", "noun", "/ˈʃɛpərdəsɪz/", "nữ mục đồng; cô gái chăn cừu"),
    ("086618", "shepherding", "verb", "/ˈʃɛpərdɪŋ/", "đang chăn dắt; đang hướng dẫn"),
    ("086619", "shepherds", "verb", "/ˈʃɛpərdz/", "chăn dắt; dìu dắt hướng dẫn"),
    ("086620", "sheppies", "noun", "/ˈʃɛpiz/", "chuồng cừu"),
    ("086621", "sheppy", "noun", "/ˈʃɛpi/", "chuồng cừu"),
    ("086622", "sheradize", "verb", "/ˈʃɛrəˌdaɪz/", "mạ kẽm khuếch tán nhiệt thép"),
    ("086623", "shereef", "noun", "/ʃəˈriːf/", "quý tộc hậu duệ tiên tri Ả Rập"),
    ("086624", "sherif", "noun", "/ʃəˈriːf/", "quý tộc Ả Rập; thủ lĩnh Mecca xưa"[:35]),
    ("086625", "sheriffalty", "noun", "/ˈʃɛrəfəlti/", "chức vụ cảnh sát trưởng quận"),
    ("086626", "sheriffdom", "noun", "/ˈʃɛrəfdəm/", "khu vực thẩm quyền cảnh sát trưởng"[:35]),
    ("086627", "sheriffhood", "noun", "/ˈʃɛrəfˌhʊd/", "chức vụ cảnh sát trưởng quận"),
    ("086628", "sheriffship", "noun", "/ˈʃɛrəfˌʃɪp/", "chức vụ cảnh sát trưởng quận"),
    ("086629", "sheugh", "noun", "/ʃjuːx/", "con mương rãnh thoát nước"),
    ("086630", "sheughs", "noun", "/ʃjuːxs/", "con mương rãnh thoát nước"),
    ("086631", "sheva", "noun", "/ʃəˈvɑː/", "nguyên âm trung hòa ngắn (ngữ âm)"),
    ("086632", "shevat", "noun", "/ʃəˈvɑːt/", "tháng thứ năm lịch Do Thái"),
    ("086633", "shewbread", "noun", "/ˈʃoʊˌbrɛd/", "bánh thánh dâng bàn thờ Do Thái"),
    ("086634", "shewed", "verb", "/ʃoʊd/", "đã cho thấy; đã chứng minh (cổ)"),
    ("086635", "shewing", "verb", "/ˈʃoʊɪŋ/", "đang cho thấy; đang biểu lộ (cổ)"),
    ("086636", "shewn", "verb", "/ʃoʊn/", "đã được bày tỏ; đã trưng ra (cổ)"),
    ("086637", "shews", "verb", "/ʃoʊz/", "cho thấy; chỉ rõ (dạng cổ)"),
    ("086638", "shiais", "noun", "/ʃiˈaɪz/", "trận thi đấu võ thuật (tiếng Nhật)"[:35]),
    ("086639", "shibah", "noun", "/ˈʃɪvə/", "tuần để tang bảy ngày Do Thái"),
    ("086640", "shibushi", "noun", "/ʃɪˈbuːʃi/", "tiếng Bushi (đảo Mayotte)"),
    ("086641", "shie", "verb", "/ʃaɪ/", "giật mình né tránh; ném liệng"),
    ("086642", "shied", "verb", "/ʃaɪd/", "đã giật mình lùi lại; đã ném"),
    ("086643", "shieldbone", "noun", "/ˈʃiːldˌboʊn/", "xương bả vai"),
    ("086644", "shielder", "noun", "/ˈʃiːldər/", "người che chắn bảo vệ"),
    ("086645", "shieldless", "adj", "/ˈʃiːldləs/", "không có khiên bảo vệ; không che"),
    ("086646", "shields", "verb", "/ʃiːldz/", "che chở; bảo vệ; chắn ánh sáng"),
    ("086647", "shieling", "noun", "/ˈʃiːlɪŋ/", "túp lều đồng cỏ chăn cừu Scotland"[:35]),
    ("086648", "shies", "verb", "/ʃaɪz/", "giật mình né tránh; ném liệng"),
    ("086649", "shiftable", "adj", "/ˈʃɪftəbəl/", "có thể dịch chuyển; thay đổi được"),
    ("086650", "shifted", "verb", "/ˈʃɪftɪd/", "đã dịch chuyển; đã chuyển sang"),
    ("086651", "shiftily", "adv", "/ˈʃɪftɪli/", "lấm lét gian xảo; không đáng tin"),
    ("086652", "shiftlessness", "noun", "/ˈʃɪftləsnəs/", "tính lười biếng thiếu ý chí"),
    ("086653", "shifts", "noun", "/ʃɪfts/", "ca làm việc; sự thay đổi vị trí"),
    ("086654", "shikar", "noun", "/ʃɪˈkɑːr/", "cuộc đi săn thú (tiếng Hindi)"),
    ("086655", "shikaree", "noun", "/ʃɪˈkɑːri/", "người dẫn đường đi săn Ấn Độ"),
    ("086656", "shikari", "noun", "/ʃɪˈkɑːri/", "thợ săn; người dẫn đường đi săn"),
    ("086657", "shikse", "noun", "/ˈʃɪksə/", "phụ nữ không theo đạo Do Thái"),
    ("086658", "shillalah", "noun", "/ʃɪˈleɪli/", "gậy gỗ sồi truyền thống Ireland"),
    ("086659", "shillyshally", "noun", "/ˈʃɪliˌʃæli/", "sự do dự chần chừ; thái độ lừng khừng"[:35]),
    ("086660", "shilpit", "adj", "/ˈʃɪlpɪt/", "gầy ốm yếu ớt; nhợt nhạt (Scotland)"[:35]),
    ("086661", "shily", "adv", "/ˈʃaɪli/", "e thẹn; bẽn lẽn; rụt rè"),
    ("086662", "shimane", "noun", "/ʃɪˈmɑːneɪ/", "tỉnh Shimane (Nhật Bản)"),
    ("086663", "shimmed", "verb", "/ʃɪmd/", "đã chêm miếng đệm mỏng"),
    ("086664", "shimmered", "verb", "/ˈʃɪmərd/", "đã ánh lên lung linh lấp lánh"),
    ("086665", "shimmering", "verb", "/ˈʃɪmərɪŋ/", "đang lung linh; đang lấp lánh"),
    ("086666", "shimmers", "verb", "/ˈʃɪmərz/", "lung linh; lấp lánh ánh sáng"),
    ("086667", "shimmied", "verb", "/ˈʃɪmid/", "đã rung lắc mạnh; nhảy điệu shimmy"),
    ("086668", "shimmies", "verb", "/ˈʃɪmiz/", "rung lắc mạnh; nhảy điệu shimmy"),
    ("086669", "shimming", "verb", "/ˈʃɪmɪŋ/", "đang chèn miếng chêm mỏng"),
    ("086670", "shimmying", "verb", "/ˈʃɪmiɪŋ/", "đang rung lắc mạnh; nhảy shimmy"),
    ("086671", "shims", "verb", "/ʃɪmz/", "chêm miếng đệm; chèn nêm mỏng"),
    ("086672", "shined", "verb", "/ʃaɪnd/", "đã đánh bóng; đã chiếu sáng"),
    ("086673", "shines", "verb", "/ʃaɪnz/", "tỏa sáng; chiếu sáng; xuất sắc"),
    ("086674", "shingled", "verb", "/ˈʃɪŋɡəld/", "đã lợp ván mái; đã cắt tóc ngắn"),
    ("086675", "shingly", "adj", "/ˈʃɪŋɡli/", "đầy sỏi cuội (bãi biển)"),
    ("086676", "shinies", "noun", "/ˈʃaɪniz/", "vật sáng lấp lánh; đồ sưu tầm quý"),
    ("086677", "shinines", "noun", "/ˈʃaɪninəs/", "độ bóng láng; vẻ sáng bóng"),
    ("086678", "shinleaf", "noun", "/ˈʃɪnˌliːf/", "cây cỏ lộc đề Pyrola"),
    ("086679", "shinleaved", "adj", "/ˈʃɪnˌliːvd/", "có lá bóng dáng tròn Pyrola"),
    ("086680", "shinned", "verb", "/ʃɪnd/", "đã trèo leo bằng hai chân; đá ống"[:35]),
    ("086681", "shinney", "noun", "/ˈʃɪni/", "môn khúc côn cầu đường phố"),
    ("086682", "shinnied", "verb", "/ˈʃɪnid/", "đã leo bám; chơi khúc côn cầu phố"),
    ("086683", "shinnies", "verb", "/ˈʃɪniz/", "leo bám nhanh; chơi khúc côn cầu"),
    ("086684", "shinning", "verb", "/ˈʃɪnɪŋ/", "đang leo bám; đá vào ống chân"),
    ("086685", "shinnying", "verb", "/ˈʃɪniɪŋ/", "đang leo bám thân cây cột"),
    ("086686", "shinobu", "noun", "/ʃɪˈnoʊbuː/", "tên riêng Nhật Shinobu"),
    ("086687", "shinpad", "noun", "/ˈʃɪnˌpæd/", "tấm bọc bảo vệ ống đồng"),
    ("086688", "shinplaster", "noun", "/ˈʃɪnˌplæstər/", "tiền giấy mất giá; giấy nợ lẻ xưa"),
    ("086689", "shins", "verb", "/ʃɪnz/", "trèo bám bằng chân; đá ống đồng"),
    ("086690", "shinties", "noun", "/ˈʃɪntiz/", "môn khúc côn cầu shinty Scotland"),
    ("086691", "shintoist", "adj", "/ˈʃɪntoʊɪst/", "thuộc Thần đạo Nhật Bản"),
    ("086692", "shintoistic", "adj", "/ˌʃɪntoʊˈɪstɪk/", "mang tính Thần đạo Nhật Bản"),
    ("086693", "shintoits", "noun", "/ˈʃɪntoʊɪsts/", "tín đồ Thần đạo Nhật Bản"),
    ("086694", "shinty", "noun", "/ˈʃɪnti/", "môn khúc côn cầu cổ truyền Scotland"[:35]),
    ("086695", "shipkeepers", "noun", "/ˈʃɪpˌkiːpərz/", "người trông coi tàu đậu bến"),
    ("086696", "shipman", "noun", "/ˈʃɪpmən/", "thủy thủ; thuyền trưởng (từ cổ)"),
    ("086697", "shipmaster", "noun", "/ˈʃɪpˌmæstər/", "thuyền trưởng tàu buôn"),
    ("086698", "shipmoney", "noun", "/ˈʃɪpˌmʌni/", "thuế đóng tàu chiến Anh thế kỷ 17"),
    ("086699", "shipped", "verb", "/ʃɪpt/", "đã vận chuyển hàng; đã gửi đi"),
    ("086700", "shippen", "noun", "/ˈʃɪpən/", "chuồng bò (phương ngữ Anh)"),
    ("086701", "shippens", "noun", "/ˈʃɪpənz/", "chuồng bò"),
    ("086702", "ships", "verb", "/ʃɪps/", "vận chuyển bằng tàu; gửi hàng đi"),
]

# Cleanly replace any sliced items <= 35 chars
RECORDS[1] = ("086604", "shelterless", "adj", "/ˈʃɛltərləs/", "không nơi nương tựa; vô gia cư")
RECORDS[8] = ("086611", "shelvy", "adj", "/ˈʃɛlvi/", "nhiều bãi cạn ngầm; thoai thoải")
RECORDS[21] = ("086624", "sherif", "noun", "/ʃəˈriːf/", "quý tộc Ả Rập; thủ lĩnh Mecca")
RECORDS[23] = ("086626", "sheriffdom", "noun", "/ˈʃɛrəfdəm/", "địa hạt cảnh sát trưởng quận")
RECORDS[35] = ("086638", "shiais", "noun", "/ʃiˈaɪz/", "trận thi đấu võ thuật (Nhật Bản)")
RECORDS[44] = ("086647", "shieling", "noun", "/ˈʃiːlɪŋ/", "túp lều đồng cỏ Scotland")
RECORDS[56] = ("086659", "shillyshally", "noun", "/ˈʃɪliˌʃæli/", "sự do dự chần chừ; sự lừng khừng")
RECORDS[57] = ("086660", "shilpit", "adj", "/ˈʃɪlpɪt/", "gầy ốm yếu ớt; nhợt nhạt")
RECORDS[77] = ("086680", "shinned", "verb", "/ʃɪnd/", "đã leo bám bằng chân; đá ống chân")
RECORDS[91] = ("086694", "shinty", "noun", "/ˈʃɪnti/", "môn khúc côn cầu Scotland")

assert len(RECORDS) == 100
for r in RECORDS:
    assert 0 < len(r[4]) <= 35, (r, len(r[4]))
    assert "/" not in r[4], r
    assert r[3].count("/") == 2, r

raw = json.load(open("scratch/b38_r04_raw_p2.json"))
by_id = {r["id"].split(".")[-1]: r for r in raw}
out = []
for sid, hw, pos, ipa, vi in RECORDS:
    rec = dict(by_id[sid])
    assert rec["hw"] == hw, (sid, hw, rec["hw"])
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

json.dump(out, open("scratch/b38_r04_reviewed_p2.json", "w"), ensure_ascii=False, indent=2)
print("b38_r04_p2 saved OK")
