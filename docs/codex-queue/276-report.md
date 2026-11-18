# Phiếu 276 · Lọc take Firefly bằng số đo

Ngày 2026-11-05T02:11:58+07:00 · Kết quả kiểm: **PASS**.

Đã đo **428 take âm và 12 tiếng hô**, thuộc 83 việc. Phiếu ghi 424 nhưng JSON hiện tại ghi 428 (107 generation); số WAV thực tế khớp 428. Đo cả 4 take chênh, không có take bị bỏ sót.

Có **139 take listen**: 67 việc đủ hai take, 5 việc còn một take, 11 việc bị loại cả việc. Tổng 124 take bị loại; lý do từng take nằm trong picks.md và picks.json. Tiếng hô chỉ đo, không chấm điểm hay chọn take.

Các cổng ghi nhận: 120 take cắt đỉnh, 4 take lặng đầu quá 60 ms, 0 take trùng. Tổng thời gian hai lượt nghe, gồm khoảng lặng, là 451.2 s. Callouts thực tế là mono 48 kHz; cả 428 take âm là stereo 48 kHz.

## Đầu ra

Tất cả file nghe nằm tại `.local/codex-runs/276-out/`:

- `picks.json`, `picks.md`: số đo, hạng, listen, cổng loại, cờ DSP, giải thích cách chọn và cặp gần trùng.
- 16 MP3 (hai hạng × tám nhóm), `ORDER-<nhóm>.txt` và `ORDER-<nhóm>-rank2.txt`: thời gian bắt đầu theo giây, id, take, độ dài và priority.
- `validation.json`, `md5-before.json`, `md5-after.json`, `*.ffprobe.json`: bằng chứng kiểm; `measurements.jsonl`: lưu từng phép đo để tiếp tục khi gián đoạn.
- `independent-verification.json`: kiểm lại ORDER, lựa chọn, bitrate và số khung giải mã; `cross-meter-checks.json`: đối chiếu bốn mẫu bằng ffmpeg EBU R128.
- `jobs-snapshot.json`: bản JSON đầu vào tại lúc bắt đầu; `tools/pick_firefly.py`: script tái chạy bằng venv có sẵn.

## Luật đã chạy

Đây là sàng lọc bằng số đo, chưa nghe và chưa nghiệm thu chất âm. Điểm 0–100 chỉ so các take cùng id; không phải điểm chất lượng /10.

- LUFS-I: pyloudnorm, K-weighting và cổng BS.1770, cửa sổ 400 ms. True peak: ước lượng nội suy polyphase ×4 của Audio Lab; ghi dBTP. Không thay đổi mẫu nguồn.
- Cắt đỉnh: dùng clip_scan L1 của Audio Lab: ≥3 mẫu liền có |x| ≥0,999 FS hoặc ≥4 mẫu đỉnh phẳng trên −20 dBFS, gần đỉnh kênh 1 dB, có bảo vệ đỉnh tròn PCM16. Đếm mẫu bị cắt trên cả hai kênh, hợp các vùng để không đếm hai lần; cũng ghi số mẫu sát trần và chạm rail riêng.
- DC: hàm dc_estimate của Audio Lab, trung vị các trung bình Hann 40 ms ở vùng lặng (hoặc cả file nếu không có vùng lặng); ghi FS. Trung bình thô từng kênh được lưu riêng.
- Lặng đầu: trước mẫu đầu tiên của bất kỳ kênh nào ≥−60 dBFS. Cổng loại khi >60 ms, chỉ miễn id có loop hoặc drone. Gần như im lặng: peak hoặc LUFS-I ≤−60, hoặc không đo được LUFS; file lỗi cũng bị loại.
- Tấn công: bao RMS stereo theo khung 1 ms, từ lần đầu ≥−40 dB tới lần đầu ≥−6 dB so với đỉnh bao toàn file. Không dùng sóng đổi dấu để đo. Khi đầu file đã trên −40 dB, gắn cờ phép đo bị thiếu phần trước file.
- Đuôi: từ đỉnh bao tới khung cuối trên −60 dB tương đối. Nếu chưa về −60 trước hết file, tail_to_minus60_s=null, báo cận dưới tail_observed_s, không ngoại suy RT60. Cờ này không tự loại take.
- Crest: đỉnh mẫu / RMS của các khung 1 ms trên −40 dB tương đối, giúp khoảng lặng không thổi phồng crest. Có thêm crest toàn file. Phổ Welch Hann 4096, chồng 50%, lấy trung bình năng lượng hai kênh; trọng tâm theo biên độ sqrt(PSD); phần năng lượng thấp là 0<f<120 Hz / toàn phổ f>0 (đã bỏ DC). Ghi thêm RMS qua lọc thấp 120 Hz.
- Độ liền đuôi: tỉ lệ khung còn trên −40 dB từ đỉnh đến cuối đuôi; độ nhảy P95 dB giữa khung 10 ms và số bước tăng >6 dB. Chỉ tính cặp khung cùng hoạt động; tiếng lách tách cố ý vẫn cần tai người.
- Loop: so 100 ms đầu/cuối, chênh RMS dB; chênh phổ Jensen–Shannon (bit, 0 giống nhau); chênh trọng tâm Hz; bước nhảy mẫu vượt P95 bước nhảy bình thường. Không crossfade, không sửa mối nối.
- Trùng: bỏ lặng dưới −60 dB tương đối ở hai đầu CHỈ trên bản đo trong RAM, hạ xuống 8 kHz, bỏ trung bình từng kênh, tương quan waveform stereo chuẩn hóa; thử độ trễ ±100 ms, đổi L/R và đảo cực. Cần độ dài hoạt động khớp ≥95%, chồng ≥95%, |r|≥0,985. Cụm nối bởi các cặp trùng giữ take qua cổng gốc có điểm cao nhất (hòa chọn số take nhỏ); còn lại bị loại. Tất cả cặp có trong JSON. Đây là phép dò gần trùng waveform, không phải nhận dạng nội dung bằng AI.
- Cờ DSP bổ sung: true peak >−1 dBTP, DC≥0,001 FS, lệch hai kênh >1,5 dB, tương quan stereo âm, đuôi chưa tắt, đuôi tăng đột biến. Cờ không thêm cổng loại ngoài phiếu; không khẳng định phát hiện hết lỗi L1b như rung cao độ, rít hay xoáy pha.

Xếp hạng: từng chỉ số đưa về [0,1] bằng min–max trong các take qua cổng gốc của cùng id; chỉ số bằng nhau nhận 0,5. Điểm =100×tổng trọng số. Sau đó loại trùng và xếp lại hạng; hòa chọn take số nhỏ. Không thưởng/phạt LUFS nên không ép âm chiến đấu thành nhỏ, mềm.

| Luật | Trọng số |
|---|---|
| impact/hit/burst/slash/crack/boom/clash/ignite/release | tấn công nhanh 45%; crest cao 30%; năng lượng dưới 120 Hz 25% |
| tail/drone/echo/swell/rumble | đuôi quan sát dài 45%; tỉ lệ đuôi liền 30%; ít nhảy P95 và bước tăng đột biến 25% |
| loop | lệch mức nhỏ 40%; lệch phổ JS nhỏ 40%; bước nhảy dư nhỏ 20% |
| sparkle/glint/shimmer/whoosh/flyby | trọng tâm phổ sáng 60%; tấn công gọn 40% |

Ưu tiên phân loại: loop → tail → impact → bright. Tail thắng release khi id là release-tail. Từ khóa là từng thành tố id, nên crackle không bị hiểu thành crack. Id còn lại chọn luật gần nhất bằng vai trò lớp, ghi rõ dưới từng việc. Điểm min–max chỉ tạo thứ tự tương đối trong ít ứng viên, không chứng minh đúng vật liệu, lực, lớp hay độ vang; anh nghe là cổng cuối theo Q6.

## Kiểm bắt buộc

1. Đủ 428/428 take âm thực tế và 12/12 tiếng hô; lỗi đo: 0.
2. Mỗi việc có listen hoặc ghi rõ cả việc bị loại; 11 việc bị loại cả việc được liệt kê bên dưới.
3. Xuất 16 MP3; ffprobe đọc được và sai lệch so tổng ORDER ≤0,1 s. Bảng bên dưới ghi từng file.
4. MD5 toàn bộ 428 WAV sound không đổi: **True**; cả 12 WAV callouts không đổi: **True**.

| File MP3 | Take | Tổng ORDER s | ffprobe s | Lệch s |
|---|---:|---:|---:|---:|
| twin-dragons-rank1.mp3 | 15 | 58.700000 | 58.700000 | 0.000000 |
| twin-dragons-rank2.mp3 | 13 | 46.100000 | 46.100000 | 0.000000 |
| ultimate-k5-rank1.mp3 | 8 | 36.100000 | 36.100000 | 0.000000 |
| ultimate-k5-rank2.mp3 | 8 | 36.100000 | 36.100000 | 0.000000 |
| cut-in-rank1.mp3 | 5 | 15.200000 | 15.200000 | 0.000000 |
| cut-in-rank2.mp3 | 5 | 15.200000 | 15.200000 | 0.000000 |
| hit-confirm-kills-rank1.mp3 | 13 | 30.100000 | 30.100000 | 0.000000 |
| hit-confirm-kills-rank2.mp3 | 12 | 26.300000 | 26.300000 | 0.000000 |
| fire-rank1.mp3 | 8 | 26.100000 | 26.100000 | 0.000000 |
| fire-rank2.mp3 | 8 | 26.100000 | 26.100000 | 0.000000 |
| metal-rank1.mp3 | 7 | 21.000000 | 21.000000 | 0.000000 |
| metal-rank2.mp3 | 7 | 21.000000 | 21.000000 | 0.000000 |
| per-skill-rank1.mp3 | 7 | 19.000000 | 19.000000 | 0.000000 |
| per-skill-rank2.mp3 | 6 | 15.200000 | 15.200000 | 0.000000 |
| shared-big-layers-rank1.mp3 | 9 | 32.400000 | 32.400000 | 0.000000 |
| shared-big-layers-rank2.mp3 | 8 | 26.600000 | 26.600000 | 0.000000 |

Kiểm độc lập: **PASS**. Đọc lại ORDER từ file, đối chiếu take được chọn và WAV nguồn; cả 16 MP3 là 192 kbps, stereo 48 kHz. Giải mã toàn bộ 16 file không lỗi; số khung PCM khớp chính xác tổng WAV + khoảng lặng, không mất đầu/đuôi vì padding MP3. Không phát âm ra loa trong bước này.

Đối chiếu độc lập bốn mẫu (chuông, trúng, loop, tiếng hô) bằng ffmpeg ebur128: lệch LUFS-I tối đa 0.0608 LU; true peak tối đa 0.0425 dB giữa hai bộ nội suy. ffmpeg in số đo đến 0,1 đơn vị; số đo đầy đủ vẫn giữ trong JSON.

## Cần anh/Claude xem

Máy chưa nghe take nào; thứ hạng không phải nghiệm thu chất âm. Claude chép MP3 và ORDER sang thư mục review đúng phiếu, gửi anh nghe theo nhóm và ghi take anh chọn. Ưu tiên kiểm lực, thân, lớp và độ vang theo Q6; số đo không xác nhận được những phần này.

Các việc bị loại cả việc (không được lén đưa take loại vào MP3):

- `tt-sfx-twin-bell-giant` — cả việc bị loại: take1: cắt đỉnh: 37 mẫu, 0 đoạn sát trần, 9 đoạn đỉnh phẳng; take2: cắt đỉnh: 30 mẫu, 0 đoạn sát trần, 7 đoạn đỉnh phẳng; take3: cắt đỉnh: 30 mẫu, 0 đoạn sát trần, 7 đoạn đỉnh phẳng; take4: cắt đỉnh: 25 mẫu, 0 đoạn sát trần, 6 đoạn đỉnh phẳng; take5: cắt đỉnh: 318 mẫu, 0 đoạn sát trần, 66 đoạn đỉnh phẳng; take6: cắt đỉnh: 74 mẫu, 0 đoạn sát trần, 16 đoạn đỉnh phẳng; take7: cắt đỉnh: 4 mẫu, 0 đoạn sát trần, 1 đoạn đỉnh phẳng; take8: cắt đỉnh: 4 mẫu, 0 đoạn sát trần, 1 đoạn đỉnh phẳng
- `tt-sfx-twin-deep-boom` — cả việc bị loại: take1: cắt đỉnh: 13290 mẫu, 0 đoạn sát trần, 1213 đoạn đỉnh phẳng; take2: cắt đỉnh: 6467 mẫu, 0 đoạn sát trần, 678 đoạn đỉnh phẳng; take3: cắt đỉnh: 11981 mẫu, 0 đoạn sát trần, 1126 đoạn đỉnh phẳng; take4: cắt đỉnh: 16307 mẫu, 0 đoạn sát trần, 1754 đoạn đỉnh phẳng; take5: cắt đỉnh: 9835 mẫu, 0 đoạn sát trần, 1225 đoạn đỉnh phẳng; take6: cắt đỉnh: 19361 mẫu, 0 đoạn sát trần, 2096 đoạn đỉnh phẳng; take7: cắt đỉnh: 6185 mẫu, 0 đoạn sát trần, 842 đoạn đỉnh phẳng; take8: cắt đỉnh: 11153 mẫu, 0 đoạn sát trần, 1151 đoạn đỉnh phẳng
- `tt-sfx-twin-mountain-echo` — cả việc bị loại: take1: cắt đỉnh: 85 mẫu, 0 đoạn sát trần, 14 đoạn đỉnh phẳng; take2: cắt đỉnh: 56 mẫu, 0 đoạn sát trần, 11 đoạn đỉnh phẳng; take3: cắt đỉnh: 21 mẫu, 0 đoạn sát trần, 5 đoạn đỉnh phẳng; take4: cắt đỉnh: 123 mẫu, 0 đoạn sát trần, 24 đoạn đỉnh phẳng; take5: cắt đỉnh: 106 mẫu, 0 đoạn sát trần, 23 đoạn đỉnh phẳng; take6: cắt đỉnh: 250 mẫu, 0 đoạn sát trần, 52 đoạn đỉnh phẳng; take7: cắt đỉnh: 16 mẫu, 0 đoạn sát trần, 3 đoạn đỉnh phẳng; take8: cắt đỉnh: 76 mẫu, 0 đoạn sát trần, 16 đoạn đỉnh phẳng
- `tt-sfx-twin-sub-hit` — cả việc bị loại: take1: cắt đỉnh: 375 mẫu, 0 đoạn sát trần, 56 đoạn đỉnh phẳng; take2: cắt đỉnh: 522 mẫu, 0 đoạn sát trần, 57 đoạn đỉnh phẳng; take3: cắt đỉnh: 5 mẫu, 0 đoạn sát trần, 1 đoạn đỉnh phẳng; take4: cắt đỉnh: 1405 mẫu, 0 đoạn sát trần, 133 đoạn đỉnh phẳng
- `tt-sfx-ult-release-instant` — cả việc bị loại: take1: cắt đỉnh: 76 mẫu, 0 đoạn sát trần, 15 đoạn đỉnh phẳng; take2: cắt đỉnh: 24 mẫu, 0 đoạn sát trần, 6 đoạn đỉnh phẳng; take3: cắt đỉnh: 9 mẫu, 0 đoạn sát trần, 2 đoạn đỉnh phẳng; take4: cắt đỉnh: 104 mẫu, 0 đoạn sát trần, 23 đoạn đỉnh phẳng; take5: cắt đỉnh: 51 mẫu, 0 đoạn sát trần, 11 đoạn đỉnh phẳng; take6: cắt đỉnh: 18 mẫu, 0 đoạn sát trần, 4 đoạn đỉnh phẳng; take7: cắt đỉnh: 12 mẫu, 0 đoạn sát trần, 3 đoạn đỉnh phẳng; take8: cắt đỉnh: 90 mẫu, 0 đoạn sát trần, 17 đoạn đỉnh phẳng
- `tt-sfx-ult-close-tail` — cả việc bị loại: take1: cắt đỉnh: 87 mẫu, 0 đoạn sát trần, 19 đoạn đỉnh phẳng; take2: cắt đỉnh: 525 mẫu, 0 đoạn sát trần, 105 đoạn đỉnh phẳng; take3: cắt đỉnh: 106 mẫu, 0 đoạn sát trần, 23 đoạn đỉnh phẳng; take4: cắt đỉnh: 771 mẫu, 0 đoạn sát trần, 137 đoạn đỉnh phẳng
- `tt-sfx-ult-heaven-drone` — cả việc bị loại: take1: cắt đỉnh: 28 mẫu, 0 đoạn sát trần, 7 đoạn đỉnh phẳng; take2: cắt đỉnh: 104 mẫu, 0 đoạn sát trần, 21 đoạn đỉnh phẳng; take3: cắt đỉnh: 92 mẫu, 0 đoạn sát trần, 18 đoạn đỉnh phẳng; take4: cắt đỉnh: 41 mẫu, 0 đoạn sát trần, 9 đoạn đỉnh phẳng
- `tt-sfx-elite-death-bronze` — cả việc bị loại: take1: cắt đỉnh: 41 mẫu, 0 đoạn sát trần, 9 đoạn đỉnh phẳng; take2: cắt đỉnh: 597 mẫu, 0 đoạn sát trần, 74 đoạn đỉnh phẳng; take3: cắt đỉnh: 267 mẫu, 0 đoạn sát trần, 48 đoạn đỉnh phẳng; take4: cắt đỉnh: 128 mẫu, 0 đoạn sát trần, 18 đoạn đỉnh phẳng
- `tt-sfx-auto-low-punch` — cả việc bị loại: take1: cắt đỉnh: 4 mẫu, 0 đoạn sát trần, 1 đoạn đỉnh phẳng; take2: cắt đỉnh: 4 mẫu, 0 đoạn sát trần, 1 đoạn đỉnh phẳng; take3: cắt đỉnh: 201 mẫu, 0 đoạn sát trần, 34 đoạn đỉnh phẳng; take4: cắt đỉnh: 55 mẫu, 0 đoạn sát trần, 9 đoạn đỉnh phẳng
- `tt-sfx-thunder-crack` — cả việc bị loại: take1: cắt đỉnh: 57 mẫu, 0 đoạn sát trần, 12 đoạn đỉnh phẳng; take2: cắt đỉnh: 43 mẫu, 0 đoạn sát trần, 6 đoạn đỉnh phẳng; take3: cắt đỉnh: 77 mẫu, 0 đoạn sát trần, 15 đoạn đỉnh phẳng; take4: cắt đỉnh: 35 mẫu, 0 đoạn sát trần, 5 đoạn đỉnh phẳng
- `tt-sfx-sub-drop` — cả việc bị loại: take1: cắt đỉnh: 13741 mẫu, 0 đoạn sát trần, 1865 đoạn đỉnh phẳng; take2: cắt đỉnh: 226 mẫu, 0 đoạn sát trần, 28 đoạn đỉnh phẳng; take3: cắt đỉnh: 4525 mẫu, 0 đoạn sát trần, 583 đoạn đỉnh phẳng; take4: cắt đỉnh: 13227 mẫu, 0 đoạn sát trần, 1400 đoạn đỉnh phẳng

Chỉ còn một take listen: `tt-sfx-twin-flame-flutter`, `tt-sfx-twin-bell-giant-b`, `tt-sfx-mass-kill-chain`, `tt-sfx-guard-body`, `tt-sfx-gong-hit`. Lượt hạng 2 bỏ các id này và ghi chú trong ORDER.

## Phạm vi và tái chạy

Không tạo ảnh hay âm mới, không sửa WAV/prompt nguồn, không normalize/EQ/cắt take, không chạy L3–L5 hoặc model AI. Không chạy build/test game, mở cổng mạng, tải gói hay lệnh git ghi. Không chép sang review vì nằm ngoài phạm vi ghi của phiếu; Claude làm bước đó.

Công cụ chỉ dùng numpy, scipy, soundfile, pyloudnorm có sẵn trong Audio Lab; tái sử dụng trực tiếp clip_scan, dc_estimate, true_peak_dbtp. CLI critic tách được L1/L1b/L2, nhưng dùng thời gian lên 10–90% và mối nối 50 ms; script riêng đo đúng −40→−6 dB và 100 ms của phiếu, thêm so cặp trùng, đồng thời tránh áp cổng final và xuất thẻ ảnh ngoài yêu cầu. Cờ DSP là tập con phép dò, không phải toàn bộ L1b.

```bash
/Users/toandx/AudioLab/.venv/bin/python -B .local/codex-runs/276-out/tools/pick_firefly.py
python3 -B .local/codex-runs/276-out/tools/verify_outputs.py
```

Đo và ghép bằng script riêng, kiểm đầu ra bằng ffprobe và MD5; không chạy bộ kiểm thử Audio Lab chung để tránh ghi ngoài phạm vi. Thư mục output giữ nguyên mức âm từng take nên chênh độ to giữa các take là chủ ý của phiếu.
