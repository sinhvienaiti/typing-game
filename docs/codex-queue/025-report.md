# Phiếu 025 · Map Factory · Sổ model 3D của ba game

Ngày thực hiện: 27/10/2026. Môi trường: macOS, Node v24.22.0. Chỉ đọc GLB và JSON nguồn; không dùng mạng, trình duyệt, dev server, build hoặc test của game. Không ghi vào game, media hay Tu Tiên; không chạy lệnh Git có ghi.

Đã tạo bộ quét Node ESM không phụ thuộc package, test độc lập, README và ba sổ gồm **800 GLB: 500 runtime + 300 original**. Có **0 lỗi đọc**, **0 file cần giải nén**, **800/800 md5 không đổi**; bộ test chạy bằng glob đạt **19/19**.

**Chưa thể đánh dấu đủ 5/5 điều kiện nguyên văn:** lệnh `node --test tools/map-factory/registry/test` không được Node v24.22.0 ở máy này nhận như thư mục test; lệnh glob tương đương đã đạt. `git status --short` có sẵn 7 dòng ngoài phạm vi trước khi bắt đầu; giữ nguyên chúng vì chủ dự án yêu cầu bảo toàn công việc của các làn khác. Không thêm file điểm vào ngoài danh sách cho phép và không dọn Git.

## 1. File đã tạo

- `tools/map-factory/registry/scan-assets.mjs`: đọc GLB, manifest, SOURCES; tính metadata và kiểm md5 trước/sau.
- `tools/map-factory/registry/out/assets.dragon-hold.json`: 78 mục.
- `tools/map-factory/registry/out/assets.typing-defense.json`: 139 mục.
- `tools/map-factory/registry/out/assets.space-typing.json`: 583 mục.
- `tools/map-factory/registry/test/scan-assets.test.mjs`: 19 test, không tạo fixture media trên đĩa.
- `tools/map-factory/registry/README.md`: schema, cách chạy, cách nối nguồn và giới hạn.
- `docs/codex-queue/025-report.md`: báo cáo này.

Không tạo `package.json`: dùng thư viện chuẩn Node để đọc header 12 byte, chunk JSON và BIN; không cần cài offline.

## 2. Số model theo game và category

Mỗi file GLB là một mục; hai tier high/medium là hai mục riêng. `category` giữ đúng thư mục đầu dưới `models/` hoặc `art-src/3d/`; `categoryHint` bổ sung nhóm ngữ nghĩa từ manifest. Số liệu không gộp các file có cùng hình học.

| Game | Runtime | Original | Tổng | Runtime nối được nguồn | Skinned | Có animation |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| dragon-hold | 54 | 24 | 78 | 48 | 6 | 6 |
| typing-defense | 68 | 71 | 139 | 68 | 10 | 10 |
| space-typing | 378 | 205 | 583 | 368 | 13 | 353 |

### dragon-hold

| Category | Runtime | Original | Tổng |
| --- | ---: | ---: | ---: |
| `enemies` | 0 | 6 | 6 |
| `generals` | 0 | 1 | 1 |
| `guides` | 2 | 0 | 2 |
| `heroes` | 4 | 0 | 4 |
| `houses` | 0 | 1 | 1 |
| `m0b` | 48 | 0 | 48 |
| `props` | 0 | 12 | 12 |
| `traps` | 0 | 3 | 3 |
| `units` | 0 | 1 | 1 |

48 runtime trong `m0b` gồm 14 `enemies`, 32 `props`, 2 `units` theo manifest. 6 runtime còn lại gồm 4 `heroes`, 2 `guides`. Đây là phân nhóm bổ sung, không sửa category của đường dẫn.

### typing-defense

| Category | Runtime | Original | Tổng |
| --- | ---: | ---: | ---: |
| `animals` | 0 | 3 | 3 |
| `attachments` | 18 | 0 | 18 |
| `bosses` | 0 | 1 | 1 |
| `buildings` | 14 | 8 | 22 |
| `enemies` | 6 | 15 | 21 |
| `helpers` | 0 | 10 | 10 |
| `heroes` | 2 | 3 | 5 |
| `loot` | 6 | 3 | 9 |
| `projectiles` | 8 | 4 | 12 |
| `props` | 12 | 6 | 18 |
| `units` | 2 | 5 | 7 |
| `workers` | 0 | 13 | 13 |

### space-typing

| Category | Runtime | Original | Tổng |
| --- | ---: | ---: | ---: |
| `bosses` | 54 | 25 | 79 |
| `duel-targets` | 0 | 18 | 18 |
| `enemies` | 244 | 115 | 359 |
| `guides` | 2 | 0 | 2 |
| `heroes` | 6 | 0 | 6 |
| `items` | 22 | 0 | 22 |
| `pickups` | 0 | 8 | 8 |
| `projectiles` | 0 | 12 | 12 |
| `puzzle` | 0 | 3 | 3 |
| `relics` | 0 | 12 | 12 |
| `ships` | 24 | 12 | 36 |
| `skills` | 26 | 0 | 26 |

## 3. Mười model nhiều tam giác nhất mỗi game

Bảng đầu mỗi game xếp chung runtime và original. Có thêm bảng chỉ runtime để hỗ trợ chọn model cho Map Factory. Khi bằng nhau, sắp theo id; số tam giác tính scene 0, đã nhân lượt node dùng mesh. Không lấy trường triangles của manifest thay cho kết quả đọc GLB.

### dragon-hold

| Hạng | Source | Id | Tam giác |
| ---: | --- | --- | ---: |
| 1 | runtime | `heroes/draconis-v3/draconis-v3.high` | 60.000 |
| 2 | runtime | `guides/draconis-v4/draconis-v4.high` | 31.226 |
| 3 | runtime | `guides/draconis-v4/draconis-v4.medium` | 31.226 |
| 4 | runtime | `heroes/draconis-v3/draconis-v3.medium` | 30.000 |
| 5 | runtime | `heroes/draconis-v2/draconis-v2.high` | 22.000 |
| 6 | runtime | `heroes/draconis-v2/draconis-v2.medium` | 22.000 |
| 7 | original | `props/pine-river/tree-violet` | 9.922 |
| 8 | original | `houses/herb-hut` | 9.858 |
| 9 | original | `props/pine-river/pine-round` | 9.499 |
| 10 | original | `props/pine-river/pine-tall` | 9.496 |

Chỉ runtime:

| Hạng | Id | Tam giác |
| ---: | --- | ---: |
| 1 | `heroes/draconis-v3/draconis-v3.high` | 60.000 |
| 2 | `guides/draconis-v4/draconis-v4.high` | 31.226 |
| 3 | `guides/draconis-v4/draconis-v4.medium` | 31.226 |
| 4 | `heroes/draconis-v3/draconis-v3.medium` | 30.000 |
| 5 | `heroes/draconis-v2/draconis-v2.high` | 22.000 |
| 6 | `heroes/draconis-v2/draconis-v2.medium` | 22.000 |
| 7 | `m0b/props/herb-hut/herb-hut.high` | 4.400 |
| 8 | `m0b/props/herb-hut/herb-hut.medium` | 4.400 |
| 9 | `m0b/enemies/moss-banner/moss-banner.high` | 4.325 |
| 10 | `m0b/enemies/moss-banner/moss-banner.medium` | 4.325 |

### typing-defense

| Hạng | Source | Id | Tam giác |
| ---: | --- | --- | ---: |
| 1 | original | `bosses/moc-tinh` | 29.177 |
| 2 | original | `buildings/barracks` | 27.847 |
| 3 | original | `heroes/lam` | 22.906 |
| 4 | runtime | `heroes/lam/lam.high` | 20.000 |
| 5 | runtime | `heroes/lam/lam.medium` | 20.000 |
| 6 | original | `buildings/keep` | 18.962 |
| 7 | runtime | `buildings/keep/keep.high` | 15.000 |
| 8 | runtime | `buildings/keep/keep.medium` | 15.000 |
| 9 | original | `enemies/troll` | 11.720 |
| 10 | original | `buildings/seal-dais` | 11.422 |

Chỉ runtime:

| Hạng | Id | Tam giác |
| ---: | --- | ---: |
| 1 | `heroes/lam/lam.high` | 20.000 |
| 2 | `heroes/lam/lam.medium` | 20.000 |
| 3 | `buildings/keep/keep.high` | 15.000 |
| 4 | `buildings/keep/keep.medium` | 15.000 |
| 5 | `buildings/archer/archer.high` | 10.000 |
| 6 | `buildings/archer/archer.medium` | 10.000 |
| 7 | `buildings/cannon/cannon.high` | 10.000 |
| 8 | `buildings/cannon/cannon.medium` | 10.000 |
| 9 | `buildings/seal-dais/seal-dais.high` | 10.000 |
| 10 | `buildings/seal-dais/seal-dais.medium` | 10.000 |

### space-typing

| Hạng | Source | Id | Tam giác |
| ---: | --- | --- | ---: |
| 1 | runtime | `heroes/draconis-v3/draconis-v3.high` | 60.000 |
| 2 | original | `bosses/tyrant-g07` | 31.865 |
| 3 | original | `bosses/warden-devil` | 31.833 |
| 4 | original | `bosses/tyrant-g05` | 31.772 |
| 5 | original | `bosses/lieutenant-devil` | 31.766 |
| 6 | original | `bosses/lieutenant-shadow` | 31.733 |
| 7 | original | `bosses/lieutenant-frost` | 31.729 |
| 8 | original | `enemies/magma-scout` | 31.703 |
| 9 | original | `enemies/nature-boss` | 31.689 |
| 10 | original | `bosses/warden-shadow` | 31.687 |

Chỉ runtime:

| Hạng | Id | Tam giác |
| ---: | --- | ---: |
| 1 | `heroes/draconis-v3/draconis-v3.high` | 60.000 |
| 2 | `guides/draconis-v4/draconis-v4.high` | 31.226 |
| 3 | `guides/draconis-v4/draconis-v4.medium` | 31.226 |
| 4 | `bosses/auriel-hero/auriel-hero.high` | 30.150 |
| 5 | `bosses/auriel-hero/auriel-hero.medium` | 30.150 |
| 6 | `bosses/tyrant-g01/tyrant-g01.high` | 30.150 |
| 7 | `bosses/tyrant-g01/tyrant-g01.medium` | 30.150 |
| 8 | `bosses/lieutenant-angel/lieutenant-angel.high` | 30.000 |
| 9 | `bosses/lieutenant-angel/lieutenant-angel.medium` | 30.000 |
| 10 | `bosses/lieutenant-devil/lieutenant-devil.high` | 30.000 |

Một số tier high và medium có cùng số tam giác; đây là số thực trong accessor của các GLB hiện có, không phải bộ quét chép nhầm trường manifest.

## 4. Cỡ và trục cần xem

**Không có** GLB cao hơn 30 m hoặc thấp hơn 0,05 m. Chiều cao là `sizeY` sau transform; đơn vị mét theo quy ước glTF, không tự gán cỡ thực ngoài đời cho bản gốc.

| Game | Chiều cao nhỏ nhất (m) | Chiều cao lớn nhất (m) | Cờ trục runtime | Cờ trục original |
| --- | ---: | ---: | ---: | ---: |
| dragon-hold | 0.244080 | 2.395568 | 14 | 5 |
| typing-defense | 0.094376 | 8.013843 | 0 | 29 |
| space-typing | 0.130371 | 2.033938 | 150 | 69 |

Có **267 mục** sinh vật có cạnh dài nhất X/Z: 19 Dragon Hold, 29 Typing Defense, 219 Space. Đây là cờ thô; sinh vật dài ngang hoặc model Space nằm theo hướng bay có thể đúng thiết kế. Không xoay, chuẩn cỡ hay sửa media. Chỉ xét các nhóm enemies, bosses, heroes, guides, units, generals, animals, workers, helpers; tàu trong category ships không bị coi là sinh vật.

Hộp là hợp tám góc AABB accessor qua ma trận thế giới của node, đã đổi POSITION số nguyên chuẩn hóa. Không chạy skin, morph hoặc animation. Vì vậy đây là số đo tĩnh phục vụ lập sổ, chưa phải đánh giá hướng mặt hoặc hộp va chạm khi chơi.

Danh sách đầy đủ dưới đây: `id` runtime ghép sau `games/<game>/public/assets/<game>/models/`, `id` original ghép sau `games/<game>/art-src/3d/`, rồi thêm `.glb`.

### dragon-hold · cạnh dài nhất khác Y

| Source | Id | Size X × Y × Z (m) | Trục dài nhất |
| --- | --- | --- | --- |
| original | `enemies/blight-wolf` | 1.000000 × 0.593994 × 0.375519 | X |
| original | `enemies/thorn-ant` | 1.000000 × 0.511414 × 0.706116 | X |
| original | `enemies/thorn-wasp` | 0.708374 × 0.603638 × 1.000000 | Z |
| original | `enemies/tusk-boar` | 1.000000 × 0.625793 × 0.459778 | X |
| original | `units/moss-warden` | 0.520508 × 0.997986 × 1.000000 | Z |
| runtime | `guides/draconis-v4/draconis-v4.high` | 2.000000 × 1.983642 × 1.166173 | X |
| runtime | `guides/draconis-v4/draconis-v4.medium` | 2.000000 × 1.983642 × 1.166173 | X |
| runtime | `heroes/draconis-v2/draconis-v2.high` | 2.000000 × 1.815668 × 1.416913 | X |
| runtime | `heroes/draconis-v2/draconis-v2.medium` | 2.000000 × 1.815668 × 1.416913 | X |
| runtime | `heroes/draconis-v3/draconis-v3.high` | 2.000000 × 0.973235 × 1.349040 | X |
| runtime | `heroes/draconis-v3/draconis-v3.medium` | 2.000000 × 0.973479 × 1.349528 | X |
| runtime | `m0b/enemies/blight-wolf/blight-wolf.high` | 0.425436 × 0.699994 × 1.180478 | Z |
| runtime | `m0b/enemies/blight-wolf/blight-wolf.medium` | 0.425436 × 0.699994 × 1.180478 | Z |
| runtime | `m0b/enemies/thorn-ant/thorn-ant.high` | 0.485527 × 0.362453 × 0.706513 | Z |
| runtime | `m0b/enemies/thorn-ant/thorn-ant.medium` | 0.485527 × 0.362453 × 0.706513 | Z |
| runtime | `m0b/enemies/thorn-wasp/thorn-wasp.high` | 0.925274 × 0.559056 × 0.656194 | X |
| runtime | `m0b/enemies/thorn-wasp/thorn-wasp.medium` | 0.925274 × 0.559056 × 0.656194 | X |
| runtime | `m0b/enemies/tusk-boar/tusk-boar.high` | 0.651747 × 0.900705 × 1.425905 | Z |
| runtime | `m0b/enemies/tusk-boar/tusk-boar.medium` | 0.651747 × 0.900705 × 1.425905 | Z |

### typing-defense · cạnh dài nhất khác Y

| Source | Id | Size X × Y × Z (m) | Trục dài nhất |
| --- | --- | --- | --- |
| original | `animals/chuon-chuon-tre` | 0.497284 × 0.140640 × 1.000000 | Z |
| original | `animals/piggy` | 0.536682 × 0.649170 × 1.000000 | Z |
| original | `animals/trau` | 0.442383 × 0.569702 × 1.000000 | Z |
| original | `enemies/alicanto` | 1.000000 × 0.719727 × 0.958618 | X |
| original | `enemies/cuong-thi-lead-hat` | 0.570923 × 0.505859 × 1.000000 | Z |
| original | `enemies/dokkaebi-club` | 0.605469 × 0.348572 × 1.000000 | Z |
| original | `enemies/kamaitachi` | 0.314941 × 0.585632 × 1.000000 | Z |
| original | `enemies/nuppeppo` | 0.693115 × 0.961121 × 1.000000 | Z |
| original | `enemies/oni-club` | 0.354034 × 0.348455 × 1.000000 | Z |
| original | `enemies/thuong-luong` | 1.000000 × 0.456451 × 0.291473 | X |
| original | `helpers/helper-book` | 0.804077 × 0.361450 × 1.000000 | Z |
| original | `helpers/helper-brush` | 0.189957 × 0.180939 × 1.000000 | Z |
| original | `helpers/helper-cham-glasses` | 0.843872 × 0.432831 × 1.000000 | Z |
| original | `helpers/helper-cham-scarf` | 1.000000 × 0.438812 × 0.874084 | X |
| original | `helpers/helper-drum` | 0.634094 × 0.327606 × 1.000000 | Z |
| original | `helpers/helper-fan` | 1.000000 × 0.211624 × 0.718018 | X |
| original | `helpers/helper-hammer` | 0.460175 × 0.450012 × 1.000000 | Z |
| original | `helpers/helper-owlet` | 0.555969 × 0.999268 × 1.000000 | Z |
| original | `heroes/tre-mallet` | 0.298676 × 0.387543 × 1.000000 | Z |
| original | `units/linh-giao-spear` | 0.105011 × 0.094376 × 1.000000 | Z |
| original | `workers/worker-kit-dong-head` | 0.955872 × 0.991333 × 1.000000 | Z |
| original | `workers/worker-kit-dong-rammer` | 0.248795 × 0.233551 × 1.000000 | Z |
| original | `workers/worker-kit-en-head` | 0.610168 × 0.593384 × 1.000000 | Z |
| original | `workers/worker-kit-gatekeeper-crossbow` | 0.955139 × 0.223328 × 1.000000 | Z |
| original | `workers/worker-kit-lua-head` | 0.822449 × 0.754761 × 1.000000 | Z |
| original | `workers/worker-kit-miner-head` | 1.000000 × 0.745239 × 0.960815 | X |
| original | `workers/worker-kit-miner-pickaxe` | 0.225525 × 0.757751 × 1.000000 | Z |
| original | `workers/worker-kit-sam-head` | 0.809692 × 0.598938 × 1.000000 | Z |
| original | `workers/worker-kit-se-head` | 0.858765 × 0.774170 × 1.000000 | Z |

### space-typing · cạnh dài nhất khác Y

| Source | Id | Size X × Y × Z (m) | Trục dài nhất |
| --- | --- | --- | --- |
| original | `bosses/lieutenant-devil` | 0.937988 × 0.830078 × 0.741211 | X |
| original | `bosses/tyrant-g01` | 1.748548 × 1.700001 × 0.665256 | X |
| original | `bosses/tyrant-g09` | 0.948730 × 0.923340 × 0.541016 | X |
| original | `bosses/warden-angel` | 0.948242 × 0.920899 × 0.258789 | X |
| original | `enemies/angel-carrier` | 0.944336 × 0.376953 × 0.877442 | X |
| original | `enemies/angel-cloaker` | 0.946778 × 0.881348 × 0.179688 | X |
| original | `enemies/angel-commander` | 0.937500 × 0.917481 × 0.407227 | X |
| original | `enemies/angel-leech` | 0.949708 × 0.942383 × 0.556641 | X |
| original | `enemies/angel-mine` | 0.954102 × 0.943848 × 0.725098 | X |
| original | `enemies/angel-scout` | 0.952637 × 0.736328 × 0.664062 | X |
| original | `enemies/angel-tank` | 0.883789 × 0.673340 × 0.951661 | Z |
| original | `enemies/cosmic-beast` | 0.955078 × 0.943360 × 0.384766 | X |
| original | `enemies/cosmic-carrier` | 0.949708 × 0.414063 × 0.691894 | X |
| original | `enemies/cosmic-cloaker` | 0.785156 × 0.159668 × 0.953614 | Z |
| original | `enemies/cosmic-dreadnought` | 0.953614 × 0.383789 × 0.671386 | X |
| original | `enemies/cosmic-fast` | 0.676270 × 0.235840 × 0.948242 | Z |
| original | `enemies/cosmic-jammer` | 0.949219 × 0.145507 × 0.722656 | X |
| original | `enemies/cosmic-leecher` | 0.950196 × 0.943848 × 0.465820 | X |
| original | `enemies/cosmic-shield` | 0.896972 × 0.620117 × 0.953125 | Z |
| original | `enemies/cosmic-tank` | 0.842286 × 0.704589 × 0.953613 | Z |
| original | `enemies/devil-carrier` | 0.957520 × 0.298340 × 0.803222 | X |
| original | `enemies/devil-cloaker` | 0.952149 × 0.865234 × 0.227051 | X |
| original | `enemies/devil-commander` | 0.953614 × 0.867675 × 0.512696 | X |
| original | `enemies/devil-jammer` | 0.956543 × 0.809082 × 0.657227 | X |
| original | `enemies/devil-mine` | 0.947754 × 0.925781 × 0.740235 | X |
| original | `enemies/devil-scout` | 0.957520 × 0.627930 × 0.765625 | X |
| original | `enemies/devil-sniper` | 0.958008 × 0.224121 × 0.712891 | X |
| original | `enemies/devil-tank` | 0.804200 × 0.428223 × 0.953125 | Z |
| original | `enemies/frost-cloaker` | 0.948730 × 0.928222 × 0.209472 | X |
| original | `enemies/frost-mine` | 0.952637 × 0.949219 × 0.366700 | X |
| original | `enemies/frost-scout` | 0.947754 × 0.924316 × 0.121582 | X |
| original | `enemies/frost-sniper` | 0.451172 × 0.223145 × 0.953125 | Z |
| original | `enemies/magma-carrier` | 0.957520 × 0.863282 × 0.552734 | X |
| original | `enemies/magma-cloaker` | 0.955078 × 0.690430 × 0.621094 | X |
| original | `enemies/magma-destroyer` | 0.784668 × 0.508300 × 0.951172 | Z |
| original | `enemies/magma-mine` | 0.949219 × 0.919434 × 0.828613 | X |
| original | `enemies/magma-scout` | 0.927734 × 0.406738 × 0.954102 | Z |
| original | `enemies/nature-boss` | 0.954101 × 0.790527 × 0.518555 | X |
| original | `enemies/nature-carrier` | 0.957520 × 0.416016 × 0.445801 | X |
| original | `enemies/nature-cloaker` | 0.958496 × 0.169922 × 0.614746 | X |
| original | `enemies/nature-leecher` | 0.950196 × 0.908692 × 0.466797 | X |
| original | `enemies/nature-mine` | 0.949707 × 0.881836 × 0.597168 | X |
| original | `enemies/nature-scout` | 0.847168 × 0.189454 × 0.955078 | Z |
| original | `enemies/nature-shield` | 0.957520 × 0.856445 × 0.624024 | X |
| original | `enemies/nature-splitter` | 0.955567 × 0.878906 × 0.236816 | X |
| original | `enemies/nature-tank` | 0.859863 × 0.238282 × 0.953613 | Z |
| original | `enemies/prism-carrier` | 0.950684 × 0.669434 × 0.636718 | X |
| original | `enemies/prism-cloaker` | 0.953125 × 0.895508 × 0.522461 | X |
| original | `enemies/prism-healer` | 0.949708 × 0.943359 × 0.450196 | X |
| original | `enemies/prism-leech` | 0.598144 × 0.363770 × 0.954102 | Z |
| original | `enemies/prism-mine` | 0.949708 × 0.947266 × 0.947754 | X |
| original | `enemies/prism-scout` | 0.953125 × 0.901367 × 0.166992 | X |
| original | `enemies/prism-tank` | 0.956542 × 0.826172 × 0.750977 | X |
| original | `enemies/rainbow-carrier` | 0.949708 × 0.691406 × 0.813964 | X |
| original | `enemies/rainbow-commander` | 0.945800 × 0.796386 × 0.481934 | X |
| original | `enemies/rainbow-jammer` | 0.949708 × 0.796875 × 0.704589 | X |
| original | `enemies/rainbow-leech` | 0.949708 × 0.882324 × 0.645507 | X |
| original | `enemies/rainbow-sniper` | 0.541504 × 0.475586 × 0.949707 | Z |
| original | `enemies/rainbow-splitter` | 0.948730 × 0.859863 × 0.575195 | X |
| original | `enemies/rainbow-tank` | 0.660278 × 0.933044 × 1.000000 | Z |
| original | `enemies/shadow-carrier` | 0.998108 × 0.845032 × 1.000000 | Z |
| original | `enemies/shadow-cloaker` | 0.540405 × 0.841248 × 1.000000 | Z |
| original | `enemies/shadow-commander` | 0.586609 × 0.953064 × 1.000000 | Z |
| original | `enemies/shadow-healer` | 0.605896 × 0.972107 × 1.000000 | Z |
| original | `enemies/shadow-jammer` | 0.496887 × 0.997620 × 1.000000 | Z |
| original | `enemies/shadow-scout` | 1.000000 × 0.970825 × 0.979248 | X |
| original | `enemies/shadow-shield` | 0.586914 × 0.964844 × 1.000000 | Z |
| original | `enemies/shadow-splitter` | 0.240540 × 0.966370 × 1.000000 | Z |
| original | `enemies/shadow-tank` | 0.437927 × 0.968445 × 1.000000 | Z |
| runtime | `bosses/auriel-hero/auriel-hero.high` | 2.000000 × 1.944578 × 0.760826 | X |
| runtime | `bosses/auriel-hero/auriel-hero.medium` | 2.000000 × 1.944578 × 0.760826 | X |
| runtime | `bosses/lieutenant-devil/lieutenant-devil.high` | 2.000000 × 1.770013 × 1.580554 | X |
| runtime | `bosses/lieutenant-devil/lieutenant-devil.medium` | 2.000000 × 1.770013 × 1.580554 | X |
| runtime | `bosses/tyrant-g01/tyrant-g01.high` | 2.000000 × 1.944578 × 0.760826 | X |
| runtime | `bosses/tyrant-g01/tyrant-g01.medium` | 2.000000 × 1.944578 × 0.760826 | X |
| runtime | `bosses/tyrant-g09/tyrant-g09.high` | 2.000000 × 1.946776 × 1.140538 | X |
| runtime | `bosses/tyrant-g09/tyrant-g09.medium` | 2.000000 × 1.946776 × 1.140538 | X |
| runtime | `bosses/warden-angel/warden-angel.high` | 2.000000 × 1.942381 × 0.545732 | X |
| runtime | `bosses/warden-angel/warden-angel.medium` | 2.000000 × 1.942381 × 0.545732 | X |
| runtime | `enemies/angel-cloaker-3d/angel-cloaker-3d.high` | 2.004876 × 1.859253 × 0.386205 | X |
| runtime | `enemies/angel-cloaker-3d/angel-cloaker-3d.medium` | 2.004876 × 1.859253 × 0.386205 | X |
| runtime | `enemies/angel-commander-3d/angel-commander-3d.high` | 2.000000 × 1.959960 × 0.873379 | X |
| runtime | `enemies/angel-commander-3d/angel-commander-3d.medium` | 2.000000 × 1.959960 × 0.873379 | X |
| runtime | `enemies/angel-leech-3d/angel-leech-3d.high` | 2.008556 × 1.967118 × 1.160619 | X |
| runtime | `enemies/angel-leech-3d/angel-leech-3d.medium` | 2.008556 × 1.967118 × 1.160619 | X |
| runtime | `enemies/angel-mine-3d/angel-mine-3d.high` | 2.004612 × 1.979162 × 1.521308 | X |
| runtime | `enemies/angel-mine-3d/angel-mine-3d.medium` | 2.004612 × 1.979162 × 1.521308 | X |
| runtime | `enemies/angel-scout-3d/angel-scout-3d.high` | 1.991575 × 1.552987 × 1.399275 | X |
| runtime | `enemies/angel-scout-3d/angel-scout-3d.medium` | 1.991575 × 1.552987 × 1.399275 | X |
| runtime | `enemies/angel-scout-lod/angel-scout-lod.high` | 1.992436 × 1.535417 × 1.398907 | X |
| runtime | `enemies/angel-scout-lod/angel-scout-lod.medium` | 1.992436 × 1.535417 × 1.398907 | X |
| runtime | `enemies/angel-tank-3d/angel-tank-3d.high` | 1.857057 × 1.422269 × 1.988373 | Z |
| runtime | `enemies/angel-tank-3d/angel-tank-3d.medium` | 1.857057 × 1.422269 × 1.988373 | Z |
| runtime | `enemies/angel-tank-lod/angel-tank-lod.high` | 1.748835 × 1.437181 × 1.957440 | Z |
| runtime | `enemies/angel-tank-lod/angel-tank-lod.medium` | 1.748835 × 1.437181 × 1.957440 | Z |
| runtime | `enemies/cosmic-carrier-3d/cosmic-carrier-3d.high` | 2.003827 × 1.454115 × 0.877007 | X |
| runtime | `enemies/cosmic-carrier-3d/cosmic-carrier-3d.medium` | 2.003827 × 1.454115 × 0.877007 | X |
| runtime | `enemies/cosmic-cloaker-3d/cosmic-cloaker-3d.high` | 2.002953 × 1.646704 × 0.337911 | X |
| runtime | `enemies/cosmic-cloaker-3d/cosmic-cloaker-3d.medium` | 2.002953 × 1.646704 × 0.337911 | X |
| runtime | `enemies/cosmic-healer-3d/cosmic-healer-3d.high` | 1.650089 × 1.594147 × 2.001127 | Z |
| runtime | `enemies/cosmic-healer-3d/cosmic-healer-3d.medium` | 1.650089 × 1.594147 × 2.001127 | Z |
| runtime | `enemies/cosmic-jammer-3d/cosmic-jammer-3d.high` | 2.004572 × 1.522990 × 0.311266 | X |
| runtime | `enemies/cosmic-jammer-3d/cosmic-jammer-3d.medium` | 2.004572 × 1.522990 × 0.311266 | X |
| runtime | `enemies/cosmic-leech-3d/cosmic-leech-3d.high` | 2.011309 × 1.984547 × 0.987578 | X |
| runtime | `enemies/cosmic-leech-3d/cosmic-leech-3d.medium` | 2.011309 × 1.984547 × 0.987578 | X |
| runtime | `enemies/cosmic-sniper-3d/cosmic-sniper-3d.high` | 1.706848 × 1.578695 × 2.007260 | Z |
| runtime | `enemies/cosmic-sniper-3d/cosmic-sniper-3d.medium` | 1.706848 × 1.578695 × 2.007260 | Z |
| runtime | `enemies/cosmic-splitter-3d/cosmic-splitter-3d.high` | 1.998369 × 1.981048 × 0.809728 | X |
| runtime | `enemies/cosmic-splitter-3d/cosmic-splitter-3d.medium` | 1.998369 × 1.981048 × 0.809728 | X |
| runtime | `enemies/devil-cloaker-3d/devil-cloaker-3d.high` | 1.997654 × 1.812563 × 0.477969 | X |
| runtime | `enemies/devil-cloaker-3d/devil-cloaker-3d.medium` | 1.997654 × 1.812563 × 0.477969 | X |
| runtime | `enemies/devil-commander-3d/devil-commander-3d.high` | 2.003276 × 1.824756 × 1.075155 | X |
| runtime | `enemies/devil-commander-3d/devil-commander-3d.medium` | 2.003276 × 1.824756 × 1.075155 | X |
| runtime | `enemies/devil-destroyer-3d/devil-destroyer-3d.high` | 1.997654 × 1.812563 × 0.477969 | X |
| runtime | `enemies/devil-destroyer-3d/devil-destroyer-3d.medium` | 1.997654 × 1.812563 × 0.477969 | X |
| runtime | `enemies/devil-jammer-3d/devil-jammer-3d.high` | 1.999113 × 1.684546 × 1.380899 | X |
| runtime | `enemies/devil-jammer-3d/devil-jammer-3d.medium` | 1.999113 × 1.684546 × 1.380899 | X |
| runtime | `enemies/devil-mine-3d/devil-mine-3d.high` | 2.007532 × 1.950431 × 1.562244 | X |
| runtime | `enemies/devil-mine-3d/devil-mine-3d.medium` | 2.007532 × 1.950431 × 1.562244 | X |
| runtime | `enemies/devil-scout-3d/devil-scout-3d.high` | 2.014110 × 1.317989 × 1.600064 | X |
| runtime | `enemies/devil-scout-3d/devil-scout-3d.medium` | 2.014110 × 1.317989 × 1.600064 | X |
| runtime | `enemies/devil-scout-lod/devil-scout-lod.high` | 1.977823 × 1.308005 × 1.591759 | X |
| runtime | `enemies/devil-scout-lod/devil-scout-lod.medium` | 1.977823 × 1.308005 × 1.591759 | X |
| runtime | `enemies/devil-shield-3d/devil-shield-3d.high` | 1.952165 × 2.000930 × 2.244206 | Z |
| runtime | `enemies/devil-shield-3d/devil-shield-3d.medium` | 1.952165 × 2.000930 × 2.244206 | Z |
| runtime | `enemies/frost-cloaker-3d/frost-cloaker-3d.high` | 2.002639 × 1.956434 × 0.452514 | X |
| runtime | `enemies/frost-cloaker-3d/frost-cloaker-3d.medium` | 2.002639 × 1.956434 × 0.452514 | X |
| runtime | `enemies/frost-mine-3d/frost-mine-3d.high` | 1.994905 × 1.992713 × 0.773013 | X |
| runtime | `enemies/frost-mine-3d/frost-mine-3d.medium` | 1.994905 × 1.992713 × 0.773013 | X |
| runtime | `enemies/frost-scout-3d/frost-scout-3d.high` | 2.002446 × 1.950623 × 0.258625 | X |
| runtime | `enemies/frost-scout-3d/frost-scout-3d.medium` | 2.002446 × 1.950623 × 0.258625 | X |
| runtime | `enemies/frost-scout-lod/frost-scout-lod.high` | 1.996399 × 1.943758 × 0.256625 | X |
| runtime | `enemies/frost-scout-lod/frost-scout-lod.medium` | 1.996399 × 1.943758 × 0.256625 | X |
| runtime | `enemies/frost-sniper-3d/frost-sniper-3d.high` | 0.468371 × 0.943125 × 1.992095 | Z |
| runtime | `enemies/frost-sniper-3d/frost-sniper-3d.medium` | 0.468371 × 0.943125 × 1.992095 | Z |
| runtime | `enemies/nature-carrier-3d/nature-carrier-3d.high` | 1.994504 × 0.860022 × 0.933309 | X |
| runtime | `enemies/nature-carrier-3d/nature-carrier-3d.medium` | 1.994504 × 0.860022 × 0.933309 | X |
| runtime | `enemies/nature-cloaker-3d/nature-cloaker-3d.high` | 2.001568 × 1.281927 × 0.355270 | X |
| runtime | `enemies/nature-cloaker-3d/nature-cloaker-3d.medium` | 2.001568 × 1.281927 × 0.355270 | X |
| runtime | `enemies/nature-commander-3d/nature-commander-3d.high` | 2.002858 × 1.653961 × 1.087889 | X |
| runtime | `enemies/nature-commander-3d/nature-commander-3d.medium` | 2.002858 × 1.653961 × 1.087889 | X |
| runtime | `enemies/nature-destroyer-3d/nature-destroyer-3d.high` | 1.888460 × 1.413181 × 2.023319 | Z |
| runtime | `enemies/nature-destroyer-3d/nature-destroyer-3d.medium` | 1.888460 × 1.413181 × 2.023319 | Z |
| runtime | `enemies/nature-leech-3d/nature-leech-3d.high` | 2.000354 × 1.908538 × 0.991966 | X |
| runtime | `enemies/nature-leech-3d/nature-leech-3d.medium` | 2.000354 × 1.908538 × 0.991966 | X |
| runtime | `enemies/nature-mine-3d/nature-mine-3d.high` | 1.984745 × 1.855122 × 1.273818 | X |
| runtime | `enemies/nature-mine-3d/nature-mine-3d.medium` | 1.984745 × 1.855122 × 1.273818 | X |
| runtime | `enemies/nature-shield-3d/nature-shield-3d.high` | 2.005075 × 1.799471 × 1.304000 | X |
| runtime | `enemies/nature-shield-3d/nature-shield-3d.medium` | 2.005075 × 1.799471 × 1.304000 | X |
| runtime | `enemies/nature-splitter-3d/nature-splitter-3d.high` | 1.998237 × 1.833826 × 0.510856 | X |
| runtime | `enemies/nature-splitter-3d/nature-splitter-3d.medium` | 1.998237 × 1.833826 × 0.510856 | X |
| runtime | `enemies/prism-carrier-3d/prism-carrier-3d.high` | 2.003672 × 1.405817 × 1.337575 | X |
| runtime | `enemies/prism-carrier-3d/prism-carrier-3d.medium` | 2.003672 × 1.405817 × 1.337575 | X |
| runtime | `enemies/prism-cloaker-3d/prism-cloaker-3d.high` | 2.003773 × 1.872663 × 1.101350 | X |
| runtime | `enemies/prism-cloaker-3d/prism-cloaker-3d.medium` | 2.003773 × 1.872663 × 1.101350 | X |
| runtime | `enemies/prism-healer-3d/prism-healer-3d.high` | 2.002377 × 1.994066 × 0.947993 | X |
| runtime | `enemies/prism-healer-3d/prism-healer-3d.medium` | 2.002377 × 1.994066 × 0.947993 | X |
| runtime | `enemies/prism-leech-3d/prism-leech-3d.high` | 1.272730 × 0.767930 × 2.003245 | Z |
| runtime | `enemies/prism-leech-3d/prism-leech-3d.medium` | 1.272730 × 0.767930 × 2.003245 | Z |
| runtime | `enemies/prism-mine-3d/prism-mine-3d.high` | 2.000972 × 1.994866 × 2.000240 | X |
| runtime | `enemies/prism-mine-3d/prism-mine-3d.medium` | 2.000972 × 1.994866 × 2.000240 | X |
| runtime | `enemies/prism-scout-3d/prism-scout-3d.high` | 1.996984 × 1.892890 × 0.355919 | X |
| runtime | `enemies/prism-scout-3d/prism-scout-3d.medium` | 1.996984 × 1.892890 × 0.355919 | X |
| runtime | `enemies/prism-scout-lod/prism-scout-lod.high` | 1.999198 × 1.891572 × 0.357533 | X |
| runtime | `enemies/prism-scout-lod/prism-scout-lod.medium` | 1.999198 × 1.891572 × 0.357533 | X |
| runtime | `enemies/prism-splitter-3d/prism-splitter-3d.high` | 2.002377 × 1.994066 × 0.947993 | X |
| runtime | `enemies/prism-splitter-3d/prism-splitter-3d.medium` | 2.002377 × 1.994066 × 0.947993 | X |
| runtime | `enemies/prism-tank-3d/prism-tank-3d.high` | 2.000000 × 1.728263 × 1.571276 | X |
| runtime | `enemies/prism-tank-3d/prism-tank-3d.medium` | 2.000000 × 1.728263 × 1.571276 | X |
| runtime | `enemies/rainbow-carrier-3d/rainbow-carrier-3d.high` | 1.989580 × 1.456649 × 1.717316 | X |
| runtime | `enemies/rainbow-carrier-3d/rainbow-carrier-3d.medium` | 1.989580 × 1.456649 × 1.717316 | X |
| runtime | `enemies/rainbow-cloaker-3d/rainbow-cloaker-3d.high` | 1.998791 × 1.683786 × 1.031024 | X |
| runtime | `enemies/rainbow-cloaker-3d/rainbow-cloaker-3d.medium` | 1.998791 × 1.683786 × 1.031024 | X |
| runtime | `enemies/rainbow-commander-3d/rainbow-commander-3d.high` | 1.998791 × 1.683786 × 1.031024 | X |
| runtime | `enemies/rainbow-commander-3d/rainbow-commander-3d.medium` | 1.998791 × 1.683786 × 1.031024 | X |
| runtime | `enemies/rainbow-jammer-3d/rainbow-jammer-3d.high` | 2.003594 × 1.673891 × 1.487699 | X |
| runtime | `enemies/rainbow-jammer-3d/rainbow-jammer-3d.medium` | 2.003594 × 1.673891 × 1.487699 | X |
| runtime | `enemies/rainbow-leech-3d/rainbow-leech-3d.high` | 2.006388 × 1.856982 × 1.364861 | X |
| runtime | `enemies/rainbow-leech-3d/rainbow-leech-3d.medium` | 2.006388 × 1.856982 × 1.364861 | X |
| runtime | `enemies/rainbow-scout-3d/rainbow-scout-3d.high` | 2.000000 × 1.866207 × 1.320475 | X |
| runtime | `enemies/rainbow-scout-3d/rainbow-scout-3d.medium` | 2.000000 × 1.866207 × 1.320475 | X |
| runtime | `enemies/rainbow-scout-lod/rainbow-scout-lod.high` | 1.945556 × 1.769805 × 1.324667 | X |
| runtime | `enemies/rainbow-scout-lod/rainbow-scout-lod.medium` | 1.945556 × 1.769805 × 1.324667 | X |
| runtime | `enemies/rainbow-sniper-3d/rainbow-sniper-3d.high` | 1.002529 × 1.139520 × 2.000357 | Z |
| runtime | `enemies/rainbow-sniper-3d/rainbow-sniper-3d.medium` | 1.002529 × 1.139520 × 2.000357 | Z |
| runtime | `enemies/rainbow-splitter-3d/rainbow-splitter-3d.high` | 2.001341 × 1.813220 × 1.219726 | X |
| runtime | `enemies/rainbow-splitter-3d/rainbow-splitter-3d.medium` | 2.001341 × 1.813220 × 1.219726 | X |
| runtime | `enemies/rainbow-tank-3d/rainbow-tank-3d.high` | 2.000000 × 1.866207 × 1.320475 | X |
| runtime | `enemies/rainbow-tank-3d/rainbow-tank-3d.medium` | 2.000000 × 1.866207 × 1.320475 | X |
| runtime | `enemies/shadow-carrier-3d/shadow-carrier-3d.high` | 1.997272 × 1.661293 × 1.998736 | Z |
| runtime | `enemies/shadow-carrier-3d/shadow-carrier-3d.medium` | 1.997272 × 1.661293 × 1.998736 | Z |
| runtime | `enemies/shadow-cloaker-3d/shadow-cloaker-3d.high` | 2.005249 × 1.654711 × 1.082579 | X |
| runtime | `enemies/shadow-cloaker-3d/shadow-cloaker-3d.medium` | 2.005249 × 1.654711 × 1.082579 | X |
| runtime | `enemies/shadow-commander-3d/shadow-commander-3d.high` | 1.999945 × 1.907904 × 1.155399 | X |
| runtime | `enemies/shadow-commander-3d/shadow-commander-3d.medium` | 1.999945 × 1.907904 × 1.155399 | X |
| runtime | `enemies/shadow-destroyer-3d/shadow-destroyer-3d.high` | 2.005249 × 1.654711 × 1.082579 | X |
| runtime | `enemies/shadow-destroyer-3d/shadow-destroyer-3d.medium` | 2.005249 × 1.654711 × 1.082579 | X |
| runtime | `enemies/shadow-healer-3d/shadow-healer-3d.high` | 1.988520 × 1.943369 × 1.200989 | X |
| runtime | `enemies/shadow-healer-3d/shadow-healer-3d.medium` | 1.988520 × 1.943369 × 1.200989 | X |
| runtime | `enemies/shadow-leech-3d/shadow-leech-3d.high` | 2.012380 × 2.000097 × 1.814379 | X |
| runtime | `enemies/shadow-leech-3d/shadow-leech-3d.medium` | 2.012380 × 2.000097 × 1.814379 | X |
| runtime | `enemies/shadow-scout-3d/shadow-scout-3d.high` | 1.956769 × 1.930833 × 1.985614 | Z |
| runtime | `enemies/shadow-scout-3d/shadow-scout-3d.medium` | 1.956769 × 1.930833 × 1.985614 | Z |
| runtime | `enemies/shadow-scout-lod/shadow-scout-lod.high` | 1.934021 × 1.864784 × 1.969361 | Z |
| runtime | `enemies/shadow-scout-lod/shadow-scout-lod.medium` | 1.934021 × 1.864784 × 1.969361 | Z |
| runtime | `enemies/shadow-shield-3d/shadow-shield-3d.high` | 1.990931 × 1.932358 × 1.172065 | X |
| runtime | `enemies/shadow-shield-3d/shadow-shield-3d.medium` | 1.990931 × 1.932358 × 1.172065 | X |
| runtime | `enemies/shadow-splitter-3d/shadow-splitter-3d.high` | 1.999504 × 1.925546 × 0.476947 | X |
| runtime | `enemies/shadow-splitter-3d/shadow-splitter-3d.medium` | 1.999504 × 1.925546 × 0.476947 | X |
| runtime | `enemies/shadow-tank-3d/shadow-tank-3d.high` | 2.005649 × 1.950805 × 0.868990 | X |
| runtime | `enemies/shadow-tank-3d/shadow-tank-3d.medium` | 2.005649 × 1.950805 × 0.868990 | X |
| runtime | `guides/draconis-v4/draconis-v4.high` | 2.000000 × 1.983642 × 1.166173 | X |
| runtime | `guides/draconis-v4/draconis-v4.medium` | 2.000000 × 1.983642 × 1.166173 | X |
| runtime | `heroes/draconis-v2/draconis-v2.high` | 2.000000 × 1.815668 × 1.416913 | X |
| runtime | `heroes/draconis-v2/draconis-v2.medium` | 2.000000 × 1.815668 × 1.416913 | X |
| runtime | `heroes/draconis-v3/draconis-v3.high` | 2.000000 × 0.973235 × 1.349040 | X |
| runtime | `heroes/draconis-v3/draconis-v3.medium` | 2.000000 × 0.973479 × 1.349528 | X |
| runtime | `heroes/draconis/draconis.high` | 2.000000 × 1.835200 × 0.963713 | X |
| runtime | `heroes/draconis/draconis.medium` | 2.000000 × 1.835200 × 0.963713 | X |

## 5. Nguồn, manifest và lỗi đọc

**0 lỗi đọc** trong cả ba game; **0 POSITION thiếu min/max**, **0 animation thiếu thời lượng**, danh sách cần giải nén rỗng. Không cần giải nén meshopt hoặc gọi dịch vụ ngoài. Không có cảnh báo md5 khác với SOURCES.

| Game | Runtime có mục manifest | Runtime nối nguồn | Theo usedBy | Cùng id | Tên duy nhất | standIn được khai báo | Đường dẫn trong ghi chú | Chưa tìm thấy nguồn |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| dragon-hold | 48/54 | 48 | 0 | 14 | 34 | 0 | 0 | 6 |
| typing-defense | 68/68 | 68 | 0 | 48 | 20 | 0 | 0 | 0 |
| space-typing | 378/378 | 368 | 350 | 0 | 0 | 16 | 2 | 10 |

494/500 runtime có manifest tương ứng. 6 runtime Dragon Hold của Draconis không có mục trong `m0b/manifest.json`; giữ `manifest: null`. Tất cả mục đã tìm thấy giữ nguyên object manifest, kể cả size, scale và preset nếu nguồn có; test đối chiếu trực tiếp với JSON nguồn.

484/500 runtime nối được bản gốc. 16 runtime Space dùng bản thay thế được khai báo trong `SOURCES.notMadeYet`; sổ giữ cả id mong muốn và nguyên ghi chú `standIn`. Hai tier `bosses/auriel-hero` nối `bosses/tyrant-g01.glb` bằng đường dẫn được ghi rõ trong SOURCES. Không suy diễn từ tên gần giống.

16 runtime chưa có bản gốc trong phạm vi đọc:

- **dragon-hold**: `guides/draconis-v4/draconis-v4.high`, `guides/draconis-v4/draconis-v4.medium`, `heroes/draconis-v2/draconis-v2.high`, `heroes/draconis-v2/draconis-v2.medium`, `heroes/draconis-v3/draconis-v3.high`, `heroes/draconis-v3/draconis-v3.medium`.

- **space-typing**: `guides/draconis-v4/draconis-v4.high`, `guides/draconis-v4/draconis-v4.medium`, `heroes/draconis-v2/draconis-v2.high`, `heroes/draconis-v2/draconis-v2.medium`, `heroes/draconis-v3/draconis-v3.high`, `heroes/draconis-v3/draconis-v3.medium`, `heroes/draconis/draconis.high`, `heroes/draconis/draconis.medium`, `skills/dragon-fireball/dragon-fireball.high`, `skills/dragon-fireball/dragon-fireball.medium`.

Space SOURCES ghi các bản Draconis và dragon-fireball chỉ còn bản runtime trên máy; không tự lấy nguồn từ game khác. 300 original mang nhãn `owner-tripo`; 378 runtime Space mang nhãn `space-library`; 116 runtime Dragon Hold/Typing Defense đã nối nguồn mang nhãn `owner-tripo`; 6 runtime Dragon Hold chưa rõ nguồn mang nhãn `unknown`. Không suy đoán điều khoản cấp phép khác.

Các ảnh được đọc header: PNG, JPEG, WebP. Không có KTX2 trong lượt này; nhánh ghi `ktx2` có test trong RAM. Không sửa hoặc xuất lại ảnh, texture, GLB hay BIN.

## 6. Kết quả năm phép kiểm

| # | Lệnh/phép kiểm | Kết quả |
| ---: | --- | --- |
| 1 | `node tools/map-factory/registry/scan-assets.mjs` | Đạt, mã thoát 0: 78 + 139 + 583 = 800 GLB; 0 lỗi; 0 cần giải nén; 800 md5 trước/sau khớp. |
| 2 | `node --test tools/map-factory/registry/test` | Không đạt nguyên văn, mã thoát 1: Node v24.22.0 tìm thư mục như module và báo MODULE_NOT_FOUND. Lệnh thay thế `node --test tools/map-factory/registry/test/*.test.mjs` đạt, mã thoát 0: 19 test, 19 đạt, 0 lỗi, 0 bỏ qua. |
| 3 | Đối chiếu bốn original Dragon Hold bằng `node --input-type=module` và assert; kiểm chéo BIN trong bộ test | Đạt: 4/4 đúng số 3D_IMPORT, 0 chênh lệch. Bộ đếm BIN còn kiểm keep của Typing Defense và Vanguard của Space, tổng 6 file thật. |
| 4 | Snapshot md5 toàn bộ nguồn bằng Python trước khi viết bộ quét, so lại sau khi quét và test | Đạt, mã thoát 0: 800 trước, 800 sau, 800 không đổi, 0 thêm/xóa/đổi. Ngoài ra sổ giữ md5 và md5After từng file; test hash lại đủ 800 GLB. |
| 5 | `git status --short` và `git status --short --untracked-files=all` | Không đạt điều kiện toàn repo sạch ngoài phạm vi vì có sẵn 7 dòng của các làn khác. Phần công việc của phiếu gồm đúng 7 file mới trong phạm vi được phép; không sửa hoặc xóa thay đổi cũ. |

### Đối chiếu bốn bản gốc

| File dưới games/dragon-hold/art-src/3d/ | Đã biết | Sổ | Đếm index trong BIN | Chênh lệch |
| --- | ---: | ---: | ---: | ---: |
| `enemies/moss-grunt.glb` | 5708 | 5708 | 5708 | 0 |
| `enemies/blight-wolf.glb` | 5637 | 5637 | 5637 | 0 |
| `generals/moss-banner.glb` | 8382 | 8382 | 8382 | 0 |
| `houses/herb-hut.glb` | 9858 | 9858 | 9858 | 0 |

Bộ đếm độc lập tự đọc chunk, đọc đủ từng bộ ba index trong BIN dựa trên độ dài bufferView và bề rộng component; không dùng accessor.count để suy ra số index. Có kiểm index nằm trong số đỉnh. Typing Defense keep: 18.962; Space Vanguard: 21.193; cả hai cách đếm đều khớp.

### Bằng chứng md5 toàn phiên

Chụp 800 cặp đường dẫn/md5 trước khi tạo scanner, giữ trong bộ nhớ phiên công cụ; sau khi bộ test hoàn tất, Python đọc lại đúng hai cây nguồn của từng game, theo symlink và so sánh cả tập đường dẫn lẫn hash. Không tạo file snapshot ngoài phạm vi được phép.

SHA-256 của bảng md5 chuẩn hóa, cả trước và sau đều là:

```text
1d1d4257e9ac1f6112f4757aeb00c1c5653feef60a65718d267449e97e58568e
```

Chuẩn hóa bảng: sắp đường dẫn theo thứ tự từ điển; nối `đường_dẫn + NUL + md5 + LF` cho từng file rồi SHA-256 UTF-8. Mỗi md5 đầu phiên cũng trùng `md5`/`md5After` trong sổ; có thể kiểm lại các sổ hiện tại bằng lệnh chỉ đọc sau:

```sh
python3 - <<'CHECK'
from pathlib import Path
import json, hashlib
root = Path('tools/map-factory/registry/out')
count = 0
for game in ['dragon-hold', 'typing-defense', 'space-typing']:
    registry = json.loads((root / f'assets.{game}.json').read_text())
    for asset in registry['assets']:
        current = hashlib.md5(Path(asset['file']).read_bytes()).hexdigest()
        assert asset['md5'] == asset['md5After'] == current, asset['file']
        count += 1
print(f'{count} GLB: md5 đầu/cuối/hiện tại đều khớp')
CHECK
```

### Git trước khi bắt đầu

```text
 M docs/CODEX_QUEUE.md
 M games/dragon-hold
 M games/typing-defense
 M games/typing-survival
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/025-map-asset-registry.md
```

Các dòng này có sẵn trong lần `git status --short` đầu tiên. Không thể loại bỏ chúng mà vẫn tuân thủ yêu cầu bảo toàn các làn khác và cấm lệnh Git có ghi. Kiểm riêng phần được phép ghi:

```sh
git status --short --untracked-files=all -- tools/map-factory/registry docs/codex-queue/025-report.md
```

## 7. Chủ dự án cần xem

- Duyệt 267 cờ trục theo danh sách ở mục 4 trước khi dùng hướng model cho sinh map; không có cờ chiều cao vượt ngưỡng.
- Giữ phân biệt bản thay thế được khai báo, bản gốc thực và 16 runtime chưa tìm thấy nguồn; không coi mọi liên kết nguồn là model riêng đã được tạo.
- Dùng lệnh test có glob trên Node hiện tại. Muốn giữ đúng lệnh thư mục cần thay đổi cách chạy hoặc cho phép một file điểm vào ngoài phạm vi phiếu; báo cáo không tự đánh dấu phép kiểm này đạt.
- Điều kiện Git được đánh giá theo phần thay đổi của phiếu; toàn repo đã bẩn từ trước do công việc đồng thời.

Không tạo ảnh, âm thanh, model, không gọi image_gen vì phiếu chỉ yêu cầu lập sổ từ media có sẵn. Không thay đổi kiến trúc Map Factory đang được Claude đánh giá.

## 8. Claude duyệt (27/10/2026)

- **Chạy lại bộ quét:** ba file sổ ra giống hệt từng byte so với bản của Codex. Không lỗi, md5 của 800 GLB không đổi.
- **Test:** `node --test tools/map-factory/registry/test/*.test.mjs` đạt 19/19.
- **Cỡ:** xem tay vài mục, đều hợp lý:
  - Yêu Rêu Lính (bản chạy trong game) cao 1,56 m, đúng chiều cao hình tạm;
  - Lều Thuốc Nam rộng 2,2 m, đúng ô nhà;
  - Lũy rộng 8,2 m, khớp vòng Ø 8,4 m;
  - Tháp Cung cao 7 m.
- **Cờ trục:** 267 mục bị cờ "sinh vật nằm dọc X/Z" chỉ là cờ thô. Model Space nằm theo hướng bay là đúng thiết kế. Bản gốc Tripo của Rồng Giữ Ải đã được preset M0b xoay lại trong bản chạy trong game. Map Factory sẽ đọc hướng từ manifest, không đọc từ cờ này.
- **Đã sửa:** sáu dòng chú thích mã viết tiếng Việt, đổi sang tiếng Anh theo luật repo.
- **Đã sửa:** `node --test <thư mục>` không chạy được trên Node 24, nên README dùng lệnh glob. Đây không phải lỗi của phiếu.
- **Giới hạn:** test và bộ quét cần media có trên máy, nên chỉ chạy được ở máy có media (Mac này, hoặc sau `pnpm media:pull`). Sổ đầu ra là văn bản, được commit để các bộ sinh bản đồ đọc được trên máy không có media.
