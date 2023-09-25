class Point:
    def __init__(self, x=0, y=0):
        if self.__validate_coord(x) and self.__validate_coord(y):
            self.__x = x
            self.__y = y

    def get_coord(self):
        return self.__x, self.__y

    @staticmethod
    def __validate_coord(x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__validate_coord(x) and self.__validate_coord(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Coordinates must be integers or floats")


pt = Point(1, 2)
pt.set_coord(2, True)
print(pt.get_coord())
