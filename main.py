def f(text: str) -> bool:
    length = len(text)
    for i in range(length // 2):
        if text[i] != text[length - i - 1]:
            return False
    return True


assert not f("123")
assert f("121")
assert f("")
assert f("1")
assert f("1213121")
