from dataclasses import dataclass, field


class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f"Thing {self.__dict__}"


@dataclass
class ThingData:
    name: str
    weight: float
    price: int = 0
    dims: list = field(default_factory=list)

# __init__(), __repr__(), __eq__()


t = Thing("PC", 5, 30_000)
print(t)

td = ThingData("Laptop", 2)
td2 = ThingData("Phone", 0.5, 35_000)
td3 = ThingData("Phone", 0.5, 35_000)

print(td2 == td3)
print(td)
