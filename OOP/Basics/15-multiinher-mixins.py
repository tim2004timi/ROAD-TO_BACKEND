class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("__init__ Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("__init__ MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id}: was bought at 00:00")

    def print_info(self):
        print("print_info from MixinLog")


class Laptop(Goods, MixinLog):
    def print_info(self):
        MixinLog.print_info(self)


laptop = Laptop("Acer", 1.5, 30_000)
laptop2 = Laptop("Acer", 1.5, 50_000)
laptop.print_info()
laptop.save_sell_log()
laptop2.save_sell_log()

print(Laptop.__mro__)
print(laptop.__dict__)
