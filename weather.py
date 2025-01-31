import requests

API_KEY = "YOUR_API_KEY"

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if response.status_code != 200:
            return {"error": data.get("message", "Unknown API error")}
            
        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {str(e)}"}
    except KeyError as e:
        return {"error": f"Invalid data format: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}