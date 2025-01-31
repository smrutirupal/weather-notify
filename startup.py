import os
import sys
import winshell
from win32com.client import Dispatch

def get_shortcut_path():
    startup_folder = winshell.startup()
    return os.path.join(startup_folder, "WeatherNotifier.lnk")

def add_to_startup():
    try:
        script_path = os.path.abspath(sys.argv[0])
        shortcut_path = get_shortcut_path()
        
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = script_path
        shortcut.WorkingDirectory = os.path.dirname(script_path)
        shortcut.save()
        return True
    except Exception as e:
        print(f"Startup Error: {e}")
        return False

def remove_from_startup():
    try:
        shortcut_path = get_shortcut_path()
        if os.path.exists(shortcut_path):
            os.remove(shortcut_path)
            return True
        return False
    except Exception as e:
        print(f"Startup Removal Error: {e}")
        return False