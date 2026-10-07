from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    name: str
    user_id: int
    email: str
