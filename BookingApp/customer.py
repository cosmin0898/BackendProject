from dataclasses import dataclass
from .user import User


@dataclass
class Customer(User):
    loyalty_points: int = 0

    def __post_init__(self):
        if self.loyalty_points < 0:
            raise ValueError('Loyalty points cannot be negative')
