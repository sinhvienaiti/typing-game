# Bộ giám khảo bản đồ (CL-03, 28/10/2026)

**Đọc cho ai:** người điều phối một lượt chấm bản đồ (Claude), và subagent giám khảo (chỉ đọc mục 4).

**Nguồn:** [MAP_PLAN](../../../docs/tools/map-factory/MAP_PLAN.md) §2.4 (luật nhìn), §2.5 (ánh sáng, sự sống), §2.8 (bộ giám khảo), §2.9 (cổng chất lượng), §3.4 (cổng A–D); [TICKETS](../../../docs/tools/map-factory/TICKETS.md) CL-03; [spike L2-cau](../../../docs/tools/map-factory/spike-l2-cau.md) §3, §6, §8.

**Vì sao cần:** spike được người dựng tự chấm 7,25, giám khảo độc lập chấm 6,75. LLM chấm thiên vị bài của chính nó. Bộ này cho một người chấm không phải người dựng, có thang cố định, mẫu hiệu chuẩn và luật bỏ kết quả lệch.

## 1. Ai chấm, thấy gì

- Giám khảo là **một subagent mới** cho mỗi lượt. Người dựng không bao giờ chấm làm cổng.
- Giám khảo chỉ thấy: lời nhắc ở mục 4, ảnh mẫu (mốc 10) và các ảnh đã đổi tên trung tính. Không thấy ghi chú của người dựng, spec, số đo ảnh, lịch sử commit, điểm của lượt trước, hay ảnh nào là mẫu kiểm.
- Ba mẫu hiệu chuẩn được **trộn ẩn** vào mỗi lượt như ảnh bình thường. Người điều phối kiểm điểm của chúng (mục 5.1). Lệch quá dung sai thì bỏ cả lượt.
- Số đo ảnh (Q5) là phép kiểm riêng, không đưa cho giám khảo, để giám khảo không bị neo vào số.
- Chủ dự án quyết cuối (Q9). Điểm giám khảo là cổng của agent, không thay lời chủ dự án.

## 2. Bộ hiệu chuẩn

Ba ảnh đã chuẩn bị sẵn ở `tmp/map-studio/compare-judge/` (repo cha; `tmp/` không vào Git; thư mục tên `compare-` nên `capture-prune` giữ lại).

| Mẫu | File | Lấy từ | Điểm đích | Dải nhận (±0,75) |
|---|---|---|---|---|
| Ảnh mẫu Haven Grove, nửa trên "BEFORE" | `ref-before.png` (1318×735) | `tmp/map-studio/owner-reference-haven-grove.webp`, cắt `1318x735+0+0` | 10 | ≥ 9,25 |
| M0b, khung mặc định | `m0b-default.png` (1280×720) | `tmp/map-studio/now-rong-giu-ai-m0b.png` (tấm 3 khung chồng dọc), khung trên cùng `1280x720+0+0` | 4,75 | 4,0–5,5 |
| Spike `final2`, khung mặc định | `spike-final2-default.png` (1920×1080) | `games/.wt-dh-mapspike/tmp/shots/mapspike/final2/1920x1080-default.png` | 6,75 | 6,0–7,5 |

Dựng lại khi mất (chạy ở gốc repo cha):

```bash
C=tmp/map-studio/compare-judge; mkdir -p $C
magick tmp/map-studio/owner-reference-haven-grove.webp -crop 1318x735+0+0 +repage -strip $C/ref-before.png
magick tmp/map-studio/now-rong-giu-ai-m0b.png -crop 1280x720+0+0 +repage -strip $C/m0b-default.png
magick games/.wt-dh-mapspike/tmp/shots/mapspike/final2/1920x1080-default.png -strip $C/spike-final2-default.png
```

- Ảnh mẫu vừa là mốc 10 giám khảo được thấy (`mau-10.png`), vừa là một mẫu kiểm ẩn. Mẫu kiểm này không thừa: giám khảo phải chấm nó qua 12 điểm con như mọi ảnh, nên nó kiểm mô tả mức 10 của thang có khớp ảnh mẫu không (trung bình có trọng số phải ra ≥ 9,25).
- M0b và spike là hai mốc giữa thang. Giám khảo không biết chúng là gì.
- Khi có kit khác (violet-glade…), kit đó cần ảnh mẫu riêng và ba mẫu kiểm riêng (MAP_PLAN §2.7 mục 2); bộ này chỉ cho pine-river.

## 3. Chạy một lượt chấm (người điều phối)

**Loại ảnh và tên trung tính:**

| Loại | Tên cho giám khảo | Chấm gì |
|---|---|---|
| Ảnh tĩnh (khung mặc định 1080p, 720p; 12 góc: nghiêng 40°, 55°, 75° × hướng 0°, 90°, 180°, 270°; lật gương) | `anh-NN.png` + bản nhỏ `anh-NN-nho.png` (rộng 384 px) | 12 điểm con, điểm chung |
| Ảnh AFTER (mọi ô đã xây, quái đợt 7 có thẻ chữ) | `after-NN.png` + `after-NN-nho.png` | 12 điểm con, điểm chung, đạt/trượt "đọc được khi đang chơi" |
| Dải sự sống (tờ ghép 20 khung trong 10 s) | `song-NN.jpg` | chỉ điểm con "sự sống" |

**Các bước:**

1. Chuẩn bị thư mục chấm trong worktree đang làm, dưới `tmp/map-pilot/`. Xáo ngẫu nhiên ba mẫu kiểm cùng ảnh tĩnh cần chấm, đổi tên, bỏ metadata. Khóa (tên gốc ↔ tên trung tính) để ngoài thư mục chấm:

   ```bash
   # ở gốc repo cha; W = worktree, SRC = thư mục ảnh của lượt, TAG = tên lượt
   W=games/.wt-dh-mappilot; SRC=$W/tmp/map-pilot/a3; TAG=a3-r1
   C=tmp/map-studio/compare-judge; J=$W/tmp/map-pilot/judge-$TAG; K=$J.key.txt
   mkdir -p $J && magick $C/ref-before.png -strip $J/mau-10.png
   printf '%s\n' $C/ref-before.png $C/m0b-default.png $C/spike-final2-default.png $SRC/*.png |
     node -e 'const l=require("fs").readFileSync(0,"utf8").trim().split("\n");for(let i=l.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[l[i],l[j]]=[l[j],l[i]]}l.forEach((f,i)=>console.log(f+" anh-"+String(i+1).padStart(2,"0")))' > $K
   while read src dst; do magick "$src" -strip $J/$dst.png; magick "$src" -resize 384x -strip $J/$dst-nho.png; done < $K
   ```

   Ảnh AFTER và dải sự sống đổi tên `after-NN`, `song-NN` theo cùng cách, ghi vào cùng khóa. Mỗi lượt ≤ 16 ảnh tĩnh cộng 3 mẫu kiểm; nhiều hơn thì chia lượt, lượt nào cũng có đủ 3 mẫu kiểm.

2. Gọi **một subagent mới**. Lời nhắc = khối ở mục 4 nguyên văn, cộng một dòng: `Thư mục: <đường dẫn tuyệt đối của $J>. Ảnh: anh-01 … anh-NN; after-…; song-…` (liệt kê tên, không gì khác). Không gửi khóa, không nói lượt này để làm gì.
3. Lưu khối JSON giám khảo trả về vào `$J.json`. Tính lại trung bình và kiểm mẫu:

   ```bash
   node -e '
   const fs=require("fs");const [jf,kf]=process.argv.slice(1);
   const W={bo_cuc:1.5,gom_sang:1.5,dong_yen:1,mep:1,tieu_diem:1,diem_mau:1,nhip_mat_do:1,khung:0.75,cao_do:0.5,sang_toi:1,loi_va_do:0.75,nuoc:0.5};
   const T={"ref-before.png":10,"m0b-default.png":4.75,"spike-final2-default.png":6.75};
   const key=Object.fromEntries(fs.readFileSync(kf,"utf8").trim().split("\n").map(l=>{const [s,d]=l.split(" ");return [d,s]}));
   for(const r of JSON.parse(fs.readFileSync(jf,"utf8"))){
     let s=0,w=0;for(const [k,v] of Object.entries(r.diem_con))if(W[k]&&v!=null){s+=v*W[k];w+=W[k]}
     const src=key[r.anh]||r.anh,t=T[src.split("/").pop()];
     const mau=t==null?"":Math.abs(r.diem_chung-t)<=0.75?"  mẫu: đạt":"  mẫu: TRƯỢT";
     console.log(r.anh,src,"tb",w?(s/w).toFixed(2):"-","chung",r.diem_chung,mau);
   }' $J.json $K
   ```

4. Áp mục 5 (kiểm mẫu, người thứ hai, cổng). Đổi góp ý thành tham số qua từ điển (mục 6). Ghi điểm vào báo cáo của chặng, kèm tên lượt và số lần chạy lại.
5. Dọn: `node tools/capture-prune/prune.mjs $J --apply` (bản sao ảnh). Giữ `$J.json`, `$J.key.txt` và tờ ghép.

## 4. Lời nhắc giám khảo (chép nguyên khối)

````text
Bạn là giám khảo vẻ ngoài của bản đồ cho một game phòng thủ 3D nhìn từ trên xuống (Rồng Giữ Ải). Bạn chỉ chấm cảnh: đất, cỏ, cây, đá, nước, ánh sáng, bố cục. Bạn không chấm luật chơi. Bạn không biết ai dựng ảnh nào; đừng đoán, và đừng chấm nương tay.

BẠN CÓ
- mau-10.png: nửa trên ("BEFORE") ảnh một game làng khác. Đây là mốc 10 của thang. Bỏ qua chữ phủ trên ảnh (chữ "BEFOR", logo).
- anh-NN.png: ảnh tĩnh cần chấm; anh-NN-nho.png là bản nhỏ để nheo mắt.
- after-NN.png (nếu có): ảnh đang chơi, có quái, thẻ chữ, nhà đã xây; after-NN-nho.png là bản nhỏ.
- song-NN.jpg (nếu có): 20 khung trong 10 giây của cùng một cảnh, để chấm sự sống.
Chỉ đọc những file được liệt kê, trong thư mục được cho, bằng công cụ Read. Không đọc file, thư mục, tài liệu hay trang web nào khác.

CÁCH CHẤM
1. Xem mau-10.png ở cỡ đầy đủ. Nó có: đồng cỏ sáng, lớn và yên; chi tiết nhỏ chỉ ở mép; đất mòn dưới cây và ở ngã ba, có viền tối mảnh rồi quầng cỏ nhạt; lùm cây nhiều sắc, vài cây đỏ cam rải cách xa nhau; lối mòn tỏa ra có cột đèn đều nhịp; vách đá xám xếp tầng có đá vụn dưới chân; ao xanh lam có lá súng và bến gỗ; nắng sáng, bóng mềm.
2. Với mỗi ảnh tĩnh và AFTER: xem bản nhỏ trước (để chấm bố cục, gom độ sáng), rồi bản đầy đủ (các điểm con còn lại).
3. Cho từng điểm con theo bảng mốc, bước 0,5. Mốc 10, 7, 4 là ba điểm neo; ảnh nằm giữa hai mô tả thì chọn mức giữa. Luật trần: ảnh có rõ một lỗi trong cột "7" thì điểm con đó không quá 8; có rõ một lỗi trong cột "4" thì không quá 5, dù chỗ khác đẹp.
4. Chấm mỗi ảnh theo thang và mau-10.png. Không xếp hạng các ảnh với nhau, không kéo điểm cho đều.
5. Tính trung bình có trọng số của các điểm con có số (bỏ điểm con "—"). Làm tròn tới 0,25. Đối chiếu với bảng "điểm chung nghĩa là gì": nếu lệch rõ, được chỉnh tối đa ±0,5, ghi lý do một câu (một điều lớn mà không điểm con nào bắt được). Không chỉnh để "cho đẹp số".
6. Ảnh AFTER: chấm như ảnh tĩnh, cộng đạt/trượt theo danh sách A1–A6.
7. Dải sự sống: chỉ cho điểm con "sự sống"; điểm chung của dải bằng điểm đó.
8. Ghi tối đa 3 góp ý mỗi ảnh: chỗ nào trong khung, sửa gì, mỗi góp ý một câu. Nếu khớp một câu trong danh sách mã góp ý, thêm mã ở đầu (ví dụ "FB-14: dải sọc chéo ở đồng cỏ giữa khung").

LUẬT CHẤM
- Chấm cái thấy trong khung, không chấm cái đoán. Vật bị mép khung cắt chỉ tính phần thấy.
- mau-10.png là một làng; ảnh của ta là sân phòng thủ: làn đất dẫn vào một bệ đá ở giữa, có sông, cầu, ô xây. Không trừ điểm vì làn, bệ, quái, thẻ chữ hay giao diện. Không cộng điểm vì nhà cửa.
- Nhiều vật hơn không có nghĩa đẹp hơn. Chi tiết nhỏ rải đều khắp khung là lỗi (rối), không phải ưu điểm.
- Tối hơn mau-10.png rõ rệt là lỗi ở "sáng tối" và "gom độ sáng", dù trông "điện ảnh".
- Góc nhìn gần thẳng xuống làm tán cây thành đốm: vẫn chấm theo mô tả, không bù.
- 10 là ngang mau-10.png ở điểm con đó. 8 là mức của một game bán được. Dùng cả thang; cho dưới 5 khi mô tả cột "4" khớp.

BẢNG MỐC (trọng số trong ngoặc)
1. bo_cuc — Bố cục (1,5). Nhìn bản nhỏ: có hình lớn rõ không.
   10: phân khối lớn rõ: khoảng một phần tư khung trở lên là bãi trống liền một khối; vật dày dồn về mép và về một phía; mắt đi từ tâm theo đường ra các điểm phụ.
   7: tâm và đường rõ, cây có gom cụm, nhưng cụm phủ đều khắp khung, không có bãi trống lớn liền khối; hoặc một mảng quan trọng bị mép khung cắt vụng.
   4: vật rải đều toàn khung, không phân khối; chỉ đường và tâm làm nên cấu trúc.
2. gom_sang — Gom độ sáng (1,5). Nhìn bản nhỏ, nheo mắt.
   10: 3–4 mảng sáng tối lớn và sạch; đồng sáng chiếm phần lớn khung; tối sâu chỉ ở mép.
   7: có mảng lớn nhưng đồng sáng bị chia vụn bởi nhiều cụm tối, bóng hay cây sẫm; vùng tối khoảng một phần ba khung.
   4: phần lớn khung tối hoặc trung tính; mảng sáng nhỏ, vụn; chấm tối rải khắp.
3. dong_yen — Đồng yên (1).
   10: đồng cỏ sáng, ấm, loang rất mềm; cụm cỏ hoa thưa, dày dần về mép.
   7: đồng mềm nhưng có sọc, vệt chéo, hoặc hoa và vật nhỏ rải đều khắp; hoặc sẫm hơn mẫu rõ.
   4: đồng bị chia bởi bóng dài, bụi và đá nhỏ rải đều như rắc tiêu; hoặc phẳng tối một màu.
4. mep — Mép (1). Chỗ chuyển giữa đất, cỏ, nước, rừng.
   10: đất mòn dưới cây và ở ngã ba có viền tối mảnh rồi quầng cỏ nhạt, dáng có thùy tự nhiên; mép đường mềm; mép rừng có vịnh và mũi.
   7: có đĩa đất và viền nhưng tròn đều như đóng dấu; hoặc mép rừng thẳng như tường.
   4: chuyển cứng, cắt sắc; gần như không có đất mòn; đường là dải phẳng.
5. tieu_diem — Thứ bậc tiêu điểm (1).
   10: một tiêu điểm chính rõ ở tâm (có viền, có sân); 2–3 tiêu điểm phụ (ao, vách, mốc) nằm trọn trong khung, không tranh nhau.
   7: tâm rõ; tiêu điểm phụ có nhưng bị cắt ở mép hoặc yếu.
   4: chỉ có tâm; hoặc vật lạ (khối màu, quả cầu tạm) tranh chú ý.
6. diem_mau — Điểm màu (1).
   10: xanh lá ấm làm chủ; vài điểm đỏ cam đặt cách xa nhau; đá xám, nước lam; không màu lạc.
   7: bảng màu sạch nhưng không có điểm ấm, hoặc điểm nhấn chỉ là tím lạnh; có vài chấm màu lạc (ví dụ chấm đỏ như máu).
   4: màu lệch: xanh két, tím, lam lạnh chiếm nhiều; khối màu bão hòa trông như đồ tạm.
7. nhip_mat_do — Nhịp mật độ (1). Ba bậc: lùm dày, cây lẻ, bãi trống.
   10: vài lùm dày, cây lẻ có đĩa đất ở dải chuyển tiếp, bãi trống thật; chuyển dần giữa ba bậc.
   7: có lùm và cây lẻ nhưng lùm nhiều, rải khắp, khoảng trống giữa chúng đều nhau.
   4: một mật độ đều khắp (rắc), hoặc chỉ có rừng đặc và đồng trống, không gì ở giữa.
8. khung — Khung (0,75). Mép khung hình.
   10: viền khung đa dạng (vách sáng, rừng có ngọn sáng, mép nước); mắt được giữ trong khung.
   7: có viền nhưng một bên là tường cây tối đặc, hoặc một dải sọc lạ ở mép.
   4: viền là bức tường cây tối, đều, quanh gần hết khung; hoặc khung trống trơn.
9. cao_do — Cao độ (0,5).
   10: vách đá xếp tầng, mặt trên sáng, đá vụn dưới chân; mặt đất có gò nhẹ đọc được.
   7: có vách hoặc gò nhưng đọc kém: sườn sơn màu đá, tảng tròn như trứng, sọc đều.
   4: phẳng hoàn toàn.
10. sang_toi — Sáng tối (1).
   10: nắng ấm, hướng rõ; bóng mềm, dài vừa; cả khung sáng; bóng hơi lam.
   7: hướng nắng rõ nhưng cảnh tối hơn mẫu rõ; hoặc bóng chéo dài phủ nhiều; hoặc vùng tối ngả tím hay xanh két.
   4: tối, u; bóng nặng phủ khắp; hoặc ánh màu lệch cả khung.
11. loi_va_do — Nhịp lối và đồ (0,75).
   10: mạng lối mòn có đích (ao, sân, bãi đá), có lối to lối nhỏ; cột đèn hoặc cọc đều nhịp dọc lối; rào ở khúc cong.
   7: có lối mòn có hướng, nhưng không có đồ dọc đường; hoặc lối mảnh, khó đọc.
   4: chỉ có đường chính (làn), không lối phụ; vài đồ rời rạc không theo nhịp. Không có gì ngoài làn: 3.
12. nuoc — Nước (0,5). Không có nước trong khung: "—".
   10: nước lam sạch, giữa sâu hơn; bờ có chi tiết (lau sậy, lá súng, bến gỗ); tách hẳn khỏi màu rừng.
   7: nước đẹp, có gợn, nhưng bờ trơn, hoặc màu gần màu rừng (xanh két).
   4: dải màu phẳng, khó tách khỏi nền.
13. su_song — Sự sống (1). Chỉ chấm trên song-NN.jpg; ảnh tĩnh và AFTER ghi "—".
   10: ít nhất 4 thứ chuyển động mềm: chim bay qua phần ngoài khung, bóng mây trôi, bướm hay đom đóm ở mép bãi, khói, gió đồng bộ cỏ và cây; không gì động sát làn hay thẻ chữ.
   7: 2–3 thứ chuyển động.
   4: chỉ nước chảy và cây đung đưa. Đứng im: 1. Có vật động thấp ngay trên làn hay thẻ chữ: không quá 5.

ĐIỂM CHUNG NGHĨA LÀ GÌ
10 ngang mau-10.png. 9 gần mẫu, một chỗ yếu nhỏ. 8 đẹp như game bán được, 1–2 chỗ yếu nhỏ, không lỗi nào ở cột "4". 7 đẹp, có ý đồ, nhưng có vài lỗi cột "7" (rối hay tối một phần, thiếu đồ dọc đường, rừng như tường một bên). 6 nhiều lỗi cột "7" cùng lúc. 5 gọn, đọc được, nhưng kiểu rải đều; có vài lỗi cột "4". 4 nhiều lỗi cột "4": tối, rắc đều, phẳng, màu lệch, không lối mòn. 3 khối tạm, chưa thành cảnh. 1–2 lỗi hiển thị.

AFTER: ĐỌC ĐƯỢC KHI ĐANG CHƠI (trượt nếu một mục trượt rõ; ghi mục và chỗ)
A1 Mọi quái tách khỏi nền khi nheo mắt (bản nhỏ); không quái nào chìm trong bóng, rừng hay nền cùng màu.
A2 Mọi thẻ chữ đọc được; không thẻ nào bị nền rối hay vật cảnh làm khó đọc.
A3 Mỗi làn đọc được từ mép khung tới bệ, kể cả khi có quái và nhà.
A4 Đỏ và vàng cam của cảnh báo không lẫn với màu cảnh: không cây, hoa, đèn nào gần làn trông như tín hiệu.
A5 Thứ bậc: giao diện > hiệu ứng > quân > cảnh. Không vật cảnh nào sáng hơn hay rực hơn quái gần nó; không điểm sáng của cảnh nằm dưới vùng giao diện.
A6 Nhà đã xây và bẫy đọc được, không lẫn vào lùm hay đĩa đất.

MÃ GÓP Ý (chỉ để gắn mã; viết góp ý bằng lời của bạn)
FB-01 tối quá, u ám · FB-02 rối, nhiễu, lắm chấm · FB-03 rừng như bức tường · FB-04 trống, chán, thiếu điểm nhấn · FB-05 lối không rõ · FB-06 thiếu sức sống · FB-07 ao hay tiêu điểm phụ sai chỗ · FB-08 tím quá, màu lạ · FB-09 chấm đỏ như máu, lẫn màu cảnh báo · FB-10 vách như trứng, vách sọc · FB-11 cây rắc đều như tiêu · FB-12 đất tròn như đóng dấu · FB-13 bệ chìm, không thấy tâm · FB-14 đồng cỏ sọc, vằn · FB-15 nước như rừng, nước đục · FB-16 thiếu đèn, rào dọc đường · FB-17 quái, chữ khó đọc · FB-18 vô lý: lối mòn không có đích, cong vô cớ

TRẢ LỜI
Một khối ```json duy nhất là một mảng, mỗi ảnh một phần tử, theo thứ tự tên; sau khối đó tối đa 5 dòng nhận xét chung. Số dùng dấu chấm thập phân.
[
  {
    "anh": "anh-01",
    "loai": "tinh",
    "diem_con": {"bo_cuc": 0, "gom_sang": 0, "dong_yen": 0, "mep": 0, "tieu_diem": 0, "diem_mau": 0,
                 "nhip_mat_do": 0, "khung": 0, "cao_do": 0, "sang_toi": 0, "loi_va_do": 0, "nuoc": 0, "su_song": null},
    "trung_binh": 0,
    "chinh": 0,
    "ly_do_chinh": "",
    "diem_chung": 0,
    "gioi_han": "điều kéo điểm xuống nhiều nhất, vài chữ",
    "gop_y": ["FB-xx: chỗ nào, sửa gì"],
    "after": null
  }
]
"loai" là "tinh", "after" hoặc "song". Điểm con "—" ghi null. Với after-NN, "after" là {"dat": true hoặc false, "truot": ["A2: thẻ chữ góc dưới trái nằm trên đám hoa"]}. Với song-NN, chỉ "su_song" có số.
````

## 5. Đọc kết quả

### 5.1 Kiểm mẫu

- Mỗi mẫu kiểm phải nằm trong dải nhận ở mục 2: ảnh mẫu ≥ 9,25; M0b 4,0–5,5; spike 6,0–7,5.
- Một mẫu trượt: **bỏ cả lượt**, gọi một giám khảo mới với bộ tên xáo lại. Không lấy điểm ảnh thật từ lượt có mẫu trượt.
- Ba giám khảo liên tiếp trượt mẫu: lời nhắc có vấn đề. Dừng chấm, sửa mô tả mốc ở mục 4, chạy lại phép thử ở mục 7, ghi vào báo cáo chặng.
- Trung bình giám khảo tự tính lệch quá 0,1 so với số người điều phối tính lại: dùng số tính lại.
- Điểm con của mẫu kiểm chỉ để tham khảo (mục 7); cổng chỉ xét điểm chung.

### 5.2 Luật người thứ hai (±0,5 quanh cổng)

Một giám khảo luôn có. Người thứ hai chỉ chạy khi một số quyết định cổng nằm trong ±0,5 quanh ngưỡng của nó.

| Số quyết định cổng | Khi nào gọi người thứ hai | Người thứ hai chấm gì |
|---|---|---|
| Ngưỡng từng ảnh (mỗi ảnh ≥ 8; không ảnh nào < 7 hay < 6,5; AFTER ≥ 7,5; lật gương ≥ 7,5; sự sống ≥ 7) | Điểm của ảnh đó trong [ngưỡng − 0,5; ngưỡng + 0,5] | Ảnh đó (và mọi ảnh khác cũng rơi vào vùng đó), cộng 3 mẫu kiểm |
| Trung vị 12 ảnh (≥ 7,5 ở cổng A, ≥ 8 ở cổng C) | Trung vị trong ±0,5 quanh ngưỡng | Cả 12 ảnh, cộng 3 mẫu kiểm |
| So sánh hai bản (cổng B: bản suy ra không thấp hơn bản ghim A quá 0,25) | Luôn chấm hai bản trong **cùng một lượt**, trộn lẫn; gọi người thứ hai khi chênh nằm trong [−0,75; +0,25] | Cả hai bản, cộng 3 mẫu kiểm |
| AFTER đạt/trượt | Người thứ nhất trượt đúng một mục, hoặc điểm AFTER trong ±0,5 quanh 7,5 | Ảnh AFTER |

- Người thứ hai cũng là subagent mới, cũng phải qua mẫu kiểm (5.1).
- Điểm cuối của một ảnh = trung bình hai người, làm tròn 0,25. Hai người lệch nhau > 1,0 ở một ảnh: gọi người thứ ba, lấy trung vị ba điểm.
- AFTER: hai người khác nhau ở đạt/trượt thì gọi người thứ ba, theo đa số.
- Người dựng không bao giờ là người thứ hai.

### 5.3 Cổng dùng điểm giám khảo

| Cổng | Ngưỡng (MAP_PLAN §3.4) |
|---|---|
| A (chặng A) | Trung vị 12 ảnh ≥ 7,5; không ảnh nào < 6,5 |
| B (luật thay tay) | Không thấp hơn A quá 0,25; L2-cau lật gương, khung mặc định ≥ 7,5 |
| C (ship) | Khung mặc định và 4 hướng ở 55° mỗi ảnh ≥ 8; trung vị 12 ảnh ≥ 8; không ảnh nào < 7; AFTER ≥ 7,5 và đạt; sự sống ≥ 7 trên dải 10 s |
| Triển khai R1 trở đi (MAP_PLAN §4.1) | Khung mặc định của ải dựng tay, 1 trên 10 ải còn lại, mọi ải trượt số đo ảnh |

Số đo ảnh đạt mà giám khảo < 8 thì kit là giới hạn (MAP_PLAN §3.5); số đo trượt thì sửa luật bố cục trước khi chấm lại.

## 6. Từ điển góp ý

Đổi lời chủ dự án hoặc góp ý của giám khảo thành tham số. Một câu có thể khớp nhiều mã; sửa mã có điểm con thấp nhất trước.

**Tên tham số:** khóa `layers.*` là của spec L2-cau đề xuất (map-spec/0, [spike §6.9](../../../docs/tools/map-factory/spike-l2-cau.md)); "(v1)" là trường của MapSpec v1 chưa có, hôm nay là hằng số trong mã spike (`src/view/layout.ts` `LAYOUT_RULES`, `paint.ts`, `stage.ts`, `terrain.ts` của worktree spike). Dòng nào ghi "(v1)" thì sửa hằng số đó trong worktree bản thử, và dời vào spec khi v1 có.

**Số đo kiểm:** dòng Q5 là số đo ảnh của MAP_PLAN §2.9. Phép đo chính thức (MF-C03, MF-C04, hàng 073/074) **chưa có**; tới lúc đó dùng số đo tạm của Claude (script `stats*.mjs` ngày 28/10, ảnh thu về 384×216), ghi rõ "số tạm" trong báo cáo.

| Mã | Lời thường gặp | Điểm con | Luật | Đổi gì (tham số, chiều) | Kiểm bằng |
|---|---|---|---|---|---|
| FB-01 | "Tối quá", "u ám" | `sang_toi`, `gom_sang` | V2, §2.5 | `renderer.toneMappingExposure` (`stage.ts` L190, đang 1) lên 1,05–1,15; màu đất của đèn bán cầu `#6f5d80` → khoảng `#6d7a5a` (`stage.ts` L205); tông đồng cỏ `uGrassMid`, `uGrassLight` sáng lên; mặt trời cao 45–55° (v1 `lighting`); bớt mật độ rừng mép trong khung (`vegetation.edge`) | Q5 luma trung bình ≥ 0,48; rất tối ≤ 6 % |
| FB-02 | "Rối", "nhiễu", "lắm chấm" | `dong_yen`, `nhip_mat_do` | V2, V4, V14 | decal ở bãi trống ≤ 30 % lưới hôm nay (ô lưới `paint.decals.*` lớn hơn, mật độ dồn về mép); `vegetation.groves.countMax` 12 → ≤ 7; trọng số stroke ≤ 0,08 (`paint.ts` L407, đang 0,26); biên độ mảng ±4–5 % luma; `rocks.lane.runPermille` giảm | Q5 độ rối ≤ 0,050 |
| FB-03 | "Rừng như bức tường" | `khung`, `mep` | V6 | vịnh mỗi 60–90°, sâu 6–10 m, chứa một cây hay một lùm nhỏ; 2–3 mũi; nhiễu mép ±4 m; khe ở mọi cổng (v1, cạnh `vegetation.edge.insideCm`); ngọn cây sáng hơn | Q5 xanh két tối ≤ 6 % |
| FB-04 | "Trống", "chán", "thiếu điểm nhấn" | `nhip_mat_do`, `diem_mau` | V5, V7 | cây lẻ `vegetation.solitary.count` (cách 6–10 m, chỉ ở dải chuyển tiếp); cây tán ấm 5–10 % số cây bằng nhuộm cây tán tròn (V7); thêm sự sống (FB-06). Không thêm decal ở bãi trống | Q5 điểm ấm 0,5–2 % |
| FB-05 | "Đường không rõ", "lối mờ" | `loi_va_do` | V8, V3 | lối chính `paths.widthCm` 105 → 140–160, phủ khoảng 95 %, bỏ dải cỏ giữa; lối nhánh 90, giữ dải cỏ; viền tối 0,15–0,25 m, tối hơn cỏ 25–35 % | Ảnh nheo mắt: lối đọc thành nét |
| FB-06 | "Thiếu sức sống", "đứng im" | `su_song` | §2.5 L8 | `layers.life` (v1): 2–3 đàn chim 3–6 con mỗi 15–30 s, cao 12–18 m; 10–20 bướm ở mép bãi; khói từ Campfire Ring; bóng mây −6 đến −8 % luma, 1–2 m/s; một trường gió chung | Dải 10 s; ≤ 0,15 ms, ≤ 3 draw call |
| FB-07 | "Dời ao", "ao chỗ khác" | `tieu_diem`, `bo_cuc` | V12, LG3 | `water.ponds[].site`: `"auto"` → ghim `{x, z}` cm, ghi lý do (ngoại lệ ghim); giữ `clearCm`; ứng viên L2-cau (19; 7) m | Q4: tiêu điểm phụ ≥ 80 % trong khung |
| FB-08 | "Tím quá", "màu lạ", "như đồ chơi" | `diem_mau` | V13, LG8 | `vegetation.edge.violetPermille` 180 → ≤ 80; lùm tím chỉ khi cách làn ≥ 9 m (`violetClearCm` 900, `LAYOUT_RULES.groves.violetLaneM`); thông về hue 120–150, ngọn sáng hơn | Q5 tím ≤ 1 % |
| FB-09 | "Chấm đỏ như máu", "lẫn màu cảnh báo" | `diem_mau`, AFTER A4 | V3, V7, LG8 | bỏ chấm lá đỏ trong decal đất và vụn rừng (D1, D3); cây ấm hue 10–30°, S ≤ 0,70, V ≤ 0,70, ΔE2000 ≥ 20 với `#FF4A4A`, `#FFB020`, `#FFC83A`; cách làn và ô ≥ 9 m | Lint khoảng cách; ΔE |
| FB-10 | "Vách như trứng", "vách sọc" | `cao_do`, `khung` | V10, LG4 | vạch tầng mỗi 1,8 m → 3 tầng khoảng 3 m, mặt trên sáng (sơn vách trong `terrain.ts`); bỏ tảng tròn rêu trên mặt vách (`rocks.cliff.face`, thay bằng Cliff Rock của kit đợt 3); bãi 10–20 đá nhạt 0,8–2 m dưới chân; vách ở phía pháp tuyến · nắng ≥ 0,3 | LG4 (Q3) |
| FB-11 | "Cây rắc đều như tiêu", "đốm đều" | `nhip_mat_do`, `bo_cuc` | V4, V5 | gom về lùm: ≤ 7 lùm, cách nhau ≥ 8 m (`vegetation.groves.gapCm` 350 → 800), ≥ 70 % một loài, 1–2 lùm neo R 7–9 m nhập rừng mép; rải nhiễu xanh chỉ trong mặt nạ; bỏ bụi rời ở bãi trống | Q4: ≤ 7 lùm, cách ≥ 8 m |
| FB-12 | "Đất tròn như đóng dấu" | `mep` | V3 | đĩa đất = 2–3 elip chồng, nhiễu bán kính ≤ ±25 %, 3–5 thùy, lệch 0,3–0,5 R về phía khuất nắng (v1, cạnh `paint.groveDirtPermille`, `paint.loneDirtCm`); viền tối 0,15–0,25 m rồi quầng cỏ nhạt khoảng 1 m | Xem ảnh gần |
| FB-13 | "Không thấy trung tâm", "bệ chìm" | `tieu_diem` | V12, LG6 | viền bệ (đá hoặc vòng cỏ sẫm); sân bệ `paint.plazaCm` 650; trần chiều cao cây gần bệ `vegetation.groves.heightCapCm`; đèn, rào dày gần bệ, thưa dần về cổng | Q4 |
| FB-14 | "Đồng cỏ sọc", "vằn" | `dong_yen`, `sang_toi` | V2 | bỏ ba tông phân bậc `band` (`paint.ts` L407–410 ở spike; `terrain.ts` L921–922 ở `main`); thay bằng một mảng nhiễu mềm 20–30 m; tông sẫm chỉ dưới bóng tán và sàn rừng | Q5 cỏ sáng ≥ 35 %; đồng sáng ≥ 30 % |
| FB-15 | "Nước như rừng", "nước đục" | `nuoc` | V11 | hue nước 205–215, giữa sâu hơn (shader `water.ts`); Reed Clump ở bờ chậm; Wooden Jetty ở cuối một lối mòn; lá súng | Q5 xanh két tối ≤ 6 % |
| FB-16 | "Thiếu đèn, rào", "đường trơn" | `loi_va_do` | V9 | Lantern Post mỗi 9–12 m trên lối chính, đổi bên, cách mép 0,9 m, cách ô ≥ 4,6 m, cách làn ≥ 2,2 m; Rail Fence 2–4 đoạn ở khúc cong và đầu cầu (`along.ts`, phiếu 033); dọc làn chỉ cọc thấp ≤ 1,2 m | Lint khoảng cách |
| FB-17 | "Quái khó thấy", "chữ khó đọc" | AFTER A1, A2, A5 | V15, Q6 | giảm độ sáng và độ bão hòa của cảnh gần làn (tông đồng, decal, hoa); trần chiều cao cây gần làn; không điểm sáng dưới vùng giao diện | Q6: `dh-crowd`, `dh-telegraphs`, tương phản quái với nền |
| FB-18 | "Vô lý", "lối mòn đi đâu", "cong vô cớ" | `bo_cuc`, `loi_va_do` | LG1, LG2, LG5 | lối mòn phải tới đích (cầu tàu ở ao, bãi đá chân vách, bếp lửa, khe rừng); không dừng ở ô; vật gây cong trong 6 m ở mỗi khúc ≥ 15°; khe rừng có vệt đường ở mỗi cổng | Q3 (`checks/logic.ts` khi có) |

## 7. Phép thử bộ kit

Tiêu chí của CL-03: một giám khảo mới chấm ba mẫu, mỗi số trong ±0,75.

**Lượt 28/10 (không độc lập):** lane này không gọi được subagent, nên người viết bộ kit tự chấm ba mẫu, theo đúng mục 4 (xem ảnh mẫu, bản nhỏ 384 px rồi bản đầy đủ của từng ảnh; điểm con theo bảng mốc; trung bình có trọng số).

Chạy đúng công thức ở mục 3 (xáo, đổi tên `anh-01`…`anh-03`, bản nhỏ 384 px); đoạn mã kiểm ở bước 3 in "mẫu: đạt" cho cả ba.

| Mẫu | Đích | Trung bình có trọng số | Điểm chung | Lệch | Trong ±0,75? |
|---|---|---|---|---|---|
| Ảnh mẫu | 10 | 9,88 | 10 | 0 | Có |
| M0b mặc định | 4,75 | 4,46 | 4,5 | −0,25 | Có |
| Spike `final2` mặc định | 6,75 | 6,59 | 6,5 | −0,25 | Có |

Điểm con (để so khi một giám khảo sau lệch; thứ tự như bảng mốc):

| Mẫu | bo_cuc | gom_sang | dong_yen | mep | tieu_diem | diem_mau | nhip_mat_do | khung | cao_do | sang_toi | loi_va_do | nuoc |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ảnh mẫu | 10 | 9,5 | 10 | 10 | 10 | 10 | 10 | 10 | 9,5 | 10 | 9,5 | 10 |
| M0b | 5 | 4,5 | 4 | 4 | 5 | 4 | 4,5 | 4 | 4 | 5 | 3 | 6,5 |
| Spike | 6,5 | 6,5 | 6 | 7 | 7 | 6 | 7 | 6,5 | 6,5 | 6,5 | 6,5 | 7,5 |

Góp ý đã gắn mã: spike FB-14 (sọc chéo giữa đồng), FB-03 (tường thông mép phải), FB-10 (vách góc trên trái); M0b FB-11 (bụi rắc đều), FB-08 (quả cầu tím, lam), FB-03 (viền nón xanh két). Khớp các lỗi spike §3, §8 và MAP_PLAN §2.4 đã ghi.

Không phải sửa lời nhắc: cả ba trong dung sai. Hai mốc giữa cùng thấp hơn đích 0,25, tức thang hơi chặt. Theo dõi ở lượt subagent đầu tiên: nếu cả hai lại thấp hơn đích ≥ 0,5, nới mô tả cột "7" (luật trần) trước khi chấm ảnh thật.

**Giới hạn của lượt này:** người chấm đã viết thang và biết điểm đích, nên đây không phải phép thử độc lập. Nó chỉ chứng minh thang **có thể** cho đúng ba điểm đích khi đọc đúng mô tả. Lượt chấm đầu tiên có subagent (CL-06, cổng A) chính là phép thử thật: nếu một mẫu kiểm trượt ở đó, sửa mô tả mốc theo 5.1 trước khi lấy điểm ảnh thật.

## 8. Giới hạn

- Ảnh mẫu là một game khác, một góc camera khác. Thang chấm chất lượng cảnh, không chấm "giống ảnh mẫu".
- Mốc 7 và 4 của thang được viết từ lỗi thật của spike và M0b. Khi luật mới sửa hết các lỗi đó, phần trên 8 của thang chỉ còn ảnh mẫu làm neo; cần thêm một mốc 8 (bản thử đã được chủ dự án nói "đạt") sau cổng C.
- Sự sống chỉ chấm trên dải 10 s; ảnh tĩnh không có điểm sự sống.
- Kit khác cần ảnh mẫu và mẫu kiểm riêng (mục 2).
