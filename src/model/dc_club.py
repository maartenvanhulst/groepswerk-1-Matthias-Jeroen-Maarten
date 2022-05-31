from dataclasses import dataclass


@dataclass
class Club:
    id: int
    name: str
    base_number: int
    address_1: str
    address_2: str
    post_code: str
    city: str
    country: str
    mobile_phone: str
    fixed_phone: str
    alt_phone: str
    email_1: str
    email_2: str
    website: str
    facebook: str
    is_active: bool