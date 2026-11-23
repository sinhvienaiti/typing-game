path = 'content/english/qa-batches/INDEX.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'batch-10.json' in line:
        lines[i] = line.replace('pending', 'in_progress (500/5000)')
        print(f'Updated line {i+1}: {lines[i].strip()}')
with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
