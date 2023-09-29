ONE = slice(0, 3)
TWO = slice(3, 6)

word = "Python"

print(word[ONE], word[TWO])

some_list = list(range(10))
some_list[1:3] = [None, None, None]
print(some_list)

some_list[0:1] = 10,
print(some_list)
