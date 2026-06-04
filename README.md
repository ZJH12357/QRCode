# QR Code 生成器

将网址转换为二维码并保存为 PNG 的简单脚本。

快速使用：

```bash
python qrcode_generator.py "https://example.com" -o example_qr.png
```

安装依赖：

```bash
pip install -r requirements.txt
```

打包为独立 Windows 可执行文件（可选）

如果你希望为最终用户提供无需安装 Python 的单文件 `.exe`：

- 在用于构建的 Windows 机器上运行 `build_exe.bat`（该脚本会安装 `pyinstaller` 并调用它）。
- 构建完成后，执行文件位于 `dist\qrcode_generator.exe`，拷贝该文件到目标机器即可运行并生成 PNG。

注意：打包操作需要在有 Python 的机器上进行（建议 Python 3.8+）。最终用户运行生成的 `.exe` 不需要 Python 环境。

简单的构建流程（手动步骤概览）：

1. 在构建机器上安装依赖：`pip install -r requirements.txt`
2. 运行：`build_exe.bat`
3. 在 `dist` 文件夹中找到 `qrcode_generator.exe` 并测试运行。

在没有 Python 的测试机器上验证：将 `dist\qrcode_generator.exe` 复制到该机器，双击或通过命令行运行，提供 URL 并确认 PNG 已生成。

自定义图标与隐藏控制台

如果希望为生成的可执行文件设置图标或在运行时不显示控制台，可以向 `build_exe.bat` 传入可选参数：

- 指定图标（.ico 文件）：`build_exe.bat icon.ico`。
- 隐藏控制台窗口（windowed）：`build_exe.bat icon.ico windowed` 或 `build_exe.bat "" windowed`（若不需图标，可传空字符串占位）。

示例：

```powershell
pip install -r requirements.txt
.\build_exe.bat icon.ico windowed
```

注意：隐藏控制台后，程序仍然接受命令行参数并在后台运行，但不会显示交互式提示。若你需要图形界面，请考虑实现 GUI 版本。

使用图形界面（GUI）

如果你更喜欢点两下就能操作的界面，仓库中有一个简单的图形界面程序 `gui.py`，可以通过以下步骤运行：

1. 在项目文件夹打开命令行（PowerShell），安装依赖：

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

2. 运行 GUI：

```powershell
python gui.py
```

3. 使用方法（窗口操作）：
- 在“网址 (URL)”输入框粘贴你要生成的链接。
- 在“输出文件”里填写要保存的图片名，或点击“浏览...”选择保存位置。
- 可以调整“方块像素”和“边框块数”以改变二维码的大小和留白。
- 勾选“生成后打开图片”会在生成后自动打开图片。
- 点击“生成二维码”按钮，成功后会弹窗提示已生成的文件路径。

额外说明：
- 运行 GUI 需要系统上有 Python（Windows 通常自带 `tkinter`，如果没有可以通过 `pip install Pillow` 等安装相关依赖）。
- 如果你希望把 GUI 打包成单文件 `.exe`，可以使用 PyInstaller：

```powershell
pyinstaller --onefile --windowed --name qrcode_gui gui.py
```

这样会在 `dist` 文件夹生成 `qrcode_gui.exe`，拷贝到目标机器即可运行（无需 Python）。

