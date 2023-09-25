class Clock:
    def __init__(self, seconds: int):
        if type(seconds) != int:
            raise TypeError("Seconds must be an integer")
        self.__seconds = seconds

    def get_time(self):
        s = str(self.__seconds % 60)
        m = str(self.__seconds // 60 % 60)
        h = str(self.__seconds // 3600 % 24)

        return self.__format_time(h, m, s)

    @staticmethod
    def __format_time(s, m, h):
        return f"{s.rjust(2, '0')}:{m.rjust(2, '0')}:{h.rjust(2, '0')}"

    def __add__(self, other):
        if type(other) not in [int, Clock]:
            raise TypeError("Right operand must be an integer or a Clock")

        add_seconds = other
        if type(other) == Clock:
            add_seconds = other.__seconds

        return Clock(self.__seconds + add_seconds)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if type(other) not in [int, Clock]:
            raise TypeError("Right operand must be an integer or a Clock")

        add_seconds = other
        if type(other) == Clock:
            add_seconds = other.__seconds

        self.__seconds += add_seconds
        return self


clock = Clock(640)
clock2 = Clock(60)
clock += clock2
clock = 1 + clock
clock += 10
print(clock.get_time())

# r... - объект справа
# i... - += ну или другой операнд
