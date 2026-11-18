# 328 · Critic · **FAIL**

**FAIL**: 2 lỗi chặn. Phần còn lại đúng. Đã kiểm: đo lại 7 hộp sáng, khớp từng số. Tính lại 7 vùng cắt, cỡ ra và aspect, đều khớp bảng (`m` tính từ cạnh hộp sáng). Tổng GPU ≈ 26,9 MB. Mọi dòng nêu trong `fxkit.ts`, `sword-rain.ts`, `sword-skills.ts` đúng chỗ. Lệnh `magick` crop/flop chạy được; PNG ra không có gAMA và md5 lặp lại y hệt. Tranh line và arrow có mũi về +x. Gốc `tsc` sạch. Node không có `location`, nên test cũ vẫn đi đường cũ. Lab tự nạp tranh qua constructor `SwordSkillFx`, không chạm `skills-main.ts`. Phiếu có đủ luật báo cáo và luật `CODEX-WAIT-UNTIL`.

## Sửa bắt buộc
1. **§4 Fragment `GroundMarks` không biên dịch.** Khối PAINTED đặt ở đầu `main()` khai `rev`, `add`, `a` cùng tầm với `float rev` (dòng 424), `vec3 add` (443) và `float a` (444) của đường cũ. GLSL cấm khai lại trong cùng tầm, nên khi bật PAINTED cả vết nứt lẫn rãnh đều mất. Test node không bắt được lỗi này, và phiếu cấm chạy trình duyệt. Thay câu "đầu `main()` (dòng 385) thêm:" bằng:
   "đầu `main()` (dòng 385) thêm khối dưới, **bọc trong `{ … }`** ngay sau `#ifdef PAINTED` và trước `#endif`. Lý do: GLSL cấm khai lại `rev`, `add`, `a` của dòng 424, 443, 444 trong cùng tầm `main`."
2. **Ăn mòn không bao giờ về 0.** Với `smoothstep(1.0 - uFade - 0.15, 1.0 - uFade + 0.001, x)`, điểm `x = 1` vẫn sáng đủ khi `uFade` hay `vLook.x` tiến về 0. Đo trên tranh hex, line và crack: 13–15 % vùng sáng có `v > 0.89`. Các nét sáng nhất và lõi HDR giữ nguyên tới khung `hide()` (`fadeOutEased`), hoặc tới lúc `push` bỏ mục (alpha ≤ 0.003; sao nứt giữ glow 0.8, heat ≥ 0.8), rồi tắt phụt. Như vậy trái luật "fast attack, slow decay". Thay:
   - §3: `fadeK = smoothstep((1.0 - uFade) * 1.1 - 0.1, (1.0 - uFade) * 1.1, max(s.r, s.g * 0.6)); // erosion as SOLID: faint parts first, none at uFade 0`
   - §4: `float er = smoothstep((1.0 - vLook.x) * 1.1 - 0.1, (1.0 - vLook.x) * 1.1, max(s.r, s.g * 0.6)) * rev;`

## Ghi chú (không chặn)
- Mục Phạm vi: `git -C W status --short` đã sẵn có `?? art-src` và `?? node_modules`. Thêm "ngoài hai liên kết có sẵn đó".
- CLI đọc RGB thô của tranh (≈ 4,7 MB) qua `execFileSync`, vượt `maxBuffer` mặc định 1 MiB. Ghi rõ `maxBuffer: 64 << 20` và không đặt `encoding`.
- Test ảnh thật phải tự gọi `magick` để lấy `maxCh`, vì lib chỉ có hàm thuần. Dùng `skipIf` cả khi thiếu `magick`.
- Cộng dồn 0.02 cho `hotT` ra `0.9500000000000002`. Trong test dùng `toBeCloseTo(0.95)`, hoặc tính `t = 0.75 + 0.02·k` với `k` nguyên.
- `loadPaintedSigils`: bọc cả `fetch` lẫn `res.json()` trong try/catch, để JSON hỏng cũng ra `null` kèm cảnh báo.
- Ảnh chụp lab bấm chiêu ngay lúc tải trang có thể ra bản code trước khi mặt nạ nạp xong. Nếu cần, xuất `sigilsReady: Promise<void>` công khai trên `SwordSkillFx`.
