from dataclasses import dataclass


@dataclass
class Team:
    id: int
    name: str
    display_name: str
    home_color_1: str
    home_color_2: str
    home_color_3: str
    away_color_1: str
    away_color_2: str
    away_color_3: str
    alt_color_1: str
    alt_color_2: str
    alt_color_3: str
    club_id: int
