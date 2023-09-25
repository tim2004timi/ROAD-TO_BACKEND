class Point:
    def __new__(cls, *args, **kwargs):
        print("__new__", str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):  # также называют конструктором
        print("__init__", str(self))
        self.x = x
        self.y = y


p = Point()
print(p)
