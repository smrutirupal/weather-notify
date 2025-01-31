from plyer import notification
import logging
import platform

logger = logging.getLogger(__name__)

def send_weather_notification(weather_data, display_options):
    try:
        title = "Weather Update" if not weather_data["error"] else "Weather Error"
        message = format_message(weather_data, display_options)
        
        kwargs = {
            "title": title,
            "message": message,
            "app_name": "Weather Notifier",
            "timeout": 10
        }
        
        if platform.system() == "Linux":
            kwargs["app_icon"] = ""
            
        notification.notify(**kwargs)
    except Exception as e:
        logger.error(f"Notification failed: {str(e)}")

def format_message(weather_data, display_options):
    if weather_data["error"]:
        return f"❌ Error: {weather_data['error']}"
    
    parts = []
    if display_options.get("temperature", True):
        parts.append(f"🌡️ Temp: {weather_data['temperature']}°C")
    if display_options.get("humidity", True):
        parts.append(f"💧 Humidity: {weather_data['humidity']}%")
    if display_options.get("wind_speed", True):
        parts.append(f"🌪️ Wind: {weather_data['wind_speed']} m/s")
    
    return "\n".join(parts)