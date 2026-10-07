from pydantic import BaseModel


class CreatePropertyRequest(BaseModel):
    property_id: int
    name: str
    price_per_night: float
    property_type: str
