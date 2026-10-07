from dataclasses import dataclass


@dataclass
class User:
    name: str
    user_id: int
    email: str
    active: bool = True

    def get_display_name(self):
        return self.name
