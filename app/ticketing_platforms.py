import json
from pathlib import Path

DATA_PATH = Path("data/events.json")


def load_events():
    if not DATA_PATH.exists():
        return []
    
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def fetch_events_from_eventbrite():
    # Simulated tag
    events = load_events()
    return [e for e in events if e["id"] % 2 == 1]


def fetch_events_from_ticketmaster():
    # Simulated tag
    events = load_events()
    return [e for e in events if e["id"] % 2 == 0]
