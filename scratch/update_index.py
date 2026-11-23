def update_index(batch_num, progress_str):
    with open('content/english/qa-batches/INDEX.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for the line corresponding to batch_num
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if line.startswith(f'| {batch_num} ') or line.startswith(f'| {batch_num:02d} '):
            parts = [p.strip() for p in line.split('|')]
            # parts: ['', '10', '`batch-10.json`', '5000', 'secateurs ... horehound', 'Phase 1 (100k Core & Standard)', '⏳ `in_progress` (500/5000)', '']
            if len(parts) >= 8:
                parts[6] = progress_str
                lines[i] = ' | '.join(parts).strip()
                if not lines[i].startswith('|'):
                    lines[i] = '| ' + lines[i]
                if not lines[i].endswith('|'):
                    lines[i] = lines[i] + ' |'
                break

    with open('content/english/qa-batches/INDEX.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print('Updated INDEX.md for batch', batch_num, '->', progress_str)

if __name__ == '__main__':
    import sys
    batch = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    prog = sys.argv[2] if len(sys.argv) > 2 else '⏳ `in_progress` (1000/5000)'
    update_index(batch, prog)
