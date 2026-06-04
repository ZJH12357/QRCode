# QR Code 生成器
将网址或任意文本生成二维码（PNG 格式）的轻量工具。

提供两种使用方式：
- 命令行版：适合脚本化或高级用户。
- 图形界面（GUI）：适合普通用户，支持双击打开窗口填写网址并生成图片。

目录与入口
- 核心逻辑：`qrcode_generator.py`（生成二维码的函数与命令行入口）
- 图形界面：`gui.py`（Tkinter，双击或 `python gui.py` 运行）
- 打包脚本：`build_exe.bat`（Windows 平台辅助打包）
- 打包输出目录：`dist/`（打包后生成的 `.exe` 放在这里）

环境要求
- Python 3.8+（若运行源码）
- Windows/macOS/Linux 均可运行源码（已测试 Windows）

安装依赖
在项目根目录运行：
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

命令行 使用示例
- 使用源码：
```powershell
python qrcode_generator.py "https://example.com" -o example_qr.png
```
- 使用已打包的 Windows 可执行（若你已从 `dist/` 中拿到 exe）：
```powershell
.\dist\qrcode_generator.exe "https://example.com" -o example_qr.png
```
- 查看命令行帮助：
```powershell
python qrcode_generator.py -h
```

图形界面（推荐非技术用户）
- 运行源码 GUI：
```powershell
python gui.py
```
- GUI 使用步骤：
	- 在“网址 (URL)”输入框粘贴或输入要生成的链接/文本；
	- 在“输出文件”填写文件名或点击“浏览...”选择保存位置；
	- 可调整“方块像素”和“边框块数”以改变二维码清晰度与留白；
	- 勾选“生成后打开图片”会在生成后自动打开图片；
	- 点击“生成二维码”，成功后弹窗会显示已生成的文件路径。

打包（生成单文件 exe）
- 使用内置脚本（Windows）：
```powershell
.\build_exe.bat
```
- 手动（示例，GUI）：
```powershell
pyinstaller --onefile --windowed --name qrcode_gui --icon gui_icon.ico gui.py
```
- 建议把最终的 `.exe` 放到 GitHub Releases 或云盘，不要将二进制直接提交到源码仓库。

图标替换
- 若要更换可执行文件图标，请准备一个包含多尺寸的 `.ico` 文件，然后在打包命令中使用 `--icon new_icon.ico`。仓库内已有 `make_icon.py` / `convert_to_gui_icon.py` 用于生成 `.ico`。

.gitignore 与版本控制建议
- 建议在 `.gitignore` 中忽略以下项以保持仓库整洁：
	- `dist/`, `build/`, `*.exe`, `*.zip`, `*.spec`, `venv/`, `__pycache__/`, `.vscode/` 等。

常见问题（FAQ）
- 双击 exe 没反应：尝试在命令行运行 exe 查看错误信息，或以管理员身份运行；也可用命令行版测试功能是否正常。
- 杀毒软件误报：未签名的可执行文件可能被误报。若要公开分发，请考虑对 exe 进行数字签名或使用安装器。
- 覆盖文件风险：若输出文件名与现有文件重名，会直接覆盖，请提前备份重要文件。
- 链接无效：程序仅把你输入的文本编码进二维码，不会校验网址是否能访问，请确保输入正确。

安全与隐私
- 所有二维码在本地生成，不会上传到任何服务器（除非你自己部署了在线版本）。

后续建议
- 如果面向非技术用户分发，优先打包 GUI 为 exe 并上传到 GitHub Releases，附一页简短使用说明。
- 需要我代为生成 Release 包、制作安装程序或签名 exe，请告诉我具体需求。

----
如需我直接把这份文档写入 `README.md`（我可以替换文件），我现在可以为你直接替换。

