from typing import Union, Optional, Any, Final, Callable, Type


FPS: Final = 60
Digit = Union[int, float]


def multiple(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x * y


def add(x: Optional[int] = 0) -> int:
    return x + 1 if x is not None else 0


def repeat(x: Any) -> list[Any]:
    return [x, x]


def flt(func: Callable[[int], bool], lst: list[int]) -> list[int]:
    return list(filter(func, lst))


class MyClass:
    pass


def my_func(cls: Type[MyClass]) -> MyClass:
    return cls()


print(multiple(5, 6.1))
print(add())
print(repeat("Hi"))
print(flt(lambda x: x >= 0, [9, -1, 0, 3, 5]))
