# -*- coding: utf-8 -*-
import os

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    rel = os.path.relpath(root, '.')
    depth = 0 if rel == '.' else rel.count(os.sep) + 1
    indent = '  ' * depth
    print(f"{indent}[{os.path.basename(root) if rel != '.' else 'PROJECT_ROOT'}] (dirs: {len(dirs)}, files: {len(files)})")
    for f in sorted(files):
        p = os.path.join(root, f)
        sz = os.path.getsize(p)
        if sz > 1024 * 1024:
            sz_str = f"{sz / 1024 / 1024:.2f} MB"
        else:
            sz_str = f"{sz / 1024:.1f} KB"
        print(f"{indent}  - {f} ({sz_str})")
