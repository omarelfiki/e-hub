# E-Hub for Raspberry PI


## Overview

E-Hub is a Python-based software designed for a desk unit equipped with an e-ink display. It provides at-a-glance information such as weather updates and calendar events, making it ideal for productivity and organization at your workspace.

![E-Hub Dashboard](render/dashboard.png)

## Features

- **Weather Display:** Shows current weather information from configurable data providers.
- **Calendar Integration:** Displays upcoming events from your calendar.
- **Configurable:** Easily adjust settings and data sources through the `config.yaml` file.
- **E-Ink Optimized:** Designed specifically for low-power, high-contrast e-ink screens.

## Getting Started

### Prerequisites
- Python 3.8+
- Required Python packages (see `requirements.txt`)
- E-ink display hardware (tested with Waveshare models)

### Installation
1. Clone this repository:
   ```sh
   git clone <repo-url>
   cd e-hub
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Configure your settings in `config.yaml` (see below).
4. Run the main application:
   ```sh
   python main.py
   ```

## Configuration

All settings are managed through the `config.yaml` file. You can adjust:
- Weather provider and location
- Calendar source (e.g., Google Calendar, iCal)
- Display refresh intervals
- Other display preferences

## File Structure

- `main.py` — Entry point for the application
- `data_providers/` — Modules for weather and calendar data
- `render/` — Layout and rendering logic for the e-ink display
- `assets/` — Fonts and images used in the UI
- `config.yaml` — User-editable configuration file

## Roadmap

- [x] Weather display
- [x] Calendar integration
- [ ] Additional widgets (e.g., news, reminders)
- [ ] Web-based configuration UI
- [ ] Home automation integration

## Acknowledgments

- [Waveshare E-Ink Displays](https://www.waveshare.com/)
- [Python Imaging Library (Pillow)](https://python-pillow.org/)

---

*For questions or contributions, please open an issue or pull request.*
