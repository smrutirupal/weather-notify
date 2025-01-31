from plyer import notification
import logging

logger = logging.getLogger(__name__)

def send_weather_notification(weather_data, display_options):
    try:
        if "error" in weather_data:
            message = f"❌ Error: {weather_data['error']}"
        else:
            message = []
            if display_options.get("temperature", True):
                message.append(f"🌡️ Temperature: {weather_data['temperature']}°C")
            if display_options.get("humidity", True):
                message.append(f"💧 Humidity: {weather_data['humidity']}%")
            if display_options.get("wind_speed", True):
                message.append(f"🌪️ Wind Speed: {weather_data['wind_speed']} m/s")
            message = "\n".join(message)

        notification.notify(
            title="Weather Update" if "error" not in weather_data else "Weather Error",
            message=message,
            app_name="Weather Notifier",
            timeout=10
        )
    except Exception as e:
        logger.error(f"Notification failed: {str(e)}")