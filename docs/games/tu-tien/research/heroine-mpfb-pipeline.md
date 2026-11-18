# Nữ chính từ thân người chuẩn MPFB (nghiên cứu và thử 18/11/2026)

Chủ dự án, 18/11/2026, về mặt và tóc Tripo: "phần mặt xấu quá, tóc tai mắt mũi miệng khá kém chất lượng, phải tìm cách xử lý khác". Hướng chọn: thân người chuẩn CC0 của MakeHuman qua MPFB (addon Blender), có nhãn cầu, lông mi, răng và rig chuẩn; nắn theo ảnh 2D của ta; tóc là lưới riêng.

## 1. Giấy phép (kiểm tại nguồn 18/11/2026)

| Phần | Giấy phép | Nguồn |
|---|---|---|
| Mã addon MPFB 2.0.18 | GPLv3 (chỉ chạy trên máy, không vào game) | `LICENSE.md` mục B, https://github.com/makehumancommunity/mpfb2 |
| Base mesh, proxy, target/modifier, texture, quần áo MHCLO, rig, pose, biểu cảm | CC0 1.0 | `LICENSE.md` mục C, `LICENSE.ASSETS.md` |
| File xuất (FBX, OBJ, GLB…), render, model lưu | MakeHuman "không đòi quyền gì" | `LICENSE.md` mục D |
| Gói `makehuman_system_assets` (mắt, lông mi, lông mày, răng, lưỡi, da hệ thống, tóc hệ thống) | CC0 | https://static.makehumancommunity.org/assets/assetpacks.html |
| Gói `hair01`, `skins01`, `eyebrows01`, `eyelashes01` | CC0 | như trên |
| Gói `hair02`, `hair03`, và các gói 02/03 khác (dress, shirts, pants, shoes, suits 03…) | **CC-BY, không dùng** | như trên |

Kết luận: dùng được cho thương mại, không cần ghi công, miễn chỉ lấy tài sản từ gói ghi CC0. Lưu ý: file `.mhclo` của tóc búi `rehmanpolanski_hair_bun_brown` còn dòng mẫu cũ "license AGPL3" của MakeClothes, dù gói `hair01` ghi CC0. Tóc này chỉ là tạm; thay bằng tóc tự làm trước khi phát hành. Ghi sổ: `docs/games/THIRD_PARTY.md`.

## 2. Cài đặt (tách khỏi Blender của chủ dự án)

- Blender 5.2.2, chạy headless `-b -noaudio`, Cycles CPU, view Standard.
- `BLENDER_USER_RESOURCES=<scratchpad>/mpfb/cfg`: MPFB chép vào `cfg/extensions/user_default/mpfb`, dữ liệu người dùng (gói tài sản) ở `cfg/extensions/.user/user_default/mpfb/data`. Không đụng cấu hình Blender chung.
- Tải chỉ từ GitHub release chính thức và `files.makehumancommunity.org`, mỗi gói một thư mục rỗng riêng.
- Script: `scripts/build.py` (tạo người từ file tham số JSON), `scripts/look.py` (vật liệu, đèn, camera, render). Lưu bản sao ở `games/immortality-cultivation/art-src/heroine/models3d/mpfb/scripts/`.

## 3. Bản thử v5

- Macro: nữ (gender 0), Á 100 %, tuổi 0,42, cao 1,0, proportions 0,15 (hông rộng, vai hẹp), cup 0,8, cân nặng 0,5.
- Target: chân dài (đùi +0,8, cẳng +0,6), eo −1,0, hông +0,8, mông +0,7, vai −0,45; mặt trái xoan, cằm hẹp (V-line), gò má cao, đuôi mắt xếch (corner2-up 0,9), môi nhỏ lại.
- Mắt high-poly màu nâu, lông mày `eyebrow010`, lông mi `eyelashes02`, răng, lưỡi, rig `game_engine`.
- Da: da `young_asian_female` (CC0) + mức B của `character-skin-shading.md` (nhám 0,48, SSS Random Walk Skin bán kính 1/0,35/0,2, IOR 1,4, coat 0,08, sheen 0,12), nhân tông hồng; môi tô hồng theo nhóm đỉnh `lips`.
- Leotard đen mờ: tô theo trọng số xương thân (pelvis, spine, clavicle, breast, neck) có viền mềm, không phải lưới riêng.
- Chiếu ảnh mặt 2D (`chan-dung-A`) lên da: ảnh 2D nghiêng 3/4, còn mắt, mày, mi là lưới riêng che mất phần chiếu. Kết quả chỉ làm da nhạt hơn, không mang được nét mặt. **Không giữ**; bản không chiếu là bản chính.

## 4. Còn yếu

- Mặt MakeHuman qua modifier vẫn chung chung, chưa đạt vẻ đẹp của ảnh 2D (mắt chưa đủ phượng, môi và mũi kiểu phương Tây). Cần nắn tay (sculpt) hoặc bộ target riêng theo ảnh mặt.
- Tóc búi tạm là vỏ bóng, không có sợi; cần tóc card tự làm.
- Chiều cao thực đo 1,67 m (macro height không đổi số đo nhóm `body`, cần kiểm); tỉ lệ đầu chưa đo.
- Render và GLB: `typing-game-review/owner-review/2026-11-18/tu-tien/heroine-mpfb/`, `games/immortality-cultivation/art-src/heroine/models3d/mpfb/`.
