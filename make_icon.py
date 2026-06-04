from PIL import Image, ImageDraw

def make_icon(path="icon.ico", size=256):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 背景圆
    draw.ellipse((0, 0, size-1, size-1), fill=(255, 224, 102, 255), outline=(0,0,0))

    # 眼睛
    ex = int(size * 0.28)
    ey = int(size * 0.28)
    ew = int(size * 0.10)
    eh = int(size * 0.16)
    draw.ellipse((ex, ey, ex+ew, ey+eh), fill=(0,0,0))
    ex2 = int(size * 0.62)
    draw.ellipse((ex2, ey, ex2+ew, ey+eh), fill=(0,0,0))

    # 嘴巴（弧线）
    mouth_box = (int(size*0.25), int(size*0.45), int(size*0.75), int(size*0.8))
    draw.arc(mouth_box, start=200, end=340, fill=(0,0,0), width=max(2, size//40))

    # 保存为 ico，包含多个尺寸
    sizes = [(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)]
    img.save(path, format='ICO', sizes=sizes)
    print(f"已生成图标: {path}")

if __name__ == '__main__':
    make_icon()
