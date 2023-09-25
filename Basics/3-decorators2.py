import math
from functools import wraps


def y_decorator(dx=0.001):
    def decorator(func):
        @wraps(func)  # сохранение документации и имени функции
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) -
                   func(x, *args, **kwargs)) / dx
            return res

        # wrapper.__name__ = func.__name__
        # wrapper.__doc__ = func.__doc__

        return wrapper
    return decorator


@y_decorator(dx=0.000001)
def sin(x):
    """Нахождение синуса угла в радианной мере"""
    return math.sin(x)


y = sin(0)
print(y)
print(sin.__name__, sin.__doc__)

# f = y_decorator(dx=0.0001)  можно заменить @
# sin = f(sin)
