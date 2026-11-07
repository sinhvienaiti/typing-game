# Làn 1 · Sửa vòng phản hồi Framebuffer (nguồn của glError 1282)

Bằng chứng (Claude, 07/11 10:30, console lab 3146): `GL_INVALID_OPERATION: glDrawArrays: Feedback loop formed between Framebuffer and active Texture`, lặp nhiều lần ngay sau khi nạp trang. Một lượt vẽ đang đọc chính texture mà nó đang ghi vào. B9 đã thêm test quanh `hybrid-ab.ts` nhưng chưa tìm ra chỗ.

**Mức `high`.** Worktree `games/.wt-ic-lab-all`.

## Việc
1. Tìm lượt vẽ dùng render target đang gắn làm texture đầu vào. Nghi vấn:
   - bước bloom hay hậu kỳ dùng lại một target;
   - bước làm ấm (prewarm) vẽ vào target đang được sample;
   - `FlipbookPlayer` hoặc lớp tô dùng `renderer.getRenderTarget()`.
   Đọc các chỗ gọi `setRenderTarget`, `EffectComposer`, `WebGLRenderTarget` trong `src/`.
2. Sửa bằng ping-pong target, hoặc tách target. Không tắt hiệu ứng, không đổi hình.
3. Có test node tái hiện thứ tự gọi sai bằng renderer giả.
4. Báo cáo ghi cách Claude kiểm trong trình duyệt: console không còn dòng trên.

## Ranh giới
- **Được ghi:** các file trong `src/` liên quan, tối thiểu; test; báo cáo.
- **Không:** sửa media.

## Đạt khi
`npx --no-install tsc --noEmit` sạch và `npx --no-install vitest run --maxWorkers=4` qua toàn bộ.
