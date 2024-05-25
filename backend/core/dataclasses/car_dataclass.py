from dataclasses import dataclass
from datetime import datetime


@dataclass
class CarDataClass:
    id: int
    seats: int
    year: int
    price: int
    body_type: str
    brand: str
    capacity: float
    image: str
    created_at: datetime
    updated_at: datetime


@dataclass
class AutoParcDataClass:
    id: int
    name: str
    cars: list[CarDataClass]
