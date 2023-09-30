def foo():
    try:
        x, y = map(int, input().split())
        return x, y
    except ValueError as e:
        print(e)
        return None
    finally:
        print("finally выполняется до return")


print(foo())
