from dataclasses import dataclass

from datetime import datetime

@dataclass
class Event:
    event_name: str
    event_date_time: datetime