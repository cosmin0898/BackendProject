from pydantic import BaseModel


class CreateBookingRequest(BaseModel):
    booking_id: int
    user_id: int
    property_id: int
    number_of_nights: int
