@echo off
REM 使用 PyInstaller 将 qrcode_generator.py 打包为独立的 Windows 可执行文件
REM 用法: build_exe.bat [icon_path] [windowed]
REM   icon_path - 可选，指定 .ico 文件路径（相对或绝对），例如 icon.ico
REM   windowed  - 可选，填写任意值则隐藏控制台（使用 --windowed/--noconsole）

python -m pip install --upgrade pip
pip install pyinstaller

SET ICON_ARG=
SET WINDOWED_ARG=--console

IF NOT "%1"=="" (
	IF EXIST "%~1" (
		ECHO 使用图标: %~1
		SET ICON_ARG=--icon "%~1"
	) ELSE (
		ECHO 图标文件 %~1 未找到，忽略图标设置。
	)
)

IF NOT "%2"=="" (
	REM 传入第二个参数表示使用 windowed 模式（隐藏控制台）
	SET WINDOWED_ARG=--windowed
	ECHO 将以隐藏控制台的方式打包（--windowed）。
)

REM 生成单文件 exe，名称为 qrcode_generator
pyinstaller --onefile %WINDOWED_ARG% %ICON_ARG% --name qrcode_generator qrcode_generator.py

IF %ERRORLEVEL% EQU 0 (
	ECHO.
	ECHO 打包完成。可执行文件位于 dist\qrcode_generator.exe
) ELSE (
	ECHO.
	ECHO 打包失败，错误代码 %ERRORLEVEL% 。
)

pause
