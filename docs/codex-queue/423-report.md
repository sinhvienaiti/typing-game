# Phiếu 423 — quay ba clip về bản cũ, làm mềm chân khói trắng

Ngày 16/11/2026. Đã sửa ánh xạ lab và xuất đủ hai bộ `-v2b`. **Kiểm kiểu, probe nguồn và kiểm alpha PNG đều PASS. KTX2 giải mã còn sai số alpha do nén; chưa đạt nghiệm thu alpha tuyệt đối trên đường dùng texture nén.** Không tuyên bố nghiệm thu hình trong lab.

## Tệp đã làm

- `games/.wt-ic-lab-all/src/lab/burst-v2.ts`: bỏ ba hàng `poison-big-burst`, `blood-big-burst`, `thunder-impact`; giữ nguyên metadata nguồn cũ. Thêm hậu tố riêng cho hai hàng khói trắng, mặc định các hàng khác vẫn `-v2`. Dùng cùng hậu tố khi kiểm JSON, dựng tên PNG/KTX2, tải JSON và ghi nhãn grid. Không đổi scale, intensity, shader hoặc các hàng còn lại.
- `games/immortality-cultivation/art-src/lab/vfx/dark/dark-big-burst-white-v2b.{atlas.png,json,uastc.ktx2,prompt.txt}`.
- `games/immortality-cultivation/art-src/lab/vfx/dark/dark-ground-impact-white-v2b.{atlas.png,json,uastc.ktx2,prompt.txt}`.
- `docs/games/tu-tien/skills/VFX_LIBRARY.md`: thêm mục phiếu 423, ghi rõ nguồn cũ được giữ, hai bộ mới và giới hạn KTX2.

Tổng **8 tệp asset mới, 2.025 MiB**. Không ghi đè `-v2`. SHA-256 xác nhận **24 tệp nguồn/bản cũ** trong nhóm khói trắng giữ nguyên. Prompt cạnh mỗi atlas ghi đường dẫn và SHA-256 tham chiếu repo, thao tác chính xác, thông số đóng gói và prompt nguồn phiếu 420 nguyên văn. Đây là xử lý cơ học, không gọi công cụ AI.

## Cách xử lý

Đọc cấu hình `tools/vfx-flipbook/immortality-cultivation.json`, giữ ô 256×256, lưới 8×4, 32 khung, normal RGBA thẳng, RGB nguyên từng pixel, crop/pivot và tail fade 10 khung. `dark-big-burst-white`: 24 fps; `dark-ground-impact-white`: 12 fps.

Lọc thành phần liên thông **8 hướng**, pixel sáng khi **alpha>12/255**; xoá thành phần nhỏ hơn **2% tổng diện tích sáng từng khung**, kèm rìa alpha yếu gán cho thành phần gần nhất. Dải mờ rộng **51 hàng = 19,92% chiều cao ô**, hệ số tuyến tính 1→0. Min tích lũy theo chiều xuống bảo đảm alpha thực đơn điệu, không chỉ hệ số mờ. Lọc lại sau làm mờ tới ổn định.

Lưu ý cách đặt dải: nguồn đã có lề dưới trong suốt, nên dải neo **tại đáy phần có hình chung của cả đoạn**, cố định qua mọi khung; nếu chỉ mờ 51 hàng sát mép ô thì gần như chỉ xử lý lề rỗng. Dải của burst là **y=159–209**, của impact là **y=136–186**, tọa độ gốc trên-trái và bao gồm hai đầu. Phía dưới dải alpha bằng 0. Không dịch chuyển hình hoặc pivot.

Đóng PNG bằng `vfxflip.atlas.write_atlas`; nén qua `tools/vfx-flipbook/run.sh ktx2` với manifest staging riêng trong thư mục tạm. **UASTC mức 2, sRGB, Zstd, Y-flip, 12 mip**, đúng quy trình công cụ hiện có. Không sửa cấu hình hoặc manifest thư viện gốc.

## Kết quả kiểm

`node games/.wt-ic-lab-all/node_modules/typescript/bin/tsc --noEmit -p games/.wt-ic-lab-all/tsconfig.json`: **exit 0, 0 lỗi**, trước và sau sửa. Không chạy build hoặc bộ test game.

Script độc lập quét mọi pixel của **64 khung PNG**:

| Bộ | Alpha hàng đáy lớn nhất | Bước alpha tăng ngược trong dải mờ | Thành phần rời dưới 2% |
| --- | --- | --- | --- |
| `dark-big-burst-white-v2b` | **0** | **0** | **0** |
| `dark-ground-impact-white-v2b` | **0** | **0** | **0** |

Kiểm thêm: RGB giữ nguyên, alpha không tăng so với nguồn ở bất kỳ pixel nào; hình học/nhịp phát/metadata giữ nguyên ngoài danh tính phiên bản và ghi chú xử lý. Đã mở xem cả hai ảnh tám cặp khung trước/sau.

Probe chạy trực tiếp module TypeScript và đọc manifest/JSON thật, không dùng trình duyệt: **PASS 14 hàng, 14 JSON, không cảnh báo**. Ba tên bị bỏ dùng nguyên đối tượng metadata cũ, PNG/KTX2 cũ có thật; không yêu cầu JSON `-v2` cho ba tên này:

| Tên | PNG / KTX2 trong thư mục hệ tương ứng |
| --- | --- |
| `poison-big-burst` | `poison-big-burst.atlas.png` / `poison-big-burst.uastc.ktx2` |
| `blood-big-burst` | `blood-big-burst.atlas.png` / `blood-big-burst.uastc.ktx2` |
| `thunder-impact` | `thunder-impact.atlas.png` / `thunder-impact.uastc.ktx2` |

Các URL vẫn giữ query mã băm từ manifest cũ. Probe cũng kiểm hai hậu tố `-v2b` cho JSON/PNG/KTX2/grid, từ chối JSON khói `-v2` cũ, cache không tải lặp, `burst=old` không fetch và HTTP 404 giữ nguyên nguồn cũ.

### Giới hạn KTX2 cần owner/coordinator xem

Đã giải mã KTX2 mức 0 bằng `inspect.mjs`, đảo Y về hướng PNG rồi đo cùng điều kiện. Alpha hàng đáy bằng **0 ở đủ 64 khung**, nhưng UASTC mất dữ liệu tạo lại dao động alpha và các đốm nhỏ quanh ngưỡng 12/255:

| Bộ | Khung có alpha tăng ngược | Bước tăng lớn nhất | Thành phần nhỏ, tổng qua 32 khung | Sai số alpha trung bình / tối đa, thang 255 |
| --- | --- | --- | --- | --- |
| Burst trắng | 30/32 | 22/255 | 54, trong 23 khung | 0,2415 / 56 |
| Impact trắng | 30/32 | 23/255 | 46, trong 21 khung | 0,1496 / 35 |

Đã thử UASTC mức 4 trên bản tạm: vẫn có bước tăng tối đa 22/255 và 23/255, còn 53 và 45 thành phần nhỏ. Không thay bản mức 2 bằng thử nghiệm không giải quyết được điều kiện. **Không gộp kết quả PNG PASS thành KTX2 PASS.** Muốn áp dụng điều kiện alpha tuyệt đối cả sau nén cần hướng texture giữ alpha không mất dữ liệu hoặc thay chính sách tải; hai việc đó chưa có trong giải pháp của phiếu, nên không tự đổi codec/runtime. Lab hiện vẫn trỏ tới KTX2 theo yêu cầu.

## Bằng chứng, chạy lại và việc bỏ qua

Bằng chứng ở **`/private/tmp/423-burst-soften/`**, có `ABOUT.md`, hai ảnh `<tên>-before-after.jpg` và prompt ghép ảnh, `repack.py`, `publish.py`, `verify.py`, `probe.mts`, `processing.json`, `validation.json`, `probe.json`, `outputs.json`, `original-sha256.json` và log kiểm kiểu. Không lưu khung thô hoặc RGBA giải mã trung gian; script kiểm tự giải mã vào thư mục tạm rồi xoá.

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game
PYTHONDONTWRITEBYTECODE=1 tools/vfx-flipbook/.venv/bin/python -B /private/tmp/423-burst-soften/verify.py
node --import ./games/.wt-ic-lab-all/node_modules/tsx/dist/loader.mjs /private/tmp/423-burst-soften/probe.mts
```

Thư mục review SSD nằm ngoài quyền ghi của phiên; chưa chuyển ảnh vào đó hoặc cập nhật chỉ mục. Không chạy host/browser/video hay chấm hình tổng hợp, vì phiếu chỉ cho sửa một module lab và đóng gói asset, đồng thời cấm chạy build/test game. Owner/coordinator cần xem **hai ảnh trước/sau và chân khói trong lab**, đặc biệt sai số alpha khi host chọn KTX2. Ba clip quay về bản cũ chờ Firefly làm lại theo quyết định đã có.

Chỉ ghi các đường dẫn phiếu cho phép và thư mục tạm riêng. Không đụng mã game chính, scripts/tests hoặc tài liệu khác; không đổi nhánh, stage media, commit, push, reset, clean hoặc stash. Một luồng, không subagent; quota đọc lúc bắt đầu còn **18%**.
