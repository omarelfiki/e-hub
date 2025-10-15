import time
import yaml
import logging
from data_providers.weather import get_weather
from data_providers.calendar import get_upcoming_events
from render.layout import render_display

#import for Pi
try:
    from waveshare_epd import epd4in2_V2
except ImportError:
    epd4in2_V2 = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

cfg = yaml.safe_load(open("config.yaml"))

def update_cycle(counter=0):
    logging.info("Updating display content...")
    weather = get_weather(cfg["location"]["lat"], cfg["location"]["lon"])
    events = get_upcoming_events(cfg["calendar"]["ics_url"], cfg["timezone"])
    img = render_display(
        weather,
        events,
        cfg["timezone"],
        cfg["display"]["width"],
        cfg["display"]["height"]
    )

    driver = cfg["display"].get("driver", "simulator")

    if driver == "simulator" or not epd4in2_V2:
        img.save("dashboard.png")
        logging.info("Saved dashboard.png (simulation mode).")
    elif driver == "waveshare":
        epd = epd4in2_V2.EPD()
        epd.init()
        if counter % cfg["display"]["full_refresh_every"] == 0:
            epd.Clear()
        epd.display(epd.getbuffer(img))
        epd.sleep()
        logging.info("E-ink display updated.")
    else:
        logging.warning("Unknown driver in config.yaml")

if __name__ == "__main__":
    count = 0
    while True:
        update_cycle(count)
        count += 1
        time.sleep(cfg["update_interval_minutes"] * 60)