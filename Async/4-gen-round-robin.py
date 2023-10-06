def gen1(string):
    for i in string:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1("Timofei")
g2 = gen2(10)
tasks = [g1, g2]

# Round Robin
while tasks:
    task = tasks.pop(0)

    try:
        res = next(task)
        print(res)
        tasks.append(task)
    except StopIteration:
        print("Task is over")
