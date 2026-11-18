# Phiếu 309 · `vfxflip export-video`

Đã hoàn tất ngày 06/11/2026.

- Sửa `tools/vfx-flipbook/vfxflip/__main__.py`: thêm lệnh `export-video`, đủ các cờ trong phiếu; gốc repo mặc định theo `parents[3]`.
- Thêm `tools/vfx-flipbook/vfxflip/video_export.py`: giữ nguyên công thức cắt, peakTime và pivot toàn khung; ffmpeg 24 fps theo lệnh đã chốt, ffprobe đếm khung và đọc kích thước thật; tối đa `--jobs` tác vụ. Video và manifest đều ghi qua file tạm rồi thay nguyên tử; giữ các trường khác. Tự xuất lại khi `video.take` khác take hiện tại; video thiếu take vẫn được bỏ qua.
- Thêm `tools/vfx-flipbook/tests/test_video_export.py`: kiểm công thức, pivot thật của Myriad Lotus, bộ lọc/bỏ qua, take/force, dry-run không ghi, giới hạn song song, giữ trường khác, lỗi xuất và nguồn thiếu khung. Nguồn testsrc 2 giây/24 fps được xuất thử trong thư mục tạm với cả khung ngang và vuông; kiểm H.264, yuv420p, số khung, không âm thanh và faststart.

**Kiểm chứng:** chạy qua `run.sh`/venv AudioLab, theo `pytest.ini` của công cụ; toàn bộ test cũ và mới **54 passed in 10.50s**. `git diff --check` sạch. Cache và dữ liệu test đặt trong `/private/tmp/codex-309-*`.

```bash
VFXLAB_HOME=/private/tmp/codex-309-vfxflip tools/vfx-flipbook/run.sh test -q -o cache_dir=/private/tmp/codex-309-vfxflip/pytest --basetemp=/private/tmp/codex-309-pytest
```

**Dry-run thật:** cả hai lệnh thoát mã 0; expansion có 30 mục, **0 cần xuất**; fire có 28 mục, **6 cần xuất**, 22 mục bỏ qua. Đầu ra nguyên văn:

```bash
VFXLAB_HOME=/private/tmp/codex-309-vfxflip tools/vfx-flipbook/run.sh export-video --manifest games/immortality-cultivation/art-src/lab/vfx/expansion/manifest.json --dry-run
```

```text
skip myriad-lotus-domain: đã có video cùng take (hoặc chưa ghi video.take)
skip firmament-sundering-cleave: đã có video cùng take (hoặc chưa ghi video.take)
skip glacial-moon-tide: đã có video cùng take (hoặc chưa ghi video.take)
skip karmic-ember-tempest: đã có video cùng take (hoặc chưa ghi video.take)
skip nine-heavens-tribulation-net: đã có video cùng take (hoặc chưa ghi video.take)
skip samsara-blood-mandala: đã có video cùng take (hoặc chưa ghi video.take)
skip astral-meteor-constellation: đã có video cùng take (hoặc chưa ghi video.take)
skip asura-six-arms-avatar: đã có video cùng take (hoặc chưa ghi video.take)
skip heaven-earth-titan-avatar: đã có video cùng take (hoặc chưa ghi video.take)
skip miasma-briar-abyss: đã có video cùng take (hoặc chưa ghi video.take)
skip myriad-palm-bodhi-avatar: đã có video cùng take (hoặc chưa ghi video.take)
skip azure-cloud-dragon: đã có video cùng take (hoặc chưa ghi video.take)
skip immortal-sword-progenitor-avatar: đã có video cùng take (hoặc chưa ghi video.take)
skip nether-samsara-monarch-avatar: đã có video cùng take (hoặc chưa ghi video.take)
skip polar-star-emperor-avatar: đã có video cùng take (hoặc chưa ghi video.take)
skip white-fiend-tiger: đã có video cùng take (hoặc chưa ghi video.take)
skip abyssal-xuanwu-tortoise: đã có video cùng take (hoặc chưa ghi video.take)
skip all-knowing-baize-spirit: đã có video cùng take (hoặc chưa ghi video.take)
skip astral-kunpeng-leviathan: đã có video cùng take (hoặc chưa ghi video.take)
skip auspicious-thunder-qilin: đã có video cùng take (hoặc chưa ghi video.take)
skip vermilion-solar-phoenix: đã có video cùng take (hoặc chưa ghi video.take)
skip blade-swallowing-immortal-gourd: đã có video cùng take (hoặc chưa ghi video.take)
skip mountain-crushing-imperial-seal: đã có video cùng take (hoặc chưa ghi video.take)
skip nine-dragon-refining-cauldron: đã có video cùng take (hoặc chưa ghi video.take)
skip nine-tailed-celestial-fox: đã có video cùng take (hoặc chưa ghi video.take)
skip primordial-chaos-bell: đã có video cùng take (hoặc chưa ghi video.take)
skip five-element-heavenly-silk: đã có video cùng take (hoặc chưa ghi video.take)
skip seven-treasure-suppressing-pagoda: đã có video cùng take (hoặc chưa ghi video.take)
skip twelve-stem-nether-banners: đã có video cùng take (hoặc chưa ghi video.take)
skip yin-yang-void-mirror: đã có video cùng take (hoặc chưa ghi video.take)
dry-run: 0 mục cần xuất
```

```bash
VFXLAB_HOME=/private/tmp/codex-309-vfxflip tools/vfx-flipbook/run.sh export-video --manifest games/immortality-cultivation/art-src/lab/vfx/fire/manifest.json --dry-run
```

```text
skip fire-charge: thiếu trim
skip dragonhold-charge-orb: loop: true
skip fire-burst: thiếu trim
skip fire-sparks: thiếu trim
skip dragonhold-embers: thiếu trim
skip dragonhold-flame-trail: loop: true
skip fire-trail: loop: true
skip fire-ground: thiếu trim
skip fire-brush-slash: thiếu trim
skip fire-crescent-sweep: thiếu trim
skip fire-gold-dust: loop: true
skip fire-halo-ring: thiếu trim
skip fire-halo-seal-loop: loop: true
skip fire-spark-spray: thiếu trim
skip fire-twinkle-set: thiếu trim
plan fire-ground-mark: START=0 END=121 duration=5.042s peakTime=0.000s
plan fire-slash-arc: START=0 END=110 duration=4.583s peakTime=0.000s
plan fire-crescent-sym: START=0 END=121 duration=5.042s peakTime=0.000s
skip fire-charge-gather-w2: loop: true
skip twin-fire-spiral-charge-w2: loop: true
skip fire-embers-rising-loop-w2: loop: true
plan fire-spark-spray-w2: START=15 END=79 duration=2.667s peakTime=1.750s
plan fire-smoke-roll-white-w2: START=0 END=121 duration=5.042s peakTime=3.333s
skip strip-fire-sheath-flow-w2: loop: true
skip style-w2-fire-ribbon: loop: true
plan style-w2-fire-qi-burst: START=9 END=73 duration=2.667s peakTime=1.667s
skip fire-ground-burn-loop-w2: loop: true
skip fire-comet: loop: true
dry-run: 6 mục cần xuất
```

**Không làm:** không xuất video hay sửa manifest thật, không chạy build/test game, không dùng mạng hoặc lệnh Git ghi. Không sửa README vì công cụ chưa có README. Không có mục bắt buộc nào còn bỏ dở.

**Anh cần xem:** sáu kế hoạch của fire ở trên trước khi chạy xuất thật.

