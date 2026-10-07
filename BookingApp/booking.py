from BookingApp.exceptions import InvalidNumberOfNightsError, PropertyNotAvailableError
from BookingApp.user import User
from BookingApp.property import Property


class Booking:

    def __init__(
            self,
            booking_id: int,
            user: User,
            property: Property,
            number_of_nights: int
    ):
        self.booking_id = booking_id
        self.user = user
        self.property = property
        self.number_of_nights = number_of_nights

    def calculate_total_price(self) -> float:
        return self.property.calculate_price(self.number_of_nights)

    @property
    def number_of_nights(self) -> int:
        return self._number_of_nights

    @number_of_nights.setter
    def number_of_nights(self, value: int) -> None:
        if value <= 0:
            raise InvalidNumberOfNightsError("Invalid number of nights")
        self._number_of_nights = value

    def confirm_booking(self) -> bool:
        if self.property.available:
            self.property.set_available(False)
            return True

        raise PropertyNotAvailableError("Property not available")
