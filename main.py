import sys
import json
import time
import signal
import threading
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import pystray
from PIL import Image

from weather import get_weather
from notification import send_weather_notification
from scheduler import IntervalScheduler
from gui import run_gui

class ConfigWatcher(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback
        
    def on_modified(self, event):
        if event.src_path.endswith("config.json"):
            time.sleep(0.5)  # Allow file write to complete
            self.callback()

class WeatherNotifier:
    def __init__(self):
        self.scheduler = None
        self.tray_icon = None
        self.observer = None
        self.config = {}
        self.running = True
        self.config_lock = threading.Lock()
        self.setup_signal_handlers()

    def setup_signal_handlers(self):
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)

    def initialize(self):
        self.check_config()
        self.load_config()
        self.start_config_watcher()
        self.setup_scheduler()
        self.create_tray_icon()

    def check_config(self):
        if not Path("config.json").exists():
            run_gui()
            if not Path("config.json").exists():
                sys.exit("Configuration not saved")

    def load_config(self):
        with open("config.json") as f:
            with self.config_lock:
                self.config = json.load(f)

    def start_config_watcher(self):
        self.observer = Observer()
        self.observer.schedule(ConfigWatcher(self.reload_config), path=".")
        self.observer.start()

    def reload_config(self):
        try:
            self.load_config()
            self.restart_scheduler()
            print("Configuration reloaded")
        except Exception as e:
            print(f"Config reload failed: {e}")

    def setup_scheduler(self):
        if self.scheduler:
            self.scheduler.stop()
        interval = self.config["frequency"] * 3600
        self.scheduler = IntervalScheduler(interval, self.update_weather)
        self.scheduler.start()

    def restart_scheduler(self):
        with self.config_lock:
            self.setup_scheduler()

    def update_weather(self):
        try:
            with self.config_lock:
                city = self.config["city"]
                display_opts = self.config["display"]
            
            data = get_weather(city)
            send_weather_notification(data, display_opts)
        except Exception as e:
            print(f"Weather update failed: {e}")

    def create_tray_icon(self):
        image = Image.open("icon.png") if Path("icon.png").exists() else Image.new("RGB", (64, 64), "white")
        menu = pystray.Menu(
            pystray.MenuItem("Open Config", self.open_config),
            pystray.MenuItem("Update Now", self.update_weather),
            pystray.MenuItem("Exit", self.shutdown)
        )
        self.tray_icon = pystray.Icon("weather_notifier", image, "Weather Notifier", menu)
        threading.Thread(target=self.tray_icon.run, daemon=True).start()

    def open_config(self):
        threading.Thread(target=run_gui, daemon=True).start()

    def shutdown(self, *args):
        print("\nShutting down...")
        self.running = False
        if self.scheduler:
            self.scheduler.stop()
        if self.observer:
            self.observer.stop()
        if self.tray_icon:
            self.tray_icon.stop()
        sys.exit(0)

    def run(self):
        self.initialize()
        while self.running:
            time.sleep(1)

if __name__ == "__main__":
    notifier = WeatherNotifier()
    notifier.run()