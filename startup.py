import os
import sys
import platform
from pathlib import Path

def get_startup_path():
    system = platform.system()
    if system == "Windows":
        return Path(os.getenv('APPDATA')) / 'Microsoft' / 'Windows' / 'Start Menu' / 'Programs' / 'Startup'
    elif system == "Linux":
        return Path.home() / '.config' / 'autostart'
    raise OSError("Unsupported OS")

def manage_startup(action):
    try:
        startup_path = get_startup_path()
        startup_path.mkdir(parents=True, exist_ok=True)
        script_path = Path(sys.argv[0]).resolve()

        if platform.system() == "Windows":
            from win32com.client import Dispatch
            shortcut = startup_path / "WeatherNotifier.lnk"
            
            if action == "add":
                shell = Dispatch('WScript.Shell')
                scut = shell.CreateShortCut(str(shortcut))
                scut.Targetpath = str(script_path)
                scut.WorkingDirectory = str(script_path.parent)
                scut.save()
            elif action == "remove" and shortcut.exists():
                shortcut.unlink()

        elif platform.system() == "Linux":
            desktop = startup_path / "WeatherNotifier.desktop"
            if action == "add":
                content = f"""[Desktop Entry]
Type=Application
Name=Weather Notifier
Exec={sys.executable} {script_path}
Hidden=false
"""
                desktop.write_text(content)
                desktop.chmod(0o755)
            elif action == "remove" and desktop.exists():
                desktop.unlink()

        return True
    except Exception as e:
        print(f"Startup error: {e}")
        return False