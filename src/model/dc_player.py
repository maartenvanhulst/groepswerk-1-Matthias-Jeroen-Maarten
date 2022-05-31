import datetime
from dataclasses import dataclass


@dataclass
class Player:
    id: int
    first_name: str
    middle_names: str
    last_name: str
    address_1: str
    address_2: str
    post_code: str
    city: str
    country: str
    date_of_birth: datetime.date
    city_of_birth: str
    country_of_birth: str
    mobile_phone: str
    fixed_phone: str
    alt_phone: str
    email_1: str
    email_2: str
    national_identification: str
    identification: str