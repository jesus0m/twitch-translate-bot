import platform
import sys

import PyInstaller.__main__

OS = platform.system()

if OS == 'Windows':
    PyInstaller.__main__.run([
        'translate-bot.py',
        '--clean',
        '--onefile',
        '--runtime-tmpdir=.',
        '--icon=icon.ico',
        '--exclude-module=config',
        '--name=translate-bot.exe'
    ])
elif OS == 'Darwin':
    PyInstaller.__main__.run([
        'translate-bot.py',
        '--clean',
        '--onefile',
        '--runtime-tmpdir=.',
        '--icon=icon.ico',
        '--exclude-module=config',
        '--name=translate-bot.command'
    ])
elif OS == 'Linux':
    PyInstaller.__main__.run([
        'translate-bot.py',
        '--clean',
        '--onefile',
        '--runtime-tmpdir=.',
        '--icon=icon.ico',
        '--exclude-module=config',
        '--name=translate-bot'
    ])
else:
    sys.exit(1)
