from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, old):
        self.name = name
        self.old = old

    @abstractmethod
    def voice(self):
        pass

    @abstractmethod
    def run(self):
        print(self.name, "бежит на 4-ех лапах")

    def eat(self):
        print(self.name, "ест")

    def die(self):
        print(self.name, "умер")


class Cat(Animal):
    def __init__(self, name, old):
        super().__init__(name, old)

    def run(self):
        super().run()

    def voice(self):
        print("Мяу")


class Chicken(Animal):
    def __init__(self, name, old):
        super().__init__(name, old)

    def run(self):
        print(self.name, "бежит на 2-ух лапах")

    def voice(self):
        print("Ко-ко")


boris = Cat("Борис", 10)
miya = Chicken("Мия", 1)

boris.run()
boris.voice()
boris.eat()
boris.die()

miya.voice()
miya.run()
