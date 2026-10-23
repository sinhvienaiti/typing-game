"""CLI: python -m critic <lệnh>  (qua tools/audio-lab/run.sh critic … hoặc pnpm audio:critic …)."""
from __future__ import annotations

import argparse
import json
import sys

DESC = """Tai AI nhiều lớp (mục 4 của docs/games/AUDIO_PIPELINE.md).

Lệnh:
  run     chấm file hoặc thư mục âm: JSON cho mỗi file, thẻ ảnh PNG, summary.md
  groups  liệt kê nhóm âm (khóa dùng cho --group và trường group của thẻ spec)
  schema  in JSON Schema của file kết quả
  pairs   so cặp bản gốc / bản làm hỏng (<tên>__clipped|muddy|thin) trên kết quả đã chấm
  agreement  so xếp hạng của máy với điểm mù của chủ dự án (mục 4.6), trước và sau file hiệu chỉnh

Ví dụ:
  run.sh critic run ~/AudioLab/work/typing-survival/gun.xung/r1 --spec gun.xung.yaml
  run.sh critic run a.wav b.wav --layers fast --group hit_heavy --out ~/AudioLab/work/_critic/thu
  run.sh critic run raw/ --stage raw        # file vừa tạo, chưa qua chuỗi sửa
  run.sh critic run cands/ --spec tools/audio-lab/specs/typing-survival --refs approved/ --layers L1,L1b,L2,L6
"""


def _run(a) -> int:
    from .pipeline import Options, parse_layers, run
    try:
        layers = parse_layers(a.layers)
    except ValueError as e:
        print(f"audio-lab critic: {e}", file=sys.stderr)
        return 2
    if a.no_png:
        layers = tuple(x for x in layers if x != "L6")
    if a.group:
        from .groups import GROUPS
        if a.group not in GROUPS:
            print(f"audio-lab critic: nhóm '{a.group}' không có; xem: run.sh critic groups", file=sys.stderr)
            return 2
    opts = Options(layers=layers, stage=a.stage, group=a.group, game=a.game, variant_set=a.variant_set,
                   clap_models=tuple(a.clap_models.split(",")) if a.clap_models else (), seed=a.seed, quiet=a.quiet,
                   blind_cards=a.blind_cards, calibration=a.calibration)
    from .calibration import CalibrationError
    try:
        batch = run(a.inputs, spec_path=a.spec, refs=a.refs or [], out_dir=a.out, opts=opts, sources=a.sources)
    except (FileNotFoundError, CalibrationError) as e:
        print(f"audio-lab critic: {e}", file=sys.stderr)
        return 2
    if a.fail_on_block and batch["counts"]["BLOCK"]:
        return 1
    return 0


def _groups(_a) -> int:
    from .groups import FAMILIES, GROUPS
    print("| Khóa | Tên | Họ | Dài (ms) | Lên ≤ (ms) | Im lặng đầu ≤ (ms) | Lặp | Stereo | Bẩn | Mục tiêu L2 |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for g in GROUPS.values():
        dur = "–" if not g.dur_ms else f"{g.dur_ms[0]:g}–{g.dur_ms[1]:g}"
        print(f"| `{g.key}` | {g.name_vi} | {g.family} ({FAMILIES[g.family]}) | {dur} | "
              f"{'–' if g.attack_max_ms is None else f'{g.attack_max_ms:g}'} | {'–' if g.head_max_ms is None else f'{g.head_max_ms:g}'} | "
              f"{'có' if g.loop else '–'} | {'được' if g.stereo_ok else 'mono'} | {'có' if g.dirty else '–'} | "
              f"{', '.join(t.feature for t in g.targets)} |")
    return 0


def _schema(_a) -> int:
    from .schema import FILE_SCHEMA
    print(json.dumps(FILE_SCHEMA, ensure_ascii=False, indent=1))
    return 0


def _pairs(a) -> int:
    from .calibrate import main
    main(a.dirs)
    return 0


def _agreement(a) -> int:
    from .agreement import main
    from .calibration import CalibrationError
    try:
        return main(a)
    except CalibrationError as e:
        print(f"audio-lab critic: {e}", file=sys.stderr)
        return 2


def _safe_env() -> None:
    """Same environment as run.sh (offline HF cache, no token) when started as `python -m critic`."""
    import os
    if os.environ.get("HF_HUB_DISABLE_IMPLICIT_TOKEN") == "1" and os.environ.get("HF_HOME"):
        return                       # run.sh / launch.py already applied it
    from common import env
    env.apply()


def main(argv: list[str] | None = None) -> int:
    _safe_env()
    p = argparse.ArgumentParser(prog="critic", description=DESC, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="chấm file hoặc thư mục âm")
    r.add_argument("inputs", nargs="+", help="file âm hoặc thư mục (tìm đệ quy wav, flac, ogg, mp3, aiff)")
    r.add_argument("--spec", help="thẻ spec YAML, hoặc thư mục thẻ (khớp theo id ở đầu tên file)")
    r.add_argument("--refs", nargs="+", help="âm tham chiếu đã duyệt (file hoặc thư mục), cho file mà thẻ spec "
                                             "không ghi refs; nên chạy mỗi lần một id hoặc một nhóm")
    r.add_argument("--sources", action="append", metavar="FILE",
                   help="sổ nguồn SOURCES.json hoặc licences.jsonl: file có aiInputAllowed=false không vào mô hình "
                        "(lặp lại được; sổ thư viện ~/AudioLab/libraries/SOURCES.jsonl luôn được đọc)")
    r.add_argument("--layers", default="all",
                   help="L1,L1b,L2,L3,L4,L5,L6 | all (mặc định) | fast (= L1,L1b,L2,L6, không nạp mô hình)")
    r.add_argument("--out", help="thư mục kết quả (mặc định ~/AudioLab/work/_critic/<giờ>)")
    r.add_argument("--stage", choices=("final", "raw"), default="final",
                   help="final: mọi lỗi vệ sinh đều chặn; raw: chỉ clip chặn, lỗi khác thành việc sửa")
    r.add_argument("--group", help="ép nhóm âm cho mọi file (xem: critic groups)")
    r.add_argument("--game", help="dragon-hold | typing-defense | typing-survival | space-typing (bộ nhãn CLAP)")
    r.add_argument("--variant-set", action="store_true",
                   help="các file là biến thể của một id: bản lặp của âm ngắn xoay vòng các biến thể")
    r.add_argument("--clap-models", help="danh sách mô hình CLAP, cách nhau bằng dấu phẩy")
    r.add_argument("--no-png", action="store_true", help="không vẽ thẻ ảnh (bỏ L6)")
    r.add_argument("--blind-cards", action="store_true",
                   help="vẽ thêm <tên>.blind.png cho Bảng Nghe: không tên file, không kết luận, không điểm")
    r.add_argument("--seed", type=int, default=0, help="hạt ngẫu nhiên cho việc chọn bản dò")
    r.add_argument("--calibration", help="file hiệu chỉnh theo điểm chủ dự án (đường dẫn, số phiên bản, hoặc "
                                         "none = trọng số và mục tiêu gốc của kế hoạch); mặc định: bản mới nhất "
                                         "trong critic/calibration/")
    r.add_argument("--fail-on-block", action="store_true", help="thoát mã 1 nếu có file bị chặn")
    r.add_argument("--quiet", action="store_true")
    r.set_defaults(fn=_run)
    sub.add_parser("groups", help="liệt kê nhóm âm").set_defaults(fn=_groups)
    sub.add_parser("schema", help="in JSON Schema của file kết quả").set_defaults(fn=_schema)
    q = sub.add_parser("pairs", help="so cặp bản gốc / bản làm hỏng")
    q.add_argument("dirs", nargs="+", help="thư mục kết quả của critic run")
    q.set_defaults(fn=_pairs)
    g = sub.add_parser("agreement", help="so máy với điểm mù của chủ dự án, trước và sau hiệu chỉnh")
    g.add_argument("--review", help="thư mục điểm chấm (mặc định ~/AudioLab/review)")
    g.add_argument("--batch", action="append", help="chỉ lô này (lặp lại được; mặc định 0a và 0b)")
    g.add_argument("--calibration", help="file hiệu chỉnh để so (mặc định: bản mới nhất; none = chỉ in trước)")
    g.add_argument("--json", help="ghi số liệu đầy đủ ra file JSON (ngoài repo)")
    g.add_argument("--md", help="ghi báo cáo Markdown ra file (ngoài repo)")
    g.set_defaults(fn=_agreement)
    a = p.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
