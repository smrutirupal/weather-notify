import os
import json
import signal
import sys
from weather import get_weather
from notification import send_weather_notification
from scheduler import IntervalScheduler

class WeatherNotifier:
    def __init__(self):
        self.scheduler = None
        self.running = True
        signal.signal(signal.SIGINT, self.graceful_shutdown)
        signal.signal(signal.SIGTERM, self.graceful_shutdown)

    def check_config(self):
        if not os.path.exists("config.json"):
            from gui import run_gui
            run_gui()
            if not os.path.exists("config.json"):
                print("Configuration not saved. Exiting.")
                sys.exit(1)

    def load_config(self):
        with open("config.json", "r") as f:
            return json.load(f)

    def update_weather(self):
        try:
            config = self.load_config()
            weather_data = get_weather(config["city"])
            send_weather_notification(weather_data, config["display"])
        except Exception as e:
            print(f"Weather update failed: {e}")

    def graceful_shutdown(self, signum, frame):
        print("\nShutting down gracefully...")
        self.running = False
        if self.scheduler:
            self.scheduler.stop()
        sys.exit(0)

    def run(self):
        self.check_config()
        config = self.load_config()
        
        # Convert hours to seconds
        interval = config["frequency"] * 3600
        
        # Start scheduler
        self.scheduler = IntervalScheduler(interval, self.update_weather)
        self.scheduler.start()
        
        # Keep main thread alive
        while self.running:
            pass

if __name__ == "__main__":
    notifier = WeatherNotifier()
    notifier.run()