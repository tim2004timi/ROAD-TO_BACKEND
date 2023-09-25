class Point:
    color = "red"
    radius = 1
    x: int
    y: int

    def set_coords(self, x: int = 0, y: int = 0) -> None:
        print("Method: set_coords")
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


a = Point()
a.set_coords(2, 3)
print(a.get_coords())
print(a.__dict__)

