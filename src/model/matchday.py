from attr import dataclass


@dataclass
class Matchday:
    id: int
    name: str
    sort_order: int
    series_id: int