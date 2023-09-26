class FRange:
    def __init__(self, start=0.0, end=0.0, step=1.0):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.end:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


r = FRange(end=5.0)
for i in r:
    print(i)
