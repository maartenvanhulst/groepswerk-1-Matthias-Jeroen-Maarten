from dataclasses import dataclass


@dataclass
class Competition:
    id: int
    name: str
    competition_type: str
    has_secondary_score: bool
    league_id: int