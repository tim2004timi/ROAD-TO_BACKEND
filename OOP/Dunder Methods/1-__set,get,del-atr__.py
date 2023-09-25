class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, item, value):  # вызывается при создании аттрибута
        print(item, ":", value)
        object.__setattr__(self, item, value)

    def __getattribute__(self, item):  # вызывается при обращении к аттрибуту
        print("__getattribute__", item)
        return object.__getattribute__(self, item)

    def __getattr__(self, item):  # вызывается, если такого аттрибута нет
        print("__getattr__ такого фттрибута нет")

    def __delattr__(self, item):  # вызывается при удалении аттрибута
        object.__delattr__(self, item)


p = Point(1, 2)
print(p.x)
p.r
del p.x