from dataclasses import dataclass


@dataclass
class Contact:
    id: int = 0
    role: str = "none"
    name: str = "none"
    email: str = "none"
    phone: str = "none"
