from BookingApp.property import Property


class PropertyRepository():

    def __init__(self):
        self.properties = {}

    def save(self, property: Property) -> None:
        self.properties[property.property_id] = property

    def get_by_id(self, property_id: int) -> Property | None:
        return self.properties.get(property_id)

    def get_all(self) -> list[Property]:
        return list(self.properties.values())
