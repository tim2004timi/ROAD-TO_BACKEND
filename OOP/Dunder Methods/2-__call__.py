class Counter:
    # Классы с __call__ - функторы
    def __init__(self, count=0):
        self.__count = count

    def __call__(self, step=1, *args, **kwargs):
        self.__count += step
        print("Method __call__ | count:", self.__count)


c = Counter()
c(3)
c(2)
# -------------------------------------------


class Decorator:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        print("Before")
        res = self.__func(*args, **kwargs)
        print("After")
        return res


@Decorator
def foo(x):
    print((str(x) + " ") * 5)


foo("Tim")
# foo = Decorator(foo)
