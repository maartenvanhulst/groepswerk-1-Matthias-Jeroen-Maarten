from dataclasses import dataclass


@dataclass
class Location:
    id: int = 1
    name: str = "none"
    address_1: str = "none"
    address_2: str = "none"
    post_code: str = "none"
    city: str = "none"
    country: str = "none"
    mobile_phone: str = "none"
    fixed_phone: str = "none"
    alt_phone: str = "none"
    email_1: str = "none"
    email_2: str = "none"
    website: str = "none"
    facebook: str = "none"

