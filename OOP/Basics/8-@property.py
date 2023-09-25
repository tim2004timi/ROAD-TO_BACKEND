class Person:
    def __init__(self, name, old):
        self.__name = name
        self.old = old

    @property
    def old(self):
        print("getter")
        return self.__old

    @old.setter
    def old(self, old):
        print("setter")
        self.__old = old

    @old.deleter
    def old(self):
        print("deleter")
        del self.__old

    # old = property(get_old, set_old)


p = Person("Tim", 18)
p.old = 19
print(p.old)
print(p.__dict__)
del p.old
