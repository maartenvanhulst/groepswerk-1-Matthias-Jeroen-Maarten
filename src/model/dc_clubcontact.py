from dataclasses import dataclass


@dataclass
class ClubContact:
    id: int
    mobile_phone: str
    fixed_phone: str
    alt_phone: str
    email_1: str
    email_2: str
    first_name: str
    middle_names: str
    last_name: str
    role: str
    club_id: int
