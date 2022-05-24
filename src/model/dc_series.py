from dataclasses import dataclass


@dataclass
class Series:
    id: int
    name: str
    sort_order: int
    competition_id: int