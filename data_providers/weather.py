import requests
import logging

def get_weather(lat, lon):
    try:
        url = (
            "https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&current=temperature_2m,weathercode"
            "&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
        )
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        return {
            "temp": round(data["current"]["temperature_2m"]),
            "hi": round(data["daily"]["temperature_2m_max"][0]),
            "lo": round(data["daily"]["temperature_2m_min"][0]),
            "code": data["current"]["weathercode"]
        }
    except Exception as e:
        logging.error(f"Weather fetch failed: {e}")
        return {"temp": 0, "hi": 0, "lo": 0, "code": 0}