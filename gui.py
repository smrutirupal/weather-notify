import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from startup import add_to_startup, remove_from_startup

class WeatherConfigGUI:
    def __init__(self, root):
        # ... [keep previous initialization code] ...

        # Add startup status tracking
        self.current_startup_state = False
        if config:
            self.startup.set(config.get("startup", False))
            self.current_startup_state = config.get("startup", False)

    def on_save(self):
        # ... [keep previous save code] ...

        # Handle startup changes
        new_startup_state = self.startup.get()
        if new_startup_state != self.current_startup_state:
            if new_startup_state:
                if not add_to_startup():
                    messagebox.showerror("Error", "Failed to add to startup!")
            else:
                if not remove_from_startup():
                    messagebox.showerror("Error", "Failed to remove from startup!")
            self.current_startup_state = new_startup_state

        # Update config with startup state
        config["startup"] = new_startup_state
        with open("config.json", "w") as f:
            json.dump(config, f)

        messagebox.showinfo("Success", "Configuration saved!")
        self.root.destroy()