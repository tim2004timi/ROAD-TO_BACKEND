from string import ascii_letters


class Person:
    RUS = "йцукенгшщзхъфывапролджэячсмитьбю-"
    RUS_UPPER = RUS.upper()

    def __init__(self, fio: str, old: int, height: float | str, passport: str):
        self.verify_fio(fio)
        self.__fio = fio.split()

        self.old = old

        self.height = height

        self.passport = passport

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        fio = fio.split()

        if len(fio) != 3:
            raise TypeError("Неверный формат ФИО")

        for i in fio:
            if len(i.strip(cls.RUS + cls.RUS_UPPER + ascii_letters)) != 0:
                print(i.strip(cls.RUS + cls.RUS_UPPER + ascii_letters))
                raise TypeError("ФИО состоит из недопускаемых символов")
            if len(i) < 1:
                raise TypeError("ФИО должно состоять хотя бы из одного символа")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Неверный формат возраста")

    @classmethod
    def verify_height(cls, height):
        if type(height) not in [int, float] or height < 50 or height > 300:
            raise TypeError("Неверный формат роста")

    @classmethod
    def verify_passport(cls, passport):
        if type(passport) != str:
            raise TypeError("Паспорт должен состоять из строки")

        passport = passport.split()

        if len(passport) != 2:
            raise TypeError("Неверный формат паспорта")

        if not passport[0].isdigit() or not passport[1].isdigit():
            raise TypeError("Серия, номер должны состоять из цифр")

        if len(passport[0]) != 4 or len(passport[1]) != 6:
            raise TypeError("Неверный формат серии, номера")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = float(old)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.verify_height(height)
        self.__height = height

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_passport(passport)
        self.__passport = passport


p = Person("Голубев Тимофей Александрович", 19, 185, "1234 567890")
p.old = 20
p.passport = "1230 457456"
