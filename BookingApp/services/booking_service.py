from BookingApp.booking import Booking
from BookingApp.exceptions import BookingAlreadyExistsError, BookingNotFoundError
from BookingApp.user import User
from BookingApp.property import Property
from BookingApp.repositories.booking_repository import BookingRepository


class BookingService:

    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    def create_booking(self, booking_id: int, user: User, property: Property, number_of_nights: int) -> Booking:
        if self.get_booking_by_id(booking_id) is not None:
            raise BookingAlreadyExistsError(f"Booking with id {booking_id} already exists")

        booking = Booking(
            booking_id,
            user,
            property,
            number_of_nights
        )

        booking.confirm_booking()
        self.booking_repository.save(booking)
        return booking

    def get_booking_by_id(self, booking_id: int) -> Booking | None:
        return self.booking_repository.get_by_id(booking_id)

    def cancel_booking(self, booking_id: int) -> bool:
        booking = self.get_booking_by_id(booking_id)
        if booking is not None:
            booking.property.set_available(True)
            self.booking_repository.delete(booking)
            return True
        raise BookingNotFoundError(f"Booking with id {booking_id} not found")
