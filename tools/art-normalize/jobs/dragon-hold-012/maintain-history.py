#!/usr/bin/env python3
"""Chuyển hồ sơ 012 sang trạng thái lưu trữ và sửa các chốt an toàn cũ."""
import ast
from pathlib import Path

JOB = Path(__file__).resolve().parent


class Safety(ast.NodeTransformer):
    def visit_Assert(self, node):
        return ast.If(test=ast.UnaryOp(op=ast.Not(), operand=node.test), body=[ast.Raise(
            exc=ast.Call(func=ast.Name(id="ValueError", ctx=ast.Load()),
                         args=[node.msg or ast.Constant("Kiểm tra hồ sơ 012 không đạt.")], keywords=[]), cause=None)], orelse=[])

    def visit_Call(self, node):
        self.generic_visit(node)
        if isinstance(node.func, ast.Attribute) and node.func.attr in ("write_text", "write_bytes"):
            method = "write_text_new" if node.func.attr == "write_text" else "write_bytes_new"
            return ast.copy_location(ast.Call(func=ast.Name(id=method, ctx=ast.Load()),
                                             args=[node.func.value, *node.args], keywords=node.keywords), node)
        return node


def main():
    for filename in ("normalize_dragon.py", "finalize_dragon.py"):
        path = JOB / filename
        text = path.read_text(encoding="utf-8")
        if "HỒ SƠ 012 ĐÃ KHÓA" in text:
            continue
        # These files are records, deliberately not an executable production workflow.
        text = text.replace("    main()\n", '    raise SystemExit("Hồ sơ Phiếu 012 đã khóa; dùng rebuild-012b.sh cho lô sửa.")\n')
        text = text.replace("c.replace(str(tmp),", "c.replace(str(tmp.relative_to(REPO)),")
        text = text.replace("'seam_rgb_mae_255']['x']==0", "'seams']['x']['pass']")
        # Remove the unused fallback to a different source's prompt.
        text = text.replace("    if original and not original.exists() and src.stem.endswith('.v1'):\n        original=src.with_name(src.stem[:-3]+'.prompt.txt')\n", "")
        tree = ast.fix_missing_locations(Safety().visit(ast.parse(text)))
        body = ast.unparse(tree)
        helpers = '''# HỒ SƠ 012 ĐÃ KHÓA: không dùng để tái tạo ảnh bằng công cụ 012b.
import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[2]))

def write_text_new(path, text, encoding='utf-8'):
    with open(path, 'x', encoding=encoding) as output:
        output.write(text)

def write_bytes_new(path, data):
    with open(path, 'xb') as output:
        output.write(data)

'''
        # Retain historical calculations, but all entry points refuse execution.
        path.write_text("#!/usr/bin/env python3\n" + helpers + body + "\n", encoding="utf-8")
    path = JOB / "normalize_dragon.py"
    text = path.read_text(encoding="utf-8")
    text = text.replace("write_bytes_new(prompt, original.read_bytes())", "write_bytes_new(prompt, ('Dẫn xuất từ ' + str(src) + ' bằng ' + '\\n'.join(commands) + '\\nPrompt nguồn:\\n').encode('utf-8') + original.read_bytes())")
    path.write_text(text, encoding="utf-8")
    for path in JOB.glob("*.sh"):
        if path.name in ("probe.sh", "rebuild-012b.sh"):
            continue
        text = path.read_text(encoding="utf-8")
        text = text.replace('source "$(dirname -- "${BASH_SOURCE[0]}")/common.sh"',
                            'source "$(dirname -- "${BASH_SOURCE[0]}")/../../common.sh"')
        if "Hồ sơ 012 đã khóa" not in text:
            text = text.replace("set -euo pipefail\n", "set -euo pipefail\nprintf '%s\\n' 'Hồ sơ 012 đã khóa; dùng rebuild-012b.sh.' >&2\nexit 1\n")
        text = text.replace('work_dir="$(mktemp', 'mkdir -p "$ART_NORMALIZE_DIR/.tmp"\nwork_dir="$(mktemp')
        path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit("Hồ sơ chuyển script 012 đã khóa; không chạy lại trên runner 012b.")
