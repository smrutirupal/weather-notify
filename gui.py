import tkinter as tk
from tkinter import ttk, messagebox
import json
import platform
from pathlib import Path
from startup import manage_startup

DEFAULT_CONFIG = {
    "city": "London",
    "frequency": 1,
    "display": {
        "temperature": True,
        "humidity": True,
        "wind_speed": True
    },
    "startup": False
}

class ConfigGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather Notifier Config")
        self.config_path = Path("config.json")
        self.config = self.load_config()
        self.create_widgets()

    def load_config(self):
        if self.config_path.exists():
            with open(self.config_path) as f:
                return json.load(f)
        return DEFAULT_CONFIG.copy()

    def create_widgets(self):
        # City Entry
        ttk.Label(self.master, text="City:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.city_var = tk.StringVar(value=self.config["city"])
        ttk.Entry(self.master, textvariable=self.city_var).grid(row=0, column=1, padx=10, pady=5)

        # Frequency
        ttk.Label(self.master, text="Update Frequency (hours):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.freq_var = tk.IntVar(value=self.config["frequency"])
        ttk.Spinbox(self.master, from_=1, to=24, textvariable=self.freq_var).grid(row=1, column=1, padx=10, pady=5)

        # Display Options
        ttk.Label(self.master, text="Display Options:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.temp_var = tk.BooleanVar(value=self.config["display"]["temperature"])
        self.humid_var = tk.BooleanVar(value=self.config["display"]["humidity"])
        self.wind_var = tk.BooleanVar(value=self.config["display"]["wind_speed"])
        ttk.Checkbutton(self.master, text="Temperature", variable=self.temp_var).grid(row=3, column=0, padx=20, sticky="w")
        ttk.Checkbutton(self.master, text="Humidity", variable=self.humid_var).grid(row=4, column=0, padx=20, sticky="w")
        ttk.Checkbutton(self.master, text="Wind Speed", variable=self.wind_var).grid(row=5, column=0, padx=20, sticky="w")

        # Startup
        self.startup_var = tk.BooleanVar(value=self.config["startup"])
        if platform.system() in ["Windows", "Linux"]:
            ttk.Checkbutton(self.master, text="Run at Startup", variable=self.startup_var).grid(row=6, column=0, padx=10, pady=10, sticky="w")

        # Save Button
        ttk.Button(self.master, text="Save", command=self.save_config).grid(row=7, column=0, columnspan=2, pady=10)

    def save_config(self):
        new_config = {
            "city": self.city_var.get(),
            "frequency": self.freq_var.get(),
            "display": {
                "temperature": self.temp_var.get(),
                "humidity": self.humid_var.get(),
                "wind_speed": self.wind_var.get()
            },
            "startup": self.startup_var.get()
        }

        # Manage startup entry
        if new_config["startup"] != self.config["startup"]:
            action = "add" if new_config["startup"] else "remove"
            if not manage_startup(action):
                messagebox.showerror("Error", "Failed to manage startup entry!")
                return

        with open(self.config_path, "w") as f:
            json.dump(new_config, f, indent=2)

        messagebox.showinfo("Success", "Configuration saved!")
        self.master.destroy()

def run_gui():
    root = tk.Tk()
    ConfigGUI(root)
    root.mainloop()