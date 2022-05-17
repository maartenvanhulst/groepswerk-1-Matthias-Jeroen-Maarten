import datetime

from attr import dataclass


@dataclass
class Match:
    id: int
    date: datetime.date
    start_time: datetime.time
    home_score: int
    away_score: int
    home_alt_score: int
    away_alt_score: int
    is_forfeit_home: bool
    is_forfeit_away: bool
    is_postponed: bool
    is_canceled: bool
    away_team_id: int
    home_team_id: int
    location_id: int
    match_day_id: int
    referee_id: int