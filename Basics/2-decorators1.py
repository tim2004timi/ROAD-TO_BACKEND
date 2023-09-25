def func_decorator(func): # декоратор

    def wrapper(*args, **kwargs): # функция обертка
        print("before")
        res = func(*args, **kwargs)
        print("after")
        return res

    return wrapper

@func_decorator
def some_func(word): # начальная фунция
    print(word)


some_func("Hi")
# some_func = func_decorator(some_func)
# some_func("Hi")
