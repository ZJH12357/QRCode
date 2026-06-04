import os
import tkinter as tk
from tkinter import messagebox, filedialog

from qrcode_generator import generate


def choose_save_path(default_name="qrcode.png"):
    path = filedialog.asksaveasfilename(defaultextension=".png", initialfile=default_name,
                                        filetypes=[("PNG 图片", "*.png")])
    return path


def on_generate(url_entry, output_entry, box_var, border_var, open_var):
    url = url_entry.get().strip()
    out = output_entry.get().strip() or "qrcode.png"
    try:
        box = int(box_var.get())
        border = int(border_var.get())
    except ValueError:
        messagebox.showerror("错误", "请确保方块大小和边框为整数")
        return

    if not url:
        messagebox.showwarning("提示", "请输入要生成的 URL")
        return

    try:
        saved = generate(url, out, box_size=box, border=border)
        messagebox.showinfo("完成", f"已生成：{saved}")
        if open_var.get():
            try:
                os.startfile(saved)
            except Exception:
                pass
    except Exception as e:
        messagebox.showerror("失败", f"生成二维码时出现错误：{e}")


def build_gui():
    root = tk.Tk()
    root.title("二维码生成器")
    root.geometry("480x220")

    frm = tk.Frame(root, padx=10, pady=10)
    frm.pack(fill=tk.BOTH, expand=True)

    tk.Label(frm, text="网址 (URL):").grid(row=0, column=0, sticky=tk.W)
    url_entry = tk.Entry(frm, width=50)
    url_entry.grid(row=0, column=1, columnspan=3, sticky=tk.W)

    tk.Label(frm, text="输出文件: ").grid(row=1, column=0, sticky=tk.W)
    output_entry = tk.Entry(frm, width=36)
    output_entry.insert(0, "qrcode.png")
    output_entry.grid(row=1, column=1, sticky=tk.W)
    def on_browse():
        p = choose_save_path(os.path.basename(output_entry.get()) or "qrcode.png")
        if p:
            output_entry.delete(0, tk.END)
            output_entry.insert(0, p)
    tk.Button(frm, text="浏览...", command=on_browse).grid(row=1, column=2, sticky=tk.W)

    tk.Label(frm, text="方块像素: ").grid(row=2, column=0, sticky=tk.W)
    box_var = tk.StringVar(value="10")
    tk.Spinbox(frm, from_=1, to=40, textvariable=box_var, width=5).grid(row=2, column=1, sticky=tk.W)

    tk.Label(frm, text="边框块数: ").grid(row=2, column=2, sticky=tk.W)
    border_var = tk.StringVar(value="4")
    tk.Spinbox(frm, from_=0, to=10, textvariable=border_var, width=5).grid(row=2, column=3, sticky=tk.W)

    open_var = tk.BooleanVar(value=False)
    tk.Checkbutton(frm, text="生成后打开图片", variable=open_var).grid(row=3, column=1, columnspan=2, sticky=tk.W)

    gen_btn = tk.Button(frm, text="生成二维码", width=20,
                        command=lambda: on_generate(url_entry, output_entry, box_var, border_var, open_var))
    gen_btn.grid(row=4, column=1, pady=12)

    def on_quit():
        root.destroy()
    tk.Button(frm, text="退出", command=on_quit).grid(row=4, column=2)

    root.mainloop()


if __name__ == '__main__':
    build_gui()
