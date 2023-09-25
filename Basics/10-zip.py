a = [1, 2, 3, 4, 5]
b = [True, False, False, True]
c = "Hello World"

for i in zip(a, b, c):
    print(i)

z = zip(a, b, c)
print(z)
print(next(z))
print(next(z))
print(next(z))

z1,  = z
print(z1)
