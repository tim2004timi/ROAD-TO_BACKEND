from dataclasses import dataclass, field


class Vector3D:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x ** 2 + y ** 2 + z ** 2) ** 0.5


@dataclass(init=True, frozen=False, eq=True, order=True, repr=True)
class V3D:
    x: int = field(compare=False)
    y: int = field(compare=False)
    z: int = field(compare=False)
    length: float = field(init=False, repr=False)

    def __post_init__(self):
        self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


v1 = V3D(1, 2, 2)
v2 = V3D(2, 2, 1)
print(v1)
print(v2)
print(v1 == v2)
