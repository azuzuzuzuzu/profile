from pathlib import Path
import struct

p = Path(__file__).resolve().parent
out = []
for name in ['cursor.png', 'cursor-pointer.png']:
    f = p / name
    if not f.exists():
        out.append(f'{name}: MISSING')
        continue
    data = f.read_bytes()
    line = f'{name}: {len(data)} bytes'
    if data[:8] == b'\x89PNG\r\n\x1a\n' and len(data) >= 24:
        w, h = struct.unpack('>II', data[16:24])
        line += f', {w}x{h}'
    out.append(line)
(p / '_cursor_info.txt').write_text('\n'.join(out), encoding='utf-8')
print('\n'.join(out))
