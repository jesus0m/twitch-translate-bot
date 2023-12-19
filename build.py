import sys
import subprocess


def build():
    os_name = sys.platform.lower()

    pyinstaller_command = ["pyinstaller"]

    if os_name.startswith("linux"):
        print("Building for Linux...")
        pyinstaller_command.extend(["--onefile", "translate-bot.py"])
        output_name = "translate-bot.bin"  # Opcional, puedes omitir la extensión
    elif os_name.startswith("darwin"):
        print("Building for macOS...")
        output_name = "translate-bot.command"
        pyinstaller_command.extend(["--onefile", "--name", output_name, "translate-bot.py"])
    elif os_name.startswith("win"):
        print("Building for Windows...")
        output_name = "translate-bot.exe"
        icon_path = "icon.ico"
        pyinstaller_command.extend(["--onefile", "--icon", icon_path, "--name", output_name, "translate-bot.py"])

    # Ejecutar PyInstaller
    subprocess.run(pyinstaller_command)


if __name__ == "__main__":
    build()
