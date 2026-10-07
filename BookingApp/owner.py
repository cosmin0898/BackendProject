from dataclasses import dataclass
from .user import User

@dataclass
class Owner(User):
    properties_count: int = 0

    # def __init__(self, name, user_id, email, properties_count):
    #     super().__init__(name, user_id, email)
    #     self.properties_count = properties_count

    def __post_init__(self):
        if self.properties_count < 0:
            raise ValueError("Properties count must be positive")

    def get_display_name(self):
        return f"Host: {self.name}"
