# 🌦️ Weather Notify - Your Personal Weather Companion

*"Never get caught in the rain again! 🌂"*

---

## 📖 The Story

Meet **Weather Notify**, your friendly digital meteorologist that lives quietly in your system tray! Born from the frustration of constantly checking weather apps, this little helper whispers weather updates directly to your desktop. Whether you're planning a picnic 🧺, a bike ride 🚴, or just curious if you'll need an umbrella ☔, Weather Notifier has your back!

---

## 🚀 Features

- **🌍 Real-Time Weather Updates**: Get instant updates for any city worldwide  
- **🔔 Custom Notifications**: Choose what to see (temp/humidity/wind) and how often  
- **🎛️ Friendly GUI Config**: Simple settings window for non-tech users  
- **🖥️ Cross-Platform Magic**: Works on Windows & Linux (Mac coming soon!)  
- **📌 System Tray Guardian**: Runs discreetly with right-click controls  
- **⚡ Auto-Start**: Always ready when your computer boots up  
- **🔍 Smart Config Watcher**: Automatically adapts to setting changes  
- **🎻 Graceful Exit**: Disappears without a trace when asked  

---

## 🛠️ Installation Guide

### Prerequisites
- Python 3.7+ 🐍
- [OpenWeatherMap API Key](https://openweathermap.org/api) 🔑

```bash
# Clone the repository
git clone https://github.com/yourusername/weather-notify.git
cd weather-notifier

# Install dependencies
pip install -r requirements.txt

# Create environment file
echo "OPENWEATHER_API_KEY=your_api_key_here" > .env

# Add a 64x64 PNG icon named icon.png in project root
```

⚙️ Configuration
----------------

1.  **First Run Magic** ✨

    ```bash
    python main.py
    ```

    -   A friendly GUI appears automatically!

2.  **Set Your Preferences**

    -   🌆 Choose your city (e.g., "Paris" or "New York")

    -   ⏰ Pick update frequency (1-24 hours)

    -   ✅ Select weather details to display

    -   🖥️ Optionally enable auto-start

* * * * *

🕹️ Using the Notifier
----------------------

-   **System Tray Controls** (Right-click the icon):

    -   🛠️ `Open Config`: Change settings anytime

    -   🔄 `Update Now`: Get instant weather check

    -   🚪 `Exit`: Say goodbye gently

-   **Automatic Mode** 🤖

    -   Runs silently in background

    -   Notifications appear like magic!

* * * * *

🌈 Future Adventures
--------------------

Help us make Weather Notifier even better! Possible quests:

-   **Weather Alerts** ⚠️ (Rain/storm warnings)

-   **Historical Data** 📅 (24h weather graphs)

-   **Themes** 🎨 (Dark mode & custom colors)

-   **Mobile Support** 📱 (Android/iOS version)

-   **Multi-Language** 🌐 (Localization support)

-   **Weather Widget** 🖥️ (Desktop dashboard)

-   **Error Reporting** 📝 (Auto-logging system)

-   **Installation Packages** 📦 (.exe/.deb packages)

* * * * *

🙏 Acknowledgments
------------------

-   Powered by [OpenWeatherMap](https://openweathermap.org/) 🌐

-   Made possible by Python heroes:\
    `plyer` `pystray` `watchdog` `requests` `pillow`

* * * * *

📜 License
----------

Apache License 2.0 - Open, permissive, and business-friendly!\
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

*"Sunshine is delicious, rain is refreshing, but Weather Notifier? It's essential!"* ☀️🌧️