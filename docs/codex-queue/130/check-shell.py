#!/usr/bin/env python3
import os, shlex, subprocess, sys
args = sys.argv[1:]
if len(args) == 2 and args[0] == '-c':
    cmd = args[1]
    for script in ['test', 'build']:
        cmd = cmd.replace('pnpm ' + script, 'pnpm --config.script-shell=' + shlex.quote(__file__) + ' ' + script)
    if cmd == 'vitest run':
        cmd = 'vitest run --no-cache'
    elif cmd == 'tsc --noEmit && vite build':
        cmd += ' --configLoader runner --outDir "$TICKET130_BUILD_DIR" --emptyOutDir'
    args = ['-c', cmd]
sys.exit(subprocess.call(['/bin/sh', *args]))
