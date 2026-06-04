import argparse
import qrcode


def generate(url: str, out: str = "qrcode.png", box_size: int = 10, border: int = 4) -> str:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(out)
    return out


def main():
    parser = argparse.ArgumentParser(description="将网址生成二维码并保存为 PNG")
    parser.add_argument("url", help="要编码的网址，例如：https://example.com")
    parser.add_argument("-o", "--output", default="qrcode.png", help="输出 PNG 文件名，默认 qrcode.png")
    parser.add_argument("--box-size", type=int, default=10, help="二维码单个方块像素大小，默认 10")
    parser.add_argument("--border", type=int, default=4, help="二维码边框块数，默认 4")
    args = parser.parse_args()

    out = generate(args.url, args.output, args.box_size, args.border)
    print(f"已保存：{out}")


if __name__ == "__main__":
    main()
