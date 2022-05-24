from dataclasses import dataclass


@dataclass
class League:
    id: int
    name: str
    season_id: int