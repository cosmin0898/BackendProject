from fastapi import FastAPI, HTTPException
from BookingApp.hotel_room import HotelRoom
from BookingApp.schemas.property_schema import CreatePropertyRequest
from BookingApp.schemas.user_schema import CreateUserRequest
from BookingApp.schemas.booking_schema import CreateBookingRequest
from BookingApp.repositories.user_repository import UserRepository
from BookingApp.repositories.property_repository import PropertyRepository
from BookingApp.repositories.booking_repository import BookingRepository
from BookingApp.services.booking_service import BookingService
from BookingApp.apartment import Apartment
from BookingApp.user import User

app = FastAPI()

user_repository = UserRepository()
property_repository = PropertyRepository()
booking_repository = BookingRepository()
booking_service = BookingService(booking_repository)


@app.get("/users")
def get_users():
    users = []
    for user in user_repository.get_all():
        users.append({
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "active": user.active
        })
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = user_repository.get_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "user_id": user.user_id,
        "name": user.name,
        "email": user.email
    }


@app.get("/bookings")
def get_bookings():
    bookings = []
    for booking in booking_repository.get_all():
        bookings.append({
            "booking_id": booking.booking_id,
            "user_id": booking.user.user_id,
            "property_id": booking.property.property_id,
            "number_of_nights": booking.number_of_nights,
            "total_price": booking.calculate_total_price()
        })
    return bookings


@app.get("/properties")
def get_properties():
    properties = []
    for property in property_repository.get_all():
        properties.append({
            "property_id": property.property_id,
            "name": property.name,
            "price_per_night": property.price_per_night,
            "property_type": property.get_property_type(),
            "available": property.available
        })
    return properties


@app.get("/properties/{property_id}")
def get_properties(property_id: int):
    property = property_repository.get_by_id(property_id)

    if property is None:
        raise HTTPException(
            status_code=404,
            detail="Property not found"
        )

    return {
        "property_id": property.property_id,
        "name": property.name,
        "price_per_night": property.price_per_night,
        "property_type": property.get_property_type(),
        "available": property.available
    }


@app.post("/users")
def create_user(request: CreateUserRequest):
    user = User(
        request.name,
        request.user_id,
        request.email
    )

    user_repository.save(user)

    return {
        "user_id": user.user_id,
        "name": user.name,
        "email": user.email
    }


@app.post("/bookings")
def create_booking(request: CreateBookingRequest):
    user = user_repository.get_by_id(request.user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    property = property_repository.get_by_id(request.property_id)

    if property is None:
        raise HTTPException(
            status_code=404,
            detail="Property not found"
        )

    booking = booking_service.create_booking(
        request.booking_id,
        user,
        property,
        request.number_of_nights
    )

    return {
        "booking_id": booking.booking_id,
        "user_id": booking.user.user_id,
        "property_id": booking.property.property_id,
        "number_of_nights": booking.number_of_nights,
        "total_price": booking.calculate_total_price()
    }


@app.post("/properties")
def create_property(request: CreatePropertyRequest):
    if request.property_type == "apartment":
        property = Apartment(request.name,
                             request.property_id,
                             request.price_per_night,
                             True)
    elif request.property_type == "hotel_room":
        property = HotelRoom(
            request.name,
            request.property_id,
            request.price_per_night,
            True
        )
    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid property type"
        )

    property_repository.save(property)

    return {
        "property_id": property.property_id,
        "name": property.name,
        "price_per_night": property.price_per_night,
        "available": property.available,
        "property_type": property.get_property_type()
    }
