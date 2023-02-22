from dataclasses import dataclass
from datetime import datetime


@dataclass
class Driver:
    category: str
    pay_km: float
    vacation: datetime
    vacation_duration: int = 7
