class Cat:
    def __init__(self, name):
        self.name = name

    # для отладки
    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    # для вывода информации print, str
    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __abs__(self):
        raise TypeError("К коту нельзя применять модуль")


cat = Cat("Pooh")
print(cat)
print(len(cat))
print(abs(cat))
