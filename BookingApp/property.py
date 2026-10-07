from abc import ABC, abstractmethod
from BookingApp.exceptions import PricePerNightError


class Property(ABC):
    platform_name = "StayHub"

    def __init__(self, name, property_id, price_per_night, available):
        self.name = name
        self.property_id = property_id
        self.price_per_night = price_per_night
        self.available = available

    def calculate_price(self, number_of_nights):
        return self.price_per_night * number_of_nights

    @property
    def price_per_night(self):
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        if value <= 0:
            raise PricePerNightError("Price must be greater than 0")
        self._price_per_night = value

    def set_available(self, status):
        self.available = status

    @classmethod
    def get_platform_name(cls):
        return cls.platform_name

    @abstractmethod
    def get_property_type(self):
        pass
