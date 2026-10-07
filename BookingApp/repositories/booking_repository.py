from BookingApp.booking import Booking


class BookingRepository:

    def __init__(self):
        self.bookings: list[Booking] = []

    def save(self, booking: Booking) -> None:
        self.bookings.append(booking)

    def get_by_id(self, booking_id: int) -> Booking | None:
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                return booking
        return None

    def get_all(self) -> list[Booking]:
        return list(self.bookings)

    def delete(self, booking: Booking) -> None:
        self.bookings.remove(booking)
