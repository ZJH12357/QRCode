import zipfile
from pathlib import Path

root = Path(__file__).parent
files = [root / 'dist' / 'qrcode_generator.exe', root / 'dist' / 'qrcode_gui.exe', root / 'README.md']
out = root / 'qrcode_release.zip'

with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for f in files:
        if f.exists():
            z.write(f, arcname=f.name)
            print('Added', f.name)
        else:
            print('Missing', f)

print('Created', out)
