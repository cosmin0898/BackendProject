from BookingApp.user import User


class UserRepository:

    def __init__(self):
        self.users = {}

    def save(self, user: User):
        self.users[user.user_id] = user

    def get_by_id(self, user_id: int) -> User | None:
        return self.users.get(user_id)

    def get_all(self) -> list[User]:
        return list(self.users.values())
