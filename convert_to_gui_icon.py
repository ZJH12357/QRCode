from PIL import Image
from pathlib import Path

src = Path(__file__).parent / '图标.png'
out = Path(__file__).parent / 'gui_icon.ico'

if not src.exists():
    print('源图像 图标.png 未找到，当前目录文件：')
    for f in Path(__file__).parent.iterdir():
        print(' -', f.name)
    raise SystemExit(1)

im = Image.open(src).convert('RGBA')
sizes = [(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)]
im.save(out, format='ICO', sizes=sizes)
print('已生成图标:', out)
