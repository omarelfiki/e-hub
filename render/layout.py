from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import pytz
from pathlib import Path


def render_display(weather, events, tz, width=400, height=300):
    """Create the display image (used for both simulator and hardware)."""
    img = Image.new('1', (width, height), 255)
    draw = ImageDraw.Draw(img)

    BASE = Path(__file__).resolve().parent.parent
    font_big = ImageFont.truetype(str(BASE / "assets/DejaVuSans-Bold.ttf"), 48)
    font_med = ImageFont.truetype(str(BASE / "assets/DejaVuSans.ttf"), 20)

    # Time & date
    now = datetime.now(pytz.timezone(tz))
    draw.text((10, 10), now.strftime("%H:%M"), font=font_big, fill=0)
    draw.text((10, 65), now.strftime("%A, %b %d"), font=font_med, fill=0)

    # Weather
    w = f"{weather['temp']}°C  (H:{weather['hi']}°  L:{weather['lo']}°)"
    draw.text((10, 100), w, font=font_med, fill=0)

    # Calendar
    draw.text((10, 140), "Upcoming:", font=font_med, fill=0)
    y = 170
    for ev in events:
        draw.text((20, y), f"{ev['time']}  {ev['title']}", font=font_med, fill=0)
        y += 25

    return img