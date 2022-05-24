import datetime
from dataclasses import dataclass


@dataclass
class Season:
    id: int
    is_active: bool
    name: str
    start_date: datetime.date
    end_date: datetime.date