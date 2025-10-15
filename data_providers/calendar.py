import requests
from ics import Calendar
from datetime import datetime, timedelta
import pytz
import logging

def get_upcoming_events(ics_url, tz):
    try:
        text = requests.get(ics_url, timeout=10).text
        cal = Calendar(text)
        now = datetime.now(pytz.timezone(tz))
        tomorrow = now + timedelta(days=1)
        events = [
            {"time": e.begin.to('local').strftime("%H:%M"), "title": e.name}
            for e in cal.events if now <= e.begin.to('local') <= tomorrow
        ]
        return sorted(events, key=lambda x: x["time"])[:4]
    except Exception as e:
        logging.error(f"Calendar fetch failed: {e}")
        return []